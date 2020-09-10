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


class CosBackup(AbstractModel):
    """ES cos自動備份訊息

    """

    def __init__(self):
        """
        :param IsAutoBackup: 是否開啓cos自動備份
        :type IsAutoBackup: bool
        :param BackupTime: 自動備份執行時間（精确到小時）, e.g. "22:00"
        :type BackupTime: str
        """
        self.IsAutoBackup = None
        self.BackupTime = None


    def _deserialize(self, params):
        self.IsAutoBackup = params.get("IsAutoBackup")
        self.BackupTime = params.get("BackupTime")


class CreateInstanceRequest(AbstractModel):
    """CreateInstance請求參數結構體

    """

    def __init__(self):
        """
        :param Zone: 可用區
        :type Zone: str
        :param NodeNum: 節點數量（2-50個）
        :type NodeNum: int
        :param EsVersion: 實例版本（支援"5.6.4"、"6.4.3"）
        :type EsVersion: str
        :param NodeType: 節點規格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
        :type NodeType: str
        :param DiskSize: 節點磁盤容量（單位GB）
        :type DiskSize: int
        :param VpcId: 私有網絡ID
        :type VpcId: str
        :param SubnetId: 子網ID
        :type SubnetId: str
        :param Password: 訪問密碼（密碼需8到16位，至少包括兩項（[a-z,A-Z],[0-9]和[-!@#$%&^*+=_:;,.?]的特殊符号）
        :type Password: str
        :param InstanceName: 實例名稱（1-50 個英文、漢字、數字、連接線-或下劃線_）
        :type InstanceName: str
        :param ChargeType: 計費類型<li>PREPAID：預付費，即包年包月</li><li>POSTPAID_BY_HOUR：按小時後付費</li>預設值POSTPAID_BY_HOUR
        :type ChargeType: str
        :param ChargePeriod: 包年包月購買時長（單位由參數TimeUint決定）
        :type ChargePeriod: int
        :param RenewFlag: 自動續約标識<li>RENEW_FLAG_AUTO：自動續約</li><li>RENEW_FLAG_MANUAL：不自動續約，用戶手動續約</li>ChargeType爲PREPAID時需要設置，如不傳遞該參數，普通用于預設不自動續約，SVIP用戶自動續約
        :type RenewFlag: str
        :param DiskType: 節點磁盤類型<li>CLOUD_SSD：SSD雲硬碟</li><li>CLOUD_PREMIUM：高硬能雲硬碟</li>預設值CLOUD_SSD
        :type DiskType: str
        :param TimeUnit: 計費時長單位（ChargeType爲PREPAID時需要設置，預設值爲“m”，表示月，當前只支援“m”）
        :type TimeUnit: str
        :param AutoVoucher: 是否自動使用 <li>0：不自動使用</li><li>1：自動使用</li>預設值0
        :type AutoVoucher: int
        :param VoucherIds:  ID清單（目前僅支援指定一張 ）
        :type VoucherIds: list of str
        :param EnableDedicatedMaster: 是否創建專用主節點<li>true：開啓專用主節點</li><li>false：不開啓專用主節點</li>預設值false
        :type EnableDedicatedMaster: bool
        :param MasterNodeNum: 專用主節點個數（只支援3個和5個，EnableDedicatedMaster爲true時該值必傳）
        :type MasterNodeNum: int
        :param MasterNodeType: 專用主節點類型（EnableDedicatedMaster爲true時必傳）<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
        :type MasterNodeType: str
        :param MasterNodeDiskSize: 專用主節點磁盤大小（單位GB，非必傳，若傳遞則必須爲50，暫不支援自定義）
        :type MasterNodeDiskSize: int
        :param ClusterNameInConf: 集群配置文件中的ClusterName（系統預設配置爲實例ID，暫不支援自定義）
        :type ClusterNameInConf: str
        :param DeployMode: 集群佈署方式<li>0：單可用區佈署</li><li>1：多可用區佈署</li>預設爲0
        :type DeployMode: int
        :param MultiZoneInfo: 多可用區佈署時可用區的詳細訊息(DeployMode爲1時必傳)
        :type MultiZoneInfo: list of MultiZoneInfo
        :param LicenseType: License類型<li>oss：開源版</li><li>basic：基礎版</li><li>platinum：白金版</li>預設值platinum
        :type LicenseType: str
        """
        self.Zone = None
        self.NodeNum = None
        self.EsVersion = None
        self.NodeType = None
        self.DiskSize = None
        self.VpcId = None
        self.SubnetId = None
        self.Password = None
        self.InstanceName = None
        self.ChargeType = None
        self.ChargePeriod = None
        self.RenewFlag = None
        self.DiskType = None
        self.TimeUnit = None
        self.AutoVoucher = None
        self.VoucherIds = None
        self.EnableDedicatedMaster = None
        self.MasterNodeNum = None
        self.MasterNodeType = None
        self.MasterNodeDiskSize = None
        self.ClusterNameInConf = None
        self.DeployMode = None
        self.MultiZoneInfo = None
        self.LicenseType = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.NodeNum = params.get("NodeNum")
        self.EsVersion = params.get("EsVersion")
        self.NodeType = params.get("NodeType")
        self.DiskSize = params.get("DiskSize")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Password = params.get("Password")
        self.InstanceName = params.get("InstanceName")
        self.ChargeType = params.get("ChargeType")
        self.ChargePeriod = params.get("ChargePeriod")
        self.RenewFlag = params.get("RenewFlag")
        self.DiskType = params.get("DiskType")
        self.TimeUnit = params.get("TimeUnit")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")
        self.EnableDedicatedMaster = params.get("EnableDedicatedMaster")
        self.MasterNodeNum = params.get("MasterNodeNum")
        self.MasterNodeType = params.get("MasterNodeType")
        self.MasterNodeDiskSize = params.get("MasterNodeDiskSize")
        self.ClusterNameInConf = params.get("ClusterNameInConf")
        self.DeployMode = params.get("DeployMode")
        if params.get("MultiZoneInfo") is not None:
            self.MultiZoneInfo = []
            for item in params.get("MultiZoneInfo"):
                obj = MultiZoneInfo()
                obj._deserialize(item)
                self.MultiZoneInfo.append(obj)
        self.LicenseType = params.get("LicenseType")


