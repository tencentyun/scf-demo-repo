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


class AdInfo(AbstractModel):
    """廣告訊息

    """

    def __init__(self):
        """
        :param Spots: 插播廣告清單
        :type Spots: list of PluginInfo
        :param BoutiqueRecommands: 精品推薦廣告清單
        :type BoutiqueRecommands: list of PluginInfo
        :param FloatWindowses: 懸浮窗廣告清單
        :type FloatWindowses: list of PluginInfo
        :param Banners: banner廣告清單
        :type Banners: list of PluginInfo
        :param IntegralWalls: 積分牆廣告清單
        :type IntegralWalls: list of PluginInfo
        :param NotifyBars: 通知欄廣告清單
        :type NotifyBars: list of PluginInfo
        """
        self.Spots = None
        self.BoutiqueRecommands = None
        self.FloatWindowses = None
        self.Banners = None
        self.IntegralWalls = None
        self.NotifyBars = None


    def _deserialize(self, params):
        if params.get("Spots") is not None:
            self.Spots = []
            for item in params.get("Spots"):
                obj = PluginInfo()
                obj._deserialize(item)
                self.Spots.append(obj)
        if params.get("BoutiqueRecommands") is not None:
            self.BoutiqueRecommands = []
            for item in params.get("BoutiqueRecommands"):
                obj = PluginInfo()
                obj._deserialize(item)
                self.BoutiqueRecommands.append(obj)
        if params.get("FloatWindowses") is not None:
            self.FloatWindowses = []
            for item in params.get("FloatWindowses"):
                obj = PluginInfo()
                obj._deserialize(item)
                self.FloatWindowses.append(obj)
        if params.get("Banners") is not None:
            self.Banners = []
            for item in params.get("Banners"):
                obj = PluginInfo()
                obj._deserialize(item)
                self.Banners.append(obj)
        if params.get("IntegralWalls") is not None:
            self.IntegralWalls = []
            for item in params.get("IntegralWalls"):
                obj = PluginInfo()
                obj._deserialize(item)
                self.IntegralWalls.append(obj)
        if params.get("NotifyBars") is not None:
            self.NotifyBars = []
            for item in params.get("NotifyBars"):
                obj = PluginInfo()
                obj._deserialize(item)
                self.NotifyBars.append(obj)


class AppDetailInfo(AbstractModel):
    """app的詳細基礎訊息

    """

    def __init__(self):
        """
        :param AppName: app的名稱
        :type AppName: str
        :param AppPkgName: app的包名
        :type AppPkgName: str
        :param AppVersion: app的版本号
        :type AppVersion: str
        :param AppSize: app的大小
        :type AppSize: int
        :param AppMd5: app的md5
        :type AppMd5: str
        :param AppIconUrl: app的圖标url
        :type AppIconUrl: str
        :param FileName: app的文件名稱
        :type FileName: str
        """
        self.AppName = None
        self.AppPkgName = None
        self.AppVersion = None
        self.AppSize = None
        self.AppMd5 = None
        self.AppIconUrl = None
        self.FileName = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.AppPkgName = params.get("AppPkgName")
        self.AppVersion = params.get("AppVersion")
        self.AppSize = params.get("AppSize")
        self.AppMd5 = params.get("AppMd5")
        self.AppIconUrl = params.get("AppIconUrl")
        self.FileName = params.get("FileName")


class AppInfo(AbstractModel):
    """提交的app基本訊息

    """

    def __init__(self):
        """
        :param AppUrl: app的url，必須保證不用權限校驗就可以下載
        :type AppUrl: str
        :param AppMd5: app的md5，需要正确傳遞
        :type AppMd5: str
        :param AppSize: app的大小
        :type AppSize: int
        :param FileName: app的文件名
        :type FileName: str
        :param AppPkgName: app的包名，需要正确的傳遞此欄位
        :type AppPkgName: str
        :param AppVersion: app的版本号
        :type AppVersion: str
        :param AppIconUrl: app的圖标url
        :type AppIconUrl: str
        :param AppName: app的名稱
        :type AppName: str
        """
        self.AppUrl = None
        self.AppMd5 = None
        self.AppSize = None
        self.FileName = None
        self.AppPkgName = None
        self.AppVersion = None
        self.AppIconUrl = None
        self.AppName = None


    def _deserialize(self, params):
        self.AppUrl = params.get("AppUrl")
        self.AppMd5 = params.get("AppMd5")
        self.AppSize = params.get("AppSize")
        self.FileName = params.get("FileName")
        self.AppPkgName = params.get("AppPkgName")
        self.AppVersion = params.get("AppVersion")
        self.AppIconUrl = params.get("AppIconUrl")
        self.AppName = params.get("AppName")


class AppScanSet(AbstractModel):
    """掃描後app的訊息，包含基本訊息和掃描狀态訊息

    """

    def __init__(self):
        """
        :param ItemId: 任務唯一标識
        :type ItemId: str
        :param AppName: app的名稱
        :type AppName: str
        :param AppPkgName: app的包名
        :type AppPkgName: str
        :param AppVersion: app的版本号
        :type AppVersion: str
        :param AppMd5: app的md5
        :type AppMd5: str
        :param AppSize: app的大小
        :type AppSize: int
        :param ScanCode: 掃描結果返回碼
        :type ScanCode: int
        :param TaskStatus: 任務狀态: 1-已完成,2-處理中,3-處理出錯,4-處理超時
        :type TaskStatus: int
        :param TaskTime: 提交掃描時間
        :type TaskTime: int
        :param AppIconUrl: app的圖标url
        :type AppIconUrl: str
        :param AppSid: 标識唯一該app，主要用于删除
        :type AppSid: str
        :param SafeType: 安全類型:1-安全軟體，2-風險軟體，3病毒軟體
        :type SafeType: int
        :param VulCount: 漏洞個數
        :type VulCount: int
        """
        self.ItemId = None
        self.AppName = None
        self.AppPkgName = None
        self.AppVersion = None
        self.AppMd5 = None
        self.AppSize = None
        self.ScanCode = None
        self.TaskStatus = None
        self.TaskTime = None
        self.AppIconUrl = None
        self.AppSid = None
        self.SafeType = None
        self.VulCount = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")
        self.AppName = params.get("AppName")
        self.AppPkgName = params.get("AppPkgName")
        self.AppVersion = params.get("AppVersion")
        self.AppMd5 = params.get("AppMd5")
        self.AppSize = params.get("AppSize")
        self.ScanCode = params.get("ScanCode")
        self.TaskStatus = params.get("TaskStatus")
        self.TaskTime = params.get("TaskTime")
        self.AppIconUrl = params.get("AppIconUrl")
        self.AppSid = params.get("AppSid")
        self.SafeType = params.get("SafeType")
        self.VulCount = params.get("VulCount")


