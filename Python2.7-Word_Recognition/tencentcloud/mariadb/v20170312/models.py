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
        :param FlowId: 異步任務流程ID。
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
        :param InstanceId: 待關閉外網訪問的實例ID。形如：tdsql-ow728lmc，可以通過 DescribeDBInstances 查詢實例詳情獲得。
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
        :param InstanceId: 實例 ID，形如：tdsql-ow728lmc，可以通過 DescribeDBInstances 查詢實例詳情獲得。
        :type InstanceId: str
        :param SrcUserName: 源用戶名
        :type SrcUserName: str
        :param SrcHost: 源用戶允許的訪問 host
        :type SrcHost: str
        :param DstUserName: 目的用戶名
        :type DstUserName: str
        :param DstHost: 目的用戶允許的訪問 host
        :type DstHost: str
        :param SrcReadOnly: 源賬号的 ReadOnly 屬性
        :type SrcReadOnly: str
        :param DstReadOnly: 目的賬号的 ReadOnly 屬性
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
        :param InstanceId: 實例 ID，形如：tdsql-ow728lmc，可以通過 DescribeDBInstances 查詢實例詳情獲得。
        :type InstanceId: str
        :param UserName: 登入用戶名，由字幕、數字、下劃線和連字元組成，長度爲1~32位。
        :type UserName: str
        :param Host: 可以登入的主機，與mysql 賬号的 host 格式一緻，可以支援通配符，例如 %，10.%，10.20.%。
        :type Host: str
        :param Password: 賬号密碼，由字母、數字或常見符号組成，不能包含分号、單引号和雙引号，長度爲6~32位。
        :type Password: str
        :param ReadOnly: 是否創建爲只讀賬号，0：否， 1：該賬号的sql請求優先選擇備機執行，備機不可用時選擇主機執行，2：優先選擇備機執行，備機不可用時操作失敗。
        :type ReadOnly: int
        :param Description: 賬号備注，可以包含中文、英文字元、常見符号和數字，長度爲0~256字元
        :type Description: str
        :param DelayThresh: 根據傳入時間判斷備機不可用
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


class CreateDBInstanceRequest(AbstractModel):
    """CreateDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param Zones: 實例節點可用區分布，最多可填兩個可用區。當分片規格爲一主兩從時，其中兩個節點在第一個可用區。
        :type Zones: list of str
        :param NodeCount: 節點個數大小，可以通過 DescribeDBInstanceSpecs
 查詢實例規格獲得。
        :type NodeCount: int
        :param Memory: 内存大小，單位：GB，可以通過 DescribeDBInstanceSpecs
 查詢實例規格獲得。
        :type Memory: int
        :param Storage: 儲存空間大小，單位：GB，可以通過 DescribeDBInstanceSpecs
 查詢實例規格獲得不同内存大小對應的磁盤規格下限和上限。
        :type Storage: int
        :param Period: 欲購買的時長，單位：月。
        :type Period: int
        :param Count: 欲購買的數量，預設查詢購買1個實例的價格。
        :type Count: int
        :param AutoVoucher: 是否自動使用 進行支付，預設不使用。
        :type AutoVoucher: bool
        :param VoucherIds:  ID清單，目前僅支援指定一張 。
        :type VoucherIds: list of str
        :param VpcId: 虛拟私有網絡 ID，不傳表示創建爲基礎網絡
        :type VpcId: str
        :param SubnetId: 虛拟私有網絡子網 ID，VpcId 不爲空時必填
        :type SubnetId: str
        :param ProjectId: 項目 ID，可以通過檢視項目清單獲取，不傳則關聯到預設項目
        :type ProjectId: int
        :param DbVersionId: 資料庫引擎版本，當前可選：10.0.10，10.1.9，5.7.17。如果不傳的話，預設爲 Mariadb 10.1.9。
        :type DbVersionId: str
        """
        self.Zones = None
        self.NodeCount = None
        self.Memory = None
        self.Storage = None
        self.Period = None
        self.Count = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.VpcId = None
        self.SubnetId = None
        self.ProjectId = None
        self.DbVersionId = None


    def _deserialize(self, params):
        self.Zones = params.get("Zones")
        self.NodeCount = params.get("NodeCount")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.Period = params.get("Period")
        self.Count = params.get("Count")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ProjectId = params.get("ProjectId")
        self.DbVersionId = params.get("DbVersionId")


class CreateDBInstanceResponse(AbstractModel):
    """CreateDBInstance返回參數結構體

    """

    def __init__(self):
        """
        :param DealName: 長訂單号。可以據此調用 DescribeOrders
 查詢訂單詳細訊息，或在支付失敗時調用用戶賬号相關介面進行支付。
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
    """雲資料庫賬号訊息

    """

    def __init__(self):
        """
        :param UserName: 用戶名
        :type UserName: str
        :param Host: 用戶可以從哪台主機登入（對應 MySQL 用戶的 host 欄位，UserName + Host 唯一标識一個用戶，IP形式，IP段以%結尾；支援填入%；爲空預設等于%）
        :type Host: str
        :param Description: 用戶備注訊息
        :type Description: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param UpdateTime: 最後更新時間
        :type UpdateTime: str
        :param ReadOnly: 只讀标記，0：否， 1：該賬号的sql請求優先選擇備機執行，備機不可用時選擇主機執行，2：優先選擇備機執行，備機不可用時操作失敗。
        :type ReadOnly: int
        :param DelayThresh: 該欄位對只讀帳号有意義，表示選擇主備延遲小於該值的備機
注意：此欄位可能返回 null，表示取不到有效值。
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


class DBBackupTimeConfig(AbstractModel):
    """雲資料庫實例備份時間配置訊息

    """

    def __init__(self):
        """
        :param InstanceId: 實例 Id
        :type InstanceId: str
        :param StartBackupTime: 每天備份執行的區間的開始時間，格式 mm:ss，形如 22:00
        :type StartBackupTime: str
        :param EndBackupTime: 每天備份執行的區間的結束時間，格式 mm:ss，形如 23:00
        :type EndBackupTime: str
        """
        self.InstanceId = None
        self.StartBackupTime = None
        self.EndBackupTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartBackupTime = params.get("StartBackupTime")
        self.EndBackupTime = params.get("EndBackupTime")


