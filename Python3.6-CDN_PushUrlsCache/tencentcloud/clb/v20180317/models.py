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


class AssociateTargetGroupsRequest(AbstractModel):
    """AssociateTargetGroups請求參數結構體

    """

    def __init__(self):
        """
        :param Associations: 綁定的關系數組
        :type Associations: list of TargetGroupAssociation
        """
        self.Associations = None


    def _deserialize(self, params):
        if params.get("Associations") is not None:
            self.Associations = []
            for item in params.get("Associations"):
                obj = TargetGroupAssociation()
                obj._deserialize(item)
                self.Associations.append(obj)


class AssociateTargetGroupsResponse(AbstractModel):
    """AssociateTargetGroups返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AssociationItem(AbstractModel):
    """目标組關聯到的規則

    """

    def __init__(self):
        """
        :param LoadBalancerId: 關聯到的負載均衡ID
        :type LoadBalancerId: str
        :param ListenerId: 關聯到的監聽器ID
        :type ListenerId: str
        :param LocationId: 關聯到的轉發規則ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type LocationId: str
        :param Protocol: 關聯到的監聽器協議類型，如HTTP,TCP,
        :type Protocol: str
        :param Port: 關聯到的監聽器端口
        :type Port: int
        :param Domain: 關聯到的轉發規則域名
注意：此欄位可能返回 null，表示取不到有效值。
        :type Domain: str
        :param Url: 關聯到的轉發規則URL
注意：此欄位可能返回 null，表示取不到有效值。
        :type Url: str
        :param LoadBalancerName: 負載均衡名稱
        :type LoadBalancerName: str
        :param ListenerName: 監聽器名稱
        :type ListenerName: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.LocationId = None
        self.Protocol = None
        self.Port = None
        self.Domain = None
        self.Url = None
        self.LoadBalancerName = None
        self.ListenerName = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.LocationId = params.get("LocationId")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.ListenerName = params.get("ListenerName")


class AutoRewriteRequest(AbstractModel):
    """AutoRewrite請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例ID
        :type LoadBalancerId: str
        :param ListenerId: HTTPS:443監聽器的ID
        :type ListenerId: str
        :param Domains: HTTPS:443監聽器下需要重定向的域名
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
    """監聽器綁定的後端服務的詳細訊息

    """

    def __init__(self):
        """
        :param Type: 後端服務的類型，可取：CVM、ENI（即将支援）
        :type Type: str
        :param InstanceId: 後端服務的唯一 ID，如 ins-abcd1234
        :type InstanceId: str
        :param Port: 後端服務的監聽端口
        :type Port: int
        :param Weight: 後端服務的轉發權重，取值範圍：[0, 100]，預設爲 10。
        :type Weight: int
        :param PublicIpAddresses: 後端服務的外網 IP
注意：此欄位可能返回 null，表示取不到有效值。
        :type PublicIpAddresses: list of str
        :param PrivateIpAddresses: 後端服務的内網 IP
注意：此欄位可能返回 null，表示取不到有效值。
        :type PrivateIpAddresses: list of str
        :param InstanceName: 後端服務的實例名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param RegisteredTime: 後端服務被綁定的時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type RegisteredTime: str
        :param EniId: 彈性網卡唯一ID，如 eni-1234abcd
注意：此欄位可能返回 null，表示取不到有效值。
        :type EniId: str
        """
        self.Type = None
        self.InstanceId = None
        self.Port = None
        self.Weight = None
        self.PublicIpAddresses = None
        self.PrivateIpAddresses = None
        self.InstanceName = None
        self.RegisteredTime = None
        self.EniId = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.InstanceId = params.get("InstanceId")
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.InstanceName = params.get("InstanceName")
        self.RegisteredTime = params.get("RegisteredTime")
        self.EniId = params.get("EniId")


class BasicTargetGroupInfo(AbstractModel):
    """監聽器或者轉發規則綁定的目标組基本訊息

    """

    def __init__(self):
        """
        :param TargetGroupId: 目标組ID
        :type TargetGroupId: str
        :param TargetGroupName: 目标組名稱
        :type TargetGroupName: str
        """
        self.TargetGroupId = None
        self.TargetGroupName = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        self.TargetGroupName = params.get("TargetGroupName")


class BatchDeregisterTargetsRequest(AbstractModel):
    """BatchDeregisterTargets請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡ID
        :type LoadBalancerId: str
        :param Targets: 解綁目标
        :type Targets: list of BatchTarget
        """
        self.LoadBalancerId = None
        self.Targets = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = BatchTarget()
                obj._deserialize(item)
                self.Targets.append(obj)


class BatchDeregisterTargetsResponse(AbstractModel):
    """BatchDeregisterTargets返回參數結構體

    """

    def __init__(self):
        """
        :param FailListenerIdSet: 解綁失敗的監聽器ID
        :type FailListenerIdSet: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FailListenerIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FailListenerIdSet = params.get("FailListenerIdSet")
        self.RequestId = params.get("RequestId")


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


class BatchRegisterTargetsRequest(AbstractModel):
    """BatchRegisterTargets請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡ID
        :type LoadBalancerId: str
        :param Targets: 綁定目标
        :type Targets: list of BatchTarget
        """
        self.LoadBalancerId = None
        self.Targets = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = BatchTarget()
                obj._deserialize(item)
                self.Targets.append(obj)


class BatchRegisterTargetsResponse(AbstractModel):
    """BatchRegisterTargets返回參數結構體

    """

    def __init__(self):
        """
        :param FailListenerIdSet: 綁定失敗的監聽器ID，如爲空表示全部綁定成功。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FailListenerIdSet: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FailListenerIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FailListenerIdSet = params.get("FailListenerIdSet")
        self.RequestId = params.get("RequestId")


class BatchTarget(AbstractModel):
    """批次綁定類型

    """

    def __init__(self):
        """
        :param ListenerId: 監聽器ID
        :type ListenerId: str
        :param Port: 綁定端口
        :type Port: int
        :param InstanceId: 子機ID
        :type InstanceId: str
        :param EniIp: 彈性網卡ip
        :type EniIp: str
        :param Weight: 子機權重，範圍[0, 100]。綁定時如果不存在，則預設爲10。
        :type Weight: int
        :param LocationId: 七層規則ID
        :type LocationId: str
        """
        self.ListenerId = None
        self.Port = None
        self.InstanceId = None
        self.EniIp = None
        self.Weight = None
        self.LocationId = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")
        self.EniIp = params.get("EniIp")
        self.Weight = params.get("Weight")
        self.LocationId = params.get("LocationId")


class BlockedIP(AbstractModel):
    """加入了12306黑名單的IP

    """

    def __init__(self):
        """
        :param IP: 黑名單IP
        :type IP: str
        :param CreateTime: 加入黑名單的時間
        :type CreateTime: str
        :param ExpireTime: 過期時間
        :type ExpireTime: str
        """
        self.IP = None
        self.CreateTime = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")


class CertIdRelatedWithLoadBalancers(AbstractModel):
    """證書ID，以及與該證書ID關聯的負載均衡實例清單

    """

    def __init__(self):
        """
        :param CertId: 證書ID
        :type CertId: str
        :param LoadBalancers: 與證書關聯的負載均衡實例清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type LoadBalancers: list of LoadBalancer
        """
        self.CertId = None
        self.LoadBalancers = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        if params.get("LoadBalancers") is not None:
            self.LoadBalancers = []
            for item in params.get("LoadBalancers"):
                obj = LoadBalancer()
                obj._deserialize(item)
                self.LoadBalancers.append(obj)


class CertificateInput(AbstractModel):
    """證書訊息

    """

    def __init__(self):
        """
        :param SSLMode: 認證類型，UNIDIRECTIONAL：單向認證，MUTUAL：雙向認證
        :type SSLMode: str
        :param CertId: 服務端證書的 ID，如果不填寫此項則必須上傳證書，包括 CertContent，CertKey，CertName。
        :type CertId: str
        :param CertCaId: 用戶端證書的 ID，當監聽器采用雙向認證，即 SSLMode=MUTUAL 時，如果不填寫此項則必須上傳用戶端證書，包括 CertCaContent，CertCaName。
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
        :param SSLMode: 認證類型，UNIDIRECTIONAL：單向認證，MUTUAL：雙向認證
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
    """傳統型負載均衡後端服務的健康狀态

    """

    def __init__(self):
        """
        :param IP: 後端服務的内網 IP
        :type IP: str
        :param Port: 後端服務的端口
        :type Port: int
        :param ListenerPort: 負載均衡的監聽端口
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
        :param HealthSwitch: 是否開啓了健康檢查：1（開啓）、0（關閉）
        :type HealthSwitch: int
        :param TimeOut: 響應超時時間
        :type TimeOut: int
        :param IntervalTime: 檢查間隔
        :type IntervalTime: int
        :param HealthNum: 健康阈值
        :type HealthNum: int
        :param UnhealthNum: 不健康阈值
        :type UnhealthNum: int
        :param HttpHash: 傳統型公網負載均衡的 HTTP、HTTPS 監聽器的請求均衡方法。wrr 表示按權重輪詢，ip_hash 表示根據訪問的源 IP 進行一緻性哈希方式來分發
        :type HttpHash: str
        :param HttpCode: 傳統型公網負載均衡的 HTTP、HTTPS 監聽器的健康檢查返回碼。具體可參考創建監聽器中對該欄位的解釋
        :type HttpCode: int
        :param HttpCheckPath: 傳統型公網負載均衡的 HTTP、HTTPS 監聽器的健康檢查路徑
        :type HttpCheckPath: str
        :param SSLMode: 傳統型公網負載均衡的 HTTPS 監聽器的認證方式
        :type SSLMode: str
        :param CertId: 傳統型公網負載均衡的 HTTPS 監聽器的服務端證書 ID
        :type CertId: str
        :param CertCaId: 傳統型公網負載均衡的 HTTPS 監聽器的用戶端證書 ID
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
    """傳統型負載均衡的後端服務相關訊息

    """

    def __init__(self):
        """
        :param Type: 後端服務的類型，可取值：CVM、ENI（即将支援）
        :type Type: str
        :param InstanceId: 後端服務的唯一 ID，可通過 DescribeInstances 介面返回欄位中的 unInstanceId 欄位獲取
        :type InstanceId: str
        :param Weight: 後端服務的轉發權重，取值範圍：[0, 100]，預設爲 10。
        :type Weight: int
        :param PublicIpAddresses: 後端服務的外網 IP
