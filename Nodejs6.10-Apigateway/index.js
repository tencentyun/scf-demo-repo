'use strict'
/**************************************************
公有云 - API网关触发云函数
***************************************************/

exports.main_handler = (event, context, callback) => {
  console.log('start main handler')

  const body = 'API GW Test Success'

  return {
        "isBase64": false,
        "statusCode": 200,
        "headers": {"Content-Type": "text", "Access-Control-Allow-Origin": "*"},
        "body": body
    }
}
