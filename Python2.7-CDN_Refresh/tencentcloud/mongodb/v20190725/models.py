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


class AssignProjectRequest(AbstractModel):
    """AssignProject請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 實例ID清單，格式如：cmgo-p8vnipr5。與雲資料庫控制台頁面中顯示的實例ID相同
        :type InstanceIds: list of str
        :param ProjectId: 項目ID
        :type ProjectId: int
        """
        self.InstanceIds = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.ProjectId = params.get("ProjectId")


class AssignProjectResponse(AbstractModel):
    """AssignProject返回參數結構體

    """

    def __init__(self):
        """
        :param FlowIds: 返回的異步任務ID清單
        :type FlowIds: list of int non-negative
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FlowIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowIds = params.get("FlowIds")
        self.RequestId = params.get("RequestId")


class BackupFile(AbstractModel):
    """備份文件儲存訊息

    """

    def __init__(self):
        """
        :param ReplicateSetId: 備份文件所屬的副本集/分片ID
        :type ReplicateSetId: str
        :param File: 備份文件保存路徑
        :type File: str
        """
        self.ReplicateSetId = None
        self.File = None


    def _deserialize(self, params):
        self.ReplicateSetId = params.get("ReplicateSetId")
        self.File = params.get("File")


class BackupInfo(AbstractModel):
    """備份訊息

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param BackupType: 備份方式，0-自動備份，1-手動備份
        :type BackupType: int
        :param BackupName: 備份名稱
        :type BackupName: str
        :param BackupDesc: 備份備注
注意：此欄位可能返回 null，表示取不到有效值。
        :type BackupDesc: str
        :param BackupSize: 備份文件大小，單位KB
