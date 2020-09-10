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


class AttributeKeyDetail(AbstractModel):
    """AttributeKey值詳情

    """

    def __init__(self):
        """
        :param Label: 中文标簽
        :type Label: str
        :param LabelType: 輸入框類型
        :type LabelType: str
        :param Order: 展示排序
        :type Order: int
        :param Starter: 初始化展示
        :type Starter: str
        :param Value: AttributeKey值
        :type Value: str
        """
        self.Label = None
        self.LabelType = None
        self.Order = None
        self.Starter = None
        self.Value = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.LabelType = params.get("LabelType")
        self.Order = params.get("Order")
        self.Starter = params.get("Starter")
        self.Value = params.get("Value")


class AuditSummary(AbstractModel):
    """跟蹤集概覽

    """

    def __init__(self):
        """
        :param AuditName: 跟蹤集名稱
        :type AuditName: str
        :param AuditStatus: 跟蹤集狀态，1：開啓，0：關閉
        :type AuditStatus: int
        :param CosBucketName: COS儲存桶名稱
        :type CosBucketName: str
        :param LogFilePrefix: 日志前綴
        :type LogFilePrefix: str
        """
        self.AuditName = None
        self.AuditStatus = None
        self.CosBucketName = None
        self.LogFilePrefix = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")
        self.AuditStatus = params.get("AuditStatus")
        self.CosBucketName = params.get("CosBucketName")
        self.LogFilePrefix = params.get("LogFilePrefix")


class CmqRegionInfo(AbstractModel):
    """cmq地域訊息

    """

    def __init__(self):
        """
        :param CmqRegion: cmq地域
        :type CmqRegion: str
        :param CmqRegionName: 地域描述
        :type CmqRegionName: str
        """
        self.CmqRegion = None
        self.CmqRegionName = None


    def _deserialize(self, params):
        self.CmqRegion = params.get("CmqRegion")
        self.CmqRegionName = params.get("CmqRegionName")


class CosRegionInfo(AbstractModel):
    """cmq地域訊息

    """

    def __init__(self):
        """
        :param CosRegion: cos地域
        :type CosRegion: str
        :param CosRegionName: 地域描述
        :type CosRegionName: str
        """
        self.CosRegion = None
        self.CosRegionName = None


    def _deserialize(self, params):
        self.CosRegion = params.get("CosRegion")
        self.CosRegionName = params.get("CosRegionName")


