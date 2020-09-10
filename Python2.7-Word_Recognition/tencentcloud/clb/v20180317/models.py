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


class AutoRewriteRequest(AbstractModel):
    """AutoRewrite請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID
        :type LoadBalancerId: str
        :param ListenerId: 監聽器ID
        :type ListenerId: str
        :param Domains: 需要重定向的域名
        :type Domains: list of str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Domains = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.Domains = params.get("Domains")


class AutoRewriteResponse(AbstractModel):
    """AutoRewrite返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Backend(AbstractModel):
    """監聽器後端綁定機器的詳細訊息

    """

    def __init__(self):
        """
        :param Type: 轉發目标的類型，目前僅可取值爲 CVM
        :type Type: str
        :param InstanceId: 雲伺服器的唯一 ID，可通過 DescribeInstances 介面返回欄位中的 unInstanceId 欄位獲取
        :type InstanceId: str
        :param Port: 後端雲伺服器監聽端口
        :type Port: int
        :param Weight: 後端雲伺服器的轉發權重，取值範圍：0~100，預設爲 10。
        :type Weight: int
        :param PublicIpAddresses: 雲伺服器的外網 IP
注意：此欄位可能返回 null，表示取不到有效值。
        :type PublicIpAddresses: list of str
        :param PrivateIpAddresses: 雲伺服器的内網 IP
注意：此欄位可能返回 null，表示取不到有效值。
        :type PrivateIpAddresses: list of str
        :param InstanceName: 雲伺服器實例名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param RegisteredTime: 雲伺服器被綁定到監聽器的時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type RegisteredTime: str
        """
        self.Type = None
        self.InstanceId = None
        self.Port = None
        self.Weight = None
        self.PublicIpAddresses = None
        self.PrivateIpAddresses = None
        self.InstanceName = None
        self.RegisteredTime = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.InstanceId = params.get("InstanceId")
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.InstanceName = params.get("InstanceName")
        self.RegisteredTime = params.get("RegisteredTime")


class BatchModifyTargetWeightRequest(AbstractModel):
    """BatchModifyTargetWeight請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例 ID
        :type LoadBalancerId: str
        :param ModifyList: 要批次修改權重的清單
        :type ModifyList: list of RsWeightRule
        """
        self.LoadBalancerId = None
        self.ModifyList = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("ModifyList") is not None:
            self.ModifyList = []
            for item in params.get("ModifyList"):
                obj = RsWeightRule()
                obj._deserialize(item)
                self.ModifyList.append(obj)


class BatchModifyTargetWeightResponse(AbstractModel):
    """BatchModifyTargetWeight返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CertificateInput(AbstractModel):
    """證書訊息

    """

    def __init__(self):
        """
        :param SSLMode: 認證類型，UNIDIRECTIONAL：單向認證，MUTUAL：雙向認證
        :type SSLMode: str
        :param CertId: 服務端證書的 ID，如果不填寫此項則必須上傳證書，包括 CertContent，CertKey，CertName。
        :type CertId: str
        :param CertCaId: 用戶端證書的 ID，如果 SSLMode=mutual，監聽器如果不填寫此項則必須上傳用戶端證書，包括 CertCaContent，CertCaName。
        :type CertCaId: str
        :param CertName: 上傳服務端證書的名稱，如果沒有 CertId，則此項必傳。
        :type CertName: str
        :param CertKey: 上傳服務端證書的 key，如果沒有 CertId，則此項必傳。
        :type CertKey: str
        :param CertContent: 上傳服務端證書的内容，如果沒有 CertId，則此項必傳。
        :type CertContent: str
        :param CertCaName: 上傳用戶端 CA 證書的名稱，如果 SSLMode=mutual，如果沒有 CertCaId，則此項必傳。
        :type CertCaName: str
        :param CertCaContent: 上傳用戶端證書的内容，如果 SSLMode=mutual，如果沒有 CertCaId，則此項必傳。
        :type CertCaContent: str
        """
        self.SSLMode = None
        self.CertId = None
        self.CertCaId = None
        self.CertName = None
        self.CertKey = None
        self.CertContent = None
        self.CertCaName = None
        self.CertCaContent = None


    def _deserialize(self, params):
        self.SSLMode = params.get("SSLMode")
        self.CertId = params.get("CertId")
        self.CertCaId = params.get("CertCaId")
        self.CertName = params.get("CertName")
        self.CertKey = params.get("CertKey")
        self.CertContent = params.get("CertContent")
        self.CertCaName = params.get("CertCaName")
        self.CertCaContent = params.get("CertCaContent")


class CertificateOutput(AbstractModel):
    """證書相關訊息

    """

    def __init__(self):
        """
        :param SSLMode: 認證類型，unidirectional：單向認證，mutual：雙向認證
        :type SSLMode: str
        :param CertId: 服務端證書的 ID。
        :type CertId: str
        :param CertCaId: 用戶端證書的 ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertCaId: str
        """
        self.SSLMode = None
        self.CertId = None
        self.CertCaId = None


    def _deserialize(self, params):
        self.SSLMode = params.get("SSLMode")
        self.CertId = params.get("CertId")
        self.CertCaId = params.get("CertCaId")


class ClassicalHealth(AbstractModel):
    """傳統型負載均衡健康狀态訊息

    """

    def __init__(self):
        """
        :param IP: 雲伺服器内網 IP
        :type IP: str
        :param Port: 雲伺服器端口
        :type Port: int
        :param ListenerPort: 負載均衡監聽端口
        :type ListenerPort: int
        :param Protocol: 轉發協議
        :type Protocol: str
        :param HealthStatus: 健康檢查結果，1 表示健康，0 表示不健康
        :type HealthStatus: int
        """
        self.IP = None
        self.Port = None
        self.ListenerPort = None
        self.Protocol = None
        self.HealthStatus = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.Port = params.get("Port")
        self.ListenerPort = params.get("ListenerPort")
        self.Protocol = params.get("Protocol")
        self.HealthStatus = params.get("HealthStatus")


class ClassicalListener(AbstractModel):
    """傳統型負載均衡監聽器訊息

    """

    def __init__(self):
        """
        :param ListenerId: 負載均衡監聽器ID
        :type ListenerId: str
        :param ListenerPort: 負載均衡監聽器端口
        :type ListenerPort: int
        :param InstancePort: 監聽器後端轉發端口
        :type InstancePort: int
        :param ListenerName: 監聽器名稱
        :type ListenerName: str
        :param Protocol: 監聽器協議類型
        :type Protocol: str
        :param SessionExpire: 會話保持時間
        :type SessionExpire: int
        :param HealthSwitch: 是否開啓了檢查：1（開啓）、0（關閉）
        :type HealthSwitch: int
        :param TimeOut: 響應超時時間
        :type TimeOut: int
        :param IntervalTime: 檢查間隔
        :type IntervalTime: int
        :param HealthNum: 健康阈值
        :type HealthNum: int
        :param UnhealthNum: 不健康阈值
        :type UnhealthNum: int
        :param HttpHash: 公網固定IP型的 HTTP、HTTPS 協議監聽器的輪詢方法。wrr 表示按權重輪詢，ip_hash 表示根據訪問的源 IP 進行一緻性哈希方式來分發
        :type HttpHash: str
        :param HttpCode: 公網固定IP型的 HTTP、HTTPS 協議監聽器的健康檢查返回碼。具體可參考創建監聽器中對該欄位的解釋
        :type HttpCode: int
        :param HttpCheckPath: 公網固定IP型的 HTTP、HTTPS 協議監聽器的健康檢查路徑
        :type HttpCheckPath: str
        :param SSLMode: 公網固定IP型的 HTTPS 協議監聽器的認證方式
        :type SSLMode: str
        :param CertId: 公網固定IP型的 HTTPS 協議監聽器服務端證書 ID
        :type CertId: str
        :param CertCaId: 公網固定IP型的 HTTPS 協議監聽器用戶端證書 ID
        :type CertCaId: str
        :param Status: 監聽器的狀态，0 表示創建中，1 表示運作中
        :type Status: int
        """
        self.ListenerId = None
        self.ListenerPort = None
        self.InstancePort = None
        self.ListenerName = None
        self.Protocol = None
        self.SessionExpire = None
        self.HealthSwitch = None
        self.TimeOut = None
        self.IntervalTime = None
        self.HealthNum = None
        self.UnhealthNum = None
        self.HttpHash = None
        self.HttpCode = None
        self.HttpCheckPath = None
        self.SSLMode = None
        self.CertId = None
        self.CertCaId = None
        self.Status = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerPort = params.get("ListenerPort")
        self.InstancePort = params.get("InstancePort")
        self.ListenerName = params.get("ListenerName")
        self.Protocol = params.get("Protocol")
        self.SessionExpire = params.get("SessionExpire")
        self.HealthSwitch = params.get("HealthSwitch")
        self.TimeOut = params.get("TimeOut")
        self.IntervalTime = params.get("IntervalTime")
        self.HealthNum = params.get("HealthNum")
        self.UnhealthNum = params.get("UnhealthNum")
        self.HttpHash = params.get("HttpHash")
        self.HttpCode = params.get("HttpCode")
        self.HttpCheckPath = params.get("HttpCheckPath")
        self.SSLMode = params.get("SSLMode")
        self.CertId = params.get("CertId")
        self.CertCaId = params.get("CertCaId")
        self.Status = params.get("Status")


class ClassicalLoadBalancerInfo(AbstractModel):
    """負載均衡訊息

    """

    def __init__(self):
        """
        :param InstanceId: 後端實例ID
        :type InstanceId: str
        :param LoadBalancerIds: 負載均衡實例ID清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type LoadBalancerIds: list of str
        """
        self.InstanceId = None
        self.LoadBalancerIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.LoadBalancerIds = params.get("LoadBalancerIds")


class ClassicalTarget(AbstractModel):
    """傳統型負載均衡後端訊息

    """

    def __init__(self):
        """
        :param Type: 轉發目标的類型，目前僅可取值爲 CVM
        :type Type: str
        :param InstanceId: 雲伺服器的唯一 ID，可通過 DescribeInstances 介面返回欄位中的 unInstanceId 欄位獲取
        :type InstanceId: str
        :param Weight: 後端雲伺服器的轉發權重，取值範圍：0~100，預設爲 10。
        :type Weight: int
        :param PublicIpAddresses: 雲伺服器的外網 IP
