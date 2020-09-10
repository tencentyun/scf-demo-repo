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


class BaradData(AbstractModel):
    """巴拉多返回的數據

    """

    def __init__(self):
        """
        :param MetricName: 指标名（connum表示TCP活躍連接數；
new_conn表示新建TCP連接數；
inactive_conn表示非活躍連接數;
intraffic表示入流量；
outtraffic表示出流量；
alltraffic表示出流量和入流量之和；
inpkg表示入包速率；
outpkg表示出包速率；）
        :type MetricName: str
        :param Data: 值數組
        :type Data: list of float
        :param Count: 值數組的大小
        :type Count: int
        """
        self.MetricName = None
        self.Data = None
        self.Count = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        self.Data = params.get("Data")
        self.Count = params.get("Count")


class BoundIpInfo(AbstractModel):
    """高防包綁定IP對象

    """

    def __init__(self):
        """
        :param Ip: IP
        :type Ip: str
        :param BizType: 綁定的産品分類，取值[public（CVM産品），bm（黑石産品），eni（彈性網卡），vpngw（VPN閘道）， natgw（NAT閘道），waf（Web應用安全産品），fpc（金融産品），gaap（GAAP産品）, other(托管IP)]
        :type BizType: str
        :param DeviceType: 産品分類下的子類型，取值[cvm（CVM），lb（負載均衡器），eni（彈性網卡），vpngw（VPN），natgw（NAT），waf（WAF），fpc（金融），gaap（GAAP），other（托管IP），eip（黑石彈性IP）]
        :type DeviceType: str
        :param InstanceId: IP所屬的資源實例ID，當綁定新IP時必須填寫此欄位；例如是彈性網卡的IP，則InstanceId填寫彈性網卡的ID(eni-*); 如果綁定的是托管IP沒有對應的資源實例ID，請填寫"none";
        :type InstanceId: str
        """
        self.Ip = None
        self.BizType = None
        self.DeviceType = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.BizType = params.get("BizType")
        self.DeviceType = params.get("DeviceType")
        self.InstanceId = params.get("InstanceId")


class CCAlarmThreshold(AbstractModel):
    """CC告警阈值

    """

    def __init__(self):
        """
        :param AlarmThreshold: CC告警阈值
        :type AlarmThreshold: int
        """
        self.AlarmThreshold = None


    def _deserialize(self, params):
        self.AlarmThreshold = params.get("AlarmThreshold")


class CCEventRecord(AbstractModel):
    """CC攻擊事件記錄

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版；basic表示DDoS基礎防護）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param Vip: 資源的IP
        :type Vip: str
        :param StartTime: 攻擊開始時間
        :type StartTime: str
        :param EndTime: 攻擊結束時間
        :type EndTime: str
        :param ReqQps: 總請求QPS峰值
        :type ReqQps: int
        :param DropQps: 攻擊QPS峰值
        :type DropQps: int
        :param AttackStatus: 攻擊狀态，取值[0（攻擊中）, 1（攻擊結束）]
        :type AttackStatus: int
        :param ResourceName: 資源名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResourceName: str
        :param DomainList: 域名清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type DomainList: str
        :param UriList: uri清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type UriList: str
        :param AttackipList: 攻擊源清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type AttackipList: str
        """
        self.Business = None
        self.Id = None
        self.Vip = None
        self.StartTime = None
        self.EndTime = None
        self.ReqQps = None
        self.DropQps = None
        self.AttackStatus = None
        self.ResourceName = None
        self.DomainList = None
        self.UriList = None
        self.AttackipList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Vip = params.get("Vip")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ReqQps = params.get("ReqQps")
        self.DropQps = params.get("DropQps")
        self.AttackStatus = params.get("AttackStatus")
        self.ResourceName = params.get("ResourceName")
        self.DomainList = params.get("DomainList")
        self.UriList = params.get("UriList")
        self.AttackipList = params.get("AttackipList")


class CCFrequencyRule(AbstractModel):
    """CC的訪問頻率控制規則

    """

    def __init__(self):
        """
        :param CCFrequencyRuleId: CC的訪問頻率控制規則ID
        :type CCFrequencyRuleId: str
        :param Uri: URI字串，必須以/開頭，例如/abc/a.php，長度不超過31；當URI=/時，比對模式只能選擇前綴比對；
        :type Uri: str
        :param UserAgent: User-Agent字串，長度不超過80
        :type UserAgent: str
        :param Cookie: Cookie字串，長度不超過40
        :type Cookie: str
        :param Mode: 比對規則，取值["include"(前綴比對)，"equal"(完全比對)]
        :type Mode: str
        :param Period: 統計週期，單位秒，取值[10, 30, 60]
        :type Period: int
        :param ReqNumber: 訪問次數，取值[1-10000]
        :type ReqNumber: int
        :param Act: 執行動作，取值["alg"（人機識别）, "drop"（攔截）]
        :type Act: str
        :param ExeDuration: 執行時間，單位秒，取值[1-900]
        :type ExeDuration: int
        """
        self.CCFrequencyRuleId = None
        self.Uri = None
        self.UserAgent = None
        self.Cookie = None
        self.Mode = None
        self.Period = None
        self.ReqNumber = None
        self.Act = None
        self.ExeDuration = None


    def _deserialize(self, params):
        self.CCFrequencyRuleId = params.get("CCFrequencyRuleId")
        self.Uri = params.get("Uri")
        self.UserAgent = params.get("UserAgent")
        self.Cookie = params.get("Cookie")
        self.Mode = params.get("Mode")
        self.Period = params.get("Period")
        self.ReqNumber = params.get("ReqNumber")
        self.Act = params.get("Act")
        self.ExeDuration = params.get("ExeDuration")


class CCPolicy(AbstractModel):
    """cc自定義規則

    """

    def __init__(self):
        """
        :param Name: 策略名稱
        :type Name: str
        :param Smode: 比對模式，取值[matching(比對模式), speedlimit(限速模式)]
        :type Smode: str
        :param SetId: 策略id
        :type SetId: str
        :param Frequency: 每分鍾限制的次數
        :type Frequency: int
        :param ExeMode: 執行策略模式，攔截或者驗證碼，取值[alg（驗證碼）, drop（攔截）]
        :type ExeMode: str
        :param Switch: 生效開關
        :type Switch: int
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param RuleList: 規則清單
        :type RuleList: list of CCRule
        :param IpList: IP清單，如果不填時，請傳空數組但不能爲null；
        :type IpList: list of str
        :param Protocol: cc防護類型，取值[http，https]
        :type Protocol: str
        :param RuleId: 可選欄位，表示HTTPS的CC防護域名對應的轉發規則ID;
        :type RuleId: str
        :param Domain: HTTPS的CC防護域名
        :type Domain: str
        """
        self.Name = None
        self.Smode = None
        self.SetId = None
        self.Frequency = None
        self.ExeMode = None
        self.Switch = None
        self.CreateTime = None
        self.RuleList = None
        self.IpList = None
        self.Protocol = None
        self.RuleId = None
        self.Domain = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Smode = params.get("Smode")
        self.SetId = params.get("SetId")
        self.Frequency = params.get("Frequency")
        self.ExeMode = params.get("ExeMode")
        self.Switch = params.get("Switch")
        self.CreateTime = params.get("CreateTime")
        if params.get("RuleList") is not None:
            self.RuleList = []
            for item in params.get("RuleList"):
                obj = CCRule()
                obj._deserialize(item)
                self.RuleList.append(obj)
        self.IpList = params.get("IpList")
        self.Protocol = params.get("Protocol")
        self.RuleId = params.get("RuleId")
        self.Domain = params.get("Domain")


class CCRule(AbstractModel):
    """cc自定義策略配置的規則

    """

    def __init__(self):
        """
        :param Skey: 規則的key, 可以爲host、cgi、ua、referer
        :type Skey: str
        :param Operator: 規則的條件，可以爲include、not_include、equal
        :type Operator: str
        :param Value: 規則的值，長度小於31位元
        :type Value: str
        """
        self.Skey = None
        self.Operator = None
        self.Value = None


    def _deserialize(self, params):
        self.Skey = params.get("Skey")
        self.Operator = params.get("Operator")
        self.Value = params.get("Value")


class CCRuleConfig(AbstractModel):
    """7層CC自定義規則

    """

    def __init__(self):
        """
        :param Period: 統計週期，單位秒，取值[10, 30, 60]
        :type Period: int
        :param ReqNumber: 訪問次數，取值[1-10000]
        :type ReqNumber: int
        :param Action: 執行動作，取值["alg"（人機識别）, "drop"（攔截）]
        :type Action: str
        :param ExeDuration: 執行時間，單位秒，取值[1-900]
        :type ExeDuration: int
        """
        self.Period = None
        self.ReqNumber = None
        self.Action = None
        self.ExeDuration = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.ReqNumber = params.get("ReqNumber")
        self.Action = params.get("Action")
        self.ExeDuration = params.get("ExeDuration")


class CreateBasicDDoSAlarmThresholdRequest(AbstractModel):
    """CreateBasicDDoSAlarmThreshold請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（basic表示DDoS基礎防護）
        :type Business: str
        :param Method: =get表示讀取告警阈值；=set表示設置告警阈值；
        :type Method: str
        :param AlarmType: 可選，告警阈值類型，1-入流量，2-清洗流量；當Method爲set時必須填寫；
        :type AlarmType: int
        :param AlarmThreshold: 可選，告警阈值，當Method爲set時必須填寫；當設置阈值爲0時表示清除告警阈值配置；
        :type AlarmThreshold: int
        """
        self.Business = None
        self.Method = None
        self.AlarmType = None
        self.AlarmThreshold = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Method = params.get("Method")
        self.AlarmType = params.get("AlarmType")
        self.AlarmThreshold = params.get("AlarmThreshold")


class CreateBasicDDoSAlarmThresholdResponse(AbstractModel):
    """CreateBasicDDoSAlarmThreshold返回參數結構體

    """

    def __init__(self):
        """
        :param AlarmThreshold: 當存在告警阈值配置時，返回告警阈值大于0，當不存在告警配置時，返回告警阈值爲0；
        :type AlarmThreshold: int
        :param AlarmType: 告警阈值類型，1-入流量，2-清洗流量；當AlarmThreshold大于0時有效；
        :type AlarmType: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AlarmThreshold = None
        self.AlarmType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AlarmThreshold = params.get("AlarmThreshold")
        self.AlarmType = params.get("AlarmType")
        self.RequestId = params.get("RequestId")


class CreateBoundIPRequest(AbstractModel):
    """CreateBoundIP請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgp表示獨享包；bgp-multip表示共享包）
        :type Business: str
        :param Id: 資源實例ID
        :type Id: str
        :param BoundDevList: 綁定到資源實例的IP數組，當資源實例爲高防包(獨享包)時，數組只允許填1個IP；當沒有要綁定的IP時可以爲空數組；但是BoundDevList和UnBoundDevList至少有一個不爲空；
        :type BoundDevList: list of BoundIpInfo
        :param UnBoundDevList: 與資源實例解綁的IP數組，當資源實例爲高防包(獨享包)時，數組只允許填1個IP；當沒有要解綁的IP時可以爲空數組；但是BoundDevList和UnBoundDevList至少有一個不爲空；
        :type UnBoundDevList: list of BoundIpInfo
        :param CopyPolicy: 已棄用，不填
        :type CopyPolicy: str
        """
        self.Business = None
        self.Id = None
        self.BoundDevList = None
        self.UnBoundDevList = None
        self.CopyPolicy = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("BoundDevList") is not None:
            self.BoundDevList = []
            for item in params.get("BoundDevList"):
                obj = BoundIpInfo()
                obj._deserialize(item)
                self.BoundDevList.append(obj)
        if params.get("UnBoundDevList") is not None:
            self.UnBoundDevList = []
            for item in params.get("UnBoundDevList"):
                obj = BoundIpInfo()
                obj._deserialize(item)
                self.UnBoundDevList.append(obj)
        self.CopyPolicy = params.get("CopyPolicy")


class CreateBoundIPResponse(AbstractModel):
    """CreateBoundIP返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateCCFrequencyRulesRequest(AbstractModel):
    """CreateCCFrequencyRules請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param RuleId: 7層轉發規則ID（通過獲取7層轉發規則介面可以獲取規則ID）
        :type RuleId: str
        :param Mode: 比對規則，取值["include"(前綴比對)，"equal"(完全比對)]
        :type Mode: str
        :param Period: 統計週期，單位秒，取值[10, 30, 60]
        :type Period: int
        :param ReqNumber: 訪問次數，取值[1-10000]
        :type ReqNumber: int
        :param Act: 執行動作，取值["alg"（人機識别）, "drop"（攔截）]
        :type Act: str
        :param ExeDuration: 執行時間，單位秒，取值[1-900]
        :type ExeDuration: int
        :param Uri: URI字串，必須以/開頭，例如/abc/a.php，長度不超過31；當URI=/時，比對模式只能選擇前綴比對；
        :type Uri: str
        :param UserAgent: User-Agent字串，長度不超過80
        :type UserAgent: str
        :param Cookie: Cookie字串，長度不超過40
        :type Cookie: str
        """
        self.Business = None
        self.Id = None
        self.RuleId = None
        self.Mode = None
        self.Period = None
        self.ReqNumber = None
        self.Act = None
        self.ExeDuration = None
        self.Uri = None
        self.UserAgent = None
        self.Cookie = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleId = params.get("RuleId")
        self.Mode = params.get("Mode")
        self.Period = params.get("Period")
        self.ReqNumber = params.get("ReqNumber")
        self.Act = params.get("Act")
        self.ExeDuration = params.get("ExeDuration")
        self.Uri = params.get("Uri")
        self.UserAgent = params.get("UserAgent")
        self.Cookie = params.get("Cookie")


class CreateCCFrequencyRulesResponse(AbstractModel):
    """CreateCCFrequencyRules返回參數結構體

    """

    def __init__(self):
        """
        :param CCFrequencyRuleId: CC防護的訪問頻率控制規則ID
        :type CCFrequencyRuleId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CCFrequencyRuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CCFrequencyRuleId = params.get("CCFrequencyRuleId")
        self.RequestId = params.get("RequestId")


class CreateCCSelfDefinePolicyRequest(AbstractModel):
    """CreateCCSelfDefinePolicy請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param Policy: CC策略描述
        :type Policy: :class:`tencentcloud.dayu.v20180709.models.CCPolicy`
        """
        self.Business = None
        self.Id = None
        self.Policy = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Policy") is not None:
            self.Policy = CCPolicy()
            self.Policy._deserialize(params.get("Policy"))


class CreateCCSelfDefinePolicyResponse(AbstractModel):
    """CreateCCSelfDefinePolicy返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateDDoSPolicyCaseRequest(AbstractModel):
    """CreateDDoSPolicyCase請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param CaseName: 策略場景名，字串長度小於64
        :type CaseName: str
        :param PlatformTypes: 開發平台，取值[PC（PC用戶端）， MOBILE（移動端）， TV（電視端）， SERVER（主機）]
        :type PlatformTypes: list of str
        :param AppType: 細分品類，取值[WEB（網站）， GAME（遊戲）， APP（應用）， OTHER（其他）]
        :type AppType: str
        :param AppProtocols: 應用協議，取值[tcp（TCP協議），udp（UDP協議），icmp（ICMP協議），all（其他協議）]
        :type AppProtocols: list of str
        :param TcpSportStart: TCP業務起始端口，取值(0, 65535]
        :type TcpSportStart: str
        :param TcpSportEnd: TCP業務結束端口，取值(0, 65535]，必須大于等于TCP業務起始端口
        :type TcpSportEnd: str
        :param UdpSportStart: UDP業務起始端口，取值範圍(0, 65535]
        :type UdpSportStart: str
        :param UdpSportEnd: UDP業務結束端口，取值範圍(0, 65535)，必須大于等于UDP業務起始端口
        :type UdpSportEnd: str
        :param HasAbroad: 是否有海外客戶，取值[no（沒有）, yes（有）]
        :type HasAbroad: str
        :param HasInitiateTcp: 是否會主動對外發起TCP請求，取值[no（不會）, yes（會）]
        :type HasInitiateTcp: str
        :param HasInitiateUdp: 是否會主動對外發起UDP業務請求，取值[no（不會）, yes（會）]
        :type HasInitiateUdp: str
        :param PeerTcpPort: 主動發起TCP請求的端口，取值範圍(0, 65535]
        :type PeerTcpPort: str
        :param PeerUdpPort: 主動發起UDP請求的端口，取值範圍(0, 65535]
        :type PeerUdpPort: str
        :param TcpFootprint: TCP載荷的固定特征碼，字串長度小於512
        :type TcpFootprint: str
        :param UdpFootprint: UDP載荷的固定特征碼，字串長度小於512
        :type UdpFootprint: str
        :param WebApiUrl: Web業務的API的URL
        :type WebApiUrl: list of str
        :param MinTcpPackageLen: TCP業務報文長度最小值，取值範圍(0, 1500)
        :type MinTcpPackageLen: str
        :param MaxTcpPackageLen: TCP業務報文長度最大值，取值範圍(0, 1500)，必須大于等于TCP業務報文長度最小值
        :type MaxTcpPackageLen: str
        :param MinUdpPackageLen: UDP業務報文長度最小值，取值範圍(0, 1500)
        :type MinUdpPackageLen: str
        :param MaxUdpPackageLen: UDP業務報文長度最大值，取值範圍(0, 1500)，必須大于等于UDP業務報文長度最小值
        :type MaxUdpPackageLen: str
        :param HasVPN: 是否有VPN業務，取值[no（沒有）, yes（有）]
        :type HasVPN: str
        :param TcpPortList: TCP業務端口清單，同時支援單個端口和端口段，字串格式，例如：80,443,700-800,53,1000-3000
        :type TcpPortList: str
        :param UdpPortList: UDP業務端口清單，同時支援單個端口和端口段，字串格式，例如：80,443,700-800,53,1000-3000
        :type UdpPortList: str
        """
        self.Business = None
        self.CaseName = None
        self.PlatformTypes = None
        self.AppType = None
        self.AppProtocols = None
        self.TcpSportStart = None
        self.TcpSportEnd = None
        self.UdpSportStart = None
        self.UdpSportEnd = None
        self.HasAbroad = None
        self.HasInitiateTcp = None
        self.HasInitiateUdp = None
        self.PeerTcpPort = None
        self.PeerUdpPort = None
        self.TcpFootprint = None
        self.UdpFootprint = None
        self.WebApiUrl = None
        self.MinTcpPackageLen = None
        self.MaxTcpPackageLen = None
        self.MinUdpPackageLen = None
        self.MaxUdpPackageLen = None
        self.HasVPN = None
        self.TcpPortList = None
        self.UdpPortList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.CaseName = params.get("CaseName")
        self.PlatformTypes = params.get("PlatformTypes")
        self.AppType = params.get("AppType")
        self.AppProtocols = params.get("AppProtocols")
        self.TcpSportStart = params.get("TcpSportStart")
        self.TcpSportEnd = params.get("TcpSportEnd")
        self.UdpSportStart = params.get("UdpSportStart")
        self.UdpSportEnd = params.get("UdpSportEnd")
        self.HasAbroad = params.get("HasAbroad")
        self.HasInitiateTcp = params.get("HasInitiateTcp")
        self.HasInitiateUdp = params.get("HasInitiateUdp")
        self.PeerTcpPort = params.get("PeerTcpPort")
        self.PeerUdpPort = params.get("PeerUdpPort")
        self.TcpFootprint = params.get("TcpFootprint")
        self.UdpFootprint = params.get("UdpFootprint")
        self.WebApiUrl = params.get("WebApiUrl")
        self.MinTcpPackageLen = params.get("MinTcpPackageLen")
        self.MaxTcpPackageLen = params.get("MaxTcpPackageLen")
        self.MinUdpPackageLen = params.get("MinUdpPackageLen")
        self.MaxUdpPackageLen = params.get("MaxUdpPackageLen")
        self.HasVPN = params.get("HasVPN")
        self.TcpPortList = params.get("TcpPortList")
        self.UdpPortList = params.get("UdpPortList")


class CreateDDoSPolicyCaseResponse(AbstractModel):
    """CreateDDoSPolicyCase返回參數結構體

    """

    def __init__(self):
        """
        :param SceneId: 策略場景ID
        :type SceneId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SceneId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SceneId = params.get("SceneId")
        self.RequestId = params.get("RequestId")


class CreateDDoSPolicyRequest(AbstractModel):
    """CreateDDoSPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param DropOptions: 協議禁用，必須填寫且數組長度必須爲1
        :type DropOptions: list of DDoSPolicyDropOption
        :param Name: 策略名稱
        :type Name: str
        :param PortLimits: 端口禁用，當沒有禁用端口時填空數組
        :type PortLimits: list of DDoSPolicyPortLimit
        :param IpAllowDenys: IP黑白名單，當沒有IP黑白名單時填空數組
        :type IpAllowDenys: list of IpBlackWhite
        :param PacketFilters: 報文過濾，當沒有報文過濾時填空數組
        :type PacketFilters: list of DDoSPolicyPacketFilter
        :param WaterPrint: 浮水印策略參數，當沒有啓用水印功能時填空數組，最多只能傳一條水印策略（即數組大小不超過1）
        :type WaterPrint: list of WaterPrintPolicy
        """
        self.Business = None
        self.DropOptions = None
        self.Name = None
        self.PortLimits = None
        self.IpAllowDenys = None
        self.PacketFilters = None
        self.WaterPrint = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        if params.get("DropOptions") is not None:
            self.DropOptions = []
            for item in params.get("DropOptions"):
                obj = DDoSPolicyDropOption()
                obj._deserialize(item)
                self.DropOptions.append(obj)
        self.Name = params.get("Name")
        if params.get("PortLimits") is not None:
            self.PortLimits = []
            for item in params.get("PortLimits"):
                obj = DDoSPolicyPortLimit()
                obj._deserialize(item)
                self.PortLimits.append(obj)
        if params.get("IpAllowDenys") is not None:
            self.IpAllowDenys = []
            for item in params.get("IpAllowDenys"):
                obj = IpBlackWhite()
                obj._deserialize(item)
                self.IpAllowDenys.append(obj)
        if params.get("PacketFilters") is not None:
            self.PacketFilters = []
            for item in params.get("PacketFilters"):
                obj = DDoSPolicyPacketFilter()
                obj._deserialize(item)
                self.PacketFilters.append(obj)
        if params.get("WaterPrint") is not None:
            self.WaterPrint = []
            for item in params.get("WaterPrint"):
                obj = WaterPrintPolicy()
                obj._deserialize(item)
                self.WaterPrint.append(obj)


class CreateDDoSPolicyResponse(AbstractModel):
    """CreateDDoSPolicy返回參數結構體

    """

    def __init__(self):
        """
        :param PolicyId: 策略ID
        :type PolicyId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.RequestId = params.get("RequestId")


class CreateInstanceNameRequest(AbstractModel):
    """CreateInstanceName請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param Name: 資源實例名稱，長度不超過32個字元
        :type Name: str
        """
        self.Business = None
        self.Id = None
        self.Name = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Name = params.get("Name")


