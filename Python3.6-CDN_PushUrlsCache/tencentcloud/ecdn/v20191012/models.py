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


class AddEcdnDomainRequest(AbstractModel):
    """AddEcdnDomain請求參數結構體

    """

    def __init__(self):
        """
        :param Domain: 域名。
        :type Domain: str
        :param Origin: 源站配置。
        :type Origin: :class:`taifucloudcloud.ecdn.v20191012.models.Origin`
        :param Area: 域名加速區域，mainland，overseas或global，分别表示 境内加速，海外加速或全球加速。
        :type Area: str
        :param ProjectId: 項目id，預設0。
        :type ProjectId: int
        :param IpFilter: IP黑白名單配置。
        :type IpFilter: :class:`taifucloudcloud.ecdn.v20191012.models.IpFilter`
        :param IpFreqLimit: IP限頻配置。
        :type IpFreqLimit: :class:`taifucloudcloud.ecdn.v20191012.models.IpFreqLimit`
        :param ResponseHeader: 源站響應頭部配置。
        :type ResponseHeader: :class:`taifucloudcloud.ecdn.v20191012.models.ResponseHeader`
        :param CacheKey: 節點快取配置。
        :type CacheKey: :class:`taifucloudcloud.ecdn.v20191012.models.CacheKey`
        :param Cache: 快取規則配置。
        :type Cache: :class:`taifucloudcloud.ecdn.v20191012.models.Cache`
        :param Https: Https配置。
        :type Https: :class:`taifucloudcloud.ecdn.v20191012.models.Https`
        :param ForceRedirect: 訪問協議強制跳轉配置。
        :type ForceRedirect: :class:`taifucloudcloud.ecdn.v20191012.models.ForceRedirect`
        """
        self.Domain = None
        self.Origin = None
        self.Area = None
        self.ProjectId = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.ResponseHeader = None
        self.CacheKey = None
        self.Cache = None
        self.Https = None
        self.ForceRedirect = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        self.Area = params.get("Area")
        self.ProjectId = params.get("ProjectId")
        if params.get("IpFilter") is not None:
            self.IpFilter = IpFilter()
            self.IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self.IpFreqLimit = IpFreqLimit()
            self.IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))


class AddEcdnDomainResponse(AbstractModel):
    """AddEcdnDomain返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Cache(AbstractModel):
    """快取配置簡單版本，該版本不支援設置源站未返回max-age情況下的快取規則。

    """

    def __init__(self):
        """
        :param CacheRules: 快取配置規則數組。
        :type CacheRules: list of CacheRule
        :param FollowOrigin: 遵循源站 Cache-Control: max-age 配置
on：開啓
off：關閉
開啓後，未能比對 CacheRules 規則的資源将根據源站返回的 max-age 值進行節點快取；比對了 CacheRules 規則的資源将按照 CacheRules 中設置的快取過期時間在節點進行快取
注意：此欄位可能返回 null，表示取不到有效值。
        :type FollowOrigin: str
        """
        self.CacheRules = None
        self.FollowOrigin = None


    def _deserialize(self, params):
        if params.get("CacheRules") is not None:
            self.CacheRules = []
            for item in params.get("CacheRules"):
                obj = CacheRule()
                obj._deserialize(item)
                self.CacheRules.append(obj)
        self.FollowOrigin = params.get("FollowOrigin")


class CacheKey(AbstractModel):
    """快取相關配置。

    """

    def __init__(self):
        """
        :param FullUrlCache: 是否開啓全路徑快取，on或off。
        :type FullUrlCache: str
        """
        self.FullUrlCache = None


    def _deserialize(self, params):
        self.FullUrlCache = params.get("FullUrlCache")


class CacheRule(AbstractModel):
    """快取配置規則。

    """

    def __init__(self):
        """
        :param CacheType: 快取類型，支援all，file，directory，path，index，分别表示全部文件，後綴類型，目錄，完整路徑，首頁。
        :type CacheType: str
        :param CacheContents: 快取内容清單。
        :type CacheContents: list of str
        :param CacheTime: 快取時間，單位秒。
        :type CacheTime: int
        """
        self.CacheType = None
        self.CacheContents = None
        self.CacheTime = None


    def _deserialize(self, params):
        self.CacheType = params.get("CacheType")
        self.CacheContents = params.get("CacheContents")
        self.CacheTime = params.get("CacheTime")


class ClientCert(AbstractModel):
    """https用戶端證書配置。

    """

    def __init__(self):
        """
        :param Certificate: 用戶端證書，pem格式。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Certificate: str
        :param CertName: 用戶端證書名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertName: str
        :param ExpireTime: 證書過期時間。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param DeployTime: 證書頒發時間。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeployTime: str
        """
        self.Certificate = None
        self.CertName = None
        self.ExpireTime = None
        self.DeployTime = None


    def _deserialize(self, params):
        self.Certificate = params.get("Certificate")
        self.CertName = params.get("CertName")
        self.ExpireTime = params.get("ExpireTime")
        self.DeployTime = params.get("DeployTime")


class DeleteEcdnDomainRequest(AbstractModel):
    """DeleteEcdnDomain請求參數結構體

    """

    def __init__(self):
        """
        :param Domain: 待删除域名。
        :type Domain: str
        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")


