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


class CleanUpInstanceRequest(AbstractModel):
    """CleanUpInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例Id
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class CleanUpInstanceResponse(AbstractModel):
    """CleanUpInstance返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務Id
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ClearInstanceRequest(AbstractModel):
    """ClearInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例Id
        :type InstanceId: str
        :param Password: redis的實例密碼
        :type Password: str
        """
        self.InstanceId = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Password = params.get("Password")


class ClearInstanceResponse(AbstractModel):
    """ClearInstance返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務Id
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateInstancesRequest(AbstractModel):
    """CreateInstances請求參數結構體

    """

    def __init__(self):
        """
        :param ZoneId: 實例所屬的可用區id
        :type ZoneId: int
        :param TypeId: 實例類型：2 – Redis2.8主從版，3 – Redis3.2主從版(CKV主從版)，4 – Redis3.2集群版(CKV集群版)，5-Redis2.8單機版，7 – Redis4.0集群版，
        :type TypeId: int
        :param MemSize: 實例容量，單位MB， 取值大小以 查詢售賣規格介面返回的規格爲準
        :type MemSize: int
        :param GoodsNum: 實例數量，單次購買實例數量以 查詢售賣規格介面返回的規格爲準
        :type GoodsNum: int
        :param Period: 購買時長，在創建包年包月實例的時候需要填寫，按量計費實例填1即可，單位：月，取值範圍 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]
        :type Period: int
        :param Password: 實例密碼，密碼規則：1.長度爲8-16個字元；2:至少包含字母、數字和字元!@^*()中的兩種
        :type Password: str
        :param BillingMode: 付費方式:0-按量計費，1-包年包月。
        :type BillingMode: int
        :param VpcId: 私有網絡ID，如果不傳則預設選擇基礎網絡，請使用私有網絡清單查詢，如：vpc-sad23jfdfk
        :type VpcId: str
        :param SubnetId: 基礎網絡下， subnetId無效； vpc子網下，取值以查詢子網清單，如：subnet-fdj24n34j2
        :type SubnetId: str
        :param ProjectId: 項目id，取值以用戶帳戶>用戶帳戶相關介面查詢>項目清單返回的projectId爲準
        :type ProjectId: int
        :param AutoRenew: 自動續約标識。0 - 預設狀态（手動續約）；1 - 自動續約；2 - 明确不自動續約
        :type AutoRenew: int
        :param SecurityGroupIdList: 安全組id數組
        :type SecurityGroupIdList: list of str
        :param VPort: 用戶自定義的端口 不填則預設爲6379
        :type VPort: int
        :param RedisShardNum: 實例分片數量，Redis2.8主從版、CKV主從版和Redis2.8單機版不需要填寫
        :type RedisShardNum: int
        :param RedisReplicasNum: 實例副本數量，Redis2.8主從版、CKV主從版和Redis2.8單機版不需要填寫
        :type RedisReplicasNum: int
        :param ReplicasReadonly: 是否支援副本只讀，Redis2.8主從版、CKV主從版和Redis2.8單機版不需要填寫
        :type ReplicasReadonly: bool
        :param InstanceName: 實例名稱
        :type InstanceName: str
        """
        self.ZoneId = None
        self.TypeId = None
        self.MemSize = None
        self.GoodsNum = None
        self.Period = None
        self.Password = None
        self.BillingMode = None
        self.VpcId = None
        self.SubnetId = None
        self.ProjectId = None
        self.AutoRenew = None
        self.SecurityGroupIdList = None
        self.VPort = None
        self.RedisShardNum = None
        self.RedisReplicasNum = None
        self.ReplicasReadonly = None
        self.InstanceName = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.TypeId = params.get("TypeId")
        self.MemSize = params.get("MemSize")
        self.GoodsNum = params.get("GoodsNum")
        self.Period = params.get("Period")
        self.Password = params.get("Password")
        self.BillingMode = params.get("BillingMode")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ProjectId = params.get("ProjectId")
        self.AutoRenew = params.get("AutoRenew")
        self.SecurityGroupIdList = params.get("SecurityGroupIdList")
        self.VPort = params.get("VPort")
        self.RedisShardNum = params.get("RedisShardNum")
        self.RedisReplicasNum = params.get("RedisReplicasNum")
        self.ReplicasReadonly = params.get("ReplicasReadonly")
        self.InstanceName = params.get("InstanceName")


class CreateInstancesResponse(AbstractModel):
    """CreateInstances返回參數結構體

    """

    def __init__(self):
        """
        :param DealId: 交易的Id
        :type DealId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class DescribeAutoBackupConfigRequest(AbstractModel):
    """DescribeAutoBackupConfig請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeAutoBackupConfigResponse(AbstractModel):
    """DescribeAutoBackupConfig返回參數結構體

    """

    def __init__(self):
        """
        :param AutoBackupType: 備份類型。自動備份類型： 1 “定時回檔”
        :type AutoBackupType: int
        :param WeekDays: Monday，Tuesday，Wednesday，Thursday，Friday，Saturday，Sunday。
        :type WeekDays: list of str
        :param TimePeriod: 時間段。
        :type TimePeriod: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AutoBackupType = None
        self.WeekDays = None
        self.TimePeriod = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AutoBackupType = params.get("AutoBackupType")
        self.WeekDays = params.get("WeekDays")
        self.TimePeriod = params.get("TimePeriod")
        self.RequestId = params.get("RequestId")


class DescribeBackupUrlRequest(AbstractModel):
    """DescribeBackupUrl請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例Id
        :type InstanceId: str
        :param BackupId: 備份Id，通過DescribeInstanceBackups介面可查
        :type BackupId: str
        """
        self.InstanceId = None
        self.BackupId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupId = params.get("BackupId")


class DescribeBackupUrlResponse(AbstractModel):
    """DescribeBackupUrl返回參數結構體

    """

    def __init__(self):
        """
        :param DownloadUrl: 外網下載網址（6小時）
        :type DownloadUrl: list of str
        :param InnerDownloadUrl: 内網下載網址（6小時）
        :type InnerDownloadUrl: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.InnerDownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.InnerDownloadUrl = params.get("InnerDownloadUrl")
        self.RequestId = params.get("RequestId")


class DescribeInstanceBackupsRequest(AbstractModel):
    """DescribeInstanceBackups請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 待操作的實例ID，可通過 DescribeInstance 介面返回值中的 InstanceId 獲取。
        :type InstanceId: str
        :param Limit: 實例清單大小，預設大小20
        :type Limit: int
        :param Offset: 偏移量，取Limit整數倍
        :type Offset: int
        :param BeginTime: 開始時間，格式如：2017-02-08 16:46:34。查詢實例在 [beginTime, endTime] 時間段内開始備份的備份清單。
        :type BeginTime: str
        :param EndTime: 結束時間，格式如：2017-02-08 19:09:26。查詢實例在 [beginTime, endTime] 時間段内開始備份的備份清單。
        :type EndTime: str
        :param Status: 1：備份在流程中，2：備份正常，3：備份轉RDB文件處理中，4：已完成RDB轉換，-1：備份已過期，-2：備份已删除。
        :type Status: list of int
        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None
        self.BeginTime = None
        self.EndTime = None
        self.Status = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")


