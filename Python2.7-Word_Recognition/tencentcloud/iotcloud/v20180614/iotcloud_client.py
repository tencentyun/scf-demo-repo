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
from taifucloudcloud.iotcloud.v20180614 import models


class IotcloudClient(AbstractClient):
    _apiVersion = '2018-06-14'
    _endpoint = 'iotcloud.taifucloudcloudapi.com'


    def CancelTask(self, request):
        """本介面（CancelTask）用于取消一個未被調度的任務。

        :param request: 調用CancelTask所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.CancelTaskRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.CancelTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CancelTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CancelTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDevice(self, request):
        """本介面（CreateDevice）用于新建一個物聯網通信設備。

        :param request: 調用CreateDevice所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.CreateDeviceRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.CreateDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDeviceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLoraDevice(self, request):
        """創建lora類型的設備

        :param request: 調用CreateLoraDevice所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.CreateLoraDeviceRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.CreateLoraDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLoraDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLoraDeviceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateMultiDevice(self, request):
        """本介面（CreateMultiDevice）用于批次創建物聯雲設備。

        :param request: 調用CreateMultiDevice所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.CreateMultiDeviceRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.CreateMultiDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMultiDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMultiDeviceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateProduct(self, request):
        """本介面（CreateProduct）用于創建一個新的物聯網通信産品

        :param request: 調用CreateProduct所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.CreateProductRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.CreateProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProductResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTask(self, request):
        """本介面（CreateTask）用于創建一個批次任務。目前此介面可以創建批次更新影子以及批次下發訊息的任務

        :param request: 調用CreateTask所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.CreateTaskRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.CreateTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTopicPolicy(self, request):
        """本介面（CreateTopicPolicy）用于創建一個Topic

        :param request: 調用CreateTopicPolicy所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.CreateTopicPolicyRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.CreateTopicPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTopicPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTopicPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTopicRule(self, request):
        """本介面（CreateTopicRule）用于創建一個規則

        :param request: 調用CreateTopicRule所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.CreateTopicRuleRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.CreateTopicRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTopicRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTopicRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """本介面（DeleteDevice）用于删除物聯網通信設備。

        :param request: 調用DeleteDevice所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.DeleteDeviceRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.DeleteDeviceResponse`

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


    def DeleteLoraDevice(self, request):
        """删除lora類型的設備

        :param request: 調用DeleteLoraDevice所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.DeleteLoraDeviceRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.DeleteLoraDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLoraDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLoraDeviceResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """本介面（DeleteProduct）用于删除一個物聯網通信産品。

        :param request: 調用DeleteProduct所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.DeleteProductRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.DeleteProductResponse`

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


    def DeleteTopicRule(self, request):
        """本介面（DeleteTopicRule）用于删除規則

        :param request: 調用DeleteTopicRule所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.DeleteTopicRuleRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.DeleteTopicRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTopicRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTopicRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDevice(self, request):
        """本介面（DescribeDevice）用于檢視設備訊息

        :param request: 調用DescribeDevice所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.DescribeDeviceRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.DescribeDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDeviceClientKey(self, request):
        """獲驗證書認證類型設備的私鑰，剛生成或者重置設備後僅可調用一次

        :param request: 調用DescribeDeviceClientKey所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.DescribeDeviceClientKeyRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.DescribeDeviceClientKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDeviceClientKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceClientKeyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDeviceShadow(self, request):
        """本介面（DescribeDeviceShadow）用于查詢虛拟設備訊息。

        :param request: 調用DescribeDeviceShadow所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.DescribeDeviceShadowRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.DescribeDeviceShadowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDeviceShadow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceShadowResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDevices(self, request):
        """本介面（DescribeDevices）用于查詢物聯網通信設備的設備清單。

        :param request: 調用DescribeDevices所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.DescribeDevicesRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.DescribeDevicesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDevices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDevicesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLoraDevice(self, request):
        """獲取lora類型設備的詳細訊息

        :param request: 調用DescribeLoraDevice所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.DescribeLoraDeviceRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.DescribeLoraDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLoraDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLoraDeviceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMultiDevTask(self, request):
        """本介面（DescribeMultiDevTask）用于查詢批次創建設備任務的執行狀态。

        :param request: 調用DescribeMultiDevTask所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.DescribeMultiDevTaskRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.DescribeMultiDevTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMultiDevTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMultiDevTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMultiDevices(self, request):
        """本介面（DescribeMultiDevices）用于查詢批次創建設備的執行結果。

        :param request: 調用DescribeMultiDevices所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.DescribeMultiDevicesRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.DescribeMultiDevicesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMultiDevices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMultiDevicesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProducts(self, request):
        """本介面（DescribeProducts）用于列出産品清單。

        :param request: 調用DescribeProducts所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.DescribeProductsRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.DescribeProductsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProducts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProductsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTask(self, request):
        """本介面（DescribeTask）用于查詢一個已創建任務的詳情，任務保留一個月

        :param request: 調用DescribeTask所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.DescribeTaskRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.DescribeTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTasks(self, request):
        """本介面（DescribeTasks）用于查詢已創建的任務清單，任務保留一個月

        :param request: 調用DescribeTasks所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.DescribeTasksRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTasksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisableTopicRule(self, request):
        """本介面（DisableTopicRule）用于禁用規則

        :param request: 調用DisableTopicRule所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.DisableTopicRuleRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.DisableTopicRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableTopicRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableTopicRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnableTopicRule(self, request):
        """本介面（EnableTopicRule）用于啓用規則

        :param request: 調用EnableTopicRule所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.EnableTopicRuleRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.EnableTopicRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableTopicRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableTopicRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PublishAsDevice(self, request):
        """模拟lora類型的設備端向服務器端發送訊息

        :param request: 調用PublishAsDevice所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.PublishAsDeviceRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.PublishAsDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PublishAsDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PublishAsDeviceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PublishMessage(self, request):
        """本介面（PublishMessage）用于向某個主題發訊息。

        :param request: 調用PublishMessage所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.PublishMessageRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.PublishMessageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PublishMessage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PublishMessageResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PublishToDevice(self, request):
        """服務器端下發訊息給lora類型的設備

        :param request: 調用PublishToDevice所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.PublishToDeviceRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.PublishToDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PublishToDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PublishToDeviceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReplaceTopicRule(self, request):
        """本介面（ReplaceTopicRule）用于修改替換規則

        :param request: 調用ReplaceTopicRule所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.ReplaceTopicRuleRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.ReplaceTopicRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReplaceTopicRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReplaceTopicRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetDeviceState(self, request):
        """重置設備的連接狀态

        :param request: 調用ResetDeviceState所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.ResetDeviceStateRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.ResetDeviceStateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetDeviceState", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetDeviceStateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateDeviceShadow(self, request):
        """本介面（UpdateDeviceShadow）用于更新虛拟設備訊息。

        :param request: 調用UpdateDeviceShadow所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.UpdateDeviceShadowRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.UpdateDeviceShadowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateDeviceShadow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateDeviceShadowResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateTopicPolicy(self, request):
        """本介面（UpdateTopicPolicy）用于更新Topic訊息

        :param request: 調用UpdateTopicPolicy所需參數的結構體。
        :type request: :class:`taifucloudcloud.iotcloud.v20180614.models.UpdateTopicPolicyRequest`
        :rtype: :class:`taifucloudcloud.iotcloud.v20180614.models.UpdateTopicPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateTopicPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateTopicPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)