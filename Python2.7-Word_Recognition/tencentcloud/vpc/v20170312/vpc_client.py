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
from taifucloudcloud.vpc.v20170312 import models


class VpcClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'vpc.taifucloudcloudapi.com'


    def AcceptAttachCcnInstances(self, request):
        """本介面（AcceptAttachCcnInstances）用于跨賬号關聯實例時，雲聯網所有者接受并同意關聯操作。

        :param request: 調用AcceptAttachCcnInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.AcceptAttachCcnInstancesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.AcceptAttachCcnInstancesResponse`

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
        """介面用于添加頻寬包資源，包括[彈性公網IP](https://cloud.taifucloud.com/document/product/213/1941)和[負載均衡](https://cloud.taifucloud.com/document/product/214/517)等

        :param request: 調用AddBandwidthPackageResources所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.AddBandwidthPackageResourcesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.AddBandwidthPackageResourcesResponse`

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

        :param request: 調用AddIp6Rules所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.AddIp6RulesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.AddIp6RulesResponse`

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
        """本介面 (AllocateAddresses) 用于申請一個或多個[彈性公網IP](https://cloud.taifucloud.com/document/product/213/1941)（簡稱 EIP）。
        * EIP 是專爲動态雲計算設計的靜态 IP 網址。借助 EIP，您可以快速将 EIP 重新映射到您的另一個實例上，從而屏蔽實例故障。
        * 您的 EIP 與Top Cloud 帳戶相關聯，而不是與某個實例相關聯。在您選擇顯式釋放該網址，或欠費超過七天之前，它會一直與您的Top Cloud 帳戶保持關聯。
        * 平台對用戶每地域能申請的 EIP 最大配額有所限制，可參見 [EIP 産品簡介](https://cloud.taifucloud.com/document/product/213/5733)，上述配額可通過 DescribeAddressQuota 介面獲取。

        :param request: 調用AllocateAddresses所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.AllocateAddressesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.AllocateAddressesResponse`

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


    def AssignIpv6Addresses(self, request):
        """本介面（AssignIpv6Addresses）用于彈性網卡申請`IPv6`網址。<br />
        本介面是異步完成，如需查詢異步任務執行結果，請使用本介面返回的`RequestId`輪詢`QueryTask`介面。
        * 一個彈性網卡支援綁定的IP網址是有限制的，更多資源限制訊息詳見<a href="/document/product/576/18527">彈性網卡使用限制</a>。
        * 可以指定`IPv6`網址申請，網址類型不能爲主`IP`，`IPv6`網址暫時只支援作爲輔助`IP`。
        * 網址必須要在彈性網卡所在子網内，而且不能被占用。
        * 在彈性網卡上申請一個到多個輔助`IPv6`網址，介面會在彈性網卡所在子網段内返回指定數量的輔助`IPv6`網址。

        :param request: 調用AssignIpv6Addresses所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.AssignIpv6AddressesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.AssignIpv6AddressesResponse`

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
        * 使用本介面前，你需要已有VPC實例，如果沒有可通過介面<a href="https://cloud.taifucloud.com/document/api/215/15774" title="CreateVpc" target="_blank">CreateVpc</a>創建。
        * 每個VPC只能申請一個IPv6網段

        :param request: 調用AssignIpv6CidrBlock所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.AssignIpv6CidrBlockRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.AssignIpv6CidrBlockResponse`

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

        :param request: 調用AssignIpv6SubnetCidrBlock所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.AssignIpv6SubnetCidrBlockRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.AssignIpv6SubnetCidrBlockResponse`

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

        :param request: 調用AssignPrivateIpAddresses所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.AssignPrivateIpAddressesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.AssignPrivateIpAddressesResponse`

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
        """本介面 (AssociateAddress) 用于将[彈性公網IP](https://cloud.taifucloud.com/document/product/213/1941)（簡稱 EIP）綁定到實例或彈性網卡的指定内網 IP 上。
        * 将 EIP 綁定到實例（CVM）上，其本質是将 EIP 綁定到實例上主網卡的主内網 IP 上。
        * 将 EIP 綁定到主網卡的主内網IP上，綁定過程會把其上綁定的普通公網 IP 自動解綁并釋放。
        * 将 EIP 綁定到指定網卡的内網 IP上（非主網卡的主内網IP），則必須先解綁該 EIP，才能再綁定新的。
        * 将 EIP 綁定到NAT閘道，請使用介面[EipBindNatGateway](https://cloud.taifucloud.com/document/product/215/4093)
        * EIP 如果欠費或被封堵，則不能被綁定。
        * 只有狀态爲 UNBIND 的 EIP 才能夠被綁定。

        :param request: 調用AssociateAddress所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.AssociateAddressRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.AssociateAddressResponse`

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


    def AttachCcnInstances(self, request):
        """本介面（AttachCcnInstances）用于将網絡實例加載到雲聯網實例中，網絡實例包括VPC和專線閘道。<br />
        每個雲聯網能夠關聯的網絡實例個數是有限的，詳請參考産品文件。如果需要擴充請聯系在線客服。

        :param request: 調用AttachCcnInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.AttachCcnInstancesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.AttachCcnInstancesResponse`

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
        * 私有網絡和基礎網絡的區别詳見vpc産品文件-<a href="https://cloud.taifucloud.com/document/product/215/535#2.-.E7.A7.81.E6.9C.89.E7.BD.91.E7.BB.9C.E4.B8.8E.E5.9F.BA.E7.A1.80.E7.BD.91.E7.BB.9C">私有網絡與基礎網絡</a>。

        :param request: 調用AttachClassicLinkVpc所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.AttachClassicLinkVpcRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.AttachClassicLinkVpcResponse`

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
        * 一個雲主機可以綁定多個彈性網卡，但只能綁定一個主網卡。更多限制訊息詳見<a href="https://cloud.taifucloud.com/document/product/215/6513">彈性網卡使用限制</a>。
        * 一個彈性網卡只能同時綁定一個雲主機。
        * 只有運作中或者已關機狀态的雲主機才能綁定彈性網卡，檢視雲主機狀态詳見<a href="https://cloud.taifucloud.com/document/api/213/9452#instance_state">Top Cloud 主機訊息</a>。
        * 彈性網卡綁定的雲主機必須是私有網絡的，而且雲主機所在可用區必須和彈性網卡子網的可用區相同。

        :param request: 調用AttachNetworkInterface所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.AttachNetworkInterfaceRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.AttachNetworkInterfaceResponse`

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


    def CreateAddressTemplate(self, request):
        """本介面（CreateAddressTemplate）用于創建IP網址模版

        :param request: 調用CreateAddressTemplate所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.CreateAddressTemplateRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.CreateAddressTemplateResponse`

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

        :param request: 調用CreateAddressTemplateGroup所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.CreateAddressTemplateGroupRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.CreateAddressTemplateGroupResponse`

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


    def CreateBandwidthPackage(self, request):
        """介面支援創建[設備頻寬包](https://cloud.taifucloud.com/document/product/684/15246#.E8.AE.BE.E5.A4.87.E5.B8.A6.E5.AE.BD.E5.8C.85)和[ip頻寬包](https://cloud.taifucloud.com/document/product/684/15246#ip-.E5.B8.A6.E5.AE.BD.E5.8C.85)

        :param request: 調用CreateBandwidthPackage所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.CreateBandwidthPackageRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.CreateBandwidthPackageResponse`

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
        每個賬号能創建的雲聯網實例個數是有限的，詳請參考産品文件。如果需要擴充請聯系在線客服。

        :param request: 調用CreateCcn所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.CreateCcnRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.CreateCcnResponse`

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

        :param request: 調用CreateCustomerGateway所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.CreateCustomerGatewayRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.CreateCustomerGatewayResponse`

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


    def CreateDefaultVpc(self, request):
        """本介面（CreateDefaultVpc）用于創建預設私有網絡(VPC）。

        預設VPC适用于快速入門和啓動公共實例，您可以像使用任何其他VPC一樣使用預設VPC。如果你想創建标準VPC，即指定VPC名稱、VPC網段、子網網段、子網可用區，請使用常規創建VPC介面（CreateVpc）

        正常情況，本介面并不一定生産預設VPC，而是根據用戶賬号的網絡屬性（DescribeAccountAttributes）來決定的
        * 支援基礎網絡、VPC，返回VpcId爲0
        * 只支援VPC，返回預設VPC訊息

        你也可以通過 Force 參數，強制返回預設VPC

        :param request: 調用CreateDefaultVpc所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.CreateDefaultVpcRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.CreateDefaultVpcResponse`

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

        :param request: 調用CreateDirectConnectGateway所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.CreateDirectConnectGatewayRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.CreateDirectConnectGatewayResponse`

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

        :param request: 調用CreateDirectConnectGatewayCcnRoutes所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.CreateDirectConnectGatewayCcnRoutesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.CreateDirectConnectGatewayCcnRoutesResponse`

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

        :param request: 調用CreateFlowLog所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.CreateFlowLogRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.CreateFlowLogResponse`

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

        :param request: 調用CreateHaVip所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.CreateHaVipRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.CreateHaVipResponse`

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
        2. 同一個帳戶在在一個地域最多允許創建10個轉換實例

        :param request: 調用CreateIp6Translators所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.CreateIp6TranslatorsRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.CreateIp6TranslatorsResponse`

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


    def CreateNetworkInterface(self, request):
        """本介面（CreateNetworkInterface）用于創建彈性網卡。
        * 創建彈性網卡時可以指定内網IP，并且可以指定一個主IP，指定的内網IP必須在彈性網卡所在子網内，而且不能被占用。
        * 創建彈性網卡時可以指定需要申請的内網IP數量，系統會随機生成内網IP網址。
        * 一個彈性網卡支援綁定的IP網址是有限制的，更多資源限制訊息詳見<a href="/document/product/576/18527">彈性網卡使用限制</a>。
        * 創建彈性網卡同時可以綁定已有安全組。

        :param request: 調用CreateNetworkInterface所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.CreateNetworkInterfaceRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.CreateNetworkInterfaceResponse`

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

        :param request: 調用CreateRouteTable所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.CreateRouteTableRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.CreateRouteTableResponse`

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

        :param request: 調用CreateRoutes所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.CreateRoutesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.CreateRoutesResponse`

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
        * 每個帳戶下每個地域的每個項目的<a href="https://cloud.taifucloud.com/document/product/213/500#2.-.E5.AE.89.E5.85.A8.E7.BB.84.E7.9A.84.E9.99.90.E5.88.B6">安全組數量限制</a>。
        * 新建的安全組的入站和出站規則預設都是全部拒絕，在創建後通常您需要再調用CreateSecurityGroupPolicies将安全組的規則設置爲需要的規則。

        :param request: 調用CreateSecurityGroup所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.CreateSecurityGroupRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.CreateSecurityGroupResponse`

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

        * Version安全組規則版本号，用戶每次更新安全規則版本會自動加1，防止你更新的路由規則已過期，不填不考慮沖突。
        * Protocol欄位支援輸入TCP, UDP, ICMP, GRE, ALL。
        * CidrBlock欄位允許輸入符合cidr格式标準的任意字串。(展開)在基礎網絡中，如果CidrBlock包含您的帳戶内的雲伺服器之外的設備在Top Cloud 的内網IP，并不代表此規則允許您訪問這些設備，租戶之間網絡隔離規則優先于安全組中的内網規則。
        * SecurityGroupId欄位允許輸入與待修改的安全組位于相同項目中的安全組ID，包括這個安全組ID本身，代表安全組下所有雲伺服器的内網IP。使用這個欄位時，這條規則用來比對網絡報文的過程中會随着被使用的這個ID所關聯的雲伺服器變化而變化，不需要重新修改。
        * Port欄位允許輸入一個單獨端口号，或者用減号分隔的兩個端口号代表端口範圍，例如80或8000-8010。只有當Protocol欄位是TCP或UDP時，Port欄位才被接受，即Protocol欄位不是TCP或UDP時，Protocol和Port排他關系，不允許同時輸入，否則會介面報錯。
        * Action欄位只允許輸入ACCEPT或DROP。
        * CidrBlock, SecurityGroupId, AddressTemplate三者是排他關系，不允許同時輸入，Protocol + Port和ServiceTemplate二者是排他關系，不允許同時輸入。
        * 一次請求中只能創建單個方向的規則, 如果需要指定索引（PolicyIndex）參數, 多條規則的索引必須一緻。

        :param request: 調用CreateSecurityGroupPolicies所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.CreateSecurityGroupPoliciesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.CreateSecurityGroupPoliciesResponse`

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


    def CreateServiceTemplate(self, request):
        """本介面（CreateServiceTemplate）用于創建協議端口範本

        :param request: 調用CreateServiceTemplate所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.CreateServiceTemplateRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.CreateServiceTemplateResponse`

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

        :param request: 調用CreateServiceTemplateGroup所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.CreateServiceTemplateGroupRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.CreateServiceTemplateGroupResponse`

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
        * 你可以創建的最小網段子網掩碼爲28（有16個IP網址），最大網段子網掩碼爲16（65,536個IP網址）。
        * 同一個VPC内，多個子網的網段不能重疊。
        * 子網創建後會自動關聯到預設路由表。

        :param request: 調用CreateSubnet所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.CreateSubnetRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.CreateSubnetResponse`

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
        * 你可以創建的最小網段子網掩碼爲28（有16個IP網址），最大網段子網掩碼爲16（65,536個IP網址）。
        * 同一個VPC内，多個子網的網段不能重疊。
        * 子網創建後會自動關聯到預設路由表。

        :param request: 調用CreateSubnets所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.CreateSubnetsRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.CreateSubnetsResponse`

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
        * 同一個地域能創建的VPC資源個數也是有限制的，詳見 <a href="https://cloud.taifucloud.com/doc/product/215/537" title="VPC使用限制">VPC使用限制</a>,如果需要擴充請聯系在線客服。

        :param request: 調用CreateVpc所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.CreateVpcRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.CreateVpcResponse`

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

        :param request: 調用CreateVpnConnection所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.CreateVpnConnectionRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.CreateVpnConnectionResponse`

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

        :param request: 調用CreateVpnGateway所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.CreateVpnGatewayRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.CreateVpnGatewayResponse`

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

        :param request: 調用DeleteAddressTemplate所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DeleteAddressTemplateRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DeleteAddressTemplateResponse`

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

        :param request: 調用DeleteAddressTemplateGroup所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DeleteAddressTemplateGroupRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DeleteAddressTemplateGroupResponse`

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


    def DeleteBandwidthPackage(self, request):
        """介面支援删除共享頻寬包，包括[設備頻寬包](https://cloud.taifucloud.com/document/product/684/15246#.E8.AE.BE.E5.A4.87.E5.B8.A6.E5.AE.BD.E5.8C.85)和[ip頻寬包](https://cloud.taifucloud.com/document/product/684/15246#ip-.E5.B8.A6.E5.AE.BD.E5.8C.85)

        :param request: 調用DeleteBandwidthPackage所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DeleteBandwidthPackageRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DeleteBandwidthPackageResponse`

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

        :param request: 調用DeleteCcn所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DeleteCcnRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DeleteCcnResponse`

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

        :param request: 調用DeleteCustomerGateway所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DeleteCustomerGatewayRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DeleteCustomerGatewayResponse`

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

        :param request: 調用DeleteDirectConnectGateway所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DeleteDirectConnectGatewayRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DeleteDirectConnectGatewayResponse`

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

        :param request: 調用DeleteDirectConnectGatewayCcnRoutes所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DeleteDirectConnectGatewayCcnRoutesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DeleteDirectConnectGatewayCcnRoutesResponse`

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

        :param request: 調用DeleteFlowLog所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DeleteFlowLogRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DeleteFlowLogResponse`

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

        :param request: 調用DeleteHaVip所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DeleteHaVipRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DeleteHaVipResponse`

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

        :param request: 調用DeleteIp6Translators所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DeleteIp6TranslatorsRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DeleteIp6TranslatorsResponse`

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


    def DeleteNetworkInterface(self, request):
        """本介面（DeleteNetworkInterface）用于删除彈性網卡。
        * 彈性網卡上綁定了雲主機時，不能被删除。
        * 删除指定彈性網卡，彈性網卡必須先和子機解綁才能删除。删除之後彈性網卡上所有内網IP都将被退還。

        :param request: 調用DeleteNetworkInterface所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DeleteNetworkInterfaceRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DeleteNetworkInterfaceResponse`

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

        :param request: 調用DeleteRouteTable所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DeleteRouteTableRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DeleteRouteTableResponse`

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

        :param request: 調用DeleteRoutes所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DeleteRoutesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DeleteRoutesResponse`

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

        :param request: 調用DeleteSecurityGroup所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DeleteSecurityGroupRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DeleteSecurityGroupResponse`

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

        :param request: 調用DeleteSecurityGroupPolicies所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DeleteSecurityGroupPoliciesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DeleteSecurityGroupPoliciesResponse`

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

        :param request: 調用DeleteServiceTemplate所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DeleteServiceTemplateRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DeleteServiceTemplateResponse`

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

        :param request: 調用DeleteServiceTemplateGroup所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DeleteServiceTemplateGroupRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DeleteServiceTemplateGroupResponse`

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
        * 删除子網前，請清理該子網下所有資源，包括雲主機、負載均衡、雲數據、noSql、彈性網卡等資源。

        :param request: 調用DeleteSubnet所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DeleteSubnetRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DeleteSubnetResponse`

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
        * 删除前請确保 VPC 内已經沒有相關資源，例如雲主機、雲資料庫、NoSQL、VPN閘道、專線閘道、負載均衡、對等連接、與之互通的基礎網絡設備等。
        * 删除私有網絡是不可逆的操作，請謹慎處理。

        :param request: 調用DeleteVpc所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DeleteVpcRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DeleteVpcResponse`

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

        :param request: 調用DeleteVpnConnection所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DeleteVpnConnectionRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DeleteVpnConnectionResponse`

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

        :param request: 調用DeleteVpnGateway所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DeleteVpnGatewayRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DeleteVpnGatewayResponse`

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

        :param request: 調用DescribeAccountAttributes所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeAccountAttributesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeAccountAttributesResponse`

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
        """本介面 (DescribeAddressQuota) 用于查詢您帳戶的[彈性公網IP](https://cloud.taifucloud.com/document/product/213/1941)（簡稱 EIP）在當前地域的配額訊息。配額詳情可參見 [EIP 産品簡介](https://cloud.taifucloud.com/document/product/213/5733)。

        :param request: 調用DescribeAddressQuota所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeAddressQuotaRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeAddressQuotaResponse`

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

        :param request: 調用DescribeAddressTemplateGroups所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeAddressTemplateGroupsRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeAddressTemplateGroupsResponse`

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

        :param request: 調用DescribeAddressTemplates所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeAddressTemplatesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeAddressTemplatesResponse`

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
        """本介面 (DescribeAddresses) 用于查詢一個或多個[彈性公網IP](https://cloud.taifucloud.com/document/product/213/1941)（簡稱 EIP）的詳細訊息。
        * 如果參數爲空，返回當前用戶一定數量（Limit所指定的數量，預設爲20）的 EIP。

        :param request: 調用DescribeAddresses所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeAddressesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeAddressesResponse`

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


    def DescribeBandwidthPackageQuota(self, request):
        """介面用于查詢帳戶在當前地域的頻寬包上限數量以及使用數量

        :param request: 調用DescribeBandwidthPackageQuota所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeBandwidthPackageQuotaRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeBandwidthPackageQuotaResponse`

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

        :param request: 調用DescribeBandwidthPackages所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeBandwidthPackagesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeBandwidthPackagesResponse`

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

        :param request: 調用DescribeCcnAttachedInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeCcnAttachedInstancesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeCcnAttachedInstancesResponse`

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

        :param request: 調用DescribeCcnRegionBandwidthLimits所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeCcnRegionBandwidthLimitsRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeCcnRegionBandwidthLimitsResponse`

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

        :param request: 調用DescribeCcnRoutes所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeCcnRoutesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeCcnRoutesResponse`

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

        :param request: 調用DescribeCcns所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeCcnsRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeCcnsResponse`

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

        :param request: 調用DescribeClassicLinkInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeClassicLinkInstancesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeClassicLinkInstancesResponse`

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

        :param request: 調用DescribeCustomerGatewayVendors所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeCustomerGatewayVendorsRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeCustomerGatewayVendorsResponse`

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

        :param request: 調用DescribeCustomerGateways所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeCustomerGatewaysRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeCustomerGatewaysResponse`

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

        :param request: 調用DescribeDirectConnectGatewayCcnRoutes所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeDirectConnectGatewayCcnRoutesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeDirectConnectGatewayCcnRoutesResponse`

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

        :param request: 調用DescribeDirectConnectGateways所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeDirectConnectGatewaysRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeDirectConnectGatewaysResponse`

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

        :param request: 調用DescribeFlowLog所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeFlowLogRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeFlowLogResponse`

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

        :param request: 調用DescribeFlowLogs所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeFlowLogsRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeFlowLogsResponse`

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

        :param request: 調用DescribeGatewayFlowMonitorDetail所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeGatewayFlowMonitorDetailRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeGatewayFlowMonitorDetailResponse`

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


    def DescribeHaVips(self, request):
        """本介面（DescribeHaVips）用于查詢高可用虛拟IP（HAVIP）清單。

        :param request: 調用DescribeHaVips所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeHaVipsRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeHaVipsResponse`

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


    def DescribeIp6TranslatorQuota(self, request):
        """查詢帳戶在指定地域IPV6轉換實例和規則的配額

        :param request: 調用DescribeIp6TranslatorQuota所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeIp6TranslatorQuotaRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeIp6TranslatorQuotaResponse`

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

        :param request: 調用DescribeIp6Translators所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeIp6TranslatorsRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeIp6TranslatorsResponse`

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


    def DescribeNetworkInterfaces(self, request):
        """本介面（DescribeNetworkInterfaces）用于查詢彈性網卡清單。

        :param request: 調用DescribeNetworkInterfaces所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeNetworkInterfacesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeNetworkInterfacesResponse`

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

        :param request: 調用DescribeRouteConflicts所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeRouteConflictsRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeRouteConflictsResponse`

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

        :param request: 調用DescribeRouteTables所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeRouteTablesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeRouteTablesResponse`

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

        :param request: 調用DescribeSecurityGroupAssociationStatistics所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeSecurityGroupAssociationStatisticsRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeSecurityGroupAssociationStatisticsResponse`

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


    def DescribeSecurityGroupPolicies(self, request):
        """本介面（DescribeSecurityGroupPolicies）用于查詢安全組規則。

        :param request: 調用DescribeSecurityGroupPolicies所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeSecurityGroupPoliciesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeSecurityGroupPoliciesResponse`

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


    def DescribeSecurityGroups(self, request):
        """本介面（DescribeSecurityGroups）用于查詢安全組。

        :param request: 調用DescribeSecurityGroups所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeSecurityGroupsRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeSecurityGroupsResponse`

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

        :param request: 調用DescribeServiceTemplateGroups所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeServiceTemplateGroupsRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeServiceTemplateGroupsResponse`

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

        :param request: 調用DescribeServiceTemplates所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeServiceTemplatesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeServiceTemplatesResponse`

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

        :param request: 調用DescribeSubnets所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeSubnetsRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeSubnetsResponse`

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


    def DescribeVpcIpv6Addresses(self, request):
        """本介面（DescribeVpcIpv6Addresses）用于查詢 `VPC` `IPv6` 訊息。
        只能查詢已使用的`IPv6`訊息，當查詢未使用的IP時，本介面不會報錯，但不會出現在返回結果裏。

        :param request: 調用DescribeVpcIpv6Addresses所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeVpcIpv6AddressesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeVpcIpv6AddressesResponse`

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


    def DescribeVpcPrivateIpAddresses(self, request):
        """本介面（DescribeVpcPrivateIpAddresses）用于查詢VPC内網IP訊息。<br />
        只能查詢已使用的IP訊息，當查詢未使用的IP時，本介面不會報錯，但不會出現在返回結果裏。

        :param request: 調用DescribeVpcPrivateIpAddresses所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeVpcPrivateIpAddressesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeVpcPrivateIpAddressesResponse`

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


    def DescribeVpcs(self, request):
        """本介面（DescribeVpcs）用于查詢私有網絡清單。

        :param request: 調用DescribeVpcs所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeVpcsRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeVpcsResponse`

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

        :param request: 調用DescribeVpnConnections所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeVpnConnectionsRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeVpnConnectionsResponse`

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

        :param request: 調用DescribeVpnGateways所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DescribeVpnGatewaysRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DescribeVpnGatewaysResponse`

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

        :param request: 調用DetachCcnInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DetachCcnInstancesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DetachCcnInstancesResponse`

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

        :param request: 調用DetachClassicLinkVpc所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DetachClassicLinkVpcRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DetachClassicLinkVpcResponse`

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

        :param request: 調用DetachNetworkInterface所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DetachNetworkInterfaceRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DetachNetworkInterfaceResponse`

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

        :param request: 調用DisableCcnRoutes所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DisableCcnRoutesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DisableCcnRoutesResponse`

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


    def DisableRoutes(self, request):
        """本介面（DisableRoutes）用于禁用已啓用的子網路由

        :param request: 調用DisableRoutes所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DisableRoutesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DisableRoutesResponse`

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
        """本介面 (DisassociateAddress) 用于解綁[彈性公網IP](https://cloud.taifucloud.com/document/product/213/1941)（簡稱 EIP）。
        * 支援CVM實例，彈性網卡上的EIP解綁
        * 不支援NAT上的EIP解綁。NAT上的EIP解綁請參考[EipUnBindNatGateway](https://cloud.taifucloud.com/document/product/215/4092)
        * 只有狀态爲 BIND 和 BIND_ENI 的 EIP 才能進行解綁定操作。
        * EIP 如果被封堵，則不能進行解綁定操作。

        :param request: 調用DisassociateAddress所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DisassociateAddressRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DisassociateAddressResponse`

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


    def DownloadCustomerGatewayConfiguration(self, request):
        """本介面(DownloadCustomerGatewayConfiguration)用于下載VPN通道配置。

        :param request: 調用DownloadCustomerGatewayConfiguration所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.DownloadCustomerGatewayConfigurationRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.DownloadCustomerGatewayConfigurationResponse`

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

        :param request: 調用EnableCcnRoutes所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.EnableCcnRoutesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.EnableCcnRoutesResponse`

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


    def EnableRoutes(self, request):
        """本介面（EnableRoutes）用于啓用已禁用的子網路由。<br />
        本介面會校驗啓用後，是否與已有路由沖突，如果沖突，則無法啓用，失敗處理。路由沖突時，需要先禁用與之沖突的路由，才能啓用該路由。

        :param request: 調用EnableRoutes所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.EnableRoutesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.EnableRoutesResponse`

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

        :param request: 調用HaVipAssociateAddressIp所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.HaVipAssociateAddressIpRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.HaVipAssociateAddressIpResponse`

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

        :param request: 調用HaVipDisassociateAddressIp所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.HaVipDisassociateAddressIpRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.HaVipDisassociateAddressIpResponse`

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

        :param request: 調用InquiryPriceCreateVpnGateway所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.InquiryPriceCreateVpnGatewayRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.InquiryPriceCreateVpnGatewayResponse`

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

        :param request: 調用InquiryPriceRenewVpnGateway所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.InquiryPriceRenewVpnGatewayRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.InquiryPriceRenewVpnGatewayResponse`

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

        :param request: 調用InquiryPriceResetVpnGatewayInternetMaxBandwidth所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.InquiryPriceResetVpnGatewayInternetMaxBandwidthRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.InquiryPriceResetVpnGatewayInternetMaxBandwidthResponse`

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

        :param request: 調用MigrateNetworkInterface所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.MigrateNetworkInterfaceRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.MigrateNetworkInterfaceResponse`

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

        :param request: 調用MigratePrivateIpAddress所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.MigratePrivateIpAddressRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.MigratePrivateIpAddressResponse`

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
        """本介面 (ModifyAddressAttribute) 用于修改[彈性公網IP](https://cloud.taifucloud.com/document/product/213/1941)（簡稱 EIP）的名稱。

        :param request: 調用ModifyAddressAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ModifyAddressAttributeRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ModifyAddressAttributeResponse`

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


    def ModifyAddressTemplateAttribute(self, request):
        """本介面（ModifyAddressTemplateAttribute）用于修改IP網址範本

        :param request: 調用ModifyAddressTemplateAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ModifyAddressTemplateAttributeRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ModifyAddressTemplateAttributeResponse`

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

        :param request: 調用ModifyAddressTemplateGroupAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ModifyAddressTemplateGroupAttributeRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ModifyAddressTemplateGroupAttributeResponse`

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
        """本介面（ModifyAddressesBandwidth）用于調整[彈性公網IP](https://cloud.taifucloud.com/document/product/213/1941)(簡稱EIP)頻寬，包括後付費EIP, 預付費EIP和頻寬包EIP

        :param request: 調用ModifyAddressesBandwidth所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ModifyAddressesBandwidthRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ModifyAddressesBandwidthResponse`

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


    def ModifyBandwidthPackageAttribute(self, request):
        """介面用于修改頻寬包屬性，包括頻寬包名字等

        :param request: 調用ModifyBandwidthPackageAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ModifyBandwidthPackageAttributeRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ModifyBandwidthPackageAttributeResponse`

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

        :param request: 調用ModifyCcnAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ModifyCcnAttributeRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ModifyCcnAttributeResponse`

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


    def ModifyCustomerGatewayAttribute(self, request):
        """本介面（ModifyCustomerGatewayAttribute）用于修改對端閘道訊息。

        :param request: 調用ModifyCustomerGatewayAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ModifyCustomerGatewayAttributeRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ModifyCustomerGatewayAttributeResponse`

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

        :param request: 調用ModifyDirectConnectGatewayAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ModifyDirectConnectGatewayAttributeRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ModifyDirectConnectGatewayAttributeResponse`

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

        :param request: 調用ModifyFlowLogAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ModifyFlowLogAttributeRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ModifyFlowLogAttributeResponse`

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


    def ModifyHaVipAttribute(self, request):
        """本介面（ModifyHaVipAttribute）用于修改高可用虛拟IP（HAVIP）屬性

        :param request: 調用ModifyHaVipAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ModifyHaVipAttributeRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ModifyHaVipAttributeResponse`

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


    def ModifyIp6Rule(self, request):
        """該介面用于修改IPV6轉換規則，當前僅支援修改轉換規則名稱，IPV4網址和IPV4端口号

        :param request: 調用ModifyIp6Rule所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ModifyIp6RuleRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ModifyIp6RuleResponse`

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

        :param request: 調用ModifyIp6Translator所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ModifyIp6TranslatorRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ModifyIp6TranslatorResponse`

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

        :param request: 調用ModifyIpv6AddressesAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ModifyIpv6AddressesAttributeRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ModifyIpv6AddressesAttributeResponse`

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


    def ModifyNetworkInterfaceAttribute(self, request):
        """本介面（ModifyNetworkInterfaceAttribute）用于修改彈性網卡屬性。

        :param request: 調用ModifyNetworkInterfaceAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ModifyNetworkInterfaceAttributeRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ModifyNetworkInterfaceAttributeResponse`

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

        :param request: 調用ModifyPrivateIpAddressesAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ModifyPrivateIpAddressesAttributeRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ModifyPrivateIpAddressesAttributeResponse`

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

        :param request: 調用ModifyRouteTableAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ModifyRouteTableAttributeRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ModifyRouteTableAttributeResponse`

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

        :param request: 調用ModifySecurityGroupAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ModifySecurityGroupAttributeRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ModifySecurityGroupAttributeResponse`

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
        * Protocol欄位支援輸入TCP, UDP, ICMP, GRE, ALL。
        * CidrBlock欄位允許輸入符合cidr格式标準的任意字串。(展開)在基礎網絡中，如果CidrBlock包含您的帳戶内的雲伺服器之外的設備在Top Cloud 的内網IP，并不代表此規則允許您訪問這些設備，租戶之間網絡隔離規則優先于安全組中的内網規則。
        * SecurityGroupId欄位允許輸入與待修改的安全組位于相同項目中的安全組ID，包括這個安全組ID本身，代表安全組下所有雲伺服器的内網IP。使用這個欄位時，這條規則用來比對網絡報文的過程中會随着被使用的這個ID所關聯的雲伺服器變化而變化，不需要重新修改。
        * Port欄位允許輸入一個單獨端口号，或者用減号分隔的兩個端口号代表端口範圍，例如80或8000-8010。只有當Protocol欄位是TCP或UDP時，Port欄位才被接受。
        * Action欄位只允許輸入ACCEPT或DROP。
        * CidrBlock, SecurityGroupId, AddressTemplate三者是排他關系，不允許同時輸入，Protocol + Port和ServiceTemplate二者是排他關系，不允許同時輸入。

        :param request: 調用ModifySecurityGroupPolicies所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ModifySecurityGroupPoliciesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ModifySecurityGroupPoliciesResponse`

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

        :param request: 調用ModifyServiceTemplateAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ModifyServiceTemplateAttributeRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ModifyServiceTemplateAttributeResponse`

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

        :param request: 調用ModifyServiceTemplateGroupAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ModifyServiceTemplateGroupAttributeRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ModifyServiceTemplateGroupAttributeResponse`

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

        :param request: 調用ModifySubnetAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ModifySubnetAttributeRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ModifySubnetAttributeResponse`

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

        :param request: 調用ModifyVpcAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ModifyVpcAttributeRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ModifyVpcAttributeResponse`

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

        :param request: 調用ModifyVpnConnectionAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ModifyVpnConnectionAttributeRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ModifyVpnConnectionAttributeResponse`

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

        :param request: 調用ModifyVpnGatewayAttribute所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ModifyVpnGatewayAttributeRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ModifyVpnGatewayAttributeResponse`

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


    def RejectAttachCcnInstances(self, request):
        """本介面（RejectAttachCcnInstances）用于跨賬号關聯實例時，雲聯網所有者拒絕關聯操作。

        :param request: 調用RejectAttachCcnInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.RejectAttachCcnInstancesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.RejectAttachCcnInstancesResponse`

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
        """本介面 (ReleaseAddresses) 用于釋放一個或多個[彈性公網IP](https://cloud.taifucloud.com/document/product/213/1941)（簡稱 EIP）。
        * 該操作不可逆，釋放後 EIP 關聯的 IP 網址将不再屬于您的名下。
        * 只有狀态爲 UNBIND 的 EIP 才能進行釋放操作。

        :param request: 調用ReleaseAddresses所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ReleaseAddressesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ReleaseAddressesResponse`

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


    def RemoveBandwidthPackageResources(self, request):
        """介面用于删除頻寬包資源，包括[彈性公網IP](https://cloud.taifucloud.com/document/product/213/1941)和[負載均衡](https://cloud.taifucloud.com/document/product/214/517)等

        :param request: 調用RemoveBandwidthPackageResources所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.RemoveBandwidthPackageResourcesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.RemoveBandwidthPackageResourcesResponse`

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

        :param request: 調用RemoveIp6Rules所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.RemoveIp6RulesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.RemoveIp6RulesResponse`

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

        :param request: 調用RenewVpnGateway所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.RenewVpnGatewayRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.RenewVpnGatewayResponse`

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

        :param request: 調用ReplaceDirectConnectGatewayCcnRoutes所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ReplaceDirectConnectGatewayCcnRoutesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ReplaceDirectConnectGatewayCcnRoutesResponse`

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

        :param request: 調用ReplaceRouteTableAssociation所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ReplaceRouteTableAssociationRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ReplaceRouteTableAssociationResponse`

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

        :param request: 調用ReplaceRoutes所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ReplaceRoutesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ReplaceRoutesResponse`

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

        :param request: 調用ReplaceSecurityGroupPolicy所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ReplaceSecurityGroupPolicyRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ReplaceSecurityGroupPolicyResponse`

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

        :param request: 調用ResetAttachCcnInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ResetAttachCcnInstancesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ResetAttachCcnInstancesResponse`

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


    def ResetRoutes(self, request):
        """本介面（ResetRoutes）用于對某個路由表名稱和所有路由策略（Route）進行重新設置。<br />
        注意: 調用本介面是先删除當前路由表中所有路由策略, 再保存新提交的路由策略内容, 會引起網絡中斷。

        :param request: 調用ResetRoutes所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ResetRoutesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ResetRoutesResponse`

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

        :param request: 調用ResetVpnConnection所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ResetVpnConnectionRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ResetVpnConnectionResponse`

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

        :param request: 調用ResetVpnGatewayInternetMaxBandwidth所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.ResetVpnGatewayInternetMaxBandwidthRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.ResetVpnGatewayInternetMaxBandwidthResponse`

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

        :param request: 調用SetCcnRegionBandwidthLimits所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.SetCcnRegionBandwidthLimitsRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.SetCcnRegionBandwidthLimitsResponse`

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
        """本介面 (TransformAddress) 用于将實例的普通公網 IP 轉換爲[彈性公網IP](https://cloud.taifucloud.com/document/product/213/1941)（簡稱 EIP）。
        * 平台對用戶每地域每日解綁 EIP 重新分配普通公網 IP 次數有所限制（可參見 [EIP 産品簡介](/document/product/213/1941)）。上述配額可通過 [DescribeAddressQuota](https://cloud.taifucloud.com/document/api/213/1378) 介面獲取。

        :param request: 調用TransformAddress所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.TransformAddressRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.TransformAddressResponse`

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

        :param request: 調用UnassignIpv6Addresses所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.UnassignIpv6AddressesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.UnassignIpv6AddressesResponse`

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

        :param request: 調用UnassignIpv6CidrBlock所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.UnassignIpv6CidrBlockRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.UnassignIpv6CidrBlockResponse`

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

        :param request: 調用UnassignIpv6SubnetCidrBlock所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.UnassignIpv6SubnetCidrBlockRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.UnassignIpv6SubnetCidrBlockResponse`

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

        :param request: 調用UnassignPrivateIpAddresses所需參數的結構體。
        :type request: :class:`taifucloudcloud.vpc.v20170312.models.UnassignPrivateIpAddressesRequest`
        :rtype: :class:`taifucloudcloud.vpc.v20170312.models.UnassignPrivateIpAddressesResponse`

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