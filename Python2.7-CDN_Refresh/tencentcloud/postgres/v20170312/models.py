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


class AccountInfo(AbstractModel):
    """帳戶訊息

    """

    def __init__(self):
        """
        :param DBInstanceId: 實例ID，形如postgres-lnp6j617
        :type DBInstanceId: str
        :param UserName: 帳号
        :type UserName: str
        :param Remark: 帳号備注
        :type Remark: str
        :param Status: 帳号狀态。 1-創建中，2-正常，3-修改中，4-密碼重置中，-1-删除中
        :type Status: int
        :param CreateTime: 帳号創建時間
        :type CreateTime: str
        :param UpdateTime: 帳号最後一次更新時間
        :type UpdateTime: str
        """
        self.DBInstanceId = None
        self.UserName = None
        self.Remark = None
        self.Status = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.UserName = params.get("UserName")
        self.Remark = params.get("Remark")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class CloseDBExtranetAccessRequest(AbstractModel):
    """CloseDBExtranetAccess請求參數結構體

    """

    def __init__(self):
        """
        :param DBInstanceId: 實例ID，形如postgres-6r233v55
        :type DBInstanceId: str
        """
        self.DBInstanceId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")


class CloseDBExtranetAccessResponse(AbstractModel):
    """CloseDBExtranetAccess返回參數結構體

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


class CloseServerlessDBExtranetAccessRequest(AbstractModel):
    """CloseServerlessDBExtranetAccess請求參數結構體

    """

    def __init__(self):
        """
        :param DBInstanceId: 實例唯一标識符
        :type DBInstanceId: str
        :param DBInstanceName: 實例名稱
        :type DBInstanceName: str
        """
        self.DBInstanceId = None
        self.DBInstanceName = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.DBInstanceName = params.get("DBInstanceName")


class CloseServerlessDBExtranetAccessResponse(AbstractModel):
    """CloseServerlessDBExtranetAccess返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDBInstancesRequest(AbstractModel):
    """CreateDBInstances請求參數結構體

    """

    def __init__(self):
        """
        :param SpecCode: 售賣規格ID。該參數可以通過調用DescribeProductConfig的返回值中的SpecCode欄位來獲取。
        :type SpecCode: str
        :param DBVersion: PostgreSQL内核版本，目前支援：9.3.5、9.5.4、10.4三種版本。
        :type DBVersion: str
        :param Storage: 實例容量大小，單位：GB。
        :type Storage: int
        :param InstanceCount: 一次性購買的實例數量。取值1-100
        :type InstanceCount: int
        :param Period: 購買時長，單位：月。目前只支援1,2,3,4,5,6,7,8,9,10,11,12,24,36這些值，按量計費模式下該參數傳1。
        :type Period: int
        :param Zone: 可用區ID。該參數可以通過調用 DescribeZones 介面的返回值中的Zone欄位來獲取。
        :type Zone: str
        :param ProjectId: 項目ID。
        :type ProjectId: int
        :param InstanceChargeType: 實例計費類型。目前支援：PREPAID（預付費，即包年包月），POSTPAID_BY_HOUR（後付費，即按量計費）。
        :type InstanceChargeType: str
        :param AutoVoucher: 是否自動使用代金券。1（是），0（否），預設不使用。
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID清單，目前僅支援指定一張代金券。
        :type VoucherIds: list of str
        :param VpcId: 私有網絡ID。
        :type VpcId: str
        :param SubnetId: 私有網絡子網ID。
        :type SubnetId: str
        :param AutoRenewFlag: 續約标記：0-正常續約（預設）；1-自動續約；
        :type AutoRenewFlag: int
        :param ActivityId: 活動ID
        :type ActivityId: int
        :param Name: 實例名
        :type Name: str
        """
        self.SpecCode = None
        self.DBVersion = None
        self.Storage = None
        self.InstanceCount = None
        self.Period = None
        self.Zone = None
        self.ProjectId = None
        self.InstanceChargeType = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.VpcId = None
        self.SubnetId = None
        self.AutoRenewFlag = None
        self.ActivityId = None
        self.Name = None


    def _deserialize(self, params):
        self.SpecCode = params.get("SpecCode")
        self.DBVersion = params.get("DBVersion")
        self.Storage = params.get("Storage")
        self.InstanceCount = params.get("InstanceCount")
        self.Period = params.get("Period")
        self.Zone = params.get("Zone")
        self.ProjectId = params.get("ProjectId")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.ActivityId = params.get("ActivityId")
        self.Name = params.get("Name")


class CreateDBInstancesResponse(AbstractModel):
    """CreateDBInstances返回參數結構體

    """

    def __init__(self):
        """
        :param DealNames: 訂單号清單。每個實例對應一個訂單号。
        :type DealNames: list of str
        :param BillId: 鎖定流水号
        :type BillId: str
        :param DBInstanceIdSet: 創建成功的實例ID集合，只在後付費情景下有返回值
        :type DBInstanceIdSet: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DealNames = None
        self.BillId = None
        self.DBInstanceIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealNames = params.get("DealNames")
        self.BillId = params.get("BillId")
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        self.RequestId = params.get("RequestId")


class CreateServerlessDBInstanceRequest(AbstractModel):
    """CreateServerlessDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param Zone: 可用區ID。該參數可以通過調用 DescribeZones 介面的返回值中的Zone欄位來獲取。
        :type Zone: str
        :param DBInstanceName: DB實例名稱，同一個賬号下該值必須唯一。
        :type DBInstanceName: str
        :param DBVersion: PostgreSQL内核版本，目前只支援：9.3.5、9.5.4、10.4三種版本。
        :type DBVersion: str
        :param DBCharset: PostgreSQL資料庫字元集，目前支援UTF8、LATIN1兩種。
        :type DBCharset: str
        :param ProjectId: 項目ID。
        :type ProjectId: int
        :param VpcId: 私有網絡ID。
        :type VpcId: str
        :param SubnetId: 私有網絡子網ID。
        :type SubnetId: str
        """
        self.Zone = None
        self.DBInstanceName = None
        self.DBVersion = None
        self.DBCharset = None
        self.ProjectId = None
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.DBInstanceName = params.get("DBInstanceName")
        self.DBVersion = params.get("DBVersion")
        self.DBCharset = params.get("DBCharset")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")


class CreateServerlessDBInstanceResponse(AbstractModel):
    """CreateServerlessDBInstance返回參數結構體

    """

    def __init__(self):
        """
        :param DBInstanceId: 實例ID，該ID全局唯一，如：postgres-xxxxx
        :type DBInstanceId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DBInstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.RequestId = params.get("RequestId")


