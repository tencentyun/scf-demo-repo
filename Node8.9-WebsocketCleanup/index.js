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

async function deleteConnectionId(connectionID) {
  const connection = mysql.createConnection({
    host: Host,
    user: User,
    password: Password,
    database: DB,
    port: Port
  });

  let querySpl = `delete from ${Table} where ConnectionID = ${connectionID}`;

  let queryResult = await wrapPromise(connection, querySpl);
  connection.end();

  return queryResult;
}

function close(connectionId) {
  let retmsg = {};
  retmsg = {};
  retmsg["websocket"] = {};
  retmsg["websocket"]["action"] = "closing";
  retmsg["websocket"]["secConnectionID"] = connectionId;
  // console.log(`send ${JSON.stringify(data)} to ${connectionId}`);

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

  await deleteConnectionId(connectionID);

  // 如果是主动断开连接
  // await close(connectionID)

  console.log("Finish DB Request", new dayjs().format("YYYY-MM-DD HH:mm:ss"));

  return "send success";
};