注意：此欄位可能返回 null，表示取不到有效值。
        :type BackupSize: int
        :param StartTime: 備份開始時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 備份結束時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param Status: 備份狀态，1-備份中，2-備份成功
        :type Status: int
        :param BackupMethod: 備份方法，0-邏輯備份，1-物理備份
        :type BackupMethod: int
        """
        self.InstanceId = None
        self.BackupType = None
        self.BackupName = None
        self.BackupDesc = None
        self.BackupSize = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.BackupMethod = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupType = params.get("BackupType")
        self.BackupName = params.get("BackupName")
        self.BackupDesc = params.get("BackupDesc")
        self.BackupSize = params.get("BackupSize")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        self.BackupMethod = params.get("BackupMethod")


class ClientConnection(AbstractModel):
    """用戶端連接訊息，包括用戶端IP和連接數

    """

    def __init__(self):
        """
        :param IP: 連接的用戶端IP
        :type IP: str
        :param Count: 對應用戶端IP的連接數
        :type Count: int
        """
        self.IP = None
        self.Count = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.Count = params.get("Count")


class CreateDBInstanceHourRequest(AbstractModel):
    """CreateDBInstanceHour請求參數結構體

    """

    def __init__(self):
        """
        :param Memory: 實例内存大小，單位：GB
        :type Memory: int
        :param Volume: 實例硬碟大小，單位：GB
        :type Volume: int
        :param ReplicateSetNum: 副本集個數，創建副本集實例時，該參數必須設置爲1；創建分片實例時，具體參照查詢雲資料庫的售賣規格返回參數
        :type ReplicateSetNum: int
        :param NodeNum: 每個副本集内節點個數，當前副本集節點數固定爲3，分片從節點數可選，具體參照查詢雲資料庫的售賣規格返回參數
        :type NodeNum: int
        :param MongoVersion: 版本號，具體支援的售賣版本請參照查詢雲資料庫的售賣規格（DescribeSpecInfo）返回結果。參數與版本對應關系是MONGO_3_WT：MongoDB 3.2 WiredTiger儲存引擎版本，MONGO_3_ROCKS：MongoDB 3.2 RocksDB儲存引擎版本，MONGO_36_WT：MongoDB 3.6 WiredTiger儲存引擎版本
        :type MongoVersion: str
        :param MachineCode: 機器類型，HIO：高IO型；HIO10G：高IO萬兆
        :type MachineCode: str
        :param GoodsNum: 實例數量，最小值1，最大值爲10
        :type GoodsNum: int
        :param Zone: 可用區訊息，格式如：ap-guangzhou-2
        :type Zone: str
        :param ClusterType: 實例類型，REPLSET-副本集，SHARD-分片集群
        :type ClusterType: str
        :param VpcId: 私有網絡ID，如果不設置該參數則預設選擇基礎網絡
        :type VpcId: str
        :param SubnetId: 私有網絡下的子網ID，如果設置了 VpcId，則 SubnetId必填
        :type SubnetId: str
        :param Password: 實例密碼，不設置該參數則需要在創建完成後通過設置密碼介面初始化實例密碼。密碼必須是8-16位字元，且至少包含字母、數字和字元 !@#%^*() 中的兩種
        :type Password: str
        :param ProjectId: 項目ID，不設置爲預設項目
        :type ProjectId: int
        :param Tags: 實例標簽訊息
        :type Tags: list of TagInfo
        """
        self.Memory = None
        self.Volume = None
        self.ReplicateSetNum = None
        self.NodeNum = None
        self.MongoVersion = None
        self.MachineCode = None
        self.GoodsNum = None
        self.Zone = None
        self.ClusterType = None
        self.VpcId = None
        self.SubnetId = None
        self.Password = None
        self.ProjectId = None
        self.Tags = None


    def _deserialize(self, params):
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.ReplicateSetNum = params.get("ReplicateSetNum")
        self.NodeNum = params.get("NodeNum")
        self.MongoVersion = params.get("MongoVersion")
        self.MachineCode = params.get("MachineCode")
        self.GoodsNum = params.get("GoodsNum")
        self.Zone = params.get("Zone")
        self.ClusterType = params.get("ClusterType")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Password = params.get("Password")
        self.ProjectId = params.get("ProjectId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateDBInstanceHourResponse(AbstractModel):
    """CreateDBInstanceHour返回參數結構體

    """

    def __init__(self):
        """
        :param DealId: 訂單ID
        :type DealId: str
        :param InstanceIds: 創建的實例ID清單
        :type InstanceIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class CreateDBInstanceRequest(AbstractModel):
    """CreateDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param NodeNum: 每個副本集内節點個數，當前副本集節點數固定爲3，分片從節點數可選，具體參照查詢雲資料庫的售賣規格返回參數
        :type NodeNum: int
        :param Memory: 實例内存大小，單位：GB
        :type Memory: int
        :param Volume: 實例硬碟大小，單位：GB
        :type Volume: int
        :param MongoVersion: 版本號，具體支援的售賣版本請參照查詢雲資料庫的售賣規格（DescribeSpecInfo）返回結果。參數與版本對應關系是MONGO_3_WT：MongoDB 3.2 WiredTiger儲存引擎版本，MONGO_3_ROCKS：MongoDB 3.2 RocksDB儲存引擎版本，MONGO_36_WT：MongoDB 3.6 WiredTiger儲存引擎版本
        :type MongoVersion: str
        :param GoodsNum: 實例數量, 最小值1，最大值爲10
        :type GoodsNum: int
        :param Zone: 實例所屬區域名稱，格式如：ap-guangzhou-2
        :type Zone: str
        :param Period: 實例時長，單位：月，可選值包括 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]
        :type Period: int
        :param MachineCode: 機器類型，HIO：高IO型；HIO10G：高IO萬兆型
        :type MachineCode: str
        :param ClusterType: 實例類型，REPLSET-副本集，SHARD-分片集群
        :type ClusterType: str
        :param ReplicateSetNum: 副本集個數，創建副本集實例時，該參數必須設置爲1；創建分片實例時，具體參照查詢雲資料庫的售賣規格返回參數
        :type ReplicateSetNum: int
        :param ProjectId: 項目ID，不設置爲預設項目
        :type ProjectId: int
        :param VpcId: 私有網絡 ID，如果不傳則預設選擇基礎網絡，請使用 查詢私有網絡清單
        :type VpcId: str
        :param SubnetId: 私有網絡下的子網 ID，如果設置了 UniqVpcId，則 UniqSubnetId 必填，請使用 查詢子網清單
        :type SubnetId: str
        :param Password: 實例密碼，不設置該參數則需要在創建完成後通過設置密碼介面初始化實例密碼。密碼必須是8-16位字元，且至少包含字母、數字和字元 !@#%^*() 中的兩種
        :type Password: str
        :param Tags: 實例標簽訊息
        :type Tags: list of TagInfo
        :param AutoRenewFlag: 自動續約標記，可選值爲：0 - 不自動續約；1 - 自動續約。預設爲不自動續約
        :type AutoRenewFlag: int
        """
        self.NodeNum = None
        self.Memory = None
        self.Volume = None
        self.MongoVersion = None
        self.GoodsNum = None
        self.Zone = None
        self.Period = None
        self.MachineCode = None
        self.ClusterType = None
        self.ReplicateSetNum = None
        self.ProjectId = None
        self.VpcId = None
        self.SubnetId = None
        self.Password = None
        self.Tags = None
        self.AutoRenewFlag = None


    def _deserialize(self, params):
        self.NodeNum = params.get("NodeNum")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.MongoVersion = params.get("MongoVersion")
        self.GoodsNum = params.get("GoodsNum")
        self.Zone = params.get("Zone")
        self.Period = params.get("Period")
        self.MachineCode = params.get("MachineCode")
        self.ClusterType = params.get("ClusterType")
        self.ReplicateSetNum = params.get("ReplicateSetNum")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Password = params.get("Password")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AutoRenewFlag = params.get("AutoRenewFlag")


class CreateDBInstanceResponse(AbstractModel):
    """CreateDBInstance返回參數結構體

    """

    def __init__(self):
        """
        :param DealId: 訂單ID
        :type DealId: str
        :param InstanceIds: 創建的實例ID清單
        :type InstanceIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class DBInstanceInfo(AbstractModel):
    """實例訊息

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param Region: 地域訊息
        :type Region: str
        """
        self.InstanceId = None
        self.Region = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Region = params.get("Region")


class DBInstancePrice(AbstractModel):
    """資料庫實例價格

    """

    def __init__(self):
        """
        :param UnitPrice: 單價
