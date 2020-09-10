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


class AlgorithmSpecification(AbstractModel):
    """算法配置

    """

    def __init__(self):
        """
        :param TrainingImageName: 映像名字
注意：此欄位可能返回 null，表示取不到有效值。
        :type TrainingImageName: str
        :param TrainingInputMode: 輸入模式File|Pipe
注意：此欄位可能返回 null，表示取不到有效值。
        :type TrainingInputMode: str
        :param AlgorithmName: 算法名字
注意：此欄位可能返回 null，表示取不到有效值。
        :type AlgorithmName: str
        """
        self.TrainingImageName = None
        self.TrainingInputMode = None
        self.AlgorithmName = None


    def _deserialize(self, params):
        self.TrainingImageName = params.get("TrainingImageName")
        self.TrainingInputMode = params.get("TrainingInputMode")
        self.AlgorithmName = params.get("AlgorithmName")


class CodeRepoSummary(AbstractModel):
    """儲存庫清單

    """

    def __init__(self):
        """
        :param CreationTime: 創建時間
        :type CreationTime: str
        :param LastModifiedTime: 更新時間
        :type LastModifiedTime: str
        :param CodeRepositoryName: 儲存庫名稱
        :type CodeRepositoryName: str
        :param GitConfig: Git配置
        :type GitConfig: :class:`tencentcloud.tione.v20191022.models.GitConfig`
        :param NoSecret: 是否有Git憑證
        :type NoSecret: bool
        """
        self.CreationTime = None
        self.LastModifiedTime = None
        self.CodeRepositoryName = None
        self.GitConfig = None
        self.NoSecret = None


    def _deserialize(self, params):
        self.CreationTime = params.get("CreationTime")
        self.LastModifiedTime = params.get("LastModifiedTime")
        self.CodeRepositoryName = params.get("CodeRepositoryName")
        if params.get("GitConfig") is not None:
            self.GitConfig = GitConfig()
            self.GitConfig._deserialize(params.get("GitConfig"))
        self.NoSecret = params.get("NoSecret")


class CosDataSource(AbstractModel):
    """cos路徑

    """

    def __init__(self):
        """
        :param Bucket: cos桶
注意：此欄位可能返回 null，表示取不到有效值。
        :type Bucket: str
        :param KeyPrefix: cos文件key
注意：此欄位可能返回 null，表示取不到有效值。
        :type KeyPrefix: str
        :param DataDistributionType: 分布式數據下載方式
注意：此欄位可能返回 null，表示取不到有效值。
        :type DataDistributionType: str
        :param DataType: 數據類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type DataType: str
        """
        self.Bucket = None
        self.KeyPrefix = None
        self.DataDistributionType = None
        self.DataType = None


    def _deserialize(self, params):
        self.Bucket = params.get("Bucket")
        self.KeyPrefix = params.get("KeyPrefix")
        self.DataDistributionType = params.get("DataDistributionType")
        self.DataType = params.get("DataType")


class CreateCodeRepositoryRequest(AbstractModel):
    """CreateCodeRepository請求參數結構體

    """

    def __init__(self):
        """
        :param CodeRepositoryName: 儲存庫名稱
        :type CodeRepositoryName: str
        :param GitConfig: Git相關配置
        :type GitConfig: :class:`tencentcloud.tione.v20191022.models.GitConfig`
        :param GitSecret: Git憑證
        :type GitSecret: :class:`tencentcloud.tione.v20191022.models.GitSecret`
        """
        self.CodeRepositoryName = None
        self.GitConfig = None
        self.GitSecret = None


    def _deserialize(self, params):
        self.CodeRepositoryName = params.get("CodeRepositoryName")
        if params.get("GitConfig") is not None:
            self.GitConfig = GitConfig()
            self.GitConfig._deserialize(params.get("GitConfig"))
        if params.get("GitSecret") is not None:
            self.GitSecret = GitSecret()
            self.GitSecret._deserialize(params.get("GitSecret"))


class CreateCodeRepositoryResponse(AbstractModel):
    """CreateCodeRepository返回參數結構體

    """

    def __init__(self):
        """
        :param CodeRepositoryName: 儲存庫名稱
        :type CodeRepositoryName: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CodeRepositoryName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CodeRepositoryName = params.get("CodeRepositoryName")
        self.RequestId = params.get("RequestId")


class CreateNotebookInstanceRequest(AbstractModel):
    """CreateNotebookInstance請求參數結構體

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook實例名稱
        :type NotebookInstanceName: str
        :param InstanceType: Notebook算力類型
        :type InstanceType: str
        :param VolumeSizeInGB: 數據卷大小(GB)
        :type VolumeSizeInGB: int
        :param DirectInternetAccess: 外網訪問權限，可取值Enabled/Disabled
        :type DirectInternetAccess: str
        :param RootAccess: Root用戶權限，可取值Enabled/Disabled
        :type RootAccess: str
        :param SubnetId: 子網ID
        :type SubnetId: str
        :param LifecycleScriptsName: 生命週期腳本名稱
        :type LifecycleScriptsName: str
        :param DefaultCodeRepository: 預設儲存庫名稱
可以是已創建的儲存庫名稱或者已https://開頭的公共git庫
        :type DefaultCodeRepository: str
        :param AdditionalCodeRepositories: 其他儲存庫清單
