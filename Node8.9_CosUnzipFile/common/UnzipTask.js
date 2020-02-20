const path = require('path')
const TaskManager = require('./TaskManager')
const UnzipFile = require('./UnzipFile')
const { parseFileName, getBatchLimit } = require('./utils')
const { extend } = require('lodash')

const GB = 1024 * 1024 * 1024
const PUT_OBJECT_LIMIT = 5 * GB

class UnzipTask {
  constructor({
    cosInstance,
    totalMem,
    Bucket,
    Region,
    Key,
    targetBucket,
    targetRegion,
    targetPrefix,
    maxTryTime = 3
  }) {
    const { basename, extname } = parseFileName(Key)
    extend(this, {
      cosInstance,
      totalMem,
      Bucket,
      Region,
      Key,
      targetBucket,
      targetRegion,
      targetPrefix,
      maxTryTime,
      basename,
      extname
    })
  }

  async initTaskManager() {
    if (this.taskManager && this.unzipFile) {
      return
    }

    const { cosInstance, totalMem, Bucket, Region, Key, maxTryTime } = this

    const batchLimit = getBatchLimit({
      runtimeBuffer: 10 * 1024 * 1024,
      reserveRate: 0.2,
      totalMem
    })

    const unzipFile = this.unzipFile = new UnzipFile({ cosInstance, Bucket, Region, Key, maxTryTime })

    await unzipFile.init()

    let entries, list

    try {
      entries = await unzipFile.getEntries()
      console.log(`zip file entries count is ${entries.length}`)
      list = entries.map(entry => ({ entry }))
    } catch (error) {
      throw {
        error,
        trace: 'UnzipTask.unzipFile.getEntries'
      }
    }

    this.taskManager = new TaskManager({
      batchLimit,
      list,
      onStart: async ({ task, onFinish }) => {
        if (task.entry.uncompressedSize > PUT_OBJECT_LIMIT) {
          onFinish({ error: `single sub file can not larger than ${PUT_OBJECT_LIMIT / GB} GB` })
          return
        }
        try {
          await this.unzipOneTask({ task, onFinish })
        } catch (error) {
          onFinish(error)
        }
      },
      onCancel(task) {
      }
    })
  }

  async unzipOneTask({ task, onFinish, tryTime = 1 }) {
    const {
      cosInstance,
      targetBucket,
      targetRegion,
      targetPrefix,
      basename,
      unzipFile,
      maxTryTime
    } = this

    const Key = path.join(targetPrefix, basename, task.entry.fileNameStr).replace(/\\/g, '\/')

    const Body = await unzipFile.getStream(task.entry)

    cosInstance.putObject({
      Bucket: targetBucket,
      Region: targetRegion,
      Key,
      Body
    }, (err, ...args) => {
      if (err && tryTime < maxTryTime) {
        process.nextTick(() => {
          this.unzipOneTask({
            task,
            onFinish,
            tryTime: tryTime + 1
          })
        })
      } else {
        const error = err ? {
          error: err,
          Key,
          trace: 'UnzipFile.cosInstance.putObject'
        }: null
        onFinish(error, ...args)
      }
    })
  }

  async run() {
    const { Key, extname } = this
    if (extname !== '.zip') {
      throw { error: `${Key} is not a *.zip file` }
    }
    await this.initTaskManager()
    const result = await this.taskManager.startPromise()
    return result
  }

  cancel() {
    this.taskManager && this.taskManager.cancel()
    this.unzipFile && this.unzipFile.close()
  }
}

module.exports = UnzipTask