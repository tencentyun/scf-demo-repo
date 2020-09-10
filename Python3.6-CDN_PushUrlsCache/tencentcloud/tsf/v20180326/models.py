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


class AddClusterInstancesRequest(AbstractModel):
    """AddClusterInstances請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceIdList: 雲主機ID清單
        :type InstanceIdList: list of str
        :param OsName: 作業系統名稱
        :type OsName: str
        :param ImageId: 作業系統映像ID
        :type ImageId: str
        :param Password: 重灌系統密碼設置
        :type Password: str
        :param KeyId: 重灌系統，關聯金鑰設置
        :type KeyId: str
        :param SgId: 安全組設置
        :type SgId: str
        :param InstanceImportMode: 雲主機導入方式，虛拟機集群必填，容器集群不填寫此欄位，R：重裝TSF系統映像，M：手動安裝agent
        :type InstanceImportMode: str
        """
        self.ClusterId = None
        self.InstanceIdList = None
        self.OsName = None
        self.ImageId = None
        self.Password = None
        self.KeyId = None
        self.SgId = None
        self.InstanceImportMode = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIdList = params.get("InstanceIdList")
        self.OsName = params.get("OsName")
        self.ImageId = params.get("ImageId")
        self.Password = params.get("Password")
        self.KeyId = params.get("KeyId")
        self.SgId = params.get("SgId")
        self.InstanceImportMode = params.get("InstanceImportMode")


class AddClusterInstancesResponse(AbstractModel):
    """AddClusterInstances返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 添加雲主機的返回清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.AddInstanceResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = AddInstanceResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class AddInstanceResult(AbstractModel):
    """添加實例到集群的結果

    """

    def __init__(self):
        """
        :param FailedInstanceIds: 添加集群失敗的節點清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type FailedInstanceIds: list of str
        :param SuccInstanceIds: 添加集群成功的節點清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type SuccInstanceIds: list of str
        :param TimeoutInstanceIds: 添加集群超時的節點清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type TimeoutInstanceIds: list of str
        """
        self.FailedInstanceIds = None
        self.SuccInstanceIds = None
        self.TimeoutInstanceIds = None


    def _deserialize(self, params):
        self.FailedInstanceIds = params.get("FailedInstanceIds")
        self.SuccInstanceIds = params.get("SuccInstanceIds")
        self.TimeoutInstanceIds = params.get("TimeoutInstanceIds")


class AddInstancesRequest(AbstractModel):
    """AddInstances請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceIdList: 雲主機ID清單
        :type InstanceIdList: list of str
        :param OsName: 作業系統名稱
        :type OsName: str
        :param ImageId: 作業系統映像ID
        :type ImageId: str
        :param Password: 重灌系統密碼設置
        :type Password: str
        :param KeyId: 重灌系統，關聯金鑰設置
        :type KeyId: str
        :param SgId: 安全組設置
        :type SgId: str
        :param InstanceImportMode: 雲主機導入方式，虛拟機集群必填，容器集群不填寫此欄位，R：重裝TSF系統映像，M：手動安裝agent
        :type InstanceImportMode: str
        """
        self.ClusterId = None
        self.InstanceIdList = None
        self.OsName = None
        self.ImageId = None
        self.Password = None
        self.KeyId = None
        self.SgId = None
        self.InstanceImportMode = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIdList = params.get("InstanceIdList")
        self.OsName = params.get("OsName")
        self.ImageId = params.get("ImageId")
        self.Password = params.get("Password")
        self.KeyId = params.get("KeyId")
        self.SgId = params.get("SgId")
        self.InstanceImportMode = params.get("InstanceImportMode")


class AddInstancesResponse(AbstractModel):
    """AddInstances返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 添加雲主機是否成功
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ApplicationAttribute(AbstractModel):
    """應用清單其它欄位

    """

    def __init__(self):
        """
        :param InstanceCount: 總實例個數
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceCount: int
        :param RunInstanceCount: 運作實例個數
注意：此欄位可能返回 null，表示取不到有效值。
        :type RunInstanceCount: int
        :param GroupCount: 應用下佈署組個數
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupCount: int
        """
        self.InstanceCount = None
        self.RunInstanceCount = None
        self.GroupCount = None


    def _deserialize(self, params):
        self.InstanceCount = params.get("InstanceCount")
        self.RunInstanceCount = params.get("RunInstanceCount")
        self.GroupCount = params.get("GroupCount")


class ApplicationForPage(AbstractModel):
    """分頁的應用描述訊息欄位

    """

    def __init__(self):
        """
        :param ApplicationId: 應用ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param ApplicationName: 應用名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param ApplicationDesc: 應用描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationDesc: str
        :param ApplicationType: 應用類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationType: str
        :param MicroserviceType: 微服務類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type MicroserviceType: str
        :param ProgLang: 程式設計語言
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProgLang: str
        :param CreateTime: 創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 更新時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param ApplicationResourceType: 應用資源類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationResourceType: str
        :param ApplicationRuntimeType: 應用runtime類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationRuntimeType: str
        :param ApigatewayServiceId: Apigateway的serviceId
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApigatewayServiceId: str
        """
        self.ApplicationId = None
        self.ApplicationName = None
        self.ApplicationDesc = None
        self.ApplicationType = None
        self.MicroserviceType = None
        self.ProgLang = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ApplicationResourceType = None
        self.ApplicationRuntimeType = None
        self.ApigatewayServiceId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.ApplicationDesc = params.get("ApplicationDesc")
        self.ApplicationType = params.get("ApplicationType")
        self.MicroserviceType = params.get("MicroserviceType")
        self.ProgLang = params.get("ProgLang")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ApplicationResourceType = params.get("ApplicationResourceType")
        self.ApplicationRuntimeType = params.get("ApplicationRuntimeType")
        self.ApigatewayServiceId = params.get("ApigatewayServiceId")


class Cluster(AbstractModel):
    """集群

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param ClusterName: 集群名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param ClusterDesc: 集群描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterDesc: str
        :param ClusterType: 集群類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterType: str
        :param VpcId: 集群所屬私有網絡ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param ClusterStatus: 集群狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterStatus: str
        :param ClusterCIDR: 集群CIDR
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterCIDR: str
        :param ClusterTotalCpu: 集群總CPU，單位: 核
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterTotalCpu: float
        :param ClusterTotalMem: 集群總内存，單位: G
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterTotalMem: float
        :param ClusterUsedCpu: 集群已使用CPU，單位: 核
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterUsedCpu: float
        :param ClusterUsedMem: 集群已使用内存，單位: G
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterUsedMem: float
        :param InstanceCount: 集群機器實例數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceCount: int
        :param RunInstanceCount: 集群可用的機器實例數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type RunInstanceCount: int
        :param NormalInstanceCount: 集群正常狀态的機器實例數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type NormalInstanceCount: int
        :param DeleteFlag: 删除标記：true：可以删除；false：不可删除
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeleteFlag: bool
        :param CreateTime: 創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 更新時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param TsfRegionId: 集群所屬TSF地域ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type TsfRegionId: str
        :param TsfRegionName: 集群所屬TSF地域名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type TsfRegionName: str
        :param TsfZoneId: 集群所屬TSF可用區ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type TsfZoneId: str
        :param TsfZoneName: 集群所屬TSF可用區名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type TsfZoneName: str
        :param DeleteFlagReason: 集群不可删除的原因
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeleteFlagReason: str
        :param ClusterLimitCpu: 集群最大CPU限制，單位：核
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterLimitCpu: float
        :param ClusterLimitMem: 集群最大内存限制，單位：G
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterLimitMem: float
        :param RunServiceInstanceCount: 集群可用的服務實例數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type RunServiceInstanceCount: int
        :param SubnetId: 集群所屬子網ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param OperationInfo: 返回給前端的控制訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type OperationInfo: :class:`tencentcloud.tsf.v20180326.models.OperationInfo`
        """
        self.ClusterId = None
        self.ClusterName = None
        self.ClusterDesc = None
        self.ClusterType = None
        self.VpcId = None
        self.ClusterStatus = None
        self.ClusterCIDR = None
        self.ClusterTotalCpu = None
        self.ClusterTotalMem = None
        self.ClusterUsedCpu = None
        self.ClusterUsedMem = None
        self.InstanceCount = None
        self.RunInstanceCount = None
        self.NormalInstanceCount = None
        self.DeleteFlag = None
        self.CreateTime = None
        self.UpdateTime = None
        self.TsfRegionId = None
        self.TsfRegionName = None
        self.TsfZoneId = None
        self.TsfZoneName = None
        self.DeleteFlagReason = None
        self.ClusterLimitCpu = None
        self.ClusterLimitMem = None
        self.RunServiceInstanceCount = None
        self.SubnetId = None
        self.OperationInfo = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.ClusterDesc = params.get("ClusterDesc")
        self.ClusterType = params.get("ClusterType")
        self.VpcId = params.get("VpcId")
        self.ClusterStatus = params.get("ClusterStatus")
        self.ClusterCIDR = params.get("ClusterCIDR")
        self.ClusterTotalCpu = params.get("ClusterTotalCpu")
        self.ClusterTotalMem = params.get("ClusterTotalMem")
        self.ClusterUsedCpu = params.get("ClusterUsedCpu")
        self.ClusterUsedMem = params.get("ClusterUsedMem")
        self.InstanceCount = params.get("InstanceCount")
        self.RunInstanceCount = params.get("RunInstanceCount")
        self.NormalInstanceCount = params.get("NormalInstanceCount")
        self.DeleteFlag = params.get("DeleteFlag")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.TsfRegionId = params.get("TsfRegionId")
        self.TsfRegionName = params.get("TsfRegionName")
        self.TsfZoneId = params.get("TsfZoneId")
        self.TsfZoneName = params.get("TsfZoneName")
        self.DeleteFlagReason = params.get("DeleteFlagReason")
        self.ClusterLimitCpu = params.get("ClusterLimitCpu")
        self.ClusterLimitMem = params.get("ClusterLimitMem")
        self.RunServiceInstanceCount = params.get("RunServiceInstanceCount")
        self.SubnetId = params.get("SubnetId")
        if params.get("OperationInfo") is not None:
            self.OperationInfo = OperationInfo()
            self.OperationInfo._deserialize(params.get("OperationInfo"))


class Config(AbstractModel):
    """配置項

    """

    def __init__(self):
        """
        :param ConfigId: 配置項ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConfigId: str
        :param ConfigName: 配置項名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConfigName: str
        :param ConfigVersion: 配置項版本
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConfigVersion: str
        :param ConfigVersionDesc: 配置項版本描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConfigVersionDesc: str
        :param ConfigValue: 配置項值
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConfigValue: str
        :param ConfigType: 配置項類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConfigType: str
        :param CreationTime: 創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreationTime: str
        :param ApplicationId: 應用ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param ApplicationName: 應用名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param DeleteFlag: 删除标識，true：可以删除；false：不可删除
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeleteFlag: bool
        :param LastUpdateTime: 最後更新時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type LastUpdateTime: str
        :param ConfigVersionCount: 配置項版本數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConfigVersionCount: int
        """
        self.ConfigId = None
        self.ConfigName = None
        self.ConfigVersion = None
        self.ConfigVersionDesc = None
        self.ConfigValue = None
        self.ConfigType = None
        self.CreationTime = None
        self.ApplicationId = None
        self.ApplicationName = None
        self.DeleteFlag = None
        self.LastUpdateTime = None
        self.ConfigVersionCount = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.ConfigName = params.get("ConfigName")
        self.ConfigVersion = params.get("ConfigVersion")
        self.ConfigVersionDesc = params.get("ConfigVersionDesc")
        self.ConfigValue = params.get("ConfigValue")
        self.ConfigType = params.get("ConfigType")
        self.CreationTime = params.get("CreationTime")
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.DeleteFlag = params.get("DeleteFlag")
        self.LastUpdateTime = params.get("LastUpdateTime")
        self.ConfigVersionCount = params.get("ConfigVersionCount")


class ConfigRelease(AbstractModel):
    """配置項發布訊息

    """

    def __init__(self):
        """
        :param ConfigReleaseId: 配置項發布ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConfigReleaseId: str
        :param ConfigId: 配置項ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConfigId: str
        :param ConfigName: 配置項名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConfigName: str
        :param ConfigVersion: 配置項版本
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConfigVersion: str
        :param ReleaseTime: 發布時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReleaseTime: str
        :param GroupId: 佈署組ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param GroupName: 佈署組名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param NamespaceId: 命名空間ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param NamespaceName: 命名空間名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        :param ClusterId: 集群ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param ClusterName: 集群名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param ReleaseDesc: 發布描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReleaseDesc: str
        """
        self.ConfigReleaseId = None
        self.ConfigId = None
        self.ConfigName = None
        self.ConfigVersion = None
        self.ReleaseTime = None
        self.GroupId = None
        self.GroupName = None
        self.NamespaceId = None
        self.NamespaceName = None
        self.ClusterId = None
        self.ClusterName = None
        self.ReleaseDesc = None


    def _deserialize(self, params):
        self.ConfigReleaseId = params.get("ConfigReleaseId")
        self.ConfigId = params.get("ConfigId")
        self.ConfigName = params.get("ConfigName")
        self.ConfigVersion = params.get("ConfigVersion")
        self.ReleaseTime = params.get("ReleaseTime")
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.ReleaseDesc = params.get("ReleaseDesc")


class ConfigReleaseLog(AbstractModel):
    """配置項發布日志

    """

    def __init__(self):
        """
        :param ConfigReleaseLogId: 配置項發布日志ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConfigReleaseLogId: str
        :param ConfigId: 配置項ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConfigId: str
        :param ConfigName: 配置項名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConfigName: str
        :param ConfigVersion: 配置項版本
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConfigVersion: str
        :param GroupId: 佈署組ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param GroupName: 佈署組名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param NamespaceId: 命名空間ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param NamespaceName: 命名空間名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        :param ClusterId: 集群ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param ClusterName: 集群名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param ReleaseTime: 發布時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReleaseTime: str
        :param ReleaseDesc: 發布描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReleaseDesc: str
        :param ReleaseStatus: 發布狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReleaseStatus: str
        :param LastConfigId: 上次發布的配置項ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type LastConfigId: str
        :param LastConfigName: 上次發布的配置項名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type LastConfigName: str
        :param LastConfigVersion: 上次發布的配置項版本
注意：此欄位可能返回 null，表示取不到有效值。
        :type LastConfigVersion: str
        :param RollbackFlag: 回滾标識
注意：此欄位可能返回 null，表示取不到有效值。
        :type RollbackFlag: bool
        """
        self.ConfigReleaseLogId = None
        self.ConfigId = None
        self.ConfigName = None
        self.ConfigVersion = None
        self.GroupId = None
        self.GroupName = None
        self.NamespaceId = None
        self.NamespaceName = None
        self.ClusterId = None
        self.ClusterName = None
        self.ReleaseTime = None
        self.ReleaseDesc = None
        self.ReleaseStatus = None
        self.LastConfigId = None
        self.LastConfigName = None
        self.LastConfigVersion = None
        self.RollbackFlag = None


    def _deserialize(self, params):
        self.ConfigReleaseLogId = params.get("ConfigReleaseLogId")
        self.ConfigId = params.get("ConfigId")
        self.ConfigName = params.get("ConfigName")
        self.ConfigVersion = params.get("ConfigVersion")
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.ReleaseTime = params.get("ReleaseTime")
        self.ReleaseDesc = params.get("ReleaseDesc")
        self.ReleaseStatus = params.get("ReleaseStatus")
        self.LastConfigId = params.get("LastConfigId")
        self.LastConfigName = params.get("LastConfigName")
        self.LastConfigVersion = params.get("LastConfigVersion")
        self.RollbackFlag = params.get("RollbackFlag")