class CreateInstanceNameResponse(AbstractModel):
    """CreateInstanceName返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateL4HealthConfigRequest(AbstractModel):
    """CreateL4HealthConfig請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param HealthConfig: 四層健康檢查配置數組
        :type HealthConfig: list of L4HealthConfig
        """
        self.Business = None
        self.Id = None
        self.HealthConfig = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("HealthConfig") is not None:
            self.HealthConfig = []
            for item in params.get("HealthConfig"):
                obj = L4HealthConfig()
                obj._deserialize(item)
                self.HealthConfig.append(obj)


class CreateL4HealthConfigResponse(AbstractModel):
    """CreateL4HealthConfig返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateL4RulesRequest(AbstractModel):
    """CreateL4Rules請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param Rules: 規則清單
        :type Rules: list of L4RuleEntry
        """
        self.Business = None
        self.Id = None
        self.Rules = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = L4RuleEntry()
                obj._deserialize(item)
                self.Rules.append(obj)


class CreateL4RulesResponse(AbstractModel):
    """CreateL4Rules返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateL7CCRuleRequest(AbstractModel):
    """CreateL7CCRule請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param Method: 操作碼，取值[query(表示查詢)，add(表示添加)，del(表示删除)]
        :type Method: str
        :param RuleId: 7層轉發規則ID，例如：rule-0000001
        :type RuleId: str
        :param RuleConfig: 7層CC自定義規則參數，當操作碼爲query時，可以不用填寫；當操作碼爲add或del時，必須填寫，且數組長度只能爲1；
        :type RuleConfig: list of CCRuleConfig
        """
        self.Business = None
        self.Id = None
        self.Method = None
        self.RuleId = None
        self.RuleConfig = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Method = params.get("Method")
        self.RuleId = params.get("RuleId")
        if params.get("RuleConfig") is not None:
            self.RuleConfig = []
            for item in params.get("RuleConfig"):
                obj = CCRuleConfig()
                obj._deserialize(item)
                self.RuleConfig.append(obj)


class CreateL7CCRuleResponse(AbstractModel):
    """CreateL7CCRule返回參數結構體

    """

    def __init__(self):
        """
        :param RuleConfig: 7層CC自定義規則參數，當沒有開啓CC自定義規則時，返回空數組
        :type RuleConfig: list of CCRuleConfig
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RuleConfig = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuleConfig") is not None:
            self.RuleConfig = []
            for item in params.get("RuleConfig"):
                obj = CCRuleConfig()
                obj._deserialize(item)
                self.RuleConfig.append(obj)
        self.RequestId = params.get("RequestId")


class CreateL7HealthConfigRequest(AbstractModel):
    """CreateL7HealthConfig請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param HealthConfig: 七層健康檢查配置數組
        :type HealthConfig: list of L7HealthConfig
        """
        self.Business = None
        self.Id = None
        self.HealthConfig = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("HealthConfig") is not None:
            self.HealthConfig = []
            for item in params.get("HealthConfig"):
                obj = L7HealthConfig()
                obj._deserialize(item)
                self.HealthConfig.append(obj)


class CreateL7HealthConfigResponse(AbstractModel):
    """CreateL7HealthConfig返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateL7RuleCertRequest(AbstractModel):
    """CreateL7RuleCert請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源實例ID，比如高防IP實例的ID，高防IP專業版實例的ID
        :type Id: str
        :param RuleId: 規則ID
        :type RuleId: str
        :param CertType: 證書類型，當爲協議爲HTTPS協議時必須填，取值[2(Top Cloud 托管證書)]
        :type CertType: int
        :param SSLId: 當證書來源爲Top Cloud 托管證書時，此欄位必須填寫托管證書ID
        :type SSLId: str
        :param Cert: 當證書來源爲自有證書時，此欄位必須填寫證書内容；(因已不再支援自有證書，此欄位已棄用，請不用填寫此欄位)
        :type Cert: str
        :param PrivateKey: 當證書來源爲自有證書時，此欄位必須填寫證書金鑰；(因已不再支援自有證書，此欄位已棄用，請不用填寫此欄位)
        :type PrivateKey: str
        """
        self.Business = None
        self.Id = None
        self.RuleId = None
        self.CertType = None
        self.SSLId = None
        self.Cert = None
        self.PrivateKey = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleId = params.get("RuleId")
        self.CertType = params.get("CertType")
        self.SSLId = params.get("SSLId")
        self.Cert = params.get("Cert")
        self.PrivateKey = params.get("PrivateKey")


class CreateL7RuleCertResponse(AbstractModel):
    """CreateL7RuleCert返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateL7RulesRequest(AbstractModel):
    """CreateL7Rules請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param Rules: 規則清單
        :type Rules: list of L7RuleEntry
        """
        self.Business = None
        self.Id = None
        self.Rules = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = L7RuleEntry()
                obj._deserialize(item)
                self.Rules.append(obj)


class CreateL7RulesResponse(AbstractModel):
    """CreateL7Rules返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateL7RulesUploadRequest(AbstractModel):
    """CreateL7RulesUpload請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param Rules: 規則清單
        :type Rules: list of L7RuleEntry
        """
        self.Business = None
        self.Id = None
        self.Rules = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = L7RuleEntry()
                obj._deserialize(item)
                self.Rules.append(obj)


class CreateL7RulesUploadResponse(AbstractModel):
    """CreateL7RulesUpload返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateNetReturnRequest(AbstractModel):
    """CreateNetReturn請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（net表示高防IP專業版）
        :type Business: str
        :param Id: 資源實例ID
        :type Id: str
        """
        self.Business = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")


class CreateNetReturnResponse(AbstractModel):
    """CreateNetReturn返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateNewL4RulesRequest(AbstractModel):
    """CreateNewL4Rules請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 高防産品代号：bgpip
        :type Business: str
        :param IdList: 添加規則資源清單
        :type IdList: list of str
        :param VipList: 添加規則IP清單
        :type VipList: list of str
        :param Rules: 規則清單
        :type Rules: list of L4RuleEntry
        """
        self.Business = None
        self.IdList = None
        self.VipList = None
        self.Rules = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.IdList = params.get("IdList")
        self.VipList = params.get("VipList")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = L4RuleEntry()
                obj._deserialize(item)
                self.Rules.append(obj)


class CreateNewL4RulesResponse(AbstractModel):
    """CreateNewL4Rules返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateNewL7RulesRequest(AbstractModel):
    """CreateNewL7Rules請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP）
        :type Business: str
        :param IdList: 資源ID清單
        :type IdList: list of str
        :param VipList: 資源IP清單
        :type VipList: list of str
        :param Rules: 規則清單
        :type Rules: list of L7RuleEntry
        """
        self.Business = None
        self.IdList = None
        self.VipList = None
        self.Rules = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.IdList = params.get("IdList")
        self.VipList = params.get("VipList")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = L7RuleEntry()
                obj._deserialize(item)
                self.Rules.append(obj)


class CreateNewL7RulesResponse(AbstractModel):
    """CreateNewL7Rules返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateUnblockIpRequest(AbstractModel):
    """CreateUnblockIp請求參數結構體

    """

    def __init__(self):
        """
        :param Ip: IP
        :type Ip: str
        :param ActionType: 解封類型（user：自助解封；auto：自動解封； update：升級解封；bind：綁定高防包解封）
        :type ActionType: str
        """
        self.Ip = None
        self.ActionType = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.ActionType = params.get("ActionType")


class CreateUnblockIpResponse(AbstractModel):
    """CreateUnblockIp返回參數結構體

    """

    def __init__(self):
        """
        :param Ip: IP
        :type Ip: str
        :param ActionType: 解封類型（user：自助解封；auto：自動解封； update：升級解封；bind：綁定高防包解封）
        :type ActionType: str
        :param UnblockTime: 解封時間（預計解封時間）
        :type UnblockTime: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Ip = None
        self.ActionType = None
        self.UnblockTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.ActionType = params.get("ActionType")
        self.UnblockTime = params.get("UnblockTime")
        self.RequestId = params.get("RequestId")


class DDoSAlarmThreshold(AbstractModel):
    """DDoS告警阈值

    """

    def __init__(self):
        """
        :param AlarmType: 告警阈值類型，1-入流量，2-清洗流量
        :type AlarmType: int
        :param AlarmThreshold: 告警阈值，大于0（目前排定的值）
        :type AlarmThreshold: int
        """
        self.AlarmType = None
        self.AlarmThreshold = None


    def _deserialize(self, params):
        self.AlarmType = params.get("AlarmType")
        self.AlarmThreshold = params.get("AlarmThreshold")


class DDoSAttackSourceRecord(AbstractModel):
    """攻擊源訊息

    """

    def __init__(self):
        """
        :param SrcIp: 攻擊源ip
        :type SrcIp: str
        :param Province: 省份（國内有效，不包含港澳台）
        :type Province: str
        :param Nation: 國家
        :type Nation: str
        :param PacketSum: 累計攻擊包量
        :type PacketSum: int
        :param PacketLen: 累計攻擊流量
        :type PacketLen: int
        """
        self.SrcIp = None
        self.Province = None
        self.Nation = None
        self.PacketSum = None
        self.PacketLen = None


    def _deserialize(self, params):
        self.SrcIp = params.get("SrcIp")
        self.Province = params.get("Province")
        self.Nation = params.get("Nation")
        self.PacketSum = params.get("PacketSum")
        self.PacketLen = params.get("PacketLen")


class DDoSEventRecord(AbstractModel):
    """DDoS攻擊事件記錄

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版；basic表示DDoS基礎防護）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param Vip: 資源的IP
        :type Vip: str
        :param StartTime: 攻擊開始時間
        :type StartTime: str
        :param EndTime: 攻擊結束時間
        :type EndTime: str
        :param Mbps: 攻擊最大頻寬
        :type Mbps: int
        :param Pps: 攻擊最大包速率
        :type Pps: int
        :param AttackType: 攻擊類型
        :type AttackType: str
        :param BlockFlag: 是否被封堵，取值[1（是），0（否），2（無效值）]
        :type BlockFlag: int
        :param OverLoad: 是否超過彈性防護峰值，取值取值[yes(是)，no(否)，空字串（未知值）]
        :type OverLoad: str
        :param AttackStatus: 攻擊狀态，取值[0（攻擊中）, 1（攻擊結束）]
        :type AttackStatus: int
        :param ResourceName: 資源名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResourceName: str
        :param EventId: 攻擊事件Id
注意：此欄位可能返回 null，表示取不到有效值。
        :type EventId: str
        """
        self.Business = None
        self.Id = None
        self.Vip = None
        self.StartTime = None
        self.EndTime = None
        self.Mbps = None
        self.Pps = None
        self.AttackType = None
        self.BlockFlag = None
        self.OverLoad = None
        self.AttackStatus = None
        self.ResourceName = None
        self.EventId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Vip = params.get("Vip")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Mbps = params.get("Mbps")
        self.Pps = params.get("Pps")
        self.AttackType = params.get("AttackType")
        self.BlockFlag = params.get("BlockFlag")
        self.OverLoad = params.get("OverLoad")
        self.AttackStatus = params.get("AttackStatus")
        self.ResourceName = params.get("ResourceName")
        self.EventId = params.get("EventId")


class DDoSPolicyDropOption(AbstractModel):
    """DDoS高級策略的禁用協議選項

    """

    def __init__(self):
        """
        :param DropTcp: 禁用TCP協議，取值範圍[0,1]
        :type DropTcp: int
        :param DropUdp: 禁用UDP協議，取值範圍[0,1]
        :type DropUdp: int
        :param DropIcmp: 禁用ICMP協議，取值範圍[0,1]
        :type DropIcmp: int
        :param DropOther: 禁用其他協議，取值範圍[0,1]
        :type DropOther: int
        :param DropAbroad: 拒絕海外流量，取值範圍[0,1]
        :type DropAbroad: int
        :param CheckSyncConn: 空連接防護，取值範圍[0,1]
        :type CheckSyncConn: int
        :param SdNewLimit: 基于來源IP及目的IP的新建連接抑制，取值範圍[0,4294967295]
        :type SdNewLimit: int
        :param DstNewLimit: 基于目的IP的新建連接抑制，取值範圍[0,4294967295]
        :type DstNewLimit: int
        :param SdConnLimit: 基于來源IP及目的IP的并發連接抑制，取值範圍[0,4294967295]
        :type SdConnLimit: int
        :param DstConnLimit: 基于目的IP的并發連接抑制，取值範圍[0,4294967295]
        :type DstConnLimit: int
        :param BadConnThreshold: 基于連接抑制觸發阈值，取值範圍[0,4294967295]
        :type BadConnThreshold: int
        :param NullConnEnable: 異常連接檢測條件，空連接防護開關，，取值範圍[0,1]
        :type NullConnEnable: int
        :param ConnTimeout: 異常連接檢測條件，連接超時，，取值範圍[0,65535]
        :type ConnTimeout: int
        :param SynRate: 異常連接檢測條件，syn占比ack百分比，，取值範圍[0,100]
        :type SynRate: int
        :param SynLimit: 異常連接檢測條件，syn阈值，取值範圍[0,100]
        :type SynLimit: int
        :param DTcpMbpsLimit: tcp限速，取值範圍[0,4294967295]
        :type DTcpMbpsLimit: int
        :param DUdpMbpsLimit: udp限速，取值範圍[0,4294967295]
        :type DUdpMbpsLimit: int
        :param DIcmpMbpsLimit: icmp限速，取值範圍[0,4294967295]
        :type DIcmpMbpsLimit: int
        :param DOtherMbpsLimit: other協議限速，取值範圍[0,4294967295]
        :type DOtherMbpsLimit: int
        """
        self.DropTcp = None
        self.DropUdp = None
        self.DropIcmp = None
        self.DropOther = None
        self.DropAbroad = None
        self.CheckSyncConn = None
        self.SdNewLimit = None
        self.DstNewLimit = None
        self.SdConnLimit = None
        self.DstConnLimit = None
        self.BadConnThreshold = None
        self.NullConnEnable = None
        self.ConnTimeout = None
        self.SynRate = None
        self.SynLimit = None
        self.DTcpMbpsLimit = None
        self.DUdpMbpsLimit = None
        self.DIcmpMbpsLimit = None
        self.DOtherMbpsLimit = None


    def _deserialize(self, params):
        self.DropTcp = params.get("DropTcp")
        self.DropUdp = params.get("DropUdp")
        self.DropIcmp = params.get("DropIcmp")
        self.DropOther = params.get("DropOther")
        self.DropAbroad = params.get("DropAbroad")
        self.CheckSyncConn = params.get("CheckSyncConn")
        self.SdNewLimit = params.get("SdNewLimit")
        self.DstNewLimit = params.get("DstNewLimit")
        self.SdConnLimit = params.get("SdConnLimit")
        self.DstConnLimit = params.get("DstConnLimit")
        self.BadConnThreshold = params.get("BadConnThreshold")
        self.NullConnEnable = params.get("NullConnEnable")
        self.ConnTimeout = params.get("ConnTimeout")
        self.SynRate = params.get("SynRate")
        self.SynLimit = params.get("SynLimit")
        self.DTcpMbpsLimit = params.get("DTcpMbpsLimit")
        self.DUdpMbpsLimit = params.get("DUdpMbpsLimit")
        self.DIcmpMbpsLimit = params.get("DIcmpMbpsLimit")
        self.DOtherMbpsLimit = params.get("DOtherMbpsLimit")


class DDoSPolicyPacketFilter(AbstractModel):
    """DDoS高級策略的報文過濾項

    """

    def __init__(self):
        """
        :param Protocol: 協議，取值範圍[tcp,udp,icmp,all]
        :type Protocol: str
        :param SportStart: 開始源端口，取值範圍[0,65535]
        :type SportStart: int
        :param SportEnd: 結束源端口，取值範圍[0,65535]
        :type SportEnd: int
        :param DportStart: 開始目的端口，取值範圍[0,65535]
        :type DportStart: int
        :param DportEnd: 結束目的端口，取值範圍[0,65535]
        :type DportEnd: int
        :param PktlenMin: 最小包長，取值範圍[0,1500]
        :type PktlenMin: int
        :param PktlenMax: 最大包長，取值範圍[0,1500]
        :type PktlenMax: int
        :param MatchBegin: 是否檢測載荷，取值範圍[
begin_l3(IP頭)
begin_l4(TCP頭)
begin_l5(載荷)
no_match(不檢測)
]
        :type MatchBegin: str
        :param MatchType: 是否是正規表示式，取值範圍[sunday(表示關鍵字),pcre(表示正規表示式)]
        :type MatchType: str
        :param Str: 關鍵字或正規表示式
        :type Str: str
        :param Depth: 檢測深度，取值範圍[0,1500]
        :type Depth: int
        :param Offset: 檢測偏移量，取值範圍[0,1500]
        :type Offset: int
        :param IsNot: 是否包括，取值範圍[0(表示不包含),1(表示包含)]
        :type IsNot: int
        :param Action: 策略動作，取值範圍[drop，drop_black，drop_rst，drop_black_rst，transmit]
        :type Action: str
        """
        self.Protocol = None
        self.SportStart = None
        self.SportEnd = None
        self.DportStart = None
        self.DportEnd = None
        self.PktlenMin = None
        self.PktlenMax = None
        self.MatchBegin = None
        self.MatchType = None
        self.Str = None
        self.Depth = None
        self.Offset = None
        self.IsNot = None
        self.Action = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.SportStart = params.get("SportStart")
        self.SportEnd = params.get("SportEnd")
        self.DportStart = params.get("DportStart")
        self.DportEnd = params.get("DportEnd")
        self.PktlenMin = params.get("PktlenMin")
        self.PktlenMax = params.get("PktlenMax")
        self.MatchBegin = params.get("MatchBegin")
        self.MatchType = params.get("MatchType")
        self.Str = params.get("Str")
        self.Depth = params.get("Depth")
        self.Offset = params.get("Offset")
        self.IsNot = params.get("IsNot")
        self.Action = params.get("Action")


class DDoSPolicyPortLimit(AbstractModel):
    """DDoS高級策略的禁用端口

    """

    def __init__(self):
        """
        :param Protocol: 協議，取值範圍[tcp,udp,all]
        :type Protocol: str
        :param DPortStart: 開始目的端口，取值範圍[0,65535]
        :type DPortStart: int
        :param DPortEnd: 結束目的端口，取值範圍[0,65535]，要求大于等于開始目的端口
        :type DPortEnd: int
        :param SPortStart: 開始源端口，取值範圍[0,65535]
注意：此欄位可能返回 null，表示取不到有效值。
        :type SPortStart: int
        :param SPortEnd: 結束源端口，取值範圍[0,65535]，要求大于等于開始源端口
注意：此欄位可能返回 null，表示取不到有效值。
        :type SPortEnd: int
        :param Action: 執行動作，取值[drop(丢棄) ，transmit(轉發)]
注意：此欄位可能返回 null，表示取不到有效值。
        :type Action: str
        :param Kind: 禁用端口類型，取值[0（目的端口範圍禁用）， 1（源端口範圍禁用）， 2（目的和源端口範圍同時禁用）]
注意：此欄位可能返回 null，表示取不到有效值。
        :type Kind: int
        """
        self.Protocol = None
        self.DPortStart = None
        self.DPortEnd = None
        self.SPortStart = None
        self.SPortEnd = None
        self.Action = None
        self.Kind = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.DPortStart = params.get("DPortStart")
        self.DPortEnd = params.get("DPortEnd")
        self.SPortStart = params.get("SPortStart")
        self.SPortEnd = params.get("SPortEnd")
        self.Action = params.get("Action")
        self.Kind = params.get("Kind")


class DDosPolicy(AbstractModel):
    """DDoS高級策略

    """

    def __init__(self):
        """
        :param Resources: 策略綁定的資源
        :type Resources: list of ResourceIp
        :param DropOptions: 禁用協議
        :type DropOptions: :class:`tencentcloud.dayu.v20180709.models.DDoSPolicyDropOption`
        :param PortLimits: 禁用端口
        :type PortLimits: list of DDoSPolicyPortLimit
        :param PacketFilters: 報文過濾
        :type PacketFilters: list of DDoSPolicyPacketFilter
        :param IpBlackWhiteLists: 黑白IP名單
        :type IpBlackWhiteLists: list of IpBlackWhite
        :param PolicyId: 策略ID
        :type PolicyId: str
        :param PolicyName: 策略名稱
        :type PolicyName: str
        :param CreateTime: 策略創建時間
        :type CreateTime: str
        :param WaterPrint: 浮水印策略參數，最多只有一個，當沒有水印策略時數組爲空
        :type WaterPrint: list of WaterPrintPolicy
        :param WaterKey: 浮水印金鑰，最多只有2個，當沒有水印策略時數組爲空
        :type WaterKey: list of WaterPrintKey
        :param BoundResources: 策略綁定的資源實例
注意：此欄位可能返回 null，表示取不到有效值。
        :type BoundResources: list of str
        :param SceneId: 策略所屬的策略場景
注意：此欄位可能返回 null，表示取不到有效值。
        :type SceneId: str
        """
        self.Resources = None
        self.DropOptions = None
        self.PortLimits = None
        self.PacketFilters = None
        self.IpBlackWhiteLists = None
        self.PolicyId = None
        self.PolicyName = None
        self.CreateTime = None
        self.WaterPrint = None
        self.WaterKey = None
        self.BoundResources = None
        self.SceneId = None


    def _deserialize(self, params):
        if params.get("Resources") is not None:
            self.Resources = []
            for item in params.get("Resources"):
                obj = ResourceIp()
                obj._deserialize(item)
                self.Resources.append(obj)
        if params.get("DropOptions") is not None:
            self.DropOptions = DDoSPolicyDropOption()
            self.DropOptions._deserialize(params.get("DropOptions"))
        if params.get("PortLimits") is not None:
            self.PortLimits = []
            for item in params.get("PortLimits"):
                obj = DDoSPolicyPortLimit()
                obj._deserialize(item)
                self.PortLimits.append(obj)
        if params.get("PacketFilters") is not None:
            self.PacketFilters = []
            for item in params.get("PacketFilters"):
                obj = DDoSPolicyPacketFilter()
                obj._deserialize(item)
                self.PacketFilters.append(obj)
        if params.get("IpBlackWhiteLists") is not None:
            self.IpBlackWhiteLists = []
            for item in params.get("IpBlackWhiteLists"):
                obj = IpBlackWhite()
                obj._deserialize(item)
                self.IpBlackWhiteLists.append(obj)
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.CreateTime = params.get("CreateTime")
        if params.get("WaterPrint") is not None:
            self.WaterPrint = []
            for item in params.get("WaterPrint"):
                obj = WaterPrintPolicy()
                obj._deserialize(item)
                self.WaterPrint.append(obj)
        if params.get("WaterKey") is not None:
            self.WaterKey = []
            for item in params.get("WaterKey"):
                obj = WaterPrintKey()
                obj._deserialize(item)
                self.WaterKey.append(obj)
        self.BoundResources = params.get("BoundResources")
        self.SceneId = params.get("SceneId")


