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
from tencentcloud.iotexplorer.v20190423 import models


class IotexplorerClient(AbstractClient):
    _apiVersion = '2019-04-23'
    _endpoint = 'iotexplorer.tencentcloudapi.com'


    def ControlDeviceData(self, request):
        """根據設備産品ID、設備名稱，設置控制設備的屬性數據。

        :param request: 調用ControlDeviceData所需參數的結構體。
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ControlDeviceDataRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ControlDeviceDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ControlDeviceData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ControlDeviceDataResponse()
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


    def CreateProject(self, request):
        """爲用戶提供新建項目的能力，用于集中管理産品和應用。

        :param request: 調用CreateProject所需參數的結構體。
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CreateProjectRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CreateProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProjectResponse()
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


    def CreateStudioProduct(self, request):
        """爲用戶提供新建産品的能力，用于管理用戶的設備

        :param request: 調用CreateStudioProduct所需參數的結構體。
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.CreateStudioProductRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.CreateStudioProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateStudioProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateStudioProductResponse()
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


    def DeleteProject(self, request):
        """提供删除某個項目的能力

        :param request: 調用DeleteProject所需參數的結構體。
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteProjectRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteProjectResponse()
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


    def DeleteStudioProduct(self, request):
        """提供删除某個項目下産品的能力

        :param request: 調用DeleteStudioProduct所需參數的結構體。
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteStudioProductRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DeleteStudioProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteStudioProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteStudioProductResponse()
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


    def DescribeDeviceData(self, request):
        """根據設備産品ID、設備名稱，獲取設備上報的屬性數據。

        :param request: 調用DescribeDeviceData所需參數的結構體。
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceDataRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDeviceData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceDataResponse()
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


    def DescribeDeviceDataHistory(self, request):
        """獲取設備在指定時間範圍内上報的曆史數據。

        :param request: 調用DescribeDeviceDataHistory所需參數的結構體。
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceDataHistoryRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeDeviceDataHistoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDeviceDataHistory", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceDataHistoryResponse()
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


    def DescribeModelDefinition(self, request):
        """查詢産品配置的數據範本訊息

        :param request: 調用DescribeModelDefinition所需參數的結構體。
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeModelDefinitionRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeModelDefinitionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeModelDefinition", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeModelDefinitionResponse()
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


    def DescribeProject(self, request):
        """查詢項目詳情

        :param request: 調用DescribeProject所需參數的結構體。
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeProjectRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProjectResponse()
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


    def DescribeStudioProduct(self, request):
        """提供檢視茶品詳細訊息的能力，包括産品的ID、數據協議、認證類型等重要參數

        :param request: 調用DescribeStudioProduct所需參數的結構體。
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeStudioProductRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.DescribeStudioProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStudioProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStudioProductResponse()
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


    def GetProjectList(self, request):
        """提供查詢用戶所創建的項目清單查詢功能。

        :param request: 調用GetProjectList所需參數的結構體。
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GetProjectListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GetProjectListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetProjectList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetProjectListResponse()
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


    def GetStudioProductList(self, request):
        """提供查詢某個項目下所有産品訊息的能力。

        :param request: 調用GetStudioProductList所需參數的結構體。
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.GetStudioProductListRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.GetStudioProductListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetStudioProductList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetStudioProductListResponse()
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


    def ModifyModelDefinition(self, request):
        """提供修改産品的數據範本的能力

        :param request: 調用ModifyModelDefinition所需參數的結構體。
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyModelDefinitionRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyModelDefinitionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyModelDefinition", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyModelDefinitionResponse()
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


    def ModifyProject(self, request):
        """修改項目

        :param request: 調用ModifyProject所需參數的結構體。
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyProjectRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyProjectResponse()
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


    def ModifyStudioProduct(self, request):
        """提供修改産品的名稱和描述等訊息的能力

        :param request: 調用ModifyStudioProduct所需參數的結構體。
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyStudioProductRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ModifyStudioProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyStudioProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyStudioProductResponse()
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


    def ReleaseStudioProduct(self, request):
        """産品開發完成并測試通過後，通過發布産品将産品設置爲發布狀态

        :param request: 調用ReleaseStudioProduct所需參數的結構體。
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.ReleaseStudioProductRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.ReleaseStudioProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReleaseStudioProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReleaseStudioProductResponse()
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


    def SearchStudioProduct(self, request):
        """提供根據産品名稱查找産品的能力

        :param request: 調用SearchStudioProduct所需參數的結構體。
        :type request: :class:`tencentcloud.iotexplorer.v20190423.models.SearchStudioProductRequest`
        :rtype: :class:`tencentcloud.iotexplorer.v20190423.models.SearchStudioProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SearchStudioProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SearchStudioProductResponse()
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