class AppSetInfo(AbstractModel):
    """加固後app的訊息，包含基本訊息和加固訊息

    """

    def __init__(self):
        """
        :param ItemId: 任務唯一标識
        :type ItemId: str
        :param AppName: app的名稱
        :type AppName: str
        :param AppPkgName: app的包名
        :type AppPkgName: str
        :param AppVersion: app的版本号
        :type AppVersion: str
        :param AppMd5: app的md5
        :type AppMd5: str
        :param AppSize: app的大小
        :type AppSize: int
        :param ServiceEdition: 加固服務版本
        :type ServiceEdition: str
        :param ShieldCode: 加固結果返回碼
        :type ShieldCode: int
        :param AppUrl: 加固後的APP下載網址
        :type AppUrl: str
        :param TaskStatus: 任務狀态: 1-已完成,2-處理中,3-處理出錯,4-處理超時
        :type TaskStatus: int
        :param ClientIp: 請求的用戶端ip
        :type ClientIp: str
        :param TaskTime: 提交加固時間
        :type TaskTime: int
        :param AppIconUrl: app的圖标url
        :type AppIconUrl: str
        :param ShieldMd5: 加固後app的md5
        :type ShieldMd5: str
        :param ShieldSize: 加固後app的大小
        :type ShieldSize: int
        """
        self.ItemId = None
        self.AppName = None
        self.AppPkgName = None
        self.AppVersion = None
        self.AppMd5 = None
        self.AppSize = None
        self.ServiceEdition = None
        self.ShieldCode = None
        self.AppUrl = None
        self.TaskStatus = None
        self.ClientIp = None
        self.TaskTime = None
        self.AppIconUrl = None
        self.ShieldMd5 = None
        self.ShieldSize = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")
        self.AppName = params.get("AppName")
        self.AppPkgName = params.get("AppPkgName")
        self.AppVersion = params.get("AppVersion")
        self.AppMd5 = params.get("AppMd5")
        self.AppSize = params.get("AppSize")
        self.ServiceEdition = params.get("ServiceEdition")
        self.ShieldCode = params.get("ShieldCode")
        self.AppUrl = params.get("AppUrl")
        self.TaskStatus = params.get("TaskStatus")
        self.ClientIp = params.get("ClientIp")
        self.TaskTime = params.get("TaskTime")
        self.AppIconUrl = params.get("AppIconUrl")
        self.ShieldMd5 = params.get("ShieldMd5")
        self.ShieldSize = params.get("ShieldSize")


class BindInfo(AbstractModel):
    """用戶綁定app的基本訊息

    """

    def __init__(self):
        """
        :param AppIconUrl: app的icon的url
        :type AppIconUrl: str
        :param AppName: app的名稱
        :type AppName: str
        :param AppPkgName: app的包名
        :type AppPkgName: str
        """
        self.AppIconUrl = None
        self.AppName = None
        self.AppPkgName = None


    def _deserialize(self, params):
        self.AppIconUrl = params.get("AppIconUrl")
        self.AppName = params.get("AppName")
        self.AppPkgName = params.get("AppPkgName")


class CreateBindInstanceRequest(AbstractModel):
    """CreateBindInstance請求參數結構體

    """

    def __init__(self):
        """
        :param ResourceId: 資源id，全局唯一
        :type ResourceId: str
        :param AppIconUrl: app的icon的url
        :type AppIconUrl: str
        :param AppName: app的名稱
        :type AppName: str
        :param AppPkgName: app的包名
        :type AppPkgName: str
        """
        self.ResourceId = None
        self.AppIconUrl = None
        self.AppName = None
        self.AppPkgName = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.AppIconUrl = params.get("AppIconUrl")
        self.AppName = params.get("AppName")
        self.AppPkgName = params.get("AppPkgName")


class CreateBindInstanceResponse(AbstractModel):
    """CreateBindInstance返回參數結構體

    """

    def __init__(self):
        """
        :param Progress: 任務狀态: 1-已完成,2-處理中,3-處理出錯,4-處理超時
        :type Progress: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Progress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Progress = params.get("Progress")
        self.RequestId = params.get("RequestId")


class CreateCosSecKeyInstanceRequest(AbstractModel):
    """CreateCosSecKeyInstance請求參數結構體

    """

    def __init__(self):
        """
        :param CosRegion: 地域訊息，例如 ：ap-guangzhou， ：ap-shanghai，預設爲 。
        :type CosRegion: str
        :param Duration: 金鑰有效時間，預設爲1小時。
        :type Duration: int
        """
        self.CosRegion = None
        self.Duration = None


    def _deserialize(self, params):
        self.CosRegion = params.get("CosRegion")
        self.Duration = params.get("Duration")


class CreateCosSecKeyInstanceResponse(AbstractModel):
    """CreateCosSecKeyInstance返回參數結構體

    """

    def __init__(self):
        """
        :param CosAppid: COS金鑰對應的AppId
        :type CosAppid: int
        :param CosBucket: COS金鑰對應的儲存桶名
        :type CosBucket: str
        :param CosRegion: 儲存桶對應的地域
        :type CosRegion: str
        :param ExpireTime: 金鑰過期時間
        :type ExpireTime: int
        :param CosId: 金鑰ID訊息
        :type CosId: str
        :param CosKey: 金鑰KEY訊息
        :type CosKey: str
        :param CosTocken: 金鑰TOCKEN訊息
        :type CosTocken: str
        :param CosPrefix: 金鑰可訪問的文件前綴人。例如：CosPrefix=test/123/666，則該金鑰只能操作test/123/666爲前綴的文件，例如test/123/666/1.txt
        :type CosPrefix: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CosAppid = None
        self.CosBucket = None
        self.CosRegion = None
        self.ExpireTime = None
        self.CosId = None
        self.CosKey = None
        self.CosTocken = None
        self.CosPrefix = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CosAppid = params.get("CosAppid")
        self.CosBucket = params.get("CosBucket")
        self.CosRegion = params.get("CosRegion")
        self.ExpireTime = params.get("ExpireTime")
        self.CosId = params.get("CosId")
        self.CosKey = params.get("CosKey")
        self.CosTocken = params.get("CosTocken")
        self.CosPrefix = params.get("CosPrefix")
        self.RequestId = params.get("RequestId")


