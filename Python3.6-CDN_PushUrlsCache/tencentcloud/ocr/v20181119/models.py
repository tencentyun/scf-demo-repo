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

from taifucloudcloud.common.abstract_model import AbstractModel


class ArithmeticOCRRequest(AbstractModel):
    """ArithmeticOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class ArithmeticOCRResponse(AbstractModel):
    """ArithmeticOCR返回參數結構體

    """

    def __init__(self):
        """
        :param TextDetections: 檢測到的文本訊息，具體内容請點擊左側連結。
        :type TextDetections: list of TextArithmetic
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextArithmetic()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.RequestId = params.get("RequestId")


class BankCardOCRRequest(AbstractModel):
    """BankCardOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 7M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 7M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class BankCardOCRResponse(AbstractModel):
    """BankCardOCR返回參數結構體

    """

    def __init__(self):
        """
        :param CardNo: 卡號
        :type CardNo: str
        :param BankInfo: 銀行訊息
        :type BankInfo: str
        :param ValidDate: 有效期
        :type ValidDate: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CardNo = None
        self.BankInfo = None
        self.ValidDate = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CardNo = params.get("CardNo")
        self.BankInfo = params.get("BankInfo")
        self.ValidDate = params.get("ValidDate")
        self.RequestId = params.get("RequestId")


class BizLicenseOCRRequest(AbstractModel):
    """BizLicenseOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 7M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 7M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class BizLicenseOCRResponse(AbstractModel):
    """BizLicenseOCR返回參數結構體

    """

    def __init__(self):
        """
        :param RegNum: 注冊號
        :type RegNum: str
        :param Name: 公司名稱
        :type Name: str
        :param Capital: 注冊資本
        :type Capital: str
        :param Person: 法定代表人
        :type Person: str
        :param Address: 網址
        :type Address: str
        :param Business: 經營範圍
        :type Business: str
        :param Type: 主體類型
        :type Type: str
        :param Period: 營業期限
        :type Period: str
        :param ComposingForm: 組成形式
        :type ComposingForm: str
        :param SetDate: 成立日期
        :type SetDate: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RegNum = None
        self.Name = None
        self.Capital = None
        self.Person = None
        self.Address = None
        self.Business = None
        self.Type = None
        self.Period = None
        self.ComposingForm = None
        self.SetDate = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegNum = params.get("RegNum")
        self.Name = params.get("Name")
        self.Capital = params.get("Capital")
        self.Person = params.get("Person")
        self.Address = params.get("Address")
        self.Business = params.get("Business")
        self.Type = params.get("Type")
        self.Period = params.get("Period")
        self.ComposingForm = params.get("ComposingForm")
        self.SetDate = params.get("SetDate")
        self.RequestId = params.get("RequestId")


class BusInvoiceInfo(AbstractModel):
    """汽車票欄位訊息

    """

    def __init__(self):
        """
        :param Name: 識别出的欄位名稱（關鍵字）。
        :type Name: str
        :param Value: 識别出的欄位名稱對應的值，也就是欄位Name對應的字串結果。
        :type Value: str
        :param Rect: 文本行在旋轉糾正之後的圖像中的像素坐標。
        :type Rect: :class:`taifucloudcloud.ocr.v20181119.models.Rect`
        """
        self.Name = None
        self.Value = None
        self.Rect = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        if params.get("Rect") is not None:
            self.Rect = Rect()
            self.Rect._deserialize(params.get("Rect"))


class BusInvoiceOCRRequest(AbstractModel):
    """BusInvoiceOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class BusInvoiceOCRResponse(AbstractModel):
    """BusInvoiceOCR返回參數結構體

    """

    def __init__(self):
        """
        :param BusInvoiceInfos: 汽車票識别結果，具體内容請點擊左側連結。
        :type BusInvoiceInfos: list of BusInvoiceInfo
        :param Angle: 圖片旋轉角度（角度制），文本的水平方向爲0°，順時針爲正，逆時針爲負。
        :type Angle: float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.BusInvoiceInfos = None
        self.Angle = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BusInvoiceInfos") is not None:
            self.BusInvoiceInfos = []
            for item in params.get("BusInvoiceInfos"):
                obj = BusInvoiceInfo()
                obj._deserialize(item)
                self.BusInvoiceInfos.append(obj)
        self.Angle = params.get("Angle")
        self.RequestId = params.get("RequestId")


class BusinessCardInfo(AbstractModel):
    """名片識别結果

    """

    def __init__(self):
        """
        :param Name: 識别出的欄位名稱（關鍵字，可能重複，比如多個手機），能識别的欄位名爲：
姓名、英文姓名、英文網址、公司、英文公司、職位、英文職位、部門、英文部門、手機、電話、傳真、社交帳號、 、MSN、 、 、電子信箱、郵編、網址、公司賬號、其他。
        :type Name: str
        :param Value: 識别出的欄位名稱對應的值，也就是欄位name對應的字串結果。
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class BusinessCardOCRRequest(AbstractModel):
    """BusinessCardOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 7M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 7M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        :param Config: 可選欄位，根據需要選擇是否請求對應欄位。
目前支援的欄位爲：
RetImageType-“PROPROCESS” 圖像預處理，string 類型。
圖像預處理功能爲，檢測圖片傾斜的角度，将原本傾斜的圖片圍繞中心點轉正，最終輸出一張正的名片摳圖。

SDK 設置方式參考：
Config = Json.stringify({"RetImageType":"PROPROCESS"})
API 3.0 Explorer 設置方式參考：
Config = {"RetImageType":"PROPROCESS"}
        :type Config: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.Config = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.Config = params.get("Config")


class BusinessCardOCRResponse(AbstractModel):
    """BusinessCardOCR返回參數結構體

    """

    def __init__(self):
        """
        :param BusinessCardInfos: 名片識别結果，具體内容請點擊左側連結。
        :type BusinessCardInfos: list of BusinessCardInfo
        :param RetImageBase64: 返回圖像預處理後的圖片，圖像預處理未開啓時返回内容爲空。
        :type RetImageBase64: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.BusinessCardInfos = None
        self.RetImageBase64 = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BusinessCardInfos") is not None:
            self.BusinessCardInfos = []
            for item in params.get("BusinessCardInfos"):
                obj = BusinessCardInfo()
                obj._deserialize(item)
                self.BusinessCardInfos.append(obj)
        self.RetImageBase64 = params.get("RetImageBase64")
        self.RequestId = params.get("RequestId")


class CarInvoiceInfo(AbstractModel):
    """購車發票識别結果

    """

    def __init__(self):
        """
        :param Name: 識别出的欄位名稱（關鍵字）。
        :type Name: str
        :param Value: 識别出的欄位名稱對應的值，也就是欄位name對應的字串結果。
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class CarInvoiceOCRRequest(AbstractModel):
    """CarInvoiceOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class CarInvoiceOCRResponse(AbstractModel):
    """CarInvoiceOCR返回參數結構體

    """

    def __init__(self):
        """
        :param CarInvoiceInfos: 購車發票識别結果，具體内容請點擊左側連結。
        :type CarInvoiceInfos: list of CarInvoiceInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CarInvoiceInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CarInvoiceInfos") is not None:
            self.CarInvoiceInfos = []
            for item in params.get("CarInvoiceInfos"):
                obj = CarInvoiceInfo()
                obj._deserialize(item)
                self.CarInvoiceInfos.append(obj)
        self.RequestId = params.get("RequestId")


class Coord(AbstractModel):
    """坐標

    """

    def __init__(self):
        """
        :param X: 橫坐標
        :type X: int
        :param Y: 縱坐標
        :type Y: int
        """
        self.X = None
        self.Y = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")


class DriverLicenseOCRRequest(AbstractModel):
    """DriverLicenseOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。要求圖片經Base64編碼後不超過 7M，分辨率建議500*800以上，支援PNG、JPG、JPEG、BMP格式。建議卡片部分占據圖片2/3以上。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。要求圖片經Base64編碼後不超過 7M，分辨率建議500*800以上，支援PNG、JPG、JPEG、BMP格式。建議卡片部分占據圖片2/3以上。圖片下載時間不超過 3 秒。
建議圖片儲存於Top Cloud ，可保障更高的下載速度和穩定性。
        :type ImageUrl: str
        :param CardSide: FRONT 爲駕駛證首頁正面（有紅色印章的一面），
BACK 爲駕駛證副頁正面（有檔案編號的一面）。
        :type CardSide: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.CardSide = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.CardSide = params.get("CardSide")


class DriverLicenseOCRResponse(AbstractModel):
    """DriverLicenseOCR返回參數結構體

    """

    def __init__(self):
        """
        :param Name: 姓名
        :type Name: str
        :param Sex: 性别
        :type Sex: str
        :param Nationality: 國籍
        :type Nationality: str
        :param Address: 住址
        :type Address: str
        :param DateOfBirth: 出生日期
        :type DateOfBirth: str
        :param DateOfFirstIssue: 初次領證日期
        :type DateOfFirstIssue: str
        :param Class: 準駕車型
        :type Class: str
        :param StartDate: 有效期開始時間
        :type StartDate: str
        :param EndDate: 有效期截止時間
        :type EndDate: str
        :param CardCode: 證號
        :type CardCode: str
        :param ArchivesCode: 檔案編號
        :type ArchivesCode: str
        :param Record: 記錄
        :type Record: str
        :param RecognizeWarnCode: Code 告警碼清單和釋義：
-9102  影印件告警
-9103  翻拍件告警
-9106  ps告警
注：告警碼可以同時存在多個
        :type RecognizeWarnCode: list of int
        :param RecognizeWarnMsg: 告警碼說明：
WARN_DRIVER_LICENSE_COPY_CARD 影印件告警
WARN_DRIVER_LICENSE_SCREENED_CARD 翻拍件告警
WARN_DRIVER_LICENSE_PS_CARD ps告警
注：告警訊息可以同時存在多個
        :type RecognizeWarnMsg: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.Sex = None
        self.Nationality = None
        self.Address = None
        self.DateOfBirth = None
        self.DateOfFirstIssue = None
        self.Class = None
        self.StartDate = None
        self.EndDate = None
        self.CardCode = None
        self.ArchivesCode = None
        self.Record = None
        self.RecognizeWarnCode = None
        self.RecognizeWarnMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Sex = params.get("Sex")
        self.Nationality = params.get("Nationality")
        self.Address = params.get("Address")
        self.DateOfBirth = params.get("DateOfBirth")
        self.DateOfFirstIssue = params.get("DateOfFirstIssue")
        self.Class = params.get("Class")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.CardCode = params.get("CardCode")
        self.ArchivesCode = params.get("ArchivesCode")
        self.Record = params.get("Record")
        self.RecognizeWarnCode = params.get("RecognizeWarnCode")
        self.RecognizeWarnMsg = params.get("RecognizeWarnMsg")
        self.RequestId = params.get("RequestId")


class DutyPaidProofInfo(AbstractModel):
    """識别出的欄位

    """

    def __init__(self):
        """
        :param Name: 識别出的欄位名稱（關鍵字）。
        :type Name: str
        :param Value: 識别出的欄位名稱對應的值，也就是欄位Name對應的字串結果。
        :type Value: str
        :param Rect: 文本行在旋轉糾正之後的圖像中的像素坐標。
        :type Rect: :class:`taifucloudcloud.ocr.v20181119.models.Rect`
        """
        self.Name = None
        self.Value = None
        self.Rect = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        if params.get("Rect") is not None:
            self.Rect = Rect()
            self.Rect._deserialize(params.get("Rect"))


