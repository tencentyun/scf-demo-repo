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


class COSSettings(AbstractModel):
    """COS 相關配置

    """

    def __init__(self):
        """
        :param CosSecretId: COS SecretId
        :type CosSecretId: str
        :param CosSecretKey: COS SecrectKey
        :type CosSecretKey: str
        :param LogOnCosPath: 日志儲存在COS上的路徑
        :type LogOnCosPath: str
        """
        self.CosSecretId = None
        self.CosSecretKey = None
        self.LogOnCosPath = None


    def _deserialize(self, params):
        self.CosSecretId = params.get("CosSecretId")
        self.CosSecretKey = params.get("CosSecretKey")
        self.LogOnCosPath = params.get("LogOnCosPath")


class CdbInfo(AbstractModel):
    """出參

    """

    def __init__(self):
        """
        :param InstanceName: 資料庫實例
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param Ip: 資料庫IP
注意：此欄位可能返回 null，表示取不到有效值。
        :type Ip: str
        :param Port: 資料庫端口
注意：此欄位可能返回 null，表示取不到有效值。
        :type Port: int
        :param MemSize: 資料庫内存規格
注意：此欄位可能返回 null，表示取不到有效值。
        :type MemSize: int
        :param Volume: 資料庫磁盤規格
注意：此欄位可能返回 null，表示取不到有效值。
        :type Volume: int
        :param Service: 服務标識
注意：此欄位可能返回 null，表示取不到有效值。
        :type Service: str
        :param ExpireTime: 過期時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param ApplyTime: 申請時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplyTime: str
        :param PayType: 付費類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type PayType: int
        :param ExpireFlag: 過期标識
注意：此欄位可能返回 null，表示取不到有效值。
        :type ExpireFlag: bool
        :param Status: 資料庫狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: int
        :param IsAutoRenew: 續約标識
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsAutoRenew: int
        :param SerialNo: 資料庫字串
注意：此欄位可能返回 null，表示取不到有效值。
        :type SerialNo: str
        :param ZoneId: ZoneId
注意：此欄位可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param RegionId: RegionId
注意：此欄位可能返回 null，表示取不到有效值。
        :type RegionId: int
        """
        self.InstanceName = None
        self.Ip = None
        self.Port = None
        self.MemSize = None
        self.Volume = None
        self.Service = None
        self.ExpireTime = None
        self.ApplyTime = None
        self.PayType = None
        self.ExpireFlag = None
        self.Status = None
        self.IsAutoRenew = None
        self.SerialNo = None
        self.ZoneId = None
        self.RegionId = None


    def _deserialize(self, params):
        self.InstanceName = params.get("InstanceName")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.MemSize = params.get("MemSize")
        self.Volume = params.get("Volume")
        self.Service = params.get("Service")
        self.ExpireTime = params.get("ExpireTime")
        self.ApplyTime = params.get("ApplyTime")
        self.PayType = params.get("PayType")
        self.ExpireFlag = params.get("ExpireFlag")
        self.Status = params.get("Status")
        self.IsAutoRenew = params.get("IsAutoRenew")
        self.SerialNo = params.get("SerialNo")
        self.ZoneId = params.get("ZoneId")
        self.RegionId = params.get("RegionId")


class ClusterInstancesInfo(AbstractModel):
    """集群實例訊息

    """

    def __init__(self):
        """
        :param Id: ID号
注意：此欄位可能返回 null，表示取不到有效值。
        :type Id: int
        :param ClusterId: 集群ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param Ftitle: 标題
注意：此欄位可能返回 null，表示取不到有效值。
        :type Ftitle: str
        :param ClusterName: 集群名
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param RegionId: 地域ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type RegionId: int
        :param ZoneId: 地區ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param AppId: 用戶APPID
注意：此欄位可能返回 null，表示取不到有效值。
        :type AppId: int
        :param Uin: 用戶UIN
注意：此欄位可能返回 null，表示取不到有效值。
        :type Uin: str
        :param ProjectId: 項目Id
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param VpcId: 集群VPCID
注意：此欄位可能返回 null，表示取不到有效值。
        :type VpcId: int
        :param SubnetId: 子網ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubnetId: int
        :param Status: 實例的狀态碼。取值範圍：
<li>2：表示集群運作中。</li>
<li>3：表示集群創建中。</li>
<li>4：表示集群擴容中。</li>
<li>5：表示集群增加router節點中。</li>
<li>6：表示集群安裝元件中。</li>
<li>7：表示集群執行命令中。</li>
<li>8：表示重啓服務中。</li>
<li>9：表示進入維護中。</li>
<li>10：表示服務暫停中。</li>
<li>11：表示登出維護中。</li>
<li>12：表示登出暫停中。</li>
<li>13：表示配置下發中。</li>
<li>14：表示銷毀集群中。</li>
<li>15：表示銷毀core節點中。</li>
<li>16：銷毀task節點中。</li>
<li>17：表示銷毀router節點中。</li>
<li>18：表示更改webproxy密碼中。</li>
<li>19：表示集群隔離中。</li>
<li>20：表示集群沖正中。</li>
<li>21：表示集群回收中。</li>
<li>22：表示變配等待中。</li>
<li>23：表示集群已隔離。</li>
<li>24：表示縮容節點中。</li>
<li>33：表示集群等待退費中。</li>
<li>34：表示集群已退費。</li>
<li>301：表示創建失敗。</li>
<li>302：表示擴容失敗。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: int
        :param AddTime: 添加時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type AddTime: str
        :param RunTime: 已經運作時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type RunTime: str
        :param Config: 集群産品配置訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Config: :class:`taifucloudcloud.emr.v20190103.models.EmrProductConfigOutter`
        :param MasterIp: 主節點外網IP
注意：此欄位可能返回 null，表示取不到有效值。
        :type MasterIp: str
        :param EmrVersion: EMR版本
注意：此欄位可能返回 null，表示取不到有效值。
        :type EmrVersion: str
        :param ChargeType: 收費類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type ChargeType: int
        :param TradeVersion: 交易版本
注意：此欄位可能返回 null，表示取不到有效值。
        :type TradeVersion: int
        :param ResourceOrderId: 資源訂單ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResourceOrderId: int
        :param IsTradeCluster: 是否計費集群
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsTradeCluster: int
        :param AlarmInfo: 集群錯誤狀态告警訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type AlarmInfo: str
        :param IsWoodpeckerCluster: 是否采用新架構
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsWoodpeckerCluster: int
        :param MetaDb: 中繼資料庫訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type MetaDb: str
        :param Tags: 标簽訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param HiveMetaDb: Hive中繼資料訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type HiveMetaDb: str
        :param ServiceClass: 集群類型:EMR,CLICKHOUSE,DRUID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ServiceClass: str
        :param AliasInfo: 集群所有節點的别名序列化
注意：此欄位可能返回 null，表示取不到有效值。
        :type AliasInfo: str
        :param ProductId: 集群版本Id
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProductId: int
        """
        self.Id = None
        self.ClusterId = None
        self.Ftitle = None
        self.ClusterName = None
        self.RegionId = None
        self.ZoneId = None
        self.AppId = None
        self.Uin = None
        self.ProjectId = None
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.AddTime = None
        self.RunTime = None
        self.Config = None
        self.MasterIp = None
        self.EmrVersion = None
        self.ChargeType = None
        self.TradeVersion = None
        self.ResourceOrderId = None
        self.IsTradeCluster = None
        self.AlarmInfo = None
        self.IsWoodpeckerCluster = None
        self.MetaDb = None
        self.Tags = None
        self.HiveMetaDb = None
        self.ServiceClass = None
        self.AliasInfo = None
        self.ProductId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.ClusterId = params.get("ClusterId")
        self.Ftitle = params.get("Ftitle")
        self.ClusterName = params.get("ClusterName")
        self.RegionId = params.get("RegionId")
        self.ZoneId = params.get("ZoneId")
        self.AppId = params.get("AppId")
        self.Uin = params.get("Uin")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.AddTime = params.get("AddTime")
        self.RunTime = params.get("RunTime")
        if params.get("Config") is not None:
            self.Config = EmrProductConfigOutter()
            self.Config._deserialize(params.get("Config"))
        self.MasterIp = params.get("MasterIp")
        self.EmrVersion = params.get("EmrVersion")
        self.ChargeType = params.get("ChargeType")
        self.TradeVersion = params.get("TradeVersion")
        self.ResourceOrderId = params.get("ResourceOrderId")
        self.IsTradeCluster = params.get("IsTradeCluster")
        self.AlarmInfo = params.get("AlarmInfo")
        self.IsWoodpeckerCluster = params.get("IsWoodpeckerCluster")
        self.MetaDb = params.get("MetaDb")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.HiveMetaDb = params.get("HiveMetaDb")
        self.ServiceClass = params.get("ServiceClass")
        self.AliasInfo = params.get("AliasInfo")
        self.ProductId = params.get("ProductId")


