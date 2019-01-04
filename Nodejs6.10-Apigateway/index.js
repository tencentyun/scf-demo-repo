'use strict'
/**************************************************
公有云 - API网关触发云函数
***************************************************/

exports.main_handler = (event, context, callback) => {
  const { requestContext } = event

  return {
    isBase64Encoded: 'False',
    statusCode: 200,
    headers: { 'Content-Type': 'text/html' },
    body: requestContext ? 'API GW Test' : 'event is not come from api gateway'
  }
}
