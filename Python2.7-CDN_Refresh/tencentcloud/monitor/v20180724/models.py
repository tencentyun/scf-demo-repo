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


class BindingPolicyObjectDimension(AbstractModel):
    """策略綁定實例維度訊息

    """

    def __init__(self):
        """
        :param Region: 地域名
        :type Region: str
        :param RegionId: 地域ID
        :type RegionId: int
        :param Dimensions: 維度訊息
        :type Dimensions: str
        :param EventDimensions: 事件維度訊息
        :type EventDimensions: str
        """
        self.Region = None
        self.RegionId = None
        self.Dimensions = None
        self.EventDimensions = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionId = params.get("RegionId")
        self.Dimensions = params.get("Dimensions")
        self.EventDimensions = params.get("EventDimensions")


class BindingPolicyObjectRequest(AbstractModel):
    """BindingPolicyObject請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 策略分組Id
        :type GroupId: int
        :param Module: 必填。固定值"monitor"
        :type Module: str
        :param InstanceGroupId: 實例分組ID
        :type InstanceGroupId: int
        :param Dimensions: 需要綁定的對象維度訊息
        :type Dimensions: list of BindingPolicyObjectDimension
        """
        self.GroupId = None
        self.Module = None
        self.InstanceGroupId = None
        self.Dimensions = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Module = params.get("Module")
        self.InstanceGroupId = params.get("InstanceGroupId")
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = BindingPolicyObjectDimension()
                obj._deserialize(item)
                self.Dimensions.append(obj)


class BindingPolicyObjectResponse(AbstractModel):
    """BindingPolicyObject返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreatePolicyGroupCondition(AbstractModel):
    """創建策略傳入的阈值告警條件

    """

    def __init__(self):
        """
        :param MetricId: 指标Id
        :type MetricId: int
        :param AlarmNotifyType: 告警發送收斂類型。0連續告警，1指數告警
        :type AlarmNotifyType: int
        :param AlarmNotifyPeriod: 告警發送週期單位秒。<0 不觸發, 0 只觸發一次, >0 每隔triggerTime秒觸發一次
        :type AlarmNotifyPeriod: int
        :param CalcType: 比較類型，1表示大于，2表示大于等于，3表示小於，4表示小於等于，5表示相等，6表示不相等。如果指标有配置預設比較類型值可以不填。
        :type CalcType: int
        :param CalcValue: 比較的值，如果指标不必須CalcValue可不填
        :type CalcValue: float
        :param CalcPeriod: 數據聚合週期(單位秒)，若指标有預設值可不填
        :type CalcPeriod: int
        :param ContinuePeriod: 持續幾個檢測週期觸發規則會告警
        :type ContinuePeriod: int
        :param RuleId: 如果通過模版創建，需要傳入模版中該指标的對應RuleId
        :type RuleId: int
        """
        self.MetricId = None
        self.AlarmNotifyType = None
        self.AlarmNotifyPeriod = None
        self.CalcType = None
        self.CalcValue = None
        self.CalcPeriod = None
        self.ContinuePeriod = None
        self.RuleId = None


    def _deserialize(self, params):
        self.MetricId = params.get("MetricId")
        self.AlarmNotifyType = params.get("AlarmNotifyType")
        self.AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self.CalcType = params.get("CalcType")
        self.CalcValue = params.get("CalcValue")
        self.CalcPeriod = params.get("CalcPeriod")
        self.ContinuePeriod = params.get("ContinuePeriod")
        self.RuleId = params.get("RuleId")


class CreatePolicyGroupEventCondition(AbstractModel):
    """創建策略傳入的事件告警條件

    """

    def __init__(self):
        """
        :param EventId: 告警事件的Id
        :type EventId: int
        :param AlarmNotifyType: 告警發送收斂類型。0連續告警，1指數告警
        :type AlarmNotifyType: int
        :param AlarmNotifyPeriod: 告警發送週期單位秒。<0 不觸發, 0 只觸發一次, >0 每隔triggerTime秒觸發一次
        :type AlarmNotifyPeriod: int
        :param RuleId: 如果通過模版創建，需要傳入模版中該指标的對應RuleId
        :type RuleId: int
        """
        self.EventId = None
        self.AlarmNotifyType = None
        self.AlarmNotifyPeriod = None
        self.RuleId = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.AlarmNotifyType = params.get("AlarmNotifyType")
        self.AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self.RuleId = params.get("RuleId")


class CreatePolicyGroupRequest(AbstractModel):
    """CreatePolicyGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupName: 組策略名稱
        :type GroupName: str
        :param Module: 固定值，爲"monitor"
        :type Module: str
        :param ViewName: 策略組所屬視圖的名稱，若通過模版創建，可不傳入
        :type ViewName: str
        :param ProjectId: 策略組所屬項目Id，會進行鑒權操作
        :type ProjectId: int
        :param ConditionTempGroupId: 模版策略組Id, 通過模版創建時才需要傳
        :type ConditionTempGroupId: int
        :param IsShielded: 是否屏蔽策略組，0表示不屏蔽，1表示屏蔽。不填預設爲0
        :type IsShielded: int
        :param Remark: 策略組的備注訊息
        :type Remark: str
        :param InsertTime: 插入時間，戳格式爲Unix時間戳，不填則按後台處理時間填充
        :type InsertTime: int
        :param Conditions: 策略組中的阈值告警規則
        :type Conditions: list of CreatePolicyGroupCondition
        :param EventConditions: 策略組中的事件告警規則
        :type EventConditions: list of CreatePolicyGroupEventCondition
        :param BackEndCall: 是否爲後端調用。當且僅當值爲1時，後台拉取策略模版中的規則填充入Conditions以及EventConditions欄位
        :type BackEndCall: int
        :param IsUnionRule: 指标告警規則的且或關系，0表示或規則(滿足任意規則就告警)，1表示且規則(滿足所有規則才告警)
        :type IsUnionRule: int
        """
        self.GroupName = None
        self.Module = None
        self.ViewName = None
        self.ProjectId = None
        self.ConditionTempGroupId = None
        self.IsShielded = None
        self.Remark = None
        self.InsertTime = None
        self.Conditions = None
        self.EventConditions = None
        self.BackEndCall = None
        self.IsUnionRule = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.Module = params.get("Module")
        self.ViewName = params.get("ViewName")
        self.ProjectId = params.get("ProjectId")
        self.ConditionTempGroupId = params.get("ConditionTempGroupId")
        self.IsShielded = params.get("IsShielded")
        self.Remark = params.get("Remark")
        self.InsertTime = params.get("InsertTime")
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = CreatePolicyGroupCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)
        if params.get("EventConditions") is not None:
            self.EventConditions = []
            for item in params.get("EventConditions"):
                obj = CreatePolicyGroupEventCondition()
                obj._deserialize(item)
                self.EventConditions.append(obj)
        self.BackEndCall = params.get("BackEndCall")
        self.IsUnionRule = params.get("IsUnionRule")


class CreatePolicyGroupResponse(AbstractModel):
    """CreatePolicyGroup返回參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 創建成功的策略組Id
        :type GroupId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")


class DataPoint(AbstractModel):
    """監控數據點

    """

    def __init__(self):
        """
        :param Dimensions: 實例對象維度組合
        :type Dimensions: list of Dimension
        :param Timestamps: 時間戳數組，表示那些時間點有數據，缺失的時間戳，沒有數據點，可以理解爲掉點了
        :type Timestamps: list of float
        :param Values: 監控值數組，該數組和Timestamps一一對應
        :type Values: list of float
        """
        self.Dimensions = None
        self.Timestamps = None
        self.Values = None


    def _deserialize(self, params):
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = Dimension()
                obj._deserialize(item)
                self.Dimensions.append(obj)
        self.Timestamps = params.get("Timestamps")
        self.Values = params.get("Values")


class DeletePolicyGroupRequest(AbstractModel):
    """DeletePolicyGroup請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 固定值，爲"monitor"
        :type Module: str
        :param GroupId: 策略組id
        :type GroupId: list of int
        """
        self.Module = None
        self.GroupId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.GroupId = params.get("GroupId")


class DeletePolicyGroupResponse(AbstractModel):
    """DeletePolicyGroup返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccidentEventListAlarms(AbstractModel):
    """DescribeAccidentEventList介面的出參類型

    """

    def __init__(self):
        """
        :param BusinessTypeDesc: 事件分類
注意：此欄位可能返回 null，表示取不到有效值。
        :type BusinessTypeDesc: str
        :param AccidentTypeDesc: 事件類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type AccidentTypeDesc: str
        :param BusinessID: 事件分類的ID，1表示服務問題，2表示其他訂閱
注意：此欄位可能返回 null，表示取不到有效值。
        :type BusinessID: int
        :param EventStatus: 事件狀态的ID，0表示已恢複，1表示未恢複
注意：此欄位可能返回 null，表示取不到有效值。
        :type EventStatus: int
        :param AffectResource: 影響的對象
注意：此欄位可能返回 null，表示取不到有效值。
        :type AffectResource: str
        :param Region: 事件的地域
注意：此欄位可能返回 null，表示取不到有效值。
        :type Region: str
        :param OccurTime: 事件發生的時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type OccurTime: str
        :param UpdateTime: 更新時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.BusinessTypeDesc = None
        self.AccidentTypeDesc = None
        self.BusinessID = None
        self.EventStatus = None
        self.AffectResource = None
        self.Region = None
        self.OccurTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.BusinessTypeDesc = params.get("BusinessTypeDesc")
        self.AccidentTypeDesc = params.get("AccidentTypeDesc")
        self.BusinessID = params.get("BusinessID")
        self.EventStatus = params.get("EventStatus")
        self.AffectResource = params.get("AffectResource")
        self.Region = params.get("Region")
        self.OccurTime = params.get("OccurTime")
        self.UpdateTime = params.get("UpdateTime")


