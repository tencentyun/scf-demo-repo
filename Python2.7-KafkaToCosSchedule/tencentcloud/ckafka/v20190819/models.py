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


class Acl(AbstractModel):
    """ACL對象實體

    """

    def __init__(self):
        """
        :param ResourceType: Acl資源類型，（0:UNKNOWN，1:ANY，2:TOPIC，3:GROUP，4:CLUSTER，5:TRANSACTIONAL_ID）當前只有TOPIC，
        :type ResourceType: int
        :param ResourceName: 資源名稱，和resourceType相關如當resourceType爲TOPIC時，則該欄位表示topic名稱，當resourceType爲GROUP時，該欄位表示group名稱
        :type ResourceName: str
        :param Principal: 用戶清單，預設爲User:*，表示任何user都可以訪問，當前用戶只能是用戶清單中包含的用戶
注意：此欄位可能返回 null，表示取不到有效值。
        :type Principal: str
        :param Host: 預設爲*，表示任何host都可以訪問，當前ckafka不支援host爲*，但是後面開源kafka的産品化會直接支援
注意：此欄位可能返回 null，表示取不到有效值。
        :type Host: str
        :param Operation: Acl操作方式(0:UNKNOWN，1:ANY，2:ALL，3:READ，4:WRITE，5:CREATE，6:DELETE，7:ALTER，8:DESCRIBE，9:CLUSTER_ACTION，10:DESCRIBE_CONFIGS，11:ALTER_CONFIGS，12:IDEMPOTEN_WRITE)
        :type Operation: int
        :param PermissionType: 權限類型(0:UNKNOWN，1:ANY，2:DENY，3:ALLOW)
        :type PermissionType: int
        """
        self.ResourceType = None
        self.ResourceName = None
        self.Principal = None
        self.Host = None
        self.Operation = None
        self.PermissionType = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.ResourceName = params.get("ResourceName")
        self.Principal = params.get("Principal")
        self.Host = params.get("Host")
        self.Operation = params.get("Operation")
        self.PermissionType = params.get("PermissionType")


class AclResponse(AbstractModel):
    """ACL返回結果集

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的總數據條數
        :type TotalCount: int
        :param AclList: ACL清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type AclList: list of Acl
        """
        self.TotalCount = None
        self.AclList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AclList") is not None:
            self.AclList = []
            for item in params.get("AclList"):
                obj = Acl()
                obj._deserialize(item)
                self.AclList.append(obj)


class AppIdResponse(AbstractModel):
    """AppId的查詢結果

    """

    def __init__(self):
        """
        :param TotalCount: 符合要求的所有AppId數量
        :type TotalCount: int
        :param AppIdList: 符合要求的App Id清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type AppIdList: list of int
        """
        self.TotalCount = None
        self.AppIdList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.AppIdList = params.get("AppIdList")


class Assignment(AbstractModel):
    """儲存着分配給該消費者的 partition 訊息

    """

    def __init__(self):
        """
        :param Version: assingment版本訊息
        :type Version: int
        :param Topics: topic訊息清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Topics: list of GroupInfoTopics
        """
        self.Version = None
        self.Topics = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        if params.get("Topics") is not None:
            self.Topics = []
            for item in params.get("Topics"):
                obj = GroupInfoTopics()
                obj._deserialize(item)
                self.Topics.append(obj)


class Config(AbstractModel):
    """高級配置對象

    """

    def __init__(self):
        """
        :param Retention: 訊息保留時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type Retention: int
        :param MinInsyncReplicas: 最小同步複制數
注意：此欄位可能返回 null，表示取不到有效值。
        :type MinInsyncReplicas: int
        :param CleanUpPolicy: 日志清理模式，預設 delete。
delete：日志按保存時間删除；compact：日志按 key 壓縮；compact, delete：日志按 key 壓縮且會保存時間删除。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CleanUpPolicy: str
        :param SegmentMs: Segment 分片滾動的時長
注意：此欄位可能返回 null，表示取不到有效值。
        :type SegmentMs: int
        :param UncleanLeaderElectionEnable: 0表示 false。 1表示 true。
注意：此欄位可能返回 null，表示取不到有效值。
        :type UncleanLeaderElectionEnable: int
        :param SegmentBytes: Segment 分片滾動的位元數
注意：此欄位可能返回 null，表示取不到有效值。
        :type SegmentBytes: int
        :param MaxMessageBytes: 最大訊息位元數
注意：此欄位可能返回 null，表示取不到有效值。
        :type MaxMessageBytes: int
        """
        self.Retention = None
        self.MinInsyncReplicas = None
        self.CleanUpPolicy = None
        self.SegmentMs = None
        self.UncleanLeaderElectionEnable = None
        self.SegmentBytes = None
        self.MaxMessageBytes = None


    def _deserialize(self, params):
        self.Retention = params.get("Retention")
        self.MinInsyncReplicas = params.get("MinInsyncReplicas")
        self.CleanUpPolicy = params.get("CleanUpPolicy")
        self.SegmentMs = params.get("SegmentMs")
        self.UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        self.SegmentBytes = params.get("SegmentBytes")
        self.MaxMessageBytes = params.get("MaxMessageBytes")


class ConsumerGroup(AbstractModel):
    """用戶組實體

    """

    def __init__(self):
        """
        :param ConsumerGroupName: 用戶組名稱
        :type ConsumerGroupName: str
        :param SubscribedInfo: 訂閱訊息實體
        :type SubscribedInfo: list of SubscribedInfo
        """
        self.ConsumerGroupName = None
        self.SubscribedInfo = None


    def _deserialize(self, params):
        self.ConsumerGroupName = params.get("ConsumerGroupName")
        if params.get("SubscribedInfo") is not None:
            self.SubscribedInfo = []
            for item in params.get("SubscribedInfo"):
                obj = SubscribedInfo()
                obj._deserialize(item)
                self.SubscribedInfo.append(obj)


class ConsumerGroupResponse(AbstractModel):
    """消費組返回結果實體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的消費組數量
        :type TotalCount: int
        :param TopicList: 主題清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type TopicList: list of ConsumerGroupTopic
        :param GroupList: 消費分組List
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupList: list of ConsumerGroup
        :param TotalPartition: 所有分區數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalPartition: int
        :param PartitionListForMonitor: 監控的分區清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type PartitionListForMonitor: list of Partition
        :param TotalTopic: 主題總數
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalTopic: int
        :param TopicListForMonitor: 監控的主題清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type TopicListForMonitor: list of ConsumerGroupTopic
        :param GroupListForMonitor: 監控的組清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupListForMonitor: list of Group
        """
        self.TotalCount = None
        self.TopicList = None
        self.GroupList = None
        self.TotalPartition = None
        self.PartitionListForMonitor = None
        self.TotalTopic = None
        self.TopicListForMonitor = None
        self.GroupListForMonitor = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TopicList") is not None:
            self.TopicList = []
            for item in params.get("TopicList"):
                obj = ConsumerGroupTopic()
                obj._deserialize(item)
                self.TopicList.append(obj)
        if params.get("GroupList") is not None:
            self.GroupList = []
            for item in params.get("GroupList"):
                obj = ConsumerGroup()
                obj._deserialize(item)
                self.GroupList.append(obj)
        self.TotalPartition = params.get("TotalPartition")
        if params.get("PartitionListForMonitor") is not None:
            self.PartitionListForMonitor = []
            for item in params.get("PartitionListForMonitor"):
                obj = Partition()
                obj._deserialize(item)
                self.PartitionListForMonitor.append(obj)
        self.TotalTopic = params.get("TotalTopic")
        if params.get("TopicListForMonitor") is not None:
            self.TopicListForMonitor = []
            for item in params.get("TopicListForMonitor"):
                obj = ConsumerGroupTopic()
                obj._deserialize(item)
                self.TopicListForMonitor.append(obj)
        if params.get("GroupListForMonitor") is not None:
            self.GroupListForMonitor = []
            for item in params.get("GroupListForMonitor"):
                obj = Group()
                obj._deserialize(item)
                self.GroupListForMonitor.append(obj)