class DBBackup(AbstractModel):
    """資料庫備份訊息

    """

    def __init__(self):
        """
        :param Id: 備份文件唯一标識
        :type Id: int
        :param StartTime: 文件生成的開始時間
        :type StartTime: str
        :param EndTime: 文件生成的結束時間
        :type EndTime: str
        :param Size: 文件大小(K)
        :type Size: int
        :param Strategy: 策略（0-實例備份；1-多庫備份）
        :type Strategy: int
        :param Way: 類型（0-定時）
        :type Way: int
        :param Type: 備份方式（1-完整）
        :type Type: int
        :param Status: 狀态（1-創建中；2-成功；3-失敗）
        :type Status: int
        :param DbList: DB清單
        :type DbList: list of str
        :param InternalAddr: 内網下載網址
        :type InternalAddr: str
        :param ExternalAddr: 外網下載網址
        :type ExternalAddr: str
        """
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.Size = None
        self.Strategy = None
        self.Way = None
        self.Type = None
        self.Status = None
        self.DbList = None
        self.InternalAddr = None
        self.ExternalAddr = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Size = params.get("Size")
        self.Strategy = params.get("Strategy")
        self.Way = params.get("Way")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.DbList = params.get("DbList")
        self.InternalAddr = params.get("InternalAddr")
        self.ExternalAddr = params.get("ExternalAddr")


class DBInstance(AbstractModel):
    """描述實例的詳細訊息

    """

    def __init__(self):
        """
        :param Region: 實例所屬地域，如: ap-guangzhou，對應RegionSet的Region欄位
        :type Region: str
        :param Zone: 實例所屬可用區， 如：ap-guangzhou-3，對應ZoneSet的Zone欄位
        :type Zone: str
        :param ProjectId: 項目ID
        :type ProjectId: int
        :param VpcId: 私有網絡ID
        :type VpcId: str
        :param SubnetId: SubnetId
        :type SubnetId: str
        :param DBInstanceId: 實例ID
        :type DBInstanceId: str
        :param DBInstanceName: 實例名稱
        :type DBInstanceName: str
        :param DBInstanceStatus: 實例狀态
        :type DBInstanceStatus: str
        :param DBInstanceMemory: 實例分配的内存大小，單位：GB
        :type DBInstanceMemory: int
        :param DBInstanceStorage: 實例分配的儲存空間大小，單位：GB
        :type DBInstanceStorage: int
        :param DBInstanceCpu: 實例分配的CPU數量，單位：個
        :type DBInstanceCpu: int
        :param DBInstanceClass: 售賣規格ID
        :type DBInstanceClass: str
        :param DBInstanceType: 實例類型，類型有：1、primary（主實例）；2、readonly（只讀實例）；3、guard（災備實例）；4、temp（臨時實例）
        :type DBInstanceType: str
        :param DBInstanceVersion: 實例版本，目前只支援standard（雙機高可用版, 一主一從）
        :type DBInstanceVersion: str
        :param DBCharset: 實例DB字元集
        :type DBCharset: str
        :param DBVersion: PostgreSQL内核版本
        :type DBVersion: str
        :param CreateTime: 實例創建時間
        :type CreateTime: str
        :param UpdateTime: 實例執行最後一次更新的時間
        :type UpdateTime: str
        :param ExpireTime: 實例到期時間
        :type ExpireTime: str
        :param IsolatedTime: 實例隔離時間
        :type IsolatedTime: str
        :param PayType: 計費模式，1、prepaid（包年包月,預付費）；2、postpaid（按量計費，後付費）
        :type PayType: str
        :param AutoRenew: 是否自動續約，1：自動續約，0：不自動續約
        :type AutoRenew: int
        :param DBInstanceNetInfo: 實例網絡連接訊息
        :type DBInstanceNetInfo: list of DBInstanceNetInfo
        :param Type: 機器類型
        :type Type: str
        :param AppId: 用戶的AppId
        :type AppId: int
        :param Uid: 實例的Uid
        :type Uid: int
        """
        self.Region = None
        self.Zone = None
        self.ProjectId = None
        self.VpcId = None
        self.SubnetId = None
        self.DBInstanceId = None
        self.DBInstanceName = None
        self.DBInstanceStatus = None
        self.DBInstanceMemory = None
        self.DBInstanceStorage = None
        self.DBInstanceCpu = None
        self.DBInstanceClass = None
        self.DBInstanceType = None
        self.DBInstanceVersion = None
        self.DBCharset = None
        self.DBVersion = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ExpireTime = None
        self.IsolatedTime = None
        self.PayType = None
        self.AutoRenew = None
        self.DBInstanceNetInfo = None
        self.Type = None
        self.AppId = None
        self.Uid = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.DBInstanceId = params.get("DBInstanceId")
        self.DBInstanceName = params.get("DBInstanceName")
        self.DBInstanceStatus = params.get("DBInstanceStatus")
        self.DBInstanceMemory = params.get("DBInstanceMemory")
        self.DBInstanceStorage = params.get("DBInstanceStorage")
        self.DBInstanceCpu = params.get("DBInstanceCpu")
        self.DBInstanceClass = params.get("DBInstanceClass")
        self.DBInstanceType = params.get("DBInstanceType")
        self.DBInstanceVersion = params.get("DBInstanceVersion")
        self.DBCharset = params.get("DBCharset")
        self.DBVersion = params.get("DBVersion")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.IsolatedTime = params.get("IsolatedTime")
        self.PayType = params.get("PayType")
        self.AutoRenew = params.get("AutoRenew")
        if params.get("DBInstanceNetInfo") is not None:
            self.DBInstanceNetInfo = []
            for item in params.get("DBInstanceNetInfo"):
                obj = DBInstanceNetInfo()
                obj._deserialize(item)
                self.DBInstanceNetInfo.append(obj)
        self.Type = params.get("Type")
        self.AppId = params.get("AppId")
        self.Uid = params.get("Uid")


