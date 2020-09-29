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


class AddShardConfig(AbstractModel):
    """升級實例 -- 新增分片類型

    """

    def __init__(self):
        """
        :param ShardCount: 新增分片的數量
        :type ShardCount: int
        :param ShardMemory: 分片内存大小，單位 GB
        :type ShardMemory: int
        :param ShardStorage: 分片儲存大小，單位 GB
        :type ShardStorage: int
        """
        self.ShardCount = None
        self.ShardMemory = None
        self.ShardStorage = None


    def _deserialize(self, params):
        self.ShardCount = params.get("ShardCount")
        self.ShardMemory = params.get("ShardMemory")
        self.ShardStorage = params.get("ShardStorage")


class CloneAccountRequest(AbstractModel):
    """CloneAccount請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param SrcUser: 源用戶帳戶名
        :type SrcUser: str
        :param SrcHost: 源用戶HOST
        :type SrcHost: str
        :param DstUser: 目的用戶帳戶名
        :type DstUser: str
        :param DstHost: 目的用戶HOST
        :type DstHost: str
        :param DstDesc: 目的用戶帳戶描述
        :type DstDesc: str
        """
        self.InstanceId = None
        self.SrcUser = None
        self.SrcHost = None
        self.DstUser = None
        self.DstHost = None
        self.DstDesc = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SrcUser = params.get("SrcUser")
        self.SrcHost = params.get("SrcHost")
        self.DstUser = params.get("DstUser")
        self.DstHost = params.get("DstHost")
        self.DstDesc = params.get("DstDesc")


class CloneAccountResponse(AbstractModel):
    """CloneAccount返回參數結構體

    """

    def __init__(self):
        """
        :param FlowId: 異步任務流程ID
        :type FlowId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CloseDBExtranetAccessRequest(AbstractModel):
    """CloseDBExtranetAccess請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 待關閉外網訪問的實例ID。形如：dcdbt-ow728lmc，可以通過 DescribeDCDBInstances 查詢實例詳情獲得。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class CloseDBExtranetAccessResponse(AbstractModel):
    """CloseDBExtranetAccess返回參數結構體

    """

    def __init__(self):
        """
        :param FlowId: 異步任務Id，可通過 DescribeFlow 查詢任務狀态。
        :type FlowId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ConstraintRange(AbstractModel):
    """約束類型值的範圍

    """

    def __init__(self):
        """
        :param Min: 約束類型爲section時的最小值
        :type Min: str
        :param Max: 約束類型爲section時的最大值
        :type Max: str
        """
        self.Min = None
        self.Max = None


    def _deserialize(self, params):
        self.Min = params.get("Min")
        self.Max = params.get("Max")


class CopyAccountPrivilegesRequest(AbstractModel):
    """CopyAccountPrivileges請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param SrcUserName: 源用戶名
        :type SrcUserName: str
        :param SrcHost: 源用戶允許的訪問 host
        :type SrcHost: str
        :param DstUserName: 目的用戶名
        :type DstUserName: str
        :param DstHost: 目的用戶允許的訪問 host
        :type DstHost: str
        :param SrcReadOnly: 源賬號的 ReadOnly 屬性
        :type SrcReadOnly: str
        :param DstReadOnly: 目的賬號的 ReadOnly 屬性
        :type DstReadOnly: str
        """
        self.InstanceId = None
        self.SrcUserName = None
        self.SrcHost = None
        self.DstUserName = None
        self.DstHost = None
        self.SrcReadOnly = None
        self.DstReadOnly = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SrcUserName = params.get("SrcUserName")
        self.SrcHost = params.get("SrcHost")
        self.DstUserName = params.get("DstUserName")
        self.DstHost = params.get("DstHost")
        self.SrcReadOnly = params.get("SrcReadOnly")
        self.DstReadOnly = params.get("DstReadOnly")


class CopyAccountPrivilegesResponse(AbstractModel):
    """CopyAccountPrivileges返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAccountRequest(AbstractModel):
    """CreateAccount請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：dcdbt-ow728lmc，可以通過 DescribeDCDBInstances 查詢實例詳情獲得。
        :type InstanceId: str
        :param UserName: AccountName
        :type UserName: str
        :param Host: 可以登入的主機，與mysql 賬號的 host 格式一緻，可以支援通配符，例如 %，10.%，10.20.%。
        :type Host: str
        :param Password: 賬號密碼，由字母、數字或常見符號組成，不能包含分號、單引號和雙引號，長度爲6~32位。
        :type Password: str
        :param ReadOnly: 是否創建爲只讀賬號，0：否， 1：該賬號的sql請求優先選擇備機執行，備機不可用時選擇主機執行，2：優先選擇備機執行，備機不可用時操作失敗，3：只從備機讀取。
        :type ReadOnly: int
        :param Description: 賬號備注，可以包含中文、英文字元、常見符號和數字，長度爲0~256字元
        :type Description: str
        :param DelayThresh: 如果備機延遲超過本參數設置值，系統将認爲備機發生故障
建議該參數值大於10。當ReadOnly選擇1、2時該參數生效。
        :type DelayThresh: int
        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.Password = None
        self.ReadOnly = None
        self.Description = None
        self.DelayThresh = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.Password = params.get("Password")
        self.ReadOnly = params.get("ReadOnly")
        self.Description = params.get("Description")
        self.DelayThresh = params.get("DelayThresh")


class CreateAccountResponse(AbstractModel):
    """CreateAccount返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例Id，透傳入參。
        :type InstanceId: str
        :param UserName: 用戶名，透傳入參。
        :type UserName: str
        :param Host: 允許訪問的 host，透傳入參。
        :type Host: str
        :param ReadOnly: 透傳入參。
        :type ReadOnly: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.ReadOnly = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.ReadOnly = params.get("ReadOnly")
        self.RequestId = params.get("RequestId")


class CreateDCDBInstanceRequest(AbstractModel):
    """CreateDCDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param Zones: 分片節點可用區分布，最多可填兩個可用區。當分片規格爲一主兩從時，其中兩個節點在第一個可用區。
        :type Zones: list of str
        :param Period: 欲購買的時長，單位：月。
        :type Period: int
        :param ShardMemory: 分片内存大小，單位：GB，可以通過 DescribeShardSpec
 查詢實例規格獲得。
        :type ShardMemory: int
        :param ShardStorage: 分片儲存空間大小，單位：GB，可以通過 DescribeShardSpec
 查詢實例規格獲得。
        :type ShardStorage: int
        :param ShardNodeCount: 單個分片節點個數，可以通過 DescribeShardSpec
 查詢實例規格獲得。
        :type ShardNodeCount: int
        :param ShardCount: 實例分片個數，可選範圍2-8，可以通過升級實例進行新增分片到最多64個分片。
        :type ShardCount: int
        :param Count: 欲購買實例的數量，目前只支援購買1個實例
        :type Count: int
        :param ProjectId: 項目 ID，可以通過檢視項目清單獲取，不傳則關聯到預設項目
        :type ProjectId: int
        :param VpcId: 虛拟私有網絡 ID，不傳或傳空表示創建爲基礎網絡
        :type VpcId: str
        :param SubnetId: 虛拟私有網絡子網 ID，VpcId不爲空時必填
        :type SubnetId: str
        :param DbVersionId: 資料庫引擎版本，當前可選：10.0.10，10.1.9，5.7.17。
10.0.10 - Mariadb 10.0.10；
10.1.9 - Mariadb 10.1.9；
5.7.17 - Percona 5.7.17。
如果不填的話，預設爲10.1.9，表示Mariadb 10.1.9。
        :type DbVersionId: str
        :param AutoVoucher: 是否自動使用 進行支付，預設不使用。
        :type AutoVoucher: bool
        :param VoucherIds:  ID清單，目前僅支援指定一張 。
        :type VoucherIds: list of str
        """
        self.Zones = None
        self.Period = None
        self.ShardMemory = None
        self.ShardStorage = None
        self.ShardNodeCount = None
        self.ShardCount = None
        self.Count = None
        self.ProjectId = None
        self.VpcId = None
        self.SubnetId = None
        self.DbVersionId = None
        self.AutoVoucher = None
        self.VoucherIds = None


    def _deserialize(self, params):
        self.Zones = params.get("Zones")
        self.Period = params.get("Period")
        self.ShardMemory = params.get("ShardMemory")
        self.ShardStorage = params.get("ShardStorage")
        self.ShardNodeCount = params.get("ShardNodeCount")
        self.ShardCount = params.get("ShardCount")
        self.Count = params.get("Count")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.DbVersionId = params.get("DbVersionId")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")


