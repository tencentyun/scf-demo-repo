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
from taifucloudcloud.cws.v20180312 import models


class CwsClient(AbstractClient):
    _apiVersion = '2018-03-12'
    _endpoint = 'cws.taifucloudcloudapi.com'


    def CreateMonitors(self, request):
        """本介面（CreateMonitors）用于新增一個或多個站點的監測任務。

        :param request: 調用CreateMonitors所需參數的結構體。
        :type request: :class:`taifucloudcloud.cws.v20180312.models.CreateMonitorsRequest`
        :rtype: :class:`taifucloudcloud.cws.v20180312.models.CreateMonitorsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMonitors", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMonitorsResponse()
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


    def CreateSites(self, request):
        """本介面（CreateSites）用于新增一個或多個站點。

        :param request: 調用CreateSites所需參數的結構體。
        :type request: :class:`taifucloudcloud.cws.v20180312.models.CreateSitesRequest`
        :rtype: :class:`taifucloudcloud.cws.v20180312.models.CreateSitesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSites", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSitesResponse()
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


    def CreateSitesScans(self, request):
        """本介面（CreateSitesScans）用于新增一個或多個站點的單次掃描任務。

        :param request: 調用CreateSitesScans所需參數的結構體。
        :type request: :class:`taifucloudcloud.cws.v20180312.models.CreateSitesScansRequest`
        :rtype: :class:`taifucloudcloud.cws.v20180312.models.CreateSitesScansResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSitesScans", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSitesScansResponse()
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


    def CreateVulsMisinformation(self, request):
        """本介面（CreateVulsMisinformation）用于新增一個或多個漏洞誤報訊息。

        :param request: 調用CreateVulsMisinformation所需參數的結構體。
        :type request: :class:`taifucloudcloud.cws.v20180312.models.CreateVulsMisinformationRequest`
        :rtype: :class:`taifucloudcloud.cws.v20180312.models.CreateVulsMisinformationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateVulsMisinformation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVulsMisinformationResponse()
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


    def CreateVulsReport(self, request):
        """本介面 (CreateVulsReport) 用于生成漏洞報告并返回下載連結。

        :param request: 調用CreateVulsReport所需參數的結構體。
        :type request: :class:`taifucloudcloud.cws.v20180312.models.CreateVulsReportRequest`
        :rtype: :class:`taifucloudcloud.cws.v20180312.models.CreateVulsReportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateVulsReport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVulsReportResponse()
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


    def DeleteMonitors(self, request):
        """本介面 (DeleteMonitors) 用于删除監控任務。

        :param request: 調用DeleteMonitors所需參數的結構體。
        :type request: :class:`taifucloudcloud.cws.v20180312.models.DeleteMonitorsRequest`
        :rtype: :class:`taifucloudcloud.cws.v20180312.models.DeleteMonitorsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMonitors", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMonitorsResponse()
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


    def DeleteSites(self, request):
        """本介面 (DeleteSites) 用于删除站點。

        :param request: 調用DeleteSites所需參數的結構體。
        :type request: :class:`taifucloudcloud.cws.v20180312.models.DeleteSitesRequest`
        :rtype: :class:`taifucloudcloud.cws.v20180312.models.DeleteSitesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSites", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSitesResponse()
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


    def DescribeConfig(self, request):
        """本介面 (DescribeConfig) 用于查詢用戶配置的詳細訊息。

        :param request: 調用DescribeConfig所需參數的結構體。
        :type request: :class:`taifucloudcloud.cws.v20180312.models.DescribeConfigRequest`
        :rtype: :class:`taifucloudcloud.cws.v20180312.models.DescribeConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeConfigResponse()
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


    def DescribeMonitors(self, request):
        """本介面 (DescribeMonitors) 用于查詢一個或多個監控任務的詳細訊息。

        :param request: 調用DescribeMonitors所需參數的結構體。
        :type request: :class:`taifucloudcloud.cws.v20180312.models.DescribeMonitorsRequest`
        :rtype: :class:`taifucloudcloud.cws.v20180312.models.DescribeMonitorsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMonitors", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMonitorsResponse()
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


    def DescribeSiteQuota(self, request):
        """本介面 (DescribeSiteQuota) 用于查詢用戶購買的掃描次數總數和已使用數。

        :param request: 調用DescribeSiteQuota所需參數的結構體。
        :type request: :class:`taifucloudcloud.cws.v20180312.models.DescribeSiteQuotaRequest`
        :rtype: :class:`taifucloudcloud.cws.v20180312.models.DescribeSiteQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSiteQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSiteQuotaResponse()
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


    def DescribeSites(self, request):
        """本介面 (DescribeSites) 用于查詢一個或多個站點的詳細訊息。

        :param request: 調用DescribeSites所需參數的結構體。
        :type request: :class:`taifucloudcloud.cws.v20180312.models.DescribeSitesRequest`
        :rtype: :class:`taifucloudcloud.cws.v20180312.models.DescribeSitesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSites", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSitesResponse()
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


    def DescribeSitesVerification(self, request):
        """本介面 (DescribeSitesVerification) 用于查詢一個或多個待驗證站點的驗證訊息。

        :param request: 調用DescribeSitesVerification所需參數的結構體。
        :type request: :class:`taifucloudcloud.cws.v20180312.models.DescribeSitesVerificationRequest`
        :rtype: :class:`taifucloudcloud.cws.v20180312.models.DescribeSitesVerificationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSitesVerification", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSitesVerificationResponse()
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


    def DescribeVuls(self, request):
        """本介面 (DescribeVuls) 用于查詢一個或多個漏洞的詳細訊息。

        :param request: 調用DescribeVuls所需參數的結構體。
        :type request: :class:`taifucloudcloud.cws.v20180312.models.DescribeVulsRequest`
        :rtype: :class:`taifucloudcloud.cws.v20180312.models.DescribeVulsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVuls", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulsResponse()
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


    def DescribeVulsNumber(self, request):
        """本介面 (DescribeVulsNumber) 用于查詢用戶網站的漏洞總計數量。

        :param request: 調用DescribeVulsNumber所需參數的結構體。
        :type request: :class:`taifucloudcloud.cws.v20180312.models.DescribeVulsNumberRequest`
        :rtype: :class:`taifucloudcloud.cws.v20180312.models.DescribeVulsNumberResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVulsNumber", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulsNumberResponse()
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


    def DescribeVulsNumberTimeline(self, request):
        """本介面 (DescribeVulsNumberTimeline) 用于查詢漏洞數随時間變化統計訊息。

        :param request: 調用DescribeVulsNumberTimeline所需參數的結構體。
        :type request: :class:`taifucloudcloud.cws.v20180312.models.DescribeVulsNumberTimelineRequest`
        :rtype: :class:`taifucloudcloud.cws.v20180312.models.DescribeVulsNumberTimelineResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVulsNumberTimeline", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulsNumberTimelineResponse()
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


    def ModifyConfigAttribute(self, request):
        """本介面 (ModifyConfigAttribute) 用于修改用戶配置的屬性。

        :param request: 調用ModifyConfigAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.cws.v20180312.models.ModifyConfigAttributeRequest`
        :rtype: :class:`taifucloudcloud.cws.v20180312.models.ModifyConfigAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyConfigAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyConfigAttributeResponse()
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


    def ModifyMonitorAttribute(self, request):
        """本介面 (ModifyMonitorAttribute) 用于修改監測任務的屬性。

        :param request: 調用ModifyMonitorAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.cws.v20180312.models.ModifyMonitorAttributeRequest`
        :rtype: :class:`taifucloudcloud.cws.v20180312.models.ModifyMonitorAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMonitorAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMonitorAttributeResponse()
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


    def ModifySiteAttribute(self, request):
        """本介面 (ModifySiteAttribute) 用于修改站點的屬性。

        :param request: 調用ModifySiteAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.cws.v20180312.models.ModifySiteAttributeRequest`
        :rtype: :class:`taifucloudcloud.cws.v20180312.models.ModifySiteAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySiteAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySiteAttributeResponse()
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


    def VerifySites(self, request):
        """本介面 (VerifySites) 用于驗證一個或多個待驗證站點。

        :param request: 調用VerifySites所需參數的結構體。
        :type request: :class:`taifucloudcloud.cws.v20180312.models.VerifySitesRequest`
        :rtype: :class:`taifucloudcloud.cws.v20180312.models.VerifySitesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VerifySites", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VerifySitesResponse()
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