class CreateInstanceRequest(AbstractModel):
    """CreateInstance請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID，不同産品ID表示不同的EMR産品版本。取值範圍：
<li>1：表示EMR-V1.3.1。</li>
<li>2：表示EMR-V2.0.1。</li>
<li>4：表示EMR-V2.1.0。</li>
<li>7：表示EMR-V3.0.0。</li>
        :type ProductId: int
        :param VPCSettings: 私有網絡相關訊息配置。通過該參數可以指定私有網絡的ID，子網ID等訊息。
        :type VPCSettings: :class:`taifucloudcloud.emr.v20190103.models.VPCSettings`
        :param Software: 佈署的元件清單。不同的EMR産品ID（ProductId：具體含義參考入參ProductId欄位）需要選擇不同的必選元件：
<li>ProductId爲1的時候，必選元件包括：hadoop-2.7.3、knox-1.2.0、zookeeper-3.4.9</li>
<li>ProductId爲2的時候，必選元件包括：hadoop-2.7.3、knox-1.2.0、zookeeper-3.4.9</li>
<li>ProductId爲4的時候，必選元件包括：hadoop-2.8.4、knox-1.2.0、zookeeper-3.4.9</li>
<li>ProductId爲7的時候，必選元件包括：hadoop-3.1.2、knox-1.2.0、zookeeper-3.4.9</li>
        :type Software: list of str
        :param ResourceSpec: 節點資源的規格。
        :type ResourceSpec: :class:`taifucloudcloud.emr.v20190103.models.NewResourceSpec`
        :param SupportHA: 是否開啓節點高可用。取值範圍：
<li>0：表示不開啓節點高可用。</li>
<li>1：表示開啓節點高可用。</li>
        :type SupportHA: int
        :param InstanceName: 實例名稱。
<li>長度限制爲6-36個字元。</li>
<li>只允許包含中文、字母、數字、-、_。</li>
        :type InstanceName: str
        :param PayMode: 實例計費模式。取值範圍：
<li>0：表示按量計費。</li>
<li>1：表示包年包月。</li>
        :type PayMode: int
        :param Placement: 實例所在的位置。通過該參數可以指定實例所屬可用區，所屬項目等屬性。
        :type Placement: :class:`taifucloudcloud.emr.v20190103.models.Placement`
        :param TimeSpan: 購買實例的時長。結合TimeUnit一起使用。
<li>TimeUnit爲s時，該參數只能填寫3600，表示按量計費實例。</li>
<li>TimeUnit爲m時，該參數填寫的數字表示包年包月實例的購買時長，如1表示購買一個月</li>
        :type TimeSpan: int
        :param TimeUnit: 購買實例的時間單位。取值範圍：
<li>s：表示秒。PayMode取值爲0時，TimeUnit只能取值爲s。</li>
<li>m：表示月份。PayMode取值爲1時，TimeUnit只能取值爲m。</li>
        :type TimeUnit: str
        :param LoginSettings: 實例登入設置。通過該參數可以設置所購買節點的登入方式密碼或者金鑰。
<li>設置金鑰時，密碼僅用于元件原生WebUI快捷入口登入。</li>
<li>未設置金鑰時，密碼用于登入所購節點以及元件原生WebUI快捷入口登入。</li>
        :type LoginSettings: :class:`taifucloudcloud.emr.v20190103.models.LoginSettings`
        :param COSSettings: 開啓COS訪問需要設置的參數。
        :type COSSettings: :class:`taifucloudcloud.emr.v20190103.models.COSSettings`
        :param SgId: 實例所屬安全組的ID，形如sg-xxxxxxxx。該參數可以通過調用 [DescribeSecurityGroups](https://cloud.taifucloud.com/document/api/215/15808) 的返回值中的SecurityGroupId欄位來獲取。
        :type SgId: str
        :param PreExecutedFileSettings: 引導操作腳本設置。
        :type PreExecutedFileSettings: list of PreExecuteFileSettings
        :param AutoRenew: 包年包月實例是否自動續約。取值範圍：
<li>0：表示不自動續約。</li>
<li>1：表示自動續約。</li>
        :type AutoRenew: int
        :param ClientToken: 用戶端Token。
        :type ClientToken: str
        :param NeedMasterWan: 是否開啓集群Master節點公網。取值範圍：
<li>NEED_MASTER_WAN：表示開啓集群Master節點公網。</li>
<li>NOT_NEED_MASTER_WAN：表示不開啓。</li>預設開啓集群Master節點公網。
        :type NeedMasterWan: str
        :param RemoteLoginAtCreate: 是否需要開啓外網遠端登入，即22号端口。在SgId不爲空時，該參數無效。
        :type RemoteLoginAtCreate: int
        :param CheckSecurity: 是否開啓安全集群。0表示不開啓，非0表示開啓。
        :type CheckSecurity: int
        :param ExtendFsField: 訪問外部文件系統。
        :type ExtendFsField: str
        :param Tags: 标簽描述清單。通過指定該參數可以同時綁定标簽到相應的實例。
        :type Tags: list of Tag
        :param DisasterRecoverGroupIds: 分散置放群組ID清單，當前只支援指定一個。
        :type DisasterRecoverGroupIds: list of str
        :param CbsEncrypt: 集群維度CBS加密盤，預設0表示不加密，1表示加密
        :type CbsEncrypt: int
        :param MetaType: hive共享中繼資料庫類型。取值範圍：
<li>EMR_NEW_META：表示集群預設創建</li>
<li>EMR_EXIT_METE：表示集群使用指定EMR-MetaDB。</li>
<li>USER_CUSTOM_META：表示集群使用自定義MetaDB。</li>
        :type MetaType: str
        :param UnifyMetaInstanceId: EMR-MetaDB實例
        :type UnifyMetaInstanceId: str
        :param MetaDBInfo: 自定義MetaDB訊息
        :type MetaDBInfo: :class:`taifucloudcloud.emr.v20190103.models.CustomMetaInfo`
        """
        self.ProductId = None
        self.VPCSettings = None
        self.Software = None
        self.ResourceSpec = None
        self.SupportHA = None
        self.InstanceName = None
        self.PayMode = None
        self.Placement = None
        self.TimeSpan = None
        self.TimeUnit = None
        self.LoginSettings = None
        self.COSSettings = None
        self.SgId = None
        self.PreExecutedFileSettings = None
        self.AutoRenew = None
        self.ClientToken = None
        self.NeedMasterWan = None
        self.RemoteLoginAtCreate = None
        self.CheckSecurity = None
        self.ExtendFsField = None
        self.Tags = None
        self.DisasterRecoverGroupIds = None
        self.CbsEncrypt = None
        self.MetaType = None
        self.UnifyMetaInstanceId = None
        self.MetaDBInfo = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        if params.get("VPCSettings") is not None:
            self.VPCSettings = VPCSettings()
            self.VPCSettings._deserialize(params.get("VPCSettings"))
        self.Software = params.get("Software")
        if params.get("ResourceSpec") is not None:
            self.ResourceSpec = NewResourceSpec()
            self.ResourceSpec._deserialize(params.get("ResourceSpec"))
        self.SupportHA = params.get("SupportHA")
        self.InstanceName = params.get("InstanceName")
        self.PayMode = params.get("PayMode")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnit = params.get("TimeUnit")
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        if params.get("COSSettings") is not None:
            self.COSSettings = COSSettings()
            self.COSSettings._deserialize(params.get("COSSettings"))
        self.SgId = params.get("SgId")
        if params.get("PreExecutedFileSettings") is not None:
            self.PreExecutedFileSettings = []
            for item in params.get("PreExecutedFileSettings"):
                obj = PreExecuteFileSettings()
                obj._deserialize(item)
                self.PreExecutedFileSettings.append(obj)
        self.AutoRenew = params.get("AutoRenew")
        self.ClientToken = params.get("ClientToken")
        self.NeedMasterWan = params.get("NeedMasterWan")
        self.RemoteLoginAtCreate = params.get("RemoteLoginAtCreate")
        self.CheckSecurity = params.get("CheckSecurity")
        self.ExtendFsField = params.get("ExtendFsField")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        self.CbsEncrypt = params.get("CbsEncrypt")
        self.MetaType = params.get("MetaType")
        self.UnifyMetaInstanceId = params.get("UnifyMetaInstanceId")
        if params.get("MetaDBInfo") is not None:
            self.MetaDBInfo = CustomMetaInfo()
            self.MetaDBInfo._deserialize(params.get("MetaDBInfo"))


