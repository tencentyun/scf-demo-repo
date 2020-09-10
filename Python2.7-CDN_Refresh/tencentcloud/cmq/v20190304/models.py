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

from tencentcloud.common.abstract_model import AbstractModel


class ClearQueueRequest(AbstractModel):
    """ClearQueue請求參數結構體

    """

    def __init__(self):
        """
        :param QueueName: 隊列名字，在單個地域同一帳号下唯一。隊列名稱是一個不超過64個字元的字串，必須以字母爲首字元，剩餘部分可以包含字母、數字和橫劃線(-)。
        :type QueueName: str
        """
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")


class ClearQueueResponse(AbstractModel):
    """ClearQueue返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ClearSubscriptionFilterTagsRequest(AbstractModel):
    """ClearSubscriptionFilterTags請求參數結構體

    """

    def __init__(self):
        """
        :param TopicName: 主題名字，在單個地域同一帳号下唯一。主題名稱是一個不超過64個字元的字串，必須以字母爲首字元，剩餘部分可以包含字母、數字和橫劃線（-）。
        :type TopicName: str
        :param SubscriptionName: 訂閱名字，在單個地域同一帳号的同一主題下唯一。訂閱名稱是一個不超過64個字元的字串，必須以字母爲首字元，剩餘部分可以包含字母、數字和橫劃線(-)。
        :type SubscriptionName: str
        """
        self.TopicName = None
        self.SubscriptionName = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.SubscriptionName = params.get("SubscriptionName")


class ClearSubscriptionFilterTagsResponse(AbstractModel):
    """ClearSubscriptionFilterTags返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateQueueRequest(AbstractModel):
    """CreateQueue請求參數結構體

    """

    def __init__(self):
        """
        :param QueueName: 隊列名字，在單個地域同一帳号下唯一。隊列名稱是一個不超過 64 個字元的字串，必須以字母爲首字元，剩餘部分可以包含字母、數字和橫劃線(-)。
        :type QueueName: str
        :param MaxMsgHeapNum: 最大堆積訊息數。取值範圍在公測期間爲 1,000,000 - 10,000,000，正式上線後範圍可達到 1000,000-1000,000,000。預設取值在公測期間爲 10,000,000，正式上線後爲 100,000,000。
        :type MaxMsgHeapNum: int
        :param PollingWaitSeconds: 訊息接收長輪詢等待時間。取值範圍 0-30 秒，預設值 0。
        :type PollingWaitSeconds: int
        :param VisibilityTimeout: 訊息可見性超時。取值範圍 1-43200 秒（即12小時内），預設值 30。
        :type VisibilityTimeout: int
        :param MaxMsgSize: 訊息最大長度。取值範圍 1024-65536 Byte（即1-64K），預設值 65536。
        :type MaxMsgSize: int
        :param MsgRetentionSeconds: 訊息保留週期。取值範圍 60-1296000 秒（1min-15天），預設值 345600 (4 天)。
        :type MsgRetentionSeconds: int
        :param RewindSeconds: 隊列是否開啓回溯訊息能力，該參數取值範圍0-msgRetentionSeconds,即最大的回溯時間爲訊息在隊列中的保留週期，0表示不開啓。
        :type RewindSeconds: int
        :param Transaction: 1 表示事務隊列，0 表示普通隊列
        :type Transaction: int
        :param FirstQueryInterval: 第一次回查間隔
        :type FirstQueryInterval: int
        :param MaxQueryCount: 最大回查次數
        :type MaxQueryCount: int
        :param DeadLetterQueueName: 死信隊列名稱
        :type DeadLetterQueueName: str
        :param Policy: 死信策略。0爲訊息被多次消費未删除，1爲Time-To-Live過期
        :type Policy: int
        :param MaxReceiveCount: 最大接收次數 1-1000
        :type MaxReceiveCount: int
        :param MaxTimeToLive: policy爲1時必選。最大未消費過期時間。範圍300-43200，單位秒，需要小於訊息最大保留時間msgRetentionSeconds
        :type MaxTimeToLive: int
        :param Trace: 是否開啓訊息軌迹追蹤，當不設置欄位時，預設爲不開啓，該欄位爲true表示開啓，爲false表示不開啓
        :type Trace: bool
        """
        self.QueueName = None
        self.MaxMsgHeapNum = None
        self.PollingWaitSeconds = None
        self.VisibilityTimeout = None
        self.MaxMsgSize = None
        self.MsgRetentionSeconds = None
        self.RewindSeconds = None
        self.Transaction = None
        self.FirstQueryInterval = None
        self.MaxQueryCount = None
        self.DeadLetterQueueName = None
        self.Policy = None
        self.MaxReceiveCount = None
        self.MaxTimeToLive = None
        self.Trace = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        self.MaxMsgHeapNum = params.get("MaxMsgHeapNum")
        self.PollingWaitSeconds = params.get("PollingWaitSeconds")
        self.VisibilityTimeout = params.get("VisibilityTimeout")
        self.MaxMsgSize = params.get("MaxMsgSize")
        self.MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self.RewindSeconds = params.get("RewindSeconds")
        self.Transaction = params.get("Transaction")
        self.FirstQueryInterval = params.get("FirstQueryInterval")
        self.MaxQueryCount = params.get("MaxQueryCount")
        self.DeadLetterQueueName = params.get("DeadLetterQueueName")
        self.Policy = params.get("Policy")
        self.MaxReceiveCount = params.get("MaxReceiveCount")
        self.MaxTimeToLive = params.get("MaxTimeToLive")
        self.Trace = params.get("Trace")