class CreateAuditRequest(AbstractModel):
    """CreateAudit請求參數結構體

    """

    def __init__(self):
        """
        :param AuditName: 跟蹤集名稱。3-128字元，只能包含 ASCII 編碼字母 a-z，A-Z，數字 0-9，下劃線 _。
        :type AuditName: str
        :param CosBucketName: cos的儲存桶名稱。僅支援小寫英文字母和數字即[a-z，0-9]、中劃線“-”及其組合。用戶自定義的字串支援1 - 40個字元。儲存桶命名不能以“-”開頭或結尾。如果不是新創建的儲存桶，雲審計不會去校驗該儲存桶是否真的存在，請謹慎填寫，避免日志投遞不成功，導緻您的數據丢失。
        :type CosBucketName: str
        :param CosRegion: cos地域。目前支援的地域可以使用ListCosEnableRegion來獲取。
        :type CosRegion: str
        :param IsCreateNewBucket: 是否創建新的cos儲存桶。1：是，0：否。
        :type IsCreateNewBucket: int
        :param IsEnableCmqNotify: 是否開啓cmq訊息通知。1：是，0：否。目前僅支援cmq的隊列服務。如果開啓cmq訊息通知服務，雲審計會将您的日志内容實時投遞到您指定地域的指定隊列中。
        :type IsEnableCmqNotify: int
        :param ReadWriteAttribute: 管理事件的讀寫屬性。1：只讀，2：只寫，3：全部。
        :type ReadWriteAttribute: int
        :param CmqQueueName: 隊列名稱。隊列名稱是一個不超過64個字元的字串，必須以字母爲首字元，剩餘部分可以包含字母、數字和橫劃線(-)。如果IsEnableCmqNotify值是1的話，此值屬于必填欄位。如果不是新創建的隊列，雲審計不會去校驗該隊列是否真的存在，請謹慎填寫，避免日志通知不成功，導緻您的數據丢失。
        :type CmqQueueName: str
        :param CmqRegion: 隊列所在的地域。可以通過ListCmqEnableRegion獲取支援的cmq地域。如果IsEnableCmqNotify值是1的話，此值屬于必填欄位。
        :type CmqRegion: str
        :param IsCreateNewQueue: 是否創建新的隊列。1：是，0：否。如果IsEnableCmqNotify值是1的話，此值屬于必填欄位。
        :type IsCreateNewQueue: int
        :param IsEnableKmsEncry: 是否開啓kms加密。1：是，0：否。如果開啓KMS加密，數據在投遞到cos時，會将數據加密。
        :type IsEnableKmsEncry: int
        :param KeyId: CMK的全局唯一标識符，如果不是新創建的kms，該值是必填值。可以通過ListKeyAliasByRegion來獲取。雲審計不會校驗KeyId的合法性，請您謹慎填寫，避免給您的數據造成損失。
        :type KeyId: str
        :param KmsRegion: kms地域。目前支援的地域可以使用ListKmsEnableRegion來獲取。必須要和cos的地域保持一緻。
        :type KmsRegion: str
        :param LogFilePrefix: 日志文件前綴。3-40個字元，只能包含 ASCII 編碼字母 a-z，A-Z，數字 0-9。可以不填，預設以賬号ID作爲日志前綴。
        :type LogFilePrefix: str
        """
        self.AuditName = None
        self.CosBucketName = None
        self.CosRegion = None
        self.IsCreateNewBucket = None
        self.IsEnableCmqNotify = None
        self.ReadWriteAttribute = None
        self.CmqQueueName = None
        self.CmqRegion = None
        self.IsCreateNewQueue = None
        self.IsEnableKmsEncry = None
        self.KeyId = None
        self.KmsRegion = None
        self.LogFilePrefix = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")
        self.CosBucketName = params.get("CosBucketName")
        self.CosRegion = params.get("CosRegion")
        self.IsCreateNewBucket = params.get("IsCreateNewBucket")
        self.IsEnableCmqNotify = params.get("IsEnableCmqNotify")
        self.ReadWriteAttribute = params.get("ReadWriteAttribute")
        self.CmqQueueName = params.get("CmqQueueName")
        self.CmqRegion = params.get("CmqRegion")
        self.IsCreateNewQueue = params.get("IsCreateNewQueue")
        self.IsEnableKmsEncry = params.get("IsEnableKmsEncry")
        self.KeyId = params.get("KeyId")
        self.KmsRegion = params.get("KmsRegion")
        self.LogFilePrefix = params.get("LogFilePrefix")


class CreateAuditResponse(AbstractModel):
    """CreateAudit返回參數結構體

    """

    def __init__(self):
        """
        :param IsSuccess: 是否創建成功。
        :type IsSuccess: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")


class DeleteAuditRequest(AbstractModel):
    """DeleteAudit請求參數結構體

    """

    def __init__(self):
        """
        :param AuditName: 跟蹤集名稱
        :type AuditName: str
        """
        self.AuditName = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")


class DeleteAuditResponse(AbstractModel):
    """DeleteAudit返回參數結構體

    """

    def __init__(self):
        """
        :param IsSuccess: 是否删除成功
        :type IsSuccess: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")


class DescribeAuditRequest(AbstractModel):
    """DescribeAudit請求參數結構體

    """

    def __init__(self):
        """
        :param AuditName: 跟蹤集名稱
        :type AuditName: str
        """
        self.AuditName = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")