注意：此欄位可能返回 null，表示取不到有效值。
        :type PublicIpAddresses: list of str
        :param PrivateIpAddresses: 雲伺服器的内網 IP
注意：此欄位可能返回 null，表示取不到有效值。
        :type PrivateIpAddresses: list of str
        :param InstanceName: 雲伺服器實例名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param RunFlag: 雲伺服器狀态
1：故障，2：運作中，3：創建中，4：已關機，5：已退還，6：退還中， 7：重啓中，8：開機中，9：關機中，10：密碼重置中，11：格式化中，12：映像制作中，13：頻寬設置中，14：重灌系統中，19：升級中，21：熱遷移中
注意：此欄位可能返回 null，表示取不到有效值。
        :type RunFlag: int
        """
        self.Type = None
        self.InstanceId = None
        self.Weight = None
        self.PublicIpAddresses = None
        self.PrivateIpAddresses = None
        self.InstanceName = None
        self.RunFlag = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.InstanceName = params.get("InstanceName")
        self.RunFlag = params.get("RunFlag")


class ClassicalTargetInfo(AbstractModel):
    """傳統型後端訊息

    """

    def __init__(self):
        """
        :param InstanceId: 後端實例ID
        :type InstanceId: str
        :param Weight: 權重 取值爲0-100
        :type Weight: int
        """
        self.InstanceId = None
        self.Weight = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")


class CreateListenerRequest(AbstractModel):
    """CreateListener請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例 ID
        :type LoadBalancerId: str
        :param Ports: 要将監聽器創建到哪些端口，每個端口對應一個新的監聽器
        :type Ports: list of int
        :param Protocol: 監聽器協議： TCP | UDP | HTTP | HTTPS | TCP_SSL（TCP_SSL 正在内測中，如需使用請通過工單申請）
        :type Protocol: str
        :param ListenerNames: 要創建的監聽器名稱清單，名稱與Ports數組按序一一對應，如不需立即命名，則無需提供此參數
        :type ListenerNames: list of str
        :param HealthCheck: 健康檢查相關參數，此參數僅适用于TCP/UDP/TCP_SSL監聽器
        :type HealthCheck: :class:`taifucloudcloud.clb.v20180317.models.HealthCheck`
        :param Certificate: 證書相關訊息，此參數僅适用于HTTPS/TCP_SSL監聽器
        :type Certificate: :class:`taifucloudcloud.clb.v20180317.models.CertificateInput`
        :param SessionExpireTime: 會話保持時間，單位：秒。可選值：30~3600，預設 0，表示不開啓。此參數僅适用于TCP/UDP監聽器。
        :type SessionExpireTime: int
        :param Scheduler: 監聽器轉發的方式。可選值：WRR、LEAST_CONN
分别表示按權重輪詢、最小連接數， 預設爲 WRR。此參數僅适用于TCP/UDP/TCP_SSL監聽器。
        :type Scheduler: str
        :param SniSwitch: 是否開啓SNI特性，此參數僅适用于HTTPS監聽器。
        :type SniSwitch: int
        """
        self.LoadBalancerId = None
        self.Ports = None
        self.Protocol = None
        self.ListenerNames = None
        self.HealthCheck = None
        self.Certificate = None
        self.SessionExpireTime = None
        self.Scheduler = None
        self.SniSwitch = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.Ports = params.get("Ports")
        self.Protocol = params.get("Protocol")
        self.ListenerNames = params.get("ListenerNames")
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        if params.get("Certificate") is not None:
            self.Certificate = CertificateInput()
            self.Certificate._deserialize(params.get("Certificate"))
        self.SessionExpireTime = params.get("SessionExpireTime")
        self.Scheduler = params.get("Scheduler")
        self.SniSwitch = params.get("SniSwitch")


class CreateListenerResponse(AbstractModel):
    """CreateListener返回參數結構體

    """

    def __init__(self):
        """
        :param ListenerIds: 創建的監聽器的唯一标識數組
        :type ListenerIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ListenerIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ListenerIds = params.get("ListenerIds")
        self.RequestId = params.get("RequestId")


