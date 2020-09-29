#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import json
import time
import logging
from multiprocessing import Process
from taifucloudcloud.ckafka.v20190819 import ckafka_client, models as ckafka_models
from taifucloudcloud.common import credential
from taifucloudcloud.common.exception.taifucloud_cloud_sdk_exception import TencentCloudSDKException
from taifucloudcloud.scf.v20180416 import scf_client, models as scf_models

logger = logging.getLogger()
logger.setLevel(level=logging.INFO)


def kafka_consumer_api_handler(cred, partition_id, region, consumer_function_name, namespace):
    try:

        # 實例化要請求産品的client對象，以及函數所在的地域
        client = scf_client.ScfClient(cred, region)
        # 介面參數,輸入需要調用的函數名，RequestResponse(同步) 和 Event(異步)
        function_name = consumer_function_name
        logger.debug('Start Hello World function')
        # 調用介面，發起請求，並列印返回結果
        req = scf_models.InvokeRequest()
        req.FunctionName = function_name
        req.Namespace = namespace
        req.InvocationType = "Event"
        client_param = {"partition_id": partition_id}
        req.ClientContext = json.dumps(client_param)
        ret = client.Invoke(req)
        ret_value = json.loads(s=ret.to_json_string())
        logger.debug("ret_value: %s", str(ret_value["Result"]))

    except TencentCloudSDKException as err:
        logger.error(err)


def main_handler(event, context):
    try:
        start_time = int(time.time())
        logger.info("schedule start time: %s", str(start_time))
        # 實例化一個認證對象，入參需要傳入Top Cloud 帳戶臨時secret_id，secret_key, token
        secret_id = os.getenv("TENCENTCLOUD_SECRETID")
        secret_key = os.getenv("TENCENTCLOUD_SECRETKEY")
        token = os.getenv("TENCENTCLOUD_SESSIONTOKEN")
        instance_id = os.getenv("instance_id")
        topic_name = os.getenv("topic_name")
        region = os.getenv("region")
        consumer_function_name = os.getenv("consumer_function_name")
        namespace = context["namespace"]
        cred = credential.Credential(secret_id, secret_key, token)

        # 實例化要請求kafka的client對象
        client = ckafka_client.CkafkaClient(cred, region)

        # 實例化一個請求對象
        req = ckafka_models.DescribeTopicAttributesRequest()
        req.InstanceId = instance_id
        req.TopicName = topic_name

        # 通過client對象調用想要訪問的介面，需要傳入請求對象
        resp = client.DescribeTopicAttributes(req)

        # 輸出json格式的字串回包
        logger.debug("get topic attributes: %s", resp.to_json_string())
        ret_value = json.loads(s=resp.to_json_string())

        logger.info("PartitionNum: %s", str(ret_value["Result"]["PartitionNum"]))
        partition_num = ret_value["Result"]["PartitionNum"]
        process_list = list()
        for partition_id in range(partition_num):
            logger.debug("job-------:" + str(partition_id))
            p = Process(target=kafka_consumer_api_handler, name='kafka_consumer_api_handler(%s)' % "",
                        args=(cred, partition_id, region, consumer_function_name, namespace))
            process_list.append(p)

        for p in process_list:
            p.start()

        for p in process_list:
            p.join()
        logger.info("schedule success end time: %s", str(int(time.time())))
    except TencentCloudSDKException as err:
        logger.error(err)
        logger.info("schedule failed end time: %s", str(int(time.time())))

    return "success"


if __name__ == "__main__":
    main_handler(None, None)