class DescribeAuditResponse(AbstractModel):
    """DescribeAudit返回參數結構體

    """

    def __init__(self):
        """
        :param AuditName: 跟蹤集名稱。
        :type AuditName: str
        :param AuditStatus: 跟蹤集狀态，1：開啓，0：停止。
        :type AuditStatus: int
        :param CmqQueueName: 隊列名稱。
        :type CmqQueueName: str
        :param CmqRegion: 隊列所在地域。
        :type CmqRegion: str
        :param CosBucketName: cos儲存桶名稱。
        :type CosBucketName: str
        :param CosRegion: cos儲存桶所在地域。
        :type CosRegion: str
        :param IsEnableCmqNotify: 是否開啓cmq訊息通知。1：是，0：否。
        :type IsEnableCmqNotify: int
        :param IsEnableKmsEncry: 是否開啓kms加密。1：是，0：否。如果開啓KMS加密，數據在投遞到cos時，會将數據加密。
        :type IsEnableKmsEncry: int
        :param KeyId: CMK的全局唯一标識符。
        :type KeyId: str
        :param KmsAlias: CMK别名。
        :type KmsAlias: str
        :param KmsRegion: kms地域。
        :type KmsRegion: str
        :param LogFilePrefix: 日志前綴。
        :type LogFilePrefix: str
        :param ReadWriteAttribute: 管理事件讀寫屬性，1：只讀，2：只寫，3：全部
        :type ReadWriteAttribute: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AuditName = None
        self.AuditStatus = None
        self.CmqQueueName = None
        self.CmqRegion = None
        self.CosBucketName = None
        self.CosRegion = None
        self.IsEnableCmqNotify = None
        self.IsEnableKmsEncry = None
        self.KeyId = None
        self.KmsAlias = None
        self.KmsRegion = None
        self.LogFilePrefix = None
        self.ReadWriteAttribute = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")
        self.AuditStatus = params.get("AuditStatus")
        self.CmqQueueName = params.get("CmqQueueName")
        self.CmqRegion = params.get("CmqRegion")
        self.CosBucketName = params.get("CosBucketName")
        self.CosRegion = params.get("CosRegion")
        self.IsEnableCmqNotify = params.get("IsEnableCmqNotify")
        self.IsEnableKmsEncry = params.get("IsEnableKmsEncry")
        self.KeyId = params.get("KeyId")
        self.KmsAlias = params.get("KmsAlias")
        self.KmsRegion = params.get("KmsRegion")
        self.LogFilePrefix = params.get("LogFilePrefix")
        self.ReadWriteAttribute = params.get("ReadWriteAttribute")
        self.RequestId = params.get("RequestId")


class Event(AbstractModel):
    """日志詳情

    """

    def __init__(self):
        """
        :param Resources: 資源對
        :type Resources: :class:`taifucloudcloud.cloudaudit.v20190319.models.Resource`
        :param AccountID: 主賬号ID
        :type AccountID: int
        :param CloudAuditEvent: 日志詳情
        :type CloudAuditEvent: str
        :param ErrorCode: 鑒權錯誤碼
        :type ErrorCode: int
        :param EventId: 日志ID
        :type EventId: str
        :param EventName: 事件名稱
        :type EventName: str
        :param EventNameCn: 事件名稱中文描述（此欄位請按需使用，如果您是其他語言使用者，可以忽略該欄位描述）
        :type EventNameCn: str
        :param EventRegion: 事件地域
        :type EventRegion: str
        :param EventSource: 請求來源
        :type EventSource: str
        :param EventTime: 事件時間
        :type EventTime: str
        :param RequestID: 請求ID
        :type RequestID: str
        :param ResourceRegion: 資源地域
        :type ResourceRegion: str
        :param ResourceTypeCn: 資源類型中文描述（此欄位請按需使用，如果您是其他語言使用者，可以忽略該欄位描述）
        :type ResourceTypeCn: str
        :param SecretId: 證書ID
        :type SecretId: str
        :param SourceIPAddress: 源IP
        :type SourceIPAddress: str
        :param Username: 用戶名
        :type Username: str
        """
        self.Resources = None
        self.AccountID = None
        self.CloudAuditEvent = None
        self.ErrorCode = None
        self.EventId = None
        self.EventName = None
        self.EventNameCn = None
        self.EventRegion = None
        self.EventSource = None
        self.EventTime = None
        self.RequestID = None
        self.ResourceRegion = None
        self.ResourceTypeCn = None
        self.SecretId = None
        self.SourceIPAddress = None
        self.Username = None


    def _deserialize(self, params):
        if params.get("Resources") is not None:
            self.Resources = Resource()
            self.Resources._deserialize(params.get("Resources"))
        self.AccountID = params.get("AccountID")
        self.CloudAuditEvent = params.get("CloudAuditEvent")
        self.ErrorCode = params.get("ErrorCode")
        self.EventId = params.get("EventId")
        self.EventName = params.get("EventName")
        self.EventNameCn = params.get("EventNameCn")
        self.EventRegion = params.get("EventRegion")
        self.EventSource = params.get("EventSource")
        self.EventTime = params.get("EventTime")
        self.RequestID = params.get("RequestID")
        self.ResourceRegion = params.get("ResourceRegion")
        self.ResourceTypeCn = params.get("ResourceTypeCn")
        self.SecretId = params.get("SecretId")
        self.SourceIPAddress = params.get("SourceIPAddress")
        self.Username = params.get("Username")


class GetAttributeKeyRequest(AbstractModel):
    """GetAttributeKey請求參數結構體

    """

    def __init__(self):
        """
        :param WebsiteType: 網站類型，取值範圍是zh和en。如果不傳值預設zh
        :type WebsiteType: str
        """
        self.WebsiteType = None


    def _deserialize(self, params):
        self.WebsiteType = params.get("WebsiteType")


class GetAttributeKeyResponse(AbstractModel):
    """GetAttributeKey返回參數結構體

    """

    def __init__(self):
        """
        :param AttributeKeyDetails: AttributeKey的有效取值範圍
        :type AttributeKeyDetails: list of AttributeKeyDetail
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AttributeKeyDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AttributeKeyDetails") is not None:
            self.AttributeKeyDetails = []
            for item in params.get("AttributeKeyDetails"):
                obj = AttributeKeyDetail()
                obj._deserialize(item)
                self.AttributeKeyDetails.append(obj)
        self.RequestId = params.get("RequestId")