class DescribeInstanceBackupsResponse(AbstractModel):
    """DescribeInstanceBackups返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 備份總數
        :type TotalCount: int
        :param BackupSet: 實例的備份數組
        :type BackupSet: list of RedisBackupSet
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.BackupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BackupSet") is not None:
            self.BackupSet = []
            for item in params.get("BackupSet"):
                obj = RedisBackupSet()
                obj._deserialize(item)
                self.BackupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceDealDetailRequest(AbstractModel):
    """DescribeInstanceDealDetail請求參數結構體

    """

    def __init__(self):
        """
        :param DealIds: 訂單ID數組
        :type DealIds: list of str
        """
        self.DealIds = None


    def _deserialize(self, params):
        self.DealIds = params.get("DealIds")


class DescribeInstanceDealDetailResponse(AbstractModel):
    """DescribeInstanceDealDetail返回參數結構體

    """

    def __init__(self):
        """
        :param DealDetails: 訂單詳細訊息
        :type DealDetails: list of TradeDealDetail
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DealDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DealDetails") is not None:
            self.DealDetails = []
            for item in params.get("DealDetails"):
                obj = TradeDealDetail()
                obj._deserialize(item)
                self.DealDetails.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceParamRecordsRequest(AbstractModel):
    """DescribeInstanceParamRecords請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例Id
        :type InstanceId: str
        :param Limit: 分頁大小
        :type Limit: int
        :param Offset: 偏移量，取Limit整數倍
        :type Offset: int
        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeInstanceParamRecordsResponse(AbstractModel):
    """DescribeInstanceParamRecords返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 總的修改曆史記錄數。
        :type TotalCount: int
        :param InstanceParamHistory: 修改曆史記錄訊息。
        :type InstanceParamHistory: list of InstanceParamHistory
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceParamHistory = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceParamHistory") is not None:
            self.InstanceParamHistory = []
            for item in params.get("InstanceParamHistory"):
                obj = InstanceParamHistory()
                obj._deserialize(item)
                self.InstanceParamHistory.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceParamsRequest(AbstractModel):
    """DescribeInstanceParams請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例Id
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeInstanceParamsResponse(AbstractModel):
    """DescribeInstanceParams返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 實例參數個數
        :type TotalCount: int
        :param InstanceEnumParam: 實例列舉類型參數
        :type InstanceEnumParam: list of InstanceEnumParam
        :param InstanceIntegerParam: 實例整型參數
        :type InstanceIntegerParam: list of InstanceIntegerParam
        :param InstanceTextParam: 實例字元型參數
        :type InstanceTextParam: list of InstanceTextParam
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceEnumParam = None
        self.InstanceIntegerParam = None
        self.InstanceTextParam = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceEnumParam") is not None:
            self.InstanceEnumParam = []
            for item in params.get("InstanceEnumParam"):
                obj = InstanceEnumParam()
                obj._deserialize(item)
                self.InstanceEnumParam.append(obj)
        if params.get("InstanceIntegerParam") is not None:
            self.InstanceIntegerParam = []
            for item in params.get("InstanceIntegerParam"):
                obj = InstanceIntegerParam()
                obj._deserialize(item)
                self.InstanceIntegerParam.append(obj)
        if params.get("InstanceTextParam") is not None:
            self.InstanceTextParam = []
            for item in params.get("InstanceTextParam"):
                obj = InstanceTextParam()
                obj._deserialize(item)
                self.InstanceTextParam.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceSecurityGroupRequest(AbstractModel):
    """DescribeInstanceSecurityGroup請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 實例清單
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class DescribeInstanceSecurityGroupResponse(AbstractModel):
    """DescribeInstanceSecurityGroup返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceSecurityGroupsDetail: 實例安全組訊息
        :type InstanceSecurityGroupsDetail: list of InstanceSecurityGroupDetail
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceSecurityGroupsDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceSecurityGroupsDetail") is not None:
            self.InstanceSecurityGroupsDetail = []
            for item in params.get("InstanceSecurityGroupsDetail"):
                obj = InstanceSecurityGroupDetail()
                obj._deserialize(item)
                self.InstanceSecurityGroupsDetail.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceShardsRequest(AbstractModel):
    """DescribeInstanceShards請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例id
        :type InstanceId: str
        :param FilterSlave: 是否過濾掉從節訊息
        :type FilterSlave: bool
        """
        self.InstanceId = None
        self.FilterSlave = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.FilterSlave = params.get("FilterSlave")


