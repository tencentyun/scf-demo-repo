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
from taifucloudcloud.lp.v20200224 import models


class LpClient(AbstractClient):
    _apiVersion = '2020-02-24'
    _endpoint = 'lp.taifucloudcloudapi.com'


    def QueryLoginProtection(self, request):
        """登入保護服務（LoginProtection，LP）針對網站和 APP 的用戶登入場景，實時檢測是否存在盜號、撞庫等惡意登入行爲，幫助開發者發現異常登入，降低惡意用戶登入給業務帶來的風險。

        :param request: Request instance for QueryLoginProtection.
        :type request: :class:`taifucloudcloud.lp.v20200224.models.QueryLoginProtectionRequest`
        :rtype: :class:`taifucloudcloud.lp.v20200224.models.QueryLoginProtectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryLoginProtection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryLoginProtectionResponse()
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