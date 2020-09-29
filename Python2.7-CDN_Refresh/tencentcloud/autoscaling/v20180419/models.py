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


class Activity(AbstractModel):
    """符合條件的伸縮活動相關訊息。

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸縮組ID。
        :type AutoScalingGroupId: str
        :param ActivityId: 伸縮活動ID。
        :type ActivityId: str
        :param ActivityType: 伸縮活動類型。取值如下：<br>
<li>SCALE_OUT：擴容活動<li>SCALE_IN：縮容活動<li>ATTACH_INSTANCES：添加實例<li>REMOVE_INSTANCES：銷毀實例<li>DETACH_INSTANCES：移出實例<li>TERMINATE_INSTANCES_UNEXPECTEDLY：實例在CVM控制台被銷毀<li>REPLACE_UNHEALTHY_INSTANCE：替換不健康實例
<li>START_INSTANCES：開啓實例
<li>STOP_INSTANCES：關閉實例
        :type ActivityType: str
        :param StatusCode: 伸縮活動狀态。取值如下：<br>
<li>INIT：初始化中
<li>RUNNING：運作中
<li>SUCCESSFUL：活動成功
<li>PARTIALLY_SUCCESSFUL：活動部分成功
<li>FAILED：活動失敗
<li>CANCELLED：活動取消
        :type StatusCode: str
        :param StatusMessage: 伸縮活動狀态描述。
        :type StatusMessage: str
        :param Cause: 伸縮活動起因。
        :type Cause: str
        :param Description: 伸縮活動描述。
        :type Description: str
        :param StartTime: 伸縮活動開始時間。
        :type StartTime: str
        :param EndTime: 伸縮活動結束時間。
        :type EndTime: str
        :param CreatedTime: 伸縮活動創建時間。
        :type CreatedTime: str
        :param ActivityRelatedInstanceSet: 伸縮活動相關實例訊息集合。
        :type ActivityRelatedInstanceSet: list of ActivtyRelatedInstance
        :param StatusMessageSimplified: 伸縮活動狀态簡要描述。
        :type StatusMessageSimplified: str
        :param LifecycleActionResultSet: 伸縮活動中生命週期挂鈎的執行結果。
        :type LifecycleActionResultSet: list of LifecycleActionResultInfo
        """
        self.AutoScalingGroupId = None
        self.ActivityId = None
        self.ActivityType = None
        self.StatusCode = None
        self.StatusMessage = None
        self.Cause = None
        self.Description = None
        self.StartTime = None
        self.EndTime = None
        self.CreatedTime = None
        self.ActivityRelatedInstanceSet = None
        self.StatusMessageSimplified = None
        self.LifecycleActionResultSet = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.ActivityId = params.get("ActivityId")
        self.ActivityType = params.get("ActivityType")
        self.StatusCode = params.get("StatusCode")
        self.StatusMessage = params.get("StatusMessage")
        self.Cause = params.get("Cause")
        self.Description = params.get("Description")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.CreatedTime = params.get("CreatedTime")
        if params.get("ActivityRelatedInstanceSet") is not None:
            self.ActivityRelatedInstanceSet = []
            for item in params.get("ActivityRelatedInstanceSet"):
                obj = ActivtyRelatedInstance()
                obj._deserialize(item)
                self.ActivityRelatedInstanceSet.append(obj)
        self.StatusMessageSimplified = params.get("StatusMessageSimplified")
        if params.get("LifecycleActionResultSet") is not None:
            self.LifecycleActionResultSet = []
            for item in params.get("LifecycleActionResultSet"):
                obj = LifecycleActionResultInfo()
                obj._deserialize(item)
                self.LifecycleActionResultSet.append(obj)


class ActivtyRelatedInstance(AbstractModel):
    """與本次伸縮活動相關的實例訊息。

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID。
        :type InstanceId: str
        :param InstanceStatus: 實例在伸縮活動中的狀态。取值如下：
<li>INIT：初始化中
<li>RUNNING：實例操作中
<li>SUCCESSFUL：活動成功
<li>FAILED：活動失敗
        :type InstanceStatus: str
        """
        self.InstanceId = None
        self.InstanceStatus = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceStatus = params.get("InstanceStatus")


class AttachInstancesRequest(AbstractModel):
    """AttachInstances請求參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸縮組ID
        :type AutoScalingGroupId: str
        :param InstanceIds: CVM實例ID清單
        :type InstanceIds: list of str
        """
        self.AutoScalingGroupId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.InstanceIds = params.get("InstanceIds")


class AttachInstancesResponse(AbstractModel):
    """AttachInstances返回參數結構體

    """

    def __init__(self):
        """
        :param ActivityId: 伸縮活動ID
        :type ActivityId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ActivityId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ActivityId = params.get("ActivityId")
        self.RequestId = params.get("RequestId")


class AutoScalingGroup(AbstractModel):
    """伸縮組

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸縮組ID
        :type AutoScalingGroupId: str
        :param AutoScalingGroupName: 伸縮組名稱
        :type AutoScalingGroupName: str
        :param AutoScalingGroupStatus: 伸縮組當前狀态。取值範圍：<br><li>NORMAL：正常<br><li>CVM_ABNORMAL：啓動配置異常<br><li>LB_ABNORMAL：負載均衡器異常<br><li>VPC_ABNORMAL：VPC網絡異常<br><li>INSUFFICIENT_BALANCE：餘額不足<br><li>LB_BACKEND_REGION_NOT_MATCH：CLB實例後端地域與AS服務所在地域不比對<br>
        :type AutoScalingGroupStatus: str
        :param CreatedTime: 創建時間，采用UTC標準計時
        :type CreatedTime: str
        :param DefaultCooldown: 預設冷卻時間，單位秒
        :type DefaultCooldown: int
        :param DesiredCapacity: 期望實例數
        :type DesiredCapacity: int
        :param EnabledStatus: 啓用狀态，取值包括`ENABLED`和`DISABLED`
        :type EnabledStatus: str
        :param ForwardLoadBalancerSet: 應用型負載均衡器清單
        :type ForwardLoadBalancerSet: list of ForwardLoadBalancer
        :param InstanceCount: 實例數量
        :type InstanceCount: int
        :param InServiceInstanceCount: 狀态爲`IN_SERVICE`實例的數量
        :type InServiceInstanceCount: int
        :param LaunchConfigurationId: 啓動配置ID
        :type LaunchConfigurationId: str
        :param LaunchConfigurationName: 啓動配置名稱
        :type LaunchConfigurationName: str
        :param LoadBalancerIdSet: 傳統型負載均衡器ID清單
        :type LoadBalancerIdSet: list of str
        :param MaxSize: 最大實例數
        :type MaxSize: int
        :param MinSize: 最小實例數
        :type MinSize: int
        :param ProjectId: 項目ID
        :type ProjectId: int
        :param SubnetIdSet: 子網ID清單
        :type SubnetIdSet: list of str
        :param TerminationPolicySet: 銷毀策略
        :type TerminationPolicySet: list of str
        :param VpcId: VPC標識
        :type VpcId: str
        :param ZoneSet: 可用區清單
        :type ZoneSet: list of str
        :param RetryPolicy: 重試策略
        :type RetryPolicy: str
        :param InActivityStatus: 伸縮組是否處於伸縮活動中，`IN_ACTIVITY`表示處於伸縮活動中，`NOT_IN_ACTIVITY`表示不處於伸縮活動中。
        :type InActivityStatus: str
        :param Tags: 伸縮組標簽清單
        :type Tags: list of Tag
        :param ServiceSettings: 服務設置
        :type ServiceSettings: :class:`taifucloudcloud.autoscaling.v20180419.models.ServiceSettings`
        :param Ipv6AddressCount: 實例具有IPv6網址數量的配置
        :type Ipv6AddressCount: int
        :param MultiZoneSubnetPolicy: 多可用區/子網策略。
<br><li> PRIORITY，按照可用區/子網清單的順序，作爲優先級來嘗試創建實例，如果優先級最高的可用區/子網可以創建成功，則總在該可用區/子網創建。
<br><li> EQUALITY：每次選擇當前實例數最少的可用區/子網進行擴容，使得每個可用區/子網都有機會發生擴容，多次擴容出的實例會打散到多個可用區/子網。
        :type MultiZoneSubnetPolicy: str
        """
        self.AutoScalingGroupId = None
        self.AutoScalingGroupName = None
        self.AutoScalingGroupStatus = None
        self.CreatedTime = None
        self.DefaultCooldown = None
        self.DesiredCapacity = None
        self.EnabledStatus = None
        self.ForwardLoadBalancerSet = None
        self.InstanceCount = None
        self.InServiceInstanceCount = None
        self.LaunchConfigurationId = None
        self.LaunchConfigurationName = None
        self.LoadBalancerIdSet = None
        self.MaxSize = None
        self.MinSize = None
        self.ProjectId = None
        self.SubnetIdSet = None
        self.TerminationPolicySet = None
        self.VpcId = None
        self.ZoneSet = None
        self.RetryPolicy = None
        self.InActivityStatus = None
        self.Tags = None
        self.ServiceSettings = None
        self.Ipv6AddressCount = None
        self.MultiZoneSubnetPolicy = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.AutoScalingGroupName = params.get("AutoScalingGroupName")
        self.AutoScalingGroupStatus = params.get("AutoScalingGroupStatus")
        self.CreatedTime = params.get("CreatedTime")
        self.DefaultCooldown = params.get("DefaultCooldown")
        self.DesiredCapacity = params.get("DesiredCapacity")
        self.EnabledStatus = params.get("EnabledStatus")
        if params.get("ForwardLoadBalancerSet") is not None:
            self.ForwardLoadBalancerSet = []
            for item in params.get("ForwardLoadBalancerSet"):
                obj = ForwardLoadBalancer()
                obj._deserialize(item)
                self.ForwardLoadBalancerSet.append(obj)
        self.InstanceCount = params.get("InstanceCount")
        self.InServiceInstanceCount = params.get("InServiceInstanceCount")
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.LaunchConfigurationName = params.get("LaunchConfigurationName")
        self.LoadBalancerIdSet = params.get("LoadBalancerIdSet")
        self.MaxSize = params.get("MaxSize")
        self.MinSize = params.get("MinSize")
        self.ProjectId = params.get("ProjectId")
        self.SubnetIdSet = params.get("SubnetIdSet")
        self.TerminationPolicySet = params.get("TerminationPolicySet")
        self.VpcId = params.get("VpcId")
        self.ZoneSet = params.get("ZoneSet")
        self.RetryPolicy = params.get("RetryPolicy")
        self.InActivityStatus = params.get("InActivityStatus")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("ServiceSettings") is not None:
            self.ServiceSettings = ServiceSettings()
            self.ServiceSettings._deserialize(params.get("ServiceSettings"))
        self.Ipv6AddressCount = params.get("Ipv6AddressCount")
        self.MultiZoneSubnetPolicy = params.get("MultiZoneSubnetPolicy")


class AutoScalingGroupAbstract(AbstractModel):
    """伸縮組簡明訊息。

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸縮組ID。
        :type AutoScalingGroupId: str
        :param AutoScalingGroupName: 伸縮組名稱。
        :type AutoScalingGroupName: str
        """
        self.AutoScalingGroupId = None
        self.AutoScalingGroupName = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.AutoScalingGroupName = params.get("AutoScalingGroupName")


class AutoScalingNotification(AbstractModel):
    """彈性伸縮事件通知

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸縮組ID。
        :type AutoScalingGroupId: str
        :param NotificationUserGroupIds: 用戶組ID清單。
        :type NotificationUserGroupIds: list of str
        :param NotificationTypes: 通知事件清單。
        :type NotificationTypes: list of str
        :param AutoScalingNotificationId: 事件通知ID。
        :type AutoScalingNotificationId: str
        """
        self.AutoScalingGroupId = None
        self.NotificationUserGroupIds = None
        self.NotificationTypes = None
        self.AutoScalingNotificationId = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.NotificationUserGroupIds = params.get("NotificationUserGroupIds")
        self.NotificationTypes = params.get("NotificationTypes")
        self.AutoScalingNotificationId = params.get("AutoScalingNotificationId")


class CompleteLifecycleActionRequest(AbstractModel):
    """CompleteLifecycleAction請求參數結構體

    """

    def __init__(self):
        """
        :param LifecycleHookId: 生命週期挂鈎ID
        :type LifecycleHookId: str
        :param LifecycleActionResult: 生命週期動作的結果，取值範圍爲“CONTINUE”或“ABANDON”
        :type LifecycleActionResult: str
        :param InstanceId: 實例ID，“InstanceId”和“LifecycleActionToken”必須填充其中一個
        :type InstanceId: str
        :param LifecycleActionToken: “InstanceId”和“LifecycleActionToken”必須填充其中一個
        :type LifecycleActionToken: str
        """
        self.LifecycleHookId = None
        self.LifecycleActionResult = None
        self.InstanceId = None
        self.LifecycleActionToken = None


    def _deserialize(self, params):
        self.LifecycleHookId = params.get("LifecycleHookId")
        self.LifecycleActionResult = params.get("LifecycleActionResult")
        self.InstanceId = params.get("InstanceId")
        self.LifecycleActionToken = params.get("LifecycleActionToken")


class CompleteLifecycleActionResponse(AbstractModel):
    """CompleteLifecycleAction返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAutoScalingGroupFromInstanceRequest(AbstractModel):
    """CreateAutoScalingGroupFromInstance請求參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingGroupName: 伸縮組名稱，在您賬號中必須唯一。名稱僅支援中文、英文、數字、下劃線、分隔符"-"、小數點，最大長度不能超55個位元。
        :type AutoScalingGroupName: str
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param MinSize: 最大實例數，取值範圍爲0-2000。
        :type MinSize: int
        :param MaxSize: 最小實例數，取值範圍爲0-2000。
        :type MaxSize: int
        :param DesiredCapacity: 期望實例數，大小介於最小實例數和最大實例數之間。
        :type DesiredCapacity: int
        :param InheritInstanceTag: 是否繼承實例標簽，預設值爲False
        :type InheritInstanceTag: bool
        """
        self.AutoScalingGroupName = None
        self.InstanceId = None
        self.MinSize = None
        self.MaxSize = None
        self.DesiredCapacity = None
        self.InheritInstanceTag = None


    def _deserialize(self, params):
        self.AutoScalingGroupName = params.get("AutoScalingGroupName")
        self.InstanceId = params.get("InstanceId")
        self.MinSize = params.get("MinSize")
        self.MaxSize = params.get("MaxSize")
        self.DesiredCapacity = params.get("DesiredCapacity")
        self.InheritInstanceTag = params.get("InheritInstanceTag")


class CreateAutoScalingGroupFromInstanceResponse(AbstractModel):
    """CreateAutoScalingGroupFromInstance返回參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸縮組ID
        :type AutoScalingGroupId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AutoScalingGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.RequestId = params.get("RequestId")


class CreateAutoScalingGroupRequest(AbstractModel):
    """CreateAutoScalingGroup請求參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingGroupName: 伸縮組名稱，在您賬號中必須唯一。名稱僅支援中文、英文、數字、下劃線、分隔符"-"、小數點，最大長度不能超55個位元。
        :type AutoScalingGroupName: str
        :param LaunchConfigurationId: 啓動配置ID
        :type LaunchConfigurationId: str
        :param MaxSize: 最大實例數，取值範圍爲0-2000。
        :type MaxSize: int
        :param MinSize: 最小實例數，取值範圍爲0-2000。
        :type MinSize: int
        :param VpcId: VPC ID，基礎網絡則填空字串
        :type VpcId: str
        :param DefaultCooldown: 預設冷卻時間，單位秒，預設值爲300
        :type DefaultCooldown: int
        :param DesiredCapacity: 期望實例數，大小介於最小實例數和最大實例數之間
        :type DesiredCapacity: int
        :param LoadBalancerIds: 傳統負載均衡器ID清單，目前長度上限爲20，LoadBalancerIds 和 ForwardLoadBalancers 二者同時最多只能指定一個
        :type LoadBalancerIds: list of str
        :param ProjectId: 項目ID
        :type ProjectId: int
        :param ForwardLoadBalancers: 應用型負載均衡器清單，目前長度上限爲20，LoadBalancerIds 和 ForwardLoadBalancers 二者同時最多只能指定一個
        :type ForwardLoadBalancers: list of ForwardLoadBalancer
        :param SubnetIds: 子網ID清單，VPC場景下必須指定子網。多個子網以填寫順序爲優先級，依次進行嘗試，直至可以成功創建實例。
        :type SubnetIds: list of str
        :param TerminationPolicies: 銷毀策略，目前長度上限爲1。取值包括 OLDEST_INSTANCE 和 NEWEST_INSTANCE，預設取值爲 OLDEST_INSTANCE。
