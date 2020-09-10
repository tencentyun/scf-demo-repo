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
from taifucloudcloud.bmvpc.v20180625 import models


class BmvpcClient(AbstractClient):
    _apiVersion = '2018-06-25'
    _endpoint = 'bmvpc.taifucloudcloudapi.com'


    def AcceptVpcPeerConnection(self, request):
        """接受黑石對等連接

        :param request: Request instance for AcceptVpcPeerConnection.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.AcceptVpcPeerConnectionRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.AcceptVpcPeerConnectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AcceptVpcPeerConnection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AcceptVpcPeerConnectionResponse()
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


    def AsyncRegisterIps(self, request):
        """批次注冊虛拟IP，異步介面。通過介面來查詢任務進度。每次請求最多注冊256個IP

        :param request: Request instance for AsyncRegisterIps.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.AsyncRegisterIpsRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.AsyncRegisterIpsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AsyncRegisterIps", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AsyncRegisterIpsResponse()
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


    def BindEipsToNatGateway(self, request):
        """NAT閘道綁定EIP介面，可将EIP綁定到NAT閘道，該EIP作爲訪問外網的源IP網址，将流量發送到Internet

        :param request: Request instance for BindEipsToNatGateway.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.BindEipsToNatGatewayRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.BindEipsToNatGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindEipsToNatGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindEipsToNatGatewayResponse()
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


    def BindIpsToNatGateway(self, request):
        """可用于将子網的部分IP綁定到NAT閘道

        :param request: Request instance for BindIpsToNatGateway.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.BindIpsToNatGatewayRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.BindIpsToNatGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindIpsToNatGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindIpsToNatGatewayResponse()
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


    def BindSubnetsToNatGateway(self, request):
        """NAT閘道綁定子網後，該子網内全部IP可出公網

        :param request: Request instance for BindSubnetsToNatGateway.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.BindSubnetsToNatGatewayRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.BindSubnetsToNatGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindSubnetsToNatGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindSubnetsToNatGatewayResponse()
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


    def CreateCustomerGateway(self, request):
        """本介面（CreateCustomerGateway）用于創建對端閘道。

        :param request: Request instance for CreateCustomerGateway.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.CreateCustomerGatewayRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.CreateCustomerGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCustomerGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCustomerGatewayResponse()
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


    def CreateDockerSubnetWithVlan(self, request):
        """創建黑石Docker子網， 如果不指定VlanId，将會分配2000--2999範圍的VlanId; 子網會關閉分布式閘道

        :param request: Request instance for CreateDockerSubnetWithVlan.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.CreateDockerSubnetWithVlanRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.CreateDockerSubnetWithVlanResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDockerSubnetWithVlan", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDockerSubnetWithVlanResponse()
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


    def CreateHostedInterface(self, request):
        """本介面（CreateHostedInterface）用于黑石托管機器加入帶VLANID不爲5的子網。

        1) 不能加入vlanId 爲5的子網，只能加入VLANID範圍爲2000-2999的子網。
        2) 每台托管機器最多可以加入20個子網。
        3) 每次調用最多能支援傳入10台托管機器。

        :param request: Request instance for CreateHostedInterface.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.CreateHostedInterfaceRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.CreateHostedInterfaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateHostedInterface", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateHostedInterfaceResponse()
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


    def CreateInterfaces(self, request):
        """物理機加入子網

        :param request: Request instance for CreateInterfaces.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.CreateInterfacesRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.CreateInterfacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateInterfaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateInterfacesResponse()
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


    def CreateNatGateway(self, request):
        """創建NAT閘道介面，可針對網段方式、子網全部IP、子網部分IP這三種方式創建NAT閘道

        :param request: Request instance for CreateNatGateway.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.CreateNatGatewayRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.CreateNatGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNatGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNatGatewayResponse()
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


    def CreateRoutePolicies(self, request):
        """創建黑石路由表的路由規則

        :param request: Request instance for CreateRoutePolicies.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.CreateRoutePoliciesRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.CreateRoutePoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateRoutePolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRoutePoliciesResponse()
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
        """創建黑石私有網絡的子網
        訪問管理: 用戶可以對VpcId進行授權操作。例如設置資源爲["qcs::bmvpc:::unVpc/vpc-xxxxx"]

        :param request: Request instance for CreateSubnet.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.CreateSubnetRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.CreateSubnetResponse`

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


    def CreateVirtualSubnetWithVlan(self, request):
        """創建黑石虛拟子網， 虛拟子網用于在黑石上創建虛拟網絡，與黑石子網要做好規劃。虛拟子網會分配2000-2999的VlanId。

        :param request: Request instance for CreateVirtualSubnetWithVlan.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.CreateVirtualSubnetWithVlanRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.CreateVirtualSubnetWithVlanResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateVirtualSubnetWithVlan", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVirtualSubnetWithVlanResponse()
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
        """創建黑石私有網絡

        :param request: Request instance for CreateVpc.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.CreateVpcRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.CreateVpcResponse`

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


    def CreateVpcPeerConnection(self, request):
        """創建對等連接

        :param request: Request instance for CreateVpcPeerConnection.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.CreateVpcPeerConnectionRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.CreateVpcPeerConnectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateVpcPeerConnection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVpcPeerConnectionResponse()
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


    def DeleteCustomerGateway(self, request):
        """本介面（DeleteCustomerGateway）用于删除對端閘道。

        :param request: Request instance for DeleteCustomerGateway.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DeleteCustomerGatewayRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DeleteCustomerGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCustomerGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCustomerGatewayResponse()
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


    def DeleteHostedInterface(self, request):
        """本介面用于托管機器從VLANID不爲5的子網中移除。
        1) 不能從vlanId 爲5的子網中移除。
        2) 每次調用最多能支援傳入10台物理機。

        :param request: Request instance for DeleteHostedInterface.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DeleteHostedInterfaceRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DeleteHostedInterfaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteHostedInterface", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteHostedInterfaceResponse()
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


    def DeleteHostedInterfaces(self, request):
        """托管機器移除子網批次介面，傳入一台托管機器和多個子網，批次移除這些子網。異步介面，介面返回TaskId。

        :param request: Request instance for DeleteHostedInterfaces.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DeleteHostedInterfacesRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DeleteHostedInterfacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteHostedInterfaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteHostedInterfacesResponse()
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


    def DeleteInterfaces(self, request):
        """物理機移除子網批次介面，傳入一台物理機和多個子網，批次移除這些子網。異步介面，介面返回TaskId。

        :param request: Request instance for DeleteInterfaces.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DeleteInterfacesRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DeleteInterfacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteInterfaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteInterfacesResponse()
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


    def DeleteNatGateway(self, request):
        """删除NAT閘道

        :param request: Request instance for DeleteNatGateway.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DeleteNatGatewayRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DeleteNatGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNatGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNatGatewayResponse()
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


    def DeleteRoutePolicy(self, request):
        """删除黑石路由表路由規則

        :param request: Request instance for DeleteRoutePolicy.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DeleteRoutePolicyRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DeleteRoutePolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteRoutePolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRoutePolicyResponse()
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
        """本介面（DeleteSubnet）用于删除黑石私有網絡子網。
        删除子網前，請清理該子網下所有資源，包括物理機、負載均衡、黑石資料庫、彈性IP、NAT閘道等資源

        :param request: Request instance for DeleteSubnet.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DeleteSubnetRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DeleteSubnetResponse`

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


    def DeleteVirtualIp(self, request):
        """退還虛拟IP。此介面只能退還虛拟IP，物理機IP不能退還。

        :param request: Request instance for DeleteVirtualIp.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DeleteVirtualIpRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DeleteVirtualIpResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteVirtualIp", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteVirtualIpResponse()
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
        """本介面(DeleteVpc)用于删除黑石私有網絡(VPC)。

        删除私有網絡前，請清理該私有網絡下所有資源，包括子網、負載均衡、彈性 IP、對等連接、NAT 閘道、專線通道、SSLVPN 等資源。

        :param request: Request instance for DeleteVpc.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DeleteVpcRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DeleteVpcResponse`

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


    def DeleteVpcPeerConnection(self, request):
        """删除黑石對等連接

        :param request: Request instance for DeleteVpcPeerConnection.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DeleteVpcPeerConnectionRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DeleteVpcPeerConnectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteVpcPeerConnection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteVpcPeerConnectionResponse()
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


    def DeleteVpnConnection(self, request):
        """本介面(DeleteVpnConnection)用于删除VPN通道。

        :param request: Request instance for DeleteVpnConnection.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DeleteVpnConnectionRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DeleteVpnConnectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteVpnConnection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteVpnConnectionResponse()
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


    def DeleteVpnGateway(self, request):
        """本介面（DeleteVpnGateway）用于删除VPN閘道。

        :param request: Request instance for DeleteVpnGateway.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DeleteVpnGatewayRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DeleteVpnGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteVpnGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteVpnGatewayResponse()
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


    def DeregisterIps(self, request):
        """注銷私有網絡IP爲空閑

        :param request: Request instance for DeregisterIps.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DeregisterIpsRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DeregisterIpsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeregisterIps", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeregisterIpsResponse()
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


    def DescribeCustomerGateways(self, request):
        """本介面（DescribeCustomerGateways）用于查詢對端閘道清單。

        :param request: Request instance for DescribeCustomerGateways.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeCustomerGatewaysRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeCustomerGatewaysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCustomerGateways", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCustomerGatewaysResponse()
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


    def DescribeNatGateways(self, request):
        """獲取NAT閘道訊息，包括NAT閘道 ID、閘道名稱、私有網絡、閘道并發連接上限、綁定EIP清單等

        :param request: Request instance for DescribeNatGateways.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeNatGatewaysRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeNatGatewaysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNatGateways", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNatGatewaysResponse()
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


    def DescribeNatSubnets(self, request):
        """可獲取NAT閘道綁定的子網訊息

        :param request: Request instance for DescribeNatSubnets.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeNatSubnetsRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeNatSubnetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNatSubnets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNatSubnetsResponse()
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


    def DescribeRoutePolicies(self, request):
        """本介面（DescribeRoutePolicies）用于查詢路由表條目。

        :param request: Request instance for DescribeRoutePolicies.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeRoutePoliciesRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeRoutePoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRoutePolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRoutePoliciesResponse()
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


    def DescribeRouteTables(self, request):
        """本介面（DescribeRouteTables）用于查詢路由表。

        :param request: Request instance for DescribeRouteTables.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeRouteTablesRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeRouteTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRouteTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRouteTablesResponse()
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


    def DescribeSubnetAvailableIps(self, request):
        """獲取子網内可用IP清單

        :param request: Request instance for DescribeSubnetAvailableIps.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeSubnetAvailableIpsRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeSubnetAvailableIpsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSubnetAvailableIps", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSubnetAvailableIpsResponse()
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


    def DescribeSubnetByDevice(self, request):
        """物理機可以加入物理機子網，虛拟子網，DOCKER子網，通過此介面可以查詢物理機加入的子網。

        :param request: Request instance for DescribeSubnetByDevice.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeSubnetByDeviceRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeSubnetByDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSubnetByDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSubnetByDeviceResponse()
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


    def DescribeSubnetByHostedDevice(self, request):
        """托管可以加入物理機子網，虛拟子網，DOCKER子網，通過此介面可以查詢托管加入的子網。

        :param request: Request instance for DescribeSubnetByHostedDevice.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeSubnetByHostedDeviceRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeSubnetByHostedDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSubnetByHostedDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSubnetByHostedDeviceResponse()
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
        """本介面（DescribeSubnets）用于查詢黑石子網清單。

        :param request: Request instance for DescribeSubnets.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeSubnetsRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeSubnetsResponse`

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


    def DescribeTaskStatus(self, request):
        """根據任務ID，獲取任務的執行狀态

        :param request: Request instance for DescribeTaskStatus.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeTaskStatusRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeTaskStatusResponse`

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


    def DescribeVpcPeerConnections(self, request):
        """獲取對等連接清單

        :param request: Request instance for DescribeVpcPeerConnections.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeVpcPeerConnectionsRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeVpcPeerConnectionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpcPeerConnections", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpcPeerConnectionsResponse()
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


    def DescribeVpcQuota(self, request):
        """本介面（DescribeVpcQuota）用于查詢用戶VPC相關配額限制。

        :param request: Request instance for DescribeVpcQuota.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeVpcQuotaRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeVpcQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpcQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpcQuotaResponse()
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


    def DescribeVpcResource(self, request):
        """查詢黑石私有網絡關聯資源

        :param request: Request instance for DescribeVpcResource.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeVpcResourceRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeVpcResourceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpcResource", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpcResourceResponse()
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


    def DescribeVpcView(self, request):
        """本介面（DescribeVpcView）用于查詢VPC網絡拓撲視圖。

        :param request: Request instance for DescribeVpcView.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeVpcViewRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeVpcViewResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpcView", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpcViewResponse()
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
        """本介面（DescribeVpcs）用于查詢私有網絡清單。
        本介面不傳參數時，返回預設排序下的前20條VPC訊息。

        :param request: Request instance for DescribeVpcs.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeVpcsRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeVpcsResponse`

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


    def DescribeVpnConnections(self, request):
        """本介面（DescribeVpnConnections）查詢VPN通道清單。

        :param request: Request instance for DescribeVpnConnections.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeVpnConnectionsRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeVpnConnectionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpnConnections", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpnConnectionsResponse()
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


    def DescribeVpnGateways(self, request):
        """本介面（DescribeVpnGateways）用于查詢VPN閘道清單。

        :param request: Request instance for DescribeVpnGateways.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeVpnGatewaysRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DescribeVpnGatewaysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpnGateways", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpnGatewaysResponse()
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


    def DownloadCustomerGatewayConfiguration(self, request):
        """本介面(DownloadCustomerGatewayConfiguration)用于下載VPN通道配置。

        :param request: Request instance for DownloadCustomerGatewayConfiguration.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.DownloadCustomerGatewayConfigurationRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.DownloadCustomerGatewayConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DownloadCustomerGatewayConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DownloadCustomerGatewayConfigurationResponse()
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


    def ModifyCustomerGatewayAttribute(self, request):
        """本介面（ModifyCustomerGatewayAttribute）用于修改對端閘道訊息。

        :param request: Request instance for ModifyCustomerGatewayAttribute.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.ModifyCustomerGatewayAttributeRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.ModifyCustomerGatewayAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCustomerGatewayAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCustomerGatewayAttributeResponse()
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


    def ModifyRoutePolicy(self, request):
        """修改自定義路由

        :param request: Request instance for ModifyRoutePolicy.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.ModifyRoutePolicyRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.ModifyRoutePolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyRoutePolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRoutePolicyResponse()
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


    def ModifyRouteTable(self, request):
        """修改路由表

        :param request: Request instance for ModifyRouteTable.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.ModifyRouteTableRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.ModifyRouteTableResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyRouteTable", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRouteTableResponse()
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
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.ModifySubnetAttributeRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.ModifySubnetAttributeResponse`

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


    def ModifySubnetDHCPRelay(self, request):
        """修改子網DHCP Relay屬性

        :param request: Request instance for ModifySubnetDHCPRelay.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.ModifySubnetDHCPRelayRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.ModifySubnetDHCPRelayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySubnetDHCPRelay", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySubnetDHCPRelayResponse()
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
        """本介面（ModifyVpcAttribute）用于修改VPC的标識名稱和控制VPC的監控起停。

        :param request: Request instance for ModifyVpcAttribute.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.ModifyVpcAttributeRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.ModifyVpcAttributeResponse`

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


    def ModifyVpcPeerConnection(self, request):
        """修改黑石對等連接

        :param request: Request instance for ModifyVpcPeerConnection.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.ModifyVpcPeerConnectionRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.ModifyVpcPeerConnectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyVpcPeerConnection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVpcPeerConnectionResponse()
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


    def ModifyVpnConnectionAttribute(self, request):
        """本介面（ModifyVpnConnectionAttribute）用于修改VPN通道。

        :param request: Request instance for ModifyVpnConnectionAttribute.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.ModifyVpnConnectionAttributeRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.ModifyVpnConnectionAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyVpnConnectionAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVpnConnectionAttributeResponse()
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


    def ModifyVpnGatewayAttribute(self, request):
        """本介面（ModifyVpnGatewayAttribute）用于修改VPN閘道屬性。

        :param request: Request instance for ModifyVpnGatewayAttribute.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.ModifyVpnGatewayAttributeRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.ModifyVpnGatewayAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyVpnGatewayAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVpnGatewayAttributeResponse()
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


    def RejectVpcPeerConnection(self, request):
        """拒絕黑石對等連接申請

        :param request: Request instance for RejectVpcPeerConnection.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.RejectVpcPeerConnectionRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.RejectVpcPeerConnectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RejectVpcPeerConnection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RejectVpcPeerConnectionResponse()
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


    def ResetVpnConnection(self, request):
        """本介面(ResetVpnConnection)用于重置VPN通道。

        :param request: Request instance for ResetVpnConnection.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.ResetVpnConnectionRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.ResetVpnConnectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetVpnConnection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetVpnConnectionResponse()
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


    def UnbindEipsFromNatGateway(self, request):
        """NAT閘道解綁該EIP後，NAT閘道将不會使用該EIP作爲訪問外網的源IP網址

        :param request: Request instance for UnbindEipsFromNatGateway.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.UnbindEipsFromNatGatewayRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.UnbindEipsFromNatGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnbindEipsFromNatGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindEipsFromNatGatewayResponse()
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


    def UnbindIpsFromNatGateway(self, request):
        """NAT閘道解綁IP介面，可将子網的部分IP從NAT閘道中解綁

        :param request: Request instance for UnbindIpsFromNatGateway.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.UnbindIpsFromNatGatewayRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.UnbindIpsFromNatGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnbindIpsFromNatGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindIpsFromNatGatewayResponse()
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


    def UnbindSubnetsFromNatGateway(self, request):
        """NAT閘道解綁子網介面，可将子網解綁NAT閘道

        :param request: Request instance for UnbindSubnetsFromNatGateway.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.UnbindSubnetsFromNatGatewayRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.UnbindSubnetsFromNatGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnbindSubnetsFromNatGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindSubnetsFromNatGatewayResponse()
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


    def UpgradeNatGateway(self, request):
        """升級NAT閘道介面，可NAT閘道修改爲小型NAT閘道、中型NAT閘道、以及大型NAT閘道

        :param request: Request instance for UpgradeNatGateway.
        :type request: :class:`taifucloudcloud.bmvpc.v20180625.models.UpgradeNatGatewayRequest`
        :rtype: :class:`taifucloudcloud.bmvpc.v20180625.models.UpgradeNatGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeNatGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeNatGatewayResponse()
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