class InquireAuditCreditRequest(AbstractModel):
    """InquireAuditCredit請求參數結構體

    """


class InquireAuditCreditResponse(AbstractModel):
    """InquireAuditCredit返回參數結構體

    """

    def __init__(self):
        """
        :param AuditAmount: 可創建跟蹤集的數量
        :type AuditAmount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AuditAmount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AuditAmount = params.get("AuditAmount")
        self.RequestId = params.get("RequestId")


class ListAuditsRequest(AbstractModel):
    """ListAudits請求參數結構體

    """


class ListAuditsResponse(AbstractModel):
    """ListAudits返回參數結構體

    """

    def __init__(self):
        """
        :param AuditSummarys: 查詢跟蹤集概要集合
        :type AuditSummarys: list of AuditSummary
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AuditSummarys = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AuditSummarys") is not None:
            self.AuditSummarys = []
            for item in params.get("AuditSummarys"):
                obj = AuditSummary()
                obj._deserialize(item)
                self.AuditSummarys.append(obj)
        self.RequestId = params.get("RequestId")


class ListCmqEnableRegionRequest(AbstractModel):
    """ListCmqEnableRegion請求參數結構體

    """

    def __init__(self):
        """
        :param WebsiteType: 站點類型。zh表示 區，en表示國際區。預設 區。
        :type WebsiteType: str
        """
        self.WebsiteType = None


    def _deserialize(self, params):
        self.WebsiteType = params.get("WebsiteType")


class ListCmqEnableRegionResponse(AbstractModel):
    """ListCmqEnableRegion返回參數結構體

    """

    def __init__(self):
        """
        :param EnableRegions: 雲審計支援的cmq的可用區
        :type EnableRegions: list of CmqRegionInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.EnableRegions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EnableRegions") is not None:
            self.EnableRegions = []
            for item in params.get("EnableRegions"):
                obj = CmqRegionInfo()
                obj._deserialize(item)
                self.EnableRegions.append(obj)
        self.RequestId = params.get("RequestId")


class ListCosEnableRegionRequest(AbstractModel):
    """ListCosEnableRegion請求參數結構體

    """

    def __init__(self):
        """
        :param WebsiteType: 站點類型。zh表示 區，en表示國際區。預設 區。
        :type WebsiteType: str
        """
        self.WebsiteType = None


    def _deserialize(self, params):
        self.WebsiteType = params.get("WebsiteType")


class ListCosEnableRegionResponse(AbstractModel):
    """ListCosEnableRegion返回參數結構體

    """

    def __init__(self):
        """
        :param EnableRegions: 雲審計支援的cos可用區
        :type EnableRegions: list of CosRegionInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.EnableRegions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EnableRegions") is not None:
            self.EnableRegions = []
            for item in params.get("EnableRegions"):
                obj = CosRegionInfo()
                obj._deserialize(item)
                self.EnableRegions.append(obj)
        self.RequestId = params.get("RequestId")