class DescribeAccidentEventListRequest(AbstractModel):
    """DescribeAccidentEventList請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 介面模組名，當前介面取值monitor
        :type Module: str
        :param StartTime: 起始時間，預設一天前的時間戳
        :type StartTime: int
        :param EndTime: 結束時間，預設當前時間戳
        :type EndTime: int
        :param Limit: 分頁參數，每頁返回的數量，取值1~100，預設20
        :type Limit: int
        :param Offset: 分頁參數，頁偏移量，從0開始計數，預設0
        :type Offset: int
        :param UpdateTimeOrder: 根據UpdateTime排序的規則，取值asc或desc
        :type UpdateTimeOrder: str
        :param OccurTimeOrder: 根據OccurTime排序的規則，取值asc或desc（優先根據UpdateTimeOrder排序）
        :type OccurTimeOrder: str
        :param AccidentType: 根據事件類型過濾，1表示服務問題，2表示其他訂閱
        :type AccidentType: list of int
        :param AccidentEvent: 根據事件過濾，1表示雲伺服器儲存問題，2表示雲伺服器網絡連接問題，3表示雲伺服器運作異常，202表示運營商網絡抖動
        :type AccidentEvent: list of int
        :param AccidentStatus: 根據事件狀态過濾，0表示已恢複，1表示未恢複
        :type AccidentStatus: list of int
        :param AccidentRegion: 根據事件地域過濾，gz表示 ，sh表示 等
        :type AccidentRegion: list of str
        :param AffectResource: 根據影響資源過濾，比如ins-19a06bka
        :type AffectResource: str
        """
        self.Module = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.UpdateTimeOrder = None
        self.OccurTimeOrder = None
        self.AccidentType = None
        self.AccidentEvent = None
        self.AccidentStatus = None
        self.AccidentRegion = None
        self.AffectResource = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.UpdateTimeOrder = params.get("UpdateTimeOrder")
        self.OccurTimeOrder = params.get("OccurTimeOrder")
        self.AccidentType = params.get("AccidentType")
        self.AccidentEvent = params.get("AccidentEvent")
        self.AccidentStatus = params.get("AccidentStatus")
        self.AccidentRegion = params.get("AccidentRegion")
        self.AffectResource = params.get("AffectResource")


