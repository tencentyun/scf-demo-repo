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


class BindL4Backend(AbstractModel):
    """待與四層監聽器綁定的物理機主機、虛拟機或半托管主機訊息。目前一個四層監聽器下面最多允許綁定255個主機端口。

    """

    def __init__(self):
        """
        :param Port: 待綁定的主機端口，可選值1~65535。
        :type Port: int
        :param InstanceId: 待綁定的黑石物理機主機ID、虛拟機IP或者是半托管主機ID。
        :type InstanceId: str
        :param Weight: 待綁定的主機權重，可選值0~100。
        :type Weight: int
        :param ProbePort: 自定義探測的主機端口，可選值1~65535。（需要監聽器開啓自定義健康檢查）
        :type ProbePort: int
        """
        self.Port = None
        self.InstanceId = None
        self.Weight = None
        self.ProbePort = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")
        self.ProbePort = params.get("ProbePort")


class BindL4BackendsRequest(AbstractModel):
    """BindL4Backends請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID，可通過介面DescribeLoadBalancers查詢。
        :type LoadBalancerId: str
        :param ListenerId: 四層監聽器實例ID，可通過介面DescribeL4Listeners查詢。
        :type ListenerId: str
        :param BackendSet: 待綁定的主機訊息。可以綁定多個主機端口。目前一個四層監聽器下面最多允許綁定255個主機端口。
        :type BackendSet: list of BindL4Backend
        :param BindType: 綁定類型。0：物理機 1：虛拟機 2：半托管機器
        :type BindType: int
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.BackendSet = None
        self.BindType = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("BackendSet") is not None:
            self.BackendSet = []
            for item in params.get("BackendSet"):
                obj = BindL4Backend()
                obj._deserialize(item)
                self.BackendSet.append(obj)
        self.BindType = params.get("BindType")


class BindL4BackendsResponse(AbstractModel):
    """BindL4Backends返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID。該介面爲異步任務，可根據本參數調用DescribeLoadBalancerTaskResult介面來查詢任務操作結果。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class BindL7Backend(AbstractModel):
    """待與七層監聽器轉發規則綁定的物理機主機、虛拟機或半托管主機訊息。目前一個七層轉發路徑下面最多允許綁定255個主機端口。

    """

    def __init__(self):
        """
        :param Port: 待綁定的主機端口，可選值1~65535。
        :type Port: int
        :param InstanceId: 黑石物理機主機ID、虛拟機IP或者是半托管主機ID。
        :type InstanceId: str
        :param Weight: 待綁定的主機權重，可選值0~100。
        :type Weight: int
        """
        self.Port = None
        self.InstanceId = None
        self.Weight = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")


class BindL7BackendsRequest(AbstractModel):
    """BindL7Backends請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID，可通過介面DescribeLoadBalancers查詢。
        :type LoadBalancerId: str
        :param ListenerId: 七層監聽器實例ID，可通過介面DescribeL7Listeners查詢。
        :type ListenerId: str
        :param DomainId: 轉發域名實例ID，可通過介面DescribeL7Rules查詢。
        :type DomainId: str
        :param LocationId: 轉發路徑實例ID，可通過介面DescribeL7Rules查詢。
        :type LocationId: str
        :param BackendSet: 待綁定的主機訊息。可以綁定多個主機端口。目前一個七層轉發路徑下面最多允許綁定255個主機端口。
        :type BackendSet: list of BindL7Backend
        :param BindType: 綁定類型。0：物理機，1：虛拟機 2：半托管機器。
        :type BindType: int
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.DomainId = None
        self.LocationId = None
        self.BackendSet = None
        self.BindType = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.DomainId = params.get("DomainId")
        self.LocationId = params.get("LocationId")
        if params.get("BackendSet") is not None:
            self.BackendSet = []
            for item in params.get("BackendSet"):
                obj = BindL7Backend()
                obj._deserialize(item)
                self.BackendSet.append(obj)
        self.BindType = params.get("BindType")


class BindL7BackendsResponse(AbstractModel):
    """BindL7Backends返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID。該介面爲異步任務，可根據本參數調用DescribeLoadBalancerTaskResult介面來查詢任務操作結果。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class BindTrafficMirrorListenersRequest(AbstractModel):
    """BindTrafficMirrorListeners請求參數結構體

    """

    def __init__(self):
        """
        :param TrafficMirrorId: 流量映像實例ID。
        :type TrafficMirrorId: str
        :param ListenerIds: 七層監聽器實例ID數組，可通過介面DescribeL7Listeners查詢。
        :type ListenerIds: list of str
        """
        self.TrafficMirrorId = None
        self.ListenerIds = None


    def _deserialize(self, params):
        self.TrafficMirrorId = params.get("TrafficMirrorId")
        self.ListenerIds = params.get("ListenerIds")


class BindTrafficMirrorListenersResponse(AbstractModel):
    """BindTrafficMirrorListeners返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID。該介面爲異步任務，可根據本參數調用DescribeLoadBalancerTaskResult介面來查詢任務操作結果。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class BindTrafficMirrorReceiver(AbstractModel):
    """待與流量映像綁定的接收機訊息。

    """

    def __init__(self):
        """
        :param Port: 待綁定的主機端口，可選值1~65535。
        :type Port: int
        :param InstanceId: 待綁定的主機實例ID。
        :type InstanceId: str
        :param Weight: 待綁定的主機權重，可選值0~100。
        :type Weight: int
        """
        self.Port = None
        self.InstanceId = None
        self.Weight = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")


class BindTrafficMirrorReceiversRequest(AbstractModel):
    """BindTrafficMirrorReceivers請求參數結構體

    """

    def __init__(self):
        """
        :param TrafficMirrorId: 流量映像實例ID。
        :type TrafficMirrorId: str
        :param ReceiverSet: 待綁定的黑石物理機訊息數組。
        :type ReceiverSet: list of BindTrafficMirrorReceiver
        """
        self.TrafficMirrorId = None
        self.ReceiverSet = None


    def _deserialize(self, params):
        self.TrafficMirrorId = params.get("TrafficMirrorId")
        if params.get("ReceiverSet") is not None:
            self.ReceiverSet = []
            for item in params.get("ReceiverSet"):
                obj = BindTrafficMirrorReceiver()
                obj._deserialize(item)
                self.ReceiverSet.append(obj)


class BindTrafficMirrorReceiversResponse(AbstractModel):
    """BindTrafficMirrorReceivers返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID。該介面爲異步任務，可根據本參數調用DescribeLoadBalancerTaskResult介面來查詢任務操作結果。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CertDetailLoadBalancer(AbstractModel):
    """獲驗證書訊息時返回的所用在的負載均衡訊息。

    """

    def __init__(self):
        """
        :param LoadBalancerId: 黑石負載均衡實例ID。
        :type LoadBalancerId: str
        :param LoadBalancerName: 黑石負載均衡實例名稱。
        :type LoadBalancerName: str
        :param VpcId: 該黑石負載均衡所在的VpcId。
        :type VpcId: str
        :param RegionId: 該黑石負載均衡所在的regionId。
        :type RegionId: int
        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.VpcId = None
        self.RegionId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.VpcId = params.get("VpcId")
        self.RegionId = params.get("RegionId")


class CreateL4Listener(AbstractModel):
    """用于創建四層監聽器的監聽器訊息。目前一個負載均衡下面最多允許創建50個監聽器。

    """

    def __init__(self):
        """
        :param LoadBalancerPort: 監聽器監聽端口，可選值1~65535。
        :type LoadBalancerPort: int
        :param Protocol: 監聽器協議類型，可選值tcp，udp。
        :type Protocol: str
        :param ListenerName: 監聽器名稱。
        :type ListenerName: str
        :param SessionExpire: 監聽器的會話保持時間，單位：秒。可選值：900~3600,不傳表示不開啓會話保持。
        :type SessionExpire: int
        :param HealthSwitch: 是否開啓健康檢查：1（開啓）、0（關閉）。預設值0，表示關閉。
        :type HealthSwitch: int
        :param TimeOut: 健康檢查的響應超時時間，可選值：2-60，預設值：2，單位:秒。<br><font color="red">響應超時時間要小於檢查間隔時間。</font>
        :type TimeOut: int
        :param IntervalTime: 健康檢查檢查間隔時間，預設值：5，可選值：5-300，單位：秒。
        :type IntervalTime: int
        :param HealthNum: 健康阈值，預設值：3，表示當連續探測三次健康則表示該轉發正常，可選值：2-10，單位：次。
        :type HealthNum: int
        :param UnhealthNum: 不健康阈值，預設值：3，表示當連續探測三次不健康則表示該轉發不正常，可選值：2-10，單位：次。
        :type UnhealthNum: int
        :param Bandwidth: 監聽器最大頻寬值，用于計費模式爲固定頻寬計費，可選值：0-1000，單位：Mbps。
        :type Bandwidth: int
        :param CustomHealthSwitch: 是否開啓自定義健康檢查：1（開啓）、0（關閉）。預設值0，表示關閉。（該欄位在健康檢查開啓的情況下才生效）
        :type CustomHealthSwitch: int
        :param InputType: 自定義健康探測内容類型，可選值：text（文本）、hexadecimal（十六進制）。
        :type InputType: str
        :param LineSeparatorType: 探測内容類型爲文本方式時，針對請求文本中換行替換方式。可選值：1（替換爲LF）、2（替換爲CR）、3（替換爲LF+CR）。
        :type LineSeparatorType: int
        :param HealthRequest: 自定義探測請求内容。
        :type HealthRequest: str
        :param HealthResponse: 自定義探測返回内容。
        :type HealthResponse: str
        :param ToaFlag: 是否開啓toa。可選值：0（關閉）、1（開啓），預設關閉。（該欄位在負載均衡爲fullnat類型下才生效）
        :type ToaFlag: int
        """
        self.LoadBalancerPort = None
        self.Protocol = None
        self.ListenerName = None
        self.SessionExpire = None
        self.HealthSwitch = None
        self.TimeOut = None
        self.IntervalTime = None
        self.HealthNum = None
        self.UnhealthNum = None
        self.Bandwidth = None
        self.CustomHealthSwitch = None
        self.InputType = None
        self.LineSeparatorType = None
        self.HealthRequest = None
        self.HealthResponse = None
        self.ToaFlag = None


    def _deserialize(self, params):
        self.LoadBalancerPort = params.get("LoadBalancerPort")
        self.Protocol = params.get("Protocol")
        self.ListenerName = params.get("ListenerName")
        self.SessionExpire = params.get("SessionExpire")
        self.HealthSwitch = params.get("HealthSwitch")
        self.TimeOut = params.get("TimeOut")
        self.IntervalTime = params.get("IntervalTime")
        self.HealthNum = params.get("HealthNum")
        self.UnhealthNum = params.get("UnhealthNum")
        self.Bandwidth = params.get("Bandwidth")
        self.CustomHealthSwitch = params.get("CustomHealthSwitch")
        self.InputType = params.get("InputType")
        self.LineSeparatorType = params.get("LineSeparatorType")
        self.HealthRequest = params.get("HealthRequest")
        self.HealthResponse = params.get("HealthResponse")
        self.ToaFlag = params.get("ToaFlag")


class CreateL4ListenersRequest(AbstractModel):
    """CreateL4Listeners請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID，可通過介面DescribeLoadBalancers查詢。
        :type LoadBalancerId: str
        :param ListenerSet: 監聽器訊息數組，可以創建多個監聽器。目前一個負載均衡下面最多允許創建50個監聽器
        :type ListenerSet: list of CreateL4Listener
        """
        self.LoadBalancerId = None
        self.ListenerSet = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("ListenerSet") is not None:
            self.ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = CreateL4Listener()
                obj._deserialize(item)
                self.ListenerSet.append(obj)


class CreateL4ListenersResponse(AbstractModel):
    """CreateL4Listeners返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID。該介面爲異步任務，可根據本參數調用DescribeLoadBalancerTaskResult介面來查詢任務操作結果
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateL7Listener(AbstractModel):
    """用于創建四層監聽器的監聽器訊息。目前一個負載均衡下面最多允許創建50個七層監聽器。

    """

    def __init__(self):
        """
        :param LoadBalancerPort: 七層監聽器端口，可選值1~65535。
        :type LoadBalancerPort: int
        :param Protocol: 七層監聽器協議類型，可選值：http,https。
        :type Protocol: str
        :param ListenerName: 七層監聽器名稱。
        :type ListenerName: str
        :param SslMode: 認證方式：0（不認證，用于http），1（單向認證，用于https），2（雙向認證，用于https）。當創建的是https類型的監聽器時，此值必選。
        :type SslMode: int
        :param CertId: 服務端證書ID。當創建的是https類型的監聽器時，此值必選。
        :type CertId: str
        :param CertName: 服務端證書名稱。
        :type CertName: str
        :param CertContent: 服務端證書内容。
        :type CertContent: str
        :param CertKey: 服務端證書金鑰。
        :type CertKey: str
        :param CertCaId: 用戶端證書ID。
        :type CertCaId: str
        :param CertCaName: 用戶端證書名稱。
        :type CertCaName: str
        :param CertCaContent: 用戶端證書内容。
        :type CertCaContent: str
        :param Bandwidth: 用于計費模式爲固定頻寬計費，指定監聽器最大頻寬值，可選值：0-1000，單位：Mbps。
        :type Bandwidth: int
        """
        self.LoadBalancerPort = None
        self.Protocol = None
        self.ListenerName = None
        self.SslMode = None
        self.CertId = None
        self.CertName = None
        self.CertContent = None
        self.CertKey = None
        self.CertCaId = None
        self.CertCaName = None
        self.CertCaContent = None
        self.Bandwidth = None


    def _deserialize(self, params):
        self.LoadBalancerPort = params.get("LoadBalancerPort")
        self.Protocol = params.get("Protocol")
        self.ListenerName = params.get("ListenerName")
        self.SslMode = params.get("SslMode")
        self.CertId = params.get("CertId")
        self.CertName = params.get("CertName")
        self.CertContent = params.get("CertContent")
        self.CertKey = params.get("CertKey")
        self.CertCaId = params.get("CertCaId")
        self.CertCaName = params.get("CertCaName")
        self.CertCaContent = params.get("CertCaContent")
        self.Bandwidth = params.get("Bandwidth")


class CreateL7ListenersRequest(AbstractModel):
    """CreateL7Listeners請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID
        :type LoadBalancerId: str
        :param ListenerSet: 七層監聽器訊息數組，可以創建多個七層監聽器。目前一個負載均衡下面最多允許創建50個七層監聽器。
        :type ListenerSet: list of CreateL7Listener
        """
        self.LoadBalancerId = None
        self.ListenerSet = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("ListenerSet") is not None:
            self.ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = CreateL7Listener()
                obj._deserialize(item)
                self.ListenerSet.append(obj)


