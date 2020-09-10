#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql
import os
import logging
from os import getenv
from pymysql.err import OperationalError

# 從函數環境變量獲取資料庫訊息
DB_HOST = os.getenv('dbhost') #'sh-cdb-irye027y.sql.tencentcdb.com:63374'
DB_USER = os.getenv('dbuser') #'root'
DB_USER_PASSWORD = os.getenv('dbpwd')  #'abc123!@#'
DB_DATABASE = os.getenv('dbdatabase') #'testDB'
DB_TABLE = os.getenv('dbtable') #'table'

logger = logging.getLogger()
logger.setLevel(level=logging.INFO)

mysql_conn = None

def __get_cursor():
    try:
        return mysql_conn.cursor()
    except OperationalError:
        mysql_conn.ping(reconnect=True)
        return mysql_conn.cursor()

def main_handler(event, context):
    # 使用 pymysql 無連接池功能連結資料庫，避免循環插入時報錯
    global mysql_conn
    if not mysql_conn:
        mysql_conn = pymysql.connect(DB_HOST, DB_USER, DB_USER_PASSWORD,DB_DATABASE,autocommit = True)
    sql =  "INSERT INTO `" + str(DB_TABLE)+ "` (`offset`, `msgBody`) VALUES (%s, %s)" # 插入offset，msgBody欄位，可自定義
    with __get_cursor() as cursor:
        for record in event["Records"]:
            logger.info("msg: %s", record["Ckafka"]["msgBody"])
            logger.info("offset: %s", record["Ckafka"]["offset"])
            offset = record["Ckafka"]["offset"]
            msgBody = record["Ckafka"]["msgBody"]
            cursor.execute(sql, (offset, msgBody))
    return 'successful!' 