<br><li> OLDEST_INSTANCE 優先銷毀伸縮組中最舊的實例。
<br><li> NEWEST_INSTANCE，優先銷毀伸縮組中最新的實例。
        :type TerminationPolicies: list of str
        :param Zones: 可用區清單，基礎網絡場景下必須指定可用區。多個可用區以填寫順序爲優先級，依次進行嘗試，直至可以成功創建實例。
        :type Zones: list of str
        :param RetryPolicy: 重試策略，取值包括 IMMEDIATE_RETRY、 INCREMENTAL_INTERVALS、NO_RETRY，預設取值爲 IMMEDIATE_RETRY。
<br><li> IMMEDIATE_RETRY，立即重試，在較短時間内快速重試，連續失敗超過一定次數（5次）後不再重試。
<br><li> INCREMENTAL_INTERVALS，間隔遞增重試，随着連續失敗次數的增加，重試間隔逐漸增大，重試間隔從秒級到1天不等。
<br><li> NO_RETRY，不進行重試，直到再次收到用戶調用或者告警訊息後才會重試。
        :type RetryPolicy: str
        :param ZonesCheckPolicy: 可用區校驗策略，取值包括 ALL 和 ANY，預設取值爲ANY。
<br><li> ALL，所有可用區（Zone）或子網（SubnetId）都可用則通過校驗，否則校驗報錯。
<br><li> ANY，存在任何一個可用區（Zone）或子網（SubnetId）可用則通過校驗，否則校驗報錯。

可用區或子網不可用的常見原因包括該可用區CVM實例類型售罄、該可用區CBS雲盤售罄、該可用區配額不足、該子網IP不足等。
如果 Zones/SubnetIds 中可用區或者子網不存在，則無論 ZonesCheckPolicy 采用何種取值，都會校驗報錯。
        :type ZonesCheckPolicy: str
        :param Tags: 標簽描述清單。通過指定該參數可以支援綁定標簽到伸縮組。同時綁定標簽到相應的資源實例，
        :type Tags: list of Tag
        :param ServiceSettings: 服務設置，包括雲監控不健康替換等服務設置。
        :type ServiceSettings: :class:`taifucloudcloud.autoscaling.v20180419.models.ServiceSettings`
        :param Ipv6AddressCount: 實例具有IPv6網址數量的配置，取值包括 0、1，預設值爲0。
        :type Ipv6AddressCount: int
        :param MultiZoneSubnetPolicy: 多可用區/子網策略，取值包括 PRIORITY 和 EQUALITY，預設爲 PRIORITY。
<br><li> PRIORITY，按照可用區/子網清單的順序，作爲優先級來嘗試創建實例，如果優先級最高的可用區/子網可以創建成功，則總在該可用區/子網創建。
<br><li> EQUALITY：每次選擇當前實例數最少的可用區/子網進行擴容，使得每個可用區/子網都有機會發生擴容，多次擴容出的實例會打散到多個可用區/子網。

與本策略相關的注意點：
<br><li> 當伸縮組爲基礎網絡時，本策略适用於多可用區；當伸縮組爲VPC網絡時，本策略适用於多子網，此時不再考慮可用區因素，例如四個子網ABCD，其中ABC處於可用區1，D處於可用區2，此時考慮子網ABCD進行排序，而不考慮可用區1、2。
<br><li> 本策略适用於多可用區/子網，不适用於啓動配置的多機型。多機型按照優先級策略進行選擇。
<br><li> 創建實例時，先保證多機型的策略，後保證多可用區/子網的策略。例如多機型A、B，多子網1、2、3（按照PRIORITY策略），會按照A1、A2、A3、B1、B2、B3 進行嘗試，如果A1售罄，會嘗試A2（而非B1）。
<br><li> 無論使用哪種策略，單次伸縮活動總是優先保持使用一種具體配置（機型 * 可用區/子網）。
        :type MultiZoneSubnetPolicy: str
        """
        self.AutoScalingGroupName = None
        self.LaunchConfigurationId = None
        self.MaxSize = None
        self.MinSize = None
        self.VpcId = None
        self.DefaultCooldown = None
        self.DesiredCapacity = None
        self.LoadBalancerIds = None
        self.ProjectId = None
        self.ForwardLoadBalancers = None
        self.SubnetIds = None
        self.TerminationPolicies = None
        self.Zones = None
        self.RetryPolicy = None
        self.ZonesCheckPolicy = None
        self.Tags = None
        self.ServiceSettings = None
        self.Ipv6AddressCount = None
        self.MultiZoneSubnetPolicy = None


    def _deserialize(self, params):
        self.AutoScalingGroupName = params.get("AutoScalingGroupName")
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.MaxSize = params.get("MaxSize")
        self.MinSize = params.get("MinSize")
        self.VpcId = params.get("VpcId")
        self.DefaultCooldown = params.get("DefaultCooldown")
        self.DesiredCapacity = params.get("DesiredCapacity")
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.ProjectId = params.get("ProjectId")
        if params.get("ForwardLoadBalancers") is not None:
            self.ForwardLoadBalancers = []
            for item in params.get("ForwardLoadBalancers"):
                obj = ForwardLoadBalancer()
                obj._deserialize(item)
                self.ForwardLoadBalancers.append(obj)
        self.SubnetIds = params.get("SubnetIds")
        self.TerminationPolicies = params.get("TerminationPolicies")
        self.Zones = params.get("Zones")
        self.RetryPolicy = params.get("RetryPolicy")
        self.ZonesCheckPolicy = params.get("ZonesCheckPolicy")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("ServiceSettings") is not None:
            self.ServiceSettings = ServiceSettings()
            self.ServiceSettings._deserialize(params.get("ServiceSettings"))
        self.Ipv6AddressCount = params.get("Ipv6AddressCount")
        self.MultiZoneSubnetPolicy = params.get("MultiZoneSubnetPolicy")


class CreateAutoScalingGroupResponse(AbstractModel):
    """CreateAutoScalingGroup返回參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸縮組ID
        :type AutoScalingGroupId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AutoScalingGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.RequestId = params.get("RequestId")


class CreateLaunchConfigurationRequest(AbstractModel):
    """CreateLaunchConfiguration請求參數結構體

    """

    def __init__(self):
        """
        :param LaunchConfigurationName: 啓動配置顯示名稱。名稱僅支援中文、英文、數字、下劃線、分隔符"-"、小數點，最大長度不能超60個位元。
        :type LaunchConfigurationName: str
        :param ImageId: 指定有效的[映像](https://cloud.taifucloud.com/document/product/213/4940)ID，格式形如`img-8toqc6s3`。映像類型分爲四種：<br/><li>公共映像</li><li>自定義映像</li><li>共享映像</li><li>服務市場映像</li><br/>可通過以下方式獲取可用的映像ID：<br/><li>`公共映像`、`自定義映像`、`共享映像`的映像ID可通過登入[控制台](https://console.cloud.taifucloud.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查詢；`服務映像市場`的映像ID可通過[雲市場](https://market.cloud.taifucloud.com/list)查詢。</li><li>通過調用介面 [DescribeImages](https://cloud.taifucloud.com/document/api/213/15715) ，取返回訊息中的`ImageId`欄位。</li>
        :type ImageId: str
        :param ProjectId: 實例所屬項目ID。該參數可以通過調用 [DescribeProject](https://cloud.taifucloud.com/document/api/378/4400) 的返回值中的`projectId`欄位來獲取。不填爲預設項目。
        :type ProjectId: int
        :param InstanceType: 實例機型。不同實例機型指定了不同的資源規格，具體取值可通過調用介面 [DescribeInstanceTypeConfigs](https://cloud.taifucloud.com/document/api/213/15749) 來獲得最新的規格表或參見[實例類型](https://cloud.taifucloud.com/document/product/213/11518)描述。
`InstanceType`和`InstanceTypes`參數互斥，二者必填一個且只能填寫一個。
        :type InstanceType: str
        :param SystemDisk: 實例系統盤配置訊息。若不指定該參數，則按照系統預設值進行分配。
        :type SystemDisk: :class:`taifucloudcloud.autoscaling.v20180419.models.SystemDisk`
        :param DataDisks: 實例數據盤配置訊息。若不指定該參數，則預設不購買數據盤，最多支援指定11塊數據盤。
        :type DataDisks: list of DataDisk
        :param InternetAccessible: 公網頻寬相關訊息設置。若不指定該參數，則預設公網頻寬爲0Mbps。
        :type InternetAccessible: :class:`taifucloudcloud.autoscaling.v20180419.models.InternetAccessible`
        :param LoginSettings: 實例登入設置。通過該參數可以設置實例的登入方式密碼、金鑰或保持映像的原始登入設置。預設情況下會随機生成密碼，並以站内信方式知會到用戶。
        :type LoginSettings: :class:`taifucloudcloud.autoscaling.v20180419.models.LoginSettings`
        :param SecurityGroupIds: 實例所屬安全組。該參數可以通過調用 [DescribeSecurityGroups](https://cloud.taifucloud.com/document/api/215/15808) 的返回值中的`SecurityGroupId`欄位來獲取。若不指定該參數，則預設不綁定安全組。
        :type SecurityGroupIds: list of str
        :param EnhancedService: 增強服務。通過該參數可以指定是否開啓雲安全、雲監控等服務。若不指定該參數，則預設開啓雲監控、雲安全服務。
        :type EnhancedService: :class:`taifucloudcloud.autoscaling.v20180419.models.EnhancedService`
        :param UserData: 經過 Base64 編碼後的自定義數據，最大長度不超過16KB。
        :type UserData: str
        :param InstanceChargeType: 實例計費類型，CVM預設值按照POSTPAID_BY_HOUR處理。
<br><li>POSTPAID_BY_HOUR：按小時後付費
<br><li>SPOTPAID：競價付費
        :type InstanceChargeType: str
        :param InstanceMarketOptions: 實例的市場相關選項，如競價實例相關參數，若指定實例的付費模式爲競價付費則該參數必傳。
        :type InstanceMarketOptions: :class:`taifucloudcloud.autoscaling.v20180419.models.InstanceMarketOptionsRequest`
        :param InstanceTypes: 實例機型清單，不同實例機型指定了不同的資源規格，最多支援10種實例機型。
`InstanceType`和`InstanceTypes`參數互斥，二者必填一個且只能填寫一個。
        :type InstanceTypes: list of str
        :param InstanceTypesCheckPolicy: 實例類型校驗策略，取值包括 ALL 和 ANY，預設取值爲ANY。
<br><li> ALL，所有實例類型（InstanceType）都可用則通過校驗，否則校驗報錯。
<br><li> ANY，存在任何一個實例類型（InstanceType）可用則通過校驗，否則校驗報錯。

實例類型不可用的常見原因包括該實例類型售罄、對應雲盤售罄等。
如果 InstanceTypes 中一款機型不存在或者已下線，則無論 InstanceTypesCheckPolicy 采用何種取值，都會校驗報錯。
        :type InstanceTypesCheckPolicy: str
        :param InstanceTags: 標簽清單。通過指定該參數，可以爲擴容的實例綁定標簽。最多支援指定10個標簽。
        :type InstanceTags: list of InstanceTag
        :param CamRoleName: CAM角色名稱。可通過DescribeRoleList介面返回值中的roleName獲取。
        :type CamRoleName: str
        :param HostNameSettings: 雲伺服器主機名（HostName）的相關設置。
        :type HostNameSettings: :class:`taifucloudcloud.autoscaling.v20180419.models.HostNameSettings`
        :param InstanceNameSettings: 雲伺服器實例名（InstanceName）的相關設置。
        :type InstanceNameSettings: :class:`taifucloudcloud.autoscaling.v20180419.models.InstanceNameSettings`
        :param InstanceChargePrepaid: 預付費模式，即包年包月相關參數設置。通過該參數可以指定包年包月實例的購買時長、是否設置自動續約等屬性。若指定實例的付費模式爲預付費則該參數必傳。
        :type InstanceChargePrepaid: :class:`taifucloudcloud.autoscaling.v20180419.models.InstanceChargePrepaid`
        """
        self.LaunchConfigurationName = None
        self.ImageId = None
        self.ProjectId = None
        self.InstanceType = None
        self.SystemDisk = None
        self.DataDisks = None
        self.InternetAccessible = None
        self.LoginSettings = None
        self.SecurityGroupIds = None
        self.EnhancedService = None
        self.UserData = None
        self.InstanceChargeType = None
        self.InstanceMarketOptions = None
        self.InstanceTypes = None
        self.InstanceTypesCheckPolicy = None
        self.InstanceTags = None
        self.CamRoleName = None
        self.HostNameSettings = None
        self.InstanceNameSettings = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.LaunchConfigurationName = params.get("LaunchConfigurationName")
        self.ImageId = params.get("ImageId")
        self.ProjectId = params.get("ProjectId")
        self.InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.UserData = params.get("UserData")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceMarketOptions") is not None:
            self.InstanceMarketOptions = InstanceMarketOptionsRequest()
            self.InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self.InstanceTypes = params.get("InstanceTypes")
        self.InstanceTypesCheckPolicy = params.get("InstanceTypesCheckPolicy")
        if params.get("InstanceTags") is not None:
            self.InstanceTags = []
            for item in params.get("InstanceTags"):
                obj = InstanceTag()
                obj._deserialize(item)
                self.InstanceTags.append(obj)
        self.CamRoleName = params.get("CamRoleName")
        if params.get("HostNameSettings") is not None:
            self.HostNameSettings = HostNameSettings()
            self.HostNameSettings._deserialize(params.get("HostNameSettings"))
        if params.get("InstanceNameSettings") is not None:
            self.InstanceNameSettings = InstanceNameSettings()
            self.InstanceNameSettings._deserialize(params.get("InstanceNameSettings"))
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))


class CreateLaunchConfigurationResponse(AbstractModel):
    """CreateLaunchConfiguration返回參數結構體

    """

    def __init__(self):
        """
        :param LaunchConfigurationId: 當通過本介面來創建啓動配置時會返回該參數，表示啓動配置ID。
        :type LaunchConfigurationId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.LaunchConfigurationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.RequestId = params.get("RequestId")


class CreateLifecycleHookRequest(AbstractModel):
    """CreateLifecycleHook請求參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸縮組ID
        :type AutoScalingGroupId: str
        :param LifecycleHookName: 生命週期挂鈎名稱。名稱僅支援中文、英文、數字、下劃線（_）、短橫線（-）、小數點（.），最大長度不能超128個位元。
        :type LifecycleHookName: str
        :param LifecycleTransition: 進行生命週期挂鈎的場景，取值範圍包括 INSTANCE_LAUNCHING 和 INSTANCE_TERMINATING
        :type LifecycleTransition: str
        :param DefaultResult: 定義伸縮組在生命週期挂鈎超時的情況下應采取的操作，取值範圍是 CONTINUE 或 ABANDON，預設值爲 CONTINUE
        :type DefaultResult: str
        :param HeartbeatTimeout: 生命週期挂鈎超時之前可以經過的最長時間（以秒爲單位），範圍從30到3600秒，預設值爲300秒
        :type HeartbeatTimeout: int
        :param NotificationMetadata: 彈性伸縮向通知目標發送的附加訊息，預設值爲空字串“”。最大長度不能超過1024個位元。
        :type NotificationMetadata: str
        :param NotificationTarget: 通知目標
        :type NotificationTarget: :class:`taifucloudcloud.autoscaling.v20180419.models.NotificationTarget`
        :param LifecycleTransitionType: 進行生命週期挂鈎的場景類型，取值範圍包括NORMAL 和 EXTENSION。說明：設置爲EXTENSION值，在AttachInstances、DetachInstances、RemoveInstaces介面時會觸發生命週期挂鈎操作，值爲NORMAL則不會在這些介面中觸發生命週期挂鈎。
        :type LifecycleTransitionType: str
        """
        self.AutoScalingGroupId = None
        self.LifecycleHookName = None
        self.LifecycleTransition = None
        self.DefaultResult = None
        self.HeartbeatTimeout = None
        self.NotificationMetadata = None
        self.NotificationTarget = None
        self.LifecycleTransitionType = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.LifecycleHookName = params.get("LifecycleHookName")
        self.LifecycleTransition = params.get("LifecycleTransition")
        self.DefaultResult = params.get("DefaultResult")
        self.HeartbeatTimeout = params.get("HeartbeatTimeout")
        self.NotificationMetadata = params.get("NotificationMetadata")
        if params.get("NotificationTarget") is not None:
            self.NotificationTarget = NotificationTarget()
            self.NotificationTarget._deserialize(params.get("NotificationTarget"))
        self.LifecycleTransitionType = params.get("LifecycleTransitionType")


class CreateLifecycleHookResponse(AbstractModel):
    """CreateLifecycleHook返回參數結構體

    """

    def __init__(self):
        """
        :param LifecycleHookId: 生命週期挂鈎ID
        :type LifecycleHookId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.LifecycleHookId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LifecycleHookId = params.get("LifecycleHookId")
        self.RequestId = params.get("RequestId")