class CreateL7ListenersResponse(AbstractModel):
    """CreateL7Listeners返回參數結構體

    """

    def __init__(self):
        """
        :param ListenerIds: 新建的負載均衡七層監聽器的唯一ID清單。
        :type ListenerIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ListenerIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ListenerIds = params.get("ListenerIds")
        self.RequestId = params.get("RequestId")


class CreateL7Rule(AbstractModel):
    """用于創建七層監聽器的轉發規則的訊息。目前一個七層監聽器下面最多允許創建50個七層轉發域名，而每一個轉發域名下最多可以創建100個轉發規則。

    """

    def __init__(self):
        """
        :param Domain: 七層轉發規則的轉發域名。
        :type Domain: str
        :param Url: 七層轉發規則的轉發路徑。
        :type Url: str
        :param SessionExpire: 會話保持時間，單位：秒。可選值：30~3600。預設值0，表示不開啓會話保持。
        :type SessionExpire: int
        :param HealthSwitch: 健康檢查開關：1（開啓）、0（關閉）。預設值0，表示關閉。
        :type HealthSwitch: int
        :param IntervalTime: 健康檢查檢查間隔時間，預設值：5，可選值：5-300，單位：秒。
        :type IntervalTime: int
        :param HealthNum: 健康檢查健康阈值，預設值：3，表示當連續探測三次健康則表示該轉發正常，可選值：2-10，單位：次。
        :type HealthNum: int
        :param UnhealthNum: 健康檢查不健康阈值，預設值：5，表示當連續探測五次不健康則表示該轉發不正常，可選值：2-10，單位：次。
        :type UnhealthNum: int
        :param HttpCodes: 健康檢查中認爲健康的HTTP返回碼的組合。可選值爲1~5的集合，1表示HTTP返回碼爲1xx認爲健康。2表示HTTP返回碼爲2xx認爲健康。3表示HTTP返回碼爲3xx認爲健康。4表示HTTP返回碼爲4xx認爲健康。5表示HTTP返回碼爲5xx認爲健康。
        :type HttpCodes: list of int non-negative
        :param HttpCheckPath: 健康檢查檢查路徑。
        :type HttpCheckPath: str
        :param HttpCheckDomain: 健康檢查檢查域名。如果創建規則的域名使用通配符或正規表示式，則健康檢查檢查域名可自定義，否則必須跟健康檢查檢查域名一樣。
        :type HttpCheckDomain: str
        :param BalanceMode: 均衡方式：ip_hash、wrr。預設值wrr。
        :type BalanceMode: str
        """
        self.Domain = None
        self.Url = None
        self.SessionExpire = None
        self.HealthSwitch = None
        self.IntervalTime = None
        self.HealthNum = None
        self.UnhealthNum = None
        self.HttpCodes = None
        self.HttpCheckPath = None
        self.HttpCheckDomain = None
        self.BalanceMode = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        self.SessionExpire = params.get("SessionExpire")
        self.HealthSwitch = params.get("HealthSwitch")
        self.IntervalTime = params.get("IntervalTime")
        self.HealthNum = params.get("HealthNum")
        self.UnhealthNum = params.get("UnhealthNum")
        self.HttpCodes = params.get("HttpCodes")
        self.HttpCheckPath = params.get("HttpCheckPath")
        self.HttpCheckDomain = params.get("HttpCheckDomain")
        self.BalanceMode = params.get("BalanceMode")


class CreateL7RulesRequest(AbstractModel):
    """CreateL7Rules請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID，可通過介面DescribeLoadBalancers查詢。
        :type LoadBalancerId: str
        :param ListenerId: 七層監聽器實例ID，可通過介面DescribeL7Listeners查詢。
        :type ListenerId: str
        :param RuleSet: 七層轉發規則訊息數組，可以創建多個七層轉發規則。目前一個七層監聽器下面最多允許創建50個七層轉發域名，而每一個轉發域名下最多可以創建100個轉發規則。目前只能單條創建，不能批次創建。
        :type RuleSet: list of CreateL7Rule
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.RuleSet = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("RuleSet") is not None:
            self.RuleSet = []
            for item in params.get("RuleSet"):
                obj = CreateL7Rule()
                obj._deserialize(item)
                self.RuleSet.append(obj)


class CreateL7RulesResponse(AbstractModel):
    """CreateL7Rules返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID。該介面爲異步任務，可根據本參數調用DescribeLoadBalancerTaskResult介面來查詢任務操作結果。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateLoadBalancerBzConf(AbstractModel):
    """用于創建負載均衡的個性化配置。

    """

    def __init__(self):
        """
        :param BzPayMode: 按月/按小時計費。
        :type BzPayMode: str
        :param BzL4Metrics: 四層可選按頻寬，連接數衡量。
        :type BzL4Metrics: str
        :param BzL7Metrics: 七層可選按qps衡量。
        :type BzL7Metrics: str
        """
        self.BzPayMode = None
        self.BzL4Metrics = None
        self.BzL7Metrics = None


    def _deserialize(self, params):
        self.BzPayMode = params.get("BzPayMode")
        self.BzL4Metrics = params.get("BzL4Metrics")
        self.BzL7Metrics = params.get("BzL7Metrics")


class CreateLoadBalancersRequest(AbstractModel):
    """CreateLoadBalancers請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: 黑石負載均衡實例所屬的私有網絡ID。
        :type VpcId: str
        :param LoadBalancerType: 負載均衡的類型，取值爲open或internal。open表示公網(有日租)，internal表示内網。
        :type LoadBalancerType: str
        :param SubnetId: 在私有網絡内購買内網負載均衡實例的時候需要指定子網ID，内網負載均衡實例的VIP将從這個子網中産生。其他情況不用填寫該欄位。
        :type SubnetId: str
        :param ProjectId: 負載均衡所屬項目ID。不填則屬于預設項目。
        :type ProjectId: int
        :param GoodsNum: 購買黑石負載均衡實例的數量。預設值爲1, 最大值爲20。
        :type GoodsNum: int
        :param PayMode: 黑石負載均衡的計費模式，取值爲flow和bandwidth，其中flow模式表示流量模式，bandwidth表示頻寬模式。預設值爲flow。
        :type PayMode: str
        :param TgwSetType: 負載均衡對應的TGW集群類别，取值爲tunnel、fullnat或dnat。tunnel表示隧道集群，fullnat表示FULLNAT集群，dnat表示DNAT集群。預設值爲fullnat。如需獲取client IP，可以選擇 tunnel 模式，fullnat 模式（tcp 通過toa 獲取），dnat 模式。
        :type TgwSetType: str
        :param Exclusive: 負載均衡的獨占類别，取值爲0表示非獨占，1表示四層獨占，2表示七層獨占，3表示四層和七層獨占，4表示共享容災。
        :type Exclusive: int
        :param SpecifiedVips: 指定的VIP，如果指定，則數量必須與goodsNum一緻。如果不指定，則由後台分配随機VIP。
        :type SpecifiedVips: list of str
        :param BzConf: （未全地域開放）保障型負載均衡設定參數，如果類别選擇保障型則需傳入此參數。
        :type BzConf: :class:`tencentcloud.bmlb.v20180625.models.CreateLoadBalancerBzConf`
        :param IpProtocolType: IP協議類型。可取的值爲“ipv4”或“ipv6”。
        :type IpProtocolType: str
        """
        self.VpcId = None
        self.LoadBalancerType = None
        self.SubnetId = None
        self.ProjectId = None
        self.GoodsNum = None
        self.PayMode = None
        self.TgwSetType = None
        self.Exclusive = None
        self.SpecifiedVips = None
        self.BzConf = None
        self.IpProtocolType = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.SubnetId = params.get("SubnetId")
        self.ProjectId = params.get("ProjectId")
        self.GoodsNum = params.get("GoodsNum")
        self.PayMode = params.get("PayMode")
        self.TgwSetType = params.get("TgwSetType")
        self.Exclusive = params.get("Exclusive")
        self.SpecifiedVips = params.get("SpecifiedVips")
        if params.get("BzConf") is not None:
            self.BzConf = CreateLoadBalancerBzConf()
            self.BzConf._deserialize(params.get("BzConf"))
        self.IpProtocolType = params.get("IpProtocolType")


class CreateLoadBalancersResponse(AbstractModel):
    """CreateLoadBalancers返回參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerIds: 創建的黑石負載均衡實例ID。
        :type LoadBalancerIds: list of str
        :param TaskId: 創建負載均衡的異步任務ID。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.LoadBalancerIds = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateTrafficMirrorRequest(AbstractModel):
    """CreateTrafficMirror請求參數結構體

    """

    def __init__(self):
        """
        :param Alias: 流量映像實例别名。
        :type Alias: str
        :param VpcId: 流量映像實例所屬的私有網絡ID，形如：vpc-xxx。
        :type VpcId: str
        """
        self.Alias = None
        self.VpcId = None


    def _deserialize(self, params):
        self.Alias = params.get("Alias")
        self.VpcId = params.get("VpcId")


class CreateTrafficMirrorResponse(AbstractModel):
    """CreateTrafficMirror返回參數結構體

    """

    def __init__(self):
        """
        :param TrafficMirrorId: 流量映像實例ID
        :type TrafficMirrorId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TrafficMirrorId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TrafficMirrorId = params.get("TrafficMirrorId")
        self.RequestId = params.get("RequestId")


class DeleteL7DomainsRequest(AbstractModel):
    """DeleteL7Domains請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID，可通過介面DescribeLoadBalancers查詢。
        :type LoadBalancerId: str
        :param ListenerId: 七層監聽器實例ID，可通過介面DescribeL7Listeners查詢。
        :type ListenerId: str
        :param DomainIds: 轉發域名實例ID清單，可通過介面DescribeL7Rules查詢。
        :type DomainIds: list of str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.DomainIds = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.DomainIds = params.get("DomainIds")


class DeleteL7DomainsResponse(AbstractModel):
    """DeleteL7Domains返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID。該介面爲異步任務，可根據本參數調用DescribeLoadBalancerTaskResult介面來查詢任務操作結果。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteL7RulesRequest(AbstractModel):
    """DeleteL7Rules請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID，可通過介面DescribeLoadBalancers查詢。
        :type LoadBalancerId: str
        :param ListenerId: 七層監聽器實例ID，可通過介面DescribeL7Listeners查詢。
        :type ListenerId: str
        :param DomainId: 轉發域名實例ID，可通過介面DescribeL7Rules查詢。
        :type DomainId: str
        :param LocationIds: 轉發路徑實例ID清單，可通過介面DescribeL7Rules查詢。
        :type LocationIds: list of str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.DomainId = None
        self.LocationIds = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.DomainId = params.get("DomainId")
        self.LocationIds = params.get("LocationIds")


class DeleteL7RulesResponse(AbstractModel):
    """DeleteL7Rules返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID。該介面爲異步任務，可根據本參數調用DescribeLoadBalancerTaskResult介面來查詢任務操作結果。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteListenersRequest(AbstractModel):
    """DeleteListeners請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID，可通過介面DescribeLoadBalancers查詢。
        :type LoadBalancerId: str
        :param ListenerIds: 待删除的負載均衡四層和七層監聽器ID清單，可通過介面DescribeL4Listeners和DescribeL7Listeners查詢。目前同時只能删除一種類型的監聽器，并且删除七層監聽器的數量上限爲一個。
        :type ListenerIds: list of str
        """
        self.LoadBalancerId = None
        self.ListenerIds = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerIds = params.get("ListenerIds")


class DeleteListenersResponse(AbstractModel):
    """DeleteListeners返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID。該介面爲異步任務，可根據本參數調用DescribeLoadBalancerTaskResult介面來查詢任務操作結果。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteLoadBalancerRequest(AbstractModel):
    """DeleteLoadBalancer請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID，可通過介面DescribeLoadBalancers查詢。
        :type LoadBalancerId: str
        """
        self.LoadBalancerId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")


class DeleteLoadBalancerResponse(AbstractModel):
    """DeleteLoadBalancer返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID。該介面爲異步任務，可根據本參數調用DescribeLoadBalancerTaskResult介面來查詢任務操作結果。
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteTrafficMirrorRequest(AbstractModel):
    """DeleteTrafficMirror請求參數結構體

    """

    def __init__(self):
        """
        :param TrafficMirrorIds: 流量映像實例ID數組，可以批次删除，每次删除上限爲20
        :type TrafficMirrorIds: list of str
        """
        self.TrafficMirrorIds = None


    def _deserialize(self, params):
        self.TrafficMirrorIds = params.get("TrafficMirrorIds")


class DeleteTrafficMirrorResponse(AbstractModel):
    """DeleteTrafficMirror返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID。該介面爲異步任務，可根據本參數調用DescribeLoadBalancerTaskResult介面來查詢任務操作結果。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DescribeCertDetailRequest(AbstractModel):
    """DescribeCertDetail請求參數結構體

    """

    def __init__(self):
        """
        :param CertId: 證書ID。
        :type CertId: str
        """
        self.CertId = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")


class DescribeCertDetailResponse(AbstractModel):
    """DescribeCertDetail返回參數結構體

    """

    def __init__(self):
        """
        :param CertId: 證書ID。
        :type CertId: str
        :param CertName: 證書名稱。
        :type CertName: str
        :param CertType: 證書類型（SVR=服務器證書，CA=用戶端證書）。
        :type CertType: str
        :param CertContent: 證書内容。
        :type CertContent: str
        :param CertDomain: 證書主域名。
        :type CertDomain: str
        :param CertSubjectDomain: 證書子域名清單。
        :type CertSubjectDomain: list of str
        :param CertUploadTime: 證書上傳時間。
        :type CertUploadTime: str
        :param CertBeginTime: 證書生效時間。
        :type CertBeginTime: str
        :param CertEndTime: 證書失效時間。
        :type CertEndTime: str
        :param CertLoadBalancerSet: 該證書關聯的黑石負載均衡對象清單。
        :type CertLoadBalancerSet: list of CertDetailLoadBalancer
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CertId = None
        self.CertName = None
        self.CertType = None
        self.CertContent = None
        self.CertDomain = None
        self.CertSubjectDomain = None
        self.CertUploadTime = None
        self.CertBeginTime = None
        self.CertEndTime = None
        self.CertLoadBalancerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.CertName = params.get("CertName")
        self.CertType = params.get("CertType")
        self.CertContent = params.get("CertContent")
        self.CertDomain = params.get("CertDomain")
        self.CertSubjectDomain = params.get("CertSubjectDomain")
        self.CertUploadTime = params.get("CertUploadTime")
        self.CertBeginTime = params.get("CertBeginTime")
        self.CertEndTime = params.get("CertEndTime")
        if params.get("CertLoadBalancerSet") is not None:
            self.CertLoadBalancerSet = []
            for item in params.get("CertLoadBalancerSet"):
                obj = CertDetailLoadBalancer()
                obj._deserialize(item)
                self.CertLoadBalancerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDevicesBindInfoRequest(AbstractModel):
    """DescribeDevicesBindInfo請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: 黑石私有網絡唯一ID。
        :type VpcId: str
        :param InstanceIds: 主機ID或虛機IP清單，可用于獲取綁定了該主機的負載均衡清單。
        :type InstanceIds: list of str
        """
        self.VpcId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.InstanceIds = params.get("InstanceIds")


class DescribeDevicesBindInfoResponse(AbstractModel):
    """DescribeDevicesBindInfo返回參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerSet: 返回的負載均衡綁定訊息。
        :type LoadBalancerSet: list of DevicesBindInfoLoadBalancer
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.LoadBalancerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoadBalancerSet") is not None:
            self.LoadBalancerSet = []
            for item in params.get("LoadBalancerSet"):
                obj = DevicesBindInfoLoadBalancer()
                obj._deserialize(item)
                self.LoadBalancerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeL4Backend(AbstractModel):
    """待查詢四層監聽器綁定的主機訊息。

    """

    def __init__(self):
        """
        :param Port: 待綁定的主機端口，可選值1~65535。
        :type Port: int
        :param InstanceId: 黑石物理機的主機ID。
        :type InstanceId: str
        """
        self.Port = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")


class DescribeL4BackendsRequest(AbstractModel):
    """DescribeL4Backends請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID，可通過介面DescribeLoadBalancers查詢。
        :type LoadBalancerId: str
        :param ListenerId: 負載均衡四層監聽器ID，可通過介面DescribeL4Listeners查詢。
        :type ListenerId: str
        :param BackendSet: 待查詢的主機訊息。
        :type BackendSet: list of DescribeL4Backend
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.BackendSet = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("BackendSet") is not None:
            self.BackendSet = []
            for item in params.get("BackendSet"):
                obj = DescribeL4Backend()
                obj._deserialize(item)
                self.BackendSet.append(obj)


class DescribeL4BackendsResponse(AbstractModel):
    """DescribeL4Backends返回參數結構體

    """

    def __init__(self):
        """
        :param BackendSet: 返回的綁定關系清單。
        :type BackendSet: list of L4Backend
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.BackendSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BackendSet") is not None:
            self.BackendSet = []
            for item in params.get("BackendSet"):
                obj = L4Backend()
                obj._deserialize(item)
                self.BackendSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeL4ListenerInfoRequest(AbstractModel):
    """DescribeL4ListenerInfo請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID，可通過介面DescribeLoadBalancers查詢。
        :type LoadBalancerId: str
        :param SearchKey: 查找的鍵值，可用于模糊查找該名稱的監聽器。
        :type SearchKey: str
        :param InstanceIds: 主機ID或虛機IP清單，可用于獲取綁定了該主機的監聽器。
        :type InstanceIds: list of str
        """
        self.LoadBalancerId = None
        self.SearchKey = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.SearchKey = params.get("SearchKey")
        self.InstanceIds = params.get("InstanceIds")


