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


class DeregisterMigrationTaskRequest(AbstractModel):
    """DeregisterMigrationTask請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class DeregisterMigrationTaskResponse(AbstractModel):
    """DeregisterMigrationTask返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeMigrationTaskRequest(AbstractModel):
    """DescribeMigrationTask請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class DescribeMigrationTaskResponse(AbstractModel):
    """DescribeMigrationTask返回參數結構體

    """

    def __init__(self):
        """
        :param TaskStatus: 遷移詳情清單
        :type TaskStatus: list of TaskStatus
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.TaskStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskStatus") is not None:
            self.TaskStatus = []
            for item in params.get("TaskStatus"):
                obj = TaskStatus()
                obj._deserialize(item)
                self.TaskStatus.append(obj)
        self.RequestId = params.get("RequestId")


class DstInfo(AbstractModel):
    """遷移目的訊息

    """

    def __init__(self):
        """
        :param Region: 遷移目的地域
        :type Region: str
        :param Ip: 遷移目的Ip
        :type Ip: str
        :param Port: 遷移目的端口
        :type Port: str
        :param InstanceId: 遷移目的實例Id
        :type InstanceId: str
        """
        self.Region = None
        self.Ip = None
        self.Port = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")


class ListMigrationProjectRequest(AbstractModel):
    """ListMigrationProject請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 記錄起始數，預設值爲0
        :type Offset: int
        :param Limit: 返回條數，預設值爲500
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class ListMigrationProjectResponse(AbstractModel):
    """ListMigrationProject返回參數結構體

    """

    def __init__(self):
        """
        :param Projects: 項目清單
        :type Projects: list of Project
        :param TotalCount: 項目總數
        :type TotalCount: int
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.Projects = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Projects") is not None:
            self.Projects = []
            for item in params.get("Projects"):
                obj = Project()
                obj._deserialize(item)
                self.Projects.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListMigrationTaskRequest(AbstractModel):
    """ListMigrationTask請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 記錄起始數，預設值爲0
        :type Offset: int
        :param Limit: 記錄條數，預設值爲10
        :type Limit: int
        :param ProjectId: 項目ID，預設值爲空
        :type ProjectId: int
        """
        self.Offset = None
        self.Limit = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ProjectId = params.get("ProjectId")


class ListMigrationTaskResponse(AbstractModel):
    """ListMigrationTask返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 記錄總條數
        :type TotalCount: int
        :param Tasks: 遷移任務清單
        :type Tasks: list of Task
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyMigrationTaskBelongToProjectRequest(AbstractModel):
    """ModifyMigrationTaskBelongToProject請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: str
        :param ProjectId: 項目ID
        :type ProjectId: int
        """
        self.TaskId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ProjectId = params.get("ProjectId")


class ModifyMigrationTaskBelongToProjectResponse(AbstractModel):
    """ModifyMigrationTaskBelongToProject返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMigrationTaskStatusRequest(AbstractModel):
    """ModifyMigrationTaskStatus請求參數結構體

    """

    def __init__(self):
        """
        :param Status: 任務狀态
        :type Status: str
        :param TaskId: 任務ID
        :type TaskId: str
        """
        self.Status = None
        self.TaskId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.TaskId = params.get("TaskId")


