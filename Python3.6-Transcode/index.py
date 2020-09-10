#####----------------------------------------------------------------#####
#####                                                                #####
#####   使用教程/readme:                                              #####
#####   https://cloud.taifucloud.com/document/product/583/47071         #####
#####                                                                #####
#####----------------------------------------------------------------#####

import os
import subprocess
from qcloud_cos_v5 import CosConfig
from qcloud_cos_v5 import CosS3Client
import logging
import sys
import re
import math
import requests

region = os.environ.get('region')
target_bucket = os.environ.get('target_bucket')
target_path = os.environ.get('target_path')

#ffmpeg命令
#視訊壓縮
video_press = '/tmp/ffmpeg  -i %s -r 10 -b:a 32k %s'
#視訊截取 
video_cut = '/tmp/ffmpeg -ss 00:00:00 -t 00:00:10 -i %s -vcodec copy -acodec copy %s'
#獲取視訊時長
video_length = '/tmp/ffmpeg -i %s 2>&1 | grep "Duration"'

#控制log輸出級别
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger()
logger.setLevel(level=logging.INFO)

#  ffmpeg到tmp目錄，并且賦予權限,tmp是雲函數的本地磁盤空間，可讀可寫
with open("/var/user/ffmpeg", "rb") as rf:
    with open("/tmp/ffmpeg", "wb") as wf:
        wf.write(rf.read())
subprocess.run('chmod 755 /tmp/ffmpeg', shell=True)


#删除本地文件
def delete_local_file(src):
    logger.info("delete files and folders")
    if os.path.isfile(src):
        try:
            os.remove(src)
        except:
            pass
    elif os.path.isdir(src):
        for item in os.listdir(src):
            itemsrc = os.path.join(src, item)
            delete_local_file(itemsrc)
        try:
            os.rmdir(src)
        except:
            pass

def main_handler(event, context):
    logger.info("start main handler")
    #使用臨時秘鑰初始化COS Client
    secret_id = os.environ.get('TENCENTCLOUD_SECRETID')      
    secret_key = os.environ.get('TENCENTCLOUD_SECRETKEY')    
    token = os.environ.get('TENCENTCLOUD_SESSIONTOKEN') 
    cosClient = CosS3Client(CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key,Token=token))
    #判斷請求是否從API閘道傳遞,通過閘道傳遞源文件下載網址，在body中獲取
    if "body" in event.keys():
        download_path = event['body']
        key = download_path.split('/')[-1]
        logger.info('api download_path: '+ download_path)

    #判斷請求是否從COS傳遞
    elif "Records" in event.keys():
        #從event裏獲取COS文件訊息，并獲取下載網址
        bucket = event['Records'][0]['cos']['cosBucket']['name'] + '-' + event['Records'][0]['cos']['cosBucket']['appid']
        key = "/".join(event['Records'][0]['cos']['cosObject']['key'].split("/")[3:])
        download_path = event['Records'][0]['cos']['cosObject']['url']
        logger.info('cos download_path: '+ download_path)
    else:
        return {"code": 410, "errorMsg": "event does not come from COS or APIGW"}

    logger.info('key: '+ key)
    upload_path = '/tmp/new-'+ key.split('/')[-1]
    logger.info('upload_path: '+ upload_path)
    # 執行ffmpeg命令，從下載網址讀流的方式進行轉碼
    child = subprocess.run( video_press %(download_path, upload_path), stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True, shell=True)
    # 上傳視訊，可自定義上傳路徑
    cosClient.put_object_from_local_file(
        Bucket=target_bucket,
        LocalFilePath=upload_path,
        Key= target_path+'/'+ upload_path.split('/')[-1]
    )
    delete_local_file(upload_path) 
    
    return 'success'