class CreateInstanceResponse(AbstractModel):
    """CreateInstance返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CustomMetaInfo(AbstractModel):
    """用戶自建Hive-MetaDB訊息

    """

    def __init__(self):
        """
        :param MetaDataJdbcUrl: 自定義MetaDB的JDBC連接，請以 jdbc:mysql:// 開頭
        :type MetaDataJdbcUrl: str
        :param MetaDataUser: 自定義MetaDB用戶名
        :type MetaDataUser: str
        :param MetaDataPass: 自定義MetaDB密碼
        :type MetaDataPass: str
        """
        self.MetaDataJdbcUrl = None
        self.MetaDataUser = None
        self.MetaDataPass = None


    def _deserialize(self, params):
        self.MetaDataJdbcUrl = params.get("MetaDataJdbcUrl")
        self.MetaDataUser = params.get("MetaDataUser")
        self.MetaDataPass = params.get("MetaDataPass")


class DescribeClusterNodesRequest(AbstractModel):
    """DescribeClusterNodes請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 集群實例ID,實例ID形如: emr-xxxxxxxx
        :type InstanceId: str
        :param NodeFlag: 節點标識，取值爲：
<li>all：表示獲取全部類型節點，cdb訊息除外。</li>
<li>master：表示獲取master節點訊息。</li>
<li>core：表示獲取core節點訊息。</li>
<li>task：表示獲取task節點訊息。</li>
<li>common：表示獲取common節點訊息。</li>
<li>router：表示獲取router節點訊息。</li>
<li>db：表示獲取正常狀态的cdb訊息。</li>
<li>recyle：表示獲取資源回收筒隔離中的節點訊息，包括cdb訊息。</li>
<li>renew：表示獲取所有待續約的節點訊息，包括cdb訊息，自動續約節點不會返回。</li>
注意：現在只支援以上取值，輸入其他值會導緻錯誤。
        :type NodeFlag: str
        :param Offset: 頁編号，預設值爲0，表示第一頁。
        :type Offset: int
        :param Limit: 每頁返回數量，預設值爲100，最大值爲100。
        :type Limit: int
        """
        self.InstanceId = None
        self.NodeFlag = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.NodeFlag = params.get("NodeFlag")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeClusterNodesResponse(AbstractModel):
    """DescribeClusterNodes返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCnt: 查詢到的節點總數
        :type TotalCnt: int
        :param NodeList: 節點詳細訊息清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type NodeList: list of NodeHardwareInfo
        :param TagKeys: 用戶所有的标簽鍵清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagKeys: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCnt = None
        self.NodeList = None
        self.TagKeys = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCnt = params.get("TotalCnt")
        if params.get("NodeList") is not None:
            self.NodeList = []
            for item in params.get("NodeList"):
                obj = NodeHardwareInfo()
                obj._deserialize(item)
                self.NodeList.append(obj)
        self.TagKeys = params.get("TagKeys")
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances請求參數結構體

    """

    def __init__(self):
        """
        :param DisplayStrategy: 集群篩選策略。取值範圍：