class DutyPaidProofOCRRequest(AbstractModel):
    """DutyPaidProofOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class DutyPaidProofOCRResponse(AbstractModel):
    """DutyPaidProofOCR返回參數結構體

    """

    def __init__(self):
        """
        :param DutyPaidProofInfos: 完稅證明識别結果，具體内容請點擊左側連結。
        :type DutyPaidProofInfos: list of DutyPaidProofInfo
        :param Angle: 圖片旋轉角度（角度制），文本的水平方向爲0°，順時針爲正，逆時針爲負。
        :type Angle: float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DutyPaidProofInfos = None
        self.Angle = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DutyPaidProofInfos") is not None:
            self.DutyPaidProofInfos = []
            for item in params.get("DutyPaidProofInfos"):
                obj = DutyPaidProofInfo()
                obj._deserialize(item)
                self.DutyPaidProofInfos.append(obj)
        self.Angle = params.get("Angle")
        self.RequestId = params.get("RequestId")


class EduPaperOCRRequest(AbstractModel):
    """EduPaperOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        :param Config: 擴展配置訊息。
配置格式：{"option1":value1,"option2":value2}
可配置訊息：
      參數名稱  是否必選   類型   可選值  預設值  描述
      task_type  否  Int32  [0,1]  1  用於選擇任務類型: 0: 關閉版式分析與處理 1: 開啓版式分析處理
      is_structuralization 否 Bool false\true true  用於選擇是否結構化輸出：false：返回包體返回通用輸出 true：返回包體同時返回通用和結構化輸出
      if_readable_format 否 Bool false\true false 是否按照版式整合通用文本/公式輸出結果
例子：
{"task_type": 1,"is_structuralization": true,"if_readable_format": true}
        :type Config: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.Config = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.Config = params.get("Config")


class EduPaperOCRResponse(AbstractModel):
    """EduPaperOCR返回參數結構體

    """

    def __init__(self):
        """
        :param EduPaperInfos: 檢測到的文本訊息，具體内容請點擊左側連結。
        :type EduPaperInfos: list of TextEduPaper
        :param Angle: 圖片旋轉角度（角度制），文本的水平方向爲0°；順時針爲正，逆時針爲負。
        :type Angle: int
        :param QuestionBlockInfos: 結構化方式輸出，具體内容請點擊左側連結。
        :type QuestionBlockInfos: list of QuestionBlockObj
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.EduPaperInfos = None
        self.Angle = None
        self.QuestionBlockInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EduPaperInfos") is not None:
            self.EduPaperInfos = []
            for item in params.get("EduPaperInfos"):
                obj = TextEduPaper()
                obj._deserialize(item)
                self.EduPaperInfos.append(obj)
        self.Angle = params.get("Angle")
        if params.get("QuestionBlockInfos") is not None:
            self.QuestionBlockInfos = []
            for item in params.get("QuestionBlockInfos"):
                obj = QuestionBlockObj()
                obj._deserialize(item)
                self.QuestionBlockInfos.append(obj)
        self.RequestId = params.get("RequestId")


class EnglishOCRRequest(AbstractModel):
    """EnglishOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class EnglishOCRResponse(AbstractModel):
    """EnglishOCR返回參數結構體

    """

    def __init__(self):
        """
        :param TextDetections: 檢測到的文本訊息，具體内容請點擊左側連結。
        :type TextDetections: list of TextDetectionEn
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextDetectionEn()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.RequestId = params.get("RequestId")


class EnterpriseLicenseInfo(AbstractModel):
    """企業證照單個欄位的内容

    """

    def __init__(self):
        """
        :param Name: 識别出的欄位名稱。
        :type Name: str
        :param Value: 識别出的欄位名稱對應的值，也就是欄位Name對應的字串結果。
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class EnterpriseLicenseOCRRequest(AbstractModel):
    """EnterpriseLicenseOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class EnterpriseLicenseOCRResponse(AbstractModel):
    """EnterpriseLicenseOCR返回參數結構體

    """

    def __init__(self):
        """
        :param EnterpriseLicenseInfos: 企業證照識别結果，具體内容請點擊左側連結。
        :type EnterpriseLicenseInfos: list of EnterpriseLicenseInfo
        :param Angle: 圖片旋轉角度（角度制），文本的水平方向爲0°，順時針爲正，逆時針爲負。
        :type Angle: float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.EnterpriseLicenseInfos = None
        self.Angle = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EnterpriseLicenseInfos") is not None:
            self.EnterpriseLicenseInfos = []
            for item in params.get("EnterpriseLicenseInfos"):
                obj = EnterpriseLicenseInfo()
                obj._deserialize(item)
                self.EnterpriseLicenseInfos.append(obj)
        self.Angle = params.get("Angle")
        self.RequestId = params.get("RequestId")


class EstateCertOCRRequest(AbstractModel):
    """EstateCertOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class EstateCertOCRResponse(AbstractModel):
    """EstateCertOCR返回參數結構體

    """

    def __init__(self):
        """
        :param Obligee: 權利人
        :type Obligee: str
        :param Ownership: 共有情況
        :type Ownership: str
        :param Location: 坐落
        :type Location: str
        :param Unit: 不動産單元號
        :type Unit: str
        :param Type: 權利類型
        :type Type: str
        :param Property: 權利性質
        :type Property: str
        :param Usage: 用途
        :type Usage: str
        :param Area: 面積
        :type Area: str
        :param Term: 使用期限
        :type Term: str
        :param Other: 權利其他狀況，多行會用換行符\n連接。
        :type Other: str
        :param Angle: 圖片旋轉角度
        :type Angle: float
        :param Number: 不動産權號
        :type Number: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Obligee = None
        self.Ownership = None
        self.Location = None
        self.Unit = None
        self.Type = None
        self.Property = None
        self.Usage = None
        self.Area = None
        self.Term = None
        self.Other = None
        self.Angle = None
        self.Number = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Obligee = params.get("Obligee")
        self.Ownership = params.get("Ownership")
        self.Location = params.get("Location")
        self.Unit = params.get("Unit")
        self.Type = params.get("Type")
        self.Property = params.get("Property")
        self.Usage = params.get("Usage")
        self.Area = params.get("Area")
        self.Term = params.get("Term")
        self.Other = params.get("Other")
        self.Angle = params.get("Angle")
        self.Number = params.get("Number")
        self.RequestId = params.get("RequestId")


class FinanBillInfo(AbstractModel):
    """金融票據整單識别單個欄位的内容

    """

    def __init__(self):
        """
        :param Name: 識别出的欄位名稱。
        :type Name: str
        :param Value: 識别出的欄位名稱對應的值，也就是欄位Name對應的字串結果。
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class FinanBillOCRRequest(AbstractModel):
    """FinanBillOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class FinanBillOCRResponse(AbstractModel):
    """FinanBillOCR返回參數結構體

    """

    def __init__(self):
        """
        :param FinanBillInfos: 金融票據整單識别結果，具體内容請點擊左側連結。
        :type FinanBillInfos: list of FinanBillInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FinanBillInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FinanBillInfos") is not None:
            self.FinanBillInfos = []
            for item in params.get("FinanBillInfos"):
                obj = FinanBillInfo()
                obj._deserialize(item)
                self.FinanBillInfos.append(obj)
        self.RequestId = params.get("RequestId")


class FinanBillSliceInfo(AbstractModel):
    """金融票據切片識别單個欄位的内容

    """

    def __init__(self):
        """
        :param Name: 識别出的欄位名稱。
        :type Name: str
        :param Value: 識别出的欄位名稱對應的值，也就是欄位Name對應的字串結果。
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class FinanBillSliceOCRRequest(AbstractModel):
    """FinanBillSliceOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class FinanBillSliceOCRResponse(AbstractModel):
    """FinanBillSliceOCR返回參數結構體

    """

    def __init__(self):
        """
        :param FinanBillSliceInfos: 金融票據切片識别結果，具體内容請點擊左側連結。
        :type FinanBillSliceInfos: list of FinanBillSliceInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FinanBillSliceInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FinanBillSliceInfos") is not None:
            self.FinanBillSliceInfos = []
            for item in params.get("FinanBillSliceInfos"):
                obj = FinanBillSliceInfo()
                obj._deserialize(item)
                self.FinanBillSliceInfos.append(obj)
        self.RequestId = params.get("RequestId")


class FlightInvoiceInfo(AbstractModel):
    """機票行程單識别結果

    """

    def __init__(self):
        """
        :param Name: 識别出的欄位名稱（關鍵字）。
        :type Name: str
        :param Value: 識别出的欄位名稱對應的值，也就是欄位 Name 對應的字串結果。
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class FlightInvoiceOCRRequest(AbstractModel):
    """FlightInvoiceOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class FlightInvoiceOCRResponse(AbstractModel):
    """FlightInvoiceOCR返回參數結構體

    """

    def __init__(self):
        """
        :param FlightInvoiceInfos: 機票行程單識别結果，具體内容請點擊左側連結。
        :type FlightInvoiceInfos: list of FlightInvoiceInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FlightInvoiceInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FlightInvoiceInfos") is not None:
            self.FlightInvoiceInfos = []
            for item in params.get("FlightInvoiceInfos"):
                obj = FlightInvoiceInfo()
                obj._deserialize(item)
                self.FlightInvoiceInfos.append(obj)
        self.RequestId = params.get("RequestId")


class FormulaOCRRequest(AbstractModel):
    """FormulaOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class FormulaOCRResponse(AbstractModel):
    """FormulaOCR返回參數結構體

    """

    def __init__(self):
        """
        :param Angle: 圖片旋轉角度（角度制），文本的水平方向爲0°；順時針爲正，逆時針爲負
        :type Angle: int
        :param FormulaInfos: 檢測到的文本訊息，具體内容請點擊左側連結。
        :type FormulaInfos: list of TextFormula
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Angle = None
        self.FormulaInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Angle = params.get("Angle")
        if params.get("FormulaInfos") is not None:
            self.FormulaInfos = []
            for item in params.get("FormulaInfos"):
                obj = TextFormula()
                obj._deserialize(item)
                self.FormulaInfos.append(obj)
        self.RequestId = params.get("RequestId")


class GeneralAccurateOCRRequest(AbstractModel):
    """GeneralAccurateOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class GeneralAccurateOCRResponse(AbstractModel):
    """GeneralAccurateOCR返回參數結構體

    """

    def __init__(self):
        """
        :param TextDetections: 檢測到的文本訊息，具體内容請點擊左側連結。
        :type TextDetections: list of TextDetection
        :param Angel: 圖片旋轉角度（角度制），文本的水平方向爲0°；順時針爲正，逆時針爲負
        :type Angel: float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.Angel = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextDetection()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.Angel = params.get("Angel")
        self.RequestId = params.get("RequestId")


