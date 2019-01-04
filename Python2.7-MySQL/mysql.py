# -*- coding: utf8 -*-
import datetime
import pymysql.cursors
import logging
import sys
import pytz

# MySql数据库账号信息,需要提前创建好数据库
Host = '******'
User = '****'
Password = '****'
Port = 63054
DB = u'SCF_Demo'

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger()
logger.setLevel(level=logging.INFO)

#更改时区为北京时区
tz = pytz.timezone('Asia/Shanghai')

print("connect database")
connection = pymysql.connect(host=Host,
                             user=User,
                             password=Password,
                             port=Port,
                             db=DB,
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)


def main_handler(event, context):
    print('Start function')
    print("{%s}" % datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S"))
    try:
        with connection.cursor() as cursor:
            sql = 'show databases'
            cursor.execute(sql)
            res = cursor.fetchall()
            print res

            sql = 'use %s'%DB
            cursor.execute(sql)

            #创建数据表
            cursor.execute("DROP TABLE IF EXISTS Test")
            cursor.execute("CREATE TABLE Test (Msg TEXT NOT NULL,Time Datetime)")

            time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
            sql = "insert INTO Test (`Msg`, `Time`) VALUES (%s, %s)"
            cursor.execute(sql, ("test", time))
            connection.commit()

            sql = "select count(*) from Test"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)

    finally:
        connection.close()

    print("{%s}" % datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S"))

    return "test"