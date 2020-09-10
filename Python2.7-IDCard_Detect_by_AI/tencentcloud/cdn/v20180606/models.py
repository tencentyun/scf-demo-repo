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


class CacheOptResult(AbstractModel):
    """違規資源封禁/解封返回類型

    """

    def __init__(self):
        """
        :param SuccessUrls: 成功的url清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type SuccessUrls: list of str
        :param FailUrls: 失敗的url清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type FailUrls: list of str
        """
        self.SuccessUrls = None
        self.FailUrls = None


    def _deserialize(self, params):
        self.SuccessUrls = params.get("SuccessUrls")
        self.FailUrls = params.get("FailUrls")


class CdnData(AbstractModel):
    """訪問明細數據類型

    """

    def __init__(self):
        """
        :param Metric: 查詢指定的指标名稱：
flux：流量，單位爲 byte
bandwidth：頻寬，單位爲 bps
request：請求數，單位爲 次
fluxHitRate：流量命中率，單位爲 %
statusCode：狀态碼，返回 2XX、3XX、4XX、5XX 匯總數據，單位爲 個
2XX：返回 2XX 狀态碼匯總及各 2 開頭狀态碼數據，單位爲 個
3XX：返回 3XX 狀态碼匯總及各 3 開頭狀态碼數據，單位爲 個
4XX：返回 4XX 狀态碼匯總及各 4 開頭狀态碼數據，單位爲 個
5XX：返回 5XX 狀态碼匯總及各 5 開頭狀态碼數據，單位爲 個
或指定查詢的某一具體狀态碼
        :type Metric: str
        :param DetailData: 明細數據組合
        :type DetailData: list of TimestampData
        :param SummarizedData: 匯總數據組合
        :type SummarizedData: :class:`tencentcloud.cdn.v20180606.models.SummarizedData`
        """
        self.Metric = None
        self.DetailData = None
        self.SummarizedData = None


    def _deserialize(self, params):
        self.Metric = params.get("Metric")
        if params.get("DetailData") is not None:
            self.DetailData = []
            for item in params.get("DetailData"):
                obj = TimestampData()
                obj._deserialize(item)
                self.DetailData.append(obj)
        if params.get("SummarizedData") is not None:
            self.SummarizedData = SummarizedData()
            self.SummarizedData._deserialize(params.get("SummarizedData"))