class CreateLoadBalancerRequest(AbstractModel):
    """CreateLoadBalancer請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerType: 負載均衡實例的網絡類型：
OPEN：公網屬性， INTERNAL：内網屬性。
        :type LoadBalancerType: str
        :param Forward: 負載均衡實例。1：應用型，0：傳統型，預設爲應用型負載均衡實例。
        :type Forward: int
        :param LoadBalancerName: 負載均衡實例的名稱，只用來創建一個的時候生效。規則：1-50 個英文、漢字、數字、連接線“-”或下劃線“_”。
注意：如果名稱與系統中已有負載均衡實例的名稱重複的話，則系統将會自動生成此次創建的負載均衡實例的名稱。
        :type LoadBalancerName: str
        :param VpcId: 負載均衡後端實例所屬網絡 ID，可以通過 DescribeVpcEx 介面獲取。 不填則預設爲基礎網絡。
        :type VpcId: str
        :param SubnetId: 在私有網絡内購買内網負載均衡實例的時候需要指定子網 ID，内網負載均衡實例的 VIP 将從這個子網中産生。其他情況不用填寫該欄位。
        :type SubnetId: str
        :param ProjectId: 負載均衡實例所屬的項目 ID，可以通過 DescribeProject 介面獲取。不填則屬于預設項目。
        :type ProjectId: int
        """
        self.LoadBalancerType = None
        self.Forward = None
        self.LoadBalancerName = None
        self.VpcId = None
        self.SubnetId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.Forward = params.get("Forward")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ProjectId = params.get("ProjectId")


class CreateLoadBalancerResponse(AbstractModel):
    """CreateLoadBalancer返回參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerIds: 由負載均衡實例統一 ID 組成的數組。
        :type LoadBalancerIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.LoadBalancerIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.RequestId = params.get("RequestId")


class CreateRuleRequest(AbstractModel):
    """CreateRule請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例 ID
        :type LoadBalancerId: str
        :param ListenerId: 監聽器 ID
        :type ListenerId: str
        :param Rules: 新建轉發規則的訊息
        :type Rules: list of RuleInput
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Rules = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleInput()
                obj._deserialize(item)
                self.Rules.append(obj)


class CreateRuleResponse(AbstractModel):
    """CreateRule返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteListenerRequest(AbstractModel):
    """DeleteListener請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 應用型負載均衡實例 ID
        :type LoadBalancerId: str
        :param ListenerId: 要删除的監聽器 ID
        :type ListenerId: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")


class DeleteListenerResponse(AbstractModel):
    """DeleteListener返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLoadBalancerRequest(AbstractModel):
    """DeleteLoadBalancer請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerIds: 要删除的負載均衡實例 ID數組
        :type LoadBalancerIds: list of str
        """
        self.LoadBalancerIds = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")


class DeleteLoadBalancerResponse(AbstractModel):
    """DeleteLoadBalancer返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRewriteRequest(AbstractModel):
    """DeleteRewrite請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID
        :type LoadBalancerId: str
        :param SourceListenerId: 源監聽器ID
        :type SourceListenerId: str
        :param TargetListenerId: 目标監聽器ID
        :type TargetListenerId: str
        :param RewriteInfos: 轉發規則之間的重定向關系
        :type RewriteInfos: list of RewriteLocationMap
        """
        self.LoadBalancerId = None
        self.SourceListenerId = None
        self.TargetListenerId = None
        self.RewriteInfos = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.SourceListenerId = params.get("SourceListenerId")
        self.TargetListenerId = params.get("TargetListenerId")
        if params.get("RewriteInfos") is not None:
            self.RewriteInfos = []
            for item in params.get("RewriteInfos"):
                obj = RewriteLocationMap()
                obj._deserialize(item)
                self.RewriteInfos.append(obj)


class DeleteRewriteResponse(AbstractModel):
    """DeleteRewrite返回參數結構體

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
        :param LoadBalancerId: 負載均衡實例 ID
        :type LoadBalancerId: str
        :param ListenerId: 應用型負載均衡監聽器 ID
        :type ListenerId: str
        :param LocationIds: 要删除的轉發規則的ID組成的數組
        :type LocationIds: list of str
        :param Domain: 要删除的轉發規則的域名，已提供LocationIds參數時本參數不生效
        :type Domain: str
        :param Url: 要删除的轉發規則的轉發路徑，已提供LocationIds參數時本參數不生效
        :type Url: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.LocationIds = None
        self.Domain = None
        self.Url = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.LocationIds = params.get("LocationIds")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")


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


class DeregisterTargetsFromClassicalLBRequest(AbstractModel):
    """DeregisterTargetsFromClassicalLB請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例 ID
        :type LoadBalancerId: str
        :param InstanceIds: 後端實例ID清單
        :type InstanceIds: list of str
        """
        self.LoadBalancerId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.InstanceIds = params.get("InstanceIds")


class DeregisterTargetsFromClassicalLBResponse(AbstractModel):
    """DeregisterTargetsFromClassicalLB返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeregisterTargetsRequest(AbstractModel):
    """DeregisterTargets請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例 ID
        :type LoadBalancerId: str
        :param ListenerId: 監聽器 ID
        :type ListenerId: str
        :param Targets: 要解綁的後端機器清單，數組長度最大支援20
        :type Targets: list of Target
        :param LocationId: 轉發規則的ID，當從七層轉發規則解綁機器時，必須提供此參數或Domain+Url兩者之一
        :type LocationId: str
        :param Domain: 目标規則的域名，提供LocationId參數時本參數不生效
        :type Domain: str
        :param Url: 目标規則的URL，提供LocationId參數時本參數不生效
        :type Url: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Targets = None
        self.LocationId = None
        self.Domain = None
        self.Url = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")


class DeregisterTargetsResponse(AbstractModel):
    """DeregisterTargets返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeClassicalLBByInstanceIdRequest(AbstractModel):
    """DescribeClassicalLBByInstanceId請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 後端實例ID清單
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class DescribeClassicalLBByInstanceIdResponse(AbstractModel):
    """DescribeClassicalLBByInstanceId返回參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerInfoList: 負載均衡相關訊息清單
        :type LoadBalancerInfoList: list of ClassicalLoadBalancerInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.LoadBalancerInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoadBalancerInfoList") is not None:
            self.LoadBalancerInfoList = []
            for item in params.get("LoadBalancerInfoList"):
                obj = ClassicalLoadBalancerInfo()
                obj._deserialize(item)
                self.LoadBalancerInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClassicalLBHealthStatusRequest(AbstractModel):
    """DescribeClassicalLBHealthStatus請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例 ID
        :type LoadBalancerId: str
        :param ListenerId: 負載均衡監聽器ID
        :type ListenerId: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")


class DescribeClassicalLBHealthStatusResponse(AbstractModel):
    """DescribeClassicalLBHealthStatus返回參數結構體

    """

    def __init__(self):
        """
        :param HealthList: 後端健康狀态清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type HealthList: list of ClassicalHealth
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.HealthList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HealthList") is not None:
            self.HealthList = []
            for item in params.get("HealthList"):
                obj = ClassicalHealth()
                obj._deserialize(item)
                self.HealthList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClassicalLBListenersRequest(AbstractModel):
    """DescribeClassicalLBListeners請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例 ID
        :type LoadBalancerId: str
        :param ListenerIds: 負載均衡監聽器ID清單， 範圍[1-65535]
        :type ListenerIds: list of str
        :param Protocol: 負載均衡監聽的協議, 'TCP', 'UDP', 'HTTP', 'HTTPS'
        :type Protocol: str
        :param ListenerPort: 負載均衡監聽端口
        :type ListenerPort: int
        :param Status: 監聽器的狀态，0 表示創建中，1 表示運作中
        :type Status: int
        """
        self.LoadBalancerId = None
        self.ListenerIds = None
        self.Protocol = None
        self.ListenerPort = None
        self.Status = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerIds = params.get("ListenerIds")
        self.Protocol = params.get("Protocol")
        self.ListenerPort = params.get("ListenerPort")
        self.Status = params.get("Status")