class ConsumerGroupTopic(AbstractModel):
    """消費組主題對象

    """

    def __init__(self):
        """
        :param TopicId: 主題ID
        :type TopicId: str
        :param TopicName: 主題名稱
        :type TopicName: str
        """
        self.TopicId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")


class CreateAclRequest(AbstractModel):
    """CreateAcl請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例id訊息
        :type InstanceId: str
        :param ResourceType: Acl資源類型，(0:UNKNOWN，1:ANY，2:TOPIC，3:GROUP，4:CLUSTER，5:TRANSACTIONAL_ID)，當前只有TOPIC，其它欄位用于後續兼容開源kafka的acl時使用
        :type ResourceType: int
        :param ResourceName: 資源名稱，和resourceType相關，如當resourceType爲TOPIC時，則該欄位表示topic名稱，當resourceType爲GROUP時，該欄位表示group名稱
        :type ResourceName: str
        :param Operation: Acl操作方式，(0:UNKNOWN，1:ANY，2:ALL，3:READ，4:WRITE，5:CREATE，6:DELETE，7:ALTER，8:DESCRIBE，9:CLUSTER_ACTION，10:DESCRIBE_CONFIGS，11:ALTER_CONFIGS)
        :type Operation: int
        :param PermissionType: 權限類型，(0:UNKNOWN，1:ANY，2:DENY，3:ALLOW)，當前ckakfa支援ALLOW(相當于白名單)，其它用于後續兼容開源kafka的acl時使用
        :type PermissionType: int
        :param Host: 預設爲\*，表示任何host都可以訪問，當前ckafka不支援host爲\*，但是後面開源kafka的産品化會直接支援
        :type Host: str
        :param Principal: 用戶清單，預設爲*，表示任何user都可以訪問，當前用戶只能是用戶清單中包含的用戶
        :type Principal: str
        """
        self.InstanceId = None
        self.ResourceType = None
        self.ResourceName = None
        self.Operation = None
        self.PermissionType = None
        self.Host = None
        self.Principal = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ResourceType = params.get("ResourceType")
        self.ResourceName = params.get("ResourceName")
        self.Operation = params.get("Operation")
        self.PermissionType = params.get("PermissionType")
        self.Host = params.get("Host")
        self.Principal = params.get("Principal")


class CreateAclResponse(AbstractModel):
    """CreateAcl返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 返回結果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreatePartitionRequest(AbstractModel):
    """CreatePartition請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例Id
        :type InstanceId: str
        :param TopicName: 主題名稱
        :type TopicName: str
        :param PartitionNum: 主題分區個數
        :type PartitionNum: int
        """
        self.InstanceId = None
        self.TopicName = None
        self.PartitionNum = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.PartitionNum = params.get("PartitionNum")


class CreatePartitionResponse(AbstractModel):
    """CreatePartition返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 返回的結果集
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateTopicIpWhiteListRequest(AbstractModel):
    """CreateTopicIpWhiteList請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例Id
        :type InstanceId: str
        :param TopicName: 主題名稱
        :type TopicName: str
        :param IpWhiteList: ip白名單清單
        :type IpWhiteList: list of str
        """
        self.InstanceId = None
        self.TopicName = None
        self.IpWhiteList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.IpWhiteList = params.get("IpWhiteList")