class ContainGroup(AbstractModel):
    """佈署組清單（應用下鑽界面的）

    """

    def __init__(self):
        """
        :param GroupId: 佈署組ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param GroupName: 分組名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param CreateTime: 創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param Server: 映像server
注意：此欄位可能返回 null，表示取不到有效值。
        :type Server: str
        :param RepoName: 映像名，如/tsf/nginx
注意：此欄位可能返回 null，表示取不到有效值。
        :type RepoName: str
        :param TagName: 映像版本名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagName: str
        :param ClusterId: 集群ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param ClusterName: 集群名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param NamespaceId: 命名空間ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param NamespaceName: 命名空間名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        :param CpuRequest: 初始分配的 CPU 核數，對應 K8S request
注意：此欄位可能返回 null，表示取不到有效值。
        :type CpuRequest: str
        :param CpuLimit: 最大分配的 CPU 核數，對應 K8S limit
注意：此欄位可能返回 null，表示取不到有效值。
        :type CpuLimit: str
        :param MemRequest: 初始分配的内存 MiB 數，對應 K8S request
注意：此欄位可能返回 null，表示取不到有效值。
        :type MemRequest: str
        :param MemLimit: 最大分配的内存 MiB 數，對應 K8S limit
注意：此欄位可能返回 null，表示取不到有效值。
        :type MemLimit: str
        """
        self.GroupId = None
        self.GroupName = None
        self.CreateTime = None
        self.Server = None
        self.RepoName = None
        self.TagName = None
        self.ClusterId = None
        self.ClusterName = None
        self.NamespaceId = None
        self.NamespaceName = None
        self.CpuRequest = None
        self.CpuLimit = None
        self.MemRequest = None
        self.MemLimit = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.CreateTime = params.get("CreateTime")
        self.Server = params.get("Server")
        self.RepoName = params.get("RepoName")
        self.TagName = params.get("TagName")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")
        self.CpuRequest = params.get("CpuRequest")
        self.CpuLimit = params.get("CpuLimit")
        self.MemRequest = params.get("MemRequest")
        self.MemLimit = params.get("MemLimit")


class ContainGroupResult(AbstractModel):
    """佈署組清單（應用下鑽）

    """

    def __init__(self):
        """
        :param Content: 佈署組清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Content: list of ContainGroup
        :param TotalCount: 總記錄數
        :type TotalCount: int
        """
        self.Content = None
        self.TotalCount = None


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = ContainGroup()
                obj._deserialize(item)
                self.Content.append(obj)
        self.TotalCount = params.get("TotalCount")


class ContainerGroupDetail(AbstractModel):
    """容器佈署組詳情

    """

    def __init__(self):
        """
        :param GroupId: 佈署組ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param GroupName: 分組名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param InstanceNum: 實例總數
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceNum: int
        :param CurrentNum: 已啓動實例總數
注意：此欄位可能返回 null，表示取不到有效值。
        :type CurrentNum: int
        :param CreateTime: 創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param Server: 映像server
注意：此欄位可能返回 null，表示取不到有效值。
        :type Server: str
        :param Reponame: 映像名，如/tsf/nginx
注意：此欄位可能返回 null，表示取不到有效值。
        :type Reponame: str
        :param TagName: 映像版本名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagName: str
        :param ClusterId: 集群ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param ClusterName: 集群名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param NamespaceId: 命名空間ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param NamespaceName: 命名空間名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        :param ApplicationId: 應用ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param LbIp: 負載均衡ip
注意：此欄位可能返回 null，表示取不到有效值。
        :type LbIp: str
        :param ApplicationType: 應用類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationType: str
        :param ClusterIp: Service ip
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterIp: str
        :param NodePort: NodePort端口，只有公網和NodePort訪問方式才有值
注意：此欄位可能返回 null，表示取不到有效值。
        :type NodePort: int
        :param CpuLimit: 最大分配的 CPU 核數，對應 K8S limit
注意：此欄位可能返回 null，表示取不到有效值。
        :type CpuLimit: str
        :param MemLimit: 最大分配的内存 MiB 數，對應 K8S limit
注意：此欄位可能返回 null，表示取不到有效值。
        :type MemLimit: str
        :param AccessType: 0:公網 1:集群内訪問 2：NodePort
注意：此欄位可能返回 null，表示取不到有效值。
        :type AccessType: int
        :param UpdateType: 更新方式：0:快速更新 1:滾動更新
注意：此欄位可能返回 null，表示取不到有效值。
        :type UpdateType: int
        :param UpdateIvl: 更新間隔,單位秒
注意：此欄位可能返回 null，表示取不到有效值。
        :type UpdateIvl: int
        :param ProtocolPorts: 端口數組對象
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProtocolPorts: list of ProtocolPort
        :param Envs: 環境變量數組對象
注意：此欄位可能返回 null，表示取不到有效值。
        :type Envs: list of Env
        :param ApplicationName: 應用名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param Message: pod錯誤訊息描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param Status: 佈署組狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: str
        :param MicroserviceType: 服務類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type MicroserviceType: str
        :param CpuRequest: 初始分配的 CPU 核數，對應 K8S request
注意：此欄位可能返回 null，表示取不到有效值。
        :type CpuRequest: str
        :param MemRequest: 初始分配的内存 MiB 數，對應 K8S request
注意：此欄位可能返回 null，表示取不到有效值。
        :type MemRequest: str
        :param SubnetId: 子網id
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param GroupResourceType: 佈署組資源類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupResourceType: str
        :param InstanceCount: 佈署組實例個數
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceCount: int
        :param UpdatedTime: 佈署組更新時間戳
注意：此欄位可能返回 null，表示取不到有效值。
        :type UpdatedTime: int
        """
        self.GroupId = None
        self.GroupName = None
        self.InstanceNum = None
        self.CurrentNum = None
        self.CreateTime = None
        self.Server = None
        self.Reponame = None
        self.TagName = None
        self.ClusterId = None
        self.ClusterName = None
        self.NamespaceId = None
        self.NamespaceName = None
        self.ApplicationId = None
        self.LbIp = None
        self.ApplicationType = None
        self.ClusterIp = None
        self.NodePort = None
        self.CpuLimit = None
        self.MemLimit = None
        self.AccessType = None
        self.UpdateType = None
        self.UpdateIvl = None
        self.ProtocolPorts = None
        self.Envs = None
        self.ApplicationName = None
        self.Message = None
        self.Status = None
        self.MicroserviceType = None
        self.CpuRequest = None
        self.MemRequest = None
        self.SubnetId = None
        self.GroupResourceType = None
        self.InstanceCount = None
        self.UpdatedTime = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.InstanceNum = params.get("InstanceNum")
        self.CurrentNum = params.get("CurrentNum")
        self.CreateTime = params.get("CreateTime")
        self.Server = params.get("Server")
        self.Reponame = params.get("Reponame")
        self.TagName = params.get("TagName")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")
        self.ApplicationId = params.get("ApplicationId")
        self.LbIp = params.get("LbIp")
        self.ApplicationType = params.get("ApplicationType")
        self.ClusterIp = params.get("ClusterIp")
        self.NodePort = params.get("NodePort")
        self.CpuLimit = params.get("CpuLimit")
        self.MemLimit = params.get("MemLimit")
        self.AccessType = params.get("AccessType")
        self.UpdateType = params.get("UpdateType")
        self.UpdateIvl = params.get("UpdateIvl")
        if params.get("ProtocolPorts") is not None:
            self.ProtocolPorts = []
            for item in params.get("ProtocolPorts"):
                obj = ProtocolPort()
                obj._deserialize(item)
                self.ProtocolPorts.append(obj)
        if params.get("Envs") is not None:
            self.Envs = []
            for item in params.get("Envs"):
                obj = Env()
                obj._deserialize(item)
                self.Envs.append(obj)
        self.ApplicationName = params.get("ApplicationName")
        self.Message = params.get("Message")
        self.Status = params.get("Status")
        self.MicroserviceType = params.get("MicroserviceType")
        self.CpuRequest = params.get("CpuRequest")
        self.MemRequest = params.get("MemRequest")
        self.SubnetId = params.get("SubnetId")
        self.GroupResourceType = params.get("GroupResourceType")
        self.InstanceCount = params.get("InstanceCount")
        self.UpdatedTime = params.get("UpdatedTime")


class CosCredentials(AbstractModel):
    """cos臨時帳号訊息

    """

    def __init__(self):
        """
        :param SessionToken: 會話Token
注意：此欄位可能返回 null，表示取不到有效值。
        :type SessionToken: str
        :param TmpAppId: 臨時應用ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type TmpAppId: str
        :param TmpSecretId: 臨時調用者身份ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type TmpSecretId: str
        :param TmpSecretKey: 臨時金鑰
注意：此欄位可能返回 null，表示取不到有效值。
        :type TmpSecretKey: str
        :param ExpiredTime: 過期時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type ExpiredTime: int
        :param Domain: 所在域
注意：此欄位可能返回 null，表示取不到有效值。
        :type Domain: str
        """
        self.SessionToken = None
        self.TmpAppId = None
        self.TmpSecretId = None
        self.TmpSecretKey = None
        self.ExpiredTime = None
        self.Domain = None


    def _deserialize(self, params):
        self.SessionToken = params.get("SessionToken")
        self.TmpAppId = params.get("TmpAppId")
        self.TmpSecretId = params.get("TmpSecretId")
        self.TmpSecretKey = params.get("TmpSecretKey")
        self.ExpiredTime = params.get("ExpiredTime")
        self.Domain = params.get("Domain")


class CosDownloadInfo(AbstractModel):
    """Cos下載所需訊息

    """

    def __init__(self):
        """
        :param Bucket: 桶名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type Bucket: str
        :param Region: 地域
注意：此欄位可能返回 null，表示取不到有效值。
        :type Region: str
        :param Path: 路徑
注意：此欄位可能返回 null，表示取不到有效值。
        :type Path: str
        :param Credentials: 鑒權訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Credentials: :class:`tencentcloud.tsf.v20180326.models.CosCredentials`
        """
        self.Bucket = None
        self.Region = None
        self.Path = None
        self.Credentials = None


    def _deserialize(self, params):
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.Path = params.get("Path")
        if params.get("Credentials") is not None:
            self.Credentials = CosCredentials()
            self.Credentials._deserialize(params.get("Credentials"))


class CosUploadInfo(AbstractModel):
    """cos上傳所需訊息

    """

    def __init__(self):
        """
        :param PkgId: 程式包ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type PkgId: str
        :param Bucket: 桶
注意：此欄位可能返回 null，表示取不到有效值。
        :type Bucket: str
        :param Region: 目标地域
注意：此欄位可能返回 null，表示取不到有效值。
        :type Region: str
        :param Path: 儲存路徑
注意：此欄位可能返回 null，表示取不到有效值。
        :type Path: str
        :param Credentials: 鑒權訊息
        :type Credentials: :class:`tencentcloud.tsf.v20180326.models.CosCredentials`
        """
        self.PkgId = None
        self.Bucket = None
        self.Region = None
        self.Path = None
        self.Credentials = None


    def _deserialize(self, params):
        self.PkgId = params.get("PkgId")
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.Path = params.get("Path")
        if params.get("Credentials") is not None:
            self.Credentials = CosCredentials()
            self.Credentials._deserialize(params.get("Credentials"))


class CreateApplicationRequest(AbstractModel):
    """CreateApplication請求參數結構體

    """

    def __init__(self):
        """
        :param ApplicationName: 應用名稱
        :type ApplicationName: str
        :param ApplicationType: 應用類型，V：虛拟機應用；C：容器應用；S：serverless應用
        :type ApplicationType: str
        :param MicroserviceType: 應用微服務類型，M：service mesh應用；N：普通應用；G：閘道應用
        :type MicroserviceType: str
        :param ApplicationDesc: 應用描述
        :type ApplicationDesc: str
        :param ApplicationLogConfig: 應用日志配置項，廢棄參數
        :type ApplicationLogConfig: str
        :param ApplicationResourceType: 應用資源類型，廢棄參數
        :type ApplicationResourceType: str
        :param ApplicationRuntimeType: 應用runtime類型
        :type ApplicationRuntimeType: str
        """
        self.ApplicationName = None
        self.ApplicationType = None
        self.MicroserviceType = None
        self.ApplicationDesc = None
        self.ApplicationLogConfig = None
        self.ApplicationResourceType = None
        self.ApplicationRuntimeType = None


    def _deserialize(self, params):
        self.ApplicationName = params.get("ApplicationName")
        self.ApplicationType = params.get("ApplicationType")
        self.MicroserviceType = params.get("MicroserviceType")
        self.ApplicationDesc = params.get("ApplicationDesc")
        self.ApplicationLogConfig = params.get("ApplicationLogConfig")
        self.ApplicationResourceType = params.get("ApplicationResourceType")
        self.ApplicationRuntimeType = params.get("ApplicationRuntimeType")


class CreateApplicationResponse(AbstractModel):
    """CreateApplication返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 應用ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateClusterRequest(AbstractModel):
    """CreateCluster請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterName: 集群名稱
        :type ClusterName: str
        :param ClusterType: 集群類型
        :type ClusterType: str
        :param VpcId: 私有網絡ID
        :type VpcId: str
        :param ClusterCIDR: 分配給集群容器和服務IP的CIDR
        :type ClusterCIDR: str
        :param ClusterDesc: 集群備注
        :type ClusterDesc: str
        :param TsfRegionId: 集群所屬TSF地域
        :type TsfRegionId: str
        :param TsfZoneId: 集群所屬TSF可用區
        :type TsfZoneId: str
        :param SubnetId: 私有網絡子網ID
        :type SubnetId: str
        """
        self.ClusterName = None
        self.ClusterType = None
        self.VpcId = None
        self.ClusterCIDR = None
        self.ClusterDesc = None
        self.TsfRegionId = None
        self.TsfZoneId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.ClusterName = params.get("ClusterName")
        self.ClusterType = params.get("ClusterType")
        self.VpcId = params.get("VpcId")
        self.ClusterCIDR = params.get("ClusterCIDR")
        self.ClusterDesc = params.get("ClusterDesc")
        self.TsfRegionId = params.get("TsfRegionId")
        self.TsfZoneId = params.get("TsfZoneId")
        self.SubnetId = params.get("SubnetId")


class CreateClusterResponse(AbstractModel):
    """CreateCluster返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 集群ID
        :type Result: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateConfigRequest(AbstractModel):
    """CreateConfig請求參數結構體

    """

    def __init__(self):
        """
        :param ConfigName: 配置項名稱
        :type ConfigName: str
        :param ConfigVersion: 配置項版本
        :type ConfigVersion: str
        :param ConfigValue: 配置項值
        :type ConfigValue: str
        :param ApplicationId: 應用ID
        :type ApplicationId: str
        :param ConfigVersionDesc: 配置項版本描述
        :type ConfigVersionDesc: str
        :param ConfigType: 配置項值類型
        :type ConfigType: str
        :param EncodeWithBase64: Base64編碼的配置項
        :type EncodeWithBase64: bool
        """
        self.ConfigName = None
        self.ConfigVersion = None
        self.ConfigValue = None
        self.ApplicationId = None
        self.ConfigVersionDesc = None
        self.ConfigType = None
        self.EncodeWithBase64 = None


    def _deserialize(self, params):
        self.ConfigName = params.get("ConfigName")
        self.ConfigVersion = params.get("ConfigVersion")
        self.ConfigValue = params.get("ConfigValue")
        self.ApplicationId = params.get("ApplicationId")
        self.ConfigVersionDesc = params.get("ConfigVersionDesc")
        self.ConfigType = params.get("ConfigType")
        self.EncodeWithBase64 = params.get("EncodeWithBase64")