注意：此欄位可能返回 null，表示取不到有效值。
        :type PublicIpAddresses: list of str
        :param PrivateIpAddresses: 後端服務的内網 IP
注意：此欄位可能返回 null，表示取不到有效值。
        :type PrivateIpAddresses: list of str
        :param InstanceName: 後端服務的實例名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param RunFlag: 後端服務的狀态
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
    """傳統型負載均衡的後端訊息

    """

    def __init__(self):
        """
        :param InstanceId: 後端實例ID
        :type InstanceId: str
        :param Weight: 權重，取值範圍 [0, 100]
        :type Weight: int
        """
        self.InstanceId = None
        self.Weight = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")


class ClusterItem(AbstractModel):
    """獨占集群訊息

    """

    def __init__(self):
        """
        :param ClusterId: 集群唯一ID
        :type ClusterId: str
        :param ClusterName: 集群名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param Zone: 集群所在可用區，如ap-guangzhou-1
注意：此欄位可能返回 null，表示取不到有效值。
        :type Zone: str
        """
        self.ClusterId = None
        self.ClusterName = None
        self.Zone = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.Zone = params.get("Zone")


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
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param Certificate: 證書相關訊息，此參數僅适用于TCP_SSL監聽器和未開啓SNI特性的HTTPS監聽器。
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
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
        :param Forward: 負載均衡實例的類型。1：通用的負載均衡實例，目前只支援傳入1
        :type Forward: int
        :param LoadBalancerName: 負載均衡實例的名稱，只在創建一個實例的時候才會生效。規則：1-50 個英文、漢字、數字、連接線“-”或下劃線“_”。
注意：如果名稱與系統中已有負載均衡實例的名稱相同，則系統将會自動生成此次創建的負載均衡實例的名稱。
        :type LoadBalancerName: str
        :param VpcId: 負載均衡後端目标設備所屬的網絡 ID，如vpc-12345678，可以通過 DescribeVpcEx 介面獲取。 不傳此參數則預設爲基礎網絡（"0"）。
        :type VpcId: str
        :param SubnetId: 在私有網絡内購買内網負載均衡實例的情況下，必須指定子網 ID，内網負載均衡實例的 VIP 将從這個子網中産生。
        :type SubnetId: str
        :param ProjectId: 負載均衡實例所屬的項目 ID，可以通過 DescribeProject 介面獲取。不傳此參數則視爲預設項目。
        :type ProjectId: int
        :param AddressIPVersion: 僅适用于公網負載均衡。IP版本，可取值：IPV4、IPV6、IPv6FullChain，預設值 IPV4。
        :type AddressIPVersion: str
        :param Number: 創建負載均衡的個數，預設值 1。
        :type Number: int
        :param MasterZoneId: 僅适用于公網負載均衡。設置跨可用區容災時的主可用區ID，例如 100001 或 ap-guangzhou-1
