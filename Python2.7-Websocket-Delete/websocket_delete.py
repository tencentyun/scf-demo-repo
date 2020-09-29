# -*- coding: utf8 -*-
import json
import requests
import datetime
import time
import pymysql.cursors
import logging
import sys
import pytz

print('Start Delete function')

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger()
logger.setLevel(level=logging.INFO)

# The reverse push link for API gateway. API閘道的反向推送連結
sendbackHost = "*******"
# MySql database account information, you need to create a database and form in advance, the new two columns in the form: `ConnectionID`, `Date` 
# MySql資料庫賬號訊息,需要提前創建好資料庫和表單,表單中新建2列：`ConnectionID`, `Date`
Host = '******'
User = '****'
Password = '****'
Port = 63054
DB = u'SCF_Demo'
Table = u'ConnectionID_List'

# Changing the time zone to Beijing. 更改時區爲 時區
tz = pytz.timezone('Asia/Shanghai')

# Looking up and deleting the 'connectionID' in the database. 查詢資料庫中的connectionID並删除
def delete_connectionID(connectionID):
    print('Start delete_connectionID function')
    print("connectionID is %s"%connectionID)
    connection = pymysql.connect(host=Host,
                                 user=User,
                                 password=Password,
                                 port=Port,
                                 db=DB,
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "use %s" % DB
            cursor.execute(sql)
            sql = "delete from %s"%Table + " where ConnectionID = %s"
            cursor.execute(sql, (str(connectionID)))
            connection.commit()
    finally:
        connection.close()


# Sending disconnection information proactively. 主動發送斷開訊息
def close(connectionID):
    retmsg = {}
    retmsg['websocket'] = {}
    retmsg['websocket']['action'] = "closing"
    retmsg['websocket']['secConnectionID'] = connectionID
    r = requests.post(sendbackHost, json=retmsg)
    return retmsg


def main_handler(event, context):
    print("event is %s" % event)
    if 'websocket' not in event.keys():
        return {"errNo":102, "errMsg":"not found web socket"}
    else:
        print("Start DB Request {%s}" % datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S"))
        delete_connectionID(event['websocket']['secConnectionID'])
        print("Finish DB Request {%s}" %datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S"))
        # close(connectionID)
    return event