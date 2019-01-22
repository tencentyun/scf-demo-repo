/**************************************************
公有云 - COS上传图片后，调用腾讯云图像智能的接口文字识别
TIPS: 
1. 腾讯云图像智能还有其他能力, 请参考api文档
2. 如若为API网关触发方式, 只是取数据的方式有所不同
参考: 
1. https://cloud.tencent.com/document/product/866/17594 - 腾讯云图像智能文档
2. https://www.npmjs.com/package/tcb-ai - tcb-ai相关文档
***************************************************/

const config = {
  appId: '', // 请替换为您的腾讯云Appid
  secretId: '', // 请替换为您的 SecretId
  secretKey: '', // 请替换为您的 SecretKey
}

const { ImageClient } = require("tcb-ai");

const imgClient = new ImageClient({
  AppId: config.appId,
  SecretId: config.secretId,
  SecretKey: config.secretKey
});

exports.main_handler = async (event, context, callback) => {
  console.log("Start main handler");
  try {
    for (let record of event["Records"]) {
      console.log(record);
  
      // 获取图片地址
      const cosObject = record.cos.cosObject;
      const imgUrl = cosObject.url;
      // 抽取出图片的名称
      console.log("imgUrl is: ", imgUrl);
  
      const res = await imgClient.ocrIdCard({
        data: {
          card_type: 0,
          url_list: [imgUrl]
        }
      });
      console.log("ocr result is :", JSON.stringify(res));
  
    }
    return "Success"
  } catch (err) {
    console.log('错误', err)
    return "Fail"
  }
};
