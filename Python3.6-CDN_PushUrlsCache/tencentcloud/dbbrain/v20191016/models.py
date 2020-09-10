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


class DescribeDBDiagEventRequest(AbstractModel):
    """DescribeDBDiagEvent請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID 。
        :type InstanceId: str
        :param EventId: 事件 ID 。通過“獲取實例診斷曆史DescribeDBDiagHistory”獲取。
        :type EventId: int
        """
        self.InstanceId = None
        self.EventId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.EventId = params.get("EventId")


class DescribeDBDiagEventResponse(AbstractModel):
    """DescribeDBDiagEvent返回參數結構體

    """

    def __init__(self):
        """
        :param DiagItem: 診斷項。
        :type DiagItem: str
        :param DiagType: 診斷類型。
        :type DiagType: str
        :param EventId: 事件 ID 。
        :type EventId: int
        :param Explanation: 事件詳情。
        :type Explanation: str
        :param Outline: 概要。
        :type Outline: str
        :param Problem: 診斷出的問題。
        :type Problem: str
        :param Severity: 嚴重程度。嚴重程度分爲5級，按影響程度從高至低分别爲：1：緻命，2：嚴重，3：告警，4：提示，5：健康。
        :type Severity: int
        :param StartTime: 開始時間
        :type StartTime: str
        :param Suggestions: 建議。
        :type Suggestions: str
        :param Metric: 保留欄位。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Metric: str
        :param EndTime: 結束時間。
        :type EndTime: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DiagItem = None
        self.DiagType = None
        self.EventId = None
        self.Explanation = None
        self.Outline = None
        self.Problem = None
        self.Severity = None
        self.StartTime = None
        self.Suggestions = None
        self.Metric = None
        self.EndTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DiagItem = params.get("DiagItem")
        self.DiagType = params.get("DiagType")
        self.EventId = params.get("EventId")
        self.Explanation = params.get("Explanation")
        self.Outline = params.get("Outline")
        self.Problem = params.get("Problem")
        self.Severity = params.get("Severity")
        self.StartTime = params.get("StartTime")
        self.Suggestions = params.get("Suggestions")
        self.Metric = params.get("Metric")
        self.EndTime = params.get("EndTime")
        self.RequestId = params.get("RequestId")


class DescribeDBDiagHistoryRequest(AbstractModel):
    """DescribeDBDiagHistory請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID 。
        :type InstanceId: str
        :param StartTime: 開始時間。如“2019-09-10 12:13:14”。
        :type StartTime: str
        :param EndTime: 結束時間。如“2019-09-11 12:13:14”。
        :type EndTime: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeDBDiagHistoryResponse(AbstractModel):
    """DescribeDBDiagHistory返回參數結構體

    """

    def __init__(self):
        """
        :param Events: 事件描述。
        :type Events: list of DiagHistoryEventItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Events = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Events") is not None:
            self.Events = []
            for item in params.get("Events"):
                obj = DiagHistoryEventItem()
                obj._deserialize(item)
                self.Events.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSlowLogTimeSeriesStatsRequest(AbstractModel):
    """DescribeSlowLogTimeSeriesStats請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID 。
        :type InstanceId: str
        :param StartTime: 開始時間。
        :type StartTime: str
        :param EndTime: 結束時間。
        :type EndTime: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeSlowLogTimeSeriesStatsResponse(AbstractModel):
    """DescribeSlowLogTimeSeriesStats返回參數結構體

    """

    def __init__(self):
        """
        :param Period: 柱間單位時間間隔，單位爲秒。
        :type Period: int
        :param TimeSeries: 單位時間間隔内慢日志數量統計。
        :type TimeSeries: list of TimeSlice
        :param SeriesData: 單位時間間隔内的實例 cpu 使用率監控數據。
        :type SeriesData: :class:`taifucloudcloud.dbbrain.v20191016.models.MonitorMetricSeriesData`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Period = None
        self.TimeSeries = None
        self.SeriesData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        if params.get("TimeSeries") is not None:
            self.TimeSeries = []
            for item in params.get("TimeSeries"):
                obj = TimeSlice()
                obj._deserialize(item)
                self.TimeSeries.append(obj)
        if params.get("SeriesData") is not None:
            self.SeriesData = MonitorMetricSeriesData()
            self.SeriesData._deserialize(params.get("SeriesData"))
        self.RequestId = params.get("RequestId")


class DescribeSlowLogTopSqlsRequest(AbstractModel):
    """DescribeSlowLogTopSqls請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例 ID 。
        :type InstanceId: str
        :param StartTime: 開始時間。
        :type StartTime: str
        :param EndTime: 截止時間。
        :type EndTime: str
        :param SortBy: 排序鍵，目前支援 QueryTime,ExecTimes,RowsSent,LockTime以及RowsExamined 等排序鍵。
        :type SortBy: str
        :param OrderBy: 排序方式，支援ASC（升序）以及DESC（降序）。
        :type OrderBy: str
        :param Limit: 返回數量，預設爲20，最大值爲100。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.SortBy = None
        self.OrderBy = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SortBy = params.get("SortBy")
        self.OrderBy = params.get("OrderBy")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeSlowLogTopSqlsResponse(AbstractModel):
    """DescribeSlowLogTopSqls返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的記錄總數。
        :type TotalCount: int
        :param Rows: 慢日志 top sql 清單
        :type Rows: list of SlowLogTopSqlItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Rows = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Rows") is not None:
            self.Rows = []
            for item in params.get("Rows"):
                obj = SlowLogTopSqlItem()
                obj._deserialize(item)
                self.Rows.append(obj)
        self.RequestId = params.get("RequestId")


class DiagHistoryEventItem(AbstractModel):
    """實例診斷曆史事件

    """

    def __init__(self):
        """
        :param DiagType: 診斷類型。
        :type DiagType: str
        :param EndTime: 結束時間。
        :type EndTime: str
        :param StartTime: 開始時間。
        :type StartTime: str
        :param EventId: 事件 ID 。
        :type EventId: int
        :param Severity: 嚴重程度。嚴重程度分爲5級，按影響程度從高至低分别爲：1：緻命，2：嚴重，3：告警，4：提示，5：健康。
        :type Severity: int
        :param Outline: 概要。
        :type Outline: str
        :param DiagItem: 診斷項。
        :type DiagItem: str
        :param InstanceId: 實例 ID 。
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param Metric: 保留欄位
注意：此欄位可能返回 null，表示取不到有效值。
        :type Metric: str
        :param Region: 地域