class CreateQueueResponse(AbstractModel):
    """CreateQueue返回參數結構體

    """

    def __init__(self):
        """
        :param QueueId: 創建成功的queueId
        :type QueueId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.QueueId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.QueueId = params.get("QueueId")
        self.RequestId = params.get("RequestId")


class CreateSubscribeRequest(AbstractModel):
    """CreateSubscribe請求參數結構體

    """

    def __init__(self):
        """
        :param TopicName: 主題名字，在單個地域同一帳号下唯一。主題名稱是一個不超過64個字元的字串，必須以字母爲首字元，剩餘部分可以包含字母、數字和橫劃線（-）。
        :type TopicName: str
        :param SubscriptionName: 訂閱名字，在單個地域同一帳号的同一主題下唯一。訂閱名稱是一個不超過64個字元的字串，必須以字母爲首字元，剩餘部分可以包含字母、數字和橫劃線(-)。
        :type SubscriptionName: str
        :param Protocol: 訂閱的協議，目前支援兩種協議：http、queue。使用http協議，用戶需自己搭建接受訊息的web server。使用queue，訊息會自動推送到CMQ queue，用戶可以并發地拉取訊息。
        :type Protocol: str
        :param Endpoint: 接收通知的Endpoint，根據協議Protocol區分：對于http，Endpoint必須以“`http://`”開頭，host可以是域名或IP；對于Queue，則填QueueName。 請注意，目前推送服務不能推送到私有網絡中，因此Endpoint填寫爲私有網絡域名或網址将接收不到推送的訊息，目前支援推送到公網和基礎網絡。
        :type Endpoint: str
        :param NotifyStrategy: 向Endpoint推送訊息出現錯誤時，CMQ推送服務器的重試策略。取值有：1）BACKOFF_RETRY，退避重試。每隔一定時間重試一次，重試夠一定次數後，就把該訊息丢棄，繼續推送下一條訊息；2）EXPONENTIAL_DECAY_RETRY，指數衰退重試。每次重試的間隔是指數遞增的，例如開始1s，後面是2s，4s，8s...由于Topic訊息的週期是一天，所以最多重試一天就把訊息丢棄。預設值是EXPONENTIAL_DECAY_RETRY。
        :type NotifyStrategy: str
        :param FilterTag: 訊息正文。訊息标簽（用于訊息過濾)。标簽數量不能超過5個，每個标簽不超過16個字元。與(Batch)PublishMessage的MsgTag參數配合使用，規則：1）如果FilterTag沒有設置，則無論MsgTag是否有設置，訂閱接收所有發布到Topic的訊息；2）如果FilterTag數組有值，則只有數組中至少有一個值在MsgTag數組中也存在時（即FilterTag和MsgTag有交集），訂閱才接收該發布到Topic的訊息；3）如果FilterTag數組有值，但MsgTag沒設置，則不接收任何發布到Topic的訊息，可以認爲是2）的一種特例，此時FilterTag和MsgTag沒有交集。規則整體的設計思想是以訂閱者的意願爲主。
        :type FilterTag: list of str
        :param BindingKey: BindingKey數量不超過5個， 每個BindingKey長度不超過64位元，該欄位表示訂閱接收訊息的過濾策略，每個BindingKey最多含有15個“.”， 即最多16個詞組。
        :type BindingKey: list of str
        :param NotifyContentFormat: 推送内容的格式。取值：1）JSON；2）SIMPLIFIED，即raw格式。如果Protocol是queue，則取值必須爲SIMPLIFIED。如果Protocol是http，兩個值均可以，預設值是JSON。
        :type NotifyContentFormat: str
        """
        self.TopicName = None
        self.SubscriptionName = None
        self.Protocol = None
        self.Endpoint = None
        self.NotifyStrategy = None
        self.FilterTag = None
        self.BindingKey = None
        self.NotifyContentFormat = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.SubscriptionName = params.get("SubscriptionName")
        self.Protocol = params.get("Protocol")
        self.Endpoint = params.get("Endpoint")
        self.NotifyStrategy = params.get("NotifyStrategy")
        self.FilterTag = params.get("FilterTag")
        self.BindingKey = params.get("BindingKey")
        self.NotifyContentFormat = params.get("NotifyContentFormat")


class CreateSubscribeResponse(AbstractModel):
    """CreateSubscribe返回參數結構體

    """

    def __init__(self):
        """
        :param SubscriptionId: SubscriptionId
        :type SubscriptionId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SubscriptionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubscriptionId = params.get("SubscriptionId")
        self.RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    """CreateTopic請求參數結構體

    """

    def __init__(self):
        """
        :param TopicName: 主題名字，在單個地域同一帳号下唯一。主題名稱是一個不超過64個字元的字串，必須以字母爲首字元，剩餘部分可以包含字母、數字和橫劃線（-）。
        :type TopicName: str
        :param MaxMsgSize: 訊息最大長度。取值範圍 1024-65536 Byte（即1-64K），預設值 65536。
        :type MaxMsgSize: int
        :param FilterType: 用于指定主題的訊息比對策略。
        :type FilterType: int
        :param MsgRetentionSeconds: 訊息保存時間。取值範圍60 - 86400 s（即1分鍾 - 1天），預設值86400。
        :type MsgRetentionSeconds: int
        :param Trace: 是否開啓訊息軌迹标識，true表示開啓，false表示不開啓，不填表示不開啓。
        :type Trace: bool
        """
        self.TopicName = None
        self.MaxMsgSize = None
        self.FilterType = None
        self.MsgRetentionSeconds = None
        self.Trace = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.MaxMsgSize = params.get("MaxMsgSize")
        self.FilterType = params.get("FilterType")
        self.MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self.Trace = params.get("Trace")


