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


class Account(AbstractModel):
    """資料庫賬号訊息

    """

    def __init__(self):
        """
        :param User: 新帳戶的名稱
        :type User: str
        :param Host: 新帳戶的域名
        :type Host: str
        """
        self.User = None
        self.Host = None


    def _deserialize(self, params):
        self.User = params.get("User")
        self.Host = params.get("Host")


class AccountInfo(AbstractModel):
    """賬号詳細訊息

    """

    def __init__(self):
        """
        :param Notes: 賬号備注訊息
        :type Notes: str
        :param Host: 賬号的域名
        :type Host: str
        :param User: 賬号的名稱
        :type User: str
        :param ModifyTime: 賬号訊息修改時間
        :type ModifyTime: str
        :param ModifyPasswordTime: 修改密碼的時間
        :type ModifyPasswordTime: str
        :param CreateTime: 賬号的創建時間
        :type CreateTime: str
        """
        self.Notes = None
        self.Host = None
        self.User = None
        self.ModifyTime = None
        self.ModifyPasswordTime = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.Notes = params.get("Notes")
        self.Host = params.get("Host")
        self.User = params.get("User")
        self.ModifyTime = params.get("ModifyTime")
        self.ModifyPasswordTime = params.get("ModifyPasswordTime")
        self.CreateTime = params.get("CreateTime")


class AddTimeWindowRequest(AbstractModel):
    """AddTimeWindow請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        :param Monday: 星期一的可維護時間段，其中每一個時間段的格式形如：10:00-12:00；起始時間按半個小時對齊；最短半個小時，最長三個小時；最多設置兩個時間段；下同。
        :type Monday: list of str
        :param Tuesday: 星期二的可維護時間視窗。
        :type Tuesday: list of str
        :param Wednesday: 星期三的可維護時間視窗。
        :type Wednesday: list of str
        :param Thursday: 星期四的可維護時間視窗。
        :type Thursday: list of str
        :param Friday: 星期五的可維護時間視窗。
        :type Friday: list of str
        :param Saturday: 星期六的可維護時間視窗。
        :type Saturday: list of str
        :param Sunday: 星期日的可維護時間視窗。
        :type Sunday: list of str
        """
        self.InstanceId = None
        self.Monday = None
        self.Tuesday = None
        self.Wednesday = None
        self.Thursday = None
        self.Friday = None
        self.Saturday = None
        self.Sunday = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Monday = params.get("Monday")
        self.Tuesday = params.get("Tuesday")
        self.Wednesday = params.get("Wednesday")
        self.Thursday = params.get("Thursday")
        self.Friday = params.get("Friday")
        self.Saturday = params.get("Saturday")
        self.Sunday = params.get("Sunday")


class AddTimeWindowResponse(AbstractModel):
    """AddTimeWindow返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups請求參數結構體

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全組Id。
        :type SecurityGroupId: str
        :param InstanceIds: 實例ID清單，一個或者多個實例Id組成的數組。
        :type InstanceIds: list of str
        """
        self.SecurityGroupId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.InstanceIds = params.get("InstanceIds")


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BackupConfig(AbstractModel):
    """ECDB第二個從庫的配置訊息，只有ECDB實例才有這個欄位

    """

    def __init__(self):
        """
        :param ReplicationMode: 第二個從庫複制方式，可能的返回值：async-異步，semisync-半同步
        :type ReplicationMode: str
        :param Zone: 第二個從庫可用區的正式名稱，如ap-shanghai-1
        :type Zone: str
        :param Vip: 第二個從庫内網IP網址
        :type Vip: str
        :param Vport: 第二個從庫訪問端口
        :type Vport: int
        """
        self.ReplicationMode = None
        self.Zone = None
        self.Vip = None
        self.Vport = None


    def _deserialize(self, params):
        self.ReplicationMode = params.get("ReplicationMode")
        self.Zone = params.get("Zone")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")


class BackupInfo(AbstractModel):
    """備份詳細訊息

    """

    def __init__(self):
        """
        :param Name: 備份文件名
        :type Name: str
        :param Size: 備份文件大小，單位：Byte
        :type Size: int
        :param Date: 備份快照時間，時間格式：2016-03-17 02:10:37
        :type Date: str
        :param IntranetUrl: 内網下載網址
        :type IntranetUrl: str
        :param InternetUrl: 外網下載網址
        :type InternetUrl: str
        :param Type: 日志具體類型，可能的值有：logic - 邏輯冷備，physical - 物理冷備
        :type Type: str
        :param BackupId: 備份子任務的ID，删除備份文件時使用
        :type BackupId: int
        :param Status: 備份任務狀态
        :type Status: str
        :param FinishTime: 備份任務的完成時間
        :type FinishTime: str
        :param Creator: 備份的創建者，可能的值：SYSTEM - 系統創建，Uin - 發起者Uin值
        :type Creator: str
        """
        self.Name = None
        self.Size = None
        self.Date = None
        self.IntranetUrl = None
        self.InternetUrl = None
        self.Type = None
        self.BackupId = None
        self.Status = None
        self.FinishTime = None
        self.Creator = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Size = params.get("Size")
        self.Date = params.get("Date")
        self.IntranetUrl = params.get("IntranetUrl")
        self.InternetUrl = params.get("InternetUrl")
        self.Type = params.get("Type")
        self.BackupId = params.get("BackupId")
        self.Status = params.get("Status")
        self.FinishTime = params.get("FinishTime")
        self.Creator = params.get("Creator")


class BackupItem(AbstractModel):
    """創建備份時，指定需要備份的庫表訊息

    """

    def __init__(self):
        """
        :param Db: 需要備份的庫名
        :type Db: str
        :param Table: 需要備份的表名。 如果傳該參數，表示備份該庫中的指定表。如果不傳該參數則備份該db庫
        :type Table: str
        """
        self.Db = None
        self.Table = None


    def _deserialize(self, params):
        self.Db = params.get("Db")
        self.Table = params.get("Table")


class BinlogInfo(AbstractModel):
    """二進制日志訊息

    """

    def __init__(self):
        """
        :param Name: 備份文件名
        :type Name: str
        :param Size: 備份文件大小，單位：Byte
        :type Size: int
        :param Date: 備份快照時間，時間格式：2016-03-17 02:10:37
        :type Date: str
        :param IntranetUrl: 内網下載網址
        :type IntranetUrl: str
        :param InternetUrl: 外網下載網址
        :type InternetUrl: str
        :param Type: 日志具體類型，可能的值有：binlog - 二進制日志
        :type Type: str
        """
        self.Name = None
        self.Size = None
        self.Date = None
        self.IntranetUrl = None
        self.InternetUrl = None
        self.Type = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Size = params.get("Size")
        self.Date = params.get("Date")
        self.IntranetUrl = params.get("IntranetUrl")
        self.InternetUrl = params.get("InternetUrl")
        self.Type = params.get("Type")


class CloseWanServiceRequest(AbstractModel):
    """CloseWanService請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同，可使用[查詢實例清單](https://cloud.taifucloud.com/document/api/236/15872) 介面獲取，其值爲輸出參數中欄位 InstanceId 的值。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class CloseWanServiceResponse(AbstractModel):
    """CloseWanService返回參數結構體

    """

    def __init__(self):
        """
        :param AsyncRequestId: 異步任務的請求ID，可使用此ID查詢異步任務的執行結果。
        :type AsyncRequestId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ColumnPrivilege(AbstractModel):
    """列權限訊息

    """

    def __init__(self):
        """
        :param Database: 資料庫名
        :type Database: str
        :param Table: 資料庫表名
        :type Table: str
        :param Column: 資料庫列名
        :type Column: str
        :param Privileges: 權限訊息
        :type Privileges: list of str
        """
        self.Database = None
        self.Table = None
        self.Column = None
        self.Privileges = None


    def _deserialize(self, params):
        self.Database = params.get("Database")
        self.Table = params.get("Table")
        self.Column = params.get("Column")
        self.Privileges = params.get("Privileges")


class CreateAccountsRequest(AbstractModel):
    """CreateAccounts請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        :param Accounts: 雲資料庫賬号。
        :type Accounts: list of Account
        :param Password: 新帳戶的密碼。
        :type Password: str
        :param Description: 備注訊息。
        :type Description: str
        """
        self.InstanceId = None
        self.Accounts = None
        self.Password = None
        self.Description = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.Password = params.get("Password")
        self.Description = params.get("Description")


class CreateAccountsResponse(AbstractModel):
    """CreateAccounts返回參數結構體

    """

    def __init__(self):
        """
        :param AsyncRequestId: 異步任務的請求ID，可使用此ID查詢異步任務的執行結果。
        :type AsyncRequestId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class CreateBackupRequest(AbstractModel):
    """CreateBackup請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv。與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        :param BackupMethod: 目标備份方法，可選的值：logical - 邏輯冷備，physical - 物理冷備。
        :type BackupMethod: str
        :param BackupDBTableList: 需要備份的庫表訊息，如果不設置該參數，則預設整實例備份。在 BackupMethod=logical 邏輯備份中才可設置該參數。指定的庫表必須存在，否則可能導緻備份失敗。
例：如果需要備份 db1 庫的 tb1、tb2表 和 db2 庫。則該參數設置爲 [{"Db": "db1", "Table": "tb1"}, {"Db": "db1", "Table": "tb2"}, {"Db": "db2"} ]
        :type BackupDBTableList: list of BackupItem
        """
        self.InstanceId = None
        self.BackupMethod = None
        self.BackupDBTableList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupMethod = params.get("BackupMethod")
        if params.get("BackupDBTableList") is not None:
            self.BackupDBTableList = []
            for item in params.get("BackupDBTableList"):
                obj = BackupItem()
                obj._deserialize(item)
                self.BackupDBTableList.append(obj)


class CreateBackupResponse(AbstractModel):
    """CreateBackup返回參數結構體

    """

    def __init__(self):
        """
        :param BackupId: 備份任務ID。
        :type BackupId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.BackupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BackupId = params.get("BackupId")
        self.RequestId = params.get("RequestId")


class CreateDBImportJobRequest(AbstractModel):
    """CreateDBImportJob請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例的ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        :param FileName: 文件名稱。該文件是指用戶已上傳到Top Cloud 的文件。
        :type FileName: str
        :param User: 雲資料庫的用戶名。
        :type User: str
        :param Password: 雲資料庫實例User賬号的密碼。
        :type Password: str
        :param DbName: 導入的目标資料庫名，不傳表示不指定資料庫。
        :type DbName: str
        """
        self.InstanceId = None
        self.FileName = None
        self.User = None
        self.Password = None
        self.DbName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.FileName = params.get("FileName")
        self.User = params.get("User")
        self.Password = params.get("Password")
        self.DbName = params.get("DbName")