注意：此欄位可能返回 null，表示取不到有效值。
        :type UnitPrice: float
        :param OriginalPrice: 原價
        :type OriginalPrice: float
        :param DiscountPrice: 折扣加
        :type DiscountPrice: float
        """
        self.UnitPrice = None
        self.OriginalPrice = None
        self.DiscountPrice = None


    def _deserialize(self, params):
        self.UnitPrice = params.get("UnitPrice")
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")


class DescribeBackupAccessRequest(AbstractModel):
    """DescribeBackupAccess請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cmgo-p8vnipr5。與雲資料庫控制台頁面中顯示的實例ID相同
        :type InstanceId: str
        :param BackupName: 需要獲取下載授權的備份文件名
        :type BackupName: str
        """
        self.InstanceId = None
        self.BackupName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupName = params.get("BackupName")


class DescribeBackupAccessResponse(AbstractModel):
    """DescribeBackupAccess返回參數結構體

    """

    def __init__(self):
        """
        :param Region: 實例所屬地域
        :type Region: str
        :param Bucket: 備份文件所在儲存桶
        :type Bucket: str
        :param Files: 備份文件的儲存訊息
        :type Files: list of BackupFile
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Region = None
        self.Bucket = None
        self.Files = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Bucket = params.get("Bucket")
        if params.get("Files") is not None:
            self.Files = []
            for item in params.get("Files"):
                obj = BackupFile()
                obj._deserialize(item)
                self.Files.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClientConnectionsRequest(AbstractModel):
    """DescribeClientConnections請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cmgo-p8vnipr5。與雲資料庫控制台頁面中顯示的實例ID相同
        :type InstanceId: str
        :param Limit: 查詢返回記錄條數，預設爲10000。
        :type Limit: int
        :param Offset: 偏移量，預設值爲0。
        :type Offset: int
        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeClientConnectionsResponse(AbstractModel):
    """DescribeClientConnections返回參數結構體

    """

    def __init__(self):
        """
        :param Clients: 用戶端連接訊息，包括用戶端IP和對應IP的連接數量。
        :type Clients: list of ClientConnection
        :param TotalCount: 滿足條件的記錄總條數，可用於分頁查詢。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Clients = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Clients") is not None:
            self.Clients = []
            for item in params.get("Clients"):
                obj = ClientConnection()
                obj._deserialize(item)
                self.Clients.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDBBackupsRequest(AbstractModel):
    """DescribeDBBackups請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cmgo-p8vnipr5。與雲資料庫控制台頁面中顯示的實例ID相同
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeDBBackupsResponse(AbstractModel):
    """DescribeDBBackups返回參數結構體

    """

    def __init__(self):
        """
        :param BackupList: 備份清單
        :type BackupList: list of BackupInfo
        :param TotalCount: 備份總數
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.BackupList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BackupList") is not None:
            self.BackupList = []
            for item in params.get("BackupList"):
                obj = BackupInfo()
                obj._deserialize(item)
                self.BackupList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceDealRequest(AbstractModel):
    """DescribeDBInstanceDeal請求參數結構體

    """

    def __init__(self):
        """
        :param DealId: 訂單ID，通過CreateDBInstance等介面返回
        :type DealId: str
        """
        self.DealId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")


class DescribeDBInstanceDealResponse(AbstractModel):
    """DescribeDBInstanceDeal返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 訂單狀态，1：未支付，2：已支付，3：發貨中，4：發貨成功，5：發貨失敗，6：退款，7：訂單關閉，8：超時未支付關閉。
        :type Status: int
        :param OriginalPrice: 訂單原價。
        :type OriginalPrice: float
        :param DiscountPrice: 訂單折扣價格。
        :type DiscountPrice: float
        :param Action: 訂單行爲，purchase：新購，renew：續約，upgrade：升配，downgrade：降配，refund：退貨退款。
        :type Action: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.OriginalPrice = None
        self.DiscountPrice = None
        self.Action = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")
        self.Action = params.get("Action")
        self.RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 實例ID清單，格式如：cmgo-p8vnipr5。與雲資料庫控制台頁面中顯示的實例ID相同
        :type InstanceIds: list of str
        :param InstanceType: 實例類型，取值範圍：0-所有實例,1-正式實例，2-臨時實例, 3-只讀實例，-1-正式實例+只讀+災備實例
        :type InstanceType: int
        :param ClusterType: 集群類型，取值範圍：0-副本集實例，1-分片實例，-1-所有實例
        :type ClusterType: int
        :param Status: 實例狀态，取值範圍：0-待初始化，1-流程執行中，2-實例有效，-2-實例已過期
        :type Status: list of int
        :param VpcId: 私有網絡的ID，基礎網絡則不傳該參數
        :type VpcId: str
        :param SubnetId: 私有網絡的子網ID，基礎網絡則不傳該參數。入參設置該參數的同時，必須設置相應的VpcId
        :type SubnetId: str
        :param PayMode: 付費類型，取值範圍：0-按量計費，1-包年包月，-1-按量計費+包年包月
        :type PayMode: int
        :param Limit: 單次請求返回的數量，最小值爲1，最大值爲100，預設值爲20
        :type Limit: int
        :param Offset: 偏移量，預設值爲0
        :type Offset: int
        :param OrderBy: 返回結果集排序的欄位，目前支援："ProjectId", "InstanceName", "CreateTime"，預設爲升序排序
        :type OrderBy: str
        :param OrderByType: 返回結果集排序方式，目前支援："ASC"或者"DESC"
        :type OrderByType: str
        :param ProjectIds: 項目 ID
        :type ProjectIds: list of int non-negative
        :param SearchKey: 搜索關鍵詞，支援實例Id、實例名稱、完整IP
        :type SearchKey: str
        """
        self.InstanceIds = None
        self.InstanceType = None
        self.ClusterType = None
        self.Status = None
        self.VpcId = None
        self.SubnetId = None
        self.PayMode = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None
        self.ProjectIds = None
        self.SearchKey = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceType = params.get("InstanceType")
        self.ClusterType = params.get("ClusterType")
        self.Status = params.get("Status")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.PayMode = params.get("PayMode")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        self.ProjectIds = params.get("ProjectIds")
        self.SearchKey = params.get("SearchKey")


