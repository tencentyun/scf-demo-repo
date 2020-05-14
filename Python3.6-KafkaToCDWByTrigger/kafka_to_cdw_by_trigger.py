# -*- coding: utf8 -*-
import os
import time
import logging
from io import StringIO

from cdw_client import CDWClient

logger = logging.getLogger()
logger.setLevel(level=logging.INFO)

## 各种系统常量，以下常量均可通过同名环境变量进行覆盖
MSG_SEPARATOR = ',' #kafka中消息的分隔符
DB_PORT = 5436 #CDW的端口，默认应该是5436

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
        return False
    if os.getenv("DB_HOST") is None:
        logger.error("need environment variable DB_HOST")
        return False
    if os.getenv("DB_USER") is None:
        logger.error("need environment variable DB_USER")
        return False
    if os.getenv("DB_PASSWORD") is None:
        logger.error("need environment variable DB_PASSWORD")
        return False
    if os.getenv("DB_SCHEMA") is None:
        logger.error("need environment variable DB_SCHEMA")
        return False
    if os.getenv("DB_TABLE") is None:
        logger.error("need environment variable DB_TABLE")
        return False

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
    for record in event["Records"]:
        msg_consumed_count += 1
        sio.write(record["Ckafka"]["msgBody"])
        sio.write('\n')
    logger.info("get msg num: [%d] from event, cost time: [%ds]", msg_consumed_count, int(time.time()) - start_time)

    # 将数据copy到cdw中
    schema = os.getenv("DB_SCHEMA")
    table = os.getenv("DB_TABLE")
    msg_separator = os.getenv("MSG_SEPARATOR", MSG_SEPARATOR)
    sio.seek(0)
    ret = cdw_client.copy_from(sio, schema+"."+table, msg_separator)
    if ret == False:
        # copy是一个事务，要么全部成功，要么全部失败，copy失败，抛出异常，让平台重试
        sio.close()
        raise Exception('copy fail')
    sio.close()

    return "done"


if __name__ == "__main__":
    main_handler(None, None)