class DescribeInstanceShardsResponse(AbstractModel):
    """DescribeInstanceShards返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceShards: 實例分片清單訊息
        :type InstanceShards: list of InstanceClusterShard
        :param TotalCount: 實例分片節點總數
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceShards = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceShards") is not None:
            self.InstanceShards = []
            for item in params.get("InstanceShards"):
                obj = InstanceClusterShard()
                obj._deserialize(item)
                self.InstanceShards.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances請求參數結構體

    """

    def __init__(self):
        """
        :param Limit: 實例清單的大小，參數預設值20
        :type Limit: int
        :param Offset: 偏移量，取Limit整數倍
        :type Offset: int
        :param InstanceId: 實例Id，如：crs-6ubhgouj
        :type InstanceId: str
        :param OrderBy: 列舉範圍： projectId,createtime,instancename,type,curDeadline
        :type OrderBy: str
        :param OrderType: 1倒序，0順序，預設倒序
        :type OrderType: int
        :param VpcIds: 私有網絡ID數組，數組下标從0開始，如果不傳則預設選擇基礎網絡，如：47525
        :type VpcIds: list of str
        :param SubnetIds: 子網ID數組，數組下标從0開始，如：56854
        :type SubnetIds: list of str
        :param ProjectIds: 項目ID 組成的數組，數組下标從0開始
        :type ProjectIds: list of int
        :param SearchKey: 查找實例的ID。
        :type SearchKey: str
        :param InstanceName: 實例名稱
        :type InstanceName: str
        :param UniqVpcIds: 私有網絡ID數組，數組下标從0開始，如果不傳則預設選擇基礎網絡，如：vpc-sad23jfdfk
        :type UniqVpcIds: list of str
        :param UniqSubnetIds: 子網ID數組，數組下标從0開始，如：subnet-fdj24n34j2
        :type UniqSubnetIds: list of str
        :param RegionIds: 地域ID，已經棄用，可通過公共參數Region查詢對應地域
        :type RegionIds: list of int
        :param Status: 實例狀态：0-待初始化，1-流程中，2-運作中，-2-已隔離，-3-待删除
        :type Status: list of int
        :param TypeVersion: 類型版本：1-單機版,2-主從版,3-集群版
        :type TypeVersion: int
        :param EngineName: 引擎訊息：Redis-2.8，Redis-4.0，CKV
        :type EngineName: str
        :param AutoRenew: 續約模式：0 - 預設狀态（手動續約）；1 - 自動續約；2 - 明确不自動續約
        :type AutoRenew: list of int
        :param BillingMode: 計費模式：postpaid-按量計費；prepaid-包年包月
        :type BillingMode: str
        :param Type: 實例類型：1-Redis老集群版；2-Redis 2.8主從版；3-CKV主從版；4-CKV集群版；5-Redis 2.8單機版；7-Redis 4.0集群版
        :type Type: int
        :param SearchKeys: 搜索關鍵詞：支援實例Id、實例名稱、完整IP
        :type SearchKeys: list of str
        """
        self.Limit = None
        self.Offset = None
        self.InstanceId = None
        self.OrderBy = None
        self.OrderType = None
        self.VpcIds = None
        self.SubnetIds = None
        self.ProjectIds = None
        self.SearchKey = None
        self.InstanceName = None
        self.UniqVpcIds = None
        self.UniqSubnetIds = None
        self.RegionIds = None
        self.Status = None
        self.TypeVersion = None
        self.EngineName = None
        self.AutoRenew = None
        self.BillingMode = None
        self.Type = None
        self.SearchKeys = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.InstanceId = params.get("InstanceId")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.VpcIds = params.get("VpcIds")
        self.SubnetIds = params.get("SubnetIds")
        self.ProjectIds = params.get("ProjectIds")
        self.SearchKey = params.get("SearchKey")
        self.InstanceName = params.get("InstanceName")
        self.UniqVpcIds = params.get("UniqVpcIds")
        self.UniqSubnetIds = params.get("UniqSubnetIds")
        self.RegionIds = params.get("RegionIds")
        self.Status = params.get("Status")
        self.TypeVersion = params.get("TypeVersion")
        self.EngineName = params.get("EngineName")
        self.AutoRenew = params.get("AutoRenew")
        self.BillingMode = params.get("BillingMode")
        self.Type = params.get("Type")
        self.SearchKeys = params.get("SearchKeys")


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 實例數
        :type TotalCount: int
        :param InstanceSet: 實例詳細訊息清單
        :type InstanceSet: list of InstanceSet
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = InstanceSet()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProductInfoRequest(AbstractModel):
    """DescribeProductInfo請求參數結構體

    """


class DescribeProductInfoResponse(AbstractModel):
    """DescribeProductInfo返回參數結構體

    """

    def __init__(self):
        """
        :param RegionSet: 地域售賣訊息
        :type RegionSet: list of RegionConf
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionSet") is not None:
            self.RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionConf()
                obj._deserialize(item)
                self.RegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupRequest(AbstractModel):
    """DescribeProjectSecurityGroup請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: 0:預設項目；-1 所有項目; >0: 特定項目
        :type ProjectId: int
        :param SecurityGroupId: 安全組Id
        :type SecurityGroupId: str
        """
        self.ProjectId = None
        self.SecurityGroupId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.SecurityGroupId = params.get("SecurityGroupId")


class DescribeProjectSecurityGroupResponse(AbstractModel):
    """DescribeProjectSecurityGroup返回參數結構體

    """

    def __init__(self):
        """
        :param SecurityGroupDetails: 項目安全組
        :type SecurityGroupDetails: list of SecurityGroupDetail
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SecurityGroupDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroupDetails") is not None:
            self.SecurityGroupDetails = []
            for item in params.get("SecurityGroupDetails"):
                obj = SecurityGroupDetail()
                obj._deserialize(item)
                self.SecurityGroupDetails.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskInfoRequest(AbstractModel):
    """DescribeTaskInfo請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class DescribeTaskInfoResponse(AbstractModel):
    """DescribeTaskInfo返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 任務狀态preparing:待執行，running：執行中，succeed：成功，failed：失敗，error 執行出錯
        :type Status: str
        :param StartTime: 任務開始時間
        :type StartTime: str
        :param TaskType: 任務類型
        :type TaskType: str
        :param InstanceId: 實例的ID
        :type InstanceId: str
        :param TaskMessage: 任務訊息，錯誤時顯示錯誤訊息。執行中與成功則爲空
        :type TaskMessage: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.StartTime = None
        self.TaskType = None
        self.InstanceId = None
        self.TaskMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        self.TaskType = params.get("TaskType")
        self.InstanceId = params.get("InstanceId")
        self.TaskMessage = params.get("TaskMessage")
        self.RequestId = params.get("RequestId")


class DestroyPostpaidInstanceRequest(AbstractModel):
    """DestroyPostpaidInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例Id
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DestroyPostpaidInstanceResponse(AbstractModel):
    """DestroyPostpaidInstance返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務Id
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DestroyPrepaidInstanceRequest(AbstractModel):
    """DestroyPrepaidInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例Id
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DestroyPrepaidInstanceResponse(AbstractModel):
    """DestroyPrepaidInstance返回參數結構體

    """

    def __init__(self):
        """
        :param DealId: 訂單Id
        :type DealId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class DisableReplicaReadonlyRequest(AbstractModel):
    """DisableReplicaReadonly請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例序号ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DisableReplicaReadonlyResponse(AbstractModel):
    """DisableReplicaReadonly返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 失敗:ERROR，成功:OK
        :type Status: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class EnableReplicaReadonlyRequest(AbstractModel):
    """EnableReplicaReadonly請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例序号ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class EnableReplicaReadonlyResponse(AbstractModel):
    """EnableReplicaReadonly返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 錯誤：ERROR，正确OK。
        :type Status: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class InstanceClusterNode(AbstractModel):
    """實例節點類型

    """

    def __init__(self):
        """
        :param Name: 節點名稱
        :type Name: str
        :param RunId: 實例運作時節點Id
        :type RunId: str
        :param Role: 集群角色：0-master；1-slave
        :type Role: int
        :param Status: 節點狀态：0-readwrite, 1-read, 2-backup
        :type Status: int
        :param Connected: 服務狀态：0-down；1-on
        :type Connected: int
        :param CreateTime: 節點創建時間
        :type CreateTime: str
        :param DownTime: 節點下線時間
        :type DownTime: str
        :param Slots: 節點slot分布
        :type Slots: str
        :param Keys: 節點key分布
        :type Keys: int
        :param Qps: 節點qps
        :type Qps: int
        :param QpsSlope: 節點qps傾斜度
        :type QpsSlope: float
        :param Storage: 節點儲存
        :type Storage: int
        :param StorageSlope: 節點儲存傾斜度
        :type StorageSlope: float
        """
        self.Name = None
        self.RunId = None
        self.Role = None
        self.Status = None
        self.Connected = None
        self.CreateTime = None
        self.DownTime = None
        self.Slots = None
        self.Keys = None
        self.Qps = None
        self.QpsSlope = None
        self.Storage = None
        self.StorageSlope = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.RunId = params.get("RunId")
        self.Role = params.get("Role")
        self.Status = params.get("Status")
        self.Connected = params.get("Connected")
        self.CreateTime = params.get("CreateTime")
        self.DownTime = params.get("DownTime")
        self.Slots = params.get("Slots")
        self.Keys = params.get("Keys")
        self.Qps = params.get("Qps")
        self.QpsSlope = params.get("QpsSlope")
        self.Storage = params.get("Storage")
        self.StorageSlope = params.get("StorageSlope")


