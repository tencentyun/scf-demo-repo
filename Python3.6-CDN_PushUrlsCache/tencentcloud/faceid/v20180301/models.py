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


class BankCard2EVerificationRequest(AbstractModel):
    """BankCard2EVerification請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 姓名
        :type Name: str
        :param BankCard: 銀行卡
        :type BankCard: str
        """
        self.Name = None
        self.BankCard = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.BankCard = params.get("BankCard")


class BankCard2EVerificationResponse(AbstractModel):
    """BankCard2EVerification返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 認證結果碼
計費結果碼：
  '0': '認證通過'
  '-1': '認證未通過'
 '-4': '持卡人訊息有誤'
  '-5': '未開通無卡支付'
  '-6': '此卡被沒收'
  '-7': '無效卡號'
  '-8': '此卡無對應發卡行'
  '-9': '該卡未初始化或睡眠卡'
  '-10': '作弊卡、吞卡'
  '-11': '此卡已挂失'
  '-12': '該卡已過期'
  '-13': '受限制的卡'
  '-14': '密碼錯誤次數超限'
  '-15': '發卡行不支援此交易'
不計費結果碼：
  '-2': '姓名校驗不通過'
  '-3': '銀行卡號碼有誤'
  '-16': '驗證中心服務繁忙'
        :type Result: str
        :param Description: 業務結果描述。
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


class BankCard4EVerificationRequest(AbstractModel):
    """BankCard4EVerification請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 姓名
        :type Name: str
        :param BankCard: 銀行卡
        :type BankCard: str
        :param Phone: 手機號碼
        :type Phone: str
        :param IdCard: 開戶證件號，與CertType參數的證件類型一緻，如：身份證，則傳入身份證號。
        :type IdCard: str
        :param CertType: 證件類型，請确認該證件爲開戶時使用的證件類型，未用於開戶的證件訊息不支援驗證。
目前預設：0 身份證，其他證件類型需求可以聯系小助手faceid001确認。
        :type CertType: int
        """
        self.Name = None
        self.BankCard = None
        self.Phone = None
        self.IdCard = None
        self.CertType = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.BankCard = params.get("BankCard")
        self.Phone = params.get("Phone")
        self.IdCard = params.get("IdCard")
        self.CertType = params.get("CertType")


class BankCard4EVerificationResponse(AbstractModel):
    """BankCard4EVerification返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 認證結果碼
收費結果碼：
'0': '認證通過'
'-1': '認證未通過'
'-6': '持卡人訊息有誤'
'-7': '未開通無卡支付'
'-8': '此卡被沒收'
'-9': '無效卡號'
'-10': '此卡無對應發卡行'
'-11': '該卡未初始化或睡眠卡'
'-12': '作弊卡、吞卡'
'-13': '此卡已挂失'
'-14': '該卡已過期'
'-15': '受限制的卡'
'-16': '密碼錯誤次數超限'
'-17': '發卡行不支援此交易'
不收費結果碼：
'-2': '姓名校驗不通過'
'-3': '身份證號碼有誤'
'-4': '銀行卡號碼有誤'
'-5': '手機號碼不合法'
'-18': '驗證中心服務繁忙'
        :type Result: str
        :param Description: 業務結果描述。
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


class BankCardVerificationRequest(AbstractModel):
    """BankCardVerification請求參數結構體

    """

    def __init__(self):
        """
        :param IdCard: 開戶證件號，與CertType參數的證件類型一緻，如：身份證，則傳入身份證號。
        :type IdCard: str
        :param Name: 姓名
        :type Name: str
        :param BankCard: 銀行卡
        :type BankCard: str
        :param CertType: 證件類型，請确認該證件爲開戶時使用的證件類型，未用於開戶的證件訊息不支援驗證。
目前預設：0 身份證，其他證件類型需求可以聯系小助手faceid001确認。
        :type CertType: int
        """
        self.IdCard = None
        self.Name = None
        self.BankCard = None
        self.CertType = None


    def _deserialize(self, params):
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.BankCard = params.get("BankCard")
        self.CertType = params.get("CertType")