class DescribeAccidentEventListResponse(AbstractModel):
    """DescribeAccidentEventList返回參數結構體

    """

    def __init__(self):
        """
        :param Alarms: 平台事件清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Alarms: list of DescribeAccidentEventListAlarms
        :param Total: 平台事件的總數
注意：此欄位可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Alarms = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Alarms") is not None:
            self.Alarms = []
            for item in params.get("Alarms"):
                obj = DescribeAccidentEventListAlarms()
                obj._deserialize(item)
                self.Alarms.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeBaseMetricsRequest(AbstractModel):
    """DescribeBaseMetrics請求參數結構體

    """

    def __init__(self):
        """
        :param Namespace: 業務命名空間，各個雲産品的業務命名空間不同。如需獲取業務命名空間，請前往各産品監控介面文件，例如雲伺服器的命名空間，可參見 [雲伺服器監控介面](https://cloud.taifucloud.com/document/api/248/30385)
        :type Namespace: str
        :param MetricName: 指标名，各個雲産品的指标名不同。如需獲取指标名，請前往各産品監控介面文件，例如雲伺服器的指标名，可參見 [雲伺服器監控介面](https://cloud.taifucloud.com/document/api/248/30385)
        :type MetricName: str
        """
        self.Namespace = None
        self.MetricName = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.MetricName = params.get("MetricName")


class DescribeBaseMetricsResponse(AbstractModel):
    """DescribeBaseMetrics返回參數結構體

    """

    def __init__(self):
        """
        :param MetricSet: 查詢得到的指标描述清單
        :type MetricSet: list of MetricSet
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.MetricSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MetricSet") is not None:
            self.MetricSet = []
            for item in params.get("MetricSet"):
                obj = MetricSet()
                obj._deserialize(item)
                self.MetricSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBasicAlarmListAlarms(AbstractModel):
    """DescribeBasicAlarmList返回的Alarms

    """

    def __init__(self):
        """
        :param Id: 該條告警的ID
        :type Id: int
        :param ProjectId: 項目ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param ProjectName: 項目名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProjectName: str
        :param Status: 告警狀态ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: int
        :param AlarmStatus: 告警狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type AlarmStatus: str
        :param GroupId: 策略組ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupId: int
        :param GroupName: 策略組名
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param FirstOccurTime: 發生時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type FirstOccurTime: str
        :param Duration: 持續時間，單位s
注意：此欄位可能返回 null，表示取不到有效值。
        :type Duration: int
        :param LastOccurTime: 結束時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type LastOccurTime: str
        :param Content: 告警内容
注意：此欄位可能返回 null，表示取不到有效值。
        :type Content: str
        :param ObjName: 告警對象
注意：此欄位可能返回 null，表示取不到有效值。
        :type ObjName: str
        :param ObjId: 告警對象ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ObjId: str
        :param ViewName: 策略類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type ViewName: str
        :param Vpc: VPC，只有CVM有
注意：此欄位可能返回 null，表示取不到有效值。
        :type Vpc: str
        :param MetricId: 指标ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type MetricId: int
        :param MetricName: 指标名
注意：此欄位可能返回 null，表示取不到有效值。
        :type MetricName: str
        :param AlarmType: 告警類型，0表示指标告警，2表示産品事件告警，3表示平台事件告警
注意：此欄位可能返回 null，表示取不到有效值。
        :type AlarmType: int
        :param Region: 地域
注意：此欄位可能返回 null，表示取不到有效值。
        :type Region: str
        :param Dimensions: 告警對象維度訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Dimensions: str
        :param NotifyWay: 通知方式
注意：此欄位可能返回 null，表示取不到有效值。
        :type NotifyWay: list of str
        :param InstanceGroup: 所屬實例組訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceGroup: list of InstanceGroup
        """
        self.Id = None
        self.ProjectId = None
        self.ProjectName = None
        self.Status = None
        self.AlarmStatus = None
        self.GroupId = None
        self.GroupName = None
        self.FirstOccurTime = None
        self.Duration = None
        self.LastOccurTime = None
        self.Content = None
        self.ObjName = None
        self.ObjId = None
        self.ViewName = None
        self.Vpc = None
        self.MetricId = None
        self.MetricName = None
        self.AlarmType = None
        self.Region = None
        self.Dimensions = None
        self.NotifyWay = None
        self.InstanceGroup = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.Status = params.get("Status")
        self.AlarmStatus = params.get("AlarmStatus")
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.FirstOccurTime = params.get("FirstOccurTime")
        self.Duration = params.get("Duration")
        self.LastOccurTime = params.get("LastOccurTime")
        self.Content = params.get("Content")
        self.ObjName = params.get("ObjName")
        self.ObjId = params.get("ObjId")
        self.ViewName = params.get("ViewName")
        self.Vpc = params.get("Vpc")
        self.MetricId = params.get("MetricId")
        self.MetricName = params.get("MetricName")
        self.AlarmType = params.get("AlarmType")
        self.Region = params.get("Region")
        self.Dimensions = params.get("Dimensions")
        self.NotifyWay = params.get("NotifyWay")
        if params.get("InstanceGroup") is not None:
            self.InstanceGroup = []
            for item in params.get("InstanceGroup"):
                obj = InstanceGroup()
                obj._deserialize(item)
                self.InstanceGroup.append(obj)


class DescribeBasicAlarmListRequest(AbstractModel):
    """DescribeBasicAlarmList請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 介面模組名，當前取值monitor
        :type Module: str
        :param StartTime: 起始時間，預設一天前的時間戳
        :type StartTime: int
        :param EndTime: 結束時間，預設當前時間戳
        :type EndTime: int
        :param Limit: 分頁參數，每頁返回的數量，取值1~100，預設20
        :type Limit: int
        :param Offset: 分頁參數，頁偏移量，從0開始計數，預設0
        :type Offset: int
        :param OccurTimeOrder: 根據發生時間排序，取值ASC或DESC
        :type OccurTimeOrder: str
        :param ProjectIds: 根據項目ID過濾
        :type ProjectIds: list of int
        :param ViewNames: 根據策略類型過濾
        :type ViewNames: list of str
        :param AlarmStatus: 根據告警狀态過濾
        :type AlarmStatus: list of int
        :param ObjLike: 根據告警對象過濾
        :type ObjLike: str
        :param InstanceGroupIds: 根據實例組ID過濾
        :type InstanceGroupIds: list of int
        """
        self.Module = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.OccurTimeOrder = None
        self.ProjectIds = None
        self.ViewNames = None
        self.AlarmStatus = None
        self.ObjLike = None
        self.InstanceGroupIds = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OccurTimeOrder = params.get("OccurTimeOrder")
        self.ProjectIds = params.get("ProjectIds")
        self.ViewNames = params.get("ViewNames")
        self.AlarmStatus = params.get("AlarmStatus")
        self.ObjLike = params.get("ObjLike")
        self.InstanceGroupIds = params.get("InstanceGroupIds")


class DescribeBasicAlarmListResponse(AbstractModel):
    """DescribeBasicAlarmList返回參數結構體

    """

    def __init__(self):
        """
        :param Alarms: 告警清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Alarms: list of DescribeBasicAlarmListAlarms
        :param Total: 總數
注意：此欄位可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Alarms = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Alarms") is not None:
            self.Alarms = []
            for item in params.get("Alarms"):
                obj = DescribeBasicAlarmListAlarms()
                obj._deserialize(item)
                self.Alarms.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeBindingPolicyObjectListDimension(AbstractModel):
    """DescribeBindingPolicyObjectList介面的Dimension

    """

    def __init__(self):
        """
        :param RegionId: 地域id
        :type RegionId: int
        :param Region: 地域簡稱
        :type Region: str
        :param Dimensions: 維度組合json字串
        :type Dimensions: str
        :param EventDimensions: 事件維度組合json字串
        :type EventDimensions: str
        """
        self.RegionId = None
        self.Region = None
        self.Dimensions = None
        self.EventDimensions = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.Region = params.get("Region")
        self.Dimensions = params.get("Dimensions")
        self.EventDimensions = params.get("EventDimensions")


class DescribeBindingPolicyObjectListInstance(AbstractModel):
    """查詢策略綁定對象清單介面返回的對象實例訊息

    """

    def __init__(self):
        """
        :param UniqueId: 對象唯一id
        :type UniqueId: str
        :param Dimensions: 表示對象實例的維度集合，jsonObj字串
        :type Dimensions: str
        :param IsShielded: 對象是否被屏蔽，0表示未屏蔽，1表示被屏蔽
        :type IsShielded: int
        :param Region: 對象所在的地域
        :type Region: str
        """
        self.UniqueId = None
        self.Dimensions = None
        self.IsShielded = None
        self.Region = None


    def _deserialize(self, params):
        self.UniqueId = params.get("UniqueId")
        self.Dimensions = params.get("Dimensions")
        self.IsShielded = params.get("IsShielded")
        self.Region = params.get("Region")


class DescribeBindingPolicyObjectListInstanceGroup(AbstractModel):
    """DescribeBindingPolicyObjectList返回的是實例分組訊息

    """

    def __init__(self):
        """
        :param InstanceGroupId: 實例分組id
        :type InstanceGroupId: int
        :param ViewName: 告警策略類型名稱
        :type ViewName: str
        :param LastEditUin: 最後編輯uin
        :type LastEditUin: str
        :param GroupName: 實例分組名稱
        :type GroupName: str
        :param InstanceSum: 實例數量
        :type InstanceSum: int
        :param UpdateTime: 更新時間
        :type UpdateTime: int
        :param InsertTime: 創建時間
        :type InsertTime: int
        :param Regions: 實例所在的地域集合
注意：此欄位可能返回 null，表示取不到有效值。
        :type Regions: list of str
        """
        self.InstanceGroupId = None
        self.ViewName = None
        self.LastEditUin = None
        self.GroupName = None
        self.InstanceSum = None
        self.UpdateTime = None
        self.InsertTime = None
        self.Regions = None


    def _deserialize(self, params):
        self.InstanceGroupId = params.get("InstanceGroupId")
        self.ViewName = params.get("ViewName")
        self.LastEditUin = params.get("LastEditUin")
        self.GroupName = params.get("GroupName")
        self.InstanceSum = params.get("InstanceSum")
        self.UpdateTime = params.get("UpdateTime")
        self.InsertTime = params.get("InsertTime")
        self.Regions = params.get("Regions")


class DescribeBindingPolicyObjectListRequest(AbstractModel):
    """DescribeBindingPolicyObjectList請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 固定值，爲"monitor"
        :type Module: str
        :param GroupId: 策略組id
        :type GroupId: int
        :param Limit: 分頁參數，每頁返回的數量，取值1~100，預設20
        :type Limit: int
        :param Offset: 分頁參數，頁偏移量，從0開始計數，預設0
        :type Offset: int
        :param Dimensions: 篩選對象的維度訊息
        :type Dimensions: list of DescribeBindingPolicyObjectListDimension
        """
        self.Module = None
        self.GroupId = None
        self.Limit = None
        self.Offset = None
        self.Dimensions = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.GroupId = params.get("GroupId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = DescribeBindingPolicyObjectListDimension()
                obj._deserialize(item)
                self.Dimensions.append(obj)


class DescribeBindingPolicyObjectListResponse(AbstractModel):
    """DescribeBindingPolicyObjectList返回參數結構體

    """

    def __init__(self):
        """
        :param List: 綁定的對象實例清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type List: list of DescribeBindingPolicyObjectListInstance
        :param Total: 綁定的對象實例總數
        :type Total: int
        :param NoShieldedSum: 未屏蔽的對象實例數
        :type NoShieldedSum: int
        :param InstanceGroup: 綁定的實例分組訊息，沒有綁定實例分組則爲空
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceGroup: :class:`taifucloudcloud.monitor.v20180724.models.DescribeBindingPolicyObjectListInstanceGroup`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.Total = None
        self.NoShieldedSum = None
        self.InstanceGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = DescribeBindingPolicyObjectListInstance()
                obj._deserialize(item)
                self.List.append(obj)
        self.Total = params.get("Total")
        self.NoShieldedSum = params.get("NoShieldedSum")
        if params.get("InstanceGroup") is not None:
            self.InstanceGroup = DescribeBindingPolicyObjectListInstanceGroup()
            self.InstanceGroup._deserialize(params.get("InstanceGroup"))
        self.RequestId = params.get("RequestId")


class DescribePolicyConditionListCondition(AbstractModel):
    """DescribePolicyConditionList策略條件

    """

    def __init__(self):
        """
        :param PolicyViewName: 策略視圖名稱
        :type PolicyViewName: str
        :param EventMetrics: 事件告警條件
注意：此欄位可能返回 null，表示取不到有效值。
        :type EventMetrics: list of DescribePolicyConditionListEventMetric
        :param IsSupportMultiRegion: 是否支援多地域
        :type IsSupportMultiRegion: bool
        :param Metrics: 指标告警條件
注意：此欄位可能返回 null，表示取不到有效值。
        :type Metrics: list of DescribePolicyConditionListMetric
        :param Name: 策略類型名稱
        :type Name: str
        :param SortId: 排序id
        :type SortId: int
        :param SupportDefault: 是否支援預設策略
        :type SupportDefault: bool
        :param SupportRegions: 支援該策略類型的地域清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type SupportRegions: list of str
        """
        self.PolicyViewName = None
        self.EventMetrics = None
        self.IsSupportMultiRegion = None
        self.Metrics = None
        self.Name = None
        self.SortId = None
        self.SupportDefault = None
        self.SupportRegions = None


    def _deserialize(self, params):
        self.PolicyViewName = params.get("PolicyViewName")
        if params.get("EventMetrics") is not None:
            self.EventMetrics = []
            for item in params.get("EventMetrics"):
                obj = DescribePolicyConditionListEventMetric()
                obj._deserialize(item)
                self.EventMetrics.append(obj)
        self.IsSupportMultiRegion = params.get("IsSupportMultiRegion")
        if params.get("Metrics") is not None:
            self.Metrics = []
            for item in params.get("Metrics"):
                obj = DescribePolicyConditionListMetric()
                obj._deserialize(item)
                self.Metrics.append(obj)
        self.Name = params.get("Name")
        self.SortId = params.get("SortId")
        self.SupportDefault = params.get("SupportDefault")
        self.SupportRegions = params.get("SupportRegions")


class DescribePolicyConditionListConfigManual(AbstractModel):
    """DescribePolicyConditionList.ConfigManual

    """

    def __init__(self):
        """
        :param CalcType: 檢測方式
注意：此欄位可能返回 null，表示取不到有效值。
        :type CalcType: :class:`taifucloudcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualCalcType`
        :param CalcValue: 檢測阈值
注意：此欄位可能返回 null，表示取不到有效值。
        :type CalcValue: :class:`taifucloudcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualCalcValue`
        :param ContinueTime: 持續時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type ContinueTime: :class:`taifucloudcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualContinueTime`
        :param Period: 數據週期
注意：此欄位可能返回 null，表示取不到有效值。
        :type Period: :class:`taifucloudcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualPeriod`
        :param PeriodNum: 持續週期個數
注意：此欄位可能返回 null，表示取不到有效值。
        :type PeriodNum: :class:`taifucloudcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualPeriodNum`
        :param StatType: 聚合方式
注意：此欄位可能返回 null，表示取不到有效值。
        :type StatType: :class:`taifucloudcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManualStatType`
        """
        self.CalcType = None
        self.CalcValue = None
        self.ContinueTime = None
        self.Period = None
        self.PeriodNum = None
        self.StatType = None


    def _deserialize(self, params):
        if params.get("CalcType") is not None:
            self.CalcType = DescribePolicyConditionListConfigManualCalcType()
            self.CalcType._deserialize(params.get("CalcType"))
        if params.get("CalcValue") is not None:
            self.CalcValue = DescribePolicyConditionListConfigManualCalcValue()
            self.CalcValue._deserialize(params.get("CalcValue"))
        if params.get("ContinueTime") is not None:
            self.ContinueTime = DescribePolicyConditionListConfigManualContinueTime()
            self.ContinueTime._deserialize(params.get("ContinueTime"))
        if params.get("Period") is not None:
            self.Period = DescribePolicyConditionListConfigManualPeriod()
            self.Period._deserialize(params.get("Period"))
        if params.get("PeriodNum") is not None:
            self.PeriodNum = DescribePolicyConditionListConfigManualPeriodNum()
            self.PeriodNum._deserialize(params.get("PeriodNum"))
        if params.get("StatType") is not None:
            self.StatType = DescribePolicyConditionListConfigManualStatType()
            self.StatType._deserialize(params.get("StatType"))


class DescribePolicyConditionListConfigManualCalcType(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.CalcType

    """

    def __init__(self):
        """
        :param Keys: CalcType 取值
注意：此欄位可能返回 null，表示取不到有效值。
        :type Keys: list of int
        :param Need: 是否必須
        :type Need: bool
        """
        self.Keys = None
        self.Need = None


    def _deserialize(self, params):
        self.Keys = params.get("Keys")
        self.Need = params.get("Need")


class DescribePolicyConditionListConfigManualCalcValue(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.CalcValue

    """

    def __init__(self):
        """
        :param Default: 預設值
注意：此欄位可能返回 null，表示取不到有效值。
        :type Default: str
        :param Fixed: 固定值
注意：此欄位可能返回 null，表示取不到有效值。
        :type Fixed: str
        :param Max: 最大值
注意：此欄位可能返回 null，表示取不到有效值。
        :type Max: str
        :param Min: 最小值
注意：此欄位可能返回 null，表示取不到有效值。
        :type Min: str
        :param Need: 是否必須
        :type Need: bool
        """
        self.Default = None
        self.Fixed = None
        self.Max = None
        self.Min = None
        self.Need = None


    def _deserialize(self, params):
        self.Default = params.get("Default")
        self.Fixed = params.get("Fixed")
        self.Max = params.get("Max")
        self.Min = params.get("Min")
        self.Need = params.get("Need")


class DescribePolicyConditionListConfigManualContinueTime(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.ContinueTime

    """

    def __init__(self):
        """
        :param Default: 預設持續時間，單位：秒
注意：此欄位可能返回 null，表示取不到有效值。
        :type Default: int
        :param Keys: 可選持續時間，單位：秒
注意：此欄位可能返回 null，表示取不到有效值。
        :type Keys: list of int
        :param Need: 是否必須
        :type Need: bool
        """
        self.Default = None
        self.Keys = None
        self.Need = None


    def _deserialize(self, params):
        self.Default = params.get("Default")
        self.Keys = params.get("Keys")
        self.Need = params.get("Need")


class DescribePolicyConditionListConfigManualPeriod(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.Period

    """

    def __init__(self):
        """
        :param Default: 預設週期，單位：秒
注意：此欄位可能返回 null，表示取不到有效值。
        :type Default: int
        :param Keys: 可選週期，單位：秒
注意：此欄位可能返回 null，表示取不到有效值。
        :type Keys: list of int
        :param Need: 是否必須
        :type Need: bool
        """
        self.Default = None
        self.Keys = None
        self.Need = None


    def _deserialize(self, params):
        self.Default = params.get("Default")
        self.Keys = params.get("Keys")
        self.Need = params.get("Need")


class DescribePolicyConditionListConfigManualPeriodNum(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.PeriodNum

    """

    def __init__(self):
        """
        :param Default: 預設週期數
注意：此欄位可能返回 null，表示取不到有效值。
        :type Default: int
        :param Keys: 可選週期數
注意：此欄位可能返回 null，表示取不到有效值。
        :type Keys: list of int
        :param Need: 是否必須
        :type Need: bool
        """
        self.Default = None
        self.Keys = None
        self.Need = None


    def _deserialize(self, params):
        self.Default = params.get("Default")
        self.Keys = params.get("Keys")
        self.Need = params.get("Need")


class DescribePolicyConditionListConfigManualStatType(AbstractModel):
    """DescribePolicyConditionList.ConfigManual.StatType

    """

    def __init__(self):
        """
        :param P5: 數據聚合方式，週期5秒
注意：此欄位可能返回 null，表示取不到有效值。
        :type P5: str
        :param P10: 數據聚合方式，週期10秒
注意：此欄位可能返回 null，表示取不到有效值。
        :type P10: str
        :param P60: 數據聚合方式，週期1分鍾
注意：此欄位可能返回 null，表示取不到有效值。
        :type P60: str
        :param P300: 數據聚合方式，週期5分鍾
注意：此欄位可能返回 null，表示取不到有效值。
        :type P300: str
        :param P600: 數據聚合方式，週期10分鍾
注意：此欄位可能返回 null，表示取不到有效值。
        :type P600: str
        :param P1800: 數據聚合方式，週期30分鍾
注意：此欄位可能返回 null，表示取不到有效值。
        :type P1800: str
        :param P3600: 數據聚合方式，週期1小時
注意：此欄位可能返回 null，表示取不到有效值。
        :type P3600: str
        :param P86400: 數據聚合方式，週期1天
注意：此欄位可能返回 null，表示取不到有效值。
        :type P86400: str
        """
        self.P5 = None
        self.P10 = None
        self.P60 = None
        self.P300 = None
        self.P600 = None
        self.P1800 = None
        self.P3600 = None
        self.P86400 = None


    def _deserialize(self, params):
        self.P5 = params.get("P5")
        self.P10 = params.get("P10")
        self.P60 = params.get("P60")
        self.P300 = params.get("P300")
        self.P600 = params.get("P600")
        self.P1800 = params.get("P1800")
        self.P3600 = params.get("P3600")
        self.P86400 = params.get("P86400")


class DescribePolicyConditionListEventMetric(AbstractModel):
    """DescribePolicyConditionList.EventMetric

    """

    def __init__(self):
        """
        :param EventId: 事件id
        :type EventId: int
        :param EventShowName: 事件名稱
        :type EventShowName: str
        :param NeedRecovered: 是否需要恢複
        :type NeedRecovered: bool
        :param Type: 事件類型，預留欄位，當前固定取值爲2
        :type Type: int
        """
        self.EventId = None
        self.EventShowName = None
        self.NeedRecovered = None
        self.Type = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.EventShowName = params.get("EventShowName")
        self.NeedRecovered = params.get("NeedRecovered")
        self.Type = params.get("Type")


class DescribePolicyConditionListMetric(AbstractModel):
    """指标告警配置

    """

    def __init__(self):
        """
        :param ConfigManual: 指标配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConfigManual: :class:`taifucloudcloud.monitor.v20180724.models.DescribePolicyConditionListConfigManual`
        :param MetricId: 指标id
        :type MetricId: int
        :param MetricShowName: 指标名稱
        :type MetricShowName: str
        :param MetricUnit: 指标單位
        :type MetricUnit: str
        """
        self.ConfigManual = None
        self.MetricId = None
        self.MetricShowName = None
        self.MetricUnit = None


    def _deserialize(self, params):
        if params.get("ConfigManual") is not None:
            self.ConfigManual = DescribePolicyConditionListConfigManual()
            self.ConfigManual._deserialize(params.get("ConfigManual"))
        self.MetricId = params.get("MetricId")
        self.MetricShowName = params.get("MetricShowName")
        self.MetricUnit = params.get("MetricUnit")


class DescribePolicyConditionListRequest(AbstractModel):
    """DescribePolicyConditionList請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 固定值，爲"monitor"
        :type Module: str
        """
        self.Module = None


    def _deserialize(self, params):
        self.Module = params.get("Module")


class DescribePolicyConditionListResponse(AbstractModel):
    """DescribePolicyConditionList返回參數結構體

    """

    def __init__(self):
        """
        :param Conditions: 告警策略條件清單
        :type Conditions: list of DescribePolicyConditionListCondition
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Conditions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = DescribePolicyConditionListCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePolicyGroupInfoCallback(AbstractModel):
    """查詢策略輸出的用戶回調訊息

    """

    def __init__(self):
        """
        :param CallbackUrl: 用戶回調介面網址
        :type CallbackUrl: str
        :param ValidFlag: 用戶回調介面狀态，0表示未驗證，1表示已驗證，2表示存在url但沒有通過驗證
        :type ValidFlag: int
        :param VerifyCode: 用戶回調介面驗證碼
        :type VerifyCode: str
        """
        self.CallbackUrl = None
        self.ValidFlag = None
        self.VerifyCode = None


    def _deserialize(self, params):
        self.CallbackUrl = params.get("CallbackUrl")
        self.ValidFlag = params.get("ValidFlag")
        self.VerifyCode = params.get("VerifyCode")


class DescribePolicyGroupInfoCondition(AbstractModel):
    """查詢策略輸出的阈值告警條件

    """

    def __init__(self):
        """
        :param MetricShowName: 指标名稱
        :type MetricShowName: str
        :param Period: 數據聚合週期(單位秒)
        :type Period: int
        :param MetricId: 指标id
        :type MetricId: int
        :param RuleId: 阈值規則id
        :type RuleId: int
        :param Unit: 指标單位
        :type Unit: str
        :param AlarmNotifyType: 告警發送收斂類型。0連續告警，1指數告警
        :type AlarmNotifyType: int
        :param AlarmNotifyPeriod: 告警發送週期單位秒。<0 不觸發, 0 只觸發一次, >0 每隔triggerTime秒觸發一次
        :type AlarmNotifyPeriod: int
        :param CalcType: 比較類型，1表示大于，2表示大于等于，3表示小於，4表示小於等于，5表示相等，6表示不相等，7表示日同比上漲，8表示日同比下降，9表示周同比上漲，10表示周同比下降，11表示週期環比上漲，12表示週期環比下降
注意：此欄位可能返回 null，表示取不到有效值。
        :type CalcType: int
        :param CalcValue: 檢測阈值
注意：此欄位可能返回 null，表示取不到有效值。
        :type CalcValue: str
        :param ContinueTime: 持續多長時間觸發規則會告警(單位秒)
注意：此欄位可能返回 null，表示取不到有效值。
        :type ContinueTime: int
        """
        self.MetricShowName = None
        self.Period = None
        self.MetricId = None
        self.RuleId = None
        self.Unit = None
        self.AlarmNotifyType = None
        self.AlarmNotifyPeriod = None
        self.CalcType = None
        self.CalcValue = None
        self.ContinueTime = None


    def _deserialize(self, params):
        self.MetricShowName = params.get("MetricShowName")
        self.Period = params.get("Period")
        self.MetricId = params.get("MetricId")
        self.RuleId = params.get("RuleId")
        self.Unit = params.get("Unit")
        self.AlarmNotifyType = params.get("AlarmNotifyType")
        self.AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self.CalcType = params.get("CalcType")
        self.CalcValue = params.get("CalcValue")
        self.ContinueTime = params.get("ContinueTime")


class DescribePolicyGroupInfoConditionTpl(AbstractModel):
    """查詢策略輸出的範本策略組訊息

    """

    def __init__(self):
        """
        :param GroupId: 策略組id
        :type GroupId: int
        :param GroupName: 策略組名稱
        :type GroupName: str
        :param ViewName: 策略類型
        :type ViewName: str
        :param Remark: 策略組說明
        :type Remark: str
        :param LastEditUin: 最後編輯的用戶uin
        :type LastEditUin: str
        :param UpdateTime: 更新時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param InsertTime: 創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type InsertTime: int
        :param IsUnionRule: 是否且規則
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsUnionRule: int
        """
        self.GroupId = None
        self.GroupName = None
        self.ViewName = None
        self.Remark = None
        self.LastEditUin = None
        self.UpdateTime = None
        self.InsertTime = None
        self.IsUnionRule = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.ViewName = params.get("ViewName")
        self.Remark = params.get("Remark")
        self.LastEditUin = params.get("LastEditUin")
        self.UpdateTime = params.get("UpdateTime")
        self.InsertTime = params.get("InsertTime")
        self.IsUnionRule = params.get("IsUnionRule")


class DescribePolicyGroupInfoEventCondition(AbstractModel):
    """查詢策略輸出的事件告警條件

    """

    def __init__(self):
        """
        :param EventId: 事件id
        :type EventId: int
        :param RuleId: 事件告警規則id
        :type RuleId: int
        :param EventShowName: 事件名稱
        :type EventShowName: str
        :param AlarmNotifyPeriod: 告警發送週期單位秒。<0 不觸發, 0 只觸發一次, >0 每隔triggerTime秒觸發一次
        :type AlarmNotifyPeriod: int
        :param AlarmNotifyType: 告警發送收斂類型。0連續告警，1指數告警
        :type AlarmNotifyType: int
        """
        self.EventId = None
        self.RuleId = None
        self.EventShowName = None
        self.AlarmNotifyPeriod = None
        self.AlarmNotifyType = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.RuleId = params.get("RuleId")
        self.EventShowName = params.get("EventShowName")
        self.AlarmNotifyPeriod = params.get("AlarmNotifyPeriod")
        self.AlarmNotifyType = params.get("AlarmNotifyType")


class DescribePolicyGroupInfoReceiverInfo(AbstractModel):
    """查詢策略輸出的告警接收人訊息

    """

    def __init__(self):
        """
        :param ReceiverGroupList: 告警接收組id清單
        :type ReceiverGroupList: list of int
        :param ReceiverUserList: 告警接收人id清單
        :type ReceiverUserList: list of int
        :param StartTime: 告警時間段開始時間。範圍[0,86400)，作爲unix時間戳轉成 時間後去掉日期，例如7200表示"10:0:0"
        :type StartTime: int
        :param EndTime: 告警時間段結束時間。含義同StartTime
        :type EndTime: int
        :param ReceiverType: 接收類型。“group”(接收組)或“user”(接收人)
        :type ReceiverType: str
        :param NotifyWay: 告警通知方式。可選 "SMS","SITE","EMAIL","CALL","WECHAT"
        :type NotifyWay: list of str
        :param UidList: 電話告警接收者uid
注意：此欄位可能返回 null，表示取不到有效值。
        :type UidList: list of int
        :param RoundNumber: 電話告警輪數
        :type RoundNumber: int
        :param RoundInterval: 電話告警每輪間隔（秒）
        :type RoundInterval: int
        :param PersonInterval: 電話告警對個人間隔（秒）
        :type PersonInterval: int
        :param NeedSendNotice: 是否需要電話告警觸達提示。0不需要，1需要
        :type NeedSendNotice: int
        :param SendFor: 電話告警通知時機。可選"OCCUR"(告警時通知),"RECOVER"(恢複時通知)
        :type SendFor: list of str
        :param RecoverNotify: 恢複通知方式。可選"SMS"
        :type RecoverNotify: list of str
        :param ReceiveLanguage: 告警發送語言
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReceiveLanguage: str
        """
        self.ReceiverGroupList = None
        self.ReceiverUserList = None
        self.StartTime = None
        self.EndTime = None
        self.ReceiverType = None
        self.NotifyWay = None
        self.UidList = None
        self.RoundNumber = None
        self.RoundInterval = None
        self.PersonInterval = None
        self.NeedSendNotice = None
        self.SendFor = None
        self.RecoverNotify = None
        self.ReceiveLanguage = None


    def _deserialize(self, params):
        self.ReceiverGroupList = params.get("ReceiverGroupList")
        self.ReceiverUserList = params.get("ReceiverUserList")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ReceiverType = params.get("ReceiverType")
        self.NotifyWay = params.get("NotifyWay")
        self.UidList = params.get("UidList")
        self.RoundNumber = params.get("RoundNumber")
        self.RoundInterval = params.get("RoundInterval")
        self.PersonInterval = params.get("PersonInterval")
        self.NeedSendNotice = params.get("NeedSendNotice")
        self.SendFor = params.get("SendFor")
        self.RecoverNotify = params.get("RecoverNotify")
        self.ReceiveLanguage = params.get("ReceiveLanguage")


class DescribePolicyGroupInfoRequest(AbstractModel):
    """DescribePolicyGroupInfo請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 固定值，爲"monitor"
        :type Module: str
        :param GroupId: 策略組id
        :type GroupId: int
        """
        self.Module = None
        self.GroupId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.GroupId = params.get("GroupId")


class DescribePolicyGroupInfoResponse(AbstractModel):
    """DescribePolicyGroupInfo返回參數結構體

    """

    def __init__(self):
        """
        :param GroupName: 策略組名稱
        :type GroupName: str
        :param ProjectId: 策略組所屬的項目id
        :type ProjectId: int
        :param IsDefault: 是否爲預設策略，0表示非預設策略，1表示預設策略
        :type IsDefault: int
        :param ViewName: 策略類型
        :type ViewName: str
        :param Remark: 策略說明
        :type Remark: str
        :param ShowName: 策略類型名稱
        :type ShowName: str
        :param LastEditUin: 最近編輯的用戶uin
        :type LastEditUin: str
        :param UpdateTime: 最近編輯時間
        :type UpdateTime: str
        :param Region: 該策略支援的地域
        :type Region: list of str
        :param DimensionGroup: 策略類型的維度清單
        :type DimensionGroup: list of str
        :param ConditionsConfig: 阈值規則清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConditionsConfig: list of DescribePolicyGroupInfoCondition
        :param EventConfig: 産品事件規則清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type EventConfig: list of DescribePolicyGroupInfoEventCondition
        :param ReceiverInfos: 用戶接收人清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReceiverInfos: list of DescribePolicyGroupInfoReceiverInfo
        :param Callback: 用戶回調訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Callback: :class:`taifucloudcloud.monitor.v20180724.models.DescribePolicyGroupInfoCallback`
        :param ConditionsTemp: 範本策略組
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConditionsTemp: :class:`taifucloudcloud.monitor.v20180724.models.DescribePolicyGroupInfoConditionTpl`
        :param CanSetDefault: 是否可以設置成預設策略
        :type CanSetDefault: bool
        :param IsUnionRule: 是否且規則
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsUnionRule: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.GroupName = None
        self.ProjectId = None
        self.IsDefault = None
        self.ViewName = None
        self.Remark = None
        self.ShowName = None
        self.LastEditUin = None
        self.UpdateTime = None
        self.Region = None
        self.DimensionGroup = None
        self.ConditionsConfig = None
        self.EventConfig = None
        self.ReceiverInfos = None
        self.Callback = None
        self.ConditionsTemp = None
        self.CanSetDefault = None
        self.IsUnionRule = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.ProjectId = params.get("ProjectId")
        self.IsDefault = params.get("IsDefault")
        self.ViewName = params.get("ViewName")
        self.Remark = params.get("Remark")
        self.ShowName = params.get("ShowName")
        self.LastEditUin = params.get("LastEditUin")
        self.UpdateTime = params.get("UpdateTime")
        self.Region = params.get("Region")
        self.DimensionGroup = params.get("DimensionGroup")
        if params.get("ConditionsConfig") is not None:
            self.ConditionsConfig = []
            for item in params.get("ConditionsConfig"):
                obj = DescribePolicyGroupInfoCondition()
                obj._deserialize(item)
                self.ConditionsConfig.append(obj)
        if params.get("EventConfig") is not None:
            self.EventConfig = []
            for item in params.get("EventConfig"):
                obj = DescribePolicyGroupInfoEventCondition()
                obj._deserialize(item)
                self.EventConfig.append(obj)
        if params.get("ReceiverInfos") is not None:
            self.ReceiverInfos = []
            for item in params.get("ReceiverInfos"):
                obj = DescribePolicyGroupInfoReceiverInfo()
                obj._deserialize(item)
                self.ReceiverInfos.append(obj)
        if params.get("Callback") is not None:
            self.Callback = DescribePolicyGroupInfoCallback()
            self.Callback._deserialize(params.get("Callback"))
        if params.get("ConditionsTemp") is not None:
            self.ConditionsTemp = DescribePolicyGroupInfoConditionTpl()
            self.ConditionsTemp._deserialize(params.get("ConditionsTemp"))
        self.CanSetDefault = params.get("CanSetDefault")
        self.IsUnionRule = params.get("IsUnionRule")
        self.RequestId = params.get("RequestId")


class DescribePolicyGroupListGroup(AbstractModel):
    """DescribePolicyGroupList.Group

    """

    def __init__(self):
        """
        :param GroupId: 策略組id
        :type GroupId: int
        :param GroupName: 策略組名稱
        :type GroupName: str
        :param IsOpen: 是否開啓
        :type IsOpen: bool
        :param ViewName: 策略視圖名稱
        :type ViewName: str
        :param LastEditUin: 最近編輯的用戶uin
        :type LastEditUin: str
        :param UpdateTime: 最後修改時間
        :type UpdateTime: int
        :param InsertTime: 創建時間
        :type InsertTime: int
        :param UseSum: 策略組綁定的實例數
        :type UseSum: int
        :param NoShieldedSum: 策略組綁定的未屏蔽實例數
        :type NoShieldedSum: int
        :param IsDefault: 是否爲預設策略，0表示非預設策略，1表示預設策略
        :type IsDefault: int
        :param CanSetDefault: 是否可以設置成預設策略
        :type CanSetDefault: bool
        :param ParentGroupId: 父策略組id
        :type ParentGroupId: int
        :param Remark: 策略組備注
        :type Remark: str
        :param ProjectId: 策略組所屬項目id
        :type ProjectId: int
        :param Conditions: 阈值規則清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Conditions: list of DescribePolicyGroupInfoCondition
        :param EventConditions: 産品事件規則清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type EventConditions: list of DescribePolicyGroupInfoEventCondition
        :param ReceiverInfos: 用戶接收人清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReceiverInfos: list of DescribePolicyGroupInfoReceiverInfo
        :param ConditionsTemp: 範本策略組
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConditionsTemp: :class:`taifucloudcloud.monitor.v20180724.models.DescribePolicyGroupInfoConditionTpl`
        :param InstanceGroup: 策略組綁定的實例組訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceGroup: :class:`taifucloudcloud.monitor.v20180724.models.DescribePolicyGroupListGroupInstanceGroup`
        :param IsUnionRule: 且或規則标識, 0表示或規則(任意一條規則滿足阈值條件就告警), 1表示且規則(所有規則都滿足阈值條件才告警)
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsUnionRule: int
        """
        self.GroupId = None
        self.GroupName = None
        self.IsOpen = None
        self.ViewName = None
        self.LastEditUin = None
        self.UpdateTime = None
        self.InsertTime = None
        self.UseSum = None
        self.NoShieldedSum = None
        self.IsDefault = None
        self.CanSetDefault = None
        self.ParentGroupId = None
        self.Remark = None
        self.ProjectId = None
        self.Conditions = None
        self.EventConditions = None
        self.ReceiverInfos = None
        self.ConditionsTemp = None
        self.InstanceGroup = None
        self.IsUnionRule = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.IsOpen = params.get("IsOpen")
        self.ViewName = params.get("ViewName")
        self.LastEditUin = params.get("LastEditUin")
        self.UpdateTime = params.get("UpdateTime")
        self.InsertTime = params.get("InsertTime")
        self.UseSum = params.get("UseSum")
        self.NoShieldedSum = params.get("NoShieldedSum")
        self.IsDefault = params.get("IsDefault")
        self.CanSetDefault = params.get("CanSetDefault")
        self.ParentGroupId = params.get("ParentGroupId")
        self.Remark = params.get("Remark")
        self.ProjectId = params.get("ProjectId")
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = DescribePolicyGroupInfoCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)
        if params.get("EventConditions") is not None:
            self.EventConditions = []
            for item in params.get("EventConditions"):
                obj = DescribePolicyGroupInfoEventCondition()
                obj._deserialize(item)
                self.EventConditions.append(obj)
        if params.get("ReceiverInfos") is not None:
            self.ReceiverInfos = []
            for item in params.get("ReceiverInfos"):
                obj = DescribePolicyGroupInfoReceiverInfo()
                obj._deserialize(item)
                self.ReceiverInfos.append(obj)
        if params.get("ConditionsTemp") is not None:
            self.ConditionsTemp = DescribePolicyGroupInfoConditionTpl()
            self.ConditionsTemp._deserialize(params.get("ConditionsTemp"))
        if params.get("InstanceGroup") is not None:
            self.InstanceGroup = DescribePolicyGroupListGroupInstanceGroup()
            self.InstanceGroup._deserialize(params.get("InstanceGroup"))
        self.IsUnionRule = params.get("IsUnionRule")


class DescribePolicyGroupListGroupInstanceGroup(AbstractModel):
    """DescribePolicyGroupList介面策略組綁定的實例分組訊息

    """

    def __init__(self):
        """
        :param InstanceGroupId: 實例分組名稱id
        :type InstanceGroupId: int
        :param ViewName: 策略類型視圖名稱
        :type ViewName: str
        :param LastEditUin: 最近編輯的用戶uin
        :type LastEditUin: str
        :param GroupName: 實例分組名稱
        :type GroupName: str
        :param InstanceSum: 實例數量
        :type InstanceSum: int
        :param UpdateTime: 更新時間
        :type UpdateTime: int
        :param InsertTime: 創建時間
        :type InsertTime: int
        """
        self.InstanceGroupId = None
        self.ViewName = None
        self.LastEditUin = None
        self.GroupName = None
        self.InstanceSum = None
        self.UpdateTime = None
        self.InsertTime = None


    def _deserialize(self, params):
        self.InstanceGroupId = params.get("InstanceGroupId")
        self.ViewName = params.get("ViewName")
        self.LastEditUin = params.get("LastEditUin")
        self.GroupName = params.get("GroupName")
        self.InstanceSum = params.get("InstanceSum")
        self.UpdateTime = params.get("UpdateTime")
        self.InsertTime = params.get("InsertTime")


class DescribePolicyGroupListRequest(AbstractModel):
    """DescribePolicyGroupList請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 固定值，爲"monitor"
        :type Module: str
        :param Limit: 分頁參數，每頁返回的數量，取值1~100
        :type Limit: int
        :param Offset: 分頁參數，頁偏移量，從0開始計數
        :type Offset: int
        :param Like: 按策略名搜索
        :type Like: str
        :param InstanceGroupId: 實例分組id
        :type InstanceGroupId: int
        :param UpdateTimeOrder: 按更新時間排序, asc 或者 desc
        :type UpdateTimeOrder: str
        :param ProjectIds: 項目id清單
        :type ProjectIds: list of int
        :param ViewNames: 告警策略類型清單
        :type ViewNames: list of str
        :param FilterUnuseReceiver: 是否過濾無接收人策略組, 1表示過濾, 0表示不過濾
        :type FilterUnuseReceiver: int
        :param Receivers: 過濾條件, 接收組清單
        :type Receivers: list of str
        :param ReceiverUserList: 過濾條件, 接收人清單
        :type ReceiverUserList: list of str
        :param Dimensions: 維度組合欄位(json字串), 例如[[{"name":"unInstanceId","value":"ins-6e4b2aaa"}]]
        :type Dimensions: str
        :param ConditionTempGroupId: 範本策略組id, 多個id用逗号分隔
        :type ConditionTempGroupId: str
        :param ReceiverType: 過濾條件, 接收人或者接收組, user表示接收人, group表示接收組
        :type ReceiverType: str
        """
        self.Module = None
        self.Limit = None
        self.Offset = None
        self.Like = None
        self.InstanceGroupId = None
        self.UpdateTimeOrder = None
        self.ProjectIds = None
        self.ViewNames = None
        self.FilterUnuseReceiver = None
        self.Receivers = None
        self.ReceiverUserList = None
        self.Dimensions = None
        self.ConditionTempGroupId = None
        self.ReceiverType = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Like = params.get("Like")
        self.InstanceGroupId = params.get("InstanceGroupId")
        self.UpdateTimeOrder = params.get("UpdateTimeOrder")
        self.ProjectIds = params.get("ProjectIds")
        self.ViewNames = params.get("ViewNames")
        self.FilterUnuseReceiver = params.get("FilterUnuseReceiver")
        self.Receivers = params.get("Receivers")
        self.ReceiverUserList = params.get("ReceiverUserList")
        self.Dimensions = params.get("Dimensions")
        self.ConditionTempGroupId = params.get("ConditionTempGroupId")
        self.ReceiverType = params.get("ReceiverType")


class DescribePolicyGroupListResponse(AbstractModel):
    """DescribePolicyGroupList返回參數結構體

    """

    def __init__(self):
        """
        :param GroupList: 策略組清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupList: list of DescribePolicyGroupListGroup
        :param Total: 策略組總數
        :type Total: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.GroupList = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GroupList") is not None:
            self.GroupList = []
            for item in params.get("GroupList"):
                obj = DescribePolicyGroupListGroup()
                obj._deserialize(item)
                self.GroupList.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeProductEventListDimensions(AbstractModel):
    """DescribeProductEventList的入參Dimensions

    """

    def __init__(self):
        """
        :param Name: 維度名
        :type Name: str
        :param Value: 維度值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class DescribeProductEventListEvents(AbstractModel):
    """DescribeProductEventList返回的Events

    """

    def __init__(self):
        """
        :param EventId: 事件ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type EventId: int
        :param EventCName: 事件中文名
注意：此欄位可能返回 null，表示取不到有效值。
        :type EventCName: str
        :param EventEName: 事件英文名
注意：此欄位可能返回 null，表示取不到有效值。
        :type EventEName: str
        :param EventName: 事件簡稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type EventName: str
        :param ProductCName: 産品中文名
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProductCName: str
        :param ProductEName: 産品英文名
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProductEName: str
        :param ProductName: 産品簡稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param InstanceId: 實例ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param InstanceName: 實例名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param ProjectId: 項目ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param Region: 地域
注意：此欄位可能返回 null，表示取不到有效值。
        :type Region: str
        :param Status: 狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: str
        :param SupportAlarm: 是否支援告警
注意：此欄位可能返回 null，表示取不到有效值。
        :type SupportAlarm: int
        :param Type: 事件類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type Type: str
        :param StartTime: 開始時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type StartTime: int
        :param UpdateTime: 更新時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param Dimensions: 實例對象訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Dimensions: list of DescribeProductEventListEventsDimensions
        :param AdditionMsg: 實例對象附加訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type AdditionMsg: list of DescribeProductEventListEventsDimensions
        :param IsAlarmConfig: 是否配置告警
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsAlarmConfig: int
        :param GroupInfo: 策略訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupInfo: list of DescribeProductEventListEventsGroupInfo
        """
        self.EventId = None
        self.EventCName = None
        self.EventEName = None
        self.EventName = None
        self.ProductCName = None
        self.ProductEName = None
        self.ProductName = None
        self.InstanceId = None
        self.InstanceName = None
        self.ProjectId = None
        self.Region = None
        self.Status = None
        self.SupportAlarm = None
        self.Type = None
        self.StartTime = None
        self.UpdateTime = None
        self.Dimensions = None
        self.AdditionMsg = None
        self.IsAlarmConfig = None
        self.GroupInfo = None


    def _deserialize(self, params):
        self.EventId = params.get("EventId")
        self.EventCName = params.get("EventCName")
        self.EventEName = params.get("EventEName")
        self.EventName = params.get("EventName")
        self.ProductCName = params.get("ProductCName")
        self.ProductEName = params.get("ProductEName")
        self.ProductName = params.get("ProductName")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.ProjectId = params.get("ProjectId")
        self.Region = params.get("Region")
        self.Status = params.get("Status")
        self.SupportAlarm = params.get("SupportAlarm")
        self.Type = params.get("Type")
        self.StartTime = params.get("StartTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = DescribeProductEventListEventsDimensions()
                obj._deserialize(item)
                self.Dimensions.append(obj)
        if params.get("AdditionMsg") is not None:
            self.AdditionMsg = []
            for item in params.get("AdditionMsg"):
                obj = DescribeProductEventListEventsDimensions()
                obj._deserialize(item)
                self.AdditionMsg.append(obj)
        self.IsAlarmConfig = params.get("IsAlarmConfig")
        if params.get("GroupInfo") is not None:
            self.GroupInfo = []
            for item in params.get("GroupInfo"):
                obj = DescribeProductEventListEventsGroupInfo()
                obj._deserialize(item)
                self.GroupInfo.append(obj)


class DescribeProductEventListEventsDimensions(AbstractModel):
    """DescribeProductEventList返回的Events的Dimensions

    """

    def __init__(self):
        """
        :param Key: 維度名（英文）
注意：此欄位可能返回 null，表示取不到有效值。
        :type Key: str
        :param Name: 維度名（中文）
注意：此欄位可能返回 null，表示取不到有效值。
        :type Name: str
        :param Value: 維度值
注意：此欄位可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Key = None
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class DescribeProductEventListEventsGroupInfo(AbstractModel):
    """DescribeProductEventList返回的Events裏的GroupInfo

    """

    def __init__(self):
        """
        :param GroupId: 策略ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupId: int
        :param GroupName: 策略名
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupName: str
        """
        self.GroupId = None
        self.GroupName = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")


class DescribeProductEventListOverView(AbstractModel):
    """DescribeProductEventList返回的OverView對象

    """

    def __init__(self):
        """
        :param StatusChangeAmount: 狀态變更的事件數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type StatusChangeAmount: int
        :param UnConfigAlarmAmount: 告警狀态未配置的事件數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type UnConfigAlarmAmount: int
        :param UnNormalEventAmount: 異常事件數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type UnNormalEventAmount: int
        :param UnRecoverAmount: 未恢複的事件數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type UnRecoverAmount: int
        """
        self.StatusChangeAmount = None
        self.UnConfigAlarmAmount = None
        self.UnNormalEventAmount = None
        self.UnRecoverAmount = None


    def _deserialize(self, params):
        self.StatusChangeAmount = params.get("StatusChangeAmount")
        self.UnConfigAlarmAmount = params.get("UnConfigAlarmAmount")
        self.UnNormalEventAmount = params.get("UnNormalEventAmount")
        self.UnRecoverAmount = params.get("UnRecoverAmount")


class DescribeProductEventListRequest(AbstractModel):
    """DescribeProductEventList請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 介面模組名，固定值"monitor"
        :type Module: str
        :param ProductName: 産品類型過濾，比如"cvm"表示雲伺服器
        :type ProductName: list of str
        :param EventName: 事件名稱過濾，比如"guest_reboot"表示機器重啓
        :type EventName: list of str
        :param InstanceId: 影響對象，比如ins-19708ino
        :type InstanceId: list of str
        :param Dimensions: 維度過濾，比如外網IP:10.0.0.1
        :type Dimensions: list of DescribeProductEventListDimensions
        :param RegionList: 地域過濾，比如gz
        :type RegionList: list of str
        :param Type: 事件類型過濾，取值範圍["status_change","abnormal"]，分别表示狀态變更、異常事件
        :type Type: list of str
        :param Status: 事件狀态過濾，取值範圍["recover","alarm","-"]，分别表示已恢複、未恢複、無狀态
        :type Status: list of str
        :param Project: 項目ID過濾
        :type Project: list of str
        :param IsAlarmConfig: 告警狀态配置過濾，1表示已配置，0表示未配置
        :type IsAlarmConfig: int
        :param TimeOrder: 按更新時間排序，ASC表示升序，DESC表示降序，預設DESC
        :type TimeOrder: str
        :param StartTime: 起始時間，預設一天前的時間戳
        :type StartTime: int
        :param EndTime: 結束時間，預設當前時間戳
        :type EndTime: int
        :param Offset: 頁偏移量，預設0
        :type Offset: int
        :param Limit: 每頁返回的數量，預設20
        :type Limit: int
        """
        self.Module = None
        self.ProductName = None
        self.EventName = None
        self.InstanceId = None
        self.Dimensions = None
        self.RegionList = None
        self.Type = None
        self.Status = None
        self.Project = None
        self.IsAlarmConfig = None
        self.TimeOrder = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.ProductName = params.get("ProductName")
        self.EventName = params.get("EventName")
        self.InstanceId = params.get("InstanceId")
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = DescribeProductEventListDimensions()
                obj._deserialize(item)
                self.Dimensions.append(obj)
        self.RegionList = params.get("RegionList")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.Project = params.get("Project")
        self.IsAlarmConfig = params.get("IsAlarmConfig")
        self.TimeOrder = params.get("TimeOrder")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeProductEventListResponse(AbstractModel):
    """DescribeProductEventList返回參數結構體

    """

    def __init__(self):
        """
        :param Events: 事件清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Events: list of DescribeProductEventListEvents
        :param OverView: 事件統計
        :type OverView: :class:`taifucloudcloud.monitor.v20180724.models.DescribeProductEventListOverView`
        :param Total: 事件總數
注意：此欄位可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Events = None
        self.OverView = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Events") is not None:
            self.Events = []
            for item in params.get("Events"):
                obj = DescribeProductEventListEvents()
                obj._deserialize(item)
                self.Events.append(obj)
        if params.get("OverView") is not None:
            self.OverView = DescribeProductEventListOverView()
            self.OverView._deserialize(params.get("OverView"))
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class Dimension(AbstractModel):
    """實例對象的維度組合

    """

    def __init__(self):
        """
        :param Name: 實例維度名稱
        :type Name: str
        :param Value: 實例維度值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class DimensionsDesc(AbstractModel):
    """維度訊息

    """

    def __init__(self):
        """
        :param Dimensions: 維度名數組
        :type Dimensions: list of str
        """
        self.Dimensions = None


    def _deserialize(self, params):
        self.Dimensions = params.get("Dimensions")


class GetMonitorDataRequest(AbstractModel):
    """GetMonitorData請求參數結構體

    """

    def __init__(self):
        """
        :param Namespace: 命名空間，每個雲産品會有一個命名空間
        :type Namespace: str
        :param MetricName: 指标名稱，各個雲産品的詳細指标說明請參閱各個産品[監控介面](https://cloud.taifucloud.com/document/product/248/30384)文件
        :type MetricName: str
        :param Instances: 實例對象的維度組合
        :type Instances: list of Instance
        :param Period: 監控統計週期。預設爲取值爲300，單位爲s
        :type Period: int
        :param StartTime: 起始時間，如2018-09-22T19:51:23+08:00
        :type StartTime: str
        :param EndTime: 結束時間，預設爲當前時間。 EndTime不能小於StartTime
        :type EndTime: str
        """
        self.Namespace = None
        self.MetricName = None
        self.Instances = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.MetricName = params.get("MetricName")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = Instance()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class GetMonitorDataResponse(AbstractModel):
    """GetMonitorData返回參數結構體

    """

    def __init__(self):
        """
        :param Period: 統計週期
        :type Period: int
        :param MetricName: 指标名
        :type MetricName: str
        :param DataPoints: 數據點數組
        :type DataPoints: list of DataPoint
        :param StartTime: 開始時間
        :type StartTime: str
        :param EndTime: 結束時間
        :type EndTime: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Period = None
        self.MetricName = None
        self.DataPoints = None
        self.StartTime = None
        self.EndTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.MetricName = params.get("MetricName")
        if params.get("DataPoints") is not None:
            self.DataPoints = []
            for item in params.get("DataPoints"):
                obj = DataPoint()
                obj._deserialize(item)
                self.DataPoints.append(obj)
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.RequestId = params.get("RequestId")


class Instance(AbstractModel):
    """實例維度組合數組

    """

    def __init__(self):
        """
        :param Dimensions: 實例的維度組合
        :type Dimensions: list of Dimension
        """
        self.Dimensions = None


    def _deserialize(self, params):
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = Dimension()
                obj._deserialize(item)
                self.Dimensions.append(obj)


class InstanceGroup(AbstractModel):
    """DescribeBasicAlarmList返回的Alarms裏的InstanceGroup

    """

    def __init__(self):
        """
        :param InstanceGroupId: 實例組ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceGroupId: int
        :param InstanceGroupName: 實例組名
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceGroupName: str
        """
        self.InstanceGroupId = None
        self.InstanceGroupName = None


    def _deserialize(self, params):
        self.InstanceGroupId = params.get("InstanceGroupId")
        self.InstanceGroupName = params.get("InstanceGroupName")


class MetricDatum(AbstractModel):
    """指标名稱和值的封裝

    """

    def __init__(self):
        """
        :param MetricName: 指标名稱
        :type MetricName: str
        :param Value: 指标的值
        :type Value: int
        """
        self.MetricName = None
        self.Value = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        self.Value = params.get("Value")


class MetricObjectMeaning(AbstractModel):
    """指标數據的解釋

    """

    def __init__(self):
        """
        :param En: 指标英文解釋
        :type En: str
        :param Zh: 指标中文解釋
        :type Zh: str
        """
        self.En = None
        self.Zh = None


    def _deserialize(self, params):
        self.En = params.get("En")
        self.Zh = params.get("Zh")


class MetricSet(AbstractModel):
    """對業務指标的單位及支援統計週期的描述

    """

    def __init__(self):
        """
        :param Namespace: 命名空間，每個雲産品會有一個命名空間
        :type Namespace: str
        :param MetricName: 指标名稱
        :type MetricName: str
        :param Unit: 指标使用的單位
        :type Unit: str
        :param UnitCname: 指标使用的單位
        :type UnitCname: str
        :param Period: 指标支援的統計週期，單位是秒，如60、300
        :type Period: list of int
        :param Periods: 統計週期内指标方式
        :type Periods: list of PeriodsSt
        :param Meaning: 統計指标含義解釋
        :type Meaning: :class:`taifucloudcloud.monitor.v20180724.models.MetricObjectMeaning`
        :param Dimensions: 維度描述訊息
        :type Dimensions: list of DimensionsDesc
        """
        self.Namespace = None
        self.MetricName = None
        self.Unit = None
        self.UnitCname = None
        self.Period = None
        self.Periods = None
        self.Meaning = None
        self.Dimensions = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.MetricName = params.get("MetricName")
        self.Unit = params.get("Unit")
        self.UnitCname = params.get("UnitCname")
        self.Period = params.get("Period")
        if params.get("Periods") is not None:
            self.Periods = []
            for item in params.get("Periods"):
                obj = PeriodsSt()
                obj._deserialize(item)
                self.Periods.append(obj)
        if params.get("Meaning") is not None:
            self.Meaning = MetricObjectMeaning()
            self.Meaning._deserialize(params.get("Meaning"))
        if params.get("Dimensions") is not None:
            self.Dimensions = []
            for item in params.get("Dimensions"):
                obj = DimensionsDesc()
                obj._deserialize(item)
                self.Dimensions.append(obj)


class ModifyAlarmReceiversRequest(AbstractModel):
    """ModifyAlarmReceivers請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 需要修改接收人的策略組Id
        :type GroupId: int
        :param Module: 必填。固定爲“monitor”
        :type Module: str
        :param ReceiverInfos: 新接收人訊息, 沒有填寫則删除所有接收人
        :type ReceiverInfos: list of ReceiverInfo
        """
        self.GroupId = None
        self.Module = None
        self.ReceiverInfos = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Module = params.get("Module")
        if params.get("ReceiverInfos") is not None:
            self.ReceiverInfos = []
            for item in params.get("ReceiverInfos"):
                obj = ReceiverInfo()
                obj._deserialize(item)
                self.ReceiverInfos.append(obj)


class ModifyAlarmReceiversResponse(AbstractModel):
    """ModifyAlarmReceivers返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PeriodsSt(AbstractModel):
    """週期内的統計方式

    """

    def __init__(self):
        """
        :param Period: 周期
        :type Period: str
        :param StatType: 統計方式
        :type StatType: list of str
        """
        self.Period = None
        self.StatType = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.StatType = params.get("StatType")


class PutMonitorDataRequest(AbstractModel):
    """PutMonitorData請求參數結構體

    """

    def __init__(self):
        """
        :param Metrics: 一組指标和數據
        :type Metrics: list of MetricDatum
        :param AnnounceIp: 上報時自行指定的 IP
        :type AnnounceIp: str
        :param AnnounceTimestamp: 上報時自行指定的時間戳
        :type AnnounceTimestamp: int
        :param AnnounceInstance: 上報時自行指定的 IP 或 産品實例ID
        :type AnnounceInstance: str
        """
        self.Metrics = None
        self.AnnounceIp = None
        self.AnnounceTimestamp = None
        self.AnnounceInstance = None


    def _deserialize(self, params):
        if params.get("Metrics") is not None:
            self.Metrics = []
            for item in params.get("Metrics"):
                obj = MetricDatum()
                obj._deserialize(item)
                self.Metrics.append(obj)
        self.AnnounceIp = params.get("AnnounceIp")
        self.AnnounceTimestamp = params.get("AnnounceTimestamp")
        self.AnnounceInstance = params.get("AnnounceInstance")


class PutMonitorDataResponse(AbstractModel):
    """PutMonitorData返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReceiverInfo(AbstractModel):
    """接收人訊息

    """

    def __init__(self):
        """
        :param StartTime: 告警時間段開始時間。範圍[0,86400)，作爲unix時間戳轉成 時間後去掉日期，例如7200表示"10:0:0"
        :type StartTime: int
        :param EndTime: 告警時間段結束時間。含義同StartTime
        :type EndTime: int
        :param NotifyWay: 告警通知方式。可選 "SMS","SITE","EMAIL","CALL","WECHAT"
        :type NotifyWay: list of str
        :param ReceiverType: 接收人類型。“group” 或 “user”
        :type ReceiverType: list of str
        :param Id: Id
        :type Id: int
        :param SendFor: 電話告警通知時機。可選"OCCUR"(告警時通知),"RECOVER"(恢複時通知)
        :type SendFor: list of str
        :param UidList: 電話告警接收者uid
        :type UidList: list of int
        :param RoundNumber: 電話告警輪數
        :type RoundNumber: int
        :param PersonInterval: 電話告警對個人間隔（秒）
        :type PersonInterval: int
        :param RoundInterval: 電話告警每輪間隔（秒）
        :type RoundInterval: int
        :param RecoverNotify: 恢複通知方式。可選"SMS"
        :type RecoverNotify: list of str
        :param NeedSendNotice: 是否需要電話告警觸達提示。0不需要，1需要
        :type NeedSendNotice: int
        :param ReceiverGroupList: 接收組清單。通過平台介面查詢到的接收組id清單
        :type ReceiverGroupList: list of int
        :param ReceiverUserList: 接收人清單。通過平台介面查詢到的接收人id清單
        :type ReceiverUserList: list of int
        :param ReceiveLanguage: 告警接收語言，列舉值（zh-CN，en-US）
        :type ReceiveLanguage: str
        """
        self.StartTime = None
        self.EndTime = None
        self.NotifyWay = None
        self.ReceiverType = None
        self.Id = None
        self.SendFor = None
        self.UidList = None
        self.RoundNumber = None
        self.PersonInterval = None
        self.RoundInterval = None
        self.RecoverNotify = None
        self.NeedSendNotice = None
        self.ReceiverGroupList = None
        self.ReceiverUserList = None
        self.ReceiveLanguage = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.NotifyWay = params.get("NotifyWay")
        self.ReceiverType = params.get("ReceiverType")
        self.Id = params.get("Id")
        self.SendFor = params.get("SendFor")
        self.UidList = params.get("UidList")
        self.RoundNumber = params.get("RoundNumber")
        self.PersonInterval = params.get("PersonInterval")
        self.RoundInterval = params.get("RoundInterval")
        self.RecoverNotify = params.get("RecoverNotify")
        self.NeedSendNotice = params.get("NeedSendNotice")
        self.ReceiverGroupList = params.get("ReceiverGroupList")
        self.ReceiverUserList = params.get("ReceiverUserList")
        self.ReceiveLanguage = params.get("ReceiveLanguage")


class SendCustomAlarmMsgRequest(AbstractModel):
    """SendCustomAlarmMsg請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 介面模組名，當前取值monitor
        :type Module: str
        :param PolicyId: 訊息策略ID，在雲監控自定義訊息頁面配置
        :type PolicyId: str
        :param Msg: 用戶想要發送的自定義訊息内容
        :type Msg: str
        """
        self.Module = None
        self.PolicyId = None
        self.Msg = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.PolicyId = params.get("PolicyId")
        self.Msg = params.get("Msg")


class SendCustomAlarmMsgResponse(AbstractModel):
    """SendCustomAlarmMsg返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnBindingAllPolicyObjectRequest(AbstractModel):
    """UnBindingAllPolicyObject請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 固定值，爲"monitor"
        :type Module: str
        :param GroupId: 策略組id
        :type GroupId: int
        """
        self.Module = None
        self.GroupId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.GroupId = params.get("GroupId")


class UnBindingAllPolicyObjectResponse(AbstractModel):
    """UnBindingAllPolicyObject返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnBindingPolicyObjectRequest(AbstractModel):
    """UnBindingPolicyObject請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 固定值，爲"monitor"
        :type Module: str
        :param GroupId: 策略組id
        :type GroupId: int
        :param UniqueId: 待删除對象實例的唯一id清單
        :type UniqueId: list of str
        :param InstanceGroupId: 實例分組id, 如果按實例分組删除的話UniqueId參數是無效的
        :type InstanceGroupId: int
        """
        self.Module = None
        self.GroupId = None
        self.UniqueId = None
        self.InstanceGroupId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.GroupId = params.get("GroupId")
        self.UniqueId = params.get("UniqueId")
        self.InstanceGroupId = params.get("InstanceGroupId")


class UnBindingPolicyObjectResponse(AbstractModel):
    """UnBindingPolicyObject返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")