class CreateDCDBInstanceResponse(AbstractModel):
    """CreateDCDBInstance返回參數結構體

    """

    def __init__(self):
        """
        :param DealName: 長訂單號。可以據此調用 DescribeOrders
 查詢訂單詳細訊息，或在支付失敗時調用用戶賬號相關介面進行支付。
        :type DealName: str
        :param InstanceIds: 訂單對應的實例 ID 清單，如果此處沒有返回實例 ID，可以通過訂單查詢介面獲取。還可通過實例查詢介面查詢實例是否創建完成。
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class DBAccount(AbstractModel):
    """雲資料庫賬號訊息

    """

    def __init__(self):
        """
        :param UserName: 用戶名
        :type UserName: str
        :param Host: 用戶可以從哪台主機登入（對應 MySQL 用戶的 host 欄位，UserName + Host 唯一標識一個用戶，IP形式，IP段以%結尾；支援填入%；爲空預設等於%）
        :type Host: str
        :param Description: 用戶備注訊息
        :type Description: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param UpdateTime: 最後更新時間
        :type UpdateTime: str
        :param ReadOnly: 只讀標記，0：否， 1：該賬號的sql請求優先選擇備機執行，備機不可用時選擇主機執行，2：優先選擇備機執行，備機不可用時操作失敗。
        :type ReadOnly: int
        :param DelayThresh: 如果備機延遲超過本參數設置值，系統将認爲備機發生故障
建議該參數值大於10。當ReadOnly選擇1、2時該參數生效。
        :type DelayThresh: int
        """
        self.UserName = None
        self.Host = None
        self.Description = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ReadOnly = None
        self.DelayThresh = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ReadOnly = params.get("ReadOnly")
        self.DelayThresh = params.get("DelayThresh")


class DBParamValue(AbstractModel):
    """雲資料庫參數訊息。

    """

    def __init__(self):
        """
        :param Param: 參數名稱
        :type Param: str
        :param Value: 參數值
        :type Value: str
        """
        self.Param = None
        self.Value = None


    def _deserialize(self, params):
        self.Param = params.get("Param")
        self.Value = params.get("Value")


class DCDBInstanceInfo(AbstractModel):
    """分布式資料庫實例訊息

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param InstanceName: 實例名稱
        :type InstanceName: str
        :param AppId: APPID
        :type AppId: int
        :param ProjectId: 項目ID
        :type ProjectId: int
        :param Region: 地域
        :type Region: str
        :param Zone: 可用區
        :type Zone: str
        :param VpcId: VPC數字ID
        :type VpcId: int
        :param SubnetId: Subnet數字ID
        :type SubnetId: int
        :param StatusDesc: 狀态中文描述
        :type StatusDesc: str
        :param Status: 狀态
        :type Status: int
        :param Vip: 内網IP
        :type Vip: str
        :param Vport: 内網端口
        :type Vport: int
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param AutoRenewFlag: 自動續約標志
        :type AutoRenewFlag: int
        :param Memory: 内存大小，單位 GB
        :type Memory: int
        :param Storage: 儲存大小，單位 GB
        :type Storage: int
        :param ShardCount: 分片個數
        :type ShardCount: int
        :param PeriodEndTime: 到期時間
        :type PeriodEndTime: str
        :param IsolatedTimestamp: 隔離時間
        :type IsolatedTimestamp: str
        :param Uin: UIN
        :type Uin: str
        :param ShardDetail: 分片詳情
        :type ShardDetail: list of ShardInfo
        :param NodeCount: 節點數，2 爲一主一從， 3 爲一主二從
        :type NodeCount: int
        :param IsTmp: 臨時實例標記，0 爲非臨時實例
        :type IsTmp: int
        :param ExclusterId: 獨享集群Id，爲空表示非獨享集群實例
        :type ExclusterId: str
        :param UniqueVpcId: 字串型的私有網絡Id
        :type UniqueVpcId: str
        :param UniqueSubnetId: 字串型的私有網絡子網Id
        :type UniqueSubnetId: str
        :param Id: 數字實例Id（過時欄位，請勿依賴該值）
        :type Id: int
        :param WanDomain: 外網訪問的域名，公網可解析
        :type WanDomain: str
        :param WanVip: 外網 IP 網址，公網可訪問
        :type WanVip: str
        :param WanPort: 外網端口
        :type WanPort: int
        :param Pid: 産品類型 Id（過時欄位，請勿依賴該值）
        :type Pid: int
        :param UpdateTime: 實例最後更新時間，格式爲 2006-01-02 15:04:05
        :type UpdateTime: str
        :param DbEngine: 資料庫引擎
        :type DbEngine: str
        :param DbVersion: 資料庫引擎版本
        :type DbVersion: str
        :param Paymode: 付費模式
        :type Paymode: str
        :param Locker: 實例處於異步任務狀态時，表示異步任務流程ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type Locker: int
        :param WanStatus: 外網狀态，0-未開通；1-已開通；2-關閉；3-開通中
        :type WanStatus: int
        :param IsAuditSupported: 該實例是否支援審計。1-支援；0-不支援
        :type IsAuditSupported: int
        """
        self.InstanceId = None
        self.InstanceName = None
        self.AppId = None
        self.ProjectId = None
        self.Region = None
        self.Zone = None
        self.VpcId = None
        self.SubnetId = None
        self.StatusDesc = None
        self.Status = None
        self.Vip = None
        self.Vport = None
        self.CreateTime = None
        self.AutoRenewFlag = None
        self.Memory = None
        self.Storage = None
        self.ShardCount = None
        self.PeriodEndTime = None
        self.IsolatedTimestamp = None
        self.Uin = None
        self.ShardDetail = None
        self.NodeCount = None
        self.IsTmp = None
        self.ExclusterId = None
        self.UniqueVpcId = None
        self.UniqueSubnetId = None
        self.Id = None
        self.WanDomain = None
        self.WanVip = None
        self.WanPort = None
        self.Pid = None
        self.UpdateTime = None
        self.DbEngine = None
        self.DbVersion = None
        self.Paymode = None
        self.Locker = None
        self.WanStatus = None
        self.IsAuditSupported = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.AppId = params.get("AppId")
        self.ProjectId = params.get("ProjectId")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.StatusDesc = params.get("StatusDesc")
        self.Status = params.get("Status")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.CreateTime = params.get("CreateTime")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.ShardCount = params.get("ShardCount")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.IsolatedTimestamp = params.get("IsolatedTimestamp")
        self.Uin = params.get("Uin")
        if params.get("ShardDetail") is not None:
            self.ShardDetail = []
            for item in params.get("ShardDetail"):
                obj = ShardInfo()
                obj._deserialize(item)
                self.ShardDetail.append(obj)
        self.NodeCount = params.get("NodeCount")
        self.IsTmp = params.get("IsTmp")
        self.ExclusterId = params.get("ExclusterId")
        self.UniqueVpcId = params.get("UniqueVpcId")
        self.UniqueSubnetId = params.get("UniqueSubnetId")
        self.Id = params.get("Id")
        self.WanDomain = params.get("WanDomain")
        self.WanVip = params.get("WanVip")
        self.WanPort = params.get("WanPort")
        self.Pid = params.get("Pid")
        self.UpdateTime = params.get("UpdateTime")
        self.DbEngine = params.get("DbEngine")
        self.DbVersion = params.get("DbVersion")
        self.Paymode = params.get("Paymode")
        self.Locker = params.get("Locker")
        self.WanStatus = params.get("WanStatus")
        self.IsAuditSupported = params.get("IsAuditSupported")


class DCDBShardInfo(AbstractModel):
    """描述分布式資料庫分片訊息。

    """

    def __init__(self):
        """
        :param InstanceId: 所屬實例Id
        :type InstanceId: str
        :param ShardSerialId: 分片SQL透傳Id，用於将sql透傳到指定分片執行
        :type ShardSerialId: str
        :param ShardInstanceId: 全局唯一的分片Id
        :type ShardInstanceId: str
        :param Status: 狀态：0 創建中，1 流程處理中， 2 運作中，3 分片未初始化
        :type Status: int
        :param StatusDesc: 狀态中文描述
        :type StatusDesc: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param VpcId: 字串格式的私有網絡Id
        :type VpcId: str
        :param SubnetId: 字串格式的私有網絡子網Id
        :type SubnetId: str
        :param ProjectId: 項目ID
        :type ProjectId: int
        :param Region: 地域
        :type Region: str
        :param Zone: 可用區
        :type Zone: str
        :param Memory: 内存大小，單位 GB
        :type Memory: int
        :param Storage: 儲存大小，單位 GB
        :type Storage: int
        :param PeriodEndTime: 到期時間
        :type PeriodEndTime: str
        :param NodeCount: 節點數，2 爲一主一從， 3 爲一主二從
        :type NodeCount: int
        :param StorageUsage: 儲存使用率，單位爲 %
        :type StorageUsage: float
        :param MemoryUsage: 内存使用率，單位爲 %
        :type MemoryUsage: float
        :param ShardId: 數字分片Id（過時欄位，請勿依賴該值）
        :type ShardId: int
        """
        self.InstanceId = None
        self.ShardSerialId = None
        self.ShardInstanceId = None
        self.Status = None
        self.StatusDesc = None
        self.CreateTime = None
        self.VpcId = None
        self.SubnetId = None
        self.ProjectId = None
        self.Region = None
        self.Zone = None
        self.Memory = None
        self.Storage = None
        self.PeriodEndTime = None
        self.NodeCount = None
        self.StorageUsage = None
        self.MemoryUsage = None
        self.ShardId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ShardSerialId = params.get("ShardSerialId")
        self.ShardInstanceId = params.get("ShardInstanceId")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.CreateTime = params.get("CreateTime")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ProjectId = params.get("ProjectId")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.NodeCount = params.get("NodeCount")
        self.StorageUsage = params.get("StorageUsage")
        self.MemoryUsage = params.get("MemoryUsage")
        self.ShardId = params.get("ShardId")


class Database(AbstractModel):
    """資料庫訊息

    """

    def __init__(self):
        """
        :param DbName: 資料庫名稱
        :type DbName: str
        """
        self.DbName = None


    def _deserialize(self, params):
        self.DbName = params.get("DbName")


class DatabaseFunction(AbstractModel):
    """資料庫函數訊息

    """

    def __init__(self):
        """
        :param Func: 函數名稱
        :type Func: str
        """
        self.Func = None


    def _deserialize(self, params):
        self.Func = params.get("Func")


class DatabaseProcedure(AbstractModel):
    """資料庫儲存過程訊息

    """

    def __init__(self):
        """
        :param Proc: 儲存過程名稱
        :type Proc: str
        """
        self.Proc = None


    def _deserialize(self, params):
        self.Proc = params.get("Proc")


class DatabaseTable(AbstractModel):
    """資料庫表訊息

    """

    def __init__(self):
        """
        :param Table: 表名
        :type Table: str
        """
        self.Table = None


    def _deserialize(self, params):
        self.Table = params.get("Table")


class DatabaseView(AbstractModel):
    """資料庫視圖訊息

    """

    def __init__(self):
        """
        :param View: 視圖名稱
        :type View: str
        """
        self.View = None


    def _deserialize(self, params):
        self.View = params.get("View")


class Deal(AbstractModel):
    """訂單訊息

    """

    def __init__(self):
        """
        :param DealName: 訂單號
        :type DealName: str
        :param OwnerUin: 所屬賬號
        :type OwnerUin: str
        :param Count: 商品數量
        :type Count: int
        :param FlowId: 關聯的流程 Id，可用於查詢流程執行狀态
        :type FlowId: int
        :param InstanceIds: 只有創建實例的訂單會填充該欄位，表示該訂單創建的實例的 ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceIds: list of str
        :param PayMode: 付費模式，0後付費/1預付費
        :type PayMode: int
        """
        self.DealName = None
        self.OwnerUin = None
        self.Count = None
        self.FlowId = None
        self.InstanceIds = None
        self.PayMode = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.OwnerUin = params.get("OwnerUin")
        self.Count = params.get("Count")
        self.FlowId = params.get("FlowId")
        self.InstanceIds = params.get("InstanceIds")
        self.PayMode = params.get("PayMode")


class DeleteAccountRequest(AbstractModel):
    """DeleteAccount請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，形如：dcdbt-ow728lmc，可以通過 DescribeDCDBInstances 查詢實例詳情獲得。
        :type InstanceId: str
        :param UserName: 用戶名
        :type UserName: str
        :param Host: 用戶允許的訪問 host
        :type Host: str
        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")