class InstanceClusterShard(AbstractModel):
    """實例分片清單訊息

    """

    def __init__(self):
        """
        :param ShardName: 分片節點名稱
        :type ShardName: str
        :param ShardId: 分片節點Id
        :type ShardId: str
        :param Role: 角色
        :type Role: int
        :param Keys: Key數量
        :type Keys: int
        :param Slots: slot訊息
        :type Slots: str
        :param Storage: 使用容量
        :type Storage: int
        :param StorageSlope: 容量傾斜率
        :type StorageSlope: float
        :param Runid: 實例運作時節點Id
        :type Runid: str
        :param Connected: 服務狀态：0-down；1-on
        :type Connected: int
        """
        self.ShardName = None
        self.ShardId = None
        self.Role = None
        self.Keys = None
        self.Slots = None
        self.Storage = None
        self.StorageSlope = None
        self.Runid = None
        self.Connected = None


    def _deserialize(self, params):
        self.ShardName = params.get("ShardName")
        self.ShardId = params.get("ShardId")
        self.Role = params.get("Role")
        self.Keys = params.get("Keys")
        self.Slots = params.get("Slots")
        self.Storage = params.get("Storage")
        self.StorageSlope = params.get("StorageSlope")
        self.Runid = params.get("Runid")
        self.Connected = params.get("Connected")


class InstanceEnumParam(AbstractModel):
    """實例列舉類型參數描述

    """

    def __init__(self):
        """
        :param ParamName: 參數名
        :type ParamName: str
        :param ValueType: 參數類型：enum
        :type ValueType: str
        :param NeedRestart: 修改後是否需要重啓：true，false
        :type NeedRestart: str
        :param DefaultValue: 參數預設值
        :type DefaultValue: str
        :param CurrentValue: 當前運作參數值
        :type CurrentValue: str
        :param Tips: 參數說明
        :type Tips: str
        :param EnumValue: 參數可取值
        :type EnumValue: list of str
        """
        self.ParamName = None
        self.ValueType = None
        self.NeedRestart = None
        self.DefaultValue = None
        self.CurrentValue = None
        self.Tips = None
        self.EnumValue = None


    def _deserialize(self, params):
        self.ParamName = params.get("ParamName")
        self.ValueType = params.get("ValueType")
        self.NeedRestart = params.get("NeedRestart")
        self.DefaultValue = params.get("DefaultValue")
        self.CurrentValue = params.get("CurrentValue")
        self.Tips = params.get("Tips")
        self.EnumValue = params.get("EnumValue")


class InstanceIntegerParam(AbstractModel):
    """實例整型參數描述

    """

    def __init__(self):
        """
        :param ParamName: 參數名
        :type ParamName: str
        :param ValueType: 參數類型：integer
        :type ValueType: str
        :param NeedRestart: 修改後是否需要重啓：true，false
        :type NeedRestart: str
        :param DefaultValue: 參數預設值
        :type DefaultValue: str
        :param CurrentValue: 當前運作參數值
        :type CurrentValue: str
        :param Tips: 參數說明
        :type Tips: str
        :param Min: 參數最小值
        :type Min: str
        :param Max: 參數最大值
        :type Max: str
        """
        self.ParamName = None
        self.ValueType = None
        self.NeedRestart = None
        self.DefaultValue = None
        self.CurrentValue = None
        self.Tips = None
        self.Min = None
        self.Max = None


    def _deserialize(self, params):
        self.ParamName = params.get("ParamName")
        self.ValueType = params.get("ValueType")
        self.NeedRestart = params.get("NeedRestart")
        self.DefaultValue = params.get("DefaultValue")
        self.CurrentValue = params.get("CurrentValue")
        self.Tips = params.get("Tips")
        self.Min = params.get("Min")
        self.Max = params.get("Max")


class InstanceNode(AbstractModel):
    """實例節點

    """

    def __init__(self):
        """
        :param Id: Id
        :type Id: int
        :param InstanceClusterNode: 節點詳細訊息
        :type InstanceClusterNode: list of InstanceClusterNode
        """
        self.Id = None
        self.InstanceClusterNode = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        if params.get("InstanceClusterNode") is not None:
            self.InstanceClusterNode = []
            for item in params.get("InstanceClusterNode"):
                obj = InstanceClusterNode()
                obj._deserialize(item)
                self.InstanceClusterNode.append(obj)


