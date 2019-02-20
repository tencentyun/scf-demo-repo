/**************************************************
公有云 - 获取ckafka的数据写入cos
参考: 
1. https://cloud.tencent.com/document/product/583/17530- SCF ckafka触发器设置相关文档
***************************************************/

const fs = require("fs")
const cos = require("cos-nodejs-sdk-v5")
const local_path = "/tmp/local_file.txt"
const config = {
  appId: '', // 请替换为您的腾讯云Appid
  secretId: '', // 请替换为您的 SecretId
  secretKey: '', // 请替换为您的 SecretKey
  bucketName: ''
}


const cosSdk = new cos({
  SecretId: config.secretId,
  SecretKey: config.secretKey
})

exports.main_handler = async (event, context, callback) => {
  try {
    let out = fs.createWriteStream(local_path, {
      flags: "a",
      encoding: "utf8"
    });
  
    let records = event.Records || []
  
    records.forEach(r => {
      if (r.Ckafka) {
        let msg = r.Ckafka.msgBody
  
        out.write(msg)
        out.write("\r\n")
      }
    })
  
    out.end()
  
    // 上传到cos
    await putCosObject(cosSdk, {
      Bucket: `${config.appId}-${config.bucketName}`,
      Region: 'ap-guangzhou',
      Key: `ckafka_${Date.now()}.txt`,
      Body: fs.createReadStream(local_path)
    })
  
    console.log('cos上传成功')
    return true
  } catch (err) {
    console.log(err)
    return false
  }
};

function putCosObject(cos, params) {
  return new Promise(function (resolve, reject) {
    cos.putObject(params, function (err, data) {
      if (err) {
        reject(err);
      } else {
        resolve(data);
      }
    });
  });
}