class BankCardVerificationResponse(AbstractModel):
    """BankCardVerification返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 認證結果碼
收費結果碼：
'0': '認證通過'
'-1': '認證未通過'
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
不收費結果碼：
'-2': '姓名校驗不通過'
'-3': '身份證號碼有誤'
'-4': '銀行卡號碼有誤'
'-17': '驗證中心服務繁忙'
        :type Result: str
        :param Description: 業務結果描述。
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
        :param RuleId: 用於細分客戶使用場景，申請開通服務後，可以在Top Cloud 慧眼人臉核身控制台（https://console.cloud.taifucloud.com/faceid） 自助接入裏面創建，審核通過後即可調用。如有疑問，請加慧眼小助手 （faceid001）進行咨詢。
        :type RuleId: str
        :param TerminalType: 本介面不需要傳遞此參數。
        :type TerminalType: str
        :param IdCard: 身份標識（未使用OCR服務時，必須傳入）。
規則：a-zA-Z0-9組合。最長長度32位。
        :type IdCard: str
        :param Name: 姓名。（未使用OCR服務時，必須傳入）最長長度32位。中文請使用UTF-8編碼。
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


class DetectDetail(AbstractModel):
    """活體一比一詳情

    """

    def __init__(self):
        """
        :param ReqTime: 請求時間戳。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReqTime: str
        :param Seq: 本次活體一比一請求的唯一標記。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Seq: str
        :param Idcard: 參與本次活體一比一的身份證號。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Idcard: str
        :param Name: 參與本次活體一比一的姓名。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Name: str
        :param Sim: 本次活體一比一的相似度。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Sim: str
        :param IsNeedCharge: 本次活體一比一是否收費
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsNeedCharge: bool
        :param Errcode: 本次活體一比一最終結果。0爲成功
注意：此欄位可能返回 null，表示取不到有效值。
        :type Errcode: int
        :param Errmsg: 本次活體一比一最終結果描述。（僅描述用，文案更新時不會通知。）
注意：此欄位可能返回 null，表示取不到有效值。
        :type Errmsg: str
        :param Livestatus: 本次活體結果。0爲成功
注意：此欄位可能返回 null，表示取不到有效值。
        :type Livestatus: int
        :param Livemsg: 本次活體結果描述。（僅描述用，文案更新時不會通知。）
注意：此欄位可能返回 null，表示取不到有效值。
        :type Livemsg: str
        :param Comparestatus: 本次一比一結果。0爲成功
注意：此欄位可能返回 null，表示取不到有效值。
        :type Comparestatus: int
        :param Comparemsg: 本次一比一結果描述。（僅描述用，文案更新時不會通知。）
注意：此欄位可能返回 null，表示取不到有效值。
        :type Comparemsg: str
        """
        self.ReqTime = None
        self.Seq = None
        self.Idcard = None
        self.Name = None
        self.Sim = None
        self.IsNeedCharge = None
        self.Errcode = None
        self.Errmsg = None
        self.Livestatus = None
        self.Livemsg = None
        self.Comparestatus = None
        self.Comparemsg = None


    def _deserialize(self, params):
        self.ReqTime = params.get("ReqTime")
        self.Seq = params.get("Seq")
        self.Idcard = params.get("Idcard")
        self.Name = params.get("Name")
        self.Sim = params.get("Sim")
        self.IsNeedCharge = params.get("IsNeedCharge")
        self.Errcode = params.get("Errcode")
        self.Errmsg = params.get("Errmsg")
        self.Livestatus = params.get("Livestatus")
        self.Livemsg = params.get("Livemsg")
        self.Comparestatus = params.get("Comparestatus")
        self.Comparemsg = params.get("Comparemsg")


class DetectInfoBestFrame(AbstractModel):
    """核身最佳幀訊息

    """

    def __init__(self):
        """
        :param BestFrame: 活體比對最佳幀。
注意：此欄位可能返回 null，表示取不到有效值。
        :type BestFrame: str
        :param BestFrames: 自截幀。