class CreateResourceInstancesRequest(AbstractModel):
    """CreateResourceInstances請求參數結構體

    """

    def __init__(self):
        """
        :param Pid: 資源類型id。13624：加固專業版。
        :type Pid: int
        :param TimeUnit: 時間單位，取值爲d，m，y，分别表示天，月，年。
        :type TimeUnit: str
        :param TimeSpan: 時間數量。
        :type TimeSpan: int
        :param ResourceNum: 資源數量。
        :type ResourceNum: int
        """
        self.Pid = None
        self.TimeUnit = None
        self.TimeSpan = None
        self.ResourceNum = None


    def _deserialize(self, params):
        self.Pid = params.get("Pid")
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.ResourceNum = params.get("ResourceNum")


class CreateResourceInstancesResponse(AbstractModel):
    """CreateResourceInstances返回參數結構體

    """

    def __init__(self):
        """
        :param ResourceSet: 新創建的資源清單。
        :type ResourceSet: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ResourceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResourceSet = params.get("ResourceSet")
        self.RequestId = params.get("RequestId")


class CreateScanInstancesRequest(AbstractModel):
    """CreateScanInstances請求參數結構體

    """

    def __init__(self):
        """
        :param AppInfos: 待掃描的app訊息清單，一次最多提交20個
        :type AppInfos: list of AppInfo
        :param ScanInfo: 掃描訊息
        :type ScanInfo: :class:`taifucloudcloud.ms.v20180408.models.ScanInfo`
        """
        self.AppInfos = None
        self.ScanInfo = None


    def _deserialize(self, params):
        if params.get("AppInfos") is not None:
            self.AppInfos = []
            for item in params.get("AppInfos"):
                obj = AppInfo()
                obj._deserialize(item)
                self.AppInfos.append(obj)
        if params.get("ScanInfo") is not None:
            self.ScanInfo = ScanInfo()
            self.ScanInfo._deserialize(params.get("ScanInfo"))


class CreateScanInstancesResponse(AbstractModel):
    """CreateScanInstances返回參數結構體

    """

    def __init__(self):
        """
        :param ItemId: 任務唯一标識
        :type ItemId: str
        :param Progress: 任務狀态: 1-已完成,2-處理中,3-處理出錯,4-處理超時
        :type Progress: int
        :param AppMd5s: 提交成功的app的md5集合
        :type AppMd5s: list of str
        :param LimitCount: 剩餘可用次數
        :type LimitCount: int
        :param LimitTime: 到期時間
        :type LimitTime: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ItemId = None
        self.Progress = None
        self.AppMd5s = None
        self.LimitCount = None
        self.LimitTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")
        self.Progress = params.get("Progress")
        self.AppMd5s = params.get("AppMd5s")
        self.LimitCount = params.get("LimitCount")
        self.LimitTime = params.get("LimitTime")
        self.RequestId = params.get("RequestId")


class CreateShieldInstanceRequest(AbstractModel):
    """CreateShieldInstance請求參數結構體

    """

    def __init__(self):
        """
        :param AppInfo: 待加固的應用訊息
        :type AppInfo: :class:`taifucloudcloud.ms.v20180408.models.AppInfo`
        :param ServiceInfo: 加固服務訊息
        :type ServiceInfo: :class:`taifucloudcloud.ms.v20180408.models.ServiceInfo`
        """
        self.AppInfo = None
        self.ServiceInfo = None


    def _deserialize(self, params):
        if params.get("AppInfo") is not None:
            self.AppInfo = AppInfo()
            self.AppInfo._deserialize(params.get("AppInfo"))
        if params.get("ServiceInfo") is not None:
            self.ServiceInfo = ServiceInfo()
            self.ServiceInfo._deserialize(params.get("ServiceInfo"))


class CreateShieldInstanceResponse(AbstractModel):
    """CreateShieldInstance返回參數結構體

    """

    def __init__(self):
        """
        :param Progress: 任務狀态: 1-已完成,2-處理中,3-處理出錯,4-處理超時
        :type Progress: int
        :param ItemId: 任務唯一标識
        :type ItemId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Progress = None
        self.ItemId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Progress = params.get("Progress")
        self.ItemId = params.get("ItemId")
        self.RequestId = params.get("RequestId")


class CreateShieldPlanInstanceRequest(AbstractModel):
    """CreateShieldPlanInstance請求參數結構體

    """

    def __init__(self):
        """
        :param ResourceId: 資源id
        :type ResourceId: str
        :param PlanName: 策略名稱
        :type PlanName: str
        :param PlanInfo: 策略具體訊息
        :type PlanInfo: :class:`taifucloudcloud.ms.v20180408.models.PlanInfo`
        """
        self.ResourceId = None
        self.PlanName = None
        self.PlanInfo = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.PlanName = params.get("PlanName")
        if params.get("PlanInfo") is not None:
            self.PlanInfo = PlanInfo()
            self.PlanInfo._deserialize(params.get("PlanInfo"))


class CreateShieldPlanInstanceResponse(AbstractModel):
    """CreateShieldPlanInstance返回參數結構體

    """

    def __init__(self):
        """
        :param PlanId: 策略id
        :type PlanId: int
        :param Progress: 任務狀态: 1-已完成,2-處理中,3-處理出錯,4-處理超時
        :type Progress: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PlanId = None
        self.Progress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PlanId = params.get("PlanId")
        self.Progress = params.get("Progress")
        self.RequestId = params.get("RequestId")


