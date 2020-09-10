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
from taifucloudcloud.ssl.v20191205 import models


class SslClient(AbstractClient):
    _apiVersion = '2019-12-05'
    _endpoint = 'ssl.taifucloudcloudapi.com'


    def ApplyCertificate(self, request):
        """本介面（ApplyCertificate）用于免費證書申請。

        :param request: Request instance for ApplyCertificate.
        :type request: :class:`taifucloudcloud.ssl.v20191205.models.ApplyCertificateRequest`
        :rtype: :class:`taifucloudcloud.ssl.v20191205.models.ApplyCertificateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ApplyCertificate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplyCertificateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CancelCertificateOrder(self, request):
        """取消證書訂單。

        :param request: Request instance for CancelCertificateOrder.
        :type request: :class:`taifucloudcloud.ssl.v20191205.models.CancelCertificateOrderRequest`
        :rtype: :class:`taifucloudcloud.ssl.v20191205.models.CancelCertificateOrderResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CancelCertificateOrder", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CancelCertificateOrderResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CommitCertificateInformation(self, request):
        """提交證書訂單。

        :param request: Request instance for CommitCertificateInformation.
        :type request: :class:`taifucloudcloud.ssl.v20191205.models.CommitCertificateInformationRequest`
        :rtype: :class:`taifucloudcloud.ssl.v20191205.models.CommitCertificateInformationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CommitCertificateInformation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CommitCertificateInformationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteCertificate(self, request):
        """本介面（DeleteCertificate）用于删除證書。

        :param request: Request instance for DeleteCertificate.
        :type request: :class:`taifucloudcloud.ssl.v20191205.models.DeleteCertificateRequest`
        :rtype: :class:`taifucloudcloud.ssl.v20191205.models.DeleteCertificateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCertificate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCertificateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCertificate(self, request):
        """本介面（DescribeCertificate）用于獲驗證書訊息。

        :param request: Request instance for DescribeCertificate.
        :type request: :class:`taifucloudcloud.ssl.v20191205.models.DescribeCertificateRequest`
        :rtype: :class:`taifucloudcloud.ssl.v20191205.models.DescribeCertificateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCertificate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCertificateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCertificateDetail(self, request):
        """獲驗證書詳情。

        :param request: Request instance for DescribeCertificateDetail.
        :type request: :class:`taifucloudcloud.ssl.v20191205.models.DescribeCertificateDetailRequest`
        :rtype: :class:`taifucloudcloud.ssl.v20191205.models.DescribeCertificateDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCertificateDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCertificateDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCertificateOperateLogs(self, request):
        """獲取用戶賬号下有關證書的操作日志。

        :param request: Request instance for DescribeCertificateOperateLogs.
        :type request: :class:`taifucloudcloud.ssl.v20191205.models.DescribeCertificateOperateLogsRequest`
        :rtype: :class:`taifucloudcloud.ssl.v20191205.models.DescribeCertificateOperateLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCertificateOperateLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCertificateOperateLogsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCertificates(self, request):
        """本介面（DescribeCertificates）用于獲驗證書清單。

        :param request: Request instance for DescribeCertificates.
        :type request: :class:`taifucloudcloud.ssl.v20191205.models.DescribeCertificatesRequest`
        :rtype: :class:`taifucloudcloud.ssl.v20191205.models.DescribeCertificatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCertificates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCertificatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DownloadCertificate(self, request):
        """本介面（DownloadCertificate）用于下載證書。

        :param request: Request instance for DownloadCertificate.
        :type request: :class:`taifucloudcloud.ssl.v20191205.models.DownloadCertificateRequest`
        :rtype: :class:`taifucloudcloud.ssl.v20191205.models.DownloadCertificateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DownloadCertificate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DownloadCertificateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCertificateAlias(self, request):
        """用戶傳入證書id和備注來修改證書備注。

        :param request: Request instance for ModifyCertificateAlias.
        :type request: :class:`taifucloudcloud.ssl.v20191205.models.ModifyCertificateAliasRequest`
        :rtype: :class:`taifucloudcloud.ssl.v20191205.models.ModifyCertificateAliasResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCertificateAlias", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCertificateAliasResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCertificateProject(self, request):
        """批次修改證書所屬項目。

        :param request: Request instance for ModifyCertificateProject.
        :type request: :class:`taifucloudcloud.ssl.v20191205.models.ModifyCertificateProjectRequest`
        :rtype: :class:`taifucloudcloud.ssl.v20191205.models.ModifyCertificateProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCertificateProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCertificateProjectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReplaceCertificate(self, request):
        """本介面（ReplaceCertificate）用于重頒發證書。已申請的免費證書僅支援 RSA 算法、金鑰對參數爲2048的證書重頒發，并且目前僅支援1次重頒發。

        :param request: Request instance for ReplaceCertificate.
        :type request: :class:`taifucloudcloud.ssl.v20191205.models.ReplaceCertificateRequest`
        :rtype: :class:`taifucloudcloud.ssl.v20191205.models.ReplaceCertificateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReplaceCertificate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReplaceCertificateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitCertificateInformation(self, request):
        """提交證書資料。

        :param request: Request instance for SubmitCertificateInformation.
        :type request: :class:`taifucloudcloud.ssl.v20191205.models.SubmitCertificateInformationRequest`
        :rtype: :class:`taifucloudcloud.ssl.v20191205.models.SubmitCertificateInformationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SubmitCertificateInformation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SubmitCertificateInformationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UploadCertificate(self, request):
        """本介面（UploadCertificate）用于上傳證書。

        :param request: Request instance for UploadCertificate.
        :type request: :class:`taifucloudcloud.ssl.v20191205.models.UploadCertificateRequest`
        :rtype: :class:`taifucloudcloud.ssl.v20191205.models.UploadCertificateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UploadCertificate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UploadCertificateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)