"use strict";
/**************************************************
公有云 - api网关 webscoket注册函数
参考: https://cloud.tencent.com/document/product/583/32553
***************************************************/

// API网关的反向推送链接
const sendbackHost = "*******";
// MySql数据库账号信息,需要提前创建好数据库和表单,表单中新建2列：`ConnectionID`, `Date`
const Host = "10.0.1.148";
const User = "root";
const Password = "root12345";
const Port = 3306;
const DB = "SCF_Demo";
const Table = "ConnectionID_List";

const mysql = require("mysql");
const dayjs = require("dayjs");
const request = require("request");

function wrapPromise(connection, sql) {
  return new Promise((res, rej) => {
    connection.query(sql, function(error, results, fields) {
      if (error) {
        rej(error);
      }
      res(results);
    });
  });
}

async function getConnectionIdList() {
  const connection = mysql.createConnection({
    host: Host,
    user: User,
    password: Password,
    database: DB,
    port: Port
  });

  let querySpl = `select * from ${Table}`;

  let queryResult = await wrapPromise(connection, querySpl);
  connection.close();

  return queryResult;
}

function send(connectionId, data) {
  let retmsg = {};
  retmsg["websocket"] = {};
  retmsg["websocket"]["action"] = "data send";
  retmsg["websocket"]["secConnectionID"] = connectionId;
  retmsg["websocket"]["dataType"] = "text";
  retmsg["websocket"]["data"] = data;
  console.log(`send ${JSON.stringify(data)} to ${connectionId}`);

  // 用request 来发一下包
  // requests.post(sendbackHost, (json = retmsg));

  request.post(
    {
      url: sendbackHost,
      json: true,
      body: retmsg
    },
    (err, response, body) => {
      if (err) {
        console.log(err);
      }
      console.log(body);
    }
  );
}

exports.main_handler = async (event, context, callback) => {
  console.log("event is", event);

  if (!event.websocket) {
    return { errNo: 102, errMsg: "not found web socket" };
  }

  let connectionID = event["websocket"]["secConnectionID"];

  console.log("connecting: connection id", connectionID);

  console.log("Start DB Request", new dayjs().format("YYYY-MM-DD HH:mm:ss"));

  let connectionIdList = await getConnectionIdList();

  let count = connectionIdList.length;

  let data =
    event["websocket"]["data"] + "(===Online people:" + str(count) + "===)";

  console.log("Finish DB Request", new dayjs().format("YYYY-MM-DD HH:mm:ss"));

  connectionIdList.forEach(id => {
    if (id !== connectionID) {
      send(id, data);
    }
  });

  return "send success";
};