class DeleteScanInstancesRequest(AbstractModel):
    """DeleteScanInstances請求參數結構體

    """

    def __init__(self):
        """
        :param AppSids: 删除一個或多個掃描的app，最大支援20個
        :type AppSids: list of str
        """
        self.AppSids = None


    def _deserialize(self, params):
        self.AppSids = params.get("AppSids")


class DeleteScanInstancesResponse(AbstractModel):
    """DeleteScanInstances返回參數結構體

    """

    def __init__(self):
        """
        :param Progress: 任務狀态: 1-已完成,2-處理中,3-處理出錯,4-處理超時
        :type Progress: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Progress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Progress = params.get("Progress")
        self.RequestId = params.get("RequestId")


class DeleteShieldInstancesRequest(AbstractModel):
    """DeleteShieldInstances請求參數結構體

    """

    def __init__(self):
        """
        :param ItemIds: 任務唯一标識ItemId的清單
        :type ItemIds: list of str
        """
        self.ItemIds = None


    def _deserialize(self, params):
        self.ItemIds = params.get("ItemIds")


class DeleteShieldInstancesResponse(AbstractModel):
    """DeleteShieldInstances返回參數結構體

    """

    def __init__(self):
        """
        :param Progress: 任務狀态: 1-已完成,2-處理中,3-處理出錯,4-處理超時
        :type Progress: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Progress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Progress = params.get("Progress")
        self.RequestId = params.get("RequestId")


class DescribeResourceInstancesRequest(AbstractModel):
    """DescribeResourceInstances請求參數結構體

    """

    def __init__(self):
        """
        :param Pids: 資源類别id數組，13624：加固專業版，12750：企業版。空數組表示返回全部資源。
        :type Pids: list of int non-negative
        :param Filters: 支援通過資源id，pid進行查詢
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 數量限制，預設爲20，最大值爲100。
        :type Limit: int
        :param OrderField: 按某個欄位排序，目前支援CreateTime、ExpireTime其中的一個排序。
        :type OrderField: str
        :param OrderDirection: 升序（asc）還是降序（desc），預設：desc。
        :type OrderDirection: str
        """
        self.Pids = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.OrderDirection = None


    def _deserialize(self, params):
        self.Pids = params.get("Pids")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderField = params.get("OrderField")
        self.OrderDirection = params.get("OrderDirection")


class DescribeResourceInstancesResponse(AbstractModel):
    """DescribeResourceInstances返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合要求的資源數量
        :type TotalCount: int
        :param ResourceSet: 符合要求的資源數組
        :type ResourceSet: list of ResourceInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ResourceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ResourceSet") is not None:
            self.ResourceSet = []
            for item in params.get("ResourceSet"):
                obj = ResourceInfo()
                obj._deserialize(item)
                self.ResourceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeScanInstancesRequest(AbstractModel):
    """DescribeScanInstances請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 支援通過app名稱，app包名進行篩選
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 數量限制，預設爲20，最大值爲100。
        :type Limit: int
        :param ItemIds: 可以提供ItemId數組來查詢一個或者多個結果。注意不可以同時指定ItemIds和Filters。
        :type ItemIds: list of str
        :param OrderField: 按某個欄位排序，目前僅支援TaskTime排序。
        :type OrderField: str
        :param OrderDirection: 升序（asc）還是降序（desc），預設：desc。
        :type OrderDirection: str
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.ItemIds = None
        self.OrderField = None
        self.OrderDirection = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ItemIds = params.get("ItemIds")
        self.OrderField = params.get("OrderField")
        self.OrderDirection = params.get("OrderDirection")


class DescribeScanInstancesResponse(AbstractModel):
    """DescribeScanInstances返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合要求的app數量
        :type TotalCount: int
        :param ScanSet: 一個關于app詳細訊息的結構體，主要包括app的基本訊息和掃描狀态訊息。
        :type ScanSet: list of AppScanSet
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ScanSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ScanSet") is not None:
            self.ScanSet = []
            for item in params.get("ScanSet"):
                obj = AppScanSet()
                obj._deserialize(item)
                self.ScanSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeScanResultsRequest(AbstractModel):
    """DescribeScanResults請求參數結構體

    """

    def __init__(self):
        """
        :param ItemId: 任務唯一标識
        :type ItemId: str
        :param AppMd5s: 批次查詢一個或者多個app的掃描結果，如果不傳表示查詢該任務下所提交的所有app
        :type AppMd5s: list of str
        """
        self.ItemId = None
        self.AppMd5s = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")
        self.AppMd5s = params.get("AppMd5s")


class DescribeScanResultsResponse(AbstractModel):
    """DescribeScanResults返回參數結構體

    """

    def __init__(self):
        """
        :param ScanSet: 批次掃描的app結果集
        :type ScanSet: list of ScanSetInfo
        :param TotalCount: 批次掃描結果的個數
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ScanSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ScanSet") is not None:
            self.ScanSet = []
            for item in params.get("ScanSet"):
                obj = ScanSetInfo()
                obj._deserialize(item)
                self.ScanSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeShieldInstancesRequest(AbstractModel):
    """DescribeShieldInstances請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 支援通過app名稱，app包名，加固的服務版本，提交的管道進行篩選。
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Limit: 數量限制，預設爲20，最大值爲100。
        :type Limit: int
        :param ItemIds: 可以提供ItemId數組來查詢一個或者多個結果。注意不可以同時指定ItemIds和Filters。
        :type ItemIds: list of str
        :param OrderField: 按某個欄位排序，目前僅支援TaskTime排序。
        :type OrderField: str
        :param OrderDirection: 升序（asc）還是降序（desc），預設：desc。
        :type OrderDirection: str
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.ItemIds = None
        self.OrderField = None
        self.OrderDirection = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ItemIds = params.get("ItemIds")
        self.OrderField = params.get("OrderField")
        self.OrderDirection = params.get("OrderDirection")


class DescribeShieldInstancesResponse(AbstractModel):
    """DescribeShieldInstances返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合要求的app數量
        :type TotalCount: int
        :param AppSet: 一個關于app詳細訊息的結構體，主要包括app的基本訊息和加固訊息。
        :type AppSet: list of AppSetInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AppSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AppSet") is not None:
            self.AppSet = []
            for item in params.get("AppSet"):
                obj = AppSetInfo()
                obj._deserialize(item)
                self.AppSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeShieldPlanInstanceRequest(AbstractModel):
    """DescribeShieldPlanInstance請求參數結構體

    """

    def __init__(self):
        """
        :param ResourceId: 資源id
        :type ResourceId: str
        :param Pid: 服務類别id
        :type Pid: int
        """
        self.ResourceId = None
        self.Pid = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.Pid = params.get("Pid")


