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
from tencentcloud.cdn.v20180606 import models


class CdnClient(AbstractClient):
    _apiVersion = '2018-06-06'
    _endpoint = 'cdn.tencentcloudapi.com'


    def DescribeCdnData(self, request):
        """DescribeCdnData 用于查詢 CDN 實時訪問監控數據，支援以下指标查詢：

        + 流量（單位爲 byte）
        + 頻寬（單位爲 bps）
        + 請求數（單位爲 次）
        + 流量命中率（單位爲 %，小數點後保留兩位）
        + 狀态碼 2xx 匯總及各 2 開頭狀态碼明細（單位爲 個）
        + 狀态碼 3xx 匯總及各 3 開頭狀态碼明細（單位爲 個）
        + 狀态碼 4xx 匯總及各 4 開頭狀态碼明細（單位爲 個）
        + 狀态碼 5xx 匯總及各 5 開頭狀态碼明細（單位爲 個）

        :param request: 調用DescribeCdnData所需參數的結構體。
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnDataRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeCdnDataResponse`

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


    def DescribeIpVisit(self, request):
        """DescribeIpVisit 用于查詢 5 分鍾活躍用戶數，及日活躍用戶數明細

        + 5 分鍾活躍用戶數：根據日志中用戶端 IP，5 分鍾粒度去重統計
        + 日活躍用戶數：根據日志中用戶端 IP，按天粒度去重統計

        :param request: 調用DescribeIpVisit所需參數的結構體。
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeIpVisitRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeIpVisitResponse`

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
        """DescribeMapInfo 用于查詢省份對應的 ID，運營商對應的 ID 訊息。

        :param request: 調用DescribeMapInfo所需參數的結構體。
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeMapInfoRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeMapInfoResponse`

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
        """DescribeOriginData 用于查詢 CDN 實時回源監控數據，支援以下指标查詢：

        + 回源流量（單位爲 byte）
        + 回源頻寬（單位爲 bps）
        + 回源請求數（單位爲 次）
        + 回源失敗請求數（單位爲 次）
        + 回源失敗率（單位爲 %，小數點後保留兩位）
        + 回源狀态碼 2xx 匯總及各 2 開頭回源狀态碼明細（單位爲 個）
        + 回源狀态碼 3xx 匯總及各 3 開頭回源狀态碼明細（單位爲 個）
        + 回源狀态碼 4xx 匯總及各 4 開頭回源狀态碼明細（單位爲 個）
        + 回源狀态碼 5xx 匯總及各 5 開頭回源狀态碼明細（單位爲 個）

        :param request: 調用DescribeOriginData所需參數的結構體。
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribeOriginDataRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribeOriginDataResponse`

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
        """DescribePayType 用于查詢用戶的計費類型，計費週期等訊息。

        :param request: 調用DescribePayType所需參數的結構體。
        :type request: :class:`tencentcloud.cdn.v20180606.models.DescribePayTypeRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DescribePayTypeResponse`

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


    def DisableCaches(self, request):
        """DisableCaches 用于禁用 CDN 上指定 URL 的訪問，禁用完成後，全網訪問會直接返回 403。（介面尚在内測中，暫未全量開放使用）

        :param request: 調用DisableCaches所需參數的結構體。
        :type request: :class:`tencentcloud.cdn.v20180606.models.DisableCachesRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DisableCachesResponse`

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


    def EnableCaches(self, request):
        """EnableCaches 用于解禁手工封禁的 URL，解禁成功後，全網生效時間約 5~10 分鍾。（介面尚在内測中，暫未全量開放使用）

        :param request: 調用EnableCaches所需參數的結構體。
        :type request: :class:`tencentcloud.cdn.v20180606.models.EnableCachesRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.EnableCachesResponse`

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


    def GetDisableRecords(self, request):
        """GetDisableRecords 用戶查詢資源禁用曆史，及 URL 當前狀态。（介面尚在内測中，暫未全量開放使用）

        :param request: 調用GetDisableRecords所需參數的結構體。
        :type request: :class:`tencentcloud.cdn.v20180606.models.GetDisableRecordsRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.GetDisableRecordsResponse`

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


    def ListTopData(self, request):
        """ListTopData 通過入參 Metric 和 Filter 組合不同，可以查詢以下排序數據：

        + 依據總流量、總請求數對訪問 URL 排序，從大至小返回 TOP 1000 URL
        + 依據總流量、總請求數對用戶端省份排序，從大至小返回省份清單
        + 依據總流量、總請求數對用戶端運營商排序，從大至小返回運營商清單
        + 依據總流量、峰值頻寬、總請求數、平均命中率、2XX/3XX/4XX/5XX 狀态碼對域名排序，從大至小返回域名清單
        + 依據總回源流量、回源峰值頻寬、總回源請求數、平均回源失敗率、2XX/3XX/4XX/5XX 回源狀态碼對域名排序，從大至小返回域名清單

        :param request: 調用ListTopData所需參數的結構體。
        :type request: :class:`tencentcloud.cdn.v20180606.models.ListTopDataRequest`
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ListTopDataResponse`

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