每個元素可以是已創建的儲存庫名稱或者已https://開頭的公共git庫
        :type AdditionalCodeRepositories: list of str
        """
        self.NotebookInstanceName = None
        self.InstanceType = None
        self.VolumeSizeInGB = None
        self.DirectInternetAccess = None
        self.RootAccess = None
        self.SubnetId = None
        self.LifecycleScriptsName = None
        self.DefaultCodeRepository = None
        self.AdditionalCodeRepositories = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")
        self.InstanceType = params.get("InstanceType")
        self.VolumeSizeInGB = params.get("VolumeSizeInGB")
        self.DirectInternetAccess = params.get("DirectInternetAccess")
        self.RootAccess = params.get("RootAccess")
        self.SubnetId = params.get("SubnetId")
        self.LifecycleScriptsName = params.get("LifecycleScriptsName")
        self.DefaultCodeRepository = params.get("DefaultCodeRepository")
        self.AdditionalCodeRepositories = params.get("AdditionalCodeRepositories")


class CreateNotebookInstanceResponse(AbstractModel):
    """CreateNotebookInstance返回參數結構體

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook實例名字
        :type NotebookInstanceName: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NotebookInstanceName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")
        self.RequestId = params.get("RequestId")


class CreateNotebookLifecycleScriptRequest(AbstractModel):
    """CreateNotebookLifecycleScript請求參數結構體

    """

    def __init__(self):
        """
        :param NotebookLifecycleScriptsName: Notebook生命週期腳本名稱
        :type NotebookLifecycleScriptsName: str
        :param CreateScript: 創建腳本，base64編碼格式
        :type CreateScript: str
        :param StartScript: 啓動腳本，base64編碼格式
        :type StartScript: str
        """
        self.NotebookLifecycleScriptsName = None
        self.CreateScript = None
        self.StartScript = None


    def _deserialize(self, params):
        self.NotebookLifecycleScriptsName = params.get("NotebookLifecycleScriptsName")
        self.CreateScript = params.get("CreateScript")
        self.StartScript = params.get("StartScript")


class CreateNotebookLifecycleScriptResponse(AbstractModel):
    """CreateNotebookLifecycleScript返回參數結構體

    """

    def __init__(self):
        """
        :param NotebookLifecycleScriptsName: 生命週期腳本名稱
        :type NotebookLifecycleScriptsName: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NotebookLifecycleScriptsName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NotebookLifecycleScriptsName = params.get("NotebookLifecycleScriptsName")
        self.RequestId = params.get("RequestId")


class CreatePresignedNotebookInstanceUrlRequest(AbstractModel):
    """CreatePresignedNotebookInstanceUrl請求參數結構體

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook實例名稱
        :type NotebookInstanceName: str
        :param SessionExpirationDurationInSeconds: session有效時間，秒
        :type SessionExpirationDurationInSeconds: int
        """
        self.NotebookInstanceName = None
        self.SessionExpirationDurationInSeconds = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")
        self.SessionExpirationDurationInSeconds = params.get("SessionExpirationDurationInSeconds")


class CreatePresignedNotebookInstanceUrlResponse(AbstractModel):
    """CreatePresignedNotebookInstanceUrl返回參數結構體

    """

    def __init__(self):
        """
        :param AuthorizedUrl: 授權url
        :type AuthorizedUrl: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AuthorizedUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AuthorizedUrl = params.get("AuthorizedUrl")
        self.RequestId = params.get("RequestId")


class CreateTrainingJobRequest(AbstractModel):
    """CreateTrainingJob請求參數結構體

    """

    def __init__(self):
        """
        :param AlgorithmSpecification: 算法映像配置
        :type AlgorithmSpecification: :class:`tencentcloud.tione.v20191022.models.AlgorithmSpecification`
        :param InputDataConfig: 輸入數據配置
        :type InputDataConfig: list of InputDataConfig
        :param OutputDataConfig: 輸出數據配置
        :type OutputDataConfig: :class:`tencentcloud.tione.v20191022.models.OutputDataConfig`
        :param ResourceConfig: 資源實例配置
        :type ResourceConfig: :class:`tencentcloud.tione.v20191022.models.ResourceConfig`
        :param TrainingJobName: 訓練任務名稱
        :type TrainingJobName: str
        :param StoppingCondition: 中止條件
        :type StoppingCondition: :class:`tencentcloud.tione.v20191022.models.StoppingCondition`
        :param VpcConfig: 私有網絡配置
        :type VpcConfig: :class:`tencentcloud.tione.v20191022.models.VpcConfig`
        :param HyperParameters: 算法超級參數
        :type HyperParameters: str
        :param EnvConfig: 環境變量配置
        :type EnvConfig: list of EnvConfig
        :param RoleName: 角色名稱
        :type RoleName: str
        """
        self.AlgorithmSpecification = None
        self.InputDataConfig = None
        self.OutputDataConfig = None
        self.ResourceConfig = None
        self.TrainingJobName = None
        self.StoppingCondition = None
        self.VpcConfig = None
        self.HyperParameters = None
        self.EnvConfig = None
        self.RoleName = None


    def _deserialize(self, params):
        if params.get("AlgorithmSpecification") is not None:
            self.AlgorithmSpecification = AlgorithmSpecification()
            self.AlgorithmSpecification._deserialize(params.get("AlgorithmSpecification"))
        if params.get("InputDataConfig") is not None:
            self.InputDataConfig = []
            for item in params.get("InputDataConfig"):
                obj = InputDataConfig()
                obj._deserialize(item)
                self.InputDataConfig.append(obj)
        if params.get("OutputDataConfig") is not None:
            self.OutputDataConfig = OutputDataConfig()
            self.OutputDataConfig._deserialize(params.get("OutputDataConfig"))
        if params.get("ResourceConfig") is not None:
            self.ResourceConfig = ResourceConfig()
            self.ResourceConfig._deserialize(params.get("ResourceConfig"))
        self.TrainingJobName = params.get("TrainingJobName")
        if params.get("StoppingCondition") is not None:
            self.StoppingCondition = StoppingCondition()
            self.StoppingCondition._deserialize(params.get("StoppingCondition"))
        if params.get("VpcConfig") is not None:
            self.VpcConfig = VpcConfig()
            self.VpcConfig._deserialize(params.get("VpcConfig"))
        self.HyperParameters = params.get("HyperParameters")
        if params.get("EnvConfig") is not None:
            self.EnvConfig = []
            for item in params.get("EnvConfig"):
                obj = EnvConfig()
                obj._deserialize(item)
                self.EnvConfig.append(obj)
        self.RoleName = params.get("RoleName")