class InstanceParam(AbstractModel):
    """實例參數

    """

    def __init__(self):
        """
        :param Key: 設置參數的名字
        :type Key: str
        :param Value: 設置參數的值
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class InstanceParamHistory(AbstractModel):
    """實例參數修改曆史

    """

    def __init__(self):
        """
        :param ParamName: 參數名稱
        :type ParamName: str
        :param PreValue: 修改前值
        :type PreValue: str
        :param NewValue: 修改後值
        :type NewValue: str
        :param Status: 狀态：1-參數配置修改中；2-參數配置修改成功；3-參數配置修改失敗
        :type Status: int
        :param ModifyTime: 修改時間
        :type ModifyTime: str
        """
        self.ParamName = None
        self.PreValue = None
        self.NewValue = None
        self.Status = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.ParamName = params.get("ParamName")
        self.PreValue = params.get("PreValue")
        self.NewValue = params.get("NewValue")
        self.Status = params.get("Status")
        self.ModifyTime = params.get("ModifyTime")


class InstanceSecurityGroupDetail(AbstractModel):
    """實例安全組訊息

    """

    def __init__(self):
        """
        :param InstanceId: 實例Id
        :type InstanceId: str
        :param SecurityGroupDetails: 安全組訊息
        :type SecurityGroupDetails: list of SecurityGroupDetail
        """
        self.InstanceId = None
        self.SecurityGroupDetails = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("SecurityGroupDetails") is not None:
            self.SecurityGroupDetails = []
            for item in params.get("SecurityGroupDetails"):
                obj = SecurityGroupDetail()
                obj._deserialize(item)
                self.SecurityGroupDetails.append(obj)


class InstanceSet(AbstractModel):
    """實例詳細訊息清單

    """

    def __init__(self):
        """
        :param InstanceName: 實例名稱
        :type InstanceName: str
        :param InstanceId: 實例Id
        :type InstanceId: str
        :param Appid: 用戶的Appid
        :type Appid: int
        :param ProjectId: 項目Id
        :type ProjectId: int
        :param RegionId: 地域id 1--  4--  5--   6--多倫多 7-- 金融 8--  9-- 新加坡 11-- 金融 15--美西（矽谷）16--  17--德國 18--韓國 19--  21--印度 22--美東（弗吉尼亞）23--泰國 24--俄羅斯 25--日本
        :type RegionId: int
        :param ZoneId: 區域id
        :type ZoneId: int
        :param VpcId: vpc網絡id 如：75101
        :type VpcId: int
        :param SubnetId: vpc網絡下子網id 如：46315
        :type SubnetId: int
        :param Status: 實例當前狀态，0：待初始化；1：實例在流程中；2：實例運作中；-2：實例已隔離；-3：實例待删除
        :type Status: int
        :param WanIp: 實例vip
        :type WanIp: str
        :param Port: 實例端口号
        :type Port: int
        :param Createtime: 實例創建時間
        :type Createtime: str
        :param Size: 實例容量大小，單位：MB
        :type Size: float
        :param SizeUsed: 該欄位已廢棄
        :type SizeUsed: float
        :param Type: 實例類型，1：Redis2.8集群版；2：Redis2.8主從版；3：CKV主從版（Redis3.2）；4：CKV集群版（Redis3.2）；5：Redis2.8單機版；7：Redis4.0集群版；
        :type Type: int
        :param AutoRenewFlag: 實例是否設置自動續約标識，1：設置自動續約；0：未設置自動續約
        :type AutoRenewFlag: int
        :param DeadlineTime: 實例到期時間
        :type DeadlineTime: str
        :param Engine: 引擎：社區版Redis、Top Cloud CKV
        :type Engine: str
        :param ProductType: 産品類型：Redis2.8集群版、Redis2.8主從版、Redis3.2主從版（CKV主從版）、Redis3.2集群版（CKV集群版）、Redis2.8單機版、Redis4.0集群版
        :type ProductType: str
        :param UniqVpcId: vpc網絡id 如：vpc-fk33jsf43kgv
        :type UniqVpcId: str
        :param UniqSubnetId: vpc網絡下子網id 如：subnet-fd3j6l35mm0
        :type UniqSubnetId: str
        :param BillingMode: 計費模式：0-按量計費，1-包年包月
        :type BillingMode: int
        :param InstanceTitle: 實例運作狀态描述：如”實例運作中“
        :type InstanceTitle: str
        :param OfflineTime: 計劃下線時間
        :type OfflineTime: str
        :param SubStatus: 流程中的實例，返回子狀态
        :type SubStatus: int
        :param Tags: 反親和性标簽
        :type Tags: list of str
        :param InstanceNode: 實例節點訊息
        :type InstanceNode: list of InstanceNode
        :param RedisShardSize: 分片大小
        :type RedisShardSize: int
        :param RedisShardNum: 分片數量
        :type RedisShardNum: int
        :param RedisReplicasNum: 副本數量
        :type RedisReplicasNum: int
        :param PriceId: 計費Id
        :type PriceId: int
        :param CloseTime: 隔離時間
        :type CloseTime: str
        :param SlaveReadWeight: 從節點讀取權重
        :type SlaveReadWeight: int
        :param InstanceTags: 實例關聯的标簽訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceTags: list of InstanceTagInfo
        :param ProjectName: 項目名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProjectName: str
        """
        self.InstanceName = None
        self.InstanceId = None
        self.Appid = None
        self.ProjectId = None
        self.RegionId = None
        self.ZoneId = None
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.WanIp = None
        self.Port = None
        self.Createtime = None
        self.Size = None
        self.SizeUsed = None
        self.Type = None
        self.AutoRenewFlag = None
        self.DeadlineTime = None
        self.Engine = None
        self.ProductType = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.BillingMode = None
        self.InstanceTitle = None
        self.OfflineTime = None
        self.SubStatus = None
        self.Tags = None
        self.InstanceNode = None
        self.RedisShardSize = None
        self.RedisShardNum = None
        self.RedisReplicasNum = None
        self.PriceId = None
        self.CloseTime = None
        self.SlaveReadWeight = None
        self.InstanceTags = None
        self.ProjectName = None


    def _deserialize(self, params):
        self.InstanceName = params.get("InstanceName")
        self.InstanceId = params.get("InstanceId")
        self.Appid = params.get("Appid")
        self.ProjectId = params.get("ProjectId")
        self.RegionId = params.get("RegionId")
        self.ZoneId = params.get("ZoneId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.WanIp = params.get("WanIp")
        self.Port = params.get("Port")
        self.Createtime = params.get("Createtime")
        self.Size = params.get("Size")
        self.SizeUsed = params.get("SizeUsed")
        self.Type = params.get("Type")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.DeadlineTime = params.get("DeadlineTime")
        self.Engine = params.get("Engine")
        self.ProductType = params.get("ProductType")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.BillingMode = params.get("BillingMode")
        self.InstanceTitle = params.get("InstanceTitle")
        self.OfflineTime = params.get("OfflineTime")
        self.SubStatus = params.get("SubStatus")
        self.Tags = params.get("Tags")
        if params.get("InstanceNode") is not None:
            self.InstanceNode = []
            for item in params.get("InstanceNode"):
                obj = InstanceNode()
                obj._deserialize(item)
                self.InstanceNode.append(obj)
        self.RedisShardSize = params.get("RedisShardSize")
        self.RedisShardNum = params.get("RedisShardNum")
        self.RedisReplicasNum = params.get("RedisReplicasNum")
        self.PriceId = params.get("PriceId")
        self.CloseTime = params.get("CloseTime")
        self.SlaveReadWeight = params.get("SlaveReadWeight")
        if params.get("InstanceTags") is not None:
            self.InstanceTags = []
            for item in params.get("InstanceTags"):
                obj = InstanceTagInfo()
                obj._deserialize(item)
                self.InstanceTags.append(obj)
        self.ProjectName = params.get("ProjectName")


class InstanceTagInfo(AbstractModel):
    """實例标簽訊息

    """

    def __init__(self):
        """
        :param TagKey: 标簽鍵
        :type TagKey: str
        :param TagValue: 标簽值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class InstanceTextParam(AbstractModel):
    """實例字元型參數描述

    """

    def __init__(self):
        """
        :param ParamName: 參數名
        :type ParamName: str
        :param ValueType: 參數類型：text
        :type ValueType: str
        :param NeedRestart: 修改後是否需要重啓：true，false
        :type NeedRestart: str
        :param DefaultValue: 參數預設值
        :type DefaultValue: str
        :param CurrentValue: 當前運作參數值
        :type CurrentValue: str
        :param Tips: 參數說明
        :type Tips: str
        :param TextValue: 參數可取值
        :type TextValue: list of str
        """
        self.ParamName = None
        self.ValueType = None
        self.NeedRestart = None
        self.DefaultValue = None
        self.CurrentValue = None
        self.Tips = None
        self.TextValue = None


    def _deserialize(self, params):
        self.ParamName = params.get("ParamName")
        self.ValueType = params.get("ValueType")
        self.NeedRestart = params.get("NeedRestart")
        self.DefaultValue = params.get("DefaultValue")
        self.CurrentValue = params.get("CurrentValue")
        self.Tips = params.get("Tips")
        self.TextValue = params.get("TextValue")


