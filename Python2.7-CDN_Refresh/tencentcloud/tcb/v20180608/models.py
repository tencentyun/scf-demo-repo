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


class AuthDomain(AbstractModel):
    """合法域名

    """

    def __init__(self):
        """
        :param Id: 域名ID
        :type Id: str
        :param Domain: 域名
        :type Domain: str
        :param Type: 域名類型。包含以下取值：
<li>SYSTEM</li>
<li>USER</li>
        :type Type: str
        :param Status: 狀态。包含以下取值：
<li>ENABLE</li>
<li>DISABLE</li>
        :type Status: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param UpdateTime: 更新時間
        :type UpdateTime: str
        """
        self.Id = None
        self.Domain = None
        self.Type = None
        self.Status = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Domain = params.get("Domain")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class CheckTcbServiceRequest(AbstractModel):
    """CheckTcbService請求參數結構體

    """


class CheckTcbServiceResponse(AbstractModel):
    """CheckTcbService返回參數結構體

    """

    def __init__(self):
        """
        :param Initialized: true表示已開通
        :type Initialized: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Initialized = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Initialized = params.get("Initialized")
        self.RequestId = params.get("RequestId")


class CommonServiceAPIRequest(AbstractModel):
    """CommonServiceAPI請求參數結構體

    """

    def __init__(self):
        """
        :param Service: Service名，需要轉發訪問的介面名
        :type Service: str
        :param JSONData: 需要轉發的雲API參數，要轉成JSON格式
        :type JSONData: str
        """
        self.Service = None
        self.JSONData = None


    def _deserialize(self, params):
        self.Service = params.get("Service")
        self.JSONData = params.get("JSONData")


class CommonServiceAPIResponse(AbstractModel):
    """CommonServiceAPI返回參數結構體

    """

    def __init__(self):
        """
        :param JSONResp: json格式response
        :type JSONResp: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.JSONResp = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JSONResp = params.get("JSONResp")
        self.RequestId = params.get("RequestId")


class CreateAuthDomainRequest(AbstractModel):
    """CreateAuthDomain請求參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 環境ID
        :type EnvId: str
        :param Domains: 安全域名
        :type Domains: list of str
        """
        self.EnvId = None
        self.Domains = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.Domains = params.get("Domains")


class CreateAuthDomainResponse(AbstractModel):
    """CreateAuthDomain返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateHostingDomainRequest(AbstractModel):
    """CreateHostingDomain請求參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 環境ID
        :type EnvId: str
        :param Domain: 域名
        :type Domain: str
        :param CertId: 證書ID
        :type CertId: str
        """
        self.EnvId = None
        self.Domain = None
        self.CertId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.Domain = params.get("Domain")
        self.CertId = params.get("CertId")


class CreateHostingDomainResponse(AbstractModel):
    """CreateHostingDomain返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateStaticStoreRequest(AbstractModel):
    """CreateStaticStore請求參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 環境ID
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")


class CreateStaticStoreResponse(AbstractModel):
    """CreateStaticStore返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 創建靜态資源結果(succ/fail)
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


class DeleteEndUserRequest(AbstractModel):
    """DeleteEndUser請求參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 環境ID
        :type EnvId: str
        :param UserList: 用戶清單，每一項都是uuid
        :type UserList: list of str
        """
        self.EnvId = None
        self.UserList = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.UserList = params.get("UserList")


class DeleteEndUserResponse(AbstractModel):
    """DeleteEndUser返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAuthDomainsRequest(AbstractModel):
    """DescribeAuthDomains請求參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 環境ID
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")


class DescribeAuthDomainsResponse(AbstractModel):
    """DescribeAuthDomains返回參數結構體

    """

    def __init__(self):
        """
        :param Domains: 安全域名清單清單
        :type Domains: list of AuthDomain
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Domains = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Domains") is not None:
            self.Domains = []
            for item in params.get("Domains"):
                obj = AuthDomain()
                obj._deserialize(item)
                self.Domains.append(obj)
        self.RequestId = params.get("RequestId")


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
        :param AclTag: 權限标簽。包含以下取值：
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


class DescribeEndUsersRequest(AbstractModel):
    """DescribeEndUsers請求參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 開發者的環境ID
        :type EnvId: str
        :param UUIds: 按照 uuid 清單過濾，最大個數爲100
        :type UUIds: list of str
        """
        self.EnvId = None
        self.UUIds = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.UUIds = params.get("UUIds")


class DescribeEndUsersResponse(AbstractModel):
    """DescribeEndUsers返回參數結構體

    """

    def __init__(self):
        """
        :param Total: 用戶總數
        :type Total: int
        :param Users: 用戶清單
        :type Users: list of EndUserInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Users = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Users") is not None:
            self.Users = []
            for item in params.get("Users"):
                obj = EndUserInfo()
                obj._deserialize(item)
                self.Users.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEnvFreeQuotaRequest(AbstractModel):
    """DescribeEnvFreeQuota請求參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 環境ID
        :type EnvId: str
        :param ResourceTypes: 資源類型：可選值：CDN, COS, FLEXDB, HOSTING, SCF
不傳則返回全部資源指标
        :type ResourceTypes: list of str
        """
        self.EnvId = None
        self.ResourceTypes = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ResourceTypes = params.get("ResourceTypes")


