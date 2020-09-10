/**************************************************
Nodejs8.9-AutomatedTesting
TIPS:
1. There is no CMQ SDK for node
   CMQ暫時沒有node版本的SDK

Reference: 
1. https://cloud.tencent.com/document/product/583/19504 - Function test（python）
2. https://cloud.tencent.com/document/product/406/5851 - CMQ interface files
***************************************************/

const Capi = require('qcloudapi-sdk')
const request = require('request')

// The cmq authentication information
// 使用 cmq 所需的鑒權/配置訊息
const SECRET_ID = 'xxx' // Replace it with your SecretId , 請替換爲您的 SecretId
const SECRET_KEY = 'xxx' // Replace it with your SecretKey, 請替換爲您的 SecretKey
const CMQ_TOPIC_NAME = 'CMQ_TOPIC_NAME' // Replace it with your Topic name, 請替換爲您的 Topic 名稱
const CMQ_REGION = 'gz' // The region of your cmq topic, cmq主題所在地域

// While fails, the email notify list
// 撥測失敗後，告警郵件需要通知的電子信箱清單
const EMAIL_NOTIFY_LIST = ['******@qq.com', '******@qq.com']

// While fails, the email sending the error message, please replace it with your own email address
// 撥測失敗後，發出告警郵件的電子信箱，請根據您自身設置的電子信箱網址進行修改
const FROM_ADDR = '******@qq.com'

// The test url list
// 撥測網址清單
const TEST_URL_LIST = ['http://wrong.tencent.com', 'http://www.qq.com']

/**Simple CMQ-SDK */
function CMQRequestHelper(SecretId, SecretKey) {
  // Generate the CMQ api
  // CMQ雲api構建
  this.requestHelper = new Capi({
    SecretId,
    SecretKey,
    serviceType: `cmq-topic-${CMQ_REGION}`
  })
  this.inited = true
}
CMQRequestHelper.prototype.publishMessage = function(
  region,
  topicName,
  msgBody
) {
  if (!this.inited) throw Error('Instantiate CMQRequestHelper first please')
  const self = this
  return new Promise((resolve, reject) => {
    let params = {
      Region: region,
      Action: 'PublishMessage',
      topicName,
      msgBody
    }
    self.requestHelper.request(params, function(error, data) {
      if (error) {
        reject(error)
      } else {
        resolve(data)
      }
    })
  })
}

const cmqRequestInst = new CMQRequestHelper(SECRET_ID, SECRET_KEY)

function sendCMQ(body) {
  let promiseArr = []
  promiseArr = EMAIL_NOTIFY_LIST.map(toAddr => {
    return cmqRequestInst.publishMessage(
      CMQ_REGION,
      CMQ_TOPIC_NAME,
      JSON.stringify({
        fromAddr: FROM_ADDR,
        toAddr: toAddr,
        title: 'Please note: PlayCheck Error',
        body: body
      })
    )
  })
  return Promise.all(promiseArr)
}

function testUrl(urlList) {
  let errorInfo = []
  let promiseArr = []
  promiseArr = urlList.map(url => {
    return request(
      {
        url,
        timeout: 3000
      },
      function(e, r, body) {
        if (e) errorInfo.push(e)
      }
    )
  })
  return Promise.all(promiseArr).then(() => sendCMQ(errorInfo.join('\r\n')))
}

exports.main_handler = (event, context, callback) => {
  testUrl(TEST_URL_LIST).then(res => {
    callback(null, res)
  })
}