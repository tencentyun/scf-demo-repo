const request = require('request')
const fs = require('fs')
const FdSlicer = require('fd-slicer')
const { RandomAccessReader } = require('yauzl')
const { extend } = require('lodash')

class CosRandomAccessReader extends RandomAccessReader {
  constructor({
    cosInstance,
    Bucket,
    Region,
    Key,
    Expires = 900 * 1000,
    Sign = true,
    requestTimeout = 900 * 1000,

    localSizeLimit = 450 * 1024 * 1024,

    totalSize = 0,
    localFdSlicer = null,
    localPath = '/tmp/temp.zip',

    centralDirSize = 0,
    centralDirStart = 0,
    localCentralDirFdSlicer = null,
    localCentralDirPath = '/tmp/temp_central_dir.zip'
  }) {
    super()
    const objectUrl = cosInstance.getObjectUrl({
      Bucket,
      Region,
      Key,
      Expires,
      Sign
    })
    extend(this, {
      cosInstance,
      Bucket,
      Region,
      Key,
      objectUrl,
      requestTimeout,

      localSizeLimit,

      totalSize,
      localFdSlicer,
      localPath,

      centralDirSize,
      centralDirStart,
      localCentralDirFdSlicer,
      localCentralDirPath
    })
  }

  async getTotalSize() {
    const {
      cosInstance,
      Bucket,
      Region,
      Key,
      localSizeLimit,
      localPath
    } = this

    try {
      const { headers } = await cosInstance.headObjectPromise({ Bucket, Region, Key })
      this.totalSize = headers['content-length'] * 1
      console.log(`whole zip file size is ${this.totalSize}`)
    } catch (error) {
      throw {
        error,
        trace: 'CosRandomAccessReader.cosInstance.headObjectPromise'
      }
    }

    if (this.totalSize <= localSizeLimit) {
      await this.downloadFileAndInitSlicer({
        filePath: localPath,
        fdSlicerKey: 'localFdSlicer'
      })
      console.log(`whole zip file is downloaded, size is ${this.totalSize}`)
    }
    return this.totalSize
  }

  /**
   * try to download zip file central directory
   * try to init central directory fdSlicer
   */
  async initCentralDir({ centralDirStart }) {
    this.centralDirStart = centralDirStart
    this.centralDirSize = this.totalSize - centralDirStart

    if (!this.localFdSlicer && this.centralDirSize <= this.localSizeLimit) {
      await this.downloadFileAndInitSlicer({
        headers: {
          Range: `bytes=${this.centralDirStart}-`
        },
        filePath: this.localCentralDirPath,
        fdSlicerKey: 'localCentralDirFdSlicer'
      })
      console.log(`zip file central directory is downloaded, size is ${this.centralDirSize}`)
    }
  }

  // download file to local disk and init the fdSlicer
  async downloadFileAndInitSlicer({
    filePath,
    fdSlicerKey,
    headers = {}
  }) {
    const {
      cosInstance,
      Bucket,
      Region,
      Key
    } = this
    try {
      await cosInstance.getObjectPromise({
        Bucket,
        Region,
        Key,
        Headers: headers,
        Output: fs.createWriteStream(filePath)
      })
    } catch (error) {
      throw {
        error,
        trace: 'CosRandomAccessReader.cosInstance.getObjectPromise'
      }
    }

    try {
      this[fdSlicerKey] = await this.getFdSlicer({ filePath })
    } catch (error) {
      throw {
        error,
        trace: 'CosRandomAccessReader.getFdSlicer'
      }
    }
  }

  getFdSlicer({ filePath }) {
    return new Promise((resolve, reject) => {
      fs.open(filePath, 'r', (err, fd) => {
        if (err) {
          reject(err)
        } else {
          resolve(FdSlicer.createFromFd(fd))
        }
      })
    })
  }

  /**
   * if the whole file is downloaded, read it from disk
   * else if the central directory is downloaded, and now is trying to read sub file meta data, read it from disk
   * else read it from request
   */
  getRangeStream({ start, end }) {
    if (this.localFdSlicer) {
      return this.localFdSlicer.createReadStream({ start, end })
    } else if (this.localCentralDirFdSlicer && start >= this.centralDirStart) {
      return this.localCentralDirFdSlicer.createReadStream({
        start: start - this.centralDirStart,
        end: end - this.centralDirStart
      })
    } else {
      return request({
        url: this.objectUrl,
        timeout: this.requestTimeout,
        headers: {
          Range: `bytes=${start}-${end - 1}`
        }
      })
    }
  }

  _readStreamForRange(start, end) {
    return this.getRangeStream({ start, end })
  }
}

module.exports = CosRandomAccessReader