class DBInstance(AbstractModel):
    """描述雲資料庫實例的詳細訊息。

    """

    def __init__(self):
        """
        :param InstanceId: 實例 Id，唯一标識一個 TDSQL 實例
        :type InstanceId: str
        :param InstanceName: 實例名稱，用戶可修改
        :type InstanceName: str
        :param AppId: 實例所屬應用 Id
        :type AppId: int
        :param ProjectId: 實例所屬項目 Id
        :type ProjectId: int
        :param Region: 實例所在地域名稱，如 ap-shanghai
        :type Region: str
        :param Zone: 實例所在可用區名稱，如 ap-shanghai-1
        :type Zone: str
        :param VpcId: 私有網絡 Id，基礎網絡時爲 0
        :type VpcId: int
        :param SubnetId: 子網 Id，基礎網絡時爲 0
        :type SubnetId: int
        :param Status: 實例狀态：0 創建中，1 流程處理中， 2 運作中，3 實例未初始化，-1 實例已隔離，-2 實例已删除
        :type Status: int
        :param Vip: 内網 IP 網址
        :type Vip: str
        :param Vport: 内網端口
        :type Vport: int
        :param WanDomain: 外網訪問的域名，公網可解析
        :type WanDomain: str
        :param WanVip: 外網 IP 網址，公網可訪問
        :type WanVip: str
        :param WanPort: 外網端口
        :type WanPort: int
        :param CreateTime: 實例創建時間，格式爲 2006-01-02 15:04:05
        :type CreateTime: str
        :param UpdateTime: 實例最後更新時間，格式爲 2006-01-02 15:04:05
        :type UpdateTime: str
        :param AutoRenewFlag: 自動續約标志：0 否，1 是
        :type AutoRenewFlag: int
        :param PeriodEndTime: 實例到期時間，格式爲 2006-01-02 15:04:05
        :type PeriodEndTime: str
        :param Uin: 實例所屬賬号
        :type Uin: str
        :param TdsqlVersion: TDSQL 版本訊息
        :type TdsqlVersion: str
        :param Memory: 實例内存大小，單位 GB
        :type Memory: int
        :param Storage: 實例儲存大小，單位 GB
        :type Storage: int
        :param UniqueVpcId: 字串型的私有網絡Id
        :type UniqueVpcId: str
        :param UniqueSubnetId: 字串型的私有網絡子網Id
        :type UniqueSubnetId: str
        :param OriginSerialId: 原始實例ID（過時欄位，請勿依賴該值）
        :type OriginSerialId: str
        :param NodeCount: 節點數，2爲一主一從，3爲一主二從
        :type NodeCount: int
        :param IsTmp: 是否臨時實例，0爲否，非0爲是
        :type IsTmp: int
        :param ExclusterId: 獨享集群Id，爲空表示爲普通實例
        :type ExclusterId: str
        :param Id: 數字實例Id（過時欄位，請勿依賴該值）
        :type Id: int
        :param Pid: 産品類型 Id
        :type Pid: int
        :param Qps: 最大 Qps 值
        :type Qps: int
        :param Paymode: 付費模式
注意：此欄位可能返回 null，表示取不到有效值。
        :type Paymode: str
        :param Locker: 實例處于異步任務時的異步任務流程ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type Locker: int
        :param StatusDesc: 實例目前運作狀态描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type StatusDesc: str
        :param WanStatus: 外網狀态，0-未開通；1-已開通；2-關閉；3-開通中
        :type WanStatus: int
        :param IsAuditSupported: 該實例是否支援審計。1-支援；0-不支援
        :type IsAuditSupported: int
        :param Machine: 機器型号
        :type Machine: str
        :param IsEncryptSupported: 是否支援數據加密。1-支援；0-不支援
        :type IsEncryptSupported: int
        """
        self.InstanceId = None
        self.InstanceName = None
        self.AppId = None
        self.ProjectId = None
        self.Region = None
        self.Zone = None
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.Vip = None
        self.Vport = None
        self.WanDomain = None
        self.WanVip = None
        self.WanPort = None
        self.CreateTime = None
        self.UpdateTime = None
        self.AutoRenewFlag = None
        self.PeriodEndTime = None
        self.Uin = None
        self.TdsqlVersion = None
        self.Memory = None
        self.Storage = None
        self.UniqueVpcId = None
        self.UniqueSubnetId = None
        self.OriginSerialId = None
        self.NodeCount = None
        self.IsTmp = None
        self.ExclusterId = None
        self.Id = None
        self.Pid = None
        self.Qps = None
        self.Paymode = None
        self.Locker = None
        self.StatusDesc = None
        self.WanStatus = None
        self.IsAuditSupported = None
        self.Machine = None
        self.IsEncryptSupported = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.AppId = params.get("AppId")
        self.ProjectId = params.get("ProjectId")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.WanDomain = params.get("WanDomain")
        self.WanVip = params.get("WanVip")
        self.WanPort = params.get("WanPort")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.Uin = params.get("Uin")
        self.TdsqlVersion = params.get("TdsqlVersion")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.UniqueVpcId = params.get("UniqueVpcId")
        self.UniqueSubnetId = params.get("UniqueSubnetId")
        self.OriginSerialId = params.get("OriginSerialId")
        self.NodeCount = params.get("NodeCount")
        self.IsTmp = params.get("IsTmp")
        self.ExclusterId = params.get("ExclusterId")
        self.Id = params.get("Id")
        self.Pid = params.get("Pid")
        self.Qps = params.get("Qps")
        self.Paymode = params.get("Paymode")
        self.Locker = params.get("Locker")
        self.StatusDesc = params.get("StatusDesc")
        self.WanStatus = params.get("WanStatus")
        self.IsAuditSupported = params.get("IsAuditSupported")
        self.Machine = params.get("Machine")
        self.IsEncryptSupported = params.get("IsEncryptSupported")


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


