# -*- coding: utf8 -*-
# SCF configures the COS trigger, obtains the file uploading information from COS, and downloads it to the local temporary disk 'tmp' of SCF.
# SCF配置COS觸發，從COS獲取文件上傳訊息，並下載到SCF的本地臨時磁盤tmp
from qcloud_cos_v5 import CosConfig
from qcloud_cos_v5 import CosS3Client
from qcloud_cos_v5 import CosServiceError
from qcloud_cos_v5 import CosClientError
import sys
import logging

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

appid = XXXXXX  # Please replace with your APPID. 請替換爲您的 APPID
secret_id = u'************'  # Please replace with your SecretId. 請替換爲您的 SecretId
secret_key = u'****************'  # Please replace with your SecretKey. 請替換爲您的 SecretKey
region = u'ap-shanghai'  # Please replace with the region where COS bucket located. 請替換爲您bucket 所在的地域
token = ''

config = CosConfig(Secret_id=secret_id, Secret_key=secret_key, Region=region, Token=token)
client = CosS3Client(config)
logger = logging.getLogger()


def main_handler(event, context):
    logger.info("start main handler")
    for record in event['Records']:
        try:
            bucket = record['cos']['cosBucket']['name'] + '-' + str(appid)
            key = record['cos']['cosObject']['key']
            key = key.replace('/' + str(appid) + '/' + record['cos']['cosBucket']['name'] + '/', '', 1)
            logger.info("Key is " + key)

            # download object from cos
            logger.info("Get from [%s] to download file [%s]" % (bucket, key))
            download_path = '/tmp/{}'.format(key)
            try:
                response = client.get_object(Bucket=bucket, Key=key, )
                response['Body'].get_stream_to_file(download_path)
            except CosServiceError as e:
                print(e.get_error_code())
                print(e.get_error_msg())
                print(e.get_resource_location())
                return "Fail"
            logger.info("Download file [%s] Success" % key)

        except Exception as e:
            print(e)
            print('Error getting object {} from bucket {}. '.format(key, bucket))
            raise e
            return "Fail"

    return "Success"