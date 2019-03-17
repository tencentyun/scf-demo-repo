"use strict";
/**************************************************
公有云 - api网关 把数据写入es
参考: https://cloud.tencent.com/document/product/583/32553
***************************************************/

// es集群的主机地址
// const Host = "10.0.1.148";
// const Port = "80";

// const dayjs = require("dayjs");
const elasticsearch = require("elasticsearch");

const client = new elasticsearch.Client({
  host: "**",
  requestTimeout: 300000
});

const esPrefix = "cron-"; // 查找的 index 索引前缀
const esCuratorTimeStr = "%Y%m%d%H"; // 索引中的时间格式
const esCuratorTimeUnit = "hour"; // 过滤清理的时间单位
const esCuratorTimeCount = 8; // 时间间隔

exports.main_handler = async (event, context, callback) => {
  // 索引删除
  try {
    // 获取所有的index
    let result = await new Promise((res, rej) => {
      client.cat.indices(
        {
          format: "json"
        },
        function(error, result) {
          if (error) {
            rej(error);
          } else {
            res(result);
          }
        }
      );
    });

    // 删除index
    await new Promise((res, rej) => {
      client.indices.delete(
        {
          index: result[0].index
        },
        function(error, result) {
          if (error) {
            rej(error);
          } else {
            res(result);
          }
        }
      );
    });
    // 删除
  } catch (err) {
    console.log(err);
  }

  return "success";
};
