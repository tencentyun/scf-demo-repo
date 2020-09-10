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


class AutoDelStrategyInfo(AbstractModel):
    """自動删除策略訊息

    """

    def __init__(self):
        """
        :param Username: 用戶名
        :type Username: str
        :param RepoName: 倉庫名
        :type RepoName: str
        :param Type: 類型
        :type Type: str
        :param Value: 策略值
        :type Value: int
        :param Valid: Valid
        :type Valid: int
        :param CreationTime: 創建時間
        :type CreationTime: str
        """
        self.Username = None
        self.RepoName = None
        self.Type = None
        self.Value = None
        self.Valid = None
        self.CreationTime = None


    def _deserialize(self, params):
        self.Username = params.get("Username")
        self.RepoName = params.get("RepoName")
        self.Type = params.get("Type")
        self.Value = params.get("Value")
        self.Valid = params.get("Valid")
        self.CreationTime = params.get("CreationTime")


class AutoDelStrategyInfoResp(AbstractModel):
    """獲取自動删除策略

    """

    def __init__(self):
        """
        :param TotalCount: 總數目
        :type TotalCount: int
        :param StrategyInfo: 自動删除策略清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type StrategyInfo: list of AutoDelStrategyInfo
        """
        self.TotalCount = None
        self.StrategyInfo = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("StrategyInfo") is not None:
            self.StrategyInfo = []
            for item in params.get("StrategyInfo"):
                obj = AutoDelStrategyInfo()
                obj._deserialize(item)
                self.StrategyInfo.append(obj)


class BatchDeleteImagePersonalRequest(AbstractModel):
    """BatchDeleteImagePersonal請求參數結構體

    """

    def __init__(self):
        """
        :param RepoName: 倉庫名稱
        :type RepoName: str
        :param Tags: Tag清單
        :type Tags: list of str
        """
        self.RepoName = None
        self.Tags = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Tags = params.get("Tags")


class BatchDeleteImagePersonalResponse(AbstractModel):
    """BatchDeleteImagePersonal返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BatchDeleteRepositoryPersonalRequest(AbstractModel):
    """BatchDeleteRepositoryPersonal請求參數結構體

    """

    def __init__(self):
        """
        :param RepoNames: 倉庫名稱數組
        :type RepoNames: list of str
        """
        self.RepoNames = None


    def _deserialize(self, params):
        self.RepoNames = params.get("RepoNames")


class BatchDeleteRepositoryPersonalResponse(AbstractModel):
    """BatchDeleteRepositoryPersonal返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateApplicationTriggerPersonalRequest(AbstractModel):
    """CreateApplicationTriggerPersonal請求參數結構體

    """

    def __init__(self):
        """
        :param RepoName: 觸發器關聯的映像倉庫，library/test格式
        :type RepoName: str
        :param TriggerName: 觸發器名稱
        :type TriggerName: str
        :param InvokeMethod: 觸發方式，"all"全部觸發，"taglist"指定tag觸發，"regex"正則觸發
        :type InvokeMethod: str
        :param ClusterId: 應用所在TKE集群ID
        :type ClusterId: str
        :param Namespace: 應用所在TKE集群命名空間
        :type Namespace: str
        :param WorkloadType: 應用所在TKE集群工作負載類型,支援Deployment、StatefulSet、DaemonSet、CronJob、Job。
        :type WorkloadType: str
        :param WorkloadName: 應用所在TKE集群工作負載名稱
        :type WorkloadName: str
        :param ContainerName: 應用所在TKE集群工作負載下容器名稱
        :type ContainerName: str
        :param ClusterRegion: 應用所在TKE集群地域
        :type ClusterRegion: int
        :param InvokeExpr: 觸發方式對應的表達式
        :type InvokeExpr: str
        """
        self.RepoName = None
        self.TriggerName = None
        self.InvokeMethod = None
        self.ClusterId = None
        self.Namespace = None
        self.WorkloadType = None
        self.WorkloadName = None
        self.ContainerName = None
        self.ClusterRegion = None
        self.InvokeExpr = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.TriggerName = params.get("TriggerName")
        self.InvokeMethod = params.get("InvokeMethod")
        self.ClusterId = params.get("ClusterId")
        self.Namespace = params.get("Namespace")
        self.WorkloadType = params.get("WorkloadType")
        self.WorkloadName = params.get("WorkloadName")
        self.ContainerName = params.get("ContainerName")
        self.ClusterRegion = params.get("ClusterRegion")
        self.InvokeExpr = params.get("InvokeExpr")


class CreateApplicationTriggerPersonalResponse(AbstractModel):
    """CreateApplicationTriggerPersonal返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateImageLifecyclePersonalRequest(AbstractModel):
    """CreateImageLifecyclePersonal請求參數結構體

    """

    def __init__(self):
        """
        :param RepoName: 倉庫名稱
        :type RepoName: str
        :param Type: keep_last_days:保留最近幾天的數據;keep_last_nums:保留最近多少個
        :type Type: str
        :param Val: 策略值
        :type Val: int
        """
        self.RepoName = None
        self.Type = None
        self.Val = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Type = params.get("Type")
        self.Val = params.get("Val")


class CreateImageLifecyclePersonalResponse(AbstractModel):
    """CreateImageLifecyclePersonal返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateInstanceRequest(AbstractModel):
    """CreateInstance請求參數結構體

    """

    def __init__(self):
        """
        :param RegistryName: 企業版實例名稱
        :type RegistryName: str
        :param RegistryType: 企業版實例類型
        :type RegistryType: str
        """
        self.RegistryName = None
        self.RegistryType = None


    def _deserialize(self, params):
        self.RegistryName = params.get("RegistryName")
        self.RegistryType = params.get("RegistryType")


class CreateInstanceResponse(AbstractModel):
    """CreateInstance返回參數結構體

    """

    def __init__(self):
        """
        :param RegistryId: 企業版實例Id
        :type RegistryId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RegistryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RequestId = params.get("RequestId")


class CreateInstanceTokenRequest(AbstractModel):
    """CreateInstanceToken請求參數結構體

    """

    def __init__(self):
        """
        :param RegistryId: 實例Id
        :type RegistryId: str
        :param TokenType: 訪問憑證類型，longterm 爲長期訪問憑證，temp 爲臨時訪問憑證，預設是臨時訪問憑證，有效期1小時
        :type TokenType: str
        :param Desc: 長期訪問憑證描述訊息
        :type Desc: str
        """
        self.RegistryId = None
        self.TokenType = None
        self.Desc = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.TokenType = params.get("TokenType")
        self.Desc = params.get("Desc")


class CreateInstanceTokenResponse(AbstractModel):
    """CreateInstanceToken返回參數結構體

    """

    def __init__(self):
        """
        :param Username: 用戶名
注意：此欄位可能返回 null，表示取不到有效值。
        :type Username: str
        :param Token: 訪問憑證
        :type Token: str
        :param ExpTime: 訪問憑證過期時間戳
        :type ExpTime: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Username = None
        self.Token = None
        self.ExpTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Username = params.get("Username")
        self.Token = params.get("Token")
        self.ExpTime = params.get("ExpTime")
        self.RequestId = params.get("RequestId")


class CreateNamespacePersonalRequest(AbstractModel):
    """CreateNamespacePersonal請求參數結構體

    """

    def __init__(self):
        """
        :param Namespace: 命名空間名稱
        :type Namespace: str
        """
        self.Namespace = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")


class CreateNamespacePersonalResponse(AbstractModel):
    """CreateNamespacePersonal返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateNamespaceRequest(AbstractModel):
    """CreateNamespace請求參數結構體

    """

    def __init__(self):
        """
        :param RegistryId: 實例ID
        :type RegistryId: str
        :param NamespaceName: 命名空間的名稱
        :type NamespaceName: str
        :param IsPublic: 是否公開，true爲公開，fale爲私有
        :type IsPublic: bool
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.IsPublic = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.IsPublic = params.get("IsPublic")


