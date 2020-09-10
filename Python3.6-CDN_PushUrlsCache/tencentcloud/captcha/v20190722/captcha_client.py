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
from tencentcloud.captcha.v20190722 import models


class CaptchaClient(AbstractClient):
    _apiVersion = '2019-07-22'
    _endpoint = 'captcha.tencentcloudapi.com'


    def DescribeCaptchaAppIdInfo(self, request):
        """查詢安全驗證碼應用APPId訊息

        :param request: Request instance for DescribeCaptchaAppIdInfo.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaAppIdInfoRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaAppIdInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCaptchaAppIdInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCaptchaAppIdInfoResponse()
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


    def DescribeCaptchaData(self, request):
        """安全驗證碼分類查詢數據介面，請求量type=0、驗證量type=1、通過量type=2、攔截量type=3  分鍾級查詢

        :param request: Request instance for DescribeCaptchaData.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaDataRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCaptchaData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCaptchaDataResponse()
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


    def DescribeCaptchaDataSum(self, request):
        """安全驗證碼查詢請求數據概況，例如：按照時間段查詢數據  昨日請求量、昨日惡意比例、昨日驗證量、昨日通過量、昨日惡意攔截量……

        :param request: Request instance for DescribeCaptchaDataSum.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaDataSumRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaDataSumResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCaptchaDataSum", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCaptchaDataSumResponse()
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


    def DescribeCaptchaOperData(self, request):
        """安全驗證碼用戶操作數據查詢，驗證碼加載耗時type = 1 、攔截情況type = 2、 一周通過平均嘗試次數 type = 3、嘗試次數分布 type = 4

        :param request: Request instance for DescribeCaptchaOperData.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaOperDataRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaOperDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCaptchaOperData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCaptchaOperDataResponse()
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


    def DescribeCaptchaResult(self, request):
        """核查驗證碼票據結果

        :param request: Request instance for DescribeCaptchaResult.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaResultRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCaptchaResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCaptchaResultResponse()
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


    def DescribeCaptchaUserAllAppId(self, request):
        """安全驗證碼獲取用戶注冊所有APPId和應用名稱

        :param request: Request instance for DescribeCaptchaUserAllAppId.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaUserAllAppIdRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaUserAllAppIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCaptchaUserAllAppId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCaptchaUserAllAppIdResponse()
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


    def UpdateCaptchaAppIdInfo(self, request):
        """更新驗證碼應用APPId訊息

        :param request: Request instance for UpdateCaptchaAppIdInfo.
        :type request: :class:`tencentcloud.captcha.v20190722.models.UpdateCaptchaAppIdInfoRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.UpdateCaptchaAppIdInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateCaptchaAppIdInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateCaptchaAppIdInfoResponse()
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