class CreateTopicResponse(AbstractModel):
    """CreateTopic返回參數結構體

    """

    def __init__(self):
        """
        :param TopicId: TopicName
        :type TopicId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TopicId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.RequestId = params.get("RequestId")


class DeadLetterPolicy(AbstractModel):
    """DeadLetterPolicy

    """

    def __init__(self):
        """
        :param DeadLetterQueueName: DeadLetterQueueName
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeadLetterQueueName: str
        :param DeadLetterQueue: DeadLetterQueue
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeadLetterQueue: str
        :param Policy: Policy
注意：此欄位可能返回 null，表示取不到有效值。
        :type Policy: int
        :param MaxTimeToLive: MaxTimeToLive
注意：此欄位可能返回 null，表示取不到有效值。
        :type MaxTimeToLive: int
        :param MaxReceiveCount: MaxReceiveCount
注意：此欄位可能返回 null，表示取不到有效值。
        :type MaxReceiveCount: int
        """
        self.DeadLetterQueueName = None
        self.DeadLetterQueue = None
        self.Policy = None
        self.MaxTimeToLive = None
        self.MaxReceiveCount = None


    def _deserialize(self, params):
        self.DeadLetterQueueName = params.get("DeadLetterQueueName")
        self.DeadLetterQueue = params.get("DeadLetterQueue")
        self.Policy = params.get("Policy")
        self.MaxTimeToLive = params.get("MaxTimeToLive")
        self.MaxReceiveCount = params.get("MaxReceiveCount")


class DeadLetterSource(AbstractModel):
    """DeadLetterSource

    """

    def __init__(self):
        """
        :param QueueId: QueueId
注意：此欄位可能返回 null，表示取不到有效值。
        :type QueueId: str
        :param QueueName: QueueName
注意：此欄位可能返回 null，表示取不到有效值。
        :type QueueName: str
        """
        self.QueueId = None
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueId = params.get("QueueId")
        self.QueueName = params.get("QueueName")


class DeleteQueueRequest(AbstractModel):
    """DeleteQueue請求參數結構體

    """

    def __init__(self):
        """
        :param QueueName: 隊列名字，在單個地域同一帳号下唯一。隊列名稱是一個不超過64個字元的字串，必須以字母爲首字元，剩餘部分可以包含字母、數字和橫劃線(-)。
        :type QueueName: str
        """
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")


class DeleteQueueResponse(AbstractModel):
    """DeleteQueue返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSubscribeRequest(AbstractModel):
    """DeleteSubscribe請求參數結構體

    """

    def __init__(self):
        """
        :param TopicName: 主題名字，在單個地域同一帳号下唯一。主題名稱是一個不超過64個字元的字串，必須以字母爲首字元，剩餘部分可以包含字母、數字和橫劃線(-)。
        :type TopicName: str
        :param SubscriptionName: 訂閱名字，在單個地域同一帳号的同一主題下唯一。訂閱名稱是一個不超過64個字元的字串，必須以字母爲首字元，剩餘部分可以包含字母、數字和橫劃線(-)。
        :type SubscriptionName: str
        """
        self.TopicName = None
        self.SubscriptionName = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.SubscriptionName = params.get("SubscriptionName")


