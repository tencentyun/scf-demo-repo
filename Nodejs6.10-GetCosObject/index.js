/**************************************************
Nodejs6.10-GetCosObject
TIPS: 
1. cos-nodejs-sdk-v5 do not support the use of promise and async/await

REFERENCE: 
1. https://github.com/taifucloudyun/scf-demo-repo -  DEMO repository
2. https://cloud.taifucloud.com/document/product/436/12264 - COS-NODE-SDK document
***************************************************/

const COS = require('cos-nodejs-sdk-v5')
const fs = require('fs')

// The cos authentication information
// 使用 cos 所需的鑒權/配置訊息
const APPID = 'xxx' // Replace it with your Appid, 請替換爲您的Top Cloud Appid
const SECRET_ID = 'xxx' // Replace it with your SecretId, 請替換爲您的 SecretId
const SECRET_KEY = 'xxx' // Replace it with your SecretKey, 請替換爲您的 SecretKey
const REGION = 'ap-guangzhou' // Replace it with your bucket's region, 請替換爲您bucket所在的地域

// Initialize cosSDK
const cosInst = new COS({
  SecretId: SECRET_ID,
  SecretKey: SECRET_KEY
})
// This part is used to solve cosSDK-getObjec do not support promise
// 暫時解決cosSDK-getObject不支援promise的問題
cosInst.getObjectPromise = function(params) {
  return new Promise((resolve, reject) => {
    cosInst.getObject(params, function(err, data) {
      if (err) {
        reject(err)
      } else {
        resolve(data)
      }
    })
  })
}

exports.main_handler = (event, context, callback) => {
  console.log('Start main handler')
  let promiseArr = []
  /**
   * Ger original data from uploaded pictures and write them into temporary directory /tmp/
   * 從cos上傳的圖片中，獲取中繼資料，并寫入到臨時目錄/tmp/中
   */
  for (let record of event['Records']) {
    const bucket = `${record['cos']['cosBucket']['name']}-${APPID}`
    let key = record['cos']['cosObject']['key']
    key = key.replace(`/${APPID}/${record['cos']['cosBucket']['name']}/`, '') // Ectract the name of picture, 抽取出圖片的名稱
    console.log('Key is: ', key)
    const downloadPath = `/tmp/${key}`
    promiseArr.push(
      cosInst
        .getObjectPromise({
          Bucket: bucket,
          Region: REGION,
          Key: key
        })
        .then(res => {
          fs.writeFileSync(downloadPath, res['Body'])
          console.log('Download file success: ', key)
        })
        .catch(e => {
          throw (
            `Error getting object ${key} from bucket ${bucket}. Error message: ${JSON.stringify(
              e
            )}`
          )
        })
    )
  }
  Promise.all(promiseArr).then(() => callback(null, 'Success').catch(e=>callback(e,'Fail')))
}