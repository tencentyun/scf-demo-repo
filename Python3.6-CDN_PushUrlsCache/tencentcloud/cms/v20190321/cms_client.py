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


    def CreateFileSample(self, request):
        """本文件适用于圖片内容安全、視訊内容安全自定義識别庫的管理。
        <br>
        通過該介面可以将圖片新增到樣本庫。

        :param request: Request instance for CreateFileSample.
        :type request: :class:`taifucloudcloud.cms.v20190321.models.CreateFileSampleRequest`
        :rtype: :class:`taifucloudcloud.cms.v20190321.models.CreateFileSampleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateFileSample", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateFileSampleResponse()
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


    def CreateTextSample(self, request):
        """本文件适用于文本内容安全、音訊内容安全自定義識别庫的管理。
        <br>
        通過該介面可以将文本新增到樣本庫。

        :param request: Request instance for CreateTextSample.
        :type request: :class:`taifucloudcloud.cms.v20190321.models.CreateTextSampleRequest`
        :rtype: :class:`taifucloudcloud.cms.v20190321.models.CreateTextSampleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTextSample", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTextSampleResponse()
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


    def DeleteFileSample(self, request):
        """本文件适用于圖片内容安全、視訊内容安全自定義識别庫的管理。
        <br>
        删除圖片樣本庫，支援批次删除，一次提交不超過20個。

        :param request: Request instance for DeleteFileSample.
        :type request: :class:`taifucloudcloud.cms.v20190321.models.DeleteFileSampleRequest`
        :rtype: :class:`taifucloudcloud.cms.v20190321.models.DeleteFileSampleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteFileSample", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteFileSampleResponse()
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


    def DeleteTextSample(self, request):
        """本文件适用于文本内容安全、音訊内容安全自定義識别庫的管理。
        <br>
        删除文本樣本庫，暫時只支援單個删除。

        :param request: Request instance for DeleteTextSample.
        :type request: :class:`taifucloudcloud.cms.v20190321.models.DeleteTextSampleRequest`
        :rtype: :class:`taifucloudcloud.cms.v20190321.models.DeleteTextSampleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTextSample", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTextSampleResponse()
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


    def DescribeFileSample(self, request):
        """本文件适用于圖片内容安全、視訊内容安全自定義識别庫的管理。
        <br>
        查詢圖片樣本庫，支援批次查詢。

        :param request: Request instance for DescribeFileSample.
        :type request: :class:`taifucloudcloud.cms.v20190321.models.DescribeFileSampleRequest`
        :rtype: :class:`taifucloudcloud.cms.v20190321.models.DescribeFileSampleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFileSample", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFileSampleResponse()
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


    def DescribeTextSample(self, request):
        """本文件适用于文本内容安全、音訊内容安全自定義識别庫的管理。
        <br>
        支援批次查詢文本樣本庫。

        :param request: Request instance for DescribeTextSample.
        :type request: :class:`taifucloudcloud.cms.v20190321.models.DescribeTextSampleRequest`
        :rtype: :class:`taifucloudcloud.cms.v20190321.models.DescribeTextSampleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTextSample", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTextSampleResponse()
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

        :param request: Request instance for ImageModeration.
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

        :param request: Request instance for TextModeration.
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