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
from taifucloudcloud.cis.v20180408 import models


class CisClient(AbstractClient):
    _apiVersion = '2018-04-08'
    _endpoint = 'cis.taifucloudcloudapi.com'


    def CreateContainerInstance(self, request):
        """此介面（CreateContainerInstance）用於創建容器實例

        :param request: 調用CreateContainerInstance所需參數的結構體。
        :type request: :class:`taifucloudcloud.cis.v20180408.models.CreateContainerInstanceRequest`
        :rtype: :class:`taifucloudcloud.cis.v20180408.models.CreateContainerInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateContainerInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateContainerInstanceResponse()
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


    def DeleteContainerInstance(self, request):
        """此介面（DeleteContainerInstance）用於删除容器實例

        :param request: 調用DeleteContainerInstance所需參數的結構體。
        :type request: :class:`taifucloudcloud.cis.v20180408.models.DeleteContainerInstanceRequest`
        :rtype: :class:`taifucloudcloud.cis.v20180408.models.DeleteContainerInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteContainerInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteContainerInstanceResponse()
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


    def DescribeContainerInstance(self, request):
        """此介面（DescribeContainerInstance）用於獲取容器實例詳情

        :param request: 調用DescribeContainerInstance所需參數的結構體。
        :type request: :class:`taifucloudcloud.cis.v20180408.models.DescribeContainerInstanceRequest`
        :rtype: :class:`taifucloudcloud.cis.v20180408.models.DescribeContainerInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeContainerInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeContainerInstanceResponse()
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


    def DescribeContainerInstanceEvents(self, request):
        """此介面（DescribeContainerInstanceEvents）用於查詢容器實例事件清單

        :param request: 調用DescribeContainerInstanceEvents所需參數的結構體。
        :type request: :class:`taifucloudcloud.cis.v20180408.models.DescribeContainerInstanceEventsRequest`
        :rtype: :class:`taifucloudcloud.cis.v20180408.models.DescribeContainerInstanceEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeContainerInstanceEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeContainerInstanceEventsResponse()
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


    def DescribeContainerInstances(self, request):
        """此介面（DescribeContainerInstances）查詢容器實例清單

        :param request: 調用DescribeContainerInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.cis.v20180408.models.DescribeContainerInstancesRequest`
        :rtype: :class:`taifucloudcloud.cis.v20180408.models.DescribeContainerInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeContainerInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeContainerInstancesResponse()
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


    def DescribeContainerLog(self, request):
        """此介面（DescribeContainerLog）用於獲取容器日志訊息

        :param request: 調用DescribeContainerLog所需參數的結構體。
        :type request: :class:`taifucloudcloud.cis.v20180408.models.DescribeContainerLogRequest`
        :rtype: :class:`taifucloudcloud.cis.v20180408.models.DescribeContainerLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeContainerLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeContainerLogResponse()
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


    def InquiryPriceCreateCis(self, request):
        """此介面（InquiryPriceCreateCis）用於查詢容器實例價格

        :param request: 調用InquiryPriceCreateCis所需參數的結構體。
        :type request: :class:`taifucloudcloud.cis.v20180408.models.InquiryPriceCreateCisRequest`
        :rtype: :class:`taifucloudcloud.cis.v20180408.models.InquiryPriceCreateCisResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceCreateCis", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceCreateCisResponse()
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