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
from taifucloudcloud.ie.v20200304 import models


class IeClient(AbstractClient):
    _apiVersion = '2020-03-04'
    _endpoint = 'ie.taifucloudcloudapi.com'


    def CreateEditingTask(self, request):
        """創建智慧編輯任務，可以同時選擇視訊标簽識别、分類識别、智慧拆條、智慧集錦、智慧封面和片頭片尾識别中的一項或者多項能力。

        :param request: Request instance for CreateEditingTask.
        :type request: :class:`taifucloudcloud.ie.v20200304.models.CreateEditingTaskRequest`
        :rtype: :class:`taifucloudcloud.ie.v20200304.models.CreateEditingTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateEditingTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEditingTaskResponse()
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


    def DescribeEditingTaskResult(self, request):
        """獲取智慧編輯任務結果。

        :param request: Request instance for DescribeEditingTaskResult.
        :type request: :class:`taifucloudcloud.ie.v20200304.models.DescribeEditingTaskResultRequest`
        :rtype: :class:`taifucloudcloud.ie.v20200304.models.DescribeEditingTaskResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEditingTaskResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEditingTaskResultResponse()
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