class CreateNamespaceResponse(AbstractModel):
    """CreateNamespace返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateRepositoryPersonalRequest(AbstractModel):
    """CreateRepositoryPersonal請求參數結構體

    """

    def __init__(self):
        """
        :param RepoName: 倉庫名稱
        :type RepoName: str
        :param Public: 是否公共,1:公共,0:私有
        :type Public: int
        :param Description: 倉庫描述
        :type Description: str
        """
        self.RepoName = None
        self.Public = None
        self.Description = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Public = params.get("Public")
        self.Description = params.get("Description")


class CreateRepositoryPersonalResponse(AbstractModel):
    """CreateRepositoryPersonal返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateRepositoryRequest(AbstractModel):
    """CreateRepository請求參數結構體

    """

    def __init__(self):
        """
        :param RegistryId: 實例ID
        :type RegistryId: str
        :param NamespaceName: 命名空間名稱
        :type NamespaceName: str
        :param RepositoryName: 倉庫名稱
        :type RepositoryName: str
        :param BriefDescription: 倉庫簡短描述
        :type BriefDescription: str
        :param Description: 倉庫詳細描述
        :type Description: str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None
        self.BriefDescription = None
        self.Description = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")
        self.BriefDescription = params.get("BriefDescription")
        self.Description = params.get("Description")


class CreateRepositoryResponse(AbstractModel):
    """CreateRepository返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateUserPersonalRequest(AbstractModel):
    """CreateUserPersonal請求參數結構體

    """

    def __init__(self):
        """
        :param Password: 用戶密碼
        :type Password: str
        """
        self.Password = None


    def _deserialize(self, params):
        self.Password = params.get("Password")


class CreateUserPersonalResponse(AbstractModel):
    """CreateUserPersonal返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateWebhookTriggerRequest(AbstractModel):
    """CreateWebhookTrigger請求參數結構體

    """

    def __init__(self):
        """
        :param RegistryId: 實例 Id
        :type RegistryId: str
        :param Trigger: 觸發器參數
        :type Trigger: :class:`taifucloudcloud.tcr.v20190924.models.WebhookTrigger`
        :param Namespace: 命名空間
        :type Namespace: str
        """
        self.RegistryId = None
        self.Trigger = None
        self.Namespace = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        if params.get("Trigger") is not None:
            self.Trigger = WebhookTrigger()
            self.Trigger._deserialize(params.get("Trigger"))
        self.Namespace = params.get("Namespace")


class CreateWebhookTriggerResponse(AbstractModel):
    """CreateWebhookTrigger返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteApplicationTriggerPersonalRequest(AbstractModel):
    """DeleteApplicationTriggerPersonal請求參數結構體

    """

    def __init__(self):
        """
        :param TriggerName: 觸發器名稱
        :type TriggerName: str
        """
        self.TriggerName = None


    def _deserialize(self, params):
        self.TriggerName = params.get("TriggerName")


class DeleteApplicationTriggerPersonalResponse(AbstractModel):
    """DeleteApplicationTriggerPersonal返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImageLifecycleGlobalPersonalRequest(AbstractModel):
    """DeleteImageLifecycleGlobalPersonal請求參數結構體

    """


class DeleteImageLifecycleGlobalPersonalResponse(AbstractModel):
    """DeleteImageLifecycleGlobalPersonal返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImageLifecyclePersonalRequest(AbstractModel):
    """DeleteImageLifecyclePersonal請求參數結構體

    """

    def __init__(self):
        """
        :param RepoName: 倉庫名稱
        :type RepoName: str
        """
        self.RepoName = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")


class DeleteImageLifecyclePersonalResponse(AbstractModel):
    """DeleteImageLifecyclePersonal返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImagePersonalRequest(AbstractModel):
    """DeleteImagePersonal請求參數結構體

    """

    def __init__(self):
        """
        :param RepoName: 倉庫名稱
        :type RepoName: str
        :param Tag: Tag名
        :type Tag: str
        """
        self.RepoName = None
        self.Tag = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Tag = params.get("Tag")


class DeleteImagePersonalResponse(AbstractModel):
    """DeleteImagePersonal返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteInstanceTokenRequest(AbstractModel):
    """DeleteInstanceToken請求參數結構體

    """

    def __init__(self):
        """
        :param RegistryId: 實例 ID
        :type RegistryId: str
        :param TokenId: 訪問憑證 ID
        :type TokenId: str
        """
        self.RegistryId = None
        self.TokenId = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.TokenId = params.get("TokenId")


class DeleteInstanceTokenResponse(AbstractModel):
    """DeleteInstanceToken返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNamespacePersonalRequest(AbstractModel):
    """DeleteNamespacePersonal請求參數結構體

    """

    def __init__(self):
        """
        :param Namespace: 命名空間名稱
        :type Namespace: str
        """
        self.Namespace = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")


class DeleteNamespacePersonalResponse(AbstractModel):
    """DeleteNamespacePersonal返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNamespaceRequest(AbstractModel):
    """DeleteNamespace請求參數結構體

    """

    def __init__(self):
        """
        :param RegistryId: 實例ID
        :type RegistryId: str
        :param NamespaceName: 命名空間的名稱
        :type NamespaceName: str
        """
        self.RegistryId = None
        self.NamespaceName = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")


class DeleteNamespaceResponse(AbstractModel):
    """DeleteNamespace返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRepositoryPersonalRequest(AbstractModel):
    """DeleteRepositoryPersonal請求參數結構體

    """

    def __init__(self):
        """
        :param RepoName: 倉庫名稱
        :type RepoName: str
        """
        self.RepoName = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")


class DeleteRepositoryPersonalResponse(AbstractModel):
    """DeleteRepositoryPersonal返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRepositoryRequest(AbstractModel):
    """DeleteRepository請求參數結構體

    """

    def __init__(self):
        """
        :param RegistryId: 實例Id
        :type RegistryId: str
        :param NamespaceName: 命名空間的名稱
        :type NamespaceName: str
        :param RepositoryName: 倉庫名稱的名稱
        :type RepositoryName: str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")


class DeleteRepositoryResponse(AbstractModel):
    """DeleteRepository返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWebhookTriggerRequest(AbstractModel):
    """DeleteWebhookTrigger請求參數結構體

    """

    def __init__(self):
        """
        :param RegistryId: 實例Id
        :type RegistryId: str
        :param Namespace: 命名空間
        :type Namespace: str
        :param Id: 觸發器 Id
        :type Id: int
        """
        self.RegistryId = None
        self.Namespace = None
        self.Id = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Namespace = params.get("Namespace")
        self.Id = params.get("Id")