class DescribeClassicalLBListenersResponse(AbstractModel):
    """DescribeClassicalLBListeners返回參數結構體

    """

    def __init__(self):
        """
        :param Listeners: 監聽器清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Listeners: list of ClassicalListener
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Listeners = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Listeners") is not None:
            self.Listeners = []
            for item in params.get("Listeners"):
                obj = ClassicalListener()
                obj._deserialize(item)
                self.Listeners.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClassicalLBTargetsRequest(AbstractModel):
    """DescribeClassicalLBTargets請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例 ID
        :type LoadBalancerId: str
        """
        self.LoadBalancerId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")


class DescribeClassicalLBTargetsResponse(AbstractModel):
    """DescribeClassicalLBTargets返回參數結構體

    """

    def __init__(self):
        """
        :param Targets: 後端服務清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Targets: list of ClassicalTarget
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Targets = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = ClassicalTarget()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeListenersRequest(AbstractModel):
    """DescribeListeners請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例 ID
        :type LoadBalancerId: str
        :param ListenerIds: 要查詢的應用型負載均衡監聽器 ID數組
        :type ListenerIds: list of str
        :param Protocol: 要查詢的監聽器協議類型，取值 TCP | UDP | HTTP | HTTPS | TCP_SSL
        :type Protocol: str
        :param Port: 要查詢的監聽器的端口
        :type Port: int
        """
        self.LoadBalancerId = None
        self.ListenerIds = None
        self.Protocol = None
        self.Port = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerIds = params.get("ListenerIds")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")


class DescribeListenersResponse(AbstractModel):
    """DescribeListeners返回參數結構體

    """

    def __init__(self):
        """
        :param Listeners: 監聽器清單
        :type Listeners: list of Listener
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Listeners = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Listeners") is not None:
            self.Listeners = []
            for item in params.get("Listeners"):
                obj = Listener()
                obj._deserialize(item)
                self.Listeners.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancersRequest(AbstractModel):
    """DescribeLoadBalancers請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerIds: 負載均衡實例 ID。
        :type LoadBalancerIds: list of str
        :param LoadBalancerType: 負載均衡實例的網絡類型：
OPEN：公網屬性， INTERNAL：内網屬性。
        :type LoadBalancerType: str
        :param Forward: 1：應用型，0：傳統型。
        :type Forward: int
        :param LoadBalancerName: 負載均衡實例名稱。
        :type LoadBalancerName: str
        :param Domain: Top Cloud 爲負載均衡實例分配的域名，應用型負載均衡該欄位無意義。
        :type Domain: str
        :param LoadBalancerVips: 負載均衡實例的 VIP 網址，支援多個。
        :type LoadBalancerVips: list of str
        :param BackendPublicIps: 後端雲伺服器的外網 IP。
        :type BackendPublicIps: list of str
        :param BackendPrivateIps: 後端雲伺服器的内網 IP。
        :type BackendPrivateIps: list of str
        :param Offset: 數據偏移量，預設爲 0。
        :type Offset: int
        :param Limit: 返回負載均衡個數，預設爲 20。
        :type Limit: int
        :param OrderBy: 排序欄位，支援以下欄位：LoadBalancerName，CreateTime，Domain，LoadBalancerType。
        :type OrderBy: str
        :param OrderType: 1：倒序，0：順序，預設按照創建時間倒序。
        :type OrderType: int
        :param SearchKey: 搜索欄位，模糊比對名稱、域名、VIP。
        :type SearchKey: str
        :param ProjectId: 負載均衡實例所屬的項目 ID，可以通過 DescribeProject 介面獲取。
        :type ProjectId: int
        :param WithRs: 查詢的負載均衡是否綁定後端服務器，0：沒有綁定雲伺服器，1：綁定雲伺服器，-1：查詢全部。
        :type WithRs: int
        :param VpcId: 負載均衡實例所屬私有網絡，如 vpc-bhqkbhdx，
基礎網絡不支援通過VpcId查詢。
        :type VpcId: str
        :param SecurityGroup: 安全組ID，如 sg-m1cc9123
        :type SecurityGroup: str
        """
        self.LoadBalancerIds = None
        self.LoadBalancerType = None
        self.Forward = None
        self.LoadBalancerName = None
        self.Domain = None
        self.LoadBalancerVips = None
        self.BackendPublicIps = None
        self.BackendPrivateIps = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None
        self.OrderType = None
        self.SearchKey = None
        self.ProjectId = None
        self.WithRs = None
        self.VpcId = None
        self.SecurityGroup = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.Forward = params.get("Forward")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.Domain = params.get("Domain")
        self.LoadBalancerVips = params.get("LoadBalancerVips")
        self.BackendPublicIps = params.get("BackendPublicIps")
        self.BackendPrivateIps = params.get("BackendPrivateIps")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.SearchKey = params.get("SearchKey")
        self.ProjectId = params.get("ProjectId")
        self.WithRs = params.get("WithRs")
        self.VpcId = params.get("VpcId")
        self.SecurityGroup = params.get("SecurityGroup")


class DescribeLoadBalancersResponse(AbstractModel):
    """DescribeLoadBalancers返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 滿足過濾條件的負載均衡實例總數。
        :type TotalCount: int
        :param LoadBalancerSet: 返回的負載均衡實例數組。
        :type LoadBalancerSet: list of LoadBalancer
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.LoadBalancerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("LoadBalancerSet") is not None:
            self.LoadBalancerSet = []
            for item in params.get("LoadBalancerSet"):
                obj = LoadBalancer()
                obj._deserialize(item)
                self.LoadBalancerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRewriteRequest(AbstractModel):
    """DescribeRewrite請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID
        :type LoadBalancerId: str
        :param SourceListenerIds: 負載均衡監聽器ID數組
        :type SourceListenerIds: list of str
        :param SourceLocationIds: 負載均衡轉發規則的ID數組
        :type SourceLocationIds: list of str
        """
        self.LoadBalancerId = None
        self.SourceListenerIds = None
        self.SourceLocationIds = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.SourceListenerIds = params.get("SourceListenerIds")
        self.SourceLocationIds = params.get("SourceLocationIds")


class DescribeRewriteResponse(AbstractModel):
    """DescribeRewrite返回參數結構體

    """

    def __init__(self):
        """
        :param RewriteSet: 重定向轉發規則構成的數組，若無重定向規則，則返回空數組
        :type RewriteSet: list of RuleOutput
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RewriteSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RewriteSet") is not None:
            self.RewriteSet = []
            for item in params.get("RewriteSet"):
                obj = RuleOutput()
                obj._deserialize(item)
                self.RewriteSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTargetHealthRequest(AbstractModel):
    """DescribeTargetHealth請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerIds: 要查詢的負載均衡實例 ID清單
        :type LoadBalancerIds: list of str
        """
        self.LoadBalancerIds = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")


class DescribeTargetHealthResponse(AbstractModel):
    """DescribeTargetHealth返回參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancers: 負載均衡實例清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type LoadBalancers: list of LoadBalancerHealth
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.LoadBalancers = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoadBalancers") is not None:
            self.LoadBalancers = []
            for item in params.get("LoadBalancers"):
                obj = LoadBalancerHealth()
                obj._deserialize(item)
                self.LoadBalancers.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTargetsRequest(AbstractModel):
    """DescribeTargets請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例 ID
        :type LoadBalancerId: str
        :param ListenerIds: 監聽器 ID清單
        :type ListenerIds: list of str
        :param Protocol: 監聽器協議類型
        :type Protocol: str
        :param Port: 負載均衡監聽器端口
        :type Port: int
        """
        self.LoadBalancerId = None
        self.ListenerIds = None
        self.Protocol = None
        self.Port = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerIds = params.get("ListenerIds")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")


