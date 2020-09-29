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
from taifucloudcloud.cdn.v20180606 import models


class CdnClient(AbstractClient):
    _apiVersion = '2018-06-06'
    _endpoint = 'cdn.taifucloudcloudapi.com'


    def AddCdnDomain(self, request):
        """AddCdnDomain 用於新增内容分發網絡加速域名。

        :param request: Request instance for AddCdnDomain.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.AddCdnDomainRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.AddCdnDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddCdnDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddCdnDomainResponse()
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


    def CreateClsLogTopic(self, request):
        """CreatClsLogTopic 用於創建日志主題。注意：一個日志集下至多可創建10個日志主題。

        :param request: Request instance for CreateClsLogTopic.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.CreateClsLogTopicRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.CreateClsLogTopicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateClsLogTopic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClsLogTopicResponse()
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


    def DeleteCdnDomain(self, request):
        """DeleteCdnDomain 用於删除指定加速域名

        :param request: Request instance for DeleteCdnDomain.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.DeleteCdnDomainRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.DeleteCdnDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCdnDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCdnDomainResponse()
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


    def DeleteClsLogTopic(self, request):
        """DeleteClsLogTopic 用於删除日志主題。注意：删除後，所有該日志主題下綁定域名的日志将不再繼續投遞至該主題，已經投遞的日志将會被全部清空。生效時間約爲 5~15 分鍾。

        :param request: Request instance for DeleteClsLogTopic.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.DeleteClsLogTopicRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.DeleteClsLogTopicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteClsLogTopic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteClsLogTopicResponse()
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


    def DescribeBillingData(self, request):
        """DescribeBillingData 用於查詢實際計費數據明細。

        :param request: Request instance for DescribeBillingData.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.DescribeBillingDataRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.DescribeBillingDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBillingData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBillingDataResponse()
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


    def DescribeCdnData(self, request):
        """DescribeCdnData 用於查詢 CDN 實時訪問監控數據，支援以下指標查詢：

        + 流量（單位爲 byte）
        + 頻寬（單位爲 bps）
        + 請求數（單位爲 次）
        + 流量命中率（單位爲 %，小數點後保留兩位）
        + 狀态碼 2xx 匯總及各 2 開頭狀态碼明細（單位爲 個）
        + 狀态碼 3xx 匯總及各 3 開頭狀态碼明細（單位爲 個）
        + 狀态碼 4xx 匯總及各 4 開頭狀态碼明細（單位爲 個）
        + 狀态碼 5xx 匯總及各 5 開頭狀态碼明細（單位爲 個）

        :param request: Request instance for DescribeCdnData.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.DescribeCdnDataRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.DescribeCdnDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCdnData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCdnDataResponse()
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


    def DescribeCdnDomainLogs(self, request):
        """DescribeCdnDomainLogs 用於查詢訪問日志下載網址，僅支援 30 天以内的境内、境外訪問日志下載連結查詢。

        :param request: Request instance for DescribeCdnDomainLogs.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.DescribeCdnDomainLogsRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.DescribeCdnDomainLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCdnDomainLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCdnDomainLogsResponse()
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


    def DescribeCdnIp(self, request):
        """DescribeCdnIp 用於查詢 CDN IP 歸屬。

        :param request: Request instance for DescribeCdnIp.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.DescribeCdnIpRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.DescribeCdnIpResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCdnIp", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCdnIpResponse()
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


    def DescribeCertDomains(self, request):
        """校驗證書並提取SSL證書中包含的域名，返回CDN已接入的域名清單，及已配置證書的域名清單

        :param request: Request instance for DescribeCertDomains.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.DescribeCertDomainsRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.DescribeCertDomainsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCertDomains", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCertDomainsResponse()
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
        """DescribeDomains 用於查詢内容分發網絡加速域名（含境内、境外）基本配置訊息，包括項目ID、服務狀态，業務類型、創建時間、更新時間等訊息。

        :param request: Request instance for DescribeDomains.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.DescribeDomainsRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.DescribeDomainsResponse`

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
        """DescribeDomainsConfig 用於查詢内容分發網絡加速域名（含境内、境外）的所有配置訊息。

        :param request: Request instance for DescribeDomainsConfig.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.DescribeDomainsConfigRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.DescribeDomainsConfigResponse`

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


    def DescribeImageConfig(self, request):
        """獲取域名圖片優化的當前配置，支援Webp、TPG、Guetzli

        :param request: Request instance for DescribeImageConfig.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.DescribeImageConfigRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.DescribeImageConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImageConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageConfigResponse()
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


    def DescribeIpStatus(self, request):
        """DescribeIpStatus 用於查詢域名所在加速平台的邊緣節點、回源節點明細
        注意事項：介面尚未全量開放，未在内測名單中的賬號不支援調用

        :param request: Request instance for DescribeIpStatus.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.DescribeIpStatusRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.DescribeIpStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIpStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIpStatusResponse()
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


    def DescribeIpVisit(self, request):
        """DescribeIpVisit 用於查詢 5 分鍾活躍用戶數，及日活躍用戶數明細

        + 5 分鍾活躍用戶數：根據日志中用戶端 IP，5 分鍾粒度去重統計
        + 日活躍用戶數：根據日志中用戶端 IP，按天粒度去重統計

        :param request: Request instance for DescribeIpVisit.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.DescribeIpVisitRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.DescribeIpVisitResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIpVisit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIpVisitResponse()
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


    def DescribeMapInfo(self, request):
        """DescribeMapInfo 用於查詢 對應的 ID，運營商對應的 ID 訊息。

        :param request: Request instance for DescribeMapInfo.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.DescribeMapInfoRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.DescribeMapInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMapInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMapInfoResponse()
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


    def DescribeOriginData(self, request):
        """DescribeOriginData 用於查詢 CDN 實時回源監控數據，支援以下指標查詢：

        + 回源流量（單位爲 byte）
        + 回源頻寬（單位爲 bps）
        + 回源請求數（單位爲 次）
        + 回源失敗請求數（單位爲 次）
        + 回源失敗率（單位爲 %，小數點後保留兩位）
        + 回源狀态碼 2xx 匯總及各 2 開頭回源狀态碼明細（單位爲 個）
        + 回源狀态碼 3xx 匯總及各 3 開頭回源狀态碼明細（單位爲 個）
        + 回源狀态碼 4xx 匯總及各 4 開頭回源狀态碼明細（單位爲 個）
        + 回源狀态碼 5xx 匯總及各 5 開頭回源狀态碼明細（單位爲 個）

        :param request: Request instance for DescribeOriginData.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.DescribeOriginDataRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.DescribeOriginDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeOriginData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOriginDataResponse()
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


    def DescribePayType(self, request):
        """DescribePayType 用於查詢用戶的計費類型，計費週期等訊息。

        :param request: Request instance for DescribePayType.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.DescribePayTypeRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.DescribePayTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePayType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePayTypeResponse()
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
        """DescribePurgeQuota 用於查詢帳戶重新整理配額和每日可用量。

        :param request: Request instance for DescribePurgeQuota.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.DescribePurgeQuotaRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.DescribePurgeQuotaResponse`

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
        """DescribePurgeTasks 用於查詢提交的 URL 重新整理、目錄重新整理記錄及執行進度，通過 PurgePathCache 與 PurgeUrlsCache 介面提交的任務均可通過此介面進行查詢。

        :param request: Request instance for DescribePurgeTasks.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.DescribePurgeTasksRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.DescribePurgeTasksResponse`

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


    def DescribePushQuota(self, request):
        """DescribePushQuota  用於查詢預熱配額和每日可用量。

        :param request: Request instance for DescribePushQuota.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.DescribePushQuotaRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.DescribePushQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePushQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePushQuotaResponse()
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


    def DescribePushTasks(self, request):
        """DescribePushTasks  用於查詢預熱任務提交曆史記錄及執行進度。
        介面灰度中，暫未全量開放，敬請期待。

        :param request: Request instance for DescribePushTasks.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.DescribePushTasksRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.DescribePushTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePushTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePushTasksResponse()
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


    def DescribeReportData(self, request):
        """DescribeReportData 用於查詢域名/項目維度的日/周/月報表數據。

        :param request: Request instance for DescribeReportData.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.DescribeReportDataRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.DescribeReportDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeReportData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReportDataResponse()
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


    def DescribeTrafficPackages(self, request):
        """DescribeTrafficPackages 用於查詢境内 CDN 流量包詳情。

        :param request: Request instance for DescribeTrafficPackages.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.DescribeTrafficPackagesRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.DescribeTrafficPackagesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTrafficPackages", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTrafficPackagesResponse()
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


    def DescribeUrlViolations(self, request):
        """DescribeUrlViolations 用於查詢被 CDN 系統掃描到的域名違規 URL 清單及當前狀态。
        對應内容分發網絡控制台【圖片 】頁面。

        :param request: Request instance for DescribeUrlViolations.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.DescribeUrlViolationsRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.DescribeUrlViolationsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUrlViolations", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUrlViolationsResponse()
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


    def DisableCaches(self, request):
        """DisableCaches 用於禁用 CDN 上指定 URL 的訪問，禁用完成後，全網訪問會直接返回 403。（介面尚在内測中，暫未全量開放使用）

        :param request: Request instance for DisableCaches.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.DisableCachesRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.DisableCachesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableCaches", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableCachesResponse()
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


    def DisableClsLogTopic(self, request):
        """DisableClsLogTopic 用於停止日志主題投遞。注意：停止後，所有綁定該日志主題域名的日志将不再繼續投遞至該主題，已經投遞的日志将會繼續保留。生效時間約爲 5~15 分鍾。

        :param request: Request instance for DisableClsLogTopic.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.DisableClsLogTopicRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.DisableClsLogTopicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableClsLogTopic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableClsLogTopicResponse()
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


    def EnableCaches(self, request):
        """EnableCaches 用於解禁手工封禁的 URL，解禁成功後，全網生效時間約 5~10 分鍾。（介面尚在内測中，暫未全量開放使用）

        :param request: Request instance for EnableCaches.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.EnableCachesRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.EnableCachesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableCaches", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableCachesResponse()
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


    def EnableClsLogTopic(self, request):
        """EnableClsLogTopic 用於啓動日志主題投遞。注意：啓動後，所有綁定該日志主題域名的日志将繼續投遞至該主題。生效時間約爲 5~15 分鍾。

        :param request: Request instance for EnableClsLogTopic.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.EnableClsLogTopicRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.EnableClsLogTopicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableClsLogTopic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableClsLogTopicResponse()
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


    def GetDisableRecords(self, request):
        """GetDisableRecords 用於查詢資源禁用曆史，及 URL 當前狀态。（介面尚在内測中，暫未全量開放使用）

        :param request: Request instance for GetDisableRecords.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.GetDisableRecordsRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.GetDisableRecordsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetDisableRecords", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDisableRecordsResponse()
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


    def ListClsLogTopics(self, request):
        """ListClsLogTopics 用於顯示日志主題清單。注意：一個日志集下至多含10個日志主題。

        :param request: Request instance for ListClsLogTopics.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.ListClsLogTopicsRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.ListClsLogTopicsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListClsLogTopics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListClsLogTopicsResponse()
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


    def ListClsTopicDomains(self, request):
        """ListClsTopicDomains 用於獲取某日志主題下綁定的域名清單。

        :param request: Request instance for ListClsTopicDomains.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.ListClsTopicDomainsRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.ListClsTopicDomainsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListClsTopicDomains", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListClsTopicDomainsResponse()
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


    def ListTopData(self, request):
        """ListTopData 通過入參 Metric 和 Filter 組合不同，可以查詢以下排序數據：

        + 依據總流量、總請求數對訪問 URL 排序，從大至小返回 TOP 1000 URL
        + 依據總流量、總請求數對用戶端 排序，從大至小返回 清單
        + 依據總流量、總請求數對用戶端運營商排序，從大至小返回運營商清單
        + 依據總流量、峰值頻寬、總請求數、平均命中率、2XX/3XX/4XX/5XX 狀态碼對域名排序，從大至小返回域名清單
        + 依據總回源流量、回源峰值頻寬、總回源請求數、平均回源失敗率、2XX/3XX/4XX/5XX 回源狀态碼對域名排序，從大至小返回域名清單

        注意：僅支援 90 天内數據查詢

        :param request: Request instance for ListTopData.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.ListTopDataRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.ListTopDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListTopData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListTopDataResponse()
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


    def ManageClsTopicDomains(self, request):
        """ManageClsTopicDomains 用於管理某日志主題下綁定的域名清單。

        :param request: Request instance for ManageClsTopicDomains.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.ManageClsTopicDomainsRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.ManageClsTopicDomainsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ManageClsTopicDomains", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ManageClsTopicDomainsResponse()
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
        """PurgePathCache 用於批次提交目錄重新整理，根據域名的加速區域進行對應區域的重新整理。
        預設情況下境内、境外加速區域每日目錄重新整理額度爲各 100 條，每次最多可提交 20 條。

        :param request: Request instance for PurgePathCache.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.PurgePathCacheRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.PurgePathCacheResponse`

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
        """PurgeUrlsCache 用於批次提交 URL 進行重新整理，根據 URL 中域名的當前加速區域進行對應區域的重新整理。
        預設情況下境内、境外加速區域每日 URL 重新整理額度各爲 10000 條，每次最多可提交 1000 條。

        :param request: Request instance for PurgeUrlsCache.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.PurgeUrlsCacheRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.PurgeUrlsCacheResponse`

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


    def PushUrlsCache(self, request):
        """PushUrlsCache 用於将指定 URL 資源清單加載至 CDN 節點，支援指定加速區域預熱。
        預設情況下境内、境外每日預熱 URL 限額爲各 1000 條，每次最多可提交 20 條。
        介面灰度中，暫未全量開放，敬請期待。

        :param request: Request instance for PushUrlsCache.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.PushUrlsCacheRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.PushUrlsCacheResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PushUrlsCache", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PushUrlsCacheResponse()
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


    def SearchClsLog(self, request):
        """SearchClsLog 用於 CLS 日志檢索。支援檢索今天，24小時（可選近7中的某一天），近7天的日志數據。

        :param request: Request instance for SearchClsLog.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.SearchClsLogRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.SearchClsLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SearchClsLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SearchClsLogResponse()
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


    def StartCdnDomain(self, request):
        """StartCdnDomain 用於啓用已停用域名的加速服務

        :param request: Request instance for StartCdnDomain.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.StartCdnDomainRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.StartCdnDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartCdnDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartCdnDomainResponse()
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


    def StopCdnDomain(self, request):
        """StopCdnDomain 用於停止域名的加速服務。
        注意：停止加速服務後，訪問至加速節點的請求将會直接返回 404。爲避免對您的業務造成影響，請在停止加速服務前将解析切走。

        :param request: Request instance for StopCdnDomain.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.StopCdnDomainRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.StopCdnDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopCdnDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopCdnDomainResponse()
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
        """UpdateDomainConfig 用於修改内容分發網絡加速域名配置訊息
        注意：如果需要更新複雜類型的配置項，必須傳遞整個對象的所有屬性，未傳遞的屬性将使用預設值，建議通過查詢介面獲取配置屬性後，直接修改後傳遞給本介面。Https配置由於證書的特殊性，更新時不用傳遞證書和金鑰欄位。

        :param request: Request instance for UpdateDomainConfig.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.UpdateDomainConfigRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.UpdateDomainConfigResponse`

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


    def UpdateImageConfig(self, request):
        """更新控制台圖片優化的相關配置，支援Webp、TPG、Guetzli

        :param request: Request instance for UpdateImageConfig.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.UpdateImageConfigRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.UpdateImageConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateImageConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateImageConfigResponse()
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


    def UpdatePayType(self, request):
        """本介面(UpdatePayType)用於修改賬號計費類型，暫不支援月結用戶或子賬號修改。

        :param request: Request instance for UpdatePayType.
        :type request: :class:`taifucloudcloud.cdn.v20180606.models.UpdatePayTypeRequest`
        :rtype: :class:`taifucloudcloud.cdn.v20180606.models.UpdatePayTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdatePayType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdatePayTypeResponse()
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