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


class AccessRegionDetial(AbstractModel):
    """根據源站查詢的可用加速區域訊息及對應的可選頻寬和並發量

    """

    def __init__(self):
        """
        :param RegionId: 區域ID
        :type RegionId: str
        :param RegionName: 區域的中文或英文名稱
        :type RegionName: str
        :param ConcurrentList: 可選的並發量取值數組
        :type ConcurrentList: list of int
        :param BandwidthList: 可選的頻寬取值數組
        :type BandwidthList: list of int
        """
        self.RegionId = None
        self.RegionName = None
        self.ConcurrentList = None
        self.BandwidthList = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        self.ConcurrentList = params.get("ConcurrentList")
        self.BandwidthList = params.get("BandwidthList")


class AccessRegionDomainConf(AbstractModel):
    """域名就近接入配置

    """

    def __init__(self):
        """
        :param RegionId: 地域ID。
        :type RegionId: str
        :param NationCountryInnerList: 就近接入區域國家内部編碼，編碼清單可通過DescribeCountryAreaMapping介面獲取。
        :type NationCountryInnerList: list of str
        """
        self.RegionId = None
        self.NationCountryInnerList = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.NationCountryInnerList = params.get("NationCountryInnerList")


class AddRealServersRequest(AbstractModel):
    """AddRealServers請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: 源站對應的項目ID
        :type ProjectId: int
        :param RealServerIP: 源站對應的IP或域名
        :type RealServerIP: list of str
        :param RealServerName: 源站名稱
        :type RealServerName: str
        :param TagSet: 標簽清單
        :type TagSet: list of TagPair
        """
        self.ProjectId = None
        self.RealServerIP = None
        self.RealServerName = None
        self.TagSet = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.RealServerIP = params.get("RealServerIP")
        self.RealServerName = params.get("RealServerName")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self.TagSet.append(obj)


class AddRealServersResponse(AbstractModel):
    """AddRealServers返回參數結構體

    """

    def __init__(self):
        """
        :param RealServerSet: 源站訊息清單
        :type RealServerSet: list of NewRealServer
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RealServerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RealServerSet") is not None:
            self.RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = NewRealServer()
                obj._deserialize(item)
                self.RealServerSet.append(obj)
        self.RequestId = params.get("RequestId")


class BandwidthPriceGradient(AbstractModel):
    """頻寬梯度價格

    """

    def __init__(self):
        """
        :param BandwidthRange: 頻寬範圍。
        :type BandwidthRange: list of int
        :param BandwidthUnitPrice: 在對應頻寬範圍内的單寬單價，單位：元/Mbps/天。
        :type BandwidthUnitPrice: float
        """
        self.BandwidthRange = None
        self.BandwidthUnitPrice = None


    def _deserialize(self, params):
        self.BandwidthRange = params.get("BandwidthRange")
        self.BandwidthUnitPrice = params.get("BandwidthUnitPrice")


class BindListenerRealServersRequest(AbstractModel):
    """BindListenerRealServers請求參數結構體

    """

    def __init__(self):
        """
        :param ListenerId: 監聽器ID
        :type ListenerId: str
        :param RealServerBindSet: 待綁定源站清單。如果該監聽器的源站調度策略是加權輪詢，需要填寫源站權重 RealServerWeight, 不填或者其他調度類型預設源站權重爲1。
        :type RealServerBindSet: list of RealServerBindSetReq
        """
        self.ListenerId = None
        self.RealServerBindSet = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        if params.get("RealServerBindSet") is not None:
            self.RealServerBindSet = []
            for item in params.get("RealServerBindSet"):
                obj = RealServerBindSetReq()
                obj._deserialize(item)
                self.RealServerBindSet.append(obj)


class BindListenerRealServersResponse(AbstractModel):
    """BindListenerRealServers返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BindRealServer(AbstractModel):
    """已綁定的源站訊息

    """

    def __init__(self):
        """
        :param RealServerId: 源站ID
        :type RealServerId: str
        :param RealServerIP: 源站IP或者域名
        :type RealServerIP: str
        :param RealServerWeight: 該源站所占權重
        :type RealServerWeight: int
        :param RealServerStatus: 源站健康檢查狀态，其中：
0表示正常；
1表示異常。
未開啓健康檢查狀态時，該狀态始終爲正常。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RealServerStatus: int
        :param RealServerPort: 源站的端口號
注意：此欄位可能返回 null，表示取不到有效值。
        :type RealServerPort: int
        :param DownIPList: 當源站爲域名時，域名被解析成一個或者多個IP，該欄位表示其中異常的IP清單。狀态異常，但該欄位爲空時，表示域名解析異常。
        :type DownIPList: list of str
        """
        self.RealServerId = None
        self.RealServerIP = None
        self.RealServerWeight = None
        self.RealServerStatus = None
        self.RealServerPort = None
        self.DownIPList = None


    def _deserialize(self, params):
        self.RealServerId = params.get("RealServerId")
        self.RealServerIP = params.get("RealServerIP")
        self.RealServerWeight = params.get("RealServerWeight")
        self.RealServerStatus = params.get("RealServerStatus")
        self.RealServerPort = params.get("RealServerPort")
        self.DownIPList = params.get("DownIPList")


class BindRealServerInfo(AbstractModel):
    """添加源站的源站訊息返回值

    """

    def __init__(self):
        """
        :param RealServerIP: 源站的IP或域名
        :type RealServerIP: str
        :param RealServerId: 源站ID
        :type RealServerId: str
        :param RealServerName: 源站名稱
        :type RealServerName: str
        :param ProjectId: 項目ID
        :type ProjectId: int
        :param TagSet: 標簽清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagSet: list of TagPair
        """
        self.RealServerIP = None
        self.RealServerId = None
        self.RealServerName = None
        self.ProjectId = None
        self.TagSet = None


    def _deserialize(self, params):
        self.RealServerIP = params.get("RealServerIP")
        self.RealServerId = params.get("RealServerId")
        self.RealServerName = params.get("RealServerName")
        self.ProjectId = params.get("ProjectId")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self.TagSet.append(obj)


class BindRuleRealServersRequest(AbstractModel):
    """BindRuleRealServers請求參數結構體

    """

    def __init__(self):
        """
        :param RuleId: 轉發規則ID
        :type RuleId: str
        :param RealServerBindSet: 需要綁定的源站訊息清單。
如果已經存在綁定的源站，則會函蓋更新成這個源站清單。
當不帶該欄位時，表示解綁該規則上的所有源站。
如果該規則的源站調度策略是加權輪詢，需要填寫源站權重 RealServerWeight, 不填或者其他調度類型預設源站權重爲1。
        :type RealServerBindSet: list of RealServerBindSetReq
        """
        self.RuleId = None
        self.RealServerBindSet = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        if params.get("RealServerBindSet") is not None:
            self.RealServerBindSet = []
            for item in params.get("RealServerBindSet"):
                obj = RealServerBindSetReq()
                obj._deserialize(item)
                self.RealServerBindSet.append(obj)


class BindRuleRealServersResponse(AbstractModel):
    """BindRuleRealServers返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Certificate(AbstractModel):
    """服務器證書

    """

    def __init__(self):
        """
        :param CertificateId: 證書ID
        :type CertificateId: str
        :param CertificateName: 證書名稱（舊參數，請使用CertificateAlias）。
        :type CertificateName: str
        :param CertificateType: 證書類型。
        :type CertificateType: int
        :param CertificateAlias: 證書名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertificateAlias: str
        :param CreateTime: 證書創建時間，采用Unix時間戳的方式，表示從1970年1月1日（UTC/GMT的午夜）開始所經過的秒數。
        :type CreateTime: int
        :param BeginTime: 證書生效起始時間，采用Unix時間戳的方式，表示從1970年1月1日（UTC/GMT的午夜）開始所經過的秒數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type BeginTime: int
        :param EndTime: 證書過期時間，采用Unix時間戳的方式，表示從1970年1月1日（UTC/GMT的午夜）開始所經過的秒數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type EndTime: int
        :param IssuerCN: 證書簽發者通用名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IssuerCN: str
        :param SubjectCN: 證書主題通用名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubjectCN: str
        """
        self.CertificateId = None
        self.CertificateName = None
        self.CertificateType = None
        self.CertificateAlias = None
        self.CreateTime = None
        self.BeginTime = None
        self.EndTime = None
        self.IssuerCN = None
        self.SubjectCN = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.CertificateName = params.get("CertificateName")
        self.CertificateType = params.get("CertificateType")
        self.CertificateAlias = params.get("CertificateAlias")
        self.CreateTime = params.get("CreateTime")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.IssuerCN = params.get("IssuerCN")
        self.SubjectCN = params.get("SubjectCN")


class CertificateAliasInfo(AbstractModel):
    """證書别名訊息

    """

    def __init__(self):
        """
        :param CertificateId: 證書ID
        :type CertificateId: str
        :param CertificateAlias: 證書别名
        :type CertificateAlias: str
        """
        self.CertificateId = None
        self.CertificateAlias = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.CertificateAlias = params.get("CertificateAlias")


class CertificateDetail(AbstractModel):
    """證書詳情，包括證書ID， 證書名字，證書類型，證書内容以及金鑰内容。

    """

    def __init__(self):
        """
        :param CertificateId: 證書ID。
        :type CertificateId: str
        :param CertificateType: 證書類型。
        :type CertificateType: int
        :param CertificateAlias: 證書名字。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertificateAlias: str
        :param CertificateContent: 證書内容。
        :type CertificateContent: str
        :param CertificateKey: 金鑰内容。僅當證書類型爲SSL證書時，返回該欄位。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertificateKey: str
        :param CreateTime: 創建時間，采用Unix時間戳的方式，表示從1970年1月1日（UTC/GMT的午夜）開始所經過的秒數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param BeginTime: 證書生效起始時間，采用Unix時間戳的方式，表示從1970年1月1日（UTC/GMT的午夜）開始所經過的秒數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type BeginTime: int
        :param EndTime: 證書過期時間，采用Unix時間戳的方式，表示從1970年1月1日（UTC/GMT的午夜）開始所經過的秒數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type EndTime: int
        :param IssuerCN: 證書簽發者通用名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IssuerCN: str
        :param SubjectCN: 證書主題通用名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubjectCN: str
        """
        self.CertificateId = None
        self.CertificateType = None
        self.CertificateAlias = None
        self.CertificateContent = None
        self.CertificateKey = None
        self.CreateTime = None
        self.BeginTime = None
        self.EndTime = None
        self.IssuerCN = None
        self.SubjectCN = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.CertificateType = params.get("CertificateType")
        self.CertificateAlias = params.get("CertificateAlias")
        self.CertificateContent = params.get("CertificateContent")
        self.CertificateKey = params.get("CertificateKey")
        self.CreateTime = params.get("CreateTime")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.IssuerCN = params.get("IssuerCN")
        self.SubjectCN = params.get("SubjectCN")


class CheckProxyCreateRequest(AbstractModel):
    """CheckProxyCreate請求參數結構體

    """

    def __init__(self):
        """
        :param AccessRegion: 通道的接入(加速)區域。取值可通過介面DescribeAccessRegionsByDestRegion獲取到
        :type AccessRegion: str
        :param RealServerRegion: 通道的源站區域。取值可通過介面DescribeDestRegions獲取到
        :type RealServerRegion: str
        :param Bandwidth: 通道頻寬上限，單位：Mbps。
        :type Bandwidth: int
        :param Concurrent: 通道並發量上限，表示同時在線的連接數，單位：萬。
        :type Concurrent: int
        """
        self.AccessRegion = None
        self.RealServerRegion = None
        self.Bandwidth = None
        self.Concurrent = None


    def _deserialize(self, params):
        self.AccessRegion = params.get("AccessRegion")
        self.RealServerRegion = params.get("RealServerRegion")
        self.Bandwidth = params.get("Bandwidth")
        self.Concurrent = params.get("Concurrent")


class CheckProxyCreateResponse(AbstractModel):
    """CheckProxyCreate返回參數結構體

    """

    def __init__(self):
        """
        :param CheckFlag: 查詢能否創建給定配置的通道，1可以創建，0不可創建。
        :type CheckFlag: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CheckFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CheckFlag = params.get("CheckFlag")
        self.RequestId = params.get("RequestId")


class CloseProxiesRequest(AbstractModel):
    """CloseProxies請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: （舊參數，請切換到ProxyIds）通道的實例ID。
        :type InstanceIds: list of str
        :param ClientToken: 用於保證請求幂等性的字串。該字串由客戶生成，需保證不同請求之間唯一，最大值不超過64個ASCII字元。若不指定該參數，則無法保證請求的幂等性。
更多詳細訊息請參閱：如何保證幂等性。
        :type ClientToken: str
        :param ProxyIds: （新參數）通道的實例ID。
        :type ProxyIds: list of str
        """
        self.InstanceIds = None
        self.ClientToken = None
        self.ProxyIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.ClientToken = params.get("ClientToken")
        self.ProxyIds = params.get("ProxyIds")


class CloseProxiesResponse(AbstractModel):
    """CloseProxies返回參數結構體

    """

    def __init__(self):
        """
        :param InvalidStatusInstanceSet: 非運作狀态下的通道實例ID清單，不可開啓。
        :type InvalidStatusInstanceSet: list of str
        :param OperationFailedInstanceSet: 開啓操作失敗的通道實例ID清單。
        :type OperationFailedInstanceSet: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InvalidStatusInstanceSet = None
        self.OperationFailedInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InvalidStatusInstanceSet = params.get("InvalidStatusInstanceSet")
        self.OperationFailedInstanceSet = params.get("OperationFailedInstanceSet")
        self.RequestId = params.get("RequestId")


class CloseSecurityPolicyRequest(AbstractModel):
    """CloseSecurityPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param ProxyId: 通道ID
        :type ProxyId: str
        """
        self.ProxyId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")


class CloseSecurityPolicyResponse(AbstractModel):
    """CloseSecurityPolicy返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步流程ID，可以通過DescribeAsyncTaskStatus 查詢流程執行進展和狀态
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CountryAreaMap(AbstractModel):
    """國家地區映射關系（名稱和編碼）

    """

    def __init__(self):
        """
        :param NationCountryName: 國家名稱。
        :type NationCountryName: str
        :param NationCountryInnerCode: 國家編碼。
        :type NationCountryInnerCode: str
        :param GeographicalZoneName: 地區名稱。
        :type GeographicalZoneName: str
        :param GeographicalZoneInnerCode: 地區編碼。
        :type GeographicalZoneInnerCode: str
        :param ContinentName: 大洲名稱。
        :type ContinentName: str
        :param ContinentInnerCode: 大洲編碼。
        :type ContinentInnerCode: str
        """
        self.NationCountryName = None
        self.NationCountryInnerCode = None
        self.GeographicalZoneName = None
        self.GeographicalZoneInnerCode = None
        self.ContinentName = None
        self.ContinentInnerCode = None


    def _deserialize(self, params):
        self.NationCountryName = params.get("NationCountryName")
        self.NationCountryInnerCode = params.get("NationCountryInnerCode")
        self.GeographicalZoneName = params.get("GeographicalZoneName")
        self.GeographicalZoneInnerCode = params.get("GeographicalZoneInnerCode")
        self.ContinentName = params.get("ContinentName")
        self.ContinentInnerCode = params.get("ContinentInnerCode")


class CreateCertificateRequest(AbstractModel):
    """CreateCertificate請求參數結構體

    """

    def __init__(self):
        """
        :param CertificateType: 證書類型。其中：
0，表示基礎認證配置；
1，表示用戶端CA證書；
2，服務器SSL證書；
3，表示源站CA證書；
4，表示通道SSL證書。
        :type CertificateType: int
        :param CertificateContent: 證書内容。采用url編碼。其中：
當證書類型爲基礎認證配置時，該參數填寫用戶名/密碼對。格式：“用戶名：密碼”，例如：root:FSGdT。其中密碼使用htpasswd或者openssl，例如：openssl passwd -crypt 123456。
當證書類型爲CA/SSL證書時，該參數填寫證書内容，格式爲pem。
        :type CertificateContent: str
        :param CertificateAlias: 證書名稱
        :type CertificateAlias: str
        :param CertificateKey: 金鑰内容。采用url編碼。僅當證書類型爲SSL證書時，需要填寫該參數。格式爲pem。
        :type CertificateKey: str
        """
        self.CertificateType = None
        self.CertificateContent = None
        self.CertificateAlias = None
        self.CertificateKey = None


    def _deserialize(self, params):
        self.CertificateType = params.get("CertificateType")
        self.CertificateContent = params.get("CertificateContent")
        self.CertificateAlias = params.get("CertificateAlias")
        self.CertificateKey = params.get("CertificateKey")


class CreateCertificateResponse(AbstractModel):
    """CreateCertificate返回參數結構體

    """

    def __init__(self):
        """
        :param CertificateId: 證書ID
        :type CertificateId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class CreateDomainErrorPageInfoRequest(AbstractModel):
    """CreateDomainErrorPageInfo請求參數結構體

    """

    def __init__(self):
        """
        :param ListenerId: 監聽器ID
        :type ListenerId: str
        :param Domain: 域名
        :type Domain: str
        :param ErrorNos: 原始錯誤碼
        :type ErrorNos: list of int
        :param Body: 新的響應包體
        :type Body: str
        :param NewErrorNo: 新錯誤碼
        :type NewErrorNo: int
        :param ClearHeaders: 需要删除的響應頭
        :type ClearHeaders: list of str
        :param SetHeaders: 需要設置的響應頭
        :type SetHeaders: list of HttpHeaderParam
        """
        self.ListenerId = None
        self.Domain = None
        self.ErrorNos = None
        self.Body = None
        self.NewErrorNo = None
        self.ClearHeaders = None
        self.SetHeaders = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.ErrorNos = params.get("ErrorNos")
        self.Body = params.get("Body")
        self.NewErrorNo = params.get("NewErrorNo")
        self.ClearHeaders = params.get("ClearHeaders")
        if params.get("SetHeaders") is not None:
            self.SetHeaders = []
            for item in params.get("SetHeaders"):
                obj = HttpHeaderParam()
                obj._deserialize(item)
                self.SetHeaders.append(obj)


class CreateDomainErrorPageInfoResponse(AbstractModel):
    """CreateDomainErrorPageInfo返回參數結構體

    """

    def __init__(self):
        """
        :param ErrorPageId: 錯誤定制響應的配置ID
        :type ErrorPageId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ErrorPageId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorPageId = params.get("ErrorPageId")
        self.RequestId = params.get("RequestId")