注：主可用區是需要承載流量的可用區，備可用區預設不承載流量，主可用區不可用時才使用備可用區，平台将爲您自動選擇最佳備可用區。可通過 DescribeMasterZones 介面查詢一個地域的主可用區的清單。
        :type MasterZoneId: str
        :param ZoneId: 僅适用于公網負載均衡。可用區ID，指定可用區以創建負載均衡實例。如：ap-guangzhou-1
        :type ZoneId: str
        :param InternetAccessible: 僅适用于公網負載均衡。負載均衡的網絡計費模式。
        :type InternetAccessible: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`
        :param VipIsp: 僅适用于公網負載均衡。CMCC | CTCC | CUCC，分别對應 移動 | 電信 | 聯通，如果不指定本參數，則預設使用BGP。可通過 DescribeSingleIsp 介面查詢一個地域所支援的Isp。如果指定運營商，則網絡計費式只能使用按頻寬包計費(BANDWIDTH_PACKAGE)。
        :type VipIsp: str
        :param Tags: 購買負載均衡同時，給負載均衡打上标簽
        :type Tags: list of TagInfo
        """
        self.LoadBalancerType = None
        self.Forward = None
        self.LoadBalancerName = None
        self.VpcId = None
        self.SubnetId = None
        self.ProjectId = None
        self.AddressIPVersion = None
        self.Number = None
        self.MasterZoneId = None
        self.ZoneId = None
        self.InternetAccessible = None
        self.VipIsp = None
        self.Tags = None


    def _deserialize(self, params):
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.Forward = params.get("Forward")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ProjectId = params.get("ProjectId")
        self.AddressIPVersion = params.get("AddressIPVersion")
        self.Number = params.get("Number")
        self.MasterZoneId = params.get("MasterZoneId")
        self.ZoneId = params.get("ZoneId")
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.VipIsp = params.get("VipIsp")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateLoadBalancerResponse(AbstractModel):
    """CreateLoadBalancer返回參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerIds: 由負載均衡實例唯一 ID 組成的數組。
        :type LoadBalancerIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.LoadBalancerIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.RequestId = params.get("RequestId")


class CreateLoadBalancerSnatIpsRequest(AbstractModel):
    """CreateLoadBalancerSnatIps請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡唯一性Id，如lb-12345678
        :type LoadBalancerId: str
        :param SnatIps: 添加SnatIp訊息，可指定Ip申請，或者指定子網自動申請
        :type SnatIps: list of SnatIp
        """
        self.LoadBalancerId = None
        self.SnatIps = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("SnatIps") is not None:
            self.SnatIps = []
            for item in params.get("SnatIps"):
                obj = SnatIp()
                obj._deserialize(item)
                self.SnatIps.append(obj)


class CreateLoadBalancerSnatIpsResponse(AbstractModel):
    """CreateLoadBalancerSnatIps返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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
        :param LocationIds: 創建的轉發規則的唯一标識數組
        :type LocationIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.LocationIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LocationIds = params.get("LocationIds")
        self.RequestId = params.get("RequestId")


class CreateTargetGroupRequest(AbstractModel):
    """CreateTargetGroup請求參數結構體

    """

    def __init__(self):
        """
        :param TargetGroupName: 目标組名稱，限定50個字元
        :type TargetGroupName: str
        :param VpcId: 目标組的vpcid屬性，不填則使用預設vpc
        :type VpcId: str
        :param Port: 目标組的預設端口， 後續添加服務器時可使用該預設端口
        :type Port: int
        :param TargetGroupInstances: 目标組綁定的後端服務器
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self.TargetGroupName = None
        self.VpcId = None
        self.Port = None
        self.TargetGroupInstances = None


    def _deserialize(self, params):
        self.TargetGroupName = params.get("TargetGroupName")
        self.VpcId = params.get("VpcId")
        self.Port = params.get("Port")
        if params.get("TargetGroupInstances") is not None:
            self.TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self.TargetGroupInstances.append(obj)


class CreateTargetGroupResponse(AbstractModel):
    """CreateTargetGroup返回參數結構體

    """

    def __init__(self):
        """
        :param TargetGroupId: 創建目标組後生成的id
        :type TargetGroupId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TargetGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        self.RequestId = params.get("RequestId")


class DeleteListenerRequest(AbstractModel):
    """DeleteListener請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例 ID
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


class DeleteLoadBalancerListenersRequest(AbstractModel):
    """DeleteLoadBalancerListeners請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例 ID
        :type LoadBalancerId: str
        :param ListenerIds: 指定删除的監聽器ID數組，若不填則删除負載均衡的所有監聽器
        :type ListenerIds: list of str
        """
        self.LoadBalancerId = None
        self.ListenerIds = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerIds = params.get("ListenerIds")


class DeleteLoadBalancerListenersResponse(AbstractModel):
    """DeleteLoadBalancerListeners返回參數結構體

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
        :param LoadBalancerIds: 要删除的負載均衡實例 ID數組，數組大小最大支援20
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


class DeleteLoadBalancerSnatIpsRequest(AbstractModel):
    """DeleteLoadBalancerSnatIps請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡唯一Id，如lb-12345678
        :type LoadBalancerId: str
        :param Ips: 删除SnatIp網址數組
        :type Ips: list of str
        """
        self.LoadBalancerId = None
        self.Ips = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.Ips = params.get("Ips")


class DeleteLoadBalancerSnatIpsResponse(AbstractModel):
    """DeleteLoadBalancerSnatIps返回參數結構體

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
        :param ListenerId: 負載均衡監聽器 ID
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


class DeleteTargetGroupsRequest(AbstractModel):
    """DeleteTargetGroups請求參數結構體

    """

    def __init__(self):
        """
        :param TargetGroupIds: 目标組的ID數組
        :type TargetGroupIds: list of str
        """
        self.TargetGroupIds = None


    def _deserialize(self, params):
        self.TargetGroupIds = params.get("TargetGroupIds")


class DeleteTargetGroupsResponse(AbstractModel):
    """DeleteTargetGroups返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeregisterTargetGroupInstancesRequest(AbstractModel):
    """DeregisterTargetGroupInstances請求參數結構體

    """

    def __init__(self):
        """
        :param TargetGroupId: 目标組ID
        :type TargetGroupId: str
        :param TargetGroupInstances: 待解綁的服務器訊息
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self.TargetGroupId = None
        self.TargetGroupInstances = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetGroupInstances") is not None:
            self.TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self.TargetGroupInstances.append(obj)


class DeregisterTargetGroupInstancesResponse(AbstractModel):
    """DeregisterTargetGroupInstances返回參數結構體

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
        :param InstanceIds: 後端服務的實例ID清單
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
        :param LoadBalancerId: 負載均衡實例 ID，格式如 lb-12345678
        :type LoadBalancerId: str
        :param ListenerId: 監聽器 ID，格式如 lbl-12345678
        :type ListenerId: str
        :param Targets: 要解綁的後端服務清單，數組長度最大支援20
        :type Targets: list of Target
        :param LocationId: 轉發規則的ID，格式如 loc-12345678，當從七層轉發規則解綁機器時，必須提供此參數或Domain+Url兩者之一
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


class DescribeBlockIPListRequest(AbstractModel):
    """DescribeBlockIPList請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例 ID。
        :type LoadBalancerId: str
        :param Offset: 數據偏移量，預設爲 0。
        :type Offset: int
        :param Limit: 返回IP的最大個數，預設爲 100000。
        :type Limit: int
        """
        self.LoadBalancerId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeBlockIPListResponse(AbstractModel):
    """DescribeBlockIPList返回參數結構體

    """

    def __init__(self):
        """
        :param BlockedIPCount: 返回的IP的數量
        :type BlockedIPCount: int
        :param ClientIPField: 獲取用戶真實IP的欄位
        :type ClientIPField: str
        :param BlockedIPList: 加入了12360黑名單的IP清單
        :type BlockedIPList: list of BlockedIP
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.BlockedIPCount = None
        self.ClientIPField = None
        self.BlockedIPList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BlockedIPCount = params.get("BlockedIPCount")
        self.ClientIPField = params.get("ClientIPField")
        if params.get("BlockedIPList") is not None:
            self.BlockedIPList = []
            for item in params.get("BlockedIPList"):
                obj = BlockedIP()
                obj._deserialize(item)
                self.BlockedIPList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBlockIPTaskRequest(AbstractModel):
    """DescribeBlockIPTask請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: ModifyBlockIPList 介面返回的異步任務的ID。
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class DescribeBlockIPTaskResponse(AbstractModel):
    """DescribeBlockIPTask返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 1 running，2 fail，6 succ
        :type Status: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
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
        :param ListenerIds: 負載均衡監聽器ID清單
        :type ListenerIds: list of str
        :param Protocol: 負載均衡監聽的協議, 'TCP', 'UDP', 'HTTP', 'HTTPS'
        :type Protocol: str
        :param ListenerPort: 負載均衡監聽端口， 範圍[1-65535]
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
        :param ListenerIds: 要查詢的負載均衡監聽器 ID數組
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
        :param TotalCount: 總的監聽器個數
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Listeners = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Listeners") is not None:
            self.Listeners = []
            for item in params.get("Listeners"):
                obj = Listener()
                obj._deserialize(item)
                self.Listeners.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancerListByCertIdRequest(AbstractModel):
    """DescribeLoadBalancerListByCertId請求參數結構體

    """

    def __init__(self):
        """
        :param CertIds: 服務端證書的ID，或用戶端證書的ID
        :type CertIds: list of str
        """
        self.CertIds = None


    def _deserialize(self, params):
        self.CertIds = params.get("CertIds")


class DescribeLoadBalancerListByCertIdResponse(AbstractModel):
    """DescribeLoadBalancerListByCertId返回參數結構體

    """

    def __init__(self):
        """
        :param CertSet: 證書ID，以及與該證書ID關聯的負載均衡實例清單
        :type CertSet: list of CertIdRelatedWithLoadBalancers
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CertSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CertSet") is not None:
            self.CertSet = []
            for item in params.get("CertSet"):
                obj = CertIdRelatedWithLoadBalancers()
                obj._deserialize(item)
                self.CertSet.append(obj)
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
        :param Forward: 負載均衡實例的類型。1：通用的負載均衡實例，0：傳統型負載均衡實例。如果不傳此參數，則查詢所有類型的負載均衡實例。
        :type Forward: int
        :param LoadBalancerName: 負載均衡實例的名稱。
        :type LoadBalancerName: str
        :param Domain: Top Cloud 爲負載均衡實例分配的域名，本參數僅對傳統型公網負載均衡才有意義。
        :type Domain: str
        :param LoadBalancerVips: 負載均衡實例的 VIP 網址，支援多個。
        :type LoadBalancerVips: list of str
        :param BackendPublicIps: 負載均衡綁定的後端服務的外網 IP。
        :type BackendPublicIps: list of str
        :param BackendPrivateIps: 負載均衡綁定的後端服務的内網 IP。
        :type BackendPrivateIps: list of str
        :param Offset: 數據偏移量，預設爲 0。
        :type Offset: int
        :param Limit: 返回負載均衡實例的數量，預設爲20，最大值爲100。
        :type Limit: int
        :param OrderBy: 排序參數，支援以下欄位：LoadBalancerName，CreateTime，Domain，LoadBalancerType。
        :type OrderBy: str
        :param OrderType: 1：倒序，0：順序，預設按照創建時間倒序。
        :type OrderType: int
        :param SearchKey: 搜索欄位，模糊比對名稱、域名、VIP。
        :type SearchKey: str
        :param ProjectId: 負載均衡實例所屬的項目 ID，可以通過 DescribeProject 介面獲取。
        :type ProjectId: int
        :param WithRs: 負載均衡是否綁定後端服務，0：沒有綁定後端服務，1：綁定後端服務，-1：查詢全部。
        :type WithRs: int
        :param VpcId: 負載均衡實例所屬私有網絡唯一ID，如 vpc-bhqkbhdx，
基礎網絡可傳入'0'。
        :type VpcId: str
        :param SecurityGroup: 安全組ID，如 sg-m1cc9123
        :type SecurityGroup: str
        :param MasterZone: 主可用區ID，如 ："100001" （對應的是廣州一區）
        :type MasterZone: str
        :param Filters: 每次請求的`Filters`的上限爲10，`Filter.Values`的上限爲100。詳細的過濾條件如下：
<li> internet-charge-type - String - 是否必填：否 - （過濾條件）按照 CLB 的網絡計費模式過濾，包括"BANDWIDTH_PREPAID","TRAFFIC_POSTPAID_BY_HOUR","BANDWIDTH_POSTPAID_BY_HOUR","BANDWIDTH_PACKAGE"。</li>
<li> master-zone-id - String - 是否必填：否 - （過濾條件）按照 CLB 的主可用區ID過濾，如 ："100001" （對應的是廣州一區）。</li>
<li> tag-key - String - 是否必填：否 - （過濾條件）按照 CLB 标簽的鍵過濾。</li>
        :type Filters: list of Filter
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
        self.MasterZone = None
        self.Filters = None


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
        self.MasterZone = params.get("MasterZone")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeLoadBalancersResponse(AbstractModel):
    """DescribeLoadBalancers返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 滿足過濾條件的負載均衡實例總數。此數值與入參中的Limit無關。
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


class DescribeTargetGroupInstancesRequest(AbstractModel):
    """DescribeTargetGroupInstances請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 過濾條件，當前僅支援TargetGroupId，BindIP，InstanceId過濾
        :type Filters: list of Filter
        :param Limit: 顯示數量限制，預設20
        :type Limit: int
        :param Offset: 顯示的偏移量，預設爲0
        :type Offset: int
        """
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeTargetGroupInstancesResponse(AbstractModel):
    """DescribeTargetGroupInstances返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 本次查詢的結果數量
        :type TotalCount: int
        :param TargetGroupInstanceSet: 綁定的服務器訊息
        :type TargetGroupInstanceSet: list of TargetGroupBackend
        :param RealCount: 實際統計數量，不受Limit，Offset，CAM的影響
        :type RealCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TargetGroupInstanceSet = None
        self.RealCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TargetGroupInstanceSet") is not None:
            self.TargetGroupInstanceSet = []
            for item in params.get("TargetGroupInstanceSet"):
                obj = TargetGroupBackend()
                obj._deserialize(item)
                self.TargetGroupInstanceSet.append(obj)
        self.RealCount = params.get("RealCount")
        self.RequestId = params.get("RequestId")


class DescribeTargetGroupListRequest(AbstractModel):
    """DescribeTargetGroupList請求參數結構體

    """

    def __init__(self):
        """
        :param TargetGroupIds: 目标組ID數組
        :type TargetGroupIds: list of str
        :param Filters: 過濾條件數組，支援TargetGroupVpcId和TargetGroupName。與TargetGroupIds互斥，優先使用目标組ID，
        :type Filters: list of Filter
        :param Offset: 顯示的偏移起始量
        :type Offset: int
        :param Limit: 顯示條數限制，預設爲20
        :type Limit: int
        """
        self.TargetGroupIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.TargetGroupIds = params.get("TargetGroupIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTargetGroupListResponse(AbstractModel):
    """DescribeTargetGroupList返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 顯示的結果數量
        :type TotalCount: int
        :param TargetGroupSet: 顯示的目标組訊息集合
        :type TargetGroupSet: list of TargetGroupInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TargetGroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TargetGroupSet") is not None:
            self.TargetGroupSet = []
            for item in params.get("TargetGroupSet"):
                obj = TargetGroupInfo()
                obj._deserialize(item)
                self.TargetGroupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTargetGroupsRequest(AbstractModel):
    """DescribeTargetGroups請求參數結構體

    """

    def __init__(self):
        """
        :param TargetGroupIds: 目标組ID，與Filters互斥
        :type TargetGroupIds: list of str
        :param Limit: 顯示條數限制，預設爲20
        :type Limit: int
        :param Offset: 顯示的偏移起始量
        :type Offset: int
        :param Filters: 過濾條件數組，與TargetGroupIds互斥，支援TargetGroupVpcId和TargetGroupName
        :type Filters: list of Filter
        """
        self.TargetGroupIds = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.TargetGroupIds = params.get("TargetGroupIds")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeTargetGroupsResponse(AbstractModel):
    """DescribeTargetGroups返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 顯示的結果數量
        :type TotalCount: int
        :param TargetGroupSet: 顯示的目标組訊息集合
        :type TargetGroupSet: list of TargetGroupInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TargetGroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TargetGroupSet") is not None:
            self.TargetGroupSet = []
            for item in params.get("TargetGroupSet"):
                obj = TargetGroupInfo()
                obj._deserialize(item)
                self.TargetGroupSet.append(obj)
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
        :param Port: 監聽器端口
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
注意：此欄位可能返回 null，表示取不到有效值。
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
        :param TaskId: 請求ID，即介面返回的 RequestId 參數
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


class DisassociateTargetGroupsRequest(AbstractModel):
    """DisassociateTargetGroups請求參數結構體

    """

    def __init__(self):
        """
        :param Associations: 待解綁的規則關系數組
        :type Associations: list of TargetGroupAssociation
        """
        self.Associations = None


    def _deserialize(self, params):
        if params.get("Associations") is not None:
            self.Associations = []
            for item in params.get("Associations"):
                obj = TargetGroupAssociation()
                obj._deserialize(item)
                self.Associations.append(obj)


class DisassociateTargetGroupsResponse(AbstractModel):
    """DisassociateTargetGroups返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ExclusiveCluster(AbstractModel):
    """獨占集群

    """

    def __init__(self):
        """
        :param L4Clusters: 4層獨占集群清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type L4Clusters: list of ClusterItem
        :param L7Clusters: 7層獨占集群清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type L7Clusters: list of ClusterItem
        :param ClassicalCluster: vpcgw集群
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClassicalCluster: :class:`tencentcloud.clb.v20180317.models.ClusterItem`
        """
        self.L4Clusters = None
        self.L7Clusters = None
        self.ClassicalCluster = None


    def _deserialize(self, params):
        if params.get("L4Clusters") is not None:
            self.L4Clusters = []
            for item in params.get("L4Clusters"):
                obj = ClusterItem()
                obj._deserialize(item)
                self.L4Clusters.append(obj)
        if params.get("L7Clusters") is not None:
            self.L7Clusters = []
            for item in params.get("L7Clusters"):
                obj = ClusterItem()
                obj._deserialize(item)
                self.L7Clusters.append(obj)
        if params.get("ClassicalCluster") is not None:
            self.ClassicalCluster = ClusterItem()
            self.ClassicalCluster._deserialize(params.get("ClassicalCluster"))


class ExtraInfo(AbstractModel):
    """暫做保留，一般用戶無需關注。

    """

    def __init__(self):
        """
        :param ZhiTong: 是否開通VIP直通
注意：此欄位可能返回 null，表示取不到有效值。
        :type ZhiTong: bool
        :param TgwGroupName: TgwGroup名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type TgwGroupName: str
        """
        self.ZhiTong = None
        self.TgwGroupName = None


    def _deserialize(self, params):
        self.ZhiTong = params.get("ZhiTong")
        self.TgwGroupName = params.get("TgwGroupName")


class Filter(AbstractModel):
    """過濾器條件

    """

    def __init__(self):
        """
        :param Name: 過濾器的名稱
        :type Name: str
        :param Values: 過濾器的值數組
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class HealthCheck(AbstractModel):
    """健康檢查訊息。
    注意，自定義探測相關參數 目前只有少量區域灰度支援。

    """

    def __init__(self):
        """
        :param HealthSwitch: 是否開啓健康檢查：1（開啓）、0（關閉）。
        :type HealthSwitch: int
        :param TimeOut: 健康檢查的響應超時時間（僅适用于四層監聽器），可選值：2~60，預設值：2，單位：秒。響應超時時間要小於檢查間隔時間。
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
        :param HttpCode: 健康檢查狀态碼（僅适用于HTTP/HTTPS轉發規則、TCP監聽器的HTTP健康檢查方式）。可選值：1~31，預設 31。
1 表示探測後返回值 1xx 代表健康，2 表示返回 2xx 代表健康，4 表示返回 3xx 代表健康，8 表示返回 4xx 代表健康，16 表示返回 5xx 代表健康。若希望多種返回碼都可代表健康，則将相應的值相加。注意：TCP監聽器的HTTP健康檢查方式，只支援指定一種健康檢查狀态碼。
注意：此欄位可能返回 null，表示取不到有效值。
        :type HttpCode: int
        :param HttpCheckPath: 健康檢查路徑（僅适用于HTTP/HTTPS轉發規則、TCP監聽器的HTTP健康檢查方式）。
注意：此欄位可能返回 null，表示取不到有效值。
        :type HttpCheckPath: str
        :param HttpCheckDomain: 健康檢查域名（僅适用于HTTP/HTTPS轉發規則、TCP監聽器的HTTP健康檢查方式）。
注意：此欄位可能返回 null，表示取不到有效值。
        :type HttpCheckDomain: str
        :param HttpCheckMethod: 健康檢查方法（僅适用于HTTP/HTTPS轉發規則、TCP監聽器的HTTP健康檢查方式），預設值：HEAD，可選值HEAD或GET。
注意：此欄位可能返回 null，表示取不到有效值。
        :type HttpCheckMethod: str
        :param CheckPort: 自定義探測相關參數。健康檢查端口，預設爲後端服務的端口，除非您希望指定特定端口，否則建議留空。（僅适用于TCP/UDP監聽器）。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CheckPort: int
        :param ContextType: 自定義探測相關參數。健康檢查協議CheckType的值取CUSTOM時，必填此欄位，代表健康檢查的輸入格式，可取值：HEX或TEXT；取值爲HEX時，SendContext和RecvContext的字元只能在0123456789ABCDEF中選取且長度必須是偶數位。（僅适用于TCP/UDP監聽器）
注意：此欄位可能返回 null，表示取不到有效值。
        :type ContextType: str
        :param SendContext: 自定義探測相關參數。健康檢查協議CheckType的值取CUSTOM時，必填此欄位，代表健康檢查發送的請求内容，只允許ASCII可見字元，最大長度限制500。（僅适用于TCP/UDP監聽器）。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SendContext: str
        :param RecvContext: 自定義探測相關參數。健康檢查協議CheckType的值取CUSTOM時，必填此欄位，代表健康檢查返回的結果，只允許ASCII可見字元，最大長度限制500。（僅适用于TCP/UDP監聽器）。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RecvContext: str
        :param CheckType: 自定義探測相關參數。健康檢查使用的協議：TCP | HTTP | CUSTOM（僅适用于TCP/UDP監聽器，其中UDP監聽器只支援CUSTOM；如果使用自定義健康檢查功能，則必傳）。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CheckType: str
        :param HttpVersion: 自定義探測相關參數。健康檢查協議CheckType的值取HTTP時，必傳此欄位，代表後端服務的HTTP版本：HTTP/1.0、HTTP/1.1；（僅适用于TCP監聽器）
注意：此欄位可能返回 null，表示取不到有效值。
        :type HttpVersion: str
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
        self.CheckPort = None
        self.ContextType = None
        self.SendContext = None
        self.RecvContext = None
        self.CheckType = None
        self.HttpVersion = None


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
        self.CheckPort = params.get("CheckPort")
        self.ContextType = params.get("ContextType")
        self.SendContext = params.get("SendContext")
        self.RecvContext = params.get("RecvContext")
        self.CheckType = params.get("CheckType")
        self.HttpVersion = params.get("HttpVersion")


class InternetAccessible(AbstractModel):
    """網絡計費模式，最大出頻寬

    """

    def __init__(self):
        """
        :param InternetChargeType: TRAFFIC_POSTPAID_BY_HOUR 按流量按小時後計費 ; BANDWIDTH_POSTPAID_BY_HOUR 按頻寬按小時後計費;
BANDWIDTH_PACKAGE 按頻寬包計費（當前，只有指定運營商時才支援此種計費模式）
注意：此欄位可能返回 null，表示取不到有效值。
        :type InternetChargeType: str
        :param InternetMaxBandwidthOut: 最大出頻寬，單位Mbps，範圍支援0到2048，僅對公網屬性的LB生效，預設值 10
注意：此欄位可能返回 null，表示取不到有效值。
        :type InternetMaxBandwidthOut: int
        :param BandwidthpkgSubType: 頻寬包的類型，如SINGLEISP
注意：此欄位可能返回 null，表示取不到有效值。
        :type BandwidthpkgSubType: str
        """
        self.InternetChargeType = None
        self.InternetMaxBandwidthOut = None
        self.BandwidthpkgSubType = None


    def _deserialize(self, params):
        self.InternetChargeType = params.get("InternetChargeType")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.BandwidthpkgSubType = params.get("BandwidthpkgSubType")


class LBChargePrepaid(AbstractModel):
    """lb實例包年包月相關配置屬性

    """

    def __init__(self):
        """
        :param RenewFlag: 續約類型：AUTO_RENEW 自動續約，  MANUAL_RENEW 手動續約
注意：此欄位可能返回 null，表示取不到有效值。
        :type RenewFlag: str
        :param Period: 購買時長，單位：月
注意：此欄位可能返回 null，表示取不到有效值。
        :type Period: int
        """
        self.RenewFlag = None
        self.Period = None


    def _deserialize(self, params):
        self.RenewFlag = params.get("RenewFlag")
        self.Period = params.get("Period")


class Listener(AbstractModel):
    """監聽器的訊息

    """

    def __init__(self):
        """
        :param ListenerId: 負載均衡監聽器 ID
        :type ListenerId: str
        :param Protocol: 監聽器協議
        :type Protocol: str
        :param Port: 監聽器端口
        :type Port: int
        :param Certificate: 監聽器綁定的證書訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateOutput`
        :param HealthCheck: 監聽器的健康檢查訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
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
        :param CreateTime: 監聽器的創建時間。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param EndPort: 端口段結束端口