class CreateConfigResponse(AbstractModel):
    """CreateConfig返回參數結構體

    """

    def __init__(self):
        """
        :param Result: true：創建成功；false：創建失敗
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateContainGroupRequest(AbstractModel):
    """CreateContainGroup請求參數結構體

    """

    def __init__(self):
        """
        :param ApplicationId: 分組所屬應用ID
        :type ApplicationId: str
        :param NamespaceId: 分組所屬命名空間ID
        :type NamespaceId: str
        :param GroupName: 分組名稱欄位，長度1~60，字母或下劃線開頭，可包含字母數字下劃線
        :type GroupName: str
        :param InstanceNum: 實例數量
        :type InstanceNum: int
        :param AccessType: 0:公網 1:集群内訪問 2：NodePort
        :type AccessType: int
        :param ProtocolPorts: 數組對象，見下方定義
        :type ProtocolPorts: list of ProtocolPort
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param CpuLimit: 最大分配 CPU 核數，對應 K8S limit
        :type CpuLimit: str
        :param MemLimit: 最大分配内存 MiB 數，對應 K8S limit
        :type MemLimit: str
        :param GroupComment: 分組備注欄位，長度應不大于200字元
        :type GroupComment: str
        :param UpdateType: 更新方式：0:快速更新 1:滾動更新
        :type UpdateType: int
        :param UpdateIvl: 滾動更新必填，更新間隔
        :type UpdateIvl: int
        :param CpuRequest: 初始分配的 CPU 核數，對應 K8S request
        :type CpuRequest: str
        :param MemRequest: 初始分配的内存 MiB 數，對應 K8S request
        :type MemRequest: str
        :param GroupResourceType: 佈署組資源類型
        :type GroupResourceType: str
        :param SubnetId: 子網ID
        :type SubnetId: str
        :param AgentCpuRequest: agent 容器分配的 CPU 核數，對應 K8S 的 request
        :type AgentCpuRequest: str
        :param AgentCpuLimit: agent 容器最大的 CPU 核數，對應 K8S 的 limit
        :type AgentCpuLimit: str
        :param AgentMemRequest: agent 容器分配的内存 MiB 數，對應 K8S 的 request
        :type AgentMemRequest: str
        :param AgentMemLimit: agent 容器最大的内存 MiB 數，對應 K8S 的 limit
        :type AgentMemLimit: str
        :param IstioCpuRequest: istioproxy 容器分配的 CPU 核數，對應 K8S 的 request
        :type IstioCpuRequest: str
        :param IstioCpuLimit: istioproxy 容器最大的 CPU 核數，對應 K8S 的 limit
        :type IstioCpuLimit: str
        :param IstioMemRequest: istioproxy 容器分配的内存 MiB 數，對應 K8S 的 request
        :type IstioMemRequest: str
        :param IstioMemLimit: istioproxy 容器最大的内存 MiB 數，對應 K8S 的 limit
        :type IstioMemLimit: str
        """
        self.ApplicationId = None
        self.NamespaceId = None
        self.GroupName = None
        self.InstanceNum = None
        self.AccessType = None
        self.ProtocolPorts = None
        self.ClusterId = None
        self.CpuLimit = None
        self.MemLimit = None
        self.GroupComment = None
        self.UpdateType = None
        self.UpdateIvl = None
        self.CpuRequest = None
        self.MemRequest = None
        self.GroupResourceType = None
        self.SubnetId = None
        self.AgentCpuRequest = None
        self.AgentCpuLimit = None
        self.AgentMemRequest = None
        self.AgentMemLimit = None
        self.IstioCpuRequest = None
        self.IstioCpuLimit = None
        self.IstioMemRequest = None
        self.IstioMemLimit = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.NamespaceId = params.get("NamespaceId")
        self.GroupName = params.get("GroupName")
        self.InstanceNum = params.get("InstanceNum")
        self.AccessType = params.get("AccessType")
        if params.get("ProtocolPorts") is not None:
            self.ProtocolPorts = []
            for item in params.get("ProtocolPorts"):
                obj = ProtocolPort()
                obj._deserialize(item)
                self.ProtocolPorts.append(obj)
        self.ClusterId = params.get("ClusterId")
        self.CpuLimit = params.get("CpuLimit")
        self.MemLimit = params.get("MemLimit")
        self.GroupComment = params.get("GroupComment")
        self.UpdateType = params.get("UpdateType")
        self.UpdateIvl = params.get("UpdateIvl")
        self.CpuRequest = params.get("CpuRequest")
        self.MemRequest = params.get("MemRequest")
        self.GroupResourceType = params.get("GroupResourceType")
        self.SubnetId = params.get("SubnetId")
        self.AgentCpuRequest = params.get("AgentCpuRequest")
        self.AgentCpuLimit = params.get("AgentCpuLimit")
        self.AgentMemRequest = params.get("AgentMemRequest")
        self.AgentMemLimit = params.get("AgentMemLimit")
        self.IstioCpuRequest = params.get("IstioCpuRequest")
        self.IstioCpuLimit = params.get("IstioCpuLimit")
        self.IstioMemRequest = params.get("IstioMemRequest")
        self.IstioMemLimit = params.get("IstioMemLimit")


class CreateContainGroupResponse(AbstractModel):
    """CreateContainGroup返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 返回創建成功的佈署組ID，返回null表示失敗
        :type Result: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateGroupRequest(AbstractModel):
    """CreateGroup請求參數結構體

    """

    def __init__(self):
        """
        :param ApplicationId: 佈署組所屬的應用ID
        :type ApplicationId: str
        :param NamespaceId: 佈署組所屬命名空間ID
        :type NamespaceId: str
        :param GroupName: 佈署組名稱
        :type GroupName: str
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param GroupDesc: 佈署組描述
        :type GroupDesc: str
        :param GroupResourceType: 佈署組資源類型
        :type GroupResourceType: str
        """
        self.ApplicationId = None
        self.NamespaceId = None
        self.GroupName = None
        self.ClusterId = None
        self.GroupDesc = None
        self.GroupResourceType = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.NamespaceId = params.get("NamespaceId")
        self.GroupName = params.get("GroupName")
        self.ClusterId = params.get("ClusterId")
        self.GroupDesc = params.get("GroupDesc")
        self.GroupResourceType = params.get("GroupResourceType")


class CreateGroupResponse(AbstractModel):
    """CreateGroup返回參數結構體

    """

    def __init__(self):
        """
        :param Result: groupId， null表示創建失敗
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateMicroserviceRequest(AbstractModel):
    """CreateMicroservice請求參數結構體

    """

    def __init__(self):
        """
        :param NamespaceId: 命名空間ID
        :type NamespaceId: str
        :param MicroserviceName: 微服務名稱
        :type MicroserviceName: str
        :param MicroserviceDesc: 微服務描述訊息
        :type MicroserviceDesc: str
        """
        self.NamespaceId = None
        self.MicroserviceName = None
        self.MicroserviceDesc = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.MicroserviceName = params.get("MicroserviceName")
        self.MicroserviceDesc = params.get("MicroserviceDesc")


class CreateMicroserviceResponse(AbstractModel):
    """CreateMicroservice返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 新增微服務是否成功。
true：操作成功。
false：操作失敗。
        :type Result: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateNamespaceRequest(AbstractModel):
    """CreateNamespace請求參數結構體

    """

    def __init__(self):
        """
        :param NamespaceName: 命名空間名稱
        :type NamespaceName: str
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param NamespaceDesc: 命名空間描述
        :type NamespaceDesc: str
        :param NamespaceResourceType: 命名空間資源類型(預設值爲DEF)
        :type NamespaceResourceType: str
        :param NamespaceType: 是否是全局命名空間(預設是DEF，表示普通命名空間；GLOBAL表示全局命名空間)
        :type NamespaceType: str
        :param NamespaceId: 命名空間ID
        :type NamespaceId: str
        """
        self.NamespaceName = None
        self.ClusterId = None
        self.NamespaceDesc = None
        self.NamespaceResourceType = None
        self.NamespaceType = None
        self.NamespaceId = None


    def _deserialize(self, params):
        self.NamespaceName = params.get("NamespaceName")
        self.ClusterId = params.get("ClusterId")
        self.NamespaceDesc = params.get("NamespaceDesc")
        self.NamespaceResourceType = params.get("NamespaceResourceType")
        self.NamespaceType = params.get("NamespaceType")
        self.NamespaceId = params.get("NamespaceId")


class CreateNamespaceResponse(AbstractModel):
    """CreateNamespace返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 成功時爲命名空間ID，失敗爲null
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreatePublicConfigRequest(AbstractModel):
    """CreatePublicConfig請求參數結構體

    """

    def __init__(self):
        """
        :param ConfigName: 配置項名稱
        :type ConfigName: str
        :param ConfigVersion: 配置項版本
        :type ConfigVersion: str
        :param ConfigValue: 配置項值，總是接收yaml格式的内容
        :type ConfigValue: str
        :param ConfigVersionDesc: 配置項版本描述
        :type ConfigVersionDesc: str
        :param ConfigType: 配置項類型
        :type ConfigType: str
        :param EncodeWithBase64: Base64編碼的配置項
        :type EncodeWithBase64: bool
        """
        self.ConfigName = None
        self.ConfigVersion = None
        self.ConfigValue = None
        self.ConfigVersionDesc = None
        self.ConfigType = None
        self.EncodeWithBase64 = None


    def _deserialize(self, params):
        self.ConfigName = params.get("ConfigName")
        self.ConfigVersion = params.get("ConfigVersion")
        self.ConfigValue = params.get("ConfigValue")
        self.ConfigVersionDesc = params.get("ConfigVersionDesc")
        self.ConfigType = params.get("ConfigType")
        self.EncodeWithBase64 = params.get("EncodeWithBase64")


class CreatePublicConfigResponse(AbstractModel):
    """CreatePublicConfig返回參數結構體

    """

    def __init__(self):
        """
        :param Result: true：創建成功；false：創建失敗
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateServerlessGroupRequest(AbstractModel):
    """CreateServerlessGroup請求參數結構體

    """

    def __init__(self):
        """
        :param ApplicationId: 分組所屬應用ID
        :type ApplicationId: str
        :param GroupName: 分組名稱欄位，長度1~60，字母或下劃線開頭，可包含字母數字下劃線
        :type GroupName: str
        :param NamespaceId: 分組所屬名字空間ID
        :type NamespaceId: str
        :param ClusterId: 分組所屬集群ID
        :type ClusterId: str
        """
        self.ApplicationId = None
        self.GroupName = None
        self.NamespaceId = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.GroupName = params.get("GroupName")
        self.NamespaceId = params.get("NamespaceId")
        self.ClusterId = params.get("ClusterId")


class CreateServerlessGroupResponse(AbstractModel):
    """CreateServerlessGroup返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 創建成功的佈署組ID，返回null表示失敗
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteApplicationRequest(AbstractModel):
    """DeleteApplication請求參數結構體

    """

    def __init__(self):
        """
        :param ApplicationId: 應用ID
        :type ApplicationId: str
        """
        self.ApplicationId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")


class DeleteApplicationResponse(AbstractModel):
    """DeleteApplication返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 删除應用操作是否成功。
true：操作成功。
false：操作失敗。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteConfigRequest(AbstractModel):
    """DeleteConfig請求參數結構體

    """

    def __init__(self):
        """
        :param ConfigId: 配置項ID
        :type ConfigId: str
        """
        self.ConfigId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")


class DeleteConfigResponse(AbstractModel):
    """DeleteConfig返回參數結構體

    """

    def __init__(self):
        """
        :param Result: true：删除成功；false：删除失敗
        :type Result: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteContainerGroupRequest(AbstractModel):
    """DeleteContainerGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 佈署組ID，分組唯一标識
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DeleteContainerGroupResponse(AbstractModel):
    """DeleteContainerGroup返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 删除操作是否成功：
true：成功
false：失敗
        :type Result: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteGroupRequest(AbstractModel):
    """DeleteGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 佈署組ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DeleteGroupResponse(AbstractModel):
    """DeleteGroup返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 删除佈署組操作是否成功。
true：操作成功。
false：操作失敗。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteImageTag(AbstractModel):
    """需要删除的映像版本

    """

    def __init__(self):
        """
        :param RepoName: 倉庫名，如/tsf/nginx
        :type RepoName: str
        :param TagName: 版本号:如V1
        :type TagName: str
        """
        self.RepoName = None
        self.TagName = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.TagName = params.get("TagName")


class DeleteImageTagsRequest(AbstractModel):
    """DeleteImageTags請求參數結構體

    """

    def __init__(self):
        """
        :param ImageTags: 映像版本數組
        :type ImageTags: list of DeleteImageTag
        """
        self.ImageTags = None


    def _deserialize(self, params):
        if params.get("ImageTags") is not None:
            self.ImageTags = []
            for item in params.get("ImageTags"):
                obj = DeleteImageTag()
                obj._deserialize(item)
                self.ImageTags.append(obj)


class DeleteImageTagsResponse(AbstractModel):
    """DeleteImageTags返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 批次删除操作是否成功。
true：成功。
false：失敗。
        :type Result: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteMicroserviceRequest(AbstractModel):
    """DeleteMicroservice請求參數結構體

    """

    def __init__(self):
        """
        :param MicroserviceId: 微服務ID
        :type MicroserviceId: str
        """
        self.MicroserviceId = None


    def _deserialize(self, params):
        self.MicroserviceId = params.get("MicroserviceId")


class DeleteMicroserviceResponse(AbstractModel):
    """DeleteMicroservice返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 删除微服務是否成功。
true：操作成功。
false：操作失敗。
        :type Result: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteNamespaceRequest(AbstractModel):
    """DeleteNamespace請求參數結構體

    """

    def __init__(self):
        """
        :param NamespaceId: 命名空間ID
        :type NamespaceId: str
        :param ClusterId: 集群ID
        :type ClusterId: str
        """
        self.NamespaceId = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.ClusterId = params.get("ClusterId")


class DeleteNamespaceResponse(AbstractModel):
    """DeleteNamespace返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 删除命名空間是否成功。
true：删除成功。
false：删除失敗。
        :type Result: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeletePkgsRequest(AbstractModel):
    """DeletePkgs請求參數結構體

    """

    def __init__(self):
        """
        :param ApplicationId: 應用ID
        :type ApplicationId: str
        :param PkgIds: 需要删除的程式包ID清單
        :type PkgIds: list of str
        """
        self.ApplicationId = None
        self.PkgIds = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.PkgIds = params.get("PkgIds")