class CreateTrainingJobResponse(AbstractModel):
    """CreateTrainingJob返回參數結構體

    """

    def __init__(self):
        """
        :param TrainingJobName: 訓練任務名稱
        :type TrainingJobName: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TrainingJobName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TrainingJobName = params.get("TrainingJobName")
        self.RequestId = params.get("RequestId")


class DataSource(AbstractModel):
    """數據源

    """

    def __init__(self):
        """
        :param CosDataSource: cos數據源
注意：此欄位可能返回 null，表示取不到有效值。
        :type CosDataSource: :class:`tencentcloud.tione.v20191022.models.CosDataSource`
        :param FileSystemDataSource: 文件系統輸入源
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileSystemDataSource: :class:`tencentcloud.tione.v20191022.models.FileSystemDataSource`
        """
        self.CosDataSource = None
        self.FileSystemDataSource = None


    def _deserialize(self, params):
        if params.get("CosDataSource") is not None:
            self.CosDataSource = CosDataSource()
            self.CosDataSource._deserialize(params.get("CosDataSource"))
        if params.get("FileSystemDataSource") is not None:
            self.FileSystemDataSource = FileSystemDataSource()
            self.FileSystemDataSource._deserialize(params.get("FileSystemDataSource"))


class DeleteCodeRepositoryRequest(AbstractModel):
    """DeleteCodeRepository請求參數結構體

    """

    def __init__(self):
        """
        :param CodeRepositoryName: 儲存庫名稱
        :type CodeRepositoryName: str
        """
        self.CodeRepositoryName = None


    def _deserialize(self, params):
        self.CodeRepositoryName = params.get("CodeRepositoryName")


class DeleteCodeRepositoryResponse(AbstractModel):
    """DeleteCodeRepository返回參數結構體

    """

    def __init__(self):
        """
        :param CodeRepositoryName: 儲存庫名稱
        :type CodeRepositoryName: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CodeRepositoryName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CodeRepositoryName = params.get("CodeRepositoryName")
        self.RequestId = params.get("RequestId")


class DeleteNotebookInstanceRequest(AbstractModel):
    """DeleteNotebookInstance請求參數結構體

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook實例名稱
        :type NotebookInstanceName: str
        """
        self.NotebookInstanceName = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")


class DeleteNotebookInstanceResponse(AbstractModel):
    """DeleteNotebookInstance返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNotebookLifecycleScriptRequest(AbstractModel):
    """DeleteNotebookLifecycleScript請求參數結構體

    """

    def __init__(self):
        """
        :param NotebookLifecycleScriptsName: 生命週期腳本名稱
        :type NotebookLifecycleScriptsName: str
        :param Forcible: 是否忽略已關聯的 notebook 實例強行删除生命週期腳本，預設 false
        :type Forcible: bool
        """
        self.NotebookLifecycleScriptsName = None
        self.Forcible = None


    def _deserialize(self, params):
        self.NotebookLifecycleScriptsName = params.get("NotebookLifecycleScriptsName")
        self.Forcible = params.get("Forcible")


class DeleteNotebookLifecycleScriptResponse(AbstractModel):
    """DeleteNotebookLifecycleScript返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeCodeRepositoriesRequest(AbstractModel):
    """DescribeCodeRepositories請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 返回數量，預設爲20
        :type Limit: int
        :param Filters: 過濾條件。
instance-name - String - 是否必填：否 -（過濾條件）按照名稱過濾。
search-by-name - String - 是否必填：否 -（過濾條件）按照名稱檢索，模糊比對。
        :type Filters: list of Filter
        :param SortOrder: 排序規則。預設取Descending
Descending 按更新時間降序
Ascending 按更新時間升序
        :type SortOrder: str
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.SortOrder = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.SortOrder = params.get("SortOrder")


class DescribeCodeRepositoriesResponse(AbstractModel):
    """DescribeCodeRepositories返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 儲存庫總數目
        :type TotalCount: int
        :param CodeRepoSet: 儲存庫清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type CodeRepoSet: list of CodeRepoSummary
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.CodeRepoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("CodeRepoSet") is not None:
            self.CodeRepoSet = []
            for item in params.get("CodeRepoSet"):
                obj = CodeRepoSummary()
                obj._deserialize(item)
                self.CodeRepoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCodeRepositoryRequest(AbstractModel):
    """DescribeCodeRepository請求參數結構體

    """

    def __init__(self):
        """
        :param CodeRepositoryName: 儲存庫名稱
        :type CodeRepositoryName: str
        """
        self.CodeRepositoryName = None


    def _deserialize(self, params):
        self.CodeRepositoryName = params.get("CodeRepositoryName")