注意：此欄位可能返回 null，表示取不到有效值。
        :type EndPort: int
        :param TargetType: 後端服務器類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type TargetType: str
        :param TargetGroup: 綁定的目标組基本訊息；當監聽器綁定目标組時，會返回該欄位
注意：此欄位可能返回 null，表示取不到有效值。
        :type TargetGroup: :class:`tencentcloud.clb.v20180317.models.BasicTargetGroupInfo`
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
        self.CreateTime = None
        self.EndPort = None
        self.TargetType = None
        self.TargetGroup = None


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
        self.CreateTime = params.get("CreateTime")
        self.EndPort = params.get("EndPort")
        self.TargetType = params.get("TargetType")
        if params.get("TargetGroup") is not None:
            self.TargetGroup = BasicTargetGroupInfo()
            self.TargetGroup._deserialize(params.get("TargetGroup"))


class ListenerBackend(AbstractModel):
    """監聽器上綁定的後端服務的訊息

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
        :param Targets: 監聽器上綁定的後端服務清單（僅适用于TCP/UDP/TCP_SSL監聽器）
注意：此欄位可能返回 null，表示取不到有效值。
        :type Targets: list of Backend
        :param EndPort: 若支援端口段，則爲端口段結束端口；若不支援端口段，則爲0
注意：此欄位可能返回 null，表示取不到有效值。
        :type EndPort: int
        """
        self.ListenerId = None
        self.Protocol = None
        self.Port = None
        self.Rules = None
        self.Targets = None
        self.EndPort = None


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
        self.EndPort = params.get("EndPort")


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
        :param Forward: 負載均衡類型标識，1：負載均衡，0：傳統型負載均衡。
        :type Forward: int
        :param Domain: 負載均衡實例的域名，僅公網傳統型負載均衡實例才提供該欄位
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
        :type TargetRegionInfo: :class:`tencentcloud.clb.v20180317.models.TargetRegionInfo`
        :param AnycastZone: anycast負載均衡的發布域，對于非anycast的負載均衡，此欄位返回爲空字串