class DeleteEcdnDomainResponse(AbstractModel):
    """DeleteEcdnDomain返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDomainsConfigRequest(AbstractModel):
    """DescribeDomainsConfig請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 分頁查詢的偏移網址，預設0。
        :type Offset: int
        :param Limit: 分頁查詢的域名個數，預設100。
        :type Limit: int
        :param Filters: 查詢條件過濾器。
        :type Filters: list of DomainFilter
        :param Sort: 查詢結果排序規則。
        :type Sort: :class:`taifucloudcloud.ecdn.v20191012.models.Sort`
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.Sort = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = DomainFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("Sort") is not None:
            self.Sort = Sort()
            self.Sort._deserialize(params.get("Sort"))


class DescribeDomainsConfigResponse(AbstractModel):
    """DescribeDomainsConfig返回參數結構體

    """

    def __init__(self):
        """
        :param Domains: 域名清單。
        :type Domains: list of DomainDetailInfo
        :param TotalCount: 符合查詢條件的域名總數，用于分頁查詢。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Domains = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Domains") is not None:
            self.Domains = []
            for item in params.get("Domains"):
                obj = DomainDetailInfo()
                obj._deserialize(item)
                self.Domains.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDomainsRequest(AbstractModel):
    """DescribeDomains請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 分頁查詢的偏移網址，預設0。
        :type Offset: int
        :param Limit: 分頁查詢的域名個數，預設100，最大支援1000。
        :type Limit: int
        :param Filters: 查詢條件過濾器。
        :type Filters: list of DomainFilter
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = DomainFilter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeDomainsResponse(AbstractModel):
    """DescribeDomains返回參數結構體

    """

    def __init__(self):
        """
        :param Domains: 域名訊息清單。
        :type Domains: list of DomainBriefInfo
        :param TotalCount: 域名總個數。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Domains = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Domains") is not None:
            self.Domains = []
            for item in params.get("Domains"):
                obj = DomainBriefInfo()
                obj._deserialize(item)
                self.Domains.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeEcdnDomainLogsRequest(AbstractModel):
    """DescribeEcdnDomainLogs請求參數結構體

    """

    def __init__(self):
        """
        :param Domain: 待查詢域名。
        :type Domain: str
        :param StartTime: 日志起始時間。如：2019-10-01 00:00:00
        :type StartTime: str
        :param EndTime: 日志結束時間，只支援最近30天内日志查詢。2019-10-02 00:00:00
        :type EndTime: str
        :param Offset: 日志連結清單分頁起始網址，預設0。
        :type Offset: int
        :param Limit: 日志連結清單分頁記錄條數，預設100，最大1000。
        :type Limit: int
        """
        self.Domain = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeEcdnDomainLogsResponse(AbstractModel):
    """DescribeEcdnDomainLogs返回參數結構體

    """

    def __init__(self):
        """
        :param DomainLogs: 日志連結清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DomainLogs: list of DomainLogs
        :param TotalCount: 日志連結總條數。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DomainLogs = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainLogs") is not None:
            self.DomainLogs = []
            for item in params.get("DomainLogs"):
                obj = DomainLogs()
                obj._deserialize(item)
                self.DomainLogs.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeEcdnDomainStatisticsRequest(AbstractModel):
    """DescribeEcdnDomainStatistics請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 查詢起始時間，如：2019-12-13 00:00:00。
起止時間不超過90天。
        :type StartTime: str
        :param EndTime: 查詢結束時間，如：2019-12-13 23:59:59。
起止時間不超過90天。
        :type EndTime: str
        :param Metrics: 統計指标名稱。flux：流量，單位爲 byte
bandwidth：頻寬，單位爲 bps
request：請求數，單位爲 次
delay：響應時間，單位爲ms
static_request ： 靜态請求數，單位爲 次
static_flux：靜态流量，單位爲 byte
static_bandwidth ： 靜态頻寬，單位爲 bps
dynamic_request：動态請求數，單位爲 次
dynamic_flux：動态流量，單位爲 byte
dynamic_bandwidth：動态頻寬，單位爲 bps
        :type Metrics: list of str
        :param Domains: 指定查詢域名清單
        :type Domains: list of str
        :param Projects: 指定要查詢的項目 ID，[前往檢視項目 ID](https://console.cloud.taifucloud.com/project)
未填充域名情況下，指定項目查詢，若填充了具體域名訊息，以域名爲主
        :type Projects: list of int
        :param Offset: 清單分頁起始網址，預設0。
        :type Offset: int
        :param Limit: 清單分頁記錄條數，預設1000，最大3000。
        :type Limit: int
        """
        self.StartTime = None
        self.EndTime = None
        self.Metrics = None
        self.Domains = None
        self.Projects = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Metrics = params.get("Metrics")
        self.Domains = params.get("Domains")
        self.Projects = params.get("Projects")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeEcdnDomainStatisticsResponse(AbstractModel):
    """DescribeEcdnDomainStatistics返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 域名數據
        :type Data: list of DomainData
        :param TotalCount: 數量
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DomainData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeEcdnStatisticsRequest(AbstractModel):
    """DescribeEcdnStatistics請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 查詢起始時間，如：2019-12-13 00:00:00
        :type StartTime: str
        :param EndTime: 查詢結束時間，如：2019-12-13 23:59:59
        :type EndTime: str
        :param Metrics: 指定查詢指标，支援的類型有：