class DescribeCodeRepositoryResponse(AbstractModel):
    """DescribeCodeRepository返回參數結構體

    """

    def __init__(self):
        """
        :param CreationTime: 創建時間
        :type CreationTime: str
        :param LastModifiedTime: 更新時間
        :type LastModifiedTime: str
        :param CodeRepositoryName: 儲存庫名稱
        :type CodeRepositoryName: str
        :param GitConfig: Git儲存配置
        :type GitConfig: :class:`tencentcloud.tione.v20191022.models.GitConfig`
        :param NoSecret: 是否有Git憑證
        :type NoSecret: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CreationTime = None
        self.LastModifiedTime = None
        self.CodeRepositoryName = None
        self.GitConfig = None
        self.NoSecret = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CreationTime = params.get("CreationTime")
        self.LastModifiedTime = params.get("LastModifiedTime")
        self.CodeRepositoryName = params.get("CodeRepositoryName")
        if params.get("GitConfig") is not None:
            self.GitConfig = GitConfig()
            self.GitConfig._deserialize(params.get("GitConfig"))
        self.NoSecret = params.get("NoSecret")
        self.RequestId = params.get("RequestId")


class DescribeNotebookInstanceRequest(AbstractModel):
    """DescribeNotebookInstance請求參數結構體

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook實例名稱
        :type NotebookInstanceName: str
        """
        self.NotebookInstanceName = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")


class DescribeNotebookInstanceResponse(AbstractModel):
    """DescribeNotebookInstance返回參數結構體

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook實例名稱
        :type NotebookInstanceName: str
        :param InstanceType: Notebook算力資源類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param RoleArn: 角色的資源描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type RoleArn: str
        :param DirectInternetAccess: 外網訪問權限
注意：此欄位可能返回 null，表示取不到有效值。
        :type DirectInternetAccess: str
        :param RootAccess: Root用戶權限
注意：此欄位可能返回 null，表示取不到有效值。
        :type RootAccess: str
        :param SubnetId: 子網ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param VolumeSizeInGB: 數據卷大小(GB)
注意：此欄位可能返回 null，表示取不到有效值。
        :type VolumeSizeInGB: int
        :param FailureReason: 創建失敗原因
注意：此欄位可能返回 null，表示取不到有效值。
        :type FailureReason: str
        :param CreationTime: Notebook實例創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreationTime: str
        :param LastModifiedTime: Notebook實例最近修改時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type LastModifiedTime: str
        :param LogUrl: Notebook實例日志連結
注意：此欄位可能返回 null，表示取不到有效值。
        :type LogUrl: str
        :param NotebookInstanceStatus: Notebook實例狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type NotebookInstanceStatus: str
        :param InstanceId: Notebook實例ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param LifecycleScriptsName: notebook生命週期腳本名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type LifecycleScriptsName: str
        :param DefaultCodeRepository: 預設儲存庫名稱
可以是已創建的儲存庫名稱或者已https://開頭的公共git庫
注意：此欄位可能返回 null，表示取不到有效值。
        :type DefaultCodeRepository: str
        :param AdditionalCodeRepositories: 其他儲存庫清單
每個元素可以是已創建的儲存庫名稱或者已https://開頭的公共git庫
注意：此欄位可能返回 null，表示取不到有效值。
        :type AdditionalCodeRepositories: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NotebookInstanceName = None
        self.InstanceType = None
        self.RoleArn = None
        self.DirectInternetAccess = None
        self.RootAccess = None
        self.SubnetId = None
        self.VolumeSizeInGB = None
        self.FailureReason = None
        self.CreationTime = None
        self.LastModifiedTime = None
        self.LogUrl = None
        self.NotebookInstanceStatus = None
        self.InstanceId = None
        self.LifecycleScriptsName = None
        self.DefaultCodeRepository = None
        self.AdditionalCodeRepositories = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")
        self.InstanceType = params.get("InstanceType")
        self.RoleArn = params.get("RoleArn")
        self.DirectInternetAccess = params.get("DirectInternetAccess")
        self.RootAccess = params.get("RootAccess")
        self.SubnetId = params.get("SubnetId")
        self.VolumeSizeInGB = params.get("VolumeSizeInGB")
        self.FailureReason = params.get("FailureReason")
        self.CreationTime = params.get("CreationTime")
        self.LastModifiedTime = params.get("LastModifiedTime")
        self.LogUrl = params.get("LogUrl")
        self.NotebookInstanceStatus = params.get("NotebookInstanceStatus")
        self.InstanceId = params.get("InstanceId")
        self.LifecycleScriptsName = params.get("LifecycleScriptsName")
        self.DefaultCodeRepository = params.get("DefaultCodeRepository")
        self.AdditionalCodeRepositories = params.get("AdditionalCodeRepositories")
        self.RequestId = params.get("RequestId")


class DescribeNotebookInstancesRequest(AbstractModel):
    """DescribeNotebookInstances請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制數目
        :type Limit: int
        :param SortOrder: 排序規則。預設取Descending
Descending 按更新時間降序
Ascending 按更新時間升序
        :type SortOrder: str
        :param Filters: 過濾條件。
instance-name - String - 是否必填：否 -（過濾條件）按照名稱過濾。
search-by-name - String - 是否必填：否 -（過濾條件）按照名稱檢索，模糊比對。
lifecycle-name - String - 是否必填：否 -（過濾條件）按照生命週期腳本名稱過濾。
default-code-repo-name - String - 是否必填：否 -（過濾條件）按照預設儲存庫名稱過濾。
additional-code-repo-name - String - 是否必填：否 -（過濾條件）按照其他儲存庫名稱過濾。
        :type Filters: list of Filter
        :param SortBy: 【廢棄欄位】排序欄位
        :type SortBy: str
        """
        self.Offset = None
        self.Limit = None
        self.SortOrder = None
        self.Filters = None
        self.SortBy = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SortOrder = params.get("SortOrder")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.SortBy = params.get("SortBy")


