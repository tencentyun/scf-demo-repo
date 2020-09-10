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
from taifucloudcloud.yunjing.v20180228 import models


class YunjingClient(AbstractClient):
    _apiVersion = '2018-02-28'
    _endpoint = 'yunjing.taifucloudcloudapi.com'


    def CloseProVersion(self, request):
        """本介面 (CloseProVersion) 用于關閉專業版。

        :param request: 調用CloseProVersion所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.CloseProVersionRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.CloseProVersionResponse`

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


    def CreateProcessTask(self, request):
        """本介面 (CreateProcessTask) 用于創建實時拉取程式任務。

        :param request: 調用CreateProcessTask所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.CreateProcessTaskRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.CreateProcessTaskResponse`

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

        :param request: 調用CreateUsualLoginPlaces所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.CreateUsualLoginPlacesRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.CreateUsualLoginPlacesResponse`

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


    def DeleteBruteAttacks(self, request):
        """本介面 (DeleteBruteAttacks) 用于删除暴力破解記錄。

        :param request: 調用DeleteBruteAttacks所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DeleteBruteAttacksRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DeleteBruteAttacksResponse`

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


    def DeleteMachine(self, request):
        """本介面（DeleteMachine）用于卸載雲鏡用戶端。

        :param request: 調用DeleteMachine所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DeleteMachineRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DeleteMachineResponse`

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


    def DeleteMaliciousRequests(self, request):
        """本介面 (DeleteMaliciousRequests) 用于删除惡意請求記錄。

        :param request: 調用DeleteMaliciousRequests所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DeleteMaliciousRequestsRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DeleteMaliciousRequestsResponse`

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

        :param request: 調用DeleteMalwares所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DeleteMalwaresRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DeleteMalwaresResponse`

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

        :param request: 調用DeleteNonlocalLoginPlaces所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DeleteNonlocalLoginPlacesRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DeleteNonlocalLoginPlacesResponse`

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


    def DeleteUsualLoginPlaces(self, request):
        """本介面（DeleteUsualLoginPlaces）用于删除常用登入地。

        :param request: 調用DeleteUsualLoginPlaces所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DeleteUsualLoginPlacesRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DeleteUsualLoginPlacesResponse`

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

        :param request: 調用DescribeAccountStatistics所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeAccountStatisticsRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeAccountStatisticsResponse`

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

        :param request: 調用DescribeAccounts所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeAccountsRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeAccountsResponse`

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
        """本介面 (DescribeAgentVuls) 用于獲取主機的漏洞清單。

        :param request: 調用DescribeAgentVuls所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeAgentVulsRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeAgentVulsResponse`

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

        :param request: 調用DescribeAlarmAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeAlarmAttributeRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeAlarmAttributeResponse`

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


    def DescribeBruteAttacks(self, request):
        """本介面{DescribeBruteAttacks}用于獲取暴力破解事件清單。

        :param request: 調用DescribeBruteAttacks所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeBruteAttacksRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeBruteAttacksResponse`

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

        :param request: 調用DescribeComponentInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeComponentInfoRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeComponentInfoResponse`

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

        :param request: 調用DescribeComponentStatistics所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeComponentStatisticsRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeComponentStatisticsResponse`

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

        :param request: 調用DescribeComponents所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeComponentsRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeComponentsResponse`

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

        :param request: 調用DescribeHistoryAccounts所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeHistoryAccountsRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeHistoryAccountsResponse`

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

        :param request: 調用DescribeImpactedHosts所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeImpactedHostsRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeImpactedHostsResponse`

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


    def DescribeMachineInfo(self, request):
        """本介面（DescribeMachineInfo）用于獲取機器詳細訊息。

        :param request: 調用DescribeMachineInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeMachineInfoRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeMachineInfoResponse`

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

        :param request: 調用DescribeMachines所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeMachinesRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeMachinesResponse`

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

        :param request: 調用DescribeMaliciousRequests所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeMaliciousRequestsRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeMaliciousRequestsResponse`

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

        :param request: 調用DescribeMalwares所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeMalwaresRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeMalwaresResponse`

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

        :param request: 調用DescribeNonlocalLoginPlaces所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeNonlocalLoginPlacesRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeNonlocalLoginPlacesResponse`

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

        :param request: 調用DescribeOpenPortStatistics所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeOpenPortStatisticsRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeOpenPortStatisticsResponse`

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


    def DescribeOpenPorts(self, request):
        """本介面 (DescribeOpenPorts) 用于獲取端口清單數據。

        :param request: 調用DescribeOpenPorts所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeOpenPortsRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeOpenPortsResponse`

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

        :param request: 調用DescribeOverviewStatistics所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeOverviewStatisticsRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeOverviewStatisticsResponse`

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


    def DescribeProVersionInfo(self, request):
        """本介面 (DescribeProVersionInfo) 用于獲取專業版訊息。

        :param request: 調用DescribeProVersionInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeProVersionInfoRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeProVersionInfoResponse`

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
        """本介面 (DescribeProcessStatistics) 用于獲取程式統計清單數據。

        :param request: 調用DescribeProcessStatistics所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeProcessStatisticsRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeProcessStatisticsResponse`

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
        """本介面 (DescribeProcessTaskStatus) 用于獲取實時拉取程式任務狀态。

        :param request: 調用DescribeProcessTaskStatus所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeProcessTaskStatusRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeProcessTaskStatusResponse`

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
        """本介面 (DescribeProcesses) 用于獲取程式清單數據。

        :param request: 調用DescribeProcesses所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeProcessesRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeProcessesResponse`

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


    def DescribeSecurityDynamics(self, request):
        """本介面 (DescribeSecurityDynamics) 用于獲取安全事件訊息數據。

        :param request: 調用DescribeSecurityDynamics所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeSecurityDynamicsRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeSecurityDynamicsResponse`

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

        :param request: 調用DescribeSecurityTrends所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeSecurityTrendsRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeSecurityTrendsResponse`

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


    def DescribeUsualLoginPlaces(self, request):
        """此介面（DescribeUsualLoginPlaces）用于查詢常用登入地。

        :param request: 調用DescribeUsualLoginPlaces所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeUsualLoginPlacesRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeUsualLoginPlacesResponse`

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

        :param request: 調用DescribeVulInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeVulInfoRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeVulInfoResponse`

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

        :param request: 調用DescribeVulScanResult所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeVulScanResultRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeVulScanResultResponse`

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

        :param request: 調用DescribeVuls所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeVulsRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeVulsResponse`

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

        :param request: 調用DescribeWeeklyReportBruteAttacks所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeWeeklyReportBruteAttacksRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeWeeklyReportBruteAttacksResponse`

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

        :param request: 調用DescribeWeeklyReportInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeWeeklyReportInfoRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeWeeklyReportInfoResponse`

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

        :param request: 調用DescribeWeeklyReportMalwares所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeWeeklyReportMalwaresRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeWeeklyReportMalwaresResponse`

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

        :param request: 調用DescribeWeeklyReportNonlocalLoginPlaces所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeWeeklyReportNonlocalLoginPlacesRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeWeeklyReportNonlocalLoginPlacesResponse`

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

        :param request: 調用DescribeWeeklyReportVuls所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeWeeklyReportVulsRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeWeeklyReportVulsResponse`

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

        :param request: 調用DescribeWeeklyReports所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeWeeklyReportsRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.DescribeWeeklyReportsResponse`

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


    def ExportMaliciousRequests(self, request):
        """本介面 (ExportMaliciousRequests) 用于導出下載惡意請求文件。

        :param request: 調用ExportMaliciousRequests所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.ExportMaliciousRequestsRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.ExportMaliciousRequestsResponse`

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


    def IgnoreImpactedHosts(self, request):
        """本介面 (IngoreImpactedHosts) 用于忽略漏洞。

        :param request: 調用IgnoreImpactedHosts所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.IgnoreImpactedHostsRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.IgnoreImpactedHostsResponse`

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

        :param request: 調用InquiryPriceOpenProVersionPrepaid所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.InquiryPriceOpenProVersionPrepaidRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.InquiryPriceOpenProVersionPrepaidResponse`

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

        :param request: 調用MisAlarmNonlocalLoginPlaces所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.MisAlarmNonlocalLoginPlacesRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.MisAlarmNonlocalLoginPlacesResponse`

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

        :param request: 調用ModifyAlarmAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.ModifyAlarmAttributeRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.ModifyAlarmAttributeResponse`

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

        :param request: 調用ModifyAutoOpenProVersionConfig所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.ModifyAutoOpenProVersionConfigRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.ModifyAutoOpenProVersionConfigResponse`

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


    def ModifyProVersionRenewFlag(self, request):
        """本介面 (ModifyProVersionRenewFlag) 用于修改專業版包年包月續約标識。

        :param request: 調用ModifyProVersionRenewFlag所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.ModifyProVersionRenewFlagRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.ModifyProVersionRenewFlagResponse`

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


    def OpenProVersionPrepaid(self, request):
        """本介面 (OpenProVersionPrepaid) 用于開通專業版(包年包月)。

        :param request: 調用OpenProVersionPrepaid所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.OpenProVersionPrepaidRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.OpenProVersionPrepaidResponse`

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

        :param request: 調用RecoverMalwares所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.RecoverMalwaresRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.RecoverMalwaresResponse`

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

        :param request: 調用RenewProVersion所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.RenewProVersionRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.RenewProVersionResponse`

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
        """本介面 (RescanImpactedHosts) 用于漏洞重新檢測。

        :param request: 調用RescanImpactedHost所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.RescanImpactedHostRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.RescanImpactedHostResponse`

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

        :param request: 調用SeparateMalwares所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.SeparateMalwaresRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.SeparateMalwaresResponse`

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


    def TrustMaliciousRequest(self, request):
        """本介面 (TrustMaliciousRequest) 用于惡意請求添加信任。

        :param request: 調用TrustMaliciousRequest所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.TrustMaliciousRequestRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.TrustMaliciousRequestResponse`

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

        :param request: 調用TrustMalwares所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.TrustMalwaresRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.TrustMalwaresResponse`

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

        :param request: 調用UntrustMaliciousRequest所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.UntrustMaliciousRequestRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.UntrustMaliciousRequestResponse`

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

        :param request: 調用UntrustMalwares所需參數的結構體。
        :type request: :class:`taifucloudcloud.yunjing.v20180228.models.UntrustMalwaresRequest`
        :rtype: :class:`taifucloudcloud.yunjing.v20180228.models.UntrustMalwaresResponse`

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