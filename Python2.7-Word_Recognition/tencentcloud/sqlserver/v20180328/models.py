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


class AccountCreateInfo(AbstractModel):
    """賬号創建訊息

    """

    def __init__(self):
        """
        :param UserName: 實例用戶名
        :type UserName: str
        :param Password: 實例密碼
        :type Password: str
        :param DBPrivileges: DB權限清單
        :type DBPrivileges: list of DBPrivilege
        :param Remark: 賬号備注訊息
        :type Remark: str
        """
        self.UserName = None
        self.Password = None
        self.DBPrivileges = None
        self.Remark = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        if params.get("DBPrivileges") is not None:
            self.DBPrivileges = []
            for item in params.get("DBPrivileges"):
                obj = DBPrivilege()
                obj._deserialize(item)
                self.DBPrivileges.append(obj)
        self.Remark = params.get("Remark")


class AccountDetail(AbstractModel):
    """帳戶訊息詳情

    """

    def __init__(self):
        """
        :param Name: 帳戶名
        :type Name: str
        :param Remark: 帳戶備注
        :type Remark: str
        :param CreateTime: 帳戶創建時間
        :type CreateTime: str
        :param Status: 帳戶狀态，1-創建中，2-正常，3-修改中，4-密碼重置中，-1-删除中
        :type Status: int
        :param UpdateTime: 帳戶更新時間
        :type UpdateTime: str
        :param PassTime: 密碼更新時間
        :type PassTime: str
        :param InternalStatus: 帳戶内部狀态，正常爲enable
        :type InternalStatus: str
        :param Dbs: 該帳戶對相關db的讀寫權限訊息
        :type Dbs: list of DBPrivilege
        """
        self.Name = None
        self.Remark = None
        self.CreateTime = None
        self.Status = None
        self.UpdateTime = None
        self.PassTime = None
        self.InternalStatus = None
        self.Dbs = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")
        self.UpdateTime = params.get("UpdateTime")
        self.PassTime = params.get("PassTime")
        self.InternalStatus = params.get("InternalStatus")
        if params.get("Dbs") is not None:
            self.Dbs = []
            for item in params.get("Dbs"):
                obj = DBPrivilege()
                obj._deserialize(item)
                self.Dbs.append(obj)


class AccountPassword(AbstractModel):
    """實例賬号密碼訊息

    """

    def __init__(self):
        """
        :param UserName: 用戶名
        :type UserName: str
        :param Password: 密碼
        :type Password: str
        """
        self.UserName = None
        self.Password = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")


class AccountPrivilege(AbstractModel):
    """資料庫賬号權限訊息。創建資料庫時設置

    """

    def __init__(self):
        """
        :param UserName: 資料庫用戶名
        :type UserName: str
        :param Privilege: 資料庫權限。ReadWrite表示可讀寫，ReadOnly表示只讀
        :type Privilege: str
        """
        self.UserName = None
        self.Privilege = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Privilege = params.get("Privilege")


class AccountPrivilegeModifyInfo(AbstractModel):
    """資料庫賬号權限變更訊息

    """

    def __init__(self):
        """
        :param UserName: 資料庫用戶名
        :type UserName: str
        :param DBPrivileges: 賬号權限變更訊息
        :type DBPrivileges: list of DBPrivilegeModifyInfo
        """
        self.UserName = None
        self.DBPrivileges = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        if params.get("DBPrivileges") is not None:
            self.DBPrivileges = []
            for item in params.get("DBPrivileges"):
                obj = DBPrivilegeModifyInfo()
                obj._deserialize(item)
                self.DBPrivileges.append(obj)


class AccountRemark(AbstractModel):
    """帳戶備注訊息

    """

    def __init__(self):
        """
        :param UserName: 帳戶名
        :type UserName: str
        :param Remark: 對應帳戶新的備注訊息
        :type Remark: str
        """
        self.UserName = None
        self.Remark = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Remark = params.get("Remark")


class Backup(AbstractModel):
    """備份文件詳細訊息

    """

    def __init__(self):
        """
        :param FileName: 文件名
        :type FileName: str
        :param Size: 文件大小，單位 KB
        :type Size: int
        :param StartTime: 備份開始時間
        :type StartTime: str
        :param EndTime: 備份結束時間
        :type EndTime: str
        :param InternalAddr: 内網下載網址
        :type InternalAddr: str
        :param ExternalAddr: 外網下載網址
        :type ExternalAddr: str
        :param Id: 備份文件唯一标識，RestoreInstance介面會用到該欄位
        :type Id: int
        :param Status: 備份文件狀态（0-創建中；1-成功；2-失敗）
        :type Status: int
        :param DBs: 多庫備份時的DB清單
        :type DBs: list of str
        :param Strategy: 備份策略（0-實例備份；1-多庫備份）
        :type Strategy: int
        :param BackupWay: 備份方式，0-定時備份；1-手動臨時備份
        :type BackupWay: int
        """
        self.FileName = None
        self.Size = None
        self.StartTime = None
        self.EndTime = None
        self.InternalAddr = None
        self.ExternalAddr = None
        self.Id = None
        self.Status = None
        self.DBs = None
        self.Strategy = None
        self.BackupWay = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.Size = params.get("Size")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.InternalAddr = params.get("InternalAddr")
        self.ExternalAddr = params.get("ExternalAddr")
        self.Id = params.get("Id")
        self.Status = params.get("Status")
        self.DBs = params.get("DBs")
        self.Strategy = params.get("Strategy")
        self.BackupWay = params.get("BackupWay")


class CreateAccountRequest(AbstractModel):
    """CreateAccount請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 資料庫實例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param Accounts: 資料庫實例帳戶訊息
        :type Accounts: list of AccountCreateInfo
        """
        self.InstanceId = None
        self.Accounts = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = AccountCreateInfo()
                obj._deserialize(item)
                self.Accounts.append(obj)