class DescribeTargetsResponse(AbstractModel):
    """DescribeTargets返回參數結構體

    """

    def __init__(self):
        """
        :param Listeners: 監聽器後端綁定的機器訊息
        :type Listeners: list of ListenerBackend
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Listeners = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Listeners") is not None:
            self.Listeners = []
            for item in params.get("Listeners"):
                obj = ListenerBackend()
                obj._deserialize(item)
                self.Listeners.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 請求ID，即介面返回的RequestId
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class DescribeTaskStatusResponse(AbstractModel):
    """DescribeTaskStatus返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 任務的當前狀态。 0：成功，1：失敗，2：進行中。
        :type Status: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class HealthCheck(AbstractModel):
    """健康檢查訊息

    """

    def __init__(self):
        """
        :param HealthSwitch: 是否開啓健康檢查：1（開啓）、0（關閉）。
        :type HealthSwitch: int
        :param TimeOut: 健康檢查的響應超時時間，可選值：2~60，預設值：2，單位：秒。響應超時時間要小於檢查間隔時間。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TimeOut: int
        :param IntervalTime: 健康檢查探測間隔時間，預設值：5，可選值：5~300，單位：秒。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IntervalTime: int
        :param HealthNum: 健康阈值，預設值：3，表示當連續探測三次健康則表示該轉發正常，可選值：2~10，單位：次。
注意：此欄位可能返回 null，表示取不到有效值。
        :type HealthNum: int
        :param UnHealthNum: 不健康阈值，預設值：3，表示當連續探測三次不健康則表示該轉發異常，可選值：2~10，單位：次。
注意：此欄位可能返回 null，表示取不到有效值。
        :type UnHealthNum: int
        :param HttpCode: 健康檢查狀态碼（僅适用于HTTP/HTTPS轉發規則）。可選值：1~31，預設 31。
1 表示探測後返回值 1xx 表示健康，2 表示返回 2xx 表示健康，4 表示返回 3xx 表示健康，8 表示返回 4xx 表示健康，16 表示返回 5xx 表示健康。若希望多種碼都表示健康，則将相應的值相加。
注意：此欄位可能返回 null，表示取不到有效值。
        :type HttpCode: int
        :param HttpCheckPath: 健康檢查路徑（僅适用于HTTP/HTTPS轉發規則）。
注意：此欄位可能返回 null，表示取不到有效值。
        :type HttpCheckPath: str
        :param HttpCheckDomain: 健康檢查域名（僅适用于HTTP/HTTPS轉發規則）。
注意：此欄位可能返回 null，表示取不到有效值。
        :type HttpCheckDomain: str
        :param HttpCheckMethod: 健康檢查方法（僅适用于HTTP/HTTPS轉發規則），取值爲HEAD或GET。
注意：此欄位可能返回 null，表示取不到有效值。
        :type HttpCheckMethod: str
        """
        self.HealthSwitch = None
        self.TimeOut = None
        self.IntervalTime = None
        self.HealthNum = None
        self.UnHealthNum = None
        self.HttpCode = None
        self.HttpCheckPath = None
        self.HttpCheckDomain = None
        self.HttpCheckMethod = None


    def _deserialize(self, params):
        self.HealthSwitch = params.get("HealthSwitch")
        self.TimeOut = params.get("TimeOut")
        self.IntervalTime = params.get("IntervalTime")
        self.HealthNum = params.get("HealthNum")
        self.UnHealthNum = params.get("UnHealthNum")
        self.HttpCode = params.get("HttpCode")
        self.HttpCheckPath = params.get("HttpCheckPath")
        self.HttpCheckDomain = params.get("HttpCheckDomain")
        self.HttpCheckMethod = params.get("HttpCheckMethod")


class Listener(AbstractModel):
    """監聽器的訊息

    """

    def __init__(self):
        """
        :param ListenerId: 應用型負載均衡監聽器 ID
        :type ListenerId: str
        :param Protocol: 監聽器協議
        :type Protocol: str
        :param Port: 監聽器端口
        :type Port: int
        :param Certificate: 監聽器綁定的證書訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Certificate: :class:`taifucloudcloud.clb.v20180317.models.CertificateOutput`
        :param HealthCheck: 監聽器的健康檢查訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type HealthCheck: :class:`taifucloudcloud.clb.v20180317.models.HealthCheck`
        :param Scheduler: 請求的調度方式
注意：此欄位可能返回 null，表示取不到有效值。
        :type Scheduler: str
        :param SessionExpireTime: 會話保持時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type SessionExpireTime: int
        :param SniSwitch: 是否開啓SNI特性（本參數僅對于HTTPS監聽器有意義）
注意：此欄位可能返回 null，表示取不到有效值。
        :type SniSwitch: int
        :param Rules: 監聽器下的全部轉發規則（本參數僅對于HTTP/HTTPS監聽器有意義）
注意：此欄位可能返回 null，表示取不到有效值。
        :type Rules: list of RuleOutput
        :param ListenerName: 監聽器的名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ListenerName: str
        """
        self.ListenerId = None
        self.Protocol = None
        self.Port = None
        self.Certificate = None
        self.HealthCheck = None
        self.Scheduler = None
        self.SessionExpireTime = None
        self.SniSwitch = None
        self.Rules = None
        self.ListenerName = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        if params.get("Certificate") is not None:
            self.Certificate = CertificateOutput()
            self.Certificate._deserialize(params.get("Certificate"))
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        self.Scheduler = params.get("Scheduler")
        self.SessionExpireTime = params.get("SessionExpireTime")
        self.SniSwitch = params.get("SniSwitch")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleOutput()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.ListenerName = params.get("ListenerName")


class ListenerBackend(AbstractModel):
    """監聽器上注冊的後端機器的訊息

    """

    def __init__(self):
        """
        :param ListenerId: 監聽器 ID
        :type ListenerId: str
        :param Protocol: 監聽器的協議
        :type Protocol: str
        :param Port: 監聽器的端口
        :type Port: int
        :param Rules: 監聽器下的規則訊息（僅适用于HTTP/HTTPS監聽器）
注意：此欄位可能返回 null，表示取不到有效值。
        :type Rules: list of RuleTargets
        :param Targets: 監聽器上注冊的機器清單（僅适用于TCP/UDP/TCP_SSL監聽器）
注意：此欄位可能返回 null，表示取不到有效值。
        :type Targets: list of Backend
        """
        self.ListenerId = None
        self.Protocol = None
        self.Port = None
        self.Rules = None
        self.Targets = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleTargets()
                obj._deserialize(item)
                self.Rules.append(obj)
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Backend()
                obj._deserialize(item)
                self.Targets.append(obj)


class ListenerHealth(AbstractModel):
    """監聽器的健康檢查訊息

    """

    def __init__(self):
        """
        :param ListenerId: 監聽器ID
        :type ListenerId: str
        :param ListenerName: 監聽器名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ListenerName: str
        :param Protocol: 監聽器的協議
        :type Protocol: str
        :param Port: 監聽器的端口
        :type Port: int
        :param Rules: 監聽器的轉發規則清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Rules: list of RuleHealth
        """
        self.ListenerId = None
        self.ListenerName = None
        self.Protocol = None
        self.Port = None
        self.Rules = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleHealth()
                obj._deserialize(item)
                self.Rules.append(obj)


