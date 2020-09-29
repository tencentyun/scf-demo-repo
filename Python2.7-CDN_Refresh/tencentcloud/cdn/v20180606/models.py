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


class AddCdnDomainRequest(AbstractModel):
    """AddCdnDomain請求參數結構體

    """

    def __init__(self):
        """
        :param Domain: 域名
        :type Domain: str
        :param ServiceType: 加速域名業務類型
web：靜态加速
download：下載加速
media：流媒體點播加速
        :type ServiceType: str
        :param Origin: 源站配置
        :type Origin: :class:`taifucloudcloud.cdn.v20180606.models.Origin`
        :param ProjectId: 項目 ID，預設爲 0，代表【預設項目】
        :type ProjectId: int
        :param IpFilter: IP 黑白名單配置
        :type IpFilter: :class:`taifucloudcloud.cdn.v20180606.models.IpFilter`
        :param IpFreqLimit: IP 限頻配置
        :type IpFreqLimit: :class:`taifucloudcloud.cdn.v20180606.models.IpFreqLimit`
        :param StatusCodeCache: 狀态碼快取配置
        :type StatusCodeCache: :class:`taifucloudcloud.cdn.v20180606.models.StatusCodeCache`
        :param Compression: 智慧壓縮配置
        :type Compression: :class:`taifucloudcloud.cdn.v20180606.models.Compression`
        :param BandwidthAlert: 頻寬封頂配置
        :type BandwidthAlert: :class:`taifucloudcloud.cdn.v20180606.models.BandwidthAlert`
        :param RangeOriginPull: Range 回源配置
        :type RangeOriginPull: :class:`taifucloudcloud.cdn.v20180606.models.RangeOriginPull`
        :param FollowRedirect: 301/302 回源跟随配置。
        :type FollowRedirect: :class:`taifucloudcloud.cdn.v20180606.models.FollowRedirect`
        :param ErrorPage: 錯誤碼重定向配置（功能灰度中，尚未全量）
        :type ErrorPage: :class:`taifucloudcloud.cdn.v20180606.models.ErrorPage`
        :param RequestHeader: 請求頭部配置
        :type RequestHeader: :class:`taifucloudcloud.cdn.v20180606.models.RequestHeader`
        :param ResponseHeader: 響應頭部配置
        :type ResponseHeader: :class:`taifucloudcloud.cdn.v20180606.models.ResponseHeader`
        :param DownstreamCapping: 下載速度配置
        :type DownstreamCapping: :class:`taifucloudcloud.cdn.v20180606.models.DownstreamCapping`
        :param CacheKey: 節點快取鍵配置
        :type CacheKey: :class:`taifucloudcloud.cdn.v20180606.models.CacheKey`
        :param ResponseHeaderCache: 頭部快取配置
        :type ResponseHeaderCache: :class:`taifucloudcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param VideoSeek: 視訊拖拽配置
        :type VideoSeek: :class:`taifucloudcloud.cdn.v20180606.models.VideoSeek`
        :param Cache: 快取過期時間配置
        :type Cache: :class:`taifucloudcloud.cdn.v20180606.models.Cache`
        :param OriginPullOptimization: 跨國鏈路優化配置
        :type OriginPullOptimization: :class:`taifucloudcloud.cdn.v20180606.models.OriginPullOptimization`
        :param Https: Https 加速配置
        :type Https: :class:`taifucloudcloud.cdn.v20180606.models.Https`
        :param Authentication: 時間戳防盜鏈配置
        :type Authentication: :class:`taifucloudcloud.cdn.v20180606.models.Authentication`
        :param Seo: SEO 優化配置
        :type Seo: :class:`taifucloudcloud.cdn.v20180606.models.Seo`
        :param ForceRedirect: 訪問協議強制跳轉配置
        :type ForceRedirect: :class:`taifucloudcloud.cdn.v20180606.models.ForceRedirect`
        :param Referer: Referer 防盜鏈配置
        :type Referer: :class:`taifucloudcloud.cdn.v20180606.models.Referer`
        :param MaxAge: 浏覽器快取配置（功能灰度中，尚未全量）
        :type MaxAge: :class:`taifucloudcloud.cdn.v20180606.models.MaxAge`
        :param Ipv6: Ipv6 配置（功能灰度中，尚未全量）
        :type Ipv6: :class:`taifucloudcloud.cdn.v20180606.models.Ipv6`
        :param SpecificConfig: 地域屬性特殊配置
适用於域名境内加速、境外加速配置不一緻場景
        :type SpecificConfig: :class:`taifucloudcloud.cdn.v20180606.models.SpecificConfig`
        :param Area: 域名加速區域
mainland： 境内加速
overseas： 境外加速
global：全球加速
使用 境外加速、全球加速時，需要先開通 境外加速服務
        :type Area: str
        :param OriginPullTimeout: 回源超時配置
        :type OriginPullTimeout: :class:`taifucloudcloud.cdn.v20180606.models.OriginPullTimeout`
        """
        self.Domain = None
        self.ServiceType = None
        self.Origin = None
        self.ProjectId = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.StatusCodeCache = None
        self.Compression = None
        self.BandwidthAlert = None
        self.RangeOriginPull = None
        self.FollowRedirect = None
        self.ErrorPage = None
        self.RequestHeader = None
        self.ResponseHeader = None
        self.DownstreamCapping = None
        self.CacheKey = None
        self.ResponseHeaderCache = None
        self.VideoSeek = None
        self.Cache = None
        self.OriginPullOptimization = None
        self.Https = None
        self.Authentication = None
        self.Seo = None
        self.ForceRedirect = None
        self.Referer = None
        self.MaxAge = None
        self.Ipv6 = None
        self.SpecificConfig = None
        self.Area = None
        self.OriginPullTimeout = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.ServiceType = params.get("ServiceType")
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
        if params.get("StatusCodeCache") is not None:
            self.StatusCodeCache = StatusCodeCache()
            self.StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("BandwidthAlert") is not None:
            self.BandwidthAlert = BandwidthAlert()
            self.BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("RangeOriginPull") is not None:
            self.RangeOriginPull = RangeOriginPull()
            self.RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("FollowRedirect") is not None:
            self.FollowRedirect = FollowRedirect()
            self.FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ErrorPage") is not None:
            self.ErrorPage = ErrorPage()
            self.ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("RequestHeader") is not None:
            self.RequestHeader = RequestHeader()
            self.RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("DownstreamCapping") is not None:
            self.DownstreamCapping = DownstreamCapping()
            self.DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("ResponseHeaderCache") is not None:
            self.ResponseHeaderCache = ResponseHeaderCache()
            self.ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("VideoSeek") is not None:
            self.VideoSeek = VideoSeek()
            self.VideoSeek._deserialize(params.get("VideoSeek"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("OriginPullOptimization") is not None:
            self.OriginPullOptimization = OriginPullOptimization()
            self.OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("Authentication") is not None:
            self.Authentication = Authentication()
            self.Authentication._deserialize(params.get("Authentication"))
        if params.get("Seo") is not None:
            self.Seo = Seo()
            self.Seo._deserialize(params.get("Seo"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Referer") is not None:
            self.Referer = Referer()
            self.Referer._deserialize(params.get("Referer"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6()
            self.Ipv6._deserialize(params.get("Ipv6"))
        if params.get("SpecificConfig") is not None:
            self.SpecificConfig = SpecificConfig()
            self.SpecificConfig._deserialize(params.get("SpecificConfig"))
        self.Area = params.get("Area")
        if params.get("OriginPullTimeout") is not None:
            self.OriginPullTimeout = OriginPullTimeout()
            self.OriginPullTimeout._deserialize(params.get("OriginPullTimeout"))


class AddCdnDomainResponse(AbstractModel):
    """AddCdnDomain返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AdvanceCacheRule(AbstractModel):
    """快取配置高級版本規則

    """

    def __init__(self):
        """
        :param CacheType: 規則類型：
all：所有文件生效
file：指定文件後綴生效
directory：指定路徑生效
path：指定絕對路徑生效
default：源站未返回 max-age 情況下的快取規則
注意：此欄位可能返回 null，表示取不到有效值。
        :type CacheType: str
        :param CacheContents: 對應類型下的比對内容：
all 時填充 *
file 時填充後綴名，如 jpg、txt
directory 時填充路徑，如 /xxx/test/
path 時填充絕對路徑，如 /xxx/test.html
default 時填充 "no max-age"
注意：此欄位可能返回 null，表示取不到有效值。
        :type CacheContents: list of str
        :param CacheTime: 快取過期時間
單位爲秒，最大可設置爲 365 天
注意：此欄位可能返回 null，表示取不到有效值。
        :type CacheTime: int
        """
        self.CacheType = None
        self.CacheContents = None
        self.CacheTime = None


    def _deserialize(self, params):
        self.CacheType = params.get("CacheType")
        self.CacheContents = params.get("CacheContents")
        self.CacheTime = params.get("CacheTime")


class AdvancedCache(AbstractModel):
    """快取過期配置高級版（功能灰度中，尚未全量）
    注意：該版本不支援設置首頁快取規則

    """

    def __init__(self):
        """
        :param CacheRules: 快取過期規則
注意：此欄位可能返回 null，表示取不到有效值。
        :type CacheRules: list of AdvanceCacheRule
        :param IgnoreCacheControl: 強制快取配置
on：開啓
off：關閉
開啓時，源站返回 no-cache、no-store 頭部時，仍按照快取過期規則進行節點快取
預設爲關閉狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type IgnoreCacheControl: str
        :param IgnoreSetCookie: 忽略源站的 Set-Cookie 頭部
on：開啓
off：關閉
預設爲關閉狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type IgnoreSetCookie: str
        """
        self.CacheRules = None
        self.IgnoreCacheControl = None
        self.IgnoreSetCookie = None


    def _deserialize(self, params):
        if params.get("CacheRules") is not None:
            self.CacheRules = []
            for item in params.get("CacheRules"):
                obj = AdvanceCacheRule()
                obj._deserialize(item)
                self.CacheRules.append(obj)
        self.IgnoreCacheControl = params.get("IgnoreCacheControl")
        self.IgnoreSetCookie = params.get("IgnoreSetCookie")


class Authentication(AbstractModel):
    """時間戳防盜鏈配置

    """

    def __init__(self):
        """
        :param Switch: 防盜鏈配置開關
on：開啓
off：關閉
開啓時必須且只配置一種模式，其餘模式需要設置爲 null
        :type Switch: str
        :param TypeA: 時間戳防盜鏈模式 A 配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type TypeA: :class:`taifucloudcloud.cdn.v20180606.models.AuthenticationTypeA`
        :param TypeB: 時間戳防盜鏈模式 B 配置（模式 B 後台升級中，暫時不支援配置）
注意：此欄位可能返回 null，表示取不到有效值。
        :type TypeB: :class:`taifucloudcloud.cdn.v20180606.models.AuthenticationTypeB`
        :param TypeC: 時間戳防盜鏈模式 C 配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type TypeC: :class:`taifucloudcloud.cdn.v20180606.models.AuthenticationTypeC`
        :param TypeD: 時間戳防盜鏈模式 D 配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type TypeD: :class:`taifucloudcloud.cdn.v20180606.models.AuthenticationTypeD`
        """
        self.Switch = None
        self.TypeA = None
        self.TypeB = None
        self.TypeC = None
        self.TypeD = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("TypeA") is not None:
            self.TypeA = AuthenticationTypeA()
            self.TypeA._deserialize(params.get("TypeA"))
        if params.get("TypeB") is not None:
            self.TypeB = AuthenticationTypeB()
            self.TypeB._deserialize(params.get("TypeB"))
        if params.get("TypeC") is not None:
            self.TypeC = AuthenticationTypeC()
            self.TypeC._deserialize(params.get("TypeC"))
        if params.get("TypeD") is not None:
            self.TypeD = AuthenticationTypeD()
            self.TypeD._deserialize(params.get("TypeD"))


class AuthenticationTypeA(AbstractModel):
    """時間戳防盜鏈模式 A 配置
    時間戳防盜鏈模式 A 的訪問 URL 格式爲：http://DomainName/Filename?sign=timestamp-rand-uid-md5hash
    其中 timestamp 爲十進制 UNIX 時間戳；
    rand 爲随機字串，0 ~ 100 位大小寫字母與數字組成；
    uid 爲 0；
    md5hash：MD5（文件路徑-timestamp-rand-uid-自定義金鑰）

    """

    def __init__(self):
        """
        :param SecretKey: 計算簽名的金鑰
僅允許大小寫字母與數字，長度 6~32 位
注意：此欄位可能返回 null，表示取不到有效值。
        :type SecretKey: str
        :param SignParam: 簽名參數名設置
僅允許大小寫字母、數字或下劃線，長度 1~100 位，不能以數字開頭
        :type SignParam: str
        :param ExpireTime: 簽名過期時間設置
單位爲秒，最大可設置爲 31536000
        :type ExpireTime: int
        :param FileExtensions: 鑒權/不做鑒權的文件擴展名清單設置
如果包含字元 *  則表示所有文件
        :type FileExtensions: list of str
        :param FilterType: whitelist：白名單，表示對除了 FileExtensions 清單之外的所有類型進行鑒權
blacklist：黑名單，表示僅對 FileExtensions 中的類型進行鑒權
        :type FilterType: str
        """
        self.SecretKey = None
        self.SignParam = None
        self.ExpireTime = None
        self.FileExtensions = None
        self.FilterType = None


    def _deserialize(self, params):
        self.SecretKey = params.get("SecretKey")
        self.SignParam = params.get("SignParam")
        self.ExpireTime = params.get("ExpireTime")
        self.FileExtensions = params.get("FileExtensions")
        self.FilterType = params.get("FilterType")


class AuthenticationTypeB(AbstractModel):
    """時間戳防盜鏈模式 B 配置（B 模式正在進行平台升級，暫不支援配置）

    """

    def __init__(self):
        """
        :param SecretKey: 計算簽名的金鑰
僅允許大小寫字母與數字，長度 6~32 位
注意：此欄位可能返回 null，表示取不到有效值。
        :type SecretKey: str
        :param ExpireTime: 簽名過期時間設置
單位爲秒，最大可設置爲 31536000
        :type ExpireTime: int
        :param FileExtensions: 鑒權/不做鑒權的文件擴展名清單設置
如果包含字元 *  則表示所有文件
        :type FileExtensions: list of str
        :param FilterType: whitelist：白名單，表示對除了 FileExtensions 清單之外的所有類型進行鑒權
blacklist：黑名單，表示僅對 FileExtensions 中的類型進行鑒權
        :type FilterType: str
        """
        self.SecretKey = None
        self.ExpireTime = None
        self.FileExtensions = None
        self.FilterType = None


    def _deserialize(self, params):
        self.SecretKey = params.get("SecretKey")
        self.ExpireTime = params.get("ExpireTime")
        self.FileExtensions = params.get("FileExtensions")
        self.FilterType = params.get("FilterType")


class AuthenticationTypeC(AbstractModel):
    """時間戳防盜鏈模式 C 配置
    時間戳防盜鏈模式 C 的訪問 URL 格式爲：http://DomainName/md5hash/timestamp/FileName
    其中 timestamp 爲十六進制 UNIX 時間戳；
    md5hash：MD5（自定義金鑰 + 文件路徑 + timestamp）

    """

    def __init__(self):
        """
        :param SecretKey: 計算簽名的金鑰
僅允許大小寫字母與數字，長度 6~32 位
注意：此欄位可能返回 null，表示取不到有效值。
        :type SecretKey: str
        :param ExpireTime: 簽名過期時間設置
單位爲秒，最大可設置爲 31536000
        :type ExpireTime: int
        :param FileExtensions: 鑒權/不做鑒權的文件擴展名清單設置
如果包含字元 *  則表示所有文件
        :type FileExtensions: list of str
        :param FilterType: whitelist：白名單，表示對除了 FileExtensions 清單之外的所有類型進行鑒權
blacklist：黑名單，表示僅對 FileExtensions 中的類型進行鑒權
        :type FilterType: str
        """
        self.SecretKey = None
        self.ExpireTime = None
        self.FileExtensions = None
        self.FilterType = None


    def _deserialize(self, params):
        self.SecretKey = params.get("SecretKey")
        self.ExpireTime = params.get("ExpireTime")
        self.FileExtensions = params.get("FileExtensions")
        self.FilterType = params.get("FilterType")


class AuthenticationTypeD(AbstractModel):
    """時間戳防盜鏈模式 D 配置
    時間戳防盜鏈模式 D 的訪問 URL 格式爲：http://DomainName/FileName?sign=md5hash&t=timestamp
    其中 timestamp 爲十進制或十六進制 UNIX 時間戳；
    md5hash：MD5（自定義金鑰 + 文件路徑 + timestamp）

    """

    def __init__(self):
        """
        :param SecretKey: 計算簽名的金鑰
僅允許大小寫字母與數字，長度 6~32 位
注意：此欄位可能返回 null，表示取不到有效值。
        :type SecretKey: str
        :param ExpireTime: 簽名過期時間設置
單位爲秒，最大可設置爲 31536000
        :type ExpireTime: int
        :param FileExtensions: 鑒權/不做鑒權的文件擴展名清單設置
如果包含字元 *  則表示所有文件
        :type FileExtensions: list of str
        :param FilterType: whitelist：白名單，表示對除了 FileExtensions 清單之外的所有類型進行鑒權
blacklist：黑名單，表示僅對 FileExtensions 中的類型進行鑒權
        :type FilterType: str
        :param SignParam: 簽名參數名設置
僅允許大小寫字母、數字或下劃線，長度 1~100 位，不能以數字開頭
        :type SignParam: str
        :param TimeParam: 時間戳參數名設置
僅允許大小寫字母、數字或下劃線，長度 1~100 位，不能以數字開頭
        :type TimeParam: str
        :param TimeFormat: 時間戳進制設置
dec：十進制
hex：十六進制
        :type TimeFormat: str
        """
        self.SecretKey = None
        self.ExpireTime = None
        self.FileExtensions = None
        self.FilterType = None
        self.SignParam = None
        self.TimeParam = None
        self.TimeFormat = None


    def _deserialize(self, params):
        self.SecretKey = params.get("SecretKey")
        self.ExpireTime = params.get("ExpireTime")
        self.FileExtensions = params.get("FileExtensions")
        self.FilterType = params.get("FilterType")
        self.SignParam = params.get("SignParam")
        self.TimeParam = params.get("TimeParam")
        self.TimeFormat = params.get("TimeFormat")


class AwsPrivateAccess(AbstractModel):
    """s3源站回源鑒權。

    """

    def __init__(self):
        """
        :param Switch: 開關，on/off。
        :type Switch: str
        :param AccessKey: 訪問ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AccessKey: str
        :param SecretKey: 金鑰。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SecretKey: str
        """
        self.Switch = None
        self.AccessKey = None
        self.SecretKey = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.AccessKey = params.get("AccessKey")
        self.SecretKey = params.get("SecretKey")


class BandwidthAlert(AbstractModel):
    """頻寬封頂配置，預設爲關閉狀态

    """

    def __init__(self):
        """
        :param Switch: 頻寬封頂配置開關
on：開啓
off：關閉
        :type Switch: str
        :param BpsThreshold: 頻寬封頂阈值，單位爲bps
注意：此欄位可能返回 null，表示取不到有效值。
        :type BpsThreshold: int
        :param CounterMeasure: 達到阈值後的操作
RESOLVE_DNS_TO_ORIGIN：直接回源，僅自有源站域名支援
RETURN_404：全部請求返回 404
注意：此欄位可能返回 null，表示取不到有效值。
        :type CounterMeasure: str
        :param LastTriggerTime: 上次觸發頻寬封頂阈值的時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type LastTriggerTime: str
        """
        self.Switch = None
        self.BpsThreshold = None
        self.CounterMeasure = None
        self.LastTriggerTime = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BpsThreshold = params.get("BpsThreshold")
        self.CounterMeasure = params.get("CounterMeasure")
        self.LastTriggerTime = params.get("LastTriggerTime")


class BriefDomain(AbstractModel):
    """域名基礎配置訊息，含 CNAME、狀态、業務類型、加速區域、創建時間、更新時間、源站配置等。

    """

    def __init__(self):
        """
        :param ResourceId: 域名 ID
        :type ResourceId: str
        :param AppId: Top Cloud 賬號 ID
        :type AppId: int
        :param Domain: 加速域名
        :type Domain: str
        :param Cname: 域名對應的 CNAME 網址
        :type Cname: str
        :param Status: 加速服務狀态
rejected：域名審核未通過，域名備案過期/被注銷導緻
processing：部署中
online：已啓動
offline：已關閉
        :type Status: str
        :param ProjectId: 項目 ID，可前往Top Cloud 項目管理頁面檢視
        :type ProjectId: int
        :param ServiceType: 域名業務類型
web：靜态加速
download：下載加速
media：流媒體點播加速
        :type ServiceType: str
        :param CreateTime: 域名創建時間
        :type CreateTime: str
        :param UpdateTime: 域名更新時間
        :type UpdateTime: str
        :param Origin: 源站配置詳情
        :type Origin: :class:`taifucloudcloud.cdn.v20180606.models.Origin`
        :param Disable: 域名封禁狀态
normal：正常狀态
overdue：賬號欠費導緻域名關閉，儲值完成後可自行啓動加速服務
malicious：域名出現惡意行爲，強制關閉加速服務
ddos：域名被大規模 DDoS 攻擊，關閉加速服務
idle：域名超過 90 天内無任何操作、數據産生，判定爲不活躍域名自動關閉加速服務，可自行啓動加速服務
unlicensed：域名未備案/備案注銷，自動關閉加速服務，備案完成後可自行啓動加速服務
capping：觸發配置的頻寬阈值上限
readonly：域名存在特殊配置，被鎖定
        :type Disable: str
        :param Area: 加速區域
mainland： 境内加速
overseas： 境外加速
global：全球加速
        :type Area: str
        :param Readonly: 域名鎖定狀态
normal：未鎖定
mainland： 境内鎖定
overseas： 境外鎖定
global：全球鎖定
        :type Readonly: str
        """
        self.ResourceId = None
        self.AppId = None
        self.Domain = None
        self.Cname = None
        self.Status = None
        self.ProjectId = None
        self.ServiceType = None
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
        self.ServiceType = params.get("ServiceType")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        self.Disable = params.get("Disable")
        self.Area = params.get("Area")
        self.Readonly = params.get("Readonly")


class Cache(AbstractModel):
    """節點快取過期時間配置，分爲以下兩種：
    + 基礎版快取過期規則配置
    + 高級版快取過期規則配置

    """

    def __init__(self):
        """
        :param SimpleCache: 基礎快取過期時間配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type SimpleCache: :class:`taifucloudcloud.cdn.v20180606.models.SimpleCache`
        :param AdvancedCache: 高級快取過期時間配置（功能灰度中，尚未全量）
注意：此欄位可能返回 null，表示取不到有效值。
        :type AdvancedCache: :class:`taifucloudcloud.cdn.v20180606.models.AdvancedCache`
        """
        self.SimpleCache = None
        self.AdvancedCache = None


    def _deserialize(self, params):
        if params.get("SimpleCache") is not None:
            self.SimpleCache = SimpleCache()
            self.SimpleCache._deserialize(params.get("SimpleCache"))
        if params.get("AdvancedCache") is not None:
            self.AdvancedCache = AdvancedCache()
            self.AdvancedCache._deserialize(params.get("AdvancedCache"))


class CacheKey(AbstractModel):
    """快取鍵配置（過濾參數配置）

    """

    def __init__(self):
        """
        :param FullUrlCache: 是否開啓全路徑快取
on：開啓全路徑快取（即關閉參數過濾）
off：關閉全路徑快取（即開啓參數過濾）
        :type FullUrlCache: str
        """
        self.FullUrlCache = None


    def _deserialize(self, params):
        self.FullUrlCache = params.get("FullUrlCache")


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


class CappingRule(AbstractModel):
    """下行限速配置規則，最多可配置 100 條

    """

    def __init__(self):
        """
        :param RuleType: 規則類型：
all：所有文件生效
file：指定文件後綴生效
directory：指定路徑生效
path：指定絕對路徑生效
        :type RuleType: str
        :param RulePaths: RuleType 對應類型下的比對内容： 
all 時填充 *
file 時填充後綴名，如 jpg、txt
directory 時填充路徑，如 /xxx/test/
path 時填充絕對路徑，如 /xxx/test.html
        :type RulePaths: list of str
        :param KBpsThreshold: 下行速度值設置，單位爲 KB/s
        :type KBpsThreshold: int
        """
        self.RuleType = None
        self.RulePaths = None
        self.KBpsThreshold = None


    def _deserialize(self, params):
        self.RuleType = params.get("RuleType")
        self.RulePaths = params.get("RulePaths")
        self.KBpsThreshold = params.get("KBpsThreshold")


class CdnData(AbstractModel):
    """訪問明細數據類型

    """

    def __init__(self):
        """
        :param Metric: 查詢指定的指標名稱：
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
        :type SummarizedData: :class:`taifucloudcloud.cdn.v20180606.models.SummarizedData`
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


class CdnIp(AbstractModel):
    """IP 屬性訊息

    """

    def __init__(self):
        """
        :param Ip: 指定查詢的 IP
        :type Ip: str
        :param Platform: IP 歸屬：
yes：節點歸屬於Top Cloud  CDN
no：節點不屬於Top Cloud  CDN
        :type Platform: str
        :param Location: 節點所處的 /國家
unknown 表示節點位置未知
        :type Location: str
        :param History: 節點上下線曆史記錄
        :type History: list of CdnIpHistory
        :param Area: 節點的所在區域
mainland： 境内加速節點
overseas： 境外加速節點
unknown：服務地域無法獲取
        :type Area: str
        """
        self.Ip = None
        self.Platform = None
        self.Location = None
        self.History = None
        self.Area = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Platform = params.get("Platform")
        self.Location = params.get("Location")
        if params.get("History") is not None:
            self.History = []
            for item in params.get("History"):
                obj = CdnIpHistory()
                obj._deserialize(item)
                self.History.append(obj)
        self.Area = params.get("Area")


class CdnIpHistory(AbstractModel):
    """CDN 節點上下線曆史記錄

    """

    def __init__(self):
        """
        :param Status: 操作類型
online：節點上線
offline：節點下線
        :type Status: str
        :param Datetime: 操作類型對應的操作時間
當該值爲 null 時表示無曆史狀态變更記錄
注意：此欄位可能返回 null，表示取不到有效值。
        :type Datetime: str
        """
        self.Status = None
        self.Datetime = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Datetime = params.get("Datetime")


class ClientCert(AbstractModel):
    """https 用戶端證書配置

    """

    def __init__(self):
        """
        :param Certificate: 用戶端證書
PEM 格式，需要進行 Base 64 編碼
注意：此欄位可能返回 null，表示取不到有效值。
        :type Certificate: str
        :param CertName: 用戶端證書名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertName: str
        :param ExpireTime: 證書過期時間
作爲入參時無需填充
注意：此欄位可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param DeployTime: 證書頒發時間
作爲入參時無需填充
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


class ClsLogObject(AbstractModel):
    """CLS日志搜索對象

    """

    def __init__(self):
        """
        :param TopicId: 主題ID
        :type TopicId: str
        :param TopicName: 主題名字
        :type TopicName: str
        :param Timestamp: 日志時間
        :type Timestamp: str
        :param Content: 日志内容
        :type Content: str
        :param Filename: 采集路徑
        :type Filename: str
        :param Source: 日志來源設備
        :type Source: str
        """
        self.TopicId = None
        self.TopicName = None
        self.Timestamp = None
        self.Content = None
        self.Filename = None
        self.Source = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.Timestamp = params.get("Timestamp")
        self.Content = params.get("Content")
        self.Filename = params.get("Filename")
        self.Source = params.get("Source")


class ClsSearchLogs(AbstractModel):
    """Cls日志搜索結果

    """

    def __init__(self):
        """
        :param Context: 獲取更多檢索結果的遊標
        :type Context: str
        :param Listover: 搜索結果是否已經全部返回
        :type Listover: bool
        :param Results: 日志内容訊息
        :type Results: list of ClsLogObject
        """
        self.Context = None
        self.Listover = None
        self.Results = None


    def _deserialize(self, params):
        self.Context = params.get("Context")
        self.Listover = params.get("Listover")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = ClsLogObject()
                obj._deserialize(item)
                self.Results.append(obj)


class Compatibility(AbstractModel):
    """是否兼容舊版配置

    """

    def __init__(self):
        """
        :param Code: 兼容標志狀态碼。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Code: int
        """
        self.Code = None


    def _deserialize(self, params):
        self.Code = params.get("Code")


class Compression(AbstractModel):
    """智慧壓縮配置，預設對 js、html、css、xml、json、shtml、htm 後綴且大小爲 256 ~ 2097152 位元的文件進行 GZIP 壓縮

    """

    def __init__(self):
        """
        :param Switch: 智慧壓縮配置開關
on：開啓
off：關閉
        :type Switch: str
        :param CompressionRules: 壓縮規則數組
注意：此欄位可能返回 null，表示取不到有效值。
        :type CompressionRules: list of CompressionRule
        """
        self.Switch = None
        self.CompressionRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("CompressionRules") is not None:
            self.CompressionRules = []
            for item in params.get("CompressionRules"):
                obj = CompressionRule()
                obj._deserialize(item)
                self.CompressionRules.append(obj)


class CompressionRule(AbstractModel):
    """壓縮規則配置，最多可設置 100 條

    """

    def __init__(self):
        """
        :param Compress: true：需要設置爲 ture，啓用壓縮
注意：此欄位可能返回 null，表示取不到有效值。
        :type Compress: bool
        :param FileExtensions: 根據文件後綴類型壓縮
例如 jpg、txt
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileExtensions: list of str
        :param MinLength: 觸發壓縮的文件長度最小值，單位爲位元數
注意：此欄位可能返回 null，表示取不到有效值。
        :type MinLength: int
        :param MaxLength: 觸發壓縮的文件長度最大值，單位爲位元數
最大可設置爲 30MB
注意：此欄位可能返回 null，表示取不到有效值。
        :type MaxLength: int
        :param Algorithms: 文件壓縮算法
gzip：指定 GZIP 壓縮
brotli：需要同時指定 GZIP 壓縮才可啓用
注意：此欄位可能返回 null，表示取不到有效值。
        :type Algorithms: list of str
        """
        self.Compress = None
        self.FileExtensions = None
        self.MinLength = None
        self.MaxLength = None
        self.Algorithms = None


    def _deserialize(self, params):
        self.Compress = params.get("Compress")
        self.FileExtensions = params.get("FileExtensions")
        self.MinLength = params.get("MinLength")
        self.MaxLength = params.get("MaxLength")
        self.Algorithms = params.get("Algorithms")


class CreateClsLogTopicRequest(AbstractModel):
    """CreateClsLogTopic請求參數結構體

    """

    def __init__(self):
        """
        :param TopicName: 日志主題名稱
        :type TopicName: str
        :param LogsetId: 日志集ID
        :type LogsetId: str
        :param Channel: 接入管道，預設值爲cdn
        :type Channel: str
        :param DomainAreaConfigs: 域名區域訊息
        :type DomainAreaConfigs: list of DomainAreaConfig
        """
        self.TopicName = None
        self.LogsetId = None
        self.Channel = None
        self.DomainAreaConfigs = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.LogsetId = params.get("LogsetId")
        self.Channel = params.get("Channel")
        if params.get("DomainAreaConfigs") is not None:
            self.DomainAreaConfigs = []
            for item in params.get("DomainAreaConfigs"):
                obj = DomainAreaConfig()
                obj._deserialize(item)
                self.DomainAreaConfigs.append(obj)


class CreateClsLogTopicResponse(AbstractModel):
    """CreateClsLogTopic返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCdnDomainRequest(AbstractModel):
    """DeleteCdnDomain請求參數結構體

    """

    def __init__(self):
        """
        :param Domain: 域名
域名狀态需要爲【已停用】
        :type Domain: str
        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")


class DeleteCdnDomainResponse(AbstractModel):
    """DeleteCdnDomain返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClsLogTopicRequest(AbstractModel):
    """DeleteClsLogTopic請求參數結構體

    """

    def __init__(self):
        """
        :param TopicId: 日志主題ID
        :type TopicId: str
        :param LogsetId: 日志集ID
        :type LogsetId: str
        :param Channel: 接入管道，預設值爲cdn
        :type Channel: str
        """
        self.TopicId = None
        self.LogsetId = None
        self.Channel = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.LogsetId = params.get("LogsetId")
        self.Channel = params.get("Channel")


class DeleteClsLogTopicResponse(AbstractModel):
    """DeleteClsLogTopic返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeBillingDataRequest(AbstractModel):
    """DescribeBillingData請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 查詢起始時間，如：2018-09-04 10:40:00，返回結果大於等於指定時間
根據指定時間粒度參數不同，會進行向前取整，如指定起始時間爲 2018-09-04 10:40:00 按小時粒度查詢，返回的第一個數據對應時間點爲 2018-09-04 10:00:00
起始時間與結束時間間隔小於等於 90 天
        :type StartTime: str
        :param EndTime: 查詢結束時間，如：2018-09-04 10:40:00，返回結果小於等於指定時間
根據指定時間粒度參數不同，會進行向前取整，如指定結束時間爲  2018-09-04 10:40:00 按小時粒度查詢時，返回的最後一個數據對應時間點爲 2018-09-04 10:00:00
起始時間與結束時間間隔小於等於 90 天
        :type EndTime: str
        :param Interval: 時間粒度，支援模式如下：
min：1 分鍾粒度，查詢區間需要小於等於 24 小時
5min：5 分鍾粒度，查詢區間需要小於等於 31 天
hour：1 小時粒度，查詢區間需要小於等於 31 天内
day：天粒度，查詢區間需要大於 31 天

Area 欄位爲 overseas 時暫不支援1分鍾粒度數據查詢
        :type Interval: str
        :param Domain: 指定域名查詢計費數據
        :type Domain: str
        :param Project: 指定項目 ID 查詢，[前往檢視項目 ID](https://console.cloud.taifucloud.com/project)
若 Domain 參數填充了具體域名訊息，則返回該域名的計費數據，而非指定項目計費數據
        :type Project: int
        :param Area: 指定加速區域查詢計費數據：
mainland： 境内
overseas： 境外
不填充時，預設爲 mainland
        :type Area: str
        :param District: Area 爲 overseas 時，指定國家/地區查詢
 、國家/地區編碼可以檢視 [ 編碼映射](https://cloud.taifucloud.com/document/product/228/6316#.E7.9C.81.E4.BB.BD.E6.98.A0.E5.B0.84)
不填充時，查詢所有國家/地區
        :type District: int
        :param Metric: 計費統計類型
flux：計費流量
bandwidth：計費頻寬
預設爲 bandwidth
        :type Metric: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.Domain = None
        self.Project = None
        self.Area = None
        self.District = None
        self.Metric = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Interval = params.get("Interval")
        self.Domain = params.get("Domain")
        self.Project = params.get("Project")
        self.Area = params.get("Area")
        self.District = params.get("District")
        self.Metric = params.get("Metric")


class DescribeBillingDataResponse(AbstractModel):
    """DescribeBillingData返回參數結構體

    """

    def __init__(self):
        """
        :param Interval: 時間粒度，根據查詢時傳遞參數指定：
min：1 分鍾粒度
5min：5 分鍾粒度
hour：1 小時粒度
day：天粒度
        :type Interval: str
        :param Data: 數據明細
        :type Data: list of ResourceBillingData
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
                obj = ResourceBillingData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCdnDataRequest(AbstractModel):
    """DescribeCdnData請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 查詢起始時間，如：2018-09-04 10:40:00，返回結果大於等於指定時間
根據指定時間粒度不同，會進行向前歸整，如 2018-09-04 10:40:00 在按 1 小時的時間粒度查詢時，返回的第一個數據對應時間點爲 2018-09-04 10:00:00
起始時間與結束時間間隔小於等於 90 天
        :type StartTime: str
        :param EndTime: 查詢結束時間，如：2018-09-04 10:40:00，返回結果小於等於指定時間
根據指定時間粒度不同，會進行向前歸整，如 2018-09-04 10:40:00 在按 1 小時的時間粒度查詢時，返回的最後一個數據對應時間點爲 2018-09-04 10:00:00
起始時間與結束時間間隔小於等於 90 天
        :type EndTime: str
        :param Metric: 指定查詢指標，支援的類型有：
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
        :param Project: 指定要查詢的項目 ID，[前往檢視項目 ID](https://console.cloud.taifucloud.com/project)
未填充域名情況下，指定項目查詢，若填充了具體域名訊息，以域名爲主
        :type Project: int
        :param Interval: 時間粒度，支援以下幾種模式：
min：1 分鍾粒度，指定查詢區間 24 小時内（含 24 小時），可返回 1 分鍾粒度明細數據（指定查詢服務地域爲 境外時不支援 1 分鍾粒度）
5min：5 分鍾粒度，指定查詢區間 31 天内（含 31 天），可返回 5 分鍾粒度明細數據
hour：1 小時粒度，指定查詢區間 31 天内（含 31 天），可返回 1 小時粒度明細數據
day：天粒度，指定查詢區間大於 31 天，可返回天粒度明細數據
        :type Interval: str
        :param Detail: 多域名查詢時，預設（false)返回多個域名的匯總數據
可按需指定爲 true，返回每一個 Domain 的明細數據（statusCode 指標暫不支援）
        :type Detail: bool
        :param Isp: 查詢 境内CDN數據時，指定運營商查詢，不填充表示查詢所有運營商
運營商編碼可以檢視 [運營商編碼映射](https://cloud.taifucloud.com/document/product/228/6316#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)
指定運營商查詢時，不可同時指定 、IP協議查詢
        :type Isp: int
        :param District: 查詢 境内CDN數據時，指定 查詢，不填充表示查詢所有 
查詢 境外CDN數據時，指定國家/地區查詢，不填充表示查詢所有國家/地區
 、國家/地區編碼可以檢視 [ 編碼映射](https://cloud.taifucloud.com/document/product/228/6316#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)
指定（ 境内） 查詢時，不可同時指定運營商、IP協議查詢
        :type District: int
        :param Protocol: 指定協議查詢，不填充表示查詢所有協議
all：所有協議
http：指定查詢 HTTP 對應指標
https：指定查詢 HTTPS 對應指標
        :type Protocol: str
        :param DataSource: 指定數據源查詢，白名單功能
        :type DataSource: str
        :param IpProtocol: 指定IP協議查詢，不填充表示查詢所有協議
all：所有協議
ipv4：指定查詢 ipv4 對應指標
ipv6：指定查詢 ipv6 對應指標
指定IP協議查詢時，不可同時指定 、運營商查詢
        :type IpProtocol: str
        :param Area: 指定服務地域查詢，不填充表示查詢 境内CDN數據
mainland：指定查詢 境内 CDN 數據
overseas：指定查詢 境外 CDN 數據
        :type Area: str
        :param AreaType: 查詢 境外CDN數據時，可指定地區類型查詢，不填充表示查詢服務地區數據（僅在 Area 爲 overseas 時可用）
server：指定查詢服務地區（Top Cloud  CDN 節點服務器所在地區）數據
client：指定查詢用戶端地區（用戶請求終端所在地區）數據
        :type AreaType: str
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
        self.Area = None
        self.AreaType = None


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
        self.Area = params.get("Area")
        self.AreaType = params.get("AreaType")


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


class DescribeCdnDomainLogsRequest(AbstractModel):
    """DescribeCdnDomainLogs請求參數結構體

    """

    def __init__(self):
        """
        :param Domain: 指定域名查詢
        :type Domain: str
        :param StartTime: 開始時間，如 2019-09-04 00:00:00
        :type StartTime: str
        :param EndTime: 結束時間，如 2019-09-04 12:00:00
        :type EndTime: str
        :param Offset: 分頁查詢偏移量，預設爲 0 （第一頁）
        :type Offset: int
        :param Limit: 分頁查詢限制數目，預設爲 100，最大爲 1000
        :type Limit: int
        :param Area: 指定區域下載日志
mainland：獲取境内加速日志包下載連結
overseas：獲取境外加速日志包下載連結
global：同時獲取境内、境外加速日志包下載連結（分開打包）
不指定時預設爲 mainland
        :type Area: str
        """
        self.Domain = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.Area = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Area = params.get("Area")


class DescribeCdnDomainLogsResponse(AbstractModel):
    """DescribeCdnDomainLogs返回參數結構體

    """

    def __init__(self):
        """
        :param DomainLogs: 日志包下載連結
        :type DomainLogs: list of DomainLog
        :param TotalCount: 查詢到的總條數
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
                obj = DomainLog()
                obj._deserialize(item)
                self.DomainLogs.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCdnIpRequest(AbstractModel):
    """DescribeCdnIp請求參數結構體

    """

    def __init__(self):
        """
        :param Ips: 需要查詢的 IP 清單
        :type Ips: list of str
        """
        self.Ips = None


    def _deserialize(self, params):
        self.Ips = params.get("Ips")


class DescribeCdnIpResponse(AbstractModel):
    """DescribeCdnIp返回參數結構體

    """

    def __init__(self):
        """
        :param Ips: 查詢的節點歸屬詳情。
        :type Ips: list of CdnIp
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Ips = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Ips") is not None:
            self.Ips = []
            for item in params.get("Ips"):
                obj = CdnIp()
                obj._deserialize(item)
                self.Ips.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCertDomainsRequest(AbstractModel):
    """DescribeCertDomains請求參數結構體

    """

    def __init__(self):
        """
        :param Cert: PEM格式證書Base64編碼後的字串
        :type Cert: str
        """
        self.Cert = None


    def _deserialize(self, params):
        self.Cert = params.get("Cert")


class DescribeCertDomainsResponse(AbstractModel):
    """DescribeCertDomains返回參數結構體

    """

    def __init__(self):
        """
        :param Domains: 已接入CDN的域名清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Domains: list of str
        :param CertifiedDomains: CDN已配置證書的域名清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertifiedDomains: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Domains = None
        self.CertifiedDomains = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Domains = params.get("Domains")
        self.CertifiedDomains = params.get("CertifiedDomains")
        self.RequestId = params.get("RequestId")


class DescribeDomainsConfigRequest(AbstractModel):
    """DescribeDomainsConfig請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 分頁查詢偏移量，預設爲 0 （第一頁）
        :type Offset: int
        :param Limit: 分頁查詢限制數目，預設爲 100，最大可設置爲 1000
        :type Limit: int
        :param Filters: 查詢條件過濾器，複雜類型
        :type Filters: list of DomainFilter
        :param Sort: 排序規則
        :type Sort: :class:`taifucloudcloud.cdn.v20180606.models.Sort`
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
        :param Domains: 域名清單
        :type Domains: list of DetailDomain
        :param TotalNumber: 符合查詢條件的域名總數
用於分頁查詢
        :type TotalNumber: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Domains = None
        self.TotalNumber = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Domains") is not None:
            self.Domains = []
            for item in params.get("Domains"):
                obj = DetailDomain()
                obj._deserialize(item)
                self.Domains.append(obj)
        self.TotalNumber = params.get("TotalNumber")
        self.RequestId = params.get("RequestId")


class DescribeDomainsRequest(AbstractModel):
    """DescribeDomains請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 分頁查詢偏移量，預設爲 0 （第一頁）
        :type Offset: int
        :param Limit: 分頁查詢限制數目，預設爲 100，最大可設置爲 1000
        :type Limit: int
        :param Filters: 查詢條件過濾器，複雜類型
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
        :param Domains: 域名清單
        :type Domains: list of BriefDomain
        :param TotalNumber: 符合查詢條件的域名總數
用於分頁查詢
        :type TotalNumber: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Domains = None
        self.TotalNumber = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Domains") is not None:
            self.Domains = []
            for item in params.get("Domains"):
                obj = BriefDomain()
                obj._deserialize(item)
                self.Domains.append(obj)
        self.TotalNumber = params.get("TotalNumber")
        self.RequestId = params.get("RequestId")


class DescribeImageConfigRequest(AbstractModel):
    """DescribeImageConfig請求參數結構體

    """

    def __init__(self):
        """
        :param Domain: 域名
        :type Domain: str
        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")


class DescribeImageConfigResponse(AbstractModel):
    """DescribeImageConfig返回參數結構體

    """

    def __init__(self):
        """
        :param WebpAdapter: WebpAdapter配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type WebpAdapter: :class:`taifucloudcloud.cdn.v20180606.models.WebpAdapter`
        :param TpgAdapter: TpgAdapter配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type TpgAdapter: :class:`taifucloudcloud.cdn.v20180606.models.TpgAdapter`
        :param GuetzliAdapter: GuetzliAdapter配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type GuetzliAdapter: :class:`taifucloudcloud.cdn.v20180606.models.GuetzliAdapter`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.WebpAdapter = None
        self.TpgAdapter = None
        self.GuetzliAdapter = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WebpAdapter") is not None:
            self.WebpAdapter = WebpAdapter()
            self.WebpAdapter._deserialize(params.get("WebpAdapter"))
        if params.get("TpgAdapter") is not None:
            self.TpgAdapter = TpgAdapter()
            self.TpgAdapter._deserialize(params.get("TpgAdapter"))
        if params.get("GuetzliAdapter") is not None:
            self.GuetzliAdapter = GuetzliAdapter()
            self.GuetzliAdapter._deserialize(params.get("GuetzliAdapter"))
        self.RequestId = params.get("RequestId")


class DescribeIpStatusRequest(AbstractModel):
    """DescribeIpStatus請求參數結構體

    """

    def __init__(self):
        """
        :param Domain: 加速域名
        :type Domain: str
        :param Layer: 節點類型：
edge：表示邊緣節點
last：表示回源層節點
不填充情況下，預設返回邊緣節點訊息
        :type Layer: str
        """
        self.Domain = None
        self.Layer = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Layer = params.get("Layer")


class DescribeIpStatusResponse(AbstractModel):
    """DescribeIpStatus返回參數結構體

    """

    def __init__(self):
        """
        :param Ips: 節點清單
        :type Ips: list of IpStatus
        :param TotalCount: 節點總個數
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Ips = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Ips") is not None:
            self.Ips = []
            for item in params.get("Ips"):
                obj = IpStatus()
                obj._deserialize(item)
                self.Ips.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeIpVisitRequest(AbstractModel):
    """DescribeIpVisit請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 查詢起始時間，如：2018-09-04 10:40:10，返回結果大於等於指定時間
根據指定時間粒度不同，會進行向前歸整，如 2018-09-04 10:40:10 在按 5 分鍾的時間粒度查詢時，返回的第一個數據對應時間點爲 2018-09-04 10:40:00
        :type StartTime: str
        :param EndTime: 查詢結束時間，如：2018-09-04 10:40:10，返回結果小於等於指定時間
根據指定時間粒度不同，會進行向前歸整，如 2018-09-04 10:40:10 在按 5 分鍾的時間粒度查詢時，返回的最後一個數據對應時間點爲 2018-09-04 10:40:00
        :type EndTime: str
        :param Domains: 指定查詢域名清單，最多可一次性查詢 30 個加速域名明細
        :type Domains: list of str
        :param Project: 指定要查詢的項目 ID，[前往檢視項目 ID](https://console.cloud.taifucloud.com/project)
未填充域名情況下，指定項目查詢，若填充了具體域名訊息，以域名爲主
        :type Project: int
        :param Interval: 時間粒度，支援以下幾種模式：
5min：5 分鍾粒度，查詢時間區間 24 小時内，預設返回 5 分鍾粒度活躍用戶數
day：天粒度，查詢時間區間大於 1 天時，預設返回天粒度活躍用戶數
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
isp：運營商映射查詢
district： （ 境内）、國家/地區（ 境外）映射查詢
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
        :param ServerRegionRelation: 服務端區域id和子區域id的映射關系。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ServerRegionRelation: list of RegionMapRelation
        :param ClientRegionRelation: 用戶端區域id和子區域id的映射關系。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClientRegionRelation: list of RegionMapRelation
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.MapInfoList = None
        self.ServerRegionRelation = None
        self.ClientRegionRelation = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MapInfoList") is not None:
            self.MapInfoList = []
            for item in params.get("MapInfoList"):
                obj = MapInfo()
                obj._deserialize(item)
                self.MapInfoList.append(obj)
        if params.get("ServerRegionRelation") is not None:
            self.ServerRegionRelation = []
            for item in params.get("ServerRegionRelation"):
                obj = RegionMapRelation()
                obj._deserialize(item)
                self.ServerRegionRelation.append(obj)
        if params.get("ClientRegionRelation") is not None:
            self.ClientRegionRelation = []
            for item in params.get("ClientRegionRelation"):
                obj = RegionMapRelation()
                obj._deserialize(item)
                self.ClientRegionRelation.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOriginDataRequest(AbstractModel):
    """DescribeOriginData請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 查詢起始時間，如：2018-09-04 10:40:00，返回結果大於等於指定時間
根據指定時間粒度不同，會進行向前歸整，如 2018-09-04 10:40:00 在按 1 小時的時間粒度查詢時，返回的第一個數據對應時間點爲 2018-09-04 10:00:00
起始時間與結束時間間隔小於等於 90 天
        :type StartTime: str
        :param EndTime: 查詢結束時間，如：2018-09-04 10:40:00，返回結果小於等於指定時間
根據指定時間粒度不同，會進行向前歸整，如 2018-09-04 10:40:00 在按 1 小時的時間粒度查詢時，返回的最後一個數據對應時間點爲 2018-09-04 10:00:00
起始時間與結束時間間隔小於等於 90 天
        :type EndTime: str
        :param Metric: 指定查詢指標，支援的類型有：
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
        :param Project: 指定要查詢的項目 ID，[前往檢視項目 ID](https://console.cloud.taifucloud.com/project)
未填充域名情況下，指定項目查詢，若填充了具體域名訊息，以域名爲主
        :type Project: int
        :param Interval: 時間粒度，支援以下幾種模式：
min：1 分鍾粒度，指定查詢區間 24 小時内（含 24 小時），可返回 1 分鍾粒度明細數據（指定查詢服務地域爲 境外時不支援 1 分鍾粒度）
5min：5 分鍾粒度，指定查詢區間 31 天内（含 31 天），可返回 5 分鍾粒度明細數據
hour：1 小時粒度，指定查詢區間 31 天内（含 31 天），可返回 1 小時粒度明細數據
day：天粒度，指定查詢區間大於 31 天，可返回天粒度明細數據
        :type Interval: str
        :param Detail: Domains 傳入多個時，預設（false)返回多個域名的匯總數據
可按需指定爲 true，返回每一個 Domain 的明細數據（statusCode 指標暫不支援）
        :type Detail: bool
        :param Area: 指定服務地域查詢，不填充表示查詢 境内 CDN 數據
mainland：指定查詢 境内 CDN 數據
overseas：指定查詢 境外 CDN 數據
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Metric = None
        self.Domains = None
        self.Project = None
        self.Interval = None
        self.Detail = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Metric = params.get("Metric")
        self.Domains = params.get("Domains")
        self.Project = params.get("Project")
        self.Interval = params.get("Interval")
        self.Detail = params.get("Detail")
        self.Area = params.get("Area")


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

    def __init__(self):
        """
        :param Area: 指定服務地域查詢
mainland：境内計費方式查詢
overseas：境外計費方式查詢
未填充時預設爲 mainland
        :type Area: str
        """
        self.Area = None


    def _deserialize(self, params):
        self.Area = params.get("Area")


class DescribePayTypeResponse(AbstractModel):
    """DescribePayType返回參數結構體

    """

    def __init__(self):
        """
        :param PayType: 計費類型：
flux：流量計費
bandwidth：頻寬計費
日結計費方式切換時，若當日産生消耗，則此欄位表示第二天即将生效的計費方式，若未産生消耗，則表示已經生效的計費方式。
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
        :param RegionType: 境外計費類型：
all：全地區統一計費
multiple：分地區計費
        :type RegionType: str
        :param CurrentPayType: 當前生效計費類型：
flux：流量計費
bandwidth：頻寬計費
        :type CurrentPayType: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PayType = None
        self.BillingCycle = None
        self.StatType = None
        self.RegionType = None
        self.CurrentPayType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PayType = params.get("PayType")
        self.BillingCycle = params.get("BillingCycle")
        self.StatType = params.get("StatType")
        self.RegionType = params.get("RegionType")
        self.CurrentPayType = params.get("CurrentPayType")
        self.RequestId = params.get("RequestId")


class DescribePurgeQuotaRequest(AbstractModel):
    """DescribePurgeQuota請求參數結構體

    """


class DescribePurgeQuotaResponse(AbstractModel):
    """DescribePurgeQuota返回參數結構體

    """

    def __init__(self):
        """
        :param UrlPurge: URL重新整理用量及配額。
        :type UrlPurge: list of Quota
        :param PathPurge: 目錄重新整理用量及配額。
        :type PathPurge: list of Quota
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.UrlPurge = None
        self.PathPurge = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UrlPurge") is not None:
            self.UrlPurge = []
            for item in params.get("UrlPurge"):
                obj = Quota()
                obj._deserialize(item)
                self.UrlPurge.append(obj)
        if params.get("PathPurge") is not None:
            self.PathPurge = []
            for item in params.get("PathPurge"):
                obj = Quota()
                obj._deserialize(item)
                self.PathPurge.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePurgeTasksRequest(AbstractModel):
    """DescribePurgeTasks請求參數結構體

    """

    def __init__(self):
        """
        :param PurgeType: 指定重新整理類型查詢
url：url 重新整理記錄
path：目錄重新整理記錄
        :type PurgeType: str
        :param StartTime: 根據時間區間查詢時，填充開始時間，如 2018-08-08 00:00:00
        :type StartTime: str
        :param EndTime: 根據時間區間查詢時，填充結束時間，如 2018-08-08 23:59:59
        :type EndTime: str
        :param TaskId: 根據任務 ID 查詢時，填充任務 ID
查詢時任務 ID 與起始時間必須填充一項
        :type TaskId: str
        :param Offset: 分頁查詢偏移量，預設爲 0 （第一頁）
        :type Offset: int
        :param Limit: 分頁查詢限制數目，預設爲 20
        :type Limit: int
        :param Keyword: 支援域名過濾，或 http(s):// 開頭完整 URL 過濾
        :type Keyword: str
        :param Status: 指定任務狀态查詢
fail：重新整理失敗
done：重新整理成功
process：重新整理中
        :type Status: str
        :param Area: 指定重新整理地域查詢
mainland：境内
overseas：境外
global：全球
        :type Area: str
        """
        self.PurgeType = None
        self.StartTime = None
        self.EndTime = None
        self.TaskId = None
        self.Offset = None
        self.Limit = None
        self.Keyword = None
        self.Status = None
        self.Area = None


    def _deserialize(self, params):
        self.PurgeType = params.get("PurgeType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TaskId = params.get("TaskId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Keyword = params.get("Keyword")
        self.Status = params.get("Status")
        self.Area = params.get("Area")


class DescribePurgeTasksResponse(AbstractModel):
    """DescribePurgeTasks返回參數結構體

    """

    def __init__(self):
        """
        :param PurgeLogs: 詳細重新整理記錄
注意：此欄位可能返回 null，表示取不到有效值。
        :type PurgeLogs: list of PurgeTask
        :param TotalCount: 任務總數，用於分頁
注意：此欄位可能返回 null，表示取不到有效值。
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


class DescribePushQuotaRequest(AbstractModel):
    """DescribePushQuota請求參數結構體

    """


class DescribePushQuotaResponse(AbstractModel):
    """DescribePushQuota返回參數結構體

    """

    def __init__(self):
        """
        :param UrlPush: Url預熱用量及配額。
        :type UrlPush: list of Quota
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.UrlPush = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UrlPush") is not None:
            self.UrlPush = []
            for item in params.get("UrlPush"):
                obj = Quota()
                obj._deserialize(item)
                self.UrlPush.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePushTasksRequest(AbstractModel):
    """DescribePushTasks請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 開始時間，如2018-08-08 00:00:00。
        :type StartTime: str
        :param EndTime: 結束時間，如2018-08-08 23:59:59。
        :type EndTime: str
        :param TaskId: 指定任務 ID 查詢
TaskId 和起始時間必須指定一項
        :type TaskId: str
        :param Keyword: 查詢關鍵字，請輸入域名或 http(s):// 開頭完整 URL
        :type Keyword: str
        :param Offset: 分頁查詢偏移量，預設爲 0 （第一頁）
        :type Offset: int
        :param Limit: 分頁查詢限制數目，預設爲 20
        :type Limit: int
        :param Area: 指定地區查詢預熱紀錄
mainland：境内
overseas：境外
global：全球
        :type Area: str
        :param Status: 指定任務狀态查詢
fail：預熱失敗
done：預熱成功
process：預熱中
        :type Status: str
        """
        self.StartTime = None
        self.EndTime = None
        self.TaskId = None
        self.Keyword = None
        self.Offset = None
        self.Limit = None
        self.Area = None
        self.Status = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TaskId = params.get("TaskId")
        self.Keyword = params.get("Keyword")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Area = params.get("Area")
        self.Status = params.get("Status")


class DescribePushTasksResponse(AbstractModel):
    """DescribePushTasks返回參數結構體

    """

    def __init__(self):
        """
        :param PushLogs: 預熱曆史記錄
注意：此欄位可能返回 null，表示取不到有效值。
        :type PushLogs: list of PushTask
        :param TotalCount: 任務總數，用於分頁
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PushLogs = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PushLogs") is not None:
            self.PushLogs = []
            for item in params.get("PushLogs"):
                obj = PushTask()
                obj._deserialize(item)
                self.PushLogs.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeReportDataRequest(AbstractModel):
    """DescribeReportData請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 查詢起始時間
        :type StartTime: str
        :param EndTime: 查詢結束時間
        :type EndTime: str
        :param ReportType: 報表類型
daily：日報表
weekly：周報表
monthly：月報表
        :type ReportType: str
        :param Area: 域名加速區域
mainland： 境内
overseas： 境外
        :type Area: str
        :param Offset: 偏移量，預設0。
        :type Offset: int
        :param Limit: 數據個數，預設1000。
        :type Limit: int
        :param Project: 按項目ID篩選
        :type Project: int
        """
        self.StartTime = None
        self.EndTime = None
        self.ReportType = None
        self.Area = None
        self.Offset = None
        self.Limit = None
        self.Project = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ReportType = params.get("ReportType")
        self.Area = params.get("Area")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Project = params.get("Project")


class DescribeReportDataResponse(AbstractModel):
    """DescribeReportData返回參數結構體

    """

    def __init__(self):
        """
        :param DomainReport: 域名維度數據詳情
        :type DomainReport: list of ReportData
        :param ProjectReport: 項目維度數據詳情
        :type ProjectReport: list of ReportData
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DomainReport = None
        self.ProjectReport = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainReport") is not None:
            self.DomainReport = []
            for item in params.get("DomainReport"):
                obj = ReportData()
                obj._deserialize(item)
                self.DomainReport.append(obj)
        if params.get("ProjectReport") is not None:
            self.ProjectReport = []
            for item in params.get("ProjectReport"):
                obj = ReportData()
                obj._deserialize(item)
                self.ProjectReport.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTrafficPackagesRequest(AbstractModel):
    """DescribeTrafficPackages請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 分頁查詢起始網址，預設 0（第一頁）
        :type Offset: int
        :param Limit: 分頁查詢記錄個數，預設100，最大1000
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTrafficPackagesResponse(AbstractModel):
    """DescribeTrafficPackages返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 流量包總個數
        :type TotalCount: int
        :param TrafficPackages: 流量包詳情
        :type TrafficPackages: list of TrafficPackage
        :param ExpiringCount: 即将過期的流量包個數（7天内）
        :type ExpiringCount: int
        :param EnabledCount: 有效流量包個數
        :type EnabledCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TrafficPackages = None
        self.ExpiringCount = None
        self.EnabledCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TrafficPackages") is not None:
            self.TrafficPackages = []
            for item in params.get("TrafficPackages"):
                obj = TrafficPackage()
                obj._deserialize(item)
                self.TrafficPackages.append(obj)
        self.ExpiringCount = params.get("ExpiringCount")
        self.EnabledCount = params.get("EnabledCount")
        self.RequestId = params.get("RequestId")


class DescribeUrlViolationsRequest(AbstractModel):
    """DescribeUrlViolations請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 分頁查詢偏移量，預設爲 0 （第一頁）
        :type Offset: int
        :param Limit: 分頁查詢限制數目，預設爲 100
        :type Limit: int
        :param Domains: 指定的域名查詢
        :type Domains: list of str
        """
        self.Offset = None
        self.Limit = None
        self.Domains = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Domains = params.get("Domains")


class DescribeUrlViolationsResponse(AbstractModel):
    """DescribeUrlViolations返回參數結構體

    """

    def __init__(self):
        """
        :param UrlRecordList: 違規 URL 詳情
注意：此欄位可能返回 null，表示取不到有效值。
        :type UrlRecordList: list of ViolationUrl
        :param TotalCount: 記錄總數，用於分頁
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.UrlRecordList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UrlRecordList") is not None:
            self.UrlRecordList = []
            for item in params.get("UrlRecordList"):
                obj = ViolationUrl()
                obj._deserialize(item)
                self.UrlRecordList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DetailDomain(AbstractModel):
    """加速域名全量配置訊息

    """

    def __init__(self):
        """
        :param ResourceId: 域名 ID
        :type ResourceId: str
        :param AppId: Top Cloud 賬號ID
        :type AppId: int
        :param Domain: 加速域名
        :type Domain: str
        :param Cname: 域名對應的 CNAME 網址
注意：此欄位可能返回 null，表示取不到有效值。
        :type Cname: str
        :param Status: 加速服務狀态
rejected：域名審核未通過，域名備案過期/被注銷導緻
processing：部署中
online：已啓動
offline：已關閉
        :type Status: str
        :param ProjectId: 項目 ID，可前往Top Cloud 項目管理頁面檢視
        :type ProjectId: int
        :param ServiceType: 域名業務類型
web：靜态加速
download：下載加速
media：流媒體點播加速
        :type ServiceType: str
        :param CreateTime: 域名創建時間
        :type CreateTime: str
        :param UpdateTime: 域名更新時間
        :type UpdateTime: str
        :param Origin: 源站配置
        :type Origin: :class:`taifucloudcloud.cdn.v20180606.models.Origin`
        :param IpFilter: IP 黑白名單配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type IpFilter: :class:`taifucloudcloud.cdn.v20180606.models.IpFilter`
        :param IpFreqLimit: IP 訪問限頻配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type IpFreqLimit: :class:`taifucloudcloud.cdn.v20180606.models.IpFreqLimit`
        :param StatusCodeCache: 狀态碼快取配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type StatusCodeCache: :class:`taifucloudcloud.cdn.v20180606.models.StatusCodeCache`
        :param Compression: 智慧壓縮配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type Compression: :class:`taifucloudcloud.cdn.v20180606.models.Compression`
        :param BandwidthAlert: 頻寬封頂配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type BandwidthAlert: :class:`taifucloudcloud.cdn.v20180606.models.BandwidthAlert`
        :param RangeOriginPull: Range 回源配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type RangeOriginPull: :class:`taifucloudcloud.cdn.v20180606.models.RangeOriginPull`
        :param FollowRedirect: 301/302 回源自動跟随配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type FollowRedirect: :class:`taifucloudcloud.cdn.v20180606.models.FollowRedirect`
        :param ErrorPage: 自定義錯誤頁面配置（功能灰度中，敬請期待）
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrorPage: :class:`taifucloudcloud.cdn.v20180606.models.ErrorPage`
        :param RequestHeader: 自定義請求頭部配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type RequestHeader: :class:`taifucloudcloud.cdn.v20180606.models.RequestHeader`
        :param ResponseHeader: 自定義響應頭部配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResponseHeader: :class:`taifucloudcloud.cdn.v20180606.models.ResponseHeader`
        :param DownstreamCapping: 單連結下行限速配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type DownstreamCapping: :class:`taifucloudcloud.cdn.v20180606.models.DownstreamCapping`
        :param CacheKey: 帶參/不帶參快取配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type CacheKey: :class:`taifucloudcloud.cdn.v20180606.models.CacheKey`
        :param ResponseHeaderCache: 源站頭部快取配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResponseHeaderCache: :class:`taifucloudcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param VideoSeek: 視訊拖拽配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type VideoSeek: :class:`taifucloudcloud.cdn.v20180606.models.VideoSeek`
        :param Cache: 節點快取過期規則配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type Cache: :class:`taifucloudcloud.cdn.v20180606.models.Cache`
        :param OriginPullOptimization: 跨國鏈路優化配置（功能灰度中，敬請期待）
注意：此欄位可能返回 null，表示取不到有效值。
        :type OriginPullOptimization: :class:`taifucloudcloud.cdn.v20180606.models.OriginPullOptimization`
        :param Https: Https 加速相關配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type Https: :class:`taifucloudcloud.cdn.v20180606.models.Https`
        :param Authentication: 時間戳防盜鏈配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type Authentication: :class:`taifucloudcloud.cdn.v20180606.models.Authentication`
        :param Seo: SEO 優化配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type Seo: :class:`taifucloudcloud.cdn.v20180606.models.Seo`
        :param Disable: 域名封禁狀态
normal：正常狀态
overdue：賬號欠費導緻域名關閉，儲值完成後可自行啓動加速服務
malicious：域名出現惡意行爲，強制關閉加速服務
ddos：域名被大規模 DDoS 攻擊，關閉加速服務
idle：域名超過 90 天内無任何操作、數據産生，判定爲不活躍域名自動關閉加速服務，可自行啓動加速服務
unlicensed：域名未備案/備案注銷，自動關閉加速服務，備案完成後可自行啓動加速服務
capping：觸發配置的頻寬阈值上限
readonly：域名存在特殊配置，被鎖定
注意：此欄位可能返回 null，表示取不到有效值。
        :type Disable: str
        :param ForceRedirect: 訪問協議強制跳轉配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type ForceRedirect: :class:`taifucloudcloud.cdn.v20180606.models.ForceRedirect`
        :param Referer: Referer 防盜鏈配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type Referer: :class:`taifucloudcloud.cdn.v20180606.models.Referer`
        :param MaxAge: 浏覽器快取過期規則配置（功能灰度中，敬請期待）
注意：此欄位可能返回 null，表示取不到有效值。
        :type MaxAge: :class:`taifucloudcloud.cdn.v20180606.models.MaxAge`
        :param Ipv6: Ipv6 配置（功能灰度中，敬請期待）
注意：此欄位可能返回 null，表示取不到有效值。
        :type Ipv6: :class:`taifucloudcloud.cdn.v20180606.models.Ipv6`
        :param Compatibility: 是否兼容舊版本配置（内部相容性欄位）
注意：此欄位可能返回 null，表示取不到有效值。
        :type Compatibility: :class:`taifucloudcloud.cdn.v20180606.models.Compatibility`
        :param SpecificConfig: 區域特殊配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type SpecificConfig: :class:`taifucloudcloud.cdn.v20180606.models.SpecificConfig`
        :param Area: 加速區域
mainland： 境内加速
overseas： 境外加速
global：全球加速
注意：此欄位可能返回 null，表示取不到有效值。
        :type Area: str
        :param Readonly: 域名鎖定狀态
normal：未鎖定
mainland： 境内鎖定
overseas： 境外鎖定
global：全球鎖定
注意：此欄位可能返回 null，表示取不到有效值。
        :type Readonly: str
        :param OriginPullTimeout: 回源超時配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type OriginPullTimeout: :class:`taifucloudcloud.cdn.v20180606.models.OriginPullTimeout`
        :param AwsPrivateAccess: 回源S3鑒權配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type AwsPrivateAccess: :class:`taifucloudcloud.cdn.v20180606.models.AwsPrivateAccess`
        :param SecurityConfig: Scdn配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type SecurityConfig: :class:`taifucloudcloud.cdn.v20180606.models.SecurityConfig`
        :param ImageOptimization: ImageOptimization配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type ImageOptimization: :class:`taifucloudcloud.cdn.v20180606.models.ImageOptimization`
        """
        self.ResourceId = None
        self.AppId = None
        self.Domain = None
        self.Cname = None
        self.Status = None
        self.ProjectId = None
        self.ServiceType = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Origin = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.StatusCodeCache = None
        self.Compression = None
        self.BandwidthAlert = None
        self.RangeOriginPull = None
        self.FollowRedirect = None
        self.ErrorPage = None
        self.RequestHeader = None
        self.ResponseHeader = None
        self.DownstreamCapping = None
        self.CacheKey = None
        self.ResponseHeaderCache = None
        self.VideoSeek = None
        self.Cache = None
        self.OriginPullOptimization = None
        self.Https = None
        self.Authentication = None
        self.Seo = None
        self.Disable = None
        self.ForceRedirect = None
        self.Referer = None
        self.MaxAge = None
        self.Ipv6 = None
        self.Compatibility = None
        self.SpecificConfig = None
        self.Area = None
        self.Readonly = None
        self.OriginPullTimeout = None
        self.AwsPrivateAccess = None
        self.SecurityConfig = None
        self.ImageOptimization = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.AppId = params.get("AppId")
        self.Domain = params.get("Domain")
        self.Cname = params.get("Cname")
        self.Status = params.get("Status")
        self.ProjectId = params.get("ProjectId")
        self.ServiceType = params.get("ServiceType")
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
        if params.get("StatusCodeCache") is not None:
            self.StatusCodeCache = StatusCodeCache()
            self.StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("BandwidthAlert") is not None:
            self.BandwidthAlert = BandwidthAlert()
            self.BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("RangeOriginPull") is not None:
            self.RangeOriginPull = RangeOriginPull()
            self.RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("FollowRedirect") is not None:
            self.FollowRedirect = FollowRedirect()
            self.FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ErrorPage") is not None:
            self.ErrorPage = ErrorPage()
            self.ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("RequestHeader") is not None:
            self.RequestHeader = RequestHeader()
            self.RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("DownstreamCapping") is not None:
            self.DownstreamCapping = DownstreamCapping()
            self.DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("ResponseHeaderCache") is not None:
            self.ResponseHeaderCache = ResponseHeaderCache()
            self.ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("VideoSeek") is not None:
            self.VideoSeek = VideoSeek()
            self.VideoSeek._deserialize(params.get("VideoSeek"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("OriginPullOptimization") is not None:
            self.OriginPullOptimization = OriginPullOptimization()
            self.OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("Authentication") is not None:
            self.Authentication = Authentication()
            self.Authentication._deserialize(params.get("Authentication"))
        if params.get("Seo") is not None:
            self.Seo = Seo()
            self.Seo._deserialize(params.get("Seo"))
        self.Disable = params.get("Disable")
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Referer") is not None:
            self.Referer = Referer()
            self.Referer._deserialize(params.get("Referer"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6()
            self.Ipv6._deserialize(params.get("Ipv6"))
        if params.get("Compatibility") is not None:
            self.Compatibility = Compatibility()
            self.Compatibility._deserialize(params.get("Compatibility"))
        if params.get("SpecificConfig") is not None:
            self.SpecificConfig = SpecificConfig()
            self.SpecificConfig._deserialize(params.get("SpecificConfig"))
        self.Area = params.get("Area")
        self.Readonly = params.get("Readonly")
        if params.get("OriginPullTimeout") is not None:
            self.OriginPullTimeout = OriginPullTimeout()
            self.OriginPullTimeout._deserialize(params.get("OriginPullTimeout"))
        if params.get("AwsPrivateAccess") is not None:
            self.AwsPrivateAccess = AwsPrivateAccess()
            self.AwsPrivateAccess._deserialize(params.get("AwsPrivateAccess"))
        if params.get("SecurityConfig") is not None:
            self.SecurityConfig = SecurityConfig()
            self.SecurityConfig._deserialize(params.get("SecurityConfig"))
        if params.get("ImageOptimization") is not None:
            self.ImageOptimization = ImageOptimization()
            self.ImageOptimization._deserialize(params.get("ImageOptimization"))


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
        :type CacheOptResult: :class:`taifucloudcloud.cdn.v20180606.models.CacheOptResult`
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


class DisableClsLogTopicRequest(AbstractModel):
    """DisableClsLogTopic請求參數結構體

    """

    def __init__(self):
        """
        :param LogsetId: 日志集ID
        :type LogsetId: str
        :param TopicId: 日志主題ID
        :type TopicId: str
        :param Channel: 接入管道，預設值爲cdn
        :type Channel: str
        """
        self.LogsetId = None
        self.TopicId = None
        self.Channel = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.TopicId = params.get("TopicId")
        self.Channel = params.get("Channel")


class DisableClsLogTopicResponse(AbstractModel):
    """DisableClsLogTopic返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DomainAreaConfig(AbstractModel):
    """域名地區配置

    """

    def __init__(self):
        """
        :param Domain: 域名
        :type Domain: str
        :param Area: 地區清單，其中元素可爲mainland/overseas
        :type Area: list of str
        """
        self.Domain = None
        self.Area = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Area = params.get("Area")


class DomainFilter(AbstractModel):
    """域名查詢時過濾條件。

    """

    def __init__(self):
        """
        :param Name: 過濾欄位名，支援的清單如下：
- origin：主源站。
- domain：域名。
- resourceId：域名id。
- status：域名狀态，online，offline或processing。
- serviceType：業務類型，web，download或media。
- projectId：項目ID。
- domainType：主源站類型，cname表示自有源，cos表示cos接入。
- fullUrlCache：全路徑快取，on或off。
- https：是否配置https，on，off或processing。
- originPullProtocol：回源協議類型，支援http，follow或https。
- tagKey：標簽鍵。
        :type Name: str
        :param Value: 過濾欄位值。
        :type Value: list of str
        :param Fuzzy: 是否啓用模糊查詢，僅支援過濾欄位名爲origin，domain。
模糊查詢時，Value長度最大爲1，否則Value長度最大爲5。
        :type Fuzzy: bool
        """
        self.Name = None
        self.Value = None
        self.Fuzzy = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        self.Fuzzy = params.get("Fuzzy")


class DomainLog(AbstractModel):
    """日志包下載連結詳情

    """

    def __init__(self):
        """
        :param StartTime: 日志包起始時間
        :type StartTime: str
        :param EndTime: 日志包結束時間
        :type EndTime: str
        :param LogPath: 日志包下載連結
        :type LogPath: str
        :param Area: 日志包對應加速區域
mainland：境内
overseas：境外
        :type Area: str
        :param LogName: 日志包文件名
        :type LogName: str
        """
        self.StartTime = None
        self.EndTime = None
        self.LogPath = None
        self.Area = None
        self.LogName = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.LogPath = params.get("LogPath")
        self.Area = params.get("Area")
        self.LogName = params.get("LogName")


class DownstreamCapping(AbstractModel):
    """單連結下行限速配置，預設爲關閉狀态

    """

    def __init__(self):
        """
        :param Switch: 下行速度配置開關
on：開啓
off：關閉
        :type Switch: str
        :param CappingRules: 下行限速規則
注意：此欄位可能返回 null，表示取不到有效值。
        :type CappingRules: list of CappingRule
        """
        self.Switch = None
        self.CappingRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("CappingRules") is not None:
            self.CappingRules = []
            for item in params.get("CappingRules"):
                obj = CappingRule()
                obj._deserialize(item)
                self.CappingRules.append(obj)


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
        :type CacheOptResult: :class:`taifucloudcloud.cdn.v20180606.models.CacheOptResult`
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


class EnableClsLogTopicRequest(AbstractModel):
    """EnableClsLogTopic請求參數結構體

    """

    def __init__(self):
        """
        :param LogsetId: 日志集ID
        :type LogsetId: str
        :param TopicId: 日志主題ID
        :type TopicId: str
        :param Channel: 接入管道，預設值爲cdn
        :type Channel: str
        """
        self.LogsetId = None
        self.TopicId = None
        self.Channel = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.TopicId = params.get("TopicId")
        self.Channel = params.get("Channel")


class EnableClsLogTopicResponse(AbstractModel):
    """EnableClsLogTopic返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ErrorPage(AbstractModel):
    """狀态碼重定向配置，預設爲關閉狀态（功能灰度中，尚未全量）

    """

    def __init__(self):
        """
        :param Switch: 狀态碼重定向配置開關
on：開啓
off：關閉
注意：此欄位可能返回 null，表示取不到有效值。
        :type Switch: str
        :param PageRules: 狀态碼重定向規則配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type PageRules: list of ErrorPageRule
        """
        self.Switch = None
        self.PageRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("PageRules") is not None:
            self.PageRules = []
            for item in params.get("PageRules"):
                obj = ErrorPageRule()
                obj._deserialize(item)
                self.PageRules.append(obj)


class ErrorPageRule(AbstractModel):
    """狀态碼重定向規則配置

    """

    def __init__(self):
        """
        :param StatusCode: 狀态碼
支援 400、403、404、500
        :type StatusCode: int
        :param RedirectCode: 重定向狀态碼設置
支援 301 或 302
        :type RedirectCode: int
        :param RedirectUrl: 重定向 URL
需要爲完整跳轉路徑，如 https://www.test.com/error.html
        :type RedirectUrl: str
        """
        self.StatusCode = None
        self.RedirectCode = None
        self.RedirectUrl = None


    def _deserialize(self, params):
        self.StatusCode = params.get("StatusCode")
        self.RedirectCode = params.get("RedirectCode")
        self.RedirectUrl = params.get("RedirectUrl")


class FollowRedirect(AbstractModel):
    """回源 301/302 狀态碼自動跟随配置，預設爲關閉狀态

    """

    def __init__(self):
        """
        :param Switch: 回源跟随開關
on：開啓
off：關閉
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class ForceRedirect(AbstractModel):
    """訪問協議強制跳轉配置，預設爲關閉狀态

    """

    def __init__(self):
        """
        :param Switch: 訪問強制跳轉配置開關
on：開啓
off：關閉
注意：此欄位可能返回 null，表示取不到有效值。
        :type Switch: str
        :param RedirectType: 訪問強制跳轉類型
http：強制 http 跳轉
https：強制 https 跳轉
注意：此欄位可能返回 null，表示取不到有效值。
        :type RedirectType: str
        :param RedirectStatusCode: 強制跳轉時返回狀态碼 
支援 301、302
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


class GetDisableRecordsRequest(AbstractModel):
    """GetDisableRecords請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 開始時間，如：2018-12-12 10:24:00。
        :type StartTime: str
        :param EndTime: 結束時間，如：2018-12-14 10:24:00。
        :type EndTime: str
        :param Url: 指定 URL 查詢
        :type Url: str
        :param Status: URL 當前狀态
disable：當前仍爲禁用狀态，訪問返回 403
enable：當前爲可用狀态，已解禁，可正常訪問
        :type Status: str
        :param Offset: 分頁查詢偏移量，預設爲 0 （第一頁）。
        :type Offset: int
        :param Limit: 分頁查詢限制數目，預設爲20。
        :type Limit: int
        """
        self.StartTime = None
        self.EndTime = None
        self.Url = None
        self.Status = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Url = params.get("Url")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetDisableRecordsResponse(AbstractModel):
    """GetDisableRecords返回參數結構體

    """

    def __init__(self):
        """
        :param UrlRecordList: 封禁曆史記錄
注意：此欄位可能返回 null，表示取不到有效值。
        :type UrlRecordList: list of UrlRecord
        :param TotalCount: 任務總數，用於分頁
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.UrlRecordList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UrlRecordList") is not None:
            self.UrlRecordList = []
            for item in params.get("UrlRecordList"):
                obj = UrlRecord()
                obj._deserialize(item)
                self.UrlRecordList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class GuetzliAdapter(AbstractModel):
    """圖片優化-GuetzliAdapter配置

    """

    def __init__(self):
        """
        :param Switch: 開關，"on/off"
注意：此欄位可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class HttpHeaderPathRule(AbstractModel):
    """Http 頭部設置規則，最多可設置 100 條

    """

    def __init__(self):
        """
        :param HeaderMode: http 頭部設置方式
add：添加頭部，若已存在頭部，則會存在重複頭部
set：僅回源頭部配置支援，若頭部已存在則會函蓋原有頭部值，若不存在，則會增加該頭部及值
del：删除頭部
注意：此欄位可能返回 null，表示取不到有效值。
        :type HeaderMode: str
        :param HeaderName: http 頭部名稱，最多可設置 100 個字元
注意：此欄位可能返回 null，表示取不到有效值。
        :type HeaderName: str
        :param HeaderValue: http 頭部值，最多可設置 1000 個字元
Mode 爲 del 時非必填
Mode 爲 add/set 時必填
注意：此欄位可能返回 null，表示取不到有效值。
        :type HeaderValue: str
        :param RuleType: 規則類型：
all：所有文件生效
file：指定文件後綴生效
directory：指定路徑生效
path：指定絕對路徑生效
注意：此欄位可能返回 null，表示取不到有效值。
        :type RuleType: str
        :param RulePaths: RuleType 對應類型下的比對内容：
all 時填充 *
file 時填充後綴名，如 jpg、txt
directory 時填充路徑，如 /xxx/test/
path 時填充絕對路徑，如 /xxx/test.html
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
    """域名 https 加速配置，預設爲關閉狀态

    """

    def __init__(self):
        """
        :param Switch: https 配置開關
on：開啓
off：關閉
注意：此欄位可能返回 null，表示取不到有效值。
        :type Switch: str
        :param Http2: http2 配置開關
on：開啓
off：關閉
初次啓用 https 加速會預設開啓 http2 配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type Http2: str
        :param OcspStapling: OCSP 配置開關
on：開啓
off：關閉
預設爲關閉狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type OcspStapling: str
        :param VerifyClient: 用戶端證書校驗功能
on：開啓
off：關閉
預設爲關閉狀态，開啓時需要上傳用戶端證書訊息，該配置項目前在灰度中，尚未全量
注意：此欄位可能返回 null，表示取不到有效值。
        :type VerifyClient: str
        :param CertInfo: 服務端證書配置訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertInfo: :class:`taifucloudcloud.cdn.v20180606.models.ServerCert`
        :param ClientCertInfo: 用戶端證書配置訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClientCertInfo: :class:`taifucloudcloud.cdn.v20180606.models.ClientCert`
        :param Spdy: Spdy 配置開關
on：開啓
off：關閉
預設爲關閉狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type Spdy: str
        :param SslStatus: https 證書佈署狀态
closed：已關閉
deploying：部署中
deployed：部署成功
failed：佈署失敗
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


class ImageOptimization(AbstractModel):
    """ImageOptimization配置

    """

    def __init__(self):
        """
        :param WebpAdapter: WebpAdapter配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type WebpAdapter: :class:`taifucloudcloud.cdn.v20180606.models.WebpAdapter`
        :param TpgAdapter: TpgAdapter配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type TpgAdapter: :class:`taifucloudcloud.cdn.v20180606.models.TpgAdapter`
        :param GuetzliAdapter: GuetzliAdapter配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type GuetzliAdapter: :class:`taifucloudcloud.cdn.v20180606.models.GuetzliAdapter`
        """
        self.WebpAdapter = None
        self.TpgAdapter = None
        self.GuetzliAdapter = None


    def _deserialize(self, params):
        if params.get("WebpAdapter") is not None:
            self.WebpAdapter = WebpAdapter()
            self.WebpAdapter._deserialize(params.get("WebpAdapter"))
        if params.get("TpgAdapter") is not None:
            self.TpgAdapter = TpgAdapter()
            self.TpgAdapter._deserialize(params.get("TpgAdapter"))
        if params.get("GuetzliAdapter") is not None:
            self.GuetzliAdapter = GuetzliAdapter()
            self.GuetzliAdapter._deserialize(params.get("GuetzliAdapter"))


class IpFilter(AbstractModel):
    """IP 黑白名單配置，預設爲關閉狀态

    """

    def __init__(self):
        """
        :param Switch: IP 黑白名單配置開關
on：開啓
off：關閉
        :type Switch: str
        :param FilterType: IP 黑白名單類型
whitelist：白名單
blacklist：黑名單
注意：此欄位可能返回 null，表示取不到有效值。
        :type FilterType: str
        :param Filters: IP 黑白名單清單
支援 X.X.X.X 形式 IP，或 /8、 /16、/24 形式網段
最多可填充 50 個白名單或 50 個黑名單
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
    """單節點單 IP 訪問限頻配置，預設爲關閉狀态

    """

    def __init__(self):
        """
        :param Switch: IP 限頻配置開關
on：開啓
off：關閉
        :type Switch: str
        :param Qps: 設置每秒請求數限制
超出限制的請求會直接返回 514
注意：此欄位可能返回 null，表示取不到有效值。
        :type Qps: int
        """
        self.Switch = None
        self.Qps = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Qps = params.get("Qps")


class IpStatus(AbstractModel):
    """節點 IP 訊息

    """

    def __init__(self):
        """
        :param Ip: 節點 IP
        :type Ip: str
        :param District: 節點所屬區域
        :type District: str
        :param Isp: 節點所屬運營商
        :type Isp: str
        :param City: 節點所在城市
        :type City: str
        :param Status: 節點狀态
online：上線狀态，正常調度服務中
offline：下線狀态
        :type Status: str
        """
        self.Ip = None
        self.District = None
        self.Isp = None
        self.City = None
        self.Status = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.District = params.get("District")
        self.Isp = params.get("Isp")
        self.City = params.get("City")
        self.Status = params.get("Status")


class Ipv6(AbstractModel):
    """Ipv6啓用配置，不可更改

    """

    def __init__(self):
        """
        :param Switch: 域名是否開啓ipv6功能，on或off。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class ListClsLogTopicsRequest(AbstractModel):
    """ListClsLogTopics請求參數結構體

    """

    def __init__(self):
        """
        :param Channel: 接入管道，預設值爲cdn
        :type Channel: str
        """
        self.Channel = None


    def _deserialize(self, params):
        self.Channel = params.get("Channel")


class ListClsLogTopicsResponse(AbstractModel):
    """ListClsLogTopics返回參數結構體

    """

    def __init__(self):
        """
        :param Logset: 日志集訊息
        :type Logset: :class:`taifucloudcloud.cdn.v20180606.models.LogSetInfo`
        :param Topics: 日志主題訊息清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Topics: list of TopicInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Logset = None
        self.Topics = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Logset") is not None:
            self.Logset = LogSetInfo()
            self.Logset._deserialize(params.get("Logset"))
        if params.get("Topics") is not None:
            self.Topics = []
            for item in params.get("Topics"):
                obj = TopicInfo()
                obj._deserialize(item)
                self.Topics.append(obj)
        self.RequestId = params.get("RequestId")


class ListClsTopicDomainsRequest(AbstractModel):
    """ListClsTopicDomains請求參數結構體

    """

    def __init__(self):
        """
        :param LogsetId: 日志集ID
        :type LogsetId: str
        :param TopicId: 日志主題ID
        :type TopicId: str
        :param Channel: 接入管道，預設值爲cdn
        :type Channel: str
        """
        self.LogsetId = None
        self.TopicId = None
        self.Channel = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.TopicId = params.get("TopicId")
        self.Channel = params.get("Channel")


class ListClsTopicDomainsResponse(AbstractModel):
    """ListClsTopicDomains返回參數結構體

    """

    def __init__(self):
        """
        :param AppId: 開發者ID
        :type AppId: int
        :param Channel: 管道
        :type Channel: str
        :param LogsetId: 日志集ID
        :type LogsetId: str
        :param TopicId: 日志主題ID
        :type TopicId: str
        :param DomainAreaConfigs: 域名區域配置，其中可能含有已删除的域名，如果要再傳回ManageClsTopicDomains介面，需要結合ListCdnDomains介面排除掉已删除的域名
        :type DomainAreaConfigs: list of DomainAreaConfig
        :param TopicName: 日志主題名稱
        :type TopicName: str
        :param UpdateTime: 日志主題最近更新時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AppId = None
        self.Channel = None
        self.LogsetId = None
        self.TopicId = None
        self.DomainAreaConfigs = None
        self.TopicName = None
        self.UpdateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.Channel = params.get("Channel")
        self.LogsetId = params.get("LogsetId")
        self.TopicId = params.get("TopicId")
        if params.get("DomainAreaConfigs") is not None:
            self.DomainAreaConfigs = []
            for item in params.get("DomainAreaConfigs"):
                obj = DomainAreaConfig()
                obj._deserialize(item)
                self.DomainAreaConfigs.append(obj)
        self.TopicName = params.get("TopicName")
        self.UpdateTime = params.get("UpdateTime")
        self.RequestId = params.get("RequestId")


class ListTopDataRequest(AbstractModel):
    """ListTopData請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 查詢起始日期，如：2018-09-09
僅支援按天粒度的數據查詢，取入參中的天訊息作爲起始日期
返回大於等於起始日期當天 00:00:00 點産生的數據
僅支援 90 天内數據查詢
        :type StartTime: str
        :param EndTime: 查詢結束日期，如：2018-09-10
僅支援按天粒度的數據查詢，取入參中的天訊息作爲結束日期
返回小於等於結束日期當天 23:59:59 産生的數據
EndTime 需要大於等於 StartTime
        :type EndTime: str
        :param Metric: 排序對象，支援以下幾種形式：
url：訪問 URL 排序，帶參數統計，支援的 Filter 爲 flux、request
path：訪問 URL 排序，不帶參數統計，支援的 Filter 爲 flux、request（白名單功能）
district： 、國家/地區排序，支援的 Filter 爲 flux、request
isp：運營商排序，支援的 Filter 爲 flux、request
host：域名訪問數據排序，支援的 Filter 爲：flux、request、bandwidth、fluxHitRate、2XX、3XX、4XX、5XX、statusCode
originHost：域名回源數據排序，支援的 Filter 爲 flux、request、bandwidth、origin_2XX、origin_3XX、origin_4XX、origin_5XX、OriginStatusCode
        :type Metric: str
        :param Filter: 排序使用的指標名稱：
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
        :param Project: 指定要查詢的項目 ID，[前往檢視項目 ID](https://console.cloud.taifucloud.com/project)
未填充域名情況下，指定項目查詢，若填充了具體域名訊息，以域名爲主
        :type Project: int
        :param Detail: 多域名查詢時，預設（false)返回所有域名匯總排序結果
Metric 爲 url、path、district、isp，Filter 爲 flux、request 時，可設置爲 true，返回每一個 Domain 的排序數據
        :type Detail: bool
        :param Code: Filter 爲 statusCode、OriginStatusCode 時，填充指定狀态碼查詢排序結果
        :type Code: str
        :param Area: 指定服務地域查詢，不填充表示查詢 境内 CDN 數據
mainland：指定查詢 境内 CDN 數據
overseas：指定查詢 境外 CDN 數據，支援的 Metric 爲 url、district、host、originHost，當 Metric 爲 originHost 時僅支援 flux、request、bandwidth Filter
        :type Area: str
        :param AreaType: 查詢 境外CDN數據，且僅當 Metric 爲 district 或 host 時，可指定地區類型查詢，不填充表示查詢服務地區數據（僅在 Area 爲 overseas，且 Metric 是 district 或 host 時可用）
server：指定查詢服務地區（Top Cloud  CDN 節點服務器所在地區）數據
client：指定查詢用戶端地區（用戶請求終端所在地區）數據，當 Metric 爲 host 時僅支援 flux、request、bandwidth Filter
        :type AreaType: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Metric = None
        self.Filter = None
        self.Domains = None
        self.Project = None
        self.Detail = None
        self.Code = None
        self.Area = None
        self.AreaType = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Metric = params.get("Metric")
        self.Filter = params.get("Filter")
        self.Domains = params.get("Domains")
        self.Project = params.get("Project")
        self.Detail = params.get("Detail")
        self.Code = params.get("Code")
        self.Area = params.get("Area")
        self.AreaType = params.get("AreaType")


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


class LogSetInfo(AbstractModel):
    """日志集訊息

    """

    def __init__(self):
        """
        :param AppId: 開發者ID
        :type AppId: int
        :param Channel: 管道
注意：此欄位可能返回 null，表示取不到有效值。
        :type Channel: str
        :param LogsetId: 日志集ID
        :type LogsetId: str
        :param LogsetName: 日志集名字
        :type LogsetName: str
        :param IsDefault: 是否預設日志集
        :type IsDefault: int
        :param LogsetSavePeriod: 日志保存時間，單位爲天
        :type LogsetSavePeriod: int
        :param CreateTime: 創建日期
        :type CreateTime: str
        :param Region: 區域
        :type Region: str
        """
        self.AppId = None
        self.Channel = None
        self.LogsetId = None
        self.LogsetName = None
        self.IsDefault = None
        self.LogsetSavePeriod = None
        self.CreateTime = None
        self.Region = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.Channel = params.get("Channel")
        self.LogsetId = params.get("LogsetId")
        self.LogsetName = params.get("LogsetName")
        self.IsDefault = params.get("IsDefault")
        self.LogsetSavePeriod = params.get("LogsetSavePeriod")
        self.CreateTime = params.get("CreateTime")
        self.Region = params.get("Region")


class MainlandConfig(AbstractModel):
    """域名國内地區特殊配置。分地區特殊配置。UpdateDomainConfig介面只支援修改部分分地區配置，爲了兼容舊版本配置，本類型會列出舊版本所有可能存在差異的配置清單，支援修改的配置清單如下：
    + Authentication
    + BandwidthAlert
    + ErrorPage
    + IpFilter
    + Origin
    + Referer

    """

    def __init__(self):
        """
        :param Authentication: 時間戳防盜鏈配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Authentication: :class:`taifucloudcloud.cdn.v20180606.models.Authentication`
        :param BandwidthAlert: 頻寬封頂配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type BandwidthAlert: :class:`taifucloudcloud.cdn.v20180606.models.BandwidthAlert`
        :param Cache: 快取規則配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Cache: :class:`taifucloudcloud.cdn.v20180606.models.Cache`
        :param CacheKey: 快取相關配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CacheKey: :class:`taifucloudcloud.cdn.v20180606.models.CacheKey`
        :param Compression: 智慧壓縮配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Compression: :class:`taifucloudcloud.cdn.v20180606.models.Compression`
        :param DownstreamCapping: 下載限速配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DownstreamCapping: :class:`taifucloudcloud.cdn.v20180606.models.DownstreamCapping`
        :param ErrorPage: 錯誤碼重定向配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrorPage: :class:`taifucloudcloud.cdn.v20180606.models.ErrorPage`
        :param FollowRedirect: 301和302自動回源跟随配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FollowRedirect: :class:`taifucloudcloud.cdn.v20180606.models.FollowRedirect`
        :param ForceRedirect: 訪問協議強制跳轉配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ForceRedirect: :class:`taifucloudcloud.cdn.v20180606.models.ForceRedirect`
        :param Https: Https配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Https: :class:`taifucloudcloud.cdn.v20180606.models.Https`
        :param IpFilter: IP黑白名單配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IpFilter: :class:`taifucloudcloud.cdn.v20180606.models.IpFilter`
        :param IpFreqLimit: IP限頻配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IpFreqLimit: :class:`taifucloudcloud.cdn.v20180606.models.IpFreqLimit`
        :param MaxAge: 浏覽器快取規則配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type MaxAge: :class:`taifucloudcloud.cdn.v20180606.models.MaxAge`
        :param Origin: 源站配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Origin: :class:`taifucloudcloud.cdn.v20180606.models.Origin`
        :param OriginPullOptimization: 跨國優化配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OriginPullOptimization: :class:`taifucloudcloud.cdn.v20180606.models.OriginPullOptimization`
        :param RangeOriginPull: Range回源配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RangeOriginPull: :class:`taifucloudcloud.cdn.v20180606.models.RangeOriginPull`
        :param Referer: 防盜鏈配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Referer: :class:`taifucloudcloud.cdn.v20180606.models.Referer`
        :param RequestHeader: 回源請求頭部配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RequestHeader: :class:`taifucloudcloud.cdn.v20180606.models.RequestHeader`
        :param ResponseHeader: 源站響應頭部配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResponseHeader: :class:`taifucloudcloud.cdn.v20180606.models.ResponseHeader`
        :param ResponseHeaderCache: 遵循源站快取頭部配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResponseHeaderCache: :class:`taifucloudcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param Seo: seo優化配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Seo: :class:`taifucloudcloud.cdn.v20180606.models.Seo`
        :param ServiceType: 域名業務類型，web，download，media分别表示靜态加速，下載加速和流媒體加速。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ServiceType: str
        :param StatusCodeCache: 狀态碼快取配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type StatusCodeCache: :class:`taifucloudcloud.cdn.v20180606.models.StatusCodeCache`
        :param VideoSeek: 視訊拖拽配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type VideoSeek: :class:`taifucloudcloud.cdn.v20180606.models.VideoSeek`
        """
        self.Authentication = None
        self.BandwidthAlert = None
        self.Cache = None
        self.CacheKey = None
        self.Compression = None
        self.DownstreamCapping = None
        self.ErrorPage = None
        self.FollowRedirect = None
        self.ForceRedirect = None
        self.Https = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.MaxAge = None
        self.Origin = None
        self.OriginPullOptimization = None
        self.RangeOriginPull = None
        self.Referer = None
        self.RequestHeader = None
        self.ResponseHeader = None
        self.ResponseHeaderCache = None
        self.Seo = None
        self.ServiceType = None
        self.StatusCodeCache = None
        self.VideoSeek = None


    def _deserialize(self, params):
        if params.get("Authentication") is not None:
            self.Authentication = Authentication()
            self.Authentication._deserialize(params.get("Authentication"))
        if params.get("BandwidthAlert") is not None:
            self.BandwidthAlert = BandwidthAlert()
            self.BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("DownstreamCapping") is not None:
            self.DownstreamCapping = DownstreamCapping()
            self.DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("ErrorPage") is not None:
            self.ErrorPage = ErrorPage()
            self.ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("FollowRedirect") is not None:
            self.FollowRedirect = FollowRedirect()
            self.FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("IpFilter") is not None:
            self.IpFilter = IpFilter()
            self.IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self.IpFreqLimit = IpFreqLimit()
            self.IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        if params.get("OriginPullOptimization") is not None:
            self.OriginPullOptimization = OriginPullOptimization()
            self.OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("RangeOriginPull") is not None:
            self.RangeOriginPull = RangeOriginPull()
            self.RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("Referer") is not None:
            self.Referer = Referer()
            self.Referer._deserialize(params.get("Referer"))
        if params.get("RequestHeader") is not None:
            self.RequestHeader = RequestHeader()
            self.RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("ResponseHeaderCache") is not None:
            self.ResponseHeaderCache = ResponseHeaderCache()
            self.ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("Seo") is not None:
            self.Seo = Seo()
            self.Seo._deserialize(params.get("Seo"))
        self.ServiceType = params.get("ServiceType")
        if params.get("StatusCodeCache") is not None:
            self.StatusCodeCache = StatusCodeCache()
            self.StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("VideoSeek") is not None:
            self.VideoSeek = VideoSeek()
            self.VideoSeek._deserialize(params.get("VideoSeek"))


class ManageClsTopicDomainsRequest(AbstractModel):
    """ManageClsTopicDomains請求參數結構體

    """

    def __init__(self):
        """
        :param LogsetId: 日志集ID
        :type LogsetId: str
        :param TopicId: 日志主題ID
        :type TopicId: str
        :param Channel: 接入管道，預設值爲cdn
        :type Channel: str
        :param DomainAreaConfigs: 域名區域配置，注意：如果此欄位爲空，則表示解綁對應主題下的所有域名
        :type DomainAreaConfigs: list of DomainAreaConfig
        """
        self.LogsetId = None
        self.TopicId = None
        self.Channel = None
        self.DomainAreaConfigs = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.TopicId = params.get("TopicId")
        self.Channel = params.get("Channel")
        if params.get("DomainAreaConfigs") is not None:
            self.DomainAreaConfigs = []
            for item in params.get("DomainAreaConfigs"):
                obj = DomainAreaConfig()
                obj._deserialize(item)
                self.DomainAreaConfigs.append(obj)


class ManageClsTopicDomainsResponse(AbstractModel):
    """ManageClsTopicDomains返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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


class MaxAge(AbstractModel):
    """浏覽器快取規則配置，用於設置 MaxAge 預設值，預設爲關閉狀态（功能灰度中，尚未全量）

    """

    def __init__(self):
        """
        :param Switch: 浏覽器快取配置開關
on：開啓
off：關閉
注意：此欄位可能返回 null，表示取不到有效值。
        :type Switch: str
        :param MaxAgeRules: MaxAge 規則
注意：此欄位可能返回 null，表示取不到有效值。
        :type MaxAgeRules: list of MaxAgeRule
        """
        self.Switch = None
        self.MaxAgeRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("MaxAgeRules") is not None:
            self.MaxAgeRules = []
            for item in params.get("MaxAgeRules"):
                obj = MaxAgeRule()
                obj._deserialize(item)
                self.MaxAgeRules.append(obj)


class MaxAgeRule(AbstractModel):
    """MagAge 規則配置

    """

    def __init__(self):
        """
        :param MaxAgeType: 規則類型：
all：所有文件生效
file：指定文件後綴生效
directory：指定路徑生效
path：指定絕對路徑生效
        :type MaxAgeType: str
        :param MaxAgeContents: MaxAgeType 對應類型下的比對内容：
all 時填充 *
file 時填充後綴名，如 jpg、txt
directory 時填充路徑，如 /xxx/test/
path 時填充絕對路徑，如 /xxx/test.html
        :type MaxAgeContents: list of str
        :param MaxAgeTime: MaxAge 時間設置，單位秒
        :type MaxAgeTime: int
        """
        self.MaxAgeType = None
        self.MaxAgeContents = None
        self.MaxAgeTime = None


    def _deserialize(self, params):
        self.MaxAgeType = params.get("MaxAgeType")
        self.MaxAgeContents = params.get("MaxAgeContents")
        self.MaxAgeTime = params.get("MaxAgeTime")


class Origin(AbstractModel):
    """源站配置複雜類型，支援以下配置：
    + 源站指定爲單個域名
    + 源站指定爲多個 IP，可配置端口（1~65535），可配置權重（1~100），格式爲 IP:端口:權重
    + 回源域名配置
    + 物件儲存（COS）作爲源站
    + 熱備源站指定爲單個域名
    + 熱備源站指定爲多個 IP，可配置端口（1~65535），暫不支援權重配置
    + 熱備源站回源域名配置

    """

    def __init__(self):
        """
        :param Origins: 主源站清單
修改源站時，需要同時填充對應的 OriginType
注意：此欄位可能返回 null，表示取不到有效值。
        :type Origins: list of str
        :param OriginType: 主源站類型
入參支援以下幾種類型：
domain：域名類型
cos：物件儲存源站
ip：IP 清單作爲源站
ipv6：源站清單爲一個單獨的 IPv6 網址
ip_ipv6：源站清單爲多個 IPv4 網址和一個 IPv6 網址
出參增加以下幾種類型：
image：數據萬象源站
ftp：曆史 FTP 托管源源站，現已不維護
修改 Origins 時需要同時填充對應的 OriginType
IPv6 功能目前尚未全量，需要先申請試用
注意：此欄位可能返回 null，表示取不到有效值。
        :type OriginType: str
        :param ServerName: 回主源站時 Host 頭部，不填充則預設爲加速域名
若接入的是泛域名，則回源 Host 預設爲訪問時的子域名
注意：此欄位可能返回 null，表示取不到有效值。
        :type ServerName: str
        :param CosPrivateAccess: OriginType 爲物件儲存（COS）時，可以指定是否允許訪問私有 bucket
注意：需要先授權 CDN 訪問該私有 Bucket 的權限後，才可開啓此配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CosPrivateAccess: str
        :param OriginPullProtocol: 回源協議配置
http：強制 http 回源
follow：協議跟随回源
https：強制 https 回源，https 回源時僅支援源站 443 端口
注意：此欄位可能返回 null，表示取不到有效值。
        :type OriginPullProtocol: str
        :param BackupOrigins: 備源站清單
修改備源站時，需要同時填充對應的 BackupOriginType
注意：此欄位可能返回 null，表示取不到有效值。
        :type BackupOrigins: list of str
        :param BackupOriginType: 備源站類型，支援以下類型：
domain：域名類型
ip：IP 清單作爲源站
修改 BackupOrigins 時需要同時填充對應的 BackupOriginType
注意：此欄位可能返回 null，表示取不到有效值。
        :type BackupOriginType: str
        :param BackupServerName: 回備源站時 Host 頭部，不填充則預設爲主源站的 ServerName
注意：此欄位可能返回 null，表示取不到有效值。
        :type BackupServerName: str
        """
        self.Origins = None
        self.OriginType = None
        self.ServerName = None
        self.CosPrivateAccess = None
        self.OriginPullProtocol = None
        self.BackupOrigins = None
        self.BackupOriginType = None
        self.BackupServerName = None


    def _deserialize(self, params):
        self.Origins = params.get("Origins")
        self.OriginType = params.get("OriginType")
        self.ServerName = params.get("ServerName")
        self.CosPrivateAccess = params.get("CosPrivateAccess")
        self.OriginPullProtocol = params.get("OriginPullProtocol")
        self.BackupOrigins = params.get("BackupOrigins")
        self.BackupOriginType = params.get("BackupOriginType")
        self.BackupServerName = params.get("BackupServerName")


class OriginPullOptimization(AbstractModel):
    """跨國回源優化配置，預設爲關閉狀态（功能灰度中，尚未全量）

    """

    def __init__(self):
        """
        :param Switch: 跨國回源優化配置開關
on：開啓
off：關閉
        :type Switch: str
        :param OptimizationType: 跨國類型
OVToCN：境外回源境内
CNToOV：境内回源境外
注意：此欄位可能返回 null，表示取不到有效值。
        :type OptimizationType: str
        """
        self.Switch = None
        self.OptimizationType = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.OptimizationType = params.get("OptimizationType")


class OriginPullTimeout(AbstractModel):
    """回源超時配置

    """

    def __init__(self):
        """
        :param ConnectTimeout: 回源建連超時時間，單位爲秒，要求5~60之間
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConnectTimeout: int
        :param ReceiveTimeout: 回源接收超時時間，單位爲秒，要求10 ~ 60之間
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReceiveTimeout: int
        """
        self.ConnectTimeout = None
        self.ReceiveTimeout = None


    def _deserialize(self, params):
        self.ConnectTimeout = params.get("ConnectTimeout")
        self.ReceiveTimeout = params.get("ReceiveTimeout")


class OverseaConfig(AbstractModel):
    """域名海外地區特殊配置。UpdateDomainConfig介面只支援修改部分分地區配置，爲了兼容舊版本配置，本類型會列出舊版本所有可能存在差異的配置清單，支援修改的配置清單如下：
    + Authentication
    + BandwidthAlert
    + ErrorPage
    + IpFilter
    + Origin
    + Referer

    """

    def __init__(self):
        """
        :param Authentication: 時間戳防盜鏈配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Authentication: :class:`taifucloudcloud.cdn.v20180606.models.Authentication`
        :param BandwidthAlert: 頻寬封頂配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type BandwidthAlert: :class:`taifucloudcloud.cdn.v20180606.models.BandwidthAlert`
        :param Cache: 快取規則配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Cache: :class:`taifucloudcloud.cdn.v20180606.models.Cache`
        :param CacheKey: 快取相關配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CacheKey: :class:`taifucloudcloud.cdn.v20180606.models.CacheKey`
        :param Compression: 智慧壓縮配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Compression: :class:`taifucloudcloud.cdn.v20180606.models.Compression`
        :param DownstreamCapping: 下載限速配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DownstreamCapping: :class:`taifucloudcloud.cdn.v20180606.models.DownstreamCapping`
        :param ErrorPage: 錯誤碼重定向配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrorPage: :class:`taifucloudcloud.cdn.v20180606.models.ErrorPage`
        :param FollowRedirect: 301和302自動回源跟随配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FollowRedirect: :class:`taifucloudcloud.cdn.v20180606.models.FollowRedirect`
        :param ForceRedirect: 訪問協議強制跳轉配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ForceRedirect: :class:`taifucloudcloud.cdn.v20180606.models.ForceRedirect`
        :param Https: Https配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Https: :class:`taifucloudcloud.cdn.v20180606.models.Https`
        :param IpFilter: IP黑白名單配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IpFilter: :class:`taifucloudcloud.cdn.v20180606.models.IpFilter`
        :param IpFreqLimit: IP限頻配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IpFreqLimit: :class:`taifucloudcloud.cdn.v20180606.models.IpFreqLimit`
        :param MaxAge: 浏覽器快取規則配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type MaxAge: :class:`taifucloudcloud.cdn.v20180606.models.MaxAge`
        :param Origin: 源站配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Origin: :class:`taifucloudcloud.cdn.v20180606.models.Origin`
        :param OriginPullOptimization: 跨國優化配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OriginPullOptimization: :class:`taifucloudcloud.cdn.v20180606.models.OriginPullOptimization`
        :param RangeOriginPull: Range回源配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RangeOriginPull: :class:`taifucloudcloud.cdn.v20180606.models.RangeOriginPull`
        :param Referer: 防盜鏈配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Referer: :class:`taifucloudcloud.cdn.v20180606.models.Referer`
        :param RequestHeader: 回源請求頭部配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RequestHeader: :class:`taifucloudcloud.cdn.v20180606.models.RequestHeader`
        :param ResponseHeader: 源站響應頭部配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResponseHeader: :class:`taifucloudcloud.cdn.v20180606.models.ResponseHeader`
        :param ResponseHeaderCache: 遵循源站快取頭部配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResponseHeaderCache: :class:`taifucloudcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param Seo: seo優化配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Seo: :class:`taifucloudcloud.cdn.v20180606.models.Seo`
        :param ServiceType: 域名業務類型，web，download，media分别表示靜态加速，下載加速和流媒體加速。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ServiceType: str
        :param StatusCodeCache: 狀态碼快取配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type StatusCodeCache: :class:`taifucloudcloud.cdn.v20180606.models.StatusCodeCache`
        :param VideoSeek: 視訊拖拽配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type VideoSeek: :class:`taifucloudcloud.cdn.v20180606.models.VideoSeek`
        """
        self.Authentication = None
        self.BandwidthAlert = None
        self.Cache = None
        self.CacheKey = None
        self.Compression = None
        self.DownstreamCapping = None
        self.ErrorPage = None
        self.FollowRedirect = None
        self.ForceRedirect = None
        self.Https = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.MaxAge = None
        self.Origin = None
        self.OriginPullOptimization = None
        self.RangeOriginPull = None
        self.Referer = None
        self.RequestHeader = None
        self.ResponseHeader = None
        self.ResponseHeaderCache = None
        self.Seo = None
        self.ServiceType = None
        self.StatusCodeCache = None
        self.VideoSeek = None


    def _deserialize(self, params):
        if params.get("Authentication") is not None:
            self.Authentication = Authentication()
            self.Authentication._deserialize(params.get("Authentication"))
        if params.get("BandwidthAlert") is not None:
            self.BandwidthAlert = BandwidthAlert()
            self.BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("DownstreamCapping") is not None:
            self.DownstreamCapping = DownstreamCapping()
            self.DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("ErrorPage") is not None:
            self.ErrorPage = ErrorPage()
            self.ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("FollowRedirect") is not None:
            self.FollowRedirect = FollowRedirect()
            self.FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("IpFilter") is not None:
            self.IpFilter = IpFilter()
            self.IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self.IpFreqLimit = IpFreqLimit()
            self.IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        if params.get("OriginPullOptimization") is not None:
            self.OriginPullOptimization = OriginPullOptimization()
            self.OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("RangeOriginPull") is not None:
            self.RangeOriginPull = RangeOriginPull()
            self.RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("Referer") is not None:
            self.Referer = Referer()
            self.Referer._deserialize(params.get("Referer"))
        if params.get("RequestHeader") is not None:
            self.RequestHeader = RequestHeader()
            self.RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("ResponseHeaderCache") is not None:
            self.ResponseHeaderCache = ResponseHeaderCache()
            self.ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("Seo") is not None:
            self.Seo = Seo()
            self.Seo._deserialize(params.get("Seo"))
        self.ServiceType = params.get("ServiceType")
        if params.get("StatusCodeCache") is not None:
            self.StatusCodeCache = StatusCodeCache()
            self.StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("VideoSeek") is not None:
            self.VideoSeek = VideoSeek()
            self.VideoSeek._deserialize(params.get("VideoSeek"))


class PurgePathCacheRequest(AbstractModel):
    """PurgePathCache請求參數結構體

    """

    def __init__(self):
        """
        :param Paths: 目錄清單，需要包含協議頭部 http:// 或 https://
        :type Paths: list of str
        :param FlushType: 重新整理類型
flush：重新整理産生更新的資源
delete：重新整理全部資源
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
        :param TaskId: 重新整理任務 ID，同一批次提交的目錄共用一個任務 ID
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
    """重新整理任務詳情

    """

    def __init__(self):
        """
        :param TaskId: 重新整理任務 ID
        :type TaskId: str
        :param Url: 重新整理 URL
        :type Url: str
        :param Status: 重新整理任務狀态
fail：重新整理失敗
done：重新整理成功
process：重新整理中
        :type Status: str
        :param PurgeType: 重新整理類型
url：URL 重新整理
path：目錄重新整理
        :type PurgeType: str
        :param FlushType: 重新整理方式
flush：重新整理更新資源（僅目錄重新整理時有此類型）
delete：重新整理全部資源
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
        :param Urls: URL 清單，需要包含協議頭部 http:// 或 https://
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
        :param TaskId: 重新整理任務 ID，同一批次提交的 URL 共用一個任務 ID
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class PushTask(AbstractModel):
    """預熱任務詳情

    """

    def __init__(self):
        """
        :param TaskId: 預熱任務 ID
        :type TaskId: str
        :param Url: 預熱 URL
        :type Url: str
        :param Status: 預熱任務狀态
fail：預熱失敗
done：預熱成功
process：預熱中
        :type Status: str
        :param Percent: 預熱進度百分比
        :type Percent: int
        :param CreateTime: 預熱任務提交時間
        :type CreateTime: str
        :param Area: 預熱區域
mainland：境内
overseas：境外
global：全球
        :type Area: str
        :param UpdateTime: 預熱任務更新時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.TaskId = None
        self.Url = None
        self.Status = None
        self.Percent = None
        self.CreateTime = None
        self.Area = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Url = params.get("Url")
        self.Status = params.get("Status")
        self.Percent = params.get("Percent")
        self.CreateTime = params.get("CreateTime")
        self.Area = params.get("Area")
        self.UpdateTime = params.get("UpdateTime")


class PushUrlsCacheRequest(AbstractModel):
    """PushUrlsCache請求參數結構體

    """

    def __init__(self):
        """
        :param Urls: URL 清單，需要包含協議頭部 http:// 或 https://
        :type Urls: list of str
        :param UserAgent: 指定預熱請求回源時 HTTP 請求的 User-Agent 頭部
預設爲 TencentCdn
        :type UserAgent: str
        :param Area: 預熱生效區域
mainland：預熱至境内節點
overseas：預熱至境外節點
global：預熱全球節點
不填充情況下，預設爲 mainland， URL 中域名必須在對應區域啓用了加速服務才能提交對應區域的預熱任務
        :type Area: str
        """
        self.Urls = None
        self.UserAgent = None
        self.Area = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")
        self.UserAgent = params.get("UserAgent")
        self.Area = params.get("Area")


class PushUrlsCacheResponse(AbstractModel):
    """PushUrlsCache返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 此批提交的任務 ID
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
    """重新整理/預熱 可用量及配額

    """

    def __init__(self):
        """
        :param Batch: 單次批次提交配額上限。
        :type Batch: int
        :param Total: 每日提交配額上限。
        :type Total: int
        :param Available: 每日剩餘的可提交配額。
        :type Available: int
        :param Area: 配額的區域。
        :type Area: str
        """
        self.Batch = None
        self.Total = None
        self.Available = None
        self.Area = None


    def _deserialize(self, params):
        self.Batch = params.get("Batch")
        self.Total = params.get("Total")
        self.Available = params.get("Available")
        self.Area = params.get("Area")


class RangeOriginPull(AbstractModel):
    """分片回源配置，預設爲開啓狀态

    """

    def __init__(self):
        """
        :param Switch: 分片回源配置開關
on：開啓
off：關閉
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class Referer(AbstractModel):
    """Referer 黑白名單配置，預設爲關閉狀态

    """

    def __init__(self):
        """
        :param Switch: referer 黑白名單配置開關
on：開啓
off：關閉
        :type Switch: str
        :param RefererRules: referer 黑白名單配置規則
注意：此欄位可能返回 null，表示取不到有效值。
        :type RefererRules: list of RefererRule
        """
        self.Switch = None
        self.RefererRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("RefererRules") is not None:
            self.RefererRules = []
            for item in params.get("RefererRules"):
                obj = RefererRule()
                obj._deserialize(item)
                self.RefererRules.append(obj)


class RefererRule(AbstractModel):
    """Referer 黑白名單配置規則，針對特定資源生效

    """

    def __init__(self):
        """
        :param RuleType: 規則類型：
all：所有文件生效
file：指定文件後綴生效
directory：指定路徑生效
path：指定絕對路徑生效
        :type RuleType: str
        :param RulePaths: RuleType 對應類型下的比對内容：
all 時填充 *
file 時填充後綴名，如 jpg、txt
directory 時填充路徑，如 /xxx/test/
path 時填充絕對路徑，如 /xxx/test.html
        :type RulePaths: list of str
        :param RefererType: referer 配置類型
whitelist：白名單
blacklist：黑名單
        :type RefererType: str
        :param Referers: referer 内容清單清單
        :type Referers: list of str
        :param AllowEmpty: 是否允許空 referer
true：允許空 referer
false：不允許空 referer
        :type AllowEmpty: bool
        """
        self.RuleType = None
        self.RulePaths = None
        self.RefererType = None
        self.Referers = None
        self.AllowEmpty = None


    def _deserialize(self, params):
        self.RuleType = params.get("RuleType")
        self.RulePaths = params.get("RulePaths")
        self.RefererType = params.get("RefererType")
        self.Referers = params.get("Referers")
        self.AllowEmpty = params.get("AllowEmpty")


class RegionMapRelation(AbstractModel):
    """區域映射id和子區域id的關聯訊息。

    """

    def __init__(self):
        """
        :param RegionId: 區域ID。
        :type RegionId: int
        :param SubRegionIdList: 子區域ID清單
        :type SubRegionIdList: list of int
        """
        self.RegionId = None
        self.SubRegionIdList = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.SubRegionIdList = params.get("SubRegionIdList")


class ReportData(AbstractModel):
    """CDN報表數據

    """

    def __init__(self):
        """
        :param ResourceId: 項目ID/域名ID。
        :type ResourceId: str
        :param Resource: 項目名稱/域名。
        :type Resource: str
        :param Value: 流量總和/頻寬最大值，單位分别爲bytes，bps。
        :type Value: int
        :param Percentage: 單個資源占總體百分比。
        :type Percentage: float
        :param BillingValue: 計費流量總和/計費頻寬最大值，單位分别爲bytes，bps。
        :type BillingValue: int
        :param BillingPercentage: 計費數值占總體百分比。
        :type BillingPercentage: float
        """
        self.ResourceId = None
        self.Resource = None
        self.Value = None
        self.Percentage = None
        self.BillingValue = None
        self.BillingPercentage = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.Resource = params.get("Resource")
        self.Value = params.get("Value")
        self.Percentage = params.get("Percentage")
        self.BillingValue = params.get("BillingValue")
        self.BillingPercentage = params.get("BillingPercentage")


class RequestHeader(AbstractModel):
    """自定義請求頭配置，預設爲關閉狀态

    """

    def __init__(self):
        """
        :param Switch: 自定義請求頭配置開關
on：開啓
off：關閉
        :type Switch: str
        :param HeaderRules: 自定義請求頭配置規則
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


class ResourceBillingData(AbstractModel):
    """計費數據明細

    """

    def __init__(self):
        """
        :param Resource: 資源名稱，根據查詢條件不同分爲以下幾類：
某一個具體域名：表示該域名明細數據
multiDomains：表示多域名匯總明細數據
某一個項目 ID：指定項目查詢時，顯示爲項目 ID
all：賬號維度數據明細
        :type Resource: str
        :param BillingData: 計費數據詳情
        :type BillingData: list of CdnData
        """
        self.Resource = None
        self.BillingData = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        if params.get("BillingData") is not None:
            self.BillingData = []
            for item in params.get("BillingData"):
                obj = CdnData()
                obj._deserialize(item)
                self.BillingData.append(obj)


class ResourceData(AbstractModel):
    """查詢對象及其對應的訪問明細數據

    """

    def __init__(self):
        """
        :param Resource: 資源名稱，根據查詢條件不同分爲以下幾類：
具體域名：表示該域名明細數據
multiDomains：表示多域名匯總明細數據
項目 ID：指定項目查詢時，顯示爲項目 ID
all：賬號維度明細數據
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
all：賬號維度明細數據
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


class ResponseHeader(AbstractModel):
    """自定義響應頭配置，預設爲關閉狀态

    """

    def __init__(self):
        """
        :param Switch: 自定義響應頭開關
on：開啓
off：關閉
        :type Switch: str
        :param HeaderRules: 自定義響應頭規則
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


class ResponseHeaderCache(AbstractModel):
    """源站頭部快取配置，預設爲開啓狀态，快取所有頭部訊息

    """

    def __init__(self):
        """
        :param Switch: 源站頭部快取開關
on：開啓
off：關閉
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class SearchClsLogRequest(AbstractModel):
    """SearchClsLog請求參數結構體

    """

    def __init__(self):
        """
        :param LogsetId: 需要查詢的日志集ID
        :type LogsetId: str
        :param TopicIds: 需要查詢的日志主題ID組合，以逗號分隔
        :type TopicIds: str
        :param StartTime: 需要查詢的日志的起始時間，格式 YYYY-mm-dd HH:MM:SS
        :type StartTime: str
        :param EndTime: 需要查詢的日志的結束時間，格式 YYYY-mm-dd HH:MM:SS
        :type EndTime: str
        :param Limit: 單次要返回的日志條數，單次返回的最大條數爲100
        :type Limit: int
        :param Channel: 接入管道，預設值爲cdn
        :type Channel: str
        :param Query: 需要查詢的内容，詳情請參考https://cloud.taifucloud.com/document/product/614/16982
        :type Query: str
        :param Context: 加載更多使用，透傳上次返回的 context 值，獲取後續的日志内容，通過遊標最多可獲取10000條，請盡可能縮小時間範圍
        :type Context: str
        :param Sort: 按日志時間排序， asc（升序）或者 desc（降序），預設爲 desc
        :type Sort: str
        """
        self.LogsetId = None
        self.TopicIds = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Channel = None
        self.Query = None
        self.Context = None
        self.Sort = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.TopicIds = params.get("TopicIds")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Channel = params.get("Channel")
        self.Query = params.get("Query")
        self.Context = params.get("Context")
        self.Sort = params.get("Sort")


class SearchClsLogResponse(AbstractModel):
    """SearchClsLog返回參數結構體

    """

    def __init__(self):
        """
        :param Logs: 查詢結果
        :type Logs: :class:`taifucloudcloud.cdn.v20180606.models.ClsSearchLogs`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Logs = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Logs") is not None:
            self.Logs = ClsSearchLogs()
            self.Logs._deserialize(params.get("Logs"))
        self.RequestId = params.get("RequestId")


class SecurityConfig(AbstractModel):
    """scdn相關的配置

    """

    def __init__(self):
        """
        :param Switch: on|off
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class Seo(AbstractModel):
    """SEO 搜索引擎優化配置，預設爲關閉狀态

    """

    def __init__(self):
        """
        :param Switch: SEO 配置開關
on：開啓
off：關閉
注意：此欄位可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class ServerCert(AbstractModel):
    """https 加速服務端證書配置：
    + 支援使用托管至 SSL 證書管理的證書進行佈署
    + 支援上傳 PEM 格式的證書進行佈署
    注意：上傳 PEM 證書時，需要進行 Base 64 編碼

    """

    def __init__(self):
        """
        :param CertId: 服務器證書 ID
在 SSL 證書管理進行證書托管時自動生成
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertId: str
        :param CertName: 服務器證書名稱
在 SSL 證書管理進行證書托管時自動生成
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertName: str
        :param Certificate: 服務器證書訊息
上傳自有證書時必填，需要包含完整的證書鏈
注意：此欄位可能返回 null，表示取不到有效值。
        :type Certificate: str
        :param PrivateKey: 服務器金鑰訊息
上傳自有證書時必填
注意：此欄位可能返回 null，表示取不到有效值。
        :type PrivateKey: str
        :param ExpireTime: 證書過期時間
作爲入參配置時無需填充
注意：此欄位可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param DeployTime: 證書頒發時間
作爲入參配置時無需填充
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeployTime: str
        :param Message: 證書備注訊息
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


class SimpleCache(AbstractModel):
    """快取配置基礎版本
    預設情況下所有文件快取過期時間爲 30 天
    預設情況下靜态加速類型的域名 .php;.jsp;.asp;.aspx 不快取
    注意：該版本不支援設置源站未返回 max-age 情況下的快取過期規則設置

    """

    def __init__(self):
        """
        :param CacheRules: 快取過期時間規則
注意：此欄位可能返回 null，表示取不到有效值。
        :type CacheRules: list of SimpleCacheRule
        :param FollowOrigin: 遵循源站 Cache-Control: max-age 配置
on：開啓
off：關閉
開啓後，未能比對 CacheRules 規則的資源将根據源站返回的 max-age 值進行節點快取；比對了 CacheRules 規則的資源将按照 CacheRules 中設置的快取過期時間在節點進行快取
與 CompareMaxAge 沖突，不能同時開啓
注意：此欄位可能返回 null，表示取不到有效值。
        :type FollowOrigin: str
        :param IgnoreCacheControl: 強制快取
on：開啓
off：關閉
預設爲關閉狀态，開啓後，源站發揮的 no-store、no-cache 資源，也将按照 CacheRules 規則進行快取
注意：此欄位可能返回 null，表示取不到有效值。
        :type IgnoreCacheControl: str
        :param IgnoreSetCookie: 忽略源站的Set-Cookie頭部
on：開啓
off：關閉
預設爲關閉狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type IgnoreSetCookie: str
        :param CompareMaxAge: 高級快取過期配置，開啓時會對比源站返回的 max-age 值與 CacheRules 中設置的快取過期時間，取最小值在節點進行快取
on：開啓
off：關閉
預設爲關閉狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type CompareMaxAge: str
        """
        self.CacheRules = None
        self.FollowOrigin = None
        self.IgnoreCacheControl = None
        self.IgnoreSetCookie = None
        self.CompareMaxAge = None


    def _deserialize(self, params):
        if params.get("CacheRules") is not None:
            self.CacheRules = []
            for item in params.get("CacheRules"):
                obj = SimpleCacheRule()
                obj._deserialize(item)
                self.CacheRules.append(obj)
        self.FollowOrigin = params.get("FollowOrigin")
        self.IgnoreCacheControl = params.get("IgnoreCacheControl")
        self.IgnoreSetCookie = params.get("IgnoreSetCookie")
        self.CompareMaxAge = params.get("CompareMaxAge")


class SimpleCacheRule(AbstractModel):
    """快取過期規則配置

    """

    def __init__(self):
        """
        :param CacheType: 規則類型：
all：所有文件生效
file：指定文件後綴生效
directory：指定路徑生效
path：指定絕對路徑生效
index：首頁
        :type CacheType: str
        :param CacheContents: CacheType 對應類型下的比對内容：
all 時填充 *
file 時填充後綴名，如 jpg、txt
directory 時填充路徑，如 /xxx/test/
path 時填充絕對路徑，如 /xxx/test.html
index 時填充 /
        :type CacheContents: list of str
        :param CacheTime: 快取過期時間設置
單位爲秒，最大可設置爲 365 天
        :type CacheTime: int
        """
        self.CacheType = None
        self.CacheContents = None
        self.CacheTime = None


    def _deserialize(self, params):
        self.CacheType = params.get("CacheType")
        self.CacheContents = params.get("CacheContents")
        self.CacheTime = params.get("CacheTime")


class Sort(AbstractModel):
    """查詢結果排序條件

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


class SpecificConfig(AbstractModel):
    """域名國内海外分地區特殊配置。

    """

    def __init__(self):
        """
        :param Mainland: 國内特殊配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Mainland: :class:`taifucloudcloud.cdn.v20180606.models.MainlandConfig`
        :param Overseas: 海外特殊配置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Overseas: :class:`taifucloudcloud.cdn.v20180606.models.OverseaConfig`
        """
        self.Mainland = None
        self.Overseas = None


    def _deserialize(self, params):
        if params.get("Mainland") is not None:
            self.Mainland = MainlandConfig()
            self.Mainland._deserialize(params.get("Mainland"))
        if params.get("Overseas") is not None:
            self.Overseas = OverseaConfig()
            self.Overseas._deserialize(params.get("Overseas"))


class StartCdnDomainRequest(AbstractModel):
    """StartCdnDomain請求參數結構體

    """

    def __init__(self):
        """
        :param Domain: 域名
域名狀态需要爲【已停用】
        :type Domain: str
        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")


class StartCdnDomainResponse(AbstractModel):
    """StartCdnDomain返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StatusCodeCache(AbstractModel):
    """狀态碼快取過期配置，預設情況下會對 404 狀态碼快取 10 秒

    """

    def __init__(self):
        """
        :param Switch: 狀态碼快取過期配置開關
on：開啓
off：關閉
注意：此欄位可能返回 null，表示取不到有效值。
        :type Switch: str
        :param CacheRules: 狀态碼快取過期規則明細
注意：此欄位可能返回 null，表示取不到有效值。
        :type CacheRules: list of StatusCodeCacheRule
        """
        self.Switch = None
        self.CacheRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("CacheRules") is not None:
            self.CacheRules = []
            for item in params.get("CacheRules"):
                obj = StatusCodeCacheRule()
                obj._deserialize(item)
                self.CacheRules.append(obj)


class StatusCodeCacheRule(AbstractModel):
    """狀态碼快取過期時間規則配置

    """

    def __init__(self):
        """
        :param StatusCode: http 狀态碼
支援 403、404 狀态碼
        :type StatusCode: str
        :param CacheTime: 狀态碼快取過期時間，單位秒
        :type CacheTime: int
        """
        self.StatusCode = None
        self.CacheTime = None


    def _deserialize(self, params):
        self.StatusCode = params.get("StatusCode")
        self.CacheTime = params.get("CacheTime")


class StopCdnDomainRequest(AbstractModel):
    """StopCdnDomain請求參數結構體

    """

    def __init__(self):
        """
        :param Domain: 域名
域名需要爲【已啓動】狀态
        :type Domain: str
        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")


class StopCdnDomainResponse(AbstractModel):
    """StopCdnDomain返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SummarizedData(AbstractModel):
    """明細數據的匯總值，各指標根據其特性不同擁有不同匯總方式

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
all：賬號維度明細數據
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


class TopicInfo(AbstractModel):
    """CLS主題訊息

    """

    def __init__(self):
        """
        :param TopicId: 主題ID
        :type TopicId: str
        :param TopicName: 主題名字
        :type TopicName: str
        :param Enabled: 是否啓用投遞
        :type Enabled: int
        :param CreateTime: 創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self.TopicId = None
        self.TopicName = None
        self.Enabled = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.Enabled = params.get("Enabled")
        self.CreateTime = params.get("CreateTime")


class TpgAdapter(AbstractModel):
    """圖片優化-TpgAdapter配置

    """

    def __init__(self):
        """
        :param Switch: 開關，"on/off"
注意：此欄位可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class TrafficPackage(AbstractModel):
    """CDN加速流量包。

    """

    def __init__(self):
        """
        :param Id: 流量包 Id
        :type Id: int
        :param Type: 流量包類型
        :type Type: str
        :param Bytes: 流量包大小（單位爲 Byte）
        :type Bytes: int
        :param BytesUsed: 已消耗流量（單位爲 Byte）
        :type BytesUsed: int
        :param Status: 流量包狀态
enabled：已啓用
expired：已過期
disabled：未啓用
        :type Status: str
        :param CreateTime: 流量包發放時間
        :type CreateTime: str
        :param EnableTime: 流量包生效時間
        :type EnableTime: str
        :param ExpireTime: 流量包過期時間
        :type ExpireTime: str
        :param ContractExtension: 流量包是否續訂
        :type ContractExtension: bool
        :param AutoExtension: 流量包是否自動續訂
        :type AutoExtension: bool
        :param Channel: 流量包來源
        :type Channel: str
        """
        self.Id = None
        self.Type = None
        self.Bytes = None
        self.BytesUsed = None
        self.Status = None
        self.CreateTime = None
        self.EnableTime = None
        self.ExpireTime = None
        self.ContractExtension = None
        self.AutoExtension = None
        self.Channel = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Bytes = params.get("Bytes")
        self.BytesUsed = params.get("BytesUsed")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.EnableTime = params.get("EnableTime")
        self.ExpireTime = params.get("ExpireTime")
        self.ContractExtension = params.get("ContractExtension")
        self.AutoExtension = params.get("AutoExtension")
        self.Channel = params.get("Channel")


class UpdateDomainConfigRequest(AbstractModel):
    """UpdateDomainConfig請求參數結構體

    """

    def __init__(self):
        """
        :param Domain: 域名
        :type Domain: str
        :param ProjectId: 項目 ID
        :type ProjectId: int
        :param Origin: 源站配置
        :type Origin: :class:`taifucloudcloud.cdn.v20180606.models.Origin`
        :param IpFilter: IP 黑白名單配置
        :type IpFilter: :class:`taifucloudcloud.cdn.v20180606.models.IpFilter`
        :param IpFreqLimit: IP 限頻配置
        :type IpFreqLimit: :class:`taifucloudcloud.cdn.v20180606.models.IpFreqLimit`
        :param StatusCodeCache: 狀态碼快取配置
        :type StatusCodeCache: :class:`taifucloudcloud.cdn.v20180606.models.StatusCodeCache`
        :param Compression: 智慧壓縮配置
        :type Compression: :class:`taifucloudcloud.cdn.v20180606.models.Compression`
        :param BandwidthAlert: 頻寬封頂配置
        :type BandwidthAlert: :class:`taifucloudcloud.cdn.v20180606.models.BandwidthAlert`
        :param RangeOriginPull: Range 回源配置
        :type RangeOriginPull: :class:`taifucloudcloud.cdn.v20180606.models.RangeOriginPull`
        :param FollowRedirect: 301/302 回源跟随配置
        :type FollowRedirect: :class:`taifucloudcloud.cdn.v20180606.models.FollowRedirect`
        :param ErrorPage: 錯誤碼重定向配置（功能灰度中，尚未全量）
        :type ErrorPage: :class:`taifucloudcloud.cdn.v20180606.models.ErrorPage`
        :param RequestHeader: 請求頭部配置
        :type RequestHeader: :class:`taifucloudcloud.cdn.v20180606.models.RequestHeader`
        :param ResponseHeader: 響應頭部配置
        :type ResponseHeader: :class:`taifucloudcloud.cdn.v20180606.models.ResponseHeader`
        :param DownstreamCapping: 下載速度配置
        :type DownstreamCapping: :class:`taifucloudcloud.cdn.v20180606.models.DownstreamCapping`
        :param CacheKey: 節點快取鍵配置
        :type CacheKey: :class:`taifucloudcloud.cdn.v20180606.models.CacheKey`
        :param ResponseHeaderCache: 頭部快取配置
        :type ResponseHeaderCache: :class:`taifucloudcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param VideoSeek: 視訊拖拽配置
        :type VideoSeek: :class:`taifucloudcloud.cdn.v20180606.models.VideoSeek`
        :param Cache: 快取過期時間配置
        :type Cache: :class:`taifucloudcloud.cdn.v20180606.models.Cache`
        :param OriginPullOptimization: 跨國鏈路優化配置
        :type OriginPullOptimization: :class:`taifucloudcloud.cdn.v20180606.models.OriginPullOptimization`
        :param Https: Https 加速配置
        :type Https: :class:`taifucloudcloud.cdn.v20180606.models.Https`
        :param Authentication: 時間戳防盜鏈配置
        :type Authentication: :class:`taifucloudcloud.cdn.v20180606.models.Authentication`
        :param Seo: SEO 優化配置
        :type Seo: :class:`taifucloudcloud.cdn.v20180606.models.Seo`
        :param ForceRedirect: 訪問協議強制跳轉配置
        :type ForceRedirect: :class:`taifucloudcloud.cdn.v20180606.models.ForceRedirect`
        :param Referer: Referer 防盜鏈配置
        :type Referer: :class:`taifucloudcloud.cdn.v20180606.models.Referer`
        :param MaxAge: 浏覽器快取配置（功能灰度中，尚未全量）
        :type MaxAge: :class:`taifucloudcloud.cdn.v20180606.models.MaxAge`
        :param ServiceType: 域名業務類型
web：靜态加速
download：下載加速
media：流媒體點播加速
        :type ServiceType: str
        :param SpecificConfig: 地域屬性特殊配置
适用於域名境内加速、境外加速配置不一緻場景
        :type SpecificConfig: :class:`taifucloudcloud.cdn.v20180606.models.SpecificConfig`
        :param Area: 域名加速區域
mainland： 境内加速
overseas： 境外加速
global：全球加速
        :type Area: str
        :param OriginPullTimeout: 回源超時配置
        :type OriginPullTimeout: :class:`taifucloudcloud.cdn.v20180606.models.OriginPullTimeout`
        :param AwsPrivateAccess: 回源S3私有鑒權
        :type AwsPrivateAccess: :class:`taifucloudcloud.cdn.v20180606.models.AwsPrivateAccess`
        """
        self.Domain = None
        self.ProjectId = None
        self.Origin = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.StatusCodeCache = None
        self.Compression = None
        self.BandwidthAlert = None
        self.RangeOriginPull = None
        self.FollowRedirect = None
        self.ErrorPage = None
        self.RequestHeader = None
        self.ResponseHeader = None
        self.DownstreamCapping = None
        self.CacheKey = None
        self.ResponseHeaderCache = None
        self.VideoSeek = None
        self.Cache = None
        self.OriginPullOptimization = None
        self.Https = None
        self.Authentication = None
        self.Seo = None
        self.ForceRedirect = None
        self.Referer = None
        self.MaxAge = None
        self.ServiceType = None
        self.SpecificConfig = None
        self.Area = None
        self.OriginPullTimeout = None
        self.AwsPrivateAccess = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.ProjectId = params.get("ProjectId")
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        if params.get("IpFilter") is not None:
            self.IpFilter = IpFilter()
            self.IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self.IpFreqLimit = IpFreqLimit()
            self.IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("StatusCodeCache") is not None:
            self.StatusCodeCache = StatusCodeCache()
            self.StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("BandwidthAlert") is not None:
            self.BandwidthAlert = BandwidthAlert()
            self.BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("RangeOriginPull") is not None:
            self.RangeOriginPull = RangeOriginPull()
            self.RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("FollowRedirect") is not None:
            self.FollowRedirect = FollowRedirect()
            self.FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ErrorPage") is not None:
            self.ErrorPage = ErrorPage()
            self.ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("RequestHeader") is not None:
            self.RequestHeader = RequestHeader()
            self.RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("DownstreamCapping") is not None:
            self.DownstreamCapping = DownstreamCapping()
            self.DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("ResponseHeaderCache") is not None:
            self.ResponseHeaderCache = ResponseHeaderCache()
            self.ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("VideoSeek") is not None:
            self.VideoSeek = VideoSeek()
            self.VideoSeek._deserialize(params.get("VideoSeek"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("OriginPullOptimization") is not None:
            self.OriginPullOptimization = OriginPullOptimization()
            self.OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("Authentication") is not None:
            self.Authentication = Authentication()
            self.Authentication._deserialize(params.get("Authentication"))
        if params.get("Seo") is not None:
            self.Seo = Seo()
            self.Seo._deserialize(params.get("Seo"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Referer") is not None:
            self.Referer = Referer()
            self.Referer._deserialize(params.get("Referer"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        self.ServiceType = params.get("ServiceType")
        if params.get("SpecificConfig") is not None:
            self.SpecificConfig = SpecificConfig()
            self.SpecificConfig._deserialize(params.get("SpecificConfig"))
        self.Area = params.get("Area")
        if params.get("OriginPullTimeout") is not None:
            self.OriginPullTimeout = OriginPullTimeout()
            self.OriginPullTimeout._deserialize(params.get("OriginPullTimeout"))
        if params.get("AwsPrivateAccess") is not None:
            self.AwsPrivateAccess = AwsPrivateAccess()
            self.AwsPrivateAccess._deserialize(params.get("AwsPrivateAccess"))


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


class UpdateImageConfigRequest(AbstractModel):
    """UpdateImageConfig請求參數結構體

    """

    def __init__(self):
        """
        :param Domain: 域名
        :type Domain: str
        :param WebpAdapter: WebpAdapter配置項
        :type WebpAdapter: :class:`taifucloudcloud.cdn.v20180606.models.WebpAdapter`
        :param TpgAdapter: TpgAdapter配置項
        :type TpgAdapter: :class:`taifucloudcloud.cdn.v20180606.models.TpgAdapter`
        :param GuetzliAdapter: GuetzliAdapter配置項
        :type GuetzliAdapter: :class:`taifucloudcloud.cdn.v20180606.models.GuetzliAdapter`
        """
        self.Domain = None
        self.WebpAdapter = None
        self.TpgAdapter = None
        self.GuetzliAdapter = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        if params.get("WebpAdapter") is not None:
            self.WebpAdapter = WebpAdapter()
            self.WebpAdapter._deserialize(params.get("WebpAdapter"))
        if params.get("TpgAdapter") is not None:
            self.TpgAdapter = TpgAdapter()
            self.TpgAdapter._deserialize(params.get("TpgAdapter"))
        if params.get("GuetzliAdapter") is not None:
            self.GuetzliAdapter = GuetzliAdapter()
            self.GuetzliAdapter._deserialize(params.get("GuetzliAdapter"))


class UpdateImageConfigResponse(AbstractModel):
    """UpdateImageConfig返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdatePayTypeRequest(AbstractModel):
    """UpdatePayType請求參數結構體

    """

    def __init__(self):
        """
        :param Area: 計費區域，mainland或overseas。
        :type Area: str
        :param PayType: 計費類型，flux或bandwidth。
        :type PayType: str
        """
        self.Area = None
        self.PayType = None


    def _deserialize(self, params):
        self.Area = params.get("Area")
        self.PayType = params.get("PayType")


class UpdatePayTypeResponse(AbstractModel):
    """UpdatePayType返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


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


class VideoSeek(AbstractModel):
    """視訊拖拽配置，預設爲關閉狀态

    """

    def __init__(self):
        """
        :param Switch: 視訊拖拽開關
on：開啓
off：關閉
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class ViolationUrl(AbstractModel):
    """違規 URL 詳情

    """

    def __init__(self):
        """
        :param Id: ID
        :type Id: int
        :param RealUrl: 違規資源原始訪問 URL
        :type RealUrl: str
        :param DownloadUrl: 快照路徑，用於控制台展示違規内容快照
        :type DownloadUrl: str
        :param UrlStatus: 違規資源當前狀态
forbid：已封禁
release：已解封
delay ： 延遲處理
reject ：申訴駁回，狀态仍爲封禁态
complain：申訴進行中
        :type UrlStatus: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param UpdateTime: 更新時間
        :type UpdateTime: str
        """
        self.Id = None
        self.RealUrl = None
        self.DownloadUrl = None
        self.UrlStatus = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RealUrl = params.get("RealUrl")
        self.DownloadUrl = params.get("DownloadUrl")
        self.UrlStatus = params.get("UrlStatus")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class WebpAdapter(AbstractModel):
    """圖片優化-WebpAdapter配置

    """

    def __init__(self):
        """
        :param Switch: 開關，"on/off"
注意：此欄位可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")