class DescribeEnvFreeQuotaResponse(AbstractModel):
    """DescribeEnvFreeQuota返回參數結構體

    """

    def __init__(self):
        """
        :param QuotaItems: 免費抵扣配額詳情
注意：此欄位可能返回 null，表示取不到有效值。
        :type QuotaItems: list of PostpayEnvQuota
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.QuotaItems = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("QuotaItems") is not None:
            self.QuotaItems = []
            for item in params.get("QuotaItems"):
                obj = PostpayEnvQuota()
                obj._deserialize(item)
                self.QuotaItems.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEnvLimitRequest(AbstractModel):
    """DescribeEnvLimit請求參數結構體

    """


class DescribeEnvLimitResponse(AbstractModel):
    """DescribeEnvLimit返回參數結構體

    """

    def __init__(self):
        """
        :param MaxEnvNum: 環境總數上限
        :type MaxEnvNum: int
        :param CurrentEnvNum: 目前環境總數
        :type CurrentEnvNum: int
        :param MaxFreeEnvNum: 免費環境數量上限
        :type MaxFreeEnvNum: int
        :param CurrentFreeEnvNum: 目前免費環境數量
        :type CurrentFreeEnvNum: int
        :param MaxDeleteTotal: 總計允許銷毀環境次數上限
        :type MaxDeleteTotal: int
        :param CurrentDeleteTotal: 目前已銷毀環境次數
        :type CurrentDeleteTotal: int
        :param MaxDeleteMonthly: 每月允許銷毀環境次數上限
        :type MaxDeleteMonthly: int
        :param CurrentDeleteMonthly: 本月已銷毀環境次數
        :type CurrentDeleteMonthly: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.MaxEnvNum = None
        self.CurrentEnvNum = None
        self.MaxFreeEnvNum = None
        self.CurrentFreeEnvNum = None
        self.MaxDeleteTotal = None
        self.CurrentDeleteTotal = None
        self.MaxDeleteMonthly = None
        self.CurrentDeleteMonthly = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MaxEnvNum = params.get("MaxEnvNum")
        self.CurrentEnvNum = params.get("CurrentEnvNum")
        self.MaxFreeEnvNum = params.get("MaxFreeEnvNum")
        self.CurrentFreeEnvNum = params.get("CurrentFreeEnvNum")
        self.MaxDeleteTotal = params.get("MaxDeleteTotal")
        self.CurrentDeleteTotal = params.get("CurrentDeleteTotal")
        self.MaxDeleteMonthly = params.get("MaxDeleteMonthly")
        self.CurrentDeleteMonthly = params.get("CurrentDeleteMonthly")
        self.RequestId = params.get("RequestId")


class DescribeEnvsRequest(AbstractModel):
    """DescribeEnvs請求參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 環境ID，如果傳了這個參數則只返回該環境的相關訊息
        :type EnvId: str
        :param IsVisible: 指定Channels欄位爲可見管道清單或不可見管道清單
如只想獲取管道A的環境 就填寫IsVisible= true,Channels = ["A"], 過濾管道A拉取其他管道環境時填寫IsVisible= false,Channels = ["A"]
        :type IsVisible: bool
        :param Channels: 管道清單，代表可見或不可見管道由IsVisible參數指定
        :type Channels: list of str
        """
        self.EnvId = None
        self.IsVisible = None
        self.Channels = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.IsVisible = params.get("IsVisible")
        self.Channels = params.get("Channels")


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