注意：此欄位可能返回 null，表示取不到有效值。
        :type BestFrames: list of str
        """
        self.BestFrame = None
        self.BestFrames = None


    def _deserialize(self, params):
        self.BestFrame = params.get("BestFrame")
        self.BestFrames = params.get("BestFrames")


class DetectInfoIdCardData(AbstractModel):
    """核身身份證圖片訊息

    """

    def __init__(self):
        """
        :param OcrFront: OCR正面照片的base64編碼。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OcrFront: str
        :param OcrBack: OCR反面照片的base64編碼
注意：此欄位可能返回 null，表示取不到有效值。
        :type OcrBack: str
        :param ProcessedFrontImage: 旋轉裁邊後的正面照片base64編碼。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProcessedFrontImage: str
        :param ProcessedBackImage: 旋轉裁邊後的背面照片base64編碼。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProcessedBackImage: str
        :param Avatar: 身份證正面人像圖base64編碼。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Avatar: str
        """
        self.OcrFront = None
        self.OcrBack = None
        self.ProcessedFrontImage = None
        self.ProcessedBackImage = None
        self.Avatar = None


    def _deserialize(self, params):
        self.OcrFront = params.get("OcrFront")
        self.OcrBack = params.get("OcrBack")
        self.ProcessedFrontImage = params.get("ProcessedFrontImage")
        self.ProcessedBackImage = params.get("ProcessedBackImage")
        self.Avatar = params.get("Avatar")


class DetectInfoText(AbstractModel):
    """核身文本訊息

    """

    def __init__(self):
        """
        :param ErrCode: 本次流程最終驗證結果。0爲成功
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param ErrMsg: 本次流程最終驗證結果描述。（僅描述用，文案更新時不會通知。）
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param IdCard: 本次驗證使用的身份證號。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IdCard: str
        :param Name: 本次驗證使用的姓名。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Name: str
        :param OcrNation: Ocr識别結果。民族。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OcrNation: str
        :param OcrAddress: Ocr識别結果。家庭住址。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OcrAddress: str
        :param OcrBirth: Ocr識别結果。生日。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OcrBirth: str
        :param OcrAuthority: Ocr識别結果。簽發機關。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OcrAuthority: str
        :param OcrValidDate: Ocr識别結果。有效日期。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OcrValidDate: str
        :param OcrName: Ocr識别結果。姓名。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OcrName: str
        :param OcrIdCard: Ocr識别結果。身份證號。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OcrIdCard: str
        :param OcrGender: Ocr識别結果。性别。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OcrGender: str
        :param LiveStatus: 本次流程最終活體結果。0爲成功
注意：此欄位可能返回 null，表示取不到有效值。
        :type LiveStatus: int
        :param LiveMsg: 本次流程最終活體結果描述。（僅描述用，文案更新時不會通知。）
注意：此欄位可能返回 null，表示取不到有效值。
        :type LiveMsg: str
        :param Comparestatus: 本次流程最終一比一結果。0爲成功
注意：此欄位可能返回 null，表示取不到有效值。
        :type Comparestatus: int
        :param Comparemsg: 本次流程最終一比一結果描述。（僅描述用，文案更新時不會通知。）
注意：此欄位可能返回 null，表示取不到有效值。
        :type Comparemsg: str
        :param Sim: 本次流程活體一比一的分數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Sim: str
        :param Location: 地理位置經緯度。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Location: str
        :param Extra: Auth介面帶入額外訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Extra: str
        :param LivenessDetail: 本次流程進行的活體一比一流水。
