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
        :param SelectRowsPerTable: 1-100的整數值，select(*)對比時每張表的抽樣行數比例
        :type SelectRowsPerTable: int
        :param TablesSelectAll: 1-100的整數值，select(*)對比的表的比例
        :type TablesSelectAll: int
        :param TablesSelectCount: 1-100的整數值，select count(*)對比的表的比例
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
        :type MigrateOption: :class:`tencentcloud.dts.v20180330.models.MigrateOption`
        :param SrcDatabaseType: 源實例資料庫類型:mysql,redis,mongodb
        :type SrcDatabaseType: str
        :param SrcAccessType: 源實例接入類型，值包括：extranet(外網),cvm(cvm自建實例),dcg(專線接入的實例),vpncloud(雲vpn接入的實例),vpnselfbuild(自建vpn接入的實例)，cdb(雲上cdb實例)
        :type SrcAccessType: str
        :param SrcInfo: 源實例訊息，具體内容跟遷移任務類型相關
        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SrcInfo`
        :param DstDatabaseType: 目标實例資料庫類型,mysql,redis,mongodb
        :type DstDatabaseType: str
        :param DstAccessType: 目标實例接入類型，值包括：extranet(外網),cvm(cvm自建實例),dcg(專線接入的實例),vpncloud(雲vpn接入的實例),vpnselfbuild(自建vpn接入的實例)，cdb(雲上cdb實例). 目前只支援cdb.
        :type DstAccessType: str
        :param DstInfo: 目标實例訊息
        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.DstInfo`
        :param DatabaseInfo: 需要遷移的源資料庫表訊息，用json格式的字串描述。
對于database-table兩級結構的資料庫：
[{Database:db1,Table:[table1,table2]},{Database:db2}]
對于database-schema-table三級結構：
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
        :type SyncOption: :class:`tencentcloud.dts.v20180330.models.SyncOption`
        :param SrcDatabaseType: 源實例資料庫類型，目前僅包括：mysql
        :type SrcDatabaseType: str
        :param SrcAccessType: 源實例接入類型，目前僅包括：cdb(雲上cdb實例)
        :type SrcAccessType: str
        :param SrcInfo: 源實例訊息
        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SyncInstanceInfo`
        :param DstDatabaseType: 目标實例資料庫類型，目前僅包括：mysql
        :type DstDatabaseType: str
        :param DstAccessType: 目标實例接入類型，目前僅包括：cdb(雲上cdb實例)
        :type DstAccessType: str
        :param DstInfo: 目标實例訊息
        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.SyncInstanceInfo`
        :param DatabaseInfo: 需要同步的源資料庫表訊息，用json格式的字串描述。
