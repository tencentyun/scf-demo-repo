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
from taifucloudcloud.tics.v20181115 import models


class TicsClient(AbstractClient):
    _apiVersion = '2018-11-15'
    _endpoint = 'tics.taifucloudcloudapi.com'


    def DescribeDomainInfo(self, request):
        """提供域名相關的基礎訊息以及與攻擊事件（團夥、家族）、惡意文件等相關聯訊息。

        :param request: 調用DescribeDomainInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.tics.v20181115.models.DescribeDomainInfoRequest`
        :rtype: :class:`taifucloudcloud.tics.v20181115.models.DescribeDomainInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDomainInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDomainInfoResponse()
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


    def DescribeFileInfo(self, request):
        """提供文件相關的基礎訊息以及與攻擊事件（團夥、家族）、惡意文件等相關聯訊息。

        :param request: 調用DescribeFileInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.tics.v20181115.models.DescribeFileInfoRequest`
        :rtype: :class:`taifucloudcloud.tics.v20181115.models.DescribeFileInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFileInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFileInfoResponse()
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


    def DescribeIpInfo(self, request):
        """提供IP相關的基礎訊息以及與攻擊事件（團夥、家族）、惡意文件等相關聯訊息。

        :param request: 調用DescribeIpInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.tics.v20181115.models.DescribeIpInfoRequest`
        :rtype: :class:`taifucloudcloud.tics.v20181115.models.DescribeIpInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIpInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIpInfoResponse()
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


    def DescribeThreatInfo(self, request):
        """提供IP和域名相關威脅情報訊息查詢，這些訊息可以輔助檢測失陷主機、幫助SIEM/SOC等系統做研判決策、幫助運營團隊對設備報警的編排處理。

        :param request: 調用DescribeThreatInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.tics.v20181115.models.DescribeThreatInfoRequest`
        :rtype: :class:`taifucloudcloud.tics.v20181115.models.DescribeThreatInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeThreatInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeThreatInfoResponse()
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