class ManualBackupInstanceRequest(AbstractModel):
    """ManualBackupInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 待操作的實例ID，可通過 DescribeInstance介面返回值中的 InstanceId 獲取。
        :type InstanceId: str
        :param Remark: 備份的備注訊息
        :type Remark: str
        """
        self.InstanceId = None
        self.Remark = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Remark = params.get("Remark")


class ManualBackupInstanceResponse(AbstractModel):
    """ManualBackupInstance返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModfiyInstancePasswordRequest(AbstractModel):
    """ModfiyInstancePassword請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param OldPassword: 實例舊密碼
        :type OldPassword: str
        :param Password: 實例新密碼
        :type Password: str
        """
        self.InstanceId = None
        self.OldPassword = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.OldPassword = params.get("OldPassword")
        self.Password = params.get("Password")


class ModfiyInstancePasswordResponse(AbstractModel):
    """ModfiyInstancePassword返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyAutoBackupConfigRequest(AbstractModel):
    """ModifyAutoBackupConfig請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param WeekDays: 日期 Monday，Tuesday，Wednesday，Thursday，Friday，Saturday，Sunday
        :type WeekDays: list of str
        :param TimePeriod: 時間段 00:00-01:00, 01:00-02:00...... 23:00-00:00
        :type TimePeriod: str
        :param AutoBackupType: 自動備份類型： 1 “定時回檔”
        :type AutoBackupType: int
        """
        self.InstanceId = None
        self.WeekDays = None
        self.TimePeriod = None
        self.AutoBackupType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.WeekDays = params.get("WeekDays")
        self.TimePeriod = params.get("TimePeriod")
        self.AutoBackupType = params.get("AutoBackupType")


class ModifyAutoBackupConfigResponse(AbstractModel):
    """ModifyAutoBackupConfig返回參數結構體

    """

    def __init__(self):
        """
        :param AutoBackupType: 自動備份類型： 1 “定時回檔”
        :type AutoBackupType: int
        :param WeekDays: 日期Monday，Tuesday，Wednesday，Thursday，Friday，Saturday，Sunday。
        :type WeekDays: list of str
        :param TimePeriod: 時間段 00:00-01:00, 01:00-02:00...... 23:00-00:00
        :type TimePeriod: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AutoBackupType = None
        self.WeekDays = None
        self.TimePeriod = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AutoBackupType = params.get("AutoBackupType")
        self.WeekDays = params.get("WeekDays")
        self.TimePeriod = params.get("TimePeriod")
        self.RequestId = params.get("RequestId")


class ModifyInstanceParamsRequest(AbstractModel):
    """ModifyInstanceParams請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例Id
        :type InstanceId: str
        :param InstanceParams: 實例修改的參數清單
        :type InstanceParams: list of InstanceParam
        """
        self.InstanceId = None
        self.InstanceParams = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("InstanceParams") is not None:
            self.InstanceParams = []
            for item in params.get("InstanceParams"):
                obj = InstanceParam()
                obj._deserialize(item)
                self.InstanceParams.append(obj)


class ModifyInstanceParamsResponse(AbstractModel):
    """ModifyInstanceParams返回參數結構體

    """

    def __init__(self):
        """
        :param Changed: 修改是否成功。
        :type Changed: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Changed = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Changed = params.get("Changed")
        self.RequestId = params.get("RequestId")


class ModifyInstanceRequest(AbstractModel):
    """ModifyInstance請求參數結構體

    """

    def __init__(self):
        """
        :param Operation: 修改實例操作，如填寫：rename-表示實例重命名；modifyProject-修改實例所屬項目；modifyAutoRenew-修改實例續約标記
        :type Operation: str
        :param InstanceId: 實例Id
        :type InstanceId: str
        :param InstanceName: 實例的新名稱
        :type InstanceName: str
        :param ProjectId: 項目Id
        :type ProjectId: int
        :param AutoRenew: 自動續約标識。0 - 預設狀态（手動續約）；1 - 自動續約；2 - 明确不自動續約
        :type AutoRenew: int
        """
        self.Operation = None
        self.InstanceId = None
        self.InstanceName = None
        self.ProjectId = None
        self.AutoRenew = None


    def _deserialize(self, params):
        self.Operation = params.get("Operation")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.ProjectId = params.get("ProjectId")
        self.AutoRenew = params.get("AutoRenew")


