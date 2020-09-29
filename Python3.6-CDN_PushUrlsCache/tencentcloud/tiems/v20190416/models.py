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


class Conditions(AbstractModel):
    """狀态

    """

    def __init__(self):
        """
        :param Reason: 原因
        :type Reason: str
        :param Count: 具有相同原因的副本個數
        :type Count: int
        """
        self.Reason = None
        self.Count = None


    def _deserialize(self, params):
        self.Reason = params.get("Reason")
        self.Count = params.get("Count")


class Config(AbstractModel):
    """配置

    """

    def __init__(self):
        """
        :param Id: Id
        :type Id: str
        :param Name: 配置名
        :type Name: str
        :param ModelUri: 模型網址
        :type ModelUri: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param Runtime: 運作環境
        :type Runtime: str
        :param Version: 配置版本
        :type Version: str
        :param UpdateTime: 更新時間
        :type UpdateTime: str
        :param Description: 配置描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type Description: str
        """
        self.Id = None
        self.Name = None
        self.ModelUri = None
        self.CreateTime = None
        self.Runtime = None
        self.Version = None
        self.UpdateTime = None
        self.Description = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.ModelUri = params.get("ModelUri")
        self.CreateTime = params.get("CreateTime")
        self.Runtime = params.get("Runtime")
        self.Version = params.get("Version")
        self.UpdateTime = params.get("UpdateTime")
        self.Description = params.get("Description")


class CreateJobRequest(AbstractModel):
    """CreateJob請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 任務名稱
        :type Name: str
        :param ResourceGroupId: 使用的資源組 Id，預設使用共享資源組
        :type ResourceGroupId: str
        :param Cpu: 處理器配置, 單位爲1/1000核；範圍[100, 256000]
        :type Cpu: int
        :param Memory: 内存配置, 單位爲1M；範圍[100, 256000]
        :type Memory: int
        :param Cluster: 運作集群
        :type Cluster: str
        :param PredictInput: 預測輸入
        :type PredictInput: :class:`taifucloudcloud.tiems.v20190416.models.PredictInput`
        :param Description: 任務描述
        :type Description: str
        :param WorkerCount: 同時處理任務的 Worker 個數
        :type WorkerCount: int
        :param ConfigId: 使用的配置 Id
        :type ConfigId: str
        :param Gpu: GPU算力配置，單位爲1/1000 卡，範圍 [0, 256000]
        :type Gpu: int
        :param GpuMemory: 顯存配置, 單位爲1M，範圍 [0, 256000]
        :type GpuMemory: int
        :param GpuType: GPU類型
        :type GpuType: str
        :param QuantizationInput: 量化輸入
        :type QuantizationInput: :class:`taifucloudcloud.tiems.v20190416.models.QuantizationInput`
        :param LogTopicId: Cls日志主題ID
        :type LogTopicId: str
        """
        self.Name = None
        self.ResourceGroupId = None
        self.Cpu = None
        self.Memory = None
        self.Cluster = None
        self.PredictInput = None
        self.Description = None
        self.WorkerCount = None
        self.ConfigId = None
        self.Gpu = None
        self.GpuMemory = None
        self.GpuType = None
        self.QuantizationInput = None
        self.LogTopicId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ResourceGroupId = params.get("ResourceGroupId")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Cluster = params.get("Cluster")
        if params.get("PredictInput") is not None:
            self.PredictInput = PredictInput()
            self.PredictInput._deserialize(params.get("PredictInput"))
        self.Description = params.get("Description")
        self.WorkerCount = params.get("WorkerCount")
        self.ConfigId = params.get("ConfigId")
        self.Gpu = params.get("Gpu")
        self.GpuMemory = params.get("GpuMemory")
        self.GpuType = params.get("GpuType")
        if params.get("QuantizationInput") is not None:
            self.QuantizationInput = QuantizationInput()
            self.QuantizationInput._deserialize(params.get("QuantizationInput"))
        self.LogTopicId = params.get("LogTopicId")


class CreateJobResponse(AbstractModel):
    """CreateJob返回參數結構體

    """

    def __init__(self):
        """
        :param Job: 任務
        :type Job: :class:`taifucloudcloud.tiems.v20190416.models.Job`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Job = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Job") is not None:
            self.Job = Job()
            self.Job._deserialize(params.get("Job"))
        self.RequestId = params.get("RequestId")


class CreateRsgAsGroupRequest(AbstractModel):
    """CreateRsgAsGroup請求參數結構體

    """

    def __init__(self):
        """
        :param RsgId: 資源組 ID
        :type RsgId: str
        :param MaxSize: 伸縮組允許的最大節點數
        :type MaxSize: int
        :param MinSize: 伸縮組允許的最小節點數
        :type MinSize: int
        :param InstanceType: 伸縮組的節點規格
        :type InstanceType: str
        :param Cluster: 資源組所在的集群名
        :type Cluster: str
        :param Name: 伸縮組名稱
        :type Name: str
        :param DesiredSize: 伸縮組期望的節點數
        :type DesiredSize: int
        """
        self.RsgId = None
        self.MaxSize = None
        self.MinSize = None
        self.InstanceType = None
        self.Cluster = None
        self.Name = None
        self.DesiredSize = None


    def _deserialize(self, params):
        self.RsgId = params.get("RsgId")
        self.MaxSize = params.get("MaxSize")
        self.MinSize = params.get("MinSize")
        self.InstanceType = params.get("InstanceType")
        self.Cluster = params.get("Cluster")
        self.Name = params.get("Name")
        self.DesiredSize = params.get("DesiredSize")


class CreateRsgAsGroupResponse(AbstractModel):
    """CreateRsgAsGroup返回參數結構體

    """

    def __init__(self):
        """
        :param RsgAsGroup: 所創建的資源組的伸縮組
        :type RsgAsGroup: :class:`taifucloudcloud.tiems.v20190416.models.RsgAsGroup`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RsgAsGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RsgAsGroup") is not None:
            self.RsgAsGroup = RsgAsGroup()
            self.RsgAsGroup._deserialize(params.get("RsgAsGroup"))
        self.RequestId = params.get("RequestId")


class CreateRuntimeRequest(AbstractModel):
    """CreateRuntime請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 全局唯一的運作環境名稱
        :type Name: str
        :param Image: 運作環境映像網址
        :type Image: str
        :param Framework: 運作環境框架
        :type Framework: str
        :param Description: 運作環境描述
        :type Description: str
        :param HealthCheckOn: 是否支援健康檢查，預設爲False
        :type HealthCheckOn: bool
        """
        self.Name = None
        self.Image = None
        self.Framework = None
        self.Description = None
        self.HealthCheckOn = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Image = params.get("Image")
        self.Framework = params.get("Framework")
        self.Description = params.get("Description")
        self.HealthCheckOn = params.get("HealthCheckOn")