class DescribeCdnDataRequest(AbstractModel):
    """DescribeCdnData請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 查詢起始時間，如：2018-09-04 10:40:00，返回結果大于等于指定時間
根據指定時間粒度不同，會進行向前歸整，如 2018-09-04 10:40:00 在按 1 小時的時間粒度查詢時，返回的第一個數據對應時間點爲 2018-09-04 10:00:00
起始時間與結束時間間隔小於等于 90 天
        :type StartTime: str
        :param EndTime: 查詢結束時間，如：2018-09-04 10:40:00，返回結果小於等于指定時間
根據指定時間粒度不同，會進行向前歸整，如 2018-09-04 10:40:00 在按 1 小時的時間粒度查詢時，返回的最後一個數據對應時間點爲 2018-09-04 10:00:00
起始時間與結束時間間隔小於等于 90 天
        :type EndTime: str
        :param Metric: 指定查詢指标，支援的類型有：
flux：流量，單位爲 byte
bandwidth：頻寬，單位爲 bps
request：請求數，單位爲 次
fluxHitRate：流量命中率，單位爲 %
statusCode：狀态碼，返回 2xx、3xx、4xx、5xx 匯總數據，單位爲 個
2xx：返回 2xx 狀态碼匯總及各 2 開頭狀态碼數據，單位爲 個
3xx：返回 3xx 狀态碼匯總及各 3 開頭狀态碼數據，單位爲 個
4xx：返回 4xx 狀态碼匯總及各 4 開頭狀态碼數據，單位爲 個
5xx：返回 5xx 狀态碼匯總及各 5 開頭狀态碼數據，單位爲 個
支援指定具體狀态碼查詢，若未産生過，則返回爲空
        :type Metric: str
        :param Domains: 指定查詢域名清單
最多可一次性查詢 30 個加速域名明細
        :type Domains: list of str
        :param Project: 指定要查詢的項目 ID，[前往檢視項目 ID](https://console.cloud.tencent.com/project)
未填充域名情況下，指定項目查詢，若填充了具體域名訊息，以域名爲主
        :type Project: int
        :param Interval: 時間粒度，支援以下幾種模式：
min：1 分鍾粒度，指定查詢區間 24 小時内（含 24 小時），可返回 1 分鍾粒度明細數據
5min：5 分鍾粒度，指定查詢區間 31 天内（含 31 天），可返回 5 分鍾粒度明細數據
hour：1 小時粒度，指定查詢區間 31 天内（含 31 天），可返回 1 小時粒度明細數據
day：天粒度，指定查詢區間大于 31 天，可返回天粒度明細數據
        :type Interval: str
        :param Detail: 多域名查詢時，預設（false)返回多個域名的匯總數據
可按需指定爲 true，返回每一個 Domain 的明細數據（statusCode 指标暫不支援）
        :type Detail: bool
        :param Isp: 指定運營商查詢，不填充表示查詢所有運營商
運營商編碼可以檢視 [運營商編碼映射](https://cloud.tencent.com/document/product/228/6316#.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84)
        :type Isp: int
        :param District: 指定省份查詢，不填充表示查詢所有省份
省份編碼可以檢視 [省份編碼映射](https://cloud.tencent.com/document/product/228/6316#.E7.9C.81.E4.BB.BD.E6.98.A0.E5.B0.84)
        :type District: int
        :param Protocol: 指定協議查詢，不填充表示查詢所有協議
all：所有協議
http：指定查詢 HTTP 對應指标
https：指定查詢 HTTPS 對應指标
        :type Protocol: str
        :param DataSource: 指定數據源查詢，白名單功能
        :type DataSource: str
        :param IpProtocol: 指定IP協議查詢，不填充表示查詢所有協議
all：所有協議
ipv4：指定查詢 ipv4對應指标
ipv6：指定查詢 ipv6 對應指标
        :type IpProtocol: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Metric = None
        self.Domains = None
        self.Project = None
        self.Interval = None
        self.Detail = None
        self.Isp = None
        self.District = None
        self.Protocol = None
        self.DataSource = None
        self.IpProtocol = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Metric = params.get("Metric")
        self.Domains = params.get("Domains")
        self.Project = params.get("Project")
        self.Interval = params.get("Interval")
        self.Detail = params.get("Detail")
        self.Isp = params.get("Isp")
        self.District = params.get("District")
        self.Protocol = params.get("Protocol")
        self.DataSource = params.get("DataSource")
        self.IpProtocol = params.get("IpProtocol")


class DescribeCdnDataResponse(AbstractModel):
    """DescribeCdnData返回參數結構體

    """

    def __init__(self):
        """
        :param Interval: 返回數據的時間粒度，查詢時指定：