class DescribeShieldPlanInstanceResponse(AbstractModel):
    """DescribeShieldPlanInstance返回參數結構體

    """

    def __init__(self):
        """
        :param BindInfo: 綁定資源訊息
        :type BindInfo: :class:`taifucloudcloud.ms.v20180408.models.BindInfo`
        :param ShieldPlanInfo: 加固策略訊息
        :type ShieldPlanInfo: :class:`taifucloudcloud.ms.v20180408.models.ShieldPlanInfo`
        :param ResourceServiceInfo: 加固資源訊息
        :type ResourceServiceInfo: :class:`taifucloudcloud.ms.v20180408.models.ResourceServiceInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.BindInfo = None
        self.ShieldPlanInfo = None
        self.ResourceServiceInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BindInfo") is not None:
            self.BindInfo = BindInfo()
            self.BindInfo._deserialize(params.get("BindInfo"))
        if params.get("ShieldPlanInfo") is not None:
            self.ShieldPlanInfo = ShieldPlanInfo()
            self.ShieldPlanInfo._deserialize(params.get("ShieldPlanInfo"))
        if params.get("ResourceServiceInfo") is not None:
            self.ResourceServiceInfo = ResourceServiceInfo()
            self.ResourceServiceInfo._deserialize(params.get("ResourceServiceInfo"))
        self.RequestId = params.get("RequestId")


class DescribeShieldResultRequest(AbstractModel):
    """DescribeShieldResult請求參數結構體

    """

    def __init__(self):
        """
        :param ItemId: 任務唯一标識
        :type ItemId: str
        """
        self.ItemId = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")


class DescribeShieldResultResponse(AbstractModel):
    """DescribeShieldResult返回參數結構體

    """

    def __init__(self):
        """
        :param TaskStatus: 任務狀态: 0-請返回,1-已完成,2-處理中,3-處理出錯,4-處理超時
        :type TaskStatus: int
        :param AppDetailInfo: app加固前的詳細訊息
        :type AppDetailInfo: :class:`taifucloudcloud.ms.v20180408.models.AppDetailInfo`
        :param ShieldInfo: app加固後的詳細訊息
        :type ShieldInfo: :class:`taifucloudcloud.ms.v20180408.models.ShieldInfo`
        :param StatusDesc: 狀态描述
        :type StatusDesc: str
        :param StatusRef: 狀态指引
        :type StatusRef: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskStatus = None
        self.AppDetailInfo = None
        self.ShieldInfo = None
        self.StatusDesc = None
        self.StatusRef = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskStatus = params.get("TaskStatus")
        if params.get("AppDetailInfo") is not None:
            self.AppDetailInfo = AppDetailInfo()
            self.AppDetailInfo._deserialize(params.get("AppDetailInfo"))
        if params.get("ShieldInfo") is not None:
            self.ShieldInfo = ShieldInfo()
            self.ShieldInfo._deserialize(params.get("ShieldInfo"))
        self.StatusDesc = params.get("StatusDesc")
        self.StatusRef = params.get("StatusRef")
        self.RequestId = params.get("RequestId")


class DescribeUserBaseInfoInstanceRequest(AbstractModel):
    """DescribeUserBaseInfoInstance請求參數結構體

    """


class DescribeUserBaseInfoInstanceResponse(AbstractModel):
    """DescribeUserBaseInfoInstance返回參數結構體

    """

    def __init__(self):
        """
        :param UserUin: 用戶uin訊息
        :type UserUin: int
        :param UserAppid: 用戶APPID訊息
        :type UserAppid: int
        :param TimeStamp: 系統時間戳
        :type TimeStamp: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.UserUin = None
        self.UserAppid = None
        self.TimeStamp = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserUin = params.get("UserUin")
        self.UserAppid = params.get("UserAppid")
        self.TimeStamp = params.get("TimeStamp")
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """篩選數據結構

    """

    def __init__(self):
        """
        :param Name: 需要過濾的欄位
        :type Name: str
        :param Value: 需要過濾欄位的值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class PlanDetailInfo(AbstractModel):
    """加固策略具體訊息

    """

    def __init__(self):
        """
        :param IsDefault: 預設策略，1爲預設，0爲非預設
        :type IsDefault: int
        :param PlanId: 策略id
        :type PlanId: int
        :param PlanName: 策略名稱
        :type PlanName: str
        :param PlanInfo: 策略訊息
        :type PlanInfo: :class:`taifucloudcloud.ms.v20180408.models.PlanInfo`
        """
        self.IsDefault = None
        self.PlanId = None
        self.PlanName = None
        self.PlanInfo = None


    def _deserialize(self, params):
        self.IsDefault = params.get("IsDefault")
        self.PlanId = params.get("PlanId")
        self.PlanName = params.get("PlanName")
        if params.get("PlanInfo") is not None:
            self.PlanInfo = PlanInfo()
            self.PlanInfo._deserialize(params.get("PlanInfo"))