class ModifyMigrationTaskStatusResponse(AbstractModel):
    """ModifyMigrationTaskStatus返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Project(AbstractModel):
    """清單類型

    """

    def __init__(self):
        """
        :param ProjectId: 項目ID
        :type ProjectId: int
        :param ProjectName: 項目名稱
        :type ProjectName: str
        """
        self.ProjectId = None
        self.ProjectName = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")


class RegisterMigrationTaskRequest(AbstractModel):
    """RegisterMigrationTask請求參數結構體

    """

    def __init__(self):
        """
        :param TaskType: 任務類型，取值database（資料庫遷移）、file（文件遷移）、host（主機遷移）
        :type TaskType: str
        :param TaskName: 任務名稱
        :type TaskName: str
        :param ServiceSupplier: 服務提供商名稱
        :type ServiceSupplier: str
        :param SrcInfo: 遷移任務源訊息
        :type SrcInfo: :class:`taifucloudcloud.msp.v20180319.models.SrcInfo`
        :param DstInfo: 遷移任務目的訊息
        :type DstInfo: :class:`taifucloudcloud.msp.v20180319.models.DstInfo`
        :param CreateTime: 遷移任務創建時間
        :type CreateTime: str
        :param UpdateTime: 遷移任務更新時間
        :type UpdateTime: str
        :param MigrateClass: 遷移類别，如資料庫遷移中mysql:mysql代表從mysql遷移到mysql，文件遷移中oss:cos代表從阿裏雲oss遷移到Top Cloud cos
        :type MigrateClass: str
        :param SrcAccessType: 源實例接入類型
        :type SrcAccessType: str
        :param SrcDatabaseType: 源實例資料庫類型
        :type SrcDatabaseType: str
        :param DstAccessType: 目标實例接入類型
        :type DstAccessType: str
        :param DstDatabaseType: 目标實例資料庫類型
        :type DstDatabaseType: str
        """
        self.TaskType = None
        self.TaskName = None
        self.ServiceSupplier = None
        self.SrcInfo = None
        self.DstInfo = None
        self.CreateTime = None
        self.UpdateTime = None
        self.MigrateClass = None
        self.SrcAccessType = None
        self.SrcDatabaseType = None
        self.DstAccessType = None
        self.DstDatabaseType = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.TaskName = params.get("TaskName")
        self.ServiceSupplier = params.get("ServiceSupplier")
        if params.get("SrcInfo") is not None:
            self.SrcInfo = SrcInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("DstInfo") is not None:
            self.DstInfo = DstInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.MigrateClass = params.get("MigrateClass")
        self.SrcAccessType = params.get("SrcAccessType")
        self.SrcDatabaseType = params.get("SrcDatabaseType")
        self.DstAccessType = params.get("DstAccessType")
        self.DstDatabaseType = params.get("DstDatabaseType")


class RegisterMigrationTaskResponse(AbstractModel):
    """RegisterMigrationTask返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: str
        :param RequestId: 唯一請求ID，每次請求都會返回。定位問題時需要提供該次請求的RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class SrcInfo(AbstractModel):
    """遷移源訊息

    """

    def __init__(self):
        """
        :param Region: 遷移源地域
        :type Region: str
        :param Ip: 遷移源Ip
        :type Ip: str
        :param Port: 遷移源端口
        :type Port: str
        :param InstanceId: 遷移源實例Id
        :type InstanceId: str
        """
        self.Region = None
        self.Ip = None
        self.Port = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")


class Task(AbstractModel):
    """遷移任務類别

    """

    def __init__(self):
        """
        :param TaskId: 任務Id
        :type TaskId: str
        :param TaskName: 任務名稱
        :type TaskName: str
        :param MigrationType: 遷移類型
        :type MigrationType: str
        :param Status: 遷移狀态
        :type Status: str
        :param ProjectId: 項目Id
        :type ProjectId: int
        :param ProjectName: 項目名稱
        :type ProjectName: str
        :param SrcInfo: 遷移源訊息
        :type SrcInfo: :class:`taifucloudcloud.msp.v20180319.models.SrcInfo`
        :param MigrationTimeLine: 遷移時間訊息
        :type MigrationTimeLine: :class:`taifucloudcloud.msp.v20180319.models.TimeObj`
        :param Updated: 狀态更新時間
        :type Updated: str
        :param DstInfo: 遷移目的訊息
        :type DstInfo: :class:`taifucloudcloud.msp.v20180319.models.DstInfo`
        """
        self.TaskId = None
        self.TaskName = None
        self.MigrationType = None
        self.Status = None
        self.ProjectId = None
        self.ProjectName = None
        self.SrcInfo = None
        self.MigrationTimeLine = None
        self.Updated = None
        self.DstInfo = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskName = params.get("TaskName")
        self.MigrationType = params.get("MigrationType")
        self.Status = params.get("Status")
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        if params.get("SrcInfo") is not None:
            self.SrcInfo = SrcInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("MigrationTimeLine") is not None:
            self.MigrationTimeLine = TimeObj()
            self.MigrationTimeLine._deserialize(params.get("MigrationTimeLine"))
        self.Updated = params.get("Updated")
        if params.get("DstInfo") is not None:
            self.DstInfo = DstInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))


class TaskStatus(AbstractModel):
    """遷移詳情清單

    """

    def __init__(self):
        """
        :param Status: 遷移狀态
        :type Status: str
        :param Progress: 遷移進度
        :type Progress: str
        :param UpdateTime: 遷移日期
        :type UpdateTime: str
        """
        self.Status = None
        self.Progress = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Progress = params.get("Progress")
        self.UpdateTime = params.get("UpdateTime")


class TimeObj(AbstractModel):
    """時間對象

    """

    def __init__(self):
        """
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param EndTime: 結束時間
        :type EndTime: str
        """
        self.CreateTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.EndTime = params.get("EndTime")