class CreateRuntimeResponse(AbstractModel):
    """CreateRuntime返回參數結構體

    """

    def __init__(self):
        """
        :param Runtime: 運作環境
        :type Runtime: :class:`taifucloudcloud.tiems.v20190416.models.Runtime`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Runtime = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Runtime") is not None:
            self.Runtime = Runtime()
            self.Runtime._deserialize(params.get("Runtime"))
        self.RequestId = params.get("RequestId")


class CreateServiceConfigRequest(AbstractModel):
    """CreateServiceConfig請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 配置名稱
        :type Name: str
        :param Runtime: 運作環境
        :type Runtime: str
        :param ModelUri: 模型網址，支援cos路徑，格式爲 cos://bucket名-appid.cos.region名.myqcloud.com/模型文件夾路徑。爲模型文件的上一層文件夾網址。
        :type ModelUri: str
        :param Description: 配置描述
        :type Description: str
        """
        self.Name = None
        self.Runtime = None
        self.ModelUri = None
        self.Description = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Runtime = params.get("Runtime")
        self.ModelUri = params.get("ModelUri")
        self.Description = params.get("Description")


class CreateServiceConfigResponse(AbstractModel):
    """CreateServiceConfig返回參數結構體

    """

    def __init__(self):
        """
        :param ServiceConfig: 服務配置
        :type ServiceConfig: :class:`taifucloudcloud.tiems.v20190416.models.Config`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ServiceConfig = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ServiceConfig") is not None:
            self.ServiceConfig = Config()
            self.ServiceConfig._deserialize(params.get("ServiceConfig"))
        self.RequestId = params.get("RequestId")


class CreateServiceRequest(AbstractModel):
    """CreateService請求參數結構體

    """

    def __init__(self):
        """
        :param Scaler: 擴縮容配置
        :type Scaler: :class:`taifucloudcloud.tiems.v20190416.models.Scaler`
        :param ServiceConfigId: 服務配置Id
        :type ServiceConfigId: str
        :param Name: 服務名稱
        :type Name: str
        :param ScaleMode: 擴縮容方式，支援AUTO, MANUAL，分别表示自動擴縮容和手動擴縮容
        :type ScaleMode: str
        :param ResourceGroupId: 佈署要使用的資源組Id，預設爲共享資源組
        :type ResourceGroupId: str
        :param Cpu: 處理器配置, 單位爲1/1000核；範圍[100, 256000]
        :type Cpu: int
        :param Memory: 内存配置, 單位爲1M；範圍[100, 256000]
        :type Memory: int
        :param Cluster: 集群，不填則使用預設集群
        :type Cluster: str
        :param Authentication: 預設爲空，表示不需要鑒權，TOKEN 表示選擇 Token 鑒權方式
        :type Authentication: str
        :param Gpu: GPU算力配置，單位爲1/1000 卡，範圍 [0, 256000]
        :type Gpu: int
        :param GpuMemory: 顯存配置, 單位爲1M，範圍 [0, 256000]
        :type GpuMemory: int
        :param Description: 備注
        :type Description: str
        :param GpuType: GPU類型
        :type GpuType: str
        :param LogTopicId: Cls日志主題ID
        :type LogTopicId: str
        """
        self.Scaler = None
        self.ServiceConfigId = None
        self.Name = None
        self.ScaleMode = None
        self.ResourceGroupId = None
        self.Cpu = None
        self.Memory = None
        self.Cluster = None
        self.Authentication = None
        self.Gpu = None
        self.GpuMemory = None
        self.Description = None
        self.GpuType = None
        self.LogTopicId = None


    def _deserialize(self, params):
        if params.get("Scaler") is not None:
            self.Scaler = Scaler()
            self.Scaler._deserialize(params.get("Scaler"))
        self.ServiceConfigId = params.get("ServiceConfigId")
        self.Name = params.get("Name")
        self.ScaleMode = params.get("ScaleMode")
        self.ResourceGroupId = params.get("ResourceGroupId")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Cluster = params.get("Cluster")
        self.Authentication = params.get("Authentication")
        self.Gpu = params.get("Gpu")
        self.GpuMemory = params.get("GpuMemory")
        self.Description = params.get("Description")
        self.GpuType = params.get("GpuType")
        self.LogTopicId = params.get("LogTopicId")


class CreateServiceResponse(AbstractModel):
    """CreateService返回參數結構體

    """

    def __init__(self):
        """
        :param Service: 服務
        :type Service: :class:`taifucloudcloud.tiems.v20190416.models.ModelService`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Service = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Service") is not None:
            self.Service = ModelService()
            self.Service._deserialize(params.get("Service"))
        self.RequestId = params.get("RequestId")


class DeleteInstanceRequest(AbstractModel):
    """DeleteInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 要删除的節點 ID
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


class DeleteJobRequest(AbstractModel):
    """DeleteJob請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 任務 Id
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


class DeleteResourceGroupRequest(AbstractModel):
    """DeleteResourceGroup請求參數結構體

    """

    def __init__(self):
        """
        :param ResourceGroupId: 要删除的資源組 ID
        :type ResourceGroupId: str
        """
        self.ResourceGroupId = None


    def _deserialize(self, params):
        self.ResourceGroupId = params.get("ResourceGroupId")


class DeleteResourceGroupResponse(AbstractModel):
    """DeleteResourceGroup返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRsgAsGroupRequest(AbstractModel):
    """DeleteRsgAsGroup請求參數結構體

    """

    def __init__(self):
        """
        :param Id: 伸縮組 ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")


class DeleteRsgAsGroupResponse(AbstractModel):
    """DeleteRsgAsGroup返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRuntimeRequest(AbstractModel):
    """DeleteRuntime請求參數結構體

    """

    def __init__(self):
        """
        :param Runtime: 要删除的Runtime名
        :type Runtime: str
        """
        self.Runtime = None


    def _deserialize(self, params):
        self.Runtime = params.get("Runtime")


class DeleteRuntimeResponse(AbstractModel):
    """DeleteRuntime返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteServiceConfigRequest(AbstractModel):
    """DeleteServiceConfig請求參數結構體

    """

    def __init__(self):
        """
        :param ServiceConfigId: 服務配置Id
        :type ServiceConfigId: str
        :param ServiceConfigName: 服務配置名稱
        :type ServiceConfigName: str
        """
        self.ServiceConfigId = None
        self.ServiceConfigName = None


    def _deserialize(self, params):
        self.ServiceConfigId = params.get("ServiceConfigId")
        self.ServiceConfigName = params.get("ServiceConfigName")


class DeleteServiceConfigResponse(AbstractModel):
    """DeleteServiceConfig返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteServiceRequest(AbstractModel):
    """DeleteService請求參數結構體

    """

    def __init__(self):
        """
        :param ServiceId: 服務Id
        :type ServiceId: str
        """
        self.ServiceId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")