class GeneralBasicOCRRequest(AbstractModel):
    """GeneralBasicOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        :param Scene: 保留欄位。
        :type Scene: str
        :param LanguageType: 識别語言類型。
支援自動識别語言類型，同時支援自選語言種類，預設中英文混合(zh)。
可選值：
zh\auto\jap\kor\
spa\fre\ger\por\
vie\may\rus\ita\
hol\swe\fin\dan\
nor\hun\tha\lat
可選值分别表示：
中英文混合、自動識别、日語、韓語、
西班牙語、法語、德語、葡萄牙語、
越南語、馬來語、俄語、意大利語、
荷蘭語、瑞典語、芬蘭語、丹麥語、
挪威語、匈牙利語、泰語、拉丁語系。
        :type LanguageType: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.Scene = None
        self.LanguageType = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.Scene = params.get("Scene")
        self.LanguageType = params.get("LanguageType")


class GeneralBasicOCRResponse(AbstractModel):
    """GeneralBasicOCR返回參數結構體

    """

    def __init__(self):
        """
        :param TextDetections: 檢測到的文本訊息，具體内容請點擊左側連結。
        :type TextDetections: list of TextDetection
        :param Language: 檢測到的語言類型，目前支援的語言類型參考入參LanguageType說明。
        :type Language: str
        :param Angel: 圖片旋轉角度（角度制），文本的水平方向爲0°；順時針爲正，逆時針爲負
        :type Angel: float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.Language = None
        self.Angel = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextDetection()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.Language = params.get("Language")
        self.Angel = params.get("Angel")
        self.RequestId = params.get("RequestId")


class GeneralEfficientOCRRequest(AbstractModel):
    """GeneralEfficientOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class GeneralEfficientOCRResponse(AbstractModel):
    """GeneralEfficientOCR返回參數結構體

    """

    def __init__(self):
        """
        :param TextDetections: 檢測到的文本訊息，具體内容請點擊左側連結。
        :type TextDetections: list of TextDetection
        :param Angel: 圖片旋轉角度（角度制），文本的水平方向爲0°；順時針爲正，逆時針爲負
        :type Angel: float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.Angel = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextDetection()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.Angel = params.get("Angel")
        self.RequestId = params.get("RequestId")


class GeneralFastOCRRequest(AbstractModel):
    """GeneralFastOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class GeneralFastOCRResponse(AbstractModel):
    """GeneralFastOCR返回參數結構體

    """

    def __init__(self):
        """
        :param TextDetections: 檢測到的文本訊息，具體内容請點擊左側連結。
        :type TextDetections: list of TextDetection
        :param Language: 檢測到的語言，目前支援的語種範圍爲：簡體中文、繁體中文、英文、日文、韓文。未來将陸續新增對更多語種的支援。
返回結果含義爲：zh - 中英混合，jap - 日文，kor - 韓文。
        :type Language: str
        :param Angel: 圖片旋轉角度（角度制），文本的水平方向爲0°；順時針爲正，逆時針爲負
        :type Angel: float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.Language = None
        self.Angel = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextDetection()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.Language = params.get("Language")
        self.Angel = params.get("Angel")
        self.RequestId = params.get("RequestId")


class GeneralHandwritingOCRRequest(AbstractModel):
    """GeneralHandwritingOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        :param Scene: 場景欄位，預設不用填寫。
可選值:only_hw  表示只輸出手寫體識别結果，過濾印刷體。
        :type Scene: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.Scene = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.Scene = params.get("Scene")


class GeneralHandwritingOCRResponse(AbstractModel):
    """GeneralHandwritingOCR返回參數結構體

    """

    def __init__(self):
        """
        :param TextDetections: 檢測到的文本訊息，具體内容請點擊左側連結。
        :type TextDetections: list of TextGeneralHandwriting
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextGeneralHandwriting()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.RequestId = params.get("RequestId")


class HmtResidentPermitOCRRequest(AbstractModel):
    """HmtResidentPermitOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        :param CardSide: FRONT：有照片的一面（人像面），
BACK：無照片的一面（國徽面），
該參數如果不填或填錯，将爲您自動判斷正反面。
        :type CardSide: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.CardSide = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.CardSide = params.get("CardSide")


class HmtResidentPermitOCRResponse(AbstractModel):
    """HmtResidentPermitOCR返回參數結構體

    """

    def __init__(self):
        """
        :param Name: 證件姓名
        :type Name: str
        :param Sex: 性别
        :type Sex: str
        :param Birth: 出生日期
        :type Birth: str
        :param Address: 網址
        :type Address: str
        :param IdCardNo: 身份證號
        :type IdCardNo: str
        :param CardType: 0-正面
1-反面
        :type CardType: int
        :param ValidDate: 證件有效期限
        :type ValidDate: str
        :param Authority: 簽發機關
        :type Authority: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.Sex = None
        self.Birth = None
        self.Address = None
        self.IdCardNo = None
        self.CardType = None
        self.ValidDate = None
        self.Authority = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Sex = params.get("Sex")
        self.Birth = params.get("Birth")
        self.Address = params.get("Address")
        self.IdCardNo = params.get("IdCardNo")
        self.CardType = params.get("CardType")
        self.ValidDate = params.get("ValidDate")
        self.Authority = params.get("Authority")
        self.RequestId = params.get("RequestId")


class IDCardOCRRequest(AbstractModel):
    """IDCardOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。要求圖片經Base64編碼後不超過 7M，分辨率建議500*800以上，支援PNG、JPG、JPEG、BMP格式。建議卡片部分占據圖片2/3以上。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。要求圖片經Base64編碼後不超過 7M，分辨率建議500*800以上，支援PNG、JPG、JPEG、BMP格式。建議卡片部分占據圖片2/3以上。
建議圖片儲存於Top Cloud ，可保障更高的下載速度和穩定性。
        :type ImageUrl: str
        :param CardSide: FRONT：身份證有照片的一面（人像面），
BACK：身份證有國徽的一面（國徽面），
該參數如果不填，将爲您自動判斷身份證正反面。
        :type CardSide: str
        :param Config: 以下可選欄位均爲bool 類型，預設false：
CropIdCard，身份證照片裁剪（去掉證件外多餘的邊緣、自動矯正拍攝角度）
CropPortrait，人像照片裁剪（自動摳取身份證頭像區域）
CopyWarn，影印件告警
BorderCheckWarn，邊框和框内遮擋告警
ReshootWarn，翻拍告警
DetectPsWarn，PS檢測告警
TempIdWarn，臨時身份證告警
InvalidDateWarn，身份證有效日期不合法告警
Quality，圖片質量分數（評價圖片的模糊程度）

SDK 設置方式參考：
Config = Json.stringify({"CropIdCard":true,"CropPortrait":true})
API 3.0 Explorer 設置方式參考：
Config = {"CropIdCard":true,"CropPortrait":true}
        :type Config: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.CardSide = None
        self.Config = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.CardSide = params.get("CardSide")
        self.Config = params.get("Config")


class IDCardOCRResponse(AbstractModel):
    """IDCardOCR返回參數結構體

    """

    def __init__(self):
        """
        :param Name: 姓名（人像面）
        :type Name: str
        :param Sex: 性别（人像面）
        :type Sex: str
        :param Nation: 民族（人像面）
        :type Nation: str
        :param Birth: 出生日期（人像面）
        :type Birth: str
        :param Address: 網址（人像面）
        :type Address: str
        :param IdNum: 身份證號（人像面）
        :type IdNum: str
        :param Authority: 發證機關（國徽面）
        :type Authority: str
        :param ValidDate: 證件有效期（國徽面）
        :type ValidDate: str
        :param AdvancedInfo: 擴展訊息，不請求則不返回，具體輸入參考範例3和範例4。
IdCard，裁剪後身份證照片的base64編碼，請求 CropIdCard 時返回；
Portrait，身份證頭像照片的base64編碼，請求 CropPortrait 時返回；
QualityValue，圖片質量分，請求 Quality 時返回（取值範圍：0~100，分數越低越模糊，建議阈值≥50）;
WarnInfos，告警訊息，Code 告警碼清單和釋義：
-9100	身份證有效日期不合法告警，
-9101	身份證邊框不完整告警，
-9102	身份證影印件告警，
-9103	身份證翻拍告警，
-9105	身份證框内遮擋告警，
-9104	臨時身份證告警，
-9106	身份證 PS 告警。
        :type AdvancedInfo: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.Sex = None
        self.Nation = None
        self.Birth = None
        self.Address = None
        self.IdNum = None
        self.Authority = None
        self.ValidDate = None
        self.AdvancedInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Sex = params.get("Sex")
        self.Nation = params.get("Nation")
        self.Birth = params.get("Birth")
        self.Address = params.get("Address")
        self.IdNum = params.get("IdNum")
        self.Authority = params.get("Authority")
        self.ValidDate = params.get("ValidDate")
        self.AdvancedInfo = params.get("AdvancedInfo")
        self.RequestId = params.get("RequestId")


class InstitutionOCRRequest(AbstractModel):
    """InstitutionOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class InstitutionOCRResponse(AbstractModel):
    """InstitutionOCR返回參數結構體

    """

    def __init__(self):
        """
        :param RegId: 注冊號
        :type RegId: str
        :param ValidDate: 有效期
        :type ValidDate: str
        :param Location: 住所
        :type Location: str
        :param Name: 名稱
        :type Name: str
        :param LegalPerson: 法定代表人
        :type LegalPerson: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RegId = None
        self.ValidDate = None
        self.Location = None
        self.Name = None
        self.LegalPerson = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegId = params.get("RegId")
        self.ValidDate = params.get("ValidDate")
        self.Location = params.get("Location")
        self.Name = params.get("Name")
        self.LegalPerson = params.get("LegalPerson")
        self.RequestId = params.get("RequestId")


class InsuranceBillInfo(AbstractModel):
    """保險單據訊息

    """

    def __init__(self):
        """
        :param Name: 識别出的欄位名稱（關鍵字）。
        :type Name: str
        :param Value: 識别出的欄位名稱對應的值，也就是欄位Name對應的字串結果。
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class InsuranceBillOCRRequest(AbstractModel):
    """InsuranceBillOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class InsuranceBillOCRResponse(AbstractModel):
    """InsuranceBillOCR返回參數結構體

    """

    def __init__(self):
        """
        :param InsuranceBillInfos: 保險單據識别結果，具體内容請點擊左側連結。
        :type InsuranceBillInfos: list of InsuranceBillInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InsuranceBillInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InsuranceBillInfos") is not None:
            self.InsuranceBillInfos = []
            for item in params.get("InsuranceBillInfos"):
                obj = InsuranceBillInfo()
                obj._deserialize(item)
                self.InsuranceBillInfos.append(obj)
        self.RequestId = params.get("RequestId")


class InvoiceDetectInfo(AbstractModel):
    """票據檢測結果

    """

    def __init__(self):
        """
        :param Angle: 識别出的圖片在混貼票據圖片中的旋轉角度。
        :type Angle: float
        :param Type: 識别出的圖片所屬的票據類型。