class DescribeDBInstancesResponse(AbstractModel):
    """DescribeDBInstances返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合查詢條件的實例總數
        :type TotalCount: int
        :param InstanceDetails: 實例詳細訊息清單
        :type InstanceDetails: list of InstanceDetail
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceDetails") is not None:
            self.InstanceDetails = []
            for item in params.get("InstanceDetails"):
                obj = InstanceDetail()
                obj._deserialize(item)
                self.InstanceDetails.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSlowLogPatternsRequest(AbstractModel):
    """DescribeSlowLogPatterns請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cmgo-p8vnipr5。與雲資料庫控制台頁面中顯示的實例ID相同
        :type InstanceId: str
        :param StartTime: 慢日志起始時間，格式：yyyy-mm-dd hh:mm:ss，如：2019-06-01 10:00:00。查詢起止時間間隔不能超過24小時，只允許查詢最近7天内慢日志。
        :type StartTime: str
        :param EndTime: 慢日志終止時間，格式：yyyy-mm-dd hh:mm:ss，如：2019-06-02 12:00:00。查詢起止時間間隔不能超過24小時，只允許查詢最近7天内慢日志。
        :type EndTime: str
        :param SlowMS: 慢日志執行時間阈值，返回執行時間超過該阈值的慢日志，單位爲毫秒(ms)，最小爲100毫秒。
        :type SlowMS: int
        :param Offset: 偏移量，最小值爲0，最大值爲10000，預設值爲0。
        :type Offset: int
        :param Limit: 分頁大小，最小值爲1，最大值爲100，預設值爲20。
        :type Limit: int
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.SlowMS = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SlowMS = params.get("SlowMS")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeSlowLogPatternsResponse(AbstractModel):
    """DescribeSlowLogPatterns返回參數結構體

    """

    def __init__(self):
        """
        :param Count: 慢日志統計訊息總數
        :type Count: int
        :param SlowLogPatterns: 慢日志統計訊息
        :type SlowLogPatterns: list of SlowLogPattern
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.SlowLogPatterns = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        if params.get("SlowLogPatterns") is not None:
            self.SlowLogPatterns = []
            for item in params.get("SlowLogPatterns"):
                obj = SlowLogPattern()
                obj._deserialize(item)
                self.SlowLogPatterns.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSlowLogsRequest(AbstractModel):
    """DescribeSlowLogs請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cmgo-p8vnipr5。與雲資料庫控制台頁面中顯示的實例ID相同
        :type InstanceId: str
        :param StartTime: 慢日志起始時間，格式：yyyy-mm-dd hh:mm:ss，如：2019-06-01 10:00:00。查詢起止時間間隔不能超過24小時，只允許查詢最近7天内慢日志。
        :type StartTime: str
        :param EndTime: 慢日志終止時間，格式：yyyy-mm-dd hh:mm:ss，如：2019-06-02 12:00:00。查詢起止時間間隔不能超過24小時，只允許查詢最近7天内慢日志。
        :type EndTime: str
        :param SlowMS: 慢日志執行時間阈值，返回執行時間超過該阈值的慢日志，單位爲毫秒(ms)，最小爲100毫秒。
        :type SlowMS: int
        :param Offset: 偏移量，最小值爲0，最大值爲10000，預設值爲0。
        :type Offset: int
        :param Limit: 分頁大小，最小值爲1，最大值爲100，預設值爲20。
        :type Limit: int
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.SlowMS = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SlowMS = params.get("SlowMS")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeSlowLogsResponse(AbstractModel):
    """DescribeSlowLogs返回參數結構體

    """

    def __init__(self):
        """
        :param Count: 慢日志總數
        :type Count: int
        :param SlowLogs: 慢日志詳情
注意：此欄位可能返回 null，表示取不到有效值。
        :type SlowLogs: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.SlowLogs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.SlowLogs = params.get("SlowLogs")
        self.RequestId = params.get("RequestId")


class DescribeSpecInfoRequest(AbstractModel):
    """DescribeSpecInfo請求參數結構體

    """

    def __init__(self):
        """
        :param Zone: 待查詢可用區
        :type Zone: str
        """
        self.Zone = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")


class DescribeSpecInfoResponse(AbstractModel):
    """DescribeSpecInfo返回參數結構體

    """

    def __init__(self):
        """
        :param SpecInfoList: 實例售賣規格訊息清單
        :type SpecInfoList: list of SpecificationInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SpecInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SpecInfoList") is not None:
            self.SpecInfoList = []
            for item in params.get("SpecInfoList"):
                obj = SpecificationInfo()
                obj._deserialize(item)
                self.SpecInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class InquirePriceCreateDBInstancesRequest(AbstractModel):
    """InquirePriceCreateDBInstances請求參數結構體

    """

    def __init__(self):
        """
        :param Zone: 實例所屬區域名稱，格式如：ap-guangzhou-2
        :type Zone: str
        :param NodeNum: 每個副本集内節點個數，當前副本集節點數固定爲3，分片從節點數可選，具體參照查詢雲資料庫的售賣規格返回參數
        :type NodeNum: int
        :param Memory: 實例内存大小，單位：GB
        :type Memory: int
        :param Volume: 實例硬碟大小，單位：GB
        :type Volume: int
        :param MongoVersion: 版本號，具體支援的售賣版本請參照查詢雲資料庫的售賣規格（DescribeSpecInfo）返回結果。參數與版本對應關系是MONGO_3_WT：MongoDB 3.2 WiredTiger儲存引擎版本，MONGO_3_ROCKS：MongoDB 3.2 RocksDB儲存引擎版本，MONGO_36_WT：MongoDB 3.6 WiredTiger儲存引擎版本，MONGO_40_WT：MongoDB 4.0 WiredTiger儲存引擎版本
        :type MongoVersion: str
        :param MachineCode: 機器類型，HIO：高IO型；HIO10G：高IO萬兆型；STDS5：標準型
        :type MachineCode: str
        :param GoodsNum: 實例數量, 最小值1，最大值爲10
        :type GoodsNum: int
        :param Period: 實例時長，單位：月，可選值包括[1,2,3,4,5,6,7,8,9,10,11,12,24,36]
        :type Period: int
        :param ClusterType: 實例類型，REPLSET-副本集，SHARD-分片集群，STANDALONE-單節點
        :type ClusterType: str
        :param ReplicateSetNum: 副本集個數，創建副本集實例時，該參數必須設置爲1；創建分片實例時，具體參照查詢雲資料庫的售賣規格返回參數；若爲單節點實例，該參數設置爲0
        :type ReplicateSetNum: int
        """
        self.Zone = None
        self.NodeNum = None
        self.Memory = None
        self.Volume = None
        self.MongoVersion = None
        self.MachineCode = None
        self.GoodsNum = None
        self.Period = None
        self.ClusterType = None
        self.ReplicateSetNum = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.NodeNum = params.get("NodeNum")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.MongoVersion = params.get("MongoVersion")
        self.MachineCode = params.get("MachineCode")
        self.GoodsNum = params.get("GoodsNum")
        self.Period = params.get("Period")
        self.ClusterType = params.get("ClusterType")
        self.ReplicateSetNum = params.get("ReplicateSetNum")