class LoadBalancer(AbstractModel):
    """負載均衡實例的訊息

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例 ID。
        :type LoadBalancerId: str
        :param LoadBalancerName: 負載均衡實例的名稱。
        :type LoadBalancerName: str
        :param LoadBalancerType: 負載均衡實例的網絡類型：
OPEN：公網屬性， INTERNAL：内網屬性。
        :type LoadBalancerType: str
        :param Forward: 應用型負載均衡标識，1：應用型負載均衡，0：傳統型的負載均衡。
        :type Forward: int
        :param Domain: 負載均衡實例的域名，内網類型負載均衡以及應用型負載均衡實例不提供該欄位
注意：此欄位可能返回 null，表示取不到有效值。
        :type Domain: str
        :param LoadBalancerVips: 負載均衡實例的 VIP 清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type LoadBalancerVips: list of str
        :param Status: 負載均衡實例的狀态，包括
0：創建中，1：正常運作。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: int
        :param CreateTime: 負載均衡實例的創建時間。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param StatusTime: 負載均衡實例的上次狀态轉換時間。
注意：此欄位可能返回 null，表示取不到有效值。
        :type StatusTime: str
        :param ProjectId: 負載均衡實例所屬的項目 ID， 0 表示預設項目。
        :type ProjectId: int
        :param VpcId: 私有網絡的 ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param OpenBgp: 高防 LB 的标識，1：高防負載均衡 0：非高防負載均衡。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OpenBgp: int
        :param Snat: 在 2016 年 12 月份之前的傳統型内網負載均衡都是開啓了 snat 的。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Snat: bool
        :param Isolation: 0：表示未被隔離，1：表示被隔離。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Isolation: int
        :param Log: 用戶開啓日志的訊息，日志只有公網屬性創建了 HTTP 、HTTPS 監聽器的負載均衡才會有日志。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Log: str
        :param SubnetId: 負載均衡實例所在的子網（僅對内網VPC型LB有意義）
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param Tags: 負載均衡實例的标簽訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Tags: list of TagInfo
        :param SecureGroups: 負載均衡實例的安全組
注意：此欄位可能返回 null，表示取不到有效值。
        :type SecureGroups: list of str
        :param TargetRegionInfo: 負載均衡實例綁定的後端設備的基本訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type TargetRegionInfo: :class:`taifucloudcloud.clb.v20180317.models.TargetRegionInfo`
        :param AnycastZone: anycast負載均衡的發布域，對于非anycast的負載均衡，此欄位返回爲空字串
注意：此欄位可能返回 null，表示取不到有效值。
        :type AnycastZone: str
        :param AddressIPVersion: IP版本，ipv4 | ipv6
注意：此欄位可能返回 null，表示取不到有效值。
        :type AddressIPVersion: str
        :param NumericalVpcId: 數值形式的私有網絡 ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type NumericalVpcId: int
        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.LoadBalancerType = None
        self.Forward = None
        self.Domain = None
        self.LoadBalancerVips = None
        self.Status = None
        self.CreateTime = None
        self.StatusTime = None
        self.ProjectId = None
        self.VpcId = None
        self.OpenBgp = None
        self.Snat = None
        self.Isolation = None
        self.Log = None
        self.SubnetId = None
        self.Tags = None
        self.SecureGroups = None
        self.TargetRegionInfo = None
        self.AnycastZone = None
        self.AddressIPVersion = None
        self.NumericalVpcId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.Forward = params.get("Forward")
        self.Domain = params.get("Domain")
        self.LoadBalancerVips = params.get("LoadBalancerVips")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.StatusTime = params.get("StatusTime")
        self.ProjectId = params.get("ProjectId")
        self.VpcId = params.get("VpcId")
        self.OpenBgp = params.get("OpenBgp")
        self.Snat = params.get("Snat")
        self.Isolation = params.get("Isolation")
        self.Log = params.get("Log")
        self.SubnetId = params.get("SubnetId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.SecureGroups = params.get("SecureGroups")
        if params.get("TargetRegionInfo") is not None:
            self.TargetRegionInfo = TargetRegionInfo()
            self.TargetRegionInfo._deserialize(params.get("TargetRegionInfo"))
        self.AnycastZone = params.get("AnycastZone")
        self.AddressIPVersion = params.get("AddressIPVersion")
        self.NumericalVpcId = params.get("NumericalVpcId")


class LoadBalancerHealth(AbstractModel):
    """負載均衡實例的健康檢查狀态

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID
        :type LoadBalancerId: str
        :param LoadBalancerName: 負載均衡實例名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type LoadBalancerName: str
        :param Listeners: 監聽器清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Listeners: list of ListenerHealth
        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.Listeners = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        if params.get("Listeners") is not None:
            self.Listeners = []
            for item in params.get("Listeners"):
                obj = ListenerHealth()
                obj._deserialize(item)
                self.Listeners.append(obj)


class ManualRewriteRequest(AbstractModel):
    """ManualRewrite請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID
        :type LoadBalancerId: str
        :param SourceListenerId: 源監聽器ID
        :type SourceListenerId: str
        :param TargetListenerId: 目标監聽器ID
        :type TargetListenerId: str
        :param RewriteInfos: 轉發規則之間的重定向關系
        :type RewriteInfos: list of RewriteLocationMap
        """
        self.LoadBalancerId = None
        self.SourceListenerId = None
        self.TargetListenerId = None
        self.RewriteInfos = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.SourceListenerId = params.get("SourceListenerId")
        self.TargetListenerId = params.get("TargetListenerId")
        if params.get("RewriteInfos") is not None:
            self.RewriteInfos = []
            for item in params.get("RewriteInfos"):
                obj = RewriteLocationMap()
                obj._deserialize(item)
                self.RewriteInfos.append(obj)


class ManualRewriteResponse(AbstractModel):
    """ManualRewrite返回參數結構體

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
        :param LoadBalancerId: 負載均衡實例 ID
        :type LoadBalancerId: str
        :param ListenerId: 應用型負載均衡監聽器 ID
        :type ListenerId: str
        :param Domain: 監聽器下的某個舊域名。
        :type Domain: str
        :param NewDomain: 新域名，	長度限制爲：1-80。有三種使用格式：非正規表示式格式，通配符格式，正規表示式格式。非正規表示式格式只能使用字母、數字、‘-’、‘.’。通配符格式的使用 ‘*’ 只能在開頭或者結尾。正規表示式以'~'開頭。
        :type NewDomain: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Domain = None
        self.NewDomain = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.NewDomain = params.get("NewDomain")


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


class ModifyListenerRequest(AbstractModel):
    """ModifyListener請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例 ID
        :type LoadBalancerId: str
        :param ListenerId: 負載均衡監聽器 ID
        :type ListenerId: str
        :param ListenerName: 新的監聽器名稱
        :type ListenerName: str
        :param SessionExpireTime: 會話保持時間，單位：秒。可選值：30~3600，預設 0，表示不開啓。此參數僅适用于TCP/UDP監聽器。
        :type SessionExpireTime: int
        :param HealthCheck: 健康檢查相關參數，此參數僅适用于TCP/UDP/TCP_SSL監聽器
        :type HealthCheck: :class:`taifucloudcloud.clb.v20180317.models.HealthCheck`
        :param Certificate: 證書相關訊息，此參數僅适用于HTTPS/TCP_SSL監聽器
        :type Certificate: :class:`taifucloudcloud.clb.v20180317.models.CertificateInput`
        :param Scheduler: 監聽器轉發的方式。可選值：WRR、LEAST_CONN
分别表示按權重輪詢、最小連接數， 預設爲 WRR。
        :type Scheduler: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.ListenerName = None
        self.SessionExpireTime = None
        self.HealthCheck = None
        self.Certificate = None
        self.Scheduler = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.SessionExpireTime = params.get("SessionExpireTime")
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        if params.get("Certificate") is not None:
            self.Certificate = CertificateInput()
            self.Certificate._deserialize(params.get("Certificate"))
        self.Scheduler = params.get("Scheduler")


