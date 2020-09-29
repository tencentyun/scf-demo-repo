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
from taifucloudcloud.tbm.v20180129 import models


class TbmClient(AbstractClient):
    _apiVersion = '2018-01-29'
    _endpoint = 'tbm.taifucloudcloudapi.com'


    def DescribeBrandCommentCount(self, request):
        """通過分析用戶在評價品牌時用詞的正負面情緒評分，返回品牌好評與差評評價條數，按天輸出結果。

        :param request: Request instance for DescribeBrandCommentCount.
        :type request: :class:`taifucloudcloud.tbm.v20180129.models.DescribeBrandCommentCountRequest`
        :rtype: :class:`taifucloudcloud.tbm.v20180129.models.DescribeBrandCommentCountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBrandCommentCount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBrandCommentCountResponse()
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


    def DescribeBrandExposure(self, request):
        """監測品牌關鍵詞命中文章標題或全文的文章篇數，按天輸出數據。

        :param request: Request instance for DescribeBrandExposure.
        :type request: :class:`taifucloudcloud.tbm.v20180129.models.DescribeBrandExposureRequest`
        :rtype: :class:`taifucloudcloud.tbm.v20180129.models.DescribeBrandExposureResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBrandExposure", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBrandExposureResponse()
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


    def DescribeBrandMediaReport(self, request):
        """監測品牌關鍵詞出現在媒體網站（新聞媒體、網絡門戶、政府網站、 公衆號、天天快報等）發布資訊標題和正文中的報道數。按天輸出結果。

        :param request: Request instance for DescribeBrandMediaReport.
        :type request: :class:`taifucloudcloud.tbm.v20180129.models.DescribeBrandMediaReportRequest`
        :rtype: :class:`taifucloudcloud.tbm.v20180129.models.DescribeBrandMediaReportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBrandMediaReport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBrandMediaReportResponse()
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


    def DescribeBrandNegComments(self, request):
        """通過分析用戶在評價品牌時用詞的正負面情緒評分，返回品牌熱門差評觀點清單。

        :param request: Request instance for DescribeBrandNegComments.
        :type request: :class:`taifucloudcloud.tbm.v20180129.models.DescribeBrandNegCommentsRequest`
        :rtype: :class:`taifucloudcloud.tbm.v20180129.models.DescribeBrandNegCommentsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBrandNegComments", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBrandNegCommentsResponse()
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


    def DescribeBrandPosComments(self, request):
        """通過分析用戶在評價品牌時用詞的正負面情緒評分，返回品牌熱門好評觀點清單。

        :param request: Request instance for DescribeBrandPosComments.
        :type request: :class:`taifucloudcloud.tbm.v20180129.models.DescribeBrandPosCommentsRequest`
        :rtype: :class:`taifucloudcloud.tbm.v20180129.models.DescribeBrandPosCommentsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBrandPosComments", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBrandPosCommentsResponse()
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


    def DescribeBrandSocialOpinion(self, request):
        """檢測品牌關鍵詞出現在 、 興趣部落、論壇、博客等個人公開貢獻資訊中的内容，每天聚合近30天熱度最高的觀點清單。

        :param request: Request instance for DescribeBrandSocialOpinion.
        :type request: :class:`taifucloudcloud.tbm.v20180129.models.DescribeBrandSocialOpinionRequest`
        :rtype: :class:`taifucloudcloud.tbm.v20180129.models.DescribeBrandSocialOpinionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBrandSocialOpinion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBrandSocialOpinionResponse()
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


    def DescribeBrandSocialReport(self, request):
        """監測品牌關鍵詞出現在 、 興趣部落、論壇、博客等個人公開貢獻資訊中的條數。按天輸出數據結果。

        :param request: Request instance for DescribeBrandSocialReport.
        :type request: :class:`taifucloudcloud.tbm.v20180129.models.DescribeBrandSocialReportRequest`
        :rtype: :class:`taifucloudcloud.tbm.v20180129.models.DescribeBrandSocialReportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBrandSocialReport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBrandSocialReportResponse()
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


    def DescribeIndustryNews(self, request):
        """根據客戶定制的行業關鍵詞，監測關鍵詞出現在媒體網站（新聞媒體、網絡門戶、政府網站、 公衆號、天天快報等）發布資訊標題和正文中的報道數，以及文章清單、來源管道、作者、發布時間等。

        :param request: Request instance for DescribeIndustryNews.
        :type request: :class:`taifucloudcloud.tbm.v20180129.models.DescribeIndustryNewsRequest`
        :rtype: :class:`taifucloudcloud.tbm.v20180129.models.DescribeIndustryNewsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIndustryNews", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIndustryNewsResponse()
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


    def DescribeUserPortrait(self, request):
        """通過分析洞察參與過品牌媒體互動的用戶，比如公開發表品牌的新聞評論、在公開社交管道發表過對品牌的評價觀點等用戶，返回用戶的畫像屬性分布，例如性别、年齡、地域、喜愛的明星、喜愛的影視。

        :param request: Request instance for DescribeUserPortrait.
        :type request: :class:`taifucloudcloud.tbm.v20180129.models.DescribeUserPortraitRequest`
        :rtype: :class:`taifucloudcloud.tbm.v20180129.models.DescribeUserPortraitResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUserPortrait", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUserPortraitResponse()
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