class DeleteServiceResponse(AbstractModel):
    """DeleteService返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 篩選選項
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲200
        :type Limit: int
        :param Order: 輸出清單的排列順序。取值範圍：ASC：升序排列 DESC：降序排列
        :type Order: str
        :param OrderField: 排序的依據欄位， 取值範圍 "CREATE_TIME", "UPDATE_TIME", "NAME"
        :type OrderField: str
        :param ResourceGroupId: 要查詢的資源組 ID
        :type ResourceGroupId: str
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderField = None
        self.ResourceGroupId = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")
        self.ResourceGroupId = params.get("ResourceGroupId")


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 資源組下節點總數
        :type TotalCount: int
        :param Instances: 資源組下節點清單
        :type Instances: list of Instance
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Instances = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = Instance()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResourceGroupsRequest(AbstractModel):
    """DescribeResourceGroups請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 篩選選項
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲200
        :type Limit: int
        :param Order: 輸出清單的排列順序。取值範圍：ASC：升序排列 DESC：降序排列
        :type Order: str
        :param OrderField: 排序的依據欄位， 取值範圍 "CREATE_TIME", "UPDATE_TIME", "NAME"
        :type OrderField: str
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderField = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")


class DescribeResourceGroupsResponse(AbstractModel):
    """DescribeResourceGroups返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 資源組總數
        :type TotalCount: int
        :param ResourceGroups: 資源組清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResourceGroups: list of ResourceGroup
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ResourceGroups = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ResourceGroups") is not None:
            self.ResourceGroups = []
            for item in params.get("ResourceGroups"):
                obj = ResourceGroup()
                obj._deserialize(item)
                self.ResourceGroups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRsgAsGroupActivitiesRequest(AbstractModel):
    """DescribeRsgAsGroupActivities請求參數結構體

    """

    def __init__(self):
        """
        :param Id: 伸縮組 ID
        :type Id: str
        :param StartTime: 查詢活動的開始時間
        :type StartTime: str
        :param EndTime: 查詢互動的結束時間
        :type EndTime: str
        :param Filters: 篩選選項
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲 0
        :type Offset: int
        :param Limit: 返回數量，預設爲 20，最大值爲 200
        :type Limit: int
        :param Order: 輸出清單的排列順序。取值範圍："ASC", "DESC"
        :type Order: str
        :param OrderField: 排序的依據欄位， 取值範圍 "CREATE_TIME", "UPDATE_TIME", "NAME"
        :type OrderField: str
        """
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderField = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")


class DescribeRsgAsGroupActivitiesResponse(AbstractModel):
    """DescribeRsgAsGroupActivities返回參數結構體

    """

    def __init__(self):
        """
        :param RsgAsGroupActivitySet: 伸縮組活動數組
注意：此欄位可能返回 null，表示取不到有效值。
        :type RsgAsGroupActivitySet: list of RsgAsGroupActivity
        :param TotalCount: 所查詢的伸縮組活動總數目
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RsgAsGroupActivitySet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RsgAsGroupActivitySet") is not None:
            self.RsgAsGroupActivitySet = []
            for item in params.get("RsgAsGroupActivitySet"):
                obj = RsgAsGroupActivity()
                obj._deserialize(item)
                self.RsgAsGroupActivitySet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRsgAsGroupsRequest(AbstractModel):
    """DescribeRsgAsGroups請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 篩選選項
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲 0
        :type Offset: int
        :param Limit: 返回數量，預設爲 20，最大值爲 200
        :type Limit: int
        :param Order: 輸出清單的排列順序。取值範圍："ASC", "DESC"
        :type Order: str
        :param OrderField: 排序的依據欄位， 取值範圍 "CREATE_TIME", "UPDATE_TIME", "NAME"
        :type OrderField: str
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderField = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")


class DescribeRsgAsGroupsResponse(AbstractModel):
    """DescribeRsgAsGroups返回參數結構體

    """

    def __init__(self):
        """
        :param RsgAsGroupSet: 所查詢的伸縮組數組
        :type RsgAsGroupSet: list of RsgAsGroup
        :param TotalCount: 伸縮組數組總數目
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RsgAsGroupSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RsgAsGroupSet") is not None:
            self.RsgAsGroupSet = []
            for item in params.get("RsgAsGroupSet"):
                obj = RsgAsGroup()
                obj._deserialize(item)
                self.RsgAsGroupSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRuntimesRequest(AbstractModel):
    """DescribeRuntimes請求參數結構體

    """


class DescribeRuntimesResponse(AbstractModel):
    """DescribeRuntimes返回參數結構體

    """

    def __init__(self):
        """
        :param Runtimes: TIEMS支援的運作環境清單
        :type Runtimes: list of Runtime
        :param UserAccess: 用戶對runtime對權限
注意：此欄位可能返回 null，表示取不到有效值。
        :type UserAccess: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Runtimes = None
        self.UserAccess = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Runtimes") is not None:
            self.Runtimes = []
            for item in params.get("Runtimes"):
                obj = Runtime()
                obj._deserialize(item)
                self.Runtimes.append(obj)
        self.UserAccess = params.get("UserAccess")
        self.RequestId = params.get("RequestId")


class DescribeServiceConfigsRequest(AbstractModel):
    """DescribeServiceConfigs請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 篩選選項，支援按照name等進行篩選
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲1000
        :type Limit: int
        :param Order: 輸出清單的排列順序。取值範圍：ASC：升序排列 DESC：降序排列
        :type Order: str
        :param OrderField: 排序的依據欄位， 取值範圍 "CREATE_TIME", "UPDATE_TIME", "NAME"
        :type OrderField: str
        :param PageByName: 是否按照配置名分頁
        :type PageByName: bool
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderField = None
        self.PageByName = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")
        self.PageByName = params.get("PageByName")


class DescribeServiceConfigsResponse(AbstractModel):
    """DescribeServiceConfigs返回參數結構體

    """

    def __init__(self):
        """
        :param ServiceConfigs: 服務配置
        :type ServiceConfigs: list of Config
        :param TotalCount: 服務配置總數
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ServiceConfigs = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ServiceConfigs") is not None:
            self.ServiceConfigs = []
            for item in params.get("ServiceConfigs"):
                obj = Config()
                obj._deserialize(item)
                self.ServiceConfigs.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeServicesRequest(AbstractModel):
    """DescribeServices請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 篩選選項，支援篩選的欄位：id, region, zone, cluster, status, runtime, rsg_id
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100
        :type Limit: int
        :param Order: 輸出清單的排列順序。取值範圍：ASC：升序排列 DESC：降序排列
        :type Order: str
        :param OrderField: 排序的依據欄位， 取值範圍 "CREATE_TIME" "UPDATE_TIME"
        :type OrderField: str
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderField = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")


class DescribeServicesResponse(AbstractModel):
    """DescribeServices返回參數結構體

    """

    def __init__(self):
        """
        :param Services: 服務清單
        :type Services: list of ModelService
        :param TotalCount: 服務總數
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Services = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Services") is not None:
            self.Services = []
            for item in params.get("Services"):
                obj = ModelService()
                obj._deserialize(item)
                self.Services.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DisableRsgAsGroupRequest(AbstractModel):
    """DisableRsgAsGroup請求參數結構體

    """

    def __init__(self):
        """
        :param Id: 伸縮組 ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")


