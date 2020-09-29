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
from taifucloudcloud.ocr.v20181119 import models


class OcrClient(AbstractClient):
    _apiVersion = '2018-11-19'
    _endpoint = 'ocr.taifucloudcloudapi.com'


    def ArithmeticOCR(self, request):
        """本介面支援作業算式題目的自動識别，目前函蓋 K12 學力範圍内的 14 種題型，包括加減乘除四則運算、分數四則運算、豎式四則運算、脫式計算等。

        :param request: 調用ArithmeticOCR所需參數的結構體。
        :type request: :class:`taifucloudcloud.ocr.v20181119.models.ArithmeticOCRRequest`
        :rtype: :class:`taifucloudcloud.ocr.v20181119.models.ArithmeticOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ArithmeticOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ArithmeticOCRResponse()
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


    def EnglishOCR(self, request):
        """本介面支援圖像英文文字的檢測和識别，返回文字框位置與文字内容。支援多場景、任意版面下的英文、字母、數字和常見字元的識别，同時函蓋英文印刷體和英文手寫體識别。

        :param request: 調用EnglishOCR所需參數的結構體。
        :type request: :class:`taifucloudcloud.ocr.v20181119.models.EnglishOCRRequest`
        :rtype: :class:`taifucloudcloud.ocr.v20181119.models.EnglishOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnglishOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnglishOCRResponse()
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


    def GeneralAccurateOCR(self, request):
        """本介面支援圖像整體文字的檢測和識别，返回文字框位置與文字内容。相比通用印刷體識别介面，準确率和召回率更高。

        :param request: 調用GeneralAccurateOCR所需參數的結構體。
        :type request: :class:`taifucloudcloud.ocr.v20181119.models.GeneralAccurateOCRRequest`
        :rtype: :class:`taifucloudcloud.ocr.v20181119.models.GeneralAccurateOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GeneralAccurateOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GeneralAccurateOCRResponse()
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


    def GeneralBasicOCR(self, request):
        """本介面支援多場景、任意版面下整圖文字的識别，包括中英文、字母、數字和日文、韓文的識别。應用場景包括：印刷文件識别、網絡圖片識别、廣告圖文字識别、街景店招識别、清單識别、視訊標題識别、頭像文字識别等。

        :param request: 調用GeneralBasicOCR所需參數的結構體。
        :type request: :class:`taifucloudcloud.ocr.v20181119.models.GeneralBasicOCRRequest`
        :rtype: :class:`taifucloudcloud.ocr.v20181119.models.GeneralBasicOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GeneralBasicOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GeneralBasicOCRResponse()
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


    def GeneralFastOCR(self, request):
        """本介面支援圖片中整體文字的檢測和識别，返回文字框位置與文字内容。相比通用印刷體識别介面，識别速度更快、支援的 QPS 更高。

        :param request: 調用GeneralFastOCR所需參數的結構體。
        :type request: :class:`taifucloudcloud.ocr.v20181119.models.GeneralFastOCRRequest`
        :rtype: :class:`taifucloudcloud.ocr.v20181119.models.GeneralFastOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GeneralFastOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GeneralFastOCRResponse()
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


    def IDCardOCR(self, request):
        """本介面支援二代身份證正反面所有欄位的識别，包括姓名、性别、民族、出生日期、住址、公民身份證號、簽發機關、有效期限；具備身份證照片、人像照片的裁剪功能和翻拍件、影印件的識别告警功能。

        :param request: 調用IDCardOCR所需參數的結構體。
        :type request: :class:`taifucloudcloud.ocr.v20181119.models.IDCardOCRRequest`
        :rtype: :class:`taifucloudcloud.ocr.v20181119.models.IDCardOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("IDCardOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IDCardOCRResponse()
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


    def TableOCR(self, request):
        """本介面支援圖片内表格文件的檢測和識别，返回每個單元格的文字内容，支援将識别結果保存爲 Excel 格式。

        :param request: 調用TableOCR所需參數的結構體。
        :type request: :class:`taifucloudcloud.ocr.v20181119.models.TableOCRRequest`
        :rtype: :class:`taifucloudcloud.ocr.v20181119.models.TableOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TableOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TableOCRResponse()
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


    def VinOCR(self, request):
        """本介面支援圖片内車輛識别代號（VIN）的檢測和識别。

        :param request: 調用VinOCR所需參數的結構體。
        :type request: :class:`taifucloudcloud.ocr.v20181119.models.VinOCRRequest`
        :rtype: :class:`taifucloudcloud.ocr.v20181119.models.VinOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VinOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VinOCRResponse()
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


    def WaybillOCR(self, request):
        """本介面支援市面上主流版式電子運單的識别，包括收件人和寄件人的姓名、電話、網址以及運單號等欄位。

        :param request: 調用WaybillOCR所需參數的結構體。
        :type request: :class:`taifucloudcloud.ocr.v20181119.models.WaybillOCRRequest`
        :rtype: :class:`taifucloudcloud.ocr.v20181119.models.WaybillOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("WaybillOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.WaybillOCRResponse()
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