class DBInstanceNetInfo(AbstractModel):
    """描述實例的網絡連接訊息

    """

    def __init__(self):
        """
        :param Address: DNS域名
        :type Address: str
        :param Ip: Ip
        :type Ip: str
        :param Port: 連接Port網址
        :type Port: int
        :param NetType: 網絡類型，1、inner（内網網址）；2、public（外網網址）
        :type NetType: str
        :param Status: 網絡連接狀态
        :type Status: str
        """
        self.Address = None
        self.Ip = None
        self.Port = None
        self.NetType = None
        self.Status = None


    def _deserialize(self, params):
        self.Address = params.get("Address")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.NetType = params.get("NetType")
        self.Status = params.get("Status")


class DeleteServerlessDBInstanceRequest(AbstractModel):
    """DeleteServerlessDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param DBInstanceName: DB實例名稱，實例名和實例ID必須至少傳一個，如果同時存在，将只以實例ID爲準。
        :type DBInstanceName: str
        :param DBInstanceId: DB實例ID，實例名和實例ID必須至少傳一個，如果同時存在，将只以實例ID爲準。
        :type DBInstanceId: str
        """
        self.DBInstanceName = None
        self.DBInstanceId = None


    def _deserialize(self, params):
        self.DBInstanceName = params.get("DBInstanceName")
        self.DBInstanceId = params.get("DBInstanceId")


class DeleteServerlessDBInstanceResponse(AbstractModel):
    """DeleteServerlessDBInstance返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
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
        :param DBInstanceId: 實例ID，形如postgres-6fego161
        :type DBInstanceId: str
        :param Limit: 分頁返回，每頁最大返回數目，預設20，取值範圍爲1-100
        :type Limit: int
        :param Offset: 分頁返回，返回第幾頁的用戶數據。頁碼從0開始計數
        :type Offset: int
        :param OrderBy: 返回數據按照創建時間或者用戶名排序。取值只能爲createTime或者name。createTime-按照創建時間排序；name-按照用戶名排序
        :type OrderBy: str
        :param OrderByType: 返回結果是升序還是降序。取值只能爲desc或者asc。desc-降序；asc-升序
        :type OrderByType: str
        """
        self.DBInstanceId = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 本次調用介面共返回了多少條數據。
        :type TotalCount: int
        :param Details: 帳号清單詳細訊息。
        :type Details: list of AccountInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Details = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = AccountInfo()
                obj._deserialize(item)
                self.Details.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBBackupsRequest(AbstractModel):
    """DescribeDBBackups請求參數結構體

    """

    def __init__(self):
        """
        :param DBInstanceId: 實例ID，形如postgres-4wdeb0zv。
        :type DBInstanceId: str
        :param Type: 備份方式（1-全量）。目前只支援全量，取值爲1。
        :type Type: int
        :param StartTime: 查詢開始時間，形如2018-06-10 17:06:38，起始時間不得小於7天以前
        :type StartTime: str
        :param EndTime: 查詢結束時間，形如2018-06-10 17:06:38
        :type EndTime: str
        :param Limit: 備份清單分頁返回，每頁返回數量，預設爲 20，最小爲1，最大值爲 100。
        :type Limit: int
        :param Offset: 返回結果中的第幾頁，從第0頁開始。預設爲0。
        :type Offset: int
        """
        self.DBInstanceId = None
        self.Type = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.Type = params.get("Type")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeDBBackupsResponse(AbstractModel):
    """DescribeDBBackups返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 返回備份清單中備份文件的個數
        :type TotalCount: int
        :param BackupList: 備份清單
        :type BackupList: list of DBBackup
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.BackupList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BackupList") is not None:
            self.BackupList = []
            for item in params.get("BackupList"):
                obj = DBBackup()
                obj._deserialize(item)
                self.BackupList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBErrlogsRequest(AbstractModel):
    """DescribeDBErrlogs請求參數結構體

    """

    def __init__(self):
        """
        :param DBInstanceId: 實例ID，形如postgres-5bq3wfjd
        :type DBInstanceId: str
        :param StartTime: 查詢起始時間，形如2018-01-01 00:00:00，起始時間不得小於7天以前
        :type StartTime: str
        :param EndTime: 查詢結束時間，形如2018-01-01 00:00:00
        :type EndTime: str
        :param DatabaseName: 資料庫名字
        :type DatabaseName: str
        :param SearchKeys: 搜索關鍵字
        :type SearchKeys: list of str
        :param Limit: 分頁返回，每頁返回的最大數量。取值爲1-100
        :type Limit: int
        :param Offset: 分頁返回，返回第幾頁的數據，從第0頁開始計數
        :type Offset: int
        """
        self.DBInstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.DatabaseName = None
        self.SearchKeys = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.DatabaseName = params.get("DatabaseName")
        self.SearchKeys = params.get("SearchKeys")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeDBErrlogsResponse(AbstractModel):
    """DescribeDBErrlogs返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 本次調用返回了多少條數據
        :type TotalCount: int
        :param Details: 錯誤日志清單
        :type Details: list of ErrLogDetail
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Details = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = ErrLogDetail()
                obj._deserialize(item)
                self.Details.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBInstanceAttributeRequest(AbstractModel):
    """DescribeDBInstanceAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param DBInstanceId: 實例ID
        :type DBInstanceId: str
        """
        self.DBInstanceId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")


class DescribeDBInstanceAttributeResponse(AbstractModel):
    """DescribeDBInstanceAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param DBInstance: 實例詳細訊息。
        :type DBInstance: :class:`tencentcloud.postgres.v20170312.models.DBInstance`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DBInstance = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DBInstance") is not None:
            self.DBInstance = DBInstance()
            self.DBInstance._deserialize(params.get("DBInstance"))
        self.RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 過濾條件，目前支援：db-instance-id、db-instance-name、db-project-id、db-pay-mode。
        :type Filters: list of Filter
        :param Limit: 每頁顯示數量，預設返回10條。
        :type Limit: int
        :param Offset: 分頁序号，從0開始。
        :type Offset: int
        :param OrderBy: 排序指标，如實例名、創建時間等，支援DBInstanceId,CreateTime,Name,EndTime
        :type OrderBy: str
        :param OrderByType: 排序方式，包括升序、降序
        :type OrderByType: str
        """
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")


