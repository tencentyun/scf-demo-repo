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


class AddExistedInstancesRequest(AbstractModel):
    """AddExistedInstances請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceIds: 實例清單
        :type InstanceIds: list of str
        :param InstanceAdvancedSettings: 實例額外需要設置參數訊息
        :type InstanceAdvancedSettings: :class:`taifucloudcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param EnhancedService: 增強服務。通過該參數可以指定是否開啓雲安全、雲監控等服務。若不指定該參數，則預設開啓雲監控、雲安全服務。
        :type EnhancedService: :class:`taifucloudcloud.tke.v20180525.models.EnhancedService`
        :param LoginSettings: 節點登入訊息（目前僅支援使用Password或者單個KeyIds）
        :type LoginSettings: :class:`taifucloudcloud.tke.v20180525.models.LoginSettings`
        :param SecurityGroupIds: 實例所屬安全組。該參數可以通過調用 DescribeSecurityGroups 的返回值中的sgId欄位來獲取。若不指定該參數，則綁定預設安全組。（目前僅支援設置單個sgId）
        :type SecurityGroupIds: list of str
        :param HostName: 重灌系統時，可以指定修改實例的HostName(集群爲HostName模式時，此參數必傳，規則名稱除不支援大寫字元外與[CVM創建實例](https://cloud.taifucloud.com/document/product/213/15730)介面HostName一緻)
        :type HostName: str
        """
        self.ClusterId = None
        self.InstanceIds = None
        self.InstanceAdvancedSettings = None
        self.EnhancedService = None
        self.LoginSettings = None
        self.SecurityGroupIds = None
        self.HostName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIds = params.get("InstanceIds")
        if params.get("InstanceAdvancedSettings") is not None:
            self.InstanceAdvancedSettings = InstanceAdvancedSettings()
            self.InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.HostName = params.get("HostName")


class AddExistedInstancesResponse(AbstractModel):
    """AddExistedInstances返回參數結構體

    """

    def __init__(self):
        """
        :param FailedInstanceIds: 失敗的節點ID
        :type FailedInstanceIds: list of str
        :param SuccInstanceIds: 成功的節點ID
        :type SuccInstanceIds: list of str
        :param TimeoutInstanceIds: 超時未返回出來節點的ID(可能失敗，也可能成功)
        :type TimeoutInstanceIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FailedInstanceIds = None
        self.SuccInstanceIds = None
        self.TimeoutInstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FailedInstanceIds = params.get("FailedInstanceIds")
        self.SuccInstanceIds = params.get("SuccInstanceIds")
        self.TimeoutInstanceIds = params.get("TimeoutInstanceIds")
        self.RequestId = params.get("RequestId")


class AutoScalingGroupRange(AbstractModel):
    """集群關聯的伸縮組最大實例數最小值實例數

    """

    def __init__(self):
        """
        :param MinSize: 伸縮組最小實例數
        :type MinSize: int
        :param MaxSize: 伸縮組最大實例數
        :type MaxSize: int
        """
        self.MinSize = None
        self.MaxSize = None


    def _deserialize(self, params):
        self.MinSize = params.get("MinSize")
        self.MaxSize = params.get("MaxSize")


class Cluster(AbstractModel):
    """集群訊息結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ClusterName: 集群名稱
        :type ClusterName: str
        :param ClusterDescription: 集群描述
        :type ClusterDescription: str
        :param ClusterVersion: 集群版本（預設值爲1.10.5）
        :type ClusterVersion: str
        :param ClusterOs: 集群系統。centos7.2x86_64 或者 ubuntu16.04.1 LTSx86_64，預設取值爲ubuntu16.04.1 LTSx86_64
        :type ClusterOs: str
        :param ClusterType: 集群類型，托管集群：MANAGED_CLUSTER，獨立集群：INDEPENDENT_CLUSTER。
        :type ClusterType: str
        :param ClusterNetworkSettings: 集群網絡相關參數
        :type ClusterNetworkSettings: :class:`taifucloudcloud.tke.v20180525.models.ClusterNetworkSettings`
        :param ClusterNodeNum: 集群當前node數量
        :type ClusterNodeNum: int
        :param ProjectId: 集群所屬的項目ID
        :type ProjectId: int
        :param TagSpecification: 標簽描述清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagSpecification: list of TagSpecification
        :param ClusterStatus: 集群狀态 (Running 運作中  Creating 創建中 Abnormal 異常  )
        :type ClusterStatus: str
        :param Property: 集群屬性(包括集群不同屬性的MAP，屬性欄位包括NodeNameType (lan-ip模式和hostname 模式，預設無lan-ip模式))
注意：此欄位可能返回 null，表示取不到有效值。
        :type Property: str
        :param ClusterMaterNodeNum: 集群當前master數量
        :type ClusterMaterNodeNum: int
        :param ImageId: 集群使用映像id
注意：此欄位可能返回 null，表示取不到有效值。
        :type ImageId: str
        :param OsCustomizeType: OsCustomizeType
注意：此欄位可能返回 null，表示取不到有效值。
        :type OsCustomizeType: str
        :param ContainerRuntime: 集群運作環境docker或container
注意：此欄位可能返回 null，表示取不到有效值。
        :type ContainerRuntime: str
        :param CreatedTime: 創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        """
        self.ClusterId = None
        self.ClusterName = None
        self.ClusterDescription = None
        self.ClusterVersion = None
        self.ClusterOs = None
        self.ClusterType = None
        self.ClusterNetworkSettings = None
        self.ClusterNodeNum = None
        self.ProjectId = None
        self.TagSpecification = None
        self.ClusterStatus = None
        self.Property = None
        self.ClusterMaterNodeNum = None
        self.ImageId = None
        self.OsCustomizeType = None
        self.ContainerRuntime = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.ClusterDescription = params.get("ClusterDescription")
        self.ClusterVersion = params.get("ClusterVersion")
        self.ClusterOs = params.get("ClusterOs")
        self.ClusterType = params.get("ClusterType")
        if params.get("ClusterNetworkSettings") is not None:
            self.ClusterNetworkSettings = ClusterNetworkSettings()
            self.ClusterNetworkSettings._deserialize(params.get("ClusterNetworkSettings"))
        self.ClusterNodeNum = params.get("ClusterNodeNum")
        self.ProjectId = params.get("ProjectId")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        self.ClusterStatus = params.get("ClusterStatus")
        self.Property = params.get("Property")
        self.ClusterMaterNodeNum = params.get("ClusterMaterNodeNum")
        self.ImageId = params.get("ImageId")
        self.OsCustomizeType = params.get("OsCustomizeType")
        self.ContainerRuntime = params.get("ContainerRuntime")
        self.CreatedTime = params.get("CreatedTime")


class ClusterAdvancedSettings(AbstractModel):
    """集群高級配置

    """

    def __init__(self):
        """
        :param IPVS: 是否啓用IPVS
        :type IPVS: bool
        :param AsEnabled: 是否啓用集群節點自動擴縮容(創建集群流程不支援開啓此功能)
        :type AsEnabled: bool
        :param ContainerRuntime: 集群使用的runtime類型，包括"docker"和"containerd"兩種類型，預設爲"docker"
        :type ContainerRuntime: str
        :param NodeNameType: 集群中節點NodeName類型（包括 hostname,lan-ip兩種形式，預設爲lan-ip。如果開啓了hostname模式，創建節點時需要設置HostName參數，並且InstanceName需要和HostName一緻）
        :type NodeNameType: str
        :param ExtraArgs: 集群自定義參數
        :type ExtraArgs: :class:`taifucloudcloud.tke.v20180525.models.ClusterExtraArgs`
        :param NetworkType: 集群網絡類型（包括GR(全局路由)和VPC-CNI兩種模式，預設爲GR。
        :type NetworkType: str
        :param IsNonStaticIpMode: 集群VPC-CNI模式是否爲非固定IP，預設: FALSE 固定IP。
        :type IsNonStaticIpMode: bool
        """
        self.IPVS = None
        self.AsEnabled = None
        self.ContainerRuntime = None
        self.NodeNameType = None
        self.ExtraArgs = None
        self.NetworkType = None
        self.IsNonStaticIpMode = None


    def _deserialize(self, params):
        self.IPVS = params.get("IPVS")
        self.AsEnabled = params.get("AsEnabled")
        self.ContainerRuntime = params.get("ContainerRuntime")
        self.NodeNameType = params.get("NodeNameType")
        if params.get("ExtraArgs") is not None:
            self.ExtraArgs = ClusterExtraArgs()
            self.ExtraArgs._deserialize(params.get("ExtraArgs"))
        self.NetworkType = params.get("NetworkType")
        self.IsNonStaticIpMode = params.get("IsNonStaticIpMode")


class ClusterAsGroup(AbstractModel):
    """集群關聯的伸縮組訊息

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸縮組ID
        :type AutoScalingGroupId: str
        :param Status: 伸縮組狀态(開啓 enabled 開啓中 enabling 關閉 disabled 關閉中 disabling 更新中 updating 删除中 deleting 開啓縮容中 scaleDownEnabling 關閉縮容中 scaleDownDisabling)
        :type Status: str
        :param IsUnschedulable: 節點是否設置成不可調度
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsUnschedulable: bool
        :param Labels: 伸縮組的label清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Labels: list of Label
        """
        self.AutoScalingGroupId = None
        self.Status = None
        self.IsUnschedulable = None
        self.Labels = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.Status = params.get("Status")
        self.IsUnschedulable = params.get("IsUnschedulable")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self.Labels.append(obj)


class ClusterAsGroupAttribute(AbstractModel):
    """集群伸縮組屬性

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸縮組ID
        :type AutoScalingGroupId: str
        :param AutoScalingGroupEnabled: 是否開啓
        :type AutoScalingGroupEnabled: bool
        :param AutoScalingGroupRange: 伸縮組最大最小實例數
        :type AutoScalingGroupRange: :class:`taifucloudcloud.tke.v20180525.models.AutoScalingGroupRange`
        """
        self.AutoScalingGroupId = None
        self.AutoScalingGroupEnabled = None
        self.AutoScalingGroupRange = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.AutoScalingGroupEnabled = params.get("AutoScalingGroupEnabled")
        if params.get("AutoScalingGroupRange") is not None:
            self.AutoScalingGroupRange = AutoScalingGroupRange()
            self.AutoScalingGroupRange._deserialize(params.get("AutoScalingGroupRange"))


class ClusterAsGroupOption(AbstractModel):
    """集群彈性伸縮配置

    """

    def __init__(self):
        """
        :param IsScaleDownEnabled: 是否開啓縮容
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsScaleDownEnabled: bool
        :param Expander: 多伸縮組情況下擴容選擇算法(random 随機選擇，most-pods 最多類型的Pod least-waste 最少的資源浪費，預設爲random)
