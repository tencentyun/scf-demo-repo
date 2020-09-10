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

import json

from taifucloudcloud.common.exception.taifucloud_cloud_sdk_exception import TencentCloudSDKException
from taifucloudcloud.common.abstract_client import AbstractClient
from taifucloudcloud.cat.v20180409 import models


class CatClient(AbstractClient):
    _apiVersion = '2018-04-09'
    _endpoint = 'cat.taifucloudcloudapi.com'


    def BindAlarmPolicy(self, request):
        """綁定撥測任務和告警策略組

        :param request: Request instance for BindAlarmPolicy.
        :type request: :class:`taifucloudcloud.cat.v20180409.models.BindAlarmPolicyRequest`
        :rtype: :class:`taifucloudcloud.cat.v20180409.models.BindAlarmPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindAlarmPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindAlarmPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAgentGroup(self, request):
        """添加撥測分組

        :param request: Request instance for CreateAgentGroup.
        :type request: :class:`taifucloudcloud.cat.v20180409.models.CreateAgentGroupRequest`
        :rtype: :class:`taifucloudcloud.cat.v20180409.models.CreateAgentGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAgentGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAgentGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTaskEx(self, request):
        """創建撥測任務(擴展)

        :param request: Request instance for CreateTaskEx.
        :type request: :class:`taifucloudcloud.cat.v20180409.models.CreateTaskExRequest`
        :rtype: :class:`taifucloudcloud.cat.v20180409.models.CreateTaskExResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTaskEx", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTaskExResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAgentGroup(self, request):
        """删除撥測分組

        :param request: Request instance for DeleteAgentGroup.
        :type request: :class:`taifucloudcloud.cat.v20180409.models.DeleteAgentGroupRequest`
        :rtype: :class:`taifucloudcloud.cat.v20180409.models.DeleteAgentGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAgentGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAgentGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteTasks(self, request):
        """删除多個撥測任務

        :param request: Request instance for DeleteTasks.
        :type request: :class:`taifucloudcloud.cat.v20180409.models.DeleteTasksRequest`
        :rtype: :class:`taifucloudcloud.cat.v20180409.models.DeleteTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTasksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAgentGroups(self, request):
        """查詢撥測分組清單

        :param request: Request instance for DescribeAgentGroups.
        :type request: :class:`taifucloudcloud.cat.v20180409.models.DescribeAgentGroupsRequest`
        :rtype: :class:`taifucloudcloud.cat.v20180409.models.DescribeAgentGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAgentGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAgentGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAgents(self, request):
        """查詢本用戶可選的撥測點清單

        :param request: Request instance for DescribeAgents.
        :type request: :class:`taifucloudcloud.cat.v20180409.models.DescribeAgentsRequest`
        :rtype: :class:`taifucloudcloud.cat.v20180409.models.DescribeAgentsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAgents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAgentsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAlarmTopic(self, request):
        """查詢用戶的告警主題清單

        :param request: Request instance for DescribeAlarmTopic.
        :type request: :class:`taifucloudcloud.cat.v20180409.models.DescribeAlarmTopicRequest`
        :rtype: :class:`taifucloudcloud.cat.v20180409.models.DescribeAlarmTopicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAlarmTopic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAlarmTopicResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAlarms(self, request):
        """查詢撥測告警清單

        :param request: Request instance for DescribeAlarms.
        :type request: :class:`taifucloudcloud.cat.v20180409.models.DescribeAlarmsRequest`
        :rtype: :class:`taifucloudcloud.cat.v20180409.models.DescribeAlarmsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAlarms", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAlarmsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAlarmsByTask(self, request):
        """按任務查詢撥測告警清單

        :param request: Request instance for DescribeAlarmsByTask.
        :type request: :class:`taifucloudcloud.cat.v20180409.models.DescribeAlarmsByTaskRequest`
        :rtype: :class:`taifucloudcloud.cat.v20180409.models.DescribeAlarmsByTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAlarmsByTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAlarmsByTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCatLogs(self, request):
        """查詢撥測流水

        :param request: Request instance for DescribeCatLogs.
        :type request: :class:`taifucloudcloud.cat.v20180409.models.DescribeCatLogsRequest`
        :rtype: :class:`taifucloudcloud.cat.v20180409.models.DescribeCatLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCatLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCatLogsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskDetail(self, request):
        """查詢撥測任務訊息

        :param request: Request instance for DescribeTaskDetail.
        :type request: :class:`taifucloudcloud.cat.v20180409.models.DescribeTaskDetailRequest`
        :rtype: :class:`taifucloudcloud.cat.v20180409.models.DescribeTaskDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTasksByType(self, request):
        """按類型查詢撥測任務清單

        :param request: Request instance for DescribeTasksByType.
        :type request: :class:`taifucloudcloud.cat.v20180409.models.DescribeTasksByTypeRequest`
        :rtype: :class:`taifucloudcloud.cat.v20180409.models.DescribeTasksByTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTasksByType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTasksByTypeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUserLimit(self, request):
        """獲取用戶可用資源限制

        :param request: Request instance for DescribeUserLimit.
        :type request: :class:`taifucloudcloud.cat.v20180409.models.DescribeUserLimitRequest`
        :rtype: :class:`taifucloudcloud.cat.v20180409.models.DescribeUserLimitResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUserLimit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUserLimitResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetAvailRatioHistory(self, request):
        """獲取指定時刻的可用率地圖訊息

        :param request: Request instance for GetAvailRatioHistory.
        :type request: :class:`taifucloudcloud.cat.v20180409.models.GetAvailRatioHistoryRequest`
        :rtype: :class:`taifucloudcloud.cat.v20180409.models.GetAvailRatioHistoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetAvailRatioHistory", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetAvailRatioHistoryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetDailyAvailRatio(self, request):
        """獲取一天的整體可用率訊息

        :param request: Request instance for GetDailyAvailRatio.
        :type request: :class:`taifucloudcloud.cat.v20180409.models.GetDailyAvailRatioRequest`
        :rtype: :class:`taifucloudcloud.cat.v20180409.models.GetDailyAvailRatioResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDailyAvailRatio", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDailyAvailRatioResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetRealAvailRatio(self, request):
        """獲取實時可用率訊息

        :param request: Request instance for GetRealAvailRatio.
        :type request: :class:`taifucloudcloud.cat.v20180409.models.GetRealAvailRatioRequest`
        :rtype: :class:`taifucloudcloud.cat.v20180409.models.GetRealAvailRatioResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetRealAvailRatio", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetRealAvailRatioResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetRespTimeTrendEx(self, request):
        """查詢撥測任務的走勢數據

        :param request: Request instance for GetRespTimeTrendEx.
        :type request: :class:`taifucloudcloud.cat.v20180409.models.GetRespTimeTrendExRequest`
        :rtype: :class:`taifucloudcloud.cat.v20180409.models.GetRespTimeTrendExResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetRespTimeTrendEx", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetRespTimeTrendExResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetResultSummary(self, request):
        """獲取任務清單的實時數據

        :param request: Request instance for GetResultSummary.
        :type request: :class:`taifucloudcloud.cat.v20180409.models.GetResultSummaryRequest`
        :rtype: :class:`taifucloudcloud.cat.v20180409.models.GetResultSummaryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetResultSummary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetResultSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetReturnCodeHistory(self, request):
        """查詢撥測任務的曆史返回碼訊息

        :param request: Request instance for GetReturnCodeHistory.
        :type request: :class:`taifucloudcloud.cat.v20180409.models.GetReturnCodeHistoryRequest`
        :rtype: :class:`taifucloudcloud.cat.v20180409.models.GetReturnCodeHistoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetReturnCodeHistory", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetReturnCodeHistoryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetReturnCodeInfo(self, request):
        """查詢撥測任務的返回碼統計訊息

        :param request: Request instance for GetReturnCodeInfo.
        :type request: :class:`taifucloudcloud.cat.v20180409.models.GetReturnCodeInfoRequest`
        :rtype: :class:`taifucloudcloud.cat.v20180409.models.GetReturnCodeInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetReturnCodeInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetReturnCodeInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetTaskTotalNumber(self, request):
        """獲取AppId下的撥測任務總數

        :param request: Request instance for GetTaskTotalNumber.
        :type request: :class:`taifucloudcloud.cat.v20180409.models.GetTaskTotalNumberRequest`
        :rtype: :class:`taifucloudcloud.cat.v20180409.models.GetTaskTotalNumberResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetTaskTotalNumber", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetTaskTotalNumberResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAgentGroup(self, request):
        """修改撥測分組

        :param request: Request instance for ModifyAgentGroup.
        :type request: :class:`taifucloudcloud.cat.v20180409.models.ModifyAgentGroupRequest`
        :rtype: :class:`taifucloudcloud.cat.v20180409.models.ModifyAgentGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAgentGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAgentGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTaskEx(self, request):
        """修改撥測任務(擴展)

        :param request: Request instance for ModifyTaskEx.
        :type request: :class:`taifucloudcloud.cat.v20180409.models.ModifyTaskExRequest`
        :rtype: :class:`taifucloudcloud.cat.v20180409.models.ModifyTaskExResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTaskEx", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTaskExResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PauseTask(self, request):
        """暫停撥測任務

        :param request: Request instance for PauseTask.
        :type request: :class:`taifucloudcloud.cat.v20180409.models.PauseTaskRequest`
        :rtype: :class:`taifucloudcloud.cat.v20180409.models.PauseTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PauseTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PauseTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RunTask(self, request):
        """運作撥測任務

        :param request: Request instance for RunTask.
        :type request: :class:`taifucloudcloud.cat.v20180409.models.RunTaskRequest`
        :rtype: :class:`taifucloudcloud.cat.v20180409.models.RunTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RunTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RunTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def VerifyResult(self, request):
        """驗證撥測任務，結果驗證查詢（驗證成功的，才建議創建撥測任務）

        :param request: Request instance for VerifyResult.
        :type request: :class:`taifucloudcloud.cat.v20180409.models.VerifyResultRequest`
        :rtype: :class:`taifucloudcloud.cat.v20180409.models.VerifyResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VerifyResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VerifyResultResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)