class DescribeL4ListenerInfoResponse(AbstractModel):
    """DescribeL4ListenerInfo返回參數結構體

    """

    def __init__(self):
        """
        :param ListenerSet: 返回的四層監聽器清單。
        :type ListenerSet: list of L4ListenerInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ListenerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ListenerSet") is not None:
            self.ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = L4ListenerInfo()
                obj._deserialize(item)
                self.ListenerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeL4ListenersRequest(AbstractModel):
    """DescribeL4Listeners請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID，可通過介面DescribeLoadBalancers查詢。
        :type LoadBalancerId: str
        :param ListenerIds: 四層監聽器實例ID數組，可通過介面DescribeL4Listeners查詢。
        :type ListenerIds: list of str
        """
        self.LoadBalancerId = None
        self.ListenerIds = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerIds = params.get("ListenerIds")


class DescribeL4ListenersResponse(AbstractModel):
    """DescribeL4Listeners返回參數結構體

    """

    def __init__(self):
        """
        :param ListenerSet: 監聽器訊息數組。
        :type ListenerSet: list of L4Listener
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ListenerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ListenerSet") is not None:
            self.ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = L4Listener()
                obj._deserialize(item)
                self.ListenerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeL7BackendsRequest(AbstractModel):
    """DescribeL7Backends請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID，可通過介面DescribeLoadBalancers查詢。
        :type LoadBalancerId: str
        :param ListenerId: 七層監聽器實例ID，可通過介面DescribeL7Listeners查詢。
        :type ListenerId: str
        :param DomainId: 轉發域名實例ID，可通過介面DescribeL7Rules查詢。
        :type DomainId: str
        :param LocationId: 轉發路徑實例ID，可通過介面DescribeL7Rules查詢。
        :type LocationId: str
        :param QueryType: 查詢條件，傳'all'則查詢所有與規則綁定的主機訊息。
        :type QueryType: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.DomainId = None
        self.LocationId = None
        self.QueryType = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.DomainId = params.get("DomainId")
        self.LocationId = params.get("LocationId")
        self.QueryType = params.get("QueryType")


class DescribeL7BackendsResponse(AbstractModel):
    """DescribeL7Backends返回參數結構體

    """

    def __init__(self):
        """
        :param BackendSet: 返回的綁定關系清單。
        :type BackendSet: list of L7Backend
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.BackendSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BackendSet") is not None:
            self.BackendSet = []
            for item in params.get("BackendSet"):
                obj = L7Backend()
                obj._deserialize(item)
                self.BackendSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeL7ListenerInfoRequest(AbstractModel):
    """DescribeL7ListenerInfo請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID，可通過介面DescribeLoadBalancers查詢。
        :type LoadBalancerId: str
        :param SearchKey: 查找的鍵值，可用于模糊查找有該轉發域名的監聽器。
        :type SearchKey: str
        :param InstanceIds: 主機ID或虛機IP清單，可用于獲取綁定了該主機的監聽器。
        :type InstanceIds: list of str
        :param IfGetBackendInfo: 是否獲取轉發規則下的主機訊息。預設爲0，不獲取。
        :type IfGetBackendInfo: int
        """
        self.LoadBalancerId = None
        self.SearchKey = None
        self.InstanceIds = None
        self.IfGetBackendInfo = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.SearchKey = params.get("SearchKey")
        self.InstanceIds = params.get("InstanceIds")
        self.IfGetBackendInfo = params.get("IfGetBackendInfo")


class DescribeL7ListenerInfoResponse(AbstractModel):
    """DescribeL7ListenerInfo返回參數結構體

    """

    def __init__(self):
        """
        :param ListenerSet: 返回的七層監聽器清單。
        :type ListenerSet: list of L7ListenerInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ListenerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ListenerSet") is not None:
            self.ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = L7ListenerInfo()
                obj._deserialize(item)
                self.ListenerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeL7ListenersExRequest(AbstractModel):
    """DescribeL7ListenersEx請求參數結構體

    """

    def __init__(self):
        """
        :param TrafficMirrorId: 返回的監聽器中标識是否綁定在此流量映像中。
        :type TrafficMirrorId: str
        :param VpcId: 待獲取監聽器所在的VPC的ID。
        :type VpcId: str
        :param Offset: 此VPC中獲取負載均衡的偏移。
        :type Offset: int
        :param Limit: 此VPC中獲取負載均衡的數量。
        :type Limit: int
        :param Filters: 過濾條件。
LoadBalancerId - String - （過濾條件）負載均衡ID。
LoadBalancerName - String - （過濾條件）負載均衡名稱。
Vip - String - （過濾條件）VIP。
ListenerId - String - （過濾條件）監聽器ID。
ListenerName -  String - （過濾條件）監聽器名稱。
Protocol -  String - （過濾條件）七層協議。
LoadBalancerPort -  String - （過濾條件）監聽器端口。
        :type Filters: list of Filter
        """
        self.TrafficMirrorId = None
        self.VpcId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.TrafficMirrorId = params.get("TrafficMirrorId")
        self.VpcId = params.get("VpcId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeL7ListenersExResponse(AbstractModel):
    """DescribeL7ListenersEx返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 此指定VPC中負載均衡的總數。
        :type TotalCount: int
        :param ListenerSet: 符合條件的監聽器。
        :type ListenerSet: list of L7ExListener
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
                obj = L7ExListener()
                obj._deserialize(item)
                self.ListenerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeL7ListenersRequest(AbstractModel):
    """DescribeL7Listeners請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID，可通過介面DescribeLoadBalancers查詢。
        :type LoadBalancerId: str
        :param ListenerIds: 七層監聽器實例ID清單，可通過介面DescribeL7Listeners查詢。
        :type ListenerIds: list of str
        """
        self.LoadBalancerId = None
        self.ListenerIds = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerIds = params.get("ListenerIds")


class DescribeL7ListenersResponse(AbstractModel):
    """DescribeL7Listeners返回參數結構體

    """

    def __init__(self):
        """
        :param ListenerSet: 返回的七層監聽器清單。
        :type ListenerSet: list of L7Listener
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ListenerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ListenerSet") is not None:
            self.ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = L7Listener()
                obj._deserialize(item)
                self.ListenerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeL7RulesRequest(AbstractModel):
    """DescribeL7Rules請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID，可通過介面DescribeLoadBalancers查詢。
        :type LoadBalancerId: str
        :param ListenerId: 七層監聽器ID，可通過介面DescribeL7Listeners查詢。
        :type ListenerId: str
        :param DomainIds: 轉發域名ID清單，可通過介面DescribeL7Rules查詢。
        :type DomainIds: list of str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.DomainIds = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.DomainIds = params.get("DomainIds")


class DescribeL7RulesResponse(AbstractModel):
    """DescribeL7Rules返回參數結構體

    """

    def __init__(self):
        """
        :param RuleSet: 返回的轉發規則清單。
        :type RuleSet: list of L7Rule
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RuleSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuleSet") is not None:
            self.RuleSet = []
            for item in params.get("RuleSet"):
                obj = L7Rule()
                obj._deserialize(item)
                self.RuleSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancerPortInfoRequest(AbstractModel):
    """DescribeLoadBalancerPortInfo請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID，可通過介面DescribeLoadBalancers查詢。
        :type LoadBalancerId: str
        """
        self.LoadBalancerId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")


class DescribeLoadBalancerPortInfoResponse(AbstractModel):
    """DescribeLoadBalancerPortInfo返回參數結構體

    """

    def __init__(self):
        """
        :param ListenerSet: 返回的監聽器清單（四層和七層）。
        :type ListenerSet: list of LoadBalancerPortInfoListener
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ListenerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ListenerSet") is not None:
            self.ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = LoadBalancerPortInfoListener()
                obj._deserialize(item)
                self.ListenerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancerTaskResultRequest(AbstractModel):
    """DescribeLoadBalancerTaskResult請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID。由具體的異步操作介面提供。
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class DescribeLoadBalancerTaskResultResponse(AbstractModel):
    """DescribeLoadBalancerTaskResult返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 任務當前狀态。0：成功，1：失敗，2：進行中。
        :type Status: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancersRequest(AbstractModel):
    """DescribeLoadBalancers請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerIds: 負載均衡器ID數組
        :type LoadBalancerIds: list of str
        :param LoadBalancerType: 負載均衡的類型 : open表示公網LB類型，internal表示内網LB類型
        :type LoadBalancerType: str
        :param LoadBalancerName: 負載均衡器名稱
        :type LoadBalancerName: str
        :param Domain: 負載均衡域名。規則：1-60個小寫英文字母、數字、點号“.”或連接線“-”。内網類型的負載均衡不能配置該欄位
        :type Domain: str
        :param LoadBalancerVips: 負載均衡獲得的公網IP網址,支援多個
        :type LoadBalancerVips: list of str
        :param Offset: 數據偏移量，預設爲0
        :type Offset: int
        :param Limit: 返回數據長度，預設爲20
        :type Limit: int
        :param SearchKey: 模糊查找名稱、域名、VIP
        :type SearchKey: str
        :param OrderBy: 排序欄位，支援：loadBalancerName,createTime,domain,loadBalancerType
        :type OrderBy: str
        :param OrderType: 1倒序，0順序，預設順序
        :type OrderType: int
        :param ProjectId: 項目ID
        :type ProjectId: int
        :param Exclusive: 是否篩選獨占集群，0表示非獨占集群，1表示四層獨占集群，2表示七層獨占集群，3表示四層和七層獨占集群，4表示共享容災
        :type Exclusive: int
        :param TgwSetType: 該負載均衡對應的tgw集群（fullnat,tunnel,dnat）
        :type TgwSetType: str
        :param VpcId: 該負載均衡對應的所在的私有網絡ID
        :type VpcId: str
        :param QueryType: 'CONFLIST' 查詢帶confId的LB清單，'CONFID' 查詢某個confId綁定的LB清單
        :type QueryType: str
        :param ConfId: 個性化配置ID
        :type ConfId: str
        """
        self.LoadBalancerIds = None
        self.LoadBalancerType = None
        self.LoadBalancerName = None
        self.Domain = None
        self.LoadBalancerVips = None
        self.Offset = None
        self.Limit = None
        self.SearchKey = None
        self.OrderBy = None
        self.OrderType = None
        self.ProjectId = None
        self.Exclusive = None
        self.TgwSetType = None
        self.VpcId = None
        self.QueryType = None
        self.ConfId = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.Domain = params.get("Domain")
        self.LoadBalancerVips = params.get("LoadBalancerVips")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchKey = params.get("SearchKey")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.ProjectId = params.get("ProjectId")
        self.Exclusive = params.get("Exclusive")
        self.TgwSetType = params.get("TgwSetType")
        self.VpcId = params.get("VpcId")
        self.QueryType = params.get("QueryType")
        self.ConfId = params.get("ConfId")


class DescribeLoadBalancersResponse(AbstractModel):
    """DescribeLoadBalancers返回參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerSet: 返回負載均衡訊息清單。
        :type LoadBalancerSet: list of LoadBalancer
        :param TotalCount: 符合條件的負載均衡總數。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.LoadBalancerSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoadBalancerSet") is not None:
            self.LoadBalancerSet = []
            for item in params.get("LoadBalancerSet"):
                obj = LoadBalancer()
                obj._deserialize(item)
                self.LoadBalancerSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTrafficMirrorListenersRequest(AbstractModel):
    """DescribeTrafficMirrorListeners請求參數結構體

    """

    def __init__(self):
        """
        :param TrafficMirrorId: 流量映像實例ID。
        :type TrafficMirrorId: str
        :param Offset: 分頁的偏移量，也即從第幾條記錄開始查詢
        :type Offset: int
        :param Limit: 單次查詢返回的條目數，預設值：500。
        :type Limit: int
        :param SearchLoadBalancerIds: 待搜索的負載均衡Id。
        :type SearchLoadBalancerIds: list of str
        :param SearchLoadBalancerNames: 待搜索的負載均衡名稱。
        :type SearchLoadBalancerNames: list of str
        :param SearchVips: 待搜索的Vip。
        :type SearchVips: list of str
        :param SearchListenerIds: 待搜索的監聽器ID。
        :type SearchListenerIds: list of str
        :param SearchListenerNames: 待搜索的監聽器名稱。
        :type SearchListenerNames: list of str
        :param SearchProtocols: 待搜索的協議名稱。
        :type SearchProtocols: list of str
        :param SearchLoadBalancerPorts: 待搜索的端口。
        :type SearchLoadBalancerPorts: list of int non-negative
        """
        self.TrafficMirrorId = None
        self.Offset = None
        self.Limit = None
        self.SearchLoadBalancerIds = None
        self.SearchLoadBalancerNames = None
        self.SearchVips = None
        self.SearchListenerIds = None
        self.SearchListenerNames = None
        self.SearchProtocols = None
        self.SearchLoadBalancerPorts = None


    def _deserialize(self, params):
        self.TrafficMirrorId = params.get("TrafficMirrorId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchLoadBalancerIds = params.get("SearchLoadBalancerIds")
        self.SearchLoadBalancerNames = params.get("SearchLoadBalancerNames")
        self.SearchVips = params.get("SearchVips")
        self.SearchListenerIds = params.get("SearchListenerIds")
        self.SearchListenerNames = params.get("SearchListenerNames")
        self.SearchProtocols = params.get("SearchProtocols")
        self.SearchLoadBalancerPorts = params.get("SearchLoadBalancerPorts")


class DescribeTrafficMirrorListenersResponse(AbstractModel):
    """DescribeTrafficMirrorListeners返回參數結構體

    """

    def __init__(self):
        """
        :param ListenerSet: 監聽器清單。
        :type ListenerSet: list of TrafficMirrorListener
        :param TotalCount: 監聽器總數。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ListenerSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ListenerSet") is not None:
            self.ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = TrafficMirrorListener()
                obj._deserialize(item)
                self.ListenerSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTrafficMirrorReceiver(AbstractModel):
    """流量映像進行健康檢查的接收機訊息。

    """

    def __init__(self):
        """
        :param InstanceId: 物理機實例ID。
        :type InstanceId: str
        :param Port: 物理機綁定的端口。
        :type Port: int
        """
        self.InstanceId = None
        self.Port = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Port = params.get("Port")


class DescribeTrafficMirrorReceiverHealthStatusRequest(AbstractModel):
    """DescribeTrafficMirrorReceiverHealthStatus請求參數結構體

    """

    def __init__(self):
        """
        :param TrafficMirrorId: 查詢所在的流量映像ID。
        :type TrafficMirrorId: str
        :param ReceiverSet: 流量映像接收機實例ID和端口數組。
        :type ReceiverSet: list of DescribeTrafficMirrorReceiver
        """
        self.TrafficMirrorId = None
        self.ReceiverSet = None


    def _deserialize(self, params):
        self.TrafficMirrorId = params.get("TrafficMirrorId")
        if params.get("ReceiverSet") is not None:
            self.ReceiverSet = []
            for item in params.get("ReceiverSet"):
                obj = DescribeTrafficMirrorReceiver()
                obj._deserialize(item)
                self.ReceiverSet.append(obj)