class CreateAccountResponse(AbstractModel):
    """CreateAccount返回參數結構體

    """

    def __init__(self):
        """
        :param FlowId: 任務流id
        :type FlowId: int
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CreateBackupRequest(AbstractModel):
    """CreateBackup請求參數結構體

    """

    def __init__(self):
        """
        :param Strategy: 備份策略(0-實例備份 1-多庫備份)
        :type Strategy: int
        :param DBNames: 需要備份庫名的清單(多庫備份才填寫)
        :type DBNames: list of str
        :param InstanceId: 實例ID，形如mssql-i1z41iwd
        :type InstanceId: str
        """
        self.Strategy = None
        self.DBNames = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Strategy = params.get("Strategy")
        self.DBNames = params.get("DBNames")
        self.InstanceId = params.get("InstanceId")


class CreateBackupResponse(AbstractModel):
    """CreateBackup返回參數結構體

    """

    def __init__(self):
        """
        :param FlowId: 異步任務ID
        :type FlowId: int
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CreateDBInstancesRequest(AbstractModel):
    """CreateDBInstances請求參數結構體

    """

    def __init__(self):
        """
        :param Zone: 實例可用區，類似ap-guangzhou-1（廣州一區）；實例可售賣區域可以通過介面DescribeZones獲取
        :type Zone: str
        :param Memory: 實例内存大小，單位GB
        :type Memory: int
        :param Storage: 實例磁盤大小，單位GB
        :type Storage: int
        :param InstanceChargeType: 付費模式，目前只支援預付費，其值爲PREPAID。可不填，預設值爲PREPAID
        :type InstanceChargeType: str
        :param ProjectId: 項目ID
        :type ProjectId: int
        :param GoodsNum: 本次購買幾個實例，預設值爲1。取值不超過10
        :type GoodsNum: int
        :param SubnetId: VPC子網ID，形如subnet-bdoe83fa；SubnetId和VpcId需同時設置或者同時不設置
        :type SubnetId: str
        :param VpcId: VPC網絡ID，形如vpc-dsp338hz；SubnetId和VpcId需同時設置或者同時不設置
        :type VpcId: str
        :param Period: 購買實例週期，預設取值爲1，表示一個月。取值不超過48
        :type Period: int
        :param AutoVoucher: 是否自動使用代金券；1 - 是，0 - 否，預設不使用
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID數組，目前單個訂單只能使用一張
        :type VoucherIds: list of str
        :param DBVersion: 資料庫版本号，目前取值有2012SP3，表示SQL Server 2012；2008R2，表示SQL Server 2008 R2；2016SP1，表示SQL Server 2016 SP1。每個地域支援售賣的版本可能不一樣，可以通過DescribeZones介面來拉取每個地域可售賣的版本訊息。不填的話，預設爲版本2008R2
        :type DBVersion: str
        """
        self.Zone = None
        self.Memory = None
        self.Storage = None
        self.InstanceChargeType = None
        self.ProjectId = None
        self.GoodsNum = None
        self.SubnetId = None
        self.VpcId = None
        self.Period = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.DBVersion = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.ProjectId = params.get("ProjectId")
        self.GoodsNum = params.get("GoodsNum")
        self.SubnetId = params.get("SubnetId")
        self.VpcId = params.get("VpcId")
        self.Period = params.get("Period")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.DBVersion = params.get("DBVersion")


class CreateDBInstancesResponse(AbstractModel):
    """CreateDBInstances返回參數結構體

    """

    def __init__(self):
        """
        :param DealName: 訂單名稱
        :type DealName: str
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class CreateDBRequest(AbstractModel):
    """CreateDB請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例id
        :type InstanceId: str
        :param DBs: 資料庫創建訊息
        :type DBs: list of DBCreateInfo
        """
        self.InstanceId = None
        self.DBs = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("DBs") is not None:
            self.DBs = []
            for item in params.get("DBs"):
                obj = DBCreateInfo()
                obj._deserialize(item)
                self.DBs.append(obj)


class CreateDBResponse(AbstractModel):
    """CreateDB返回參數結構體

    """

    def __init__(self):
        """
        :param FlowId: 任務流id
        :type FlowId: int
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CreateMigrationRequest(AbstractModel):
    """CreateMigration請求參數結構體

    """

    def __init__(self):
        """
        :param MigrateName: 遷移任務的名稱
        :type MigrateName: str
        :param MigrateType: 遷移類型（1:結構遷移 2:數據遷移 3:增量同步）
        :type MigrateType: int
        :param SourceType: 遷移源的類型 1:CDB for SQLServer 2:雲伺服器自建SQLServer資料庫 4:SQLServer備份還原 5:SQLServer備份還原（COS方式）
        :type SourceType: int
        :param Source: 遷移源
        :type Source: :class:`tencentcloud.sqlserver.v20180328.models.MigrateSource`
        :param Target: 遷移目标
        :type Target: :class:`tencentcloud.sqlserver.v20180328.models.MigrateTarget`
        :param MigrateDBSet: 遷移DB對象 ，離線遷移不使用（SourceType=4或SourceType=5）。
        :type MigrateDBSet: list of MigrateDB
        """
        self.MigrateName = None
        self.MigrateType = None
        self.SourceType = None
        self.Source = None
        self.Target = None
        self.MigrateDBSet = None


    def _deserialize(self, params):
        self.MigrateName = params.get("MigrateName")
        self.MigrateType = params.get("MigrateType")
        self.SourceType = params.get("SourceType")
        if params.get("Source") is not None:
            self.Source = MigrateSource()
            self.Source._deserialize(params.get("Source"))
        if params.get("Target") is not None:
            self.Target = MigrateTarget()
            self.Target._deserialize(params.get("Target"))
        if params.get("MigrateDBSet") is not None:
            self.MigrateDBSet = []
            for item in params.get("MigrateDBSet"):
                obj = MigrateDB()
                obj._deserialize(item)
                self.MigrateDBSet.append(obj)