class ModifyInstanceResponse(AbstractModel):
    """ModifyInstance返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNetworkConfigRequest(AbstractModel):
    """ModifyNetworkConfig請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param Operation: 操作類型：changeVip——修改實例VIP；changeVpc——修改實例子網；changeBaseToVpc——基礎網絡轉VPC網絡
        :type Operation: str
        :param Vip: VIP網址，changeVip的時候填寫，不填則預設分配
        :type Vip: str
        :param VpcId: 私有網絡ID，changeVpc、changeBaseToVpc的時候需要提供
        :type VpcId: str
        :param SubnetId: 子網ID，changeVpc、changeBaseToVpc的時候需要提供
        :type SubnetId: str
        """
        self.InstanceId = None
        self.Operation = None
        self.Vip = None
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Operation = params.get("Operation")
        self.Vip = params.get("Vip")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")


class ModifyNetworkConfigResponse(AbstractModel):
    """ModifyNetworkConfig返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 執行狀态：true|false
        :type Status: bool
        :param SubnetId: 子網ID
        :type SubnetId: str
        :param VpcId: 私有網絡ID
        :type VpcId: str
        :param Vip: VIP網址
        :type Vip: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.SubnetId = None
        self.VpcId = None
        self.Vip = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.SubnetId = params.get("SubnetId")
        self.VpcId = params.get("VpcId")
        self.Vip = params.get("Vip")
        self.RequestId = params.get("RequestId")


class ProductConf(AbstractModel):
    """産品訊息

    """

    def __init__(self):
        """
        :param Type: 産品類型，2-Redis主從版，3-CKV主從版，4-CKV集群版，5-Redis單機版，7-Redis集群版
        :type Type: int
        :param TypeName: 産品名稱，Redis主從版，CKV主從版，CKV集群版，Redis單機版，Redis集群版
        :type TypeName: str
        :param MinBuyNum: 購買時的最小數量
        :type MinBuyNum: int
        :param MaxBuyNum: 購買時的最大數量
        :type MaxBuyNum: int
        :param Saleout: 産品是否售罄
        :type Saleout: bool
        :param Engine: 産品引擎，Top Cloud CKV或者社區版Redis
        :type Engine: str
        :param Version: 兼容版本，Redis-2.8，Redis-3.2，Redis-4.0
        :type Version: str
        :param TotalSize: 規格總大小，單位G
        :type TotalSize: list of str
        :param ShardSize: 每個分片大小，單位G
        :type ShardSize: list of str
        :param ReplicaNum: 副本數量
        :type ReplicaNum: list of str
        :param ShardNum: 分片數量
        :type ShardNum: list of str
        :param PayMode: 支援的計費模式，1-包年包月，0-按量計費
        :type PayMode: str
        :param EnableRepicaReadOnly: 是否支援副本只讀
        :type EnableRepicaReadOnly: bool
        """
        self.Type = None
        self.TypeName = None
        self.MinBuyNum = None
        self.MaxBuyNum = None
        self.Saleout = None
        self.Engine = None
        self.Version = None
        self.TotalSize = None
        self.ShardSize = None
        self.ReplicaNum = None
        self.ShardNum = None
        self.PayMode = None
        self.EnableRepicaReadOnly = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.TypeName = params.get("TypeName")
        self.MinBuyNum = params.get("MinBuyNum")
        self.MaxBuyNum = params.get("MaxBuyNum")
        self.Saleout = params.get("Saleout")
        self.Engine = params.get("Engine")
        self.Version = params.get("Version")
        self.TotalSize = params.get("TotalSize")
        self.ShardSize = params.get("ShardSize")
        self.ReplicaNum = params.get("ReplicaNum")
        self.ShardNum = params.get("ShardNum")
        self.PayMode = params.get("PayMode")
        self.EnableRepicaReadOnly = params.get("EnableRepicaReadOnly")


class RedisBackupSet(AbstractModel):
    """實例的備份數組

    """

    def __init__(self):
        """
        :param StartTime: 開始備份的時間
        :type StartTime: str
        :param BackupId: 備份ID
        :type BackupId: str
        :param BackupType: 備份類型。 manualBackupInstance：用戶發起的手動備份； systemBackupInstance：淩晨系統發起的備份
        :type BackupType: str
        :param Status: 備份狀态。  1:"備份被其它流程鎖定";  2:"備份正常，沒有被任何流程鎖定";  -1:"備份已過期"； 3:"備份正在被導出";  4:"備份導出成功"
        :type Status: int
        :param Remark: 備份的備注訊息
        :type Remark: str
        :param Locked: 備份是否被鎖定，0：未被鎖定；1：已被鎖定
        :type Locked: int
        """
        self.StartTime = None
        self.BackupId = None
        self.BackupType = None
        self.Status = None
        self.Remark = None
        self.Locked = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.BackupId = params.get("BackupId")
        self.BackupType = params.get("BackupType")
        self.Status = params.get("Status")
        self.Remark = params.get("Remark")
        self.Locked = params.get("Locked")


class RegionConf(AbstractModel):
    """地域訊息

    """

    def __init__(self):
        """
        :param RegionId: 地域ID
        :type RegionId: str
        :param RegionName: 地域名稱
        :type RegionName: str
        :param RegionShortName: 地域簡稱
        :type RegionShortName: str
        :param Area: 地域所在大區名稱
        :type Area: str
        :param ZoneSet: 可用區訊息
        :type ZoneSet: list of ZoneCapacityConf
        """
        self.RegionId = None
        self.RegionName = None
        self.RegionShortName = None
        self.Area = None
        self.ZoneSet = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        self.RegionShortName = params.get("RegionShortName")
        self.Area = params.get("Area")
        if params.get("ZoneSet") is not None:
            self.ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = ZoneCapacityConf()
                obj._deserialize(item)
                self.ZoneSet.append(obj)


class RenewInstanceRequest(AbstractModel):
    """RenewInstance請求參數結構體

    """

    def __init__(self):
        """
        :param Period: 購買時長，單位：月
        :type Period: int
        :param InstanceId: 實例ID
        :type InstanceId: str
        """
        self.Period = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.InstanceId = params.get("InstanceId")


class RenewInstanceResponse(AbstractModel):
    """RenewInstance返回參數結構體

    """

    def __init__(self):
        """
        :param DealId: 交易Id
        :type DealId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class ResetPasswordRequest(AbstractModel):
    """ResetPassword請求參數結構體

    """

    def __init__(self):
        """
        :param Password: 重置的密碼
        :type Password: str
        :param InstanceId: Redis實例ID
        :type InstanceId: str
        """
        self.Password = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Password = params.get("Password")
        self.InstanceId = params.get("InstanceId")


class ResetPasswordResponse(AbstractModel):
    """ResetPassword返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class RestoreInstanceRequest(AbstractModel):
    """RestoreInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 待操作的實例ID，可通過 DescribeRedis 介面返回值中的 redisId 獲取。
        :type InstanceId: str
        :param Password: 實例密碼，恢複實例時，需要校驗實例密碼
        :type Password: str
        :param BackupId: 備份ID，可通過 GetRedisBackupList 介面返回值中的 backupId 獲取
        :type BackupId: str
        """
        self.InstanceId = None
        self.Password = None
        self.BackupId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Password = params.get("Password")
        self.BackupId = params.get("BackupId")