class LookUpEventsRequest(AbstractModel):
    """LookUpEvents請求參數結構體

    """

    def __init__(self):
        """
        :param EndTime: 結束時間
        :type EndTime: int
        :param StartTime: 開始時間
        :type StartTime: int
        :param LookupAttributes: 檢索條件
        :type LookupAttributes: list of LookupAttribute
        :param MaxResults: 返回日志的最大條數
        :type MaxResults: int
        :param Mode: 雲審計模式，有效值：standard | quick，其中standard是标準模式，quick是極速模式。預設爲标準模式
        :type Mode: str
        :param NextToken: 檢視更多日志的憑證
        :type NextToken: str
        """
        self.EndTime = None
        self.StartTime = None
        self.LookupAttributes = None
        self.MaxResults = None
        self.Mode = None
        self.NextToken = None


    def _deserialize(self, params):
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        if params.get("LookupAttributes") is not None:
            self.LookupAttributes = []
            for item in params.get("LookupAttributes"):
                obj = LookupAttribute()
                obj._deserialize(item)
                self.LookupAttributes.append(obj)
        self.MaxResults = params.get("MaxResults")
        self.Mode = params.get("Mode")
        self.NextToken = params.get("NextToken")


class LookUpEventsResponse(AbstractModel):
    """LookUpEvents返回參數結構體

    """

    def __init__(self):
        """
        :param Events: 日志集合
        :type Events: list of Event
        :param ListOver: 日志集合是否結束
        :type ListOver: bool
        :param NextToken: 檢視更多日志的憑證
        :type NextToken: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Events = None
        self.ListOver = None
        self.NextToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Events") is not None:
            self.Events = []
            for item in params.get("Events"):
                obj = Event()
                obj._deserialize(item)
                self.Events.append(obj)
        self.ListOver = params.get("ListOver")
        self.NextToken = params.get("NextToken")
        self.RequestId = params.get("RequestId")


class LookupAttribute(AbstractModel):
    """檢索條件

    """

    def __init__(self):
        """
        :param AttributeKey: AttributeKey的有效取值範圍是:RequestId、EventName、ReadOnly、Username、ResourceType、ResourceName和AccessKeyId，EventId
        :type AttributeKey: str
        :param AttributeValue: AttributeValue
        :type AttributeValue: str
        """
        self.AttributeKey = None
        self.AttributeValue = None


    def _deserialize(self, params):
        self.AttributeKey = params.get("AttributeKey")
        self.AttributeValue = params.get("AttributeValue")


class Resource(AbstractModel):
    """資源類型

    """

    def __init__(self):
        """
        :param ResourceName: 資源名稱
        :type ResourceName: str
        :param ResourceType: 資源類型
        :type ResourceType: str
        """
        self.ResourceName = None
        self.ResourceType = None


    def _deserialize(self, params):
        self.ResourceName = params.get("ResourceName")
        self.ResourceType = params.get("ResourceType")


class StartLoggingRequest(AbstractModel):
    """StartLogging請求參數結構體

    """

    def __init__(self):
        """
        :param AuditName: 跟蹤集名稱
        :type AuditName: str
        """
        self.AuditName = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")


class StartLoggingResponse(AbstractModel):
    """StartLogging返回參數結構體

    """

    def __init__(self):
        """
        :param IsSuccess: 是否開啓成功
        :type IsSuccess: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")


class StopLoggingRequest(AbstractModel):
    """StopLogging請求參數結構體

    """

    def __init__(self):
        """
        :param AuditName: 跟蹤集名稱
        :type AuditName: str
        """
        self.AuditName = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")


