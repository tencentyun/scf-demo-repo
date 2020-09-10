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
from taifucloudcloud.partners.v20180321 import models


class PartnersClient(AbstractClient):
    _apiVersion = '2018-03-21'
    _endpoint = 'partners.taifucloudcloudapi.com'


    def AgentPayDeals(self, request):
        """ 支付訂單介面，支援自付/代付

        :param request: Request instance for AgentPayDeals.
        :type request: :class:`taifucloudcloud.partners.v20180321.models.AgentPayDealsRequest`
        :rtype: :class:`taifucloudcloud.partners.v20180321.models.AgentPayDealsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AgentPayDeals", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AgentPayDealsResponse()
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


    def AgentTransferMoney(self, request):
        """爲合作夥伴提供轉賬給客戶能力。僅支援合作夥伴爲自己名下客戶轉賬。

        :param request: Request instance for AgentTransferMoney.
        :type request: :class:`taifucloudcloud.partners.v20180321.models.AgentTransferMoneyRequest`
        :rtype: :class:`taifucloudcloud.partners.v20180321.models.AgentTransferMoneyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AgentTransferMoney", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AgentTransferMoneyResponse()
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


    def AuditApplyClient(self, request):
        """ 可以審核其名下申請中代客

        :param request: Request instance for AuditApplyClient.
        :type request: :class:`taifucloudcloud.partners.v20180321.models.AuditApplyClientRequest`
        :rtype: :class:`taifucloudcloud.partners.v20180321.models.AuditApplyClientResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AuditApplyClient", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AuditApplyClientResponse()
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


    def CreatePayRelationForClient(self, request):
        """合作夥伴爲客戶創建強代付關系

        :param request: Request instance for CreatePayRelationForClient.
        :type request: :class:`taifucloudcloud.partners.v20180321.models.CreatePayRelationForClientRequest`
        :rtype: :class:`taifucloudcloud.partners.v20180321.models.CreatePayRelationForClientResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePayRelationForClient", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePayRelationForClientResponse()
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


    def DescribeAgentAuditedClients(self, request):
        """查詢已審核客戶清單

        :param request: Request instance for DescribeAgentAuditedClients.
        :type request: :class:`taifucloudcloud.partners.v20180321.models.DescribeAgentAuditedClientsRequest`
        :rtype: :class:`taifucloudcloud.partners.v20180321.models.DescribeAgentAuditedClientsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAgentAuditedClients", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAgentAuditedClientsResponse()
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


    def DescribeAgentBills(self, request):
        """ 可查詢自己及名下代客所有業務明細

        :param request: Request instance for DescribeAgentBills.
        :type request: :class:`taifucloudcloud.partners.v20180321.models.DescribeAgentBillsRequest`
        :rtype: :class:`taifucloudcloud.partners.v20180321.models.DescribeAgentBillsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAgentBills", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAgentBillsResponse()
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


    def DescribeAgentClients(self, request):
        """ 可查詢自己名下待審核客戶清單

        :param request: Request instance for DescribeAgentClients.
        :type request: :class:`taifucloudcloud.partners.v20180321.models.DescribeAgentClientsRequest`
        :rtype: :class:`taifucloudcloud.partners.v20180321.models.DescribeAgentClientsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAgentClients", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAgentClientsResponse()
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


    def DescribeAgentDealsCache(self, request):
        """供超大型 （代客數量>=3000 ）拉取快取的全量客戶訂單。

        :param request: Request instance for DescribeAgentDealsCache.
        :type request: :class:`taifucloudcloud.partners.v20180321.models.DescribeAgentDealsCacheRequest`
        :rtype: :class:`taifucloudcloud.partners.v20180321.models.DescribeAgentDealsCacheResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAgentDealsCache", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAgentDealsCacheResponse()
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


    def DescribeAgentPayDeals(self, request):
        """可以查詢 代付的所有訂單

        :param request: Request instance for DescribeAgentPayDeals.
        :type request: :class:`taifucloudcloud.partners.v20180321.models.DescribeAgentPayDealsRequest`
        :rtype: :class:`taifucloudcloud.partners.v20180321.models.DescribeAgentPayDealsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAgentPayDeals", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAgentPayDealsResponse()
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


    def DescribeClientBalance(self, request):
        """爲合作夥伴提供查詢客戶餘額能力。調用者必須是合作夥伴，只能查詢自己名下客戶餘額

        :param request: Request instance for DescribeClientBalance.
        :type request: :class:`taifucloudcloud.partners.v20180321.models.DescribeClientBalanceRequest`
        :rtype: :class:`taifucloudcloud.partners.v20180321.models.DescribeClientBalanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClientBalance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClientBalanceResponse()
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


    def DescribeRebateInfos(self, request):
        """ 可查詢自己名下全部返傭訊息

        :param request: Request instance for DescribeRebateInfos.
        :type request: :class:`taifucloudcloud.partners.v20180321.models.DescribeRebateInfosRequest`
        :rtype: :class:`taifucloudcloud.partners.v20180321.models.DescribeRebateInfosResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRebateInfos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRebateInfosResponse()
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


    def DescribeSalesmans(self, request):
        """ 查詢名下業務員清單訊息

        :param request: Request instance for DescribeSalesmans.
        :type request: :class:`taifucloudcloud.partners.v20180321.models.DescribeSalesmansRequest`
        :rtype: :class:`taifucloudcloud.partners.v20180321.models.DescribeSalesmansResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSalesmans", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSalesmansResponse()
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


    def ModifyClientRemark(self, request):
        """ 可以對名下客戶添加備注、修改備注

        :param request: Request instance for ModifyClientRemark.
        :type request: :class:`taifucloudcloud.partners.v20180321.models.ModifyClientRemarkRequest`
        :rtype: :class:`taifucloudcloud.partners.v20180321.models.ModifyClientRemarkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyClientRemark", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyClientRemarkResponse()
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


    def RemovePayRelationForClient(self, request):
        """合作夥伴爲客戶消除強代付關系

        :param request: Request instance for RemovePayRelationForClient.
        :type request: :class:`taifucloudcloud.partners.v20180321.models.RemovePayRelationForClientRequest`
        :rtype: :class:`taifucloudcloud.partners.v20180321.models.RemovePayRelationForClientResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RemovePayRelationForClient", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemovePayRelationForClientResponse()
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