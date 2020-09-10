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
from taifucloudcloud.rp.v20200224 import models


class RpClient(AbstractClient):
    _apiVersion = '2020-02-24'
    _endpoint = 'rp.taifucloudcloudapi.com'


    def QueryRegisterProtection(self, request):
        """注冊保護服務（RegisterProtection，RP）針對網站、APP 的線上注冊場景，遇到 “惡意注冊” 、“小号注冊” 、“注冊器注冊” 等惡意行爲，提供基于天禦 DNA 算法的惡意防護引擎，從賬号、設備、行爲三個維度有效識别 “惡意注冊”，從“源頭”上防範業務風險。

        :param request: Request instance for QueryRegisterProtection.
        :type request: :class:`taifucloudcloud.rp.v20200224.models.QueryRegisterProtectionRequest`
        :rtype: :class:`taifucloudcloud.rp.v20200224.models.QueryRegisterProtectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryRegisterProtection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryRegisterProtectionResponse()
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