class DescribeTrafficMirrorReceiverHealthStatusResponse(AbstractModel):
    """DescribeTrafficMirrorReceiverHealthStatus返回參數結構體

    """

    def __init__(self):
        """
        :param ReceiversStatusSet: 内網IP和端口對應的狀态。
        :type ReceiversStatusSet: list of TrafficMirrorReciversStatus
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ReceiversStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ReceiversStatusSet") is not None:
            self.ReceiversStatusSet = []
            for item in params.get("ReceiversStatusSet"):
                obj = TrafficMirrorReciversStatus()
                obj._deserialize(item)
                self.ReceiversStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTrafficMirrorReceiversRequest(AbstractModel):
    """DescribeTrafficMirrorReceivers請求參數結構體

    """

    def __init__(self):
        """
        :param TrafficMirrorId: 流量映像實例ID。
        :type TrafficMirrorId: str
        :param InstanceIds: 接收機黑石物理機實例ID數組。
        :type InstanceIds: list of str
        :param Ports: 接收機接收端口數組。
        :type Ports: list of int
        :param Weights: 接收機實例權重數組。
        :type Weights: list of int
        :param Offset: 分頁的偏移量，也即從第幾條記錄開始查詢
        :type Offset: int
        :param Limit: 單次查詢返回的條目數，預設值：500。
        :type Limit: int
        :param VagueStr: 搜索instance或者alias
        :type VagueStr: str
        :param VagueIp: 搜索IP
        :type VagueIp: str
        """
        self.TrafficMirrorId = None
        self.InstanceIds = None
        self.Ports = None
        self.Weights = None
        self.Offset = None
        self.Limit = None
        self.VagueStr = None
        self.VagueIp = None


    def _deserialize(self, params):
        self.TrafficMirrorId = params.get("TrafficMirrorId")
        self.InstanceIds = params.get("InstanceIds")
        self.Ports = params.get("Ports")
        self.Weights = params.get("Weights")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.VagueStr = params.get("VagueStr")
        self.VagueIp = params.get("VagueIp")


class DescribeTrafficMirrorReceiversResponse(AbstractModel):
    """DescribeTrafficMirrorReceivers返回參數結構體

    """

    def __init__(self):
        """
        :param ReceiverSet: 接收機清單，具體結構描述如data結構所示。
        :type ReceiverSet: list of TrafficMirrorReceiver
        :param TotalCount: 接收機總數。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ReceiverSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ReceiverSet") is not None:
            self.ReceiverSet = []
            for item in params.get("ReceiverSet"):
                obj = TrafficMirrorReceiver()
                obj._deserialize(item)
                self.ReceiverSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTrafficMirrorsRequest(AbstractModel):
    """DescribeTrafficMirrors請求參數結構體

    """

    def __init__(self):
        """
        :param TrafficMirrorIds: 流量映像實例ID的數組，支援批次查詢
        :type TrafficMirrorIds: list of str
        :param Aliases: 流量映像實例别名數組。
        :type Aliases: list of str
        :param VpcIds: 流量映像實例所屬的私有網絡ID數組，形如：vpc-xxx。
        :type VpcIds: list of str
        :param Offset: 分頁的偏移量，也即從第幾條記錄開始查詢
        :type Offset: int
        :param Limit: 單次查詢返回的條目數，預設值：500。
        :type Limit: int
        """
        self.TrafficMirrorIds = None
        self.Aliases = None
        self.VpcIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.TrafficMirrorIds = params.get("TrafficMirrorIds")
        self.Aliases = params.get("Aliases")
        self.VpcIds = params.get("VpcIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTrafficMirrorsResponse(AbstractModel):
    """DescribeTrafficMirrors返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 流量映像總數。
        :type TotalCount: int
        :param TrafficMirrorSet: 對象數組。數組元素爲流量映像訊息，具體結構描述如list結構所示。
        :type TrafficMirrorSet: list of TrafficMirror
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TrafficMirrorSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TrafficMirrorSet") is not None:
            self.TrafficMirrorSet = []
            for item in params.get("TrafficMirrorSet"):
                obj = TrafficMirror()
                obj._deserialize(item)
                self.TrafficMirrorSet.append(obj)
        self.RequestId = params.get("RequestId")


class DevicesBindInfoBackend(AbstractModel):
    """獲取設備綁定訊息時返回的所綁定的主機訊息。

    """

    def __init__(self):
        """
        :param InstanceId: 黑石物理機的主機ID、托管主機ID或虛拟機IP。
        :type InstanceId: str
        :param Port: 主機端口。
        :type Port: int
        """
        self.InstanceId = None
        self.Port = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Port = params.get("Port")


class DevicesBindInfoL4Listener(AbstractModel):
    """獲取設備綁定訊息時返回的四層監聽器訊息。

    """

    def __init__(self):
        """
        :param ListenerId: 七層監聽器實例ID。
        :type ListenerId: str
        :param Protocol: 七層監聽器協議類型，可選值：http,https。
        :type Protocol: str
        :param LoadBalancerPort: 七層監聽器的監聽端口。
        :type LoadBalancerPort: int
        :param BackendSet: 該轉發路徑所綁定的主機清單。
        :type BackendSet: list of DevicesBindInfoBackend
        """
        self.ListenerId = None
        self.Protocol = None
        self.LoadBalancerPort = None
        self.BackendSet = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Protocol = params.get("Protocol")
        self.LoadBalancerPort = params.get("LoadBalancerPort")
        if params.get("BackendSet") is not None:
            self.BackendSet = []
            for item in params.get("BackendSet"):
                obj = DevicesBindInfoBackend()
                obj._deserialize(item)
                self.BackendSet.append(obj)


class DevicesBindInfoL7Listener(AbstractModel):
    """獲取設備綁定訊息時返回的七層監聽器訊息。

    """

    def __init__(self):
        """
        :param ListenerId: 七層監聽器實例ID。
        :type ListenerId: str
        :param Protocol: 七層監聽器協議類型，可選值：http,https。
        :type Protocol: str
        :param LoadBalancerPort: 七層監聽器的監聽端口。
        :type LoadBalancerPort: int
        :param RuleSet: 返回的轉發規則清單。
        :type RuleSet: list of DevicesBindInfoRule
        """
        self.ListenerId = None
        self.Protocol = None
        self.LoadBalancerPort = None
        self.RuleSet = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Protocol = params.get("Protocol")
        self.LoadBalancerPort = params.get("LoadBalancerPort")
        if params.get("RuleSet") is not None:
            self.RuleSet = []
            for item in params.get("RuleSet"):
                obj = DevicesBindInfoRule()
                obj._deserialize(item)
                self.RuleSet.append(obj)


class DevicesBindInfoLoadBalancer(AbstractModel):
    """獲取設備綁定訊息時返回的設備被綁定所在的負載均衡訊息。

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID。
        :type LoadBalancerId: str
        :param AppId: 開發商AppId。
        :type AppId: int
        :param ProjectId: 負載均衡所屬的項目ID。
        :type ProjectId: int
        :param VpcId: 黑石私有網絡唯一ID。
        :type VpcId: str
        :param Vip: 負載均衡的IP網址。
        :type Vip: str
        :param TgwSetType: 負載均衡對應的TGW集群類别，取值爲tunnel或fullnat。tunnel表示隧道集群，fullnat表示FULLNAT集群。
        :type TgwSetType: str
        :param Exclusive: 是否獨占TGW集群。
        :type Exclusive: int
        :param L4ListenerSet: 具有該綁定關系的四層監聽器清單。
        :type L4ListenerSet: list of DevicesBindInfoL4Listener
        :param L7ListenerSet: 具有該綁定關系的七層監聽器清單。
        :type L7ListenerSet: list of DevicesBindInfoL7Listener
        """
        self.LoadBalancerId = None
        self.AppId = None
        self.ProjectId = None
        self.VpcId = None
        self.Vip = None
        self.TgwSetType = None
        self.Exclusive = None
        self.L4ListenerSet = None
        self.L7ListenerSet = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.AppId = params.get("AppId")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.Vip = params.get("Vip")
        self.TgwSetType = params.get("TgwSetType")
        self.Exclusive = params.get("Exclusive")
        if params.get("L4ListenerSet") is not None:
            self.L4ListenerSet = []
            for item in params.get("L4ListenerSet"):
                obj = DevicesBindInfoL4Listener()
                obj._deserialize(item)
                self.L4ListenerSet.append(obj)
        if params.get("L7ListenerSet") is not None:
            self.L7ListenerSet = []
            for item in params.get("L7ListenerSet"):
                obj = DevicesBindInfoL7Listener()
                obj._deserialize(item)
                self.L7ListenerSet.append(obj)


class DevicesBindInfoLocation(AbstractModel):
    """獲取設備綁定訊息時返回的設備所綁定的轉發路徑訊息。

    """

    def __init__(self):
        """
        :param Url: 轉發路徑。
        :type Url: str
        :param LocationId: 轉發路徑實例ID。
        :type LocationId: str
        :param BackendSet: 該轉發路徑所綁定的主機清單。
        :type BackendSet: list of DevicesBindInfoBackend
        """
        self.Url = None
        self.LocationId = None
        self.BackendSet = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.LocationId = params.get("LocationId")
        if params.get("BackendSet") is not None:
            self.BackendSet = []
            for item in params.get("BackendSet"):
                obj = DevicesBindInfoBackend()
                obj._deserialize(item)
                self.BackendSet.append(obj)


class DevicesBindInfoRule(AbstractModel):
    """獲取設備綁定訊息時返回的設備所綁定的轉發規則訊息。

    """

    def __init__(self):
        """
        :param Domain: 轉發域名。
        :type Domain: str
        :param DomainId: 轉發域名ID。
        :type DomainId: str
        :param LocationSet: 轉發路徑清單。
        :type LocationSet: list of DevicesBindInfoLocation
        """
        self.Domain = None
        self.DomainId = None
        self.LocationSet = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        if params.get("LocationSet") is not None:
            self.LocationSet = []
            for item in params.get("LocationSet"):
                obj = DevicesBindInfoLocation()
                obj._deserialize(item)
                self.LocationSet.append(obj)


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


class L4Backend(AbstractModel):
    """查詢四層監聽器返回的與監聽器綁定關系的主機訊息。

    """

    def __init__(self):
        """
        :param BindType: 綁定類别（0代表黑石物理機，1代表虛拟機IP）。
        :type BindType: int
        :param Port: 主機端口。
        :type Port: int
        :param Weight: 權重。
        :type Weight: int
        :param Status: 當前綁定關系的健康檢查狀态（Dead代表不健康，Alive代表健康）。
        :type Status: str
        :param InstanceId: 黑石物理機的主機ID。
        :type InstanceId: str
        :param Alias: 黑石物理機的别名。
        :type Alias: str
        :param LanIp: 主機IP。
        :type LanIp: str
        :param Operates: 黑石物理機當前可以執行的操作。
        :type Operates: list of str
        :param ProbePort: 主機探測端口。
        :type ProbePort: int
        """
        self.BindType = None
        self.Port = None
        self.Weight = None
        self.Status = None
        self.InstanceId = None
        self.Alias = None
        self.LanIp = None
        self.Operates = None
        self.ProbePort = None


    def _deserialize(self, params):
        self.BindType = params.get("BindType")
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")
        self.Status = params.get("Status")
        self.InstanceId = params.get("InstanceId")
        self.Alias = params.get("Alias")
        self.LanIp = params.get("LanIp")
        self.Operates = params.get("Operates")
        self.ProbePort = params.get("ProbePort")


class L4Listener(AbstractModel):
    """查詢四層監聽器時返回的四層監聽器訊息。

    """

    def __init__(self):
        """
        :param ListenerId: 監聽器ID。
        :type ListenerId: str
        :param ListenerName: 用戶自定義的監聽器名稱。
        :type ListenerName: str
        :param Protocol: 負載均衡實例監聽器協議類型，可選值tcp，udp。
        :type Protocol: str
        :param LoadBalancerPort: 負載均衡監聽器的監聽介面，可選值1~65535。
        :type LoadBalancerPort: int
        :param Bandwidth: 用于計費模式爲固定頻寬計費，指定監聽器最大頻寬值，可選值：0-1000，單位：Mbps。
        :type Bandwidth: int
        :param ListenerType: 監聽器的類别：L4Listener（四層監聽器），L7Listener（七層監聽器）。
        :type ListenerType: str
        :param SessionExpire: 會話保持時間。單位：秒
        :type SessionExpire: int
        :param HealthSwitch: 是否開啓了檢查：1（開啓）、0（關閉）。
        :type HealthSwitch: int
        :param TimeOut: 響應超時時間，單位：秒。
        :type TimeOut: int
        :param IntervalTime: 檢查間隔，單位：秒。
        :type IntervalTime: int
        :param HealthNum: 負載均衡監聽器健康阈值，預設值：3，表示當連續探測三次健康則表示該轉發正常，可選值：2-10，單位：次。
        :type HealthNum: int
        :param UnhealthNum: 負載均衡監聽器不健康阈值，預設值：3，表示當連續探測三次不健康則表示該轉發不正常，可選值：2-10，單位：次。
        :type UnhealthNum: int
        :param CustomHealthSwitch: 是否開啓自定義健康檢查：1（開啓）、0（關閉）。預設值0，表示關閉。（該欄位在健康檢查開啓的情況下才生效）
        :type CustomHealthSwitch: int
        :param InputType: 自定義健康探測内容類型，可選值：text（文本）、hexadecimal（十六進制）。
        :type InputType: str
        :param LineSeparatorType: 探測内容類型爲文本方式時，針對請求文本中換行替換方式。可選值：1（替換爲LF）、2（替換爲CR）、3（替換爲LF+CR）。
        :type LineSeparatorType: int
        :param HealthRequest: 自定義探測請求内容。
        :type HealthRequest: str
        :param HealthResponse: 自定義探測返回内容。
        :type HealthResponse: str
        :param ToaFlag: 是否開啓toa：1（開啓）、0（關閉）。
        :type ToaFlag: int
        :param Status: 監聽器當前狀态（0代表創建中，1代表正常運作，2代表創建失敗，3代表删除中，4代表删除失敗）。
        :type Status: int
        :param AddTimestamp: 創建時間戳。
        :type AddTimestamp: str
        :param BalanceMode: 轉發後端服務器調度類型。
        :type BalanceMode: str
        """
        self.ListenerId = None
        self.ListenerName = None
        self.Protocol = None
        self.LoadBalancerPort = None
        self.Bandwidth = None
        self.ListenerType = None
        self.SessionExpire = None
        self.HealthSwitch = None
        self.TimeOut = None
        self.IntervalTime = None
        self.HealthNum = None
        self.UnhealthNum = None
        self.CustomHealthSwitch = None
        self.InputType = None
        self.LineSeparatorType = None
        self.HealthRequest = None
        self.HealthResponse = None
        self.ToaFlag = None
        self.Status = None
        self.AddTimestamp = None
        self.BalanceMode = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Protocol = params.get("Protocol")
        self.LoadBalancerPort = params.get("LoadBalancerPort")
        self.Bandwidth = params.get("Bandwidth")
        self.ListenerType = params.get("ListenerType")
        self.SessionExpire = params.get("SessionExpire")
        self.HealthSwitch = params.get("HealthSwitch")
        self.TimeOut = params.get("TimeOut")
        self.IntervalTime = params.get("IntervalTime")
        self.HealthNum = params.get("HealthNum")
        self.UnhealthNum = params.get("UnhealthNum")
        self.CustomHealthSwitch = params.get("CustomHealthSwitch")
        self.InputType = params.get("InputType")
        self.LineSeparatorType = params.get("LineSeparatorType")
        self.HealthRequest = params.get("HealthRequest")
        self.HealthResponse = params.get("HealthResponse")
        self.ToaFlag = params.get("ToaFlag")
        self.Status = params.get("Status")
        self.AddTimestamp = params.get("AddTimestamp")
        self.BalanceMode = params.get("BalanceMode")


class L4ListenerInfo(AbstractModel):
    """查詢綁定了某主機的四層監聽器時返回的四層監聽器訊息。

    """

    def __init__(self):
        """
        :param ListenerId: 監聽器ID。
        :type ListenerId: str
        :param ListenerName: 用戶自定義的監聽器名稱。
        :type ListenerName: str
        :param Protocol: 負載均衡實例監聽器協議類型，可選值tcp，udp。
        :type Protocol: str
        :param LoadBalancerPort: 負載均衡監聽器的監聽介面，可選值1~65535。
        :type LoadBalancerPort: int
        :param Bandwidth: 用于計費模式爲固定頻寬計費，指定監聽器最大頻寬值，可選值：0-1000，單位：Mbps。
        :type Bandwidth: int
        :param ListenerType: 監聽器的類别：L4Listener（四層監聽器），L7Listener（七層監聽器）。
        :type ListenerType: str
        :param SessionExpire: 會話保持時間。單位：秒
        :type SessionExpire: int
        :param HealthSwitch: 是否開啓了檢查：1（開啓）、0（關閉）。
        :type HealthSwitch: int
        :param TimeOut: 響應超時時間，單位：秒。
        :type TimeOut: int
        :param IntervalTime: 檢查間隔，單位：秒。
        :type IntervalTime: int
        :param HealthNum: 負載均衡監聽器健康阈值，預設值：3，表示當連續探測三次健康則表示該轉發正常，可選值：2-10，單位：次。
        :type HealthNum: int
        :param UnhealthNum: 負載均衡監聽器不健康阈值，預設值：3，表示當連續探測三次不健康則表示該轉發不正常，可選值：2-10，單位：次。
        :type UnhealthNum: int
        :param Status: 監聽器當前狀态（0代表創建中，1代表正常運作，2代表創建失敗，3代表删除中，4代表删除失敗）。
        :type Status: int
        :param AddTimestamp: 創建時間戳。
        :type AddTimestamp: str
        """
        self.ListenerId = None
        self.ListenerName = None
        self.Protocol = None
        self.LoadBalancerPort = None
        self.Bandwidth = None
        self.ListenerType = None
        self.SessionExpire = None
        self.HealthSwitch = None
        self.TimeOut = None
        self.IntervalTime = None
        self.HealthNum = None
        self.UnhealthNum = None
        self.Status = None
        self.AddTimestamp = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Protocol = params.get("Protocol")
        self.LoadBalancerPort = params.get("LoadBalancerPort")
        self.Bandwidth = params.get("Bandwidth")
        self.ListenerType = params.get("ListenerType")
        self.SessionExpire = params.get("SessionExpire")
        self.HealthSwitch = params.get("HealthSwitch")
        self.TimeOut = params.get("TimeOut")
        self.IntervalTime = params.get("IntervalTime")
        self.HealthNum = params.get("HealthNum")
        self.UnhealthNum = params.get("UnhealthNum")
        self.Status = params.get("Status")
        self.AddTimestamp = params.get("AddTimestamp")


class L7Backend(AbstractModel):
    """獲取七層轉發路徑綁定的主機清單時返回的主機訊息。

    """

    def __init__(self):
        """
        :param BindType: 綁定類别（0代表黑石物理機，1代表虛拟機IP）。
        :type BindType: int
        :param Port: 主機端口。
        :type Port: int
        :param Weight: 權重。
        :type Weight: int
        :param Status: 當前綁定關系的健康檢查狀态（Dead代表不健康，Alive代表健康）。
        :type Status: str
        :param InstanceId: 黑石物理機的主機ID。
        :type InstanceId: str
        :param Alias: 黑石物理機的别名。
        :type Alias: str
        :param LanIp: 主機IP。
        :type LanIp: str
        :param MgtIp: 黑石物理機的管理IP。
        :type MgtIp: str
        :param Operates: 黑石物理機當前可以執行的操作。
        :type Operates: list of str
        """
        self.BindType = None
        self.Port = None
        self.Weight = None
        self.Status = None
        self.InstanceId = None
        self.Alias = None
        self.LanIp = None
        self.MgtIp = None
        self.Operates = None


    def _deserialize(self, params):
        self.BindType = params.get("BindType")
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")
        self.Status = params.get("Status")
        self.InstanceId = params.get("InstanceId")
        self.Alias = params.get("Alias")
        self.LanIp = params.get("LanIp")
        self.MgtIp = params.get("MgtIp")
        self.Operates = params.get("Operates")


class L7ExListener(AbstractModel):
    """監聽器訊息。

    """

    def __init__(self):
        """
        :param ListenerId: 綁定的監聽器唯一ID。
        :type ListenerId: str
        :param ListenerName: 監聽器名稱。
        :type ListenerName: str
        :param Protocol: 七層監聽器協議類型，可選值：http,https。
        :type Protocol: str
        :param LoadBalancerPort: 監聽器的監聽端口。
        :type LoadBalancerPort: int
        :param Bandwidth: 當前頻寬。
        :type Bandwidth: int
        :param MaxBandwidth: 頻寬上限。
        :type MaxBandwidth: int
        :param ListenerType: 監聽器類型。
        :type ListenerType: str
        :param SslMode: 認證方式：0（不認證，用于http），1（單向認證，用于https），2（雙向認證，用于https）。
        :type SslMode: int
        :param CertId: 服務端證書ID。
        :type CertId: str
        :param CertCaId: 用戶端證書ID。
        :type CertCaId: str
        :param AddTimestamp: 添加時間。
        :type AddTimestamp: str
        :param LoadBalancerId: 負載均衡名ID。
        :type LoadBalancerId: str
        :param VpcName: 私有網絡名稱。
        :type VpcName: str
        :param VpcCidrBlock: 私有網絡Cidr。
        :type VpcCidrBlock: str
        :param LoadBalancerVips: 負載均衡的VIP。
        :type LoadBalancerVips: list of str
        :param LoadBalancerName: 負載均衡名稱。
        :type LoadBalancerName: str
        :param LoadBalancerVipv6s: 負載均衡IPV6的VIP。
        :type LoadBalancerVipv6s: list of str
        :param IpProtocolType: 支援的IP協議類型。ipv4或者是ipv6。
        :type IpProtocolType: str
        :param BindTrafficMirror: 是否綁定在入參指定的流量映像中。
        :type BindTrafficMirror: bool
        """
        self.ListenerId = None
        self.ListenerName = None
        self.Protocol = None
        self.LoadBalancerPort = None
        self.Bandwidth = None
        self.MaxBandwidth = None
        self.ListenerType = None
        self.SslMode = None
        self.CertId = None
        self.CertCaId = None
        self.AddTimestamp = None
        self.LoadBalancerId = None
        self.VpcName = None
        self.VpcCidrBlock = None
        self.LoadBalancerVips = None
        self.LoadBalancerName = None
        self.LoadBalancerVipv6s = None
        self.IpProtocolType = None
        self.BindTrafficMirror = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Protocol = params.get("Protocol")
        self.LoadBalancerPort = params.get("LoadBalancerPort")
        self.Bandwidth = params.get("Bandwidth")
        self.MaxBandwidth = params.get("MaxBandwidth")
        self.ListenerType = params.get("ListenerType")
        self.SslMode = params.get("SslMode")
        self.CertId = params.get("CertId")
        self.CertCaId = params.get("CertCaId")
        self.AddTimestamp = params.get("AddTimestamp")
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.VpcName = params.get("VpcName")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.LoadBalancerVips = params.get("LoadBalancerVips")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.LoadBalancerVipv6s = params.get("LoadBalancerVipv6s")
        self.IpProtocolType = params.get("IpProtocolType")
        self.BindTrafficMirror = params.get("BindTrafficMirror")


class L7Listener(AbstractModel):
    """獲取黑石負載均衡七層監聽器時返回的七層監聽器訊息。

    """

    def __init__(self):
        """
        :param ListenerId: 七層監聽器實例ID。
        :type ListenerId: str
        :param ListenerName: 七層監聽器名稱。
        :type ListenerName: str
        :param Protocol: 七層監聽器協議類型，可選值：http,https。
        :type Protocol: str
        :param LoadBalancerPort: 七層監聽器的監聽端口。
        :type LoadBalancerPort: int
        :param Bandwidth: 計費模式爲按固定頻寬方式時監聽器的限速值，單位：Mbps。
        :type Bandwidth: int
        :param ListenerType: 監聽器的類别：L4Listener（四層監聽器），L7Listener（七層監聽器）。
        :type ListenerType: str
        :param SslMode: 七層監聽器的認證方式：0（不認證，用于http），1（單向認證，用于https），2（雙向認證，用于https）。
        :type SslMode: int
        :param CertId: 七層監聽器關聯的服務端證書ID。
        :type CertId: str
        :param CertCaId: 七層監聽器關聯的用戶端證書ID。
        :type CertCaId: str
        :param Status: 監聽器當前狀态（0代表創建中，1代表正常運作，2代表創建失敗，3代表删除中，4代表删除失敗）。
        :type Status: int
        :param AddTimestamp: 創建時間戳。
        :type AddTimestamp: str
        :param ForwardProtocol: https轉發類型。0：關閉。1：spdy。2：http2。3：spdy+http2。
        :type ForwardProtocol: int
        """
        self.ListenerId = None
        self.ListenerName = None
        self.Protocol = None
        self.LoadBalancerPort = None
        self.Bandwidth = None
        self.ListenerType = None
        self.SslMode = None
        self.CertId = None
        self.CertCaId = None
        self.Status = None
        self.AddTimestamp = None
        self.ForwardProtocol = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Protocol = params.get("Protocol")
        self.LoadBalancerPort = params.get("LoadBalancerPort")
        self.Bandwidth = params.get("Bandwidth")
        self.ListenerType = params.get("ListenerType")
        self.SslMode = params.get("SslMode")
        self.CertId = params.get("CertId")
        self.CertCaId = params.get("CertCaId")
        self.Status = params.get("Status")
        self.AddTimestamp = params.get("AddTimestamp")
        self.ForwardProtocol = params.get("ForwardProtocol")


class L7ListenerInfo(AbstractModel):
    """查詢綁定了某主機的七層監聽器時返回的七層監聽器訊息。

    """

    def __init__(self):
        """
        :param ListenerId: 七層監聽器實例ID。
        :type ListenerId: str
        :param ListenerName: 七層監聽器名稱。
        :type ListenerName: str
        :param Protocol: 七層監聽器協議類型，可選值：http,https。
        :type Protocol: str
        :param LoadBalancerPort: 七層監聽器的監聽端口。
        :type LoadBalancerPort: int
        :param Bandwidth: 計費模式爲按固定頻寬方式時監聽器的限速值，單位：Mbps。
        :type Bandwidth: int
        :param ListenerType: 監聽器的類别：L4Listener（四層監聽器），L7Listener（七層監聽器）。
        :type ListenerType: str
        :param SslMode: 七層監聽器的認證方式：0（不認證，用于http），1（單向認證，用于https），2（雙向認證，用于https）。
        :type SslMode: int
        :param CertId: 七層監聽器關聯的服務端證書ID。
        :type CertId: str
        :param CertCaId: 七層監聽器關聯的用戶端證書ID。
        :type CertCaId: str
        :param Status: 當前綁定關系的健康檢查狀态（Dead代表不健康，Alive代表健康）。
        :type Status: int
        :param AddTimestamp: 創建時間戳。
        :type AddTimestamp: str
        :param RuleSet: 返回的轉發規則清單。
        :type RuleSet: list of L7ListenerInfoRule
        """
        self.ListenerId = None
        self.ListenerName = None
        self.Protocol = None
        self.LoadBalancerPort = None
        self.Bandwidth = None
        self.ListenerType = None
        self.SslMode = None
        self.CertId = None
        self.CertCaId = None
        self.Status = None
        self.AddTimestamp = None
        self.RuleSet = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Protocol = params.get("Protocol")
        self.LoadBalancerPort = params.get("LoadBalancerPort")
        self.Bandwidth = params.get("Bandwidth")
        self.ListenerType = params.get("ListenerType")
        self.SslMode = params.get("SslMode")
        self.CertId = params.get("CertId")
        self.CertCaId = params.get("CertCaId")
        self.Status = params.get("Status")
        self.AddTimestamp = params.get("AddTimestamp")
        if params.get("RuleSet") is not None:
            self.RuleSet = []
            for item in params.get("RuleSet"):
                obj = L7ListenerInfoRule()
                obj._deserialize(item)
                self.RuleSet.append(obj)


class L7ListenerInfoBackend(AbstractModel):
    """查詢綁定了某主機七層監聽器時返回的與轉發路徑所綁定的主機訊息。

    """

    def __init__(self):
        """
        :param BindType: 綁定類别（0代表黑石物理機，1代表虛拟機IP）。
        :type BindType: int
        :param Port: 主機端口。
        :type Port: int
        :param Weight: 權重。
        :type Weight: int
        :param Status: 當前綁定關系的健康檢查狀态（Dead代表不健康，Alive代表健康）。
        :type Status: str
        :param InstanceId: 黑石物理機的主機ID。
        :type InstanceId: str
        :param Alias: 黑石物理機的别名。
        :type Alias: str
        :param LanIp: 主機IP。
        :type LanIp: str
        """
        self.BindType = None
        self.Port = None
        self.Weight = None
        self.Status = None
        self.InstanceId = None
        self.Alias = None
        self.LanIp = None


    def _deserialize(self, params):
        self.BindType = params.get("BindType")
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")
        self.Status = params.get("Status")
        self.InstanceId = params.get("InstanceId")
        self.Alias = params.get("Alias")
        self.LanIp = params.get("LanIp")


class L7ListenerInfoLocation(AbstractModel):
    """查詢綁定了某主機的七層監聽器時返回的轉發路徑。

    """

    def __init__(self):
        """
        :param Url: 轉發路徑。
        :type Url: str
        :param LocationId: 轉發路徑實例ID。
        :type LocationId: str
        :param SessionExpire: 會話保持時間。
        :type SessionExpire: int
        :param HealthSwitch: 是否開啓健康檢查。
        :type HealthSwitch: int
        :param HttpCheckPath: 健康檢查檢查路徑。
        :type HttpCheckPath: str
        :param HttpCheckDomain: 健康檢查檢查域名。
        :type HttpCheckDomain: str
        :param IntervalTime: 健康檢查檢查間隔時間。
        :type IntervalTime: int
        :param HealthNum: 健康檢查健康阈值。
        :type HealthNum: int
        :param UnhealthNum: 健康檢查不健康阈值。
        :type UnhealthNum: int
        :param HttpCodes: 健康檢查中認爲健康的HTTP返回碼的組合。可選值爲1~5的集合，1表示HTTP返回碼爲1xx認爲健康。2表示HTTP返回碼爲2xx認爲健康。3表示HTTP返回碼爲3xx認爲健康。4表示HTTP返回碼爲4xx認爲健康。5表示HTTP返回碼爲5xx認爲健康。
        :type HttpCodes: list of int non-negative
        :param BalanceMode: 均衡方式。
        :type BalanceMode: str
        :param Status: 當前綁定關系的健康檢查狀态（Dead代表不健康，Alive代表健康）。
        :type Status: int
        :param AddTimestamp: 創建時間戳。
        :type AddTimestamp: str
        :param BackendSet: 該轉發路徑所綁定的主機清單。
        :type BackendSet: list of L7ListenerInfoBackend
        """
        self.Url = None
        self.LocationId = None
        self.SessionExpire = None
        self.HealthSwitch = None
        self.HttpCheckPath = None
        self.HttpCheckDomain = None
        self.IntervalTime = None
        self.HealthNum = None
        self.UnhealthNum = None
        self.HttpCodes = None
        self.BalanceMode = None
        self.Status = None
        self.AddTimestamp = None
        self.BackendSet = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.LocationId = params.get("LocationId")
        self.SessionExpire = params.get("SessionExpire")
        self.HealthSwitch = params.get("HealthSwitch")
        self.HttpCheckPath = params.get("HttpCheckPath")
        self.HttpCheckDomain = params.get("HttpCheckDomain")
        self.IntervalTime = params.get("IntervalTime")
        self.HealthNum = params.get("HealthNum")
        self.UnhealthNum = params.get("UnhealthNum")
        self.HttpCodes = params.get("HttpCodes")
        self.BalanceMode = params.get("BalanceMode")
        self.Status = params.get("Status")
        self.AddTimestamp = params.get("AddTimestamp")
        if params.get("BackendSet") is not None:
            self.BackendSet = []
            for item in params.get("BackendSet"):
                obj = L7ListenerInfoBackend()
                obj._deserialize(item)
                self.BackendSet.append(obj)


class L7ListenerInfoRule(AbstractModel):
    """查詢綁定了某主機的七層監聽器時返回的轉發規則。

    """

    def __init__(self):
        """
        :param Domain: 轉發域名。
        :type Domain: str
        :param DomainId: 轉發域名實例ID。
        :type DomainId: str
        :param Status: 當前綁定關系的健康檢查狀态（Dead代表不健康，Alive代表健康）。
        :type Status: int
        :param AddTimestamp: 創建時間戳。
        :type AddTimestamp: str
        :param LocationSet: 該轉發域名下面的轉發路徑清單。
        :type LocationSet: list of L7ListenerInfoLocation
        """
        self.Domain = None
        self.DomainId = None
        self.Status = None
        self.AddTimestamp = None
        self.LocationSet = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        self.Status = params.get("Status")
        self.AddTimestamp = params.get("AddTimestamp")
        if params.get("LocationSet") is not None:
            self.LocationSet = []
            for item in params.get("LocationSet"):
                obj = L7ListenerInfoLocation()
                obj._deserialize(item)
                self.LocationSet.append(obj)


class L7Rule(AbstractModel):
    """獲取七層監聽器轉發規則時返回的轉發規則。

    """

    def __init__(self):
        """
        :param Domain: 轉發域名。
        :type Domain: str
        :param DomainId: 轉發域名實例ID。
        :type DomainId: str
        :param Status: 轉發路徑當前狀态（0代表創建中，1代表正常運作，2代表創建失敗，3代表删除中，4代表删除失敗）。
        :type Status: int
        :param AddTimestamp: 創建時間戳。
        :type AddTimestamp: str
        :param LocationSet: 該轉發域名下面的轉發路徑清單。
        :type LocationSet: list of L7RulesLocation
        """
        self.Domain = None
        self.DomainId = None
        self.Status = None
        self.AddTimestamp = None
        self.LocationSet = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DomainId = params.get("DomainId")
        self.Status = params.get("Status")
        self.AddTimestamp = params.get("AddTimestamp")
        if params.get("LocationSet") is not None:
            self.LocationSet = []
            for item in params.get("LocationSet"):
                obj = L7RulesLocation()
                obj._deserialize(item)
                self.LocationSet.append(obj)


class L7RulesLocation(AbstractModel):
    """獲取七層轉發規則時返回的轉發域名下面的轉發路徑。

    """

    def __init__(self):
        """
        :param Url: 轉發路徑。
        :type Url: str
        :param LocationId: 轉發路徑實例ID。
        :type LocationId: str
        :param SessionExpire: 會話保持時間。
        :type SessionExpire: int
        :param HealthSwitch: 是否開啓健康檢查。
        :type HealthSwitch: int
        :param HttpCheckPath: 健康檢查檢查路徑。
        :type HttpCheckPath: str
        :param HttpCheckDomain: 健康檢查檢查域名。
        :type HttpCheckDomain: str
        :param IntervalTime: 健康檢查檢查間隔時間。
        :type IntervalTime: int
        :param HealthNum: 健康檢查健康阈值。
        :type HealthNum: int
        :param UnhealthNum: 健康檢查不健康阈值。
        :type UnhealthNum: int
        :param HttpCodes: 健康檢查中認爲健康的HTTP返回碼的組合。可選值爲1~5的集合，1表示HTTP返回碼爲1xx認爲健康。2表示HTTP返回碼爲2xx認爲健康。3表示HTTP返回碼爲3xx認爲健康。4表示HTTP返回碼爲4xx認爲健康。5表示HTTP返回碼爲5xx認爲健康。
        :type HttpCodes: list of int non-negative
        :param BalanceMode: 均衡方式。
        :type BalanceMode: str
        :param Status: 轉發路徑當前狀态（0代表創建中，1代表正常運作，2代表創建失敗，3代表删除中，4代表删除失敗）。
        :type Status: int
        :param AddTimestamp: 創建時間戳。
        :type AddTimestamp: str
        """
        self.Url = None
        self.LocationId = None
        self.SessionExpire = None
        self.HealthSwitch = None
        self.HttpCheckPath = None
        self.HttpCheckDomain = None
        self.IntervalTime = None
        self.HealthNum = None
        self.UnhealthNum = None
        self.HttpCodes = None
        self.BalanceMode = None
        self.Status = None
        self.AddTimestamp = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.LocationId = params.get("LocationId")
        self.SessionExpire = params.get("SessionExpire")
        self.HealthSwitch = params.get("HealthSwitch")
        self.HttpCheckPath = params.get("HttpCheckPath")
        self.HttpCheckDomain = params.get("HttpCheckDomain")
        self.IntervalTime = params.get("IntervalTime")
        self.HealthNum = params.get("HealthNum")
        self.UnhealthNum = params.get("UnhealthNum")
        self.HttpCodes = params.get("HttpCodes")
        self.BalanceMode = params.get("BalanceMode")
        self.Status = params.get("Status")
        self.AddTimestamp = params.get("AddTimestamp")


class LoadBalancer(AbstractModel):
    """獲取負載均衡實例清單時返回的負載均衡訊息。

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡器ID
        :type LoadBalancerId: str
        :param ProjectId: 項目ID，通過v2/DescribeProject 介面獲得
        :type ProjectId: int
        :param LoadBalancerName: 負載均衡器名稱
        :type LoadBalancerName: str
        :param LoadBalancerType: 負載均衡的類型 : open表示公網負載均衡類型，internal表示内網負載均衡類型
        :type LoadBalancerType: str
        :param Exclusive: 是否篩選獨占集群，0表示非獨占集群，1表示四層獨占集群，2表示七層獨占集群，3表示四層和七層獨占集群，4表示共享容災
        :type Exclusive: int
        :param TgwSetType: 該負載均衡對應的tgw集群（fullnat,tunnel,dnat）
        :type TgwSetType: str
        :param Domain: 負載均衡域名。規則：1-60個小寫英文字母、數字、點号“.”或連接線“-”。内網類型的負載均衡不能配置該欄位
        :type Domain: str
        :param VpcId: 該負載均衡對應的所在的VpcId
        :type VpcId: str
        :param SubnetId: 該負載均衡對應的所在的SubnetId
        :type SubnetId: str
        :param Status: 無
        :type Status: int
        :param PayMode: 無
        :type PayMode: str
        :param LatestPayMode: 無
        :type LatestPayMode: str
        :param CreateTime: 無
        :type CreateTime: str
        :param StatusTime: 無
        :type StatusTime: str
        :param VpcName: 私有網絡名稱。
        :type VpcName: str
        :param VpcCidrBlock: 私有網絡Cidr。
        :type VpcCidrBlock: str
        :param LoadBalancerVips: 負載均衡獲得的公網IP網址,支援多個
        :type LoadBalancerVips: list of str
        :param SupportListenerTypes: 無
        :type SupportListenerTypes: list of str
        :param Bandwidth: 無
        :type Bandwidth: int
        :param ConfId: 負載均衡個性化配置ID
        :type ConfId: str
        :param ConfName: 無
        :type ConfName: str
        :param LoadBalancerVipv6s: 負載均衡的IPV6的VIP。
        :type LoadBalancerVipv6s: list of str
        :param IpProtocolType: 負載均衡IP協議類型。ipv4或者ipv6。
        :type IpProtocolType: str
        :param BzPayMode: 保障型閘道計費形式
        :type BzPayMode: str
        :param BzL4Metrics: 保障型閘道四層計費指标
        :type BzL4Metrics: str
        :param BzL7Metrics: 保障型閘道七層計費指标
        :type BzL7Metrics: str
        :param IspId: Isp類型。5:騰訊CAP;7:内網。
        :type IspId: str
        """
        self.LoadBalancerId = None
        self.ProjectId = None
        self.LoadBalancerName = None
        self.LoadBalancerType = None
        self.Exclusive = None
        self.TgwSetType = None
        self.Domain = None
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.PayMode = None
        self.LatestPayMode = None
        self.CreateTime = None
        self.StatusTime = None
        self.VpcName = None
        self.VpcCidrBlock = None
        self.LoadBalancerVips = None
        self.SupportListenerTypes = None
        self.Bandwidth = None
        self.ConfId = None
        self.ConfName = None
        self.LoadBalancerVipv6s = None
        self.IpProtocolType = None
        self.BzPayMode = None
        self.BzL4Metrics = None
        self.BzL7Metrics = None
        self.IspId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ProjectId = params.get("ProjectId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.Exclusive = params.get("Exclusive")
        self.TgwSetType = params.get("TgwSetType")
        self.Domain = params.get("Domain")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.PayMode = params.get("PayMode")
        self.LatestPayMode = params.get("LatestPayMode")
        self.CreateTime = params.get("CreateTime")
        self.StatusTime = params.get("StatusTime")
        self.VpcName = params.get("VpcName")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.LoadBalancerVips = params.get("LoadBalancerVips")
        self.SupportListenerTypes = params.get("SupportListenerTypes")
        self.Bandwidth = params.get("Bandwidth")
        self.ConfId = params.get("ConfId")
        self.ConfName = params.get("ConfName")
        self.LoadBalancerVipv6s = params.get("LoadBalancerVipv6s")
        self.IpProtocolType = params.get("IpProtocolType")
        self.BzPayMode = params.get("BzPayMode")
        self.BzL4Metrics = params.get("BzL4Metrics")
        self.BzL7Metrics = params.get("BzL7Metrics")
        self.IspId = params.get("IspId")


class LoadBalancerPortInfoListener(AbstractModel):
    """獲取黑石負載均衡端口相關訊息時返回的監聽器訊息（四層和七層）。

    """

    def __init__(self):
        """
        :param ListenerId: 負載均衡監聽器ID。
        :type ListenerId: str
        :param ListenerName: 監聽器名稱。
        :type ListenerName: str
        :param Protocol: 監聽器協議類型，可選值：http，https，tcp，udp。
        :type Protocol: str
        :param LoadBalancerPort: 監聽器的監聽端口。
        :type LoadBalancerPort: int
        :param Bandwidth: 計費模式爲按固定頻寬方式時監聽器的限速值，單位：Mbps。
        :type Bandwidth: int
        :param Status: 監聽器當前狀态（0代表創建中，1代表正常運作，2代表創建失敗，3代表删除中，4代表删除失敗）。
        :type Status: int
        :param Port: 與監聽器綁定的主機端口。
        :type Port: int
        """
        self.ListenerId = None
        self.ListenerName = None
        self.Protocol = None
        self.LoadBalancerPort = None
        self.Bandwidth = None
        self.Status = None
        self.Port = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Protocol = params.get("Protocol")
        self.LoadBalancerPort = params.get("LoadBalancerPort")
        self.Bandwidth = params.get("Bandwidth")
        self.Status = params.get("Status")
        self.Port = params.get("Port")


class ModifyL4BackendPortRequest(AbstractModel):
    """ModifyL4BackendPort請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID，可通過介面DescribeLoadBalancers查詢。
        :type LoadBalancerId: str
        :param ListenerId: 負載均衡四層監聽器ID，可通過介面DescribeL4Listeners查詢。
        :type ListenerId: str
        :param InstanceId: 黑石物理機主機ID、虛拟機IP或者是半托管主機ID。
        :type InstanceId: str
        :param Port: 已綁定的主機端口。
        :type Port: int
        :param NewPort: 新的主機端口，可選值1~65535。
        :type NewPort: int
        :param BindType: 綁定類型。0：物理機  1：虛拟機 2：半托管機器
        :type BindType: int
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.InstanceId = None
        self.Port = None
        self.NewPort = None
        self.BindType = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.InstanceId = params.get("InstanceId")
        self.Port = params.get("Port")
        self.NewPort = params.get("NewPort")
        self.BindType = params.get("BindType")


class ModifyL4BackendPortResponse(AbstractModel):
    """ModifyL4BackendPort返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID。該介面爲異步任務，可根據本參數調用DescribeLoadBalancerTaskResult介面來查詢任務操作結果
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyL4BackendProbePortRequest(AbstractModel):
    """ModifyL4BackendProbePort請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID，可通過介面DescribeLoadBalancers查詢。
        :type LoadBalancerId: str
        :param ListenerId: 負載均衡四層監聽器ID，可通過介面DescribeL7Listeners查詢。
        :type ListenerId: str
        :param InstanceId: 黑石物理機主機ID、虛拟機IP或者是半托管主機ID。
        :type InstanceId: str
        :param Port: 已綁定的主機端口。
        :type Port: int
        :param ProbePort: 新的探測端口，可選值1~65535。
        :type ProbePort: int
        :param BindType: 綁定類型。0：物理機 1：虛拟機IP 2：半托管機器
        :type BindType: int
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.InstanceId = None
        self.Port = None
        self.ProbePort = None
        self.BindType = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.InstanceId = params.get("InstanceId")
        self.Port = params.get("Port")
        self.ProbePort = params.get("ProbePort")
        self.BindType = params.get("BindType")


class ModifyL4BackendProbePortResponse(AbstractModel):
    """ModifyL4BackendProbePort返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID。該介面爲異步任務，可根據本參數調用DescribeLoadBalancerTaskResult介面來查詢任務操作結果。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyL4BackendWeightRequest(AbstractModel):
    """ModifyL4BackendWeight請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID，可通過介面DescribeLoadBalancers查詢。
        :type LoadBalancerId: str
        :param ListenerId: 負載均衡四層監聽器ID，可通過介面DescribeL4Listeners查詢。
        :type ListenerId: str
        :param InstanceId: 黑石物理機主機ID、虛拟機IP或者是半托管主機ID。
        :type InstanceId: str
        :param Weight: 權重訊息，可選值0~100。
        :type Weight: int
        :param Port: 已綁定的主機端口。
        :type Port: int
        :param BindType: 綁定類型。0：物理機 1：虛拟機 2：半托管機器
        :type BindType: int
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.InstanceId = None
        self.Weight = None
        self.Port = None
        self.BindType = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")
        self.Port = params.get("Port")
        self.BindType = params.get("BindType")


class ModifyL4BackendWeightResponse(AbstractModel):
    """ModifyL4BackendWeight返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID。該介面爲異步任務，可根據本參數調用DescribeLoadBalancerTaskResult介面來查詢任務操作結果。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyL4ListenerRequest(AbstractModel):
    """ModifyL4Listener請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID，可通過介面DescribeLoadBalancers查詢。
        :type LoadBalancerId: str
        :param ListenerId: 四層監聽器ID。可通過介面DescribeL4Listeners查詢。
        :type ListenerId: str
        :param ListenerName: 四層監聽器名稱。
        :type ListenerName: str
        :param SessionExpire: 會話保持時間，單位：秒。可選值：900~3600。
        :type SessionExpire: int
        :param HealthSwitch: 是否開啓健康檢查：1（開啓）、0（關閉）。預設值0，表示關閉。
        :type HealthSwitch: int
        :param TimeOut: 健康檢查的響應超時時間，可選值：2-60，預設值：2，單位:秒。<br><font color="red">響應超時時間要小於檢查間隔時間。</font>
        :type TimeOut: int
        :param IntervalTime: 健康檢查間隔，預設值：5，可選值：5-300，單位：秒。
        :type IntervalTime: int
        :param HealthNum: 健康阈值，預設值：3，表示當連續探測三次健康則表示該轉發正常，可選值：2-10，單位：次。
        :type HealthNum: int
        :param UnhealthNum: 不健康阈值，預設值：3，表示當連續探測三次不健康則表示該轉發不正常，可選值：2-10，單位：次。
        :type UnhealthNum: int
        :param Bandwidth: 監聽器最大頻寬值，用于計費模式爲固定頻寬計費。可選值：0-1000，單位：Mbps。
        :type Bandwidth: int
        :param CustomHealthSwitch: 是否開啓自定義健康檢查：1（開啓）、0（關閉）。預設值0，表示關閉。（該欄位在健康檢查開啓的情況下才生效）
        :type CustomHealthSwitch: int
        :param InputType: 自定義健康探測内容類型，可選值：text（文本）、hexadecimal（十六進制）。
        :type InputType: str
        :param LineSeparatorType: 探測内容類型爲文本方式時，針對請求文本中換行替換方式。可選值：1（替換爲LF）、2（替換爲CR）、3（替換爲LF+CR）。
        :type LineSeparatorType: int
        :param HealthRequest: 自定義探測請求内容。
        :type HealthRequest: str
        :param HealthResponse: 自定義探測返回内容。
        :type HealthResponse: str
        :param ToaFlag: 是否開啓toa。可選值：0（關閉）、1（開啓），預設關閉。（該欄位在負載均衡爲fullnat類型下才生效）
        :type ToaFlag: int
        :param BalanceMode: 四層調度方式。wrr，wlc。
        :type BalanceMode: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.ListenerName = None
        self.SessionExpire = None
        self.HealthSwitch = None
        self.TimeOut = None
        self.IntervalTime = None
        self.HealthNum = None
        self.UnhealthNum = None
        self.Bandwidth = None
        self.CustomHealthSwitch = None
        self.InputType = None
        self.LineSeparatorType = None
        self.HealthRequest = None
        self.HealthResponse = None
        self.ToaFlag = None
        self.BalanceMode = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.SessionExpire = params.get("SessionExpire")
        self.HealthSwitch = params.get("HealthSwitch")
        self.TimeOut = params.get("TimeOut")
        self.IntervalTime = params.get("IntervalTime")
        self.HealthNum = params.get("HealthNum")
        self.UnhealthNum = params.get("UnhealthNum")
        self.Bandwidth = params.get("Bandwidth")
        self.CustomHealthSwitch = params.get("CustomHealthSwitch")
        self.InputType = params.get("InputType")
        self.LineSeparatorType = params.get("LineSeparatorType")
        self.HealthRequest = params.get("HealthRequest")
        self.HealthResponse = params.get("HealthResponse")
        self.ToaFlag = params.get("ToaFlag")
        self.BalanceMode = params.get("BalanceMode")


class ModifyL4ListenerResponse(AbstractModel):
    """ModifyL4Listener返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID。該介面爲異步任務，可根據本參數調用DescribeLoadBalancerTaskResult介面來查詢任務操作結果。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyL7BackendPortRequest(AbstractModel):
    """ModifyL7BackendPort請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID，可通過介面DescribeLoadBalancers查詢。
        :type LoadBalancerId: str
        :param ListenerId: 七層監聽器實例ID，可通過介面DescribeL7Listeners查詢。
        :type ListenerId: str
        :param DomainId: 轉發域名實例ID，可通過介面DescribeL7Rules查詢。
        :type DomainId: str
        :param LocationId: 轉發路徑實例ID，可通過介面DescribeL7Rules查詢。
        :type LocationId: str
        :param InstanceId: 黑石物理機主機ID、虛拟機IP或者是半托管主機ID。
        :type InstanceId: str
        :param Port: 已綁定的主機端口。
        :type Port: int
        :param NewPort: 新的主機端口，可選值1~65535。
        :type NewPort: int
        :param BindType: 綁定類型。0：物理機 1：虛拟機 2：半托管機器
        :type BindType: int
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.DomainId = None
        self.LocationId = None
        self.InstanceId = None
        self.Port = None
        self.NewPort = None
        self.BindType = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.DomainId = params.get("DomainId")
        self.LocationId = params.get("LocationId")
        self.InstanceId = params.get("InstanceId")
        self.Port = params.get("Port")
        self.NewPort = params.get("NewPort")
        self.BindType = params.get("BindType")


class ModifyL7BackendPortResponse(AbstractModel):
    """ModifyL7BackendPort返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID。該介面爲異步任務，可根據本參數調用DescribeLoadBalancerTaskResult介面來查詢任務操作結果。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyL7BackendWeightRequest(AbstractModel):
    """ModifyL7BackendWeight請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID，可通過介面DescribeLoadBalancers查詢。
        :type LoadBalancerId: str
        :param ListenerId: 七層監聽器實例ID，可通過介面DescribeL7Listeners查詢。
        :type ListenerId: str
        :param DomainId: 轉發域名實例ID，可通過介面DescribeL7Rules查詢。
        :type DomainId: str
        :param LocationId: 轉發路徑實例ID，可通過介面DescribeL7Rules查詢。
        :type LocationId: str
        :param InstanceId: 黑石物理機主機ID、虛拟機IP或者是半托管主機ID。
        :type InstanceId: str
        :param Weight: 權重訊息，可選值0~100。
        :type Weight: int
        :param Port: 已綁定的主機端口。
        :type Port: int
        :param BindType: 綁定類型。0：物理機 1：虛拟機 2：半托管機器
        :type BindType: int
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.DomainId = None
        self.LocationId = None
        self.InstanceId = None
        self.Weight = None
        self.Port = None
        self.BindType = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.DomainId = params.get("DomainId")
        self.LocationId = params.get("LocationId")
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")
        self.Port = params.get("Port")
        self.BindType = params.get("BindType")


class ModifyL7BackendWeightResponse(AbstractModel):
    """ModifyL7BackendWeight返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID。該介面爲異步任務，可根據本參數調用DescribeLoadBalancerTaskResult介面來查詢任務操作結果
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyL7ListenerRequest(AbstractModel):
    """ModifyL7Listener請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID，可通過介面DescribeLoadBalancers查詢。
        :type LoadBalancerId: str
        :param ListenerId: 七層監聽器實例ID，可通過介面DescribeL7Listeners查詢。
        :type ListenerId: str
        :param ListenerName: 七層監聽器名稱。
        :type ListenerName: str
        :param SslMode: 認證方式：0（不認證，用于http），1（單向認證，用于https），2（雙向認證，用于https）。
        :type SslMode: int
        :param CertId: 服務端證書ID。
        :type CertId: str
        :param CertName: 服務端證書名稱。
        :type CertName: str
        :param CertContent: 服務端證書内容。
        :type CertContent: str
        :param CertKey: 服務端證書金鑰。
        :type CertKey: str
        :param CertCaId: 用戶端證書ID。
        :type CertCaId: str
        :param CertCaName: 用戶端證書名稱。
        :type CertCaName: str
        :param CertCaContent: 用戶端證書内容。
        :type CertCaContent: str
        :param Bandwidth: 計費模式爲按固定頻寬方式時監聽器的限速值，可選值：0-1000，單位：Mbps。
        :type Bandwidth: int
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.ListenerName = None
        self.SslMode = None
        self.CertId = None
        self.CertName = None
        self.CertContent = None
        self.CertKey = None
        self.CertCaId = None
        self.CertCaName = None
        self.CertCaContent = None
        self.Bandwidth = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.SslMode = params.get("SslMode")
        self.CertId = params.get("CertId")
        self.CertName = params.get("CertName")
        self.CertContent = params.get("CertContent")
        self.CertKey = params.get("CertKey")
        self.CertCaId = params.get("CertCaId")
        self.CertCaName = params.get("CertCaName")
        self.CertCaContent = params.get("CertCaContent")
        self.Bandwidth = params.get("Bandwidth")


class ModifyL7ListenerResponse(AbstractModel):
    """ModifyL7Listener返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID。該介面爲異步任務，可根據本參數調用[DescribeLoadBalancerTaskResult](/document/product/386/9308)介面來查詢任務操作結果
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyL7LocationRule(AbstractModel):
    """修改黑石負載均衡七層轉發路徑時待修改的七層轉發規則訊息。

    """

    def __init__(self):
        """
        :param DomainId: 轉發域名實例ID，可通過介面DescribeL7Rules查詢。
        :type DomainId: str
        :param LocationId: 轉發路徑實例ID，可通過介面DescribeL7Rules查詢。
        :type LocationId: str
        :param Url: 轉發路徑。
        :type Url: str
        :param SessionExpire: 會話保持時間，單位：秒。可選值：30~3600。預設值0，表示不開啓會話保持。
        :type SessionExpire: int
        :param HealthSwitch: 健康檢查開關：1（開啓）、0（關閉）。預設值0，表示關閉。
        :type HealthSwitch: int
        :param IntervalTime: 健康檢查檢查間隔時間，預設值：5，可選值：5-300，單位：秒。
        :type IntervalTime: int
        :param HealthNum: 健康檢查健康阈值，預設值：3，表示當連續探測三次健康則表示該轉發正常，可選值：2-10，單位：次。
        :type HealthNum: int
        :param UnhealthNum: 健康檢查不健康阈值，預設值：5，表示當連續探測五次不健康則表示該轉發不正常，可選值：2-10，單位：次。
        :type UnhealthNum: int
        :param HttpCodes: 健康檢查中認爲健康的HTTP返回碼的組合。可選值爲1~5的集合，1表示HTTP返回碼爲1xx認爲健康。2表示HTTP返回碼爲2xx認爲健康。3表示HTTP返回碼爲3xx認爲健康。4表示HTTP返回碼爲4xx認爲健康。5表示HTTP返回碼爲5xx認爲健康。
        :type HttpCodes: list of int non-negative
        :param HttpCheckPath: 健康檢查檢查路徑。
        :type HttpCheckPath: str
        :param HttpCheckDomain: 健康檢查檢查域名。如果規則的域名使用通配符或正規表示式，則健康檢查檢查域名可自定義，否則必須跟健康檢查檢查域名一樣。不填表示不修改。
        :type HttpCheckDomain: str
        :param BalanceMode: 均衡方式：ip_hash、wrr。預設值wrr。
        :type BalanceMode: str
        :param Domain: 轉發域名。
        :type Domain: str
        """
        self.DomainId = None
        self.LocationId = None
        self.Url = None
        self.SessionExpire = None
        self.HealthSwitch = None
        self.IntervalTime = None
        self.HealthNum = None
        self.UnhealthNum = None
        self.HttpCodes = None
        self.HttpCheckPath = None
        self.HttpCheckDomain = None
        self.BalanceMode = None
        self.Domain = None


    def _deserialize(self, params):
        self.DomainId = params.get("DomainId")
        self.LocationId = params.get("LocationId")
        self.Url = params.get("Url")
        self.SessionExpire = params.get("SessionExpire")
        self.HealthSwitch = params.get("HealthSwitch")
        self.IntervalTime = params.get("IntervalTime")
        self.HealthNum = params.get("HealthNum")
        self.UnhealthNum = params.get("UnhealthNum")
        self.HttpCodes = params.get("HttpCodes")
        self.HttpCheckPath = params.get("HttpCheckPath")
        self.HttpCheckDomain = params.get("HttpCheckDomain")
        self.BalanceMode = params.get("BalanceMode")
        self.Domain = params.get("Domain")


class ModifyL7LocationsRequest(AbstractModel):
    """ModifyL7Locations請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID，可通過介面DescribeLoadBalancers查詢。
        :type LoadBalancerId: str
        :param ListenerId: 七層監聽器實例ID，可通過介面DescribeL7Listeners查詢。
        :type ListenerId: str
        :param RuleSet: 待更新的七層轉發規則訊息數組。
        :type RuleSet: list of ModifyL7LocationRule
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.RuleSet = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("RuleSet") is not None:
            self.RuleSet = []
            for item in params.get("RuleSet"):
                obj = ModifyL7LocationRule()
                obj._deserialize(item)
                self.RuleSet.append(obj)


class ModifyL7LocationsResponse(AbstractModel):
    """ModifyL7Locations返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID。該介面爲異步任務，可根據本參數調用DescribeLoadBalancerTaskResult介面來查詢任務操作結果。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyLoadBalancerChargeModeListener(AbstractModel):
    """修改負載均衡計費方式的監聽器訊息。

    """

    def __init__(self):
        """
        :param ListenerId: 監聽器ID。
        :type ListenerId: str
        :param Protocol: 協議類型。
        :type Protocol: str
        :param Bandwidth: 頻寬。
        :type Bandwidth: int
        """
        self.ListenerId = None
        self.Protocol = None
        self.Bandwidth = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Protocol = params.get("Protocol")
        self.Bandwidth = params.get("Bandwidth")


class ModifyLoadBalancerChargeModeRequest(AbstractModel):
    """ModifyLoadBalancerChargeMode請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID。
        :type LoadBalancerId: str
        :param PayMode: 計費方式。flow或bandwidth。
        :type PayMode: str
        :param ListenerSet: 監聽器訊息，當計費方式選爲 bandwidth 且此負載均衡實例下存在監聽器時需填入此欄位，可以自定義每個監聽器頻寬上限。
        :type ListenerSet: list of ModifyLoadBalancerChargeModeListener
        """
        self.LoadBalancerId = None
        self.PayMode = None
        self.ListenerSet = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.PayMode = params.get("PayMode")
        if params.get("ListenerSet") is not None:
            self.ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = ModifyLoadBalancerChargeModeListener()
                obj._deserialize(item)
                self.ListenerSet.append(obj)


class ModifyLoadBalancerChargeModeResponse(AbstractModel):
    """ModifyLoadBalancerChargeMode返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLoadBalancerRequest(AbstractModel):
    """ModifyLoadBalancer請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID，可通過介面DescribeLoadBalancers查詢。
        :type LoadBalancerId: str
        :param LoadBalancerName: 負載均衡器名稱，規則：1-20個英文、漢字、數字、連接線“-”或下劃線“_”。
        :type LoadBalancerName: str
        :param DomainPrefix: 域名前綴，負載均衡的域名由用戶輸入的域名前綴與配置文件中的域名後綴一起組合而成，保證是唯一的域名。規則：1-20個小寫英文字母、數字或連接線“-”。内網類型的負載均衡不能配置該欄位。
        :type DomainPrefix: str
        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.DomainPrefix = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.DomainPrefix = params.get("DomainPrefix")


class ModifyLoadBalancerResponse(AbstractModel):
    """ModifyLoadBalancer返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID。該介面爲異步任務，可根據本參數調用DescribeLoadBalancerTaskResult介面來查詢任務操作結果。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ReplaceCertRequest(AbstractModel):
    """ReplaceCert請求參數結構體

    """

    def __init__(self):
        """
        :param OldCertId: 要被替換的證書ID
        :type OldCertId: str
        :param NewCert: 證書内容
        :type NewCert: str
        :param NewAlias: 證書名稱
        :type NewAlias: str
        :param NewKey: 私鑰内容，證書類型爲SVR時不需要傳遞
        :type NewKey: str
        :param DeleteOld: 是否删除舊證書，0 表示不删除，1 表示删除
        :type DeleteOld: int
        """
        self.OldCertId = None
        self.NewCert = None
        self.NewAlias = None
        self.NewKey = None
        self.DeleteOld = None


    def _deserialize(self, params):
        self.OldCertId = params.get("OldCertId")
        self.NewCert = params.get("NewCert")
        self.NewAlias = params.get("NewAlias")
        self.NewKey = params.get("NewKey")
        self.DeleteOld = params.get("DeleteOld")


class ReplaceCertResponse(AbstractModel):
    """ReplaceCert返回參數結構體

    """

    def __init__(self):
        """
        :param NewCertId: 新證書ID。
        :type NewCertId: str
        :param OldCertId: 舊證書ID。
        :type OldCertId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NewCertId = None
        self.OldCertId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NewCertId = params.get("NewCertId")
        self.OldCertId = params.get("OldCertId")
        self.RequestId = params.get("RequestId")


class SetTrafficMirrorAliasRequest(AbstractModel):
    """SetTrafficMirrorAlias請求參數結構體

    """

    def __init__(self):
        """
        :param TrafficMirrorId: 流量映像實例ID。
        :type TrafficMirrorId: str
        :param Alias: 流量映像實例别名。
        :type Alias: str
        """
        self.TrafficMirrorId = None
        self.Alias = None


    def _deserialize(self, params):
        self.TrafficMirrorId = params.get("TrafficMirrorId")
        self.Alias = params.get("Alias")


class SetTrafficMirrorAliasResponse(AbstractModel):
    """SetTrafficMirrorAlias返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetTrafficMirrorHealthSwitchRequest(AbstractModel):
    """SetTrafficMirrorHealthSwitch請求參數結構體

    """

    def __init__(self):
        """
        :param TrafficMirrorId: 流量映像實例ID。
        :type TrafficMirrorId: str
        :param HealthSwitch: 健康檢查開關，0：關閉，1：打開
        :type HealthSwitch: int
        :param HealthNum: 健康檢查判斷健康的次數，最小值2，最大值10。
        :type HealthNum: int
        :param UnhealthNum: 健康檢查判斷不健康的次數，最小值2，最大值10。
        :type UnhealthNum: int
        :param IntervalTime: 健康檢查間隔，單位：秒，最小值5，最大值300。
        :type IntervalTime: int
        :param HttpCheckDomain: 檢查的域名配置。
        :type HttpCheckDomain: str
        :param HttpCheckPath: 檢查的路徑配置。
        :type HttpCheckPath: str
        :param HttpCodes: 健康檢查中認爲健康的HTTP返回碼的組合。可選值爲1~5的集合，1表示HTTP返回碼爲1xx認爲健康。2表示HTTP返回碼爲2xx認爲健康。3表示HTTP返回碼爲3xx認爲健康。4表示HTTP返回碼爲4xx認爲健康。5表示HTTP返回碼爲5xx認爲健康。
        :type HttpCodes: list of int
        """
        self.TrafficMirrorId = None
        self.HealthSwitch = None
        self.HealthNum = None
        self.UnhealthNum = None
        self.IntervalTime = None
        self.HttpCheckDomain = None
        self.HttpCheckPath = None
        self.HttpCodes = None


    def _deserialize(self, params):
        self.TrafficMirrorId = params.get("TrafficMirrorId")
        self.HealthSwitch = params.get("HealthSwitch")
        self.HealthNum = params.get("HealthNum")
        self.UnhealthNum = params.get("UnhealthNum")
        self.IntervalTime = params.get("IntervalTime")
        self.HttpCheckDomain = params.get("HttpCheckDomain")
        self.HttpCheckPath = params.get("HttpCheckPath")
        self.HttpCodes = params.get("HttpCodes")


class SetTrafficMirrorHealthSwitchResponse(AbstractModel):
    """SetTrafficMirrorHealthSwitch返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID。該介面爲異步任務，可根據本參數調用DescribeLoadBalancerTaskResult介面來查詢任務操作結果。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class TrafficMirror(AbstractModel):
    """獲取流量映像實例的清單訊息時返回的流量映像訊息。

    """

    def __init__(self):
        """
        :param TrafficMirrorId: 流量映像ID。
        :type TrafficMirrorId: str
        :param Alias: 流量映像名稱。
        :type Alias: str
        :param VpcId: 流量映像所在的私有網絡ID。
        :type VpcId: str
        :param LoadBalancerType: 接收機負載均衡方式。wrr，ip_hash，wlc。
        :type LoadBalancerType: str
        :param HealthSwitch: 是否開始對接收機的健康檢查。0：關閉，非0：開啓。
        :type HealthSwitch: int
        :param HealthNum: 健康阈值。
        :type HealthNum: int
        :param UnhealthNum: 不健康阈值。
        :type UnhealthNum: int
        :param IntervalTime: 檢查間隔。
        :type IntervalTime: int
        :param HttpCheckDomain: 檢查域名。
        :type HttpCheckDomain: str
        :param HttpCheckPath: 檢查目錄。
        :type HttpCheckPath: str
        :param HttpCodes: 健康檢查返回碼。 1：1xx，2：2xx，3：3xx，4：4xx，5：5xx。
        :type HttpCodes: list of int
        :param CreateTime: 創建時間。
        :type CreateTime: str
        :param VpcCidrBlock: 流量映像所在私有網絡的Cidr。
        :type VpcCidrBlock: str
        :param VpcName: 流量映像所在私有網絡的名稱。
        :type VpcName: str
        """
        self.TrafficMirrorId = None
        self.Alias = None
        self.VpcId = None
        self.LoadBalancerType = None
        self.HealthSwitch = None
        self.HealthNum = None
        self.UnhealthNum = None
        self.IntervalTime = None
        self.HttpCheckDomain = None
        self.HttpCheckPath = None
        self.HttpCodes = None
        self.CreateTime = None
        self.VpcCidrBlock = None
        self.VpcName = None


    def _deserialize(self, params):
        self.TrafficMirrorId = params.get("TrafficMirrorId")
        self.Alias = params.get("Alias")
        self.VpcId = params.get("VpcId")
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.HealthSwitch = params.get("HealthSwitch")
        self.HealthNum = params.get("HealthNum")
        self.UnhealthNum = params.get("UnhealthNum")
        self.IntervalTime = params.get("IntervalTime")
        self.HttpCheckDomain = params.get("HttpCheckDomain")
        self.HttpCheckPath = params.get("HttpCheckPath")
        self.HttpCodes = params.get("HttpCodes")
        self.CreateTime = params.get("CreateTime")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.VpcName = params.get("VpcName")


class TrafficMirrorListener(AbstractModel):
    """獲取流量映像的監聽器清單訊息時返回的與流量映像綁定的監聽器訊息。

    """

    def __init__(self):
        """
        :param ListenerId: 監聽器ID。
        :type ListenerId: str
        :param ListenerName: 監聽器名稱。
        :type ListenerName: str
        :param Protocol: 七層監聽器協議類型，可選值：http,https。
        :type Protocol: str
        :param LoadBalancerPort: 監聽器的監聽端口。
        :type LoadBalancerPort: int
        :param Bandwidth: 當前頻寬。
        :type Bandwidth: int
        :param MaxBandwidth: 頻寬上限。
        :type MaxBandwidth: int
        :param ListenerType: 監聽器類型。
        :type ListenerType: str
        :param SslMode: 認證方式：0（不認證，用于http），1（單向認證，用于https），2（雙向認證，用于https）。
        :type SslMode: int
        :param CertId: 服務端證書ID。
        :type CertId: str
        :param CertCaId: 用戶端證書ID。
        :type CertCaId: str
        :param AddTimestamp: 添加時間。
        :type AddTimestamp: str
        :param LoadBalancerId: 負載均衡ID。
        :type LoadBalancerId: str
        :param VpcName: 私有網絡名稱。
        :type VpcName: str
        :param VpcCidrBlock: 私有網絡Cidr。
        :type VpcCidrBlock: str
        :param LoadBalancerVips: 負載均衡的VIP。
        :type LoadBalancerVips: list of str
        :param LoadBalancerName: 負載均衡名稱。
        :type LoadBalancerName: str
        :param LoadBalancerVipv6s: 負載均衡的IPV6的VIP。
        :type LoadBalancerVipv6s: list of str
        :param IpProtocolType: 支援的IP協議類型。ipv4或者是ipv6。
        :type IpProtocolType: str
        """
        self.ListenerId = None
        self.ListenerName = None
        self.Protocol = None
        self.LoadBalancerPort = None
        self.Bandwidth = None
        self.MaxBandwidth = None
        self.ListenerType = None
        self.SslMode = None
        self.CertId = None
        self.CertCaId = None
        self.AddTimestamp = None
        self.LoadBalancerId = None
        self.VpcName = None
        self.VpcCidrBlock = None
        self.LoadBalancerVips = None
        self.LoadBalancerName = None
        self.LoadBalancerVipv6s = None
        self.IpProtocolType = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Protocol = params.get("Protocol")
        self.LoadBalancerPort = params.get("LoadBalancerPort")
        self.Bandwidth = params.get("Bandwidth")
        self.MaxBandwidth = params.get("MaxBandwidth")
        self.ListenerType = params.get("ListenerType")
        self.SslMode = params.get("SslMode")
        self.CertId = params.get("CertId")
        self.CertCaId = params.get("CertCaId")
        self.AddTimestamp = params.get("AddTimestamp")
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.VpcName = params.get("VpcName")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.LoadBalancerVips = params.get("LoadBalancerVips")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.LoadBalancerVipv6s = params.get("LoadBalancerVipv6s")
        self.IpProtocolType = params.get("IpProtocolType")


class TrafficMirrorPortStatus(AbstractModel):
    """流量映像健康檢查返回的接收機的端口及狀态訊息。

    """

    def __init__(self):
        """
        :param Port: 接收機端口。
        :type Port: int
        :param Status: 狀态。
        :type Status: str
        """
        self.Port = None
        self.Status = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.Status = params.get("Status")


class TrafficMirrorReceiver(AbstractModel):
    """獲取與流量映像綁定的接收機訊息時返回的接收機訊息。

    """

    def __init__(self):
        """
        :param InstanceId: 接收機實例ID。
        :type InstanceId: str
        :param Port: 接收機接收端口。
        :type Port: int
        :param Weight: 接收機權重。
        :type Weight: int
        :param TrafficMirrorId: 流量映像ID。
        :type TrafficMirrorId: str
        :param Alias: 接收機别名。
        :type Alias: str
        :param LanIp: 接收機内網IP網址。
        :type LanIp: str
        :param SubnetId: 接收機所在的子網的ID。
        :type SubnetId: str
        :param SubnetName: 接收機所在的子網的名稱。
        :type SubnetName: str
        :param SubnetCidrBlock: 接收機所在的子網的Cidr。
        :type SubnetCidrBlock: str
        :param VpcId: 接收機所在的私有網絡的ID。
        :type VpcId: str
        :param VpcName: 接收機所在的私有網絡的名稱。
        :type VpcName: str
        :param VpcCidrBlock: 接收機所在的私有網絡的Cidr。
        :type VpcCidrBlock: str
        :param HealthStatus: 接收機的健康狀态。
        :type HealthStatus: str
        """
        self.InstanceId = None
        self.Port = None
        self.Weight = None
        self.TrafficMirrorId = None
        self.Alias = None
        self.LanIp = None
        self.SubnetId = None
        self.SubnetName = None
        self.SubnetCidrBlock = None
        self.VpcId = None
        self.VpcName = None
        self.VpcCidrBlock = None
        self.HealthStatus = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")
        self.TrafficMirrorId = params.get("TrafficMirrorId")
        self.Alias = params.get("Alias")
        self.LanIp = params.get("LanIp")
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.SubnetCidrBlock = params.get("SubnetCidrBlock")
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.HealthStatus = params.get("HealthStatus")


class TrafficMirrorReciversStatus(AbstractModel):
    """流量映像健康檢查返回的接收機狀态訊息。

    """

    def __init__(self):
        """
        :param LanIp: 内網IP。
        :type LanIp: str
        :param ReceiversPortStatusSet: 端口及對應的狀态。
        :type ReceiversPortStatusSet: list of TrafficMirrorPortStatus
        """
        self.LanIp = None
        self.ReceiversPortStatusSet = None


    def _deserialize(self, params):
        self.LanIp = params.get("LanIp")
        if params.get("ReceiversPortStatusSet") is not None:
            self.ReceiversPortStatusSet = []
            for item in params.get("ReceiversPortStatusSet"):
                obj = TrafficMirrorPortStatus()
                obj._deserialize(item)
                self.ReceiversPortStatusSet.append(obj)


class UnbindL4Backend(AbstractModel):
    """待與四層監聽器解綁的物理機主機、虛拟機或半托管主機訊息。

    """

    def __init__(self):
        """
        :param Port: 待解綁的主機端口，可選值1~65535。
        :type Port: int
        :param InstanceId: 黑石物理機主機ID、虛拟機IP或者是半托管主機ID。
        :type InstanceId: str
        """
        self.Port = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")


class UnbindL4BackendsRequest(AbstractModel):
    """UnbindL4Backends請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID，可通過介面DescribeLoadBalancers查詢。
        :type LoadBalancerId: str
        :param ListenerId: 負載均衡四層監聽器ID，可通過介面DescribeL4Listeners查詢。
        :type ListenerId: str
        :param BackendSet: 待解綁的主機訊息。可以綁定多個主機端口。目前一個四層監聽器下面最多允許綁定255個主機端口。
        :type BackendSet: list of UnbindL4Backend
        :param BindType: 綁定類型。0：物理機 1：虛拟機 2：半托管機器
        :type BindType: int
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.BackendSet = None
        self.BindType = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("BackendSet") is not None:
            self.BackendSet = []
            for item in params.get("BackendSet"):
                obj = UnbindL4Backend()
                obj._deserialize(item)
                self.BackendSet.append(obj)
        self.BindType = params.get("BindType")


class UnbindL4BackendsResponse(AbstractModel):
    """UnbindL4Backends返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID。該介面爲異步任務，可根據本參數調用DescribeLoadBalancerTaskResult介面來查詢任務操作結果。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class UnbindL7Backend(AbstractModel):
    """待與七層監聽器轉發規則解綁的物理機主機、虛拟機或半托管主機訊息。

    """

    def __init__(self):
        """
        :param Port: 待解綁的主機端口，可選值1~65535。
        :type Port: int
        :param InstanceId: 黑石物理機主機ID、虛拟機IP或者是半托管主機ID。
        :type InstanceId: str
        """
        self.Port = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")


class UnbindL7BackendsRequest(AbstractModel):
    """UnbindL7Backends請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID，可通過介面DescribeLoadBalancers查詢。
        :type LoadBalancerId: str
        :param ListenerId: 七層監聽器實例ID，可通過介面DescribeL7Listeners查詢。
        :type ListenerId: str
        :param DomainId: 轉發域名實例ID，可通過介面DescribeL7Rules查詢。
        :type DomainId: str
        :param LocationId: 轉發路徑實例ID，可通過介面DescribeL7Rules查詢。
        :type LocationId: str
        :param BackendSet: 待綁定的主機訊息。
        :type BackendSet: list of UnbindL7Backend
        :param BindType: 綁定類型。0：物理機  1：虛拟機 2：半托管機器
        :type BindType: int
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.DomainId = None
        self.LocationId = None
        self.BackendSet = None
        self.BindType = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.DomainId = params.get("DomainId")
        self.LocationId = params.get("LocationId")
        if params.get("BackendSet") is not None:
            self.BackendSet = []
            for item in params.get("BackendSet"):
                obj = UnbindL7Backend()
                obj._deserialize(item)
                self.BackendSet.append(obj)
        self.BindType = params.get("BindType")


class UnbindL7BackendsResponse(AbstractModel):
    """UnbindL7Backends返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID。該介面爲異步任務，可根據本參數調用DescribeLoadBalancerTaskResult介面來查詢任務操作結果。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class UnbindTrafficMirrorListenersRequest(AbstractModel):
    """UnbindTrafficMirrorListeners請求參數結構體

    """

    def __init__(self):
        """
        :param TrafficMirrorId: 流量映像實例ID。
        :type TrafficMirrorId: str
        :param ListenerIds: 七層監聽器實例ID數組，可通過介面DescribeL7Listeners查詢。
        :type ListenerIds: list of str
        """
        self.TrafficMirrorId = None
        self.ListenerIds = None


    def _deserialize(self, params):
        self.TrafficMirrorId = params.get("TrafficMirrorId")
        self.ListenerIds = params.get("ListenerIds")


class UnbindTrafficMirrorListenersResponse(AbstractModel):
    """UnbindTrafficMirrorListeners返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID。該介面爲異步任務，可根據本參數調用DescribeLoadBalancerTaskResult介面來查詢任務操作結果。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class UnbindTrafficMirrorReceiver(AbstractModel):
    """待與流量映像解綁的接收機訊息。

    """

    def __init__(self):
        """
        :param Port: 待解綁的主機端口，可選值1~65535。
        :type Port: int
        :param InstanceId: 待解綁的主機實例ID。
        :type InstanceId: str
        """
        self.Port = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")


class UnbindTrafficMirrorReceiversRequest(AbstractModel):
    """UnbindTrafficMirrorReceivers請求參數結構體

    """

    def __init__(self):
        """
        :param TrafficMirrorId: 流量映像實例ID。
        :type TrafficMirrorId: str
        :param ReceiverSet: 待綁定的主機實例ID和端口數組。
        :type ReceiverSet: list of UnbindTrafficMirrorReceiver
        """
        self.TrafficMirrorId = None
        self.ReceiverSet = None


    def _deserialize(self, params):
        self.TrafficMirrorId = params.get("TrafficMirrorId")
        if params.get("ReceiverSet") is not None:
            self.ReceiverSet = []
            for item in params.get("ReceiverSet"):
                obj = UnbindTrafficMirrorReceiver()
                obj._deserialize(item)
                self.ReceiverSet.append(obj)


class UnbindTrafficMirrorReceiversResponse(AbstractModel):
    """UnbindTrafficMirrorReceivers返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID。該介面爲異步任務，可根據本參數調用DescribeLoadBalancerTaskResult介面來查詢任務操作結果。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class UploadCertRequest(AbstractModel):
    """UploadCert請求參數結構體

    """

    def __init__(self):
        """
        :param CertType: 證書類型，可選值：CA，SVR。
        :type CertType: str
        :param Cert: 證書内容。
        :type Cert: str
        :param Alias: 證書别名。
        :type Alias: str
        :param Key: 私鑰内容，證書類型爲SVR時不需要傳遞。
        :type Key: str
        """
        self.CertType = None
        self.Cert = None
        self.Alias = None
        self.Key = None


    def _deserialize(self, params):
        self.CertType = params.get("CertType")
        self.Cert = params.get("Cert")
        self.Alias = params.get("Alias")
        self.Key = params.get("Key")


class UploadCertResponse(AbstractModel):
    """UploadCert返回參數結構體

    """

    def __init__(self):
        """
        :param CertId: 新建的證書ID。
        :type CertId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CertId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.RequestId = params.get("RequestId")