class Deal(AbstractModel):
    """訂單訊息

    """

    def __init__(self):
        """
        :param DealName: 訂單号
        :type DealName: str
        :param OwnerUin: 所屬賬号
        :type OwnerUin: str
        :param Count: 商品數量
        :type Count: int
        :param FlowId: 關聯的流程 Id，可用于查詢流程執行狀态
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
        :param InstanceId: 實例ID，形如：tdsql-ow728lmc，可以通過 DescribeDBInstances 查詢實例詳情獲得。
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
        :param InstanceId: 實例 ID，形如：tdsql-ow728lmc，可以通過 DescribeDBInstances 查詢實例詳情獲得。
        :type InstanceId: str
        :param UserName: 登入用戶名。
        :type UserName: str
        :param Host: 用戶允許的訪問 host，用戶名+host唯一确定一個賬号。
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
        :param UserName: 資料庫賬号用戶名
        :type UserName: str
        :param Host: 資料庫賬号Host
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
        :param InstanceId: 實例ID，形如：tdsql-ow728lmc，可以通過 DescribeDBInstances 查詢實例詳情獲得。
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


class DescribeBackupTimeRequest(AbstractModel):
    """DescribeBackupTime請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 實例ID，形如：tdsql-ow728lmc，可以通過 DescribeDBInstances 查詢實例詳情獲得。
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class DescribeBackupTimeResponse(AbstractModel):
    """DescribeBackupTime返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 返回的配置數量
        :type TotalCount: int
        :param Items: 實例備份時間配置訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Items: list of DBBackupTimeConfig
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
                obj = DBBackupTimeConfig()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceSpecsRequest(AbstractModel):
    """DescribeDBInstanceSpecs請求參數結構體

    """


class DescribeDBInstanceSpecsResponse(AbstractModel):
    """DescribeDBInstanceSpecs返回參數結構體

    """

    def __init__(self):
        """
        :param Specs: 按機型分類的可售賣規格清單
        :type Specs: list of InstanceSpec
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Specs = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Specs") is not None:
            self.Specs = []
            for item in params.get("Specs"):
                obj = InstanceSpec()
                obj._deserialize(item)
                self.Specs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 按照一個或者多個實例 ID 查詢。實例 ID 形如：tdsql-ow728lmc。每次請求的實例的上限爲100。
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
        :param Limit: 返回數量，預設爲 20，最大值爲 100。
        :type Limit: int
        :param OriginSerialIds: 按 OriginSerialId 查詢
        :type OriginSerialIds: list of str
        :param IsFilterExcluster: 标識是否使用ExclusterType欄位, false不使用，true使用
        :type IsFilterExcluster: bool
        :param ExclusterType: 實例所屬獨享集群類型。取值範圍：1-非獨享集群，2-獨享集群， 0-全部
        :type ExclusterType: int
        :param ExclusterIds: 按獨享集群Id過濾實例，獨享集群Id形如dbdc-4ih6uct9
        :type ExclusterIds: list of str
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
        self.OriginSerialIds = None
        self.IsFilterExcluster = None
        self.ExclusterType = None
        self.ExclusterIds = None


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
        self.OriginSerialIds = params.get("OriginSerialIds")
        self.IsFilterExcluster = params.get("IsFilterExcluster")
        self.ExclusterType = params.get("ExclusterType")
        self.ExclusterIds = params.get("ExclusterIds")


class DescribeDBInstancesResponse(AbstractModel):
    """DescribeDBInstances返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的實例數量
        :type TotalCount: int
        :param Instances: 實例詳細訊息清單
        :type Instances: list of DBInstance
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
                obj = DBInstance()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBLogFilesRequest(AbstractModel):
    """DescribeDBLogFiles請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        :param Type: 請求日志類型，取值只能爲1、2、3或者4。1-binlog，2-冷備，3-errlog，4-slowlog。
        :type Type: int
        """
        self.InstanceId = None
        self.Type = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Type = params.get("Type")


class DescribeDBLogFilesResponse(AbstractModel):
    """DescribeDBLogFiles返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        :param Type: 請求日志類型，取值只能爲1、2、3或者4。1-binlog，2-冷備，3-errlog，4-slowlog。
        :type Type: int
        :param Total: 請求日志總數
        :type Total: int
        :param Files: 包含uri、length、mtime（修改時間）等訊息
        :type Files: list of LogFileInfo
        :param VpcPrefix: 如果是VPC網絡的實例，做用本前綴加上URI爲下載網址
        :type VpcPrefix: str
        :param NormalPrefix: 如果是普通網絡的實例，做用本前綴加上URI爲下載網址
        :type NormalPrefix: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.Type = None
        self.Total = None
        self.Files = None
        self.VpcPrefix = None
        self.NormalPrefix = None
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
        self.RequestId = params.get("RequestId")


class DescribeDBParametersRequest(AbstractModel):
    """DescribeDBParameters請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：tdsql-ow728lmc。
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
        :param InstanceId: 實例 ID，形如：tdsql-ow728lmc。
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


class DescribeDBPerformanceDetailsRequest(AbstractModel):
    """DescribeDBPerformanceDetails請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        :param StartTime: 開始日期，格式yyyy-mm-dd
        :type StartTime: str
        :param EndTime: 結束日期，格式yyyy-mm-dd
        :type EndTime: str
        :param MetricName: 拉取的指标名，支援的值爲：long_query,select_total,update_total,insert_total,delete_total,mem_hit_rate,disk_iops,conn_active,is_master_switched,slave_delay
        :type MetricName: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")


class DescribeDBPerformanceDetailsResponse(AbstractModel):
    """DescribeDBPerformanceDetails返回參數結構體

    """

    def __init__(self):
        """
        :param Master: 主節點效能監控數據
        :type Master: :class:`taifucloudcloud.mariadb.v20170312.models.PerformanceMonitorSet`
        :param Slave1: 備機1效能監控數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type Slave1: :class:`taifucloudcloud.mariadb.v20170312.models.PerformanceMonitorSet`
        :param Slave2: 備機2效能監控數據，如果實例是一主一從，則沒有該欄位
注意：此欄位可能返回 null，表示取不到有效值。
        :type Slave2: :class:`taifucloudcloud.mariadb.v20170312.models.PerformanceMonitorSet`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Master = None
        self.Slave1 = None
        self.Slave2 = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Master") is not None:
            self.Master = PerformanceMonitorSet()
            self.Master._deserialize(params.get("Master"))
        if params.get("Slave1") is not None:
            self.Slave1 = PerformanceMonitorSet()
            self.Slave1._deserialize(params.get("Slave1"))
        if params.get("Slave2") is not None:
            self.Slave2 = PerformanceMonitorSet()
            self.Slave2._deserialize(params.get("Slave2"))
        self.RequestId = params.get("RequestId")


class DescribeDBPerformanceRequest(AbstractModel):
    """DescribeDBPerformance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        :param StartTime: 開始日期，格式yyyy-mm-dd
        :type StartTime: str
        :param EndTime: 結束日期，格式yyyy-mm-dd
        :type EndTime: str
        :param MetricName: 拉取的指标名，支援的值爲：long_query,select_total,update_total,insert_total,delete_total,mem_hit_rate,disk_iops,conn_active,is_master_switched,slave_delay
        :type MetricName: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")


