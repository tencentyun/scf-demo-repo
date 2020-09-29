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


class ActivateSubscribeRequest(AbstractModel):
    """ActivateSubscribe請求參數結構體

    """

    def __init__(self):
        """
        :param SubscribeId: 訂閱實例ID。
        :type SubscribeId: str
        :param InstanceId: 資料庫實例ID
        :type InstanceId: str
        :param SubscribeObjectType: 數據訂閱類型0-全實例訂閱，1數據訂閱，2結構訂閱，3數據訂閱與結構訂閱
        :type SubscribeObjectType: int
        :param Objects: 訂閱對象
        :type Objects: :class:`taifucloudcloud.dts.v20180330.models.SubscribeObject`
        :param UniqSubnetId: 數據訂閱服務所在子網。預設爲資料庫實例所在的子網内。
        :type UniqSubnetId: str
        :param Vport: 訂閱服務端口；預設爲7507
        :type Vport: int
        """
        self.SubscribeId = None
        self.InstanceId = None
        self.SubscribeObjectType = None
        self.Objects = None
        self.UniqSubnetId = None
        self.Vport = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.InstanceId = params.get("InstanceId")
        self.SubscribeObjectType = params.get("SubscribeObjectType")
        if params.get("Objects") is not None:
            self.Objects = SubscribeObject()
            self.Objects._deserialize(params.get("Objects"))
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.Vport = params.get("Vport")


class ActivateSubscribeResponse(AbstractModel):
    """ActivateSubscribe返回參數結構體

    """

    def __init__(self):
        """
        :param AsyncRequestId: 配置數據訂閱任務ID。
        :type AsyncRequestId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class CompleteMigrateJobRequest(AbstractModel):
    """CompleteMigrateJob請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 數據遷移任務ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class CompleteMigrateJobResponse(AbstractModel):
    """CompleteMigrateJob返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ConsistencyParams(AbstractModel):
    """抽樣檢驗時的抽樣參數

    """

    def __init__(self):
        """
        :param SelectRowsPerTable: 數據内容檢測參數。表中選出用來數據對比的行，占表的總行數的百分比。取值範圍是整數[1-100]
        :type SelectRowsPerTable: int
        :param TablesSelectAll: 數據内容檢測參數。遷移庫表中，要進行數據内容檢測的表，占所有表的百分比。取值範圍是整數[1-100]
        :type TablesSelectAll: int
        :param TablesSelectCount: 數據數量檢測，檢測表行數是否一緻。遷移庫表中，要進行數據數量檢測的表，占所有表的百分比。取值範圍是整數[1-100]
        :type TablesSelectCount: int
        """
        self.SelectRowsPerTable = None
        self.TablesSelectAll = None
        self.TablesSelectCount = None


    def _deserialize(self, params):
        self.SelectRowsPerTable = params.get("SelectRowsPerTable")
        self.TablesSelectAll = params.get("TablesSelectAll")
        self.TablesSelectCount = params.get("TablesSelectCount")


class CreateMigrateCheckJobRequest(AbstractModel):
    """CreateMigrateCheckJob請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 數據遷移任務ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class CreateMigrateCheckJobResponse(AbstractModel):
    """CreateMigrateCheckJob返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateMigrateJobRequest(AbstractModel):
    """CreateMigrateJob請求參數結構體

    """

    def __init__(self):
        """
        :param JobName: 數據遷移任務名稱
        :type JobName: str
        :param MigrateOption: 遷移任務配置選項
        :type MigrateOption: :class:`taifucloudcloud.dts.v20180330.models.MigrateOption`
        :param SrcDatabaseType: 源實例資料庫類型，目前支援：mysql，redis，mongodb，postgresql，mariadb，percona。不同地域資料庫類型的具體支援情況，請參考控制台創建遷移頁面。
        :type SrcDatabaseType: str
        :param SrcAccessType: 源實例接入類型，值包括：extranet(外網),cvm(CVM自建實例),dcg(專線接入的實例),vpncloud(雲VPN接入的實例),cdb(Top Cloud 資料庫實例),ccn(雲聯網實例)
        :type SrcAccessType: str
        :param SrcInfo: 源實例訊息，具體内容跟遷移任務類型相關
        :type SrcInfo: :class:`taifucloudcloud.dts.v20180330.models.SrcInfo`
        :param DstDatabaseType: 目標實例資料庫類型，目前支援：mysql，redis，mongodb，postgresql，mariadb，percona。不同地域資料庫類型的具體支援情況，請參考控制台創建遷移頁面。
        :type DstDatabaseType: str
        :param DstAccessType: 目標實例接入類型，目前支援：cdb（Top Cloud 資料庫實例）
        :type DstAccessType: str
        :param DstInfo: 目標實例訊息
        :type DstInfo: :class:`taifucloudcloud.dts.v20180330.models.DstInfo`
        :param DatabaseInfo: 需要遷移的源資料庫表訊息，用json格式的字串描述。當MigrateOption.MigrateObject配置爲2（指定庫表遷移）時必填。
對於database-table兩級結構的資料庫：
[{Database:db1,Table:[table1,table2]},{Database:db2}]
對於database-schema-table三級結構：
[{Database:db1,Schema:s1
Table:[table1,table2]},{Database:db1,Schema:s2
Table:[table1,table2]},{Database:db2,Schema:s1
Table:[table1,table2]},{Database:db3},{Database:db4
Schema:s1}]
        :type DatabaseInfo: str
        """
        self.JobName = None
        self.MigrateOption = None
        self.SrcDatabaseType = None
        self.SrcAccessType = None
        self.SrcInfo = None
        self.DstDatabaseType = None
        self.DstAccessType = None
        self.DstInfo = None
        self.DatabaseInfo = None


    def _deserialize(self, params):
        self.JobName = params.get("JobName")
        if params.get("MigrateOption") is not None:
            self.MigrateOption = MigrateOption()
            self.MigrateOption._deserialize(params.get("MigrateOption"))
        self.SrcDatabaseType = params.get("SrcDatabaseType")
        self.SrcAccessType = params.get("SrcAccessType")
        if params.get("SrcInfo") is not None:
            self.SrcInfo = SrcInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        self.DstDatabaseType = params.get("DstDatabaseType")
        self.DstAccessType = params.get("DstAccessType")
        if params.get("DstInfo") is not None:
            self.DstInfo = DstInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        self.DatabaseInfo = params.get("DatabaseInfo")


class CreateMigrateJobResponse(AbstractModel):
    """CreateMigrateJob返回參數結構體

    """

    def __init__(self):
        """
        :param JobId: 數據遷移任務ID
        :type JobId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class CreateSubscribeRequest(AbstractModel):
    """CreateSubscribe請求參數結構體

    """

    def __init__(self):
        """
        :param Product: 訂閱的資料庫類型，目前支援的有 mysql
        :type Product: str
        :param PayType: 實例付費類型，1小時計費，0包年包月
        :type PayType: int
        :param Duration: 購買時長。PayType爲0時必填。單位爲月，最大支援120
        :type Duration: int
        :param Count: 購買數量,預設爲1，最大爲10
        :type Count: int
        :param AutoRenew: 是否自動續約，預設爲0，1表示自動續約。小時計費實例設置該標識無效。
        :type AutoRenew: int
        """
        self.Product = None
        self.PayType = None
        self.Duration = None
        self.Count = None
        self.AutoRenew = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.PayType = params.get("PayType")
        self.Duration = params.get("Duration")
        self.Count = params.get("Count")
        self.AutoRenew = params.get("AutoRenew")


