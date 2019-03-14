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


const esPrefix = "cron-"              // 查找的 index 索引前缀
const esCuratorTimeStr = "%Y%m%d%H"   // 索引中的时间格式
const esCuratorTimeUnit = "hour"      // 过滤清理的时间单位
const esCuratorTimeCount = 8          // 时间间隔

// 如上示例可以清理 索引格式类似为 index-2018101113 ，当前时间的8个小时前的索引

// ESServer = Elasticsearch(esServer)

function clean_index() {
  ilo = curator.IndexList(ESServer)
    ilo.filter_by_regex(kind='prefix', value=esPrefix)
    ilo.filter_by_age(source='name', direction='older', timestring=esCuratorTimeStr, unit=esCuratorTimeUnit, unit_count=esCuratorTimeCount)
    try:
        ilo.empty_list_check()
    except Exception,e:
        print(e)
        print("list is empty")
        return
    delete_indices = curator.DeleteIndices(ilo)
    print(delete_indices.do_action())
}
    

def main_handler(event,context):
    clean_index()

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
