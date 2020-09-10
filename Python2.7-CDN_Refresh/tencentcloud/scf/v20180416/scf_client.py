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
from tencentcloud.scf.v20180416 import models


class ScfClient(AbstractClient):
    _apiVersion = '2018-04-16'
    _endpoint = 'scf.tencentcloudapi.com'


    def CopyFunction(self, request):
        """複制一個函數，您可以選擇将複制出的新函數放置在特定的Region和Namespace。
        注：本介面**不會**複制函數的以下對象或屬性：
        1. 函數的觸發器
        2. 除了$LATEST以外的其它版本
        3. 函數配置的日志投遞到的CLS目标。

        如有需要，您可以在複制後手動配置新函數。

        :param request: Request instance for CopyFunction.
        :type request: :class:`tencentcloud.scf.v20180416.models.CopyFunctionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.CopyFunctionResponse`

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

        :param request: Request instance for CreateFunction.
        :type request: :class:`tencentcloud.scf.v20180416.models.CreateFunctionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.CreateFunctionResponse`

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


    def CreateNamespace(self, request):
        """該介面根據傳入的參數創建命名空間。

        :param request: Request instance for CreateNamespace.
        :type request: :class:`tencentcloud.scf.v20180416.models.CreateNamespaceRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.CreateNamespaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNamespace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNamespaceResponse()
                model._deserialize(response["Response"])
                return model
            else:
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

        :param request: Request instance for CreateTrigger.
        :type request: :class:`tencentcloud.scf.v20180416.models.CreateTriggerRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.CreateTriggerResponse`

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


    def DeleteAlias(self, request):
        """删除一個函數版本的别名

        :param request: Request instance for DeleteAlias.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteAliasRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteAliasResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAlias", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAliasResponse()
                model._deserialize(response["Response"])
                return model
            else:
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

        :param request: Request instance for DeleteFunction.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteFunctionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteFunctionResponse`

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


    def DeleteLayerVersion(self, request):
        """删除指定層的指定版本，被删除的版本無法再關聯到函數上，但不會影響正在引用這個層的函數。

        :param request: Request instance for DeleteLayerVersion.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteLayerVersionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteLayerVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLayerVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLayerVersionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteNamespace(self, request):
        """該介面根據傳入的參數創建命名空間。

        :param request: Request instance for DeleteNamespace.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteNamespaceRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteNamespaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNamespace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNamespaceResponse()
                model._deserialize(response["Response"])
                return model
            else:
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

        :param request: Request instance for DeleteTrigger.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteTriggerRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteTriggerResponse`

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

        :param request: Request instance for GetFunction.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetFunctionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetFunctionResponse`

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


    def GetFunctionAddress(self, request):
        """該介面用于獲取函數代碼包的下載網址。

        :param request: Request instance for GetFunctionAddress.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetFunctionAddressRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetFunctionAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetFunctionAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetFunctionAddressResponse()
                model._deserialize(response["Response"])
                return model
            else:
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

        :param request: Request instance for GetFunctionLogs.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetFunctionLogsRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetFunctionLogsResponse`

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


    def GetLayerVersion(self, request):
        """獲取層版本詳細訊息，包括用于下載層中文件的連結。

        :param request: Request instance for GetLayerVersion.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetLayerVersionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetLayerVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetLayerVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetLayerVersionResponse()
                model._deserialize(response["Response"])
                return model
            else:
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

        :param request: Request instance for Invoke.
        :type request: :class:`tencentcloud.scf.v20180416.models.InvokeRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.InvokeResponse`

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

        :param request: Request instance for ListFunctions.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListFunctionsRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListFunctionsResponse`

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


    def ListLayerVersions(self, request):
        """返回指定層的全部版本的訊息

        :param request: Request instance for ListLayerVersions.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListLayerVersionsRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListLayerVersionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListLayerVersions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListLayerVersionsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListLayers(self, request):
        """返回全部層的清單，其中包含了每個層最新版本的訊息，可以通過适配運作時進行過濾。

        :param request: Request instance for ListLayers.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListLayersRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListLayersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListLayers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListLayersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListNamespaces(self, request):
        """列出命名空間清單

        :param request: Request instance for ListNamespaces.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListNamespacesRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListNamespacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListNamespaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListNamespacesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListVersionByFunction(self, request):
        """該介面根據傳入的參數查詢函數的版本。

        :param request: Request instance for ListVersionByFunction.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListVersionByFunctionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListVersionByFunctionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListVersionByFunction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListVersionByFunctionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PublishLayerVersion(self, request):
        """使用給定的zip文件或cos對象創建一個層的新版本，每次使用相同的層的名稱調用本介面，都會生成一個新版本。

        :param request: Request instance for PublishLayerVersion.
        :type request: :class:`tencentcloud.scf.v20180416.models.PublishLayerVersionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.PublishLayerVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PublishLayerVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PublishLayerVersionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PublishVersion(self, request):
        """該介面用于用戶發布新版本函數。

        :param request: Request instance for PublishVersion.
        :type request: :class:`tencentcloud.scf.v20180416.models.PublishVersionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.PublishVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PublishVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PublishVersionResponse()
                model._deserialize(response["Response"])
                return model
            else:
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

        :param request: Request instance for UpdateFunctionCode.
        :type request: :class:`tencentcloud.scf.v20180416.models.UpdateFunctionCodeRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.UpdateFunctionCodeResponse`

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

        :param request: Request instance for UpdateFunctionConfiguration.
        :type request: :class:`tencentcloud.scf.v20180416.models.UpdateFunctionConfigurationRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.UpdateFunctionConfigurationResponse`

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


    def UpdateNamespace(self, request):
        """更新命名空間

        :param request: Request instance for UpdateNamespace.
        :type request: :class:`tencentcloud.scf.v20180416.models.UpdateNamespaceRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.UpdateNamespaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateNamespace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateNamespaceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)