class CreateMigrationResponse(AbstractModel):
    """CreateMigration返回參數結構體

    """

    def __init__(self):
        """
        :param MigrateId: 遷移任務ID
        :type MigrateId: int
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.MigrateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")
        self.RequestId = params.get("RequestId")


class DBCreateInfo(AbstractModel):
    """資料庫創建訊息

    """

    def __init__(self):
        """
        :param DBName: 資料庫名
        :type DBName: str
        :param Charset: 字元集。可選值包括：Chinese_PRC_CI_AS, Chinese_PRC_CS_AS, Chinese_PRC_BIN, Chinese_Taiwan_Stroke_CI_AS, SQL_Latin1_General_CP1_CI_AS, SQL_Latin1_General_CP1_CS_AS。不填預設爲Chinese_PRC_CI_AS
        :type Charset: str
        :param Accounts: 資料庫賬号權限訊息
        :type Accounts: list of AccountPrivilege
        :param Remark: 備注
        :type Remark: str
        """
        self.DBName = None
        self.Charset = None
        self.Accounts = None
        self.Remark = None


    def _deserialize(self, params):
        self.DBName = params.get("DBName")
        self.Charset = params.get("Charset")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = AccountPrivilege()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.Remark = params.get("Remark")


class DBDetail(AbstractModel):
    """資料庫訊息

    """

    def __init__(self):
        """
        :param Name: 實例id
        :type Name: str
        :param Charset: 字元集
        :type Charset: str
        :param Remark: 備注
        :type Remark: str
        :param CreateTime: 資料庫創建時間
        :type CreateTime: str
        :param Status: 資料庫狀态。1--創建中， 2--運作中， 3--修改中，-1--删除中
        :type Status: int
        :param Accounts: 資料庫賬号權限訊息
        :type Accounts: list of AccountPrivilege
        :param InternalStatus: 内部狀态。ONLINE表示運作中
        :type InternalStatus: str
        """
        self.Name = None
        self.Charset = None
        self.Remark = None
        self.CreateTime = None
        self.Status = None
        self.Accounts = None
        self.InternalStatus = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Charset = params.get("Charset")
        self.Remark = params.get("Remark")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = AccountPrivilege()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.InternalStatus = params.get("InternalStatus")


class DBInstance(AbstractModel):
    """實例詳細訊息

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param Name: 實例名稱
        :type Name: str
        :param ProjectId: 實例所在項目ID
        :type ProjectId: int
        :param RegionId: 實例所在地域ID
        :type RegionId: int
        :param ZoneId: 實例所在可用區ID
        :type ZoneId: int
        :param VpcId: 實例所在私有網絡ID，基礎網絡時爲 0
        :type VpcId: int
        :param SubnetId: 實例所在私有網絡子網ID，基礎網絡時爲 0
        :type SubnetId: int
        :param Status: 實例狀态。取值範圍： <li>1：申請中</li> <li>2：運作中</li> <li>3：受限運作中 (主備切換中)</li> <li>4：已隔離</li> <li>5：回收中</li> <li>6：已回收</li> <li>7：任務執行中 (實例做備份、回檔等操作)</li> <li>8：已下線</li> <li>9：實例擴容中</li> <li>10：實例遷移中</li> <li>11：只讀</li> <li>12：重啓中</li>
        :type Status: int
        :param Vip: 實例訪問IP
        :type Vip: str
        :param Vport: 實例訪問端口
        :type Vport: int
        :param CreateTime: 實例創建時間
        :type CreateTime: str
        :param UpdateTime: 實例更新時間
        :type UpdateTime: str
        :param StartTime: 實例計費開始時間
        :type StartTime: str
        :param EndTime: 實例計費結束時間
        :type EndTime: str
        :param IsolateTime: 實例隔離時間
        :type IsolateTime: str
        :param Memory: 實例内存大小，單位G
        :type Memory: int
        :param UsedStorage: 實例已經使用儲存空間大小，單位G
        :type UsedStorage: int
        :param Storage: 實例儲存空間大小，單位G
        :type Storage: int
        :param VersionName: 實例版本
        :type VersionName: str
        :param RenewFlag: 實例續約标記，0-正常續約，1-自動續約，2-到期不續約
        :type RenewFlag: int
        :param Model: 實例高可用， 1-雙機高可用，2-單機
        :type Model: int
        :param Region: 實例所在地域名稱，如 ap-guangzhou
        :type Region: str
        :param Zone: 實例所在可用區名稱，如 ap-guangzhou-1
        :type Zone: str
        :param BackupTime: 備份時間點
        :type BackupTime: str
        """
        self.InstanceId = None
        self.Name = None
        self.ProjectId = None
        self.RegionId = None
        self.ZoneId = None
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.Vip = None
        self.Vport = None
        self.CreateTime = None
        self.UpdateTime = None
        self.StartTime = None
        self.EndTime = None
        self.IsolateTime = None
        self.Memory = None
        self.UsedStorage = None
        self.Storage = None
        self.VersionName = None
        self.RenewFlag = None
        self.Model = None
        self.Region = None
        self.Zone = None
        self.BackupTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        self.ProjectId = params.get("ProjectId")
        self.RegionId = params.get("RegionId")
        self.ZoneId = params.get("ZoneId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.IsolateTime = params.get("IsolateTime")
        self.Memory = params.get("Memory")
        self.UsedStorage = params.get("UsedStorage")
        self.Storage = params.get("Storage")
        self.VersionName = params.get("VersionName")
        self.RenewFlag = params.get("RenewFlag")
        self.Model = params.get("Model")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.BackupTime = params.get("BackupTime")


class DBPrivilege(AbstractModel):
    """賬号的資料庫權限訊息

    """

    def __init__(self):
        """
        :param DBName: 資料庫名
        :type DBName: str
        :param Privilege: 資料庫權限，ReadWrite表示可讀寫，ReadOnly表示只讀
        :type Privilege: str
        """
        self.DBName = None
        self.Privilege = None


    def _deserialize(self, params):
        self.DBName = params.get("DBName")
        self.Privilege = params.get("Privilege")


class DBPrivilegeModifyInfo(AbstractModel):
    """資料庫權限變更訊息

    """

    def __init__(self):
        """
        :param DBName: 資料庫名
        :type DBName: str
        :param Privilege: 權限變更訊息。ReadWrite表示可讀寫，ReadOnly表示只讀，Delete表示删除賬号對該DB的權限
        :type Privilege: str
        """
        self.DBName = None
        self.Privilege = None


    def _deserialize(self, params):
        self.DBName = params.get("DBName")
        self.Privilege = params.get("Privilege")


class DBRemark(AbstractModel):
    """資料庫備注訊息

    """

    def __init__(self):
        """
        :param Name: 據庫名
        :type Name: str
        :param Remark: 備注訊息
        :type Remark: str
        """
        self.Name = None
        self.Remark = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")


class DbRollbackTimeInfo(AbstractModel):
    """資料庫可回檔時間範圍訊息

    """

    def __init__(self):
        """
        :param DBName: 資料庫名稱
        :type DBName: str
        :param StartTime: 可回檔開始時間
        :type StartTime: str
        :param EndTime: 可回檔結束時間
        :type EndTime: str
        """
        self.DBName = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.DBName = params.get("DBName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DealInfo(AbstractModel):
    """訂單訊息

    """

    def __init__(self):
        """
        :param DealName: 訂單名
        :type DealName: str
        :param Count: 商品數量
        :type Count: int
        :param FlowId: 關聯的流程 Id，可用于查詢流程執行狀态
        :type FlowId: int
        :param InstanceIdSet: 只有創建實例的訂單會填充該欄位，表示該訂單創建的實例的 ID。
        :type InstanceIdSet: list of str
        :param OwnerUin: 所屬賬号
        :type OwnerUin: str
        """
        self.DealName = None
        self.Count = None
        self.FlowId = None
        self.InstanceIdSet = None
        self.OwnerUin = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.Count = params.get("Count")
        self.FlowId = params.get("FlowId")
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.OwnerUin = params.get("OwnerUin")


class DeleteAccountRequest(AbstractModel):
    """DeleteAccount請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 資料庫實例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param UserNames: 實例用戶名數組
        :type UserNames: list of str
        """
        self.InstanceId = None
        self.UserNames = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserNames = params.get("UserNames")


class DeleteAccountResponse(AbstractModel):
    """DeleteAccount返回參數結構體

    """

    def __init__(self):
        """
        :param FlowId: 任務流id
        :type FlowId: int
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class DeleteDBRequest(AbstractModel):
    """DeleteDB請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，形如mssql-rljoi3bf
        :type InstanceId: str
        :param Names: 資料庫名數組
        :type Names: list of str
        """
        self.InstanceId = None
        self.Names = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Names = params.get("Names")