class CreateTopicIpWhiteListResponse(AbstractModel):
    """CreateTopicIpWhiteList返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 删除主題IP白名單結果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    """CreateTopic請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例Id
        :type InstanceId: str
        :param TopicName: 主題名稱，是一個不超過 64 個字元的字串，必須以字母爲首字元，剩餘部分可以包含字母、數字和橫劃線(-)
        :type TopicName: str
        :param PartitionNum: Partition個數，大于0
        :type PartitionNum: int
        :param ReplicaNum: 副本個數，不能多于 broker 數，最大爲3
        :type ReplicaNum: int
        :param EnableWhiteList: ip白名單開關, 1:打開  0:關閉，預設不打開
        :type EnableWhiteList: int
        :param IpWhiteList: Ip白名單清單，配額限制，enableWhileList=1時必選
        :type IpWhiteList: list of str
        :param CleanUpPolicy: 清理日志策略，日志清理模式，預設爲"delete"。"delete"：日志按保存時間删除，"compact"：日志按 key 壓縮，"compact, delete"：日志按 key 壓縮且會按保存時間删除。
        :type CleanUpPolicy: str
        :param Note: 主題備注，是一個不超過 64 個字元的字串，必須以字母爲首字元，剩餘部分可以包含字母、數字和橫劃線(-)
        :type Note: str
        :param MinInsyncReplicas: 預設爲1
        :type MinInsyncReplicas: int
        :param UncleanLeaderElectionEnable: 是否允許未同步的副本選爲leader，false:不允許，true:允許，預設不允許
        :type UncleanLeaderElectionEnable: int
        :param RetentionMs: 可訊息選。保留時間，單位ms，當前最小值爲60000ms
        :type RetentionMs: int
        :param SegmentMs: Segment分片滾動的時長，單位ms，當前最小爲3600000ms
        :type SegmentMs: int
        """
        self.InstanceId = None
        self.TopicName = None
        self.PartitionNum = None
        self.ReplicaNum = None
        self.EnableWhiteList = None
        self.IpWhiteList = None
        self.CleanUpPolicy = None
        self.Note = None
        self.MinInsyncReplicas = None
        self.UncleanLeaderElectionEnable = None
        self.RetentionMs = None
        self.SegmentMs = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.PartitionNum = params.get("PartitionNum")
        self.ReplicaNum = params.get("ReplicaNum")
        self.EnableWhiteList = params.get("EnableWhiteList")
        self.IpWhiteList = params.get("IpWhiteList")
        self.CleanUpPolicy = params.get("CleanUpPolicy")
        self.Note = params.get("Note")
        self.MinInsyncReplicas = params.get("MinInsyncReplicas")
        self.UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        self.RetentionMs = params.get("RetentionMs")
        self.SegmentMs = params.get("SegmentMs")


class CreateTopicResp(AbstractModel):
    """創建主題返回

    """

    def __init__(self):
        """
        :param TopicId: 主題Id
        :type TopicId: str
        """
        self.TopicId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")


class CreateTopicResponse(AbstractModel):
    """CreateTopic返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 返回創建結果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.CreateTopicResp`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateTopicResp()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateUserRequest(AbstractModel):
    """CreateUser請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例Id
        :type InstanceId: str
        :param Name: 用戶名稱
        :type Name: str
        :param Password: 用戶密碼
        :type Password: str
        """
        self.InstanceId = None
        self.Name = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        self.Password = params.get("Password")


class CreateUserResponse(AbstractModel):
    """CreateUser返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 返回的結果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DeleteAclRequest(AbstractModel):
    """DeleteAcl請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例id訊息
        :type InstanceId: str
        :param ResourceType: Acl資源類型，(0:UNKNOWN，1:ANY，2:TOPIC，3:GROUP，4:CLUSTER，5:TRANSACTIONAL_ID)，當前只有TOPIC，其它欄位用于後續兼容開源kafka的acl時使用
        :type ResourceType: int
        :param ResourceName: 資源名稱，和resourceType相關，如當resourceType爲TOPIC時，則該欄位表示topic名稱，當resourceType爲GROUP時，該欄位表示group名稱
        :type ResourceName: str
        :param Operation: Acl操作方式，(0:UNKNOWN，1:ANY，2:ALL，3:READ，4:WRITE，5:CREATE，6:DELETE，7:ALTER，8:DESCRIBE，9:CLUSTER_ACTION，10:DESCRIBE_CONFIGS，11:ALTER_CONFIGS，12:IDEMPOTEN_WRITE)，當前ckafka只支援READ,WRITE，其它用于後續兼容開源kafka的acl時使用
        :type Operation: int
        :param PermissionType: 權限類型，(0:UNKNOWN，1:ANY，2:DENY，3:ALLOW)，當前ckakfa支援ALLOW(相當于白名單)，其它用于後續兼容開源kafka的acl時使用
        :type PermissionType: int
        :param Host: 預設爲\*，表示任何host都可以訪問，當前ckafka不支援host爲\*，但是後面開源kafka的産品化會直接支援
        :type Host: str
        :param Principal: 用戶清單，預設爲*，表示任何user都可以訪問，當前用戶只能是用戶清單中包含的用戶
        :type Principal: str
        """
        self.InstanceId = None
        self.ResourceType = None
        self.ResourceName = None
        self.Operation = None
        self.PermissionType = None
        self.Host = None
        self.Principal = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ResourceType = params.get("ResourceType")
        self.ResourceName = params.get("ResourceName")
        self.Operation = params.get("Operation")
        self.PermissionType = params.get("PermissionType")
        self.Host = params.get("Host")
        self.Principal = params.get("Principal")


class DeleteAclResponse(AbstractModel):
    """DeleteAcl返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 返回結果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DeleteTopicIpWhiteListRequest(AbstractModel):
    """DeleteTopicIpWhiteList請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param TopicName: 主題名稱
        :type TopicName: str
        :param IpWhiteList: ip白名單清單
        :type IpWhiteList: list of str
        """
        self.InstanceId = None
        self.TopicName = None
        self.IpWhiteList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.IpWhiteList = params.get("IpWhiteList")


class DeleteTopicIpWhiteListResponse(AbstractModel):
    """DeleteTopicIpWhiteList返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 删除主題IP白名單結果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DeleteTopicRequest(AbstractModel):
    """DeleteTopic請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: ckafka 實例Id
        :type InstanceId: str
        :param TopicName: ckafka 主題名稱
        :type TopicName: str
        """
        self.InstanceId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")


class DeleteTopicResponse(AbstractModel):
    """DeleteTopic返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 返回的結果集
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DeleteUserRequest(AbstractModel):
    """DeleteUser請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例Id
        :type InstanceId: str
        :param Name: 用戶名稱
        :type Name: str
        """
        self.InstanceId = None
        self.Name = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")


class DeleteUserResponse(AbstractModel):
    """DeleteUser返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 返回結果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeACLRequest(AbstractModel):
    """DescribeACL請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例Id
        :type InstanceId: str
        :param ResourceType: Acl資源類型，(0:UNKNOWN，1:ANY，2:TOPIC，3:GROUP，4:CLUSTER，5:TRANSACTIONAL_ID)，當前只有TOPIC，其它欄位用于後續兼容開源kafka的acl時使用
        :type ResourceType: int
        :param ResourceName: 資源名稱，和resourceType相關，如當resourceType爲TOPIC時，則該欄位表示topic名稱，當resourceType爲GROUP時，該欄位表示group名稱
        :type ResourceName: str
        :param Offset: 偏移位置
        :type Offset: int
        :param Limit: 個數限制
        :type Limit: int
        :param SearchWord: 關鍵字比對
        :type SearchWord: str
        """
        self.InstanceId = None
        self.ResourceType = None
        self.ResourceName = None
        self.Offset = None
        self.Limit = None
        self.SearchWord = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ResourceType = params.get("ResourceType")
        self.ResourceName = params.get("ResourceName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchWord = params.get("SearchWord")


class DescribeACLResponse(AbstractModel):
    """DescribeACL返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 返回的ACL結果集對象
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.AclResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = AclResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeAppInfoRequest(AbstractModel):
    """DescribeAppInfo請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移位置
        :type Offset: int
        :param Limit: 本次查詢用戶數目最大數量限制，最大值爲50，預設50
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAppInfoResponse(AbstractModel):
    """DescribeAppInfo返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 返回的符合要求的App Id清單
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.AppIdResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = AppIdResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeConsumerGroupRequest(AbstractModel):
    """DescribeConsumerGroup請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: ckafka實例id。
        :type InstanceId: str
        :param GroupName: 可選，用戶需要查詢的group名稱。
        :type GroupName: str
        :param TopicName: 可選，用戶需要查詢的group中的對應的topic名稱，如果指定了該參數，而group又未指定則忽略該參數。
        :type TopicName: str
        :param Limit: 本次返回個數限制
        :type Limit: int
        :param Offset: 偏移位置
        :type Offset: int
        """
        self.InstanceId = None
        self.GroupName = None
        self.TopicName = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.GroupName = params.get("GroupName")
        self.TopicName = params.get("TopicName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeConsumerGroupResponse(AbstractModel):
    """DescribeConsumerGroup返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 返回的消費分組訊息
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ConsumerGroupResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ConsumerGroupResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeGroup(AbstractModel):
    """DescribeGroup返回實體

    """

    def __init__(self):
        """
        :param Group: groupId
        :type Group: str
        :param Protocol: 該 group 使用的協議。
        :type Protocol: str
        """
        self.Group = None
        self.Protocol = None


    def _deserialize(self, params):
        self.Group = params.get("Group")
        self.Protocol = params.get("Protocol")


class DescribeGroupInfoRequest(AbstractModel):
    """DescribeGroupInfo請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: （過濾條件）按照實例 ID 過濾。
        :type InstanceId: str
        :param GroupList: Kafka 消費分組，Consumer-group，這裏是數組形式，格式：GroupList.0=xxx&GroupList.1=yyy。
        :type GroupList: list of str
        """
        self.InstanceId = None
        self.GroupList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.GroupList = params.get("GroupList")


class DescribeGroupInfoResponse(AbstractModel):
    """DescribeGroupInfo返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 返回的結果
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: list of GroupInfoResponse
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = GroupInfoResponse()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeGroupOffsetsRequest(AbstractModel):
    """DescribeGroupOffsets請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: （過濾條件）按照實例 ID 過濾
        :type InstanceId: str
        :param Group: Kafka 消費分組
        :type Group: str
        :param Topics: group 訂閱的主題名稱數組，如果沒有該數組，則表示指定的 group 下所有 topic 訊息
        :type Topics: list of str
        :param SearchWord: 模糊比對 topicName
        :type SearchWord: str
        :param Offset: 本次查詢的偏移位置，預設爲0
        :type Offset: int
        :param Limit: 本次返回結果的最大個數，預設爲50，最大值爲50
        :type Limit: int
        """
        self.InstanceId = None
        self.Group = None
        self.Topics = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Group = params.get("Group")
        self.Topics = params.get("Topics")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeGroupOffsetsResponse(AbstractModel):
    """DescribeGroupOffsets返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 返回的結果對象
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.GroupOffsetResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = GroupOffsetResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeGroupRequest(AbstractModel):
    """DescribeGroup請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param SearchWord: 搜索關鍵字
        :type SearchWord: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 最大返回數量
        :type Limit: int
        """
        self.InstanceId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeGroupResponse(AbstractModel):
    """DescribeGroup返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 返回結果集清單
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.GroupResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = GroupResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeInstanceAttributesRequest(AbstractModel):
    """DescribeInstanceAttributes請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例id
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeInstanceAttributesResponse(AbstractModel):
    """DescribeInstanceAttributes返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 實例屬性返回結果對象
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceAttributesResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = InstanceAttributesResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeInstancesDetailRequest(AbstractModel):
    """DescribeInstancesDetail請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: （過濾條件）按照實例ID過濾
        :type InstanceId: str
        :param SearchWord: （過濾條件）按照實例名稱過濾，支援模糊查詢
        :type SearchWord: str
        :param Status: （過濾條件）實例的狀态。0：創建中，1：運作中，2：删除中，不填預設返回全部
        :type Status: list of int
        :param Offset: 偏移量，不填預設爲0
        :type Offset: int
        :param Limit: 返回數量，不填則預設10，最大值20
        :type Limit: int
        :param TagKey: 比對标簽key值。
        :type TagKey: str
        :param Filters: 過濾器
        :type Filters: list of Filter
        """
        self.InstanceId = None
        self.SearchWord = None
        self.Status = None
        self.Offset = None
        self.Limit = None
        self.TagKey = None
        self.Filters = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TagKey = params.get("TagKey")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeInstancesDetailResponse(AbstractModel):
    """DescribeInstancesDetail返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 返回的實例詳情結果對象
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceDetailResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = InstanceDetailResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: （過濾條件）按照實例ID過濾
        :type InstanceId: str
        :param SearchWord: （過濾條件）按照實例名稱過濾，支援模糊查詢
        :type SearchWord: str
        :param Status: （過濾條件）實例的狀态。0：創建中，1：運作中，2：删除中，不填預設返回全部
        :type Status: list of int
        :param Offset: 偏移量，不填預設爲0
        :type Offset: int
        :param Limit: 返回數量，不填則預設10，最大值20
        :type Limit: int
        :param TagKey: 比對标簽key值。
        :type TagKey: str
        """
        self.InstanceId = None
        self.SearchWord = None
        self.Status = None
        self.Offset = None
        self.Limit = None
        self.TagKey = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TagKey = params.get("TagKey")


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 返回的結果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = InstanceResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeTopicAttributesRequest(AbstractModel):
    """DescribeTopicAttributes請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID
        :type InstanceId: str
        :param TopicName: 主題名稱
        :type TopicName: str
        """
        self.InstanceId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")


class DescribeTopicAttributesResponse(AbstractModel):
    """DescribeTopicAttributes返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 返回的結果對象
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicAttributesResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TopicAttributesResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeTopicDetailRequest(AbstractModel):
    """DescribeTopicDetail請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例id
        :type InstanceId: str
        :param SearchWord: （過濾條件）按照topicName過濾，支援模糊查詢
        :type SearchWord: str
        :param Offset: 偏移量，不填預設爲0
        :type Offset: int
        :param Limit: 返回數量，不填則預設 10，最大值20，取值要大于0
        :type Limit: int
        """
        self.InstanceId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTopicDetailResponse(AbstractModel):
    """DescribeTopicDetail返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 返回的主題詳情實體
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicDetailResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TopicDetailResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeTopicRequest(AbstractModel):
    """DescribeTopic請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID
        :type InstanceId: str
        :param SearchWord: 過濾條件，按照 topicName 過濾，支援模糊查詢
        :type SearchWord: str
        :param Offset: 偏移量，不填預設爲0
        :type Offset: int
        :param Limit: 返回數量，不填則預設爲10，最大值爲50
        :type Limit: int
        """
        self.InstanceId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTopicResponse(AbstractModel):
    """DescribeTopic返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 返回的結果
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TopicResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeUserRequest(AbstractModel):
    """DescribeUser請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例Id
        :type InstanceId: str
        :param SearchWord: 按照名稱過濾
        :type SearchWord: str
        :param Offset: 偏移
        :type Offset: int
        :param Limit: 本次返回個數
        :type Limit: int
        """
        self.InstanceId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeUserResponse(AbstractModel):
    """DescribeUser返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 返回結果清單
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.UserResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = UserResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """查詢過濾器
    >描述鍵值對過濾器，用于條件過濾查詢。例如過濾ID、名稱、狀态等
    > * 若存在多個`Filter`時，`Filter`間的關系爲邏輯與（`AND`）關系。
    > * 若同一個`Filter`存在多個`Values`，同一`Filter`下`Values`間的關系爲邏輯或（`OR`）關系。
    >

    """

    def __init__(self):
        """
        :param Name: 需要過濾的欄位。
        :type Name: str
        :param Values: 欄位的過濾值。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class Group(AbstractModel):
    """組實體

    """

    def __init__(self):
        """
        :param GroupName: 組名稱
        :type GroupName: str
        """
        self.GroupName = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")


class GroupInfoMember(AbstractModel):
    """consumer訊息

    """

    def __init__(self):
        """
        :param MemberId: coordinator 爲消費分組中的消費者生成的唯一 ID
        :type MemberId: str
        :param ClientId: 客戶消費者 SDK 自己設置的 client.id 訊息
        :type ClientId: str
        :param ClientHost: 一般儲存客戶的 IP 網址
        :type ClientHost: str
        :param Assignment: 儲存着分配給該消費者的 partition 訊息
        :type Assignment: :class:`tencentcloud.ckafka.v20190819.models.Assignment`
        """
        self.MemberId = None
        self.ClientId = None
        self.ClientHost = None
        self.Assignment = None


    def _deserialize(self, params):
        self.MemberId = params.get("MemberId")
        self.ClientId = params.get("ClientId")
        self.ClientHost = params.get("ClientHost")
        if params.get("Assignment") is not None:
            self.Assignment = Assignment()
            self.Assignment._deserialize(params.get("Assignment"))


class GroupInfoResponse(AbstractModel):
    """GroupInfo返回數據的實體

    """

    def __init__(self):
        """
        :param ErrorCode: 錯誤碼，正常爲0
        :type ErrorCode: str
        :param State: group 狀态描述（常見的爲 Empty、Stable、Dead 三種狀态）：
Dead：消費分組不存在
Empty：消費分組，當前沒有任何消費者訂閱
PreparingRebalance：消費分組處于 rebalance 狀态
CompletingRebalance：消費分組處于 rebalance 狀态
Stable：消費分組中各個消費者已經加入，處于穩定狀态
        :type State: str
        :param ProtocolType: 消費分組選擇的協議類型正常的消費者一般爲 consumer 但有些系統采用了自己的協議如 kafka-connect 用的就是 connect。只有标準的 consumer 協議，本介面才知道具體的分配方式的格式，才能解析到具體的 partition 的分配情況
        :type ProtocolType: str
        :param Protocol: 消費者 partition 分配算法常見的有如下幾種(Kafka 消費者 SDK 預設的選擇項爲 range)：range、 roundrobin、 sticky
        :type Protocol: str
        :param Members: 僅當 state 爲 Stable 且 protocol_type 爲 consumer 時， 該數組才包含訊息
        :type Members: list of GroupInfoMember
        :param Group: Kafka 消費分組
        :type Group: str
        """
        self.ErrorCode = None
        self.State = None
        self.ProtocolType = None
        self.Protocol = None
        self.Members = None
        self.Group = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.State = params.get("State")
        self.ProtocolType = params.get("ProtocolType")
        self.Protocol = params.get("Protocol")
        if params.get("Members") is not None:
            self.Members = []
            for item in params.get("Members"):
                obj = GroupInfoMember()
                obj._deserialize(item)
                self.Members.append(obj)
        self.Group = params.get("Group")


class GroupInfoTopics(AbstractModel):
    """GroupInfo内部topic對象

    """

    def __init__(self):
        """
        :param Topic: 分配的 topic 名稱
        :type Topic: str
        :param Partitions: 分配的 partition 訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Partitions: list of int
        """
        self.Topic = None
        self.Partitions = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        self.Partitions = params.get("Partitions")


class GroupOffsetPartition(AbstractModel):
    """組偏移量分區對象

    """

    def __init__(self):
        """
        :param Partition: topic 的 partitionId
        :type Partition: int
        :param Offset: consumer 提交的 offset 位置
        :type Offset: int
        :param Metadata: 支援消費者提交訊息時，傳入 metadata 作爲它用，當前一般爲空字串
注意：此欄位可能返回 null，表示取不到有效值。
        :type Metadata: str
        :param ErrorCode: 錯誤碼
        :type ErrorCode: int
        :param LogEndOffset: 當前 partition 最新的 offset
        :type LogEndOffset: int
        :param Lag: 未消費的訊息個數
        :type Lag: int
        """
        self.Partition = None
        self.Offset = None
        self.Metadata = None
        self.ErrorCode = None
        self.LogEndOffset = None
        self.Lag = None


    def _deserialize(self, params):
        self.Partition = params.get("Partition")
        self.Offset = params.get("Offset")
        self.Metadata = params.get("Metadata")
        self.ErrorCode = params.get("ErrorCode")
        self.LogEndOffset = params.get("LogEndOffset")
        self.Lag = params.get("Lag")


class GroupOffsetResponse(AbstractModel):
    """消費組偏移量返回結果

    """

    def __init__(self):
        """
        :param TotalCount: 符合調節的總結果數
        :type TotalCount: int
        :param TopicList: 該主題分區數組，其中每個元素爲一個 json object
注意：此欄位可能返回 null，表示取不到有效值。
        :type TopicList: list of GroupOffsetTopic
        """
        self.TotalCount = None
        self.TopicList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TopicList") is not None:
            self.TopicList = []
            for item in params.get("TopicList"):
                obj = GroupOffsetTopic()
                obj._deserialize(item)
                self.TopicList.append(obj)


class GroupOffsetTopic(AbstractModel):
    """消費分組主題對象

    """

    def __init__(self):
        """
        :param Topic: 主題名稱
        :type Topic: str
        :param Partitions: 該主題分區數組，其中每個元素爲一個 json object
注意：此欄位可能返回 null，表示取不到有效值。
        :type Partitions: list of GroupOffsetPartition
        """
        self.Topic = None
        self.Partitions = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        if params.get("Partitions") is not None:
            self.Partitions = []
            for item in params.get("Partitions"):
                obj = GroupOffsetPartition()
                obj._deserialize(item)
                self.Partitions.append(obj)


class GroupResponse(AbstractModel):
    """DescribeGroup的返回

    """

    def __init__(self):
        """
        :param TotalCount: 計數
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param GroupList: GroupList
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupList: list of DescribeGroup
        """
        self.TotalCount = None
        self.GroupList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("GroupList") is not None:
            self.GroupList = []
            for item in params.get("GroupList"):
                obj = DescribeGroup()
                obj._deserialize(item)
                self.GroupList.append(obj)


class Instance(AbstractModel):
    """實例對象

    """

    def __init__(self):
        """
        :param InstanceId: 實例id
        :type InstanceId: str
        :param InstanceName: 實例名稱
        :type InstanceName: str
        :param Status: 實例的狀态。0：創建中，1：運作中，2：删除中 ， 5 隔離中，-1 創建失敗
        :type Status: int
        :param IfCommunity: 是否開源實例。開源：true，不開源：false
注意：此欄位可能返回 null，表示取不到有效值。
        :type IfCommunity: bool
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Status = None
        self.IfCommunity = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Status = params.get("Status")
        self.IfCommunity = params.get("IfCommunity")


class InstanceAttributesResponse(AbstractModel):
    """實例屬性返回結果對象

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param InstanceName: 實例名稱
        :type InstanceName: str
        :param VipList: 接入點 VIP 清單訊息
        :type VipList: list of VipEntity
        :param Vip: 虛拟IP
        :type Vip: str
        :param Vport: 虛拟端口
        :type Vport: str
        :param Status: 實例的狀态。0：創建中，1：運作中，2：删除中
        :type Status: int
        :param Bandwidth: 實例頻寬，單位：Mbps
        :type Bandwidth: int
        :param DiskSize: 實例的儲存大小，單位：GB
        :type DiskSize: int
        :param ZoneId: 可用區
        :type ZoneId: int
        :param VpcId: VPC 的 ID，爲空表示是基礎網絡
        :type VpcId: str
        :param SubnetId: 子網 ID， 爲空表示基礎網絡
        :type SubnetId: str
        :param Healthy: 實例健康狀态， 1：健康，2：告警，3：異常
        :type Healthy: int
        :param HealthyMessage: 實例健康訊息，當前會展示磁盤使用率，最大長度爲256
        :type HealthyMessage: str
        :param CreateTime: 創建時間
        :type CreateTime: int
        :param MsgRetentionTime: 訊息保存時間,單位爲分鍾
        :type MsgRetentionTime: int
        :param Config: 自動創建 Topic 配置， 若該欄位爲空，則表示未開啓自動創建
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.InstanceConfigDO`
        :param RemainderPartitions: 剩餘創建分區數
        :type RemainderPartitions: int
        :param RemainderTopics: 剩餘創建主題數
        :type RemainderTopics: int
        :param CreatedPartitions: 當前創建分區數
        :type CreatedPartitions: int
        :param CreatedTopics: 當前創建主題數
        :type CreatedTopics: int
        :param Tags: 标簽數組
