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


class CreateJobRequest(AbstractModel):
    """CreateJob請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 任務名稱
        :type Name: str
        :param Cluster: 運作任務的集群，詳見 [使用集群](https://cloud.tencent.com/document/product/851/17317)
        :type Cluster: str
        :param RuntimeVersion: 運作任務的環境，詳見 [運作環境](https://cloud.tencent.com/document/product/851/17320)
        :type RuntimeVersion: str
        :param PackageDir: 掛載的路徑，支援 NFS，[CFS](https://cloud.tencent.com/product/cfs) 和 [COS](https://cloud.tencent.com/product/cos)，其中 COS 只在 [TI-A 定制環境](https://cloud.tencent.com/document/product/851/17320#ti-a-.E5.AE.9A.E5.88.B6.E7.8E.AF.E5.A2.83) 中支援
        :type PackageDir: list of str
        :param Command: 任務啓動命令
        :type Command: list of str
        :param Args: 任務啓動參數
        :type Args: list of str
        :param ScaleTier: 運作任務的配置訊息，詳見 [訓練規模](https://cloud.tencent.com/document/product/851/17319)
        :type ScaleTier: str
        :param MasterType: Master 機器類型，ScaleTier 取值爲 `CUSTOM` 時必填，詳見 [訓練規模](https://cloud.tencent.com/document/product/851/17319)
        :type MasterType: str
        :param WorkerType: Worker 機器類型，ScaleTier 取值爲 `CUSTOM` 時必填，詳見 [訓練規模](https://cloud.tencent.com/document/product/851/17319)
        :type WorkerType: str
        :param ParameterServerType: Parameter server 機器類型，ScaleTier 取值爲 `CUSTOM` 時必填,詳見 [訓練規模](https://cloud.tencent.com/document/product/851/17319)
        :type ParameterServerType: str
        :param WorkerCount: Worker 機器數量，ScaleTier 取值爲 `CUSTOM` 時必填,詳見 [訓練規模](https://cloud.tencent.com/document/product/851/17319)
        :type WorkerCount: int
        :param ParameterServerCount: Parameter server 機器數量，ScaleTier 取值爲 `CUSTOM` 時必填,詳見 [訓練規模](https://cloud.tencent.com/document/product/851/17319)
        :type ParameterServerCount: int
        :param Debug: 啓動 debug 模式，預設爲 false
        :type Debug: bool
        :param RuntimeConf: 運作任務的其他配置訊息
        :type RuntimeConf: list of str
        """
        self.Name = None
        self.Cluster = None
        self.RuntimeVersion = None
        self.PackageDir = None
        self.Command = None
        self.Args = None
        self.ScaleTier = None
        self.MasterType = None
        self.WorkerType = None
        self.ParameterServerType = None
        self.WorkerCount = None
        self.ParameterServerCount = None
        self.Debug = None
        self.RuntimeConf = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Cluster = params.get("Cluster")
        self.RuntimeVersion = params.get("RuntimeVersion")
        self.PackageDir = params.get("PackageDir")
        self.Command = params.get("Command")
        self.Args = params.get("Args")
        self.ScaleTier = params.get("ScaleTier")
        self.MasterType = params.get("MasterType")
        self.WorkerType = params.get("WorkerType")
        self.ParameterServerType = params.get("ParameterServerType")
        self.WorkerCount = params.get("WorkerCount")
        self.ParameterServerCount = params.get("ParameterServerCount")
        self.Debug = params.get("Debug")
        self.RuntimeConf = params.get("RuntimeConf")