class CreateSubscribeResponse(AbstractModel):
    """CreateSubscribe返回參數結構體

    """

    def __init__(self):
        """
        :param SubscribeIds: 數據訂閱實例的ID數組
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubscribeIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SubscribeIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubscribeIds = params.get("SubscribeIds")
        self.RequestId = params.get("RequestId")


class CreateSyncCheckJobRequest(AbstractModel):
    """CreateSyncCheckJob請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 災備同步任務ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class CreateSyncCheckJobResponse(AbstractModel):
    """CreateSyncCheckJob返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSyncJobRequest(AbstractModel):
    """CreateSyncJob請求參數結構體

    """

    def __init__(self):
        """
        :param JobName: 災備同步任務名
        :type JobName: str
        :param SyncOption: 災備同步任務配置選項
        :type SyncOption: :class:`taifucloudcloud.dts.v20180330.models.SyncOption`
        :param SrcDatabaseType: 源實例資料庫類型，目前僅包括：mysql
        :type SrcDatabaseType: str
        :param SrcAccessType: 源實例接入類型，目前僅包括：cdb(雲上cdb實例)
        :type SrcAccessType: str
        :param SrcInfo: 源實例訊息
        :type SrcInfo: :class:`taifucloudcloud.dts.v20180330.models.SyncInstanceInfo`
        :param DstDatabaseType: 目標實例資料庫類型，目前僅包括：mysql
        :type DstDatabaseType: str
        :param DstAccessType: 目標實例接入類型，目前僅包括：cdb(雲上cdb實例)
        :type DstAccessType: str
        :param DstInfo: 目標實例訊息
        :type DstInfo: :class:`taifucloudcloud.dts.v20180330.models.SyncInstanceInfo`
        :param DatabaseInfo: 需要同步的源資料庫表訊息，用json格式的字串描述。
對於database-table兩級結構的資料庫：
[{Database:db1,Table:[table1,table2]},{Database:db2}]
        :type DatabaseInfo: str
        """
        self.JobName = None
        self.SyncOption = None
        self.SrcDatabaseType = None
        self.SrcAccessType = None
        self.SrcInfo = None
        self.DstDatabaseType = None
        self.DstAccessType = None
        self.DstInfo = None
        self.DatabaseInfo = None


    def _deserialize(self, params):
        self.JobName = params.get("JobName")
        if params.get("SyncOption") is not None:
            self.SyncOption = SyncOption()
            self.SyncOption._deserialize(params.get("SyncOption"))
        self.SrcDatabaseType = params.get("SrcDatabaseType")
        self.SrcAccessType = params.get("SrcAccessType")
        if params.get("SrcInfo") is not None:
            self.SrcInfo = SyncInstanceInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        self.DstDatabaseType = params.get("DstDatabaseType")
        self.DstAccessType = params.get("DstAccessType")
        if params.get("DstInfo") is not None:
            self.DstInfo = SyncInstanceInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        self.DatabaseInfo = params.get("DatabaseInfo")


class CreateSyncJobResponse(AbstractModel):
    """CreateSyncJob返回參數結構體

    """

    def __init__(self):
        """
        :param JobId: 災備同步任務ID
        :type JobId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class DeleteMigrateJobRequest(AbstractModel):
    """DeleteMigrateJob請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 數據遷移任務ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class DeleteMigrateJobResponse(AbstractModel):
    """DeleteMigrateJob返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSyncJobRequest(AbstractModel):
    """DeleteSyncJob請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 待删除的災備同步任務ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class DeleteSyncJobResponse(AbstractModel):
    """DeleteSyncJob返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAsyncRequestInfoRequest(AbstractModel):
    """DescribeAsyncRequestInfo請求參數結構體

    """

    def __init__(self):
        """
        :param AsyncRequestId: 任務 ID
        :type AsyncRequestId: str
        """
        self.AsyncRequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")


class DescribeAsyncRequestInfoResponse(AbstractModel):
    """DescribeAsyncRequestInfo返回參數結構體

    """

    def __init__(self):
        """
        :param Info: 任務執行結果訊息
        :type Info: str
        :param Status: 任務執行狀态，可能的值有：success，failed，running
        :type Status: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Info = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Info = params.get("Info")
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeMigrateCheckJobRequest(AbstractModel):
    """DescribeMigrateCheckJob請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 數據遷移任務ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class DescribeMigrateCheckJobResponse(AbstractModel):
    """DescribeMigrateCheckJob返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 校驗任務狀态：unavailable(當前不可用), starting(開始中)，running(校驗中)，finished(校驗完成)
        :type Status: str
        :param ErrorCode: 任務的錯誤碼
        :type ErrorCode: int
        :param ErrorMessage: 任務的錯誤訊息
        :type ErrorMessage: str
        :param Progress: Check任務總進度,如："30"表示30%
        :type Progress: str
        :param CheckFlag: 校驗是否通過,0-未通過，1-校驗通過, 3-未校驗
        :type CheckFlag: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.ErrorCode = None
        self.ErrorMessage = None
        self.Progress = None
        self.CheckFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrorCode = params.get("ErrorCode")
        self.ErrorMessage = params.get("ErrorMessage")
        self.Progress = params.get("Progress")
        self.CheckFlag = params.get("CheckFlag")
        self.RequestId = params.get("RequestId")


class DescribeMigrateJobsRequest(AbstractModel):
    """DescribeMigrateJobs請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 數據遷移任務ID
        :type JobId: str
        :param JobName: 數據遷移任務名稱
        :type JobName: str
        :param Order: 排序欄位，可以取值爲JobId、Status、JobName、MigrateType、RunMode、CreateTime
        :type Order: str
        :param OrderSeq: 排序方式，升序爲ASC，降序爲DESC
        :type OrderSeq: str
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 返回實例數量，預設20，有效區間[1,100]
        :type Limit: int
        """
        self.JobId = None
        self.JobName = None
        self.Order = None
        self.OrderSeq = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.Order = params.get("Order")
        self.OrderSeq = params.get("OrderSeq")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeMigrateJobsResponse(AbstractModel):
    """DescribeMigrateJobs返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 任務數目
        :type TotalCount: int
        :param JobList: 任務詳情數組
        :type JobList: list of MigrateJobInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.JobList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("JobList") is not None:
            self.JobList = []
            for item in params.get("JobList"):
                obj = MigrateJobInfo()
                obj._deserialize(item)
                self.JobList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRegionConfRequest(AbstractModel):
    """DescribeRegionConf請求參數結構體

    """


