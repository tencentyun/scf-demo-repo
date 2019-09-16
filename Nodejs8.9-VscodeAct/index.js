const fs = require('fs')
const path = require('path')
const render = require('./render')

exports.main_handler = async (event, context,callback ) => {
  let html = fs.readFileSync(path.resolve(__dirname, './demo.html'), {
    encoding: 'utf-8'
  })
  html = render(html, {
    appropriate:"奋发向上", // 适宜
    avoid: "懒惰消极", // 避免
    from: "超级无敌美少女" // 您的姓名/昵称
  })
  return {
    isBase64Encoded: false,
    statusCode: 200,
    headers: { 'Content-Type': 'text/html' },
    body: html
  }
}