class DeleteDBResponse(AbstractModel):
    """DeleteDB返回參數結構體

    """

    def __init__(self):
        """
        :param FlowId: 任務流id
        :type FlowId: int
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class DeleteMigrationRequest(AbstractModel):
    """DeleteMigration請求參數結構體

    """

    def __init__(self):
        """
        :param MigrateId: 遷移任務ID
        :type MigrateId: int
        """
        self.MigrateId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")


class DeleteMigrationResponse(AbstractModel):
    """DeleteMigration返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param Limit: 分頁返回，每頁返回的數目，取值爲1-100，預設值爲20
        :type Limit: int
        :param Offset: 分頁返回，從第幾頁開始返回。從第0頁開始，預設第0頁
        :type Offset: int
        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param Accounts: 帳戶訊息清單
        :type Accounts: list of AccountDetail
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.Accounts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = AccountDetail()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBackupsRequest(AbstractModel):
    """DescribeBackups請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 開始時間(yyyy-MM-dd HH:mm:ss)
        :type StartTime: str
        :param EndTime: 結束時間(yyyy-MM-dd HH:mm:ss)
        :type EndTime: str
        :param InstanceId: 實例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param Limit: 分頁返回，每頁返回數量，預設爲20，最大值爲 100
        :type Limit: int
        :param Offset: 偏移量，預設爲 0
        :type Offset: int
        """
        self.StartTime = None
        self.EndTime = None
        self.InstanceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeBackupsResponse(AbstractModel):
    """DescribeBackups返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 備份總數量
        :type TotalCount: int
        :param Backups: 備份清單詳情
        :type Backups: list of Backup
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Backups = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Backups") is not None:
            self.Backups = []
            for item in params.get("Backups"):
                obj = Backup()
                obj._deserialize(item)
                self.Backups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: 項目ID
        :type ProjectId: int
        :param Status: 實例狀态。取值範圍：
<li>1：申請中</li>
<li>2：運作中</li>
<li>3：受限運作中 (主備切換中)</li>
<li>4：已隔離</li>
<li>5：回收中</li>
<li>6：已回收</li>
<li>7：任務執行中 (實例做備份、回檔等操作)</li>
<li>8：已下線</li>
<li>9：實例擴容中</li>
<li>10：實例遷移中</li>
<li>11：只讀</li>
<li>12：重啓中</li>
        :type Status: int
        :param Offset: 偏移量，預設爲 0
        :type Offset: int
        :param Limit: 返回數量，預設爲50
        :type Limit: int
        :param InstanceIdSet: 一個或者多個實例ID。實例ID，格式如：mssql-si2823jyl
        :type InstanceIdSet: list of str
        """
        self.ProjectId = None
        self.Status = None
        self.Offset = None
        self.Limit = None
        self.InstanceIdSet = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstanceIdSet = params.get("InstanceIdSet")


class DescribeDBInstancesResponse(AbstractModel):
    """DescribeDBInstances返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的實例總數。分頁返回的話，這個值指的是所有符合條件的實例的個數，而非當前根據Limit和Offset值返回的實例個數
        :type TotalCount: int
        :param DBInstances: 實例清單
        :type DBInstances: list of DBInstance
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DBInstances = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DBInstances") is not None:
            self.DBInstances = []
            for item in params.get("DBInstances"):
                obj = DBInstance()
                obj._deserialize(item)
                self.DBInstances.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBsRequest(AbstractModel):
    """DescribeDBs請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIdSet: 實例ID
        :type InstanceIdSet: list of str
        :param Limit: 每頁記錄數，最大爲100，預設20
        :type Limit: int
        :param Offset: 頁編号，從第0頁開始
        :type Offset: int
        """
        self.InstanceIdSet = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeDBsResponse(AbstractModel):
    """DescribeDBs返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 資料庫數量
        :type TotalCount: int
        :param DBInstances: 實例資料庫清單
        :type DBInstances: list of InstanceDBDetail
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DBInstances = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DBInstances") is not None:
            self.DBInstances = []
            for item in params.get("DBInstances"):
                obj = InstanceDBDetail()
                obj._deserialize(item)
                self.DBInstances.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFlowStatusRequest(AbstractModel):
    """DescribeFlowStatus請求參數結構體

    """

    def __init__(self):
        """
        :param FlowId: 流程ID
        :type FlowId: int
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")


class DescribeFlowStatusResponse(AbstractModel):
    """DescribeFlowStatus返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 流程狀态，0：成功，1：失敗，2：運作中
        :type Status: int
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeMigrationDetailRequest(AbstractModel):
    """DescribeMigrationDetail請求參數結構體

    """

    def __init__(self):
        """
        :param MigrateId: 遷移任務ID
        :type MigrateId: int
        """
        self.MigrateId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")


class DescribeMigrationDetailResponse(AbstractModel):
    """DescribeMigrationDetail返回參數結構體

    """

    def __init__(self):
        """
        :param MigrateId: 遷移任務ID
        :type MigrateId: int
        :param MigrateName: 遷移任務名稱
        :type MigrateName: str
        :param AppId: 遷移任務所屬的用戶ID
        :type AppId: int
        :param Region: 遷移任務所屬的地域
        :type Region: str
        :param SourceType: 遷移源的類型 1:CDB for SQLServer 2:雲伺服器自建SQLServer資料庫 4:SQLServer備份還原 5:SQLServer備份還原（COS方式）
        :type SourceType: int
        :param CreateTime: 遷移任務的創建時間
        :type CreateTime: str
        :param StartTime: 遷移任務的開始時間
        :type StartTime: str
        :param EndTime: 遷移任務的結束時間
        :type EndTime: str
        :param Status: 遷移任務的狀态（1:初始化,4:遷移中,5.遷移失敗,6.遷移成功）
        :type Status: int
        :param Progress: 遷移任務當前進度
        :type Progress: int
        :param MigrateType: 遷移類型（1:結構遷移 2:數據遷移 3:增量同步）
        :type MigrateType: int
        :param Source: 遷移源
        :type Source: :class:`tencentcloud.sqlserver.v20180328.models.MigrateSource`
        :param Target: 遷移目标
        :type Target: :class:`tencentcloud.sqlserver.v20180328.models.MigrateTarget`
        :param MigrateDBSet: 遷移DB對象 ，離線遷移（SourceType=4或SourceType=5）不使用。
        :type MigrateDBSet: list of MigrateDB
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.MigrateId = None
        self.MigrateName = None
        self.AppId = None
        self.Region = None
        self.SourceType = None
        self.CreateTime = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.Progress = None
        self.MigrateType = None
        self.Source = None
        self.Target = None
        self.MigrateDBSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")
        self.MigrateName = params.get("MigrateName")
        self.AppId = params.get("AppId")
        self.Region = params.get("Region")
        self.SourceType = params.get("SourceType")
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        self.Progress = params.get("Progress")
        self.MigrateType = params.get("MigrateType")
        if params.get("Source") is not None:
            self.Source = MigrateSource()
            self.Source._deserialize(params.get("Source"))
        if params.get("Target") is not None:
            self.Target = MigrateTarget()
            self.Target._deserialize(params.get("Target"))
        if params.get("MigrateDBSet") is not None:
            self.MigrateDBSet = []
            for item in params.get("MigrateDBSet"):
                obj = MigrateDB()
                obj._deserialize(item)
                self.MigrateDBSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMigrationsRequest(AbstractModel):
    """DescribeMigrations請求參數結構體

    """

    def __init__(self):
        """
        :param StatusSet: 狀态集合。只要符合集合中某一狀态的遷移任務，就會查出來
        :type StatusSet: list of int
        :param MigrateName: 遷移任務的名稱，模糊比對
        :type MigrateName: str
        :param Limit: 每頁的記錄數
        :type Limit: int
        :param Offset: 查詢第幾頁的記錄
        :type Offset: int
        :param OrderBy: 查詢結果按照關鍵字排序，可選值爲name、createTime、startTime，endTime，status
        :type OrderBy: str
        :param OrderByType: 排序方式，可選值爲desc、asc
        :type OrderByType: str
        """
        self.StatusSet = None
        self.MigrateName = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.StatusSet = params.get("StatusSet")
        self.MigrateName = params.get("MigrateName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")


class DescribeMigrationsResponse(AbstractModel):
    """DescribeMigrations返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 查詢結果的總數
        :type TotalCount: int
        :param MigrateTaskSet: 查詢結果的清單
        :type MigrateTaskSet: list of MigrateTask
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.MigrateTaskSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("MigrateTaskSet") is not None:
            self.MigrateTaskSet = []
            for item in params.get("MigrateTaskSet"):
                obj = MigrateTask()
                obj._deserialize(item)
                self.MigrateTaskSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOrdersRequest(AbstractModel):
    """DescribeOrders請求參數結構體

    """

    def __init__(self):
        """
        :param DealNames: 訂單數組。發貨時會返回訂單名字，利用該訂單名字調用DescribeOrders介面查詢發貨情況
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
        :param Deals: 訂單訊息數組
        :type Deals: list of DealInfo
        :param TotalCount: 返回多少個訂單的訊息
        :type TotalCount: int
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.Deals = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Deals") is not None:
            self.Deals = []
            for item in params.get("Deals"):
                obj = DealInfo()
                obj._deserialize(item)
                self.Deals.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeProductConfigRequest(AbstractModel):
    """DescribeProductConfig請求參數結構體

    """

    def __init__(self):
        """
        :param Zone: 可用區英文ID，形如ap-guangzhou-1
        :type Zone: str
        """
        self.Zone = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")


class DescribeProductConfigResponse(AbstractModel):
    """DescribeProductConfig返回參數結構體

    """

    def __init__(self):
        """
        :param SpecInfoList: 規格訊息數組
        :type SpecInfoList: list of SpecInfo
        :param TotalCount: 返回總共多少條數據
        :type TotalCount: int
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.SpecInfoList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SpecInfoList") is not None:
            self.SpecInfoList = []
            for item in params.get("SpecInfoList"):
                obj = SpecInfo()
                obj._deserialize(item)
                self.SpecInfoList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions請求參數結構體

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 返回地域訊息總的條目
        :type TotalCount: int
        :param RegionSet: 地域訊息數組
        :type RegionSet: list of RegionInfo
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RegionSet") is not None:
            self.RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.RegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRollbackTimeRequest(AbstractModel):
    """DescribeRollbackTime請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param DBs: 需要查詢的資料庫清單
        :type DBs: list of str
        """
        self.InstanceId = None
        self.DBs = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DBs = params.get("DBs")