class StopLoggingResponse(AbstractModel):
    """StopLogging返回參數結構體

    """

    def __init__(self):
        """
        :param IsSuccess: 是否關閉成功
        :type IsSuccess: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")


class UpdateAuditRequest(AbstractModel):
    """UpdateAudit請求參數結構體

    """

    def __init__(self):
        """
        :param AuditName: 跟蹤集名稱
        :type AuditName: str
        :param CmqQueueName: 隊列名稱。隊列名稱是一個不超過64個字元的字串，必須以字母爲首字元，剩餘部分可以包含字母、數字和橫劃線(-)。如果IsEnableCmqNotify值是1的話，此值屬于必填欄位。如果不是新創建的隊列，雲審計不會去校驗該隊列是否真的存在，請謹慎填寫，避免日志通知不成功，導緻您的數據丢失。
        :type CmqQueueName: str
        :param CmqRegion: 隊列所在的地域。可以通過ListCmqEnableRegion獲取支援的cmq地域。如果IsEnableCmqNotify值是1的話，此值屬于必填欄位。
        :type CmqRegion: str
        :param CosBucketName: cos的儲存桶名稱。僅支援小寫英文字母和數字即[a-z，0-9]、中劃線“-”及其組合。用戶自定義的字串支援1 - 40個字元。儲存桶命名不能以“-”開頭或結尾。如果不是新創建的儲存桶，雲審計不會去校驗該儲存桶是否真的存在，請謹慎填寫，避免日志投遞不成功，導緻您的數據丢失。
        :type CosBucketName: str
        :param CosRegion: cos地域。目前支援的地域可以使用ListCosEnableRegion來獲取。
        :type CosRegion: str
        :param IsCreateNewBucket: 是否創建新的cos儲存桶。1：是，0：否。
        :type IsCreateNewBucket: int
        :param IsCreateNewQueue: 是否創建新的隊列。1：是，0：否。如果IsEnableCmqNotify值是1的話，此值屬于必填欄位。
        :type IsCreateNewQueue: int
        :param IsEnableCmqNotify: 是否開啓cmq訊息通知。1：是，0：否。目前僅支援cmq的隊列服務。如果開啓cmq訊息通知服務，雲審計會将您的日志内容實時投遞到您指定地域的指定隊列中。
        :type IsEnableCmqNotify: int
        :param IsEnableKmsEncry: 是否開啓kms加密。1：是，0：否。如果開啓KMS加密，數據在投遞到cos時，會将數據加密。
        :type IsEnableKmsEncry: int
        :param KeyId: CMK的全局唯一标識符，如果不是新創建的kms，該值是必填值。可以通過ListKeyAliasByRegion來獲取。雲審計不會校驗KeyId的合法性，請您謹慎填寫，避免給您的數據造成損失。
        :type KeyId: str
        :param KmsRegion: kms地域。目前支援的地域可以使用ListKmsEnableRegion來獲取。必須要和cos的地域保持一緻。
        :type KmsRegion: str
        :param LogFilePrefix: 日志文件前綴。3-40個字元，只能包含 ASCII 編碼字母 a-z，A-Z，數字 0-9。
        :type LogFilePrefix: str
        :param ReadWriteAttribute: 管理事件的讀寫屬性。1：只讀，2：只寫，3：全部。
        :type ReadWriteAttribute: int
        """
        self.AuditName = None
        self.CmqQueueName = None
        self.CmqRegion = None
        self.CosBucketName = None
        self.CosRegion = None
        self.IsCreateNewBucket = None
        self.IsCreateNewQueue = None
        self.IsEnableCmqNotify = None
        self.IsEnableKmsEncry = None
        self.KeyId = None
        self.KmsRegion = None
        self.LogFilePrefix = None
        self.ReadWriteAttribute = None


    def _deserialize(self, params):
        self.AuditName = params.get("AuditName")
        self.CmqQueueName = params.get("CmqQueueName")
        self.CmqRegion = params.get("CmqRegion")
        self.CosBucketName = params.get("CosBucketName")
        self.CosRegion = params.get("CosRegion")
        self.IsCreateNewBucket = params.get("IsCreateNewBucket")
        self.IsCreateNewQueue = params.get("IsCreateNewQueue")
        self.IsEnableCmqNotify = params.get("IsEnableCmqNotify")
        self.IsEnableKmsEncry = params.get("IsEnableKmsEncry")
        self.KeyId = params.get("KeyId")
        self.KmsRegion = params.get("KmsRegion")
        self.LogFilePrefix = params.get("LogFilePrefix")
        self.ReadWriteAttribute = params.get("ReadWriteAttribute")


class UpdateAuditResponse(AbstractModel):
    """UpdateAudit返回參數結構體

    """

    def __init__(self):
        """
        :param IsSuccess: 是否更新成功
        :type IsSuccess: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")