注意：此欄位可能返回 null，表示取不到有效值。
        :type Expander: str
        :param MaxEmptyBulkDelete: 最大並發縮容數
注意：此欄位可能返回 null，表示取不到有效值。
        :type MaxEmptyBulkDelete: int
        :param ScaleDownDelay: 集群擴容後多少分鍾開始判斷縮容（預設爲10分鍾）
注意：此欄位可能返回 null，表示取不到有效值。
        :type ScaleDownDelay: int
        :param ScaleDownUnneededTime: 節點連續空閑多少分鍾後被縮容（預設爲 10分鍾）
注意：此欄位可能返回 null，表示取不到有效值。
        :type ScaleDownUnneededTime: int
        :param ScaleDownUtilizationThreshold: 節點資源使用量低於多少(百分比)時認爲空閑(預設: 50(百分比))
注意：此欄位可能返回 null，表示取不到有效值。
        :type ScaleDownUtilizationThreshold: int
        :param SkipNodesWithLocalStorage: 含有本地儲存Pod的節點是否不縮容(預設： FALSE)
注意：此欄位可能返回 null，表示取不到有效值。
        :type SkipNodesWithLocalStorage: bool
        :param SkipNodesWithSystemPods: 含有kube-system namespace下非DaemonSet管理的Pod的節點是否不縮容 (預設： FALSE)
注意：此欄位可能返回 null，表示取不到有效值。
        :type SkipNodesWithSystemPods: bool
        :param IgnoreDaemonSetsUtilization: 計算資源使用量時是否預設忽略DaemonSet的實例(預設值: False，不忽略)
注意：此欄位可能返回 null，表示取不到有效值。
        :type IgnoreDaemonSetsUtilization: bool
        """
        self.IsScaleDownEnabled = None
        self.Expander = None
        self.MaxEmptyBulkDelete = None
        self.ScaleDownDelay = None
        self.ScaleDownUnneededTime = None
        self.ScaleDownUtilizationThreshold = None
        self.SkipNodesWithLocalStorage = None
        self.SkipNodesWithSystemPods = None
        self.IgnoreDaemonSetsUtilization = None


    def _deserialize(self, params):
        self.IsScaleDownEnabled = params.get("IsScaleDownEnabled")
        self.Expander = params.get("Expander")
        self.MaxEmptyBulkDelete = params.get("MaxEmptyBulkDelete")
        self.ScaleDownDelay = params.get("ScaleDownDelay")
        self.ScaleDownUnneededTime = params.get("ScaleDownUnneededTime")
        self.ScaleDownUtilizationThreshold = params.get("ScaleDownUtilizationThreshold")
        self.SkipNodesWithLocalStorage = params.get("SkipNodesWithLocalStorage")
        self.SkipNodesWithSystemPods = params.get("SkipNodesWithSystemPods")
        self.IgnoreDaemonSetsUtilization = params.get("IgnoreDaemonSetsUtilization")


class ClusterBasicSettings(AbstractModel):
    """描述集群的基本配置訊息

    """

    def __init__(self):
        """
        :param ClusterOs: 集群系統。centos7.2x86_64 或者 ubuntu16.04.1 LTSx86_64，預設取值爲ubuntu16.04.1 LTSx86_64
        :type ClusterOs: str
        :param ClusterVersion: 集群版本,預設值爲1.10.5
        :type ClusterVersion: str
        :param ClusterName: 集群名稱
        :type ClusterName: str
        :param ClusterDescription: 集群描述
        :type ClusterDescription: str
        :param VpcId: 私有網絡ID，形如vpc-xxx。創建托管空集群時必傳。
        :type VpcId: str
        :param ProjectId: 集群内新增資源所屬項目ID。
        :type ProjectId: int
        :param TagSpecification: 標簽描述清單。通過指定該參數可以同時綁定標簽到相應的資源實例，當前僅支援綁定標簽到集群實例。
        :type TagSpecification: list of TagSpecification
        :param OsCustomizeType: 容器的映像版本，"DOCKER_CUSTOMIZE"(容器定制版),"GENERAL"(普通版本，預設值)
        :type OsCustomizeType: str
        :param NeedWorkSecurityGroup: 是否開啓節點的預設安全組(預設: 否，Aphla特性)
        :type NeedWorkSecurityGroup: bool
        """
        self.ClusterOs = None
        self.ClusterVersion = None
        self.ClusterName = None
        self.ClusterDescription = None
        self.VpcId = None
        self.ProjectId = None
        self.TagSpecification = None
        self.OsCustomizeType = None
        self.NeedWorkSecurityGroup = None


    def _deserialize(self, params):
        self.ClusterOs = params.get("ClusterOs")
        self.ClusterVersion = params.get("ClusterVersion")
        self.ClusterName = params.get("ClusterName")
        self.ClusterDescription = params.get("ClusterDescription")
        self.VpcId = params.get("VpcId")
        self.ProjectId = params.get("ProjectId")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        self.OsCustomizeType = params.get("OsCustomizeType")
        self.NeedWorkSecurityGroup = params.get("NeedWorkSecurityGroup")


class ClusterCIDRSettings(AbstractModel):
    """集群容器網絡相關參數

    """

    def __init__(self):
        """
        :param ClusterCIDR: 用於分配集群容器和服務 IP 的 CIDR，不得與 VPC CIDR 沖突，也不得與同 VPC 内其他集群 CIDR 沖突。且網段範圍必須在内網網段内，例如:10.1.0.0/14, 192.168.0.1/18,172.16.0.0/16。
        :type ClusterCIDR: str
        :param IgnoreClusterCIDRConflict: 是否忽略 ClusterCIDR 沖突錯誤, 預設不忽略
        :type IgnoreClusterCIDRConflict: bool
        :param MaxNodePodNum: 集群中每個Node上最大的Pod數量。取值範圍4～256。不爲2的幂值時會向上取最接近的2的幂值。
        :type MaxNodePodNum: int
        :param MaxClusterServiceNum: 集群最大的service數量。取值範圍32～32768，不爲2的幂值時會向上取最接近的2的幂值。
        :type MaxClusterServiceNum: int
        :param ServiceCIDR: 用於分配集群服務 IP 的 CIDR，不得與 VPC CIDR 沖突，也不得與同 VPC 内其他集群 CIDR 沖突。且網段範圍必須在内網網段内，例如:10.1.0.0/14, 192.168.0.1/18,172.16.0.0/16。
        :type ServiceCIDR: str
        :param EniSubnetIds: VPC-CNI網絡模式下，彈性網卡的子網Id。
        :type EniSubnetIds: list of str
        :param ClaimExpiredSeconds: VPC-CNI網絡模式下，彈性網卡IP的回收時間，取值範圍[300,15768000)
        :type ClaimExpiredSeconds: int
        """
        self.ClusterCIDR = None
        self.IgnoreClusterCIDRConflict = None
        self.MaxNodePodNum = None
        self.MaxClusterServiceNum = None
        self.ServiceCIDR = None
        self.EniSubnetIds = None
        self.ClaimExpiredSeconds = None


    def _deserialize(self, params):
        self.ClusterCIDR = params.get("ClusterCIDR")
        self.IgnoreClusterCIDRConflict = params.get("IgnoreClusterCIDRConflict")
        self.MaxNodePodNum = params.get("MaxNodePodNum")
        self.MaxClusterServiceNum = params.get("MaxClusterServiceNum")
        self.ServiceCIDR = params.get("ServiceCIDR")
        self.EniSubnetIds = params.get("EniSubnetIds")
        self.ClaimExpiredSeconds = params.get("ClaimExpiredSeconds")


class ClusterExtraArgs(AbstractModel):
    """集群master自定義參數

    """

    def __init__(self):
        """
        :param KubeAPIServer: kube-apiserver自定義參數