class PlanInfo(AbstractModel):
    """加固策略訊息

    """

    def __init__(self):
        """
        :param ApkSizeOpt: apk大小優化，0關閉，1開啓
        :type ApkSizeOpt: int
        :param Dex: Dex加固，0關閉，1開啓
        :type Dex: int
        :param So: So加固，0關閉，1開啓
        :type So: int
        :param Bugly: 數據收集，0關閉，1開啓
        :type Bugly: int
        :param AntiRepack: 防止重打包，0關閉，1開啓
        :type AntiRepack: int
        :param SeperateDex: Dex分離，0關閉，1開啓
        :type SeperateDex: int
        :param Db: 内存保護，0關閉，1開啓
        :type Db: int
        :param DexSig: Dex簽名校驗，0關閉，1開啓
        :type DexSig: int
        :param SoInfo: So文件訊息
        :type SoInfo: :class:`taifucloudcloud.ms.v20180408.models.SoInfo`
        :param AntiVMP: vmp，0關閉，1開啓
        :type AntiVMP: int
        :param SoType: 保護so的強度，
        :type SoType: list of str
        :param AntiLogLeak: 防日志洩漏，0關閉，1開啓
        :type AntiLogLeak: int
        :param AntiQemuRoot: root檢測，0關閉，1開啓
        :type AntiQemuRoot: int
        :param AntiAssets: 資源防篡改，0關閉，1開啓
        :type AntiAssets: int
        :param AntiScreenshot: 防止截屏，0關閉，1開啓
        :type AntiScreenshot: int
        :param AntiSSL: SSL證書防竊取，0關閉，1開啓
        :type AntiSSL: int
        """
        self.ApkSizeOpt = None
        self.Dex = None
        self.So = None
        self.Bugly = None
        self.AntiRepack = None
        self.SeperateDex = None
        self.Db = None
        self.DexSig = None
        self.SoInfo = None
        self.AntiVMP = None
        self.SoType = None
        self.AntiLogLeak = None
        self.AntiQemuRoot = None
        self.AntiAssets = None
        self.AntiScreenshot = None
        self.AntiSSL = None


    def _deserialize(self, params):
        self.ApkSizeOpt = params.get("ApkSizeOpt")
        self.Dex = params.get("Dex")
        self.So = params.get("So")
        self.Bugly = params.get("Bugly")
        self.AntiRepack = params.get("AntiRepack")
        self.SeperateDex = params.get("SeperateDex")
        self.Db = params.get("Db")
        self.DexSig = params.get("DexSig")
        if params.get("SoInfo") is not None:
            self.SoInfo = SoInfo()
            self.SoInfo._deserialize(params.get("SoInfo"))
        self.AntiVMP = params.get("AntiVMP")
        self.SoType = params.get("SoType")
        self.AntiLogLeak = params.get("AntiLogLeak")
        self.AntiQemuRoot = params.get("AntiQemuRoot")
        self.AntiAssets = params.get("AntiAssets")
        self.AntiScreenshot = params.get("AntiScreenshot")
        self.AntiSSL = params.get("AntiSSL")


class PluginInfo(AbstractModel):
    """插件訊息

    """

    def __init__(self):
        """
        :param PluginType: 插件類型，分别爲 1-通知欄廣告，2-積分牆廣告，3-banner廣告，4- 懸浮窗圖标廣告，5-精品推薦清單廣告, 6-插播廣告
        :type PluginType: int
        :param PluginName: 插件名稱
        :type PluginName: str
        :param PluginDesc: 插件描述
        :type PluginDesc: str
        """
        self.PluginType = None
        self.PluginName = None
        self.PluginDesc = None


    def _deserialize(self, params):
        self.PluginType = params.get("PluginType")
        self.PluginName = params.get("PluginName")
        self.PluginDesc = params.get("PluginDesc")


class ResourceInfo(AbstractModel):
    """拉取某個用戶的所有資源訊息

    """

    def __init__(self):
        """
        :param ResourceId: 用戶購買的資源id，全局唯一
        :type ResourceId: str
        :param Pid: 資源的pid，MTP加固-12767，應用加固-12750 MTP反作弊-12766 原始碼混淆-12736
        :type Pid: int
        :param CreateTime: 購買時間戳
        :type CreateTime: int
        :param ExpireTime: 到期時間戳
        :type ExpireTime: int
        :param IsBind: 0-未綁定，1-已綁定
        :type IsBind: int
        :param BindInfo: 用戶綁定app的基本訊息
        :type BindInfo: :class:`taifucloudcloud.ms.v20180408.models.BindInfo`
        :param ResourceName: 資源名稱，如應用加固，漏洞掃描
        :type ResourceName: str
        """
        self.ResourceId = None
        self.Pid = None
        self.CreateTime = None
        self.ExpireTime = None
        self.IsBind = None
        self.BindInfo = None
        self.ResourceName = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.Pid = params.get("Pid")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.IsBind = params.get("IsBind")
        if params.get("BindInfo") is not None:
            self.BindInfo = BindInfo()
            self.BindInfo._deserialize(params.get("BindInfo"))
        self.ResourceName = params.get("ResourceName")


class ResourceServiceInfo(AbstractModel):
    """資源服務訊息

    """

    def __init__(self):
        """
        :param CreateTime: 創建時間戳
        :type CreateTime: int
        :param ExpireTime: 到期時間戳
        :type ExpireTime: int
        :param ResourceName: 資源名稱，如應用加固，源碼混淆
        :type ResourceName: str
        """
        self.CreateTime = None
        self.ExpireTime = None
        self.ResourceName = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.ResourceName = params.get("ResourceName")


