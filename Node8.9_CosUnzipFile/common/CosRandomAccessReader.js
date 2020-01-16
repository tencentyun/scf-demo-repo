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
    totalSize = 0,
    localFdSlicer = null,
    localSizeLimit = 400 * 1024 * 1024,
    localPath = '/tmp/temp.zip'
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
      totalSize,
      localFdSlicer,
      localSizeLimit,
      localPath
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
    } catch (error) {
      throw {
        error,
        trace: 'CosRandomAccessReader.cosInstance.headObjectPromise'
      }
    }

    if (this.totalSize <= localSizeLimit) {
      try {
        await cosInstance.getObjectPromise({
          Bucket,
          Region,
          Key,
          Output: fs.createWriteStream(localPath)
        })
      } catch (error) {
        throw {
          error,
          trace: 'CosRandomAccessReader.cosInstance.getObjectPromise'
        }
      }

      try {
        await this.getFdSlicer()
      } catch (error) {
        throw {
          error,
          trace: 'CosRandomAccessReader.getFdSlicer'
        }
      }
    }
    return this.totalSize
  }

  getFdSlicer() {
    return new Promise((resolve, reject) => {
      fs.open(this.localPath, 'r', (err, fd) => {
        if (err) {
          reject(err)
        } else {
          this.localFdSlicer = FdSlicer.createFromFd(fd)
          resolve()
        }
      })
    })
  }

  getRangeStream({ start, end }) {
    if (this.localFdSlicer) {
      return this.localFdSlicer.createReadStream({ start, end })
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