-1：未知類型
0：出租車發票
1：定額發票
2：火車票
3：增值稅發票
4：客運限額發票
5：機票行程單
6：酒店帳單
7：完稅證明
8：通用機打發票
9：汽車票
10：輪船票
11：增值稅發票（卷票 ）
12：購車發票
13：過路過橋費發票
14：購物小票
        :type Type: int
        :param Rect: 識别出的圖片在混貼票據圖片中的位置訊息。與Angel結合可以得出原圖位置，組成RotatedRect((X,Y), (Width, Height), Angle)，詳情可參考OpenCV文件。
        :type Rect: :class:`taifucloudcloud.ocr.v20181119.models.Rect`
        :param Image: 入參 ReturnImage 爲 True 時返回 Base64 編碼後的圖片。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Image: str
        """
        self.Angle = None
        self.Type = None
        self.Rect = None
        self.Image = None


    def _deserialize(self, params):
        self.Angle = params.get("Angle")
        self.Type = params.get("Type")
        if params.get("Rect") is not None:
            self.Rect = Rect()
            self.Rect._deserialize(params.get("Rect"))
        self.Image = params.get("Image")


class InvoiceGeneralInfo(AbstractModel):
    """通用機打發票訊息

    """

    def __init__(self):
        """
        :param Name: 識别出的欄位名稱（關鍵字）。
        :type Name: str
        :param Value: 識别出的欄位名稱對應的值，也就是欄位Name對應的字串結果。
        :type Value: str
        :param Rect: 文本行在旋轉糾正之後的圖像中的像素坐標。
        :type Rect: :class:`taifucloudcloud.ocr.v20181119.models.Rect`
        """
        self.Name = None
        self.Value = None
        self.Rect = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        if params.get("Rect") is not None:
            self.Rect = Rect()
            self.Rect._deserialize(params.get("Rect"))


class InvoiceGeneralOCRRequest(AbstractModel):
    """InvoiceGeneralOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class InvoiceGeneralOCRResponse(AbstractModel):
    """InvoiceGeneralOCR返回參數結構體

    """

    def __init__(self):
        """
        :param InvoiceGeneralInfos: 通用機打發票識别結果，具體内容請點擊左側連結。
        :type InvoiceGeneralInfos: list of InvoiceGeneralInfo
        :param Angle: 圖片旋轉角度（角度制），文本的水平方向爲0°，順時針爲正，逆時針爲負。
        :type Angle: float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InvoiceGeneralInfos = None
        self.Angle = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InvoiceGeneralInfos") is not None:
            self.InvoiceGeneralInfos = []
            for item in params.get("InvoiceGeneralInfos"):
                obj = InvoiceGeneralInfo()
                obj._deserialize(item)
                self.InvoiceGeneralInfos.append(obj)
        self.Angle = params.get("Angle")
        self.RequestId = params.get("RequestId")


class ItemCoord(AbstractModel):
    """文本行在旋轉糾正之後的圖像中的像素坐標，表示爲（左上角x, 左上角y，寬width，高height）

    """

    def __init__(self):
        """
        :param X: 左上角x
        :type X: int
        :param Y: 左上角y
        :type Y: int
        :param Width: 寬width
        :type Width: int
        :param Height: 高height
        :type Height: int
        """
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class LicensePlateOCRRequest(AbstractModel):
    """LicensePlateOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class LicensePlateOCRResponse(AbstractModel):
    """LicensePlateOCR返回參數結構體

    """

    def __init__(self):
        """
        :param Number: 識别出的車牌號碼。
        :type Number: str
        :param Confidence: 置信度，0 - 100 之間。
        :type Confidence: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Number = None
        self.Confidence = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Number = params.get("Number")
        self.Confidence = params.get("Confidence")
        self.RequestId = params.get("RequestId")


class MLIDCardOCRRequest(AbstractModel):
    """MLIDCardOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。(  地區之外不支援這個欄位 )
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        :param RetImage: 是否返回圖片
        :type RetImage: bool
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.RetImage = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.RetImage = params.get("RetImage")


class MLIDCardOCRResponse(AbstractModel):
    """MLIDCardOCR返回參數結構體

    """

    def __init__(self):
        """
        :param ID: 身份證號
        :type ID: str
        :param Name: 姓名
        :type Name: str
        :param Address: 網址
        :type Address: str
        :param Sex: 性别
        :type Sex: str
        :param Warn: 告警碼
-9103	證照翻拍告警
-9102	證照影印件告警
        :type Warn: list of int
        :param Image: 證件圖片
        :type Image: str
        :param AdvancedInfo: 擴展欄位:
{
    ID:{
        Confidence:0.9999
    },
    Name:{
        Confidence:0.9996
    }
}
        :type AdvancedInfo: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ID = None
        self.Name = None
        self.Address = None
        self.Sex = None
        self.Warn = None
        self.Image = None
        self.AdvancedInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.Name = params.get("Name")
        self.Address = params.get("Address")
        self.Sex = params.get("Sex")
        self.Warn = params.get("Warn")
        self.Image = params.get("Image")
        self.AdvancedInfo = params.get("AdvancedInfo")
        self.RequestId = params.get("RequestId")


class MLIDPassportOCRRequest(AbstractModel):
    """MLIDPassportOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。要求圖片經Base64編碼後不超過 7M，分辨率建議500*800以上，支援PNG、JPG、JPEG、BMP格式。建議卡片部分占據圖片2/3以上。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param RetImage: 是否返回圖片
        :type RetImage: bool
        """
        self.ImageBase64 = None
        self.RetImage = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.RetImage = params.get("RetImage")


class MLIDPassportOCRResponse(AbstractModel):
    """MLIDPassportOCR返回參數結構體

    """

    def __init__(self):
        """
        :param ID: 護照ID
        :type ID: str
        :param Name: 姓名
        :type Name: str
        :param DateOfBirth: 出生日期
        :type DateOfBirth: str
        :param Sex: 性别（F女，M男）
        :type Sex: str
        :param DateOfExpiration: 有效期
        :type DateOfExpiration: str
        :param IssuingCountry: 發行國
        :type IssuingCountry: str
        :param Nationality: 國籍
        :type Nationality: str
        :param Warn: 告警碼
-9103	證照翻拍告警
-9102	證照影印件告警
-9106       證件遮擋告警
        :type Warn: list of int
        :param Image: 證件圖片
        :type Image: str
        :param AdvancedInfo: 擴展欄位:
{
    ID:{
        Confidence:0.9999
    },
    Name:{
        Confidence:0.9996
    }
}
        :type AdvancedInfo: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ID = None
        self.Name = None
        self.DateOfBirth = None
        self.Sex = None
        self.DateOfExpiration = None
        self.IssuingCountry = None
        self.Nationality = None
        self.Warn = None
        self.Image = None
        self.AdvancedInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.Name = params.get("Name")
        self.DateOfBirth = params.get("DateOfBirth")
        self.Sex = params.get("Sex")
        self.DateOfExpiration = params.get("DateOfExpiration")
        self.IssuingCountry = params.get("IssuingCountry")
        self.Nationality = params.get("Nationality")
        self.Warn = params.get("Warn")
        self.Image = params.get("Image")
        self.AdvancedInfo = params.get("AdvancedInfo")
        self.RequestId = params.get("RequestId")


class MainlandPermitOCRRequest(AbstractModel):
    """MainlandPermitOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        :param RetProfile: 是非返回頭像。預設不返回。
        :type RetProfile: bool
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.RetProfile = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.RetProfile = params.get("RetProfile")


class MainlandPermitOCRResponse(AbstractModel):
    """MainlandPermitOCR返回參數結構體

    """

    def __init__(self):
        """
        :param Name: 中文姓名
        :type Name: str
        :param EnglishName: 英文姓名
        :type EnglishName: str
        :param Sex: 性别
        :type Sex: str
        :param Birthday: 出生日期
        :type Birthday: str
        :param IssueAuthority: 簽發機關
        :type IssueAuthority: str
        :param ValidDate: 有效期限
        :type ValidDate: str
        :param Number: 證件號
        :type Number: str
        :param IssueAddress: 簽發地點
        :type IssueAddress: str
        :param IssueNumber: 簽發次數
        :type IssueNumber: str
        :param Type: 證件類别， 如：台灣居民來往大陸通行證、 居民來往内地通行證。
        :type Type: str
        :param Profile: RetProfile爲True時返回頭像欄位， Base64編碼
        :type Profile: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.EnglishName = None
        self.Sex = None
        self.Birthday = None
        self.IssueAuthority = None
        self.ValidDate = None
        self.Number = None
        self.IssueAddress = None
        self.IssueNumber = None
        self.Type = None
        self.Profile = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.EnglishName = params.get("EnglishName")
        self.Sex = params.get("Sex")
        self.Birthday = params.get("Birthday")
        self.IssueAuthority = params.get("IssueAuthority")
        self.ValidDate = params.get("ValidDate")
        self.Number = params.get("Number")
        self.IssueAddress = params.get("IssueAddress")
        self.IssueNumber = params.get("IssueNumber")
        self.Type = params.get("Type")
        self.Profile = params.get("Profile")
        self.RequestId = params.get("RequestId")


class MixedInvoiceDetectRequest(AbstractModel):
    """MixedInvoiceDetect請求參數結構體

    """

    def __init__(self):
        """
        :param ReturnImage: 是否需要返回裁剪後的圖片。
        :type ReturnImage: bool
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ReturnImage = None
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ReturnImage = params.get("ReturnImage")
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class MixedInvoiceDetectResponse(AbstractModel):
    """MixedInvoiceDetect返回參數結構體

    """

    def __init__(self):
        """
        :param InvoiceDetectInfos: 檢測出的票據類型清單，具體内容請點擊左側連結。
        :type InvoiceDetectInfos: list of InvoiceDetectInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InvoiceDetectInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InvoiceDetectInfos") is not None:
            self.InvoiceDetectInfos = []
            for item in params.get("InvoiceDetectInfos"):
                obj = InvoiceDetectInfo()
                obj._deserialize(item)
                self.InvoiceDetectInfos.append(obj)
        self.RequestId = params.get("RequestId")


class MixedInvoiceItem(AbstractModel):
    """混貼票據單張發票識别訊息

    """

    def __init__(self):
        """
        :param Code: 識别結果。
OK：表示識别成功；FailedOperation.UnsupportedInvioce：表示不支援識别；
FailedOperation.UnKnowError：表示識别失敗；
其它錯誤碼見各個票據介面的定義。
        :type Code: str
        :param Type: 識别出的圖片所屬的票據類型。
-1：未知類型
0：出租車發票
1：定額發票
2：火車票
3：增值稅發票
5：機票行程單
8：通用機打發票
9：汽車票
10：輪船票
11：增值稅發票（卷票 ）
12：購車發票
13：過路過橋費發票
        :type Type: int
        :param Rect: 識别出的圖片在混貼票據圖片中的位置訊息。與Angel結合可以得出原圖位置，組成RotatedRect((X,Y), (Width, Height), Angle)，詳情可參考OpenCV文件。
        :type Rect: :class:`taifucloudcloud.ocr.v20181119.models.Rect`
        :param Angle: 識别出的圖片在混貼票據圖片中的旋轉角度。
        :type Angle: float
        :param SingleInvoiceInfos: 識别到的内容。
        :type SingleInvoiceInfos: list of SingleInvoiceInfo
        """
        self.Code = None
        self.Type = None
        self.Rect = None
        self.Angle = None
        self.SingleInvoiceInfos = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Type = params.get("Type")
        if params.get("Rect") is not None:
            self.Rect = Rect()
            self.Rect._deserialize(params.get("Rect"))
        self.Angle = params.get("Angle")
        if params.get("SingleInvoiceInfos") is not None:
            self.SingleInvoiceInfos = []
            for item in params.get("SingleInvoiceInfos"):
                obj = SingleInvoiceInfo()
                obj._deserialize(item)
                self.SingleInvoiceInfos.append(obj)


class MixedInvoiceOCRRequest(AbstractModel):
    """MixedInvoiceOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        :param Types: 需要識别的票據類型清單，爲空或不填表示識别全部類型。
0：出租車發票
1：定額發票
2：火車票
3：增值稅發票
5：機票行程單
8：通用機打發票
9：汽車票
10：輪船票
11：增值稅發票（卷票 ）
12：購車發票
13：過路過橋費發票
        :type Types: list of int
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.Types = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.Types = params.get("Types")


class MixedInvoiceOCRResponse(AbstractModel):
    """MixedInvoiceOCR返回參數結構體

    """

    def __init__(self):
        """
        :param MixedInvoiceItems: 混貼票據識别結果，具體内容請點擊左側連結。
        :type MixedInvoiceItems: list of MixedInvoiceItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.MixedInvoiceItems = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MixedInvoiceItems") is not None:
            self.MixedInvoiceItems = []
            for item in params.get("MixedInvoiceItems"):
                obj = MixedInvoiceItem()
                obj._deserialize(item)
                self.MixedInvoiceItems.append(obj)
        self.RequestId = params.get("RequestId")