注意：此欄位可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param ExpireTime: 過期時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type ExpireTime: int
        :param ZoneIds: 跨可用區
注意：此欄位可能返回 null，表示取不到有效值。
        :type ZoneIds: list of int
        :param Version: kafka版本訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Version: str
        :param MaxGroupNum: 最大分組數
注意：此欄位可能返回 null，表示取不到有效值。
        :type MaxGroupNum: int
        :param Cvm: 售賣類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type Cvm: int
        """
        self.InstanceId = None
        self.InstanceName = None
        self.VipList = None
        self.Vip = None
        self.Vport = None
        self.Status = None
        self.Bandwidth = None
        self.DiskSize = None
        self.ZoneId = None
        self.VpcId = None
        self.SubnetId = None
        self.Healthy = None
        self.HealthyMessage = None
        self.CreateTime = None
        self.MsgRetentionTime = None
        self.Config = None
        self.RemainderPartitions = None
        self.RemainderTopics = None
        self.CreatedPartitions = None
        self.CreatedTopics = None
        self.Tags = None
        self.ExpireTime = None
        self.ZoneIds = None
        self.Version = None
        self.MaxGroupNum = None
        self.Cvm = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        if params.get("VipList") is not None:
            self.VipList = []
            for item in params.get("VipList"):
                obj = VipEntity()
                obj._deserialize(item)
                self.VipList.append(obj)
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.Status = params.get("Status")
        self.Bandwidth = params.get("Bandwidth")
        self.DiskSize = params.get("DiskSize")
        self.ZoneId = params.get("ZoneId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Healthy = params.get("Healthy")
        self.HealthyMessage = params.get("HealthyMessage")
        self.CreateTime = params.get("CreateTime")
        self.MsgRetentionTime = params.get("MsgRetentionTime")
        if params.get("Config") is not None:
            self.Config = InstanceConfigDO()
            self.Config._deserialize(params.get("Config"))
        self.RemainderPartitions = params.get("RemainderPartitions")
        self.RemainderTopics = params.get("RemainderTopics")
        self.CreatedPartitions = params.get("CreatedPartitions")
        self.CreatedTopics = params.get("CreatedTopics")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.ExpireTime = params.get("ExpireTime")
        self.ZoneIds = params.get("ZoneIds")
        self.Version = params.get("Version")
        self.MaxGroupNum = params.get("MaxGroupNum")
        self.Cvm = params.get("Cvm")


class InstanceConfigDO(AbstractModel):
    """實例配置實體

    """

    def __init__(self):
        """
        :param AutoCreateTopicsEnable: 是否自動創建主題
        :type AutoCreateTopicsEnable: bool
        :param DefaultNumPartitions: 分區數
        :type DefaultNumPartitions: int
        :param DefaultReplicationFactor: 預設的複制Factor
        :type DefaultReplicationFactor: int
        """
        self.AutoCreateTopicsEnable = None
        self.DefaultNumPartitions = None
        self.DefaultReplicationFactor = None


    def _deserialize(self, params):
        self.AutoCreateTopicsEnable = params.get("AutoCreateTopicsEnable")
        self.DefaultNumPartitions = params.get("DefaultNumPartitions")
        self.DefaultReplicationFactor = params.get("DefaultReplicationFactor")


class InstanceDetail(AbstractModel):
    """實例詳情

    """

    def __init__(self):
        """
        :param InstanceId: 實例id
        :type InstanceId: str
        :param InstanceName: 實例名稱
        :type InstanceName: str
        :param Vip: 訪問實例的vip 訊息
        :type Vip: str
        :param Vport: 訪問實例的端口訊息
        :type Vport: str
        :param VipList: 虛拟IP清單
        :type VipList: list of VipEntity
        :param Status: 實例的狀态。0：創建中，1：運作中，2：删除中：5隔離中， -1 創建失敗
        :type Status: int
        :param Bandwidth: 實例頻寬，單位Mbps
        :type Bandwidth: int
        :param DiskSize: 實例的儲存大小，單位GB
        :type DiskSize: int
        :param ZoneId: 可用區域ID
        :type ZoneId: int
        :param VpcId: vpcId，如果爲空，說明是基礎網絡
        :type VpcId: str
        :param SubnetId: 子網id
        :type SubnetId: str
        :param RenewFlag: 實例是否續約，int  列舉值：1表示自動續約，2表示明确不自動續約
        :type RenewFlag: int
        :param Healthy: 實例狀态 int：0表示健康，1表示告警，2 表示實例狀态異常
        :type Healthy: int
        :param HealthyMessage: 實例狀态訊息
        :type HealthyMessage: str
        :param CreateTime: 實例創建時間時間
        :type CreateTime: int
        :param ExpireTime: 實例過期時間
        :type ExpireTime: int
        :param IsInternal: 是否爲内部客戶。值爲1 表示内部客戶
        :type IsInternal: int
        :param TopicNum: Topic個數
        :type TopicNum: int
        :param Tags: 标識tag
        :type Tags: list of Tag
        :param Version: kafka版本訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Version: str
        :param ZoneIds: 跨可用區