class CreateInstanceResponse(AbstractModel):
    """CreateInstance返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class DeleteInstanceRequest(AbstractModel):
    """DeleteInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DeleteInstanceResponse(AbstractModel):
    """DeleteInstance返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeInstanceLogsRequest(AbstractModel):
    """DescribeInstanceLogs請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 集群實例ID
        :type InstanceId: str
        :param LogType: 日志類型，預設值爲1
<li>1, 主日志</li>
<li>2, 搜索慢日志</li>
<li>3, 索引慢日志</li>
<li>4, GC日志</li>
        :type LogType: int
        :param SearchKey: 搜索詞，支援LUCENE語法，如 level:WARN、ip:1.1.1.1、message:test-index等
        :type SearchKey: str
        :param StartTime: 日志開始時間，格式爲YYYY-MM-DD HH:MM:SS, 如2019-01-22 20:15:53
        :type StartTime: str
        :param EndTime: 日志結束時間，格式爲YYYY-MM-DD HH:MM:SS, 如2019-01-22 20:15:53
        :type EndTime: str
        :param Offset: 分頁起始值, 預設值爲0
        :type Offset: int
        :param Limit: 分頁大小，預設值爲100，最大值100
        :type Limit: int
        :param OrderByType: 時間排序方式，預設值爲0