class InquirePriceCreateDBInstancesResponse(AbstractModel):
    """InquirePriceCreateDBInstances返回參數結構體

    """

    def __init__(self):
        """
        :param Price: 價格
        :type Price: :class:`taifucloudcloud.mongodb.v20190725.models.DBInstancePrice`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = DBInstancePrice()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquirePriceModifyDBInstanceSpecRequest(AbstractModel):
    """InquirePriceModifyDBInstanceSpec請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cmgo-p8vnipr5。與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        :param Memory: 變更配置後實例内存大小，單位：GB。
        :type Memory: int
        :param Volume: 變更配置後實例磁盤大小，單位：GB。
        :type Volume: int
        """
        self.InstanceId = None
        self.Memory = None
        self.Volume = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")


class InquirePriceModifyDBInstanceSpecResponse(AbstractModel):
    """InquirePriceModifyDBInstanceSpec返回參數結構體

    """

    def __init__(self):
        """
        :param Price: 價格。
        :type Price: :class:`taifucloudcloud.mongodb.v20190725.models.DBInstancePrice`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = DBInstancePrice()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquirePriceRenewDBInstancesRequest(AbstractModel):
    """InquirePriceRenewDBInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 實例ID，格式如：cmgo-p8vnipr5。與雲資料庫控制台頁面中顯示的實例ID相同，介面單次最多只支援5個實例進行操作。
        :type InstanceIds: list of str
        :param InstanceChargePrepaid: 預付費模式（即包年包月）相關參數設置。通過該參數可以指定包年包月實例的續約時長、是否設置自動續約等屬性。
        :type InstanceChargePrepaid: :class:`taifucloudcloud.mongodb.v20190725.models.InstanceChargePrepaid`
        """
        self.InstanceIds = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))


class InquirePriceRenewDBInstancesResponse(AbstractModel):
    """InquirePriceRenewDBInstances返回參數結構體

    """

    def __init__(self):
        """
        :param Price: 價格
        :type Price: :class:`taifucloudcloud.mongodb.v20190725.models.DBInstancePrice`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = DBInstancePrice()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InstanceChargePrepaid(AbstractModel):
    """描述了實例的計費模式

    """

    def __init__(self):
        """
        :param Period: 購買實例的時長，單位：月。取值範圍：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36。預設爲1。
        :type Period: int
        :param RenewFlag: 自動續約標識。取值範圍：
NOTIFY_AND_AUTO_RENEW：通知過期且自動續約
NOTIFY_AND_MANUAL_RENEW：通知過期不自動續約
DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知過期不自動續約