class DescribeDBPerformanceResponse(AbstractModel):
    """DescribeDBPerformance返回參數結構體

    """

    def __init__(self):
        """
        :param LongQuery: 慢查詢數
        :type LongQuery: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        :param SelectTotal: 查詢操作數SELECT
        :type SelectTotal: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        :param UpdateTotal: 更新操作數UPDATE
        :type UpdateTotal: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        :param InsertTotal: 插入操作數INSERT
        :type InsertTotal: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        :param DeleteTotal: 删除操作數DELETE
        :type DeleteTotal: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        :param MemHitRate: 快取命中率
        :type MemHitRate: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        :param DiskIops: 磁盤每秒IO次數
        :type DiskIops: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        :param ConnActive: 活躍連接數
        :type ConnActive: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        :param IsMasterSwitched: 是否發生主備切換，1爲發生，0否
        :type IsMasterSwitched: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        :param SlaveDelay: 主備延遲
        :type SlaveDelay: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.LongQuery = None
        self.SelectTotal = None
        self.UpdateTotal = None
        self.InsertTotal = None
        self.DeleteTotal = None
        self.MemHitRate = None
        self.DiskIops = None
        self.ConnActive = None
        self.IsMasterSwitched = None
        self.SlaveDelay = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LongQuery") is not None:
            self.LongQuery = MonitorData()
            self.LongQuery._deserialize(params.get("LongQuery"))
        if params.get("SelectTotal") is not None:
            self.SelectTotal = MonitorData()
            self.SelectTotal._deserialize(params.get("SelectTotal"))
        if params.get("UpdateTotal") is not None:
            self.UpdateTotal = MonitorData()
            self.UpdateTotal._deserialize(params.get("UpdateTotal"))
        if params.get("InsertTotal") is not None:
            self.InsertTotal = MonitorData()
            self.InsertTotal._deserialize(params.get("InsertTotal"))
        if params.get("DeleteTotal") is not None:
            self.DeleteTotal = MonitorData()
            self.DeleteTotal._deserialize(params.get("DeleteTotal"))
        if params.get("MemHitRate") is not None:
            self.MemHitRate = MonitorData()
            self.MemHitRate._deserialize(params.get("MemHitRate"))
        if params.get("DiskIops") is not None:
            self.DiskIops = MonitorData()
            self.DiskIops._deserialize(params.get("DiskIops"))
        if params.get("ConnActive") is not None:
            self.ConnActive = MonitorData()
            self.ConnActive._deserialize(params.get("ConnActive"))
        if params.get("IsMasterSwitched") is not None:
            self.IsMasterSwitched = MonitorData()
            self.IsMasterSwitched._deserialize(params.get("IsMasterSwitched"))
        if params.get("SlaveDelay") is not None:
            self.SlaveDelay = MonitorData()
            self.SlaveDelay._deserialize(params.get("SlaveDelay"))
        self.RequestId = params.get("RequestId")


class DescribeDBResourceUsageDetailsRequest(AbstractModel):
    """DescribeDBResourceUsageDetails請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        :param StartTime: 開始日期，格式yyyy-mm-dd
        :type StartTime: str
        :param EndTime: 結束日期，格式yyyy-mm-dd
        :type EndTime: str
        :param MetricName: 拉取的指标名稱，支援的值爲：data_disk_available,binlog_disk_available,mem_available,cpu_usage_rate
        :type MetricName: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")


class DescribeDBResourceUsageDetailsResponse(AbstractModel):
    """DescribeDBResourceUsageDetails返回參數結構體

    """

    def __init__(self):
        """
        :param Master: 主節點資源使用情況監控數據
        :type Master: :class:`taifucloudcloud.mariadb.v20170312.models.ResourceUsageMonitorSet`
        :param Slave1: 備機1資源使用情況監控數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type Slave1: :class:`taifucloudcloud.mariadb.v20170312.models.ResourceUsageMonitorSet`
        :param Slave2: 備機2資源使用情況監控數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type Slave2: :class:`taifucloudcloud.mariadb.v20170312.models.ResourceUsageMonitorSet`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Master = None
        self.Slave1 = None
        self.Slave2 = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Master") is not None:
            self.Master = ResourceUsageMonitorSet()
            self.Master._deserialize(params.get("Master"))
        if params.get("Slave1") is not None:
            self.Slave1 = ResourceUsageMonitorSet()
            self.Slave1._deserialize(params.get("Slave1"))
        if params.get("Slave2") is not None:
            self.Slave2 = ResourceUsageMonitorSet()
            self.Slave2._deserialize(params.get("Slave2"))
        self.RequestId = params.get("RequestId")


class DescribeDBResourceUsageRequest(AbstractModel):
    """DescribeDBResourceUsage請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        :param StartTime: 開始日期，格式yyyy-mm-dd
        :type StartTime: str
        :param EndTime: 結束日期，格式yyyy-mm-dd
        :type EndTime: str
        :param MetricName: 拉取的指标名稱，支援的值爲：data_disk_available,binlog_disk_available,mem_available,cpu_usage_rate
        :type MetricName: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")