<li>0, 降序</li>
<li>1, 升序</li>
        :type OrderByType: int
        """
        self.InstanceId = None
        self.LogType = None
        self.SearchKey = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.LogType = params.get("LogType")
        self.SearchKey = params.get("SearchKey")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderByType = params.get("OrderByType")


class DescribeInstanceLogsResponse(AbstractModel):
    """DescribeInstanceLogs返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 返回的日志條數
        :type TotalCount: int
        :param InstanceLogList: 日志詳細訊息清單
        :type InstanceLogList: list of InstanceLog
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceLogList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceLogList") is not None:
            self.InstanceLogList = []
            for item in params.get("InstanceLogList"):
                obj = InstanceLog()
                obj._deserialize(item)
                self.InstanceLogList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceOperationsRequest(AbstractModel):
    """DescribeInstanceOperations請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 集群實例ID
        :type InstanceId: str
        :param StartTime: 起始時間, e.g. "2019-03-07 16:30:39"
        :type StartTime: str
        :param EndTime: 結束時間, e.g. "2019-03-30 20:18:03"
        :type EndTime: str
        :param Offset: 分頁起始值
        :type Offset: int
        :param Limit: 分頁大小
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


class DescribeInstanceOperationsResponse(AbstractModel):
    """DescribeInstanceOperations返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 操作記錄總數
        :type TotalCount: int
        :param Operations: 操作記錄
        :type Operations: list of Operation
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Operations = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Operations") is not None:
            self.Operations = []
            for item in params.get("Operations"):
                obj = Operation()
                obj._deserialize(item)
                self.Operations.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances請求參數結構體

    """

    def __init__(self):
        """
        :param Zone: 集群實例所屬可用區，不傳則預設所有可用區
        :type Zone: str
        :param InstanceIds: 集群實例ID清單
        :type InstanceIds: list of str
        :param InstanceNames: 集群實例名稱清單
        :type InstanceNames: list of str
        :param Offset: 分頁起始值, 預設值0
        :type Offset: int
        :param Limit: 分頁大小，預設值20
        :type Limit: int
        :param OrderByKey: 排序欄位<li>1：實例ID</li><li>2：實例名稱</li><li>3：可用區</li><li>4：創建時間</li>若orderKey未傳遞則按創建時間降序排序
        :type OrderByKey: int
        :param OrderByType: 排序方式<li>0：升序</li><li>1：降序</li>若傳遞了orderByKey未傳遞orderByType, 則預設升序
        :type OrderByType: int
        """
        self.Zone = None
        self.InstanceIds = None
        self.InstanceNames = None
        self.Offset = None
        self.Limit = None
        self.OrderByKey = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceNames = params.get("InstanceNames")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderByKey = params.get("OrderByKey")
        self.OrderByType = params.get("OrderByType")


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 返回的實例個數
        :type TotalCount: int
        :param InstanceList: 實例詳細訊息清單
        :type InstanceList: list of InstanceInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        self.RequestId = params.get("RequestId")


class DictInfo(AbstractModel):
    """ik插件詞典新

    """

    def __init__(self):
        """
        :param Key: 詞典鍵值
        :type Key: str
        :param Name: 詞典名稱
        :type Name: str
        :param Size: 詞典大小，單位B
        :type Size: int
        """
        self.Key = None
        self.Name = None
        self.Size = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Name = params.get("Name")
        self.Size = params.get("Size")


class EsAcl(AbstractModel):
    """ES集群配置項

    """

    def __init__(self):
        """
        :param BlackIpList: kibana訪問黑名單
        :type BlackIpList: list of str
        :param WhiteIpList: kibana訪問白名單
        :type WhiteIpList: list of str
        """
        self.BlackIpList = None
        self.WhiteIpList = None


    def _deserialize(self, params):
        self.BlackIpList = params.get("BlackIpList")
        self.WhiteIpList = params.get("WhiteIpList")


class EsDictionaryInfo(AbstractModel):
    """ES IK詞庫訊息

    """

    def __init__(self):
        """
        :param MainDict: 啓用詞詞典清單
        :type MainDict: list of DictInfo
        :param Stopwords: 停用詞詞典清單
        :type Stopwords: list of DictInfo
        """
        self.MainDict = None
        self.Stopwords = None


    def _deserialize(self, params):
        if params.get("MainDict") is not None:
            self.MainDict = []
            for item in params.get("MainDict"):
                obj = DictInfo()
                obj._deserialize(item)
                self.MainDict.append(obj)
        if params.get("Stopwords") is not None:
            self.Stopwords = []
            for item in params.get("Stopwords"):
                obj = DictInfo()
                obj._deserialize(item)
                self.Stopwords.append(obj)


class InstanceInfo(AbstractModel):
    """實例詳細訊息

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param InstanceName: 實例名稱
        :type InstanceName: str
        :param Region: 地域
        :type Region: str
        :param Zone: 可用區
        :type Zone: str
        :param AppId: 用戶ID
        :type AppId: int
        :param Uin: 用戶UIN
        :type Uin: str
        :param VpcUid: 實例所屬VPC的UID
        :type VpcUid: str
        :param SubnetUid: 實例所屬子網的UID
        :type SubnetUid: str
        :param Status: 實例狀态，0:處理中,1:正常,-1停止,-2:銷毀中,-3:已銷毀
        :type Status: int
        :param ChargeType: 實例計費模式。取值範圍：  PREPAID：表示預付費，即包年包月  POSTPAID_BY_HOUR：表示後付費，即按量計費  CDHPAID：CDH付費，即只對CDH計費，不對CDH上的實例計費。
        :type ChargeType: str
        :param ChargePeriod: 包年包月購買時長,單位:月
        :type ChargePeriod: int
        :param RenewFlag: 自動續約标識。取值範圍：  NOTIFY_AND_AUTO_RENEW：通知過期且自動續約  NOTIFY_AND_MANUAL_RENEW：通知過期不自動續約  DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知過期不自動續約  預設取值：NOTIFY_AND_AUTO_RENEW。若該參數指定爲NOTIFY_AND_AUTO_RENEW，在帳戶餘額充足的情況下，實例到期後将按月自動續約。
        :type RenewFlag: str
        :param NodeType: 節點規格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
        :type NodeType: str
        :param NodeNum: 節點個數
        :type NodeNum: int
        :param CpuNum: 節點CPU核數
        :type CpuNum: int
        :param MemSize: 節點内存大小，單位GB
        :type MemSize: int
        :param DiskType: 節點磁盤類型
        :type DiskType: str
        :param DiskSize: 節點磁盤大小，單位GB
        :type DiskSize: int
        :param EsDomain: ES域名
        :type EsDomain: str
        :param EsVip: ES VIP
        :type EsVip: str
        :param EsPort: ES端口
        :type EsPort: int
        :param KibanaUrl: Kibana訪問url
        :type KibanaUrl: str
        :param EsVersion: ES版本号
        :type EsVersion: str
        :param EsConfig: ES配置項
        :type EsConfig: str
        :param EsAcl: ES訪問控制配置
        :type EsAcl: :class:`taifucloudcloud.es.v20180416.models.EsAcl`
        :param CreateTime: 實例創建時間
        :type CreateTime: str
        :param UpdateTime: 實例最後修改操作時間
        :type UpdateTime: str
        :param Deadline: 實例到期時間
        :type Deadline: str
        :param InstanceType: 實例類型（實例類型标識，當前只有1,2兩種）
        :type InstanceType: int
        :param IkConfig: Ik分詞器配置
        :type IkConfig: :class:`taifucloudcloud.es.v20180416.models.EsDictionaryInfo`
        :param MasterNodeInfo: 專用主節點配置
        :type MasterNodeInfo: :class:`taifucloudcloud.es.v20180416.models.MasterNodeInfo`
        :param CosBackup: cos自動備份配置
        :type CosBackup: :class:`taifucloudcloud.es.v20180416.models.CosBackup`
        :param AllowCosBackup: 是否允許cos自動備份
        :type AllowCosBackup: bool
        :param TagList: 實例擁有的标簽清單
        :type TagList: list of TagInfo
        :param LicenseType: License類型<li>oss：開源版</li><li>basic：基礎版</li><li>platinum：白金版</li>預設值platinum
        :type LicenseType: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Region = None
        self.Zone = None
        self.AppId = None
        self.Uin = None
        self.VpcUid = None
        self.SubnetUid = None
        self.Status = None
        self.ChargeType = None
        self.ChargePeriod = None
        self.RenewFlag = None
        self.NodeType = None
        self.NodeNum = None
        self.CpuNum = None
        self.MemSize = None
        self.DiskType = None
        self.DiskSize = None
        self.EsDomain = None
        self.EsVip = None
        self.EsPort = None
        self.KibanaUrl = None
        self.EsVersion = None
        self.EsConfig = None
        self.EsAcl = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Deadline = None
        self.InstanceType = None
        self.IkConfig = None
        self.MasterNodeInfo = None
        self.CosBackup = None
        self.AllowCosBackup = None
        self.TagList = None
        self.LicenseType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.AppId = params.get("AppId")
        self.Uin = params.get("Uin")
        self.VpcUid = params.get("VpcUid")
        self.SubnetUid = params.get("SubnetUid")
        self.Status = params.get("Status")
        self.ChargeType = params.get("ChargeType")
        self.ChargePeriod = params.get("ChargePeriod")
        self.RenewFlag = params.get("RenewFlag")
        self.NodeType = params.get("NodeType")
        self.NodeNum = params.get("NodeNum")
        self.CpuNum = params.get("CpuNum")
        self.MemSize = params.get("MemSize")
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        self.EsDomain = params.get("EsDomain")
        self.EsVip = params.get("EsVip")
        self.EsPort = params.get("EsPort")
        self.KibanaUrl = params.get("KibanaUrl")
        self.EsVersion = params.get("EsVersion")
        self.EsConfig = params.get("EsConfig")
        if params.get("EsAcl") is not None:
            self.EsAcl = EsAcl()
            self.EsAcl._deserialize(params.get("EsAcl"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Deadline = params.get("Deadline")
        self.InstanceType = params.get("InstanceType")
        if params.get("IkConfig") is not None:
            self.IkConfig = EsDictionaryInfo()
            self.IkConfig._deserialize(params.get("IkConfig"))
        if params.get("MasterNodeInfo") is not None:
            self.MasterNodeInfo = MasterNodeInfo()
            self.MasterNodeInfo._deserialize(params.get("MasterNodeInfo"))
        if params.get("CosBackup") is not None:
            self.CosBackup = CosBackup()
            self.CosBackup._deserialize(params.get("CosBackup"))
        self.AllowCosBackup = params.get("AllowCosBackup")
        if params.get("TagList") is not None:
            self.TagList = []
            for item in params.get("TagList"):
                obj = TagInfo()
                obj._deserialize(item)
                self.TagList.append(obj)
        self.LicenseType = params.get("LicenseType")


class InstanceLog(AbstractModel):
    """ES集群日志詳細訊息

    """

    def __init__(self):
        """
        :param Time: 日志時間
        :type Time: str
        :param Level: 日志級别
        :type Level: str
        :param Ip: 集群節點ip
        :type Ip: str
        :param Message: 日志内容
        :type Message: str
        """
        self.Time = None
        self.Level = None
        self.Ip = None
        self.Message = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Level = params.get("Level")
        self.Ip = params.get("Ip")
        self.Message = params.get("Message")


class KeyValue(AbstractModel):
    """OperationDetail使用此結構的數組描述新舊配置

    """

    def __init__(self):
        """
        :param Key: 鍵
        :type Key: str
        :param Value: 值
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class MasterNodeInfo(AbstractModel):
    """實例專用主節點相關訊息

    """

    def __init__(self):
        """
        :param EnableDedicatedMaster: 是否啓用了專用主節點
        :type EnableDedicatedMaster: bool
        :param MasterNodeType: 專用主節點規格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
        :type MasterNodeType: str
        :param MasterNodeNum: 專用主節點個數
        :type MasterNodeNum: int
        :param MasterNodeCpuNum: 專用主節點CPU核數
        :type MasterNodeCpuNum: int
        :param MasterNodeMemSize: 專用主節點内存大小，單位GB
        :type MasterNodeMemSize: int
        :param MasterNodeDiskSize: 專用主節點磁盤大小，單位GB
        :type MasterNodeDiskSize: int
        :param MasterNodeDiskType: 專用主節點磁盤類型
        :type MasterNodeDiskType: str
        """
        self.EnableDedicatedMaster = None
        self.MasterNodeType = None
        self.MasterNodeNum = None
        self.MasterNodeCpuNum = None
        self.MasterNodeMemSize = None
        self.MasterNodeDiskSize = None
        self.MasterNodeDiskType = None


    def _deserialize(self, params):
        self.EnableDedicatedMaster = params.get("EnableDedicatedMaster")
        self.MasterNodeType = params.get("MasterNodeType")
        self.MasterNodeNum = params.get("MasterNodeNum")
        self.MasterNodeCpuNum = params.get("MasterNodeCpuNum")
        self.MasterNodeMemSize = params.get("MasterNodeMemSize")
        self.MasterNodeDiskSize = params.get("MasterNodeDiskSize")
        self.MasterNodeDiskType = params.get("MasterNodeDiskType")


class MultiZoneInfo(AbstractModel):
    """多可用區佈署時可用區的詳細訊息

    """

    def __init__(self):
        """
        :param Zone: 可用區
        :type Zone: str
        :param SubnetId: 子網ID
        :type SubnetId: str
        """
        self.Zone = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.SubnetId = params.get("SubnetId")


class Operation(AbstractModel):
    """ES集群操作詳細訊息

    """

    def __init__(self):
        """
        :param Id: 操作唯一id
        :type Id: int
        :param StartTime: 操作開始時間
        :type StartTime: str
        :param Type: 操作類型
        :type Type: str
        :param Detail: 操作詳情
        :type Detail: :class:`taifucloudcloud.es.v20180416.models.OperationDetail`
        :param Result: 操作結果
        :type Result: str
        :param Tasks: 流程任務訊息
        :type Tasks: list of TaskDetail
        :param Progress: 操作進度
        :type Progress: float
        """
        self.Id = None
        self.StartTime = None
        self.Type = None
        self.Detail = None
        self.Result = None
        self.Tasks = None
        self.Progress = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.Type = params.get("Type")
        if params.get("Detail") is not None:
            self.Detail = OperationDetail()
            self.Detail._deserialize(params.get("Detail"))
        self.Result = params.get("Result")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = TaskDetail()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.Progress = params.get("Progress")


class OperationDetail(AbstractModel):
    """操作詳情

    """

    def __init__(self):
        """
        :param OldInfo: 實例原始配置訊息
        :type OldInfo: list of KeyValue
        :param NewInfo: 實例更新後配置訊息
        :type NewInfo: list of KeyValue
        """
        self.OldInfo = None
        self.NewInfo = None


    def _deserialize(self, params):
        if params.get("OldInfo") is not None:
            self.OldInfo = []
            for item in params.get("OldInfo"):
                obj = KeyValue()
                obj._deserialize(item)
                self.OldInfo.append(obj)
        if params.get("NewInfo") is not None:
            self.NewInfo = []
            for item in params.get("NewInfo"):
                obj = KeyValue()
                obj._deserialize(item)
                self.NewInfo.append(obj)


class RestartInstanceRequest(AbstractModel):
    """RestartInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param ForceRestart: 是否強制重啓<li>true：強制重啓</li><li>false：不強制重啓</li>預設false
        :type ForceRestart: bool
        """
        self.InstanceId = None
        self.ForceRestart = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ForceRestart = params.get("ForceRestart")


class RestartInstanceResponse(AbstractModel):
    """RestartInstance返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SubTaskDetail(AbstractModel):
    """實例操作記錄流程任務中的子任務訊息（如升級檢查任務中的各個檢查項）

    """

    def __init__(self):
        """
        :param Name: 子任務名
        :type Name: str
        :param Result: 子任務結果
        :type Result: bool
        :param ErrMsg: 子任務錯誤訊息
        :type ErrMsg: str
        """
        self.Name = None
        self.Result = None
        self.ErrMsg = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Result = params.get("Result")
        self.ErrMsg = params.get("ErrMsg")


class TagInfo(AbstractModel):
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


class TaskDetail(AbstractModel):
    """實例操作記錄中的流程任務訊息

    """

    def __init__(self):
        """
        :param Name: 任務名
        :type Name: str
        :param Progress: 任務進度
        :type Progress: float
        :param FinishTime: 任務完成時間
        :type FinishTime: str
        :param SubTasks: 子任務
        :type SubTasks: list of SubTaskDetail
        """
        self.Name = None
        self.Progress = None
        self.FinishTime = None
        self.SubTasks = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Progress = params.get("Progress")
        self.FinishTime = params.get("FinishTime")
        if params.get("SubTasks") is not None:
            self.SubTasks = []
            for item in params.get("SubTasks"):
                obj = SubTaskDetail()
                obj._deserialize(item)
                self.SubTasks.append(obj)


class UpdateInstanceRequest(AbstractModel):
    """UpdateInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param InstanceName: 實例名稱（1-50 個英文、漢字、數字、連接線-或下劃線_）
        :type InstanceName: str
        :param NodeNum: 節點個數（2-50個）
        :type NodeNum: int
        :param EsConfig: 配置項（JSON格式字串）。當前僅支援以下配置項：<li>action.destructive_requires_name</li><li>indices.fielddata.cache.size</li><li>indices.query.bool.max_clause_count</li>
        :type EsConfig: str
        :param Password: 預設用戶elastic的密碼（8到16位，至少包括兩項（[a-z,A-Z],[0-9]和[-!@#$%&^*+=_:;,.?]的特殊符号）
        :type Password: str
        :param EsAcl: 訪問控制清單
        :type EsAcl: :class:`taifucloudcloud.es.v20180416.models.EsAcl`
        :param DiskSize: 磁盤大小（單位GB）
        :type DiskSize: int
        :param NodeType: 節點規格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
        :type NodeType: str
        :param MasterNodeNum: 專用主節點個數（只支援3個或5個）
        :type MasterNodeNum: int
        :param MasterNodeType: 專用主節點規格<li>ES.S1.SMALL2：1核2G</li><li>ES.S1.MEDIUM4：2核4G</li><li>ES.S1.MEDIUM8：2核8G</li><li>ES.S1.LARGE16：4核16G</li><li>ES.S1.2XLARGE32：8核32G</li><li>ES.S1.4XLARGE32：16核32G</li><li>ES.S1.4XLARGE64：16核64G</li>
        :type MasterNodeType: str
        :param MasterNodeDiskSize: 專用主節點磁盤大小（單位GB系統預設配置爲50GB,暫不支援自定義）
        :type MasterNodeDiskSize: int
        :param ForceRestart: 更新配置時是否強制重啓<li>true強制重啓</li><li>false不強制重啓</li>當前僅更新EsConfig時需要設置，預設值爲false
        :type ForceRestart: bool
        :param CosBackup: COS自動備份訊息
        :type CosBackup: :class:`taifucloudcloud.es.v20180416.models.CosBackup`
        """
        self.InstanceId = None
        self.InstanceName = None
        self.NodeNum = None
        self.EsConfig = None
        self.Password = None
        self.EsAcl = None
        self.DiskSize = None
        self.NodeType = None
        self.MasterNodeNum = None
        self.MasterNodeType = None
        self.MasterNodeDiskSize = None
        self.ForceRestart = None
        self.CosBackup = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.NodeNum = params.get("NodeNum")
        self.EsConfig = params.get("EsConfig")
        self.Password = params.get("Password")
        if params.get("EsAcl") is not None:
            self.EsAcl = EsAcl()
            self.EsAcl._deserialize(params.get("EsAcl"))
        self.DiskSize = params.get("DiskSize")
        self.NodeType = params.get("NodeType")
        self.MasterNodeNum = params.get("MasterNodeNum")
        self.MasterNodeType = params.get("MasterNodeType")
        self.MasterNodeDiskSize = params.get("MasterNodeDiskSize")
        self.ForceRestart = params.get("ForceRestart")
        if params.get("CosBackup") is not None:
            self.CosBackup = CosBackup()
            self.CosBackup._deserialize(params.get("CosBackup"))


class UpdateInstanceResponse(AbstractModel):
    """UpdateInstance返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")