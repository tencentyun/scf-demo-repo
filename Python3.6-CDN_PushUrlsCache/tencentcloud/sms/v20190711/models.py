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


class AddSignStatus(AbstractModel):
    """添加簽名響應

    """

    def __init__(self):
        """
        :param SignId: 簽名Id。
        :type SignId: int
        :param SignApplyId: 簽名申請Id。
        :type SignApplyId: int
        """
        self.SignId = None
        self.SignApplyId = None


    def _deserialize(self, params):
        self.SignId = params.get("SignId")
        self.SignApplyId = params.get("SignApplyId")


class AddSmsSignRequest(AbstractModel):
    """AddSmsSign請求參數結構體

    """

    def __init__(self):
        """
        :param SignName: 簽名名稱。
        :type SignName: str
        :param SignType: 簽名類型。其中每種類型後面标注了其可選的 DocumentType（證明類型）：
0：公司（0，1，2，3）。
1：APP（0，1，2，3，4） 。
2：網站（0，1，2，3，5）。
3：公衆号或者小程式（0，1，2，3，6）。
4：商标（7）。
5：政府/機關事業單位/其他機構（2，3）。
注：必須按照對應關系選擇證明類型，否則會審核失敗。
        :type SignType: int
        :param DocumentType: 證明類型：
0：三證合一。
1：企業營業執照。
2：組織機構代碼證書。
3：社會信用代碼證書。
4：應用後台管理截圖（個人開發APP）。
5：網站備案後台截圖（個人開發網站）。
6：小程式設置頁面截圖（個人認證小程式）。
7：商标注冊書。
        :type DocumentType: int
        :param International: 是否國際/ 簡訊：
0：表示國内簡訊。
1：表示國際/ 簡訊。
        :type International: int
        :param UsedMethod: 簽名用途：
0：自用。
1：他用。
        :type UsedMethod: int
        :param ProofImage: 簽名對應的資質證明圖片需先進行 base64 編碼格式轉換，将轉換後的字串去掉前綴`data:image/jpeg;base64,`再賦值給該參數。
        :type ProofImage: str
        :param CommissionImage: 委托授權證明。選擇 UsedMethod 爲他用之後需要提交委托的授權證明。
圖片需先進行 base64 編碼格式轉換，将轉換後的字串去掉前綴`data:image/jpeg;base64,`再賦值給該參數。
注：只有 UsedMethod 在選擇爲 1（他用）時，這個欄位才會生效。
        :type CommissionImage: str
        :param Remark: 簽名的申請備注。
        :type Remark: str
        """
        self.SignName = None
        self.SignType = None
        self.DocumentType = None
        self.International = None
        self.UsedMethod = None
        self.ProofImage = None
        self.CommissionImage = None
        self.Remark = None


    def _deserialize(self, params):
        self.SignName = params.get("SignName")
        self.SignType = params.get("SignType")
        self.DocumentType = params.get("DocumentType")
        self.International = params.get("International")
        self.UsedMethod = params.get("UsedMethod")
        self.ProofImage = params.get("ProofImage")
        self.CommissionImage = params.get("CommissionImage")
        self.Remark = params.get("Remark")


class AddSmsSignResponse(AbstractModel):
    """AddSmsSign返回參數結構體

    """

    def __init__(self):
        """
        :param AddSignStatus: 添加簽名響應
        :type AddSignStatus: :class:`taifucloudcloud.sms.v20190711.models.AddSignStatus`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AddSignStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AddSignStatus") is not None:
            self.AddSignStatus = AddSignStatus()
            self.AddSignStatus._deserialize(params.get("AddSignStatus"))
        self.RequestId = params.get("RequestId")


class AddSmsTemplateRequest(AbstractModel):
    """AddSmsTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param TemplateName: 範本名稱。
        :type TemplateName: str
        :param TemplateContent: 範本内容。
        :type TemplateContent: str
        :param SmsType: 簡訊類型，0表示普通簡訊, 1表示營銷簡訊。
        :type SmsType: int
        :param International: 是否國際/ 簡訊：
0：表示國内簡訊。
1：表示國際/ 簡訊。
        :type International: int
        :param Remark: 範本備注，例如申請原因，使用場景等。
        :type Remark: str
        """
        self.TemplateName = None
        self.TemplateContent = None
        self.SmsType = None
        self.International = None
        self.Remark = None


    def _deserialize(self, params):
        self.TemplateName = params.get("TemplateName")
        self.TemplateContent = params.get("TemplateContent")
        self.SmsType = params.get("SmsType")
        self.International = params.get("International")
        self.Remark = params.get("Remark")


class AddSmsTemplateResponse(AbstractModel):
    """AddSmsTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param AddTemplateStatus: 添加簡訊範本響應包體
        :type AddTemplateStatus: :class:`taifucloudcloud.sms.v20190711.models.AddTemplateStatus`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AddTemplateStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AddTemplateStatus") is not None:
            self.AddTemplateStatus = AddTemplateStatus()
            self.AddTemplateStatus._deserialize(params.get("AddTemplateStatus"))
        self.RequestId = params.get("RequestId")


