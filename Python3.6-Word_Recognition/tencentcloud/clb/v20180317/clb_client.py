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
from taifucloudcloud.clb.v20180317 import models


class ClbClient(AbstractClient):
    _apiVersion = '2018-03-17'
    _endpoint = 'clb.taifucloudcloudapi.com'


    def AutoRewrite(self, request):
        """系統自動爲已存在的HTTPS:443監聽器創建HTTP監聽器進行轉發，預設使用80端口。創建成功後可以通過HTTP:80網址自動跳轉爲HTTPS:443網址進行訪問。

        :param request: 調用AutoRewrite所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.AutoRewriteRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.AutoRewriteResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AutoRewrite", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AutoRewriteResponse()
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


    def BatchModifyTargetWeight(self, request):
        """BatchModifyTargetWeight介面用於批次修改監聽器綁定的後端機器的轉發權重，當前介面只支援應用型HTTP/HTTPS監聽器。
        本介面爲異步介面，本介面返回成功後需以返回的RequestID爲入參，調用DescribeTaskStatus介面查詢本次任務是否成功。

        :param request: 調用BatchModifyTargetWeight所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.BatchModifyTargetWeightRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.BatchModifyTargetWeightResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BatchModifyTargetWeight", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BatchModifyTargetWeightResponse()
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


    def CreateListener(self, request):
        """在一個負載均衡實例下創建監聽器。
        本介面爲異步介面，本介面返回成功後需以返回的RequestID爲入參，調用DescribeTaskStatus介面查詢本次任務是否成功。

        :param request: 調用CreateListener所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.CreateListenerRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.CreateListenerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateListener", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateListenerResponse()
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


    def CreateLoadBalancer(self, request):
        """CreateLoadBalancer 介面用來創建負載均衡實例。爲了使用負載均衡服務，您必須要購買一個或者多個負載均衡實例。通過成功調用該介面，會返回負載均衡實例的唯一 ID。用戶可以購買的負載均衡實例類型分爲：公網（應用型）、内網（應用型）。可以參考産品說明的産品類型。
        本介面成功返回後，可使用查詢負載均衡實例清單介面DescribeLoadBalancers查詢負載均衡實例的狀态，以确定是否創建成功。

        :param request: 調用CreateLoadBalancer所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.CreateLoadBalancerRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.CreateLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLoadBalancer", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLoadBalancerResponse()
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


    def CreateRule(self, request):
        """CreateRule 介面用於在一個已存在的應用型負載均衡七層監聽器下創建轉發規則，七層監聽器中，後端機器必須綁定到規則上而非監聽器上。
        本介面爲異步介面，本介面返回成功後需以返回的RequestID爲入參，調用DescribeTaskStatus介面查詢本次任務是否成功。

        :param request: 調用CreateRule所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.CreateRuleRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.CreateRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRuleResponse()
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


    def DeleteListener(self, request):
        """本介面用來删除應用型（四層和七層）負載均衡實例下的監聽器。
        本介面爲異步介面，本介面返回成功後需以返回的RequestID爲入參，調用DescribeTaskStatus介面查詢本次任務是否成功。

        :param request: 調用DeleteListener所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.DeleteListenerRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.DeleteListenerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteListener", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteListenerResponse()
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
        """DeleteLoadBalancer 介面用來删除用戶指定的一個負載均衡實例。
        本介面爲異步介面，本介面返回成功後需以返回的RequestID爲入參，調用DescribeTaskStatus介面查詢本次任務是否成功。

        :param request: 調用DeleteLoadBalancer所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.DeleteLoadBalancerRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.DeleteLoadBalancerResponse`

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


    def DeleteRewrite(self, request):
        """DeleteRewrite 介面支援删除指定轉發規則之間的重定向關系。

        :param request: 調用DeleteRewrite所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.DeleteRewriteRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.DeleteRewriteResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteRewrite", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRewriteResponse()
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


    def DeleteRule(self, request):
        """DeleteRule 介面用來删除應用型負載均衡實例七層監聽器下的轉發規則。
        本介面爲異步介面，本介面返回成功後需以返回的RequestID爲入參，調用DescribeTaskStatus介面查詢本次任務是否成功。

        :param request: 調用DeleteRule所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.DeleteRuleRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.DeleteRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRuleResponse()
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


    def DeregisterTargets(self, request):
        """DeregisterTargets 介面用來将一台或多台後端機器從應用型負載均衡的監聽器上解綁，對於四層監聽器（TCP、UDP），只需指定監聽器ID即可，對於七層監聽器（HTTP、HTTPS），還需通過LocationId或者Domain+Url指定轉發規則。
        本介面爲異步介面，本介面返回成功後需以返回的RequestID爲入參，調用DescribeTaskStatus介面查詢本次任務是否成功。

        :param request: 調用DeregisterTargets所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.DeregisterTargetsRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.DeregisterTargetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeregisterTargets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeregisterTargetsResponse()
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


    def DeregisterTargetsFromClassicalLB(self, request):
        """DeregisterTargetsFromClassicalLB用於解綁後端服務器

        :param request: 調用DeregisterTargetsFromClassicalLB所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.DeregisterTargetsFromClassicalLBRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.DeregisterTargetsFromClassicalLBResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeregisterTargetsFromClassicalLB", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeregisterTargetsFromClassicalLBResponse()
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


    def DescribeClassicalLBByInstanceId(self, request):
        """DescribeClassicalLBByInstanceId用於通過後端實例ID獲取傳統型負載均衡ID清單

        :param request: 調用DescribeClassicalLBByInstanceId所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.DescribeClassicalLBByInstanceIdRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.DescribeClassicalLBByInstanceIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClassicalLBByInstanceId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClassicalLBByInstanceIdResponse()
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


    def DescribeClassicalLBHealthStatus(self, request):
        """DescribeClassicalLBHealthStatus用於獲取傳統型負載均衡後端的健康狀态

        :param request: 調用DescribeClassicalLBHealthStatus所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.DescribeClassicalLBHealthStatusRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.DescribeClassicalLBHealthStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClassicalLBHealthStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClassicalLBHealthStatusResponse()
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


    def DescribeClassicalLBListeners(self, request):
        """DescribeClassicalLBListeners用於獲取傳統型負載均衡訊息

        :param request: 調用DescribeClassicalLBListeners所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.DescribeClassicalLBListenersRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.DescribeClassicalLBListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClassicalLBListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClassicalLBListenersResponse()
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


    def DescribeClassicalLBTargets(self, request):
        """DescribeClassicalLBTargets用於獲取傳統型負載均衡綁定的後端服務

        :param request: 調用DescribeClassicalLBTargets所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.DescribeClassicalLBTargetsRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.DescribeClassicalLBTargetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClassicalLBTargets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClassicalLBTargetsResponse()
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


    def DescribeListeners(self, request):
        """DescribeListeners 介面可根據負載均衡器 ID，監聽器的協議或者端口作爲過濾條件獲取監聽器清單。如果不指定任何過濾條件，預設返該負載均衡器下的預設數據長度（20 個）的監聽器。

        :param request: 調用DescribeListeners所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.DescribeListenersRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.DescribeListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListenersResponse()
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
        """查詢負載均衡實例清單

        :param request: 調用DescribeLoadBalancers所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.DescribeLoadBalancersRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.DescribeLoadBalancersResponse`

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


    def DescribeRewrite(self, request):
        """DescribeRewrite 介面可根據負載均衡實例ID，查詢一個負載均衡實例下轉發規則的重定向關系。如果不指定監聽器ID或轉發規則ID，則返回該負載均衡實例下的所有重定向關系。

        :param request: 調用DescribeRewrite所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.DescribeRewriteRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.DescribeRewriteResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRewrite", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRewriteResponse()
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


    def DescribeTargetHealth(self, request):
        """DescribeTargetHealth 介面用來獲取應用型負載均衡後端的健康檢查結果。

        :param request: 調用DescribeTargetHealth所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.DescribeTargetHealthRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.DescribeTargetHealthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTargetHealth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTargetHealthResponse()
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


    def DescribeTargets(self, request):
        """DescribeTargets 介面用來查詢應用型負載均衡實例的某些監聽器後端綁定的機器清單。

        :param request: 調用DescribeTargets所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.DescribeTargetsRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.DescribeTargetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTargets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTargetsResponse()
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


    def DescribeTaskStatus(self, request):
        """本介面用於查詢異步執行任務的狀态，對於非查詢類的介面（創建/删除負載均衡實例、監聽器、規則以及綁定或解綁後端機器等），在調用成功後都需要使用本介面查詢任務是否最終執行成功。

        :param request: 調用DescribeTaskStatus所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.DescribeTaskStatusRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.DescribeTaskStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskStatusResponse()
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


    def ManualRewrite(self, request):
        """用戶手動配置原訪問網址和重定向網址，系統自動将原訪問網址的請求重定向至對應路徑的目的網址。同一域名下可以配置多條路徑作爲重定向策略，實現http/https之間請求的自動跳轉。

        :param request: 調用ManualRewrite所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.ManualRewriteRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.ManualRewriteResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ManualRewrite", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ManualRewriteResponse()
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


    def ModifyDomain(self, request):
        """ModifyDomain介面用來修改應用型負載均衡七層監聽器下的域名。
        本介面爲異步介面，本介面返回成功後需以返回的RequestID爲入參，調用DescribeTaskStatus介面查詢本次任務是否成功。

        :param request: 調用ModifyDomain所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.ModifyDomainRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.ModifyDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDomainResponse()
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


    def ModifyListener(self, request):
        """ModifyListener介面用來修改應用型負載均衡監聽器的屬性，包括監聽器名稱、健康檢查參數、證書訊息、轉發策略等。
        本介面爲異步介面，本介面返回成功後需以返回的RequestID爲入參，調用DescribeTaskStatus介面查詢本次任務是否成功。

        :param request: 調用ModifyListener所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.ModifyListenerRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.ModifyListenerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyListener", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyListenerResponse()
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


    def ModifyLoadBalancerAttributes(self, request):
        """修改負載均衡實例的屬性，支援修改負載均衡實例的名稱、設置負載均衡的跨域屬性。
        本介面爲異步介面，本介面返回成功後需以返回的RequestID爲入參，調用DescribeTaskStatus介面查詢本次任務是否成功。

        :param request: 調用ModifyLoadBalancerAttributes所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.ModifyLoadBalancerAttributesRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.ModifyLoadBalancerAttributesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLoadBalancerAttributes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLoadBalancerAttributesResponse()
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


    def ModifyRule(self, request):
        """ModifyRule 介面用來修改應用型負載均衡七層監聽器下的轉發規則的各項屬性，包括轉發路徑、健康檢查屬性、轉發策略等。
        本介面爲異步介面，本介面返回成功後需以返回的RequestID爲入參，調用DescribeTaskStatus介面查詢本次任務是否成功。

        :param request: 調用ModifyRule所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.ModifyRuleRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.ModifyRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRuleResponse()
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


    def ModifyTargetPort(self, request):
        """ModifyTargetPort介面用於修改監聽器綁定的後端雲伺服器的端口。
        本介面爲異步介面，本介面返回成功後需以返回的RequestID爲入參，調用DescribeTaskStatus介面查詢本次任務是否成功。

        :param request: 調用ModifyTargetPort所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.ModifyTargetPortRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.ModifyTargetPortResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTargetPort", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTargetPortResponse()
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


    def ModifyTargetWeight(self, request):
        """ModifyTargetWeight 介面用於修改監聽器綁定的後端機器的轉發權重。
        本介面爲異步介面，本介面返回成功後需以返回的RequestID爲入參，調用DescribeTaskStatus介面查詢本次任務是否成功。

        :param request: 調用ModifyTargetWeight所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.ModifyTargetWeightRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.ModifyTargetWeightResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTargetWeight", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTargetWeightResponse()
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


    def RegisterTargets(self, request):
        """RegisterTargets 介面用來将一台或多台後端機器注冊到應用型負載均衡的監聽器，對於四層監聽器（TCP、UDP），只需指定監聽器ID即可，對於七層監聽器（HTTP、HTTPS），還需通過LocationId或者Domain+Url指定轉發規則。
        本介面爲異步介面，本介面返回成功後需以返回的RequestID爲入參，調用DescribeTaskStatus介面查詢本次任務是否成功。

        :param request: 調用RegisterTargets所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.RegisterTargetsRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.RegisterTargetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RegisterTargets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RegisterTargetsResponse()
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


    def RegisterTargetsWithClassicalLB(self, request):
        """RegisterTargetsWithClassicalLB用於綁定後端服務到傳統型負載均衡

        :param request: 調用RegisterTargetsWithClassicalLB所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.RegisterTargetsWithClassicalLBRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.RegisterTargetsWithClassicalLBResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RegisterTargetsWithClassicalLB", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RegisterTargetsWithClassicalLBResponse()
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


    def SetLoadBalancerSecurityGroups(self, request):
        """SetLoadBalancerSecurityGroups 介面支援對一個負載均衡實例執行設置（綁定、解綁）安全組操作，查詢一個負載均衡實例目前已綁定的安全組，可使用 DescribeLoadBalancers 介面。
        綁定操作時，入參需要傳入負載均衡實例要綁定的所有安全組（已綁定的+新增綁定的）。
        解綁操作時，入參需要傳入負載均衡實例執行解綁後所綁定的所有安全組；如果要解綁所有安全組，可傳入空數組。

        :param request: 調用SetLoadBalancerSecurityGroups所需參數的結構體。
        :type request: :class:`taifucloudcloud.clb.v20180317.models.SetLoadBalancerSecurityGroupsRequest`
        :rtype: :class:`taifucloudcloud.clb.v20180317.models.SetLoadBalancerSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetLoadBalancerSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetLoadBalancerSecurityGroupsResponse()
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