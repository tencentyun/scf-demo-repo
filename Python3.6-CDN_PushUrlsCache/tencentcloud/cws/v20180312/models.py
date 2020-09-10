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


class CreateMonitorsRequest(AbstractModel):
    """CreateMonitors請求參數結構體

    """

    def __init__(self):
        """
        :param Urls: 站點的url清單
        :type Urls: list of str
        :param Name: 任務名稱
        :type Name: str
        :param ScannerType: 掃描模式，normal-正常掃描；deep-深度掃描
        :type ScannerType: str
        :param Crontab: 掃描週期，單位小時，每X小時執行一次
        :type Crontab: int
        :param RateLimit: 掃描速率限制，每秒發送X個HTTP請求
        :type RateLimit: int
        :param FirstScanStartTime: 首次掃描開始時間
        :type FirstScanStartTime: str
        """
        self.Urls = None
        self.Name = None
        self.ScannerType = None
        self.Crontab = None
        self.RateLimit = None
        self.FirstScanStartTime = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")
        self.Name = params.get("Name")
        self.ScannerType = params.get("ScannerType")
        self.Crontab = params.get("Crontab")
        self.RateLimit = params.get("RateLimit")
        self.FirstScanStartTime = params.get("FirstScanStartTime")


class CreateMonitorsResponse(AbstractModel):
    """CreateMonitors返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSitesRequest(AbstractModel):
    """CreateSites請求參數結構體

    """

    def __init__(self):
        """
        :param Urls: 站點的url清單
        :type Urls: list of str
        :param UserAgent: 訪問網站的用戶端标識
        :type UserAgent: str
        """
        self.Urls = None
        self.UserAgent = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")
        self.UserAgent = params.get("UserAgent")


class CreateSitesResponse(AbstractModel):
    """CreateSites返回參數結構體

    """

    def __init__(self):
        """
        :param Number: 新增站點數。
        :type Number: int
        :param Sites: 站點數組
        :type Sites: list of MiniSite
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Number = None
        self.Sites = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Number = params.get("Number")
        if params.get("Sites") is not None:
            self.Sites = []
            for item in params.get("Sites"):
                obj = MiniSite()
                obj._deserialize(item)
                self.Sites.append(obj)
        self.RequestId = params.get("RequestId")


class CreateSitesScansRequest(AbstractModel):
    """CreateSitesScans請求參數結構體

    """

    def __init__(self):
        """
        :param SiteIds: 站點的ID清單
        :type SiteIds: list of int non-negative
        :param ScannerType: 掃描模式，normal-正常掃描；deep-深度掃描
        :type ScannerType: str
        :param RateLimit: 掃描速率限制，每秒發送X個HTTP請求
        :type RateLimit: int
        """
        self.SiteIds = None
        self.ScannerType = None
        self.RateLimit = None


    def _deserialize(self, params):
        self.SiteIds = params.get("SiteIds")
        self.ScannerType = params.get("ScannerType")
        self.RateLimit = params.get("RateLimit")


class CreateSitesScansResponse(AbstractModel):
    """CreateSitesScans返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateVulsMisinformationRequest(AbstractModel):
    """CreateVulsMisinformation請求參數結構體

    """

    def __init__(self):
        """
        :param VulIds: 漏洞ID清單
        :type VulIds: list of int non-negative
        """
        self.VulIds = None


    def _deserialize(self, params):
        self.VulIds = params.get("VulIds")


class CreateVulsMisinformationResponse(AbstractModel):
    """CreateVulsMisinformation返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateVulsReportRequest(AbstractModel):
    """CreateVulsReport請求參數結構體

    """

    def __init__(self):
        """
        :param SiteId: 站點ID
        :type SiteId: int
        :param MonitorId: 監控任務ID
        :type MonitorId: int
        """
        self.SiteId = None
        self.MonitorId = None


    def _deserialize(self, params):
        self.SiteId = params.get("SiteId")
        self.MonitorId = params.get("MonitorId")


class CreateVulsReportResponse(AbstractModel):
    """CreateVulsReport返回參數結構體

    """

    def __init__(self):
        """
        :param ReportFileUrl: 報告下載網址
        :type ReportFileUrl: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ReportFileUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReportFileUrl = params.get("ReportFileUrl")
        self.RequestId = params.get("RequestId")


class DeleteMonitorsRequest(AbstractModel):
    """DeleteMonitors請求參數結構體

    """

    def __init__(self):
        """
        :param MonitorIds: 監控任務ID清單
        :type MonitorIds: list of int non-negative
        """
        self.MonitorIds = None


    def _deserialize(self, params):
        self.MonitorIds = params.get("MonitorIds")


class DeleteMonitorsResponse(AbstractModel):
    """DeleteMonitors返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSitesRequest(AbstractModel):
    """DeleteSites請求參數結構體

    """

    def __init__(self):
        """
        :param SiteIds: 站點ID清單
        :type SiteIds: list of int non-negative
        """
        self.SiteIds = None


    def _deserialize(self, params):
        self.SiteIds = params.get("SiteIds")