class ModifyListenerResponse(AbstractModel):
    """ModifyListener返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLoadBalancerAttributesRequest(AbstractModel):
    """ModifyLoadBalancerAttributes請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡的唯一ID
        :type LoadBalancerId: str
        :param LoadBalancerName: 負載均衡實例名稱
        :type LoadBalancerName: str
        :param TargetRegionInfo: 負載均衡綁定的後端服務的地域訊息
        :type TargetRegionInfo: :class:`taifucloudcloud.clb.v20180317.models.TargetRegionInfo`
        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.TargetRegionInfo = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        if params.get("TargetRegionInfo") is not None:
            self.TargetRegionInfo = TargetRegionInfo()
            self.TargetRegionInfo._deserialize(params.get("TargetRegionInfo"))


class ModifyLoadBalancerAttributesResponse(AbstractModel):
    """ModifyLoadBalancerAttributes返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRuleRequest(AbstractModel):
    """ModifyRule請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例 ID
        :type LoadBalancerId: str
        :param ListenerId: 應用型負載均衡監聽器 ID
        :type ListenerId: str
        :param LocationId: 要修改的轉發規則的 ID。
        :type LocationId: str
        :param Url: 轉發規則的新的轉發路徑，如不需修改Url，則不需提供此參數
        :type Url: str
        :param HealthCheck: 健康檢查訊息
        :type HealthCheck: :class:`taifucloudcloud.clb.v20180317.models.HealthCheck`
        :param Scheduler: 規則的請求轉發方式
        :type Scheduler: str
        :param SessionExpireTime: 會話保持時間
        :type SessionExpireTime: int
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.LocationId = None
        self.Url = None
        self.HealthCheck = None
        self.Scheduler = None
        self.SessionExpireTime = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.LocationId = params.get("LocationId")
        self.Url = params.get("Url")
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        self.Scheduler = params.get("Scheduler")
        self.SessionExpireTime = params.get("SessionExpireTime")


class ModifyRuleResponse(AbstractModel):
    """ModifyRule返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTargetPortRequest(AbstractModel):
    """ModifyTargetPort請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例 ID
        :type LoadBalancerId: str
        :param ListenerId: 負載均衡監聽器 ID
        :type ListenerId: str
        :param Targets: 要修改端口的後端機器清單
        :type Targets: list of Target
        :param NewPort: 後端機器綁定到監聽器的新端口
        :type NewPort: int
        :param LocationId: 轉發規則的ID
        :type LocationId: str
        :param Domain: 目标規則的域名，提供LocationId參數時本參數不生效
        :type Domain: str
        :param Url: 目标規則的URL，提供LocationId參數時本參數不生效
        :type Url: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Targets = None
        self.NewPort = None
        self.LocationId = None
        self.Domain = None
        self.Url = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.NewPort = params.get("NewPort")
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")


class ModifyTargetPortResponse(AbstractModel):
    """ModifyTargetPort返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTargetWeightRequest(AbstractModel):
    """ModifyTargetWeight請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例 ID
        :type LoadBalancerId: str
        :param ListenerId: 負載均衡監聽器 ID
        :type ListenerId: str
        :param Weight: 後端雲伺服器新的轉發權重，取值範圍：0~100。
        :type Weight: int
        :param LocationId: 轉發規則的ID，當綁定機器到七層轉發規則時，必須提供此參數或Domain+Url兩者之一
        :type LocationId: str
        :param Domain: 目标規則的域名，提供LocationId參數時本參數不生效
        :type Domain: str
        :param Url: 目标規則的URL，提供LocationId參數時本參數不生效
        :type Url: str
        :param Targets: 要修改權重的後端機器清單
        :type Targets: list of Target
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Weight = None
        self.LocationId = None
        self.Domain = None
        self.Url = None
        self.Targets = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.Weight = params.get("Weight")
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)


class ModifyTargetWeightResponse(AbstractModel):
    """ModifyTargetWeight返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegisterTargetsRequest(AbstractModel):
    """RegisterTargets請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例 ID
        :type LoadBalancerId: str
        :param ListenerId: 負載均衡監聽器 ID
        :type ListenerId: str
        :param Targets: 要注冊的後端機器清單，數組長度最大支援20
        :type Targets: list of Target
        :param LocationId: 轉發規則的ID，當注冊機器到七層轉發規則時，必須提供此參數或Domain+Url兩者之一
        :type LocationId: str
        :param Domain: 目标規則的域名，提供LocationId參數時本參數不生效
        :type Domain: str
        :param Url: 目标規則的URL，提供LocationId參數時本參數不生效
        :type Url: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Targets = None
        self.LocationId = None
        self.Domain = None
        self.Url = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")


class RegisterTargetsResponse(AbstractModel):
    """RegisterTargets返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegisterTargetsWithClassicalLBRequest(AbstractModel):
    """RegisterTargetsWithClassicalLB請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例 ID
        :type LoadBalancerId: str
        :param Targets: 後端服務訊息
        :type Targets: list of ClassicalTargetInfo
        """
        self.LoadBalancerId = None
        self.Targets = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = ClassicalTargetInfo()
                obj._deserialize(item)
                self.Targets.append(obj)


class RegisterTargetsWithClassicalLBResponse(AbstractModel):
    """RegisterTargetsWithClassicalLB返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RewriteLocationMap(AbstractModel):
    """轉發規則之間的重定向關系

    """

    def __init__(self):
        """
        :param SourceLocationId: 源轉發規則ID
        :type SourceLocationId: str
        :param TargetLocationId: 重定向至的目标轉發規則ID
        :type TargetLocationId: str
        """
        self.SourceLocationId = None
        self.TargetLocationId = None


    def _deserialize(self, params):
        self.SourceLocationId = params.get("SourceLocationId")
        self.TargetLocationId = params.get("TargetLocationId")


class RewriteTarget(AbstractModel):
    """重定向目标的訊息

    """

    def __init__(self):
        """
        :param TargetListenerId: 重定向目标的監聽器ID
注意：此欄位可能返回 null，表示無重定向。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TargetListenerId: str
        :param TargetLocationId: 重定向目标的轉發規則ID
注意：此欄位可能返回 null，表示無重定向。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TargetLocationId: str
        """
        self.TargetListenerId = None
        self.TargetLocationId = None


    def _deserialize(self, params):
        self.TargetListenerId = params.get("TargetListenerId")
        self.TargetLocationId = params.get("TargetLocationId")


