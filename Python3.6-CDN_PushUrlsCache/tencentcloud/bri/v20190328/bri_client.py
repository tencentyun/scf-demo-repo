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

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.bri.v20190328 import models


class BriClient(AbstractClient):
    _apiVersion = '2019-03-28'
    _endpoint = 'bri.tencentcloudapi.com'


    def DescribeBRI(self, request):
        """輸入業務名 (bri_num, bri_dev, bri_ip, bri_apk, bri_url 五種之一)  及其 相應欄位, 獲取業務風險分數和标簽。

        當業務名爲bri_num時，必須填PhoneNumber欄位.

        當業務名爲bri_dev時, 必須填Imei欄位.

        當業務名爲bri_ip時，必須填IP欄位.

        當業務名爲bri_apk時，必須填 (PackageName,CertMd5,FileSize) 三個欄位 或者 FileMd5一個欄位.

        當業務名爲bri_url時，必須填Url欄位.

        :param request: Request instance for DescribeBRI.
        :type request: :class:`tencentcloud.bri.v20190328.models.DescribeBRIRequest`
        :rtype: :class:`tencentcloud.bri.v20190328.models.DescribeBRIResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBRI", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBRIResponse()
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