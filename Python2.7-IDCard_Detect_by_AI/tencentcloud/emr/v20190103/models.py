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
        :param LogOnCosPath: 日志儲存在COS上的路徑
        :type LogOnCosPath: str
        :param CosSecretId: COS SecretId
        :type CosSecretId: str
        :param CosSecretKey: COS SecrectKey
        :type CosSecretKey: str
        """
        self.LogOnCosPath = None
        self.CosSecretId = None
        self.CosSecretKey = None


    def _deserialize(self, params):
        self.LogOnCosPath = params.get("LogOnCosPath")
        self.CosSecretId = params.get("CosSecretId")
        self.CosSecretKey = params.get("CosSecretKey")


class ClusterInfoResult(AbstractModel):
    """查詢結果

    """

    def __init__(self):
        """
        :param TotalCnt: 數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCnt: int
        :param ClusterList: 集群訊息清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterList: list of ClusterInstanceInfo
        """
        self.TotalCnt = None
        self.ClusterList = None


    def _deserialize(self, params):
        self.TotalCnt = params.get("TotalCnt")
        if params.get("ClusterList") is not None:
            self.ClusterList = []
            for item in params.get("ClusterList"):
                obj = ClusterInstanceInfo()
                obj._deserialize(item)
                self.ClusterList.append(obj)


class ClusterInstanceInfo(AbstractModel):
    """實例訊息

    """

    def __init__(self):
        """
        :param ClusterId: clusterId
        :type ClusterId: str
        :param StatusDesc: 狀态描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type StatusDesc: str
        :param ClusterName: 集群名字
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param ZoneId: 集群地域
        :type ZoneId: int
        :param AppId: 用戶APPID
        :type AppId: int
        :param Addtime: 創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type Addtime: str
        :param Runtime: 運作時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type Runtime: str
        :param Config: 集群配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type Config: :class:`taifucloudcloud.emr.v20190103.models.EMRProductConfigSettings`
        :param MasterIp: 集群IP
        :type MasterIp: str
        :param EmrVersion: 集群版本
        :type EmrVersion: str
        :param ChargeType: 集群計費類型
        :type ChargeType: int
        """
        self.ClusterId = None
        self.StatusDesc = None
        self.ClusterName = None
        self.ZoneId = None
        self.AppId = None
        self.Addtime = None
        self.Runtime = None
        self.Config = None
        self.MasterIp = None
        self.EmrVersion = None
        self.ChargeType = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.StatusDesc = params.get("StatusDesc")
        self.ClusterName = params.get("ClusterName")
        self.ZoneId = params.get("ZoneId")
        self.AppId = params.get("AppId")
        self.Addtime = params.get("Addtime")
        self.Runtime = params.get("Runtime")
        if params.get("Config") is not None:
            self.Config = EMRProductConfigSettings()
            self.Config._deserialize(params.get("Config"))
        self.MasterIp = params.get("MasterIp")
        self.EmrVersion = params.get("EmrVersion")
        self.ChargeType = params.get("ChargeType")


class CreateInstanceRequest(AbstractModel):
    """CreateInstance請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: int
        :param VPCSettings: VPC設置參數
        :type VPCSettings: :class:`taifucloudcloud.emr.v20190103.models.VPCSettings`
        :param Software: 軟體清單
        :type Software: list of str
        :param ResourceSpec: 資源描述
        :type ResourceSpec: :class:`taifucloudcloud.emr.v20190103.models.ResourceSpec`
        :param SupportHA: 支援HA
        :type SupportHA: int
        :param InstanceName: 實例名稱
        :type InstanceName: str
        :param PayMode: 計費類型
        :type PayMode: int
        :param Placement: 集群位置訊息
        :type Placement: :class:`taifucloudcloud.emr.v20190103.models.Placement`
        :param TimeSpan: 時間長度
        :type TimeSpan: int
        :param TimeUnit: 時間單位
        :type TimeUnit: str
        :param LoginSettings: 登入配置
        :type LoginSettings: :class:`taifucloudcloud.emr.v20190103.models.LoginSettings`
        :param ClientToken: 用戶端Token
        :type ClientToken: str
        :param COSSettings: COS設置參數
        :type COSSettings: :class:`taifucloudcloud.emr.v20190103.models.COSSettings`
        :param SgId: 安全組ID
        :type SgId: str
        :param PreExecutedFileSettings: 預執行腳本設置
        :type PreExecutedFileSettings: :class:`taifucloudcloud.emr.v20190103.models.PreExecuteFileSettings`
        :param AutoRenew: 自動續約
        :type AutoRenew: int
        :param NeedMasterWan: 是否需要外網Ip。支援填NEED_MASTER_WAN，不支援使用NOT_NEED_MASTER_WAN，預設使用NEED_MASTER_WAN
        :type NeedMasterWan: str
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
        self.ClientToken = None
        self.COSSettings = None
        self.SgId = None
        self.PreExecutedFileSettings = None
        self.AutoRenew = None
        self.NeedMasterWan = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        if params.get("VPCSettings") is not None:
            self.VPCSettings = VPCSettings()
            self.VPCSettings._deserialize(params.get("VPCSettings"))
        self.Software = params.get("Software")
        if params.get("ResourceSpec") is not None:
            self.ResourceSpec = ResourceSpec()
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
        self.ClientToken = params.get("ClientToken")
        if params.get("COSSettings") is not None:
            self.COSSettings = COSSettings()
            self.COSSettings._deserialize(params.get("COSSettings"))
        self.SgId = params.get("SgId")
        if params.get("PreExecutedFileSettings") is not None:
            self.PreExecutedFileSettings = PreExecuteFileSettings()
            self.PreExecutedFileSettings._deserialize(params.get("PreExecutedFileSettings"))
        self.AutoRenew = params.get("AutoRenew")
        self.NeedMasterWan = params.get("NeedMasterWan")