注意：此欄位可能返回 null，表示取不到有效值。
        :type LivenessDetail: list of DetectDetail
        :param Mobile: 手機號碼。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Mobile: str
        """
        self.ErrCode = None
        self.ErrMsg = None
        self.IdCard = None
        self.Name = None
        self.OcrNation = None
        self.OcrAddress = None
        self.OcrBirth = None
        self.OcrAuthority = None
        self.OcrValidDate = None
        self.OcrName = None
        self.OcrIdCard = None
        self.OcrGender = None
        self.LiveStatus = None
        self.LiveMsg = None
        self.Comparestatus = None
        self.Comparemsg = None
        self.Sim = None
        self.Location = None
        self.Extra = None
        self.LivenessDetail = None
        self.Mobile = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.OcrNation = params.get("OcrNation")
        self.OcrAddress = params.get("OcrAddress")
        self.OcrBirth = params.get("OcrBirth")
        self.OcrAuthority = params.get("OcrAuthority")
        self.OcrValidDate = params.get("OcrValidDate")
        self.OcrName = params.get("OcrName")
        self.OcrIdCard = params.get("OcrIdCard")
        self.OcrGender = params.get("OcrGender")
        self.LiveStatus = params.get("LiveStatus")
        self.LiveMsg = params.get("LiveMsg")
        self.Comparestatus = params.get("Comparestatus")
        self.Comparemsg = params.get("Comparemsg")
        self.Sim = params.get("Sim")
        self.Location = params.get("Location")
        self.Extra = params.get("Extra")
        if params.get("LivenessDetail") is not None:
            self.LivenessDetail = []
            for item in params.get("LivenessDetail"):
                obj = DetectDetail()
                obj._deserialize(item)
                self.LivenessDetail.append(obj)
        self.Mobile = params.get("Mobile")


class DetectInfoVideoData(AbstractModel):
    """核身視訊訊息

    """

    def __init__(self):
        """
        :param LivenessVideo: 活體視訊的base64編碼
注意：此欄位可能返回 null，表示取不到有效值。
        :type LivenessVideo: str
        """
        self.LivenessVideo = None


    def _deserialize(self, params):
        self.LivenessVideo = params.get("LivenessVideo")


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


class GetDetectInfoEnhancedRequest(AbstractModel):
    """GetDetectInfoEnhanced請求參數結構體

    """

    def __init__(self):
        """
        :param BizToken: 人臉核身流程的標識，調用DetectAuth介面時生成。
        :type BizToken: str
        :param RuleId: 用於細分客戶使用場景，由 側在線下對接時分配。
        :type RuleId: str
        :param InfoType: 指定拉取的結果訊息，取值（0：全部；1：文本類；2：身份證訊息；3：視訊最佳截圖訊息；4：視訊訊息）。
如 134表示拉取文本類、視訊最佳截圖訊息、視訊訊息。
預設值：0
        :type InfoType: str
        :param BestFramesCount: 從活體視訊中截取一定張數的最佳幀。預設爲0，最大爲10，超出10的最多只給10張。（InfoType需要包含3）
        :type BestFramesCount: int
        :param IsCutIdCardImage: 是否對身份證照片進行裁邊。預設爲false。（InfoType需要包含2）
        :type IsCutIdCardImage: bool
        :param IsNeedIdCardAvatar: 是否需要從身份證中摳出頭像。預設爲false。（InfoType需要包含2）
        :type IsNeedIdCardAvatar: bool
        """
        self.BizToken = None
        self.RuleId = None
        self.InfoType = None
        self.BestFramesCount = None
        self.IsCutIdCardImage = None
        self.IsNeedIdCardAvatar = None


    def _deserialize(self, params):
        self.BizToken = params.get("BizToken")
        self.RuleId = params.get("RuleId")
        self.InfoType = params.get("InfoType")
        self.BestFramesCount = params.get("BestFramesCount")
        self.IsCutIdCardImage = params.get("IsCutIdCardImage")
        self.IsNeedIdCardAvatar = params.get("IsNeedIdCardAvatar")


class GetDetectInfoEnhancedResponse(AbstractModel):
    """GetDetectInfoEnhanced返回參數結構體

    """

    def __init__(self):
        """
        :param Text: 文本類訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Text: :class:`taifucloudcloud.faceid.v20180301.models.DetectInfoText`
        :param IdCardData: 身份證照片訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IdCardData: :class:`taifucloudcloud.faceid.v20180301.models.DetectInfoIdCardData`
        :param BestFrame: 最佳幀訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type BestFrame: :class:`taifucloudcloud.faceid.v20180301.models.DetectInfoBestFrame`
        :param VideoData: 視訊訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type VideoData: :class:`taifucloudcloud.faceid.v20180301.models.DetectInfoVideoData`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Text = None
        self.IdCardData = None
        self.BestFrame = None
        self.VideoData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Text") is not None:
            self.Text = DetectInfoText()
            self.Text._deserialize(params.get("Text"))
        if params.get("IdCardData") is not None:
            self.IdCardData = DetectInfoIdCardData()
            self.IdCardData._deserialize(params.get("IdCardData"))
        if params.get("BestFrame") is not None:
            self.BestFrame = DetectInfoBestFrame()
            self.BestFrame._deserialize(params.get("BestFrame"))
        if params.get("VideoData") is not None:
            self.VideoData = DetectInfoVideoData()
            self.VideoData._deserialize(params.get("VideoData"))
        self.RequestId = params.get("RequestId")