class DescribeDBResourceUsageResponse(AbstractModel):
    """DescribeDBResourceUsage返回參數結構體

    """

    def __init__(self):
        """
        :param BinlogDiskAvailable: binlog日志磁盤可用空間,單位GB
        :type BinlogDiskAvailable: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        :param DataDiskAvailable: 磁盤可用空間,單位GB
        :type DataDiskAvailable: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        :param CpuUsageRate: CPU使用率
        :type CpuUsageRate: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        :param MemAvailable: 内存可用空間,單位GB
        :type MemAvailable: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.BinlogDiskAvailable = None
        self.DataDiskAvailable = None
        self.CpuUsageRate = None
        self.MemAvailable = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BinlogDiskAvailable") is not None:
            self.BinlogDiskAvailable = MonitorData()
            self.BinlogDiskAvailable._deserialize(params.get("BinlogDiskAvailable"))
        if params.get("DataDiskAvailable") is not None:
            self.DataDiskAvailable = MonitorData()
            self.DataDiskAvailable._deserialize(params.get("DataDiskAvailable"))
        if params.get("CpuUsageRate") is not None:
            self.CpuUsageRate = MonitorData()
            self.CpuUsageRate._deserialize(params.get("CpuUsageRate"))
        if params.get("MemAvailable") is not None:
            self.MemAvailable = MonitorData()
            self.MemAvailable._deserialize(params.get("MemAvailable"))
        self.RequestId = params.get("RequestId")


class DescribeDBSlowLogsRequest(AbstractModel):
    """DescribeDBSlowLogs請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        :param Offset: 從結果的第幾條數據開始返回
        :type Offset: int
        :param Limit: 返回的結果條數
        :type Limit: int
        :param StartTime: 查詢的起始時間，形如2016-07-23 14:55:20
        :type StartTime: str
        :param EndTime: 查詢的結束時間，形如2016-08-22 14:55:20
        :type EndTime: str
        :param Db: 要查詢的具體資料庫名稱
        :type Db: str
        :param OrderBy: 排序指标，取值爲query_time_sum或者query_count
        :type OrderBy: str
        :param OrderByType: 排序類型，desc或者asc
        :type OrderByType: str
        :param Slave: 是否查詢從機的慢查詢，0-主機; 1-從機
        :type Slave: int
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None
        self.StartTime = None
        self.EndTime = None
        self.Db = None
        self.OrderBy = None
        self.OrderByType = None
        self.Slave = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Db = params.get("Db")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        self.Slave = params.get("Slave")


class DescribeDBSlowLogsResponse(AbstractModel):
    """DescribeDBSlowLogs返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 慢查詢日志數據
        :type Data: list of SlowLogData
        :param LockTimeSum: 所有語句鎖時間總和
        :type LockTimeSum: float
        :param QueryCount: 所有語句查詢總次數
        :type QueryCount: int
        :param Total: 總記錄數
        :type Total: int
        :param QueryTimeSum: 所有語句查詢時間總和
        :type QueryTimeSum: float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.LockTimeSum = None
        self.QueryCount = None
        self.Total = None
        self.QueryTimeSum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SlowLogData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.LockTimeSum = params.get("LockTimeSum")
        self.QueryCount = params.get("QueryCount")
        self.Total = params.get("Total")
        self.QueryTimeSum = params.get("QueryTimeSum")
        self.RequestId = params.get("RequestId")


class DescribeFlowRequest(AbstractModel):
    """DescribeFlow請求參數結構體

    """

    def __init__(self):
        """
        :param FlowId: 異步請求介面返回的任務流程号。
        :type FlowId: int
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")


class DescribeFlowResponse(AbstractModel):
    """DescribeFlow返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 流程狀态，0：成功，1：失敗，2：運作中
        :type Status: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeLogFileRetentionPeriodRequest(AbstractModel):
    """DescribeLogFileRetentionPeriod請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeLogFileRetentionPeriodResponse(AbstractModel):
    """DescribeLogFileRetentionPeriod返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        :param Days: 日志備份天數
        :type Days: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.Days = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Days = params.get("Days")
        self.RequestId = params.get("RequestId")


class DescribeOrdersRequest(AbstractModel):
    """DescribeOrders請求參數結構體

    """

    def __init__(self):
        """
        :param DealNames: 待查詢的長訂單号清單，創建實例、續約實例、擴容實例介面返回。
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


class DescribePriceRequest(AbstractModel):
    """DescribePrice請求參數結構體

    """

    def __init__(self):
        """
        :param Zone: 欲新購實例的可用區ID。
        :type Zone: str
        :param NodeCount: 實例節點個數，可以通過 DescribeDBInstanceSpecs
 查詢實例規格獲得。
        :type NodeCount: int
        :param Memory: 内存大小，單位：GB，可以通過 DescribeDBInstanceSpecs
 查詢實例規格獲得。
        :type Memory: int
        :param Storage: 儲存空間大小，單位：GB，可以通過 DescribeDBInstanceSpecs
 查詢實例規格獲得不同内存大小對應的磁盤規格下限和上限。
        :type Storage: int
        :param Period: 欲購買的時長，單位：月。
        :type Period: int
        :param Count: 欲購買的數量，預設查詢購買1個實例的價格。
        :type Count: int
        """
        self.Zone = None
        self.NodeCount = None
        self.Memory = None
        self.Storage = None
        self.Period = None
        self.Count = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.NodeCount = params.get("NodeCount")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.Period = params.get("Period")
        self.Count = params.get("Count")


class DescribePriceResponse(AbstractModel):
    """DescribePrice返回參數結構體

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


class DescribeRenewalPriceRequest(AbstractModel):
    """DescribeRenewalPrice請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 待續約的實例ID。形如：tdsql-ow728lmc，可以通過 DescribeDBInstances 查詢實例詳情獲得。
        :type InstanceId: str
        :param Period: 續約時長，單位：月。不傳則預設爲1個月。
        :type Period: int
        """
        self.InstanceId = None
        self.Period = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Period = params.get("Period")


class DescribeRenewalPriceResponse(AbstractModel):
    """DescribeRenewalPrice返回參數結構體

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


class DescribeSaleInfoRequest(AbstractModel):
    """DescribeSaleInfo請求參數結構體

    """


class DescribeSaleInfoResponse(AbstractModel):
    """DescribeSaleInfo返回參數結構體

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


class DescribeSqlLogsRequest(AbstractModel):
    """DescribeSqlLogs請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：tdsql-ow728lmc，可以通過 DescribeDBInstances 查詢實例詳情獲得。
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