class CreateInstanceResponse(AbstractModel):
    """CreateInstance返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 創建實例結果訊息
        :type Result: :class:`taifucloudcloud.emr.v20190103.models.CreateInstanceResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateInstanceResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateInstanceResult(AbstractModel):
    """創建介面返回值

    """

    def __init__(self):
        """
        :param ClientToken: 用戶端TOKEN
        :type ClientToken: str
        :param InstanceName: 集群名稱
        :type InstanceName: str
        :param DealNames: 訂單清單
        :type DealNames: list of str
        """
        self.ClientToken = None
        self.InstanceName = None
        self.DealNames = None


    def _deserialize(self, params):
        self.ClientToken = params.get("ClientToken")
        self.InstanceName = params.get("InstanceName")
        self.DealNames = params.get("DealNames")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 查詢清單,  如果不填寫，返回該AppId下所有實例清單
        :type InstanceIds: list of str
        :param Offset: 查詢偏移量，預設0
        :type Offset: int
        :param Limit: 查詢結果限制，預設值10
        :type Limit: int
        """
        self.InstanceIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 實例數量
        :type Result: :class:`taifucloudcloud.emr.v20190103.models.ClusterInfoResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ClusterInfoResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class EMRProductConfigSettings(AbstractModel):
    """集群的config訊息

    """

    def __init__(self):
        """
        :param SoftInfo: 集群軟體訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type SoftInfo: list of str
        :param MasterNodeSize: master節點數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type MasterNodeSize: int
        :param CoreNodeSize: core節點數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type CoreNodeSize: int
        :param TaskNodeSize: task節點數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type TaskNodeSize: int
        :param ComNodeSize: common節點數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type ComNodeSize: int
        :param MasterResourceSpec: master規格
注意：此欄位可能返回 null，表示取不到有效值。
        :type MasterResourceSpec: :class:`taifucloudcloud.emr.v20190103.models.NodeSpec`
        :param CoreResourceSpec: core規格
注意：此欄位可能返回 null，表示取不到有效值。
        :type CoreResourceSpec: :class:`taifucloudcloud.emr.v20190103.models.NodeSpec`
        :param TaskResourceSpec: task規格
注意：此欄位可能返回 null，表示取不到有效值。
        :type TaskResourceSpec: :class:`taifucloudcloud.emr.v20190103.models.NodeSpec`
        :param CommonResourceSpec: common規格
注意：此欄位可能返回 null，表示取不到有效值。
        :type CommonResourceSpec: :class:`taifucloudcloud.emr.v20190103.models.NodeSpec`
        :param Oncos: 是否使用COS
注意：此欄位可能返回 null，表示取不到有效值。
        :type Oncos: bool
        :param COSSettings: COS配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type COSSettings: :class:`taifucloudcloud.emr.v20190103.models.COSSettings`
        """
        self.SoftInfo = None
        self.MasterNodeSize = None
        self.CoreNodeSize = None
        self.TaskNodeSize = None
        self.ComNodeSize = None
        self.MasterResourceSpec = None
        self.CoreResourceSpec = None
        self.TaskResourceSpec = None
        self.CommonResourceSpec = None
        self.Oncos = None
        self.COSSettings = None


    def _deserialize(self, params):
        self.SoftInfo = params.get("SoftInfo")
        self.MasterNodeSize = params.get("MasterNodeSize")
        self.CoreNodeSize = params.get("CoreNodeSize")
        self.TaskNodeSize = params.get("TaskNodeSize")
        self.ComNodeSize = params.get("ComNodeSize")
        if params.get("MasterResourceSpec") is not None:
            self.MasterResourceSpec = NodeSpec()
            self.MasterResourceSpec._deserialize(params.get("MasterResourceSpec"))
        if params.get("CoreResourceSpec") is not None:
            self.CoreResourceSpec = NodeSpec()
            self.CoreResourceSpec._deserialize(params.get("CoreResourceSpec"))
        if params.get("TaskResourceSpec") is not None:
            self.TaskResourceSpec = NodeSpec()
            self.TaskResourceSpec._deserialize(params.get("TaskResourceSpec"))
        if params.get("CommonResourceSpec") is not None:
            self.CommonResourceSpec = NodeSpec()
            self.CommonResourceSpec._deserialize(params.get("CommonResourceSpec"))
        self.Oncos = params.get("Oncos")
        if params.get("COSSettings") is not None:
            self.COSSettings = COSSettings()
            self.COSSettings._deserialize(params.get("COSSettings"))


class InquiryPriceCreateInstanceRequest(AbstractModel):
    """InquiryPriceCreateInstance請求參數結構體

    """

    def __init__(self):
        """
        :param TimeUnit: 時間單位
        :type TimeUnit: str
        :param TimeSpan: 時間長度
        :type TimeSpan: int
        :param ResourceSpec: 詢價資源描述
        :type ResourceSpec: :class:`taifucloudcloud.emr.v20190103.models.ResourceSpec`
        :param Currency: 貨币種類
        :type Currency: str
        :param PayMode: 計費類型
        :type PayMode: int
        :param SupportHA: 是否支援HA， 1 支援，0 不支援
        :type SupportHA: int
        :param Software: 軟體清單
        :type Software: list of str
        :param Placement: 位置訊息
        :type Placement: :class:`taifucloudcloud.emr.v20190103.models.Placement`
        :param VPCSettings: VPC訊息
        :type VPCSettings: :class:`taifucloudcloud.emr.v20190103.models.VPCSettings`
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


    def _deserialize(self, params):
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        if params.get("ResourceSpec") is not None:
            self.ResourceSpec = ResourceSpec()
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


class InquiryPriceCreateInstanceResponse(AbstractModel):
    """InquiryPriceCreateInstance返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 詢價結果
        :type Result: :class:`taifucloudcloud.emr.v20190103.models.InquiryPriceResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = InquiryPriceResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class InquiryPriceResult(AbstractModel):
    """用于詢價輸出

    """

    def __init__(self):
        """
        :param OriginalCost: 原始價格
        :type OriginalCost: float
        :param DiscountCost: 折扣後價格
        :type DiscountCost: float
        :param TimeUnit: 時間單位
        :type TimeUnit: str
        :param TimeSpan: 時間長度
        :type TimeSpan: int
        """
        self.OriginalCost = None
        self.DiscountCost = None
        self.TimeUnit = None
        self.TimeSpan = None


    def _deserialize(self, params):
        self.OriginalCost = params.get("OriginalCost")
        self.DiscountCost = params.get("DiscountCost")
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")


