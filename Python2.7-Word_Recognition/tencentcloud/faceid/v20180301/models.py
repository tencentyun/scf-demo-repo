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


class BankCardVerificationRequest(AbstractModel):
    """BankCardVerification請求參數結構體

    """

    def __init__(self):
        """
        :param IdCard: 身份證號
        :type IdCard: str
        :param Name: 姓名
        :type Name: str
        :param BankCard: 銀行卡
        :type BankCard: str
        """
        self.IdCard = None
        self.Name = None
        self.BankCard = None


    def _deserialize(self, params):
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.BankCard = params.get("BankCard")


class BankCardVerificationResponse(AbstractModel):
    """BankCardVerification返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 認證結果碼。
'0': '認證通過'
'-1': '認證未通過'
'-2': '姓名校驗不通過'
'-3': '身份證號碼有誤'
'-4': '銀行卡號碼有誤'
'-5': '持卡人訊息有誤'
'-6': '未開通無卡支付'
'-7': '此卡被沒收'
'-8': '無效卡號'
'-9': '此卡無對應發卡行'
'-10': '該卡未初始化或睡眠卡'
'-11': '作弊卡、吞卡'
'-12': '此卡已挂失'
'-13': '該卡已過期'
'-14': '受限制的卡'
'-15': '密碼錯誤次數超限'
'-16': '發卡行不支援此交易'
'-17': '服務繁忙'
        :type Result: str
        :param Description: 認證結果訊息。
        :type Description: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class DetectAuthRequest(AbstractModel):
    """DetectAuth請求參數結構體

    """

    def __init__(self):
        """
        :param RuleId: 用於細分客戶使用場景，由 側在線下對接時分配。
        :type RuleId: str
        :param TerminalType: 本介面不需要傳遞此參數。
        :type TerminalType: str
        :param IdCard: 身份標識（與警察權威庫比對時必須是身份證號）。
規則：a-zA-Z0-9組合。最長長度32位。
        :type IdCard: str
        :param Name: 姓名。最長長度32位。中文請使用UTF-8編碼。
        :type Name: str
        :param RedirectUrl: 認證結束後重定向的回調連結網址。最長長度1024位。
        :type RedirectUrl: str
        :param Extra: 透傳欄位，在獲取驗證結果時返回。
        :type Extra: str
        :param ImageBase64: 用於人臉比對的照片，圖片的BASE64值；
BASE64編碼後的圖片數據大小不超過3M，僅支援jpg、png格式。
        :type ImageBase64: str
        """
        self.RuleId = None
        self.TerminalType = None
        self.IdCard = None
        self.Name = None
        self.RedirectUrl = None
        self.Extra = None
        self.ImageBase64 = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.TerminalType = params.get("TerminalType")
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.RedirectUrl = params.get("RedirectUrl")
        self.Extra = params.get("Extra")
        self.ImageBase64 = params.get("ImageBase64")


class DetectAuthResponse(AbstractModel):
    """DetectAuth返回參數結構體

    """

    def __init__(self):
        """
        :param Url: 用於發起核身流程的URL，僅 H5場景使用。
        :type Url: str
        :param BizToken: 一次核身流程的標識，有效時間爲7,200秒；
完成核身後，可用該標識獲取驗證結果訊息。
        :type BizToken: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Url = None
        self.BizToken = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.BizToken = params.get("BizToken")
        self.RequestId = params.get("RequestId")


class GetActionSequenceRequest(AbstractModel):
    """GetActionSequence請求參數結構體

    """


class GetActionSequenceResponse(AbstractModel):
    """GetActionSequence返回參數結構體

    """

    def __init__(self):
        """
        :param ActionSequence: 動作順序(2,1 or 1,2) 。1代表張嘴，2代表閉眼。
        :type ActionSequence: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ActionSequence = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ActionSequence = params.get("ActionSequence")
        self.RequestId = params.get("RequestId")


class GetDetectInfoRequest(AbstractModel):
    """GetDetectInfo請求參數結構體

    """

    def __init__(self):
        """
        :param BizToken: 人臉核身流程的標識，調用DetectAuth介面時生成。
        :type BizToken: str
        :param RuleId: 用於細分客戶使用場景，由 側在線下對接時分配。
        :type RuleId: str
        :param InfoType: 指定拉取的結果訊息，取值（0：全部；1：文本類；2：身份證正反面；3：視訊最佳截圖照片；4：視訊）。
