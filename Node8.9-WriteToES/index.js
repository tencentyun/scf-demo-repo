"use strict";
/**************************************************
公有云 - api网关 把数据写入es
参考: https://cloud.tencent.com/document/product/583/32553
***************************************************/

// es集群的主机地址
// const Host = "10.0.1.148";
// const Port = "80";

const dayjs = require("dayjs");
const elasticsearch = require("elasticsearch");

const client = new elasticsearch.Client({
  host: "10.0.21.6:9200"
});

exports.main_handler = async (event, context, callback) => {
  let write_data = {};
  write_data["timestamp"] = new dayjs().format("YYYY-MM-DD HH:mm:ss");
  write_data["randomcode"] = parseInt(Math.random() * 100);
  client.index({
    index: "cron_write",
    doc_type: "doc",
    body: write_data
  });

  return "write success";
};
