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
from taifucloudcloud.ic.v20190307 import models


class IcClient(AbstractClient):
    _apiVersion = '2019-03-07'
    _endpoint = 'ic.taifucloudcloudapi.com'


    def DescribeApp(self, request):
        """根據應用id查詢物聯卡應用詳情

        :param request: 調用DescribeApp所需參數的結構體。
        :type request: :class:`taifucloudcloud.ic.v20190307.models.DescribeAppRequest`
        :rtype: :class:`taifucloudcloud.ic.v20190307.models.DescribeAppResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeApp", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAppResponse()
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


    def DescribeCard(self, request):
        """查詢卡片詳細訊息

        :param request: 調用DescribeCard所需參數的結構體。
        :type request: :class:`taifucloudcloud.ic.v20190307.models.DescribeCardRequest`
        :rtype: :class:`taifucloudcloud.ic.v20190307.models.DescribeCardResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCard", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCardResponse()
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


    def DescribeCards(self, request):
        """查詢卡片清單訊息

        :param request: 調用DescribeCards所需參數的結構體。
        :type request: :class:`taifucloudcloud.ic.v20190307.models.DescribeCardsRequest`
        :rtype: :class:`taifucloudcloud.ic.v20190307.models.DescribeCardsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCards", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCardsResponse()
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


    def SendMultiSms(self, request):
        """群發簡訊

        :param request: 調用SendMultiSms所需參數的結構體。
        :type request: :class:`taifucloudcloud.ic.v20190307.models.SendMultiSmsRequest`
        :rtype: :class:`taifucloudcloud.ic.v20190307.models.SendMultiSmsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SendMultiSms", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SendMultiSmsResponse()
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


    def SendSms(self, request):
        """發送短訊息介面

        :param request: 調用SendSms所需參數的結構體。
        :type request: :class:`taifucloudcloud.ic.v20190307.models.SendSmsRequest`
        :rtype: :class:`taifucloudcloud.ic.v20190307.models.SendSmsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SendSms", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SendSmsResponse()
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