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
from tencentcloud.faceid.v20180301 import models


class FaceidClient(AbstractClient):
    _apiVersion = '2018-03-01'
    _endpoint = 'faceid.tencentcloudapi.com'


    def BankCard2EVerification(self, request):
        """本介面用于校驗姓名和銀行卡号的真實性和一緻性。

        :param request: Request instance for BankCard2EVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.BankCard2EVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.BankCard2EVerificationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BankCard2EVerification", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BankCard2EVerificationResponse()
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


    def BankCard4EVerification(self, request):
        """本介面用于輸入銀行卡号、姓名、開戶證件号、開戶手機号，校驗訊息的真實性和一緻性。

        :param request: Request instance for BankCard4EVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.BankCard4EVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.BankCard4EVerificationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BankCard4EVerification", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BankCard4EVerificationResponse()
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


    def BankCardVerification(self, request):
        """本介面用于銀行卡号、姓名、開戶證件号訊息的真實性和一緻性。

        :param request: Request instance for BankCardVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.BankCardVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.BankCardVerificationResponse`

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
        """每次調用人臉核身SaaS化服務前，需先調用本介面獲取BizToken，用來串聯核身流程，在驗證完成後，用于獲取驗證結果訊息。

        :param request: Request instance for DetectAuth.
        :type request: :class:`tencentcloud.faceid.v20180301.models.DetectAuthRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.DetectAuthResponse`

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

        :param request: Request instance for GetActionSequence.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetActionSequenceRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetActionSequenceResponse`

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

        :param request: Request instance for GetDetectInfo.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetDetectInfoRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetDetectInfoResponse`

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


    def GetDetectInfoEnhanced(self, request):
        """完成驗證後，用BizToken調用本介面獲取結果訊息，BizToken生成後三天内（3\*24\*3,600秒）可多次拉取。

        :param request: Request instance for GetDetectInfoEnhanced.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetDetectInfoEnhancedRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetDetectInfoEnhancedResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDetectInfoEnhanced", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDetectInfoEnhancedResponse()
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

        :param request: Request instance for GetLiveCode.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetLiveCodeRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetLiveCodeResponse`

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


    def IdCardOCRVerification(self, request):
        """本介面用于校驗姓名和身份證号的真實性和一緻性，您可以通過輸入姓名和身份證号或傳入身份證人像面照片提供所需驗證訊息。

        :param request: Request instance for IdCardOCRVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.IdCardOCRVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.IdCardOCRVerificationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("IdCardOCRVerification", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IdCardOCRVerificationResponse()
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

        :param request: Request instance for IdCardVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.IdCardVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.IdCardVerificationResponse`

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

        :param request: Request instance for ImageRecognition.
        :type request: :class:`tencentcloud.faceid.v20180301.models.ImageRecognitionRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.ImageRecognitionResponse`

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


    def Liveness(self, request):
        """活體檢測

        :param request: Request instance for Liveness.
        :type request: :class:`tencentcloud.faceid.v20180301.models.LivenessRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.LivenessResponse`

        """
        try:
            params = request._serialize()
            body = self.call("Liveness", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.LivenessResponse()
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

        :param request: Request instance for LivenessCompare.
        :type request: :class:`tencentcloud.faceid.v20180301.models.LivenessCompareRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.LivenessCompareResponse`

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

        :param request: Request instance for LivenessRecognition.
        :type request: :class:`tencentcloud.faceid.v20180301.models.LivenessRecognitionRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.LivenessRecognitionResponse`

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


    def MinorsVerification(self, request):
        """未成年人守護介面是通過傳入手機号或姓名和身份證号，結合權威數據源和騰訊健康守護可信模型，判斷該訊息是否真實且年滿18周歲。騰訊健康守護可信模型函蓋了上十億手機庫源，函蓋率高、準确率高，如果不在庫中的手機号，還可以通過姓名+身份證進行兜底驗證。

        :param request: Request instance for MinorsVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.MinorsVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.MinorsVerificationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MinorsVerification", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MinorsVerificationResponse()
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


    def MobileNetworkTimeVerification(self, request):
        """本介面用于查詢手機号在網時長，輸入手機号進行查詢。

        :param request: Request instance for MobileNetworkTimeVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.MobileNetworkTimeVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.MobileNetworkTimeVerificationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MobileNetworkTimeVerification", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MobileNetworkTimeVerificationResponse()
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


    def MobileStatus(self, request):
        """本介面用于驗證手機号的狀态，您可以輸入手機号進行查詢。

        :param request: Request instance for MobileStatus.
        :type request: :class:`tencentcloud.faceid.v20180301.models.MobileStatusRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.MobileStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MobileStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MobileStatusResponse()
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


    def PhoneVerification(self, request):
        """本介面用于校驗手機号、姓名和身份證号的真實性和一緻性。

        :param request: Request instance for PhoneVerification.
        :type request: :class:`tencentcloud.faceid.v20180301.models.PhoneVerificationRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.PhoneVerificationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PhoneVerification", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PhoneVerificationResponse()
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