class DescribeNotebookInstancesResponse(AbstractModel):
    """DescribeNotebookInstances返回參數結構體

    """

    def __init__(self):
        """
        :param NotebookInstanceSet: Notebook實例清單
        :type NotebookInstanceSet: list of NotebookInstanceSummary
        :param TotalCount: Notebook實例總數目
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NotebookInstanceSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NotebookInstanceSet") is not None:
            self.NotebookInstanceSet = []
            for item in params.get("NotebookInstanceSet"):
                obj = NotebookInstanceSummary()
                obj._deserialize(item)
                self.NotebookInstanceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNotebookLifecycleScriptRequest(AbstractModel):
    """DescribeNotebookLifecycleScript請求參數結構體

    """

    def __init__(self):
        """
        :param NotebookLifecycleScriptsName: 生命週期腳本名稱
        :type NotebookLifecycleScriptsName: str
        """
        self.NotebookLifecycleScriptsName = None


    def _deserialize(self, params):
        self.NotebookLifecycleScriptsName = params.get("NotebookLifecycleScriptsName")


class DescribeNotebookLifecycleScriptResponse(AbstractModel):
    """DescribeNotebookLifecycleScript返回參數結構體

    """

    def __init__(self):
        """
        :param NotebookLifecycleScriptsName: 生命週期腳本名稱
        :type NotebookLifecycleScriptsName: str
        :param CreateScript: 創建腳本
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateScript: str
        :param StartScript: 啓動腳本
注意：此欄位可能返回 null，表示取不到有效值。
        :type StartScript: str
        :param CreationTime: 創建時間
        :type CreationTime: str
        :param LastModifiedTime: 最後修改時間
        :type LastModifiedTime: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NotebookLifecycleScriptsName = None
        self.CreateScript = None
        self.StartScript = None
        self.CreationTime = None
        self.LastModifiedTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NotebookLifecycleScriptsName = params.get("NotebookLifecycleScriptsName")
        self.CreateScript = params.get("CreateScript")
        self.StartScript = params.get("StartScript")
        self.CreationTime = params.get("CreationTime")
        self.LastModifiedTime = params.get("LastModifiedTime")
        self.RequestId = params.get("RequestId")


class DescribeNotebookLifecycleScriptsRequest(AbstractModel):
    """DescribeNotebookLifecycleScripts請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 返回數量，預設爲20
        :type Limit: int
        :param Filters: 過濾條件。
instance-name - String - 是否必填：否 -（過濾條件）按照名稱過濾。
search-by-name - String - 是否必填：否 -（過濾條件）按照名稱檢索，模糊比對。
        :type Filters: list of Filter
        :param SortOrder: 排序規則。預設取Descending
Descending 按更新時間降序
Ascending 按更新時間升序
        :type SortOrder: str
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.SortOrder = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.SortOrder = params.get("SortOrder")


class DescribeNotebookLifecycleScriptsResponse(AbstractModel):
    """DescribeNotebookLifecycleScripts返回參數結構體

    """

    def __init__(self):
        """
        :param NotebookLifecycleScriptsSet: Notebook生命週期腳本清單
        :type NotebookLifecycleScriptsSet: list of NotebookLifecycleScriptsSummary
        :param TotalCount: Notebook生命週期腳本總數量
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NotebookLifecycleScriptsSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NotebookLifecycleScriptsSet") is not None:
            self.NotebookLifecycleScriptsSet = []
            for item in params.get("NotebookLifecycleScriptsSet"):
                obj = NotebookLifecycleScriptsSummary()
                obj._deserialize(item)
                self.NotebookLifecycleScriptsSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTrainingJobRequest(AbstractModel):
    """DescribeTrainingJob請求參數結構體

    """

    def __init__(self):
        """
        :param TrainingJobName: 訓練任務名稱
        :type TrainingJobName: str
        """
        self.TrainingJobName = None


    def _deserialize(self, params):
        self.TrainingJobName = params.get("TrainingJobName")