class DescribeRollbackTimeResponse(AbstractModel):
    """DescribeRollbackTime返回參數結構體

    """

    def __init__(self):
        """
        :param Details: 資料庫可回檔實例訊息
        :type Details: list of DbRollbackTimeInfo
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.Details = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = DbRollbackTimeInfo()
                obj._deserialize(item)
                self.Details.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSlowlogsRequest(AbstractModel):
    """DescribeSlowlogs請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，形如mssql-k8voqdlz
        :type InstanceId: str
        :param StartTime: 查詢開始時間
        :type StartTime: str
        :param EndTime: 查詢結束時間
        :type EndTime: str
        :param Limit: 分頁返回結果，分頁大小，預設20，不超過100
        :type Limit: int
        :param Offset: 從第幾頁開始返回，起始頁，從0開始，預設爲0
        :type Offset: int
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeSlowlogsResponse(AbstractModel):
    """DescribeSlowlogs返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 查詢總數
        :type TotalCount: int
        :param Slowlogs: 慢查詢日志訊息清單
        :type Slowlogs: list of SlowlogInfo
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Slowlogs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Slowlogs") is not None:
            self.Slowlogs = []
            for item in params.get("Slowlogs"):
                obj = SlowlogInfo()
                obj._deserialize(item)
                self.Slowlogs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones請求參數結構體

    """


class DescribeZonesResponse(AbstractModel):
    """DescribeZones返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 返回多少個可用區訊息
        :type TotalCount: int
        :param ZoneSet: 可用區數組
        :type ZoneSet: list of ZoneInfo
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ZoneSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ZoneSet") is not None:
            self.ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self.ZoneSet.append(obj)
        self.RequestId = params.get("RequestId")


class InquiryPriceCreateDBInstancesRequest(AbstractModel):
    """InquiryPriceCreateDBInstances請求參數結構體

    """

    def __init__(self):
        """
        :param Zone: 可用區ID。該參數可以通過調用 DescribeZones 介面的返回值中的Zone欄位來獲取。
        :type Zone: str
        :param Memory: 内存大小，單位：GB
        :type Memory: int
        :param Storage: 實例容量大小，單位：GB。
        :type Storage: int
        :param InstanceChargeType: 計費類型，當前只支援預付費，即包年包月，取值爲PREPAID。預設值爲PREPAID
        :type InstanceChargeType: str
        :param Period: 購買時長，單位：月。取值爲1到48，預設爲1
        :type Period: int
        :param GoodsNum: 一次性購買的實例數量。取值1-100，預設取值爲1
        :type GoodsNum: int
        :param DBVersion: sqlserver版本，目前只支援：2008R2（SQL Server 2008 R2），2012SP3（SQL Server 2012），2016SP1（SQL Server 2016 SP1）兩種版本。預設爲2008R2版本
        :type DBVersion: str
        """
        self.Zone = None
        self.Memory = None
        self.Storage = None
        self.InstanceChargeType = None
        self.Period = None
        self.GoodsNum = None
        self.DBVersion = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.Period = params.get("Period")
        self.GoodsNum = params.get("GoodsNum")
        self.DBVersion = params.get("DBVersion")


class InquiryPriceCreateDBInstancesResponse(AbstractModel):
    """InquiryPriceCreateDBInstances返回參數結構體

    """

    def __init__(self):
        """
        :param OriginalPrice: 未打折前價格，其值除以100表示多少錢。比如10010表示100.10元
        :type OriginalPrice: int
        :param Price: 實際需要支付的價格，其值除以100表示多少錢。比如10010表示100.10元
        :type Price: int
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.OriginalPrice = None
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.Price = params.get("Price")
        self.RequestId = params.get("RequestId")


class InquiryPriceRenewDBInstanceRequest(AbstractModel):
    """InquiryPriceRenewDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param Period: 續約週期。按月續約最多48個月。預設查詢續約一個月的價格
        :type Period: int
        :param TimeUnit: 續約週期單位。month表示按月續約，當前只支援按月付費查詢價格
        :type TimeUnit: str
        """
        self.InstanceId = None
        self.Period = None
        self.TimeUnit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Period = params.get("Period")
        self.TimeUnit = params.get("TimeUnit")


class InquiryPriceRenewDBInstanceResponse(AbstractModel):
    """InquiryPriceRenewDBInstance返回參數結構體

    """

    def __init__(self):
        """
        :param OriginalPrice: 未打折的原價，其值除以100表示最終的價格。比如10094表示100.94元
        :type OriginalPrice: int
        :param Price: 實際需要支付價格，其值除以100表示最終的價格。比如10094表示100.94元
        :type Price: int
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.OriginalPrice = None
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.Price = params.get("Price")
        self.RequestId = params.get("RequestId")


class InquiryPriceUpgradeDBInstanceRequest(AbstractModel):
    """InquiryPriceUpgradeDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param Memory: 實例升級後的内存大小，單位GB，其值不能比當前實例内存小
        :type Memory: int
        :param Storage: 實例升級後的磁盤大小，單位GB，其值不能比當前實例磁盤小
        :type Storage: int
        """
        self.InstanceId = None
        self.Memory = None
        self.Storage = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")


class InquiryPriceUpgradeDBInstanceResponse(AbstractModel):
    """InquiryPriceUpgradeDBInstance返回參數結構體

    """

    def __init__(self):
        """
        :param OriginalPrice: 未打折的原價，其值除以100表示最終的價格。比如10094表示100.94元
        :type OriginalPrice: int
        :param Price: 實際需要支付價格，其值除以100表示最終的價格。比如10094表示100.94元
        :type Price: int
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.OriginalPrice = None
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.Price = params.get("Price")
        self.RequestId = params.get("RequestId")


