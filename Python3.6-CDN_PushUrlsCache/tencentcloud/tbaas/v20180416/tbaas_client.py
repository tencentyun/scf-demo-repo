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
from taifucloudcloud.tbaas.v20180416 import models


class TbaasClient(AbstractClient):
    _apiVersion = '2018-04-16'
    _endpoint = 'tbaas.taifucloudcloudapi.com'


    def ApplyUserCert(self, request):
        """申請用戶證書

        :param request: Request instance for ApplyUserCert.
        :type request: :class:`taifucloudcloud.tbaas.v20180416.models.ApplyUserCertRequest`
        :rtype: :class:`taifucloudcloud.tbaas.v20180416.models.ApplyUserCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ApplyUserCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplyUserCertResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BlockByNumberHandler(self, request):
        """Bcos根據塊高查詢區塊訊息

        :param request: Request instance for BlockByNumberHandler.
        :type request: :class:`taifucloudcloud.tbaas.v20180416.models.BlockByNumberHandlerRequest`
        :rtype: :class:`taifucloudcloud.tbaas.v20180416.models.BlockByNumberHandlerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BlockByNumberHandler", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BlockByNumberHandlerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeployDynamicContractHandler(self, request):
        """動态佈署合約

        :param request: Request instance for DeployDynamicContractHandler.
        :type request: :class:`taifucloudcloud.tbaas.v20180416.models.DeployDynamicContractHandlerRequest`
        :rtype: :class:`taifucloudcloud.tbaas.v20180416.models.DeployDynamicContractHandlerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeployDynamicContractHandler", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeployDynamicContractHandlerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DownloadUserCert(self, request):
        """下載用戶證書

        :param request: Request instance for DownloadUserCert.
        :type request: :class:`taifucloudcloud.tbaas.v20180416.models.DownloadUserCertRequest`
        :rtype: :class:`taifucloudcloud.tbaas.v20180416.models.DownloadUserCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DownloadUserCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DownloadUserCertResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetBlockList(self, request):
        """檢視當前網絡下的所有區塊清單，分頁展示

        :param request: Request instance for GetBlockList.
        :type request: :class:`taifucloudcloud.tbaas.v20180416.models.GetBlockListRequest`
        :rtype: :class:`taifucloudcloud.tbaas.v20180416.models.GetBlockListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetBlockList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetBlockListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetBlockListHandler(self, request):
        """Bcos分頁查詢當前群組下的區塊清單

        :param request: Request instance for GetBlockListHandler.
        :type request: :class:`taifucloudcloud.tbaas.v20180416.models.GetBlockListHandlerRequest`
        :rtype: :class:`taifucloudcloud.tbaas.v20180416.models.GetBlockListHandlerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetBlockListHandler", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetBlockListHandlerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetBlockTransactionListForUser(self, request):
        """獲取區塊内的交易清單

        :param request: Request instance for GetBlockTransactionListForUser.
        :type request: :class:`taifucloudcloud.tbaas.v20180416.models.GetBlockTransactionListForUserRequest`
        :rtype: :class:`taifucloudcloud.tbaas.v20180416.models.GetBlockTransactionListForUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetBlockTransactionListForUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetBlockTransactionListForUserResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetClusterSummary(self, request):
        """獲取區塊鏈網絡概要

        :param request: Request instance for GetClusterSummary.
        :type request: :class:`taifucloudcloud.tbaas.v20180416.models.GetClusterSummaryRequest`
        :rtype: :class:`taifucloudcloud.tbaas.v20180416.models.GetClusterSummaryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetClusterSummary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetClusterSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetInvokeTx(self, request):
        """Invoke異步調用結果查詢

        :param request: Request instance for GetInvokeTx.
        :type request: :class:`taifucloudcloud.tbaas.v20180416.models.GetInvokeTxRequest`
        :rtype: :class:`taifucloudcloud.tbaas.v20180416.models.GetInvokeTxResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetInvokeTx", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetInvokeTxResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetLatesdTransactionList(self, request):
        """獲取最新交易清單

        :param request: Request instance for GetLatesdTransactionList.
        :type request: :class:`taifucloudcloud.tbaas.v20180416.models.GetLatesdTransactionListRequest`
        :rtype: :class:`taifucloudcloud.tbaas.v20180416.models.GetLatesdTransactionListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetLatesdTransactionList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetLatesdTransactionListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetTransByHashHandler(self, request):
        """Bcos根據交易哈希檢視交易詳細訊息

        :param request: Request instance for GetTransByHashHandler.
        :type request: :class:`taifucloudcloud.tbaas.v20180416.models.GetTransByHashHandlerRequest`
        :rtype: :class:`taifucloudcloud.tbaas.v20180416.models.GetTransByHashHandlerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetTransByHashHandler", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetTransByHashHandlerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetTransListHandler(self, request):
        """Bcos分頁查詢當前群組的交易訊息清單

        :param request: Request instance for GetTransListHandler.
        :type request: :class:`taifucloudcloud.tbaas.v20180416.models.GetTransListHandlerRequest`
        :rtype: :class:`taifucloudcloud.tbaas.v20180416.models.GetTransListHandlerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetTransListHandler", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetTransListHandlerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetTransactionDetailForUser(self, request):
        """獲取交易詳情

        :param request: Request instance for GetTransactionDetailForUser.
        :type request: :class:`taifucloudcloud.tbaas.v20180416.models.GetTransactionDetailForUserRequest`
        :rtype: :class:`taifucloudcloud.tbaas.v20180416.models.GetTransactionDetailForUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetTransactionDetailForUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetTransactionDetailForUserResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """新增交易

        :param request: Request instance for Invoke.
        :type request: :class:`taifucloudcloud.tbaas.v20180416.models.InvokeRequest`
        :rtype: :class:`taifucloudcloud.tbaas.v20180416.models.InvokeResponse`

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


    def Query(self, request):
        """查詢交易

        :param request: Request instance for Query.
        :type request: :class:`taifucloudcloud.tbaas.v20180416.models.QueryRequest`
        :rtype: :class:`taifucloudcloud.tbaas.v20180416.models.QueryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("Query", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SendTransactionHandler(self, request):
        """Bcos發送交易

        :param request: Request instance for SendTransactionHandler.
        :type request: :class:`taifucloudcloud.tbaas.v20180416.models.SendTransactionHandlerRequest`
        :rtype: :class:`taifucloudcloud.tbaas.v20180416.models.SendTransactionHandlerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SendTransactionHandler", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SendTransactionHandlerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SrvInvoke(self, request):
        """trustsql服務統一介面

        :param request: Request instance for SrvInvoke.
        :type request: :class:`taifucloudcloud.tbaas.v20180416.models.SrvInvokeRequest`
        :rtype: :class:`taifucloudcloud.tbaas.v20180416.models.SrvInvokeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SrvInvoke", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SrvInvokeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TransByDynamicContractHandler(self, request):
        """根據動态佈署的合約發送交易

        :param request: Request instance for TransByDynamicContractHandler.
        :type request: :class:`taifucloudcloud.tbaas.v20180416.models.TransByDynamicContractHandlerRequest`
        :rtype: :class:`taifucloudcloud.tbaas.v20180416.models.TransByDynamicContractHandlerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TransByDynamicContractHandler", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TransByDynamicContractHandlerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)