class DescribeDBInstancesResponse(AbstractModel):
    """DescribeDBInstances返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 查詢到的實例數量。
        :type TotalCount: int
        :param DBInstanceSet: 實例詳細訊息集合。
        :type DBInstanceSet: list of DBInstance
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DBInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DBInstanceSet") is not None:
            self.DBInstanceSet = []
            for item in params.get("DBInstanceSet"):
                obj = DBInstance()
                obj._deserialize(item)
                self.DBInstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBSlowlogsRequest(AbstractModel):
    """DescribeDBSlowlogs請求參數結構體

    """

    def __init__(self):
        """
        :param DBInstanceId: 實例ID，形如postgres-lnp6j617
        :type DBInstanceId: str
        :param StartTime: 查詢起始時間，形如2018-06-10 17:06:38，起始時間不得小於7天以前
        :type StartTime: str
        :param EndTime: 查詢結束時間，形如2018-06-10 17:06:38
        :type EndTime: str
        :param DatabaseName: 資料庫名字
        :type DatabaseName: str
        :param OrderBy: 按照何種指标排序，取值爲sum_calls或者sum_cost_time。sum_calls-總調用次數；sum_cost_time-總的花費時間
        :type OrderBy: str
        :param OrderByType: 排序規則。desc-降序；asc-升序
        :type OrderByType: str
        :param Limit: 分頁返回結果，每頁最大返回數量，取值爲1-100，預設20
        :type Limit: int
        :param Offset: 分頁返回結果，返回結果的第幾頁，從0開始計數
        :type Offset: int
        """
        self.DBInstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.DatabaseName = None
        self.OrderBy = None
        self.OrderByType = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.DatabaseName = params.get("DatabaseName")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeDBSlowlogsResponse(AbstractModel):
    """DescribeDBSlowlogs返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 本次返回多少條數據
        :type TotalCount: int
        :param Detail: 慢查詢日志詳情
        :type Detail: :class:`tencentcloud.postgres.v20170312.models.SlowlogDetail`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Detail = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Detail") is not None:
            self.Detail = SlowlogDetail()
            self.Detail._deserialize(params.get("Detail"))
        self.RequestId = params.get("RequestId")


class DescribeDBXlogsRequest(AbstractModel):
    """DescribeDBXlogs請求參數結構體

    """

    def __init__(self):
        """
        :param DBInstanceId: 實例ID，形如postgres-4wdeb0zv。
        :type DBInstanceId: str
        :param StartTime: 查詢開始時間，形如2018-06-10 17:06:38，起始時間不得小於7天以前
        :type StartTime: str
        :param EndTime: 查詢結束時間，形如2018-06-10 17:06:38
        :type EndTime: str
        :param Offset: 分頁返回，表示返回第幾頁的條目。從第0頁開始計數。
        :type Offset: int
        :param Limit: 分頁返回，表示每頁有多少條目。取值爲1-100。
        :type Limit: int
        """
        self.DBInstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeDBXlogsResponse(AbstractModel):
    """DescribeDBXlogs返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 表示此次返回結果有多少條數據。
        :type TotalCount: int
        :param XlogList: Xlog清單
        :type XlogList: list of Xlog
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.XlogList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("XlogList") is not None:
            self.XlogList = []
            for item in params.get("XlogList"):
                obj = Xlog()
                obj._deserialize(item)
                self.XlogList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    """DescribeDatabases請求參數結構體

    """

    def __init__(self):
        """
        :param DBInstanceId: 實例ID
        :type DBInstanceId: str
        """
        self.DBInstanceId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")


class DescribeDatabasesResponse(AbstractModel):
    """DescribeDatabases返回參數結構體

    """

    def __init__(self):
        """
        :param Items: 資料庫訊息
        :type Items: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Items = params.get("Items")
        self.RequestId = params.get("RequestId")


class DescribeOrdersRequest(AbstractModel):
    """DescribeOrders請求參數結構體

    """

    def __init__(self):
        """
        :param DealNames: 訂單名集合
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
        :param TotalCount: 訂單數量
        :type TotalCount: int
        :param Deals: 訂單數組
        :type Deals: list of PgDeal
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
                obj = PgDeal()
                obj._deserialize(item)
                self.Deals.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProductConfigRequest(AbstractModel):
    """DescribeProductConfig請求參數結構體

    """

    def __init__(self):
        """
        :param Zone: 可用區名稱
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
        :param SpecInfoList: 售賣規格清單。
        :type SpecInfoList: list of SpecInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SpecInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SpecInfoList") is not None:
            self.SpecInfoList = []
            for item in params.get("SpecInfoList"):
                obj = SpecInfo()
                obj._deserialize(item)
                self.SpecInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions請求參數結構體

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 返回的結果數量。
        :type TotalCount: int
        :param RegionSet: 地域訊息集合。
        :type RegionSet: list of RegionInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
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


class DescribeServerlessDBInstancesRequest(AbstractModel):
    """DescribeServerlessDBInstances請求參數結構體

    """

    def __init__(self):
        """
        :param Filter: 查詢條件
        :type Filter: list of Filter
        :param Limit: 查詢個數
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        """
        self.Filter = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self.Filter = []
            for item in params.get("Filter"):
                obj = Filter()
                obj._deserialize(item)
                self.Filter.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeServerlessDBInstancesResponse(AbstractModel):
    """DescribeServerlessDBInstances返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 查詢結果數
        :type TotalCount: int
        :param DBInstanceSet: 查詢結果
注意：此欄位可能返回 null，表示取不到有效值。
        :type DBInstanceSet: list of ServerlessDBInstance
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DBInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DBInstanceSet") is not None:
            self.DBInstanceSet = []
            for item in params.get("DBInstanceSet"):
                obj = ServerlessDBInstance()
                obj._deserialize(item)
                self.DBInstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones請求參數結構體

    """