<li>clusterList：表示查詢除了已銷毀集群之外的集群清單。</li>
<li>monitorManage：表示查詢除了已銷毀、創建中以及創建失敗的集群之外的集群清單。</li>
<li>cloudHardwareManage/componentManage：目前這兩個取值爲預留取值，暫時和monitorManage表示同樣的含義。</li>
        :type DisplayStrategy: str
        :param InstanceIds: 按照一個或者多個實例ID查詢。實例ID形如: emr-xxxxxxxx 。(此參數的具體格式可參考API[簡介](https://cloud.taifucloud.com/document/api/213/15688)的 Ids.N 一節)。如果不填寫實例ID，返回該APPID下所有實例清單。
        :type InstanceIds: list of str
        :param Offset: 頁編号，預設值爲0，表示第一頁。
        :type Offset: int
        :param Limit: 每頁返回數量，預設值爲10，最大值爲100。
        :type Limit: int
        :param ProjectId: 建議必填-1，表示拉取所有項目下的集群。
不填預設值爲0，表示拉取預設項目下的集群。
實例所屬項目ID。該參數可以通過調用 [DescribeProject](https://cloud.taifucloud.com/document/api/378/4400) 的返回值中的 projectId 欄位來獲取。
        :type ProjectId: int
        :param OrderField: 排序欄位。取值範圍：
<li>clusterId：表示按照實例ID排序。</li>
<li>addTime：表示按照實例創建時間排序。</li>
<li>status：表示按照實例的狀态碼排序。</li>
        :type OrderField: str
        :param Asc: 按照OrderField升序或者降序進行排序。取值範圍：
<li>0：表示降序。</li>
<li>1：表示升序。</li>預設值爲0。
        :type Asc: int
        """
        self.DisplayStrategy = None
        self.InstanceIds = None
        self.Offset = None
        self.Limit = None
        self.ProjectId = None
        self.OrderField = None
        self.Asc = None


    def _deserialize(self, params):
        self.DisplayStrategy = params.get("DisplayStrategy")
        self.InstanceIds = params.get("InstanceIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ProjectId = params.get("ProjectId")
        self.OrderField = params.get("OrderField")
        self.Asc = params.get("Asc")


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCnt: 符合條件的實例總數。
        :type TotalCnt: int
        :param ClusterList: EMR實例詳細訊息清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterList: list of ClusterInstancesInfo
        :param TagKeys: 實例關聯的标簽鍵清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagKeys: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCnt = None
        self.ClusterList = None
        self.TagKeys = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCnt = params.get("TotalCnt")
        if params.get("ClusterList") is not None:
            self.ClusterList = []
            for item in params.get("ClusterList"):
                obj = ClusterInstancesInfo()
                obj._deserialize(item)
                self.ClusterList.append(obj)
        self.TagKeys = params.get("TagKeys")
        self.RequestId = params.get("RequestId")


class EmrProductConfigOutter(AbstractModel):
    """EMR産品配置

    """

    def __init__(self):
        """
        :param SoftInfo: 軟體訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type SoftInfo: list of str
        :param MasterNodeSize: Master節點個數
注意：此欄位可能返回 null，表示取不到有效值。
        :type MasterNodeSize: int
        :param CoreNodeSize: Core節點個數
注意：此欄位可能返回 null，表示取不到有效值。
        :type CoreNodeSize: int
        :param TaskNodeSize: Task節點個數
注意：此欄位可能返回 null，表示取不到有效值。
        :type TaskNodeSize: int
        :param ComNodeSize: Common節點個數
注意：此欄位可能返回 null，表示取不到有效值。
        :type ComNodeSize: int
        :param MasterResource: Master節點資源
注意：此欄位可能返回 null，表示取不到有效值。
        :type MasterResource: :class:`taifucloudcloud.emr.v20190103.models.OutterResource`
        :param CoreResource: Core節點資源
注意：此欄位可能返回 null，表示取不到有效值。
        :type CoreResource: :class:`taifucloudcloud.emr.v20190103.models.OutterResource`
        :param TaskResource: Task節點資源
注意：此欄位可能返回 null，表示取不到有效值。
        :type TaskResource: :class:`taifucloudcloud.emr.v20190103.models.OutterResource`
        :param ComResource: Common節點資源
注意：此欄位可能返回 null，表示取不到有效值。
        :type ComResource: :class:`taifucloudcloud.emr.v20190103.models.OutterResource`
        :param OnCos: 是否使用COS
注意：此欄位可能返回 null，表示取不到有效值。
        :type OnCos: bool
        :param ChargeType: 收費類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type ChargeType: int
        :param RouterNodeSize: Router節點個數
注意：此欄位可能返回 null，表示取不到有效值。
        :type RouterNodeSize: int
        :param SupportHA: 是否支援HA
注意：此欄位可能返回 null，表示取不到有效值。
        :type SupportHA: bool
        :param SecurityOn: 是否支援安全模式
注意：此欄位可能返回 null，表示取不到有效值。
        :type SecurityOn: bool
        :param SecurityGroup: 安全組名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type SecurityGroup: str
        :param CbsEncrypt: 是否開啓Cbs加密
注意：此欄位可能返回 null，表示取不到有效值。
        :type CbsEncrypt: int
        """
        self.SoftInfo = None
        self.MasterNodeSize = None
        self.CoreNodeSize = None
        self.TaskNodeSize = None
        self.ComNodeSize = None
        self.MasterResource = None
        self.CoreResource = None
        self.TaskResource = None
        self.ComResource = None
        self.OnCos = None
        self.ChargeType = None
        self.RouterNodeSize = None
        self.SupportHA = None
        self.SecurityOn = None
        self.SecurityGroup = None
        self.CbsEncrypt = None


    def _deserialize(self, params):
        self.SoftInfo = params.get("SoftInfo")
        self.MasterNodeSize = params.get("MasterNodeSize")
        self.CoreNodeSize = params.get("CoreNodeSize")
        self.TaskNodeSize = params.get("TaskNodeSize")
        self.ComNodeSize = params.get("ComNodeSize")
        if params.get("MasterResource") is not None:
            self.MasterResource = OutterResource()
            self.MasterResource._deserialize(params.get("MasterResource"))
        if params.get("CoreResource") is not None:
            self.CoreResource = OutterResource()
            self.CoreResource._deserialize(params.get("CoreResource"))
        if params.get("TaskResource") is not None:
            self.TaskResource = OutterResource()
            self.TaskResource._deserialize(params.get("TaskResource"))
        if params.get("ComResource") is not None:
            self.ComResource = OutterResource()
            self.ComResource._deserialize(params.get("ComResource"))
        self.OnCos = params.get("OnCos")
        self.ChargeType = params.get("ChargeType")
        self.RouterNodeSize = params.get("RouterNodeSize")
        self.SupportHA = params.get("SupportHA")
        self.SecurityOn = params.get("SecurityOn")
        self.SecurityGroup = params.get("SecurityGroup")
        self.CbsEncrypt = params.get("CbsEncrypt")


class InquiryPriceCreateInstanceRequest(AbstractModel):
    """InquiryPriceCreateInstance請求參數結構體

    """

    def __init__(self):
        """
        :param TimeUnit: 購買實例的時間單位。取值範圍：
<li>s：表示秒。PayMode取值爲0時，TimeUnit只能取值爲s。</li>
<li>m：表示月份。PayMode取值爲1時，TimeUnit只能取值爲m。</li>
        :type TimeUnit: str
        :param TimeSpan: 購買實例的時長。結合TimeUnit一起使用。
<li>TimeUnit爲s時，該參數只能填寫3600，表示按量計費實例。</li>
<li>TimeUnit爲m時，該參數填寫的數字表示包年包月實例的購買時長，如1表示購買一個月</li>
        :type TimeSpan: int
        :param ResourceSpec: 詢價的節點規格。
        :type ResourceSpec: :class:`taifucloudcloud.emr.v20190103.models.NewResourceSpec`
        :param Currency: 貨币種類。取值範圍：
<li>CNY：表示人民币。</li>
        :type Currency: str
        :param PayMode: 實例計費模式。取值範圍：
<li>0：表示按量計費。</li>
<li>1：表示包年包月。</li>
        :type PayMode: int
        :param SupportHA: 是否開啓節點高可用。取值範圍：
<li>0：表示不開啓節點高可用。</li>
<li>1：表示開啓節點高可用。</li>
        :type SupportHA: int
        :param Software: 佈署的元件清單。不同的EMR産品ID（ProductId：具體含義參考入參ProductId欄位）需要選擇不同的必選元件：
<li>ProductId爲1的時候，必選元件包括：hadoop-2.7.3、knox-1.2.0、zookeeper-3.4.9</li>
<li>ProductId爲2的時候，必選元件包括：hadoop-2.7.3、knox-1.2.0、zookeeper-3.4.9</li>
<li>ProductId爲4的時候，必選元件包括：hadoop-2.8.4、knox-1.2.0、zookeeper-3.4.9</li>
<li>ProductId爲7的時候，必選元件包括：hadoop-3.1.2、knox-1.2.0、zookeeper-3.4.9</li>
        :type Software: list of str
        :param Placement: 實例所在的位置。通過該參數可以指定實例所屬可用區，所屬項目等屬性。
        :type Placement: :class:`taifucloudcloud.emr.v20190103.models.Placement`
        :param VPCSettings: 私有網絡相關訊息配置。通過該參數可以指定私有網絡的ID，子網ID等訊息。
        :type VPCSettings: :class:`taifucloudcloud.emr.v20190103.models.VPCSettings`
        :param MetaType: hive共享中繼資料庫類型。取值範圍：
<li>EMR_NEW_META：表示集群預設創建</li>
<li>EMR_EXIT_METE：表示集群使用指定EMR-MetaDB。</li>
<li>USER_CUSTOM_META：表示集群使用自定義MetaDB。</li>
        :type MetaType: str
        :param UnifyMetaInstanceId: EMR-MetaDB實例
        :type UnifyMetaInstanceId: str
        :param MetaDBInfo: 自定義MetaDB訊息
        :type MetaDBInfo: :class:`taifucloudcloud.emr.v20190103.models.CustomMetaInfo`
        :param ProductId: 産品ID，不同産品ID表示不同的EMR産品版本。取值範圍：
<li>1：表示EMR-V1.3.1。</li>
<li>2：表示EMR-V2.0.1。</li>
<li>4：表示EMR-V2.1.0。</li>
<li>7：表示EMR-V3.0.0。</li>
        :type ProductId: int
        """
        self.TimeUnit = None
        self.TimeSpan = None
        self.ResourceSpec = None
        self.Currency = None
        self.PayMode = None
        self.SupportHA = None
        self.Software = None
        self.Placement = None
        self.VPCSettings = None
        self.MetaType = None
        self.UnifyMetaInstanceId = None
        self.MetaDBInfo = None
        self.ProductId = None


    def _deserialize(self, params):
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        if params.get("ResourceSpec") is not None:
            self.ResourceSpec = NewResourceSpec()
            self.ResourceSpec._deserialize(params.get("ResourceSpec"))
        self.Currency = params.get("Currency")
        self.PayMode = params.get("PayMode")
        self.SupportHA = params.get("SupportHA")
        self.Software = params.get("Software")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        if params.get("VPCSettings") is not None:
            self.VPCSettings = VPCSettings()
            self.VPCSettings._deserialize(params.get("VPCSettings"))
        self.MetaType = params.get("MetaType")
        self.UnifyMetaInstanceId = params.get("UnifyMetaInstanceId")
        if params.get("MetaDBInfo") is not None:
            self.MetaDBInfo = CustomMetaInfo()
            self.MetaDBInfo._deserialize(params.get("MetaDBInfo"))
        self.ProductId = params.get("ProductId")


class InquiryPriceCreateInstanceResponse(AbstractModel):
    """InquiryPriceCreateInstance返回參數結構體

    """

    def __init__(self):
        """
        :param OriginalCost: 原價，單位爲元。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OriginalCost: float
        :param DiscountCost: 折扣價，單位爲元。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DiscountCost: float
        :param TimeUnit: 購買實例的時間單位。取值範圍：
<li>s：表示秒。</li>
<li>m：表示月份。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type TimeUnit: str
        :param TimeSpan: 購買實例的時長。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TimeSpan: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.OriginalCost = None
        self.DiscountCost = None
        self.TimeUnit = None
        self.TimeSpan = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalCost = params.get("OriginalCost")
        self.DiscountCost = params.get("DiscountCost")
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.RequestId = params.get("RequestId")


class InquiryPriceRenewInstanceRequest(AbstractModel):
    """InquiryPriceRenewInstance請求參數結構體

    """

    def __init__(self):
        """
        :param TimeSpan: 實例續約的時長。需要結合TimeUnit一起使用。1表示續約1一個月
        :type TimeSpan: int
        :param ResourceIds: 待續約節點的資源ID清單。資源ID形如：emr-vm-xxxxxxxx。有效的資源ID可通過登入[控制台](https://console.cloud.taifucloud.com/emr/static/hardware)查詢。
        :type ResourceIds: list of str
        :param Placement: 實例所在的位置。通過該參數可以指定實例所屬可用區，所屬項目等屬性。
        :type Placement: :class:`taifucloudcloud.emr.v20190103.models.Placement`
        :param PayMode: 實例計費模式。此處只支援取值爲1，表示包年包月。
        :type PayMode: int
        :param TimeUnit: 實例續約的時間單位。取值範圍：
<li>m：表示月份。</li>
        :type TimeUnit: str
        :param Currency: 貨币種類。取值範圍：
<li>CNY：表示人民币。</li>
        :type Currency: str
        """
        self.TimeSpan = None
        self.ResourceIds = None
        self.Placement = None
        self.PayMode = None
        self.TimeUnit = None
        self.Currency = None


    def _deserialize(self, params):
        self.TimeSpan = params.get("TimeSpan")
        self.ResourceIds = params.get("ResourceIds")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.PayMode = params.get("PayMode")
        self.TimeUnit = params.get("TimeUnit")
        self.Currency = params.get("Currency")


class InquiryPriceRenewInstanceResponse(AbstractModel):
    """InquiryPriceRenewInstance返回參數結構體

    """

    def __init__(self):
        """
        :param OriginalCost: 原價，單位爲元。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OriginalCost: float
        :param DiscountCost: 折扣價，單位爲元。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DiscountCost: float
        :param TimeUnit: 實例續約的時間單位。取值範圍：
<li>m：表示月份。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type TimeUnit: str
        :param TimeSpan: 實例續約的時長。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TimeSpan: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.OriginalCost = None
        self.DiscountCost = None
        self.TimeUnit = None
        self.TimeSpan = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalCost = params.get("OriginalCost")
        self.DiscountCost = params.get("DiscountCost")
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.RequestId = params.get("RequestId")


class InquiryPriceScaleOutInstanceRequest(AbstractModel):
    """InquiryPriceScaleOutInstance請求參數結構體

    """

    def __init__(self):
        """
        :param TimeUnit: 擴容的時間單位。取值範圍：
<li>s：表示秒。PayMode取值爲0時，TimeUnit只能取值爲s。</li>
<li>m：表示月份。PayMode取值爲1時，TimeUnit只能取值爲m。</li>
        :type TimeUnit: str
        :param TimeSpan: 擴容的時長。結合TimeUnit一起使用。
<li>TimeUnit爲s時，該參數只能填寫3600，表示按量計費實例。</li>
<li>TimeUnit爲m時，該參數填寫的數字表示包年包月實例的購買時長，如1表示購買一個月</li>
        :type TimeSpan: int
        :param ZoneId: 實例所屬的可用區ID，例如100003。該參數可以通過調用 [DescribeZones](https://cloud.taifucloud.com/document/api/213/15707) 的返回值中的ZoneId欄位來獲取。
        :type ZoneId: int
        :param PayMode: 實例計費模式。取值範圍：
<li>0：表示按量計費。</li>
<li>1：表示包年包月。</li>
        :type PayMode: int
        :param InstanceId: 實例ID。
        :type InstanceId: str
        :param CoreCount: 擴容的Core節點數量。
        :type CoreCount: int
        :param TaskCount: 擴容的Task節點數量。
        :type TaskCount: int
        :param Currency: 貨币種類。取值範圍：
<li>CNY：表示人民币。</li>
        :type Currency: str
        :param RouterCount: 擴容的Router節點數量。
        :type RouterCount: int
        """
        self.TimeUnit = None
        self.TimeSpan = None
        self.ZoneId = None
        self.PayMode = None
        self.InstanceId = None
        self.CoreCount = None
        self.TaskCount = None
        self.Currency = None
        self.RouterCount = None


    def _deserialize(self, params):
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.ZoneId = params.get("ZoneId")
        self.PayMode = params.get("PayMode")
        self.InstanceId = params.get("InstanceId")
        self.CoreCount = params.get("CoreCount")
        self.TaskCount = params.get("TaskCount")
        self.Currency = params.get("Currency")
        self.RouterCount = params.get("RouterCount")


class InquiryPriceScaleOutInstanceResponse(AbstractModel):
    """InquiryPriceScaleOutInstance返回參數結構體

    """

    def __init__(self):
        """
        :param OriginalCost: 原價，單位爲元。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OriginalCost: str
        :param DiscountCost: 折扣價，單位爲元。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DiscountCost: str
        :param Unit: 擴容的時間單位。取值範圍：
<li>s：表示秒。</li>
<li>m：表示月份。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type Unit: str
        :param PriceSpec: 詢價的節點規格。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PriceSpec: :class:`taifucloudcloud.emr.v20190103.models.PriceResource`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.OriginalCost = None
        self.DiscountCost = None
        self.Unit = None
        self.PriceSpec = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalCost = params.get("OriginalCost")
        self.DiscountCost = params.get("DiscountCost")
        self.Unit = params.get("Unit")
        if params.get("PriceSpec") is not None:
            self.PriceSpec = PriceResource()
            self.PriceSpec._deserialize(params.get("PriceSpec"))
        self.RequestId = params.get("RequestId")


class InquiryPriceUpdateInstanceRequest(AbstractModel):
    """InquiryPriceUpdateInstance請求參數結構體

    """

    def __init__(self):
        """
        :param TimeUnit: 變配的時間單位。取值範圍：
<li>s：表示秒。PayMode取值爲0時，TimeUnit只能取值爲s。</li>
<li>m：表示月份。PayMode取值爲1時，TimeUnit只能取值爲m。</li>
        :type TimeUnit: str
        :param TimeSpan: 變配的時長。結合TimeUnit一起使用。
<li>TimeUnit爲s時，該參數只能填寫3600，表示按量計費實例。</li>
<li>TimeUnit爲m時，該參數填寫的數字表示包年包月實例的購買時長，如1表示購買一個月</li>
        :type TimeSpan: int
        :param UpdateSpec: 節點變配的目标配置。
        :type UpdateSpec: :class:`taifucloudcloud.emr.v20190103.models.UpdateInstanceSettings`
        :param PayMode: 實例計費模式。取值範圍：
<li>0：表示按量計費。</li>
<li>1：表示包年包月。</li>
        :type PayMode: int
        :param Placement: 實例所在的位置。通過該參數可以指定實例所屬可用區，所屬項目等屬性。
        :type Placement: :class:`taifucloudcloud.emr.v20190103.models.Placement`
        :param Currency: 貨币種類。取值範圍：
<li>CNY：表示人民币。</li>
        :type Currency: str
        """
        self.TimeUnit = None
        self.TimeSpan = None
        self.UpdateSpec = None
        self.PayMode = None
        self.Placement = None
        self.Currency = None


    def _deserialize(self, params):
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        if params.get("UpdateSpec") is not None:
            self.UpdateSpec = UpdateInstanceSettings()
            self.UpdateSpec._deserialize(params.get("UpdateSpec"))
        self.PayMode = params.get("PayMode")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.Currency = params.get("Currency")


class InquiryPriceUpdateInstanceResponse(AbstractModel):
    """InquiryPriceUpdateInstance返回參數結構體

    """

    def __init__(self):
        """
        :param OriginalCost: 原價，單位爲元。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OriginalCost: float
        :param DiscountCost: 折扣價，單位爲元。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DiscountCost: float
        :param TimeUnit: 變配的時間單位。取值範圍：
<li>s：表示秒。</li>
<li>m：表示月份。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type TimeUnit: str
        :param TimeSpan: 變配的時長。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TimeSpan: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.OriginalCost = None
        self.DiscountCost = None
        self.TimeUnit = None
        self.TimeSpan = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalCost = params.get("OriginalCost")
        self.DiscountCost = params.get("DiscountCost")
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.RequestId = params.get("RequestId")


class LoginSettings(AbstractModel):
    """登入設置

    """

    def __init__(self):
        """
        :param Password: Password
        :type Password: str
        :param PublicKeyId: Public Key
        :type PublicKeyId: str
        """
        self.Password = None
        self.PublicKeyId = None


    def _deserialize(self, params):
        self.Password = params.get("Password")
        self.PublicKeyId = params.get("PublicKeyId")


class MultiDisk(AbstractModel):
    """多雲盤參數

    """

    def __init__(self):
        """
        :param DiskType: 雲盤類型("CLOUD_PREMIUM","CLOUD_SSD","CLOUD_BASIC")的一種
        :type DiskType: str
        :param Volume: 雲盤大小
        :type Volume: int
        :param Count: 該類型雲盤個數
        :type Count: int
        """
        self.DiskType = None
        self.Volume = None
        self.Count = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.Volume = params.get("Volume")
        self.Count = params.get("Count")


class MultiDiskMC(AbstractModel):
    """多雲盤參數

    """

    def __init__(self):
        """
        :param Count: 該類型雲盤個數
注意：此欄位可能返回 null，表示取不到有效值。
        :type Count: int
        :param Type: 磁盤類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type Type: int
        :param Volume: 雲盤大小
注意：此欄位可能返回 null，表示取不到有效值。
        :type Volume: int
        """
        self.Count = None
        self.Type = None
        self.Volume = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.Type = params.get("Type")
        self.Volume = params.get("Volume")


class NewResourceSpec(AbstractModel):
    """資源描述

    """

    def __init__(self):
        """
        :param MasterResourceSpec: 描述Master節點資源
        :type MasterResourceSpec: :class:`taifucloudcloud.emr.v20190103.models.Resource`
        :param CoreResourceSpec: 描述Core節點資源
        :type CoreResourceSpec: :class:`taifucloudcloud.emr.v20190103.models.Resource`
        :param TaskResourceSpec: 描述Task節點資源
        :type TaskResourceSpec: :class:`taifucloudcloud.emr.v20190103.models.Resource`
        :param MasterCount: Master節點數量
        :type MasterCount: int
        :param CoreCount: Core節點數量
        :type CoreCount: int
        :param TaskCount: Task節點數量
        :type TaskCount: int
        :param CommonResourceSpec: 描述Common節點資源
        :type CommonResourceSpec: :class:`taifucloudcloud.emr.v20190103.models.Resource`
        :param CommonCount: Common節點數量
        :type CommonCount: int
        """
        self.MasterResourceSpec = None
        self.CoreResourceSpec = None
        self.TaskResourceSpec = None
        self.MasterCount = None
        self.CoreCount = None
        self.TaskCount = None
        self.CommonResourceSpec = None
        self.CommonCount = None


    def _deserialize(self, params):
        if params.get("MasterResourceSpec") is not None:
            self.MasterResourceSpec = Resource()
            self.MasterResourceSpec._deserialize(params.get("MasterResourceSpec"))
        if params.get("CoreResourceSpec") is not None:
            self.CoreResourceSpec = Resource()
            self.CoreResourceSpec._deserialize(params.get("CoreResourceSpec"))
        if params.get("TaskResourceSpec") is not None:
            self.TaskResourceSpec = Resource()
            self.TaskResourceSpec._deserialize(params.get("TaskResourceSpec"))
        self.MasterCount = params.get("MasterCount")
        self.CoreCount = params.get("CoreCount")
        self.TaskCount = params.get("TaskCount")
        if params.get("CommonResourceSpec") is not None:
            self.CommonResourceSpec = Resource()
            self.CommonResourceSpec._deserialize(params.get("CommonResourceSpec"))
        self.CommonCount = params.get("CommonCount")


class NodeHardwareInfo(AbstractModel):
    """節點硬體訊息

    """

    def __init__(self):
        """
        :param AppId: 用戶APPID
注意：此欄位可能返回 null，表示取不到有效值。
        :type AppId: int
        :param SerialNo: 序列号
注意：此欄位可能返回 null，表示取不到有效值。
        :type SerialNo: str
        :param OrderNo: 機器實例ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type OrderNo: str
        :param WanIp: master節點綁定外網IP
注意：此欄位可能返回 null，表示取不到有效值。
        :type WanIp: str
        :param Flag: 節點類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type Flag: int
        :param Spec: 節點規格
注意：此欄位可能返回 null，表示取不到有效值。
        :type Spec: str
        :param CpuNum: 節點核數
注意：此欄位可能返回 null，表示取不到有效值。
        :type CpuNum: int
        :param MemSize: 節點内存
注意：此欄位可能返回 null，表示取不到有效值。
        :type MemSize: int
        :param MemDesc: 節點内存描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type MemDesc: str
        :param RegionId: 節點所在region
注意：此欄位可能返回 null，表示取不到有效值。
        :type RegionId: int
        :param ZoneId: 節點所在Zone
注意：此欄位可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param ApplyTime: 申請時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplyTime: str
        :param FreeTime: 釋放時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type FreeTime: str
        :param DiskSize: 硬碟大小
注意：此欄位可能返回 null，表示取不到有效值。
        :type DiskSize: str
        :param NameTag: 節點描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type NameTag: str
        :param Services: 節點佈署服務
注意：此欄位可能返回 null，表示取不到有效值。
        :type Services: str
        :param StorageType: 磁盤類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type StorageType: int
        :param RootSize: 系統盤大小
注意：此欄位可能返回 null，表示取不到有效值。
        :type RootSize: int
        :param ChargeType: 付費類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type ChargeType: int
        :param CdbIp: 資料庫IP
注意：此欄位可能返回 null，表示取不到有效值。
        :type CdbIp: str
        :param CdbPort: 資料庫端口
注意：此欄位可能返回 null，表示取不到有效值。
        :type CdbPort: int
        :param HwDiskSize: 硬碟容量
注意：此欄位可能返回 null，表示取不到有效值。
        :type HwDiskSize: int
        :param HwDiskSizeDesc: 硬碟容量描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type HwDiskSizeDesc: str
        :param HwMemSize: 内存容量
注意：此欄位可能返回 null，表示取不到有效值。
        :type HwMemSize: int
        :param HwMemSizeDesc: 内存容量描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type HwMemSizeDesc: str
        :param ExpireTime: 過期時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param EmrResourceId: 節點資源ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type EmrResourceId: str
        :param IsAutoRenew: 續約标志
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsAutoRenew: int
        :param DeviceClass: 設備标識
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeviceClass: str
        :param Mutable: 支援變配
注意：此欄位可能返回 null，表示取不到有效值。
        :type Mutable: int
        :param MCMultiDisk: 多雲盤
注意：此欄位可能返回 null，表示取不到有效值。
        :type MCMultiDisk: list of MultiDiskMC
        :param CdbNodeInfo: 資料庫訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type CdbNodeInfo: :class:`taifucloudcloud.emr.v20190103.models.CdbInfo`
        :param Ip: 内網IP
注意：此欄位可能返回 null，表示取不到有效值。
        :type Ip: str
        :param Destroyable: 此節點是否可銷毀，1可銷毀，0不可銷毀
注意：此欄位可能返回 null，表示取不到有效值。
        :type Destroyable: int
        :param Tags: 節點綁定的标簽
注意：此欄位可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param AutoFlag: 是否是自動擴縮容節點，0爲普通節點，1爲自動擴縮容節點。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AutoFlag: int
        """
        self.AppId = None
        self.SerialNo = None
        self.OrderNo = None
        self.WanIp = None
        self.Flag = None
        self.Spec = None
        self.CpuNum = None
        self.MemSize = None
        self.MemDesc = None
        self.RegionId = None
        self.ZoneId = None
        self.ApplyTime = None
        self.FreeTime = None
        self.DiskSize = None
        self.NameTag = None
        self.Services = None
        self.StorageType = None
        self.RootSize = None
        self.ChargeType = None
        self.CdbIp = None
        self.CdbPort = None
        self.HwDiskSize = None
        self.HwDiskSizeDesc = None
        self.HwMemSize = None
        self.HwMemSizeDesc = None
        self.ExpireTime = None
        self.EmrResourceId = None
        self.IsAutoRenew = None
        self.DeviceClass = None
        self.Mutable = None
        self.MCMultiDisk = None
        self.CdbNodeInfo = None
        self.Ip = None
        self.Destroyable = None
        self.Tags = None
        self.AutoFlag = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.SerialNo = params.get("SerialNo")
        self.OrderNo = params.get("OrderNo")
        self.WanIp = params.get("WanIp")
        self.Flag = params.get("Flag")
        self.Spec = params.get("Spec")
        self.CpuNum = params.get("CpuNum")
        self.MemSize = params.get("MemSize")
        self.MemDesc = params.get("MemDesc")
        self.RegionId = params.get("RegionId")
        self.ZoneId = params.get("ZoneId")
        self.ApplyTime = params.get("ApplyTime")
        self.FreeTime = params.get("FreeTime")
        self.DiskSize = params.get("DiskSize")
        self.NameTag = params.get("NameTag")
        self.Services = params.get("Services")
        self.StorageType = params.get("StorageType")
        self.RootSize = params.get("RootSize")
        self.ChargeType = params.get("ChargeType")
        self.CdbIp = params.get("CdbIp")
        self.CdbPort = params.get("CdbPort")
        self.HwDiskSize = params.get("HwDiskSize")
        self.HwDiskSizeDesc = params.get("HwDiskSizeDesc")
        self.HwMemSize = params.get("HwMemSize")
        self.HwMemSizeDesc = params.get("HwMemSizeDesc")
        self.ExpireTime = params.get("ExpireTime")
        self.EmrResourceId = params.get("EmrResourceId")
        self.IsAutoRenew = params.get("IsAutoRenew")
        self.DeviceClass = params.get("DeviceClass")
        self.Mutable = params.get("Mutable")
        if params.get("MCMultiDisk") is not None:
            self.MCMultiDisk = []
            for item in params.get("MCMultiDisk"):
                obj = MultiDiskMC()
                obj._deserialize(item)
                self.MCMultiDisk.append(obj)
        if params.get("CdbNodeInfo") is not None:
            self.CdbNodeInfo = CdbInfo()
            self.CdbNodeInfo._deserialize(params.get("CdbNodeInfo"))
        self.Ip = params.get("Ip")
        self.Destroyable = params.get("Destroyable")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AutoFlag = params.get("AutoFlag")


class OutterResource(AbstractModel):
    """資源詳情

    """

    def __init__(self):
        """
        :param Spec: 規格
注意：此欄位可能返回 null，表示取不到有效值。
        :type Spec: str
        :param SpecName: 規格名
注意：此欄位可能返回 null，表示取不到有效值。
        :type SpecName: str
        :param StorageType: 硬碟類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type StorageType: int
        :param DiskType: 硬碟類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param RootSize: 系統盤大小
注意：此欄位可能返回 null，表示取不到有效值。
        :type RootSize: int
        :param MemSize: 内存大小
注意：此欄位可能返回 null，表示取不到有效值。
        :type MemSize: int
        :param Cpu: CPU個數
注意：此欄位可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param DiskSize: 硬碟大小
注意：此欄位可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param InstanceType: 規格
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceType: str
        """
        self.Spec = None
        self.SpecName = None
        self.StorageType = None
        self.DiskType = None
        self.RootSize = None
        self.MemSize = None
        self.Cpu = None
        self.DiskSize = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.Spec = params.get("Spec")
        self.SpecName = params.get("SpecName")
        self.StorageType = params.get("StorageType")
        self.DiskType = params.get("DiskType")
        self.RootSize = params.get("RootSize")
        self.MemSize = params.get("MemSize")
        self.Cpu = params.get("Cpu")
        self.DiskSize = params.get("DiskSize")
        self.InstanceType = params.get("InstanceType")


class Placement(AbstractModel):
    """描述集群實例位置訊息

    """

    def __init__(self):
        """
        :param ProjectId: 實例所屬項目ID。該參數可以通過調用 DescribeProject 的返回值中的 projectId 欄位來獲取。填0爲預設項目。
        :type ProjectId: int
        :param Zone: 實例所屬的可用區，例如ap-guangzhou-1。該參數也可以通過調用 DescribeZones 的返回值中的Zone欄位來獲取。
        :type Zone: str
        """
        self.ProjectId = None
        self.Zone = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Zone = params.get("Zone")


class PreExecuteFileSettings(AbstractModel):
    """預執行腳本配置

    """

    def __init__(self):
        """
        :param Path: 腳本在COS上路徑，已廢棄
        :type Path: str
        :param Args: 執行腳本參數
        :type Args: list of str
        :param Bucket: COS的Bucket名稱，已廢棄
        :type Bucket: str
        :param Region: COS的Region名稱，已廢棄
        :type Region: str
        :param Domain: COS的Domain數據，已廢棄
        :type Domain: str
        :param RunOrder: 執行順序
        :type RunOrder: int
        :param WhenRun: resourceAfter 或 clusterAfter
        :type WhenRun: str
        :param CosFileName: 腳本文件名，已廢棄
        :type CosFileName: str
        :param CosFileURI: 腳本的cos網址
        :type CosFileURI: str
        :param CosSecretId: cos的SecretId
        :type CosSecretId: str
        :param CosSecretKey: Cos的SecretKey
        :type CosSecretKey: str
        :param AppId: cos的appid，已廢棄
        :type AppId: str
        """
        self.Path = None
        self.Args = None
        self.Bucket = None
        self.Region = None
        self.Domain = None
        self.RunOrder = None
        self.WhenRun = None
        self.CosFileName = None
        self.CosFileURI = None
        self.CosSecretId = None
        self.CosSecretKey = None
        self.AppId = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Args = params.get("Args")
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.Domain = params.get("Domain")
        self.RunOrder = params.get("RunOrder")
        self.WhenRun = params.get("WhenRun")
        self.CosFileName = params.get("CosFileName")
        self.CosFileURI = params.get("CosFileURI")
        self.CosSecretId = params.get("CosSecretId")
        self.CosSecretKey = params.get("CosSecretKey")
        self.AppId = params.get("AppId")


class PriceResource(AbstractModel):
    """詢價資源

    """

    def __init__(self):
        """
        :param Spec: 需要的規格
注意：此欄位可能返回 null，表示取不到有效值。
        :type Spec: str
        :param StorageType: 硬碟類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type StorageType: int
        :param DiskType: 硬碟類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param RootSize: 系統盤大小
注意：此欄位可能返回 null，表示取不到有效值。
        :type RootSize: int
        :param MemSize: 内存大小
注意：此欄位可能返回 null，表示取不到有效值。
        :type MemSize: int
        :param Cpu: 核心數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param DiskSize: 硬碟大小
注意：此欄位可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param MultiDisks: 雲盤清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type MultiDisks: list of MultiDisk
        :param DiskCnt: 磁盤數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type DiskCnt: int
        :param InstanceType: 規格
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param Tags: 标簽
注意：此欄位可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param DiskNum: 磁盤數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type DiskNum: int
        :param LocalDiskNum: 本地盤的數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type LocalDiskNum: int
        """
        self.Spec = None
        self.StorageType = None
        self.DiskType = None
        self.RootSize = None
        self.MemSize = None
        self.Cpu = None
        self.DiskSize = None
        self.MultiDisks = None
        self.DiskCnt = None
        self.InstanceType = None
        self.Tags = None
        self.DiskNum = None
        self.LocalDiskNum = None


    def _deserialize(self, params):
        self.Spec = params.get("Spec")
        self.StorageType = params.get("StorageType")
        self.DiskType = params.get("DiskType")
        self.RootSize = params.get("RootSize")
        self.MemSize = params.get("MemSize")
        self.Cpu = params.get("Cpu")
        self.DiskSize = params.get("DiskSize")
        if params.get("MultiDisks") is not None:
            self.MultiDisks = []
            for item in params.get("MultiDisks"):
                obj = MultiDisk()
                obj._deserialize(item)
                self.MultiDisks.append(obj)
        self.DiskCnt = params.get("DiskCnt")
        self.InstanceType = params.get("InstanceType")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.DiskNum = params.get("DiskNum")
        self.LocalDiskNum = params.get("LocalDiskNum")


class Resource(AbstractModel):
    """資源詳情

    """

    def __init__(self):
        """
        :param Spec: 節點規格描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type Spec: str
        :param StorageType: 儲存類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type StorageType: int
        :param DiskType: 磁盤類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param MemSize: 内存容量,單位爲M
注意：此欄位可能返回 null，表示取不到有效值。
        :type MemSize: int
        :param Cpu: CPU核數
注意：此欄位可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param DiskSize: 數據盤容量
注意：此欄位可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param RootSize: 系統盤容量
注意：此欄位可能返回 null，表示取不到有效值。
        :type RootSize: int
        :param MultiDisks: 雲盤清單，當數據盤爲一塊雲盤時，直接使用DiskType和DiskSize參數，超出部分使用MultiDisks
注意：此欄位可能返回 null，表示取不到有效值。
        :type MultiDisks: list of MultiDisk
        :param Tags: 需要綁定的标簽清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param InstanceType: 規格類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param LocalDiskNum: 本地盤數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type LocalDiskNum: int
        :param DiskNum: 盤數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type DiskNum: int
        """
        self.Spec = None
        self.StorageType = None
        self.DiskType = None
        self.MemSize = None
        self.Cpu = None
        self.DiskSize = None
        self.RootSize = None
        self.MultiDisks = None
        self.Tags = None
        self.InstanceType = None
        self.LocalDiskNum = None
        self.DiskNum = None


    def _deserialize(self, params):
        self.Spec = params.get("Spec")
        self.StorageType = params.get("StorageType")
        self.DiskType = params.get("DiskType")
        self.MemSize = params.get("MemSize")
        self.Cpu = params.get("Cpu")
        self.DiskSize = params.get("DiskSize")
        self.RootSize = params.get("RootSize")
        if params.get("MultiDisks") is not None:
            self.MultiDisks = []
            for item in params.get("MultiDisks"):
                obj = MultiDisk()
                obj._deserialize(item)
                self.MultiDisks.append(obj)
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.InstanceType = params.get("InstanceType")
        self.LocalDiskNum = params.get("LocalDiskNum")
        self.DiskNum = params.get("DiskNum")


class ScaleOutInstanceRequest(AbstractModel):
    """ScaleOutInstance請求參數結構體

    """

    def __init__(self):
        """
        :param TimeUnit: 擴容的時間單位。取值範圍：
<li>s：表示秒。PayMode取值爲0時，TimeUnit只能取值爲s。</li>
<li>m：表示月份。PayMode取值爲1時，TimeUnit只能取值爲m。</li>
        :type TimeUnit: str
        :param TimeSpan: 擴容的時長。結合TimeUnit一起使用。
<li>TimeUnit爲s時，該參數只能填寫3600，表示按量計費實例。</li>
<li>TimeUnit爲m時，該參數填寫的數字表示包年包月實例的購買時長，如1表示購買一個月</li>
        :type TimeSpan: int
        :param InstanceId: 實例ID。
        :type InstanceId: str
        :param PayMode: 實例計費模式。取值範圍：
<li>0：表示按量計費。</li>
<li>1：表示包年包月。</li>
        :type PayMode: int
        :param ClientToken: 用戶端Token。
        :type ClientToken: str
        :param PreExecutedFileSettings: 引導操作腳本設置。
        :type PreExecutedFileSettings: list of PreExecuteFileSettings
        :param TaskCount: 擴容的Task節點數量。
        :type TaskCount: int
        :param CoreCount: 擴容的Core節點數量。
        :type CoreCount: int
        :param UnNecessaryNodeList: 擴容時不需要安裝的程式。
        :type UnNecessaryNodeList: list of int non-negative
        :param RouterCount: 擴容的Router節點數量。
        :type RouterCount: int
        :param SoftDeployInfo: 佈署的服務。
<li>SoftDeployInfo和ServiceNodeInfo是同組參數，和UnNecessaryNodeList參數互斥。</li>
<li>建議使用SoftDeployInfo和ServiceNodeInfo組合。</li>
        :type SoftDeployInfo: list of int non-negative
        :param ServiceNodeInfo: 啓動的程式。
        :type ServiceNodeInfo: list of int non-negative
        :param DisasterRecoverGroupIds: 分散置放群組ID清單，當前僅支援指定一個。
        :type DisasterRecoverGroupIds: list of str
        :param Tags: 擴容節點綁定标簽清單。
        :type Tags: list of Tag
        """
        self.TimeUnit = None
        self.TimeSpan = None
        self.InstanceId = None
        self.PayMode = None
        self.ClientToken = None
        self.PreExecutedFileSettings = None
        self.TaskCount = None
        self.CoreCount = None
        self.UnNecessaryNodeList = None
        self.RouterCount = None
        self.SoftDeployInfo = None
        self.ServiceNodeInfo = None
        self.DisasterRecoverGroupIds = None
        self.Tags = None


    def _deserialize(self, params):
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.InstanceId = params.get("InstanceId")
        self.PayMode = params.get("PayMode")
        self.ClientToken = params.get("ClientToken")
        if params.get("PreExecutedFileSettings") is not None:
            self.PreExecutedFileSettings = []
            for item in params.get("PreExecutedFileSettings"):
                obj = PreExecuteFileSettings()
                obj._deserialize(item)
                self.PreExecutedFileSettings.append(obj)
        self.TaskCount = params.get("TaskCount")
        self.CoreCount = params.get("CoreCount")
        self.UnNecessaryNodeList = params.get("UnNecessaryNodeList")
        self.RouterCount = params.get("RouterCount")
        self.SoftDeployInfo = params.get("SoftDeployInfo")
        self.ServiceNodeInfo = params.get("ServiceNodeInfo")
        self.DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class ScaleOutInstanceResponse(AbstractModel):
    """ScaleOutInstance返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID。
        :type InstanceId: str
        :param DealNames: 訂單号。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DealNames: list of str
        :param ClientToken: 用戶端Token。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClientToken: str
        :param FlowId: 擴容流程ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FlowId: int
        :param BillId: 大訂單号。
注意：此欄位可能返回 null，表示取不到有效值。
        :type BillId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.DealNames = None
        self.ClientToken = None
        self.FlowId = None
        self.BillId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DealNames = params.get("DealNames")
        self.ClientToken = params.get("ClientToken")
        self.FlowId = params.get("FlowId")
        self.BillId = params.get("BillId")
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """标簽

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


class TerminateInstanceRequest(AbstractModel):
    """TerminateInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID。
        :type InstanceId: str
        :param ResourceIds: 銷毀節點ID。該參數爲預留參數，用戶無需配置。
        :type ResourceIds: list of str
        """
        self.InstanceId = None
        self.ResourceIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ResourceIds = params.get("ResourceIds")


class TerminateInstanceResponse(AbstractModel):
    """TerminateInstance返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TerminateTasksRequest(AbstractModel):
    """TerminateTasks請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID。
        :type InstanceId: str
        :param ResourceIds: 待銷毀節點的資源ID清單。資源ID形如：emr-vm-xxxxxxxx。有效的資源ID可通過登入[控制台](https://console.cloud.taifucloud.com/emr/static/hardware)查詢。
        :type ResourceIds: list of str
        """
        self.InstanceId = None
        self.ResourceIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ResourceIds = params.get("ResourceIds")


class TerminateTasksResponse(AbstractModel):
    """TerminateTasks返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateInstanceSettings(AbstractModel):
    """變配資源規格

    """

    def __init__(self):
        """
        :param Memory: 内存容量，單位爲G
        :type Memory: int
        :param CPUCores: CPU核數
        :type CPUCores: int
        :param ResourceId: 機器資源ID（EMR測資源标識）
        :type ResourceId: str
        :param InstanceType: 變配機器規格
        :type InstanceType: str
        """
        self.Memory = None
        self.CPUCores = None
        self.ResourceId = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.Memory = params.get("Memory")
        self.CPUCores = params.get("CPUCores")
        self.ResourceId = params.get("ResourceId")
        self.InstanceType = params.get("InstanceType")


class VPCSettings(AbstractModel):
    """VPC 參數

    """

    def __init__(self):
        """
        :param VpcId: VPC ID
        :type VpcId: str
        :param SubnetId: Subnet ID
        :type SubnetId: str
        """
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")