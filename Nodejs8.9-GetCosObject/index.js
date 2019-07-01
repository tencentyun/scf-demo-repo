/**************************************************
公有云 - COS触发元数据读取
TIPS: 
1. cos-nodejs-sdk-v5暂不支持promise和async/await用法

参考: 
1. https://github.com/tencentyun/scf-demo-repo - COS触发元数据读取的DEMO仓库
2. https://cloud.tencent.com/document/product/436/12264 - COS-NODE-SDK文档
***************************************************/

const COS = require('cos-nodejs-sdk-v5')
const fs = require('fs')

// 使用 cos 所需的鉴权/配置信息
const APPID = 'xxx' // 请替换为您的腾讯云Appid
const SECRET_ID = 'xxx' // 请替换为您的 SecretId
const SECRET_KEY = 'xxx' // 请替换为您的 SecretKey
const REGION = 'ap-guangzhou' // 请替换为您bucket所在的地域

// cosSDK初始化
const cosInst = new COS({
  SecretId: SECRET_ID,
  SecretKey: SECRET_KEY
})
// 暂时解决cosSDK-getObject不支持promise的问题
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

exports.main_handler = async (event, context, callback) => {
  console.log('Start main handler')
  let promiseArr = []
  /**
   * 从cos上传的图片中，获取元数据，并写入到临时目录/tmp/中
   */
  for (let record of event['Records']) {
    const bucket = `${record['cos']['cosBucket']['name']}-${APPID}`
    let key = record['cos']['cosObject']['key']
    key = key.replace(`/${APPID}/${record['cos']['cosBucket']['name']}/`, '') // 抽取出图片的名称
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
  
  try {
    await Promise.all(promiseArr)
    return 'Success'
  } catch(e) {
    console.log(e)
    return 'Fail'
  }
}
