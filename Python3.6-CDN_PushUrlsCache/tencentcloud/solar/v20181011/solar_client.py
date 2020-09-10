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
from taifucloudcloud.solar.v20181011 import models


class SolarClient(AbstractClient):
    _apiVersion = '2018-10-11'
    _endpoint = 'solar.taifucloudcloudapi.com'


    def CheckStaffChUser(self, request):
        """員工管道更改員工狀态

        :param request: Request instance for CheckStaffChUser.
        :type request: :class:`taifucloudcloud.solar.v20181011.models.CheckStaffChUserRequest`
        :rtype: :class:`taifucloudcloud.solar.v20181011.models.CheckStaffChUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckStaffChUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckStaffChUserResponse()
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


    def CopyActivityChannel(self, request):
        """複制活動管道的策略

        :param request: Request instance for CopyActivityChannel.
        :type request: :class:`taifucloudcloud.solar.v20181011.models.CopyActivityChannelRequest`
        :rtype: :class:`taifucloudcloud.solar.v20181011.models.CopyActivityChannelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CopyActivityChannel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CopyActivityChannelResponse()
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
        """創建項目

        :param request: Request instance for CreateProject.
        :type request: :class:`taifucloudcloud.solar.v20181011.models.CreateProjectRequest`
        :rtype: :class:`taifucloudcloud.solar.v20181011.models.CreateProjectResponse`

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


    def CreateSubProject(self, request):
        """創建子項目

        :param request: Request instance for CreateSubProject.
        :type request: :class:`taifucloudcloud.solar.v20181011.models.CreateSubProjectRequest`
        :rtype: :class:`taifucloudcloud.solar.v20181011.models.CreateSubProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSubProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSubProjectResponse()
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
        """删除項目

        :param request: Request instance for DeleteProject.
        :type request: :class:`taifucloudcloud.solar.v20181011.models.DeleteProjectRequest`
        :rtype: :class:`taifucloudcloud.solar.v20181011.models.DeleteProjectResponse`

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


    def DescribeCustomer(self, request):
        """客戶檔案查詢客戶詳情

        :param request: Request instance for DescribeCustomer.
        :type request: :class:`taifucloudcloud.solar.v20181011.models.DescribeCustomerRequest`
        :rtype: :class:`taifucloudcloud.solar.v20181011.models.DescribeCustomerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCustomer", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCustomerResponse()
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


    def DescribeCustomers(self, request):
        """查詢客戶檔案清單

        :param request: Request instance for DescribeCustomers.
        :type request: :class:`taifucloudcloud.solar.v20181011.models.DescribeCustomersRequest`
        :rtype: :class:`taifucloudcloud.solar.v20181011.models.DescribeCustomersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCustomers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCustomersResponse()
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
        """項目詳情展示

        :param request: Request instance for DescribeProject.
        :type request: :class:`taifucloudcloud.solar.v20181011.models.DescribeProjectRequest`
        :rtype: :class:`taifucloudcloud.solar.v20181011.models.DescribeProjectResponse`

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


    def DescribeProjectStock(self, request):
        """項目庫存詳情

        :param request: Request instance for DescribeProjectStock.
        :type request: :class:`taifucloudcloud.solar.v20181011.models.DescribeProjectStockRequest`
        :rtype: :class:`taifucloudcloud.solar.v20181011.models.DescribeProjectStockResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProjectStock", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProjectStockResponse()
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


    def DescribeProjects(self, request):
        """項目清單展示

        :param request: Request instance for DescribeProjects.
        :type request: :class:`taifucloudcloud.solar.v20181011.models.DescribeProjectsRequest`
        :rtype: :class:`taifucloudcloud.solar.v20181011.models.DescribeProjectsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProjects", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProjectsResponse()
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


    def DescribeResourceTemplateHeaders(self, request):
        """素材查詢服務号範本的清單（樣例）

        :param request: Request instance for DescribeResourceTemplateHeaders.
        :type request: :class:`taifucloudcloud.solar.v20181011.models.DescribeResourceTemplateHeadersRequest`
        :rtype: :class:`taifucloudcloud.solar.v20181011.models.DescribeResourceTemplateHeadersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeResourceTemplateHeaders", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourceTemplateHeadersResponse()
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


    def DescribeSubProject(self, request):
        """子項目詳情

        :param request: Request instance for DescribeSubProject.
        :type request: :class:`taifucloudcloud.solar.v20181011.models.DescribeSubProjectRequest`
        :rtype: :class:`taifucloudcloud.solar.v20181011.models.DescribeSubProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSubProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSubProjectResponse()
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


    def ExpireFlow(self, request):
        """把審批中的工單置爲已失效

        :param request: Request instance for ExpireFlow.
        :type request: :class:`taifucloudcloud.solar.v20181011.models.ExpireFlowRequest`
        :rtype: :class:`taifucloudcloud.solar.v20181011.models.ExpireFlowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExpireFlow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExpireFlowResponse()
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

        :param request: Request instance for ModifyProject.
        :type request: :class:`taifucloudcloud.solar.v20181011.models.ModifyProjectRequest`
        :rtype: :class:`taifucloudcloud.solar.v20181011.models.ModifyProjectResponse`

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


    def OffLineProject(self, request):
        """下線項目

        :param request: Request instance for OffLineProject.
        :type request: :class:`taifucloudcloud.solar.v20181011.models.OffLineProjectRequest`
        :rtype: :class:`taifucloudcloud.solar.v20181011.models.OffLineProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OffLineProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OffLineProjectResponse()
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


    def ReplenishProjectStock(self, request):
        """補充子項目庫存

        :param request: Request instance for ReplenishProjectStock.
        :type request: :class:`taifucloudcloud.solar.v20181011.models.ReplenishProjectStockRequest`
        :rtype: :class:`taifucloudcloud.solar.v20181011.models.ReplenishProjectStockResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReplenishProjectStock", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReplenishProjectStockResponse()
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


    def SendWxTouchTask(self, request):
        """發送企業 觸達任務

        :param request: Request instance for SendWxTouchTask.
        :type request: :class:`taifucloudcloud.solar.v20181011.models.SendWxTouchTaskRequest`
        :rtype: :class:`taifucloudcloud.solar.v20181011.models.SendWxTouchTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SendWxTouchTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SendWxTouchTaskResponse()
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