class AddTemplateStatus(AbstractModel):
    """添加範本參數響應

    """

    def __init__(self):
        """
        :param TemplateId: 範本參數
        :type TemplateId: str
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


class CallbackStatusStatistics(AbstractModel):
    """回執數據統計響應包體

    """

    def __init__(self):
        """
        :param CallbackCount: 簡訊回執量統計。
        :type CallbackCount: int
        :param RequestSuccessCount: 簡訊提交成功量統計。
        :type RequestSuccessCount: int
        :param CallbackFailCount: 簡訊回執失敗量統計。
        :type CallbackFailCount: int
        :param CallbackSuccessCount: 簡訊回執成功量統計。
        :type CallbackSuccessCount: int
        :param InternalErrorCount: 運營商内部錯誤統計。
        :type InternalErrorCount: int
        :param InvalidNumberCount: 号碼無效或空号統計。
        :type InvalidNumberCount: int
        :param ShutdownErrorCount: 停機、關機等錯誤統計。
        :type ShutdownErrorCount: int
        :param BlackListCount: 号碼拉入黑名單統計。
        :type BlackListCount: int
        :param FrequencyLimitCount: 運營商頻率限制統計。
        :type FrequencyLimitCount: int
        """
        self.CallbackCount = None
        self.RequestSuccessCount = None
        self.CallbackFailCount = None
        self.CallbackSuccessCount = None
        self.InternalErrorCount = None
        self.InvalidNumberCount = None
        self.ShutdownErrorCount = None
        self.BlackListCount = None
        self.FrequencyLimitCount = None


    def _deserialize(self, params):
        self.CallbackCount = params.get("CallbackCount")
        self.RequestSuccessCount = params.get("RequestSuccessCount")
        self.CallbackFailCount = params.get("CallbackFailCount")
        self.CallbackSuccessCount = params.get("CallbackSuccessCount")
        self.InternalErrorCount = params.get("InternalErrorCount")
        self.InvalidNumberCount = params.get("InvalidNumberCount")
        self.ShutdownErrorCount = params.get("ShutdownErrorCount")
        self.BlackListCount = params.get("BlackListCount")
        self.FrequencyLimitCount = params.get("FrequencyLimitCount")


class CallbackStatusStatisticsRequest(AbstractModel):
    """CallbackStatusStatistics請求參數結構體

    """

    def __init__(self):
        """
        :param StartDateTime: 開始時間，yyyymmddhh 需要拉取的起始時間，精确到小時。
        :type StartDateTime: int
        :param EndDataTime: 結束時間，yyyymmddhh 需要拉取的截止時間，精确到小時。