注意：此欄位可能返回 null，表示取不到有效值。
        :type ZoneIds: list of int
        :param Cvm: ckafka售賣類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type Cvm: int
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Vip = None
        self.Vport = None
        self.VipList = None
        self.Status = None
        self.Bandwidth = None
        self.DiskSize = None
        self.ZoneId = None
        self.VpcId = None
        self.SubnetId = None
        self.RenewFlag = None
        self.Healthy = None
        self.HealthyMessage = None
        self.CreateTime = None
        self.ExpireTime = None
        self.IsInternal = None
        self.TopicNum = None
        self.Tags = None
        self.Version = None
        self.ZoneIds = None
        self.Cvm = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        if params.get("VipList") is not None:
            self.VipList = []
            for item in params.get("VipList"):
                obj = VipEntity()
                obj._deserialize(item)
                self.VipList.append(obj)
        self.Status = params.get("Status")
        self.Bandwidth = params.get("Bandwidth")
        self.DiskSize = params.get("DiskSize")
        self.ZoneId = params.get("ZoneId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.RenewFlag = params.get("RenewFlag")
        self.Healthy = params.get("Healthy")
        self.HealthyMessage = params.get("HealthyMessage")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.IsInternal = params.get("IsInternal")
        self.TopicNum = params.get("TopicNum")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Version = params.get("Version")
        self.ZoneIds = params.get("ZoneIds")
        self.Cvm = params.get("Cvm")


class InstanceDetailResponse(AbstractModel):
    """實例詳情返回結果

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的實例總數
        :type TotalCount: int
        :param InstanceList: 符合條件的實例詳情清單
        :type InstanceList: list of InstanceDetail
        """
        self.TotalCount = None
        self.InstanceList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = InstanceDetail()
                obj._deserialize(item)
                self.InstanceList.append(obj)


class InstanceResponse(AbstractModel):
    """聚合的實例狀态返回結果

    """

    def __init__(self):
        """
        :param InstanceList: 符合條件的實例清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceList: list of Instance
        :param TotalCount: 符合條件的結果總數
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        """
        self.InstanceList = None
        self.TotalCount = None


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = Instance()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        self.TotalCount = params.get("TotalCount")


class JgwOperateResponse(AbstractModel):
    """操作型結果返回值

    """

    def __init__(self):
        """
        :param ReturnCode: 返回的code，0爲正常，非0爲錯誤
        :type ReturnCode: str
        :param ReturnMessage: 成功訊息
        :type ReturnMessage: str
        :param Data: 操作型返回的Data數據,可能有flowId等
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ckafka.v20190819.models.OperateResponseData`
        """
        self.ReturnCode = None
        self.ReturnMessage = None
        self.Data = None


    def _deserialize(self, params):
        self.ReturnCode = params.get("ReturnCode")
        self.ReturnMessage = params.get("ReturnMessage")
        if params.get("Data") is not None:
            self.Data = OperateResponseData()
            self.Data._deserialize(params.get("Data"))


class ModifyGroupOffsetsRequest(AbstractModel):
    """ModifyGroupOffsets請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: kafka實例id
        :type InstanceId: str
        :param Group: kafka 消費分組
        :type Group: str
        :param Strategy: 重置offset的策略，入參含義 0. 對齊shift-by參數，代表把offset向前或向後移動shift條 1. 對齊參考(by-duration,to-datetime,to-earliest,to-latest),代表把offset移動到指定timestamp的位置 2. 對齊參考(to-offset)，代表把offset移動到指定的offset位置
        :type Strategy: int
        :param Topics: 表示需要重置的topics， 不填表示全部
        :type Topics: list of str
        :param Shift: 當strategy爲0時，必須包含該欄位，可以大于零代表會把offset向後移動shift條，小於零則将offset向前回溯shift條數。正确重置後新的offset應該是(old_offset + shift)，需要注意的是如果新的offset小於partition的earliest則會設置爲earliest，如果大于partition 的latest則會設置爲latest
        :type Shift: int
        :param ShiftTimestamp: 單位ms。當strategy爲1時，必須包含該欄位，其中-2表示重置offset到最開始的位置，-1表示重置到最新的位置(相當于清空)，其它值則代表指定的時間，會獲取topic中指定時間的offset然後進行重置，需要注意的時，如果指定的時間不存在訊息，則獲取最末尾的offset。
        :type ShiftTimestamp: int
        :param Offset: 需要重新設置的offset位置。當strategy爲2，必須包含該欄位。
        :type Offset: int
        """
        self.InstanceId = None
        self.Group = None
        self.Strategy = None
        self.Topics = None
        self.Shift = None
        self.ShiftTimestamp = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Group = params.get("Group")
        self.Strategy = params.get("Strategy")
        self.Topics = params.get("Topics")
        self.Shift = params.get("Shift")
        self.ShiftTimestamp = params.get("ShiftTimestamp")
        self.Offset = params.get("Offset")


class ModifyGroupOffsetsResponse(AbstractModel):
    """ModifyGroupOffsets返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 返回結果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ModifyInstanceAttributesConfig(AbstractModel):
    """修改實例屬性的配置對象

    """

    def __init__(self):
        """
        :param AutoCreateTopicEnable: 自動創建 true 表示開啓，false 表示不開啓
        :type AutoCreateTopicEnable: bool
        :param DefaultNumPartitions: 可選，如果auto.create.topic.enable設置爲true沒有設置該值時，預設設置爲3
        :type DefaultNumPartitions: int
        :param DefaultReplicationFactor: 如歌auto.create.topic.enable設置爲true沒有指定該值時預設設置爲2
        :type DefaultReplicationFactor: int
        """
        self.AutoCreateTopicEnable = None
        self.DefaultNumPartitions = None
        self.DefaultReplicationFactor = None


    def _deserialize(self, params):
        self.AutoCreateTopicEnable = params.get("AutoCreateTopicEnable")
        self.DefaultNumPartitions = params.get("DefaultNumPartitions")
        self.DefaultReplicationFactor = params.get("DefaultReplicationFactor")


class ModifyInstanceAttributesRequest(AbstractModel):
    """ModifyInstanceAttributes請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例id
        :type InstanceId: str
        :param MsgRetentionTime: 實例日志的最長保留時間，單位分鍾，最大30天，0代表不開啓日志保留時間回收策略
        :type MsgRetentionTime: int
        :param InstanceName: 實例名稱，是一個不超過 64 個字元的字串，必須以字母爲首字元，剩餘部分可以包含字母、數字和橫劃線(-)
        :type InstanceName: str
        :param Config: 實例配置
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.ModifyInstanceAttributesConfig`
        """
        self.InstanceId = None
        self.MsgRetentionTime = None
        self.InstanceName = None
        self.Config = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.MsgRetentionTime = params.get("MsgRetentionTime")
        self.InstanceName = params.get("InstanceName")
        if params.get("Config") is not None:
            self.Config = ModifyInstanceAttributesConfig()
            self.Config._deserialize(params.get("Config"))


class ModifyInstanceAttributesResponse(AbstractModel):
    """ModifyInstanceAttributes返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 返回結果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ModifyPasswordRequest(AbstractModel):
    """ModifyPassword請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例Id
        :type InstanceId: str
        :param Name: 用戶名稱
        :type Name: str
        :param Password: 用戶當前密碼
        :type Password: str
        :param PasswordNew: 用戶新密碼
        :type PasswordNew: str
        """
        self.InstanceId = None
        self.Name = None
        self.Password = None
        self.PasswordNew = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        self.Password = params.get("Password")
        self.PasswordNew = params.get("PasswordNew")


class ModifyPasswordResponse(AbstractModel):
    """ModifyPassword返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 返回結果
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ModifyTopicAttributesRequest(AbstractModel):
    """ModifyTopicAttributes請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID。
        :type InstanceId: str
        :param TopicName: 主題名稱。
        :type TopicName: str
        :param Note: 主題備注，是一個不超過64個字元的字串，必須以字母爲首字元，剩餘部分可以包含字母、數字和橫劃線-。
        :type Note: str
        :param EnableWhiteList: IP 白名單開關，1：打開；0：關閉。
        :type EnableWhiteList: int
        :param MinInsyncReplicas: 預設爲1。
        :type MinInsyncReplicas: int
        :param UncleanLeaderElectionEnable: 預設爲 0，0：false；1：true。
        :type UncleanLeaderElectionEnable: int
        :param RetentionMs: 訊息保留時間，單位：ms，當前最小值爲60000ms。
        :type RetentionMs: int
        :param SegmentMs: Segment 分片滾動的時長，單位：ms，當前最小爲86400000ms。
        :type SegmentMs: int
        :param MaxMessageBytes: 主題訊息最大值，單位爲 Byte，最大值爲8388608Byte（即8MB）。
        :type MaxMessageBytes: int
        :param CleanUpPolicy: 訊息删除策略，可以選擇delete 或者compact
        :type CleanUpPolicy: str
        """
        self.InstanceId = None
        self.TopicName = None
        self.Note = None
        self.EnableWhiteList = None
        self.MinInsyncReplicas = None
        self.UncleanLeaderElectionEnable = None
        self.RetentionMs = None
        self.SegmentMs = None
        self.MaxMessageBytes = None
        self.CleanUpPolicy = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.Note = params.get("Note")
        self.EnableWhiteList = params.get("EnableWhiteList")
        self.MinInsyncReplicas = params.get("MinInsyncReplicas")
        self.UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        self.RetentionMs = params.get("RetentionMs")
        self.SegmentMs = params.get("SegmentMs")
        self.MaxMessageBytes = params.get("MaxMessageBytes")
        self.CleanUpPolicy = params.get("CleanUpPolicy")


class ModifyTopicAttributesResponse(AbstractModel):
    """ModifyTopicAttributes返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 返回結果集
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class OperateResponseData(AbstractModel):
    """操作類型返回的Data結構

    """

    def __init__(self):
        """
        :param FlowId: FlowId
注意：此欄位可能返回 null，表示取不到有效值。
        :type FlowId: int
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")


class Partition(AbstractModel):
    """分區實體

    """

    def __init__(self):
        """
        :param PartitionId: 分區ID
        :type PartitionId: int
        """
        self.PartitionId = None


    def _deserialize(self, params):
        self.PartitionId = params.get("PartitionId")


class PartitionOffset(AbstractModel):
    """分區和位移

    """

    def __init__(self):
        """
        :param Partition: Partition,例如"0"或"1"
注意：此欄位可能返回 null，表示取不到有效值。
        :type Partition: str
        :param Offset: Offset,例如100
注意：此欄位可能返回 null，表示取不到有效值。
        :type Offset: int
        """
        self.Partition = None
        self.Offset = None


    def _deserialize(self, params):
        self.Partition = params.get("Partition")
        self.Offset = params.get("Offset")


class SubscribedInfo(AbstractModel):
    """訂閱訊息實體

    """

    def __init__(self):
        """
        :param TopicName: 訂閱的主題名
        :type TopicName: str
        :param Partition: 訂閱的分區
注意：此欄位可能返回 null，表示取不到有效值。
        :type Partition: list of int
        :param PartitionOffset: 分區offset訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type PartitionOffset: list of PartitionOffset
        """
        self.TopicName = None
        self.Partition = None
        self.PartitionOffset = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.Partition = params.get("Partition")
        if params.get("PartitionOffset") is not None:
            self.PartitionOffset = []
            for item in params.get("PartitionOffset"):
                obj = PartitionOffset()
                obj._deserialize(item)
                self.PartitionOffset.append(obj)


class Tag(AbstractModel):
    """實例詳情中的标簽對象

    """

    def __init__(self):
        """
        :param TagKey: 标簽的key
        :type TagKey: str
        :param TagValue: 标簽的值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class Topic(AbstractModel):
    """返回的topic對象

    """

    def __init__(self):
        """
        :param TopicId: 主題的ID
        :type TopicId: str
        :param TopicName: 主題的名稱
        :type TopicName: str
        :param Note: 備注
注意：此欄位可能返回 null，表示取不到有效值。
        :type Note: str
        """
        self.TopicId = None
        self.TopicName = None
        self.Note = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.Note = params.get("Note")


class TopicAttributesResponse(AbstractModel):
    """主題屬性返回結果實體

    """

    def __init__(self):
        """
        :param TopicId: 主題 ID
        :type TopicId: str
        :param CreateTime: 創建時間
        :type CreateTime: int
        :param Note: 主題備注
注意：此欄位可能返回 null，表示取不到有效值。
        :type Note: str
        :param PartitionNum: 分區個數
        :type PartitionNum: int
        :param EnableWhiteList: IP 白名單開關，1：打開； 0：關閉
        :type EnableWhiteList: int
        :param IpWhiteList: IP 白名單清單
        :type IpWhiteList: list of str
        :param Config: topic 配置數組
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.Config`
        :param Partitions: 分區詳情
        :type Partitions: list of TopicPartitionDO
        """
        self.TopicId = None
        self.CreateTime = None
        self.Note = None
        self.PartitionNum = None
        self.EnableWhiteList = None
        self.IpWhiteList = None
        self.Config = None
        self.Partitions = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.CreateTime = params.get("CreateTime")
        self.Note = params.get("Note")
        self.PartitionNum = params.get("PartitionNum")
        self.EnableWhiteList = params.get("EnableWhiteList")
        self.IpWhiteList = params.get("IpWhiteList")
        if params.get("Config") is not None:
            self.Config = Config()
            self.Config._deserialize(params.get("Config"))
        if params.get("Partitions") is not None:
            self.Partitions = []
            for item in params.get("Partitions"):
                obj = TopicPartitionDO()
                obj._deserialize(item)
                self.Partitions.append(obj)


class TopicDetail(AbstractModel):
    """主題詳情

    """

    def __init__(self):
        """
        :param TopicName: 主題名稱
        :type TopicName: str
        :param TopicId: 主題ID
        :type TopicId: str
        :param PartitionNum: 分區數
        :type PartitionNum: int
        :param ReplicaNum: 副本數
        :type ReplicaNum: int
        :param Note: 備注
注意：此欄位可能返回 null，表示取不到有效值。
        :type Note: str
        :param CreateTime: 創建時間
        :type CreateTime: int
        :param EnableWhiteList: 是否開啓ip鑒權白名單，true表示開啓，false表示不開啓
        :type EnableWhiteList: bool
        :param IpWhiteListCount: ip白名單中ip個數
        :type IpWhiteListCount: int
        :param ForwardCosBucket: 數據備份cos bucket: 轉存到cos 的bucket網址
注意：此欄位可能返回 null，表示取不到有效值。
        :type ForwardCosBucket: str
        :param ForwardStatus: 數據備份cos 狀态： 1 不開啓數據備份，0 開啓數據備份
        :type ForwardStatus: int
        :param ForwardInterval: 數據備份到cos的週期頻率
        :type ForwardInterval: int
        :param Config: 高級配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.Config`
        """
        self.TopicName = None
        self.TopicId = None
        self.PartitionNum = None
        self.ReplicaNum = None
        self.Note = None
        self.CreateTime = None
        self.EnableWhiteList = None
        self.IpWhiteListCount = None
        self.ForwardCosBucket = None
        self.ForwardStatus = None
        self.ForwardInterval = None
        self.Config = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.TopicId = params.get("TopicId")
        self.PartitionNum = params.get("PartitionNum")
        self.ReplicaNum = params.get("ReplicaNum")
        self.Note = params.get("Note")
        self.CreateTime = params.get("CreateTime")
        self.EnableWhiteList = params.get("EnableWhiteList")
        self.IpWhiteListCount = params.get("IpWhiteListCount")
        self.ForwardCosBucket = params.get("ForwardCosBucket")
        self.ForwardStatus = params.get("ForwardStatus")
        self.ForwardInterval = params.get("ForwardInterval")
        if params.get("Config") is not None:
            self.Config = Config()
            self.Config._deserialize(params.get("Config"))


class TopicDetailResponse(AbstractModel):
    """主題詳情返回實體

    """

    def __init__(self):
        """
        :param TopicList: 返回的主題詳情清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type TopicList: list of TopicDetail
        :param TotalCount: 符合條件的所有主題詳情數量
        :type TotalCount: int
        """
        self.TopicList = None
        self.TotalCount = None


    def _deserialize(self, params):
        if params.get("TopicList") is not None:
            self.TopicList = []
            for item in params.get("TopicList"):
                obj = TopicDetail()
                obj._deserialize(item)
                self.TopicList.append(obj)
        self.TotalCount = params.get("TotalCount")


class TopicPartitionDO(AbstractModel):
    """分區詳情

    """

    def __init__(self):
        """
        :param Partition: Partition ID
        :type Partition: int
        :param LeaderStatus: Leader 運作狀态
        :type LeaderStatus: int
        :param IsrNum: ISR 個數
        :type IsrNum: int
        :param ReplicaNum: 副本個數
        :type ReplicaNum: int
        """
        self.Partition = None
        self.LeaderStatus = None
        self.IsrNum = None
        self.ReplicaNum = None


    def _deserialize(self, params):
        self.Partition = params.get("Partition")
        self.LeaderStatus = params.get("LeaderStatus")
        self.IsrNum = params.get("IsrNum")
        self.ReplicaNum = params.get("ReplicaNum")


class TopicResult(AbstractModel):
    """統一返回的TopicResponse

    """

    def __init__(self):
        """
        :param TopicList: 返回的主題訊息清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type TopicList: list of Topic
        :param TotalCount: 符合條件的 topic 數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        """
        self.TopicList = None
        self.TotalCount = None


    def _deserialize(self, params):
        if params.get("TopicList") is not None:
            self.TopicList = []
            for item in params.get("TopicList"):
                obj = Topic()
                obj._deserialize(item)
                self.TopicList.append(obj)
        self.TotalCount = params.get("TotalCount")


class User(AbstractModel):
    """用戶實體

    """

    def __init__(self):
        """
        :param UserId: 用戶id
        :type UserId: int
        :param Name: 用戶名稱
        :type Name: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param UpdateTime: 最後更新時間
        :type UpdateTime: str
        """
        self.UserId = None
        self.Name = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Name = params.get("Name")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class UserResponse(AbstractModel):
    """用戶返回實體

    """

    def __init__(self):
        """
        :param Users: 符合條件的用戶清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Users: list of User
        :param TotalCount: 符合條件的總用戶數
        :type TotalCount: int
        """
        self.Users = None
        self.TotalCount = None


    def _deserialize(self, params):
        if params.get("Users") is not None:
            self.Users = []
            for item in params.get("Users"):
                obj = User()
                obj._deserialize(item)
                self.Users.append(obj)
        self.TotalCount = params.get("TotalCount")


class VipEntity(AbstractModel):
    """虛拟IP實體

    """

    def __init__(self):
        """
        :param Vip: 虛拟IP
        :type Vip: str
        :param Vport: 虛拟端口
        :type Vport: str
        """
        self.Vip = None
        self.Vport = None


    def _deserialize(self, params):
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")