class DeleteAccountResponse(AbstractModel):
    """DeleteAccount返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccountPrivilegesRequest(AbstractModel):
    """DescribeAccountPrivileges請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：dcdbt-ow7t8lmc。
        :type InstanceId: str
        :param UserName: 登入用戶名。
        :type UserName: str
        :param Host: 用戶允許的訪問 host，用戶名+host唯一确定一個賬號。
        :type Host: str
        :param DbName: 資料庫名。如果爲 \*，表示查詢全局權限（即 \*.\*），此時忽略 Type 和 Object 參數
        :type DbName: str
        :param Type: 類型,可以填入 table 、 view 、 proc 、 func 和 \*。當 DbName 爲具體資料庫名，Type爲 \* 時，表示查詢該資料庫權限（即db.\*），此時忽略 Object 參數
        :type Type: str
        :param Object: 具體的 Type 的名稱，比如 Type 爲 table 時就是具體的表名。DbName 和 Type 都爲具體名稱，則 Object 表示具體對象名，不能爲 \* 或者爲空
        :type Object: str
        :param ColName: 當 Type=table 時，ColName 爲 \* 表示查詢表的權限，如果爲具體欄位名，表示查詢對應欄位的權限
        :type ColName: str
        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.DbName = None
        self.Type = None
        self.Object = None
        self.ColName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.DbName = params.get("DbName")
        self.Type = params.get("Type")
        self.Object = params.get("Object")
        self.ColName = params.get("ColName")


class DescribeAccountPrivilegesResponse(AbstractModel):
    """DescribeAccountPrivileges返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例Id
        :type InstanceId: str
        :param Privileges: 權限清單。
        :type Privileges: list of str
        :param UserName: 資料庫賬號用戶名
        :type UserName: str
        :param Host: 資料庫賬號Host
        :type Host: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.Privileges = None
        self.UserName = None
        self.Host = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Privileges = params.get("Privileges")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，透傳入參。
        :type InstanceId: str
        :param Users: 實例用戶清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Users: list of DBAccount
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.Users = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Users") is not None:
            self.Users = []
            for item in params.get("Users"):
                obj = DBAccount()
                obj._deserialize(item)
                self.Users.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBLogFilesRequest(AbstractModel):
    """DescribeDBLogFiles請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：dcdbt-ow7t8lmc。
        :type InstanceId: str
        :param ShardId: 分片 ID，形如：shard-7noic7tv
        :type ShardId: str
        :param Type: 請求日志類型，取值只能爲1、2、3或者4。1-binlog，2-冷備，3-errlog，4-slowlog。
        :type Type: int
        """
        self.InstanceId = None
        self.ShardId = None
        self.Type = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ShardId = params.get("ShardId")
        self.Type = params.get("Type")


class DescribeDBLogFilesResponse(AbstractModel):
    """DescribeDBLogFiles返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param Type: 請求日志類型。1-binlog，2-冷備，3-errlog，4-slowlog。
        :type Type: int
        :param Total: 請求日志總數
        :type Total: int
        :param Files: 日志文件清單
        :type Files: list of LogFileInfo
        :param VpcPrefix: 如果是VPC網絡的實例，做用本前綴加上URI爲下載網址
        :type VpcPrefix: str
        :param NormalPrefix: 如果是普通網絡的實例，做用本前綴加上URI爲下載網址
        :type NormalPrefix: str
        :param ShardId: 分片 ID，形如：shard-7noic7tv
        :type ShardId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.Type = None
        self.Total = None
        self.Files = None
        self.VpcPrefix = None
        self.NormalPrefix = None
        self.ShardId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Type = params.get("Type")
        self.Total = params.get("Total")
        if params.get("Files") is not None:
            self.Files = []
            for item in params.get("Files"):
                obj = LogFileInfo()
                obj._deserialize(item)
                self.Files.append(obj)
        self.VpcPrefix = params.get("VpcPrefix")
        self.NormalPrefix = params.get("NormalPrefix")
        self.ShardId = params.get("ShardId")
        self.RequestId = params.get("RequestId")


