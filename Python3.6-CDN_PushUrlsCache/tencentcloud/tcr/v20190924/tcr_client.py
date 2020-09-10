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
from tencentcloud.tcr.v20190924 import models


class TcrClient(AbstractClient):
    _apiVersion = '2019-09-24'
    _endpoint = 'tcr.tencentcloudapi.com'


    def BatchDeleteImagePersonal(self, request):
        """用于在個人版映像倉庫中批次删除Tag

        :param request: Request instance for BatchDeleteImagePersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.BatchDeleteImagePersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.BatchDeleteImagePersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BatchDeleteImagePersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BatchDeleteImagePersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchDeleteRepositoryPersonal(self, request):
        """用于個人版映像倉庫中批次删除映像倉庫

        :param request: Request instance for BatchDeleteRepositoryPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.BatchDeleteRepositoryPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.BatchDeleteRepositoryPersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BatchDeleteRepositoryPersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BatchDeleteRepositoryPersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateApplicationTriggerPersonal(self, request):
        """用于創建應用更新觸發器

        :param request: Request instance for CreateApplicationTriggerPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateApplicationTriggerPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateApplicationTriggerPersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateApplicationTriggerPersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateApplicationTriggerPersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateImageLifecyclePersonal(self, request):
        """用于在個人版中創建清理策略

        :param request: Request instance for CreateImageLifecyclePersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateImageLifecyclePersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateImageLifecyclePersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateImageLifecyclePersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateImageLifecyclePersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateInstance(self, request):
        """創建實例

        :param request: Request instance for CreateInstance.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateInstanceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateInstanceToken(self, request):
        """創建實例的臨時或長期訪問憑證

        :param request: Request instance for CreateInstanceToken.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateInstanceTokenRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateInstanceTokenResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateInstanceToken", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateInstanceTokenResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """用于在企業版中創建命名空間

        :param request: Request instance for CreateNamespace.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateNamespaceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateNamespaceResponse`

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


    def CreateNamespacePersonal(self, request):
        """創建個人版映像倉庫命名空間，此命名空間全局唯一

        :param request: Request instance for CreateNamespacePersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateNamespacePersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateNamespacePersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNamespacePersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNamespacePersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateRepository(self, request):
        """用于企業版創建映像倉庫

        :param request: Request instance for CreateRepository.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateRepositoryRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateRepositoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateRepository", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRepositoryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateRepositoryPersonal(self, request):
        """用于在個人版倉庫中創建映像倉庫

        :param request: Request instance for CreateRepositoryPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateRepositoryPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateRepositoryPersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateRepositoryPersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRepositoryPersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateUserPersonal(self, request):
        """創建個人用戶

        :param request: Request instance for CreateUserPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateUserPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateUserPersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateUserPersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateUserPersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateWebhookTrigger(self, request):
        """創建觸發器

        :param request: Request instance for CreateWebhookTrigger.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateWebhookTriggerRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateWebhookTriggerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateWebhookTrigger", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateWebhookTriggerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteApplicationTriggerPersonal(self, request):
        """用于删除應用更新觸發器

        :param request: Request instance for DeleteApplicationTriggerPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteApplicationTriggerPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteApplicationTriggerPersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteApplicationTriggerPersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteApplicationTriggerPersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteImageLifecycleGlobalPersonal(self, request):
        """用于删除個人版全局映像版本自動清理策略

        :param request: Request instance for DeleteImageLifecycleGlobalPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteImageLifecycleGlobalPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteImageLifecycleGlobalPersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteImageLifecycleGlobalPersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteImageLifecycleGlobalPersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteImageLifecyclePersonal(self, request):
        """用于在個人版映像倉庫中删除倉庫Tag自動清理策略

        :param request: Request instance for DeleteImageLifecyclePersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteImageLifecyclePersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteImageLifecyclePersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteImageLifecyclePersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteImageLifecyclePersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteImagePersonal(self, request):
        """用于在個人版中删除tag

        :param request: Request instance for DeleteImagePersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteImagePersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteImagePersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteImagePersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteImagePersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteInstanceToken(self, request):
        """删除長期訪問憑證

        :param request: Request instance for DeleteInstanceToken.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteInstanceTokenRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteInstanceTokenResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteInstanceToken", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteInstanceTokenResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """删除命名空間

        :param request: Request instance for DeleteNamespace.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteNamespaceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteNamespaceResponse`

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


    def DeleteNamespacePersonal(self, request):
        """删除共享版命名空間

        :param request: Request instance for DeleteNamespacePersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteNamespacePersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteNamespacePersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNamespacePersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNamespacePersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteRepository(self, request):
        """删除映像倉庫

        :param request: Request instance for DeleteRepository.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteRepositoryRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteRepositoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteRepository", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRepositoryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteRepositoryPersonal(self, request):
        """用于個人版映像倉庫中删除

        :param request: Request instance for DeleteRepositoryPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteRepositoryPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteRepositoryPersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteRepositoryPersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRepositoryPersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteWebhookTrigger(self, request):
        """删除觸發器

        :param request: Request instance for DeleteWebhookTrigger.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteWebhookTriggerRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteWebhookTriggerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteWebhookTrigger", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteWebhookTriggerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApplicationTriggerLogPersonal(self, request):
        """用于查詢應用更新觸發器觸發日志

        :param request: Request instance for DescribeApplicationTriggerLogPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeApplicationTriggerLogPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeApplicationTriggerLogPersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeApplicationTriggerLogPersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApplicationTriggerLogPersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApplicationTriggerPersonal(self, request):
        """用于查詢應用更新觸發器

        :param request: Request instance for DescribeApplicationTriggerPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeApplicationTriggerPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeApplicationTriggerPersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeApplicationTriggerPersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApplicationTriggerPersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFavorRepositoryPersonal(self, request):
        """查詢個人收藏倉庫

        :param request: Request instance for DescribeFavorRepositoryPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeFavorRepositoryPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeFavorRepositoryPersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFavorRepositoryPersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFavorRepositoryPersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImageFilterPersonal(self, request):
        """用于在個人版中查詢與指定tag映像内容相同的tag清單

        :param request: Request instance for DescribeImageFilterPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeImageFilterPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeImageFilterPersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImageFilterPersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageFilterPersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImageLifecycleGlobalPersonal(self, request):
        """用于獲取個人版全局映像版本自動清理策略

        :param request: Request instance for DescribeImageLifecycleGlobalPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeImageLifecycleGlobalPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeImageLifecycleGlobalPersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImageLifecycleGlobalPersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageLifecycleGlobalPersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImageLifecyclePersonal(self, request):
        """用于獲取個人版倉庫中自動清理策略

        :param request: Request instance for DescribeImageLifecyclePersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeImageLifecyclePersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeImageLifecyclePersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImageLifecyclePersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageLifecyclePersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImageManifests(self, request):
        """查詢容器映像Manifest訊息

        :param request: Request instance for DescribeImageManifests.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeImageManifestsRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeImageManifestsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImageManifests", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageManifestsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImagePersonal(self, request):
        """用于獲取個人版映像倉庫tag清單

        :param request: Request instance for DescribeImagePersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeImagePersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeImagePersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImagePersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImagePersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImages(self, request):
        """查詢映像版本清單或指定容器映像訊息

        :param request: Request instance for DescribeImages.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeImagesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeImagesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImages", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImagesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstanceStatus(self, request):
        """查詢實例當前狀态以及過程訊息

        :param request: Request instance for DescribeInstanceStatus.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeInstanceStatusRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeInstanceStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstanceToken(self, request):
        """查詢長期訪問憑證訊息

        :param request: Request instance for DescribeInstanceToken.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeInstanceTokenRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeInstanceTokenResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceToken", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceTokenResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstances(self, request):
        """查詢實例訊息

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNamespacePersonal(self, request):
        """查詢個人版命名空間訊息

        :param request: Request instance for DescribeNamespacePersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeNamespacePersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeNamespacePersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNamespacePersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNamespacePersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNamespaces(self, request):
        """查詢命名空間清單或指定命名空間訊息

        :param request: Request instance for DescribeNamespaces.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeNamespacesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeNamespacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNamespaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNamespacesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRepositories(self, request):
        """查詢映像倉庫清單或指定映像倉庫訊息

        :param request: Request instance for DescribeRepositories.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeRepositoriesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeRepositoriesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRepositories", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRepositoriesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRepositoryFilterPersonal(self, request):
        """用于在個人版映像倉庫中，獲取滿足輸入搜索條件的用戶映像倉庫

        :param request: Request instance for DescribeRepositoryFilterPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeRepositoryFilterPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeRepositoryFilterPersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRepositoryFilterPersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRepositoryFilterPersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRepositoryOwnerPersonal(self, request):
        """用于在個人版中獲取用戶全部的映像倉庫清單

        :param request: Request instance for DescribeRepositoryOwnerPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeRepositoryOwnerPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeRepositoryOwnerPersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRepositoryOwnerPersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRepositoryOwnerPersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRepositoryPersonal(self, request):
        """查詢個人版倉庫訊息

        :param request: Request instance for DescribeRepositoryPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeRepositoryPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeRepositoryPersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRepositoryPersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRepositoryPersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUserQuotaPersonal(self, request):
        """查詢個人用戶配額

        :param request: Request instance for DescribeUserQuotaPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeUserQuotaPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeUserQuotaPersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUserQuotaPersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUserQuotaPersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWebhookTrigger(self, request):
        """查詢觸發器

        :param request: Request instance for DescribeWebhookTrigger.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeWebhookTriggerRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeWebhookTriggerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWebhookTrigger", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWebhookTriggerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWebhookTriggerLog(self, request):
        """獲取觸發器日志

        :param request: Request instance for DescribeWebhookTriggerLog.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeWebhookTriggerLogRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeWebhookTriggerLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWebhookTriggerLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWebhookTriggerLogResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DuplicateImagePersonal(self, request):
        """用于在個人版映像倉庫中複制映像版本

        :param request: Request instance for DuplicateImagePersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DuplicateImagePersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DuplicateImagePersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DuplicateImagePersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DuplicateImagePersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ManageImageLifecycleGlobalPersonal(self, request):
        """用于設置個人版全局映像版本自動清理策略

        :param request: Request instance for ManageImageLifecycleGlobalPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ManageImageLifecycleGlobalPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ManageImageLifecycleGlobalPersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ManageImageLifecycleGlobalPersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ManageImageLifecycleGlobalPersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyApplicationTriggerPersonal(self, request):
        """用于修改應用更新觸發器

        :param request: Request instance for ModifyApplicationTriggerPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyApplicationTriggerPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyApplicationTriggerPersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyApplicationTriggerPersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyApplicationTriggerPersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyInstanceToken(self, request):
        """更新實例内指定長期訪問憑證的啓用狀态

        :param request: Request instance for ModifyInstanceToken.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyInstanceTokenRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyInstanceTokenResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstanceToken", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstanceTokenResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyNamespace(self, request):
        """更新命名空間訊息，當前僅支援修改命名空間訪問級别

        :param request: Request instance for ModifyNamespace.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyNamespaceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyNamespaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNamespace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNamespaceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyRepository(self, request):
        """更新映像倉庫訊息，可修改倉庫描述訊息

        :param request: Request instance for ModifyRepository.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyRepositoryRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyRepositoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyRepository", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRepositoryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyRepositoryAccessPersonal(self, request):
        """用于更新個人版映像倉庫的訪問屬性

        :param request: Request instance for ModifyRepositoryAccessPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyRepositoryAccessPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyRepositoryAccessPersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyRepositoryAccessPersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRepositoryAccessPersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyRepositoryInfoPersonal(self, request):
        """用于在個人版映像倉庫中更新容器映像描述

        :param request: Request instance for ModifyRepositoryInfoPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyRepositoryInfoPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyRepositoryInfoPersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyRepositoryInfoPersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRepositoryInfoPersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyUserPasswordPersonal(self, request):
        """修改個人用戶登入密碼

        :param request: Request instance for ModifyUserPasswordPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyUserPasswordPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyUserPasswordPersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyUserPasswordPersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyUserPasswordPersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyWebhookTrigger(self, request):
        """更新觸發器

        :param request: Request instance for ModifyWebhookTrigger.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyWebhookTriggerRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyWebhookTriggerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyWebhookTrigger", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyWebhookTriggerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ValidateNamespaceExistPersonal(self, request):
        """查詢個人版用戶命名空間是否存在

        :param request: Request instance for ValidateNamespaceExistPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ValidateNamespaceExistPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ValidateNamespaceExistPersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ValidateNamespaceExistPersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ValidateNamespaceExistPersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ValidateRepositoryExistPersonal(self, request):
        """用于判斷個人版倉庫是否存在

        :param request: Request instance for ValidateRepositoryExistPersonal.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ValidateRepositoryExistPersonalRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ValidateRepositoryExistPersonalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ValidateRepositoryExistPersonal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ValidateRepositoryExistPersonalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)