class GetDetectInfoRequest(AbstractModel):
    """GetDetectInfo請求參數結構體

    """

    def __init__(self):
        """
        :param BizToken: 人臉核身流程的標識，調用DetectAuth介面時生成。
        :type BizToken: str
        :param RuleId: 用於細分客戶使用場景，申請開通服務後，可以在Top Cloud 慧眼人臉核身控制台（https://console.cloud.taifucloud.com/faceid） 自助接入裏面創建，審核通過後即可調用。如有疑問，請加慧眼小助手 （faceid001）進行咨詢。
        :type RuleId: str
        :param InfoType: 指定拉取的結果訊息，取值（0：全部；1：文本類；2：身份證正反面；3：視訊最佳截圖照片；4：視訊）。
如 134表示拉取文本類、視訊最佳截圖照片、視訊。
預設值：0
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
    "ErrMsg": null,       // 本次核身最終結果訊息描述。
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
    "Location": null, // 地理位置訊息
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


class IdCardOCRVerificationRequest(AbstractModel):
    """IdCardOCRVerification請求參數結構體

    """

    def __init__(self):
        """
        :param IdCard: 身份證號
姓名和身份證號、ImageBase64、ImageUrl三者必須提供其中之一。若都提供了，則按照姓名和身份證號>ImageBase64>ImageUrl的優先級使用參數。
        :type IdCard: str
        :param Name: 姓名
        :type Name: str
        :param ImageBase64: 身份證人像面的 Base64 值
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經Base64編碼後不超過 3M。圖片下載時間不超過 3 秒。
        :type ImageBase64: str
        :param ImageUrl: 身份證人像面的 Url 網址
支援的圖片格式：PNG、JPG、JPEG，暫不支援 GIF 格式。
支援的圖片大小：所下載圖片經 Base64 編碼後不超過 3M。圖片下載時間不超過 3 秒。
圖片儲存於Top Cloud 的 Url 可保障更高的下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的 Url 速度和穩定性可能受一定影響。
        :type ImageUrl: str
        """
        self.IdCard = None
        self.Name = None
        self.ImageBase64 = None
        self.ImageUrl = None


    def _deserialize(self, params):
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.ImageBase64 = params.get("ImageBase64")
        self.ImageUrl = params.get("ImageUrl")


class IdCardOCRVerificationResponse(AbstractModel):
    """IdCardOCRVerification返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 認證結果碼，收費情況如下。
收費結果碼：
0: 姓名和身份證號一緻
-1: 姓名和身份證號不一緻
不收費結果碼：
-2: 非法身份證號（長度、校驗位等不正确）
-3: 非法姓名（長度、格式等不正确）
-4: 證件庫服務異常
-5: 證件庫中無此身份證記錄
        :type Result: str
        :param Description: 業務結果描述。
        :type Description: str
        :param Name: 用於驗證的姓名
        :type Name: str
        :param IdCard: 用於驗證的身份證號
        :type IdCard: str
        :param Sex: OCR得到的性别
注意：此欄位可能返回 null，表示取不到有效值。
        :type Sex: str
        :param Nation: OCR得到的民族
注意：此欄位可能返回 null，表示取不到有效值。
        :type Nation: str
        :param Birth: OCR得到的生日
