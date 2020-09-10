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
from taifucloudcloud.faceid.v20180301 import models


class FaceidClient(AbstractClient):
    _apiVersion = '2018-03-01'
    _endpoint = 'faceid.taifucloudcloudapi.com'


    def BankCardVerification(self, request):
        """銀行卡核驗

        :param request: 調用BankCardVerification所需參數的結構體。
        :type request: :class:`taifucloudcloud.faceid.v20180301.models.BankCardVerificationRequest`
        :rtype: :class:`taifucloudcloud.faceid.v20180301.models.BankCardVerificationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BankCardVerification", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BankCardVerificationResponse()
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


    def DetectAuth(self, request):
        """每次開始核身前，需先調用本介面獲取BizToken，用來串聯核身流程，在核身完成後，用于獲取驗證結果訊息。

        :param request: 調用DetectAuth所需參數的結構體。
        :type request: :class:`taifucloudcloud.faceid.v20180301.models.DetectAuthRequest`
        :rtype: :class:`taifucloudcloud.faceid.v20180301.models.DetectAuthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetectAuth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetectAuthResponse()
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


    def GetActionSequence(self, request):
        """使用動作活體檢測模式前，需調用本介面獲取動作順序。

        :param request: 調用GetActionSequence所需參數的結構體。
        :type request: :class:`taifucloudcloud.faceid.v20180301.models.GetActionSequenceRequest`
        :rtype: :class:`taifucloudcloud.faceid.v20180301.models.GetActionSequenceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetActionSequence", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetActionSequenceResponse()
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


    def GetDetectInfo(self, request):
        """完成驗證後，用BizToken調用本介面獲取結果訊息，BizToken生成後三天内（3\*24\*3,600秒）可多次拉取。

        :param request: 調用GetDetectInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.faceid.v20180301.models.GetDetectInfoRequest`
        :rtype: :class:`taifucloudcloud.faceid.v20180301.models.GetDetectInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDetectInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDetectInfoResponse()
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


    def GetLiveCode(self, request):
        """使用數字活體檢測模式前，需調用本介面獲取數字驗證碼。

        :param request: 調用GetLiveCode所需參數的結構體。
        :type request: :class:`taifucloudcloud.faceid.v20180301.models.GetLiveCodeRequest`
        :rtype: :class:`taifucloudcloud.faceid.v20180301.models.GetLiveCodeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetLiveCode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetLiveCodeResponse()
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


    def IdCardVerification(self, request):
        """傳入姓名和身份證号，校驗兩者的真實性和一緻性。

        :param request: 調用IdCardVerification所需參數的結構體。
        :type request: :class:`taifucloudcloud.faceid.v20180301.models.IdCardVerificationRequest`
        :rtype: :class:`taifucloudcloud.faceid.v20180301.models.IdCardVerificationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("IdCardVerification", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IdCardVerificationResponse()
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


    def ImageRecognition(self, request):
        """傳入照片和身份訊息，判斷該照片與警察權威庫的證件照是否屬于同一個人。

        :param request: 調用ImageRecognition所需參數的結構體。
        :type request: :class:`taifucloudcloud.faceid.v20180301.models.ImageRecognitionRequest`
        :rtype: :class:`taifucloudcloud.faceid.v20180301.models.ImageRecognitionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImageRecognition", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImageRecognitionResponse()
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


    def LivenessCompare(self, request):
        """傳入視訊和照片，先判斷視訊中是否爲真人，判斷爲真人後，再判斷該視訊中的人與上傳照片是否屬于同一個人。

        :param request: 調用LivenessCompare所需參數的結構體。
        :type request: :class:`taifucloudcloud.faceid.v20180301.models.LivenessCompareRequest`
        :rtype: :class:`taifucloudcloud.faceid.v20180301.models.LivenessCompareResponse`

        """
        try:
            params = request._serialize()
            body = self.call("LivenessCompare", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.LivenessCompareResponse()
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


    def LivenessRecognition(self, request):
        """傳入視訊和身份訊息，先判斷視訊中是否爲真人，判斷爲真人後，再判斷該視訊中的人與警察權威庫的證件照是否屬于同一個人。

        :param request: 調用LivenessRecognition所需參數的結構體。
        :type request: :class:`taifucloudcloud.faceid.v20180301.models.LivenessRecognitionRequest`
        :rtype: :class:`taifucloudcloud.faceid.v20180301.models.LivenessRecognitionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("LivenessRecognition", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.LivenessRecognitionResponse()
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