注：EndDataTime 必須大于 StartDateTime。
        :type EndDataTime: int
        :param SmsSdkAppid: 簡訊SdkAppid在 [簡訊控制台](https://console.cloud.taifucloud.com/sms/smslist) 添加應用後生成的實際SdkAppid，範例如1400006666。
        :type SmsSdkAppid: str
        :param Limit: 最大上限。
注：目前固定設置爲0。
        :type Limit: int
        :param Offset: 偏移量。
注：目前固定設置爲0。
        :type Offset: int
        """
        self.StartDateTime = None
        self.EndDataTime = None
        self.SmsSdkAppid = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.StartDateTime = params.get("StartDateTime")
        self.EndDataTime = params.get("EndDataTime")
        self.SmsSdkAppid = params.get("SmsSdkAppid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class CallbackStatusStatisticsResponse(AbstractModel):
    """CallbackStatusStatistics返回參數結構體

    """

    def __init__(self):
        """
        :param CallbackStatusStatistics: 回執數據統計響應包體。
        :type CallbackStatusStatistics: :class:`taifucloudcloud.sms.v20190711.models.CallbackStatusStatistics`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CallbackStatusStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CallbackStatusStatistics") is not None:
            self.CallbackStatusStatistics = CallbackStatusStatistics()
            self.CallbackStatusStatistics._deserialize(params.get("CallbackStatusStatistics"))
        self.RequestId = params.get("RequestId")


class DeleteSignStatus(AbstractModel):
    """删除簽名響應

    """

    def __init__(self):
        """
        :param DeleteStatus: 删除狀态訊息。
        :type DeleteStatus: str
        :param DeleteTime: 删除時間，UNIX 時間戳（單位：秒）。
        :type DeleteTime: int
        """
        self.DeleteStatus = None
        self.DeleteTime = None


    def _deserialize(self, params):
        self.DeleteStatus = params.get("DeleteStatus")
        self.DeleteTime = params.get("DeleteTime")


class DeleteSmsSignRequest(AbstractModel):
    """DeleteSmsSign請求參數結構體

    """

    def __init__(self):
        """
        :param SignId: 待删除的簽名 ID。
        :type SignId: int
        """
        self.SignId = None


    def _deserialize(self, params):
        self.SignId = params.get("SignId")


class DeleteSmsSignResponse(AbstractModel):
    """DeleteSmsSign返回參數結構體

    """

    def __init__(self):
        """
        :param DeleteSignStatus: 删除簽名響應
        :type DeleteSignStatus: :class:`taifucloudcloud.sms.v20190711.models.DeleteSignStatus`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DeleteSignStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeleteSignStatus") is not None:
            self.DeleteSignStatus = DeleteSignStatus()
            self.DeleteSignStatus._deserialize(params.get("DeleteSignStatus"))
        self.RequestId = params.get("RequestId")


class DeleteSmsTemplateRequest(AbstractModel):
    """DeleteSmsTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param TemplateId: 待删除的範本 ID。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


class DeleteSmsTemplateResponse(AbstractModel):
    """DeleteSmsTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param DeleteTemplateStatus: 删除範本響應
        :type DeleteTemplateStatus: :class:`taifucloudcloud.sms.v20190711.models.DeleteTemplateStatus`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DeleteTemplateStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeleteTemplateStatus") is not None:
            self.DeleteTemplateStatus = DeleteTemplateStatus()
            self.DeleteTemplateStatus._deserialize(params.get("DeleteTemplateStatus"))
        self.RequestId = params.get("RequestId")


class DeleteTemplateStatus(AbstractModel):
    """删除範本響應

    """

    def __init__(self):
        """
        :param DeleteStatus: 删除狀态訊息。
        :type DeleteStatus: str
        :param DeleteTime: 删除時間，UNIX 時間戳（單位：秒）。
        :type DeleteTime: int
        """
        self.DeleteStatus = None
        self.DeleteTime = None


    def _deserialize(self, params):
        self.DeleteStatus = params.get("DeleteStatus")
        self.DeleteTime = params.get("DeleteTime")


class DescribeSignListStatus(AbstractModel):
    """獲取簡訊簽名訊息響應

    """

    def __init__(self):
        """
        :param SignId: 簽名Id
        :type SignId: int
        :param International: 是否國際/ 簡訊：
0：表示國内簡訊。
1：表示國際/ 簡訊。
        :type International: int
        :param StatusCode: 申請簽名狀态。其中：
0：表示審核通過。
-1：表示審核未通過或審核失敗。
        :type StatusCode: int
        :param ReviewReply: 審核回複，審核人員審核後給出的回複，通常是審核未通過的原因。
        :type ReviewReply: str
        :param SignName: 簽名名稱。
        :type SignName: str
        :param CreateTime: 提交審核時間，UNIX 時間戳（單位：秒）。
        :type CreateTime: int
        """
        self.SignId = None
        self.International = None
        self.StatusCode = None
        self.ReviewReply = None
        self.SignName = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.SignId = params.get("SignId")
        self.International = params.get("International")
        self.StatusCode = params.get("StatusCode")
        self.ReviewReply = params.get("ReviewReply")
        self.SignName = params.get("SignName")
        self.CreateTime = params.get("CreateTime")


class DescribeSmsSignListRequest(AbstractModel):
    """DescribeSmsSignList請求參數結構體

    """

    def __init__(self):
        """
        :param SignIdSet: 簽名 ID 數組。
        :type SignIdSet: list of int non-negative
        :param International: 是否國際/ 簡訊：
0：表示國内簡訊。
1：表示國際/ 簡訊。
        :type International: int
        """
        self.SignIdSet = None
        self.International = None


    def _deserialize(self, params):
        self.SignIdSet = params.get("SignIdSet")
        self.International = params.get("International")


class DescribeSmsSignListResponse(AbstractModel):
    """DescribeSmsSignList返回參數結構體

    """

    def __init__(self):
        """
        :param DescribeSignListStatusSet: 獲取簽名訊息響應
        :type DescribeSignListStatusSet: list of DescribeSignListStatus
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DescribeSignListStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DescribeSignListStatusSet") is not None:
            self.DescribeSignListStatusSet = []
            for item in params.get("DescribeSignListStatusSet"):
                obj = DescribeSignListStatus()
                obj._deserialize(item)
                self.DescribeSignListStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSmsTemplateListRequest(AbstractModel):
    """DescribeSmsTemplateList請求參數結構體

    """

    def __init__(self):
        """
        :param TemplateIdSet: 範本 ID 數組。
        :type TemplateIdSet: list of int non-negative
        :param International: 是否國際/ 簡訊：
0：表示國内簡訊。
1：表示國際/ 簡訊。
        :type International: int
        """
        self.TemplateIdSet = None
        self.International = None


    def _deserialize(self, params):
        self.TemplateIdSet = params.get("TemplateIdSet")
        self.International = params.get("International")


class DescribeSmsTemplateListResponse(AbstractModel):
    """DescribeSmsTemplateList返回參數結構體

    """

    def __init__(self):
        """
        :param DescribeTemplateStatusSet: 獲取簡訊簽名訊息響應
        :type DescribeTemplateStatusSet: list of DescribeTemplateListStatus
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DescribeTemplateStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DescribeTemplateStatusSet") is not None:
            self.DescribeTemplateStatusSet = []
            for item in params.get("DescribeTemplateStatusSet"):
                obj = DescribeTemplateListStatus()
                obj._deserialize(item)
                self.DescribeTemplateStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTemplateListStatus(AbstractModel):
    """獲取簡訊範本訊息響應

    """

    def __init__(self):
        """
        :param TemplateId: 範本Id
        :type TemplateId: int
        :param International: 是否國際/ 簡訊：
0：表示國内簡訊。
1：表示國際/ 簡訊。
        :type International: int
        :param StatusCode: 申請簽名狀态。其中：
0：表示審核通過。
-1：表示審核未通過或審核失敗。
        :type StatusCode: int
        :param ReviewReply: 審核回複，審核人員審核後給出的回複，通常是審核未通過的原因。
        :type ReviewReply: str
        :param TemplateName: 範本名稱。
        :type TemplateName: str
        :param CreateTime: 提交審核時間，UNIX 時間戳（單位：秒）。
        :type CreateTime: int
        """
        self.TemplateId = None
        self.International = None
        self.StatusCode = None
        self.ReviewReply = None
        self.TemplateName = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.International = params.get("International")
        self.StatusCode = params.get("StatusCode")
        self.ReviewReply = params.get("ReviewReply")
        self.TemplateName = params.get("TemplateName")
        self.CreateTime = params.get("CreateTime")


class ModifySignStatus(AbstractModel):
    """修改簽名響應

    """

    def __init__(self):
        """
        :param SignId: 簽名Id
        :type SignId: int
        :param SignApplyId: 簽名修改申請Id
        :type SignApplyId: str
        """
        self.SignId = None
        self.SignApplyId = None


    def _deserialize(self, params):
        self.SignId = params.get("SignId")
        self.SignApplyId = params.get("SignApplyId")


class ModifySmsSignRequest(AbstractModel):
    """ModifySmsSign請求參數結構體

    """

    def __init__(self):
        """
        :param SignId: 待修改的簽名 ID。
        :type SignId: int
        :param SignName: 簽名名稱。
        :type SignName: str
        :param SignType: 簽名類型。其中每種類型後面标注了其可選的 DocumentType（證明類型）：
0：公司（0，1，2，3）。
1：APP（0，1，2，3，4） 。
2：網站（0，1，2，3，5）。
3：公衆号或者小程式（0，1，2，3，6）。
4：商标（7）。
5：政府/機關事業單位/其他機構（2，3）。
注：必須按照對應關系選擇證明類型，否則會審核失敗。
        :type SignType: int
        :param DocumentType: 證明類型：
0：三證合一。
1：企業營業執照。
2：組織機構代碼證書。
3：社會信用代碼證書。
4：應用後台管理截圖(個人開發APP)。
5：網站備案後台截圖(個人開發網站)。
6：小程式設置頁面截圖(個人認證小程式)。
7：商标注冊書。
        :type DocumentType: int
        :param International: 是否國際/ 簡訊：
0：表示國内簡訊。
1：表示國際/ 簡訊。
        :type International: int
        :param UsedMethod: 簽名用途：
0：自用。
1：他用。
        :type UsedMethod: int
        :param ProofImage: 簽名對應的資質證明圖片需先進行 base64 編碼格式轉換，将轉換後的字串去掉前綴`data:image/jpeg;base64,`再賦值給該參數。
        :type ProofImage: str
        :param CommissionImage: 委托授權證明。選擇 UsedMethod 爲他用之後需要提交委托的授權證明。
圖片需先進行 base64 編碼格式轉換，将轉換後的字串去掉前綴`data:image/jpeg;base64,`再賦值給該參數。
注：只有 UsedMethod 在選擇爲 1（他用）時，這個欄位才會生效。
        :type CommissionImage: str
        :param Remark: 簽名的申請備注。
        :type Remark: str
        """
        self.SignId = None
        self.SignName = None
        self.SignType = None
        self.DocumentType = None
        self.International = None
        self.UsedMethod = None
        self.ProofImage = None
        self.CommissionImage = None
        self.Remark = None


    def _deserialize(self, params):
        self.SignId = params.get("SignId")
        self.SignName = params.get("SignName")
        self.SignType = params.get("SignType")
        self.DocumentType = params.get("DocumentType")
        self.International = params.get("International")
        self.UsedMethod = params.get("UsedMethod")
        self.ProofImage = params.get("ProofImage")
        self.CommissionImage = params.get("CommissionImage")
        self.Remark = params.get("Remark")


class ModifySmsSignResponse(AbstractModel):
    """ModifySmsSign返回參數結構體

    """

    def __init__(self):
        """
        :param ModifySignStatus: 修改簽名響應
        :type ModifySignStatus: :class:`taifucloudcloud.sms.v20190711.models.ModifySignStatus`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ModifySignStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ModifySignStatus") is not None:
            self.ModifySignStatus = ModifySignStatus()
            self.ModifySignStatus._deserialize(params.get("ModifySignStatus"))
        self.RequestId = params.get("RequestId")


class ModifySmsTemplateRequest(AbstractModel):
    """ModifySmsTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param TemplateId: 待修改的範本的範本 ID。
        :type TemplateId: int
        :param TemplateName: 新的範本名稱。
        :type TemplateName: str
        :param TemplateContent: 新的範本内容。
        :type TemplateContent: str
        :param SmsType: 簡訊類型，0表示普通簡訊, 1表示營銷簡訊。
        :type SmsType: int
        :param International: 是否國際/ 簡訊：
0：表示國内簡訊。
1：表示國際/ 簡訊。
        :type International: int
        :param Remark: 範本備注，例如申請原因，使用場景等。
        :type Remark: str
        """
        self.TemplateId = None
        self.TemplateName = None
        self.TemplateContent = None
        self.SmsType = None
        self.International = None
        self.Remark = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.TemplateContent = params.get("TemplateContent")
        self.SmsType = params.get("SmsType")
        self.International = params.get("International")
        self.Remark = params.get("Remark")


class ModifySmsTemplateResponse(AbstractModel):
    """ModifySmsTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param ModifyTemplateStatus: 修改範本參數響應
        :type ModifyTemplateStatus: :class:`taifucloudcloud.sms.v20190711.models.ModifyTemplateStatus`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ModifyTemplateStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ModifyTemplateStatus") is not None:
            self.ModifyTemplateStatus = ModifyTemplateStatus()
            self.ModifyTemplateStatus._deserialize(params.get("ModifyTemplateStatus"))
        self.RequestId = params.get("RequestId")


class ModifyTemplateStatus(AbstractModel):
    """修改範本參數響應

    """

    def __init__(self):
        """
        :param TemplateId: 範本參數
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


class PullSmsReplyStatus(AbstractModel):
    """簡訊回複狀态

    """

    def __init__(self):
        """
        :param ExtendCode: 簡訊碼号擴展号，預設未開通，如需開通請聯系 [sms helper](https://cloud.taifucloud.com/document/product/382/3773)。
        :type ExtendCode: str
        :param NationCode: 國家（或地區）碼。
        :type NationCode: str
        :param PhoneNumber: 手機号碼,e.164标準，+[國家或地區碼][手機号] ，範例如：+8613711112222， 其中前面有一個+号 ，86爲國家碼，13711112222爲手機号。
        :type PhoneNumber: str
        :param Sign: 簡訊簽名。
        :type Sign: str
        :param ReplyContent: 用戶回複的内容。
        :type ReplyContent: str
        :param ReplyTime: 回複時間（例如：2019-10-08 17:18:37）。
        :type ReplyTime: str
        :param ReplyUnixTime: 回複時間，UNIX 時間戳（單位：秒）。
        :type ReplyUnixTime: int
        """
        self.ExtendCode = None
        self.NationCode = None
        self.PhoneNumber = None
        self.Sign = None
        self.ReplyContent = None
        self.ReplyTime = None
        self.ReplyUnixTime = None


    def _deserialize(self, params):
        self.ExtendCode = params.get("ExtendCode")
        self.NationCode = params.get("NationCode")
        self.PhoneNumber = params.get("PhoneNumber")
        self.Sign = params.get("Sign")
        self.ReplyContent = params.get("ReplyContent")
        self.ReplyTime = params.get("ReplyTime")
        self.ReplyUnixTime = params.get("ReplyUnixTime")


class PullSmsReplyStatusByPhoneNumberRequest(AbstractModel):
    """PullSmsReplyStatusByPhoneNumber請求參數結構體

    """

    def __init__(self):
        """
        :param SendDateTime: 拉取起始時間，UNIX 時間戳（時間：秒）。
        :type SendDateTime: int
        :param Offset: 偏移量。
注：目前固定設置爲0。
        :type Offset: int
        :param Limit: 拉取最大條數，最多 100。
        :type Limit: int
        :param PhoneNumber: 下發目的手機号碼，依據 e.164 标準爲：+[國家（或地區）碼][手機号] ，範例如：+8613711112222， 其中前面有一個+号 ，86爲國家碼，13711112222爲手機号。
        :type PhoneNumber: str
        :param SmsSdkAppid: 簡訊SdkAppid在 [簡訊控制台](https://console.cloud.taifucloud.com/sms/smslist) 添加應用後生成的實際SdkAppid，例如1400006666。
        :type SmsSdkAppid: str
        """
        self.SendDateTime = None
        self.Offset = None
        self.Limit = None
        self.PhoneNumber = None
        self.SmsSdkAppid = None


    def _deserialize(self, params):
        self.SendDateTime = params.get("SendDateTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PhoneNumber = params.get("PhoneNumber")
        self.SmsSdkAppid = params.get("SmsSdkAppid")


class PullSmsReplyStatusByPhoneNumberResponse(AbstractModel):
    """PullSmsReplyStatusByPhoneNumber返回參數結構體

    """

    def __init__(self):
        """
        :param PullSmsReplyStatusSet: 回複狀态響應集合。
        :type PullSmsReplyStatusSet: list of PullSmsReplyStatus
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PullSmsReplyStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PullSmsReplyStatusSet") is not None:
            self.PullSmsReplyStatusSet = []
            for item in params.get("PullSmsReplyStatusSet"):
                obj = PullSmsReplyStatus()
                obj._deserialize(item)
                self.PullSmsReplyStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class PullSmsReplyStatusRequest(AbstractModel):
    """PullSmsReplyStatus請求參數結構體

    """

    def __init__(self):
        """
        :param Limit: 拉取最大條數，最多100條。
        :type Limit: int
        :param SmsSdkAppid: 簡訊 SdkAppid 在 [簡訊控制台](https://console.cloud.taifucloud.com/sms/smslist) 添加應用後生成的實際 SdkAppid，例如1400006666。
        :type SmsSdkAppid: str
        """
        self.Limit = None
        self.SmsSdkAppid = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.SmsSdkAppid = params.get("SmsSdkAppid")


class PullSmsReplyStatusResponse(AbstractModel):
    """PullSmsReplyStatus返回參數結構體

    """

    def __init__(self):
        """
        :param PullSmsReplyStatusSet: 回複狀态響應集合。
        :type PullSmsReplyStatusSet: list of PullSmsReplyStatus
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PullSmsReplyStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PullSmsReplyStatusSet") is not None:
            self.PullSmsReplyStatusSet = []
            for item in params.get("PullSmsReplyStatusSet"):
                obj = PullSmsReplyStatus()
                obj._deserialize(item)
                self.PullSmsReplyStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class PullSmsSendStatus(AbstractModel):
    """簡訊的下發狀态詳細訊息

    """

    def __init__(self):
        """
        :param UserReceiveTime: 用戶實際接收到簡訊的時間。
        :type UserReceiveTime: str
        :param UserReceiveUnixTime: 用戶實際接收到簡訊的時間，UNIX 時間戳（單位：秒）。
        :type UserReceiveUnixTime: int
        :param NationCode: 國家（或地區）碼。
        :type NationCode: str
        :param PurePhoneNumber: 手機号碼,e.164标準，+[國家或地區碼][手機号] ，範例如：+8613711112222， 其中前面有一個+号 ，86爲國家碼，13711112222爲手機号。
        :type PurePhoneNumber: str
        :param PhoneNumber: 手機号碼，普通格式，範例如：13711112222。
        :type PhoneNumber: str
        :param SerialNo: 本次發送标識 ID。
        :type SerialNo: str
        :param ReportStatus: 實際是否收到簡訊接收狀态，SUCCESS（成功）、FAIL（失敗）。
        :type ReportStatus: str
        :param Description: 用戶接收簡訊狀态描述。
        :type Description: str
        """
        self.UserReceiveTime = None
        self.UserReceiveUnixTime = None
        self.NationCode = None
        self.PurePhoneNumber = None
        self.PhoneNumber = None
        self.SerialNo = None
        self.ReportStatus = None
        self.Description = None


    def _deserialize(self, params):
        self.UserReceiveTime = params.get("UserReceiveTime")
        self.UserReceiveUnixTime = params.get("UserReceiveUnixTime")
        self.NationCode = params.get("NationCode")
        self.PurePhoneNumber = params.get("PurePhoneNumber")
        self.PhoneNumber = params.get("PhoneNumber")
        self.SerialNo = params.get("SerialNo")
        self.ReportStatus = params.get("ReportStatus")
        self.Description = params.get("Description")


class PullSmsSendStatusByPhoneNumberRequest(AbstractModel):
    """PullSmsSendStatusByPhoneNumber請求參數結構體

    """

    def __init__(self):
        """
        :param SendDateTime: 拉取起始時間，UNIX 時間戳（時間：秒）。
        :type SendDateTime: int
        :param Offset: 偏移量。
注：目前固定設置爲0。
        :type Offset: int
        :param Limit: 拉取最大條數，最多 100。
        :type Limit: int
        :param PhoneNumber: 下發目的手機号碼，依據 e.164 标準爲：+[國家（或地區）碼][手機号] ，範例如：+8613711112222， 其中前面有一個+号 ，86爲國家碼，13711112222爲手機号。
        :type PhoneNumber: str
        :param SmsSdkAppid: 簡訊SdkAppid在 [簡訊控制台](https://console.cloud.taifucloud.com/sms/smslist) 添加應用後生成的實際SdkAppid，例如1400006666。
        :type SmsSdkAppid: str
        """
        self.SendDateTime = None
        self.Offset = None
        self.Limit = None
        self.PhoneNumber = None
        self.SmsSdkAppid = None


    def _deserialize(self, params):
        self.SendDateTime = params.get("SendDateTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PhoneNumber = params.get("PhoneNumber")
        self.SmsSdkAppid = params.get("SmsSdkAppid")


class PullSmsSendStatusByPhoneNumberResponse(AbstractModel):
    """PullSmsSendStatusByPhoneNumber返回參數結構體

    """

    def __init__(self):
        """
        :param PullSmsSendStatusSet: 下發狀态響應集合。
        :type PullSmsSendStatusSet: list of PullSmsSendStatus
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PullSmsSendStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PullSmsSendStatusSet") is not None:
            self.PullSmsSendStatusSet = []
            for item in params.get("PullSmsSendStatusSet"):
                obj = PullSmsSendStatus()
                obj._deserialize(item)
                self.PullSmsSendStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class PullSmsSendStatusRequest(AbstractModel):
    """PullSmsSendStatus請求參數結構體

    """

    def __init__(self):
        """
        :param Limit: 拉取最大條數，最多100條。
        :type Limit: int
        :param SmsSdkAppid: 簡訊SdkAppid在 [簡訊控制台](https://console.cloud.taifucloud.com/sms/smslist) 添加應用後生成的實際SdkAppid，例如1400006666。
        :type SmsSdkAppid: str
        """
        self.Limit = None
        self.SmsSdkAppid = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.SmsSdkAppid = params.get("SmsSdkAppid")


class PullSmsSendStatusResponse(AbstractModel):
    """PullSmsSendStatus返回參數結構體

    """

    def __init__(self):
        """
        :param PullSmsSendStatusSet: 下發狀态響應集合。
        :type PullSmsSendStatusSet: list of PullSmsSendStatus
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PullSmsSendStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PullSmsSendStatusSet") is not None:
            self.PullSmsSendStatusSet = []
            for item in params.get("PullSmsSendStatusSet"):
                obj = PullSmsSendStatus()
                obj._deserialize(item)
                self.PullSmsSendStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class SendSmsRequest(AbstractModel):
    """SendSms請求參數結構體

    """

    def __init__(self):
        """
        :param PhoneNumberSet: 下發手機号碼，采用 e.164 标準，格式爲+[國家或地區碼][手機号]，單次請求最多支援200個手機号且要求全爲境内手機号或全爲境外手機号。
例如：+8613711112222， 其中前面有一個+号 ，86爲國家碼，13711112222爲手機号。
        :type PhoneNumberSet: list of str
        :param TemplateID: 範本 ID，必須填寫已審核通過的範本 ID。範本ID可登入 [簡訊控制台](https://console.cloud.taifucloud.com/sms/smslist) 檢視。
        :type TemplateID: str
        :param SmsSdkAppid: 簡訊SdkAppid在 [簡訊控制台](https://console.cloud.taifucloud.com/sms/smslist)  添加應用後生成的實際SdkAppid，範例如1400006666。
        :type SmsSdkAppid: str
        :param Sign: 簡訊簽名内容，使用 UTF-8 編碼，必須填寫已審核通過的簽名，簽名訊息可登入 [簡訊控制台](https://console.cloud.taifucloud.com/sms/smslist)  檢視。注：國内簡訊爲必填參數。
        :type Sign: str
        :param TemplateParamSet: 範本參數，若無範本參數，則設置爲空。
        :type TemplateParamSet: list of str
        :param ExtendCode: 簡訊碼号擴展号，預設未開通，如需開通請聯系 [sms helper](https://cloud.taifucloud.com/document/product/382/3773)。
        :type ExtendCode: str
        :param SessionContext: 用戶的 session 内容，可以攜帶用戶側 ID 等上下文訊息，server 會原樣返回。
        :type SessionContext: str
        :param SenderId: 國際/ 簡訊 senderid，國内簡訊填空，預設未開通，如需開通請聯系 [sms helper](https://cloud.taifucloud.com/document/product/382/3773)。
        :type SenderId: str
        """
        self.PhoneNumberSet = None
        self.TemplateID = None
        self.SmsSdkAppid = None
        self.Sign = None
        self.TemplateParamSet = None
        self.ExtendCode = None
        self.SessionContext = None
        self.SenderId = None


    def _deserialize(self, params):
        self.PhoneNumberSet = params.get("PhoneNumberSet")
        self.TemplateID = params.get("TemplateID")
        self.SmsSdkAppid = params.get("SmsSdkAppid")
        self.Sign = params.get("Sign")
        self.TemplateParamSet = params.get("TemplateParamSet")
        self.ExtendCode = params.get("ExtendCode")
        self.SessionContext = params.get("SessionContext")
        self.SenderId = params.get("SenderId")


class SendSmsResponse(AbstractModel):
    """SendSms返回參數結構體

    """

    def __init__(self):
        """
        :param SendStatusSet: 簡訊發送狀态。
        :type SendStatusSet: list of SendStatus
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SendStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SendStatusSet") is not None:
            self.SendStatusSet = []
            for item in params.get("SendStatusSet"):
                obj = SendStatus()
                obj._deserialize(item)
                self.SendStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class SendStatus(AbstractModel):
    """發送簡訊狀态

    """

    def __init__(self):
        """
        :param SerialNo: 發送流水号。
        :type SerialNo: str
        :param PhoneNumber: 手機号碼,e.164标準，+[國家或地區碼][手機号] ，範例如：+8613711112222， 其中前面有一個+号 ，86爲國家碼，13711112222爲手機号。
        :type PhoneNumber: str
        :param Fee: 計費條數，計費規則請查詢 [計費策略](https://cloud.taifucloud.com/document/product/382/36135)。
        :type Fee: int
        :param SessionContext: 用戶Session内容。
        :type SessionContext: str
        :param Code: 簡訊請求錯誤碼，具體含義請參考錯誤碼。
        :type Code: str
        :param Message: 簡訊請求錯誤碼描述。
        :type Message: str
        """
        self.SerialNo = None
        self.PhoneNumber = None
        self.Fee = None
        self.SessionContext = None
        self.Code = None
        self.Message = None


    def _deserialize(self, params):
        self.SerialNo = params.get("SerialNo")
        self.PhoneNumber = params.get("PhoneNumber")
        self.Fee = params.get("Fee")
        self.SessionContext = params.get("SessionContext")
        self.Code = params.get("Code")
        self.Message = params.get("Message")


class SendStatusStatistics(AbstractModel):
    """發送數據統計響應包體

    """

    def __init__(self):
        """
        :param FeeCount: 簡訊計費條數統計，例如提交成功量爲100條，其中有20條是長簡訊（長度爲80字）被拆分成2條，則計費條數爲： ```80 * 1 + 20 * 2 = 120``` 條。
        :type FeeCount: int
        :param RequestCount: 簡訊提交量統計。
        :type RequestCount: int
        :param RequestSuccessCount: 簡訊提交成功量統計。
        :type RequestSuccessCount: int
        """
        self.FeeCount = None
        self.RequestCount = None
        self.RequestSuccessCount = None


    def _deserialize(self, params):
        self.FeeCount = params.get("FeeCount")
        self.RequestCount = params.get("RequestCount")
        self.RequestSuccessCount = params.get("RequestSuccessCount")


class SendStatusStatisticsRequest(AbstractModel):
    """SendStatusStatistics請求參數結構體

    """

    def __init__(self):
        """
        :param StartDateTime: 拉取起始時間，yyyymmddhh 需要拉取的起始時間，精确到小時。
        :type StartDateTime: int
        :param EndDataTime: 結束時間，yyyymmddhh 需要拉取的截止時間，精确到小時
注：EndDataTime 必須大于 StartDateTime。
        :type EndDataTime: int
        :param SmsSdkAppid: 簡訊SdkAppid在 [簡訊控制台](https://console.cloud.taifucloud.com/sms/smslist) 添加應用後生成的實際SdkAppid，範例如1400006666。
        :type SmsSdkAppid: str
        :param Limit: 最大上限。
注：目前固定設置爲0。
        :type Limit: int
        :param Offset: 偏移量。
注：目前固定設置爲0。
        :type Offset: int
        """
        self.StartDateTime = None
        self.EndDataTime = None
        self.SmsSdkAppid = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.StartDateTime = params.get("StartDateTime")
        self.EndDataTime = params.get("EndDataTime")
        self.SmsSdkAppid = params.get("SmsSdkAppid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class SendStatusStatisticsResponse(AbstractModel):
    """SendStatusStatistics返回參數結構體

    """

    def __init__(self):
        """
        :param SendStatusStatistics: 發送數據統計響應包體。
        :type SendStatusStatistics: :class:`taifucloudcloud.sms.v20190711.models.SendStatusStatistics`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SendStatusStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SendStatusStatistics") is not None:
            self.SendStatusStatistics = SendStatusStatistics()
            self.SendStatusStatistics._deserialize(params.get("SendStatusStatistics"))
        self.RequestId = params.get("RequestId")


class SmsPackagesStatistics(AbstractModel):
    """套餐包訊息統計響應包體

    """

    def __init__(self):
        """
        :param PackageCreateTime: 套餐包創建時間，标準時間，例如：2019-10-08 17:18:37。
        :type PackageCreateTime: str
        :param PackageCreateUnixTime: 套餐包創建時間，UNIX 時間戳（單位：秒）。
        :type PackageCreateUnixTime: int
        :param PackageEffectiveTime: 套餐包生效時間，标準時間，例如：2019-10-08 17:18:37。
        :type PackageEffectiveTime: str
        :param PackageEffectiveUnixTime: 套餐包生效時間，UNIX 時間戳（單位：秒）。
        :type PackageEffectiveUnixTime: int
        :param PackageExpiredTime: 套餐包過期時間，标準時間，例如：2019-10-08 17:18:37。
        :type PackageExpiredTime: str
        :param PackageExpiredUnixTime: 套餐包過期時間，UNIX 時間戳（單位：秒）。
        :type PackageExpiredUnixTime: int
        :param AmountOfPackage: 套餐包條數。
        :type AmountOfPackage: int
        :param TypeOfPackage: 0表示贈送套餐包，1表示購買套餐包。
        :type TypeOfPackage: int
        :param PackageId: 套餐包 ID。
        :type PackageId: int
        :param CurrentUsage: 當前使用量。
        :type CurrentUsage: int
        """
        self.PackageCreateTime = None
        self.PackageCreateUnixTime = None
        self.PackageEffectiveTime = None
        self.PackageEffectiveUnixTime = None
        self.PackageExpiredTime = None
        self.PackageExpiredUnixTime = None
        self.AmountOfPackage = None
        self.TypeOfPackage = None
        self.PackageId = None
        self.CurrentUsage = None


    def _deserialize(self, params):
        self.PackageCreateTime = params.get("PackageCreateTime")
        self.PackageCreateUnixTime = params.get("PackageCreateUnixTime")
        self.PackageEffectiveTime = params.get("PackageEffectiveTime")
        self.PackageEffectiveUnixTime = params.get("PackageEffectiveUnixTime")
        self.PackageExpiredTime = params.get("PackageExpiredTime")
        self.PackageExpiredUnixTime = params.get("PackageExpiredUnixTime")
        self.AmountOfPackage = params.get("AmountOfPackage")
        self.TypeOfPackage = params.get("TypeOfPackage")
        self.PackageId = params.get("PackageId")
        self.CurrentUsage = params.get("CurrentUsage")


class SmsPackagesStatisticsRequest(AbstractModel):
    """SmsPackagesStatistics請求參數結構體

    """

    def __init__(self):
        """
        :param SmsSdkAppid: 簡訊SdkAppid在 [簡訊控制台](https://console.cloud.taifucloud.com/sms/smslist) 添加應用後生成的實際SdkAppid，範例如1400006666。
        :type SmsSdkAppid: str
        :param Limit: 最大上限(需要拉取的套餐包個數)。
        :type Limit: int
        :param Offset: 偏移量。
注：目前固定設置爲0。
        :type Offset: int
        """
        self.SmsSdkAppid = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.SmsSdkAppid = params.get("SmsSdkAppid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class SmsPackagesStatisticsResponse(AbstractModel):
    """SmsPackagesStatistics返回參數結構體

    """

    def __init__(self):
        """
        :param SmsPackagesStatisticsSet: 發送數據統計響應包體。
        :type SmsPackagesStatisticsSet: list of SmsPackagesStatistics
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SmsPackagesStatisticsSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SmsPackagesStatisticsSet") is not None:
            self.SmsPackagesStatisticsSet = []
            for item in params.get("SmsPackagesStatisticsSet"):
                obj = SmsPackagesStatistics()
                obj._deserialize(item)
                self.SmsPackagesStatisticsSet.append(obj)
        self.RequestId = params.get("RequestId")