class DescribeZonesResponse(AbstractModel):
    """DescribeZones返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 返回的結果數量。
        :type TotalCount: int
        :param ZoneSet: 可用區訊息集合。
        :type ZoneSet: list of ZoneInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
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


class DestroyDBInstanceRequest(AbstractModel):
    """DestroyDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param DBInstanceId: 待删除實例标識符
        :type DBInstanceId: str
        """
        self.DBInstanceId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")


class DestroyDBInstanceResponse(AbstractModel):
    """DestroyDBInstance返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ErrLogDetail(AbstractModel):
    """錯誤日志詳情

    """

    def __init__(self):
        """
        :param UserName: 用戶名
        :type UserName: str
        :param Database: 資料庫名字
        :type Database: str
        :param ErrTime: 錯誤發生時間
        :type ErrTime: str
        :param ErrMsg: 錯誤訊息
        :type ErrMsg: str
        """
        self.UserName = None
        self.Database = None
        self.ErrTime = None
        self.ErrMsg = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Database = params.get("Database")
        self.ErrTime = params.get("ErrTime")
        self.ErrMsg = params.get("ErrMsg")


class Filter(AbstractModel):
    """描述鍵值對過濾器，用于條件過濾查詢。例如過濾ID、名稱等
    * 若存在多個Filter時，Filter間的關系爲邏輯與（AND）關系。
    * 若同一個Filter存在多個Values，同一Filter下Values間的關系爲邏輯或（OR）關系。

    """

    def __init__(self):
        """
        :param Name: 過濾鍵的名稱。
        :type Name: str
        :param Values: 一個或者多個過濾值。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class InitDBInstancesRequest(AbstractModel):
    """InitDBInstances請求參數結構體

    """

    def __init__(self):
        """
        :param DBInstanceIdSet: 實例ID集合。
        :type DBInstanceIdSet: list of str
        :param AdminName: 實例根賬号用戶名。
        :type AdminName: str
        :param AdminPassword: 實例根賬号用戶名對應的密碼。
        :type AdminPassword: str
        :param Charset: 實例字元集，目前只支援：UTF8、LATIN1。
        :type Charset: str
        """
        self.DBInstanceIdSet = None
        self.AdminName = None
        self.AdminPassword = None
        self.Charset = None


    def _deserialize(self, params):
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        self.AdminName = params.get("AdminName")
        self.AdminPassword = params.get("AdminPassword")
        self.Charset = params.get("Charset")


class InitDBInstancesResponse(AbstractModel):
    """InitDBInstances返回參數結構體

    """

    def __init__(self):
        """
        :param DBInstanceIdSet: 實例ID集合。
        :type DBInstanceIdSet: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DBInstanceIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        self.RequestId = params.get("RequestId")


class InquiryPriceCreateDBInstancesRequest(AbstractModel):
    """InquiryPriceCreateDBInstances請求參數結構體

    """

    def __init__(self):
        """
        :param Zone: 可用區ID。該參數可以通過調用 DescribeZones 介面的返回值中的Zone欄位來獲取。
        :type Zone: str
        :param SpecCode: 規格ID。該參數可以通過調用DescribeProductConfig介面的返回值中的SpecCode欄位來獲取。
        :type SpecCode: str
        :param Storage: 儲存容量大小，單位：GB。
        :type Storage: int
        :param InstanceCount: 實例數量。目前最大數量不超過100，如需一次性創建更多實例，請聯系客服支援。
        :type InstanceCount: int
        :param Period: 購買時長，單位：月。目前只支援1,2,3,4,5,6,7,8,9,10,11,12,24,36這些值。
        :type Period: int
        :param Pid: 計費ID。該參數可以通過調用DescribeProductConfig介面的返回值中的Pid欄位來獲取。
        :type Pid: int
        :param InstanceChargeType: 實例計費類型。目前只支援：PREPAID（預付費，即包年包月）。
        :type InstanceChargeType: str
        """
        self.Zone = None
        self.SpecCode = None
        self.Storage = None
        self.InstanceCount = None
        self.Period = None
        self.Pid = None
        self.InstanceChargeType = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.SpecCode = params.get("SpecCode")
        self.Storage = params.get("Storage")
        self.InstanceCount = params.get("InstanceCount")
        self.Period = params.get("Period")
        self.Pid = params.get("Pid")
        self.InstanceChargeType = params.get("InstanceChargeType")


class InquiryPriceCreateDBInstancesResponse(AbstractModel):
    """InquiryPriceCreateDBInstances返回參數結構體

    """

    def __init__(self):
        """
        :param OriginalPrice: 原始價格，單位：分
        :type OriginalPrice: int
        :param Price: 折後價格，單位：分
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


class InquiryPriceRenewDBInstanceRequest(AbstractModel):
    """InquiryPriceRenewDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param DBInstanceId: 實例ID
        :type DBInstanceId: str
        :param Period: 續約週期，按月計算，最大不超過48
        :type Period: int
        """
        self.DBInstanceId = None
        self.Period = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.Period = params.get("Period")


class InquiryPriceRenewDBInstanceResponse(AbstractModel):
    """InquiryPriceRenewDBInstance返回參數結構體

    """

    def __init__(self):
        """
        :param OriginalPrice: 總費用，打折前的。比如24650表示246.5元
        :type OriginalPrice: int
        :param Price: 實際需要付款金額。比如24650表示246.5元
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


class InquiryPriceUpgradeDBInstanceRequest(AbstractModel):
    """InquiryPriceUpgradeDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param Storage: 實例的磁盤大小，單位GB
        :type Storage: int
        :param Memory: 實例的内存大小，單位GB
        :type Memory: int
        :param DBInstanceId: 實例ID，形如postgres-hez4fh0v
        :type DBInstanceId: str
        :param InstanceChargeType: 實例計費類型，預付費或者後付費。PREPAID-預付費。目前只支援預付費。
        :type InstanceChargeType: str
        """
        self.Storage = None
        self.Memory = None
        self.DBInstanceId = None
        self.InstanceChargeType = None


    def _deserialize(self, params):
        self.Storage = params.get("Storage")
        self.Memory = params.get("Memory")
        self.DBInstanceId = params.get("DBInstanceId")
        self.InstanceChargeType = params.get("InstanceChargeType")