注意：此欄位可能返回 null，表示取不到有效值。
        :type Region: str
        """
        self.DiagType = None
        self.EndTime = None
        self.StartTime = None
        self.EventId = None
        self.Severity = None
        self.Outline = None
        self.DiagItem = None
        self.InstanceId = None
        self.Metric = None
        self.Region = None


    def _deserialize(self, params):
        self.DiagType = params.get("DiagType")
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        self.EventId = params.get("EventId")
        self.Severity = params.get("Severity")
        self.Outline = params.get("Outline")
        self.DiagItem = params.get("DiagItem")
        self.InstanceId = params.get("InstanceId")
        self.Metric = params.get("Metric")
        self.Region = params.get("Region")


class MonitorMetric(AbstractModel):
    """監控數據

    """

    def __init__(self):
        """
        :param Metric: 指标名稱。
        :type Metric: str
        :param Unit: 指标單位。
        :type Unit: str
        :param Values: 指标值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Values: list of int
        """
        self.Metric = None
        self.Unit = None
        self.Values = None


    def _deserialize(self, params):
        self.Metric = params.get("Metric")
        self.Unit = params.get("Unit")
        self.Values = params.get("Values")


class MonitorMetricSeriesData(AbstractModel):
    """單位時間間隔内的監控指标數據

    """

    def __init__(self):
        """
        :param Series: 監控指标。
        :type Series: list of MonitorMetric
        :param Timestamp: 監控指标對應的時間戳。
        :type Timestamp: list of int
        """
        self.Series = None
        self.Timestamp = None


    def _deserialize(self, params):
        if params.get("Series") is not None:
            self.Series = []
            for item in params.get("Series"):
                obj = MonitorMetric()
                obj._deserialize(item)
                self.Series.append(obj)
        self.Timestamp = params.get("Timestamp")


class SlowLogTopSqlItem(AbstractModel):
    """慢日志TopSql

    """

    def __init__(self):
        """
        :param LockTime: sql總鎖等待時間
        :type LockTime: float
        :param LockTimeMax: 最大鎖等待時間
        :type LockTimeMax: float
        :param LockTimeMin: 最小鎖等待時間
        :type LockTimeMin: float
        :param RowsExamined: 總掃描行數
        :type RowsExamined: int
        :param RowsExaminedMax: 最大掃描行數
        :type RowsExaminedMax: int
        :param RowsExaminedMin: 最小掃描行數
        :type RowsExaminedMin: int
        :param QueryTime: 總耗時
        :type QueryTime: float
        :param QueryTimeMax: 最大執行時間
        :type QueryTimeMax: float
        :param QueryTimeMin: 最小執行時間
        :type QueryTimeMin: float
        :param RowsSent: 總返回行數
        :type RowsSent: int
        :param RowsSentMax: 最大返回行數
        :type RowsSentMax: int
        :param RowsSentMin: 最小返回行數
        :type RowsSentMin: int
        :param ExecTimes: 執行次數
        :type ExecTimes: int
        :param SqlTemplate: sql範本
        :type SqlTemplate: str
        :param SqlText: 帶參數SQL（随機）
        :type SqlText: str
        :param Schema: schema
        :type Schema: str
        :param QueryTimeRatio: 總耗時占比
        :type QueryTimeRatio: float
        :param LockTimeRatio: sql總鎖等待時間占比
        :type LockTimeRatio: float
        :param RowsExaminedRatio: 總掃描行數占比
        :type RowsExaminedRatio: float
        :param RowsSentRatio: 總返回行數占比
        :type RowsSentRatio: float
        """
        self.LockTime = None
        self.LockTimeMax = None
        self.LockTimeMin = None
        self.RowsExamined = None
        self.RowsExaminedMax = None
        self.RowsExaminedMin = None
        self.QueryTime = None
        self.QueryTimeMax = None
        self.QueryTimeMin = None
        self.RowsSent = None
        self.RowsSentMax = None
        self.RowsSentMin = None
        self.ExecTimes = None
        self.SqlTemplate = None
        self.SqlText = None
        self.Schema = None
        self.QueryTimeRatio = None
        self.LockTimeRatio = None
        self.RowsExaminedRatio = None
        self.RowsSentRatio = None


    def _deserialize(self, params):
        self.LockTime = params.get("LockTime")
        self.LockTimeMax = params.get("LockTimeMax")
        self.LockTimeMin = params.get("LockTimeMin")
        self.RowsExamined = params.get("RowsExamined")
        self.RowsExaminedMax = params.get("RowsExaminedMax")
        self.RowsExaminedMin = params.get("RowsExaminedMin")
        self.QueryTime = params.get("QueryTime")
        self.QueryTimeMax = params.get("QueryTimeMax")
        self.QueryTimeMin = params.get("QueryTimeMin")
        self.RowsSent = params.get("RowsSent")
        self.RowsSentMax = params.get("RowsSentMax")
        self.RowsSentMin = params.get("RowsSentMin")
        self.ExecTimes = params.get("ExecTimes")
        self.SqlTemplate = params.get("SqlTemplate")
        self.SqlText = params.get("SqlText")
        self.Schema = params.get("Schema")
        self.QueryTimeRatio = params.get("QueryTimeRatio")
        self.LockTimeRatio = params.get("LockTimeRatio")
        self.RowsExaminedRatio = params.get("RowsExaminedRatio")
        self.RowsSentRatio = params.get("RowsSentRatio")


class TimeSlice(AbstractModel):
    """單位時間間隔内的慢日志統計

    """

    def __init__(self):
        """
        :param Count: 總數
        :type Count: int
        :param Timestamp: 統計開始時間
        :type Timestamp: int
        """
        self.Count = None
        self.Timestamp = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.Timestamp = params.get("Timestamp")