class DescribeTrainingJobResponse(AbstractModel):
    """DescribeTrainingJob返回參數結構體

    """

    def __init__(self):
        """
        :param AlgorithmSpecification: 算法映像配置
        :type AlgorithmSpecification: :class:`tencentcloud.tione.v20191022.models.AlgorithmSpecification`
        :param TrainingJobName: 任務名稱
        :type TrainingJobName: str
        :param HyperParameters: 算法超級參數
注意：此欄位可能返回 null，表示取不到有效值。
        :type HyperParameters: str
        :param InputDataConfig: 輸入數據配置
        :type InputDataConfig: list of InputDataConfig
        :param OutputDataConfig: 輸出數據配置
        :type OutputDataConfig: :class:`tencentcloud.tione.v20191022.models.OutputDataConfig`
        :param StoppingCondition: 中止條件
注意：此欄位可能返回 null，表示取不到有效值。
        :type StoppingCondition: :class:`tencentcloud.tione.v20191022.models.StoppingCondition`
        :param ResourceConfig: 計算實例配置
        :type ResourceConfig: :class:`tencentcloud.tione.v20191022.models.ResourceConfig`
        :param VpcConfig: 私有網絡配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type VpcConfig: :class:`tencentcloud.tione.v20191022.models.VpcConfig`
        :param FailureReason: 失敗原因
注意：此欄位可能返回 null，表示取不到有效值。
        :type FailureReason: str
        :param LastModifiedTime: 最近修改時間
        :type LastModifiedTime: str
        :param TrainingStartTime: 任務開始時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type TrainingStartTime: str
        :param TrainingEndTime: 任務完成時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type TrainingEndTime: str
        :param ModelArtifacts: 模型輸出配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type ModelArtifacts: :class:`tencentcloud.tione.v20191022.models.ModelArtifacts`
        :param SecondaryStatus: 詳細狀态
        :type SecondaryStatus: str
        :param SecondaryStatusTransitions: 詳細狀态事件記錄
注意：此欄位可能返回 null，表示取不到有效值。
        :type SecondaryStatusTransitions: list of SecondaryStatusTransition
        :param RoleName: 角色名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type RoleName: str
        :param TrainingJobStatus: 任務狀态
        :type TrainingJobStatus: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AlgorithmSpecification = None
        self.TrainingJobName = None
        self.HyperParameters = None
        self.InputDataConfig = None
        self.OutputDataConfig = None
        self.StoppingCondition = None
        self.ResourceConfig = None
        self.VpcConfig = None
        self.FailureReason = None
        self.LastModifiedTime = None
        self.TrainingStartTime = None
        self.TrainingEndTime = None
        self.ModelArtifacts = None
        self.SecondaryStatus = None
        self.SecondaryStatusTransitions = None
        self.RoleName = None
        self.TrainingJobStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AlgorithmSpecification") is not None:
            self.AlgorithmSpecification = AlgorithmSpecification()
            self.AlgorithmSpecification._deserialize(params.get("AlgorithmSpecification"))
        self.TrainingJobName = params.get("TrainingJobName")
        self.HyperParameters = params.get("HyperParameters")
        if params.get("InputDataConfig") is not None:
            self.InputDataConfig = []
            for item in params.get("InputDataConfig"):
                obj = InputDataConfig()
                obj._deserialize(item)
                self.InputDataConfig.append(obj)
        if params.get("OutputDataConfig") is not None:
            self.OutputDataConfig = OutputDataConfig()
            self.OutputDataConfig._deserialize(params.get("OutputDataConfig"))
        if params.get("StoppingCondition") is not None:
            self.StoppingCondition = StoppingCondition()
            self.StoppingCondition._deserialize(params.get("StoppingCondition"))
        if params.get("ResourceConfig") is not None:
            self.ResourceConfig = ResourceConfig()
            self.ResourceConfig._deserialize(params.get("ResourceConfig"))
        if params.get("VpcConfig") is not None:
            self.VpcConfig = VpcConfig()
            self.VpcConfig._deserialize(params.get("VpcConfig"))
        self.FailureReason = params.get("FailureReason")
        self.LastModifiedTime = params.get("LastModifiedTime")
        self.TrainingStartTime = params.get("TrainingStartTime")
        self.TrainingEndTime = params.get("TrainingEndTime")
        if params.get("ModelArtifacts") is not None:
            self.ModelArtifacts = ModelArtifacts()
            self.ModelArtifacts._deserialize(params.get("ModelArtifacts"))
        self.SecondaryStatus = params.get("SecondaryStatus")
        if params.get("SecondaryStatusTransitions") is not None:
            self.SecondaryStatusTransitions = []
            for item in params.get("SecondaryStatusTransitions"):
                obj = SecondaryStatusTransition()
                obj._deserialize(item)
                self.SecondaryStatusTransitions.append(obj)
        self.RoleName = params.get("RoleName")
        self.TrainingJobStatus = params.get("TrainingJobStatus")
        self.RequestId = params.get("RequestId")


class EnvConfig(AbstractModel):
    """環境變量

    """

    def __init__(self):
        """
        :param Name: 名稱
        :type Name: str
        :param Value: 值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class FileSystemDataSource(AbstractModel):
    """文件系統輸入數據源

    """

    def __init__(self):
        """
        :param DirectoryPath: 文件系統目錄
注意：此欄位可能返回 null，表示取不到有效值。
        :type DirectoryPath: str
        :param FileSystemType: 文件系統類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileSystemType: str
        :param FileSystemAccessMode: 文件系統訪問模式
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileSystemAccessMode: str
        :param FileSystemId: 文件系統ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileSystemId: str
        """
        self.DirectoryPath = None
        self.FileSystemType = None
        self.FileSystemAccessMode = None
        self.FileSystemId = None


    def _deserialize(self, params):
        self.DirectoryPath = params.get("DirectoryPath")
        self.FileSystemType = params.get("FileSystemType")
        self.FileSystemAccessMode = params.get("FileSystemAccessMode")
        self.FileSystemId = params.get("FileSystemId")


class Filter(AbstractModel):
    """過濾器

    """

    def __init__(self):
        """
        :param Name: 過濾欄位名稱
        :type Name: str
        :param Values: 過濾欄位取值
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class GitConfig(AbstractModel):
    """儲存庫Git相關配置

    """

    def __init__(self):
        """
        :param RepositoryUrl: git網址
        :type RepositoryUrl: str
        :param Branch: 代碼分支
注意：此欄位可能返回 null，表示取不到有效值。
        :type Branch: str
        """
        self.RepositoryUrl = None
        self.Branch = None


    def _deserialize(self, params):
        self.RepositoryUrl = params.get("RepositoryUrl")
        self.Branch = params.get("Branch")


class GitSecret(AbstractModel):
    """Git憑證

    """

    def __init__(self):
        """
        :param NoSecret: 無秘鑰，預設選項
        :type NoSecret: bool
        :param Secret: Git用戶名密碼base64編碼後的字串
編碼前的内容應爲Json字串，如
{"UserName": "用戶名", "Password":"密碼"}
        :type Secret: str
        """
        self.NoSecret = None
        self.Secret = None


    def _deserialize(self, params):
        self.NoSecret = params.get("NoSecret")
        self.Secret = params.get("Secret")


class InputDataConfig(AbstractModel):
    """輸入數據配置

    """

    def __init__(self):
        """
        :param ChannelName: 通道名
注意：此欄位可能返回 null，表示取不到有效值。
        :type ChannelName: str
        :param DataSource: 數據源配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type DataSource: :class:`tencentcloud.tione.v20191022.models.DataSource`
        :param InputMode: 輸入類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type InputMode: str
        :param ContentType: 文件類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type ContentType: str
        """
        self.ChannelName = None
        self.DataSource = None
        self.InputMode = None
        self.ContentType = None


    def _deserialize(self, params):
        self.ChannelName = params.get("ChannelName")
        if params.get("DataSource") is not None:
            self.DataSource = DataSource()
            self.DataSource._deserialize(params.get("DataSource"))
        self.InputMode = params.get("InputMode")
        self.ContentType = params.get("ContentType")


class ModelArtifacts(AbstractModel):
    """模型輸出

    """

    def __init__(self):
        """
        :param CosModelArtifacts: cos輸出路徑
