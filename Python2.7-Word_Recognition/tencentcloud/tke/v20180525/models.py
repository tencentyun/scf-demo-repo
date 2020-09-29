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
        """
        self.ClusterId = None
        self.InstanceIds = None
        self.InstanceAdvancedSettings = None
        self.EnhancedService = None
        self.LoginSettings = None
        self.SecurityGroupIds = None


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


class AddExistedInstancesResponse(AbstractModel):
    """AddExistedInstances返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


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


class ClusterAdvancedSettings(AbstractModel):
    """集群高級配置

    """

    def __init__(self):
        """
        :param IPVS: 是否啓用IPVS
        :type IPVS: bool
        :param AsEnabled: 是否啓用集群節點擴縮容
        :type AsEnabled: bool
        """
        self.IPVS = None
        self.AsEnabled = None


    def _deserialize(self, params):
        self.IPVS = params.get("IPVS")
        self.AsEnabled = params.get("AsEnabled")


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
        """
        self.ClusterOs = None
        self.ClusterVersion = None
        self.ClusterName = None
        self.ClusterDescription = None
        self.VpcId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.ClusterOs = params.get("ClusterOs")
        self.ClusterVersion = params.get("ClusterVersion")
        self.ClusterName = params.get("ClusterName")
        self.ClusterDescription = params.get("ClusterDescription")
        self.VpcId = params.get("VpcId")
        self.ProjectId = params.get("ProjectId")


class ClusterCIDRSettings(AbstractModel):
    """集群容器網絡相關參數

    """

    def __init__(self):
        """
        :param ClusterCIDR: 用於分配集群容器和服務 IP 的 CIDR，不得與 VPC CIDR 沖突，也不得與同 VPC 内其他集群 CIDR 沖突
        :type ClusterCIDR: str
        :param IgnoreClusterCIDRConflict: 是否忽略 ClusterCIDR 沖突錯誤, 預設不忽略
        :type IgnoreClusterCIDRConflict: bool
        :param MaxNodePodNum: 集群中每個Node上最大的Pod數量
        :type MaxNodePodNum: int
        :param MaxClusterServiceNum: 集群最大的service數量
        :type MaxClusterServiceNum: int
        """
        self.ClusterCIDR = None
        self.IgnoreClusterCIDRConflict = None
        self.MaxNodePodNum = None
        self.MaxClusterServiceNum = None


    def _deserialize(self, params):
        self.ClusterCIDR = params.get("ClusterCIDR")
        self.IgnoreClusterCIDRConflict = params.get("IgnoreClusterCIDRConflict")
        self.MaxNodePodNum = params.get("MaxNodePodNum")
        self.MaxClusterServiceNum = params.get("MaxClusterServiceNum")


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
        """
        self.ClusterCIDR = None
        self.IgnoreClusterCIDRConflict = None
        self.MaxNodePodNum = None
        self.MaxClusterServiceNum = None
        self.Ipvs = None
        self.VpcId = None


    def _deserialize(self, params):
        self.ClusterCIDR = params.get("ClusterCIDR")
        self.IgnoreClusterCIDRConflict = params.get("IgnoreClusterCIDRConflict")
        self.MaxNodePodNum = params.get("MaxNodePodNum")
        self.MaxClusterServiceNum = params.get("MaxClusterServiceNum")
        self.Ipvs = params.get("Ipvs")
        self.VpcId = params.get("VpcId")


class CreateClusterRequest(AbstractModel):
    """CreateCluster請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterCIDRSettings: 集群容器網絡配置訊息
        :type ClusterCIDRSettings: :class:`taifucloudcloud.tke.v20180525.models.ClusterCIDRSettings`
        :param ClusterType: 集群類型，托管集群：MANAGED_CLUSTER，獨立集群：INDEPENDENT_CLUSTER。
        :type ClusterType: str
        :param RunInstancesForNode: CVM創建透傳參數，json化字串格式，詳見[CVM創建實例](https://cloud.taifucloud.com/document/product/213/15730)介面。
        :type RunInstancesForNode: list of RunInstancesForNode
        :param ClusterBasicSettings: 集群的基本配置訊息
        :type ClusterBasicSettings: :class:`taifucloudcloud.tke.v20180525.models.ClusterBasicSettings`
        :param ClusterAdvancedSettings: 集群高級配置訊息
        :type ClusterAdvancedSettings: :class:`taifucloudcloud.tke.v20180525.models.ClusterAdvancedSettings`
        :param InstanceAdvancedSettings: 節點高級配置訊息
        :type InstanceAdvancedSettings: :class:`taifucloudcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param ExistedInstancesForNode: 已存在實例的配置訊息
        :type ExistedInstancesForNode: list of ExistedInstancesForNode
        """
        self.ClusterCIDRSettings = None
        self.ClusterType = None
        self.RunInstancesForNode = None
        self.ClusterBasicSettings = None
        self.ClusterAdvancedSettings = None
        self.InstanceAdvancedSettings = None
        self.ExistedInstancesForNode = None


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
        """
        self.ClusterId = None
        self.InstanceIds = None
        self.InstanceDeleteMode = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceDeleteMode = params.get("InstanceDeleteMode")


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


class DescribeClusterInstancesRequest(AbstractModel):
    """DescribeClusterInstances請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param Offset: 偏移量,預設0
        :type Offset: int
        :param Limit: 最大輸出條數，預設20
        :type Limit: int
        :param InstanceIds: 需要獲取的節點實例Id清單(預設爲空，表示拉取集群下所有節點實例)
        :type InstanceIds: list of str
        """
        self.ClusterId = None
        self.Offset = None
        self.Limit = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstanceIds = params.get("InstanceIds")


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
        :param Limit: 最大輸出條數，預設20
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


class ExistedInstancesForNode(AbstractModel):
    """不同角色的已存在節點配置參數

    """

    def __init__(self):
        """
        :param NodeRole: 節點角色，取值:MASTER_ETCD, WORKER。MASTER_ETCD只有在創建 INDEPENDENT_CLUSTER 獨立集群時需要指定。
        :type NodeRole: str
        :param ExistedInstancesPara: 已存在實例的重裝參數
        :type ExistedInstancesPara: :class:`taifucloudcloud.tke.v20180525.models.ExistedInstancesPara`
        """
        self.NodeRole = None
        self.ExistedInstancesPara = None


    def _deserialize(self, params):
        self.NodeRole = params.get("NodeRole")
        if params.get("ExistedInstancesPara") is not None:
            self.ExistedInstancesPara = ExistedInstancesPara()
            self.ExistedInstancesPara._deserialize(params.get("ExistedInstancesPara"))


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
        :param SecurityGroupIds: 實例所屬安全組。該參數可以通過調用 DescribeSecurityGroups 的返回值中的sgId欄位來獲取。若不指定該參數，則綁定預設安全組。（目前僅支援設置單個sgId）
        :type SecurityGroupIds: list of str
        """
        self.InstanceIds = None
        self.InstanceAdvancedSettings = None
        self.EnhancedService = None
        self.LoginSettings = None
        self.SecurityGroupIds = None


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


