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
from taifucloudcloud.ecdn.v20191012 import models


class EcdnClient(AbstractClient):
    _apiVersion = '2019-10-12'
    _endpoint = 'ecdn.taifucloudcloudapi.com'


    def AddEcdnDomain(self, request):
        """本介面（AddEcdnDomain）用於創建加速域名。

        :param request: Request instance for AddEcdnDomain.
        :type request: :class:`taifucloudcloud.ecdn.v20191012.models.AddEcdnDomainRequest`
        :rtype: :class:`taifucloudcloud.ecdn.v20191012.models.AddEcdnDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddEcdnDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddEcdnDomainResponse()
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


    def DeleteEcdnDomain(self, request):
        """本介面（DeleteEcdnDomain）用於删除指定加速域名。待删除域名必須處於已停用狀态。

        :param request: Request instance for DeleteEcdnDomain.
        :type request: :class:`taifucloudcloud.ecdn.v20191012.models.DeleteEcdnDomainRequest`
        :rtype: :class:`taifucloudcloud.ecdn.v20191012.models.DeleteEcdnDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteEcdnDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteEcdnDomainResponse()
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


    def DescribeDomains(self, request):
        """本介面（DescribeDomains）用於查詢CDN域名基本訊息，包括項目id，狀态，業務類型，創建時間，更新時間等。

        :param request: Request instance for DescribeDomains.
        :type request: :class:`taifucloudcloud.ecdn.v20191012.models.DescribeDomainsRequest`
        :rtype: :class:`taifucloudcloud.ecdn.v20191012.models.DescribeDomainsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDomains", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDomainsResponse()
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


    def DescribeDomainsConfig(self, request):
        """本介面（DescribeDomainsConfig）用於查詢CDN加速域名詳細配置訊息。

        :param request: Request instance for DescribeDomainsConfig.
        :type request: :class:`taifucloudcloud.ecdn.v20191012.models.DescribeDomainsConfigRequest`
        :rtype: :class:`taifucloudcloud.ecdn.v20191012.models.DescribeDomainsConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDomainsConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDomainsConfigResponse()
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


    def DescribeEcdnDomainLogs(self, request):
        """本介面（DescribeEcdnDomainLogs）用於查詢域名的訪問日志下載網址。

        :param request: Request instance for DescribeEcdnDomainLogs.
        :type request: :class:`taifucloudcloud.ecdn.v20191012.models.DescribeEcdnDomainLogsRequest`
        :rtype: :class:`taifucloudcloud.ecdn.v20191012.models.DescribeEcdnDomainLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEcdnDomainLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEcdnDomainLogsResponse()
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


    def DescribeEcdnDomainStatistics(self, request):
        """本介面（DescribeEcdnDomainStatistics）用於查詢指定時間段内的域名訪問統計指標

        :param request: Request instance for DescribeEcdnDomainStatistics.
        :type request: :class:`taifucloudcloud.ecdn.v20191012.models.DescribeEcdnDomainStatisticsRequest`
        :rtype: :class:`taifucloudcloud.ecdn.v20191012.models.DescribeEcdnDomainStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEcdnDomainStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEcdnDomainStatisticsResponse()
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


    def DescribeEcdnStatistics(self, request):
        """DescribeEcdnStatistics用於查詢 ECDN 實時訪問監控數據，支援以下指標查詢：

        + 流量（單位爲 byte）
        + 頻寬（單位爲 bps）
        + 請求數（單位爲 次）
        + 響應時間（單位爲ms）
        + 狀态碼 2xx 匯總及各 2 開頭狀态碼明細（單位爲 個）
        + 狀态碼 3xx 匯總及各 3 開頭狀态碼明細（單位爲 個）
        + 狀态碼 4xx 匯總及各 4 開頭狀态碼明細（單位爲 個）
        + 狀态碼 5xx 匯總及各 5 開頭狀态碼明細（單位爲 個）

        :param request: Request instance for DescribeEcdnStatistics.
        :type request: :class:`taifucloudcloud.ecdn.v20191012.models.DescribeEcdnStatisticsRequest`
        :rtype: :class:`taifucloudcloud.ecdn.v20191012.models.DescribeEcdnStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEcdnStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEcdnStatisticsResponse()
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


    def DescribePurgeQuota(self, request):
        """查詢重新整理介面的用量配額。

        :param request: Request instance for DescribePurgeQuota.
        :type request: :class:`taifucloudcloud.ecdn.v20191012.models.DescribePurgeQuotaRequest`
        :rtype: :class:`taifucloudcloud.ecdn.v20191012.models.DescribePurgeQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePurgeQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePurgeQuotaResponse()
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


    def DescribePurgeTasks(self, request):
        """DescribePurgeTasks 用於查詢重新整理任務提交曆史記錄及執行進度。

        :param request: Request instance for DescribePurgeTasks.
        :type request: :class:`taifucloudcloud.ecdn.v20191012.models.DescribePurgeTasksRequest`
        :rtype: :class:`taifucloudcloud.ecdn.v20191012.models.DescribePurgeTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePurgeTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePurgeTasksResponse()
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


    def PurgePathCache(self, request):
        """PurgeUrlsCache 用於批次重新整理目錄快取，一次提交将返回一個重新整理任務id。

        :param request: Request instance for PurgePathCache.
        :type request: :class:`taifucloudcloud.ecdn.v20191012.models.PurgePathCacheRequest`
        :rtype: :class:`taifucloudcloud.ecdn.v20191012.models.PurgePathCacheResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PurgePathCache", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PurgePathCacheResponse()
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


    def PurgeUrlsCache(self, request):
        """PurgeUrlsCache 用於批次重新整理Url，一次提交将返回一個重新整理任務id。

        :param request: Request instance for PurgeUrlsCache.
        :type request: :class:`taifucloudcloud.ecdn.v20191012.models.PurgeUrlsCacheRequest`
        :rtype: :class:`taifucloudcloud.ecdn.v20191012.models.PurgeUrlsCacheResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PurgeUrlsCache", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PurgeUrlsCacheResponse()
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


    def StartEcdnDomain(self, request):
        """本介面（StartEcdnDomain）用於啓用加速域名，待啓用域名必須處於已下線狀态。

        :param request: Request instance for StartEcdnDomain.
        :type request: :class:`taifucloudcloud.ecdn.v20191012.models.StartEcdnDomainRequest`
        :rtype: :class:`taifucloudcloud.ecdn.v20191012.models.StartEcdnDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartEcdnDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartEcdnDomainResponse()
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


    def StopEcdnDomain(self, request):
        """本介面（StopCdnDomain）用於停止加速域名，待停用加速域名必須處於已上線或佈署中狀态。

        :param request: Request instance for StopEcdnDomain.
        :type request: :class:`taifucloudcloud.ecdn.v20191012.models.StopEcdnDomainRequest`
        :rtype: :class:`taifucloudcloud.ecdn.v20191012.models.StopEcdnDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopEcdnDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopEcdnDomainResponse()
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


    def UpdateDomainConfig(self, request):
        """本介面（UpdateDomainConfig）用於更新ECDN加速域名配置訊息。
        注意：如果需要更新複雜類型的配置項，必須傳遞整個對象的所有屬性，未傳遞的屬性将使用預設值。建議通過查詢介面獲取配置屬性後，直接修改後傳遞給本介面。Https配置由於證書的特殊性，更新時不用傳遞證書和金鑰欄位。

        :param request: Request instance for UpdateDomainConfig.
        :type request: :class:`taifucloudcloud.ecdn.v20191012.models.UpdateDomainConfigRequest`
        :rtype: :class:`taifucloudcloud.ecdn.v20191012.models.UpdateDomainConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateDomainConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateDomainConfigResponse()
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