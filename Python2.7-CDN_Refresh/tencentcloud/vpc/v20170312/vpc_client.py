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
from tencentcloud.vpc.v20170312 import models


class VpcClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'vpc.tencentcloudapi.com'


    def AcceptAttachCcnInstances(self, request):
        """本介面（AcceptAttachCcnInstances）用于跨賬号關聯實例時，雲聯網所有者接受并同意關聯操作。

        :param request: Request instance for AcceptAttachCcnInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AcceptAttachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AcceptAttachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AcceptAttachCcnInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AcceptAttachCcnInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddBandwidthPackageResources(self, request):
        """介面用于添加頻寬包資源，包括[彈性公網IP](https://cloud.tencent.com/document/product/213/1941)和[負載均衡](https://cloud.tencent.com/document/product/214/517)等

        :param request: Request instance for AddBandwidthPackageResources.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AddBandwidthPackageResourcesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AddBandwidthPackageResourcesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddBandwidthPackageResources", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddBandwidthPackageResourcesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddIp6Rules(self, request):
        """1. 該介面用于在轉換實例下添加IPV6轉換規則。
        2. 支援在同一個轉換實例下批次添加轉換規則，一個帳戶在一個地域最多50個。
        3. 一個完整的轉換規則包括vip6:vport6:protocol:vip:vport，其中vip6:vport6:protocol必須是唯一。

        :param request: Request instance for AddIp6Rules.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AddIp6RulesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AddIp6RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddIp6Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddIp6RulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AllocateAddresses(self, request):
        """本介面 (AllocateAddresses) 用于申請一個或多個[彈性公網IP](https://cloud.tencent.com/document/product/213/1941)（簡稱 EIP）。
        * EIP 是專爲動态雲計算設計的靜态 IP 網址。借助 EIP，您可以快速将 EIP 重新映射到您的另一個實例上，從而屏蔽實例故障。
        * 您的 EIP 與Top Cloud 帳戶相關聯，而不是與某個實例相關聯。在您選擇顯式釋放該網址，或欠費超過24小時之前，它會一直與您的Top Cloud 帳戶保持關聯。
        * 一個Top Cloud 帳戶在每個地域能申請的 EIP 最大配額有所限制，可參見 [EIP 産品簡介](https://cloud.tencent.com/document/product/213/5733)，上述配額可通過 DescribeAddressQuota 介面獲取。

        :param request: Request instance for AllocateAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AllocateAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AllocateAddressesResponse`

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


    def AllocateIp6AddressesBandwidth(self, request):
        """該介面用于給IPv6網址初次分配公網頻寬

        :param request: Request instance for AllocateIp6AddressesBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AllocateIp6AddressesBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AllocateIp6AddressesBandwidthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AllocateIp6AddressesBandwidth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AllocateIp6AddressesBandwidthResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AssignIpv6Addresses(self, request):
        """本介面（AssignIpv6Addresses）用于彈性網卡申請`IPv6`網址。<br />
        本介面是異步完成，如需查詢異步任務執行結果，請使用本介面返回的`RequestId`輪詢`QueryTask`介面。
        * 一個彈性網卡支援綁定的IP網址是有限制的，更多資源限制訊息詳見<a href="/document/product/576/18527">彈性網卡使用限制</a>。
        * 可以指定`IPv6`網址申請，網址類型不能爲主`IP`，`IPv6`網址暫時只支援作爲輔助`IP`。
        * 網址必須要在彈性網卡所在子網内，而且不能被占用。
        * 在彈性網卡上申請一個到多個輔助`IPv6`網址，介面會在彈性網卡所在子網段内返回指定數量的輔助`IPv6`網址。

        :param request: Request instance for AssignIpv6Addresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssignIpv6AddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssignIpv6AddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssignIpv6Addresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssignIpv6AddressesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AssignIpv6CidrBlock(self, request):
        """本介面（AssignIpv6CidrBlock）用于分配IPv6網段。
        * 使用本介面前，您需要已有VPC實例，如果沒有可通過介面<a href="https://cloud.tencent.com/document/api/215/15774" title="CreateVpc" target="_blank">CreateVpc</a>創建。
        * 每個VPC只能申請一個IPv6網段

        :param request: Request instance for AssignIpv6CidrBlock.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssignIpv6CidrBlockRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssignIpv6CidrBlockResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssignIpv6CidrBlock", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssignIpv6CidrBlockResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AssignIpv6SubnetCidrBlock(self, request):
        """本介面（AssignIpv6SubnetCidrBlock）用于分配IPv6子網段。
        * 給子網分配 `IPv6` 網段，要求子網所屬 `VPC` 已獲得 `IPv6` 網段。如果尚未分配，請先通過介面 `AssignIpv6CidrBlock` 給子網所屬 `VPC` 分配一個 `IPv6` 網段。否則無法分配 `IPv6` 子網段。
        * 每個子網只能分配一個IPv6網段。

        :param request: Request instance for AssignIpv6SubnetCidrBlock.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssignIpv6SubnetCidrBlockRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssignIpv6SubnetCidrBlockResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssignIpv6SubnetCidrBlock", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssignIpv6SubnetCidrBlockResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """本介面（AssignPrivateIpAddresses）用于彈性網卡申請内網 IP。
        * 一個彈性網卡支援綁定的IP網址是有限制的，更多資源限制訊息詳見<a href="/document/product/576/18527">彈性網卡使用限制</a>。
        * 可以指定内網IP網址申請，内網IP網址類型不能爲主IP，主IP已存在，不能修改，内網IP必須要彈性網卡所在子網内，而且不能被占用。
        * 在彈性網卡上申請一個到多個輔助内網IP，介面會在彈性網卡所在子網網段内返回指定數量的輔助内網IP。

        :param request: Request instance for AssignPrivateIpAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssignPrivateIpAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssignPrivateIpAddressesResponse`

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
        """本介面 (AssociateAddress) 用于将[彈性公網IP](https://cloud.tencent.com/document/product/213/1941)（簡稱 EIP）綁定到實例或彈性網卡的指定内網 IP 上。
        * 将 EIP 綁定到實例（CVM）上，其本質是将 EIP 綁定到實例上主網卡的主内網 IP 上。
        * 将 EIP 綁定到主網卡的主内網IP上，綁定過程會把其上綁定的普通公網 IP 自動解綁并釋放。
        * 将 EIP 綁定到指定網卡的内網 IP上（非主網卡的主内網IP），則必須先解綁該 EIP，才能再綁定新的。
        * 将 EIP 綁定到NAT閘道，請使用介面[EipBindNatGateway](https://cloud.tencent.com/document/product/215/4093)
        * EIP 如果欠費或被封堵，則不能被綁定。
        * 只有狀态爲 UNBIND 的 EIP 才能夠被綁定。

        :param request: Request instance for AssociateAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssociateAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssociateAddressResponse`

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


    def AssociateNatGatewayAddress(self, request):
        """本介面(AssociateNatGatewayAddress)用于NAT閘道綁定彈性IP（EIP）。

        :param request: Request instance for AssociateNatGatewayAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssociateNatGatewayAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssociateNatGatewayAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssociateNatGatewayAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateNatGatewayAddressResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AssociateNetworkAclSubnets(self, request):
        """本介面（AssociateNetworkAclSubnets）用于網絡ACL關聯vpc下的子網。

        :param request: Request instance for AssociateNetworkAclSubnets.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssociateNetworkAclSubnetsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssociateNetworkAclSubnetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssociateNetworkAclSubnets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateNetworkAclSubnetsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AssociateNetworkInterfaceSecurityGroups(self, request):
        """本介面（AssociateNetworkInterfaceSecurityGroups）用于彈性網卡綁定安全組（SecurityGroup）。

        :param request: Request instance for AssociateNetworkInterfaceSecurityGroups.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssociateNetworkInterfaceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssociateNetworkInterfaceSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssociateNetworkInterfaceSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateNetworkInterfaceSecurityGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AttachCcnInstances(self, request):
        """本介面（AttachCcnInstances）用于将網絡實例加載到雲聯網實例中，網絡實例包括VPC和專線閘道。<br />
        每個雲聯網能夠關聯的網絡實例個數是有限的，詳請參考産品文件。如果需要擴充請聯系在線客服。

        :param request: Request instance for AttachCcnInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AttachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AttachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachCcnInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachCcnInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AttachClassicLinkVpc(self, request):
        """本介面(AttachClassicLinkVpc)用于創建私有網絡和基礎網絡設備互通。
        * 私有網絡和基礎網絡設備必須在同一個地域。
        * 私有網絡和基礎網絡的區别詳見vpc産品文件-<a href="https://cloud.tencent.com/document/product/215/30720">私有網絡與基礎網絡</a>。

        :param request: Request instance for AttachClassicLinkVpc.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AttachClassicLinkVpcRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AttachClassicLinkVpcResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachClassicLinkVpc", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachClassicLinkVpcResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """本介面（AttachNetworkInterface）用于彈性網卡綁定雲主機。
        * 一個雲主機可以綁定多個彈性網卡，但只能綁定一個主網卡。更多限制訊息詳見<a href="https://cloud.tencent.com/document/product/576/18527">彈性網卡使用限制</a>。
        * 一個彈性網卡只能同時綁定一個雲主機。
        * 只有運作中或者已關機狀态的雲主機才能綁定彈性網卡，檢視雲主機狀态詳見<a href="https://cloud.tencent.com/document/api/213/9452#InstanceStatus">Top Cloud 主機訊息</a>。
        * 彈性網卡綁定的雲主機必須是私有網絡的，而且雲主機所在可用區必須和彈性網卡子網的可用區相同。

        :param request: Request instance for AttachNetworkInterface.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AttachNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AttachNetworkInterfaceResponse`

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


    def CheckAssistantCidr(self, request):
        """本介面(CheckAssistantCidr)用于檢查輔助CIDR是否與存量路由、對等連接（對端VPC的CIDR）等資源存在沖突。如果存在重疊，則返回重疊的資源。（介面灰度中，如需使用請提工單。）
        * 檢測輔助CIDR是否與當前VPC的主CIDR和輔助CIDR存在重疊。
        * 檢測輔助CIDR是否與當前VPC的路由的目的端存在重疊。
        * 檢測輔助CIDR是否與當前VPC的對等連接，對端VPC下的主CIDR或輔助CIDR存在重疊。

        :param request: Request instance for CheckAssistantCidr.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CheckAssistantCidrRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CheckAssistantCidrResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckAssistantCidr", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckAssistantCidrResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckDefaultSubnet(self, request):
        """本介面（CheckDefaultSubnet）用于預判是否可建預設子網。

        :param request: Request instance for CheckDefaultSubnet.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CheckDefaultSubnetRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CheckDefaultSubnetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckDefaultSubnet", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckDefaultSubnetResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckNetDetectState(self, request):
        """本介面(CheckNetDetectState)用于驗證網絡探測。

        :param request: Request instance for CheckNetDetectState.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CheckNetDetectStateRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CheckNetDetectStateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckNetDetectState", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckNetDetectStateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAddressTemplate(self, request):
        """本介面（CreateAddressTemplate）用于創建IP網址模版

        :param request: Request instance for CreateAddressTemplate.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateAddressTemplateRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateAddressTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAddressTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAddressTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAddressTemplateGroup(self, request):
        """本介面（CreateAddressTemplateGroup）用于創建IP網址模版集合

        :param request: Request instance for CreateAddressTemplateGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateAddressTemplateGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateAddressTemplateGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAddressTemplateGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAddressTemplateGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAndAttachNetworkInterface(self, request):
        """本介面（CreateAndAttachNetworkInterface）用于創建彈性網卡并綁定雲主機。
        * 創建彈性網卡時可以指定内網IP，并且可以指定一個主IP，指定的内網IP必須在彈性網卡所在子網内，而且不能被占用。
        * 創建彈性網卡時可以指定需要申請的内網IP數量，系統會随機生成内網IP網址。
        * 一個彈性網卡支援綁定的IP網址是有限制的，更多資源限制訊息詳見<a href="/document/product/576/18527">彈性網卡使用限制</a>。
        * 創建彈性網卡同時可以綁定已有安全組。
        * 創建彈性網卡同時可以綁定标簽, 應答裏的标簽清單代表添加成功的标簽。

        :param request: Request instance for CreateAndAttachNetworkInterface.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateAndAttachNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateAndAttachNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAndAttachNetworkInterface", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAndAttachNetworkInterfaceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAssistantCidr(self, request):
        """本介面(CreateAssistantCidr)用于批次創建輔助CIDR。（介面灰度中，如需使用請提工單。）

        :param request: Request instance for CreateAssistantCidr.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateAssistantCidrRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateAssistantCidrResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAssistantCidr", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAssistantCidrResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateBandwidthPackage(self, request):
        """介面支援創建[設備頻寬包](https://cloud.tencent.com/document/product/684/15246#.E8.AE.BE.E5.A4.87.E5.B8.A6.E5.AE.BD.E5.8C.85)和[IP頻寬包](https://cloud.tencent.com/document/product/684/15246#ip-.E5.B8.A6.E5.AE.BD.E5.8C.85)

        :param request: Request instance for CreateBandwidthPackage.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateBandwidthPackageRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateBandwidthPackageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateBandwidthPackage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateBandwidthPackageResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCcn(self, request):
        """本介面（CreateCcn）用于創建雲聯網（CCN）。<br />
        * 創建雲聯網同時可以綁定标簽, 應答裏的标簽清單代表添加成功的标簽。
        每個賬号能創建的雲聯網實例個數是有限的，詳請參考産品文件。如果需要擴充請聯系在線客服。

        :param request: Request instance for CreateCcn.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateCcnRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateCcnResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCcn", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCcnResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateCustomerGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateCustomerGatewayResponse`

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


    def CreateDefaultSecurityGroup(self, request):
        """本介面（CreateDefaultSecurityGroup）用于創建（如果項目下未存在預設安全組，則創建；已存在則獲取。）預設安全組（SecurityGroup）。
        * 每個帳戶下每個地域的每個項目的<a href="https://cloud.tencent.com/document/product/213/12453">安全組數量限制</a>。
        * 新建的安全組的入站和出站規則預設都是全部拒絕，在創建後通常您需要再調用CreateSecurityGroupPolicies将安全組的規則設置爲需要的規則。
        * 創建安全組同時可以綁定标簽, 應答裏的标簽清單代表添加成功的标簽。

        :param request: Request instance for CreateDefaultSecurityGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateDefaultSecurityGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateDefaultSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDefaultSecurityGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDefaultSecurityGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDefaultVpc(self, request):
        """本介面（CreateDefaultVpc）用于創建預設私有網絡(VPC）。

        預設VPC适用于快速入門和啓動公共實例，您可以像使用任何其他VPC一樣使用預設VPC。如果您想創建标準VPC，即指定VPC名稱、VPC網段、子網網段、子網可用區，請使用常規創建VPC介面（CreateVpc）

        正常情況，本介面并不一定生産預設VPC，而是根據用戶賬号的網絡屬性（DescribeAccountAttributes）來決定的
        * 支援基礎網絡、VPC，返回VpcId爲0
        * 只支援VPC，返回預設VPC訊息

        您也可以通過 Force 參數，強制返回預設VPC

        :param request: Request instance for CreateDefaultVpc.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateDefaultVpcRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateDefaultVpcResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDefaultVpc", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDefaultVpcResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDirectConnectGateway(self, request):
        """本介面（CreateDirectConnectGateway）用于創建專線閘道。

        :param request: Request instance for CreateDirectConnectGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateDirectConnectGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateDirectConnectGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDirectConnectGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDirectConnectGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDirectConnectGatewayCcnRoutes(self, request):
        """本介面（CreateDirectConnectGatewayCcnRoutes）用于創建專線閘道的雲聯網路由（IDC網段）

        :param request: Request instance for CreateDirectConnectGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateDirectConnectGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateDirectConnectGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDirectConnectGatewayCcnRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDirectConnectGatewayCcnRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateFlowLog(self, request):
        """本介面（CreateFlowLog）用于創建流日志

        :param request: Request instance for CreateFlowLog.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateFlowLogRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateFlowLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateFlowLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateFlowLogResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateHaVip(self, request):
        """本介面（CreateHaVip）用于創建高可用虛拟IP（HAVIP）

        :param request: Request instance for CreateHaVip.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateHaVipRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateHaVipResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateHaVip", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateHaVipResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateIp6Translators(self, request):
        """1. 該介面用于創建IPV6轉換IPV4實例，支援批次
        2. 同一個帳戶在一個地域最多允許創建10個轉換實例

        :param request: Request instance for CreateIp6Translators.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateIp6TranslatorsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateIp6TranslatorsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateIp6Translators", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateIp6TranslatorsResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """本介面(CreateNatGateway)用于創建NAT閘道。

        :param request: Request instance for CreateNatGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNatGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNatGatewayResponse`

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


    def CreateNatGatewayDestinationIpPortTranslationNatRule(self, request):
        """本介面(CreateNatGatewayDestinationIpPortTranslationNatRule)用于創建NAT閘道端口轉發規則。

        :param request: Request instance for CreateNatGatewayDestinationIpPortTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNatGatewayDestinationIpPortTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNatGatewayDestinationIpPortTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNatGatewayDestinationIpPortTranslationNatRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNatGatewayDestinationIpPortTranslationNatRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateNetDetect(self, request):
        """本介面(CreateNetDetect)用于創建網絡探測。

        :param request: Request instance for CreateNetDetect.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNetDetectRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNetDetectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNetDetect", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNetDetectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateNetworkAcl(self, request):
        """本介面（CreateNetworkAcl）用于創建新的<a href="https://cloud.tencent.com/document/product/215/20088">網絡ACL</a>。
        * 新建的網絡ACL的入站和出站規則預設都是全部拒絕，在創建後通常您需要再調用ModifyNetworkAclEntries将網絡ACL的規則設置爲需要的規則。

        :param request: Request instance for CreateNetworkAcl.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNetworkAclRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNetworkAclResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNetworkAcl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNetworkAclResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """本介面（CreateNetworkInterface）用于創建彈性網卡。
        * 創建彈性網卡時可以指定内網IP，并且可以指定一個主IP，指定的内網IP必須在彈性網卡所在子網内，而且不能被占用。
        * 創建彈性網卡時可以指定需要申請的内網IP數量，系統會随機生成内網IP網址。
        * 一個彈性網卡支援綁定的IP網址是有限制的，更多資源限制訊息詳見<a href="/document/product/576/18527">彈性網卡使用限制</a>。
        * 創建彈性網卡同時可以綁定已有安全組。
        * 創建彈性網卡同時可以綁定标簽, 應答裏的标簽清單代表添加成功的标簽。

        :param request: Request instance for CreateNetworkInterface.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNetworkInterfaceResponse`

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


    def CreateRouteTable(self, request):
        """本介面(CreateRouteTable)用于創建路由表。
        * 創建了VPC後，系統會創建一個預設路由表，所有新建的子網都會關聯到預設路由表。預設情況下您可以直接使用預設路由表來管理您的路由策略。當您的路由策略較多時，您可以調用創建路由表介面創建更多路由表管理您的路由策略。
        * 創建路由表同時可以綁定标簽, 應答裏的标簽清單代表添加成功的标簽。

        :param request: Request instance for CreateRouteTable.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateRouteTableRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateRouteTableResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateRouteTable", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRouteTableResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateRoutes(self, request):
        """本介面(CreateRoutes)用于創建路由策略。
        * 向指定路由表批次新增路由策略。

        :param request: Request instance for CreateRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSecurityGroup(self, request):
        """本介面（CreateSecurityGroup）用于創建新的安全組（SecurityGroup）。
        * 每個帳戶下每個地域的每個項目的<a href="https://cloud.tencent.com/document/product/213/12453">安全組數量限制</a>。
        * 新建的安全組的入站和出站規則預設都是全部拒絕，在創建後通常您需要再調用CreateSecurityGroupPolicies将安全組的規則設置爲需要的規則。
        * 創建安全組同時可以綁定标簽, 應答裏的标簽清單代表添加成功的标簽。

        :param request: Request instance for CreateSecurityGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateSecurityGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSecurityGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSecurityGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSecurityGroupPolicies(self, request):
        """本介面（CreateSecurityGroupPolicies）用于創建安全組規則（SecurityGroupPolicy）。

        * Version安全組規則版本号，用戶每次更新安全規則版本會自動加1，防止您更新的路由規則已過期，不填不考慮沖突。
        * Protocol欄位支援輸入TCP, UDP, ICMP, ICMPV6, GRE, ALL。
        * CidrBlock欄位允許輸入符合cidr格式标準的任意字串。(展開)在基礎網絡中，如果CidrBlock包含您的帳戶内的雲伺服器之外的設備在Top Cloud 的内網IP，并不代表此規則允許您訪問這些設備，租戶之間網絡隔離規則優先于安全組中的内網規則。
        * Ipv6CidrBlock欄位允許輸入符合IPv6 cidr格式标準的任意字串。(展開)在基礎網絡中，如果Ipv6CidrBlock包含您的帳戶内的雲伺服器之外的設備在Top Cloud 的内網IPv6，并不代表此規則允許您訪問這些設備，租戶之間網絡隔離規則優先于安全組中的内網規則。
        * SecurityGroupId欄位允許輸入與待修改的安全組位于相同項目中的安全組ID，包括這個安全組ID本身，代表安全組下所有雲伺服器的内網IP。使用這個欄位時，這條規則用來比對網絡報文的過程中會随着被使用的這個ID所關聯的雲伺服器變化而變化，不需要重新修改。
        * Port欄位允許輸入一個單獨端口号，或者用減号分隔的兩個端口号代表端口範圍，例如80或8000-8010。只有當Protocol欄位是TCP或UDP時，Port欄位才被接受，即Protocol欄位不是TCP或UDP時，Protocol和Port排他關系，不允許同時輸入，否則會介面報錯。
        * Action欄位只允許輸入ACCEPT或DROP。
        * CidrBlock, Ipv6CidrBlock, SecurityGroupId, AddressTemplate四者是排他關系，不允許同時輸入，Protocol + Port和ServiceTemplate二者是排他關系，不允許同時輸入。
        * 一次請求中只能創建單個方向的規則, 如果需要指定索引（PolicyIndex）參數, 多條規則的索引必須一緻。

        :param request: Request instance for CreateSecurityGroupPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateSecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateSecurityGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSecurityGroupPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSecurityGroupPoliciesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSecurityGroupWithPolicies(self, request):
        """本介面（CreateSecurityGroupWithPolicies）用于創建新的安全組（SecurityGroup），并且可以同時添加安全組規則（SecurityGroupPolicy）。
        * 每個帳戶下每個地域的每個項目的<a href="https://cloud.tencent.com/document/product/213/12453">安全組數量限制</a>。
        * 新建的安全組的入站和出站規則預設都是全部拒絕，在創建後通常您需要再調用CreateSecurityGroupPolicies将安全組的規則設置爲需要的規則。

        安全組規則說明：
        * Version安全組規則版本号，用戶每次更新安全規則版本會自動加1，防止您更新的路由規則已過期，不填不考慮沖突。
        * Protocol欄位支援輸入TCP, UDP, ICMP, ICMPV6, GRE, ALL。
        * CidrBlock欄位允許輸入符合cidr格式标準的任意字串。(展開)在基礎網絡中，如果CidrBlock包含您的帳戶内的雲伺服器之外的設備在Top Cloud 的内網IP，并不代表此規則允許您訪問這些設備，租戶之間網絡隔離規則優先于安全組中的内網規則。
        * Ipv6CidrBlock欄位允許輸入符合IPv6 cidr格式标準的任意字串。(展開)在基礎網絡中，如果Ipv6CidrBlock包含您的帳戶内的雲伺服器之外的設備在Top Cloud 的内網IPv6，并不代表此規則允許您訪問這些設備，租戶之間網絡隔離規則優先于安全組中的内網規則。
        * SecurityGroupId欄位允許輸入與待修改的安全組位于相同項目中的安全組ID，包括這個安全組ID本身，代表安全組下所有雲伺服器的内網IP。使用這個欄位時，這條規則用來比對網絡報文的過程中會随着被使用的這個ID所關聯的雲伺服器變化而變化，不需要重新修改。
        * Port欄位允許輸入一個單獨端口号，或者用減号分隔的兩個端口号代表端口範圍，例如80或8000-8010。只有當Protocol欄位是TCP或UDP時，Port欄位才被接受，即Protocol欄位不是TCP或UDP時，Protocol和Port排他關系，不允許同時輸入，否則會介面報錯。
        * Action欄位只允許輸入ACCEPT或DROP。
        * CidrBlock, Ipv6CidrBlock, SecurityGroupId, AddressTemplate四者是排他關系，不允許同時輸入，Protocol + Port和ServiceTemplate二者是排他關系，不允許同時輸入。
        * 一次請求中只能創建單個方向的規則, 如果需要指定索引（PolicyIndex）參數, 多條規則的索引必須一緻。

        :param request: Request instance for CreateSecurityGroupWithPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateSecurityGroupWithPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateSecurityGroupWithPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSecurityGroupWithPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSecurityGroupWithPoliciesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateServiceTemplate(self, request):
        """本介面（CreateServiceTemplate）用于創建協議端口範本

        :param request: Request instance for CreateServiceTemplate.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateServiceTemplateRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateServiceTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateServiceTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateServiceTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateServiceTemplateGroup(self, request):
        """本介面（CreateServiceTemplateGroup）用于創建協議端口範本集合

        :param request: Request instance for CreateServiceTemplateGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateServiceTemplateGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateServiceTemplateGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateServiceTemplateGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateServiceTemplateGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """本介面(CreateSubnet)用于創建子網。
        * 創建子網前必須創建好 VPC。
        * 子網創建成功後，子網網段不能修改。子網網段必須在VPC網段内，可以和VPC網段相同（VPC有且只有一個子網時），建議子網網段在VPC網段内，預留網段給其他子網使用。
        * 您可以創建的最小網段子網掩碼爲28（有16個IP網址），最大網段子網掩碼爲16（65,536個IP網址）。
        * 同一個VPC内，多個子網的網段不能重疊。
        * 子網創建後會自動關聯到預設路由表。
        * 創建子網同時可以綁定标簽, 應答裏的标簽清單代表添加成功的标簽。

        :param request: Request instance for CreateSubnet.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateSubnetRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateSubnetResponse`

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


    def CreateSubnets(self, request):
        """本介面(CreateSubnets)用于批次創建子網。
        * 創建子網前必須創建好 VPC。
        * 子網創建成功後，子網網段不能修改。子網網段必須在VPC網段内，可以和VPC網段相同（VPC有且只有一個子網時），建議子網網段在VPC網段内，預留網段給其他子網使用。
        * 您可以創建的最小網段子網掩碼爲28（有16個IP網址），最大網段子網掩碼爲16（65,536個IP網址）。
        * 同一個VPC内，多個子網的網段不能重疊。
        * 子網創建後會自動關聯到預設路由表。
        * 創建子網同時可以綁定标簽, 應答裏的标簽清單代表添加成功的标簽。

        :param request: Request instance for CreateSubnets.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateSubnetsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateSubnetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSubnets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSubnetsResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """本介面(CreateVpc)用于創建私有網絡(VPC)。
        * 用戶可以創建的最小網段子網掩碼爲28（有16個IP網址），最大網段子網掩碼爲16（65,536個IP網址）,如果規劃VPC網段請參見VPC網段規劃說明。
        * 同一個地域能創建的VPC資源個數也是有限制的，詳見 <a href="https://cloud.tencent.com/doc/product/215/537" title="VPC使用限制">VPC使用限制</a>,如果需要擴充請聯系在線客服。
        * 創建VPC同時可以綁定标簽, 應答裏的标簽清單代表添加成功的标簽。

        :param request: Request instance for CreateVpc.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpcRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpcResponse`

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


    def CreateVpnConnection(self, request):
        """本介面（CreateVpnConnection）用于創建VPN通道。

        :param request: Request instance for CreateVpnConnection.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpnConnectionRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpnConnectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateVpnConnection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVpnConnectionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVpnGateway(self, request):
        """本介面（CreateVpnGateway）用于創建VPN閘道。

        :param request: Request instance for CreateVpnGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpnGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpnGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateVpnGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVpnGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAddressTemplate(self, request):
        """本介面（DeleteAddressTemplate）用于删除IP網址範本

        :param request: Request instance for DeleteAddressTemplate.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteAddressTemplateRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteAddressTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAddressTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAddressTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAddressTemplateGroup(self, request):
        """本介面（DeleteAddressTemplateGroup）用于删除IP網址範本集合

        :param request: Request instance for DeleteAddressTemplateGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteAddressTemplateGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteAddressTemplateGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAddressTemplateGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAddressTemplateGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAssistantCidr(self, request):
        """本介面(DeleteAssistantCidr)用于删除輔助CIDR。（介面灰度中，如需使用請提工單。）

        :param request: Request instance for DeleteAssistantCidr.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteAssistantCidrRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteAssistantCidrResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAssistantCidr", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAssistantCidrResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteBandwidthPackage(self, request):
        """介面支援删除共享頻寬包，包括[設備頻寬包](https://cloud.tencent.com/document/product/684/15246#.E8.AE.BE.E5.A4.87.E5.B8.A6.E5.AE.BD.E5.8C.85)和[IP頻寬包](https://cloud.tencent.com/document/product/684/15246#ip-.E5.B8.A6.E5.AE.BD.E5.8C.85)

        :param request: Request instance for DeleteBandwidthPackage.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteBandwidthPackageRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteBandwidthPackageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteBandwidthPackage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteBandwidthPackageResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteCcn(self, request):
        """本介面（DeleteCcn）用于删除雲聯網。
        * 删除後，雲聯閘道聯的所有實例間路由将被删除，網絡将會中斷，請務必确認
        * 删除雲聯網是不可逆的操作，請謹慎處理。

        :param request: Request instance for DeleteCcn.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteCcnRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteCcnResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCcn", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCcnResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteCustomerGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteCustomerGatewayResponse`

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


    def DeleteDirectConnectGateway(self, request):
        """本介面（DeleteDirectConnectGateway）用于删除專線閘道。
        <li>如果是 NAT 閘道，删除專線閘道後，NAT 規則以及 ACL 策略都被清理了。</li>
        <li>删除專線閘道後，系統會删除路由表中跟該專線閘道相關的路由策略。</li>
        本介面是異步完成，如需查詢異步任務執行結果，請使用本介面返回的`RequestId`輪詢`QueryTask`介面

        :param request: Request instance for DeleteDirectConnectGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteDirectConnectGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteDirectConnectGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDirectConnectGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDirectConnectGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteDirectConnectGatewayCcnRoutes(self, request):
        """本介面（DeleteDirectConnectGatewayCcnRoutes）用于删除專線閘道的雲聯網路由（IDC網段）

        :param request: Request instance for DeleteDirectConnectGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteDirectConnectGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteDirectConnectGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDirectConnectGatewayCcnRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDirectConnectGatewayCcnRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteFlowLog(self, request):
        """本介面（DeleteFlowLog）用于删除流日志

        :param request: Request instance for DeleteFlowLog.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteFlowLogRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteFlowLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteFlowLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteFlowLogResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteHaVip(self, request):
        """本介面（DeleteHaVip）用于删除高可用虛拟IP（HAVIP）<br />
        本介面是異步完成，如需查詢異步任務執行結果，請使用本介面返回的`RequestId`輪詢`QueryTask`介面

        :param request: Request instance for DeleteHaVip.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteHaVipRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteHaVipResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteHaVip", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteHaVipResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteIp6Translators(self, request):
        """1. 該介面用于釋放IPV6轉換實例，支援批次。
        2.  如果IPV6轉換實例建立有轉換規則，會一并删除。

        :param request: Request instance for DeleteIp6Translators.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteIp6TranslatorsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteIp6TranslatorsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteIp6Translators", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteIp6TranslatorsResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """本介面（DeleteNatGateway）用于删除NAT閘道。
        删除 NAT 閘道後，系統會自動删除路由表中包含此 NAT 閘道的路由項，同時也會解綁彈性公網IP（EIP）。

        :param request: Request instance for DeleteNatGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNatGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNatGatewayResponse`

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


    def DeleteNatGatewayDestinationIpPortTranslationNatRule(self, request):
        """本介面（DeleteNatGatewayDestinationIpPortTranslationNatRule）用于删除NAT閘道端口轉發規則。

        :param request: Request instance for DeleteNatGatewayDestinationIpPortTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNatGatewayDestinationIpPortTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNatGatewayDestinationIpPortTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNatGatewayDestinationIpPortTranslationNatRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNatGatewayDestinationIpPortTranslationNatRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteNetDetect(self, request):
        """本介面(DeleteNetDetect)用于删除網絡探測實例。

        :param request: Request instance for DeleteNetDetect.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNetDetectRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNetDetectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNetDetect", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNetDetectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteNetworkAcl(self, request):
        """本介面（DeleteNetworkAcl）用于删除網絡ACL。

        :param request: Request instance for DeleteNetworkAcl.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNetworkAclRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNetworkAclResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNetworkAcl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNetworkAclResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """本介面（DeleteNetworkInterface）用于删除彈性網卡。
        * 彈性網卡上綁定了雲伺服器時，不能被删除。
        * 删除指定彈性網卡，彈性網卡必須先和子機解綁才能删除。删除之後彈性網卡上所有内網IP都将被退還。

        :param request: Request instance for DeleteNetworkInterface.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNetworkInterfaceResponse`

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


    def DeleteRouteTable(self, request):
        """删除路由表

        :param request: Request instance for DeleteRouteTable.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteRouteTableRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteRouteTableResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteRouteTable", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRouteTableResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteRoutes(self, request):
        """本介面(DeleteRoutes)用于對某個路由表批次删除路由策略（Route）。

        :param request: Request instance for DeleteRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSecurityGroup(self, request):
        """本介面（DeleteSecurityGroup）用于删除安全組（SecurityGroup）。
        * 只有當前賬号下的安全組允許被删除。
        * 安全組實例ID如果在其他安全組的規則中被引用，則無法直接删除。這種情況下，需要先進行規則修改，再删除安全組。
        * 删除的安全組無法再找回，請謹慎調用。

        :param request: Request instance for DeleteSecurityGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteSecurityGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSecurityGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSecurityGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSecurityGroupPolicies(self, request):
        """本介面（DeleteSecurityGroupPolicies）用于用于删除安全組規則（SecurityGroupPolicy）。
        * SecurityGroupPolicySet.Version 用于指定要操作的安全組的版本。傳入 Version 版本号若不等于當前安全組的最新版本，将返回失敗；若不傳 Version 則直接删除指定PolicyIndex的規則。

        :param request: Request instance for DeleteSecurityGroupPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteSecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteSecurityGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSecurityGroupPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSecurityGroupPoliciesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteServiceTemplate(self, request):
        """本介面（DeleteServiceTemplate）用于删除協議端口範本

        :param request: Request instance for DeleteServiceTemplate.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteServiceTemplateRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteServiceTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteServiceTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteServiceTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteServiceTemplateGroup(self, request):
        """本介面（DeleteServiceTemplateGroup）用于删除協議端口範本集合

        :param request: Request instance for DeleteServiceTemplateGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteServiceTemplateGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteServiceTemplateGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteServiceTemplateGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteServiceTemplateGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """本介面（DeleteSubnet）用于用于删除子網(Subnet)。
        * 删除子網前，請清理該子網下所有資源，包括雲伺服器、負載均衡、雲數據、noSql、彈性網卡等資源。

        :param request: Request instance for DeleteSubnet.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteSubnetRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteSubnetResponse`

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
        """本介面（DeleteVpc）用于删除私有網絡。
        * 删除前請确保 VPC 内已經沒有相關資源，例如雲伺服器、雲資料庫、NoSQL、VPN閘道、專線閘道、負載均衡、對等連接、與之互通的基礎網絡設備等。
        * 删除私有網絡是不可逆的操作，請謹慎處理。

        :param request: Request instance for DeleteVpc.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpcRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpcResponse`

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


    def DeleteVpnConnection(self, request):
        """本介面(DeleteVpnConnection)用于删除VPN通道。

        :param request: Request instance for DeleteVpnConnection.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnConnectionRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnConnectionResponse`

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
        """本介面（DeleteVpnGateway）用于删除VPN閘道。目前只支援删除運作中的按量計費的IPSEC閘道實例。

        :param request: Request instance for DeleteVpnGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnGatewayResponse`

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


    def DescribeAccountAttributes(self, request):
        """本介面（DescribeAccountAttributes）用于查詢用戶賬号私有屬性。

        :param request: Request instance for DescribeAccountAttributes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAccountAttributesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAccountAttributesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccountAttributes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountAttributesResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """本介面 (DescribeAddressQuota) 用于查詢您帳戶的[彈性公網IP](https://cloud.tencent.com/document/product/213/1941)（簡稱 EIP）在當前地域的配額訊息。配額詳情可參見 [EIP 産品簡介](https://cloud.tencent.com/document/product/213/5733)。

        :param request: Request instance for DescribeAddressQuota.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressQuotaRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressQuotaResponse`

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


    def DescribeAddressTemplateGroups(self, request):
        """本介面（DescribeAddressTemplateGroups）用于查詢IP網址範本集合

        :param request: Request instance for DescribeAddressTemplateGroups.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressTemplateGroupsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressTemplateGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAddressTemplateGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAddressTemplateGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAddressTemplates(self, request):
        """本介面（DescribeAddressTemplates）用于查詢IP網址範本

        :param request: Request instance for DescribeAddressTemplates.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressTemplatesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAddressTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAddressTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """本介面 (DescribeAddresses) 用于查詢一個或多個[彈性公網IP](https://cloud.tencent.com/document/product/213/1941)（簡稱 EIP）的詳細訊息。
        * 如果參數爲空，返回當前用戶一定數量（Limit所指定的數量，預設爲20）的 EIP。

        :param request: Request instance for DescribeAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressesResponse`

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


    def DescribeAssistantCidr(self, request):
        """本介面（DescribeAssistantCidr）用于查詢輔助CIDR清單。（介面灰度中，如需使用請提工單。）

        :param request: Request instance for DescribeAssistantCidr.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAssistantCidrRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAssistantCidrResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssistantCidr", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssistantCidrResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBandwidthPackageQuota(self, request):
        """介面用于查詢帳戶在當前地域的頻寬包上限數量以及使用數量

        :param request: Request instance for DescribeBandwidthPackageQuota.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackageQuotaRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackageQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBandwidthPackageQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBandwidthPackageQuotaResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBandwidthPackages(self, request):
        """介面用于查詢頻寬包詳細訊息，包括頻寬包唯一标識ID，類型，計費模式，名稱，資源訊息等

        :param request: Request instance for DescribeBandwidthPackages.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackagesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackagesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBandwidthPackages", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBandwidthPackagesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCcnAttachedInstances(self, request):
        """本介面（DescribeCcnAttachedInstances）用于查詢雲聯網實例下已關聯的網絡實例。

        :param request: Request instance for DescribeCcnAttachedInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnAttachedInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnAttachedInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCcnAttachedInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCcnAttachedInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCcnRegionBandwidthLimits(self, request):
        """本介面（DescribeCcnRegionBandwidthLimits）用于查詢雲聯網各地域出頻寬上限，該介面只返回已關聯網絡實例包含的地域

        :param request: Request instance for DescribeCcnRegionBandwidthLimits.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnRegionBandwidthLimitsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnRegionBandwidthLimitsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCcnRegionBandwidthLimits", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCcnRegionBandwidthLimitsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCcnRoutes(self, request):
        """本介面（DescribeCcnRoutes）用于查詢已加入雲聯網（CCN）的路由

        :param request: Request instance for DescribeCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCcnRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCcnRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCcns(self, request):
        """本介面（DescribeCcns）用于查詢雲聯網（CCN）清單。

        :param request: Request instance for DescribeCcns.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCcns", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCcnsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClassicLinkInstances(self, request):
        """本介面(DescribeClassicLinkInstances)用于查詢私有網絡和基礎網絡設備互通清單。

        :param request: Request instance for DescribeClassicLinkInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeClassicLinkInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeClassicLinkInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClassicLinkInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClassicLinkInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCustomerGatewayVendors(self, request):
        """本介面（DescribeCustomerGatewayVendors）用于查詢可支援的對端閘道廠商訊息。

        :param request: Request instance for DescribeCustomerGatewayVendors.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCustomerGatewayVendorsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCustomerGatewayVendorsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCustomerGatewayVendors", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCustomerGatewayVendorsResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCustomerGatewaysRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCustomerGatewaysResponse`

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


    def DescribeDirectConnectGatewayCcnRoutes(self, request):
        """本介面（DescribeDirectConnectGatewayCcnRoutes）用于查詢專線閘道的雲聯網路由（IDC網段）

        :param request: Request instance for DescribeDirectConnectGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeDirectConnectGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeDirectConnectGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDirectConnectGatewayCcnRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDirectConnectGatewayCcnRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDirectConnectGateways(self, request):
        """本介面（DescribeDirectConnectGateways）用于查詢專線閘道。

        :param request: Request instance for DescribeDirectConnectGateways.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeDirectConnectGatewaysRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeDirectConnectGatewaysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDirectConnectGateways", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDirectConnectGatewaysResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFlowLog(self, request):
        """本介面（DescribeFlowLog）用于查詢流日志實例訊息

        :param request: Request instance for DescribeFlowLog.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeFlowLogRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeFlowLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFlowLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFlowLogResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFlowLogs(self, request):
        """本介面（DescribeFlowLogs）用于查詢獲取流日志集合

        :param request: Request instance for DescribeFlowLogs.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeFlowLogsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeFlowLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFlowLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFlowLogsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGatewayFlowMonitorDetail(self, request):
        """本介面（DescribeGatewayFlowMonitorDetail）用于查詢閘道流量監控明細。
        * 只支援單個閘道實例查詢。即入參 `VpnId` `DirectConnectGatewayId` `PeeringConnectionId` `NatId` 最多只支援傳一個，且必須傳一個。
        * 如果閘道有流量，但調用本介面沒有返回數據，請在控制台對應閘道詳情頁确認是否開啓閘道流量監控。

        :param request: Request instance for DescribeGatewayFlowMonitorDetail.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeGatewayFlowMonitorDetailRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeGatewayFlowMonitorDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGatewayFlowMonitorDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGatewayFlowMonitorDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGatewayFlowQos(self, request):
        """本介面（DescribeGatewayFlowQos）用于查詢閘道來訪IP流控頻寬。

        :param request: Request instance for DescribeGatewayFlowQos.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeGatewayFlowQosRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeGatewayFlowQosResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGatewayFlowQos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGatewayFlowQosResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeHaVips(self, request):
        """本介面（DescribeHaVips）用于查詢高可用虛拟IP（HAVIP）清單。

        :param request: Request instance for DescribeHaVips.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeHaVipsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeHaVipsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeHaVips", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeHaVipsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIp6Addresses(self, request):
        """該介面用于查詢IPV6網址訊息

        :param request: Request instance for DescribeIp6Addresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeIp6AddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeIp6AddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIp6Addresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIp6AddressesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIp6TranslatorQuota(self, request):
        """查詢帳戶在指定地域IPV6轉換實例和規則的配額

        :param request: Request instance for DescribeIp6TranslatorQuota.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeIp6TranslatorQuotaRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeIp6TranslatorQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIp6TranslatorQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIp6TranslatorQuotaResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIp6Translators(self, request):
        """1. 該介面用于查詢帳戶下的IPV6轉換實例及其綁定的轉換規則訊息
        2. 支援過濾查詢

        :param request: Request instance for DescribeIp6Translators.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeIp6TranslatorsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeIp6TranslatorsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIp6Translators", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIp6TranslatorsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNatGatewayDestinationIpPortTranslationNatRules(self, request):
        """本介面（DescribeNatGatewayDestinationIpPortTranslationNatRules）用于查詢NAT閘道端口轉發規則對象數組。

        :param request: Request instance for DescribeNatGatewayDestinationIpPortTranslationNatRules.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewayDestinationIpPortTranslationNatRulesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewayDestinationIpPortTranslationNatRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNatGatewayDestinationIpPortTranslationNatRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNatGatewayDestinationIpPortTranslationNatRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """本介面（DescribeNatGateways）用于查詢 NAT 閘道。

        :param request: Request instance for DescribeNatGateways.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewaysRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewaysResponse`

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


    def DescribeNetDetectStates(self, request):
        """本介面(DescribeNetDetectStates)用于查詢網絡探測驗證結果清單。

        :param request: Request instance for DescribeNetDetectStates.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetDetectStatesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetDetectStatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNetDetectStates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNetDetectStatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNetDetects(self, request):
        """本介面（DescribeNetDetects）用于查詢網絡探測清單。

        :param request: Request instance for DescribeNetDetects.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetDetectsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetDetectsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNetDetects", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNetDetectsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNetworkAcls(self, request):
        """本介面（DescribeNetworkAcls）用于查詢網絡ACL清單。

        :param request: Request instance for DescribeNetworkAcls.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkAclsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkAclsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNetworkAcls", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNetworkAclsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNetworkInterfaceLimit(self, request):
        """本介面（DescribeNetworkInterfaceLimit）根據CVM實例ID或彈性網卡ID查詢彈性網卡配額，返回該CVM實例或彈性網卡能綁定的彈性網卡配額，以及彈性網卡可以分配的IP配額

        :param request: Request instance for DescribeNetworkInterfaceLimit.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkInterfaceLimitRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkInterfaceLimitResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNetworkInterfaceLimit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNetworkInterfaceLimitResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """本介面（DescribeNetworkInterfaces）用于查詢彈性網卡清單。

        :param request: Request instance for DescribeNetworkInterfaces.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkInterfacesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkInterfacesResponse`

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


    def DescribeRouteConflicts(self, request):
        """本介面（DescribeRouteConflicts）用于查詢自定義路由策略與雲聯網路由策略沖突清單

        :param request: Request instance for DescribeRouteConflicts.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeRouteConflictsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeRouteConflictsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRouteConflicts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRouteConflictsResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeRouteTablesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeRouteTablesResponse`

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


    def DescribeSecurityGroupAssociationStatistics(self, request):
        """本介面（DescribeSecurityGroupAssociationStatistics）用于查詢安全組關聯的實例統計。

        :param request: Request instance for DescribeSecurityGroupAssociationStatistics.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupAssociationStatisticsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupAssociationStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecurityGroupAssociationStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityGroupAssociationStatisticsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecurityGroupLimits(self, request):
        """本介面(DescribeSecurityGroupLimits)用于查詢用戶安全組配額。

        :param request: Request instance for DescribeSecurityGroupLimits.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupLimitsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupLimitsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecurityGroupLimits", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityGroupLimitsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecurityGroupPolicies(self, request):
        """本介面（DescribeSecurityGroupPolicies）用于查詢安全組規則。

        :param request: Request instance for DescribeSecurityGroupPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecurityGroupPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityGroupPoliciesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecurityGroupReferences(self, request):
        """本介面（DescribeSecurityGroupReferences）用于查詢安全組被引用訊息。

        :param request: Request instance for DescribeSecurityGroupReferences.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupReferencesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupReferencesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecurityGroupReferences", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityGroupReferencesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecurityGroups(self, request):
        """本介面（DescribeSecurityGroups）用于查詢安全組。

        :param request: Request instance for DescribeSecurityGroups.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeServiceTemplateGroups(self, request):
        """本介面（DescribeServiceTemplateGroups）用于查詢協議端口範本集合

        :param request: Request instance for DescribeServiceTemplateGroups.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeServiceTemplateGroupsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeServiceTemplateGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeServiceTemplateGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeServiceTemplateGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeServiceTemplates(self, request):
        """本介面（DescribeServiceTemplates）用于查詢協議端口範本

        :param request: Request instance for DescribeServiceTemplates.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeServiceTemplatesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeServiceTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeServiceTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeServiceTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """本介面（DescribeSubnets）用于查詢子網清單。

        :param request: Request instance for DescribeSubnets.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSubnetsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSubnetsResponse`

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
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeTaskResultRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeTaskResultResponse`

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


    def DescribeTemplateLimits(self, request):
        """本介面（DescribeTemplateLimits）用于查詢參數範本配額清單。

        :param request: Request instance for DescribeTemplateLimits.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeTemplateLimitsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeTemplateLimitsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTemplateLimits", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTemplateLimitsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVpcInstances(self, request):
        """本介面（DescribeVpcInstances）用于查詢VPC下的雲主機實例清單。

        :param request: Request instance for DescribeVpcInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpcInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpcInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVpcIpv6Addresses(self, request):
        """本介面（DescribeVpcIpv6Addresses）用于查詢 `VPC` `IPv6` 訊息。
        只能查詢已使用的`IPv6`訊息，當查詢未使用的IP時，本介面不會報錯，但不會出現在返回結果裏。

        :param request: Request instance for DescribeVpcIpv6Addresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcIpv6AddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcIpv6AddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpcIpv6Addresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpcIpv6AddressesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVpcLimits(self, request):
        """獲取私有網絡配額，部分私有網絡的配額有地域屬性。
        LimitTypes取值範圍：
        * appid-max-vpcs （每個開發商每個地域可創建的VPC數）
        * vpc-max-subnets（每個VPC可創建的子網數）
        * vpc-max-route-tables（每個VPC可創建的路由表數）
        * route-table-max-policies（每個路由表可添加的策略數）
        * vpc-max-vpn-gateways（每個VPC可創建的VPN閘道數）
        * appid-max-custom-gateways（每個開發商可創建的對端閘道數）
        * appid-max-vpn-connections（每個開發商可創建的VPN通道數）
        * custom-gateway-max-vpn-connections（每個對端閘道可創建的VPN通道數）
        * vpn-gateway-max-custom-gateways（每個VPNGW可以創建的通道數）
        * vpc-max-network-acls（每個VPC可創建的網絡ACL數）
        * network-acl-max-inbound-policies（每個網絡ACL可添加的入站規則數）
        * network-acl-max-outbound-policies（每個網絡ACL可添加的出站規則數）
        * vpc-max-vpcpeers（每個VPC可創建的對等連接數）
        * vpc-max-available-vpcpeers（每個VPC可創建的有效對等連接數）
        * vpc-max-basic-network-interconnections（每個VPC可創建的基礎網絡雲主機與VPC互通數）
        * direct-connection-max-snats（每個專線閘道可創建的SNAT數）
        * direct-connection-max-dnats（每個專線閘道可創建的DNAT數）
        * direct-connection-max-snapts（每個專線閘道可創建的SNAPT數）
        * direct-connection-max-dnapts（每個專線閘道可創建的DNAPT數）
        * vpc-max-nat-gateways（每個VPC可創建的NAT閘道數）
        * nat-gateway-max-eips（每個NAT可以購買的外網IP數量）
        * vpc-max-enis（每個VPC可創建彈性網卡數）
        * vpc-max-havips（每個VPC可創建HAVIP數）
        * eni-max-private-ips（每個ENI可以綁定的内網IP數（ENI未綁定子機））
        * nat-gateway-max-dnapts（每個NAT閘道可創建的DNAPT數）
        * vpc-max-ipv6s（每個VPC可分配的IPv6網址數）
        * eni-max-ipv6s（每個ENI可分配的IPv6網址數）
        * vpc-max-assistant_cidrs（每個VPC可分配的輔助CIDR數）

        :param request: Request instance for DescribeVpcLimits.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcLimitsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcLimitsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpcLimits", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpcLimitsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVpcPrivateIpAddresses(self, request):
        """本介面（DescribeVpcPrivateIpAddresses）用于查詢VPC内網IP訊息。<br />
        只能查詢已使用的IP訊息，當查詢未使用的IP時，本介面不會報錯，但不會出現在返回結果裏。

        :param request: Request instance for DescribeVpcPrivateIpAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcPrivateIpAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcPrivateIpAddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpcPrivateIpAddresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpcPrivateIpAddressesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVpcResourceDashboard(self, request):
        """本介面(DescribeVpcResourceDashboard)用于檢視VPC資源訊息。

        :param request: Request instance for DescribeVpcResourceDashboard.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcResourceDashboardRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcResourceDashboardResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpcResourceDashboard", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpcResourceDashboardResponse()
                model._deserialize(response["Response"])
                return model
            else:
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

        :param request: Request instance for DescribeVpcs.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcsResponse`

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
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnConnectionsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnConnectionsResponse`

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


    def DescribeVpnGatewayCcnRoutes(self, request):
        """本介面（DescribeVpnGatewayCcnRoutes）用于查詢VPN閘道雲聯網路由

        :param request: Request instance for DescribeVpnGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpnGatewayCcnRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpnGatewayCcnRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewaysRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewaysResponse`

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


    def DetachCcnInstances(self, request):
        """本介面（DetachCcnInstances）用于從雲聯網實例中解關聯指定的網絡實例。<br />
        解關聯網絡實例後，相應的路由策略會一并删除。

        :param request: Request instance for DetachCcnInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DetachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DetachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachCcnInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachCcnInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DetachClassicLinkVpc(self, request):
        """本介面(DetachClassicLinkVpc)用于删除私有網絡和基礎網絡設備互通。

        :param request: Request instance for DetachClassicLinkVpc.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DetachClassicLinkVpcRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DetachClassicLinkVpcResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachClassicLinkVpc", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachClassicLinkVpcResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """本介面（DetachNetworkInterface）用于彈性網卡解綁雲主機。

        :param request: Request instance for DetachNetworkInterface.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DetachNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DetachNetworkInterfaceResponse`

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


    def DisableCcnRoutes(self, request):
        """本介面（DisableCcnRoutes）用于禁用已經啓用的雲聯網（CCN）路由

        :param request: Request instance for DisableCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisableCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisableCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableCcnRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableCcnRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisableGatewayFlowMonitor(self, request):
        """本介面（DisableGatewayFlowMonitor）用于關閉閘道流量監控。

        :param request: Request instance for DisableGatewayFlowMonitor.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisableGatewayFlowMonitorRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisableGatewayFlowMonitorResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableGatewayFlowMonitor", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableGatewayFlowMonitorResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisableRoutes(self, request):
        """本介面（DisableRoutes）用于禁用已啓用的子網路由

        :param request: Request instance for DisableRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisableRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisableRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """本介面 (DisassociateAddress) 用于解綁[彈性公網IP](https://cloud.tencent.com/document/product/213/1941)（簡稱 EIP）。
        * 支援CVM實例，彈性網卡上的EIP解綁
        * 不支援NAT上的EIP解綁。NAT上的EIP解綁請參考[EipUnBindNatGateway](https://cloud.tencent.com/document/product/215/4092)
        * 只有狀态爲 BIND 和 BIND_ENI 的 EIP 才能進行解綁定操作。
        * EIP 如果被封堵，則不能進行解綁定操作。

        :param request: Request instance for DisassociateAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisassociateAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisassociateAddressResponse`

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


    def DisassociateNatGatewayAddress(self, request):
        """本介面（DisassociateNatGatewayAddress）用于NAT閘道解綁彈性IP。

        :param request: Request instance for DisassociateNatGatewayAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisassociateNatGatewayAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisassociateNatGatewayAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisassociateNatGatewayAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateNatGatewayAddressResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisassociateNetworkAclSubnets(self, request):
        """本介面（DisassociateNetworkAclSubnets）用于網絡ACL解關聯vpc下的子網。

        :param request: Request instance for DisassociateNetworkAclSubnets.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisassociateNetworkAclSubnetsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisassociateNetworkAclSubnetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisassociateNetworkAclSubnets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateNetworkAclSubnetsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisassociateNetworkInterfaceSecurityGroups(self, request):
        """本介面（DisassociateNetworkInterfaceSecurityGroups）用于彈性網卡解綁安全組。支援彈性網卡完全解綁安全組。

        :param request: Request instance for DisassociateNetworkInterfaceSecurityGroups.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisassociateNetworkInterfaceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisassociateNetworkInterfaceSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisassociateNetworkInterfaceSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateNetworkInterfaceSecurityGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        :type request: :class:`tencentcloud.vpc.v20170312.models.DownloadCustomerGatewayConfigurationRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DownloadCustomerGatewayConfigurationResponse`

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


    def EnableCcnRoutes(self, request):
        """本介面（EnableCcnRoutes）用于啓用已經加入雲聯網（CCN）的路由。<br />
        本介面會校驗啓用後，是否與已有路由沖突，如果沖突，則無法啓用，失敗處理。路由沖突時，需要先禁用與之沖突的路由，才能啓用該路由。

        :param request: Request instance for EnableCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.EnableCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.EnableCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableCcnRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableCcnRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnableGatewayFlowMonitor(self, request):
        """本介面（EnableGatewayFlowMonitor）用于開啓閘道流量監控。

        :param request: Request instance for EnableGatewayFlowMonitor.
        :type request: :class:`tencentcloud.vpc.v20170312.models.EnableGatewayFlowMonitorRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.EnableGatewayFlowMonitorResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableGatewayFlowMonitor", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableGatewayFlowMonitorResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnableRoutes(self, request):
        """本介面（EnableRoutes）用于啓用已禁用的子網路由。<br />
        本介面會校驗啓用後，是否與已有路由沖突，如果沖突，則無法啓用，失敗處理。路由沖突時，需要先禁用與之沖突的路由，才能啓用該路由。

        :param request: Request instance for EnableRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.EnableRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.EnableRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def HaVipAssociateAddressIp(self, request):
        """本介面（HaVipAssociateAddressIp）用于高可用虛拟IP（HAVIP）綁定彈性公網IP（EIP）<br />
        本介面是異步完成，如需查詢異步任務執行結果，請使用本介面返回的`RequestId`輪詢`QueryTask`介面

        :param request: Request instance for HaVipAssociateAddressIp.
        :type request: :class:`tencentcloud.vpc.v20170312.models.HaVipAssociateAddressIpRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.HaVipAssociateAddressIpResponse`

        """
        try:
            params = request._serialize()
            body = self.call("HaVipAssociateAddressIp", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.HaVipAssociateAddressIpResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def HaVipDisassociateAddressIp(self, request):
        """本介面（HaVipDisassociateAddressIp）用于将高可用虛拟IP（HAVIP）已綁定的彈性公網IP（EIP）解除綁定<br />
        本介面是異步完成，如需查詢異步任務執行結果，請使用本介面返回的`RequestId`輪詢`QueryTask`介面

        :param request: Request instance for HaVipDisassociateAddressIp.
        :type request: :class:`tencentcloud.vpc.v20170312.models.HaVipDisassociateAddressIpRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.HaVipDisassociateAddressIpResponse`

        """
        try:
            params = request._serialize()
            body = self.call("HaVipDisassociateAddressIp", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.HaVipDisassociateAddressIpResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryPriceCreateVpnGateway(self, request):
        """本介面（InquiryPriceCreateVpnGateway）用于創建VPN閘道詢價。

        :param request: Request instance for InquiryPriceCreateVpnGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceCreateVpnGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceCreateVpnGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceCreateVpnGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceCreateVpnGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryPriceRenewVpnGateway(self, request):
        """本介面（InquiryPriceRenewVpnGateway）用于續約VPN閘道詢價。目前僅支援IPSEC類型閘道的詢價。

        :param request: Request instance for InquiryPriceRenewVpnGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceRenewVpnGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceRenewVpnGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceRenewVpnGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceRenewVpnGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryPriceResetVpnGatewayInternetMaxBandwidth(self, request):
        """本介面（InquiryPriceResetVpnGatewayInternetMaxBandwidth）調整VPN閘道頻寬上限詢價。

        :param request: Request instance for InquiryPriceResetVpnGatewayInternetMaxBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceResetVpnGatewayInternetMaxBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceResetVpnGatewayInternetMaxBandwidthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceResetVpnGatewayInternetMaxBandwidth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceResetVpnGatewayInternetMaxBandwidthResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """本介面（MigrateNetworkInterface）用于彈性網卡遷移。

        :param request: Request instance for MigrateNetworkInterface.
        :type request: :class:`tencentcloud.vpc.v20170312.models.MigrateNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.MigrateNetworkInterfaceResponse`

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
        """本介面（MigratePrivateIpAddress）用于彈性網卡内網IP遷移。

        * 該介面用于将一個内網IP從一個彈性網卡上遷移到另外一個彈性網卡，主IP網址不支援遷移。
        * 遷移前後的彈性網卡必須在同一個子網内。

        :param request: Request instance for MigratePrivateIpAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.MigratePrivateIpAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.MigratePrivateIpAddressResponse`

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
        """本介面 (ModifyAddressAttribute) 用于修改[彈性公網IP](https://cloud.tencent.com/document/product/213/1941)（簡稱 EIP）的名稱。

        :param request: Request instance for ModifyAddressAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressAttributeResponse`

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


    def ModifyAddressInternetChargeType(self, request):
        """該介面用于調整具有頻寬屬性彈性公網IP的網絡計費模式
        * 支援BANDWIDTH_PREPAID_BY_MONTH和TRAFFIC_POSTPAID_BY_HOUR兩種網絡計費模式之間的切換。
        * 每個彈性公網IP支援調整兩次，次數超出則無法調整。

        :param request: Request instance for ModifyAddressInternetChargeType.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressInternetChargeTypeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressInternetChargeTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAddressInternetChargeType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAddressInternetChargeTypeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAddressTemplateAttribute(self, request):
        """本介面（ModifyAddressTemplateAttribute）用于修改IP網址範本

        :param request: Request instance for ModifyAddressTemplateAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressTemplateAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressTemplateAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAddressTemplateAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAddressTemplateAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAddressTemplateGroupAttribute(self, request):
        """本介面（ModifyAddressTemplateGroupAttribute）用于修改IP網址範本集合

        :param request: Request instance for ModifyAddressTemplateGroupAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressTemplateGroupAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressTemplateGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAddressTemplateGroupAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAddressTemplateGroupAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """本介面（ModifyAddressesBandwidth）用于調整[彈性公網IP](https://cloud.tencent.com/document/product/213/1941)(簡稱EIP)頻寬，包括後付費EIP, 預付費EIP和頻寬包EIP

        :param request: Request instance for ModifyAddressesBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressesBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressesBandwidthResponse`

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


    def ModifyAssistantCidr(self, request):
        """本介面(ModifyAssistantCidr)用于批次修改輔助CIDR，支援新增和删除。（介面灰度中，如需使用請提工單。）

        :param request: Request instance for ModifyAssistantCidr.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAssistantCidrRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAssistantCidrResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAssistantCidr", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAssistantCidrResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyBandwidthPackageAttribute(self, request):
        """介面用于修改頻寬包屬性，包括頻寬包名字等

        :param request: Request instance for ModifyBandwidthPackageAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyBandwidthPackageAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyBandwidthPackageAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyBandwidthPackageAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyBandwidthPackageAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCcnAttribute(self, request):
        """本介面（ModifyCcnAttribute）用于修改雲聯網（CCN）的相關屬性。

        :param request: Request instance for ModifyCcnAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyCcnAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyCcnAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCcnAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCcnAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCcnRegionBandwidthLimitsType(self, request):
        """本介面（ModifyCcnRegionBandwidthLimitsType）用于修改後付費雲聯網實例修改頻寬限速策略。

        :param request: Request instance for ModifyCcnRegionBandwidthLimitsType.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyCcnRegionBandwidthLimitsTypeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyCcnRegionBandwidthLimitsTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCcnRegionBandwidthLimitsType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCcnRegionBandwidthLimitsTypeResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyCustomerGatewayAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyCustomerGatewayAttributeResponse`

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


    def ModifyDirectConnectGatewayAttribute(self, request):
        """本介面（ModifyDirectConnectGatewayAttribute）用于修改專線閘道屬性

        :param request: Request instance for ModifyDirectConnectGatewayAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyDirectConnectGatewayAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyDirectConnectGatewayAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDirectConnectGatewayAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDirectConnectGatewayAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyFlowLogAttribute(self, request):
        """本介面（ModifyFlowLogAttribute）用于修改流日志屬性

        :param request: Request instance for ModifyFlowLogAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyFlowLogAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyFlowLogAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyFlowLogAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyFlowLogAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyGatewayFlowQos(self, request):
        """本介面（ModifyGatewayFlowQos）用于調整閘道流控頻寬。

        :param request: Request instance for ModifyGatewayFlowQos.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyGatewayFlowQosRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyGatewayFlowQosResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyGatewayFlowQos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyGatewayFlowQosResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyHaVipAttribute(self, request):
        """本介面（ModifyHaVipAttribute）用于修改高可用虛拟IP（HAVIP）屬性

        :param request: Request instance for ModifyHaVipAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyHaVipAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyHaVipAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyHaVipAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyHaVipAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyIp6AddressesBandwidth(self, request):
        """該介面用于修改IPV6網址訪問internet的頻寬

        :param request: Request instance for ModifyIp6AddressesBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyIp6AddressesBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyIp6AddressesBandwidthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyIp6AddressesBandwidth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyIp6AddressesBandwidthResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyIp6Rule(self, request):
        """該介面用于修改IPV6轉換規則，當前僅支援修改轉換規則名稱，IPV4網址和IPV4端口号

        :param request: Request instance for ModifyIp6Rule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyIp6RuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyIp6RuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyIp6Rule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyIp6RuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyIp6Translator(self, request):
        """該介面用于修改IP6轉換實例屬性，當前僅支援修改實例名稱。

        :param request: Request instance for ModifyIp6Translator.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyIp6TranslatorRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyIp6TranslatorResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyIp6Translator", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyIp6TranslatorResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyIpv6AddressesAttribute(self, request):
        """本介面（ModifyIpv6AddressesAttribute）用于修改彈性網卡内網IPv6網址屬性。

        :param request: Request instance for ModifyIpv6AddressesAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyIpv6AddressesAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyIpv6AddressesAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyIpv6AddressesAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyIpv6AddressesAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyNatGatewayAttribute(self, request):
        """本介面（ModifyNatGatewayAttribute）用于修改NAT閘道的屬性。

        :param request: Request instance for ModifyNatGatewayAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNatGatewayAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNatGatewayAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNatGatewayAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNatGatewayAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyNatGatewayDestinationIpPortTranslationNatRule(self, request):
        """本介面（ModifyNatGatewayDestinationIpPortTranslationNatRule）用于修改NAT閘道端口轉發規則。

        :param request: Request instance for ModifyNatGatewayDestinationIpPortTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNatGatewayDestinationIpPortTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNatGatewayDestinationIpPortTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNatGatewayDestinationIpPortTranslationNatRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNatGatewayDestinationIpPortTranslationNatRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyNetDetect(self, request):
        """本介面(ModifyNetDetect)用于修改網絡探測參數。

        :param request: Request instance for ModifyNetDetect.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNetDetectRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNetDetectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNetDetect", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNetDetectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyNetworkAclAttribute(self, request):
        """本介面（ModifyNetworkAclAttribute）用于修改網絡ACL屬性。

        :param request: Request instance for ModifyNetworkAclAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkAclAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkAclAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNetworkAclAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNetworkAclAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyNetworkAclEntries(self, request):
        """本介面（ModifyNetworkAclEntries）用于修改（包括添加和删除）網絡ACL的入站規則和出站規則。

        :param request: Request instance for ModifyNetworkAclEntries.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkAclEntriesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkAclEntriesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNetworkAclEntries", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNetworkAclEntriesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyNetworkInterfaceAttribute(self, request):
        """本介面（ModifyNetworkInterfaceAttribute）用于修改彈性網卡屬性。

        :param request: Request instance for ModifyNetworkInterfaceAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkInterfaceAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkInterfaceAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNetworkInterfaceAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNetworkInterfaceAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPrivateIpAddressesAttribute(self, request):
        """本介面（ModifyPrivateIpAddressesAttribute）用于修改彈性網卡内網IP屬性。

        :param request: Request instance for ModifyPrivateIpAddressesAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyPrivateIpAddressesAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyPrivateIpAddressesAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPrivateIpAddressesAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPrivateIpAddressesAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyRouteTableAttribute(self, request):
        """本介面（ModifyRouteTableAttribute）用于修改路由表（RouteTable）屬性。

        :param request: Request instance for ModifyRouteTableAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyRouteTableAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyRouteTableAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyRouteTableAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRouteTableAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySecurityGroupAttribute(self, request):
        """本介面（ModifySecurityGroupAttribute）用于修改安全組（SecurityGroupPolicy）屬性。

        :param request: Request instance for ModifySecurityGroupAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifySecurityGroupAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifySecurityGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySecurityGroupAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySecurityGroupAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySecurityGroupPolicies(self, request):
        """本介面（ModifySecurityGroupPolicies）用于重置安全組出站和入站規則（SecurityGroupPolicy）。

        * 介面是先删除當前所有的出入站規則，然後再添加 Egress 和 Ingress 規則，不支援自定義索引 PolicyIndex 。
        * 如果指定 SecurityGroupPolicySet.Version 爲0, 表示清空所有規則，并忽略Egress和Ingress。
        * Protocol欄位支援輸入TCP, UDP, ICMP, ICMPV6, GRE, ALL。
        * CidrBlock欄位允許輸入符合cidr格式标準的任意字串。(展開)在基礎網絡中，如果CidrBlock包含您的帳戶内的雲伺服器之外的設備在Top Cloud 的内網IP，并不代表此規則允許您訪問這些設備，租戶之間網絡隔離規則優先于安全組中的内網規則。
        * Ipv6CidrBlock欄位允許輸入符合IPv6 cidr格式标準的任意字串。(展開)在基礎網絡中，如果Ipv6CidrBlock包含您的帳戶内的雲伺服器之外的設備在Top Cloud 的内網IPv6，并不代表此規則允許您訪問這些設備，租戶之間網絡隔離規則優先于安全組中的内網規則。
        * SecurityGroupId欄位允許輸入與待修改的安全組位于相同項目中的安全組ID，包括這個安全組ID本身，代表安全組下所有雲伺服器的内網IP。使用這個欄位時，這條規則用來比對網絡報文的過程中會随着被使用的這個ID所關聯的雲伺服器變化而變化，不需要重新修改。
        * Port欄位允許輸入一個單獨端口号，或者用減号分隔的兩個端口号代表端口範圍，例如80或8000-8010。只有當Protocol欄位是TCP或UDP時，Port欄位才被接受。
        * Action欄位只允許輸入ACCEPT或DROP。
        * CidrBlock, Ipv6CidrBlock, SecurityGroupId, AddressTemplate四者是排他關系，不允許同時輸入，Protocol + Port和ServiceTemplate二者是排他關系，不允許同時輸入。

        :param request: Request instance for ModifySecurityGroupPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifySecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifySecurityGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySecurityGroupPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySecurityGroupPoliciesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyServiceTemplateAttribute(self, request):
        """本介面（ModifyServiceTemplateAttribute）用于修改協議端口範本

        :param request: Request instance for ModifyServiceTemplateAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyServiceTemplateAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyServiceTemplateAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyServiceTemplateAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyServiceTemplateAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyServiceTemplateGroupAttribute(self, request):
        """本介面（ModifyServiceTemplateGroupAttribute）用于修改協議端口範本集合。

        :param request: Request instance for ModifyServiceTemplateGroupAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyServiceTemplateGroupAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyServiceTemplateGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyServiceTemplateGroupAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyServiceTemplateGroupAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """本介面（ModifySubnetAttribute）用于修改子網屬性。

        :param request: Request instance for ModifySubnetAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifySubnetAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifySubnetAttributeResponse`

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
        """本介面（ModifyVpcAttribute）用于修改私有網絡（VPC）的相關屬性。

        :param request: Request instance for ModifyVpcAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcAttributeResponse`

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


    def ModifyVpnConnectionAttribute(self, request):
        """本介面（ModifyVpnConnectionAttribute）用于修改VPN通道。

        :param request: Request instance for ModifyVpnConnectionAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnConnectionAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnConnectionAttributeResponse`

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
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewayAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewayAttributeResponse`

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


    def ModifyVpnGatewayCcnRoutes(self, request):
        """本介面（ModifyVpnGatewayCcnRoutes）用于修改VPN閘道雲聯網路由

        :param request: Request instance for ModifyVpnGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyVpnGatewayCcnRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVpnGatewayCcnRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RejectAttachCcnInstances(self, request):
        """本介面（RejectAttachCcnInstances）用于跨賬号關聯實例時，雲聯網所有者拒絕關聯操作。

        :param request: Request instance for RejectAttachCcnInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.RejectAttachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.RejectAttachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RejectAttachCcnInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RejectAttachCcnInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """本介面 (ReleaseAddresses) 用于釋放一個或多個[彈性公網IP](https://cloud.tencent.com/document/product/213/1941)（簡稱 EIP）。
        * 該操作不可逆，釋放後 EIP 關聯的 IP 網址将不再屬于您的名下。
        * 只有狀态爲 UNBIND 的 EIP 才能進行釋放操作。

        :param request: Request instance for ReleaseAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReleaseAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReleaseAddressesResponse`

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


    def ReleaseIp6AddressesBandwidth(self, request):
        """該介面用于給彈性公網IPv6網址釋放頻寬。

        :param request: Request instance for ReleaseIp6AddressesBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReleaseIp6AddressesBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReleaseIp6AddressesBandwidthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReleaseIp6AddressesBandwidth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReleaseIp6AddressesBandwidthResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RemoveBandwidthPackageResources(self, request):
        """介面用于删除頻寬包資源，包括[彈性公網IP](https://cloud.tencent.com/document/product/213/1941)和[負載均衡](https://cloud.tencent.com/document/product/214/517)等

        :param request: Request instance for RemoveBandwidthPackageResources.
        :type request: :class:`tencentcloud.vpc.v20170312.models.RemoveBandwidthPackageResourcesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.RemoveBandwidthPackageResourcesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RemoveBandwidthPackageResources", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveBandwidthPackageResourcesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RemoveIp6Rules(self, request):
        """1. 該介面用于删除IPV6轉換規則
        2. 支援批次删除同一個轉換實例下的多個轉換規則

        :param request: Request instance for RemoveIp6Rules.
        :type request: :class:`tencentcloud.vpc.v20170312.models.RemoveIp6RulesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.RemoveIp6RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RemoveIp6Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveIp6RulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RenewVpnGateway(self, request):
        """本介面（RenewVpnGateway）用于預付費（包年包月）VPN閘道續約。目前只支援IPSEC閘道。

        :param request: Request instance for RenewVpnGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.RenewVpnGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.RenewVpnGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewVpnGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewVpnGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReplaceDirectConnectGatewayCcnRoutes(self, request):
        """本介面（ReplaceDirectConnectGatewayCcnRoutes）根據路由ID（RouteId）修改指定的路由（Route），支援批次修改。

        :param request: Request instance for ReplaceDirectConnectGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReplaceDirectConnectGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReplaceDirectConnectGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReplaceDirectConnectGatewayCcnRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReplaceDirectConnectGatewayCcnRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReplaceRouteTableAssociation(self, request):
        """本介面（ReplaceRouteTableAssociation)用于修改子網（Subnet）關聯的路由表（RouteTable）。
        * 一個子網只能關聯一個路由表。

        :param request: Request instance for ReplaceRouteTableAssociation.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReplaceRouteTableAssociationRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReplaceRouteTableAssociationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReplaceRouteTableAssociation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReplaceRouteTableAssociationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReplaceRoutes(self, request):
        """本介面（ReplaceRoutes）根據路由策略ID（RouteId）修改指定的路由策略（Route），支援批次修改。

        :param request: Request instance for ReplaceRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReplaceRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReplaceRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReplaceRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReplaceRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReplaceSecurityGroupPolicy(self, request):
        """本介面（ReplaceSecurityGroupPolicy）用于替換單條安全組規則（SecurityGroupPolicy）。
        單個請求中只能替換單個方向的一條規則, 必須要指定索引（PolicyIndex）。

        :param request: Request instance for ReplaceSecurityGroupPolicy.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReplaceSecurityGroupPolicyRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReplaceSecurityGroupPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReplaceSecurityGroupPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReplaceSecurityGroupPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetAttachCcnInstances(self, request):
        """本介面（ResetAttachCcnInstances）用于跨賬号關聯實例申請過期時，重新申請關聯操作。

        :param request: Request instance for ResetAttachCcnInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetAttachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetAttachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetAttachCcnInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetAttachCcnInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetNatGatewayConnection(self, request):
        """本介面（ResetNatGatewayConnection）用來NAT閘道并發連接上限。

        :param request: Request instance for ResetNatGatewayConnection.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetNatGatewayConnectionRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetNatGatewayConnectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetNatGatewayConnection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetNatGatewayConnectionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetRoutes(self, request):
        """本介面（ResetRoutes）用于對某個路由表名稱和所有路由策略（Route）進行重新設置。<br />
        注意: 調用本介面是先删除當前路由表中所有路由策略, 再保存新提交的路由策略内容, 會引起網絡中斷。

        :param request: Request instance for ResetRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetVpnConnectionRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetVpnConnectionResponse`

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


    def ResetVpnGatewayInternetMaxBandwidth(self, request):
        """本介面（ResetVpnGatewayInternetMaxBandwidth）調整VPN閘道頻寬上限。目前支援升級配置，如果是包年包月VPN閘道需要在有效期内。

        :param request: Request instance for ResetVpnGatewayInternetMaxBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetVpnGatewayInternetMaxBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetVpnGatewayInternetMaxBandwidthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetVpnGatewayInternetMaxBandwidth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetVpnGatewayInternetMaxBandwidthResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetCcnRegionBandwidthLimits(self, request):
        """本介面（SetCcnRegionBandwidthLimits）用于設置雲聯網（CCN）各地域出頻寬上限，該介面只能設置已關聯網絡實例包含的地域的出頻寬上限

        :param request: Request instance for SetCcnRegionBandwidthLimits.
        :type request: :class:`tencentcloud.vpc.v20170312.models.SetCcnRegionBandwidthLimitsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.SetCcnRegionBandwidthLimitsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetCcnRegionBandwidthLimits", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetCcnRegionBandwidthLimitsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TransformAddress(self, request):
        """本介面 (TransformAddress) 用于将實例的普通公網 IP 轉換爲[彈性公網IP](https://cloud.tencent.com/document/product/213/1941)（簡稱 EIP）。
        * 平台對用戶每地域每日解綁 EIP 重新分配普通公網 IP 次數有所限制（可參見 [EIP 産品簡介](/document/product/213/1941)）。上述配額可通過 [DescribeAddressQuota](https://cloud.tencent.com/document/api/213/1378) 介面獲取。

        :param request: Request instance for TransformAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.TransformAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.TransformAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TransformAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TransformAddressResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnassignIpv6Addresses(self, request):
        """本介面（UnassignIpv6Addresses）用于釋放彈性網卡`IPv6`網址。<br />
        本介面是異步完成，如需查詢異步任務執行結果，請使用本介面返回的`RequestId`輪詢`QueryTask`介面。

        :param request: Request instance for UnassignIpv6Addresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6AddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6AddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnassignIpv6Addresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnassignIpv6AddressesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnassignIpv6CidrBlock(self, request):
        """本介面（UnassignIpv6CidrBlock）用于釋放IPv6網段。<br />
        網段如果還有IP占用且未回收，則網段無法釋放。

        :param request: Request instance for UnassignIpv6CidrBlock.
        :type request: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6CidrBlockRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6CidrBlockResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnassignIpv6CidrBlock", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnassignIpv6CidrBlockResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnassignIpv6SubnetCidrBlock(self, request):
        """本介面（UnassignIpv6SubnetCidrBlock）用于釋放IPv6子網段。<br />
        子網段如果還有IP占用且未回收，則子網段無法釋放。

        :param request: Request instance for UnassignIpv6SubnetCidrBlock.
        :type request: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6SubnetCidrBlockRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6SubnetCidrBlockResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnassignIpv6SubnetCidrBlock", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnassignIpv6SubnetCidrBlockResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnassignPrivateIpAddresses(self, request):
        """本介面（UnassignPrivateIpAddresses）用于彈性網卡退還内網 IP。
        * 退還彈性網卡上的輔助内網IP，介面自動解關聯彈性公網 IP。不能退還彈性網卡的主内網IP。

        :param request: Request instance for UnassignPrivateIpAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.UnassignPrivateIpAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.UnassignPrivateIpAddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnassignPrivateIpAddresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnassignPrivateIpAddressesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)