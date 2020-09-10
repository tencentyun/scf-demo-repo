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


class Activity(AbstractModel):
    """計算環境的創建或銷毀活動

    """

    def __init__(self):
        """
        :param ActivityId: 活動ID
        :type ActivityId: str
        :param ComputeNodeId: 計算節點ID
        :type ComputeNodeId: str
        :param ComputeNodeActivityType: 計算節點活動類型，創建或者銷毀
        :type ComputeNodeActivityType: str
        :param EnvId: 計算環境ID
        :type EnvId: str
        :param Cause: 起因
        :type Cause: str
        :param ActivityState: 活動狀态
        :type ActivityState: str
        :param StateReason: 狀态原因
        :type StateReason: str
        :param StartTime: 活動開始時間
        :type StartTime: str
        :param EndTime: 活動結束時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param InstanceId: 雲伺服器實例ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceId: str
        """
        self.ActivityId = None
        self.ComputeNodeId = None
        self.ComputeNodeActivityType = None
        self.EnvId = None
        self.Cause = None
        self.ActivityState = None
        self.StateReason = None
        self.StartTime = None
        self.EndTime = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.ActivityId = params.get("ActivityId")
        self.ComputeNodeId = params.get("ComputeNodeId")
        self.ComputeNodeActivityType = params.get("ComputeNodeActivityType")
        self.EnvId = params.get("EnvId")
        self.Cause = params.get("Cause")
        self.ActivityState = params.get("ActivityState")
        self.StateReason = params.get("StateReason")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.InstanceId = params.get("InstanceId")


class AgentRunningMode(AbstractModel):
    """agent運作模式

    """

    def __init__(self):
        """
        :param Scene: 場景類型，支援WINDOWS
        :type Scene: str
        :param User: 運作Agent的User
        :type User: str
        :param Session: 運作Agent的Session
        :type Session: str
        """
        self.Scene = None
        self.User = None
        self.Session = None


    def _deserialize(self, params):
        self.Scene = params.get("Scene")
        self.User = params.get("User")
        self.Session = params.get("Session")


class AnonymousComputeEnv(AbstractModel):
    """計算環境

    """

    def __init__(self):
        """
        :param EnvType: 計算環境管理類型
        :type EnvType: str
        :param EnvData: 計算環境具體參數
        :type EnvData: :class:`taifucloudcloud.batch.v20170312.models.EnvData`
        :param MountDataDisks: 數據盤掛載選項
        :type MountDataDisks: list of MountDataDisk
        :param AgentRunningMode: agent運作模式，适用于Windows系統
        :type AgentRunningMode: :class:`taifucloudcloud.batch.v20170312.models.AgentRunningMode`
        """
        self.EnvType = None
        self.EnvData = None
        self.MountDataDisks = None
        self.AgentRunningMode = None


    def _deserialize(self, params):
        self.EnvType = params.get("EnvType")
        if params.get("EnvData") is not None:
            self.EnvData = EnvData()
            self.EnvData._deserialize(params.get("EnvData"))
        if params.get("MountDataDisks") is not None:
            self.MountDataDisks = []
            for item in params.get("MountDataDisks"):
                obj = MountDataDisk()
                obj._deserialize(item)
                self.MountDataDisks.append(obj)
        if params.get("AgentRunningMode") is not None:
            self.AgentRunningMode = AgentRunningMode()
            self.AgentRunningMode._deserialize(params.get("AgentRunningMode"))


class Application(AbstractModel):
    """應用程式訊息

    """

    def __init__(self):
        """
        :param Command: 任務執行命令
        :type Command: str
        :param DeliveryForm: 應用程式的交付方式，包括PACKAGE、LOCAL 兩種取值，分别指遠端儲存的軟體包、計算環境本地。
        :type DeliveryForm: str
        :param PackagePath: 應用程式軟體包的遠端儲存路徑
        :type PackagePath: str
        :param Docker: 應用使用Docker的相關配置。在使用Docker配置的情況下，DeliveryForm 爲 LOCAL 表示直接使用Docker映像内部的應用軟體，通過Docker方式運作；DeliveryForm 爲 PACKAGE，表示将遠端應用包注入到Docker映像後，通過Docker方式運作。爲避免Docker不同版本的相容性問題，Docker安裝包及相關依賴由Batch統一負責，對于已安裝Docker的自定義映像，請卸載後再使用Docker特性。
        :type Docker: :class:`taifucloudcloud.batch.v20170312.models.Docker`
        """
        self.Command = None
        self.DeliveryForm = None
        self.PackagePath = None
        self.Docker = None


    def _deserialize(self, params):
        self.Command = params.get("Command")
        self.DeliveryForm = params.get("DeliveryForm")
        self.PackagePath = params.get("PackagePath")
        if params.get("Docker") is not None:
            self.Docker = Docker()
            self.Docker._deserialize(params.get("Docker"))


class AttachInstancesRequest(AbstractModel):
    """AttachInstances請求參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 計算環境ID
        :type EnvId: str
        :param Instances: 加入計算環境實例清單
        :type Instances: list of Instance
        """
        self.EnvId = None
        self.Instances = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = Instance()
                obj._deserialize(item)
                self.Instances.append(obj)


class AttachInstancesResponse(AbstractModel):
    """AttachInstances返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Authentication(AbstractModel):
    """授權認證訊息

    """

    def __init__(self):
        """
        :param Scene: 授權場景，例如COS
        :type Scene: str
        :param SecretId: SecretId
        :type SecretId: str
        :param SecretKey: SecretKey
        :type SecretKey: str
        """
        self.Scene = None
        self.SecretId = None
        self.SecretKey = None


    def _deserialize(self, params):
        self.Scene = params.get("Scene")
        self.SecretId = params.get("SecretId")
        self.SecretKey = params.get("SecretKey")


class ComputeEnvCreateInfo(AbstractModel):
    """計算環境創建訊息。

    """

    def __init__(self):
        """
        :param EnvId: 計算環境 ID
        :type EnvId: str
        :param EnvName: 計算環境名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type EnvName: str
        :param EnvDescription: 計算環境描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type EnvDescription: str
        :param EnvType: 計算環境類型，僅支援“MANAGED”類型
        :type EnvType: str
        :param EnvData: 計算環境參數
        :type EnvData: :class:`taifucloudcloud.batch.v20170312.models.EnvData`
        :param MountDataDisks: 數據盤掛載選項
注意：此欄位可能返回 null，表示取不到有效值。
        :type MountDataDisks: list of MountDataDisk
        :param InputMappings: 輸入映射
注意：此欄位可能返回 null，表示取不到有效值。
        :type InputMappings: list of InputMapping
        :param Authentications: 授權訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Authentications: list of Authentication
        :param Notifications: 通知訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Notifications: list of Notification
        :param DesiredComputeNodeCount: 計算節點期望個數
        :type DesiredComputeNodeCount: int
        """
        self.EnvId = None
        self.EnvName = None
        self.EnvDescription = None
        self.EnvType = None
        self.EnvData = None
        self.MountDataDisks = None
        self.InputMappings = None
        self.Authentications = None
        self.Notifications = None
        self.DesiredComputeNodeCount = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.EnvName = params.get("EnvName")
        self.EnvDescription = params.get("EnvDescription")
        self.EnvType = params.get("EnvType")
        if params.get("EnvData") is not None:
            self.EnvData = EnvData()
            self.EnvData._deserialize(params.get("EnvData"))
        if params.get("MountDataDisks") is not None:
            self.MountDataDisks = []
            for item in params.get("MountDataDisks"):
                obj = MountDataDisk()
                obj._deserialize(item)
                self.MountDataDisks.append(obj)
        if params.get("InputMappings") is not None:
            self.InputMappings = []
            for item in params.get("InputMappings"):
                obj = InputMapping()
                obj._deserialize(item)
                self.InputMappings.append(obj)
        if params.get("Authentications") is not None:
            self.Authentications = []
            for item in params.get("Authentications"):
                obj = Authentication()
                obj._deserialize(item)
                self.Authentications.append(obj)
        if params.get("Notifications") is not None:
            self.Notifications = []
            for item in params.get("Notifications"):
                obj = Notification()
                obj._deserialize(item)
                self.Notifications.append(obj)
        self.DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")


class ComputeEnvData(AbstractModel):
    """計算環境屬性數據

    """

    def __init__(self):
        """
        :param InstanceTypes: CVM實例類型清單
        :type InstanceTypes: list of str
        """
        self.InstanceTypes = None


    def _deserialize(self, params):
        self.InstanceTypes = params.get("InstanceTypes")


class ComputeEnvView(AbstractModel):
    """計算環境訊息

    """

    def __init__(self):
        """
        :param EnvId: 計算環境ID
        :type EnvId: str
        :param EnvName: 計算環境名稱
        :type EnvName: str
        :param Placement: 位置訊息
        :type Placement: :class:`taifucloudcloud.batch.v20170312.models.Placement`
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param ComputeNodeMetrics: 計算節點統計指标
        :type ComputeNodeMetrics: :class:`taifucloudcloud.batch.v20170312.models.ComputeNodeMetrics`
        :param EnvType: 計算環境類型
        :type EnvType: str
        :param DesiredComputeNodeCount: 計算節點期望個數
        :type DesiredComputeNodeCount: int
        :param ResourceType: 計算環境資源類型，當前爲CVM和CPM（黑石）
        :type ResourceType: str
        :param NextAction: 下一步動作
        :type NextAction: str
        :param AttachedComputeNodeCount: 用戶添加到計算環境中的計算節點個數
        :type AttachedComputeNodeCount: int
        """
        self.EnvId = None
        self.EnvName = None
        self.Placement = None
        self.CreateTime = None
        self.ComputeNodeMetrics = None
        self.EnvType = None
        self.DesiredComputeNodeCount = None
        self.ResourceType = None
        self.NextAction = None
        self.AttachedComputeNodeCount = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.EnvName = params.get("EnvName")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.CreateTime = params.get("CreateTime")
        if params.get("ComputeNodeMetrics") is not None:
            self.ComputeNodeMetrics = ComputeNodeMetrics()
            self.ComputeNodeMetrics._deserialize(params.get("ComputeNodeMetrics"))
        self.EnvType = params.get("EnvType")
        self.DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
        self.ResourceType = params.get("ResourceType")
        self.NextAction = params.get("NextAction")
        self.AttachedComputeNodeCount = params.get("AttachedComputeNodeCount")


class ComputeNode(AbstractModel):
    """計算節點

    """

    def __init__(self):
        """
        :param ComputeNodeId: 計算節點ID
        :type ComputeNodeId: str
        :param ComputeNodeInstanceId: 計算節點實例ID，對于CVM場景，即爲CVM的InstanceId
        :type ComputeNodeInstanceId: str
        :param ComputeNodeState: 計算節點狀态
        :type ComputeNodeState: str
        :param Cpu: CPU核數
        :type Cpu: int
        :param Mem: 内存容量，單位GiB
        :type Mem: int
        :param ResourceCreatedTime: 資源創建完成時間
        :type ResourceCreatedTime: str
        :param TaskInstanceNumAvailable: 計算節點運作  TaskInstance 可用容量。0表示計算節點忙碌。
        :type TaskInstanceNumAvailable: int
        :param AgentVersion: Batch Agent 版本
        :type AgentVersion: str
        :param PrivateIpAddresses: 實例内網IP
        :type PrivateIpAddresses: list of str
        :param PublicIpAddresses: 實例公網IP
        :type PublicIpAddresses: list of str
        :param ResourceType: 計算環境資源類型，當前爲CVM和CPM（黑石）
        :type ResourceType: str
        :param ResourceOrigin: 計算環境資源來源。<br>BATCH_CREATED：由批次計算創建的實例資源。<br>
USER_ATTACHED：用戶添加到計算環境中的實例資源。
        :type ResourceOrigin: str
        """
        self.ComputeNodeId = None
        self.ComputeNodeInstanceId = None
        self.ComputeNodeState = None
        self.Cpu = None
        self.Mem = None
        self.ResourceCreatedTime = None
        self.TaskInstanceNumAvailable = None
        self.AgentVersion = None
        self.PrivateIpAddresses = None
        self.PublicIpAddresses = None
        self.ResourceType = None
        self.ResourceOrigin = None


    def _deserialize(self, params):
        self.ComputeNodeId = params.get("ComputeNodeId")
        self.ComputeNodeInstanceId = params.get("ComputeNodeInstanceId")
        self.ComputeNodeState = params.get("ComputeNodeState")
        self.Cpu = params.get("Cpu")
        self.Mem = params.get("Mem")
        self.ResourceCreatedTime = params.get("ResourceCreatedTime")
        self.TaskInstanceNumAvailable = params.get("TaskInstanceNumAvailable")
        self.AgentVersion = params.get("AgentVersion")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.ResourceType = params.get("ResourceType")
        self.ResourceOrigin = params.get("ResourceOrigin")


class ComputeNodeMetrics(AbstractModel):
    """計算節點統計指标

    """

    def __init__(self):
        """
        :param SubmittedCount: 已經完成提交的計算節點數量
        :type SubmittedCount: int
        :param CreatingCount: 創建中的計算節點數量
        :type CreatingCount: int
        :param CreationFailedCount: 創建失敗的計算節點數量
        :type CreationFailedCount: int
        :param CreatedCount: 完成創建的計算節點數量
        :type CreatedCount: int
        :param RunningCount: 運作中的計算節點數量
        :type RunningCount: int
        :param DeletingCount: 銷毀中的計算節點數量
        :type DeletingCount: int
        :param AbnormalCount: 異常的計算節點數量
        :type AbnormalCount: int
        """
        self.SubmittedCount = None
        self.CreatingCount = None
        self.CreationFailedCount = None
        self.CreatedCount = None
        self.RunningCount = None
        self.DeletingCount = None
        self.AbnormalCount = None


    def _deserialize(self, params):
        self.SubmittedCount = params.get("SubmittedCount")
        self.CreatingCount = params.get("CreatingCount")
        self.CreationFailedCount = params.get("CreationFailedCount")
        self.CreatedCount = params.get("CreatedCount")
        self.RunningCount = params.get("RunningCount")
        self.DeletingCount = params.get("DeletingCount")
        self.AbnormalCount = params.get("AbnormalCount")


class CpmVirtualPrivateCloud(AbstractModel):
    """黑石私有網絡

    """

    def __init__(self):
        """
        :param VpcId: 黑石私有網絡ID
        :type VpcId: str
        :param SubnetId: 黑石子網ID
        :type SubnetId: str
        """
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")


class CreateComputeEnvRequest(AbstractModel):
    """CreateComputeEnv請求參數結構體

    """

    def __init__(self):
        """
        :param ComputeEnv: 計算環境訊息
        :type ComputeEnv: :class:`taifucloudcloud.batch.v20170312.models.NamedComputeEnv`
        :param Placement: 位置訊息
        :type Placement: :class:`taifucloudcloud.batch.v20170312.models.Placement`
        :param ClientToken: 用于保證請求幂等性的字串。該字串由用戶生成，需保證不同請求之間唯一，最大值不超過64個ASCII字元。若不指定該參數，則無法保證請求的幂等性。
        :type ClientToken: str
        """
        self.ComputeEnv = None
        self.Placement = None
        self.ClientToken = None


    def _deserialize(self, params):
        if params.get("ComputeEnv") is not None:
            self.ComputeEnv = NamedComputeEnv()
            self.ComputeEnv._deserialize(params.get("ComputeEnv"))
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.ClientToken = params.get("ClientToken")


class CreateComputeEnvResponse(AbstractModel):
    """CreateComputeEnv返回參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 計算環境ID
        :type EnvId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.EnvId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.RequestId = params.get("RequestId")


