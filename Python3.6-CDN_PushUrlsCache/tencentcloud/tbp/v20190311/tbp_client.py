# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from taifucloudcloud.common.exception.taifucloud_cloud_sdk_exception import TencentCloudSDKException
from taifucloudcloud.common.abstract_client import AbstractClient
from taifucloudcloud.tbp.v20190311 import models


class TbpClient(AbstractClient):
    _apiVersion = '2019-03-11'
    _endpoint = 'tbp.taifucloudcloudapi.com'


    def CreateBot(self, request):
        """創建機器人

        :param request: Request instance for CreateBot.
        :type request: :class:`taifucloudcloud.tbp.v20190311.models.CreateBotRequest`
        :rtype: :class:`taifucloudcloud.tbp.v20190311.models.CreateBotResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateBot", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateBotResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def Reset(self, request):
        """對當前機器人的會話狀态進行複位

        :param request: Request instance for Reset.
        :type request: :class:`taifucloudcloud.tbp.v20190311.models.ResetRequest`
        :rtype: :class:`taifucloudcloud.tbp.v20190311.models.ResetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("Reset", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TextProcess(self, request):
        """接收調用側的文本輸入，返回應答文本。已廢棄，推薦使用最新版TextProcess介面。

        :param request: Request instance for TextProcess.
        :type request: :class:`taifucloudcloud.tbp.v20190311.models.TextProcessRequest`
        :rtype: :class:`taifucloudcloud.tbp.v20190311.models.TextProcessResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TextProcess", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TextProcessResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TextReset(self, request):
        """會話重置介面。已廢棄，推薦使用最新版TextReset介面。

        :param request: Request instance for TextReset.
        :type request: :class:`taifucloudcloud.tbp.v20190311.models.TextResetRequest`
        :rtype: :class:`taifucloudcloud.tbp.v20190311.models.TextResetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TextReset", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TextResetResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)