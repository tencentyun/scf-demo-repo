
/**************************************************
公有云 - 通过apigw调用云函数, 操作腾讯云mysql数据库
参考: mysql相关api---https://www.npmjs.com/package/mysql
参考: 如何访问云数据库---https://cloud.tencent.com/document/product/236/3130
参考: api网关如何对接scf---https://cloud.tencent.com/document/product/628/11983
***************************************************/

function wrapPromise(connection, sql) {
  return new Promise((res, rej) => {
    connection.query(sql, function(error, results, fields) {
      if (error) {
        rej(error)
      }
      res(results)
    })
  })
}


exports.main_handler = async (event, context, callback) => {
  const mysql = require('mysql');
  const connection = mysql.createConnection({
    host: 'xxxx', // 云数据库实例ip地址
    user: 'xxx', // 云数据库用户名，如root
    password: 'xxx', // 云数据库密码
    database: 'xxx' // 数据库名称
  });

  connection.connect();

  // get value from apigw
  const {CustomerID, CustomerName} = event.queryString

  const updateSql = `UPDATE Customers SET CustomerName = '${CustomerName}' WHERE CustomerID = ${CustomerID}`
  const querySql = `SELECT * from Customers`

  await wrapPromise(connection, updateSql)

  let queryResult = await wrapPromise(connection, querySql)
  
  connection.end();

  return queryResult
}

