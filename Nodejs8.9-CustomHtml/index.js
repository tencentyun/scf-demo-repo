const fs = require('fs')
const path = require('path')
const render = require('./render')

exports.main_handler = async (event, callback, context) => {
  let html = fs.readFileSync(path.resolve(__dirname, './index.html'), {
    encoding: 'utf-8'
  })
  html = render(html, {
    master: '腾讯云云函数团队', // 您的名称
    centralCouplet: '年年有余', // 横批
    upCouplet: '千年迎新春', // 上联
    downCouplet: '瑞雪兆丰年' // 下联
  })
  return {
    isBase64Encoded: false,
    statusCode: 200,
    headers: { 'Content-Type': 'text/html' },
    body: html
  }
}
