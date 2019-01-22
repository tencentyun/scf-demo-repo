/**************************************************
公有云 - kafka 往 producer发消息
TIPS: 
1. 云函数需求kafka实例位于相同的vpc内
参考: 
1. https://www.npmjs.com/package/kafka-node - kafka Node.js 客户端
2. https://cloud.tencent.com/product/ckafka/getting-started - 腾讯云 ckafka相关文档
***************************************************/

const kafka = require('kafka-node');
const client = new kafka.KafkaClient({ kafkaHost: 'xxxx' }); // ckafka host地址，在ckafka基本信息也查看
const producer = new kafka.Producer(client)

exports.main_handler = async (event, context, callback) => {

  const payloads = [
    { 
      topic: 'xxx', // topic 名称
      messages: 'hello world', // 消息内容
    }
  ]

  await new Promise((res, rej) => {
    producer.on('ready', function () {
      producer.send(payloads, function (err, data) {
        if (err) {
          rej(err)
        }
        res(data)
      });
    });
  })
};