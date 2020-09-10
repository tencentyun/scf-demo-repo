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
圖片儲存于Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存于Top Cloud 。
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


class Coord(AbstractModel):
    """坐标

    """

    def __init__(self):
        """
        :param X: 橫坐标
        :type X: int
        :param Y: 縱坐标
        :type Y: int
        """
        self.X = None
        self.Y = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")


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
圖片儲存于Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存于Top Cloud 。
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
圖片儲存于Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存于Top Cloud 。
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
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextDetection()
                obj._deserialize(item)
                self.TextDetections.append(obj)
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
圖片儲存于Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存于Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        :param Scene: 保留欄位。
        :type Scene: str
        """
        self.ImageBase64 = None
        self.ImageUrl = None
        self.Scene = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")
        self.Scene = params.get("Scene")


class GeneralBasicOCRResponse(AbstractModel):
    """GeneralBasicOCR返回參數結構體

    """

    def __init__(self):
        """
        :param TextDetections: 檢測到的文本訊息，具體内容請點擊左側連結。
        :type TextDetections: list of TextDetection
        :param Language: 檢測到的語言，目前支援的語種範圍爲：簡體中文、繁體中文、英文、日文、韓文。未來将陸續新增對更多語種的支援。
返回結果含義爲：zh-中英混合，jap-日文，kor-韓文。
        :type Language: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.Language = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextDetection()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.Language = params.get("Language")
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
圖片儲存于Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存于Top Cloud 。
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
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TextDetections = None
        self.Language = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextDetections") is not None:
            self.TextDetections = []
            for item in params.get("TextDetections"):
                obj = TextDetection()
                obj._deserialize(item)
                self.TextDetections.append(obj)
        self.Language = params.get("Language")
        self.RequestId = params.get("RequestId")


class IDCardOCRRequest(AbstractModel):
    """IDCardOCR請求參數結構體

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
圖片儲存于Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存于Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        :param CardSide: FRONT 爲身份證有照片的一面（人像面），
BACK 爲身份證有國徽的一面（國徽面）。
        :type CardSide: str
        :param Config: 可選欄位，根據需要選擇是否請求對應欄位。
目前包含的欄位爲：
CropIdCard，身份證照片裁剪，bool 類型，
CropPortrait，人像照片裁剪，bool 類型，
CopyWarn，影印件告警，bool 類型，
ReshootWarn，翻拍告警，bool 類型。

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
        :param IdNum: 身份證号（人像面）
        :type IdNum: str
        :param Authority: 發證機關（國徽面）
        :type Authority: str
        :param ValidDate: 證件有效期（國徽面）
        :type ValidDate: str
        :param AdvancedInfo: 擴展訊息，根據請求的可選欄位返回對應内容，不請求則不返回，具體輸入參考範例3。目前支援的擴展欄位爲：
IdCard，身份證照片，請求 CropIdCard 時返回；
Portrait，人像照片，請求 CropPortrait 時返回；
WarnInfos，告警訊息（Code - 告警碼，Msg - 告警訊息内容），識别出翻拍件或影印件時返回。

Code 告警碼清單和釋義：
-9103	身份證翻拍告警，
-9102	身份證影印件告警。
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
圖片儲存于Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存于Top Cloud 。
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


class TextArithmetic(AbstractModel):
    """算式識别結果

    """

    def __init__(self):
        """
        :param DetectedText: 識别出的文本行内容
        :type DetectedText: str
        :param Result: 結果
        :type Result: bool
        :param Confidence: 置信度 0 ~100
        :type Confidence: int
        :param Polygon: 文本行坐标，以四個頂點坐标表示
注意：此欄位可能返回 null，表示取不到有效值。
        :type Polygon: list of Coord
        :param AdvancedInfo: 此欄位爲擴展欄位。
        :type AdvancedInfo: str
        """
        self.DetectedText = None
        self.Result = None
        self.Confidence = None
        self.Polygon = None
        self.AdvancedInfo = None


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


class TextDetection(AbstractModel):
    """文字識别結果

    """

    def __init__(self):
        """
        :param DetectedText: 識别出的文本行内容
        :type DetectedText: str
        :param Confidence: 置信度 0 ~100
        :type Confidence: int
        :param Polygon: 文本行坐标，以四個頂點坐标表示
注意：此欄位可能返回 null，表示取不到有效值。
        :type Polygon: list of Coord
        :param AdvancedInfo: 此欄位爲擴展欄位。
GeneralBasicOcr介面返回段落訊息Parag，包含ParagNo。
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


class TextDetectionEn(AbstractModel):
    """英文識别結果

    """

    def __init__(self):
        """
        :param DetectedText: 識别出的文本行内容
        :type DetectedText: str
        :param Confidence: 置信度 0 ~100
        :type Confidence: int
        :param Polygon: 文本行坐标，以四個頂點坐标表示
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
        :param Polygon: 文本行坐标，以四個頂點坐标表示
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


class TextWaybill(AbstractModel):
    """運單識别結果

    """

    def __init__(self):
        """
        :param RecName: 收件人姓名
        :type RecName: :class:`taifucloudcloud.ocr.v20181119.models.WaybillObj`
        :param RecNum: 收件人手機号
        :type RecNum: :class:`taifucloudcloud.ocr.v20181119.models.WaybillObj`
        :param RecAddr: 收件人網址
        :type RecAddr: :class:`taifucloudcloud.ocr.v20181119.models.WaybillObj`
        :param SenderName: 寄件人姓名
        :type SenderName: :class:`taifucloudcloud.ocr.v20181119.models.WaybillObj`
        :param SenderNum: 寄件人手機号
        :type SenderNum: :class:`taifucloudcloud.ocr.v20181119.models.WaybillObj`
        :param SenderAddr: 寄件人網址
        :type SenderAddr: :class:`taifucloudcloud.ocr.v20181119.models.WaybillObj`
        :param WaybillNum: 運單号
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
圖片儲存于Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存于Top Cloud 。
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
圖片儲存于Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存于Top Cloud 。
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
注意：此欄位可能返回 null，表示取不到有效值。
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