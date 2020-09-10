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
from tencentcloud.ecm.v20190719 import models


class EcmClient(AbstractClient):
    _apiVersion = '2019-07-19'
    _endpoint = 'ecm.tencentcloudapi.com'


    def AllocateAddresses(self, request):
        """申請一個或多個彈性公網IP（簡稱 EIP）

        :param request: Request instance for AllocateAddresses.
        :type request: :class:`tencentcloud.ecm.v20190719.models.AllocateAddressesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.AllocateAddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AllocateAddresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AllocateAddressesResponse()
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


    def AssignPrivateIpAddresses(self, request):
        """彈性網卡申請内網 IP

        :param request: Request instance for AssignPrivateIpAddresses.
        :type request: :class:`tencentcloud.ecm.v20190719.models.AssignPrivateIpAddressesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.AssignPrivateIpAddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssignPrivateIpAddresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssignPrivateIpAddressesResponse()
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


    def AssociateAddress(self, request):
        """将彈性公網IP（簡稱 EIP）綁定到實例或彈性網卡的指定内網 IP 上。
        将 EIP 綁定到實例（CVM）上，其本質是将 EIP 綁定到實例上主網卡的主内網 IP 上。
        将 EIP 綁定到主網卡的主内網IP上，綁定過程會把其上綁定的普通公網 IP 自動解綁并釋放。
        将 EIP 綁定到指定網卡的内網 IP上（非主網卡的主内網IP），則必須先解綁該 EIP，才能再綁定新的。
        将 EIP 綁定到NAT閘道，請使用介面EipBindNatGateway
        EIP 如果欠費或被封堵，則不能被綁定。
        只有狀态爲 UNBIND 的 EIP 才能夠被綁定。

        :param request: Request instance for AssociateAddress.
        :type request: :class:`tencentcloud.ecm.v20190719.models.AssociateAddressRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.AssociateAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssociateAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateAddressResponse()
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


    def AttachNetworkInterface(self, request):
        """彈性網卡綁定雲主機

        :param request: Request instance for AttachNetworkInterface.
        :type request: :class:`tencentcloud.ecm.v20190719.models.AttachNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.AttachNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachNetworkInterface", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachNetworkInterfaceResponse()
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


    def CreateModule(self, request):
        """創模組化塊

        :param request: Request instance for CreateModule.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateModuleRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateModuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateModule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateModuleResponse()
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


    def CreateNetworkInterface(self, request):
        """創建彈性網卡

        :param request: Request instance for CreateNetworkInterface.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNetworkInterface", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNetworkInterfaceResponse()
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


    def CreateSubnet(self, request):
        """創建子網

        :param request: Request instance for CreateSubnet.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateSubnetRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateSubnetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSubnet", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSubnetResponse()
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


    def CreateVpc(self, request):
        """創建私有網絡

        :param request: Request instance for CreateVpc.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateVpcRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateVpcResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateVpc", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVpcResponse()
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


    def DeleteImage(self, request):
        """删除映像

        :param request: Request instance for DeleteImage.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteImageRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteImageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteImage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteImageResponse()
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


    def DeleteModule(self, request):
        """删除業務模組

        :param request: Request instance for DeleteModule.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteModuleRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteModuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteModule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteModuleResponse()
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


    def DeleteNetworkInterface(self, request):
        """删除彈性網卡

        :param request: Request instance for DeleteNetworkInterface.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNetworkInterface", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNetworkInterfaceResponse()
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


    def DeleteSubnet(self, request):
        """删除子網

        :param request: Request instance for DeleteSubnet.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteSubnetRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteSubnetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSubnet", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSubnetResponse()
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


    def DeleteVpc(self, request):
        """删除私有網絡

        :param request: Request instance for DeleteVpc.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteVpcRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteVpcResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteVpc", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteVpcResponse()
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


    def DescribeAddressQuota(self, request):
        """查詢您帳戶的彈性公網IP（簡稱 EIP）在當前地域的配額訊息

        :param request: Request instance for DescribeAddressQuota.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeAddressQuotaRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeAddressQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAddressQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAddressQuotaResponse()
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


    def DescribeAddresses(self, request):
        """查詢彈性公網IP清單

        :param request: Request instance for DescribeAddresses.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeAddressesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeAddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAddresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAddressesResponse()
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


    def DescribeBaseOverview(self, request):
        """獲取概覽頁統計的基本數據

        :param request: Request instance for DescribeBaseOverview.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeBaseOverviewRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeBaseOverviewResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBaseOverview", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBaseOverviewResponse()
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


    def DescribeConfig(self, request):
        """獲取頻寬硬碟等數據的限制

        :param request: Request instance for DescribeConfig.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeConfigRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeConfigResponse()
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


    def DescribeImage(self, request):
        """展示映像清單

        :param request: Request instance for DescribeImage.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeImageRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeImageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageResponse()
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


    def DescribeInstanceTypeConfig(self, request):
        """獲取機型配置清單

        :param request: Request instance for DescribeInstanceTypeConfig.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeInstanceTypeConfigRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeInstanceTypeConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceTypeConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceTypeConfigResponse()
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


    def DescribeInstances(self, request):
        """獲取實例的相關訊息。

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstancesResponse()
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


    def DescribeInstancesDeniedActions(self, request):
        """通過實例id獲取當前禁止的操作

        :param request: Request instance for DescribeInstancesDeniedActions.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeInstancesDeniedActionsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeInstancesDeniedActionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstancesDeniedActions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstancesDeniedActionsResponse()
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


    def DescribeModule(self, request):
        """獲取模組清單

        :param request: Request instance for DescribeModule.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeModuleRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeModuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeModule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeModuleResponse()
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


    def DescribeModuleDetail(self, request):
        """展示模組詳細訊息

        :param request: Request instance for DescribeModuleDetail.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeModuleDetailRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeModuleDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeModuleDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeModuleDetailResponse()
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


    def DescribeNetworkInterfaces(self, request):
        """查詢彈性網卡清單

        :param request: Request instance for DescribeNetworkInterfaces.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeNetworkInterfacesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeNetworkInterfacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNetworkInterfaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNetworkInterfacesResponse()
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


    def DescribeNode(self, request):
        """獲取節點清單

        :param request: Request instance for DescribeNode.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeNodeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeNodeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNodeResponse()
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


    def DescribePeakBaseOverview(self, request):
        """CPU 内存 硬碟等基礎訊息峰值數據

        :param request: Request instance for DescribePeakBaseOverview.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribePeakBaseOverviewRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribePeakBaseOverviewResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePeakBaseOverview", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePeakBaseOverviewResponse()
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


    def DescribePeakNetworkOverview(self, request):
        """獲取網絡峰值數據

        :param request: Request instance for DescribePeakNetworkOverview.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribePeakNetworkOverviewRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribePeakNetworkOverviewResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePeakNetworkOverview", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePeakNetworkOverviewResponse()
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


    def DescribeSubnets(self, request):
        """查詢子網清單

        :param request: Request instance for DescribeSubnets.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeSubnetsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeSubnetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSubnets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSubnetsResponse()
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


    def DescribeTaskResult(self, request):
        """查詢EIP異步任務執行結果

        :param request: Request instance for DescribeTaskResult.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeTaskResultRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeTaskResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskResultResponse()
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


    def DescribeVpcs(self, request):
        """查詢私有網絡清單

        :param request: Request instance for DescribeVpcs.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeVpcsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeVpcsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpcs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpcsResponse()
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


    def DetachNetworkInterface(self, request):
        """彈性網卡解綁雲主機

        :param request: Request instance for DetachNetworkInterface.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DetachNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DetachNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachNetworkInterface", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachNetworkInterfaceResponse()
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


    def DisassociateAddress(self, request):
        """解綁彈性公網IP（簡稱 EIP）
        只有狀态爲 BIND 和 BIND_ENI 的 EIP 才能進行解綁定操作。
        EIP 如果被封堵，則不能進行解綁定操作。

        :param request: Request instance for DisassociateAddress.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DisassociateAddressRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DisassociateAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisassociateAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateAddressResponse()
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


    def ImportImage(self, request):
        """從CVM産品導入映像到ECM

        :param request: Request instance for ImportImage.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ImportImageRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ImportImageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImportImage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImportImageResponse()
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


    def MigrateNetworkInterface(self, request):
        """彈性網卡遷移

        :param request: Request instance for MigrateNetworkInterface.
        :type request: :class:`tencentcloud.ecm.v20190719.models.MigrateNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.MigrateNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MigrateNetworkInterface", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MigrateNetworkInterfaceResponse()
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


    def MigratePrivateIpAddress(self, request):
        """彈性網卡内網IP遷移。
        該介面用于将一個内網IP從一個彈性網卡上遷移到另外一個彈性網卡，主IP網址不支援遷移。
        遷移前後的彈性網卡必須在同一個子網内。

        :param request: Request instance for MigratePrivateIpAddress.
        :type request: :class:`tencentcloud.ecm.v20190719.models.MigratePrivateIpAddressRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.MigratePrivateIpAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MigratePrivateIpAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MigratePrivateIpAddressResponse()
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


    def ModifyAddressAttribute(self, request):
        """修改彈性公網IP屬性

        :param request: Request instance for ModifyAddressAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyAddressAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyAddressAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAddressAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAddressAttributeResponse()
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


    def ModifyAddressesBandwidth(self, request):
        """調整彈性公網IP頻寬

        :param request: Request instance for ModifyAddressesBandwidth.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyAddressesBandwidthRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyAddressesBandwidthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAddressesBandwidth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAddressesBandwidthResponse()
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


    def ModifyInstancesAttribute(self, request):
        """修改實例的屬性。

        :param request: Request instance for ModifyInstancesAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyInstancesAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyInstancesAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstancesAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstancesAttributeResponse()
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


    def ModifyModuleImage(self, request):
        """ModifyModuleImage

        :param request: Request instance for ModifyModuleImage.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleImageRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleImageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyModuleImage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyModuleImageResponse()
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


    def ModifyModuleName(self, request):
        """修改模組名稱

        :param request: Request instance for ModifyModuleName.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleNameRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyModuleName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyModuleNameResponse()
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


    def ModifyModuleNetwork(self, request):
        """修改模組預設頻寬上限

        :param request: Request instance for ModifyModuleNetwork.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleNetworkRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleNetworkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyModuleNetwork", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyModuleNetworkResponse()
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


    def ModifySubnetAttribute(self, request):
        """修改子網屬性

        :param request: Request instance for ModifySubnetAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifySubnetAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifySubnetAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySubnetAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySubnetAttributeResponse()
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


    def ModifyVpcAttribute(self, request):
        """修改私有網絡（VPC）的相關屬性

        :param request: Request instance for ModifyVpcAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyVpcAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyVpcAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyVpcAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVpcAttributeResponse()
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


    def RebootInstances(self, request):
        """只有狀态爲RUNNING的實例才可以進行此操作；介面調用成功時，實例會進入REBOOTING狀态；重啓實例成功時，實例會進入RUNNING狀态；支援強制重啓，強制重啓的效果等同于關閉物理電腦的電源開關再重新啓動。強制重啓可能會導緻數據丢失或文件系統損壞，請僅在服務器不能正常重啓時使用。

        :param request: Request instance for RebootInstances.
        :type request: :class:`tencentcloud.ecm.v20190719.models.RebootInstancesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.RebootInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RebootInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RebootInstancesResponse()
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


    def ReleaseAddresses(self, request):
        """釋放一個或多個彈性公網IP（簡稱 EIP）。
        該操作不可逆，釋放後 EIP 關聯的 IP 網址将不再屬于您的名下。
        只有狀态爲 UNBIND 的 EIP 才能進行釋放操作。

        :param request: Request instance for ReleaseAddresses.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ReleaseAddressesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ReleaseAddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReleaseAddresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReleaseAddressesResponse()
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


    def RemovePrivateIpAddresses(self, request):
        """彈性網卡退還内網 IP。
        退還彈性網卡上的輔助内網IP，介面自動解關聯彈性公網 IP。不能退還彈性網卡的主内網IP。

        :param request: Request instance for RemovePrivateIpAddresses.
        :type request: :class:`tencentcloud.ecm.v20190719.models.RemovePrivateIpAddressesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.RemovePrivateIpAddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RemovePrivateIpAddresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemovePrivateIpAddressesResponse()
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


    def ResetInstances(self, request):
        """重裝實例，若指定了ImageId參數，則使用指定的映像重裝；否則按照當前實例使用的映像進行重裝；若未指定密碼，則密碼通過站内信形式随後發送。

        :param request: Request instance for ResetInstances.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ResetInstancesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ResetInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetInstancesResponse()
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


    def ResetInstancesMaxBandwidth(self, request):
        """重置實例的最大頻寬上限。

        :param request: Request instance for ResetInstancesMaxBandwidth.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ResetInstancesMaxBandwidthRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ResetInstancesMaxBandwidthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetInstancesMaxBandwidth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetInstancesMaxBandwidthResponse()
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


    def ResetInstancesPassword(self, request):
        """重置處于運作中狀态的實例的密碼，需要顯式指定強制關機參數ForceStop。如果沒有顯式指定強制關機參數，則只有處于關機狀态的實例才允許執行重置密碼操作。

        :param request: Request instance for ResetInstancesPassword.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ResetInstancesPasswordRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ResetInstancesPasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetInstancesPassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetInstancesPasswordResponse()
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


    def RunInstances(self, request):
        """創建ECM實例

        :param request: Request instance for RunInstances.
        :type request: :class:`tencentcloud.ecm.v20190719.models.RunInstancesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.RunInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RunInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RunInstancesResponse()
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


    def StartInstances(self, request):
        """只有狀态爲STOPPED的實例才可以進行此操作；介面調用成功時，實例會進入STARTING狀态；啓動實例成功時，實例會進入RUNNING狀态。

        :param request: Request instance for StartInstances.
        :type request: :class:`tencentcloud.ecm.v20190719.models.StartInstancesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.StartInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartInstancesResponse()
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


    def StopInstances(self, request):
        """只有處于"RUNNING"狀态的實例才能夠進行關機操作；
        調用成功時，實例會進入STOPPING狀态；關閉實例成功時，實例會進入STOPPED狀态；
        支援強制關閉，強制關機的效果等同于關閉物理電腦的電源開關，強制關機可能會導緻數據丢失或文件系統損壞，請僅在服務器不能正常關機時使用。

        :param request: Request instance for StopInstances.
        :type request: :class:`tencentcloud.ecm.v20190719.models.StopInstancesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.StopInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopInstancesResponse()
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


    def TerminateInstances(self, request):
        """銷毀實例

        :param request: Request instance for TerminateInstances.
        :type request: :class:`tencentcloud.ecm.v20190719.models.TerminateInstancesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.TerminateInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TerminateInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateInstancesResponse()
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