class CreateJobResponse(AbstractModel):
    """CreateJob返回參數結構體

    """

    def __init__(self):
        """
        :param Job: 訓練任務訊息
        :type Job: :class:`tencentcloud.tia.v20180226.models.Job`
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


class CreateModelRequest(AbstractModel):
    """CreateModel請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 模型名稱
        :type Name: str
        :param Model: 要佈署的模型文件路徑名
        :type Model: str
        :param Description: 關于模型的描述
        :type Description: str
        :param Cluster: 佈署目标集群的名稱，`集群模式` 必填
        :type Cluster: str
        :param RuntimeVersion: 運作環境映像的标簽，詳見 [Serving 環境](https://cloud.tencent.com/document/product/851/17320#serving-.E7.8E.AF.E5.A2.83)
        :type RuntimeVersion: str
        :param Replicas: 要佈署的模型副本數目，`集群模式` 選填
        :type Replicas: int
        :param Expose: 暴露外網或内網，預設暴露外網，`集群模式` 選填
        :type Expose: str
        :param ServType: 佈署模式，取值 `serverless` 即爲 `無服務器模式`，否則爲 `集群模式` 下服務的運作規模，形如 `2U4G1P`，詳見 [自定義的訓練規模](https://cloud.tencent.com/document/product/851/17319#.E8.87.AA.E5.AE.9A.E4.B9.89.E7.9A.84.E8.AE.AD.E7.BB.83.E8.A7.84.E6.A8.A1)
        :type ServType: str
        :param RuntimeConf: `無服務器模式` 可選的其他配置訊息，詳見 [利用無服務器函數佈署](https://cloud.tencent.com/document/product/851/17049#.E5.88.A9.E7.94.A8.E6.97.A0.E6.9C.8D.E5.8A.A1.E5.99.A8.E5.87.BD.E6.95.B0.E9.83.A8.E7.BD.B2)
        :type RuntimeConf: list of str
        """
        self.Name = None
        self.Model = None
        self.Description = None
        self.Cluster = None
        self.RuntimeVersion = None
        self.Replicas = None
        self.Expose = None
        self.ServType = None
        self.RuntimeConf = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Model = params.get("Model")
        self.Description = params.get("Description")
        self.Cluster = params.get("Cluster")
        self.RuntimeVersion = params.get("RuntimeVersion")
        self.Replicas = params.get("Replicas")
        self.Expose = params.get("Expose")
        self.ServType = params.get("ServType")
        self.RuntimeConf = params.get("RuntimeConf")


class CreateModelResponse(AbstractModel):
    """CreateModel返回參數結構體

    """

    def __init__(self):
        """
        :param Model: 模型的詳細訊息
        :type Model: :class:`tencentcloud.tia.v20180226.models.Model`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Model = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self.Model = Model()
            self.Model._deserialize(params.get("Model"))
        self.RequestId = params.get("RequestId")


class DeleteJobRequest(AbstractModel):
    """DeleteJob請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 任務名稱
        :type Name: str
        :param Cluster: 運作任務的集群
        :type Cluster: str
        """
        self.Name = None
        self.Cluster = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Cluster = params.get("Cluster")


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


class DeleteModelRequest(AbstractModel):
    """DeleteModel請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 要删除的模型名稱
        :type Name: str
        :param Cluster: 要删除的模型所在的集群名稱，`集群模式` 必填
        :type Cluster: str
        :param ServType: 模型類型，取值 `serverless` 即爲 `無服務器模式`，否則爲 `集群模式`
        :type ServType: str
        """
        self.Name = None
        self.Cluster = None
        self.ServType = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Cluster = params.get("Cluster")
        self.ServType = params.get("ServType")


class DeleteModelResponse(AbstractModel):
    """DeleteModel返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeJobRequest(AbstractModel):
    """DescribeJob請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 任務名稱
        :type Name: str
        :param Cluster: 運作任務的集群
        :type Cluster: str
        """
        self.Name = None
        self.Cluster = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Cluster = params.get("Cluster")


class DescribeJobResponse(AbstractModel):
    """DescribeJob返回參數結構體

    """

    def __init__(self):
        """
        :param Job: 訓練任務訊息
        :type Job: :class:`tencentcloud.tia.v20180226.models.Job`
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


class DescribeModelRequest(AbstractModel):
    """DescribeModel請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 模型名稱
        :type Name: str
        :param Cluster: 模型所在集群名稱，`集群模式` 必填
        :type Cluster: str
        :param ServType: 模型類型，取值 `serverless` 即爲 `無服務器模式`，否則爲 `集群模式`
        :type ServType: str
        """
        self.Name = None
        self.Cluster = None
        self.ServType = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Cluster = params.get("Cluster")
        self.ServType = params.get("ServType")


class DescribeModelResponse(AbstractModel):
    """DescribeModel返回參數結構體

    """

    def __init__(self):
        """
        :param Model: 模型訊息
        :type Model: :class:`tencentcloud.tia.v20180226.models.Model`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Model = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self.Model = Model()
            self.Model._deserialize(params.get("Model"))
        self.RequestId = params.get("RequestId")


class InstallAgentRequest(AbstractModel):
    """InstallAgent請求參數結構體

    """

    def __init__(self):
        """
        :param Cluster: 集群名稱
        :type Cluster: str
        :param TiaVersion: Agent版本, 用于私有集群的agent安裝，預設爲“private-training”
        :type TiaVersion: str
        :param Update: 是否允許更新Agent
        :type Update: bool
        """
        self.Cluster = None
        self.TiaVersion = None
        self.Update = None


    def _deserialize(self, params):
        self.Cluster = params.get("Cluster")
        self.TiaVersion = params.get("TiaVersion")
        self.Update = params.get("Update")


class InstallAgentResponse(AbstractModel):
    """InstallAgent返回參數結構體

    """

    def __init__(self):
        """
        :param TiaVersion: Agent版本, 用于私有集群的agent安裝
        :type TiaVersion: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TiaVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TiaVersion = params.get("TiaVersion")
        self.RequestId = params.get("RequestId")


class Job(AbstractModel):
    """訓練任務訊息

    """

    def __init__(self):
        """
        :param Name: 任務名稱
        :type Name: str
        :param CreateTime: 任務創建時間，格式爲：2006-01-02 15:04:05.999999999 -0700 MST
        :type CreateTime: str
        :param StartTime: 任務開始時間，格式爲：2006-01-02 15:04:05.999999999 -0700 MST
        :type StartTime: str
        :param EndTime: 任務結束時間，格式爲：2006-01-02 15:04:05.999999999 -0700 MST
        :type EndTime: str
        :param State: 任務狀态，可能的狀态爲Created（已創建），Running（運作中），Succeeded（運作完成：成功），Failed（運作完成：失敗）
        :type State: str
        :param Message: 任務狀态訊息
        :type Message: str
        :param ScaleTier: 運作任務的配置訊息
        :type ScaleTier: str
        :param MasterType: （ScaleTier爲Custom時）master機器類型
        :type MasterType: str
        :param WorkerType: （ScaleTier爲Custom時）worker機器類型
        :type WorkerType: str
        :param ParameterServerType: （ScaleTier爲Custom時）parameter server機器類型
        :type ParameterServerType: str
        :param WorkerCount: （ScaleTier爲Custom時）worker機器數量
        :type WorkerCount: int
        :param ParameterServerCount: （ScaleTier爲Custom時）parameter server機器數量
        :type ParameterServerCount: int
        :param PackageDir: 掛載的路徑
        :type PackageDir: list of str
        :param Command: 任務啓動命令
        :type Command: list of str
        :param Args: 任務啓動參數
        :type Args: list of str
        :param Cluster: 運作任務的集群
        :type Cluster: str
        :param RuntimeVersion: 運作任務的環境
        :type RuntimeVersion: str
        :param DelTime: 任務删除時間，格式爲：2006-01-02 15:04:05.999999999 -0700 MST
        :type DelTime: str
        :param AppId: 創建任務的AppId
        :type AppId: int
        :param Uin: 創建任務的Uin
        :type Uin: str
        :param Debug: 創建任務的Debug模式
        :type Debug: bool
        :param RuntimeConf: Runtime的額外配置訊息
        :type RuntimeConf: list of str
        :param Id: 任務Id
        :type Id: str
        """
        self.Name = None
        self.CreateTime = None
        self.StartTime = None
        self.EndTime = None
        self.State = None
        self.Message = None
        self.ScaleTier = None
        self.MasterType = None
        self.WorkerType = None
        self.ParameterServerType = None
        self.WorkerCount = None
        self.ParameterServerCount = None
        self.PackageDir = None
        self.Command = None
        self.Args = None
        self.Cluster = None
        self.RuntimeVersion = None
        self.DelTime = None
        self.AppId = None
        self.Uin = None
        self.Debug = None
        self.RuntimeConf = None
        self.Id = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.CreateTime = params.get("CreateTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.State = params.get("State")
        self.Message = params.get("Message")
        self.ScaleTier = params.get("ScaleTier")
        self.MasterType = params.get("MasterType")
        self.WorkerType = params.get("WorkerType")
        self.ParameterServerType = params.get("ParameterServerType")
        self.WorkerCount = params.get("WorkerCount")
        self.ParameterServerCount = params.get("ParameterServerCount")
        self.PackageDir = params.get("PackageDir")
        self.Command = params.get("Command")
        self.Args = params.get("Args")
        self.Cluster = params.get("Cluster")
        self.RuntimeVersion = params.get("RuntimeVersion")
        self.DelTime = params.get("DelTime")
        self.AppId = params.get("AppId")
        self.Uin = params.get("Uin")
        self.Debug = params.get("Debug")
        self.RuntimeConf = params.get("RuntimeConf")
        self.Id = params.get("Id")


class ListJobsRequest(AbstractModel):
    """ListJobs請求參數結構體

    """

    def __init__(self):
        """
        :param Cluster: 運作任務的集群
        :type Cluster: str
        :param Limit: 分頁參數，返回數量
        :type Limit: int
        :param Offset: 分頁參數，起始位置
        :type Offset: int
        """
        self.Cluster = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Cluster = params.get("Cluster")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class ListJobsResponse(AbstractModel):
    """ListJobs返回參數結構體

    """

    def __init__(self):
        """
        :param Jobs: 訓練任務清單
        :type Jobs: list of Job
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Jobs = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Jobs") is not None:
            self.Jobs = []
            for item in params.get("Jobs"):
                obj = Job()
                obj._deserialize(item)
                self.Jobs.append(obj)
        self.RequestId = params.get("RequestId")


class ListModelsRequest(AbstractModel):
    """ListModels請求參數結構體

    """

    def __init__(self):
        """
        :param Cluster: 部署模型的集群， `集群模式` 必填
        :type Cluster: str
        :param Limit: 分頁參數，返回數量上限
        :type Limit: int
        :param Offset: 分頁參數，分頁起始位置
        :type Offset: int
        :param ServType: 佈署類型，取值 `serverless` 即爲 `無服務器模式`，否則爲 `集群模式`。
        :type ServType: str
        """
        self.Cluster = None
        self.Limit = None
        self.Offset = None
        self.ServType = None


    def _deserialize(self, params):
        self.Cluster = params.get("Cluster")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.ServType = params.get("ServType")


class ListModelsResponse(AbstractModel):
    """ListModels返回參數結構體

    """

    def __init__(self):
        """
        :param Models: Model 數組，用以顯示所有模型的訊息
        :type Models: list of Model
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Models = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Models") is not None:
            self.Models = []
            for item in params.get("Models"):
                obj = Model()
                obj._deserialize(item)
                self.Models.append(obj)
        self.RequestId = params.get("RequestId")


class Log(AbstractModel):
    """日志

    """

    def __init__(self):
        """
        :param ContainerName: 容器名
        :type ContainerName: str
        :param Log: 日志内容
        :type Log: str
        :param Namespace: 空間名
        :type Namespace: str
        :param PodId: Pod Id
        :type PodId: str
        :param PodName: Pod名
        :type PodName: str
        :param Time: 日志日期，格式爲“2018-07-02T09:10:04.916553368Z”
        :type Time: str
        """
        self.ContainerName = None
        self.Log = None
        self.Namespace = None
        self.PodId = None
        self.PodName = None
        self.Time = None


    def _deserialize(self, params):
        self.ContainerName = params.get("ContainerName")
        self.Log = params.get("Log")
        self.Namespace = params.get("Namespace")
        self.PodId = params.get("PodId")
        self.PodName = params.get("PodName")
        self.Time = params.get("Time")


class Model(AbstractModel):
    """用于描述模型的詳細情況
            "Model": {
                "Name": "test-model",
                "Description": "test-model",
                "Cluster": "ap-beijing",
                "Model": "cos://test-1255502019.cos.ap-shanghai.myqcloud.com/example:/data/mnist",
                "RuntimeVersion": "tiaserv-1.6.0-cpu",
                "CreateTime": "2018-04-26 15:59:25 +0800 CST",
                "State": "Running",
                "ServingUrl": "140.143.51.230",
                "Message": "Deployment does not have minimum availability.",
                "AppId": 1255502019,
                "ServType": "1U2G0P"
            },

    """

    def __init__(self):
        """
        :param Name: 模型名稱
        :type Name: str
        :param Description: 模型描述
        :type Description: str
        :param Cluster: 集群名稱
        :type Cluster: str
        :param Model: 模型網址
        :type Model: str
        :param RuntimeVersion: 運作環境編号
        :type RuntimeVersion: str
        :param CreateTime: 模型創建時間
        :type CreateTime: str
        :param State: 模型運作狀态
        :type State: str
        :param ServingUrl: 提供服務的url
        :type ServingUrl: str
        :param Message: 相關訊息
        :type Message: str
        :param AppId: 編号
        :type AppId: int
        :param ServType: 機型
        :type ServType: str
        :param Expose: 模型暴露方式
        :type Expose: str
        :param Replicas: 佈署副本數量
        :type Replicas: int
        :param Id: 模型Id
        :type Id: str
        :param Uin: 創建任務的Uin
        :type Uin: str
        :param DelTime: 模型删除時間，格式爲：2006-01-02 15:04:05.999999999 -0700 MST
        :type DelTime: str
        """
        self.Name = None
        self.Description = None
        self.Cluster = None
        self.Model = None
        self.RuntimeVersion = None
        self.CreateTime = None
        self.State = None
        self.ServingUrl = None
        self.Message = None
        self.AppId = None
        self.ServType = None
        self.Expose = None
        self.Replicas = None
        self.Id = None
        self.Uin = None
        self.DelTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.Cluster = params.get("Cluster")
        self.Model = params.get("Model")
        self.RuntimeVersion = params.get("RuntimeVersion")
        self.CreateTime = params.get("CreateTime")
        self.State = params.get("State")
        self.ServingUrl = params.get("ServingUrl")
        self.Message = params.get("Message")
        self.AppId = params.get("AppId")
        self.ServType = params.get("ServType")
        self.Expose = params.get("Expose")
        self.Replicas = params.get("Replicas")
        self.Id = params.get("Id")
        self.Uin = params.get("Uin")
        self.DelTime = params.get("DelTime")


class QueryLogsRequest(AbstractModel):
    """QueryLogs請求參數結構體

    """

    def __init__(self):
        """
        :param JobName: 任務的名稱
        :type JobName: str
        :param Cluster: 任務所在集群的名稱
        :type Cluster: str
        :param StartTime: 查詢日志的開始時間，格式：2019-01-01 00:00:00
        :type StartTime: str
        :param EndTime: 查詢日志的結束時間，格式：2019-01-01 00:00:00
        :type EndTime: str
        :param Limit: 單次要返回的日志條數上限
        :type Limit: int
        :param Context: 加載更多日志時使用，透傳上次返回的 Context 值，獲取後續的日志内容；使用 Context 翻頁最多能獲取 10000 條日志
        :type Context: str
        """
        self.JobName = None
        self.Cluster = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Context = None


    def _deserialize(self, params):
        self.JobName = params.get("JobName")
        self.Cluster = params.get("Cluster")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Context = params.get("Context")


class QueryLogsResponse(AbstractModel):
    """QueryLogs返回參數結構體

    """

    def __init__(self):
        """
        :param Context: 日志查詢上下文，用于加載更多日志
        :type Context: str
        :param Logs: 日志内容清單
        :type Logs: list of Log
        :param Listover: 是否已經返回所有符合條件的日志
        :type Listover: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Context = None
        self.Logs = None
        self.Listover = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Context = params.get("Context")
        if params.get("Logs") is not None:
            self.Logs = []
            for item in params.get("Logs"):
                obj = Log()
                obj._deserialize(item)
                self.Logs.append(obj)
        self.Listover = params.get("Listover")
        self.RequestId = params.get("RequestId")