class CreateNotificationConfigurationRequest(AbstractModel):
    """CreateNotificationConfiguration請求參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸縮組ID。
        :type AutoScalingGroupId: str
        :param NotificationTypes: 通知類型，即爲需要訂閱的通知類型集合，取值範圍如下：
<li>SCALE_OUT_SUCCESSFUL：擴容成功</li>
<li>SCALE_OUT_FAILED：擴容失敗</li>
<li>SCALE_IN_SUCCESSFUL：縮容成功</li>
<li>SCALE_IN_FAILED：縮容失敗</li>
<li>REPLACE_UNHEALTHY_INSTANCE_SUCCESSFUL：替換不健康子機成功</li>
<li>REPLACE_UNHEALTHY_INSTANCE_FAILED：替換不健康子機失敗</li>
        :type NotificationTypes: list of str
        :param NotificationUserGroupIds: 通知組ID，即爲用戶組ID集合，用戶組ID可以通過[ListGroups](https://cloud.taifucloud.com/document/product/598/34589)查詢。
        :type NotificationUserGroupIds: list of str
        """
        self.AutoScalingGroupId = None
        self.NotificationTypes = None
        self.NotificationUserGroupIds = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.NotificationTypes = params.get("NotificationTypes")
        self.NotificationUserGroupIds = params.get("NotificationUserGroupIds")