class DeleteWebhookTriggerResponse(AbstractModel):
    """DeleteWebhookTrigger返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeApplicationTriggerLogPersonalRequest(AbstractModel):
    """DescribeApplicationTriggerLogPersonal請求參數結構體

    """

    def __init__(self):
        """
        :param RepoName: 倉庫名稱
        :type RepoName: str
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 返回最大數量，預設 20, 最大值 100
        :type Limit: int
        :param Order: 升序或降序
        :type Order: str
        :param OrderBy: 按某列排序
        :type OrderBy: str
        """
        self.RepoName = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderBy = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderBy = params.get("OrderBy")


class DescribeApplicationTriggerLogPersonalResp(AbstractModel):
    """查詢應用更新觸發器觸發日志返回值

    """

    def __init__(self):
        """
        :param TotalCount: 返回總數
        :type TotalCount: int
        :param LogInfo: 觸發日志清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type LogInfo: list of TriggerLogResp
        """
        self.TotalCount = None
        self.LogInfo = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("LogInfo") is not None:
            self.LogInfo = []
            for item in params.get("LogInfo"):
                obj = TriggerLogResp()
                obj._deserialize(item)
                self.LogInfo.append(obj)


class DescribeApplicationTriggerLogPersonalResponse(AbstractModel):
    """DescribeApplicationTriggerLogPersonal返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 觸發日志返回值
        :type Data: :class:`taifucloudcloud.tcr.v20190924.models.DescribeApplicationTriggerLogPersonalResp`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DescribeApplicationTriggerLogPersonalResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeApplicationTriggerPersonalRequest(AbstractModel):
    """DescribeApplicationTriggerPersonal請求參數結構體

    """

    def __init__(self):
        """
        :param RepoName: 倉庫名稱
        :type RepoName: str
        :param TriggerName: 觸發器名稱
        :type TriggerName: str
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 返回最大數量，預設 20, 最大值 100
        :type Limit: int
        """
        self.RepoName = None
        self.TriggerName = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.TriggerName = params.get("TriggerName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeApplicationTriggerPersonalResp(AbstractModel):
    """拉取觸發器清單返回值

    """

    def __init__(self):
        """
        :param TotalCount: 返回條目總數
        :type TotalCount: int
        :param TriggerInfo: 觸發器清單
        :type TriggerInfo: list of TriggerResp
        """
        self.TotalCount = None
        self.TriggerInfo = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TriggerInfo") is not None:
            self.TriggerInfo = []
            for item in params.get("TriggerInfo"):
                obj = TriggerResp()
                obj._deserialize(item)
                self.TriggerInfo.append(obj)


class DescribeApplicationTriggerPersonalResponse(AbstractModel):
    """DescribeApplicationTriggerPersonal返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 觸發器清單返回值
        :type Data: :class:`taifucloudcloud.tcr.v20190924.models.DescribeApplicationTriggerPersonalResp`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DescribeApplicationTriggerPersonalResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeFavorRepositoryPersonalRequest(AbstractModel):
    """DescribeFavorRepositoryPersonal請求參數結構體

    """

    def __init__(self):
        """
        :param RepoName: 倉庫名稱
        :type RepoName: str
        :param Limit: 分頁Limit
        :type Limit: int
        :param Offset: Offset用于分頁
        :type Offset: int
        """
        self.RepoName = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeFavorRepositoryPersonalResponse(AbstractModel):
    """DescribeFavorRepositoryPersonal返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 個人收藏倉庫清單返回訊息
        :type Data: :class:`taifucloudcloud.tcr.v20190924.models.FavorResp`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = FavorResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeImageFilterPersonalRequest(AbstractModel):
    """DescribeImageFilterPersonal請求參數結構體

    """

    def __init__(self):
        """
        :param RepoName: 倉庫名稱
        :type RepoName: str
        :param Tag: Tag名
        :type Tag: str
        """
        self.RepoName = None
        self.Tag = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Tag = params.get("Tag")


class DescribeImageFilterPersonalResponse(AbstractModel):
    """DescribeImageFilterPersonal返回參數結構體

    """

    def __init__(self):
        """
        :param Data: payload
        :type Data: :class:`taifucloudcloud.tcr.v20190924.models.SameImagesResp`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = SameImagesResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeImageLifecycleGlobalPersonalRequest(AbstractModel):
    """DescribeImageLifecycleGlobalPersonal請求參數結構體

    """


class DescribeImageLifecycleGlobalPersonalResponse(AbstractModel):
    """DescribeImageLifecycleGlobalPersonal返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 全局自動删除策略訊息
        :type Data: :class:`taifucloudcloud.tcr.v20190924.models.AutoDelStrategyInfoResp`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = AutoDelStrategyInfoResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeImageLifecyclePersonalRequest(AbstractModel):
    """DescribeImageLifecyclePersonal請求參數結構體

    """

    def __init__(self):
        """
        :param RepoName: 倉庫名稱
        :type RepoName: str
        """
        self.RepoName = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")


class DescribeImageLifecyclePersonalResponse(AbstractModel):
    """DescribeImageLifecyclePersonal返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 自動删除策略訊息
        :type Data: :class:`taifucloudcloud.tcr.v20190924.models.AutoDelStrategyInfoResp`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = AutoDelStrategyInfoResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeImageManifestsRequest(AbstractModel):
    """DescribeImageManifests請求參數結構體

    """

    def __init__(self):
        """
        :param RegistryId: 實例ID
        :type RegistryId: str
        :param NamespaceName: 命名空間名稱
        :type NamespaceName: str
        :param RepositoryName: 映像倉庫名稱
        :type RepositoryName: str
        :param ImageVersion: 映像版本
        :type ImageVersion: str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None
        self.ImageVersion = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")
        self.ImageVersion = params.get("ImageVersion")


class DescribeImageManifestsResponse(AbstractModel):
    """DescribeImageManifests返回參數結構體

    """

    def __init__(self):
        """
        :param Manifest: 映像的Manifest訊息
        :type Manifest: str
        :param Config: 映像的配置訊息
        :type Config: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Manifest = None
        self.Config = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Manifest = params.get("Manifest")
        self.Config = params.get("Config")
        self.RequestId = params.get("RequestId")


class DescribeImagePersonalRequest(AbstractModel):
    """DescribeImagePersonal請求參數結構體

    """

    def __init__(self):
        """
        :param RepoName: 倉庫名稱
        :type RepoName: str
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 返回最大數量，預設 20, 最大值 100
        :type Limit: int
        :param Tag: tag名稱，可根據輸入搜索
        :type Tag: str
        """
        self.RepoName = None
        self.Offset = None
        self.Limit = None
        self.Tag = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Tag = params.get("Tag")


class DescribeImagePersonalResponse(AbstractModel):
    """DescribeImagePersonal返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 映像tag訊息
        :type Data: :class:`taifucloudcloud.tcr.v20190924.models.TagInfoResp`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = TagInfoResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeImagesRequest(AbstractModel):
    """DescribeImages請求參數結構體

    """

    def __init__(self):
        """
        :param RegistryId: 實例ID
        :type RegistryId: str
        :param NamespaceName: 命名空間名稱
        :type NamespaceName: str
        :param RepositoryName: 映像倉庫名稱
        :type RepositoryName: str
        :param ImageVersion: 指定映像版本(Tag)，不填預設返回倉庫内全部容器映像
        :type ImageVersion: str
        :param Limit: 每頁個數，用于分頁，預設20
        :type Limit: int
        :param Offset: 頁數，預設值爲1
        :type Offset: int
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None
        self.ImageVersion = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")
        self.ImageVersion = params.get("ImageVersion")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeImagesResponse(AbstractModel):
    """DescribeImages返回參數結構體

    """

    def __init__(self):
        """
        :param ImageInfoList: 容器映像訊息清單
        :type ImageInfoList: list of TcrImageInfo
        :param TotalCount: 容器映像總數
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ImageInfoList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImageInfoList") is not None:
            self.ImageInfoList = []
            for item in params.get("ImageInfoList"):
                obj = TcrImageInfo()
                obj._deserialize(item)
                self.ImageInfoList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeInstanceStatusRequest(AbstractModel):
    """DescribeInstanceStatus請求參數結構體

    """

    def __init__(self):
        """
        :param RegistryIds: 實例ID的數組
        :type RegistryIds: list of str
        """
        self.RegistryIds = None


    def _deserialize(self, params):
        self.RegistryIds = params.get("RegistryIds")


class DescribeInstanceStatusResponse(AbstractModel):
    """DescribeInstanceStatus返回參數結構體

    """

    def __init__(self):
        """
        :param RegistryStatusSet: 實例的狀态清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type RegistryStatusSet: list of RegistryStatus
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RegistryStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegistryStatusSet") is not None:
            self.RegistryStatusSet = []
            for item in params.get("RegistryStatusSet"):
                obj = RegistryStatus()
                obj._deserialize(item)
                self.RegistryStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceTokenRequest(AbstractModel):
    """DescribeInstanceToken請求參數結構體

    """

    def __init__(self):
        """
        :param RegistryId: 實例 ID
        :type RegistryId: str
        :param Limit: 分頁單頁數量
        :type Limit: int
        :param Offset: 分頁偏移量
        :type Offset: int
        """
        self.RegistryId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeInstanceTokenResponse(AbstractModel):
    """DescribeInstanceToken返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 長期訪問憑證總數
        :type TotalCount: int
        :param Tokens: 長期訪問憑證清單
        :type Tokens: list of TcrInstanceToken
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Tokens = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tokens") is not None:
            self.Tokens = []
            for item in params.get("Tokens"):
                obj = TcrInstanceToken()
                obj._deserialize(item)
                self.Tokens.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances請求參數結構體

    """

    def __init__(self):
        """
        :param Registryids: 實例ID清單(爲空時，
表示獲取賬号下所有實例)
        :type Registryids: list of str
        :param Offset: 偏移量,預設0
        :type Offset: int
        :param Limit: 最大輸出條數，預設20，最大爲100
        :type Limit: int
        :param Filters: 過濾條件
        :type Filters: list of Filter
        :param AllRegion: 獲取所有地域的實例，預設爲False
        :type AllRegion: bool
        """
        self.Registryids = None
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.AllRegion = None


    def _deserialize(self, params):
        self.Registryids = params.get("Registryids")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.AllRegion = params.get("AllRegion")


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 總實例個數
        :type TotalCount: int
        :param Registries: 實例訊息清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Registries: list of Registry
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Registries = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Registries") is not None:
            self.Registries = []
            for item in params.get("Registries"):
                obj = Registry()
                obj._deserialize(item)
                self.Registries.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNamespacePersonalRequest(AbstractModel):
    """DescribeNamespacePersonal請求參數結構體

    """

    def __init__(self):
        """
        :param Namespace: 命名空間，支援模糊查詢
        :type Namespace: str
        :param Limit: 單頁數量
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        """
        self.Namespace = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeNamespacePersonalResponse(AbstractModel):
    """DescribeNamespacePersonal返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 用戶命名空間返回訊息
        :type Data: :class:`taifucloudcloud.tcr.v20190924.models.NamespaceInfoResp`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = NamespaceInfoResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeNamespacesRequest(AbstractModel):
    """DescribeNamespaces請求參數結構體

    """

    def __init__(self):
        """
        :param RegistryId: 實例Id
        :type RegistryId: str
        :param NamespaceName: 指定命名空間，不填寫預設查詢所有命名空間
        :type NamespaceName: str
        :param Limit: 每頁個數
        :type Limit: int
        :param Offset: 頁偏移
        :type Offset: int
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeNamespacesResponse(AbstractModel):
    """DescribeNamespaces返回參數結構體

    """

    def __init__(self):
        """
        :param NamespaceList: 命名空間清單訊息
        :type NamespaceList: list of TcrNamespaceInfo
        :param TotalCount: 總個數
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NamespaceList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NamespaceList") is not None:
            self.NamespaceList = []
            for item in params.get("NamespaceList"):
                obj = TcrNamespaceInfo()
                obj._deserialize(item)
                self.NamespaceList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRepositoriesRequest(AbstractModel):
    """DescribeRepositories請求參數結構體

    """

    def __init__(self):
        """
        :param RegistryId: 實例Id
        :type RegistryId: str
        :param NamespaceName: 指定命名空間，不填寫預設爲查詢所有命名空間下映像倉庫
        :type NamespaceName: str
        :param RepositoryName: 指定映像倉庫，不填寫預設查詢指定命名空間下所有映像倉庫
        :type RepositoryName: str
        :param Offset: 頁數，用于分頁
        :type Offset: int
        :param Limit: 每頁個數，用于分頁
        :type Limit: int
        :param SortBy: 基于欄位排序，支援的值有-creation_time,-name, -update_time
        :type SortBy: str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None
        self.Offset = None
        self.Limit = None
        self.SortBy = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SortBy = params.get("SortBy")


class DescribeRepositoriesResponse(AbstractModel):
    """DescribeRepositories返回參數結構體

    """

    def __init__(self):
        """
        :param RepositoryList: 倉庫訊息清單
        :type RepositoryList: list of TcrRepositoryInfo
        :param TotalCount: 總個數
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RepositoryList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RepositoryList") is not None:
            self.RepositoryList = []
            for item in params.get("RepositoryList"):
                obj = TcrRepositoryInfo()
                obj._deserialize(item)
                self.RepositoryList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRepositoryFilterPersonalRequest(AbstractModel):
    """DescribeRepositoryFilterPersonal請求參數結構體

    """

    def __init__(self):
        """
        :param RepoName: 搜索映像名
        :type RepoName: str
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 返回最大數量，預設 20，最大100
        :type Limit: int
        :param Public: 篩選條件：1表示public，0表示private
        :type Public: int
        :param Namespace: 命名空間
        :type Namespace: str
        """
        self.RepoName = None
        self.Offset = None
        self.Limit = None
        self.Public = None
        self.Namespace = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Public = params.get("Public")
        self.Namespace = params.get("Namespace")


class DescribeRepositoryFilterPersonalResponse(AbstractModel):
    """DescribeRepositoryFilterPersonal返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 倉庫訊息
        :type Data: :class:`taifucloudcloud.tcr.v20190924.models.SearchUserRepositoryResp`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = SearchUserRepositoryResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRepositoryOwnerPersonalRequest(AbstractModel):
    """DescribeRepositoryOwnerPersonal請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 返回最大數量，預設 20, 最大值 100
        :type Limit: int
        :param RepoName: 倉庫名稱
        :type RepoName: str
        """
        self.Offset = None
        self.Limit = None
        self.RepoName = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.RepoName = params.get("RepoName")


class DescribeRepositoryOwnerPersonalResponse(AbstractModel):
    """DescribeRepositoryOwnerPersonal返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 倉庫訊息
        :type Data: :class:`taifucloudcloud.tcr.v20190924.models.RepoInfoResp`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RepoInfoResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeRepositoryPersonalRequest(AbstractModel):
    """DescribeRepositoryPersonal請求參數結構體

    """

    def __init__(self):
        """
        :param RepoName: 倉庫名字
        :type RepoName: str
        """
        self.RepoName = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")


class DescribeRepositoryPersonalResponse(AbstractModel):
    """DescribeRepositoryPersonal返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 倉庫訊息
        :type Data: :class:`taifucloudcloud.tcr.v20190924.models.RepositoryInfoResp`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RepositoryInfoResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeUserQuotaPersonalRequest(AbstractModel):
    """DescribeUserQuotaPersonal請求參數結構體

    """


class DescribeUserQuotaPersonalResponse(AbstractModel):
    """DescribeUserQuotaPersonal返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 配額返回訊息
        :type Data: :class:`taifucloudcloud.tcr.v20190924.models.RespLimit`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RespLimit()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeWebhookTriggerLogRequest(AbstractModel):
    """DescribeWebhookTriggerLog請求參數結構體

    """

    def __init__(self):
        """
        :param RegistryId: 實例 Id
        :type RegistryId: str
        :param Namespace: 命名空間
        :type Namespace: str
        :param Id: 觸發器 Id
        :type Id: int
        :param Limit: 分頁單頁數量
        :type Limit: int
        :param Offset: 分頁偏移量
        :type Offset: int
        """
        self.RegistryId = None
        self.Namespace = None
        self.Id = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Namespace = params.get("Namespace")
        self.Id = params.get("Id")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeWebhookTriggerLogResponse(AbstractModel):
    """DescribeWebhookTriggerLog返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 總數
        :type TotalCount: int
        :param Logs: 日志清單
        :type Logs: list of WebhookTriggerLog
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Logs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Logs") is not None:
            self.Logs = []
            for item in params.get("Logs"):
                obj = WebhookTriggerLog()
                obj._deserialize(item)
                self.Logs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWebhookTriggerRequest(AbstractModel):
    """DescribeWebhookTrigger請求參數結構體

    """

    def __init__(self):
        """
        :param RegistryId: 實例Id
        :type RegistryId: str
        :param Limit: 分頁單頁數量
        :type Limit: int
        :param Offset: 分頁偏移量
        :type Offset: int
        :param Namespace: 命名空間
        :type Namespace: str
        """
        self.RegistryId = None
        self.Limit = None
        self.Offset = None
        self.Namespace = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Namespace = params.get("Namespace")


class DescribeWebhookTriggerResponse(AbstractModel):
    """DescribeWebhookTrigger返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 觸發器總數
        :type TotalCount: int
        :param Triggers: 觸發器清單
        :type Triggers: list of WebhookTrigger
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Triggers = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Triggers") is not None:
            self.Triggers = []
            for item in params.get("Triggers"):
                obj = WebhookTrigger()
                obj._deserialize(item)
                self.Triggers.append(obj)
        self.RequestId = params.get("RequestId")


class DupImageTagResp(AbstractModel):
    """複制映像tag返回值

    """

    def __init__(self):
        """
        :param Digest: 映像Digest值
        :type Digest: str
        """
        self.Digest = None


    def _deserialize(self, params):
        self.Digest = params.get("Digest")


class DuplicateImagePersonalRequest(AbstractModel):
    """DuplicateImagePersonal請求參數結構體

    """

    def __init__(self):
        """
        :param SrcImage: 源映像名稱，不包含domain。例如： taifucloudyun/foo:v1
        :type SrcImage: str
        :param DestImage: 目的映像名稱，不包含domain。例如： taifucloudyun/foo:latest
        :type DestImage: str
        """
        self.SrcImage = None
        self.DestImage = None


    def _deserialize(self, params):
        self.SrcImage = params.get("SrcImage")
        self.DestImage = params.get("DestImage")


class DuplicateImagePersonalResponse(AbstractModel):
    """DuplicateImagePersonal返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 複制映像返回值
        :type Data: :class:`taifucloudcloud.tcr.v20190924.models.DupImageTagResp`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DupImageTagResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class FavorResp(AbstractModel):
    """用于獲取收藏倉庫的響應

    """

    def __init__(self):
        """
        :param TotalCount: 收藏倉庫的總數
        :type TotalCount: int
        :param RepoInfo: 倉庫訊息數組
注意：此欄位可能返回 null，表示取不到有效值。
        :type RepoInfo: list of Favors
        """
        self.TotalCount = None
        self.RepoInfo = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RepoInfo") is not None:
            self.RepoInfo = []
            for item in params.get("RepoInfo"):
                obj = Favors()
                obj._deserialize(item)
                self.RepoInfo.append(obj)


class Favors(AbstractModel):
    """倉庫收藏

    """

    def __init__(self):
        """
        :param RepoName: 倉庫名字
        :type RepoName: str
        :param RepoType: 倉庫類型
        :type RepoType: str
        :param PullCount: Pull總共的次數
注意：此欄位可能返回 null，表示取不到有效值。
        :type PullCount: int
        :param FavorCount: 倉庫收藏次數
注意：此欄位可能返回 null，表示取不到有效值。
        :type FavorCount: int
        :param Public: 倉庫是否公開
注意：此欄位可能返回 null，表示取不到有效值。
        :type Public: int
        :param IsQcloudOfficial: 是否爲官方所有
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsQcloudOfficial: bool
        :param TagCount: 倉庫Tag的數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagCount: int
        :param Logo: Logo
注意：此欄位可能返回 null，表示取不到有效值。
        :type Logo: str
        :param Region: 地域
        :type Region: str
        :param RegionId: 地域的Id
        :type RegionId: int
        """
        self.RepoName = None
        self.RepoType = None
        self.PullCount = None
        self.FavorCount = None
        self.Public = None
        self.IsQcloudOfficial = None
        self.TagCount = None
        self.Logo = None
        self.Region = None
        self.RegionId = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.RepoType = params.get("RepoType")
        self.PullCount = params.get("PullCount")
        self.FavorCount = params.get("FavorCount")
        self.Public = params.get("Public")
        self.IsQcloudOfficial = params.get("IsQcloudOfficial")
        self.TagCount = params.get("TagCount")
        self.Logo = params.get("Logo")
        self.Region = params.get("Region")
        self.RegionId = params.get("RegionId")


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


class Header(AbstractModel):
    """Header KV

    """

    def __init__(self):
        """
        :param Key: Header Key
        :type Key: str
        :param Values: Header Values
        :type Values: list of str
        """
        self.Key = None
        self.Values = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Values = params.get("Values")


class Limit(AbstractModel):
    """共享映像倉庫用戶配額

    """

    def __init__(self):
        """
        :param Username: 用戶名
        :type Username: str
        :param Type: 配額的類型
        :type Type: str
        :param Value: 配置的值
        :type Value: int
        """
        self.Username = None
        self.Type = None
        self.Value = None


    def _deserialize(self, params):
        self.Username = params.get("Username")
        self.Type = params.get("Type")
        self.Value = params.get("Value")


class ManageImageLifecycleGlobalPersonalRequest(AbstractModel):
    """ManageImageLifecycleGlobalPersonal請求參數結構體

    """

    def __init__(self):
        """
        :param Type: global_keep_last_days:全局保留最近幾天的數據;global_keep_last_nums:全局保留最近多少個
        :type Type: str
        :param Val: 策略值
        :type Val: int
        """
        self.Type = None
        self.Val = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Val = params.get("Val")


class ManageImageLifecycleGlobalPersonalResponse(AbstractModel):
    """ManageImageLifecycleGlobalPersonal返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyApplicationTriggerPersonalRequest(AbstractModel):
    """ModifyApplicationTriggerPersonal請求參數結構體

    """

    def __init__(self):
        """
        :param RepoName: 觸發器關聯的映像倉庫，library/test格式
        :type RepoName: str
        :param TriggerName: 觸發器名稱
        :type TriggerName: str
        :param InvokeMethod: 觸發方式，"all"全部觸發，"taglist"指定tag觸發，"regex"正則觸發
        :type InvokeMethod: str
        :param InvokeExpr: 觸發方式對應的表達式
        :type InvokeExpr: str
        :param ClusterId: 應用所在TKE集群ID
        :type ClusterId: str
        :param Namespace: 應用所在TKE集群命名空間
        :type Namespace: str
        :param WorkloadType: 應用所在TKE集群工作負載類型,支援Deployment、StatefulSet、DaemonSet、CronJob、Job。
        :type WorkloadType: str
        :param WorkloadName: 應用所在TKE集群工作負載名稱
        :type WorkloadName: str
        :param ContainerName: 應用所在TKE集群工作負載下容器名稱
        :type ContainerName: str
        :param ClusterRegion: 應用所在TKE集群地域數字ID，如1（ ）、16（ ）
        :type ClusterRegion: int
        :param NewTriggerName: 新觸發器名稱
        :type NewTriggerName: str
        """
        self.RepoName = None
        self.TriggerName = None
        self.InvokeMethod = None
        self.InvokeExpr = None
        self.ClusterId = None
        self.Namespace = None
        self.WorkloadType = None
        self.WorkloadName = None
        self.ContainerName = None
        self.ClusterRegion = None
        self.NewTriggerName = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.TriggerName = params.get("TriggerName")
        self.InvokeMethod = params.get("InvokeMethod")
        self.InvokeExpr = params.get("InvokeExpr")
        self.ClusterId = params.get("ClusterId")
        self.Namespace = params.get("Namespace")
        self.WorkloadType = params.get("WorkloadType")
        self.WorkloadName = params.get("WorkloadName")
        self.ContainerName = params.get("ContainerName")
        self.ClusterRegion = params.get("ClusterRegion")
        self.NewTriggerName = params.get("NewTriggerName")


class ModifyApplicationTriggerPersonalResponse(AbstractModel):
    """ModifyApplicationTriggerPersonal返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInstanceTokenRequest(AbstractModel):
    """ModifyInstanceToken請求參數結構體

    """

    def __init__(self):
        """
        :param TokenId: 實例長期訪問憑證 ID
        :type TokenId: str
        :param Enable: 啓用或禁用實例長期訪問憑證
        :type Enable: bool
        :param RegistryId: 實例 ID
        :type RegistryId: str
        """
        self.TokenId = None
        self.Enable = None
        self.RegistryId = None


    def _deserialize(self, params):
        self.TokenId = params.get("TokenId")
        self.Enable = params.get("Enable")
        self.RegistryId = params.get("RegistryId")


class ModifyInstanceTokenResponse(AbstractModel):
    """ModifyInstanceToken返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNamespaceRequest(AbstractModel):
    """ModifyNamespace請求參數結構體

    """

    def __init__(self):
        """
        :param RegistryId: 實例Id
        :type RegistryId: str
        :param NamespaceName: 命名空間名稱
        :type NamespaceName: str
        :param IsPublic: 訪問級别，True爲公開，False爲私有
        :type IsPublic: bool
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.IsPublic = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.IsPublic = params.get("IsPublic")


class ModifyNamespaceResponse(AbstractModel):
    """ModifyNamespace返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRepositoryAccessPersonalRequest(AbstractModel):
    """ModifyRepositoryAccessPersonal請求參數結構體

    """

    def __init__(self):
        """
        :param RepoName: 倉庫名稱
        :type RepoName: str
        :param Public: 預設值爲0
        :type Public: int
        """
        self.RepoName = None
        self.Public = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Public = params.get("Public")


class ModifyRepositoryAccessPersonalResponse(AbstractModel):
    """ModifyRepositoryAccessPersonal返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRepositoryInfoPersonalRequest(AbstractModel):
    """ModifyRepositoryInfoPersonal請求參數結構體

    """

    def __init__(self):
        """
        :param RepoName: 倉庫名稱
        :type RepoName: str
        :param Description: 倉庫描述
        :type Description: str
        """
        self.RepoName = None
        self.Description = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.Description = params.get("Description")


class ModifyRepositoryInfoPersonalResponse(AbstractModel):
    """ModifyRepositoryInfoPersonal返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRepositoryRequest(AbstractModel):
    """ModifyRepository請求參數結構體

    """

    def __init__(self):
        """
        :param RegistryId: 實例ID
        :type RegistryId: str
        :param NamespaceName: 命名空間名稱
        :type NamespaceName: str
        :param RepositoryName: 映像倉庫名稱
        :type RepositoryName: str
        :param BriefDescription: 倉庫簡短描述
        :type BriefDescription: str
        :param Description: 倉庫詳細描述
        :type Description: str
        """
        self.RegistryId = None
        self.NamespaceName = None
        self.RepositoryName = None
        self.BriefDescription = None
        self.Description = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.NamespaceName = params.get("NamespaceName")
        self.RepositoryName = params.get("RepositoryName")
        self.BriefDescription = params.get("BriefDescription")
        self.Description = params.get("Description")


class ModifyRepositoryResponse(AbstractModel):
    """ModifyRepository返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyUserPasswordPersonalRequest(AbstractModel):
    """ModifyUserPasswordPersonal請求參數結構體

    """

    def __init__(self):
        """
        :param Password: 更新後的密碼
        :type Password: str
        """
        self.Password = None


    def _deserialize(self, params):
        self.Password = params.get("Password")


class ModifyUserPasswordPersonalResponse(AbstractModel):
    """ModifyUserPasswordPersonal返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyWebhookTriggerRequest(AbstractModel):
    """ModifyWebhookTrigger請求參數結構體

    """

    def __init__(self):
        """
        :param RegistryId: 實例Id
        :type RegistryId: str
        :param Trigger: 觸發器參數
        :type Trigger: :class:`taifucloudcloud.tcr.v20190924.models.WebhookTrigger`
        :param Namespace: 命名空間
        :type Namespace: str
        """
        self.RegistryId = None
        self.Trigger = None
        self.Namespace = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        if params.get("Trigger") is not None:
            self.Trigger = WebhookTrigger()
            self.Trigger._deserialize(params.get("Trigger"))
        self.Namespace = params.get("Namespace")


class ModifyWebhookTriggerResponse(AbstractModel):
    """ModifyWebhookTrigger返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NamespaceInfo(AbstractModel):
    """命名空間訊息

    """

    def __init__(self):
        """
        :param Namespace: 命名空間
        :type Namespace: str
        :param CreationTime: 創建時間
        :type CreationTime: str
        :param RepoCount: 命名空間下倉庫數量
        :type RepoCount: int
        """
        self.Namespace = None
        self.CreationTime = None
        self.RepoCount = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.CreationTime = params.get("CreationTime")
        self.RepoCount = params.get("RepoCount")


class NamespaceInfoResp(AbstractModel):
    """獲取命名空間訊息返回

    """

    def __init__(self):
        """
        :param NamespaceCount: 命名空間數量
        :type NamespaceCount: int
        :param NamespaceInfo: 命名空間訊息
        :type NamespaceInfo: list of NamespaceInfo
        """
        self.NamespaceCount = None
        self.NamespaceInfo = None


    def _deserialize(self, params):
        self.NamespaceCount = params.get("NamespaceCount")
        if params.get("NamespaceInfo") is not None:
            self.NamespaceInfo = []
            for item in params.get("NamespaceInfo"):
                obj = NamespaceInfo()
                obj._deserialize(item)
                self.NamespaceInfo.append(obj)


class NamespaceIsExistsResp(AbstractModel):
    """NamespaceIsExists返回類型

    """

    def __init__(self):
        """
        :param IsExist: 命名空間是否存在
        :type IsExist: bool
        :param IsPreserved: 是否爲保留命名空間
        :type IsPreserved: bool
        """
        self.IsExist = None
        self.IsPreserved = None


    def _deserialize(self, params):
        self.IsExist = params.get("IsExist")
        self.IsPreserved = params.get("IsPreserved")


class Registry(AbstractModel):
    """實例訊息結構體

    """

    def __init__(self):
        """
        :param RegistryId: 實例ID
        :type RegistryId: str
        :param RegistryName: 實例名稱
        :type RegistryName: str
        :param RegistryType: 實例規格
        :type RegistryType: str
        :param Status: 實例狀态
        :type Status: str
        :param PublicDomain: 實例的公共訪問網址
        :type PublicDomain: str
        :param CreatedAt: 實例創建時間
        :type CreatedAt: str
        :param RegionName: 地域名稱
        :type RegionName: str
        :param RegionId: 地域Id
        :type RegionId: int
        :param EnableAnonymous: 是否支援匿名
        :type EnableAnonymous: bool
        :param TokenValidTime: Token有效時間
        :type TokenValidTime: int
        :param InternalEndpoint: 實例内部訪問網址
        :type InternalEndpoint: str
        """
        self.RegistryId = None
        self.RegistryName = None
        self.RegistryType = None
        self.Status = None
        self.PublicDomain = None
        self.CreatedAt = None
        self.RegionName = None
        self.RegionId = None
        self.EnableAnonymous = None
        self.TokenValidTime = None
        self.InternalEndpoint = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.RegistryName = params.get("RegistryName")
        self.RegistryType = params.get("RegistryType")
        self.Status = params.get("Status")
        self.PublicDomain = params.get("PublicDomain")
        self.CreatedAt = params.get("CreatedAt")
        self.RegionName = params.get("RegionName")
        self.RegionId = params.get("RegionId")
        self.EnableAnonymous = params.get("EnableAnonymous")
        self.TokenValidTime = params.get("TokenValidTime")
        self.InternalEndpoint = params.get("InternalEndpoint")


class RegistryCondition(AbstractModel):
    """實例創建過程

    """

    def __init__(self):
        """
        :param Type: 實例創建過程類型
        :type Type: str
        :param Status: 實例創建過程狀态
        :type Status: str
        :param Reason: 轉換到該過程的簡明原因
注意：此欄位可能返回 null，表示取不到有效值。
        :type Reason: str
        """
        self.Type = None
        self.Status = None
        self.Reason = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.Reason = params.get("Reason")


class RegistryStatus(AbstractModel):
    """實例狀态

    """

    def __init__(self):
        """
        :param RegistryId: 實例的Id
        :type RegistryId: str
        :param Status: 實例的狀态
        :type Status: str
        :param Conditions: 附加狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type Conditions: list of RegistryCondition
        """
        self.RegistryId = None
        self.Status = None
        self.Conditions = None


    def _deserialize(self, params):
        self.RegistryId = params.get("RegistryId")
        self.Status = params.get("Status")
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = RegistryCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)


class RepoInfo(AbstractModel):
    """倉庫的訊息

    """

    def __init__(self):
        """
        :param RepoName: 倉庫名稱
        :type RepoName: str
        :param RepoType: 倉庫類型
        :type RepoType: str
        :param TagCount: Tag數量
        :type TagCount: int
        :param Public: 是否爲公開
        :type Public: int
        :param IsUserFavor: 是否爲用戶收藏
        :type IsUserFavor: bool
        :param IsQcloudOfficial: 是否爲Top Cloud 官方倉庫
        :type IsQcloudOfficial: bool
        :param FavorCount: 被收藏的個數
        :type FavorCount: int
        :param PullCount: 拉取的數量
        :type PullCount: int
        :param Description: 描述
        :type Description: str
        :param CreationTime: 倉庫創建時間
        :type CreationTime: str
        :param UpdateTime: 倉庫更新時間
        :type UpdateTime: str
        """
        self.RepoName = None
        self.RepoType = None
        self.TagCount = None
        self.Public = None
        self.IsUserFavor = None
        self.IsQcloudOfficial = None
        self.FavorCount = None
        self.PullCount = None
        self.Description = None
        self.CreationTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.RepoType = params.get("RepoType")
        self.TagCount = params.get("TagCount")
        self.Public = params.get("Public")
        self.IsUserFavor = params.get("IsUserFavor")
        self.IsQcloudOfficial = params.get("IsQcloudOfficial")
        self.FavorCount = params.get("FavorCount")
        self.PullCount = params.get("PullCount")
        self.Description = params.get("Description")
        self.CreationTime = params.get("CreationTime")
        self.UpdateTime = params.get("UpdateTime")


class RepoInfoResp(AbstractModel):
    """倉庫訊息的返回訊息

    """

    def __init__(self):
        """
        :param TotalCount: 倉庫總數
        :type TotalCount: int
        :param RepoInfo: 倉庫訊息清單
        :type RepoInfo: list of RepoInfo
        :param Server: Server訊息
        :type Server: str
        """
        self.TotalCount = None
        self.RepoInfo = None
        self.Server = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RepoInfo") is not None:
            self.RepoInfo = []
            for item in params.get("RepoInfo"):
                obj = RepoInfo()
                obj._deserialize(item)
                self.RepoInfo.append(obj)
        self.Server = params.get("Server")


class RepoIsExistResp(AbstractModel):
    """倉庫是否存在的返回值

    """

    def __init__(self):
        """
        :param IsExist: 倉庫是否存在
        :type IsExist: bool
        """
        self.IsExist = None


    def _deserialize(self, params):
        self.IsExist = params.get("IsExist")


class RepositoryInfoResp(AbstractModel):
    """查詢共享版倉庫訊息返回

    """

    def __init__(self):
        """
        :param RepoName: 映像倉庫名字
        :type RepoName: str
        :param RepoType: 映像倉庫類型
        :type RepoType: str
        :param Server: 映像倉庫服務網址
        :type Server: str
        :param CreationTime: 創建時間
        :type CreationTime: str
        :param Description: 映像倉庫描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type Description: str
        :param Public: 是否爲公有映像
        :type Public: int
        :param PullCount: 下載次數
        :type PullCount: int
        :param FavorCount: 收藏次數
        :type FavorCount: int
        :param IsUserFavor: 是否爲用戶收藏
        :type IsUserFavor: bool
        :param IsQcloudOfficial: 是否爲Top Cloud 官方映像
        :type IsQcloudOfficial: bool
        """
        self.RepoName = None
        self.RepoType = None
        self.Server = None
        self.CreationTime = None
        self.Description = None
        self.Public = None
        self.PullCount = None
        self.FavorCount = None
        self.IsUserFavor = None
        self.IsQcloudOfficial = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.RepoType = params.get("RepoType")
        self.Server = params.get("Server")
        self.CreationTime = params.get("CreationTime")
        self.Description = params.get("Description")
        self.Public = params.get("Public")
        self.PullCount = params.get("PullCount")
        self.FavorCount = params.get("FavorCount")
        self.IsUserFavor = params.get("IsUserFavor")
        self.IsQcloudOfficial = params.get("IsQcloudOfficial")


class RespLimit(AbstractModel):
    """用戶配額返回值

    """

    def __init__(self):
        """
        :param LimitInfo: 配額訊息
        :type LimitInfo: list of Limit
        """
        self.LimitInfo = None


    def _deserialize(self, params):
        if params.get("LimitInfo") is not None:
            self.LimitInfo = []
            for item in params.get("LimitInfo"):
                obj = Limit()
                obj._deserialize(item)
                self.LimitInfo.append(obj)


class SameImagesResp(AbstractModel):
    """指定tag映像内容相同的tag清單

    """

    def __init__(self):
        """
        :param SameImages: tag清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type SameImages: list of str
        """
        self.SameImages = None


    def _deserialize(self, params):
        self.SameImages = params.get("SameImages")


class SearchUserRepositoryResp(AbstractModel):
    """獲取滿足輸入搜索條件的用戶映像倉庫

    """

    def __init__(self):
        """
        :param TotalCount: 總個數
        :type TotalCount: int
        :param RepoInfo: 倉庫清單
        :type RepoInfo: list of RepoInfo
        :param Server: Server
        :type Server: str
        :param PrivilegeFiltered: PrivilegeFiltered
        :type PrivilegeFiltered: bool
        """
        self.TotalCount = None
        self.RepoInfo = None
        self.Server = None
        self.PrivilegeFiltered = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RepoInfo") is not None:
            self.RepoInfo = []
            for item in params.get("RepoInfo"):
                obj = RepoInfo()
                obj._deserialize(item)
                self.RepoInfo.append(obj)
        self.Server = params.get("Server")
        self.PrivilegeFiltered = params.get("PrivilegeFiltered")


class TagInfo(AbstractModel):
    """映像tag訊息

    """

    def __init__(self):
        """
        :param TagName: Tag名稱
        :type TagName: str
        :param TagId: 映像Id
        :type TagId: str
        :param ImageId: docker image 可以看到的id
        :type ImageId: str
        :param Size: 大小
        :type Size: str
        :param CreationTime: 映像的創建時間
        :type CreationTime: str
        :param DurationDays: 映像創建至今時間長度
注意：此欄位可能返回 null，表示取不到有效值。
        :type DurationDays: str
        :param Author: 映像的作者
        :type Author: str
        :param Architecture: 次映像建議運作的系統架構
        :type Architecture: str
        :param DockerVersion: 創建此映像的docker版本
        :type DockerVersion: str
        :param OS: 此映像建議運作系統
        :type OS: str
        :param SizeByte: SizeByte
        :type SizeByte: int
        :param Id: Id
        :type Id: int
        :param UpdateTime: 數據更新時間
        :type UpdateTime: str
        :param PushTime: 映像更新時間
        :type PushTime: str
        """
        self.TagName = None
        self.TagId = None
        self.ImageId = None
        self.Size = None
        self.CreationTime = None
        self.DurationDays = None
        self.Author = None
        self.Architecture = None
        self.DockerVersion = None
        self.OS = None
        self.SizeByte = None
        self.Id = None
        self.UpdateTime = None
        self.PushTime = None


    def _deserialize(self, params):
        self.TagName = params.get("TagName")
        self.TagId = params.get("TagId")
        self.ImageId = params.get("ImageId")
        self.Size = params.get("Size")
        self.CreationTime = params.get("CreationTime")
        self.DurationDays = params.get("DurationDays")
        self.Author = params.get("Author")
        self.Architecture = params.get("Architecture")
        self.DockerVersion = params.get("DockerVersion")
        self.OS = params.get("OS")
        self.SizeByte = params.get("SizeByte")
        self.Id = params.get("Id")
        self.UpdateTime = params.get("UpdateTime")
        self.PushTime = params.get("PushTime")


class TagInfoResp(AbstractModel):
    """Tag清單的返回值

    """

    def __init__(self):
        """
        :param TagCount: Tag的總數
        :type TagCount: int
        :param TagInfo: TagInfo清單
        :type TagInfo: list of TagInfo
        :param Server: Server
        :type Server: str
        :param RepoName: 倉庫名稱
        :type RepoName: str
        """
        self.TagCount = None
        self.TagInfo = None
        self.Server = None
        self.RepoName = None


    def _deserialize(self, params):
        self.TagCount = params.get("TagCount")
        if params.get("TagInfo") is not None:
            self.TagInfo = []
            for item in params.get("TagInfo"):
                obj = TagInfo()
                obj._deserialize(item)
                self.TagInfo.append(obj)
        self.Server = params.get("Server")
        self.RepoName = params.get("RepoName")


class TcrImageInfo(AbstractModel):
    """映像訊息

    """

    def __init__(self):
        """
        :param Digest: 哈希值
        :type Digest: str
        :param Size: 映像大小
        :type Size: int
        :param ImageVersion: Tag名稱
        :type ImageVersion: str
        :param UpdateTime: 更新時間
        :type UpdateTime: str
        """
        self.Digest = None
        self.Size = None
        self.ImageVersion = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Digest = params.get("Digest")
        self.Size = params.get("Size")
        self.ImageVersion = params.get("ImageVersion")
        self.UpdateTime = params.get("UpdateTime")


class TcrInstanceToken(AbstractModel):
    """實例登入令牌

    """

    def __init__(self):
        """
        :param Id: 令牌ID
        :type Id: str
        :param Desc: 令牌描述
        :type Desc: str
        :param RegistryId: 令牌所屬實例ID
        :type RegistryId: str
        :param Enabled: 令牌啓用狀态
        :type Enabled: bool
        :param CreatedAt: 令牌創建時間
        :type CreatedAt: str
        :param ExpiredAt: 令牌過期時間戳
        :type ExpiredAt: int
        """
        self.Id = None
        self.Desc = None
        self.RegistryId = None
        self.Enabled = None
        self.CreatedAt = None
        self.ExpiredAt = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Desc = params.get("Desc")
        self.RegistryId = params.get("RegistryId")
        self.Enabled = params.get("Enabled")
        self.CreatedAt = params.get("CreatedAt")
        self.ExpiredAt = params.get("ExpiredAt")


class TcrNamespaceInfo(AbstractModel):
    """Tcr 命名空間的描述

    """

    def __init__(self):
        """
        :param Name: 命名空間名稱
        :type Name: str
        :param CreationTime: 創建時間
        :type CreationTime: str
        :param Public: 訪問級别
        :type Public: bool
        :param NamespaceId: 命名空間的Id
        :type NamespaceId: int
        """
        self.Name = None
        self.CreationTime = None
        self.Public = None
        self.NamespaceId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.CreationTime = params.get("CreationTime")
        self.Public = params.get("Public")
        self.NamespaceId = params.get("NamespaceId")


class TcrRepositoryInfo(AbstractModel):
    """Tcr映像倉庫訊息

    """

    def __init__(self):
        """
        :param Name: 倉庫名稱
        :type Name: str
        :param Namespace: 命名空間名稱
        :type Namespace: str
        :param CreationTime: 創建時間
        :type CreationTime: str
        :param Public: 是否公開
        :type Public: bool
        :param Description: 倉庫詳細描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type Description: str
        :param BriefDescription: 簡單描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type BriefDescription: str
        :param UpdateTime: 更新時間
        :type UpdateTime: str
        """
        self.Name = None
        self.Namespace = None
        self.CreationTime = None
        self.Public = None
        self.Description = None
        self.BriefDescription = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Namespace = params.get("Namespace")
        self.CreationTime = params.get("CreationTime")
        self.Public = params.get("Public")
        self.Description = params.get("Description")
        self.BriefDescription = params.get("BriefDescription")
        self.UpdateTime = params.get("UpdateTime")


class TriggerInvokeCondition(AbstractModel):
    """觸發器觸發條件

    """

    def __init__(self):
        """
        :param InvokeMethod: 觸發方式
        :type InvokeMethod: str
        :param InvokeExpr: 觸發表達式
注意：此欄位可能返回 null，表示取不到有效值。
        :type InvokeExpr: str
        """
        self.InvokeMethod = None
        self.InvokeExpr = None


    def _deserialize(self, params):
        self.InvokeMethod = params.get("InvokeMethod")
        self.InvokeExpr = params.get("InvokeExpr")


class TriggerInvokePara(AbstractModel):
    """觸發器觸發參數

    """

    def __init__(self):
        """
        :param AppId: AppId
注意：此欄位可能返回 null，表示取不到有效值。
        :type AppId: str
        :param ClusterId: TKE集群ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param Namespace: TKE集群命名空間
注意：此欄位可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param ServiceName: TKE集群工作負載名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param ContainerName: TKE集群工作負載中容器名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ContainerName: str
        :param ClusterRegion: TKE集群地域數字ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterRegion: int
        """
        self.AppId = None
        self.ClusterId = None
        self.Namespace = None
        self.ServiceName = None
        self.ContainerName = None
        self.ClusterRegion = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.ClusterId = params.get("ClusterId")
        self.Namespace = params.get("Namespace")
        self.ServiceName = params.get("ServiceName")
        self.ContainerName = params.get("ContainerName")
        self.ClusterRegion = params.get("ClusterRegion")


class TriggerInvokeResult(AbstractModel):
    """觸發器觸發結果

    """

    def __init__(self):
        """
        :param ReturnCode: 請求TKE返回值
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReturnCode: int
        :param ReturnMsg: 請求TKE返回訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReturnMsg: str
        """
        self.ReturnCode = None
        self.ReturnMsg = None


    def _deserialize(self, params):
        self.ReturnCode = params.get("ReturnCode")
        self.ReturnMsg = params.get("ReturnMsg")


class TriggerLogResp(AbstractModel):
    """觸發器日志

    """

    def __init__(self):
        """
        :param RepoName: 倉庫名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type RepoName: str
        :param TagName: Tag名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagName: str
        :param TriggerName: 觸發器名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type TriggerName: str
        :param InvokeSource: 觸發方式
注意：此欄位可能返回 null，表示取不到有效值。
        :type InvokeSource: str
        :param InvokeAction: 觸發動作
注意：此欄位可能返回 null，表示取不到有效值。
        :type InvokeAction: str
        :param InvokeTime: 觸發時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type InvokeTime: str
        :param InvokeCondition: 觸發條件
注意：此欄位可能返回 null，表示取不到有效值。
        :type InvokeCondition: :class:`taifucloudcloud.tcr.v20190924.models.TriggerInvokeCondition`
        :param InvokePara: 觸發參數
注意：此欄位可能返回 null，表示取不到有效值。
        :type InvokePara: :class:`taifucloudcloud.tcr.v20190924.models.TriggerInvokePara`
        :param InvokeResult: 觸發結果
注意：此欄位可能返回 null，表示取不到有效值。
        :type InvokeResult: :class:`taifucloudcloud.tcr.v20190924.models.TriggerInvokeResult`
        """
        self.RepoName = None
        self.TagName = None
        self.TriggerName = None
        self.InvokeSource = None
        self.InvokeAction = None
        self.InvokeTime = None
        self.InvokeCondition = None
        self.InvokePara = None
        self.InvokeResult = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")
        self.TagName = params.get("TagName")
        self.TriggerName = params.get("TriggerName")
        self.InvokeSource = params.get("InvokeSource")
        self.InvokeAction = params.get("InvokeAction")
        self.InvokeTime = params.get("InvokeTime")
        if params.get("InvokeCondition") is not None:
            self.InvokeCondition = TriggerInvokeCondition()
            self.InvokeCondition._deserialize(params.get("InvokeCondition"))
        if params.get("InvokePara") is not None:
            self.InvokePara = TriggerInvokePara()
            self.InvokePara._deserialize(params.get("InvokePara"))
        if params.get("InvokeResult") is not None:
            self.InvokeResult = TriggerInvokeResult()
            self.InvokeResult._deserialize(params.get("InvokeResult"))


class TriggerResp(AbstractModel):
    """觸發器返回值

    """

    def __init__(self):
        """
        :param TriggerName: 觸發器名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type TriggerName: str
        :param InvokeSource: 觸發來源
注意：此欄位可能返回 null，表示取不到有效值。
        :type InvokeSource: str
        :param InvokeAction: 觸發動作
注意：此欄位可能返回 null，表示取不到有效值。
        :type InvokeAction: str
        :param CreateTime: 創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 更新時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param InvokeCondition: 觸發條件
注意：此欄位可能返回 null，表示取不到有效值。
        :type InvokeCondition: :class:`taifucloudcloud.tcr.v20190924.models.TriggerInvokeCondition`
        :param InvokePara: 觸發器參數
注意：此欄位可能返回 null，表示取不到有效值。
        :type InvokePara: :class:`taifucloudcloud.tcr.v20190924.models.TriggerInvokePara`
        """
        self.TriggerName = None
        self.InvokeSource = None
        self.InvokeAction = None
        self.CreateTime = None
        self.UpdateTime = None
        self.InvokeCondition = None
        self.InvokePara = None


    def _deserialize(self, params):
        self.TriggerName = params.get("TriggerName")
        self.InvokeSource = params.get("InvokeSource")
        self.InvokeAction = params.get("InvokeAction")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("InvokeCondition") is not None:
            self.InvokeCondition = TriggerInvokeCondition()
            self.InvokeCondition._deserialize(params.get("InvokeCondition"))
        if params.get("InvokePara") is not None:
            self.InvokePara = TriggerInvokePara()
            self.InvokePara._deserialize(params.get("InvokePara"))


class ValidateNamespaceExistPersonalRequest(AbstractModel):
    """ValidateNamespaceExistPersonal請求參數結構體

    """

    def __init__(self):
        """
        :param Namespace: 命名空間名稱
        :type Namespace: str
        """
        self.Namespace = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")


class ValidateNamespaceExistPersonalResponse(AbstractModel):
    """ValidateNamespaceExistPersonal返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 命名空間是否存在
        :type Data: :class:`taifucloudcloud.tcr.v20190924.models.NamespaceIsExistsResp`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = NamespaceIsExistsResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class ValidateRepositoryExistPersonalRequest(AbstractModel):
    """ValidateRepositoryExistPersonal請求參數結構體

    """

    def __init__(self):
        """
        :param RepoName: 倉庫名稱
        :type RepoName: str
        """
        self.RepoName = None


    def _deserialize(self, params):
        self.RepoName = params.get("RepoName")


class ValidateRepositoryExistPersonalResponse(AbstractModel):
    """ValidateRepositoryExistPersonal返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 倉庫是否存在
        :type Data: :class:`taifucloudcloud.tcr.v20190924.models.RepoIsExistResp`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = RepoIsExistResp()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class WebhookTarget(AbstractModel):
    """觸發器目标

    """

    def __init__(self):
        """
        :param Address: 目标網址
        :type Address: str
        :param Headers: 自定義 Headers
        :type Headers: list of Header
        """
        self.Address = None
        self.Headers = None


    def _deserialize(self, params):
        self.Address = params.get("Address")
        if params.get("Headers") is not None:
            self.Headers = []
            for item in params.get("Headers"):
                obj = Header()
                obj._deserialize(item)
                self.Headers.append(obj)


class WebhookTrigger(AbstractModel):
    """Webhook 觸發器

    """

    def __init__(self):
        """
        :param Name: 觸發器名稱
        :type Name: str
        :param Targets: 觸發器目标
        :type Targets: list of WebhookTarget
        :param EventTypes: 觸發動作
        :type EventTypes: list of str
        :param Condition: 觸發規則
        :type Condition: str
        :param Enabled: 啓用觸發器
        :type Enabled: bool
        :param Id: 觸發器Id
        :type Id: int
        :param Description: 觸發器描述
        :type Description: str
        """
        self.Name = None
        self.Targets = None
        self.EventTypes = None
        self.Condition = None
        self.Enabled = None
        self.Id = None
        self.Description = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = WebhookTarget()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.EventTypes = params.get("EventTypes")
        self.Condition = params.get("Condition")
        self.Enabled = params.get("Enabled")
        self.Id = params.get("Id")
        self.Description = params.get("Description")


class WebhookTriggerLog(AbstractModel):
    """觸發器日志

    """

    def __init__(self):
        """
        :param Id: 日志 Id
        :type Id: int
        :param TriggerId: 觸發器 Id
        :type TriggerId: int
        :param EventType: 事件類型
        :type EventType: str
        :param NotifyType: 通知類型
        :type NotifyType: str
        :param Detail: 詳情
        :type Detail: str
        :param CreationTime: 創建時間
        :type CreationTime: str
        :param UpdateTime: 更新時間
        :type UpdateTime: str
        :param Status: 狀态
        :type Status: str
        """
        self.Id = None
        self.TriggerId = None
        self.EventType = None
        self.NotifyType = None
        self.Detail = None
        self.CreationTime = None
        self.UpdateTime = None
        self.Status = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.TriggerId = params.get("TriggerId")
        self.EventType = params.get("EventType")
        self.NotifyType = params.get("NotifyType")
        self.Detail = params.get("Detail")
        self.CreationTime = params.get("CreationTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Status = params.get("Status")