class InquiryPriceUpgradeDBInstanceResponse(AbstractModel):
    """InquiryPriceUpgradeDBInstance返回參數結構體

    """

    def __init__(self):
        """
        :param OriginalPrice: 總費用，打折前的
        :type OriginalPrice: int
        :param Price: 實際需要付款金額
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


class ModifyAccountRemarkRequest(AbstractModel):
    """ModifyAccountRemark請求參數結構體

    """

    def __init__(self):
        """
        :param DBInstanceId: 實例ID，形如postgres-4wdeb0zv
        :type DBInstanceId: str
        :param UserName: 實例用戶名
        :type UserName: str
        :param Remark: 用戶UserName對應的新備注
        :type Remark: str
        """
        self.DBInstanceId = None
        self.UserName = None
        self.Remark = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.UserName = params.get("UserName")
        self.Remark = params.get("Remark")


class ModifyAccountRemarkResponse(AbstractModel):
    """ModifyAccountRemark返回參數結構體

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
        :param DBInstanceId: 資料庫實例ID，形如postgres-6fego161
        :type DBInstanceId: str
        :param InstanceName: 新的資料庫實例名字
        :type InstanceName: str
        """
        self.DBInstanceId = None
        self.InstanceName = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
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
        :param DBInstanceIdSet: postgresql實例ID數組
        :type DBInstanceIdSet: list of str
        :param ProjectId: postgresql實例所屬新項目的ID
        :type ProjectId: str
        """
        self.DBInstanceIdSet = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        self.ProjectId = params.get("ProjectId")


class ModifyDBInstancesProjectResponse(AbstractModel):
    """ModifyDBInstancesProject返回參數結構體

    """

    def __init__(self):
        """
        :param Count: 轉移項目成功的實例個數
        :type Count: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class NormalQueryItem(AbstractModel):
    """單條SlowQuery訊息

    """

    def __init__(self):
        """
        :param UserName: 用戶名
        :type UserName: str
        :param Calls: 調用次數
        :type Calls: int
        :param CallsGrids: 粒度點
        :type CallsGrids: list of int
        :param CostTime: 花費總時間
        :type CostTime: float
        :param Rows: 影響的行數
        :type Rows: int
        :param MinCostTime: 花費最小時間
        :type MinCostTime: float
        :param MaxCostTime: 花費最大時間
        :type MaxCostTime: float
        :param FirstTime: 最早一條慢SQL時間
        :type FirstTime: str
        :param LastTime: 最晚一條慢SQL時間
        :type LastTime: str
        :param SharedReadBlks: 讀共享内存塊數
        :type SharedReadBlks: int
        :param SharedWriteBlks: 寫共享内存塊數
        :type SharedWriteBlks: int
        :param ReadCostTime: 讀io總耗時
        :type ReadCostTime: int
        :param WriteCostTime: 寫io總耗時
        :type WriteCostTime: int
        :param DatabaseName: 資料庫名字
        :type DatabaseName: str
        :param NormalQuery: 脫敏後的慢SQL
        :type NormalQuery: str
        """
        self.UserName = None
        self.Calls = None
        self.CallsGrids = None
        self.CostTime = None
        self.Rows = None
        self.MinCostTime = None
        self.MaxCostTime = None
        self.FirstTime = None
        self.LastTime = None
        self.SharedReadBlks = None
        self.SharedWriteBlks = None
        self.ReadCostTime = None
        self.WriteCostTime = None
        self.DatabaseName = None
        self.NormalQuery = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Calls = params.get("Calls")
        self.CallsGrids = params.get("CallsGrids")
        self.CostTime = params.get("CostTime")
        self.Rows = params.get("Rows")
        self.MinCostTime = params.get("MinCostTime")
        self.MaxCostTime = params.get("MaxCostTime")
        self.FirstTime = params.get("FirstTime")
        self.LastTime = params.get("LastTime")
        self.SharedReadBlks = params.get("SharedReadBlks")
        self.SharedWriteBlks = params.get("SharedWriteBlks")
        self.ReadCostTime = params.get("ReadCostTime")
        self.WriteCostTime = params.get("WriteCostTime")
        self.DatabaseName = params.get("DatabaseName")
        self.NormalQuery = params.get("NormalQuery")


class OpenDBExtranetAccessRequest(AbstractModel):
    """OpenDBExtranetAccess請求參數結構體

    """

    def __init__(self):
        """
        :param DBInstanceId: 實例ID，形如postgres-hez4fh0v
        :type DBInstanceId: str
        """
        self.DBInstanceId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")


class OpenDBExtranetAccessResponse(AbstractModel):
    """OpenDBExtranetAccess返回參數結構體

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


class OpenServerlessDBExtranetAccessRequest(AbstractModel):
    """OpenServerlessDBExtranetAccess請求參數結構體

    """

    def __init__(self):
        """
        :param DBInstanceId: 實例的唯一标識符
        :type DBInstanceId: str
        :param DBInstanceName: 實例名稱
        :type DBInstanceName: str
        """
        self.DBInstanceId = None
        self.DBInstanceName = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.DBInstanceName = params.get("DBInstanceName")


class OpenServerlessDBExtranetAccessResponse(AbstractModel):
    """OpenServerlessDBExtranetAccess返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PgDeal(AbstractModel):
    """訂單詳情

    """

    def __init__(self):
        """
        :param DealName: 訂單名
        :type DealName: str
        :param OwnerUin: 所屬用戶
        :type OwnerUin: str
        :param Count: 訂單涉及多少個實例
        :type Count: int
        :param PayMode: 付費模式。1-預付費；0-後付費
        :type PayMode: int
        :param FlowId: 異步任務流程ID
        :type FlowId: int
        :param DBInstanceIdSet: 實例ID數組
        :type DBInstanceIdSet: list of str
        """
        self.DealName = None
        self.OwnerUin = None
        self.Count = None
        self.PayMode = None
        self.FlowId = None
        self.DBInstanceIdSet = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.OwnerUin = params.get("OwnerUin")
        self.Count = params.get("Count")
        self.PayMode = params.get("PayMode")
        self.FlowId = params.get("FlowId")
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")


class RegionInfo(AbstractModel):
    """描述地域的編碼和狀态等訊息

    """

    def __init__(self):
        """
        :param Region: 該地域對應的英文名稱
        :type Region: str
        :param RegionName: 該地域對應的中文名稱
        :type RegionName: str
        :param RegionId: 該地域對應的數字編号
        :type RegionId: int
        :param RegionState: 可用狀态，UNAVAILABLE表示不可用，AVAILABLE表示可用
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


