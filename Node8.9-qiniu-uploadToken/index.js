'use strict';
exports.main_handler = async (event, context, callback) => {
    console.log('获取七牛云token');
    const qiniu = require("qiniu");
    const accessKey = "accessKey"; //七牛云accessKey
    const secretKey = "secretKey"; //七牛云secretKey
    const bucket = "bucketName"; //七牛项目名称

    const mac = new qiniu.auth.digest.Mac(accessKey, secretKey);
    const putPolicy = new qiniu.rs.PutPolicy({
      scope: bucket
    });

    const uploadToken =  putPolicy.uploadToken(mac);
    
    const body = {
      uploadToken:uploadToken
    }

    return {
      isBase64: false,
      statusCode: 200,
      headers: { 'Content-Type': 'application/json;charset=UTF-8', 'Access-Control-Allow-Origin': '*' },
      body: body
    }
};