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
from taifucloudcloud.iot.v20180123 import models


class IotClient(AbstractClient):
    _apiVersion = '2018-01-23'
    _endpoint = 'iot.taifucloudcloudapi.com'


    def ActivateRule(self, request):
        """啓用規則

        :param request: Request instance for ActivateRule.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.ActivateRuleRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.ActivateRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ActivateRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ActivateRuleResponse()
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


    def AddDevice(self, request):
        """提供在指定的産品Id下創建一個設備的能力，生成設備名稱與設備秘鑰。

        :param request: Request instance for AddDevice.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.AddDeviceRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.AddDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddDeviceResponse()
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


    def AddProduct(self, request):
        """本介面(AddProduct)用於創建、定義某款硬體産品。

        :param request: Request instance for AddProduct.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.AddProductRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.AddProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddProductResponse()
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


    def AddRule(self, request):
        """新增規則

        :param request: Request instance for AddRule.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.AddRuleRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.AddRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddRuleResponse()
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


    def AddTopic(self, request):
        """新增Topic，用於設備或應用發布訊息至該Topic或訂閱該Topic的訊息。

        :param request: Request instance for AddTopic.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.AddTopicRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.AddTopicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddTopic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddTopicResponse()
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


    def AppAddUser(self, request):
        """爲APP提供用戶注冊功能

        :param request: Request instance for AppAddUser.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.AppAddUserRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.AppAddUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AppAddUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AppAddUserResponse()
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


    def AppDeleteDevice(self, request):
        """用戶解除與設備的關聯關系，解除後APP用戶無法控制設備，獲取設備數據

        :param request: Request instance for AppDeleteDevice.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.AppDeleteDeviceRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.AppDeleteDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AppDeleteDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AppDeleteDeviceResponse()
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


    def AppGetDevice(self, request):
        """獲取綁定設備的基本訊息與數據範本定義

        :param request: Request instance for AppGetDevice.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.AppGetDeviceRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.AppGetDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AppGetDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AppGetDeviceResponse()
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


    def AppGetDeviceData(self, request):
        """獲取綁定設備數據，用於實時展示設備的最新數據

        :param request: Request instance for AppGetDeviceData.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.AppGetDeviceDataRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.AppGetDeviceDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AppGetDeviceData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AppGetDeviceDataResponse()
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


    def AppGetDeviceStatuses(self, request):
        """獲取綁定設備的上下線狀态

        :param request: Request instance for AppGetDeviceStatuses.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.AppGetDeviceStatusesRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.AppGetDeviceStatusesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AppGetDeviceStatuses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AppGetDeviceStatusesResponse()
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


    def AppGetDevices(self, request):
        """獲取用戶的綁定設備清單

        :param request: Request instance for AppGetDevices.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.AppGetDevicesRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.AppGetDevicesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AppGetDevices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AppGetDevicesResponse()
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


    def AppGetToken(self, request):
        """獲取用戶token

        :param request: Request instance for AppGetToken.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.AppGetTokenRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.AppGetTokenResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AppGetToken", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AppGetTokenResponse()
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


    def AppGetUser(self, request):
        """獲取用戶訊息

        :param request: Request instance for AppGetUser.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.AppGetUserRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.AppGetUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AppGetUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AppGetUserResponse()
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


    def AppIssueDeviceControl(self, request):
        """用戶通過APP控制設備

        :param request: Request instance for AppIssueDeviceControl.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.AppIssueDeviceControlRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.AppIssueDeviceControlResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AppIssueDeviceControl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AppIssueDeviceControlResponse()
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


    def AppResetPassword(self, request):
        """重置APP用戶密碼

        :param request: Request instance for AppResetPassword.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.AppResetPasswordRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.AppResetPasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AppResetPassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AppResetPasswordResponse()
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


    def AppSecureAddDevice(self, request):
        """用戶綁定設備，綁定後可以在APP端進行控制。綁定設備前需調用“獲取設備綁定簽名”介面

        :param request: Request instance for AppSecureAddDevice.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.AppSecureAddDeviceRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.AppSecureAddDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AppSecureAddDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AppSecureAddDeviceResponse()
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


    def AppUpdateDevice(self, request):
        """修改設備别名，便於用戶個性化定義設備的名稱

        :param request: Request instance for AppUpdateDevice.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.AppUpdateDeviceRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.AppUpdateDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AppUpdateDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AppUpdateDeviceResponse()
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


    def AppUpdateUser(self, request):
        """修改用戶訊息

        :param request: Request instance for AppUpdateUser.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.AppUpdateUserRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.AppUpdateUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AppUpdateUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AppUpdateUserResponse()
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


    def AssociateSubDeviceToGatewayProduct(self, request):
        """關聯子設備産品和閘道産品

        :param request: Request instance for AssociateSubDeviceToGatewayProduct.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.AssociateSubDeviceToGatewayProductRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.AssociateSubDeviceToGatewayProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssociateSubDeviceToGatewayProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateSubDeviceToGatewayProductResponse()
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


    def DeactivateRule(self, request):
        """禁用規則

        :param request: Request instance for DeactivateRule.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.DeactivateRuleRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.DeactivateRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeactivateRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeactivateRuleResponse()
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


    def DeleteDevice(self, request):
        """提供在指定的産品Id下删除一個設備的能力。

        :param request: Request instance for DeleteDevice.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.DeleteDeviceRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.DeleteDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDeviceResponse()
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


    def DeleteProduct(self, request):
        """删除用戶指定的産品Id對應的訊息。

        :param request: Request instance for DeleteProduct.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.DeleteProductRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.DeleteProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteProductResponse()
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


    def DeleteRule(self, request):
        """删除規則

        :param request: Request instance for DeleteRule.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.DeleteRuleRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.DeleteRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRuleResponse()
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


    def DeleteTopic(self, request):
        """删除Topic

        :param request: Request instance for DeleteTopic.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.DeleteTopicRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.DeleteTopicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTopic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTopicResponse()
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


    def GetDataHistory(self, request):
        """批次獲取設備某一段時間範圍的設備上報數據。該介面适用於使用高級版類型的産品

        :param request: Request instance for GetDataHistory.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.GetDataHistoryRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.GetDataHistoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDataHistory", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDataHistoryResponse()
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


    def GetDebugLog(self, request):
        """獲取設備的調試日志，用於定位問題

        :param request: Request instance for GetDebugLog.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.GetDebugLogRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.GetDebugLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDebugLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDebugLogResponse()
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


    def GetDevice(self, request):
        """提供查詢某個設備詳細訊息的能力。

        :param request: Request instance for GetDevice.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.GetDeviceRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.GetDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDeviceResponse()
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


    def GetDeviceData(self, request):
        """獲取某個設備當前上報到雲端的數據，該介面适用於使用數據範本協議的産品。

        :param request: Request instance for GetDeviceData.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.GetDeviceDataRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.GetDeviceDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDeviceData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDeviceDataResponse()
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


    def GetDeviceLog(self, request):
        """批次獲取設備與雲端的詳細通信日志，該介面适用於使用高級版類型的産品。

        :param request: Request instance for GetDeviceLog.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.GetDeviceLogRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.GetDeviceLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDeviceLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDeviceLogResponse()
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


    def GetDeviceSignatures(self, request):
        """獲取設備綁定簽名，用於用戶綁定某個設備的應用場景

        :param request: Request instance for GetDeviceSignatures.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.GetDeviceSignaturesRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.GetDeviceSignaturesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDeviceSignatures", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDeviceSignaturesResponse()
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


    def GetDeviceStatistics(self, request):
        """查詢某段時間範圍内産品的在線、啟動設備數

        :param request: Request instance for GetDeviceStatistics.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.GetDeviceStatisticsRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.GetDeviceStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDeviceStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDeviceStatisticsResponse()
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


    def GetDeviceStatuses(self, request):
        """批次獲取設備的當前狀态，狀态包括在線、離線或未啟動狀态。

        :param request: Request instance for GetDeviceStatuses.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.GetDeviceStatusesRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.GetDeviceStatusesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDeviceStatuses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDeviceStatusesResponse()
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


    def GetDevices(self, request):
        """提供分頁查詢某個産品Id下設備訊息的能力。

        :param request: Request instance for GetDevices.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.GetDevicesRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.GetDevicesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDevices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDevicesResponse()
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


    def GetProduct(self, request):
        """獲取産品定義的詳細訊息，包括産品名稱、産品描述，鑒權模式等訊息。

        :param request: Request instance for GetProduct.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.GetProductRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.GetProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetProductResponse()
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


    def GetProducts(self, request):
        """獲取用戶在物聯網套件所創建的所有産品訊息。

        :param request: Request instance for GetProducts.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.GetProductsRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.GetProductsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetProducts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetProductsResponse()
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


    def GetRule(self, request):
        """獲取轉發規則訊息

        :param request: Request instance for GetRule.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.GetRuleRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.GetRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetRuleResponse()
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


    def GetRules(self, request):
        """獲取轉發規則清單

        :param request: Request instance for GetRules.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.GetRulesRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.GetRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetRulesResponse()
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


    def GetTopic(self, request):
        """獲取Topic訊息

        :param request: Request instance for GetTopic.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.GetTopicRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.GetTopicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetTopic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetTopicResponse()
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


    def GetTopics(self, request):
        """獲取Topic清單

        :param request: Request instance for GetTopics.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.GetTopicsRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.GetTopicsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetTopics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetTopicsResponse()
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


    def IssueDeviceControl(self, request):
        """提供下發控制指令到指定設備的能力，該介面适用於使用高級版類型的産品。

        :param request: Request instance for IssueDeviceControl.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.IssueDeviceControlRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.IssueDeviceControlResponse`

        """
        try:
            params = request._serialize()
            body = self.call("IssueDeviceControl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IssueDeviceControlResponse()
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


    def PublishMsg(self, request):
        """提供向指定的Topic發布訊息的能力，常用於向設備下發控制指令。該介面只适用於産品版本爲“基礎版”類型的産品，使用高級版的産品需使用“下發設備控制指令”介面

        :param request: Request instance for PublishMsg.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.PublishMsgRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.PublishMsgResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PublishMsg", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PublishMsgResponse()
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


    def ResetDevice(self, request):
        """重置設備操作，将會爲設備生成新的證書及清空最新數據，需謹慎操作。

        :param request: Request instance for ResetDevice.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.ResetDeviceRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.ResetDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetDeviceResponse()
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


    def UnassociateSubDeviceFromGatewayProduct(self, request):
        """取消子設備産品與閘道設備産品的關聯

        :param request: Request instance for UnassociateSubDeviceFromGatewayProduct.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.UnassociateSubDeviceFromGatewayProductRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.UnassociateSubDeviceFromGatewayProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnassociateSubDeviceFromGatewayProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnassociateSubDeviceFromGatewayProductResponse()
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


    def UpdateProduct(self, request):
        """提供修改産品訊息及數據範本的能力。

        :param request: Request instance for UpdateProduct.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.UpdateProductRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.UpdateProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateProductResponse()
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


    def UpdateRule(self, request):
        """更新規則

        :param request: Request instance for UpdateRule.
        :type request: :class:`taifucloudcloud.iot.v20180123.models.UpdateRuleRequest`
        :rtype: :class:`taifucloudcloud.iot.v20180123.models.UpdateRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateRuleResponse()
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