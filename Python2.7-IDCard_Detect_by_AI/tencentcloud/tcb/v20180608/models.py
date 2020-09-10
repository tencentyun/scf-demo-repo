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


class DatabasesInfo(AbstractModel):
    """資料庫資源訊息

    """

    def __init__(self):
        """
        :param InstanceId: 資料庫唯一标識
        :type InstanceId: str
        :param Status: 狀态。包含以下取值：
<li>INITIALIZING：資源初始化中</li>
<li>RUNNING：運作中，可正常使用的狀态</li>
<li>UNUSABLE：禁用，不可用</li>
<li>OVERDUE：資源過期</li>
        :type Status: str
        :param Region: 所屬地域。
當前支援ap-shanghai
        :type Region: str
        """
        self.InstanceId = None
        self.Status = None
        self.Region = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Status = params.get("Status")
        self.Region = params.get("Region")


class DescribeDatabaseACLRequest(AbstractModel):
    """DescribeDatabaseACL請求參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 環境ID
        :type EnvId: str
        :param CollectionName: 集合名稱
        :type CollectionName: str
        """
        self.EnvId = None
        self.CollectionName = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.CollectionName = params.get("CollectionName")


class DescribeDatabaseACLResponse(AbstractModel):
    """DescribeDatabaseACL返回參數結構體

    """

    def __init__(self):
        """
        :param AclTag: 權限标簽。取值範圍：
<li> READONLY：所有用戶可讀，僅創建者和管理員可寫</li>
<li> PRIVATE：僅創建者及管理員可讀寫</li>
<li> ADMINWRITE：所有用戶可讀，僅管理員可寫</li>
<li> ADMINONLY：僅管理員可讀寫</li>
        :type AclTag: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AclTag = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AclTag = params.get("AclTag")
        self.RequestId = params.get("RequestId")


class DescribeEnvsRequest(AbstractModel):
    """DescribeEnvs請求參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 環境ID，如果傳了這個參數則只返回該環境的相關訊息
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")


class DescribeEnvsResponse(AbstractModel):
    """DescribeEnvs返回參數結構體

    """

    def __init__(self):
        """
        :param EnvList: 環境訊息清單
        :type EnvList: list of EnvInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.EnvList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EnvList") is not None:
            self.EnvList = []
            for item in params.get("EnvList"):
                obj = EnvInfo()
                obj._deserialize(item)
                self.EnvList.append(obj)
        self.RequestId = params.get("RequestId")


class EnvInfo(AbstractModel):
    """環境訊息

    """

    def __init__(self):
        """
        :param EnvId: 帳戶下該環境唯一标識
        :type EnvId: str
        :param Source: 環境來源。包含以下取值：
<li>miniapp： 小程式</li>
<li>qcloud ：Top Cloud </li>
        :type Source: str
        :param Alias: 環境别名，要以a-z開頭，不能包含 a-zA-z0-9- 以外的字元
        :type Alias: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param UpdateTime: 最後修改時間
        :type UpdateTime: str
        :param Status: 環境狀态。包含以下取值：
<li>NORMAL：正常可用</li>
<li>HALTED：停服，用量超限或後台封禁</li>
<li>UNAVAILABLE：服務不可用，可能是尚未初始化或者初始化過程中</li>
        :type Status: str
        :param Databases: 資料庫清單
        :type Databases: list of DatabasesInfo
        :param Storages: 儲存清單
        :type Storages: list of StorageInfo
        :param Functions: 函數清單
        :type Functions: list of FunctionInfo
        :param PackageId: tcb産品套餐ID，參考DescribePackages介面的返回值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PackageId: str
        :param PackageName: 套餐中文名稱，參考DescribePackages介面的返回值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PackageName: str
        """
        self.EnvId = None
        self.Source = None
        self.Alias = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Status = None
        self.Databases = None
        self.Storages = None
        self.Functions = None
        self.PackageId = None
        self.PackageName = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.Source = params.get("Source")
        self.Alias = params.get("Alias")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Status = params.get("Status")
        if params.get("Databases") is not None:
            self.Databases = []
            for item in params.get("Databases"):
                obj = DatabasesInfo()
                obj._deserialize(item)
                self.Databases.append(obj)
        if params.get("Storages") is not None:
            self.Storages = []
            for item in params.get("Storages"):
                obj = StorageInfo()
                obj._deserialize(item)
                self.Storages.append(obj)
        if params.get("Functions") is not None:
            self.Functions = []
            for item in params.get("Functions"):
                obj = FunctionInfo()
                obj._deserialize(item)
                self.Functions.append(obj)
        self.PackageId = params.get("PackageId")
        self.PackageName = params.get("PackageName")


class FunctionInfo(AbstractModel):
    """函數的訊息

    """

    def __init__(self):
        """
        :param Namespace: 命名空間
        :type Namespace: str
        :param Region: 所屬地域。
當前支援ap-shanghai
        :type Region: str
        """
        self.Namespace = None
        self.Region = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.Region = params.get("Region")


class ModifyDatabaseACLRequest(AbstractModel):
    """ModifyDatabaseACL請求參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 環境ID
        :type EnvId: str
        :param CollectionName: 集合名稱
        :type CollectionName: str
        :param AclTag: 權限标簽。取值範圍：
<li> READONLY：所有用戶可讀，僅創建者和管理員可寫</li>
<li> PRIVATE：僅創建者及管理員可讀寫</li>
<li> ADMINWRITE：所有用戶可讀，僅管理員可寫</li>
<li> ADMINONLY：僅管理員可讀寫</li>
        :type AclTag: str
        """
        self.EnvId = None
        self.CollectionName = None
        self.AclTag = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.CollectionName = params.get("CollectionName")
        self.AclTag = params.get("AclTag")


class ModifyDatabaseACLResponse(AbstractModel):
    """ModifyDatabaseACL返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyEnvRequest(AbstractModel):
    """ModifyEnv請求參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 環境ID
        :type EnvId: str
        :param Alias: 環境備注名，要以a-z開頭，不能包含 a-zA-z0-9- 以外的字元
        :type Alias: str
        """
        self.EnvId = None
        self.Alias = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.Alias = params.get("Alias")


class ModifyEnvResponse(AbstractModel):
    """ModifyEnv返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StorageInfo(AbstractModel):
    """StorageInfo 資源訊息

    """

    def __init__(self):
        """
        :param Region: 資源所屬地域。
當前支援ap-shanghai
        :type Region: str
        :param Bucket: 桶名，儲存資源的唯一标識
        :type Bucket: str
        :param CdnDomain: cdn 域名
        :type CdnDomain: str
        :param AppId: 資源所屬用戶的Top Cloud appId
        :type AppId: str
        """
        self.Region = None
        self.Bucket = None
        self.CdnDomain = None
        self.AppId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Bucket = params.get("Bucket")
        self.CdnDomain = params.get("CdnDomain")
        self.AppId = params.get("AppId")