min：1 分鍾粒度
5min：5 分鍾粒度
hour：1 小時粒度
day：天粒度
        :type Interval: str
        :param Data: 指定條件查詢得到的數據明細
        :type Data: list of ResourceData
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Interval = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Interval = params.get("Interval")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ResourceData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIpVisitRequest(AbstractModel):
    """DescribeIpVisit請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 查詢起始時間，如：2018-09-04 10:40:10，返回結果大于等于指定時間
根據指定時間粒度不同，會進行向前歸整，如 2018-09-04 10:40:10 在按 5 分鍾的時間粒度查詢時，返回的第一個數據對應時間點爲 2018-09-04 10:40:00
        :type StartTime: str
        :param EndTime: 查詢結束時間，如：2018-09-04 10:40:10，返回結果小於等于指定時間
根據指定時間粒度不同，會進行向前歸整，如 2018-09-04 10:40:10 在按 5 分鍾的時間粒度查詢時，返回的最後一個數據對應時間點爲 2018-09-04 10:40:00
        :type EndTime: str
        :param Domains: 指定查詢域名清單，最多可一次性查詢 30 個加速域名明細
        :type Domains: list of str
        :param Project: 指定要查詢的項目 ID，[前往檢視項目 ID](https://console.cloud.tencent.com/project)
未填充域名情況下，指定項目查詢，若填充了具體域名訊息，以域名爲主
        :type Project: int
        :param Interval: 時間粒度，支援以下幾種模式：
5min：5 分鍾粒度，查詢時間區間 24 小時内，預設返回 5 分鍾粒度活躍用戶數
day：天粒度，查詢時間區間大于 1 天時，預設返回天粒度活躍用戶數
        :type Interval: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Domains = None
        self.Project = None
        self.Interval = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Domains = params.get("Domains")
        self.Project = params.get("Project")
        self.Interval = params.get("Interval")


class DescribeIpVisitResponse(AbstractModel):
    """DescribeIpVisit返回參數結構體

    """

    def __init__(self):
        """
        :param Interval: 數據統計的時間粒度，支援5min,  day，分别表示5分鍾，1天的時間粒度。
        :type Interval: str
        :param Data: 各個資源的回源數據詳情。
        :type Data: list of ResourceData
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Interval = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Interval = params.get("Interval")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ResourceData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMapInfoRequest(AbstractModel):
    """DescribeMapInfo請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 映射查詢類别：
ips：運營商映射查詢
district：省份映射查詢
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")


class DescribeMapInfoResponse(AbstractModel):
    """DescribeMapInfo返回參數結構體

    """

    def __init__(self):
        """
        :param MapInfoList: 映射關系數組。
        :type MapInfoList: list of MapInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.MapInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MapInfoList") is not None:
            self.MapInfoList = []
            for item in params.get("MapInfoList"):
                obj = MapInfo()
                obj._deserialize(item)
                self.MapInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOriginDataRequest(AbstractModel):
    """DescribeOriginData請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 查詢起始時間，如：2018-09-04 10:40:00，返回結果大于等于指定時間
根據指定時間粒度不同，會進行向前歸整，如 2018-09-04 10:40:00 在按 1 小時的時間粒度查詢時，返回的第一個數據對應時間點爲 2018-09-04 10:00:00
起始時間與結束時間間隔小於等于 90 天
        :type StartTime: str
        :param EndTime: 查詢結束時間，如：2018-09-04 10:40:00，返回結果小於等于指定時間
根據指定時間粒度不同，會進行向前歸整，如 2018-09-04 10:40:00 在按 1 小時的時間粒度查詢時，返回的最後一個數據對應時間點爲 2018-09-04 10:00:00
起始時間與結束時間間隔小於等于 90 天
        :type EndTime: str
        :param Metric: 指定查詢指标，支援的類型有：
flux：回源流量，單位爲 byte
bandwidth：回源頻寬，單位爲 bps
request：回源請求數，單位爲 次
failRequest：回源失敗請求數，單位爲 次
failRate：回源失敗率，單位爲 %
statusCode：回源狀态碼，返回 2xx、3xx、4xx、5xx 匯總數據，單位爲 個
2xx：返回 2xx 回源狀态碼匯總及各 2 開頭回源狀态碼數據，單位爲 個
3xx：返回 3xx 回源狀态碼匯總及各 3 開頭回源狀态碼數據，單位爲 個
4xx：返回 4xx 回源狀态碼匯總及各 4 開頭回源狀态碼數據，單位爲 個
5xx：返回 5xx 回源狀态碼匯總及各 5 開頭回源狀态碼數據，單位爲 個
支援指定具體狀态碼查詢，若未産生過，則返回爲空
        :type Metric: str
        :param Domains: 指定查詢域名清單，最多可一次性查詢 30 個加速域名明細
        :type Domains: list of str
        :param Project: 指定要查詢的項目 ID，[前往檢視項目 ID](https://console.cloud.tencent.com/project)
未填充域名情況下，指定項目查詢，若填充了具體域名訊息，以域名爲主
        :type Project: int
        :param Interval: 時間粒度，支援以下幾種模式：
min：1 分鍾粒度，指定查詢區間 24 小時内（含 24 小時），可返回 1 分鍾粒度明細數據
5min：5 分鍾粒度，指定查詢區間 31 天内（含 31 天），可返回 5 分鍾粒度明細數據
hour：1 小時粒度，指定查詢區間 31 天内（含 31 天），可返回 1 小時粒度明細數據
day：天粒度，指定查詢區間大于 31 天，可返回天粒度明細數據
        :type Interval: str
        :param Detail: Domains 傳入多個時，預設（false)返回多個域名的匯總數據
可按需指定爲 true，返回每一個 Domain 的明細數據（statusCode 指标暫不支援）
        :type Detail: bool
        """
        self.StartTime = None
        self.EndTime = None
        self.Metric = None
        self.Domains = None
        self.Project = None
        self.Interval = None
        self.Detail = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Metric = params.get("Metric")
        self.Domains = params.get("Domains")
        self.Project = params.get("Project")
        self.Interval = params.get("Interval")
        self.Detail = params.get("Detail")