class DeleteSitesResponse(AbstractModel):
    """DeleteSites返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeConfigRequest(AbstractModel):
    """DescribeConfig請求參數結構體

    """


class DescribeConfigResponse(AbstractModel):
    """DescribeConfig返回參數結構體

    """

    def __init__(self):
        """
        :param NoticeLevel: 漏洞告警通知等級，4位分别代表：高危、中危、低危、提示。
        :type NoticeLevel: str
        :param Id: 配置ID。
        :type Id: int
        :param CreatedAt: 記錄創建時間。
        :type CreatedAt: str
        :param UpdatedAt: 記錄更新新建。
        :type UpdatedAt: str
        :param Appid: 雲用戶appid。
        :type Appid: int
        :param ContentLevel: 内容檢測通知等級-1:通知,0-不通知
        :type ContentLevel: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NoticeLevel = None
        self.Id = None
        self.CreatedAt = None
        self.UpdatedAt = None
        self.Appid = None
        self.ContentLevel = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NoticeLevel = params.get("NoticeLevel")
        self.Id = params.get("Id")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.Appid = params.get("Appid")
        self.ContentLevel = params.get("ContentLevel")
        self.RequestId = params.get("RequestId")


class DescribeMonitorsRequest(AbstractModel):
    """DescribeMonitors請求參數結構體

    """

    def __init__(self):
        """
        :param MonitorIds: 監控任務ID清單
        :type MonitorIds: list of int non-negative
        :param Filters: 過濾條件
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 返回數量，預設爲10，最大值爲100
        :type Limit: int
        """
        self.MonitorIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.MonitorIds = params.get("MonitorIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeMonitorsResponse(AbstractModel):
    """DescribeMonitors返回參數結構體

    """

    def __init__(self):
        """
        :param Monitors: 監控任務清單。
        :type Monitors: list of MonitorsDetail
        :param TotalCount: 監控任務數量。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Monitors = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Monitors") is not None:
            self.Monitors = []
            for item in params.get("Monitors"):
                obj = MonitorsDetail()
                obj._deserialize(item)
                self.Monitors.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSiteQuotaRequest(AbstractModel):
    """DescribeSiteQuota請求參數結構體

    """


class DescribeSiteQuotaResponse(AbstractModel):
    """DescribeSiteQuota返回參數結構體

    """

    def __init__(self):
        """
        :param Total: 已購買的掃描次數。
        :type Total: int
        :param Used: 已使用的掃描次數。
        :type Used: int
        :param Available: 剩餘可用的掃描次數。
        :type Available: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Used = None
        self.Available = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        self.Used = params.get("Used")
        self.Available = params.get("Available")
        self.RequestId = params.get("RequestId")


class DescribeSitesRequest(AbstractModel):
    """DescribeSites請求參數結構體

    """

    def __init__(self):
        """
        :param SiteIds: 站點ID清單
        :type SiteIds: list of int non-negative
        :param Filters: 過濾條件
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 返回數量，預設爲10，最大值爲100
        :type Limit: int
        """
        self.SiteIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SiteIds = params.get("SiteIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeSitesResponse(AbstractModel):
    """DescribeSites返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 站點數量。
        :type TotalCount: int
        :param Sites: 站點訊息清單。
        :type Sites: list of Site
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Sites = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Sites") is not None:
            self.Sites = []
            for item in params.get("Sites"):
                obj = Site()
                obj._deserialize(item)
                self.Sites.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSitesVerificationRequest(AbstractModel):
    """DescribeSitesVerification請求參數結構體

    """

    def __init__(self):
        """
        :param Urls: 站點的url清單
        :type Urls: list of str
        """
        self.Urls = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")


class DescribeSitesVerificationResponse(AbstractModel):
    """DescribeSitesVerification返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 驗證訊息數量。
        :type TotalCount: int
        :param SitesVerification: 驗證訊息清單。
        :type SitesVerification: list of SitesVerification
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SitesVerification = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SitesVerification") is not None:
            self.SitesVerification = []
            for item in params.get("SitesVerification"):
                obj = SitesVerification()
                obj._deserialize(item)
                self.SitesVerification.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVulsNumberRequest(AbstractModel):
    """DescribeVulsNumber請求參數結構體

    """


class DescribeVulsNumberResponse(AbstractModel):
    """DescribeVulsNumber返回參數結構體

    """

    def __init__(self):
        """
        :param ImpactSiteNumber: 受影響的網站總數。
        :type ImpactSiteNumber: int
        :param SiteNumber: 已驗證的網站總數。
        :type SiteNumber: int
        :param VulsHighNumber: 高風險漏洞總數。
        :type VulsHighNumber: int
        :param VulsMiddleNumber: 中風險漏洞總數。
        :type VulsMiddleNumber: int
        :param VulsLowNumber: 低高風險漏洞總數。
        :type VulsLowNumber: int
        :param VulsNoticeNumber: 風險提示總數。
        :type VulsNoticeNumber: int
        :param PageCount: 掃描頁面總數。
        :type PageCount: int
        :param Sites: 已驗證的網站清單。
        :type Sites: list of MonitorMiniSite
        :param ImpactSites: 受影響的網站清單。
        :type ImpactSites: list of MonitorMiniSite
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ImpactSiteNumber = None
        self.SiteNumber = None
        self.VulsHighNumber = None
        self.VulsMiddleNumber = None
        self.VulsLowNumber = None
        self.VulsNoticeNumber = None
        self.PageCount = None
        self.Sites = None
        self.ImpactSites = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImpactSiteNumber = params.get("ImpactSiteNumber")
        self.SiteNumber = params.get("SiteNumber")
        self.VulsHighNumber = params.get("VulsHighNumber")
        self.VulsMiddleNumber = params.get("VulsMiddleNumber")
        self.VulsLowNumber = params.get("VulsLowNumber")
        self.VulsNoticeNumber = params.get("VulsNoticeNumber")
        self.PageCount = params.get("PageCount")
        if params.get("Sites") is not None:
            self.Sites = []
            for item in params.get("Sites"):
                obj = MonitorMiniSite()
                obj._deserialize(item)
                self.Sites.append(obj)
        if params.get("ImpactSites") is not None:
            self.ImpactSites = []
            for item in params.get("ImpactSites"):
                obj = MonitorMiniSite()
                obj._deserialize(item)
                self.ImpactSites.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVulsNumberTimelineRequest(AbstractModel):
    """DescribeVulsNumberTimeline請求參數結構體

    """


class DescribeVulsNumberTimelineResponse(AbstractModel):
    """DescribeVulsNumberTimeline返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 統計數據記錄數量。
        :type TotalCount: int
        :param VulsTimeline: 用戶漏洞數随時間變化統計數據。
        :type VulsTimeline: list of VulsTimeline
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.VulsTimeline = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VulsTimeline") is not None:
            self.VulsTimeline = []
            for item in params.get("VulsTimeline"):
                obj = VulsTimeline()
                obj._deserialize(item)
                self.VulsTimeline.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVulsRequest(AbstractModel):
    """DescribeVuls請求參數結構體

    """

    def __init__(self):
        """
        :param SiteId: 站點ID
        :type SiteId: int
        :param MonitorId: 監控任務ID
        :type MonitorId: int
        :param Filters: 過濾條件
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 返回數量，預設爲10，最大值爲100
        :type Limit: int
        """
        self.SiteId = None
        self.MonitorId = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SiteId = params.get("SiteId")
        self.MonitorId = params.get("MonitorId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeVulsResponse(AbstractModel):
    """DescribeVuls返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 漏洞數量。
        :type TotalCount: int
        :param Vuls: 漏洞訊息清單。
        :type Vuls: list of Vul
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Vuls = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Vuls") is not None:
            self.Vuls = []
            for item in params.get("Vuls"):
                obj = Vul()
                obj._deserialize(item)
                self.Vuls.append(obj)
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """描述鍵值對過濾器，用于條件過濾查詢。例如過濾ID、名稱、狀态等

    若存在多個Filter時，Filter間的關系爲邏輯與（AND）關系。
    若同一個Filter存在多個Values，同一Filter下Values間的關系爲邏輯或（OR）關系。

    """

    def __init__(self):
        """
        :param Name: 過濾鍵的名稱。
        :type Name: str
        :param Values: 一個或者多個過濾值。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class MiniSite(AbstractModel):
    """站點訊息。

    """

    def __init__(self):
        """
        :param SiteId: 站點ID。
        :type SiteId: int
        :param Url: 站點Url。
        :type Url: str
        """
        self.SiteId = None
        self.Url = None


    def _deserialize(self, params):
        self.SiteId = params.get("SiteId")
        self.Url = params.get("Url")


class ModifyConfigAttributeRequest(AbstractModel):
    """ModifyConfigAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param NoticeLevel: 漏洞告警通知等級，4位分别代表：高危、中危、低危、提示
        :type NoticeLevel: str
        """
        self.NoticeLevel = None


    def _deserialize(self, params):
        self.NoticeLevel = params.get("NoticeLevel")


class ModifyConfigAttributeResponse(AbstractModel):
    """ModifyConfigAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMonitorAttributeRequest(AbstractModel):
    """ModifyMonitorAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param MonitorId: 監測任務ID
        :type MonitorId: int
        :param Urls: 站點的url清單
        :type Urls: list of str
        :param Name: 任務名稱
        :type Name: str
        :param ScannerType: 掃描模式，normal-正常掃描；deep-深度掃描
        :type ScannerType: str
        :param Crontab: 掃描週期，單位小時，每X小時執行一次
        :type Crontab: int
        :param RateLimit: 掃描速率限制，每秒發送X個HTTP請求
        :type RateLimit: int
        :param FirstScanStartTime: 首次掃描開始時間
        :type FirstScanStartTime: str
        :param MonitorStatus: 監測狀态：1-監測中；2-暫停監測
        :type MonitorStatus: int
        """
        self.MonitorId = None
        self.Urls = None
        self.Name = None
        self.ScannerType = None
        self.Crontab = None
        self.RateLimit = None
        self.FirstScanStartTime = None
        self.MonitorStatus = None


    def _deserialize(self, params):
        self.MonitorId = params.get("MonitorId")
        self.Urls = params.get("Urls")
        self.Name = params.get("Name")
        self.ScannerType = params.get("ScannerType")
        self.Crontab = params.get("Crontab")
        self.RateLimit = params.get("RateLimit")
        self.FirstScanStartTime = params.get("FirstScanStartTime")
        self.MonitorStatus = params.get("MonitorStatus")


class ModifyMonitorAttributeResponse(AbstractModel):
    """ModifyMonitorAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySiteAttributeRequest(AbstractModel):
    """ModifySiteAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param SiteId: 站點ID
        :type SiteId: int
        :param Name: 站點名稱
        :type Name: str
        :param NeedLogin: 網站是否需要登入掃描：0-未知；-1-不需要；1-需要
        :type NeedLogin: int
        :param LoginCookie: 登入後的cookie
        :type LoginCookie: str
        :param LoginCheckUrl: 用于測試cookie是否有效的URL
        :type LoginCheckUrl: str
        :param LoginCheckKw: 用于測試cookie是否有效的關鍵字
        :type LoginCheckKw: str
        :param ScanDisallow: 禁止掃描器掃描的目錄關鍵字
        :type ScanDisallow: str
        """
        self.SiteId = None
        self.Name = None
        self.NeedLogin = None
        self.LoginCookie = None
        self.LoginCheckUrl = None
        self.LoginCheckKw = None
        self.ScanDisallow = None


    def _deserialize(self, params):
        self.SiteId = params.get("SiteId")
        self.Name = params.get("Name")
        self.NeedLogin = params.get("NeedLogin")
        self.LoginCookie = params.get("LoginCookie")
        self.LoginCheckUrl = params.get("LoginCheckUrl")
        self.LoginCheckKw = params.get("LoginCheckKw")
        self.ScanDisallow = params.get("ScanDisallow")


class ModifySiteAttributeResponse(AbstractModel):
    """ModifySiteAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Monitor(AbstractModel):
    """監控任務基礎數據

    """

    def __init__(self):
        """
        :param Id: 監控任務ID。
        :type Id: int
        :param Name: 監控名稱。
        :type Name: str
        :param MonitorStatus: 監測狀态：1-監測中；2-暫停監測。
        :type MonitorStatus: int
        :param ScannerType: 監測模式，normal-正常掃描；deep-深度掃描。
        :type ScannerType: str
        :param Crontab: 掃描週期，單位小時，每X小時執行一次。
        :type Crontab: int
        :param IncludedVulsTypes: 指定掃描類型，3位數每位依次表示：掃描Web漏洞、掃描系統漏洞、掃描系統端口。
        :type IncludedVulsTypes: str
        :param RateLimit: 速率限制，每秒發送X個HTTP請求。
        :type RateLimit: int
        :param FirstScanStartTime: 首次掃描開始時間。
        :type FirstScanStartTime: str
        :param ScanStatus: 掃描狀态：0-待掃描（無任何掃描結果）；1-掃描中（正在進行掃描）；2-已掃描（有掃描結果且不正在掃描）；3-掃描完成待同步結果。
        :type ScanStatus: int
        :param LastScanFinishTime: 上一次掃描完成時間。
        :type LastScanFinishTime: str
        :param CurrentScanStartTime: 當前掃描開始時間，如掃描完成則爲上一次掃描的開始時間。
        :type CurrentScanStartTime: str
        :param CreatedAt: CreatedAt。
        :type CreatedAt: str
        :param UpdatedAt: UpdatedAt。
        :type UpdatedAt: str
        :param Appid: 雲用戶appid。
        :type Appid: int
        :param ContentScanStatus: 掃描狀态：0-待檢測；1-檢測完成
        :type ContentScanStatus: int
        """
        self.Id = None
        self.Name = None
        self.MonitorStatus = None
        self.ScannerType = None
        self.Crontab = None
        self.IncludedVulsTypes = None
        self.RateLimit = None
        self.FirstScanStartTime = None
        self.ScanStatus = None
        self.LastScanFinishTime = None
        self.CurrentScanStartTime = None
        self.CreatedAt = None
        self.UpdatedAt = None
        self.Appid = None
        self.ContentScanStatus = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.MonitorStatus = params.get("MonitorStatus")
        self.ScannerType = params.get("ScannerType")
        self.Crontab = params.get("Crontab")
        self.IncludedVulsTypes = params.get("IncludedVulsTypes")
        self.RateLimit = params.get("RateLimit")
        self.FirstScanStartTime = params.get("FirstScanStartTime")
        self.ScanStatus = params.get("ScanStatus")
        self.LastScanFinishTime = params.get("LastScanFinishTime")
        self.CurrentScanStartTime = params.get("CurrentScanStartTime")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.Appid = params.get("Appid")
        self.ContentScanStatus = params.get("ContentScanStatus")


class MonitorMiniSite(AbstractModel):
    """監控任務中的站點訊息。

    """

    def __init__(self):
        """
        :param SiteId: 站點ID。
        :type SiteId: int
        :param Url: 站點Url。
        :type Url: str
        """
        self.SiteId = None
        self.Url = None


    def _deserialize(self, params):
        self.SiteId = params.get("SiteId")
        self.Url = params.get("Url")


class MonitorsDetail(AbstractModel):
    """監控任務詳細數據

    """

    def __init__(self):
        """
        :param Basic: 監控任務基礎訊息。
        :type Basic: :class:`tencentcloud.cws.v20180312.models.Monitor`
        :param Sites: 監控任務包含的站點清單。
        :type Sites: list of MonitorMiniSite
        :param SiteNumber: 監控任務包含的站點清單數量。
        :type SiteNumber: int
        :param ImpactSites: 監控任務包含的受漏洞威脅的站點清單。
        :type ImpactSites: list of MonitorMiniSite
        :param ImpactSiteNumber: 監控任務包含的受漏洞威脅的站點清單數量。
        :type ImpactSiteNumber: int
        :param VulsHighNumber: 高風險漏洞數量。
        :type VulsHighNumber: int
        :param VulsMiddleNumber: 中風險漏洞數量。
        :type VulsMiddleNumber: int
        :param VulsLowNumber: 低風險漏洞數量。
        :type VulsLowNumber: int
        :param VulsNoticeNumber: 提示數量。
        :type VulsNoticeNumber: int
        :param Progress: 監控任務包含的站點清單的平均掃描進度。
        :type Progress: int
        :param PageCount: 掃描頁面總數。
        :type PageCount: int
        :param ContentNumber: 内容檢測數量。
        :type ContentNumber: int
        """
        self.Basic = None
        self.Sites = None
        self.SiteNumber = None
        self.ImpactSites = None
        self.ImpactSiteNumber = None
        self.VulsHighNumber = None
        self.VulsMiddleNumber = None
        self.VulsLowNumber = None
        self.VulsNoticeNumber = None
        self.Progress = None
        self.PageCount = None
        self.ContentNumber = None


    def _deserialize(self, params):
        if params.get("Basic") is not None:
            self.Basic = Monitor()
            self.Basic._deserialize(params.get("Basic"))
        if params.get("Sites") is not None:
            self.Sites = []
            for item in params.get("Sites"):
                obj = MonitorMiniSite()
                obj._deserialize(item)
                self.Sites.append(obj)
        self.SiteNumber = params.get("SiteNumber")
        if params.get("ImpactSites") is not None:
            self.ImpactSites = []
            for item in params.get("ImpactSites"):
                obj = MonitorMiniSite()
                obj._deserialize(item)
                self.ImpactSites.append(obj)
        self.ImpactSiteNumber = params.get("ImpactSiteNumber")
        self.VulsHighNumber = params.get("VulsHighNumber")
        self.VulsMiddleNumber = params.get("VulsMiddleNumber")
        self.VulsLowNumber = params.get("VulsLowNumber")
        self.VulsNoticeNumber = params.get("VulsNoticeNumber")
        self.Progress = params.get("Progress")
        self.PageCount = params.get("PageCount")
        self.ContentNumber = params.get("ContentNumber")


class Site(AbstractModel):
    """站點數據

    """

    def __init__(self):
        """
        :param Id: 站點ID。
        :type Id: int
        :param MonitorId: 監控任務ID，爲0時表示未加入監控任務。
        :type MonitorId: int
        :param Url: 站點url。
        :type Url: str
        :param Name: 站點名稱。
        :type Name: str
        :param VerifyStatus: 驗證狀态：0-未驗證；1-已驗證；2-驗證失效，待重新驗證。
        :type VerifyStatus: int
        :param MonitorStatus: 監測狀态：0-未監測；1-監測中；2-暫停監測。
        :type MonitorStatus: int
        :param ScanStatus: 掃描狀态：0-待掃描（無任何掃描結果）；1-掃描中（正在進行掃描）；2-已掃描（有掃描結果且不正在掃描）；3-掃描完成待同步結果。
        :type ScanStatus: int
        :param LastScanTaskId: 最近一次的AIScanner的掃描任務id，注意取消的情況。
        :type LastScanTaskId: int
        :param LastScanStartTime: 最近一次掃描開始時間。
        :type LastScanStartTime: str
        :param LastScanFinishTime: 最近一次掃描完成時間。
        :type LastScanFinishTime: str
        :param LastScanCancelTime: 最近一次取消時間，取消即使用上一次掃描結果。
        :type LastScanCancelTime: str
        :param LastScanPageCount: 最近一次掃描掃描的頁面數。
        :type LastScanPageCount: int
        :param LastScanScannerType: normal-正常掃描；deep-深度掃描。
        :type LastScanScannerType: str
        :param LastScanVulsHighNum: 最近一次掃描高風險漏洞數量。
        :type LastScanVulsHighNum: int
        :param LastScanVulsMiddleNum: 最近一次掃描中風險漏洞數量。
        :type LastScanVulsMiddleNum: int
        :param LastScanVulsLowNum: 最近一次掃描低風險漏洞數量。
        :type LastScanVulsLowNum: int
        :param LastScanVulsNoticeNum: 最近一次掃描提示訊息數量。
        :type LastScanVulsNoticeNum: int
        :param CreatedAt: 記錄添加時間。
        :type CreatedAt: str
        :param UpdatedAt: 記錄最近修改時間。
        :type UpdatedAt: str
        :param LastScanRateLimit: 速率限制，每秒發送X個HTTP請求。
        :type LastScanRateLimit: int
        :param LastScanVulsNum: 最近一次掃描漏洞總數量。
        :type LastScanVulsNum: int
        :param LastScanNoticeNum: 最近一次掃描提示總數量
        :type LastScanNoticeNum: int
        :param Progress: 掃描進度，百分比整數
        :type Progress: int
        :param Appid: 雲用戶appid。
        :type Appid: int
        :param Uin: 雲用戶标識。
        :type Uin: str
        :param NeedLogin: 網站是否需要登入掃描：0-未知；-1-不需要；1-需要。
        :type NeedLogin: int
        :param LoginCookie: 登入後的cookie。
        :type LoginCookie: str
        :param LoginCookieValid: 登入後的cookie是否有效：0-無效；1-有效。
        :type LoginCookieValid: int
        :param LoginCheckUrl: 用于測試cookie是否有效的URL。
        :type LoginCheckUrl: str
        :param LoginCheckKw: 用于測試cookie是否有效的關鍵字。
        :type LoginCheckKw: str
        :param ScanDisallow: 禁止掃描器掃描的目錄關鍵字。
        :type ScanDisallow: str
        :param UserAgent: 訪問網站的用戶端标識。
        :type UserAgent: str
        :param ContentStatus: 内容檢測狀态：0-未檢測；1-已檢測；
        :type ContentStatus: int
        :param LastScanContentNum: 最近一次掃描内容檢測數量
        :type LastScanContentNum: int
        """
        self.Id = None
        self.MonitorId = None
        self.Url = None
        self.Name = None
        self.VerifyStatus = None
        self.MonitorStatus = None
        self.ScanStatus = None
        self.LastScanTaskId = None
        self.LastScanStartTime = None
        self.LastScanFinishTime = None
        self.LastScanCancelTime = None
        self.LastScanPageCount = None
        self.LastScanScannerType = None
        self.LastScanVulsHighNum = None
        self.LastScanVulsMiddleNum = None
        self.LastScanVulsLowNum = None
        self.LastScanVulsNoticeNum = None
        self.CreatedAt = None
        self.UpdatedAt = None
        self.LastScanRateLimit = None
        self.LastScanVulsNum = None
        self.LastScanNoticeNum = None
        self.Progress = None
        self.Appid = None
        self.Uin = None
        self.NeedLogin = None
        self.LoginCookie = None
        self.LoginCookieValid = None
        self.LoginCheckUrl = None
        self.LoginCheckKw = None
        self.ScanDisallow = None
        self.UserAgent = None
        self.ContentStatus = None
        self.LastScanContentNum = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MonitorId = params.get("MonitorId")
        self.Url = params.get("Url")
        self.Name = params.get("Name")
        self.VerifyStatus = params.get("VerifyStatus")
        self.MonitorStatus = params.get("MonitorStatus")
        self.ScanStatus = params.get("ScanStatus")
        self.LastScanTaskId = params.get("LastScanTaskId")
        self.LastScanStartTime = params.get("LastScanStartTime")
        self.LastScanFinishTime = params.get("LastScanFinishTime")
        self.LastScanCancelTime = params.get("LastScanCancelTime")
        self.LastScanPageCount = params.get("LastScanPageCount")
        self.LastScanScannerType = params.get("LastScanScannerType")
        self.LastScanVulsHighNum = params.get("LastScanVulsHighNum")
        self.LastScanVulsMiddleNum = params.get("LastScanVulsMiddleNum")
        self.LastScanVulsLowNum = params.get("LastScanVulsLowNum")
        self.LastScanVulsNoticeNum = params.get("LastScanVulsNoticeNum")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.LastScanRateLimit = params.get("LastScanRateLimit")
        self.LastScanVulsNum = params.get("LastScanVulsNum")
        self.LastScanNoticeNum = params.get("LastScanNoticeNum")
        self.Progress = params.get("Progress")
        self.Appid = params.get("Appid")
        self.Uin = params.get("Uin")
        self.NeedLogin = params.get("NeedLogin")
        self.LoginCookie = params.get("LoginCookie")
        self.LoginCookieValid = params.get("LoginCookieValid")
        self.LoginCheckUrl = params.get("LoginCheckUrl")
        self.LoginCheckKw = params.get("LoginCheckKw")
        self.ScanDisallow = params.get("ScanDisallow")
        self.UserAgent = params.get("UserAgent")
        self.ContentStatus = params.get("ContentStatus")
        self.LastScanContentNum = params.get("LastScanContentNum")


class SitesVerification(AbstractModel):
    """站點驗證數據

    """

    def __init__(self):
        """
        :param Domain: 根域名。
        :type Domain: str
        :param TxtName: txt解析域名驗證的name。
        :type TxtName: str
        :param TxtText: txt解析域名驗證的text。
        :type TxtText: str
        :param ValidTo: 驗證有效期，在此之前有效。
        :type ValidTo: str
        :param VerifyStatus: 驗證狀态：0-未驗證；1-已驗證；2-驗證失效，待重新驗證。
        :type VerifyStatus: int
        :param CreatedAt: CreatedAt。
        :type CreatedAt: str
        :param UpdatedAt: UpdatedAt。
        :type UpdatedAt: str
        :param Id: ID。
        :type Id: int
        :param Appid: 雲用戶appid
        :type Appid: int
        :param VerifyUrl: 用于驗證站點的url，即訪問該url獲取驗證數據。
        :type VerifyUrl: str
        :param VerifyFileUrl: 獲取驗證驗證文件的url。
        :type VerifyFileUrl: str
        """
        self.Domain = None
        self.TxtName = None
        self.TxtText = None
        self.ValidTo = None
        self.VerifyStatus = None
        self.CreatedAt = None
        self.UpdatedAt = None
        self.Id = None
        self.Appid = None
        self.VerifyUrl = None
        self.VerifyFileUrl = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.TxtName = params.get("TxtName")
        self.TxtText = params.get("TxtText")
        self.ValidTo = params.get("ValidTo")
        self.VerifyStatus = params.get("VerifyStatus")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.Id = params.get("Id")
        self.Appid = params.get("Appid")
        self.VerifyUrl = params.get("VerifyUrl")
        self.VerifyFileUrl = params.get("VerifyFileUrl")


class VerifySitesRequest(AbstractModel):
    """VerifySites請求參數結構體

    """

    def __init__(self):
        """
        :param Urls: 站點的url清單
        :type Urls: list of str
        """
        self.Urls = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")


class VerifySitesResponse(AbstractModel):
    """VerifySites返回參數結構體

    """

    def __init__(self):
        """
        :param SuccessNumber: 驗證成功的根域名數量。
        :type SuccessNumber: int
        :param FailNumber: 驗證失敗的根域名數量。
        :type FailNumber: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SuccessNumber = None
        self.FailNumber = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessNumber = params.get("SuccessNumber")
        self.FailNumber = params.get("FailNumber")
        self.RequestId = params.get("RequestId")


class Vul(AbstractModel):
    """漏洞數據

    """

    def __init__(self):
        """
        :param Id: 漏洞ID。
        :type Id: int
        :param SiteId: 站點ID。
        :type SiteId: int
        :param TaskId: 掃描引擎的掃描任務ID。
        :type TaskId: int
        :param Level: 漏洞級别：high、middle、low、notice。
        :type Level: str
        :param Name: 漏洞名稱。
        :type Name: str
        :param Url: 出現漏洞的url。
        :type Url: str
        :param Html: 網址/細節。
        :type Html: str
        :param Nickname: 漏洞類型。
        :type Nickname: str
        :param Harm: 危害說明。
        :type Harm: str
        :param Describe: 漏洞描述。
        :type Describe: str
        :param Solution: 解決方案。
        :type Solution: str
        :param From: 漏洞參考。
        :type From: str
        :param Parameter: 漏洞通過該參數攻擊。
        :type Parameter: str
        :param CreatedAt: CreatedAt。
        :type CreatedAt: str
        :param UpdatedAt: UpdatedAt。
        :type UpdatedAt: str
        :param IsReported: 是否已經添加誤報，0-否，1-是。
        :type IsReported: int
        :param Appid: 雲用戶appid。
        :type Appid: int
        :param Uin: 雲用戶标識。
        :type Uin: str
        """
        self.Id = None
        self.SiteId = None
        self.TaskId = None
        self.Level = None
        self.Name = None
        self.Url = None
        self.Html = None
        self.Nickname = None
        self.Harm = None
        self.Describe = None
        self.Solution = None
        self.From = None
        self.Parameter = None
        self.CreatedAt = None
        self.UpdatedAt = None
        self.IsReported = None
        self.Appid = None
        self.Uin = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.SiteId = params.get("SiteId")
        self.TaskId = params.get("TaskId")
        self.Level = params.get("Level")
        self.Name = params.get("Name")
        self.Url = params.get("Url")
        self.Html = params.get("Html")
        self.Nickname = params.get("Nickname")
        self.Harm = params.get("Harm")
        self.Describe = params.get("Describe")
        self.Solution = params.get("Solution")
        self.From = params.get("From")
        self.Parameter = params.get("Parameter")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.IsReported = params.get("IsReported")
        self.Appid = params.get("Appid")
        self.Uin = params.get("Uin")


class VulsTimeline(AbstractModel):
    """用戶漏洞數随時間變化統計數據

    """

    def __init__(self):
        """
        :param Id: ID。
        :type Id: int
        :param Appid: 雲用戶appid。
        :type Appid: int
        :param Date: 日期。
        :type Date: str
        :param PageCount: 掃描頁面總數量。
        :type PageCount: int
        :param SiteNum: 已驗證網站總數量。
        :type SiteNum: int
        :param ImpactSiteNum: 受影響的網站總數量。
        :type ImpactSiteNum: int
        :param VulsHighNum: 高危漏洞總數量。
        :type VulsHighNum: int
        :param VulsMiddleNum: 中危漏洞總數量。
        :type VulsMiddleNum: int
        :param VulsLowNum: 低危漏洞總數量。
        :type VulsLowNum: int
        :param VulsNoticeNum: 風險提示總數量
        :type VulsNoticeNum: int
        :param CreatedAt: 記錄添加時間。
        :type CreatedAt: str
        :param UpdatedAt: 記錄最近修改時間。
        :type UpdatedAt: str
        """
        self.Id = None
        self.Appid = None
        self.Date = None
        self.PageCount = None
        self.SiteNum = None
        self.ImpactSiteNum = None
        self.VulsHighNum = None
        self.VulsMiddleNum = None
        self.VulsLowNum = None
        self.VulsNoticeNum = None
        self.CreatedAt = None
        self.UpdatedAt = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Appid = params.get("Appid")
        self.Date = params.get("Date")
        self.PageCount = params.get("PageCount")
        self.SiteNum = params.get("SiteNum")
        self.ImpactSiteNum = params.get("ImpactSiteNum")
        self.VulsHighNum = params.get("VulsHighNum")
        self.VulsMiddleNum = params.get("VulsMiddleNum")
        self.VulsLowNum = params.get("VulsLowNum")
        self.VulsNoticeNum = params.get("VulsNoticeNum")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")