class RenewInstanceRequest(AbstractModel):
    """RenewInstance請求參數結構體

    """

    def __init__(self):
        """
        :param DBInstanceId: 實例ID，形如postgres-6fego161
        :type DBInstanceId: str
        :param Period: 續約多少個月
        :type Period: int
        :param AutoVoucher: 是否自動使用代金券,1是,0否，預設不使用
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID清單，目前僅支援指定一張代金券
        :type VoucherIds: list of str
        """
        self.DBInstanceId = None
        self.Period = None
        self.AutoVoucher = None
        self.VoucherIds = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.Period = params.get("Period")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")


class RenewInstanceResponse(AbstractModel):
    """RenewInstance返回參數結構體

    """

    def __init__(self):
        """
        :param DealName: 訂單名
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
        :param DBInstanceId: 實例ID，形如postgres-4wdeb0zv
        :type DBInstanceId: str
        :param UserName: 實例帳戶名
        :type UserName: str
        :param Password: UserName帳戶對應的新密碼
        :type Password: str
        """
        self.DBInstanceId = None
        self.UserName = None
        self.Password = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.UserName = params.get("UserName")
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


class RestartDBInstanceRequest(AbstractModel):
    """RestartDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param DBInstanceId: 實例ID，形如postgres-6r233v55
        :type DBInstanceId: str
        """
        self.DBInstanceId = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")


class RestartDBInstanceResponse(AbstractModel):
    """RestartDBInstance返回參數結構體

    """

    def __init__(self):
        """
        :param FlowId: 異步流程ID
        :type FlowId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ServerlessDBAccount(AbstractModel):
    """serverless賬号描述

    """

    def __init__(self):
        """
        :param DBUser: 用戶名
注意：此欄位可能返回 null，表示取不到有效值。
        :type DBUser: str
        :param DBPassword: 密碼
注意：此欄位可能返回 null，表示取不到有效值。
        :type DBPassword: str
        :param DBConnLimit: 連接數限制
注意：此欄位可能返回 null，表示取不到有效值。
        :type DBConnLimit: int
        """
        self.DBUser = None
        self.DBPassword = None
        self.DBConnLimit = None


    def _deserialize(self, params):
        self.DBUser = params.get("DBUser")
        self.DBPassword = params.get("DBPassword")
        self.DBConnLimit = params.get("DBConnLimit")


class ServerlessDBInstance(AbstractModel):
    """serverless實例描述

    """

    def __init__(self):
        """
        :param DBInstanceId: 實例id，唯一标識符
注意：此欄位可能返回 null，表示取不到有效值。
        :type DBInstanceId: str
        :param DBInstanceName: 實例名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type DBInstanceName: str
        :param DBInstanceStatus: 實例狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type DBInstanceStatus: str
        :param Region: 地域
注意：此欄位可能返回 null，表示取不到有效值。
        :type Region: str
        :param Zone: 可用區
注意：此欄位可能返回 null，表示取不到有效值。
        :type Zone: str
        :param ProjectId: projectId
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param VpcId: VpcId
注意：此欄位可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param SubnetId: 子網id
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param DBCharset: 字元集
注意：此欄位可能返回 null，表示取不到有效值。
        :type DBCharset: str
        :param DBVersion: 資料庫版本
注意：此欄位可能返回 null，表示取不到有效值。
        :type DBVersion: str
        :param CreateTime: 創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param DBInstanceNetInfo: 實例網絡訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type DBInstanceNetInfo: list of ServerlessDBInstanceNetInfo
        :param DBAccountSet: 實例帳戶訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type DBAccountSet: list of ServerlessDBAccount
        :param DBDatabaseList: 實例下的db訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type DBDatabaseList: list of str
        """
        self.DBInstanceId = None
        self.DBInstanceName = None
        self.DBInstanceStatus = None
        self.Region = None
        self.Zone = None
        self.ProjectId = None
        self.VpcId = None
        self.SubnetId = None
        self.DBCharset = None
        self.DBVersion = None
        self.CreateTime = None
        self.DBInstanceNetInfo = None
        self.DBAccountSet = None
        self.DBDatabaseList = None


    def _deserialize(self, params):
        self.DBInstanceId = params.get("DBInstanceId")
        self.DBInstanceName = params.get("DBInstanceName")
        self.DBInstanceStatus = params.get("DBInstanceStatus")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.DBCharset = params.get("DBCharset")
        self.DBVersion = params.get("DBVersion")
        self.CreateTime = params.get("CreateTime")
        if params.get("DBInstanceNetInfo") is not None:
            self.DBInstanceNetInfo = []
            for item in params.get("DBInstanceNetInfo"):
                obj = ServerlessDBInstanceNetInfo()
                obj._deserialize(item)
                self.DBInstanceNetInfo.append(obj)
        if params.get("DBAccountSet") is not None:
            self.DBAccountSet = []
            for item in params.get("DBAccountSet"):
                obj = ServerlessDBAccount()
                obj._deserialize(item)
                self.DBAccountSet.append(obj)
        self.DBDatabaseList = params.get("DBDatabaseList")


class ServerlessDBInstanceNetInfo(AbstractModel):
    """serverless實例網絡訊息描述

    """

    def __init__(self):
        """
        :param Address: 網址
注意：此欄位可能返回 null，表示取不到有效值。
        :type Address: str
        :param Ip: ip網址
注意：此欄位可能返回 null，表示取不到有效值。
        :type Ip: str
        :param Port: 端口号