注意：此欄位可能返回 null，表示取不到有效值。
        :type Birth: str
        :param Address: OCR得到的網址
注意：此欄位可能返回 null，表示取不到有效值。
        :type Address: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.Name = None
        self.IdCard = None
        self.Sex = None
        self.Nation = None
        self.Birth = None
        self.Address = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.Name = params.get("Name")
        self.IdCard = params.get("IdCard")
        self.Sex = params.get("Sex")
        self.Nation = params.get("Nation")
        self.Birth = params.get("Birth")
        self.Address = params.get("Address")
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
        :param Result: 認證結果碼，收費情況如下。
收費結果碼：
0: 姓名和身份證號一緻
-1: 姓名和身份證號不一緻
不收費結果碼：
-2: 非法身份證號（長度、校驗位等不正确）
-3: 非法姓名（長度、格式等不正确）
-4: 證件庫服務異常
-5: 證件庫中無此身份證記錄
        :type Result: str
        :param Description: 業務結果描述。
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
        :param Description: 業務結果描述。
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
        :param Description: 業務結果描述。
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
        :param Description: 業務結果描述。
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


class LivenessRequest(AbstractModel):
    """Liveness請求參數結構體

    """

    def __init__(self):
        """
        :param VideoBase64: 用於活體檢測的視訊，視訊的BASE64值；
BASE64編碼後的大小不超過5M，支援mp4、avi、flv格式。
        :type VideoBase64: str
        :param LivenessType: 活體檢測類型，取值：LIP/ACTION/SILENT。
LIP爲數字模式，ACTION爲動作模式，SILENT爲靜默模式，三種模式選擇一種傳入。
        :type LivenessType: str
        :param ValidateData: 數字模式傳參：數字驗證碼(1234)，需先調用介面獲取數字驗證碼；
動作模式傳參：傳動作順序(2,1 or 1,2)，需先調用介面獲取動作順序；
靜默模式傳參：不需要傳遞此參數。
        :type ValidateData: str
        :param Optional: 本介面不需要傳遞此參數。
        :type Optional: str
        """
        self.VideoBase64 = None
        self.LivenessType = None
        self.ValidateData = None
        self.Optional = None


    def _deserialize(self, params):
        self.VideoBase64 = params.get("VideoBase64")
        self.LivenessType = params.get("LivenessType")
        self.ValidateData = params.get("ValidateData")
        self.Optional = params.get("Optional")


class LivenessResponse(AbstractModel):
    """Liveness返回參數結構體

    """

    def __init__(self):
        """
        :param BestFrameBase64: 驗證通過後的視訊最佳截圖照片，照片爲BASE64編碼後的值，jpg格式。
        :type BestFrameBase64: str
        :param Result: 業務錯誤碼，成功情況返回Success, 錯誤情況請參考下方錯誤碼 清單中FailedOperation部分
        :type Result: str
        :param Description: 業務結果描述。
        :type Description: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.BestFrameBase64 = None
        self.Result = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BestFrameBase64 = params.get("BestFrameBase64")
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class MinorsVerificationRequest(AbstractModel):
    """MinorsVerification請求參數結構體

    """

    def __init__(self):
        """
        :param Type: 參與校驗的參數類型。
0：使用手機號進行校驗；
1：使用姓名與身份證號進行校驗。
        :type Type: str
        :param Mobile: 手機號，11位數字，
特别提示：
手機號驗證只限制在 健康守護可信模型函蓋的數據範圍内，與手機號本身在運營商是否實名無關聯，不在範圍會提示“手機號未實名”，建議客戶與傳入姓名和身份證號訊息組合使用。
        :type Mobile: str
        :param IdCard: 身份證號碼。
        :type IdCard: str
        :param Name: 姓名。
        :type Name: str
        """
        self.Type = None
        self.Mobile = None
        self.IdCard = None
        self.Name = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Mobile = params.get("Mobile")
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")


class MinorsVerificationResponse(AbstractModel):
    """MinorsVerification返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 結果碼，收費情況如下。
