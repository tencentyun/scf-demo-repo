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
from taifucloudcloud.fmu.v20191213 import models


class FmuClient(AbstractClient):
    _apiVersion = '2019-12-13'
    _endpoint = 'fmu.taifucloudcloudapi.com'


    def BeautifyPic(self, request):
        """用戶上傳一張人臉圖片，精準定位五官，實現美膚、亮膚、祛痘等美顔功能。

        :param request: Request instance for BeautifyPic.
        :type request: :class:`taifucloudcloud.fmu.v20191213.models.BeautifyPicRequest`
        :rtype: :class:`taifucloudcloud.fmu.v20191213.models.BeautifyPicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BeautifyPic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BeautifyPicResponse()
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


    def CreateModel(self, request):
        """在使用LUT素材的modelid實現試唇色前，您需要先上傳 LUT 格式的cube文件注冊唇色ID。檢視 [LUT文件的使用說明](https://cloud.taifucloud.com/document/product/1172/41701)。

        注：您也可以直接使用 [試唇色介面](https://cloud.taifucloud.com/document/product/1172/40706)，通過輸入RGBA模型數值的方式指定唇色，更簡單易用。

        :param request: Request instance for CreateModel.
        :type request: :class:`taifucloudcloud.fmu.v20191213.models.CreateModelRequest`
        :rtype: :class:`taifucloudcloud.fmu.v20191213.models.CreateModelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateModel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateModelResponse()
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


    def DeleteModel(self, request):
        """删除已注冊的唇色素材。

        :param request: Request instance for DeleteModel.
        :type request: :class:`taifucloudcloud.fmu.v20191213.models.DeleteModelRequest`
        :rtype: :class:`taifucloudcloud.fmu.v20191213.models.DeleteModelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteModel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteModelResponse()
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


    def GetModelList(self, request):
        """查詢已注冊的唇色素材。

        :param request: Request instance for GetModelList.
        :type request: :class:`taifucloudcloud.fmu.v20191213.models.GetModelListRequest`
        :rtype: :class:`taifucloudcloud.fmu.v20191213.models.GetModelListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetModelList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetModelListResponse()
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


    def TryLipstickPic(self, request):
        """對圖片中的人臉嘴唇進行着色，最多支援同時對一張圖中的3張人臉進行試唇色。

        您可以通過事先注冊在Top Cloud 的唇色素材（LUT文件）改變圖片中的人臉唇色，也可以輸入RGBA模型數值。

        爲了更好的效果，建議您使用事先注冊在Top Cloud 的唇色素材（LUT文件）。

        >
        - 公共參數中的簽名方式請使用V3版本，即配置SignatureMethod參數爲TC3-HMAC-SHA256。

        :param request: Request instance for TryLipstickPic.
        :type request: :class:`taifucloudcloud.fmu.v20191213.models.TryLipstickPicRequest`
        :rtype: :class:`taifucloudcloud.fmu.v20191213.models.TryLipstickPicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TryLipstickPic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TryLipstickPicResponse()
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