flux：流量，單位爲 byte
bandwidth：頻寬，單位爲 bps
request：請求數，單位爲 次
delay：響應時間，單位爲ms
2xx：返回 2xx 狀态碼匯總或者 2 開頭狀态碼數據，單位爲 個
3xx：返回 3xx 狀态碼匯總或者 3 開頭狀态碼數據，單位爲 個
4xx：返回 4xx 狀态碼匯總或者 4 開頭狀态碼數據，單位爲 個
5xx：返回 5xx 狀态碼匯總或者 5 開頭狀态碼數據，單位爲 個
static_request ： 靜态請求數，單位爲 次
static_flux：靜态流量，單位爲 byte
static_bandwidth ： 靜态頻寬，單位爲 bps
dynamic_request：動态請求數，單位爲 次
dynamic_flux：動态流量，單位爲 byte
dynamic_bandwidth：動态頻寬，單位爲 bps
        :type Metrics: list of str
        :param Interval: 時間粒度，支援以下幾種模式：
1 天	 1，5，15，30，60，120，240，1440 
2 ~ 3 天	15，30，60，120，240，1440
4 ~ 7 天	30，60，120，240，1440
8 ~ 90 天	 60，120，240，1440
        :type Interval: int
        :param Domains: 指定查詢域名清單