class ScanInfo(AbstractModel):
    """需要掃描的應用的服務訊息

    """

    def __init__(self):
        """
        :param CallbackUrl: 任務處理完成後的反向通知回調網址,批次提交app每掃描完成一個會通知一次,通知爲POST請求，post訊息{ItemId:
        :type CallbackUrl: str
        :param ScanTypes: VULSCAN-漏洞掃描訊息，VIRUSSCAN-返回病毒掃描訊息， ADSCAN-廣告掃描訊息，PLUGINSCAN-插件掃描訊息，PERMISSION-系統權限訊息，SENSITIVE-敏感詞訊息，可以自由組合
        :type ScanTypes: list of str
        """
        self.CallbackUrl = None
        self.ScanTypes = None


    def _deserialize(self, params):
        self.CallbackUrl = params.get("CallbackUrl")
        self.ScanTypes = params.get("ScanTypes")


class ScanPermissionInfo(AbstractModel):
    """安全掃描系統權限訊息

    """

    def __init__(self):
        """
        :param Permission: 系統權限
        :type Permission: str
        """
        self.Permission = None


    def _deserialize(self, params):
        self.Permission = params.get("Permission")


class ScanPermissionList(AbstractModel):
    """安全掃描系統權限訊息

    """

    def __init__(self):
        """
        :param PermissionList: 系統權限訊息
        :type PermissionList: list of ScanPermissionInfo
        """
        self.PermissionList = None


    def _deserialize(self, params):
        if params.get("PermissionList") is not None:
            self.PermissionList = []
            for item in params.get("PermissionList"):
                obj = ScanPermissionInfo()
                obj._deserialize(item)
                self.PermissionList.append(obj)


class ScanSensitiveInfo(AbstractModel):
    """安全掃描敏感詞

    """

    def __init__(self):
        """
        :param WordList: 敏感詞
        :type WordList: list of str
        :param FilePath: 敏感詞對應的文件訊息
        :type FilePath: str
        :param FileSha: 文件sha1值
        :type FileSha: str
        """
        self.WordList = None
        self.FilePath = None
        self.FileSha = None


    def _deserialize(self, params):
        self.WordList = params.get("WordList")
        self.FilePath = params.get("FilePath")
        self.FileSha = params.get("FileSha")


class ScanSensitiveList(AbstractModel):
    """安全掃描敏感詞清單

    """

    def __init__(self):
        """
        :param SensitiveList: 敏感詞清單
        :type SensitiveList: list of ScanSensitiveInfo
        """
        self.SensitiveList = None


    def _deserialize(self, params):
        if params.get("SensitiveList") is not None:
            self.SensitiveList = []
            for item in params.get("SensitiveList"):
                obj = ScanSensitiveInfo()
                obj._deserialize(item)
                self.SensitiveList.append(obj)


class ScanSetInfo(AbstractModel):
    """app掃描結果集

    """

    def __init__(self):
        """
        :param TaskStatus: 任務狀态: 1-已完成,2-處理中,3-處理出錯,4-處理超時
        :type TaskStatus: int
        :param AppDetailInfo: app訊息
        :type AppDetailInfo: :class:`taifucloudcloud.ms.v20180408.models.AppDetailInfo`
        :param VirusInfo: 病毒訊息
        :type VirusInfo: :class:`taifucloudcloud.ms.v20180408.models.VirusInfo`
        :param VulInfo: 漏洞訊息
        :type VulInfo: :class:`taifucloudcloud.ms.v20180408.models.VulInfo`
        :param AdInfo: 廣告插件訊息
        :type AdInfo: :class:`taifucloudcloud.ms.v20180408.models.AdInfo`
        :param TaskTime: 提交掃描的時間
        :type TaskTime: int
        :param StatusCode: 狀态碼，成功返回0，失敗返回錯誤碼
        :type StatusCode: int
        :param StatusDesc: 狀态描述
        :type StatusDesc: str
        :param StatusRef: 狀态操作指引
        :type StatusRef: str
        :param PermissionInfo: 系統權限訊息
        :type PermissionInfo: :class:`taifucloudcloud.ms.v20180408.models.ScanPermissionList`
        :param SensitiveInfo: 敏感詞清單
        :type SensitiveInfo: :class:`taifucloudcloud.ms.v20180408.models.ScanSensitiveList`
        """
        self.TaskStatus = None
        self.AppDetailInfo = None
        self.VirusInfo = None
        self.VulInfo = None
        self.AdInfo = None
        self.TaskTime = None
        self.StatusCode = None
        self.StatusDesc = None
        self.StatusRef = None
        self.PermissionInfo = None
        self.SensitiveInfo = None


    def _deserialize(self, params):
        self.TaskStatus = params.get("TaskStatus")
        if params.get("AppDetailInfo") is not None:
            self.AppDetailInfo = AppDetailInfo()
            self.AppDetailInfo._deserialize(params.get("AppDetailInfo"))
        if params.get("VirusInfo") is not None:
            self.VirusInfo = VirusInfo()
            self.VirusInfo._deserialize(params.get("VirusInfo"))
        if params.get("VulInfo") is not None:
            self.VulInfo = VulInfo()
            self.VulInfo._deserialize(params.get("VulInfo"))
        if params.get("AdInfo") is not None:
            self.AdInfo = AdInfo()
            self.AdInfo._deserialize(params.get("AdInfo"))
        self.TaskTime = params.get("TaskTime")
        self.StatusCode = params.get("StatusCode")
        self.StatusDesc = params.get("StatusDesc")
        self.StatusRef = params.get("StatusRef")
        if params.get("PermissionInfo") is not None:
            self.PermissionInfo = ScanPermissionList()
            self.PermissionInfo._deserialize(params.get("PermissionInfo"))
        if params.get("SensitiveInfo") is not None:
            self.SensitiveInfo = ScanSensitiveList()
            self.SensitiveInfo._deserialize(params.get("SensitiveInfo"))