對于database-table兩級結構的資料庫：
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
        :param CheckFlag: 校驗标志：0（尚未校驗成功） ， 1（校驗成功）
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
        :param InstanceId: 目标實例Id
        :type InstanceId: str
        :param Ip: 目标實例vip
        :type Ip: str
        :param Port: 目标實例vport
        :type Port: int
        :param Region: 目标實例Id
        :type Region: str
        :param ReadOnly: 只讀開關
        :type ReadOnly: int
        """
        self.InstanceId = None
        self.Ip = None
        self.Port = None
        self.Region = None
        self.ReadOnly = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.Region = params.get("Region")
        self.ReadOnly = params.get("ReadOnly")


class MigrateDetailInfo(AbstractModel):
    """描述詳細遷移過程

    """

    def __init__(self):
        """
        :param StepAll: 總步驟數
        :type StepAll: int
        :param StepNow: 當前步驟
        :type StepNow: int
        :param Progress: 總進度,如：
        :type Progress: str
        :param CurrentStepProgress: 當前步驟進度,如:
        :type CurrentStepProgress: str
        :param MasterSlaveDistance: 主從差距，MB
        :type MasterSlaveDistance: int
        :param SecondsBehindMaster: 主從差距，秒
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
        :type MigrateOption: :class:`tencentcloud.dts.v20180330.models.MigrateOption`
        :param SrcDatabaseType: 源實例資料庫類型:mysql,redis,percona,mongodb,postgresql,sqlserver,mariadb
        :type SrcDatabaseType: str
        :param SrcAccessType: 源實例接入類型，值包括：extranet(外網),cvm(cvm自建實例),dcg(專線接入的實例),vpncloud(雲vpn接入的實例),vpnselfbuild(自建vpn接入的實例)，cdb(雲上cdb實例)
        :type SrcAccessType: str
        :param SrcInfo: 源實例訊息，具體内容跟遷移任務類型相關
        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SrcInfo`
        :param DstDatabaseType: 目标實例資料庫類型,mysql,redis,percona,mongodb,postgresql,sqlserver,mariadb
        :type DstDatabaseType: str
        :param DstAccessType: 源實例接入類型，值包括：extranet(外網),cvm(cvm自建實例),dcg(專線接入的實例),vpncloud(雲vpn接入的實例),vpnselfbuild(自建vpn接入的實例)，cdb(雲上cdb實例)
        :type DstAccessType: str
        :param DstInfo: 目的實例訊息
        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.DstInfo`
        :param DatabaseInfo: 需要遷移的源資料庫表訊息，如果需要遷移的是整個實例，該欄位爲[]
        :type DatabaseInfo: str
        :param CreateTime: 任務創建(提交)時間
        :type CreateTime: str
        :param StartTime: 任務開始執行時間
        :type StartTime: str
        :param EndTime: 任務執行結束時間
        :type EndTime: str
        :param Status: 任務狀态,取值爲：1-創建中(Creating),2-創建完成(Created),3-校驗中(Checking)4-校驗通過(CheckPass),5-校驗不通過（CheckNotPass）,6-準備運作(ReadyRun),7-任務運作(Running),8-準備完成（ReadyComplete）,9-任務成功（Success）,10-任務失敗（Failed）,11-中止中（Stoping）,12-完成中（Completing）
        :type Status: int
        :param Detail: 任務詳情
        :type Detail: :class:`tencentcloud.dts.v20180330.models.MigrateDetailInfo`
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
        :param ConsistencyType: 數據對比類型，1-未配置,2-全量檢測,3-抽樣檢測, 4-僅校驗不一緻表,5-不檢測
        :type ConsistencyType: int
        :param IsOverrideRoot: 是否用源庫Root帳戶函蓋目标庫，值包括：0-不函蓋，1-函蓋，選擇庫表或者結構遷移時應該爲0
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
        :type ExternParams: str
        :param ConsistencyParams: 抽樣檢驗時的抽樣參數
        :type ConsistencyParams: :class:`tencentcloud.dts.v20180330.models.ConsistencyParams`
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
        :param StepId: 步驟英文标識
        :type StepId: str
        :param Status: 步驟狀态:0-預設值,1-成功,2-失敗,3-執行中,4-未執行
        :type Status: int
        """
        self.StepNo = None
        self.StepName = None
        self.StepId = None
        self.Status = None


    def _deserialize(self, params):
        self.StepNo = params.get("StepNo")
        self.StepName = params.get("StepName")
        self.StepId = params.get("StepId")
        self.Status = params.get("Status")


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
        :type MigrateOption: :class:`tencentcloud.dts.v20180330.models.MigrateOption`
        :param SrcAccessType: 源實例接入類型，值包括：extranet(外網),cvm(cvm自建實例),dcg(專線接入的實例),vpncloud(雲vpn接入的實例),vpnselfbuild(自建vpn接入的實例)，cdb(雲上cdb實例)
        :type SrcAccessType: str
        :param SrcInfo: 源實例訊息，具體内容跟遷移任務類型相關
        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SrcInfo`
        :param DstAccessType: 目标實例接入類型，值包括：extranet(外網),cvm(cvm自建實例),dcg(專線接入的實例),vpncloud(雲vpn接入的實例),vpnselfbuild(自建vpn接入的實例)，cdb(雲上cdb實例). 目前只支援cdb.
        :type DstAccessType: str
        :param DstInfo: 目标實例訊息, 其中目标實例地域不允許修改.
        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.DstInfo`
        :param DatabaseInfo: 當選擇'指定庫表'遷移的時候, 需要設置待遷移的源資料庫表訊息,用符合json數組格式的字串描述, 如下所例。

對于database-table兩級結構的資料庫：
[{"Database":"db1","Table":["table1","table2"]},{"Database":"db2"}]
對于database-schema-table三級結構：
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
        :type SyncOption: :class:`tencentcloud.dts.v20180330.models.SyncOption`
        :param DatabaseInfo: 當選擇'指定庫表'災備同步的時候, 需要設置待同步的源資料庫表訊息,用符合json數組格式的字串描述, 如下所例。
對于database-table兩級結構的資料庫：
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


class SrcInfo(AbstractModel):
    """源實例訊息

    """

    def __init__(self):
        """
        :param AccessKey: 阿裏雲AccessKey
        :type AccessKey: str
        :param Ip: 實例的IP網址
        :type Ip: str
        :param Port: 實例的端口
        :type Port: int
        :param User: 實例的用戶名
        :type User: str
        :param Password: 實例的密碼
        :type Password: str
        :param RdsInstanceId: 阿裏雲rds實例id
        :type RdsInstanceId: str
        :param CvmInstanceId: CVM實例短ID，格式如：ins-olgl89y8，與雲主機控制台頁面顯示的實例ID相同，如果是CVM自建實例或者通過自建VPN接入的公網實例，需要傳遞此欄位
        :type CvmInstanceId: str
        :param UniqDcgId: 專線閘道ID
        :type UniqDcgId: str
        :param VpcId: 私有網絡ID，和原來的數字vpcId對應，需要調vpc的介面去轉換
        :type VpcId: str
        :param SubnetId: 私有網絡下的子網ID, 和原來的數字子網ID對應，需要調用vpc的介面去轉換
        :type SubnetId: str
        :param UniqVpnGwId: 系統分配的VPN閘道ID
        :type UniqVpnGwId: str
        :param InstanceId: 實例短Id
        :type InstanceId: str
        :param Region: 地域英文名，如：ap-guangzhou
        :type Region: str
        :param Supplier: 服務提供商，如:aliyun,others
        :type Supplier: str
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