class CreateCpmComputeEnvRequest(AbstractModel):
    """CreateCpmComputeEnv請求參數結構體

    """

    def __init__(self):
        """
        :param ComputeEnv: 計算環境訊息
        :type ComputeEnv: :class:`taifucloudcloud.batch.v20170312.models.NamedCpmComputeEnv`
        :param Placement: 位置訊息
        :type Placement: :class:`taifucloudcloud.batch.v20170312.models.Placement`
        :param ClientToken: 用于保證請求幂等性的字串。該字串由用戶生成，需保證不同請求之間唯一，最大值不超過64個ASCII字元。若不指定該參數，則無法保證請求的幂等性。
        :type ClientToken: str
        """
        self.ComputeEnv = None
        self.Placement = None
        self.ClientToken = None


    def _deserialize(self, params):
        if params.get("ComputeEnv") is not None:
            self.ComputeEnv = NamedCpmComputeEnv()
            self.ComputeEnv._deserialize(params.get("ComputeEnv"))
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.ClientToken = params.get("ClientToken")


class CreateCpmComputeEnvResponse(AbstractModel):
    """CreateCpmComputeEnv返回參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 計算環境ID
        :type EnvId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.EnvId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.RequestId = params.get("RequestId")


class CreateTaskTemplateRequest(AbstractModel):
    """CreateTaskTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param TaskTemplateName: 任務範本名稱
        :type TaskTemplateName: str
        :param TaskTemplateInfo: 任務範本内容，參數要求與任務一緻
        :type TaskTemplateInfo: :class:`taifucloudcloud.batch.v20170312.models.Task`
        :param TaskTemplateDescription: 任務範本描述
        :type TaskTemplateDescription: str
        """
        self.TaskTemplateName = None
        self.TaskTemplateInfo = None
        self.TaskTemplateDescription = None


    def _deserialize(self, params):
        self.TaskTemplateName = params.get("TaskTemplateName")
        if params.get("TaskTemplateInfo") is not None:
            self.TaskTemplateInfo = Task()
            self.TaskTemplateInfo._deserialize(params.get("TaskTemplateInfo"))
        self.TaskTemplateDescription = params.get("TaskTemplateDescription")


class CreateTaskTemplateResponse(AbstractModel):
    """CreateTaskTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param TaskTemplateId: 任務範本ID
        :type TaskTemplateId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskTemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskTemplateId = params.get("TaskTemplateId")
        self.RequestId = params.get("RequestId")


class DataDisk(AbstractModel):
    """描述了數據盤的訊息

    """

    def __init__(self):
        """
        :param DiskSize: 數據盤大小，單位：GB。最小調整步長爲10G，不同數據盤類型取值範圍不同，具體限制詳見：[儲存概述](https://cloud.taifucloud.com/document/product/213/4952)。預設值爲0，表示不購買數據盤。更多限制詳見産品文件。
        :type DiskSize: int
        :param DiskType: 數據盤類型。數據盤類型限制詳見[儲存概述](https://cloud.taifucloud.com/document/product/213/4952)。取值範圍：<br><li>LOCAL_BASIC：本地硬碟<br><li>LOCAL_SSD：本地SSD硬碟<br><li>CLOUD_BASIC：普通雲硬碟<br><li>CLOUD_PREMIUM：高效能雲硬碟<br><li>CLOUD_SSD：SSD雲硬碟<br><br>預設取值：LOCAL_BASIC。<br><br>該參數對`ResizeInstanceDisk`介面無效。
        :type DiskType: str
        :param DiskId: 數據盤ID。LOCAL_BASIC 和 LOCAL_SSD 類型沒有ID，暫時不支援該參數。
        :type DiskId: str
        :param DeleteWithInstance: 數據盤是否随子機銷毀。取值範圍：
<li>TRUE：子機銷毀時，銷毀數據盤，只支援按小時後付費雲盤
<li>FALSE：子機銷毀時，保留數據盤<br>
預設取值：TRUE<br>
該參數目前僅用于 `RunInstances` 介面。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeleteWithInstance: bool
        :param SnapshotId: 數據盤快照ID。選擇的數據盤快照大小需小於數據盤大小。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SnapshotId: str
        :param Encrypt: 數據盤是加密。取值範圍：
<li>TRUE：加密
<li>FALSE：不加密<br>
預設取值：FALSE<br>
該參數目前僅用于 `RunInstances` 介面。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Encrypt: bool
        """
        self.DiskSize = None
        self.DiskType = None
        self.DiskId = None
        self.DeleteWithInstance = None
        self.SnapshotId = None
        self.Encrypt = None


    def _deserialize(self, params):
        self.DiskSize = params.get("DiskSize")
        self.DiskType = params.get("DiskType")
        self.DiskId = params.get("DiskId")
        self.DeleteWithInstance = params.get("DeleteWithInstance")
        self.SnapshotId = params.get("SnapshotId")
        self.Encrypt = params.get("Encrypt")


class DeleteComputeEnvRequest(AbstractModel):
    """DeleteComputeEnv請求參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 計算環境ID
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")


class DeleteComputeEnvResponse(AbstractModel):
    """DeleteComputeEnv返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteJobRequest(AbstractModel):
    """DeleteJob請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 作業ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class DeleteJobResponse(AbstractModel):
    """DeleteJob返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTaskTemplatesRequest(AbstractModel):
    """DeleteTaskTemplates請求參數結構體

    """

    def __init__(self):
        """
        :param TaskTemplateIds: 用于删除任務範本訊息
        :type TaskTemplateIds: list of str
        """
        self.TaskTemplateIds = None


    def _deserialize(self, params):
        self.TaskTemplateIds = params.get("TaskTemplateIds")


class DeleteTaskTemplatesResponse(AbstractModel):
    """DeleteTaskTemplates返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Dependence(AbstractModel):
    """依賴關系

    """

    def __init__(self):
        """
        :param StartTask: 依賴關系的起點任務名稱
        :type StartTask: str
        :param EndTask: 依賴關系的終點任務名稱
        :type EndTask: str
        """
        self.StartTask = None
        self.EndTask = None


    def _deserialize(self, params):
        self.StartTask = params.get("StartTask")
        self.EndTask = params.get("EndTask")


class DescribeAvailableCvmInstanceTypesRequest(AbstractModel):
    """DescribeAvailableCvmInstanceTypes請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 過濾條件。
<li> zone - String - 是否必填：否 -（過濾條件）按照可用區過濾。</li>
<li> instance-family String - 是否必填：否 -（過濾條件）按照機型系列過濾。實例機型系列形如：S1、I1、M1等。</li>
        :type Filters: list of Filter
        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeAvailableCvmInstanceTypesResponse(AbstractModel):
    """DescribeAvailableCvmInstanceTypes返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceTypeConfigSet: 機型配置數組
        :type InstanceTypeConfigSet: list of InstanceTypeConfig
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceTypeConfigSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceTypeConfigSet") is not None:
            self.InstanceTypeConfigSet = []
            for item in params.get("InstanceTypeConfigSet"):
                obj = InstanceTypeConfig()
                obj._deserialize(item)
                self.InstanceTypeConfigSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeComputeEnvActivitiesRequest(AbstractModel):
    """DescribeComputeEnvActivities請求參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 計算環境ID
        :type EnvId: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回數量
        :type Limit: int
        :param Filters: 過濾條件
<li> compute-node-id - String - 是否必填：否 -（過濾條件）按照計算節點ID過濾。</li>
        :type Filters: :class:`taifucloudcloud.batch.v20170312.models.Filter`
        """
        self.EnvId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = Filter()
            self.Filters._deserialize(params.get("Filters"))


class DescribeComputeEnvActivitiesResponse(AbstractModel):
    """DescribeComputeEnvActivities返回參數結構體

    """

    def __init__(self):
        """
        :param ActivitySet: 計算環境中的活動清單
        :type ActivitySet: list of Activity
        :param TotalCount: 活動數量
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ActivitySet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ActivitySet") is not None:
            self.ActivitySet = []
            for item in params.get("ActivitySet"):
                obj = Activity()
                obj._deserialize(item)
                self.ActivitySet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeComputeEnvCreateInfoRequest(AbstractModel):
    """DescribeComputeEnvCreateInfo請求參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 計算環境ID
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")


class DescribeComputeEnvCreateInfoResponse(AbstractModel):
    """DescribeComputeEnvCreateInfo返回參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 計算環境 ID
        :type EnvId: str
        :param EnvName: 計算環境名稱
        :type EnvName: str
        :param EnvDescription: 計算環境描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type EnvDescription: str
        :param EnvType: 計算環境類型，僅支援“MANAGED”類型
        :type EnvType: str
        :param EnvData: 計算環境參數
        :type EnvData: :class:`taifucloudcloud.batch.v20170312.models.EnvData`
        :param MountDataDisks: 數據盤掛載選項
        :type MountDataDisks: list of MountDataDisk
        :param InputMappings: 輸入映射
        :type InputMappings: list of InputMapping
        :param Authentications: 授權訊息
        :type Authentications: list of Authentication
        :param Notifications: 通知訊息
        :type Notifications: list of Notification
        :param DesiredComputeNodeCount: 計算節點期望個數
        :type DesiredComputeNodeCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.EnvId = None
        self.EnvName = None
        self.EnvDescription = None
        self.EnvType = None
        self.EnvData = None
        self.MountDataDisks = None
        self.InputMappings = None
        self.Authentications = None
        self.Notifications = None
        self.DesiredComputeNodeCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.EnvName = params.get("EnvName")
        self.EnvDescription = params.get("EnvDescription")
        self.EnvType = params.get("EnvType")
        if params.get("EnvData") is not None:
            self.EnvData = EnvData()
            self.EnvData._deserialize(params.get("EnvData"))
        if params.get("MountDataDisks") is not None:
            self.MountDataDisks = []
            for item in params.get("MountDataDisks"):
                obj = MountDataDisk()
                obj._deserialize(item)
                self.MountDataDisks.append(obj)
        if params.get("InputMappings") is not None:
            self.InputMappings = []
            for item in params.get("InputMappings"):
                obj = InputMapping()
                obj._deserialize(item)
                self.InputMappings.append(obj)
        if params.get("Authentications") is not None:
            self.Authentications = []
            for item in params.get("Authentications"):
                obj = Authentication()
                obj._deserialize(item)
                self.Authentications.append(obj)
        if params.get("Notifications") is not None:
            self.Notifications = []
            for item in params.get("Notifications"):
                obj = Notification()
                obj._deserialize(item)
                self.Notifications.append(obj)
        self.DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
        self.RequestId = params.get("RequestId")