class DescribeRegionConfResponse(AbstractModel):
    """DescribeRegionConf返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 可售賣地域的數量
        :type TotalCount: int
        :param Items: 可售賣地域詳情
        :type Items: list of SubscribeRegionConf
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = SubscribeRegionConf()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSubscribeConfRequest(AbstractModel):
    """DescribeSubscribeConf請求參數結構體

    """

    def __init__(self):
        """
        :param SubscribeId: 訂閱實例ID
        :type SubscribeId: str
        """
        self.SubscribeId = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")


class DescribeSubscribeConfResponse(AbstractModel):
    """DescribeSubscribeConf返回參數結構體

    """

    def __init__(self):
        """
        :param SubscribeId: 訂閱實例ID
        :type SubscribeId: str
        :param SubscribeName: 訂閱實例名稱
        :type SubscribeName: str
        :param ChannelId: 訂閱通道
        :type ChannelId: str
        :param Product: 訂閱資料庫類型
        :type Product: str
        :param InstanceId: 被訂閱的實例
        :type InstanceId: str
        :param InstanceStatus: 被訂閱的實例的狀态，可能的值有running,offline,isolate
        :type InstanceStatus: str
        :param SubsStatus: 訂閱實例狀态，可能的值有unconfigure-未配置，configuring-配置中，configured-已配置
        :type SubsStatus: str
        :param Status: 訂閱實例生命週期狀态，可能的值有：normal-正常，isolating-隔離中，isolated-已隔離，offlining-下線中
        :type Status: str
        :param CreateTime: 訂閱實例創建時間
        :type CreateTime: str
        :param IsolateTime: 訂閱實例被隔離時間
        :type IsolateTime: str
        :param ExpireTime: 訂閱實例到期時間
        :type ExpireTime: str
        :param OfflineTime: 訂閱實例下線時間
        :type OfflineTime: str
        :param ConsumeStartTime: 訂閱實例消費時間起點。
        :type ConsumeStartTime: str
        :param PayType: 訂閱實例計費類型，1-小時計費，0-包年包月
        :type PayType: int
        :param Vip: 訂閱通道Vip
        :type Vip: str
        :param Vport: 訂閱通道Port
        :type Vport: int
        :param UniqVpcId: 訂閱通道所在VpcId
        :type UniqVpcId: str
        :param UniqSubnetId: 訂閱通道所在SubnetId
        :type UniqSubnetId: str
        :param SdkConsumedTime: 當前SDK消費時間位點
        :type SdkConsumedTime: str
        :param SdkHost: 訂閱SDK IP網址
        :type SdkHost: str
        :param SubscribeObjectType: 訂閱對象類型0-全實例訂閱，1-DDL數據訂閱，2-DML結構訂閱，3-DDL數據訂閱+DML結構訂閱
        :type SubscribeObjectType: int
        :param SubscribeObjects: 訂閱對象，當SubscribeObjectType 爲0時，此欄位爲空數組
        :type SubscribeObjects: list of SubscribeObject
        :param ModifyTime: 修改時間
        :type ModifyTime: str
        :param Region: 地域
        :type Region: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SubscribeId = None
        self.SubscribeName = None
        self.ChannelId = None
        self.Product = None
        self.InstanceId = None
        self.InstanceStatus = None
        self.SubsStatus = None
        self.Status = None
        self.CreateTime = None
        self.IsolateTime = None
        self.ExpireTime = None
        self.OfflineTime = None
        self.ConsumeStartTime = None
        self.PayType = None
        self.Vip = None
        self.Vport = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.SdkConsumedTime = None
        self.SdkHost = None
        self.SubscribeObjectType = None
        self.SubscribeObjects = None
        self.ModifyTime = None
        self.Region = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.SubscribeName = params.get("SubscribeName")
        self.ChannelId = params.get("ChannelId")
        self.Product = params.get("Product")
        self.InstanceId = params.get("InstanceId")
        self.InstanceStatus = params.get("InstanceStatus")
        self.SubsStatus = params.get("SubsStatus")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.IsolateTime = params.get("IsolateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.OfflineTime = params.get("OfflineTime")
        self.ConsumeStartTime = params.get("ConsumeStartTime")
        self.PayType = params.get("PayType")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.SdkConsumedTime = params.get("SdkConsumedTime")
        self.SdkHost = params.get("SdkHost")
        self.SubscribeObjectType = params.get("SubscribeObjectType")
        if params.get("SubscribeObjects") is not None:
            self.SubscribeObjects = []
            for item in params.get("SubscribeObjects"):
                obj = SubscribeObject()
                obj._deserialize(item)
                self.SubscribeObjects.append(obj)
        self.ModifyTime = params.get("ModifyTime")
        self.Region = params.get("Region")
        self.RequestId = params.get("RequestId")


class DescribeSubscribesRequest(AbstractModel):
    """DescribeSubscribes請求參數結構體

    """

    def __init__(self):
        """
        :param SubscribeId: 數據訂閱的實例ID
        :type SubscribeId: str
        :param SubscribeName: 數據訂閱的實例名稱
        :type SubscribeName: str
        :param InstanceId: 綁定資料庫實例的ID
        :type InstanceId: str
        :param ChannelId: 數據訂閱實例的通道ID
        :type ChannelId: str
        :param PayType: 計費模式篩選，可能的值：0-包年包月，1-按量計費
        :type PayType: str
        :param Product: 訂閱的資料庫産品，如mysql
        :type Product: str
        :param Status: 數據訂閱實例的狀态，creating - 創建中，normal - 正常運作，isolating - 隔離中，isolated - 已隔離，offlining - 下線中
        :type Status: list of str
        :param SubsStatus: 數據訂閱實例的配置狀态，unconfigure - 未配置， configuring - 配置中，configured - 已配置
        :type SubsStatus: list of str
        :param Offset: 返回記錄的起始偏移量
        :type Offset: int
        :param Limit: 單次返回的記錄數量
        :type Limit: int
        :param OrderDirection: 排序方向，可選的值爲"DESC"和"ASC"，預設爲"DESC"，按創建時間逆序排序
        :type OrderDirection: str
        """
        self.SubscribeId = None
        self.SubscribeName = None
        self.InstanceId = None
        self.ChannelId = None
        self.PayType = None
        self.Product = None
        self.Status = None
        self.SubsStatus = None
        self.Offset = None
        self.Limit = None
        self.OrderDirection = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.SubscribeName = params.get("SubscribeName")
        self.InstanceId = params.get("InstanceId")
        self.ChannelId = params.get("ChannelId")
        self.PayType = params.get("PayType")
        self.Product = params.get("Product")
        self.Status = params.get("Status")
        self.SubsStatus = params.get("SubsStatus")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderDirection = params.get("OrderDirection")


class DescribeSubscribesResponse(AbstractModel):
    """DescribeSubscribes返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合查詢條件的實例總數
        :type TotalCount: int
        :param Items: 數據訂閱實例的訊息清單
        :type Items: list of SubscribeInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = SubscribeInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSyncCheckJobRequest(AbstractModel):
    """DescribeSyncCheckJob請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 要查詢的災備同步任務ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class DescribeSyncCheckJobResponse(AbstractModel):
    """DescribeSyncCheckJob返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 任務校驗狀态： starting(開始中)，running(校驗中)，finished(校驗完成)
        :type Status: str
        :param ErrorCode: 任務校驗結果代碼
        :type ErrorCode: int
        :param ErrorMessage: 提示訊息
        :type ErrorMessage: str
        :param StepInfo: 任務執行步驟描述
        :type StepInfo: list of SyncCheckStepInfo
        :param CheckFlag: 校驗標志：0（尚未校驗成功） ， 1（校驗成功）
        :type CheckFlag: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.ErrorCode = None
        self.ErrorMessage = None
        self.StepInfo = None
        self.CheckFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrorCode = params.get("ErrorCode")
        self.ErrorMessage = params.get("ErrorMessage")
        if params.get("StepInfo") is not None:
            self.StepInfo = []
            for item in params.get("StepInfo"):
                obj = SyncCheckStepInfo()
                obj._deserialize(item)
                self.StepInfo.append(obj)
        self.CheckFlag = params.get("CheckFlag")
        self.RequestId = params.get("RequestId")


class DescribeSyncJobsRequest(AbstractModel):
    """DescribeSyncJobs請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 災備同步任務ID
        :type JobId: str
        :param JobName: 災備同步任務名
        :type JobName: str
        :param Order: 排序欄位，可以取值爲JobId、Status、JobName、CreateTime
        :type Order: str
        :param OrderSeq: 排序方式，升序爲ASC，降序爲DESC
        :type OrderSeq: str
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 返回實例數量，預設20，有效區間[1,100]
        :type Limit: int
        """
        self.JobId = None
        self.JobName = None
        self.Order = None
        self.OrderSeq = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.Order = params.get("Order")
        self.OrderSeq = params.get("OrderSeq")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeSyncJobsResponse(AbstractModel):
    """DescribeSyncJobs返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 任務數目
        :type TotalCount: int
        :param JobList: 任務詳情數組
        :type JobList: list of SyncJobInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.JobList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("JobList") is not None:
            self.JobList = []
            for item in params.get("JobList"):
                obj = SyncJobInfo()
                obj._deserialize(item)
                self.JobList.append(obj)
        self.RequestId = params.get("RequestId")


class DstInfo(AbstractModel):
    """目的實例訊息，具體内容跟遷移任務類型相關

    """

    def __init__(self):
        """
        :param InstanceId: 目標實例ID，如cdb-jd92ijd8
        :type InstanceId: str
        :param Region: 目標實例地域，如ap-guangzhou
        :type Region: str
        :param Ip: 目標實例vip。已廢棄，無需填寫
        :type Ip: str
        :param Port: 目標實例vport。已廢棄，無需填寫
        :type Port: int
        :param ReadOnly: 目前只對MySQL有效。當爲整實例遷移時，1-只讀，0-可讀寫。
        :type ReadOnly: int
        :param User: 目標資料庫賬號
        :type User: str
        :param Password: 目標資料庫密碼
        :type Password: str
        """
        self.InstanceId = None
        self.Region = None
        self.Ip = None
        self.Port = None
        self.ReadOnly = None
        self.User = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Region = params.get("Region")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.ReadOnly = params.get("ReadOnly")
        self.User = params.get("User")
        self.Password = params.get("Password")


class ErrorInfo(AbstractModel):
    """遷移任務錯誤訊息及提示

    """

    def __init__(self):
        """
        :param ErrorLog: 具體的報錯日志, 包含錯誤碼和錯誤訊息
        :type ErrorLog: str
        :param HelpDoc: 報錯對應的幫助文件Ur
        :type HelpDoc: str
        """
        self.ErrorLog = None
        self.HelpDoc = None


    def _deserialize(self, params):
        self.ErrorLog = params.get("ErrorLog")
        self.HelpDoc = params.get("HelpDoc")


class IsolateSubscribeRequest(AbstractModel):
    """IsolateSubscribe請求參數結構體

    """

    def __init__(self):
        """
        :param SubscribeId: 訂閱實例ID
        :type SubscribeId: str
        """
        self.SubscribeId = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")


class IsolateSubscribeResponse(AbstractModel):
    """IsolateSubscribe返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MigrateDetailInfo(AbstractModel):
    """描述詳細遷移過程

    """

    def __init__(self):
        """
        :param StepAll: 總步驟數
        :type StepAll: int
        :param StepNow: 當前步驟
        :type StepNow: int
        :param Progress: 總進度,如："10"
        :type Progress: str
        :param CurrentStepProgress: 當前步驟進度,如:"1"
        :type CurrentStepProgress: str
        :param MasterSlaveDistance: 主從差距，MB；在增量同步階段有效，目前支援産品爲：redis和mysql
        :type MasterSlaveDistance: int
        :param SecondsBehindMaster: 主從差距，秒；在增量同步階段有效，目前支援産品爲：mysql
        :type SecondsBehindMaster: int
        :param StepInfo: 步驟訊息
        :type StepInfo: list of MigrateStepDetailInfo
        """
        self.StepAll = None
        self.StepNow = None
        self.Progress = None
        self.CurrentStepProgress = None
        self.MasterSlaveDistance = None
        self.SecondsBehindMaster = None
        self.StepInfo = None


    def _deserialize(self, params):
        self.StepAll = params.get("StepAll")
        self.StepNow = params.get("StepNow")
        self.Progress = params.get("Progress")
        self.CurrentStepProgress = params.get("CurrentStepProgress")
        self.MasterSlaveDistance = params.get("MasterSlaveDistance")
        self.SecondsBehindMaster = params.get("SecondsBehindMaster")
        if params.get("StepInfo") is not None:
            self.StepInfo = []
            for item in params.get("StepInfo"):
                obj = MigrateStepDetailInfo()
                obj._deserialize(item)
                self.StepInfo.append(obj)


class MigrateJobInfo(AbstractModel):
    """遷移任務詳情

    """

    def __init__(self):
        """
        :param JobId: 數據遷移任務ID
        :type JobId: str
        :param JobName: 數據遷移任務名稱
        :type JobName: str
        :param MigrateOption: 遷移任務配置選項
        :type MigrateOption: :class:`taifucloudcloud.dts.v20180330.models.MigrateOption`
        :param SrcDatabaseType: 源實例資料庫類型:mysql，redis，mongodb，postgresql，mariadb，percona
        :type SrcDatabaseType: str
        :param SrcAccessType: 源實例接入類型，值包括：extranet(外網),cvm(cvm自建實例),dcg(專線接入的實例),vpncloud(雲vpn接入的實例),cdb(Top Cloud 資料庫實例),ccn(雲聯網實例)
        :type SrcAccessType: str
        :param SrcInfo: 源實例訊息，具體内容跟遷移任務類型相關
        :type SrcInfo: :class:`taifucloudcloud.dts.v20180330.models.SrcInfo`
        :param DstDatabaseType: 目標實例資料庫類型:mysql，redis，mongodb，postgresql，mariadb，percona
        :type DstDatabaseType: str
        :param DstAccessType: 目標實例接入類型，目前支援：cdb(Top Cloud 資料庫實例)
        :type DstAccessType: str
        :param DstInfo: 目標實例訊息
        :type DstInfo: :class:`taifucloudcloud.dts.v20180330.models.DstInfo`
        :param DatabaseInfo: 需要遷移的源資料庫表訊息，如果需要遷移的是整個實例，該欄位爲[]
        :type DatabaseInfo: str
        :param CreateTime: 任務創建(提交)時間
        :type CreateTime: str
        :param StartTime: 任務開始執行時間
        :type StartTime: str
        :param EndTime: 任務執行結束時間
        :type EndTime: str
        :param Status: 任務狀态,取值爲：1-創建中(Creating),3-校驗中(Checking)4-校驗通過(CheckPass),5-校驗不通過（CheckNotPass）,7-任務運作(Running),8-準備完成（ReadyComplete）,9-任務成功（Success）,10-任務失敗（Failed）,11-撤銷中（Stopping）,12-完成中（Completing）
        :type Status: int
        :param Detail: 任務詳情
        :type Detail: :class:`taifucloudcloud.dts.v20180330.models.MigrateDetailInfo`
        :param ErrorInfo: 任務錯誤訊息提示，當任務發生錯誤時，不爲null或者空值
        :type ErrorInfo: list of ErrorInfo
        """
        self.JobId = None
        self.JobName = None
        self.MigrateOption = None
        self.SrcDatabaseType = None
        self.SrcAccessType = None
        self.SrcInfo = None
        self.DstDatabaseType = None
        self.DstAccessType = None
        self.DstInfo = None
        self.DatabaseInfo = None
        self.CreateTime = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.Detail = None
        self.ErrorInfo = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        if params.get("MigrateOption") is not None:
            self.MigrateOption = MigrateOption()
            self.MigrateOption._deserialize(params.get("MigrateOption"))
        self.SrcDatabaseType = params.get("SrcDatabaseType")
        self.SrcAccessType = params.get("SrcAccessType")
        if params.get("SrcInfo") is not None:
            self.SrcInfo = SrcInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        self.DstDatabaseType = params.get("DstDatabaseType")
        self.DstAccessType = params.get("DstAccessType")
        if params.get("DstInfo") is not None:
            self.DstInfo = DstInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        self.DatabaseInfo = params.get("DatabaseInfo")
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        if params.get("Detail") is not None:
            self.Detail = MigrateDetailInfo()
            self.Detail._deserialize(params.get("Detail"))
        if params.get("ErrorInfo") is not None:
            self.ErrorInfo = []
            for item in params.get("ErrorInfo"):
                obj = ErrorInfo()
                obj._deserialize(item)
                self.ErrorInfo.append(obj)


class MigrateOption(AbstractModel):
    """遷移任務配置選項

    """

    def __init__(self):
        """
        :param RunMode: 任務運作模式，值包括：1-立即執行，2-定時執行
        :type RunMode: int
        :param ExpectTime: 期望執行時間，當runMode=2時，該欄位必填，時間格式：yyyy-mm-dd hh:mm:ss
        :type ExpectTime: str
        :param MigrateType: 數據遷移類型，值包括：1-結構遷移,2-全量遷移,3-全量+增量遷移
        :type MigrateType: int
        :param MigrateObject: 遷移對象，1-整個實例，2-指定庫表
        :type MigrateObject: int
        :param ConsistencyType: 抽樣數據一緻性檢測參數，1-未配置,2-全量檢測,3-抽樣檢測, 4-僅校驗不一緻表,5-不檢測
        :type ConsistencyType: int
        :param IsOverrideRoot: 是否用源庫Root帳戶函蓋目標庫，值包括：0-不函蓋，1-函蓋，選擇庫表或者結構遷移時應該爲0
        :type IsOverrideRoot: int
        :param ExternParams: 不同資料庫用到的額外參數.以JSON格式描述. 
Redis可定義如下的參數: 
{ 
	"ClientOutputBufferHardLimit":512, 	從機緩沖區的硬性容量限制(MB) 
	"ClientOutputBufferSoftLimit":512, 	從機緩沖區的軟性容量限制(MB) 
	"ClientOutputBufferPersistTime":60, 從機緩沖區的軟性限制持續時間(秒) 
	"ReplBacklogSize":512, 	環形緩沖區容量限制(MB) 
	"ReplTimeout":120，		複制超時時間(秒) 
}
MongoDB可定義如下的參數: 
{
	'SrcAuthDatabase':'admin', 
	'SrcAuthFlag': "1", 
	'SrcAuthMechanism':"SCRAM-SHA-1"
}
MySQL暫不支援額外參數設置。
        :type ExternParams: str
        :param ConsistencyParams: 僅用於“抽樣數據一緻性檢測”，ConsistencyType配置爲抽樣檢測時，必選
        :type ConsistencyParams: :class:`taifucloudcloud.dts.v20180330.models.ConsistencyParams`
        """
        self.RunMode = None
        self.ExpectTime = None
        self.MigrateType = None
        self.MigrateObject = None
        self.ConsistencyType = None
        self.IsOverrideRoot = None
        self.ExternParams = None
        self.ConsistencyParams = None


    def _deserialize(self, params):
        self.RunMode = params.get("RunMode")
        self.ExpectTime = params.get("ExpectTime")
        self.MigrateType = params.get("MigrateType")
        self.MigrateObject = params.get("MigrateObject")
        self.ConsistencyType = params.get("ConsistencyType")
        self.IsOverrideRoot = params.get("IsOverrideRoot")
        self.ExternParams = params.get("ExternParams")
        if params.get("ConsistencyParams") is not None:
            self.ConsistencyParams = ConsistencyParams()
            self.ConsistencyParams._deserialize(params.get("ConsistencyParams"))


class MigrateStepDetailInfo(AbstractModel):
    """遷移中的步驟訊息

    """

    def __init__(self):
        """
        :param StepNo: 步驟序列
        :type StepNo: int
        :param StepName: 步驟展現名稱
        :type StepName: str
        :param StepId: 步驟英文標識
        :type StepId: str
        :param Status: 步驟狀态:0-預設值,1-成功,2-失敗,3-執行中,4-未執行
        :type Status: int
        :param StartTime: 當前步驟開始的時間，格式爲"yyyy-mm-dd hh:mm:ss"，該欄位不存在或者爲空是無意義
注意：此欄位可能返回 null，表示取不到有效值。
        :type StartTime: str
        """
        self.StepNo = None
        self.StepName = None
        self.StepId = None
        self.Status = None
        self.StartTime = None


    def _deserialize(self, params):
        self.StepNo = params.get("StepNo")
        self.StepName = params.get("StepName")
        self.StepId = params.get("StepId")
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")


class ModifyMigrateJobRequest(AbstractModel):
    """ModifyMigrateJob請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 待修改的數據遷移任務ID
        :type JobId: str
        :param JobName: 數據遷移任務名稱
        :type JobName: str
        :param MigrateOption: 遷移任務配置選項
        :type MigrateOption: :class:`taifucloudcloud.dts.v20180330.models.MigrateOption`
        :param SrcAccessType: 源實例接入類型，值包括：extranet(外網),cvm(CVM自建實例),dcg(專線接入的實例),vpncloud(雲VPN接入的實例),cdb(雲上CDB實例)
        :type SrcAccessType: str
        :param SrcInfo: 源實例訊息，具體内容跟遷移任務類型相關
        :type SrcInfo: :class:`taifucloudcloud.dts.v20180330.models.SrcInfo`
        :param DstAccessType: 目標實例接入類型，值包括：extranet(外網),cvm(CVM自建實例),dcg(專線接入的實例),vpncloud(雲VPN接入的實例)，cdb(雲上CDB實例). 目前只支援cdb.
        :type DstAccessType: str
        :param DstInfo: 目標實例訊息, 其中目標實例地域不允許修改.
        :type DstInfo: :class:`taifucloudcloud.dts.v20180330.models.DstInfo`
        :param DatabaseInfo: 當選擇'指定庫表'遷移的時候, 需要設置待遷移的源資料庫表訊息,用符合json數組格式的字串描述, 如下所例。

對於database-table兩級結構的資料庫：
[{"Database":"db1","Table":["table1","table2"]},{"Database":"db2"}]
對於database-schema-table三級結構：
[{"Database":"db1","Schema":"s1","Table":["table1","table2"]},{"Database":"db1","Schema":"s2","Table":["table1","table2"]},{"Database":"db2","Schema":"s1","Table":["table1","table2"]},{"Database":"db3"},{"Database":"db4","Schema":"s1"}]

如果是'整個實例'的遷移模式,不需設置該欄位
        :type DatabaseInfo: str
        """
        self.JobId = None
        self.JobName = None
        self.MigrateOption = None
        self.SrcAccessType = None
        self.SrcInfo = None
        self.DstAccessType = None
        self.DstInfo = None
        self.DatabaseInfo = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        if params.get("MigrateOption") is not None:
            self.MigrateOption = MigrateOption()
            self.MigrateOption._deserialize(params.get("MigrateOption"))
        self.SrcAccessType = params.get("SrcAccessType")
        if params.get("SrcInfo") is not None:
            self.SrcInfo = SrcInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        self.DstAccessType = params.get("DstAccessType")
        if params.get("DstInfo") is not None:
            self.DstInfo = DstInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        self.DatabaseInfo = params.get("DatabaseInfo")


class ModifyMigrateJobResponse(AbstractModel):
    """ModifyMigrateJob返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubscribeConsumeTimeRequest(AbstractModel):
    """ModifySubscribeConsumeTime請求參數結構體

    """

    def __init__(self):
        """
        :param SubscribeId: 數據訂閱實例的ID
        :type SubscribeId: str
        :param ConsumeStartTime: 消費時間起點，也即是指定訂閱數據的時間起點，時間格式如：Y-m-d h:m:s，取值範圍爲過去24小時之内
        :type ConsumeStartTime: str
        """
        self.SubscribeId = None
        self.ConsumeStartTime = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.ConsumeStartTime = params.get("ConsumeStartTime")


class ModifySubscribeConsumeTimeResponse(AbstractModel):
    """ModifySubscribeConsumeTime返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubscribeNameRequest(AbstractModel):
    """ModifySubscribeName請求參數結構體

    """

    def __init__(self):
        """
        :param SubscribeId: 數據訂閱實例的ID
        :type SubscribeId: str
        :param SubscribeName: 數據訂閱實例的名稱，長度限制爲[1,60]
        :type SubscribeName: str
        """
        self.SubscribeId = None
        self.SubscribeName = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.SubscribeName = params.get("SubscribeName")


class ModifySubscribeNameResponse(AbstractModel):
    """ModifySubscribeName返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubscribeObjectsRequest(AbstractModel):
    """ModifySubscribeObjects請求參數結構體

    """

    def __init__(self):
        """
        :param SubscribeId: 數據訂閱實例的ID
        :type SubscribeId: str
        :param SubscribeObjectType: 數據訂閱的類型，可選的值有：0 - 全實例訂閱；1 - 數據訂閱；2 - 結構訂閱；3 - 數據訂閱+結構訂閱
        :type SubscribeObjectType: int
        :param Objects: 訂閱的資料庫表訊息
        :type Objects: list of SubscribeObject
        """
        self.SubscribeId = None
        self.SubscribeObjectType = None
        self.Objects = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.SubscribeObjectType = params.get("SubscribeObjectType")
        if params.get("Objects") is not None:
            self.Objects = []
            for item in params.get("Objects"):
                obj = SubscribeObject()
                obj._deserialize(item)
                self.Objects.append(obj)


class ModifySubscribeObjectsResponse(AbstractModel):
    """ModifySubscribeObjects返回參數結構體

    """

    def __init__(self):
        """
        :param AsyncRequestId: 異步任務的ID
        :type AsyncRequestId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifySubscribeVipVportRequest(AbstractModel):
    """ModifySubscribeVipVport請求參數結構體

    """

    def __init__(self):
        """
        :param SubscribeId: 數據訂閱實例的ID
        :type SubscribeId: str
        :param DstUniqSubnetId: 指定目的子網，如果傳此參數，DstIp必須在目的子網内
        :type DstUniqSubnetId: str
        :param DstIp: 目標IP，與DstPort至少傳一個
        :type DstIp: str
        :param DstPort: 目標PORT，支援範圍爲：[1025-65535]
        :type DstPort: int
        """
        self.SubscribeId = None
        self.DstUniqSubnetId = None
        self.DstIp = None
        self.DstPort = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.DstUniqSubnetId = params.get("DstUniqSubnetId")
        self.DstIp = params.get("DstIp")
        self.DstPort = params.get("DstPort")


class ModifySubscribeVipVportResponse(AbstractModel):
    """ModifySubscribeVipVport返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySyncJobRequest(AbstractModel):
    """ModifySyncJob請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 待修改的災備同步任務ID
        :type JobId: str
        :param JobName: 災備同步任務名稱
        :type JobName: str
        :param SyncOption: 災備同步任務配置選項
        :type SyncOption: :class:`taifucloudcloud.dts.v20180330.models.SyncOption`
        :param DatabaseInfo: 當選擇'指定庫表'災備同步的時候, 需要設置待同步的源資料庫表訊息,用符合json數組格式的字串描述, 如下所例。
對於database-table兩級結構的資料庫：
[{"Database":"db1","Table":["table1","table2"]},{"Database":"db2"}]
        :type DatabaseInfo: str
        """
        self.JobId = None
        self.JobName = None
        self.SyncOption = None
        self.DatabaseInfo = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        if params.get("SyncOption") is not None:
            self.SyncOption = SyncOption()
            self.SyncOption._deserialize(params.get("SyncOption"))
        self.DatabaseInfo = params.get("DatabaseInfo")


class ModifySyncJobResponse(AbstractModel):
    """ModifySyncJob返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OfflineIsolatedSubscribeRequest(AbstractModel):
    """OfflineIsolatedSubscribe請求參數結構體

    """

    def __init__(self):
        """
        :param SubscribeId: 數據訂閱實例的ID
        :type SubscribeId: str
        """
        self.SubscribeId = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")


class OfflineIsolatedSubscribeResponse(AbstractModel):
    """OfflineIsolatedSubscribe返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetSubscribeRequest(AbstractModel):
    """ResetSubscribe請求參數結構體

    """

    def __init__(self):
        """
        :param SubscribeId: 數據訂閱實例的ID
        :type SubscribeId: str
        """
        self.SubscribeId = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")


class ResetSubscribeResponse(AbstractModel):
    """ResetSubscribe返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SrcInfo(AbstractModel):
    """源實例訊息

    """

    def __init__(self):
        """
        :param AccessKey: 阿裏雲AccessKey。源庫是阿裏雲RDS5.6适用
        :type AccessKey: str
        :param Ip: 實例的IP網址
        :type Ip: str
        :param Port: 實例的端口
        :type Port: int
        :param User: 實例的用戶名
        :type User: str
        :param Password: 實例的密碼
        :type Password: str
        :param RdsInstanceId: 阿裏雲RDS實例ID。源庫是阿裏雲RDS5.6/5.6适用
        :type RdsInstanceId: str
        :param CvmInstanceId: CVM實例短ID，格式如：ins-olgl39y8，與雲伺服器控制台頁面顯示的實例ID相同。如果是CVM自建實例，需要傳遞此欄位
        :type CvmInstanceId: str
        :param UniqDcgId: 專線閘道ID，格式如：dcg-0rxtqqxb
        :type UniqDcgId: str
        :param VpcId: 私有網絡ID，格式如：vpc-92jblxto
        :type VpcId: str
        :param SubnetId: 私有網絡下的子網ID，格式如：subnet-3paxmkdz
        :type SubnetId: str
        :param UniqVpnGwId: VPN閘道ID，格式如：vpngw-9ghexg7q
        :type UniqVpnGwId: str
        :param InstanceId: 資料庫實例ID，格式如：cdb-powiqx8q
        :type InstanceId: str
        :param Region: 地域英文名，如：ap-guangzhou
        :type Region: str
        :param Supplier: 當實例爲RDS實例時，填寫爲aliyun, 其他情況均填寫others
        :type Supplier: str
        :param CcnId: 雲聯網ID，如：ccn-afp6kltc
注意：此欄位可能返回 null，表示取不到有效值。
        :type CcnId: str
        :param EngineVersion: 資料庫版本，當實例爲RDS實例時才有效，格式如：5.6或者5.7，預設爲5.6
        :type EngineVersion: str
        """
        self.AccessKey = None
        self.Ip = None
        self.Port = None
        self.User = None
        self.Password = None
        self.RdsInstanceId = None
        self.CvmInstanceId = None
        self.UniqDcgId = None
        self.VpcId = None
        self.SubnetId = None
        self.UniqVpnGwId = None
        self.InstanceId = None
        self.Region = None
        self.Supplier = None
        self.CcnId = None
        self.EngineVersion = None


    def _deserialize(self, params):
        self.AccessKey = params.get("AccessKey")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.User = params.get("User")
        self.Password = params.get("Password")
        self.RdsInstanceId = params.get("RdsInstanceId")
        self.CvmInstanceId = params.get("CvmInstanceId")
        self.UniqDcgId = params.get("UniqDcgId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.UniqVpnGwId = params.get("UniqVpnGwId")
        self.InstanceId = params.get("InstanceId")
        self.Region = params.get("Region")
        self.Supplier = params.get("Supplier")
        self.CcnId = params.get("CcnId")
        self.EngineVersion = params.get("EngineVersion")


class StartMigrateJobRequest(AbstractModel):
    """StartMigrateJob請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 數據遷移任務ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class StartMigrateJobResponse(AbstractModel):
    """StartMigrateJob返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StartSyncJobRequest(AbstractModel):
    """StartSyncJob請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 災備同步任務ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class StartSyncJobResponse(AbstractModel):
    """StartSyncJob返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopMigrateJobRequest(AbstractModel):
    """StopMigrateJob請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 數據遷移任務ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class StopMigrateJobResponse(AbstractModel):
    """StopMigrateJob返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SubscribeInfo(AbstractModel):
    """訂閱實例訊息

    """

    def __init__(self):
        """
        :param SubscribeId: 數據訂閱的實例ID
        :type SubscribeId: str
        :param SubscribeName: 數據訂閱實例的名稱
        :type SubscribeName: str
        :param ChannelId: 數據訂閱實例綁定的通道ID
        :type ChannelId: str
        :param Product: 數據訂閱綁定實例對應的産品名稱
        :type Product: str
        :param InstanceId: 數據訂閱實例綁定的資料庫實例ID
        :type InstanceId: str
        :param InstanceStatus: 數據訂閱實例綁定的資料庫實例狀态
        :type InstanceStatus: str
        :param SubsStatus: 數據訂閱實例的配置狀态，unconfigure - 未配置， configuring - 配置中，configured - 已配置
        :type SubsStatus: str
        :param ModifyTime: 上次修改時間
        :type ModifyTime: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param IsolateTime: 隔離時間
        :type IsolateTime: str
        :param ExpireTime: 到期時間
        :type ExpireTime: str
        :param OfflineTime: 下線時間
        :type OfflineTime: str
        :param ConsumeStartTime: 最近一次修改的消費時間起點，如果從未修改則爲零值
        :type ConsumeStartTime: str
        :param Region: 數據訂閱實例所屬地域
        :type Region: str
        :param PayType: 計費方式，0 - 包年包月，1 - 按量計費
        :type PayType: int
        :param Vip: 數據訂閱實例的Vip
        :type Vip: str
        :param Vport: 數據訂閱實例的Vport
        :type Vport: int
        :param UniqVpcId: 數據訂閱實例Vip所在VPC的唯一ID
        :type UniqVpcId: str
        :param UniqSubnetId: 數據訂閱實例Vip所在子網的唯一ID
        :type UniqSubnetId: str
        :param Status: 數據訂閱實例的狀态，creating - 創建中，normal - 正常運作，isolating - 隔離中，isolated - 已隔離，offlining - 下線中，offline - 已下線
        :type Status: str
        :param SdkConsumedTime: SDK最後一條确認訊息的時間戳，如果SDK一直消費，也可以作爲SDK當前消費時間點
        :type SdkConsumedTime: str
        """
        self.SubscribeId = None
        self.SubscribeName = None
        self.ChannelId = None
        self.Product = None
        self.InstanceId = None
        self.InstanceStatus = None
        self.SubsStatus = None
        self.ModifyTime = None
        self.CreateTime = None
        self.IsolateTime = None
        self.ExpireTime = None
        self.OfflineTime = None
        self.ConsumeStartTime = None
        self.Region = None
        self.PayType = None
        self.Vip = None
        self.Vport = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.Status = None
        self.SdkConsumedTime = None


    def _deserialize(self, params):
        self.SubscribeId = params.get("SubscribeId")
        self.SubscribeName = params.get("SubscribeName")
        self.ChannelId = params.get("ChannelId")
        self.Product = params.get("Product")
        self.InstanceId = params.get("InstanceId")
        self.InstanceStatus = params.get("InstanceStatus")
        self.SubsStatus = params.get("SubsStatus")
        self.ModifyTime = params.get("ModifyTime")
        self.CreateTime = params.get("CreateTime")
        self.IsolateTime = params.get("IsolateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.OfflineTime = params.get("OfflineTime")
        self.ConsumeStartTime = params.get("ConsumeStartTime")
        self.Region = params.get("Region")
        self.PayType = params.get("PayType")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.Status = params.get("Status")
        self.SdkConsumedTime = params.get("SdkConsumedTime")


class SubscribeObject(AbstractModel):
    """數據數據訂閱的對象

    """

    def __init__(self):
        """
        :param ObjectsType: 數據訂閱對象的類型，0-資料庫，1-資料庫内的表
注意：此欄位可能返回 null，表示取不到有效值。
        :type ObjectsType: int
        :param DatabaseName: 訂閱資料庫的名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type DatabaseName: str
        :param TableNames: 訂閱資料庫中表名稱數組
注意：此欄位可能返回 null，表示取不到有效值。
        :type TableNames: list of str
        """
        self.ObjectsType = None
        self.DatabaseName = None
        self.TableNames = None


    def _deserialize(self, params):
        self.ObjectsType = params.get("ObjectsType")
        self.DatabaseName = params.get("DatabaseName")
        self.TableNames = params.get("TableNames")


class SubscribeRegionConf(AbstractModel):
    """數據訂閱地域售賣訊息

    """

    def __init__(self):
        """
        :param RegionName: 地域名稱，如 
注意：此欄位可能返回 null，表示取不到有效值。
        :type RegionName: str
        :param Region: 地區標識，如ap-guangzhou
注意：此欄位可能返回 null，表示取不到有效值。
        :type Region: str
        :param Area: 地域名稱，如華南地區
注意：此欄位可能返回 null，表示取不到有效值。
        :type Area: str
        :param IsDefaultRegion: 是否爲預設地域，0 - 不是，1 - 是的
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsDefaultRegion: int
        :param Status: 當前地域的售賣情況，1 - 正常， 2-灰度，3 - 停售
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self.RegionName = None
        self.Region = None
        self.Area = None
        self.IsDefaultRegion = None
        self.Status = None


    def _deserialize(self, params):
        self.RegionName = params.get("RegionName")
        self.Region = params.get("Region")
        self.Area = params.get("Area")
        self.IsDefaultRegion = params.get("IsDefaultRegion")
        self.Status = params.get("Status")


class SwitchDrToMasterRequest(AbstractModel):
    """SwitchDrToMaster請求參數結構體

    """

    def __init__(self):
        """
        :param DstInfo: 災備實例的訊息
        :type DstInfo: :class:`taifucloudcloud.dts.v20180330.models.SyncInstanceInfo`
        :param DatabaseType: 資料庫的類型  （如 mysql）
        :type DatabaseType: str
        """
        self.DstInfo = None
        self.DatabaseType = None


    def _deserialize(self, params):
        if params.get("DstInfo") is not None:
            self.DstInfo = SyncInstanceInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        self.DatabaseType = params.get("DatabaseType")


class SwitchDrToMasterResponse(AbstractModel):
    """SwitchDrToMaster返回參數結構體

    """

    def __init__(self):
        """
        :param AsyncRequestId: 後台異步任務請求id
        :type AsyncRequestId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class SyncCheckStepInfo(AbstractModel):
    """災備任務校驗步驟

    """

    def __init__(self):
        """
        :param StepNo: 步驟序列
        :type StepNo: int
        :param StepName: 步驟展現名稱
        :type StepName: str
        :param StepCode: 步驟執行結果代碼
        :type StepCode: int
        :param StepMessage: 步驟執行結果提示
        :type StepMessage: str
        """
        self.StepNo = None
        self.StepName = None
        self.StepCode = None
        self.StepMessage = None


    def _deserialize(self, params):
        self.StepNo = params.get("StepNo")
        self.StepName = params.get("StepName")
        self.StepCode = params.get("StepCode")
        self.StepMessage = params.get("StepMessage")


class SyncDetailInfo(AbstractModel):
    """描述詳細同步任務過程

    """

    def __init__(self):
        """
        :param StepAll: 總步驟數
        :type StepAll: int
        :param StepNow: 當前步驟
        :type StepNow: int
        :param Progress: 總進度
        :type Progress: str
        :param CurrentStepProgress: 當前步驟進度
        :type CurrentStepProgress: str
        :param MasterSlaveDistance: 主從差距，MB
        :type MasterSlaveDistance: int
        :param SecondsBehindMaster: 主從差距，秒
        :type SecondsBehindMaster: int
        :param StepInfo: 步驟訊息
        :type StepInfo: list of SyncStepDetailInfo
        """
        self.StepAll = None
        self.StepNow = None
        self.Progress = None
        self.CurrentStepProgress = None
        self.MasterSlaveDistance = None
        self.SecondsBehindMaster = None
        self.StepInfo = None


    def _deserialize(self, params):
        self.StepAll = params.get("StepAll")
        self.StepNow = params.get("StepNow")
        self.Progress = params.get("Progress")
        self.CurrentStepProgress = params.get("CurrentStepProgress")
        self.MasterSlaveDistance = params.get("MasterSlaveDistance")
        self.SecondsBehindMaster = params.get("SecondsBehindMaster")
        if params.get("StepInfo") is not None:
            self.StepInfo = []
            for item in params.get("StepInfo"):
                obj = SyncStepDetailInfo()
                obj._deserialize(item)
                self.StepInfo.append(obj)


class SyncInstanceInfo(AbstractModel):
    """災備同步的實例訊息，記錄主實例或災備實例的訊息

    """

    def __init__(self):
        """
        :param Region: 地域英文名，如：ap-guangzhou
        :type Region: str
        :param InstanceId: 實例短ID
        :type InstanceId: str
        """
        self.Region = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.InstanceId = params.get("InstanceId")


class SyncJobInfo(AbstractModel):
    """災備同步任務訊息

    """

    def __init__(self):
        """
        :param JobId: 災備任務id
        :type JobId: str
        :param JobName: 災備任務名
        :type JobName: str
        :param SyncOption: 任務同步
        :type SyncOption: :class:`taifucloudcloud.dts.v20180330.models.SyncOption`
        :param SrcAccessType: 源接入類型
        :type SrcAccessType: str
        :param SrcDatabaseType: 源數據類型
        :type SrcDatabaseType: str
        :param SrcInfo: 源實例訊息
        :type SrcInfo: :class:`taifucloudcloud.dts.v20180330.models.SyncInstanceInfo`
        :param DstAccessType: 災備接入類型
        :type DstAccessType: str
        :param DstDatabaseType: 災備數據類型
        :type DstDatabaseType: str
        :param DstInfo: 災備實例訊息
        :type DstInfo: :class:`taifucloudcloud.dts.v20180330.models.SyncInstanceInfo`
        :param Detail: 任務訊息
        :type Detail: :class:`taifucloudcloud.dts.v20180330.models.SyncDetailInfo`
        :param Status: 任務狀态
        :type Status: int
        :param DatabaseInfo: 遷移庫表
        :type DatabaseInfo: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param StartTime: 開始時間
        :type StartTime: str
        :param EndTime: 結束時間
        :type EndTime: str
        """
        self.JobId = None
        self.JobName = None
        self.SyncOption = None
        self.SrcAccessType = None
        self.SrcDatabaseType = None
        self.SrcInfo = None
        self.DstAccessType = None
        self.DstDatabaseType = None
        self.DstInfo = None
        self.Detail = None
        self.Status = None
        self.DatabaseInfo = None
        self.CreateTime = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        if params.get("SyncOption") is not None:
            self.SyncOption = SyncOption()
            self.SyncOption._deserialize(params.get("SyncOption"))
        self.SrcAccessType = params.get("SrcAccessType")
        self.SrcDatabaseType = params.get("SrcDatabaseType")
        if params.get("SrcInfo") is not None:
            self.SrcInfo = SyncInstanceInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        self.DstAccessType = params.get("DstAccessType")
        self.DstDatabaseType = params.get("DstDatabaseType")
        if params.get("DstInfo") is not None:
            self.DstInfo = SyncInstanceInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        if params.get("Detail") is not None:
            self.Detail = SyncDetailInfo()
            self.Detail._deserialize(params.get("Detail"))
        self.Status = params.get("Status")
        self.DatabaseInfo = params.get("DatabaseInfo")
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class SyncOption(AbstractModel):
    """災備同步任務配置選項

    """

    def __init__(self):
        """
        :param SyncObject: 同步對象，1-整個實例，2-指定庫表
        :type SyncObject: int
        :param RunMode: 同步開始設置，1-立即開始
        :type RunMode: int
        :param SyncType: 同步模式， 3-全量且增量同步
        :type SyncType: int
        :param ConsistencyType: 數據一緻性檢測， 1-無需配置
        :type ConsistencyType: int
        """
        self.SyncObject = None
        self.RunMode = None
        self.SyncType = None
        self.ConsistencyType = None


    def _deserialize(self, params):
        self.SyncObject = params.get("SyncObject")
        self.RunMode = params.get("RunMode")
        self.SyncType = params.get("SyncType")
        self.ConsistencyType = params.get("ConsistencyType")


class SyncStepDetailInfo(AbstractModel):
    """同步任務進度

    """

    def __init__(self):
        """
        :param StepNo: 步驟編號
        :type StepNo: int
        :param StepName: 步驟名
        :type StepName: str
        :param CanStop: 能否中止
        :type CanStop: int
        :param StepId: 步驟號
        :type StepId: int
        """
        self.StepNo = None
        self.StepName = None
        self.CanStop = None
        self.StepId = None


    def _deserialize(self, params):
        self.StepNo = params.get("StepNo")
        self.StepName = params.get("StepName")
        self.CanStop = params.get("CanStop")
        self.StepId = params.get("StepId")