class DescribeOriginDataResponse(AbstractModel):
    """DescribeOriginData返回參數結構體

    """

    def __init__(self):
        """
        :param Interval: 數據統計的時間粒度，支援min, 5min, hour, day，分别表示1分鍾，5分鍾，1小時和1天的時間粒度。
        :type Interval: str
        :param Data: 各個資源的回源數據詳情。
        :type Data: list of ResourceOriginData
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Interval = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Interval = params.get("Interval")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ResourceOriginData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePayTypeRequest(AbstractModel):
    """DescribePayType請求參數結構體

    """


class DescribePayTypeResponse(AbstractModel):
    """DescribePayType返回參數結構體

    """

    def __init__(self):
        """
        :param PayType: 計費類型：
flux：流量計費
bandwidth：頻寬計費
        :type PayType: str
        :param BillingCycle: 計費週期：
day：日結計費
month：月結計費
        :type BillingCycle: str
        :param StatType: 計費方式：
monthMax：日峰值月平均計費，月結模式
day95：日 95 頻寬計費，月結模式
month95：月95頻寬計費，月結模式
sum：總流量計費，日結與月結均有流量計費模式
max：峰值頻寬計費，日結模式
        :type StatType: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PayType = None
        self.BillingCycle = None
        self.StatType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PayType = params.get("PayType")
        self.BillingCycle = params.get("BillingCycle")
        self.StatType = params.get("StatType")
        self.RequestId = params.get("RequestId")


class DisableCachesRequest(AbstractModel):
    """DisableCaches請求參數結構體

    """

    def __init__(self):
        """
        :param Urls: 需要禁用的 URL 清單
每次最多可提交 100 條，每日最多可提交 3000 條
        :type Urls: list of str
        """
        self.Urls = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")