class DeleteSubscribeResponse(AbstractModel):
    """DeleteSubscribe返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTopicRequest(AbstractModel):
    """DeleteTopic請求參數結構體

    """

    def __init__(self):
        """
        :param TopicName: 主題名字，在單個地域同一帳号下唯一。主題名稱是一個不超過64個字元的字串，必須以字母爲首字元，剩餘部分可以包含字母、數字和橫劃線(-)。
        :type TopicName: str
        """
        self.TopicName = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")


class DeleteTopicResponse(AbstractModel):
    """DeleteTopic返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDeadLetterSourceQueuesRequest(AbstractModel):
    """DescribeDeadLetterSourceQueues請求參數結構體

    """

    def __init__(self):
        """
        :param DeadLetterQueueName: 死信隊列名稱
        :type DeadLetterQueueName: str
        :param Limit: 分頁時本頁獲取主題清單的起始位置。如果填寫了該值，必須也要填寫 limit 。該值缺省時，後台取預設值 0。
        :type Limit: int
        :param Offset: 分頁時本頁獲取主題的個數，如果不傳遞該參數，則該參數預設爲20，最大值爲50。
        :type Offset: int
        :param Filters: 過濾死信隊列源隊列名稱，目前僅支援SourceQueueName過濾
        :type Filters: list of Filter
        """
        self.DeadLetterQueueName = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.DeadLetterQueueName = params.get("DeadLetterQueueName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeDeadLetterSourceQueuesResponse(AbstractModel):
    """DescribeDeadLetterSourceQueues返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 滿足本次條件的隊列個數
        :type TotalCount: int
        :param QueueSet: 死信隊列源隊列
        :type QueueSet: list of DeadLetterSource
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.QueueSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("QueueSet") is not None:
            self.QueueSet = []
            for item in params.get("QueueSet"):
                obj = DeadLetterSource()
                obj._deserialize(item)
                self.QueueSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeQueueDetailRequest(AbstractModel):
    """DescribeQueueDetail請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 分頁時本頁獲取隊列清單的起始位置。如果填寫了該值，必須也要填寫 limit 。該值缺省時，後台取預設值 0
        :type Offset: int
        :param Limit: 分頁時本頁獲取隊列的個數，如果不傳遞該參數，則該參數預設爲20，最大值爲50。
        :type Limit: int
        :param Filters: 篩選參數，目前支援QueueName篩選，且僅支援一個關鍵字
        :type Filters: list of Filter
        :param TagKey: 标簽搜索
        :type TagKey: str
        :param QueueName: 精确比對QueueName
        :type QueueName: str
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.TagKey = None
        self.QueueName = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.TagKey = params.get("TagKey")
        self.QueueName = params.get("QueueName")


class DescribeQueueDetailResponse(AbstractModel):
    """DescribeQueueDetail返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: queue總數量
        :type TotalCount: int
        :param QueueSet: queue清單
        :type QueueSet: list of QueueSet
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.QueueSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("QueueSet") is not None:
            self.QueueSet = []
            for item in params.get("QueueSet"):
                obj = QueueSet()
                obj._deserialize(item)
                self.QueueSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSubscriptionDetailRequest(AbstractModel):
    """DescribeSubscriptionDetail請求參數結構體

    """

    def __init__(self):
        """
        :param TopicName: 主題名字，在單個地域同一帳号下唯一。主題名稱是一個不超過64個字元的字串，必須以字母爲首字元，剩餘部分可以包含字母、數字和橫劃線（-）。
        :type TopicName: str
        :param Offset: 分頁時本頁獲取主題清單的起始位置。如果填寫了該值，必須也要填寫 limit 。該值缺省時，後台取預設值 0
        :type Offset: int
        :param Limit: 分頁時本頁獲取主題的個數，如果不傳遞該參數，則該參數預設爲20，最大值爲50。
        :type Limit: int
        :param Filters: 篩選參數，目前只支援SubscriptionName，且僅支援一個關鍵字。
        :type Filters: list of Filter
        """
        self.TopicName = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeSubscriptionDetailResponse(AbstractModel):
    """DescribeSubscriptionDetail返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 總數
        :type TotalCount: int
        :param SubscriptionSet: Subscription屬性集合
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubscriptionSet: list of Subscription
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SubscriptionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SubscriptionSet") is not None:
            self.SubscriptionSet = []
            for item in params.get("SubscriptionSet"):
                obj = Subscription()
                obj._deserialize(item)
                self.SubscriptionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTopicDetailRequest(AbstractModel):
    """DescribeTopicDetail請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 分頁時本頁獲取隊列清單的起始位置。如果填寫了該值，必須也要填寫 limit 。該值缺省時，後台取預設值 0。
        :type Offset: int
        :param Limit: 分頁時本頁獲取隊列的個數，如果不傳遞該參數，則該參數預設爲20，最大值爲50。
        :type Limit: int
        :param Filters: 目前只支援過濾TopicName ， 且只能填一個過濾值
        :type Filters: list of Filter
        :param TagKey: 标簽比對
        :type TagKey: str
        :param TopicName: 精确比對TopicName
        :type TopicName: str
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.TagKey = None
        self.TopicName = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.TagKey = params.get("TagKey")
        self.TopicName = params.get("TopicName")


class DescribeTopicDetailResponse(AbstractModel):
    """DescribeTopicDetail返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: TotalCount
        :type TotalCount: int
        :param TopicSet: TopicSet
        :type TopicSet: list of TopicSet
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TopicSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TopicSet") is not None:
            self.TopicSet = []
            for item in params.get("TopicSet"):
                obj = TopicSet()
                obj._deserialize(item)
                self.TopicSet.append(obj)
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """過濾參數

    """

    def __init__(self):
        """
        :param Name: 過濾參數的名字
        :type Name: str
        :param Values: 數值
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class ModifyQueueAttributeRequest(AbstractModel):
    """ModifyQueueAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param QueueName: 隊列名字，在單個地域同一帳号下唯一。隊列名稱是一個不超過 64 個字元的字串，必須以字母爲首字元，剩餘部分可以包含字母、數字和橫劃線(-)。
        :type QueueName: str
        :param MaxMsgHeapNum: 最大堆積訊息數。取值範圍在公測期間爲 1,000,000 - 10,000,000，正式上線後範圍可達到 1000,000-1000,000,000。預設取值在公測期間爲 10,000,000，正式上線後爲 100,000,000。
        :type MaxMsgHeapNum: int
        :param PollingWaitSeconds: 訊息接收長輪詢等待時間。取值範圍 0-30 秒，預設值 0。
        :type PollingWaitSeconds: int
        :param VisibilityTimeout: 訊息可見性超時。取值範圍 1-43200 秒（即12小時内），預設值 30。
        :type VisibilityTimeout: int
        :param MaxMsgSize: 訊息最大長度。取值範圍 1024-65536 Byte（即1-64K），預設值 65536。
        :type MaxMsgSize: int
        :param MsgRetentionSeconds: 訊息保留週期。取值範圍 60-1296000 秒（1min-15天），預設值 345600 (4 天)。
        :type MsgRetentionSeconds: int
        :param RewindSeconds: 訊息最長回溯時間，取值範圍0-msgRetentionSeconds，訊息的最大回溯之間爲訊息在隊列中的保存週期，0表示不開啓訊息回溯。
        :type RewindSeconds: int
        :param FirstQueryInterval: 第一次查詢時間
        :type FirstQueryInterval: int
        :param MaxQueryCount: 最大查詢次數
        :type MaxQueryCount: int
        :param DeadLetterQueueName: 死信隊列名稱
        :type DeadLetterQueueName: str
        :param MaxTimeToLive: MaxTimeToLivepolicy爲1時必選。最大未消費過期時間。範圍300-43200，單位秒，需要小於訊息最大保留時間MsgRetentionSeconds
        :type MaxTimeToLive: int
        :param MaxReceiveCount: 最大接收次數
        :type MaxReceiveCount: int
        :param Policy: 死信隊列策略
        :type Policy: int
        :param Trace: 是否開啓訊息軌迹标識，true表示開啓，false表示不開啓，不填表示不開啓。
        :type Trace: bool
        """
        self.QueueName = None
        self.MaxMsgHeapNum = None
        self.PollingWaitSeconds = None
        self.VisibilityTimeout = None
        self.MaxMsgSize = None
        self.MsgRetentionSeconds = None
        self.RewindSeconds = None
        self.FirstQueryInterval = None
        self.MaxQueryCount = None
        self.DeadLetterQueueName = None
        self.MaxTimeToLive = None
        self.MaxReceiveCount = None
        self.Policy = None
        self.Trace = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        self.MaxMsgHeapNum = params.get("MaxMsgHeapNum")
        self.PollingWaitSeconds = params.get("PollingWaitSeconds")
        self.VisibilityTimeout = params.get("VisibilityTimeout")
        self.MaxMsgSize = params.get("MaxMsgSize")
        self.MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self.RewindSeconds = params.get("RewindSeconds")
        self.FirstQueryInterval = params.get("FirstQueryInterval")
        self.MaxQueryCount = params.get("MaxQueryCount")
        self.DeadLetterQueueName = params.get("DeadLetterQueueName")
        self.MaxTimeToLive = params.get("MaxTimeToLive")
        self.MaxReceiveCount = params.get("MaxReceiveCount")
        self.Policy = params.get("Policy")
        self.Trace = params.get("Trace")


class ModifyQueueAttributeResponse(AbstractModel):
    """ModifyQueueAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubscriptionAttributeRequest(AbstractModel):
    """ModifySubscriptionAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param TopicName: 主題名字，在單個地域同一帳号下唯一。主題名稱是一個不超過64個字元的字串，必須以字母爲首字元，剩餘部分可以包含字母、數字和橫劃線（-）。
        :type TopicName: str
        :param SubscriptionName: 訂閱名字，在單個地域同一帳号的同一主題下唯一。訂閱名稱是一個不超過64個字元的字串，必須以字母爲首字元，剩餘部分可以包含字母、數字和橫劃線(-)。
        :type SubscriptionName: str
        :param NotifyStrategy: 向 Endpoint 推送訊息出現錯誤時，CMQ 推送服務器的重試策略。取值如下：
（1）BACKOFF_RETRY，退避重試。每隔一定時間重試一次，重試夠一定次數後，就把該訊息丢棄，繼續推送下一條訊息。
（2）EXPONENTIAL_DECAY_RETRY，指數衰退重試。每次重試的間隔是指數遞增的，例如開始1s，後面是2s，4s，8s···由于 Topic 訊息的週期是一天，所以最多重試一天就把訊息丢棄。預設值是 EXPONENTIAL_DECAY_RETRY。
        :type NotifyStrategy: str
        :param NotifyContentFormat: 推送内容的格式。取值：（1）JSON；（2）SIMPLIFIED，即 raw 格式。如果 Protocol 是 queue，則取值必須爲 SIMPLIFIED。如果 Protocol 是 HTTP，兩個值均可以，預設值是 JSON。
        :type NotifyContentFormat: str
        :param FilterTags: 訊息正文。訊息标簽（用于訊息過濾)。标簽數量不能超過5個，每個标簽不超過16個字元。與(Batch)PublishMessage的MsgTag參數配合使用，規則：1）如果FilterTag沒有設置，則無論MsgTag是否有設置，訂閱接收所有發布到Topic的訊息；2）如果FilterTag數組有值，則只有數組中至少有一個值在MsgTag數組中也存在時（即FilterTag和MsgTag有交集），訂閱才接收該發布到Topic的訊息；3）如果FilterTag數組有值，但MsgTag沒設置，則不接收任何發布到Topic的訊息，可以認爲是2）的一種特例，此時FilterTag和MsgTag沒有交集。規則整體的設計思想是以訂閱者的意願爲主。
        :type FilterTags: list of str
        :param BindingKey: BindingKey數量不超過5個， 每個BindingKey長度不超過64位元，該欄位表示訂閱接收訊息的過濾策略，每個BindingKey最多含有15個“.”， 即最多16個詞組。
        :type BindingKey: list of str
        """
        self.TopicName = None
        self.SubscriptionName = None
        self.NotifyStrategy = None
        self.NotifyContentFormat = None
        self.FilterTags = None
        self.BindingKey = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.SubscriptionName = params.get("SubscriptionName")
        self.NotifyStrategy = params.get("NotifyStrategy")
        self.NotifyContentFormat = params.get("NotifyContentFormat")
        self.FilterTags = params.get("FilterTags")
        self.BindingKey = params.get("BindingKey")


class ModifySubscriptionAttributeResponse(AbstractModel):
    """ModifySubscriptionAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTopicAttributeRequest(AbstractModel):
    """ModifyTopicAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param TopicName: 主題名字，在單個地域同一帳号下唯一。主題名稱是一個不超過64個字元的字串，必須以字母爲首字元，剩餘部分可以包含字母、數字和橫劃線(-)。
        :type TopicName: str
        :param MaxMsgSize: 訊息最大長度。取值範圍1024 - 65536 Byte（即1 - 64K），預設值65536。
        :type MaxMsgSize: int
        :param MsgRetentionSeconds: 訊息保存時間。取值範圍60 - 86400 s（即1分鍾 - 1天），預設值86400。
        :type MsgRetentionSeconds: int
        :param Trace: 是否開啓訊息軌迹标識，true表示開啓，false表示不開啓，不填表示不開啓。
        :type Trace: bool
        """
        self.TopicName = None
        self.MaxMsgSize = None
        self.MsgRetentionSeconds = None
        self.Trace = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.MaxMsgSize = params.get("MaxMsgSize")
        self.MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self.Trace = params.get("Trace")


class ModifyTopicAttributeResponse(AbstractModel):
    """ModifyTopicAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class QueueSet(AbstractModel):
    """批次queue屬性訊息

    """

    def __init__(self):
        """
        :param QueueId: QueueId
        :type QueueId: str
        :param QueueName: QueueName
        :type QueueName: str
        :param Qps: Qps
注意：此欄位可能返回 null，表示取不到有效值。
        :type Qps: int
        :param Bps: Bps
注意：此欄位可能返回 null，表示取不到有效值。
        :type Bps: int
        :param MaxDelaySeconds: MaxDelaySeconds
注意：此欄位可能返回 null，表示取不到有效值。
        :type MaxDelaySeconds: int
        :param MaxMsgHeapNum: MaxMsgHeapNum
注意：此欄位可能返回 null，表示取不到有效值。
        :type MaxMsgHeapNum: int
        :param PollingWaitSeconds: PollingWaitSeconds
注意：此欄位可能返回 null，表示取不到有效值。
        :type PollingWaitSeconds: int
        :param MsgRetentionSeconds: MsgRetentionSeconds
注意：此欄位可能返回 null，表示取不到有效值。
        :type MsgRetentionSeconds: int
        :param VisibilityTimeout: VisibilityTimeout
注意：此欄位可能返回 null，表示取不到有效值。
        :type VisibilityTimeout: int
        :param MaxMsgSize: MaxMsgSize
注意：此欄位可能返回 null，表示取不到有效值。
        :type MaxMsgSize: int
        :param RewindSeconds: RewindSeconds
注意：此欄位可能返回 null，表示取不到有效值。
        :type RewindSeconds: int
        :param CreateTime: CreateTime
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param LastModifyTime: LastModifyTime
注意：此欄位可能返回 null，表示取不到有效值。
        :type LastModifyTime: int
        :param ActiveMsgNum: ActiveMsgNum
注意：此欄位可能返回 null，表示取不到有效值。
        :type ActiveMsgNum: int
        :param InactiveMsgNum: InactiveMsgNum
注意：此欄位可能返回 null，表示取不到有效值。
        :type InactiveMsgNum: int
        :param DelayMsgNum: DelayMsgNum
注意：此欄位可能返回 null，表示取不到有效值。
        :type DelayMsgNum: int
        :param RewindMsgNum: RewindMsgNum
注意：此欄位可能返回 null，表示取不到有效值。
        :type RewindMsgNum: int
        :param MinMsgTime: MinMsgTime
注意：此欄位可能返回 null，表示取不到有效值。
        :type MinMsgTime: int
        :param Transaction: Transaction
注意：此欄位可能返回 null，表示取不到有效值。
        :type Transaction: bool
        :param DeadLetterSource: DeadLetterSource
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeadLetterSource: list of DeadLetterSource
        :param DeadLetterPolicy: DeadLetterPolicy
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeadLetterPolicy: :class:`tencentcloud.cmq.v20190304.models.DeadLetterPolicy`
        :param TransactionPolicy: TransactionPolicy
注意：此欄位可能返回 null，表示取不到有效值。
        :type TransactionPolicy: :class:`tencentcloud.cmq.v20190304.models.TransactionPolicy`
        :param CreateUin: 創建者uin
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateUin: int
        :param Tags: 标簽
注意：此欄位可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param Trace: 訊息軌迹表示，true表示開啓，false表示不開啓
注意：此欄位可能返回 null，表示取不到有效值。
        :type Trace: bool
        """
        self.QueueId = None
        self.QueueName = None
        self.Qps = None
        self.Bps = None
        self.MaxDelaySeconds = None
        self.MaxMsgHeapNum = None
        self.PollingWaitSeconds = None
        self.MsgRetentionSeconds = None
        self.VisibilityTimeout = None
        self.MaxMsgSize = None
        self.RewindSeconds = None
        self.CreateTime = None
        self.LastModifyTime = None
        self.ActiveMsgNum = None
        self.InactiveMsgNum = None
        self.DelayMsgNum = None
        self.RewindMsgNum = None
        self.MinMsgTime = None
        self.Transaction = None
        self.DeadLetterSource = None
        self.DeadLetterPolicy = None
        self.TransactionPolicy = None
        self.CreateUin = None
        self.Tags = None
        self.Trace = None


    def _deserialize(self, params):
        self.QueueId = params.get("QueueId")
        self.QueueName = params.get("QueueName")
        self.Qps = params.get("Qps")
        self.Bps = params.get("Bps")
        self.MaxDelaySeconds = params.get("MaxDelaySeconds")
        self.MaxMsgHeapNum = params.get("MaxMsgHeapNum")
        self.PollingWaitSeconds = params.get("PollingWaitSeconds")
        self.MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self.VisibilityTimeout = params.get("VisibilityTimeout")
        self.MaxMsgSize = params.get("MaxMsgSize")
        self.RewindSeconds = params.get("RewindSeconds")
        self.CreateTime = params.get("CreateTime")
        self.LastModifyTime = params.get("LastModifyTime")
        self.ActiveMsgNum = params.get("ActiveMsgNum")
        self.InactiveMsgNum = params.get("InactiveMsgNum")
        self.DelayMsgNum = params.get("DelayMsgNum")
        self.RewindMsgNum = params.get("RewindMsgNum")
        self.MinMsgTime = params.get("MinMsgTime")
        self.Transaction = params.get("Transaction")
        if params.get("DeadLetterSource") is not None:
            self.DeadLetterSource = []
            for item in params.get("DeadLetterSource"):
                obj = DeadLetterSource()
                obj._deserialize(item)
                self.DeadLetterSource.append(obj)
        if params.get("DeadLetterPolicy") is not None:
            self.DeadLetterPolicy = DeadLetterPolicy()
            self.DeadLetterPolicy._deserialize(params.get("DeadLetterPolicy"))
        if params.get("TransactionPolicy") is not None:
            self.TransactionPolicy = TransactionPolicy()
            self.TransactionPolicy._deserialize(params.get("TransactionPolicy"))
        self.CreateUin = params.get("CreateUin")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Trace = params.get("Trace")


class RewindQueueRequest(AbstractModel):
    """RewindQueue請求參數結構體

    """

    def __init__(self):
        """
        :param QueueName: 隊列名字，在單個地域同一帳号下唯一。隊列名稱是一個不超過64個字元的字串，必須以字母爲首字元，剩餘部分可以包含字母、數字和橫劃線(-)。
        :type QueueName: str
        :param StartConsumeTime: 設定該時間，則（Batch）receiveMessage介面，會按照生産訊息的先後順序消費該時間戳以後的訊息。
        :type StartConsumeTime: int
        """
        self.QueueName = None
        self.StartConsumeTime = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        self.StartConsumeTime = params.get("StartConsumeTime")


class RewindQueueResponse(AbstractModel):
    """RewindQueue返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Subscription(AbstractModel):
    """訂閱返回參數

    """

    def __init__(self):
        """
        :param SubscriptionName: SubscriptionName
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubscriptionName: str
        :param SubscriptionId: SubscriptionId
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubscriptionId: str
        :param TopicOwner: TopicOwner
注意：此欄位可能返回 null，表示取不到有效值。
        :type TopicOwner: int
        :param MsgCount: MsgCount
注意：此欄位可能返回 null，表示取不到有效值。
        :type MsgCount: int
        :param LastModifyTime: LastModifyTime
注意：此欄位可能返回 null，表示取不到有效值。
        :type LastModifyTime: int
        :param CreateTime: CreateTime
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param BindingKey: BindingKey
注意：此欄位可能返回 null，表示取不到有效值。
        :type BindingKey: list of str
        :param Endpoint: Endpoint
注意：此欄位可能返回 null，表示取不到有效值。
        :type Endpoint: str
        :param FilterTags: FilterTags
注意：此欄位可能返回 null，表示取不到有效值。
        :type FilterTags: list of str
        :param Protocol: Protocol
注意：此欄位可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param NotifyStrategy: NotifyStrategy
注意：此欄位可能返回 null，表示取不到有效值。
        :type NotifyStrategy: str
        :param NotifyContentFormat: NotifyContentFormat
注意：此欄位可能返回 null，表示取不到有效值。
        :type NotifyContentFormat: str
        """
        self.SubscriptionName = None
        self.SubscriptionId = None
        self.TopicOwner = None
        self.MsgCount = None
        self.LastModifyTime = None
        self.CreateTime = None
        self.BindingKey = None
        self.Endpoint = None
        self.FilterTags = None
        self.Protocol = None
        self.NotifyStrategy = None
        self.NotifyContentFormat = None


    def _deserialize(self, params):
        self.SubscriptionName = params.get("SubscriptionName")
        self.SubscriptionId = params.get("SubscriptionId")
        self.TopicOwner = params.get("TopicOwner")
        self.MsgCount = params.get("MsgCount")
        self.LastModifyTime = params.get("LastModifyTime")
        self.CreateTime = params.get("CreateTime")
        self.BindingKey = params.get("BindingKey")
        self.Endpoint = params.get("Endpoint")
        self.FilterTags = params.get("FilterTags")
        self.Protocol = params.get("Protocol")
        self.NotifyStrategy = params.get("NotifyStrategy")
        self.NotifyContentFormat = params.get("NotifyContentFormat")


class Tag(AbstractModel):
    """标簽

    """

    def __init__(self):
        """
        :param TagKey: 标簽Key
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param TagValue: 标簽值
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class TopicSet(AbstractModel):
    """topic返回訊息展示欄位

    """

    def __init__(self):
        """
        :param TopicId: TopicId
注意：此欄位可能返回 null，表示取不到有效值。
        :type TopicId: str
        :param TopicName: TopicName
注意：此欄位可能返回 null，表示取不到有效值。
        :type TopicName: str
        :param MsgRetentionSeconds: MsgRetentionSeconds
注意：此欄位可能返回 null，表示取不到有效值。
        :type MsgRetentionSeconds: int
        :param MaxMsgSize: MaxMsgSize
注意：此欄位可能返回 null，表示取不到有效值。
        :type MaxMsgSize: int
        :param Qps: Qps
注意：此欄位可能返回 null，表示取不到有效值。
        :type Qps: int
        :param FilterType: FilterType
注意：此欄位可能返回 null，表示取不到有效值。
        :type FilterType: int
        :param CreateTime: CreateTime
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param LastModifyTime: LastModifyTime
注意：此欄位可能返回 null，表示取不到有效值。
        :type LastModifyTime: int
        :param MsgCount: MsgCount
注意：此欄位可能返回 null，表示取不到有效值。
        :type MsgCount: int
        :param CreateUin: CreateUin
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateUin: int
        :param Tags: Tags
注意：此欄位可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param Trace: 主題是否開啓訊息軌迹，true表示開啓，false表示不開啓
注意：此欄位可能返回 null，表示取不到有效值。
        :type Trace: bool
        """
        self.TopicId = None
        self.TopicName = None
        self.MsgRetentionSeconds = None
        self.MaxMsgSize = None
        self.Qps = None
        self.FilterType = None
        self.CreateTime = None
        self.LastModifyTime = None
        self.MsgCount = None
        self.CreateUin = None
        self.Tags = None
        self.Trace = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self.MaxMsgSize = params.get("MaxMsgSize")
        self.Qps = params.get("Qps")
        self.FilterType = params.get("FilterType")
        self.CreateTime = params.get("CreateTime")
        self.LastModifyTime = params.get("LastModifyTime")
        self.MsgCount = params.get("MsgCount")
        self.CreateUin = params.get("CreateUin")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Trace = params.get("Trace")


class TransactionPolicy(AbstractModel):
    """TransactionPolicy

    """

    def __init__(self):
        """
        :param FirstQueryInterval: FirstQueryInterval
注意：此欄位可能返回 null，表示取不到有效值。
        :type FirstQueryInterval: int
        :param MaxQueryCount: MaxQueryCount
注意：此欄位可能返回 null，表示取不到有效值。
        :type MaxQueryCount: int
        """
        self.FirstQueryInterval = None
        self.MaxQueryCount = None


    def _deserialize(self, params):
        self.FirstQueryInterval = params.get("FirstQueryInterval")
        self.MaxQueryCount = params.get("MaxQueryCount")


class UnbindDeadLetterRequest(AbstractModel):
    """UnbindDeadLetter請求參數結構體

    """

    def __init__(self):
        """
        :param QueueName: 死信策略源隊列名稱，調用本介面會清空該隊列的死信隊列策略。
        :type QueueName: str
        """
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")


class UnbindDeadLetterResponse(AbstractModel):
    """UnbindDeadLetter返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")