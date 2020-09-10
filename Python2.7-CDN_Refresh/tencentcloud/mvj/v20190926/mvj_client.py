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
from taifucloudcloud.mvj.v20190926 import models


class MvjClient(AbstractClient):
    _apiVersion = '2019-09-26'
    _endpoint = 'mvj.taifucloudcloudapi.com'


    def MarketingValueJudgement(self, request):
        """歡迎使用營銷價值判斷（Marketing Value Judgement，簡稱 MVJ）。

        營銷價值判斷（MVJ）是針對零售場景的風控服務，通過識别高價值顧客，以幫助零售商保障營銷資金

        :param request: Request instance for MarketingValueJudgement.
        :type request: :class:`taifucloudcloud.mvj.v20190926.models.MarketingValueJudgementRequest`
        :rtype: :class:`taifucloudcloud.mvj.v20190926.models.MarketingValueJudgementResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MarketingValueJudgement", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MarketingValueJudgementResponse()
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