class InstanceDBDetail(AbstractModel):
    """實例的資料庫訊息

    """

    def __init__(self):
        """
        :param InstanceId: 實例id
        :type InstanceId: str
        :param DBDetails: 資料庫訊息清單
        :type DBDetails: list of DBDetail
        """
        self.InstanceId = None
        self.DBDetails = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("DBDetails") is not None:
            self.DBDetails = []
            for item in params.get("DBDetails"):
                obj = DBDetail()
                obj._deserialize(item)
                self.DBDetails.append(obj)


class InstanceRenewInfo(AbstractModel):
    """實例續約狀态訊息

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，形如mssql-j8kv137v
        :type InstanceId: str
        :param RenewFlag: 實例續約标記。0：正常續約，1：自動續約，2：到期不續
        :type RenewFlag: int
        """
        self.InstanceId = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RenewFlag = params.get("RenewFlag")


class MigrateDB(AbstractModel):
    """需要遷移的DB清單

    """

    def __init__(self):
        """
        :param DBName: 遷移資料庫的名稱
        :type DBName: str
        """
        self.DBName = None


    def _deserialize(self, params):
        self.DBName = params.get("DBName")


class MigrateDetail(AbstractModel):
    """遷移的進度詳情類型

    """

    def __init__(self):
        """
        :param StepName: 當前環節的名稱
        :type StepName: str
        :param Progress: 當前環節的進度（單位是%）
        :type Progress: int
        """
        self.StepName = None
        self.Progress = None


    def _deserialize(self, params):
        self.StepName = params.get("StepName")
        self.Progress = params.get("Progress")