預設取值：NOTIFY_AND_MANUAL_RENEW。若該參數指定爲NOTIFY_AND_AUTO_RENEW，在帳戶餘額充足的情況下，實例到期後将按月自動續約。
        :type RenewFlag: str
        """
        self.Period = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RenewFlag = params.get("RenewFlag")


class InstanceDetail(AbstractModel):
    """實例詳情

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param InstanceName: 實例名稱
        :type InstanceName: str
        :param PayMode: 付費類型，可能的返回值：1-包年包月；0-按量計費
        :type PayMode: int
        :param ProjectId: 項目ID
        :type ProjectId: int
        :param ClusterType: 集群類型，可能的返回值：0-副本集實例，1-分片實例，
        :type ClusterType: int
        :param Region: 地域訊息
        :type Region: str
        :param Zone: 可用區訊息
        :type Zone: str
        :param NetType: 網絡類型，可能的返回值：0-基礎網絡，1-私有網絡
        :type NetType: int
        :param VpcId: 私有網絡的ID
        :type VpcId: str
        :param SubnetId: 私有網絡的子網ID
        :type SubnetId: str
        :param Status: 實例狀态，可能的返回值：0-待初始化，1-流程處理中，2-運作中，-2-實例已過期
        :type Status: int
        :param Vip: 實例IP
        :type Vip: str
        :param Vport: 端口號
        :type Vport: int
        :param CreateTime: 實例創建時間
        :type CreateTime: str
        :param DeadLine: 實例到期時間
        :type DeadLine: str
        :param MongoVersion: 實例版本訊息
        :type MongoVersion: str
        :param Memory: 實例内存規格，單位爲MB
        :type Memory: int
        :param Volume: 實例磁盤規格，單位爲MB
        :type Volume: int
        :param CpuNum: 實例CPU核心數
        :type CpuNum: int
        :param MachineType: 實例機器類型
        :type MachineType: str
        :param SecondaryNum: 實例從節點數
        :type SecondaryNum: int
        :param ReplicationSetNum: 實例分片數
        :type ReplicationSetNum: int
        :param AutoRenewFlag: 實例自動續約標志，可能的返回值：0-手動續約，1-自動續約，2-确認不續約
        :type AutoRenewFlag: int
        :param UsedVolume: 已用容量，單位MB
        :type UsedVolume: int
        :param MaintenanceStart: 維護視窗起始時間
        :type MaintenanceStart: str
        :param MaintenanceEnd: 維護視窗結束時間
        :type MaintenanceEnd: str
        :param ReplicaSets: 分片訊息
        :type ReplicaSets: list of ShardInfo
        :param ReadonlyInstances: 只讀實例訊息
        :type ReadonlyInstances: list of DBInstanceInfo
        :param StandbyInstances: 災備實例訊息
        :type StandbyInstances: list of DBInstanceInfo
        :param CloneInstances: 臨時實例訊息
        :type CloneInstances: list of DBInstanceInfo
        :param RelatedInstance: 關聯實例訊息，對於正式實例，該欄位表示它的臨時實例訊息；對於臨時實例，則表示它的正式實例訊息;如果爲只讀/災備實例,則表示他的主實例訊息
        :type RelatedInstance: :class:`taifucloudcloud.mongodb.v20190725.models.DBInstanceInfo`
        :param Tags: 實例標簽訊息集合
        :type Tags: list of TagInfo
        :param InstanceVer: 實例版本標記
        :type InstanceVer: int
        :param ClusterVer: 實例版本標記
        :type ClusterVer: int
        :param Protocol: 協議訊息，可能的返回值：1-mongodb，2-dynamodb
        :type Protocol: int
        :param InstanceType: 實例類型，可能的返回值，1-正式實例，2-臨時實例，3-只讀實例，4-災備實例
        :type InstanceType: int
        :param InstanceStatusDesc: 實例狀态描述
        :type InstanceStatusDesc: str
        :param RealInstanceId: 實例對應的物理實例id，回檔並替換過的實例有不同的InstanceId和RealInstanceId，從barad獲取監控數據等場景下需要用物理id獲取
        :type RealInstanceId: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.PayMode = None
        self.ProjectId = None
        self.ClusterType = None
        self.Region = None
        self.Zone = None
        self.NetType = None
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.Vip = None
        self.Vport = None
        self.CreateTime = None
        self.DeadLine = None
        self.MongoVersion = None
        self.Memory = None
        self.Volume = None
        self.CpuNum = None
        self.MachineType = None
        self.SecondaryNum = None
        self.ReplicationSetNum = None
        self.AutoRenewFlag = None
        self.UsedVolume = None
        self.MaintenanceStart = None
        self.MaintenanceEnd = None
        self.ReplicaSets = None
        self.ReadonlyInstances = None
        self.StandbyInstances = None
        self.CloneInstances = None
        self.RelatedInstance = None
        self.Tags = None
        self.InstanceVer = None
        self.ClusterVer = None
        self.Protocol = None
        self.InstanceType = None
        self.InstanceStatusDesc = None
        self.RealInstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.PayMode = params.get("PayMode")
        self.ProjectId = params.get("ProjectId")
        self.ClusterType = params.get("ClusterType")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.NetType = params.get("NetType")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.CreateTime = params.get("CreateTime")
        self.DeadLine = params.get("DeadLine")
        self.MongoVersion = params.get("MongoVersion")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.CpuNum = params.get("CpuNum")
        self.MachineType = params.get("MachineType")
        self.SecondaryNum = params.get("SecondaryNum")
        self.ReplicationSetNum = params.get("ReplicationSetNum")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.UsedVolume = params.get("UsedVolume")
        self.MaintenanceStart = params.get("MaintenanceStart")
        self.MaintenanceEnd = params.get("MaintenanceEnd")
        if params.get("ReplicaSets") is not None:
            self.ReplicaSets = []
            for item in params.get("ReplicaSets"):
                obj = ShardInfo()
                obj._deserialize(item)
                self.ReplicaSets.append(obj)
        if params.get("ReadonlyInstances") is not None:
            self.ReadonlyInstances = []
            for item in params.get("ReadonlyInstances"):
                obj = DBInstanceInfo()
                obj._deserialize(item)
                self.ReadonlyInstances.append(obj)
        if params.get("StandbyInstances") is not None:
            self.StandbyInstances = []
            for item in params.get("StandbyInstances"):
                obj = DBInstanceInfo()
                obj._deserialize(item)
                self.StandbyInstances.append(obj)
        if params.get("CloneInstances") is not None:
            self.CloneInstances = []
            for item in params.get("CloneInstances"):
                obj = DBInstanceInfo()
                obj._deserialize(item)
                self.CloneInstances.append(obj)
        if params.get("RelatedInstance") is not None:
            self.RelatedInstance = DBInstanceInfo()
            self.RelatedInstance._deserialize(params.get("RelatedInstance"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.InstanceVer = params.get("InstanceVer")
        self.ClusterVer = params.get("ClusterVer")
        self.Protocol = params.get("Protocol")
        self.InstanceType = params.get("InstanceType")
        self.InstanceStatusDesc = params.get("InstanceStatusDesc")
        self.RealInstanceId = params.get("RealInstanceId")


class IsolateDBInstanceRequest(AbstractModel):
    """IsolateDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cmgo-p8vnipr5。與雲資料庫控制台頁面中顯示的實例ID相同
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class IsolateDBInstanceResponse(AbstractModel):
    """IsolateDBInstance返回參數結構體

    """

    def __init__(self):
        """
        :param AsyncRequestId: 異步任務的請求 ID，可使用此 ID 查詢異步任務的執行結果。
        :type AsyncRequestId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceSpecRequest(AbstractModel):
    """ModifyDBInstanceSpec請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cmgo-p8vnipr5。與雲資料庫控制台頁面中顯示的實例ID相同
        :type InstanceId: str
        :param Memory: 實例配置變更後的内存大小，單位：GB。内存和磁盤必須同時升配或同時降配
        :type Memory: int
        :param Volume: 實例配置變更後的硬碟大小，單位：GB。内存和磁盤必須同時升配或同時降配。降配時，新的磁盤參數必須大於已用磁盤容量的1.2倍
        :type Volume: int
        :param OplogSize: 實例配置變更後oplog的大小，單位：GB，預設爲磁盤空間的10%，允許設置的最小值爲磁盤的10%，最大值爲磁盤的90%
        :type OplogSize: int
        """
        self.InstanceId = None
        self.Memory = None
        self.Volume = None
        self.OplogSize = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.OplogSize = params.get("OplogSize")


class ModifyDBInstanceSpecResponse(AbstractModel):
    """ModifyDBInstanceSpec返回參數結構體

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


class OfflineIsolatedDBInstanceRequest(AbstractModel):
    """OfflineIsolatedDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cmgo-p8vnipr5。與雲資料庫控制台頁面中顯示的實例ID相同
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class OfflineIsolatedDBInstanceResponse(AbstractModel):
    """OfflineIsolatedDBInstance返回參數結構體

    """

    def __init__(self):
        """
        :param AsyncRequestId: 異步任務的請求 ID，可使用此 ID 查詢異步任務的執行結果。
        :type AsyncRequestId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class RenameInstanceRequest(AbstractModel):
    """RenameInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cmgo-p8vnipr5。與雲資料庫控制台頁面中顯示的實例ID相同
        :type InstanceId: str
        :param NewName: 實例名稱
        :type NewName: str
        """
        self.InstanceId = None
        self.NewName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.NewName = params.get("NewName")


class RenameInstanceResponse(AbstractModel):
    """RenameInstance返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RenewDBInstancesRequest(AbstractModel):
    """RenewDBInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 一個或多個待操作的實例ID。可通過DescribeInstances介面返回值中的InstanceId獲取。每次請求批次實例的上限爲100。
        :type InstanceIds: list of str
        :param InstanceChargePrepaid: 預付費模式，即包年包月相關參數設置。通過該參數可以指定包年包月實例的續約時長、是否設置自動續約等屬性。包年包月實例該參數爲必傳參數。
        :type InstanceChargePrepaid: :class:`taifucloudcloud.mongodb.v20190725.models.InstanceChargePrepaid`
        """
        self.InstanceIds = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))