注意：此欄位可能返回 null，表示取不到有效值。
        :type AnycastZone: str
        :param AddressIPVersion: IP版本，ipv4 | ipv6
注意：此欄位可能返回 null，表示取不到有效值。
        :type AddressIPVersion: str
        :param NumericalVpcId: 數值形式的私有網絡 ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type NumericalVpcId: int
        :param VipIsp: 負載均衡IP網址所屬的ISP
注意：此欄位可能返回 null，表示取不到有效值。
        :type VipIsp: str
        :param MasterZone: 主可用區
注意：此欄位可能返回 null，表示取不到有效值。
        :type MasterZone: :class:`tencentcloud.clb.v20180317.models.ZoneInfo`
        :param BackupZoneSet: 備可用區
注意：此欄位可能返回 null，表示取不到有效值。
        :type BackupZoneSet: list of ZoneInfo
        :param IsolatedTime: 負載均衡實例被隔離的時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsolatedTime: str
        :param ExpireTime: 負載均衡實例的過期時間，僅對預付費負載均衡生效
注意：此欄位可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param ChargeType: 負載均衡實例的計費類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type ChargeType: str
        :param NetworkAttributes: 負載均衡實例的網絡屬性
注意：此欄位可能返回 null，表示取不到有效值。
        :type NetworkAttributes: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`
        :param PrepaidAttributes: 負載均衡實例的預付費相關屬性
注意：此欄位可能返回 null，表示取不到有效值。
        :type PrepaidAttributes: :class:`tencentcloud.clb.v20180317.models.LBChargePrepaid`
        :param LogSetId: 負載均衡日志服務(CLS)的日志集ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type LogSetId: str
        :param LogTopicId: 負載均衡日志服務(CLS)的日志主題ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type LogTopicId: str
        :param AddressIPv6: 負載均衡實例的IPv6網址
注意：此欄位可能返回 null，表示取不到有效值。
        :type AddressIPv6: str
        :param ExtraInfo: 暫做保留，一般用戶無需關注。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ExtraInfo: :class:`tencentcloud.clb.v20180317.models.ExtraInfo`
        :param IsDDos: 是否可綁定高防包
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsDDos: bool
        :param ConfigId: 負載均衡維度的個性化配置ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConfigId: str
        :param LoadBalancerPassToTarget: 後端服務是否放通來自LB的流量
注意：此欄位可能返回 null，表示取不到有效值。
        :type LoadBalancerPassToTarget: bool
        :param ExclusiveCluster: 内網獨占集群
注意：此欄位可能返回 null，表示取不到有效值。
        :type ExclusiveCluster: :class:`tencentcloud.clb.v20180317.models.ExclusiveCluster`
        :param IPv6Mode: IP網址版本爲ipv6時此欄位有意義， IPv6Nat64 | IPv6FullChain
注意：此欄位可能返回 null，表示取不到有效值。
        :type IPv6Mode: str
        :param SnatPro: 是否開啓SnatPro
注意：此欄位可能返回 null，表示取不到有效值。
        :type SnatPro: bool
        :param SnatIps: 開啓SnatPro負載均衡後，SnatIp清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type SnatIps: list of SnatIp
        :param SlaType: 效能保障規格
注意：此欄位可能返回 null，表示取不到有效值。
        :type SlaType: str
        :param IsBlock: vip是否被封堵
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsBlock: bool
        :param IsBlockTime: 封堵或解封時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsBlockTime: str
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
        self.VipIsp = None
        self.MasterZone = None
        self.BackupZoneSet = None
        self.IsolatedTime = None
        self.ExpireTime = None
        self.ChargeType = None
        self.NetworkAttributes = None
        self.PrepaidAttributes = None
        self.LogSetId = None
        self.LogTopicId = None
        self.AddressIPv6 = None
        self.ExtraInfo = None
        self.IsDDos = None
        self.ConfigId = None
        self.LoadBalancerPassToTarget = None
        self.ExclusiveCluster = None
        self.IPv6Mode = None
        self.SnatPro = None
        self.SnatIps = None
        self.SlaType = None
        self.IsBlock = None
        self.IsBlockTime = None


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
        self.VipIsp = params.get("VipIsp")
        if params.get("MasterZone") is not None:
            self.MasterZone = ZoneInfo()
            self.MasterZone._deserialize(params.get("MasterZone"))
        if params.get("BackupZoneSet") is not None:
            self.BackupZoneSet = []
            for item in params.get("BackupZoneSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self.BackupZoneSet.append(obj)
        self.IsolatedTime = params.get("IsolatedTime")
        self.ExpireTime = params.get("ExpireTime")
        self.ChargeType = params.get("ChargeType")
        if params.get("NetworkAttributes") is not None:
            self.NetworkAttributes = InternetAccessible()
            self.NetworkAttributes._deserialize(params.get("NetworkAttributes"))
        if params.get("PrepaidAttributes") is not None:
            self.PrepaidAttributes = LBChargePrepaid()
            self.PrepaidAttributes._deserialize(params.get("PrepaidAttributes"))
        self.LogSetId = params.get("LogSetId")
        self.LogTopicId = params.get("LogTopicId")
        self.AddressIPv6 = params.get("AddressIPv6")
        if params.get("ExtraInfo") is not None:
            self.ExtraInfo = ExtraInfo()
            self.ExtraInfo._deserialize(params.get("ExtraInfo"))
        self.IsDDos = params.get("IsDDos")
        self.ConfigId = params.get("ConfigId")
        self.LoadBalancerPassToTarget = params.get("LoadBalancerPassToTarget")
        if params.get("ExclusiveCluster") is not None:
            self.ExclusiveCluster = ExclusiveCluster()
            self.ExclusiveCluster._deserialize(params.get("ExclusiveCluster"))
        self.IPv6Mode = params.get("IPv6Mode")
        self.SnatPro = params.get("SnatPro")
        if params.get("SnatIps") is not None:
            self.SnatIps = []
            for item in params.get("SnatIps"):
                obj = SnatIp()
                obj._deserialize(item)
                self.SnatIps.append(obj)
        self.SlaType = params.get("SlaType")
        self.IsBlock = params.get("IsBlock")
        self.IsBlockTime = params.get("IsBlockTime")


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


class ModifyBlockIPListRequest(AbstractModel):
    """ModifyBlockIPList請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerIds: 負載均衡實例ID
        :type LoadBalancerIds: list of str
        :param Type: 操作類型，可取：
<li> add_customized_field（首次設置header，開啓黑名單功能）</li>
<li> set_customized_field（修改header）</li>
<li> del_customized_field（删除header）</li>
<li> add_blocked（添加黑名單）</li>
<li> del_blocked（删除黑名單）</li>
<li> flush_blocked（清空黑名單）</li>
        :type Type: str
        :param ClientIPField: 用戶端真實IP存放的header欄位名
        :type ClientIPField: str
        :param BlockIPList: 封禁IP清單，單次操作數組最大長度支援200000
        :type BlockIPList: list of str
        :param ExpireTime: 過期時間，單位秒，預設值3600
        :type ExpireTime: int
        :param AddStrategy: 添加IP的策略，可取：fifo（如果黑名單容量已滿，新加入黑名單的IP采用先進先出策略）
        :type AddStrategy: str
        """
        self.LoadBalancerIds = None
        self.Type = None
        self.ClientIPField = None
        self.BlockIPList = None
        self.ExpireTime = None
        self.AddStrategy = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.Type = params.get("Type")
        self.ClientIPField = params.get("ClientIPField")
        self.BlockIPList = params.get("BlockIPList")
        self.ExpireTime = params.get("ExpireTime")
        self.AddStrategy = params.get("AddStrategy")


class ModifyBlockIPListResponse(AbstractModel):
    """ModifyBlockIPList返回參數結構體

    """

    def __init__(self):
        """
        :param JodId: 異步任務的ID
        :type JodId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.JodId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JodId = params.get("JodId")
        self.RequestId = params.get("RequestId")


class ModifyDomainAttributesRequest(AbstractModel):
    """ModifyDomainAttributes請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例 ID
        :type LoadBalancerId: str
        :param ListenerId: 負載均衡監聽器 ID
        :type ListenerId: str
        :param Domain: 域名（必須是已經創建的轉發規則下的域名）
        :type Domain: str
        :param NewDomain: 要修改的新域名
        :type NewDomain: str
        :param Certificate: 域名相關的證書訊息，注意，僅對啓用SNI的監聽器适用。
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
        :param Http2: 是否開啓Http2，注意，只有HTTPS域名才能開啓Http2。
        :type Http2: bool
        :param DefaultServer: 是否設爲預設域名，注意，一個監聽器下只能設置一個預設域名。
        :type DefaultServer: bool
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Domain = None
        self.NewDomain = None
        self.Certificate = None
        self.Http2 = None
        self.DefaultServer = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.NewDomain = params.get("NewDomain")
        if params.get("Certificate") is not None:
            self.Certificate = CertificateInput()
            self.Certificate._deserialize(params.get("Certificate"))
        self.Http2 = params.get("Http2")
        self.DefaultServer = params.get("DefaultServer")


class ModifyDomainAttributesResponse(AbstractModel):
    """ModifyDomainAttributes返回參數結構體

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
        :param ListenerId: 負載均衡監聽器 ID
        :type ListenerId: str
        :param Domain: 監聽器下的某個舊域名。
        :type Domain: str
        :param NewDomain: 新域名，	長度限制爲：1-120。有三種使用格式：非正規表示式格式，通配符格式，正規表示式格式。非正規表示式格式只能使用字母、數字、‘-’、‘.’。通配符格式的使用 ‘*’ 只能在開頭或者結尾。正規表示式以'~'開頭。
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
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param Certificate: 證書相關訊息，此參數僅适用于HTTPS/TCP_SSL監聽器
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
        :param Scheduler: 監聽器轉發的方式。可選值：WRR、LEAST_CONN
分别表示按權重輪詢、最小連接數， 預設爲 WRR。
        :type Scheduler: str
        :param SniSwitch: 是否開啓SNI特性，此參數僅适用于HTTPS監聽器。注意：未開啓SNI的監聽器可以開啓SNI；已開啓SNI的監聽器不能關閉SNI
        :type SniSwitch: int
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.ListenerName = None
        self.SessionExpireTime = None
        self.HealthCheck = None
        self.Certificate = None
        self.Scheduler = None
        self.SniSwitch = None


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
        self.SniSwitch = params.get("SniSwitch")


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
        :type TargetRegionInfo: :class:`tencentcloud.clb.v20180317.models.TargetRegionInfo`
        :param InternetChargeInfo: 網絡計費相關參數
        :type InternetChargeInfo: :class:`tencentcloud.clb.v20180317.models.InternetAccessible`
        :param LoadBalancerPassToTarget: Target是否放通來自CLB的流量。開啓放通（true）：只驗證CLB上的安全組；不開啓放通（false）：需同時驗證CLB和後端實例上的安全組。
        :type LoadBalancerPassToTarget: bool
        :param SnatPro: 是否開啓SnatPro
        :type SnatPro: bool
        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.TargetRegionInfo = None
        self.InternetChargeInfo = None
        self.LoadBalancerPassToTarget = None
        self.SnatPro = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        if params.get("TargetRegionInfo") is not None:
            self.TargetRegionInfo = TargetRegionInfo()
            self.TargetRegionInfo._deserialize(params.get("TargetRegionInfo"))
        if params.get("InternetChargeInfo") is not None:
            self.InternetChargeInfo = InternetAccessible()
            self.InternetChargeInfo._deserialize(params.get("InternetChargeInfo"))
        self.LoadBalancerPassToTarget = params.get("LoadBalancerPassToTarget")
        self.SnatPro = params.get("SnatPro")


class ModifyLoadBalancerAttributesResponse(AbstractModel):
    """ModifyLoadBalancerAttributes返回參數結構體

    """

    def __init__(self):
        """
        :param DealName: 切換負載均衡計費方式時，可用此參數查詢切換任務是否成功。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DealName: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DealName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.RequestId = params.get("RequestId")


class ModifyRuleRequest(AbstractModel):
    """ModifyRule請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例 ID
        :type LoadBalancerId: str
        :param ListenerId: 負載均衡監聽器 ID
        :type ListenerId: str
        :param LocationId: 要修改的轉發規則的 ID。
        :type LocationId: str
        :param Url: 轉發規則的新的轉發路徑，如不需修改Url，則不需提供此參數
        :type Url: str
        :param HealthCheck: 健康檢查訊息
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param Scheduler: 規則的請求轉發方式，可選值：WRR、LEAST_CONN、IP_HASH
分别表示按權重輪詢、最小連接數、按IP哈希， 預設爲 WRR。
        :type Scheduler: str
        :param SessionExpireTime: 會話保持時間
        :type SessionExpireTime: int
        :param ForwardType: 負載均衡實例與後端服務之間的轉發協議，預設HTTP，可取值：HTTP、HTTPS、TRPC
        :type ForwardType: str
        :param TrpcCallee: TRPC被調服務器路由，ForwardType爲TRPC時必填
        :type TrpcCallee: str
        :param TrpcFunc: TRPC調用服務介面，ForwardType爲TRPC時必填
        :type TrpcFunc: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.LocationId = None
        self.Url = None
        self.HealthCheck = None
        self.Scheduler = None
        self.SessionExpireTime = None
        self.ForwardType = None
        self.TrpcCallee = None
        self.TrpcFunc = None


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
        self.ForwardType = params.get("ForwardType")
        self.TrpcCallee = params.get("TrpcCallee")
        self.TrpcFunc = params.get("TrpcFunc")


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


class ModifyTargetGroupAttributeRequest(AbstractModel):
    """ModifyTargetGroupAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param TargetGroupId: 目标組的ID
        :type TargetGroupId: str
        :param TargetGroupName: 目标組的新名稱
        :type TargetGroupName: str
        :param Port: 目标組的新預設端口
        :type Port: int
        """
        self.TargetGroupId = None
        self.TargetGroupName = None
        self.Port = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        self.TargetGroupName = params.get("TargetGroupName")
        self.Port = params.get("Port")


class ModifyTargetGroupAttributeResponse(AbstractModel):
    """ModifyTargetGroupAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTargetGroupInstancesPortRequest(AbstractModel):
    """ModifyTargetGroupInstancesPort請求參數結構體

    """

    def __init__(self):
        """
        :param TargetGroupId: 目标組ID
        :type TargetGroupId: str
        :param TargetGroupInstances: 待修改端口的服務器數組
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self.TargetGroupId = None
        self.TargetGroupInstances = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetGroupInstances") is not None:
            self.TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self.TargetGroupInstances.append(obj)


class ModifyTargetGroupInstancesPortResponse(AbstractModel):
    """ModifyTargetGroupInstancesPort返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTargetGroupInstancesWeightRequest(AbstractModel):
    """ModifyTargetGroupInstancesWeight請求參數結構體

    """

    def __init__(self):
        """
        :param TargetGroupId: 目标組ID
        :type TargetGroupId: str
        :param TargetGroupInstances: 待修改權重的服務器數組
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self.TargetGroupId = None
        self.TargetGroupInstances = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetGroupInstances") is not None:
            self.TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self.TargetGroupInstances.append(obj)


class ModifyTargetGroupInstancesWeightResponse(AbstractModel):
    """ModifyTargetGroupInstancesWeight返回參數結構體

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
        :param Targets: 要修改端口的後端服務清單
        :type Targets: list of Target
        :param NewPort: 後端服務綁定到監聽器或轉發規則的新端口
        :type NewPort: int
        :param LocationId: 轉發規則的ID，當後端服務綁定到七層轉發規則時，必須提供此參數或Domain+Url兩者之一
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
        :param LocationId: 轉發規則的ID，當綁定機器到七層轉發規則時，必須提供此參數或Domain+Url兩者之一
        :type LocationId: str
        :param Domain: 目标規則的域名，提供LocationId參數時本參數不生效
        :type Domain: str
        :param Url: 目标規則的URL，提供LocationId參數時本參數不生效
        :type Url: str
        :param Targets: 要修改權重的後端服務清單
        :type Targets: list of Target
        :param Weight: 後端服務新的轉發權重，取值範圍：0~100，預設值10。如果設置了 Targets.Weight 參數，則此參數不生效。
        :type Weight: int
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.LocationId = None
        self.Domain = None
        self.Url = None
        self.Targets = None
        self.Weight = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.Url = params.get("Url")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.Weight = params.get("Weight")


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


class RegisterTargetGroupInstancesRequest(AbstractModel):
    """RegisterTargetGroupInstances請求參數結構體

    """

    def __init__(self):
        """
        :param TargetGroupId: 目标組ID
        :type TargetGroupId: str
        :param TargetGroupInstances: 服務器實例數組
        :type TargetGroupInstances: list of TargetGroupInstance
        """
        self.TargetGroupId = None
        self.TargetGroupInstances = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetGroupInstances") is not None:
            self.TargetGroupInstances = []
            for item in params.get("TargetGroupInstances"):
                obj = TargetGroupInstance()
                obj._deserialize(item)
                self.TargetGroupInstances.append(obj)


class RegisterTargetGroupInstancesResponse(AbstractModel):
    """RegisterTargetGroupInstances返回參數結構體

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
        :param Targets: 待綁定的後端服務清單，數組長度最大支援20
        :type Targets: list of Target
        :param LocationId: 轉發規則的ID，當綁定後端服務到七層轉發規則時，必須提供此參數或Domain+Url兩者之一
        :type LocationId: str
        :param Domain: 目标轉發規則的域名，提供LocationId參數時本參數不生效
        :type Domain: str
        :param Url: 目标轉發規則的URL，提供LocationId參數時本參數不生效
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


class ReplaceCertForLoadBalancersRequest(AbstractModel):
    """ReplaceCertForLoadBalancers請求參數結構體

    """

    def __init__(self):
        """
        :param OldCertificateId: 需要被替換的證書的ID，可以是服務端證書或用戶端證書
        :type OldCertificateId: str
        :param Certificate: 新證書的内容等相關訊息
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
        """
        self.OldCertificateId = None
        self.Certificate = None


    def _deserialize(self, params):
        self.OldCertificateId = params.get("OldCertificateId")
        if params.get("Certificate") is not None:
            self.Certificate = CertificateInput()
            self.Certificate._deserialize(params.get("Certificate"))


class ReplaceCertForLoadBalancersResponse(AbstractModel):
    """ReplaceCertForLoadBalancers返回參數結構體

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
        :param Targets: 要修改權重的後端機器清單
        :type Targets: list of Target
        :param LocationId: 轉發規則的ID，七層規則時需要此參數，4層規則不需要
        :type LocationId: str
        :param Domain: 目标規則的域名，提供LocationId參數時本參數不生效
        :type Domain: str
        :param Url: 目标規則的URL，提供LocationId參數時本參數不生效
        :type Url: str
        :param Weight: 後端服務新的轉發權重，取值範圍：0~100。
        :type Weight: int
        """
        self.ListenerId = None
        self.Targets = None
        self.LocationId = None
        self.Domain = None
        self.Url = None
        self.Weight = None


    def _deserialize(self, params):
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
        :param Domain: 轉發規則的域名。長度限制爲：1~80。
        :type Domain: str
        :param Url: 轉發規則的路徑。長度限制爲：1~200。
        :type Url: str
        :param SessionExpireTime: 會話保持時間。設置爲0表示關閉會話保持，開啓會話保持可取值30~3600，單位：秒。
        :type SessionExpireTime: int
        :param HealthCheck: 健康檢查訊息
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param Certificate: 證書訊息
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateInput`
        :param Scheduler: 規則的請求轉發方式，可選值：WRR、LEAST_CONN、IP_HASH
