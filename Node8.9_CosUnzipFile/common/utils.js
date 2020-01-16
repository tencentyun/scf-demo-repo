'use strict'

const COS = require('cos-nodejs-sdk-v5')
const path = require('path')
const URL = require('url')
const os = require('os')
const jschardet = require('jschardet')
const legacy = require('legacy-encoding')
const { promisify } = require('util')
const { isFunction, isString, isObject } = require('lodash')

const ERROR_TRACE_MAP = {
  'CosRandomAccessReader.cosInstance.headObjectPromise': 'zip file head object fail',
  'CosRandomAccessReader.cosInstance.getObjectPromise': 'zip file get object fail',
  'CosRandomAccessReader.getFdSlicer': 'zip file get file descriptor fail',
  'UnzipFile.cosInstance.putObject': 'sub file put object fail',
  'UnzipFile.init.yauzl.fromRandomAccessReader': 'zip file parse error, it may be broken',
  'UnzipTask.unzipFile.getEntries': 'zip file get sub file entry fail'
}

/**
 * get source and target message from event and process.env 
 */
function getParams({
  Records = []
}) {
  const objectList = Records.map(item => {
    return parseUrl({
      url: item.cos.cosObject.url
    })
  })
  const {
    env: {
      targetBucket,
      targetRegion,
      targetPrefix,
      TENCENTCLOUD_SECRETID: SecretId,
      TENCENTCLOUD_SECRETKEY: SecretKey,
      TENCENTCLOUD_SESSIONTOKEN: XCosSecurityToken
    }
  } = process

  return {
    objectList,
    targetBucket,
    targetRegion,
    targetPrefix,
    SecretId,
    SecretKey,
    XCosSecurityToken
  }
}

/**
 * parse cos url to get the Bucket, Region, Key message
 */
function parseUrl({ url }) {
  const { host, pathname } = URL.parse(url)
  const { 1: Bucket, 2: Region } = host.match(/^([^\/]*)\.cos\.([^\/]*)\.myqcloud\.com$/)
  return {
    Bucket,
    Region,
    Key: decodeURIComponent(pathname.slice(1))
  }
}

/**
 * init cos-nodejs-sdk-v5 instance，append promisify methods
 */
function initCosInstance({ SecretId, SecretKey, XCosSecurityToken, ...args }) {
  const cosInstance = new COS({
    SecretId,
    SecretKey,
    XCosSecurityToken,
    ...args
  })
  const keys = Object.keys(COS.prototype)
  for (let key of keys) {
    const value = cosInstance[key]
    if (isFunction(value)) {
      cosInstance[`${key}Promise`] = promisify(value)
    }
  }
  return cosInstance
}

/**
 * calculate the unzip-task batch limit according to the memory limit
 */
function getBatchLimit({
  runtimeBuffer = 10 * 1024 * 1024,
  reserveBuffer = 0,
  reserveRate = 0
}) {
  reserveBuffer = reserveBuffer || reserveRate * os.totalmem()
  return Math.floor((os.freemem() - reserveBuffer) / runtimeBuffer)
}

/**
 * try to decode buffer by jschardet encoding or gb2312
 */
function bufferToString(buffer) {
  const testBuffer = getExactSizeBuffer({ buffer, size: 200 })
  const { encoding, confidence } = jschardet.detect(testBuffer)
  if (confidence > 0.8) {
    return legacy.decode(buffer, encoding)
  } else {
    return legacy.decode(buffer, 'gb2312')
  }
}

/**
 * create a new buffer with exact size
 * if buffer.length is shorter than size，copy the buffer multiple times to fulfill it
 */
function getExactSizeBuffer({ buffer, size }) {
  const copyTimes = Math.ceil(size / buffer.length)
  const bufferList = Array(copyTimes).fill(buffer)
  return Buffer.concat(bufferList, size)
}

/**
 * get file basename and extname
 */
function parseFileName(fileName) {
  const extname = path.extname(fileName)
  const basename = path.basename(fileName, extname)
  return {
    basename,
    extname
  }
}

/**
 * get unzip task name
 */
function getTaskName({ Bucket, Region, Key }) {
  return `${Bucket}.cos.${Region}.myqcloud.com/${Key}`
}

/**
 * get fail reason
 */
function getReason(error) {
  if (error === 'isTimeout') {
    return 'serverless cloud function timeout'
  } else if (isString(error)) {
    return error
  } else if (error.trace) {
    const { trace, Key } = error
    return `${ERROR_TRACE_MAP[trace] || trace} ${Key ? `(Key: ${Key})` : ''}`
  } else if (isString(error.error)) {
    return error.error
  } else {
    return ''
  }
}

/**
 * get error logs
 */
function getLogs(err) {
  const cosLogs = getCosLogs(err)
  const otherLogs = getOtherLogs(err)
  return cosLogs.length ? cosLogs : otherLogs
}

/**
 * get cos error logs
 */
function getCosLogs(err) {
  if (!isObject(err)) {
    return []
  }
  if (err && err.error && err.error.statusCode) {
    err = err.error
  }
  const { headers, statusCode, error } = err

  if (!headers || !statusCode) {
    return []
  }
  try {
    const { Code, Message } = isString(error) ? { Code: error } : error
    return [
      `StatusCode: ${statusCode}`,
      `Code: ${Code}`,
      `Message: ${Message}`,
      `RequestId: ${headers['x-cos-request-id']}`,
      `TraceId: ${headers['x-cos-trace-id']}`
    ]
  } catch (err) {
    return []
  }
}

/**
 * get other error logs
 */
function getOtherLogs(err) {
  try {
    if (err === 'isTimeout' || (err.error && err.error === 'single sub file can not larger than 5 GB')) {
      return []
    } else if (isString(err)) {
      return [err]
    } else {
      return [JSON.stringify(err)]
    }
  } catch (e) {
    if (err && err.toString) {
      return [err.toString()]
    } else {
      return []
    }
  }
}

/**
 * print log message
 */
function logger({ title = '', content = '', data = {}, print = true }) {
  const message = []
  message.push(title, content)
  for (let key in data) {
    const value = data[key]
    if (isString(value)) {
      message.push(`${key}: ${value}`)
    } else {
      try {
        message.push(`${key}: ${JSON.stringify(value)}`)
      } catch (err) {
      }
    }
  }
  const result = `${message.filter(Boolean).join('\n')}`
  if (print) {
    console.log(result)
  }
  return result
}

module.exports = {
  getParams,
  initCosInstance,
  getBatchLimit,
  bufferToString,
  parseFileName,
  getTaskName,
  getReason,
  getLogs,
  logger
}