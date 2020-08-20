# -*- coding: utf8 -*-
import os
import time
import logging
from io import StringIO

from cdw_client import CDWClient

logger = logging.getLogger()
logger.setLevel(level=logging.INFO)

## 各种系统常量，以下常量均可通过同名环境变量进行覆盖
MSG_SEPARATOR_ASCII = 39 #kafka中消息的分隔符的ascii码
MSG_NULL = '\\N' #kafka中消息的null值
DB_PORT = 5436 #CDW的端口，默认应该是5436
ENABLE_DEBUG = '0' #打开该设置，会打印debug信息，包括格式错误日志
REPLACE_0X00 = '0' #打开该设置，会替换字符串中的0x00，会有一定的额外开销

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
    # 检查必要的环境变量是否设置
    ret = check_param()
    if ret == False:
        return "done"
    

    # 初始化
    cdw_client = init_cdw_client()

    # 从event中获取消息
    sio = StringIO()
    msg_consumed_count = 0
    start_time = int(time.time())

    # 是否替换0x00
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

    # 将数据copy到cdw中
    schema = os.getenv("DB_SCHEMA")
    table = os.getenv("DB_TABLE")
    msg_separator_ascii = int(os.getenv("MSG_SEPARATOR_ASCII", MSG_SEPARATOR_ASCII))
    msg_null = os.getenv("MSG_NULL", MSG_NULL)
    enable_debug = os.getenv("ENABLE_DEBUG", ENABLE_DEBUG)
    sio.seek(0)
    ret = cdw_client.copy_from(sio, schema+"."+table, chr(msg_separator_ascii), msg_null)
    if ret == False:
        # copy是一个事务，要么全部成功，要么全部失败，copy失败，抛出异常，让平台重试
        sio.close()

        # 如果配置debug，把这一批所有读取的信息都打印出来
        if enable_debug == '1':
            logger.error("kafka msg as follow:")
            for record in event['Records']:
                logger.error(record["Ckafka"]["msgBody"])

        raise Exception('copy fail')
    sio.close()

    return "done"


if __name__ == "__main__":
    main_handler(None, None)