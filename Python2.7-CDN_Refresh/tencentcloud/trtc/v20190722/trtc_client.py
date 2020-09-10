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
from tencentcloud.trtc.v20190722 import models


class TrtcClient(AbstractClient):
    _apiVersion = '2019-07-22'
    _endpoint = 'trtc.tencentcloudapi.com'


    def DescribeCallDetail(self, request):
        """查詢指定時間内的用戶清單及用戶通話質量數據。

        :param request: Request instance for DescribeCallDetail.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeCallDetailRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeCallDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCallDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCallDetailResponse()
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


    def DescribeRealtimeNetwork(self, request):
        """查詢sdkappid維度下實時網絡狀态，包括上行丢包與下行丢包。可查詢24小時内數據，查詢起止時間不超過1個小時。

        :param request: Request instance for DescribeRealtimeNetwork.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeRealtimeNetworkRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeRealtimeNetworkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRealtimeNetwork", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRealtimeNetworkResponse()
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


    def DescribeRealtimeQuality(self, request):
        """查詢sdkappid維度下實時質量數據，包括：進房成功率，首幀秒開率，音訊卡頓率，視訊卡頓率。可查詢24小時内數據，查詢起止時間不超過1個小時。

        :param request: Request instance for DescribeRealtimeQuality.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeRealtimeQualityRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeRealtimeQualityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRealtimeQuality", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRealtimeQualityResponse()
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


    def DescribeRealtimeScale(self, request):
        """查詢sdkappid維度下實時規模，可查詢24小時内數據，查詢起止時間不超過1個小時。

        :param request: Request instance for DescribeRealtimeScale.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeRealtimeScaleRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeRealtimeScaleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRealtimeScale", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRealtimeScaleResponse()
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


    def DescribeRoomInformation(self, request):
        """查詢sdkappid下的房間清單。預設返回10條通話，一次最多返回100條通話。可查詢最近5天的數據。

        :param request: Request instance for DescribeRoomInformation.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeRoomInformationRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeRoomInformationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRoomInformation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRoomInformationResponse()
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


    def DismissRoom(self, request):
        """介面說明：把房間所有用戶從房間移出，解散房間。支援所有平台，Android、iOS、Windows 和 macOS 需升級到 TRTC SDK 6.6及以上版本。

        :param request: Request instance for DismissRoom.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DismissRoomRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DismissRoomResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DismissRoom", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DismissRoomResponse()
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


    def RemoveUser(self, request):
        """介面說明：将用戶從房間移出，适用于主播/房主/管理員踢人等場景。支援所有平台，Android、iOS、Windows 和 macOS 需升級到 TRTC SDK 6.6及以上版本。

        :param request: Request instance for RemoveUser.
        :type request: :class:`tencentcloud.trtc.v20190722.models.RemoveUserRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.RemoveUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RemoveUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveUserResponse()
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