class RsWeightRule(AbstractModel):
    """修改節點權重的數據類型

    """

    def __init__(self):
        """
        :param ListenerId: 負載均衡監聽器 ID
        :type ListenerId: str
        :param LocationId: 轉發規則的ID
        :type LocationId: str
        :param Targets: 要修改權重的後端機器清單
        :type Targets: list of Target
        :param Domain: 目标規則的域名，提供LocationId參數時本參數不生效
        :type Domain: str
        :param Url: 目标規則的URL，提供LocationId參數時本參數不生效
        :type Url: str
        :param Weight: 後端雲伺服器新的轉發權重，取值範圍：0~100。
        :type Weight: int
        """
        self.ListenerId = None
        self.LocationId = None
        self.Targets = None
        self.Domain = None
        self.Url = None
        self.Weight = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.LocationId = params.get("LocationId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        self.Weight = params.get("Weight")


class RuleHealth(AbstractModel):
    """一條轉發規則的健康檢查狀态

    """

    def __init__(self):
        """
        :param LocationId: 轉發規則ID
        :type LocationId: str
        :param Domain: 轉發規則的域名
注意：此欄位可能返回 null，表示取不到有效值。
        :type Domain: str
        :param Url: 轉發規則的Url
注意：此欄位可能返回 null，表示取不到有效值。
        :type Url: str
        :param Targets: 本規則上綁定的後端的健康檢查狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type Targets: list of TargetHealth
        """
        self.LocationId = None
        self.Domain = None
        self.Url = None
        self.Targets = None


    def _deserialize(self, params):
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = TargetHealth()
                obj._deserialize(item)
                self.Targets.append(obj)


class RuleInput(AbstractModel):
    """HTTP/HTTPS轉發規則（輸入）

    """

    def __init__(self):
        """
        :param Domain: 轉發規則的域名。
        :type Domain: str
        :param Url: 轉發規則的路徑。
        :type Url: str
        :param SessionExpireTime: 會話保持時間
        :type SessionExpireTime: int
        :param HealthCheck: 健康檢查訊息
        :type HealthCheck: :class:`taifucloudcloud.clb.v20180317.models.HealthCheck`
        :param Certificate: 證書訊息
        :type Certificate: :class:`taifucloudcloud.clb.v20180317.models.CertificateInput`
        :param Scheduler: 規則的請求轉發方式
        :type Scheduler: str
        """
        self.Domain = None
        self.Url = None
        self.SessionExpireTime = None
        self.HealthCheck = None
        self.Certificate = None
        self.Scheduler = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        self.SessionExpireTime = params.get("SessionExpireTime")
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        if params.get("Certificate") is not None:
            self.Certificate = CertificateInput()
            self.Certificate._deserialize(params.get("Certificate"))
        self.Scheduler = params.get("Scheduler")


class RuleOutput(AbstractModel):
    """HTTP/HTTPS監聽器的轉發規則（輸出）

    """

    def __init__(self):
        """
        :param LocationId: 轉發規則的 ID
        :type LocationId: str
        :param Domain: 轉發規則的域名。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Domain: str
        :param Url: 轉發規則的路徑。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Url: str
        :param SessionExpireTime: 會話保持時間
        :type SessionExpireTime: int
        :param HealthCheck: 健康檢查訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type HealthCheck: :class:`taifucloudcloud.clb.v20180317.models.HealthCheck`
        :param Certificate: 證書訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Certificate: :class:`taifucloudcloud.clb.v20180317.models.CertificateOutput`
        :param Scheduler: 規則的請求轉發方式
        :type Scheduler: str
        :param ListenerId: 轉發規則所屬的監聽器 ID
        :type ListenerId: str
        :param RewriteTarget: 轉發規則的重定向目标訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type RewriteTarget: :class:`taifucloudcloud.clb.v20180317.models.RewriteTarget`
        :param HttpGzip: 是否開啓gzip
        :type HttpGzip: bool
        :param BeAutoCreated: 轉發規則是否爲自動創建
        :type BeAutoCreated: bool
        :param DefaultServer: 是否作爲預設域名
        :type DefaultServer: bool
        :param Http2: 是否開啓Http2
        :type Http2: bool
        """
        self.LocationId = None
        self.Domain = None
        self.Url = None
        self.SessionExpireTime = None
        self.HealthCheck = None
        self.Certificate = None
        self.Scheduler = None
        self.ListenerId = None
        self.RewriteTarget = None
        self.HttpGzip = None
        self.BeAutoCreated = None
        self.DefaultServer = None
        self.Http2 = None


    def _deserialize(self, params):
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        self.SessionExpireTime = params.get("SessionExpireTime")
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        if params.get("Certificate") is not None:
            self.Certificate = CertificateOutput()
            self.Certificate._deserialize(params.get("Certificate"))
        self.Scheduler = params.get("Scheduler")
        self.ListenerId = params.get("ListenerId")
        if params.get("RewriteTarget") is not None:
            self.RewriteTarget = RewriteTarget()
            self.RewriteTarget._deserialize(params.get("RewriteTarget"))
        self.HttpGzip = params.get("HttpGzip")
        self.BeAutoCreated = params.get("BeAutoCreated")
        self.DefaultServer = params.get("DefaultServer")
        self.Http2 = params.get("Http2")


class RuleTargets(AbstractModel):
    """HTTP/HTTPS監聽器下的轉發規則的機器綁定訊息

    """

    def __init__(self):
        """
        :param LocationId: 轉發規則的 ID
        :type LocationId: str
        :param Domain: 轉發規則的域名
        :type Domain: str
        :param Url: 轉發規則的路徑。
        :type Url: str
        :param Targets: 後端機器的訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Targets: list of Backend
        """
        self.LocationId = None
        self.Domain = None
        self.Url = None
        self.Targets = None


    def _deserialize(self, params):
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Backend()
                obj._deserialize(item)
                self.Targets.append(obj)


class SetLoadBalancerSecurityGroupsRequest(AbstractModel):
    """SetLoadBalancerSecurityGroups請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例 ID
        :type LoadBalancerId: str
        :param SecurityGroups: 安全組ID構成的數組，一個負載均衡實例最多關聯50個安全組，如果要解綁所有安全組，可不傳此參數。
        :type SecurityGroups: list of str
        """
        self.LoadBalancerId = None
        self.SecurityGroups = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.SecurityGroups = params.get("SecurityGroups")


class SetLoadBalancerSecurityGroupsResponse(AbstractModel):
    """SetLoadBalancerSecurityGroups返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TagInfo(AbstractModel):
    """負載均衡的标簽訊息

    """

    def __init__(self):
        """
        :param TagKey: 标簽的鍵
        :type TagKey: str
        :param TagValue: 标簽的值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class Target(AbstractModel):
    """轉發目标，即綁定在負載均衡上的後端機器

    """

    def __init__(self):
        """
        :param InstanceId: 雲伺服器的唯一 ID，可通過 DescribeInstances 介面返回欄位中的 unInstanceId 欄位獲取
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param Port: 後端雲伺服器監聽端口
注意：此欄位可能返回 null，表示取不到有效值。
        :type Port: int
        :param Type: 轉發目标的類型，目前僅可取值爲 CVM
注意：此欄位可能返回 null，表示取不到有效值。
        :type Type: str
        :param Weight: 後端雲伺服器的轉發權重，取值範圍：0~100，預設爲 10。
        :type Weight: int
        """
        self.InstanceId = None
        self.Port = None
        self.Type = None
        self.Weight = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Port = params.get("Port")
        self.Type = params.get("Type")
        self.Weight = params.get("Weight")


class TargetHealth(AbstractModel):
    """描述一個Target的健康訊息

    """

    def __init__(self):
        """
        :param IP: Target的内網IP
        :type IP: str
        :param Port: Target綁定的端口
        :type Port: int
        :param HealthStatus: 當前健康狀态，true：健康，false：不健康。
        :type HealthStatus: bool
        :param TargetId: Target的實例ID，如 ins-12345678
        :type TargetId: str
        """
        self.IP = None
        self.Port = None
        self.HealthStatus = None
        self.TargetId = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.Port = params.get("Port")
        self.HealthStatus = params.get("HealthStatus")
        self.TargetId = params.get("TargetId")


class TargetRegionInfo(AbstractModel):
    """負載均衡實例所綁定的後端服務的訊息，包括所屬地域、所屬網絡。

    """

    def __init__(self):
        """
        :param Region: Target所屬地域，如 ap-guangzhou
        :type Region: str
        :param VpcId: Target所屬網絡，私有網絡格式如 vpc-abcd1234，如果是基礎網絡，則爲"0"
        :type VpcId: str
        """
        self.Region = None
        self.VpcId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.VpcId = params.get("VpcId")