class DescribeComputeEnvCreateInfosRequest(AbstractModel):
    """DescribeComputeEnvCreateInfos請求參數結構體

    """

    def __init__(self):
        """
        :param EnvIds: 計算環境ID清單，與Filters參數不能同時指定。
        :type EnvIds: list of str
        :param Filters: 過濾條件
<li> zone - String - 是否必填：否 -（過濾條件）按照可用區過濾。</li>
<li> env-id - String - 是否必填：否 -（過濾條件）按照計算環境ID過濾。</li>
<li> env-name - String - 是否必填：否 -（過濾條件）按照計算環境名稱過濾。</li>
與EnvIds參數不能同時指定。
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回數量
        :type Limit: int
        """
        self.EnvIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.EnvIds = params.get("EnvIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeComputeEnvCreateInfosResponse(AbstractModel):
    """DescribeComputeEnvCreateInfos返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 計算環境數量
        :type TotalCount: int
        :param ComputeEnvCreateInfoSet: 計算環境創建訊息清單
        :type ComputeEnvCreateInfoSet: list of ComputeEnvCreateInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ComputeEnvCreateInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ComputeEnvCreateInfoSet") is not None:
            self.ComputeEnvCreateInfoSet = []
            for item in params.get("ComputeEnvCreateInfoSet"):
                obj = ComputeEnvCreateInfo()
                obj._deserialize(item)
                self.ComputeEnvCreateInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeComputeEnvRequest(AbstractModel):
    """DescribeComputeEnv請求參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 計算環境ID
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")


class DescribeComputeEnvResponse(AbstractModel):
    """DescribeComputeEnv返回參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 計算環境ID
        :type EnvId: str
        :param EnvName: 計算環境名稱
        :type EnvName: str
        :param Placement: 位置訊息
        :type Placement: :class:`taifucloudcloud.batch.v20170312.models.Placement`
        :param CreateTime: 計算環境創建時間
        :type CreateTime: str
        :param ComputeNodeSet: 計算節點清單訊息
        :type ComputeNodeSet: list of ComputeNode
        :param ComputeNodeMetrics: 計算節點統計指标
        :type ComputeNodeMetrics: :class:`taifucloudcloud.batch.v20170312.models.ComputeNodeMetrics`
        :param DesiredComputeNodeCount: 計算節點期望個數
        :type DesiredComputeNodeCount: int
        :param EnvType: 計算環境類型
        :type EnvType: str
        :param ResourceType: 計算環境資源類型，當前爲CVM和CPM（黑石）
        :type ResourceType: str
        :param NextAction: 下一步動作
        :type NextAction: str
        :param AttachedComputeNodeCount: 用戶添加到計算環境中的計算節點個數
        :type AttachedComputeNodeCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.EnvId = None
        self.EnvName = None
        self.Placement = None
        self.CreateTime = None
        self.ComputeNodeSet = None
        self.ComputeNodeMetrics = None
        self.DesiredComputeNodeCount = None
        self.EnvType = None
        self.ResourceType = None
        self.NextAction = None
        self.AttachedComputeNodeCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.EnvName = params.get("EnvName")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.CreateTime = params.get("CreateTime")
        if params.get("ComputeNodeSet") is not None:
            self.ComputeNodeSet = []
            for item in params.get("ComputeNodeSet"):
                obj = ComputeNode()
                obj._deserialize(item)
                self.ComputeNodeSet.append(obj)
        if params.get("ComputeNodeMetrics") is not None:
            self.ComputeNodeMetrics = ComputeNodeMetrics()
            self.ComputeNodeMetrics._deserialize(params.get("ComputeNodeMetrics"))
        self.DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
        self.EnvType = params.get("EnvType")
        self.ResourceType = params.get("ResourceType")
        self.NextAction = params.get("NextAction")
        self.AttachedComputeNodeCount = params.get("AttachedComputeNodeCount")
        self.RequestId = params.get("RequestId")


class DescribeComputeEnvsRequest(AbstractModel):
    """DescribeComputeEnvs請求參數結構體

    """

    def __init__(self):
        """
        :param EnvIds: 計算環境ID清單，與Filters參數不能同時指定。
        :type EnvIds: list of str
        :param Filters: 過濾條件
<li> zone - String - 是否必填：否 -（過濾條件）按照可用區過濾。</li>
<li> env-id - String - 是否必填：否 -（過濾條件）按照計算環境ID過濾。</li>
<li> env-name - String - 是否必填：否 -（過濾條件）按照計算環境名稱過濾。</li>
<li> resource-type - String - 是否必填：否 -（過濾條件）按照計算資源類型過濾，取值CVM或者CPM(黑石)。</li>
與EnvIds參數不能同時指定。
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回數量
        :type Limit: int
        """
        self.EnvIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.EnvIds = params.get("EnvIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeComputeEnvsResponse(AbstractModel):
    """DescribeComputeEnvs返回參數結構體

    """

    def __init__(self):
        """
        :param ComputeEnvSet: 計算環境清單
        :type ComputeEnvSet: list of ComputeEnvView
        :param TotalCount: 計算環境數量
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ComputeEnvSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ComputeEnvSet") is not None:
            self.ComputeEnvSet = []
            for item in params.get("ComputeEnvSet"):
                obj = ComputeEnvView()
                obj._deserialize(item)
                self.ComputeEnvSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCpmOsInfoRequest(AbstractModel):
    """DescribeCpmOsInfo請求參數結構體

    """

    def __init__(self):
        """
        :param DeviceClassCode: 黑石設備類型代号。 可以從[DescribeDeviceClass](https://cloud.taifucloud.com/document/api/386/32911)查詢設備類型清單。
        :type DeviceClassCode: str
        """
        self.DeviceClassCode = None


    def _deserialize(self, params):
        self.DeviceClassCode = params.get("DeviceClassCode")


class DescribeCpmOsInfoResponse(AbstractModel):
    """DescribeCpmOsInfo返回參數結構體

    """

    def __init__(self):
        """
        :param OsInfoSet: 作業系統訊息清單。
        :type OsInfoSet: list of OsInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.OsInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("OsInfoSet") is not None:
            self.OsInfoSet = []
            for item in params.get("OsInfoSet"):
                obj = OsInfo()
                obj._deserialize(item)
                self.OsInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCvmZoneInstanceConfigInfosRequest(AbstractModel):
    """DescribeCvmZoneInstanceConfigInfos請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 過濾條件。
<li> zone - String - 是否必填：否 -（過濾條件）按照可用區過濾。</li>
<li> instance-family String - 是否必填：否 -（過濾條件）按照機型系列過濾。實例機型系列形如：S1、I1、M1等。</li>
<li> instance-type - String - 是否必填：否 - （過濾條件）按照機型過濾。</li>
<li> instance-charge-type - String - 是否必填：否 -（過濾條件）按照實例計費模式過濾。 ( POSTPAID_BY_HOUR：表示後付費，即按量計費機型 | SPOTPAID：表示競價付費機型。 )  </li>
        :type Filters: list of Filter
        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeCvmZoneInstanceConfigInfosResponse(AbstractModel):
    """DescribeCvmZoneInstanceConfigInfos返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceTypeQuotaSet: 可用區機型配置清單。
        :type InstanceTypeQuotaSet: list of InstanceTypeQuotaItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceTypeQuotaSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceTypeQuotaSet") is not None:
            self.InstanceTypeQuotaSet = []
            for item in params.get("InstanceTypeQuotaSet"):
                obj = InstanceTypeQuotaItem()
                obj._deserialize(item)
                self.InstanceTypeQuotaSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceCategoriesRequest(AbstractModel):
    """DescribeInstanceCategories請求參數結構體

    """


class DescribeInstanceCategoriesResponse(AbstractModel):
    """DescribeInstanceCategories返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceCategorySet: CVM實例分類清單
        :type InstanceCategorySet: list of InstanceCategoryItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceCategorySet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceCategorySet") is not None:
            self.InstanceCategorySet = []
            for item in params.get("InstanceCategorySet"):
                obj = InstanceCategoryItem()
                obj._deserialize(item)
                self.InstanceCategorySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeJobRequest(AbstractModel):
    """DescribeJob請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 作業标識
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class DescribeJobResponse(AbstractModel):
    """DescribeJob返回參數結構體

    """

    def __init__(self):
        """
        :param JobId: 作業ID
        :type JobId: str
        :param JobName: 作業名稱
        :type JobName: str
        :param Zone: 可用區訊息
        :type Zone: str
        :param Priority: 作業優先級
        :type Priority: int
        :param JobState: 作業狀态
        :type JobState: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param EndTime: 結束時間
        :type EndTime: str
        :param TaskSet: 任務視圖訊息
        :type TaskSet: list of TaskView
        :param DependenceSet: 任務間依賴訊息
        :type DependenceSet: list of Dependence
        :param TaskMetrics: 任務統計指标
        :type TaskMetrics: :class:`taifucloudcloud.batch.v20170312.models.TaskMetrics`
        :param TaskInstanceMetrics: 任務實例統計指标
        :type TaskInstanceMetrics: :class:`taifucloudcloud.batch.v20170312.models.TaskInstanceView`
        :param StateReason: 作業失敗原因
        :type StateReason: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.JobName = None
        self.Zone = None
        self.Priority = None
        self.JobState = None
        self.CreateTime = None
        self.EndTime = None
        self.TaskSet = None
        self.DependenceSet = None
        self.TaskMetrics = None
        self.TaskInstanceMetrics = None
        self.StateReason = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.Zone = params.get("Zone")
        self.Priority = params.get("Priority")
        self.JobState = params.get("JobState")
        self.CreateTime = params.get("CreateTime")
        self.EndTime = params.get("EndTime")
        if params.get("TaskSet") is not None:
            self.TaskSet = []
            for item in params.get("TaskSet"):
                obj = TaskView()
                obj._deserialize(item)
                self.TaskSet.append(obj)
        if params.get("DependenceSet") is not None:
            self.DependenceSet = []
            for item in params.get("DependenceSet"):
                obj = Dependence()
                obj._deserialize(item)
                self.DependenceSet.append(obj)
        if params.get("TaskMetrics") is not None:
            self.TaskMetrics = TaskMetrics()
            self.TaskMetrics._deserialize(params.get("TaskMetrics"))
        if params.get("TaskInstanceMetrics") is not None:
            self.TaskInstanceMetrics = TaskInstanceView()
            self.TaskInstanceMetrics._deserialize(params.get("TaskInstanceMetrics"))
        self.StateReason = params.get("StateReason")
        self.RequestId = params.get("RequestId")


class DescribeJobSubmitInfoRequest(AbstractModel):
    """DescribeJobSubmitInfo請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 作業ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class DescribeJobSubmitInfoResponse(AbstractModel):
    """DescribeJobSubmitInfo返回參數結構體

    """

    def __init__(self):
        """
        :param JobId: 作業ID
        :type JobId: str
        :param JobName: 作業名稱
        :type JobName: str
        :param JobDescription: 作業描述
        :type JobDescription: str
        :param Priority: 作業優先級，任務（Task）和任務實例（TaskInstance）會繼承作業優先級
        :type Priority: int
        :param Tasks: 任務訊息
        :type Tasks: list of Task
        :param Dependences: 依賴訊息
        :type Dependences: list of Dependence
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.JobName = None
        self.JobDescription = None
        self.Priority = None
        self.Tasks = None
        self.Dependences = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.JobDescription = params.get("JobDescription")
        self.Priority = params.get("Priority")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self.Tasks.append(obj)
        if params.get("Dependences") is not None:
            self.Dependences = []
            for item in params.get("Dependences"):
                obj = Dependence()
                obj._deserialize(item)
                self.Dependences.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeJobsRequest(AbstractModel):
    """DescribeJobs請求參數結構體

    """

    def __init__(self):
        """
        :param JobIds: 作業ID清單，與Filters參數不能同時指定。
        :type JobIds: list of str
        :param Filters: 過濾條件
<li> job-id - String - 是否必填：否 -（過濾條件）按照作業ID過濾。</li>
<li> job-name - String - 是否必填：否 -（過濾條件）按照作業名稱過濾。</li>
<li> job-state - String - 是否必填：否 -（過濾條件）按照作業狀态過濾。</li>
<li> zone - String - 是否必填：否 -（過濾條件）按照可用區過濾。</li>
與JobIds參數不能同時指定。
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回數量
        :type Limit: int
        """
        self.JobIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.JobIds = params.get("JobIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeJobsResponse(AbstractModel):
    """DescribeJobs返回參數結構體

    """

    def __init__(self):
        """
        :param JobSet: 作業清單
        :type JobSet: list of JobView
        :param TotalCount: 符合條件的作業數量
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.JobSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("JobSet") is not None:
            self.JobSet = []
            for item in params.get("JobSet"):
                obj = JobView()
                obj._deserialize(item)
                self.JobSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTaskLogsRequest(AbstractModel):
    """DescribeTaskLogs請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 作業ID
        :type JobId: str
        :param TaskName: 任務名稱
        :type TaskName: str
        :param TaskInstanceIndexes: 任務實例集合
        :type TaskInstanceIndexes: list of int non-negative
        :param Offset: 起始任務實例
        :type Offset: int
        :param Limit: 最大任務實例數
        :type Limit: int
        """
        self.JobId = None
        self.TaskName = None
        self.TaskInstanceIndexes = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.TaskName = params.get("TaskName")
        self.TaskInstanceIndexes = params.get("TaskInstanceIndexes")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTaskLogsResponse(AbstractModel):
    """DescribeTaskLogs返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 任務實例總數
        :type TotalCount: int
        :param TaskInstanceLogSet: 任務實例日志詳情集合
        :type TaskInstanceLogSet: list of TaskInstanceLog
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TaskInstanceLogSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TaskInstanceLogSet") is not None:
            self.TaskInstanceLogSet = []
            for item in params.get("TaskInstanceLogSet"):
                obj = TaskInstanceLog()
                obj._deserialize(item)
                self.TaskInstanceLogSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskRequest(AbstractModel):
    """DescribeTask請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 作業ID
        :type JobId: str
        :param TaskName: 任務名稱
        :type TaskName: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回數量。預設取值100，最大取值1000。
        :type Limit: int
        :param Filters: 過濾條件，詳情如下：
<li> task-instance-type - String - 是否必填： 否 - 按照任務實例狀态進行過濾（SUBMITTED：已提交；PENDING：等待中；RUNNABLE：可運作；STARTING：啓動中；RUNNING：運作中；SUCCEED：成功；FAILED：失敗；FAILED_INTERRUPTED：失敗後保留實例）。</li>
        :type Filters: list of Filter
        """
        self.JobId = None
        self.TaskName = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.TaskName = params.get("TaskName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeTaskResponse(AbstractModel):
    """DescribeTask返回參數結構體

    """

    def __init__(self):
        """
        :param JobId: 作業ID
        :type JobId: str
        :param TaskName: 任務名稱
        :type TaskName: str
        :param TaskState: 任務狀态
        :type TaskState: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param EndTime: 結束時間
        :type EndTime: str
        :param TaskInstanceTotalCount: 任務實例總數
        :type TaskInstanceTotalCount: int
        :param TaskInstanceSet: 任務實例訊息
        :type TaskInstanceSet: list of TaskInstanceView
        :param TaskInstanceMetrics: 任務實例統計指标
        :type TaskInstanceMetrics: :class:`taifucloudcloud.batch.v20170312.models.TaskInstanceMetrics`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.TaskName = None
        self.TaskState = None
        self.CreateTime = None
        self.EndTime = None
        self.TaskInstanceTotalCount = None
        self.TaskInstanceSet = None
        self.TaskInstanceMetrics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.TaskName = params.get("TaskName")
        self.TaskState = params.get("TaskState")
        self.CreateTime = params.get("CreateTime")
        self.EndTime = params.get("EndTime")
        self.TaskInstanceTotalCount = params.get("TaskInstanceTotalCount")
        if params.get("TaskInstanceSet") is not None:
            self.TaskInstanceSet = []
            for item in params.get("TaskInstanceSet"):
                obj = TaskInstanceView()
                obj._deserialize(item)
                self.TaskInstanceSet.append(obj)
        if params.get("TaskInstanceMetrics") is not None:
            self.TaskInstanceMetrics = TaskInstanceMetrics()
            self.TaskInstanceMetrics._deserialize(params.get("TaskInstanceMetrics"))
        self.RequestId = params.get("RequestId")


class DescribeTaskTemplatesRequest(AbstractModel):
    """DescribeTaskTemplates請求參數結構體

    """

    def __init__(self):
        """
        :param TaskTemplateIds: 任務範本ID清單，與Filters參數不能同時指定。
        :type TaskTemplateIds: list of str
        :param Filters: 過濾條件
<li> task-template-name - String - 是否必填：否 -（過濾條件）按照任務範本名稱過濾。</li>
與TaskTemplateIds參數不能同時指定。
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回數量
        :type Limit: int
        """
        self.TaskTemplateIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.TaskTemplateIds = params.get("TaskTemplateIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTaskTemplatesResponse(AbstractModel):
    """DescribeTaskTemplates返回參數結構體

    """

    def __init__(self):
        """
        :param TaskTemplateSet: 任務範本清單
        :type TaskTemplateSet: list of TaskTemplateView
        :param TotalCount: 任務範本數量
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskTemplateSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskTemplateSet") is not None:
            self.TaskTemplateSet = []
            for item in params.get("TaskTemplateSet"):
                obj = TaskTemplateView()
                obj._deserialize(item)
                self.TaskTemplateSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DetachInstancesRequest(AbstractModel):
    """DetachInstances請求參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 計算環境ID
        :type EnvId: str
        :param InstanceIds: 實例ID清單
        :type InstanceIds: list of str
        """
        self.EnvId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.InstanceIds = params.get("InstanceIds")


class DetachInstancesResponse(AbstractModel):
    """DetachInstances返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Docker(AbstractModel):
    """Docker容器訊息

    """

    def __init__(self):
        """
        :param User: Docker Hub 用戶名或 Tencent Registry 用戶名
        :type User: str
        :param Password: Docker Hub 密碼或 Tencent Registry 密碼
        :type Password: str
        :param Image: Docker Hub填寫“[user/repo]:[tag]”，Tencent Registry填寫“ccr.ccs.taifucloudyun.com/[namespace/repo]:[tag]”
        :type Image: str
        :param Server: Docker Hub 可以不填，但确保具有公網訪問能力。或者是 Tencent Registry 服務網址“ccr.ccs.taifucloudyun.com”
        :type Server: str
        """
        self.User = None
        self.Password = None
        self.Image = None
        self.Server = None


    def _deserialize(self, params):
        self.User = params.get("User")
        self.Password = params.get("Password")
        self.Image = params.get("Image")
        self.Server = params.get("Server")


class EnhancedService(AbstractModel):
    """描述了實例的增強服務啓用情況與其設置，如雲安全，雲監控等實例 Agent

    """

    def __init__(self):
        """
        :param SecurityService: 開啓雲安全服務。若不指定該參數，則預設開啓雲安全服務。
        :type SecurityService: :class:`taifucloudcloud.batch.v20170312.models.RunSecurityServiceEnabled`
        :param MonitorService: 開啓雲監控服務。若不指定該參數，則預設開啓雲監控服務。
        :type MonitorService: :class:`taifucloudcloud.batch.v20170312.models.RunMonitorServiceEnabled`
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


class EnvData(AbstractModel):
    """計算環境數據

    """

    def __init__(self):
        """
        :param InstanceType: CVM實例類型，不能與InstanceTypes和InstanceTypeOptions同時出現。
        :type InstanceType: str
        :param ImageId: CVM映像ID
        :type ImageId: str
        :param SystemDisk: 實例系統盤配置訊息
        :type SystemDisk: :class:`taifucloudcloud.batch.v20170312.models.SystemDisk`
        :param DataDisks: 實例數據盤配置訊息
        :type DataDisks: list of DataDisk
        :param VirtualPrivateCloud: 私有網絡相關訊息配置，與Zones和VirtualPrivateClouds不能同時指定。
        :type VirtualPrivateCloud: :class:`taifucloudcloud.batch.v20170312.models.VirtualPrivateCloud`
        :param InternetAccessible: 公網頻寬相關訊息設置
        :type InternetAccessible: :class:`taifucloudcloud.batch.v20170312.models.InternetAccessible`
        :param InstanceName: CVM實例顯示名稱
        :type InstanceName: str
        :param LoginSettings: 實例登入設置
        :type LoginSettings: :class:`taifucloudcloud.batch.v20170312.models.LoginSettings`
        :param SecurityGroupIds: 實例所屬安全組
        :type SecurityGroupIds: list of str
        :param EnhancedService: 增強服務。通過該參數可以指定是否開啓雲安全、雲監控等服務。若不指定該參數，則預設開啓雲監控、雲安全服務。
        :type EnhancedService: :class:`taifucloudcloud.batch.v20170312.models.EnhancedService`
        :param InstanceChargeType: CVM實例計費類型<br><li>POSTPAID_BY_HOUR：按小時後付費<br><li>SPOTPAID：競價付費<br>預設值：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        :param InstanceMarketOptions: 實例的市場相關選項，如競價實例相關參數
        :type InstanceMarketOptions: :class:`taifucloudcloud.batch.v20170312.models.InstanceMarketOptionsRequest`
        :param InstanceTypes: CVM實例類型清單，不能與InstanceType和InstanceTypeOptions同時出現。指定該欄位後，計算節點按照機型先後順序依次嘗試創建，直到實例創建成功，結束遍曆過程。最多支援10個機型。
        :type InstanceTypes: list of str
        :param InstanceTypeOptions: CVM實例機型配置。不能與InstanceType和InstanceTypes同時出現。
        :type InstanceTypeOptions: :class:`taifucloudcloud.batch.v20170312.models.InstanceTypeOptions`
        :param Zones: 可用區清單，支援跨可用區創建CVM實例。與VirtualPrivateCloud和VirtualPrivateClouds不能同時指定。
        :type Zones: list of str
        :param VirtualPrivateClouds: 私有網絡清單，支援跨私有網絡創建CVM實例。與VirtualPrivateCloud和Zones不能同時指定。
        :type VirtualPrivateClouds: list of VirtualPrivateCloud
        """
        self.InstanceType = None
        self.ImageId = None
        self.SystemDisk = None
        self.DataDisks = None
        self.VirtualPrivateCloud = None
        self.InternetAccessible = None
        self.InstanceName = None
        self.LoginSettings = None
        self.SecurityGroupIds = None
        self.EnhancedService = None
        self.InstanceChargeType = None
        self.InstanceMarketOptions = None
        self.InstanceTypes = None
        self.InstanceTypeOptions = None
        self.Zones = None
        self.VirtualPrivateClouds = None


    def _deserialize(self, params):
        self.InstanceType = params.get("InstanceType")
        self.ImageId = params.get("ImageId")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("VirtualPrivateCloud") is not None:
            self.VirtualPrivateCloud = VirtualPrivateCloud()
            self.VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.InstanceName = params.get("InstanceName")
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceMarketOptions") is not None:
            self.InstanceMarketOptions = InstanceMarketOptionsRequest()
            self.InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self.InstanceTypes = params.get("InstanceTypes")
        if params.get("InstanceTypeOptions") is not None:
            self.InstanceTypeOptions = InstanceTypeOptions()
            self.InstanceTypeOptions._deserialize(params.get("InstanceTypeOptions"))
        self.Zones = params.get("Zones")
        if params.get("VirtualPrivateClouds") is not None:
            self.VirtualPrivateClouds = []
            for item in params.get("VirtualPrivateClouds"):
                obj = VirtualPrivateCloud()
                obj._deserialize(item)
                self.VirtualPrivateClouds.append(obj)


class EnvDataCpm(AbstractModel):
    """黑石計算環境數據

    """

    def __init__(self):
        """
        :param Zones: 黑石可用區名稱清單。如ap-guangzhou-bls-1, 可通過黑石介面[DescribeRegions]( https://cloud.taifucloud.com/document/api/386/33564)介面獲取。不是Batch可用區名稱。目前僅支援一個可用區名稱。
        :type Zones: list of str
        :param InstanceTypes: 購買的機型ID。通過黑石介面[DescribeDeviceClass]( https://cloud.taifucloud.com/document/api/386/32911)查詢設備型号，獲取機型訊息。
        :type InstanceTypes: list of str
        :param TimeUnit: 購買時長單位，取值：m(月)。
        :type TimeUnit: str
        :param TimeSpan: 購買時長。
        :type TimeSpan: int
        :param RaidId: RAID類型ID。通過黑石介面[DescribeDeviceClassPartition]( https://cloud.taifucloud.com/document/api/386/32910)查詢機型RAID方式以及系統盤大小，獲取RAID訊息。
        :type RaidId: int
        :param OsTypeId: 佈署服務器的作業系統ID。通過批次計算介面DescribeCpmOsInfo查詢作業系統訊息。
        :type OsTypeId: int
        :param VirtualPrivateClouds: 黑石VPC清單，目前僅支援一個VPC。
        :type VirtualPrivateClouds: list of CpmVirtualPrivateCloud
        :param NeedSecurityAgent: 是否安裝安全Agent，取值：1(安裝) 0(不安裝)，預設取值0。
        :type NeedSecurityAgent: int
        :param NeedMonitorAgent: 是否安裝監控Agent，取值：1(安裝) 0(不安裝)，預設取值0。
        :type NeedMonitorAgent: int
        :param AutoRenewFlag: 自動續約标志位，取值：1(自動續約) 0(不自動續約)，預設取值0。
        :type AutoRenewFlag: int
        :param IsZoning: 數據盤是否格式化，取值：1(格式化) 0(不格式化)，預設取值爲1。
        :type IsZoning: int
        :param FileSystem: 指定數據盤的文件系統格式，當前支援 ext4和xfs選項， 預設爲ext4。 參數适用于數據盤和Linux， 且在IsZoning爲1時生效。
        :type FileSystem: str
        :param Password: 設置Linux root或Windows Administrator的密碼。若不設置此參數，預設情況下會随機生成密碼，并以站内信方式通知到用戶。
        :type Password: str
        :param ApplyEip: 是否分配彈性公網IP，取值：1(分配) 0(不分配)，預設取值0。
        :type ApplyEip: int
        :param EipPayMode: 彈性公網IP計費模式，取值：flow(按流量計費) bandwidth(按頻寬計費)，預設取值flow。
        :type EipPayMode: str
        :param EipBandwidth: 彈性公網IP頻寬限制，單位Mb。
        :type EipBandwidth: int
        :param ImageId: 自定義映像ID，取值生效時用自定義映像佈署物理機。
        :type ImageId: str
        :param SysRootSpace: 系統盤根分區大小，單位爲G，預設取值10G。通過黑石介面[DescribeDeviceClassPartition]( https://cloud.taifucloud.com/document/api/386/32910)查詢機型RAID方式以及系統盤大小，獲取根分區訊息。
        :type SysRootSpace: int
        :param SysDataSpace: /data分區大小，單位爲G。如果系統盤還有剩餘大小，會分配給/data分區。（特殊情況：如果剩餘空間不足10G，并且沒有指定/data分區，則剩餘空間會分配給Root分區）。
        :type SysDataSpace: int
        :param HyperThreading: 是否開啓超線程，取值：1(開啓) 0(關閉)，預設取值1。
        :type HyperThreading: int
        :param LanIps: 指定的内網IP清單，不指定時自動分配。
        :type LanIps: list of str
        """
        self.Zones = None
        self.InstanceTypes = None
        self.TimeUnit = None
        self.TimeSpan = None
        self.RaidId = None
        self.OsTypeId = None
        self.VirtualPrivateClouds = None
        self.NeedSecurityAgent = None
        self.NeedMonitorAgent = None
        self.AutoRenewFlag = None
        self.IsZoning = None
        self.FileSystem = None
        self.Password = None
        self.ApplyEip = None
        self.EipPayMode = None
        self.EipBandwidth = None
        self.ImageId = None
        self.SysRootSpace = None
        self.SysDataSpace = None
        self.HyperThreading = None
        self.LanIps = None


    def _deserialize(self, params):
        self.Zones = params.get("Zones")
        self.InstanceTypes = params.get("InstanceTypes")
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.RaidId = params.get("RaidId")
        self.OsTypeId = params.get("OsTypeId")
        if params.get("VirtualPrivateClouds") is not None:
            self.VirtualPrivateClouds = []
            for item in params.get("VirtualPrivateClouds"):
                obj = CpmVirtualPrivateCloud()
                obj._deserialize(item)
                self.VirtualPrivateClouds.append(obj)
        self.NeedSecurityAgent = params.get("NeedSecurityAgent")
        self.NeedMonitorAgent = params.get("NeedMonitorAgent")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.IsZoning = params.get("IsZoning")
        self.FileSystem = params.get("FileSystem")
        self.Password = params.get("Password")
        self.ApplyEip = params.get("ApplyEip")
        self.EipPayMode = params.get("EipPayMode")
        self.EipBandwidth = params.get("EipBandwidth")
        self.ImageId = params.get("ImageId")
        self.SysRootSpace = params.get("SysRootSpace")
        self.SysDataSpace = params.get("SysDataSpace")
        self.HyperThreading = params.get("HyperThreading")
        self.LanIps = params.get("LanIps")


class EnvVar(AbstractModel):
    """環境變量

    """

    def __init__(self):
        """
        :param Name: 環境變量名稱
        :type Name: str
        :param Value: 環境變量取值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class EventConfig(AbstractModel):
    """事件配置

    """

    def __init__(self):
        """
        :param EventName: 事件類型，包括：<br/><li>“JOB_RUNNING”：作業運作，适用于"SubmitJob"。</li><li>“JOB_SUCCEED”：作業成功，适用于"SubmitJob"。</li><li>“JOB_FAILED”：作業失敗，适用于"SubmitJob"。</li><li>“JOB_FAILED_INTERRUPTED”：作業失敗，保留實例，适用于"SubmitJob"。</li><li>“TASK_RUNNING”：任務運作，适用于"SubmitJob"。</li><li>“TASK_SUCCEED”：任務成功，适用于"SubmitJob"。</li><li>“TASK_FAILED”：任務失敗，适用于"SubmitJob"。</li><li>“TASK_FAILED_INTERRUPTED”：任務失敗，保留實例，适用于"SubmitJob"。</li><li>“TASK_INSTANCE_RUNNING”：任務實例運作，适用于"SubmitJob"。</li><li>“TASK_INSTANCE_SUCCEED”：任務實例成功，适用于"SubmitJob"。</li><li>“TASK_INSTANCE_FAILED”：任務實例失敗，适用于"SubmitJob"。</li><li>“TASK_INSTANCE_FAILED_INTERRUPTED”：任務實例失敗，保留實例，适用于"SubmitJob"。</li><li>“COMPUTE_ENV_CREATED”：計算環境已創建，适用于"CreateComputeEnv"。</li><li>“COMPUTE_ENV_DELETED”：計算環境已删除，适用于"CreateComputeEnv"。</li><li>“COMPUTE_NODE_CREATED”：計算節點已創建，适用于"CreateComputeEnv"和"SubmitJob"。</li><li>“COMPUTE_NODE_CREATION_FAILED”：計算節點創建失敗，适用于"CreateComputeEnv"和"SubmitJob"。</li><li>“COMPUTE_NODE_RUNNING”：計算節點運作中，适用于"CreateComputeEnv"和"SubmitJob"。</li><li>“COMPUTE_NODE_ABNORMAL”：計算節點異常，适用于"CreateComputeEnv"和"SubmitJob"。</li><li>“COMPUTE_NODE_DELETING”：計算節點已删除，适用于"CreateComputeEnv"和"SubmitJob"。</li>
        :type EventName: str
        :param EventVars: 自定義鍵值對
        :type EventVars: list of EventVar
        """
        self.EventName = None
        self.EventVars = None


    def _deserialize(self, params):
        self.EventName = params.get("EventName")
        if params.get("EventVars") is not None:
            self.EventVars = []
            for item in params.get("EventVars"):
                obj = EventVar()
                obj._deserialize(item)
                self.EventVars.append(obj)


class EventVar(AbstractModel):
    """自定義鍵值對

    """

    def __init__(self):
        """
        :param Name: 自定義鍵
        :type Name: str
        :param Value: 自定義值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class Externals(AbstractModel):
    """擴展數據

    """

    def __init__(self):
        """
        :param ReleaseAddress: 釋放網址
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReleaseAddress: bool
        :param UnsupportNetworks: 不支援的網絡類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type UnsupportNetworks: list of str
        :param StorageBlockAttr: HDD本地儲存屬性
注意：此欄位可能返回 null，表示取不到有效值。
        :type StorageBlockAttr: :class:`taifucloudcloud.batch.v20170312.models.StorageBlock`
        """
        self.ReleaseAddress = None
        self.UnsupportNetworks = None
        self.StorageBlockAttr = None


    def _deserialize(self, params):
        self.ReleaseAddress = params.get("ReleaseAddress")
        self.UnsupportNetworks = params.get("UnsupportNetworks")
        if params.get("StorageBlockAttr") is not None:
            self.StorageBlockAttr = StorageBlock()
            self.StorageBlockAttr._deserialize(params.get("StorageBlockAttr"))


class Filter(AbstractModel):
    """>描述鍵值對過濾器，用于條件過濾查詢。例如過濾ID、名稱、狀态等
    > * 若存在多個`Filter`時，`Filter`間的關系爲邏輯與（`AND`）關系。
    > * 若同一個`Filter`存在多個`Values`，同一`Filter`下`Values`間的關系爲邏輯或（`OR`）關系。
    >
    > 以[DescribeInstances](https://cloud.taifucloud.com/document/api/213/15728)介面的`Filter`爲例。若我們需要查詢可用區（`zone`）爲 一區 ***并且*** 實例計費模式（`instance-charge-type`）爲包年包月 ***或者*** 按量計費的實例時，可如下實現：
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


class InputMapping(AbstractModel):
    """輸入映射

    """

    def __init__(self):
        """
        :param SourcePath: 源端路徑
        :type SourcePath: str
        :param DestinationPath: 目的端路徑
        :type DestinationPath: str
        :param MountOptionParameter: 掛載配置項參數
        :type MountOptionParameter: str
        """
        self.SourcePath = None
        self.DestinationPath = None
        self.MountOptionParameter = None


    def _deserialize(self, params):
        self.SourcePath = params.get("SourcePath")
        self.DestinationPath = params.get("DestinationPath")
        self.MountOptionParameter = params.get("MountOptionParameter")


class Instance(AbstractModel):
    """描述實例的訊息

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param ImageId: 映像ID
        :type ImageId: str
        :param LoginSettings: 實例登入設置。
        :type LoginSettings: :class:`taifucloudcloud.batch.v20170312.models.LoginSettings`
        """
        self.InstanceId = None
        self.ImageId = None
        self.LoginSettings = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ImageId = params.get("ImageId")
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))


class InstanceCategoryItem(AbstractModel):
    """實例分類清單

    """

    def __init__(self):
        """
        :param InstanceCategory: 實例類型名
        :type InstanceCategory: str
        :param InstanceFamilySet: 實例族清單
        :type InstanceFamilySet: list of str
        """
        self.InstanceCategory = None
        self.InstanceFamilySet = None


    def _deserialize(self, params):
        self.InstanceCategory = params.get("InstanceCategory")
        self.InstanceFamilySet = params.get("InstanceFamilySet")


class InstanceMarketOptionsRequest(AbstractModel):
    """競價請求相關選項

    """

    def __init__(self):
        """
        :param SpotOptions: 競價相關選項
        :type SpotOptions: :class:`taifucloudcloud.batch.v20170312.models.SpotMarketOptions`
        :param MarketType: 市場選項類型，當前只支援取值：spot
        :type MarketType: str
        """
        self.SpotOptions = None
        self.MarketType = None


    def _deserialize(self, params):
        if params.get("SpotOptions") is not None:
            self.SpotOptions = SpotMarketOptions()
            self.SpotOptions._deserialize(params.get("SpotOptions"))
        self.MarketType = params.get("MarketType")


class InstanceTypeConfig(AbstractModel):
    """批次計算可用的InstanceTypeConfig訊息

    """

    def __init__(self):
        """
        :param Mem: 内存容量，單位：`GB`。
        :type Mem: int
        :param Cpu: CPU核數，單位：核。
        :type Cpu: int
        :param InstanceType: 實例機型。
        :type InstanceType: str
        :param Zone: 可用區。
        :type Zone: str
        :param InstanceFamily: 實例機型系列。
        :type InstanceFamily: str
        """
        self.Mem = None
        self.Cpu = None
        self.InstanceType = None
        self.Zone = None
        self.InstanceFamily = None


    def _deserialize(self, params):
        self.Mem = params.get("Mem")
        self.Cpu = params.get("Cpu")
        self.InstanceType = params.get("InstanceType")
        self.Zone = params.get("Zone")
        self.InstanceFamily = params.get("InstanceFamily")


class InstanceTypeOptions(AbstractModel):
    """實例機型配置。

    """

    def __init__(self):
        """
        :param CPU: CPU核數。
        :type CPU: int
        :param Memory: 内存值，單位GB。
        :type Memory: int
        :param InstanceCategories: 實例機型類别，可選參數：“ALL”、“GENERAL”、“GENERAL_2”、“GENERAL_3”、“COMPUTE”、“COMPUTE_2”和“COMPUTE_3”。預設值“ALL”。
        :type InstanceCategories: list of str
        """
        self.CPU = None
        self.Memory = None
        self.InstanceCategories = None


    def _deserialize(self, params):
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")
        self.InstanceCategories = params.get("InstanceCategories")


class InstanceTypeQuotaItem(AbstractModel):
    """描述實例機型配額訊息。

    """

    def __init__(self):
        """
        :param Zone: 可用區。
        :type Zone: str
        :param InstanceType: 實例機型。
        :type InstanceType: str
        :param InstanceChargeType: 實例計費模式。取值範圍： <br><li>PREPAID：表示預付費，即包年包月<br><li>POSTPAID_BY_HOUR：表示後付費，即按量計費<br><li>CDHPAID：表示[CDH](https://cloud.taifucloud.com/document/product/416)付費，即只對CDH計費，不對CDH上的實例計費。<br><li>`SPOTPAID`：表示競價實例付費。
        :type InstanceChargeType: str
        :param NetworkCard: 網卡類型，例如：25代表25G網卡
        :type NetworkCard: int
        :param Externals: 擴展屬性。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Externals: :class:`taifucloudcloud.batch.v20170312.models.Externals`
        :param Cpu: 實例的CPU核數，單位：核。
        :type Cpu: int
        :param Memory: 實例内存容量，單位：`GB`。
        :type Memory: int
        :param InstanceFamily: 實例機型系列。
        :type InstanceFamily: str
        :param TypeName: 機型名稱。
        :type TypeName: str
        :param LocalDiskTypeList: 本地磁盤規格清單。當該參數返回爲空值時，表示當前情況下無法創建本地盤。
        :type LocalDiskTypeList: list of LocalDiskType
        :param Status: 實例是否售賣。取值範圍： <br><li>SELL：表示實例可購買<br><li>SOLD_OUT：表示實例已售罄。
        :type Status: str
        :param Price: 實例的售賣價格。
        :type Price: :class:`taifucloudcloud.batch.v20170312.models.ItemPrice`
        :param SoldOutReason: 售罄原因。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SoldOutReason: str
        """
        self.Zone = None
        self.InstanceType = None
        self.InstanceChargeType = None
        self.NetworkCard = None
        self.Externals = None
        self.Cpu = None
        self.Memory = None
        self.InstanceFamily = None
        self.TypeName = None
        self.LocalDiskTypeList = None
        self.Status = None
        self.Price = None
        self.SoldOutReason = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceType = params.get("InstanceType")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.NetworkCard = params.get("NetworkCard")
        if params.get("Externals") is not None:
            self.Externals = Externals()
            self.Externals._deserialize(params.get("Externals"))
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.InstanceFamily = params.get("InstanceFamily")
        self.TypeName = params.get("TypeName")
        if params.get("LocalDiskTypeList") is not None:
            self.LocalDiskTypeList = []
            for item in params.get("LocalDiskTypeList"):
                obj = LocalDiskType()
                obj._deserialize(item)
                self.LocalDiskTypeList.append(obj)
        self.Status = params.get("Status")
        if params.get("Price") is not None:
            self.Price = ItemPrice()
            self.Price._deserialize(params.get("Price"))
        self.SoldOutReason = params.get("SoldOutReason")


class InternetAccessible(AbstractModel):
    """描述了實例的公網可訪問性，聲明了實例的公網使用計費模式，最大頻寬等

    """

    def __init__(self):
        """
        :param InternetChargeType: 網絡計費類型。取值範圍：<br><li>BANDWIDTH_PREPAID：預付費按頻寬結算<br><li>TRAFFIC_POSTPAID_BY_HOUR：流量按小時後付費<br><li>BANDWIDTH_POSTPAID_BY_HOUR：頻寬按小時後付費<br><li>BANDWIDTH_PACKAGE：頻寬包用戶<br>預設取值：非頻寬包用戶預設與子機付費類型保持一緻。
        :type InternetChargeType: str
        :param InternetMaxBandwidthOut: 公網出頻寬上限，單位：Mbps。預設值：0Mbps。不同機型頻寬上限範圍不一緻，具體限制詳見[購買網絡頻寬](https://cloud.taifucloud.com/document/product/213/12523)。
        :type InternetMaxBandwidthOut: int
        :param PublicIpAssigned: 是否分配公網IP。取值範圍：<br><li>TRUE：表示分配公網IP<br><li>FALSE：表示不分配公網IP<br><br>當公網頻寬大于0Mbps時，可自由選擇開通與否，預設開通公網IP；當公網頻寬爲0，則不允許分配公網IP。該參數僅在RunInstances介面中作爲入參使用。
        :type PublicIpAssigned: bool
        :param BandwidthPackageId: 頻寬包ID。可通過[`DescribeBandwidthPackages`](https://cloud.taifucloud.com/document/api/215/19209)介面返回值中的`BandwidthPackageId`獲取。該參數僅在RunInstances介面中作爲入參使用。
        :type BandwidthPackageId: str
        """
        self.InternetChargeType = None
        self.InternetMaxBandwidthOut = None
        self.PublicIpAssigned = None
        self.BandwidthPackageId = None


    def _deserialize(self, params):
        self.InternetChargeType = params.get("InternetChargeType")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.PublicIpAssigned = params.get("PublicIpAssigned")
        self.BandwidthPackageId = params.get("BandwidthPackageId")


class ItemPrice(AbstractModel):
    """描述了單項的價格訊息

    """

    def __init__(self):
        """
        :param UnitPrice: 後續合計費用的原價，後付費模式使用，單位：元。<br><li>如返回了其他時間區間項，如UnitPriceSecondStep，則本項代表時間區間在(0, 96)小時；若未返回其他時間區間項，則本項代表全時段，即(0, ∞)小時
注意：此欄位可能返回 null，表示取不到有效值。
        :type UnitPrice: float
        :param ChargeUnit: 後續計價單元，後付費模式使用，可取值範圍： <br><li>HOUR：表示計價單元是按每小時來計算。當前涉及該計價單元的場景有：實例按小時後付費（POSTPAID_BY_HOUR）、頻寬按小時後付費（BANDWIDTH_POSTPAID_BY_HOUR）：<br><li>GB：表示計價單元是按每GB來計算。當前涉及該計價單元的場景有：流量按小時後付費（TRAFFIC_POSTPAID_BY_HOUR）。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ChargeUnit: str
        :param OriginalPrice: 預支合計費用的原價，預付費模式使用，單位：元。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OriginalPrice: float
        :param DiscountPrice: 預支合計費用的折扣價，預付費模式使用，單位：元。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DiscountPrice: float
        :param Discount: 折扣，如20.0代表2折
注意：此欄位可能返回 null，表示取不到有效值。
        :type Discount: float
        :param UnitPriceDiscount: 後續合計費用的折扣價，後付費模式使用，單位：元<br><li>如返回了其他時間區間項，如UnitPriceDiscountSecondStep，則本項代表時間區間在(0, 96)小時；若未返回其他時間區間項，則本項代表全時段，即(0, ∞)小時
注意：此欄位可能返回 null，表示取不到有效值。
        :type UnitPriceDiscount: float
        :param UnitPriceSecondStep: 使用時間區間在(96, 360)小時的後續合計費用的原價，後付費模式使用，單位：元。
注意：此欄位可能返回 null，表示取不到有效值。
        :type UnitPriceSecondStep: float
        :param UnitPriceDiscountSecondStep: 使用時間區間在(96, 360)小時的後續合計費用的折扣價，後付費模式使用，單位：元
注意：此欄位可能返回 null，表示取不到有效值。
        :type UnitPriceDiscountSecondStep: float
        :param UnitPriceThirdStep: 使用時間區間在(360, ∞)小時的後續合計費用的原價，後付費模式使用，單位：元。
注意：此欄位可能返回 null，表示取不到有效值。
        :type UnitPriceThirdStep: float
        :param UnitPriceDiscountThirdStep: 使用時間區間在(360, ∞)小時的後續合計費用的折扣價，後付費模式使用，單位：元
注意：此欄位可能返回 null，表示取不到有效值。
        :type UnitPriceDiscountThirdStep: float
        """
        self.UnitPrice = None
        self.ChargeUnit = None
        self.OriginalPrice = None
        self.DiscountPrice = None
        self.Discount = None
        self.UnitPriceDiscount = None
        self.UnitPriceSecondStep = None
        self.UnitPriceDiscountSecondStep = None
        self.UnitPriceThirdStep = None
        self.UnitPriceDiscountThirdStep = None


    def _deserialize(self, params):
        self.UnitPrice = params.get("UnitPrice")
        self.ChargeUnit = params.get("ChargeUnit")
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")
        self.Discount = params.get("Discount")
        self.UnitPriceDiscount = params.get("UnitPriceDiscount")
        self.UnitPriceSecondStep = params.get("UnitPriceSecondStep")
        self.UnitPriceDiscountSecondStep = params.get("UnitPriceDiscountSecondStep")
        self.UnitPriceThirdStep = params.get("UnitPriceThirdStep")
        self.UnitPriceDiscountThirdStep = params.get("UnitPriceDiscountThirdStep")


class Job(AbstractModel):
    """作業

    """

    def __init__(self):
        """
        :param Tasks: 任務訊息
        :type Tasks: list of Task
        :param JobName: 作業名稱
        :type JobName: str
        :param JobDescription: 作業描述
        :type JobDescription: str
        :param Priority: 作業優先級，任務（Task）和任務實例（TaskInstance）會繼承作業優先級
        :type Priority: int
        :param Dependences: 依賴訊息
        :type Dependences: list of Dependence
        :param Notifications: 通知訊息
        :type Notifications: list of Notification
        :param TaskExecutionDependOn: 對于存在依賴關系的任務中，後序任務執行對于前序任務的依賴條件。取值範圍包括 PRE_TASK_SUCCEED，PRE_TASK_AT_LEAST_PARTLY_SUCCEED，PRE_TASK_FINISHED，預設值爲PRE_TASK_SUCCEED。
        :type TaskExecutionDependOn: str
        :param StateIfCreateCvmFailed: 表示創建 CVM 失敗按照何種策略處理。取值範圍包括 FAILED，RUNNABLE。FAILED 表示創建 CVM 失敗按照一次執行失敗處理，RUNNABLE 表示創建 CVM 失敗按照繼續等待處理。預設值爲FAILED。StateIfCreateCvmFailed對于提交的指定計算環境的作業無效。
        :type StateIfCreateCvmFailed: str
        """
        self.Tasks = None
        self.JobName = None
        self.JobDescription = None
        self.Priority = None
        self.Dependences = None
        self.Notifications = None
        self.TaskExecutionDependOn = None
        self.StateIfCreateCvmFailed = None


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.JobName = params.get("JobName")
        self.JobDescription = params.get("JobDescription")
        self.Priority = params.get("Priority")
        if params.get("Dependences") is not None:
            self.Dependences = []
            for item in params.get("Dependences"):
                obj = Dependence()
                obj._deserialize(item)
                self.Dependences.append(obj)
        if params.get("Notifications") is not None:
            self.Notifications = []
            for item in params.get("Notifications"):
                obj = Notification()
                obj._deserialize(item)
                self.Notifications.append(obj)
        self.TaskExecutionDependOn = params.get("TaskExecutionDependOn")
        self.StateIfCreateCvmFailed = params.get("StateIfCreateCvmFailed")


class JobView(AbstractModel):
    """作業訊息

    """

    def __init__(self):
        """
        :param JobId: 作業ID
        :type JobId: str
        :param JobName: 作業名稱
        :type JobName: str
        :param JobState: 作業狀态
        :type JobState: str
        :param Priority: 作業優先級
        :type Priority: int
        :param Placement: 位置訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Placement: :class:`taifucloudcloud.batch.v20170312.models.Placement`
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param EndTime: 結束時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param TaskMetrics: 任務統計指标
        :type TaskMetrics: :class:`taifucloudcloud.batch.v20170312.models.TaskMetrics`
        """
        self.JobId = None
        self.JobName = None
        self.JobState = None
        self.Priority = None
        self.Placement = None
        self.CreateTime = None
        self.EndTime = None
        self.TaskMetrics = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.JobState = params.get("JobState")
        self.Priority = params.get("Priority")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.CreateTime = params.get("CreateTime")
        self.EndTime = params.get("EndTime")
        if params.get("TaskMetrics") is not None:
            self.TaskMetrics = TaskMetrics()
            self.TaskMetrics._deserialize(params.get("TaskMetrics"))


class LocalDiskType(AbstractModel):
    """本地磁盤規格

    """

    def __init__(self):
        """
        :param Type: 本地磁盤類型。
        :type Type: str
        :param PartitionType: 本地磁盤屬性。
        :type PartitionType: str
        :param MinSize: 本地磁盤最小值。
        :type MinSize: int
        :param MaxSize: 本地磁盤最大值。
        :type MaxSize: int
        :param Required: 購買時本地盤是否爲必選。取值範圍：<br><li>REQUIRED：表示必選<br><li>OPTIONAL：表示可選。
        :type Required: str
        """
        self.Type = None
        self.PartitionType = None
        self.MinSize = None
        self.MaxSize = None
        self.Required = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.PartitionType = params.get("PartitionType")
        self.MinSize = params.get("MinSize")
        self.MaxSize = params.get("MaxSize")
        self.Required = params.get("Required")


class LoginSettings(AbstractModel):
    """描述了實例登入相關配置與訊息。

    """

    def __init__(self):
        """
        :param Password: 實例登入密碼。不同作業系統類型密碼複雜度限制不一樣，具體如下：<br><li>Linux實例密碼必須8到16位，至少包括兩項[a-z，A-Z]、[0-9] 和 [( ) ` ~ ! @ # $ % ^ & * - + = | { } [ ] : ; ' , . ? \/ ]中的特殊符号。<br><li>Windows實例密碼必須12到16位，至少包括三項[a-z]，[A-Z]，[0-9] 和 [( ) ` ~ ! @ # $ % ^ & * - + = { } [ ] : ; ' , . ? \/]中的特殊符号。<br><br>若不指定該參數，則由系統随機生成密碼，并通過站内信方式通知到用戶。
        :type Password: str
        :param KeyIds: 金鑰ID清單。關聯金鑰後，就可以通過對應的私鑰來訪問實例；KeyId可通過介面DescribeKeyPairs獲取，金鑰與密碼不能同時指定，同時Windows作業系統不支援指定金鑰。當前僅支援購買的時候指定一個金鑰。
        :type KeyIds: list of str
        :param KeepImageLogin: 保持映像的原始設置。該參數與Password或KeyIds.N不能同時指定。只有使用自定義映像、共享映像或外部導入映像創建實例時才能指定該參數爲TRUE。取值範圍：<br><li>TRUE：表示保持映像的登入設置<br><li>FALSE：表示不保持映像的登入設置<br><br>預設取值：FALSE。
        :type KeepImageLogin: str
        """
        self.Password = None
        self.KeyIds = None
        self.KeepImageLogin = None


    def _deserialize(self, params):
        self.Password = params.get("Password")
        self.KeyIds = params.get("KeyIds")
        self.KeepImageLogin = params.get("KeepImageLogin")


class ModifyComputeEnvRequest(AbstractModel):
    """ModifyComputeEnv請求參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 計算環境ID
        :type EnvId: str
        :param DesiredComputeNodeCount: 計算節點期望個數
        :type DesiredComputeNodeCount: int
        :param EnvName: 計算環境名稱
        :type EnvName: str
        :param EnvDescription: 計算環境描述
        :type EnvDescription: str
        :param EnvData: 計算環境屬性數據
        :type EnvData: :class:`taifucloudcloud.batch.v20170312.models.ComputeEnvData`
        """
        self.EnvId = None
        self.DesiredComputeNodeCount = None
        self.EnvName = None
        self.EnvDescription = None
        self.EnvData = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
        self.EnvName = params.get("EnvName")
        self.EnvDescription = params.get("EnvDescription")
        if params.get("EnvData") is not None:
            self.EnvData = ComputeEnvData()
            self.EnvData._deserialize(params.get("EnvData"))


class ModifyComputeEnvResponse(AbstractModel):
    """ModifyComputeEnv返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTaskTemplateRequest(AbstractModel):
    """ModifyTaskTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param TaskTemplateId: 任務範本ID
        :type TaskTemplateId: str
        :param TaskTemplateName: 任務範本名稱
        :type TaskTemplateName: str
        :param TaskTemplateDescription: 任務範本描述
        :type TaskTemplateDescription: str
        :param TaskTemplateInfo: 任務範本訊息
        :type TaskTemplateInfo: :class:`taifucloudcloud.batch.v20170312.models.Task`
        """
        self.TaskTemplateId = None
        self.TaskTemplateName = None
        self.TaskTemplateDescription = None
        self.TaskTemplateInfo = None


    def _deserialize(self, params):
        self.TaskTemplateId = params.get("TaskTemplateId")
        self.TaskTemplateName = params.get("TaskTemplateName")
        self.TaskTemplateDescription = params.get("TaskTemplateDescription")
        if params.get("TaskTemplateInfo") is not None:
            self.TaskTemplateInfo = Task()
            self.TaskTemplateInfo._deserialize(params.get("TaskTemplateInfo"))


class ModifyTaskTemplateResponse(AbstractModel):
    """ModifyTaskTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MountDataDisk(AbstractModel):
    """數據盤掛載選項

    """

    def __init__(self):
        """
        :param LocalPath: 掛載點，Linux系統合法路徑，或Windows系統盤符,比如"H:\\"
        :type LocalPath: str
        :param FileSystemType: 文件系統類型，Linux系統下支援"EXT3"和"EXT4"兩種，預設"EXT3"；Windows系統下僅支援"NTFS"
        :type FileSystemType: str
        """
        self.LocalPath = None
        self.FileSystemType = None


    def _deserialize(self, params):
        self.LocalPath = params.get("LocalPath")
        self.FileSystemType = params.get("FileSystemType")


class NamedComputeEnv(AbstractModel):
    """計算環境

    """

    def __init__(self):
        """
        :param EnvName: 計算環境名稱
        :type EnvName: str
        :param DesiredComputeNodeCount: 計算節點期望個數
        :type DesiredComputeNodeCount: int
        :param EnvDescription: 計算環境描述
        :type EnvDescription: str
        :param EnvType: 計算環境管理類型
        :type EnvType: str
        :param EnvData: 計算環境具體參數
        :type EnvData: :class:`taifucloudcloud.batch.v20170312.models.EnvData`
        :param MountDataDisks: 數據盤掛載選項
        :type MountDataDisks: list of MountDataDisk
        :param Authentications: 授權訊息
        :type Authentications: list of Authentication
        :param InputMappings: 輸入映射訊息
        :type InputMappings: list of InputMapping
        :param AgentRunningMode: agent運作模式，适用于Windows系統
        :type AgentRunningMode: :class:`taifucloudcloud.batch.v20170312.models.AgentRunningMode`
        :param Notifications: 通知訊息
        :type Notifications: :class:`taifucloudcloud.batch.v20170312.models.Notification`
        :param ActionIfComputeNodeInactive: 非活躍節點處理策略，預設“RECREATE”，即對于實例創建失敗或異常退還的計算節點，定期重新創建實例資源。
        :type ActionIfComputeNodeInactive: str
        :param ResourceMaxRetryCount: 對于實例創建失敗或異常退還的計算節點，定期重新創建實例資源的最大重試次數，最大值11，如果不設置的話，系統會設置一個預設值，當前爲7
        :type ResourceMaxRetryCount: int
        """
        self.EnvName = None
        self.DesiredComputeNodeCount = None
        self.EnvDescription = None
        self.EnvType = None
        self.EnvData = None
        self.MountDataDisks = None
        self.Authentications = None
        self.InputMappings = None
        self.AgentRunningMode = None
        self.Notifications = None
        self.ActionIfComputeNodeInactive = None
        self.ResourceMaxRetryCount = None


    def _deserialize(self, params):
        self.EnvName = params.get("EnvName")
        self.DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
        self.EnvDescription = params.get("EnvDescription")
        self.EnvType = params.get("EnvType")
        if params.get("EnvData") is not None:
            self.EnvData = EnvData()
            self.EnvData._deserialize(params.get("EnvData"))
        if params.get("MountDataDisks") is not None:
            self.MountDataDisks = []
            for item in params.get("MountDataDisks"):
                obj = MountDataDisk()
                obj._deserialize(item)
                self.MountDataDisks.append(obj)
        if params.get("Authentications") is not None:
            self.Authentications = []
            for item in params.get("Authentications"):
                obj = Authentication()
                obj._deserialize(item)
                self.Authentications.append(obj)
        if params.get("InputMappings") is not None:
            self.InputMappings = []
            for item in params.get("InputMappings"):
                obj = InputMapping()
                obj._deserialize(item)
                self.InputMappings.append(obj)
        if params.get("AgentRunningMode") is not None:
            self.AgentRunningMode = AgentRunningMode()
            self.AgentRunningMode._deserialize(params.get("AgentRunningMode"))
        if params.get("Notifications") is not None:
            self.Notifications = Notification()
            self.Notifications._deserialize(params.get("Notifications"))
        self.ActionIfComputeNodeInactive = params.get("ActionIfComputeNodeInactive")
        self.ResourceMaxRetryCount = params.get("ResourceMaxRetryCount")


class NamedCpmComputeEnv(AbstractModel):
    """黑石計算環境

    """

    def __init__(self):
        """
        :param EnvName: 計算環境名稱
        :type EnvName: str
        :param EnvData: 計算環境具體參數
        :type EnvData: :class:`taifucloudcloud.batch.v20170312.models.EnvDataCpm`
        :param DesiredComputeNodeCount: 計算節點期望個數
        :type DesiredComputeNodeCount: int
        :param EnvDescription: 計算環境描述
        :type EnvDescription: str
        :param EnvType: 計算環境管理類型， 取值MANAGED。
        :type EnvType: str
        :param Authentications: 授權訊息
        :type Authentications: list of Authentication
        :param InputMappings: 輸入映射訊息
        :type InputMappings: list of InputMapping
        :param Notifications: 通知訊息
        :type Notifications: :class:`taifucloudcloud.batch.v20170312.models.Notification`
        :param ActionIfComputeNodeInactive: 非活躍節點處理策略，預設“RECREATE”，即對于實例創建失敗或異常退還的計算節點，定期重新創建實例資源。
        :type ActionIfComputeNodeInactive: str
        :param ResourceMaxRetryCount: 對于實例創建失敗或異常退還的計算節點，定期重新創建實例資源的最大重試次數，最大值11，如果不設置的話，系統會設置一個預設值，當前爲7
        :type ResourceMaxRetryCount: int
        """
        self.EnvName = None
        self.EnvData = None
        self.DesiredComputeNodeCount = None
        self.EnvDescription = None
        self.EnvType = None
        self.Authentications = None
        self.InputMappings = None
        self.Notifications = None
        self.ActionIfComputeNodeInactive = None
        self.ResourceMaxRetryCount = None


    def _deserialize(self, params):
        self.EnvName = params.get("EnvName")
        if params.get("EnvData") is not None:
            self.EnvData = EnvDataCpm()
            self.EnvData._deserialize(params.get("EnvData"))
        self.DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
        self.EnvDescription = params.get("EnvDescription")
        self.EnvType = params.get("EnvType")
        if params.get("Authentications") is not None:
            self.Authentications = []
            for item in params.get("Authentications"):
                obj = Authentication()
                obj._deserialize(item)
                self.Authentications.append(obj)
        if params.get("InputMappings") is not None:
            self.InputMappings = []
            for item in params.get("InputMappings"):
                obj = InputMapping()
                obj._deserialize(item)
                self.InputMappings.append(obj)
        if params.get("Notifications") is not None:
            self.Notifications = Notification()
            self.Notifications._deserialize(params.get("Notifications"))
        self.ActionIfComputeNodeInactive = params.get("ActionIfComputeNodeInactive")
        self.ResourceMaxRetryCount = params.get("ResourceMaxRetryCount")


class Notification(AbstractModel):
    """通知訊息

    """

    def __init__(self):
        """
        :param TopicName: CMQ主題名字，要求主題名有效且關聯訂閱
        :type TopicName: str
        :param EventConfigs: 事件配置
        :type EventConfigs: list of EventConfig
        """
        self.TopicName = None
        self.EventConfigs = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        if params.get("EventConfigs") is not None:
            self.EventConfigs = []
            for item in params.get("EventConfigs"):
                obj = EventConfig()
                obj._deserialize(item)
                self.EventConfigs.append(obj)


class OsInfo(AbstractModel):
    """作業系統類型

    """

    def __init__(self):
        """
        :param OsTypeId: 作業系統ID。
        :type OsTypeId: int
        :param OsName: 作業系統名稱。
        :type OsName: str
        :param OsDescription: 作業系統名稱描述。
        :type OsDescription: str
        :param OsEnglishDescription: 作業系統英文名稱。
        :type OsEnglishDescription: str
        :param OsClass: 作業系統的分類，如CentOs Debian。
        :type OsClass: str
        :param ImageTag: 标識映像分類。public:公共映像; private: 專屬映像。
        :type ImageTag: str
        :param MaxPartitionSize: 作業系統，ext4文件下所支援的最大的磁盤大小。單位爲T。
        :type MaxPartitionSize: int
        """
        self.OsTypeId = None
        self.OsName = None
        self.OsDescription = None
        self.OsEnglishDescription = None
        self.OsClass = None
        self.ImageTag = None
        self.MaxPartitionSize = None


    def _deserialize(self, params):
        self.OsTypeId = params.get("OsTypeId")
        self.OsName = params.get("OsName")
        self.OsDescription = params.get("OsDescription")
        self.OsEnglishDescription = params.get("OsEnglishDescription")
        self.OsClass = params.get("OsClass")
        self.ImageTag = params.get("ImageTag")
        self.MaxPartitionSize = params.get("MaxPartitionSize")


class OutputMapping(AbstractModel):
    """輸出映射

    """

    def __init__(self):
        """
        :param SourcePath: 源端路徑
        :type SourcePath: str
        :param DestinationPath: 目的端路徑
        :type DestinationPath: str
        """
        self.SourcePath = None
        self.DestinationPath = None


    def _deserialize(self, params):
        self.SourcePath = params.get("SourcePath")
        self.DestinationPath = params.get("DestinationPath")


class OutputMappingConfig(AbstractModel):
    """輸出映射配置

    """

    def __init__(self):
        """
        :param Scene: 儲存類型，僅支援COS
        :type Scene: str
        :param WorkerNum: 並行worker數量
        :type WorkerNum: int
        :param WorkerPartSize: worker分塊大小，單位MB
        :type WorkerPartSize: int
        """
        self.Scene = None
        self.WorkerNum = None
        self.WorkerPartSize = None


    def _deserialize(self, params):
        self.Scene = params.get("Scene")
        self.WorkerNum = params.get("WorkerNum")
        self.WorkerPartSize = params.get("WorkerPartSize")


class Placement(AbstractModel):
    """描述了實例的抽象位置，包括其所在的可用區，所屬的項目，宿主機（僅CDH産品可用），母機ip等

    """

    def __init__(self):
        """
        :param Zone: 實例所屬的[可用區](https://cloud.taifucloud.com/document/product/213/15753#ZoneInfo)ID。該參數也可以通過調用  [DescribeZones](https://cloud.taifucloud.com/document/product/213/15707) 的返回值中的Zone欄位來獲取。
        :type Zone: str
        :param ProjectId: 實例所屬項目ID。該參數可以通過調用 [DescribeProject](/document/api/378/4400) 的返回值中的 projectId 欄位來獲取。不填爲預設項目。
        :type ProjectId: int
        :param HostIds: 實例所屬的專用宿主機ID清單，僅用于入參。如果您有購買專用宿主機并且指定了該參數，則您購買的實例就會随機的佈署在這些專用宿主機上。
        :type HostIds: list of str
        :param HostIps: 指定母機ip生産子機
        :type HostIps: list of str
        :param HostId: 實例所屬的專用宿主機ID，僅用于出參。
        :type HostId: str
        """
        self.Zone = None
        self.ProjectId = None
        self.HostIds = None
        self.HostIps = None
        self.HostId = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ProjectId = params.get("ProjectId")
        self.HostIds = params.get("HostIds")
        self.HostIps = params.get("HostIps")
        self.HostId = params.get("HostId")


class RedirectInfo(AbstractModel):
    """重定向訊息

    """

    def __init__(self):
        """
        :param StdoutRedirectPath: 标準輸出重定向路徑
        :type StdoutRedirectPath: str
        :param StderrRedirectPath: 标準錯誤重定向路徑
        :type StderrRedirectPath: str
        :param StdoutRedirectFileName: 标準輸出重定向文件名，支援三個占位符${BATCH_JOB_ID}、${BATCH_TASK_NAME}、${BATCH_TASK_INSTANCE_INDEX}
        :type StdoutRedirectFileName: str
        :param StderrRedirectFileName: 标準錯誤重定向文件名，支援三個占位符${BATCH_JOB_ID}、${BATCH_TASK_NAME}、${BATCH_TASK_INSTANCE_INDEX}
        :type StderrRedirectFileName: str
        """
        self.StdoutRedirectPath = None
        self.StderrRedirectPath = None
        self.StdoutRedirectFileName = None
        self.StderrRedirectFileName = None


    def _deserialize(self, params):
        self.StdoutRedirectPath = params.get("StdoutRedirectPath")
        self.StderrRedirectPath = params.get("StderrRedirectPath")
        self.StdoutRedirectFileName = params.get("StdoutRedirectFileName")
        self.StderrRedirectFileName = params.get("StderrRedirectFileName")


class RedirectLocalInfo(AbstractModel):
    """本地重定向訊息

    """

    def __init__(self):
        """
        :param StdoutLocalPath: 标準輸出重定向本地路徑
        :type StdoutLocalPath: str
        :param StderrLocalPath: 标準錯誤重定向本地路徑
        :type StderrLocalPath: str
        :param StdoutLocalFileName: 标準輸出重定向本地文件名，支援三個占位符${BATCH_JOB_ID}、${BATCH_TASK_NAME}、${BATCH_TASK_INSTANCE_INDEX}
        :type StdoutLocalFileName: str
        :param StderrLocalFileName: 标準錯誤重定向本地文件名，支援三個占位符${BATCH_JOB_ID}、${BATCH_TASK_NAME}、${BATCH_TASK_INSTANCE_INDEX}
        :type StderrLocalFileName: str
        """
        self.StdoutLocalPath = None
        self.StderrLocalPath = None
        self.StdoutLocalFileName = None
        self.StderrLocalFileName = None


    def _deserialize(self, params):
        self.StdoutLocalPath = params.get("StdoutLocalPath")
        self.StderrLocalPath = params.get("StderrLocalPath")
        self.StdoutLocalFileName = params.get("StdoutLocalFileName")
        self.StderrLocalFileName = params.get("StderrLocalFileName")


class RetryJobsRequest(AbstractModel):
    """RetryJobs請求參數結構體

    """

    def __init__(self):
        """
        :param JobIds: 作業ID清單。
        :type JobIds: list of str
        """
        self.JobIds = None


    def _deserialize(self, params):
        self.JobIds = params.get("JobIds")


class RetryJobsResponse(AbstractModel):
    """RetryJobs返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


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


class SpotMarketOptions(AbstractModel):
    """競價相關選項

    """

    def __init__(self):
        """
        :param MaxPrice: 競價出價
        :type MaxPrice: str
        :param SpotInstanceType: 競價請求類型，當前僅支援類型：one-time
        :type SpotInstanceType: str
        """
        self.MaxPrice = None
        self.SpotInstanceType = None


    def _deserialize(self, params):
        self.MaxPrice = params.get("MaxPrice")
        self.SpotInstanceType = params.get("SpotInstanceType")


class StorageBlock(AbstractModel):
    """HDD的本地儲存訊息

    """

    def __init__(self):
        """
        :param Type: HDD本地儲存類型，值爲：LOCAL_PRO.
注意：此欄位可能返回 null，表示取不到有效值。
        :type Type: str
        :param MinSize: HDD本地儲存的最小容量
注意：此欄位可能返回 null，表示取不到有效值。
        :type MinSize: int
        :param MaxSize: HDD本地儲存的最大容量
注意：此欄位可能返回 null，表示取不到有效值。
        :type MaxSize: int
        """
        self.Type = None
        self.MinSize = None
        self.MaxSize = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.MinSize = params.get("MinSize")
        self.MaxSize = params.get("MaxSize")


class SubmitJobRequest(AbstractModel):
    """SubmitJob請求參數結構體

    """

    def __init__(self):
        """
        :param Placement: 作業所提交的位置訊息。通過該參數可以指定作業關聯CVM所屬可用區等訊息。
        :type Placement: :class:`taifucloudcloud.batch.v20170312.models.Placement`
        :param Job: 作業訊息
        :type Job: :class:`taifucloudcloud.batch.v20170312.models.Job`
        :param ClientToken: 用于保證請求幂等性的字串。該字串由用戶生成，需保證不同請求之間唯一，最大值不超過64個ASCII字元。若不指定該參數，則無法保證請求的幂等性。
        :type ClientToken: str
        """
        self.Placement = None
        self.Job = None
        self.ClientToken = None


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        if params.get("Job") is not None:
            self.Job = Job()
            self.Job._deserialize(params.get("Job"))
        self.ClientToken = params.get("ClientToken")


class SubmitJobResponse(AbstractModel):
    """SubmitJob返回參數結構體

    """

    def __init__(self):
        """
        :param JobId: 當通過本介面來提交作業時會返回該參數，表示一個作業ID。返回作業ID清單并不代表作業解析/運作成功，可根據 DescribeJob 介面查詢其狀态。
        :type JobId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class SystemDisk(AbstractModel):
    """描述了作業系統所在塊設備即系統盤的訊息

    """

    def __init__(self):
        """
        :param DiskType: 系統盤類型。系統盤類型限制詳見[儲存概述](https://cloud.taifucloud.com/document/product/213/4952)。取值範圍：<br><li>LOCAL_BASIC：本地硬碟<br><li>LOCAL_SSD：本地SSD硬碟<br><li>CLOUD_BASIC：普通雲硬碟<br><li>CLOUD_SSD：SSD雲硬碟<br><li>CLOUD_PREMIUM：高效能雲硬碟<br><br>預設取值：CLOUD_BASIC。
        :type DiskType: str
        :param DiskId: 系統盤ID。LOCAL_BASIC 和 LOCAL_SSD 類型沒有ID。暫時不支援該參數。
        :type DiskId: str
        :param DiskSize: 系統盤大小，單位：GB。預設值爲 50
        :type DiskSize: int
        """
        self.DiskType = None
        self.DiskId = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskId = params.get("DiskId")
        self.DiskSize = params.get("DiskSize")


class Task(AbstractModel):
    """任務

    """

    def __init__(self):
        """
        :param Application: 應用程式訊息
        :type Application: :class:`taifucloudcloud.batch.v20170312.models.Application`
        :param TaskName: 任務名稱，在一個作業内部唯一
        :type TaskName: str
        :param TaskInstanceNum: 任務實例運作個數
        :type TaskInstanceNum: int
        :param ComputeEnv: 運作環境訊息，ComputeEnv 和 EnvId 必須指定一個（且只有一個）參數。
        :type ComputeEnv: :class:`taifucloudcloud.batch.v20170312.models.AnonymousComputeEnv`
        :param EnvId: 計算環境ID，ComputeEnv 和 EnvId 必須指定一個（且只有一個）參數。
        :type EnvId: str
        :param RedirectInfo: 重定向訊息
        :type RedirectInfo: :class:`taifucloudcloud.batch.v20170312.models.RedirectInfo`
        :param RedirectLocalInfo: 重定向本地訊息
        :type RedirectLocalInfo: :class:`taifucloudcloud.batch.v20170312.models.RedirectLocalInfo`
        :param InputMappings: 輸入映射
        :type InputMappings: list of InputMapping
        :param OutputMappings: 輸出映射
        :type OutputMappings: list of OutputMapping
        :param OutputMappingConfigs: 輸出映射配置
        :type OutputMappingConfigs: list of OutputMappingConfig
        :param EnvVars: 自定義環境變量
        :type EnvVars: list of EnvVar
        :param Authentications: 授權訊息
        :type Authentications: list of Authentication
        :param FailedAction: TaskInstance失敗後處理方式，取值包括TERMINATE（預設）、INTERRUPT、FAST_INTERRUPT。
        :type FailedAction: str
        :param MaxRetryCount: 任務失敗後的最大重試次數，預設爲0
        :type MaxRetryCount: int
        :param Timeout: 任務啓動後的超時時間，單位秒，預設爲86400秒
        :type Timeout: int
        :param MaxConcurrentNum: 任務最大并發數限制，預設沒有限制。
        :type MaxConcurrentNum: int
        :param RestartComputeNode: 任務完成後，重啓計算節點。适用于指定計算環境執行任務。
        :type RestartComputeNode: bool
        :param ResourceMaxRetryCount: 啓動任務過程中，創建計算資源如CVM失敗後的最大重試次數，預設爲0。
        :type ResourceMaxRetryCount: int
        """
        self.Application = None
        self.TaskName = None
        self.TaskInstanceNum = None
        self.ComputeEnv = None
        self.EnvId = None
        self.RedirectInfo = None
        self.RedirectLocalInfo = None
        self.InputMappings = None
        self.OutputMappings = None
        self.OutputMappingConfigs = None
        self.EnvVars = None
        self.Authentications = None
        self.FailedAction = None
        self.MaxRetryCount = None
        self.Timeout = None
        self.MaxConcurrentNum = None
        self.RestartComputeNode = None
        self.ResourceMaxRetryCount = None


    def _deserialize(self, params):
        if params.get("Application") is not None:
            self.Application = Application()
            self.Application._deserialize(params.get("Application"))
        self.TaskName = params.get("TaskName")
        self.TaskInstanceNum = params.get("TaskInstanceNum")
        if params.get("ComputeEnv") is not None:
            self.ComputeEnv = AnonymousComputeEnv()
            self.ComputeEnv._deserialize(params.get("ComputeEnv"))
        self.EnvId = params.get("EnvId")
        if params.get("RedirectInfo") is not None:
            self.RedirectInfo = RedirectInfo()
            self.RedirectInfo._deserialize(params.get("RedirectInfo"))
        if params.get("RedirectLocalInfo") is not None:
            self.RedirectLocalInfo = RedirectLocalInfo()
            self.RedirectLocalInfo._deserialize(params.get("RedirectLocalInfo"))
        if params.get("InputMappings") is not None:
            self.InputMappings = []
            for item in params.get("InputMappings"):
                obj = InputMapping()
                obj._deserialize(item)
                self.InputMappings.append(obj)
        if params.get("OutputMappings") is not None:
            self.OutputMappings = []
            for item in params.get("OutputMappings"):
                obj = OutputMapping()
                obj._deserialize(item)
                self.OutputMappings.append(obj)
        if params.get("OutputMappingConfigs") is not None:
            self.OutputMappingConfigs = []
            for item in params.get("OutputMappingConfigs"):
                obj = OutputMappingConfig()
                obj._deserialize(item)
                self.OutputMappingConfigs.append(obj)
        if params.get("EnvVars") is not None:
            self.EnvVars = []
            for item in params.get("EnvVars"):
                obj = EnvVar()
                obj._deserialize(item)
                self.EnvVars.append(obj)
        if params.get("Authentications") is not None:
            self.Authentications = []
            for item in params.get("Authentications"):
                obj = Authentication()
                obj._deserialize(item)
                self.Authentications.append(obj)
        self.FailedAction = params.get("FailedAction")
        self.MaxRetryCount = params.get("MaxRetryCount")
        self.Timeout = params.get("Timeout")
        self.MaxConcurrentNum = params.get("MaxConcurrentNum")
        self.RestartComputeNode = params.get("RestartComputeNode")
        self.ResourceMaxRetryCount = params.get("ResourceMaxRetryCount")


class TaskInstanceLog(AbstractModel):
    """任務實例日志詳情。

    """

    def __init__(self):
        """
        :param TaskInstanceIndex: 任務實例
        :type TaskInstanceIndex: int
        :param StdoutLog: 标準輸出日志（Base64編碼）
注意：此欄位可能返回 null，表示取不到有效值。
        :type StdoutLog: str
        :param StderrLog: 标準錯誤日志（Base64編碼）
注意：此欄位可能返回 null，表示取不到有效值。
        :type StderrLog: str
        :param StdoutRedirectPath: 标準輸出重定向路徑
注意：此欄位可能返回 null，表示取不到有效值。
        :type StdoutRedirectPath: str
        :param StderrRedirectPath: 标準錯誤重定向路徑
注意：此欄位可能返回 null，表示取不到有效值。
        :type StderrRedirectPath: str
        :param StdoutRedirectFileName: 标準輸出重定向文件名
注意：此欄位可能返回 null，表示取不到有效值。
        :type StdoutRedirectFileName: str
        :param StderrRedirectFileName: 标準錯誤重定向文件名
注意：此欄位可能返回 null，表示取不到有效值。
        :type StderrRedirectFileName: str
        """
        self.TaskInstanceIndex = None
        self.StdoutLog = None
        self.StderrLog = None
        self.StdoutRedirectPath = None
        self.StderrRedirectPath = None
        self.StdoutRedirectFileName = None
        self.StderrRedirectFileName = None


    def _deserialize(self, params):
        self.TaskInstanceIndex = params.get("TaskInstanceIndex")
        self.StdoutLog = params.get("StdoutLog")
        self.StderrLog = params.get("StderrLog")
        self.StdoutRedirectPath = params.get("StdoutRedirectPath")
        self.StderrRedirectPath = params.get("StderrRedirectPath")
        self.StdoutRedirectFileName = params.get("StdoutRedirectFileName")
        self.StderrRedirectFileName = params.get("StderrRedirectFileName")


class TaskInstanceMetrics(AbstractModel):
    """任務實例統計指标

    """

    def __init__(self):
        """
        :param SubmittedCount: Submitted個數
        :type SubmittedCount: int
        :param PendingCount: Pending個數
        :type PendingCount: int
        :param RunnableCount: Runnable個數
        :type RunnableCount: int
        :param StartingCount: Starting個數
        :type StartingCount: int
        :param RunningCount: Running個數
        :type RunningCount: int
        :param SucceedCount: Succeed個數
        :type SucceedCount: int
        :param FailedInterruptedCount: FailedInterrupted個數
        :type FailedInterruptedCount: int
        :param FailedCount: Failed個數
        :type FailedCount: int
        """
        self.SubmittedCount = None
        self.PendingCount = None
        self.RunnableCount = None
        self.StartingCount = None
        self.RunningCount = None
        self.SucceedCount = None
        self.FailedInterruptedCount = None
        self.FailedCount = None


    def _deserialize(self, params):
        self.SubmittedCount = params.get("SubmittedCount")
        self.PendingCount = params.get("PendingCount")
        self.RunnableCount = params.get("RunnableCount")
        self.StartingCount = params.get("StartingCount")
        self.RunningCount = params.get("RunningCount")
        self.SucceedCount = params.get("SucceedCount")
        self.FailedInterruptedCount = params.get("FailedInterruptedCount")
        self.FailedCount = params.get("FailedCount")


class TaskInstanceView(AbstractModel):
    """任務實例視圖訊息

    """

    def __init__(self):
        """
        :param TaskInstanceIndex: 任務實例索引
        :type TaskInstanceIndex: int
        :param TaskInstanceState: 任務實例狀态
        :type TaskInstanceState: str
        :param ExitCode: 應用程式執行結束的exit code
注意：此欄位可能返回 null，表示取不到有效值。
        :type ExitCode: int
        :param StateReason: 任務實例狀态原因，任務實例失敗時，會記錄失敗原因
        :type StateReason: str
        :param ComputeNodeInstanceId: 任務實例運作時所在計算節點（例如CVM）的InstanceId。任務實例未運作或者完結時，本欄位爲空。任務實例重試時，本欄位會随之變化
注意：此欄位可能返回 null，表示取不到有效值。
        :type ComputeNodeInstanceId: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param LaunchTime: 啓動時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type LaunchTime: str
        :param RunningTime: 開始運作時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type RunningTime: str
        :param EndTime: 結束時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param RedirectInfo: 重定向訊息
        :type RedirectInfo: :class:`taifucloudcloud.batch.v20170312.models.RedirectInfo`
        :param StateDetailedReason: 任務實例狀态原因詳情，任務實例失敗時，會記錄失敗原因
        :type StateDetailedReason: str
        """
        self.TaskInstanceIndex = None
        self.TaskInstanceState = None
        self.ExitCode = None
        self.StateReason = None
        self.ComputeNodeInstanceId = None
        self.CreateTime = None
        self.LaunchTime = None
        self.RunningTime = None
        self.EndTime = None
        self.RedirectInfo = None
        self.StateDetailedReason = None


    def _deserialize(self, params):
        self.TaskInstanceIndex = params.get("TaskInstanceIndex")
        self.TaskInstanceState = params.get("TaskInstanceState")
        self.ExitCode = params.get("ExitCode")
        self.StateReason = params.get("StateReason")
        self.ComputeNodeInstanceId = params.get("ComputeNodeInstanceId")
        self.CreateTime = params.get("CreateTime")
        self.LaunchTime = params.get("LaunchTime")
        self.RunningTime = params.get("RunningTime")
        self.EndTime = params.get("EndTime")
        if params.get("RedirectInfo") is not None:
            self.RedirectInfo = RedirectInfo()
            self.RedirectInfo._deserialize(params.get("RedirectInfo"))
        self.StateDetailedReason = params.get("StateDetailedReason")


class TaskMetrics(AbstractModel):
    """任務統計指标

    """

    def __init__(self):
        """
        :param SubmittedCount: Submitted個數
        :type SubmittedCount: int
        :param PendingCount: Pending個數
        :type PendingCount: int
        :param RunnableCount: Runnable個數
        :type RunnableCount: int
        :param StartingCount: Starting個數
        :type StartingCount: int
        :param RunningCount: Running個數
        :type RunningCount: int
        :param SucceedCount: Succeed個數
        :type SucceedCount: int
        :param FailedInterruptedCount: FailedInterrupted個數
        :type FailedInterruptedCount: int
        :param FailedCount: Failed個數
        :type FailedCount: int
        """
        self.SubmittedCount = None
        self.PendingCount = None
        self.RunnableCount = None
        self.StartingCount = None
        self.RunningCount = None
        self.SucceedCount = None
        self.FailedInterruptedCount = None
        self.FailedCount = None


    def _deserialize(self, params):
        self.SubmittedCount = params.get("SubmittedCount")
        self.PendingCount = params.get("PendingCount")
        self.RunnableCount = params.get("RunnableCount")
        self.StartingCount = params.get("StartingCount")
        self.RunningCount = params.get("RunningCount")
        self.SucceedCount = params.get("SucceedCount")
        self.FailedInterruptedCount = params.get("FailedInterruptedCount")
        self.FailedCount = params.get("FailedCount")


class TaskTemplateView(AbstractModel):
    """任務範本訊息

    """

    def __init__(self):
        """
        :param TaskTemplateId: 任務範本ID
        :type TaskTemplateId: str
        :param TaskTemplateName: 任務範本名稱
        :type TaskTemplateName: str
        :param TaskTemplateDescription: 任務範本描述
        :type TaskTemplateDescription: str
        :param TaskTemplateInfo: 任務範本訊息
        :type TaskTemplateInfo: :class:`taifucloudcloud.batch.v20170312.models.Task`
        :param CreateTime: 創建時間
        :type CreateTime: str
        """
        self.TaskTemplateId = None
        self.TaskTemplateName = None
        self.TaskTemplateDescription = None
        self.TaskTemplateInfo = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.TaskTemplateId = params.get("TaskTemplateId")
        self.TaskTemplateName = params.get("TaskTemplateName")
        self.TaskTemplateDescription = params.get("TaskTemplateDescription")
        if params.get("TaskTemplateInfo") is not None:
            self.TaskTemplateInfo = Task()
            self.TaskTemplateInfo._deserialize(params.get("TaskTemplateInfo"))
        self.CreateTime = params.get("CreateTime")


class TaskView(AbstractModel):
    """任務視圖訊息

    """

    def __init__(self):
        """
        :param TaskName: 任務名稱
        :type TaskName: str
        :param TaskState: 任務狀态
        :type TaskState: str
        :param CreateTime: 開始時間
        :type CreateTime: str
        :param EndTime: 結束時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self.TaskName = None
        self.TaskState = None
        self.CreateTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.TaskName = params.get("TaskName")
        self.TaskState = params.get("TaskState")
        self.CreateTime = params.get("CreateTime")
        self.EndTime = params.get("EndTime")


class TerminateComputeNodeRequest(AbstractModel):
    """TerminateComputeNode請求參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 計算環境ID
        :type EnvId: str
        :param ComputeNodeId: 計算節點ID
        :type ComputeNodeId: str
        """
        self.EnvId = None
        self.ComputeNodeId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ComputeNodeId = params.get("ComputeNodeId")


class TerminateComputeNodeResponse(AbstractModel):
    """TerminateComputeNode返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TerminateComputeNodesRequest(AbstractModel):
    """TerminateComputeNodes請求參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 計算環境ID
        :type EnvId: str
        :param ComputeNodeIds: 計算節點ID清單
        :type ComputeNodeIds: list of str
        """
        self.EnvId = None
        self.ComputeNodeIds = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ComputeNodeIds = params.get("ComputeNodeIds")


class TerminateComputeNodesResponse(AbstractModel):
    """TerminateComputeNodes返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TerminateJobRequest(AbstractModel):
    """TerminateJob請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 作業ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class TerminateJobResponse(AbstractModel):
    """TerminateJob返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TerminateTaskInstanceRequest(AbstractModel):
    """TerminateTaskInstance請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 作業ID
        :type JobId: str
        :param TaskName: 任務名稱
        :type TaskName: str
        :param TaskInstanceIndex: 任務實例索引
        :type TaskInstanceIndex: int
        """
        self.JobId = None
        self.TaskName = None
        self.TaskInstanceIndex = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.TaskName = params.get("TaskName")
        self.TaskInstanceIndex = params.get("TaskInstanceIndex")


class TerminateTaskInstanceResponse(AbstractModel):
    """TerminateTaskInstance返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class VirtualPrivateCloud(AbstractModel):
    """描述了VPC相關訊息，包括子網，IP訊息等

    """

    def __init__(self):
        """
        :param VpcId: 私有網絡ID，形如`vpc-xxx`。有效的VpcId可通過登入[控制台](https://console.cloud.taifucloud.com/vpc/vpc?rid=1)查詢；也可以調用介面 [DescribeVpcEx](/document/api/215/1372) ，從介面返回中的`unVpcId`欄位獲取。若在創建子機時VpcId與SubnetId同時傳入`DEFAULT`，則強制使用預設vpc網絡。
        :type VpcId: str
        :param SubnetId: 私有網絡子網ID，形如`subnet-xxx`。有效的私有網絡子網ID可通過登入[控制台](https://console.cloud.taifucloud.com/vpc/subnet?rid=1)查詢；也可以調用介面  [DescribeSubnets](/document/api/215/15784) ，從介面返回中的`unSubnetId`欄位獲取。若在創建子機時SubnetId與VpcId同時傳入`DEFAULT`，則強制使用預設vpc網絡。
        :type SubnetId: str
        :param AsVpcGateway: 是否用作公網閘道。公網閘道只有在實例擁有公網IP以及處于私有網絡下時才能正常使用。取值範圍：<br><li>TRUE：表示用作公網閘道<br><li>FALSE：表示不用作公網閘道<br><br>預設取值：FALSE。
        :type AsVpcGateway: bool
        :param PrivateIpAddresses: 私有網絡子網 IP 數組，在創建實例、修改實例vpc屬性操作中可使用此參數。當前僅批次創建多台實例時支援傳入相同子網的多個 IP。
        :type PrivateIpAddresses: list of str
        :param Ipv6AddressCount: 爲彈性網卡指定随機生成的 IPv6 網址數量。
        :type Ipv6AddressCount: int
        """
        self.VpcId = None
        self.SubnetId = None
        self.AsVpcGateway = None
        self.PrivateIpAddresses = None
        self.Ipv6AddressCount = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.AsVpcGateway = params.get("AsVpcGateway")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.Ipv6AddressCount = params.get("Ipv6AddressCount")