class DeleteCCFrequencyRulesRequest(AbstractModel):
    """DeleteCCFrequencyRules請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param CCFrequencyRuleId: CC防護的訪問頻率控制規則ID
        :type CCFrequencyRuleId: str
        """
        self.Business = None
        self.CCFrequencyRuleId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.CCFrequencyRuleId = params.get("CCFrequencyRuleId")


class DeleteCCFrequencyRulesResponse(AbstractModel):
    """DeleteCCFrequencyRules返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class DeleteCCSelfDefinePolicyRequest(AbstractModel):
    """DeleteCCSelfDefinePolicy請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param SetId: 策略ID
        :type SetId: str
        """
        self.Business = None
        self.Id = None
        self.SetId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.SetId = params.get("SetId")


class DeleteCCSelfDefinePolicyResponse(AbstractModel):
    """DeleteCCSelfDefinePolicy返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class DeleteDDoSPolicyCaseRequest(AbstractModel):
    """DeleteDDoSPolicyCase請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param SceneId: 策略場景ID
        :type SceneId: str
        """
        self.Business = None
        self.SceneId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.SceneId = params.get("SceneId")


class DeleteDDoSPolicyCaseResponse(AbstractModel):
    """DeleteDDoSPolicyCase返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class DeleteDDoSPolicyRequest(AbstractModel):
    """DeleteDDoSPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param PolicyId: 策略ID
        :type PolicyId: str
        """
        self.Business = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.PolicyId = params.get("PolicyId")


class DeleteDDoSPolicyResponse(AbstractModel):
    """DeleteDDoSPolicy返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class DeleteL4RulesRequest(AbstractModel):
    """DeleteL4Rules請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param RuleIdList: 規則ID清單
        :type RuleIdList: list of str
        """
        self.Business = None
        self.Id = None
        self.RuleIdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleIdList = params.get("RuleIdList")


class DeleteL4RulesResponse(AbstractModel):
    """DeleteL4Rules返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class DeleteL7RulesRequest(AbstractModel):
    """DeleteL7Rules請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param RuleIdList: 規則ID清單
        :type RuleIdList: list of str
        """
        self.Business = None
        self.Id = None
        self.RuleIdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleIdList = params.get("RuleIdList")


class DeleteL7RulesResponse(AbstractModel):
    """DeleteL7Rules返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class DeleteNewL4RulesRequest(AbstractModel):
    """DeleteNewL4Rules請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP）
        :type Business: str
        :param Rule: 删除介面結構體
        :type Rule: list of L4DelRule
        """
        self.Business = None
        self.Rule = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        if params.get("Rule") is not None:
            self.Rule = []
            for item in params.get("Rule"):
                obj = L4DelRule()
                obj._deserialize(item)
                self.Rule.append(obj)


class DeleteNewL4RulesResponse(AbstractModel):
    """DeleteNewL4Rules返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class DeleteNewL7RulesRequest(AbstractModel):
    """DeleteNewL7Rules請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP)
        :type Business: str
        :param Rule: 删除規則清單
        :type Rule: list of L4DelRule
        """
        self.Business = None
        self.Rule = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        if params.get("Rule") is not None:
            self.Rule = []
            for item in params.get("Rule"):
                obj = L4DelRule()
                obj._deserialize(item)
                self.Rule.append(obj)


class DeleteNewL7RulesResponse(AbstractModel):
    """DeleteNewL7Rules返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class DescribeActionLogRequest(AbstractModel):
    """DescribeActionLog請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 開始時間
        :type StartTime: str
        :param EndTime: 結束時間
        :type EndTime: str
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param Filter: 搜索值，只支援資源ID或用戶UIN
        :type Filter: str
        :param Limit: 一頁條數，填0表示不分頁
        :type Limit: int
        :param Offset: 頁起始偏移，取值爲(頁碼-1)*一頁條數
        :type Offset: int
        """
        self.StartTime = None
        self.EndTime = None
        self.Business = None
        self.Filter = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Business = params.get("Business")
        self.Filter = params.get("Filter")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeActionLogResponse(AbstractModel):
    """DescribeActionLog返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 總記錄數
        :type TotalCount: int
        :param Data: 記錄數組
        :type Data: list of KeyValueRecord
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBGPIPL7RuleMaxCntRequest(AbstractModel):
    """DescribeBGPIPL7RuleMaxCnt請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP）
        :type Business: str
        :param Id: 資源實例ID
        :type Id: str
        """
        self.Business = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")


class DescribeBGPIPL7RuleMaxCntResponse(AbstractModel):
    """DescribeBGPIPL7RuleMaxCnt返回參數結構體

    """

    def __init__(self):
        """
        :param Count: 高防IP最多可添加的7層規則數量
        :type Count: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class DescribeBaradDataRequest(AbstractModel):
    """DescribeBaradData請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源實例ID
        :type Id: str
        :param MetricName: 指标名，取值：
connum表示TCP活躍連接數；
new_conn表示新建TCP連接數；
inactive_conn表示非活躍連接數;
intraffic表示入流量；
outtraffic表示出流量；
alltraffic表示出流量和入流量之和；
inpkg表示入包速率；
outpkg表示出包速率；
        :type MetricName: str
        :param Period: 統計時間粒度，單位秒（300表示5分鍾；3600表示小時；86400表示天）
        :type Period: int
        :param StartTime: 統計開始時間，秒部分保持爲0，分鍾部分爲5的倍數
        :type StartTime: str
        :param EndTime: 統計結束時間，秒部分保持爲0，分鍾部分爲5的倍數
        :type EndTime: str
        :param Statistics: 統計方式，取值：
max表示最大值；
min表示最小值；
avg表示均值；
        :type Statistics: str
        :param ProtocolPort: 協議端口數組
        :type ProtocolPort: list of ProtocolPort
        :param Ip: 資源實例下的IP，只有當Business=net(高防IP專業版)時才必須填寫資源的一個IP（因爲高防IP專業版資源實例有多個IP，才需要指定）；
        :type Ip: str
        """
        self.Business = None
        self.Id = None
        self.MetricName = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.Statistics = None
        self.ProtocolPort = None
        self.Ip = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Statistics = params.get("Statistics")
        if params.get("ProtocolPort") is not None:
            self.ProtocolPort = []
            for item in params.get("ProtocolPort"):
                obj = ProtocolPort()
                obj._deserialize(item)
                self.ProtocolPort.append(obj)
        self.Ip = params.get("Ip")


class DescribeBaradDataResponse(AbstractModel):
    """DescribeBaradData返回參數結構體

    """

    def __init__(self):
        """
        :param DataList: 返回指标的值
        :type DataList: list of BaradData
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DataList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataList") is not None:
            self.DataList = []
            for item in params.get("DataList"):
                obj = BaradData()
                obj._deserialize(item)
                self.DataList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBasicCCThresholdRequest(AbstractModel):
    """DescribeBasicCCThreshold請求參數結構體

    """

    def __init__(self):
        """
        :param BasicIp: 查詢的IP網址，取值如：1.1.1.1
        :type BasicIp: str
        :param BasicRegion: 查詢IP所屬地域，取值如：gz、bj、sh、hk等地域縮寫
        :type BasicRegion: str
        :param BasicBizType: 專區類型，取值如：公有雲專區：public，黑石專區：bm, NAT服務器專區：nat，網際網路通道：channel。
        :type BasicBizType: str
        :param BasicDeviceType: 設備類型，取值如：服務器：cvm，公有雲負載均衡：clb，黑石負載均衡：lb，NAT服務器：nat，網際網路通道：channel.
        :type BasicDeviceType: str
        :param BasicIpInstance: 可選，IPInstance Nat 閘道（如果查詢的設備類型是NAT服務器，需要傳此參數，通過nat資源查詢介面獲取）
        :type BasicIpInstance: str
        :param BasicIspCode: 可選，運營商線路（如果查詢的設備類型是NAT服務器，需要傳此參數爲5）
        :type BasicIspCode: int
        """
        self.BasicIp = None
        self.BasicRegion = None
        self.BasicBizType = None
        self.BasicDeviceType = None
        self.BasicIpInstance = None
        self.BasicIspCode = None


    def _deserialize(self, params):
        self.BasicIp = params.get("BasicIp")
        self.BasicRegion = params.get("BasicRegion")
        self.BasicBizType = params.get("BasicBizType")
        self.BasicDeviceType = params.get("BasicDeviceType")
        self.BasicIpInstance = params.get("BasicIpInstance")
        self.BasicIspCode = params.get("BasicIspCode")


class DescribeBasicCCThresholdResponse(AbstractModel):
    """DescribeBasicCCThreshold返回參數結構體

    """

    def __init__(self):
        """
        :param CCEnable: CC啓動開關（0:關閉；1:開啓）
        :type CCEnable: int
        :param CCThreshold: CC防護阈值
        :type CCThreshold: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CCEnable = None
        self.CCThreshold = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CCEnable = params.get("CCEnable")
        self.CCThreshold = params.get("CCThreshold")
        self.RequestId = params.get("RequestId")


class DescribeBasicDeviceThresholdRequest(AbstractModel):
    """DescribeBasicDeviceThreshold請求參數結構體

    """

    def __init__(self):
        """
        :param BasicIp: 查詢的IP網址，取值如：1.1.1.1
        :type BasicIp: str
        :param BasicRegion: 查詢IP所屬地域，取值如：gz、bj、sh、hk等地域縮寫
        :type BasicRegion: str
        :param BasicBizType: 專區類型，取值如：公有雲專區：public，黑石專區：bm, NAT服務器專區：nat，網際網路通道：channel。
        :type BasicBizType: str
        :param BasicDeviceType: 設備類型，取值如：服務器：cvm，公有雲負載均衡：clb，黑石負載均衡：lb，NAT服務器：nat，網際網路通道：channel.
        :type BasicDeviceType: str
        :param BasicCheckFlag: 有效性檢查，取值爲1
        :type BasicCheckFlag: int
        :param BasicIpInstance: 可選，IPInstance Nat 閘道（如果查詢的設備類型是NAT服務器，需要傳此參數，通過nat資源查詢介面獲取）
        :type BasicIpInstance: str
        :param BasicIspCode: 可選，運營商線路（如果查詢的設備類型是NAT服務器，需要傳此參數爲5）
        :type BasicIspCode: int
        """
        self.BasicIp = None
        self.BasicRegion = None
        self.BasicBizType = None
        self.BasicDeviceType = None
        self.BasicCheckFlag = None
        self.BasicIpInstance = None
        self.BasicIspCode = None


    def _deserialize(self, params):
        self.BasicIp = params.get("BasicIp")
        self.BasicRegion = params.get("BasicRegion")
        self.BasicBizType = params.get("BasicBizType")
        self.BasicDeviceType = params.get("BasicDeviceType")
        self.BasicCheckFlag = params.get("BasicCheckFlag")
        self.BasicIpInstance = params.get("BasicIpInstance")
        self.BasicIspCode = params.get("BasicIspCode")


class DescribeBasicDeviceThresholdResponse(AbstractModel):
    """DescribeBasicDeviceThreshold返回參數結構體

    """

    def __init__(self):
        """
        :param Threshold: 返回黑洞封堵值
        :type Threshold: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Threshold = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Threshold = params.get("Threshold")
        self.RequestId = params.get("RequestId")


class DescribeCCAlarmThresholdRequest(AbstractModel):
    """DescribeCCAlarmThreshold請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（shield表示棋牌；bgpip表示高防IP；bgp表示高防包；bgp-multip表示多ip高防包；net表示高防IP專業版）
        :type Business: str
        :param RsId: 資源ID,字串類型
        :type RsId: str
        """
        self.Business = None
        self.RsId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.RsId = params.get("RsId")


class DescribeCCAlarmThresholdResponse(AbstractModel):
    """DescribeCCAlarmThreshold返回參數結構體

    """

    def __init__(self):
        """
        :param CCAlarmThreshold: CC告警阈值
        :type CCAlarmThreshold: :class:`tencentcloud.dayu.v20180709.models.CCAlarmThreshold`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CCAlarmThreshold = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CCAlarmThreshold") is not None:
            self.CCAlarmThreshold = CCAlarmThreshold()
            self.CCAlarmThreshold._deserialize(params.get("CCAlarmThreshold"))
        self.RequestId = params.get("RequestId")


class DescribeCCEvListRequest(AbstractModel):
    """DescribeCCEvList請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版；basic表示DDoS基礎防護）
        :type Business: str
        :param StartTime: 開始時間
        :type StartTime: str
        :param EndTime: 結束時間
        :type EndTime: str
        :param Id: 資源實例ID
        :type Id: str
        :param IpList: 資源實例的IP，當business不爲basic時，如果IpList不爲空則Id也必須不能爲空；
        :type IpList: list of str
        :param Limit: 一頁條數，填0表示不分頁
        :type Limit: int
        :param Offset: 頁起始偏移，取值爲(頁碼-1)*一頁條數
        :type Offset: int
        """
        self.Business = None
        self.StartTime = None
        self.EndTime = None
        self.Id = None
        self.IpList = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Id = params.get("Id")
        self.IpList = params.get("IpList")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeCCEvListResponse(AbstractModel):
    """DescribeCCEvList返回參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（shield表示棋牌盾；bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版；basic表示DDoS基礎防護）
        :type Business: str
        :param Id: 資源實例ID
        :type Id: str
        :param IpList: 資源實例的IP清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type IpList: list of str
        :param StartTime: 開始時間
        :type StartTime: str
        :param EndTime: 結束時間
        :type EndTime: str
        :param Data: CC攻擊事件清單
        :type Data: list of CCEventRecord
        :param Total: 總記錄數
        :type Total: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Business = None
        self.Id = None
        self.IpList = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.IpList = params.get("IpList")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = CCEventRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeCCFrequencyRulesRequest(AbstractModel):
    """DescribeCCFrequencyRules請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param RuleId: 7層轉發規則ID（通過獲取7層轉發規則介面可以獲取規則ID）；當填寫時表示獲取轉發規則的訪問頻率控制規則；
        :type RuleId: str
        """
        self.Business = None
        self.Id = None
        self.RuleId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleId = params.get("RuleId")


class DescribeCCFrequencyRulesResponse(AbstractModel):
    """DescribeCCFrequencyRules返回參數結構體

    """

    def __init__(self):
        """
        :param CCFrequencyRuleList: 訪問頻率控制規則清單
        :type CCFrequencyRuleList: list of CCFrequencyRule
        :param CCFrequencyRuleStatus: 訪問頻率控制規則開關狀态，取值[on(開啓)，off(關閉)]
        :type CCFrequencyRuleStatus: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CCFrequencyRuleList = None
        self.CCFrequencyRuleStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CCFrequencyRuleList") is not None:
            self.CCFrequencyRuleList = []
            for item in params.get("CCFrequencyRuleList"):
                obj = CCFrequencyRule()
                obj._deserialize(item)
                self.CCFrequencyRuleList.append(obj)
        self.CCFrequencyRuleStatus = params.get("CCFrequencyRuleStatus")
        self.RequestId = params.get("RequestId")


class DescribeCCIpAllowDenyRequest(AbstractModel):
    """DescribeCCIpAllowDeny請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param Type: 黑或白名單，取值[white(白名單)，black(黑名單)]
注意：此數組只能有一個值，不能同時獲取黑名單和白名單
        :type Type: list of str
        :param Limit: 分頁參數
        :type Limit: int
        :param Offset: 分頁參數
        :type Offset: int
        :param Protocol: 可選，代表HTTP協議或HTTPS協議的CC防護，取值[http（HTTP協議的CC防護），https（HTTPS協議的CC防護）]；
        :type Protocol: str
        """
        self.Business = None
        self.Id = None
        self.Type = None
        self.Limit = None
        self.Offset = None
        self.Protocol = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Protocol = params.get("Protocol")


class DescribeCCIpAllowDenyResponse(AbstractModel):
    """DescribeCCIpAllowDeny返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 該欄位被RecordList欄位替代了，請不要使用
        :type Data: list of KeyValue
        :param Total: 記錄數
        :type Total: int
        :param RecordList: 返回黑/白名單的記錄，
"Key":"ip"時，"Value":值表示ip;
"Key":"domain"時， "Value":值表示域名;
"Key":"type"時，"Value":值表示黑白名單類型(white爲白名單，block爲黑名單);
"Key":"protocol"時，"Value":值表示CC防護的協議(http或https);
        :type RecordList: list of KeyValueRecord
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Total = None
        self.RecordList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Total = params.get("Total")
        if params.get("RecordList") is not None:
            self.RecordList = []
            for item in params.get("RecordList"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.RecordList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCCSelfDefinePolicyRequest(AbstractModel):
    """DescribeCCSelfDefinePolicy請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgp高防包；bgp-multip共享包）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param Limit: 拉取的條數
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        """
        self.Business = None
        self.Id = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeCCSelfDefinePolicyResponse(AbstractModel):
    """DescribeCCSelfDefinePolicy返回參數結構體

    """

    def __init__(self):
        """
        :param Total: 自定義規則總數
        :type Total: int
        :param Policys: 策略清單
        :type Policys: list of CCPolicy
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Policys = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Policys") is not None:
            self.Policys = []
            for item in params.get("Policys"):
                obj = CCPolicy()
                obj._deserialize(item)
                self.Policys.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCCTrendRequest(AbstractModel):
    """DescribeCCTrend請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版；basic表示DDoS基礎防護）
        :type Business: str
        :param Ip: 資源的IP
        :type Ip: str
        :param MetricName: 指标，取值[inqps(總請求峰值，dropqps(攻擊請求峰值))]
        :type MetricName: str
        :param Period: 統計粒度，取值[300(5分鍾)，3600(小時)，86400(天)]
        :type Period: int
        :param StartTime: 統計開始時間
        :type StartTime: str
        :param EndTime: 統計結束時間
        :type EndTime: str
        :param Id: 資源實例ID，當Business爲basic時，此欄位不用填寫（因爲基礎防護沒有資源實例）
        :type Id: str
        """
        self.Business = None
        self.Ip = None
        self.MetricName = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Ip = params.get("Ip")
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Id = params.get("Id")


class DescribeCCTrendResponse(AbstractModel):
    """DescribeCCTrend返回參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版；basic表示DDoS基礎防護）
        :type Business: str
        :param Id: 資源ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type Id: str
        :param Ip: 資源的IP
        :type Ip: str
        :param MetricName: 指标，取值[inqps(總請求峰值，dropqps(攻擊請求峰值))]
        :type MetricName: str
        :param Period: 統計粒度，取值[300(5分鍾)，3600(小時)，86400(天)]
        :type Period: int
        :param StartTime: 統計開始時間
        :type StartTime: str
        :param EndTime: 統計結束時間
        :type EndTime: str
        :param Data: 值數組
        :type Data: list of int non-negative
        :param Count: 值個數
        :type Count: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Business = None
        self.Id = None
        self.Ip = None
        self.MetricName = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Data = params.get("Data")
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class DescribeCCUrlAllowRequest(AbstractModel):
    """DescribeCCUrlAllow請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param Type: 黑或白名單，取值[white(白名單)]，目前只支援白名單
注意：此數組只能有一個值，且只能爲white
        :type Type: list of str
        :param Limit: 分頁參數
        :type Limit: int
        :param Offset: 分頁參數
        :type Offset: int
        :param Protocol: 可選，代表HTTP協議或HTTPS協議的CC防護，取值[http（HTTP協議的CC防護），https（HTTPS協議的CC防護）]；
        :type Protocol: str
        """
        self.Business = None
        self.Id = None
        self.Type = None
        self.Limit = None
        self.Offset = None
        self.Protocol = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Protocol = params.get("Protocol")


class DescribeCCUrlAllowResponse(AbstractModel):
    """DescribeCCUrlAllow返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 該欄位被RecordList欄位替代了，請不要使用
        :type Data: list of KeyValue
        :param Total: 記錄總數
        :type Total: int
        :param RecordList: 返回黑/白名單的記錄，