class OrgCodeCertOCRRequest(AbstractModel):
    """OrgCodeCertOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class OrgCodeCertOCRResponse(AbstractModel):
    """OrgCodeCertOCR返回參數結構體

    """

    def __init__(self):
        """
        :param OrgCode: 代碼
        :type OrgCode: str
        :param Name: 機構名稱
        :type Name: str
        :param Address: 網址
        :type Address: str
        :param ValidDate: 有效期
        :type ValidDate: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.OrgCode = None
        self.Name = None
        self.Address = None
        self.ValidDate = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OrgCode = params.get("OrgCode")
        self.Name = params.get("Name")
        self.Address = params.get("Address")
        self.ValidDate = params.get("ValidDate")
        self.RequestId = params.get("RequestId")


class PassportOCRRequest(AbstractModel):
    """PassportOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。要求圖片經Base64編碼後不超過 7M，分辨率建議500*800以上，支援PNG、JPG、JPEG、BMP格式。建議卡片部分占據圖片2/3以上。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。要求圖片經Base64編碼後不超過 7M，分辨率建議500*800以上，支援PNG、JPG、JPEG、BMP格式。建議卡片部分占據圖片2/3以上。
建議圖片儲存於Top Cloud ，可保障更高的下載速度和穩定性。
        :type ImageUrl: str
        :param Type: 預設填寫CN
支援 大陸地區護照。
        :type Type: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.Type = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.Type = params.get("Type")


class PassportOCRResponse(AbstractModel):
    """PassportOCR返回參數結構體

    """

    def __init__(self):
        """
        :param Country: 國家碼
        :type Country: str
        :param PassportNo: 護照號
        :type PassportNo: str
        :param Sex: 性别
        :type Sex: str
        :param Nationality: 國籍
        :type Nationality: str
        :param BirthDate: 出生日期
        :type BirthDate: str
        :param BirthPlace: 出生地點
        :type BirthPlace: str
        :param IssueDate: 簽發日期
        :type IssueDate: str
        :param IssuePlace: 簽發地點
        :type IssuePlace: str
        :param ExpiryDate: 有效期
        :type ExpiryDate: str
        :param Signature: 持證人簽名
        :type Signature: str
        :param CodeSet: 最下方第一行 MRZ Code 序列
        :type CodeSet: str
        :param CodeCrc: 最下方第二行 MRZ Code 序列
        :type CodeCrc: str
        :param Name: 姓名
        :type Name: str
        :param FamilyName: 姓
        :type FamilyName: str
        :param FirstName: 名
        :type FirstName: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Country = None
        self.PassportNo = None
        self.Sex = None
        self.Nationality = None
        self.BirthDate = None
        self.BirthPlace = None
        self.IssueDate = None
        self.IssuePlace = None
        self.ExpiryDate = None
        self.Signature = None
        self.CodeSet = None
        self.CodeCrc = None
        self.Name = None
        self.FamilyName = None
        self.FirstName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Country = params.get("Country")
        self.PassportNo = params.get("PassportNo")
        self.Sex = params.get("Sex")
        self.Nationality = params.get("Nationality")
        self.BirthDate = params.get("BirthDate")
        self.BirthPlace = params.get("BirthPlace")
        self.IssueDate = params.get("IssueDate")
        self.IssuePlace = params.get("IssuePlace")
        self.ExpiryDate = params.get("ExpiryDate")
        self.Signature = params.get("Signature")
        self.CodeSet = params.get("CodeSet")
        self.CodeCrc = params.get("CodeCrc")
        self.Name = params.get("Name")
        self.FamilyName = params.get("FamilyName")
        self.FirstName = params.get("FirstName")
        self.RequestId = params.get("RequestId")


class PermitOCRRequest(AbstractModel):
    """PermitOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class PermitOCRResponse(AbstractModel):
    """PermitOCR返回參數結構體

    """

    def __init__(self):
        """
        :param Name: 姓名
        :type Name: str
        :param EnglishName: 英文姓名
        :type EnglishName: str
        :param Number: 證件號
        :type Number: str
        :param Sex: 性别
        :type Sex: str
        :param ValidDate: 有效期限
        :type ValidDate: str
        :param IssueAuthority: 簽發機關
        :type IssueAuthority: str
        :param IssueAddress: 簽發地點
        :type IssueAddress: str
        :param Birthday: 出生日期
        :type Birthday: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.EnglishName = None
        self.Number = None
        self.Sex = None
        self.ValidDate = None
        self.IssueAuthority = None
        self.IssueAddress = None
        self.Birthday = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.EnglishName = params.get("EnglishName")
        self.Number = params.get("Number")
        self.Sex = params.get("Sex")
        self.ValidDate = params.get("ValidDate")
        self.IssueAuthority = params.get("IssueAuthority")
        self.IssueAddress = params.get("IssueAddress")
        self.Birthday = params.get("Birthday")
        self.RequestId = params.get("RequestId")


class PropOwnerCertOCRRequest(AbstractModel):
    """PropOwnerCertOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class PropOwnerCertOCRResponse(AbstractModel):
    """PropOwnerCertOCR返回參數結構體

    """

    def __init__(self):
        """
        :param Owner: 房地産權利人
        :type Owner: str
        :param Possession: 共有情況
        :type Possession: str
        :param RegisterTime: 登記時間
        :type RegisterTime: str
        :param Purpose: 規劃用途
        :type Purpose: str
        :param Nature: 房屋性質
        :type Nature: str
        :param Location: 房地坐落
        :type Location: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Owner = None
        self.Possession = None
        self.RegisterTime = None
        self.Purpose = None
        self.Nature = None
        self.Location = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Owner = params.get("Owner")
        self.Possession = params.get("Possession")
        self.RegisterTime = params.get("RegisterTime")
        self.Purpose = params.get("Purpose")
        self.Nature = params.get("Nature")
        self.Location = params.get("Location")
        self.RequestId = params.get("RequestId")


class QrcodeImgSize(AbstractModel):
    """圖片大小

    """

    def __init__(self):
        """
        :param Wide: 寬
        :type Wide: int
        :param High: 高
        :type High: int
        """
        self.Wide = None
        self.High = None


    def _deserialize(self, params):
        self.Wide = params.get("Wide")
        self.High = params.get("High")


class QrcodeOCRRequest(AbstractModel):
    """QrcodeOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class QrcodeOCRResponse(AbstractModel):
    """QrcodeOCR返回參數結構體

    """

    def __init__(self):
        """
        :param CodeResults: 二維碼/條形碼識别結果訊息，具體内容請點擊左側連結。
        :type CodeResults: list of QrcodeResultsInfo
        :param ImgSize: 圖片大小，具體内容請點擊左側連結。
        :type ImgSize: :class:`taifucloudcloud.ocr.v20181119.models.QrcodeImgSize`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CodeResults = None
        self.ImgSize = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CodeResults") is not None:
            self.CodeResults = []
            for item in params.get("CodeResults"):
                obj = QrcodeResultsInfo()
                obj._deserialize(item)
                self.CodeResults.append(obj)
        if params.get("ImgSize") is not None:
            self.ImgSize = QrcodeImgSize()
            self.ImgSize._deserialize(params.get("ImgSize"))
        self.RequestId = params.get("RequestId")


class QrcodePositionObj(AbstractModel):
    """二維碼/條形碼坐標訊息

    """

    def __init__(self):
        """
        :param LeftTop: 左上頂點坐標（如果是條形碼，X和Y都爲-1）
        :type LeftTop: :class:`taifucloudcloud.ocr.v20181119.models.Coord`
        :param RightTop: 右上頂點坐標（如果是條形碼，X和Y都爲-1）
        :type RightTop: :class:`taifucloudcloud.ocr.v20181119.models.Coord`
        :param RightBottom: 右下頂點坐標（如果是條形碼，X和Y都爲-1）
        :type RightBottom: :class:`taifucloudcloud.ocr.v20181119.models.Coord`
        :param LeftBottom: 左下頂點坐標（如果是條形碼，X和Y都爲-1）
        :type LeftBottom: :class:`taifucloudcloud.ocr.v20181119.models.Coord`
        """
        self.LeftTop = None
        self.RightTop = None
        self.RightBottom = None
        self.LeftBottom = None


    def _deserialize(self, params):
        if params.get("LeftTop") is not None:
            self.LeftTop = Coord()
            self.LeftTop._deserialize(params.get("LeftTop"))
        if params.get("RightTop") is not None:
            self.RightTop = Coord()
            self.RightTop._deserialize(params.get("RightTop"))
        if params.get("RightBottom") is not None:
            self.RightBottom = Coord()
            self.RightBottom._deserialize(params.get("RightBottom"))
        if params.get("LeftBottom") is not None:
            self.LeftBottom = Coord()
            self.LeftBottom._deserialize(params.get("LeftBottom"))


class QrcodeResultsInfo(AbstractModel):
    """二維碼/條形碼識别結果訊息

    """

    def __init__(self):
        """
        :param TypeName: 類型（二維碼、條形碼）
        :type TypeName: str
        :param Url: 二維碼/條形碼包含的網址
        :type Url: str
        :param Position: 二維碼/條形碼坐標（二維碼會返回位置坐標，條形碼暫不返回位置坐標，因此預設X和Y返回值均爲-1）
        :type Position: :class:`taifucloudcloud.ocr.v20181119.models.QrcodePositionObj`
        """
        self.TypeName = None
        self.Url = None
        self.Position = None


    def _deserialize(self, params):
        self.TypeName = params.get("TypeName")
        self.Url = params.get("Url")
        if params.get("Position") is not None:
            self.Position = QrcodePositionObj()
            self.Position._deserialize(params.get("Position"))


class QuestionBlockObj(AbstractModel):
    """數學試題識别結構化對象

    """

    def __init__(self):
        """
        :param QuestionArr: 數學試題識别結構化訊息數組
        :type QuestionArr: list of QuestionObj
        """
        self.QuestionArr = None


    def _deserialize(self, params):
        if params.get("QuestionArr") is not None:
            self.QuestionArr = []
            for item in params.get("QuestionArr"):
                obj = QuestionObj()
                obj._deserialize(item)
                self.QuestionArr.append(obj)


class QuestionObj(AbstractModel):
    """試題識别結構化訊息

    """

    def __init__(self):
        """
        :param QuestionTextNo: 題號
        :type QuestionTextNo: str
        :param QuestionTextType: 題型：
1: "選擇題"
2: "填空題"
3: "解答題"
        :type QuestionTextType: int
        :param QuestionText: 題幹
        :type QuestionText: str
        :param QuestionOptions: 選擇題選項，包含1個或多個option
        :type QuestionOptions: str
        :param QuestionSubquestion: 所有子題的question屬性
        :type QuestionSubquestion: str
        """
        self.QuestionTextNo = None
        self.QuestionTextType = None
        self.QuestionText = None
        self.QuestionOptions = None
        self.QuestionSubquestion = None


    def _deserialize(self, params):
        self.QuestionTextNo = params.get("QuestionTextNo")
        self.QuestionTextType = params.get("QuestionTextType")
        self.QuestionText = params.get("QuestionText")
        self.QuestionOptions = params.get("QuestionOptions")
        self.QuestionSubquestion = params.get("QuestionSubquestion")