class RestoreInstanceResponse(AbstractModel):
    """RestoreInstance返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID，可通過 DescribeTaskInfo 介面查詢任務執行狀态
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class SecurityGroupDetail(AbstractModel):
    """安全組詳情

    """

    def __init__(self):
        """
        :param ProjectId: 項目Id
        :type ProjectId: int
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param SecurityGroupId: 安全組Id
        :type SecurityGroupId: str
        :param SecurityGroupName: 安全組名稱
        :type SecurityGroupName: str
        :param SecurityGroupRemark: 安全組标記
        :type SecurityGroupRemark: str
        :param InboundRule: 安全組入站規則
        :type InboundRule: list of SecurityGroupsInboundAndOutbound
        :param OutboundRule: 安全組出站規則
        :type OutboundRule: list of SecurityGroupsInboundAndOutbound
        """
        self.ProjectId = None
        self.CreateTime = None
        self.SecurityGroupId = None
        self.SecurityGroupName = None
        self.SecurityGroupRemark = None
        self.InboundRule = None
        self.OutboundRule = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.CreateTime = params.get("CreateTime")
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.SecurityGroupName = params.get("SecurityGroupName")
        self.SecurityGroupRemark = params.get("SecurityGroupRemark")
        if params.get("InboundRule") is not None:
            self.InboundRule = []
            for item in params.get("InboundRule"):
                obj = SecurityGroupsInboundAndOutbound()
                obj._deserialize(item)
                self.InboundRule.append(obj)
        if params.get("OutboundRule") is not None:
            self.OutboundRule = []
            for item in params.get("OutboundRule"):
                obj = SecurityGroupsInboundAndOutbound()
                obj._deserialize(item)
                self.OutboundRule.append(obj)


class SecurityGroupsInboundAndOutbound(AbstractModel):
    """安全組出入規則

    """

    def __init__(self):
        """
        :param Action: 執行動作
        :type Action: str
        :param Ip: IP網址
        :type Ip: str
        :param Port: 端口号
        :type Port: str
        :param Proto: 協議類型
        :type Proto: str
        """
        self.Action = None
        self.Ip = None
        self.Port = None
        self.Proto = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.Proto = params.get("Proto")


class TradeDealDetail(AbstractModel):
    """訂單交易訊息

    """

    def __init__(self):
        """
        :param DealId: 訂單号ID，調用雲API時使用此ID
        :type DealId: str
        :param DealName: 長訂單ID，反饋訂單問題給官方客服使用此ID
        :type DealName: str
        :param ZoneId: 可用區id
        :type ZoneId: int
        :param GoodsNum: 訂單關聯的實例數
        :type GoodsNum: int
        :param Creater: 創建用戶uin
        :type Creater: str
        :param CreatTime: 訂單創建時間
        :type CreatTime: str
        :param OverdueTime: 訂單超時時間
        :type OverdueTime: str
        :param EndTime: 訂單完成時間
        :type EndTime: str
        :param Status: 訂單狀态 1：未支付 2:已支付，未發貨 3:發貨中 4:發貨成功 5:發貨失敗 6:已退款 7:已關閉訂單 8:訂單過期 9:訂單已失效 10:産品已失效 11:代付拒絕 12:支付中
        :type Status: int
        :param Description: 訂單狀态描述
        :type Description: str
        :param Price: 訂單實際總價，單位：分
        :type Price: int
        :param InstanceIds: 實例ID
        :type InstanceIds: list of str
        """
        self.DealId = None
        self.DealName = None
        self.ZoneId = None
        self.GoodsNum = None
        self.Creater = None
        self.CreatTime = None
        self.OverdueTime = None
        self.EndTime = None
        self.Status = None
        self.Description = None
        self.Price = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.DealName = params.get("DealName")
        self.ZoneId = params.get("ZoneId")
        self.GoodsNum = params.get("GoodsNum")
        self.Creater = params.get("Creater")
        self.CreatTime = params.get("CreatTime")
        self.OverdueTime = params.get("OverdueTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        self.Description = params.get("Description")
        self.Price = params.get("Price")
        self.InstanceIds = params.get("InstanceIds")


class UpgradeInstanceRequest(AbstractModel):
    """UpgradeInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例Id
        :type InstanceId: str
        :param MemSize: 分片大小 單位 MB
        :type MemSize: int
        :param RedisShardNum: 分片數量，Redis2.8主從版、CKV主從版和Redis2.8單機版不需要填寫
        :type RedisShardNum: int
        :param RedisReplicasNum: 副本數量，Redis2.8主從版、CKV主從版和Redis2.8單機版不需要填寫
        :type RedisReplicasNum: int
        """
        self.InstanceId = None
        self.MemSize = None
        self.RedisShardNum = None
        self.RedisReplicasNum = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.MemSize = params.get("MemSize")
        self.RedisShardNum = params.get("RedisShardNum")
        self.RedisReplicasNum = params.get("RedisReplicasNum")


class UpgradeInstanceResponse(AbstractModel):
    """UpgradeInstance返回參數結構體

    """

    def __init__(self):
        """
        :param DealId: 訂單ID
        :type DealId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class ZoneCapacityConf(AbstractModel):
    """可用區内産品訊息

    """

    def __init__(self):
        """
        :param ZoneId: 可用區ID：如ap-guangzhou-3
        :type ZoneId: str
        :param ZoneName: 可用區名稱
        :type ZoneName: str
        :param IsSaleout: 可用區是否售罄
        :type IsSaleout: bool
        :param IsDefault: 是否爲預設可用區
        :type IsDefault: bool
        :param NetWorkType: 網絡類型：basenet -- 基礎網絡；vpcnet -- VPC網絡
        :type NetWorkType: list of str
        :param ProductSet: 可用區内産品規格等訊息
        :type ProductSet: list of ProductConf
        :param OldZoneId: 可用區ID：如100003
        :type OldZoneId: int
        """
        self.ZoneId = None
        self.ZoneName = None
        self.IsSaleout = None
        self.IsDefault = None
        self.NetWorkType = None
        self.ProductSet = None
        self.OldZoneId = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.IsSaleout = params.get("IsSaleout")
        self.IsDefault = params.get("IsDefault")
        self.NetWorkType = params.get("NetWorkType")
        if params.get("ProductSet") is not None:
            self.ProductSet = []
            for item in params.get("ProductSet"):
                obj = ProductConf()
                obj._deserialize(item)
                self.ProductSet.append(obj)
        self.OldZoneId = params.get("OldZoneId")