class DisableCachesResponse(AbstractModel):
    """DisableCaches返回參數結構體

    """

    def __init__(self):
        """
        :param CacheOptResult: 提交結果
注意：此欄位可能返回 null，表示取不到有效值。
        :type CacheOptResult: :class:`tencentcloud.cdn.v20180606.models.CacheOptResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CacheOptResult = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CacheOptResult") is not None:
            self.CacheOptResult = CacheOptResult()
            self.CacheOptResult._deserialize(params.get("CacheOptResult"))
        self.RequestId = params.get("RequestId")


class EnableCachesRequest(AbstractModel):
    """EnableCaches請求參數結構體

    """

    def __init__(self):
        """
        :param Urls: 解封 URL 清單
        :type Urls: list of str
        """
        self.Urls = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")


class EnableCachesResponse(AbstractModel):
    """EnableCaches返回參數結構體

    """

    def __init__(self):
        """
        :param CacheOptResult: 結果清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type CacheOptResult: :class:`tencentcloud.cdn.v20180606.models.CacheOptResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CacheOptResult = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CacheOptResult") is not None:
            self.CacheOptResult = CacheOptResult()
            self.CacheOptResult._deserialize(params.get("CacheOptResult"))
        self.RequestId = params.get("RequestId")


class GetDisableRecordsRequest(AbstractModel):
    """GetDisableRecords請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 開始時間
        :type StartTime: str
        :param EndTime: 結束時間
        :type EndTime: str
        :param Url: 指定 URL 查詢
        :type Url: str
        :param Status: URL 當前狀态
disable：當前仍爲禁用狀态，訪問返回 403
enable：當前爲可用狀态，已解禁，可正常訪問
        :type Status: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Url = None
        self.Status = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Url = params.get("Url")
        self.Status = params.get("Status")


class GetDisableRecordsResponse(AbstractModel):
    """GetDisableRecords返回參數結構體

    """

    def __init__(self):
        """
        :param UrlRecordList: 封禁曆史記錄
注意：此欄位可能返回 null，表示取不到有效值。
        :type UrlRecordList: list of UrlRecord
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.UrlRecordList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UrlRecordList") is not None:
            self.UrlRecordList = []
            for item in params.get("UrlRecordList"):
                obj = UrlRecord()
                obj._deserialize(item)
                self.UrlRecordList.append(obj)
        self.RequestId = params.get("RequestId")


class ListTopDataRequest(AbstractModel):
    """ListTopData請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 查詢起始日期，如：2018-09-09 00:00:00
        :type StartTime: str
        :param EndTime: 查詢結束日期，如：2018-09-10 00:00:00
        :type EndTime: str
        :param Metric: 排序對象，支援以下幾種形式：
Url：訪問 URL 排序，帶參數統計，支援的 Filter 爲 flux、request（白名單功能）
Path：訪問 URL 排序，不帶參數統計，支援的 Filter 爲 flux、request
District：省份排序，支援的 Filter 爲 flux、request
Isp：運營商排序，支援的 Filter 爲 flux、request
Host：域名訪問數據排序，支援的 Filter 爲：flux, request, bandwidth, fluxHitRate, 2XX, 3XX, 4XX, 5XX，具體狀态碼統計
originHost：域名回源數據排序，支援的 Filter 爲 flux， request，bandwidth，origin_2XX，origin_3XX，oringin_4XX，origin_5XX，具體回源狀态碼統計
        :type Metric: str
        :param Filter: 排序使用的指标名稱：
flux：Metric 爲 host 時指代訪問流量，originHost 時指代回源流量
bandwidth：Metric 爲 host 時指代訪問頻寬，originHost 時指代回源頻寬
request：Metric 爲 host 時指代訪問請求數，originHost 時指代回源請求數
fluxHitRate：平均流量命中率
2XX：訪問 2XX 狀态碼
3XX：訪問 3XX 狀态碼
4XX：訪問 4XX 狀态碼
5XX：訪問 5XX 狀态碼
origin_2XX：回源 2XX 狀态碼
origin_3XX：回源 3XX 狀态碼
origin_4XX：回源 4XX 狀态碼
origin_5XX：回源 5XX 狀态碼
statusCode：指定訪問狀态碼統計，在 Code 參數中填充指定狀态碼
OriginStatusCode：指定回源狀态碼統計，在 Code 參數中填充指定狀态碼
        :type Filter: str
        :param Domains: 指定查詢域名清單，最多可一次性查詢 30 個加速域名明細
        :type Domains: list of str
        :param Project: 指定要查詢的項目 ID，[前往檢視項目 ID](https://console.cloud.tencent.com/project)
未填充域名情況下，指定項目查詢，若填充了具體域名訊息，以域名爲主
        :type Project: int
        :param Detail: 多域名查詢時，預設（false)返回所有域名匯總排序結果
Metric 爲 Url、Path、District、Isp，Filter 爲 flux、reqeust 時，可設置爲 true，返回每一個 Domain 的排序數據
        :type Detail: bool
        :param Code: Filter 爲 statusCode、OriginStatusCode 時，填充指定狀态碼查詢排序結果
        :type Code: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Metric = None
        self.Filter = None
        self.Domains = None
        self.Project = None
        self.Detail = None
        self.Code = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Metric = params.get("Metric")
        self.Filter = params.get("Filter")
        self.Domains = params.get("Domains")
        self.Project = params.get("Project")
        self.Detail = params.get("Detail")
        self.Code = params.get("Code")


class ListTopDataResponse(AbstractModel):
    """ListTopData返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 各個資源的Top 訪問數據詳情。
        :type Data: list of TopData
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TopData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class MapInfo(AbstractModel):
    """名稱與ID映射關系

    """

    def __init__(self):
        """
        :param Id: 對象 Id
        :type Id: int
        :param Name: 對象名稱
        :type Name: str
        """
        self.Id = None
        self.Name = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")


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
        :param CdnData: 資源對應的數據明細
        :type CdnData: list of CdnData
        """
        self.Resource = None
        self.CdnData = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        if params.get("CdnData") is not None:
            self.CdnData = []
            for item in params.get("CdnData"):
                obj = CdnData()
                obj._deserialize(item)
                self.CdnData.append(obj)


class ResourceOriginData(AbstractModel):
    """查詢對象及其對應的回源明細數據

    """

    def __init__(self):
        """
        :param Resource: 資源名稱，根據查詢條件不同分爲以下幾類：
具體域名：表示該域名明細數據
multiDomains：表示多域名匯總明細數據
項目 ID：指定項目查詢時，顯示爲項目 ID
all：賬号維度明細數據
        :type Resource: str
        :param OriginData: 回源數據詳情
        :type OriginData: list of CdnData
        """
        self.Resource = None
        self.OriginData = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        if params.get("OriginData") is not None:
            self.OriginData = []
            for item in params.get("OriginData"):
                obj = CdnData()
                obj._deserialize(item)
                self.OriginData.append(obj)


class SummarizedData(AbstractModel):
    """明細數據的匯總值，各指标根據其特性不同擁有不同匯總方式

    """

    def __init__(self):
        """
        :param Name: 匯總方式，存在以下幾種：
sum：累加求和
max：最大值，頻寬模式下，采用 5 分鍾粒度匯總數據，計算峰值頻寬
avg：平均值
        :type Name: str
        :param Value: 匯總後的數據值
        :type Value: float
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class TimestampData(AbstractModel):
    """時間戳與其對應的數值

    """

    def __init__(self):
        """
        :param Time: 數據統計時間點，采用向前匯總模式
以 5 分鍾粒度爲例，13:35:00 時間點代表的統計數據區間爲 13:35:00 至 13:39:59
        :type Time: str
        :param Value: 數據值
        :type Value: float
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")


class TopData(AbstractModel):
    """排序類型數據結構

    """

    def __init__(self):
        """
        :param Resource: 資源名稱，根據查詢條件不同分爲以下幾類：
具體域名：表示該域名明細數據
multiDomains：表示多域名匯總明細數據
項目 ID：指定項目查詢時，顯示爲項目 ID
all：賬号維度明細數據
        :type Resource: str
        :param DetailData: 排序結果詳情
        :type DetailData: list of TopDetailData
        """
        self.Resource = None
        self.DetailData = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        if params.get("DetailData") is not None:
            self.DetailData = []
            for item in params.get("DetailData"):
                obj = TopDetailData()
                obj._deserialize(item)
                self.DetailData.append(obj)


class TopDetailData(AbstractModel):
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


class UrlRecord(AbstractModel):
    """封禁url的詳細訊息

    """

    def __init__(self):
        """
        :param Status: 狀态(disable表示封禁，enable表示解封)
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: str
        :param RealUrl: 對應的url
注意：此欄位可能返回 null，表示取不到有效值。
        :type RealUrl: str
        :param CreateTime: 創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 更新時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.Status = None
        self.RealUrl = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RealUrl = params.get("RealUrl")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")