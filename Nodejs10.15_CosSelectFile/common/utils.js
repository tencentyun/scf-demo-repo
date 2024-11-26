/* eslint-disable no-restricted-syntax */
'use strict';

const URL = require('url');
const { pipeline } = require('stream');
const { inspect } = require('util');

/**
 * parse params from event and process.env
 */
function getParams({ Records = [] }) {
  const objects = Records.map(item => parseUrl({ url: item.cos.cosObject.url }));
  const {
    env: {
      TENCENTCLOUD_SECRETID: secretId,
      TENCENTCLOUD_SECRETKEY: secretKey,
      TENCENTCLOUD_SESSIONTOKEN: token,
      selectType = '2',
      cosSelectConfig: cosSelectConfigStr,
      targetBucket,
      targetRegion,
      targetPrefix = '',
      targetNameFormat = 'basename.cos_select_result.extname',
      localSizeLimit = `${500 * 1024 * 1024}`,
      sourceSizeLimit = `${500 * 1024 * 1024}`,
      ...args
    },
  } = process;

  let cosSelectConfig;

  const missingParams = [
    { key: 'targetBucket', value: targetBucket },
    { key: 'targetRegion', value: targetRegion },
    { key: 'cosSelectConfig', value: cosSelectConfigStr },
    { key: 'TENCENTCLOUD_SECRETID', value: secretId },
    { key: 'TENCENTCLOUD_SECRETKEY', value: secretKey },
    // { key: 'TENCENTCLOUD_SESSIONTOKEN', value: token },
  ]
    .filter(item => !item.value)
    .map(item => item.key);

  if (missingParams.length) {
    throw new Error(`params parsed error, missing params: ${missingParams.join(', ')}`);
  }

  try {
    cosSelectConfig = JSON.parse(cosSelectConfigStr);
  } catch (err) {
    throw new Error('params parsed error, cosSelectConfig is not a json string');
  }

  try {
    if (!cosSelectConfig.SelectRequest.OutputSerialization) {
      throw cosSelectConfig;
    }
  } catch (err) {
    throw new Error('params parsed error, cosSelectConfig.SelectRequest.OutputSerialization does not exist');
  }

  if (!/^[0-9]+$/.test(localSizeLimit)) {
    throw new Error('params parsed error, localSizeLimit should be positive integer');
  }

  if (!/^[0-9]+$/.test(sourceSizeLimit)) {
    throw new Error('params parsed error, sourceSizeLimit should be positive integer');
  }

  if (
    !targetNameFormat.includes('basename')
    || !targetNameFormat.includes('extname')
  ) {
    throw new Error('params parsed error, targetNameFormat should includes "basename" and "extname"');
  }

  return {
    objects,
    secretId,
    secretKey,
    token,
    targetBucket,
    targetRegion,
    targetPrefix,
    targetNameFormat,
    selectType,
    cosSelectConfig,
    localSizeLimit,
    sourceSizeLimit,
    ...args,
  };
}

/**
 * parse cos url to get the bucket, region, key message
 */
function parseUrl({ url }) {
  const { host, pathname } = URL.parse(url);
  const { 1: bucket, 2: region } = host.match(/^([^/]*)\.cos\.([^/]*)\.myqcloud\.com$/);
  return {
    bucket,
    region,
    key: decodeURIComponent(pathname.slice(1)),
  };
}

/**
 * print log message
 */
function logger({ messages = [], title = '', data = {} }) {
  const messageList = [...messages, title];
  for (const key in data) {
    const value = data[key];
    try {
      messageList.push(`${key}: ${inspect(value, { depth: 20 })}`);
    } catch (err) {
      messageList.push(`${key}: [inspect error]`);
    }
  }
  const result = `${messageList.filter(Boolean).join('\n')}`;
  console.log(`${result}\n\n`);
  return result;
}

/**
 * get log summary
 */
function getLogSummary(results) {
  let success = 0;
  let total = 0;
  const details = [];
  for (const { params, result, error } of results) {
    if (error) {
      details.push(`TaskStatus: fail, Params: ${JSON.stringify(params)}, Error: ${inspect(error, { depth: 20 })}`);
    } else {
      details.push(`TaskStatus: success, Params: ${JSON.stringify(params)}, Result: ${JSON.stringify(result)}`);
      success += 1;
    }
    total += 1;
  }
  return {
    status: success < total ? 'fail' : 'success',
    messages: [
      `Result: cos select ${
        success === total ? 'success' : 'fail'
      }, success: ${success}, total: ${total}`,
      ...details,
    ].filter(Boolean),
  };
}

/**
 * sleep logic
 */
function sleep(duration) {
  return new Promise(r => setTimeout(r, duration));
}

/**
 * get stream pipeline promise
 */
function streamPipelinePromise(streams) {
  return new Promise((resolve, reject) => {
    pipeline(streams, (err, ...args) => {
      if (err) {
        reject(err);
      } else {
        resolve(...args);
      }
    });
  });
}

/**
 * replace str's placeholder with value in map
 */
function replaceMap(str, map = {}) {
  const regxp = (Object.keys(map) || []).join('|');
  return str.replace(new RegExp(regxp, 'gm'), placeholder => map[placeholder]);
}

module.exports = {
  getParams,
  logger,
  getLogSummary,
  sleep,
  streamPipelinePromise,
  replaceMap,
};