注意：此欄位可能返回 null，表示取不到有效值。
        :type KubeAPIServer: list of str
        :param KubeControllerManager: kube-controller-manager自定義參數
注意：此欄位可能返回 null，表示取不到有效值。
        :type KubeControllerManager: list of str
        :param KubeScheduler: kube-scheduler自定義參數
注意：此欄位可能返回 null，表示取不到有效值。
        :type KubeScheduler: list of str
        """
        self.KubeAPIServer = None
        self.KubeControllerManager = None
        self.KubeScheduler = None


    def _deserialize(self, params):
        self.KubeAPIServer = params.get("KubeAPIServer")
        self.KubeControllerManager = params.get("KubeControllerManager")
        self.KubeScheduler = params.get("KubeScheduler")


class ClusterNetworkSettings(AbstractModel):
    """集群網絡相關的參數

    """

    def __init__(self):
        """
        :param ClusterCIDR: 用於分配集群容器和服務 IP 的 CIDR，不得與 VPC CIDR 沖突，也不得與同 VPC 内其他集群 CIDR 沖突
        :type ClusterCIDR: str
        :param IgnoreClusterCIDRConflict: 是否忽略 ClusterCIDR 沖突錯誤, 預設不忽略
        :type IgnoreClusterCIDRConflict: bool
        :param MaxNodePodNum: 集群中每個Node上最大的Pod數量(預設爲256)
        :type MaxNodePodNum: int
        :param MaxClusterServiceNum: 集群最大的service數量(預設爲256)
        :type MaxClusterServiceNum: int
        :param Ipvs: 是否啓用IPVS(預設不開啓)
        :type Ipvs: bool
        :param VpcId: 集群的VPCID（如果創建空集群，爲必傳值，否則自動設置爲和集群的節點保持一緻）
        :type VpcId: str
        :param Cni: 網絡插件是否啓用CNI(預設開啓)
        :type Cni: bool
        """
        self.ClusterCIDR = None
        self.IgnoreClusterCIDRConflict = None
        self.MaxNodePodNum = None
        self.MaxClusterServiceNum = None
        self.Ipvs = None
        self.VpcId = None
        self.Cni = None


    def _deserialize(self, params):
        self.ClusterCIDR = params.get("ClusterCIDR")
        self.IgnoreClusterCIDRConflict = params.get("IgnoreClusterCIDRConflict")
        self.MaxNodePodNum = params.get("MaxNodePodNum")
        self.MaxClusterServiceNum = params.get("MaxClusterServiceNum")
        self.Ipvs = params.get("Ipvs")
        self.VpcId = params.get("VpcId")
        self.Cni = params.get("Cni")


class CreateClusterAsGroupRequest(AbstractModel):
    """CreateClusterAsGroup請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param AutoScalingGroupPara: 伸縮組創建透傳參數，json化字串格式，詳見[伸縮組創建實例](https://cloud.taifucloud.com/document/api/377/20440)介面。LaunchConfigurationId由LaunchConfigurePara參數創建，不支援填寫
        :type AutoScalingGroupPara: str
        :param LaunchConfigurePara: 啓動配置創建透傳參數，json化字串格式，詳見[創建啓動配置](https://cloud.taifucloud.com/document/api/377/20447)介面。另外ImageId參數由於集群維度已經有的ImageId訊息，這個欄位不需要填寫。UserData欄位設置通過UserScript設置，這個欄位不需要填寫。
        :type LaunchConfigurePara: str
        :param InstanceAdvancedSettings: 節點高級配置訊息
        :type InstanceAdvancedSettings: :class:`taifucloudcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param Labels: 節點Label數組
        :type Labels: list of Label
        """
        self.ClusterId = None
        self.AutoScalingGroupPara = None
        self.LaunchConfigurePara = None
        self.InstanceAdvancedSettings = None
        self.Labels = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.AutoScalingGroupPara = params.get("AutoScalingGroupPara")
        self.LaunchConfigurePara = params.get("LaunchConfigurePara")
        if params.get("InstanceAdvancedSettings") is not None:
            self.InstanceAdvancedSettings = InstanceAdvancedSettings()
            self.InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self.Labels.append(obj)


class CreateClusterAsGroupResponse(AbstractModel):
    """CreateClusterAsGroup返回參數結構體

    """

    def __init__(self):
        """
        :param LaunchConfigurationId: 啓動配置ID
        :type LaunchConfigurationId: str
        :param AutoScalingGroupId: 伸縮組ID
        :type AutoScalingGroupId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.LaunchConfigurationId = None
        self.AutoScalingGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.RequestId = params.get("RequestId")


class CreateClusterEndpointRequest(AbstractModel):
    """CreateClusterEndpoint請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param SubnetId: 集群端口所在的子網ID  (僅在開啓非外網訪問時需要填，必須爲集群所在VPC内的子網)
        :type SubnetId: str
        :param IsExtranet: 是否爲外網訪問（TRUE 外網訪問 FALSE 内網訪問，預設值： FALSE）
        :type IsExtranet: bool
        """
        self.ClusterId = None
        self.SubnetId = None
        self.IsExtranet = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.SubnetId = params.get("SubnetId")
        self.IsExtranet = params.get("IsExtranet")


class CreateClusterEndpointResponse(AbstractModel):
    """CreateClusterEndpoint返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateClusterEndpointVipRequest(AbstractModel):
    """CreateClusterEndpointVip請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param SecurityPolicies: 安全策略放通單個IP或CIDR(例如: "192.168.1.0/24",預設爲拒絕所有)
        :type SecurityPolicies: list of str
        """
        self.ClusterId = None
        self.SecurityPolicies = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.SecurityPolicies = params.get("SecurityPolicies")


class CreateClusterEndpointVipResponse(AbstractModel):
    """CreateClusterEndpointVip返回參數結構體

    """

    def __init__(self):
        """
        :param RequestFlowId: 請求任務的FlowId
        :type RequestFlowId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestFlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestFlowId = params.get("RequestFlowId")
        self.RequestId = params.get("RequestId")


class CreateClusterInstancesRequest(AbstractModel):
    """CreateClusterInstances請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群 ID，請填寫 查詢集群清單 介面中返回的 clusterId 欄位
        :type ClusterId: str
        :param RunInstancePara: CVM創建透傳參數，json化字串格式，詳見[CVM創建實例](https://cloud.taifucloud.com/document/product/213/15730)介面。
        :type RunInstancePara: str
        :param InstanceAdvancedSettings: 實例額外需要設置參數訊息
        :type InstanceAdvancedSettings: :class:`taifucloudcloud.tke.v20180525.models.InstanceAdvancedSettings`
        """
        self.ClusterId = None
        self.RunInstancePara = None
        self.InstanceAdvancedSettings = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.RunInstancePara = params.get("RunInstancePara")
        if params.get("InstanceAdvancedSettings") is not None:
            self.InstanceAdvancedSettings = InstanceAdvancedSettings()
            self.InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))


class CreateClusterInstancesResponse(AbstractModel):
    """CreateClusterInstances返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceIdSet: 節點實例ID
        :type InstanceIdSet: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.RequestId = params.get("RequestId")


class CreateClusterRequest(AbstractModel):
    """CreateCluster請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterCIDRSettings: 集群容器網絡配置訊息
        :type ClusterCIDRSettings: :class:`taifucloudcloud.tke.v20180525.models.ClusterCIDRSettings`
        :param ClusterType: 集群類型，托管集群：MANAGED_CLUSTER，獨立集群：INDEPENDENT_CLUSTER。
        :type ClusterType: str
        :param RunInstancesForNode: CVM創建透傳參數，json化字串格式，詳見[CVM創建實例](https://cloud.taifucloud.com/document/product/213/15730)介面。總機型(包括地域)數量不超過10個，相同機型(地域)購買多台機器可以通過設置參數中RunInstances中InstanceCount來實現。
        :type RunInstancesForNode: list of RunInstancesForNode
        :param ClusterBasicSettings: 集群的基本配置訊息
        :type ClusterBasicSettings: :class:`taifucloudcloud.tke.v20180525.models.ClusterBasicSettings`
        :param ClusterAdvancedSettings: 集群高級配置訊息
        :type ClusterAdvancedSettings: :class:`taifucloudcloud.tke.v20180525.models.ClusterAdvancedSettings`
        :param InstanceAdvancedSettings: 節點高級配置訊息
        :type InstanceAdvancedSettings: :class:`taifucloudcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param ExistedInstancesForNode: 已存在實例的配置訊息。所有實例必須在同一個VPC中，最大數量不超過100。
        :type ExistedInstancesForNode: list of ExistedInstancesForNode
        :param InstanceDataDiskMountSettings: CVM類型和其對應的數據盤掛載配置訊息
        :type InstanceDataDiskMountSettings: list of InstanceDataDiskMountSetting
        """
        self.ClusterCIDRSettings = None
        self.ClusterType = None
        self.RunInstancesForNode = None
        self.ClusterBasicSettings = None
        self.ClusterAdvancedSettings = None
        self.InstanceAdvancedSettings = None
        self.ExistedInstancesForNode = None
        self.InstanceDataDiskMountSettings = None


    def _deserialize(self, params):
        if params.get("ClusterCIDRSettings") is not None:
            self.ClusterCIDRSettings = ClusterCIDRSettings()
            self.ClusterCIDRSettings._deserialize(params.get("ClusterCIDRSettings"))
        self.ClusterType = params.get("ClusterType")
        if params.get("RunInstancesForNode") is not None:
            self.RunInstancesForNode = []
            for item in params.get("RunInstancesForNode"):
                obj = RunInstancesForNode()
                obj._deserialize(item)
                self.RunInstancesForNode.append(obj)
        if params.get("ClusterBasicSettings") is not None:
            self.ClusterBasicSettings = ClusterBasicSettings()
            self.ClusterBasicSettings._deserialize(params.get("ClusterBasicSettings"))
        if params.get("ClusterAdvancedSettings") is not None:
            self.ClusterAdvancedSettings = ClusterAdvancedSettings()
            self.ClusterAdvancedSettings._deserialize(params.get("ClusterAdvancedSettings"))
        if params.get("InstanceAdvancedSettings") is not None:
            self.InstanceAdvancedSettings = InstanceAdvancedSettings()
            self.InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        if params.get("ExistedInstancesForNode") is not None:
            self.ExistedInstancesForNode = []
            for item in params.get("ExistedInstancesForNode"):
                obj = ExistedInstancesForNode()
                obj._deserialize(item)
                self.ExistedInstancesForNode.append(obj)
        if params.get("InstanceDataDiskMountSettings") is not None:
            self.InstanceDataDiskMountSettings = []
            for item in params.get("InstanceDataDiskMountSettings"):
                obj = InstanceDataDiskMountSetting()
                obj._deserialize(item)
                self.InstanceDataDiskMountSettings.append(obj)


class CreateClusterResponse(AbstractModel):
    """CreateCluster返回參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ClusterId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.RequestId = params.get("RequestId")


class CreateClusterRouteRequest(AbstractModel):
    """CreateClusterRoute請求參數結構體

    """

    def __init__(self):
        """
        :param RouteTableName: 路由表名稱。
        :type RouteTableName: str
        :param DestinationCidrBlock: 目的端CIDR。
        :type DestinationCidrBlock: str
        :param GatewayIp: 下一跳網址。
        :type GatewayIp: str
        """
        self.RouteTableName = None
        self.DestinationCidrBlock = None
        self.GatewayIp = None


    def _deserialize(self, params):
        self.RouteTableName = params.get("RouteTableName")
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        self.GatewayIp = params.get("GatewayIp")


class CreateClusterRouteResponse(AbstractModel):
    """CreateClusterRoute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateClusterRouteTableRequest(AbstractModel):
    """CreateClusterRouteTable請求參數結構體

    """

    def __init__(self):
        """
        :param RouteTableName: 路由表名稱
        :type RouteTableName: str
        :param RouteTableCidrBlock: 路由表CIDR
        :type RouteTableCidrBlock: str
        :param VpcId: 路由表綁定的VPC
        :type VpcId: str
        :param IgnoreClusterCidrConflict: 是否忽略CIDR沖突
        :type IgnoreClusterCidrConflict: int
        """
        self.RouteTableName = None
        self.RouteTableCidrBlock = None
        self.VpcId = None
        self.IgnoreClusterCidrConflict = None


    def _deserialize(self, params):
        self.RouteTableName = params.get("RouteTableName")
        self.RouteTableCidrBlock = params.get("RouteTableCidrBlock")
        self.VpcId = params.get("VpcId")
        self.IgnoreClusterCidrConflict = params.get("IgnoreClusterCidrConflict")


class CreateClusterRouteTableResponse(AbstractModel):
    """CreateClusterRouteTable返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DataDisk(AbstractModel):
    """描述了k8s節點數據盤相關配置與訊息。

    """

    def __init__(self):
        """
        :param DiskType: 雲盤類型
        :type DiskType: str
        :param FileSystem: 文件系統(ext3/ext4/xfs)
        :type FileSystem: str
        :param DiskSize: 雲盤大小(G）
        :type DiskSize: int
        :param AutoFormatAndMount: 是否自動化格式盤並掛載
        :type AutoFormatAndMount: bool
        :param MountTarget: 掛載目錄
        :type MountTarget: str
        """
        self.DiskType = None
        self.FileSystem = None
        self.DiskSize = None
        self.AutoFormatAndMount = None
        self.MountTarget = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.FileSystem = params.get("FileSystem")
        self.DiskSize = params.get("DiskSize")
        self.AutoFormatAndMount = params.get("AutoFormatAndMount")
        self.MountTarget = params.get("MountTarget")


class DeleteClusterAsGroupsRequest(AbstractModel):
    """DeleteClusterAsGroups請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID，通過[DescribeClusters](https://cloud.taifucloud.com/document/api/457/31862)介面獲取。
        :type ClusterId: str
        :param AutoScalingGroupIds: 集群伸縮組ID的清單
        :type AutoScalingGroupIds: list of str
        :param KeepInstance: 是否保留伸縮組中的節點(預設值： false(不保留))
        :type KeepInstance: bool
        """
        self.ClusterId = None
        self.AutoScalingGroupIds = None
        self.KeepInstance = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.AutoScalingGroupIds = params.get("AutoScalingGroupIds")
        self.KeepInstance = params.get("KeepInstance")


class DeleteClusterAsGroupsResponse(AbstractModel):
    """DeleteClusterAsGroups返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClusterEndpointRequest(AbstractModel):
    """DeleteClusterEndpoint請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param IsExtranet: 是否爲外網訪問（TRUE 外網訪問 FALSE 内網訪問，預設值： FALSE）
        :type IsExtranet: bool
        """
        self.ClusterId = None
        self.IsExtranet = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.IsExtranet = params.get("IsExtranet")


class DeleteClusterEndpointResponse(AbstractModel):
    """DeleteClusterEndpoint返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClusterEndpointVipRequest(AbstractModel):
    """DeleteClusterEndpointVip請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")


class DeleteClusterEndpointVipResponse(AbstractModel):
    """DeleteClusterEndpointVip返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClusterInstancesRequest(AbstractModel):
    """DeleteClusterInstances請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceIds: 主機InstanceId清單
        :type InstanceIds: list of str
        :param InstanceDeleteMode: 集群實例删除時的策略：terminate（銷毀實例，僅支援按量計費雲主機實例） retain （僅移除，保留實例）
        :type InstanceDeleteMode: str
        :param ForceDelete: 是否強制删除(當節點在初始化時，可以指定參數爲TRUE)
        :type ForceDelete: bool
        """
        self.ClusterId = None
        self.InstanceIds = None
        self.InstanceDeleteMode = None
        self.ForceDelete = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceDeleteMode = params.get("InstanceDeleteMode")
        self.ForceDelete = params.get("ForceDelete")


class DeleteClusterInstancesResponse(AbstractModel):
    """DeleteClusterInstances返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClusterRequest(AbstractModel):
    """DeleteCluster請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceDeleteMode: 集群實例删除時的策略：terminate（銷毀實例，僅支援按量計費雲主機實例） retain （僅移除，保留實例）
        :type InstanceDeleteMode: str
        :param ResourceDeleteOptions: 集群删除時資源的删除策略，目前支援CBS（預設保留CBS）
        :type ResourceDeleteOptions: list of ResourceDeleteOption
        """
        self.ClusterId = None
        self.InstanceDeleteMode = None
        self.ResourceDeleteOptions = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceDeleteMode = params.get("InstanceDeleteMode")
        if params.get("ResourceDeleteOptions") is not None:
            self.ResourceDeleteOptions = []
            for item in params.get("ResourceDeleteOptions"):
                obj = ResourceDeleteOption()
                obj._deserialize(item)
                self.ResourceDeleteOptions.append(obj)


class DeleteClusterResponse(AbstractModel):
    """DeleteCluster返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClusterRouteRequest(AbstractModel):
    """DeleteClusterRoute請求參數結構體

    """

    def __init__(self):
        """
        :param RouteTableName: 路由表名稱。
        :type RouteTableName: str
        :param GatewayIp: 下一跳網址。
        :type GatewayIp: str
        :param DestinationCidrBlock: 目的端CIDR。
        :type DestinationCidrBlock: str
        """
        self.RouteTableName = None
        self.GatewayIp = None
        self.DestinationCidrBlock = None


    def _deserialize(self, params):
        self.RouteTableName = params.get("RouteTableName")
        self.GatewayIp = params.get("GatewayIp")
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")


class DeleteClusterRouteResponse(AbstractModel):
    """DeleteClusterRoute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClusterRouteTableRequest(AbstractModel):
    """DeleteClusterRouteTable請求參數結構體

    """

    def __init__(self):
        """
        :param RouteTableName: 路由表名稱
        :type RouteTableName: str
        """
        self.RouteTableName = None


    def _deserialize(self, params):
        self.RouteTableName = params.get("RouteTableName")


class DeleteClusterRouteTableResponse(AbstractModel):
    """DeleteClusterRouteTable返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeClusterAsGroupOptionRequest(AbstractModel):
    """DescribeClusterAsGroupOption請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")


class DescribeClusterAsGroupOptionResponse(AbstractModel):
    """DescribeClusterAsGroupOption返回參數結構體

    """

    def __init__(self):
        """
        :param ClusterAsGroupOption: 集群彈性伸縮屬性
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterAsGroupOption: :class:`taifucloudcloud.tke.v20180525.models.ClusterAsGroupOption`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ClusterAsGroupOption = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClusterAsGroupOption") is not None:
            self.ClusterAsGroupOption = ClusterAsGroupOption()
            self.ClusterAsGroupOption._deserialize(params.get("ClusterAsGroupOption"))
        self.RequestId = params.get("RequestId")


class DescribeClusterAsGroupsRequest(AbstractModel):
    """DescribeClusterAsGroups請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param AutoScalingGroupIds: 伸縮組ID清單，如果爲空，表示拉取集群關聯的所有伸縮組。
        :type AutoScalingGroupIds: list of str
        :param Offset: 偏移量，預設爲0。關於Offset的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。關於Limit的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Limit: int
        """
        self.ClusterId = None
        self.AutoScalingGroupIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.AutoScalingGroupIds = params.get("AutoScalingGroupIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeClusterAsGroupsResponse(AbstractModel):
    """DescribeClusterAsGroups返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 集群關聯的伸縮組總數
        :type TotalCount: int
        :param ClusterAsGroupSet: 集群關聯的伸縮組清單
        :type ClusterAsGroupSet: :class:`taifucloudcloud.tke.v20180525.models.ClusterAsGroup`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ClusterAsGroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ClusterAsGroupSet") is not None:
            self.ClusterAsGroupSet = ClusterAsGroup()
            self.ClusterAsGroupSet._deserialize(params.get("ClusterAsGroupSet"))
        self.RequestId = params.get("RequestId")


class DescribeClusterEndpointStatusRequest(AbstractModel):
    """DescribeClusterEndpointStatus請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param IsExtranet: 是否爲外網訪問（TRUE 外網訪問 FALSE 内網訪問，預設值： FALSE）
        :type IsExtranet: bool
        """
        self.ClusterId = None
        self.IsExtranet = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.IsExtranet = params.get("IsExtranet")


class DescribeClusterEndpointStatusResponse(AbstractModel):
    """DescribeClusterEndpointStatus返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 查詢集群訪問端口狀态（Created 開啓成功，Creating 開啓中中，NotFound 未開啓）
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeClusterEndpointVipStatusRequest(AbstractModel):
    """DescribeClusterEndpointVipStatus請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")


class DescribeClusterEndpointVipStatusResponse(AbstractModel):
    """DescribeClusterEndpointVipStatus返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 端口操作狀态 (Creating 創建中  CreateFailed 創建失敗 Created 創建完成 Deleting 删除中 DeletedFailed 删除失敗 Deleted 已删除 NotFound 未發現操作 )
        :type Status: str
        :param ErrorMsg: 操作失敗的原因
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.ErrorMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrorMsg = params.get("ErrorMsg")
        self.RequestId = params.get("RequestId")


class DescribeClusterInstancesRequest(AbstractModel):
    """DescribeClusterInstances請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param Offset: 偏移量，預設爲0。關於Offset的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。關於Limit的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Limit: int
        :param InstanceIds: 需要獲取的節點實例Id清單。如果爲空，表示拉取集群下所有節點實例。
        :type InstanceIds: list of str
        :param InstanceRole: 節點角色, MASTER, WORKER, ETCD, MASTER_ETCD,ALL, 預設爲WORKER。預設爲WORKER類型。
        :type InstanceRole: str
        """
        self.ClusterId = None
        self.Offset = None
        self.Limit = None
        self.InstanceIds = None
        self.InstanceRole = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceRole = params.get("InstanceRole")


class DescribeClusterInstancesResponse(AbstractModel):
    """DescribeClusterInstances返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 集群中實例總數
        :type TotalCount: int
        :param InstanceSet: 集群中實例清單
        :type InstanceSet: list of Instance
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = Instance()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterRouteTablesRequest(AbstractModel):
    """DescribeClusterRouteTables請求參數結構體

    """


class DescribeClusterRouteTablesResponse(AbstractModel):
    """DescribeClusterRouteTables返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的實例數量。
        :type TotalCount: int
        :param RouteTableSet: 集群路由表對象。
        :type RouteTableSet: list of RouteTableInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RouteTableSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RouteTableSet") is not None:
            self.RouteTableSet = []
            for item in params.get("RouteTableSet"):
                obj = RouteTableInfo()
                obj._deserialize(item)
                self.RouteTableSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterRoutesRequest(AbstractModel):
    """DescribeClusterRoutes請求參數結構體

    """

    def __init__(self):
        """
        :param RouteTableName: 路由表名稱。
        :type RouteTableName: str
        """
        self.RouteTableName = None


    def _deserialize(self, params):
        self.RouteTableName = params.get("RouteTableName")


class DescribeClusterRoutesResponse(AbstractModel):
    """DescribeClusterRoutes返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的實例數量。
        :type TotalCount: int
        :param RouteSet: 集群路由對象。
        :type RouteSet: list of RouteInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RouteSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RouteSet") is not None:
            self.RouteSet = []
            for item in params.get("RouteSet"):
                obj = RouteInfo()
                obj._deserialize(item)
                self.RouteSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterSecurityRequest(AbstractModel):
    """DescribeClusterSecurity請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群 ID，請填寫 查詢集群清單 介面中返回的 clusterId 欄位
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")


class DescribeClusterSecurityResponse(AbstractModel):
    """DescribeClusterSecurity返回參數結構體

    """

    def __init__(self):
        """
        :param UserName: 集群的賬號名稱
        :type UserName: str
        :param Password: 集群的訪問密碼
        :type Password: str
        :param CertificationAuthority: 集群訪問CA證書
        :type CertificationAuthority: str
        :param ClusterExternalEndpoint: 集群訪問的網址
        :type ClusterExternalEndpoint: str
        :param Domain: 集群訪問的域名
        :type Domain: str
        :param PgwEndpoint: 集群Endpoint網址
        :type PgwEndpoint: str
        :param SecurityPolicy: 集群訪問策略組
        :type SecurityPolicy: list of str
        :param Kubeconfig: 集群Kubeconfig文件
注意：此欄位可能返回 null，表示取不到有效值。
        :type Kubeconfig: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.UserName = None
        self.Password = None
        self.CertificationAuthority = None
        self.ClusterExternalEndpoint = None
        self.Domain = None
        self.PgwEndpoint = None
        self.SecurityPolicy = None
        self.Kubeconfig = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        self.CertificationAuthority = params.get("CertificationAuthority")
        self.ClusterExternalEndpoint = params.get("ClusterExternalEndpoint")
        self.Domain = params.get("Domain")
        self.PgwEndpoint = params.get("PgwEndpoint")
        self.SecurityPolicy = params.get("SecurityPolicy")
        self.Kubeconfig = params.get("Kubeconfig")
        self.RequestId = params.get("RequestId")


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterIds: 集群ID清單(爲空時，
表示獲取賬號下所有集群)
        :type ClusterIds: list of str
        :param Offset: 偏移量,預設0
        :type Offset: int
        :param Limit: 最大輸出條數，預設20，最大爲100
        :type Limit: int
        :param Filters: 過濾條件,當前只支援按照單個條件ClusterName進行過濾
        :type Filters: list of Filter
        """
        self.ClusterIds = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.ClusterIds = params.get("ClusterIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeClustersResponse(AbstractModel):
    """DescribeClusters返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 集群總個數
        :type TotalCount: int
        :param Clusters: 集群訊息清單
        :type Clusters: list of Cluster
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Clusters = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Clusters") is not None:
            self.Clusters = []
            for item in params.get("Clusters"):
                obj = Cluster()
                obj._deserialize(item)
                self.Clusters.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeExistedInstancesRequest(AbstractModel):
    """DescribeExistedInstances請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群 ID，請填寫查詢集群清單 介面中返回的 ClusterId 欄位（僅通過ClusterId獲取需要過濾條件中的VPCID。節點狀态比較時會使用該地域下所有集群中的節點進行比較。參數不支援同時指定InstanceIds和ClusterId。
        :type ClusterId: str
        :param InstanceIds: 按照一個或者多個實例ID查詢。實例ID形如：ins-xxxxxxxx。（此參數的具體格式可參考API簡介的id.N一節）。每次請求的實例的上限爲100。參數不支援同時指定InstanceIds和Filters。
        :type InstanceIds: list of str
        :param Filters: 過濾條件,欄位和詳見[CVM查詢實例](https://cloud.taifucloud.com/document/api/213/15728)如果設置了ClusterId，會附加集群的VPCID作爲查詢欄位，在此情況下如果在Filter中指定了"vpc-id"作爲過濾欄位，指定的VPCID必須與集群的VPCID相同。
        :type Filters: list of Filter
        :param VagueIpAddress: 實例IP進行過濾(同時支援内網IP和外網IP)
        :type VagueIpAddress: str
        :param VagueInstanceName: 實例名稱進行過濾
        :type VagueInstanceName: str
        :param Offset: 偏移量，預設爲0。關於Offset的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。關於Limit的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Limit: int
        """
        self.ClusterId = None
        self.InstanceIds = None
        self.Filters = None
        self.VagueIpAddress = None
        self.VagueInstanceName = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIds = params.get("InstanceIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.VagueIpAddress = params.get("VagueIpAddress")
        self.VagueInstanceName = params.get("VagueInstanceName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeExistedInstancesResponse(AbstractModel):
    """DescribeExistedInstances返回參數結構體

    """

    def __init__(self):
        """
        :param ExistedInstanceSet: 已經存在的實例訊息數組。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ExistedInstanceSet: list of ExistedInstance
        :param TotalCount: 符合條件的實例數量。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ExistedInstanceSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ExistedInstanceSet") is not None:
            self.ExistedInstanceSet = []
            for item in params.get("ExistedInstanceSet"):
                obj = ExistedInstance()
                obj._deserialize(item)
                self.ExistedInstanceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeImagesRequest(AbstractModel):
    """DescribeImages請求參數結構體

    """


class DescribeImagesResponse(AbstractModel):
    """DescribeImages返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 映像數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param ImageInstanceSet: 映像訊息清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type ImageInstanceSet: list of ImageInstance
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ImageInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ImageInstanceSet") is not None:
            self.ImageInstanceSet = []
            for item in params.get("ImageInstanceSet"):
                obj = ImageInstance()
                obj._deserialize(item)
                self.ImageInstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions請求參數結構體

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 地域的數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RegionInstanceSet: 地域清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type RegionInstanceSet: list of RegionInstance
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RegionInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RegionInstanceSet") is not None:
            self.RegionInstanceSet = []
            for item in params.get("RegionInstanceSet"):
                obj = RegionInstance()
                obj._deserialize(item)
                self.RegionInstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRouteTableConflictsRequest(AbstractModel):
    """DescribeRouteTableConflicts請求參數結構體

    """

    def __init__(self):
        """
        :param RouteTableCidrBlock: 路由表CIDR
        :type RouteTableCidrBlock: str
        :param VpcId: 路由表綁定的VPC
        :type VpcId: str
        """
        self.RouteTableCidrBlock = None
        self.VpcId = None


    def _deserialize(self, params):
        self.RouteTableCidrBlock = params.get("RouteTableCidrBlock")
        self.VpcId = params.get("VpcId")


class DescribeRouteTableConflictsResponse(AbstractModel):
    """DescribeRouteTableConflicts返回參數結構體

    """

    def __init__(self):
        """
        :param HasConflict: 路由表是否沖突。
        :type HasConflict: bool
        :param RouteTableConflictSet: 路由表沖突清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RouteTableConflictSet: list of RouteTableConflict
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.HasConflict = None
        self.RouteTableConflictSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.HasConflict = params.get("HasConflict")
        if params.get("RouteTableConflictSet") is not None:
            self.RouteTableConflictSet = []
            for item in params.get("RouteTableConflictSet"):
                obj = RouteTableConflict()
                obj._deserialize(item)
                self.RouteTableConflictSet.append(obj)
        self.RequestId = params.get("RequestId")


class EnhancedService(AbstractModel):
    """描述了實例的增強服務啓用情況與其設置，如雲安全，雲監控等實例 Agent

    """

    def __init__(self):
        """
        :param SecurityService: 開啓雲安全服務。若不指定該參數，則預設開啓雲安全服務。
        :type SecurityService: :class:`taifucloudcloud.tke.v20180525.models.RunSecurityServiceEnabled`
        :param MonitorService: 開啓雲監控服務。若不指定該參數，則預設開啓雲監控服務。
        :type MonitorService: :class:`taifucloudcloud.tke.v20180525.models.RunMonitorServiceEnabled`
        """
        self.SecurityService = None
        self.MonitorService = None


    def _deserialize(self, params):
        if params.get("SecurityService") is not None:
            self.SecurityService = RunSecurityServiceEnabled()
            self.SecurityService._deserialize(params.get("SecurityService"))
        if params.get("MonitorService") is not None:
            self.MonitorService = RunMonitorServiceEnabled()
            self.MonitorService._deserialize(params.get("MonitorService"))


class ExistedInstance(AbstractModel):
    """已經存在的實例訊息

    """

    def __init__(self):
        """
        :param Usable: 實例是否支援加入集群(TRUE 可以加入 FALSE 不能加入)。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Usable: bool
        :param UnusableReason: 實例不支援加入的原因。
注意：此欄位可能返回 null，表示取不到有效值。
        :type UnusableReason: str
        :param AlreadyInCluster: 實例已經所在的集群ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AlreadyInCluster: str
        :param InstanceId: 實例ID形如：ins-xxxxxxxx。
        :type InstanceId: str
        :param InstanceName: 實例名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param PrivateIpAddresses: 實例主網卡的内網IP清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PrivateIpAddresses: list of str
        :param PublicIpAddresses: 實例主網卡的公網IP清單。
注意：此欄位可能返回 null，表示取不到有效值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PublicIpAddresses: list of str
        :param CreatedTime: 創建時間。按照ISO8601標準表示，並且使用UTC時間。格式爲：YYYY-MM-DDThh:mm:ssZ。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param InstanceChargeType: 實例計費模式。取值範圍：
PREPAID：表示預付費，即包年包月
POSTPAID_BY_HOUR：表示後付費，即按量計費
CDHPAID：CDH付費，即只對CDH計費，不對CDH上的實例計費。
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceChargeType: str
        :param CPU: 實例的CPU核數，單位：核。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CPU: int
        :param Memory: 實例内存容量，單位：GB。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Memory: int
        :param OsName: 作業系統名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OsName: str
        :param InstanceType: 實例機型。
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceType: str
        """
        self.Usable = None
        self.UnusableReason = None
        self.AlreadyInCluster = None
        self.InstanceId = None
        self.InstanceName = None
        self.PrivateIpAddresses = None
        self.PublicIpAddresses = None
        self.CreatedTime = None
        self.InstanceChargeType = None
        self.CPU = None
        self.Memory = None
        self.OsName = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.Usable = params.get("Usable")
        self.UnusableReason = params.get("UnusableReason")
        self.AlreadyInCluster = params.get("AlreadyInCluster")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.CreatedTime = params.get("CreatedTime")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")
        self.OsName = params.get("OsName")
        self.InstanceType = params.get("InstanceType")


class ExistedInstancesForNode(AbstractModel):
    """不同角色的已存在節點配置參數

    """

    def __init__(self):
        """
        :param NodeRole: 節點角色，取值:MASTER_ETCD, WORKER。MASTER_ETCD只有在創建 INDEPENDENT_CLUSTER 獨立集群時需要指定。MASTER_ETCD節點數量爲3～7，建議爲奇數。MASTER_ETCD最小配置爲4C8G。
        :type NodeRole: str
        :param ExistedInstancesPara: 已存在實例的重裝參數
        :type ExistedInstancesPara: :class:`taifucloudcloud.tke.v20180525.models.ExistedInstancesPara`
        :param InstanceAdvancedSettingsOverride: 節點高級設置，會函蓋集群級别設置的InstanceAdvancedSettings（當前只對節點自定義參數ExtraArgs生效）
        :type InstanceAdvancedSettingsOverride: :class:`taifucloudcloud.tke.v20180525.models.InstanceAdvancedSettings`
        """
        self.NodeRole = None
        self.ExistedInstancesPara = None
        self.InstanceAdvancedSettingsOverride = None


    def _deserialize(self, params):
        self.NodeRole = params.get("NodeRole")
        if params.get("ExistedInstancesPara") is not None:
            self.ExistedInstancesPara = ExistedInstancesPara()
            self.ExistedInstancesPara._deserialize(params.get("ExistedInstancesPara"))
        if params.get("InstanceAdvancedSettingsOverride") is not None:
            self.InstanceAdvancedSettingsOverride = InstanceAdvancedSettings()
            self.InstanceAdvancedSettingsOverride._deserialize(params.get("InstanceAdvancedSettingsOverride"))


class ExistedInstancesPara(AbstractModel):
    """已存在實例的重裝參數

    """

    def __init__(self):
        """
        :param InstanceIds: 集群ID
        :type InstanceIds: list of str
        :param InstanceAdvancedSettings: 實例額外需要設置參數訊息
        :type InstanceAdvancedSettings: :class:`taifucloudcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param EnhancedService: 增強服務。通過該參數可以指定是否開啓雲安全、雲監控等服務。若不指定該參數，則預設開啓雲監控、雲安全服務。
        :type EnhancedService: :class:`taifucloudcloud.tke.v20180525.models.EnhancedService`
        :param LoginSettings: 節點登入訊息（目前僅支援使用Password或者單個KeyIds）
        :type LoginSettings: :class:`taifucloudcloud.tke.v20180525.models.LoginSettings`
        :param SecurityGroupIds: 實例所屬安全組。該參數可以通過調用 DescribeSecurityGroups 的返回值中的sgId欄位來獲取。若不指定該參數，則綁定預設安全組。
        :type SecurityGroupIds: list of str
        :param HostName: 重灌系統時，可以指定修改實例的HostName(集群爲HostName模式時，此參數必傳，規則名稱除不支援大寫字元外與[CVM創建實例](https://cloud.taifucloud.com/document/product/213/15730)介面HostName一緻)
        :type HostName: str
        """
        self.InstanceIds = None
        self.InstanceAdvancedSettings = None
        self.EnhancedService = None
        self.LoginSettings = None
        self.SecurityGroupIds = None
        self.HostName = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("InstanceAdvancedSettings") is not None:
            self.InstanceAdvancedSettings = InstanceAdvancedSettings()
            self.InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.HostName = params.get("HostName")


class Filter(AbstractModel):
    """>描述鍵值對過濾器，用於條件過濾查詢。例如過濾ID、名稱、狀态等
    > * 若存在多個`Filter`時，`Filter`間的關系爲邏輯與（`AND`）關系。
    > * 若同一個`Filter`存在多個`Values`，同一`Filter`下`Values`間的關系爲邏輯或（`OR`）關系。
    >
    > 以[DescribeInstances](https://cloud.taifucloud.com/document/api/213/15728)介面的`Filter`爲例。若我們需要查詢可用區（`zone`）爲 一區 ***並且*** 實例計費模式（`instance-charge-type`）爲包年包月 ***或者*** 按量計費的實例時，可如下實現：
    ```
    Filters.0.Name=zone
    &Filters.0.Values.0=ap-guangzhou-1
    &Filters.1.Name=instance-charge-type
    &Filters.1.Values.0=PREPAID
    &Filters.1.Values.1=POSTPAID_BY_HOUR
    ```

    """

    def __init__(self):
        """
        :param Name: 需要過濾的欄位。
        :type Name: str
        :param Values: 欄位的過濾值。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class ImageInstance(AbstractModel):
    """映像訊息

    """

    def __init__(self):
        """
        :param Alias: 映像别名
注意：此欄位可能返回 null，表示取不到有效值。
        :type Alias: str
        :param OsName: 作業系統名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type OsName: str
        :param ImageId: 映像ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ImageId: str
        :param OsCustomizeType: 容器的映像版本，"DOCKER_CUSTOMIZE"(容器定制版),"GENERAL"(普通版本，預設值)
注意：此欄位可能返回 null，表示取不到有效值。
        :type OsCustomizeType: str
        """
        self.Alias = None
        self.OsName = None
        self.ImageId = None
        self.OsCustomizeType = None


    def _deserialize(self, params):
        self.Alias = params.get("Alias")
        self.OsName = params.get("OsName")
        self.ImageId = params.get("ImageId")
        self.OsCustomizeType = params.get("OsCustomizeType")


class Instance(AbstractModel):
    """集群的實例訊息

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param InstanceRole: 節點角色, MASTER, WORKER, ETCD, MASTER_ETCD,ALL, 預設爲WORKER
        :type InstanceRole: str
        :param FailedReason: 實例異常(或者處於初始化中)的原因
        :type FailedReason: str
        :param InstanceState: 實例的狀态（running 運作中，initializing 初始化中，failed 異常）
        :type InstanceState: str
        :param DrainStatus: 實例是否封鎖狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type DrainStatus: str
        :param InstanceAdvancedSettings: 節點配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceAdvancedSettings: :class:`taifucloudcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param CreatedTime: 添加時間
        :type CreatedTime: str
        :param LanIP: 節點内網IP
注意：此欄位可能返回 null，表示取不到有效值。
        :type LanIP: str
        """
        self.InstanceId = None
        self.InstanceRole = None
        self.FailedReason = None
        self.InstanceState = None
        self.DrainStatus = None
        self.InstanceAdvancedSettings = None
        self.CreatedTime = None
        self.LanIP = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceRole = params.get("InstanceRole")
        self.FailedReason = params.get("FailedReason")
        self.InstanceState = params.get("InstanceState")
        self.DrainStatus = params.get("DrainStatus")
        if params.get("InstanceAdvancedSettings") is not None:
            self.InstanceAdvancedSettings = InstanceAdvancedSettings()
            self.InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        self.CreatedTime = params.get("CreatedTime")
        self.LanIP = params.get("LanIP")


class InstanceAdvancedSettings(AbstractModel):
    """描述了k8s集群相關配置與訊息。

    """

    def __init__(self):
        """
        :param MountTarget: 數據盤掛載點, 預設不掛載數據盤. 已格式化的 ext3，ext4，xfs 文件系統的數據盤将直接掛載，其他文件系統或未格式化的數據盤将自動格式化爲ext4 並掛載，請注意備份數據! 無數據盤或有多塊數據盤的雲主機此設置不生效。
        :type MountTarget: str
        :param DockerGraphPath: dockerd --graph 指定值, 預設爲 /var/lib/docker
        :type DockerGraphPath: str
        :param UserScript: base64 編碼的用戶腳本, 此腳本會在 k8s 元件運作後執行, 需要用戶保證腳本的可重入及重試邏輯, 腳本及其生成的日志文件可在節點的 /data/ccs_userscript/ 路徑檢視, 如果要求節點需要在進行初始化完成後才可加入調度, 可配合 unschedulable 參數使用, 在 userScript 最後初始化完成後, 添加 kubectl uncordon nodename --kubeconfig=/root/.kube/config 命令使節點加入調度
        :type UserScript: str
        :param Unschedulable: 設置加入的節點是否參與調度，預設值爲0，表示參與調度；非0表示不參與調度, 待節點初始化完成之後, 可執行kubectl uncordon nodename使node加入調度.
        :type Unschedulable: int
        :param Labels: 節點Label數組
        :type Labels: list of Label
        :param DataDisks: 數據盤相關訊息
        :type DataDisks: list of DataDisk
        :param ExtraArgs: 節點相關的自定義參數訊息
        :type ExtraArgs: :class:`taifucloudcloud.tke.v20180525.models.InstanceExtraArgs`
        """
        self.MountTarget = None
        self.DockerGraphPath = None
        self.UserScript = None
        self.Unschedulable = None
        self.Labels = None
        self.DataDisks = None
        self.ExtraArgs = None


    def _deserialize(self, params):
        self.MountTarget = params.get("MountTarget")
        self.DockerGraphPath = params.get("DockerGraphPath")
        self.UserScript = params.get("UserScript")
        self.Unschedulable = params.get("Unschedulable")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("ExtraArgs") is not None:
            self.ExtraArgs = InstanceExtraArgs()
            self.ExtraArgs._deserialize(params.get("ExtraArgs"))


class InstanceDataDiskMountSetting(AbstractModel):
    """CVM實例數據盤掛載配置

    """

    def __init__(self):
        """
        :param InstanceType: CVM實例類型
        :type InstanceType: str
        :param DataDisks: 數據盤掛載訊息
        :type DataDisks: list of DataDisk
        :param Zone: CVM實例所屬可用區
        :type Zone: str
        """
        self.InstanceType = None
        self.DataDisks = None
        self.Zone = None


    def _deserialize(self, params):
        self.InstanceType = params.get("InstanceType")
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        self.Zone = params.get("Zone")


class InstanceExtraArgs(AbstractModel):
    """節點自定義參數

    """

    def __init__(self):
        """
        :param Kubelet: kubelet自定義參數
注意：此欄位可能返回 null，表示取不到有效值。
        :type Kubelet: list of str
        """
        self.Kubelet = None


    def _deserialize(self, params):
        self.Kubelet = params.get("Kubelet")


class Label(AbstractModel):
    """k8s中標簽，一般以數組的方式存在

    """

    def __init__(self):
        """
        :param Name: map表中的Name
        :type Name: str
        :param Value: map表中的Value
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class LoginSettings(AbstractModel):
    """描述了實例登入相關配置與訊息。

    """

    def __init__(self):
        """
        :param Password: 實例登入密碼。不同作業系統類型密碼複雜度限制不一樣，具體如下：<br><li>Linux實例密碼必須8到30位，至少包括兩項[a-z]，[A-Z]、[0-9] 和 [( ) \` ~ ! @ # $ % ^ & *  - + = | { } [ ] : ; ' , . ? / ]中的特殊符號。<br><li>Windows實例密碼必須12到30位，至少包括三項[a-z]，[A-Z]，[0-9] 和 [( ) \` ~ ! @ # $ % ^ & * - + = | { } [ ] : ; ' , . ? /]中的特殊符號。<br><br>若不指定該參數，則由系統随機生成密碼，並通過站内信方式通知到用戶。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Password: str
        :param KeyIds: 金鑰ID清單。關聯金鑰後，就可以通過對應的私鑰來訪問實例；KeyId可通過介面[DescribeKeyPairs](https://cloud.taifucloud.com/document/api/213/15699)獲取，金鑰與密碼不能同時指定，同時Windows作業系統不支援指定金鑰。當前僅支援購買的時候指定一個金鑰。
注意：此欄位可能返回 null，表示取不到有效值。
        :type KeyIds: list of str
        :param KeepImageLogin: 保持映像的原始設置。該參數與Password或KeyIds.N不能同時指定。只有使用自定義映像、共享映像或外部導入映像創建實例時才能指定該參數爲TRUE。取值範圍：<br><li>TRUE：表示保持映像的登入設置<br><li>FALSE：表示不保持映像的登入設置<br><br>預設取值：FALSE。
注意：此欄位可能返回 null，表示取不到有效值。
        :type KeepImageLogin: str
        """
        self.Password = None
        self.KeyIds = None
        self.KeepImageLogin = None


    def _deserialize(self, params):
        self.Password = params.get("Password")
        self.KeyIds = params.get("KeyIds")
        self.KeepImageLogin = params.get("KeepImageLogin")


class ModifyClusterAsGroupAttributeRequest(AbstractModel):
    """ModifyClusterAsGroupAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ClusterAsGroupAttribute: 集群關聯的伸縮組屬性
        :type ClusterAsGroupAttribute: :class:`taifucloudcloud.tke.v20180525.models.ClusterAsGroupAttribute`
        """
        self.ClusterId = None
        self.ClusterAsGroupAttribute = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("ClusterAsGroupAttribute") is not None:
            self.ClusterAsGroupAttribute = ClusterAsGroupAttribute()
            self.ClusterAsGroupAttribute._deserialize(params.get("ClusterAsGroupAttribute"))


class ModifyClusterAsGroupAttributeResponse(AbstractModel):
    """ModifyClusterAsGroupAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterAttributeRequest(AbstractModel):
    """ModifyClusterAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ProjectId: 集群所屬項目
        :type ProjectId: int
        :param ClusterName: 集群名稱
        :type ClusterName: str
        :param ClusterDesc: 集群描述
        :type ClusterDesc: str
        """
        self.ClusterId = None
        self.ProjectId = None
        self.ClusterName = None
        self.ClusterDesc = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ProjectId = params.get("ProjectId")
        self.ClusterName = params.get("ClusterName")
        self.ClusterDesc = params.get("ClusterDesc")


class ModifyClusterAttributeResponse(AbstractModel):
    """ModifyClusterAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: 集群所屬項目
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param ClusterName: 集群名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param ClusterDesc: 集群描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterDesc: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ProjectId = None
        self.ClusterName = None
        self.ClusterDesc = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ClusterName = params.get("ClusterName")
        self.ClusterDesc = params.get("ClusterDesc")
        self.RequestId = params.get("RequestId")


class ModifyClusterEndpointSPRequest(AbstractModel):
    """ModifyClusterEndpointSP請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param SecurityPolicies: 安全策略放通單個IP或CIDR(例如: "192.168.1.0/24",預設爲拒絕所有)
        :type SecurityPolicies: list of str
        """
        self.ClusterId = None
        self.SecurityPolicies = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.SecurityPolicies = params.get("SecurityPolicies")


class ModifyClusterEndpointSPResponse(AbstractModel):
    """ModifyClusterEndpointSP返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegionInstance(AbstractModel):
    """地域屬性訊息

    """

    def __init__(self):
        """
        :param RegionName: 地域名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type RegionName: str
        :param RegionId: 地域ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type RegionId: int
        :param Status: 地域狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: str
        :param FeatureGates: 地域特性開關(按照JSON的形式返回所有屬性)
注意：此欄位可能返回 null，表示取不到有效值。
        :type FeatureGates: str
        :param Alias: 地域簡稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type Alias: str
        :param Remark: 地域白名單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self.RegionName = None
        self.RegionId = None
        self.Status = None
        self.FeatureGates = None
        self.Alias = None
        self.Remark = None


    def _deserialize(self, params):
        self.RegionName = params.get("RegionName")
        self.RegionId = params.get("RegionId")
        self.Status = params.get("Status")
        self.FeatureGates = params.get("FeatureGates")
        self.Alias = params.get("Alias")
        self.Remark = params.get("Remark")


class ResourceDeleteOption(AbstractModel):
    """資源删除選項

    """

    def __init__(self):
        """
        :param ResourceType: 資源類型，例如CBS
        :type ResourceType: str
        :param DeleteMode: 集群删除時資源的删除模式：terminate（銷毀），retain （保留）
        :type DeleteMode: str
        """
        self.ResourceType = None
        self.DeleteMode = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.DeleteMode = params.get("DeleteMode")


class RouteInfo(AbstractModel):
    """集群路由對象

    """

    def __init__(self):
        """
        :param RouteTableName: 路由表名稱。
        :type RouteTableName: str
        :param DestinationCidrBlock: 目的端CIDR。
        :type DestinationCidrBlock: str
        :param GatewayIp: 下一跳網址。
        :type GatewayIp: str
        """
        self.RouteTableName = None
        self.DestinationCidrBlock = None
        self.GatewayIp = None


    def _deserialize(self, params):
        self.RouteTableName = params.get("RouteTableName")
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        self.GatewayIp = params.get("GatewayIp")


class RouteTableConflict(AbstractModel):
    """路由表沖突對象

    """

    def __init__(self):
        """
        :param RouteTableType: 路由表類型。
        :type RouteTableType: str
        :param RouteTableCidrBlock: 路由表CIDR。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RouteTableCidrBlock: str
        :param RouteTableName: 路由表名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RouteTableName: str
        :param RouteTableId: 路由表ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RouteTableId: str
        """
        self.RouteTableType = None
        self.RouteTableCidrBlock = None
        self.RouteTableName = None
        self.RouteTableId = None


    def _deserialize(self, params):
        self.RouteTableType = params.get("RouteTableType")
        self.RouteTableCidrBlock = params.get("RouteTableCidrBlock")
        self.RouteTableName = params.get("RouteTableName")
        self.RouteTableId = params.get("RouteTableId")


class RouteTableInfo(AbstractModel):
    """集群路由表對象

    """

    def __init__(self):
        """
        :param RouteTableName: 路由表名稱。
        :type RouteTableName: str
        :param RouteTableCidrBlock: 路由表CIDR。
        :type RouteTableCidrBlock: str
        :param VpcId: VPC實例ID。
        :type VpcId: str
        """
        self.RouteTableName = None
        self.RouteTableCidrBlock = None
        self.VpcId = None


    def _deserialize(self, params):
        self.RouteTableName = params.get("RouteTableName")
        self.RouteTableCidrBlock = params.get("RouteTableCidrBlock")
        self.VpcId = params.get("VpcId")


class RunInstancesForNode(AbstractModel):
    """不同角色的節點配置參數

    """

    def __init__(self):
        """
        :param NodeRole: 節點角色，取值:MASTER_ETCD, WORKER。MASTER_ETCD只有在創建 INDEPENDENT_CLUSTER 獨立集群時需要指定。MASTER_ETCD節點數量爲3～7，建議爲奇數。MASTER_ETCD節點最小配置爲4C8G。
        :type NodeRole: str
        :param RunInstancesPara: CVM創建透傳參數，json化字串格式，詳見[CVM創建實例](https://cloud.taifucloud.com/document/product/213/15730)介面，傳入公共參數外的其他參數即可，其中ImageId會替換爲TKE集群OS對應的映像。
        :type RunInstancesPara: list of str
        :param InstanceAdvancedSettingsOverrides: 節點高級設置，該參數會函蓋集群級别設置的InstanceAdvancedSettings，和上邊的RunInstancesPara按照順序一一對應（當前只對節點自定義參數ExtraArgs生效）。
        :type InstanceAdvancedSettingsOverrides: list of InstanceAdvancedSettings
        """
        self.NodeRole = None
        self.RunInstancesPara = None
        self.InstanceAdvancedSettingsOverrides = None


    def _deserialize(self, params):
        self.NodeRole = params.get("NodeRole")
        self.RunInstancesPara = params.get("RunInstancesPara")
        if params.get("InstanceAdvancedSettingsOverrides") is not None:
            self.InstanceAdvancedSettingsOverrides = []
            for item in params.get("InstanceAdvancedSettingsOverrides"):
                obj = InstanceAdvancedSettings()
                obj._deserialize(item)
                self.InstanceAdvancedSettingsOverrides.append(obj)


class RunMonitorServiceEnabled(AbstractModel):
    """描述了 “雲監控” 服務相關的訊息

    """

    def __init__(self):
        """
        :param Enabled: 是否開啓[雲監控](/document/product/248)服務。取值範圍：<br><li>TRUE：表示開啓雲監控服務<br><li>FALSE：表示不開啓雲監控服務<br><br>預設取值：TRUE。
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")


class RunSecurityServiceEnabled(AbstractModel):
    """描述了 “雲安全” 服務相關的訊息

    """

    def __init__(self):
        """
        :param Enabled: 是否開啓[雲安全](/document/product/296)服務。取值範圍：<br><li>TRUE：表示開啓雲安全服務<br><li>FALSE：表示不開啓雲安全服務<br><br>預設取值：TRUE。
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")


class Tag(AbstractModel):
    """標簽綁定的資源類型，當前支援類型："cluster"

    """

    def __init__(self):
        """
        :param Key: 標簽鍵
        :type Key: str
        :param Value: 標簽值
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class TagSpecification(AbstractModel):
    """標簽描述清單。通過指定該參數可以同時綁定標簽到相應的資源實例，當前僅支援綁定標簽到雲主機實例。

    """

    def __init__(self):
        """
        :param ResourceType: 標簽綁定的資源類型，當前支援類型："cluster"
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param Tags: 標簽對清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self.ResourceType = None
        self.Tags = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)