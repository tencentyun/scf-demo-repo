'use strict'
/**************************************************
公有云 - 图片压缩
Tips: 调用腾讯云数据万象接口对图片进行压缩，参考: https://cloud.tencent.com/document/product/460/6925
***************************************************/

const path = require('path')

exports.main_handler = async (event, context, callback) => {
  let { Records } = event
  const quality = '80'
  let url

  if (Records) {
    url = Records[0].cos.cosObject.url
  }

  const compressedUrl = path.join(url + '?imageMogr2/rquality/', quality)

  console.log('入参:', event)
  console.log('图片地址:', url)
  console.log('图片压缩比:', quality)
  console.log('压缩后图片地址:', compressedUrl)

  return compressedUrl
}