class SwitchDrToMasterRequest(AbstractModel):
    """SwitchDrToMaster請求參數結構體

    """

    def __init__(self):
        """
        :param DstInfo: 災備實例的訊息
        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.SyncInstanceInfo`
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
        :param InstanceId: 實例短Id
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
        :type SyncOption: :class:`tencentcloud.dts.v20180330.models.SyncOption`
        :param SrcAccessType: 源接入類型
        :type SrcAccessType: str
        :param SrcDatabaseType: 源數據類型
        :type SrcDatabaseType: str
        :param SrcInfo: 源實例訊息
        :type SrcInfo: :class:`tencentcloud.dts.v20180330.models.SyncInstanceInfo`
        :param DstAccessType: 災備接入類型
        :type DstAccessType: str
        :param DstDatabaseType: 災備數據類型
        :type DstDatabaseType: str
        :param DstInfo: 災備實例訊息
        :type DstInfo: :class:`tencentcloud.dts.v20180330.models.SyncInstanceInfo`
        :param Detail: 任務訊息
        :type Detail: :class:`tencentcloud.dts.v20180330.models.SyncDetailInfo`
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
        :param StepNo: 步驟編号
        :type StepNo: int
        :param StepName: 步驟名
        :type StepName: str
        :param CanStop: 能否中止
        :type CanStop: int
        :param StepId: 步驟号
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