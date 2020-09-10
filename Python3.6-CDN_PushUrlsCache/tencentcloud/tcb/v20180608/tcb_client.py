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
from tencentcloud.tcb.v20180608 import models


class TcbClient(AbstractClient):
    _apiVersion = '2018-06-08'
    _endpoint = 'tcb.tencentcloudapi.com'


    def CheckTcbService(self, request):
        """檢查是否開通Tcb服務

        :param request: Request instance for CheckTcbService.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CheckTcbServiceRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CheckTcbServiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckTcbService", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckTcbServiceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CommonServiceAPI(self, request):
        """TCB雲API統一入口

        :param request: Request instance for CommonServiceAPI.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CommonServiceAPIRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CommonServiceAPIResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CommonServiceAPI", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CommonServiceAPIResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAuthDomain(self, request):
        """增加安全域名

        :param request: Request instance for CreateAuthDomain.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateAuthDomainRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateAuthDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAuthDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAuthDomainResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateHostingDomain(self, request):
        """創建托管域名

        :param request: Request instance for CreateHostingDomain.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateHostingDomainRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateHostingDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateHostingDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateHostingDomainResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateStaticStore(self, request):
        """創建靜态托管資源，包括COS和CDN，異步任務創建，檢視創建結果需要根據DescribeStaticStore介面來檢視

        :param request: Request instance for CreateStaticStore.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateStaticStoreRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateStaticStoreResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateStaticStore", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateStaticStoreResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteEndUser(self, request):
        """删除終端用戶

        :param request: Request instance for DeleteEndUser.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DeleteEndUserRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DeleteEndUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteEndUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteEndUserResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAuthDomains(self, request):
        """獲取安全域名清單

        :param request: Request instance for DescribeAuthDomains.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeAuthDomainsRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeAuthDomainsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAuthDomains", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAuthDomainsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDatabaseACL(self, request):
        """獲取資料庫權限

        :param request: Request instance for DescribeDatabaseACL.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeDatabaseACLRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeDatabaseACLResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDatabaseACL", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDatabaseACLResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEndUsers(self, request):
        """獲取終端用戶清單

        :param request: Request instance for DescribeEndUsers.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeEndUsersRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeEndUsersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEndUsers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEndUsersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEnvFreeQuota(self, request):
        """查詢後付費免費配額訊息

        :param request: Request instance for DescribeEnvFreeQuota.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvFreeQuotaRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvFreeQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEnvFreeQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEnvFreeQuotaResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEnvLimit(self, request):
        """查詢環境個數上限

        :param request: Request instance for DescribeEnvLimit.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvLimitRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvLimitResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEnvLimit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEnvLimitResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEnvs(self, request):
        """獲取環境清單，含環境下的各個資源訊息。尤其是各資源的唯一标識，是請求各資源的關鍵參數

        :param request: Request instance for DescribeEnvs.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvsRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEnvs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEnvsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeQuotaData(self, request):
        """查詢指定指标的配額使用量

        :param request: Request instance for DescribeQuotaData.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeQuotaDataRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeQuotaDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeQuotaData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeQuotaDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DestroyEnv(self, request):
        """銷毀環境

        :param request: Request instance for DestroyEnv.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DestroyEnvRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DestroyEnvResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DestroyEnv", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DestroyEnvResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DestroyStaticStore(self, request):
        """銷毀靜态托管資源，該介面創建異步銷毀任務，資源最終狀态可從DestroyStaticStore介面檢視

        :param request: Request instance for DestroyStaticStore.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DestroyStaticStoreRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DestroyStaticStoreResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DestroyStaticStore", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DestroyStaticStoreResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDatabaseACL(self, request):
        """修改資料庫權限

        :param request: Request instance for ModifyDatabaseACL.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ModifyDatabaseACLRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifyDatabaseACLResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDatabaseACL", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDatabaseACLResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyEnv(self, request):
        """更新環境訊息

        :param request: Request instance for ModifyEnv.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ModifyEnvRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifyEnvResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyEnv", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyEnvResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReinstateEnv(self, request):
        """針對已隔離的免費環境，可以通過本介面将其恢複訪問。

        :param request: Request instance for ReinstateEnv.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ReinstateEnvRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ReinstateEnvResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReinstateEnv", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReinstateEnvResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)