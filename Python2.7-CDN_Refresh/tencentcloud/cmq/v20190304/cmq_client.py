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
from taifucloudcloud.cmq.v20190304 import models


class CmqClient(AbstractClient):
    _apiVersion = '2019-03-04'
    _endpoint = 'cmq.taifucloudcloudapi.com'


    def ClearQueue(self, request):
        """清除queue中的所有訊息

        :param request: Request instance for ClearQueue.
        :type request: :class:`taifucloudcloud.cmq.v20190304.models.ClearQueueRequest`
        :rtype: :class:`taifucloudcloud.cmq.v20190304.models.ClearQueueResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ClearQueue", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ClearQueueResponse()
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


    def ClearSubscriptionFilterTags(self, request):
        """清空訂閱者訊息標簽

        :param request: Request instance for ClearSubscriptionFilterTags.
        :type request: :class:`taifucloudcloud.cmq.v20190304.models.ClearSubscriptionFilterTagsRequest`
        :rtype: :class:`taifucloudcloud.cmq.v20190304.models.ClearSubscriptionFilterTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ClearSubscriptionFilterTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ClearSubscriptionFilterTagsResponse()
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


    def CreateQueue(self, request):
        """創建隊列介面

        :param request: Request instance for CreateQueue.
        :type request: :class:`taifucloudcloud.cmq.v20190304.models.CreateQueueRequest`
        :rtype: :class:`taifucloudcloud.cmq.v20190304.models.CreateQueueResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateQueue", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateQueueResponse()
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


    def CreateSubscribe(self, request):
        """創建訂閱介面

        :param request: Request instance for CreateSubscribe.
        :type request: :class:`taifucloudcloud.cmq.v20190304.models.CreateSubscribeRequest`
        :rtype: :class:`taifucloudcloud.cmq.v20190304.models.CreateSubscribeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSubscribe", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSubscribeResponse()
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


    def CreateTopic(self, request):
        """創建主題

        :param request: Request instance for CreateTopic.
        :type request: :class:`taifucloudcloud.cmq.v20190304.models.CreateTopicRequest`
        :rtype: :class:`taifucloudcloud.cmq.v20190304.models.CreateTopicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTopic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTopicResponse()
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


    def DeleteQueue(self, request):
        """DeleteQueue

        :param request: Request instance for DeleteQueue.
        :type request: :class:`taifucloudcloud.cmq.v20190304.models.DeleteQueueRequest`
        :rtype: :class:`taifucloudcloud.cmq.v20190304.models.DeleteQueueResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteQueue", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteQueueResponse()
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


    def DeleteSubscribe(self, request):
        """删除訂閱

        :param request: Request instance for DeleteSubscribe.
        :type request: :class:`taifucloudcloud.cmq.v20190304.models.DeleteSubscribeRequest`
        :rtype: :class:`taifucloudcloud.cmq.v20190304.models.DeleteSubscribeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSubscribe", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSubscribeResponse()
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


    def DeleteTopic(self, request):
        """删除主題

        :param request: Request instance for DeleteTopic.
        :type request: :class:`taifucloudcloud.cmq.v20190304.models.DeleteTopicRequest`
        :rtype: :class:`taifucloudcloud.cmq.v20190304.models.DeleteTopicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTopic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTopicResponse()
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


    def DescribeDeadLetterSourceQueues(self, request):
        """列舉死信隊列源隊列

        :param request: Request instance for DescribeDeadLetterSourceQueues.
        :type request: :class:`taifucloudcloud.cmq.v20190304.models.DescribeDeadLetterSourceQueuesRequest`
        :rtype: :class:`taifucloudcloud.cmq.v20190304.models.DescribeDeadLetterSourceQueuesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDeadLetterSourceQueues", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeadLetterSourceQueuesResponse()
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


    def DescribeQueueDetail(self, request):
        """列舉隊列

        :param request: Request instance for DescribeQueueDetail.
        :type request: :class:`taifucloudcloud.cmq.v20190304.models.DescribeQueueDetailRequest`
        :rtype: :class:`taifucloudcloud.cmq.v20190304.models.DescribeQueueDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeQueueDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeQueueDetailResponse()
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


    def DescribeSubscriptionDetail(self, request):
        """查詢訂閱詳情

        :param request: Request instance for DescribeSubscriptionDetail.
        :type request: :class:`taifucloudcloud.cmq.v20190304.models.DescribeSubscriptionDetailRequest`
        :rtype: :class:`taifucloudcloud.cmq.v20190304.models.DescribeSubscriptionDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSubscriptionDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSubscriptionDetailResponse()
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


    def DescribeTopicDetail(self, request):
        """查詢主題詳情

        :param request: Request instance for DescribeTopicDetail.
        :type request: :class:`taifucloudcloud.cmq.v20190304.models.DescribeTopicDetailRequest`
        :rtype: :class:`taifucloudcloud.cmq.v20190304.models.DescribeTopicDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTopicDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTopicDetailResponse()
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


    def ModifyQueueAttribute(self, request):
        """修改隊列屬性

        :param request: Request instance for ModifyQueueAttribute.
        :type request: :class:`taifucloudcloud.cmq.v20190304.models.ModifyQueueAttributeRequest`
        :rtype: :class:`taifucloudcloud.cmq.v20190304.models.ModifyQueueAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyQueueAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyQueueAttributeResponse()
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


    def ModifySubscriptionAttribute(self, request):
        """修改訂閱屬性

        :param request: Request instance for ModifySubscriptionAttribute.
        :type request: :class:`taifucloudcloud.cmq.v20190304.models.ModifySubscriptionAttributeRequest`
        :rtype: :class:`taifucloudcloud.cmq.v20190304.models.ModifySubscriptionAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySubscriptionAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySubscriptionAttributeResponse()
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


    def ModifyTopicAttribute(self, request):
        """修改主題屬性

        :param request: Request instance for ModifyTopicAttribute.
        :type request: :class:`taifucloudcloud.cmq.v20190304.models.ModifyTopicAttributeRequest`
        :rtype: :class:`taifucloudcloud.cmq.v20190304.models.ModifyTopicAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTopicAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTopicAttributeResponse()
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


    def RewindQueue(self, request):
        """回溯隊列

        :param request: Request instance for RewindQueue.
        :type request: :class:`taifucloudcloud.cmq.v20190304.models.RewindQueueRequest`
        :rtype: :class:`taifucloudcloud.cmq.v20190304.models.RewindQueueResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RewindQueue", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RewindQueueResponse()
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


    def UnbindDeadLetter(self, request):
        """解綁死信隊列

        :param request: Request instance for UnbindDeadLetter.
        :type request: :class:`taifucloudcloud.cmq.v20190304.models.UnbindDeadLetterRequest`
        :rtype: :class:`taifucloudcloud.cmq.v20190304.models.UnbindDeadLetterResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnbindDeadLetter", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindDeadLetterResponse()
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