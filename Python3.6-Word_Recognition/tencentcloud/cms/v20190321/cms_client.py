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
from taifucloudcloud.cms.v20190321 import models


class CmsClient(AbstractClient):
    _apiVersion = '2019-03-21'
    _endpoint = 'cms.taifucloudcloudapi.com'


    def AudioModeration(self, request):
        """音訊内容檢測（Audio Moderation, AM）服務使用了波形分析、聲紋分析等技術，能識别涉黃、涉政、涉恐等違規音訊，同時支援用戶配置音訊黑庫，打擊自定義的違規内容。

        通過API直接上傳音訊即可進行檢測，對於高危部分直接屏蔽，可疑部分人工複審，從而節省審核人力，釋放業務風險。

        :param request: 調用AudioModeration所需參數的結構體。
        :type request: :class:`taifucloudcloud.cms.v20190321.models.AudioModerationRequest`
        :rtype: :class:`taifucloudcloud.cms.v20190321.models.AudioModerationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AudioModeration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AudioModerationResponse()
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


    def DescribeModerationOverview(self, request):
        """根據日期，管道和服務類型查詢識别結果概覽數據

        :param request: 調用DescribeModerationOverview所需參數的結構體。
        :type request: :class:`taifucloudcloud.cms.v20190321.models.DescribeModerationOverviewRequest`
        :rtype: :class:`taifucloudcloud.cms.v20190321.models.DescribeModerationOverviewResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeModerationOverview", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeModerationOverviewResponse()
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


    def ImageModeration(self, request):
        """圖片内容檢測服務（Image Moderation, IM）能自動掃描圖片，識别涉黃、涉恐、涉政、涉毒等有害内容，同時支援用戶配置圖片黑名單，打擊自定義的違規圖片。
        通過API獲取檢測的標簽及置信度，可直接采信高置信度的結果，人工複審低置信度的結果，從而降低人工成本，提高審核效率。

        :param request: 調用ImageModeration所需參數的結構體。
        :type request: :class:`taifucloudcloud.cms.v20190321.models.ImageModerationRequest`
        :rtype: :class:`taifucloudcloud.cms.v20190321.models.ImageModerationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImageModeration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImageModerationResponse()
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


    def TextModeration(self, request):
        """文本内容檢測（Text Moderation）服務使用了深度學習技術，識别涉黃、涉政、涉恐等有害内容，同時支援用戶配置詞庫，打擊自定義的違規文本。
        通過API介面，能檢測内容的危險等級，對於高危部分直接過濾，可疑部分人工複審，從而節省審核人力，釋放業務風險。

        :param request: 調用TextModeration所需參數的結構體。
        :type request: :class:`taifucloudcloud.cms.v20190321.models.TextModerationRequest`
        :rtype: :class:`taifucloudcloud.cms.v20190321.models.TextModerationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TextModeration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TextModerationResponse()
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


    def VideoModeration(self, request):
        """視訊内容檢測（Video Moderation, VM）服務能識别涉黃、涉政、涉恐等違規視訊，同時支援用戶配置視訊黑庫，打擊自定義的違規内容。
        通過API直接上傳視訊即可進行檢測，對於高危部分直接過濾，可疑部分人工複審，從而節省審核人力，釋放業務風險。

        :param request: 調用VideoModeration所需參數的結構體。
        :type request: :class:`taifucloudcloud.cms.v20190321.models.VideoModerationRequest`
        :rtype: :class:`taifucloudcloud.cms.v20190321.models.VideoModerationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VideoModeration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VideoModerationResponse()
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