class DescribeUpgradePriceRequest(AbstractModel):
    """DescribeUpgradePrice請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 待升級的實例ID。形如：tdsql-ow728lmc，可以通過 DescribeDBInstances 查詢實例詳情獲得。
        :type InstanceId: str
        :param Memory: 内存大小，單位：GB，可以通過 DescribeDBInstanceSpecs
 查詢實例規格獲得。
        :type Memory: int
        :param Storage: 儲存空間大小，單位：GB，可以通過 DescribeDBInstanceSpecs
 查詢實例規格獲得不同内存大小對應的磁盤規格下限和上限。
        :type Storage: int
        """
        self.InstanceId = None
        self.Memory = None
        self.Storage = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")


class DescribeUpgradePriceResponse(AbstractModel):
    """DescribeUpgradePrice返回參數結構體

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


class GrantAccountPrivilegesRequest(AbstractModel):
    """GrantAccountPrivileges請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：tdsql-ow728lmc，可以通過 DescribeDBInstances 查詢實例詳情獲得。
        :type InstanceId: str
        :param UserName: 登入用戶名。
        :type UserName: str
        :param Host: 用戶允許的訪問 host，用戶名+host唯一确定一個賬号。
        :type Host: str
        :param DbName: 資料庫名。如果爲 \*，表示設置全局權限（即 \*.\*），此時忽略 Type 和 Object 參數。當DbName不爲\*時，需要傳入參 Type。
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


class InitDBInstancesRequest(AbstractModel):
    """InitDBInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 待初始化的實例Id清單，形如：tdsql-ow728lmc，可以通過 DescribeDBInstances 查詢實例詳情獲得。
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


class InitDBInstancesResponse(AbstractModel):
    """InitDBInstances返回參數結構體

    """

    def __init__(self):
        """
        :param FlowId: 異步任務Id，可通過 DescribeFlow 查詢任務狀态。
        :type FlowId: int
        :param InstanceIds: 透傳入參。
        :type InstanceIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class InstanceSpec(AbstractModel):
    """按機型歸類的實例可售賣規格訊息

    """

    def __init__(self):
        """
        :param Machine: 設備型号
        :type Machine: str
        :param SpecInfos: 該機型對應的可售賣規格清單
        :type SpecInfos: list of SpecConfigInfo
        """
        self.Machine = None
        self.SpecInfos = None


    def _deserialize(self, params):
        self.Machine = params.get("Machine")
        if params.get("SpecInfos") is not None:
            self.SpecInfos = []
            for item in params.get("SpecInfos"):
                obj = SpecConfigInfo()
                obj._deserialize(item)
                self.SpecInfos.append(obj)


class LogFileInfo(AbstractModel):
    """拉取的日志訊息

    """

    def __init__(self):
        """
        :param Mtime: Log最後修改時間
        :type Mtime: int
        :param Length: 文件長度
        :type Length: int
        :param Uri: 下載Log時用到的統一資源标識符
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
        :param InstanceId: 實例 ID，形如：tdsql-ow728lmc，可以通過 DescribeDBInstances 查詢實例詳情獲得。
        :type InstanceId: str
        :param UserName: 登入用戶名。
        :type UserName: str
        :param Host: 用戶允許的訪問 host，用戶名+host唯一确定一個賬号。
        :type Host: str
        :param Description: 新的賬号備注，長度 0~256。
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


class ModifyBackupTimeRequest(AbstractModel):
    """ModifyBackupTime請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，形如：tdsql-ow728lmc，可以通過 DescribeDBInstances 查詢實例詳情獲得。
        :type InstanceId: str
        :param StartBackupTime: 每天備份執行的區間的開始時間，格式 mm:ss，形如 22:00
        :type StartBackupTime: str
        :param EndBackupTime: 每天備份執行的區間的結束時間，格式 mm:ss，形如 23:59
        :type EndBackupTime: str
        """
        self.InstanceId = None
        self.StartBackupTime = None
        self.EndBackupTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartBackupTime = params.get("StartBackupTime")
        self.EndBackupTime = params.get("EndBackupTime")


class ModifyBackupTimeResponse(AbstractModel):
    """ModifyBackupTime返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 設置的狀态，0 表示成功
        :type Status: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceNameRequest(AbstractModel):
    """ModifyDBInstanceName請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 待修改的實例 ID。形如：tdsql-ow728lmc，可以通過 DescribeDBInstances 查詢實例詳情獲得。
        :type InstanceId: str
        :param InstanceName: 新的實例名稱。允許的字元爲字母、數字、下劃線、連字元和中文。
        :type InstanceName: str
        """
        self.InstanceId = None
        self.InstanceName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")


class ModifyDBInstanceNameResponse(AbstractModel):
    """ModifyDBInstanceName返回參數結構體

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
        :param InstanceIds: 待修改的實例ID清單。實例 ID 形如：tdsql-ow728lmc，可以通過 DescribeDBInstances 查詢實例詳情獲得。
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
        :param InstanceId: 實例 ID，形如：tdsql-ow728lmc。
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
        :param InstanceId: 實例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        :param Result: 參數修改結果
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


class ModifyLogFileRetentionPeriodRequest(AbstractModel):
    """ModifyLogFileRetentionPeriod請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        :param Days: 保存的天數,不能超過30
        :type Days: int
        """
        self.InstanceId = None
        self.Days = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Days = params.get("Days")


class ModifyLogFileRetentionPeriodResponse(AbstractModel):
    """ModifyLogFileRetentionPeriod返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID，形如：tdsql-ow728lmc。
        :type InstanceId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class MonitorData(AbstractModel):
    """監控數據

    """

    def __init__(self):
        """
        :param StartTime: 起始時間，形如 2018-03-24 23:59:59
        :type StartTime: str
        :param EndTime: 結束時間，形如 2018-03-24 23:59:59
        :type EndTime: str
        :param Data: 監控數據
        :type Data: list of float
        """
        self.StartTime = None
        self.EndTime = None
        self.Data = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Data = params.get("Data")


