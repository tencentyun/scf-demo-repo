'use strict'
/**************************************************
公有云 - API网关触发云函数
参考: https://cloud.tencent.com/document/product/583/13197
***************************************************/

const pathToRegExp = require('path-to-regexp')

/**
 * 简易路由
 */
const router = {
  keys: [],
  reg: '',
  /**
   * 判断传入路径和注册路径是否匹配
   * @param {string} path 传入路径，eg: /user/100
   * @param {string} pathRes 注册路径，eg: /user/:id
   * @return {boolean}
   */
  match: function(path, pathReg) {
    const reg = pathToRegExp(pathReg, this.keys)
    this.reg = reg
    return reg.test(path)
  },
  /**
   * 注册路径
   * @param {string} path 传入路径，eg: /user/100
   * @param {string} pathRes 注册路径，eg: /user/:id
   * @param {function} cb 传入路径与注册路径匹配时执行的回调
   * @return {boolean}
   */
  captures: function(path, pathReg, cb) {
    if (this.match(path, pathReg)) {
      const extractArr = path.match(this.reg).slice(1)
      let event = {}
      extractArr.forEach((item, index) => {
        event[this.keys[index].name] = item
      })
      cb && cb(path, event)
    } else {
      throw Error(`路由器传入路径(${path})和注册路径(${pathReg})不匹配`)
    }
  }
}

exports.main_handler = (event, context, callback) => {
  const { path } = event

  router.captures(path, '/article/:articleId', (path, params) => {
    console.log(`当前请求路径为: ${path}`)
    console.log(`命中的注册路径的参数: ${JSON.stringify(params)}`)
    callback(null, params)
  })
}