收費結果碼：
0: 成年
-1: 未成年
-2: 手機號未實名
-3: 姓名和身份證號不一緻

不收費結果碼：
-4: 非法身份證號（長度、校驗位等不正确）
-5: 非法姓名（長度、格式等不正确）
-6: 數據源服務異常
-7: 數據源中無此身份證記錄
-8: 警察比對系統升級中，請稍後再試
        :type Result: str
        :param Description: 業務結果描述。
        :type Description: str
        :param AgeRange: 當結果碼爲0或者-1時，該欄位的值爲年齡區間。
格式爲[a,b)，表示年齡在a歲以上（包括a歲），b歲以下（不包括b歲）。若b爲+時表示沒有上限。
        :type AgeRange: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.AgeRange = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.AgeRange = params.get("AgeRange")
        self.RequestId = params.get("RequestId")


class MobileNetworkTimeVerificationRequest(AbstractModel):
    """MobileNetworkTimeVerification請求參數結構體

    """

    def __init__(self):
        """
        :param Mobile: 手機號碼。不支援電信手機號。
        :type Mobile: str
        """
        self.Mobile = None


    def _deserialize(self, params):
        self.Mobile = params.get("Mobile")


class MobileNetworkTimeVerificationResponse(AbstractModel):
    """MobileNetworkTimeVerification返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 認證結果碼，收費情況如下。
收費結果碼：
0: 成功
-2: 手機號不存在
-3: 手機號存在，但無法查詢到在網時長
不收費結果碼：
-1: 手機號格式不正确
-4: 驗證中心服務繁忙
        :type Result: str
        :param Description: 業務結果描述。
        :type Description: str
        :param Range: 在網時長區間。
格式爲(a,b]，表示在網時長在a個月以上，b個月以下。若b爲+時表示沒有上限。
        :type Range: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.Range = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.Range = params.get("Range")
        self.RequestId = params.get("RequestId")


class MobileStatusRequest(AbstractModel):
    """MobileStatus請求參數結構體

    """

    def __init__(self):
        """
        :param Mobile: 手機號碼
        :type Mobile: str
        """
        self.Mobile = None


    def _deserialize(self, params):
        self.Mobile = params.get("Mobile")


class MobileStatusResponse(AbstractModel):
    """MobileStatus返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 認證結果碼，收費情況如下。
收費結果碼：
0：成功
不收費結果碼：
-1：未查詢到結果
-2：手機號格式不正确
-3：驗證中心服務繁忙
        :type Result: str
        :param Description: 業務結果描述。
        :type Description: str
        :param StatusCode: 狀态碼：
0：正常
1：停機
2：銷號
3：空號
4：不在網
99：未知狀态
        :type StatusCode: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.Description = None
        self.StatusCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.Description = params.get("Description")
        self.StatusCode = params.get("StatusCode")
        self.RequestId = params.get("RequestId")


class PhoneVerificationRequest(AbstractModel):
    """PhoneVerification請求參數結構體

    """

    def __init__(self):
        """
        :param IdCard: 身份證號
        :type IdCard: str
        :param Name: 姓名
        :type Name: str
        :param Phone: 手機號
        :type Phone: str
        """
        self.IdCard = None
        self.Name = None
        self.Phone = None


    def _deserialize(self, params):
        self.IdCard = params.get("IdCard")
        self.Name = params.get("Name")
        self.Phone = params.get("Phone")


class PhoneVerificationResponse(AbstractModel):
    """PhoneVerification返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 認證結果碼:
0: 認證通過
-1: 手機號已實名，但是身份證和姓名均與實名訊息不一緻 
-2: 手機號已實名，手機號和證件號一緻，姓名不一緻
-3: 手機號已實名，手機號和姓名一緻，身份證不一緻
-4: 訊息不一緻
-5: 手機號未實名
-6: 手機號碼不合法
-7: 身份證號碼有誤
-8: 姓名校驗不通過
-9: 沒有記錄
-10: 認證未通過
-11: 驗證中心服務繁忙
        :type Result: str
        :param Description: 業務結果描述。
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