class DisableRsgAsGroupResponse(AbstractModel):
    """DisableRsgAsGroup返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableRsgAsGroupRequest(AbstractModel):
    """EnableRsgAsGroup請求參數結構體

    """

    def __init__(self):
        """
        :param Id: 伸縮組 ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")


class EnableRsgAsGroupResponse(AbstractModel):
    """EnableRsgAsGroup返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ExposeInfo(AbstractModel):
    """暴露訊息

    """

    def __init__(self):
        """
        :param ExposeType: 暴露方式，支援 EXTERNAL（外網暴露），VPC （VPC内網打通）
        :type ExposeType: str
        :param Ip: 暴露Ip。暴露方式爲 EXTERNAL 爲外網 Ip，暴露方式爲 VPC 時爲指定 Vpc 下的Vip
        :type Ip: str
        :param VpcId: 暴露方式爲 VPC 時，打通的私有網絡Id
注意：此欄位可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param SubnetId: 暴露方式爲 VPC 時，打通的子網Id
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param GateWayServiceId: GATEWAY 服務id，ExposeType = GATEWAY 時返回
注意：此欄位可能返回 null，表示取不到有效值。
        :type GateWayServiceId: str
        :param GateWayAPIId: GATEWAY api id，ExposeType = GATEWAY 時返回
注意：此欄位可能返回 null，表示取不到有效值。
        :type GateWayAPIId: str
        :param GateWayDomain: GATEWAY domain，ExposeType = GATEWAY 時返回