class InquiryPriceScaleOutInstanceRequest(AbstractModel):
    """InquiryPriceScaleOutInstance請求參數結構體

    """

    def __init__(self):
        """
        :param TimeUnit: 時間單位。s:按量用例單位。m:包年包月用例單位
        :type TimeUnit: str
        :param TimeSpan: 時間長度。按量用例長度爲3600。
        :type TimeSpan: int
        :param ZoneId: Zone ID
        :type ZoneId: int
        :param PayMode: 計費類型
        :type PayMode: int
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param CoreCount: 擴容Core節點個數
        :type CoreCount: int
        :param TaskCount: 擴容Task節點個數
        :type TaskCount: int
        :param Currency: 貨币種類
        :type Currency: str
        """
        self.TimeUnit = None
        self.TimeSpan = None
        self.ZoneId = None
        self.PayMode = None
        self.InstanceId = None
        self.CoreCount = None
        self.TaskCount = None
        self.Currency = None


    def _deserialize(self, params):
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.ZoneId = params.get("ZoneId")
        self.PayMode = params.get("PayMode")
        self.InstanceId = params.get("InstanceId")
        self.CoreCount = params.get("CoreCount")
        self.TaskCount = params.get("TaskCount")
        self.Currency = params.get("Currency")


class InquiryPriceScaleOutInstanceResponse(AbstractModel):
    """InquiryPriceScaleOutInstance返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 擴容價格
        :type Result: :class:`taifucloudcloud.emr.v20190103.models.InquiryPriceResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = InquiryPriceResult()
            self.Result._deserialize(params.get("Result"))
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
        """
        self.DiskType = None
        self.Volume = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.Volume = params.get("Volume")