class QuotaInvoiceOCRRequest(AbstractModel):
    """QuotaInvoiceOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class QuotaInvoiceOCRResponse(AbstractModel):
    """QuotaInvoiceOCR返回參數結構體

    """

    def __init__(self):
        """
        :param InvoiceNum: 發票號碼
        :type InvoiceNum: str
        :param InvoiceCode: 發票代碼
        :type InvoiceCode: str
        :param Rate: 大寫金額
        :type Rate: str
        :param RateNum: 小寫金額
        :type RateNum: str
        :param InvoiceType: 發票消費類型
        :type InvoiceType: str
        :param Province: 省
注意：此欄位可能返回 null，表示取不到有效值。
        :type Province: str
        :param City: 市
注意：此欄位可能返回 null，表示取不到有效值。
        :type City: str
        :param HasStamp: 是否有公司印章（1有 0無 空爲識别不出）
注意：此欄位可能返回 null，表示取不到有效值。
        :type HasStamp: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InvoiceNum = None
        self.InvoiceCode = None
        self.Rate = None
        self.RateNum = None
        self.InvoiceType = None
        self.Province = None
        self.City = None
        self.HasStamp = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InvoiceNum = params.get("InvoiceNum")
        self.InvoiceCode = params.get("InvoiceCode")
        self.Rate = params.get("Rate")
        self.RateNum = params.get("RateNum")
        self.InvoiceType = params.get("InvoiceType")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.HasStamp = params.get("HasStamp")
        self.RequestId = params.get("RequestId")


class Rect(AbstractModel):
    """矩形坐標

    """

    def __init__(self):
        """
        :param X: 左上角x
        :type X: int
        :param Y: 左上角y
        :type Y: int
        :param Width: 寬度
        :type Width: int
        :param Height: 高度
        :type Height: int
        """
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class ResidenceBookletOCRRequest(AbstractModel):
    """ResidenceBookletOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class ResidenceBookletOCRResponse(AbstractModel):
    """ResidenceBookletOCR返回參數結構體

    """

    def __init__(self):
        """
        :param HouseholdNumber: 戶號
        :type HouseholdNumber: str
        :param Name: 姓名
        :type Name: str
        :param Sex: 性别
        :type Sex: str
        :param BirthPlace: 出生地
        :type BirthPlace: str
        :param Nation: 民族
        :type Nation: str
        :param NativePlace: 籍貫
        :type NativePlace: str
        :param BirthDate: 出生日期
        :type BirthDate: str
        :param IdCardNumber: 公民身份證件編號
        :type IdCardNumber: str
        :param EducationDegree: 文化程度
        :type EducationDegree: str
        :param ServicePlace: 服務處所
        :type ServicePlace: str
        :param Household: 戶别
        :type Household: str
        :param Address: 住址
        :type Address: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.HouseholdNumber = None
        self.Name = None
        self.Sex = None
        self.BirthPlace = None
        self.Nation = None
        self.NativePlace = None
        self.BirthDate = None
        self.IdCardNumber = None
        self.EducationDegree = None
        self.ServicePlace = None
        self.Household = None
        self.Address = None
        self.RequestId = None


    def _deserialize(self, params):
        self.HouseholdNumber = params.get("HouseholdNumber")
        self.Name = params.get("Name")
        self.Sex = params.get("Sex")
        self.BirthPlace = params.get("BirthPlace")
        self.Nation = params.get("Nation")
        self.NativePlace = params.get("NativePlace")
        self.BirthDate = params.get("BirthDate")
        self.IdCardNumber = params.get("IdCardNumber")
        self.EducationDegree = params.get("EducationDegree")
        self.ServicePlace = params.get("ServicePlace")
        self.Household = params.get("Household")
        self.Address = params.get("Address")
        self.RequestId = params.get("RequestId")


class ShipInvoiceInfo(AbstractModel):
    """輪船票欄位訊息

    """

    def __init__(self):
        """
        :param Name: 識别出的欄位名稱（關鍵字）。
        :type Name: str
        :param Value: 識别出的欄位名稱對應的值，也就是欄位Name對應的字串結果。
        :type Value: str
        :param Rect: 文本行在旋轉糾正之後的圖像中的像素坐標。
        :type Rect: :class:`taifucloudcloud.ocr.v20181119.models.Rect`
        """
        self.Name = None
        self.Value = None
        self.Rect = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        if params.get("Rect") is not None:
            self.Rect = Rect()
            self.Rect._deserialize(params.get("Rect"))


class ShipInvoiceOCRRequest(AbstractModel):
    """ShipInvoiceOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class ShipInvoiceOCRResponse(AbstractModel):
    """ShipInvoiceOCR返回參數結構體

    """

    def __init__(self):
        """
        :param ShipInvoiceInfos: 輪船票識别結果，具體内容請點擊左側連結。
        :type ShipInvoiceInfos: list of ShipInvoiceInfo
        :param Angle: 圖片旋轉角度（角度制），文本的水平方向爲0°，順時針爲正，逆時針爲負。
        :type Angle: float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ShipInvoiceInfos = None
        self.Angle = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ShipInvoiceInfos") is not None:
            self.ShipInvoiceInfos = []
            for item in params.get("ShipInvoiceInfos"):
                obj = ShipInvoiceInfo()
                obj._deserialize(item)
                self.ShipInvoiceInfos.append(obj)
        self.Angle = params.get("Angle")
        self.RequestId = params.get("RequestId")


class SingleInvoiceInfo(AbstractModel):
    """混貼票據中單張發票的内容

    """

    def __init__(self):
        """
        :param Name: 識别出的欄位名稱
        :type Name: str
        :param Value: 識别出的欄位名稱對應的值，也就是欄位name對應的字串結果。
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class TableOCRRequest(AbstractModel):
    """TableOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class TableOCRResponse(AbstractModel):
    """TableOCR返回參數結構體

    """

    def __init__(self):
        """
        :param TextDetections: 檢測到的文本訊息，具體内容請點擊左側連結。
        :type TextDetections: list of TextTable
        :param Data: Base64 編碼後的 Excel 數據。
        :type Data: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextTable()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class TaxiInvoiceOCRRequest(AbstractModel):
    """TaxiInvoiceOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class TaxiInvoiceOCRResponse(AbstractModel):
    """TaxiInvoiceOCR返回參數結構體

    """

    def __init__(self):
        """
        :param InvoiceNum: 發票代碼
        :type InvoiceNum: str
        :param InvoiceCode: 發票號碼
        :type InvoiceCode: str
        :param Date: 日期
        :type Date: str
        :param Fare: 金額
        :type Fare: str
        :param GetOnTime: 上車時間
        :type GetOnTime: str
        :param GetOffTime: 下車時間
        :type GetOffTime: str
        :param Distance: 裏程
        :type Distance: str
        :param Location: 發票所在地
        :type Location: str
        :param PlateNumber: 車牌號
        :type PlateNumber: str
        :param InvoiceType: 發票消費類型
        :type InvoiceType: str
        :param Province: 省
注意：此欄位可能返回 null，表示取不到有效值。
        :type Province: str
        :param City: 市
注意：此欄位可能返回 null，表示取不到有效值。
        :type City: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InvoiceNum = None
        self.InvoiceCode = None
        self.Date = None
        self.Fare = None
        self.GetOnTime = None
        self.GetOffTime = None
        self.Distance = None
        self.Location = None
        self.PlateNumber = None
        self.InvoiceType = None
        self.Province = None
        self.City = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InvoiceNum = params.get("InvoiceNum")
        self.InvoiceCode = params.get("InvoiceCode")
        self.Date = params.get("Date")
        self.Fare = params.get("Fare")
        self.GetOnTime = params.get("GetOnTime")
        self.GetOffTime = params.get("GetOffTime")
        self.Distance = params.get("Distance")
        self.Location = params.get("Location")
        self.PlateNumber = params.get("PlateNumber")
        self.InvoiceType = params.get("InvoiceType")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.RequestId = params.get("RequestId")


class TextArithmetic(AbstractModel):
    """算式識别結果

    """

    def __init__(self):
        """
        :param DetectedText: 識别出的文本行内容
        :type DetectedText: str
        :param Result: 算式運算結果
        :type Result: bool
        :param Confidence: 保留欄位，暫不支援
        :type Confidence: int
        :param Polygon: 原圖文本行坐標，以四個頂點坐標表示（保留欄位，暫不支援）
注意：此欄位可能返回 null，表示取不到有效值。
        :type Polygon: list of Coord
        :param AdvancedInfo: 保留欄位，暫不支援
        :type AdvancedInfo: str
        :param ItemCoord: 文本行旋轉糾正之後在圖像中的像素坐標，表示爲（左上角x, 左上角y，寬width，高height）
        :type ItemCoord: :class:`taifucloudcloud.ocr.v20181119.models.ItemCoord`
        :param ExpressionType: 算式題型編號：
‘1’: 加減乘除四則
‘2’: 加減乘除已知結果求運算因子
‘3’: 判斷大小
‘4’: 約等於估算
‘5’: 帶餘數除法
‘6’: 分數四則運算
‘7’: 單位換算
‘8’: 豎式加減法
‘9’: 豎式乘除法
‘10’: 脫式計算
‘11’: 解方程
        :type ExpressionType: str
        """
        self.DetectedText = None
        self.Result = None
        self.Confidence = None
        self.Polygon = None
        self.AdvancedInfo = None
        self.ItemCoord = None
        self.ExpressionType = None


    def _deserialize(self, params):
        self.DetectedText = params.get("DetectedText")
        self.Result = params.get("Result")
        self.Confidence = params.get("Confidence")
        if params.get("Polygon") is not None:
            self.Polygon = []
            for item in params.get("Polygon"):
                obj = Coord()
                obj._deserialize(item)
                self.Polygon.append(obj)
        self.AdvancedInfo = params.get("AdvancedInfo")
        if params.get("ItemCoord") is not None:
            self.ItemCoord = ItemCoord()
            self.ItemCoord._deserialize(params.get("ItemCoord"))
        self.ExpressionType = params.get("ExpressionType")


class TextDetectRequest(AbstractModel):
    """TextDetect請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class TextDetectResponse(AbstractModel):
    """TextDetect返回參數結構體

    """

    def __init__(self):
        """
        :param HasText: 圖片中是否包含文字。
        :type HasText: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.HasText = None
        self.RequestId = None


    def _deserialize(self, params):
        self.HasText = params.get("HasText")
        self.RequestId = params.get("RequestId")


class TextDetection(AbstractModel):
    """文字識别結果

    """

    def __init__(self):
        """
        :param DetectedText: 識别出的文本行内容
        :type DetectedText: str
        :param Confidence: 置信度 0 ~100
        :type Confidence: int
        :param Polygon: 文本行坐標，以四個頂點坐標表示
注意：此欄位可能返回 null，表示取不到有效值。
        :type Polygon: list of Coord
        :param AdvancedInfo: 此欄位爲擴展欄位。
