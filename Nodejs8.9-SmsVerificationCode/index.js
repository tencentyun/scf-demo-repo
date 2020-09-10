
/**************************************************
* 功能：1.發送簡訊 2.登入（校驗簡訊驗證碼）
* 函數運作的前提條件： 
1.創模組化板函數後，請先添加函數運作角色，并給該角色關聯簡訊QcloudSMSFullAccess權限。
2.本服務用到redis儲存驗證碼，請先申請redis資源，并将redis的host和密碼設置成環境變量。
3.去雲簡訊控制台申請簡訊範本和簽名
* 詳細請參考：https://github.com/taifucloudyun/scf-demo-repo/tree/master/Nodejs8.9-SmsVerificationCode
***************************************************/

'use strict';
const redis = require('ioredis');
const taifucloudcloud = require('taifucloudcloud-sdk-nodejs');
const queryParse = require('querystring')
const expireTime = 5 * 60;//驗證碼有效期5分鍾

exports.main_handler = async (event, context, callback) => {
  let queryString = event.queryString // get形式
  if(event.httpMethod === "POST") { // post形式
    queryString = queryParse.parse(event.body)
  }
  
  if(!queryString || !queryString.method || !queryString.phone) {
    return {
      codeStr: 'InValidParam',
      msg: "缺少參數"
    }
  }
  const redisStore = new redis({
    port: 6369, // Redis instance port, redis實例端口
    host: process.env.REDIS_HOST, // Redis instance host, redis實例host
    family: 4,
    password: process.env.REDIS_PASSWORD, // Redis instance password, redis實例密碼
    db: 0
  });
  if(queryString.method === "getSms") {
    return await getSms(queryString, redisStore)
  } else if(queryString.method === "login") {
    return await loginSms(queryString, redisStore)
  }
}

/*
* 功能：登入，校驗驗證碼
*/
async function loginSms(queryString, redisStore) {
  if(!queryString.code) {
    return {
        codeStr: 'MissingCode',
        errorMessage: "缺少驗證碼參數"
    }
  }
  const redisResult = await redisPromise(redisStore, queryString)
  if(!redisResult) {//沒有找到記錄
    return {
      codeStr: 'CodeHasExpired',
      msg: "驗證碼已過期"
    }
  }
  let result = JSON.parse(redisResult)
  
  if(!result || result.used || result.num >= 3) {
    return {
      codeStr: 'CodeHasValid',
      msg: "驗證碼已失效"
    }
  }
  
  if(result.code == queryString.code) { //驗證碼校驗正确
    updateRedis(redisStore, queryString.phone, result, true) //将驗證碼更新爲已使用
    // 驗證碼校驗通過，執行登入邏輯
    console.log('校驗驗證碼成功')
    return {
      codeStr: 'Success',
      msg: '校驗驗證碼成功'
    }
  } else { // 驗證碼校驗失敗
    updateRedis(redisStore, queryString.phone, result, false)
    return {
      codeStr: 'CodeIsError',
      msg: "請檢查手機号和驗證碼是否正确"
    }
  }
}
// 更新redis狀态
function updateRedis(redisStore, phone, result, used) {
  const sessionCode = {
    code: result.code,
    sessionId: result.sessionId,
    num: ++result.num, //驗證次數，最多可驗證3次
    used: used //true-已使用，false-未使用
  }
  redisStore.set('sms_' + phone, JSON.stringify(sessionCode));
  if(used) {
    redisStore.expire('sms_' + phone, 0);
  } else {
    redisStore.expire('sms_' + phone, expireTime);
  }
}
/*
 * 功能：根據手機号獲取簡訊驗證碼
 */
async function getSms(queryString, redisStore) {
  const code = Math.random().toString().slice(-6);//生成6位數随機驗證碼
  const sessionCode = {
      code: code,
      num: 0, //驗證次數，最多可驗證3次
      used: false //false-未使用，true-已使用
  }
  redisStore.set('sms_' + queryString.phone, JSON.stringify(sessionCode));
  redisStore.expire('sms_' + queryString.phone, expireTime);

  let queryResult = await sendSms(queryString.phone, code)
  return queryResult
}
/*
 * 功能：通過sdk調用簡訊api發送簡訊
 * 參數 手機号、簡訊驗證碼
 */
async function sendSms(phone, code) {
  const SmsClient = taifucloudcloud.sms.v20190711.Client;
  const Credential = taifucloudcloud.common.Credential;
  const ClientProfile = taifucloudcloud.common.ClientProfile;
  const HttpProfile = taifucloudcloud.common.HttpProfile;
  const secretId = process.env.TENCENTCLOUD_SECRETID;
  const secretKey = process.env.TENCENTCLOUD_SECRETKEY;
  const token = process.env.TENCENTCLOUD_SESSIONTOKEN;

  let cred = new Credential(secretId, secretKey, token);
  let httpProfile = new HttpProfile();
  httpProfile.endpoint = "sms.taifucloudcloudapi.com";
  let clientProfile = new ClientProfile();
  clientProfile.httpProfile = httpProfile;
  let client = new SmsClient(cred, "ap-guangzhou", clientProfile);

  let req = {
      PhoneNumberSet: ["+" + phone], //大陸手機号861856624****
      TemplateID: process.env.SMS_TEMPLATE_ID, //Top Cloud 簡訊範本id
      Sign: process.env.SMS_SIGN, //Top Cloud 簡訊簽名
      TemplateParamSet: [code],
      SmsSdkAppid: process.env.SMS_SDKAPPID //簡訊應用id
  }
  
  let queryResult = await smsPromise(client, req)
  return queryResult
}

async function smsPromise(client, req) {
  return new Promise((resolve, reject) => {
      client.SendSms(req, function(errMsg, response) {
          if (errMsg) {
              reject(errMsg)
          } else {
              if(response.SendStatusSet && response.SendStatusSet[0] && response.SendStatusSet[0].Code === "Ok") {
                  resolve({
                      codeStr: response.SendStatusSet[0].Code,
                      msg: response.SendStatusSet[0].Message
                  })
              } else {
                  resolve({
                      codeStr: response.SendStatusSet[0].Code,
                      msg: response.SendStatusSet[0].Message
                  })
              }
          }                
      });
  })
}

async function redisPromise(redisStore, queryString) {
  return new Promise((res, rej) => {
    redisStore.get('sms_' + queryString.phone, function (err, result) {
      if (err) {
        rej(err)
      }
      res(result)
    });
  })
}