class ServiceInfo(AbstractModel):
    """提交app加固的服務訊息

    """

    def __init__(self):
        """
        :param ServiceEdition: 服務版本，基礎版basic，專業版professional，企業版enterprise。
        :type ServiceEdition: str
        :param CallbackUrl: 任務處理完成後的反向通知回調網址，如果不需要通知請傳遞空字串。通知爲POST請求，post包體數據範例{"Response":{"ItemId":"4cdad8fb86f036b06bccb3f58971c306","ShieldCode":0,"ShieldMd5":"78701576793c4a5f04e1c9660de0aa0b","ShieldSize":11997354,"TaskStatus":1,"TaskTime":1539148141}}，調用方需要返回如下訊息，{"Result":"ok","Reason":"xxxxx"}，如果Result欄位值不等于ok會繼續回調。
        :type CallbackUrl: str
        :param SubmitSource: 提交來源 YYB-應用寶 RDM-rdm MC-控制台 MAC_TOOL-mac工具 WIN_TOOL-window工具。
        :type SubmitSource: str
        :param PlanId: 加固策略編号，如果不傳則使用系統預設加固策略。如果指定的plan不存在會返回錯誤。
        :type PlanId: int
        """
        self.ServiceEdition = None
        self.CallbackUrl = None
        self.SubmitSource = None
        self.PlanId = None


    def _deserialize(self, params):
        self.ServiceEdition = params.get("ServiceEdition")
        self.CallbackUrl = params.get("CallbackUrl")
        self.SubmitSource = params.get("SubmitSource")
        self.PlanId = params.get("PlanId")


class ShieldInfo(AbstractModel):
    """加固後app的訊息

    """

    def __init__(self):
        """
        :param ShieldCode: 加固結果的返回碼
        :type ShieldCode: int
        :param ShieldSize: 加固後app的大小
        :type ShieldSize: int
        :param ShieldMd5: 加固後app的md5
        :type ShieldMd5: str
        :param AppUrl: 加固後的APP下載網址，該網址有效期爲20分鍾，請及時下載
        :type AppUrl: str
        :param TaskTime: 加固的提交時間
        :type TaskTime: int
        :param ItemId: 任務唯一标識
        :type ItemId: str
        :param ServiceEdition: 加固版本，basic基礎版，professional專業版，enterprise企業版
        :type ServiceEdition: str
        """
        self.ShieldCode = None
        self.ShieldSize = None
        self.ShieldMd5 = None
        self.AppUrl = None
        self.TaskTime = None
        self.ItemId = None
        self.ServiceEdition = None


    def _deserialize(self, params):
        self.ShieldCode = params.get("ShieldCode")
        self.ShieldSize = params.get("ShieldSize")
        self.ShieldMd5 = params.get("ShieldMd5")
        self.AppUrl = params.get("AppUrl")
        self.TaskTime = params.get("TaskTime")
        self.ItemId = params.get("ItemId")
        self.ServiceEdition = params.get("ServiceEdition")


class ShieldPlanInfo(AbstractModel):
    """加固策略訊息

    """

    def __init__(self):
        """
        :param TotalCount: 加固策略數量
        :type TotalCount: int
        :param PlanSet: 加固策略具體訊息數組
        :type PlanSet: list of PlanDetailInfo
        """
        self.TotalCount = None
        self.PlanSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PlanSet") is not None:
            self.PlanSet = []
            for item in params.get("PlanSet"):
                obj = PlanDetailInfo()
                obj._deserialize(item)
                self.PlanSet.append(obj)


class SoInfo(AbstractModel):
    """so加固訊息

    """

    def __init__(self):
        """
        :param SoFileNames: so文件清單
        :type SoFileNames: list of str
        """
        self.SoFileNames = None


    def _deserialize(self, params):
        self.SoFileNames = params.get("SoFileNames")


class VirusInfo(AbstractModel):
    """病毒訊息

    """

    def __init__(self):
        """
        :param SafeType: 軟體安全類型，分别爲0-未知、 1-安全軟體、2-風險軟體、3-病毒軟體
        :type SafeType: int
        :param VirusName: 病毒名稱， utf8編碼，非病毒時值爲空
        :type VirusName: str
        :param VirusDesc: 病毒描述，utf8編碼，非病毒時值爲空
        :type VirusDesc: str
        """
        self.SafeType = None
        self.VirusName = None
        self.VirusDesc = None


    def _deserialize(self, params):
        self.SafeType = params.get("SafeType")
        self.VirusName = params.get("VirusName")
        self.VirusDesc = params.get("VirusDesc")


class VulInfo(AbstractModel):
    """漏洞訊息

    """

    def __init__(self):
        """
        :param VulList: 漏洞清單
        :type VulList: list of VulList
        :param VulFileScore: 漏洞文件評分
        :type VulFileScore: int
        """
        self.VulList = None
        self.VulFileScore = None


    def _deserialize(self, params):
        if params.get("VulList") is not None:
            self.VulList = []
            for item in params.get("VulList"):
                obj = VulList()
                obj._deserialize(item)
                self.VulList.append(obj)
        self.VulFileScore = params.get("VulFileScore")


class VulList(AbstractModel):
    """漏洞訊息

    """

    def __init__(self):
        """
        :param VulId: 漏洞id
        :type VulId: str
        :param VulName: 漏洞名稱
        :type VulName: str
        :param VulCode: 漏洞代碼
        :type VulCode: str
        :param VulDesc: 漏洞描述
        :type VulDesc: str
        :param VulSolution: 漏洞解決方案
        :type VulSolution: str
        :param VulSrcType: 漏洞來源類别，0預設自身，1第三方插件
        :type VulSrcType: int
        :param VulFilepath: 漏洞位置
        :type VulFilepath: str
        :param RiskLevel: 風險級别：1 低風險 ；2中等風險；3 高風險
        :type RiskLevel: int
        """
        self.VulId = None
        self.VulName = None
        self.VulCode = None
        self.VulDesc = None
        self.VulSolution = None
        self.VulSrcType = None
        self.VulFilepath = None
        self.RiskLevel = None


    def _deserialize(self, params):
        self.VulId = params.get("VulId")
        self.VulName = params.get("VulName")
        self.VulCode = params.get("VulCode")
        self.VulDesc = params.get("VulDesc")
        self.VulSolution = params.get("VulSolution")
        self.VulSrcType = params.get("VulSrcType")
        self.VulFilepath = params.get("VulFilepath")
        self.RiskLevel = params.get("RiskLevel")