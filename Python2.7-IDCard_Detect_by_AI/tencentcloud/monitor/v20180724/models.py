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


class DescribeBaseMetricsRequest(AbstractModel):
    """DescribeBaseMetrics請求參數結構體

    """

    def __init__(self):
        """
        :param Namespace: 業務命名空間
        :type Namespace: str
        :param MetricName: 指标名
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
        :param EndTime: 結束時間，預設爲當前時間。 EndTime不能小於EtartTime
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