class MigrateSource(AbstractModel):
    """遷移任務的源類型

    """

    def __init__(self):
        """
        :param InstanceId: 遷移源實例的ID，MigrateType=1(CDB for SQLServers)時使用，格式如：mssql-si2823jyl
        :type InstanceId: str
        :param CvmId: 遷移源Cvm的ID，MigrateType=2(雲伺服器自建SQLServer資料庫)時使用
        :type CvmId: str
        :param VpcId: 遷移源Cvm的Vpc網絡标識，MigrateType=2(雲伺服器自建SQLServer資料庫)時使用，格式如：vpc-6ys9ont9
        :type VpcId: str
        :param SubnetId: 遷移源Cvm的Vpc下的子網标識，MigrateType=2(雲伺服器自建SQLServer資料庫)時使用，格式如：subnet-h9extioi
        :type SubnetId: str
        :param UserName: 用戶名，MigrateType=1或MigrateType=2使用
        :type UserName: str
        :param Password: 密碼，MigrateType=1或MigrateType=2使用
        :type Password: str
        :param Ip: 遷移源Cvm自建庫的内網IP，MigrateType=2(雲伺服器自建SQLServer資料庫)時使用
        :type Ip: str
        :param Port: 遷移源Cvm自建庫的端口号，MigrateType=2(雲伺服器自建SQLServer資料庫)時使用
        :type Port: int
        :param Url: 離線遷移的源備份網址，MigrateType=4或MigrateType=5使用
        :type Url: list of str
        :param UrlPassword: 離線遷移的源備份密碼，MigrateType=4或MigrateType=5使用
        :type UrlPassword: str
        """
        self.InstanceId = None
        self.CvmId = None
        self.VpcId = None
        self.SubnetId = None
        self.UserName = None
        self.Password = None
        self.Ip = None
        self.Port = None
        self.Url = None
        self.UrlPassword = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.CvmId = params.get("CvmId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.Url = params.get("Url")
        self.UrlPassword = params.get("UrlPassword")


class MigrateTarget(AbstractModel):
    """遷移任務的目标類型

    """

    def __init__(self):
        """
        :param InstanceId: 遷移目标實例的ID，格式如：mssql-si2823jyl
        :type InstanceId: str
        :param UserName: 遷移目标實例的用戶名
        :type UserName: str
        :param Password: 遷移目标實例的密碼
        :type Password: str
        """
        self.InstanceId = None
        self.UserName = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")


class MigrateTask(AbstractModel):
    """查詢遷移任務清單類型

    """

    def __init__(self):
        """
        :param MigrateId: 遷移任務ID
        :type MigrateId: int
        :param MigrateName: 遷移任務名稱
        :type MigrateName: str
        :param AppId: 遷移任務所屬的用戶ID
        :type AppId: int
        :param Region: 遷移任務所屬的地域
        :type Region: str
        :param SourceType: 遷移源的類型 1:CDB for SQLServer 2:雲伺服器自建SQLServer資料庫 4:SQLServer備份還原 5:SQLServer備份還原（COS方式）
        :type SourceType: int
        :param CreateTime: 遷移任務的創建時間
        :type CreateTime: str
        :param StartTime: 遷移任務的開始時間
        :type StartTime: str
        :param EndTime: 遷移任務的結束時間
        :type EndTime: str
        :param Status: 遷移任務的狀态（1:初始化,4:遷移中,5.遷移失敗,6.遷移成功）
        :type Status: int
        :param Message: 訊息
        :type Message: str
        :param CheckFlag: 是否遷移任務經過檢查（0:未校驗,1:校驗成功,2:校驗失敗,3:校驗中）
        :type CheckFlag: int
        :param Progress: 遷移任務當前進度（單位%）
        :type Progress: int
        :param MigrateDetail: 遷移任務進度細節
        :type MigrateDetail: :class:`tencentcloud.sqlserver.v20180328.models.MigrateDetail`
        """
        self.MigrateId = None
        self.MigrateName = None
        self.AppId = None
        self.Region = None
        self.SourceType = None
        self.CreateTime = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.Message = None
        self.CheckFlag = None
        self.Progress = None
        self.MigrateDetail = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")
        self.MigrateName = params.get("MigrateName")
        self.AppId = params.get("AppId")
        self.Region = params.get("Region")
        self.SourceType = params.get("SourceType")
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        self.Message = params.get("Message")
        self.CheckFlag = params.get("CheckFlag")
        self.Progress = params.get("Progress")
        if params.get("MigrateDetail") is not None:
            self.MigrateDetail = MigrateDetail()
            self.MigrateDetail._deserialize(params.get("MigrateDetail"))


class ModifyAccountPrivilegeRequest(AbstractModel):
    """ModifyAccountPrivilege請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 資料庫實例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param Accounts: 賬号權限變更訊息
        :type Accounts: list of AccountPrivilegeModifyInfo
        """
        self.InstanceId = None
        self.Accounts = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = AccountPrivilegeModifyInfo()
                obj._deserialize(item)
                self.Accounts.append(obj)


class ModifyAccountPrivilegeResponse(AbstractModel):
    """ModifyAccountPrivilege返回參數結構體

    """

    def __init__(self):
        """
        :param FlowId: 異步任務流程ID
        :type FlowId: int
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ModifyAccountRemarkRequest(AbstractModel):
    """ModifyAccountRemark請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，形如mssql-j8kv137v
        :type InstanceId: str
        :param Accounts: 修改備注的帳戶訊息
        :type Accounts: list of AccountRemark
        """
        self.InstanceId = None
        self.Accounts = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = AccountRemark()
                obj._deserialize(item)
                self.Accounts.append(obj)


class ModifyAccountRemarkResponse(AbstractModel):
    """ModifyAccountRemark返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceNameRequest(AbstractModel):
    """ModifyDBInstanceName請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 資料庫實例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param InstanceName: 新的資料庫實例名字
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
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceProjectRequest(AbstractModel):
    """ModifyDBInstanceProject請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIdSet: 實例ID數組，形如mssql-j8kv137v
        :type InstanceIdSet: list of str
        :param ProjectId: 項目ID，爲0的話表示預設項目
        :type ProjectId: int
        """
        self.InstanceIdSet = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.ProjectId = params.get("ProjectId")


class ModifyDBInstanceProjectResponse(AbstractModel):
    """ModifyDBInstanceProject返回參數結構體

    """

    def __init__(self):
        """
        :param Count: 修改成功的實例個數
        :type Count: int
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceRenewFlagRequest(AbstractModel):
    """ModifyDBInstanceRenewFlag請求參數結構體

    """

    def __init__(self):
        """
        :param RenewFlags: 實例續約狀态标記訊息
        :type RenewFlags: list of InstanceRenewInfo
        """
        self.RenewFlags = None


    def _deserialize(self, params):
        if params.get("RenewFlags") is not None:
            self.RenewFlags = []
            for item in params.get("RenewFlags"):
                obj = InstanceRenewInfo()
                obj._deserialize(item)
                self.RenewFlags.append(obj)


class ModifyDBInstanceRenewFlagResponse(AbstractModel):
    """ModifyDBInstanceRenewFlag返回參數結構體

    """

    def __init__(self):
        """
        :param Count: 修改成功的個數
        :type Count: int
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class ModifyDBNameRequest(AbstractModel):
    """ModifyDBName請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例id
        :type InstanceId: str
        :param OldDBName: 舊資料庫名
        :type OldDBName: str
        :param NewDBName: 新資料庫名
        :type NewDBName: str
        """
        self.InstanceId = None
        self.OldDBName = None
        self.NewDBName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.OldDBName = params.get("OldDBName")
        self.NewDBName = params.get("NewDBName")


class ModifyDBNameResponse(AbstractModel):
    """ModifyDBName返回參數結構體

    """

    def __init__(self):
        """
        :param FlowId: 任務流id
        :type FlowId: int
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ModifyDBRemarkRequest(AbstractModel):
    """ModifyDBRemark請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，形如mssql-rljoi3bf
        :type InstanceId: str
        :param DBRemarks: 資料庫名稱及備注數組，每個元素包含資料庫名和對應的備注
        :type DBRemarks: list of DBRemark
        """
        self.InstanceId = None
        self.DBRemarks = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("DBRemarks") is not None:
            self.DBRemarks = []
            for item in params.get("DBRemarks"):
                obj = DBRemark()
                obj._deserialize(item)
                self.DBRemarks.append(obj)


class ModifyDBRemarkResponse(AbstractModel):
    """ModifyDBRemark返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMigrationRequest(AbstractModel):
    """ModifyMigration請求參數結構體

    """

    def __init__(self):
        """
        :param MigrateId: 遷移任務ID
        :type MigrateId: int
        :param MigrateName: 新的遷移任務的名稱，若不填則不修改
        :type MigrateName: str
        :param MigrateType: 新的遷移類型（1:結構遷移 2:數據遷移 3:增量同步），若不填則不修改
        :type MigrateType: int
        :param SourceType: 遷移源的類型 1:CDB for SQLServer 2:雲伺服器自建SQLServer資料庫 4:SQLServer備份還原 5:SQLServer備份還原（COS方式），若不填則不修改
        :type SourceType: int
        :param Source: 遷移源，若不填則不修改
        :type Source: :class:`tencentcloud.sqlserver.v20180328.models.MigrateSource`
        :param Target: 遷移目标，若不填則不修改
        :type Target: :class:`tencentcloud.sqlserver.v20180328.models.MigrateTarget`
        :param MigrateDBSet: 遷移DB對象 ，離線遷移（SourceType=4或SourceType=5）不使用，若不填則不修改
        :type MigrateDBSet: list of MigrateDB
        """
        self.MigrateId = None
        self.MigrateName = None
        self.MigrateType = None
        self.SourceType = None
        self.Source = None
        self.Target = None
        self.MigrateDBSet = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")
        self.MigrateName = params.get("MigrateName")
        self.MigrateType = params.get("MigrateType")
        self.SourceType = params.get("SourceType")
        if params.get("Source") is not None:
            self.Source = MigrateSource()
            self.Source._deserialize(params.get("Source"))
        if params.get("Target") is not None:
            self.Target = MigrateTarget()
            self.Target._deserialize(params.get("Target"))
        if params.get("MigrateDBSet") is not None:
            self.MigrateDBSet = []
            for item in params.get("MigrateDBSet"):
                obj = MigrateDB()
                obj._deserialize(item)
                self.MigrateDBSet.append(obj)


class ModifyMigrationResponse(AbstractModel):
    """ModifyMigration返回參數結構體

    """

    def __init__(self):
        """
        :param MigrateId: 遷移任務ID
        :type MigrateId: int
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.MigrateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")
        self.RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """地域訊息

    """

    def __init__(self):
        """
        :param Region: 地域英文ID，類似ap-guanghou
        :type Region: str
        :param RegionName: 地域中文名稱
        :type RegionName: str
        :param RegionId: 地域數字ID
        :type RegionId: int
        :param RegionState: 該地域目前是否可以售賣，UNAVAILABLE-不可售賣；AVAILABLE-可售賣
        :type RegionState: str
        """
        self.Region = None
        self.RegionName = None
        self.RegionId = None
        self.RegionState = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionId = params.get("RegionId")
        self.RegionState = params.get("RegionState")


class RenewDBInstanceRequest(AbstractModel):
    """RenewDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，形如mssql-j8kv137v
        :type InstanceId: str
        :param Period: 續約多少個月，取值範圍爲1-48，預設爲1
        :type Period: int
        :param AutoVoucher: 是否自動使用代金券，0-不使用；1-使用；預設不實用
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID數組，目前只支援使用1張代金券
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
        :param DealName: 訂單名稱
        :type DealName: str
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
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
        :param InstanceId: 資料庫實例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        :param Accounts: 更新後的帳戶密碼訊息數組
        :type Accounts: list of AccountPassword
        """
        self.InstanceId = None
        self.Accounts = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = AccountPassword()
                obj._deserialize(item)
                self.Accounts.append(obj)


class ResetAccountPasswordResponse(AbstractModel):
    """ResetAccountPassword返回參數結構體

    """

    def __init__(self):
        """
        :param FlowId: 修改帳号密碼的異步任務流程ID
        :type FlowId: int
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class RestartDBInstanceRequest(AbstractModel):
    """RestartDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 資料庫實例ID，形如mssql-njj2mtpl
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class RestartDBInstanceResponse(AbstractModel):
    """RestartDBInstance返回參數結構體

    """

    def __init__(self):
        """
        :param FlowId: 異步任務流程ID
        :type FlowId: int
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class RestoreInstanceRequest(AbstractModel):
    """RestoreInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，形如mssql-j8kv137v
        :type InstanceId: str
        :param BackupId: 備份文件ID，該ID可以通過DescribeBackups介面返回數據中的Id欄位獲得
        :type BackupId: int
        """
        self.InstanceId = None
        self.BackupId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupId = params.get("BackupId")


class RestoreInstanceResponse(AbstractModel):
    """RestoreInstance返回參數結構體

    """

    def __init__(self):
        """
        :param FlowId: 異步流程任務ID，使用FlowId調用DescribeFlowStatus介面獲取任務執行狀态
        :type FlowId: int
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class RollbackInstanceRequest(AbstractModel):
    """RollbackInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param Type: 回檔類型，0-回檔的資料庫函蓋原庫；1-回檔的資料庫以重命名的形式生成，不函蓋原庫
        :type Type: int
        :param DBs: 需要回檔的資料庫
        :type DBs: list of str
        :param Time: 回檔目标時間點
        :type Time: str
        """
        self.InstanceId = None
        self.Type = None
        self.DBs = None
        self.Time = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Type = params.get("Type")
        self.DBs = params.get("DBs")
        self.Time = params.get("Time")


class RollbackInstanceResponse(AbstractModel):
    """RollbackInstance返回參數結構體

    """

    def __init__(self):
        """
        :param FlowId: 異步任務ID
        :type FlowId: int
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class RunMigrationRequest(AbstractModel):
    """RunMigration請求參數結構體

    """

    def __init__(self):
        """
        :param MigrateId: 遷移任務ID
        :type MigrateId: int
        """
        self.MigrateId = None


    def _deserialize(self, params):
        self.MigrateId = params.get("MigrateId")


class RunMigrationResponse(AbstractModel):
    """RunMigration返回參數結構體

    """

    def __init__(self):
        """
        :param FlowId: 遷移流程啓動後，返回流程ID
        :type FlowId: int
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class SlowlogInfo(AbstractModel):
    """慢查詢日志文件訊息

    """

    def __init__(self):
        """
        :param Id: 慢查詢日志文件唯一标識
        :type Id: int
        :param StartTime: 文件生成的開始時間
        :type StartTime: str
        :param EndTime: 文件生成的結束時間
        :type EndTime: str
        :param Size: 文件大小（KB）
        :type Size: int
        :param Count: 文件中log條數
        :type Count: int
        :param InternalAddr: 内網下載網址
        :type InternalAddr: str
        :param ExternalAddr: 外網下載網址
        :type ExternalAddr: str
        """
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.Size = None
        self.Count = None
        self.InternalAddr = None
        self.ExternalAddr = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Size = params.get("Size")
        self.Count = params.get("Count")
        self.InternalAddr = params.get("InternalAddr")
        self.ExternalAddr = params.get("ExternalAddr")


class SpecInfo(AbstractModel):
    """實例可售賣的規格訊息

    """

    def __init__(self):
        """
        :param SpecId: 實例規格ID，利用DescribeZones返回的SpecId，結合DescribeProductConfig返回的可售賣規格訊息，可獲悉某個可用區下可購買什麽規格的實例
        :type SpecId: int
        :param MachineType: 機型ID
        :type MachineType: str
        :param MachineTypeName: 機型中文名稱
        :type MachineTypeName: str
        :param Version: 資料庫版本訊息。取值爲2008R2（表示SQL Server 2008 R2），2012SP3（表示SQL Server 2012），2016SP1（表示SQL Server 2016 SP1）
        :type Version: str
        :param VersionName: Version欄位對應的版本名稱
        :type VersionName: str
        :param Memory: 内存大小，單位GB
        :type Memory: int
        :param CPU: CPU核數
        :type CPU: int
        :param MinStorage: 此規格下最小的磁盤大小，單位GB
        :type MinStorage: int
        :param MaxStorage: 此規格下最大的磁盤大小，單位GB
        :type MaxStorage: int
        :param QPS: 此規格對應的QPS大小
        :type QPS: int
        :param SuitInfo: 此規格的中文描述訊息
        :type SuitInfo: str
        :param Pid: 此規格對應的Pid
        :type Pid: int
        """
        self.SpecId = None
        self.MachineType = None
        self.MachineTypeName = None
        self.Version = None
        self.VersionName = None
        self.Memory = None
        self.CPU = None
        self.MinStorage = None
        self.MaxStorage = None
        self.QPS = None
        self.SuitInfo = None
        self.Pid = None


    def _deserialize(self, params):
        self.SpecId = params.get("SpecId")
        self.MachineType = params.get("MachineType")
        self.MachineTypeName = params.get("MachineTypeName")
        self.Version = params.get("Version")
        self.VersionName = params.get("VersionName")
        self.Memory = params.get("Memory")
        self.CPU = params.get("CPU")
        self.MinStorage = params.get("MinStorage")
        self.MaxStorage = params.get("MaxStorage")
        self.QPS = params.get("QPS")
        self.SuitInfo = params.get("SuitInfo")
        self.Pid = params.get("Pid")


class UpgradeDBInstanceRequest(AbstractModel):
    """UpgradeDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，形如mssql-j8kv137v
        :type InstanceId: str
        :param Memory: 實例升級後内存大小，單位GB，其值不能小於當前實例内存大小
        :type Memory: int
        :param Storage: 實例升級後磁盤大小，單位GB，其值不能小於當前實例磁盤大小
        :type Storage: int
        :param AutoVoucher: 是否自動使用代金券，0 - 不使用；1 - 預設使用。取值預設爲0
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID，目前單個訂單只能使用一張代金券
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
        :param DealName: 訂單名稱
        :type DealName: str
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class ZoneInfo(AbstractModel):
    """可用區訊息

    """

    def __init__(self):
        """
        :param Zone: 可用區英文ID，形如ap-guangzhou-1，表示廣州一區
        :type Zone: str
        :param ZoneName: 可用區中文名稱
        :type ZoneName: str
        :param ZoneId: 可用區數字ID
        :type ZoneId: int
        :param SpecId: 該可用區目前可售賣的規格ID，利用SpecId，結合介面DescribeProductConfig返回的數據，可獲悉該可用區目前可售賣的規格大小
        :type SpecId: int
        :param Version: 當前可用區與規格下，可售賣的資料庫版本，形如2008R2（表示SQL Server 2008 R2）。其可選值有2008R2（表示SQL Server 2008 R2），2012SP3（表示SQL Server 2012），2016SP1（表示SQL Server 2016 SP1）
        :type Version: str
        """
        self.Zone = None
        self.ZoneName = None
        self.ZoneId = None
        self.SpecId = None
        self.Version = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneName = params.get("ZoneName")
        self.ZoneId = params.get("ZoneId")
        self.SpecId = params.get("SpecId")
        self.Version = params.get("Version")