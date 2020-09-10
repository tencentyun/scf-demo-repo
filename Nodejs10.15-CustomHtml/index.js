/*************************************************************************
*****                                                                *****
*****    使用教程/readme ：                                            *****
*****    https://cloud.tencent.com/document/product/583/32996        *****
*****                                                                *****
**************************************************************************/
const fs = require('fs')
const path = require('path')
const render = require('./render')

exports.main_handler = async (event, context,callback ) => {
  let html = fs.readFileSync(path.resolve(__dirname, './demo.html'), {
    encoding: 'utf-8'
  })
  html = render(html, {
    master: 'Top Cloud 雲函數團隊', // Your name 您的名稱
    centralCouplet: '年年有餘', // centralCouplet 橫批
    upCouplet: '千年迎新春', // upCouplet 上聯
    downCouplet: '瑞雪兆豐年' // downCouplet 下聯
  })
  return {
    isBase64Encoded: false,
    statusCode: 200,
    headers: { 'Content-Type': 'text/html' },
    body: html
  }
}