#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import hashlib
import urllib
import requests
import binascii
import hmac
import copy
import random
import sys
import time
from pprint import pprint
from optparse import OptionParser
from requests.packages.urllib3.exceptions import InsecurePlatformWarning
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import json
from qcloud_cos_v5 import CosConfig
from qcloud_cos_v5 import CosS3Client
from qcloud_cos_v5 import CosServiceError
from qcloud_cos_v5 import CosClientError
import logging

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger()
logger.setLevel(level=logging.INFO)

appid = '1253970226'  # 请替换为您的 APPID
secret_id = 'xxxxxxxxx'  # 请替换为您的 SecretId
secret_key ='xxxxxxxxx'  # 请替换为您的 SecretKey
region = u'ap-beijing'  # 请替换为您bucket 所在的地域
url_host = 'http://mason-test-1253970226.file.myqcloud.com' # 请替换为您要加速的bucket域名，具体的文件路径在main函数里拼装

token = ''
config = CosConfig(Secret_id=secret_id, Secret_key=secret_key, Region=region, Token=token)
client = CosS3Client(config)

class Sign:
    def __init__(self, secretId, secretKey):
        self.secretId = secretId
        self.secretKey = secretKey

    def make(self, requestHost, requestUri, params, method = 'GET'):
        srcStr = method.upper() + requestHost + requestUri + '?' + "&".join(k.replace("_",".") + "=" + str(params[k]) for k in sorted(params.keys()))
        hashed = hmac.new(self.secretKey, srcStr, hashlib.sha1)
        return binascii.b2a_base64(hashed.digest())[:-1]

class Request:
    timeout = 10
    version = 'Python_Tools'
    def __init__(self, secretId, secretKey):
        self.secretId = secretId
        self.secretKey = secretKey

    def send(self,cdn_urls):
        requestHost = 'cdn.api.qcloud.com'
        requestUri = '/v2/index.php'
        files = {}
        method = 'POST'
        debug = 1
        params = {
            'Region': 'gz',
            'Nonce': random.randint(1, sys.maxint),
            'Timestamp': int(time.time()),
            'Action': 'RefreshCdnUrl'
        }        
        params['urls.0'] = cdn_urls
        params['RequestClient'] = Request.version
        params['SecretId'] = self.secretId
        sign = Sign(self.secretId, self.secretKey)
        params['Signature'] = sign.make(requestHost, requestUri, params, method)

        url = 'https://%s%s' % (requestHost, requestUri)

        if debug:
            print method.upper(), url
            print 'Request Args:'
            pprint(params)
        if method.upper() == 'GET':
            req = requests.get(url, params=params, timeout=Request.timeout,verify=False)
        else:
            req = requests.post(url, data=params, files=files, timeout=Request.timeout,verify=False)

        if debug:
            print "Response:", req.status_code, req.text
        if req.status_code != requests.codes.ok:
            req.raise_for_status()

        rsp = {}
        try:
            rsp = json.loads(req.text)
        except:
            raise ValueError, "Error: response is not json\n%s" % req.text

        code = rsp.get("code", -1)
        message = rsp.get("message", req.text)
        if rsp.get('code', -404) != 0:
            raise ValueError, "Error: code=%s, message=%s" % (code, message)
        if rsp.get('data', None) is None:
            print 'request is success.'
        else:
            print rsp['data']

def main_handler(event, context):
    logger.info("start main handler")
    if "Records" not in event.keys():
        return {"code": 410, "errorMsg": "event is not come from cos"}
    for record in event['Records']:
        try:
            bucket = record['cos']['cosBucket']['name'] + '-' + str(appid)
            key = record['cos']['cosObject']['key']
            key = key.replace('/' + str(appid) + '/' + record['cos']['cosBucket']['name'] + '/', '', 1)
            logger.info("Key is " + key)
            if key[-1] == '/':
                print ("No need refresh")
                return "No need refresh"
            #拼装待刷新的url地址
            rel_url = url_host + '/' + key
            logger.info("rel_url is " + rel_url)

            #调用刷新函数
            request = Request(secret_id, secret_key)
            res = request.send(rel_url)

        except Exception as e:
            print(e)
            return "refresh fail"

    return "refresh success"