class DescribeQuotaDataRequest(AbstractModel):
    """DescribeQuotaData請求參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 環境ID
        :type EnvId: str
        :param MetricName: <li> 指标名: </li>
<li> StorageSizepkg: 當月儲存空間容量, 單位MB </li>
<li> StorageReadpkg: 當月儲存讀請求次數 </li>
<li> StorageWritepkg: 當月儲存寫請求次數 </li>
<li> StorageCdnOriginFluxpkg: 當月CDN回源流量, 單位位元 </li>
<li> StorageCdnOriginFluxpkgDay: 當日CDN回源流量, 單位位元 </li>
<li> StorageReadpkgDay: 當日儲存讀請求次數 </li>
<li> StorageWritepkgDay: 當日寫請求次數 </li>
<li> CDNFluxpkg: 當月CDN流量, 單位爲位元 </li>
<li> CDNFluxpkgDay: 當日CDN流量, 單位爲位元 </li>
<li> FunctionInvocationpkg: 當月雲函數調用次數 </li>
<li> FunctionGBspkg: 當月雲函數資源使用量, 單位Mb*Ms </li>
<li> FunctionFluxpkg: 當月雲函數流量, 單位千位元(KB) </li>
<li> FunctionInvocationpkgDay: 當日雲函數調用次數 </li>
<li> FunctionGBspkgDay: 當日雲函數資源使用量, 單位Mb*Ms </li>
<li> FunctionFluxpkgDay: 當日雲函數流量, 單位千位元(KB) </li>
<li> DbSizepkg: 當月資料庫容量大小, 單位MB </li>
<li> DbReadpkg: 當日資料庫讀請求數 </li>
<li> DbWritepkg: 當日資料庫寫請求數 </li>
<li> StaticFsFluxPkgDay: 當日靜态托管流量 </li>
<li> StaticFsFluxPkg: 當月靜态托管流量</li>
<li> StaticFsSizePkg: 當月靜态托管容量 </li>
        :type MetricName: str
        :param ResourceID: 資源ID, 目前僅對雲函數相關的指标(FunctionInvocationpkg, FunctionGBspkg, FunctionFluxpkg)有意義, 如果想查詢某個雲函數的指标則在ResourceId中傳入函數名; 如果只想查詢整個namespace的指标, 則留空或不傳.
        :type ResourceID: str
        """
        self.EnvId = None
        self.MetricName = None
        self.ResourceID = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.MetricName = params.get("MetricName")
        self.ResourceID = params.get("ResourceID")


class DescribeQuotaDataResponse(AbstractModel):
    """DescribeQuotaData返回參數結構體

    """

    def __init__(self):
        """
        :param MetricName: 指标名
        :type MetricName: str
        :param Value: 指标的值
        :type Value: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.MetricName = None
        self.Value = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        self.Value = params.get("Value")
        self.RequestId = params.get("RequestId")


class DestroyEnvRequest(AbstractModel):
    """DestroyEnv請求參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 環境Id
        :type EnvId: str
        :param IsForce: 針對預付費 删除隔離中的環境時要傳true 正常環境直接跳過隔離期删除
        :type IsForce: bool
        """
        self.EnvId = None
        self.IsForce = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.IsForce = params.get("IsForce")


class DestroyEnvResponse(AbstractModel):
    """DestroyEnv返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DestroyStaticStoreRequest(AbstractModel):
    """DestroyStaticStore請求參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 環境ID
        :type EnvId: str
        :param CdnDomain: cdn域名
        :type CdnDomain: str
        """
        self.EnvId = None
        self.CdnDomain = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.CdnDomain = params.get("CdnDomain")