class DeletePkgsResponse(AbstractModel):
    """DeletePkgs返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePublicConfigRequest(AbstractModel):
    """DeletePublicConfig請求參數結構體

    """

    def __init__(self):
        """
        :param ConfigId: 配置項ID
        :type ConfigId: str
        """
        self.ConfigId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")


class DeletePublicConfigResponse(AbstractModel):
    """DeletePublicConfig返回參數結構體

    """

    def __init__(self):
        """
        :param Result: true：删除成功；false：删除失敗
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteServerlessGroupRequest(AbstractModel):
    """DeleteServerlessGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: groupId，分組唯一标識
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DeleteServerlessGroupResponse(AbstractModel):
    """DeleteServerlessGroup返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 結果true：成功；false：失敗。
        :type Result: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeployContainerGroupRequest(AbstractModel):
    """DeployContainerGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 佈署組ID，分組唯一标識
        :type GroupId: str
        :param Server: 映像server
        :type Server: str
        :param TagName: 映像版本名稱,如v1
        :type TagName: str
        :param InstanceNum: 實例數量
        :type InstanceNum: int
        :param Reponame: 舊版映像名，如/tsf/nginx
        :type Reponame: str
        :param CpuLimit: 業務容器最大的 CPU 核數，對應 K8S 的 limit；不填時預設爲 request 的 2 倍
        :type CpuLimit: str
        :param MemLimit: 業務容器最大的内存 MiB 數，對應 K8S 的 limit；不填時預設爲 request 的 2 倍
        :type MemLimit: str
        :param JvmOpts: jvm參數
        :type JvmOpts: str
        :param CpuRequest: 業務容器分配的 CPU 核數，對應 K8S 的 request
        :type CpuRequest: str
        :param MemRequest: 業務容器分配的内存 MiB 數，對應 K8S 的 request
        :type MemRequest: str
        :param DoNotStart: 是否不立即啓動
        :type DoNotStart: bool
        :param RepoName: （優先使用）新版映像名，如/tsf/nginx
        :type RepoName: str
        :param UpdateType: 更新方式：0:快速更新 1:滾動更新
        :type UpdateType: int
        :param UpdateIvl: 滾動更新必填，更新間隔
        :type UpdateIvl: int
        :param AgentCpuRequest: agent 容器分配的 CPU 核數，對應 K8S 的 request
        :type AgentCpuRequest: str
        :param AgentCpuLimit: agent 容器最大的 CPU 核數，對應 K8S 的 limit
        :type AgentCpuLimit: str
        :param AgentMemRequest: agent 容器分配的内存 MiB 數，對應 K8S 的 request
        :type AgentMemRequest: str
        :param AgentMemLimit: agent 容器最大的内存 MiB 數，對應 K8S 的 limit
        :type AgentMemLimit: str
        :param IstioCpuRequest: istioproxy 容器分配的 CPU 核數，對應 K8S 的 request
        :type IstioCpuRequest: str
        :param IstioCpuLimit: istioproxy 容器最大的 CPU 核數，對應 K8S 的 limit
        :type IstioCpuLimit: str
        :param IstioMemRequest: istioproxy 容器分配的内存 MiB 數，對應 K8S 的 request
        :type IstioMemRequest: str
        :param IstioMemLimit: istioproxy 容器最大的内存 MiB 數，對應 K8S 的 limit
        :type IstioMemLimit: str
        """
        self.GroupId = None
        self.Server = None
        self.TagName = None
        self.InstanceNum = None
        self.Reponame = None
        self.CpuLimit = None
        self.MemLimit = None
        self.JvmOpts = None
        self.CpuRequest = None
        self.MemRequest = None
        self.DoNotStart = None
        self.RepoName = None
        self.UpdateType = None
        self.UpdateIvl = None
        self.AgentCpuRequest = None
        self.AgentCpuLimit = None
        self.AgentMemRequest = None
        self.AgentMemLimit = None
        self.IstioCpuRequest = None
        self.IstioCpuLimit = None
        self.IstioMemRequest = None
        self.IstioMemLimit = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Server = params.get("Server")
        self.TagName = params.get("TagName")
        self.InstanceNum = params.get("InstanceNum")
        self.Reponame = params.get("Reponame")
        self.CpuLimit = params.get("CpuLimit")
        self.MemLimit = params.get("MemLimit")
        self.JvmOpts = params.get("JvmOpts")
        self.CpuRequest = params.get("CpuRequest")
        self.MemRequest = params.get("MemRequest")
        self.DoNotStart = params.get("DoNotStart")
        self.RepoName = params.get("RepoName")
        self.UpdateType = params.get("UpdateType")
        self.UpdateIvl = params.get("UpdateIvl")
        self.AgentCpuRequest = params.get("AgentCpuRequest")
        self.AgentCpuLimit = params.get("AgentCpuLimit")
        self.AgentMemRequest = params.get("AgentMemRequest")
        self.AgentMemLimit = params.get("AgentMemLimit")
        self.IstioCpuRequest = params.get("IstioCpuRequest")
        self.IstioCpuLimit = params.get("IstioCpuLimit")
        self.IstioMemRequest = params.get("IstioMemRequest")
        self.IstioMemLimit = params.get("IstioMemLimit")


class DeployContainerGroupResponse(AbstractModel):
    """DeployContainerGroup返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 佈署容器應用是否成功。
true：成功。
false：失敗。
        :type Result: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeployGroupRequest(AbstractModel):
    """DeployGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 佈署組ID
        :type GroupId: str
        :param PkgId: 程式包ID
        :type PkgId: str
        :param StartupParameters: 佈署組啓動參數
        :type StartupParameters: str
        """
        self.GroupId = None
        self.PkgId = None
        self.StartupParameters = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.PkgId = params.get("PkgId")
        self.StartupParameters = params.get("StartupParameters")


class DeployGroupResponse(AbstractModel):
    """DeployGroup返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 任務ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TaskId`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TaskId()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DeployServerlessGroupRequest(AbstractModel):
    """DeployServerlessGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 佈署組ID
        :type GroupId: str
        :param PkgId: 程式包ID
        :type PkgId: str
        :param Memory: 所需實例内存大小，取值爲 1Gi 2Gi 4Gi 8Gi 16Gi，缺省爲 1Gi，不傳表示維持原态
        :type Memory: str
        :param InstanceRequest: 要求最小實例數，取值範圍 [1, 4]，缺省爲 1，不傳表示維持原态
        :type InstanceRequest: int
        :param StartupParameters: 佈署組啓動參數，不傳表示維持原态
        :type StartupParameters: str
        """
        self.GroupId = None
        self.PkgId = None
        self.Memory = None
        self.InstanceRequest = None
        self.StartupParameters = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.PkgId = params.get("PkgId")
        self.Memory = params.get("Memory")
        self.InstanceRequest = params.get("InstanceRequest")
        self.StartupParameters = params.get("StartupParameters")


class DeployServerlessGroupResponse(AbstractModel):
    """DeployServerlessGroup返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 結果true：成功；false：失敗；
        :type Result: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeApplicationAttributeRequest(AbstractModel):
    """DescribeApplicationAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param ApplicationId: 應用ID
        :type ApplicationId: str
        """
        self.ApplicationId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")


class DescribeApplicationAttributeResponse(AbstractModel):
    """DescribeApplicationAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 應用清單其它欄位返回參數
        :type Result: :class:`tencentcloud.tsf.v20180326.models.ApplicationAttribute`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApplicationAttribute()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApplicationRequest(AbstractModel):
    """DescribeApplication請求參數結構體

    """

    def __init__(self):
        """
        :param ApplicationId: 應用ID
        :type ApplicationId: str
        """
        self.ApplicationId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")


class DescribeApplicationResponse(AbstractModel):
    """DescribeApplication返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 應用訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.ApplicationForPage`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApplicationForPage()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApplicationsRequest(AbstractModel):
    """DescribeApplications請求參數結構體

    """

    def __init__(self):
        """
        :param SearchWord: 搜索欄位
        :type SearchWord: str
        :param OrderBy: 排序欄位
        :type OrderBy: str
        :param OrderType: 排序類型
        :type OrderType: int
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 分頁個數
        :type Limit: int
        :param ApplicationType: 應用類型
        :type ApplicationType: str
        :param MicroserviceType: 應用的微服務類型
        :type MicroserviceType: str
        :param ApplicationResourceTypeList: 應用資源類型數組
        :type ApplicationResourceTypeList: list of str
        """
        self.SearchWord = None
        self.OrderBy = None
        self.OrderType = None
        self.Offset = None
        self.Limit = None
        self.ApplicationType = None
        self.MicroserviceType = None
        self.ApplicationResourceTypeList = None


    def _deserialize(self, params):
        self.SearchWord = params.get("SearchWord")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ApplicationType = params.get("ApplicationType")
        self.MicroserviceType = params.get("MicroserviceType")
        self.ApplicationResourceTypeList = params.get("ApplicationResourceTypeList")