注意：此欄位可能返回 null，表示取不到有效值。
        :type CosModelArtifacts: str
        """
        self.CosModelArtifacts = None


    def _deserialize(self, params):
        self.CosModelArtifacts = params.get("CosModelArtifacts")


class NotebookInstanceSummary(AbstractModel):
    """notebook實例概覽

    """

    def __init__(self):
        """
        :param CreationTime: 創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreationTime: str
        :param LastModifiedTime: 最近修改時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type LastModifiedTime: str
        :param NotebookInstanceName: notebook實例名字
注意：此欄位可能返回 null，表示取不到有效值。
        :type NotebookInstanceName: str
        :param NotebookInstanceStatus: notebook實例狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type NotebookInstanceStatus: str
        :param InstanceType: 算力類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param InstanceId: 算力Id
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceId: str
        """
        self.CreationTime = None
        self.LastModifiedTime = None
        self.NotebookInstanceName = None
        self.NotebookInstanceStatus = None
        self.InstanceType = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.CreationTime = params.get("CreationTime")
        self.LastModifiedTime = params.get("LastModifiedTime")
        self.NotebookInstanceName = params.get("NotebookInstanceName")
        self.NotebookInstanceStatus = params.get("NotebookInstanceStatus")
        self.InstanceType = params.get("InstanceType")
        self.InstanceId = params.get("InstanceId")


class NotebookLifecycleScriptsSummary(AbstractModel):
    """notebook生命週期腳本實例概覽

    """

    def __init__(self):
        """
        :param NotebookLifecycleScriptsName: notebook生命週期腳本名稱
        :type NotebookLifecycleScriptsName: str
        :param CreationTime: 創建時間
        :type CreationTime: str
        :param LastModifiedTime: 修改時間
        :type LastModifiedTime: str
        """
        self.NotebookLifecycleScriptsName = None
        self.CreationTime = None
        self.LastModifiedTime = None


    def _deserialize(self, params):
        self.NotebookLifecycleScriptsName = params.get("NotebookLifecycleScriptsName")
        self.CreationTime = params.get("CreationTime")
        self.LastModifiedTime = params.get("LastModifiedTime")


class OutputDataConfig(AbstractModel):
    """輸出數據配置

    """

    def __init__(self):
        """
        :param CosOutputBucket: cos桶
注意：此欄位可能返回 null，表示取不到有效值。
        :type CosOutputBucket: str
        :param CosOutputKeyPrefix: cos文件key
注意：此欄位可能返回 null，表示取不到有效值。
        :type CosOutputKeyPrefix: str
        """
        self.CosOutputBucket = None
        self.CosOutputKeyPrefix = None


    def _deserialize(self, params):
        self.CosOutputBucket = params.get("CosOutputBucket")
        self.CosOutputKeyPrefix = params.get("CosOutputKeyPrefix")


class ResourceConfig(AbstractModel):
    """計算資源配置

    """

    def __init__(self):
        """
        :param InstanceCount: 計算實例數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceCount: int
        :param InstanceType: 計算實例類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param VolumeSizeInGB: 掛載CBS大小（GB）
注意：此欄位可能返回 null，表示取不到有效值。
        :type VolumeSizeInGB: int
        """
        self.InstanceCount = None
        self.InstanceType = None
        self.VolumeSizeInGB = None


    def _deserialize(self, params):
        self.InstanceCount = params.get("InstanceCount")
        self.InstanceType = params.get("InstanceType")
        self.VolumeSizeInGB = params.get("VolumeSizeInGB")


class SecondaryStatusTransition(AbstractModel):
    """二級狀态流水

    """

    def __init__(self):
        """
        :param StartTime: 狀态開始時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 狀态結束時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param Status: 狀态名
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: str
        :param StatusMessage: 狀态詳情
注意：此欄位可能返回 null，表示取不到有效值。
        :type StatusMessage: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.StatusMessage = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        self.StatusMessage = params.get("StatusMessage")


class StartNotebookInstanceRequest(AbstractModel):
    """StartNotebookInstance請求參數結構體

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook實例名稱
        :type NotebookInstanceName: str
        """
        self.NotebookInstanceName = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")


class StartNotebookInstanceResponse(AbstractModel):
    """StartNotebookInstance返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopNotebookInstanceRequest(AbstractModel):
    """StopNotebookInstance請求參數結構體

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook實例名稱
        :type NotebookInstanceName: str
        """
        self.NotebookInstanceName = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")


class StopNotebookInstanceResponse(AbstractModel):
    """StopNotebookInstance返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopTrainingJobRequest(AbstractModel):
    """StopTrainingJob請求參數結構體

    """

    def __init__(self):
        """
        :param TrainingJobName: 訓練任務名稱
        :type TrainingJobName: str
        """
        self.TrainingJobName = None


    def _deserialize(self, params):
        self.TrainingJobName = params.get("TrainingJobName")


class StopTrainingJobResponse(AbstractModel):
    """StopTrainingJob返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StoppingCondition(AbstractModel):
    """終止條件

    """

    def __init__(self):
        """
        :param MaxRuntimeInSeconds: 最長運作運作時間（秒）