分别表示按權重輪詢、最小連接數、按IP哈希， 預設爲 WRR。
        :type Scheduler: str
        :param ForwardType: 負載均衡與後端服務之間的轉發協議，目前支援 HTTP/HTTPS/TRPC
        :type ForwardType: str
        :param DefaultServer: 是否将該域名設爲預設域名，注意，一個監聽器下只能設置一個預設域名。
        :type DefaultServer: bool
        :param Http2: 是否開啓Http2，注意，只有HTTPS域名才能開啓Http2。
        :type Http2: bool
        :param TargetType: 後端目标類型，NODE表示綁定普通節點，TARGETGROUP表示綁定目标組
        :type TargetType: str
        :param TrpcCallee: TRPC被調服務器路由，ForwardType爲TRPC時必填
        :type TrpcCallee: str
        :param TrpcFunc: TRPC調用服務介面，ForwardType爲TRPC時必填
        :type TrpcFunc: str
        :param Quic: 是否開啓QUIC，注意，只有HTTPS域名才能開啓QUIC
        :type Quic: bool
        """
        self.Domain = None
        self.Url = None
        self.SessionExpireTime = None
        self.HealthCheck = None
        self.Certificate = None
        self.Scheduler = None
        self.ForwardType = None
        self.DefaultServer = None
        self.Http2 = None
        self.TargetType = None
        self.TrpcCallee = None
        self.TrpcFunc = None
        self.Quic = None


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
        self.ForwardType = params.get("ForwardType")
        self.DefaultServer = params.get("DefaultServer")
        self.Http2 = params.get("Http2")
        self.TargetType = params.get("TargetType")
        self.TrpcCallee = params.get("TrpcCallee")
        self.TrpcFunc = params.get("TrpcFunc")
        self.Quic = params.get("Quic")


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
        :type HealthCheck: :class:`tencentcloud.clb.v20180317.models.HealthCheck`
        :param Certificate: 證書訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Certificate: :class:`tencentcloud.clb.v20180317.models.CertificateOutput`
        :param Scheduler: 規則的請求轉發方式
        :type Scheduler: str
        :param ListenerId: 轉發規則所屬的監聽器 ID
        :type ListenerId: str
        :param RewriteTarget: 轉發規則的重定向目标訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type RewriteTarget: :class:`tencentcloud.clb.v20180317.models.RewriteTarget`
        :param HttpGzip: 是否開啓gzip
        :type HttpGzip: bool
        :param BeAutoCreated: 轉發規則是否爲自動創建
        :type BeAutoCreated: bool
        :param DefaultServer: 是否作爲預設域名
        :type DefaultServer: bool
        :param Http2: 是否開啓Http2
        :type Http2: bool
        :param ForwardType: 負載均衡與後端服務之間的轉發協議
        :type ForwardType: str
        :param CreateTime: 轉發規則的創建時間
        :type CreateTime: str
        :param TargetType: 後端服務器類型
        :type TargetType: str
        :param TargetGroup: 綁定的目标組基本訊息；當規則綁定目标組時，會返回該欄位
注意：此欄位可能返回 null，表示取不到有效值。
        :type TargetGroup: :class:`tencentcloud.clb.v20180317.models.BasicTargetGroupInfo`
        :param WafDomainId: WAF實例ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type WafDomainId: str
        :param TrpcCallee: TRPC被調服務器路由，ForwardType爲TRPC時有效
注意：此欄位可能返回 null，表示取不到有效值。
        :type TrpcCallee: str
        :param TrpcFunc: TRPC調用服務介面，ForwardType爲TRPC時有效
注意：此欄位可能返回 null，表示取不到有效值。
        :type TrpcFunc: str
        :param QuicStatus: QUIC狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type QuicStatus: str
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
        self.ForwardType = None
        self.CreateTime = None
        self.TargetType = None
        self.TargetGroup = None
        self.WafDomainId = None
        self.TrpcCallee = None
        self.TrpcFunc = None
        self.QuicStatus = None


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
        self.ForwardType = params.get("ForwardType")
        self.CreateTime = params.get("CreateTime")
        self.TargetType = params.get("TargetType")
        if params.get("TargetGroup") is not None:
            self.TargetGroup = BasicTargetGroupInfo()
            self.TargetGroup._deserialize(params.get("TargetGroup"))
        self.WafDomainId = params.get("WafDomainId")
        self.TrpcCallee = params.get("TrpcCallee")
        self.TrpcFunc = params.get("TrpcFunc")
        self.QuicStatus = params.get("QuicStatus")


class RuleTargets(AbstractModel):
    """HTTP/HTTPS監聽器下的轉發規則綁定的後端服務訊息

    """

    def __init__(self):
        """
        :param LocationId: 轉發規則的 ID
        :type LocationId: str
        :param Domain: 轉發規則的域名
        :type Domain: str
        :param Url: 轉發規則的路徑。
        :type Url: str
        :param Targets: 後端服務的訊息
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