最多可一次性查詢30個加速域名。
        :type Domains: list of str
        :param Projects: 指定要查詢的項目 ID，[前往檢視項目 ID](https://console.cloud.taifucloud.com/project)
未填充域名情況下，指定項目查詢，若填充了具體域名訊息，以域名爲主
        :type Projects: list of int
        """
        self.StartTime = None
        self.EndTime = None
        self.Metrics = None
        self.Interval = None
        self.Domains = None
        self.Projects = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Metrics = params.get("Metrics")
        self.Interval = params.get("Interval")
        self.Domains = params.get("Domains")
        self.Projects = params.get("Projects")


class DescribeEcdnStatisticsResponse(AbstractModel):
    """DescribeEcdnStatistics返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 指定條件查詢得到的數據明細
        :type Data: list of ResourceData
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ResourceData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePurgeQuotaRequest(AbstractModel):
    """DescribePurgeQuota請求參數結構體

    """


class DescribePurgeQuotaResponse(AbstractModel):
    """DescribePurgeQuota返回參數結構體

    """

    def __init__(self):
        """
        :param UrlPurge: Url重新整理用量及配額。
        :type UrlPurge: :class:`taifucloudcloud.ecdn.v20191012.models.Quota`
        :param PathPurge: 目錄重新整理用量及配額。
        :type PathPurge: :class:`taifucloudcloud.ecdn.v20191012.models.Quota`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.UrlPurge = None
        self.PathPurge = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UrlPurge") is not None:
            self.UrlPurge = Quota()
            self.UrlPurge._deserialize(params.get("UrlPurge"))
        if params.get("PathPurge") is not None:
            self.PathPurge = Quota()
            self.PathPurge._deserialize(params.get("PathPurge"))
        self.RequestId = params.get("RequestId")


class DescribePurgeTasksRequest(AbstractModel):
    """DescribePurgeTasks請求參數結構體

    """

    def __init__(self):
        """
        :param PurgeType: 查詢重新整理類型。url：查詢 url 重新整理記錄；path：查詢目錄重新整理記錄。
        :type PurgeType: str
        :param StartTime: 開始時間，如2018-08-08 00:00:00。
        :type StartTime: str
        :param EndTime: 結束時間，如2018-08-08 23:59:59。
        :type EndTime: str
        :param TaskId: 提交時返回的任務 Id，查詢時 TaskId 和起始時間必須指定一項。
        :type TaskId: str
        :param Offset: 分頁查詢偏移量，預設爲0（從第0條開始）。
        :type Offset: int
        :param Limit: 分頁查詢限制數目，預設爲20。
        :type Limit: int
        :param Keyword: 查詢關鍵字，請輸入域名或 http(s):// 開頭完整 URL。
        :type Keyword: str
        :param Status: 查詢指定任務狀态，fail表示失敗，done表示成功，process表示重新整理中。
        :type Status: str
        """
        self.PurgeType = None
        self.StartTime = None
        self.EndTime = None
        self.TaskId = None
        self.Offset = None
        self.Limit = None
        self.Keyword = None
        self.Status = None


    def _deserialize(self, params):
        self.PurgeType = params.get("PurgeType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TaskId = params.get("TaskId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Keyword = params.get("Keyword")
        self.Status = params.get("Status")


class DescribePurgeTasksResponse(AbstractModel):
    """DescribePurgeTasks返回參數結構體

    """

    def __init__(self):
        """
        :param PurgeLogs: 重新整理曆史記錄。
        :type PurgeLogs: list of PurgeTask
        :param TotalCount: 任務總數，用于分頁。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PurgeLogs = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PurgeLogs") is not None:
            self.PurgeLogs = []
            for item in params.get("PurgeLogs"):
                obj = PurgeTask()
                obj._deserialize(item)
                self.PurgeLogs.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DetailData(AbstractModel):
    """排序類型的數據結構

    """

    def __init__(self):
        """
        :param Name: 數據類型的名稱
        :type Name: str
        :param Value: 數據值
        :type Value: float
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class DomainBriefInfo(AbstractModel):
    """CDN域名簡要訊息。

    """

    def __init__(self):
        """
        :param ResourceId: 域名ID。
        :type ResourceId: str
        :param AppId: Top Cloud 賬号ID。
        :type AppId: int
        :param Domain: CDN加速域名。
        :type Domain: str
        :param Cname: 域名CName。
        :type Cname: str
        :param Status: 域名狀态，pending，rejected，processing， online，offline，deleted分别表示審核中，審核未通過，審核通過佈署中，已開啓，已關閉，已删除。
        :type Status: str
        :param ProjectId: 項目ID。
        :type ProjectId: int
        :param CreateTime: 域名創建時間。
        :type CreateTime: str
        :param UpdateTime: 域名更新時間。
        :type UpdateTime: str
        :param Origin: 源站配置詳情。
        :type Origin: :class:`taifucloudcloud.ecdn.v20191012.models.Origin`
        :param Disable: 域名封禁狀态，normal，overdue，quota，malicious，ddos，idle，unlicensed，capping，readonly分别表示 正常，欠費停服，試用客戶流量包耗盡，惡意用戶，ddos攻擊，無流量域名，未備案，頻寬封頂，只讀
        :type Disable: str
        :param Area: 加速區域，mainland，oversea或global。
        :type Area: str
        :param Readonly: 域名鎖定狀态，normal、global，分别表示未被鎖定、全球鎖定。
        :type Readonly: str
        """
        self.ResourceId = None
        self.AppId = None
        self.Domain = None
        self.Cname = None
        self.Status = None
        self.ProjectId = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Origin = None
        self.Disable = None
        self.Area = None
        self.Readonly = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.AppId = params.get("AppId")
        self.Domain = params.get("Domain")
        self.Cname = params.get("Cname")
        self.Status = params.get("Status")
        self.ProjectId = params.get("ProjectId")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        self.Disable = params.get("Disable")
        self.Area = params.get("Area")
        self.Readonly = params.get("Readonly")


class DomainData(AbstractModel):
    """排序類型數據結構

    """

    def __init__(self):
        """
        :param Resource: 域名
        :type Resource: str
        :param DetailData: 結果詳情
        :type DetailData: list of DetailData
        """
        self.Resource = None
        self.DetailData = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        if params.get("DetailData") is not None:
            self.DetailData = []
            for item in params.get("DetailData"):
                obj = DetailData()
                obj._deserialize(item)
                self.DetailData.append(obj)


class DomainDetailInfo(AbstractModel):
    """ECDN域名詳細配置訊息。

    """

    def __init__(self):
        """
        :param ResourceId: 域名ID。
        :type ResourceId: str
        :param AppId: Top Cloud 賬号ID。
        :type AppId: int
        :param Domain: 加速域名。
        :type Domain: str
        :param Cname: 域名CName。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Cname: str
        :param Status: 域名狀态，pending，rejected，processing， online，offline，deleted分别表示審核中，審核未通過，審核通過佈署中，已開啓，已關閉，已删除。
        :type Status: str
        :param ProjectId: 項目ID。
        :type ProjectId: int
        :param CreateTime: 域名創建時間。
        :type CreateTime: str
        :param UpdateTime: 域名更新時間。
        :type UpdateTime: str
        :param Origin: 源站配置。
        :type Origin: :class:`taifucloudcloud.ecdn.v20191012.models.Origin`
        :param IpFilter: IP黑白名單配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IpFilter: :class:`taifucloudcloud.ecdn.v20191012.models.IpFilter`
        :param IpFreqLimit: IP限頻配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IpFreqLimit: :class:`taifucloudcloud.ecdn.v20191012.models.IpFreqLimit`
        :param ResponseHeader: 源站響應頭部配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResponseHeader: :class:`taifucloudcloud.ecdn.v20191012.models.ResponseHeader`
        :param CacheKey: 節點快取配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CacheKey: :class:`taifucloudcloud.ecdn.v20191012.models.CacheKey`
        :param Cache: 快取規則配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Cache: :class:`taifucloudcloud.ecdn.v20191012.models.Cache`
        :param Https: Https配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Https: :class:`taifucloudcloud.ecdn.v20191012.models.Https`
        :param Disable: 域名封禁狀态，normal，overdue，quota，malicious，ddos，idle，unlicensed，capping，readonly分别表示 正常，欠費停服，試用客戶流量包耗盡，惡意用戶，ddos攻擊，無流量域名，未備案，頻寬封頂，只讀。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Disable: str
        :param ForceRedirect: 訪問協議強制跳轉配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ForceRedirect: :class:`taifucloudcloud.ecdn.v20191012.models.ForceRedirect`
        :param Area: 加速區域，mainland，overseas或global。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Area: str
        :param Readonly: 域名鎖定狀态，normal、global 分别表示未被鎖定，全球鎖定。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Readonly: str
        """
        self.ResourceId = None
        self.AppId = None
        self.Domain = None
        self.Cname = None
        self.Status = None
        self.ProjectId = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Origin = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.ResponseHeader = None
        self.CacheKey = None
        self.Cache = None
        self.Https = None
        self.Disable = None
        self.ForceRedirect = None
        self.Area = None
        self.Readonly = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.AppId = params.get("AppId")
        self.Domain = params.get("Domain")
        self.Cname = params.get("Cname")
        self.Status = params.get("Status")
        self.ProjectId = params.get("ProjectId")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        if params.get("IpFilter") is not None:
            self.IpFilter = IpFilter()
            self.IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self.IpFreqLimit = IpFreqLimit()
            self.IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        self.Disable = params.get("Disable")
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        self.Area = params.get("Area")
        self.Readonly = params.get("Readonly")


class DomainFilter(AbstractModel):
    """域名查詢時過濾條件。

    """

    def __init__(self):
        """
        :param Name: 過濾欄位名，支援的清單如下：
- origin：主源站。
- domain：域名。
- resourceId：域名id。
- status：域名狀态，online，offline，processing。
- disable：域名封禁狀态，normal，unlicensed。
- projectId：項目ID。
- fullUrlCache：全路徑快取，on或off。
- https：是否配置https，on，off或processing。
- originPullProtocol：回源協議類型，支援http，follow或https。
- area：加速區域，支援mainland，overseas或global。
        :type Name: str
        :param Value: 過濾欄位值。
        :type Value: list of str
        :param Fuzzy: 是否啓用模糊查詢，僅支援過濾欄位名爲origin，domain。
        :type Fuzzy: bool
        """
        self.Name = None
        self.Value = None
        self.Fuzzy = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        self.Fuzzy = params.get("Fuzzy")


class DomainLogs(AbstractModel):
    """域名日志訊息

    """

    def __init__(self):
        """
        :param StartTime: 日志起始時間。
        :type StartTime: str
        :param EndTime: 日志結束時間。
        :type EndTime: str
        :param LogPath: 日志下載路徑。
        :type LogPath: str
        """
        self.StartTime = None
        self.EndTime = None
        self.LogPath = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.LogPath = params.get("LogPath")


class EcdnData(AbstractModel):
    """訪問明細數據類型

    """

    def __init__(self):
        """
        :param Metrics: 查詢指定的指标名稱：Bandwidth，Flux，Request，Delay，狀态碼，LogBandwidth，LogFlux，LogRequest
        :type Metrics: list of str
        :param DetailData: 明細數據組合
        :type DetailData: list of TimestampData
        """
        self.Metrics = None
        self.DetailData = None


    def _deserialize(self, params):
        self.Metrics = params.get("Metrics")
        if params.get("DetailData") is not None:
            self.DetailData = []
            for item in params.get("DetailData"):
                obj = TimestampData()
                obj._deserialize(item)
                self.DetailData.append(obj)


class ForceRedirect(AbstractModel):
    """訪問協議強制跳轉配置。

    """

    def __init__(self):
        """
        :param Switch: 訪問協議強制跳轉配置開關，on或off。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Switch: str
        :param RedirectType: 強制跳轉訪問協議類型，支援http，https，分别表示請求強制跳轉http協議，請求強制跳轉https協議。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RedirectType: str
        :param RedirectStatusCode: 強制跳轉開啓時返回的http狀态碼，支援301或302。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RedirectStatusCode: int
        """
        self.Switch = None
        self.RedirectType = None
        self.RedirectStatusCode = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.RedirectType = params.get("RedirectType")
        self.RedirectStatusCode = params.get("RedirectStatusCode")


class HttpHeaderPathRule(AbstractModel):
    """分路徑的http頭部設置規則。

    """

    def __init__(self):
        """
        :param HeaderMode: http頭部設置方式，支援add，set或del，分别表示新增，設置或删除頭部。
請求頭部暫不支援set。
注意：此欄位可能返回 null，表示取不到有效值。
        :type HeaderMode: str
        :param HeaderName: http頭部名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type HeaderName: str
        :param HeaderValue: http頭部值。del時可不填寫該欄位。
注意：此欄位可能返回 null，表示取不到有效值。
        :type HeaderValue: str
        :param RuleType: 生效的url路徑規則類型，支援all，file，directory或path，分别表示全部路徑，文件後綴類型，目錄或絕對路徑生效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RuleType: str
        :param RulePaths: url路徑或文件類型清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RulePaths: list of str
        """
        self.HeaderMode = None
        self.HeaderName = None
        self.HeaderValue = None
        self.RuleType = None
        self.RulePaths = None


    def _deserialize(self, params):
        self.HeaderMode = params.get("HeaderMode")
        self.HeaderName = params.get("HeaderName")
        self.HeaderValue = params.get("HeaderValue")
        self.RuleType = params.get("RuleType")
        self.RulePaths = params.get("RulePaths")


class Https(AbstractModel):
    """域名https配置。

    """

    def __init__(self):
        """
        :param Switch: https配置開關，on或off。開啓https配置的域名在佈署中狀态，開關保持off。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Switch: str
        :param Http2: 是否開啓http2，on或off。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Http2: str
        :param OcspStapling: 是否開啓OCSP功能，on或off。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OcspStapling: str
        :param VerifyClient: 是否開啓用戶端證書校驗功能，on或off，開啓時必選上傳用戶端證書訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type VerifyClient: str
        :param CertInfo: 服務器證書配置訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertInfo: :class:`taifucloudcloud.ecdn.v20191012.models.ServerCert`
        :param ClientCertInfo: 用戶端證書配置訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClientCertInfo: :class:`taifucloudcloud.ecdn.v20191012.models.ClientCert`
        :param Spdy: 是否開啓Spdy，on或off。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Spdy: str
        :param SslStatus: https證書佈署狀态，closed，deploying，deployed，failed分别表示已關閉，佈署中，佈署成功，佈署失敗。不可作爲入參使用。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SslStatus: str
        """
        self.Switch = None
        self.Http2 = None
        self.OcspStapling = None
        self.VerifyClient = None
        self.CertInfo = None
        self.ClientCertInfo = None
        self.Spdy = None
        self.SslStatus = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Http2 = params.get("Http2")
        self.OcspStapling = params.get("OcspStapling")
        self.VerifyClient = params.get("VerifyClient")
        if params.get("CertInfo") is not None:
            self.CertInfo = ServerCert()
            self.CertInfo._deserialize(params.get("CertInfo"))
        if params.get("ClientCertInfo") is not None:
            self.ClientCertInfo = ClientCert()
            self.ClientCertInfo._deserialize(params.get("ClientCertInfo"))
        self.Spdy = params.get("Spdy")
        self.SslStatus = params.get("SslStatus")


class IpFilter(AbstractModel):
    """IP黑白名單。

    """

    def __init__(self):
        """
        :param Switch: IP黑白名單開關，on或off。
        :type Switch: str
        :param FilterType: IP黑白名單類型，whitelist或blacklist。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FilterType: str
        :param Filters: IP黑白名單清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Filters: list of str
        """
        self.Switch = None
        self.FilterType = None
        self.Filters = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.FilterType = params.get("FilterType")
        self.Filters = params.get("Filters")


class IpFreqLimit(AbstractModel):
    """IP限頻配置。

    """

    def __init__(self):
        """
        :param Switch: IP限頻配置開關，on或off。
        :type Switch: str
        :param Qps: 每秒請求數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Qps: int
        """
        self.Switch = None
        self.Qps = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Qps = params.get("Qps")


class Origin(AbstractModel):
    """源站配置。

    """

    def __init__(self):
        """
        :param Origins: 主源站清單，預設格式爲 ["ip1:port1", "ip2:port2"]。
支援在源站清單中配置權重，配置IP源站權重格式爲 ["ip1:port1:weight1", "ip2:port2:weight2"]。
        :type Origins: list of str
        :param OriginType: 主源站類型，支援domain，ip，分别表示域名源站，ip源站。
設置Origins時必須填寫。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OriginType: str
        :param ServerName: 回源時Host頭部值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ServerName: str
        :param OriginPullProtocol: 回源協議類型，支援http，follow，https，分别表示強制http回源，協議跟随回源，https回源。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OriginPullProtocol: str
        :param BackupOrigins: 備份源站清單。
        :type BackupOrigins: list of str
        :param BackupOriginType: 備份源站類型，同OriginType。
設置BackupOrigins時必須填寫。
注意：此欄位可能返回 null，表示取不到有效值。
        :type BackupOriginType: str
        """
        self.Origins = None
        self.OriginType = None
        self.ServerName = None
        self.OriginPullProtocol = None
        self.BackupOrigins = None
        self.BackupOriginType = None


    def _deserialize(self, params):
        self.Origins = params.get("Origins")
        self.OriginType = params.get("OriginType")
        self.ServerName = params.get("ServerName")
        self.OriginPullProtocol = params.get("OriginPullProtocol")
        self.BackupOrigins = params.get("BackupOrigins")
        self.BackupOriginType = params.get("BackupOriginType")


class PurgePathCacheRequest(AbstractModel):
    """PurgePathCache請求參數結構體

    """

    def __init__(self):
        """
        :param Paths: 要重新整理的目錄清單，必須包含協議頭部。
        :type Paths: list of str
        :param FlushType: 重新整理類型，flush 代表重新整理有更新的資源，delete 表示重新整理全部資源。
        :type FlushType: str
        """
        self.Paths = None
        self.FlushType = None


    def _deserialize(self, params):
        self.Paths = params.get("Paths")
        self.FlushType = params.get("FlushType")


class PurgePathCacheResponse(AbstractModel):
    """PurgePathCache返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 重新整理任務Id，前十位爲提交任務時的UTC時間。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class PurgeTask(AbstractModel):
    """重新整理任務日志詳情

    """

    def __init__(self):
        """
        :param TaskId: 重新整理任務ID。
        :type TaskId: str
        :param Url: 重新整理Url。
        :type Url: str
        :param Status: 重新整理任務狀态，fail表示失敗，done表示成功，process表示重新整理中。
        :type Status: str
        :param PurgeType: 重新整理類型，url表示url重新整理，path表示目錄重新整理。
        :type PurgeType: str
        :param FlushType: 重新整理資源方式，flush代表重新整理更新資源，delete代表重新整理全部資源。
        :type FlushType: str
        :param CreateTime: 重新整理任務提交時間
        :type CreateTime: str
        """
        self.TaskId = None
        self.Url = None
        self.Status = None
        self.PurgeType = None
        self.FlushType = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Url = params.get("Url")
        self.Status = params.get("Status")
        self.PurgeType = params.get("PurgeType")
        self.FlushType = params.get("FlushType")
        self.CreateTime = params.get("CreateTime")


class PurgeUrlsCacheRequest(AbstractModel):
    """PurgeUrlsCache請求參數結構體

    """

    def __init__(self):
        """
        :param Urls: 要重新整理的Url清單，必須包含協議頭部。
        :type Urls: list of str
        """
        self.Urls = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")


class PurgeUrlsCacheResponse(AbstractModel):
    """PurgeUrlsCache返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 重新整理任務Id，前十位爲提交任務時的UTC時間。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class Quota(AbstractModel):
    """重新整理用量及重新整理配額

    """

    def __init__(self):
        """
        :param Batch: 單次批次提交配額上限。
        :type Batch: int
        :param Total: 每日提交配額上限。
        :type Total: int
        :param Available: 每日剩餘的可提交配額。
        :type Available: int
        """
        self.Batch = None
        self.Total = None
        self.Available = None


    def _deserialize(self, params):
        self.Batch = params.get("Batch")
        self.Total = params.get("Total")
        self.Available = params.get("Available")


class ResourceData(AbstractModel):
    """查詢對象及其對應的訪問明細數據

    """

    def __init__(self):
        """
        :param Resource: 資源名稱，根據查詢條件不同分爲以下幾類：
具體域名：表示該域名明細數據
multiDomains：表示多域名匯總明細數據
項目 ID：指定項目查詢時，顯示爲項目 ID
all：賬号維度明細數據
        :type Resource: str
        :param EcdnData: 資源對應的數據明細
        :type EcdnData: :class:`taifucloudcloud.ecdn.v20191012.models.EcdnData`
        """
        self.Resource = None
        self.EcdnData = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        if params.get("EcdnData") is not None:
            self.EcdnData = EcdnData()
            self.EcdnData._deserialize(params.get("EcdnData"))


class ResponseHeader(AbstractModel):
    """自定義響應頭配置。

    """

    def __init__(self):
        """
        :param Switch: 自定義響應頭開關，on或off。
        :type Switch: str
        :param HeaderRules: 自定義響應頭規則數組。
注意：此欄位可能返回 null，表示取不到有效值。
        :type HeaderRules: list of HttpHeaderPathRule
        """
        self.Switch = None
        self.HeaderRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("HeaderRules") is not None:
            self.HeaderRules = []
            for item in params.get("HeaderRules"):
                obj = HttpHeaderPathRule()
                obj._deserialize(item)
                self.HeaderRules.append(obj)


class ServerCert(AbstractModel):
    """https服務端證書配置。

    """

    def __init__(self):
        """
        :param CertId: 服務器證書id，當證書爲Top Cloud 托管證書時必填。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertId: str
        :param CertName: 服務器證書名稱，當證書爲Top Cloud 托管證書時必填。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertName: str
        :param Certificate: 服務器證書訊息，上傳自有證書時必填，必須包含完整的證書鏈訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Certificate: str
        :param PrivateKey: 服務器金鑰訊息，上傳自有證書時必填。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PrivateKey: str
        :param ExpireTime: 證書過期時間。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param DeployTime: 證書頒發時間。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeployTime: str
        :param Message: 證書備注訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self.CertId = None
        self.CertName = None
        self.Certificate = None
        self.PrivateKey = None
        self.ExpireTime = None
        self.DeployTime = None
        self.Message = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.CertName = params.get("CertName")
        self.Certificate = params.get("Certificate")
        self.PrivateKey = params.get("PrivateKey")
        self.ExpireTime = params.get("ExpireTime")
        self.DeployTime = params.get("DeployTime")
        self.Message = params.get("Message")


class Sort(AbstractModel):
    """查詢結果排序條件。

    """

    def __init__(self):
        """
        :param Key: 排序欄位，當前支援：
createTime，域名創建時間
certExpireTime，證書過期時間
        :type Key: str
        :param Sequence: asc/desc，預設desc。
        :type Sequence: str
        """
        self.Key = None
        self.Sequence = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Sequence = params.get("Sequence")


class StartEcdnDomainRequest(AbstractModel):
    """StartEcdnDomain請求參數結構體

    """

    def __init__(self):
        """
        :param Domain: 待啓用域名。
        :type Domain: str
        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")


class StartEcdnDomainResponse(AbstractModel):
    """StartEcdnDomain返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopEcdnDomainRequest(AbstractModel):
    """StopEcdnDomain請求參數結構體

    """

    def __init__(self):
        """
        :param Domain: 待停用域名。
        :type Domain: str
        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")


class StopEcdnDomainResponse(AbstractModel):
    """StopEcdnDomain返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TimestampData(AbstractModel):
    """時間戳與其對應的數值

    """

    def __init__(self):
        """
        :param Time: 數據統計時間點，采用向前匯總模式
以 5 分鍾粒度爲例，13:35:00 時間點代表的統計數據區間爲 13:35:00 至 13:39:59
        :type Time: str
        :param Value: 數據值
        :type Value: list of float
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")


class UpdateDomainConfigRequest(AbstractModel):
    """UpdateDomainConfig請求參數結構體

    """

    def __init__(self):
        """
        :param Domain: 域名。
        :type Domain: str
        :param Origin: 源站配置。
        :type Origin: :class:`taifucloudcloud.ecdn.v20191012.models.Origin`
        :param ProjectId: 項目id。
        :type ProjectId: int
        :param IpFilter: IP黑白名單配置。
        :type IpFilter: :class:`taifucloudcloud.ecdn.v20191012.models.IpFilter`
        :param IpFreqLimit: IP限頻配置。
        :type IpFreqLimit: :class:`taifucloudcloud.ecdn.v20191012.models.IpFreqLimit`
        :param ResponseHeader: 源站響應頭部配置。
        :type ResponseHeader: :class:`taifucloudcloud.ecdn.v20191012.models.ResponseHeader`
        :param CacheKey: 節點快取配置。
        :type CacheKey: :class:`taifucloudcloud.ecdn.v20191012.models.CacheKey`
        :param Cache: 快取規則配置。
        :type Cache: :class:`taifucloudcloud.ecdn.v20191012.models.Cache`
        :param Https: Https配置。
        :type Https: :class:`taifucloudcloud.ecdn.v20191012.models.Https`
        :param ForceRedirect: 訪問協議強制跳轉配置。
        :type ForceRedirect: :class:`taifucloudcloud.ecdn.v20191012.models.ForceRedirect`
        :param Area: 域名加速區域，mainland，overseas或global，分别表示 境内加速，海外加速或全球加速。
        :type Area: str
        """
        self.Domain = None
        self.Origin = None
        self.ProjectId = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.ResponseHeader = None
        self.CacheKey = None
        self.Cache = None
        self.Https = None
        self.ForceRedirect = None
        self.Area = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        self.ProjectId = params.get("ProjectId")
        if params.get("IpFilter") is not None:
            self.IpFilter = IpFilter()
            self.IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self.IpFreqLimit = IpFreqLimit()
            self.IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        self.Area = params.get("Area")


class UpdateDomainConfigResponse(AbstractModel):
    """UpdateDomainConfig返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")