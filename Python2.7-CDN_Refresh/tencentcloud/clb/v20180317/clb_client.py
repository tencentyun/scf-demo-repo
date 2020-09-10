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
from tencentcloud.clb.v20180317 import models


class ClbClient(AbstractClient):
    _apiVersion = '2018-03-17'
    _endpoint = 'clb.tencentcloudapi.com'


    def AssociateTargetGroups(self, request):
        """本介面(AssociateTargetGroups)用來将目标組綁定到負載均衡的監聽器（四層協議）或轉發規則（七層協議）上。
        本介面爲異步介面，本介面返回成功後需以返回的 RequestID 爲入參，調用 DescribeTaskStatus 介面查詢本次任務是否成功。

        :param request: Request instance for AssociateTargetGroups.
        :type request: :class:`tencentcloud.clb.v20180317.models.AssociateTargetGroupsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.AssociateTargetGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssociateTargetGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateTargetGroupsResponse()
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


    def AutoRewrite(self, request):
        """用戶需要先創建出一個HTTPS:443監聽器，并在其下創建轉發規則。通過調用本介面，系統會自動創建出一個HTTP:80監聽器（如果之前不存在），并在其下創建轉發規則，與HTTPS:443監聽器下的Domains（在入參中指定）對應。創建成功後可以通過HTTP:80網址自動跳轉爲HTTPS:443網址進行訪問。
        本介面爲異步介面，本介面返回成功後需以返回的RequestID爲入參，調用DescribeTaskStatus介面查詢本次任務是否成功。

        :param request: Request instance for AutoRewrite.
        :type request: :class:`tencentcloud.clb.v20180317.models.AutoRewriteRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.AutoRewriteResponse`

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


    def BatchDeregisterTargets(self, request):
        """批次解綁四七層後端服務。

        :param request: Request instance for BatchDeregisterTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.BatchDeregisterTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.BatchDeregisterTargetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BatchDeregisterTargets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BatchDeregisterTargetsResponse()
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
        """本介面(BatchModifyTargetWeight)用于批次修改負載均衡監聽器綁定的後端機器的轉發權重，支援負載均衡的4層和7層監聽器；不支援傳統型負載均衡。
        本介面爲異步介面，本介面返回成功後需以返回的 RequestID 爲入參，調用 DescribeTaskStatus 介面查詢本次任務是否成功。

        :param request: Request instance for BatchModifyTargetWeight.
        :type request: :class:`tencentcloud.clb.v20180317.models.BatchModifyTargetWeightRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.BatchModifyTargetWeightResponse`

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


    def BatchRegisterTargets(self, request):
        """批次綁定虛拟主機或彈性網卡，支援跨域綁定，支援四層、七層（TCP、UDP、HTTP、HTTPS）協議綁定。

        :param request: Request instance for BatchRegisterTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.BatchRegisterTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.BatchRegisterTargetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BatchRegisterTargets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BatchRegisterTargetsResponse()
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
        本介面爲異步介面，介面返回成功後，需以返回的 RequestId 爲入參，調用 DescribeTaskStatus 介面查詢本次任務是否成功。

        :param request: Request instance for CreateListener.
        :type request: :class:`tencentcloud.clb.v20180317.models.CreateListenerRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.CreateListenerResponse`

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
        """本介面(CreateLoadBalancer)用來創建負載均衡實例（本介面只支援購買按量計費的負載均衡，包年包月的負載均衡請通過控制台購買）。爲了使用負載均衡服務，您必須購買一個或多個負載均衡實例。成功調用該介面後，會返回負載均衡實例的唯一 ID。負載均衡實例的類型分爲：公網、内網。詳情可參考産品說明中的産品類型。
        注意：(1)指定可用區申請負載均衡、跨zone容災(僅香港支援)【如果您需要體驗該功能，請通過 [工單申請](https://console.cloud.tencent.com/workorder/category)】；(2)目前只有北京、上海、廣州支援IPv6；(3)一個賬号在每個地域的預設購買配額爲：公網100個，内網100個。
        本介面爲異步介面，介面成功返回後，可使用 DescribeLoadBalancers 介面查詢負載均衡實例的狀态（如創建中、正常），以确定是否創建成功。

        :param request: Request instance for CreateLoadBalancer.
        :type request: :class:`tencentcloud.clb.v20180317.models.CreateLoadBalancerRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.CreateLoadBalancerResponse`

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


    def CreateLoadBalancerSnatIps(self, request):
        """針對SnatPro負載均衡，這個介面用于添加SnatIp，如果負載均衡沒有開啓SnatPro，添加SnatIp後會自動開啓

        :param request: Request instance for CreateLoadBalancerSnatIps.
        :type request: :class:`tencentcloud.clb.v20180317.models.CreateLoadBalancerSnatIpsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.CreateLoadBalancerSnatIpsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLoadBalancerSnatIps", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLoadBalancerSnatIpsResponse()
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
        """CreateRule 介面用于在一個已存在的負載均衡七層監聽器下創建轉發規則，七層監聽器中，後端服務必須綁定到規則上而非監聽器上。
        本介面爲異步介面，本介面返回成功後需以返回的RequestID爲入參，調用DescribeTaskStatus介面查詢本次任務是否成功。

        :param request: Request instance for CreateRule.
        :type request: :class:`tencentcloud.clb.v20180317.models.CreateRuleRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.CreateRuleResponse`

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


    def CreateTargetGroup(self, request):
        """創建目标組。（目标組功能正在灰度中，需要開通白名單支援）

        :param request: Request instance for CreateTargetGroup.
        :type request: :class:`tencentcloud.clb.v20180317.models.CreateTargetGroupRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.CreateTargetGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTargetGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTargetGroupResponse()
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
        """本介面用來删除負載均衡實例下的監聽器（四層和七層）。
        本介面爲異步介面，介面返回成功後，需以得到的 RequestID 爲入參，調用 DescribeTaskStatus 介面查詢本次任務是否成功。

        :param request: Request instance for DeleteListener.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeleteListenerRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeleteListenerResponse`

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
        """DeleteLoadBalancer 介面用以删除指定的一個或多個負載均衡實例。
        本介面爲異步介面，介面返回成功後，需以返回的 RequestId 爲入參，調用 DescribeTaskStatus 介面查詢本次任務是否成功。

        :param request: Request instance for DeleteLoadBalancer.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeleteLoadBalancerRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeleteLoadBalancerResponse`

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


    def DeleteLoadBalancerListeners(self, request):
        """該介面支援删除負載均衡的多個監聽器。
        本介面爲異步介面，本介面返回成功後需以返回的 RequestID 爲入參，調用 DescribeTaskStatus 介面查詢本次任務是否成功。

        :param request: Request instance for DeleteLoadBalancerListeners.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeleteLoadBalancerListenersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeleteLoadBalancerListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLoadBalancerListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLoadBalancerListenersResponse()
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


    def DeleteLoadBalancerSnatIps(self, request):
        """對于SnatPro的負載均衡，這個介面用于删除SnatIp

        :param request: Request instance for DeleteLoadBalancerSnatIps.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeleteLoadBalancerSnatIpsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeleteLoadBalancerSnatIpsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLoadBalancerSnatIps", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLoadBalancerSnatIpsResponse()
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
        本介面爲異步介面，本介面返回成功後需以返回的RequestID爲入參，調用DescribeTaskStatus介面查詢本次任務是否成功。

        :param request: Request instance for DeleteRewrite.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeleteRewriteRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeleteRewriteResponse`

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
        """DeleteRule 介面用來删除負載均衡實例七層監聽器下的轉發規則。
        本介面爲異步介面，本介面返回成功後需以返回的RequestID爲入參，調用DescribeTaskStatus介面查詢本次任務是否成功。

        :param request: Request instance for DeleteRule.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeleteRuleRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeleteRuleResponse`

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


    def DeleteTargetGroups(self, request):
        """删除目标組

        :param request: Request instance for DeleteTargetGroups.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeleteTargetGroupsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeleteTargetGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTargetGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTargetGroupsResponse()
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


    def DeregisterTargetGroupInstances(self, request):
        """将服務器從目标組中解綁。
        本介面爲異步介面，本介面返回成功後需以返回的 RequestID 爲入參，調用 DescribeTaskStatus 介面查詢本次任務是否成功。

        :param request: Request instance for DeregisterTargetGroupInstances.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeregisterTargetGroupInstancesRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeregisterTargetGroupInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeregisterTargetGroupInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeregisterTargetGroupInstancesResponse()
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
        """DeregisterTargets 介面用來将一台或多台後端服務從負載均衡的監聽器或轉發規則上解綁，對于四層監聽器，只需指定監聽器ID即可，對于七層監聽器，還需通過LocationId或Domain+Url指定轉發規則。
        本介面爲異步介面，本介面返回成功後需以返回的RequestID爲入參，調用DescribeTaskStatus介面查詢本次任務是否成功。

        :param request: Request instance for DeregisterTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeregisterTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeregisterTargetsResponse`

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
        """DeregisterTargetsFromClassicalLB 介面用于解綁負載均衡後端服務。
        本介面爲異步介面，介面返回成功後，需以返回的 RequestId 爲入參，調用 DescribeTaskStatus 介面查詢本次任務是否成功。

        :param request: Request instance for DeregisterTargetsFromClassicalLB.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeregisterTargetsFromClassicalLBRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeregisterTargetsFromClassicalLBResponse`

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


    def DescribeBlockIPList(self, request):
        """查詢一個負載均衡所封禁的IP清單（黑名單）。（介面灰度中，如需使用請提工單）

        :param request: Request instance for DescribeBlockIPList.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeBlockIPListRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeBlockIPListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBlockIPList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBlockIPListResponse()
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


    def DescribeBlockIPTask(self, request):
        """根據 ModifyBlockIPList 介面返回的異步任務的ID，查詢封禁IP（黑名單）異步任務的執行狀态。（介面灰度中，如需使用請提工單）

        :param request: Request instance for DescribeBlockIPTask.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeBlockIPTaskRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeBlockIPTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBlockIPTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBlockIPTaskResponse()
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
        """DescribeClassicalLBByInstanceId用于通過後端實例ID獲取傳統型負載均衡ID清單

        :param request: Request instance for DescribeClassicalLBByInstanceId.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBByInstanceIdRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBByInstanceIdResponse`

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
        """DescribeClassicalLBHealthStatus用于獲取傳統型負載均衡後端的健康狀态

        :param request: Request instance for DescribeClassicalLBHealthStatus.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBHealthStatusRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBHealthStatusResponse`

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
        """DescribeClassicalLBListeners 介面用于獲取傳統型負載均衡的監聽器訊息。

        :param request: Request instance for DescribeClassicalLBListeners.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBListenersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBListenersResponse`

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
        """DescribeClassicalLBTargets用于獲取傳統型負載均衡綁定的後端服務

        :param request: Request instance for DescribeClassicalLBTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBTargetsResponse`

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
        """DescribeListeners 介面可根據負載均衡器 ID，監聽器的協議或端口作爲過濾條件獲取監聽器清單。如果不指定任何過濾條件，則返回該負載均衡實例下的所有監聽器。

        :param request: Request instance for DescribeListeners.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeListenersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeListenersResponse`

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


    def DescribeLoadBalancerListByCertId(self, request):
        """根據證書ID查詢其在一個地域中所關聯到負載均衡實例清單

        :param request: Request instance for DescribeLoadBalancerListByCertId.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancerListByCertIdRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancerListByCertIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLoadBalancerListByCertId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLoadBalancerListByCertIdResponse()
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
        """查詢一個地域的負載均衡實例清單

        :param request: Request instance for DescribeLoadBalancers.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancersResponse`

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

        :param request: Request instance for DescribeRewrite.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeRewriteRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeRewriteResponse`

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


    def DescribeTargetGroupInstances(self, request):
        """獲取目标組綁定的服務器訊息

        :param request: Request instance for DescribeTargetGroupInstances.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeTargetGroupInstancesRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeTargetGroupInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTargetGroupInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTargetGroupInstancesResponse()
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


    def DescribeTargetGroupList(self, request):
        """獲取目标組清單

        :param request: Request instance for DescribeTargetGroupList.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeTargetGroupListRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeTargetGroupListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTargetGroupList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTargetGroupListResponse()
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


    def DescribeTargetGroups(self, request):
        """查詢目标組訊息

        :param request: Request instance for DescribeTargetGroups.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeTargetGroupsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeTargetGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTargetGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTargetGroupsResponse()
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
        """DescribeTargetHealth 介面用來獲取負載均衡後端服務的健康檢查結果，不支援傳統型負載均衡。

        :param request: Request instance for DescribeTargetHealth.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeTargetHealthRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeTargetHealthResponse`

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
        """DescribeTargets 介面用來查詢負載均衡實例的某些監聽器綁定的後端服務清單。

        :param request: Request instance for DescribeTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeTargetsResponse`

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
        """本介面用于查詢異步任務的執行狀态，對于非查詢類的介面（創建/删除負載均衡實例、監聽器、規則以及綁定或解綁後端服務等），在介面調用成功後，都需要使用本介面查詢任務最終是否執行成功。

        :param request: Request instance for DescribeTaskStatus.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeTaskStatusRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeTaskStatusResponse`

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


    def DisassociateTargetGroups(self, request):
        """解除規則的目标組關聯關系。
        本介面爲異步介面，本介面返回成功後需以返回的 RequestID 爲入參，調用 DescribeTaskStatus 介面查詢本次任務是否成功。

        :param request: Request instance for DisassociateTargetGroups.
        :type request: :class:`tencentcloud.clb.v20180317.models.DisassociateTargetGroupsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DisassociateTargetGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisassociateTargetGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateTargetGroupsResponse()
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
        """用戶手動配置原訪問網址和重定向網址，系統自動将原訪問網址的請求重定向至對應路徑的目的網址。同一域名下可以配置多條路徑作爲重定向策略，實現http/https之間請求的自動跳轉。設置重定向時，需滿足如下約束條件：若A已經重定向至B，則A不能再重定向至C（除非先删除老的重定向關系，再建立新的重定向關系），B不能重定向至任何其它網址。
        本介面爲異步介面，本介面返回成功後需以返回的RequestID爲入參，調用DescribeTaskStatus介面查詢本次任務是否成功。

        :param request: Request instance for ManualRewrite.
        :type request: :class:`tencentcloud.clb.v20180317.models.ManualRewriteRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ManualRewriteResponse`

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


    def ModifyBlockIPList(self, request):
        """修改負載均衡的IP（client IP）封禁黑名單清單，一個轉發規則最多支援封禁 2000000 個IP，及黑名單容量爲 2000000。
        （介面灰度中，如需使用請提工單）

        :param request: Request instance for ModifyBlockIPList.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyBlockIPListRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyBlockIPListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyBlockIPList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyBlockIPListResponse()
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
        """ModifyDomain介面用來修改負載均衡七層監聽器下的域名。
        本介面爲異步介面，本介面返回成功後需以返回的RequestID爲入參，調用DescribeTaskStatus介面查詢本次任務是否成功。

        :param request: Request instance for ModifyDomain.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyDomainRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyDomainResponse`

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


    def ModifyDomainAttributes(self, request):
        """ModifyDomainAttributes介面用于修改負載均衡7層監聽器轉發規則的域名級别屬性，如修改域名、修改DefaultServer、開啓/關閉Http2、修改證書。
        本介面爲異步介面，本介面返回成功後，需以返回的RequestId爲入參，調用DescribeTaskStatus介面查詢本次任務是否成功。

        :param request: Request instance for ModifyDomainAttributes.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyDomainAttributesRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyDomainAttributesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDomainAttributes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDomainAttributesResponse()
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
        """ModifyListener介面用來修改負載均衡監聽器的屬性，包括監聽器名稱、健康檢查參數、證書訊息、轉發策略等。本介面不支援傳統型負載均衡。
        本介面爲異步介面，本介面返回成功後需以返回的RequestID爲入參，調用DescribeTaskStatus介面查詢本次任務是否成功。

        :param request: Request instance for ModifyListener.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyListenerRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyListenerResponse`

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
        """修改負載均衡實例的屬性。支援修改負載均衡實例的名稱、設置負載均衡的跨域屬性。

        :param request: Request instance for ModifyLoadBalancerAttributes.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyLoadBalancerAttributesRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyLoadBalancerAttributesResponse`

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
        """ModifyRule 介面用來修改負載均衡七層監聽器下的轉發規則的各項屬性，包括轉發路徑、健康檢查屬性、轉發策略等。
        本介面爲異步介面，本介面返回成功後需以返回的RequestID爲入參，調用DescribeTaskStatus介面查詢本次任務是否成功。

        :param request: Request instance for ModifyRule.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyRuleRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyRuleResponse`

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


    def ModifyTargetGroupAttribute(self, request):
        """修改目标組的名稱或者預設端口屬性

        :param request: Request instance for ModifyTargetGroupAttribute.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyTargetGroupAttributeRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyTargetGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTargetGroupAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTargetGroupAttributeResponse()
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


    def ModifyTargetGroupInstancesPort(self, request):
        """批次修改目标組服務器端口。
        本介面爲異步介面，本介面返回成功後需以返回的 RequestID 爲入參，調用 DescribeTaskStatus 介面查詢本次任務是否成功。

        :param request: Request instance for ModifyTargetGroupInstancesPort.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyTargetGroupInstancesPortRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyTargetGroupInstancesPortResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTargetGroupInstancesPort", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTargetGroupInstancesPortResponse()
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


    def ModifyTargetGroupInstancesWeight(self, request):
        """批次修改目标組的服務器權重。
        本介面爲異步介面，本介面返回成功後需以返回的 RequestID 爲入參，調用 DescribeTaskStatus 介面查詢本次任務是否成功。

        :param request: Request instance for ModifyTargetGroupInstancesWeight.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyTargetGroupInstancesWeightRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyTargetGroupInstancesWeightResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTargetGroupInstancesWeight", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTargetGroupInstancesWeightResponse()
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
        """ModifyTargetPort介面用于修改監聽器綁定的後端服務的端口。
        本介面爲異步介面，本介面返回成功後需以返回的RequestID爲入參，調用DescribeTaskStatus介面查詢本次任務是否成功。

        :param request: Request instance for ModifyTargetPort.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyTargetPortRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyTargetPortResponse`

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
        """ModifyTargetWeight 介面用于修改負載均衡綁定的後端服務的轉發權重。
        本介面爲異步介面，本介面返回成功後需以返回的RequestID爲入參，調用DescribeTaskStatus介面查詢本次任務是否成功。

        :param request: Request instance for ModifyTargetWeight.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyTargetWeightRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyTargetWeightResponse`

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


    def RegisterTargetGroupInstances(self, request):
        """注冊服務器到目标組。
        本介面爲異步介面，本介面返回成功後需以返回的 RequestID 爲入參，調用 DescribeTaskStatus 介面查詢本次任務是否成功。

        :param request: Request instance for RegisterTargetGroupInstances.
        :type request: :class:`tencentcloud.clb.v20180317.models.RegisterTargetGroupInstancesRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.RegisterTargetGroupInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RegisterTargetGroupInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RegisterTargetGroupInstancesResponse()
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
        """RegisterTargets 介面用來将一台或多台後端服務綁定到負載均衡的監聽器（或7層轉發規則），在此之前您需要先行創建相關的4層監聽器或7層轉發規則。對于四層監聽器（TCP、UDP），只需指定監聽器ID即可，對于七層監聽器（HTTP、HTTPS），還需通過LocationId或者Domain+Url指定轉發規則。
        本介面爲異步介面，本介面返回成功後需以返回的RequestID爲入參，調用DescribeTaskStatus介面查詢本次任務是否成功。

        :param request: Request instance for RegisterTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.RegisterTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.RegisterTargetsResponse`

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
        """RegisterTargetsWithClassicalLB 介面用于綁定後端服務到傳統型負載均衡。
        本介面爲異步介面，介面返回成功後，需以返回的 RequestId 爲入參，調用 DescribeTaskStatus 介面查詢本次任務是否成功。

        :param request: Request instance for RegisterTargetsWithClassicalLB.
        :type request: :class:`tencentcloud.clb.v20180317.models.RegisterTargetsWithClassicalLBRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.RegisterTargetsWithClassicalLBResponse`

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


    def ReplaceCertForLoadBalancers(self, request):
        """ReplaceCertForLoadBalancers 介面用以替換負載均衡實例所關聯的證書，對于各個地域的負載均衡，如果指定的老的證書ID與其有關聯關系，則會先解除關聯，再建立新證書與該負載均衡的關聯關系。
        此介面支援替換服務端證書或用戶端證書。
        需要使用的新證書，可以通過傳入證書ID來指定，如果不指定證書ID，則必須傳入證書内容等相關訊息，用以新建證書并綁定至負載均衡。
        注：本介面僅可從廣州地域調用。

        :param request: Request instance for ReplaceCertForLoadBalancers.
        :type request: :class:`tencentcloud.clb.v20180317.models.ReplaceCertForLoadBalancersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ReplaceCertForLoadBalancersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReplaceCertForLoadBalancers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReplaceCertForLoadBalancersResponse()
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


    def SetLoadBalancerClsLog(self, request):
        """增加、删除、更新負載均衡的日志服務(CLS)主題

        :param request: Request instance for SetLoadBalancerClsLog.
        :type request: :class:`tencentcloud.clb.v20180317.models.SetLoadBalancerClsLogRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.SetLoadBalancerClsLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetLoadBalancerClsLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetLoadBalancerClsLogResponse()
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
        """SetLoadBalancerSecurityGroups 介面支援對一個公網負載均衡實例執行設置（綁定、解綁）安全組操作。查詢一個負載均衡實例目前已綁定的安全組，可使用 DescribeLoadBalancers 介面。本介面是set語義，
        綁定操作時，入參需要傳入負載均衡實例要綁定的所有安全組（已綁定的+新增綁定的）。
        解綁操作時，入參需要傳入負載均衡實例執行解綁後所綁定的所有安全組；如果要解綁所有安全組，可不傳此參數，或傳入空數組。注意：内網負載均衡不支援綁定安全組。

        :param request: Request instance for SetLoadBalancerSecurityGroups.
        :type request: :class:`tencentcloud.clb.v20180317.models.SetLoadBalancerSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.SetLoadBalancerSecurityGroupsResponse`

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


    def SetSecurityGroupForLoadbalancers(self, request):
        """綁定或解綁一個安全組到多個公網負載均衡實例。注意：内網負載均衡不支援綁定安全組。

        :param request: Request instance for SetSecurityGroupForLoadbalancers.
        :type request: :class:`tencentcloud.clb.v20180317.models.SetSecurityGroupForLoadbalancersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.SetSecurityGroupForLoadbalancersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetSecurityGroupForLoadbalancers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetSecurityGroupForLoadbalancersResponse()
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