class DescribeDBParametersRequest(AbstractModel):
    """DescribeDBParameters請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：dcdbt-ow7t8lmc。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeDBParametersResponse(AbstractModel):
    """DescribeDBParameters返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：dcdbt-ow7t8lmc。
        :type InstanceId: str
        :param Params: 請求DB的當前參數值
        :type Params: list of ParamDesc
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.Params = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Params") is not None:
            self.Params = []
            for item in params.get("Params"):
                obj = ParamDesc()
                obj._deserialize(item)
                self.Params.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBSyncModeRequest(AbstractModel):
    """DescribeDBSyncMode請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 待修改同步模式的實例ID。形如：dcdbt-ow728lmc。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeDBSyncModeResponse(AbstractModel):
    """DescribeDBSyncMode返回參數結構體

    """

    def __init__(self):
        """
        :param SyncMode: 同步模式：0 異步，1 強同步， 2 強同步可退化
        :type SyncMode: int
        :param IsModifying: 是否有修改流程在執行中：1 是， 0 否。
        :type IsModifying: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SyncMode = None
        self.IsModifying = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SyncMode = params.get("SyncMode")
        self.IsModifying = params.get("IsModifying")
        self.RequestId = params.get("RequestId")


class DescribeDCDBInstancesRequest(AbstractModel):
    """DescribeDCDBInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 按照一個或者多個實例 ID 查詢。實例 ID 形如：dcdbt-2t4cf98d
        :type InstanceIds: list of str
        :param SearchName: 搜索的欄位名，當前支援的值有：instancename、vip、all。傳 instancename 表示按實例名進行搜索；傳 vip 表示按内網IP進行搜索；傳 all 将會按實例ID、實例名和内網IP進行搜索。
        :type SearchName: str
        :param SearchKey: 搜索的關鍵字，支援模糊搜索。多個關鍵字使用換行符（'\n'）分割。
        :type SearchKey: str
        :param ProjectIds: 按項目 ID 查詢
        :type ProjectIds: list of int
        :param IsFilterVpc: 是否根據 VPC 網絡來搜索
        :type IsFilterVpc: bool
        :param VpcId: 私有網絡 ID， IsFilterVpc 爲 1 時有效
        :type VpcId: str
        :param SubnetId: 私有網絡的子網 ID， IsFilterVpc 爲 1 時有效
        :type SubnetId: str
        :param OrderBy: 排序欄位， projectId， createtime， instancename 三者之一
        :type OrderBy: str
        :param OrderByType: 排序類型， desc 或者 asc
        :type OrderByType: str
        :param Offset: 偏移量，預設爲 0
        :type Offset: int
        :param Limit: 返回數量，預設爲 10，最大值爲 100。
        :type Limit: int
        :param ExclusterType: 1非獨享集群，2獨享集群， 0全部
        :type ExclusterType: int
        :param IsFilterExcluster: 標識是否使用ExclusterType欄位, false不使用，true使用
        :type IsFilterExcluster: bool
        """
        self.InstanceIds = None
        self.SearchName = None
        self.SearchKey = None
        self.ProjectIds = None
        self.IsFilterVpc = None
        self.VpcId = None
        self.SubnetId = None
        self.OrderBy = None
        self.OrderByType = None
        self.Offset = None
        self.Limit = None
        self.ExclusterType = None
        self.IsFilterExcluster = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.SearchName = params.get("SearchName")
        self.SearchKey = params.get("SearchKey")
        self.ProjectIds = params.get("ProjectIds")
        self.IsFilterVpc = params.get("IsFilterVpc")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ExclusterType = params.get("ExclusterType")
        self.IsFilterExcluster = params.get("IsFilterExcluster")


class DescribeDCDBInstancesResponse(AbstractModel):
    """DescribeDCDBInstances返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的實例數量
        :type TotalCount: int
        :param Instances: 實例詳細訊息清單
        :type Instances: list of DCDBInstanceInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Instances = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = DCDBInstanceInfo()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDCDBPriceRequest(AbstractModel):
    """DescribeDCDBPrice請求參數結構體

    """

    def __init__(self):
        """
        :param Zone: 欲新購實例的可用區ID。
        :type Zone: str
        :param Count: 欲購買實例的數量，目前只支援購買1個實例
        :type Count: int
        :param Period: 欲購買的時長，單位：月。
        :type Period: int
        :param ShardNodeCount: 單個分片節點個數大小，可以通過 DescribeShardSpec
 查詢實例規格獲得。
        :type ShardNodeCount: int
        :param ShardMemory: 分片内存大小，單位：GB，可以通過 DescribeShardSpec
 查詢實例規格獲得。
        :type ShardMemory: int
        :param ShardStorage: 分片儲存空間大小，單位：GB，可以通過 DescribeShardSpec
 查詢實例規格獲得。
        :type ShardStorage: int
        :param ShardCount: 實例分片個數，可選範圍2-8，可以通過升級實例進行新增分片到最多64個分片。
        :type ShardCount: int
        """
        self.Zone = None
        self.Count = None
        self.Period = None
        self.ShardNodeCount = None
        self.ShardMemory = None
        self.ShardStorage = None
        self.ShardCount = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.Count = params.get("Count")
        self.Period = params.get("Period")
        self.ShardNodeCount = params.get("ShardNodeCount")
        self.ShardMemory = params.get("ShardMemory")
        self.ShardStorage = params.get("ShardStorage")
        self.ShardCount = params.get("ShardCount")


class DescribeDCDBPriceResponse(AbstractModel):
    """DescribeDCDBPrice返回參數結構體

    """

    def __init__(self):
        """
        :param OriginalPrice: 原價，單位：分
        :type OriginalPrice: int
        :param Price: 實際價格，單位：分。受折扣等影響，可能和原價不同。
        :type Price: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.OriginalPrice = None
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.Price = params.get("Price")
        self.RequestId = params.get("RequestId")


class DescribeDCDBRenewalPriceRequest(AbstractModel):
    """DescribeDCDBRenewalPrice請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 待續約的實例ID。形如：dcdbt-ow728lmc，可以通過 DescribeDCDBInstances 查詢實例詳情獲得。
        :type InstanceId: str
        :param Period: 續約時長，單位：月。不傳則預設爲1個月。
        :type Period: int
        """
        self.InstanceId = None
        self.Period = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Period = params.get("Period")


