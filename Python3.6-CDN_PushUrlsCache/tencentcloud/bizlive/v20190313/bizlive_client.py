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
from tencentcloud.bizlive.v20190313 import models


class BizliveClient(AbstractClient):
    _apiVersion = '2019-03-13'
    _endpoint = 'bizlive.tencentcloudapi.com'


    def CreateSession(self, request):
        """創建會話

        :param request: Request instance for CreateSession.
        :type request: :class:`tencentcloud.bizlive.v20190313.models.CreateSessionRequest`
        :rtype: :class:`tencentcloud.bizlive.v20190313.models.CreateSessionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSession", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSessionResponse()
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


    def DescribeStreamPlayInfoList(self, request):
        """查詢播放數據，支援按流名稱查詢詳細播放數據，也可按播放域名查詢詳細總數據。

        :param request: Request instance for DescribeStreamPlayInfoList.
        :type request: :class:`tencentcloud.bizlive.v20190313.models.DescribeStreamPlayInfoListRequest`
        :rtype: :class:`tencentcloud.bizlive.v20190313.models.DescribeStreamPlayInfoListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStreamPlayInfoList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStreamPlayInfoListResponse()
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


    def DescribeWorkers(self, request):
        """查詢空閑機器數量

        :param request: Request instance for DescribeWorkers.
        :type request: :class:`tencentcloud.bizlive.v20190313.models.DescribeWorkersRequest`
        :rtype: :class:`tencentcloud.bizlive.v20190313.models.DescribeWorkersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWorkers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWorkersResponse()
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


    def ForbidLiveStream(self, request):
        """禁止某條流的推送，可以預設某個時刻将流恢複。

        :param request: Request instance for ForbidLiveStream.
        :type request: :class:`tencentcloud.bizlive.v20190313.models.ForbidLiveStreamRequest`
        :rtype: :class:`tencentcloud.bizlive.v20190313.models.ForbidLiveStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ForbidLiveStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ForbidLiveStreamResponse()
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


    def RegisterIM(self, request):
        """注冊聊天室

        :param request: Request instance for RegisterIM.
        :type request: :class:`tencentcloud.bizlive.v20190313.models.RegisterIMRequest`
        :rtype: :class:`tencentcloud.bizlive.v20190313.models.RegisterIMResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RegisterIM", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RegisterIMResponse()
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


    def StopGame(self, request):
        """強制登出遊戲

        :param request: Request instance for StopGame.
        :type request: :class:`tencentcloud.bizlive.v20190313.models.StopGameRequest`
        :rtype: :class:`tencentcloud.bizlive.v20190313.models.StopGameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopGame", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopGameResponse()
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