class SetLoadBalancerClsLogRequest(AbstractModel):
    """SetLoadBalancerClsLog請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例 ID
        :type LoadBalancerId: str
        :param LogSetId: 日志服務(CLS)的日志集ID
        :type LogSetId: str
        :param LogTopicId: 日志服務(CLS)的日志主題ID
        :type LogTopicId: str
        """
        self.LoadBalancerId = None
        self.LogSetId = None
        self.LogTopicId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LogSetId = params.get("LogSetId")
        self.LogTopicId = params.get("LogTopicId")


class SetLoadBalancerClsLogResponse(AbstractModel):
    """SetLoadBalancerClsLog返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetLoadBalancerSecurityGroupsRequest(AbstractModel):
    """SetLoadBalancerSecurityGroups請求參數結構體

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡實例 ID
        :type LoadBalancerId: str
        :param SecurityGroups: 安全組ID構成的數組，一個負載均衡實例最多可綁定50個安全組，如果要解綁所有安全組，可不傳此參數，或傳入空數組。
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


class SetSecurityGroupForLoadbalancersRequest(AbstractModel):
    """SetSecurityGroupForLoadbalancers請求參數結構體

    """

    def __init__(self):
        """
        :param SecurityGroup: 安全組ID，如 sg-12345678
        :type SecurityGroup: str
        :param OperationType: ADD 綁定安全組；
DEL 解綁安全組
        :type OperationType: str
        :param LoadBalancerIds: 負載均衡實例ID數組
        :type LoadBalancerIds: list of str
        """
        self.SecurityGroup = None
        self.OperationType = None
        self.LoadBalancerIds = None


    def _deserialize(self, params):
        self.SecurityGroup = params.get("SecurityGroup")
        self.OperationType = params.get("OperationType")
        self.LoadBalancerIds = params.get("LoadBalancerIds")


