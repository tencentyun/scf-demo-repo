/**************************************************
公有云 - 操作Credis
相关文档
1、https://www.npmjs.com/package/ioredis - redis客户端相关接口
***************************************************/

const redis = require("ioredis");

exports.main_handler = async (event, context, callback) => {
  const redisStore = new redis({
    port: 6379, // redis实例端口
    host: "", // redis实例host
    family: 4,
    password: "", // redis实例密码
    db: 0
  });
  // return "Success";
  redisStore.set('foo', 'bar');
  
  let result = await new Promise((res, rej) => {
    redisStore.get('foo', function (err, result) {
      if (err) {
        rej(err)
      }

      res(result)
    });
  })
  
  return result
};