class OpenDBExtranetAccessRequest(AbstractModel):
    """OpenDBExtranetAccess請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 待開放外網訪問的實例ID。形如：tdsql-ow728lmc，可以通過 DescribeDBInstances 查詢實例詳情獲得。
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
        :type Range: :class:`taifucloudcloud.mariadb.v20170312.models.ConstraintRange`
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
        :param SetValue: 設置過的值，參數生效後，該值和value一樣。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SetValue: str
        :param Default: 系統預設值
        :type Default: str
        :param Constraint: 參數限制
        :type Constraint: :class:`taifucloudcloud.mariadb.v20170312.models.ParamConstraint`
        :param HaveSetValue: 是否有設置過值，false:沒有設置過值，true:有設置過值。
        :type HaveSetValue: bool
        """
        self.Param = None
        self.Value = None
        self.SetValue = None
        self.Default = None
        self.Constraint = None
        self.HaveSetValue = None


    def _deserialize(self, params):
        self.Param = params.get("Param")
        self.Value = params.get("Value")
        self.SetValue = params.get("SetValue")
        self.Default = params.get("Default")
        if params.get("Constraint") is not None:
            self.Constraint = ParamConstraint()
            self.Constraint._deserialize(params.get("Constraint"))
        self.HaveSetValue = params.get("HaveSetValue")


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


class PerformanceMonitorSet(AbstractModel):
    """DB效能監控指标集合

    """

    def __init__(self):
        """
        :param UpdateTotal: 更新操作數UPDATE
        :type UpdateTotal: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        :param DiskIops: 磁盤每秒IO次數
        :type DiskIops: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        :param ConnActive: 活躍連接數
        :type ConnActive: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        :param MemHitRate: 快取命中率
        :type MemHitRate: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        :param SlaveDelay: 主備延遲
        :type SlaveDelay: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        :param SelectTotal: 查詢操作數SELECT
        :type SelectTotal: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        :param LongQuery: 慢查詢數
        :type LongQuery: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        :param DeleteTotal: 删除操作數DELETE
        :type DeleteTotal: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        :param InsertTotal: 插入操作數INSERT
        :type InsertTotal: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        :param IsMasterSwitched: 是否發生主備切換，1爲發生，0否
        :type IsMasterSwitched: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        """
        self.UpdateTotal = None
        self.DiskIops = None
        self.ConnActive = None
        self.MemHitRate = None
        self.SlaveDelay = None
        self.SelectTotal = None
        self.LongQuery = None
        self.DeleteTotal = None
        self.InsertTotal = None
        self.IsMasterSwitched = None


    def _deserialize(self, params):
        if params.get("UpdateTotal") is not None:
            self.UpdateTotal = MonitorData()
            self.UpdateTotal._deserialize(params.get("UpdateTotal"))
        if params.get("DiskIops") is not None:
            self.DiskIops = MonitorData()
            self.DiskIops._deserialize(params.get("DiskIops"))
        if params.get("ConnActive") is not None:
            self.ConnActive = MonitorData()
            self.ConnActive._deserialize(params.get("ConnActive"))
        if params.get("MemHitRate") is not None:
            self.MemHitRate = MonitorData()
            self.MemHitRate._deserialize(params.get("MemHitRate"))
        if params.get("SlaveDelay") is not None:
            self.SlaveDelay = MonitorData()
            self.SlaveDelay._deserialize(params.get("SlaveDelay"))
        if params.get("SelectTotal") is not None:
            self.SelectTotal = MonitorData()
            self.SelectTotal._deserialize(params.get("SelectTotal"))
        if params.get("LongQuery") is not None:
            self.LongQuery = MonitorData()
            self.LongQuery._deserialize(params.get("LongQuery"))
        if params.get("DeleteTotal") is not None:
            self.DeleteTotal = MonitorData()
            self.DeleteTotal._deserialize(params.get("DeleteTotal"))
        if params.get("InsertTotal") is not None:
            self.InsertTotal = MonitorData()
            self.InsertTotal._deserialize(params.get("InsertTotal"))
        if params.get("IsMasterSwitched") is not None:
            self.IsMasterSwitched = MonitorData()
            self.IsMasterSwitched._deserialize(params.get("IsMasterSwitched"))


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
        :type AvailableChoice: list of ZoneChooseInfo
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
                obj = ZoneChooseInfo()
                obj._deserialize(item)
                self.AvailableChoice.append(obj)


class RenewDBInstanceRequest(AbstractModel):
    """RenewDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 待續約的實例ID。形如：tdsql-ow728lmc，可以通過 DescribeDBInstances 查詢實例詳情獲得。
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


class RenewDBInstanceResponse(AbstractModel):
    """RenewDBInstance返回參數結構體

    """

    def __init__(self):
        """
        :param DealName: 長訂單号。可以據此調用 DescribeOrders
 查詢訂單詳細訊息，或在支付失敗時調用用戶賬号相關介面進行支付。
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
        :param InstanceId: 實例 ID，形如：tdsql-ow728lmc，可以通過 DescribeDBInstances 查詢實例詳情獲得。
        :type InstanceId: str
        :param UserName: 登入用戶名。
        :type UserName: str
        :param Host: 用戶允許的訪問 host，用戶名+host唯一确定一個賬号。
        :type Host: str
        :param Password: 新密碼，由字母、數字或常見符号組成，不能包含分号、單引号和雙引号，長度爲6~32位。
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


class ResourceUsageMonitorSet(AbstractModel):
    """DB資源使用情況監控指标集合

    """

    def __init__(self):
        """
        :param BinlogDiskAvailable: binlog日志磁盤可用空間,單位GB
        :type BinlogDiskAvailable: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        :param CpuUsageRate: CPU使用率
        :type CpuUsageRate: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        :param MemAvailable: 内存可用空間,單位GB
        :type MemAvailable: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        :param DataDiskAvailable: 磁盤可用空間,單位GB
        :type DataDiskAvailable: :class:`taifucloudcloud.mariadb.v20170312.models.MonitorData`
        """
        self.BinlogDiskAvailable = None
        self.CpuUsageRate = None
        self.MemAvailable = None
        self.DataDiskAvailable = None


    def _deserialize(self, params):
        if params.get("BinlogDiskAvailable") is not None:
            self.BinlogDiskAvailable = MonitorData()
            self.BinlogDiskAvailable._deserialize(params.get("BinlogDiskAvailable"))
        if params.get("CpuUsageRate") is not None:
            self.CpuUsageRate = MonitorData()
            self.CpuUsageRate._deserialize(params.get("CpuUsageRate"))
        if params.get("MemAvailable") is not None:
            self.MemAvailable = MonitorData()
            self.MemAvailable._deserialize(params.get("MemAvailable"))
        if params.get("DataDiskAvailable") is not None:
            self.DataDiskAvailable = MonitorData()
            self.DataDiskAvailable._deserialize(params.get("DataDiskAvailable"))