"Key":"url"時，"Value":值表示URL;
"Key":"domain"時， "Value":值表示域名;
"Key":"type"時，"Value":值表示黑白名單類型(white爲白名單，block爲黑名單);
"Key":"protocol"時，"Value":值表示CC的防護類型(HTTP防護或HTTPS域名防護);
        :type RecordList: list of KeyValueRecord
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Total = None
        self.RecordList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Total = params.get("Total")
        if params.get("RecordList") is not None:
            self.RecordList = []
            for item in params.get("RecordList"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.RecordList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSAlarmThresholdRequest(AbstractModel):
    """DescribeDDoSAlarmThreshold請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（shield表示棋牌；bgpip表示高防IP；bgp表示高防包；bgp-multip表示多ip高防包；net表示高防IP專業版）
        :type Business: str
        :param RsId: 資源ID,字串類型
        :type RsId: str
        """
        self.Business = None
        self.RsId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.RsId = params.get("RsId")


class DescribeDDoSAlarmThresholdResponse(AbstractModel):
    """DescribeDDoSAlarmThreshold返回參數結構體

    """

    def __init__(self):
        """
        :param DDoSAlarmThreshold: DDoS告警阈值
        :type DDoSAlarmThreshold: :class:`tencentcloud.dayu.v20180709.models.DDoSAlarmThreshold`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DDoSAlarmThreshold = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DDoSAlarmThreshold") is not None:
            self.DDoSAlarmThreshold = DDoSAlarmThreshold()
            self.DDoSAlarmThreshold._deserialize(params.get("DDoSAlarmThreshold"))
        self.RequestId = params.get("RequestId")


class DescribeDDoSAttackIPRegionMapRequest(AbstractModel):
    """DescribeDDoSAttackIPRegionMap請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（shield表示棋牌；bgpip表示高防IP；bgp表示高防包；bgp-multip表示多ip高防包；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param StartTime: 統計開始時間
        :type StartTime: str
        :param EndTime: 統計結束時間，最大可統計的時間範圍是半年；
        :type EndTime: str
        :param IpList: 指定資源的特定IP的攻擊源，可選
        :type IpList: list of str
        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.IpList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.IpList = params.get("IpList")


class DescribeDDoSAttackIPRegionMapResponse(AbstractModel):
    """DescribeDDoSAttackIPRegionMap返回參數結構體

    """

    def __init__(self):
        """
        :param NationCount: 全球地域分布數據
        :type NationCount: list of KeyValueRecord
        :param ProvinceCount: 國内省份地域分布數據
        :type ProvinceCount: list of KeyValueRecord
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NationCount = None
        self.ProvinceCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NationCount") is not None:
            self.NationCount = []
            for item in params.get("NationCount"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.NationCount.append(obj)
        if params.get("ProvinceCount") is not None:
            self.ProvinceCount = []
            for item in params.get("ProvinceCount"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.ProvinceCount.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSAttackSourceRequest(AbstractModel):
    """DescribeDDoSAttackSource請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param StartTime: 起始時間
        :type StartTime: str
        :param EndTime: 結束時間
        :type EndTime: str
        :param Limit: 一頁條數，填0表示不分頁
        :type Limit: int
        :param Offset: 頁起始偏移，取值爲(頁碼-1)*一頁條數
        :type Offset: int
        :param IpList: 獲取指定資源的特定ip的攻擊源，可選
        :type IpList: list of str
        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.IpList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.IpList = params.get("IpList")


class DescribeDDoSAttackSourceResponse(AbstractModel):
    """DescribeDDoSAttackSource返回參數結構體

    """

    def __init__(self):
        """
        :param Total: 總攻擊源條數
        :type Total: int
        :param AttackSourceList: 攻擊源清單
        :type AttackSourceList: list of DDoSAttackSourceRecord
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.AttackSourceList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("AttackSourceList") is not None:
            self.AttackSourceList = []
            for item in params.get("AttackSourceList"):
                obj = DDoSAttackSourceRecord()
                obj._deserialize(item)
                self.AttackSourceList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSCountRequest(AbstractModel):
    """DescribeDDoSCount請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param Ip: 資源的IP
        :type Ip: str
        :param StartTime: 統計開始時間
        :type StartTime: str
        :param EndTime: 統計結束時間
        :type EndTime: str
        :param MetricName: 指标，取值[traffic（攻擊協議流量, 單位KB）, pkg（攻擊協議報文數）, classnum（攻擊事件次數）]
        :type MetricName: str
        """
        self.Business = None
        self.Id = None
        self.Ip = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")


class DescribeDDoSCountResponse(AbstractModel):
    """DescribeDDoSCount返回參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param Ip: 資源的IP
        :type Ip: str
        :param StartTime: 統計開始時間
        :type StartTime: str
        :param EndTime: 統計結束時間
        :type EndTime: str
        :param MetricName: 指标，取值[traffic（攻擊協議流量, 單位KB）, pkg（攻擊協議報文數）, classnum（攻擊事件次數）]
        :type MetricName: str
        :param Data: Key-Value值數組，Key說明如下，
當MetricName爲traffic時：
key爲"TcpKBSum"，表示TCP報文流量，單位KB
key爲"UdpKBSum"，表示UDP報文流量，單位KB
key爲"IcmpKBSum"，表示ICMP報文流量，單位KB
key爲"OtherKBSum"，表示其他報文流量，單位KB

當MetricName爲pkg時：
key爲"TcpPacketSum"，表示TCP報文個數，單位個
key爲"UdpPacketSum"，表示UDP報文個數，單位個
key爲"IcmpPacketSum"，表示ICMP報文個數，單位個
key爲"OtherPacketSum"，表示其他報文個數，單位個

當MetricName爲classnum時：
key的值表示攻擊事件類型，其中Key爲"UNKNOWNFLOOD"，表示未知的攻擊事件
        :type Data: list of KeyValue
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Business = None
        self.Id = None
        self.Ip = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSDefendStatusRequest(AbstractModel):
    """DescribeDDoSDefendStatus請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（basic表示基礎防護；bgp表示獨享包；bgp-multip表示共享包；bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源實例ID，只有當Business不是基礎防護時才需要填寫此欄位；
        :type Id: str
        :param Ip: 基礎防護的IP，只有當Business爲基礎防護時才需要填寫此欄位；
        :type Ip: str
        :param BizType: 只有當Business爲基礎防護時才需要填寫此欄位，IP所屬的産品類型，取值[public（CVM産品），bm（黑石産品），eni（彈性網卡），vpngw（VPN閘道）， natgw（NAT閘道），waf（Web應用安全産品），fpc（金融産品），gaap（GAAP産品）, other(托管IP)]
        :type BizType: str
        :param DeviceType: 只有當Business爲基礎防護時才需要填寫此欄位，IP所屬的産品子類，取值[cvm（CVM），lb（負載均衡器），eni（彈性網卡），vpngw（VPN），natgw（NAT），waf（WAF），fpc（金融），gaap（GAAP），other（托管IP），eip（黑石彈性IP）]
        :type DeviceType: str
        :param InstanceId: 只有當Business爲基礎防護時才需要填寫此欄位，IP所屬的資源實例ID，當綁定新IP時必須填寫此欄位；例如是彈性網卡的IP，則InstanceId填寫彈性網卡的ID(eni-*);
        :type InstanceId: str
        :param IPRegion: 只有當Business爲基礎防護時才需要填寫此欄位，表示IP所屬的地域，取值：
"bj":     華北地區(北京)
"cd":     西南地區(成都)
"cq":     西南地區(重慶)
"gz":     華南地區(廣州)
"gzopen": 華南地區(廣州Open)
"hk":     中國香港
"kr":     東南亞地區(首爾)
"sh":     華東地區(上海)
"shjr":   華東地區(上海金融)
"szjr":   華南地區(深圳金融)
"sg":     東南亞地區(新加坡)
"th":     東南亞地區(泰國)
"de":     歐洲地區(德國)
"usw":    美國西部（矽谷）
"ca":     北美地區(多倫多)
"jp":     日本
"hzec":   杭州
"in":     印度
"use":    美東地區（弗吉尼亞）
"ru":     俄羅斯
"tpe":    中國台灣
"nj":     南京
        :type IPRegion: str
        """
        self.Business = None
        self.Id = None
        self.Ip = None
        self.BizType = None
        self.DeviceType = None
        self.InstanceId = None
        self.IPRegion = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.BizType = params.get("BizType")
        self.DeviceType = params.get("DeviceType")
        self.InstanceId = params.get("InstanceId")
        self.IPRegion = params.get("IPRegion")


class DescribeDDoSDefendStatusResponse(AbstractModel):
    """DescribeDDoSDefendStatus返回參數結構體

    """

    def __init__(self):
        """
        :param DefendStatus: 防護狀态，爲0表示防護處于關閉狀态，爲1表示防護處于開啓狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type DefendStatus: int
        :param UndefendExpire: 防護臨時關閉的過期時間，當防護狀态爲開啓時此欄位爲空；
注意：此欄位可能返回 null，表示取不到有效值。
        :type UndefendExpire: str
        :param ShowFlag: 控制台功能展示欄位，爲1表示控制台功能展示，爲0表示控制台功能隐藏
注意：此欄位可能返回 null，表示取不到有效值。
        :type ShowFlag: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DefendStatus = None
        self.UndefendExpire = None
        self.ShowFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DefendStatus = params.get("DefendStatus")
        self.UndefendExpire = params.get("UndefendExpire")
        self.ShowFlag = params.get("ShowFlag")
        self.RequestId = params.get("RequestId")


class DescribeDDoSEvInfoRequest(AbstractModel):
    """DescribeDDoSEvInfo請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param Ip: 資源的IP
        :type Ip: str
        :param StartTime: 攻擊開始時間
        :type StartTime: str
        :param EndTime: 攻擊結束時間
        :type EndTime: str
        """
        self.Business = None
        self.Id = None
        self.Ip = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeDDoSEvInfoResponse(AbstractModel):
    """DescribeDDoSEvInfo返回參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param Ip: 資源的IP
        :type Ip: str
        :param StartTime: 攻擊開始時間
        :type StartTime: str
        :param EndTime: 攻擊結束時間
        :type EndTime: str
        :param TcpPacketSum: TCP報文攻擊包數
        :type TcpPacketSum: int
        :param TcpKBSum: TCP報文攻擊流量，單位KB
        :type TcpKBSum: int
        :param UdpPacketSum: UDP報文攻擊包數
        :type UdpPacketSum: int
        :param UdpKBSum: UDP報文攻擊流量，單位KB
        :type UdpKBSum: int
        :param IcmpPacketSum: ICMP報文攻擊包數
        :type IcmpPacketSum: int
        :param IcmpKBSum: ICMP報文攻擊流量，單位KB
        :type IcmpKBSum: int
        :param OtherPacketSum: 其他報文攻擊包數
        :type OtherPacketSum: int
        :param OtherKBSum: 其他報文攻擊流量，單位KB
        :type OtherKBSum: int
        :param TotalTraffic: 累計攻擊流量，單位KB
        :type TotalTraffic: int
        :param Mbps: 攻擊流量頻寬峰值
        :type Mbps: int
        :param Pps: 攻擊包速率峰值
        :type Pps: int
        :param PcapUrl: PCAP文件下載連結
        :type PcapUrl: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Business = None
        self.Id = None
        self.Ip = None
        self.StartTime = None
        self.EndTime = None
        self.TcpPacketSum = None
        self.TcpKBSum = None
        self.UdpPacketSum = None
        self.UdpKBSum = None
        self.IcmpPacketSum = None
        self.IcmpKBSum = None
        self.OtherPacketSum = None
        self.OtherKBSum = None
        self.TotalTraffic = None
        self.Mbps = None
        self.Pps = None
        self.PcapUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TcpPacketSum = params.get("TcpPacketSum")
        self.TcpKBSum = params.get("TcpKBSum")
        self.UdpPacketSum = params.get("UdpPacketSum")
        self.UdpKBSum = params.get("UdpKBSum")
        self.IcmpPacketSum = params.get("IcmpPacketSum")
        self.IcmpKBSum = params.get("IcmpKBSum")
        self.OtherPacketSum = params.get("OtherPacketSum")
        self.OtherKBSum = params.get("OtherKBSum")
        self.TotalTraffic = params.get("TotalTraffic")
        self.Mbps = params.get("Mbps")
        self.Pps = params.get("Pps")
        self.PcapUrl = params.get("PcapUrl")
        self.RequestId = params.get("RequestId")


class DescribeDDoSEvListRequest(AbstractModel):
    """DescribeDDoSEvList請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版；basic表示DDoS基礎防護）
        :type Business: str
        :param StartTime: 開始時間
        :type StartTime: str
        :param EndTime: 結束時間
        :type EndTime: str
        :param Id: 資源實例ID，當Business爲basic時，此欄位不用填寫（因爲基礎防護沒有資源實例）
        :type Id: str
        :param IpList: 資源的IP
        :type IpList: list of str
        :param OverLoad: 是否超過彈性防護峰值，取值[yes(是)，no(否)]，填寫空字串時表示不進行過濾
        :type OverLoad: str
        :param Limit: 一頁條數，填0表示不分頁
        :type Limit: int
        :param Offset: 頁起始偏移，取值爲(頁碼-1)*一頁條數
        :type Offset: int
        """
        self.Business = None
        self.StartTime = None
        self.EndTime = None
        self.Id = None
        self.IpList = None
        self.OverLoad = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Id = params.get("Id")
        self.IpList = params.get("IpList")
        self.OverLoad = params.get("OverLoad")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeDDoSEvListResponse(AbstractModel):
    """DescribeDDoSEvList返回參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版；basic表示DDoS基礎防護）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param IpList: 資源的IP
注意：此欄位可能返回 null，表示取不到有效值。
        :type IpList: list of str
        :param StartTime: 開始時間
        :type StartTime: str
        :param EndTime: 結束時間
        :type EndTime: str
        :param Data: DDoS攻擊事件清單
        :type Data: list of DDoSEventRecord
        :param Total: 總記錄數
        :type Total: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Business = None
        self.Id = None
        self.IpList = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.IpList = params.get("IpList")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DDoSEventRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeDDoSIpLogRequest(AbstractModel):
    """DescribeDDoSIpLog請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param Ip: 資源的IP
        :type Ip: str
        :param StartTime: 攻擊開始時間
        :type StartTime: str
        :param EndTime: 攻擊結束時間
        :type EndTime: str
        """
        self.Business = None
        self.Id = None
        self.Ip = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeDDoSIpLogResponse(AbstractModel):
    """DescribeDDoSIpLog返回參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param Ip: 資源的IP
        :type Ip: str
        :param StartTime: 攻擊開始時間
        :type StartTime: str
        :param EndTime: 攻擊結束時間
        :type EndTime: str
        :param Data: IP攻擊日志，KeyValue數組，Key-Value取值說明：
Key爲"LogTime"時，Value值爲IP日志時間
Key爲"LogMessage"時，Value值爲Ip日志内容
        :type Data: list of KeyValueRecord
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Business = None
        self.Id = None
        self.Ip = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSNetCountRequest(AbstractModel):
    """DescribeDDoSNetCount請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param StartTime: 統計開始時間
        :type StartTime: str
        :param EndTime: 統計結束時間
        :type EndTime: str
        :param MetricName: 指标，取值[traffic（攻擊協議流量, 單位KB）, pkg（攻擊協議報文數）, classnum（攻擊事件次數）]
        :type MetricName: str
        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")


class DescribeDDoSNetCountResponse(AbstractModel):
    """DescribeDDoSNetCount返回參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param StartTime: 統計開始時間
        :type StartTime: str
        :param EndTime: 統計結束時間
        :type EndTime: str
        :param MetricName: 指标，取值[traffic（攻擊協議流量, 單位KB）, pkg（攻擊協議報文數）, classnum（攻擊事件次數）]
        :type MetricName: str
        :param Data: Key-Value值數組，Key說明如下，
當MetricName爲traffic時：
key爲"TcpKBSum"，表示TCP報文流量，單位KB
key爲"UdpKBSum"，表示UDP報文流量，單位KB
key爲"IcmpKBSum"，表示ICMP報文流量，單位KB
key爲"OtherKBSum"，表示其他報文流量，單位KB

當MetricName爲pkg時：
key爲"TcpPacketSum"，表示TCP報文個數，單位個
key爲"UdpPacketSum"，表示UDP報文個數，單位個
key爲"IcmpPacketSum"，表示ICMP報文個數，單位個
key爲"OtherPacketSum"，表示其他報文個數，單位個

當MetricName爲classnum時：
key的值表示攻擊事件類型，其中Key爲"UNKNOWNFLOOD"，表示未知的攻擊事件
        :type Data: list of KeyValue
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSNetEvInfoRequest(AbstractModel):
    """DescribeDDoSNetEvInfo請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param StartTime: 攻擊開始時間
        :type StartTime: str
        :param EndTime: 攻擊結束時間
        :type EndTime: str
        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeDDoSNetEvInfoResponse(AbstractModel):
    """DescribeDDoSNetEvInfo返回參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param StartTime: 攻擊開始時間
        :type StartTime: str
        :param EndTime: 攻擊結束時間
        :type EndTime: str
        :param TcpPacketSum: TCP報文攻擊包數
        :type TcpPacketSum: int
        :param TcpKBSum: TCP報文攻擊流量，單位KB
        :type TcpKBSum: int
        :param UdpPacketSum: UDP報文攻擊包數
        :type UdpPacketSum: int
        :param UdpKBSum: UDP報文攻擊流量，單位KB
        :type UdpKBSum: int
        :param IcmpPacketSum: ICMP報文攻擊包數
        :type IcmpPacketSum: int
        :param IcmpKBSum: ICMP報文攻擊流量，單位KB
        :type IcmpKBSum: int
        :param OtherPacketSum: 其他報文攻擊包數
        :type OtherPacketSum: int
        :param OtherKBSum: 其他報文攻擊流量，單位KB
        :type OtherKBSum: int
        :param TotalTraffic: 累計攻擊流量，單位KB
        :type TotalTraffic: int
        :param Mbps: 攻擊流量頻寬峰值
        :type Mbps: int
        :param Pps: 攻擊包速率峰值
        :type Pps: int
        :param PcapUrl: PCAP文件下載連結
        :type PcapUrl: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.TcpPacketSum = None
        self.TcpKBSum = None
        self.UdpPacketSum = None
        self.UdpKBSum = None
        self.IcmpPacketSum = None
        self.IcmpKBSum = None
        self.OtherPacketSum = None
        self.OtherKBSum = None
        self.TotalTraffic = None
        self.Mbps = None
        self.Pps = None
        self.PcapUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TcpPacketSum = params.get("TcpPacketSum")
        self.TcpKBSum = params.get("TcpKBSum")
        self.UdpPacketSum = params.get("UdpPacketSum")
        self.UdpKBSum = params.get("UdpKBSum")
        self.IcmpPacketSum = params.get("IcmpPacketSum")
        self.IcmpKBSum = params.get("IcmpKBSum")
        self.OtherPacketSum = params.get("OtherPacketSum")
        self.OtherKBSum = params.get("OtherKBSum")
        self.TotalTraffic = params.get("TotalTraffic")
        self.Mbps = params.get("Mbps")
        self.Pps = params.get("Pps")
        self.PcapUrl = params.get("PcapUrl")
        self.RequestId = params.get("RequestId")


class DescribeDDoSNetEvListRequest(AbstractModel):
    """DescribeDDoSNetEvList請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param StartTime: 開始時間
        :type StartTime: str
        :param EndTime: 結束時間
        :type EndTime: str
        :param Limit: 一頁條數，填0表示不分頁
        :type Limit: int
        :param Offset: 頁起始偏移，取值爲(頁碼-1)*一頁條數
        :type Offset: int
        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeDDoSNetEvListResponse(AbstractModel):
    """DescribeDDoSNetEvList返回參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param StartTime: 開始時間
        :type StartTime: str
        :param EndTime: 結束時間
        :type EndTime: str
        :param Data: DDoS攻擊事件清單
        :type Data: list of DDoSEventRecord
        :param Total: 總記錄數
        :type Total: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DDoSEventRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeDDoSNetIpLogRequest(AbstractModel):
    """DescribeDDoSNetIpLog請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param StartTime: 攻擊開始時間
        :type StartTime: str
        :param EndTime: 攻擊結束時間
        :type EndTime: str
        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeDDoSNetIpLogResponse(AbstractModel):
    """DescribeDDoSNetIpLog返回參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param StartTime: 攻擊開始時間
        :type StartTime: str
        :param EndTime: 攻擊結束時間
        :type EndTime: str
        :param Data: IP攻擊日志，KeyValue數組，Key-Value取值說明：
Key爲"LogTime"時，Value值爲IP日志時間
Key爲"LogMessage"時，Value值爲Ip日志内容
        :type Data: list of KeyValueRecord
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSNetTrendRequest(AbstractModel):
    """DescribeDDoSNetTrend請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param MetricName: 指标，取值[bps(攻擊流量頻寬，pps(攻擊包速率))]
        :type MetricName: str
        :param Period: 統計粒度，取值[300(5分鍾)，3600(小時)，86400(天)]
        :type Period: int
        :param StartTime: 統計開始時間
        :type StartTime: str
        :param EndTime: 統計結束時間
        :type EndTime: str
        """
        self.Business = None
        self.Id = None
        self.MetricName = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeDDoSNetTrendResponse(AbstractModel):
    """DescribeDDoSNetTrend返回參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param MetricName: 指标，取值[bps(攻擊流量頻寬，pps(攻擊包速率))]
        :type MetricName: str
        :param Period: 統計粒度，取值[300(5分鍾)，3600(小時)，86400(天)]
        :type Period: int
        :param StartTime: 統計開始時間
        :type StartTime: str
        :param EndTime: 統計結束時間
        :type EndTime: str
        :param Data: 值數組
        :type Data: list of int non-negative
        :param Count: 值個數
        :type Count: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Business = None
        self.Id = None
        self.MetricName = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Data = params.get("Data")
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class DescribeDDoSPolicyRequest(AbstractModel):
    """DescribeDDoSPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param Id: 可選欄位，資源ID，如果填寫則表示該資源綁定的DDoS高級策略
        :type Id: str
        """
        self.Business = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")


class DescribeDDoSPolicyResponse(AbstractModel):
    """DescribeDDoSPolicy返回參數結構體

    """

    def __init__(self):
        """
        :param DDosPolicyList: DDoS高級策略清單
        :type DDosPolicyList: list of DDosPolicy
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DDosPolicyList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DDosPolicyList") is not None:
            self.DDosPolicyList = []
            for item in params.get("DDosPolicyList"):
                obj = DDosPolicy()
                obj._deserialize(item)
                self.DDosPolicyList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSTrendRequest(AbstractModel):
    """DescribeDDoSTrend請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版；basic表示DDoS基礎防護）
        :type Business: str
        :param Ip: 資源實例的IP
        :type Ip: str
        :param MetricName: 指标，取值[bps(攻擊流量頻寬，pps(攻擊包速率))]
        :type MetricName: str
        :param Period: 統計粒度，取值[300(5分鍾)，3600(小時)，86400(天)]
        :type Period: int
        :param StartTime: 統計開始時間
        :type StartTime: str
        :param EndTime: 統計結束時間
        :type EndTime: str
        :param Id: 資源實例ID，當Business爲basic時，此欄位不用填寫（因爲基礎防護沒有資源實例）
        :type Id: str
        """
        self.Business = None
        self.Ip = None
        self.MetricName = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Ip = params.get("Ip")
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Id = params.get("Id")


class DescribeDDoSTrendResponse(AbstractModel):
    """DescribeDDoSTrend返回參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版；basic表示DDoS基礎防護）
        :type Business: str
        :param Id: 資源ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type Id: str
        :param Ip: 資源的IP
        :type Ip: str
        :param MetricName: 指标，取值[bps(攻擊流量頻寬，pps(攻擊包速率))]
        :type MetricName: str
        :param Period: 統計粒度，取值[300(5分鍾)，3600(小時)，86400(天)]
        :type Period: int
        :param StartTime: 統計開始時間
        :type StartTime: str
        :param EndTime: 統計結束時間
        :type EndTime: str
        :param Data: 值數組
        :type Data: list of int non-negative
        :param Count: 值個數
        :type Count: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Business = None
        self.Id = None
        self.Ip = None
        self.MetricName = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Data = params.get("Data")
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class DescribeDDoSUsedStatisRequest(AbstractModel):
    """DescribeDDoSUsedStatis請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP）
        :type Business: str
        """
        self.Business = None


    def _deserialize(self, params):
        self.Business = params.get("Business")


class DescribeDDoSUsedStatisResponse(AbstractModel):
    """DescribeDDoSUsedStatis返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 欄位值，如下：
Days：高防資源使用天數
Attacks：DDoS防護次數
        :type Data: list of KeyValue
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIPProductInfoRequest(AbstractModel):
    """DescribeIPProductInfo請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgp表示獨享包；bgp-multip表示共享包）
        :type Business: str
        :param IpList: IP清單
        :type IpList: list of str
        """
        self.Business = None
        self.IpList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.IpList = params.get("IpList")


class DescribeIPProductInfoResponse(AbstractModel):
    """DescribeIPProductInfo返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 雲産品訊息清單，如果沒有查詢到則返回空數組，值說明如下：
Key爲ProductName時，value表示雲産品實例的名稱；
Key爲ProductInstanceId時，value表示雲産品實例的ID；
Key爲ProductType時，value表示的是雲産品的類型（cvm表示雲主機、clb表示負載均衡）;
Key爲IP時，value表示雲産品實例的IP；
        :type Data: list of KeyValueRecord
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInsurePacksRequest(AbstractModel):
    """DescribeInsurePacks請求參數結構體

    """

    def __init__(self):
        """
        :param IdList: 可選欄位，保險包套餐ID，當要獲取指定ID（例如insure-000000xe）的保險包套餐時請填寫此欄位；
        :type IdList: list of str
        """
        self.IdList = None


    def _deserialize(self, params):
        self.IdList = params.get("IdList")


class DescribeInsurePacksResponse(AbstractModel):
    """DescribeInsurePacks返回參數結構體

    """

    def __init__(self):
        """
        :param InsurePacks: 保險包套餐清單
        :type InsurePacks: list of KeyValueRecord
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InsurePacks = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InsurePacks") is not None:
            self.InsurePacks = []
            for item in params.get("InsurePacks"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.InsurePacks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIpBlockListRequest(AbstractModel):
    """DescribeIpBlockList請求參數結構體

    """


class DescribeIpBlockListResponse(AbstractModel):
    """DescribeIpBlockList返回參數結構體

    """

    def __init__(self):
        """
        :param List: IP封堵清單
        :type List: list of IpBlockData
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = IpBlockData()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIpUnBlockListRequest(AbstractModel):
    """DescribeIpUnBlockList請求參數結構體

    """

    def __init__(self):
        """
        :param BeginTime: 開始時間
        :type BeginTime: str
        :param EndTime: 結束時間
        :type EndTime: str
        :param Ip: IP（不爲空時，進行IP過濾）
        :type Ip: str
        :param Paging: 分頁參數（不爲空時，進行分頁查詢），此欄位後面會棄用，請用Limit和Offset欄位代替；
        :type Paging: :class:`tencentcloud.dayu.v20180709.models.Paging`
        :param Limit: 一頁條數，填0表示不分頁
        :type Limit: int
        :param Offset: 頁起始偏移，取值爲(頁碼-1)*一頁條數
        :type Offset: int
        """
        self.BeginTime = None
        self.EndTime = None
        self.Ip = None
        self.Paging = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Ip = params.get("Ip")
        if params.get("Paging") is not None:
            self.Paging = Paging()
            self.Paging._deserialize(params.get("Paging"))
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeIpUnBlockListResponse(AbstractModel):
    """DescribeIpUnBlockList返回參數結構體

    """

    def __init__(self):
        """
        :param BeginTime: 開始時間
        :type BeginTime: str
        :param EndTime: 結束時間
        :type EndTime: str
        :param List: IP解封記錄
        :type List: list of IpUnBlockData
        :param Total: 總記錄數
        :type Total: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.BeginTime = None
        self.EndTime = None
        self.List = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = IpUnBlockData()
                obj._deserialize(item)
                self.List.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeL4HealthConfigRequest(AbstractModel):
    """DescribeL4HealthConfig請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param RuleIdList: 規則ID數組，當導出所有規則的健康檢查配置則不填或填空數組；
        :type RuleIdList: list of str
        """
        self.Business = None
        self.Id = None
        self.RuleIdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleIdList = params.get("RuleIdList")


class DescribeL4HealthConfigResponse(AbstractModel):
    """DescribeL4HealthConfig返回參數結構體

    """

    def __init__(self):
        """
        :param HealthConfig: 四層健康檢查配置數組
        :type HealthConfig: list of L4HealthConfig
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.HealthConfig = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HealthConfig") is not None:
            self.HealthConfig = []
            for item in params.get("HealthConfig"):
                obj = L4HealthConfig()
                obj._deserialize(item)
                self.HealthConfig.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeL4RulesErrHealthRequest(AbstractModel):
    """DescribeL4RulesErrHealth請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        """
        self.Business = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")


class DescribeL4RulesErrHealthResponse(AbstractModel):
    """DescribeL4RulesErrHealth返回參數結構體

    """

    def __init__(self):
        """
        :param Total: 異常規則的總數
        :type Total: int
        :param ErrHealths: 異常規則清單，返回值說明: Key值爲規則ID，Value值爲異常IP，多個IP用","分割
        :type ErrHealths: list of KeyValue
        :param ExtErrHealths: 異常規則清單(提供更多的錯誤相關訊息)，返回值說明:
Key值爲RuleId時，Value值爲規則ID；
Key值爲Protocol時，Value值爲規則的轉發協議；
Key值爲VirtualPort時，Value值爲規則的轉發端口；
Key值爲ErrMessage時，Value值爲健康檢查異常訊息；
健康檢查異常訊息的格式爲"SourceIp:1.1.1.1|SourcePort:1234|AbnormalStatTime:1570689065|AbnormalReason:connection time out|Interval:20|CheckNum:6|FailNum:6" 多個源IP的錯誤訊息用，分割,
SourceIp表示源站IP，SourcePort表示源站端口，AbnormalStatTime表示異常時間，AbnormalReason表示異常原因，Interval表示檢查週期，CheckNum表示檢查次數，FailNum表示失敗次數；
        :type ExtErrHealths: list of KeyValueRecord
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.ErrHealths = None
        self.ExtErrHealths = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("ErrHealths") is not None:
            self.ErrHealths = []
            for item in params.get("ErrHealths"):
                obj = KeyValue()
                obj._deserialize(item)
                self.ErrHealths.append(obj)
        if params.get("ExtErrHealths") is not None:
            self.ExtErrHealths = []
            for item in params.get("ExtErrHealths"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.ExtErrHealths.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeL7HealthConfigRequest(AbstractModel):
    """DescribeL7HealthConfig請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param RuleIdList: 規則ID數組，當導出所有規則的健康檢查配置則不填或填空數組；
        :type RuleIdList: list of str
        """
        self.Business = None
        self.Id = None
        self.RuleIdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleIdList = params.get("RuleIdList")


class DescribeL7HealthConfigResponse(AbstractModel):
    """DescribeL7HealthConfig返回參數結構體

    """

    def __init__(self):
        """
        :param HealthConfig: 七層健康檢查配置數組
        :type HealthConfig: list of L7HealthConfig
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.HealthConfig = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HealthConfig") is not None:
            self.HealthConfig = []
            for item in params.get("HealthConfig"):
                obj = L7HealthConfig()
                obj._deserialize(item)
                self.HealthConfig.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNewL4RulesErrHealthRequest(AbstractModel):
    """DescribeNewL4RulesErrHealth請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP）
        :type Business: str
        :param RuleIdList: 規則ID清單
        :type RuleIdList: list of str
        """
        self.Business = None
        self.RuleIdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.RuleIdList = params.get("RuleIdList")


class DescribeNewL4RulesErrHealthResponse(AbstractModel):
    """DescribeNewL4RulesErrHealth返回參數結構體

    """

    def __init__(self):
        """
        :param Total: 異常規則的總數
        :type Total: int
        :param ErrHealths: 異常規則清單，返回值說明: Key值爲規則ID，Value值爲異常IP，多個IP用","分割
        :type ErrHealths: list of KeyValue
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.ErrHealths = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("ErrHealths") is not None:
            self.ErrHealths = []
            for item in params.get("ErrHealths"):
                obj = KeyValue()
                obj._deserialize(item)
                self.ErrHealths.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNewL4RulesRequest(AbstractModel):
    """DescribeNewL4Rules請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP）
        :type Business: str
        :param Ip: 指定IP查詢
        :type Ip: str
        :param VirtualPort: 指定高防IP端口查詢
        :type VirtualPort: int
        :param Limit: 一頁條數，填0表示不分頁
        :type Limit: int
        :param Offset: 頁起始偏移，取值爲(頁碼-1)*一頁條數
        :type Offset: int
        """
        self.Business = None
        self.Ip = None
        self.VirtualPort = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Ip = params.get("Ip")
        self.VirtualPort = params.get("VirtualPort")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeNewL4RulesResponse(AbstractModel):
    """DescribeNewL4Rules返回參數結構體

    """

    def __init__(self):
        """
        :param Rules: 轉發規則清單
        :type Rules: list of NewL4RuleEntry
        :param Total: 總規則數
        :type Total: int
        :param Healths: 四層健康檢查配置清單
        :type Healths: list of L4RuleHealth
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Rules = None
        self.Total = None
        self.Healths = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = NewL4RuleEntry()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Total = params.get("Total")
        if params.get("Healths") is not None:
            self.Healths = []
            for item in params.get("Healths"):
                obj = L4RuleHealth()
                obj._deserialize(item)
                self.Healths.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNewL7RulesErrHealthRequest(AbstractModel):
    """DescribeNewL7RulesErrHealth請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP)
        :type Business: str
        :param RuleIdList: 規則Id清單
        :type RuleIdList: list of str
        """
        self.Business = None
        self.RuleIdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.RuleIdList = params.get("RuleIdList")


class DescribeNewL7RulesErrHealthResponse(AbstractModel):
    """DescribeNewL7RulesErrHealth返回參數結構體

    """

    def __init__(self):
        """
        :param Total: 異常規則的總數
        :type Total: int
        :param ErrHealths: 異常規則清單，返回值說明: Key值爲規則ID，Value值爲異常IP及錯誤訊息，多個IP用","分割
        :type ErrHealths: list of KeyValue
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.ErrHealths = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("ErrHealths") is not None:
            self.ErrHealths = []
            for item in params.get("ErrHealths"):
                obj = KeyValue()
                obj._deserialize(item)
                self.ErrHealths.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePackIndexRequest(AbstractModel):
    """DescribePackIndex請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示高防包；net表示高防IP專業版）
        :type Business: str
        """
        self.Business = None


    def _deserialize(self, params):
        self.Business = params.get("Business")


class DescribePackIndexResponse(AbstractModel):
    """DescribePackIndex返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 欄位值，如下：
TotalPackCount：資源數
AttackPackCount：清洗中的資源數
BlockPackCount：封堵中的資源數
ExpiredPackCount：過期的資源數
ExpireingPackCount：即将過期的資源數
IsolatePackCount：隔離中的資源數
        :type Data: list of KeyValue
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePcapRequest(AbstractModel):
    """DescribePcap請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源實例ID
        :type Id: str
        :param StartTime: 攻擊事件的開始時間，格式爲"2018-08-28 07:00:00"
        :type StartTime: str
        :param EndTime: 攻擊事件的結束時間，格式爲"2018-08-28 07:02:00"
        :type EndTime: str
        :param Ip: 資源的IP，只有當Business爲net時才需要填寫資源實例下的IP；
        :type Ip: str
        """
        self.Business = None
        self.Id = None
        self.StartTime = None
        self.EndTime = None
        self.Ip = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Ip = params.get("Ip")


class DescribePcapResponse(AbstractModel):
    """DescribePcap返回參數結構體

    """

    def __init__(self):
        """
        :param PcapUrlList: pcap包的下載連結清單，無pcap包時爲空數組；
        :type PcapUrlList: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PcapUrlList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PcapUrlList = params.get("PcapUrlList")
        self.RequestId = params.get("RequestId")


class DescribePolicyCaseRequest(AbstractModel):
    """DescribePolicyCase請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param SceneId: 策略場景ID
        :type SceneId: str
        """
        self.Business = None
        self.SceneId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.SceneId = params.get("SceneId")


class DescribePolicyCaseResponse(AbstractModel):
    """DescribePolicyCase返回參數結構體

    """

    def __init__(self):
        """
        :param CaseList: 策略場景清單
        :type CaseList: list of KeyValueRecord
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CaseList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CaseList") is not None:
            self.CaseList = []
            for item in params.get("CaseList"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.CaseList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResIpListRequest(AbstractModel):
    """DescribeResIpList請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param IdList: 資源ID, 如果不填，則獲取用戶所有資源的IP
        :type IdList: list of str
        """
        self.Business = None
        self.IdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.IdList = params.get("IdList")


class DescribeResIpListResponse(AbstractModel):
    """DescribeResIpList返回參數結構體

    """

    def __init__(self):
        """
        :param Resource: 資源的IP清單
        :type Resource: list of ResourceIp
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Resource = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Resource") is not None:
            self.Resource = []
            for item in params.get("Resource"):
                obj = ResourceIp()
                obj._deserialize(item)
                self.Resource.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResourceListRequest(AbstractModel):
    """DescribeResourceList請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgp表示獨享包；bgp-multip表示共享包；bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param RegionList: 地域碼搜索，可選，當不指定地域時空數組，當指定地域時，填地域碼。例如：["gz", "sh"]
        :type RegionList: list of str
        :param Line: 線路搜索，可選，只有當獲取高防IP資源清單是可以選填，取值爲[1（BGP線路），2（南京電信），3（南京聯通），99（第三方合作線路）]，當獲取其他産品時請填空數組；
        :type Line: list of int non-negative
        :param IdList: 資源ID搜索，可選，當不爲空數組時表示獲取指定資源的資源清單；
        :type IdList: list of str
        :param Name: 資源名稱搜索，可選，當不爲空字串時表示按名稱搜索資源；
        :type Name: str
        :param IpList: IP搜索清單，可選，當不爲空時表示安裝IP搜索資源；
        :type IpList: list of str
        :param Status: 資源狀态搜索清單，可選，取值爲[0（運作中）, 1（清洗中）, 2（封堵中）]，當填空數組時不進行狀态搜索；
        :type Status: list of int non-negative
        :param Expire: 即将到期搜索；可選，取值爲[0（不搜索），1（搜索即将到期的資源）]
        :type Expire: int
        :param OderBy: 排序欄位，可選
        :type OderBy: list of OrderBy
        :param Limit: 一頁條數，填0表示不分頁
        :type Limit: int
        :param Offset: 頁起始偏移，取值爲(頁碼-1)*一頁條數
        :type Offset: int
        :param CName: 高防IP專業版資源的CNAME，可選，只對高防IP專業版資源清單有效；
        :type CName: str
        :param Domain: 高防IP專業版資源的域名，可選，只對高防IP專業版資源清單有效；
        :type Domain: str
        """
        self.Business = None
        self.RegionList = None
        self.Line = None
        self.IdList = None
        self.Name = None
        self.IpList = None
        self.Status = None
        self.Expire = None
        self.OderBy = None
        self.Limit = None
        self.Offset = None
        self.CName = None
        self.Domain = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.RegionList = params.get("RegionList")
        self.Line = params.get("Line")
        self.IdList = params.get("IdList")
        self.Name = params.get("Name")
        self.IpList = params.get("IpList")
        self.Status = params.get("Status")
        self.Expire = params.get("Expire")
        if params.get("OderBy") is not None:
            self.OderBy = []
            for item in params.get("OderBy"):
                obj = OrderBy()
                obj._deserialize(item)
                self.OderBy.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.CName = params.get("CName")
        self.Domain = params.get("Domain")


class DescribeResourceListResponse(AbstractModel):
    """DescribeResourceList返回參數結構體

    """

    def __init__(self):
        """
        :param Total: 總記錄數
        :type Total: int
        :param ServicePacks: 資源記錄清單，返回Key值說明：
"Key": "CreateTime" 表示資源實例購買時間
"Key": "Region" 表示資源實例的地域
"Key": "BoundIP" 表示獨享包實例綁定的IP
"Key": "Id" 表示資源實例的ID
"Key": "CCEnabled" 表示資源實例的CC防護開關狀态
"Key": "DDoSThreshold" 表示資源實例的DDoS的清洗阈值	
"Key": "BoundStatus" 表示獨享包或共享包實例的綁定IP操作狀态(綁定中或綁定完成)
"Key": "Type" 此欄位棄用
"Key": "ElasticLimit" 表示資源實例的彈性防護值
"Key": "DDoSAI" 表示資源實例的DDoS AI防護開關
"Key": "Bandwidth" 表示資源實例的保底防護值
"Key": "OverloadCount" 表示資源實例受到超過彈性防護值的次數
"Key": "Status" 表示資源實例的狀态(idle:運作中, attacking:攻擊中, blocking:封堵中, isolate:隔離中)
"Key": "Lbid" 此欄位棄用
"Key": "ShowFlag" 此欄位棄用
"Key": "Expire" 表示資源實例的過期時間
"Key": "CCThreshold" 表示資源實例的CC防護觸發阈值
"Key": "AutoRenewFlag" 表示資源實例的自動續約是否開啓
"Key": "IspCode" 表示獨享包或共享包的線路(0-電信, 1-聯通, 2-移動, 5-BGP)
"Key": "PackType" 表示套餐包類型
"Key": "PackId" 表示套餐包ID
"Key": "Name" 表示資源實例的名稱
"Key": "Locked" 此欄位棄用
"Key": "IpDDoSLevel" 表示資源實例的防護等級(low-寬松, middle-正常, high-嚴格)
"Key": "DefendStatus" 表示資源實例的DDoS防護狀态(防護開啓或臨時關閉)
"Key": "UndefendExpire" 表示資源實例的DDoS防護臨時關閉結束時間
"Key": "Tgw" 表示資源實例是否是新資源
        :type ServicePacks: list of KeyValueRecord
        :param Business: 大禹子産品代号（bgp表示獨享包；bgp-multip表示共享包；bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.ServicePacks = None
        self.Business = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("ServicePacks") is not None:
            self.ServicePacks = []
            for item in params.get("ServicePacks"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.ServicePacks.append(obj)
        self.Business = params.get("Business")
        self.RequestId = params.get("RequestId")


class DescribeRuleSetsRequest(AbstractModel):
    """DescribeRuleSets請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param IdList: 資源ID清單
        :type IdList: list of str
        """
        self.Business = None
        self.IdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.IdList = params.get("IdList")


class DescribeRuleSetsResponse(AbstractModel):
    """DescribeRuleSets返回參數結構體

    """

    def __init__(self):
        """
        :param L4RuleSets: 規則記錄數數組，取值說明:
Key值爲"Id"時，Value表示資源ID
Key值爲"RuleIdList"時，Value值表示資源的規則ID，多個規則ID用","分割
Key值爲"RuleNameList"時，Value值表示資源的規則名，多個規則名用","分割
Key值爲"RuleNum"時，Value值表示資源的規則數
        :type L4RuleSets: list of KeyValueRecord
        :param L7RuleSets: 規則記錄數數組，取值說明:
Key值爲"Id"時，Value表示資源ID
Key值爲"RuleIdList"時，Value值表示資源的規則ID，多個規則ID用","分割
Key值爲"RuleNameList"時，Value值表示資源的規則名，多個規則名用","分割
Key值爲"RuleNum"時，Value值表示資源的規則數
        :type L7RuleSets: list of KeyValueRecord
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.L4RuleSets = None
        self.L7RuleSets = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("L4RuleSets") is not None:
            self.L4RuleSets = []
            for item in params.get("L4RuleSets"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.L4RuleSets.append(obj)
        if params.get("L7RuleSets") is not None:
            self.L7RuleSets = []
            for item in params.get("L7RuleSets"):
                obj = KeyValueRecord()
                obj._deserialize(item)
                self.L7RuleSets.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSchedulingDomainListRequest(AbstractModel):
    """DescribeSchedulingDomainList請求參數結構體

    """

    def __init__(self):
        """
        :param Limit: 一頁條數，填0表示不分頁
        :type Limit: int
        :param Offset: 頁起始偏移，取值爲(頁碼-1)*一頁條數
        :type Offset: int
        :param Domain: 可選，篩選特定的域名
        :type Domain: str
        """
        self.Limit = None
        self.Offset = None
        self.Domain = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Domain = params.get("Domain")


class DescribeSchedulingDomainListResponse(AbstractModel):
    """DescribeSchedulingDomainList返回參數結構體

    """

    def __init__(self):
        """
        :param Total: 調度域名總數
        :type Total: int
        :param DomainList: 調度域名清單訊息
        :type DomainList: list of SchedulingDomain
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.DomainList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("DomainList") is not None:
            self.DomainList = []
            for item in params.get("DomainList"):
                obj = SchedulingDomain()
                obj._deserialize(item)
                self.DomainList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecIndexRequest(AbstractModel):
    """DescribeSecIndex請求參數結構體

    """


class DescribeSecIndexResponse(AbstractModel):
    """DescribeSecIndex返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 欄位值，如下：
AttackIpCount：受攻擊的IP數
AttackCount：攻擊次數
BlockCount：封堵次數
MaxMbps：攻擊峰值Mbps
IpNum：統計的IP數據
        :type Data: list of KeyValue
        :param BeginDate: 本月開始時間
        :type BeginDate: str
        :param EndDate: 本月結束時間
        :type EndDate: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.BeginDate = None
        self.EndDate = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self.Data.append(obj)
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")
        self.RequestId = params.get("RequestId")


class DescribeSourceIpSegmentRequest(AbstractModel):
    """DescribeSourceIpSegment請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        """
        self.Business = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")


class DescribeSourceIpSegmentResponse(AbstractModel):
    """DescribeSourceIpSegment返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 回源IP段，多個用"；"分隔
        :type Data: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeTransmitStatisRequest(AbstractModel):
    """DescribeTransmitStatis請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版；bgp表示獨享包；bgp-multip表示共享包）
        :type Business: str
        :param Id: 資源實例ID
        :type Id: str
        :param MetricName: 指标名，取值：
traffic表示流量頻寬；
pkg表示包速率；
        :type MetricName: str
        :param Period: 統計時間粒度（300表示5分鍾；3600表示小時；86400表示天）
        :type Period: int
        :param StartTime: 統計開始時間，秒部分保持爲0，分鍾部分爲5的倍數
        :type StartTime: str
        :param EndTime: 統計結束時間，秒部分保持爲0，分鍾部分爲5的倍數
        :type EndTime: str
        :param IpList: 資源的IP（當Business爲bgp-multip時必填，且僅支援一個IP）；當不填寫時，預設統計資源實例的所有IP；資源實例有多個IP（比如高防IP專業版）時，統計方式是求和；
        :type IpList: list of str
        """
        self.Business = None
        self.Id = None
        self.MetricName = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.IpList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.MetricName = params.get("MetricName")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.IpList = params.get("IpList")


class DescribeTransmitStatisResponse(AbstractModel):
    """DescribeTransmitStatis返回參數結構體

    """

    def __init__(self):
        """
        :param InDataList: 當MetricName=traffic時，表示入流量頻寬，單位bps；
當MetricName=pkg時，表示入包速率，單位pps；
        :type InDataList: list of float
        :param OutDataList: 當MetricName=traffic時，表示出流量頻寬，單位bps；
當MetricName=pkg時，表示出包速率，單位pps；
        :type OutDataList: list of float
        :param MetricName: 指标名：
traffic表示流量頻寬；
pkg表示包速率；
        :type MetricName: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InDataList = None
        self.OutDataList = None
        self.MetricName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InDataList = params.get("InDataList")
        self.OutDataList = params.get("OutDataList")
        self.MetricName = params.get("MetricName")
        self.RequestId = params.get("RequestId")


class DescribeUnBlockStatisRequest(AbstractModel):
    """DescribeUnBlockStatis請求參數結構體

    """


class DescribeUnBlockStatisResponse(AbstractModel):
    """DescribeUnBlockStatis返回參數結構體

    """

    def __init__(self):
        """
        :param Total: 解封總配額數
        :type Total: int
        :param Used: 已使用次數
        :type Used: int
        :param BeginTime: 統計起始時間
        :type BeginTime: str
        :param EndTime: 統計結束時間
        :type EndTime: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Used = None
        self.BeginTime = None
        self.EndTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        self.Used = params.get("Used")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.RequestId = params.get("RequestId")


class DescribleL4RulesRequest(AbstractModel):
    """DescribleL4Rules請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param RuleIdList: 規則ID，可選參數，填寫後獲取指定的規則
        :type RuleIdList: list of str
        :param Limit: 一頁條數，填0表示不分頁
        :type Limit: int
        :param Offset: 頁起始偏移，取值爲(頁碼-1)*一頁條數
        :type Offset: int
        """
        self.Business = None
        self.Id = None
        self.RuleIdList = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleIdList = params.get("RuleIdList")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribleL4RulesResponse(AbstractModel):
    """DescribleL4Rules返回參數結構體

    """

    def __init__(self):
        """
        :param Rules: 轉發規則清單
        :type Rules: list of L4RuleEntry
        :param Total: 總規則數
        :type Total: int
        :param Healths: 健康檢查配置清單
        :type Healths: list of L4RuleHealth
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Rules = None
        self.Total = None
        self.Healths = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = L4RuleEntry()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Total = params.get("Total")
        if params.get("Healths") is not None:
            self.Healths = []
            for item in params.get("Healths"):
                obj = L4RuleHealth()
                obj._deserialize(item)
                self.Healths.append(obj)
        self.RequestId = params.get("RequestId")


class DescribleL7RulesRequest(AbstractModel):
    """DescribleL7Rules請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param RuleIdList: 規則ID，可選參數，填寫後獲取指定的規則
        :type RuleIdList: list of str
        :param Limit: 一頁條數，填0表示不分頁
        :type Limit: int
        :param Offset: 頁起始偏移，取值爲(頁碼-1)*一頁條數
        :type Offset: int
        :param Domain: 域名搜索，選填，當需要搜索域名請填寫
        :type Domain: str
        :param ProtocolList: 轉發協議搜索，選填，取值[http, https, http/https]
        :type ProtocolList: list of str
        :param StatusList: 狀态搜索，選填，取值[0(規則配置成功)，1(規則配置生效中)，2(規則配置失敗)，3(規則删除生效中)，5(規則删除失敗)，6(規則等待配置)，7(規則等待删除)，8(規則待配置證書)]
        :type StatusList: list of int non-negative
        """
        self.Business = None
        self.Id = None
        self.RuleIdList = None
        self.Limit = None
        self.Offset = None
        self.Domain = None
        self.ProtocolList = None
        self.StatusList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleIdList = params.get("RuleIdList")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Domain = params.get("Domain")
        self.ProtocolList = params.get("ProtocolList")
        self.StatusList = params.get("StatusList")


class DescribleL7RulesResponse(AbstractModel):
    """DescribleL7Rules返回參數結構體

    """

    def __init__(self):
        """
        :param Rules: 轉發規則清單
        :type Rules: list of L7RuleEntry
        :param Total: 總規則數
        :type Total: int
        :param Healths: 健康檢查配置清單
        :type Healths: list of L7RuleHealth
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Rules = None
        self.Total = None
        self.Healths = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = L7RuleEntry()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Total = params.get("Total")
        if params.get("Healths") is not None:
            self.Healths = []
            for item in params.get("Healths"):
                obj = L7RuleHealth()
                obj._deserialize(item)
                self.Healths.append(obj)
        self.RequestId = params.get("RequestId")


class DescribleNewL7RulesRequest(AbstractModel):
    """DescribleNewL7Rules請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP）
        :type Business: str
        :param Limit: 一頁條數，填0表示不分頁
        :type Limit: int
        :param Offset: 頁起始偏移，取值爲(頁碼-1)*一頁條數
        :type Offset: int
        :param Domain: 域名搜索，選填，當需要搜索域名請填寫
        :type Domain: str
        :param ProtocolList: 轉發協議搜索，選填，取值[http, https, http/https]
        :type ProtocolList: list of str
        :param StatusList: 狀态搜索，選填，取值[0(規則配置成功)，1(規則配置生效中)，2(規則配置失敗)，3(規則删除生效中)，5(規則删除失敗)，6(規則等待配置)，7(規則等待删除)，8(規則待配置證書)]
        :type StatusList: list of int non-negative
        :param Ip: IP搜索，選填，當需要搜索IP請填寫
        :type Ip: str
        """
        self.Business = None
        self.Limit = None
        self.Offset = None
        self.Domain = None
        self.ProtocolList = None
        self.StatusList = None
        self.Ip = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Domain = params.get("Domain")
        self.ProtocolList = params.get("ProtocolList")
        self.StatusList = params.get("StatusList")
        self.Ip = params.get("Ip")


class DescribleNewL7RulesResponse(AbstractModel):
    """DescribleNewL7Rules返回參數結構體

    """

    def __init__(self):
        """
        :param Rules: 轉發規則清單
        :type Rules: list of NewL7RuleEntry
        :param Total: 總規則數
        :type Total: int
        :param Healths: 健康檢查配置清單
        :type Healths: list of L7RuleHealth
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Rules = None
        self.Total = None
        self.Healths = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = NewL7RuleEntry()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Total = params.get("Total")
        if params.get("Healths") is not None:
            self.Healths = []
            for item in params.get("Healths"):
                obj = L7RuleHealth()
                obj._deserialize(item)
                self.Healths.append(obj)
        self.RequestId = params.get("RequestId")


class DescribleRegionCountRequest(AbstractModel):
    """DescribleRegionCount請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；）
        :type Business: str
        :param LineList: 根據線路統計，取值爲[1（BGP線路），2（南京電信），3（南京聯通），99（第三方合作線路）]；只對高防IP産品有效，其他産品此欄位忽略
        :type LineList: list of int non-negative
        """
        self.Business = None
        self.LineList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.LineList = params.get("LineList")


class DescribleRegionCountResponse(AbstractModel):
    """DescribleRegionCount返回參數結構體

    """

    def __init__(self):
        """
        :param RegionList: 地域資源實例數
        :type RegionList: list of RegionInstanceCount
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RegionList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionList") is not None:
            self.RegionList = []
            for item in params.get("RegionList"):
                obj = RegionInstanceCount()
                obj._deserialize(item)
                self.RegionList.append(obj)
        self.RequestId = params.get("RequestId")


class IpBlackWhite(AbstractModel):
    """黑白IP

    """

    def __init__(self):
        """
        :param Ip: IP網址
        :type Ip: str
        :param Type: 黑白類型，取值範圍[black，white]
        :type Type: str
        """
        self.Ip = None
        self.Type = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Type = params.get("Type")


class IpBlockData(AbstractModel):
    """IP封堵記錄

    """

    def __init__(self):
        """
        :param Ip: IP
        :type Ip: str
        :param Status: 狀态（Blocked：被封堵；UnBlocking：解封中；UnBlockFailed：解封失敗）
        :type Status: str
        :param BlockTime: 封堵時間
        :type BlockTime: str
        :param UnBlockTime: 解封時間（預計解封時間）
        :type UnBlockTime: str
        :param ActionType: 解封類型（user：自助解封；auto：自動解封； update：升級解封；bind：綁定高防包解封）
        :type ActionType: str
        """
        self.Ip = None
        self.Status = None
        self.BlockTime = None
        self.UnBlockTime = None
        self.ActionType = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Status = params.get("Status")
        self.BlockTime = params.get("BlockTime")
        self.UnBlockTime = params.get("UnBlockTime")
        self.ActionType = params.get("ActionType")


class IpUnBlockData(AbstractModel):
    """IP解封記錄

    """

    def __init__(self):
        """
        :param Ip: IP
        :type Ip: str
        :param BlockTime: 封堵時間
        :type BlockTime: str
        :param UnBlockTime: 解封時間（實際解封時間）
        :type UnBlockTime: str
        :param ActionType: 解封類型（user：自助解封；auto：自動解封； update：升級解封；bind：綁定高防包解封）
        :type ActionType: str
        """
        self.Ip = None
        self.BlockTime = None
        self.UnBlockTime = None
        self.ActionType = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.BlockTime = params.get("BlockTime")
        self.UnBlockTime = params.get("UnBlockTime")
        self.ActionType = params.get("ActionType")


class KeyValue(AbstractModel):
    """欄位值，K-V形式

    """

    def __init__(self):
        """
        :param Key: 欄位名稱
        :type Key: str
        :param Value: 欄位取值
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class KeyValueRecord(AbstractModel):
    """KeyValue記錄

    """

    def __init__(self):
        """
        :param Record: 一條記錄的Key-Value數組
        :type Record: list of KeyValue
        """
        self.Record = None


    def _deserialize(self, params):
        if params.get("Record") is not None:
            self.Record = []
            for item in params.get("Record"):
                obj = KeyValue()
                obj._deserialize(item)
                self.Record.append(obj)


class L4DelRule(AbstractModel):
    """删除l4規則介面

    """

    def __init__(self):
        """
        :param Id: 資源Id
        :type Id: str
        :param Ip: 資源IP
        :type Ip: str
        :param RuleIdList: 規則Id
        :type RuleIdList: list of str
        """
        self.Id = None
        self.Ip = None
        self.RuleIdList = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.RuleIdList = params.get("RuleIdList")


class L4HealthConfig(AbstractModel):
    """四層健康檢查配置

    """

    def __init__(self):
        """
        :param Protocol: 轉發協議，取值[TCP, UDP]
        :type Protocol: str
        :param VirtualPort: 轉發端口
        :type VirtualPort: int
        :param Enable: =1表示開啓；=0表示關閉
        :type Enable: int
        :param TimeOut: 響應超時時間，單位秒
        :type TimeOut: int
        :param Interval: 檢測間隔時間，單位秒
        :type Interval: int
        :param KickNum: 不健康阈值，單位次
        :type KickNum: int
        :param AliveNum: 健康阈值，單位次
        :type AliveNum: int
        :param KeepTime: 會話保持時間，單位秒
        :type KeepTime: int
        """
        self.Protocol = None
        self.VirtualPort = None
        self.Enable = None
        self.TimeOut = None
        self.Interval = None
        self.KickNum = None
        self.AliveNum = None
        self.KeepTime = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.VirtualPort = params.get("VirtualPort")
        self.Enable = params.get("Enable")
        self.TimeOut = params.get("TimeOut")
        self.Interval = params.get("Interval")
        self.KickNum = params.get("KickNum")
        self.AliveNum = params.get("AliveNum")
        self.KeepTime = params.get("KeepTime")


class L4RuleEntry(AbstractModel):
    """L4規則

    """

    def __init__(self):
        """
        :param Protocol: 轉發協議，取值[TCP, UDP]
        :type Protocol: str
        :param VirtualPort: 轉發端口
        :type VirtualPort: int
        :param SourcePort: 源站端口
        :type SourcePort: int
        :param SourceType: 回源方式，取值[1(域名回源)，2(IP回源)]
        :type SourceType: int
        :param KeepTime: 會話保持時間，單位秒
        :type KeepTime: int
        :param SourceList: 回源清單
        :type SourceList: list of L4RuleSource
        :param LbType: 負載均衡方式，取值[1(加權輪詢)，2(源IP hash)]
        :type LbType: int
        :param KeepEnable: 會話保持開關，取值[0(會話保持關閉)，1(會話保持開啓)]；
        :type KeepEnable: int
        :param RuleId: 規則ID
        :type RuleId: str
        :param RuleName: 規則描述
        :type RuleName: str
        :param RemoveSwitch: 移除浮水印狀态，取值[0(關閉)，1(開啓)]
        :type RemoveSwitch: int
        """
        self.Protocol = None
        self.VirtualPort = None
        self.SourcePort = None
        self.SourceType = None
        self.KeepTime = None
        self.SourceList = None
        self.LbType = None
        self.KeepEnable = None
        self.RuleId = None
        self.RuleName = None
        self.RemoveSwitch = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.VirtualPort = params.get("VirtualPort")
        self.SourcePort = params.get("SourcePort")
        self.SourceType = params.get("SourceType")
        self.KeepTime = params.get("KeepTime")
        if params.get("SourceList") is not None:
            self.SourceList = []
            for item in params.get("SourceList"):
                obj = L4RuleSource()
                obj._deserialize(item)
                self.SourceList.append(obj)
        self.LbType = params.get("LbType")
        self.KeepEnable = params.get("KeepEnable")
        self.RuleId = params.get("RuleId")
        self.RuleName = params.get("RuleName")
        self.RemoveSwitch = params.get("RemoveSwitch")


class L4RuleHealth(AbstractModel):
    """規則健康檢查參數

    """

    def __init__(self):
        """
        :param RuleId: 規則ID
        :type RuleId: str
        :param Enable: =1表示開啓；=0表示關閉
        :type Enable: int
        :param TimeOut: 響應超時時間，單位秒
        :type TimeOut: int
        :param Interval: 檢測間隔時間，單位秒，必須要大于響應超時時間
        :type Interval: int
        :param KickNum: 不健康阈值，單位次
        :type KickNum: int
        :param AliveNum: 健康阈值，單位次
        :type AliveNum: int
        """
        self.RuleId = None
        self.Enable = None
        self.TimeOut = None
        self.Interval = None
        self.KickNum = None
        self.AliveNum = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.Enable = params.get("Enable")
        self.TimeOut = params.get("TimeOut")
        self.Interval = params.get("Interval")
        self.KickNum = params.get("KickNum")
        self.AliveNum = params.get("AliveNum")


class L4RuleSource(AbstractModel):
    """L4規則回源清單

    """

    def __init__(self):
        """
        :param Source: 回源IP或域名
        :type Source: str
        :param Weight: 權重值，取值[0,100]
        :type Weight: int
        """
        self.Source = None
        self.Weight = None


    def _deserialize(self, params):
        self.Source = params.get("Source")
        self.Weight = params.get("Weight")


class L7HealthConfig(AbstractModel):
    """七層健康檢查配置

    """

    def __init__(self):
        """
        :param Protocol: 轉發協議，取值[http, https, http/https]
        :type Protocol: str
        :param Domain: 轉發域名
        :type Domain: str
        :param Enable: =1表示開啓；=0表示關閉
        :type Enable: int
        :param Interval: 檢測間隔時間，單位秒
        :type Interval: int
        :param KickNum: 異常判定次數，單位次
        :type KickNum: int
        :param AliveNum: 健康判定次數，單位次
        :type AliveNum: int
        :param Method: 健康檢查探測方法，可選HEAD或GET，預設爲HEAD
        :type Method: str
        :param StatusCode: 健康檢查判定正常狀态碼，1xx =1, 2xx=2, 3xx=4, 4xx=8,5xx=16，多個狀态碼值加和
        :type StatusCode: int
        :param Url: 檢查目錄的URL，預設爲/
        :type Url: str
        """
        self.Protocol = None
        self.Domain = None
        self.Enable = None
        self.Interval = None
        self.KickNum = None
        self.AliveNum = None
        self.Method = None
        self.StatusCode = None
        self.Url = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Domain = params.get("Domain")
        self.Enable = params.get("Enable")
        self.Interval = params.get("Interval")
        self.KickNum = params.get("KickNum")
        self.AliveNum = params.get("AliveNum")
        self.Method = params.get("Method")
        self.StatusCode = params.get("StatusCode")
        self.Url = params.get("Url")


class L7RuleEntry(AbstractModel):
    """L7規則

    """

    def __init__(self):
        """
        :param Protocol: 轉發協議，取值[http, https]
        :type Protocol: str
        :param Domain: 轉發域名
        :type Domain: str
        :param SourceType: 回源方式，取值[1(域名回源)，2(IP回源)]
        :type SourceType: int
        :param KeepTime: 會話保持時間，單位秒
        :type KeepTime: int
        :param SourceList: 回源清單
        :type SourceList: list of L4RuleSource
        :param LbType: 負載均衡方式，取值[1(加權輪詢)]
        :type LbType: int
        :param KeepEnable: 會話保持開關，取值[0(會話保持關閉)，1(會話保持開啓)]
        :type KeepEnable: int
        :param RuleId: 規則ID，當添加新規則時可以不用填寫此欄位；當修改或者删除規則時需要填寫此欄位；
        :type RuleId: str
        :param CertType: 證書來源，當轉發協議爲https時必須填，取值[2(Top Cloud 托管證書)]，當轉發協議爲http時也可以填0
        :type CertType: int
        :param SSLId: 當證書來源爲Top Cloud 托管證書時，此欄位必須填寫托管證書ID
        :type SSLId: str
        :param Cert: 當證書來源爲自有證書時，此欄位必須填寫證書内容；(因已不再支援自有證書，此欄位已棄用，請不用填寫此欄位)
        :type Cert: str
        :param PrivateKey: 當證書來源爲自有證書時，此欄位必須填寫證書金鑰；(因已不再支援自有證書，此欄位已棄用，請不用填寫此欄位)
        :type PrivateKey: str
        :param RuleName: 規則描述
        :type RuleName: str
        :param Status: 規則狀态，取值[0(規則配置成功)，1(規則配置生效中)，2(規則配置失敗)，3(規則删除生效中)，5(規則删除失敗)，6(規則等待配置)，7(規則等待删除)，8(規則待配置證書)]
        :type Status: int
        :param CCStatus: cc防護狀态，取值[0(關閉), 1(開啓)]
        :type CCStatus: int
        :param CCEnable: HTTPS協議的CC防護狀态，取值[0(關閉), 1(開啓)]
        :type CCEnable: int
        :param CCThreshold: HTTPS協議的CC防護阈值
        :type CCThreshold: int
        :param CCLevel: HTTPS協議的CC防護等級
        :type CCLevel: str
        :param HttpsToHttpEnable: 是否開啓Https協議使用Http回源，取值[0(關閉), 1(開啓)]，不填寫預設是關閉
注意：此欄位可能返回 null，表示取不到有效值。
        :type HttpsToHttpEnable: int
        """
        self.Protocol = None
        self.Domain = None
        self.SourceType = None
        self.KeepTime = None
        self.SourceList = None
        self.LbType = None
        self.KeepEnable = None
        self.RuleId = None
        self.CertType = None
        self.SSLId = None
        self.Cert = None
        self.PrivateKey = None
        self.RuleName = None
        self.Status = None
        self.CCStatus = None
        self.CCEnable = None
        self.CCThreshold = None
        self.CCLevel = None
        self.HttpsToHttpEnable = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Domain = params.get("Domain")
        self.SourceType = params.get("SourceType")
        self.KeepTime = params.get("KeepTime")
        if params.get("SourceList") is not None:
            self.SourceList = []
            for item in params.get("SourceList"):
                obj = L4RuleSource()
                obj._deserialize(item)
                self.SourceList.append(obj)
        self.LbType = params.get("LbType")
        self.KeepEnable = params.get("KeepEnable")
        self.RuleId = params.get("RuleId")
        self.CertType = params.get("CertType")
        self.SSLId = params.get("SSLId")
        self.Cert = params.get("Cert")
        self.PrivateKey = params.get("PrivateKey")
        self.RuleName = params.get("RuleName")
        self.Status = params.get("Status")
        self.CCStatus = params.get("CCStatus")
        self.CCEnable = params.get("CCEnable")
        self.CCThreshold = params.get("CCThreshold")
        self.CCLevel = params.get("CCLevel")
        self.HttpsToHttpEnable = params.get("HttpsToHttpEnable")


class L7RuleHealth(AbstractModel):
    """L7規則健康檢查參數

    """

    def __init__(self):
        """
        :param RuleId: 規則ID
        :type RuleId: str
        :param Enable: =1表示開啓；=0表示關閉
        :type Enable: int
        :param Interval: 檢測間隔時間，單位秒
        :type Interval: int
        :param KickNum: 不健康阈值，單位次
        :type KickNum: int
        :param AliveNum: 健康阈值，單位次
        :type AliveNum: int
        :param Method: HTTP請求方式，取值[HEAD,GET]
        :type Method: str
        :param StatusCode: 健康檢查判定正常狀态碼，1xx =1, 2xx=2, 3xx=4, 4xx=8,5xx=16，多個狀态碼值加和
        :type StatusCode: int
        :param Url: 檢查目錄的URL，預設爲/
        :type Url: str
        :param Status: 配置狀态，0： 正常，1：配置中，2：配置失敗
        :type Status: int
        """
        self.RuleId = None
        self.Enable = None
        self.Interval = None
        self.KickNum = None
        self.AliveNum = None
        self.Method = None
        self.StatusCode = None
        self.Url = None
        self.Status = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.Enable = params.get("Enable")
        self.Interval = params.get("Interval")
        self.KickNum = params.get("KickNum")
        self.AliveNum = params.get("AliveNum")
        self.Method = params.get("Method")
        self.StatusCode = params.get("StatusCode")
        self.Url = params.get("Url")
        self.Status = params.get("Status")


class ModifyCCAlarmThresholdRequest(AbstractModel):
    """ModifyCCAlarmThreshold請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（shield表示棋牌；bgpip表示高防IP；bgp表示高防包；bgp-multip表示多ip高防包；net表示高防IP專業版）
        :type Business: str
        :param RsId: 資源ID,字串類型
        :type RsId: str
        :param AlarmThreshold: 告警阈值，大于0（目前排定的值），後台設置預設值爲1000
        :type AlarmThreshold: int
        :param IpList: 資源關聯的IP清單，高防包未綁定時，傳空數組，高防IP專業版傳多個IP的數據
        :type IpList: list of str
        """
        self.Business = None
        self.RsId = None
        self.AlarmThreshold = None
        self.IpList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.RsId = params.get("RsId")
        self.AlarmThreshold = params.get("AlarmThreshold")
        self.IpList = params.get("IpList")


class ModifyCCAlarmThresholdResponse(AbstractModel):
    """ModifyCCAlarmThreshold返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyCCFrequencyRulesRequest(AbstractModel):
    """ModifyCCFrequencyRules請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param CCFrequencyRuleId: CC的訪問頻率控制規則ID
        :type CCFrequencyRuleId: str
        :param Mode: 比對規則，取值["include"(前綴比對)，"equal"(完全比對)]
        :type Mode: str
        :param Period: 統計週期，單位秒，取值[10, 30, 60]
        :type Period: int
        :param ReqNumber: 訪問次數，取值[1-10000]
        :type ReqNumber: int
        :param Act: 執行動作，取值["alg"（人機識别）, "drop"（攔截）]
        :type Act: str
        :param ExeDuration: 執行時間，單位秒，取值[1-900]
        :type ExeDuration: int
        :param Uri: URI字串，必須以/開頭，例如/abc/a.php，長度不超過31；當URI=/時，比對模式只能選擇前綴比對；
        :type Uri: str
        :param UserAgent: User-Agent字串，長度不超過80
        :type UserAgent: str
        :param Cookie: Cookie字串，長度不超過40
        :type Cookie: str
        """
        self.Business = None
        self.CCFrequencyRuleId = None
        self.Mode = None
        self.Period = None
        self.ReqNumber = None
        self.Act = None
        self.ExeDuration = None
        self.Uri = None
        self.UserAgent = None
        self.Cookie = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.CCFrequencyRuleId = params.get("CCFrequencyRuleId")
        self.Mode = params.get("Mode")
        self.Period = params.get("Period")
        self.ReqNumber = params.get("ReqNumber")
        self.Act = params.get("Act")
        self.ExeDuration = params.get("ExeDuration")
        self.Uri = params.get("Uri")
        self.UserAgent = params.get("UserAgent")
        self.Cookie = params.get("Cookie")


class ModifyCCFrequencyRulesResponse(AbstractModel):
    """ModifyCCFrequencyRules返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyCCFrequencyRulesStatusRequest(AbstractModel):
    """ModifyCCFrequencyRulesStatus請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param RuleId: 7層轉發規則ID（通過獲取7層轉發規則介面可以獲取規則ID）
        :type RuleId: str
        :param Method: 開啓或關閉，取值["on"(開啓)，"off"(關閉)]
        :type Method: str
        """
        self.Business = None
        self.Id = None
        self.RuleId = None
        self.Method = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleId = params.get("RuleId")
        self.Method = params.get("Method")


class ModifyCCFrequencyRulesStatusResponse(AbstractModel):
    """ModifyCCFrequencyRulesStatus返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyCCHostProtectionRequest(AbstractModel):
    """ModifyCCHostProtection請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param RuleId: 規則ID
        :type RuleId: str
        :param Method: 開啓/關閉CC域名防護，取值[open(表示開啓)，close(表示關閉)]
        :type Method: str
        """
        self.Business = None
        self.Id = None
        self.RuleId = None
        self.Method = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleId = params.get("RuleId")
        self.Method = params.get("Method")


class ModifyCCHostProtectionResponse(AbstractModel):
    """ModifyCCHostProtection返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyCCIpAllowDenyRequest(AbstractModel):
    """ModifyCCIpAllowDeny請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param Method: add表示添加，delete表示删除
        :type Method: str
        :param Type: 黑/白名單類型；取值[white(白名單)，black(黑名單)]
        :type Type: str
        :param IpList: 黑/白名單的IP數組
        :type IpList: list of str
        :param Protocol: 可選欄位，代表CC防護類型，取值[http（HTTP協議的CC防護），https（HTTPS協議的CC防護）]；當不填時，預設爲HTTP協議的CC防護；當填寫https時還需要填寫Domain和RuleId欄位；
        :type Protocol: str
        :param Domain: 可選欄位，表示HTTPS協議的7層轉發規則域名（通過獲取7層轉發規則介面可以獲取域名），只有當Protocol欄位爲https時才必須填寫此欄位；
        :type Domain: str
        :param RuleId: 可選欄位，表示HTTPS協議的7層轉發規則ID（通過獲取7層轉發規則介面可以獲取規則ID），
當Method爲delete時，不用填寫此欄位；
        :type RuleId: str
        """
        self.Business = None
        self.Id = None
        self.Method = None
        self.Type = None
        self.IpList = None
        self.Protocol = None
        self.Domain = None
        self.RuleId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Method = params.get("Method")
        self.Type = params.get("Type")
        self.IpList = params.get("IpList")
        self.Protocol = params.get("Protocol")
        self.Domain = params.get("Domain")
        self.RuleId = params.get("RuleId")


class ModifyCCIpAllowDenyResponse(AbstractModel):
    """ModifyCCIpAllowDeny返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyCCLevelRequest(AbstractModel):
    """ModifyCCLevel請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param Level: CC防護等級，取值[default(正常), loose(寬松), strict(嚴格)];
        :type Level: str
        :param Protocol: 可選欄位，代表CC防護類型，取值[http（HTTP協議的CC防護），https（HTTPS協議的CC防護）]；當不填時，預設爲HTTP協議的CC防護；當填寫https時還需要填寫RuleId欄位；
        :type Protocol: str
        :param RuleId: 表示7層轉發規則ID（通過獲取7層轉發規則介面可以獲取規則ID）；
        :type RuleId: str
        """
        self.Business = None
        self.Id = None
        self.Level = None
        self.Protocol = None
        self.RuleId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Level = params.get("Level")
        self.Protocol = params.get("Protocol")
        self.RuleId = params.get("RuleId")


class ModifyCCLevelResponse(AbstractModel):
    """ModifyCCLevel返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyCCPolicySwitchRequest(AbstractModel):
    """ModifyCCPolicySwitch請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param SetId: 策略ID
        :type SetId: str
        :param Switch: 開關狀态
        :type Switch: int
        """
        self.Business = None
        self.Id = None
        self.SetId = None
        self.Switch = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.SetId = params.get("SetId")
        self.Switch = params.get("Switch")


class ModifyCCPolicySwitchResponse(AbstractModel):
    """ModifyCCPolicySwitch返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyCCSelfDefinePolicyRequest(AbstractModel):
    """ModifyCCSelfDefinePolicy請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param SetId: 策略ID
        :type SetId: str
        :param Policy: CC策略描述
        :type Policy: :class:`tencentcloud.dayu.v20180709.models.CCPolicy`
        """
        self.Business = None
        self.Id = None
        self.SetId = None
        self.Policy = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.SetId = params.get("SetId")
        if params.get("Policy") is not None:
            self.Policy = CCPolicy()
            self.Policy._deserialize(params.get("Policy"))


class ModifyCCSelfDefinePolicyResponse(AbstractModel):
    """ModifyCCSelfDefinePolicy返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyCCThresholdRequest(AbstractModel):
    """ModifyCCThreshold請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版；basic表示基礎防護）
        :type Business: str
        :param Threshold: CC防護阈值，取值(0 100 150 240 350 480 550 700 850 1000 1500 2000 3000 5000 10000 20000);
當Business爲高防IP、高防IP專業版時，其CC防護最大阈值跟資源的保底防護頻寬有關，對應關系如下：
  保底頻寬: 最大C防護阈值
  10:  20000,
  20:  40000,
  30:  70000,
  40:  100000,
  50:  150000,
  60:  200000,
  80:  250000,
  100: 300000,
        :type Threshold: int
        :param Id: 資源ID
        :type Id: str
        :param Protocol: 可選欄位，代表CC防護類型，取值[http（HTTP協議的CC防護），https（HTTPS協議的CC防護）]；當不填時，預設爲HTTP協議的CC防護；當填寫https時還需要填寫RuleId欄位；
        :type Protocol: str
        :param RuleId: 可選欄位，表示HTTPS協議的7層轉發規則ID（通過獲取7層轉發規則介面可以獲取規則ID）；
當Protocol=https時必須填寫；
        :type RuleId: str
        :param BasicIp: 查詢的IP網址（僅基礎防護提供），取值如：1.1.1.1
        :type BasicIp: str
        :param BasicRegion: 查詢IP所屬地域（僅基礎防護提供），取值如：gz、bj、sh、hk等地域縮寫
        :type BasicRegion: str
        :param BasicBizType: 專區類型（僅基礎防護提供），取值如：公有雲專區：public，黑石專區：bm, NAT服務器專區：nat，網際網路通道：channel。
        :type BasicBizType: str
        :param BasicDeviceType: 設備類型（僅基礎防護提供），取值如：服務器：cvm，公有雲負載均衡：clb，黑石負載均衡：lb，NAT服務器：nat，網際網路通道：channel.
        :type BasicDeviceType: str
        :param BasicIpInstance: 僅基礎防護提供。可選，IPInstance Nat 閘道（如果查詢的設備類型是NAT服務器，需要傳此參數，通過nat資源查詢介面獲取）
        :type BasicIpInstance: str
        :param BasicIspCode: 僅基礎防護提供。可選，運營商線路（如果查詢的設備類型是NAT服務器，需要傳此參數爲5）
        :type BasicIspCode: int
        """
        self.Business = None
        self.Threshold = None
        self.Id = None
        self.Protocol = None
        self.RuleId = None
        self.BasicIp = None
        self.BasicRegion = None
        self.BasicBizType = None
        self.BasicDeviceType = None
        self.BasicIpInstance = None
        self.BasicIspCode = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Threshold = params.get("Threshold")
        self.Id = params.get("Id")
        self.Protocol = params.get("Protocol")
        self.RuleId = params.get("RuleId")
        self.BasicIp = params.get("BasicIp")
        self.BasicRegion = params.get("BasicRegion")
        self.BasicBizType = params.get("BasicBizType")
        self.BasicDeviceType = params.get("BasicDeviceType")
        self.BasicIpInstance = params.get("BasicIpInstance")
        self.BasicIspCode = params.get("BasicIspCode")


class ModifyCCThresholdResponse(AbstractModel):
    """ModifyCCThreshold返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyCCUrlAllowRequest(AbstractModel):
    """ModifyCCUrlAllow請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param Method: =add表示添加，=delete表示删除
        :type Method: str
        :param Type: 黑/白名單類型；取值[white(白名單)]
        :type Type: str
        :param UrlList: URL數組，URL格式如下：
http://域名/cgi
https://域名/cgi
        :type UrlList: list of str
        :param Protocol: 可選欄位，代表CC防護類型，取值[http（HTTP協議的CC防護），https（HTTPS協議的CC防護）]；當不填時，預設爲HTTP協議的CC防護；當填寫https時還需要填寫Domain和RuleId欄位；
        :type Protocol: str
        :param Domain: 可選欄位，表示HTTPS協議的7層轉發規則域名（通過獲取7層轉發規則介面可以獲取域名），只有當Protocol欄位爲https時才必須填寫此欄位；
        :type Domain: str
        :param RuleId: 可選欄位，表示HTTPS協議的7層轉發規則ID（通過獲取7層轉發規則介面可以獲取規則ID），當添加并且Protocol=https時必須填寫；
當Method爲delete時，可以不用填寫此欄位；
        :type RuleId: str
        """
        self.Business = None
        self.Id = None
        self.Method = None
        self.Type = None
        self.UrlList = None
        self.Protocol = None
        self.Domain = None
        self.RuleId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Method = params.get("Method")
        self.Type = params.get("Type")
        self.UrlList = params.get("UrlList")
        self.Protocol = params.get("Protocol")
        self.Domain = params.get("Domain")
        self.RuleId = params.get("RuleId")


class ModifyCCUrlAllowResponse(AbstractModel):
    """ModifyCCUrlAllow返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyDDoSAIStatusRequest(AbstractModel):
    """ModifyDDoSAIStatus請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param Method: =get表示讀取AI防護狀态；=set表示修改AI防護狀态；
        :type Method: str
        :param DDoSAI: AI防護狀态，取值[on，off]；當Method=set時必填；
        :type DDoSAI: str
        """
        self.Business = None
        self.Id = None
        self.Method = None
        self.DDoSAI = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Method = params.get("Method")
        self.DDoSAI = params.get("DDoSAI")


class ModifyDDoSAIStatusResponse(AbstractModel):
    """ModifyDDoSAIStatus返回參數結構體

    """

    def __init__(self):
        """
        :param DDoSAI: AI防護狀态，取值[on，off]
        :type DDoSAI: str
        :param Id: 資源ID
        :type Id: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DDoSAI = None
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DDoSAI = params.get("DDoSAI")
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class ModifyDDoSAlarmThresholdRequest(AbstractModel):
    """ModifyDDoSAlarmThreshold請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（shield表示棋牌；bgpip表示高防IP；bgp表示高防包；bgp-multip表示多ip高防包；net表示高防IP專業版）
        :type Business: str
        :param RsId: 資源ID,字串類型
        :type RsId: str
        :param AlarmType: 告警阈值類型，0-未設置，1-入流量，2-清洗流量
        :type AlarmType: int
        :param AlarmThreshold: 告警阈值，大于0（目前暫定的值）
        :type AlarmThreshold: int
        :param IpList: 資源關聯的IP清單，高防包未綁定時，傳空數組，高防IP專業版傳多個IP的數據
        :type IpList: list of str
        """
        self.Business = None
        self.RsId = None
        self.AlarmType = None
        self.AlarmThreshold = None
        self.IpList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.RsId = params.get("RsId")
        self.AlarmType = params.get("AlarmType")
        self.AlarmThreshold = params.get("AlarmThreshold")
        self.IpList = params.get("IpList")


class ModifyDDoSAlarmThresholdResponse(AbstractModel):
    """ModifyDDoSAlarmThreshold返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyDDoSDefendStatusRequest(AbstractModel):
    """ModifyDDoSDefendStatus請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgp表示獨享包；bgp-multip表示共享包；bgpip表示高防IP；net表示高防IP專業版；basic表示基礎防護）
        :type Business: str
        :param Status: 防護狀态值，取值[0（關閉），1（開啓）]
        :type Status: int
        :param Hour: 關閉時長，單位小時，取值[0，1，2，3，4，5，6]；當Status=0表示關閉時，Hour必須大于0；
        :type Hour: int
        :param Id: 資源ID；當Business不是基礎防護時必須填寫此欄位；
        :type Id: str
        :param Ip: 基礎防護的IP，只有當Business爲基礎防護時才需要填寫此欄位；
        :type Ip: str
        :param BizType: 只有當Business爲基礎防護時才需要填寫此欄位，IP所屬的産品類型，取值[public（CVM産品），bm（黑石産品），eni（彈性網卡），vpngw（VPN閘道）， natgw（NAT閘道），waf（Web應用安全産品），fpc（金融産品），gaap（GAAP産品）, other(托管IP)]
        :type BizType: str
        :param DeviceType: 只有當Business爲基礎防護時才需要填寫此欄位，IP所屬的産品子類，取值[cvm（CVM），lb（負載均衡器），eni（彈性網卡），vpngw（VPN），natgw（NAT），waf（WAF），fpc（金融），gaap（GAAP），other（托管IP），eip（黑石彈性IP）]
        :type DeviceType: str
        :param InstanceId: 只有當Business爲基礎防護時才需要填寫此欄位，IP所屬的資源實例ID，當綁定新IP時必須填寫此欄位；例如是彈性網卡的IP，則InstanceId填寫彈性網卡的ID(eni-*);
        :type InstanceId: str
        :param IPRegion: 只有當Business爲基礎防護時才需要填寫此欄位，表示IP所屬的地域，取值：
"bj":     華北地區(北京)
"cd":     西南地區(成都)
"cq":     西南地區(重慶)
"gz":     華南地區(廣州)
"gzopen": 華南地區(廣州Open)
"hk":     中國香港
"kr":     東南亞地區(首爾)
"sh":     華東地區(上海)
"shjr":   華東地區(上海金融)
"szjr":   華南地區(深圳金融)
"sg":     東南亞地區(新加坡)
"th":     東南亞地區(泰國)
"de":     歐洲地區(德國)
"usw":    美國西部（矽谷）
"ca":     北美地區(多倫多)
"jp":     日本
"hzec":   杭州
"in":     印度
"use":    美東地區（弗吉尼亞）
"ru":     俄羅斯
"tpe":    中國台灣
"nj":     南京
        :type IPRegion: str
        """
        self.Business = None
        self.Status = None
        self.Hour = None
        self.Id = None
        self.Ip = None
        self.BizType = None
        self.DeviceType = None
        self.InstanceId = None
        self.IPRegion = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Status = params.get("Status")
        self.Hour = params.get("Hour")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.BizType = params.get("BizType")
        self.DeviceType = params.get("DeviceType")
        self.InstanceId = params.get("InstanceId")
        self.IPRegion = params.get("IPRegion")


class ModifyDDoSDefendStatusResponse(AbstractModel):
    """ModifyDDoSDefendStatus返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyDDoSLevelRequest(AbstractModel):
    """ModifyDDoSLevel請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param Method: =get表示讀取防護等級；=set表示修改防護等級
        :type Method: str
        :param DDoSLevel: 防護等級，取值[low,middle,high]；當Method=set時必填
        :type DDoSLevel: str
        """
        self.Business = None
        self.Id = None
        self.Method = None
        self.DDoSLevel = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Method = params.get("Method")
        self.DDoSLevel = params.get("DDoSLevel")


class ModifyDDoSLevelResponse(AbstractModel):
    """ModifyDDoSLevel返回參數結構體

    """

    def __init__(self):
        """
        :param Id: 資源ID
        :type Id: str
        :param DDoSLevel: 防護等級，取值[low,middle,high]
        :type DDoSLevel: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.DDoSLevel = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.DDoSLevel = params.get("DDoSLevel")
        self.RequestId = params.get("RequestId")


class ModifyDDoSPolicyCaseRequest(AbstractModel):
    """ModifyDDoSPolicyCase請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param SceneId: 策略場景ID
        :type SceneId: str
        :param PlatformTypes: 開發平台，取值[PC（PC用戶端）， MOBILE（移動端）， TV（電視端）， SERVER（主機）]
        :type PlatformTypes: list of str
        :param AppType: 細分品類，取值[WEB（網站）， GAME（遊戲）， APP（應用）， OTHER（其他）]
        :type AppType: str
        :param AppProtocols: 應用協議，取值[tcp（TCP協議），udp（UDP協議），icmp（ICMP協議），all（其他協議）]
        :type AppProtocols: list of str
        :param TcpSportStart: TCP業務起始端口，取值(0, 65535]
        :type TcpSportStart: str
        :param TcpSportEnd: TCP業務結束端口，取值(0, 65535]，必須大于等于TCP業務起始端口
        :type TcpSportEnd: str
        :param UdpSportStart: UDP業務起始端口，取值範圍(0, 65535]
        :type UdpSportStart: str
        :param UdpSportEnd: UDP業務結束端口，取值範圍(0, 65535)，必須大于等于UDP業務起始端口
        :type UdpSportEnd: str
        :param HasAbroad: 是否有海外客戶，取值[no（沒有）, yes（有）]
        :type HasAbroad: str
        :param HasInitiateTcp: 是否會主動對外發起TCP請求，取值[no（不會）, yes（會）]
        :type HasInitiateTcp: str
        :param HasInitiateUdp: 是否會主動對外發起UDP業務請求，取值[no（不會）, yes（會）]
        :type HasInitiateUdp: str
        :param PeerTcpPort: 主動發起TCP請求的端口，取值範圍(0, 65535]
        :type PeerTcpPort: str
        :param PeerUdpPort: 主動發起UDP請求的端口，取值範圍(0, 65535]
        :type PeerUdpPort: str
        :param TcpFootprint: TCP載荷的固定特征碼，字串長度小於512
        :type TcpFootprint: str
        :param UdpFootprint: UDP載荷的固定特征碼，字串長度小於512
        :type UdpFootprint: str
        :param WebApiUrl: Web業務的API的URL
        :type WebApiUrl: list of str
        :param MinTcpPackageLen: TCP業務報文長度最小值，取值範圍(0, 1500)
        :type MinTcpPackageLen: str
        :param MaxTcpPackageLen: TCP業務報文長度最大值，取值範圍(0, 1500)，必須大于等于TCP業務報文長度最小值
        :type MaxTcpPackageLen: str
        :param MinUdpPackageLen: UDP業務報文長度最小值，取值範圍(0, 1500)
        :type MinUdpPackageLen: str
        :param MaxUdpPackageLen: UDP業務報文長度最大值，取值範圍(0, 1500)，必須大于等于UDP業務報文長度最小值
        :type MaxUdpPackageLen: str
        :param HasVPN: 是否有VPN業務，取值[no（沒有）, yes（有）]
        :type HasVPN: str
        :param TcpPortList: TCP業務端口清單，同時支援單個端口和端口段，字串格式，例如：80,443,700-800,53,1000-3000
        :type TcpPortList: str
        :param UdpPortList: UDP業務端口清單，同時支援單個端口和端口段，字串格式，例如：80,443,700-800,53,1000-3000
        :type UdpPortList: str
        """
        self.Business = None
        self.SceneId = None
        self.PlatformTypes = None
        self.AppType = None
        self.AppProtocols = None
        self.TcpSportStart = None
        self.TcpSportEnd = None
        self.UdpSportStart = None
        self.UdpSportEnd = None
        self.HasAbroad = None
        self.HasInitiateTcp = None
        self.HasInitiateUdp = None
        self.PeerTcpPort = None
        self.PeerUdpPort = None
        self.TcpFootprint = None
        self.UdpFootprint = None
        self.WebApiUrl = None
        self.MinTcpPackageLen = None
        self.MaxTcpPackageLen = None
        self.MinUdpPackageLen = None
        self.MaxUdpPackageLen = None
        self.HasVPN = None
        self.TcpPortList = None
        self.UdpPortList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.SceneId = params.get("SceneId")
        self.PlatformTypes = params.get("PlatformTypes")
        self.AppType = params.get("AppType")
        self.AppProtocols = params.get("AppProtocols")
        self.TcpSportStart = params.get("TcpSportStart")
        self.TcpSportEnd = params.get("TcpSportEnd")
        self.UdpSportStart = params.get("UdpSportStart")
        self.UdpSportEnd = params.get("UdpSportEnd")
        self.HasAbroad = params.get("HasAbroad")
        self.HasInitiateTcp = params.get("HasInitiateTcp")
        self.HasInitiateUdp = params.get("HasInitiateUdp")
        self.PeerTcpPort = params.get("PeerTcpPort")
        self.PeerUdpPort = params.get("PeerUdpPort")
        self.TcpFootprint = params.get("TcpFootprint")
        self.UdpFootprint = params.get("UdpFootprint")
        self.WebApiUrl = params.get("WebApiUrl")
        self.MinTcpPackageLen = params.get("MinTcpPackageLen")
        self.MaxTcpPackageLen = params.get("MaxTcpPackageLen")
        self.MinUdpPackageLen = params.get("MinUdpPackageLen")
        self.MaxUdpPackageLen = params.get("MaxUdpPackageLen")
        self.HasVPN = params.get("HasVPN")
        self.TcpPortList = params.get("TcpPortList")
        self.UdpPortList = params.get("UdpPortList")


class ModifyDDoSPolicyCaseResponse(AbstractModel):
    """ModifyDDoSPolicyCase返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyDDoSPolicyNameRequest(AbstractModel):
    """ModifyDDoSPolicyName請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param PolicyId: 策略ID
        :type PolicyId: str
        :param Name: 策略名稱
        :type Name: str
        """
        self.Business = None
        self.PolicyId = None
        self.Name = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.PolicyId = params.get("PolicyId")
        self.Name = params.get("Name")


class ModifyDDoSPolicyNameResponse(AbstractModel):
    """ModifyDDoSPolicyName返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyDDoSPolicyRequest(AbstractModel):
    """ModifyDDoSPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param PolicyId: 策略ID
        :type PolicyId: str
        :param DropOptions: 協議禁用，必須填寫且數組長度必須爲1
        :type DropOptions: list of DDoSPolicyDropOption
        :param PortLimits: 端口禁用，當沒有禁用端口時填空數組
        :type PortLimits: list of DDoSPolicyPortLimit
        :param IpAllowDenys: IP黑白名單，當沒有IP黑白名單時填空數組
        :type IpAllowDenys: list of IpBlackWhite
        :param PacketFilters: 報文過濾，當沒有報文過濾時填空數組
        :type PacketFilters: list of DDoSPolicyPacketFilter
        :param WaterPrint: 浮水印策略參數，當沒有啓用水印功能時填空數組，最多只能傳一條水印策略（即數組大小不超過1）
        :type WaterPrint: list of WaterPrintPolicy
        """
        self.Business = None
        self.PolicyId = None
        self.DropOptions = None
        self.PortLimits = None
        self.IpAllowDenys = None
        self.PacketFilters = None
        self.WaterPrint = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.PolicyId = params.get("PolicyId")
        if params.get("DropOptions") is not None:
            self.DropOptions = []
            for item in params.get("DropOptions"):
                obj = DDoSPolicyDropOption()
                obj._deserialize(item)
                self.DropOptions.append(obj)
        if params.get("PortLimits") is not None:
            self.PortLimits = []
            for item in params.get("PortLimits"):
                obj = DDoSPolicyPortLimit()
                obj._deserialize(item)
                self.PortLimits.append(obj)
        if params.get("IpAllowDenys") is not None:
            self.IpAllowDenys = []
            for item in params.get("IpAllowDenys"):
                obj = IpBlackWhite()
                obj._deserialize(item)
                self.IpAllowDenys.append(obj)
        if params.get("PacketFilters") is not None:
            self.PacketFilters = []
            for item in params.get("PacketFilters"):
                obj = DDoSPolicyPacketFilter()
                obj._deserialize(item)
                self.PacketFilters.append(obj)
        if params.get("WaterPrint") is not None:
            self.WaterPrint = []
            for item in params.get("WaterPrint"):
                obj = WaterPrintPolicy()
                obj._deserialize(item)
                self.WaterPrint.append(obj)


class ModifyDDoSPolicyResponse(AbstractModel):
    """ModifyDDoSPolicy返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyDDoSSwitchRequest(AbstractModel):
    """ModifyDDoSSwitch請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（basic表示基礎防護）
        :type Business: str
        :param Method: =get表示讀取DDoS防護狀态；=set表示修改DDoS防護狀态；
        :type Method: str
        :param Ip: 基礎防護的IP，只有當Business爲基礎防護時才需要填寫此欄位；
        :type Ip: str
        :param BizType: 只有當Business爲基礎防護時才需要填寫此欄位，IP所屬的産品類型，取值[public（CVM産品），bm（黑石産品），eni（彈性網卡），vpngw（VPN閘道）， natgw（NAT閘道），waf（Web應用安全産品），fpc（金融産品），gaap（GAAP産品）, other(托管IP)]
        :type BizType: str
        :param DeviceType: 只有當Business爲基礎防護時才需要填寫此欄位，IP所屬的産品子類，取值[cvm（CVM），lb（負載均衡器），eni（彈性網卡），vpngw（VPN），natgw（NAT），waf（WAF），fpc（金融），gaap（GAAP），other（托管IP），eip（黑石彈性IP）]
        :type DeviceType: str
        :param InstanceId: 只有當Business爲基礎防護時才需要填寫此欄位，IP所屬的資源實例ID，當綁定新IP時必須填寫此欄位；例如是彈性網卡的IP，則InstanceId填寫彈性網卡的ID(eni-*);
        :type InstanceId: str
        :param IPRegion: 只有當Business爲基礎防護時才需要填寫此欄位，表示IP所屬的地域，取值：
"bj":     華北地區(北京)
"cd":     西南地區(成都)
"cq":     西南地區(重慶)
"gz":     華南地區(廣州)
"gzopen": 華南地區(廣州Open)
"hk":     中國香港
"kr":     東南亞地區(首爾)
"sh":     華東地區(上海)
"shjr":   華東地區(上海金融)
"szjr":   華南地區(深圳金融)
"sg":     東南亞地區(新加坡)
"th":     東南亞地區(泰國)
"de":     歐洲地區(德國)
"usw":    美國西部（矽谷）
"ca":     北美地區(多倫多)
"jp":     日本
"hzec":   杭州
"in":     印度
"use":    美東地區（弗吉尼亞）
"ru":     俄羅斯
"tpe":    中國台灣
"nj":     南京
        :type IPRegion: str
        :param Status: 可選欄位，防護狀态值，取值[0（關閉），1（開啓）]；當Method爲get時可以不填寫此欄位；
        :type Status: int
        """
        self.Business = None
        self.Method = None
        self.Ip = None
        self.BizType = None
        self.DeviceType = None
        self.InstanceId = None
        self.IPRegion = None
        self.Status = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Method = params.get("Method")
        self.Ip = params.get("Ip")
        self.BizType = params.get("BizType")
        self.DeviceType = params.get("DeviceType")
        self.InstanceId = params.get("InstanceId")
        self.IPRegion = params.get("IPRegion")
        self.Status = params.get("Status")


class ModifyDDoSSwitchResponse(AbstractModel):
    """ModifyDDoSSwitch返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 當前防護狀态值，取值[0（關閉），1（開啓）]
        :type Status: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ModifyDDoSThresholdRequest(AbstractModel):
    """ModifyDDoSThreshold請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param Threshold: DDoS清洗阈值，取值[0, 60, 80, 100, 150, 200, 250, 300, 400, 500, 700, 1000];
當設置值爲0時，表示采用預設值；
        :type Threshold: int
        """
        self.Business = None
        self.Id = None
        self.Threshold = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Threshold = params.get("Threshold")


class ModifyDDoSThresholdResponse(AbstractModel):
    """ModifyDDoSThreshold返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyDDoSWaterKeyRequest(AbstractModel):
    """ModifyDDoSWaterKey請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param PolicyId: 策略ID
        :type PolicyId: str
        :param Method: 金鑰操作，取值：[add（添加），delete（删除），open（開啓），close（關閉），get（獲取金鑰）]
        :type Method: str
        :param KeyId: 金鑰ID，當添加金鑰操作時可以不填或填0，其他操作時必須填寫；
        :type KeyId: int
        """
        self.Business = None
        self.PolicyId = None
        self.Method = None
        self.KeyId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.PolicyId = params.get("PolicyId")
        self.Method = params.get("Method")
        self.KeyId = params.get("KeyId")


class ModifyDDoSWaterKeyResponse(AbstractModel):
    """ModifyDDoSWaterKey返回參數結構體

    """

    def __init__(self):
        """
        :param KeyList: 浮水印金鑰清單
        :type KeyList: list of WaterPrintKey
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.KeyList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KeyList") is not None:
            self.KeyList = []
            for item in params.get("KeyList"):
                obj = WaterPrintKey()
                obj._deserialize(item)
                self.KeyList.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyElasticLimitRequest(AbstractModel):
    """ModifyElasticLimit請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param Limit: 彈性防護阈值，取值[0 10000 20000 30000 40000 50000 60000 70000 80000 90000 100000 120000 150000 200000 250000 300000 400000 600000 800000 220000 310000 110000 270000 610000]
        :type Limit: int
        """
        self.Business = None
        self.Id = None
        self.Limit = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Limit = params.get("Limit")


class ModifyElasticLimitResponse(AbstractModel):
    """ModifyElasticLimit返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyL4HealthRequest(AbstractModel):
    """ModifyL4Health請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param Healths: 健康檢查參數數組
        :type Healths: list of L4RuleHealth
        """
        self.Business = None
        self.Id = None
        self.Healths = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Healths") is not None:
            self.Healths = []
            for item in params.get("Healths"):
                obj = L4RuleHealth()
                obj._deserialize(item)
                self.Healths.append(obj)


class ModifyL4HealthResponse(AbstractModel):
    """ModifyL4Health返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyL4KeepTimeRequest(AbstractModel):
    """ModifyL4KeepTime請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param RuleId: 規則ID
        :type RuleId: str
        :param KeepEnable: 會話保持開關，取值[0(會話保持關閉)，1(會話保持開啓)]
        :type KeepEnable: int
        :param KeepTime: 會話保持時間，單位秒
        :type KeepTime: int
        """
        self.Business = None
        self.Id = None
        self.RuleId = None
        self.KeepEnable = None
        self.KeepTime = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RuleId = params.get("RuleId")
        self.KeepEnable = params.get("KeepEnable")
        self.KeepTime = params.get("KeepTime")


class ModifyL4KeepTimeResponse(AbstractModel):
    """ModifyL4KeepTime返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyL4RulesRequest(AbstractModel):
    """ModifyL4Rules請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param Rule: 規則
        :type Rule: :class:`tencentcloud.dayu.v20180709.models.L4RuleEntry`
        """
        self.Business = None
        self.Id = None
        self.Rule = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Rule") is not None:
            self.Rule = L4RuleEntry()
            self.Rule._deserialize(params.get("Rule"))


class ModifyL4RulesResponse(AbstractModel):
    """ModifyL4Rules返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyL7RulesRequest(AbstractModel):
    """ModifyL7Rules請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param Rule: 規則
        :type Rule: :class:`tencentcloud.dayu.v20180709.models.L7RuleEntry`
        """
        self.Business = None
        self.Id = None
        self.Rule = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Rule") is not None:
            self.Rule = L7RuleEntry()
            self.Rule._deserialize(params.get("Rule"))


class ModifyL7RulesResponse(AbstractModel):
    """ModifyL7Rules返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyNetReturnSwitchRequest(AbstractModel):
    """ModifyNetReturnSwitch請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（net表示高防IP專業版）
        :type Business: str
        :param Id: 資源實例ID
        :type Id: str
        :param Status: Status 表示回切開關，0: 關閉， 1:打開
        :type Status: int
        :param Hour: 回切時長，單位：小時，取值[0,1,2,3,4,5,6;]當status=1時必選填寫Hour>0
        :type Hour: int
        """
        self.Business = None
        self.Id = None
        self.Status = None
        self.Hour = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.Status = params.get("Status")
        self.Hour = params.get("Hour")


class ModifyNetReturnSwitchResponse(AbstractModel):
    """ModifyNetReturnSwitch返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyResBindDDoSPolicyRequest(AbstractModel):
    """ModifyResBindDDoSPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；bgp表示獨享包；bgp-multip表示共享包；net表示高防IP專業版）
        :type Business: str
        :param Id: 資源ID
        :type Id: str
        :param PolicyId: 策略ID
        :type PolicyId: str
        :param Method: 綁定或解綁，bind表示綁定策略，unbind表示解綁策略
        :type Method: str
        """
        self.Business = None
        self.Id = None
        self.PolicyId = None
        self.Method = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.PolicyId = params.get("PolicyId")
        self.Method = params.get("Method")


class ModifyResBindDDoSPolicyResponse(AbstractModel):
    """ModifyResBindDDoSPolicy返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyResourceRenewFlagRequest(AbstractModel):
    """ModifyResourceRenewFlag請求參數結構體

    """

    def __init__(self):
        """
        :param Business: 大禹子産品代号（bgpip表示高防IP；net表示高防IP專業版；shield表示棋牌盾；bgp表示獨享包；bgp-multip表示共享包；insurance表示保險包；staticpack表示三網套餐包）
        :type Business: str
        :param Id: 資源Id
        :type Id: str
        :param RenewFlag: 自動續約标記（0手動續約；1自動續約；2到期不續約）
        :type RenewFlag: int
        """
        self.Business = None
        self.Id = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        self.RenewFlag = params.get("RenewFlag")


class ModifyResourceRenewFlagResponse(AbstractModel):
    """ModifyResourceRenewFlag返回參數結構體

    """

    def __init__(self):
        """
        :param Success: 成功碼
        :type Success: :class:`tencentcloud.dayu.v20180709.models.SuccessCode`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class NewL4RuleEntry(AbstractModel):
    """四層規則結構體

    """

    def __init__(self):
        """
        :param Protocol: 轉發協議，取值[TCP, UDP]
        :type Protocol: str
        :param VirtualPort: 轉發端口
        :type VirtualPort: int
        :param SourcePort: 源站端口
        :type SourcePort: int
        :param KeepTime: 會話保持時間，單位秒
        :type KeepTime: int
        :param SourceList: 回源清單
        :type SourceList: list of L4RuleSource
        :param LbType: 負載均衡方式，取值[1(加權輪詢)，2(源IP hash)]
        :type LbType: int
        :param KeepEnable: 會話保持開關，取值[0(會話保持關閉)，1(會話保持開啓)]；
        :type KeepEnable: int
        :param SourceType: 回源方式，取值[1(域名回源)，2(IP回源)]
        :type SourceType: int
        :param RuleId: 規則ID
        :type RuleId: str
        :param RuleName: 規則描述
        :type RuleName: str
        :param RemoveSwitch: 移除浮水印狀态，取值[0(關閉)，1(開啓)]
        :type RemoveSwitch: int
        :param ModifyTime: 規則修改時間
        :type ModifyTime: str
        :param Region: 對應地區訊息
        :type Region: int
        :param Ip: 綁定資源IP訊息
        :type Ip: str
        :param Id: 綁定資源Id訊息
        :type Id: str
        """
        self.Protocol = None
        self.VirtualPort = None
        self.SourcePort = None
        self.KeepTime = None
        self.SourceList = None
        self.LbType = None
        self.KeepEnable = None
        self.SourceType = None
        self.RuleId = None
        self.RuleName = None
        self.RemoveSwitch = None
        self.ModifyTime = None
        self.Region = None
        self.Ip = None
        self.Id = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.VirtualPort = params.get("VirtualPort")
        self.SourcePort = params.get("SourcePort")
        self.KeepTime = params.get("KeepTime")
        if params.get("SourceList") is not None:
            self.SourceList = []
            for item in params.get("SourceList"):
                obj = L4RuleSource()
                obj._deserialize(item)
                self.SourceList.append(obj)
        self.LbType = params.get("LbType")
        self.KeepEnable = params.get("KeepEnable")
        self.SourceType = params.get("SourceType")
        self.RuleId = params.get("RuleId")
        self.RuleName = params.get("RuleName")
        self.RemoveSwitch = params.get("RemoveSwitch")
        self.ModifyTime = params.get("ModifyTime")
        self.Region = params.get("Region")
        self.Ip = params.get("Ip")
        self.Id = params.get("Id")


class NewL7RuleEntry(AbstractModel):
    """L7規則

    """

    def __init__(self):
        """
        :param Protocol: 轉發協議，取值[http, https]
        :type Protocol: str
        :param Domain: 轉發域名
        :type Domain: str
        :param SourceType: 回源方式，取值[1(域名回源)，2(IP回源)]
        :type SourceType: int
        :param KeepTime: 會話保持時間，單位秒
        :type KeepTime: int
        :param SourceList: 回源清單
        :type SourceList: list of L4RuleSource
        :param LbType: 負載均衡方式，取值[1(加權輪詢)]
        :type LbType: int
        :param KeepEnable: 會話保持開關，取值[0(會話保持關閉)，1(會話保持開啓)]
        :type KeepEnable: int
        :param RuleId: 規則ID，當添加新規則時可以不用填寫此欄位；當修改或者删除規則時需要填寫此欄位；
        :type RuleId: str
        :param CertType: 證書來源，當轉發協議爲https時必須填，取值[2(Top Cloud 托管證書)]，當轉發協議爲http時也可以填0
        :type CertType: int
        :param SSLId: 當證書來源爲Top Cloud 托管證書時，此欄位必須填寫托管證書ID
        :type SSLId: str
        :param Cert: 當證書來源爲自有證書時，此欄位必須填寫證書内容；(因已不再支援自有證書，此欄位已棄用，請不用填寫此欄位)
        :type Cert: str
        :param PrivateKey: 當證書來源爲自有證書時，此欄位必須填寫證書金鑰；(因已不再支援自有證書，此欄位已棄用，請不用填寫此欄位)
        :type PrivateKey: str
        :param RuleName: 規則描述
        :type RuleName: str
        :param Status: 規則狀态，取值[0(規則配置成功)，1(規則配置生效中)，2(規則配置失敗)，3(規則删除生效中)，5(規則删除失敗)，6(規則等待配置)，7(規則等待删除)，8(規則待配置證書)]
        :type Status: int
        :param CCStatus: cc防護狀态，取值[0(關閉), 1(開啓)]
        :type CCStatus: int
        :param CCEnable: HTTPS協議的CC防護狀态，取值[0(關閉), 1(開啓)]
        :type CCEnable: int
        :param CCThreshold: HTTPS協議的CC防護阈值
        :type CCThreshold: int
        :param CCLevel: HTTPS協議的CC防護等級
        :type CCLevel: str
        :param Region: 區域碼
        :type Region: int
        :param Id: 資源Id
        :type Id: str
        :param Ip: 資源Ip
        :type Ip: str
        :param ModifyTime: 修改時間
        :type ModifyTime: str
        :param HttpsToHttpEnable: 是否開啓Https協議使用Http回源，取值[0(關閉), 1(開啓)]，不填寫預設是關閉
        :type HttpsToHttpEnable: int
        """
        self.Protocol = None
        self.Domain = None
        self.SourceType = None
        self.KeepTime = None
        self.SourceList = None
        self.LbType = None
        self.KeepEnable = None
        self.RuleId = None
        self.CertType = None
        self.SSLId = None
        self.Cert = None
        self.PrivateKey = None
        self.RuleName = None
        self.Status = None
        self.CCStatus = None
        self.CCEnable = None
        self.CCThreshold = None
        self.CCLevel = None
        self.Region = None
        self.Id = None
        self.Ip = None
        self.ModifyTime = None
        self.HttpsToHttpEnable = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Domain = params.get("Domain")
        self.SourceType = params.get("SourceType")
        self.KeepTime = params.get("KeepTime")
        if params.get("SourceList") is not None:
            self.SourceList = []
            for item in params.get("SourceList"):
                obj = L4RuleSource()
                obj._deserialize(item)
                self.SourceList.append(obj)
        self.LbType = params.get("LbType")
        self.KeepEnable = params.get("KeepEnable")
        self.RuleId = params.get("RuleId")
        self.CertType = params.get("CertType")
        self.SSLId = params.get("SSLId")
        self.Cert = params.get("Cert")
        self.PrivateKey = params.get("PrivateKey")
        self.RuleName = params.get("RuleName")
        self.Status = params.get("Status")
        self.CCStatus = params.get("CCStatus")
        self.CCEnable = params.get("CCEnable")
        self.CCThreshold = params.get("CCThreshold")
        self.CCLevel = params.get("CCLevel")
        self.Region = params.get("Region")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.ModifyTime = params.get("ModifyTime")
        self.HttpsToHttpEnable = params.get("HttpsToHttpEnable")


class OrderBy(AbstractModel):
    """排序欄位

    """

    def __init__(self):
        """
        :param Field: 排序欄位名稱，取值[
bandwidth（頻寬），
overloadCount（超峰值次數）
]
        :type Field: str
        :param Order: 升降序，取值爲[asc（升序），（升序），desc（降序）， DESC（降序）]
        :type Order: str
        """
        self.Field = None
        self.Order = None


    def _deserialize(self, params):
        self.Field = params.get("Field")
        self.Order = params.get("Order")


class Paging(AbstractModel):
    """分頁索引

    """

    def __init__(self):
        """
        :param Offset: 起始位置
        :type Offset: int
        :param Limit: 數量
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class ProtocolPort(AbstractModel):
    """Protocol、Port參數

    """

    def __init__(self):
        """
        :param Protocol: 協議（tcp；udp）
        :type Protocol: str
        :param Port: 端口
        :type Port: int
        """
        self.Protocol = None
        self.Port = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")


class RegionInstanceCount(AbstractModel):
    """地域資源實例數

    """

    def __init__(self):
        """
        :param Region: 地域碼
        :type Region: str
        :param RegionV3: 地域碼（新規範）
        :type RegionV3: str
        :param Count: 資源實例數
        :type Count: int
        """
        self.Region = None
        self.RegionV3 = None
        self.Count = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionV3 = params.get("RegionV3")
        self.Count = params.get("Count")


class ResourceIp(AbstractModel):
    """資源的IP數組

    """

    def __init__(self):
        """
        :param Id: 資源ID
        :type Id: str
        :param IpList: 資源的IP數組
        :type IpList: list of str
        """
        self.Id = None
        self.IpList = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.IpList = params.get("IpList")


class SchedulingDomain(AbstractModel):
    """調度域名訊息

    """

    def __init__(self):
        """
        :param Domain: 調度域名
        :type Domain: str
        :param BGPIpList: BGP線路IP清單
        :type BGPIpList: list of str
        :param CTCCIpList: 電信線路IP清單
        :type CTCCIpList: list of str
        :param CUCCIpList: 聯通線路IP清單
        :type CUCCIpList: list of str
        :param CMCCIpList: 移動線路IP清單
        :type CMCCIpList: list of str
        :param OverseaIpList: 海外線路IP清單
        :type OverseaIpList: list of str
        :param Method: 調度方式，當前僅支援優先級, 取值爲priority
        :type Method: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param TTL: ttl
        :type TTL: int
        :param Status: 狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: int
        :param ModifyTime: 修改時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        """
        self.Domain = None
        self.BGPIpList = None
        self.CTCCIpList = None
        self.CUCCIpList = None
        self.CMCCIpList = None
        self.OverseaIpList = None
        self.Method = None
        self.CreateTime = None
        self.TTL = None
        self.Status = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.BGPIpList = params.get("BGPIpList")
        self.CTCCIpList = params.get("CTCCIpList")
        self.CUCCIpList = params.get("CUCCIpList")
        self.CMCCIpList = params.get("CMCCIpList")
        self.OverseaIpList = params.get("OverseaIpList")
        self.Method = params.get("Method")
        self.CreateTime = params.get("CreateTime")
        self.TTL = params.get("TTL")
        self.Status = params.get("Status")
        self.ModifyTime = params.get("ModifyTime")


class SuccessCode(AbstractModel):
    """操作返回碼，只用于返回成功的情況

    """

    def __init__(self):
        """
        :param Code: 成功/錯誤碼
        :type Code: str
        :param Message: 描述
        :type Message: str
        """
        self.Code = None
        self.Message = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")


class WaterPrintKey(AbstractModel):
    """浮水印Key

    """

    def __init__(self):
        """
        :param KeyId: 浮水印KeyID
        :type KeyId: str
        :param KeyContent: 浮水印Key值
        :type KeyContent: str
        :param KeyVersion: 浮水印Key的版本号
        :type KeyVersion: str
        :param OpenStatus: 是否開啓，取值[0（沒有開啓），1（已開啓）]
        :type OpenStatus: int
        :param CreateTime: 金鑰生成時間
        :type CreateTime: str
        """
        self.KeyId = None
        self.KeyContent = None
        self.KeyVersion = None
        self.OpenStatus = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.KeyContent = params.get("KeyContent")
        self.KeyVersion = params.get("KeyVersion")
        self.OpenStatus = params.get("OpenStatus")
        self.CreateTime = params.get("CreateTime")


class WaterPrintPolicy(AbstractModel):
    """浮水印策略參數

    """

    def __init__(self):
        """
        :param TcpPortList: TCP端口段，例如["2000-3000","3500-4000"]
        :type TcpPortList: list of str
        :param UdpPortList: UDP端口段，例如["2000-3000","3500-4000"]
        :type UdpPortList: list of str
        :param Offset: 浮水印偏移量，取值範圍[0, 100)
        :type Offset: int
        :param RemoveSwitch: 是否自動剝離，取值[0（不自動剝離），1（自動剝離）]
        :type RemoveSwitch: int
        :param OpenStatus: 是否開啓，取值[0（沒有開啓），1（已開啓）]
        :type OpenStatus: int
        """
        self.TcpPortList = None
        self.UdpPortList = None
        self.Offset = None
        self.RemoveSwitch = None
        self.OpenStatus = None


    def _deserialize(self, params):
        self.TcpPortList = params.get("TcpPortList")
        self.UdpPortList = params.get("UdpPortList")
        self.Offset = params.get("Offset")
        self.RemoveSwitch = params.get("RemoveSwitch")
        self.OpenStatus = params.get("OpenStatus")