GeneralBasicOcr介面返回段落訊息Parag，包含ParagNo。
        :type AdvancedInfo: str
        :param ItemPolygon: 文本行在旋轉糾正之後的圖像中的像素坐標，表示爲（左上角x, 左上角y，寬width，高height）
        :type ItemPolygon: :class:`taifucloudcloud.ocr.v20181119.models.ItemCoord`
        """
        self.DetectedText = None
        self.Confidence = None
        self.Polygon = None
        self.AdvancedInfo = None
        self.ItemPolygon = None


    def _deserialize(self, params):
        self.DetectedText = params.get("DetectedText")
        self.Confidence = params.get("Confidence")
        if params.get("Polygon") is not None:
            self.Polygon = []
            for item in params.get("Polygon"):
                obj = Coord()
                obj._deserialize(item)
                self.Polygon.append(obj)
        self.AdvancedInfo = params.get("AdvancedInfo")
        if params.get("ItemPolygon") is not None:
            self.ItemPolygon = ItemCoord()
            self.ItemPolygon._deserialize(params.get("ItemPolygon"))


class TextDetectionEn(AbstractModel):
    """英文識别結果

    """

    def __init__(self):
        """
        :param DetectedText: 識别出的文本行内容
        :type DetectedText: str
        :param Confidence: 置信度 0 ~100
        :type Confidence: int
        :param Polygon: 文本行坐標，以四個頂點坐標表示
注意：此欄位可能返回 null，表示取不到有效值。
        :type Polygon: list of Coord
        :param AdvancedInfo: 此欄位爲擴展欄位。目前EnglishOCR介面返回内容爲空。
        :type AdvancedInfo: str
        """
        self.DetectedText = None
        self.Confidence = None
        self.Polygon = None
        self.AdvancedInfo = None


    def _deserialize(self, params):
        self.DetectedText = params.get("DetectedText")
        self.Confidence = params.get("Confidence")
        if params.get("Polygon") is not None:
            self.Polygon = []
            for item in params.get("Polygon"):
                obj = Coord()
                obj._deserialize(item)
                self.Polygon.append(obj)
        self.AdvancedInfo = params.get("AdvancedInfo")


class TextEduPaper(AbstractModel):
    """數學試題識别結果

    """

    def __init__(self):
        """
        :param Item: 識别出的欄位名稱（關鍵字）
        :type Item: str
        :param DetectedText: 識别出的欄位名稱對應的值，也就是欄位Item對應的字串結果
        :type DetectedText: str
        :param Itemcoord: 文本行在旋轉糾正之後的圖像中的像素坐標，表示爲（左上角x, 左上角y，寬width，高height）
        :type Itemcoord: :class:`taifucloudcloud.ocr.v20181119.models.ItemCoord`
        """
        self.Item = None
        self.DetectedText = None
        self.Itemcoord = None


    def _deserialize(self, params):
        self.Item = params.get("Item")
        self.DetectedText = params.get("DetectedText")
        if params.get("Itemcoord") is not None:
            self.Itemcoord = ItemCoord()
            self.Itemcoord._deserialize(params.get("Itemcoord"))


class TextFormula(AbstractModel):
    """數學公式識别結果

    """

    def __init__(self):
        """
        :param DetectedText: 識别出的文本行内容
        :type DetectedText: str
        """
        self.DetectedText = None


    def _deserialize(self, params):
        self.DetectedText = params.get("DetectedText")


class TextGeneralHandwriting(AbstractModel):
    """文字識别結果

    """

    def __init__(self):
        """
        :param DetectedText: 識别出的文本行内容
        :type DetectedText: str
        :param Confidence: 置信度 0 - 100
        :type Confidence: int
        :param Polygon: 文本行坐標，以四個頂點坐標表示
        :type Polygon: list of Coord
        :param AdvancedInfo: 此欄位爲擴展欄位。