class Filter(AbstractModel):
    """過濾器

    """

    def __init__(self):
        """
        :param Name: 屬性名稱, 若存在多個Filter時，Filter間的關系爲邏輯與（AND）關系。
        :type Name: str
        :param Values: 屬性值, 若同一個Filter存在多個Values，同一Filter下Values間的關系爲邏輯或（OR）關系。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class Instance(AbstractModel):
    """集群的實例訊息

    """

    def __init__(self):
        """
        :param InstanceAdvanceSettings: 實例的附加訊息
        :type InstanceAdvanceSettings: :class:`taifucloudcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param InstanceRole: 節點角色, MASTER, WORKER, ETCD, MASTER_ETCD,ALL, 預設爲WORKER
        :type InstanceRole: str
        :param FailedReason: 實例異常(或者處於初始化中)的原因
        :type FailedReason: str
        :param InstanceState: 實例的狀态（running 運作中，initializing 初始化中，failed 異常）
        :type InstanceState: str
        """
        self.InstanceAdvanceSettings = None
        self.InstanceId = None
        self.InstanceRole = None
        self.FailedReason = None
        self.InstanceState = None


    def _deserialize(self, params):
        if params.get("InstanceAdvanceSettings") is not None:
            self.InstanceAdvanceSettings = InstanceAdvancedSettings()
            self.InstanceAdvanceSettings._deserialize(params.get("InstanceAdvanceSettings"))
        self.InstanceId = params.get("InstanceId")
        self.InstanceRole = params.get("InstanceRole")
        self.FailedReason = params.get("FailedReason")
        self.InstanceState = params.get("InstanceState")


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
        """
        self.MountTarget = None
        self.DockerGraphPath = None
        self.UserScript = None
        self.Unschedulable = None


    def _deserialize(self, params):
        self.MountTarget = params.get("MountTarget")
        self.DockerGraphPath = params.get("DockerGraphPath")
        self.UserScript = params.get("UserScript")
        self.Unschedulable = params.get("Unschedulable")


class LoginSettings(AbstractModel):
    """描述了實例登入相關配置與訊息。

    """

    def __init__(self):
        """
        :param Password: 實例登入密碼。不同作業系統類型密碼複雜度限制不一樣，具體如下：<br><li>Linux實例密碼必須8到16位，至少包括兩項[a-z，A-Z]、[0-9] 和 [( ) ` ~ ! @ # $ % ^ & * - + = | { } [ ] : ; ' , . ? / ]中的特殊符號。<br><li>Windows實例密碼必須12到16位，至少包括三項[a-z]，[A-Z]，[0-9] 和 [( ) ` ~ ! @ # $ % ^ & * - + = { } [ ] : ; ' , . ? /]中的特殊符號。<br><br>若不指定該參數，則由系統随機生成密碼，並通過站内信方式通知到用戶。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Password: str
        :param KeyIds: 金鑰ID清單。關聯金鑰後，就可以通過對應的私鑰來訪問實例；KeyId可通過介面DescribeKeyPairs獲取，金鑰與密碼不能同時指定，同時Windows作業系統不支援指定金鑰。當前僅支援購買的時候指定一個金鑰。
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


class RunInstancesForNode(AbstractModel):
    """不同角色的節點配置參數

    """

    def __init__(self):
        """
        :param NodeRole: 節點角色，取值:MASTER_ETCD, WORKER。MASTER_ETCD只有在創建 INDEPENDENT_CLUSTER 獨立集群時需要指定。
        :type NodeRole: str
        :param RunInstancesPara: CVM創建透傳參數，json化字串格式，詳見[CVM創建實例](https://cloud.taifucloud.com/document/product/213/15730)介面，傳入公共參數外的其他參數即可，其中ImageId會替換爲TKE集群OS對應的映像。
        :type RunInstancesPara: list of str
        """
        self.NodeRole = None
        self.RunInstancesPara = None


    def _deserialize(self, params):
        self.NodeRole = params.get("NodeRole")
        self.RunInstancesPara = params.get("RunInstancesPara")


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