class CreateNotificationConfigurationResponse(AbstractModel):
    """CreateNotificationConfiguration返回參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingNotificationId: 通知ID。
        :type AutoScalingNotificationId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AutoScalingNotificationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AutoScalingNotificationId = params.get("AutoScalingNotificationId")
        self.RequestId = params.get("RequestId")


class CreatePaiInstanceRequest(AbstractModel):
    """CreatePaiInstance請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: PAI實例的域名。
        :type DomainName: str
        :param InternetAccessible: 公網頻寬相關訊息設置。
        :type InternetAccessible: :class:`taifucloudcloud.autoscaling.v20180419.models.InternetAccessible`
        :param InitScript: 啓動腳本的base64編碼字串。
        :type InitScript: str
        :param Zones: 可用區清單。
        :type Zones: list of str
        :param VpcId: VPC ID。
        :type VpcId: str
        :param SubnetIds: 子網清單。
        :type SubnetIds: list of str
        :param InstanceName: 實例顯示名稱。
        :type InstanceName: str
        :param InstanceTypes: 實例機型清單。
        :type InstanceTypes: list of str
        :param LoginSettings: 實例登入設置。
        :type LoginSettings: :class:`taifucloudcloud.autoscaling.v20180419.models.LoginSettings`
        :param InstanceChargeType: 實例計費類型。
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: 預付費模式，即包年包月相關參數設置。通過該參數可以指定包年包月實例的購買時長、是否設置自動續約等屬性。若指定實例的付費模式爲預付費則該參數必傳。
        :type InstanceChargePrepaid: :class:`taifucloudcloud.autoscaling.v20180419.models.InstanceChargePrepaid`
        """
        self.DomainName = None
        self.InternetAccessible = None
        self.InitScript = None
        self.Zones = None
        self.VpcId = None
        self.SubnetIds = None
        self.InstanceName = None
        self.InstanceTypes = None
        self.LoginSettings = None
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.InitScript = params.get("InitScript")
        self.Zones = params.get("Zones")
        self.VpcId = params.get("VpcId")
        self.SubnetIds = params.get("SubnetIds")
        self.InstanceName = params.get("InstanceName")
        self.InstanceTypes = params.get("InstanceTypes")
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))


class CreatePaiInstanceResponse(AbstractModel):
    """CreatePaiInstance返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceIdSet: 當通過本介面來創建實例時會返回該參數，表示一個或多個實例`ID`。返回實例`ID`清單並不代表實例創建成功，可根據 [DescribeInstances](https://cloud.taifucloud.com/document/api/213/15728) 介面查詢返回的InstancesSet中對應實例的`ID`的狀态來判斷創建是否完成；如果實例狀态由“準備中”變爲“正在運作”，則爲創建成功。
        :type InstanceIdSet: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.RequestId = params.get("RequestId")


class CreateScalingPolicyRequest(AbstractModel):
    """CreateScalingPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸縮組ID。
        :type AutoScalingGroupId: str
        :param ScalingPolicyName: 告警觸發策略名稱。
        :type ScalingPolicyName: str
        :param AdjustmentType: 告警觸發後，期望實例數修改方式。取值 ：<br><li>CHANGE_IN_CAPACITY：增加或減少若幹期望實例數</li><li>EXACT_CAPACITY：調整至指定期望實例數</li> <li>PERCENT_CHANGE_IN_CAPACITY：按百分比調整期望實例數</li>
        :type AdjustmentType: str
        :param AdjustmentValue: 告警觸發後，期望實例數的調整值。取值：<br><li>當 AdjustmentType 爲 CHANGE_IN_CAPACITY 時，AdjustmentValue 爲正數表示告警觸發後增加實例，爲負數表示告警觸發後減少實例 </li> <li> 當 AdjustmentType 爲 EXACT_CAPACITY 時，AdjustmentValue 的值即爲告警觸發後新的期望實例數，需要大於或等於0 </li> <li> 當 AdjustmentType 爲 PERCENT_CHANGE_IN_CAPACITY 時，AdjusmentValue 爲正數表示告警觸發後按百分比增加實例，爲負數表示告警觸發後按百分比減少實例，單位是：%。
        :type AdjustmentValue: int
        :param MetricAlarm: 告警監控指標。
        :type MetricAlarm: :class:`taifucloudcloud.autoscaling.v20180419.models.MetricAlarm`
        :param Cooldown: 冷卻時間，單位爲秒。預設冷卻時間300秒。
        :type Cooldown: int
        :param NotificationUserGroupIds: 通知組ID，即爲用戶組ID集合，用戶組ID可以通過[ListGroups](https://cloud.taifucloud.com/document/product/598/34589)查詢。
        :type NotificationUserGroupIds: list of str
        """
        self.AutoScalingGroupId = None
        self.ScalingPolicyName = None
        self.AdjustmentType = None
        self.AdjustmentValue = None
        self.MetricAlarm = None
        self.Cooldown = None
        self.NotificationUserGroupIds = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.ScalingPolicyName = params.get("ScalingPolicyName")
        self.AdjustmentType = params.get("AdjustmentType")
        self.AdjustmentValue = params.get("AdjustmentValue")
        if params.get("MetricAlarm") is not None:
            self.MetricAlarm = MetricAlarm()
            self.MetricAlarm._deserialize(params.get("MetricAlarm"))
        self.Cooldown = params.get("Cooldown")
        self.NotificationUserGroupIds = params.get("NotificationUserGroupIds")


class CreateScalingPolicyResponse(AbstractModel):
    """CreateScalingPolicy返回參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingPolicyId: 告警觸發策略ID。
        :type AutoScalingPolicyId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AutoScalingPolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AutoScalingPolicyId = params.get("AutoScalingPolicyId")
        self.RequestId = params.get("RequestId")


class CreateScheduledActionRequest(AbstractModel):
    """CreateScheduledAction請求參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸縮組ID
        :type AutoScalingGroupId: str
        :param ScheduledActionName: 定時任務名稱。名稱僅支援中文、英文、數字、下劃線、分隔符"-"、小數點，最大長度不能超60個位元。同一伸縮組下必須唯一。
        :type ScheduledActionName: str
        :param MaxSize: 當定時任務觸發時，設置的伸縮組最大實例數。
        :type MaxSize: int
        :param MinSize: 當定時任務觸發時，設置的伸縮組最小實例數。
        :type MinSize: int
        :param DesiredCapacity: 當定時任務觸發時，設置的伸縮組期望實例數。
        :type DesiredCapacity: int
        :param StartTime: 定時任務的首次觸發時間，取值爲` 時間`（UTC+8），按照`ISO8601`標準，格式：`YYYY-MM-DDThh:mm:ss+08:00`。
        :type StartTime: str
        :param EndTime: 定時任務的結束時間，取值爲` 時間`（UTC+8），按照`ISO8601`標準，格式：`YYYY-MM-DDThh:mm:ss+08:00`。<br><br>此參數與`Recurrence`需要同時指定，到達結束時間之後，定時任務将不再生效。
        :type EndTime: str
        :param Recurrence: 定時任務的重複方式。爲標準 Cron 格式<br><br>此參數與`EndTime`需要同時指定。
        :type Recurrence: str
        """
        self.AutoScalingGroupId = None
        self.ScheduledActionName = None
        self.MaxSize = None
        self.MinSize = None
        self.DesiredCapacity = None
        self.StartTime = None
        self.EndTime = None
        self.Recurrence = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.ScheduledActionName = params.get("ScheduledActionName")
        self.MaxSize = params.get("MaxSize")
        self.MinSize = params.get("MinSize")
        self.DesiredCapacity = params.get("DesiredCapacity")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Recurrence = params.get("Recurrence")


class CreateScheduledActionResponse(AbstractModel):
    """CreateScheduledAction返回參數結構體

    """

    def __init__(self):
        """
        :param ScheduledActionId: 定時任務ID
        :type ScheduledActionId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ScheduledActionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ScheduledActionId = params.get("ScheduledActionId")
        self.RequestId = params.get("RequestId")


class DataDisk(AbstractModel):
    """啓動配置的數據盤配置訊息。若不指定該參數，則預設不購買數據盤，當前僅支援購買的時候指定一個數據盤。

    """

    def __init__(self):
        """
        :param DiskType: 數據盤類型。數據盤類型限制詳見[CVM實例配置](https://cloud.taifucloud.com/document/product/213/2177)。取值範圍：<br><li>LOCAL_BASIC：本地硬碟<br><li>LOCAL_SSD：本地SSD硬碟<br><li>CLOUD_BASIC：普通雲硬碟<br><li>CLOUD_PREMIUM：高效能雲硬碟<br><li>CLOUD_SSD：SSD雲硬碟<br><br>預設取值：LOCAL_BASIC。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param DiskSize: 數據盤大小，單位：GB。最小調整步長爲10G，不同數據盤類型取值範圍不同，具體限制詳見：[CVM實例配置](https://cloud.taifucloud.com/document/product/213/2177)。預設值爲0，表示不購買數據盤。更多限制詳見産品文件。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param SnapshotId: 數據盤快照 ID，類似 `snap-l8psqwnt`。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SnapshotId: str
        """
        self.DiskType = None
        self.DiskSize = None
        self.SnapshotId = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        self.SnapshotId = params.get("SnapshotId")


class DeleteAutoScalingGroupRequest(AbstractModel):
    """DeleteAutoScalingGroup請求參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸縮組ID
        :type AutoScalingGroupId: str
        """
        self.AutoScalingGroupId = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")


class DeleteAutoScalingGroupResponse(AbstractModel):
    """DeleteAutoScalingGroup返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLaunchConfigurationRequest(AbstractModel):
    """DeleteLaunchConfiguration請求參數結構體

    """

    def __init__(self):
        """
        :param LaunchConfigurationId: 需要删除的啓動配置ID。
        :type LaunchConfigurationId: str
        """
        self.LaunchConfigurationId = None


    def _deserialize(self, params):
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")


class DeleteLaunchConfigurationResponse(AbstractModel):
    """DeleteLaunchConfiguration返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLifecycleHookRequest(AbstractModel):
    """DeleteLifecycleHook請求參數結構體

    """

    def __init__(self):
        """
        :param LifecycleHookId: 生命週期挂鈎ID
        :type LifecycleHookId: str
        """
        self.LifecycleHookId = None


    def _deserialize(self, params):
        self.LifecycleHookId = params.get("LifecycleHookId")


class DeleteLifecycleHookResponse(AbstractModel):
    """DeleteLifecycleHook返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNotificationConfigurationRequest(AbstractModel):
    """DeleteNotificationConfiguration請求參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingNotificationId: 待删除的通知ID。
        :type AutoScalingNotificationId: str
        """
        self.AutoScalingNotificationId = None


    def _deserialize(self, params):
        self.AutoScalingNotificationId = params.get("AutoScalingNotificationId")


class DeleteNotificationConfigurationResponse(AbstractModel):
    """DeleteNotificationConfiguration返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteScalingPolicyRequest(AbstractModel):
    """DeleteScalingPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingPolicyId: 待删除的告警策略ID。
        :type AutoScalingPolicyId: str
        """
        self.AutoScalingPolicyId = None


    def _deserialize(self, params):
        self.AutoScalingPolicyId = params.get("AutoScalingPolicyId")


class DeleteScalingPolicyResponse(AbstractModel):
    """DeleteScalingPolicy返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteScheduledActionRequest(AbstractModel):
    """DeleteScheduledAction請求參數結構體

    """

    def __init__(self):
        """
        :param ScheduledActionId: 待删除的定時任務ID。
        :type ScheduledActionId: str
        """
        self.ScheduledActionId = None


    def _deserialize(self, params):
        self.ScheduledActionId = params.get("ScheduledActionId")


class DeleteScheduledActionResponse(AbstractModel):
    """DeleteScheduledAction返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccountLimitsRequest(AbstractModel):
    """DescribeAccountLimits請求參數結構體

    """


class DescribeAccountLimitsResponse(AbstractModel):
    """DescribeAccountLimits返回參數結構體

    """

    def __init__(self):
        """
        :param MaxNumberOfLaunchConfigurations: 用戶帳戶被允許創建的啓動配置最大數量
        :type MaxNumberOfLaunchConfigurations: int
        :param NumberOfLaunchConfigurations: 用戶帳戶啓動配置的當前數量
        :type NumberOfLaunchConfigurations: int
        :param MaxNumberOfAutoScalingGroups: 用戶帳戶被允許創建的伸縮組最大數量
        :type MaxNumberOfAutoScalingGroups: int
        :param NumberOfAutoScalingGroups: 用戶帳戶伸縮組的當前數量
        :type NumberOfAutoScalingGroups: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.MaxNumberOfLaunchConfigurations = None
        self.NumberOfLaunchConfigurations = None
        self.MaxNumberOfAutoScalingGroups = None
        self.NumberOfAutoScalingGroups = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MaxNumberOfLaunchConfigurations = params.get("MaxNumberOfLaunchConfigurations")
        self.NumberOfLaunchConfigurations = params.get("NumberOfLaunchConfigurations")
        self.MaxNumberOfAutoScalingGroups = params.get("MaxNumberOfAutoScalingGroups")
        self.NumberOfAutoScalingGroups = params.get("NumberOfAutoScalingGroups")
        self.RequestId = params.get("RequestId")


class DescribeAutoScalingActivitiesRequest(AbstractModel):
    """DescribeAutoScalingActivities請求參數結構體

    """

    def __init__(self):
        """
        :param ActivityIds: 按照一個或者多個伸縮活動ID查詢。伸縮活動ID形如：`asa-5l2ejpfo`。每次請求的上限爲100。參數不支援同時指定`ActivityIds`和`Filters`。
        :type ActivityIds: list of str
        :param Filters: 過濾條件。
<li> auto-scaling-group-id - String - 是否必填：否 -（過濾條件）按照伸縮組ID過濾。</li>
<li> activity-status-code - String - 是否必填：否 -（過濾條件）按照伸縮活動狀态過濾。（INIT：初始化中|RUNNING：運作中|SUCCESSFUL：活動成功|PARTIALLY_SUCCESSFUL：活動部分成功|FAILED：活動失敗|CANCELLED：活動取消）</li>
<li> activity-type - String - 是否必填：否 -（過濾條件）按照伸縮活動類型過濾。（SCALE_OUT：擴容活動|SCALE_IN：縮容活動|ATTACH_INSTANCES：添加實例|REMOVE_INSTANCES：銷毀實例|DETACH_INSTANCES：移出實例|TERMINATE_INSTANCES_UNEXPECTEDLY：實例在CVM控制台被銷毀|REPLACE_UNHEALTHY_INSTANCE：替換不健康實例|UPDATE_LOAD_BALANCERS：更新負載均衡器）</li>
<li> activity-id - String - 是否必填：否 -（過濾條件）按照伸縮活動ID過濾。</li>
每次請求的`Filters`的上限爲10，`Filter.Values`的上限爲5。參數不支援同時指定`ActivityIds`和`Filters`。
        :type Filters: list of Filter
        :param Limit: 返回數量，預設爲20，最大值爲100。關於`Limit`的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。關於`Offset`的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Offset: int
        :param StartTime: 伸縮活動最早的開始時間，如果指定了ActivityIds，此參數将被忽略。取值爲`UTC`時間，按照`ISO8601`標準，格式：`YYYY-MM-DDThh:mm:ssZ`。
        :type StartTime: str
        :param EndTime: 伸縮活動最晚的結束時間，如果指定了ActivityIds，此參數将被忽略。取值爲`UTC`時間，按照`ISO8601`標準，格式：`YYYY-MM-DDThh:mm:ssZ`。
        :type EndTime: str
        """
        self.ActivityIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.ActivityIds = params.get("ActivityIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeAutoScalingActivitiesResponse(AbstractModel):
    """DescribeAutoScalingActivities返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的伸縮活動數量。
        :type TotalCount: int
        :param ActivitySet: 符合條件的伸縮活動訊息集合。
        :type ActivitySet: list of Activity
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ActivitySet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ActivitySet") is not None:
            self.ActivitySet = []
            for item in params.get("ActivitySet"):
                obj = Activity()
                obj._deserialize(item)
                self.ActivitySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAutoScalingGroupLastActivitiesRequest(AbstractModel):
    """DescribeAutoScalingGroupLastActivities請求參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingGroupIds: 伸縮組ID清單
        :type AutoScalingGroupIds: list of str
        """
        self.AutoScalingGroupIds = None


    def _deserialize(self, params):
        self.AutoScalingGroupIds = params.get("AutoScalingGroupIds")


class DescribeAutoScalingGroupLastActivitiesResponse(AbstractModel):
    """DescribeAutoScalingGroupLastActivities返回參數結構體

    """

    def __init__(self):
        """
        :param ActivitySet: 符合條件的伸縮活動訊息集合。說明：伸縮組伸縮活動不存在的則不返回，如傳50個伸縮組ID，返回45條數據，說明其中有5個伸縮組伸縮活動不存在。
        :type ActivitySet: list of Activity
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ActivitySet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ActivitySet") is not None:
            self.ActivitySet = []
            for item in params.get("ActivitySet"):
                obj = Activity()
                obj._deserialize(item)
                self.ActivitySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAutoScalingGroupsRequest(AbstractModel):
    """DescribeAutoScalingGroups請求參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingGroupIds: 按照一個或者多個伸縮組ID查詢。伸縮組ID形如：`asg-nkdwoui0`。每次請求的上限爲100。參數不支援同時指定`AutoScalingGroupIds`和`Filters`。
        :type AutoScalingGroupIds: list of str
        :param Filters: 過濾條件。
<li> auto-scaling-group-id - String - 是否必填：否 -（過濾條件）按照伸縮組ID過濾。</li>
<li> auto-scaling-group-name - String - 是否必填：否 -（過濾條件）按照伸縮組名稱過濾。</li>
<li> vague-auto-scaling-group-name - String - 是否必填：否 -（過濾條件）按照伸縮組名稱模糊搜索。</li>
<li> launch-configuration-id - String - 是否必填：否 -（過濾條件）按照啓動配置ID過濾。</li>
<li> tag-key - String - 是否必填：否 -（過濾條件）按照標簽鍵進行過濾。</li>
<li> tag-value - String - 是否必填：否 -（過濾條件）按照標簽值進行過濾。</li>
<li> tag:tag-key - String - 是否必填：否 -（過濾條件）按照標簽鍵值對進行過濾。 tag-key使用具體的標簽鍵進行替換。使用請參考範例2</li>
每次請求的`Filters`的上限爲10，`Filter.Values`的上限爲5。參數不支援同時指定`AutoScalingGroupIds`和`Filters`。
        :type Filters: list of Filter
        :param Limit: 返回數量，預設爲20，最大值爲100。關於`Limit`的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。關於`Offset`的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Offset: int
        """
        self.AutoScalingGroupIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.AutoScalingGroupIds = params.get("AutoScalingGroupIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeAutoScalingGroupsResponse(AbstractModel):
    """DescribeAutoScalingGroups返回參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingGroupSet: 伸縮組詳細訊息清單。
        :type AutoScalingGroupSet: list of AutoScalingGroup
        :param TotalCount: 符合條件的伸縮組數量。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AutoScalingGroupSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AutoScalingGroupSet") is not None:
            self.AutoScalingGroupSet = []
            for item in params.get("AutoScalingGroupSet"):
                obj = AutoScalingGroup()
                obj._deserialize(item)
                self.AutoScalingGroupSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAutoScalingInstancesRequest(AbstractModel):
    """DescribeAutoScalingInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 待查詢雲伺服器（CVM）的實例ID。參數不支援同時指定InstanceIds和Filters。
        :type InstanceIds: list of str
        :param Filters: 過濾條件。
<li> instance-id - String - 是否必填：否 -（過濾條件）按照實例ID過濾。</li>
<li> auto-scaling-group-id - String - 是否必填：否 -（過濾條件）按照伸縮組ID過濾。</li>
每次請求的`Filters`的上限爲10，`Filter.Values`的上限爲5。參數不支援同時指定`InstanceIds`和`Filters`。
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。關於`Offset`的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。關於`Limit`的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Limit: int
        """
        self.InstanceIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAutoScalingInstancesResponse(AbstractModel):
    """DescribeAutoScalingInstances返回參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingInstanceSet: 實例詳細訊息清單。
        :type AutoScalingInstanceSet: list of Instance
        :param TotalCount: 符合條件的實例數量。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AutoScalingInstanceSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AutoScalingInstanceSet") is not None:
            self.AutoScalingInstanceSet = []
            for item in params.get("AutoScalingInstanceSet"):
                obj = Instance()
                obj._deserialize(item)
                self.AutoScalingInstanceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeLaunchConfigurationsRequest(AbstractModel):
    """DescribeLaunchConfigurations請求參數結構體

    """

    def __init__(self):
        """
        :param LaunchConfigurationIds: 按照一個或者多個啓動配置ID查詢。啓動配置ID形如：`asc-ouy1ax38`。每次請求的上限爲100。參數不支援同時指定`LaunchConfigurationIds`和`Filters`
        :type LaunchConfigurationIds: list of str
        :param Filters: 過濾條件。
<li> launch-configuration-id - String - 是否必填：否 -（過濾條件）按照啓動配置ID過濾。</li>
<li> launch-configuration-name - String - 是否必填：否 -（過濾條件）按照啓動配置名稱過濾。</li>
<li> vague-launch-configuration-name - String - 是否必填：否 -（過濾條件）按照啓動配置名稱模糊搜索。</li>
每次請求的`Filters`的上限爲10，`Filter.Values`的上限爲5。參數不支援同時指定`LaunchConfigurationIds`和`Filters`。
        :type Filters: list of Filter
        :param Limit: 返回數量，預設爲20，最大值爲100。關於`Limit`的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。關於`Offset`的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Offset: int
        """
        self.LaunchConfigurationIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.LaunchConfigurationIds = params.get("LaunchConfigurationIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeLaunchConfigurationsResponse(AbstractModel):
    """DescribeLaunchConfigurations返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的啓動配置數量。
        :type TotalCount: int
        :param LaunchConfigurationSet: 啓動配置詳細訊息清單。
        :type LaunchConfigurationSet: list of LaunchConfiguration
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.LaunchConfigurationSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("LaunchConfigurationSet") is not None:
            self.LaunchConfigurationSet = []
            for item in params.get("LaunchConfigurationSet"):
                obj = LaunchConfiguration()
                obj._deserialize(item)
                self.LaunchConfigurationSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLifecycleHooksRequest(AbstractModel):
    """DescribeLifecycleHooks請求參數結構體

    """

    def __init__(self):
        """
        :param LifecycleHookIds: 按照一個或者多個生命週期挂鈎ID查詢。生命週期挂鈎ID形如：`ash-8azjzxcl`。每次請求的上限爲100。參數不支援同時指定`LifecycleHookIds`和`Filters`。
        :type LifecycleHookIds: list of str
        :param Filters: 過濾條件。
<li> lifecycle-hook-id - String - 是否必填：否 -（過濾條件）按照生命週期挂鈎ID過濾。</li>
<li> lifecycle-hook-name - String - 是否必填：否 -（過濾條件）按照生命週期挂鈎名稱過濾。</li>
<li> auto-scaling-group-id - String - 是否必填：否 -（過濾條件）按照伸縮組ID過濾。</li>
過濾條件。
<li> lifecycle-hook-id - String - 是否必填：否 -（過濾條件）按照生命週期挂鈎ID過濾。</li>
<li> lifecycle-hook-name - String - 是否必填：否 -（過濾條件）按照生命週期挂鈎名稱過濾。</li>
<li> auto-scaling-group-id - String - 是否必填：否 -（過濾條件）按照伸縮組ID過濾。</li>
每次請求的`Filters`的上限爲10，`Filter.Values`的上限爲5。參數不支援同時指定`LifecycleHookIds `和`Filters`。
        :type Filters: list of Filter
        :param Limit: 返回數量，預設爲20，最大值爲100。關於`Limit`的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。關於`Offset`的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Offset: int
        """
        self.LifecycleHookIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.LifecycleHookIds = params.get("LifecycleHookIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeLifecycleHooksResponse(AbstractModel):
    """DescribeLifecycleHooks返回參數結構體

    """

    def __init__(self):
        """
        :param LifecycleHookSet: 生命週期挂鈎數組
        :type LifecycleHookSet: list of LifecycleHook
        :param TotalCount: 總體數量
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.LifecycleHookSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LifecycleHookSet") is not None:
            self.LifecycleHookSet = []
            for item in params.get("LifecycleHookSet"):
                obj = LifecycleHook()
                obj._deserialize(item)
                self.LifecycleHookSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNotificationConfigurationsRequest(AbstractModel):
    """DescribeNotificationConfigurations請求參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingNotificationIds: 按照一個或者多個通知ID查詢。實例ID形如：asn-2sestqbr。每次請求的實例的上限爲100。參數不支援同時指定`AutoScalingNotificationIds`和`Filters`。
        :type AutoScalingNotificationIds: list of str
        :param Filters: 過濾條件。
<li> auto-scaling-notification-id - String - 是否必填：否 -（過濾條件）按照通知ID過濾。</li>
<li> auto-scaling-group-id - String - 是否必填：否 -（過濾條件）按照伸縮組ID過濾。</li>
每次請求的`Filters`的上限爲10，`Filter.Values`的上限爲5。參數不支援同時指定`AutoScalingNotificationIds`和`Filters`。
        :type Filters: list of Filter
        :param Limit: 返回數量，預設爲20，最大值爲100。關於`Limit`的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。關於`Offset`的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Offset: int
        """
        self.AutoScalingNotificationIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.AutoScalingNotificationIds = params.get("AutoScalingNotificationIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeNotificationConfigurationsResponse(AbstractModel):
    """DescribeNotificationConfigurations返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的通知數量。
        :type TotalCount: int
        :param AutoScalingNotificationSet: 彈性伸縮事件通知詳細訊息清單。
        :type AutoScalingNotificationSet: list of AutoScalingNotification
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AutoScalingNotificationSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AutoScalingNotificationSet") is not None:
            self.AutoScalingNotificationSet = []
            for item in params.get("AutoScalingNotificationSet"):
                obj = AutoScalingNotification()
                obj._deserialize(item)
                self.AutoScalingNotificationSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePaiInstancesRequest(AbstractModel):
    """DescribePaiInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 依據PAI實例的實例ID進行查詢。
        :type InstanceIds: list of str
        :param Filters: 過濾條件。
        :type Filters: list of Filter
        :param Limit: 返回數量，預設爲20，最大值爲100。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        """
        self.InstanceIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribePaiInstancesResponse(AbstractModel):
    """DescribePaiInstances返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的PAI實例數量
        :type TotalCount: int
        :param PaiInstanceSet: PAI實例詳細訊息
        :type PaiInstanceSet: list of PaiInstance
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.PaiInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PaiInstanceSet") is not None:
            self.PaiInstanceSet = []
            for item in params.get("PaiInstanceSet"):
                obj = PaiInstance()
                obj._deserialize(item)
                self.PaiInstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeScalingPoliciesRequest(AbstractModel):
    """DescribeScalingPolicies請求參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingPolicyIds: 按照一個或者多個告警策略ID查詢。告警策略ID形如：asp-i9vkg894。每次請求的實例的上限爲100。參數不支援同時指定`AutoScalingPolicyIds`和`Filters`。
        :type AutoScalingPolicyIds: list of str
        :param Filters: 過濾條件。
<li> auto-scaling-policy-id - String - 是否必填：否 -（過濾條件）按照告警策略ID過濾。</li>
<li> auto-scaling-group-id - String - 是否必填：否 -（過濾條件）按照伸縮組ID過濾。</li>
<li> scaling-policy-name - String - 是否必填：否 -（過濾條件）按照告警策略名稱過濾。</li>
每次請求的`Filters`的上限爲10，`Filter.Values`的上限爲5。參數不支援同時指定`AutoScalingPolicyIds`和`Filters`。
        :type Filters: list of Filter
        :param Limit: 返回數量，預設爲20，最大值爲100。關於`Limit`的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。關於`Offset`的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Offset: int
        """
        self.AutoScalingPolicyIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.AutoScalingPolicyIds = params.get("AutoScalingPolicyIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeScalingPoliciesResponse(AbstractModel):
    """DescribeScalingPolicies返回參數結構體

    """

    def __init__(self):
        """
        :param ScalingPolicySet: 彈性伸縮告警觸發策略詳細訊息清單。
        :type ScalingPolicySet: list of ScalingPolicy
        :param TotalCount: 符合條件的通知數量。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ScalingPolicySet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ScalingPolicySet") is not None:
            self.ScalingPolicySet = []
            for item in params.get("ScalingPolicySet"):
                obj = ScalingPolicy()
                obj._deserialize(item)
                self.ScalingPolicySet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeScheduledActionsRequest(AbstractModel):
    """DescribeScheduledActions請求參數結構體

    """

    def __init__(self):
        """
        :param ScheduledActionIds: 按照一個或者多個定時任務ID查詢。實例ID形如：asst-am691zxo。每次請求的實例的上限爲100。參數不支援同時指定ScheduledActionIds和Filters。
        :type ScheduledActionIds: list of str
        :param Filters: 過濾條件。
<li> scheduled-action-id - String - 是否必填：否 -（過濾條件）按照定時任務ID過濾。</li>
<li> scheduled-action-name - String - 是否必填：否 - （過濾條件） 按照定時任務名稱過濾。</li>
<li> auto-scaling-group-id - String - 是否必填：否 - （過濾條件） 按照伸縮組ID過濾。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。關於Offset的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。關於Limit的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Limit: int
        """
        self.ScheduledActionIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ScheduledActionIds = params.get("ScheduledActionIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeScheduledActionsResponse(AbstractModel):
    """DescribeScheduledActions返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的定時任務數量。
        :type TotalCount: int
        :param ScheduledActionSet: 定時任務詳細訊息清單。
        :type ScheduledActionSet: list of ScheduledAction
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ScheduledActionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ScheduledActionSet") is not None:
            self.ScheduledActionSet = []
            for item in params.get("ScheduledActionSet"):
                obj = ScheduledAction()
                obj._deserialize(item)
                self.ScheduledActionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DetachInstancesRequest(AbstractModel):
    """DetachInstances請求參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸縮組ID
        :type AutoScalingGroupId: str
        :param InstanceIds: CVM實例ID清單
        :type InstanceIds: list of str
        """
        self.AutoScalingGroupId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.InstanceIds = params.get("InstanceIds")


class DetachInstancesResponse(AbstractModel):
    """DetachInstances返回參數結構體

    """

    def __init__(self):
        """
        :param ActivityId: 伸縮活動ID
        :type ActivityId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ActivityId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ActivityId = params.get("ActivityId")
        self.RequestId = params.get("RequestId")


class DisableAutoScalingGroupRequest(AbstractModel):
    """DisableAutoScalingGroup請求參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸縮組ID
        :type AutoScalingGroupId: str
        """
        self.AutoScalingGroupId = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")


class DisableAutoScalingGroupResponse(AbstractModel):
    """DisableAutoScalingGroup返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableAutoScalingGroupRequest(AbstractModel):
    """EnableAutoScalingGroup請求參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸縮組ID
        :type AutoScalingGroupId: str
        """
        self.AutoScalingGroupId = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")


class EnableAutoScalingGroupResponse(AbstractModel):
    """EnableAutoScalingGroup返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnhancedService(AbstractModel):
    """描述了實例的增強服務啓用情況與其設置，如雲安全，雲監控等實例 Agent。

    """

    def __init__(self):
        """
        :param SecurityService: 開啓雲安全服務。若不指定該參數，則預設開啓雲安全服務。
        :type SecurityService: :class:`taifucloudcloud.autoscaling.v20180419.models.RunSecurityServiceEnabled`
        :param MonitorService: 開啓雲監控服務。若不指定該參數，則預設開啓雲監控服務。
        :type MonitorService: :class:`taifucloudcloud.autoscaling.v20180419.models.RunMonitorServiceEnabled`
        """
        self.SecurityService = None
        self.MonitorService = None


    def _deserialize(self, params):
        if params.get("SecurityService") is not None:
            self.SecurityService = RunSecurityServiceEnabled()
            self.SecurityService._deserialize(params.get("SecurityService"))
        if params.get("MonitorService") is not None:
            self.MonitorService = RunMonitorServiceEnabled()
            self.MonitorService._deserialize(params.get("MonitorService"))


class ExecuteScalingPolicyRequest(AbstractModel):
    """ExecuteScalingPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingPolicyId: 告警伸縮策略ID
        :type AutoScalingPolicyId: str
        :param HonorCooldown: 是否檢查伸縮組活動處於冷卻時間内，預設值爲false
        :type HonorCooldown: bool
        """
        self.AutoScalingPolicyId = None
        self.HonorCooldown = None


    def _deserialize(self, params):
        self.AutoScalingPolicyId = params.get("AutoScalingPolicyId")
        self.HonorCooldown = params.get("HonorCooldown")


class ExecuteScalingPolicyResponse(AbstractModel):
    """ExecuteScalingPolicy返回參數結構體

    """

    def __init__(self):
        """
        :param ActivityId: 伸縮活動ID
        :type ActivityId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ActivityId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ActivityId = params.get("ActivityId")
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """>描述鍵值對過濾器，用於條件過濾查詢。例如過濾ID、名稱、狀态等
    > * 若存在多個`Filter`時，`Filter`間的關系爲邏輯與（`AND`）關系。
    > * 若同一個`Filter`存在多個`Values`，同一`Filter`下`Values`間的關系爲邏輯或（`OR`）關系。
    >
    > 以[DescribeInstances](https://cloud.taifucloud.com/document/api/213/15728)介面的`Filter`爲例。若我們需要查詢可用區（`zone`）爲 一區 ***並且*** 實例計費模式（`instance-charge-type`）爲包年包月 ***或者*** 按量計費的實例時，可如下實現：
    ```
    Filters.0.Name=zone
    &Filters.0.Values.0=ap-guangzhou-1
    &Filters.1.Name=instance-charge-type
    &Filters.1.Values.0=PREPAID
    &Filters.1.Values.1=POSTPAID_BY_HOUR
    ```

    """

    def __init__(self):
        """
        :param Name: 需要過濾的欄位。
        :type Name: str
        :param Values: 欄位的過濾值。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class ForwardLoadBalancer(AbstractModel):
    """應用型負載均衡器

    """

    def __init__(self):
        """
        :param LoadBalancerId: 負載均衡器ID
        :type LoadBalancerId: str
        :param ListenerId: 應用型負載均衡監聽器 ID
        :type ListenerId: str
        :param TargetAttributes: 目標規則屬性清單
        :type TargetAttributes: list of TargetAttribute
        :param LocationId: 轉發規則ID，注意：針對七層監聽器此參數必填
        :type LocationId: str
        :param Region: 負載均衡實例所屬地域，預設取AS服務所在地域。格式與公共參數Region相同，如："ap-guangzhou"。
        :type Region: str
        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.TargetAttributes = None
        self.LocationId = None
        self.Region = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("TargetAttributes") is not None:
            self.TargetAttributes = []
            for item in params.get("TargetAttributes"):
                obj = TargetAttribute()
                obj._deserialize(item)
                self.TargetAttributes.append(obj)
        self.LocationId = params.get("LocationId")
        self.Region = params.get("Region")


class HostNameSettings(AbstractModel):
    """雲伺服器主機名（HostName）的相關設置

    """

    def __init__(self):
        """
        :param HostName: 雲伺服器的主機名。
<br><li> 點號（.）和短橫線（-）不能作爲 HostName 的首尾字元，不能連續使用。
<br><li> 不支援 Windows 實例。
<br><li> 其他類型（Linux 等）實例：字元長度爲[2, 40]，允許支援多個點號，點之間爲一段，每段允許字母（不限制大小寫）、數字和短橫線（-）組成。
注意：此欄位可能返回 null，表示取不到有效值。
        :type HostName: str
        :param HostNameStyle: 雲伺服器主機名的風格，取值範圍包括 ORIGINAL 和  UNIQUE，預設爲 ORIGINAL。
<br><li> ORIGINAL，AS 直接将入參中所填的 HostName 傳遞給 CVM，CVM 可能會對 HostName 追加序列號，伸縮組中實例的 HostName 會出現沖突的情況。
<br><li> UNIQUE，入參所填的 HostName 相當於主機名前綴，AS 和 CVM 會對其進行拓展，伸縮組中實例的 HostName 可以保證唯一。
注意：此欄位可能返回 null，表示取不到有效值。
        :type HostNameStyle: str
        """
        self.HostName = None
        self.HostNameStyle = None


    def _deserialize(self, params):
        self.HostName = params.get("HostName")
        self.HostNameStyle = params.get("HostNameStyle")


class Instance(AbstractModel):
    """實例訊息

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param AutoScalingGroupId: 伸縮組ID
        :type AutoScalingGroupId: str
        :param LaunchConfigurationId: 啓動配置ID
        :type LaunchConfigurationId: str
        :param LaunchConfigurationName: 啓動配置名稱
        :type LaunchConfigurationName: str
        :param LifeCycleState: 生命週期狀态，取值如下：<br>
<li>IN_SERVICE：運作中
<li>CREATING：創建中
<li>CREATION_FAILED：創建失敗
<li>TERMINATING：中止中
<li>TERMINATION_FAILED：中止失敗
<li>ATTACHING：綁定中
<li>DETACHING：解綁中
<li>ATTACHING_LB：綁定LB中<li>DETACHING_LB：解綁LB中
<li>STARTING：開機中
<li>START_FAILED：開機失敗
<li>STOPPING：關機中
<li>STOP_FAILED：關機失敗
<li>STOPPED：已關機
        :type LifeCycleState: str
        :param HealthStatus: 健康狀态，取值包括HEALTHY和UNHEALTHY
        :type HealthStatus: str
        :param ProtectedFromScaleIn: 是否加入縮容保護
        :type ProtectedFromScaleIn: bool
        :param Zone: 可用區
        :type Zone: str
        :param CreationType: 創建類型，取值包括AUTO_CREATION, MANUAL_ATTACHING。
        :type CreationType: str
        :param AddTime: 實例加入時間
        :type AddTime: str
        :param InstanceType: 實例類型
        :type InstanceType: str
        :param VersionNumber: 版本號
        :type VersionNumber: int
        :param AutoScalingGroupName: 伸縮組名稱
        :type AutoScalingGroupName: str
        """
        self.InstanceId = None
        self.AutoScalingGroupId = None
        self.LaunchConfigurationId = None
        self.LaunchConfigurationName = None
        self.LifeCycleState = None
        self.HealthStatus = None
        self.ProtectedFromScaleIn = None
        self.Zone = None
        self.CreationType = None
        self.AddTime = None
        self.InstanceType = None
        self.VersionNumber = None
        self.AutoScalingGroupName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.LaunchConfigurationName = params.get("LaunchConfigurationName")
        self.LifeCycleState = params.get("LifeCycleState")
        self.HealthStatus = params.get("HealthStatus")
        self.ProtectedFromScaleIn = params.get("ProtectedFromScaleIn")
        self.Zone = params.get("Zone")
        self.CreationType = params.get("CreationType")
        self.AddTime = params.get("AddTime")
        self.InstanceType = params.get("InstanceType")
        self.VersionNumber = params.get("VersionNumber")
        self.AutoScalingGroupName = params.get("AutoScalingGroupName")


class InstanceChargePrepaid(AbstractModel):
    """描述了實例的計費模式

    """

    def __init__(self):
        """
        :param Period: 購買實例的時長，單位：月。取值範圍：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36。
        :type Period: int
        :param RenewFlag: 自動續約標識。取值範圍：<br><li>NOTIFY_AND_AUTO_RENEW：通知過期且自動續約<br><li>NOTIFY_AND_MANUAL_RENEW：通知過期不自動續約<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知過期不自動續約<br><br>預設取值：NOTIFY_AND_MANUAL_RENEW。若該參數指定爲NOTIFY_AND_AUTO_RENEW，在帳戶餘額充足的情況下，實例到期後将按月自動續約。
        :type RenewFlag: str
        """
        self.Period = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RenewFlag = params.get("RenewFlag")


class InstanceMarketOptionsRequest(AbstractModel):
    """CVM競價請求相關選項

    """

    def __init__(self):
        """
        :param SpotOptions: 競價相關選項
        :type SpotOptions: :class:`taifucloudcloud.autoscaling.v20180419.models.SpotMarketOptions`
        :param MarketType: 市場選項類型，當前只支援取值：spot
注意：此欄位可能返回 null，表示取不到有效值。
        :type MarketType: str
        """
        self.SpotOptions = None
        self.MarketType = None


    def _deserialize(self, params):
        if params.get("SpotOptions") is not None:
            self.SpotOptions = SpotMarketOptions()
            self.SpotOptions._deserialize(params.get("SpotOptions"))
        self.MarketType = params.get("MarketType")


class InstanceNameSettings(AbstractModel):
    """雲伺服器實例名稱（InstanceName）的相關設置

    """

    def __init__(self):
        """
        :param InstanceName: 雲伺服器的實例名。

點號（.）和短橫線（-）不能作爲 InstanceName 的首尾字元，不能連續使用。

其他類型（Linux 等）實例：字元長度爲[2, 40]，允許支援多個點號，點之間爲一段，每段允許字母（不限制大小寫）、數字和短橫線（-）組成。
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param InstanceNameStyle: 雲伺服器實例名的風格，取值範圍包括 ORIGINAL 和 UNIQUE，預設爲 ORIGINAL。

ORIGINAL，AS 直接将入參中所填的 InstanceName 傳遞給 CVM，CVM 可能會對 InstanceName 追加序列號，伸縮組中實例的 InstanceName 會出現沖突的情況。

UNIQUE，入參所填的 InstanceName 相當於實例名前綴，AS 和 CVM 會對其進行拓展，伸縮組中實例的 InstanceName 可以保證唯一。
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceNameStyle: str
        """
        self.InstanceName = None
        self.InstanceNameStyle = None


    def _deserialize(self, params):
        self.InstanceName = params.get("InstanceName")
        self.InstanceNameStyle = params.get("InstanceNameStyle")


class InstanceTag(AbstractModel):
    """實例標簽。通過指定該參數，可以爲擴容的實例綁定標簽。

    """

    def __init__(self):
        """
        :param Key: 標簽鍵
        :type Key: str
        :param Value: 標簽值
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class InternetAccessible(AbstractModel):
    """描述了啓動配置創建實例的公網可訪問性，聲明了實例的公網使用計費模式，最大頻寬等

    """

    def __init__(self):
        """
        :param InternetChargeType: 網絡計費類型。取值範圍：<br><li>BANDWIDTH_PREPAID：預付費按頻寬結算<br><li>TRAFFIC_POSTPAID_BY_HOUR：流量按小時後付費<br><li>BANDWIDTH_POSTPAID_BY_HOUR：頻寬按小時後付費<br><li>BANDWIDTH_PACKAGE：頻寬包用戶<br>預設取值：TRAFFIC_POSTPAID_BY_HOUR。
注意：此欄位可能返回 null，表示取不到有效值。
        :type InternetChargeType: str
        :param InternetMaxBandwidthOut: 公網出頻寬上限，單位：Mbps。預設值：0Mbps。不同機型頻寬上限範圍不一緻，具體限制詳見[購買網絡頻寬](https://cloud.taifucloud.com/document/product/213/509)。
注意：此欄位可能返回 null，表示取不到有效值。
        :type InternetMaxBandwidthOut: int
        :param PublicIpAssigned: 是否分配公網IP。取值範圍：<br><li>TRUE：表示分配公網IP<br><li>FALSE：表示不分配公網IP<br><br>當公網頻寬大於0Mbps時，可自由選擇開通與否，預設開通公網IP；當公網頻寬爲0，則不允許分配公網IP。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PublicIpAssigned: bool
        """
        self.InternetChargeType = None
        self.InternetMaxBandwidthOut = None
        self.PublicIpAssigned = None


    def _deserialize(self, params):
        self.InternetChargeType = params.get("InternetChargeType")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.PublicIpAssigned = params.get("PublicIpAssigned")


class LaunchConfiguration(AbstractModel):
    """符合條件的啓動配置訊息的集合。

    """

    def __init__(self):
        """
        :param ProjectId: 實例所屬項目ID。
        :type ProjectId: int
        :param LaunchConfigurationId: 啓動配置ID。
        :type LaunchConfigurationId: str
        :param LaunchConfigurationName: 啓動配置名稱。
        :type LaunchConfigurationName: str
        :param InstanceType: 實例機型。
        :type InstanceType: str
        :param SystemDisk: 實例系統盤配置訊息。
        :type SystemDisk: :class:`taifucloudcloud.autoscaling.v20180419.models.SystemDisk`
        :param DataDisks: 實例數據盤配置訊息。
        :type DataDisks: list of DataDisk
        :param LoginSettings: 實例登入設置。
        :type LoginSettings: :class:`taifucloudcloud.autoscaling.v20180419.models.LimitedLoginSettings`
        :param InternetAccessible: 公網頻寬相關訊息設置。
        :type InternetAccessible: :class:`taifucloudcloud.autoscaling.v20180419.models.InternetAccessible`
        :param SecurityGroupIds: 實例所屬安全組。
        :type SecurityGroupIds: list of str
        :param AutoScalingGroupAbstractSet: 啓動配置關聯的伸縮組。
        :type AutoScalingGroupAbstractSet: list of AutoScalingGroupAbstract
        :param UserData: 自定義數據。
注意：此欄位可能返回 null，表示取不到有效值。
        :type UserData: str
        :param CreatedTime: 啓動配置創建時間。
        :type CreatedTime: str
        :param EnhancedService: 實例的增強服務啓用情況與其設置。
        :type EnhancedService: :class:`taifucloudcloud.autoscaling.v20180419.models.EnhancedService`
        :param ImageId: 映像ID。
        :type ImageId: str
        :param LaunchConfigurationStatus: 啓動配置當前狀态。取值範圍：<br><li>NORMAL：正常<br><li>IMAGE_ABNORMAL：啓動配置映像異常<br><li>CBS_SNAP_ABNORMAL：啓動配置數據盤快照異常<br><li>SECURITY_GROUP_ABNORMAL：啓動配置安全組異常<br>
        :type LaunchConfigurationStatus: str
        :param InstanceChargeType: 實例計費類型，CVM預設值按照POSTPAID_BY_HOUR處理。
<br><li>POSTPAID_BY_HOUR：按小時後付費
<br><li>SPOTPAID：競價付費
        :type InstanceChargeType: str
        :param InstanceMarketOptions: 實例的市場相關選項，如競價實例相關參數，若指定實例的付費模式爲競價付費則該參數必傳。
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceMarketOptions: :class:`taifucloudcloud.autoscaling.v20180419.models.InstanceMarketOptionsRequest`
        :param InstanceTypes: 實例機型清單。
        :type InstanceTypes: list of str
        :param InstanceTags: 標簽清單。
        :type InstanceTags: list of InstanceTag
        :param VersionNumber: 版本號。
        :type VersionNumber: int
        :param UpdatedTime: 更新時間。
        :type UpdatedTime: str
        :param CamRoleName: CAM角色名稱。可通過DescribeRoleList介面返回值中的roleName獲取。
        :type CamRoleName: str
        :param LastOperationInstanceTypesCheckPolicy: 上次操作時，InstanceTypesCheckPolicy 取值。
        :type LastOperationInstanceTypesCheckPolicy: str
        :param HostNameSettings: 雲伺服器主機名（HostName）的相關設置。
        :type HostNameSettings: :class:`taifucloudcloud.autoscaling.v20180419.models.HostNameSettings`
        :param InstanceNameSettings: 雲伺服器實例名（InstanceName）的相關設置。
        :type InstanceNameSettings: :class:`taifucloudcloud.autoscaling.v20180419.models.InstanceNameSettings`
        :param InstanceChargePrepaid: 預付費模式，即包年包月相關參數設置。通過該參數可以指定包年包月實例的購買時長、是否設置自動續約等屬性。若指定實例的付費模式爲預付費則該參數必傳。
        :type InstanceChargePrepaid: :class:`taifucloudcloud.autoscaling.v20180419.models.InstanceChargePrepaid`
        """
        self.ProjectId = None
        self.LaunchConfigurationId = None
        self.LaunchConfigurationName = None
        self.InstanceType = None
        self.SystemDisk = None
        self.DataDisks = None
        self.LoginSettings = None
        self.InternetAccessible = None
        self.SecurityGroupIds = None
        self.AutoScalingGroupAbstractSet = None
        self.UserData = None
        self.CreatedTime = None
        self.EnhancedService = None
        self.ImageId = None
        self.LaunchConfigurationStatus = None
        self.InstanceChargeType = None
        self.InstanceMarketOptions = None
        self.InstanceTypes = None
        self.InstanceTags = None
        self.VersionNumber = None
        self.UpdatedTime = None
        self.CamRoleName = None
        self.LastOperationInstanceTypesCheckPolicy = None
        self.HostNameSettings = None
        self.InstanceNameSettings = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.LaunchConfigurationName = params.get("LaunchConfigurationName")
        self.InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LimitedLoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("AutoScalingGroupAbstractSet") is not None:
            self.AutoScalingGroupAbstractSet = []
            for item in params.get("AutoScalingGroupAbstractSet"):
                obj = AutoScalingGroupAbstract()
                obj._deserialize(item)
                self.AutoScalingGroupAbstractSet.append(obj)
        self.UserData = params.get("UserData")
        self.CreatedTime = params.get("CreatedTime")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.ImageId = params.get("ImageId")
        self.LaunchConfigurationStatus = params.get("LaunchConfigurationStatus")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceMarketOptions") is not None:
            self.InstanceMarketOptions = InstanceMarketOptionsRequest()
            self.InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self.InstanceTypes = params.get("InstanceTypes")
        if params.get("InstanceTags") is not None:
            self.InstanceTags = []
            for item in params.get("InstanceTags"):
                obj = InstanceTag()
                obj._deserialize(item)
                self.InstanceTags.append(obj)
        self.VersionNumber = params.get("VersionNumber")
        self.UpdatedTime = params.get("UpdatedTime")
        self.CamRoleName = params.get("CamRoleName")
        self.LastOperationInstanceTypesCheckPolicy = params.get("LastOperationInstanceTypesCheckPolicy")
        if params.get("HostNameSettings") is not None:
            self.HostNameSettings = HostNameSettings()
            self.HostNameSettings._deserialize(params.get("HostNameSettings"))
        if params.get("InstanceNameSettings") is not None:
            self.InstanceNameSettings = InstanceNameSettings()
            self.InstanceNameSettings._deserialize(params.get("InstanceNameSettings"))
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))


class LifecycleActionResultInfo(AbstractModel):
    """生命週期挂鈎動作的執行結果訊息。

    """

    def __init__(self):
        """
        :param LifecycleHookId: 生命週期挂鈎標識。
        :type LifecycleHookId: str
        :param InstanceId: 實例標識。
        :type InstanceId: str
        :param NotificationResult: 通知的結果，表示通知CMQ是否成功。
        :type NotificationResult: str
        :param LifecycleActionResult: 生命週期挂鈎動作的執行結果，取值包括 CONTINUE、ABANDON。
        :type LifecycleActionResult: str
        :param ResultReason: 結果的原因。
        :type ResultReason: str
        """
        self.LifecycleHookId = None
        self.InstanceId = None
        self.NotificationResult = None
        self.LifecycleActionResult = None
        self.ResultReason = None


    def _deserialize(self, params):
        self.LifecycleHookId = params.get("LifecycleHookId")
        self.InstanceId = params.get("InstanceId")
        self.NotificationResult = params.get("NotificationResult")
        self.LifecycleActionResult = params.get("LifecycleActionResult")
        self.ResultReason = params.get("ResultReason")


class LifecycleHook(AbstractModel):
    """生命週期挂鈎

    """

    def __init__(self):
        """
        :param LifecycleHookId: 生命週期挂鈎ID
        :type LifecycleHookId: str
        :param LifecycleHookName: 生命週期挂鈎名稱
        :type LifecycleHookName: str
        :param AutoScalingGroupId: 伸縮組ID
        :type AutoScalingGroupId: str
        :param DefaultResult: 生命週期挂鈎預設結果
        :type DefaultResult: str
        :param HeartbeatTimeout: 生命週期挂鈎等待超時時間
        :type HeartbeatTimeout: int
        :param LifecycleTransition: 生命週期挂鈎适用場景
        :type LifecycleTransition: str
        :param NotificationMetadata: 通知目標的附加訊息
        :type NotificationMetadata: str
        :param CreatedTime: 創建時間
        :type CreatedTime: str
        :param NotificationTarget: 通知目標
        :type NotificationTarget: :class:`taifucloudcloud.autoscaling.v20180419.models.NotificationTarget`
        :param LifecycleTransitionType: 生命週期挂鈎适用場景
        :type LifecycleTransitionType: str
        """
        self.LifecycleHookId = None
        self.LifecycleHookName = None
        self.AutoScalingGroupId = None
        self.DefaultResult = None
        self.HeartbeatTimeout = None
        self.LifecycleTransition = None
        self.NotificationMetadata = None
        self.CreatedTime = None
        self.NotificationTarget = None
        self.LifecycleTransitionType = None


    def _deserialize(self, params):
        self.LifecycleHookId = params.get("LifecycleHookId")
        self.LifecycleHookName = params.get("LifecycleHookName")
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.DefaultResult = params.get("DefaultResult")
        self.HeartbeatTimeout = params.get("HeartbeatTimeout")
        self.LifecycleTransition = params.get("LifecycleTransition")
        self.NotificationMetadata = params.get("NotificationMetadata")
        self.CreatedTime = params.get("CreatedTime")
        if params.get("NotificationTarget") is not None:
            self.NotificationTarget = NotificationTarget()
            self.NotificationTarget._deserialize(params.get("NotificationTarget"))
        self.LifecycleTransitionType = params.get("LifecycleTransitionType")


class LimitedLoginSettings(AbstractModel):
    """描述了實例登入相關配置與訊息，出於安全性考慮，不會描述敏感訊息。

    """

    def __init__(self):
        """
        :param KeyIds: 金鑰ID清單。
        :type KeyIds: list of str
        """
        self.KeyIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")


class LoginSettings(AbstractModel):
    """描述了實例登入相關配置與訊息。

    """

    def __init__(self):
        """
        :param Password: 實例登入密碼。不同作業系統類型密碼複雜度限制不一樣，具體如下：<br><li>Linux實例密碼必須8到16位，至少包括兩項[a-z，A-Z]、[0-9] 和 [( ) ` ~ ! @ # $ % ^ & * - + = | { } [ ] : ; ' , . ? / ]中的特殊符號。<br><li>Windows實例密碼必須12到16位，至少包括三項[a-z]，[A-Z]，[0-9] 和 [( ) ` ~ ! @ # $ % ^ & * - + = { } [ ] : ; ' , . ? /]中的特殊符號。<br><br>若不指定該參數，則由系統随機生成密碼，並通過站内信方式通知到用戶。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Password: str
        :param KeyIds: 金鑰ID清單。關聯金鑰後，就可以通過對應的私鑰來訪問實例；KeyId可通過介面DescribeKeyPairs獲取，金鑰與密碼不能同時指定，同時Windows作業系統不支援指定金鑰。當前僅支援購買的時候指定一個金鑰。
        :type KeyIds: list of str
        :param KeepImageLogin: 保持映像的原始設置。該參數與Password或KeyIds.N不能同時指定。只有使用自定義映像、共享映像或外部導入映像創建實例時才能指定該參數爲TRUE。取值範圍：<br><li>TRUE：表示保持映像的登入設置<br><li>FALSE：表示不保持映像的登入設置<br><br>預設取值：FALSE。
注意：此欄位可能返回 null，表示取不到有效值。
        :type KeepImageLogin: bool
        """
        self.Password = None
        self.KeyIds = None
        self.KeepImageLogin = None


    def _deserialize(self, params):
        self.Password = params.get("Password")
        self.KeyIds = params.get("KeyIds")
        self.KeepImageLogin = params.get("KeepImageLogin")


class MetricAlarm(AbstractModel):
    """彈性伸縮告警指標

    """

    def __init__(self):
        """
        :param ComparisonOperator: 比較運算符，可選值：<br><li>GREATER_THAN：大於</li><li>GREATER_THAN_OR_EQUAL_TO：大於或等於</li><li>LESS_THAN：小於</li><li> LESS_THAN_OR_EQUAL_TO：小於或等於</li><li> EQUAL_TO：等於</li> <li>NOT_EQUAL_TO：不等於</li>
        :type ComparisonOperator: str
        :param MetricName: 指標名稱，可選欄位如下：<br><li>CPU_UTILIZATION：CPU使用率</li><li>MEM_UTILIZATION：内存使用率</li><li>LAN_TRAFFIC_OUT：内網出頻寬</li><li>LAN_TRAFFIC_IN：内網入頻寬</li><li>WAN_TRAFFIC_OUT：外網出頻寬</li><li>WAN_TRAFFIC_IN：外網入頻寬</li>
        :type MetricName: str
        :param Threshold: 告警阈值：<br><li>CPU_UTILIZATION：[1, 100]，單位：%</li><li>MEM_UTILIZATION：[1, 100]，單位：%</li><li>LAN_TRAFFIC_OUT：>0，單位：Mbps </li><li>LAN_TRAFFIC_IN：>0，單位：Mbps</li><li>WAN_TRAFFIC_OUT：>0，單位：Mbps</li><li>WAN_TRAFFIC_IN：>0，單位：Mbps</li>
        :type Threshold: int
        :param Period: 時間週期，單位：秒，取值列舉值爲60、300。
        :type Period: int
        :param ContinuousTime: 重複次數。取值範圍 [1, 10]
        :type ContinuousTime: int
        :param Statistic: 統計類型，可選欄位如下：<br><li>AVERAGE：平均值</li><li>MAXIMUM：最大值<li>MINIMUM：最小值</li><br> 預設取值：AVERAGE
        :type Statistic: str
        """
        self.ComparisonOperator = None
        self.MetricName = None
        self.Threshold = None
        self.Period = None
        self.ContinuousTime = None
        self.Statistic = None


    def _deserialize(self, params):
        self.ComparisonOperator = params.get("ComparisonOperator")
        self.MetricName = params.get("MetricName")
        self.Threshold = params.get("Threshold")
        self.Period = params.get("Period")
        self.ContinuousTime = params.get("ContinuousTime")
        self.Statistic = params.get("Statistic")


class ModifyAutoScalingGroupRequest(AbstractModel):
    """ModifyAutoScalingGroup請求參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸縮組ID
        :type AutoScalingGroupId: str
        :param AutoScalingGroupName: 伸縮組名稱，在您賬號中必須唯一。名稱僅支援中文、英文、數字、下劃線、分隔符"-"、小數點，最大長度不能超55個位元。
        :type AutoScalingGroupName: str
        :param DefaultCooldown: 預設冷卻時間，單位秒，預設值爲300
        :type DefaultCooldown: int
        :param DesiredCapacity: 期望實例數，大小介於最小實例數和最大實例數之間
        :type DesiredCapacity: int
        :param LaunchConfigurationId: 啓動配置ID
        :type LaunchConfigurationId: str
        :param MaxSize: 最大實例數，取值範圍爲0-2000。
        :type MaxSize: int
        :param MinSize: 最小實例數，取值範圍爲0-2000。
        :type MinSize: int
        :param ProjectId: 項目ID
        :type ProjectId: int
        :param SubnetIds: 子網ID清單
        :type SubnetIds: list of str
        :param TerminationPolicies: 銷毀策略，目前長度上限爲1。取值包括 OLDEST_INSTANCE 和 NEWEST_INSTANCE。
<br><li> OLDEST_INSTANCE 優先銷毀伸縮組中最舊的實例。
<br><li> NEWEST_INSTANCE，優先銷毀伸縮組中最新的實例。
        :type TerminationPolicies: list of str
        :param VpcId: VPC ID，基礎網絡則填空字串。修改爲具體VPC ID時，需指定相應的SubnetIds；修改爲基礎網絡時，需指定相應的Zones。
        :type VpcId: str
        :param Zones: 可用區清單
        :type Zones: list of str
        :param RetryPolicy: 重試策略，取值包括 IMMEDIATE_RETRY、 INCREMENTAL_INTERVALS、NO_RETRY，預設取值爲 IMMEDIATE_RETRY。
<br><li> IMMEDIATE_RETRY，立即重試，在較短時間内快速重試，連續失敗超過一定次數（5次）後不再重試。
<br><li> INCREMENTAL_INTERVALS，間隔遞增重試，随着連續失敗次數的增加，重試間隔逐漸增大，重試間隔從秒級到1天不等。
<br><li> NO_RETRY，不進行重試，直到再次收到用戶調用或者告警訊息後才會重試。
        :type RetryPolicy: str
        :param ZonesCheckPolicy: 可用區校驗策略，取值包括 ALL 和 ANY，預設取值爲ANY。在伸縮組實際變更資源相關欄位時（啓動配置、可用區、子網）發揮作用。
<br><li> ALL，所有可用區（Zone）或子網（SubnetId）都可用則通過校驗，否則校驗報錯。
<br><li> ANY，存在任何一個可用區（Zone）或子網（SubnetId）可用則通過校驗，否則校驗報錯。

可用區或子網不可用的常見原因包括該可用區CVM實例類型售罄、該可用區CBS雲盤售罄、該可用區配額不足、該子網IP不足等。
如果 Zones/SubnetIds 中可用區或者子網不存在，則無論 ZonesCheckPolicy 采用何種取值，都會校驗報錯。
        :type ZonesCheckPolicy: str
        :param ServiceSettings: 服務設置，包括雲監控不健康替換等服務設置。
        :type ServiceSettings: :class:`taifucloudcloud.autoscaling.v20180419.models.ServiceSettings`
        :param Ipv6AddressCount: 實例具有IPv6網址數量的配置，取值包括0、1。
        :type Ipv6AddressCount: int
        :param MultiZoneSubnetPolicy: 多可用區/子網策略，取值包括 PRIORITY 和 EQUALITY。
<br><li> PRIORITY，按照可用區/子網清單的順序，作爲優先級來嘗試創建實例，如果優先級最高的可用區/子網可以創建成功，則總在該可用區/子網創建。
<br><li> EQUALITY：每次選擇當前實例數最少的可用區/子網進行擴容，使得每個可用區/子網都有機會發生擴容，多次擴容出的實例會打散到多個可用區/子網。

與本策略相關的注意點：
<br><li> 當伸縮組爲基礎網絡時，本策略适用於多可用區；當伸縮組爲VPC網絡時，本策略适用於多子網，此時不再考慮可用區因素，例如四個子網ABCD，其中ABC處於可用區1，D處於可用區2，此時考慮子網ABCD進行排序，而不考慮可用區1、2。
<br><li> 本策略适用於多可用區/子網，不适用於啓動配置的多機型。多機型按照優先級策略進行選擇。
<br><li> 創建實例時，先保證多機型的策略，後保證多可用區/子網的策略。例如多機型A、B，多子網1、2、3（按照PRIORITY策略），會按照A1、A2、A3、B1、B2、B3 進行嘗試，如果A1售罄，會嘗試A2（而非B1）。
<br><li> 無論使用哪種策略，單次伸縮活動總是優先保持使用一種具體配置（機型 * 可用區/子網）。
        :type MultiZoneSubnetPolicy: str
        """
        self.AutoScalingGroupId = None
        self.AutoScalingGroupName = None
        self.DefaultCooldown = None
        self.DesiredCapacity = None
        self.LaunchConfigurationId = None
        self.MaxSize = None
        self.MinSize = None
        self.ProjectId = None
        self.SubnetIds = None
        self.TerminationPolicies = None
        self.VpcId = None
        self.Zones = None
        self.RetryPolicy = None
        self.ZonesCheckPolicy = None
        self.ServiceSettings = None
        self.Ipv6AddressCount = None
        self.MultiZoneSubnetPolicy = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.AutoScalingGroupName = params.get("AutoScalingGroupName")
        self.DefaultCooldown = params.get("DefaultCooldown")
        self.DesiredCapacity = params.get("DesiredCapacity")
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.MaxSize = params.get("MaxSize")
        self.MinSize = params.get("MinSize")
        self.ProjectId = params.get("ProjectId")
        self.SubnetIds = params.get("SubnetIds")
        self.TerminationPolicies = params.get("TerminationPolicies")
        self.VpcId = params.get("VpcId")
        self.Zones = params.get("Zones")
        self.RetryPolicy = params.get("RetryPolicy")
        self.ZonesCheckPolicy = params.get("ZonesCheckPolicy")
        if params.get("ServiceSettings") is not None:
            self.ServiceSettings = ServiceSettings()
            self.ServiceSettings._deserialize(params.get("ServiceSettings"))
        self.Ipv6AddressCount = params.get("Ipv6AddressCount")
        self.MultiZoneSubnetPolicy = params.get("MultiZoneSubnetPolicy")


class ModifyAutoScalingGroupResponse(AbstractModel):
    """ModifyAutoScalingGroup返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDesiredCapacityRequest(AbstractModel):
    """ModifyDesiredCapacity請求參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸縮組ID
        :type AutoScalingGroupId: str
        :param DesiredCapacity: 期望實例數
        :type DesiredCapacity: int
        """
        self.AutoScalingGroupId = None
        self.DesiredCapacity = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.DesiredCapacity = params.get("DesiredCapacity")


class ModifyDesiredCapacityResponse(AbstractModel):
    """ModifyDesiredCapacity返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLaunchConfigurationAttributesRequest(AbstractModel):
    """ModifyLaunchConfigurationAttributes請求參數結構體

    """

    def __init__(self):
        """
        :param LaunchConfigurationId: 啓動配置ID
        :type LaunchConfigurationId: str
        :param ImageId: 指定有效的[映像](https://cloud.taifucloud.com/document/product/213/4940)ID，格式形如`img-8toqc6s3`。映像類型分爲四種：<br/><li>公共映像</li><li>自定義映像</li><li>共享映像</li><li>服務市場映像</li><br/>可通過以下方式獲取可用的映像ID：<br/><li>`公共映像`、`自定義映像`、`共享映像`的映像ID可通過登入[控制台](https://console.cloud.taifucloud.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查詢；`服務映像市場`的映像ID可通過[雲市場](https://market.cloud.taifucloud.com/list)查詢。</li><li>通過調用介面 [DescribeImages](https://cloud.taifucloud.com/document/api/213/15715) ，取返回訊息中的`ImageId`欄位。</li>
        :type ImageId: str
        :param InstanceTypes: 實例類型清單，不同實例機型指定了不同的資源規格，最多支援5種實例機型。
啓動配置，通過 InstanceType 表示單一實例類型，通過 InstanceTypes 表示多實例類型。指定 InstanceTypes 成功啓動配置後，原有的 InstanceType 自動失效。
        :type InstanceTypes: list of str
        :param InstanceTypesCheckPolicy: 實例類型校驗策略，在實際修改 InstanceTypes 時發揮作用，取值包括 ALL 和 ANY，預設取值爲ANY。
<br><li> ALL，所有實例類型（InstanceType）都可用則通過校驗，否則校驗報錯。
<br><li> ANY，存在任何一個實例類型（InstanceType）可用則通過校驗，否則校驗報錯。

實例類型不可用的常見原因包括該實例類型售罄、對應雲盤售罄等。
如果 InstanceTypes 中一款機型不存在或者已下線，則無論 InstanceTypesCheckPolicy 采用何種取值，都會校驗報錯。
        :type InstanceTypesCheckPolicy: str
        :param LaunchConfigurationName: 啓動配置顯示名稱。名稱僅支援中文、英文、數字、下劃線、分隔符"-"、小數點，最大長度不能超60個位元。
        :type LaunchConfigurationName: str
        :param UserData: 經過 Base64 編碼後的自定義數據，最大長度不超過16KB。如果要清空UserData，則指定其爲空字串
        :type UserData: str
        """
        self.LaunchConfigurationId = None
        self.ImageId = None
        self.InstanceTypes = None
        self.InstanceTypesCheckPolicy = None
        self.LaunchConfigurationName = None
        self.UserData = None


    def _deserialize(self, params):
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.ImageId = params.get("ImageId")
        self.InstanceTypes = params.get("InstanceTypes")
        self.InstanceTypesCheckPolicy = params.get("InstanceTypesCheckPolicy")
        self.LaunchConfigurationName = params.get("LaunchConfigurationName")
        self.UserData = params.get("UserData")


class ModifyLaunchConfigurationAttributesResponse(AbstractModel):
    """ModifyLaunchConfigurationAttributes返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLoadBalancersRequest(AbstractModel):
    """ModifyLoadBalancers請求參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸縮組ID
        :type AutoScalingGroupId: str
        :param LoadBalancerIds: 傳統負載均衡器ID清單，目前長度上限爲20，LoadBalancerIds 和 ForwardLoadBalancers 二者同時最多只能指定一個
        :type LoadBalancerIds: list of str
        :param ForwardLoadBalancers: 應用型負載均衡器清單，目前長度上限爲20，LoadBalancerIds 和 ForwardLoadBalancers 二者同時最多只能指定一個
        :type ForwardLoadBalancers: list of ForwardLoadBalancer
        :param LoadBalancersCheckPolicy: 負載均衡器校驗策略，取值包括 ALL 和 DIFF，預設取值爲 ALL。
<br><li> ALL，所有負載均衡器都合法則通過校驗，否則校驗報錯。
<br><li> DIFF，僅校驗負載均衡器參數中實際變化的部分，如果合法則通過校驗，否則校驗報錯。
        :type LoadBalancersCheckPolicy: str
        """
        self.AutoScalingGroupId = None
        self.LoadBalancerIds = None
        self.ForwardLoadBalancers = None
        self.LoadBalancersCheckPolicy = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        if params.get("ForwardLoadBalancers") is not None:
            self.ForwardLoadBalancers = []
            for item in params.get("ForwardLoadBalancers"):
                obj = ForwardLoadBalancer()
                obj._deserialize(item)
                self.ForwardLoadBalancers.append(obj)
        self.LoadBalancersCheckPolicy = params.get("LoadBalancersCheckPolicy")


class ModifyLoadBalancersResponse(AbstractModel):
    """ModifyLoadBalancers返回參數結構體

    """

    def __init__(self):
        """
        :param ActivityId: 伸縮活動ID
        :type ActivityId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ActivityId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ActivityId = params.get("ActivityId")
        self.RequestId = params.get("RequestId")


class ModifyNotificationConfigurationRequest(AbstractModel):
    """ModifyNotificationConfiguration請求參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingNotificationId: 待修改的通知ID。
        :type AutoScalingNotificationId: str
        :param NotificationTypes: 通知類型，即爲需要訂閱的通知類型集合，取值範圍如下：
<li>SCALE_OUT_SUCCESSFUL：擴容成功</li>
<li>SCALE_OUT_FAILED：擴容失敗</li>
<li>SCALE_IN_SUCCESSFUL：縮容成功</li>
<li>SCALE_IN_FAILED：縮容失敗</li>
<li>REPLACE_UNHEALTHY_INSTANCE_SUCCESSFUL：替換不健康子機成功</li>
<li>REPLACE_UNHEALTHY_INSTANCE_FAILED：替換不健康子機失敗</li>
        :type NotificationTypes: list of str
        :param NotificationUserGroupIds: 通知組ID，即爲用戶組ID集合，用戶組ID可以通過[ListGroups](https://cloud.taifucloud.com/document/product/598/34589)查詢。
        :type NotificationUserGroupIds: list of str
        """
        self.AutoScalingNotificationId = None
        self.NotificationTypes = None
        self.NotificationUserGroupIds = None


    def _deserialize(self, params):
        self.AutoScalingNotificationId = params.get("AutoScalingNotificationId")
        self.NotificationTypes = params.get("NotificationTypes")
        self.NotificationUserGroupIds = params.get("NotificationUserGroupIds")


class ModifyNotificationConfigurationResponse(AbstractModel):
    """ModifyNotificationConfiguration返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyScalingPolicyRequest(AbstractModel):
    """ModifyScalingPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingPolicyId: 告警策略ID。
        :type AutoScalingPolicyId: str
        :param ScalingPolicyName: 告警策略名稱。
        :type ScalingPolicyName: str
        :param AdjustmentType: 告警觸發後，期望實例數修改方式。取值 ：<br><li>CHANGE_IN_CAPACITY：增加或減少若幹期望實例數</li><li>EXACT_CAPACITY：調整至指定期望實例數</li> <li>PERCENT_CHANGE_IN_CAPACITY：按百分比調整期望實例數</li>
        :type AdjustmentType: str
        :param AdjustmentValue: 告警觸發後，期望實例數的調整值。取值：<br><li>當 AdjustmentType 爲 CHANGE_IN_CAPACITY 時，AdjustmentValue 爲正數表示告警觸發後增加實例，爲負數表示告警觸發後減少實例 </li> <li> 當 AdjustmentType 爲 EXACT_CAPACITY 時，AdjustmentValue 的值即爲告警觸發後新的期望實例數，需要大於或等於0 </li> <li> 當 AdjustmentType 爲 PERCENT_CHANGE_IN_CAPACITY 時，AdjusmentValue 爲正數表示告警觸發後按百分比增加實例，爲負數表示告警觸發後按百分比減少實例，單位是：%。
        :type AdjustmentValue: int
        :param Cooldown: 冷卻時間，單位爲秒。
        :type Cooldown: int
        :param MetricAlarm: 告警監控指標。
        :type MetricAlarm: :class:`taifucloudcloud.autoscaling.v20180419.models.MetricAlarm`
        :param NotificationUserGroupIds: 通知組ID，即爲用戶組ID集合，用戶組ID可以通過[ListGroups](https://cloud.taifucloud.com/document/product/598/34589)查詢。
如果需要清空通知用戶組，需要在清單中傳入特定字串 "NULL"。
        :type NotificationUserGroupIds: list of str
        """
        self.AutoScalingPolicyId = None
        self.ScalingPolicyName = None
        self.AdjustmentType = None
        self.AdjustmentValue = None
        self.Cooldown = None
        self.MetricAlarm = None
        self.NotificationUserGroupIds = None


    def _deserialize(self, params):
        self.AutoScalingPolicyId = params.get("AutoScalingPolicyId")
        self.ScalingPolicyName = params.get("ScalingPolicyName")
        self.AdjustmentType = params.get("AdjustmentType")
        self.AdjustmentValue = params.get("AdjustmentValue")
        self.Cooldown = params.get("Cooldown")
        if params.get("MetricAlarm") is not None:
            self.MetricAlarm = MetricAlarm()
            self.MetricAlarm._deserialize(params.get("MetricAlarm"))
        self.NotificationUserGroupIds = params.get("NotificationUserGroupIds")


class ModifyScalingPolicyResponse(AbstractModel):
    """ModifyScalingPolicy返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyScheduledActionRequest(AbstractModel):
    """ModifyScheduledAction請求參數結構體

    """

    def __init__(self):
        """
        :param ScheduledActionId: 待修改的定時任務ID
        :type ScheduledActionId: str
        :param ScheduledActionName: 定時任務名稱。名稱僅支援中文、英文、數字、下劃線、分隔符"-"、小數點，最大長度不能超60個位元。同一伸縮組下必須唯一。
        :type ScheduledActionName: str
        :param MaxSize: 當定時任務觸發時，設置的伸縮組最大實例數。
        :type MaxSize: int
        :param MinSize: 當定時任務觸發時，設置的伸縮組最小實例數。
        :type MinSize: int
        :param DesiredCapacity: 當定時任務觸發時，設置的伸縮組期望實例數。
        :type DesiredCapacity: int
        :param StartTime: 定時任務的首次觸發時間，取值爲` 時間`（UTC+8），按照`ISO8601`標準，格式：`YYYY-MM-DDThh:mm:ss+08:00`。
        :type StartTime: str
        :param EndTime: 定時任務的結束時間，取值爲` 時間`（UTC+8），按照`ISO8601`標準，格式：`YYYY-MM-DDThh:mm:ss+08:00`。<br>此參數與`Recurrence`需要同時指定，到達結束時間之後，定時任務将不再生效。
        :type EndTime: str
        :param Recurrence: 定時任務的重複方式。爲標準 Cron 格式<br>此參數與`EndTime`需要同時指定。
        :type Recurrence: str
        """
        self.ScheduledActionId = None
        self.ScheduledActionName = None
        self.MaxSize = None
        self.MinSize = None
        self.DesiredCapacity = None
        self.StartTime = None
        self.EndTime = None
        self.Recurrence = None


    def _deserialize(self, params):
        self.ScheduledActionId = params.get("ScheduledActionId")
        self.ScheduledActionName = params.get("ScheduledActionName")
        self.MaxSize = params.get("MaxSize")
        self.MinSize = params.get("MinSize")
        self.DesiredCapacity = params.get("DesiredCapacity")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Recurrence = params.get("Recurrence")


class ModifyScheduledActionResponse(AbstractModel):
    """ModifyScheduledAction返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NotificationTarget(AbstractModel):
    """通知目標

    """

    def __init__(self):
        """
        :param TargetType: 目標類型，取值範圍包括`CMQ_QUEUE`、`CMQ_TOPIC`。
<li> CMQ_QUEUE，指Top Cloud 訊息隊列-隊列模型。</li>
<li> CMQ_TOPIC，指Top Cloud 訊息隊列-主題模型。</li>
        :type TargetType: str
        :param QueueName: 隊列名稱，如果`TargetType`取值爲`CMQ_QUEUE`，則本欄位必填。
        :type QueueName: str
        :param TopicName: 主題名稱，如果`TargetType`取值爲`CMQ_TOPIC`，則本欄位必填。
        :type TopicName: str
        """
        self.TargetType = None
        self.QueueName = None
        self.TopicName = None


    def _deserialize(self, params):
        self.TargetType = params.get("TargetType")
        self.QueueName = params.get("QueueName")
        self.TopicName = params.get("TopicName")


class PaiInstance(AbstractModel):
    """PAI實例

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param DomainName: 實例域名
        :type DomainName: str
        :param PaiMateUrl: PAI管理頁面URL
        :type PaiMateUrl: str
        """
        self.InstanceId = None
        self.DomainName = None
        self.PaiMateUrl = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DomainName = params.get("DomainName")
        self.PaiMateUrl = params.get("PaiMateUrl")


class PreviewPaiDomainNameRequest(AbstractModel):
    """PreviewPaiDomainName請求參數結構體

    """

    def __init__(self):
        """
        :param DomainNameType: 域名類型
        :type DomainNameType: str
        """
        self.DomainNameType = None


    def _deserialize(self, params):
        self.DomainNameType = params.get("DomainNameType")


class PreviewPaiDomainNameResponse(AbstractModel):
    """PreviewPaiDomainName返回參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 可用的PAI域名
        :type DomainName: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DomainName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.RequestId = params.get("RequestId")


class RemoveInstancesRequest(AbstractModel):
    """RemoveInstances請求參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸縮組ID
        :type AutoScalingGroupId: str
        :param InstanceIds: CVM實例ID清單
        :type InstanceIds: list of str
        """
        self.AutoScalingGroupId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.InstanceIds = params.get("InstanceIds")


class RemoveInstancesResponse(AbstractModel):
    """RemoveInstances返回參數結構體

    """

    def __init__(self):
        """
        :param ActivityId: 伸縮活動ID
        :type ActivityId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ActivityId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ActivityId = params.get("ActivityId")
        self.RequestId = params.get("RequestId")


class RunMonitorServiceEnabled(AbstractModel):
    """描述了 “雲監控” 服務相關的訊息。

    """

    def __init__(self):
        """
        :param Enabled: 是否開啓[雲監控](https://cloud.taifucloud.com/document/product/248)服務。取值範圍：<br><li>TRUE：表示開啓雲監控服務<br><li>FALSE：表示不開啓雲監控服務<br><br>預設取值：TRUE。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")


class RunSecurityServiceEnabled(AbstractModel):
    """描述了 “雲安全” 服務相關的訊息

    """

    def __init__(self):
        """
        :param Enabled: 是否開啓[雲安全](https://cloud.taifucloud.com/document/product/296)服務。取值範圍：<br><li>TRUE：表示開啓雲安全服務<br><li>FALSE：表示不開啓雲安全服務<br><br>預設取值：TRUE。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")


class ScalingPolicy(AbstractModel):
    """告警觸發策略。

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸縮組ID。
        :type AutoScalingGroupId: str
        :param AutoScalingPolicyId: 告警觸發策略ID。
        :type AutoScalingPolicyId: str
        :param ScalingPolicyName: 告警觸發策略名稱。
        :type ScalingPolicyName: str
        :param AdjustmentType: 告警觸發後，期望實例數修改方式。取值 ：<br><li>CHANGE_IN_CAPACITY：增加或減少若幹期望實例數</li><li>EXACT_CAPACITY：調整至指定期望實例數</li> <li>PERCENT_CHANGE_IN_CAPACITY：按百分比調整期望實例數</li>
        :type AdjustmentType: str
        :param AdjustmentValue: 告警觸發後，期望實例數的調整值。
        :type AdjustmentValue: int
        :param Cooldown: 冷卻時間。
        :type Cooldown: int
        :param MetricAlarm: 告警監控指標。
        :type MetricAlarm: :class:`taifucloudcloud.autoscaling.v20180419.models.MetricAlarm`
        :param NotificationUserGroupIds: 通知組ID，即爲用戶組ID集合。
        :type NotificationUserGroupIds: list of str
        """
        self.AutoScalingGroupId = None
        self.AutoScalingPolicyId = None
        self.ScalingPolicyName = None
        self.AdjustmentType = None
        self.AdjustmentValue = None
        self.Cooldown = None
        self.MetricAlarm = None
        self.NotificationUserGroupIds = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.AutoScalingPolicyId = params.get("AutoScalingPolicyId")
        self.ScalingPolicyName = params.get("ScalingPolicyName")
        self.AdjustmentType = params.get("AdjustmentType")
        self.AdjustmentValue = params.get("AdjustmentValue")
        self.Cooldown = params.get("Cooldown")
        if params.get("MetricAlarm") is not None:
            self.MetricAlarm = MetricAlarm()
            self.MetricAlarm._deserialize(params.get("MetricAlarm"))
        self.NotificationUserGroupIds = params.get("NotificationUserGroupIds")


class ScheduledAction(AbstractModel):
    """描述定時任務的訊息

    """

    def __init__(self):
        """
        :param ScheduledActionId: 定時任務ID。
        :type ScheduledActionId: str
        :param ScheduledActionName: 定時任務名稱。
        :type ScheduledActionName: str
        :param AutoScalingGroupId: 定時任務所在伸縮組ID。
        :type AutoScalingGroupId: str
        :param StartTime: 定時任務的開始時間。取值爲` 時間`（UTC+8），按照`ISO8601`標準，格式：`YYYY-MM-DDThh:mm:ss+08:00`。
        :type StartTime: str
        :param Recurrence: 定時任務的重複方式。
        :type Recurrence: str
        :param EndTime: 定時任務的結束時間。取值爲` 時間`（UTC+8），按照`ISO8601`標準，格式：`YYYY-MM-DDThh:mm:ss+08:00`。
        :type EndTime: str
        :param MaxSize: 定時任務設置的最大實例數。
        :type MaxSize: int
        :param DesiredCapacity: 定時任務設置的期望實例數。
        :type DesiredCapacity: int
        :param MinSize: 定時任務設置的最小實例數。
        :type MinSize: int
        :param CreatedTime: 定時任務的創建時間。取值爲`UTC`時間，按照`ISO8601`標準，格式：`YYYY-MM-DDThh:mm:ssZ`。
        :type CreatedTime: str
        """
        self.ScheduledActionId = None
        self.ScheduledActionName = None
        self.AutoScalingGroupId = None
        self.StartTime = None
        self.Recurrence = None
        self.EndTime = None
        self.MaxSize = None
        self.DesiredCapacity = None
        self.MinSize = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.ScheduledActionId = params.get("ScheduledActionId")
        self.ScheduledActionName = params.get("ScheduledActionName")
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.StartTime = params.get("StartTime")
        self.Recurrence = params.get("Recurrence")
        self.EndTime = params.get("EndTime")
        self.MaxSize = params.get("MaxSize")
        self.DesiredCapacity = params.get("DesiredCapacity")
        self.MinSize = params.get("MinSize")
        self.CreatedTime = params.get("CreatedTime")


class ServiceSettings(AbstractModel):
    """服務設置

    """

    def __init__(self):
        """
        :param ReplaceMonitorUnhealthy: 開啓監控不健康替換服務。若開啓則對於雲監控標記爲不健康的實例，彈性伸縮服務會進行替換。若不指定該參數，則預設爲 False。
        :type ReplaceMonitorUnhealthy: bool
        :param ScalingMode: 取值範圍： 
CLASSIC_SCALING：經典方式，使用創建、銷毀實例來實現擴縮容； 
WAKE_UP_STOPPED_SCALING：擴容優先開機。擴容時優先對已關機的實例執行開機操作，若開機後實例數仍低於期望實例數，則創建實例，縮容仍采用銷毀實例的方式。用戶可以使用StopAutoScalingInstances介面來關閉伸縮組内的實例。監控告警觸發的擴容仍将創建實例
預設取值：CLASSIC_SCALING
        :type ScalingMode: str
        """
        self.ReplaceMonitorUnhealthy = None
        self.ScalingMode = None


    def _deserialize(self, params):
        self.ReplaceMonitorUnhealthy = params.get("ReplaceMonitorUnhealthy")
        self.ScalingMode = params.get("ScalingMode")


class SetInstancesProtectionRequest(AbstractModel):
    """SetInstancesProtection請求參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸縮組ID。
        :type AutoScalingGroupId: str
        :param InstanceIds: 實例ID。
        :type InstanceIds: list of str
        :param ProtectedFromScaleIn: 實例是否需要移出保護。
        :type ProtectedFromScaleIn: bool
        """
        self.AutoScalingGroupId = None
        self.InstanceIds = None
        self.ProtectedFromScaleIn = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.InstanceIds = params.get("InstanceIds")
        self.ProtectedFromScaleIn = params.get("ProtectedFromScaleIn")


class SetInstancesProtectionResponse(AbstractModel):
    """SetInstancesProtection返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SpotMarketOptions(AbstractModel):
    """競價相關選項

    """

    def __init__(self):
        """
        :param MaxPrice: 競價出價，例如“1.05”
        :type MaxPrice: str
        :param SpotInstanceType: 競價請求類型，當前僅支援類型：one-time，預設值爲one-time
注意：此欄位可能返回 null，表示取不到有效值。
        :type SpotInstanceType: str
        """
        self.MaxPrice = None
        self.SpotInstanceType = None


    def _deserialize(self, params):
        self.MaxPrice = params.get("MaxPrice")
        self.SpotInstanceType = params.get("SpotInstanceType")


class StartAutoScalingInstancesRequest(AbstractModel):
    """StartAutoScalingInstances請求參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸縮組ID
        :type AutoScalingGroupId: str
        :param InstanceIds: 待開啓的CVM實例ID清單
        :type InstanceIds: list of str
        """
        self.AutoScalingGroupId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.InstanceIds = params.get("InstanceIds")


class StartAutoScalingInstancesResponse(AbstractModel):
    """StartAutoScalingInstances返回參數結構體

    """

    def __init__(self):
        """
        :param ActivityId: 伸縮活動ID
        :type ActivityId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ActivityId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ActivityId = params.get("ActivityId")
        self.RequestId = params.get("RequestId")


class StopAutoScalingInstancesRequest(AbstractModel):
    """StopAutoScalingInstances請求參數結構體

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸縮組ID
        :type AutoScalingGroupId: str
        :param InstanceIds: 待關閉的CVM實例ID清單
        :type InstanceIds: list of str
        :param StoppedMode: 關閉的實例是否收費，取值爲：  
KEEP_CHARGING：關機繼續收費  
STOP_CHARGING：關機停止收費
預設爲 KEEP_CHARGING
        :type StoppedMode: str
        """
        self.AutoScalingGroupId = None
        self.InstanceIds = None
        self.StoppedMode = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.InstanceIds = params.get("InstanceIds")
        self.StoppedMode = params.get("StoppedMode")


class StopAutoScalingInstancesResponse(AbstractModel):
    """StopAutoScalingInstances返回參數結構體

    """

    def __init__(self):
        """
        :param ActivityId: 伸縮活動ID
        :type ActivityId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ActivityId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ActivityId = params.get("ActivityId")
        self.RequestId = params.get("RequestId")


class SystemDisk(AbstractModel):
    """啓動配置的系統盤配置訊息。若不指定該參數，則按照系統預設值進行分配。

    """

    def __init__(self):
        """
        :param DiskType: 系統盤類型。系統盤類型限制詳見[CVM實例配置](https://cloud.taifucloud.com/document/product/213/2177)。取值範圍：<br><li>LOCAL_BASIC：本地硬碟<br><li>LOCAL_SSD：本地SSD硬碟<br><li>CLOUD_BASIC：普通雲硬碟<br><li>CLOUD_PREMIUM：高效能雲硬碟<br><li>CLOUD_SSD：SSD雲硬碟<br><br>預設取值：LOCAL_BASIC。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param DiskSize: 系統盤大小，單位：GB。預設值爲 50
注意：此欄位可能返回 null，表示取不到有效值。
        :type DiskSize: int
        """
        self.DiskType = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")


class Tag(AbstractModel):
    """資源類型及標簽鍵值對

    """

    def __init__(self):
        """
        :param Key: 標簽鍵
        :type Key: str
        :param Value: 標簽值
        :type Value: str
        :param ResourceType: 標簽綁定的資源類型，當前支援類型："auto-scaling-group
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResourceType: str
        """
        self.Key = None
        self.Value = None
        self.ResourceType = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        self.ResourceType = params.get("ResourceType")


class TargetAttribute(AbstractModel):
    """負載均衡器目標屬性

    """

    def __init__(self):
        """
        :param Port: 端口
        :type Port: int
        :param Weight: 權重
        :type Weight: int
        """
        self.Port = None
        self.Weight = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")


class UpgradeLaunchConfigurationRequest(AbstractModel):
    """UpgradeLaunchConfiguration請求參數結構體

    """

    def __init__(self):
        """
        :param LaunchConfigurationId: 啓動配置ID。
        :type LaunchConfigurationId: str
        :param ImageId: 指定有效的[映像](https://cloud.taifucloud.com/document/product/213/4940)ID，格式形如`img-8toqc6s3`。映像類型分爲四種：<br/><li>公共映像</li><li>自定義映像</li><li>共享映像</li><li>服務市場映像</li><br/>可通過以下方式獲取可用的映像ID：<br/><li>`公共映像`、`自定義映像`、`共享映像`的映像ID可通過登入[控制台](https://console.cloud.taifucloud.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查詢；`服務映像市場`的映像ID可通過[雲市場](https://market.cloud.taifucloud.com/list)查詢。</li><li>通過調用介面 [DescribeImages](https://cloud.taifucloud.com/document/api/213/15715) ，取返回訊息中的`ImageId`欄位。</li>
        :type ImageId: str
        :param InstanceTypes: 實例機型清單，不同實例機型指定了不同的資源規格，最多支援5種實例機型。
        :type InstanceTypes: list of str
        :param LaunchConfigurationName: 啓動配置顯示名稱。名稱僅支援中文、英文、數字、下劃線、分隔符"-"、小數點，最大長度不能超60個位元。
        :type LaunchConfigurationName: str
        :param DataDisks: 實例數據盤配置訊息。若不指定該參數，則預設不購買數據盤，最多支援指定11塊數據盤。
        :type DataDisks: list of DataDisk
        :param EnhancedService: 增強服務。通過該參數可以指定是否開啓雲安全、雲監控等服務。若不指定該參數，則預設開啓雲監控、雲安全服務。
        :type EnhancedService: :class:`taifucloudcloud.autoscaling.v20180419.models.EnhancedService`
        :param InstanceChargeType: 實例計費類型，CVM預設值按照POSTPAID_BY_HOUR處理。
<br><li>POSTPAID_BY_HOUR：按小時後付費
<br><li>SPOTPAID：競價付費
        :type InstanceChargeType: str
        :param InstanceMarketOptions: 實例的市場相關選項，如競價實例相關參數，若指定實例的付費模式爲競價付費則該參數必傳。
        :type InstanceMarketOptions: :class:`taifucloudcloud.autoscaling.v20180419.models.InstanceMarketOptionsRequest`
        :param InstanceTypesCheckPolicy: 實例類型校驗策略，取值包括 ALL 和 ANY，預設取值爲ANY。
<br><li> ALL，所有實例類型（InstanceType）都可用則通過校驗，否則校驗報錯。
<br><li> ANY，存在任何一個實例類型（InstanceType）可用則通過校驗，否則校驗報錯。

實例類型不可用的常見原因包括該實例類型售罄、對應雲盤售罄等。
如果 InstanceTypes 中一款機型不存在或者已下線，則無論 InstanceTypesCheckPolicy 采用何種取值，都會校驗報錯。
        :type InstanceTypesCheckPolicy: str
        :param InternetAccessible: 公網頻寬相關訊息設置。若不指定該參數，則預設公網頻寬爲0Mbps。
        :type InternetAccessible: :class:`taifucloudcloud.autoscaling.v20180419.models.InternetAccessible`
        :param LoginSettings: 實例登入設置。通過該參數可以設置實例的登入方式密碼、金鑰或保持映像的原始登入設置。預設情況下會随機生成密碼，並以站内信方式知會到用戶。
        :type LoginSettings: :class:`taifucloudcloud.autoscaling.v20180419.models.LoginSettings`
        :param ProjectId: 實例所屬項目ID。該參數可以通過調用 [DescribeProject](https://cloud.taifucloud.com/document/api/378/4400) 的返回值中的`projectId`欄位來獲取。不填爲預設項目。
        :type ProjectId: int
        :param SecurityGroupIds: 實例所屬安全組。該參數可以通過調用 [DescribeSecurityGroups](https://cloud.taifucloud.com/document/api/215/15808) 的返回值中的`SecurityGroupId`欄位來獲取。若不指定該參數，則預設不綁定安全組。
        :type SecurityGroupIds: list of str
        :param SystemDisk: 實例系統盤配置訊息。若不指定該參數，則按照系統預設值進行分配。
        :type SystemDisk: :class:`taifucloudcloud.autoscaling.v20180419.models.SystemDisk`
        :param UserData: 經過 Base64 編碼後的自定義數據，最大長度不超過16KB。
        :type UserData: str
        :param InstanceTags: 標簽清單。通過指定該參數，可以爲擴容的實例綁定標簽。最多支援指定10個標簽。
        :type InstanceTags: list of InstanceTag
        :param CamRoleName: CAM角色名稱。可通過DescribeRoleList介面返回值中的roleName獲取。
        :type CamRoleName: str
        :param HostNameSettings: 雲伺服器主機名（HostName）的相關設置。
        :type HostNameSettings: :class:`taifucloudcloud.autoscaling.v20180419.models.HostNameSettings`
        :param InstanceNameSettings: 雲伺服器實例名（InstanceName）的相關設置。
        :type InstanceNameSettings: :class:`taifucloudcloud.autoscaling.v20180419.models.InstanceNameSettings`
        :param InstanceChargePrepaid: 預付費模式，即包年包月相關參數設置。通過該參數可以指定包年包月實例的購買時長、是否設置自動續約等屬性。若指定實例的付費模式爲預付費則該參數必傳。
        :type InstanceChargePrepaid: :class:`taifucloudcloud.autoscaling.v20180419.models.InstanceChargePrepaid`
        """
        self.LaunchConfigurationId = None
        self.ImageId = None
        self.InstanceTypes = None
        self.LaunchConfigurationName = None
        self.DataDisks = None
        self.EnhancedService = None
        self.InstanceChargeType = None
        self.InstanceMarketOptions = None
        self.InstanceTypesCheckPolicy = None
        self.InternetAccessible = None
        self.LoginSettings = None
        self.ProjectId = None
        self.SecurityGroupIds = None
        self.SystemDisk = None
        self.UserData = None
        self.InstanceTags = None
        self.CamRoleName = None
        self.HostNameSettings = None
        self.InstanceNameSettings = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.ImageId = params.get("ImageId")
        self.InstanceTypes = params.get("InstanceTypes")
        self.LaunchConfigurationName = params.get("LaunchConfigurationName")
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceMarketOptions") is not None:
            self.InstanceMarketOptions = InstanceMarketOptionsRequest()
            self.InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self.InstanceTypesCheckPolicy = params.get("InstanceTypesCheckPolicy")
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.ProjectId = params.get("ProjectId")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        self.UserData = params.get("UserData")
        if params.get("InstanceTags") is not None:
            self.InstanceTags = []
            for item in params.get("InstanceTags"):
                obj = InstanceTag()
                obj._deserialize(item)
                self.InstanceTags.append(obj)
        self.CamRoleName = params.get("CamRoleName")
        if params.get("HostNameSettings") is not None:
            self.HostNameSettings = HostNameSettings()
            self.HostNameSettings._deserialize(params.get("HostNameSettings"))
        if params.get("InstanceNameSettings") is not None:
            self.InstanceNameSettings = InstanceNameSettings()
            self.InstanceNameSettings._deserialize(params.get("InstanceNameSettings"))
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))


class UpgradeLaunchConfigurationResponse(AbstractModel):
    """UpgradeLaunchConfiguration返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpgradeLifecycleHookRequest(AbstractModel):
    """UpgradeLifecycleHook請求參數結構體

    """

    def __init__(self):
        """
        :param LifecycleHookId: 生命週期挂鈎ID
        :type LifecycleHookId: str
        :param LifecycleHookName: 生命週期挂鈎名稱
        :type LifecycleHookName: str
        :param LifecycleTransition: 進行生命週期挂鈎的場景，取值範圍包括“INSTANCE_LAUNCHING”和“INSTANCE_TERMINATING”
        :type LifecycleTransition: str
        :param DefaultResult: 定義伸縮組在生命週期挂鈎超時的情況下應采取的操作，取值範圍是“CONTINUE”或“ABANDON”，預設值爲“CONTINUE”
        :type DefaultResult: str
        :param HeartbeatTimeout: 生命週期挂鈎超時之前可以經過的最長時間（以秒爲單位），範圍從30到3600秒，預設值爲300秒
        :type HeartbeatTimeout: int
        :param NotificationMetadata: 彈性伸縮向通知目標發送的附加訊息，預設值爲''
        :type NotificationMetadata: str
        :param NotificationTarget: 通知目標
        :type NotificationTarget: :class:`taifucloudcloud.autoscaling.v20180419.models.NotificationTarget`
        :param LifecycleTransitionType: 進行生命週期挂鈎的場景類型，取值範圍包括NORMAL 和 EXTENSION。說明：設置爲EXTENSION值，在AttachInstances、DetachInstances、RemoveInstaces介面時會觸發生命週期挂鈎操作，值爲NORMAL則不會在這些介面中觸發生命週期挂鈎。
        :type LifecycleTransitionType: str
        """
        self.LifecycleHookId = None
        self.LifecycleHookName = None
        self.LifecycleTransition = None
        self.DefaultResult = None
        self.HeartbeatTimeout = None
        self.NotificationMetadata = None
        self.NotificationTarget = None
        self.LifecycleTransitionType = None


    def _deserialize(self, params):
        self.LifecycleHookId = params.get("LifecycleHookId")
        self.LifecycleHookName = params.get("LifecycleHookName")
        self.LifecycleTransition = params.get("LifecycleTransition")
        self.DefaultResult = params.get("DefaultResult")
        self.HeartbeatTimeout = params.get("HeartbeatTimeout")
        self.NotificationMetadata = params.get("NotificationMetadata")
        if params.get("NotificationTarget") is not None:
            self.NotificationTarget = NotificationTarget()
            self.NotificationTarget._deserialize(params.get("NotificationTarget"))
        self.LifecycleTransitionType = params.get("LifecycleTransitionType")


class UpgradeLifecycleHookResponse(AbstractModel):
    """UpgradeLifecycleHook返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")