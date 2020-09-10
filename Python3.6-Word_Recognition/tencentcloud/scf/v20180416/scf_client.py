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
from taifucloudcloud.scf.v20180416 import models


class ScfClient(AbstractClient):
    _apiVersion = '2018-04-16'
    _endpoint = 'scf.taifucloudcloudapi.com'


    def CopyFunction(self, request):
        """複制一個函數，可以選擇将複制出的新函數放置在同一個namespace或另一個namespace。
        注：本介面**不會**複制函數的以下對象或屬性：
        1. 函數的觸發器
        2. 除了$LATEST以外的其它版本
        3. 函數配置的日志投遞到的CLS目标

        如有需要，您可以在複制後手動修改新函數。

        :param request: 調用CopyFunction所需參數的結構體。
        :type request: :class:`taifucloudcloud.scf.v20180416.models.CopyFunctionRequest`
        :rtype: :class:`taifucloudcloud.scf.v20180416.models.CopyFunctionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CopyFunction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CopyFunctionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateFunction(self, request):
        """該介面根據傳入參數創建新的函數。

        :param request: 調用CreateFunction所需參數的結構體。
        :type request: :class:`taifucloudcloud.scf.v20180416.models.CreateFunctionRequest`
        :rtype: :class:`taifucloudcloud.scf.v20180416.models.CreateFunctionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateFunction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateFunctionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTrigger(self, request):
        """該介面根據參數輸入設置新的觸發方式。

        :param request: 調用CreateTrigger所需參數的結構體。
        :type request: :class:`taifucloudcloud.scf.v20180416.models.CreateTriggerRequest`
        :rtype: :class:`taifucloudcloud.scf.v20180416.models.CreateTriggerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTrigger", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTriggerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteFunction(self, request):
        """該介面根據傳入參數删除函數。

        :param request: 調用DeleteFunction所需參數的結構體。
        :type request: :class:`taifucloudcloud.scf.v20180416.models.DeleteFunctionRequest`
        :rtype: :class:`taifucloudcloud.scf.v20180416.models.DeleteFunctionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteFunction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteFunctionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteTrigger(self, request):
        """該介面根據參數傳入删除已有的觸發方式。

        :param request: 調用DeleteTrigger所需參數的結構體。
        :type request: :class:`taifucloudcloud.scf.v20180416.models.DeleteTriggerRequest`
        :rtype: :class:`taifucloudcloud.scf.v20180416.models.DeleteTriggerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTrigger", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTriggerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetFunction(self, request):
        """該介面獲取某個函數的詳細訊息，包括名稱、代碼、處理方法、關聯觸發器和超時時間等欄位。

        :param request: 調用GetFunction所需參數的結構體。
        :type request: :class:`taifucloudcloud.scf.v20180416.models.GetFunctionRequest`
        :rtype: :class:`taifucloudcloud.scf.v20180416.models.GetFunctionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetFunction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetFunctionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetFunctionLogs(self, request):
        """該介面根據指定的日志查詢條件返回函數運作日志。

        :param request: 調用GetFunctionLogs所需參數的結構體。
        :type request: :class:`taifucloudcloud.scf.v20180416.models.GetFunctionLogsRequest`
        :rtype: :class:`taifucloudcloud.scf.v20180416.models.GetFunctionLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetFunctionLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetFunctionLogsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def Invoke(self, request):
        """該介面用于運作函數。

        :param request: 調用Invoke所需參數的結構體。
        :type request: :class:`taifucloudcloud.scf.v20180416.models.InvokeRequest`
        :rtype: :class:`taifucloudcloud.scf.v20180416.models.InvokeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("Invoke", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InvokeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListFunctions(self, request):
        """該介面根據傳入的查詢參數返回相關函數訊息。

        :param request: 調用ListFunctions所需參數的結構體。
        :type request: :class:`taifucloudcloud.scf.v20180416.models.ListFunctionsRequest`
        :rtype: :class:`taifucloudcloud.scf.v20180416.models.ListFunctionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListFunctions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListFunctionsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateFunctionCode(self, request):
        """該介面根據傳入參數更新函數代碼。

        :param request: 調用UpdateFunctionCode所需參數的結構體。
        :type request: :class:`taifucloudcloud.scf.v20180416.models.UpdateFunctionCodeRequest`
        :rtype: :class:`taifucloudcloud.scf.v20180416.models.UpdateFunctionCodeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateFunctionCode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateFunctionCodeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateFunctionConfiguration(self, request):
        """該介面根據傳入參數更新函數配置。

        :param request: 調用UpdateFunctionConfiguration所需參數的結構體。
        :type request: :class:`taifucloudcloud.scf.v20180416.models.UpdateFunctionConfigurationRequest`
        :rtype: :class:`taifucloudcloud.scf.v20180416.models.UpdateFunctionConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateFunctionConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateFunctionConfigurationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)