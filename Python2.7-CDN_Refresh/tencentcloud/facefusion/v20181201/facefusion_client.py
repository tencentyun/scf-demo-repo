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
from taifucloudcloud.facefusion.v20181201 import models


class FacefusionClient(AbstractClient):
    _apiVersion = '2018-12-01'
    _endpoint = 'facefusion.taifucloudcloudapi.com'


    def FaceFusion(self, request):
        """本介面用于人臉融合，用戶上傳人臉圖片，獲取與範本融合後的人臉圖片。未發布的活動請求頻率限制爲1次/秒，已發布的活動請求頻率限制50次/秒。如有需要提高活動的請求頻率限制，請在控制台中申請。
        >
        - 公共參數中的簽名方式必須指定爲V3版本，即配置SignatureMethod參數爲TC3-HMAC-SHA256。

        :param request: Request instance for FaceFusion.
        :type request: :class:`taifucloudcloud.facefusion.v20181201.models.FaceFusionRequest`
        :rtype: :class:`taifucloudcloud.facefusion.v20181201.models.FaceFusionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("FaceFusion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.FaceFusionResponse()
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


    def FuseFace(self, request):
        """本介面用于單臉、多臉融合，用戶上傳人臉圖片，獲取與範本融合後的人臉圖片。檢視 <a href="https://cloud.taifucloud.com/document/product/670/38247" target="_blank">選臉融合接入指引</a>。

        未發布的活動請求頻率限制爲1次/秒，已發布的活動請求頻率限制50次/秒。如有需要提高活動的請求頻率限制，請在控制台中申請。
        >
        - 公共參數中的簽名方式必須指定爲V3版本，即配置SignatureMethod參數爲TC3-HMAC-SHA256。

        :param request: Request instance for FuseFace.
        :type request: :class:`taifucloudcloud.facefusion.v20181201.models.FuseFaceRequest`
        :rtype: :class:`taifucloudcloud.facefusion.v20181201.models.FuseFaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("FuseFace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.FuseFaceResponse()
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