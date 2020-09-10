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
from tencentcloud.ocr.v20181119 import models


class OcrClient(AbstractClient):
    _apiVersion = '2018-11-19'
    _endpoint = 'ocr.tencentcloudapi.com'


    def ArithmeticOCR(self, request):
        """本介面支援作業算式題目的自動識别，目前函蓋 K12 學力範圍内的 14 種題型，包括加減乘除四則運算、分數四則運算、豎式四則運算、脫式計算等。

        :param request: Request instance for ArithmeticOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.ArithmeticOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.ArithmeticOCRResponse`

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


    def BankCardOCR(self, request):
        """本介面支援對中國大陸主流銀行卡的卡号、銀行訊息、有效期等關鍵欄位的檢測與識别。

        :param request: Request instance for BankCardOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.BankCardOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.BankCardOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BankCardOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BankCardOCRResponse()
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


    def BizLicenseOCR(self, request):
        """本介面支援快速精準識别營業執照上的欄位，包括注冊号、公司名稱、經營場所、主體類型、法定代表人、注冊資金、組成形式、成立日期、營業期限和經營範圍等欄位。

        :param request: Request instance for BizLicenseOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.BizLicenseOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.BizLicenseOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BizLicenseOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BizLicenseOCRResponse()
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


    def BusInvoiceOCR(self, request):
        """本介面支援識别公路汽車客票的發票代碼、發票号碼、日期、姓名、票價等欄位。

        :param request: Request instance for BusInvoiceOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.BusInvoiceOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.BusInvoiceOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BusInvoiceOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BusInvoiceOCRResponse()
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


    def BusinessCardOCR(self, request):
        """本介面支援名片各欄位的自動定位與識别，包含姓名、電話、手機号、電子信箱、公司、部門、職位、網址、網址、QQ、微信、MSN等。

        :param request: Request instance for BusinessCardOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.BusinessCardOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.BusinessCardOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BusinessCardOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BusinessCardOCRResponse()
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


    def CarInvoiceOCR(self, request):
        """本介面支援機動車銷售統一發票和二手車銷售統一發票的識别，包括發票号碼、發票代碼、合計金額、合計稅額等二十多個欄位。

        :param request: Request instance for CarInvoiceOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.CarInvoiceOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.CarInvoiceOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CarInvoiceOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CarInvoiceOCRResponse()
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


    def DriverLicenseOCR(self, request):
        """本介面支援駕駛證首頁和副頁所有欄位的自動定位與識别，重點欄位的識别準确度達到99%以上。

        駕駛證首頁：包括證号、姓名、性别、國籍、住址、出生日期、初次領證日期、準駕車型、有效期限。

        駕駛證副頁：包括證号、姓名、檔案編号、記錄。

        另外，本介面還支援影印件、翻拍和PS告警功能。

        :param request: Request instance for DriverLicenseOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.DriverLicenseOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.DriverLicenseOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DriverLicenseOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DriverLicenseOCRResponse()
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


    def DutyPaidProofOCR(self, request):
        """本介面支援對完稅證明的稅号、納稅人識别号、納稅人名稱、金額合計大寫、金額合計小寫、填發日期、稅務機關、填票人等關鍵欄位的識别。

        :param request: Request instance for DutyPaidProofOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.DutyPaidProofOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.DutyPaidProofOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DutyPaidProofOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DutyPaidProofOCRResponse()
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


    def EduPaperOCR(self, request):
        """本介面支援數學試題内容的識别和結構化輸出，包括通用文本解析和小學/初中/高中數學公式解析能力（包括91種題型，180種符号）。

        :param request: Request instance for EduPaperOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.EduPaperOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.EduPaperOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EduPaperOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EduPaperOCRResponse()
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

        :param request: Request instance for EnglishOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.EnglishOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.EnglishOCRResponse`

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


    def EnterpriseLicenseOCR(self, request):
        """本介面支援智慧化識别各類企業登記證書、許可證書、企業執照、三證合一類證書，結構化輸出統一社會信用代碼、公司名稱、法定代表人、公司網址、注冊資金、企業類型、經營範圍等關鍵欄位。

        :param request: Request instance for EnterpriseLicenseOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.EnterpriseLicenseOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.EnterpriseLicenseOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnterpriseLicenseOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnterpriseLicenseOCRResponse()
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


    def EstateCertOCR(self, request):
        """本介面支援不動産權證關鍵欄位的識别，包括使用期限、面積、用途、權利性質、權利類型、坐落、共有情況、權利人、權利其他狀況等。



        :param request: Request instance for EstateCertOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.EstateCertOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.EstateCertOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EstateCertOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EstateCertOCRResponse()
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


    def FinanBillOCR(self, request):
        """本介面支援常見銀行票據的自動分類和識别。整單識别包括支票（含現金支票、普通支票、轉賬支票），承兌匯票（含銀行承兌匯票、商業承兌匯票）以及進帳單等，适用于中國人民銀行印發的 2010 版銀行票據憑證版式（銀發[2010]299 号）。

        :param request: Request instance for FinanBillOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.FinanBillOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.FinanBillOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("FinanBillOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.FinanBillOCRResponse()
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


    def FinanBillSliceOCR(self, request):
        """本介面支援常見銀行票據的自動分類和識别。切片識别包括金融行業常見票據的重要切片欄位識别，包括金額、賬号、日期、憑證号碼等。（金融票據切片：金融票據中待識别欄位及其周圍局部區域的裁剪圖像。）

        :param request: Request instance for FinanBillSliceOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.FinanBillSliceOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.FinanBillSliceOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("FinanBillSliceOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.FinanBillSliceOCRResponse()
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


    def FlightInvoiceOCR(self, request):
        """本介面支援機票行程單關鍵欄位的識别，包括姓名、身份證件号碼、航班号、票價 、合計、電子客票号碼、填開日期等。

        :param request: Request instance for FlightInvoiceOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.FlightInvoiceOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.FlightInvoiceOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("FlightInvoiceOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.FlightInvoiceOCRResponse()
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


    def FormulaOCR(self, request):
        """本介面支援識别主流初高中數學符号和公式，返回公式的 Latex 格式文本。

        :param request: Request instance for FormulaOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.FormulaOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.FormulaOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("FormulaOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.FormulaOCRResponse()
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
        """本介面支援圖像整體文字的檢測和識别，返回文字框位置與文字内容。相比通用印刷體識别介面，高精度版在英文、數字、小字、模糊字、傾斜文本行等困難場景下，準确率和召回率更高。

        :param request: Request instance for GeneralAccurateOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.GeneralAccurateOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.GeneralAccurateOCRResponse`

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
        """本介面支援多場景、任意版面下整圖文字的識别。支援自動識别語言類型，同時支援自選語言種類（推薦），除中英文外，支援日語、韓語、西班牙語、法語、德語、葡萄牙語、越南語、馬來語、俄語、意大利語、荷蘭語、瑞典語、芬蘭語、丹麥語、挪威語、匈牙利語、泰語等多種語言。應用場景包括：印刷文件識别、網絡圖片識别、廣告圖文字識别、街景店招識别、清單識别、視訊标題識别、頭像文字識别等。

        :param request: Request instance for GeneralBasicOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.GeneralBasicOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.GeneralBasicOCRResponse`

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


    def GeneralEfficientOCR(self, request):
        """本介面支援多場景、任意版面下整圖文字的識别。相較于“通用印刷體識别”介面，精簡版介面在準召率有一定損失的情況下，耗時更短。适用于對介面耗時較爲敏感的客戶。

        :param request: Request instance for GeneralEfficientOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.GeneralEfficientOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.GeneralEfficientOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GeneralEfficientOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GeneralEfficientOCRResponse()
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

        :param request: Request instance for GeneralFastOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.GeneralFastOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.GeneralFastOCRResponse`

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


    def GeneralHandwritingOCR(self, request):
        """本介面支援圖片内手寫體文字的檢測和識别，針對手寫字體無規則、字迹潦草、模糊等特點進行了識别能力的增強。

        :param request: Request instance for GeneralHandwritingOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.GeneralHandwritingOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.GeneralHandwritingOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GeneralHandwritingOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GeneralHandwritingOCRResponse()
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


    def HmtResidentPermitOCR(self, request):
        """港澳台居住證OCR支援港澳台居住證正反面全欄位内容檢測識别功能，包括姓名、性别、出生日期、網址、身份證ID、簽發機關、有效期限、簽發次數、通行證号碼關鍵欄位識别。可以應用于港澳台居住證訊息有效性校驗場景，例如銀行開戶、用戶注冊等場景。

        :param request: Request instance for HmtResidentPermitOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.HmtResidentPermitOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.HmtResidentPermitOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("HmtResidentPermitOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.HmtResidentPermitOCRResponse()
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
        """本介面支援中國大陸居民二代身份證正反面所有欄位的識别，包括姓名、性别、民族、出生日期、住址、公民身份證号、簽發機關、有效期限，識别準确度達到99%以上。

        另外，本介面還支援多種增值能力，滿足不同場景的需求。如身份證照片、人像照片的裁剪功能，同時具備9種告警功能，如下表所示。

        <table style="width:650px">
              <thead>
                <tr>
               <th width="150">增值能力</th>
                  <th width="500">能力項</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td rowspan="2">裁剪功能</td>
                  <td>身份證照片裁剪（去掉證件外多餘的邊緣、自動矯正拍攝角度）</td>
                </tr>
                <tr>
                  <td>人像照片裁剪（自動摳取身份證頭像區域）</td>
                </tr>
                <tr>
                  <td rowspan="9">告警功能</td>
                  <td>身份證有效日期不合法告警</td>
                </tr>
                <tr>
                  <td>身份證邊框不完整告警</td>
                </tr>
                <tr>
                  <td>身份證影印件告警</td>
                </tr>
                <tr>
                  <td>身份證翻拍告警</td>
                </tr>
                  <tr>
                  <td>身份證框内遮擋告警</td>
                </tr>
                 <tr>
                  <td>臨時身份證告警</td>
                </tr>
                  <tr>
                  <td>身份證 PS 告警</td>
                </tr>
                  <tr>
                  <td>圖片模糊告警</td>
                </tr>
              </tbody>
            </table>

        :param request: Request instance for IDCardOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.IDCardOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.IDCardOCRResponse`

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


    def InstitutionOCR(self, request):
        """本介面支援事業單位法人證書關鍵欄位識别，包括注冊号、有效期、住所、名稱、法定代表人等。

        :param request: Request instance for InstitutionOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.InstitutionOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.InstitutionOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InstitutionOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InstitutionOCRResponse()
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


    def InsuranceBillOCR(self, request):
        """本介面支援病案首頁、費用清單、結算單、醫療發票四種保險理賠單據的文本識别和結構化輸出。

        :param request: Request instance for InsuranceBillOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.InsuranceBillOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.InsuranceBillOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InsuranceBillOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InsuranceBillOCRResponse()
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


    def InvoiceGeneralOCR(self, request):
        """本介面支援對通用機打發票的發票代碼、發票号碼、日期、購買方識别号、銷售方識别号、校驗碼、小寫金額等關鍵欄位的識别。

        :param request: Request instance for InvoiceGeneralOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.InvoiceGeneralOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.InvoiceGeneralOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InvoiceGeneralOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InvoiceGeneralOCRResponse()
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


    def LicensePlateOCR(self, request):
        """本介面支援對中國大陸機動車車牌的自動定位和識别，返回地域編号和車牌号訊息。

        :param request: Request instance for LicensePlateOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.LicensePlateOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.LicensePlateOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("LicensePlateOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.LicensePlateOCRResponse()
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


    def MLIDCardOCR(self, request):
        """本介面支援馬來西亞身份證識别，識别欄位包括身份證号、姓名、性别、網址；具備身份證人像照片的裁剪功能和翻拍、影印件告警功能。
        本介面暫未完全對外開放，如需咨詢，請[聯系商務](https://cloud.tencent.com/about/connect)

        :param request: Request instance for MLIDCardOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.MLIDCardOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.MLIDCardOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MLIDCardOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MLIDCardOCRResponse()
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


    def MLIDPassportOCR(self, request):
        """本介面支援中國港澳台地區以及其他國家、地區的護照。識别欄位包括護照ID、姓名、出生日期、性别、有效期、發行國、國籍；具備護照人像照片的裁剪功能和翻拍、影印件告警功能。
        本介面暫未完全對外開放，如需咨詢，請[聯系商務](https://cloud.tencent.com/about/connect)

        :param request: Request instance for MLIDPassportOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.MLIDPassportOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.MLIDPassportOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MLIDPassportOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MLIDPassportOCRResponse()
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


    def MainlandPermitOCR(self, request):
        """智慧識别并結構化港澳台居民來往内地通行證正面全部欄位，包含中文姓名、英文姓名、性别、出生日期、簽發機關、有效期限、證件号、簽發地點、簽發次數、證件類别。

        :param request: Request instance for MainlandPermitOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.MainlandPermitOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.MainlandPermitOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MainlandPermitOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MainlandPermitOCRResponse()
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


    def MixedInvoiceDetect(self, request):
        """本介面支援多張、多類型票據的混合檢測和自動分類，返回對應票據類型。目前已支援增值稅發票、增值稅發票（卷票）、定額發票、通用機打發票、購車發票、火車票、出租車發票、機票行程單、汽車票、輪船票、過路過橋費發票、酒店帳單、客運限額發票、購物小票、完稅證明共15種票據。

        :param request: Request instance for MixedInvoiceDetect.
        :type request: :class:`tencentcloud.ocr.v20181119.models.MixedInvoiceDetectRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.MixedInvoiceDetectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MixedInvoiceDetect", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MixedInvoiceDetectResponse()
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


    def MixedInvoiceOCR(self, request):
        """本介面支援多張、多類型票據的混合識别，系統自動實現分割、分類和識别，同時支援自選需要識别的票據類型。目前已支援增值稅發票、增值稅發票（卷票）、定額發票、通用機打發票、購車發票、火車票、出租車發票、機票行程單、汽車票、輪船票、過路過橋費發票共11種票據。

        :param request: Request instance for MixedInvoiceOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.MixedInvoiceOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.MixedInvoiceOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MixedInvoiceOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MixedInvoiceOCRResponse()
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


    def OrgCodeCertOCR(self, request):
        """本介面支援組織機構代碼證關鍵欄位的識别，包括代碼、有效期、網址、機構名稱等。

        :param request: Request instance for OrgCodeCertOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.OrgCodeCertOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.OrgCodeCertOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OrgCodeCertOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OrgCodeCertOCRResponse()
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


    def PassportOCR(self, request):
        """本介面支援中國大陸地區護照個人資料頁多個欄位的檢測與識别。已支援欄位包括英文姓名、中文姓名、國家碼、護照号、出生地、出生日期、國籍英文、性别英文、有效期、簽發地點英文、簽發日期、持證人簽名、護照機讀碼（MRZ碼）等。

        :param request: Request instance for PassportOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.PassportOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.PassportOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PassportOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PassportOCRResponse()
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


    def PermitOCR(self, request):
        """本介面支援對卡式港澳台通行證的識别，包括簽發地點、簽發機關、有效期限、性别、出生日期、英文姓名、姓名、證件号等欄位。

        :param request: Request instance for PermitOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.PermitOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.PermitOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PermitOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PermitOCRResponse()
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


    def PropOwnerCertOCR(self, request):
        """本介面支援房産證關鍵欄位的識别，包括房地産權利人、共有情況、登記時間、規劃用途、房屋性質、房屋坐落等。

        :param request: Request instance for PropOwnerCertOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.PropOwnerCertOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.PropOwnerCertOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PropOwnerCertOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PropOwnerCertOCRResponse()
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


    def QrcodeOCR(self, request):
        """本介面支援條形碼和二維碼的識别（包括 DataMatrix 和 PDF417）。
        本介面暫未完全對外開放，如需咨詢，請[聯系商務](https://cloud.tencent.com/about/connect)

        :param request: Request instance for QrcodeOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.QrcodeOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.QrcodeOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QrcodeOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QrcodeOCRResponse()
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


    def QuotaInvoiceOCR(self, request):
        """本介面支援定額發票的發票号碼、發票代碼、金額(大小寫)、發票消費類型、地區及是否有公司印章等關鍵欄位的識别。

        :param request: Request instance for QuotaInvoiceOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.QuotaInvoiceOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.QuotaInvoiceOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QuotaInvoiceOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QuotaInvoiceOCRResponse()
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


    def ResidenceBookletOCR(self, request):
        """本介面支援居民戶口簿戶首頁及成員頁關鍵欄位的識别，包括姓名、戶别、網址、籍貫、身份證号碼等。

        :param request: Request instance for ResidenceBookletOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.ResidenceBookletOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.ResidenceBookletOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResidenceBookletOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResidenceBookletOCRResponse()
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


    def ShipInvoiceOCR(self, request):
        """本介面支援識别輪船票的發票代碼、發票号碼、日期、姓名、票價等欄位。

        :param request: Request instance for ShipInvoiceOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.ShipInvoiceOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.ShipInvoiceOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ShipInvoiceOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ShipInvoiceOCRResponse()
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

        :param request: Request instance for TableOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.TableOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TableOCRResponse`

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


    def TaxiInvoiceOCR(self, request):
        """本介面支援出租車發票關鍵欄位的識别，包括發票号碼、發票代碼、金額、日期、上下車時間、裏程、車牌号、發票類型及所屬地區等欄位。

        :param request: Request instance for TaxiInvoiceOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.TaxiInvoiceOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TaxiInvoiceOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TaxiInvoiceOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TaxiInvoiceOCRResponse()
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


    def TextDetect(self, request):
        """本介面通過檢測圖片中的文字訊息特征，快速判斷圖片中有無文字并返回判斷結果，幫助用戶過濾無文字的圖片。

        :param request: Request instance for TextDetect.
        :type request: :class:`tencentcloud.ocr.v20181119.models.TextDetectRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TextDetect", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TextDetectResponse()
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


    def TollInvoiceOCR(self, request):
        """本介面支援對過路過橋費發票的發票代碼、發票号碼、日期、小寫金額等關鍵欄位的識别。

        :param request: Request instance for TollInvoiceOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.TollInvoiceOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TollInvoiceOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TollInvoiceOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TollInvoiceOCRResponse()
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


    def TrainTicketOCR(self, request):
        """本介面支援火車票全欄位的識别，包括編号、票價、姓名、座位号、出發時間、出發站、到達站、車次、席别、發票類型及序列号等。

        :param request: Request instance for TrainTicketOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.TrainTicketOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TrainTicketOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TrainTicketOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TrainTicketOCRResponse()
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


    def VatInvoiceOCR(self, request):
        """本介面支援增值稅專用發票、增值稅普通發票、增值稅電子發票全欄位的内容檢測和識别，包括發票代碼、發票号碼、開票日期、合計金額、校驗碼、稅率、合計稅額、價稅合計、購買方識别号、複核、銷售方識别号、開票人、密碼區1、密碼區2、密碼區3、密碼區4、發票名稱、購買方名稱、銷售方名稱、服務名稱、備注、規格型号、數量、單價、金額、稅額、收款人等欄位。

        :param request: Request instance for VatInvoiceOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VatInvoiceOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VatInvoiceOCRResponse()
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


    def VatRollInvoiceOCR(self, request):
        """本介面支援對增值稅發票（卷票）的發票代碼、發票号碼、日期、校驗碼、合計金額（小寫）等關鍵欄位的識别。

        :param request: Request instance for VatRollInvoiceOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.VatRollInvoiceOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.VatRollInvoiceOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VatRollInvoiceOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VatRollInvoiceOCRResponse()
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


    def VehicleLicenseOCR(self, request):
        """本介面支援行駛證首頁和副頁所有欄位的自動定位與識别。

        行駛證首頁：車牌号碼、車輛類型、所有人、住址、使用性質、品牌型号、識别代碼、發動機号、注冊日期、發證日期、發證單位。

        行駛證副頁：号牌号碼、檔案編号、核定載人數、總質量、整備質量、核定載質量、外廓尺寸、準牽引總質量、備注、檢驗記錄。

        另外，本介面還支援影印件、翻拍和PS告警功能。

        :param request: Request instance for VehicleLicenseOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.VehicleLicenseOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.VehicleLicenseOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VehicleLicenseOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VehicleLicenseOCRResponse()
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


    def VehicleRegCertOCR(self, request):
        """本介面支援國内機動車登記證書主要欄位的結構化識别，包括機動車所有人、身份證明名稱、号碼、車輛型号、車輛識别代号、發動機号、制造廠名稱等。

        :param request: Request instance for VehicleRegCertOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.VehicleRegCertOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.VehicleRegCertOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VehicleRegCertOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VehicleRegCertOCRResponse()
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
        """本介面支援圖片内車輛識别代号（VIN）的檢測和識别。

        :param request: Request instance for VinOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.VinOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.VinOCRResponse`

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
        """本介面支援市面上主流版式電子運單的識别，包括收件人和寄件人的姓名、電話、網址以及運單号等欄位。

        :param request: Request instance for WaybillOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.WaybillOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.WaybillOCRResponse`

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