class NodeSpec(AbstractModel):
    """節點描述

    """

    def __init__(self):
        """
        :param Memory: 内存容量,單位爲M
注意：此欄位可能返回 null，表示取不到有效值。
        :type Memory: int
        :param CPUCores: CPU核數
注意：此欄位可能返回 null，表示取不到有效值。
        :type CPUCores: int
        :param Volume: 數據盤容量
注意：此欄位可能返回 null，表示取不到有效值。
        :type Volume: int
        :param DiskType: 磁盤類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param Spec: 節點規格描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type Spec: str
        :param RootDiskVolume: 系統盤容量
注意：此欄位可能返回 null，表示取不到有效值。
        :type RootDiskVolume: int
        :param StorageType: 儲存類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type StorageType: int
        :param SpecName: 規格名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type SpecName: str
        :param MultiDisks: 多雲盤參數
注意：此欄位可能返回 null，表示取不到有效值。
        :type MultiDisks: list of MultiDisk
        """
        self.Memory = None
        self.CPUCores = None
        self.Volume = None
        self.DiskType = None
        self.Spec = None
        self.RootDiskVolume = None
        self.StorageType = None
        self.SpecName = None
        self.MultiDisks = None


    def _deserialize(self, params):
        self.Memory = params.get("Memory")
        self.CPUCores = params.get("CPUCores")
        self.Volume = params.get("Volume")
        self.DiskType = params.get("DiskType")
        self.Spec = params.get("Spec")
        self.RootDiskVolume = params.get("RootDiskVolume")
        self.StorageType = params.get("StorageType")
        self.SpecName = params.get("SpecName")
        if params.get("MultiDisks") is not None:
            self.MultiDisks = []
            for item in params.get("MultiDisks"):
                obj = MultiDisk()
                obj._deserialize(item)
                self.MultiDisks.append(obj)


class Placement(AbstractModel):
    """描述集實例位置訊息

    """

    def __init__(self):
        """
        :param ProjectId: 實例所屬項目ID。該參數可以通過調用 DescribeProject 的返回值中的 projectId 欄位來獲取。不填爲預設項目。
        :type ProjectId: int
        :param Zone: 實例所屬的可用區ID。該參數也可以通過調用 DescribeZones 的返回值中的Zone欄位來獲取。
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
        :param Path: 腳本在COS上路徑
        :type Path: str
        :param Args: 執行腳本參數
        :type Args: list of str
        :param Bucket: COS的Bucket名稱
        :type Bucket: str
        :param Region: COS的Region名稱
        :type Region: str
        :param Domain: COS的Domain數據
        :type Domain: str
        """
        self.Path = None
        self.Args = None
        self.Bucket = None
        self.Region = None
        self.Domain = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Args = params.get("Args")
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.Domain = params.get("Domain")


class ResourceSpec(AbstractModel):
    """資源描述

    """

    def __init__(self):
        """
        :param CommonCount: Common節點數量
        :type CommonCount: int
        :param MasterResourceSpec: 描述Master節點資源
        :type MasterResourceSpec: :class:`taifucloudcloud.emr.v20190103.models.NodeSpec`
        :param CoreResourceSpec: 描述Core節點資源
        :type CoreResourceSpec: :class:`taifucloudcloud.emr.v20190103.models.NodeSpec`
        :param TaskResourceSpec: 描述Task節點資源
        :type TaskResourceSpec: :class:`taifucloudcloud.emr.v20190103.models.NodeSpec`
        :param MasterCount: Master節點數量
        :type MasterCount: int
        :param CoreCount: Core節點數量
        :type CoreCount: int
        :param TaskCount: Task節點數量
        :type TaskCount: int
        :param CommonResourceSpec: 描述Common節點資源
        :type CommonResourceSpec: :class:`taifucloudcloud.emr.v20190103.models.NodeSpec`
        """
        self.CommonCount = None
        self.MasterResourceSpec = None
        self.CoreResourceSpec = None
        self.TaskResourceSpec = None
        self.MasterCount = None
        self.CoreCount = None
        self.TaskCount = None
        self.CommonResourceSpec = None


    def _deserialize(self, params):
        self.CommonCount = params.get("CommonCount")
        if params.get("MasterResourceSpec") is not None:
            self.MasterResourceSpec = NodeSpec()
            self.MasterResourceSpec._deserialize(params.get("MasterResourceSpec"))
        if params.get("CoreResourceSpec") is not None:
            self.CoreResourceSpec = NodeSpec()
            self.CoreResourceSpec._deserialize(params.get("CoreResourceSpec"))
        if params.get("TaskResourceSpec") is not None:
            self.TaskResourceSpec = NodeSpec()
            self.TaskResourceSpec._deserialize(params.get("TaskResourceSpec"))
        self.MasterCount = params.get("MasterCount")
        self.CoreCount = params.get("CoreCount")
        self.TaskCount = params.get("TaskCount")
        if params.get("CommonResourceSpec") is not None:
            self.CommonResourceSpec = NodeSpec()
            self.CommonResourceSpec._deserialize(params.get("CommonResourceSpec"))