注意：此欄位可能返回 null，表示取不到有效值。
        :type MaxRuntimeInSeconds: int
        """
        self.MaxRuntimeInSeconds = None


    def _deserialize(self, params):
        self.MaxRuntimeInSeconds = params.get("MaxRuntimeInSeconds")


class UpdateCodeRepositoryRequest(AbstractModel):
    """UpdateCodeRepository請求參數結構體

    """

    def __init__(self):
        """
        :param CodeRepositoryName: 查詢儲存庫名稱
        :type CodeRepositoryName: str
        :param GitSecret: Git憑證
        :type GitSecret: :class:`tencentcloud.tione.v20191022.models.GitSecret`
        """
        self.CodeRepositoryName = None
        self.GitSecret = None


    def _deserialize(self, params):
        self.CodeRepositoryName = params.get("CodeRepositoryName")
        if params.get("GitSecret") is not None:
            self.GitSecret = GitSecret()
            self.GitSecret._deserialize(params.get("GitSecret"))


class UpdateCodeRepositoryResponse(AbstractModel):
    """UpdateCodeRepository返回參數結構體

    """

    def __init__(self):
        """
        :param CodeRepositoryName: 儲存庫名稱
        :type CodeRepositoryName: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CodeRepositoryName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CodeRepositoryName = params.get("CodeRepositoryName")
        self.RequestId = params.get("RequestId")


class UpdateNotebookInstanceRequest(AbstractModel):
    """UpdateNotebookInstance請求參數結構體

    """

    def __init__(self):
        """
        :param NotebookInstanceName: Notebook實例名稱
        :type NotebookInstanceName: str
        :param RoleArn: 角色的資源描述
        :type RoleArn: str
        :param RootAccess: Root訪問權限
        :type RootAccess: str
        :param VolumeSizeInGB: 數據卷大小(GB)
        :type VolumeSizeInGB: int
        :param InstanceType: 算力資源類型
        :type InstanceType: str
        :param LifecycleScriptsName: notebook生命週期腳本名稱
        :type LifecycleScriptsName: str
        :param DisassociateLifecycleScript: 是否解綁生命週期腳本，預設 false。
如果本來就沒有綁定腳本，則忽略此參數；
如果本來有綁定腳本，此參數爲 true 則解綁；
如果本來有綁定腳本，此參數爲 false，則需要額外填入 LifecycleScriptsName
        :type DisassociateLifecycleScript: bool
        :param DefaultCodeRepository: 預設儲存庫名稱
可以是已創建的儲存庫名稱或者已https://開頭的公共git庫
        :type DefaultCodeRepository: str
        :param AdditionalCodeRepositories: 其他儲存庫清單
每個元素可以是已創建的儲存庫名稱或者已https://開頭的公共git庫
        :type AdditionalCodeRepositories: list of str
        :param DisassociateDefaultCodeRepository: 是否取消關聯預設儲存庫，預設false
該值爲true時，DefaultCodeRepository将被忽略
        :type DisassociateDefaultCodeRepository: bool
        :param DisassociateAdditionalCodeRepositories: 是否取消關聯其他儲存庫，預設false
該值爲true時，AdditionalCodeRepositories将被忽略
        :type DisassociateAdditionalCodeRepositories: bool
        """
        self.NotebookInstanceName = None
        self.RoleArn = None
        self.RootAccess = None
        self.VolumeSizeInGB = None
        self.InstanceType = None
        self.LifecycleScriptsName = None
        self.DisassociateLifecycleScript = None
        self.DefaultCodeRepository = None
        self.AdditionalCodeRepositories = None
        self.DisassociateDefaultCodeRepository = None
        self.DisassociateAdditionalCodeRepositories = None


    def _deserialize(self, params):
        self.NotebookInstanceName = params.get("NotebookInstanceName")
        self.RoleArn = params.get("RoleArn")
        self.RootAccess = params.get("RootAccess")
        self.VolumeSizeInGB = params.get("VolumeSizeInGB")
        self.InstanceType = params.get("InstanceType")
        self.LifecycleScriptsName = params.get("LifecycleScriptsName")
        self.DisassociateLifecycleScript = params.get("DisassociateLifecycleScript")
        self.DefaultCodeRepository = params.get("DefaultCodeRepository")
        self.AdditionalCodeRepositories = params.get("AdditionalCodeRepositories")
        self.DisassociateDefaultCodeRepository = params.get("DisassociateDefaultCodeRepository")
        self.DisassociateAdditionalCodeRepositories = params.get("DisassociateAdditionalCodeRepositories")


class UpdateNotebookInstanceResponse(AbstractModel):
    """UpdateNotebookInstance返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateNotebookLifecycleScriptRequest(AbstractModel):
    """UpdateNotebookLifecycleScript請求參數結構體

    """

    def __init__(self):
        """
        :param NotebookLifecycleScriptsName: notebook生命週期腳本名稱
        :type NotebookLifecycleScriptsName: str
        :param CreateScript: 創建腳本
        :type CreateScript: str
        :param StartScript: 啓動腳本
        :type StartScript: str
        """
        self.NotebookLifecycleScriptsName = None
        self.CreateScript = None
        self.StartScript = None


    def _deserialize(self, params):
        self.NotebookLifecycleScriptsName = params.get("NotebookLifecycleScriptsName")
        self.CreateScript = params.get("CreateScript")
        self.StartScript = params.get("StartScript")


class UpdateNotebookLifecycleScriptResponse(AbstractModel):
    """UpdateNotebookLifecycleScript返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class VpcConfig(AbstractModel):
    """VPC配置

    """

    def __init__(self):
        """
        :param SecurityGroupIds: 安全組id
注意：此欄位可能返回 null，表示取不到有效值。
        :type SecurityGroupIds: list of str
        :param SubnetId: 子網id
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubnetId: str
        """
        self.SecurityGroupIds = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.SubnetId = params.get("SubnetId")