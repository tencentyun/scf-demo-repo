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

async function record_connectionID(connectionID) {
  console.log("Start record_connectionID function");
  console.log("connectionID is", connectionID);

  const connection = mysql.createConnection({
    host: Host,
    user: User,
    password: Password,
    database: DB,
    port: Port
  });

  // 把 connection ID 存到数据库
  const now = new dayjs();
  const nowStr = now.format("YYYY-MM-DD HH:mm:ss");

  let addsql = `insert INTO ${Table} (\`ConnectionID\`, \`Date\`) VALUES (${connectionID}, ${nowStr})`;

  await wrapPromise(connection, addsql);
  connection.close();
}

exports.main_handler = async (event, context, callback) => {
  console.log("event is", event);

  if (!event.requestContext) {
    return { errNo: 101, errMsg: "not found request context" };
  }

  if (!event.websocket) {
    return { errNo: 102, errMsg: "not found web socket" };
  }

  let connectionID = event["websocket"]["secConnectionID"];
  let retmsg = {};
  retmsg["errNo"] = 0;
  retmsg["errMsg"] = "ok";
  retmsg["websocket"] = {
    action: "connecting",
    secConnectionID: connectionID
  };

  if (event["websocket"]["secWebSocketProtocol"]) {
    retmsg["websocket"]["secWebSocketProtocol"] =
      event["websocket"]["secWebSocketProtocol"];
  }

  if (event["websocket"]["secWebSocketExtensions"]) {
    retmsg["websocket"]["secWebSocketExtensions"] =
      event["websocket"]["secWebSocketExtensions"];
  }

  // 在数据库中记录新的connectionID
  console.log("Start DB Request", new dayjs().format("YYYY-MM-DD HH:mm:ss"));

  await record_connectionID(connectionID);

  console.log("Finish DB Request", new dayjs().format("YYYY-MM-DD HH:mm:ss"));

  console.log(
    "connecting: connection id",
    event["websocket"]["secConnectionID"]
  );
  return retmsg;
};