注意：此欄位可能返回 null，表示取不到有效值。
        :type Port: int
        :param Status: 狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: str
        :param NetType: 網絡類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type NetType: str
        """
        self.Address = None
        self.Ip = None
        self.Port = None
        self.Status = None
        self.NetType = None


    def _deserialize(self, params):
        self.Address = params.get("Address")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.Status = params.get("Status")
        self.NetType = params.get("NetType")


class SetAutoRenewFlagRequest(AbstractModel):
    """SetAutoRenewFlag請求參數結構體

    """

    def __init__(self):
        """
        :param DBInstanceIdSet: 實例ID數組
        :type DBInstanceIdSet: list of str
        :param AutoRenewFlag: 續約标記。0-正常續約；1-自動續約；2-到期不續約
        :type AutoRenewFlag: int
        """
        self.DBInstanceIdSet = None
        self.AutoRenewFlag = None


    def _deserialize(self, params):
        self.DBInstanceIdSet = params.get("DBInstanceIdSet")
        self.AutoRenewFlag = params.get("AutoRenewFlag")


class SetAutoRenewFlagResponse(AbstractModel):
    """SetAutoRenewFlag返回參數結構體

    """

    def __init__(self):
        """
        :param Count: 設置成功的實例個數
        :type Count: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class SlowlogDetail(AbstractModel):
    """慢查詢詳情

    """

    def __init__(self):
        """
        :param TotalTime: 花費總時間
        :type TotalTime: float
        :param TotalCalls: 調用總次數
        :type TotalCalls: int
        :param NormalQueries: 脫敏後的慢SQL清單
        :type NormalQueries: list of NormalQueryItem
        """
        self.TotalTime = None
        self.TotalCalls = None
        self.NormalQueries = None


    def _deserialize(self, params):
        self.TotalTime = params.get("TotalTime")
        self.TotalCalls = params.get("TotalCalls")
        if params.get("NormalQueries") is not None:
            self.NormalQueries = []
            for item in params.get("NormalQueries"):
                obj = NormalQueryItem()
                obj._deserialize(item)
                self.NormalQueries.append(obj)


class SpecInfo(AbstractModel):
    """描述某個地域下某個可用區的可售賣規格詳細訊息。

    """

    def __init__(self):
        """
        :param Region: 地域英文編碼，對應RegionSet的Region欄位
        :type Region: str
        :param Zone: 區域英文編碼，對應ZoneSet的Zone欄位
        :type Zone: str
        :param SpecItemInfoList: 規格詳細訊息清單
        :type SpecItemInfoList: list of SpecItemInfo
        """
        self.Region = None
        self.Zone = None
        self.SpecItemInfoList = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        if params.get("SpecItemInfoList") is not None:
            self.SpecItemInfoList = []
            for item in params.get("SpecItemInfoList"):
                obj = SpecItemInfo()
                obj._deserialize(item)
                self.SpecItemInfoList.append(obj)


class SpecItemInfo(AbstractModel):
    """描述一種規格的訊息訊息

    """

    def __init__(self):
        """
        :param SpecCode: 規格ID
        :type SpecCode: str
        :param Version: PostgreSQL的内核版本編号
        :type Version: str
        :param VersionName: 内核編号對應的完整版本名稱
        :type VersionName: str
        :param Cpu: CPU核數
        :type Cpu: int
        :param Memory: 内存大小，單位：MB
        :type Memory: int
        :param MaxStorage: 該規格所支援最大儲存容量，單位：GB
        :type MaxStorage: int
        :param MinStorage: 該規格所支援最小儲存容量，單位：GB
        :type MinStorage: int
        :param Qps: 該規格的預估QPS
        :type Qps: int
        :param Pid: 該規格對應的計費ID
        :type Pid: int
        :param Type: 機器類型
        :type Type: str
        """
        self.SpecCode = None
        self.Version = None
        self.VersionName = None
        self.Cpu = None
        self.Memory = None
        self.MaxStorage = None
        self.MinStorage = None
        self.Qps = None
        self.Pid = None
        self.Type = None


    def _deserialize(self, params):
        self.SpecCode = params.get("SpecCode")
        self.Version = params.get("Version")
        self.VersionName = params.get("VersionName")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.MaxStorage = params.get("MaxStorage")
        self.MinStorage = params.get("MinStorage")
        self.Qps = params.get("Qps")
        self.Pid = params.get("Pid")
        self.Type = params.get("Type")


class UpgradeDBInstanceRequest(AbstractModel):
    """UpgradeDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param Memory: 升級後的實例内存大小，單位GB
        :type Memory: int
        :param Storage: 升級後的實例磁盤大小，單位GB
        :type Storage: int
        :param DBInstanceId: 實例ID，形如postgres-lnp6j617
        :type DBInstanceId: str
        :param AutoVoucher: 是否自動使用代金券,1是,0否，預設不使用
        :type AutoVoucher: int
        :param VoucherIds: 代金券ID清單，目前僅支援指定一張代金券
        :type VoucherIds: list of str
        :param ActivityId: 活動ID
        :type ActivityId: int
        """
        self.Memory = None
        self.Storage = None
        self.DBInstanceId = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.ActivityId = None


    def _deserialize(self, params):
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.DBInstanceId = params.get("DBInstanceId")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.ActivityId = params.get("ActivityId")


class UpgradeDBInstanceResponse(AbstractModel):
    """UpgradeDBInstance返回參數結構體

    """

    def __init__(self):
        """
        :param DealName: 交易名字。
        :type DealName: str
        :param BillId: 鎖定流水号
        :type BillId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.BillId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.BillId = params.get("BillId")
        self.RequestId = params.get("RequestId")


class Xlog(AbstractModel):
    """資料庫Xlog訊息

    """

    def __init__(self):
        """
        :param Id: 備份文件唯一标識
        :type Id: int
        :param StartTime: 文件生成的開始時間
        :type StartTime: str
        :param EndTime: 文件生成的結束時間
        :type EndTime: str
        :param InternalAddr: 内網下載網址
        :type InternalAddr: str
        :param ExternalAddr: 外網下載網址
        :type ExternalAddr: str
        :param Size: 備份文件大小
        :type Size: int
        """
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.InternalAddr = None
        self.ExternalAddr = None
        self.Size = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.InternalAddr = params.get("InternalAddr")
        self.ExternalAddr = params.get("ExternalAddr")
        self.Size = params.get("Size")


class ZoneInfo(AbstractModel):
    """描述可用區的編碼和狀态訊息

    """

    def __init__(self):
        """
        :param Zone: 該可用區的英文名稱
        :type Zone: str
        :param ZoneName: 該可用區的中文名稱
        :type ZoneName: str
        :param ZoneId: 該可用區對應的數字編号
        :type ZoneId: int
        :param ZoneState: 可用狀态，UNAVAILABLE表示不可用，AVAILABLE表示可用
        :type ZoneState: str
        """
        self.Zone = None
        self.ZoneName = None
        self.ZoneId = None
        self.ZoneState = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneName = params.get("ZoneName")
        self.ZoneId = params.get("ZoneId")
        self.ZoneState = params.get("ZoneState")