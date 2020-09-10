# -*- coding: utf8 -*-
import os
import time
import logging
from io import StringIO

from cdw_client import CDWClient

logger = logging.getLogger()
logger.setLevel(level=logging.INFO)

## 各種系統常數，以下常數均可通過同名環境變量進行函蓋
MSG_SEPARATOR_ASCII = 39 #kafka中訊息的分隔符的ascii碼
MSG_NULL = '\\N' #kafka中訊息的null值
DB_PORT = 5436 #CDW的端口，預設應該是5436
ENABLE_DEBUG = '0' #打開該設置，會列印debug訊息，包括格式錯誤日志
REPLACE_0X00 = '0' #打開該設置，會替換字串中的0x00，會有一定的額外開銷

def init_cdw_client():
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_DATABASE")
    port = os.getenv("DB_PORT", DB_PORT)
    
    cdw_client = CDWClient(host, user, password, int(port), database)
    return cdw_client

def check_param():
    if os.getenv("DB_DATABASE") is None:
        logger.error("need environment variable DB_DATABASE")
        raise Exception('check param fail')
    if os.getenv("DB_HOST") is None:
        logger.error("need environment variable DB_HOST")
        raise Exception('check param fail')
    if os.getenv("DB_USER") is None:
        logger.error("need environment variable DB_USER")
        raise Exception('check param fail')
    if os.getenv("DB_PASSWORD") is None:
        logger.error("need environment variable DB_PASSWORD")
        raise Exception('check param fail')
    if os.getenv("DB_SCHEMA") is None:
        logger.error("need environment variable DB_SCHEMA")
        raise Exception('check param fail')
    if os.getenv("DB_TABLE") is None:
        logger.error("need environment variable DB_TABLE")
        raise Exception('check param fail')

    return True

def main_handler(event, context):
    # 檢查必要的環境變量是否設置
    ret = check_param()
    if ret == False:
        return "done"
    

    # 初始化
    cdw_client = init_cdw_client()

    # 從event中獲取訊息
    sio = StringIO()
    msg_consumed_count = 0
    start_time = int(time.time())

    # 是否替換0x00
    replace_0x00 = os.getenv("REPLACE_0X00", REPLACE_0X00)
    if replace_0x00 == '1':
        for record in event["Records"]:
            msg_consumed_count += 1
            sio.write(record["Ckafka"]["msgBody"].replace('\x00',''))
            sio.write('\n')
    else:
        for record in event["Records"]:
            msg_consumed_count += 1
            sio.write(record["Ckafka"]["msgBody"])
            sio.write('\n')

    logger.info("get msg num: [%d] from event, cost time: [%ds]", msg_consumed_count, int(time.time()) - start_time)

    # 将數據copy到cdw中
    schema = os.getenv("DB_SCHEMA")
    table = os.getenv("DB_TABLE")
    msg_separator_ascii = int(os.getenv("MSG_SEPARATOR_ASCII", MSG_SEPARATOR_ASCII))
    msg_null = os.getenv("MSG_NULL", MSG_NULL)
    enable_debug = os.getenv("ENABLE_DEBUG", ENABLE_DEBUG)
    sio.seek(0)
    ret = cdw_client.copy_from(sio, schema+"."+table, chr(msg_separator_ascii), msg_null)
    if ret == False:
        # copy是一個事務，要麽全部成功，要麽全部失敗，copy失敗，抛出異常，讓平台重試
        sio.close()

        # 如果配置debug，把這一批所有讀取的訊息都列印出來
        if enable_debug == '1':
            logger.error("kafka msg as follow:")
            for record in event['Records']:
                logger.error(record["Ckafka"]["msgBody"])

        raise Exception('copy fail')
    sio.close()

    return "done"


if __name__ == "__main__":
    main_handler(None, None)