注意：此欄位可能返回 null，表示取不到有效值。
        :type GateWayDomain: str
        """
        self.ExposeType = None
        self.Ip = None
        self.VpcId = None
        self.SubnetId = None
        self.GateWayServiceId = None
        self.GateWayAPIId = None
        self.GateWayDomain = None


    def _deserialize(self, params):
        self.ExposeType = params.get("ExposeType")
        self.Ip = params.get("Ip")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.GateWayServiceId = params.get("GateWayServiceId")
        self.GateWayAPIId = params.get("GateWayAPIId")
        self.GateWayDomain = params.get("GateWayDomain")


class ExposeServiceRequest(AbstractModel):
    """ExposeService請求參數結構體

    """

    def __init__(self):
        """
        :param ServiceId: 服務Id
        :type ServiceId: str
        :param ExposeType: 暴露方式，支援 EXTERNAL（外網暴露），VPC （VPC内網打通）
        :type ExposeType: str
        :param VpcId: 暴露方式爲 VPC 時，填寫需要打通的私有網絡Id
        :type VpcId: str
        :param SubnetId: 暴露方式爲 VPC 時，填寫需要打通的子網Id
        :type SubnetId: str
        """
        self.ServiceId = None
        self.ExposeType = None
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ExposeType = params.get("ExposeType")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")


class ExposeServiceResponse(AbstractModel):
    """ExposeService返回參數結構體

    """

    def __init__(self):
        """
        :param Expose: 暴露方式
        :type Expose: :class:`taifucloudcloud.tiems.v20190416.models.ExposeInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Expose = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Expose") is not None:
            self.Expose = ExposeInfo()
            self.Expose._deserialize(params.get("Expose"))
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """篩選項

    """

    def __init__(self):
        """
        :param Name: 名稱
        :type Name: str
        :param Values: 取值
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class Instance(AbstractModel):
    """節點

    """

    def __init__(self):
        """
        :param Id: 節點 ID
        :type Id: str
        :param Zone: 節點所在地區
        :type Zone: str
        :param InstanceType: 節點類型
        :type InstanceType: str
        :param InstanceChargeType: 節點儲值類型
        :type InstanceChargeType: str
        :param Cpu: Cpu 核數
        :type Cpu: int
        :param Memory: 内存
        :type Memory: int
        :param Gpu: Gpu 核數
        :type Gpu: int
        :param State: 節點狀态
        :type State: str
        :param AbnormalReason: 節點故障訊息
        :type AbnormalReason: str
        :param Created: 創建時間
        :type Created: str
        :param Updated: 更新時間
        :type Updated: str
        :param DeadlineTime: 到期時間
        :type DeadlineTime: str
        :param ResourceGroupId: 所屬資源組 ID
        :type ResourceGroupId: str
        :param RenewFlag: 自動續約標簽
        :type RenewFlag: str
        :param Region: 節點所在地域
        :type Region: str
        :param CpuRequested: 當前 Cpu 申請使用量
        :type CpuRequested: int
        :param MemoryRequested: 當前 Memory 申請使用量
        :type MemoryRequested: int
        :param GpuRequested: 當前 Gpu 申請使用量
        :type GpuRequested: int
        :param RsgAsGroupId: 節點所在伸縮組 ID
        :type RsgAsGroupId: str
        """
        self.Id = None
        self.Zone = None
        self.InstanceType = None
        self.InstanceChargeType = None
        self.Cpu = None
        self.Memory = None
        self.Gpu = None
        self.State = None
        self.AbnormalReason = None
        self.Created = None
        self.Updated = None
        self.DeadlineTime = None
        self.ResourceGroupId = None
        self.RenewFlag = None
        self.Region = None
        self.CpuRequested = None
        self.MemoryRequested = None
        self.GpuRequested = None
        self.RsgAsGroupId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Zone = params.get("Zone")
        self.InstanceType = params.get("InstanceType")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Gpu = params.get("Gpu")
        self.State = params.get("State")
        self.AbnormalReason = params.get("AbnormalReason")
        self.Created = params.get("Created")
        self.Updated = params.get("Updated")
        self.DeadlineTime = params.get("DeadlineTime")
        self.ResourceGroupId = params.get("ResourceGroupId")
        self.RenewFlag = params.get("RenewFlag")
        self.Region = params.get("Region")
        self.CpuRequested = params.get("CpuRequested")
        self.MemoryRequested = params.get("MemoryRequested")
        self.GpuRequested = params.get("GpuRequested")
        self.RsgAsGroupId = params.get("RsgAsGroupId")


class Job(AbstractModel):
    """任務

    """

    def __init__(self):
        """
        :param Id: 任務 Id
        :type Id: str
        :param Cluster: 集群名
注意：此欄位可能返回 null，表示取不到有效值。
        :type Cluster: str
        :param Region: Region 名
        :type Region: str
        :param Name: 任務名稱
        :type Name: str
        :param Runtime: Worker 使用的運作環境
注意：此欄位可能返回 null，表示取不到有效值。
        :type Runtime: str
        :param Description: 任務描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type Description: str
        :param ConfigId: 配置 Id
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConfigId: str
        :param PredictInput: 預測輸入
注意：此欄位可能返回 null，表示取不到有效值。
        :type PredictInput: :class:`taifucloudcloud.tiems.v20190416.models.PredictInput`
        :param Status: 任務狀态
        :type Status: :class:`taifucloudcloud.tiems.v20190416.models.JobStatus`
        :param CreateTime: 任務創建時間
        :type CreateTime: str
        :param StartTime: 任務開始時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 任務結束時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param CancelTime: 任務取消時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CancelTime: str
        :param ResourceGroupId: 任務使用資源組 Id
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResourceGroupId: str
        :param Cpu: 處理器配置, 單位爲1/1000核；範圍[100, 256000]
注意：此欄位可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param Memory: 内存配置, 單位爲1M；範圍[100, 256000]
注意：此欄位可能返回 null，表示取不到有效值。
        :type Memory: int
        :param Gpu: GPU算力配置，單位爲1/1000 卡，範圍 [0, 256000]
注意：此欄位可能返回 null，表示取不到有效值。
        :type Gpu: int
        :param GpuMemory: 顯存配置, 單位爲1M，範圍 [0, 256000]
注意：此欄位可能返回 null，表示取不到有效值。
        :type GpuMemory: int
        :param ResourceGroupName: 任務使用資源組名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResourceGroupName: str
        :param GpuType: GPU類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type GpuType: str
        :param ConfigName: 配置名
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConfigName: str
        :param ConfigVersion: 配置版本
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConfigVersion: str
        :param JobType: Job類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type JobType: str
        :param QuantizationInput: 量化輸入
注意：此欄位可能返回 null，表示取不到有效值。
        :type QuantizationInput: :class:`taifucloudcloud.tiems.v20190416.models.QuantizationInput`
        :param LogTopicId: Cls日志主題ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type LogTopicId: str
        """
        self.Id = None
        self.Cluster = None
        self.Region = None
        self.Name = None
        self.Runtime = None
        self.Description = None
        self.ConfigId = None
        self.PredictInput = None
        self.Status = None
        self.CreateTime = None
        self.StartTime = None
        self.EndTime = None
        self.CancelTime = None
        self.ResourceGroupId = None
        self.Cpu = None
        self.Memory = None
        self.Gpu = None
        self.GpuMemory = None
        self.ResourceGroupName = None
        self.GpuType = None
        self.ConfigName = None
        self.ConfigVersion = None
        self.JobType = None
        self.QuantizationInput = None
        self.LogTopicId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Cluster = params.get("Cluster")
        self.Region = params.get("Region")
        self.Name = params.get("Name")
        self.Runtime = params.get("Runtime")
        self.Description = params.get("Description")
        self.ConfigId = params.get("ConfigId")
        if params.get("PredictInput") is not None:
            self.PredictInput = PredictInput()
            self.PredictInput._deserialize(params.get("PredictInput"))
        if params.get("Status") is not None:
            self.Status = JobStatus()
            self.Status._deserialize(params.get("Status"))
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.CancelTime = params.get("CancelTime")
        self.ResourceGroupId = params.get("ResourceGroupId")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Gpu = params.get("Gpu")
        self.GpuMemory = params.get("GpuMemory")
        self.ResourceGroupName = params.get("ResourceGroupName")
        self.GpuType = params.get("GpuType")
        self.ConfigName = params.get("ConfigName")
        self.ConfigVersion = params.get("ConfigVersion")
        self.JobType = params.get("JobType")
        if params.get("QuantizationInput") is not None:
            self.QuantizationInput = QuantizationInput()
            self.QuantizationInput._deserialize(params.get("QuantizationInput"))
        self.LogTopicId = params.get("LogTopicId")


class JobStatus(AbstractModel):
    """任務狀态

    """

    def __init__(self):
        """
        :param Status: 任務狀态
        :type Status: str
        :param Message: 錯誤時爲錯誤描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param DesiredWorkers: 預期Worker數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type DesiredWorkers: int
        :param CurrentWorkers: 當前Worker數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type CurrentWorkers: int
        :param Replicas: 副本名
注意：此欄位可能返回 null，表示取不到有效值。
        :type Replicas: list of str
        :param ReplicaInfos: 副本實例
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReplicaInfos: list of ReplicaInfo
        """
        self.Status = None
        self.Message = None
        self.DesiredWorkers = None
        self.CurrentWorkers = None
        self.Replicas = None
        self.ReplicaInfos = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Message = params.get("Message")
        self.DesiredWorkers = params.get("DesiredWorkers")
        self.CurrentWorkers = params.get("CurrentWorkers")
        self.Replicas = params.get("Replicas")
        if params.get("ReplicaInfos") is not None:
            self.ReplicaInfos = []
            for item in params.get("ReplicaInfos"):
                obj = ReplicaInfo()
                obj._deserialize(item)
                self.ReplicaInfos.append(obj)


class ModelService(AbstractModel):
    """模型服務

    """

    def __init__(self):
        """
        :param Id: 服務ID
        :type Id: str
        :param Cluster: 運作集群
注意：此欄位可能返回 null，表示取不到有效值。
        :type Cluster: str
        :param Name: 服務名稱
        :type Name: str
        :param Runtime: 運作環境
        :type Runtime: str
        :param ModelUri: 模型網址
        :type ModelUri: str
        :param Cpu: 處理器配置, 單位爲1/1000核
        :type Cpu: int
        :param Memory: 内存配置, 單位爲1M
        :type Memory: int
        :param Gpu: GPU 配置, 單位爲1/1000 卡
        :type Gpu: int
        :param GpuMemory: 顯存配置, 單位爲1M
        :type GpuMemory: int
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param UpdateTime: 更新時間
        :type UpdateTime: str
        :param ScaleMode: 支援AUTO, MANUAL
        :type ScaleMode: str
        :param Scaler: 彈性伸縮配置
        :type Scaler: :class:`taifucloudcloud.tiems.v20190416.models.Scaler`
        :param Status: 服務狀态
        :type Status: :class:`taifucloudcloud.tiems.v20190416.models.ServiceStatus`
        :param AccessToken: 訪問金鑰
注意：此欄位可能返回 null，表示取不到有效值。
        :type AccessToken: str
        :param ConfigId: 服務配置Id
        :type ConfigId: str
        :param ConfigName: 服務配置名
        :type ConfigName: str
        :param ServeSeconds: 服務運作時長
        :type ServeSeconds: int
        :param ConfigVersion: 配置版本
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConfigVersion: str
        :param ResourceGroupId: 服務使用資源組 Id
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResourceGroupId: str
        :param Exposes: 暴露方式
注意：此欄位可能返回 null，表示取不到有效值。
        :type Exposes: list of ExposeInfo
        :param Region: Region 名
注意：此欄位可能返回 null，表示取不到有效值。
        :type Region: str
        :param ResourceGroupName: 服務使用資源組名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResourceGroupName: str
        :param Description: 備注
注意：此欄位可能返回 null，表示取不到有效值。
        :type Description: str
        :param GpuType: GPU類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type GpuType: str
        :param LogTopicId: Cls日志主題Id
注意：此欄位可能返回 null，表示取不到有效值。
        :type LogTopicId: str
        """
        self.Id = None
        self.Cluster = None
        self.Name = None
        self.Runtime = None
        self.ModelUri = None
        self.Cpu = None
        self.Memory = None
        self.Gpu = None
        self.GpuMemory = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ScaleMode = None
        self.Scaler = None
        self.Status = None
        self.AccessToken = None
        self.ConfigId = None
        self.ConfigName = None
        self.ServeSeconds = None
        self.ConfigVersion = None
        self.ResourceGroupId = None
        self.Exposes = None
        self.Region = None
        self.ResourceGroupName = None
        self.Description = None
        self.GpuType = None
        self.LogTopicId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Cluster = params.get("Cluster")
        self.Name = params.get("Name")
        self.Runtime = params.get("Runtime")
        self.ModelUri = params.get("ModelUri")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Gpu = params.get("Gpu")
        self.GpuMemory = params.get("GpuMemory")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ScaleMode = params.get("ScaleMode")
        if params.get("Scaler") is not None:
            self.Scaler = Scaler()
            self.Scaler._deserialize(params.get("Scaler"))
        if params.get("Status") is not None:
            self.Status = ServiceStatus()
            self.Status._deserialize(params.get("Status"))
        self.AccessToken = params.get("AccessToken")
        self.ConfigId = params.get("ConfigId")
        self.ConfigName = params.get("ConfigName")
        self.ServeSeconds = params.get("ServeSeconds")
        self.ConfigVersion = params.get("ConfigVersion")
        self.ResourceGroupId = params.get("ResourceGroupId")
        if params.get("Exposes") is not None:
            self.Exposes = []
            for item in params.get("Exposes"):
                obj = ExposeInfo()
                obj._deserialize(item)
                self.Exposes.append(obj)
        self.Region = params.get("Region")
        self.ResourceGroupName = params.get("ResourceGroupName")
        self.Description = params.get("Description")
        self.GpuType = params.get("GpuType")
        self.LogTopicId = params.get("LogTopicId")


class Option(AbstractModel):
    """配置項

    """

    def __init__(self):
        """
        :param Name: 名稱
        :type Name: str
        :param Value: 取值
        :type Value: int
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class PredictInput(AbstractModel):
    """預測輸入

    """

    def __init__(self):
        """
        :param InputPath: 輸入路徑，支援 cos 格式路徑文件夾或文件
        :type InputPath: str
        :param OutputPath: 輸出路徑，支援 cos 格式路徑
        :type OutputPath: str
        :param InputDataFormat: 輸入數據格式，目前支援：JSON
        :type InputDataFormat: str
        :param OutputDataFormat: 輸出數據格式，目前支援：JSON
        :type OutputDataFormat: str
        :param BatchSize: 預測批大小，預設爲 64
        :type BatchSize: int
        :param SignatureName: 模型簽名
注意：此欄位可能返回 null，表示取不到有效值。
        :type SignatureName: str
        """
        self.InputPath = None
        self.OutputPath = None
        self.InputDataFormat = None
        self.OutputDataFormat = None
        self.BatchSize = None
        self.SignatureName = None


    def _deserialize(self, params):
        self.InputPath = params.get("InputPath")
        self.OutputPath = params.get("OutputPath")
        self.InputDataFormat = params.get("InputDataFormat")
        self.OutputDataFormat = params.get("OutputDataFormat")
        self.BatchSize = params.get("BatchSize")
        self.SignatureName = params.get("SignatureName")


class QuantizationInput(AbstractModel):
    """量化輸入

    """

    def __init__(self):
        """
        :param InputPath: 量化輸入路徑
        :type InputPath: str
        :param OutputPath: 量化輸出路徑
        :type OutputPath: str
        :param BatchSize: 量化批大小
        :type BatchSize: int
        :param Precision: 量化精度，支援：FP32，FP16，INT8
        :type Precision: str
        :param ConvertType: 轉換類型
        :type ConvertType: str
        """
        self.InputPath = None
        self.OutputPath = None
        self.BatchSize = None
        self.Precision = None
        self.ConvertType = None


    def _deserialize(self, params):
        self.InputPath = params.get("InputPath")
        self.OutputPath = params.get("OutputPath")
        self.BatchSize = params.get("BatchSize")
        self.Precision = params.get("Precision")
        self.ConvertType = params.get("ConvertType")


class ReplicaInfo(AbstractModel):
    """實例訊息

    """

    def __init__(self):
        """
        :param Name: 實例名稱
        :type Name: str
        :param EniIp: 彈性網卡模式時，彈性網卡Ip
注意：此欄位可能返回 null，表示取不到有效值。
        :type EniIp: str
        :param Status: Normal: 正常運作中; Abnormal: 異常；Waiting：等待中
        :type Status: str
        :param Message: 當 status爲 Abnormal 的時候，一些額外的訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param StartTime: 啓動時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param CreateTime: 創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param Restarted: 重啓次數
        :type Restarted: int
        """
        self.Name = None
        self.EniIp = None
        self.Status = None
        self.Message = None
        self.StartTime = None
        self.CreateTime = None
        self.Restarted = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.EniIp = params.get("EniIp")
        self.Status = params.get("Status")
        self.Message = params.get("Message")
        self.StartTime = params.get("StartTime")
        self.CreateTime = params.get("CreateTime")
        self.Restarted = params.get("Restarted")


class ResourceGroup(AbstractModel):
    """資源組

    """

    def __init__(self):
        """
        :param Id: 資源組 Id
        :type Id: str
        :param Region: 地域
        :type Region: str
        :param Cluster: 集群
注意：此欄位可能返回 null，表示取不到有效值。
        :type Cluster: str
        :param Name: 資源組名稱
        :type Name: str
        :param Description: 資源組描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type Description: str
        :param Created: 創建時間
        :type Created: str
        :param Updated: 更新時間
        :type Updated: str
        :param InstanceCount: 資源組主機數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceCount: int
        :param ServiceCount: 使用資源組的服務數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type ServiceCount: int
        :param JobCount: 使用資源組的任務數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type JobCount: int
        :param Public: 資源組是否爲公共資源組
注意：此欄位可能返回 null，表示取不到有效值。
        :type Public: bool
        :param InstanceType: 機器類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param Status: 資源組狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: str
        :param Gpu: 顯示卡總張數
注意：此欄位可能返回 null，表示取不到有效值。
        :type Gpu: int
        :param Cpu: 處理器總核數
注意：此欄位可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param Memory: 内存總量，單位爲G
注意：此欄位可能返回 null，表示取不到有效值。
        :type Memory: int
        :param Zone: 可用區
注意：此欄位可能返回 null，表示取不到有效值。
        :type Zone: str
        :param GpuType: Gpu類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type GpuType: list of str
        :param HasPrepaid: 該資源組下是否有預付費資源
注意：此欄位可能返回 null，表示取不到有效值。
        :type HasPrepaid: bool
        :param PayMode: 資源組是否允許預付費或後付費模式
注意：此欄位可能返回 null，表示取不到有效值。
        :type PayMode: str
        """
        self.Id = None
        self.Region = None
        self.Cluster = None
        self.Name = None
        self.Description = None
        self.Created = None
        self.Updated = None
        self.InstanceCount = None
        self.ServiceCount = None
        self.JobCount = None
        self.Public = None
        self.InstanceType = None
        self.Status = None
        self.Gpu = None
        self.Cpu = None
        self.Memory = None
        self.Zone = None
        self.GpuType = None
        self.HasPrepaid = None
        self.PayMode = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Region = params.get("Region")
        self.Cluster = params.get("Cluster")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.Created = params.get("Created")
        self.Updated = params.get("Updated")
        self.InstanceCount = params.get("InstanceCount")
        self.ServiceCount = params.get("ServiceCount")
        self.JobCount = params.get("JobCount")
        self.Public = params.get("Public")
        self.InstanceType = params.get("InstanceType")
        self.Status = params.get("Status")
        self.Gpu = params.get("Gpu")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Zone = params.get("Zone")
        self.GpuType = params.get("GpuType")
        self.HasPrepaid = params.get("HasPrepaid")
        self.PayMode = params.get("PayMode")


class RsgAsActivityRelatedInstance(AbstractModel):
    """伸縮組活動關聯的節點

    """

    def __init__(self):
        """
        :param InstanceId: 節點 ID
        :type InstanceId: str
        :param InstanceStatus: 節點狀态
        :type InstanceStatus: str
        """
        self.InstanceId = None
        self.InstanceStatus = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceStatus = params.get("InstanceStatus")


class RsgAsGroup(AbstractModel):
    """資源組的伸縮組

    """

    def __init__(self):
        """
        :param Id: 伸縮組 ID
        :type Id: str
        :param Region: 伸縮組所在地域
        :type Region: str
        :param Zone: 伸縮組所在可用區
        :type Zone: str
        :param Cluster: 伸縮組所在集群
        :type Cluster: str
        :param RsgId: 伸縮組所在資源組 ID
        :type RsgId: str
        :param Name: 伸縮組名稱
        :type Name: str
        :param MaxSize: 伸縮組允許的最大節點個數
        :type MaxSize: int
        :param MinSize: 伸縮組允許的最小節點個數
        :type MinSize: int
        :param CreateTime: 伸縮組創建時間
        :type CreateTime: str
        :param UpdateTime: 伸縮組更新時間
        :type UpdateTime: str
        :param Status: 伸縮組狀态
        :type Status: str
        :param InstanceType: 伸縮組節點類型
        :type InstanceType: str
        :param InstanceCount: 伸縮組内節點個數
        :type InstanceCount: int
        :param DesiredSize: 伸縮組起始節點數
        :type DesiredSize: int
        """
        self.Id = None
        self.Region = None
        self.Zone = None
        self.Cluster = None
        self.RsgId = None
        self.Name = None
        self.MaxSize = None
        self.MinSize = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Status = None
        self.InstanceType = None
        self.InstanceCount = None
        self.DesiredSize = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.Cluster = params.get("Cluster")
        self.RsgId = params.get("RsgId")
        self.Name = params.get("Name")
        self.MaxSize = params.get("MaxSize")
        self.MinSize = params.get("MinSize")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Status = params.get("Status")
        self.InstanceType = params.get("InstanceType")
        self.InstanceCount = params.get("InstanceCount")
        self.DesiredSize = params.get("DesiredSize")


class RsgAsGroupActivity(AbstractModel):
    """伸縮組活動訊息

    """

    def __init__(self):
        """
        :param Id: 伸縮組活動 ID
        :type Id: str
        :param RsgAsGroupId: 關聯的伸縮組 ID
        :type RsgAsGroupId: str
        :param ActivityType: 活動類型
        :type ActivityType: str
        :param StatusCode: 狀态的編碼
        :type StatusCode: str
        :param StatusMessage: 狀态的訊息
        :type StatusMessage: str
        :param Cause: 活動原因
        :type Cause: str
        :param Description: 活動描述
        :type Description: str
        :param StartTime: 活動開始時間
        :type StartTime: str
        :param EndTime: 活動結束時間
        :type EndTime: str
        :param CreateTime: 活動創建時間
        :type CreateTime: str
        :param RsgAsActivityRelatedInstance: 活動相關聯的節點
        :type RsgAsActivityRelatedInstance: list of RsgAsActivityRelatedInstance
        :param StatusMessageSimplified: 簡略的狀态訊息
        :type StatusMessageSimplified: str
        """
        self.Id = None
        self.RsgAsGroupId = None
        self.ActivityType = None
        self.StatusCode = None
        self.StatusMessage = None
        self.Cause = None
        self.Description = None
        self.StartTime = None
        self.EndTime = None
        self.CreateTime = None
        self.RsgAsActivityRelatedInstance = None
        self.StatusMessageSimplified = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RsgAsGroupId = params.get("RsgAsGroupId")
        self.ActivityType = params.get("ActivityType")
        self.StatusCode = params.get("StatusCode")
        self.StatusMessage = params.get("StatusMessage")
        self.Cause = params.get("Cause")
        self.Description = params.get("Description")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.CreateTime = params.get("CreateTime")
        if params.get("RsgAsActivityRelatedInstance") is not None:
            self.RsgAsActivityRelatedInstance = []
            for item in params.get("RsgAsActivityRelatedInstance"):
                obj = RsgAsActivityRelatedInstance()
                obj._deserialize(item)
                self.RsgAsActivityRelatedInstance.append(obj)
        self.StatusMessageSimplified = params.get("StatusMessageSimplified")


class Runtime(AbstractModel):
    """運作環境

    """

    def __init__(self):
        """
        :param Name: 運作環境名稱
        :type Name: str
        :param Framework: 運作環境框架
        :type Framework: str
        :param Description: 運作環境描述
        :type Description: str
        :param Public: 是否爲公開運作環境
注意：此欄位可能返回 null，表示取不到有效值。
        :type Public: bool
        :param HealthCheckOn: 是否打開健康檢查
注意：此欄位可能返回 null，表示取不到有效值。
        :type HealthCheckOn: bool
        :param Image: 映像網址
注意：此欄位可能返回 null，表示取不到有效值。
        :type Image: str
        :param CreateTime: 創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self.Name = None
        self.Framework = None
        self.Description = None
        self.Public = None
        self.HealthCheckOn = None
        self.Image = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Framework = params.get("Framework")
        self.Description = params.get("Description")
        self.Public = params.get("Public")
        self.HealthCheckOn = params.get("HealthCheckOn")
        self.Image = params.get("Image")
        self.CreateTime = params.get("CreateTime")


class Scaler(AbstractModel):
    """擴縮容配置

    """

    def __init__(self):
        """
        :param MaxReplicas: 最大副本數，ScaleMode 爲 MANUAL 時辭會此值會被置爲 StartReplicas 取值
        :type MaxReplicas: int
        :param MinReplicas: 最小副本數，ScaleMode 爲 MANUAL 時辭會此值會被置爲 StartReplicas 取值
        :type MinReplicas: int
        :param StartReplicas: 起始副本數
        :type StartReplicas: int
        :param HpaMetrics: 擴縮容指標，選擇自動擴縮容時至少需要選擇一個指標，支援CPU-UTIL、MEMORY-UTIL
        :type HpaMetrics: list of Option
        """
        self.MaxReplicas = None
        self.MinReplicas = None
        self.StartReplicas = None
        self.HpaMetrics = None


    def _deserialize(self, params):
        self.MaxReplicas = params.get("MaxReplicas")
        self.MinReplicas = params.get("MinReplicas")
        self.StartReplicas = params.get("StartReplicas")
        if params.get("HpaMetrics") is not None:
            self.HpaMetrics = []
            for item in params.get("HpaMetrics"):
                obj = Option()
                obj._deserialize(item)
                self.HpaMetrics.append(obj)


class ServiceStatus(AbstractModel):
    """服務狀态

    """

    def __init__(self):
        """
        :param DesiredReplicas: 預期副本數
        :type DesiredReplicas: int
        :param CurrentReplicas: 當前副本數
        :type CurrentReplicas: int
        :param Status: Normal：正常運作中；Abnormal：服務異常，例如容器啓動失敗等；Waiting：服務等待中，例如容器下載映像過程等；Stopped：已停止 Stopping 停止中；Resuming：重啓中；Updating：服務更新中
        :type Status: str
        :param Conditions: 服務處於當前狀态的原因集合
注意：此欄位可能返回 null，表示取不到有效值。
        :type Conditions: list of Conditions
        :param Replicas: 副本名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type Replicas: list of str
        :param Message: 運作狀态對額外訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param ReplicaInfos: 副本訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReplicaInfos: list of ReplicaInfo
        """
        self.DesiredReplicas = None
        self.CurrentReplicas = None
        self.Status = None
        self.Conditions = None
        self.Replicas = None
        self.Message = None
        self.ReplicaInfos = None


    def _deserialize(self, params):
        self.DesiredReplicas = params.get("DesiredReplicas")
        self.CurrentReplicas = params.get("CurrentReplicas")
        self.Status = params.get("Status")
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = Conditions()
                obj._deserialize(item)
                self.Conditions.append(obj)
        self.Replicas = params.get("Replicas")
        self.Message = params.get("Message")
        if params.get("ReplicaInfos") is not None:
            self.ReplicaInfos = []
            for item in params.get("ReplicaInfos"):
                obj = ReplicaInfo()
                obj._deserialize(item)
                self.ReplicaInfos.append(obj)


class UpdateJobRequest(AbstractModel):
    """UpdateJob請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 任務 Id
        :type JobId: str
        :param JobAction: 任務更新動作，支援：Cancel
        :type JobAction: str
        :param Description: 備注
        :type Description: str
        """
        self.JobId = None
        self.JobAction = None
        self.Description = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobAction = params.get("JobAction")
        self.Description = params.get("Description")


class UpdateJobResponse(AbstractModel):
    """UpdateJob返回參數結構體

    """

    def __init__(self):
        """
        :param Job: 任務
注意：此欄位可能返回 null，表示取不到有效值。
        :type Job: :class:`taifucloudcloud.tiems.v20190416.models.Job`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Job = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Job") is not None:
            self.Job = Job()
            self.Job._deserialize(params.get("Job"))
        self.RequestId = params.get("RequestId")


class UpdateRsgAsGroupRequest(AbstractModel):
    """UpdateRsgAsGroup請求參數結構體

    """

    def __init__(self):
        """
        :param Id: 伸縮組 ID
        :type Id: str
        :param Name: 重命名名稱
        :type Name: str
        :param MaxSize: 伸縮組最大節點數
        :type MaxSize: int
        :param MinSize: 伸縮組最小節點數
        :type MinSize: int
        :param DesiredSize: 伸縮組期望的節點數
        :type DesiredSize: int
        """
        self.Id = None
        self.Name = None
        self.MaxSize = None
        self.MinSize = None
        self.DesiredSize = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.MaxSize = params.get("MaxSize")
        self.MinSize = params.get("MinSize")
        self.DesiredSize = params.get("DesiredSize")


class UpdateRsgAsGroupResponse(AbstractModel):
    """UpdateRsgAsGroup返回參數結構體

    """

    def __init__(self):
        """
        :param RsgAsGroup: 資源組的伸縮組
        :type RsgAsGroup: :class:`taifucloudcloud.tiems.v20190416.models.RsgAsGroup`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RsgAsGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RsgAsGroup") is not None:
            self.RsgAsGroup = RsgAsGroup()
            self.RsgAsGroup._deserialize(params.get("RsgAsGroup"))
        self.RequestId = params.get("RequestId")


class UpdateServiceRequest(AbstractModel):
    """UpdateService請求參數結構體

    """

    def __init__(self):
        """
        :param ServiceId: 服務Id
        :type ServiceId: str
        :param Scaler: 擴縮容配置
        :type Scaler: :class:`taifucloudcloud.tiems.v20190416.models.Scaler`
        :param ServiceConfigId: 服務配置Id
        :type ServiceConfigId: str
        :param ScaleMode: 支援AUTO, MANUAL，分别表示自動擴縮容，手動擴縮容
        :type ScaleMode: str
        :param ServiceAction: 支援STOP(停止) RESUME(重啓)
        :type ServiceAction: str
        :param Description: 備注
        :type Description: str
        :param GpuType: GPU卡類型
        :type GpuType: str
        :param Cpu: 處理器配置，單位爲 1/1000 核
        :type Cpu: int
        :param Memory: 内存配置，單位爲1M
        :type Memory: int
        :param Gpu: 顯示卡配置，單位爲 1/1000 卡
        :type Gpu: int
        :param LogTopicId: Cls日志主題ID
        :type LogTopicId: str
        """
        self.ServiceId = None
        self.Scaler = None
        self.ServiceConfigId = None
        self.ScaleMode = None
        self.ServiceAction = None
        self.Description = None
        self.GpuType = None
        self.Cpu = None
        self.Memory = None
        self.Gpu = None
        self.LogTopicId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        if params.get("Scaler") is not None:
            self.Scaler = Scaler()
            self.Scaler._deserialize(params.get("Scaler"))
        self.ServiceConfigId = params.get("ServiceConfigId")
        self.ScaleMode = params.get("ScaleMode")
        self.ServiceAction = params.get("ServiceAction")
        self.Description = params.get("Description")
        self.GpuType = params.get("GpuType")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Gpu = params.get("Gpu")
        self.LogTopicId = params.get("LogTopicId")


class UpdateServiceResponse(AbstractModel):
    """UpdateService返回參數結構體

    """

    def __init__(self):
        """
        :param Service: 服務
        :type Service: :class:`taifucloudcloud.tiems.v20190416.models.ModelService`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Service = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Service") is not None:
            self.Service = ModelService()
            self.Service._deserialize(params.get("Service"))
        self.RequestId = params.get("RequestId")