如 134表示拉取文本類、視訊最佳截圖照片、視訊。
        :type InfoType: str
        """
        self.BizToken = None
        self.RuleId = None
        self.InfoType = None


    def _deserialize(self, params):
        self.BizToken = params.get("BizToken")
        self.RuleId = params.get("RuleId")
        self.InfoType = params.get("InfoType")


class GetDetectInfoResponse(AbstractModel):
    """GetDetectInfo返回參數結構體

    """

    def __init__(self):
        """
        :param DetectInfo: JSON字串。
{
  // 文本類訊息
  "Text": {
    "ErrCode": null,      // 本次核身最終結果。0爲成功
    "ErrMsg": null,       // 本次核身的錯誤訊息。
    "IdCard": "",         // 本次核身最終獲得的身份證號。
    "Name": "",           // 本次核身最終獲得的姓名。
    "OcrNation": null,    // ocr階段獲取的民族
    "OcrAddress": null,   // ocr階段獲取的網址
    "OcrBirth": null,     // ocr階段獲取的出生訊息
    "OcrAuthority": null, // ocr階段獲取的證件簽發機關
    "OcrValidDate": null, // ocr階段獲取的證件有效期
    "OcrName": null,      // ocr階段獲取的姓名
    "OcrIdCard": null,    // ocr階段獲取的身份證號
    "OcrGender": null,    // ocr階段獲取的性别
    "LiveStatus": null,   // 活體檢測階段的錯誤碼。0爲成功
    "LiveMsg": null,      // 活體檢測階段的錯誤訊息
    "Comparestatus": null,// 一比一階段的錯誤碼。0爲成功
    "Comparemsg": null,   // 一比一階段的錯誤訊息
    "Extra": "",          // DetectAuth結果傳進來的Extra訊息
    "Detail": {           // 活體一比一訊息詳情
      "LivenessData": []
    }
  },
  // 身份證正反面照片Base64
  "IdCardData": {
    "OcrFront": null,
    "OcrBack": null
  },
  // 視訊最佳幀截圖Base64
  "BestFrame": {
    "BestFrame": null
  },
  // 活體視訊Base64
  "VideoData": {
    "LivenessVideo": null
  }
}
        :type DetectInfo: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DetectInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DetectInfo = params.get("DetectInfo")
        self.RequestId = params.get("RequestId")


class GetLiveCodeRequest(AbstractModel):
    """GetLiveCode請求參數結構體

    """


class GetLiveCodeResponse(AbstractModel):
    """GetLiveCode返回參數結構體

    """

    def __init__(self):
        """
        :param LiveCode: 數字驗證碼，如：1234
        :type LiveCode: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.LiveCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LiveCode = params.get("LiveCode")
        self.RequestId = params.get("RequestId")


class IdCardVerificationRequest(AbstractModel):
    """IdCardVerification請求參數結構體

    """

    def __init__(self):
        """
        :param IdCard: 身份證號
        :type IdCard: str
        :param Name: 姓名
        :type Name: str
        """
        self.IdCard = None
        self.Name = None


    def _deserialize(self, params):
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")


class IdCardVerificationResponse(AbstractModel):
    """IdCardVerification返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 認證結果碼。
0: 姓名和身份證號一緻
-1: 姓名和身份證號不一緻
-2: 身份證號錯誤
-3: 姓名錯誤
-4: 認證出錯
        :type Result: str
        :param Description: 認證結果訊息。
        :type Description: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class ImageRecognitionRequest(AbstractModel):
    """ImageRecognition請求參數結構體

    """

    def __init__(self):
        """
        :param IdCard: 身份證號
        :type IdCard: str
        :param Name: 姓名。中文請使用UTF-8編碼。
        :type Name: str
        :param ImageBase64: 用於人臉比對的照片，圖片的BASE64值；
BASE64編碼後的圖片數據大小不超過3M，僅支援jpg、png格式。
        :type ImageBase64: str
        :param Optional: 本介面不需要傳遞此參數。
        :type Optional: str
        """
        self.IdCard = None
        self.Name = None
        self.ImageBase64 = None
        self.Optional = None


    def _deserialize(self, params):
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.ImageBase64 = params.get("ImageBase64")
        self.Optional = params.get("Optional")


class ImageRecognitionResponse(AbstractModel):
    """ImageRecognition返回參數結構體

    """

    def __init__(self):
        """
        :param Sim: 相似度，取值範圍 [0.00, 100.00]。推薦相似度大於等於70時可判斷爲同一人，可根據具體場景自行調整阈值（阈值70的誤通過率爲千分之一，阈值80的誤通過率是萬分之一）
        :type Sim: float
        :param Result: 業務錯誤碼，成功情況返回Success, 錯誤情況請參考下方錯誤碼 清單中FailedOperation部分
        :type Result: str
        :param Description: 業務錯誤描述
        :type Description: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Sim = None
        self.Result = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Sim = params.get("Sim")
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class LivenessCompareRequest(AbstractModel):
    """LivenessCompare請求參數結構體

    """

    def __init__(self):
        """
        :param ImageBase64: 用於人臉比對的照片，圖片的BASE64值；