class CreateDomainRequest(AbstractModel):
    """CreateDomain請求參數結構體

    """

    def __init__(self):
        """
        :param ListenerId: 監聽器ID。
        :type ListenerId: str
        :param Domain: 需要創建的域名，一個監聽器下最大支援100個域名。
        :type Domain: str
        :param CertificateId: 服務器證書，用於用戶端與GAAP的HTTPS的交互。
        :type CertificateId: str
        :param ClientCertificateId: 用戶端CA證書，用於用戶端與GAAP的HTTPS的交互。
僅當采用雙向認證的方式時，需要設置該欄位或PolyClientCertificateIds欄位。
        :type ClientCertificateId: str
        :param PolyClientCertificateIds: 用戶端CA證書，用於用戶端與GAAP的HTTPS的交互。
僅當采用雙向認證的方式時，需要設置該欄位或ClientCertificateId欄位。
        :type PolyClientCertificateIds: list of str
        """
        self.ListenerId = None
        self.Domain = None
        self.CertificateId = None
        self.ClientCertificateId = None
        self.PolyClientCertificateIds = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.CertificateId = params.get("CertificateId")
        self.ClientCertificateId = params.get("ClientCertificateId")
        self.PolyClientCertificateIds = params.get("PolyClientCertificateIds")


class CreateDomainResponse(AbstractModel):
    """CreateDomain返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateHTTPListenerRequest(AbstractModel):
    """CreateHTTPListener請求參數結構體

    """

    def __init__(self):
        """
        :param ListenerName: 監聽器名稱
        :type ListenerName: str
        :param Port: 監聽器端口，基於同種傳輸層協議（TCP 或 UDP）的監聽器，端口不可重複
        :type Port: int
        :param ProxyId: 通道ID
        :type ProxyId: str
        """
        self.ListenerName = None
        self.Port = None
        self.ProxyId = None


    def _deserialize(self, params):
        self.ListenerName = params.get("ListenerName")
        self.Port = params.get("Port")
        self.ProxyId = params.get("ProxyId")


class CreateHTTPListenerResponse(AbstractModel):
    """CreateHTTPListener返回參數結構體

    """

    def __init__(self):
        """
        :param ListenerId: 創建的監聽器ID
        :type ListenerId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ListenerId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.RequestId = params.get("RequestId")


class CreateHTTPSListenerRequest(AbstractModel):
    """CreateHTTPSListener請求參數結構體

    """

    def __init__(self):
        """
        :param ListenerName: 監聽器名稱
        :type ListenerName: str
        :param Port: 監聽器端口，基於同種傳輸層協議（TCP 或 UDP）的監聽器，端口不可重複
        :type Port: int
        :param CertificateId: 服務器證書ID
        :type CertificateId: str
        :param ForwardProtocol: 加速通道轉發到源站的協議類型：HTTP | HTTPS
        :type ForwardProtocol: str
        :param ProxyId: 通道ID
        :type ProxyId: str
        :param AuthType: 認證類型，其中：
0，單向認證；
1，雙向認證。
預設使用單向認證。
        :type AuthType: int
        :param ClientCertificateId: 用戶端CA單證書ID，僅當雙向認證時設置該參數或PolyClientCertificateIds參數
        :type ClientCertificateId: str
        :param PolyClientCertificateIds: 新的用戶端多CA證書ID，僅當雙向認證時設置該參數或設置ClientCertificateId參數
        :type PolyClientCertificateIds: list of str
        """
        self.ListenerName = None
        self.Port = None
        self.CertificateId = None
        self.ForwardProtocol = None
        self.ProxyId = None
        self.AuthType = None
        self.ClientCertificateId = None
        self.PolyClientCertificateIds = None


    def _deserialize(self, params):
        self.ListenerName = params.get("ListenerName")
        self.Port = params.get("Port")
        self.CertificateId = params.get("CertificateId")
        self.ForwardProtocol = params.get("ForwardProtocol")
        self.ProxyId = params.get("ProxyId")
        self.AuthType = params.get("AuthType")
        self.ClientCertificateId = params.get("ClientCertificateId")
        self.PolyClientCertificateIds = params.get("PolyClientCertificateIds")


class CreateHTTPSListenerResponse(AbstractModel):
    """CreateHTTPSListener返回參數結構體

    """

    def __init__(self):
        """
        :param ListenerId: 創建的監聽器ID
        :type ListenerId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ListenerId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.RequestId = params.get("RequestId")


class CreateProxyGroupDomainRequest(AbstractModel):
    """CreateProxyGroupDomain請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 需要開啓域名的通道組ID。
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class CreateProxyGroupDomainResponse(AbstractModel):
    """CreateProxyGroupDomain返回參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 通道組ID。
        :type GroupId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")


class CreateProxyGroupRequest(AbstractModel):
    """CreateProxyGroup請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: 通道組所屬項目ID
        :type ProjectId: int
        :param GroupName: 通道組别名
        :type GroupName: str
        :param RealServerRegion: 源站地域，參考介面DescribeDestRegions 返回參數RegionDetail中的RegionId
        :type RealServerRegion: str
        :param TagSet: 標簽清單
        :type TagSet: list of TagPair
        """
        self.ProjectId = None
        self.GroupName = None
        self.RealServerRegion = None
        self.TagSet = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.GroupName = params.get("GroupName")
        self.RealServerRegion = params.get("RealServerRegion")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self.TagSet.append(obj)


class CreateProxyGroupResponse(AbstractModel):
    """CreateProxyGroup返回參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 通道組ID
        :type GroupId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")


class CreateProxyRequest(AbstractModel):
    """CreateProxy請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: 通道的項目ID。
        :type ProjectId: int
        :param ProxyName: 通道名稱。
        :type ProxyName: str
        :param AccessRegion: 接入地域。
        :type AccessRegion: str
        :param Bandwidth: 通道頻寬上限，單位：Mbps。
        :type Bandwidth: int
        :param Concurrent: 通道並發量上限，表示同時在線的連接數，單位：萬。
        :type Concurrent: int
        :param RealServerRegion: 源站地域。當GroupId存在時，源站地域爲通道組的源站地域,此時可不填該欄位。當GroupId不存在時，需要填寫該欄位
        :type RealServerRegion: str
        :param ClientToken: 用於保證請求幂等性的字串。該字串由客戶生成，需保證不同請求之間唯一，最大值不超過64個ASCII字元。若不指定該參數，則無法保證請求的幂等性。
更多詳細訊息請參閱：如何保證幂等性。
        :type ClientToken: str
        :param GroupId: 通道所在的通道組ID，當在通道組中創建通道時必帶，否則忽略該欄位。
        :type GroupId: str
        :param TagSet: 通道需要添加的標簽清單。
        :type TagSet: list of TagPair
        :param ClonedProxyId: 被複制的通道ID。只有處於運作中狀态的通道可以被複制。
當設置該參數時，表示複制該通道。
        :type ClonedProxyId: str
        :param BillingType: 計費方式 (0:按頻寬計費，1:按流量計費 預設按頻寬計費）
        :type BillingType: int
        """
        self.ProjectId = None
        self.ProxyName = None
        self.AccessRegion = None
        self.Bandwidth = None
        self.Concurrent = None
        self.RealServerRegion = None
        self.ClientToken = None
        self.GroupId = None
        self.TagSet = None
        self.ClonedProxyId = None
        self.BillingType = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProxyName = params.get("ProxyName")
        self.AccessRegion = params.get("AccessRegion")
        self.Bandwidth = params.get("Bandwidth")
        self.Concurrent = params.get("Concurrent")
        self.RealServerRegion = params.get("RealServerRegion")
        self.ClientToken = params.get("ClientToken")
        self.GroupId = params.get("GroupId")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.ClonedProxyId = params.get("ClonedProxyId")
        self.BillingType = params.get("BillingType")


class CreateProxyResponse(AbstractModel):
    """CreateProxy返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 通道的實例ID。
        :type InstanceId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class CreateRuleRequest(AbstractModel):
    """CreateRule請求參數結構體

    """

    def __init__(self):
        """
        :param ListenerId: 7層監聽器ID
        :type ListenerId: str
        :param Domain: 轉發規則的域名
        :type Domain: str
        :param Path: 轉發規則的路徑
        :type Path: str
        :param RealServerType: 轉發規則對應源站的類型，支援IP和DOMAIN類型。
        :type RealServerType: str
        :param Scheduler: 規則轉發源站調度策略，支援輪詢（rr），加權輪詢（wrr），最小連接數（lc）。
        :type Scheduler: str
        :param HealthCheck: 規則是否開啓健康檢查，1開啓，0關閉。
        :type HealthCheck: int
        :param CheckParams: 源站健康檢查相關參數
        :type CheckParams: :class:`taifucloudcloud.gaap.v20180529.models.RuleCheckParams`
        :param ForwardProtocol: 加速通道轉發到源站的協議類型：支援HTTP或HTTPS。
不傳遞該欄位時表示使用對應監聽器的ForwardProtocol。
        :type ForwardProtocol: str
        :param ForwardHost: 加速通道轉發到遠照的host，不設置該參數時，使用預設的host設置，即用戶端發起的http請求的host。
        :type ForwardHost: str
        """
        self.ListenerId = None
        self.Domain = None
        self.Path = None
        self.RealServerType = None
        self.Scheduler = None
        self.HealthCheck = None
        self.CheckParams = None
        self.ForwardProtocol = None
        self.ForwardHost = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.Path = params.get("Path")
        self.RealServerType = params.get("RealServerType")
        self.Scheduler = params.get("Scheduler")
        self.HealthCheck = params.get("HealthCheck")
        if params.get("CheckParams") is not None:
            self.CheckParams = RuleCheckParams()
            self.CheckParams._deserialize(params.get("CheckParams"))
        self.ForwardProtocol = params.get("ForwardProtocol")
        self.ForwardHost = params.get("ForwardHost")


class CreateRuleResponse(AbstractModel):
    """CreateRule返回參數結構體

    """

    def __init__(self):
        """
        :param RuleId: 創建轉發規則成功返回規則ID
        :type RuleId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class CreateSecurityPolicyRequest(AbstractModel):
    """CreateSecurityPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param ProxyId: 加速通道ID
        :type ProxyId: str
        :param DefaultAction: 預設策略：ACCEPT或DROP
        :type DefaultAction: str
        """
        self.ProxyId = None
        self.DefaultAction = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.DefaultAction = params.get("DefaultAction")


class CreateSecurityPolicyResponse(AbstractModel):
    """CreateSecurityPolicy返回參數結構體

    """

    def __init__(self):
        """
        :param PolicyId: 安全策略ID
        :type PolicyId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.RequestId = params.get("RequestId")


class CreateSecurityRulesRequest(AbstractModel):
    """CreateSecurityRules請求參數結構體

    """

    def __init__(self):
        """
        :param PolicyId: 安全策略ID
        :type PolicyId: str
        :param RuleList: 訪問規則清單
        :type RuleList: list of SecurityPolicyRuleIn
        """
        self.PolicyId = None
        self.RuleList = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        if params.get("RuleList") is not None:
            self.RuleList = []
            for item in params.get("RuleList"):
                obj = SecurityPolicyRuleIn()
                obj._deserialize(item)
                self.RuleList.append(obj)


class CreateSecurityRulesResponse(AbstractModel):
    """CreateSecurityRules返回參數結構體

    """

    def __init__(self):
        """
        :param RuleIdList: 規則ID清單
        :type RuleIdList: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RuleIdList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleIdList = params.get("RuleIdList")
        self.RequestId = params.get("RequestId")


class CreateTCPListenersRequest(AbstractModel):
    """CreateTCPListeners請求參數結構體

    """

    def __init__(self):
        """
        :param ListenerName: 監聽器名稱。
        :type ListenerName: str
        :param Ports: 監聽器端口清單。
        :type Ports: list of int non-negative
        :param Scheduler: 監聽器源站調度策略，支援輪詢（rr），加權輪詢（wrr），最小連接數（lc）。
        :type Scheduler: str
        :param HealthCheck: 源站是否開啓健康檢查：1開啓，0關閉，UDP監聽器不支援健康檢查
        :type HealthCheck: int
        :param RealServerType: 監聽器對應源站類型，支援IP或者DOMAIN類型。DOMAIN源站類型不支援wrr的源站調度策略。
        :type RealServerType: str
        :param ProxyId: 通道ID，ProxyId和GroupId必須設置一個，但不能同時設置。
        :type ProxyId: str
        :param GroupId: 通道組ID，ProxyId和GroupId必須設置一個，但不能同時設置。
        :type GroupId: str
        :param DelayLoop: 源站健康檢查時間間隔，單位：秒。時間間隔取值在[5，300]之間。
        :type DelayLoop: int
        :param ConnectTimeout: 源站健康檢查響應超時時間，單位：秒。超時時間取值在[2，60]之間。超時時間應小於健康檢查時間間隔DelayLoop。
        :type ConnectTimeout: int
        :param RealServerPorts: 源站端口清單，該參數僅支援v1版本監聽器和通道組監聽器。
        :type RealServerPorts: list of int non-negative
        """
        self.ListenerName = None
        self.Ports = None
        self.Scheduler = None
        self.HealthCheck = None
        self.RealServerType = None
        self.ProxyId = None
        self.GroupId = None
        self.DelayLoop = None
        self.ConnectTimeout = None
        self.RealServerPorts = None


    def _deserialize(self, params):
        self.ListenerName = params.get("ListenerName")
        self.Ports = params.get("Ports")
        self.Scheduler = params.get("Scheduler")
        self.HealthCheck = params.get("HealthCheck")
        self.RealServerType = params.get("RealServerType")
        self.ProxyId = params.get("ProxyId")
        self.GroupId = params.get("GroupId")
        self.DelayLoop = params.get("DelayLoop")
        self.ConnectTimeout = params.get("ConnectTimeout")
        self.RealServerPorts = params.get("RealServerPorts")


class CreateTCPListenersResponse(AbstractModel):
    """CreateTCPListeners返回參數結構體

    """

    def __init__(self):
        """
        :param ListenerIds: 返回監聽器ID
        :type ListenerIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ListenerIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ListenerIds = params.get("ListenerIds")
        self.RequestId = params.get("RequestId")


class CreateUDPListenersRequest(AbstractModel):
    """CreateUDPListeners請求參數結構體

    """

    def __init__(self):
        """
        :param ListenerName: 監聽器名稱
        :type ListenerName: str
        :param Ports: 監聽器端口清單
        :type Ports: list of int non-negative
        :param Scheduler: 監聽器源站調度策略，支援輪詢（rr），加權輪詢（wrr），最小連接數（lc）
        :type Scheduler: str
        :param RealServerType: 監聽器對應源站類型，支援IP或者DOMAIN類型
        :type RealServerType: str
        :param ProxyId: 通道ID，ProxyId和GroupId必須設置一個，但不能同時設置。
        :type ProxyId: str
        :param GroupId: 通道組ID，ProxyId和GroupId必須設置一個，但不能同時設置。
        :type GroupId: str
        :param RealServerPorts: 源站端口清單，該參數僅支援v1版本監聽器和通道組監聽器
        :type RealServerPorts: list of int non-negative
        """
        self.ListenerName = None
        self.Ports = None
        self.Scheduler = None
        self.RealServerType = None
        self.ProxyId = None
        self.GroupId = None
        self.RealServerPorts = None


    def _deserialize(self, params):
        self.ListenerName = params.get("ListenerName")
        self.Ports = params.get("Ports")
        self.Scheduler = params.get("Scheduler")
        self.RealServerType = params.get("RealServerType")
        self.ProxyId = params.get("ProxyId")
        self.GroupId = params.get("GroupId")
        self.RealServerPorts = params.get("RealServerPorts")


class CreateUDPListenersResponse(AbstractModel):
    """CreateUDPListeners返回參數結構體

    """

    def __init__(self):
        """
        :param ListenerIds: 返回監聽器ID
        :type ListenerIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ListenerIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ListenerIds = params.get("ListenerIds")
        self.RequestId = params.get("RequestId")


class DeleteCertificateRequest(AbstractModel):
    """DeleteCertificate請求參數結構體

    """

    def __init__(self):
        """
        :param CertificateId: 需要删除的證書ID。
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")


class DeleteCertificateResponse(AbstractModel):
    """DeleteCertificate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDomainErrorPageInfoRequest(AbstractModel):
    """DeleteDomainErrorPageInfo請求參數結構體

    """

    def __init__(self):
        """
        :param ErrorPageId: 定制錯誤響應頁的唯一ID，請參考CreateDomainErrorPageInfo的響應
        :type ErrorPageId: str
        """
        self.ErrorPageId = None


    def _deserialize(self, params):
        self.ErrorPageId = params.get("ErrorPageId")


class DeleteDomainErrorPageInfoResponse(AbstractModel):
    """DeleteDomainErrorPageInfo返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDomainRequest(AbstractModel):
    """DeleteDomain請求參數結構體

    """

    def __init__(self):
        """
        :param ListenerId: 監聽器ID
        :type ListenerId: str
        :param Domain: 需要删除的域名
        :type Domain: str
        :param Force: 是否強制删除已綁定源站的轉發規則，0非強制，1強制。