class RenewDBInstancesResponse(AbstractModel):
    """RenewDBInstances返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ShardInfo(AbstractModel):
    """實例分片詳情

    """

    def __init__(self):
        """
        :param UsedVolume: 分片已使用容量
        :type UsedVolume: float
        :param ReplicaSetId: 分片ID
        :type ReplicaSetId: str
        :param ReplicaSetName: 分片名
        :type ReplicaSetName: str
        :param Memory: 分片内存規格，單位爲MB
        :type Memory: int
        :param Volume: 分片磁盤規格，單位爲MB
        :type Volume: int
        :param OplogSize: 分片Oplog大小，單位爲MB
        :type OplogSize: int
        :param SecondaryNum: 分片從節點數
        :type SecondaryNum: int
        :param RealReplicaSetId: 分片物理id
        :type RealReplicaSetId: str
        """
        self.UsedVolume = None
        self.ReplicaSetId = None
        self.ReplicaSetName = None
        self.Memory = None
        self.Volume = None
        self.OplogSize = None
        self.SecondaryNum = None
        self.RealReplicaSetId = None


    def _deserialize(self, params):
        self.UsedVolume = params.get("UsedVolume")
        self.ReplicaSetId = params.get("ReplicaSetId")
        self.ReplicaSetName = params.get("ReplicaSetName")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.OplogSize = params.get("OplogSize")
        self.SecondaryNum = params.get("SecondaryNum")
        self.RealReplicaSetId = params.get("RealReplicaSetId")


class SlowLogPattern(AbstractModel):
    """用於描述MongoDB資料庫慢日志統計訊息

    """

    def __init__(self):
        """
        :param Pattern: 慢日志模式
        :type Pattern: str
        :param MaxTime: 最大執行時間
        :type MaxTime: int
        :param AverageTime: 平均執行時間
        :type AverageTime: int
        :param Total: 該模式慢日志條數
        :type Total: int
        """
        self.Pattern = None
        self.MaxTime = None
        self.AverageTime = None
        self.Total = None


    def _deserialize(self, params):
        self.Pattern = params.get("Pattern")
        self.MaxTime = params.get("MaxTime")
        self.AverageTime = params.get("AverageTime")
        self.Total = params.get("Total")


class SpecItem(AbstractModel):
    """mongodb售賣規格

    """

    def __init__(self):
        """
        :param SpecCode: 規格訊息標識
        :type SpecCode: str
        :param Status: 規格有效標志，取值：0-停止售賣，1-開放售賣
        :type Status: int
        :param Cpu: 規格有效標志，取值：0-停止售賣，1-開放售賣
        :type Cpu: int
        :param Memory: 内存規格，單位爲MB
        :type Memory: int
        :param DefaultStorage: 預設磁盤規格，單位MB
        :type DefaultStorage: int
        :param MaxStorage: 最大磁盤規格，單位MB
        :type MaxStorage: int
        :param MinStorage: 最小磁盤規格，單位MB
        :type MinStorage: int
        :param Qps: 可承載qps訊息
        :type Qps: int
        :param Conns: 連接數限制
        :type Conns: int
        :param MongoVersionCode: 實例mongodb版本訊息
        :type MongoVersionCode: str
        :param MongoVersionValue: 實例mongodb版本號
        :type MongoVersionValue: int
        :param Version: 實例mongodb版本號（短）
        :type Version: str
        :param EngineName: 儲存引擎
        :type EngineName: str
        :param ClusterType: 集群類型，取值：1-分片集群，0-副本集集群
        :type ClusterType: int
        :param MinNodeNum: 最小副本集從節點數
        :type MinNodeNum: int
        :param MaxNodeNum: 最大副本集從節點數
        :type MaxNodeNum: int
        :param MinReplicateSetNum: 最小分片數
        :type MinReplicateSetNum: int
        :param MaxReplicateSetNum: 最大分片數
        :type MaxReplicateSetNum: int
        :param MinReplicateSetNodeNum: 最小分片從節點數
        :type MinReplicateSetNodeNum: int
        :param MaxReplicateSetNodeNum: 最大分片從節點數
        :type MaxReplicateSetNodeNum: int
        :param MachineType: 機器類型，取值：0-HIO，4-HIO10G
        :type MachineType: str
        """
        self.SpecCode = None
        self.Status = None
        self.Cpu = None
        self.Memory = None
        self.DefaultStorage = None
        self.MaxStorage = None
        self.MinStorage = None
        self.Qps = None
        self.Conns = None
        self.MongoVersionCode = None
        self.MongoVersionValue = None
        self.Version = None
        self.EngineName = None
        self.ClusterType = None
        self.MinNodeNum = None
        self.MaxNodeNum = None
        self.MinReplicateSetNum = None
        self.MaxReplicateSetNum = None
        self.MinReplicateSetNodeNum = None
        self.MaxReplicateSetNodeNum = None
        self.MachineType = None


    def _deserialize(self, params):
        self.SpecCode = params.get("SpecCode")
        self.Status = params.get("Status")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.DefaultStorage = params.get("DefaultStorage")
        self.MaxStorage = params.get("MaxStorage")
        self.MinStorage = params.get("MinStorage")
        self.Qps = params.get("Qps")
        self.Conns = params.get("Conns")
        self.MongoVersionCode = params.get("MongoVersionCode")
        self.MongoVersionValue = params.get("MongoVersionValue")
        self.Version = params.get("Version")
        self.EngineName = params.get("EngineName")
        self.ClusterType = params.get("ClusterType")
        self.MinNodeNum = params.get("MinNodeNum")
        self.MaxNodeNum = params.get("MaxNodeNum")
        self.MinReplicateSetNum = params.get("MinReplicateSetNum")
        self.MaxReplicateSetNum = params.get("MaxReplicateSetNum")
        self.MinReplicateSetNodeNum = params.get("MinReplicateSetNodeNum")
        self.MaxReplicateSetNodeNum = params.get("MaxReplicateSetNodeNum")
        self.MachineType = params.get("MachineType")


class SpecificationInfo(AbstractModel):
    """實例規格訊息

    """

    def __init__(self):
        """
        :param Region: 地域訊息
        :type Region: str
        :param Zone: 可用區訊息
        :type Zone: str
        :param SpecItems: 售賣規格訊息
        :type SpecItems: list of SpecItem
        """
        self.Region = None
        self.Zone = None
        self.SpecItems = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        if params.get("SpecItems") is not None:
            self.SpecItems = []
            for item in params.get("SpecItems"):
                obj = SpecItem()
                obj._deserialize(item)
                self.SpecItems.append(obj)


class TagInfo(AbstractModel):
    """實例標簽訊息

    """

    def __init__(self):
        """
        :param TagKey: 標簽鍵
        :type TagKey: str
        :param TagValue: 標簽值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")