class DescribeApplicationsResponse(AbstractModel):
    """DescribeApplications返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 應用分頁清單訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageApplication`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageApplication()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeClusterInstancesRequest(AbstractModel):
    """DescribeClusterInstances請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param SearchWord: 搜索欄位
        :type SearchWord: str
        :param OrderBy: 排序欄位
        :type OrderBy: str
        :param OrderType: 排序類型
        :type OrderType: int
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 分頁個數
        :type Limit: int
        """
        self.ClusterId = None
        self.SearchWord = None
        self.OrderBy = None
        self.OrderType = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.SearchWord = params.get("SearchWord")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeClusterInstancesResponse(AbstractModel):
    """DescribeClusterInstances返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 集群機器實例分頁訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageInstance`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageInstance()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeConfigReleaseLogsRequest(AbstractModel):
    """DescribeConfigReleaseLogs請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 佈署組ID，不傳入時查詢全量
        :type GroupId: str
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 每頁條數，預設爲20
        :type Limit: int
        :param NamespaceId: 命名空間ID，不傳入時查詢全量
        :type NamespaceId: str
        :param ClusterId: 集群ID，不傳入時查詢全量
        :type ClusterId: str
        :param ApplicationId: 應用ID，不傳入時查詢全量
        :type ApplicationId: str
        """
        self.GroupId = None
        self.Offset = None
        self.Limit = None
        self.NamespaceId = None
        self.ClusterId = None
        self.ApplicationId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.NamespaceId = params.get("NamespaceId")
        self.ClusterId = params.get("ClusterId")
        self.ApplicationId = params.get("ApplicationId")


class DescribeConfigReleaseLogsResponse(AbstractModel):
    """DescribeConfigReleaseLogs返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 分頁的配置項發布曆史清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageConfigReleaseLog`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageConfigReleaseLog()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeConfigReleasesRequest(AbstractModel):
    """DescribeConfigReleases請求參數結構體

    """

    def __init__(self):
        """
        :param ConfigName: 配置項名稱，不傳入時查詢全量
        :type ConfigName: str
        :param GroupId: 佈署組ID，不傳入時查詢全量
        :type GroupId: str
        :param NamespaceId: 命名空間ID，不傳入時查詢全量
        :type NamespaceId: str
        :param ClusterId: 集群ID，不傳入時查詢全量
        :type ClusterId: str
        :param Limit: 每頁條數
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        :param ConfigId: 配置ID，不傳入時查詢全量
        :type ConfigId: str
        :param ApplicationId: 應用ID，不傳入時查詢全量
        :type ApplicationId: str
        """
        self.ConfigName = None
        self.GroupId = None
        self.NamespaceId = None
        self.ClusterId = None
        self.Limit = None
        self.Offset = None
        self.ConfigId = None
        self.ApplicationId = None


    def _deserialize(self, params):
        self.ConfigName = params.get("ConfigName")
        self.GroupId = params.get("GroupId")
        self.NamespaceId = params.get("NamespaceId")
        self.ClusterId = params.get("ClusterId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.ConfigId = params.get("ConfigId")
        self.ApplicationId = params.get("ApplicationId")


class DescribeConfigReleasesResponse(AbstractModel):
    """DescribeConfigReleases返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 分頁的配置發布訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageConfigRelease`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageConfigRelease()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeConfigRequest(AbstractModel):
    """DescribeConfig請求參數結構體

    """

    def __init__(self):
        """
        :param ConfigId: 配置項ID
        :type ConfigId: str
        """
        self.ConfigId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")


class DescribeConfigResponse(AbstractModel):
    """DescribeConfig返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 配置項
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.Config`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = Config()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeConfigSummaryRequest(AbstractModel):
    """DescribeConfigSummary請求參數結構體

    """

    def __init__(self):
        """
        :param ApplicationId: 應用ID，不傳入時查詢全量
        :type ApplicationId: str
        :param SearchWord: 查詢關鍵字，模糊查詢：應用名稱，配置項名稱，不傳入時查詢全量
        :type SearchWord: str
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 每頁條數，預設爲20
        :type Limit: int
        """
        self.ApplicationId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeConfigSummaryResponse(AbstractModel):
    """DescribeConfigSummary返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 配置項分頁對象
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageConfig`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageConfig()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeConfigsRequest(AbstractModel):
    """DescribeConfigs請求參數結構體

    """

    def __init__(self):
        """
        :param ApplicationId: 應用ID，不傳入時查詢全量
        :type ApplicationId: str
        :param ConfigId: 配置項ID，不傳入時查詢全量，高優先級
        :type ConfigId: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 每頁條數
        :type Limit: int
        :param ConfigIdList: 配置項ID清單，不傳入時查詢全量，低優先級
        :type ConfigIdList: list of str
        :param ConfigName: 配置項名稱，精确查詢，不傳入時查詢全量
        :type ConfigName: str
        :param ConfigVersion: 配置項版本，精确查詢，不傳入時查詢全量
        :type ConfigVersion: str
        """
        self.ApplicationId = None
        self.ConfigId = None
        self.Offset = None
        self.Limit = None
        self.ConfigIdList = None
        self.ConfigName = None
        self.ConfigVersion = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.ConfigId = params.get("ConfigId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ConfigIdList = params.get("ConfigIdList")
        self.ConfigName = params.get("ConfigName")
        self.ConfigVersion = params.get("ConfigVersion")


class DescribeConfigsResponse(AbstractModel):
    """DescribeConfigs返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 分頁後的配置項清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageConfig`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageConfig()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeContainerGroupDetailRequest(AbstractModel):
    """DescribeContainerGroupDetail請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 分組ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DescribeContainerGroupDetailResponse(AbstractModel):
    """DescribeContainerGroupDetail返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 容器佈署組詳情
        :type Result: :class:`tencentcloud.tsf.v20180326.models.ContainerGroupDetail`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ContainerGroupDetail()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeContainerGroupsRequest(AbstractModel):
    """DescribeContainerGroups請求參數結構體

    """

    def __init__(self):
        """
        :param SearchWord: 搜索欄位，模糊搜索groupName欄位
        :type SearchWord: str
        :param ApplicationId: 分組所屬應用ID
        :type ApplicationId: str
        :param OrderBy: 排序欄位，預設爲 createTime欄位，支援id， name， createTime
        :type OrderBy: str
        :param OrderType: 排序方式，預設爲1：倒序排序，0：正序，1：倒序
        :type OrderType: int
        :param Offset: 偏移量，取值從0開始
        :type Offset: int
        :param Limit: 分頁個數，預設爲20， 取值應爲1~50
        :type Limit: int
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param NamespaceId: 命名空間 ID
        :type NamespaceId: str
        """
        self.SearchWord = None
        self.ApplicationId = None
        self.OrderBy = None
        self.OrderType = None
        self.Offset = None
        self.Limit = None
        self.ClusterId = None
        self.NamespaceId = None


    def _deserialize(self, params):
        self.SearchWord = params.get("SearchWord")
        self.ApplicationId = params.get("ApplicationId")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")


class DescribeContainerGroupsResponse(AbstractModel):
    """DescribeContainerGroups返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 查詢的權限數據對象
        :type Result: :class:`tencentcloud.tsf.v20180326.models.ContainGroupResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ContainGroupResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeDownloadInfoRequest(AbstractModel):
    """DescribeDownloadInfo請求參數結構體

    """

    def __init__(self):
        """
        :param ApplicationId: 應用ID
        :type ApplicationId: str
        :param PkgId: 程式包ID
        :type PkgId: str
        """
        self.ApplicationId = None
        self.PkgId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.PkgId = params.get("PkgId")


class DescribeDownloadInfoResponse(AbstractModel):
    """DescribeDownloadInfo返回參數結構體

    """

    def __init__(self):
        """
        :param Result: COS鑒權訊息
        :type Result: :class:`tencentcloud.tsf.v20180326.models.CosDownloadInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CosDownloadInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeGroupInstancesRequest(AbstractModel):
    """DescribeGroupInstances請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 佈署組ID
        :type GroupId: str
        :param SearchWord: 搜索欄位
        :type SearchWord: str
        :param OrderBy: 排序欄位
        :type OrderBy: str
        :param OrderType: 排序類型
        :type OrderType: int
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 分頁個數
        :type Limit: int
        """
        self.GroupId = None
        self.SearchWord = None
        self.OrderBy = None
        self.OrderType = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.SearchWord = params.get("SearchWord")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeGroupInstancesResponse(AbstractModel):
    """DescribeGroupInstances返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 佈署組機器訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageInstance`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageInstance()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeGroupRequest(AbstractModel):
    """DescribeGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 佈署組ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DescribeGroupResponse(AbstractModel):
    """DescribeGroup返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 虛拟機佈署組詳情
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.VmGroup`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = VmGroup()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeGroupsRequest(AbstractModel):
    """DescribeGroups請求參數結構體

    """

    def __init__(self):
        """
        :param SearchWord: 搜索欄位
        :type SearchWord: str
        :param ApplicationId: 應用ID
        :type ApplicationId: str
        :param OrderBy: 排序欄位
        :type OrderBy: str
        :param OrderType: 排序方式
        :type OrderType: int
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 分頁個數
        :type Limit: int
        :param NamespaceId: 命名空間ID
        :type NamespaceId: str
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param GroupResourceTypeList: 佈署組資源類型清單
        :type GroupResourceTypeList: list of str
        """
        self.SearchWord = None
        self.ApplicationId = None
        self.OrderBy = None
        self.OrderType = None
        self.Offset = None
        self.Limit = None
        self.NamespaceId = None
        self.ClusterId = None
        self.GroupResourceTypeList = None


    def _deserialize(self, params):
        self.SearchWord = params.get("SearchWord")
        self.ApplicationId = params.get("ApplicationId")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.NamespaceId = params.get("NamespaceId")
        self.ClusterId = params.get("ClusterId")
        self.GroupResourceTypeList = params.get("GroupResourceTypeList")


class DescribeGroupsResponse(AbstractModel):
    """DescribeGroups返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 虛拟機佈署組分頁訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageVmGroup`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageVmGroup()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeImageTagsRequest(AbstractModel):
    """DescribeImageTags請求參數結構體

    """

    def __init__(self):
        """
        :param ApplicationId: 應用Id
        :type ApplicationId: str
        :param Offset: 偏移量，取值從0開始
        :type Offset: int
        :param Limit: 分頁個數，預設爲20， 取值應爲1~100
        :type Limit: int
        :param QueryImageIdFlag: 不填和0:查詢 1:不查詢
        :type QueryImageIdFlag: int
        :param SearchWord: 可用于搜索的 tag 名字
        :type SearchWord: str
        """
        self.ApplicationId = None
        self.Offset = None
        self.Limit = None
        self.QueryImageIdFlag = None
        self.SearchWord = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.QueryImageIdFlag = params.get("QueryImageIdFlag")
        self.SearchWord = params.get("SearchWord")


class DescribeImageTagsResponse(AbstractModel):
    """DescribeImageTags返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 查詢的權限數據對象
        :type Result: :class:`tencentcloud.tsf.v20180326.models.ImageTagsResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ImageTagsResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeMicroserviceRequest(AbstractModel):
    """DescribeMicroservice請求參數結構體

    """

    def __init__(self):
        """
        :param MicroserviceId: 微服務ID
        :type MicroserviceId: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 分頁個數
        :type Limit: int
        """
        self.MicroserviceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.MicroserviceId = params.get("MicroserviceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeMicroserviceResponse(AbstractModel):
    """DescribeMicroservice返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 微服務詳情實例清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageMsInstance`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageMsInstance()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeMicroservicesRequest(AbstractModel):
    """DescribeMicroservices請求參數結構體

    """

    def __init__(self):
        """
        :param NamespaceId: 命名空間ID
        :type NamespaceId: str
        :param SearchWord: 搜索欄位
        :type SearchWord: str
        :param OrderBy: 排序欄位
        :type OrderBy: str
        :param OrderType: 排序類型
        :type OrderType: int
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 分頁個數
        :type Limit: int
        """
        self.NamespaceId = None
        self.SearchWord = None
        self.OrderBy = None
        self.OrderType = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.SearchWord = params.get("SearchWord")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeMicroservicesResponse(AbstractModel):
    """DescribeMicroservices返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 微服務分頁清單訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageMicroservice`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageMicroservice()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribePkgsRequest(AbstractModel):
    """DescribePkgs請求參數結構體

    """

    def __init__(self):
        """
        :param ApplicationId: 應用ID（只傳入應用ID，返回該應用下所有軟體包訊息）
        :type ApplicationId: str
        :param SearchWord: 查詢關鍵字（支援根據包ID，包名，包版本号搜索）
        :type SearchWord: str
        :param OrderBy: 排序關鍵字（預設爲"UploadTime"：上傳時間）
        :type OrderBy: str
        :param OrderType: 升序：0/降序：1（預設降序）
        :type OrderType: int
        :param Offset: 查詢起始偏移
        :type Offset: int
        :param Limit: 返回數量限制
        :type Limit: int
        """
        self.ApplicationId = None
        self.SearchWord = None
        self.OrderBy = None
        self.OrderType = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.SearchWord = params.get("SearchWord")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribePkgsResponse(AbstractModel):
    """DescribePkgs返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 符合查詢程式包訊息清單
        :type Result: :class:`tencentcloud.tsf.v20180326.models.PkgList`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = PkgList()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribePodInstancesRequest(AbstractModel):
    """DescribePodInstances請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 實例所屬groupId
        :type GroupId: str
        :param Offset: 偏移量，取值從0開始
        :type Offset: int
        :param Limit: 分頁個數，預設爲20， 取值應爲1~50
        :type Limit: int
        """
        self.GroupId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribePodInstancesResponse(AbstractModel):
    """DescribePodInstances返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 查詢的權限數據對象
        :type Result: :class:`tencentcloud.tsf.v20180326.models.GroupPodResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = GroupPodResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribePublicConfigReleaseLogsRequest(AbstractModel):
    """DescribePublicConfigReleaseLogs請求參數結構體

    """

    def __init__(self):
        """
        :param NamespaceId: 命名空間ID，不傳入時查詢全量
        :type NamespaceId: str
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 每頁條數，預設爲20
        :type Limit: int
        """
        self.NamespaceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribePublicConfigReleaseLogsResponse(AbstractModel):
    """DescribePublicConfigReleaseLogs返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 分頁後的公共配置項發布曆史清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageConfigReleaseLog`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageConfigReleaseLog()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribePublicConfigReleasesRequest(AbstractModel):
    """DescribePublicConfigReleases請求參數結構體

    """

    def __init__(self):
        """
        :param ConfigName: 配置項名稱，不傳入時查詢全量
        :type ConfigName: str
        :param NamespaceId: 命名空間ID，不傳入時查詢全量
        :type NamespaceId: str
        :param Limit: 每頁條數
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        :param ConfigId: 配置項ID，不傳入時查詢全量
        :type ConfigId: str
        """
        self.ConfigName = None
        self.NamespaceId = None
        self.Limit = None
        self.Offset = None
        self.ConfigId = None


    def _deserialize(self, params):
        self.ConfigName = params.get("ConfigName")
        self.NamespaceId = params.get("NamespaceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.ConfigId = params.get("ConfigId")


class DescribePublicConfigReleasesResponse(AbstractModel):
    """DescribePublicConfigReleases返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 公共配置發布訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageConfigRelease`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageConfigRelease()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribePublicConfigRequest(AbstractModel):
    """DescribePublicConfig請求參數結構體

    """

    def __init__(self):
        """
        :param ConfigId: 需要查詢的配置項ID
        :type ConfigId: str
        """
        self.ConfigId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")


class DescribePublicConfigResponse(AbstractModel):
    """DescribePublicConfig返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 全局配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.Config`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = Config()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribePublicConfigSummaryRequest(AbstractModel):
    """DescribePublicConfigSummary請求參數結構體

    """

    def __init__(self):
        """
        :param SearchWord: 查詢關鍵字，模糊查詢：配置項名稱，不傳入時查詢全量
        :type SearchWord: str
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 每頁條數，預設爲20
        :type Limit: int
        """
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribePublicConfigSummaryResponse(AbstractModel):
    """DescribePublicConfigSummary返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 分頁的全局配置統計訊息清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageConfig`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageConfig()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribePublicConfigsRequest(AbstractModel):
    """DescribePublicConfigs請求參數結構體

    """

    def __init__(self):
        """
        :param ConfigId: 配置項ID，不傳入時查詢全量，高優先級
        :type ConfigId: str
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 每頁條數，預設爲20
        :type Limit: int
        :param ConfigIdList: 配置項ID清單，不傳入時查詢全量，低優先級
        :type ConfigIdList: list of str
        :param ConfigName: 配置項名稱，精确查詢，不傳入時查詢全量
        :type ConfigName: str
        :param ConfigVersion: 配置項版本，精确查詢，不傳入時查詢全量
        :type ConfigVersion: str
        """
        self.ConfigId = None
        self.Offset = None
        self.Limit = None
        self.ConfigIdList = None
        self.ConfigName = None
        self.ConfigVersion = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ConfigIdList = params.get("ConfigIdList")
        self.ConfigName = params.get("ConfigName")
        self.ConfigVersion = params.get("ConfigVersion")


class DescribePublicConfigsResponse(AbstractModel):
    """DescribePublicConfigs返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 分頁後的全局配置項清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageConfig`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageConfig()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeReleasedConfigRequest(AbstractModel):
    """DescribeReleasedConfig請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 佈署組ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DescribeReleasedConfigResponse(AbstractModel):
    """DescribeReleasedConfig返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 已發布的配置内容
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeServerlessGroupRequest(AbstractModel):
    """DescribeServerlessGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 佈署組ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DescribeServerlessGroupResponse(AbstractModel):
    """DescribeServerlessGroup返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 結果
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.ServerlessGroup`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ServerlessGroup()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeServerlessGroupsRequest(AbstractModel):
    """DescribeServerlessGroups請求參數結構體

    """

    def __init__(self):
        """
        :param SearchWord: 搜索欄位，模糊搜索groupName欄位
        :type SearchWord: str
        :param ApplicationId: 分組所屬應用ID
        :type ApplicationId: str
        :param OrderBy: 排序欄位，預設爲 createTime欄位，支援id， name， createTime
        :type OrderBy: str
        :param OrderType: 排序方式，預設爲1：倒序排序，0：正序，1：倒序
        :type OrderType: str
        :param Offset: 偏移量，取值從0開始
        :type Offset: int
        :param Limit: 分頁個數，預設爲20， 取值應爲1~50
        :type Limit: int
        :param NamespaceId: 分組所屬名字空間ID
        :type NamespaceId: str
        :param ClusterId: 分組所屬集群ID
        :type ClusterId: str
        """
        self.SearchWord = None
        self.ApplicationId = None
        self.OrderBy = None
        self.OrderType = None
        self.Offset = None
        self.Limit = None
        self.NamespaceId = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.SearchWord = params.get("SearchWord")
        self.ApplicationId = params.get("ApplicationId")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.NamespaceId = params.get("NamespaceId")
        self.ClusterId = params.get("ClusterId")


class DescribeServerlessGroupsResponse(AbstractModel):
    """DescribeServerlessGroups返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 數據清單對象
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.ServerlessGroupPage`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ServerlessGroupPage()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeSimpleApplicationsRequest(AbstractModel):
    """DescribeSimpleApplications請求參數結構體

    """

    def __init__(self):
        """
        :param ApplicationIdList: 應用ID清單
        :type ApplicationIdList: list of str
        :param ApplicationType: 應用類型
        :type ApplicationType: str
        :param Limit: 每頁條數
        :type Limit: int
        :param Offset: 起始偏移量
        :type Offset: int
        :param MicroserviceType: 微服務類型
        :type MicroserviceType: str
        :param ApplicationResourceTypeList: 資源類型數組
        :type ApplicationResourceTypeList: list of str
        :param SearchWord: 通過id和name進行關鍵詞過濾
        :type SearchWord: str
        """
        self.ApplicationIdList = None
        self.ApplicationType = None
        self.Limit = None
        self.Offset = None
        self.MicroserviceType = None
        self.ApplicationResourceTypeList = None
        self.SearchWord = None


    def _deserialize(self, params):
        self.ApplicationIdList = params.get("ApplicationIdList")
        self.ApplicationType = params.get("ApplicationType")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.MicroserviceType = params.get("MicroserviceType")
        self.ApplicationResourceTypeList = params.get("ApplicationResourceTypeList")
        self.SearchWord = params.get("SearchWord")


class DescribeSimpleApplicationsResponse(AbstractModel):
    """DescribeSimpleApplications返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 簡單應用分頁對象
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageSimpleApplication`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageSimpleApplication()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeSimpleClustersRequest(AbstractModel):
    """DescribeSimpleClusters請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterIdList: 需要查詢的集群ID清單，不填或不傳入時查詢所有内容
        :type ClusterIdList: list of str
        :param ClusterType: 需要查詢的集群類型，不填或不傳入時查詢所有内容
        :type ClusterType: str
        :param Offset: 查詢偏移量，預設爲0
        :type Offset: int
        :param Limit: 分頁個數，預設爲20， 取值應爲1~50
        :type Limit: int
        :param SearchWord: 對id和name進行關鍵詞過濾
        :type SearchWord: str
        """
        self.ClusterIdList = None
        self.ClusterType = None
        self.Offset = None
        self.Limit = None
        self.SearchWord = None


    def _deserialize(self, params):
        self.ClusterIdList = params.get("ClusterIdList")
        self.ClusterType = params.get("ClusterType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchWord = params.get("SearchWord")


class DescribeSimpleClustersResponse(AbstractModel):
    """DescribeSimpleClusters返回參數結構體

    """

    def __init__(self):
        """
        :param Result: TSF集群分頁對象
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageCluster`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageCluster()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeSimpleGroupsRequest(AbstractModel):
    """DescribeSimpleGroups請求參數結構體

    """

    def __init__(self):
        """
        :param GroupIdList: 佈署組ID清單，不填寫時查詢全量
        :type GroupIdList: list of str
        :param ApplicationId: 應用ID，不填寫時查詢全量
        :type ApplicationId: str
        :param ClusterId: 集群ID，不填寫時查詢全量
        :type ClusterId: str
        :param NamespaceId: 命名空間ID，不填寫時查詢全量
        :type NamespaceId: str
        :param Limit: 每頁條數
        :type Limit: int
        :param Offset: 起始偏移量
        :type Offset: int
        :param GroupId: 佈署組ID，不填寫時查詢全量
        :type GroupId: str
        :param SearchWord: 模糊查詢，佈署組名稱，不填寫時查詢全量
        :type SearchWord: str
        :param AppMicroServiceType: 佈署組類型，精确過濾欄位，M：service mesh, P：原生應用， M：閘道應用
        :type AppMicroServiceType: str
        """
        self.GroupIdList = None
        self.ApplicationId = None
        self.ClusterId = None
        self.NamespaceId = None
        self.Limit = None
        self.Offset = None
        self.GroupId = None
        self.SearchWord = None
        self.AppMicroServiceType = None


    def _deserialize(self, params):
        self.GroupIdList = params.get("GroupIdList")
        self.ApplicationId = params.get("ApplicationId")
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.GroupId = params.get("GroupId")
        self.SearchWord = params.get("SearchWord")
        self.AppMicroServiceType = params.get("AppMicroServiceType")


class DescribeSimpleGroupsResponse(AbstractModel):
    """DescribeSimpleGroups返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 簡單佈署組清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageSimpleGroup`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageSimpleGroup()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeSimpleNamespacesRequest(AbstractModel):
    """DescribeSimpleNamespaces請求參數結構體

    """

    def __init__(self):
        """
        :param NamespaceIdList: 命名空間ID清單，不傳入時查詢全量
        :type NamespaceIdList: list of str
        :param ClusterId: 集群ID，不傳入時查詢全量
        :type ClusterId: str
        :param Limit: 每頁條數
        :type Limit: int
        :param Offset: 起始偏移量
        :type Offset: int
        :param NamespaceId: 命名空間ID，不傳入時查詢全量
        :type NamespaceId: str
        :param NamespaceResourceTypeList: 查詢資源類型清單
        :type NamespaceResourceTypeList: list of str
        :param SearchWord: 通過id和name進行過濾
        :type SearchWord: str
        :param NamespaceTypeList: 查詢的命名空間類型清單
        :type NamespaceTypeList: list of str
        :param NamespaceName: 通過命名空間名精确過濾
        :type NamespaceName: str
        :param IsDefault: 通過是否是預設命名空間過濾，不傳表示拉取全部命名空間。0：預設，命名空間。1：非預設命名空間
        :type IsDefault: str
        """
        self.NamespaceIdList = None
        self.ClusterId = None
        self.Limit = None
        self.Offset = None
        self.NamespaceId = None
        self.NamespaceResourceTypeList = None
        self.SearchWord = None
        self.NamespaceTypeList = None
        self.NamespaceName = None
        self.IsDefault = None


    def _deserialize(self, params):
        self.NamespaceIdList = params.get("NamespaceIdList")
        self.ClusterId = params.get("ClusterId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceResourceTypeList = params.get("NamespaceResourceTypeList")
        self.SearchWord = params.get("SearchWord")
        self.NamespaceTypeList = params.get("NamespaceTypeList")
        self.NamespaceName = params.get("NamespaceName")
        self.IsDefault = params.get("IsDefault")


class DescribeSimpleNamespacesResponse(AbstractModel):
    """DescribeSimpleNamespaces返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 命名空間分頁清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TsfPageNamespace`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TsfPageNamespace()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeUploadInfoRequest(AbstractModel):
    """DescribeUploadInfo請求參數結構體

    """

    def __init__(self):
        """
        :param ApplicationId: 應用ID
        :type ApplicationId: str
        :param PkgName: 程式包名
        :type PkgName: str
        :param PkgVersion: 程式包版本
        :type PkgVersion: str
        :param PkgType: 程式包類型
        :type PkgType: str
        :param PkgDesc: 程式包介紹
        :type PkgDesc: str
        """
        self.ApplicationId = None
        self.PkgName = None
        self.PkgVersion = None
        self.PkgType = None
        self.PkgDesc = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.PkgName = params.get("PkgName")
        self.PkgVersion = params.get("PkgVersion")
        self.PkgType = params.get("PkgType")
        self.PkgDesc = params.get("PkgDesc")


class DescribeUploadInfoResponse(AbstractModel):
    """DescribeUploadInfo返回參數結構體

    """

    def __init__(self):
        """
        :param Result: COS上傳訊息
        :type Result: :class:`tencentcloud.tsf.v20180326.models.CosUploadInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CosUploadInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class Env(AbstractModel):
    """環境變量

    """

    def __init__(self):
        """
        :param Name: 環境變量名稱
        :type Name: str
        :param Value: 服務端口
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class ExpandGroupRequest(AbstractModel):
    """ExpandGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 佈署組ID
        :type GroupId: str
        :param InstanceIdList: 擴容的機器實例ID清單
        :type InstanceIdList: list of str
        """
        self.GroupId = None
        self.InstanceIdList = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.InstanceIdList = params.get("InstanceIdList")


class ExpandGroupResponse(AbstractModel):
    """ExpandGroup返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 任務ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TaskId`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TaskId()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class GroupPod(AbstractModel):
    """佈署組實例清單

    """

    def __init__(self):
        """
        :param PodName: 實例名稱(對應到kubernetes的pod名稱)
注意：此欄位可能返回 null，表示取不到有效值。
        :type PodName: str
        :param PodId: 實例ID(對應到kubernetes的pod id)
注意：此欄位可能返回 null，表示取不到有效值。
        :type PodId: str
        :param Status: 實例狀态，請參考後面的實例以及容器的狀态定義
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: str
        :param Reason: 實例處于當前狀态的原因，例如容器下載映像失敗
注意：此欄位可能返回 null，表示取不到有效值。
        :type Reason: str
        :param NodeIp: 主機IP
注意：此欄位可能返回 null，表示取不到有效值。
        :type NodeIp: str
        :param Ip: 實例IP
注意：此欄位可能返回 null，表示取不到有效值。
        :type Ip: str
        :param RestartCount: 實例中容器的重啓次數
注意：此欄位可能返回 null，表示取不到有效值。
        :type RestartCount: int
        :param ReadyCount: 實例中已就緒容器的個數
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReadyCount: int
        :param Runtime: 運作時長
注意：此欄位可能返回 null，表示取不到有效值。
        :type Runtime: str
        :param CreatedAt: 實例啓動時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param ServiceInstanceStatus: 服務實例狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type ServiceInstanceStatus: str
        :param InstanceAvailableStatus: 機器實例可使用狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceAvailableStatus: str
        :param InstanceStatus: 機器實例狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceStatus: str
        """
        self.PodName = None
        self.PodId = None
        self.Status = None
        self.Reason = None
        self.NodeIp = None
        self.Ip = None
        self.RestartCount = None
        self.ReadyCount = None
        self.Runtime = None
        self.CreatedAt = None
        self.ServiceInstanceStatus = None
        self.InstanceAvailableStatus = None
        self.InstanceStatus = None


    def _deserialize(self, params):
        self.PodName = params.get("PodName")
        self.PodId = params.get("PodId")
        self.Status = params.get("Status")
        self.Reason = params.get("Reason")
        self.NodeIp = params.get("NodeIp")
        self.Ip = params.get("Ip")
        self.RestartCount = params.get("RestartCount")
        self.ReadyCount = params.get("ReadyCount")
        self.Runtime = params.get("Runtime")
        self.CreatedAt = params.get("CreatedAt")
        self.ServiceInstanceStatus = params.get("ServiceInstanceStatus")
        self.InstanceAvailableStatus = params.get("InstanceAvailableStatus")
        self.InstanceStatus = params.get("InstanceStatus")


class GroupPodResult(AbstractModel):
    """佈署組實例清單

    """

    def __init__(self):
        """
        :param TotalCount: 總記錄數
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 清單訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Content: list of GroupPod
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = GroupPod()
                obj._deserialize(item)
                self.Content.append(obj)


class ImageTag(AbstractModel):
    """清單訊息

    """

    def __init__(self):
        """
        :param RepoName: 倉庫名
        :type RepoName: str
        :param TagName: 版本名稱
        :type TagName: str
        :param TagId: 版本ID
        :type TagId: str
        :param ImageId: 映像ID
        :type ImageId: str
        :param Size: 大小
        :type Size: str
        :param CreationTime: 創建時間
        :type CreationTime: str
        :param UpdateTime: 更新時間
        :type UpdateTime: str
        :param Author: 映像制作者
        :type Author: str
        :param Architecture: CPU架構
        :type Architecture: str
        :param DockerVersion: Docker用戶端版本
        :type DockerVersion: str
        :param Os: 作業系統
注意：此欄位可能返回 null，表示取不到有效值。
        :type Os: str
        :param PushTime: push時間
        :type PushTime: str
        :param SizeByte: 單位爲位元
        :type SizeByte: int
        """
        self.RepoName = None
        self.TagName = None
        self.TagId = None
        self.ImageId = None
        self.Size = None
        self.CreationTime = None
        self.UpdateTime = None
        self.Author = None
        self.Architecture = None
        self.DockerVersion = None
        self.Os = None
        self.PushTime = None
        self.SizeByte = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.TagName = params.get("TagName")
        self.TagId = params.get("TagId")
        self.ImageId = params.get("ImageId")
        self.Size = params.get("Size")
        self.CreationTime = params.get("CreationTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Author = params.get("Author")
        self.Architecture = params.get("Architecture")
        self.DockerVersion = params.get("DockerVersion")
        self.Os = params.get("Os")
        self.PushTime = params.get("PushTime")
        self.SizeByte = params.get("SizeByte")


class ImageTagsResult(AbstractModel):
    """映像版本清單

    """

    def __init__(self):
        """
        :param TotalCount: 總記錄數
        :type TotalCount: int
        :param RepoName: 倉庫名,含命名空間,如tsf/ngin
        :type RepoName: str
        :param Server: 映像服務器網址
        :type Server: str
        :param Content: 清單訊息
        :type Content: list of ImageTag
        """
        self.TotalCount = None
        self.RepoName = None
        self.Server = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.RepoName = params.get("RepoName")
        self.Server = params.get("Server")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = ImageTag()
                obj._deserialize(item)
                self.Content.append(obj)


class Instance(AbstractModel):
    """機器實例

    """

    def __init__(self):
        """
        :param InstanceId: 機器實例ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param InstanceName: 機器名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param LanIp: 機器内網網址IP
注意：此欄位可能返回 null，表示取不到有效值。
        :type LanIp: str
        :param WanIp: 機器外網網址IP
注意：此欄位可能返回 null，表示取不到有效值。
        :type WanIp: str
        :param InstanceDesc: 機器描述訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceDesc: str
        :param ClusterId: 集群ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param ClusterName: 集群名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param InstanceStatus: VM的狀态 虛機：虛機的狀态 容器：Pod所在虛機的狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceStatus: str
        :param InstanceAvailableStatus: VM的可使用狀态 虛機：虛機是否能夠作爲資源使用 容器：虛機是否能夠作爲資源佈署POD
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceAvailableStatus: str
        :param ServiceInstanceStatus: 服務下的服務實例的狀态 虛機：應用是否可用 + Agent狀态 容器：Pod狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type ServiceInstanceStatus: str
        :param CountInTsf: 标識此instance是否已添加在tsf中
注意：此欄位可能返回 null，表示取不到有效值。
        :type CountInTsf: int
        :param GroupId: 機器所屬佈署組ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param ApplicationId: 機器所屬應用ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param ApplicationName: 機器所屬應用名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param InstanceCreatedTime: 機器實例在CVM的創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceCreatedTime: str
        :param InstanceExpiredTime: 機器實例在CVM的過期時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceExpiredTime: str
        :param InstanceChargeType: 機器實例在CVM的計費模式
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceChargeType: str
        :param InstanceTotalCpu: 機器實例總CPU訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceTotalCpu: float
        :param InstanceTotalMem: 機器實例總内存訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceTotalMem: float
        :param InstanceUsedCpu: 機器實例使用的CPU訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceUsedCpu: float
        :param InstanceUsedMem: 機器實例使用的内存訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceUsedMem: float
        :param InstanceLimitCpu: 機器實例Limit CPU訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceLimitCpu: float
        :param InstanceLimitMem: 機器實例Limit 内存訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceLimitMem: float
        :param InstancePkgVersion: 包版本
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstancePkgVersion: str
        :param ClusterType: 集群類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterType: str
        :param RestrictState: 機器實例業務狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type RestrictState: str
        :param UpdateTime: 更新時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param OperationState: 實例執行狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type OperationState: int
        :param NamespaceId: NamespaceId
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param InstanceZoneId: InstanceZoneId
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceZoneId: str
        :param InstanceImportMode: InstanceImportMode
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceImportMode: str
        :param ApplicationType: ApplicationType
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationType: str
        :param ApplicationResourceType: ApplicationResourceType
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationResourceType: str
        :param ServiceSidecarStatus: ServiceSidecarStatus
注意：此欄位可能返回 null，表示取不到有效值。
        :type ServiceSidecarStatus: str
        :param GroupName: GroupName
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param NamespaceName: NamespaceName
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.LanIp = None
        self.WanIp = None
        self.InstanceDesc = None
        self.ClusterId = None
        self.ClusterName = None
        self.InstanceStatus = None
        self.InstanceAvailableStatus = None
        self.ServiceInstanceStatus = None
        self.CountInTsf = None
        self.GroupId = None
        self.ApplicationId = None
        self.ApplicationName = None
        self.InstanceCreatedTime = None
        self.InstanceExpiredTime = None
        self.InstanceChargeType = None
        self.InstanceTotalCpu = None
        self.InstanceTotalMem = None
        self.InstanceUsedCpu = None
        self.InstanceUsedMem = None
        self.InstanceLimitCpu = None
        self.InstanceLimitMem = None
        self.InstancePkgVersion = None
        self.ClusterType = None
        self.RestrictState = None
        self.UpdateTime = None
        self.OperationState = None
        self.NamespaceId = None
        self.InstanceZoneId = None
        self.InstanceImportMode = None
        self.ApplicationType = None
        self.ApplicationResourceType = None
        self.ServiceSidecarStatus = None
        self.GroupName = None
        self.NamespaceName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.LanIp = params.get("LanIp")
        self.WanIp = params.get("WanIp")
        self.InstanceDesc = params.get("InstanceDesc")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.InstanceStatus = params.get("InstanceStatus")
        self.InstanceAvailableStatus = params.get("InstanceAvailableStatus")
        self.ServiceInstanceStatus = params.get("ServiceInstanceStatus")
        self.CountInTsf = params.get("CountInTsf")
        self.GroupId = params.get("GroupId")
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.InstanceCreatedTime = params.get("InstanceCreatedTime")
        self.InstanceExpiredTime = params.get("InstanceExpiredTime")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.InstanceTotalCpu = params.get("InstanceTotalCpu")
        self.InstanceTotalMem = params.get("InstanceTotalMem")
        self.InstanceUsedCpu = params.get("InstanceUsedCpu")
        self.InstanceUsedMem = params.get("InstanceUsedMem")
        self.InstanceLimitCpu = params.get("InstanceLimitCpu")
        self.InstanceLimitMem = params.get("InstanceLimitMem")
        self.InstancePkgVersion = params.get("InstancePkgVersion")
        self.ClusterType = params.get("ClusterType")
        self.RestrictState = params.get("RestrictState")
        self.UpdateTime = params.get("UpdateTime")
        self.OperationState = params.get("OperationState")
        self.NamespaceId = params.get("NamespaceId")
        self.InstanceZoneId = params.get("InstanceZoneId")
        self.InstanceImportMode = params.get("InstanceImportMode")
        self.ApplicationType = params.get("ApplicationType")
        self.ApplicationResourceType = params.get("ApplicationResourceType")
        self.ServiceSidecarStatus = params.get("ServiceSidecarStatus")
        self.GroupName = params.get("GroupName")
        self.NamespaceName = params.get("NamespaceName")


class Microservice(AbstractModel):
    """微服務

    """

    def __init__(self):
        """
        :param MicroserviceId: 微服務ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type MicroserviceId: str
        :param MicroserviceName: 微服務名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type MicroserviceName: str
        :param MicroserviceDesc: 微服務描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type MicroserviceDesc: str
        :param CreateTime: 創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param UpdateTime: 更新時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param NamespaceId: 命名空間ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param RunInstanceCount: 微服務的運作實例數目
注意：此欄位可能返回 null，表示取不到有效值。
        :type RunInstanceCount: int
        """
        self.MicroserviceId = None
        self.MicroserviceName = None
        self.MicroserviceDesc = None
        self.CreateTime = None
        self.UpdateTime = None
        self.NamespaceId = None
        self.RunInstanceCount = None


    def _deserialize(self, params):
        self.MicroserviceId = params.get("MicroserviceId")
        self.MicroserviceName = params.get("MicroserviceName")
        self.MicroserviceDesc = params.get("MicroserviceDesc")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.NamespaceId = params.get("NamespaceId")
        self.RunInstanceCount = params.get("RunInstanceCount")


class ModifyContainerGroupRequest(AbstractModel):
    """ModifyContainerGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 佈署組ID
        :type GroupId: str
        :param AccessType: 0:公網 1:集群内訪問 2：NodePort
        :type AccessType: int
        :param ProtocolPorts: ProtocolPorts數組
        :type ProtocolPorts: list of ProtocolPort
        :param UpdateType: 更新方式：0:快速更新 1:滾動更新
        :type UpdateType: int
        :param UpdateIvl: 更新間隔,單位秒
        :type UpdateIvl: int
        """
        self.GroupId = None
        self.AccessType = None
        self.ProtocolPorts = None
        self.UpdateType = None
        self.UpdateIvl = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.AccessType = params.get("AccessType")
        if params.get("ProtocolPorts") is not None:
            self.ProtocolPorts = []
            for item in params.get("ProtocolPorts"):
                obj = ProtocolPort()
                obj._deserialize(item)
                self.ProtocolPorts.append(obj)
        self.UpdateType = params.get("UpdateType")
        self.UpdateIvl = params.get("UpdateIvl")


class ModifyContainerGroupResponse(AbstractModel):
    """ModifyContainerGroup返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 更新佈署組是否成功。
true：成功。
false：失敗。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyContainerReplicasRequest(AbstractModel):
    """ModifyContainerReplicas請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 佈署組ID，佈署組唯一标識
        :type GroupId: str
        :param InstanceNum: 實例數量
        :type InstanceNum: int
        """
        self.GroupId = None
        self.InstanceNum = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.InstanceNum = params.get("InstanceNum")


class ModifyContainerReplicasResponse(AbstractModel):
    """ModifyContainerReplicas返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 結果true：成功；false：失敗；
        :type Result: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyMicroserviceRequest(AbstractModel):
    """ModifyMicroservice請求參數結構體

    """

    def __init__(self):
        """
        :param MicroserviceId: 微服務 ID
        :type MicroserviceId: str
        :param MicroserviceDesc: 微服務備注訊息
        :type MicroserviceDesc: str
        """
        self.MicroserviceId = None
        self.MicroserviceDesc = None


    def _deserialize(self, params):
        self.MicroserviceId = params.get("MicroserviceId")
        self.MicroserviceDesc = params.get("MicroserviceDesc")


class ModifyMicroserviceResponse(AbstractModel):
    """ModifyMicroservice返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 修改微服務詳情是否成功。
true：操作成功。
false：操作失敗。
        :type Result: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyUploadInfoRequest(AbstractModel):
    """ModifyUploadInfo請求參數結構體

    """

    def __init__(self):
        """
        :param ApplicationId: 應用ID
        :type ApplicationId: str
        :param PkgId: 調用DescribeUploadInfo介面時返回的軟體包ID
        :type PkgId: str
        :param Result: COS返回上傳結果（預設爲0：成功，其他值表示失敗）
        :type Result: int
        :param Md5: 程式包MD5
        :type Md5: str
        :param Size: 程式包大小（單位位元）
        :type Size: int
        """
        self.ApplicationId = None
        self.PkgId = None
        self.Result = None
        self.Md5 = None
        self.Size = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.PkgId = params.get("PkgId")
        self.Result = params.get("Result")
        self.Md5 = params.get("Md5")
        self.Size = params.get("Size")


class ModifyUploadInfoResponse(AbstractModel):
    """ModifyUploadInfo返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MsInstance(AbstractModel):
    """微服務實例訊息

    """

    def __init__(self):
        """
        :param InstanceId: 機器實例ID訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param InstanceName: 機器實例名稱訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param Port: 服務運作的端口号
注意：此欄位可能返回 null，表示取不到有效值。
        :type Port: str
        :param LanIp: 機器實例内網IP
注意：此欄位可能返回 null，表示取不到有效值。
        :type LanIp: str
        :param WanIp: 機器實例外網IP
注意：此欄位可能返回 null，表示取不到有效值。
        :type WanIp: str
        :param InstanceAvailableStatus: 機器可用狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceAvailableStatus: str
        :param ServiceInstanceStatus: 服務運作狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type ServiceInstanceStatus: str
        :param ApplicationId: 應用ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param ApplicationName: 應用名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param ClusterId: 集群ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param ClusterName: 集群名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param NamespaceId: 命名空間ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param NamespaceName: 命名空間名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        :param GroupId: 佈署組ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param GroupName: 佈署組名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param InstanceStatus: 機器TSF可用狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceStatus: str
        :param HealthCheckUrl: 健康檢查URL
注意：此欄位可能返回 null，表示取不到有效值。
        :type HealthCheckUrl: str
        :param ClusterType: 集群類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterType: str
        :param ApplicationPackageVersion: 應用程式包版本
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationPackageVersion: str
        :param ApplicationType: 應用類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationType: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Port = None
        self.LanIp = None
        self.WanIp = None
        self.InstanceAvailableStatus = None
        self.ServiceInstanceStatus = None
        self.ApplicationId = None
        self.ApplicationName = None
        self.ClusterId = None
        self.ClusterName = None
        self.NamespaceId = None
        self.NamespaceName = None
        self.GroupId = None
        self.GroupName = None
        self.InstanceStatus = None
        self.HealthCheckUrl = None
        self.ClusterType = None
        self.ApplicationPackageVersion = None
        self.ApplicationType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Port = params.get("Port")
        self.LanIp = params.get("LanIp")
        self.WanIp = params.get("WanIp")
        self.InstanceAvailableStatus = params.get("InstanceAvailableStatus")
        self.ServiceInstanceStatus = params.get("ServiceInstanceStatus")
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.InstanceStatus = params.get("InstanceStatus")
        self.HealthCheckUrl = params.get("HealthCheckUrl")
        self.ClusterType = params.get("ClusterType")
        self.ApplicationPackageVersion = params.get("ApplicationPackageVersion")
        self.ApplicationType = params.get("ApplicationType")


class Namespace(AbstractModel):
    """命名空間

    """

    def __init__(self):
        """
        :param NamespaceId: 命名空間ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param NamespaceCode: 命名空間編碼
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceCode: str
        :param NamespaceName: 命名空間名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        :param NamespaceDesc: 命名空間描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceDesc: str
        :param IsDefault: 預設命名空間
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsDefault: str
        :param NamespaceStatus: 命名空間狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceStatus: str
        :param DeleteFlag: 删除标識
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeleteFlag: bool
        :param CreateTime: 創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 更新時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param ClusterList: 集群數組，僅攜帶集群ID，集群名稱，集群類型等基礎訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterList: list of Cluster
        :param ClusterId: 集群ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param NamespaceResourceType: 集群資源類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceResourceType: str
        :param NamespaceType: 命名空間類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceType: str
        """
        self.NamespaceId = None
        self.NamespaceCode = None
        self.NamespaceName = None
        self.NamespaceDesc = None
        self.IsDefault = None
        self.NamespaceStatus = None
        self.DeleteFlag = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ClusterList = None
        self.ClusterId = None
        self.NamespaceResourceType = None
        self.NamespaceType = None


    def _deserialize(self, params):
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceCode = params.get("NamespaceCode")
        self.NamespaceName = params.get("NamespaceName")
        self.NamespaceDesc = params.get("NamespaceDesc")
        self.IsDefault = params.get("IsDefault")
        self.NamespaceStatus = params.get("NamespaceStatus")
        self.DeleteFlag = params.get("DeleteFlag")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("ClusterList") is not None:
            self.ClusterList = []
            for item in params.get("ClusterList"):
                obj = Cluster()
                obj._deserialize(item)
                self.ClusterList.append(obj)
        self.ClusterId = params.get("ClusterId")
        self.NamespaceResourceType = params.get("NamespaceResourceType")
        self.NamespaceType = params.get("NamespaceType")


class OperationInfo(AbstractModel):
    """提供給前端，控制按鈕是否顯示

    """

    def __init__(self):
        """
        :param Init: 初始化按鈕的控制訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Init: :class:`tencentcloud.tsf.v20180326.models.OperationInfoDetail`
        :param AddInstance: 添加實例按鈕的控制訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type AddInstance: :class:`tencentcloud.tsf.v20180326.models.OperationInfoDetail`
        :param Destroy: 銷毀機器的控制訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Destroy: :class:`tencentcloud.tsf.v20180326.models.OperationInfoDetail`
        """
        self.Init = None
        self.AddInstance = None
        self.Destroy = None


    def _deserialize(self, params):
        if params.get("Init") is not None:
            self.Init = OperationInfoDetail()
            self.Init._deserialize(params.get("Init"))
        if params.get("AddInstance") is not None:
            self.AddInstance = OperationInfoDetail()
            self.AddInstance._deserialize(params.get("AddInstance"))
        if params.get("Destroy") is not None:
            self.Destroy = OperationInfoDetail()
            self.Destroy._deserialize(params.get("Destroy"))


class OperationInfoDetail(AbstractModel):
    """提供給前端控制按鈕顯示邏輯的欄位

    """

    def __init__(self):
        """
        :param DisabledReason: 不顯示的原因
注意：此欄位可能返回 null，表示取不到有效值。
        :type DisabledReason: str
        :param Enabled: 該按鈕是否可點擊
注意：此欄位可能返回 null，表示取不到有效值。
        :type Enabled: bool
        :param Supported: 是否顯示該按鈕
注意：此欄位可能返回 null，表示取不到有效值。
        :type Supported: bool
        """
        self.DisabledReason = None
        self.Enabled = None
        self.Supported = None


    def _deserialize(self, params):
        self.DisabledReason = params.get("DisabledReason")
        self.Enabled = params.get("Enabled")
        self.Supported = params.get("Supported")


class PkgInfo(AbstractModel):
    """包訊息

    """

    def __init__(self):
        """
        :param PkgId: 程式包ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type PkgId: str
        :param PkgName: 程式包名
注意：此欄位可能返回 null，表示取不到有效值。
        :type PkgName: str
        :param PkgType: 程式包類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type PkgType: str
        :param PkgVersion: 程式包版本
注意：此欄位可能返回 null，表示取不到有效值。
        :type PkgVersion: str
        :param PkgDesc: 程式包描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type PkgDesc: str
        :param UploadTime: 上傳時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type UploadTime: str
        :param Md5: 程式包MD5
注意：此欄位可能返回 null，表示取不到有效值。
        :type Md5: str
        :param PkgPubStatus: 程式包狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type PkgPubStatus: int
        """
        self.PkgId = None
        self.PkgName = None
        self.PkgType = None
        self.PkgVersion = None
        self.PkgDesc = None
        self.UploadTime = None
        self.Md5 = None
        self.PkgPubStatus = None


    def _deserialize(self, params):
        self.PkgId = params.get("PkgId")
        self.PkgName = params.get("PkgName")
        self.PkgType = params.get("PkgType")
        self.PkgVersion = params.get("PkgVersion")
        self.PkgDesc = params.get("PkgDesc")
        self.UploadTime = params.get("UploadTime")
        self.Md5 = params.get("Md5")
        self.PkgPubStatus = params.get("PkgPubStatus")


class PkgList(AbstractModel):
    """包清單

    """

    def __init__(self):
        """
        :param TotalCount: 程式包總量
        :type TotalCount: int
        :param Content: 程式包訊息清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Content: list of PkgInfo
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = PkgInfo()
                obj._deserialize(item)
                self.Content.append(obj)


class ProtocolPort(AbstractModel):
    """端口對象

    """

    def __init__(self):
        """
        :param Protocol: TCP UDP
        :type Protocol: str
        :param Port: 服務端口
        :type Port: int
        :param TargetPort: 容器端口
        :type TargetPort: int
        :param NodePort: 主機端口
注意：此欄位可能返回 null，表示取不到有效值。
        :type NodePort: int
        """
        self.Protocol = None
        self.Port = None
        self.TargetPort = None
        self.NodePort = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        self.TargetPort = params.get("TargetPort")
        self.NodePort = params.get("NodePort")


class ReleaseConfigRequest(AbstractModel):
    """ReleaseConfig請求參數結構體

    """

    def __init__(self):
        """
        :param ConfigId: 配置ID
        :type ConfigId: str
        :param GroupId: 佈署組ID
        :type GroupId: str
        :param ReleaseDesc: 發布描述
        :type ReleaseDesc: str
        """
        self.ConfigId = None
        self.GroupId = None
        self.ReleaseDesc = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.GroupId = params.get("GroupId")
        self.ReleaseDesc = params.get("ReleaseDesc")


class ReleaseConfigResponse(AbstractModel):
    """ReleaseConfig返回參數結構體

    """

    def __init__(self):
        """
        :param Result: true：發布成功；false：發布失敗
        :type Result: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ReleasePublicConfigRequest(AbstractModel):
    """ReleasePublicConfig請求參數結構體

    """

    def __init__(self):
        """
        :param ConfigId: 配置ID
        :type ConfigId: str
        :param NamespaceId: 命名空間ID
        :type NamespaceId: str
        :param ReleaseDesc: 發布描述
        :type ReleaseDesc: str
        """
        self.ConfigId = None
        self.NamespaceId = None
        self.ReleaseDesc = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.NamespaceId = params.get("NamespaceId")
        self.ReleaseDesc = params.get("ReleaseDesc")


class ReleasePublicConfigResponse(AbstractModel):
    """ReleasePublicConfig返回參數結構體

    """

    def __init__(self):
        """
        :param Result: true：發布成功；false：發布失敗
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class RemoveInstancesRequest(AbstractModel):
    """RemoveInstances請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群 ID
        :type ClusterId: str
        :param InstanceIdList: 雲主機 ID 清單
        :type InstanceIdList: list of str
        """
        self.ClusterId = None
        self.InstanceIdList = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIdList = params.get("InstanceIdList")


class RemoveInstancesResponse(AbstractModel):
    """RemoveInstances返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 集群移除機器是否成功
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class RevocationConfigRequest(AbstractModel):
    """RevocationConfig請求參數結構體

    """

    def __init__(self):
        """
        :param ConfigReleaseId: 配置項發布ID
        :type ConfigReleaseId: str
        """
        self.ConfigReleaseId = None


    def _deserialize(self, params):
        self.ConfigReleaseId = params.get("ConfigReleaseId")


class RevocationConfigResponse(AbstractModel):
    """RevocationConfig返回參數結構體

    """

    def __init__(self):
        """
        :param Result: true：回滾成功；false：回滾失敗
        :type Result: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class RevocationPublicConfigRequest(AbstractModel):
    """RevocationPublicConfig請求參數結構體

    """

    def __init__(self):
        """
        :param ConfigReleaseId: 配置項發布ID
        :type ConfigReleaseId: str
        """
        self.ConfigReleaseId = None


    def _deserialize(self, params):
        self.ConfigReleaseId = params.get("ConfigReleaseId")


class RevocationPublicConfigResponse(AbstractModel):
    """RevocationPublicConfig返回參數結構體

    """

    def __init__(self):
        """
        :param Result: true：撤銷成功；false：撤銷失敗
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class RollbackConfigRequest(AbstractModel):
    """RollbackConfig請求參數結構體

    """

    def __init__(self):
        """
        :param ConfigReleaseLogId: 配置項發布曆史ID
        :type ConfigReleaseLogId: str
        :param ReleaseDesc: 回滾描述
        :type ReleaseDesc: str
        """
        self.ConfigReleaseLogId = None
        self.ReleaseDesc = None


    def _deserialize(self, params):
        self.ConfigReleaseLogId = params.get("ConfigReleaseLogId")
        self.ReleaseDesc = params.get("ReleaseDesc")


class RollbackConfigResponse(AbstractModel):
    """RollbackConfig返回參數結構體

    """

    def __init__(self):
        """
        :param Result: true：回滾成功；false：回滾失敗
        :type Result: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ServerlessGroup(AbstractModel):
    """Serverless佈署組訊息

    """

    def __init__(self):
        """
        :param GroupId: 佈署組ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param GroupName: 分組名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param CreateTime: 創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param Status: 服務狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: str
        :param PkgId: 程式包ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type PkgId: str
        :param PkgName: 程式包名
注意：此欄位可能返回 null，表示取不到有效值。
        :type PkgName: str
        :param ClusterId: 集群id
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param ClusterName: 集群名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param NamespaceId: 命名空間id
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param NamespaceName: 命名空間名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        :param VpcId: vpc ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param SubnetId: vpc 子網ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param PkgVersion: 程式包版本
注意：此欄位可能返回 null，表示取不到有效值。
        :type PkgVersion: str
        :param Memory: 所需實例内存大小
注意：此欄位可能返回 null，表示取不到有效值。
        :type Memory: str
        :param InstanceRequest: 要求最小實例數
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceRequest: int
        :param StartupParameters: 佈署組啓動參數
注意：此欄位可能返回 null，表示取不到有效值。
        :type StartupParameters: str
        :param ApplicationId: 應用ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param InstanceCount: 佈署組實例數
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceCount: int
        :param ApplicationName: 應用名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationName: list of str
        """
        self.GroupId = None
        self.GroupName = None
        self.CreateTime = None
        self.Status = None
        self.PkgId = None
        self.PkgName = None
        self.ClusterId = None
        self.ClusterName = None
        self.NamespaceId = None
        self.NamespaceName = None
        self.VpcId = None
        self.SubnetId = None
        self.PkgVersion = None
        self.Memory = None
        self.InstanceRequest = None
        self.StartupParameters = None
        self.ApplicationId = None
        self.InstanceCount = None
        self.ApplicationName = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")
        self.PkgId = params.get("PkgId")
        self.PkgName = params.get("PkgName")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.PkgVersion = params.get("PkgVersion")
        self.Memory = params.get("Memory")
        self.InstanceRequest = params.get("InstanceRequest")
        self.StartupParameters = params.get("StartupParameters")
        self.ApplicationId = params.get("ApplicationId")
        self.InstanceCount = params.get("InstanceCount")
        self.ApplicationName = params.get("ApplicationName")


class ServerlessGroupPage(AbstractModel):
    """ServerlessGroup 翻頁對象

    """

    def __init__(self):
        """
        :param TotalCount: 總記錄數
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 清單訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Content: list of ServerlessGroup
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = ServerlessGroup()
                obj._deserialize(item)
                self.Content.append(obj)


class ShrinkGroupRequest(AbstractModel):
    """ShrinkGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 佈署組ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class ShrinkGroupResponse(AbstractModel):
    """ShrinkGroup返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 任務ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TaskId`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TaskId()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ShrinkInstancesRequest(AbstractModel):
    """ShrinkInstances請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 佈署組ID
        :type GroupId: str
        :param InstanceIdList: 下線機器實例ID清單
        :type InstanceIdList: list of str
        """
        self.GroupId = None
        self.InstanceIdList = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.InstanceIdList = params.get("InstanceIdList")


class ShrinkInstancesResponse(AbstractModel):
    """ShrinkInstances返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 任務ID
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TaskId`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TaskId()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class SimpleApplication(AbstractModel):
    """簡單應用

    """

    def __init__(self):
        """
        :param ApplicationId: 應用ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param ApplicationName: 應用名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param ApplicationType: 應用類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationType: str
        :param MicroserviceType: 應用微服務類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type MicroserviceType: str
        :param ApplicationDesc: ApplicationDesc
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationDesc: str
        :param ProgLang: ProgLang
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProgLang: str
        :param ApplicationResourceType: ApplicationResourceType
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationResourceType: str
        :param CreateTime: CreateTime
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: UpdateTime
注意：此欄位可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param ApigatewayServiceId: ApigatewayServiceId
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApigatewayServiceId: str
        :param ApplicationRuntimeType: ApplicationRuntimeType
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationRuntimeType: str
        """
        self.ApplicationId = None
        self.ApplicationName = None
        self.ApplicationType = None
        self.MicroserviceType = None
        self.ApplicationDesc = None
        self.ProgLang = None
        self.ApplicationResourceType = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ApigatewayServiceId = None
        self.ApplicationRuntimeType = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.ApplicationType = params.get("ApplicationType")
        self.MicroserviceType = params.get("MicroserviceType")
        self.ApplicationDesc = params.get("ApplicationDesc")
        self.ProgLang = params.get("ProgLang")
        self.ApplicationResourceType = params.get("ApplicationResourceType")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ApigatewayServiceId = params.get("ApigatewayServiceId")
        self.ApplicationRuntimeType = params.get("ApplicationRuntimeType")


class SimpleGroup(AbstractModel):
    """佈署組

    """

    def __init__(self):
        """
        :param GroupId: 佈署組ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param GroupName: 佈署組名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param ApplicationId: 應用ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param ApplicationName: 應用名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param ApplicationType: 應用類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationType: str
        :param ClusterId: 集群ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param ClusterName: 集群名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param ClusterType: 集群類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterType: str
        :param NamespaceId: 命名空間ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param NamespaceName: 命名空間名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        :param StartupParameters: 啓動參數
注意：此欄位可能返回 null，表示取不到有效值。
        :type StartupParameters: str
        :param GroupResourceType: 佈署組資源類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupResourceType: str
        :param AppMicroServiceType: 應用微服務類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type AppMicroServiceType: str
        """
        self.GroupId = None
        self.GroupName = None
        self.ApplicationId = None
        self.ApplicationName = None
        self.ApplicationType = None
        self.ClusterId = None
        self.ClusterName = None
        self.ClusterType = None
        self.NamespaceId = None
        self.NamespaceName = None
        self.StartupParameters = None
        self.GroupResourceType = None
        self.AppMicroServiceType = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.ApplicationType = params.get("ApplicationType")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.ClusterType = params.get("ClusterType")
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")
        self.StartupParameters = params.get("StartupParameters")
        self.GroupResourceType = params.get("GroupResourceType")
        self.AppMicroServiceType = params.get("AppMicroServiceType")


class StartContainerGroupRequest(AbstractModel):
    """StartContainerGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 佈署組ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class StartContainerGroupResponse(AbstractModel):
    """StartContainerGroup返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 啓動操作是否成功。
true：啓動成功
false：啓動失敗
        :type Result: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class StartGroupRequest(AbstractModel):
    """StartGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 佈署組ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class StartGroupResponse(AbstractModel):
    """StartGroup返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 任務ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TaskId`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TaskId()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class StopContainerGroupRequest(AbstractModel):
    """StopContainerGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 佈署組ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class StopContainerGroupResponse(AbstractModel):
    """StopContainerGroup返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 停止操作是否成功。
true：停止成功
flase：停止失敗
        :type Result: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class StopGroupRequest(AbstractModel):
    """StopGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 佈署組ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class StopGroupResponse(AbstractModel):
    """StopGroup返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 任務ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tsf.v20180326.models.TaskId`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TaskId()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class TaskId(AbstractModel):
    """任務id

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class TsfPageApplication(AbstractModel):
    """應用分頁訊息

    """

    def __init__(self):
        """
        :param TotalCount: 應用總數目
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 應用訊息清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Content: list of ApplicationForPage
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = ApplicationForPage()
                obj._deserialize(item)
                self.Content.append(obj)


class TsfPageCluster(AbstractModel):
    """Tsf分頁集群對象

    """

    def __init__(self):
        """
        :param TotalCount: 總條數
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 集群清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Content: list of Cluster
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = Cluster()
                obj._deserialize(item)
                self.Content.append(obj)


class TsfPageConfig(AbstractModel):
    """TsfPage<Config>

    """

    def __init__(self):
        """
        :param TotalCount: TsfPageConfig
        :type TotalCount: int
        :param Content: 配置項清單
        :type Content: list of Config
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = Config()
                obj._deserialize(item)
                self.Content.append(obj)


class TsfPageConfigRelease(AbstractModel):
    """TSF配置項發布訊息分頁對象

    """

    def __init__(self):
        """
        :param TotalCount: 總條數
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 配置項發布訊息數組
注意：此欄位可能返回 null，表示取不到有效值。
        :type Content: list of ConfigRelease
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = ConfigRelease()
                obj._deserialize(item)
                self.Content.append(obj)


class TsfPageConfigReleaseLog(AbstractModel):
    """TSF配置項發布日志分頁對象

    """

    def __init__(self):
        """
        :param TotalCount: 總條數
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 配置項發布日志數組
注意：此欄位可能返回 null，表示取不到有效值。
        :type Content: list of ConfigReleaseLog
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = ConfigReleaseLog()
                obj._deserialize(item)
                self.Content.append(obj)


class TsfPageInstance(AbstractModel):
    """TSF機器實例分頁對象

    """

    def __init__(self):
        """
        :param TotalCount: 機器實例總數目
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 機器實例清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Content: list of Instance
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = Instance()
                obj._deserialize(item)
                self.Content.append(obj)


class TsfPageMicroservice(AbstractModel):
    """微服務清單訊息

    """

    def __init__(self):
        """
        :param TotalCount: 微服務總數目
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 微服務清單訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Content: list of Microservice
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = Microservice()
                obj._deserialize(item)
                self.Content.append(obj)


class TsfPageMsInstance(AbstractModel):
    """微服務實例的分頁内容

    """

    def __init__(self):
        """
        :param TotalCount: 微服務實例總數目
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 微服務實例清單内容
注意：此欄位可能返回 null，表示取不到有效值。
        :type Content: list of MsInstance
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = MsInstance()
                obj._deserialize(item)
                self.Content.append(obj)


class TsfPageNamespace(AbstractModel):
    """Tsf命名空間分頁對象

    """

    def __init__(self):
        """
        :param TotalCount: 命名空間總條數
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 命名空間清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Content: list of Namespace
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = Namespace()
                obj._deserialize(item)
                self.Content.append(obj)


class TsfPageSimpleApplication(AbstractModel):
    """TSF分頁簡單應用對象

    """

    def __init__(self):
        """
        :param TotalCount: 總條數
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 簡單應用清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Content: list of SimpleApplication
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = SimpleApplication()
                obj._deserialize(item)
                self.Content.append(obj)


class TsfPageSimpleGroup(AbstractModel):
    """TSF簡單佈署組分頁清單

    """

    def __init__(self):
        """
        :param TotalCount: 總條數
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 簡單佈署組清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Content: list of SimpleGroup
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = SimpleGroup()
                obj._deserialize(item)
                self.Content.append(obj)


class TsfPageVmGroup(AbstractModel):
    """清單中佈署組分頁訊息

    """

    def __init__(self):
        """
        :param TotalCount: 虛拟機佈署組總數目
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Content: 虛拟機佈署組清單訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Content: list of VmGroupSimple
        """
        self.TotalCount = None
        self.Content = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = VmGroupSimple()
                obj._deserialize(item)
                self.Content.append(obj)


class VmGroup(AbstractModel):
    """虛拟機佈署組訊息

    """

    def __init__(self):
        """
        :param GroupId: 佈署組ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param GroupName: 佈署組名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param GroupStatus: 佈署組狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupStatus: str
        :param PackageId: 程式包ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type PackageId: str
        :param PackageName: 程式包名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type PackageName: str
        :param PackageVersion: 程式包版本号
注意：此欄位可能返回 null，表示取不到有效值。
        :type PackageVersion: str
        :param ClusterId: 集群ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param ClusterName: 集群名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param NamespaceId: 命名空間ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param NamespaceName: 命名空間名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        :param ApplicationId: 應用ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param ApplicationName: 應用名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param InstanceCount: 佈署組機器數目
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceCount: int
        :param RunInstanceCount: 佈署組運作中機器數目
注意：此欄位可能返回 null，表示取不到有效值。
        :type RunInstanceCount: int
        :param StartupParameters: 佈署組啓動參數訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type StartupParameters: str
        :param CreateTime: 佈署組創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 佈署組更新時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param OffInstanceCount: 佈署組停止機器數目
注意：此欄位可能返回 null，表示取不到有效值。
        :type OffInstanceCount: int
        :param GroupDesc: 佈署組描述訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupDesc: str
        :param MicroserviceType: 微服務類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type MicroserviceType: str
        :param ApplicationType: 應用類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationType: str
        :param GroupResourceType: 佈署組資源類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupResourceType: str
        :param UpdatedTime: 佈署組更新時間戳
注意：此欄位可能返回 null，表示取不到有效值。
        :type UpdatedTime: int
        """
        self.GroupId = None
        self.GroupName = None
        self.GroupStatus = None
        self.PackageId = None
        self.PackageName = None
        self.PackageVersion = None
        self.ClusterId = None
        self.ClusterName = None
        self.NamespaceId = None
        self.NamespaceName = None
        self.ApplicationId = None
        self.ApplicationName = None
        self.InstanceCount = None
        self.RunInstanceCount = None
        self.StartupParameters = None
        self.CreateTime = None
        self.UpdateTime = None
        self.OffInstanceCount = None
        self.GroupDesc = None
        self.MicroserviceType = None
        self.ApplicationType = None
        self.GroupResourceType = None
        self.UpdatedTime = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.GroupStatus = params.get("GroupStatus")
        self.PackageId = params.get("PackageId")
        self.PackageName = params.get("PackageName")
        self.PackageVersion = params.get("PackageVersion")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.NamespaceId = params.get("NamespaceId")
        self.NamespaceName = params.get("NamespaceName")
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.InstanceCount = params.get("InstanceCount")
        self.RunInstanceCount = params.get("RunInstanceCount")
        self.StartupParameters = params.get("StartupParameters")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.OffInstanceCount = params.get("OffInstanceCount")
        self.GroupDesc = params.get("GroupDesc")
        self.MicroserviceType = params.get("MicroserviceType")
        self.ApplicationType = params.get("ApplicationType")
        self.GroupResourceType = params.get("GroupResourceType")
        self.UpdatedTime = params.get("UpdatedTime")


class VmGroupSimple(AbstractModel):
    """虛拟機佈署組清單簡要欄位

    """

    def __init__(self):
        """
        :param GroupId: 佈署組ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param GroupName: 佈署組名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param ApplicationType: 應用類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationType: str
        :param GroupDesc: 佈署組描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupDesc: str
        :param UpdateTime: 佈署組更新時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param ClusterId: 集群ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param StartupParameters: 佈署組啓動參數
注意：此欄位可能返回 null，表示取不到有效值。
        :type StartupParameters: str
        :param NamespaceId: 命名空間ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceId: str
        :param CreateTime: 佈署組創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param ClusterName: 集群名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param ApplicationId: 應用ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationId: str
        :param ApplicationName: 應用名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApplicationName: str
        :param NamespaceName: 命名空間名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type NamespaceName: str
        :param MicroserviceType: 應用微服務類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type MicroserviceType: str
        :param GroupResourceType: 佈署組資源類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupResourceType: str
        :param UpdatedTime: 佈署組更新時間戳
注意：此欄位可能返回 null，表示取不到有效值。
        :type UpdatedTime: int
        """
        self.GroupId = None
        self.GroupName = None
        self.ApplicationType = None
        self.GroupDesc = None
        self.UpdateTime = None
        self.ClusterId = None
        self.StartupParameters = None
        self.NamespaceId = None
        self.CreateTime = None
        self.ClusterName = None
        self.ApplicationId = None
        self.ApplicationName = None
        self.NamespaceName = None
        self.MicroserviceType = None
        self.GroupResourceType = None
        self.UpdatedTime = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.ApplicationType = params.get("ApplicationType")
        self.GroupDesc = params.get("GroupDesc")
        self.UpdateTime = params.get("UpdateTime")
        self.ClusterId = params.get("ClusterId")
        self.StartupParameters = params.get("StartupParameters")
        self.NamespaceId = params.get("NamespaceId")
        self.CreateTime = params.get("CreateTime")
        self.ClusterName = params.get("ClusterName")
        self.ApplicationId = params.get("ApplicationId")
        self.ApplicationName = params.get("ApplicationName")
        self.NamespaceName = params.get("NamespaceName")
        self.MicroserviceType = params.get("MicroserviceType")
        self.GroupResourceType = params.get("GroupResourceType")
        self.UpdatedTime = params.get("UpdatedTime")