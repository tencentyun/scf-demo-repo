/**************************************************
Node8.9_OperateRedis
Reference:
1、https://www.npmjs.com/package/ioredis - redis interfaces
***************************************************/

const redis = require("ioredis");

exports.main_handler = async (event, context, callback) => {
  const redisStore = new redis({
    port: 6379, // Redis instance port, redis實例端口
    host: "", // Redis instance host, redis實例host
    family: 4,
    password: "", // Redis instance password, redis實例密碼
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