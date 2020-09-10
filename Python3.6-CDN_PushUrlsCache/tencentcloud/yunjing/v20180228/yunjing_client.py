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

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.yunjing.v20180228 import models


class YunjingClient(AbstractClient):
    _apiVersion = '2018-02-28'
    _endpoint = 'yunjing.tencentcloudapi.com'


    def AddLoginWhiteList(self, request):
        """本介面（AddLoginWhiteList）用于添加白名單規則

        :param request: Request instance for AddLoginWhiteList.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.AddLoginWhiteListRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.AddLoginWhiteListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddLoginWhiteList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddLoginWhiteListResponse()
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


    def AddMachineTag(self, request):
        """增加機器關聯标簽

        :param request: Request instance for AddMachineTag.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.AddMachineTagRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.AddMachineTagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddMachineTag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddMachineTagResponse()
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


    def CloseProVersion(self, request):
        """本介面 (CloseProVersion) 用于關閉專業版。

        :param request: Request instance for CloseProVersion.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.CloseProVersionRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.CloseProVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CloseProVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CloseProVersionResponse()
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


    def CreateOpenPortTask(self, request):
        """本介面 (CreateOpenPortTask) 用于創建實時獲取端口任務。

        :param request: Request instance for CreateOpenPortTask.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.CreateOpenPortTaskRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.CreateOpenPortTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateOpenPortTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateOpenPortTaskResponse()
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


    def CreateProcessTask(self, request):
        """本介面 (CreateProcessTask) 用于創建實時拉取程序任務。

        :param request: Request instance for CreateProcessTask.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.CreateProcessTaskRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.CreateProcessTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateProcessTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProcessTaskResponse()
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


    def CreateUsualLoginPlaces(self, request):
        """此介面（CreateUsualLoginPlaces）用于添加常用登入地。

        :param request: Request instance for CreateUsualLoginPlaces.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.CreateUsualLoginPlacesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.CreateUsualLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateUsualLoginPlaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateUsualLoginPlacesResponse()
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


    def DeleteAttackLogs(self, request):
        """删除網絡攻擊日志

        :param request: Request instance for DeleteAttackLogs.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteAttackLogsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteAttackLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAttackLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAttackLogsResponse()
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


    def DeleteBashEvents(self, request):
        """根據Ids删除高危命令事件

        :param request: Request instance for DeleteBashEvents.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteBashEventsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteBashEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteBashEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteBashEventsResponse()
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


    def DeleteBashRules(self, request):
        """删除高危命令規則

        :param request: Request instance for DeleteBashRules.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteBashRulesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteBashRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteBashRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteBashRulesResponse()
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


    def DeleteBruteAttacks(self, request):
        """本介面 (DeleteBruteAttacks) 用于删除暴力破解記錄。

        :param request: Request instance for DeleteBruteAttacks.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteBruteAttacksRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteBruteAttacksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteBruteAttacks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteBruteAttacksResponse()
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


    def DeleteLoginWhiteList(self, request):
        """删除白名單規則

        :param request: Request instance for DeleteLoginWhiteList.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteLoginWhiteListRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteLoginWhiteListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLoginWhiteList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLoginWhiteListResponse()
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


    def DeleteMachine(self, request):
        """本介面（DeleteMachine）用于卸載雲鏡用戶端。

        :param request: Request instance for DeleteMachine.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteMachineRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteMachineResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMachine", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMachineResponse()
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


    def DeleteMachineTag(self, request):
        """删除服務器關聯的标簽

        :param request: Request instance for DeleteMachineTag.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteMachineTagRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteMachineTagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMachineTag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMachineTagResponse()
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


    def DeleteMaliciousRequests(self, request):
        """本介面 (DeleteMaliciousRequests) 用于删除惡意請求記錄。

        :param request: Request instance for DeleteMaliciousRequests.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteMaliciousRequestsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteMaliciousRequestsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMaliciousRequests", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMaliciousRequestsResponse()
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


    def DeleteMalwares(self, request):
        """本介面 (DeleteMalwares) 用于删除木馬記錄。

        :param request: Request instance for DeleteMalwares.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteMalwaresRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteMalwaresResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMalwares", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMalwaresResponse()
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


    def DeleteNonlocalLoginPlaces(self, request):
        """本介面 (DeleteNonlocalLoginPlaces) 用于删除異地登入記錄。

        :param request: Request instance for DeleteNonlocalLoginPlaces.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteNonlocalLoginPlacesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteNonlocalLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNonlocalLoginPlaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNonlocalLoginPlacesResponse()
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


    def DeletePrivilegeEvents(self, request):
        """根據Ids删除本地提權

        :param request: Request instance for DeletePrivilegeEvents.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeletePrivilegeEventsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeletePrivilegeEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePrivilegeEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePrivilegeEventsResponse()
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


    def DeletePrivilegeRules(self, request):
        """删除本地提權規則

        :param request: Request instance for DeletePrivilegeRules.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeletePrivilegeRulesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeletePrivilegeRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePrivilegeRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePrivilegeRulesResponse()
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


    def DeleteReverseShellEvents(self, request):
        """根據Ids删除反彈Shell事件

        :param request: Request instance for DeleteReverseShellEvents.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteReverseShellEventsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteReverseShellEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteReverseShellEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteReverseShellEventsResponse()
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


    def DeleteReverseShellRules(self, request):
        """删除反彈Shell規則

        :param request: Request instance for DeleteReverseShellRules.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteReverseShellRulesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteReverseShellRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteReverseShellRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteReverseShellRulesResponse()
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


    def DeleteTags(self, request):
        """删除标簽

        :param request: Request instance for DeleteTags.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteTagsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTagsResponse()
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


    def DeleteUsualLoginPlaces(self, request):
        """本介面（DeleteUsualLoginPlaces）用于删除常用登入地。

        :param request: Request instance for DeleteUsualLoginPlaces.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DeleteUsualLoginPlacesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DeleteUsualLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteUsualLoginPlaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteUsualLoginPlacesResponse()
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


    def DescribeAccountStatistics(self, request):
        """本介面 (DescribeAccountStatistics) 用于獲取帳号統計清單數據。

        :param request: Request instance for DescribeAccountStatistics.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeAccountStatisticsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeAccountStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccountStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountStatisticsResponse()
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


    def DescribeAccounts(self, request):
        """本介面 (DescribeAccounts) 用于獲取帳号清單數據。

        :param request: Request instance for DescribeAccounts.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeAccountsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccounts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountsResponse()
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


    def DescribeAgentVuls(self, request):
        """本介面 (DescribeAgentVuls) 用于獲取單台主機的漏洞清單。

        :param request: Request instance for DescribeAgentVuls.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeAgentVulsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeAgentVulsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAgentVuls", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAgentVulsResponse()
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


    def DescribeAlarmAttribute(self, request):
        """本介面 (DescribeAlarmAttribute) 用于獲取告警設置。

        :param request: Request instance for DescribeAlarmAttribute.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeAlarmAttributeRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeAlarmAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAlarmAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAlarmAttributeResponse()
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


    def DescribeAttackLogInfo(self, request):
        """網絡攻擊日志詳情

        :param request: Request instance for DescribeAttackLogInfo.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeAttackLogInfoRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeAttackLogInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAttackLogInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAttackLogInfoResponse()
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


    def DescribeAttackLogs(self, request):
        """按分頁形式展示網絡攻擊日志清單

        :param request: Request instance for DescribeAttackLogs.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeAttackLogsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeAttackLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAttackLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAttackLogsResponse()
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


    def DescribeBashEvents(self, request):
        """獲取高危命令清單

        :param request: Request instance for DescribeBashEvents.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeBashEventsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeBashEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBashEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBashEventsResponse()
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


    def DescribeBashRules(self, request):
        """獲取高危命令規則清單

        :param request: Request instance for DescribeBashRules.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeBashRulesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeBashRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBashRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBashRulesResponse()
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


    def DescribeBruteAttacks(self, request):
        """本介面{DescribeBruteAttacks}用于獲取暴力破解事件清單。

        :param request: Request instance for DescribeBruteAttacks.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeBruteAttacksRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeBruteAttacksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBruteAttacks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBruteAttacksResponse()
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


    def DescribeComponentInfo(self, request):
        """本介面 (DescribeComponentInfo) 用于獲取元件訊息數據。

        :param request: Request instance for DescribeComponentInfo.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeComponentInfoRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeComponentInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComponentInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComponentInfoResponse()
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


    def DescribeComponentStatistics(self, request):
        """本介面 (DescribeComponentStatistics) 用于獲取元件統計清單數據。

        :param request: Request instance for DescribeComponentStatistics.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeComponentStatisticsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeComponentStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComponentStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComponentStatisticsResponse()
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


    def DescribeComponents(self, request):
        """本介面 (DescribeComponents) 用于獲取元件清單數據。

        :param request: Request instance for DescribeComponents.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeComponentsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeComponentsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComponents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComponentsResponse()
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


    def DescribeHistoryAccounts(self, request):
        """本介面 (DescribeHistoryAccounts) 用于獲取帳号變更曆史清單數據。

        :param request: Request instance for DescribeHistoryAccounts.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeHistoryAccountsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeHistoryAccountsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeHistoryAccounts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeHistoryAccountsResponse()
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


    def DescribeImpactedHosts(self, request):
        """本介面 (DescribeImpactedHosts) 用于獲取漏洞受影響機器清單。

        :param request: Request instance for DescribeImpactedHosts.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeImpactedHostsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeImpactedHostsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImpactedHosts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImpactedHostsResponse()
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


    def DescribeLoginWhiteList(self, request):
        """獲取異地登入白名單清單

        :param request: Request instance for DescribeLoginWhiteList.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeLoginWhiteListRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeLoginWhiteListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLoginWhiteList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLoginWhiteListResponse()
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


    def DescribeMachineInfo(self, request):
        """本介面（DescribeMachineInfo）用于獲取機器詳細訊息。

        :param request: Request instance for DescribeMachineInfo.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeMachineInfoRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeMachineInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMachineInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMachineInfoResponse()
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


    def DescribeMachines(self, request):
        """本介面 (DescribeMachines) 用于獲取區域主機清單。

        :param request: Request instance for DescribeMachines.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeMachinesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeMachinesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMachines", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMachinesResponse()
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


    def DescribeMaliciousRequests(self, request):
        """本介面 (DescribeMaliciousRequests) 用于獲取惡意請求數據。

        :param request: Request instance for DescribeMaliciousRequests.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeMaliciousRequestsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeMaliciousRequestsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMaliciousRequests", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMaliciousRequestsResponse()
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


    def DescribeMalwares(self, request):
        """本介面（DescribeMalwares）用于獲取木馬事件清單。

        :param request: Request instance for DescribeMalwares.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeMalwaresRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeMalwaresResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMalwares", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMalwaresResponse()
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


    def DescribeNonlocalLoginPlaces(self, request):
        """本介面(DescribeNonlocalLoginPlaces)用于獲取異地登入事件。

        :param request: Request instance for DescribeNonlocalLoginPlaces.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeNonlocalLoginPlacesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeNonlocalLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNonlocalLoginPlaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNonlocalLoginPlacesResponse()
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


    def DescribeOpenPortStatistics(self, request):
        """本介面 (DescribeOpenPortStatistics) 用于獲取端口統計清單。

        :param request: Request instance for DescribeOpenPortStatistics.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeOpenPortStatisticsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeOpenPortStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeOpenPortStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOpenPortStatisticsResponse()
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


    def DescribeOpenPortTaskStatus(self, request):
        """本介面 (DescribeOpenPortTaskStatus) 用于獲取實時拉取端口任務狀态。

        :param request: Request instance for DescribeOpenPortTaskStatus.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeOpenPortTaskStatusRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeOpenPortTaskStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeOpenPortTaskStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOpenPortTaskStatusResponse()
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


    def DescribeOpenPorts(self, request):
        """本介面 (DescribeOpenPorts) 用于獲取端口清單數據。

        :param request: Request instance for DescribeOpenPorts.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeOpenPortsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeOpenPortsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeOpenPorts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOpenPortsResponse()
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


    def DescribeOverviewStatistics(self, request):
        """本介面用于（DescribeOverviewStatistics）獲取概覽統計數據。

        :param request: Request instance for DescribeOverviewStatistics.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeOverviewStatisticsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeOverviewStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeOverviewStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOverviewStatisticsResponse()
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


    def DescribePrivilegeEvents(self, request):
        """獲取本地提權事件清單

        :param request: Request instance for DescribePrivilegeEvents.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribePrivilegeEventsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribePrivilegeEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePrivilegeEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrivilegeEventsResponse()
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


    def DescribePrivilegeRules(self, request):
        """獲取本地提權規則清單

        :param request: Request instance for DescribePrivilegeRules.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribePrivilegeRulesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribePrivilegeRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePrivilegeRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePrivilegeRulesResponse()
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


    def DescribeProVersionInfo(self, request):
        """本介面 (DescribeProVersionInfo) 用于獲取專業版訊息。

        :param request: Request instance for DescribeProVersionInfo.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeProVersionInfoRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeProVersionInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProVersionInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProVersionInfoResponse()
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


    def DescribeProcessStatistics(self, request):
        """本介面 (DescribeProcessStatistics) 用于獲取程序統計清單數據。

        :param request: Request instance for DescribeProcessStatistics.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeProcessStatisticsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeProcessStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProcessStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProcessStatisticsResponse()
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


    def DescribeProcessTaskStatus(self, request):
        """本介面 (DescribeProcessTaskStatus) 用于獲取實時拉取程序任務狀态。

        :param request: Request instance for DescribeProcessTaskStatus.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeProcessTaskStatusRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeProcessTaskStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProcessTaskStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProcessTaskStatusResponse()
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


    def DescribeProcesses(self, request):
        """本介面 (DescribeProcesses) 用于獲取程序清單數據。

        :param request: Request instance for DescribeProcesses.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeProcessesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeProcessesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProcesses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProcessesResponse()
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


    def DescribeReverseShellEvents(self, request):
        """獲取反彈Shell清單

        :param request: Request instance for DescribeReverseShellEvents.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeReverseShellEventsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeReverseShellEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeReverseShellEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReverseShellEventsResponse()
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


    def DescribeReverseShellRules(self, request):
        """獲取反彈Shell規則清單

        :param request: Request instance for DescribeReverseShellRules.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeReverseShellRulesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeReverseShellRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeReverseShellRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReverseShellRulesResponse()
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


    def DescribeSecurityDynamics(self, request):
        """本介面 (DescribeSecurityDynamics) 用于獲取安全事件訊息數據。

        :param request: Request instance for DescribeSecurityDynamics.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeSecurityDynamicsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeSecurityDynamicsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecurityDynamics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityDynamicsResponse()
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


    def DescribeSecurityTrends(self, request):
        """本介面 (DescribeSecurityTrends) 用于獲取安全事件統計數據。

        :param request: Request instance for DescribeSecurityTrends.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeSecurityTrendsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeSecurityTrendsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecurityTrends", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityTrendsResponse()
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


    def DescribeTagMachines(self, request):
        """獲取指定标簽關聯的服務器訊息

        :param request: Request instance for DescribeTagMachines.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeTagMachinesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeTagMachinesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTagMachines", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTagMachinesResponse()
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


    def DescribeTags(self, request):
        """獲取所有主機标簽

        :param request: Request instance for DescribeTags.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeTagsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTagsResponse()
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


    def DescribeUsualLoginPlaces(self, request):
        """此介面（DescribeUsualLoginPlaces）用于查詢常用登入地。

        :param request: Request instance for DescribeUsualLoginPlaces.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeUsualLoginPlacesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeUsualLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUsualLoginPlaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUsualLoginPlacesResponse()
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


    def DescribeVulInfo(self, request):
        """本介面 (DescribeVulInfo) 用于獲取漏洞詳情。

        :param request: Request instance for DescribeVulInfo.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeVulInfoRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeVulInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVulInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulInfoResponse()
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


    def DescribeVulScanResult(self, request):
        """本介面 (DescribeVulScanResult) 用于獲取漏洞檢測結果。

        :param request: Request instance for DescribeVulScanResult.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeVulScanResultRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeVulScanResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVulScanResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulScanResultResponse()
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


    def DescribeVuls(self, request):
        """本介面 (DescribeVuls) 用于獲取漏洞清單數據。

        :param request: Request instance for DescribeVuls.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeVulsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeVulsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVuls", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulsResponse()
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


    def DescribeWeeklyReportBruteAttacks(self, request):
        """本介面 (DescribeWeeklyReportBruteAttacks) 用于獲取專業周報密碼破解數據。

        :param request: Request instance for DescribeWeeklyReportBruteAttacks.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportBruteAttacksRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportBruteAttacksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWeeklyReportBruteAttacks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWeeklyReportBruteAttacksResponse()
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


    def DescribeWeeklyReportInfo(self, request):
        """本介面 (DescribeWeeklyReportInfo) 用于獲取專業周報詳情數據。

        :param request: Request instance for DescribeWeeklyReportInfo.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportInfoRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWeeklyReportInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWeeklyReportInfoResponse()
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


    def DescribeWeeklyReportMalwares(self, request):
        """本介面 (DescribeWeeklyReportMalwares) 用于獲取專業周報木馬數據。

        :param request: Request instance for DescribeWeeklyReportMalwares.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportMalwaresRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportMalwaresResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWeeklyReportMalwares", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWeeklyReportMalwaresResponse()
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


    def DescribeWeeklyReportNonlocalLoginPlaces(self, request):
        """本介面 (DescribeWeeklyReportNonlocalLoginPlaces) 用于獲取專業周報異地登入數據。

        :param request: Request instance for DescribeWeeklyReportNonlocalLoginPlaces.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportNonlocalLoginPlacesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportNonlocalLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWeeklyReportNonlocalLoginPlaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWeeklyReportNonlocalLoginPlacesResponse()
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


    def DescribeWeeklyReportVuls(self, request):
        """本介面 (DescribeWeeklyReportVuls) 用于專業版周報漏洞數據。

        :param request: Request instance for DescribeWeeklyReportVuls.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportVulsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportVulsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWeeklyReportVuls", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWeeklyReportVulsResponse()
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


    def DescribeWeeklyReports(self, request):
        """本介面 (DescribeWeeklyReports) 用于獲取周報清單數據。

        :param request: Request instance for DescribeWeeklyReports.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.DescribeWeeklyReportsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWeeklyReports", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWeeklyReportsResponse()
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


    def EditBashRule(self, request):
        """新增或修改高危命令規則

        :param request: Request instance for EditBashRule.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.EditBashRuleRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.EditBashRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EditBashRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EditBashRuleResponse()
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


    def EditPrivilegeRule(self, request):
        """新增或修改本地提權規則

        :param request: Request instance for EditPrivilegeRule.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.EditPrivilegeRuleRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.EditPrivilegeRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EditPrivilegeRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EditPrivilegeRuleResponse()
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


    def EditReverseShellRule(self, request):
        """編輯反彈Shell規則

        :param request: Request instance for EditReverseShellRule.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.EditReverseShellRuleRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.EditReverseShellRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EditReverseShellRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EditReverseShellRuleResponse()
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


    def EditTags(self, request):
        """新增或編輯标簽

        :param request: Request instance for EditTags.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.EditTagsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.EditTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EditTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EditTagsResponse()
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


    def ExportAttackLogs(self, request):
        """導出網絡攻擊日志

        :param request: Request instance for ExportAttackLogs.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ExportAttackLogsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ExportAttackLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportAttackLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportAttackLogsResponse()
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


    def ExportBashEvents(self, request):
        """導出高危命令事件

        :param request: Request instance for ExportBashEvents.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ExportBashEventsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ExportBashEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportBashEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportBashEventsResponse()
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


    def ExportBruteAttacks(self, request):
        """本介面 (ExportBruteAttacks) 用于導出密碼破解記錄成CSV文件。

        :param request: Request instance for ExportBruteAttacks.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ExportBruteAttacksRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ExportBruteAttacksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportBruteAttacks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportBruteAttacksResponse()
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


    def ExportMaliciousRequests(self, request):
        """本介面 (ExportMaliciousRequests) 用于導出下載惡意請求文件。

        :param request: Request instance for ExportMaliciousRequests.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ExportMaliciousRequestsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ExportMaliciousRequestsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportMaliciousRequests", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportMaliciousRequestsResponse()
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


    def ExportMalwares(self, request):
        """本介面 (ExportMalwares) 用于導出木馬記錄CSV文件。

        :param request: Request instance for ExportMalwares.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ExportMalwaresRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ExportMalwaresResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportMalwares", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportMalwaresResponse()
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


    def ExportNonlocalLoginPlaces(self, request):
        """本介面 (ExportNonlocalLoginPlaces) 用于導出異地登入事件記錄CSV文件。

        :param request: Request instance for ExportNonlocalLoginPlaces.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ExportNonlocalLoginPlacesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ExportNonlocalLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportNonlocalLoginPlaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportNonlocalLoginPlacesResponse()
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


    def ExportPrivilegeEvents(self, request):
        """導出本地提權事件

        :param request: Request instance for ExportPrivilegeEvents.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ExportPrivilegeEventsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ExportPrivilegeEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportPrivilegeEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportPrivilegeEventsResponse()
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


    def ExportReverseShellEvents(self, request):
        """導出反彈Shell事件

        :param request: Request instance for ExportReverseShellEvents.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ExportReverseShellEventsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ExportReverseShellEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportReverseShellEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportReverseShellEventsResponse()
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


    def IgnoreImpactedHosts(self, request):
        """本介面 (IgnoreImpactedHosts) 用于忽略漏洞。

        :param request: Request instance for IgnoreImpactedHosts.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.IgnoreImpactedHostsRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.IgnoreImpactedHostsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("IgnoreImpactedHosts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IgnoreImpactedHostsResponse()
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


    def InquiryPriceOpenProVersionPrepaid(self, request):
        """本介面 (InquiryPriceOpenProVersionPrepaid) 用于開通專業版詢價(預付費)。

        :param request: Request instance for InquiryPriceOpenProVersionPrepaid.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.InquiryPriceOpenProVersionPrepaidRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.InquiryPriceOpenProVersionPrepaidResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceOpenProVersionPrepaid", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceOpenProVersionPrepaidResponse()
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


    def MisAlarmNonlocalLoginPlaces(self, request):
        """本介面{MisAlarmNonlocalLoginPlaces}将設置當前地點爲常用登入地。

        :param request: Request instance for MisAlarmNonlocalLoginPlaces.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.MisAlarmNonlocalLoginPlacesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.MisAlarmNonlocalLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MisAlarmNonlocalLoginPlaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MisAlarmNonlocalLoginPlacesResponse()
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


    def ModifyAlarmAttribute(self, request):
        """本介面（ModifyAlarmAttribute）用于修改告警設置。

        :param request: Request instance for ModifyAlarmAttribute.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ModifyAlarmAttributeRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ModifyAlarmAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAlarmAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAlarmAttributeResponse()
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


    def ModifyAutoOpenProVersionConfig(self, request):
        """本介面 (ModifyAutoOpenProVersionConfig) 用于設置新增主機自動開通專業版配置。

        :param request: Request instance for ModifyAutoOpenProVersionConfig.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ModifyAutoOpenProVersionConfigRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ModifyAutoOpenProVersionConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAutoOpenProVersionConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAutoOpenProVersionConfigResponse()
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


    def ModifyLoginWhiteList(self, request):
        """編輯白名單規則

        :param request: Request instance for ModifyLoginWhiteList.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ModifyLoginWhiteListRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ModifyLoginWhiteListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLoginWhiteList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLoginWhiteListResponse()
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


    def ModifyProVersionRenewFlag(self, request):
        """本介面 (ModifyProVersionRenewFlag) 用于修改專業版包年包月續約标識。

        :param request: Request instance for ModifyProVersionRenewFlag.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.ModifyProVersionRenewFlagRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.ModifyProVersionRenewFlagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyProVersionRenewFlag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyProVersionRenewFlagResponse()
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


    def OpenProVersion(self, request):
        """本介面 (OpenProVersion) 用于開通專業版。

        :param request: Request instance for OpenProVersion.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.OpenProVersionRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.OpenProVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OpenProVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OpenProVersionResponse()
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


    def OpenProVersionPrepaid(self, request):
        """本介面 (OpenProVersionPrepaid) 用于開通專業版(包年包月)。

        :param request: Request instance for OpenProVersionPrepaid.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.OpenProVersionPrepaidRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.OpenProVersionPrepaidResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OpenProVersionPrepaid", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OpenProVersionPrepaidResponse()
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


    def RecoverMalwares(self, request):
        """本介面（RecoverMalwares）用于批次恢複已經被隔離的木馬文件。

        :param request: Request instance for RecoverMalwares.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.RecoverMalwaresRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.RecoverMalwaresResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RecoverMalwares", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RecoverMalwaresResponse()
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


    def RenewProVersion(self, request):
        """本介面 (RenewProVersion) 用于續約專業版(包年包月)。

        :param request: Request instance for RenewProVersion.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.RenewProVersionRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.RenewProVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewProVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewProVersionResponse()
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


    def RescanImpactedHost(self, request):
        """本介面 (RescanImpactedHost) 用于漏洞重新檢測。

        :param request: Request instance for RescanImpactedHost.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.RescanImpactedHostRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.RescanImpactedHostResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RescanImpactedHost", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RescanImpactedHostResponse()
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


    def SeparateMalwares(self, request):
        """本介面（SeparateMalwares）用于隔離木馬。

        :param request: Request instance for SeparateMalwares.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.SeparateMalwaresRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.SeparateMalwaresResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SeparateMalwares", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SeparateMalwaresResponse()
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


    def SetBashEventsStatus(self, request):
        """設置高危命令事件狀态

        :param request: Request instance for SetBashEventsStatus.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.SetBashEventsStatusRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.SetBashEventsStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetBashEventsStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetBashEventsStatusResponse()
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


    def SwitchBashRules(self, request):
        """切換高危命令規則狀态

        :param request: Request instance for SwitchBashRules.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.SwitchBashRulesRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.SwitchBashRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SwitchBashRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SwitchBashRulesResponse()
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


    def TrustMaliciousRequest(self, request):
        """本介面 (TrustMaliciousRequest) 用于惡意請求添加信任。

        :param request: Request instance for TrustMaliciousRequest.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.TrustMaliciousRequestRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.TrustMaliciousRequestResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TrustMaliciousRequest", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TrustMaliciousRequestResponse()
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


    def TrustMalwares(self, request):
        """本介面(TrustMalwares)将被識别木馬文件設爲信任。

        :param request: Request instance for TrustMalwares.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.TrustMalwaresRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.TrustMalwaresResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TrustMalwares", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TrustMalwaresResponse()
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


    def UntrustMaliciousRequest(self, request):
        """本介面 (UntrustMaliciousRequest) 用于取消信任惡意請求。

        :param request: Request instance for UntrustMaliciousRequest.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.UntrustMaliciousRequestRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.UntrustMaliciousRequestResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UntrustMaliciousRequest", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UntrustMaliciousRequestResponse()
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


    def UntrustMalwares(self, request):
        """本介面（UntrustMalwares）用于取消信任木馬文件。

        :param request: Request instance for UntrustMalwares.
        :type request: :class:`tencentcloud.yunjing.v20180228.models.UntrustMalwaresRequest`
        :rtype: :class:`tencentcloud.yunjing.v20180228.models.UntrustMalwaresResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UntrustMalwares", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UntrustMalwaresResponse()
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