class DescribeDCDBRenewalPriceResponse(AbstractModel):
    """DescribeDCDBRenewalPrice返回參數結構體

    """

    def __init__(self):
        """
        :param OriginalPrice: 原價，單位：分
        :type OriginalPrice: int
        :param Price: 實際價格，單位：分。受折扣等影響，可能和原價不同。
        :type Price: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.OriginalPrice = None
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.Price = params.get("Price")
        self.RequestId = params.get("RequestId")


class DescribeDCDBSaleInfoRequest(AbstractModel):
    """DescribeDCDBSaleInfo請求參數結構體

    """


class DescribeDCDBSaleInfoResponse(AbstractModel):
    """DescribeDCDBSaleInfo返回參數結構體

    """

    def __init__(self):
        """
        :param RegionList: 可售賣地域訊息清單
        :type RegionList: list of RegionInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RegionList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionList") is not None:
            self.RegionList = []
            for item in params.get("RegionList"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.RegionList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDCDBShardsRequest(AbstractModel):
    """DescribeDCDBShards請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param ShardInstanceIds: 分片Id清單。
        :type ShardInstanceIds: list of str
        :param Offset: 偏移量，預設爲 0
        :type Offset: int
        :param Limit: 返回數量，預設爲 20，最大值爲 100。
        :type Limit: int
        :param OrderBy: 排序欄位， 目前僅支援 createtime
        :type OrderBy: str
        :param OrderByType: 排序類型， desc 或者 asc
        :type OrderByType: str
        """
        self.InstanceId = None
        self.ShardInstanceIds = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ShardInstanceIds = params.get("ShardInstanceIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")


class DescribeDCDBShardsResponse(AbstractModel):
    """DescribeDCDBShards返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的分片數量
        :type TotalCount: int
        :param Shards: 分片訊息清單
        :type Shards: list of DCDBShardInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Shards = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Shards") is not None:
            self.Shards = []
            for item in params.get("Shards"):
                obj = DCDBShardInfo()
                obj._deserialize(item)
                self.Shards.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDCDBUpgradePriceRequest(AbstractModel):
    """DescribeDCDBUpgradePrice請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 待升級的實例ID。形如：dcdbt-ow728lmc，可以通過 DescribeDCDBInstances 查詢實例詳情獲得。
        :type InstanceId: str
        :param UpgradeType: 升級類型，取值範圍: 
<li> ADD: 新增分片 </li> 
 <li> EXPAND: 升級實例中的已有分片 </li> 
 <li> SPLIT: 将已有分片中的數據切分到新增分片上</li>
        :type UpgradeType: str
        :param AddShardConfig: 新增分片配置，當UpgradeType爲ADD時生效。
        :type AddShardConfig: :class:`taifucloudcloud.dcdb.v20180411.models.AddShardConfig`
        :param ExpandShardConfig: 擴容分片配置，當UpgradeType爲EXPAND時生效。
        :type ExpandShardConfig: :class:`taifucloudcloud.dcdb.v20180411.models.ExpandShardConfig`
        :param SplitShardConfig: 切分分片配置，當UpgradeType爲SPLIT時生效。
        :type SplitShardConfig: :class:`taifucloudcloud.dcdb.v20180411.models.SplitShardConfig`
        """
        self.InstanceId = None
        self.UpgradeType = None
        self.AddShardConfig = None
        self.ExpandShardConfig = None
        self.SplitShardConfig = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UpgradeType = params.get("UpgradeType")
        if params.get("AddShardConfig") is not None:
            self.AddShardConfig = AddShardConfig()
            self.AddShardConfig._deserialize(params.get("AddShardConfig"))
        if params.get("ExpandShardConfig") is not None:
            self.ExpandShardConfig = ExpandShardConfig()
            self.ExpandShardConfig._deserialize(params.get("ExpandShardConfig"))
        if params.get("SplitShardConfig") is not None:
            self.SplitShardConfig = SplitShardConfig()
            self.SplitShardConfig._deserialize(params.get("SplitShardConfig"))


class DescribeDCDBUpgradePriceResponse(AbstractModel):
    """DescribeDCDBUpgradePrice返回參數結構體

    """

    def __init__(self):
        """
        :param OriginalPrice: 原價，單位：分
        :type OriginalPrice: int
        :param Price: 實際價格，單位：分。受折扣等影響，可能和原價不同。
        :type Price: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.OriginalPrice = None
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.Price = params.get("Price")
        self.RequestId = params.get("RequestId")


class DescribeDatabaseObjectsRequest(AbstractModel):
    """DescribeDatabaseObjects請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：dcdbt-ow7t8lmc。
        :type InstanceId: str
        :param DbName: 資料庫名稱，通過 DescribeDatabases 介面獲取。
        :type DbName: str
        """
        self.InstanceId = None
        self.DbName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DbName = params.get("DbName")


class DescribeDatabaseObjectsResponse(AbstractModel):
    """DescribeDatabaseObjects返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 透傳入參。
        :type InstanceId: str
        :param DbName: 資料庫名稱。
        :type DbName: str
        :param Tables: 表清單。
        :type Tables: list of DatabaseTable
        :param Views: 視圖清單。
        :type Views: list of DatabaseView
        :param Procs: 儲存過程清單。
        :type Procs: list of DatabaseProcedure
        :param Funcs: 函數清單。
        :type Funcs: list of DatabaseFunction
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.DbName = None
        self.Tables = None
        self.Views = None
        self.Procs = None
        self.Funcs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DbName = params.get("DbName")
        if params.get("Tables") is not None:
            self.Tables = []
            for item in params.get("Tables"):
                obj = DatabaseTable()
                obj._deserialize(item)
                self.Tables.append(obj)
        if params.get("Views") is not None:
            self.Views = []
            for item in params.get("Views"):
                obj = DatabaseView()
                obj._deserialize(item)
                self.Views.append(obj)
        if params.get("Procs") is not None:
            self.Procs = []
            for item in params.get("Procs"):
                obj = DatabaseProcedure()
                obj._deserialize(item)
                self.Procs.append(obj)
        if params.get("Funcs") is not None:
            self.Funcs = []
            for item in params.get("Funcs"):
                obj = DatabaseFunction()
                obj._deserialize(item)
                self.Funcs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDatabaseTableRequest(AbstractModel):
    """DescribeDatabaseTable請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：dcdbt-ow7t8lmc。
        :type InstanceId: str
        :param DbName: 資料庫名稱，通過 DescribeDatabases 介面獲取。
        :type DbName: str
        :param Table: 表名稱，通過 DescribeDatabaseObjects 介面獲取。
        :type Table: str
        """
        self.InstanceId = None
        self.DbName = None
        self.Table = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DbName = params.get("DbName")
        self.Table = params.get("Table")


class DescribeDatabaseTableResponse(AbstractModel):
    """DescribeDatabaseTable返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例名稱。
        :type InstanceId: str
        :param DbName: 資料庫名稱。
        :type DbName: str
        :param Table: 表名稱。
        :type Table: str
        :param Cols: 列訊息。
        :type Cols: list of TableColumn
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.DbName = None
        self.Table = None
        self.Cols = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DbName = params.get("DbName")
        self.Table = params.get("Table")
        if params.get("Cols") is not None:
            self.Cols = []
            for item in params.get("Cols"):
                obj = TableColumn()
                obj._deserialize(item)
                self.Cols.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    """DescribeDatabases請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：dcdbt-ow7t8lmc。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeDatabasesResponse(AbstractModel):
    """DescribeDatabases返回參數結構體

    """

    def __init__(self):
        """
        :param Databases: 該實例上的資料庫清單。
        :type Databases: list of Database
        :param InstanceId: 透傳入參。
        :type InstanceId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Databases = None
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Databases") is not None:
            self.Databases = []
            for item in params.get("Databases"):
                obj = Database()
                obj._deserialize(item)
                self.Databases.append(obj)
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class DescribeOrdersRequest(AbstractModel):
    """DescribeOrders請求參數結構體

    """

    def __init__(self):
        """
        :param DealNames: 待查詢的長訂單號清單，創建實例、續約實例、擴容實例介面返回。
        :type DealNames: list of str
        """
        self.DealNames = None


    def _deserialize(self, params):
        self.DealNames = params.get("DealNames")


class DescribeOrdersResponse(AbstractModel):
    """DescribeOrders返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 返回的訂單數量。
        :type TotalCount: list of int
        :param Deals: 訂單訊息清單。
        :type Deals: list of Deal
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Deals = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Deals") is not None:
            self.Deals = []
            for item in params.get("Deals"):
                obj = Deal()
                obj._deserialize(item)
                self.Deals.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeShardSpecRequest(AbstractModel):
    """DescribeShardSpec請求參數結構體

    """


class DescribeShardSpecResponse(AbstractModel):
    """DescribeShardSpec返回參數結構體

    """

    def __init__(self):
        """
        :param SpecConfig: 按機型分類的可售賣規格清單
        :type SpecConfig: list of SpecConfig
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SpecConfig = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SpecConfig") is not None:
            self.SpecConfig = []
            for item in params.get("SpecConfig"):
                obj = SpecConfig()
                obj._deserialize(item)
                self.SpecConfig.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSqlLogsRequest(AbstractModel):
    """DescribeSqlLogs請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：dcdbt-ow728lmc，可以通過 DescribeDCDBInstances 查詢實例詳情獲得。
        :type InstanceId: str
        :param Offset: SQL日志偏移。
        :type Offset: int
        :param Limit: 拉取數量（0-10000，爲0時拉取總數訊息）。
        :type Limit: int
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeSqlLogsResponse(AbstractModel):
    """DescribeSqlLogs返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 當前訊息隊列中的sql日志條目數。
        :type TotalCount: int
        :param StartOffset: 訊息隊列中的sql日志起始偏移。
        :type StartOffset: int
        :param EndOffset: 訊息隊列中的sql日志結束偏移。
        :type EndOffset: int
        :param Offset: 返回的第一條sql日志的偏移。
        :type Offset: int
        :param Count: 返回的sql日志數量。
        :type Count: int
        :param SqlItems: Sql日志清單。
        :type SqlItems: list of SqlLogItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.StartOffset = None
        self.EndOffset = None
        self.Offset = None
        self.Count = None
        self.SqlItems = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.StartOffset = params.get("StartOffset")
        self.EndOffset = params.get("EndOffset")
        self.Offset = params.get("Offset")
        self.Count = params.get("Count")
        if params.get("SqlItems") is not None:
            self.SqlItems = []
            for item in params.get("SqlItems"):
                obj = SqlLogItem()
                obj._deserialize(item)
                self.SqlItems.append(obj)
        self.RequestId = params.get("RequestId")


class ExpandShardConfig(AbstractModel):
    """升級實例 -- 擴容分片類型

    """

    def __init__(self):
        """
        :param ShardInstanceIds: 分片ID數組
        :type ShardInstanceIds: list of str
        :param ShardMemory: 分片内存大小，單位 GB
        :type ShardMemory: int
        :param ShardStorage: 分片儲存大小，單位 GB
        :type ShardStorage: int
        """
        self.ShardInstanceIds = None
        self.ShardMemory = None
        self.ShardStorage = None


    def _deserialize(self, params):
        self.ShardInstanceIds = params.get("ShardInstanceIds")
        self.ShardMemory = params.get("ShardMemory")
        self.ShardStorage = params.get("ShardStorage")


class GrantAccountPrivilegesRequest(AbstractModel):
    """GrantAccountPrivileges請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param UserName: 登入用戶名。
        :type UserName: str
        :param Host: 用戶允許的訪問 host，用戶名+host唯一确定一個賬號。
        :type Host: str
        :param DbName: 資料庫名。如果爲 \*，表示查詢全局權限（即 \*.\*），此時忽略 Type 和 Object 參數
        :type DbName: str
        :param Privileges: 全局權限： SELECT，INSERT，UPDATE，DELETE，CREATE，DROP，REFERENCES，INDEX，ALTER，CREATE TEMPORARY TABLES，LOCK TABLES，EXECUTE，CREATE VIEW，SHOW VIEW，CREATE ROUTINE，ALTER ROUTINE，EVENT，TRIGGER，SHOW DATABASES 
庫權限： SELECT，INSERT，UPDATE，DELETE，CREATE，DROP，REFERENCES，INDEX，ALTER，CREATE TEMPORARY TABLES，LOCK TABLES，EXECUTE，CREATE VIEW，SHOW VIEW，CREATE ROUTINE，ALTER ROUTINE，EVENT，TRIGGER 
表/視圖權限： SELECT，INSERT，UPDATE，DELETE，CREATE，DROP，REFERENCES，INDEX，ALTER，CREATE VIEW，SHOW VIEW，TRIGGER 
儲存過程/函數權限： ALTER ROUTINE，EXECUTE 
欄位權限： INSERT，REFERENCES，SELECT，UPDATE
        :type Privileges: list of str
        :param Type: 類型,可以填入 table 、 view 、 proc 、 func 和 \*。當 DbName 爲具體資料庫名，Type爲 \* 時，表示設置該資料庫權限（即db.\*），此時忽略 Object 參數
        :type Type: str
        :param Object: 具體的 Type 的名稱，比如 Type 爲 table 時就是具體的表名。DbName 和 Type 都爲具體名稱，則 Object 表示具體對象名，不能爲 \* 或者爲空
        :type Object: str
        :param ColName: 當 Type=table 時，ColName 爲 \* 表示對表授權，如果爲具體欄位名，表示對欄位授權
        :type ColName: str
        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.DbName = None
        self.Privileges = None
        self.Type = None
        self.Object = None
        self.ColName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.DbName = params.get("DbName")
        self.Privileges = params.get("Privileges")
        self.Type = params.get("Type")
        self.Object = params.get("Object")
        self.ColName = params.get("ColName")


class GrantAccountPrivilegesResponse(AbstractModel):
    """GrantAccountPrivileges返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class InitDCDBInstancesRequest(AbstractModel):
    """InitDCDBInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 待初始化的實例Id清單，形如：dcdbt-ow728lmc，可以通過 DescribeDCDBInstances 查詢實例詳情獲得。
        :type InstanceIds: list of str
        :param Params: 參數清單。本介面的可選值爲：character_set_server（字元集，必傳），lower_case_table_names（表名大小寫敏感，必傳，0 - 敏感；1-不敏感），innodb_page_size（innodb數據頁，預設16K），sync_mode（同步模式：0 - 異步； 1 - 強同步；2 - 強同步可退化。預設爲強同步）。
        :type Params: list of DBParamValue
        """
        self.InstanceIds = None
        self.Params = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("Params") is not None:
            self.Params = []
            for item in params.get("Params"):
                obj = DBParamValue()
                obj._deserialize(item)
                self.Params.append(obj)


class InitDCDBInstancesResponse(AbstractModel):
    """InitDCDBInstances返回參數結構體

    """

    def __init__(self):
        """
        :param FlowIds: 異步任務Id，可通過 DescribeFlow 查詢任務狀态。
        :type FlowIds: list of int non-negative
        :param InstanceIds: 透傳入參。
        :type InstanceIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FlowIds = None
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowIds = params.get("FlowIds")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class LogFileInfo(AbstractModel):
    """拉取的日志訊息

    """

    def __init__(self):
        """
        :param Mtime: Log最後修改時間
        :type Mtime: int
        :param Length: 文件長度
        :type Length: int
        :param Uri: 下載Log時用到的統一資源標識符
        :type Uri: str
        :param FileName: 文件名
        :type FileName: str
        """
        self.Mtime = None
        self.Length = None
        self.Uri = None
        self.FileName = None


    def _deserialize(self, params):
        self.Mtime = params.get("Mtime")
        self.Length = params.get("Length")
        self.Uri = params.get("Uri")
        self.FileName = params.get("FileName")


class ModifyAccountDescriptionRequest(AbstractModel):
    """ModifyAccountDescription請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param UserName: 登入用戶名。
        :type UserName: str
        :param Host: 用戶允許的訪問 host，用戶名+host唯一确定一個賬號。
        :type Host: str
        :param Description: 新的賬號備注，長度 0~256。
        :type Description: str
        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.Description = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.Description = params.get("Description")


class ModifyAccountDescriptionResponse(AbstractModel):
    """ModifyAccountDescription返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstancesProjectRequest(AbstractModel):
    """ModifyDBInstancesProject請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 待修改的實例ID清單。實例 ID 形如：dcdbt-ow728lmc。
        :type InstanceIds: list of str
        :param ProjectId: 要分配的項目 ID，可以通過 DescribeProjects 查詢項目清單介面獲取。
        :type ProjectId: int
        """
        self.InstanceIds = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.ProjectId = params.get("ProjectId")


class ModifyDBInstancesProjectResponse(AbstractModel):
    """ModifyDBInstancesProject返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBParametersRequest(AbstractModel):
    """ModifyDBParameters請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param Params: 參數清單，每一個元素是Param和Value的組合
        :type Params: list of DBParamValue
        """
        self.InstanceId = None
        self.Params = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Params") is not None:
            self.Params = []
            for item in params.get("Params"):
                obj = DBParamValue()
                obj._deserialize(item)
                self.Params.append(obj)


class ModifyDBParametersResponse(AbstractModel):
    """ModifyDBParameters返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param Result: 各參數修改結果
        :type Result: list of ParamModifyResult
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = ParamModifyResult()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyDBSyncModeRequest(AbstractModel):
    """ModifyDBSyncMode請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 待修改同步模式的實例ID。形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param SyncMode: 同步模式：0 異步，1 強同步， 2 強同步可退化
        :type SyncMode: int
        """
        self.InstanceId = None
        self.SyncMode = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SyncMode = params.get("SyncMode")


class ModifyDBSyncModeResponse(AbstractModel):
    """ModifyDBSyncMode返回參數結構體

    """

    def __init__(self):
        """
        :param FlowId: 異步任務Id，可通過 DescribeFlow 查詢任務狀态。
        :type FlowId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class OpenDBExtranetAccessRequest(AbstractModel):
    """OpenDBExtranetAccess請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 待開放外網訪問的實例ID。形如：dcdbt-ow728lmc。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class OpenDBExtranetAccessResponse(AbstractModel):
    """OpenDBExtranetAccess返回參數結構體

    """

    def __init__(self):
        """
        :param FlowId: 異步任務Id，可通過 DescribeFlow 查詢任務狀态。
        :type FlowId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ParamConstraint(AbstractModel):
    """參數約束

    """

    def __init__(self):
        """
        :param Type: 約束類型,如列舉enum，區間section
        :type Type: str
        :param Enum: 約束類型爲enum時的可選值清單
        :type Enum: str
        :param Range: 約束類型爲section時的範圍
注意：此欄位可能返回 null，表示取不到有效值。
        :type Range: :class:`taifucloudcloud.dcdb.v20180411.models.ConstraintRange`
        :param String: 約束類型爲string時的可選值清單
        :type String: str
        """
        self.Type = None
        self.Enum = None
        self.Range = None
        self.String = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Enum = params.get("Enum")
        if params.get("Range") is not None:
            self.Range = ConstraintRange()
            self.Range._deserialize(params.get("Range"))
        self.String = params.get("String")


class ParamDesc(AbstractModel):
    """DB參數描述

    """

    def __init__(self):
        """
        :param Param: 參數名字
        :type Param: str
        :param Value: 當前參數值
        :type Value: str
        :param SetValue: 設置過的值，參數生效後，該值和value一樣。未設置過就不返回該欄位。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SetValue: str
        :param Default: 系統預設值
        :type Default: str
        :param Constraint: 參數限制
        :type Constraint: :class:`taifucloudcloud.dcdb.v20180411.models.ParamConstraint`
        """
        self.Param = None
        self.Value = None
        self.SetValue = None
        self.Default = None
        self.Constraint = None


    def _deserialize(self, params):
        self.Param = params.get("Param")
        self.Value = params.get("Value")
        self.SetValue = params.get("SetValue")
        self.Default = params.get("Default")
        if params.get("Constraint") is not None:
            self.Constraint = ParamConstraint()
            self.Constraint._deserialize(params.get("Constraint"))


class ParamModifyResult(AbstractModel):
    """修改參數結果

    """

    def __init__(self):
        """
        :param Param: 修改參數名字
        :type Param: str
        :param Code: 參數修改結果。0表示修改成功；-1表示修改失敗；-2表示該參數值非法
        :type Code: int
        """
        self.Param = None
        self.Code = None


    def _deserialize(self, params):
        self.Param = params.get("Param")
        self.Code = params.get("Code")


class RegionInfo(AbstractModel):
    """售賣可用區訊息

    """

    def __init__(self):
        """
        :param Region: 地域英文ID
        :type Region: str
        :param RegionId: 地域數字ID
        :type RegionId: int
        :param RegionName: 地域中文名
        :type RegionName: str
        :param ZoneList: 可用區清單
        :type ZoneList: list of ZonesInfo
        :param AvailableChoice: 可選擇的主可用區和從可用區
        :type AvailableChoice: list of ShardZoneChooseInfo
        """
        self.Region = None
        self.RegionId = None
        self.RegionName = None
        self.ZoneList = None
        self.AvailableChoice = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        if params.get("ZoneList") is not None:
            self.ZoneList = []
            for item in params.get("ZoneList"):
                obj = ZonesInfo()
                obj._deserialize(item)
                self.ZoneList.append(obj)
        if params.get("AvailableChoice") is not None:
            self.AvailableChoice = []
            for item in params.get("AvailableChoice"):
                obj = ShardZoneChooseInfo()
                obj._deserialize(item)
                self.AvailableChoice.append(obj)


class RenewDCDBInstanceRequest(AbstractModel):
    """RenewDCDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 待續約的實例ID。形如：dcdbt-ow728lmc，可以通過 DescribeDCDBInstances 查詢實例詳情獲得。
        :type InstanceId: str
        :param Period: 續約時長，單位：月。
        :type Period: int
        :param AutoVoucher: 是否自動使用 進行支付，預設不使用。
        :type AutoVoucher: bool
        :param VoucherIds:  ID清單，目前僅支援指定一張 。
        :type VoucherIds: list of str
        """
        self.InstanceId = None
        self.Period = None
        self.AutoVoucher = None
        self.VoucherIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Period = params.get("Period")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")


class RenewDCDBInstanceResponse(AbstractModel):
    """RenewDCDBInstance返回參數結構體

    """

    def __init__(self):
        """
        :param DealName: 長訂單號。可以據此調用 DescribeOrders
 查詢訂單詳細訊息，或在支付失敗時調用用戶賬號相關介面進行支付。
        :type DealName: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class ResetAccountPasswordRequest(AbstractModel):
    """ResetAccountPassword請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：dcdbt-ow728lmc。
        :type InstanceId: str
        :param UserName: 登入用戶名。
        :type UserName: str
        :param Host: 用戶允許的訪問 host，用戶名+host唯一确定一個賬號。
        :type Host: str
        :param Password: 新密碼，由字母、數字或常見符號組成，不能包含分號、單引號和雙引號，長度爲6~32位。
        :type Password: str
        """
        self.InstanceId = None
        self.UserName = None
        self.Host = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Host = params.get("Host")
        self.Password = params.get("Password")


class ResetAccountPasswordResponse(AbstractModel):
    """ResetAccountPassword返回參數結構體

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
    """分片訊息

    """

    def __init__(self):
        """
        :param ShardInstanceId: 分片ID
        :type ShardInstanceId: str
        :param ShardSerialId: 分片Set ID
        :type ShardSerialId: str
        :param Status: 狀态：0 創建中，1 流程處理中， 2 運作中，3 分片未初始化，-2 分片已删除
        :type Status: int
        :param Createtime: 創建時間
        :type Createtime: str
        :param Memory: 内存大小，單位 GB
        :type Memory: int
        :param Storage: 儲存大小，單位 GB
        :type Storage: int
        :param ShardId: 分片數字ID
        :type ShardId: int
        :param NodeCount: 節點數，2 爲一主一從， 3 爲一主二從
        :type NodeCount: int
        :param Pid: 産品類型 Id（過時欄位，請勿依賴該值）
        :type Pid: int
        """
        self.ShardInstanceId = None
        self.ShardSerialId = None
        self.Status = None
        self.Createtime = None
        self.Memory = None
        self.Storage = None
        self.ShardId = None
        self.NodeCount = None
        self.Pid = None


    def _deserialize(self, params):
        self.ShardInstanceId = params.get("ShardInstanceId")
        self.ShardSerialId = params.get("ShardSerialId")
        self.Status = params.get("Status")
        self.Createtime = params.get("Createtime")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.ShardId = params.get("ShardId")
        self.NodeCount = params.get("NodeCount")
        self.Pid = params.get("Pid")


class ShardZoneChooseInfo(AbstractModel):
    """分片節點可用區選擇

    """

    def __init__(self):
        """
        :param MasterZone: 主可用區
        :type MasterZone: :class:`taifucloudcloud.dcdb.v20180411.models.ZonesInfo`
        :param SlaveZones: 可選的從可用區
        :type SlaveZones: list of ZonesInfo
        """
        self.MasterZone = None
        self.SlaveZones = None


    def _deserialize(self, params):
        if params.get("MasterZone") is not None:
            self.MasterZone = ZonesInfo()
            self.MasterZone._deserialize(params.get("MasterZone"))
        if params.get("SlaveZones") is not None:
            self.SlaveZones = []
            for item in params.get("SlaveZones"):
                obj = ZonesInfo()
                obj._deserialize(item)
                self.SlaveZones.append(obj)


class SpecConfig(AbstractModel):
    """按機型分類的規格配置

    """

    def __init__(self):
        """
        :param Machine: 規格機型
        :type Machine: str
        :param SpecConfigInfos: 規格清單
        :type SpecConfigInfos: list of SpecConfigInfo
        """
        self.Machine = None
        self.SpecConfigInfos = None


    def _deserialize(self, params):
        self.Machine = params.get("Machine")
        if params.get("SpecConfigInfos") is not None:
            self.SpecConfigInfos = []
            for item in params.get("SpecConfigInfos"):
                obj = SpecConfigInfo()
                obj._deserialize(item)
                self.SpecConfigInfos.append(obj)


class SpecConfigInfo(AbstractModel):
    """實例可售賣規格詳細訊息，創建實例和擴容實例時 NodeCount、Memory 确定售賣規格，硬碟大小可用區間爲[MinStorage,MaxStorage]

    """

    def __init__(self):
        """
        :param NodeCount: 節點個數，2 表示一主一從，3 表示一主二從
        :type NodeCount: int
        :param Memory: 内存大小，單位 GB
        :type Memory: int
        :param MinStorage: 數據盤規格最小值，單位 GB
        :type MinStorage: int
        :param MaxStorage: 數據盤規格最大值，單位 GB
        :type MaxStorage: int
        :param SuitInfo: 推薦的使用場景
        :type SuitInfo: str
        :param Pid: 産品類型 Id
        :type Pid: int
        :param Qps: 最大 Qps 值
        :type Qps: int
        """
        self.NodeCount = None
        self.Memory = None
        self.MinStorage = None
        self.MaxStorage = None
        self.SuitInfo = None
        self.Pid = None
        self.Qps = None


    def _deserialize(self, params):
        self.NodeCount = params.get("NodeCount")
        self.Memory = params.get("Memory")
        self.MinStorage = params.get("MinStorage")
        self.MaxStorage = params.get("MaxStorage")
        self.SuitInfo = params.get("SuitInfo")
        self.Pid = params.get("Pid")
        self.Qps = params.get("Qps")


class SplitShardConfig(AbstractModel):
    """升級實例 -- 切分分片類型

    """

    def __init__(self):
        """
        :param ShardInstanceIds: 分片ID數組
        :type ShardInstanceIds: list of str
        :param SplitRate: 數據切分比例
        :type SplitRate: int
        :param ShardMemory: 分片内存大小，單位 GB
        :type ShardMemory: int
        :param ShardStorage: 分片儲存大小，單位 GB
        :type ShardStorage: int
        """
        self.ShardInstanceIds = None
        self.SplitRate = None
        self.ShardMemory = None
        self.ShardStorage = None


    def _deserialize(self, params):
        self.ShardInstanceIds = params.get("ShardInstanceIds")
        self.SplitRate = params.get("SplitRate")
        self.ShardMemory = params.get("ShardMemory")
        self.ShardStorage = params.get("ShardStorage")


class SqlLogItem(AbstractModel):
    """描述一條sql日志的詳細訊息。

    """

    def __init__(self):
        """
        :param Offset: 本條日志在訊息隊列中的偏移量。
        :type Offset: int
        :param User: 執行本條sql的用戶。
        :type User: str
        :param Client: 執行本條sql的用戶端IP+端口。
        :type Client: str
        :param DbName: 資料庫名稱。
        :type DbName: str
        :param Sql: 執行的sql語句。
        :type Sql: str
        :param SelectRowNum: 返回的數據行數。
        :type SelectRowNum: int
        :param AffectRowNum: 影響行數。
        :type AffectRowNum: int
        :param Timestamp: Sql執行時間戳。
        :type Timestamp: int
        :param TimeCostMs: Sql耗時，單位爲毫秒。
        :type TimeCostMs: int
        :param ResultCode: Sql返回碼，0爲成功。
        :type ResultCode: int
        """
        self.Offset = None
        self.User = None
        self.Client = None
        self.DbName = None
        self.Sql = None
        self.SelectRowNum = None
        self.AffectRowNum = None
        self.Timestamp = None
        self.TimeCostMs = None
        self.ResultCode = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.User = params.get("User")
        self.Client = params.get("Client")
        self.DbName = params.get("DbName")
        self.Sql = params.get("Sql")
        self.SelectRowNum = params.get("SelectRowNum")
        self.AffectRowNum = params.get("AffectRowNum")
        self.Timestamp = params.get("Timestamp")
        self.TimeCostMs = params.get("TimeCostMs")
        self.ResultCode = params.get("ResultCode")


class TableColumn(AbstractModel):
    """資料庫列訊息

    """

    def __init__(self):
        """
        :param Col: 列名稱
        :type Col: str
        :param Type: 列類型
        :type Type: str
        """
        self.Col = None
        self.Type = None


    def _deserialize(self, params):
        self.Col = params.get("Col")
        self.Type = params.get("Type")


class UpgradeDCDBInstanceRequest(AbstractModel):
    """UpgradeDCDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 待升級的實例ID。形如：dcdbt-ow728lmc，可以通過 DescribeDCDBInstances 查詢實例詳情獲得。
        :type InstanceId: str
        :param UpgradeType: 升級類型，取值範圍: 
<li> ADD: 新增分片 </li> 
 <li> EXPAND: 升級實例中的已有分片 </li> 
 <li> SPLIT: 将已有分片中的數據切分到新增分片上</li>
        :type UpgradeType: str
        :param AddShardConfig: 新增分片配置，當UpgradeType爲ADD時生效。
        :type AddShardConfig: :class:`taifucloudcloud.dcdb.v20180411.models.AddShardConfig`
        :param ExpandShardConfig: 擴容分片配置，當UpgradeType爲EXPAND時生效。
        :type ExpandShardConfig: :class:`taifucloudcloud.dcdb.v20180411.models.ExpandShardConfig`
        :param SplitShardConfig: 切分分片配置，當UpgradeType爲SPLIT時生效。
        :type SplitShardConfig: :class:`taifucloudcloud.dcdb.v20180411.models.SplitShardConfig`
        :param AutoVoucher: 是否自動使用 進行支付，預設不使用。
        :type AutoVoucher: bool
        :param VoucherIds:  ID清單，目前僅支援指定一張 。
        :type VoucherIds: list of str
        """
        self.InstanceId = None
        self.UpgradeType = None
        self.AddShardConfig = None
        self.ExpandShardConfig = None
        self.SplitShardConfig = None
        self.AutoVoucher = None
        self.VoucherIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UpgradeType = params.get("UpgradeType")
        if params.get("AddShardConfig") is not None:
            self.AddShardConfig = AddShardConfig()
            self.AddShardConfig._deserialize(params.get("AddShardConfig"))
        if params.get("ExpandShardConfig") is not None:
            self.ExpandShardConfig = ExpandShardConfig()
            self.ExpandShardConfig._deserialize(params.get("ExpandShardConfig"))
        if params.get("SplitShardConfig") is not None:
            self.SplitShardConfig = SplitShardConfig()
            self.SplitShardConfig._deserialize(params.get("SplitShardConfig"))
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")


class UpgradeDCDBInstanceResponse(AbstractModel):
    """UpgradeDCDBInstance返回參數結構體

    """

    def __init__(self):
        """
        :param DealName: 長訂單號。可以據此調用 DescribeOrders
 查詢訂單詳細訊息，或在支付失敗時調用用戶賬號相關介面進行支付。
        :type DealName: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class ZonesInfo(AbstractModel):
    """可用區訊息

    """

    def __init__(self):
        """
        :param Zone: 可用區英文ID
        :type Zone: str
        :param ZoneId: 可用區數字ID
        :type ZoneId: int
        :param ZoneName: 可用區中文名
        :type ZoneName: str
        """
        self.Zone = None
        self.ZoneId = None
        self.ZoneName = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")