class SetSecurityGroupForLoadbalancersResponse(AbstractModel):
    """SetSecurityGroupForLoadbalancers返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SnatIp(AbstractModel):
    """SnatIp的訊息結構

    """

    def __init__(self):
        """
        :param SubnetId: 私有網絡子網的唯一性id，如subnet-12345678
        :type SubnetId: str
        :param Ip: IP網址，如192.168.0.1
        :type Ip: str
        """
        self.SubnetId = None
        self.Ip = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.Ip = params.get("Ip")


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
    """轉發目标，即綁定在負載均衡上的後端服務

    """

    def __init__(self):
        """
        :param Port: 後端服務的監聽端口
注意：此欄位可能返回 null，表示取不到有效值。
        :type Port: int
        :param Type: 後端服務的類型，可取：CVM（雲伺服器）、ENI（彈性網卡）；作爲入參時，目前本參數暫不生效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Type: str
        :param InstanceId: 綁定CVM時需要傳入此參數，代表CVM的唯一 ID，可通過 DescribeInstances 介面返回欄位中的 InstanceId 欄位獲取。
注意：參數 InstanceId 和 EniIp 只能傳入一個且必須傳入一個。
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param Weight: 後端服務的轉發權重，取值範圍：[0, 100]，預設爲 10。
        :type Weight: int
        :param EniIp: 綁定彈性網卡時需要傳入此參數，代表彈性網卡的IP，彈性網卡必須先綁定至CVM，然後才能綁定到負載均衡實例。注意：參數 InstanceId 和 EniIp 只能傳入一個且必須傳入一個。注意：綁定彈性網卡需要先提交工單開白名單使用。
注意：此欄位可能返回 null，表示取不到有效值。
        :type EniIp: str
        """
        self.Port = None
        self.Type = None
        self.InstanceId = None
        self.Weight = None
        self.EniIp = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.Type = params.get("Type")
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")
        self.EniIp = params.get("EniIp")


class TargetGroupAssociation(AbstractModel):
    """規則與目标組的關聯關系

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡ID
        :type LoadBalancerId: str
        :param ListenerId: 監聽器ID
        :type ListenerId: str
        :param TargetGroupId: 目标組ID
        :type TargetGroupId: str
        :param LocationId: 轉發規則ID
        :type LocationId: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.TargetGroupId = None
        self.LocationId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.TargetGroupId = params.get("TargetGroupId")
        self.LocationId = params.get("LocationId")


class TargetGroupBackend(AbstractModel):
    """目标組綁定的後端服務器

    """

    def __init__(self):
        """
        :param TargetGroupId: 目标組ID
        :type TargetGroupId: str
        :param Type: 後端服務的類型，可取：CVM、ENI（即将支援）
        :type Type: str
        :param InstanceId: 後端服務的唯一 ID
        :type InstanceId: str
        :param Port: 後端服務的監聽端口
        :type Port: int
        :param Weight: 後端服務的轉發權重，取值範圍：[0, 100]，預設爲 10。
        :type Weight: int
        :param PublicIpAddresses: 後端服務的外網 IP
注意：此欄位可能返回 null，表示取不到有效值。
        :type PublicIpAddresses: list of str
        :param PrivateIpAddresses: 後端服務的内網 IP
注意：此欄位可能返回 null，表示取不到有效值。
        :type PrivateIpAddresses: list of str
        :param InstanceName: 後端服務的實例名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param RegisteredTime: 後端服務被綁定的時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type RegisteredTime: str
        :param EniId: 彈性網卡唯一ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type EniId: str
        """
        self.TargetGroupId = None
        self.Type = None
        self.InstanceId = None
        self.Port = None
        self.Weight = None
        self.PublicIpAddresses = None
        self.PrivateIpAddresses = None
        self.InstanceName = None
        self.RegisteredTime = None
        self.EniId = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        self.Type = params.get("Type")
        self.InstanceId = params.get("InstanceId")
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.InstanceName = params.get("InstanceName")
        self.RegisteredTime = params.get("RegisteredTime")
        self.EniId = params.get("EniId")


class TargetGroupInfo(AbstractModel):
    """目标組訊息

    """

    def __init__(self):
        """
        :param TargetGroupId: 目标組ID
        :type TargetGroupId: str
        :param VpcId: 目标組的vpcid
        :type VpcId: str
        :param TargetGroupName: 目标組的名字
        :type TargetGroupName: str
        :param Port: 目标組的預設端口
注意：此欄位可能返回 null，表示取不到有效值。
        :type Port: int
        :param CreatedTime: 目标組的創建時間
        :type CreatedTime: str
        :param UpdatedTime: 目标組的修改時間
        :type UpdatedTime: str
        :param AssociatedRule: 關聯到的規則數組
注意：此欄位可能返回 null，表示取不到有效值。
        :type AssociatedRule: list of AssociationItem
        """
        self.TargetGroupId = None
        self.VpcId = None
        self.TargetGroupName = None
        self.Port = None
        self.CreatedTime = None
        self.UpdatedTime = None
        self.AssociatedRule = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        self.VpcId = params.get("VpcId")
        self.TargetGroupName = params.get("TargetGroupName")
        self.Port = params.get("Port")
        self.CreatedTime = params.get("CreatedTime")
        self.UpdatedTime = params.get("UpdatedTime")
        if params.get("AssociatedRule") is not None:
            self.AssociatedRule = []
            for item in params.get("AssociatedRule"):
                obj = AssociationItem()
                obj._deserialize(item)
                self.AssociatedRule.append(obj)


class TargetGroupInstance(AbstractModel):
    """目标組實例

    """

    def __init__(self):
        """
        :param BindIP: 目标組實例的内網IP
        :type BindIP: str
        :param Port: 目标組實例的端口
        :type Port: int
        :param Weight: 目标組實例的權重
        :type Weight: int
        :param NewPort: 目标組實例的新端口
        :type NewPort: int
        """
        self.BindIP = None
        self.Port = None
        self.Weight = None
        self.NewPort = None


    def _deserialize(self, params):
        self.BindIP = params.get("BindIP")
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")
        self.NewPort = params.get("NewPort")


class TargetHealth(AbstractModel):
    """描述一個Target的健康訊息

    """

    def __init__(self):
        """
        :param IP: Target的内網IP
        :type IP: str
        :param Port: Target綁定的端口
        :type Port: int
        :param HealthStatus: 當前健康狀态，true：健康，false：不健康（包括尚未開始探測、探測中、狀态異常等幾種狀态）。只有處于健康狀态（且權重大于0），負載均衡才會向其轉發流量。
        :type HealthStatus: bool
        :param TargetId: Target的實例ID，如 ins-12345678
        :type TargetId: str
        :param HealthStatusDetial: 當前健康狀态的詳細訊息。如：Alive、Dead、Unknown。Alive狀态爲健康，Dead狀态爲異常，Unknown狀态包括尚未開始探測、探測中、狀态未知。
        :type HealthStatusDetial: str
        """
        self.IP = None
        self.Port = None
        self.HealthStatus = None
        self.TargetId = None
        self.HealthStatusDetial = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.Port = params.get("Port")
        self.HealthStatus = params.get("HealthStatus")
        self.TargetId = params.get("TargetId")
        self.HealthStatusDetial = params.get("HealthStatusDetial")


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


class ZoneInfo(AbstractModel):
    """可用區相關訊息

    """

    def __init__(self):
        """
        :param ZoneId: 可用區數值形式的唯一ID，如：100001
注意：此欄位可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param Zone: 可用區字串形式的唯一ID，如：ap-guangzhou-1
注意：此欄位可能返回 null，表示取不到有效值。
        :type Zone: str
        :param ZoneName: 可用區名稱，如：廣州一區
注意：此欄位可能返回 null，表示取不到有效值。
        :type ZoneName: str
        """
        self.ZoneId = None
        self.Zone = None
        self.ZoneName = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.Zone = params.get("Zone")
        self.ZoneName = params.get("ZoneName")