class DestroyStaticStoreResponse(AbstractModel):
    """DestroyStaticStore返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 條件任務結果(succ/fail)
        :type Result: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class EndUserInfo(AbstractModel):
    """終端用戶訊息

    """

    def __init__(self):
        """
        :param UUId: 用戶唯一ID
        :type UUId: str
        :param WXOpenId:  ID
        :type WXOpenId: str
        :param  OpenId: qq ID
        :type  OpenId: str
        :param Phone: 手機号
        :type Phone: str
        :param Email: 電子信箱
        :type Email: str
        :param NickName: 昵稱
        :type NickName: str
        :param Gender: 性别
        :type Gender: str
        :param AvatarUrl: 頭像網址
        :type AvatarUrl: str
        :param UpdateTime: 更新時間
        :type UpdateTime: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param IsAnonymous: 是否爲匿名用戶
        :type IsAnonymous: bool
        :param IsDisabled: 是否禁用帳戶
        :type IsDisabled: bool
        """
        self.UUId = None
        self.WXOpenId = None
        self. OpenId = None
        self.Phone = None
        self.Email = None
        self.NickName = None
        self.Gender = None
        self.AvatarUrl = None
        self.UpdateTime = None
        self.CreateTime = None
        self.IsAnonymous = None
        self.IsDisabled = None


    def _deserialize(self, params):
        self.UUId = params.get("UUId")
        self.WXOpenId = params.get("WXOpenId")
        self. OpenId = params.get(" OpenId")
        self.Phone = params.get("Phone")
        self.Email = params.get("Email")
        self.NickName = params.get("NickName")
        self.Gender = params.get("Gender")
        self.AvatarUrl = params.get("AvatarUrl")
        self.UpdateTime = params.get("UpdateTime")
        self.CreateTime = params.get("CreateTime")
        self.IsAnonymous = params.get("IsAnonymous")
        self.IsDisabled = params.get("IsDisabled")


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
        :param LogServices: 雲日志服務清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type LogServices: list of LogServiceInfo
        :param StaticStorages: 靜态資源訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type StaticStorages: list of StaticStorageInfo
        :param IsAutoDegrade: 是否到期自動降爲免費版
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsAutoDegrade: bool
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
        self.LogServices = None
        self.StaticStorages = None
        self.IsAutoDegrade = None


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
        if params.get("LogServices") is not None:
            self.LogServices = []
            for item in params.get("LogServices"):
                obj = LogServiceInfo()
                obj._deserialize(item)
                self.LogServices.append(obj)
        if params.get("StaticStorages") is not None:
            self.StaticStorages = []
            for item in params.get("StaticStorages"):
                obj = StaticStorageInfo()
                obj._deserialize(item)
                self.StaticStorages.append(obj)
        self.IsAutoDegrade = params.get("IsAutoDegrade")


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


class LogServiceInfo(AbstractModel):
    """雲日志服務相關訊息

    """

    def __init__(self):
        """
        :param LogsetName: log名
        :type LogsetName: str
        :param LogsetId: log-id
        :type LogsetId: str
        :param TopicName: topic名
        :type TopicName: str
        :param TopicId: topic-id
        :type TopicId: str
        :param Region: cls日志所屬地域
        :type Region: str
        """
        self.LogsetName = None
        self.LogsetId = None
        self.TopicName = None
        self.TopicId = None
        self.Region = None


    def _deserialize(self, params):
        self.LogsetName = params.get("LogsetName")
        self.LogsetId = params.get("LogsetId")
        self.TopicName = params.get("TopicName")
        self.TopicId = params.get("TopicId")
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
        :param AclTag: 權限标簽。包含以下取值：
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


class PostpayEnvQuota(AbstractModel):
    """按量付費免費配額訊息

    """

    def __init__(self):
        """
        :param ResourceType: 資源類型
        :type ResourceType: str
        :param MetricName: 指标名
        :type MetricName: str
        :param Value: 配額值
        :type Value: int
        :param StartTime: 配額生效時間
爲空表示沒有時間限制
        :type StartTime: str
        :param EndTime: 配額失效時間
爲空表示沒有時間限制
        :type EndTime: str
        """
        self.ResourceType = None
        self.MetricName = None
        self.Value = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.MetricName = params.get("MetricName")
        self.Value = params.get("Value")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class ReinstateEnvRequest(AbstractModel):
    """ReinstateEnv請求參數結構體

    """

    def __init__(self):
        """
        :param EnvId: 環境ID
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")


class ReinstateEnvResponse(AbstractModel):
    """ReinstateEnv返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StaticStorageInfo(AbstractModel):
    """靜态CDN資源訊息

    """

    def __init__(self):
        """
        :param StaticDomain: 靜态CDN域名
注意：此欄位可能返回 null，表示取不到有效值。
        :type StaticDomain: str
        :param DefaultDirName: 靜态CDN預設文件夾，當前爲根目錄
注意：此欄位可能返回 null，表示取不到有效值。
        :type DefaultDirName: str
        :param Status: 資源狀态(process/online/offline/init)
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: str
        :param Region: cos所屬區域
注意：此欄位可能返回 null，表示取不到有效值。
        :type Region: str
        :param Bucket: bucket訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Bucket: str
        """
        self.StaticDomain = None
        self.DefaultDirName = None
        self.Status = None
        self.Region = None
        self.Bucket = None


    def _deserialize(self, params):
        self.StaticDomain = params.get("StaticDomain")
        self.DefaultDirName = params.get("DefaultDirName")
        self.Status = params.get("Status")
        self.Region = params.get("Region")
        self.Bucket = params.get("Bucket")


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