能返回文本行的段落訊息，例如：{\"Parag\":{\"ParagNo\":2}}，
其中ParagNo爲段落行，從1開始。
        :type AdvancedInfo: str
        """
        self.DetectedText = None
        self.Confidence = None
        self.Polygon = None
        self.AdvancedInfo = None


    def _deserialize(self, params):
        self.DetectedText = params.get("DetectedText")
        self.Confidence = params.get("Confidence")
        if params.get("Polygon") is not None:
            self.Polygon = []
            for item in params.get("Polygon"):
                obj = Coord()
                obj._deserialize(item)
                self.Polygon.append(obj)
        self.AdvancedInfo = params.get("AdvancedInfo")


class TextTable(AbstractModel):
    """表格識别結果

    """

    def __init__(self):
        """
        :param ColTl: 單元格左上角的列索引
        :type ColTl: int
        :param RowTl: 單元格左上角的行索引
        :type RowTl: int
        :param ColBr: 單元格右下角的列索引
        :type ColBr: int
        :param RowBr: 單元格右下角的行索引
        :type RowBr: int
        :param Text: 單元格文字
        :type Text: str
        :param Type: 單元格類型，包含body（表格主體）、header（表頭）、footer（表尾）三種
        :type Type: str
        :param Confidence: 置信度 0 ~100
        :type Confidence: int
        :param Polygon: 文本行坐標，以四個頂點坐標表示
        :type Polygon: list of Coord
        :param AdvancedInfo: 此欄位爲擴展欄位
        :type AdvancedInfo: str
        """
        self.ColTl = None
        self.RowTl = None
        self.ColBr = None
        self.RowBr = None
        self.Text = None
        self.Type = None
        self.Confidence = None
        self.Polygon = None
        self.AdvancedInfo = None


    def _deserialize(self, params):
        self.ColTl = params.get("ColTl")
        self.RowTl = params.get("RowTl")
        self.ColBr = params.get("ColBr")
        self.RowBr = params.get("RowBr")
        self.Text = params.get("Text")
        self.Type = params.get("Type")
        self.Confidence = params.get("Confidence")
        if params.get("Polygon") is not None:
            self.Polygon = []
            for item in params.get("Polygon"):
                obj = Coord()
                obj._deserialize(item)
                self.Polygon.append(obj)
        self.AdvancedInfo = params.get("AdvancedInfo")


class TextVatInvoice(AbstractModel):
    """增值稅發票識别結果

    """

    def __init__(self):
        """
        :param Name: 識别出的欄位名稱（關鍵字）。
        :type Name: str
        :param Value: 識别出的欄位名稱對應的值，也就是欄位Name對應的字串結果。
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class TextVehicleBack(AbstractModel):
    """行駛證副頁正面的識别結果

    """

    def __init__(self):
        """
        :param PlateNo: 號牌號碼
注意：此欄位可能返回 null，表示取不到有效值。
        :type PlateNo: str
        :param FileNo: 檔案編號
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileNo: str
        :param AllowNum: 核定人數
注意：此欄位可能返回 null，表示取不到有效值。
        :type AllowNum: str
        :param TotalMass: 總質量
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalMass: str
        :param CurbWeight: 整備質量
注意：此欄位可能返回 null，表示取不到有效值。
        :type CurbWeight: str
        :param LoadQuality: 核定載質量
注意：此欄位可能返回 null，表示取不到有效值。
        :type LoadQuality: str
        :param ExternalSize: 外廓尺寸
注意：此欄位可能返回 null，表示取不到有效值。
        :type ExternalSize: str
        :param Marks: 備注
注意：此欄位可能返回 null，表示取不到有效值。
        :type Marks: str
        :param Record: 檢驗記錄
注意：此欄位可能返回 null，表示取不到有效值。
        :type Record: str
        :param TotalQuasiMass: 準牽引總質量
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalQuasiMass: str
        """
        self.PlateNo = None
        self.FileNo = None
        self.AllowNum = None
        self.TotalMass = None
        self.CurbWeight = None
        self.LoadQuality = None
        self.ExternalSize = None
        self.Marks = None
        self.Record = None
        self.TotalQuasiMass = None


    def _deserialize(self, params):
        self.PlateNo = params.get("PlateNo")
        self.FileNo = params.get("FileNo")
        self.AllowNum = params.get("AllowNum")
        self.TotalMass = params.get("TotalMass")
        self.CurbWeight = params.get("CurbWeight")
        self.LoadQuality = params.get("LoadQuality")
        self.ExternalSize = params.get("ExternalSize")
        self.Marks = params.get("Marks")
        self.Record = params.get("Record")
        self.TotalQuasiMass = params.get("TotalQuasiMass")


class TextVehicleFront(AbstractModel):
    """行駛證首頁正面的識别結果

    """

    def __init__(self):
        """
        :param PlateNo: 號牌號碼
注意：此欄位可能返回 null，表示取不到有效值。
        :type PlateNo: str
        :param VehicleType: 車輛類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type VehicleType: str
        :param Owner: 所有人
注意：此欄位可能返回 null，表示取不到有效值。
        :type Owner: str
        :param Address: 住址
注意：此欄位可能返回 null，表示取不到有效值。
        :type Address: str
        :param UseCharacter: 使用性質
注意：此欄位可能返回 null，表示取不到有效值。
        :type UseCharacter: str
        :param Model: 品牌型號
注意：此欄位可能返回 null，表示取不到有效值。
        :type Model: str
        :param Vin: 車輛識别代號
注意：此欄位可能返回 null，表示取不到有效值。
        :type Vin: str
        :param EngineNo: 發動機號碼
注意：此欄位可能返回 null，表示取不到有效值。
        :type EngineNo: str
        :param RegisterDate: 注冊日期
注意：此欄位可能返回 null，表示取不到有效值。
        :type RegisterDate: str
        :param IssueDate: 發證日期
注意：此欄位可能返回 null，表示取不到有效值。
        :type IssueDate: str
        :param Seal: 印章
注意：此欄位可能返回 null，表示取不到有效值。
        :type Seal: str
        """
        self.PlateNo = None
        self.VehicleType = None
        self.Owner = None
        self.Address = None
        self.UseCharacter = None
        self.Model = None
        self.Vin = None
        self.EngineNo = None
        self.RegisterDate = None
        self.IssueDate = None
        self.Seal = None


    def _deserialize(self, params):
        self.PlateNo = params.get("PlateNo")
        self.VehicleType = params.get("VehicleType")
        self.Owner = params.get("Owner")
        self.Address = params.get("Address")
        self.UseCharacter = params.get("UseCharacter")
        self.Model = params.get("Model")
        self.Vin = params.get("Vin")
        self.EngineNo = params.get("EngineNo")
        self.RegisterDate = params.get("RegisterDate")
        self.IssueDate = params.get("IssueDate")
        self.Seal = params.get("Seal")


class TextWaybill(AbstractModel):
    """運單識别結果

    """

    def __init__(self):
        """
        :param RecName: 收件人姓名
        :type RecName: :class:`taifucloudcloud.ocr.v20181119.models.WaybillObj`
        :param RecNum: 收件人手機號
        :type RecNum: :class:`taifucloudcloud.ocr.v20181119.models.WaybillObj`
        :param RecAddr: 收件人網址
        :type RecAddr: :class:`taifucloudcloud.ocr.v20181119.models.WaybillObj`
        :param SenderName: 寄件人姓名
        :type SenderName: :class:`taifucloudcloud.ocr.v20181119.models.WaybillObj`
        :param SenderNum: 寄件人手機號
        :type SenderNum: :class:`taifucloudcloud.ocr.v20181119.models.WaybillObj`
        :param SenderAddr: 寄件人網址
        :type SenderAddr: :class:`taifucloudcloud.ocr.v20181119.models.WaybillObj`
        :param WaybillNum: 運單號
        :type WaybillNum: :class:`taifucloudcloud.ocr.v20181119.models.WaybillObj`
        """
        self.RecName = None
        self.RecNum = None
        self.RecAddr = None
        self.SenderName = None
        self.SenderNum = None
        self.SenderAddr = None
        self.WaybillNum = None


    def _deserialize(self, params):
        if params.get("RecName") is not None:
            self.RecName = WaybillObj()
            self.RecName._deserialize(params.get("RecName"))
        if params.get("RecNum") is not None:
            self.RecNum = WaybillObj()
            self.RecNum._deserialize(params.get("RecNum"))
        if params.get("RecAddr") is not None:
            self.RecAddr = WaybillObj()
            self.RecAddr._deserialize(params.get("RecAddr"))
        if params.get("SenderName") is not None:
            self.SenderName = WaybillObj()
            self.SenderName._deserialize(params.get("SenderName"))
        if params.get("SenderNum") is not None:
            self.SenderNum = WaybillObj()
            self.SenderNum._deserialize(params.get("SenderNum"))
        if params.get("SenderAddr") is not None:
            self.SenderAddr = WaybillObj()
            self.SenderAddr._deserialize(params.get("SenderAddr"))
        if params.get("WaybillNum") is not None:
            self.WaybillNum = WaybillObj()
            self.WaybillNum._deserialize(params.get("WaybillNum"))


class TollInvoiceInfo(AbstractModel):
    """過路過橋費欄位訊息

    """

    def __init__(self):
        """
        :param Name: 識别出的欄位名稱（關鍵字）。
        :type Name: str
        :param Value: 識别出的欄位名稱對應的值，也就是欄位Name對應的字串結果。
        :type Value: str
        :param Rect: 文本行在旋轉糾正之後的圖像中的像素坐標。
        :type Rect: :class:`taifucloudcloud.ocr.v20181119.models.Rect`
        """
        self.Name = None
        self.Value = None
        self.Rect = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        if params.get("Rect") is not None:
            self.Rect = Rect()
            self.Rect._deserialize(params.get("Rect"))


class TollInvoiceOCRRequest(AbstractModel):
    """TollInvoiceOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class TollInvoiceOCRResponse(AbstractModel):
    """TollInvoiceOCR返回參數結構體

    """

    def __init__(self):
        """
        :param TollInvoiceInfos: 過路過橋費發票識别結果，具體内容請點擊左側連結。
        :type TollInvoiceInfos: list of TollInvoiceInfo
        :param Angle: 圖片旋轉角度（角度制），文本的水平方向爲0°，順時針爲正，逆時針爲負。
        :type Angle: float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TollInvoiceInfos = None
        self.Angle = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TollInvoiceInfos") is not None:
            self.TollInvoiceInfos = []
            for item in params.get("TollInvoiceInfos"):
                obj = TollInvoiceInfo()
                obj._deserialize(item)
                self.TollInvoiceInfos.append(obj)
        self.Angle = params.get("Angle")
        self.RequestId = params.get("RequestId")


class TrainTicketOCRRequest(AbstractModel):
    """TrainTicketOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class TrainTicketOCRResponse(AbstractModel):
    """TrainTicketOCR返回參數結構體

    """

    def __init__(self):
        """
        :param TicketNum: 編號
        :type TicketNum: str
        :param StartStation: 出發站
        :type StartStation: str
        :param DestinationStation: 到達站
        :type DestinationStation: str
        :param Date: 出發時間
        :type Date: str
        :param TrainNum: 車次
        :type TrainNum: str
        :param Seat: 座位號
        :type Seat: str
        :param Name: 姓名
        :type Name: str
        :param Price: 票價
        :type Price: str
        :param SeatCategory: 席别
        :type SeatCategory: str
        :param ID: 身份證號
        :type ID: str
        :param InvoiceType: 發票消費類型
        :type InvoiceType: str
        :param SerialNumber: 序列號
        :type SerialNumber: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TicketNum = None
        self.StartStation = None
        self.DestinationStation = None
        self.Date = None
        self.TrainNum = None
        self.Seat = None
        self.Name = None
        self.Price = None
        self.SeatCategory = None
        self.ID = None
        self.InvoiceType = None
        self.SerialNumber = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TicketNum = params.get("TicketNum")
        self.StartStation = params.get("StartStation")
        self.DestinationStation = params.get("DestinationStation")
        self.Date = params.get("Date")
        self.TrainNum = params.get("TrainNum")
        self.Seat = params.get("Seat")
        self.Name = params.get("Name")
        self.Price = params.get("Price")
        self.SeatCategory = params.get("SeatCategory")
        self.ID = params.get("ID")
        self.InvoiceType = params.get("InvoiceType")
        self.SerialNumber = params.get("SerialNumber")
        self.RequestId = params.get("RequestId")


class VatInvoiceOCRRequest(AbstractModel):
    """VatInvoiceOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class VatInvoiceOCRResponse(AbstractModel):
    """VatInvoiceOCR返回參數結構體

    """

    def __init__(self):
        """
        :param VatInvoiceInfos: 檢測到的文本訊息，具體内容請點擊左側連結。
        :type VatInvoiceInfos: list of TextVatInvoice
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.VatInvoiceInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VatInvoiceInfos") is not None:
            self.VatInvoiceInfos = []
            for item in params.get("VatInvoiceInfos"):
                obj = TextVatInvoice()
                obj._deserialize(item)
                self.VatInvoiceInfos.append(obj)
        self.RequestId = params.get("RequestId")


class VatRollInvoiceInfo(AbstractModel):
    """增值稅發票卷票訊息

    """

    def __init__(self):
        """
        :param Name: 識别出的欄位名稱（關鍵字）。
        :type Name: str
        :param Value: 識别出的欄位名稱對應的值，也就是欄位Name對應的字串結果。
        :type Value: str
        :param Rect: 文本行在旋轉糾正之後的圖像中的像素坐標。
        :type Rect: :class:`taifucloudcloud.ocr.v20181119.models.Rect`
        """
        self.Name = None
        self.Value = None
        self.Rect = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        if params.get("Rect") is not None:
            self.Rect = Rect()
            self.Rect._deserialize(params.get("Rect"))


class VatRollInvoiceOCRRequest(AbstractModel):
    """VatRollInvoiceOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class VatRollInvoiceOCRResponse(AbstractModel):
    """VatRollInvoiceOCR返回參數結構體

    """

    def __init__(self):
        """
        :param VatRollInvoiceInfos: 增值稅發票（卷票）識别結果，具體内容請點擊左側連結。
        :type VatRollInvoiceInfos: list of VatRollInvoiceInfo
        :param Angle: 圖片旋轉角度（角度制），文本的水平方向爲0°，順時針爲正，逆時針爲負。
        :type Angle: float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.VatRollInvoiceInfos = None
        self.Angle = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VatRollInvoiceInfos") is not None:
            self.VatRollInvoiceInfos = []
            for item in params.get("VatRollInvoiceInfos"):
                obj = VatRollInvoiceInfo()
                obj._deserialize(item)
                self.VatRollInvoiceInfos.append(obj)
        self.Angle = params.get("Angle")
        self.RequestId = params.get("RequestId")


class VehicleLicenseOCRRequest(AbstractModel):
    """VehicleLicenseOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。要求圖片經Base64編碼後不超過 7M，分辨率建議500*800以上，支援PNG、JPG、JPEG、BMP格式。建議卡片部分占據圖片2/3以上。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。要求圖片經Base64編碼後不超過 7M，分辨率建議500*800以上，支援PNG、JPG、JPEG、BMP格式。建議卡片部分占據圖片2/3以上。圖片下載時間不超過 3 秒。
建議圖片儲存於Top Cloud ，可保障更高的下載速度和穩定性。
        :type ImageUrl: str
        :param CardSide: FRONT 爲行駛證首頁正面（有紅色印章的一面），
BACK 爲行駛證副頁正面（有號碼號牌的一面）。
        :type CardSide: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.CardSide = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.CardSide = params.get("CardSide")


class VehicleLicenseOCRResponse(AbstractModel):
    """VehicleLicenseOCR返回參數結構體

    """

    def __init__(self):
        """
        :param FrontInfo: 行駛證首頁正面的識别結果，CardSide 爲 FRONT。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FrontInfo: :class:`taifucloudcloud.ocr.v20181119.models.TextVehicleFront`
        :param BackInfo: 行駛證副頁正面的識别結果，CardSide 爲 BACK。
注意：此欄位可能返回 null，表示取不到有效值。
        :type BackInfo: :class:`taifucloudcloud.ocr.v20181119.models.TextVehicleBack`
        :param RecognizeWarnCode: Code 告警碼清單和釋義：
-9102 影印件告警
-9103 翻拍件告警
-9106 ps告警
注：告警碼可以同時存在多個
        :type RecognizeWarnCode: list of int
        :param RecognizeWarnMsg: 告警碼說明：
WARN_DRIVER_LICENSE_COPY_CARD 影印件告警
WARN_DRIVER_LICENSE_SCREENED_CARD 翻拍件告警
WARN_DRIVER_LICENSE_PS_CARD ps告警
注：告警訊息可以同時存在多個
        :type RecognizeWarnMsg: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FrontInfo = None
        self.BackInfo = None
        self.RecognizeWarnCode = None
        self.RecognizeWarnMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FrontInfo") is not None:
            self.FrontInfo = TextVehicleFront()
            self.FrontInfo._deserialize(params.get("FrontInfo"))
        if params.get("BackInfo") is not None:
            self.BackInfo = TextVehicleBack()
            self.BackInfo._deserialize(params.get("BackInfo"))
        self.RecognizeWarnCode = params.get("RecognizeWarnCode")
        self.RecognizeWarnMsg = params.get("RecognizeWarnMsg")
        self.RequestId = params.get("RequestId")


class VehicleRegCertInfo(AbstractModel):
    """機動車登記證書識别結果

    """

    def __init__(self):
        """
        :param Name: 識别出的欄位名稱
        :type Name: str
        :param Value: 識别出的欄位名稱對應的值，也就是欄位name對應的字串結果。
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class VehicleRegCertOCRRequest(AbstractModel):
    """VehicleRegCertOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class VehicleRegCertOCRResponse(AbstractModel):
    """VehicleRegCertOCR返回參數結構體

    """

    def __init__(self):
        """
        :param VehicleRegCertInfos: 機動車登記證書識别結果，具體内容請點擊左側連結。
        :type VehicleRegCertInfos: list of VehicleRegCertInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.VehicleRegCertInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VehicleRegCertInfos") is not None:
            self.VehicleRegCertInfos = []
            for item in params.get("VehicleRegCertInfos"):
                obj = VehicleRegCertInfo()
                obj._deserialize(item)
                self.VehicleRegCertInfos.append(obj)
        self.RequestId = params.get("RequestId")


class VinOCRRequest(AbstractModel):
    """VinOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class VinOCRResponse(AbstractModel):
    """VinOCR返回參數結構體

    """

    def __init__(self):
        """
        :param Vin: 檢測到的車輛 VIN 碼。
        :type Vin: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Vin = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Vin = params.get("Vin")
        self.RequestId = params.get("RequestId")


class WaybillOCRRequest(AbstractModel):
    """WaybillOCR請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 圖片的 Base64 值。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片的 ImageUrl、ImageBase64 必須提供一個，如果都提供，只使用 ImageUrl。
        :type ImageBase64: str
        :param ImageUrl: 圖片的 Url 網址。
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class WaybillOCRResponse(AbstractModel):
    """WaybillOCR返回參數結構體

    """

    def __init__(self):
        """
        :param TextDetections: 檢測到的文本訊息，具體内容請點擊左側連結。
        :type TextDetections: :class:`taifucloudcloud.ocr.v20181119.models.TextWaybill`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = TextWaybill()
            self.TextDetections._deserialize(params.get("TextDetections"))
        self.RequestId = params.get("RequestId")


class WaybillObj(AbstractModel):
    """運單識别對象

    """

    def __init__(self):
        """
        :param Text: 識别出的文本行内容
        :type Text: str
        """
        self.Text = None


    def _deserialize(self, params):
        self.Text = params.get("Text")