class SlowLogData(AbstractModel):
    """慢查詢條目訊息

    """

    def __init__(self):
        """
        :param CheckSum: 語句校驗和，用于查詢詳情
        :type CheckSum: str
        :param Db: 資料庫名稱
        :type Db: str
        :param FingerPrint: 抽象的SQL語句
        :type FingerPrint: str
        :param LockTimeAvg: 平均的鎖時間
        :type LockTimeAvg: str
        :param LockTimeMax: 最大鎖時間
        :type LockTimeMax: str
        :param LockTimeMin: 最小鎖時間
        :type LockTimeMin: str
        :param LockTimeSum: 鎖時間總和
        :type LockTimeSum: str
        :param QueryCount: 查詢次數
        :type QueryCount: str
        :param QueryTimeAvg: 平均查詢時間
        :type QueryTimeAvg: str
        :param QueryTimeMax: 最大查詢時間
        :type QueryTimeMax: str
        :param QueryTimeMin: 最小查詢時間
        :type QueryTimeMin: str
        :param QueryTimeSum: 查詢時間總和
        :type QueryTimeSum: str
        :param RowsExaminedSum: 掃描行數
        :type RowsExaminedSum: str
        :param RowsSentSum: 發送行數
        :type RowsSentSum: str
        :param TsMax: 最後執行時間
        :type TsMax: str
        :param TsMin: 首次執行時間
        :type TsMin: str
        :param User: 帳号
        :type User: str
        """
        self.CheckSum = None
        self.Db = None
        self.FingerPrint = None
        self.LockTimeAvg = None
        self.LockTimeMax = None
        self.LockTimeMin = None
        self.LockTimeSum = None
        self.QueryCount = None
        self.QueryTimeAvg = None
        self.QueryTimeMax = None
        self.QueryTimeMin = None
        self.QueryTimeSum = None
        self.RowsExaminedSum = None
        self.RowsSentSum = None
        self.TsMax = None
        self.TsMin = None
        self.User = None


    def _deserialize(self, params):
        self.CheckSum = params.get("CheckSum")
        self.Db = params.get("Db")
        self.FingerPrint = params.get("FingerPrint")
        self.LockTimeAvg = params.get("LockTimeAvg")
        self.LockTimeMax = params.get("LockTimeMax")
        self.LockTimeMin = params.get("LockTimeMin")
        self.LockTimeSum = params.get("LockTimeSum")
        self.QueryCount = params.get("QueryCount")
        self.QueryTimeAvg = params.get("QueryTimeAvg")
        self.QueryTimeMax = params.get("QueryTimeMax")
        self.QueryTimeMin = params.get("QueryTimeMin")
        self.QueryTimeSum = params.get("QueryTimeSum")
        self.RowsExaminedSum = params.get("RowsExaminedSum")
        self.RowsSentSum = params.get("RowsSentSum")
        self.TsMax = params.get("TsMax")
        self.TsMin = params.get("TsMin")
        self.User = params.get("User")


class SpecConfigInfo(AbstractModel):
    """實例可售賣規格詳細訊息，創建實例和擴容實例時 Pid+MemSize 唯一确定一種售賣規格，磁盤大小可用區間爲[MinDataDisk,MaxDataDisk]

    """

    def __init__(self):
        """
        :param Machine: 設備型号
        :type Machine: str
        :param Memory: 内存大小，單位 GB
        :type Memory: int
        :param MinStorage: 數據盤規格最小值，單位 GB
        :type MinStorage: int
        :param MaxStorage: 數據盤規格最大值，單位 GB
        :type MaxStorage: int
        :param SuitInfo: 推薦的使用場景
        :type SuitInfo: str
        :param Qps: 最大 Qps 值
        :type Qps: int
        :param Pid: 産品類型 Id
        :type Pid: int
        :param NodeCount: 節點個數，2 表示一主一從，3 表示一主二從
        :type NodeCount: int
        """
        self.Machine = None
        self.Memory = None
        self.MinStorage = None
        self.MaxStorage = None
        self.SuitInfo = None
        self.Qps = None
        self.Pid = None
        self.NodeCount = None


    def _deserialize(self, params):
        self.Machine = params.get("Machine")
        self.Memory = params.get("Memory")
        self.MinStorage = params.get("MinStorage")
        self.MaxStorage = params.get("MaxStorage")
        self.SuitInfo = params.get("SuitInfo")
        self.Qps = params.get("Qps")
        self.Pid = params.get("Pid")
        self.NodeCount = params.get("NodeCount")


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


class UpgradeDBInstanceRequest(AbstractModel):
    """UpgradeDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 待升級的實例ID。形如：tdsql-ow728lmc，可以通過 DescribeDBInstances 查詢實例詳情獲得。
        :type InstanceId: str
        :param Memory: 内存大小，單位：GB，可以通過 DescribeDBInstanceSpecs
 查詢實例規格獲得。
        :type Memory: int
        :param Storage: 儲存空間大小，單位：GB，可以通過 DescribeDBInstanceSpecs
 查詢實例規格獲得不同内存大小對應的磁盤規格下限和上限。
        :type Storage: int
        :param AutoVoucher: 是否自動使用 進行支付，預設不使用。
        :type AutoVoucher: bool
        :param VoucherIds:  ID清單，目前僅支援指定一張 。
        :type VoucherIds: list of str
        """
        self.InstanceId = None
        self.Memory = None
        self.Storage = None
        self.AutoVoucher = None
        self.VoucherIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")


class UpgradeDBInstanceResponse(AbstractModel):
    """UpgradeDBInstance返回參數結構體

    """

    def __init__(self):
        """
        :param DealName: 長訂單号。可以據此調用 DescribeOrders
 查詢訂單詳細訊息，或在支付失敗時調用用戶賬号相關介面進行支付。
        :type DealName: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class ZoneChooseInfo(AbstractModel):
    """分片節點可用區選擇

    """

    def __init__(self):
        """
        :param MasterZone: 主可用區
        :type MasterZone: :class:`taifucloudcloud.mariadb.v20170312.models.ZonesInfo`
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