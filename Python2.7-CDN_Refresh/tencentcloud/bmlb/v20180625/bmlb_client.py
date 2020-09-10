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
from tencentcloud.bmlb.v20180625 import models


class BmlbClient(AbstractClient):
    _apiVersion = '2018-06-25'
    _endpoint = 'bmlb.tencentcloudapi.com'


    def BindL4Backends(self, request):
        """綁定黑石服務器到四層監聽器。服務器包括物理服務器、虛拟機以及半托管機器。

        :param request: Request instance for BindL4Backends.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.BindL4BackendsRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.BindL4BackendsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindL4Backends", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindL4BackendsResponse()
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


    def BindL7Backends(self, request):
        """綁定黑石物理服務器或半托管服務器到七層轉發路徑。

        :param request: Request instance for BindL7Backends.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.BindL7BackendsRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.BindL7BackendsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindL7Backends", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindL7BackendsResponse()
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


    def BindTrafficMirrorListeners(self, request):
        """綁定黑石服務器七層監聽器到流量映像實例。

        :param request: Request instance for BindTrafficMirrorListeners.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.BindTrafficMirrorListenersRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.BindTrafficMirrorListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindTrafficMirrorListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindTrafficMirrorListenersResponse()
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


    def BindTrafficMirrorReceivers(self, request):
        """綁定黑石物理服務器成爲流量映像接收機。

        :param request: Request instance for BindTrafficMirrorReceivers.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.BindTrafficMirrorReceiversRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.BindTrafficMirrorReceiversResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindTrafficMirrorReceivers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindTrafficMirrorReceiversResponse()
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


    def CreateL4Listeners(self, request):
        """創建黑石四層負載均衡監聽器功能。黑石負載均衡四層監聽器提供了轉發用戶請求的具體規則，包括端口、協議、會話保持、健康檢查等參數。

        :param request: Request instance for CreateL4Listeners.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.CreateL4ListenersRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.CreateL4ListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateL4Listeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateL4ListenersResponse()
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


    def CreateL7Listeners(self, request):
        """創建黑石負載均衡七層監聽器功能。負載均衡七層監聽器提供了轉發用戶請求的具體規則，包括端口、協議等參數。

        :param request: Request instance for CreateL7Listeners.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.CreateL7ListenersRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.CreateL7ListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateL7Listeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateL7ListenersResponse()
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


    def CreateL7Rules(self, request):
        """創建黑石負載均衡七層轉發規則。

        :param request: Request instance for CreateL7Rules.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.CreateL7RulesRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.CreateL7RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateL7Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateL7RulesResponse()
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


    def CreateLoadBalancers(self, request):
        """用來創建黑石負載均衡。爲了使用黑石負載均衡服務，您必須要創建一個或者多個負載均衡實例。通過成功調用該介面，會返回負載均衡實例的唯一ID。用戶可以購買的黑石負載均衡實例類型分爲：公網類型、内網類型。公網類型負載均衡對應一個BGP VIP，可用于快速訪問公網負載均衡綁定的物理服務器；内網類型負載均衡對應一個Top Cloud 内部的VIP，不能通過Internet訪問，可快速訪問内網負載均衡綁定的物理服務器。

        :param request: Request instance for CreateLoadBalancers.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.CreateLoadBalancersRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.CreateLoadBalancersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLoadBalancers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLoadBalancersResponse()
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


    def CreateTrafficMirror(self, request):
        """創建流量映像實例。

        :param request: Request instance for CreateTrafficMirror.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.CreateTrafficMirrorRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.CreateTrafficMirrorResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTrafficMirror", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTrafficMirrorResponse()
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


    def DeleteL7Domains(self, request):
        """删除黑石負載均衡七層轉發域名。

        :param request: Request instance for DeleteL7Domains.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DeleteL7DomainsRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DeleteL7DomainsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteL7Domains", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteL7DomainsResponse()
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


    def DeleteL7Rules(self, request):
        """删除黑石負載均衡七層轉發規則。

        :param request: Request instance for DeleteL7Rules.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DeleteL7RulesRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DeleteL7RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteL7Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteL7RulesResponse()
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


    def DeleteListeners(self, request):
        """删除黑石負載均衡監聽器。

        :param request: Request instance for DeleteListeners.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DeleteListenersRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DeleteListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteListenersResponse()
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


    def DeleteLoadBalancer(self, request):
        """删除用戶指定的黑石負載均衡實例。

        :param request: Request instance for DeleteLoadBalancer.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DeleteLoadBalancerRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DeleteLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLoadBalancer", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLoadBalancerResponse()
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


    def DeleteTrafficMirror(self, request):
        """删除已創建的黑石流量映像實例，删除過程是異步執行的，因此需要使用查詢任務介面獲取删除的結果。

        :param request: Request instance for DeleteTrafficMirror.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DeleteTrafficMirrorRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DeleteTrafficMirrorResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTrafficMirror", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTrafficMirrorResponse()
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


    def DescribeCertDetail(self, request):
        """獲取黑石負載均衡證書詳情。

        :param request: Request instance for DescribeCertDetail.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeCertDetailRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeCertDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCertDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCertDetailResponse()
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


    def DescribeDevicesBindInfo(self, request):
        """查詢黑石物理機和虛機以及托管服務器綁定的黑石負載均衡詳情。

        :param request: Request instance for DescribeDevicesBindInfo.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeDevicesBindInfoRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeDevicesBindInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDevicesBindInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDevicesBindInfoResponse()
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


    def DescribeL4Backends(self, request):
        """獲取黑石負載均衡四層監聽器綁定的主機清單。

        :param request: Request instance for DescribeL4Backends.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeL4BackendsRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeL4BackendsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeL4Backends", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeL4BackendsResponse()
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


    def DescribeL4ListenerInfo(self, request):
        """查找綁定了某主機或者指定監聽器名稱的黑石負載均衡四層監聽器。

        :param request: Request instance for DescribeL4ListenerInfo.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeL4ListenerInfoRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeL4ListenerInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeL4ListenerInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeL4ListenerInfoResponse()
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


    def DescribeL4Listeners(self, request):
        """獲取黑石負載均衡四層監聽器。

        :param request: Request instance for DescribeL4Listeners.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeL4ListenersRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeL4ListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeL4Listeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeL4ListenersResponse()
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


    def DescribeL7Backends(self, request):
        """獲取黑石負載均衡七層監聽器綁定的主機清單

        :param request: Request instance for DescribeL7Backends.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeL7BackendsRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeL7BackendsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeL7Backends", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeL7BackendsResponse()
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


    def DescribeL7ListenerInfo(self, request):
        """查找綁定了某主機或者有某轉發域名黑石負載均衡七層監聽器。

        :param request: Request instance for DescribeL7ListenerInfo.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeL7ListenerInfoRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeL7ListenerInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeL7ListenerInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeL7ListenerInfoResponse()
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


    def DescribeL7Listeners(self, request):
        """獲取黑石負載均衡七層監聽器清單訊息。

        :param request: Request instance for DescribeL7Listeners.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeL7ListenersRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeL7ListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeL7Listeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeL7ListenersResponse()
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


    def DescribeL7ListenersEx(self, request):
        """獲取指定VPC下的7層監聽器(支援模糊比對)。

        :param request: Request instance for DescribeL7ListenersEx.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeL7ListenersExRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeL7ListenersExResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeL7ListenersEx", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeL7ListenersExResponse()
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


    def DescribeL7Rules(self, request):
        """獲取黑石負載均衡七層轉發規則。

        :param request: Request instance for DescribeL7Rules.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeL7RulesRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeL7RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeL7Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeL7RulesResponse()
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


    def DescribeLoadBalancerPortInfo(self, request):
        """獲取黑石負載均衡端口相關訊息。

        :param request: Request instance for DescribeLoadBalancerPortInfo.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeLoadBalancerPortInfoRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeLoadBalancerPortInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLoadBalancerPortInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLoadBalancerPortInfoResponse()
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


    def DescribeLoadBalancerTaskResult(self, request):
        """查詢負載均衡實例異步任務的執行情況。

        :param request: Request instance for DescribeLoadBalancerTaskResult.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeLoadBalancerTaskResultRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeLoadBalancerTaskResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLoadBalancerTaskResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLoadBalancerTaskResultResponse()
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


    def DescribeLoadBalancers(self, request):
        """獲取黑石負載均衡實例清單

        :param request: Request instance for DescribeLoadBalancers.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeLoadBalancersRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeLoadBalancersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLoadBalancers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLoadBalancersResponse()
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


    def DescribeTrafficMirrorListeners(self, request):
        """獲取流量映像的監聽器清單訊息。

        :param request: Request instance for DescribeTrafficMirrorListeners.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeTrafficMirrorListenersRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeTrafficMirrorListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTrafficMirrorListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTrafficMirrorListenersResponse()
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


    def DescribeTrafficMirrorReceiverHealthStatus(self, request):
        """獲取流量映像接收機健康狀态。

        :param request: Request instance for DescribeTrafficMirrorReceiverHealthStatus.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeTrafficMirrorReceiverHealthStatusRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeTrafficMirrorReceiverHealthStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTrafficMirrorReceiverHealthStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTrafficMirrorReceiverHealthStatusResponse()
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


    def DescribeTrafficMirrorReceivers(self, request):
        """獲取指定流量映像實例的接收機訊息。

        :param request: Request instance for DescribeTrafficMirrorReceivers.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeTrafficMirrorReceiversRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeTrafficMirrorReceiversResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTrafficMirrorReceivers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTrafficMirrorReceiversResponse()
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


    def DescribeTrafficMirrors(self, request):
        """獲取流量映像實例的清單訊息。

        :param request: Request instance for DescribeTrafficMirrors.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeTrafficMirrorsRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeTrafficMirrorsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTrafficMirrors", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTrafficMirrorsResponse()
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


    def ModifyL4BackendPort(self, request):
        """修改黑石負載均衡四層監聽器後端實例端口。

        :param request: Request instance for ModifyL4BackendPort.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.ModifyL4BackendPortRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.ModifyL4BackendPortResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyL4BackendPort", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyL4BackendPortResponse()
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


    def ModifyL4BackendProbePort(self, request):
        """修改黑石負載均衡四層監聽器後端探測端口。

        :param request: Request instance for ModifyL4BackendProbePort.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.ModifyL4BackendProbePortRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.ModifyL4BackendProbePortResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyL4BackendProbePort", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyL4BackendProbePortResponse()
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


    def ModifyL4BackendWeight(self, request):
        """修改黑石負載均衡四層監聽器後端實例權重功能。

        :param request: Request instance for ModifyL4BackendWeight.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.ModifyL4BackendWeightRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.ModifyL4BackendWeightResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyL4BackendWeight", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyL4BackendWeightResponse()
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


    def ModifyL4Listener(self, request):
        """修改黑石負載均衡四層監聽器。

        :param request: Request instance for ModifyL4Listener.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.ModifyL4ListenerRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.ModifyL4ListenerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyL4Listener", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyL4ListenerResponse()
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


    def ModifyL7BackendPort(self, request):
        """修改黑石負載均衡七層轉發路徑後端實例端口。

        :param request: Request instance for ModifyL7BackendPort.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.ModifyL7BackendPortRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.ModifyL7BackendPortResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyL7BackendPort", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyL7BackendPortResponse()
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


    def ModifyL7BackendWeight(self, request):
        """修改黑石負載均衡七層轉發路徑後端實例權重。

        :param request: Request instance for ModifyL7BackendWeight.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.ModifyL7BackendWeightRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.ModifyL7BackendWeightResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyL7BackendWeight", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyL7BackendWeightResponse()
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


    def ModifyL7Listener(self, request):
        """修改黑石負載均衡七層監聽器。

        :param request: Request instance for ModifyL7Listener.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.ModifyL7ListenerRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.ModifyL7ListenerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyL7Listener", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyL7ListenerResponse()
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


    def ModifyL7Locations(self, request):
        """修改黑石負載均衡七層轉發路徑。

        :param request: Request instance for ModifyL7Locations.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.ModifyL7LocationsRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.ModifyL7LocationsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyL7Locations", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyL7LocationsResponse()
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


    def ModifyLoadBalancer(self, request):
        """根據輸入參數來修改黑石負載均衡實例的基本配置訊息。可能的訊息包括負載均衡實例的名稱，域名前綴。

        :param request: Request instance for ModifyLoadBalancer.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.ModifyLoadBalancerRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.ModifyLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLoadBalancer", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLoadBalancerResponse()
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


    def ModifyLoadBalancerChargeMode(self, request):
        """更改黑石負載均衡的計費方式

        :param request: Request instance for ModifyLoadBalancerChargeMode.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.ModifyLoadBalancerChargeModeRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.ModifyLoadBalancerChargeModeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLoadBalancerChargeMode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLoadBalancerChargeModeResponse()
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


    def ReplaceCert(self, request):
        """更新黑石負載均衡證書。

        :param request: Request instance for ReplaceCert.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.ReplaceCertRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.ReplaceCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReplaceCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReplaceCertResponse()
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


    def SetTrafficMirrorAlias(self, request):
        """設置流量映像的别名。

        :param request: Request instance for SetTrafficMirrorAlias.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.SetTrafficMirrorAliasRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.SetTrafficMirrorAliasResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetTrafficMirrorAlias", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetTrafficMirrorAliasResponse()
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


    def SetTrafficMirrorHealthSwitch(self, request):
        """設置流量映像的健康檢查參數。

        :param request: Request instance for SetTrafficMirrorHealthSwitch.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.SetTrafficMirrorHealthSwitchRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.SetTrafficMirrorHealthSwitchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetTrafficMirrorHealthSwitch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetTrafficMirrorHealthSwitchResponse()
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


    def UnbindL4Backends(self, request):
        """解綁黑石負載均衡四層監聽器物理服務器。

        :param request: Request instance for UnbindL4Backends.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.UnbindL4BackendsRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.UnbindL4BackendsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnbindL4Backends", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindL4BackendsResponse()
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


    def UnbindL7Backends(self, request):
        """解綁黑石物理服務器或者托管服務器到七層轉發路徑功能。

        :param request: Request instance for UnbindL7Backends.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.UnbindL7BackendsRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.UnbindL7BackendsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnbindL7Backends", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindL7BackendsResponse()
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


    def UnbindTrafficMirrorListeners(self, request):
        """解綁流量映像監聽器。

        :param request: Request instance for UnbindTrafficMirrorListeners.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.UnbindTrafficMirrorListenersRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.UnbindTrafficMirrorListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnbindTrafficMirrorListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindTrafficMirrorListenersResponse()
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


    def UnbindTrafficMirrorReceivers(self, request):
        """從流量映像實例上解綁流量映像接收機。

        :param request: Request instance for UnbindTrafficMirrorReceivers.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.UnbindTrafficMirrorReceiversRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.UnbindTrafficMirrorReceiversResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnbindTrafficMirrorReceivers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindTrafficMirrorReceiversResponse()
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


    def UploadCert(self, request):
        """創建黑石負載均衡證書。

        :param request: Request instance for UploadCert.
        :type request: :class:`tencentcloud.bmlb.v20180625.models.UploadCertRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.UploadCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UploadCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UploadCertResponse()
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