BASE64編碼後的圖片數據大小不超過3M，僅支援jpg、png格式。
        :type ImageBase64: str
        :param VideoBase64: 用於活體檢測的視訊，視訊的BASE64值；
BASE64編碼後的大小不超過5M，支援mp4、avi、flv格式。
        :type VideoBase64: str
        :param LivenessType: 活體檢測類型，取值：LIP/ACTION/SILENT。
LIP爲數字模式，ACTION爲動作模式，SILENT爲靜默模式，三種模式選擇一種傳入。
        :type LivenessType: str
        :param ValidateData: 數字模式傳參：數字驗證碼(1234)，需先調用介面獲取數字驗證碼；
動作模式傳參：傳動作順序(2,1 or 1,2)，需先調用介面獲取動作順序；
靜默模式傳參：空。
        :type ValidateData: str
        :param Optional: 本介面不需要傳遞此參數。
        :type Optional: str
        """
        self.ImageBase64 = None
        self.VideoBase64 = None
        self.LivenessType = None
        self.ValidateData = None
        self.Optional = None


    def _deserialize(self, params):
        self.ImageBase64 = params.get("ImageBase64")
        self.VideoBase64 = params.get("VideoBase64")
        self.LivenessType = params.get("LivenessType")
        self.ValidateData = params.get("ValidateData")
        self.Optional = params.get("Optional")


class LivenessCompareResponse(AbstractModel):
    """LivenessCompare返回參數結構體

    """

    def __init__(self):
        """
        :param BestFrameBase64: 驗證通過後的視訊最佳截圖照片，照片爲BASE64編碼後的值，jpg格式。
        :type BestFrameBase64: str
        :param Sim: 相似度，取值範圍 [0.00, 100.00]。推薦相似度大於等於70時可判斷爲同一人，可根據具體場景自行調整阈值（阈值70的誤通過率爲千分之一，阈值80的誤通過率是萬分之一）。
        :type Sim: float
        :param Result: 業務錯誤碼，成功情況返回Success, 錯誤情況請參考下方錯誤碼 清單中FailedOperation部分
        :type Result: str
        :param Description: 業務錯誤描述
        :type Description: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.BestFrameBase64 = None
        self.Sim = None
        self.Result = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BestFrameBase64 = params.get("BestFrameBase64")
        self.Sim = params.get("Sim")
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class LivenessRecognitionRequest(AbstractModel):
    """LivenessRecognition請求參數結構體

    """

    def __init__(self):
        """
        :param IdCard: 身份證號
        :type IdCard: str
        :param Name: 姓名。中文請使用UTF-8編碼。
        :type Name: str
        :param VideoBase64: 用於活體檢測的視訊，視訊的BASE64值；
BASE64編碼後的大小不超過5M，支援mp4、avi、flv格式。
        :type VideoBase64: str
        :param LivenessType: 活體檢測類型，取值：LIP/ACTION/SILENT。
LIP爲數字模式，ACTION爲動作模式，SILENT爲靜默模式，三種模式選擇一種傳入。
        :type LivenessType: str
        :param ValidateData: 數字模式傳參：數字驗證碼(1234)，需先調用介面獲取數字驗證碼；
動作模式傳參：傳動作順序(2,1 or 1,2)，需先調用介面獲取動作順序；
靜默模式傳參：空。
        :type ValidateData: str
        :param Optional: 本介面不需要傳遞此參數。
        :type Optional: str
        """
        self.IdCard = None
        self.Name = None
        self.VideoBase64 = None
        self.LivenessType = None
        self.ValidateData = None
        self.Optional = None


    def _deserialize(self, params):
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.VideoBase64 = params.get("VideoBase64")
        self.LivenessType = params.get("LivenessType")
        self.ValidateData = params.get("ValidateData")
        self.Optional = params.get("Optional")


class LivenessRecognitionResponse(AbstractModel):
    """LivenessRecognition返回參數結構體

    """

    def __init__(self):
        """
        :param BestFrameBase64: 驗證通過後的視訊最佳截圖照片，照片爲BASE64編碼後的值，jpg格式。
        :type BestFrameBase64: str
        :param Sim: 相似度，取值範圍 [0.00, 100.00]。推薦相似度大於等於70時可判斷爲同一人，可根據具體場景自行調整阈值（阈值70的誤通過率爲千分之一，阈值80的誤通過率是萬分之一）
        :type Sim: float
        :param Result: 業務錯誤碼，成功情況返回Success, 錯誤情況請參考下方錯誤碼 清單中FailedOperation部分
        :type Result: str
        :param Description: 業務錯誤描述
        :type Description: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.BestFrameBase64 = None
        self.Sim = None
        self.Result = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BestFrameBase64 = params.get("BestFrameBase64")
        self.Sim = params.get("Sim")
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")