當采用非強制删除時，如果域名下已有規則綁定了源站，則無法删除。
        :type Force: int
        """
        self.ListenerId = None
        self.Domain = None
        self.Force = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.Force = params.get("Force")


class DeleteDomainResponse(AbstractModel):
    """DeleteDomain返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteListenersRequest(AbstractModel):
    """DeleteListeners請求參數結構體

    """

    def __init__(self):
        """
        :param ListenerIds: 待删除的監聽器ID清單
        :type ListenerIds: list of str
        :param Force: 已綁定源站的監聽器是否允許強制删除，1：允許， 0：不允許
        :type Force: int
        :param GroupId: 通道組ID，該參數和GroupId必須設置一個，但不能同時設置。
        :type GroupId: str
        :param ProxyId: 通道ID，該參數和GroupId必須設置一個，但不能同時設置。
        :type ProxyId: str
        """
        self.ListenerIds = None
        self.Force = None
        self.GroupId = None
        self.ProxyId = None


    def _deserialize(self, params):
        self.ListenerIds = params.get("ListenerIds")
        self.Force = params.get("Force")
        self.GroupId = params.get("GroupId")
        self.ProxyId = params.get("ProxyId")


class DeleteListenersResponse(AbstractModel):
    """DeleteListeners返回參數結構體

    """

    def __init__(self):
        """
        :param OperationFailedListenerSet: 删除操作失敗的監聽器ID清單
        :type OperationFailedListenerSet: list of str
        :param OperationSucceedListenerSet: 删除操作成功的監聽器ID清單
        :type OperationSucceedListenerSet: list of str
        :param InvalidStatusListenerSet: 無效的監聽器ID清單，如：監聽器不存在，監聽器對應實例不比對
        :type InvalidStatusListenerSet: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.OperationFailedListenerSet = None
        self.OperationSucceedListenerSet = None
        self.InvalidStatusListenerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OperationFailedListenerSet = params.get("OperationFailedListenerSet")
        self.OperationSucceedListenerSet = params.get("OperationSucceedListenerSet")
        self.InvalidStatusListenerSet = params.get("InvalidStatusListenerSet")
        self.RequestId = params.get("RequestId")


class DeleteProxyGroupRequest(AbstractModel):
    """DeleteProxyGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 需要删除的通道組ID。
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DeleteProxyGroupResponse(AbstractModel):
    """DeleteProxyGroup返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRuleRequest(AbstractModel):
    """DeleteRule請求參數結構體

    """

    def __init__(self):
        """
        :param ListenerId: 7層監聽器ID
        :type ListenerId: str
        :param RuleId: 轉發規則ID
        :type RuleId: str
        :param Force: 是否可以強制删除已綁定源站的轉發規則，0非強制，1強制
        :type Force: int
        """
        self.ListenerId = None
        self.RuleId = None
        self.Force = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.RuleId = params.get("RuleId")
        self.Force = params.get("Force")


class DeleteRuleResponse(AbstractModel):
    """DeleteRule返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSecurityPolicyRequest(AbstractModel):
    """DeleteSecurityPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param PolicyId: 策略ID
        :type PolicyId: str
        """
        self.PolicyId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")


class DeleteSecurityPolicyResponse(AbstractModel):
    """DeleteSecurityPolicy返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSecurityRulesRequest(AbstractModel):
    """DeleteSecurityRules請求參數結構體

    """

    def __init__(self):
        """
        :param PolicyId: 安全策略ID
        :type PolicyId: str
        :param RuleIdList: 訪問規則ID清單
        :type RuleIdList: list of str
        """
        self.PolicyId = None
        self.RuleIdList = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.RuleIdList = params.get("RuleIdList")


class DeleteSecurityRulesResponse(AbstractModel):
    """DeleteSecurityRules返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccessRegionsByDestRegionRequest(AbstractModel):
    """DescribeAccessRegionsByDestRegion請求參數結構體

    """

    def __init__(self):
        """
        :param DestRegion: 源站區域：介面DescribeDestRegions返回DestRegionSet中的RegionId欄位值
        :type DestRegion: str
        """
        self.DestRegion = None


    def _deserialize(self, params):
        self.DestRegion = params.get("DestRegion")


class DescribeAccessRegionsByDestRegionResponse(AbstractModel):
    """DescribeAccessRegionsByDestRegion返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 可用加速區域數量
        :type TotalCount: int
        :param AccessRegionSet: 可用加速區域訊息清單
        :type AccessRegionSet: list of AccessRegionDetial
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AccessRegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AccessRegionSet") is not None:
            self.AccessRegionSet = []
            for item in params.get("AccessRegionSet"):
                obj = AccessRegionDetial()
                obj._deserialize(item)
                self.AccessRegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAccessRegionsRequest(AbstractModel):
    """DescribeAccessRegions請求參數結構體

    """


class DescribeAccessRegionsResponse(AbstractModel):
    """DescribeAccessRegions返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 加速區域總數
        :type TotalCount: int
        :param AccessRegionSet: 加速區域詳情清單
        :type AccessRegionSet: list of RegionDetail
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AccessRegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AccessRegionSet") is not None:
            self.AccessRegionSet = []
            for item in params.get("AccessRegionSet"):
                obj = RegionDetail()
                obj._deserialize(item)
                self.AccessRegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCertificateDetailRequest(AbstractModel):
    """DescribeCertificateDetail請求參數結構體

    """

    def __init__(self):
        """
        :param CertificateId: 證書ID。
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")


class DescribeCertificateDetailResponse(AbstractModel):
    """DescribeCertificateDetail返回參數結構體

    """

    def __init__(self):
        """
        :param CertificateDetail: 證書詳情。
        :type CertificateDetail: :class:`taifucloudcloud.gaap.v20180529.models.CertificateDetail`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CertificateDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CertificateDetail") is not None:
            self.CertificateDetail = CertificateDetail()
            self.CertificateDetail._deserialize(params.get("CertificateDetail"))
        self.RequestId = params.get("RequestId")