class ScaleOutInstanceRequest(AbstractModel):
    """ScaleOutInstance請求參數結構體

    """

    def __init__(self):
        """
        :param ClientToken: Token
        :type ClientToken: str
        :param TimeUnit: 時間單位
        :type TimeUnit: str
        :param TimeSpan: 時間長度
        :type TimeSpan: int
        :param InstanceId: 擴容實例ID
        :type InstanceId: str
        :param PayMode: 付費類型
        :type PayMode: int
        :param PreExecutedFileSettings: 預執行腳本設置
        :type PreExecutedFileSettings: :class:`taifucloudcloud.emr.v20190103.models.PreExecuteFileSettings`
        :param TaskCount: 擴容Task節點數量
        :type TaskCount: int
        :param CoreCount: 擴容Core節點數量
        :type CoreCount: int
        """
        self.ClientToken = None
        self.TimeUnit = None
        self.TimeSpan = None
        self.InstanceId = None
        self.PayMode = None
        self.PreExecutedFileSettings = None
        self.TaskCount = None
        self.CoreCount = None


    def _deserialize(self, params):
        self.ClientToken = params.get("ClientToken")
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.InstanceId = params.get("InstanceId")
        self.PayMode = params.get("PayMode")
        if params.get("PreExecutedFileSettings") is not None:
            self.PreExecutedFileSettings = PreExecuteFileSettings()
            self.PreExecutedFileSettings._deserialize(params.get("PreExecutedFileSettings"))
        self.TaskCount = params.get("TaskCount")
        self.CoreCount = params.get("CoreCount")


class ScaleOutInstanceResponse(AbstractModel):
    """ScaleOutInstance返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 擴容結果
        :type Result: :class:`taifucloudcloud.emr.v20190103.models.ScaleOutInstanceResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ScaleOutInstanceResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ScaleOutInstanceResult(AbstractModel):
    """擴容實例結果描述

    """

    def __init__(self):
        """
        :param ClientToken: 用戶端調用時傳入的TOKEN
        :type ClientToken: str
        :param InstanceId: 擴容實例ID
        :type InstanceId: str
        :param DealNames: 訂單名稱
        :type DealNames: list of str
        """
        self.ClientToken = None
        self.InstanceId = None
        self.DealNames = None


    def _deserialize(self, params):
        self.ClientToken = params.get("ClientToken")
        self.InstanceId = params.get("InstanceId")
        self.DealNames = params.get("DealNames")


class TerminateInstanceRequest(AbstractModel):
    """TerminateInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 被銷毀的實例ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class TerminateInstanceResponse(AbstractModel):
    """TerminateInstance返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 退單描述
        :type Result: :class:`taifucloudcloud.emr.v20190103.models.TerminateResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TerminateResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class TerminateResult(AbstractModel):
    """退單請求描述描述

    """

    def __init__(self):
        """
        :param InstanceId: 退單集群ID
        :type InstanceId: str
        :param ResourceIds: 資源資源ID
        :type ResourceIds: list of str
        """
        self.InstanceId = None
        self.ResourceIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ResourceIds = params.get("ResourceIds")


class TerminateTasksRequest(AbstractModel):
    """TerminateTasks請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 銷毀節點所屬實例ID
        :type InstanceId: str
        :param ResourceIds: 銷毀節點ID
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
        :param Result: 退單結果
        :type Result: :class:`taifucloudcloud.emr.v20190103.models.TerminateResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TerminateResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


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