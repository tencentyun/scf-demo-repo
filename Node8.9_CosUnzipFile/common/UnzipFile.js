const yauzl = require('yauzl')
const CosRandomAccessReader = require('./CosRandomAccessReader')
const { extend, noop } = require('lodash')
const { bufferToString } = require('./utils')

class UnzipFile {
  constructor({
    cosInstance,
    Bucket,
    Region,
    Key,
    zipFile = null,
    maxTryTime = 3
  }) {
    extend(this, {
      cosInstance,
      Bucket,
      Region,
      Key,
      zipFile,
      maxTryTime
    })
  }

  init({
    lazyEntries = true,
    autoClose = false,
    decodeStrings = false
  } = {}) {
    return new Promise(async (resolve, reject) => {
      const { cosInstance, Bucket, Region, Key } = this
      const reader = new CosRandomAccessReader({ cosInstance, Bucket, Region, Key })
      let totalSize = 0

      try {
        totalSize = await reader.getTotalSize()
      } catch (err) {
        reject(err)
        return
      }

      yauzl.fromRandomAccessReader(reader, totalSize, {
        lazyEntries,
        autoClose,
        decodeStrings
      }, (error, zipFile) => {
        if (error) {
          reject({
            error,
            trace: 'UnzipFile.init.yauzl.fromRandomAccessReader'
          })
        } else {
          this.zipFile = zipFile
          resolve(this.zipFile)
        }
      })
    })
  }

  getEntries() {
    return new Promise((resolve, reject) => {
      let tryTime = 0, entries = []

      this.zipFile.on('entry', entry => {
        tryTime = 0
        entry.fileNameStr = bufferToString(entry.fileName)
        entries.push(entry)
        if (this.zipFile.isOpen) {
          this.zipFile.readEntry()
        } else {
          reject()
        }
      })

      this.zipFile.on('end', () => {
        this.zipFile.on('error', noop)
        resolve(entries)
      })

      this.zipFile.on('error', err => {
        tryTime ++
        if (tryTime >= this.maxTryTime) {
          reject(err)
        } else {
          this.zipFile.readEntry()
        }
      })

      this.zipFile.readEntry()
    })
  }

  getStream(entry) {
    return new Promise((resolve, reject) => {
      if (/\/$/.test(entry.fileNameStr)) {
        process.nextTick(() => {
          resolve(Buffer.from(''))
        })
        return
      }
      this.zipFile.openReadStream(entry, (err, stream) => {
        if (!this.zipFile.isOpen) {
          reject()
          return
        }
        if (err) {
          reject(err)
        } else {
          resolve(stream)
        }
      })
    })
  }

  close() {
    if (this.zipFile && this.zipFile.isOpen) {
      this.zipFile.on('error', noop)
      this.zipFile.close()
    }
  }
}

module.exports = UnzipFile