class DescribeCertificatesRequest(AbstractModel):
    """DescribeCertificates請求參數結構體

    """

    def __init__(self):
        """
        :param CertificateType: 證書類型。其中：
0，表示基礎認證配置；
1，表示用戶端CA證書；
2，表示服務器SSL證書；
3，表示源站CA證書；
4，表示通道SSL證書。
-1，所有類型。
預設爲-1。
        :type CertificateType: int
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Limit: 限制數量，預設爲20。
        :type Limit: int
        """
        self.CertificateType = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.CertificateType = params.get("CertificateType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeCertificatesResponse(AbstractModel):
    """DescribeCertificates返回參數結構體

    """

    def __init__(self):
        """
        :param CertificateSet: 服務器證書清單，包括證書ID 和證書名稱。
        :type CertificateSet: list of Certificate
        :param TotalCount: 滿足查詢條件的服務器證書總數量。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CertificateSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CertificateSet") is not None:
            self.CertificateSet = []
            for item in params.get("CertificateSet"):
                obj = Certificate()
                obj._deserialize(item)
                self.CertificateSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCountryAreaMappingRequest(AbstractModel):
    """DescribeCountryAreaMapping請求參數結構體

    """


class DescribeCountryAreaMappingResponse(AbstractModel):
    """DescribeCountryAreaMapping返回參數結構體

    """

    def __init__(self):
        """
        :param CountryAreaMappingList: 國家地區編碼映射表。
        :type CountryAreaMappingList: list of CountryAreaMap
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CountryAreaMappingList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CountryAreaMappingList") is not None:
            self.CountryAreaMappingList = []
            for item in params.get("CountryAreaMappingList"):
                obj = CountryAreaMap()
                obj._deserialize(item)
                self.CountryAreaMappingList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDestRegionsRequest(AbstractModel):
    """DescribeDestRegions請求參數結構體

    """


class DescribeDestRegionsResponse(AbstractModel):
    """DescribeDestRegions返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 源站區域總數
        :type TotalCount: int
        :param DestRegionSet: 源站區域詳情清單
        :type DestRegionSet: list of RegionDetail
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DestRegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DestRegionSet") is not None:
            self.DestRegionSet = []
            for item in params.get("DestRegionSet"):
                obj = RegionDetail()
                obj._deserialize(item)
                self.DestRegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDomainErrorPageInfoByIdsRequest(AbstractModel):
    """DescribeDomainErrorPageInfoByIds請求參數結構體

    """

    def __init__(self):
        """
        :param ErrorPageIds: 定制錯誤ID清單,最多支援10個
        :type ErrorPageIds: list of str
        """
        self.ErrorPageIds = None


    def _deserialize(self, params):
        self.ErrorPageIds = params.get("ErrorPageIds")


class DescribeDomainErrorPageInfoByIdsResponse(AbstractModel):
    """DescribeDomainErrorPageInfoByIds返回參數結構體

    """

    def __init__(self):
        """
        :param ErrorPageSet: 定制錯誤響應配置集
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrorPageSet: list of DomainErrorPageInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ErrorPageSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ErrorPageSet") is not None:
            self.ErrorPageSet = []
            for item in params.get("ErrorPageSet"):
                obj = DomainErrorPageInfo()
                obj._deserialize(item)
                self.ErrorPageSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDomainErrorPageInfoRequest(AbstractModel):
    """DescribeDomainErrorPageInfo請求參數結構體

    """

    def __init__(self):
        """
        :param ListenerId: 監聽器ID
        :type ListenerId: str
        :param Domain: 域名
        :type Domain: str
        """
        self.ListenerId = None
        self.Domain = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")


class DescribeDomainErrorPageInfoResponse(AbstractModel):
    """DescribeDomainErrorPageInfo返回參數結構體

    """

    def __init__(self):
        """
        :param ErrorPageSet: 定制錯誤響應配置集
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrorPageSet: list of DomainErrorPageInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ErrorPageSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ErrorPageSet") is not None:
            self.ErrorPageSet = []
            for item in params.get("ErrorPageSet"):
                obj = DomainErrorPageInfo()
                obj._deserialize(item)
                self.ErrorPageSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeGroupAndStatisticsProxyRequest(AbstractModel):
    """DescribeGroupAndStatisticsProxy請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: 項目ID
        :type ProjectId: int
        """
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")


class DescribeGroupAndStatisticsProxyResponse(AbstractModel):
    """DescribeGroupAndStatisticsProxy返回參數結構體

    """

    def __init__(self):
        """
        :param GroupSet: 可以統計的通道組訊息
        :type GroupSet: list of GroupStatisticsInfo
        :param TotalCount: 通道組數量
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.GroupSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GroupSet") is not None:
            self.GroupSet = []
            for item in params.get("GroupSet"):
                obj = GroupStatisticsInfo()
                obj._deserialize(item)
                self.GroupSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeGroupDomainConfigRequest(AbstractModel):
    """DescribeGroupDomainConfig請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 通道組ID。
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DescribeGroupDomainConfigResponse(AbstractModel):
    """DescribeGroupDomainConfig返回參數結構體

    """

    def __init__(self):
        """
        :param AccessRegionList: 域名解析就近接入配置清單。
        :type AccessRegionList: list of DomainAccessRegionDict
        :param DefaultDnsIp: 預設訪問Ip。
        :type DefaultDnsIp: str
        :param GroupId: 通道組ID。
        :type GroupId: str
        :param AccessRegionCount: 接入地域的配置的總數。
        :type AccessRegionCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AccessRegionList = None
        self.DefaultDnsIp = None
        self.GroupId = None
        self.AccessRegionCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccessRegionList") is not None:
            self.AccessRegionList = []
            for item in params.get("AccessRegionList"):
                obj = DomainAccessRegionDict()
                obj._deserialize(item)
                self.AccessRegionList.append(obj)
        self.DefaultDnsIp = params.get("DefaultDnsIp")
        self.GroupId = params.get("GroupId")
        self.AccessRegionCount = params.get("AccessRegionCount")
        self.RequestId = params.get("RequestId")


class DescribeHTTPListenersRequest(AbstractModel):
    """DescribeHTTPListeners請求參數結構體

    """

    def __init__(self):
        """
        :param ProxyId: 通道ID
        :type ProxyId: str
        :param ListenerId: 過濾條件，按照監聽器ID進行精确查詢
        :type ListenerId: str
        :param ListenerName: 過濾條件，按照監聽器名稱進行精确查詢
        :type ListenerName: str
        :param Port: 過濾條件，按照監聽器端口進行精确查詢
        :type Port: int
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 限制數量，預設爲20個
        :type Limit: int
        :param SearchValue: 過濾條件，支援按照端口或監聽器名稱進行模糊查詢，該參數不能與ListenerName和Port同時使用
        :type SearchValue: str
        """
        self.ProxyId = None
        self.ListenerId = None
        self.ListenerName = None
        self.Port = None
        self.Offset = None
        self.Limit = None
        self.SearchValue = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Port = params.get("Port")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchValue = params.get("SearchValue")


class DescribeHTTPListenersResponse(AbstractModel):
    """DescribeHTTPListeners返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 監聽器數量
        :type TotalCount: int
        :param ListenerSet: HTTP監聽器清單
        :type ListenerSet: list of HTTPListener
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ListenerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ListenerSet") is not None:
            self.ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = HTTPListener()
                obj._deserialize(item)
                self.ListenerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHTTPSListenersRequest(AbstractModel):
    """DescribeHTTPSListeners請求參數結構體

    """

    def __init__(self):
        """
        :param ProxyId: 過濾條件，通道ID
        :type ProxyId: str
        :param ListenerId: 過濾條件，根據監聽器ID進行精确查詢。
        :type ListenerId: str
        :param ListenerName: 過濾條件，根據監聽器名稱進行精确查詢。
        :type ListenerName: str
        :param Port: 過濾條件，根據監聽器端口進行精确查詢。
        :type Port: int
        :param Offset: 偏移量， 預設爲0
        :type Offset: int
        :param Limit: 限制數量，預設爲20
        :type Limit: int
        :param SearchValue: 過濾條件，支援按照端口或監聽器名稱進行模糊查詢
        :type SearchValue: str
        """
        self.ProxyId = None
        self.ListenerId = None
        self.ListenerName = None
        self.Port = None
        self.Offset = None
        self.Limit = None
        self.SearchValue = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Port = params.get("Port")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchValue = params.get("SearchValue")


class DescribeHTTPSListenersResponse(AbstractModel):
    """DescribeHTTPSListeners返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 監聽器數量
        :type TotalCount: int
        :param ListenerSet: HTTPS監聽器清單
        :type ListenerSet: list of HTTPSListener
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ListenerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ListenerSet") is not None:
            self.ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = HTTPSListener()
                obj._deserialize(item)
                self.ListenerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeListenerRealServersRequest(AbstractModel):
    """DescribeListenerRealServers請求參數結構體

    """

    def __init__(self):
        """
        :param ListenerId: 監聽器ID
        :type ListenerId: str
        """
        self.ListenerId = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")


class DescribeListenerRealServersResponse(AbstractModel):
    """DescribeListenerRealServers返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 可綁定源站的個數
        :type TotalCount: int
        :param RealServerSet: 源站訊息清單
        :type RealServerSet: list of RealServer
        :param BindRealServerTotalCount: 已綁定源站的個數
        :type BindRealServerTotalCount: int
        :param BindRealServerSet: 已綁定源站訊息清單
        :type BindRealServerSet: list of BindRealServer
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RealServerSet = None
        self.BindRealServerTotalCount = None
        self.BindRealServerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RealServerSet") is not None:
            self.RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = RealServer()
                obj._deserialize(item)
                self.RealServerSet.append(obj)
        self.BindRealServerTotalCount = params.get("BindRealServerTotalCount")
        if params.get("BindRealServerSet") is not None:
            self.BindRealServerSet = []
            for item in params.get("BindRealServerSet"):
                obj = BindRealServer()
                obj._deserialize(item)
                self.BindRealServerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeListenerStatisticsRequest(AbstractModel):
    """DescribeListenerStatistics請求參數結構體

    """

    def __init__(self):
        """
        :param ListenerId: 監聽器ID
        :type ListenerId: str
        :param StartTime: 起始時間
        :type StartTime: str
        :param EndTime: 結束時間
        :type EndTime: str
        :param MetricNames: 統計指標名稱清單，支援: 入頻寬:InBandwidth, 出頻寬:OutBandwidth, 並發:Concurrent, 入包量:InPackets, 出包量:OutPackets。
        :type MetricNames: list of str
        :param Granularity: 監控粒度，目前支援300，3600，86400，單位：秒。
查詢時間範圍不超過1天，支援最小粒度300秒；
查詢間範圍不超過7天，支援最小粒度3600秒；
查詢間範圍超過7天，支援最小粒度86400秒。
        :type Granularity: int
        """
        self.ListenerId = None
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.Granularity = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.Granularity = params.get("Granularity")


class DescribeListenerStatisticsResponse(AbstractModel):
    """DescribeListenerStatistics返回參數結構體

    """

    def __init__(self):
        """
        :param StatisticsData: 通道組統計數據
        :type StatisticsData: list of MetricStatisticsInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.StatisticsData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("StatisticsData") is not None:
            self.StatisticsData = []
            for item in params.get("StatisticsData"):
                obj = MetricStatisticsInfo()
                obj._deserialize(item)
                self.StatisticsData.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProxiesRequest(AbstractModel):
    """DescribeProxies請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: （舊參數，請切換到ProxyIds）按照一個或者多個實例ID查詢。每次請求的實例的上限爲100。參數不支援同時指定InstanceIds和Filters。
        :type InstanceIds: list of str
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。
        :type Limit: int
        :param Filters: 過濾條件。   
每次請求的Filters的上限爲10，Filter.Values的上限爲5。參數不支援同時指定InstanceIds和Filters。 
ProjectId - String - 是否必填：否 -（過濾條件）按照項目ID過濾。    
AccessRegion - String - 是否必填：否 - （過濾條件）按照接入地域過濾。    
RealServerRegion - String - 是否必填：否 - （過濾條件）按照源站地域過濾。
GroupId - String - 是否必填：否 - （過濾條件）按照通道組ID過濾。
        :type Filters: list of Filter
        :param ProxyIds: （新參數，替代InstanceIds）按照一個或者多個實例ID查詢。每次請求的實例的上限爲100。參數不支援同時指定InstanceIds和Filters。
        :type ProxyIds: list of str
        :param TagSet: 標簽清單，當存在該欄位時，拉取對應標簽下的資源清單。
最多支援5個標簽，當存在兩個或兩個以上的標簽時，滿足其中任意一個標簽時，通道會被拉取出來。
        :type TagSet: list of TagPair
        :param Independent: 當該欄位爲1時，僅拉取非通道組的通道，
當該欄位爲0時，僅拉取通道組的通道，
不存在該欄位時，拉取所有通道，包括獨立通道和通道組通道。
        :type Independent: int
        """
        self.InstanceIds = None
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.ProxyIds = None
        self.TagSet = None
        self.Independent = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.ProxyIds = params.get("ProxyIds")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.Independent = params.get("Independent")


class DescribeProxiesResponse(AbstractModel):
    """DescribeProxies返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 通道個數。
        :type TotalCount: int
        :param InstanceSet: （舊參數，請切換到ProxySet）通道實例訊息清單。
        :type InstanceSet: list of ProxyInfo
        :param ProxySet: （新參數）通道實例訊息清單。
        :type ProxySet: list of ProxyInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceSet = None
        self.ProxySet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = ProxyInfo()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        if params.get("ProxySet") is not None:
            self.ProxySet = []
            for item in params.get("ProxySet"):
                obj = ProxyInfo()
                obj._deserialize(item)
                self.ProxySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProxiesStatusRequest(AbstractModel):
    """DescribeProxiesStatus請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: （舊參數，請切換到ProxyIds）通道ID清單。
        :type InstanceIds: list of str
        :param ProxyIds: （新參數）通道ID清單。
        :type ProxyIds: list of str
        """
        self.InstanceIds = None
        self.ProxyIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.ProxyIds = params.get("ProxyIds")


class DescribeProxiesStatusResponse(AbstractModel):
    """DescribeProxiesStatus返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceStatusSet: 通道狀态清單。
        :type InstanceStatusSet: list of ProxyStatus
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceStatusSet") is not None:
            self.InstanceStatusSet = []
            for item in params.get("InstanceStatusSet"):
                obj = ProxyStatus()
                obj._deserialize(item)
                self.InstanceStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProxyAndStatisticsListenersRequest(AbstractModel):
    """DescribeProxyAndStatisticsListeners請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: 項目ID
        :type ProjectId: int
        """
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")


class DescribeProxyAndStatisticsListenersResponse(AbstractModel):
    """DescribeProxyAndStatisticsListeners返回參數結構體

    """

    def __init__(self):
        """
        :param ProxySet: 可以統計的通道訊息
        :type ProxySet: list of ProxySimpleInfo
        :param TotalCount: 通道數量
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ProxySet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProxySet") is not None:
            self.ProxySet = []
            for item in params.get("ProxySet"):
                obj = ProxySimpleInfo()
                obj._deserialize(item)
                self.ProxySet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeProxyDetailRequest(AbstractModel):
    """DescribeProxyDetail請求參數結構體

    """

    def __init__(self):
        """
        :param ProxyId: 需查詢的通道ID。
        :type ProxyId: str
        """
        self.ProxyId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")


class DescribeProxyDetailResponse(AbstractModel):
    """DescribeProxyDetail返回參數結構體

    """

    def __init__(self):
        """
        :param ProxyDetail: 通道詳情訊息。
        :type ProxyDetail: :class:`taifucloudcloud.gaap.v20180529.models.ProxyInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ProxyDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProxyDetail") is not None:
            self.ProxyDetail = ProxyInfo()
            self.ProxyDetail._deserialize(params.get("ProxyDetail"))
        self.RequestId = params.get("RequestId")


class DescribeProxyGroupDetailsRequest(AbstractModel):
    """DescribeProxyGroupDetails請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 通道組ID。
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DescribeProxyGroupDetailsResponse(AbstractModel):
    """DescribeProxyGroupDetails返回參數結構體

    """

    def __init__(self):
        """
        :param ProxyGroupDetail: 通道組詳細訊息。
        :type ProxyGroupDetail: :class:`taifucloudcloud.gaap.v20180529.models.ProxyGroupDetail`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ProxyGroupDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProxyGroupDetail") is not None:
            self.ProxyGroupDetail = ProxyGroupDetail()
            self.ProxyGroupDetail._deserialize(params.get("ProxyGroupDetail"))
        self.RequestId = params.get("RequestId")


class DescribeProxyGroupListRequest(AbstractModel):
    """DescribeProxyGroupList請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移量，預設值爲0。
        :type Offset: int
        :param Limit: 返回數量，預設值爲20，最大值爲100。
        :type Limit: int
        :param ProjectId: 項目ID。取值範圍：
-1，該用戶下所有項目
0，預設項目
其他值，指定的項目
        :type ProjectId: int
        :param TagSet: 標簽清單，當存在該欄位時，拉取對應標簽下的資源清單。
最多支援5個標簽，當存在兩個或兩個以上的標簽時，滿足其中任意一個標簽時，該通道組會被拉取出來。
        :type TagSet: list of TagPair
        :param Filters: 過濾條件。   
每次請求的Filter.Values的上限爲5。
RealServerRegion - String - 是否必填：否 -（過濾條件）按照源站地域過濾，可參考DescribeDestRegions介面返回結果中的RegionId。
        :type Filters: list of Filter
        """
        self.Offset = None
        self.Limit = None
        self.ProjectId = None
        self.TagSet = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ProjectId = params.get("ProjectId")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self.TagSet.append(obj)
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeProxyGroupListResponse(AbstractModel):
    """DescribeProxyGroupList返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 通道組總數。
        :type TotalCount: int
        :param ProxyGroupList: 通道組清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProxyGroupList: list of ProxyGroupInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ProxyGroupList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ProxyGroupList") is not None:
            self.ProxyGroupList = []
            for item in params.get("ProxyGroupList"):
                obj = ProxyGroupInfo()
                obj._deserialize(item)
                self.ProxyGroupList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProxyGroupStatisticsRequest(AbstractModel):
    """DescribeProxyGroupStatistics請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 通道組ID
        :type GroupId: str
        :param StartTime: 起始時間
        :type StartTime: str
        :param EndTime: 結束時間
        :type EndTime: str
        :param MetricNames: 統計指標名稱清單，支援: 入頻寬:InBandwidth, 出頻寬:OutBandwidth, 並發:Concurrent, 入包量:InPackets, 出包量:OutPackets
        :type MetricNames: list of str
        :param Granularity: 監控粒度，目前支援60，300，3600，86400，單位：秒。
當時間範圍不超過1天，支援最小粒度60秒；
當時間範圍不超過7天，支援最小粒度3600秒；
當時間範圍不超過30天，支援最小粒度86400秒。
        :type Granularity: int
        """
        self.GroupId = None
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.Granularity = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.Granularity = params.get("Granularity")


class DescribeProxyGroupStatisticsResponse(AbstractModel):
    """DescribeProxyGroupStatistics返回參數結構體

    """

    def __init__(self):
        """
        :param StatisticsData: 通道組統計數據
        :type StatisticsData: list of MetricStatisticsInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.StatisticsData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("StatisticsData") is not None:
            self.StatisticsData = []
            for item in params.get("StatisticsData"):
                obj = MetricStatisticsInfo()
                obj._deserialize(item)
                self.StatisticsData.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProxyStatisticsRequest(AbstractModel):
    """DescribeProxyStatistics請求參數結構體

    """

    def __init__(self):
        """
        :param ProxyId: 通道ID
        :type ProxyId: str
        :param StartTime: 起始時間(2019-03-25 12:00:00)
        :type StartTime: str
        :param EndTime: 結束時間(2019-03-25 12:00:00)
        :type EndTime: str
        :param MetricNames: 統計指標名稱清單，支援: 入頻寬:InBandwidth, 出頻寬:OutBandwidth, 並發:Concurrent, 入包量:InPackets, 出包量:OutPackets, 丢包率:PacketLoss, 延遲:Latency
        :type MetricNames: list of str
        :param Granularity: 監控粒度，目前支援60，300，3600，86400，單位：秒。
當時間範圍不超過3天，支援最小粒度60秒；
當時間範圍不超過7天，支援最小粒度300秒；
當時間範圍不超過30天，支援最小粒度3600秒。
        :type Granularity: int
        """
        self.ProxyId = None
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.Granularity = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.Granularity = params.get("Granularity")


class DescribeProxyStatisticsResponse(AbstractModel):
    """DescribeProxyStatistics返回參數結構體

    """

    def __init__(self):
        """
        :param StatisticsData: 通道統計數據
        :type StatisticsData: list of MetricStatisticsInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.StatisticsData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("StatisticsData") is not None:
            self.StatisticsData = []
            for item in params.get("StatisticsData"):
                obj = MetricStatisticsInfo()
                obj._deserialize(item)
                self.StatisticsData.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRealServerStatisticsRequest(AbstractModel):
    """DescribeRealServerStatistics請求參數結構體

    """

    def __init__(self):
        """
        :param RealServerId: 源站ID
        :type RealServerId: str
        :param ListenerId: 監聽器ID
        :type ListenerId: str
        :param WithinTime: 統計時長，單位：小時。僅支援最近1,3,6,12,24小時的統計查詢
        :type WithinTime: int
        :param RuleId: 規則ID
        :type RuleId: str
        """
        self.RealServerId = None
        self.ListenerId = None
        self.WithinTime = None
        self.RuleId = None


    def _deserialize(self, params):
        self.RealServerId = params.get("RealServerId")
        self.ListenerId = params.get("ListenerId")
        self.WithinTime = params.get("WithinTime")
        self.RuleId = params.get("RuleId")


class DescribeRealServerStatisticsResponse(AbstractModel):
    """DescribeRealServerStatistics返回參數結構體

    """

    def __init__(self):
        """
        :param StatisticsData: 源站狀态統計數據
        :type StatisticsData: list of StatisticsDataInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.StatisticsData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("StatisticsData") is not None:
            self.StatisticsData = []
            for item in params.get("StatisticsData"):
                obj = StatisticsDataInfo()
                obj._deserialize(item)
                self.StatisticsData.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRealServersRequest(AbstractModel):
    """DescribeRealServers請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: 查詢源站的所屬項目ID，-1表示所有項目
        :type ProjectId: int
        :param SearchValue: 需要查詢的源站IP或域名，支援模糊比對
        :type SearchValue: str
        :param Offset: 偏移量，預設值是0
        :type Offset: int
        :param Limit: 返回數量，預設爲20個，最大值爲50個
        :type Limit: int
        :param TagSet: 標簽清單，當存在該欄位時，拉取對應標簽下的資源清單。
最多支援5個標簽，當存在兩個或兩個以上的標簽時，滿足其中任意一個標簽時，源站會被拉取出來。
        :type TagSet: list of TagPair
        :param Filters: 過濾條件。filter的name取值(RealServerName,RealServerIP)
        :type Filters: list of Filter
        """
        self.ProjectId = None
        self.SearchValue = None
        self.Offset = None
        self.Limit = None
        self.TagSet = None
        self.Filters = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.SearchValue = params.get("SearchValue")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self.TagSet.append(obj)
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeRealServersResponse(AbstractModel):
    """DescribeRealServers返回參數結構體

    """

    def __init__(self):
        """
        :param RealServerSet: 源站訊息清單
        :type RealServerSet: list of BindRealServerInfo
        :param TotalCount: 查詢得到的源站數量
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RealServerSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RealServerSet") is not None:
            self.RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = BindRealServerInfo()
                obj._deserialize(item)
                self.RealServerSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRealServersStatusRequest(AbstractModel):
    """DescribeRealServersStatus請求參數結構體

    """

    def __init__(self):
        """
        :param RealServerIds: 源站ID清單
        :type RealServerIds: list of str
        """
        self.RealServerIds = None


    def _deserialize(self, params):
        self.RealServerIds = params.get("RealServerIds")


class DescribeRealServersStatusResponse(AbstractModel):
    """DescribeRealServersStatus返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 返回源站查詢結果的個數
        :type TotalCount: int
        :param RealServerStatusSet: 源站被綁定狀态清單
        :type RealServerStatusSet: list of RealServerStatus
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RealServerStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RealServerStatusSet") is not None:
            self.RealServerStatusSet = []
            for item in params.get("RealServerStatusSet"):
                obj = RealServerStatus()
                obj._deserialize(item)
                self.RealServerStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRegionAndPriceRequest(AbstractModel):
    """DescribeRegionAndPrice請求參數結構體

    """


class DescribeRegionAndPriceResponse(AbstractModel):
    """DescribeRegionAndPrice返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 源站區域總數
        :type TotalCount: int
        :param DestRegionSet: 源站區域詳情清單
        :type DestRegionSet: list of RegionDetail
        :param BandwidthUnitPrice: 通道頻寬費用梯度價格
        :type BandwidthUnitPrice: list of BandwidthPriceGradient
        :param Currency: 頻寬價格貨币類型：
CNY 人民币
USD 美元
        :type Currency: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DestRegionSet = None
        self.BandwidthUnitPrice = None
        self.Currency = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DestRegionSet") is not None:
            self.DestRegionSet = []
            for item in params.get("DestRegionSet"):
                obj = RegionDetail()
                obj._deserialize(item)
                self.DestRegionSet.append(obj)
        if params.get("BandwidthUnitPrice") is not None:
            self.BandwidthUnitPrice = []
            for item in params.get("BandwidthUnitPrice"):
                obj = BandwidthPriceGradient()
                obj._deserialize(item)
                self.BandwidthUnitPrice.append(obj)
        self.Currency = params.get("Currency")
        self.RequestId = params.get("RequestId")


class DescribeResourcesByTagRequest(AbstractModel):
    """DescribeResourcesByTag請求參數結構體

    """

    def __init__(self):
        """
        :param TagKey: 標簽鍵。
        :type TagKey: str
        :param TagValue: 標簽值。
        :type TagValue: str
        :param ResourceType: 資源類型，其中：
Proxy表示通道；
ProxyGroup表示通道組；
RealServer表示源站。
不指定該欄位則查詢該標簽下所有資源。
        :type ResourceType: str
        """
        self.TagKey = None
        self.TagValue = None
        self.ResourceType = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        self.ResourceType = params.get("ResourceType")


class DescribeResourcesByTagResponse(AbstractModel):
    """DescribeResourcesByTag返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 資源總數
        :type TotalCount: int
        :param ResourceSet: 標簽對應的資源清單
        :type ResourceSet: list of TagResourceInfo
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
                obj = TagResourceInfo()
                obj._deserialize(item)
                self.ResourceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRuleRealServersRequest(AbstractModel):
    """DescribeRuleRealServers請求參數結構體

    """

    def __init__(self):
        """
        :param RuleId: 轉發規則ID
        :type RuleId: str
        """
        self.RuleId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")


class DescribeRuleRealServersResponse(AbstractModel):
    """DescribeRuleRealServers返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 可綁定的源站個數
        :type TotalCount: int
        :param RealServerSet: 可綁定的源站訊息清單
        :type RealServerSet: list of RealServer
        :param BindRealServerTotalCount: 已綁定的源站個數
        :type BindRealServerTotalCount: int
        :param BindRealServerSet: 已綁定的源站訊息清單
        :type BindRealServerSet: list of BindRealServer
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RealServerSet = None
        self.BindRealServerTotalCount = None
        self.BindRealServerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RealServerSet") is not None:
            self.RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = RealServer()
                obj._deserialize(item)
                self.RealServerSet.append(obj)
        self.BindRealServerTotalCount = params.get("BindRealServerTotalCount")
        if params.get("BindRealServerSet") is not None:
            self.BindRealServerSet = []
            for item in params.get("BindRealServerSet"):
                obj = BindRealServer()
                obj._deserialize(item)
                self.BindRealServerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRulesByRuleIdsRequest(AbstractModel):
    """DescribeRulesByRuleIds請求參數結構體

    """

    def __init__(self):
        """
        :param RuleIds: 規則ID清單。最多支援10個規則。
        :type RuleIds: list of str
        """
        self.RuleIds = None


    def _deserialize(self, params):
        self.RuleIds = params.get("RuleIds")


class DescribeRulesByRuleIdsResponse(AbstractModel):
    """DescribeRulesByRuleIds返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 返回的規則總個數。
        :type TotalCount: int
        :param RuleSet: 返回的規則清單。
        :type RuleSet: list of RuleInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RuleSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RuleSet") is not None:
            self.RuleSet = []
            for item in params.get("RuleSet"):
                obj = RuleInfo()
                obj._deserialize(item)
                self.RuleSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRulesRequest(AbstractModel):
    """DescribeRules請求參數結構體

    """

    def __init__(self):
        """
        :param ListenerId: 7層監聽器Id。
        :type ListenerId: str
        """
        self.ListenerId = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")


class DescribeRulesResponse(AbstractModel):
    """DescribeRules返回參數結構體

    """

    def __init__(self):
        """
        :param DomainRuleSet: 按照域名分類的規則訊息清單
        :type DomainRuleSet: list of DomainRuleSet
        :param TotalCount: 該監聽器下的域名總數
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DomainRuleSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainRuleSet") is not None:
            self.DomainRuleSet = []
            for item in params.get("DomainRuleSet"):
                obj = DomainRuleSet()
                obj._deserialize(item)
                self.DomainRuleSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSecurityPolicyDetailRequest(AbstractModel):
    """DescribeSecurityPolicyDetail請求參數結構體

    """

    def __init__(self):
        """
        :param PolicyId: 安全策略ID
        :type PolicyId: str
        """
        self.PolicyId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")


class DescribeSecurityPolicyDetailResponse(AbstractModel):
    """DescribeSecurityPolicyDetail返回參數結構體

    """

    def __init__(self):
        """
        :param ProxyId: 通道ID
        :type ProxyId: str
        :param Status: 安全策略狀态：
BOUND，已開啓安全策略
UNBIND，已關閉安全策略
BINDING，安全策略開啓中
UNBINDING，安全策略關閉中。
        :type Status: str
        :param DefaultAction: 預設策略：ACCEPT或DROP。
        :type DefaultAction: str
        :param PolicyId: 策略ID
        :type PolicyId: str
        :param RuleList: 規則清單
        :type RuleList: list of SecurityPolicyRuleOut
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ProxyId = None
        self.Status = None
        self.DefaultAction = None
        self.PolicyId = None
        self.RuleList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.Status = params.get("Status")
        self.DefaultAction = params.get("DefaultAction")
        self.PolicyId = params.get("PolicyId")
        if params.get("RuleList") is not None:
            self.RuleList = []
            for item in params.get("RuleList"):
                obj = SecurityPolicyRuleOut()
                obj._deserialize(item)
                self.RuleList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecurityRulesRequest(AbstractModel):
    """DescribeSecurityRules請求參數結構體

    """

    def __init__(self):
        """
        :param SecurityRuleIds: 安全規則ID清單。總數不能超過20個。
        :type SecurityRuleIds: list of str
        """
        self.SecurityRuleIds = None


    def _deserialize(self, params):
        self.SecurityRuleIds = params.get("SecurityRuleIds")


class DescribeSecurityRulesResponse(AbstractModel):
    """DescribeSecurityRules返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 返回的安全規則詳情總數。
        :type TotalCount: int
        :param SecurityRuleSet: 返回的安全規則詳情清單。
        :type SecurityRuleSet: list of SecurityPolicyRuleOut
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SecurityRuleSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SecurityRuleSet") is not None:
            self.SecurityRuleSet = []
            for item in params.get("SecurityRuleSet"):
                obj = SecurityPolicyRuleOut()
                obj._deserialize(item)
                self.SecurityRuleSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTCPListenersRequest(AbstractModel):
    """DescribeTCPListeners請求參數結構體

    """

    def __init__(self):
        """
        :param ProxyId: 過濾條件，根據通道ID進行拉取，ProxyId/GroupId/ListenerId必須設置一個，但ProxyId和GroupId不能同時設置。
        :type ProxyId: str
        :param ListenerId: 過濾條件，根據監聽器ID精确查詢。
當設置了ProxyId時，會檢查該監聽器是否歸屬於該通道。
當設置了GroupId時，會檢查該監聽器是否歸屬於該通道組。
        :type ListenerId: str
        :param ListenerName: 過濾條件，根據監聽器名稱精确查詢
        :type ListenerName: str
        :param Port: 過濾條件，根據監聽器端口精确查詢
        :type Port: int
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 限制數量，預設爲20
        :type Limit: int
        :param GroupId: 過濾條件，根據通道組ID進行拉取，ProxyId/GroupId/ListenerId必須設置一個，但ProxyId和GroupId不能同時設置。
        :type GroupId: str
        :param SearchValue: 過濾條件，支援按照端口或監聽器名稱進行模糊查詢，該參數不能與ListenerName和Port同時使用
        :type SearchValue: str
        """
        self.ProxyId = None
        self.ListenerId = None
        self.ListenerName = None
        self.Port = None
        self.Offset = None
        self.Limit = None
        self.GroupId = None
        self.SearchValue = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Port = params.get("Port")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.GroupId = params.get("GroupId")
        self.SearchValue = params.get("SearchValue")


class DescribeTCPListenersResponse(AbstractModel):
    """DescribeTCPListeners返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 滿足條件的監聽器總個數
        :type TotalCount: int
        :param ListenerSet: TCP監聽器清單
        :type ListenerSet: list of TCPListener
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ListenerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ListenerSet") is not None:
            self.ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = TCPListener()
                obj._deserialize(item)
                self.ListenerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUDPListenersRequest(AbstractModel):
    """DescribeUDPListeners請求參數結構體

    """

    def __init__(self):
        """
        :param ProxyId: 過濾條件，根據通道ID進行拉取，ProxyId/GroupId/ListenerId必須設置一個，但ProxyId和GroupId不能同時設置。
        :type ProxyId: str
        :param ListenerId: 過濾條件，根據監聽器ID精确查詢。
當設置了ProxyId時，會檢查該監聽器是否歸屬於該通道。
當設置了GroupId時，會檢查該監聽器是否歸屬於該通道組。
        :type ListenerId: str
        :param ListenerName: 過濾條件，根據監聽器名稱精确查詢
        :type ListenerName: str
        :param Port: 過濾條件，根據監聽器端口精确查詢
        :type Port: int
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 限制數量，預設爲20
        :type Limit: int
        :param GroupId: 過濾條件，根據通道組ID進行拉取，ProxyId/GroupId/ListenerId必須設置一個，但ProxyId和GroupId不能同時設置。
        :type GroupId: str
        :param SearchValue: 過濾條件，支援按照端口或監聽器名稱進行模糊查詢，該參數不能與ListenerName和Port同時使用
        :type SearchValue: str
        """
        self.ProxyId = None
        self.ListenerId = None
        self.ListenerName = None
        self.Port = None
        self.Offset = None
        self.Limit = None
        self.GroupId = None
        self.SearchValue = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Port = params.get("Port")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.GroupId = params.get("GroupId")
        self.SearchValue = params.get("SearchValue")


class DescribeUDPListenersResponse(AbstractModel):
    """DescribeUDPListeners返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 監聽器個數
        :type TotalCount: int
        :param ListenerSet: UDP監聽器清單
        :type ListenerSet: list of UDPListener
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ListenerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ListenerSet") is not None:
            self.ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = UDPListener()
                obj._deserialize(item)
                self.ListenerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DestroyProxiesRequest(AbstractModel):
    """DestroyProxies請求參數結構體

    """

    def __init__(self):
        """
        :param Force: 強制删除標識。
1，強制删除該通道清單，無論是否已經綁定了源站；
0，如果已綁定了源站，則無法删除。
删除多通道時，如果該標識爲0，只有所有的通道都沒有綁定源站，才允許删除。
        :type Force: int
        :param InstanceIds: （舊參數，請切換到ProxyIds）通道實例ID清單。
        :type InstanceIds: list of str
        :param ClientToken: 用於保證請求幂等性的字串。該字串由客戶生成，需保證不同請求之間唯一，最大值不超過64個ASCII字元。若不指定該參數，則無法保證請求的幂等性。
更多詳細訊息請參閱：如何保證幂等性。
        :type ClientToken: str
        :param ProxyIds: （新參數）通道實例ID清單。
        :type ProxyIds: list of str
        """
        self.Force = None
        self.InstanceIds = None
        self.ClientToken = None
        self.ProxyIds = None


    def _deserialize(self, params):
        self.Force = params.get("Force")
        self.InstanceIds = params.get("InstanceIds")
        self.ClientToken = params.get("ClientToken")
        self.ProxyIds = params.get("ProxyIds")


class DestroyProxiesResponse(AbstractModel):
    """DestroyProxies返回參數結構體

    """

    def __init__(self):
        """
        :param InvalidStatusInstanceSet: 處於不可銷毀狀态下的通道實例ID清單。
        :type InvalidStatusInstanceSet: list of str
        :param OperationFailedInstanceSet: 銷毀操作失敗的通道實例ID清單。
        :type OperationFailedInstanceSet: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InvalidStatusInstanceSet = None
        self.OperationFailedInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InvalidStatusInstanceSet = params.get("InvalidStatusInstanceSet")
        self.OperationFailedInstanceSet = params.get("OperationFailedInstanceSet")
        self.RequestId = params.get("RequestId")


class DomainAccessRegionDict(AbstractModel):
    """域名解析就近訪問配置詳情

    """

    def __init__(self):
        """
        :param NationCountryInnerList: 就近接入區域
        :type NationCountryInnerList: list of NationCountryInnerInfo
        :param ProxyList: 加速區域通道清單
        :type ProxyList: list of ProxyIdDict
        :param RegionId: 加速區域ID
        :type RegionId: str
        :param GeographicalZoneInnerCode: 加速區域内部編碼
        :type GeographicalZoneInnerCode: str
        :param ContinentInnerCode: 加速區域所屬大洲内部編碼
        :type ContinentInnerCode: str
        :param RegionName: 加速區域别名
        :type RegionName: str
        """
        self.NationCountryInnerList = None
        self.ProxyList = None
        self.RegionId = None
        self.GeographicalZoneInnerCode = None
        self.ContinentInnerCode = None
        self.RegionName = None


    def _deserialize(self, params):
        if params.get("NationCountryInnerList") is not None:
            self.NationCountryInnerList = []
            for item in params.get("NationCountryInnerList"):
                obj = NationCountryInnerInfo()
                obj._deserialize(item)
                self.NationCountryInnerList.append(obj)
        if params.get("ProxyList") is not None:
            self.ProxyList = []
            for item in params.get("ProxyList"):
                obj = ProxyIdDict()
                obj._deserialize(item)
                self.ProxyList.append(obj)
        self.RegionId = params.get("RegionId")
        self.GeographicalZoneInnerCode = params.get("GeographicalZoneInnerCode")
        self.ContinentInnerCode = params.get("ContinentInnerCode")
        self.RegionName = params.get("RegionName")


class DomainErrorPageInfo(AbstractModel):
    """域名的定制錯誤響應配置

    """

    def __init__(self):
        """
        :param ErrorPageId: 錯誤定制響應的配置ID
        :type ErrorPageId: str
        :param ListenerId: 監聽器ID
        :type ListenerId: str
        :param Domain: 域名
        :type Domain: str
        :param ErrorNos: 原始錯誤碼
        :type ErrorNos: list of int
        :param NewErrorNo: 新的錯誤碼
注意：此欄位可能返回 null，表示取不到有效值。
        :type NewErrorNo: int
        :param ClearHeaders: 需要清理的響應頭
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClearHeaders: list of str
        :param SetHeaders: 需要設置的響應頭
注意：此欄位可能返回 null，表示取不到有效值。
        :type SetHeaders: list of HttpHeaderParam
        :param Body: 設置的響應體(不包括 HTTP頭)
注意：此欄位可能返回 null，表示取不到有效值。
        :type Body: str
        :param Status: 規則狀态,0爲成功
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self.ErrorPageId = None
        self.ListenerId = None
        self.Domain = None
        self.ErrorNos = None
        self.NewErrorNo = None
        self.ClearHeaders = None
        self.SetHeaders = None
        self.Body = None
        self.Status = None


    def _deserialize(self, params):
        self.ErrorPageId = params.get("ErrorPageId")
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.ErrorNos = params.get("ErrorNos")
        self.NewErrorNo = params.get("NewErrorNo")
        self.ClearHeaders = params.get("ClearHeaders")
        if params.get("SetHeaders") is not None:
            self.SetHeaders = []
            for item in params.get("SetHeaders"):
                obj = HttpHeaderParam()
                obj._deserialize(item)
                self.SetHeaders.append(obj)
        self.Body = params.get("Body")
        self.Status = params.get("Status")


class DomainRuleSet(AbstractModel):
    """按照域名分類的7層監聽器轉發規則訊息

    """

    def __init__(self):
        """
        :param Domain: 轉發規則域名。
        :type Domain: str
        :param RuleSet: 該域名對應的轉發規則清單。
        :type RuleSet: list of RuleInfo
        :param CertificateId: 該域名對應的服務器證書ID，值爲default時，表示使用預設證書（監聽器配置的證書）。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertificateId: str
        :param CertificateAlias: 該域名對應服務器證書名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertificateAlias: str
        :param ClientCertificateId: 該域名對應的用戶端證書ID，值爲default時，表示使用預設證書（監聽器配置的證書）。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClientCertificateId: str
        :param ClientCertificateAlias: 該域名對應用戶端證書名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClientCertificateAlias: str
        :param BasicAuthConfId: 該域名對應基礎認證配置ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type BasicAuthConfId: str
        :param BasicAuth: 基礎認證開關，其中：
0，表示未開啓；
1，表示已開啓。
注意：此欄位可能返回 null，表示取不到有效值。
        :type BasicAuth: int
        :param BasicAuthConfAlias: 該域名對應基礎認證配置名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type BasicAuthConfAlias: str
        :param RealServerCertificateId: 該域名對應源站認證證書ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RealServerCertificateId: str
        :param RealServerAuth: 源站認證開關，其中：
0，表示未開啓；
1，表示已開啓。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RealServerAuth: int
        :param RealServerCertificateAlias: 該域名對應源站認證證書名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RealServerCertificateAlias: str
        :param GaapCertificateId: 該域名對應通道認證證書ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type GaapCertificateId: str
        :param GaapAuth: 通道認證開關，其中：
0，表示未開啓；
1，表示已開啓。
注意：此欄位可能返回 null，表示取不到有效值。
        :type GaapAuth: int
        :param GaapCertificateAlias: 該域名對應通道認證證書名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type GaapCertificateAlias: str
        :param RealServerCertificateDomain: 源站認證域名。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RealServerCertificateDomain: str
        :param PolyClientCertificateAliasInfo: 多用戶端證書時，返回多個證書的id和别名
注意：此欄位可能返回 null，表示取不到有效值。
        :type PolyClientCertificateAliasInfo: list of CertificateAliasInfo
        :param PolyRealServerCertificateAliasInfo: 多源站證書時，返回多個證書的id和别名
注意：此欄位可能返回 null，表示取不到有效值。
        :type PolyRealServerCertificateAliasInfo: list of CertificateAliasInfo
        """
        self.Domain = None
        self.RuleSet = None
        self.CertificateId = None
        self.CertificateAlias = None
        self.ClientCertificateId = None
        self.ClientCertificateAlias = None
        self.BasicAuthConfId = None
        self.BasicAuth = None
        self.BasicAuthConfAlias = None
        self.RealServerCertificateId = None
        self.RealServerAuth = None
        self.RealServerCertificateAlias = None
        self.GaapCertificateId = None
        self.GaapAuth = None
        self.GaapCertificateAlias = None
        self.RealServerCertificateDomain = None
        self.PolyClientCertificateAliasInfo = None
        self.PolyRealServerCertificateAliasInfo = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        if params.get("RuleSet") is not None:
            self.RuleSet = []
            for item in params.get("RuleSet"):
                obj = RuleInfo()
                obj._deserialize(item)
                self.RuleSet.append(obj)
        self.CertificateId = params.get("CertificateId")
        self.CertificateAlias = params.get("CertificateAlias")
        self.ClientCertificateId = params.get("ClientCertificateId")
        self.ClientCertificateAlias = params.get("ClientCertificateAlias")
        self.BasicAuthConfId = params.get("BasicAuthConfId")
        self.BasicAuth = params.get("BasicAuth")
        self.BasicAuthConfAlias = params.get("BasicAuthConfAlias")
        self.RealServerCertificateId = params.get("RealServerCertificateId")
        self.RealServerAuth = params.get("RealServerAuth")
        self.RealServerCertificateAlias = params.get("RealServerCertificateAlias")
        self.GaapCertificateId = params.get("GaapCertificateId")
        self.GaapAuth = params.get("GaapAuth")
        self.GaapCertificateAlias = params.get("GaapCertificateAlias")
        self.RealServerCertificateDomain = params.get("RealServerCertificateDomain")
        if params.get("PolyClientCertificateAliasInfo") is not None:
            self.PolyClientCertificateAliasInfo = []
            for item in params.get("PolyClientCertificateAliasInfo"):
                obj = CertificateAliasInfo()
                obj._deserialize(item)
                self.PolyClientCertificateAliasInfo.append(obj)
        if params.get("PolyRealServerCertificateAliasInfo") is not None:
            self.PolyRealServerCertificateAliasInfo = []
            for item in params.get("PolyRealServerCertificateAliasInfo"):
                obj = CertificateAliasInfo()
                obj._deserialize(item)
                self.PolyRealServerCertificateAliasInfo.append(obj)


class Filter(AbstractModel):
    """過濾條件

    """

    def __init__(self):
        """
        :param Name: 過濾條件
        :type Name: str
        :param Values: 過濾值
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class GroupStatisticsInfo(AbstractModel):
    """可以顯示統計數據的通道組和對應通道訊息

    """

    def __init__(self):
        """
        :param GroupId: 通道組ID
        :type GroupId: str
        :param GroupName: 通道組名稱
        :type GroupName: str
        :param ProxySet: 通道組下通道清單
        :type ProxySet: list of ProxySimpleInfo
        """
        self.GroupId = None
        self.GroupName = None
        self.ProxySet = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        if params.get("ProxySet") is not None:
            self.ProxySet = []
            for item in params.get("ProxySet"):
                obj = ProxySimpleInfo()
                obj._deserialize(item)
                self.ProxySet.append(obj)


class HTTPListener(AbstractModel):
    """HTTP類型監聽器訊息

    """

    def __init__(self):
        """
        :param ListenerId: 監聽器ID
        :type ListenerId: str
        :param ListenerName: 監聽器名稱
        :type ListenerName: str
        :param Port: 監聽器端口
        :type Port: int
        :param CreateTime: 監聽器創建時間，Unix時間戳
        :type CreateTime: int
        :param Protocol: 監聽器協議
        :type Protocol: str
        :param ListenerStatus: 監聽器狀态，其中：
0表示運作中；
1表示創建中；
2表示銷毀中；
3表示源站調整中；
4表示配置變更中。
        :type ListenerStatus: int
        """
        self.ListenerId = None
        self.ListenerName = None
        self.Port = None
        self.CreateTime = None
        self.Protocol = None
        self.ListenerStatus = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Port = params.get("Port")
        self.CreateTime = params.get("CreateTime")
        self.Protocol = params.get("Protocol")
        self.ListenerStatus = params.get("ListenerStatus")


class HTTPSListener(AbstractModel):
    """HTTPS類型監聽器訊息

    """

    def __init__(self):
        """
        :param ListenerId: 監聽器ID
        :type ListenerId: str
        :param ListenerName: 監聽器名稱
        :type ListenerName: str
        :param Port: 監聽器端口
        :type Port: int
        :param Protocol: 監聽器協議， 值爲：HTTP
        :type Protocol: str
        :param ListenerStatus: 監聽器狀态，其中：
0表示運作中；
1表示創建中；
2表示銷毀中；
3表示源站調整中；
4表示配置變更中。
        :type ListenerStatus: int
        :param CertificateId: 監聽器服務器SSL證書ID
        :type CertificateId: str
        :param ForwardProtocol: 監聽器後端轉發源站協議
        :type ForwardProtocol: str
        :param CreateTime: 監聽器創建時間，Unix時間戳
        :type CreateTime: int
        :param CertificateAlias: 服務器SSL證書的别名
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertificateAlias: str
        :param ClientCertificateId: 監聽器用戶端CA證書ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClientCertificateId: str
        :param AuthType: 監聽器認證方式。其中，
0，單向認證；
1，雙向認證。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AuthType: int
        :param ClientCertificateAlias: 用戶端CA證書别名
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClientCertificateAlias: str
        :param PolyClientCertificateAliasInfo: 多用戶端CA證書别名訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type PolyClientCertificateAliasInfo: list of CertificateAliasInfo
        """
        self.ListenerId = None
        self.ListenerName = None
        self.Port = None
        self.Protocol = None
        self.ListenerStatus = None
        self.CertificateId = None
        self.ForwardProtocol = None
        self.CreateTime = None
        self.CertificateAlias = None
        self.ClientCertificateId = None
        self.AuthType = None
        self.ClientCertificateAlias = None
        self.PolyClientCertificateAliasInfo = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Port = params.get("Port")
        self.Protocol = params.get("Protocol")
        self.ListenerStatus = params.get("ListenerStatus")
        self.CertificateId = params.get("CertificateId")
        self.ForwardProtocol = params.get("ForwardProtocol")
        self.CreateTime = params.get("CreateTime")
        self.CertificateAlias = params.get("CertificateAlias")
        self.ClientCertificateId = params.get("ClientCertificateId")
        self.AuthType = params.get("AuthType")
        self.ClientCertificateAlias = params.get("ClientCertificateAlias")
        if params.get("PolyClientCertificateAliasInfo") is not None:
            self.PolyClientCertificateAliasInfo = []
            for item in params.get("PolyClientCertificateAliasInfo"):
                obj = CertificateAliasInfo()
                obj._deserialize(item)
                self.PolyClientCertificateAliasInfo.append(obj)


class HttpHeaderParam(AbstractModel):
    """描述HTTP的標頭參數

    """

    def __init__(self):
        """
        :param HeaderName: HTTP頭名
        :type HeaderName: str
        :param HeaderValue: HTTP頭值
        :type HeaderValue: str
        """
        self.HeaderName = None
        self.HeaderValue = None


    def _deserialize(self, params):
        self.HeaderName = params.get("HeaderName")
        self.HeaderValue = params.get("HeaderValue")


class InquiryPriceCreateProxyRequest(AbstractModel):
    """InquiryPriceCreateProxy請求參數結構體

    """

    def __init__(self):
        """
        :param AccessRegion: 加速區域名稱。
        :type AccessRegion: str
        :param Bandwidth: 通道頻寬上限，單位：Mbps。
        :type Bandwidth: int
        :param DestRegion: （舊參數，請切換到RealServerRegion）源站區域名稱。
        :type DestRegion: str
        :param Concurrency: （舊參數，請切換到Concurrent）通道並發量上限，表示同時在線的連接數，單位：萬。
        :type Concurrency: int
        :param RealServerRegion: （新參數）源站區域名稱。
        :type RealServerRegion: str
        :param Concurrent: （新參數）通道並發量上限，表示同時在線的連接數，單位：萬。
        :type Concurrent: int
        :param BillingType: 計費方式 (0:按頻寬計費，1:按流量計費 預設按頻寬計費）
        :type BillingType: int
        """
        self.AccessRegion = None
        self.Bandwidth = None
        self.DestRegion = None
        self.Concurrency = None
        self.RealServerRegion = None
        self.Concurrent = None
        self.BillingType = None


    def _deserialize(self, params):
        self.AccessRegion = params.get("AccessRegion")
        self.Bandwidth = params.get("Bandwidth")
        self.DestRegion = params.get("DestRegion")
        self.Concurrency = params.get("Concurrency")
        self.RealServerRegion = params.get("RealServerRegion")
        self.Concurrent = params.get("Concurrent")
        self.BillingType = params.get("BillingType")


class InquiryPriceCreateProxyResponse(AbstractModel):
    """InquiryPriceCreateProxy返回參數結構體

    """

    def __init__(self):
        """
        :param ProxyDailyPrice: 通道基礎費用價格，單位：元/天。
        :type ProxyDailyPrice: float
        :param BandwidthUnitPrice: 通道頻寬費用梯度價格。
注意：此欄位可能返回 null，表示取不到有效值。
        :type BandwidthUnitPrice: list of BandwidthPriceGradient
        :param DiscountProxyDailyPrice: 通道基礎費用折扣價格，單位：元/天。
        :type DiscountProxyDailyPrice: float
        :param Currency: 價格使用的貨币，支援人民币，美元等。
        :type Currency: str
        :param FlowUnitPrice: 通道的流量費用價格，單位: 元/GB
注意：此欄位可能返回 null，表示取不到有效值。
        :type FlowUnitPrice: float
        :param DiscountFlowUnitPrice: 通道的流量費用折扣價格，單位:元/GB
注意：此欄位可能返回 null，表示取不到有效值。
        :type DiscountFlowUnitPrice: float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ProxyDailyPrice = None
        self.BandwidthUnitPrice = None
        self.DiscountProxyDailyPrice = None
        self.Currency = None
        self.FlowUnitPrice = None
        self.DiscountFlowUnitPrice = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProxyDailyPrice = params.get("ProxyDailyPrice")
        if params.get("BandwidthUnitPrice") is not None:
            self.BandwidthUnitPrice = []
            for item in params.get("BandwidthUnitPrice"):
                obj = BandwidthPriceGradient()
                obj._deserialize(item)
                self.BandwidthUnitPrice.append(obj)
        self.DiscountProxyDailyPrice = params.get("DiscountProxyDailyPrice")
        self.Currency = params.get("Currency")
        self.FlowUnitPrice = params.get("FlowUnitPrice")
        self.DiscountFlowUnitPrice = params.get("DiscountFlowUnitPrice")
        self.RequestId = params.get("RequestId")


class ListenerInfo(AbstractModel):
    """内部介面使用，返回可以查詢統計數據的監聽器訊息

    """

    def __init__(self):
        """
        :param ListenerId: 監聽器ID
        :type ListenerId: str
        :param ListenerName: 監聽器名稱
        :type ListenerName: str
        :param Port: 監聽器監聽端口
        :type Port: int
        :param Protocol: 監聽器協議類型
        :type Protocol: str
        """
        self.ListenerId = None
        self.ListenerName = None
        self.Port = None
        self.Protocol = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Port = params.get("Port")
        self.Protocol = params.get("Protocol")


class MetricStatisticsInfo(AbstractModel):
    """單指標的統計數據

    """

    def __init__(self):
        """
        :param MetricName: 指標名稱
        :type MetricName: str
        :param MetricData: 指標統計數據
        :type MetricData: list of StatisticsDataInfo
        """
        self.MetricName = None
        self.MetricData = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        if params.get("MetricData") is not None:
            self.MetricData = []
            for item in params.get("MetricData"):
                obj = StatisticsDataInfo()
                obj._deserialize(item)
                self.MetricData.append(obj)


class ModifyCertificateAttributesRequest(AbstractModel):
    """ModifyCertificateAttributes請求參數結構體

    """

    def __init__(self):
        """
        :param CertificateId: 證書ID。
        :type CertificateId: str
        :param CertificateAlias: 證書名字。長度不超過50個字元。
        :type CertificateAlias: str
        """
        self.CertificateId = None
        self.CertificateAlias = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.CertificateAlias = params.get("CertificateAlias")


class ModifyCertificateAttributesResponse(AbstractModel):
    """ModifyCertificateAttributes返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCertificateRequest(AbstractModel):
    """ModifyCertificate請求參數結構體

    """

    def __init__(self):
        """
        :param ListenerId: 監聽器實例ID
        :type ListenerId: str
        :param Domain: 需要修改證書的域名
        :type Domain: str
        :param CertificateId: 新的服務器證書ID。其中：
當CertificateId=default時，表示使用監聽器的證書。
        :type CertificateId: str
        :param ClientCertificateId: 新的用戶端證書ID。其中：
當ClientCertificateId=default時，表示使用監聽器的證書。
僅當采用雙向認證方式時，需要設置該參數或者PolyClientCertificateIds。
        :type ClientCertificateId: str
        :param PolyClientCertificateIds: 新的多用戶端證書ID清單。其中：
僅當采用雙向認證方式時，需要設置該參數或ClientCertificateId參數。
        :type PolyClientCertificateIds: list of str
        """
        self.ListenerId = None
        self.Domain = None
        self.CertificateId = None
        self.ClientCertificateId = None
        self.PolyClientCertificateIds = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.CertificateId = params.get("CertificateId")
        self.ClientCertificateId = params.get("ClientCertificateId")
        self.PolyClientCertificateIds = params.get("PolyClientCertificateIds")


class ModifyCertificateResponse(AbstractModel):
    """ModifyCertificate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDomainRequest(AbstractModel):
    """ModifyDomain請求參數結構體

    """

    def __init__(self):
        """
        :param ListenerId: 7層監聽器ID
        :type ListenerId: str
        :param OldDomain: 修改前的域名訊息
        :type OldDomain: str
        :param NewDomain: 修改後的域名訊息
        :type NewDomain: str
        :param CertificateId: 服務器SSL證書ID，僅适用於version3.0的通道。其中：
不帶該欄位時，表示使用原證書；
攜帶該欄位時並且CertificateId=default，表示使用監聽器證書；
其他情況，使用該CertificateId指定的證書。
        :type CertificateId: str
        :param ClientCertificateId: 用戶端CA證書ID，僅适用於version3.0的通道。其中：
不帶該欄位和PolyClientCertificateIds時，表示使用原證書；
攜帶該欄位時並且ClientCertificateId=default，表示使用監聽器證書；
其他情況，使用該ClientCertificateId或PolyClientCertificateIds指定的證書。
        :type ClientCertificateId: str
        :param PolyClientCertificateIds: 用戶端CA證書ID，僅适用於version3.0的通道。其中：
不帶該欄位和ClientCertificateId時，表示使用原證書；
攜帶該欄位時並且ClientCertificateId=default，表示使用監聽器證書；
其他情況，使用該ClientCertificateId或PolyClientCertificateIds指定的證書。
        :type PolyClientCertificateIds: list of str
        """
        self.ListenerId = None
        self.OldDomain = None
        self.NewDomain = None
        self.CertificateId = None
        self.ClientCertificateId = None
        self.PolyClientCertificateIds = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.OldDomain = params.get("OldDomain")
        self.NewDomain = params.get("NewDomain")
        self.CertificateId = params.get("CertificateId")
        self.ClientCertificateId = params.get("ClientCertificateId")
        self.PolyClientCertificateIds = params.get("PolyClientCertificateIds")


class ModifyDomainResponse(AbstractModel):
    """ModifyDomain返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyGroupDomainConfigRequest(AbstractModel):
    """ModifyGroupDomainConfig請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 通道組ID。
        :type GroupId: str
        :param DefaultDnsIp: 域名解析預設訪問IP或域名。
        :type DefaultDnsIp: str
        :param AccessRegionList: 就近接入區域配置。
        :type AccessRegionList: list of AccessRegionDomainConf
        """
        self.GroupId = None
        self.DefaultDnsIp = None
        self.AccessRegionList = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.DefaultDnsIp = params.get("DefaultDnsIp")
        if params.get("AccessRegionList") is not None:
            self.AccessRegionList = []
            for item in params.get("AccessRegionList"):
                obj = AccessRegionDomainConf()
                obj._deserialize(item)
                self.AccessRegionList.append(obj)


class ModifyGroupDomainConfigResponse(AbstractModel):
    """ModifyGroupDomainConfig返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyHTTPListenerAttributeRequest(AbstractModel):
    """ModifyHTTPListenerAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param ListenerId: 需要修改的監聽器ID
        :type ListenerId: str
        :param ListenerName: 新的監聽器名稱
        :type ListenerName: str
        :param ProxyId: 通道ID
        :type ProxyId: str
        """
        self.ListenerId = None
        self.ListenerName = None
        self.ProxyId = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.ProxyId = params.get("ProxyId")


class ModifyHTTPListenerAttributeResponse(AbstractModel):
    """ModifyHTTPListenerAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyHTTPSListenerAttributeRequest(AbstractModel):
    """ModifyHTTPSListenerAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param ListenerId: 監聽器ID
        :type ListenerId: str
        :param ProxyId: 通道ID， 若爲單通道監聽器，此項必須填寫
        :type ProxyId: str
        :param ListenerName: 修改後的監聽器名稱
        :type ListenerName: str
        :param ForwardProtocol: 監聽器後端轉發與源站之間的協議類型
        :type ForwardProtocol: str
        :param CertificateId: 修改後的監聽器服務器證書ID
        :type CertificateId: str
        :param ClientCertificateId: 修改後的監聽器用戶端證書ID，不支援多用戶端證書，多用戶端證書新采用PolyClientCertificateIds欄位
        :type ClientCertificateId: str
        :param PolyClientCertificateIds: 新欄位,修改後的監聽器用戶端證書ID
        :type PolyClientCertificateIds: list of str
        """
        self.ListenerId = None
        self.ProxyId = None
        self.ListenerName = None
        self.ForwardProtocol = None
        self.CertificateId = None
        self.ClientCertificateId = None
        self.PolyClientCertificateIds = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ProxyId = params.get("ProxyId")
        self.ListenerName = params.get("ListenerName")
        self.ForwardProtocol = params.get("ForwardProtocol")
        self.CertificateId = params.get("CertificateId")
        self.ClientCertificateId = params.get("ClientCertificateId")
        self.PolyClientCertificateIds = params.get("PolyClientCertificateIds")


class ModifyHTTPSListenerAttributeResponse(AbstractModel):
    """ModifyHTTPSListenerAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyProxiesAttributeRequest(AbstractModel):
    """ModifyProxiesAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: （舊參數，請切換到ProxyIds）一個或多個待操作的通道ID。
        :type InstanceIds: list of str
        :param ProxyName: 通道名稱。可任意命名，但不得超過30個字元。
        :type ProxyName: str
        :param ClientToken: 用於保證請求幂等性的字串。該字串由客戶生成，需保證不同請求之間唯一，最大值不超過64個ASCII字元。若不指定該參數，則無法保證請求的幂等性。
更多詳細訊息請參閱：如何保證幂等性。
        :type ClientToken: str
        :param ProxyIds: （新參數）一個或多個待操作的通道ID。
        :type ProxyIds: list of str
        """
        self.InstanceIds = None
        self.ProxyName = None
        self.ClientToken = None
        self.ProxyIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.ProxyName = params.get("ProxyName")
        self.ClientToken = params.get("ClientToken")
        self.ProxyIds = params.get("ProxyIds")


class ModifyProxiesAttributeResponse(AbstractModel):
    """ModifyProxiesAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyProxiesProjectRequest(AbstractModel):
    """ModifyProxiesProject請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: 需要修改到的項目ID。
        :type ProjectId: int
        :param InstanceIds: （舊參數，請切換到ProxyIds）一個或多個待操作的通道ID。
        :type InstanceIds: list of str
        :param ClientToken: 用於保證請求幂等性的字串。該字串由客戶生成，需保證不同請求之間唯一，最大值不超過64個ASCII字元。若不指定該參數，則無法保證請求的幂等性。
更多詳細訊息請參閱：如何保證幂等性。
        :type ClientToken: str
        :param ProxyIds: （新參數）一個或多個待操作的通道ID。
        :type ProxyIds: list of str
        """
        self.ProjectId = None
        self.InstanceIds = None
        self.ClientToken = None
        self.ProxyIds = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.InstanceIds = params.get("InstanceIds")
        self.ClientToken = params.get("ClientToken")
        self.ProxyIds = params.get("ProxyIds")


class ModifyProxiesProjectResponse(AbstractModel):
    """ModifyProxiesProject返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyProxyConfigurationRequest(AbstractModel):
    """ModifyProxyConfiguration請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: （舊參數，請切換到ProxyId）通道的實例ID。
        :type InstanceId: str
        :param Bandwidth: 需要調整到的目標頻寬，單位：Mbps。
Bandwidth與Concurrent必須至少設置一個。取值範圍根據DescribeAccessRegionsByDestRegion介面獲取得到
        :type Bandwidth: int
        :param Concurrent: 需要調整到的目標並發值，單位：萬。
Bandwidth與Concurrent必須至少設置一個。取值範圍根據DescribeAccessRegionsByDestRegion介面獲取得到
        :type Concurrent: int
        :param ClientToken: 用於保證請求幂等性的字串。該字串由客戶生成，需保證不同請求之間唯一，最大值不超過64個ASCII字元。若不指定該參數，則無法保證請求的幂等性。
更多詳細訊息請參閱：如何保證幂等性。
        :type ClientToken: str
        :param ProxyId: （新參數）通道的實例ID。
        :type ProxyId: str
        :param BillingType: 計費方式 (0:按頻寬計費，1:按流量計費 預設按頻寬計費）
        :type BillingType: int
        """
        self.InstanceId = None
        self.Bandwidth = None
        self.Concurrent = None
        self.ClientToken = None
        self.ProxyId = None
        self.BillingType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Bandwidth = params.get("Bandwidth")
        self.Concurrent = params.get("Concurrent")
        self.ClientToken = params.get("ClientToken")
        self.ProxyId = params.get("ProxyId")
        self.BillingType = params.get("BillingType")


class ModifyProxyConfigurationResponse(AbstractModel):
    """ModifyProxyConfiguration返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyProxyGroupAttributeRequest(AbstractModel):
    """ModifyProxyGroupAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 需要修改的通道組ID。
        :type GroupId: str
        :param GroupName: 修改後的通道組名稱：不超過30個字元，超過部分會被截斷。
        :type GroupName: str
        """
        self.GroupId = None
        self.GroupName = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")


class ModifyProxyGroupAttributeResponse(AbstractModel):
    """ModifyProxyGroupAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRealServerNameRequest(AbstractModel):
    """ModifyRealServerName請求參數結構體

    """

    def __init__(self):
        """
        :param RealServerName: 源站名稱
        :type RealServerName: str
        :param RealServerId: 源站ID
        :type RealServerId: str
        """
        self.RealServerName = None
        self.RealServerId = None


    def _deserialize(self, params):
        self.RealServerName = params.get("RealServerName")
        self.RealServerId = params.get("RealServerId")


class ModifyRealServerNameResponse(AbstractModel):
    """ModifyRealServerName返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRuleAttributeRequest(AbstractModel):
    """ModifyRuleAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param ListenerId: 監聽器ID
        :type ListenerId: str
        :param RuleId: 轉發規則ID
        :type RuleId: str
        :param Scheduler: 調度策略，其中：
rr，輪詢；
wrr，加權輪詢；
lc，最小連接數。
        :type Scheduler: str
        :param HealthCheck: 源站健康檢查開關，其中：
1，開啓；
0，關閉。
        :type HealthCheck: int
        :param CheckParams: 健康檢查配置參數
        :type CheckParams: :class:`taifucloudcloud.gaap.v20180529.models.RuleCheckParams`
        :param Path: 轉發規則路徑
        :type Path: str
        :param ForwardProtocol: 加速通道轉發到源站的協議類型，支援：default, HTTP和HTTPS。
當ForwardProtocol=default時，表示使用對應監聽器的ForwardProtocol。
        :type ForwardProtocol: str
        :param ForwardHost: 加速通道轉發到源站的請求中攜帶的host。
當ForwardHost=default時，使用規則的域名，其他情況爲該欄位所設置的值。
        :type ForwardHost: str
        """
        self.ListenerId = None
        self.RuleId = None
        self.Scheduler = None
        self.HealthCheck = None
        self.CheckParams = None
        self.Path = None
        self.ForwardProtocol = None
        self.ForwardHost = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.RuleId = params.get("RuleId")
        self.Scheduler = params.get("Scheduler")
        self.HealthCheck = params.get("HealthCheck")
        if params.get("CheckParams") is not None:
            self.CheckParams = RuleCheckParams()
            self.CheckParams._deserialize(params.get("CheckParams"))
        self.Path = params.get("Path")
        self.ForwardProtocol = params.get("ForwardProtocol")
        self.ForwardHost = params.get("ForwardHost")


class ModifyRuleAttributeResponse(AbstractModel):
    """ModifyRuleAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySecurityRuleRequest(AbstractModel):
    """ModifySecurityRule請求參數結構體

    """

    def __init__(self):
        """
        :param RuleId: 規則ID
        :type RuleId: str
        :param AliasName: 規則名：不得超過30個字元，超過部分會被截斷。
        :type AliasName: str
        :param PolicyId: 安全策略ID
        :type PolicyId: str
        """
        self.RuleId = None
        self.AliasName = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.AliasName = params.get("AliasName")
        self.PolicyId = params.get("PolicyId")


class ModifySecurityRuleResponse(AbstractModel):
    """ModifySecurityRule返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTCPListenerAttributeRequest(AbstractModel):
    """ModifyTCPListenerAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param ListenerId: 監聽器ID
        :type ListenerId: str
        :param GroupId: 通道組ID，ProxyId和GroupId必須設置一個，但不能同時設置。
        :type GroupId: str
        :param ProxyId: 通道ID，ProxyId和GroupId必須設置一個，但不能同時設置。
        :type ProxyId: str
        :param ListenerName: 監聽器名稱
        :type ListenerName: str
        :param Scheduler: 監聽器源站調度策略，支援輪詢（rr），加權輪詢（wrr），最小連接數（lc）。
        :type Scheduler: str
        :param DelayLoop: 源站健康檢查時間間隔，單位：秒。時間間隔取值在[5，300]之間。
        :type DelayLoop: int
        :param ConnectTimeout: 源站健康檢查響應超時時間，單位：秒。超時時間取值在[2，60]之間。超時時間應小於健康檢查時間間隔DelayLoop。
        :type ConnectTimeout: int
        :param HealthCheck: 是否開啓健康檢查，1開啓，0關閉。
        :type HealthCheck: int
        """
        self.ListenerId = None
        self.GroupId = None
        self.ProxyId = None
        self.ListenerName = None
        self.Scheduler = None
        self.DelayLoop = None
        self.ConnectTimeout = None
        self.HealthCheck = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.GroupId = params.get("GroupId")
        self.ProxyId = params.get("ProxyId")
        self.ListenerName = params.get("ListenerName")
        self.Scheduler = params.get("Scheduler")
        self.DelayLoop = params.get("DelayLoop")
        self.ConnectTimeout = params.get("ConnectTimeout")
        self.HealthCheck = params.get("HealthCheck")


class ModifyTCPListenerAttributeResponse(AbstractModel):
    """ModifyTCPListenerAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyUDPListenerAttributeRequest(AbstractModel):
    """ModifyUDPListenerAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param ListenerId: 監聽器ID
        :type ListenerId: str
        :param GroupId: 通道組ID，ProxyId和GroupId必須設置一個，但不能同時設置。
        :type GroupId: str
        :param ProxyId: 通道ID，ProxyId和GroupId必須設置一個，但不能同時設置。
        :type ProxyId: str
        :param ListenerName: 監聽器名稱
        :type ListenerName: str
        :param Scheduler: 監聽器源站調度策略
        :type Scheduler: str
        """
        self.ListenerId = None
        self.GroupId = None
        self.ProxyId = None
        self.ListenerName = None
        self.Scheduler = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.GroupId = params.get("GroupId")
        self.ProxyId = params.get("ProxyId")
        self.ListenerName = params.get("ListenerName")
        self.Scheduler = params.get("Scheduler")


class ModifyUDPListenerAttributeResponse(AbstractModel):
    """ModifyUDPListenerAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NationCountryInnerInfo(AbstractModel):
    """就近接入的國家地區詳情

    """

    def __init__(self):
        """
        :param NationCountryName: 國家名
        :type NationCountryName: str
        :param NationCountryInnerCode: 國家内部編碼
        :type NationCountryInnerCode: str
        """
        self.NationCountryName = None
        self.NationCountryInnerCode = None


    def _deserialize(self, params):
        self.NationCountryName = params.get("NationCountryName")
        self.NationCountryInnerCode = params.get("NationCountryInnerCode")


class NewRealServer(AbstractModel):
    """新添加源站訊息

    """

    def __init__(self):
        """
        :param RealServerId: 源站ID
        :type RealServerId: str
        :param RealServerIP: 源站ip或域名
        :type RealServerIP: str
        """
        self.RealServerId = None
        self.RealServerIP = None


    def _deserialize(self, params):
        self.RealServerId = params.get("RealServerId")
        self.RealServerIP = params.get("RealServerIP")


class OpenProxiesRequest(AbstractModel):
    """OpenProxies請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: （舊參數，請切換到ProxyIds）通道的實例ID清單。
        :type InstanceIds: list of str
        :param ClientToken: 用於保證請求幂等性的字串。該字串由客戶生成，需保證不同請求之間唯一，最大值不超過64個ASCII字元。若不指定該參數，則無法保證請求的幂等性。
更多詳細訊息請參閱：如何保證幂等性。
        :type ClientToken: str
        :param ProxyIds: （新參數）通道的實例ID清單。
        :type ProxyIds: list of str
        """
        self.InstanceIds = None
        self.ClientToken = None
        self.ProxyIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.ClientToken = params.get("ClientToken")
        self.ProxyIds = params.get("ProxyIds")


class OpenProxiesResponse(AbstractModel):
    """OpenProxies返回參數結構體

    """

    def __init__(self):
        """
        :param InvalidStatusInstanceSet: 非關閉狀态下的通道實例ID清單，不可開啓。
        :type InvalidStatusInstanceSet: list of str
        :param OperationFailedInstanceSet: 開啓操作失敗的通道實例ID清單。
        :type OperationFailedInstanceSet: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InvalidStatusInstanceSet = None
        self.OperationFailedInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InvalidStatusInstanceSet = params.get("InvalidStatusInstanceSet")
        self.OperationFailedInstanceSet = params.get("OperationFailedInstanceSet")
        self.RequestId = params.get("RequestId")


class OpenSecurityPolicyRequest(AbstractModel):
    """OpenSecurityPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param ProxyId: 需開啓安全策略的通道ID
        :type ProxyId: str
        """
        self.ProxyId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")


class OpenSecurityPolicyResponse(AbstractModel):
    """OpenSecurityPolicy返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步流程ID，可以通過DescribeAsyncTaskStatus介面查詢流程運作狀态
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ProxyGroupDetail(AbstractModel):
    """通道組詳情訊息

    """

    def __init__(self):
        """
        :param CreateTime: 創建時間
        :type CreateTime: int
        :param ProjectId: 項目ID
        :type ProjectId: int
        :param ProxyNum: 通道組中通道數量
        :type ProxyNum: int
        :param Status: 通道組狀态：
0表示正常運作；
1表示創建中；
4表示銷毀中；
11表示遷移中；
        :type Status: int
        :param OwnerUin: 歸屬Uin
        :type OwnerUin: str
        :param CreateUin: 創建Uin
        :type CreateUin: str
        :param GroupName: 通道名稱
        :type GroupName: str
        :param DnsDefaultIp: 通道組域名解析預設IP
        :type DnsDefaultIp: str
        :param Domain: 通道組域名
注意：此欄位可能返回 null，表示取不到有效值。
        :type Domain: str
        :param RealServerRegionInfo: 目標地域
        :type RealServerRegionInfo: :class:`taifucloudcloud.gaap.v20180529.models.RegionDetail`
        :param IsOldGroup: 是否老通道組，2018-08-03之前創建的通道組爲老通道組
        :type IsOldGroup: bool
        :param GroupId: 通道組ID
        :type GroupId: str
        :param TagSet: 標簽清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagSet: list of TagPair
        """
        self.CreateTime = None
        self.ProjectId = None
        self.ProxyNum = None
        self.Status = None
        self.OwnerUin = None
        self.CreateUin = None
        self.GroupName = None
        self.DnsDefaultIp = None
        self.Domain = None
        self.RealServerRegionInfo = None
        self.IsOldGroup = None
        self.GroupId = None
        self.TagSet = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.ProjectId = params.get("ProjectId")
        self.ProxyNum = params.get("ProxyNum")
        self.Status = params.get("Status")
        self.OwnerUin = params.get("OwnerUin")
        self.CreateUin = params.get("CreateUin")
        self.GroupName = params.get("GroupName")
        self.DnsDefaultIp = params.get("DnsDefaultIp")
        self.Domain = params.get("Domain")
        if params.get("RealServerRegionInfo") is not None:
            self.RealServerRegionInfo = RegionDetail()
            self.RealServerRegionInfo._deserialize(params.get("RealServerRegionInfo"))
        self.IsOldGroup = params.get("IsOldGroup")
        self.GroupId = params.get("GroupId")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self.TagSet.append(obj)


class ProxyGroupInfo(AbstractModel):
    """通道組詳情清單

    """

    def __init__(self):
        """
        :param GroupId: 通道組id
        :type GroupId: str
        :param Domain: 通道組域名
注意：此欄位可能返回 null，表示取不到有效值。
        :type Domain: str
        :param GroupName: 通道組名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param ProjectId: 項目ID
        :type ProjectId: int
        :param RealServerRegionInfo: 目標地域
        :type RealServerRegionInfo: :class:`taifucloudcloud.gaap.v20180529.models.RegionDetail`
        :param Status: 通道組狀态。
其中，
0表示運作中；
1表示創建中；
4表示銷毀中；
11表示通道遷移中。
        :type Status: str
        :param TagSet: 標簽清單。
        :type TagSet: list of TagPair
        """
        self.GroupId = None
        self.Domain = None
        self.GroupName = None
        self.ProjectId = None
        self.RealServerRegionInfo = None
        self.Status = None
        self.TagSet = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Domain = params.get("Domain")
        self.GroupName = params.get("GroupName")
        self.ProjectId = params.get("ProjectId")
        if params.get("RealServerRegionInfo") is not None:
            self.RealServerRegionInfo = RegionDetail()
            self.RealServerRegionInfo._deserialize(params.get("RealServerRegionInfo"))
        self.Status = params.get("Status")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self.TagSet.append(obj)


class ProxyIdDict(AbstractModel):
    """通道ID

    """

    def __init__(self):
        """
        :param ProxyId: 通道ID
        :type ProxyId: str
        """
        self.ProxyId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")


class ProxyInfo(AbstractModel):
    """通道訊息

    """

    def __init__(self):
        """
        :param InstanceId: （舊參數，請使用ProxyId）通道實例ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param CreateTime: 創建時間，采用Unix時間戳的方式，表示從1970年1月1日（UTC/GMT的午夜）開始所經過的秒數。
        :type CreateTime: int
        :param ProjectId: 項目ID。
        :type ProjectId: int
        :param ProxyName: 通道名稱。
        :type ProxyName: str
        :param AccessRegion: 接入地域。
        :type AccessRegion: str
        :param RealServerRegion: 源站地域。
        :type RealServerRegion: str
        :param Bandwidth: 頻寬，單位：Mbps。
        :type Bandwidth: int
        :param Concurrent: 並發，單位：個/秒。
        :type Concurrent: int
        :param Status: 通道狀态。其中：
RUNNING表示運作中；
CREATING表示創建中；
DESTROYING表示銷毀中；
OPENING表示開啓中；
CLOSING表示關閉中；
CLOSED表示已關閉；
ADJUSTING表示配置變更中；
ISOLATING表示隔離中；
ISOLATED表示已隔離；
CLONING表示複制中；
UNKNOWN表示未知狀态。
        :type Status: str
        :param Domain: 接入域名。
        :type Domain: str
        :param IP: 接入IP。
        :type IP: str
        :param Version: 通道版本號：1.0，2.0，3.0。
        :type Version: str
        :param ProxyId: （新參數）通道實例ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProxyId: str
        :param Scalarable: 1，該通道可縮擴容；0，該通道無法縮擴容。
        :type Scalarable: int
        :param SupportProtocols: 支援的協議類型。
        :type SupportProtocols: list of str
        :param GroupId: 通道組ID，當通道歸屬於某一通道組時，存在該欄位。
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param PolicyId: 安全策略ID，當設置了安全策略時，存在該欄位。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PolicyId: str
        :param AccessRegionInfo: 接入地域詳細訊息，包括地域ID和地域名。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AccessRegionInfo: :class:`taifucloudcloud.gaap.v20180529.models.RegionDetail`
        :param RealServerRegionInfo: 源站地域詳細訊息，包括地域ID和地域名。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RealServerRegionInfo: :class:`taifucloudcloud.gaap.v20180529.models.RegionDetail`
        :param ForwardIP: 通道轉發IP
        :type ForwardIP: str
        :param TagSet: 標簽清單，不存在標簽時，該欄位爲空清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagSet: list of TagPair
        :param SupportSecurity: 是否支援安全組配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type SupportSecurity: int
        :param BillingType: 計費類型:(0:按頻寬計費  1:按流量計費）
注意：此欄位可能返回 null，表示取不到有效值。
        :type BillingType: int
        """
        self.InstanceId = None
        self.CreateTime = None
        self.ProjectId = None
        self.ProxyName = None
        self.AccessRegion = None
        self.RealServerRegion = None
        self.Bandwidth = None
        self.Concurrent = None
        self.Status = None
        self.Domain = None
        self.IP = None
        self.Version = None
        self.ProxyId = None
        self.Scalarable = None
        self.SupportProtocols = None
        self.GroupId = None
        self.PolicyId = None
        self.AccessRegionInfo = None
        self.RealServerRegionInfo = None
        self.ForwardIP = None
        self.TagSet = None
        self.SupportSecurity = None
        self.BillingType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.CreateTime = params.get("CreateTime")
        self.ProjectId = params.get("ProjectId")
        self.ProxyName = params.get("ProxyName")
        self.AccessRegion = params.get("AccessRegion")
        self.RealServerRegion = params.get("RealServerRegion")
        self.Bandwidth = params.get("Bandwidth")
        self.Concurrent = params.get("Concurrent")
        self.Status = params.get("Status")
        self.Domain = params.get("Domain")
        self.IP = params.get("IP")
        self.Version = params.get("Version")
        self.ProxyId = params.get("ProxyId")
        self.Scalarable = params.get("Scalarable")
        self.SupportProtocols = params.get("SupportProtocols")
        self.GroupId = params.get("GroupId")
        self.PolicyId = params.get("PolicyId")
        if params.get("AccessRegionInfo") is not None:
            self.AccessRegionInfo = RegionDetail()
            self.AccessRegionInfo._deserialize(params.get("AccessRegionInfo"))
        if params.get("RealServerRegionInfo") is not None:
            self.RealServerRegionInfo = RegionDetail()
            self.RealServerRegionInfo._deserialize(params.get("RealServerRegionInfo"))
        self.ForwardIP = params.get("ForwardIP")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.SupportSecurity = params.get("SupportSecurity")
        self.BillingType = params.get("BillingType")


class ProxySimpleInfo(AbstractModel):
    """内部介面使用，返回可以查詢統計數據的通道和對應的監聽器訊息

    """

    def __init__(self):
        """
        :param ProxyId: 通道ID
        :type ProxyId: str
        :param ProxyName: 通道名稱
        :type ProxyName: str
        :param ListenerList: 監聽器清單
        :type ListenerList: list of ListenerInfo
        """
        self.ProxyId = None
        self.ProxyName = None
        self.ListenerList = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.ProxyName = params.get("ProxyName")
        if params.get("ListenerList") is not None:
            self.ListenerList = []
            for item in params.get("ListenerList"):
                obj = ListenerInfo()
                obj._deserialize(item)
                self.ListenerList.append(obj)


class ProxyStatus(AbstractModel):
    """通道狀态訊息

    """

    def __init__(self):
        """
        :param InstanceId: 通道實例ID。
        :type InstanceId: str
        :param Status: 通道狀态。
其中：
RUNNING表示運作中；
CREATING表示創建中；
DESTROYING表示銷毀中；
OPENING表示開啓中；
CLOSING表示關閉中；
CLOSED表示已關閉；
ADJUSTING表示配置變更中；
ISOLATING表示隔離中；
ISOLATED表示已隔離；
UNKNOWN表示未知狀态。
        :type Status: str
        """
        self.InstanceId = None
        self.Status = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Status = params.get("Status")


class RealServer(AbstractModel):
    """查詢監聽器或者規則相關的源站訊息，不包括tag訊息

    """

    def __init__(self):
        """
        :param RealServerIP: 源站的IP或域名
        :type RealServerIP: str
        :param RealServerId: 源站ID
        :type RealServerId: str
        :param RealServerName: 源站名稱
        :type RealServerName: str
        :param ProjectId: 項目ID
        :type ProjectId: int
        """
        self.RealServerIP = None
        self.RealServerId = None
        self.RealServerName = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.RealServerIP = params.get("RealServerIP")
        self.RealServerId = params.get("RealServerId")
        self.RealServerName = params.get("RealServerName")
        self.ProjectId = params.get("ProjectId")


class RealServerBindSetReq(AbstractModel):
    """RealServerBindSetReq

    """

    def __init__(self):
        """
        :param RealServerId: 源站id
        :type RealServerId: str
        :param RealServerPort: 源站端口
        :type RealServerPort: int
        :param RealServerIP: 源站IP
        :type RealServerIP: str
        :param RealServerWeight: 源站權重
        :type RealServerWeight: int
        """
        self.RealServerId = None
        self.RealServerPort = None
        self.RealServerIP = None
        self.RealServerWeight = None


    def _deserialize(self, params):
        self.RealServerId = params.get("RealServerId")
        self.RealServerPort = params.get("RealServerPort")
        self.RealServerIP = params.get("RealServerIP")
        self.RealServerWeight = params.get("RealServerWeight")


class RealServerStatus(AbstractModel):
    """源站綁定訊息查詢，BindStatus， 0: 未被綁定 1：被規則或者監聽器綁定

    """

    def __init__(self):
        """
        :param RealServerId: 源站ID。
        :type RealServerId: str
        :param BindStatus: 0表示未被綁定 1表示被規則或者監聽器綁定。
        :type BindStatus: int
        :param ProxyId: 綁定此源站的通道ID，沒有綁定時爲空字串。
        :type ProxyId: str
        """
        self.RealServerId = None
        self.BindStatus = None
        self.ProxyId = None


    def _deserialize(self, params):
        self.RealServerId = params.get("RealServerId")
        self.BindStatus = params.get("BindStatus")
        self.ProxyId = params.get("ProxyId")


class RegionDetail(AbstractModel):
    """區域訊息詳情

    """

    def __init__(self):
        """
        :param RegionId: 區域ID
        :type RegionId: str
        :param RegionName: 區域英文名或中文名
        :type RegionName: str
        """
        self.RegionId = None
        self.RegionName = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")


class RemoveRealServersRequest(AbstractModel):
    """RemoveRealServers請求參數結構體

    """

    def __init__(self):
        """
        :param RealServerIds: 源站Id清單
        :type RealServerIds: list of str
        """
        self.RealServerIds = None


    def _deserialize(self, params):
        self.RealServerIds = params.get("RealServerIds")


class RemoveRealServersResponse(AbstractModel):
    """RemoveRealServers返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RuleCheckParams(AbstractModel):
    """7層監聽器轉發規則健康檢查相關參數

    """

    def __init__(self):
        """
        :param DelayLoop: 健康檢查的時間間隔
        :type DelayLoop: int
        :param ConnectTimeout: 健康檢查的響應超時時間
        :type ConnectTimeout: int
        :param Path: 健康檢查的檢查路徑
        :type Path: str
        :param Method: 健康檢查的方法，GET/HEAD
        :type Method: str
        :param StatusCode: 确認源站正常的返回碼，可選範圍[100, 200, 300, 400, 500]
        :type StatusCode: list of int non-negative
        :param Domain: 健康檢查的檢查域名。
當調用ModifyRuleAttribute時，不支援修改該參數。
        :type Domain: str
        """
        self.DelayLoop = None
        self.ConnectTimeout = None
        self.Path = None
        self.Method = None
        self.StatusCode = None
        self.Domain = None


    def _deserialize(self, params):
        self.DelayLoop = params.get("DelayLoop")
        self.ConnectTimeout = params.get("ConnectTimeout")
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        self.StatusCode = params.get("StatusCode")
        self.Domain = params.get("Domain")


class RuleInfo(AbstractModel):
    """7層監聽器轉發規則訊息

    """

    def __init__(self):
        """
        :param RuleId: 規則訊息
        :type RuleId: str
        :param ListenerId: 監聽器訊息
        :type ListenerId: str
        :param Domain: 規則域名
        :type Domain: str
        :param Path: 規則路徑
        :type Path: str
        :param RealServerType: 源站類型
        :type RealServerType: str
        :param Scheduler: 轉發源站策略
        :type Scheduler: str
        :param HealthCheck: 是否開啓健康檢查標志，1表示開啓，0表示關閉
        :type HealthCheck: int
        :param RuleStatus: 規則狀态，0表示運作中，1表示創建中，2表示銷毀中，3表示綁定解綁源站中，4表示配置更新中
        :type RuleStatus: int
        :param CheckParams: 健康檢查相關參數
        :type CheckParams: :class:`taifucloudcloud.gaap.v20180529.models.RuleCheckParams`
        :param RealServerSet: 已綁定的源站相關訊息
        :type RealServerSet: list of BindRealServer
        :param BindStatus: 源站的服務狀态，0表示異常，1表示正常。
未開啓健康檢查時，該狀态始終未正常。
只要有一個源站健康狀态爲異常時，該狀态爲異常，具體源站的狀态請檢視RealServerSet。
        :type BindStatus: int
        :param ForwardHost: 通道轉發到源站的請求所攜帶的host，其中default表示直接轉發接收到的host。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ForwardHost: str
        """
        self.RuleId = None
        self.ListenerId = None
        self.Domain = None
        self.Path = None
        self.RealServerType = None
        self.Scheduler = None
        self.HealthCheck = None
        self.RuleStatus = None
        self.CheckParams = None
        self.RealServerSet = None
        self.BindStatus = None
        self.ForwardHost = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.Path = params.get("Path")
        self.RealServerType = params.get("RealServerType")
        self.Scheduler = params.get("Scheduler")
        self.HealthCheck = params.get("HealthCheck")
        self.RuleStatus = params.get("RuleStatus")
        if params.get("CheckParams") is not None:
            self.CheckParams = RuleCheckParams()
            self.CheckParams._deserialize(params.get("CheckParams"))
        if params.get("RealServerSet") is not None:
            self.RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = BindRealServer()
                obj._deserialize(item)
                self.RealServerSet.append(obj)
        self.BindStatus = params.get("BindStatus")
        self.ForwardHost = params.get("ForwardHost")


class SecurityPolicyRuleIn(AbstractModel):
    """安全策略規則（入參）

    """

    def __init__(self):
        """
        :param SourceCidr: 請求來源IP或IP段。
        :type SourceCidr: str
        :param Action: 策略：允許（ACCEPT）或拒絕（DROP）
        :type Action: str
        :param AliasName: 規則别名
        :type AliasName: str
        :param Protocol: 協議：TCP或UDP，ALL表示所有協議
        :type Protocol: str
        :param DestPortRange: 目標端口，填寫格式舉例：
單個端口: 80
多個端口: 80,443
連續端口: 3306-20000
所有端口: ALL
        :type DestPortRange: str
        """
        self.SourceCidr = None
        self.Action = None
        self.AliasName = None
        self.Protocol = None
        self.DestPortRange = None


    def _deserialize(self, params):
        self.SourceCidr = params.get("SourceCidr")
        self.Action = params.get("Action")
        self.AliasName = params.get("AliasName")
        self.Protocol = params.get("Protocol")
        self.DestPortRange = params.get("DestPortRange")


class SecurityPolicyRuleOut(AbstractModel):
    """安全策略規則（出參）

    """

    def __init__(self):
        """
        :param Action: 策略：允許（ACCEPT）或拒絕（DROP）
        :type Action: str
        :param SourceCidr: 請求來源Ip或Ip段
        :type SourceCidr: str
        :param AliasName: 規則别名
        :type AliasName: str
        :param DestPortRange: 目標端口範圍
注意：此欄位可能返回 null，表示取不到有效值。
        :type DestPortRange: str
        :param RuleId: 規則ID
        :type RuleId: str
        :param Protocol: 要比對的協議類型（TCP/UDP）
注意：此欄位可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param PolicyId: 安全策略ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type PolicyId: str
        """
        self.Action = None
        self.SourceCidr = None
        self.AliasName = None
        self.DestPortRange = None
        self.RuleId = None
        self.Protocol = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.SourceCidr = params.get("SourceCidr")
        self.AliasName = params.get("AliasName")
        self.DestPortRange = params.get("DestPortRange")
        self.RuleId = params.get("RuleId")
        self.Protocol = params.get("Protocol")
        self.PolicyId = params.get("PolicyId")


class SetAuthenticationRequest(AbstractModel):
    """SetAuthentication請求參數結構體

    """

    def __init__(self):
        """
        :param ListenerId: 監聽器ID。
        :type ListenerId: str
        :param Domain: 需要進行高級配置的域名，該域名爲監聽器下的轉發規則的域名。
        :type Domain: str
        :param BasicAuth: 基礎認證開關，其中：
0，關閉基礎認證；
1，開啓基礎認證。
預設爲0。
        :type BasicAuth: int
        :param GaapAuth: 通道認證開關，用於源站對Gaap的認證，其中：
0，關閉通道認證；
1，開啓通道認證。
預設爲0。
        :type GaapAuth: int
        :param RealServerAuth: 源站認證開關，用於Gaap對服務器的認證，其中：
0，關閉源站認證；
1，開啓源站認證。
預設爲0。
        :type RealServerAuth: int
        :param BasicAuthConfId: 基礎認證配置ID，從證書管理頁獲取。
        :type BasicAuthConfId: str
        :param GaapCertificateId: 通道SSL證書ID，從證書管理頁獲取。
        :type GaapCertificateId: str
        :param RealServerCertificateId: 源站CA證書ID，從證書管理頁獲取。源站認證時，填寫該參數或RealServerCertificateId參數
        :type RealServerCertificateId: str
        :param RealServerCertificateDomain: 源站證書域名。
        :type RealServerCertificateDomain: str
        :param PolyRealServerCertificateIds: 多源站CA證書ID，從證書管理頁獲取。源站認證時，填寫該參數或RealServerCertificateId參數
        :type PolyRealServerCertificateIds: list of str
        """
        self.ListenerId = None
        self.Domain = None
        self.BasicAuth = None
        self.GaapAuth = None
        self.RealServerAuth = None
        self.BasicAuthConfId = None
        self.GaapCertificateId = None
        self.RealServerCertificateId = None
        self.RealServerCertificateDomain = None
        self.PolyRealServerCertificateIds = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.BasicAuth = params.get("BasicAuth")
        self.GaapAuth = params.get("GaapAuth")
        self.RealServerAuth = params.get("RealServerAuth")
        self.BasicAuthConfId = params.get("BasicAuthConfId")
        self.GaapCertificateId = params.get("GaapCertificateId")
        self.RealServerCertificateId = params.get("RealServerCertificateId")
        self.RealServerCertificateDomain = params.get("RealServerCertificateDomain")
        self.PolyRealServerCertificateIds = params.get("PolyRealServerCertificateIds")


class SetAuthenticationResponse(AbstractModel):
    """SetAuthentication返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StatisticsDataInfo(AbstractModel):
    """統計數據訊息

    """

    def __init__(self):
        """
        :param Time: 對應的時間點
        :type Time: int
        :param Data: 統計數據值
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: float
        """
        self.Time = None
        self.Data = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Data = params.get("Data")


class TCPListener(AbstractModel):
    """TCP類型監聽器訊息

    """

    def __init__(self):
        """
        :param ListenerId: 監聽器ID
        :type ListenerId: str
        :param ListenerName: 監聽器名稱
        :type ListenerName: str
        :param Port: 監聽器端口
        :type Port: int
        :param RealServerPort: 監聽器轉發源站端口，僅對版本爲1.0的通道有效
注意：此欄位可能返回 null，表示取不到有效值。
        :type RealServerPort: int
        :param RealServerType: 監聽器綁定源站類型
        :type RealServerType: str
        :param Protocol: 監聽器協議， TCP
        :type Protocol: str
        :param ListenerStatus: 監聽器狀态，其中：
0表示運作中；
1表示創建中；
2表示銷毀中；
3表示源站調整中；
4表示配置變更中。
        :type ListenerStatus: int
        :param Scheduler: 監聽器源站訪問策略，其中：
rr表示輪詢；
wrr表示加權輪詢；
lc表示最小連接數。
        :type Scheduler: str
        :param ConnectTimeout: 源站健康檢查響應超時時間，單位：秒
        :type ConnectTimeout: int
        :param DelayLoop: 源站健康檢查時間間隔，單位：秒
        :type DelayLoop: int
        :param HealthCheck: 監聽器是否開啓健康檢查，其中：
0表示關閉；
1表示開啓
        :type HealthCheck: int
        :param BindStatus: 監聽器綁定的源站狀态， 其中：
0表示異常；
1表示正常。
        :type BindStatus: int
        :param RealServerSet: 監聽器綁定的源站訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type RealServerSet: list of BindRealServer
        :param CreateTime: 監聽器創建時間，Unix時間戳
        :type CreateTime: int
        """
        self.ListenerId = None
        self.ListenerName = None
        self.Port = None
        self.RealServerPort = None
        self.RealServerType = None
        self.Protocol = None
        self.ListenerStatus = None
        self.Scheduler = None
        self.ConnectTimeout = None
        self.DelayLoop = None
        self.HealthCheck = None
        self.BindStatus = None
        self.RealServerSet = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Port = params.get("Port")
        self.RealServerPort = params.get("RealServerPort")
        self.RealServerType = params.get("RealServerType")
        self.Protocol = params.get("Protocol")
        self.ListenerStatus = params.get("ListenerStatus")
        self.Scheduler = params.get("Scheduler")
        self.ConnectTimeout = params.get("ConnectTimeout")
        self.DelayLoop = params.get("DelayLoop")
        self.HealthCheck = params.get("HealthCheck")
        self.BindStatus = params.get("BindStatus")
        if params.get("RealServerSet") is not None:
            self.RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = BindRealServer()
                obj._deserialize(item)
                self.RealServerSet.append(obj)
        self.CreateTime = params.get("CreateTime")


class TagPair(AbstractModel):
    """標簽鍵值對

    """

    def __init__(self):
        """
        :param TagKey: 標簽鍵
        :type TagKey: str
        :param TagValue: 標簽值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class TagResourceInfo(AbstractModel):
    """標簽對應資源訊息

    """

    def __init__(self):
        """
        :param ResourceType: 資源類型，其中：
Proxy表示通道，
ProxyGroup表示通道組，
RealServer表示源站
        :type ResourceType: str
        :param ResourceId: 資源ID
        :type ResourceId: str
        """
        self.ResourceType = None
        self.ResourceId = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.ResourceId = params.get("ResourceId")


class UDPListener(AbstractModel):
    """UDP類型監聽器訊息

    """

    def __init__(self):
        """
        :param ListenerId: 監聽器ID
        :type ListenerId: str
        :param ListenerName: 監聽器名稱
        :type ListenerName: str
        :param Port: 監聽器端口
        :type Port: int
        :param RealServerPort: 監聽器轉發源站端口，僅V1版本通道或通道組監聽器有效
注意：此欄位可能返回 null，表示取不到有效值。
        :type RealServerPort: int
        :param RealServerType: 監聽器綁定源站類型
        :type RealServerType: str
        :param Protocol: 監聽器協議， UDP
        :type Protocol: str
        :param ListenerStatus: 監聽器狀态，其中：
0表示運作中；
1表示創建中；
2表示銷毀中；
3表示源站調整中；
4表示配置變更中。
        :type ListenerStatus: int
        :param Scheduler: 監聽器源站訪問策略
        :type Scheduler: str
        :param BindStatus: 監聽器綁定源站狀态， 0表示正常，1表示IP異常，2表示域名解析異常
        :type BindStatus: int
        :param RealServerSet: 監聽器綁定的源站訊息
        :type RealServerSet: list of BindRealServer
        :param CreateTime: 監聽器創建時間，Unix時間戳
        :type CreateTime: int
        """
        self.ListenerId = None
        self.ListenerName = None
        self.Port = None
        self.RealServerPort = None
        self.RealServerType = None
        self.Protocol = None
        self.ListenerStatus = None
        self.Scheduler = None
        self.BindStatus = None
        self.RealServerSet = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Port = params.get("Port")
        self.RealServerPort = params.get("RealServerPort")
        self.RealServerType = params.get("RealServerType")
        self.Protocol = params.get("Protocol")
        self.ListenerStatus = params.get("ListenerStatus")
        self.Scheduler = params.get("Scheduler")
        self.BindStatus = params.get("BindStatus")
        if params.get("RealServerSet") is not None:
            self.RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = BindRealServer()
                obj._deserialize(item)
                self.RealServerSet.append(obj)
        self.CreateTime = params.get("CreateTime")