class CreateDBImportJobResponse(AbstractModel):
    """CreateDBImportJob返回參數結構體

    """

    def __init__(self):
        """
        :param AsyncRequestId: 異步任務的請求ID，可使用此ID查詢異步任務的執行結果
        :type AsyncRequestId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class CreateDBInstanceHourRequest(AbstractModel):
    """CreateDBInstanceHour請求參數結構體

    """

    def __init__(self):
        """
        :param GoodsNum: 實例數量，預設值爲1, 最小值1，最大值爲100
        :type GoodsNum: int
        :param Memory: 實例内存大小，單位：MB，請使用[獲取雲資料庫可售賣規格](https://cloud.taifucloud.com/document/api/236/17229)介面獲取可創建的内存規格
        :type Memory: int
        :param Volume: 實例硬碟大小，單位：GB，請使用[獲取雲資料庫可售賣規格](https://cloud.taifucloud.com/document/api/236/17229)介面獲取可創建的硬碟範圍
        :type Volume: int
        :param EngineVersion: MySQL版本，值包括：5.5、5.6和5.7，請使用[獲取雲資料庫可售賣規格](https://cloud.taifucloud.com/document/api/236/17229)介面獲取可創建的實例版本
        :type EngineVersion: str
        :param UniqVpcId: 私有網絡ID，如果不傳則預設選擇基礎網絡，請使用[查詢私有網絡清單](/document/api/215/15778)
        :type UniqVpcId: str
        :param UniqSubnetId: 私有網絡下的子網ID，如果設置了 UniqVpcId，則 UniqSubnetId 必填，請使用[查詢子網清單](/document/api/215/15784)
        :type UniqSubnetId: str
        :param ProjectId: 項目ID，不填爲預設項目。請使用[查詢項目清單](https://cloud.taifucloud.com/document/product/378/4400)介面獲取項目ID
        :type ProjectId: int
        :param Zone: 可用區訊息，該參數缺省時，系統會自動選擇一個可用區，請使用[獲取雲資料庫可售賣規格](https://cloud.taifucloud.com/document/api/236/17229)介面獲取可創建的可用區
        :type Zone: str
        :param MasterInstanceId: 實例ID，購買只讀實例或者災備實例時必填，該欄位表示只讀實例或者災備實例的主實例ID，請使用[查詢實例清單](https://cloud.taifucloud.com/document/api/236/15872)介面查詢雲資料庫實例ID
        :type MasterInstanceId: str
        :param InstanceRole: 實例類型，預設爲 master，支援值包括：master-表示主實例，dr-表示災備實例，ro-表示只讀實例
        :type InstanceRole: str
        :param MasterRegion: 主實例的可用區訊息，購買災備實例時必填
        :type MasterRegion: str
        :param Port: 自定義端口，端口支援範圍：[ 1024-65535 ]
        :type Port: int
        :param Password: 設置root帳号密碼，密碼規則：8-64個字元，至少包含字母、數字、字元（支援的字元：_+-&=!@#$%^*()）中的兩種，購買主實例時可指定該參數，購買只讀實例或者災備實例時指定該參數無意義
        :type Password: str
        :param ParamList: 參數清單，參數格式如ParamList.0.Name=auto_increment&ParamList.0.Value=1。可通過[查詢預設的可設置參數清單](https://cloud.taifucloud.com/document/api/236/32662)查詢支援設置的參數
        :type ParamList: list of ParamInfo
        :param ProtectMode: 數據複制方式，預設爲0，支援值包括：0-表示異步複制，1-表示半同步複制，2-表示強同步複制，購買主實例時可指定該參數，購買只讀實例或者災備實例時指定該參數無意義
        :type ProtectMode: int
        :param DeployMode: 多可用區域，預設爲0，支援值包括：0-表示單可用區，1-表示多可用區，購買主實例時可指定該參數，購買只讀實例或者災備實例時指定該參數無意義
        :type DeployMode: int
        :param SlaveZone: 備庫1的可用區ID，預設爲zoneId的值，購買主實例時可指定該參數，購買只讀實例或者災備實例時指定該參數無意義
        :type SlaveZone: str
        :param BackupZone: 備庫2的可用區ID，預設爲0，購買主實例時可指定該參數，購買只讀實例或者災備實例時指定該參數無意義
        :type BackupZone: str
        :param SecurityGroup: 安全組參數，可使用[查詢項目安全組訊息](https://cloud.taifucloud.com/document/api/236/15850)介面查詢某個項目的安全組詳情
        :type SecurityGroup: list of str
        :param RoGroup: 只讀實例訊息
        :type RoGroup: :class:`taifucloudcloud.cdb.v20170320.models.RoGroup`
        :param AutoRenewFlag: 自動續約标記，值爲0或1。購買按量計費實例該欄位無意義
        :type AutoRenewFlag: int
        :param InstanceName: 實例名稱
        :type InstanceName: str
        :param ResourceTags: 實例标簽
        :type ResourceTags: list of TagInfo
        """
        self.GoodsNum = None
        self.Memory = None
        self.Volume = None
        self.EngineVersion = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.ProjectId = None
        self.Zone = None
        self.MasterInstanceId = None
        self.InstanceRole = None
        self.MasterRegion = None
        self.Port = None
        self.Password = None
        self.ParamList = None
        self.ProtectMode = None
        self.DeployMode = None
        self.SlaveZone = None
        self.BackupZone = None
        self.SecurityGroup = None
        self.RoGroup = None
        self.AutoRenewFlag = None
        self.InstanceName = None
        self.ResourceTags = None


    def _deserialize(self, params):
        self.GoodsNum = params.get("GoodsNum")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.EngineVersion = params.get("EngineVersion")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.ProjectId = params.get("ProjectId")
        self.Zone = params.get("Zone")
        self.MasterInstanceId = params.get("MasterInstanceId")
        self.InstanceRole = params.get("InstanceRole")
        self.MasterRegion = params.get("MasterRegion")
        self.Port = params.get("Port")
        self.Password = params.get("Password")
        if params.get("ParamList") is not None:
            self.ParamList = []
            for item in params.get("ParamList"):
                obj = ParamInfo()
                obj._deserialize(item)
                self.ParamList.append(obj)
        self.ProtectMode = params.get("ProtectMode")
        self.DeployMode = params.get("DeployMode")
        self.SlaveZone = params.get("SlaveZone")
        self.BackupZone = params.get("BackupZone")
        self.SecurityGroup = params.get("SecurityGroup")
        if params.get("RoGroup") is not None:
            self.RoGroup = RoGroup()
            self.RoGroup._deserialize(params.get("RoGroup"))
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.InstanceName = params.get("InstanceName")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.ResourceTags.append(obj)


class CreateDBInstanceHourResponse(AbstractModel):
    """CreateDBInstanceHour返回參數結構體

    """

    def __init__(self):
        """
        :param DealIds: 短訂單ID
        :type DealIds: list of str
        :param InstanceIds: 實例ID清單
        :type InstanceIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DealIds = None
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealIds = params.get("DealIds")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class CreateDBInstanceRequest(AbstractModel):
    """CreateDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param Memory: 實例内存大小，單位：MB，請使用[獲取雲資料庫可售賣規格](https://cloud.taifucloud.com/document/api/236/17229)介面獲取可創建的内存規格
        :type Memory: int
        :param Volume: 實例硬碟大小，單位：GB，請使用[獲取雲資料庫可售賣規格](https://cloud.taifucloud.com/document/api/236/17229)介面獲取可創建的硬碟範圍
        :type Volume: int
        :param Period: 實例時長，單位：月，可選值包括[1,2,3,4,5,6,7,8,9,10,11,12,24,36]
        :type Period: int
        :param GoodsNum: 實例數量，預設值爲1, 最小值1，最大值爲100
        :type GoodsNum: int
        :param Zone: 可用區訊息，該參數缺省時，系統會自動選擇一個可用區，請使用[獲取雲資料庫可售賣規格](https://cloud.taifucloud.com/document/api/236/17229)介面獲取可創建的可用區
        :type Zone: str
        :param UniqVpcId: 私有網絡ID，如果不傳則預設選擇基礎網絡，請使用[查詢私有網絡清單](/document/api/215/15778)
        :type UniqVpcId: str
        :param UniqSubnetId: 私有網絡下的子網ID，如果設置了 UniqVpcId，則 UniqSubnetId 必填，請使用[查詢子網清單](/document/api/215/15784)
        :type UniqSubnetId: str
        :param ProjectId: 項目ID，不填爲預設項目。請使用[查詢項目清單](https://cloud.taifucloud.com/document/product/378/4400)介面獲取項目ID
        :type ProjectId: int
        :param Port: 自定義端口，端口支援範圍：[ 1024-65535 ]
        :type Port: int
        :param InstanceRole: 實例類型，預設爲 master，支援值包括：master-表示主實例，dr-表示災備實例，ro-表示只讀實例
        :type InstanceRole: str
        :param MasterInstanceId: 實例ID，購買只讀實例時必填，該欄位表示只讀實例的主實例ID，請使用[查詢實例清單](https://cloud.taifucloud.com/document/api/236/15872)介面查詢雲資料庫實例ID
        :type MasterInstanceId: str
        :param EngineVersion: MySQL版本，值包括：5.5、5.6和5.7，請使用[獲取雲資料庫可售賣規格](https://cloud.taifucloud.com/document/api/236/17229)介面獲取可創建的實例版本
        :type EngineVersion: str
        :param Password: 設置root帳号密碼，密碼規則：8-64個字元，至少包含字母、數字、字元（支援的字元：_+-&=!@#$%^*()）中的兩種，購買主實例時可指定該參數，購買只讀實例或者災備實例時指定該參數無意義
        :type Password: str
        :param ProtectMode: 數據複制方式，預設爲0，支援值包括：0-表示異步複制，1-表示半同步複制，2-表示強同步複制
        :type ProtectMode: int
        :param DeployMode: 多可用區域，預設爲0，支援值包括：0-表示單可用區，1-表示多可用區
        :type DeployMode: int
        :param SlaveZone: 備庫1的可用區訊息，預設爲zone的值
        :type SlaveZone: str
        :param ParamList: 參數清單，參數格式如ParamList.0.Name=auto_increment&ParamList.0.Value=1。可通過[查詢預設的可設置參數清單](https://cloud.taifucloud.com/document/api/236/32662)查詢支援設置的參數
        :type ParamList: list of ParamInfo
        :param BackupZone: 備庫2的可用區ID，預設爲0，購買主實例時可指定該參數，購買只讀實例或者災備實例時指定該參數無意義
        :type BackupZone: str
        :param AutoRenewFlag: 自動續約标記，可選值爲：0-不自動續約；1-自動續約
        :type AutoRenewFlag: int
        :param MasterRegion: 主實例地域訊息，購買災備實例時，該欄位必填
        :type MasterRegion: str
        :param SecurityGroup: 安全組參數，可使用[查詢項目安全組訊息](https://cloud.taifucloud.com/document/api/236/15850)介面查詢某個項目的安全組詳情
        :type SecurityGroup: list of str
        :param RoGroup: 只讀實例參數
        :type RoGroup: :class:`taifucloudcloud.cdb.v20170320.models.RoGroup`
        :param InstanceName: 實例名稱
        :type InstanceName: str
        :param ResourceTags: 實例要綁定的标簽
        :type ResourceTags: list of TagInfo
        """
        self.Memory = None
        self.Volume = None
        self.Period = None
        self.GoodsNum = None
        self.Zone = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.ProjectId = None
        self.Port = None
        self.InstanceRole = None
        self.MasterInstanceId = None
        self.EngineVersion = None
        self.Password = None
        self.ProtectMode = None
        self.DeployMode = None
        self.SlaveZone = None
        self.ParamList = None
        self.BackupZone = None
        self.AutoRenewFlag = None
        self.MasterRegion = None
        self.SecurityGroup = None
        self.RoGroup = None
        self.InstanceName = None
        self.ResourceTags = None


    def _deserialize(self, params):
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.Period = params.get("Period")
        self.GoodsNum = params.get("GoodsNum")
        self.Zone = params.get("Zone")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.ProjectId = params.get("ProjectId")
        self.Port = params.get("Port")
        self.InstanceRole = params.get("InstanceRole")
        self.MasterInstanceId = params.get("MasterInstanceId")
        self.EngineVersion = params.get("EngineVersion")
        self.Password = params.get("Password")
        self.ProtectMode = params.get("ProtectMode")
        self.DeployMode = params.get("DeployMode")
        self.SlaveZone = params.get("SlaveZone")
        if params.get("ParamList") is not None:
            self.ParamList = []
            for item in params.get("ParamList"):
                obj = ParamInfo()
                obj._deserialize(item)
                self.ParamList.append(obj)
        self.BackupZone = params.get("BackupZone")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.MasterRegion = params.get("MasterRegion")
        self.SecurityGroup = params.get("SecurityGroup")
        if params.get("RoGroup") is not None:
            self.RoGroup = RoGroup()
            self.RoGroup._deserialize(params.get("RoGroup"))
        self.InstanceName = params.get("InstanceName")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.ResourceTags.append(obj)


class CreateDBInstanceResponse(AbstractModel):
    """CreateDBInstance返回參數結構體

    """

    def __init__(self):
        """
        :param DealIds: 短訂單ID
        :type DealIds: list of str
        :param InstanceIds: 實例ID清單
        :type InstanceIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DealIds = None
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealIds = params.get("DealIds")
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class CreateParamTemplateRequest(AbstractModel):
    """CreateParamTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 參數範本名稱。
        :type Name: str
        :param Description: 參數範本描述。
        :type Description: str
        :param EngineVersion: mysql版本。
        :type EngineVersion: str
        :param TemplateId: 源參數範本ID。
        :type TemplateId: int
        :param ParamList: 參數清單。
        :type ParamList: list of Parameter
        """
        self.Name = None
        self.Description = None
        self.EngineVersion = None
        self.TemplateId = None
        self.ParamList = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.EngineVersion = params.get("EngineVersion")
        self.TemplateId = params.get("TemplateId")
        if params.get("ParamList") is not None:
            self.ParamList = []
            for item in params.get("ParamList"):
                obj = Parameter()
                obj._deserialize(item)
                self.ParamList.append(obj)


class CreateParamTemplateResponse(AbstractModel):
    """CreateParamTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param TemplateId: 參數範本ID。
        :type TemplateId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")


class DBSwitchInfo(AbstractModel):
    """雲資料庫切換記錄

    """

    def __init__(self):
        """
        :param SwitchTime: 切換時間，格式爲：2017-09-03 01:34:31
        :type SwitchTime: str
        :param SwitchType: 切換類型，可能的返回值爲：TRANSFER - 數據遷移；MASTER2SLAVE - 主備切換；RECOVERY - 主從恢複
        :type SwitchType: str
        """
        self.SwitchTime = None
        self.SwitchType = None


    def _deserialize(self, params):
        self.SwitchTime = params.get("SwitchTime")
        self.SwitchType = params.get("SwitchType")


class DatabaseName(AbstractModel):
    """資料庫表名

    """

    def __init__(self):
        """
        :param DatabaseName: 資料庫表名
        :type DatabaseName: str
        """
        self.DatabaseName = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")


class DatabasePrivilege(AbstractModel):
    """資料庫權限

    """

    def __init__(self):
        """
        :param Privileges: 權限訊息
        :type Privileges: list of str
        :param Database: 資料庫名
        :type Database: str
        """
        self.Privileges = None
        self.Database = None


    def _deserialize(self, params):
        self.Privileges = params.get("Privileges")
        self.Database = params.get("Database")


class DeleteAccountsRequest(AbstractModel):
    """DeleteAccounts請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        :param Accounts: 雲資料庫賬号。
        :type Accounts: list of Account
        """
        self.InstanceId = None
        self.Accounts = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self.Accounts.append(obj)


class DeleteAccountsResponse(AbstractModel):
    """DeleteAccounts返回參數結構體

    """

    def __init__(self):
        """
        :param AsyncRequestId: 異步任務的請求ID，可使用此ID查詢異步任務的執行結果。
        :type AsyncRequestId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class DeleteBackupRequest(AbstractModel):
    """DeleteBackup請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv。與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        :param BackupId: 備份任務ID。該任務ID爲[創建雲資料庫備份](https://cloud.taifucloud.com/document/api/236/15844)介面返回的任務ID。
        :type BackupId: int
        """
        self.InstanceId = None
        self.BackupId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupId = params.get("BackupId")


class DeleteBackupResponse(AbstractModel):
    """DeleteBackup返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteParamTemplateRequest(AbstractModel):
    """DeleteParamTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param TemplateId: 參數範本ID。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


class DeleteParamTemplateResponse(AbstractModel):
    """DeleteParamTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTimeWindowRequest(AbstractModel):
    """DeleteTimeWindow請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DeleteTimeWindowResponse(AbstractModel):
    """DeleteTimeWindow返回參數結構體

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
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        :param User: 資料庫的賬号名稱。
        :type User: str
        :param Host: 資料庫的賬号域名。
        :type Host: str
        """
        self.InstanceId = None
        self.User = None
        self.Host = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.User = params.get("User")
        self.Host = params.get("Host")


class DescribeAccountPrivilegesResponse(AbstractModel):
    """DescribeAccountPrivileges返回參數結構體

    """

    def __init__(self):
        """
        :param GlobalPrivileges: 全局權限數組。
        :type GlobalPrivileges: list of str
        :param DatabasePrivileges: 資料庫權限數組。
        :type DatabasePrivileges: list of DatabasePrivilege
        :param TablePrivileges: 資料庫中的表權限數組。
        :type TablePrivileges: list of TablePrivilege
        :param ColumnPrivileges: 資料庫表中的列權限數組。
        :type ColumnPrivileges: list of ColumnPrivilege
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.GlobalPrivileges = None
        self.DatabasePrivileges = None
        self.TablePrivileges = None
        self.ColumnPrivileges = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GlobalPrivileges = params.get("GlobalPrivileges")
        if params.get("DatabasePrivileges") is not None:
            self.DatabasePrivileges = []
            for item in params.get("DatabasePrivileges"):
                obj = DatabasePrivilege()
                obj._deserialize(item)
                self.DatabasePrivileges.append(obj)
        if params.get("TablePrivileges") is not None:
            self.TablePrivileges = []
            for item in params.get("TablePrivileges"):
                obj = TablePrivilege()
                obj._deserialize(item)
                self.TablePrivileges.append(obj)
        if params.get("ColumnPrivileges") is not None:
            self.ColumnPrivileges = []
            for item in params.get("ColumnPrivileges"):
                obj = ColumnPrivilege()
                obj._deserialize(item)
                self.ColumnPrivileges.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        :param Offset: 記錄偏移量，預設值爲0。
        :type Offset: int
        :param Limit: 單次請求返回的數量，預設值爲20，最小值爲1，最大值爲100。
        :type Limit: int
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合查詢條件的賬号數量。
        :type TotalCount: int
        :param Items: 符合查詢條件的賬号詳細訊息。
        :type Items: list of AccountInfo
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
                obj = AccountInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAsyncRequestInfoRequest(AbstractModel):
    """DescribeAsyncRequestInfo請求參數結構體

    """

    def __init__(self):
        """
        :param AsyncRequestId: 異步任務的請求ID。
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
        :param Status: 任務執行結果。可能的取值：INITIAL - 初始化，RUNNING - 運作中，SUCCESS - 執行成功，FAILED - 執行失敗，KILLED - 已終止，REMOVED - 已删除，PAUSED - 終止中。
        :type Status: str
        :param Info: 任務執行訊息描述。
        :type Info: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Info = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Info = params.get("Info")
        self.RequestId = params.get("RequestId")


class DescribeBackupConfigRequest(AbstractModel):
    """DescribeBackupConfig請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例短實例ID，格式如：cdb-c1nl9rpv。與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeBackupConfigResponse(AbstractModel):
    """DescribeBackupConfig返回參數結構體

    """

    def __init__(self):
        """
        :param StartTimeMin: 備份開始的最早時間點，單位爲時刻。例如，2 - 淩晨2:00
        :type StartTimeMin: int
        :param StartTimeMax: 備份開始的最晚時間點，單位爲時刻。例如，6 - 淩晨6:00
        :type StartTimeMax: int
        :param BackupExpireDays: 備份過期時間，單位爲天
        :type BackupExpireDays: int
        :param BackupMethod: 備份方式，可能的值爲：physical - 物理備份，logical - 邏輯備份
        :type BackupMethod: str
        :param BinlogExpireDays: Binlog過期時間，單位爲天
        :type BinlogExpireDays: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.StartTimeMin = None
        self.StartTimeMax = None
        self.BackupExpireDays = None
        self.BackupMethod = None
        self.BinlogExpireDays = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StartTimeMin = params.get("StartTimeMin")
        self.StartTimeMax = params.get("StartTimeMax")
        self.BackupExpireDays = params.get("BackupExpireDays")
        self.BackupMethod = params.get("BackupMethod")
        self.BinlogExpireDays = params.get("BinlogExpireDays")
        self.RequestId = params.get("RequestId")


class DescribeBackupDatabasesRequest(AbstractModel):
    """DescribeBackupDatabases請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv。與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        :param StartTime: 開始時間，格式爲：2017-07-12 10:29:20。
        :type StartTime: str
        :param SearchDatabase: 要查詢的資料庫名前綴。
        :type SearchDatabase: str
        :param Offset: 分頁偏移量。
        :type Offset: int
        :param Limit: 分頁大小，最小值爲1，最大值爲2000。
        :type Limit: int
        """
        self.InstanceId = None
        self.StartTime = None
        self.SearchDatabase = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.SearchDatabase = params.get("SearchDatabase")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeBackupDatabasesResponse(AbstractModel):
    """DescribeBackupDatabases返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 返回的數據個數
        :type TotalCount: int
        :param Items: 符合查詢條件的資料庫數組
        :type Items: list of DatabaseName
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
                obj = DatabaseName()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBackupTablesRequest(AbstractModel):
    """DescribeBackupTables請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv。與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        :param StartTime: 開始時間，格式爲：2017-07-12 10:29:20。
        :type StartTime: str
        :param DatabaseName: 指定的資料庫名。
        :type DatabaseName: str
        :param SearchTable: 要查詢的數據表名前綴。
        :type SearchTable: str
        :param Offset: 分頁偏移。
        :type Offset: int
        :param Limit: 分頁大小，最小值爲1，最大值爲2000。
        :type Limit: int
        """
        self.InstanceId = None
        self.StartTime = None
        self.DatabaseName = None
        self.SearchTable = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.DatabaseName = params.get("DatabaseName")
        self.SearchTable = params.get("SearchTable")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeBackupTablesResponse(AbstractModel):
    """DescribeBackupTables返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 返回的數據個數。
        :type TotalCount: int
        :param Items: 符合條件的數據表數組。
        :type Items: list of TableName
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
                obj = TableName()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBackupsRequest(AbstractModel):
    """DescribeBackups請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv。與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        :param Offset: 偏移量，最小值爲0。
        :type Offset: int
        :param Limit: 分頁大小，預設值爲20，最小值爲1，最大值爲100。
        :type Limit: int
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeBackupsResponse(AbstractModel):
    """DescribeBackups返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合查詢條件的實例總數
        :type TotalCount: int
        :param Items: 符合查詢條件的備份訊息詳情
        :type Items: list of BackupInfo
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
                obj = BackupInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBinlogsRequest(AbstractModel):
    """DescribeBinlogs請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv。與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        :param Offset: 偏移量，最小值爲0。
        :type Offset: int
        :param Limit: 分頁大小，預設值爲20，最小值爲1，最大值爲100。
        :type Limit: int
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeBinlogsResponse(AbstractModel):
    """DescribeBinlogs返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合查詢條件的日志文件總數
        :type TotalCount: int
        :param Items: 符合查詢條件的二進制日志文件詳情
        :type Items: list of BinlogInfo
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
                obj = BinlogInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBImportRecordsRequest(AbstractModel):
    """DescribeDBImportRecords請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        :param StartTime: 開始時間，時間格式如：2016-01-01 00:00:01。
        :type StartTime: str
        :param EndTime: 結束時間，時間格式如：2016-01-01 23:59:59。
        :type EndTime: str
        :param Offset: 分頁參數 , 偏移量 , 預設值爲0。
        :type Offset: int
        :param Limit: 分頁參數 , 單次請求返回的數量 , 預設值爲20，最小值爲1，最大值爲100。
        :type Limit: int
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeDBImportRecordsResponse(AbstractModel):
    """DescribeDBImportRecords返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合查詢條件的導入任務操作日志總數。
        :type TotalCount: int
        :param Items: 返回的導入操作記錄清單。
        :type Items: list of ImportRecord
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
                obj = ImportRecord()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceCharsetRequest(AbstractModel):
    """DescribeDBInstanceCharset請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同，可使用[查詢實例清單](https://cloud.taifucloud.com/document/api/236/15872) 介面獲取，其值爲輸出參數中欄位 InstanceId 的值。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeDBInstanceCharsetResponse(AbstractModel):
    """DescribeDBInstanceCharset返回參數結構體

    """

    def __init__(self):
        """
        :param Charset: 實例的預設字元集，如"latin1", "utf8"等。
        :type Charset: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Charset = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Charset = params.get("Charset")
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceConfigRequest(AbstractModel):
    """DescribeDBInstanceConfig請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeDBInstanceConfigResponse(AbstractModel):
    """DescribeDBInstanceConfig返回參數結構體

    """

    def __init__(self):
        """
        :param ProtectMode: 主庫數據保護方式，主實例屬性，可能的返回值：0-異步複制方式，1-半同步複制方式，2-強同步複制方式。
        :type ProtectMode: int
        :param DeployMode: 主庫佈署方式，主實例屬性，可能的返回值：0-單可用佈署，1-多可用區佈署。
        :type DeployMode: int
        :param Zone: 主庫可用區的正式名稱，如ap-shanghai-1。
        :type Zone: str
        :param SlaveConfig: 從庫的配置訊息。
        :type SlaveConfig: :class:`taifucloudcloud.cdb.v20170320.models.SlaveConfig`
        :param BackupConfig: ECDB第二個從庫的配置訊息，只有ECDB實例才有這個欄位。
        :type BackupConfig: :class:`taifucloudcloud.cdb.v20170320.models.BackupConfig`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ProtectMode = None
        self.DeployMode = None
        self.Zone = None
        self.SlaveConfig = None
        self.BackupConfig = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProtectMode = params.get("ProtectMode")
        self.DeployMode = params.get("DeployMode")
        self.Zone = params.get("Zone")
        if params.get("SlaveConfig") is not None:
            self.SlaveConfig = SlaveConfig()
            self.SlaveConfig._deserialize(params.get("SlaveConfig"))
        if params.get("BackupConfig") is not None:
            self.BackupConfig = BackupConfig()
            self.BackupConfig._deserialize(params.get("BackupConfig"))
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceGTIDRequest(AbstractModel):
    """DescribeDBInstanceGTID請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同，可使用[查詢實例清單](https://cloud.taifucloud.com/document/api/236/15872) 介面獲取，其值爲輸出參數中欄位 InstanceId 的值。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeDBInstanceGTIDResponse(AbstractModel):
    """DescribeDBInstanceGTID返回參數結構體

    """

    def __init__(self):
        """
        :param IsGTIDOpen: GTID是否開通的标記：0-未開通，1-已開通。
        :type IsGTIDOpen: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.IsGTIDOpen = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsGTIDOpen = params.get("IsGTIDOpen")
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceRebootTimeRequest(AbstractModel):
    """DescribeDBInstanceRebootTime請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 實例的ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class DescribeDBInstanceRebootTimeResponse(AbstractModel):
    """DescribeDBInstanceRebootTime返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合查詢條件的實例總數。
        :type TotalCount: int
        :param Items: 返回的參數訊息。
        :type Items: list of InstanceRebootTime
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
                obj = InstanceRebootTime()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: 項目ID，可使用[查詢項目清單](https://cloud.taifucloud.com/document/product/378/4400)介面查詢項目ID
        :type ProjectId: int
        :param InstanceTypes: 實例類型，可取值：1-主實例，2-災備實例，3-只讀實例
        :type InstanceTypes: list of int non-negative
        :param Vips: 實例的内網IP網址
        :type Vips: list of str
        :param Status: 實例狀态，可取值：0-創建中，1-運作中，4-隔離中，5-已隔離
        :type Status: list of int non-negative
        :param Offset: 偏移量，預設值爲0
        :type Offset: int
        :param Limit: 單次請求返回的數量，預設值爲20，最大值爲2000
        :type Limit: int
        :param SecurityGroupId: 安全組ID
        :type SecurityGroupId: str
        :param PayTypes: 付費類型，可取值：0-包年包月，1-小時計費
        :type PayTypes: list of int non-negative
        :param InstanceNames: 實例名稱
        :type InstanceNames: list of str
        :param TaskStatus: 實例任務狀态，可能取值：<br>0-沒有任務<br>1-升級中<br>2-數據導入中<br>3-開放Slave中<br>4-外網訪問開通中<br>5-批次操作執行中<br>6-回檔中<br>7-外網訪問關閉中<br>8-密碼修改中<br>9-實例名修改中<br>10-重啓中<br>12-自建遷移中<br>13-删除庫表中<br>14-災備實例創建同步中<br>15-升級待切換<br>16-升級切換中<br>17-升級切換完成
        :type TaskStatus: list of int non-negative
        :param EngineVersions: 實例資料庫引擎版本，可能取值：5.1、5.5、5.6和5.7
        :type EngineVersions: list of str
        :param VpcIds: 私有網絡的ID
        :type VpcIds: list of int non-negative
        :param ZoneIds: 可用區的ID
        :type ZoneIds: list of int non-negative
        :param SubnetIds: 子網ID
        :type SubnetIds: list of int non-negative
        :param CdbErrors: 是否鎖定标記
        :type CdbErrors: list of int
        :param OrderBy: 返回結果集排序的欄位，目前支援："InstanceId", "InstanceName", "CreateTime", "DeadlineTime"
        :type OrderBy: str
        :param OrderDirection: 返回結果集排序方式，目前支援："ASC"或者"DESC"
        :type OrderDirection: str
        :param WithSecurityGroup: 是否包含安全組詳細訊息，可取值：0-不包含，1-包含
        :type WithSecurityGroup: int
        :param WithExCluster: 是否包含獨享集群詳細訊息，可取值：0-不包含，1-包含
        :type WithExCluster: int
        :param ExClusterId: 獨享集群ID
        :type ExClusterId: str
        :param InstanceIds: 實例ID
        :type InstanceIds: list of str
        :param InitFlag: 初始化标記，可取值：0-未初始化，1-初始化
        :type InitFlag: int
        :param WithDr: 是否包含災備實例，可取值：0-不包含，1-包含
        :type WithDr: int
        :param WithRo: 是否包含只讀實例，可取值：0-不包含，1-包含
        :type WithRo: int
        :param WithMaster: 是否包含主實例，可取值：0-不包含，1-包含
        :type WithMaster: int
        """
        self.ProjectId = None
        self.InstanceTypes = None
        self.Vips = None
        self.Status = None
        self.Offset = None
        self.Limit = None
        self.SecurityGroupId = None
        self.PayTypes = None
        self.InstanceNames = None
        self.TaskStatus = None
        self.EngineVersions = None
        self.VpcIds = None
        self.ZoneIds = None
        self.SubnetIds = None
        self.CdbErrors = None
        self.OrderBy = None
        self.OrderDirection = None
        self.WithSecurityGroup = None
        self.WithExCluster = None
        self.ExClusterId = None
        self.InstanceIds = None
        self.InitFlag = None
        self.WithDr = None
        self.WithRo = None
        self.WithMaster = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.InstanceTypes = params.get("InstanceTypes")
        self.Vips = params.get("Vips")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.PayTypes = params.get("PayTypes")
        self.InstanceNames = params.get("InstanceNames")
        self.TaskStatus = params.get("TaskStatus")
        self.EngineVersions = params.get("EngineVersions")
        self.VpcIds = params.get("VpcIds")
        self.ZoneIds = params.get("ZoneIds")
        self.SubnetIds = params.get("SubnetIds")
        self.CdbErrors = params.get("CdbErrors")
        self.OrderBy = params.get("OrderBy")
        self.OrderDirection = params.get("OrderDirection")
        self.WithSecurityGroup = params.get("WithSecurityGroup")
        self.WithExCluster = params.get("WithExCluster")
        self.ExClusterId = params.get("ExClusterId")
        self.InstanceIds = params.get("InstanceIds")
        self.InitFlag = params.get("InitFlag")
        self.WithDr = params.get("WithDr")
        self.WithRo = params.get("WithRo")
        self.WithMaster = params.get("WithMaster")


class DescribeDBInstancesResponse(AbstractModel):
    """DescribeDBInstances返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合查詢條件的實例總數
        :type TotalCount: int
        :param Items: 實例詳細訊息
        :type Items: list of InstanceInfo
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
                obj = InstanceInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBPriceRequest(AbstractModel):
    """DescribeDBPrice請求參數結構體

    """

    def __init__(self):
        """
        :param Zone: 可用區訊息，格式如"ap-guangzhou-2"。具體能設置的值請通過<a href="https://cloud.taifucloud.com/document/api/236/17229">DescribeDBZoneConfig</a>介面查詢。
        :type Zone: str
        :param GoodsNum: 實例數量，預設值爲1, 最小值1，最大值爲100
        :type GoodsNum: int
        :param Memory: 實例内存大小，單位：MB
        :type Memory: int
        :param Volume: 實例硬碟大小，單位：GB
        :type Volume: int
        :param PayType: 付費類型，支援值包括：PRE_PAID - 包年包月，HOUR_PAID - 按量計費
        :type PayType: str
        :param Period: 實例時長，單位：月，最小值1，最大值爲36；查詢按量計費價格時，該欄位無效
        :type Period: int
        :param InstanceRole: 實例類型，預設爲 master，支援值包括：master-表示主實例，ro-表示只讀實例，dr-表示災備實例
        :type InstanceRole: str
        :param ProtectMode: 數據複制方式，預設爲0，支援值包括：0-表示異步複制，1-表示半同步複制，2-表示強同步複制
        :type ProtectMode: int
        """
        self.Zone = None
        self.GoodsNum = None
        self.Memory = None
        self.Volume = None
        self.PayType = None
        self.Period = None
        self.InstanceRole = None
        self.ProtectMode = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.GoodsNum = params.get("GoodsNum")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.PayType = params.get("PayType")
        self.Period = params.get("Period")
        self.InstanceRole = params.get("InstanceRole")
        self.ProtectMode = params.get("ProtectMode")


class DescribeDBPriceResponse(AbstractModel):
    """DescribeDBPrice返回參數結構體

    """

    def __init__(self):
        """
        :param Price: 實例價格，單位：分（人民币）
        :type Price: int
        :param OriginalPrice: 實例原價，單位：分（人民币）
        :type OriginalPrice: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.OriginalPrice = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Price = params.get("Price")
        self.OriginalPrice = params.get("OriginalPrice")
        self.RequestId = params.get("RequestId")


class DescribeDBSecurityGroupsRequest(AbstractModel):
    """DescribeDBSecurityGroups請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeDBSecurityGroupsResponse(AbstractModel):
    """DescribeDBSecurityGroups返回參數結構體

    """

    def __init__(self):
        """
        :param Groups: 安全組詳情。
        :type Groups: list of SecurityGroup
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Groups = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self.Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self.Groups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBSwitchRecordsRequest(AbstractModel):
    """DescribeDBSwitchRecords請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        :param Offset: 分頁偏移量。
        :type Offset: int
        :param Limit: 分頁大小，預設值爲50，最小值爲1，最大值爲2000。
        :type Limit: int
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeDBSwitchRecordsResponse(AbstractModel):
    """DescribeDBSwitchRecords返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 實例切換記錄的總數。
        :type TotalCount: int
        :param Items: 實例切換記錄詳情。
        :type Items: list of DBSwitchInfo
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
                obj = DBSwitchInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBZoneConfigRequest(AbstractModel):
    """DescribeDBZoneConfig請求參數結構體

    """


class DescribeDBZoneConfigResponse(AbstractModel):
    """DescribeDBZoneConfig返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 可售賣地域配置數量
        :type TotalCount: int
        :param Items: 可售賣地域配置詳情
        :type Items: list of RegionSellConf
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
                obj = RegionSellConf()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    """DescribeDatabases請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        :param Offset: 偏移量，最小值爲0。
        :type Offset: int
        :param Limit: 單次請求數量，預設值爲20，最小值爲1，最大值爲100。
        :type Limit: int
        :param DatabaseRegexp: 比對資料庫庫名的正規表示式，規則同MySQL官網
        :type DatabaseRegexp: str
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None
        self.DatabaseRegexp = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.DatabaseRegexp = params.get("DatabaseRegexp")


class DescribeDatabasesResponse(AbstractModel):
    """DescribeDatabases返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合查詢條件的實例總數。
        :type TotalCount: int
        :param Items: 返回的實例訊息。
        :type Items: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Items = params.get("Items")
        self.RequestId = params.get("RequestId")


class DescribeDefaultParamsRequest(AbstractModel):
    """DescribeDefaultParams請求參數結構體

    """

    def __init__(self):
        """
        :param EngineVersion: mysql版本，目前支援["5.1", "5.5", "5.6", "5.7"]
        :type EngineVersion: str
        """
        self.EngineVersion = None


    def _deserialize(self, params):
        self.EngineVersion = params.get("EngineVersion")


class DescribeDefaultParamsResponse(AbstractModel):
    """DescribeDefaultParams返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 參數個數
        :type TotalCount: int
        :param Items: 參數詳情
        :type Items: list of ParameterDetail
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
                obj = ParameterDetail()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceMonitorInfoRequest(AbstractModel):
    """DescribeDeviceMonitorInfo請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv。與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        :param Count: 返回當天最近Count個5分鍾粒度的監控數據。最小值1，最大值288，不傳該參數預設返回當天所有5分鍾粒度監控數據。
        :type Count: int
        """
        self.InstanceId = None
        self.Count = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Count = params.get("Count")


class DescribeDeviceMonitorInfoResponse(AbstractModel):
    """DescribeDeviceMonitorInfo返回參數結構體

    """

    def __init__(self):
        """
        :param Cpu: 實例CPU監控數據
        :type Cpu: :class:`taifucloudcloud.cdb.v20170320.models.DeviceCpuInfo`
        :param Mem: 實例内存監控數據
        :type Mem: :class:`taifucloudcloud.cdb.v20170320.models.DeviceMemInfo`
        :param Net: 實例網絡監控數據
        :type Net: :class:`taifucloudcloud.cdb.v20170320.models.DeviceNetInfo`
        :param Disk: 實例磁盤監控數據
        :type Disk: :class:`taifucloudcloud.cdb.v20170320.models.DeviceDiskInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Cpu = None
        self.Mem = None
        self.Net = None
        self.Disk = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Cpu") is not None:
            self.Cpu = DeviceCpuInfo()
            self.Cpu._deserialize(params.get("Cpu"))
        if params.get("Mem") is not None:
            self.Mem = DeviceMemInfo()
            self.Mem._deserialize(params.get("Mem"))
        if params.get("Net") is not None:
            self.Net = DeviceNetInfo()
            self.Net._deserialize(params.get("Net"))
        if params.get("Disk") is not None:
            self.Disk = DeviceDiskInfo()
            self.Disk._deserialize(params.get("Disk"))
        self.RequestId = params.get("RequestId")


class DescribeInstanceParamRecordsRequest(AbstractModel):
    """DescribeInstanceParamRecords請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同，可使用[查詢實例清單](https://cloud.taifucloud.com/document/api/236/15872) 介面獲取，其值爲輸出參數中欄位 InstanceId 的值。
        :type InstanceId: str
        :param Offset: 分頁偏移量。
        :type Offset: int
        :param Limit: 分頁大小。
        :type Limit: int
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeInstanceParamRecordsResponse(AbstractModel):
    """DescribeInstanceParamRecords返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的記錄數
        :type TotalCount: int
        :param Items: 參數修改記錄
        :type Items: list of ParamRecord
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
                obj = ParamRecord()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceParamsRequest(AbstractModel):
    """DescribeInstanceParams請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同，可使用[查詢實例清單](https://cloud.taifucloud.com/document/api/236/15872) 介面獲取，其值爲輸出參數中欄位 InstanceId 的值
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
        :param TotalCount: 實例的參數總數
        :type TotalCount: int
        :param Items: 參數詳情
        :type Items: list of ParameterDetail
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
                obj = ParameterDetail()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeParamTemplateInfoRequest(AbstractModel):
    """DescribeParamTemplateInfo請求參數結構體

    """

    def __init__(self):
        """
        :param TemplateId: 參數範本Id。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


class DescribeParamTemplateInfoResponse(AbstractModel):
    """DescribeParamTemplateInfo返回參數結構體

    """

    def __init__(self):
        """
        :param TemplateId: 參數範本Id。
        :type TemplateId: int
        :param Name: 參數範本名稱。
        :type Name: str
        :param EngineVersion: 參數範本描述
        :type EngineVersion: str
        :param TotalCount: 參數範本中的參數數量
        :type TotalCount: int
        :param Items: 參數詳情
        :type Items: list of ParameterDetail
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TemplateId = None
        self.Name = None
        self.EngineVersion = None
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.Name = params.get("Name")
        self.EngineVersion = params.get("EngineVersion")
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = ParameterDetail()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeParamTemplatesRequest(AbstractModel):
    """DescribeParamTemplates請求參數結構體

    """


class DescribeParamTemplatesResponse(AbstractModel):
    """DescribeParamTemplates返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 該用戶的參數範本數量。
        :type TotalCount: int
        :param Items: 參數範本詳情。
        :type Items: list of ParamTemplateInfo
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
                obj = ParamTemplateInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    """DescribeProjectSecurityGroups請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: 項目ID。
        :type ProjectId: int
        """
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")


class DescribeProjectSecurityGroupsResponse(AbstractModel):
    """DescribeProjectSecurityGroups返回參數結構體

    """

    def __init__(self):
        """
        :param Groups: 安全組詳情。
        :type Groups: list of SecurityGroup
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Groups = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self.Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self.Groups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRollbackRangeTimeRequest(AbstractModel):
    """DescribeRollbackRangeTime請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 實例ID清單，單個實例Id的格式如：cdb-c1nl9rpv。與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class DescribeRollbackRangeTimeResponse(AbstractModel):
    """DescribeRollbackRangeTime返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合查詢條件的實例總數。
        :type TotalCount: int
        :param Items: 返回的參數訊息。
        :type Items: list of InstanceRollbackRangeTime
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
                obj = InstanceRollbackRangeTime()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSlowLogsRequest(AbstractModel):
    """DescribeSlowLogs請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv。與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        :param Offset: 偏移量，最小值爲0。
        :type Offset: int
        :param Limit: 分頁大小，預設值爲20，最小值爲1，最大值爲100。
        :type Limit: int
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeSlowLogsResponse(AbstractModel):
    """DescribeSlowLogs返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合查詢條件的慢查詢日志總數
        :type TotalCount: int
        :param Items: 符合查詢條件的慢查詢日志詳情
        :type Items: list of SlowLogInfo
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
                obj = SlowLogInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSupportedPrivilegesRequest(AbstractModel):
    """DescribeSupportedPrivileges請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeSupportedPrivilegesResponse(AbstractModel):
    """DescribeSupportedPrivileges返回參數結構體

    """

    def __init__(self):
        """
        :param GlobalSupportedPrivileges: 實例支援的全局權限。
        :type GlobalSupportedPrivileges: list of str
        :param DatabaseSupportedPrivileges: 實例支援的資料庫權限。
        :type DatabaseSupportedPrivileges: list of str
        :param TableSupportedPrivileges: 實例支援的資料庫表權限。
        :type TableSupportedPrivileges: list of str
        :param ColumnSupportedPrivileges: 實例支援的資料庫列權限。
        :type ColumnSupportedPrivileges: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.GlobalSupportedPrivileges = None
        self.DatabaseSupportedPrivileges = None
        self.TableSupportedPrivileges = None
        self.ColumnSupportedPrivileges = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GlobalSupportedPrivileges = params.get("GlobalSupportedPrivileges")
        self.DatabaseSupportedPrivileges = params.get("DatabaseSupportedPrivileges")
        self.TableSupportedPrivileges = params.get("TableSupportedPrivileges")
        self.ColumnSupportedPrivileges = params.get("ColumnSupportedPrivileges")
        self.RequestId = params.get("RequestId")


class DescribeTablesRequest(AbstractModel):
    """DescribeTables請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        :param Database: 資料庫的名稱。
        :type Database: str
        :param Offset: 記錄偏移量，預設值爲0。
        :type Offset: int
        :param Limit: 單次請求返回的數量，預設值爲20，最大值爲2000。
        :type Limit: int
        :param TableRegexp: 比對資料庫表名的正規表示式，規則同MySQL官網
        :type TableRegexp: str
        """
        self.InstanceId = None
        self.Database = None
        self.Offset = None
        self.Limit = None
        self.TableRegexp = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Database = params.get("Database")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TableRegexp = params.get("TableRegexp")


class DescribeTablesResponse(AbstractModel):
    """DescribeTables返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合查詢條件的資料庫表總數。
        :type TotalCount: int
        :param Items: 返回的資料庫表訊息。
        :type Items: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Items = params.get("Items")
        self.RequestId = params.get("RequestId")


class DescribeTagsOfInstanceIdsRequest(AbstractModel):
    """DescribeTagsOfInstanceIds請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 實例清單
        :type InstanceIds: list of str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 每頁返回多少個标簽
        :type Limit: int
        """
        self.InstanceIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTagsOfInstanceIdsResponse(AbstractModel):
    """DescribeTagsOfInstanceIds返回參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 每頁返回多少個标簽
        :type Limit: int
        :param Rows: 實例标簽訊息
        :type Rows: list of TagsInfoOfInstance
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Offset = None
        self.Limit = None
        self.Rows = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Rows") is not None:
            self.Rows = []
            for item in params.get("Rows"):
                obj = TagsInfoOfInstance()
                obj._deserialize(item)
                self.Rows.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同，可使用[查詢實例清單](https://cloud.taifucloud.com/document/api/236/15872) 介面獲取，其值爲輸出參數中欄位 InstanceId 的值
        :type InstanceId: str
        :param AsyncRequestId: 異步任務請求ID，執行 CDB 相關操作返回的 AsyncRequestId
        :type AsyncRequestId: str
        :param TaskTypes: 任務類型，不傳值則查詢所有任務類型，可能的值：1-資料庫回檔；2-SQL操作；3-數據導入；5-參數設置；6-初始化；7-重啓；8-開啓GTID；9-只讀實例升級；10-資料庫批次回檔；11-主實例升級；12-删除庫表；13-切換爲主實例；
        :type TaskTypes: list of int
        :param TaskStatus: 任務狀态，不傳值則查詢所有任務狀态，可能的值：-1-未定義；0-初始化; 1-運作中；2-執行成功；3-執行失敗；4-已終止；5-已删除；6-已暫停；
        :type TaskStatus: list of int
        :param StartTimeBegin: 第一個任務的開始時間，用于範圍查詢，時間格式如：2017-12-31 10:40:01
        :type StartTimeBegin: str
        :param StartTimeEnd: 最後一個任務的開始時間，用于範圍查詢，時間格式如：2017-12-31 10:40:01
        :type StartTimeEnd: str
        :param Offset: 記錄偏移量，預設值爲0
        :type Offset: int
        :param Limit: 單次請求返回的數量，預設值爲20，最大值爲100
        :type Limit: int
        """
        self.InstanceId = None
        self.AsyncRequestId = None
        self.TaskTypes = None
        self.TaskStatus = None
        self.StartTimeBegin = None
        self.StartTimeEnd = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.TaskTypes = params.get("TaskTypes")
        self.TaskStatus = params.get("TaskStatus")
        self.StartTimeBegin = params.get("StartTimeBegin")
        self.StartTimeEnd = params.get("StartTimeEnd")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合查詢條件的實例總數
        :type TotalCount: int
        :param Items: 返回的實例任務訊息
        :type Items: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Items = params.get("Items")
        self.RequestId = params.get("RequestId")


class DescribeTimeWindowRequest(AbstractModel):
    """DescribeTimeWindow請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeTimeWindowResponse(AbstractModel):
    """DescribeTimeWindow返回參數結構體

    """

    def __init__(self):
        """
        :param Monday: 星期一的可維護時間清單。
        :type Monday: list of str
        :param Tuesday: 星期二的可維護時間清單。
        :type Tuesday: list of str
        :param Wednesday: 星期三的可維護時間清單。
        :type Wednesday: list of str
        :param Thursday: 星期四的可維護時間清單。
        :type Thursday: list of str
        :param Friday: 星期五的可維護時間清單。
        :type Friday: list of str
        :param Saturday: 星期六的可維護時間清單。
        :type Saturday: list of str
        :param Sunday: 星期日的可維護時間清單。
        :type Sunday: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Monday = None
        self.Tuesday = None
        self.Wednesday = None
        self.Thursday = None
        self.Friday = None
        self.Saturday = None
        self.Sunday = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Monday = params.get("Monday")
        self.Tuesday = params.get("Tuesday")
        self.Wednesday = params.get("Wednesday")
        self.Thursday = params.get("Thursday")
        self.Friday = params.get("Friday")
        self.Saturday = params.get("Saturday")
        self.Sunday = params.get("Sunday")
        self.RequestId = params.get("RequestId")


class DescribeUploadedFilesRequest(AbstractModel):
    """DescribeUploadedFiles請求參數結構體

    """

    def __init__(self):
        """
        :param Path: 文件路徑。該欄位應填用戶主賬号的OwnerUin訊息。
        :type Path: str
        :param Offset: 記錄偏移量，預設值爲0。
        :type Offset: int
        :param Limit: 單次請求返回的數量，預設值爲20。
        :type Limit: int
        """
        self.Path = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeUploadedFilesResponse(AbstractModel):
    """DescribeUploadedFiles返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合查詢條件的SQL文件總數。
        :type TotalCount: int
        :param Items: 返回的SQL文件清單。
        :type Items: list of SqlFileInfo
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
                obj = SqlFileInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DeviceCpuInfo(AbstractModel):
    """CPU負載

    """

    def __init__(self):
        """
        :param Rate: 實例CPU平均使用率
        :type Rate: list of DeviceCpuRateInfo
        :param Load: 實例CPU監控數據
        :type Load: list of int
        """
        self.Rate = None
        self.Load = None


    def _deserialize(self, params):
        if params.get("Rate") is not None:
            self.Rate = []
            for item in params.get("Rate"):
                obj = DeviceCpuRateInfo()
                obj._deserialize(item)
                self.Rate.append(obj)
        self.Load = params.get("Load")


class DeviceCpuRateInfo(AbstractModel):
    """實例CPU平均使用率

    """

    def __init__(self):
        """
        :param CpuCore: Cpu核編号
        :type CpuCore: int
        :param Rate: Cpu使用率
        :type Rate: list of int
        """
        self.CpuCore = None
        self.Rate = None


    def _deserialize(self, params):
        self.CpuCore = params.get("CpuCore")
        self.Rate = params.get("Rate")


class DeviceDiskInfo(AbstractModel):
    """實例磁盤監控數據

    """

    def __init__(self):
        """
        :param IoRatioPerSec: 平均每秒有百分之幾的時間用于IO操作
        :type IoRatioPerSec: list of int
        :param IoWaitTime: 平均每次設備I/O操作的等待時間*100，單位爲毫秒。例如：該值爲201，表示平均每次I/O操作等待時間爲：201/100=2.1毫秒
        :type IoWaitTime: list of int
        :param Read: 磁盤平均每秒完成的讀操作次數總和*100。例如：該值爲2002，表示磁盤平均每秒完成讀操作爲：2002/100=20.2次
        :type Read: list of int
        :param Write: 磁盤平均每秒完成的寫操作次數總和*100。例如：該值爲30001，表示磁盤平均每秒完成寫操作爲：30001/100=300.01次
        :type Write: list of int
        """
        self.IoRatioPerSec = None
        self.IoWaitTime = None
        self.Read = None
        self.Write = None


    def _deserialize(self, params):
        self.IoRatioPerSec = params.get("IoRatioPerSec")
        self.IoWaitTime = params.get("IoWaitTime")
        self.Read = params.get("Read")
        self.Write = params.get("Write")


class DeviceMemInfo(AbstractModel):
    """實例所在物理機内存監控訊息

    """

    def __init__(self):
        """
        :param Total: 總内存大小。free命令中Mem:一行total的值,單位：KB
        :type Total: list of int
        :param Used: 已使用内存。free命令中Mem:一行used的值,單位：KB
        :type Used: list of int
        """
        self.Total = None
        self.Used = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        self.Used = params.get("Used")


class DeviceNetInfo(AbstractModel):
    """實例所在物理機網絡監控訊息

    """

    def __init__(self):
        """
        :param Conn: tcp連接數
        :type Conn: list of int
        :param PackageIn: 網卡入包量
        :type PackageIn: list of int
        :param PackageOut: 網卡出包量
        :type PackageOut: list of int
        :param FlowIn: 入流量，單位：KB
        :type FlowIn: list of int
        :param FlowOut: 出流量，單位：KB
        :type FlowOut: list of int
        """
        self.Conn = None
        self.PackageIn = None
        self.PackageOut = None
        self.FlowIn = None
        self.FlowOut = None


    def _deserialize(self, params):
        self.Conn = params.get("Conn")
        self.PackageIn = params.get("PackageIn")
        self.PackageOut = params.get("PackageOut")
        self.FlowIn = params.get("FlowIn")
        self.FlowOut = params.get("FlowOut")


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups請求參數結構體

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全組Id。
        :type SecurityGroupId: str
        :param InstanceIds: 實例ID清單，一個或者多個實例Id組成的數組。
        :type InstanceIds: list of str
        """
        self.SecurityGroupId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.InstanceIds = params.get("InstanceIds")


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DrInfo(AbstractModel):
    """災備實例訊息

    """

    def __init__(self):
        """
        :param Status: 災備實例狀态
        :type Status: int
        :param Zone: 可用區訊息
        :type Zone: str
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param Region: 地域訊息
        :type Region: str
        :param SyncStatus: 實例同步狀态
        :type SyncStatus: int
        :param InstanceName: 實例名稱
        :type InstanceName: str
        :param InstanceType: 實例類型
        :type InstanceType: int
        """
        self.Status = None
        self.Zone = None
        self.InstanceId = None
        self.Region = None
        self.SyncStatus = None
        self.InstanceName = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Zone = params.get("Zone")
        self.InstanceId = params.get("InstanceId")
        self.Region = params.get("Region")
        self.SyncStatus = params.get("SyncStatus")
        self.InstanceName = params.get("InstanceName")
        self.InstanceType = params.get("InstanceType")


class ImportRecord(AbstractModel):
    """導入任務記錄

    """

    def __init__(self):
        """
        :param Status: 狀态值
        :type Status: int
        :param Code: 狀态值
        :type Code: int
        :param CostTime: 執行時間
        :type CostTime: int
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param WorkId: 後端任務ID
        :type WorkId: str
        :param FileName: 導入文件名
        :type FileName: str
        :param Process: 執行進度
        :type Process: int
        :param CreateTime: 任務創建時間
        :type CreateTime: str
        :param FileSize: 文件大小
        :type FileSize: str
        :param Message: 任務執行訊息
        :type Message: str
        :param JobId: 任務ID
        :type JobId: int
        :param DbName: 導入庫表名
        :type DbName: str
        :param AsyncRequestId: 異步任務的請求ID
        :type AsyncRequestId: str
        """
        self.Status = None
        self.Code = None
        self.CostTime = None
        self.InstanceId = None
        self.WorkId = None
        self.FileName = None
        self.Process = None
        self.CreateTime = None
        self.FileSize = None
        self.Message = None
        self.JobId = None
        self.DbName = None
        self.AsyncRequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Code = params.get("Code")
        self.CostTime = params.get("CostTime")
        self.InstanceId = params.get("InstanceId")
        self.WorkId = params.get("WorkId")
        self.FileName = params.get("FileName")
        self.Process = params.get("Process")
        self.CreateTime = params.get("CreateTime")
        self.FileSize = params.get("FileSize")
        self.Message = params.get("Message")
        self.JobId = params.get("JobId")
        self.DbName = params.get("DbName")
        self.AsyncRequestId = params.get("AsyncRequestId")


class Inbound(AbstractModel):
    """安全組入站規則

    """

    def __init__(self):
        """
        :param Action: 策略，ACCEPT或者DROP
        :type Action: str
        :param CidrIp: 來源Ip或Ip段，例如192.168.0.0/16
        :type CidrIp: str
        :param PortRange: 端口
        :type PortRange: str
        :param IpProtocol: 網絡協議，支援udp、tcp等
        :type IpProtocol: str
        :param Dir: 規則限定的方向，進站規則爲INPUT
        :type Dir: str
        """
        self.Action = None
        self.CidrIp = None
        self.PortRange = None
        self.IpProtocol = None
        self.Dir = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.CidrIp = params.get("CidrIp")
        self.PortRange = params.get("PortRange")
        self.IpProtocol = params.get("IpProtocol")
        self.Dir = params.get("Dir")


class InitDBInstancesRequest(AbstractModel):
    """InitDBInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同，可使用[查詢實例清單](https://cloud.taifucloud.com/document/api/236/15872) 介面獲取，其值爲輸出參數中欄位 InstanceId 的值。
        :type InstanceIds: list of str
        :param NewPassword: 實例新的密碼，密碼規則：8-64個字元，至少包含字母、數字、字元（支援的字元：!@#$%^*()）中的兩種。
        :type NewPassword: str
        :param Parameters: 實例的參數清單，目前支援設置“character_set_server”、“lower_case_table_names”參數。其中，“character_set_server”參數可選值爲["utf8","latin1","gbk","utf8mb4"]；“lower_case_table_names”可選值爲[“0”,“1”]。
        :type Parameters: list of ParamInfo
        :param Vport: 實例的端口，取值範圍爲[1024, 65535]
        :type Vport: int
        """
        self.InstanceIds = None
        self.NewPassword = None
        self.Parameters = None
        self.Vport = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.NewPassword = params.get("NewPassword")
        if params.get("Parameters") is not None:
            self.Parameters = []
            for item in params.get("Parameters"):
                obj = ParamInfo()
                obj._deserialize(item)
                self.Parameters.append(obj)
        self.Vport = params.get("Vport")


class InitDBInstancesResponse(AbstractModel):
    """InitDBInstances返回參數結構體

    """

    def __init__(self):
        """
        :param AsyncRequestIds: 異步任務的請求ID數組，可使用此ID查詢異步任務的執行結果
        :type AsyncRequestIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestIds = params.get("AsyncRequestIds")
        self.RequestId = params.get("RequestId")


class InquiryPriceUpgradeInstancesRequest(AbstractModel):
    """InquiryPriceUpgradeInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv。與雲資料庫控制台頁面中顯示的實例ID相同，可使用[查詢實例清單](https://cloud.taifucloud.com/document/api/236/15872) 介面獲取，其值爲輸出參數中欄位 InstanceId 的值
        :type InstanceId: str
        :param Memory: 升級後的内存大小，單位：MB，爲保證傳入 Memory 值有效，請使用[獲取雲資料庫可售賣規格](https://cloud.taifucloud.com/document/product/236/17229)介面獲取可升級的内存規格
        :type Memory: int
        :param Volume: 升級後的硬碟大小，單位：GB，爲保證傳入 Volume 值有效，請使用[獲取雲資料庫可售賣規格](https://cloud.taifucloud.com/document/product/236/17229)介面獲取可升級的硬碟範圍
        :type Volume: int
        :param Cpu: 升級後的核心數目，單位：核，爲保證傳入 CPU 值有效，請使用[獲取雲資料庫可售賣規格](https://cloud.taifucloud.com/document/product/236/17229)介面獲取可升級的核心數目，當未指定該值時，将按照 Memory 大小補全一個預設值
        :type Cpu: int
        :param ProtectMode: 數據複制方式，支援值包括：0-異步複制，1-半同步複制，2-強同步複制，升級主實例時可指定該參數，升級只讀實例或者災備實例時指定該參數無意義
        :type ProtectMode: int
        """
        self.InstanceId = None
        self.Memory = None
        self.Volume = None
        self.Cpu = None
        self.ProtectMode = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.Cpu = params.get("Cpu")
        self.ProtectMode = params.get("ProtectMode")


class InquiryPriceUpgradeInstancesResponse(AbstractModel):
    """InquiryPriceUpgradeInstances返回參數結構體

    """

    def __init__(self):
        """
        :param Price: 實例價格，單位：分（人民币）
        :type Price: int
        :param OriginalPrice: 實例原價，單位：分（人民币）
        :type OriginalPrice: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.OriginalPrice = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Price = params.get("Price")
        self.OriginalPrice = params.get("OriginalPrice")
        self.RequestId = params.get("RequestId")


class InstanceInfo(AbstractModel):
    """實例詳細訊息

    """

    def __init__(self):
        """
        :param WanStatus: 外網狀态，可能的返回值爲：0-未開通外網；1-已開通外網；2-已關閉外網
        :type WanStatus: int
        :param Zone: 可用區訊息
        :type Zone: str
        :param InitFlag: 初始化标志，可能的返回值爲：0-未初始化；1-已初始化
        :type InitFlag: int
        :param RoVipInfo: 只讀vip訊息。單獨開通只讀實例訪問的只讀實例才有該欄位
        :type RoVipInfo: :class:`taifucloudcloud.cdb.v20170320.models.RoVipInfo`
        :param Memory: 内存容量，單位爲MB
        :type Memory: int
        :param Status: 實例狀态，可能的返回值：0-創建中；1-運作中；4-隔離中；5-已隔離
        :type Status: int
        :param VpcId: 私有網絡ID，例如：51102
        :type VpcId: int
        :param SlaveInfo: 備機訊息
        :type SlaveInfo: :class:`taifucloudcloud.cdb.v20170320.models.SlaveInfo`
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param Volume: 硬碟容量，單位爲GB
        :type Volume: int
        :param AutoRenew: 自動續約标志，可能的返回值：0-未開通自動續約；1-已開通自動續約；2-已關閉自動續約
        :type AutoRenew: int
        :param ProtectMode: 數據複制方式
        :type ProtectMode: int
        :param RoGroups: 只讀組詳細訊息
        :type RoGroups: list of RoGroup
        :param SubnetId: 子網ID，例如：2333
        :type SubnetId: int
        :param InstanceType: 實例類型，可能的返回值：1-主實例；2-災備實例；3-只讀實例
        :type InstanceType: int
        :param ProjectId: 項目ID
        :type ProjectId: int
        :param Region: 地域訊息
        :type Region: str
        :param DeadlineTime: 實例到期時間
        :type DeadlineTime: str
        :param DeployMode: 可用區佈署方式
        :type DeployMode: int
        :param TaskStatus: 實例任務狀态
        :type TaskStatus: int
        :param MasterInfo: 主實例詳細訊息
        :type MasterInfo: :class:`taifucloudcloud.cdb.v20170320.models.MasterInfo`
        :param DeviceType: 實例類型，可能的返回值：“HA”-高可用版；“BASIC”-基礎版
        :type DeviceType: str
        :param EngineVersion: 内核版本
        :type EngineVersion: str
        :param InstanceName: 實例名稱
        :type InstanceName: str
        :param DrInfo: 災備實例詳細訊息
        :type DrInfo: list of DrInfo
        :param WanDomain: 外網域名
        :type WanDomain: str
        :param WanPort: 外網端口号
        :type WanPort: int
        :param PayType: 付費類型，可能的返回值：0-包年包月；1-按量計費
        :type PayType: int
        :param CreateTime: 實例創建時間
        :type CreateTime: str
        :param Vip: 實例IP
        :type Vip: str
        :param Vport: 端口号
        :type Vport: int
        :param CdbError: 是否鎖定标記
        :type CdbError: int
        :param UniqVpcId: 私有網絡描述符，例如：“vpc-5v8wn9mg”
        :type UniqVpcId: str
        :param UniqSubnetId: 子網描述符，例如：“subnet-1typ0s7d”
        :type UniqSubnetId: str
        :param PhysicalId: 物理ID
        :type PhysicalId: str
        :param Cpu: 核心數
        :type Cpu: int
        :param Qps: 每秒查詢數量
        :type Qps: int
        :param ZoneName: 可用區中文名稱
        :type ZoneName: str
        """
        self.WanStatus = None
        self.Zone = None
        self.InitFlag = None
        self.RoVipInfo = None
        self.Memory = None
        self.Status = None
        self.VpcId = None
        self.SlaveInfo = None
        self.InstanceId = None
        self.Volume = None
        self.AutoRenew = None
        self.ProtectMode = None
        self.RoGroups = None
        self.SubnetId = None
        self.InstanceType = None
        self.ProjectId = None
        self.Region = None
        self.DeadlineTime = None
        self.DeployMode = None
        self.TaskStatus = None
        self.MasterInfo = None
        self.DeviceType = None
        self.EngineVersion = None
        self.InstanceName = None
        self.DrInfo = None
        self.WanDomain = None
        self.WanPort = None
        self.PayType = None
        self.CreateTime = None
        self.Vip = None
        self.Vport = None
        self.CdbError = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.PhysicalId = None
        self.Cpu = None
        self.Qps = None
        self.ZoneName = None


    def _deserialize(self, params):
        self.WanStatus = params.get("WanStatus")
        self.Zone = params.get("Zone")
        self.InitFlag = params.get("InitFlag")
        if params.get("RoVipInfo") is not None:
            self.RoVipInfo = RoVipInfo()
            self.RoVipInfo._deserialize(params.get("RoVipInfo"))
        self.Memory = params.get("Memory")
        self.Status = params.get("Status")
        self.VpcId = params.get("VpcId")
        if params.get("SlaveInfo") is not None:
            self.SlaveInfo = SlaveInfo()
            self.SlaveInfo._deserialize(params.get("SlaveInfo"))
        self.InstanceId = params.get("InstanceId")
        self.Volume = params.get("Volume")
        self.AutoRenew = params.get("AutoRenew")
        self.ProtectMode = params.get("ProtectMode")
        if params.get("RoGroups") is not None:
            self.RoGroups = []
            for item in params.get("RoGroups"):
                obj = RoGroup()
                obj._deserialize(item)
                self.RoGroups.append(obj)
        self.SubnetId = params.get("SubnetId")
        self.InstanceType = params.get("InstanceType")
        self.ProjectId = params.get("ProjectId")
        self.Region = params.get("Region")
        self.DeadlineTime = params.get("DeadlineTime")
        self.DeployMode = params.get("DeployMode")
        self.TaskStatus = params.get("TaskStatus")
        if params.get("MasterInfo") is not None:
            self.MasterInfo = MasterInfo()
            self.MasterInfo._deserialize(params.get("MasterInfo"))
        self.DeviceType = params.get("DeviceType")
        self.EngineVersion = params.get("EngineVersion")
        self.InstanceName = params.get("InstanceName")
        if params.get("DrInfo") is not None:
            self.DrInfo = []
            for item in params.get("DrInfo"):
                obj = DrInfo()
                obj._deserialize(item)
                self.DrInfo.append(obj)
        self.WanDomain = params.get("WanDomain")
        self.WanPort = params.get("WanPort")
        self.PayType = params.get("PayType")
        self.CreateTime = params.get("CreateTime")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.CdbError = params.get("CdbError")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.PhysicalId = params.get("PhysicalId")
        self.Cpu = params.get("Cpu")
        self.Qps = params.get("Qps")
        self.ZoneName = params.get("ZoneName")


class InstanceRebootTime(AbstractModel):
    """實例預期重啓時間

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同
        :type InstanceId: str
        :param TimeInSeconds: 預期重啓時間
        :type TimeInSeconds: int
        """
        self.InstanceId = None
        self.TimeInSeconds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TimeInSeconds = params.get("TimeInSeconds")


class InstanceRollbackRangeTime(AbstractModel):
    """實例可回檔時間範圍

    """

    def __init__(self):
        """
        :param Code: 查詢資料庫錯誤碼
        :type Code: int
        :param Message: 查詢資料庫錯誤訊息
        :type Message: str
        :param InstanceId: 實例ID清單，單個實例Id的格式如：cdb-c1nl9rpv。與雲資料庫控制台頁面中顯示的實例ID相同
        :type InstanceId: str
        :param Times: 可回檔時間範圍
        :type Times: list of RollbackTimeRange
        """
        self.Code = None
        self.Message = None
        self.InstanceId = None
        self.Times = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        self.InstanceId = params.get("InstanceId")
        if params.get("Times") is not None:
            self.Times = []
            for item in params.get("Times"):
                obj = RollbackTimeRange()
                obj._deserialize(item)
                self.Times.append(obj)


class IsolateDBInstanceRequest(AbstractModel):
    """IsolateDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同，可使用[查詢實例清單](https://cloud.taifucloud.com/document/api/236/15872) 介面獲取，其值爲輸出參數中欄位 InstanceId 的值
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
        :param AsyncRequestId: 異步任務的請求ID，可使用此ID查詢異步任務的執行結果
        :type AsyncRequestId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class MasterInfo(AbstractModel):
    """主實例訊息

    """

    def __init__(self):
        """
        :param Region: 地域訊息
        :type Region: str
        :param RegionId: 地域ID
        :type RegionId: int
        :param ZoneId: 可用區ID
        :type ZoneId: int
        :param Zone: 可用區訊息
        :type Zone: str
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param ResourceId: 實例長ID
        :type ResourceId: str
        :param Status: 實例狀态
        :type Status: int
        :param InstanceName: 實例名稱
        :type InstanceName: str
        :param InstanceType: 實例類型
        :type InstanceType: int
        :param TaskStatus: 任務狀态
        :type TaskStatus: int
        :param Memory: 内存容量
        :type Memory: int
        :param Volume: 硬碟容量
        :type Volume: int
        :param DeviceType: 實例機型
        :type DeviceType: str
        :param Qps: 每秒查詢數
        :type Qps: int
        :param VpcId: 私有網絡ID
        :type VpcId: int
        :param SubnetId: 子網ID
        :type SubnetId: int
        :param ExClusterId: 獨享集群ID
        :type ExClusterId: str
        :param ExClusterName: 獨享集群名稱
        :type ExClusterName: str
        """
        self.Region = None
        self.RegionId = None
        self.ZoneId = None
        self.Zone = None
        self.InstanceId = None
        self.ResourceId = None
        self.Status = None
        self.InstanceName = None
        self.InstanceType = None
        self.TaskStatus = None
        self.Memory = None
        self.Volume = None
        self.DeviceType = None
        self.Qps = None
        self.VpcId = None
        self.SubnetId = None
        self.ExClusterId = None
        self.ExClusterName = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionId = params.get("RegionId")
        self.ZoneId = params.get("ZoneId")
        self.Zone = params.get("Zone")
        self.InstanceId = params.get("InstanceId")
        self.ResourceId = params.get("ResourceId")
        self.Status = params.get("Status")
        self.InstanceName = params.get("InstanceName")
        self.InstanceType = params.get("InstanceType")
        self.TaskStatus = params.get("TaskStatus")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.DeviceType = params.get("DeviceType")
        self.Qps = params.get("Qps")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ExClusterId = params.get("ExClusterId")
        self.ExClusterName = params.get("ExClusterName")


class ModifyAccountDescriptionRequest(AbstractModel):
    """ModifyAccountDescription請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        :param Accounts: 雲資料庫賬号。
        :type Accounts: list of Account
        :param Description: 資料庫賬号的備注訊息。
        :type Description: str
        """
        self.InstanceId = None
        self.Accounts = None
        self.Description = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.Description = params.get("Description")


class ModifyAccountDescriptionResponse(AbstractModel):
    """ModifyAccountDescription返回參數結構體

    """

    def __init__(self):
        """
        :param AsyncRequestId: 異步任務的請求ID，可使用此ID查詢異步任務的執行結果。
        :type AsyncRequestId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyAccountPasswordRequest(AbstractModel):
    """ModifyAccountPassword請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        :param NewPassword: 資料庫賬号的新密碼。密碼應至少包含字母、數字和字元（_+-&=!@#$%^*()）中的兩種，長度爲8-64個字元。
        :type NewPassword: str
        :param Accounts: 雲資料庫賬号。
        :type Accounts: list of Account
        """
        self.InstanceId = None
        self.NewPassword = None
        self.Accounts = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.NewPassword = params.get("NewPassword")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self.Accounts.append(obj)


class ModifyAccountPasswordResponse(AbstractModel):
    """ModifyAccountPassword返回參數結構體

    """

    def __init__(self):
        """
        :param AsyncRequestId: 異步任務的請求ID，可使用此ID查詢異步任務的執行結果。
        :type AsyncRequestId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyAccountPrivilegesRequest(AbstractModel):
    """ModifyAccountPrivileges請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        :param Accounts: 資料庫的賬号，包括用戶名和域名。
        :type Accounts: list of Account
        :param GlobalPrivileges: 全局權限。其中，GlobalPrivileges 中權限的可選值爲："SELECT","INSERT","UPDATE","DELETE","CREATE",	"DROP","REFERENCES","INDEX","ALTER","SHOW DATABASES","CREATE TEMPORARY TABLES","LOCK TABLES","EXECUTE","CREATE VIEW","SHOW VIEW","CREATE ROUTINE","ALTER ROUTINE","EVENT","TRIGGER"。
        :type GlobalPrivileges: list of str
        :param DatabasePrivileges: 資料庫的權限。Privileges權限的可選值爲："SELECT","INSERT","UPDATE","DELETE","CREATE",	"DROP","REFERENCES","INDEX","ALTER","CREATE TEMPORARY TABLES","LOCK TABLES","EXECUTE","CREATE VIEW","SHOW VIEW","CREATE ROUTINE","ALTER ROUTINE","EVENT","TRIGGER"。
        :type DatabasePrivileges: list of DatabasePrivilege
        :param TablePrivileges: 資料庫中表的權限。Privileges權限的可選值爲：權限的可選值爲："SELECT","INSERT","UPDATE","DELETE","CREATE",	"DROP","REFERENCES","INDEX","ALTER","CREATE VIEW","SHOW VIEW", "TRIGGER"。
        :type TablePrivileges: list of TablePrivilege
        :param ColumnPrivileges: 資料庫表中列的權限。Privileges權限的可選值爲："SELECT","INSERT","UPDATE","REFERENCES"。
        :type ColumnPrivileges: list of ColumnPrivilege
        """
        self.InstanceId = None
        self.Accounts = None
        self.GlobalPrivileges = None
        self.DatabasePrivileges = None
        self.TablePrivileges = None
        self.ColumnPrivileges = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.GlobalPrivileges = params.get("GlobalPrivileges")
        if params.get("DatabasePrivileges") is not None:
            self.DatabasePrivileges = []
            for item in params.get("DatabasePrivileges"):
                obj = DatabasePrivilege()
                obj._deserialize(item)
                self.DatabasePrivileges.append(obj)
        if params.get("TablePrivileges") is not None:
            self.TablePrivileges = []
            for item in params.get("TablePrivileges"):
                obj = TablePrivilege()
                obj._deserialize(item)
                self.TablePrivileges.append(obj)
        if params.get("ColumnPrivileges") is not None:
            self.ColumnPrivileges = []
            for item in params.get("ColumnPrivileges"):
                obj = ColumnPrivilege()
                obj._deserialize(item)
                self.ColumnPrivileges.append(obj)


class ModifyAccountPrivilegesResponse(AbstractModel):
    """ModifyAccountPrivileges返回參數結構體

    """

    def __init__(self):
        """
        :param AsyncRequestId: 異步任務的請求ID，可使用此ID查詢異步任務的執行結果。
        :type AsyncRequestId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyAutoRenewFlagRequest(AbstractModel):
    """ModifyAutoRenewFlag請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 實例的ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceIds: list of str
        :param AutoRenew: 自動續約标記，可取值的有：0-不自動續約，1-自動續約。
        :type AutoRenew: int
        """
        self.InstanceIds = None
        self.AutoRenew = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.AutoRenew = params.get("AutoRenew")


class ModifyAutoRenewFlagResponse(AbstractModel):
    """ModifyAutoRenewFlag返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBackupConfigRequest(AbstractModel):
    """ModifyBackupConfig請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv。與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        :param ExpireDays: 備份過期時間，單位爲天，最小值爲7天，最大值爲732天。
        :type ExpireDays: int
        :param StartTime: 備份時間範圍，格式爲：02:00-06:00，起點和終點時間目前限制爲整點，目前可以選擇的範圍爲： 02:00-06:00，06：00-10：00，10:00-14:00，14:00-18:00，18:00-22:00，22:00-02:00。
        :type StartTime: str
        :param BackupMethod: 目标備份方法，可選的值：logical - 邏輯冷備，physical - 物理冷備；預設備份方法爲 邏輯冷備。
        :type BackupMethod: str
        """
        self.InstanceId = None
        self.ExpireDays = None
        self.StartTime = None
        self.BackupMethod = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ExpireDays = params.get("ExpireDays")
        self.StartTime = params.get("StartTime")
        self.BackupMethod = params.get("BackupMethod")


class ModifyBackupConfigResponse(AbstractModel):
    """ModifyBackupConfig返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
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
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同，可使用[查詢實例清單](https://cloud.taifucloud.com/document/api/236/15872) 介面獲取，其值爲輸出參數中欄位 InstanceId 的值。
        :type InstanceId: str
        :param InstanceName: 實例名稱。
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


class ModifyDBInstanceProjectRequest(AbstractModel):
    """ModifyDBInstanceProject請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 實例ID數組，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同，可使用[查詢實例清單](https://cloud.taifucloud.com/document/api/236/15872) 介面獲取，其值爲輸出參數中欄位 InstanceId 的值。
        :type InstanceIds: list of str
        :param NewProjectId: 項目的ID。
        :type NewProjectId: int
        """
        self.InstanceIds = None
        self.NewProjectId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.NewProjectId = params.get("NewProjectId")


class ModifyDBInstanceProjectResponse(AbstractModel):
    """ModifyDBInstanceProject返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        :param SecurityGroupIds: 要修改的安全組ID清單，一個或者多個安全組Id組成的數組。
        :type SecurityGroupIds: list of str
        """
        self.InstanceId = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SecurityGroupIds = params.get("SecurityGroupIds")


class ModifyDBInstanceSecurityGroupsResponse(AbstractModel):
    """ModifyDBInstanceSecurityGroups返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceVipVportRequest(AbstractModel):
    """ModifyDBInstanceVipVport請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同，可使用[查詢實例清單](https://cloud.taifucloud.com/document/api/236/15872) 介面獲取，其值爲輸出參數中欄位 InstanceId 的值。
        :type InstanceId: str
        :param DstIp: 目标IP。該參數和DstPort參數，兩者必傳一個。
        :type DstIp: str
        :param DstPort: 目标端口，支援範圍爲：[1024-65535]。該參數和DstIp參數，兩者必傳一個。
        :type DstPort: int
        :param UniqVpcId: 私有網絡統一ID。
        :type UniqVpcId: str
        :param UniqSubnetId: 子網統一ID。
        :type UniqSubnetId: str
        """
        self.InstanceId = None
        self.DstIp = None
        self.DstPort = None
        self.UniqVpcId = None
        self.UniqSubnetId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DstIp = params.get("DstIp")
        self.DstPort = params.get("DstPort")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")


class ModifyDBInstanceVipVportResponse(AbstractModel):
    """ModifyDBInstanceVipVport返回參數結構體

    """

    def __init__(self):
        """
        :param AsyncRequestId: 異步任務ID。
        :type AsyncRequestId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyInstanceParamRequest(AbstractModel):
    """ModifyInstanceParam請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 實例短Id清單。
        :type InstanceIds: list of str
        :param ParamList: 要修改的參數清單。每一個元素是name和currentValue的組合。name是參數名，currentValue是要修改成的值。
        :type ParamList: list of Parameter
        """
        self.InstanceIds = None
        self.ParamList = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("ParamList") is not None:
            self.ParamList = []
            for item in params.get("ParamList"):
                obj = Parameter()
                obj._deserialize(item)
                self.ParamList.append(obj)


class ModifyInstanceParamResponse(AbstractModel):
    """ModifyInstanceParam返回參數結構體

    """

    def __init__(self):
        """
        :param AsyncRequestId: 異步任務Id，可用于查詢任務進度。
        :type AsyncRequestId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyInstanceTagRequest(AbstractModel):
    """ModifyInstanceTag請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param ReplaceTags: 要增加或修改的标簽
        :type ReplaceTags: list of TagInfo
        :param DeleteTags: 要删除的标簽
        :type DeleteTags: list of TagInfo
        """
        self.InstanceId = None
        self.ReplaceTags = None
        self.DeleteTags = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("ReplaceTags") is not None:
            self.ReplaceTags = []
            for item in params.get("ReplaceTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.ReplaceTags.append(obj)
        if params.get("DeleteTags") is not None:
            self.DeleteTags = []
            for item in params.get("DeleteTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.DeleteTags.append(obj)


class ModifyInstanceTagResponse(AbstractModel):
    """ModifyInstanceTag返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyParamTemplateRequest(AbstractModel):
    """ModifyParamTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param TemplateId: 範本Id。
        :type TemplateId: int
        :param Name: 範本名稱。
        :type Name: str
        :param Description: 範本描述。
        :type Description: str
        :param ParamList: 參數清單。
        :type ParamList: list of Parameter
        """
        self.TemplateId = None
        self.Name = None
        self.Description = None
        self.ParamList = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("ParamList") is not None:
            self.ParamList = []
            for item in params.get("ParamList"):
                obj = Parameter()
                obj._deserialize(item)
                self.ParamList.append(obj)


class ModifyParamTemplateResponse(AbstractModel):
    """ModifyParamTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTimeWindowRequest(AbstractModel):
    """ModifyTimeWindow請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        :param TimeRanges: 修改後的可維護時間段，其中每一個時間段的格式形如：10:00-12:00；起止時間按半個小時對齊；最短半個小時，最長三個小時；最多設置兩個時間段；起止時間範圍爲：[00:00, 24:00]。
        :type TimeRanges: list of str
        :param Weekdays: 指定修改哪一天的客戶時間段，可能的取值爲：monday, tuesday, wednesday, thursday, friday, saturday, sunday。如果不指定該值或者爲空，則預設一周七天都修改。
        :type Weekdays: list of str
        """
        self.InstanceId = None
        self.TimeRanges = None
        self.Weekdays = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TimeRanges = params.get("TimeRanges")
        self.Weekdays = params.get("Weekdays")


class ModifyTimeWindowResponse(AbstractModel):
    """ModifyTimeWindow返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OpenDBInstanceGTIDRequest(AbstractModel):
    """OpenDBInstanceGTID請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class OpenDBInstanceGTIDResponse(AbstractModel):
    """OpenDBInstanceGTID返回參數結構體

    """

    def __init__(self):
        """
        :param AsyncRequestId: 異步任務的請求ID，可使用此ID查詢異步任務的執行結果。
        :type AsyncRequestId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class OpenWanServiceRequest(AbstractModel):
    """OpenWanService請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同，可使用[查詢實例清單](https://cloud.taifucloud.com/document/api/236/15872) 介面獲取，其值爲輸出參數中欄位 InstanceId 的值
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class OpenWanServiceResponse(AbstractModel):
    """OpenWanService返回參數結構體

    """

    def __init__(self):
        """
        :param AsyncRequestId: 異步任務的請求ID，可使用此ID查詢異步任務的執行結果
        :type AsyncRequestId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class Outbound(AbstractModel):
    """安全組出站規則

    """

    def __init__(self):
        """
        :param Action: 策略，ACCEPT或者DROP
        :type Action: str
        :param CidrIp: 目的Ip或Ip段，例如172.16.0.0/12
        :type CidrIp: str
        :param PortRange: 端口或者端口範圍
        :type PortRange: str
        :param IpProtocol: 網絡協議，支援udp、tcp等
        :type IpProtocol: str
        :param Dir: 規則限定的方向，進站規則爲OUTPUT
        :type Dir: str
        """
        self.Action = None
        self.CidrIp = None
        self.PortRange = None
        self.IpProtocol = None
        self.Dir = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.CidrIp = params.get("CidrIp")
        self.PortRange = params.get("PortRange")
        self.IpProtocol = params.get("IpProtocol")
        self.Dir = params.get("Dir")


class ParamInfo(AbstractModel):
    """實例參數訊息

    """

    def __init__(self):
        """
        :param Name: 參數名
        :type Name: str
        :param Value: 參數值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class ParamRecord(AbstractModel):
    """參數修改記錄

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param ParamName: 參數名稱
        :type ParamName: str
        :param OldValue: 參數修改前的值
        :type OldValue: str
        :param NewValue: 參數修改後的值
        :type NewValue: str
        :param IsSucess: 參數是否修改成功
        :type IsSucess: bool
        :param ModifyTime: 修改時間
        :type ModifyTime: str
        """
        self.InstanceId = None
        self.ParamName = None
        self.OldValue = None
        self.NewValue = None
        self.IsSucess = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ParamName = params.get("ParamName")
        self.OldValue = params.get("OldValue")
        self.NewValue = params.get("NewValue")
        self.IsSucess = params.get("IsSucess")
        self.ModifyTime = params.get("ModifyTime")


class ParamTemplateInfo(AbstractModel):
    """參數範本訊息

    """

    def __init__(self):
        """
        :param TemplateId: 參數範本ID
        :type TemplateId: int
        :param Name: 參數範本名稱
        :type Name: str
        :param Description: 參數範本描述
        :type Description: str
        :param EngineVersion: 實例引擎版本
        :type EngineVersion: str
        """
        self.TemplateId = None
        self.Name = None
        self.Description = None
        self.EngineVersion = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.EngineVersion = params.get("EngineVersion")


class Parameter(AbstractModel):
    """資料庫實例參數

    """

    def __init__(self):
        """
        :param Name: 參數名稱
        :type Name: str
        :param CurrentValue: 參數值
        :type CurrentValue: str
        """
        self.Name = None
        self.CurrentValue = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.CurrentValue = params.get("CurrentValue")


class ParameterDetail(AbstractModel):
    """實例參數的詳細描述

    """

    def __init__(self):
        """
        :param Name: 參數名稱
        :type Name: str
        :param ParamType: 參數類型
        :type ParamType: str
        :param Default: 參數預設值
        :type Default: str
        :param Description: 參數描述
        :type Description: str
        :param CurrentValue: 參數當前值
        :type CurrentValue: str
        :param NeedReboot: 修改參數後，是否需要重啓資料庫以使參數生效。可能的值包括：0-不需要重啓；1-需要重啓
        :type NeedReboot: int
        :param Max: 參數允許的最大值
        :type Max: int
        :param Min: 參數允許的最小值
        :type Min: int
        :param EnumValue: 參數的可選列舉值。如果爲非列舉參數，則爲空
        :type EnumValue: list of str
        """
        self.Name = None
        self.ParamType = None
        self.Default = None
        self.Description = None
        self.CurrentValue = None
        self.NeedReboot = None
        self.Max = None
        self.Min = None
        self.EnumValue = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ParamType = params.get("ParamType")
        self.Default = params.get("Default")
        self.Description = params.get("Description")
        self.CurrentValue = params.get("CurrentValue")
        self.NeedReboot = params.get("NeedReboot")
        self.Max = params.get("Max")
        self.Min = params.get("Min")
        self.EnumValue = params.get("EnumValue")


class RegionSellConf(AbstractModel):
    """地域售賣配置

    """

    def __init__(self):
        """
        :param RegionName: 地域中文名稱
        :type RegionName: str
        :param Area: 所屬大區
        :type Area: str
        :param IsDefaultRegion: 是否爲預設地域
        :type IsDefaultRegion: int
        :param Region: 地域名稱
        :type Region: str
        :param ZonesConf: 可用區售賣配置
        :type ZonesConf: list of ZoneSellConf
        """
        self.RegionName = None
        self.Area = None
        self.IsDefaultRegion = None
        self.Region = None
        self.ZonesConf = None


    def _deserialize(self, params):
        self.RegionName = params.get("RegionName")
        self.Area = params.get("Area")
        self.IsDefaultRegion = params.get("IsDefaultRegion")
        self.Region = params.get("Region")
        if params.get("ZonesConf") is not None:
            self.ZonesConf = []
            for item in params.get("ZonesConf"):
                obj = ZoneSellConf()
                obj._deserialize(item)
                self.ZonesConf.append(obj)


class RenewDBInstanceRequest(AbstractModel):
    """RenewDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 待續約的實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同，可使用[查詢實例清單](https://cloud.taifucloud.com/document/api/236/15872)
        :type InstanceId: str
        :param TimeSpan: 續約時長，單位：月，可選值包括[1,2,3,4,5,6,7,8,9,10,11,12,24,36]
        :type TimeSpan: int
        """
        self.InstanceId = None
        self.TimeSpan = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TimeSpan = params.get("TimeSpan")


class RenewDBInstanceResponse(AbstractModel):
    """RenewDBInstance返回參數結構體

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


class RestartDBInstancesRequest(AbstractModel):
    """RestartDBInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 實例ID數組，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class RestartDBInstancesResponse(AbstractModel):
    """RestartDBInstances返回參數結構體

    """

    def __init__(self):
        """
        :param AsyncRequestId: 異步任務的請求ID，可使用此ID查詢異步任務的執行結果。
        :type AsyncRequestId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class RoGroup(AbstractModel):
    """只讀組參數

    """

    def __init__(self):
        """
        :param RoGroupMode: 只讀組模式，可選值爲：alone-系統自動分配只讀組；allinone-新建只讀組；join-使用現有只讀組
        :type RoGroupMode: str
        :param RoGroupId: 只讀組ID
        :type RoGroupId: str
        :param RoGroupName: 只讀組名稱
        :type RoGroupName: str
        :param RoOfflineDelay: 是否啓用延遲超限剔除功能，啓用該功能後，只讀實例與主實例的延遲超過延遲阈值，只讀實例将被隔離。可選值：1-啓用；0-不啓用
        :type RoOfflineDelay: int
        :param RoMaxDelayTime: 延遲阈值
        :type RoMaxDelayTime: int
        :param MinRoInGroup: 最少實例保留個數，若購買只讀實例數量小於設置數量将不做剔除
        :type MinRoInGroup: int
        :param WeightMode: 讀寫權重分配模式，可選值：system-系統自動分配；custom-自定義
        :type WeightMode: str
        :param Weight: 權重值
        :type Weight: int
        :param RoInstances: 只讀組中的只讀實例詳情
        :type RoInstances: list of RoInstanceInfo
        :param Vip: 只讀組的内網IP
        :type Vip: str
        :param Vport: 只讀組的内網端口号
        :type Vport: int
        """
        self.RoGroupMode = None
        self.RoGroupId = None
        self.RoGroupName = None
        self.RoOfflineDelay = None
        self.RoMaxDelayTime = None
        self.MinRoInGroup = None
        self.WeightMode = None
        self.Weight = None
        self.RoInstances = None
        self.Vip = None
        self.Vport = None


    def _deserialize(self, params):
        self.RoGroupMode = params.get("RoGroupMode")
        self.RoGroupId = params.get("RoGroupId")
        self.RoGroupName = params.get("RoGroupName")
        self.RoOfflineDelay = params.get("RoOfflineDelay")
        self.RoMaxDelayTime = params.get("RoMaxDelayTime")
        self.MinRoInGroup = params.get("MinRoInGroup")
        self.WeightMode = params.get("WeightMode")
        self.Weight = params.get("Weight")
        if params.get("RoInstances") is not None:
            self.RoInstances = []
            for item in params.get("RoInstances"):
                obj = RoInstanceInfo()
                obj._deserialize(item)
                self.RoInstances.append(obj)
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")


class RoInstanceInfo(AbstractModel):
    """RO實例的詳細訊息

    """

    def __init__(self):
        """
        :param MasterInstanceId: RO組對應的主實例的ID
        :type MasterInstanceId: str
        :param RoStatus: RO實例在RO組内的狀态，可能的值：online-在線，offline-下線
        :type RoStatus: str
        :param OfflineTime: RO實例在RO組内上一次下線的時間
        :type OfflineTime: str
        :param Weight: RO實例在RO組内的權重
        :type Weight: int
        :param Region: RO實例所在區域名稱，如ap-shanghai
        :type Region: str
        :param Zone: RO可用區的正式名稱，如ap-shanghai-1
        :type Zone: str
        :param InstanceId: RO實例ID，格式如：cdbro-c1nl9rpv
        :type InstanceId: str
        :param Status: RO實例狀态，可能返回值：0-創建中，1-運作中，4-删除中
        :type Status: int
        :param InstanceType: 實例類型，可能返回值：1-主實例，2-災備實例，3-只讀實例
        :type InstanceType: int
        :param InstanceName: RO實例名稱
        :type InstanceName: str
        :param HourFeeStatus: 按量計費狀态，可能的取值：1-正常，2-欠費
        :type HourFeeStatus: int
        :param TaskStatus: RO實例任務狀态，可能返回值：<br>0-沒有任務<br>1-升級中<br>2-數據導入中<br>3-開放Slave中<br>4-外網訪問開通中<br>5-批次操作執行中<br>6-回檔中<br>7-外網訪問關閉中<br>8-密碼修改中<br>9-實例名修改中<br>10-重啓中<br>12-自建遷移中<br>13-删除庫表中<br>14-災備實例創建同步中
        :type TaskStatus: int
        :param Memory: RO實例内存大小，單位：MB
        :type Memory: int
        :param Volume: RO實例硬碟大小，單位：GB
        :type Volume: int
        :param Qps: 每次查詢數量
        :type Qps: int
        :param Vip: RO實例的内網IP網址
        :type Vip: str
        :param Vport: RO實例訪問端口
        :type Vport: int
        :param VpcId: RO實例所在私有網絡ID
        :type VpcId: int
        :param SubnetId: RO實例所在私有網絡子網ID
        :type SubnetId: int
        :param DeviceType: RO實例規格描述，目前可取值 CUSTOM
        :type DeviceType: str
        :param EngineVersion: RO實例資料庫引擎版本，可能返回值：5.1、5.5、5.6和5.7
        :type EngineVersion: str
        :param DeadlineTime: RO實例到期時間，時間格式：yyyy-mm-dd hh:mm:ss，如實例爲按量計費模式，則此欄位值爲0000-00-00 00:00:00
        :type DeadlineTime: str
        :param PayType: RO實例計費類型，可能返回值：0-包年包月，1-按量計費，2-後付費月結
        :type PayType: int
        """
        self.MasterInstanceId = None
        self.RoStatus = None
        self.OfflineTime = None
        self.Weight = None
        self.Region = None
        self.Zone = None
        self.InstanceId = None
        self.Status = None
        self.InstanceType = None
        self.InstanceName = None
        self.HourFeeStatus = None
        self.TaskStatus = None
        self.Memory = None
        self.Volume = None
        self.Qps = None
        self.Vip = None
        self.Vport = None
        self.VpcId = None
        self.SubnetId = None
        self.DeviceType = None
        self.EngineVersion = None
        self.DeadlineTime = None
        self.PayType = None


    def _deserialize(self, params):
        self.MasterInstanceId = params.get("MasterInstanceId")
        self.RoStatus = params.get("RoStatus")
        self.OfflineTime = params.get("OfflineTime")
        self.Weight = params.get("Weight")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.InstanceId = params.get("InstanceId")
        self.Status = params.get("Status")
        self.InstanceType = params.get("InstanceType")
        self.InstanceName = params.get("InstanceName")
        self.HourFeeStatus = params.get("HourFeeStatus")
        self.TaskStatus = params.get("TaskStatus")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.Qps = params.get("Qps")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.DeviceType = params.get("DeviceType")
        self.EngineVersion = params.get("EngineVersion")
        self.DeadlineTime = params.get("DeadlineTime")
        self.PayType = params.get("PayType")


class RoVipInfo(AbstractModel):
    """只讀vip訊息

    """

    def __init__(self):
        """
        :param RoVipStatus: 只讀vip狀态
        :type RoVipStatus: int
        :param RoSubnetId: 只讀vip的子網
        :type RoSubnetId: int
        :param RoVpcId: 只讀vip的私有網絡
        :type RoVpcId: int
        :param RoVport: 只讀vip的端口号
        :type RoVport: int
        :param RoVip: 只讀vip
        :type RoVip: str
        """
        self.RoVipStatus = None
        self.RoSubnetId = None
        self.RoVpcId = None
        self.RoVport = None
        self.RoVip = None


    def _deserialize(self, params):
        self.RoVipStatus = params.get("RoVipStatus")
        self.RoSubnetId = params.get("RoSubnetId")
        self.RoVpcId = params.get("RoVpcId")
        self.RoVport = params.get("RoVport")
        self.RoVip = params.get("RoVip")


class RollbackDBName(AbstractModel):
    """用于回檔的資料庫名

    """

    def __init__(self):
        """
        :param DatabaseName: 回檔前的原資料庫名
        :type DatabaseName: str
        :param NewDatabaseName: 回檔後的新資料庫名
        :type NewDatabaseName: str
        """
        self.DatabaseName = None
        self.NewDatabaseName = None


    def _deserialize(self, params):
        self.DatabaseName = params.get("DatabaseName")
        self.NewDatabaseName = params.get("NewDatabaseName")


class RollbackInstancesInfo(AbstractModel):
    """用于回檔的實例詳情

    """

    def __init__(self):
        """
        :param InstanceId: 雲資料庫實例ID
        :type InstanceId: str
        :param Strategy: 回檔策略。可選值爲：table、db、full；預設值爲full。table - 急速回檔模式，僅導入所選中表級别的備份和binlog，如有跨表操作，且關聯表未被同時選中，将會導緻回檔失敗，該模式下參數Databases必須爲空；db - 快速模式，僅導入所選中庫級别的備份和binlog，如有跨庫操作，且關聯庫未被同時選中，将會導緻回檔失敗；full - 普通回檔模式，将導入整個實例的備份和binlog，速度較慢。
        :type Strategy: str
        :param RollbackTime: 資料庫回檔時間，時間格式爲：yyyy-mm-dd hh:mm:ss
        :type RollbackTime: str
        :param Databases: 待回檔的資料庫訊息，表示整庫回檔
        :type Databases: list of RollbackDBName
        :param Tables: 待回檔的資料庫表訊息，表示按表回檔
        :type Tables: list of RollbackTables
        """
        self.InstanceId = None
        self.Strategy = None
        self.RollbackTime = None
        self.Databases = None
        self.Tables = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Strategy = params.get("Strategy")
        self.RollbackTime = params.get("RollbackTime")
        if params.get("Databases") is not None:
            self.Databases = []
            for item in params.get("Databases"):
                obj = RollbackDBName()
                obj._deserialize(item)
                self.Databases.append(obj)
        if params.get("Tables") is not None:
            self.Tables = []
            for item in params.get("Tables"):
                obj = RollbackTables()
                obj._deserialize(item)
                self.Tables.append(obj)


class RollbackTableName(AbstractModel):
    """用于回檔的資料庫表名

    """

    def __init__(self):
        """
        :param TableName: 回檔前的原資料庫表名
        :type TableName: str
        :param NewTableName: 回檔後的新資料庫表名
        :type NewTableName: str
        """
        self.TableName = None
        self.NewTableName = None


    def _deserialize(self, params):
        self.TableName = params.get("TableName")
        self.NewTableName = params.get("NewTableName")


class RollbackTables(AbstractModel):
    """用于回檔的資料庫表詳情

    """

    def __init__(self):
        """
        :param Database: 資料庫名
        :type Database: str
        :param Table: 資料庫表詳情
        :type Table: list of RollbackTableName
        """
        self.Database = None
        self.Table = None


    def _deserialize(self, params):
        self.Database = params.get("Database")
        if params.get("Table") is not None:
            self.Table = []
            for item in params.get("Table"):
                obj = RollbackTableName()
                obj._deserialize(item)
                self.Table.append(obj)


class RollbackTimeRange(AbstractModel):
    """可回檔時間範圍

    """

    def __init__(self):
        """
        :param Begin: 實例可回檔開始時間，時間格式：2016-10-29 01:06:04
        :type Begin: str
        :param End: 實例可回檔結束時間，時間格式：2016-11-02 11:44:47
        :type End: str
        """
        self.Begin = None
        self.End = None


    def _deserialize(self, params):
        self.Begin = params.get("Begin")
        self.End = params.get("End")


class SecurityGroup(AbstractModel):
    """安全組詳情

    """

    def __init__(self):
        """
        :param ProjectId: 項目ID
        :type ProjectId: int
        :param CreateTime: 創建時間，時間格式：yyyy-mm-dd hh:mm:ss
        :type CreateTime: str
        :param Inbound: 入站規則
        :type Inbound: list of Inbound
        :param Outbound: 出站規則
        :type Outbound: list of Outbound
        :param SecurityGroupId: 安全組ID
        :type SecurityGroupId: str
        :param SecurityGroupName: 安全組名稱
        :type SecurityGroupName: str
        :param SecurityGroupRemark: 安全組備注
        :type SecurityGroupRemark: str
        """
        self.ProjectId = None
        self.CreateTime = None
        self.Inbound = None
        self.Outbound = None
        self.SecurityGroupId = None
        self.SecurityGroupName = None
        self.SecurityGroupRemark = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.CreateTime = params.get("CreateTime")
        if params.get("Inbound") is not None:
            self.Inbound = []
            for item in params.get("Inbound"):
                obj = Inbound()
                obj._deserialize(item)
                self.Inbound.append(obj)
        if params.get("Outbound") is not None:
            self.Outbound = []
            for item in params.get("Outbound"):
                obj = Outbound()
                obj._deserialize(item)
                self.Outbound.append(obj)
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.SecurityGroupName = params.get("SecurityGroupName")
        self.SecurityGroupRemark = params.get("SecurityGroupRemark")


class SellConfig(AbstractModel):
    """售賣配置詳情

    """

    def __init__(self):
        """
        :param Device: 設備類型
        :type Device: str
        :param Type: 售賣規格描述
        :type Type: str
        :param CdbType: 實例類型
        :type CdbType: str
        :param Memory: 内存大小，單位爲MB
        :type Memory: int
        :param Cpu: CPU核心數
        :type Cpu: int
        :param VolumeMin: 磁盤最小規格，單位爲GB
        :type VolumeMin: int
        :param VolumeMax: 磁盤最大規格，單位爲GB
        :type VolumeMax: int
        :param VolumeStep: 磁盤步長，單位爲GB
        :type VolumeStep: int
        :param Connection: 連結數
        :type Connection: int
        :param Qps: 每秒查詢數量
        :type Qps: int
        :param Iops: 每秒IO數量
        :type Iops: int
        :param Info: 應用場景描述
        :type Info: str
        :param Status: 狀态值
        :type Status: int
        """
        self.Device = None
        self.Type = None
        self.CdbType = None
        self.Memory = None
        self.Cpu = None
        self.VolumeMin = None
        self.VolumeMax = None
        self.VolumeStep = None
        self.Connection = None
        self.Qps = None
        self.Iops = None
        self.Info = None
        self.Status = None


    def _deserialize(self, params):
        self.Device = params.get("Device")
        self.Type = params.get("Type")
        self.CdbType = params.get("CdbType")
        self.Memory = params.get("Memory")
        self.Cpu = params.get("Cpu")
        self.VolumeMin = params.get("VolumeMin")
        self.VolumeMax = params.get("VolumeMax")
        self.VolumeStep = params.get("VolumeStep")
        self.Connection = params.get("Connection")
        self.Qps = params.get("Qps")
        self.Iops = params.get("Iops")
        self.Info = params.get("Info")
        self.Status = params.get("Status")


class SellType(AbstractModel):
    """售賣實例類型

    """

    def __init__(self):
        """
        :param TypeName: 售賣實例名稱
        :type TypeName: str
        :param EngineVersion: 内核版本号
        :type EngineVersion: list of str
        :param Configs: 售賣規格詳細配置
        :type Configs: list of SellConfig
        """
        self.TypeName = None
        self.EngineVersion = None
        self.Configs = None


    def _deserialize(self, params):
        self.TypeName = params.get("TypeName")
        self.EngineVersion = params.get("EngineVersion")
        if params.get("Configs") is not None:
            self.Configs = []
            for item in params.get("Configs"):
                obj = SellConfig()
                obj._deserialize(item)
                self.Configs.append(obj)


class SlaveConfig(AbstractModel):
    """從庫的配置訊息

    """

    def __init__(self):
        """
        :param ReplicationMode: 從庫複制方式，可能的返回值：aysnc-異步，semisync-半同步
        :type ReplicationMode: str
        :param Zone: 從庫可用區的正式名稱，如ap-shanghai-1
        :type Zone: str
        """
        self.ReplicationMode = None
        self.Zone = None


    def _deserialize(self, params):
        self.ReplicationMode = params.get("ReplicationMode")
        self.Zone = params.get("Zone")


class SlaveInfo(AbstractModel):
    """備機訊息

    """

    def __init__(self):
        """
        :param First: 第一備機訊息
        :type First: :class:`taifucloudcloud.cdb.v20170320.models.SlaveInstanceInfo`
        :param Second: 第二備機訊息
        :type Second: :class:`taifucloudcloud.cdb.v20170320.models.SlaveInstanceInfo`
        """
        self.First = None
        self.Second = None


    def _deserialize(self, params):
        if params.get("First") is not None:
            self.First = SlaveInstanceInfo()
            self.First._deserialize(params.get("First"))
        if params.get("Second") is not None:
            self.Second = SlaveInstanceInfo()
            self.Second._deserialize(params.get("Second"))


class SlaveInstanceInfo(AbstractModel):
    """備機訊息

    """

    def __init__(self):
        """
        :param Vport: 端口号
        :type Vport: int
        :param Region: 地域訊息
        :type Region: str
        :param Vip: 虛拟Ip訊息
        :type Vip: str
        :param Zone: 可用區訊息
        :type Zone: str
        """
        self.Vport = None
        self.Region = None
        self.Vip = None
        self.Zone = None


    def _deserialize(self, params):
        self.Vport = params.get("Vport")
        self.Region = params.get("Region")
        self.Vip = params.get("Vip")
        self.Zone = params.get("Zone")


class SlowLogInfo(AbstractModel):
    """慢查詢日志詳情

    """

    def __init__(self):
        """
        :param Name: 備份文件名
        :type Name: str
        :param Size: 備份文件大小，單位：Byte
        :type Size: int
        :param Date: 備份快照時間，時間格式：2016-03-17 02:10:37
        :type Date: str
        :param IntranetUrl: 内網下載網址
        :type IntranetUrl: str
        :param InternetUrl: 外網下載網址
        :type InternetUrl: str
        :param Type: 日志具體類型，可能的值：slowlog - 慢日志
        :type Type: str
        """
        self.Name = None
        self.Size = None
        self.Date = None
        self.IntranetUrl = None
        self.InternetUrl = None
        self.Type = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Size = params.get("Size")
        self.Date = params.get("Date")
        self.IntranetUrl = params.get("IntranetUrl")
        self.InternetUrl = params.get("InternetUrl")
        self.Type = params.get("Type")


class SqlFileInfo(AbstractModel):
    """sql文件訊息

    """

    def __init__(self):
        """
        :param UploadTime: 上傳時間
        :type UploadTime: str
        :param UploadInfo: 上傳進度
        :type UploadInfo: :class:`taifucloudcloud.cdb.v20170320.models.UploadInfo`
        :param FileName: 文件名
        :type FileName: str
        :param FileSize: 文件大小，單位爲Bytes
        :type FileSize: int
        :param IsUploadFinished: 上傳是否完成标志，可選值：0 - 未完成，1 - 已完成
        :type IsUploadFinished: int
        :param FileId: 文件ID
        :type FileId: str
        """
        self.UploadTime = None
        self.UploadInfo = None
        self.FileName = None
        self.FileSize = None
        self.IsUploadFinished = None
        self.FileId = None


    def _deserialize(self, params):
        self.UploadTime = params.get("UploadTime")
        if params.get("UploadInfo") is not None:
            self.UploadInfo = UploadInfo()
            self.UploadInfo._deserialize(params.get("UploadInfo"))
        self.FileName = params.get("FileName")
        self.FileSize = params.get("FileSize")
        self.IsUploadFinished = params.get("IsUploadFinished")
        self.FileId = params.get("FileId")


class StartBatchRollbackRequest(AbstractModel):
    """StartBatchRollback請求參數結構體

    """

    def __init__(self):
        """
        :param Instances: 用于回檔的實例詳情訊息
        :type Instances: list of RollbackInstancesInfo
        """
        self.Instances = None


    def _deserialize(self, params):
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = RollbackInstancesInfo()
                obj._deserialize(item)
                self.Instances.append(obj)


class StartBatchRollbackResponse(AbstractModel):
    """StartBatchRollback返回參數結構體

    """

    def __init__(self):
        """
        :param AsyncRequestId: 異步任務的請求ID，可使用此ID查詢異步任務的執行結果
        :type AsyncRequestId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class StopDBImportJobRequest(AbstractModel):
    """StopDBImportJob請求參數結構體

    """

    def __init__(self):
        """
        :param AsyncRequestId: 異步任務的請求ID。
        :type AsyncRequestId: str
        """
        self.AsyncRequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")


class StopDBImportJobResponse(AbstractModel):
    """StopDBImportJob返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SwitchForUpgradeRequest(AbstractModel):
    """SwitchForUpgrade請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class SwitchForUpgradeResponse(AbstractModel):
    """SwitchForUpgrade返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TableName(AbstractModel):
    """表名

    """

    def __init__(self):
        """
        :param TableName: 表名
        :type TableName: str
        """
        self.TableName = None


    def _deserialize(self, params):
        self.TableName = params.get("TableName")


class TablePrivilege(AbstractModel):
    """資料庫表權限

    """

    def __init__(self):
        """
        :param Database: 資料庫名
        :type Database: str
        :param Table: 資料庫表名
        :type Table: str
        :param Privileges: 權限訊息
        :type Privileges: list of str
        """
        self.Database = None
        self.Table = None
        self.Privileges = None


    def _deserialize(self, params):
        self.Database = params.get("Database")
        self.Table = params.get("Table")
        self.Privileges = params.get("Privileges")


class TagInfo(AbstractModel):
    """标簽訊息

    """

    def __init__(self):
        """
        :param TagKey: 标簽鍵
        :type TagKey: str
        :param TagValue: 标簽值
        :type TagValue: list of str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class TagInfoUnit(AbstractModel):
    """tag訊息單元

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


class TagsInfoOfInstance(AbstractModel):
    """實例的标簽訊息

    """

    def __init__(self):
        """
        :param InstanceId: 實例Id
        :type InstanceId: str
        :param Tags: 标簽訊息
        :type Tags: list of TagInfoUnit
        """
        self.InstanceId = None
        self.Tags = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfoUnit()
                obj._deserialize(item)
                self.Tags.append(obj)


class UpgradeDBInstanceEngineVersionRequest(AbstractModel):
    """UpgradeDBInstanceEngineVersion請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv。與雲資料庫控制台頁面中顯示的實例ID相同，可使用[查詢實例清單](https://cloud.taifucloud.com/document/api/236/15872) 介面獲取，其值爲輸出參數中欄位 InstanceId 的值
        :type InstanceId: str
        :param EngineVersion: 主實例資料庫引擎版本，支援值包括：5.6和5.7
        :type EngineVersion: str
        :param WaitSwitch: 切換訪問新實例的方式，預設爲0。支援值包括：0-立刻切換，1-時間窗切換；當該值爲1時，升級中過程中，切換訪問新實例的流程将會在時間窗内進行，或者用戶主動調用介面[切換訪問新實例](https://cloud.taifucloud.com/document/product/236/15864)觸發該流程
        :type WaitSwitch: int
        """
        self.InstanceId = None
        self.EngineVersion = None
        self.WaitSwitch = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.EngineVersion = params.get("EngineVersion")
        self.WaitSwitch = params.get("WaitSwitch")


class UpgradeDBInstanceEngineVersionResponse(AbstractModel):
    """UpgradeDBInstanceEngineVersion返回參數結構體

    """

    def __init__(self):
        """
        :param AsyncRequestId: 異步任務ID，可使用[查詢異步任務的執行結果](https://cloud.taifucloud.com/document/api/236/20410)獲取其執行情況。
        :type AsyncRequestId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class UpgradeDBInstanceRequest(AbstractModel):
    """UpgradeDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv。與雲資料庫控制台頁面中顯示的實例ID相同，可使用[查詢實例清單](https://cloud.taifucloud.com/document/api/236/15872) 介面獲取，其值爲輸出參數中欄位 InstanceId 的值
        :type InstanceId: str
        :param Memory: 升級後的内存大小，單位：MB，爲保證傳入 Memory 值有效，請使用[獲取雲資料庫可售賣規格](https://cloud.taifucloud.com/document/product/236/17229)介面獲取可升級的内存規格
        :type Memory: int
        :param Volume: 升級後的硬碟大小，單位：GB，爲保證傳入 Volume 值有效，請使用[獲取雲資料庫可售賣規格](https://cloud.taifucloud.com/document/product/236/17229)介面獲取可升級的硬碟範圍
        :type Volume: int
        :param ProtectMode: 數據複制方式，支援值包括：0-異步複制，1-半同步複制，2-強同步複制，升級主實例時可指定該參數，升級只讀實例或者災備實例時指定該參數無意義
        :type ProtectMode: int
        :param DeployMode: 佈署模式，預設爲0，支援值包括：0-單可用區佈署，1-多可用區佈署，升級主實例時可指定該參數，升級只讀實例或者災備實例時指定該參數無意義
        :type DeployMode: int
        :param SlaveZone: 備庫1的可用區訊息，預設和實例的Zone參數一緻，升級主實例爲多可用區佈署時可指定該參數，升級只讀實例或者災備實例時指定該參數無意義。可通過[獲取雲資料庫可售賣規格](https://cloud.taifucloud.com/document/product/236/17229)介面查詢支援的可用區
        :type SlaveZone: str
        :param EngineVersion: 主實例資料庫引擎版本，支援值包括：5.5、5.6和5.7
        :type EngineVersion: str
        :param WaitSwitch: 切換訪問新實例的方式，預設爲0。支援值包括：0-立刻切換，1-時間窗切換；當該值爲1時，升級中過程中，切換訪問新實例的流程将會在時間窗内進行，或者用戶主動調用介面[切換訪問新實例](https://cloud.taifucloud.com/document/product/236/15864)觸發該流程
        :type WaitSwitch: int
        :param BackupZone: 備庫2的可用區ID，預設爲0，升級主實例時可指定該參數，升級只讀實例或者災備實例時指定該參數無意義
        :type BackupZone: str
        :param InstanceRole: 實例類型，預設爲 master，支援值包括：master-表示主實例，dr-表示災備實例，ro-表示只讀實例
        :type InstanceRole: str
        """
        self.InstanceId = None
        self.Memory = None
        self.Volume = None
        self.ProtectMode = None
        self.DeployMode = None
        self.SlaveZone = None
        self.EngineVersion = None
        self.WaitSwitch = None
        self.BackupZone = None
        self.InstanceRole = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.ProtectMode = params.get("ProtectMode")
        self.DeployMode = params.get("DeployMode")
        self.SlaveZone = params.get("SlaveZone")
        self.EngineVersion = params.get("EngineVersion")
        self.WaitSwitch = params.get("WaitSwitch")
        self.BackupZone = params.get("BackupZone")
        self.InstanceRole = params.get("InstanceRole")


class UpgradeDBInstanceResponse(AbstractModel):
    """UpgradeDBInstance返回參數結構體

    """

    def __init__(self):
        """
        :param DealIds: 訂單ID
        :type DealIds: list of str
        :param AsyncRequestId: 異步任務的請求ID，可使用此ID查詢異步任務的執行結果
        :type AsyncRequestId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DealIds = None
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealIds = params.get("DealIds")
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class UploadInfo(AbstractModel):
    """文件上傳描述

    """

    def __init__(self):
        """
        :param AllSliceNum: 文件所有分片數
        :type AllSliceNum: int
        :param CompleteNum: 已完成分片數
        :type CompleteNum: int
        """
        self.AllSliceNum = None
        self.CompleteNum = None


    def _deserialize(self, params):
        self.AllSliceNum = params.get("AllSliceNum")
        self.CompleteNum = params.get("CompleteNum")


class VerifyRootAccountRequest(AbstractModel):
    """VerifyRootAccount請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cdb-c1nl9rpv，與雲資料庫控制台頁面中顯示的實例ID相同。
        :type InstanceId: str
        :param Password: 實例ROOT賬号的密碼。
        :type Password: str
        """
        self.InstanceId = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Password = params.get("Password")


class VerifyRootAccountResponse(AbstractModel):
    """VerifyRootAccount返回參數結構體

    """

    def __init__(self):
        """
        :param AsyncRequestId: 異步任務的請求ID，可使用此ID查詢異步任務的執行結果
        :type AsyncRequestId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ZoneConf(AbstractModel):
    """多可用區訊息

    """

    def __init__(self):
        """
        :param DeployMode: 可用區佈署方式，可能的值爲：0-單可用區；1-多可用區
        :type DeployMode: list of int
        :param MasterZone: 主實例所在的可用區
        :type MasterZone: list of str
        :param SlaveZone: 實例爲多可用區佈署時，備庫1所在的可用區
        :type SlaveZone: list of str
        :param BackupZone: 實例爲多可用區佈署時，備庫2所在的可用區
        :type BackupZone: list of str
        """
        self.DeployMode = None
        self.MasterZone = None
        self.SlaveZone = None
        self.BackupZone = None


    def _deserialize(self, params):
        self.DeployMode = params.get("DeployMode")
        self.MasterZone = params.get("MasterZone")
        self.SlaveZone = params.get("SlaveZone")
        self.BackupZone = params.get("BackupZone")


class ZoneSellConf(AbstractModel):
    """可用區售賣配置

    """

    def __init__(self):
        """
        :param Status: 可用區狀态。可能的返回值爲：0-未上線；1-上線；2-開放；3-停售；4-不展示
        :type Status: int
        :param ZoneName: 可用區中文名稱
        :type ZoneName: str
        :param IsCustom: 實例類型是否爲自定義類型
        :type IsCustom: bool
        :param IsSupportDr: 是否支援災備
        :type IsSupportDr: bool
        :param IsSupportVpc: 是否支援私有網絡
        :type IsSupportVpc: bool
        :param HourInstanceSaleMaxNum: 小時計費實例最大售賣數量
        :type HourInstanceSaleMaxNum: int
        :param IsDefaultZone: 是否爲預設可用區
        :type IsDefaultZone: bool
        :param IsBm: 是否爲黑石區
        :type IsBm: bool
        :param PayType: 支援的付費類型。可能的返回值爲：0-包年包月；1-小時計費；2-後付費
        :type PayType: list of str
        :param ProtectMode: 數據複制類型。0-異步複制；1-半同步複制；2-強同步複制
        :type ProtectMode: list of str
        :param Zone: 可用區名稱
        :type Zone: str
        :param SellType: 售賣實例類型數組
        :type SellType: list of SellType
        :param ZoneConf: 多可用區訊息
        :type ZoneConf: :class:`taifucloudcloud.cdb.v20170320.models.ZoneConf`
        :param DrZone: 可支援的災備可用區訊息
        :type DrZone: list of str
        """
        self.Status = None
        self.ZoneName = None
        self.IsCustom = None
        self.IsSupportDr = None
        self.IsSupportVpc = None
        self.HourInstanceSaleMaxNum = None
        self.IsDefaultZone = None
        self.IsBm = None
        self.PayType = None
        self.ProtectMode = None
        self.Zone = None
        self.SellType = None
        self.ZoneConf = None
        self.DrZone = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ZoneName = params.get("ZoneName")
        self.IsCustom = params.get("IsCustom")
        self.IsSupportDr = params.get("IsSupportDr")
        self.IsSupportVpc = params.get("IsSupportVpc")
        self.HourInstanceSaleMaxNum = params.get("HourInstanceSaleMaxNum")
        self.IsDefaultZone = params.get("IsDefaultZone")
        self.IsBm = params.get("IsBm")
        self.PayType = params.get("PayType")
        self.ProtectMode = params.get("ProtectMode")
        self.Zone = params.get("Zone")
        if params.get("SellType") is not None:
            self.SellType = []
            for item in params.get("SellType"):
                obj = SellType()
                obj._deserialize(item)
                self.SellType.append(obj)
        if params.get("ZoneConf") is not None:
            self.ZoneConf = ZoneConf()
            self.ZoneConf._deserialize(params.get("ZoneConf"))
        self.DrZone = params.get("DrZone")