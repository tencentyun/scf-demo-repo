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

from tencentcloud.common.abstract_model import AbstractModel


class AcceptAttachCcnInstancesRequest(AbstractModel):
    """AcceptAttachCcnInstances請求參數結構體

    """

    def __init__(self):
        """
        :param CcnId: CCN實例ID。形如：ccn-f49l6u0z。
        :type CcnId: str
        :param Instances: 接受關聯實例清單。
        :type Instances: list of CcnInstance
        """
        self.CcnId = None
        self.Instances = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = CcnInstance()
                obj._deserialize(item)
                self.Instances.append(obj)


class AcceptAttachCcnInstancesResponse(AbstractModel):
    """AcceptAttachCcnInstances返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AccountAttribute(AbstractModel):
    """帳戶屬性對象

    """

    def __init__(self):
        """
        :param AttributeName: 屬性名
        :type AttributeName: str
        :param AttributeValues: 屬性值
        :type AttributeValues: list of str
        """
        self.AttributeName = None
        self.AttributeValues = None


    def _deserialize(self, params):
        self.AttributeName = params.get("AttributeName")
        self.AttributeValues = params.get("AttributeValues")


class AddBandwidthPackageResourcesRequest(AbstractModel):
    """AddBandwidthPackageResources請求參數結構體

    """

    def __init__(self):
        """
        :param ResourceIds: 資源唯一ID，當前支援EIP資源和LB資源，形如'eip-xxxx', 'lb-xxxx'
        :type ResourceIds: list of str
        :param BandwidthPackageId: 頻寬包唯一标識ID，形如'bwp-xxxx'
        :type BandwidthPackageId: str
        :param NetworkType: 頻寬包類型，當前支援'BGP'類型，表示内部資源是BGP IP。
        :type NetworkType: str
        :param ResourceType: 資源類型，包括'Address', 'LoadBalance'
        :type ResourceType: str
        :param Protocol: 頻寬包協議類型。當前支援'ipv4'和'ipv6'協議類型。
        :type Protocol: str
        """
        self.ResourceIds = None
        self.BandwidthPackageId = None
        self.NetworkType = None
        self.ResourceType = None
        self.Protocol = None


    def _deserialize(self, params):
        self.ResourceIds = params.get("ResourceIds")
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        self.NetworkType = params.get("NetworkType")
        self.ResourceType = params.get("ResourceType")
        self.Protocol = params.get("Protocol")


class AddBandwidthPackageResourcesResponse(AbstractModel):
    """AddBandwidthPackageResources返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddIp6RulesRequest(AbstractModel):
    """AddIp6Rules請求參數結構體

    """

    def __init__(self):
        """
        :param Ip6TranslatorId: IPV6轉換實例唯一ID，形如ip6-xxxxxxxx
        :type Ip6TranslatorId: str
        :param Ip6RuleInfos: IPV6轉換規則訊息
        :type Ip6RuleInfos: list of Ip6RuleInfo
        :param Ip6RuleName: IPV6轉換規則名稱
        :type Ip6RuleName: str
        """
        self.Ip6TranslatorId = None
        self.Ip6RuleInfos = None
        self.Ip6RuleName = None


    def _deserialize(self, params):
        self.Ip6TranslatorId = params.get("Ip6TranslatorId")
        if params.get("Ip6RuleInfos") is not None:
            self.Ip6RuleInfos = []
            for item in params.get("Ip6RuleInfos"):
                obj = Ip6RuleInfo()
                obj._deserialize(item)
                self.Ip6RuleInfos.append(obj)
        self.Ip6RuleName = params.get("Ip6RuleName")


class AddIp6RulesResponse(AbstractModel):
    """AddIp6Rules返回參數結構體

    """

    def __init__(self):
        """
        :param Ip6RuleSet: IPV6轉換規則唯一ID數組，形如rule6-xxxxxxxx
        :type Ip6RuleSet: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Ip6RuleSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ip6RuleSet = params.get("Ip6RuleSet")
        self.RequestId = params.get("RequestId")


class Address(AbstractModel):
    """描述 EIP 訊息

    """

    def __init__(self):
        """
        :param AddressId: `EIP`的`ID`，是`EIP`的唯一标識。
        :type AddressId: str
        :param AddressName: `EIP`名稱。
        :type AddressName: str
        :param AddressStatus: `EIP`狀态，包含'CREATING'(創建中),'BINDING'(綁定中),'BIND'(已綁定),'UNBINDING'(解綁中),'UNBIND'(已解綁),'OFFLINING'(釋放中),'BIND_ENI'(綁定懸空彈性網卡)
        :type AddressStatus: str
        :param AddressIp: 外網IP網址
        :type AddressIp: str
        :param InstanceId: 綁定的資源實例`ID`。可能是一個`CVM`，`NAT`。
        :type InstanceId: str
        :param CreatedTime: 創建時間。按照`ISO8601`标準表示，并且使用`UTC`時間。格式爲：`YYYY-MM-DDThh:mm:ssZ`。
        :type CreatedTime: str
        :param NetworkInterfaceId: 綁定的彈性網卡ID
        :type NetworkInterfaceId: str
        :param PrivateAddressIp: 綁定的資源内網ip
        :type PrivateAddressIp: str
        :param IsArrears: 資源隔離狀态。true表示eip處于隔離狀态，false表示資源處于未隔離狀态
        :type IsArrears: bool
        :param IsBlocked: 資源封堵狀态。true表示eip處于封堵狀态，false表示eip處于未封堵狀态
        :type IsBlocked: bool
        :param IsEipDirectConnection: eip是否支援直通模式。true表示eip支援直通模式，false表示資源不支援直通模式
        :type IsEipDirectConnection: bool
        :param AddressType: eip資源類型，包括"CalcIP","WanIP","EIP","AnycastEIP"。其中"CalcIP"表示設備ip，“WanIP”表示普通公網ip，“EIP”表示彈性公網ip，“AnycastEip”表示加速EIP
        :type AddressType: str
        :param CascadeRelease: eip是否在解綁後自動釋放。true表示eip将會在解綁後自動釋放，false表示eip在解綁後不會自動釋放
        :type CascadeRelease: bool
        :param EipAlgType: EIP ALG開啓的協議類型。
        :type EipAlgType: :class:`tencentcloud.vpc.v20170312.models.AlgType`
        :param InternetServiceProvider: 彈性公網IP的運營商訊息，當前可能返回值包括"CMCC","CTCC","CUCC","BGP"
        :type InternetServiceProvider: str
        """
        self.AddressId = None
        self.AddressName = None
        self.AddressStatus = None
        self.AddressIp = None
        self.InstanceId = None
        self.CreatedTime = None
        self.NetworkInterfaceId = None
        self.PrivateAddressIp = None
        self.IsArrears = None
        self.IsBlocked = None
        self.IsEipDirectConnection = None
        self.AddressType = None
        self.CascadeRelease = None
        self.EipAlgType = None
        self.InternetServiceProvider = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.AddressName = params.get("AddressName")
        self.AddressStatus = params.get("AddressStatus")
        self.AddressIp = params.get("AddressIp")
        self.InstanceId = params.get("InstanceId")
        self.CreatedTime = params.get("CreatedTime")
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.PrivateAddressIp = params.get("PrivateAddressIp")
        self.IsArrears = params.get("IsArrears")
        self.IsBlocked = params.get("IsBlocked")
        self.IsEipDirectConnection = params.get("IsEipDirectConnection")
        self.AddressType = params.get("AddressType")
        self.CascadeRelease = params.get("CascadeRelease")
        if params.get("EipAlgType") is not None:
            self.EipAlgType = AlgType()
            self.EipAlgType._deserialize(params.get("EipAlgType"))
        self.InternetServiceProvider = params.get("InternetServiceProvider")


class AddressChargePrepaid(AbstractModel):
    """用于描述彈性公網IP的費用對象

    """

    def __init__(self):
        """
        :param Period: 購買實例的時長
        :type Period: int
        :param RenewFlag: 自動續約标志
        :type RenewFlag: str
        """
        self.Period = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RenewFlag = params.get("RenewFlag")


class AddressTemplate(AbstractModel):
    """IP網址範本

    """

    def __init__(self):
        """
        :param AddressTemplateName: IP網址範本名稱。
        :type AddressTemplateName: str
        :param AddressTemplateId: IP網址範本實例唯一ID。
        :type AddressTemplateId: str
        :param AddressSet: IP網址訊息。
        :type AddressSet: list of str
        :param CreatedTime: 創建時間。
        :type CreatedTime: str
        """
        self.AddressTemplateName = None
        self.AddressTemplateId = None
        self.AddressSet = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.AddressTemplateName = params.get("AddressTemplateName")
        self.AddressTemplateId = params.get("AddressTemplateId")
        self.AddressSet = params.get("AddressSet")
        self.CreatedTime = params.get("CreatedTime")


class AddressTemplateGroup(AbstractModel):
    """IP網址範本集合

    """

    def __init__(self):
        """
        :param AddressTemplateGroupName: IP網址範本集合名稱。
        :type AddressTemplateGroupName: str
        :param AddressTemplateGroupId: IP網址範本集合實例ID，例如：ipmg-dih8xdbq。
        :type AddressTemplateGroupId: str
        :param AddressTemplateIdSet: IP網址範本ID。
        :type AddressTemplateIdSet: list of str
        :param CreatedTime: 創建時間。
        :type CreatedTime: str
        :param AddressTemplateSet: IP網址範本實例。
        :type AddressTemplateSet: list of AddressTemplateItem
        """
        self.AddressTemplateGroupName = None
        self.AddressTemplateGroupId = None
        self.AddressTemplateIdSet = None
        self.CreatedTime = None
        self.AddressTemplateSet = None


    def _deserialize(self, params):
        self.AddressTemplateGroupName = params.get("AddressTemplateGroupName")
        self.AddressTemplateGroupId = params.get("AddressTemplateGroupId")
        self.AddressTemplateIdSet = params.get("AddressTemplateIdSet")
        self.CreatedTime = params.get("CreatedTime")
        if params.get("AddressTemplateSet") is not None:
            self.AddressTemplateSet = []
            for item in params.get("AddressTemplateSet"):
                obj = AddressTemplateItem()
                obj._deserialize(item)
                self.AddressTemplateSet.append(obj)


class AddressTemplateItem(AbstractModel):
    """網址訊息

    """

    def __init__(self):
        """
        :param From: 起始網址。
        :type From: str
        :param To: 結束網址。
        :type To: str
        """
        self.From = None
        self.To = None


    def _deserialize(self, params):
        self.From = params.get("From")
        self.To = params.get("To")


class AddressTemplateSpecification(AbstractModel):
    """IP網址模版

    """

    def __init__(self):
        """
        :param AddressId: IP網址ID，例如：ipm-2uw6ujo6。
        :type AddressId: str
        :param AddressGroupId: IP網址組ID，例如：ipmg-2uw6ujo6。
        :type AddressGroupId: str
        """
        self.AddressId = None
        self.AddressGroupId = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.AddressGroupId = params.get("AddressGroupId")


class AlgType(AbstractModel):
    """ALG協議類型

    """

    def __init__(self):
        """
        :param Ftp: Ftp協議Alg功能是否開啓
        :type Ftp: bool
        :param Sip: Sip協議Alg功能是否開啓
        :type Sip: bool
        """
        self.Ftp = None
        self.Sip = None


    def _deserialize(self, params):
        self.Ftp = params.get("Ftp")
        self.Sip = params.get("Sip")


class AllocateAddressesRequest(AbstractModel):
    """AllocateAddresses請求參數結構體

    """

    def __init__(self):
        """
        :param AddressCount: EIP數量。預設值：1。
        :type AddressCount: int
        :param InternetServiceProvider: EIP線路類型。預設值：BGP。
<ul style="margin:0"><li>已開通靜态單線IP白名單的用戶，可選值：<ul><li>CMCC：中國移動</li>
<li>CTCC：中國電信</li>
<li>CUCC：中國聯通</li></ul>注意：僅部分地域支援靜态單線IP。</li></ul>
        :type InternetServiceProvider: str
        :param InternetChargeType: EIP計費方式。
<ul style="margin:0"><li>已開通頻寬上移白名單的用戶，可選值：<ul><li>BANDWIDTH_PACKAGE：[共享頻寬包](https://cloud.tencent.com/document/product/684/15255)付費（需額外開通共享頻寬包白名單）</li>
<li>BANDWIDTH_POSTPAID_BY_HOUR：頻寬按小時後付費</li>
<li>TRAFFIC_POSTPAID_BY_HOUR：流量按小時後付費</li></ul>預設值：TRAFFIC_POSTPAID_BY_HOUR。</li>
<li>未開通頻寬上移白名單的用戶，EIP計費方式與其綁定的實例的計費方式一緻，無需傳遞此參數。</li></ul>
        :type InternetChargeType: str
        :param InternetMaxBandwidthOut: EIP出頻寬上限，單位：Mbps。
<ul style="margin:0"><li>已開通頻寬上移白名單的用戶，可選值範圍取決于EIP計費方式：<ul><li>BANDWIDTH_PACKAGE：1 Mbps 至 1000 Mbps</li>
<li>BANDWIDTH_POSTPAID_BY_HOUR：1 Mbps 至 100 Mbps</li>
<li>TRAFFIC_POSTPAID_BY_HOUR：1 Mbps 至 100 Mbps</li></ul>預設值：1 Mbps。</li>
<li>未開通頻寬上移白名單的用戶，EIP出頻寬上限取決于與其綁定的實例的公網出頻寬上限，無需傳遞此參數。</li></ul>
        :type InternetMaxBandwidthOut: int
        :param AddressType: EIP類型。預設值：EIP。
<ul style="margin:0"><li>已開通Anycast公網加速白名單的用戶，可選值：<ul><li>AnycastEIP：加速IP，可參見 [Anycast 公網加速](https://cloud.tencent.com/document/product/644)</li></ul>注意：僅部分地域支援加速IP。</li></ul>
        :type AddressType: str
        :param AnycastZone: Anycast發布域。
<ul style="margin:0"><li>已開通Anycast公網加速白名單的用戶，可選值：<ul><li>ANYCAST_ZONE_GLOBAL：全球發布域（需要額外開通Anycast全球加速白名單）</li><li>ANYCAST_ZONE_OVERSEAS：境外發布域</li><li><b>[已廢棄]</b> ANYCAST_ZONE_A：發布域A（已更新爲全球發布域）</li><li><b>[已廢棄]</b> ANYCAST_ZONE_B：發布域B（已更新爲全球發布域）</li></ul>預設值：ANYCAST_ZONE_OVERSEAS。</li></ul>
        :type AnycastZone: str
        :param ApplicableForCLB: <b>[已廢棄]</b> AnycastEIP不再區分是否負載均衡。原參數說明如下：
AnycastEIP是否用于綁定負載均衡。
<ul style="margin:0"><li>已開通Anycast公網加速白名單的用戶，可選值：<ul><li>TRUE：AnycastEIP可綁定對象爲負載均衡</li>
<li>FALSE：AnycastEIP可綁定對象爲雲伺服器、NAT閘道、高可用虛拟IP等</li></ul>預設值：FALSE。</li></ul>
        :type ApplicableForCLB: bool
        :param Tags: 需要關聯的标簽清單。
        :type Tags: list of Tag
        :param BandwidthPackageId: BGP頻寬包唯一ID參數。設定該參數且InternetChargeType爲BANDWIDTH_PACKAGE，則表示創建的EIP加入該BGP頻寬包并采用頻寬包計費
        :type BandwidthPackageId: str
        """
        self.AddressCount = None
        self.InternetServiceProvider = None
        self.InternetChargeType = None
        self.InternetMaxBandwidthOut = None
        self.AddressType = None
        self.AnycastZone = None
        self.ApplicableForCLB = None
        self.Tags = None
        self.BandwidthPackageId = None


    def _deserialize(self, params):
        self.AddressCount = params.get("AddressCount")
        self.InternetServiceProvider = params.get("InternetServiceProvider")
        self.InternetChargeType = params.get("InternetChargeType")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.AddressType = params.get("AddressType")
        self.AnycastZone = params.get("AnycastZone")
        self.ApplicableForCLB = params.get("ApplicableForCLB")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.BandwidthPackageId = params.get("BandwidthPackageId")


class AllocateAddressesResponse(AbstractModel):
    """AllocateAddresses返回參數結構體

    """

    def __init__(self):
        """
        :param AddressSet: 申請到的 EIP 的唯一 ID 清單。
        :type AddressSet: list of str
        :param TaskId: 異步任務TaskId。可以使用[DescribeTaskResult](https://cloud.tencent.com/document/api/215/36271)介面查詢任務狀态。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AddressSet = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AddressSet = params.get("AddressSet")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class AllocateIp6AddressesBandwidthRequest(AbstractModel):
    """AllocateIp6AddressesBandwidth請求參數結構體

    """

    def __init__(self):
        """
        :param Ip6Addresses: 需要開通公網訪問能力的IPV6網址
        :type Ip6Addresses: list of str
        :param InternetMaxBandwidthOut: 頻寬，單位Mbps。預設是1Mbps
        :type InternetMaxBandwidthOut: int
        :param InternetChargeType: 網絡計費模式。IPV6當前支援"TRAFFIC_POSTPAID_BY_HOUR"，預設是"TRAFFIC_POSTPAID_BY_HOUR"。
        :type InternetChargeType: str
        """
        self.Ip6Addresses = None
        self.InternetMaxBandwidthOut = None
        self.InternetChargeType = None


    def _deserialize(self, params):
        self.Ip6Addresses = params.get("Ip6Addresses")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.InternetChargeType = params.get("InternetChargeType")


class AllocateIp6AddressesBandwidthResponse(AbstractModel):
    """AllocateIp6AddressesBandwidth返回參數結構體

    """

    def __init__(self):
        """
        :param AddressSet: 彈性公網 IPV6 的唯一 ID 清單。
        :type AddressSet: list of str
        :param TaskId: 異步任務TaskId。可以使用[DescribeTaskResult](https://cloud.tencent.com/document/api/215/36271)介面查詢任務狀态。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AddressSet = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AddressSet = params.get("AddressSet")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class AssignIpv6AddressesRequest(AbstractModel):
    """AssignIpv6Addresses請求參數結構體

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 彈性網卡實例`ID`，形如：`eni-m6dyj72l`。
        :type NetworkInterfaceId: str
        :param Ipv6Addresses: 指定的`IPv6`網址清單，單次最多指定10個。與入參`Ipv6AddressCount`合并計算配額。與Ipv6AddressCount必填一個。
        :type Ipv6Addresses: list of Ipv6Address
        :param Ipv6AddressCount: 自動分配`IPv6`網址個數，内網IP網址個數總和不能超過配數。與入參`Ipv6Addresses`合并計算配額。與Ipv6Addresses必填一個。
        :type Ipv6AddressCount: int
        """
        self.NetworkInterfaceId = None
        self.Ipv6Addresses = None
        self.Ipv6AddressCount = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("Ipv6Addresses") is not None:
            self.Ipv6Addresses = []
            for item in params.get("Ipv6Addresses"):
                obj = Ipv6Address()
                obj._deserialize(item)
                self.Ipv6Addresses.append(obj)
        self.Ipv6AddressCount = params.get("Ipv6AddressCount")


class AssignIpv6AddressesResponse(AbstractModel):
    """AssignIpv6Addresses返回參數結構體

    """

    def __init__(self):
        """
        :param Ipv6AddressSet: 分配給彈性網卡的`IPv6`網址清單。
        :type Ipv6AddressSet: list of Ipv6Address
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Ipv6AddressSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Ipv6AddressSet") is not None:
            self.Ipv6AddressSet = []
            for item in params.get("Ipv6AddressSet"):
                obj = Ipv6Address()
                obj._deserialize(item)
                self.Ipv6AddressSet.append(obj)
        self.RequestId = params.get("RequestId")


class AssignIpv6CidrBlockRequest(AbstractModel):
    """AssignIpv6CidrBlock請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: `VPC`實例`ID`，形如：`vpc-f49l6u0z`。
        :type VpcId: str
        """
        self.VpcId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")


class AssignIpv6CidrBlockResponse(AbstractModel):
    """AssignIpv6CidrBlock返回參數結構體

    """

    def __init__(self):
        """
        :param Ipv6CidrBlock: 分配的 `IPv6` 網段。形如：`3402:4e00:20:1000::/56`
        :type Ipv6CidrBlock: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Ipv6CidrBlock = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        self.RequestId = params.get("RequestId")


class AssignIpv6SubnetCidrBlockRequest(AbstractModel):
    """AssignIpv6SubnetCidrBlock請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: 子網所在私有網絡`ID`。形如：`vpc-f49l6u0z`。
        :type VpcId: str
        :param Ipv6SubnetCidrBlocks: 分配 `IPv6` 子網段清單。
        :type Ipv6SubnetCidrBlocks: list of Ipv6SubnetCidrBlock
        """
        self.VpcId = None
        self.Ipv6SubnetCidrBlocks = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        if params.get("Ipv6SubnetCidrBlocks") is not None:
            self.Ipv6SubnetCidrBlocks = []
            for item in params.get("Ipv6SubnetCidrBlocks"):
                obj = Ipv6SubnetCidrBlock()
                obj._deserialize(item)
                self.Ipv6SubnetCidrBlocks.append(obj)


class AssignIpv6SubnetCidrBlockResponse(AbstractModel):
    """AssignIpv6SubnetCidrBlock返回參數結構體

    """

    def __init__(self):
        """
        :param Ipv6SubnetCidrBlockSet: 分配 `IPv6` 子網段清單。
        :type Ipv6SubnetCidrBlockSet: list of Ipv6SubnetCidrBlock
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Ipv6SubnetCidrBlockSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Ipv6SubnetCidrBlockSet") is not None:
            self.Ipv6SubnetCidrBlockSet = []
            for item in params.get("Ipv6SubnetCidrBlockSet"):
                obj = Ipv6SubnetCidrBlock()
                obj._deserialize(item)
                self.Ipv6SubnetCidrBlockSet.append(obj)
        self.RequestId = params.get("RequestId")


class AssignPrivateIpAddressesRequest(AbstractModel):
    """AssignPrivateIpAddresses請求參數結構體

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 彈性網卡實例ID，例如：eni-m6dyj72l。
        :type NetworkInterfaceId: str
        :param PrivateIpAddresses: 指定的内網IP訊息，單次最多指定10個。與SecondaryPrivateIpAddressCount至少提供一個。
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        :param SecondaryPrivateIpAddressCount: 新申請的内網IP網址個數，與PrivateIpAddresses至少提供一個。内網IP網址個數總和不能超過配額數，詳見<a href="/document/product/576/18527">彈性網卡使用限制</a>。
        :type SecondaryPrivateIpAddressCount: int
        """
        self.NetworkInterfaceId = None
        self.PrivateIpAddresses = None
        self.SecondaryPrivateIpAddressCount = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("PrivateIpAddresses") is not None:
            self.PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self.PrivateIpAddresses.append(obj)
        self.SecondaryPrivateIpAddressCount = params.get("SecondaryPrivateIpAddressCount")


class AssignPrivateIpAddressesResponse(AbstractModel):
    """AssignPrivateIpAddresses返回參數結構體

    """

    def __init__(self):
        """
        :param PrivateIpAddressSet: 内網IP詳細訊息。
        :type PrivateIpAddressSet: list of PrivateIpAddressSpecification
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PrivateIpAddressSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PrivateIpAddressSet") is not None:
            self.PrivateIpAddressSet = []
            for item in params.get("PrivateIpAddressSet"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self.PrivateIpAddressSet.append(obj)
        self.RequestId = params.get("RequestId")


class AssistantCidr(AbstractModel):
    """VPC輔助CIDR訊息。

    """

    def __init__(self):
        """
        :param VpcId: `VPC`實例`ID`。形如：`vpc-6v2ht8q5`
        :type VpcId: str
        :param CidrBlock: 輔助CIDR。形如：`172.16.0.0/16`
        :type CidrBlock: str
        :param AssistantType: 輔助CIDR類型（0：普通輔助CIDR，1：容器輔助CIDR），預設都是0。
        :type AssistantType: int
        :param SubnetSet: 輔助CIDR拆分的子網。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubnetSet: list of Subnet
        """
        self.VpcId = None
        self.CidrBlock = None
        self.AssistantType = None
        self.SubnetSet = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.CidrBlock = params.get("CidrBlock")
        self.AssistantType = params.get("AssistantType")
        if params.get("SubnetSet") is not None:
            self.SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = Subnet()
                obj._deserialize(item)
                self.SubnetSet.append(obj)


class AssociateAddressRequest(AbstractModel):
    """AssociateAddress請求參數結構體

    """

    def __init__(self):
        """
        :param AddressId: 标識 EIP 的唯一 ID。EIP 唯一 ID 形如：`eip-11112222`。
        :type AddressId: str
        :param InstanceId: 要綁定的實例 ID。實例 ID 形如：`ins-11112222`。可通過登入[控制台](https://console.cloud.tencent.com/cvm)查詢，也可通過 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) 介面返回值中的`InstanceId`獲取。
        :type InstanceId: str
        :param NetworkInterfaceId: 要綁定的彈性網卡 ID。 彈性網卡 ID 形如：`eni-11112222`。`NetworkInterfaceId` 與 `InstanceId` 不可同時指定。彈性網卡 ID 可通過登入[控制台](https://console.cloud.tencent.com/vpc/eni)查詢，也可通過[DescribeNetworkInterfaces](https://cloud.tencent.com/document/api/215/15817)介面返回值中的`networkInterfaceId`獲取。
        :type NetworkInterfaceId: str
        :param PrivateIpAddress: 要綁定的内網 IP。如果指定了 `NetworkInterfaceId` 則也必須指定 `PrivateIpAddress` ，表示将 EIP 綁定到指定彈性網卡的指定内網 IP 上。同時要确保指定的 `PrivateIpAddress` 是指定的 `NetworkInterfaceId` 上的一個内網 IP。指定彈性網卡的内網 IP 可通過登入[控制台](https://console.cloud.tencent.com/vpc/eni)查詢，也可通過[DescribeNetworkInterfaces](https://cloud.tencent.com/document/api/215/15817)介面返回值中的`privateIpAddress`獲取。
        :type PrivateIpAddress: str
        """
        self.AddressId = None
        self.InstanceId = None
        self.NetworkInterfaceId = None
        self.PrivateIpAddress = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.InstanceId = params.get("InstanceId")
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.PrivateIpAddress = params.get("PrivateIpAddress")


class AssociateAddressResponse(AbstractModel):
    """AssociateAddress返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步任務TaskId。可以使用[DescribeTaskResult](https://cloud.tencent.com/document/api/215/36271)介面查詢任務狀态。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class AssociateNatGatewayAddressRequest(AbstractModel):
    """AssociateNatGatewayAddress請求參數結構體

    """

    def __init__(self):
        """
        :param NatGatewayId: NAT閘道的ID，形如：`nat-df45454`。
        :type NatGatewayId: str
        :param AddressCount: 需要申請的彈性IP個數，系統會按您的要求生産N個彈性IP, 其中AddressCount和PublicAddresses至少傳遞一個。
        :type AddressCount: int
        :param PublicIpAddresses: 綁定NAT閘道的彈性IP數組，其中AddressCount和PublicAddresses至少傳遞一個。。
        :type PublicIpAddresses: list of str
        :param Zone: 彈性IP可以區，自動分配彈性IP時傳遞。
        :type Zone: str
        """
        self.NatGatewayId = None
        self.AddressCount = None
        self.PublicIpAddresses = None
        self.Zone = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        self.AddressCount = params.get("AddressCount")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.Zone = params.get("Zone")


class AssociateNatGatewayAddressResponse(AbstractModel):
    """AssociateNatGatewayAddress返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AssociateNetworkAclSubnetsRequest(AbstractModel):
    """AssociateNetworkAclSubnets請求參數結構體

    """

    def __init__(self):
        """
        :param NetworkAclId: 網絡ACL實例ID。例如：acl-12345678。
        :type NetworkAclId: str
        :param SubnetIds: 子網實例ID數組。例如：[subnet-12345678]
        :type SubnetIds: list of str
        """
        self.NetworkAclId = None
        self.SubnetIds = None


    def _deserialize(self, params):
        self.NetworkAclId = params.get("NetworkAclId")
        self.SubnetIds = params.get("SubnetIds")


class AssociateNetworkAclSubnetsResponse(AbstractModel):
    """AssociateNetworkAclSubnets返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AssociateNetworkInterfaceSecurityGroupsRequest(AbstractModel):
    """AssociateNetworkInterfaceSecurityGroups請求參數結構體

    """

    def __init__(self):
        """
        :param NetworkInterfaceIds: 彈性網卡實例ID。形如：eni-pxir56ns。每次請求的實例的上限爲100。
        :type NetworkInterfaceIds: list of str
        :param SecurityGroupIds: 安全組實例ID，例如：sg-33ocnj9n，可通過DescribeSecurityGroups獲取。每次請求的實例的上限爲100。
        :type SecurityGroupIds: list of str
        """
        self.NetworkInterfaceIds = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.NetworkInterfaceIds = params.get("NetworkInterfaceIds")
        self.SecurityGroupIds = params.get("SecurityGroupIds")


class AssociateNetworkInterfaceSecurityGroupsResponse(AbstractModel):
    """AssociateNetworkInterfaceSecurityGroups返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachCcnInstancesRequest(AbstractModel):
    """AttachCcnInstances請求參數結構體

    """

    def __init__(self):
        """
        :param CcnId: CCN實例ID。形如：ccn-f49l6u0z。
        :type CcnId: str
        :param Instances: 關聯網絡實例清單
        :type Instances: list of CcnInstance
        :param CcnUin: CCN所屬UIN（根賬号），預設當前賬号所屬UIN
        :type CcnUin: str
        """
        self.CcnId = None
        self.Instances = None
        self.CcnUin = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = CcnInstance()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.CcnUin = params.get("CcnUin")


class AttachCcnInstancesResponse(AbstractModel):
    """AttachCcnInstances返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachClassicLinkVpcRequest(AbstractModel):
    """AttachClassicLinkVpc請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: VPC實例ID
        :type VpcId: str
        :param InstanceIds: CVM實例ID
        :type InstanceIds: list of str
        """
        self.VpcId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.InstanceIds = params.get("InstanceIds")


class AttachClassicLinkVpcResponse(AbstractModel):
    """AttachClassicLinkVpc返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachNetworkInterfaceRequest(AbstractModel):
    """AttachNetworkInterface請求參數結構體

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 彈性網卡實例ID，例如：eni-m6dyj72l。
        :type NetworkInterfaceId: str
        :param InstanceId: CVM實例ID。形如：ins-r8hr2upy。
        :type InstanceId: str
        """
        self.NetworkInterfaceId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.InstanceId = params.get("InstanceId")


class AttachNetworkInterfaceResponse(AbstractModel):
    """AttachNetworkInterface返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BandwidthPackage(AbstractModel):
    """描述頻寬包訊息的結構

    """

    def __init__(self):
        """
        :param BandwidthPackageId: 頻寬包唯一标識Id
        :type BandwidthPackageId: str
        :param NetworkType: 頻寬包類型，包括'BGP','SINGLEISP','ANYCAST'
        :type NetworkType: str
        :param ChargeType: 頻寬包計費類型，包括'TOP5_POSTPAID_BY_MONTH'和'PERCENT95_POSTPAID_BY_MONTH'
        :type ChargeType: str
        :param BandwidthPackageName: 頻寬包名稱
        :type BandwidthPackageName: str
        :param CreatedTime: 頻寬包創建時間。按照`ISO8601`标準表示，并且使用`UTC`時間。格式爲：`YYYY-MM-DDThh:mm:ssZ`。
        :type CreatedTime: str
        :param Status: 頻寬包狀态，包括'CREATING','CREATED','DELETING','DELETED'
        :type Status: str
        :param ResourceSet: 頻寬包資源訊息
        :type ResourceSet: list of Resource
        :param Bandwidth: 頻寬包限速大小。單位：Mbps，-1表示不限速。
        :type Bandwidth: int
        """
        self.BandwidthPackageId = None
        self.NetworkType = None
        self.ChargeType = None
        self.BandwidthPackageName = None
        self.CreatedTime = None
        self.Status = None
        self.ResourceSet = None
        self.Bandwidth = None


    def _deserialize(self, params):
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        self.NetworkType = params.get("NetworkType")
        self.ChargeType = params.get("ChargeType")
        self.BandwidthPackageName = params.get("BandwidthPackageName")
        self.CreatedTime = params.get("CreatedTime")
        self.Status = params.get("Status")
        if params.get("ResourceSet") is not None:
            self.ResourceSet = []
            for item in params.get("ResourceSet"):
                obj = Resource()
                obj._deserialize(item)
                self.ResourceSet.append(obj)
        self.Bandwidth = params.get("Bandwidth")


class CCN(AbstractModel):
    """雲聯網（CCN）對象

    """

    def __init__(self):
        """
        :param CcnId: 雲聯網唯一ID
        :type CcnId: str
        :param CcnName: 雲聯網名稱
        :type CcnName: str
        :param CcnDescription: 雲聯網描述訊息
        :type CcnDescription: str
        :param InstanceCount: 關聯實例數量
        :type InstanceCount: int
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param State: 實例狀态， 'ISOLATED': 隔離中（欠費停服），'AVAILABLE'：運作中。
        :type State: str
        :param QosLevel: 實例服務質量，’PT’：白金，'AU'：金，'AG'：銀。
        :type QosLevel: str
        :param InstanceChargeType: 付費類型，PREPAID爲預付費，POSTPAID爲後付費。
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceChargeType: str
        :param BandwidthLimitType: 限速類型，INTER_REGION_LIMIT爲地域間限速；OUTER_REGION_LIMIT爲地域出口限速。
注意：此欄位可能返回 null，表示取不到有效值。
        :type BandwidthLimitType: str
        :param TagSet: 标簽鍵值對。
        :type TagSet: list of Tag
        """
        self.CcnId = None
        self.CcnName = None
        self.CcnDescription = None
        self.InstanceCount = None
        self.CreateTime = None
        self.State = None
        self.QosLevel = None
        self.InstanceChargeType = None
        self.BandwidthLimitType = None
        self.TagSet = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.CcnName = params.get("CcnName")
        self.CcnDescription = params.get("CcnDescription")
        self.InstanceCount = params.get("InstanceCount")
        self.CreateTime = params.get("CreateTime")
        self.State = params.get("State")
        self.QosLevel = params.get("QosLevel")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.BandwidthLimitType = params.get("BandwidthLimitType")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)


class CcnAttachedInstance(AbstractModel):
    """雲聯網（CCN）關聯實例（Instance）對象

    """

    def __init__(self):
        """
        :param CcnId: 雲聯網實例ID。
        :type CcnId: str
        :param InstanceType: 關聯實例類型：
<li>`VPC`：私有網絡</li>
<li>`DIRECTCONNECT`：專線閘道</li>
<li>`BMVPC`：黑石私有網絡</li>
        :type InstanceType: str
        :param InstanceId: 關聯實例ID。
        :type InstanceId: str
        :param InstanceName: 關聯實例名稱。
        :type InstanceName: str
        :param InstanceRegion: 關聯實例所屬大區，例如：ap-guangzhou。
        :type InstanceRegion: str
        :param InstanceUin: 關聯實例所屬UIN（根賬号）。
        :type InstanceUin: str
        :param CidrBlock: 關聯實例CIDR。
        :type CidrBlock: list of str
        :param State: 關聯實例狀态：
<li>`PENDING`：申請中</li>
<li>`ACTIVE`：已連接</li>
<li>`EXPIRED`：已過期</li>
<li>`REJECTED`：已拒絕</li>
<li>`DELETED`：已删除</li>
<li>`FAILED`：失敗的（2小時後将異步強制解關聯）</li>
<li>`ATTACHING`：關聯中</li>
<li>`DETACHING`：解關聯中</li>
<li>`DETACHFAILED`：解關聯失敗（2小時後将異步強制解關聯）</li>
        :type State: str
        :param AttachedTime: 關聯時間。
        :type AttachedTime: str
        :param CcnUin: 雲聯網所屬UIN（根賬号）。
        :type CcnUin: str
        """
        self.CcnId = None
        self.InstanceType = None
        self.InstanceId = None
        self.InstanceName = None
        self.InstanceRegion = None
        self.InstanceUin = None
        self.CidrBlock = None
        self.State = None
        self.AttachedTime = None
        self.CcnUin = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.InstanceType = params.get("InstanceType")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.InstanceRegion = params.get("InstanceRegion")
        self.InstanceUin = params.get("InstanceUin")
        self.CidrBlock = params.get("CidrBlock")
        self.State = params.get("State")
        self.AttachedTime = params.get("AttachedTime")
        self.CcnUin = params.get("CcnUin")


class CcnInstance(AbstractModel):
    """雲聯網（CCN）關聯實例（Instance）對象。

    """

    def __init__(self):
        """
        :param InstanceId: 關聯實例ID。
        :type InstanceId: str
        :param InstanceRegion: 關聯實例ID所屬大區，例如：ap-guangzhou。
        :type InstanceRegion: str
        :param InstanceType: 關聯實例類型，可選值：
<li>`VPC`：私有網絡</li>
<li>`DIRECTCONNECT`：專線閘道</li>
<li>`BMVPC`：黑石私有網絡</li>
        :type InstanceType: str
        """
        self.InstanceId = None
        self.InstanceRegion = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceRegion = params.get("InstanceRegion")
        self.InstanceType = params.get("InstanceType")


class CcnRegionBandwidthLimit(AbstractModel):
    """雲聯網（CCN）地域出頻寬上限

    """

    def __init__(self):
        """
        :param Region: 地域，例如：ap-guangzhou
        :type Region: str
        :param BandwidthLimit: 出頻寬上限，單位：Mbps
        :type BandwidthLimit: int
        :param IsBm: 是否黑石地域，預設`false`。
        :type IsBm: bool
        :param DstRegion: 目的地域，例如：ap-shanghai
注意：此欄位可能返回 null，表示取不到有效值。
        :type DstRegion: str
        :param DstIsBm: 目的地域是否爲黑石地域，預設`false`。
        :type DstIsBm: bool
        """
        self.Region = None
        self.BandwidthLimit = None
        self.IsBm = None
        self.DstRegion = None
        self.DstIsBm = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.BandwidthLimit = params.get("BandwidthLimit")
        self.IsBm = params.get("IsBm")
        self.DstRegion = params.get("DstRegion")
        self.DstIsBm = params.get("DstIsBm")


class CcnRoute(AbstractModel):
    """CCN路由策略對象

    """

    def __init__(self):
        """
        :param RouteId: 路由策略ID
        :type RouteId: str
        :param DestinationCidrBlock: 目的端
        :type DestinationCidrBlock: str
        :param InstanceType: 下一跳類型（關聯實例類型），所有類型：VPC、DIRECTCONNECT
        :type InstanceType: str
        :param InstanceId: 下一跳（關聯實例）
        :type InstanceId: str
        :param InstanceName: 下一跳名稱（關聯實例名稱）
        :type InstanceName: str
        :param InstanceRegion: 下一跳所屬地域（關聯實例所屬地域）
        :type InstanceRegion: str
        :param UpdateTime: 更新時間
        :type UpdateTime: str
        :param Enabled: 路由是否啓用
        :type Enabled: bool
        :param InstanceUin: 關聯實例所屬UIN（根賬号）
        :type InstanceUin: str
        """
        self.RouteId = None
        self.DestinationCidrBlock = None
        self.InstanceType = None
        self.InstanceId = None
        self.InstanceName = None
        self.InstanceRegion = None
        self.UpdateTime = None
        self.Enabled = None
        self.InstanceUin = None


    def _deserialize(self, params):
        self.RouteId = params.get("RouteId")
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        self.InstanceType = params.get("InstanceType")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.InstanceRegion = params.get("InstanceRegion")
        self.UpdateTime = params.get("UpdateTime")
        self.Enabled = params.get("Enabled")
        self.InstanceUin = params.get("InstanceUin")


class CheckAssistantCidrRequest(AbstractModel):
    """CheckAssistantCidr請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: `VPC`實例`ID`。形如：`vpc-6v2ht8q5`
        :type VpcId: str
        :param NewCidrBlocks: 待添加的負載CIDR。CIDR數組，格式如["10.0.0.0/16", "172.16.0.0/16"]
        :type NewCidrBlocks: list of str
        :param OldCidrBlocks: 待删除的負載CIDR。CIDR數組，格式如["10.0.0.0/16", "172.16.0.0/16"]
        :type OldCidrBlocks: list of str
        """
        self.VpcId = None
        self.NewCidrBlocks = None
        self.OldCidrBlocks = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NewCidrBlocks = params.get("NewCidrBlocks")
        self.OldCidrBlocks = params.get("OldCidrBlocks")


class CheckAssistantCidrResponse(AbstractModel):
    """CheckAssistantCidr返回參數結構體

    """

    def __init__(self):
        """
        :param ConflictSourceSet: 沖突資源訊息數組。
        :type ConflictSourceSet: list of ConflictSource
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ConflictSourceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ConflictSourceSet") is not None:
            self.ConflictSourceSet = []
            for item in params.get("ConflictSourceSet"):
                obj = ConflictSource()
                obj._deserialize(item)
                self.ConflictSourceSet.append(obj)
        self.RequestId = params.get("RequestId")


class CheckDefaultSubnetRequest(AbstractModel):
    """CheckDefaultSubnet請求參數結構體

    """

    def __init__(self):
        """
        :param Zone: 子網所在的可用區ID，不同子網選擇不同可用區可以做跨可用區災備。
        :type Zone: str
        """
        self.Zone = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")


class CheckDefaultSubnetResponse(AbstractModel):
    """CheckDefaultSubnet返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 檢查結果。true爲可以創建預設子網，false爲不可以創建預設子網。
        :type Result: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CheckNetDetectStateRequest(AbstractModel):
    """CheckNetDetectState請求參數結構體

    """

    def __init__(self):
        """
        :param DetectDestinationIp: 探測目的IPv4網址數組，最多兩個。
        :type DetectDestinationIp: list of str
        :param NextHopType: 下一跳類型，目前我們支援的類型有：
VPN：VPN閘道；
DIRECTCONNECT：專線閘道；
PEERCONNECTION：對等連接；
NAT：NAT閘道；
NORMAL_CVM：普通雲伺服器；
        :type NextHopType: str
        :param NextHopDestination: 下一跳目的閘道，取值與“下一跳類型”相關：
下一跳類型爲VPN，取值VPN閘道ID，形如：vpngw-12345678；
下一跳類型爲DIRECTCONNECT，取值專線閘道ID，形如：dcg-12345678；
下一跳類型爲PEERCONNECTION，取值對等連接ID，形如：pcx-12345678；
下一跳類型爲NAT，取值Nat閘道，形如：nat-12345678；
下一跳類型爲NORMAL_CVM，取值雲伺服器IPv4網址，形如：10.0.0.12；
        :type NextHopDestination: str
        :param NetDetectId: 網絡探測實例ID。形如：netd-12345678。該參數與（VpcId，SubnetId，NetDetectName），至少要有一個。當NetDetectId存在時，使用NetDetectId。
        :type NetDetectId: str
        :param VpcId: `VPC`實例`ID`。形如：`vpc-12345678`。該參數與（SubnetId，NetDetectName）配合使用，與NetDetectId至少要有一個。當NetDetectId存在時，使用NetDetectId。
        :type VpcId: str
        :param SubnetId: 子網實例ID。形如：subnet-12345678。該參數與（VpcId，NetDetectName）配合使用，與NetDetectId至少要有一個。當NetDetectId存在時，使用NetDetectId。
        :type SubnetId: str
        :param NetDetectName: 網絡探測名稱，最大長度不能超過60個位元。該參數與（VpcId，SubnetId）配合使用，與NetDetectId至少要有一個。當NetDetectId存在時，使用NetDetectId。
        :type NetDetectName: str
        """
        self.DetectDestinationIp = None
        self.NextHopType = None
        self.NextHopDestination = None
        self.NetDetectId = None
        self.VpcId = None
        self.SubnetId = None
        self.NetDetectName = None


    def _deserialize(self, params):
        self.DetectDestinationIp = params.get("DetectDestinationIp")
        self.NextHopType = params.get("NextHopType")
        self.NextHopDestination = params.get("NextHopDestination")
        self.NetDetectId = params.get("NetDetectId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.NetDetectName = params.get("NetDetectName")


class CheckNetDetectStateResponse(AbstractModel):
    """CheckNetDetectState返回參數結構體

    """

    def __init__(self):
        """
        :param NetDetectIpStateSet: 網絡探測驗證結果對象數組。
        :type NetDetectIpStateSet: list of NetDetectIpState
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NetDetectIpStateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetDetectIpStateSet") is not None:
            self.NetDetectIpStateSet = []
            for item in params.get("NetDetectIpStateSet"):
                obj = NetDetectIpState()
                obj._deserialize(item)
                self.NetDetectIpStateSet.append(obj)
        self.RequestId = params.get("RequestId")


class ClassicLinkInstance(AbstractModel):
    """私有網絡和基礎網絡互通設備

    """

    def __init__(self):
        """
        :param VpcId: VPC實例ID
        :type VpcId: str
        :param InstanceId: 雲伺服器實例唯一ID
        :type InstanceId: str
        """
        self.VpcId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.InstanceId = params.get("InstanceId")


class ConflictItem(AbstractModel):
    """沖突資源條目訊息。

    """

    def __init__(self):
        """
        :param ConfilctId: 沖突資源的ID
        :type ConfilctId: str
        :param DestinationItem: 沖突目的資源
        :type DestinationItem: str
        """
        self.ConfilctId = None
        self.DestinationItem = None


    def _deserialize(self, params):
        self.ConfilctId = params.get("ConfilctId")
        self.DestinationItem = params.get("DestinationItem")


class ConflictSource(AbstractModel):
    """沖突資源訊息。

    """

    def __init__(self):
        """
        :param ConflictSourceId: 沖突資源ID
        :type ConflictSourceId: str
        :param SourceItem: 沖突資源
        :type SourceItem: str
        :param ConflictItemSet: 沖突資源條目訊息
        :type ConflictItemSet: list of ConflictItem
        """
        self.ConflictSourceId = None
        self.SourceItem = None
        self.ConflictItemSet = None


    def _deserialize(self, params):
        self.ConflictSourceId = params.get("ConflictSourceId")
        self.SourceItem = params.get("SourceItem")
        if params.get("ConflictItemSet") is not None:
            self.ConflictItemSet = []
            for item in params.get("ConflictItemSet"):
                obj = ConflictItem()
                obj._deserialize(item)
                self.ConflictItemSet.append(obj)


class CreateAddressTemplateGroupRequest(AbstractModel):
    """CreateAddressTemplateGroup請求參數結構體

    """

    def __init__(self):
        """
        :param AddressTemplateGroupName: IP網址模版集合名稱。
        :type AddressTemplateGroupName: str
        :param AddressTemplateIds: IP網址模版實例ID，例如：ipm-mdunqeb6。
        :type AddressTemplateIds: list of str
        """
        self.AddressTemplateGroupName = None
        self.AddressTemplateIds = None


    def _deserialize(self, params):
        self.AddressTemplateGroupName = params.get("AddressTemplateGroupName")
        self.AddressTemplateIds = params.get("AddressTemplateIds")


class CreateAddressTemplateGroupResponse(AbstractModel):
    """CreateAddressTemplateGroup返回參數結構體

    """

    def __init__(self):
        """
        :param AddressTemplateGroup: IP網址範本集合對象。
        :type AddressTemplateGroup: :class:`tencentcloud.vpc.v20170312.models.AddressTemplateGroup`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AddressTemplateGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AddressTemplateGroup") is not None:
            self.AddressTemplateGroup = AddressTemplateGroup()
            self.AddressTemplateGroup._deserialize(params.get("AddressTemplateGroup"))
        self.RequestId = params.get("RequestId")


class CreateAddressTemplateRequest(AbstractModel):
    """CreateAddressTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param AddressTemplateName: IP網址模版名稱
        :type AddressTemplateName: str
        :param Addresses: 網址訊息，支援 IP、CIDR、IP 範圍。
        :type Addresses: list of str
        """
        self.AddressTemplateName = None
        self.Addresses = None


    def _deserialize(self, params):
        self.AddressTemplateName = params.get("AddressTemplateName")
        self.Addresses = params.get("Addresses")


class CreateAddressTemplateResponse(AbstractModel):
    """CreateAddressTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param AddressTemplate: IP網址範本對象。
        :type AddressTemplate: :class:`tencentcloud.vpc.v20170312.models.AddressTemplate`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AddressTemplate = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AddressTemplate") is not None:
            self.AddressTemplate = AddressTemplate()
            self.AddressTemplate._deserialize(params.get("AddressTemplate"))
        self.RequestId = params.get("RequestId")


class CreateAndAttachNetworkInterfaceRequest(AbstractModel):
    """CreateAndAttachNetworkInterface請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: VPC實例ID。可通過DescribeVpcs介面返回值中的VpcId獲取。
        :type VpcId: str
        :param NetworkInterfaceName: 彈性網卡名稱，最大長度不能超過60個位元。
        :type NetworkInterfaceName: str
        :param SubnetId: 彈性網卡所在的子網實例ID，例如：subnet-0ap8nwca。
        :type SubnetId: str
        :param InstanceId: 雲主機實例ID。
        :type InstanceId: str
        :param PrivateIpAddresses: 指定的内網IP訊息，單次最多指定10個。
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        :param SecondaryPrivateIpAddressCount: 新申請的内網IP網址個數，内網IP網址個數總和不能超過配數。
        :type SecondaryPrivateIpAddressCount: int
        :param SecurityGroupIds: 指定綁定的安全組，例如：['sg-1dd51d']。
        :type SecurityGroupIds: list of str
        :param NetworkInterfaceDescription: 彈性網卡描述，可任意命名，但不得超過60個字元。
        :type NetworkInterfaceDescription: str
        :param Tags: 指定綁定的标簽清單，例如：[{"Key": "city", "Value": "shanghai"}]
        :type Tags: list of Tag
        """
        self.VpcId = None
        self.NetworkInterfaceName = None
        self.SubnetId = None
        self.InstanceId = None
        self.PrivateIpAddresses = None
        self.SecondaryPrivateIpAddressCount = None
        self.SecurityGroupIds = None
        self.NetworkInterfaceDescription = None
        self.Tags = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NetworkInterfaceName = params.get("NetworkInterfaceName")
        self.SubnetId = params.get("SubnetId")
        self.InstanceId = params.get("InstanceId")
        if params.get("PrivateIpAddresses") is not None:
            self.PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self.PrivateIpAddresses.append(obj)
        self.SecondaryPrivateIpAddressCount = params.get("SecondaryPrivateIpAddressCount")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.NetworkInterfaceDescription = params.get("NetworkInterfaceDescription")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateAndAttachNetworkInterfaceResponse(AbstractModel):
    """CreateAndAttachNetworkInterface返回參數結構體

    """

    def __init__(self):
        """
        :param NetworkInterface: 彈性網卡實例。
        :type NetworkInterface: :class:`tencentcloud.vpc.v20170312.models.NetworkInterface`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NetworkInterface = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetworkInterface") is not None:
            self.NetworkInterface = NetworkInterface()
            self.NetworkInterface._deserialize(params.get("NetworkInterface"))
        self.RequestId = params.get("RequestId")


class CreateAssistantCidrRequest(AbstractModel):
    """CreateAssistantCidr請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: `VPC`實例`ID`。形如：`vpc-6v2ht8q5`
        :type VpcId: str
        :param CidrBlocks: CIDR數組，格式如["10.0.0.0/16", "172.16.0.0/16"]
        :type CidrBlocks: list of str
        """
        self.VpcId = None
        self.CidrBlocks = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.CidrBlocks = params.get("CidrBlocks")


class CreateAssistantCidrResponse(AbstractModel):
    """CreateAssistantCidr返回參數結構體

    """

    def __init__(self):
        """
        :param AssistantCidrSet: 輔助CIDR數組。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AssistantCidrSet: list of AssistantCidr
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AssistantCidrSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AssistantCidrSet") is not None:
            self.AssistantCidrSet = []
            for item in params.get("AssistantCidrSet"):
                obj = AssistantCidr()
                obj._deserialize(item)
                self.AssistantCidrSet.append(obj)
        self.RequestId = params.get("RequestId")


class CreateBandwidthPackageRequest(AbstractModel):
    """CreateBandwidthPackage請求參數結構體

    """

    def __init__(self):
        """
        :param NetworkType: 頻寬包類型，包括'BGP'，'SINGLEISP'，'ANYCAST'
        :type NetworkType: str
        :param ChargeType: 頻寬包計費類型，包括‘TOP5_POSTPAID_BY_MONTH’，‘PERCENT95_POSTPAID_BY_MONTH’
        :type ChargeType: str
        :param BandwidthPackageName: 頻寬包名字
        :type BandwidthPackageName: str
        :param BandwidthPackageCount: 頻寬包數量(非上移帳戶只能填1)
        :type BandwidthPackageCount: int
        :param InternetMaxBandwidth: 頻寬包限速大小。單位：Mbps，-1表示不限速。
        :type InternetMaxBandwidth: int
        :param Tags: 需要關聯的标簽清單。
        :type Tags: list of Tag
        :param Protocol: 頻寬包協議類型。當前支援'ipv4'和'ipv6'協議頻寬包，預設值是'ipv4'。
        :type Protocol: str
        """
        self.NetworkType = None
        self.ChargeType = None
        self.BandwidthPackageName = None
        self.BandwidthPackageCount = None
        self.InternetMaxBandwidth = None
        self.Tags = None
        self.Protocol = None


    def _deserialize(self, params):
        self.NetworkType = params.get("NetworkType")
        self.ChargeType = params.get("ChargeType")
        self.BandwidthPackageName = params.get("BandwidthPackageName")
        self.BandwidthPackageCount = params.get("BandwidthPackageCount")
        self.InternetMaxBandwidth = params.get("InternetMaxBandwidth")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Protocol = params.get("Protocol")


class CreateBandwidthPackageResponse(AbstractModel):
    """CreateBandwidthPackage返回參數結構體

    """

    def __init__(self):
        """
        :param BandwidthPackageId: 頻寬包唯一ID
        :type BandwidthPackageId: str
        :param BandwidthPackageIds: 頻寬包唯一ID清單(申請數量大于1時有效)
        :type BandwidthPackageIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.BandwidthPackageId = None
        self.BandwidthPackageIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        self.BandwidthPackageIds = params.get("BandwidthPackageIds")
        self.RequestId = params.get("RequestId")


class CreateCcnRequest(AbstractModel):
    """CreateCcn請求參數結構體

    """

    def __init__(self):
        """
        :param CcnName: CCN名稱，最大長度不能超過60個位元。
        :type CcnName: str
        :param CcnDescription: CCN描述訊息，最大長度不能超過100個位元。
        :type CcnDescription: str
        :param QosLevel: CCN服務質量，'PT'：白金，'AU'：金，'AG'：銀，預設爲‘AU’。
        :type QosLevel: str
        :param InstanceChargeType: 計費模式，PREPAID：表示預付費，即包年包月，POSTPAID：表示後付費，即按量計費。預設：POSTPAID。
        :type InstanceChargeType: str
        :param BandwidthLimitType: 限速類型，OUTER_REGION_LIMIT表示地域出口限速，INTER_REGION_LIMIT爲地域間限速，預設爲OUTER_REGION_LIMIT
        :type BandwidthLimitType: str
        :param Tags: 指定綁定的标簽清單，例如：[{"Key": "city", "Value": "shanghai"}]
        :type Tags: list of Tag
        """
        self.CcnName = None
        self.CcnDescription = None
        self.QosLevel = None
        self.InstanceChargeType = None
        self.BandwidthLimitType = None
        self.Tags = None


    def _deserialize(self, params):
        self.CcnName = params.get("CcnName")
        self.CcnDescription = params.get("CcnDescription")
        self.QosLevel = params.get("QosLevel")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.BandwidthLimitType = params.get("BandwidthLimitType")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateCcnResponse(AbstractModel):
    """CreateCcn返回參數結構體

    """

    def __init__(self):
        """
        :param Ccn: 雲聯網（CCN）對象。
        :type Ccn: :class:`tencentcloud.vpc.v20170312.models.CCN`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Ccn = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Ccn") is not None:
            self.Ccn = CCN()
            self.Ccn._deserialize(params.get("Ccn"))
        self.RequestId = params.get("RequestId")


class CreateCustomerGatewayRequest(AbstractModel):
    """CreateCustomerGateway請求參數結構體

    """

    def __init__(self):
        """
        :param CustomerGatewayName: 對端閘道名稱，可任意命名，但不得超過60個字元。
        :type CustomerGatewayName: str
        :param IpAddress: 對端閘道公網IP。
        :type IpAddress: str
        """
        self.CustomerGatewayName = None
        self.IpAddress = None


    def _deserialize(self, params):
        self.CustomerGatewayName = params.get("CustomerGatewayName")
        self.IpAddress = params.get("IpAddress")


class CreateCustomerGatewayResponse(AbstractModel):
    """CreateCustomerGateway返回參數結構體

    """

    def __init__(self):
        """
        :param CustomerGateway: 對端閘道對象
        :type CustomerGateway: :class:`tencentcloud.vpc.v20170312.models.CustomerGateway`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CustomerGateway = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CustomerGateway") is not None:
            self.CustomerGateway = CustomerGateway()
            self.CustomerGateway._deserialize(params.get("CustomerGateway"))
        self.RequestId = params.get("RequestId")


class CreateDefaultSecurityGroupRequest(AbstractModel):
    """CreateDefaultSecurityGroup請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: 項目ID，預設0。可在qcloud控制台項目管理頁面查詢到。
        :type ProjectId: str
        """
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")


class CreateDefaultSecurityGroupResponse(AbstractModel):
    """CreateDefaultSecurityGroup返回參數結構體

    """

    def __init__(self):
        """
        :param SecurityGroup: 安全組對象。
        :type SecurityGroup: :class:`tencentcloud.vpc.v20170312.models.SecurityGroup`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SecurityGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroup") is not None:
            self.SecurityGroup = SecurityGroup()
            self.SecurityGroup._deserialize(params.get("SecurityGroup"))
        self.RequestId = params.get("RequestId")


class CreateDefaultVpcRequest(AbstractModel):
    """CreateDefaultVpc請求參數結構體

    """

    def __init__(self):
        """
        :param Zone: 子網所在的可用區ID，不指定将随機選擇可用區
        :type Zone: str
        :param Force: 是否強制返回預設VPC
        :type Force: bool
        """
        self.Zone = None
        self.Force = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.Force = params.get("Force")


class CreateDefaultVpcResponse(AbstractModel):
    """CreateDefaultVpc返回參數結構體

    """

    def __init__(self):
        """
        :param Vpc: 預設VPC和子網ID
        :type Vpc: :class:`tencentcloud.vpc.v20170312.models.DefaultVpcSubnet`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Vpc = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Vpc") is not None:
            self.Vpc = DefaultVpcSubnet()
            self.Vpc._deserialize(params.get("Vpc"))
        self.RequestId = params.get("RequestId")


class CreateDirectConnectGatewayCcnRoutesRequest(AbstractModel):
    """CreateDirectConnectGatewayCcnRoutes請求參數結構體

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: 專線閘道ID，形如：dcg-prpqlmg1
        :type DirectConnectGatewayId: str
        :param Routes: 需要連通的IDC網段清單
        :type Routes: list of DirectConnectGatewayCcnRoute
        """
        self.DirectConnectGatewayId = None
        self.Routes = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = DirectConnectGatewayCcnRoute()
                obj._deserialize(item)
                self.Routes.append(obj)


class CreateDirectConnectGatewayCcnRoutesResponse(AbstractModel):
    """CreateDirectConnectGatewayCcnRoutes返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDirectConnectGatewayRequest(AbstractModel):
    """CreateDirectConnectGateway請求參數結構體

    """

    def __init__(self):
        """
        :param DirectConnectGatewayName: 專線閘道名稱
        :type DirectConnectGatewayName: str
        :param NetworkType: 關聯網絡類型，可選值：
<li>VPC - 私有網絡</li>
<li>CCN - 雲聯網</li>
        :type NetworkType: str
        :param NetworkInstanceId: <li>NetworkType 爲 VPC 時，這裏傳值爲私有網絡實例ID</li>
<li>NetworkType 爲 CCN 時，這裏傳值爲雲聯網實例ID</li>
        :type NetworkInstanceId: str
        :param GatewayType: 閘道類型，可選值：
<li>NORMAL - （預設）标準型，注：雲聯網只支援标準型</li>
<li>NAT - NAT型</li>NAT類型支援網絡網址轉換配置，類型确定後不能修改；一個私有網絡可以創建一個NAT類型的專線閘道和一個非NAT類型的專線閘道
        :type GatewayType: str
        """
        self.DirectConnectGatewayName = None
        self.NetworkType = None
        self.NetworkInstanceId = None
        self.GatewayType = None


    def _deserialize(self, params):
        self.DirectConnectGatewayName = params.get("DirectConnectGatewayName")
        self.NetworkType = params.get("NetworkType")
        self.NetworkInstanceId = params.get("NetworkInstanceId")
        self.GatewayType = params.get("GatewayType")


class CreateDirectConnectGatewayResponse(AbstractModel):
    """CreateDirectConnectGateway返回參數結構體

    """

    def __init__(self):
        """
        :param DirectConnectGateway: 專線閘道對象。
        :type DirectConnectGateway: :class:`tencentcloud.vpc.v20170312.models.DirectConnectGateway`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DirectConnectGateway = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DirectConnectGateway") is not None:
            self.DirectConnectGateway = DirectConnectGateway()
            self.DirectConnectGateway._deserialize(params.get("DirectConnectGateway"))
        self.RequestId = params.get("RequestId")


class CreateFlowLogRequest(AbstractModel):
    """CreateFlowLog請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: 私用網絡ID或者統一ID，建議使用統一ID
        :type VpcId: str
        :param FlowLogName: 流日志實例名字
        :type FlowLogName: str
        :param ResourceType: 流日志所屬資源類型，VPC|SUBNET|NETWORKINTERFACE
        :type ResourceType: str
        :param ResourceId: 資源唯一ID
        :type ResourceId: str
        :param TrafficType: 流日志采集類型，ACCEPT|REJECT|ALL
        :type TrafficType: str
        :param CloudLogId: 流日志儲存ID
        :type CloudLogId: str
        :param FlowLogDescription: 流日志實例描述
        :type FlowLogDescription: str
        """
        self.VpcId = None
        self.FlowLogName = None
        self.ResourceType = None
        self.ResourceId = None
        self.TrafficType = None
        self.CloudLogId = None
        self.FlowLogDescription = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.FlowLogName = params.get("FlowLogName")
        self.ResourceType = params.get("ResourceType")
        self.ResourceId = params.get("ResourceId")
        self.TrafficType = params.get("TrafficType")
        self.CloudLogId = params.get("CloudLogId")
        self.FlowLogDescription = params.get("FlowLogDescription")


class CreateFlowLogResponse(AbstractModel):
    """CreateFlowLog返回參數結構體

    """

    def __init__(self):
        """
        :param FlowLog: 創建的流日志訊息
        :type FlowLog: list of FlowLog
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FlowLog = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FlowLog") is not None:
            self.FlowLog = []
            for item in params.get("FlowLog"):
                obj = FlowLog()
                obj._deserialize(item)
                self.FlowLog.append(obj)
        self.RequestId = params.get("RequestId")


class CreateHaVipRequest(AbstractModel):
    """CreateHaVip請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: `HAVIP`所在私有網絡`ID`。
        :type VpcId: str
        :param SubnetId: `HAVIP`所在子網`ID`。
        :type SubnetId: str
        :param HaVipName: `HAVIP`名稱。
        :type HaVipName: str
        :param Vip: 指定虛拟IP網址，必須在`VPC`網段内且未被占用。不指定則自動分配。
        :type Vip: str
        """
        self.VpcId = None
        self.SubnetId = None
        self.HaVipName = None
        self.Vip = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.HaVipName = params.get("HaVipName")
        self.Vip = params.get("Vip")


class CreateHaVipResponse(AbstractModel):
    """CreateHaVip返回參數結構體

    """

    def __init__(self):
        """
        :param HaVip: `HAVIP`對象。
        :type HaVip: :class:`tencentcloud.vpc.v20170312.models.HaVip`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.HaVip = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HaVip") is not None:
            self.HaVip = HaVip()
            self.HaVip._deserialize(params.get("HaVip"))
        self.RequestId = params.get("RequestId")


class CreateIp6TranslatorsRequest(AbstractModel):
    """CreateIp6Translators請求參數結構體

    """

    def __init__(self):
        """
        :param Ip6TranslatorName: 轉換實例名稱
        :type Ip6TranslatorName: str
        :param Ip6TranslatorCount: 創建轉換實例數量，預設是1個
        :type Ip6TranslatorCount: int
        :param Ip6InternetServiceProvider: 轉換實例運營商屬性，可取"CMCC","CTCC","CUCC","BGP"
        :type Ip6InternetServiceProvider: str
        """
        self.Ip6TranslatorName = None
        self.Ip6TranslatorCount = None
        self.Ip6InternetServiceProvider = None


    def _deserialize(self, params):
        self.Ip6TranslatorName = params.get("Ip6TranslatorName")
        self.Ip6TranslatorCount = params.get("Ip6TranslatorCount")
        self.Ip6InternetServiceProvider = params.get("Ip6InternetServiceProvider")


class CreateIp6TranslatorsResponse(AbstractModel):
    """CreateIp6Translators返回參數結構體

    """

    def __init__(self):
        """
        :param Ip6TranslatorSet: 轉換實例的唯一ID數組，形如"ip6-xxxxxxxx"
        :type Ip6TranslatorSet: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Ip6TranslatorSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ip6TranslatorSet = params.get("Ip6TranslatorSet")
        self.RequestId = params.get("RequestId")


class CreateNatGatewayDestinationIpPortTranslationNatRuleRequest(AbstractModel):
    """CreateNatGatewayDestinationIpPortTranslationNatRule請求參數結構體

    """

    def __init__(self):
        """
        :param NatGatewayId: NAT閘道的ID，形如：`nat-df45454`。
        :type NatGatewayId: str
        :param DestinationIpPortTranslationNatRules: NAT閘道的端口轉換規則。
        :type DestinationIpPortTranslationNatRules: list of DestinationIpPortTranslationNatRule
        """
        self.NatGatewayId = None
        self.DestinationIpPortTranslationNatRules = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        if params.get("DestinationIpPortTranslationNatRules") is not None:
            self.DestinationIpPortTranslationNatRules = []
            for item in params.get("DestinationIpPortTranslationNatRules"):
                obj = DestinationIpPortTranslationNatRule()
                obj._deserialize(item)
                self.DestinationIpPortTranslationNatRules.append(obj)


class CreateNatGatewayDestinationIpPortTranslationNatRuleResponse(AbstractModel):
    """CreateNatGatewayDestinationIpPortTranslationNatRule返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateNatGatewayRequest(AbstractModel):
    """CreateNatGateway請求參數結構體

    """

    def __init__(self):
        """
        :param NatGatewayName: NAT閘道名稱
        :type NatGatewayName: str
        :param VpcId: VPC實例ID。可通過DescribeVpcs介面返回值中的VpcId獲取。
        :type VpcId: str
        :param InternetMaxBandwidthOut: NAT閘道最大外網出頻寬(單位:Mbps)，支援的參數值：`20, 50, 100, 200, 500, 1000, 2000, 5000`，預設: `100Mbps`。
        :type InternetMaxBandwidthOut: int
        :param MaxConcurrentConnection: NAT閘道并發連接上限，支援參數值：`1000000、3000000、10000000`，預設值爲`100000`。
        :type MaxConcurrentConnection: int
        :param AddressCount: 需要申請的彈性IP個數，系統會按您的要求生産N個彈性IP，其中AddressCount和PublicAddresses至少傳遞一個。
        :type AddressCount: int
        :param PublicIpAddresses: 綁定NAT閘道的彈性IP數組，其中AddressCount和PublicAddresses至少傳遞一個。
        :type PublicIpAddresses: list of str
        :param Zone: 可用區，形如：`ap-guangzhou-1`。
        :type Zone: str
        :param Tags: 指定綁定的标簽清單，例如：[{"Key": "city", "Value": "shanghai"}]
        :type Tags: list of Tag
        """
        self.NatGatewayName = None
        self.VpcId = None
        self.InternetMaxBandwidthOut = None
        self.MaxConcurrentConnection = None
        self.AddressCount = None
        self.PublicIpAddresses = None
        self.Zone = None
        self.Tags = None


    def _deserialize(self, params):
        self.NatGatewayName = params.get("NatGatewayName")
        self.VpcId = params.get("VpcId")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.MaxConcurrentConnection = params.get("MaxConcurrentConnection")
        self.AddressCount = params.get("AddressCount")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.Zone = params.get("Zone")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateNatGatewayResponse(AbstractModel):
    """CreateNatGateway返回參數結構體

    """

    def __init__(self):
        """
        :param NatGatewaySet: NAT閘道對象數組。
        :type NatGatewaySet: list of NatGateway
        :param TotalCount: 符合條件的 NAT閘道對象數量。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NatGatewaySet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NatGatewaySet") is not None:
            self.NatGatewaySet = []
            for item in params.get("NatGatewaySet"):
                obj = NatGateway()
                obj._deserialize(item)
                self.NatGatewaySet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class CreateNetDetectRequest(AbstractModel):
    """CreateNetDetect請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: `VPC`實例`ID`。形如：`vpc-12345678`
        :type VpcId: str
        :param SubnetId: 子網實例ID。形如：subnet-12345678。
        :type SubnetId: str
        :param NetDetectName: 網絡探測名稱，最大長度不能超過60個位元。
        :type NetDetectName: str
        :param DetectDestinationIp: 探測目的IPv4網址數組。最多兩個。
        :type DetectDestinationIp: list of str
        :param NextHopType: 下一跳類型，目前我們支援的類型有：
VPN：VPN閘道；
DIRECTCONNECT：專線閘道；
PEERCONNECTION：對等連接；
NAT：NAT閘道；
NORMAL_CVM：普通雲伺服器；
        :type NextHopType: str
        :param NextHopDestination: 下一跳目的閘道，取值與“下一跳類型”相關：
下一跳類型爲VPN，取值VPN閘道ID，形如：vpngw-12345678；
下一跳類型爲DIRECTCONNECT，取值專線閘道ID，形如：dcg-12345678；
下一跳類型爲PEERCONNECTION，取值對等連接ID，形如：pcx-12345678；
下一跳類型爲NAT，取值Nat閘道，形如：nat-12345678；
下一跳類型爲NORMAL_CVM，取值雲伺服器IPv4網址，形如：10.0.0.12；
        :type NextHopDestination: str
        :param NetDetectDescription: 網絡探測描述。
        :type NetDetectDescription: str
        """
        self.VpcId = None
        self.SubnetId = None
        self.NetDetectName = None
        self.DetectDestinationIp = None
        self.NextHopType = None
        self.NextHopDestination = None
        self.NetDetectDescription = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.NetDetectName = params.get("NetDetectName")
        self.DetectDestinationIp = params.get("DetectDestinationIp")
        self.NextHopType = params.get("NextHopType")
        self.NextHopDestination = params.get("NextHopDestination")
        self.NetDetectDescription = params.get("NetDetectDescription")


class CreateNetDetectResponse(AbstractModel):
    """CreateNetDetect返回參數結構體

    """

    def __init__(self):
        """
        :param NetDetect: 網絡探測（NetDetect）對象。
        :type NetDetect: :class:`tencentcloud.vpc.v20170312.models.NetDetect`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NetDetect = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetDetect") is not None:
            self.NetDetect = NetDetect()
            self.NetDetect._deserialize(params.get("NetDetect"))
        self.RequestId = params.get("RequestId")


class CreateNetworkAclRequest(AbstractModel):
    """CreateNetworkAcl請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: VPC實例ID。可通過DescribeVpcs介面返回值中的VpcId獲取。
        :type VpcId: str
        :param NetworkAclName: 網絡ACL名稱，最大長度不能超過60個位元。
        :type NetworkAclName: str
        """
        self.VpcId = None
        self.NetworkAclName = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NetworkAclName = params.get("NetworkAclName")


class CreateNetworkAclResponse(AbstractModel):
    """CreateNetworkAcl返回參數結構體

    """

    def __init__(self):
        """
        :param NetworkAcl: 網絡ACL實例。
        :type NetworkAcl: :class:`tencentcloud.vpc.v20170312.models.NetworkAcl`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NetworkAcl = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetworkAcl") is not None:
            self.NetworkAcl = NetworkAcl()
            self.NetworkAcl._deserialize(params.get("NetworkAcl"))
        self.RequestId = params.get("RequestId")


class CreateNetworkInterfaceRequest(AbstractModel):
    """CreateNetworkInterface請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: VPC實例ID。可通過DescribeVpcs介面返回值中的VpcId獲取。
        :type VpcId: str
        :param NetworkInterfaceName: 彈性網卡名稱，最大長度不能超過60個位元。
        :type NetworkInterfaceName: str
        :param SubnetId: 彈性網卡所在的子網實例ID，例如：subnet-0ap8nwca。
        :type SubnetId: str
        :param NetworkInterfaceDescription: 彈性網卡描述，可任意命名，但不得超過60個字元。
        :type NetworkInterfaceDescription: str
        :param SecondaryPrivateIpAddressCount: 新申請的内網IP網址個數，内網IP網址個數總和不能超過配數。
        :type SecondaryPrivateIpAddressCount: int
        :param SecurityGroupIds: 指定綁定的安全組，例如：['sg-1dd51d']。
        :type SecurityGroupIds: list of str
        :param PrivateIpAddresses: 指定的内網IP訊息，單次最多指定10個。
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        :param Tags: 指定綁定的标簽清單，例如：[{"Key": "city", "Value": "shanghai"}]
        :type Tags: list of Tag
        """
        self.VpcId = None
        self.NetworkInterfaceName = None
        self.SubnetId = None
        self.NetworkInterfaceDescription = None
        self.SecondaryPrivateIpAddressCount = None
        self.SecurityGroupIds = None
        self.PrivateIpAddresses = None
        self.Tags = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NetworkInterfaceName = params.get("NetworkInterfaceName")
        self.SubnetId = params.get("SubnetId")
        self.NetworkInterfaceDescription = params.get("NetworkInterfaceDescription")
        self.SecondaryPrivateIpAddressCount = params.get("SecondaryPrivateIpAddressCount")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("PrivateIpAddresses") is not None:
            self.PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self.PrivateIpAddresses.append(obj)
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateNetworkInterfaceResponse(AbstractModel):
    """CreateNetworkInterface返回參數結構體

    """

    def __init__(self):
        """
        :param NetworkInterface: 彈性網卡實例。
        :type NetworkInterface: :class:`tencentcloud.vpc.v20170312.models.NetworkInterface`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NetworkInterface = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetworkInterface") is not None:
            self.NetworkInterface = NetworkInterface()
            self.NetworkInterface._deserialize(params.get("NetworkInterface"))
        self.RequestId = params.get("RequestId")


class CreateRouteTableRequest(AbstractModel):
    """CreateRouteTable請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: 待操作的VPC實例ID。可通過DescribeVpcs介面返回值中的VpcId獲取。
        :type VpcId: str
        :param RouteTableName: 路由表名稱，最大長度不能超過60個位元。
        :type RouteTableName: str
        :param Tags: 指定綁定的标簽清單，例如：[{"Key": "city", "Value": "shanghai"}]
        :type Tags: list of Tag
        """
        self.VpcId = None
        self.RouteTableName = None
        self.Tags = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.RouteTableName = params.get("RouteTableName")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateRouteTableResponse(AbstractModel):
    """CreateRouteTable返回參數結構體

    """

    def __init__(self):
        """
        :param RouteTable: 路由表對象。
        :type RouteTable: :class:`tencentcloud.vpc.v20170312.models.RouteTable`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RouteTable = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RouteTable") is not None:
            self.RouteTable = RouteTable()
            self.RouteTable._deserialize(params.get("RouteTable"))
        self.RequestId = params.get("RequestId")


class CreateRoutesRequest(AbstractModel):
    """CreateRoutes請求參數結構體

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表實例ID。
        :type RouteTableId: str
        :param Routes: 路由策略對象。
        :type Routes: list of Route
        """
        self.RouteTableId = None
        self.Routes = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = Route()
                obj._deserialize(item)
                self.Routes.append(obj)


class CreateRoutesResponse(AbstractModel):
    """CreateRoutes返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 新增的實例個數。
        :type TotalCount: int
        :param RouteTableSet: 路由表對象。
        :type RouteTableSet: list of RouteTable
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RouteTableSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RouteTableSet") is not None:
            self.RouteTableSet = []
            for item in params.get("RouteTableSet"):
                obj = RouteTable()
                obj._deserialize(item)
                self.RouteTableSet.append(obj)
        self.RequestId = params.get("RequestId")


class CreateSecurityGroupPoliciesRequest(AbstractModel):
    """CreateSecurityGroupPolicies請求參數結構體

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全組實例ID，例如sg-33ocnj9n，可通過DescribeSecurityGroups獲取。
        :type SecurityGroupId: str
        :param SecurityGroupPolicySet: 安全組規則集合。
        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`
        """
        self.SecurityGroupId = None
        self.SecurityGroupPolicySet = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = SecurityGroupPolicySet()
            self.SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))


class CreateSecurityGroupPoliciesResponse(AbstractModel):
    """CreateSecurityGroupPolicies返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSecurityGroupRequest(AbstractModel):
    """CreateSecurityGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupName: 安全組名稱，可任意命名，但不得超過60個字元。
        :type GroupName: str
        :param GroupDescription: 安全組備注，最多100個字元。
        :type GroupDescription: str
        :param ProjectId: 項目ID，預設0。可在qcloud控制台項目管理頁面查詢到。
        :type ProjectId: str
        :param Tags: 指定綁定的标簽清單，例如：[{"Key": "city", "Value": "shanghai"}]
        :type Tags: list of Tag
        """
        self.GroupName = None
        self.GroupDescription = None
        self.ProjectId = None
        self.Tags = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupDescription = params.get("GroupDescription")
        self.ProjectId = params.get("ProjectId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateSecurityGroupResponse(AbstractModel):
    """CreateSecurityGroup返回參數結構體

    """

    def __init__(self):
        """
        :param SecurityGroup: 安全組對象。
        :type SecurityGroup: :class:`tencentcloud.vpc.v20170312.models.SecurityGroup`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SecurityGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroup") is not None:
            self.SecurityGroup = SecurityGroup()
            self.SecurityGroup._deserialize(params.get("SecurityGroup"))
        self.RequestId = params.get("RequestId")


class CreateSecurityGroupWithPoliciesRequest(AbstractModel):
    """CreateSecurityGroupWithPolicies請求參數結構體

    """

    def __init__(self):
        """
        :param GroupName: 安全組名稱，可任意命名，但不得超過60個字元。
        :type GroupName: str
        :param GroupDescription: 安全組備注，最多100個字元。
        :type GroupDescription: str
        :param ProjectId: 項目ID，預設0。可在qcloud控制台項目管理頁面查詢到。
        :type ProjectId: str
        :param SecurityGroupPolicySet: 安全組規則集合。
        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`
        """
        self.GroupName = None
        self.GroupDescription = None
        self.ProjectId = None
        self.SecurityGroupPolicySet = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupDescription = params.get("GroupDescription")
        self.ProjectId = params.get("ProjectId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = SecurityGroupPolicySet()
            self.SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))


class CreateSecurityGroupWithPoliciesResponse(AbstractModel):
    """CreateSecurityGroupWithPolicies返回參數結構體

    """

    def __init__(self):
        """
        :param SecurityGroup: 安全組對象。
        :type SecurityGroup: :class:`tencentcloud.vpc.v20170312.models.SecurityGroup`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SecurityGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroup") is not None:
            self.SecurityGroup = SecurityGroup()
            self.SecurityGroup._deserialize(params.get("SecurityGroup"))
        self.RequestId = params.get("RequestId")


class CreateServiceTemplateGroupRequest(AbstractModel):
    """CreateServiceTemplateGroup請求參數結構體

    """

    def __init__(self):
        """
        :param ServiceTemplateGroupName: 協議端口範本集合名稱
        :type ServiceTemplateGroupName: str
        :param ServiceTemplateIds: 協議端口範本實例ID，例如：ppm-4dw6agho。
        :type ServiceTemplateIds: list of str
        """
        self.ServiceTemplateGroupName = None
        self.ServiceTemplateIds = None


    def _deserialize(self, params):
        self.ServiceTemplateGroupName = params.get("ServiceTemplateGroupName")
        self.ServiceTemplateIds = params.get("ServiceTemplateIds")


class CreateServiceTemplateGroupResponse(AbstractModel):
    """CreateServiceTemplateGroup返回參數結構體

    """

    def __init__(self):
        """
        :param ServiceTemplateGroup: 協議端口範本集合對象。
        :type ServiceTemplateGroup: :class:`tencentcloud.vpc.v20170312.models.ServiceTemplateGroup`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ServiceTemplateGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ServiceTemplateGroup") is not None:
            self.ServiceTemplateGroup = ServiceTemplateGroup()
            self.ServiceTemplateGroup._deserialize(params.get("ServiceTemplateGroup"))
        self.RequestId = params.get("RequestId")


class CreateServiceTemplateRequest(AbstractModel):
    """CreateServiceTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param ServiceTemplateName: 協議端口範本名稱
        :type ServiceTemplateName: str
        :param Services: 支援單個端口、多個端口、連續端口及所有端口，協議支援：TCP、UDP、ICMP、GRE 協議。
        :type Services: list of str
        """
        self.ServiceTemplateName = None
        self.Services = None


    def _deserialize(self, params):
        self.ServiceTemplateName = params.get("ServiceTemplateName")
        self.Services = params.get("Services")


class CreateServiceTemplateResponse(AbstractModel):
    """CreateServiceTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param ServiceTemplate: 協議端口範本對象。
        :type ServiceTemplate: :class:`tencentcloud.vpc.v20170312.models.ServiceTemplate`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ServiceTemplate = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ServiceTemplate") is not None:
            self.ServiceTemplate = ServiceTemplate()
            self.ServiceTemplate._deserialize(params.get("ServiceTemplate"))
        self.RequestId = params.get("RequestId")


class CreateSubnetRequest(AbstractModel):
    """CreateSubnet請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: 待操作的VPC實例ID。可通過DescribeVpcs介面返回值中的VpcId獲取。
        :type VpcId: str
        :param SubnetName: 子網名稱，最大長度不能超過60個位元。
        :type SubnetName: str
        :param CidrBlock: 子網網段，子網網段必須在VPC網段内，相同VPC内子網網段不能重疊。
        :type CidrBlock: str
        :param Zone: 子網所在的可用區ID，不同子網選擇不同可用區可以做跨可用區災備。
        :type Zone: str
        :param Tags: 指定綁定的标簽清單，例如：[{"Key": "city", "Value": "shanghai"}]
        :type Tags: list of Tag
        """
        self.VpcId = None
        self.SubnetName = None
        self.CidrBlock = None
        self.Zone = None
        self.Tags = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetName = params.get("SubnetName")
        self.CidrBlock = params.get("CidrBlock")
        self.Zone = params.get("Zone")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateSubnetResponse(AbstractModel):
    """CreateSubnet返回參數結構體

    """

    def __init__(self):
        """
        :param Subnet: 子網對象。
        :type Subnet: :class:`tencentcloud.vpc.v20170312.models.Subnet`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Subnet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Subnet") is not None:
            self.Subnet = Subnet()
            self.Subnet._deserialize(params.get("Subnet"))
        self.RequestId = params.get("RequestId")


class CreateSubnetsRequest(AbstractModel):
    """CreateSubnets請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: `VPC`實例`ID`。形如：`vpc-6v2ht8q5`
        :type VpcId: str
        :param Subnets: 子網對象清單。
        :type Subnets: list of SubnetInput
        :param Tags: 指定綁定的标簽清單，注意這裏的标簽集合爲清單中所有子網對象所共享，不能爲每個子網對象單獨指定标簽，例如：[{"Key": "city", "Value": "shanghai"}]
        :type Tags: list of Tag
        """
        self.VpcId = None
        self.Subnets = None
        self.Tags = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        if params.get("Subnets") is not None:
            self.Subnets = []
            for item in params.get("Subnets"):
                obj = SubnetInput()
                obj._deserialize(item)
                self.Subnets.append(obj)
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateSubnetsResponse(AbstractModel):
    """CreateSubnets返回參數結構體

    """

    def __init__(self):
        """
        :param SubnetSet: 新創建的子網清單。
        :type SubnetSet: list of Subnet
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SubnetSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SubnetSet") is not None:
            self.SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = Subnet()
                obj._deserialize(item)
                self.SubnetSet.append(obj)
        self.RequestId = params.get("RequestId")


class CreateVpcRequest(AbstractModel):
    """CreateVpc請求參數結構體

    """

    def __init__(self):
        """
        :param VpcName: vpc名稱，最大長度不能超過60個位元。
        :type VpcName: str
        :param CidrBlock: vpc的cidr，只能爲10.0.0.0/16，172.16.0.0/16，192.168.0.0/16這三個内網網段内。
        :type CidrBlock: str
        :param EnableMulticast: 是否開啓組播。true: 開啓, false: 不開啓。
        :type EnableMulticast: str
        :param DnsServers: DNS網址，最多支援4個
        :type DnsServers: list of str
        :param DomainName: 域名
        :type DomainName: str
        :param Tags: 指定綁定的标簽清單，例如：[{"Key": "city", "Value": "shanghai"}]
        :type Tags: list of Tag
        """
        self.VpcName = None
        self.CidrBlock = None
        self.EnableMulticast = None
        self.DnsServers = None
        self.DomainName = None
        self.Tags = None


    def _deserialize(self, params):
        self.VpcName = params.get("VpcName")
        self.CidrBlock = params.get("CidrBlock")
        self.EnableMulticast = params.get("EnableMulticast")
        self.DnsServers = params.get("DnsServers")
        self.DomainName = params.get("DomainName")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateVpcResponse(AbstractModel):
    """CreateVpc返回參數結構體

    """

    def __init__(self):
        """
        :param Vpc: Vpc對象。
        :type Vpc: :class:`tencentcloud.vpc.v20170312.models.Vpc`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Vpc = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Vpc") is not None:
            self.Vpc = Vpc()
            self.Vpc._deserialize(params.get("Vpc"))
        self.RequestId = params.get("RequestId")


class CreateVpnConnectionRequest(AbstractModel):
    """CreateVpnConnection請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: VPC實例ID。可通過DescribeVpcs介面返回值中的VpcId獲取。
        :type VpcId: str
        :param VpnGatewayId: VPN閘道實例ID。
        :type VpnGatewayId: str
        :param CustomerGatewayId: 對端閘道ID，例如：cgw-2wqq41m9，可通過DescribeCustomerGateways介面查詢對端閘道。
        :type CustomerGatewayId: str
        :param VpnConnectionName: 通道名稱，可任意命名，但不得超過60個字元。
        :type VpnConnectionName: str
        :param PreShareKey: 預共享金鑰。
        :type PreShareKey: str
        :param SecurityPolicyDatabases: SPD策略組，例如：{"10.0.0.5/24":["172.123.10.5/16"]}，10.0.0.5/24是vpc内網段172.123.10.5/16是IDC網段。用戶指定VPC内哪些網段可以和您IDC中哪些網段通信。
        :type SecurityPolicyDatabases: list of SecurityPolicyDatabase
        :param IKEOptionsSpecification: IKE配置（Internet Key Exchange，因特網金鑰交換），IKE具有一套自我保護機制，用戶配置網絡安全協議
        :type IKEOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IKEOptionsSpecification`
        :param IPSECOptionsSpecification: IPSec配置，Top Cloud 提供IPSec安全會話設置
        :type IPSECOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IPSECOptionsSpecification`
        """
        self.VpcId = None
        self.VpnGatewayId = None
        self.CustomerGatewayId = None
        self.VpnConnectionName = None
        self.PreShareKey = None
        self.SecurityPolicyDatabases = None
        self.IKEOptionsSpecification = None
        self.IPSECOptionsSpecification = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.CustomerGatewayId = params.get("CustomerGatewayId")
        self.VpnConnectionName = params.get("VpnConnectionName")
        self.PreShareKey = params.get("PreShareKey")
        if params.get("SecurityPolicyDatabases") is not None:
            self.SecurityPolicyDatabases = []
            for item in params.get("SecurityPolicyDatabases"):
                obj = SecurityPolicyDatabase()
                obj._deserialize(item)
                self.SecurityPolicyDatabases.append(obj)
        if params.get("IKEOptionsSpecification") is not None:
            self.IKEOptionsSpecification = IKEOptionsSpecification()
            self.IKEOptionsSpecification._deserialize(params.get("IKEOptionsSpecification"))
        if params.get("IPSECOptionsSpecification") is not None:
            self.IPSECOptionsSpecification = IPSECOptionsSpecification()
            self.IPSECOptionsSpecification._deserialize(params.get("IPSECOptionsSpecification"))


class CreateVpnConnectionResponse(AbstractModel):
    """CreateVpnConnection返回參數結構體

    """

    def __init__(self):
        """
        :param VpnConnection: 通道實例對象。
        :type VpnConnection: :class:`tencentcloud.vpc.v20170312.models.VpnConnection`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.VpnConnection = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VpnConnection") is not None:
            self.VpnConnection = VpnConnection()
            self.VpnConnection._deserialize(params.get("VpnConnection"))
        self.RequestId = params.get("RequestId")


class CreateVpnGatewayRequest(AbstractModel):
    """CreateVpnGateway請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: VPC實例ID。可通過DescribeVpcs介面返回值中的VpcId獲取。
        :type VpcId: str
        :param VpnGatewayName: VPN閘道名稱，最大長度不能超過60個位元。
        :type VpnGatewayName: str
        :param InternetMaxBandwidthOut: 公網頻寬設置。可選頻寬規格：5, 10, 20, 50, 100；單位：Mbps
        :type InternetMaxBandwidthOut: int
        :param InstanceChargeType: VPN閘道計費模式，PREPAID：表示預付費，即包年包月，POSTPAID_BY_HOUR：表示後付費，即按量計費。預設：POSTPAID_BY_HOUR，如果指定預付費模式，參數InstanceChargePrepaid必填。
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: 預付費模式，即包年包月相關參數設置。通過該參數可以指定包年包月實例的購買時長、是否設置自動續約等屬性。若指定實例的付費模式爲預付費則該參數必傳。
        :type InstanceChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.InstanceChargePrepaid`
        :param Zone: 可用區，如：ap-guangzhou-2。
        :type Zone: str
        :param Type: VPN閘道類型。值“CCN”雲聯網類型VPN閘道
        :type Type: str
        """
        self.VpcId = None
        self.VpnGatewayName = None
        self.InternetMaxBandwidthOut = None
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None
        self.Zone = None
        self.Type = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpnGatewayName = params.get("VpnGatewayName")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self.Zone = params.get("Zone")
        self.Type = params.get("Type")


class CreateVpnGatewayResponse(AbstractModel):
    """CreateVpnGateway返回參數結構體

    """

    def __init__(self):
        """
        :param VpnGateway: VPN閘道對象
        :type VpnGateway: :class:`tencentcloud.vpc.v20170312.models.VpnGateway`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.VpnGateway = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VpnGateway") is not None:
            self.VpnGateway = VpnGateway()
            self.VpnGateway._deserialize(params.get("VpnGateway"))
        self.RequestId = params.get("RequestId")


class CustomerGateway(AbstractModel):
    """對端閘道

    """

    def __init__(self):
        """
        :param CustomerGatewayId: 用戶閘道唯一ID
        :type CustomerGatewayId: str
        :param CustomerGatewayName: 閘道名稱
        :type CustomerGatewayName: str
        :param IpAddress: 公網網址
        :type IpAddress: str
        :param CreatedTime: 創建時間
        :type CreatedTime: str
        """
        self.CustomerGatewayId = None
        self.CustomerGatewayName = None
        self.IpAddress = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.CustomerGatewayId = params.get("CustomerGatewayId")
        self.CustomerGatewayName = params.get("CustomerGatewayName")
        self.IpAddress = params.get("IpAddress")
        self.CreatedTime = params.get("CreatedTime")


class CustomerGatewayVendor(AbstractModel):
    """對端閘道廠商訊息對象。

    """

    def __init__(self):
        """
        :param Platform: 平台。
        :type Platform: str
        :param SoftwareVersion: 軟體版本。
        :type SoftwareVersion: str
        :param VendorName: 供應商名稱。
        :type VendorName: str
        """
        self.Platform = None
        self.SoftwareVersion = None
        self.VendorName = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.SoftwareVersion = params.get("SoftwareVersion")
        self.VendorName = params.get("VendorName")


class CvmInstance(AbstractModel):
    """雲主機實例訊息。

    """

    def __init__(self):
        """
        :param VpcId: VPC實例ID。
        :type VpcId: str
        :param SubnetId: 子網實例ID。
        :type SubnetId: str
        :param InstanceId: 雲主機實例ID
        :type InstanceId: str
        :param InstanceName: 雲主機名稱。
        :type InstanceName: str
        :param InstanceState: 雲主機狀态。
        :type InstanceState: str
        :param CPU: 實例的CPU核數，單位：核。
        :type CPU: int
        :param Memory: 實例内存容量，單位：GB。
        :type Memory: int
        :param CreatedTime: 創建時間。
        :type CreatedTime: str
        :param InstanceType: 實例機型。
        :type InstanceType: str
        :param EniLimit: 實例彈性網卡配額（包含主網卡）。
        :type EniLimit: int
        :param EniIpLimit: 實例彈性網卡内網IP配額（包含主網卡）。
        :type EniIpLimit: int
        :param InstanceEniCount: 實例已綁定彈性網卡的個數（包含主網卡）。
        :type InstanceEniCount: int
        """
        self.VpcId = None
        self.SubnetId = None
        self.InstanceId = None
        self.InstanceName = None
        self.InstanceState = None
        self.CPU = None
        self.Memory = None
        self.CreatedTime = None
        self.InstanceType = None
        self.EniLimit = None
        self.EniIpLimit = None
        self.InstanceEniCount = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.InstanceState = params.get("InstanceState")
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")
        self.CreatedTime = params.get("CreatedTime")
        self.InstanceType = params.get("InstanceType")
        self.EniLimit = params.get("EniLimit")
        self.EniIpLimit = params.get("EniIpLimit")
        self.InstanceEniCount = params.get("InstanceEniCount")


class DefaultVpcSubnet(AbstractModel):
    """預設VPC和子網

    """

    def __init__(self):
        """
        :param VpcId: 預設VpcId
        :type VpcId: str
        :param SubnetId: 預設SubnetId
        :type SubnetId: str
        """
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")


class DeleteAddressTemplateGroupRequest(AbstractModel):
    """DeleteAddressTemplateGroup請求參數結構體

    """

    def __init__(self):
        """
        :param AddressTemplateGroupId: IP網址範本集合實例ID，例如：ipmg-90cex8mq。
        :type AddressTemplateGroupId: str
        """
        self.AddressTemplateGroupId = None


    def _deserialize(self, params):
        self.AddressTemplateGroupId = params.get("AddressTemplateGroupId")


class DeleteAddressTemplateGroupResponse(AbstractModel):
    """DeleteAddressTemplateGroup返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAddressTemplateRequest(AbstractModel):
    """DeleteAddressTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param AddressTemplateId: IP網址範本實例ID，例如：ipm-09o5m8kc。
        :type AddressTemplateId: str
        """
        self.AddressTemplateId = None


    def _deserialize(self, params):
        self.AddressTemplateId = params.get("AddressTemplateId")


class DeleteAddressTemplateResponse(AbstractModel):
    """DeleteAddressTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAssistantCidrRequest(AbstractModel):
    """DeleteAssistantCidr請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: `VPC`實例`ID`。形如：`vpc-6v2ht8q5`
        :type VpcId: str
        :param CidrBlocks: CIDR數組，格式如["10.0.0.0/16", "172.16.0.0/16"]
        :type CidrBlocks: list of str
        """
        self.VpcId = None
        self.CidrBlocks = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.CidrBlocks = params.get("CidrBlocks")


class DeleteAssistantCidrResponse(AbstractModel):
    """DeleteAssistantCidr返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteBandwidthPackageRequest(AbstractModel):
    """DeleteBandwidthPackage請求參數結構體

    """

    def __init__(self):
        """
        :param BandwidthPackageId: 待删除頻寬包唯一ID
        :type BandwidthPackageId: str
        """
        self.BandwidthPackageId = None


    def _deserialize(self, params):
        self.BandwidthPackageId = params.get("BandwidthPackageId")


class DeleteBandwidthPackageResponse(AbstractModel):
    """DeleteBandwidthPackage返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCcnRequest(AbstractModel):
    """DeleteCcn請求參數結構體

    """

    def __init__(self):
        """
        :param CcnId: CCN實例ID。形如：ccn-f49l6u0z。
        :type CcnId: str
        """
        self.CcnId = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")


class DeleteCcnResponse(AbstractModel):
    """DeleteCcn返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCustomerGatewayRequest(AbstractModel):
    """DeleteCustomerGateway請求參數結構體

    """

    def __init__(self):
        """
        :param CustomerGatewayId: 對端閘道ID，例如：cgw-2wqq41m9，可通過DescribeCustomerGateways介面查詢對端閘道。
        :type CustomerGatewayId: str
        """
        self.CustomerGatewayId = None


    def _deserialize(self, params):
        self.CustomerGatewayId = params.get("CustomerGatewayId")


class DeleteCustomerGatewayResponse(AbstractModel):
    """DeleteCustomerGateway返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDirectConnectGatewayCcnRoutesRequest(AbstractModel):
    """DeleteDirectConnectGatewayCcnRoutes請求參數結構體

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: 專線閘道ID，形如：dcg-prpqlmg1
        :type DirectConnectGatewayId: str
        :param RouteIds: 路由ID。形如：ccnr-f49l6u0z。
        :type RouteIds: list of str
        """
        self.DirectConnectGatewayId = None
        self.RouteIds = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.RouteIds = params.get("RouteIds")


class DeleteDirectConnectGatewayCcnRoutesResponse(AbstractModel):
    """DeleteDirectConnectGatewayCcnRoutes返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDirectConnectGatewayRequest(AbstractModel):
    """DeleteDirectConnectGateway請求參數結構體

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: 專線閘道唯一`ID`，形如：`dcg-9o233uri`。
        :type DirectConnectGatewayId: str
        """
        self.DirectConnectGatewayId = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")


class DeleteDirectConnectGatewayResponse(AbstractModel):
    """DeleteDirectConnectGateway返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteFlowLogRequest(AbstractModel):
    """DeleteFlowLog請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: 私用網絡ID或者統一ID，建議使用統一ID
        :type VpcId: str
        :param FlowLogId: 流日志唯一ID
        :type FlowLogId: str
        """
        self.VpcId = None
        self.FlowLogId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.FlowLogId = params.get("FlowLogId")


class DeleteFlowLogResponse(AbstractModel):
    """DeleteFlowLog返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteHaVipRequest(AbstractModel):
    """DeleteHaVip請求參數結構體

    """

    def __init__(self):
        """
        :param HaVipId: `HAVIP`唯一`ID`，形如：`havip-9o233uri`。
        :type HaVipId: str
        """
        self.HaVipId = None


    def _deserialize(self, params):
        self.HaVipId = params.get("HaVipId")


class DeleteHaVipResponse(AbstractModel):
    """DeleteHaVip返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteIp6TranslatorsRequest(AbstractModel):
    """DeleteIp6Translators請求參數結構體

    """

    def __init__(self):
        """
        :param Ip6TranslatorIds: 待釋放的IPV6轉換實例的唯一ID，形如‘ip6-xxxxxxxx’
        :type Ip6TranslatorIds: list of str
        """
        self.Ip6TranslatorIds = None


    def _deserialize(self, params):
        self.Ip6TranslatorIds = params.get("Ip6TranslatorIds")


class DeleteIp6TranslatorsResponse(AbstractModel):
    """DeleteIp6Translators返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNatGatewayDestinationIpPortTranslationNatRuleRequest(AbstractModel):
    """DeleteNatGatewayDestinationIpPortTranslationNatRule請求參數結構體

    """

    def __init__(self):
        """
        :param NatGatewayId: NAT閘道的ID，形如：`nat-df45454`。
        :type NatGatewayId: str
        :param DestinationIpPortTranslationNatRules: NAT閘道的端口轉換規則。
        :type DestinationIpPortTranslationNatRules: list of DestinationIpPortTranslationNatRule
        """
        self.NatGatewayId = None
        self.DestinationIpPortTranslationNatRules = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        if params.get("DestinationIpPortTranslationNatRules") is not None:
            self.DestinationIpPortTranslationNatRules = []
            for item in params.get("DestinationIpPortTranslationNatRules"):
                obj = DestinationIpPortTranslationNatRule()
                obj._deserialize(item)
                self.DestinationIpPortTranslationNatRules.append(obj)


class DeleteNatGatewayDestinationIpPortTranslationNatRuleResponse(AbstractModel):
    """DeleteNatGatewayDestinationIpPortTranslationNatRule返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNatGatewayRequest(AbstractModel):
    """DeleteNatGateway請求參數結構體

    """

    def __init__(self):
        """
        :param NatGatewayId: NAT閘道的ID，形如：`nat-df45454`。
        :type NatGatewayId: str
        """
        self.NatGatewayId = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")


class DeleteNatGatewayResponse(AbstractModel):
    """DeleteNatGateway返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNetDetectRequest(AbstractModel):
    """DeleteNetDetect請求參數結構體

    """

    def __init__(self):
        """
        :param NetDetectId: 網絡探測實例`ID`。形如：`netd-12345678`
        :type NetDetectId: str
        """
        self.NetDetectId = None


    def _deserialize(self, params):
        self.NetDetectId = params.get("NetDetectId")


class DeleteNetDetectResponse(AbstractModel):
    """DeleteNetDetect返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNetworkAclRequest(AbstractModel):
    """DeleteNetworkAcl請求參數結構體

    """

    def __init__(self):
        """
        :param NetworkAclId: 網絡ACL實例ID。例如：acl-12345678。
        :type NetworkAclId: str
        """
        self.NetworkAclId = None


    def _deserialize(self, params):
        self.NetworkAclId = params.get("NetworkAclId")


class DeleteNetworkAclResponse(AbstractModel):
    """DeleteNetworkAcl返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNetworkInterfaceRequest(AbstractModel):
    """DeleteNetworkInterface請求參數結構體

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 彈性網卡實例ID，例如：eni-m6dyj72l。
        :type NetworkInterfaceId: str
        """
        self.NetworkInterfaceId = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")


class DeleteNetworkInterfaceResponse(AbstractModel):
    """DeleteNetworkInterface返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRouteTableRequest(AbstractModel):
    """DeleteRouteTable請求參數結構體

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表實例ID，例如：rtb-azd4dt1c。
        :type RouteTableId: str
        """
        self.RouteTableId = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")


class DeleteRouteTableResponse(AbstractModel):
    """DeleteRouteTable返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRoutesRequest(AbstractModel):
    """DeleteRoutes請求參數結構體

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表實例ID。
        :type RouteTableId: str
        :param Routes: 路由策略對象。
        :type Routes: list of Route
        """
        self.RouteTableId = None
        self.Routes = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = Route()
                obj._deserialize(item)
                self.Routes.append(obj)


class DeleteRoutesResponse(AbstractModel):
    """DeleteRoutes返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSecurityGroupPoliciesRequest(AbstractModel):
    """DeleteSecurityGroupPolicies請求參數結構體

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全組實例ID，例如sg-33ocnj9n，可通過DescribeSecurityGroups獲取。
        :type SecurityGroupId: str
        :param SecurityGroupPolicySet: 安全組規則集合。一個請求中只能删除單個方向的一條或多條規則。支援指定索引（PolicyIndex） 比對删除和安全組規則比對删除兩種方式，一個請求中只能使用一種比對方式。
        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`
        """
        self.SecurityGroupId = None
        self.SecurityGroupPolicySet = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = SecurityGroupPolicySet()
            self.SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))


class DeleteSecurityGroupPoliciesResponse(AbstractModel):
    """DeleteSecurityGroupPolicies返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSecurityGroupRequest(AbstractModel):
    """DeleteSecurityGroup請求參數結構體

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全組實例ID，例如sg-33ocnj9n，可通過DescribeSecurityGroups獲取。
        :type SecurityGroupId: str
        """
        self.SecurityGroupId = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")


class DeleteSecurityGroupResponse(AbstractModel):
    """DeleteSecurityGroup返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteServiceTemplateGroupRequest(AbstractModel):
    """DeleteServiceTemplateGroup請求參數結構體

    """

    def __init__(self):
        """
        :param ServiceTemplateGroupId: 協議端口範本集合實例ID，例如：ppmg-n17uxvve。
        :type ServiceTemplateGroupId: str
        """
        self.ServiceTemplateGroupId = None


    def _deserialize(self, params):
        self.ServiceTemplateGroupId = params.get("ServiceTemplateGroupId")


class DeleteServiceTemplateGroupResponse(AbstractModel):
    """DeleteServiceTemplateGroup返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteServiceTemplateRequest(AbstractModel):
    """DeleteServiceTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param ServiceTemplateId: 協議端口範本實例ID，例如：ppm-e6dy460g。
        :type ServiceTemplateId: str
        """
        self.ServiceTemplateId = None


    def _deserialize(self, params):
        self.ServiceTemplateId = params.get("ServiceTemplateId")


class DeleteServiceTemplateResponse(AbstractModel):
    """DeleteServiceTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSubnetRequest(AbstractModel):
    """DeleteSubnet請求參數結構體

    """

    def __init__(self):
        """
        :param SubnetId: 子網實例ID。可通過DescribeSubnets介面返回值中的SubnetId獲取。
        :type SubnetId: str
        """
        self.SubnetId = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")


class DeleteSubnetResponse(AbstractModel):
    """DeleteSubnet返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteVpcRequest(AbstractModel):
    """DeleteVpc請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: VPC實例ID。可通過DescribeVpcs介面返回值中的VpcId獲取。
        :type VpcId: str
        """
        self.VpcId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")


class DeleteVpcResponse(AbstractModel):
    """DeleteVpc返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteVpnConnectionRequest(AbstractModel):
    """DeleteVpnConnection請求參數結構體

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN閘道實例ID。
        :type VpnGatewayId: str
        :param VpnConnectionId: VPN通道實例ID。形如：vpnx-f49l6u0z。
        :type VpnConnectionId: str
        """
        self.VpnGatewayId = None
        self.VpnConnectionId = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.VpnConnectionId = params.get("VpnConnectionId")


class DeleteVpnConnectionResponse(AbstractModel):
    """DeleteVpnConnection返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteVpnGatewayRequest(AbstractModel):
    """DeleteVpnGateway請求參數結構體

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN閘道實例ID。
        :type VpnGatewayId: str
        """
        self.VpnGatewayId = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")


class DeleteVpnGatewayResponse(AbstractModel):
    """DeleteVpnGateway返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccountAttributesRequest(AbstractModel):
    """DescribeAccountAttributes請求參數結構體

    """


class DescribeAccountAttributesResponse(AbstractModel):
    """DescribeAccountAttributes返回參數結構體

    """

    def __init__(self):
        """
        :param AccountAttributeSet: 用戶賬号屬性對象
        :type AccountAttributeSet: list of AccountAttribute
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AccountAttributeSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccountAttributeSet") is not None:
            self.AccountAttributeSet = []
            for item in params.get("AccountAttributeSet"):
                obj = AccountAttribute()
                obj._deserialize(item)
                self.AccountAttributeSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAddressQuotaRequest(AbstractModel):
    """DescribeAddressQuota請求參數結構體

    """


class DescribeAddressQuotaResponse(AbstractModel):
    """DescribeAddressQuota返回參數結構體

    """

    def __init__(self):
        """
        :param QuotaSet: 帳戶 EIP 配額訊息。
        :type QuotaSet: list of Quota
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.QuotaSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("QuotaSet") is not None:
            self.QuotaSet = []
            for item in params.get("QuotaSet"):
                obj = Quota()
                obj._deserialize(item)
                self.QuotaSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAddressTemplateGroupsRequest(AbstractModel):
    """DescribeAddressTemplateGroups請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 過濾條件。
<li>address-template-group-name - String - （過濾條件）IP網址範本集合名稱。</li>
<li>address-template-group-id - String - （過濾條件）IP網址範本實集合例ID，例如：ipmg-mdunqeb6。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。
        :type Offset: str
        :param Limit: 返回數量，預設爲20，最大值爲100。
        :type Limit: str
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAddressTemplateGroupsResponse(AbstractModel):
    """DescribeAddressTemplateGroups返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的實例數量。
        :type TotalCount: int
        :param AddressTemplateGroupSet: IP網址範本。
        :type AddressTemplateGroupSet: list of AddressTemplateGroup
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AddressTemplateGroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AddressTemplateGroupSet") is not None:
            self.AddressTemplateGroupSet = []
            for item in params.get("AddressTemplateGroupSet"):
                obj = AddressTemplateGroup()
                obj._deserialize(item)
                self.AddressTemplateGroupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAddressTemplatesRequest(AbstractModel):
    """DescribeAddressTemplates請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 過濾條件。
<li>address-template-name - String - （過濾條件）IP網址範本名稱。</li>
<li>address-template-id - String - （過濾條件）IP網址範本實例ID，例如：ipm-mdunqeb6。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。
        :type Offset: str
        :param Limit: 返回數量，預設爲20，最大值爲100。
        :type Limit: str
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAddressTemplatesResponse(AbstractModel):
    """DescribeAddressTemplates返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的實例數量。
        :type TotalCount: int
        :param AddressTemplateSet: IP網址模版。
        :type AddressTemplateSet: list of AddressTemplate
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AddressTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AddressTemplateSet") is not None:
            self.AddressTemplateSet = []
            for item in params.get("AddressTemplateSet"):
                obj = AddressTemplate()
                obj._deserialize(item)
                self.AddressTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAddressesRequest(AbstractModel):
    """DescribeAddresses請求參數結構體

    """

    def __init__(self):
        """
        :param AddressIds: 标識 EIP 的唯一 ID 清單。EIP 唯一 ID 形如：`eip-11112222`。參數不支援同時指定`AddressIds`和`Filters`。
        :type AddressIds: list of str
        :param Filters: 每次請求的`Filters`的上限爲10，`Filter.Values`的上限爲5。參數不支援同時指定`AddressIds`和`Filters`。詳細的過濾條件如下：
<li> address-id - String - 是否必填：否 - （過濾條件）按照 EIP 的唯一 ID 過濾。EIP 唯一 ID 形如：eip-11112222。</li>
<li> address-name - String - 是否必填：否 - （過濾條件）按照 EIP 名稱過濾。不支援模糊過濾。</li>
<li> address-ip - String - 是否必填：否 - （過濾條件）按照 EIP 的 IP 網址過濾。</li>
<li> address-status - String - 是否必填：否 - （過濾條件）按照 EIP 的狀态過濾。狀态包含：'CREATING'，'BINDING'，'BIND'，'UNBINDING'，'UNBIND'，'OFFLINING'，'BIND_ENI'。</li>
<li> instance-id - String - 是否必填：否 - （過濾條件）按照 EIP 綁定的實例 ID 過濾。實例 ID 形如：ins-11112222。</li>
<li> private-ip-address - String - 是否必填：否 - （過濾條件）按照 EIP 綁定的内網 IP 過濾。</li>
<li> network-interface-id - String - 是否必填：否 - （過濾條件）按照 EIP 綁定的彈性網卡 ID 過濾。彈性網卡 ID 形如：eni-11112222。</li>
<li> is-arrears - String - 是否必填：否 - （過濾條件）按照 EIP 是否欠費進行過濾。（TRUE：EIP 處于欠費狀态|FALSE：EIP 費用狀态正常）</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。關于`Offset`的更進一步介紹請參考 API [簡介](https://cloud.tencent.com/document/api/213/11646)中的相關小節。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。關于`Limit`的更進一步介紹請參考 API [簡介](https://cloud.tencent.com/document/api/213/11646)中的相關小節。
        :type Limit: int
        """
        self.AddressIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.AddressIds = params.get("AddressIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAddressesResponse(AbstractModel):
    """DescribeAddresses返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的 EIP 數量。
        :type TotalCount: int
        :param AddressSet: EIP 詳細訊息清單。
        :type AddressSet: list of Address
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AddressSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AddressSet") is not None:
            self.AddressSet = []
            for item in params.get("AddressSet"):
                obj = Address()
                obj._deserialize(item)
                self.AddressSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAssistantCidrRequest(AbstractModel):
    """DescribeAssistantCidr請求參數結構體

    """

    def __init__(self):
        """
        :param VpcIds: `VPC`實例`ID`數組。形如：[`vpc-6v2ht8q5`]
        :type VpcIds: list of str
        :param Filters: 過濾條件，參數不支援同時指定NetworkInterfaceIds和Filters。
<li>vpc-id - String - （過濾條件）VPC實例ID，形如：vpc-f49l6u0z。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。
        :type Limit: int
        """
        self.VpcIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.VpcIds = params.get("VpcIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAssistantCidrResponse(AbstractModel):
    """DescribeAssistantCidr返回參數結構體

    """

    def __init__(self):
        """
        :param AssistantCidrSet: 符合條件的輔助CIDR數組。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AssistantCidrSet: list of AssistantCidr
        :param TotalCount: 符合條件的實例數量。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AssistantCidrSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AssistantCidrSet") is not None:
            self.AssistantCidrSet = []
            for item in params.get("AssistantCidrSet"):
                obj = AssistantCidr()
                obj._deserialize(item)
                self.AssistantCidrSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeBandwidthPackageQuotaRequest(AbstractModel):
    """DescribeBandwidthPackageQuota請求參數結構體

    """


class DescribeBandwidthPackageQuotaResponse(AbstractModel):
    """DescribeBandwidthPackageQuota返回參數結構體

    """

    def __init__(self):
        """
        :param QuotaSet: 頻寬包配額詳細訊息
        :type QuotaSet: list of Quota
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.QuotaSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("QuotaSet") is not None:
            self.QuotaSet = []
            for item in params.get("QuotaSet"):
                obj = Quota()
                obj._deserialize(item)
                self.QuotaSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBandwidthPackagesRequest(AbstractModel):
    """DescribeBandwidthPackages請求參數結構體

    """

    def __init__(self):
        """
        :param BandwidthPackageIds: 頻寬包唯一ID清單
        :type BandwidthPackageIds: list of str
        :param Filters: 每次請求的`Filters`的上限爲10。參數不支援同時指定`BandwidthPackageIds`和`Filters`。詳細的過濾條件如下：
<li> bandwidth-package_id - String - 是否必填：否 - （過濾條件）按照頻寬包的唯一标識ID過濾。</li>
<li> bandwidth-package-name - String - 是否必填：否 - （過濾條件）按照 頻寬包名稱過濾。不支援模糊過濾。</li>
<li> network-type - String - 是否必填：否 - （過濾條件）按照頻寬包的類型過濾。類型包括'BGP','SINGLEISP'和'ANYCAST'。</li>
<li> charge-type - String - 是否必填：否 - （過濾條件）按照頻寬包的計費類型過濾。計費類型包括'TOP5_POSTPAID_BY_MONTH'和'PERCENT95_POSTPAID_BY_MONTH'</li>
<li> resource.resource-type - String - 是否必填：否 - （過濾條件）按照頻寬包資源類型過濾。資源類型包括'Address'和'LoadBalance'</li>
<li> resource.resource-id - String - 是否必填：否 - （過濾條件）按照頻寬包資源Id過濾。資源Id形如'eip-xxxx','lb-xxxx'</li>
<li> resource.address-ip - String - 是否必填：否 - （過濾條件）按照頻寬包資源Ip過濾。</li>
        :type Filters: list of Filter
        :param Offset: 查詢頻寬包偏移量
        :type Offset: int
        :param Limit: 查詢頻寬包數量限制
        :type Limit: int
        """
        self.BandwidthPackageIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.BandwidthPackageIds = params.get("BandwidthPackageIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeBandwidthPackagesResponse(AbstractModel):
    """DescribeBandwidthPackages返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的頻寬包數量
        :type TotalCount: int
        :param BandwidthPackageSet: 描述頻寬包詳細訊息
        :type BandwidthPackageSet: list of BandwidthPackage
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.BandwidthPackageSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BandwidthPackageSet") is not None:
            self.BandwidthPackageSet = []
            for item in params.get("BandwidthPackageSet"):
                obj = BandwidthPackage()
                obj._deserialize(item)
                self.BandwidthPackageSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCcnAttachedInstancesRequest(AbstractModel):
    """DescribeCcnAttachedInstances請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回數量
        :type Limit: int
        :param Filters: 過濾條件：
<li>ccn-id - String -（過濾條件）CCN實例ID。</li>
<li>instance-type - String -（過濾條件）關聯實例類型。</li>
<li>instance-region - String -（過濾條件）關聯實例所屬地域。</li>
<li>instance-id - String -（過濾條件）關聯實例實例ID。</li>
        :type Filters: list of Filter
        :param CcnId: 雲聯網實例ID
        :type CcnId: str
        :param OrderField: 排序欄位。支援：`CcnId` `InstanceType` `InstanceId` `InstanceName` `InstanceRegion` `AttachedTime` `State`。
        :type OrderField: str
        :param OrderDirection: 排序方法。順序：`ASC`，倒序：`DESC`。
        :type OrderDirection: str
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.CcnId = None
        self.OrderField = None
        self.OrderDirection = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.CcnId = params.get("CcnId")
        self.OrderField = params.get("OrderField")
        self.OrderDirection = params.get("OrderDirection")


class DescribeCcnAttachedInstancesResponse(AbstractModel):
    """DescribeCcnAttachedInstances返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的對象數。
        :type TotalCount: int
        :param InstanceSet: 關聯實例清單。
        :type InstanceSet: list of CcnAttachedInstance
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = CcnAttachedInstance()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCcnRegionBandwidthLimitsRequest(AbstractModel):
    """DescribeCcnRegionBandwidthLimits請求參數結構體

    """

    def __init__(self):
        """
        :param CcnId: CCN實例ID。形如：ccn-f49l6u0z。
        :type CcnId: str
        """
        self.CcnId = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")


class DescribeCcnRegionBandwidthLimitsResponse(AbstractModel):
    """DescribeCcnRegionBandwidthLimits返回參數結構體

    """

    def __init__(self):
        """
        :param CcnRegionBandwidthLimitSet: 雲聯網（CCN）各地域出頻寬上限
        :type CcnRegionBandwidthLimitSet: list of CcnRegionBandwidthLimit
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CcnRegionBandwidthLimitSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CcnRegionBandwidthLimitSet") is not None:
            self.CcnRegionBandwidthLimitSet = []
            for item in params.get("CcnRegionBandwidthLimitSet"):
                obj = CcnRegionBandwidthLimit()
                obj._deserialize(item)
                self.CcnRegionBandwidthLimitSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCcnRoutesRequest(AbstractModel):
    """DescribeCcnRoutes請求參數結構體

    """

    def __init__(self):
        """
        :param CcnId: CCN實例ID，形如：ccn-gree226l。
        :type CcnId: str
        :param RouteIds: CCN路由策略唯一ID。形如：ccnr-f49l6u0z。
        :type RouteIds: list of str
        :param Filters: 過濾條件，參數不支援同時指定RouteIds和Filters。
<li>route-id - String -（過濾條件）路由策略ID。</li>
<li>cidr-block - String -（過濾條件）目的端。</li>
<li>instance-type - String -（過濾條件）下一跳類型。</li>
<li>instance-region - String -（過濾條件）下一跳所屬地域。</li>
<li>instance-id - String -（過濾條件）下一跳實例ID。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回數量
        :type Limit: int
        """
        self.CcnId = None
        self.RouteIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.RouteIds = params.get("RouteIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeCcnRoutesResponse(AbstractModel):
    """DescribeCcnRoutes返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的對象數。
        :type TotalCount: int
        :param RouteSet: CCN路由策略對象。
        :type RouteSet: list of CcnRoute
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RouteSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RouteSet") is not None:
            self.RouteSet = []
            for item in params.get("RouteSet"):
                obj = CcnRoute()
                obj._deserialize(item)
                self.RouteSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCcnsRequest(AbstractModel):
    """DescribeCcns請求參數結構體

    """

    def __init__(self):
        """
        :param CcnIds: CCN實例ID。形如：ccn-f49l6u0z。每次請求的實例的上限爲100。參數不支援同時指定CcnIds和Filters。
        :type CcnIds: list of str
        :param Filters: 過濾條件，參數不支援同時指定CcnIds和Filters。
<li>ccn-id - String - （過濾條件）CCN唯一ID，形如：vpc-f49l6u0z。</li>
<li>ccn-name - String - （過濾條件）CCN名稱。</li>
<li>ccn-description - String - （過濾條件）CCN描述。</li>
<li>state - String - （過濾條件）實例狀态， 'ISOLATED': 隔離中（欠費停服），'AVAILABLE'：運作中。</li>
<li>tag-key - String -是否必填：否- （過濾條件）按照标簽鍵進行過濾。</li>
<li>tag:tag-key - String - 是否必填：否 - （過濾條件）按照标簽鍵值對進行過濾。 tag-key使用具體的标簽鍵進行替換。使用請參考範例：查詢綁定了标簽的CCN清單。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回數量
        :type Limit: int
        :param OrderField: 排序欄位。支援：`CcnId` `CcnName` `CreateTime` `State` `QosLevel`
        :type OrderField: str
        :param OrderDirection: 排序方法。順序：`ASC`，倒序：`DESC`。
        :type OrderDirection: str
        """
        self.CcnIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.OrderDirection = None


    def _deserialize(self, params):
        self.CcnIds = params.get("CcnIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderField = params.get("OrderField")
        self.OrderDirection = params.get("OrderDirection")


class DescribeCcnsResponse(AbstractModel):
    """DescribeCcns返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的對象數。
        :type TotalCount: int
        :param CcnSet: CCN對象。
        :type CcnSet: list of CCN
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.CcnSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("CcnSet") is not None:
            self.CcnSet = []
            for item in params.get("CcnSet"):
                obj = CCN()
                obj._deserialize(item)
                self.CcnSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClassicLinkInstancesRequest(AbstractModel):
    """DescribeClassicLinkInstances請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 過濾條件。
<li>vpc-id - String - （過濾條件）VPC實例ID。</li>
<li>vm-ip - String - （過濾條件）基礎網絡雲伺服器IP。</li>
        :type Filters: list of FilterObject
        :param Offset: 偏移量
        :type Offset: str
        :param Limit: 返回數量
        :type Limit: str
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = FilterObject()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeClassicLinkInstancesResponse(AbstractModel):
    """DescribeClassicLinkInstances返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的實例數量。
        :type TotalCount: int
        :param ClassicLinkInstanceSet: 私有網絡和基礎網絡互通設備。
        :type ClassicLinkInstanceSet: list of ClassicLinkInstance
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ClassicLinkInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ClassicLinkInstanceSet") is not None:
            self.ClassicLinkInstanceSet = []
            for item in params.get("ClassicLinkInstanceSet"):
                obj = ClassicLinkInstance()
                obj._deserialize(item)
                self.ClassicLinkInstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCustomerGatewayVendorsRequest(AbstractModel):
    """DescribeCustomerGatewayVendors請求參數結構體

    """


class DescribeCustomerGatewayVendorsResponse(AbstractModel):
    """DescribeCustomerGatewayVendors返回參數結構體

    """

    def __init__(self):
        """
        :param CustomerGatewayVendorSet: 對端閘道廠商訊息對象。
        :type CustomerGatewayVendorSet: list of CustomerGatewayVendor
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CustomerGatewayVendorSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CustomerGatewayVendorSet") is not None:
            self.CustomerGatewayVendorSet = []
            for item in params.get("CustomerGatewayVendorSet"):
                obj = CustomerGatewayVendor()
                obj._deserialize(item)
                self.CustomerGatewayVendorSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCustomerGatewaysRequest(AbstractModel):
    """DescribeCustomerGateways請求參數結構體

    """

    def __init__(self):
        """
        :param CustomerGatewayIds: 對端閘道ID，例如：cgw-2wqq41m9。每次請求的實例的上限爲100。參數不支援同時指定CustomerGatewayIds和Filters。
        :type CustomerGatewayIds: list of str
        :param Filters: 過濾條件，詳見下表：實例過濾條件表。每次請求的Filters的上限爲10，Filter.Values的上限爲5。參數不支援同時指定CustomerGatewayIds和Filters。
<li>customer-gateway-id - String - （過濾條件）用戶閘道唯一ID形如：`cgw-mgp33pll`。</li>
<li>customer-gateway-name - String - （過濾條件）用戶閘道名稱形如：`test-cgw`。</li>
<li>ip-address - String - （過濾條件）公網網址形如：`58.211.1.12`。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。關于Offset的更進一步介紹請參考 API 簡介中的相關小節。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。
        :type Limit: int
        """
        self.CustomerGatewayIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.CustomerGatewayIds = params.get("CustomerGatewayIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeCustomerGatewaysResponse(AbstractModel):
    """DescribeCustomerGateways返回參數結構體

    """

    def __init__(self):
        """
        :param CustomerGatewaySet: 對端閘道對象清單
        :type CustomerGatewaySet: list of CustomerGateway
        :param TotalCount: 符合條件的實例數量。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CustomerGatewaySet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CustomerGatewaySet") is not None:
            self.CustomerGatewaySet = []
            for item in params.get("CustomerGatewaySet"):
                obj = CustomerGateway()
                obj._deserialize(item)
                self.CustomerGatewaySet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDirectConnectGatewayCcnRoutesRequest(AbstractModel):
    """DescribeDirectConnectGatewayCcnRoutes請求參數結構體

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: 專線閘道ID，形如：`dcg-prpqlmg1`。
        :type DirectConnectGatewayId: str
        :param CcnRouteType: 雲聯網路由學習類型，可選值：
<li>`BGP` - 自動學習。</li>
<li>`STATIC` - 靜态，即用戶配置，預設值。</li>
        :type CcnRouteType: str
        :param Offset: 偏移量。
        :type Offset: int
        :param Limit: 返回數量。
        :type Limit: int
        """
        self.DirectConnectGatewayId = None
        self.CcnRouteType = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.CcnRouteType = params.get("CcnRouteType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeDirectConnectGatewayCcnRoutesResponse(AbstractModel):
    """DescribeDirectConnectGatewayCcnRoutes返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的對象數。
        :type TotalCount: int
        :param RouteSet: 雲聯網路由（IDC網段）清單。
        :type RouteSet: list of DirectConnectGatewayCcnRoute
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RouteSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RouteSet") is not None:
            self.RouteSet = []
            for item in params.get("RouteSet"):
                obj = DirectConnectGatewayCcnRoute()
                obj._deserialize(item)
                self.RouteSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDirectConnectGatewaysRequest(AbstractModel):
    """DescribeDirectConnectGateways請求參數結構體

    """

    def __init__(self):
        """
        :param DirectConnectGatewayIds: 專線閘道唯一`ID`，形如：`dcg-9o233uri`。
        :type DirectConnectGatewayIds: list of str
        :param Filters: 過濾條件，參數不支援同時指定`DirectConnectGatewayIds`和`Filters`。
<li>direct-connect-gateway-id - String - 專線閘道唯一`ID`，形如：`dcg-9o233uri`。</li>
<li>direct-connect-gateway-name - String - 專線閘道名稱，預設模糊查詢。</li>
<li>direct-connect-gateway-ip - String - 專線閘道`IP`。</li>
<li>gateway-type - String - 閘道類型，可選值：`NORMAL`（普通型）、`NAT`（NAT型）。</li>
<li>network-type- String - 網絡類型，可選值：`VPC`（私有網絡類型）、`CCN`（雲聯網類型）。</li>
<li>ccn-id - String - 專線閘道所在雲聯網`ID`。</li>
<li>vpc-id - String - 專線閘道所在私有網絡`ID`。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量。
        :type Offset: int
        :param Limit: 返回數量。
        :type Limit: int
        """
        self.DirectConnectGatewayIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.DirectConnectGatewayIds = params.get("DirectConnectGatewayIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeDirectConnectGatewaysResponse(AbstractModel):
    """DescribeDirectConnectGateways返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的對象數。
        :type TotalCount: int
        :param DirectConnectGatewaySet: 專線閘道對象數組。
        :type DirectConnectGatewaySet: list of DirectConnectGateway
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DirectConnectGatewaySet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DirectConnectGatewaySet") is not None:
            self.DirectConnectGatewaySet = []
            for item in params.get("DirectConnectGatewaySet"):
                obj = DirectConnectGateway()
                obj._deserialize(item)
                self.DirectConnectGatewaySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFlowLogRequest(AbstractModel):
    """DescribeFlowLog請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: 私用網絡ID或者統一ID，建議使用統一ID
        :type VpcId: str
        :param FlowLogId: 流日志唯一ID
        :type FlowLogId: str
        """
        self.VpcId = None
        self.FlowLogId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.FlowLogId = params.get("FlowLogId")


class DescribeFlowLogResponse(AbstractModel):
    """DescribeFlowLog返回參數結構體

    """

    def __init__(self):
        """
        :param FlowLog: 流日志訊息
        :type FlowLog: list of FlowLog
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FlowLog = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FlowLog") is not None:
            self.FlowLog = []
            for item in params.get("FlowLog"):
                obj = FlowLog()
                obj._deserialize(item)
                self.FlowLog.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFlowLogsRequest(AbstractModel):
    """DescribeFlowLogs請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: 私用網絡ID或者統一ID，建議使用統一ID
        :type VpcId: str
        :param FlowLogId: 流日志唯一ID
        :type FlowLogId: str
        :param FlowLogName: 流日志實例名字
        :type FlowLogName: str
        :param ResourceType: 流日志所屬資源類型，VPC|SUBNET|NETWORKINTERFACE
        :type ResourceType: str
        :param ResourceId: 資源唯一ID
        :type ResourceId: str
        :param TrafficType: 流日志采集類型，ACCEPT|REJECT|ALL
        :type TrafficType: str
        :param CloudLogId: 流日志儲存ID
        :type CloudLogId: str
        :param CloudLogState: 流日志儲存ID狀态
        :type CloudLogState: str
        :param OrderField: 按某個欄位排序,支援欄位：flowLogName,createTime，預設按createTime
        :type OrderField: str
        :param OrderDirection: 升序（asc）還是降序（desc）,預設：desc
        :type OrderDirection: str
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Limit: 每頁行數，預設爲10
        :type Limit: int
        :param Filters: 過濾條件，參數不支援同時指定FlowLogIds和Filters。
<li>tag-key - String -是否必填：否- （過濾條件）按照标簽鍵進行過濾。</li>
<li>tag:tag-key - String - 是否必填：否 - （過濾條件）按照标簽鍵值對進行過濾。 tag-key使用具體的标簽鍵進行替換。</li>
        :type Filters: :class:`tencentcloud.vpc.v20170312.models.Filter`
        """
        self.VpcId = None
        self.FlowLogId = None
        self.FlowLogName = None
        self.ResourceType = None
        self.ResourceId = None
        self.TrafficType = None
        self.CloudLogId = None
        self.CloudLogState = None
        self.OrderField = None
        self.OrderDirection = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.FlowLogId = params.get("FlowLogId")
        self.FlowLogName = params.get("FlowLogName")
        self.ResourceType = params.get("ResourceType")
        self.ResourceId = params.get("ResourceId")
        self.TrafficType = params.get("TrafficType")
        self.CloudLogId = params.get("CloudLogId")
        self.CloudLogState = params.get("CloudLogState")
        self.OrderField = params.get("OrderField")
        self.OrderDirection = params.get("OrderDirection")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = Filter()
            self.Filters._deserialize(params.get("Filters"))


class DescribeFlowLogsResponse(AbstractModel):
    """DescribeFlowLogs返回參數結構體

    """

    def __init__(self):
        """
        :param FlowLog: 流日志實例集合
        :type FlowLog: list of FlowLog
        :param TotalNum: 流日志總數目
        :type TotalNum: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FlowLog = None
        self.TotalNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FlowLog") is not None:
            self.FlowLog = []
            for item in params.get("FlowLog"):
                obj = FlowLog()
                obj._deserialize(item)
                self.FlowLog.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.RequestId = params.get("RequestId")


class DescribeGatewayFlowMonitorDetailRequest(AbstractModel):
    """DescribeGatewayFlowMonitorDetail請求參數結構體

    """

    def __init__(self):
        """
        :param TimePoint: 時間點。表示要查詢這分鍾内的明細。如：`2019-02-28 18:15:20`，将查詢 `18:15` 這一分鍾内的明細。
        :type TimePoint: str
        :param VpnId: VPN閘道實例ID，形如：`vpn-ltjahce6`。
        :type VpnId: str
        :param DirectConnectGatewayId: 專線閘道實例ID，形如：`dcg-ltjahce6`。
        :type DirectConnectGatewayId: str
        :param PeeringConnectionId: 對等連接實例ID，形如：`pcx-ltjahce6`。
        :type PeeringConnectionId: str
        :param NatId: NAT閘道實例ID，形如：`nat-ltjahce6`。
        :type NatId: str
        :param Offset: 偏移量。
        :type Offset: int
        :param Limit: 返回數量。
        :type Limit: int
        :param OrderField: 排序欄位。支援 `InPkg` `OutPkg` `InTraffic` `OutTraffic`。
        :type OrderField: str
        :param OrderDirection: 排序方法。順序：`ASC`，倒序：`DESC`。
        :type OrderDirection: str
        """
        self.TimePoint = None
        self.VpnId = None
        self.DirectConnectGatewayId = None
        self.PeeringConnectionId = None
        self.NatId = None
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.OrderDirection = None


    def _deserialize(self, params):
        self.TimePoint = params.get("TimePoint")
        self.VpnId = params.get("VpnId")
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.PeeringConnectionId = params.get("PeeringConnectionId")
        self.NatId = params.get("NatId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderField = params.get("OrderField")
        self.OrderDirection = params.get("OrderDirection")


class DescribeGatewayFlowMonitorDetailResponse(AbstractModel):
    """DescribeGatewayFlowMonitorDetail返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的對象數。
        :type TotalCount: int
        :param GatewayFlowMonitorDetailSet: 閘道流量監控明細。
        :type GatewayFlowMonitorDetailSet: list of GatewayFlowMonitorDetail
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.GatewayFlowMonitorDetailSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("GatewayFlowMonitorDetailSet") is not None:
            self.GatewayFlowMonitorDetailSet = []
            for item in params.get("GatewayFlowMonitorDetailSet"):
                obj = GatewayFlowMonitorDetail()
                obj._deserialize(item)
                self.GatewayFlowMonitorDetailSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeGatewayFlowQosRequest(AbstractModel):
    """DescribeGatewayFlowQos請求參數結構體

    """

    def __init__(self):
        """
        :param GatewayId: 閘道實例ID，目前我們支援的閘道實例類型有，
專線閘道實例ID，形如，`dcg-ltjahce6`；
Nat閘道實例ID，形如，`nat-ltjahce6`；
VPN閘道實例ID，形如，`vpn-ltjahce6`。
        :type GatewayId: str
        :param IpAddresses: 限流的雲伺服器内網IP。
        :type IpAddresses: list of str
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。
        :type Limit: int
        """
        self.GatewayId = None
        self.IpAddresses = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.GatewayId = params.get("GatewayId")
        self.IpAddresses = params.get("IpAddresses")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeGatewayFlowQosResponse(AbstractModel):
    """DescribeGatewayFlowQos返回參數結構體

    """

    def __init__(self):
        """
        :param GatewayQosSet: 實例詳細訊息清單。
        :type GatewayQosSet: list of GatewayQos
        :param TotalCount: 符合條件的實例數量。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.GatewayQosSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GatewayQosSet") is not None:
            self.GatewayQosSet = []
            for item in params.get("GatewayQosSet"):
                obj = GatewayQos()
                obj._deserialize(item)
                self.GatewayQosSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeHaVipsRequest(AbstractModel):
    """DescribeHaVips請求參數結構體

    """

    def __init__(self):
        """
        :param HaVipIds: `HAVIP`唯一`ID`，形如：`havip-9o233uri`。
        :type HaVipIds: list of str
        :param Filters: 過濾條件，參數不支援同時指定`HaVipIds`和`Filters`。
<li>havip-id - String - `HAVIP`唯一`ID`，形如：`havip-9o233uri`。</li>
<li>havip-name - String - `HAVIP`名稱。</li>
<li>vpc-id - String - `HAVIP`所在私有網絡`ID`。</li>
<li>subnet-id - String - `HAVIP`所在子網`ID`。</li>
<li>address-ip - String - `HAVIP`綁定的彈性公網`IP`。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回數量
        :type Limit: int
        """
        self.HaVipIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.HaVipIds = params.get("HaVipIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeHaVipsResponse(AbstractModel):
    """DescribeHaVips返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的對象數。
        :type TotalCount: int
        :param HaVipSet: `HAVIP`對象數組。
        :type HaVipSet: list of HaVip
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.HaVipSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("HaVipSet") is not None:
            self.HaVipSet = []
            for item in params.get("HaVipSet"):
                obj = HaVip()
                obj._deserialize(item)
                self.HaVipSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIp6AddressesRequest(AbstractModel):
    """DescribeIp6Addresses請求參數結構體

    """

    def __init__(self):
        """
        :param Ip6AddressIds: 标識 IPV6 的唯一 ID 清單。IPV6 唯一 ID 形如：`eip-11112222`。參數不支援同時指定`Ip6AddressIds`和`Filters`。
        :type Ip6AddressIds: list of str
        :param Filters: 每次請求的`Filters`的上限爲10，`Filter.Values`的上限爲5。參數不支援同時指定`AddressIds`和`Filters`。詳細的過濾條件如下：
<li> address-ip - String - 是否必填：否 - （過濾條件）按照 EIP 的 IP 網址過濾。</li>
<li> network-interface-id - String - 是否必填：否 - （過濾條件）按照彈性網卡的唯一ID過濾。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。關于`Offset`的更進一步介紹請參考 API [簡介](https://cloud.tencent.com/document/api/213/11646)中的相關小節。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。關于`Limit`的更進一步介紹請參考 API [簡介](https://cloud.tencent.com/document/api/213/11646)中的相關小節。
        :type Limit: int
        """
        self.Ip6AddressIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Ip6AddressIds = params.get("Ip6AddressIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeIp6AddressesResponse(AbstractModel):
    """DescribeIp6Addresses返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的 IPV6 數量。
        :type TotalCount: int
        :param AddressSet: IPV6 詳細訊息清單。
        :type AddressSet: list of Address
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AddressSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AddressSet") is not None:
            self.AddressSet = []
            for item in params.get("AddressSet"):
                obj = Address()
                obj._deserialize(item)
                self.AddressSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIp6TranslatorQuotaRequest(AbstractModel):
    """DescribeIp6TranslatorQuota請求參數結構體

    """

    def __init__(self):
        """
        :param Ip6TranslatorIds: 待查詢IPV6轉換實例的唯一ID清單，形如ip6-xxxxxxxx
        :type Ip6TranslatorIds: list of str
        """
        self.Ip6TranslatorIds = None


    def _deserialize(self, params):
        self.Ip6TranslatorIds = params.get("Ip6TranslatorIds")


class DescribeIp6TranslatorQuotaResponse(AbstractModel):
    """DescribeIp6TranslatorQuota返回參數結構體

    """

    def __init__(self):
        """
        :param QuotaSet: 帳戶在指定地域的IPV6轉換實例及規則配額訊息
QUOTAID屬性是TOTAL_TRANSLATOR_QUOTA，表示帳戶在指定地域的IPV6轉換實例配額訊息；QUOTAID屬性是IPV6轉換實例唯一ID（形如ip6-xxxxxxxx），表示帳戶在該轉換實例允許創建的轉換規則配額
        :type QuotaSet: list of Quota
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.QuotaSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("QuotaSet") is not None:
            self.QuotaSet = []
            for item in params.get("QuotaSet"):
                obj = Quota()
                obj._deserialize(item)
                self.QuotaSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIp6TranslatorsRequest(AbstractModel):
    """DescribeIp6Translators請求參數結構體

    """

    def __init__(self):
        """
        :param Ip6TranslatorIds: IPV6轉換實例唯一ID數組，形如ip6-xxxxxxxx
        :type Ip6TranslatorIds: list of str
        :param Filters: 每次請求的`Filters`的上限爲10，`Filter.Values`的上限爲5。參數不支援同時指定`Ip6TranslatorIds`和`Filters`。詳細的過濾條件如下：
<li> ip6-translator-id - String - 是否必填：否 - （過濾條件）按照IPV6轉換實例的唯一ID過濾,形如ip6-xxxxxxx。</li>
<li> ip6-translator-vip6 - String - 是否必填：否 - （過濾條件）按照IPV6網址過濾。不支援模糊過濾。</li>
<li> ip6-translator-name - String - 是否必填：否 - （過濾條件）按照IPV6轉換實例名稱過濾。不支援模糊過濾。</li>
<li> ip6-translator-status - String - 是否必填：否 - （過濾條件）按照IPV6轉換實例的狀态過濾。狀态取值範圍爲"CREATING","RUNNING","DELETING","MODIFYING"
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。關于`Offset`的更進一步介紹請參考 API [簡介](https://cloud.tencent.com/document/api/213/11646)中的相關小節。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。關于`Limit`的更進一步介紹請參考 API [簡介](https://cloud.tencent.com/document/api/213/11646)中的相關小節。
        :type Limit: int
        """
        self.Ip6TranslatorIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Ip6TranslatorIds = params.get("Ip6TranslatorIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeIp6TranslatorsResponse(AbstractModel):
    """DescribeIp6Translators返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合過濾條件的IPV6轉換實例數量。
        :type TotalCount: int
        :param Ip6TranslatorSet: 符合過濾條件的IPV6轉換實例詳細訊息
        :type Ip6TranslatorSet: list of Ip6Translator
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Ip6TranslatorSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Ip6TranslatorSet") is not None:
            self.Ip6TranslatorSet = []
            for item in params.get("Ip6TranslatorSet"):
                obj = Ip6Translator()
                obj._deserialize(item)
                self.Ip6TranslatorSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNatGatewayDestinationIpPortTranslationNatRulesRequest(AbstractModel):
    """DescribeNatGatewayDestinationIpPortTranslationNatRules請求參數結構體

    """

    def __init__(self):
        """
        :param NatGatewayIds: NAT閘道ID。
        :type NatGatewayIds: list of str
        :param Filters: 過濾條件:
參數不支援同時指定NatGatewayIds和Filters。
<li> nat-gateway-id，NAT閘道的ID，如`nat-0yi4hekt`</li>
<li> vpc-id，私有網絡VPC的ID，如`vpc-0yi4hekt`</li>
<li> public-ip-address， 彈性IP，如`139.199.232.238`。</li>
<li>public-port， 公網端口。</li>
<li>private-ip-address， 内網IP，如`10.0.0.1`。</li>
<li>private-port， 内網端口。</li>
<li>description，規則描述。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。
        :type Limit: int
        """
        self.NatGatewayIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NatGatewayIds = params.get("NatGatewayIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeNatGatewayDestinationIpPortTranslationNatRulesResponse(AbstractModel):
    """DescribeNatGatewayDestinationIpPortTranslationNatRules返回參數結構體

    """

    def __init__(self):
        """
        :param NatGatewayDestinationIpPortTranslationNatRuleSet: NAT閘道端口轉發規則對象數組。
        :type NatGatewayDestinationIpPortTranslationNatRuleSet: list of NatGatewayDestinationIpPortTranslationNatRule
        :param TotalCount: 符合條件的NAT閘道端口轉發規則對象數目。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NatGatewayDestinationIpPortTranslationNatRuleSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NatGatewayDestinationIpPortTranslationNatRuleSet") is not None:
            self.NatGatewayDestinationIpPortTranslationNatRuleSet = []
            for item in params.get("NatGatewayDestinationIpPortTranslationNatRuleSet"):
                obj = NatGatewayDestinationIpPortTranslationNatRule()
                obj._deserialize(item)
                self.NatGatewayDestinationIpPortTranslationNatRuleSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNatGatewaysRequest(AbstractModel):
    """DescribeNatGateways請求參數結構體

    """

    def __init__(self):
        """
        :param NatGatewayIds: NAT閘道統一 ID，形如：`nat-123xx454`。
        :type NatGatewayIds: list of str
        :param Filters: 過濾條件，參數不支援同時指定NatGatewayIds和Filters。
<li>nat-gateway-id - String - （過濾條件）協議端口範本實例ID，形如：`nat-123xx454`。</li>
<li>vpc-id - String - （過濾條件）私有網絡 唯一ID，形如：`vpc-123xx454`。</li>
<li>nat-gateway-name - String - （過濾條件）協議端口範本實例ID，形如：`test_nat`。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。
        :type Limit: int
        """
        self.NatGatewayIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NatGatewayIds = params.get("NatGatewayIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeNatGatewaysResponse(AbstractModel):
    """DescribeNatGateways返回參數結構體

    """

    def __init__(self):
        """
        :param NatGatewaySet: NAT閘道對象數組。
        :type NatGatewaySet: list of NatGateway
        :param TotalCount: 符合條件的NAT閘道對象個數。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NatGatewaySet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NatGatewaySet") is not None:
            self.NatGatewaySet = []
            for item in params.get("NatGatewaySet"):
                obj = NatGateway()
                obj._deserialize(item)
                self.NatGatewaySet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNetDetectStatesRequest(AbstractModel):
    """DescribeNetDetectStates請求參數結構體

    """

    def __init__(self):
        """
        :param NetDetectIds: 網絡探測實例`ID`數組。形如：[`netd-12345678`]
        :type NetDetectIds: list of str
        :param Filters: 過濾條件，參數不支援同時指定NetDetectIds和Filters。
<li>net-detect-id - String - （過濾條件）網絡探測實例ID，形如：netd-12345678</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。
        :type Limit: int
        """
        self.NetDetectIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NetDetectIds = params.get("NetDetectIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeNetDetectStatesResponse(AbstractModel):
    """DescribeNetDetectStates返回參數結構體

    """

    def __init__(self):
        """
        :param NetDetectStateSet: 符合條件的網絡探測驗證結果對象數組。
注意：此欄位可能返回 null，表示取不到有效值。
        :type NetDetectStateSet: list of NetDetectState
        :param TotalCount: 符合條件的網絡探測驗證結果對象數量。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NetDetectStateSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetDetectStateSet") is not None:
            self.NetDetectStateSet = []
            for item in params.get("NetDetectStateSet"):
                obj = NetDetectState()
                obj._deserialize(item)
                self.NetDetectStateSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNetDetectsRequest(AbstractModel):
    """DescribeNetDetects請求參數結構體

    """

    def __init__(self):
        """
        :param NetDetectIds: 網絡探測實例`ID`數組。形如：[`netd-12345678`]
        :type NetDetectIds: list of str
        :param Filters: 過濾條件，參數不支援同時指定NetDetectIds和Filters。
<li>vpc-id - String - （過濾條件）VPC實例ID，形如：vpc-12345678</li>
<li>net-detect-id - String - （過濾條件）網絡探測實例ID，形如：netd-12345678</li>
<li>subnet-id - String - （過濾條件）子網實例ID，形如：subnet-12345678</li>
<li>net-detect-name - String - （過濾條件）網絡探測名稱</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。
        :type Limit: int
        """
        self.NetDetectIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NetDetectIds = params.get("NetDetectIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeNetDetectsResponse(AbstractModel):
    """DescribeNetDetects返回參數結構體

    """

    def __init__(self):
        """
        :param NetDetectSet: 符合條件的網絡探測對象數組。
注意：此欄位可能返回 null，表示取不到有效值。
        :type NetDetectSet: list of NetDetect
        :param TotalCount: 符合條件的網絡探測對象數量。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NetDetectSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetDetectSet") is not None:
            self.NetDetectSet = []
            for item in params.get("NetDetectSet"):
                obj = NetDetect()
                obj._deserialize(item)
                self.NetDetectSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNetworkAclsRequest(AbstractModel):
    """DescribeNetworkAcls請求參數結構體

    """

    def __init__(self):
        """
        :param NetworkAclIds: 網絡ACL實例ID數組。形如：[acl-12345678]。每次請求的實例的上限爲100。參數不支援同時指定NetworkAclIds和Filters。
        :type NetworkAclIds: list of str
        :param Filters: 過濾條件，參數不支援同時指定NetworkAclIds和Filters。
<li>vpc-id - String - （過濾條件）VPC實例ID，形如：vpc-12345678。</li>
<li>network-acl-id - String - （過濾條件）網絡ACL實例ID，形如：acl-12345678。</li>
<li>network-acl-name - String - （過濾條件）網絡ACL實例名稱。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最小值爲1，最大值爲100。
        :type Limit: int
        """
        self.NetworkAclIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NetworkAclIds = params.get("NetworkAclIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeNetworkAclsResponse(AbstractModel):
    """DescribeNetworkAcls返回參數結構體

    """

    def __init__(self):
        """
        :param NetworkAclSet: 實例詳細訊息清單。
        :type NetworkAclSet: list of NetworkAcl
        :param TotalCount: 符合條件的實例數量。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NetworkAclSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetworkAclSet") is not None:
            self.NetworkAclSet = []
            for item in params.get("NetworkAclSet"):
                obj = NetworkAcl()
                obj._deserialize(item)
                self.NetworkAclSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNetworkInterfaceLimitRequest(AbstractModel):
    """DescribeNetworkInterfaceLimit請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 要查詢的CVM實例ID或彈性網卡ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeNetworkInterfaceLimitResponse(AbstractModel):
    """DescribeNetworkInterfaceLimit返回參數結構體

    """

    def __init__(self):
        """
        :param EniQuantity: 彈性網卡配額
        :type EniQuantity: int
        :param EniPrivateIpAddressQuantity: 每個彈性網卡可以分配的IP配額
        :type EniPrivateIpAddressQuantity: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.EniQuantity = None
        self.EniPrivateIpAddressQuantity = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EniQuantity = params.get("EniQuantity")
        self.EniPrivateIpAddressQuantity = params.get("EniPrivateIpAddressQuantity")
        self.RequestId = params.get("RequestId")


class DescribeNetworkInterfacesRequest(AbstractModel):
    """DescribeNetworkInterfaces請求參數結構體

    """

    def __init__(self):
        """
        :param NetworkInterfaceIds: 彈性網卡實例ID查詢。形如：eni-pxir56ns。每次請求的實例的上限爲100。參數不支援同時指定NetworkInterfaceIds和Filters。
        :type NetworkInterfaceIds: list of str
        :param Filters: 過濾條件，參數不支援同時指定NetworkInterfaceIds和Filters。
<li>vpc-id - String - （過濾條件）VPC實例ID，形如：vpc-f49l6u0z。</li>
<li>subnet-id - String - （過濾條件）所屬子網實例ID，形如：subnet-f49l6u0z。</li>
<li>network-interface-id - String - （過濾條件）彈性網卡實例ID，形如：eni-5k56k7k7。</li>
<li>attachment.instance-id - String - （過濾條件）綁定的雲伺服器實例ID，形如：ins-3nqpdn3i。</li>
<li>groups.security-group-id - String - （過濾條件）綁定的安全組實例ID，例如：sg-f9ekbxeq。</li>
<li>network-interface-name - String - （過濾條件）網卡實例名稱。</li>
<li>network-interface-description - String - （過濾條件）網卡實例描述。</li>
<li>address-ip - String - （過濾條件）内網IPv4網址。</li>
<li>tag-key - String -是否必填：否- （過濾條件）按照标簽鍵進行過濾。使用請參考範例2</li>
<li>tag:tag-key - String - 是否必填：否 - （過濾條件）按照标簽鍵值對進行過濾。 tag-key使用具體的标簽鍵進行替換。使用請參考範例3。</li>
<li>is-primary - Boolean - 是否必填：否 - （過濾條件）按照是否主網卡進行過濾。值爲true時，僅過濾主網卡；值爲false時，僅過濾輔助網卡；次過濾參數爲提供時，同時過濾主網卡和輔助網卡。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。
        :type Limit: int
        """
        self.NetworkInterfaceIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NetworkInterfaceIds = params.get("NetworkInterfaceIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeNetworkInterfacesResponse(AbstractModel):
    """DescribeNetworkInterfaces返回參數結構體

    """

    def __init__(self):
        """
        :param NetworkInterfaceSet: 實例詳細訊息清單。
        :type NetworkInterfaceSet: list of NetworkInterface
        :param TotalCount: 符合條件的實例數量。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NetworkInterfaceSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetworkInterfaceSet") is not None:
            self.NetworkInterfaceSet = []
            for item in params.get("NetworkInterfaceSet"):
                obj = NetworkInterface()
                obj._deserialize(item)
                self.NetworkInterfaceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRouteConflictsRequest(AbstractModel):
    """DescribeRouteConflicts請求參數結構體

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表實例ID，例如：rtb-azd4dt1c。
        :type RouteTableId: str
        :param DestinationCidrBlocks: 要檢查的與之沖突的目的端清單
        :type DestinationCidrBlocks: list of str
        """
        self.RouteTableId = None
        self.DestinationCidrBlocks = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.DestinationCidrBlocks = params.get("DestinationCidrBlocks")


class DescribeRouteConflictsResponse(AbstractModel):
    """DescribeRouteConflicts返回參數結構體

    """

    def __init__(self):
        """
        :param RouteConflictSet: 路由策略沖突清單
        :type RouteConflictSet: list of RouteConflict
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RouteConflictSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RouteConflictSet") is not None:
            self.RouteConflictSet = []
            for item in params.get("RouteConflictSet"):
                obj = RouteConflict()
                obj._deserialize(item)
                self.RouteConflictSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRouteTablesRequest(AbstractModel):
    """DescribeRouteTables請求參數結構體

    """

    def __init__(self):
        """
        :param RouteTableIds: 路由表實例ID，例如：rtb-azd4dt1c。
        :type RouteTableIds: list of str
        :param Filters: 過濾條件，參數不支援同時指定RouteTableIds和Filters。
<li>route-table-id - String - （過濾條件）路由表實例ID。</li>
<li>route-table-name - String - （過濾條件）路由表名稱。</li>
<li>vpc-id - String - （過濾條件）VPC實例ID，形如：vpc-f49l6u0z。</li>
<li>association.main - String - （過濾條件）是否主路由表。</li>
<li>tag-key - String -是否必填：否- （過濾條件）按照标簽鍵進行過濾。</li>
<li>tag:tag-key - String - 是否必填：否 - （過濾條件）按照标簽鍵值對進行過濾。 tag-key使用具體的标簽鍵進行替換。使用請參考範例2。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量。
        :type Offset: str
        :param Limit: 請求對象個數。
        :type Limit: str
        """
        self.RouteTableIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.RouteTableIds = params.get("RouteTableIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeRouteTablesResponse(AbstractModel):
    """DescribeRouteTables返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的實例數量。
        :type TotalCount: int
        :param RouteTableSet: 路由表對象。
        :type RouteTableSet: list of RouteTable
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RouteTableSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RouteTableSet") is not None:
            self.RouteTableSet = []
            for item in params.get("RouteTableSet"):
                obj = RouteTable()
                obj._deserialize(item)
                self.RouteTableSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecurityGroupAssociationStatisticsRequest(AbstractModel):
    """DescribeSecurityGroupAssociationStatistics請求參數結構體

    """

    def __init__(self):
        """
        :param SecurityGroupIds: 安全實例ID，例如sg-33ocnj9n，可通過DescribeSecurityGroups獲取。
        :type SecurityGroupIds: list of str
        """
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.SecurityGroupIds = params.get("SecurityGroupIds")


class DescribeSecurityGroupAssociationStatisticsResponse(AbstractModel):
    """DescribeSecurityGroupAssociationStatistics返回參數結構體

    """

    def __init__(self):
        """
        :param SecurityGroupAssociationStatisticsSet: 安全組關聯實例統計。
        :type SecurityGroupAssociationStatisticsSet: list of SecurityGroupAssociationStatistics
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SecurityGroupAssociationStatisticsSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroupAssociationStatisticsSet") is not None:
            self.SecurityGroupAssociationStatisticsSet = []
            for item in params.get("SecurityGroupAssociationStatisticsSet"):
                obj = SecurityGroupAssociationStatistics()
                obj._deserialize(item)
                self.SecurityGroupAssociationStatisticsSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecurityGroupLimitsRequest(AbstractModel):
    """DescribeSecurityGroupLimits請求參數結構體

    """


class DescribeSecurityGroupLimitsResponse(AbstractModel):
    """DescribeSecurityGroupLimits返回參數結構體

    """

    def __init__(self):
        """
        :param SecurityGroupLimitSet: 用戶安全組配額限制。
        :type SecurityGroupLimitSet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupLimitSet`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SecurityGroupLimitSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroupLimitSet") is not None:
            self.SecurityGroupLimitSet = SecurityGroupLimitSet()
            self.SecurityGroupLimitSet._deserialize(params.get("SecurityGroupLimitSet"))
        self.RequestId = params.get("RequestId")


class DescribeSecurityGroupPoliciesRequest(AbstractModel):
    """DescribeSecurityGroupPolicies請求參數結構體

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全組實例ID，例如：sg-33ocnj9n，可通過DescribeSecurityGroups獲取。
        :type SecurityGroupId: str
        """
        self.SecurityGroupId = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")


class DescribeSecurityGroupPoliciesResponse(AbstractModel):
    """DescribeSecurityGroupPolicies返回參數結構體

    """

    def __init__(self):
        """
        :param SecurityGroupPolicySet: 安全組規則集合。
        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SecurityGroupPolicySet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = SecurityGroupPolicySet()
            self.SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))
        self.RequestId = params.get("RequestId")


class DescribeSecurityGroupReferencesRequest(AbstractModel):
    """DescribeSecurityGroupReferences請求參數結構體

    """

    def __init__(self):
        """
        :param SecurityGroupIds: 安全組實例ID數組。格式如：['sg-12345678']
        :type SecurityGroupIds: list of str
        """
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.SecurityGroupIds = params.get("SecurityGroupIds")


class DescribeSecurityGroupReferencesResponse(AbstractModel):
    """DescribeSecurityGroupReferences返回參數結構體

    """

    def __init__(self):
        """
        :param ReferredSecurityGroupSet: 安全組被引用訊息。
        :type ReferredSecurityGroupSet: list of ReferredSecurityGroup
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ReferredSecurityGroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ReferredSecurityGroupSet") is not None:
            self.ReferredSecurityGroupSet = []
            for item in params.get("ReferredSecurityGroupSet"):
                obj = ReferredSecurityGroup()
                obj._deserialize(item)
                self.ReferredSecurityGroupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecurityGroupsRequest(AbstractModel):
    """DescribeSecurityGroups請求參數結構體

    """

    def __init__(self):
        """
        :param SecurityGroupIds: 安全組實例ID，例如：sg-33ocnj9n，可通過DescribeSecurityGroups獲取。每次請求的實例的上限爲100。參數不支援同時指定SecurityGroupIds和Filters。
        :type SecurityGroupIds: list of str
        :param Filters: 過濾條件，參數不支援同時指定SecurityGroupIds和Filters。
<li>security-group-id - String - （過濾條件）安全組ID。</li>
<li>project-id - Integer - （過濾條件）項目ID。</li>
<li>security-group-name - String - （過濾條件）安全組名稱。</li>
<li>tag-key - String -是否必填：否- （過濾條件）按照标簽鍵進行過濾。使用請參考範例2。</li>
<li>tag:tag-key - String - 是否必填：否 - （過濾條件）按照标簽鍵值對進行過濾。 tag-key使用具體的标簽鍵進行替換。使用請參考範例3。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。
        :type Offset: str
        :param Limit: 返回數量，預設爲20，最大值爲100。
        :type Limit: str
        """
        self.SecurityGroupIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeSecurityGroupsResponse(AbstractModel):
    """DescribeSecurityGroups返回參數結構體

    """

    def __init__(self):
        """
        :param SecurityGroupSet: 安全組對象。
        :type SecurityGroupSet: list of SecurityGroup
        :param TotalCount: 符合條件的實例數量。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SecurityGroupSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroupSet") is not None:
            self.SecurityGroupSet = []
            for item in params.get("SecurityGroupSet"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self.SecurityGroupSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeServiceTemplateGroupsRequest(AbstractModel):
    """DescribeServiceTemplateGroups請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 過濾條件。
<li>service-template-group-name - String - （過濾條件）協議端口範本集合名稱。</li>
<li>service-template-group-id - String - （過濾條件）協議端口範本集合實例ID，例如：ppmg-e6dy460g。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。
        :type Offset: str
        :param Limit: 返回數量，預設爲20，最大值爲100。
        :type Limit: str
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeServiceTemplateGroupsResponse(AbstractModel):
    """DescribeServiceTemplateGroups返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的實例數量。
        :type TotalCount: int
        :param ServiceTemplateGroupSet: 協議端口範本集合。
        :type ServiceTemplateGroupSet: list of ServiceTemplateGroup
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ServiceTemplateGroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ServiceTemplateGroupSet") is not None:
            self.ServiceTemplateGroupSet = []
            for item in params.get("ServiceTemplateGroupSet"):
                obj = ServiceTemplateGroup()
                obj._deserialize(item)
                self.ServiceTemplateGroupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeServiceTemplatesRequest(AbstractModel):
    """DescribeServiceTemplates請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 過濾條件。
<li>service-template-name - String - （過濾條件）協議端口範本名稱。</li>
<li>service-template-id - String - （過濾條件）協議端口範本實例ID，例如：ppm-e6dy460g。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。
        :type Offset: str
        :param Limit: 返回數量，預設爲20，最大值爲100。
        :type Limit: str
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeServiceTemplatesResponse(AbstractModel):
    """DescribeServiceTemplates返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的實例數量。
        :type TotalCount: int
        :param ServiceTemplateSet: 協議端口範本對象。
        :type ServiceTemplateSet: list of ServiceTemplate
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ServiceTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ServiceTemplateSet") is not None:
            self.ServiceTemplateSet = []
            for item in params.get("ServiceTemplateSet"):
                obj = ServiceTemplate()
                obj._deserialize(item)
                self.ServiceTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSubnetsRequest(AbstractModel):
    """DescribeSubnets請求參數結構體

    """

    def __init__(self):
        """
        :param SubnetIds: 子網實例ID查詢。形如：subnet-pxir56ns。每次請求的實例的上限爲100。參數不支援同時指定SubnetIds和Filters。
        :type SubnetIds: list of str
        :param Filters: 過濾條件，參數不支援同時指定SubnetIds和Filters。
<li>subnet-id - String - （過濾條件）Subnet實例名稱。</li>
<li>vpc-id - String - （過濾條件）VPC實例ID，形如：vpc-f49l6u0z。</li>
<li>cidr-block - String - （過濾條件）子網網段，形如: 192.168.1.0 。</li>
<li>is-default - Boolean - （過濾條件）是否是預設子網。</li>
<li>is-remote-vpc-snat - Boolean - （過濾條件）是否爲VPC SNAT網址池子網。</li>
<li>subnet-name - String - （過濾條件）子網名稱。</li>
<li>zone - String - （過濾條件）可用區。</li>
<li>tag-key - String -是否必填：否- （過濾條件）按照标簽鍵進行過濾。</li>
<li>tag:tag-key - String - 是否必填：否 - （過濾條件）按照标簽鍵值對進行過濾。 tag-key使用具體的标簽鍵進行替換。使用請參考範例2。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。
        :type Offset: str
        :param Limit: 返回數量，預設爲20，最大值爲100。
        :type Limit: str
        """
        self.SubnetIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SubnetIds = params.get("SubnetIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeSubnetsResponse(AbstractModel):
    """DescribeSubnets返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的實例數量。
        :type TotalCount: int
        :param SubnetSet: 子網對象。
        :type SubnetSet: list of Subnet
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SubnetSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SubnetSet") is not None:
            self.SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = Subnet()
                obj._deserialize(item)
                self.SubnetSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskResultRequest(AbstractModel):
    """DescribeTaskResult請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步任務ID。TaskId和DealName必填一個參數
        :type TaskId: int
        :param DealName: 計費訂單号。TaskId和DealName必填一個參數
        :type DealName: str
        """
        self.TaskId = None
        self.DealName = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.DealName = params.get("DealName")


class DescribeTaskResultResponse(AbstractModel):
    """DescribeTaskResult返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param Result: 執行結果，包括"SUCCESS", "FAILED", "RUNNING"
        :type Result: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeTemplateLimitsRequest(AbstractModel):
    """DescribeTemplateLimits請求參數結構體

    """


class DescribeTemplateLimitsResponse(AbstractModel):
    """DescribeTemplateLimits返回參數結構體

    """

    def __init__(self):
        """
        :param TemplateLimit: 參數範本配額對象。
        :type TemplateLimit: :class:`tencentcloud.vpc.v20170312.models.TemplateLimit`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TemplateLimit = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TemplateLimit") is not None:
            self.TemplateLimit = TemplateLimit()
            self.TemplateLimit._deserialize(params.get("TemplateLimit"))
        self.RequestId = params.get("RequestId")


class DescribeVpcInstancesRequest(AbstractModel):
    """DescribeVpcInstances請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 過濾條件，參數不支援同時指定RouteTableIds和Filters。
<li>vpc-id - String - （過濾條件）VPC實例ID，形如：vpc-f49l6u0z。</li>
<li>instance-id - String - （過濾條件）雲主機實例ID。</li>
<li>instance-name - String - （過濾條件）雲主機名稱。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量。
        :type Offset: int
        :param Limit: 請求對象個數。
        :type Limit: int
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeVpcInstancesResponse(AbstractModel):
    """DescribeVpcInstances返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceSet: 雲主機實例清單。
        :type InstanceSet: list of CvmInstance
        :param TotalCount: 滿足條件的雲主機實例個數。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = CvmInstance()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeVpcIpv6AddressesRequest(AbstractModel):
    """DescribeVpcIpv6Addresses請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: `VPC`實例`ID`，形如：`vpc-f49l6u0z`。
        :type VpcId: str
        :param Ipv6Addresses: `IP`網址清單，批次查詢單次請求最多支援`10`個。
        :type Ipv6Addresses: list of str
        :param Offset: 偏移量。
        :type Offset: int
        :param Limit: 返回數量。
        :type Limit: int
        """
        self.VpcId = None
        self.Ipv6Addresses = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.Ipv6Addresses = params.get("Ipv6Addresses")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeVpcIpv6AddressesResponse(AbstractModel):
    """DescribeVpcIpv6Addresses返回參數結構體

    """

    def __init__(self):
        """
        :param Ipv6AddressSet: `IPv6`網址清單。
        :type Ipv6AddressSet: list of VpcIpv6Address
        :param TotalCount: `IPv6`網址總數。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Ipv6AddressSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Ipv6AddressSet") is not None:
            self.Ipv6AddressSet = []
            for item in params.get("Ipv6AddressSet"):
                obj = VpcIpv6Address()
                obj._deserialize(item)
                self.Ipv6AddressSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeVpcLimitsRequest(AbstractModel):
    """DescribeVpcLimits請求參數結構體

    """

    def __init__(self):
        """
        :param LimitTypes: 配額名稱。每次最大查詢100個配額類型。
        :type LimitTypes: list of str
        """
        self.LimitTypes = None


    def _deserialize(self, params):
        self.LimitTypes = params.get("LimitTypes")


class DescribeVpcLimitsResponse(AbstractModel):
    """DescribeVpcLimits返回參數結構體

    """

    def __init__(self):
        """
        :param VpcLimitSet: 私有網絡配額
        :type VpcLimitSet: list of VpcLimit
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.VpcLimitSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VpcLimitSet") is not None:
            self.VpcLimitSet = []
            for item in params.get("VpcLimitSet"):
                obj = VpcLimit()
                obj._deserialize(item)
                self.VpcLimitSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVpcPrivateIpAddressesRequest(AbstractModel):
    """DescribeVpcPrivateIpAddresses請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: `VPC`實例`ID`，形如：`vpc-f49l6u0z`。
        :type VpcId: str
        :param PrivateIpAddresses: 内網`IP`網址清單，批次查詢單次請求最多支援`10`個。
        :type PrivateIpAddresses: list of str
        """
        self.VpcId = None
        self.PrivateIpAddresses = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")


class DescribeVpcPrivateIpAddressesResponse(AbstractModel):
    """DescribeVpcPrivateIpAddresses返回參數結構體

    """

    def __init__(self):
        """
        :param VpcPrivateIpAddressSet: 内網`IP`網址訊息清單。
        :type VpcPrivateIpAddressSet: list of VpcPrivateIpAddress
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.VpcPrivateIpAddressSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VpcPrivateIpAddressSet") is not None:
            self.VpcPrivateIpAddressSet = []
            for item in params.get("VpcPrivateIpAddressSet"):
                obj = VpcPrivateIpAddress()
                obj._deserialize(item)
                self.VpcPrivateIpAddressSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVpcResourceDashboardRequest(AbstractModel):
    """DescribeVpcResourceDashboard請求參數結構體

    """

    def __init__(self):
        """
        :param VpcIds: Vpc實例ID，例如：vpc-f1xjkw1b。
        :type VpcIds: list of str
        """
        self.VpcIds = None


    def _deserialize(self, params):
        self.VpcIds = params.get("VpcIds")


class DescribeVpcResourceDashboardResponse(AbstractModel):
    """DescribeVpcResourceDashboard返回參數結構體

    """

    def __init__(self):
        """
        :param ResourceDashboardSet: 資源對象清單。
        :type ResourceDashboardSet: list of ResourceDashboard
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ResourceDashboardSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResourceDashboardSet") is not None:
            self.ResourceDashboardSet = []
            for item in params.get("ResourceDashboardSet"):
                obj = ResourceDashboard()
                obj._deserialize(item)
                self.ResourceDashboardSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVpcsRequest(AbstractModel):
    """DescribeVpcs請求參數結構體

    """

    def __init__(self):
        """
        :param VpcIds: VPC實例ID。形如：vpc-f49l6u0z。每次請求的實例的上限爲100。參數不支援同時指定VpcIds和Filters。
        :type VpcIds: list of str
        :param Filters: 過濾條件，參數不支援同時指定VpcIds和Filters。
<li>vpc-name - String - （過濾條件）VPC實例名稱。</li>
<li>is-default - String - （過濾條件）是否預設VPC。</li>
<li>vpc-id - String - （過濾條件）VPC實例ID形如：vpc-f49l6u0z。</li>
<li>cidr-block - String - （過濾條件）vpc的cidr。</li>
<li>tag-key - String -是否必填：否- （過濾條件）按照标簽鍵進行過濾。</li>
<li>tag:tag-key - String - 是否必填：否 - （過濾條件）按照标簽鍵值對進行過濾。 tag-key使用具體的标簽鍵進行替換。使用請參考範例2。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。
        :type Offset: str
        :param Limit: 返回數量，預設爲20，最大值爲100。
        :type Limit: str
        """
        self.VpcIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.VpcIds = params.get("VpcIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeVpcsResponse(AbstractModel):
    """DescribeVpcs返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的對象數。
        :type TotalCount: int
        :param VpcSet: VPC對象。
        :type VpcSet: list of Vpc
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.VpcSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VpcSet") is not None:
            self.VpcSet = []
            for item in params.get("VpcSet"):
                obj = Vpc()
                obj._deserialize(item)
                self.VpcSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVpnConnectionsRequest(AbstractModel):
    """DescribeVpnConnections請求參數結構體

    """

    def __init__(self):
        """
        :param VpnConnectionIds: VPN通道實例ID。形如：vpnx-f49l6u0z。每次請求的實例的上限爲100。參數不支援同時指定VpnConnectionIds和Filters。
        :type VpnConnectionIds: list of str
        :param Filters: 過濾條件。每次請求的Filters的上限爲10，Filter.Values的上限爲5。參數不支援同時指定VpnConnectionIds和Filters。
<li>vpc-id - String - VPC實例ID，形如：`vpc-0a36uwkr`。</li>
<li>vpn-gateway-id - String - VPN閘道實例ID，形如：`vpngw-p4lmqawn`。</li>
<li>customer-gateway-id - String - 對端閘道實例ID，形如：`cgw-l4rblw63`。</li>
<li>vpn-connection-name - String - 通道名稱，形如：`test-vpn`。</li>
<li>vpn-connection-id - String - 通道實例ID，形如：`vpnx-5p7vkch8"`。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。關于Offset的更進一步介紹請參考 API 簡介中的相關小節。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。
        :type Limit: int
        """
        self.VpnConnectionIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.VpnConnectionIds = params.get("VpnConnectionIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeVpnConnectionsResponse(AbstractModel):
    """DescribeVpnConnections返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的實例數量。
        :type TotalCount: int
        :param VpnConnectionSet: VPN通道實例。
        :type VpnConnectionSet: list of VpnConnection
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.VpnConnectionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VpnConnectionSet") is not None:
            self.VpnConnectionSet = []
            for item in params.get("VpnConnectionSet"):
                obj = VpnConnection()
                obj._deserialize(item)
                self.VpnConnectionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVpnGatewayCcnRoutesRequest(AbstractModel):
    """DescribeVpnGatewayCcnRoutes請求參數結構體

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN閘道實例ID
        :type VpnGatewayId: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回數量
        :type Limit: int
        """
        self.VpnGatewayId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeVpnGatewayCcnRoutesResponse(AbstractModel):
    """DescribeVpnGatewayCcnRoutes返回參數結構體

    """

    def __init__(self):
        """
        :param RouteSet: 雲聯網路由（IDC網段）清單。
        :type RouteSet: list of VpngwCcnRoutes
        :param TotalCount: 符合條件的對象數。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RouteSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RouteSet") is not None:
            self.RouteSet = []
            for item in params.get("RouteSet"):
                obj = VpngwCcnRoutes()
                obj._deserialize(item)
                self.RouteSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeVpnGatewaysRequest(AbstractModel):
    """DescribeVpnGateways請求參數結構體

    """

    def __init__(self):
        """
        :param VpnGatewayIds: VPN閘道實例ID。形如：vpngw-f49l6u0z。每次請求的實例的上限爲100。參數不支援同時指定VpnGatewayIds和Filters。
        :type VpnGatewayIds: list of str
        :param Filters: 過濾條件，參數不支援同時指定VpnGatewayIds和Filters。
<li>vpc-id - String - （過濾條件）VPC實例ID形如：vpc-f49l6u0z。</li>
<li>vpn-gateway-id - String - （過濾條件）VPN實例ID形如：vpngw-5aluhh9t。</li>
<li>vpn-gateway-name - String - （過濾條件）VPN實例名稱。</li>
<li>type - String - （過濾條件）VPN閘道類型：'IPSEC', 'SSL'。</li>
<li>public-ip-address- String - （過濾條件）公網IP。</li>
<li>renew-flag - String - （過濾條件）閘道續約類型，手動續約：'NOTIFY_AND_MANUAL_RENEW'、自動續約：'NOTIFY_AND_AUTO_RENEW'。</li>
<li>zone - String - （過濾條件）VPN所在可用區，形如：ap-guangzhou-2。</li>
        :type Filters: list of FilterObject
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 請求對象個數
        :type Limit: int
        """
        self.VpnGatewayIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.VpnGatewayIds = params.get("VpnGatewayIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = FilterObject()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeVpnGatewaysResponse(AbstractModel):
    """DescribeVpnGateways返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的實例數量。
        :type TotalCount: int
        :param VpnGatewaySet: VPN閘道實例詳細訊息清單。
        :type VpnGatewaySet: list of VpnGateway
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.VpnGatewaySet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VpnGatewaySet") is not None:
            self.VpnGatewaySet = []
            for item in params.get("VpnGatewaySet"):
                obj = VpnGateway()
                obj._deserialize(item)
                self.VpnGatewaySet.append(obj)
        self.RequestId = params.get("RequestId")


class DestinationIpPortTranslationNatRule(AbstractModel):
    """NAT閘道的端口轉發規則

    """

    def __init__(self):
        """
        :param IpProtocol: 網絡協議，可選值：`TCP`、`UDP`。
        :type IpProtocol: str
        :param PublicIpAddress: 彈性IP。
        :type PublicIpAddress: str
        :param PublicPort: 公網端口。
        :type PublicPort: int
        :param PrivateIpAddress: 内網網址。
        :type PrivateIpAddress: str
        :param PrivatePort: 内網端口。
        :type PrivatePort: int
        :param Description: NAT閘道轉發規則描述。
        :type Description: str
        """
        self.IpProtocol = None
        self.PublicIpAddress = None
        self.PublicPort = None
        self.PrivateIpAddress = None
        self.PrivatePort = None
        self.Description = None


    def _deserialize(self, params):
        self.IpProtocol = params.get("IpProtocol")
        self.PublicIpAddress = params.get("PublicIpAddress")
        self.PublicPort = params.get("PublicPort")
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        self.PrivatePort = params.get("PrivatePort")
        self.Description = params.get("Description")


class DetachCcnInstancesRequest(AbstractModel):
    """DetachCcnInstances請求參數結構體

    """

    def __init__(self):
        """
        :param CcnId: CCN實例ID。形如：ccn-f49l6u0z。
        :type CcnId: str
        :param Instances: 要解關聯網絡實例清單
        :type Instances: list of CcnInstance
        """
        self.CcnId = None
        self.Instances = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = CcnInstance()
                obj._deserialize(item)
                self.Instances.append(obj)


class DetachCcnInstancesResponse(AbstractModel):
    """DetachCcnInstances返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DetachClassicLinkVpcRequest(AbstractModel):
    """DetachClassicLinkVpc請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: VPC實例ID。可通過DescribeVpcs介面返回值中的VpcId獲取。
        :type VpcId: str
        :param InstanceIds: CVM實例ID查詢。形如：ins-r8hr2upy。
        :type InstanceIds: list of str
        """
        self.VpcId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.InstanceIds = params.get("InstanceIds")


class DetachClassicLinkVpcResponse(AbstractModel):
    """DetachClassicLinkVpc返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DetachNetworkInterfaceRequest(AbstractModel):
    """DetachNetworkInterface請求參數結構體

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 彈性網卡實例ID，例如：eni-m6dyj72l。
        :type NetworkInterfaceId: str
        :param InstanceId: CVM實例ID。形如：ins-r8hr2upy。
        :type InstanceId: str
        """
        self.NetworkInterfaceId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.InstanceId = params.get("InstanceId")


class DetachNetworkInterfaceResponse(AbstractModel):
    """DetachNetworkInterface返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DirectConnectGateway(AbstractModel):
    """專線閘道對象。

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: 專線閘道`ID`。
        :type DirectConnectGatewayId: str
        :param DirectConnectGatewayName: 專線閘道名稱。
        :type DirectConnectGatewayName: str
        :param VpcId: 專線閘道關聯`VPC`實例`ID`。
        :type VpcId: str
        :param NetworkType: 關聯網絡類型：
<li>`VPC` - 私有網絡</li>
<li>`CCN` - 雲聯網</li>
        :type NetworkType: str
        :param NetworkInstanceId: 關聯網絡實例`ID`：
<li>`NetworkType`爲`VPC`時，這裏爲私有網絡實例`ID`</li>
<li>`NetworkType`爲`CCN`時，這裏爲雲聯網實例`ID`</li>
        :type NetworkInstanceId: str
        :param GatewayType: 閘道類型：
<li>NORMAL - 标準型，注：雲聯網只支援标準型</li>
<li>NAT - NAT型</li>
NAT類型支援網絡網址轉換配置，類型确定後不能修改；一個私有網絡可以創建一個NAT類型的專線閘道和一個非NAT類型的專線閘道
        :type GatewayType: str
        :param CreateTime: 創建時間。
        :type CreateTime: str
        :param DirectConnectGatewayIp: 專線閘道IP。
        :type DirectConnectGatewayIp: str
        :param CcnId: 專線閘道關聯`CCN`實例`ID`。
        :type CcnId: str
        :param CcnRouteType: 雲聯網路由學習類型：
<li>`BGP` - 自動學習。</li>
<li>`STATIC` - 靜态，即用戶配置。</li>
        :type CcnRouteType: str
        :param EnableBGP: 是否啓用BGP。
        :type EnableBGP: bool
        :param EnableBGPCommunity: 開啓和關閉BGP的community屬性。
        :type EnableBGPCommunity: bool
        """
        self.DirectConnectGatewayId = None
        self.DirectConnectGatewayName = None
        self.VpcId = None
        self.NetworkType = None
        self.NetworkInstanceId = None
        self.GatewayType = None
        self.CreateTime = None
        self.DirectConnectGatewayIp = None
        self.CcnId = None
        self.CcnRouteType = None
        self.EnableBGP = None
        self.EnableBGPCommunity = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.DirectConnectGatewayName = params.get("DirectConnectGatewayName")
        self.VpcId = params.get("VpcId")
        self.NetworkType = params.get("NetworkType")
        self.NetworkInstanceId = params.get("NetworkInstanceId")
        self.GatewayType = params.get("GatewayType")
        self.CreateTime = params.get("CreateTime")
        self.DirectConnectGatewayIp = params.get("DirectConnectGatewayIp")
        self.CcnId = params.get("CcnId")
        self.CcnRouteType = params.get("CcnRouteType")
        self.EnableBGP = params.get("EnableBGP")
        self.EnableBGPCommunity = params.get("EnableBGPCommunity")


class DirectConnectGatewayCcnRoute(AbstractModel):
    """專線閘道雲聯網路由（IDC網段）對象

    """

    def __init__(self):
        """
        :param RouteId: 路由ID。
        :type RouteId: str
        :param DestinationCidrBlock: IDC網段。
        :type DestinationCidrBlock: str
        :param ASPath: `BGP`的`AS-Path`屬性。
        :type ASPath: list of str
        """
        self.RouteId = None
        self.DestinationCidrBlock = None
        self.ASPath = None


    def _deserialize(self, params):
        self.RouteId = params.get("RouteId")
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        self.ASPath = params.get("ASPath")


class DisableCcnRoutesRequest(AbstractModel):
    """DisableCcnRoutes請求參數結構體

    """

    def __init__(self):
        """
        :param CcnId: CCN實例ID。形如：ccn-f49l6u0z。
        :type CcnId: str
        :param RouteIds: CCN路由策略唯一ID。形如：ccnr-f49l6u0z。
        :type RouteIds: list of str
        """
        self.CcnId = None
        self.RouteIds = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.RouteIds = params.get("RouteIds")


class DisableCcnRoutesResponse(AbstractModel):
    """DisableCcnRoutes返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableGatewayFlowMonitorRequest(AbstractModel):
    """DisableGatewayFlowMonitor請求參數結構體

    """

    def __init__(self):
        """
        :param GatewayId: 閘道實例ID，目前我們支援的閘道實例類型有，
專線閘道實例ID，形如，`dcg-ltjahce6`；
Nat閘道實例ID，形如，`nat-ltjahce6`；
VPN閘道實例ID，形如，`vpn-ltjahce6`。
        :type GatewayId: str
        """
        self.GatewayId = None


    def _deserialize(self, params):
        self.GatewayId = params.get("GatewayId")


class DisableGatewayFlowMonitorResponse(AbstractModel):
    """DisableGatewayFlowMonitor返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableRoutesRequest(AbstractModel):
    """DisableRoutes請求參數結構體

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表唯一ID。
        :type RouteTableId: str
        :param RouteIds: 路由策略唯一ID。
        :type RouteIds: list of int non-negative
        """
        self.RouteTableId = None
        self.RouteIds = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RouteIds = params.get("RouteIds")


class DisableRoutesResponse(AbstractModel):
    """DisableRoutes返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisassociateAddressRequest(AbstractModel):
    """DisassociateAddress請求參數結構體

    """

    def __init__(self):
        """
        :param AddressId: 标識 EIP 的唯一 ID。EIP 唯一 ID 形如：`eip-11112222`。
        :type AddressId: str
        :param ReallocateNormalPublicIp: 表示解綁 EIP 之後是否分配普通公網 IP。取值範圍：<br><li>TRUE：表示解綁 EIP 之後分配普通公網 IP。<br><li>FALSE：表示解綁 EIP 之後不分配普通公網 IP。<br>預設取值：FALSE。<br><br>只有滿足以下條件時才能指定該參數：<br><li> 只有在解綁主網卡的主内網 IP 上的 EIP 時才能指定該參數。<br><li>解綁 EIP 後重新分配普通公網 IP 操作一個賬号每天最多操作 10 次；詳情可通過 [DescribeAddressQuota](https://cloud.tencent.com/document/api/213/1378) 介面獲取。
        :type ReallocateNormalPublicIp: bool
        """
        self.AddressId = None
        self.ReallocateNormalPublicIp = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.ReallocateNormalPublicIp = params.get("ReallocateNormalPublicIp")


class DisassociateAddressResponse(AbstractModel):
    """DisassociateAddress返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步任務TaskId。可以使用[DescribeTaskResult](https://cloud.tencent.com/document/api/215/36271)介面查詢任務狀态。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DisassociateNatGatewayAddressRequest(AbstractModel):
    """DisassociateNatGatewayAddress請求參數結構體

    """

    def __init__(self):
        """
        :param NatGatewayId: NAT閘道的ID，形如：`nat-df45454`。
        :type NatGatewayId: str
        :param PublicIpAddresses: 綁定NAT閘道的彈性IP數組。
        :type PublicIpAddresses: list of str
        """
        self.NatGatewayId = None
        self.PublicIpAddresses = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        self.PublicIpAddresses = params.get("PublicIpAddresses")


class DisassociateNatGatewayAddressResponse(AbstractModel):
    """DisassociateNatGatewayAddress返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisassociateNetworkAclSubnetsRequest(AbstractModel):
    """DisassociateNetworkAclSubnets請求參數結構體

    """

    def __init__(self):
        """
        :param NetworkAclId: 網絡ACL實例ID。例如：acl-12345678。
        :type NetworkAclId: str
        :param SubnetIds: 子網實例ID數組。例如：[subnet-12345678]
        :type SubnetIds: list of str
        """
        self.NetworkAclId = None
        self.SubnetIds = None


    def _deserialize(self, params):
        self.NetworkAclId = params.get("NetworkAclId")
        self.SubnetIds = params.get("SubnetIds")


class DisassociateNetworkAclSubnetsResponse(AbstractModel):
    """DisassociateNetworkAclSubnets返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisassociateNetworkInterfaceSecurityGroupsRequest(AbstractModel):
    """DisassociateNetworkInterfaceSecurityGroups請求參數結構體

    """

    def __init__(self):
        """
        :param NetworkInterfaceIds: 彈性網卡實例ID。形如：eni-pxir56ns。每次請求的實例的上限爲100。
        :type NetworkInterfaceIds: list of str
        :param SecurityGroupIds: 安全組實例ID，例如：sg-33ocnj9n，可通過DescribeSecurityGroups獲取。每次請求的實例的上限爲100。
        :type SecurityGroupIds: list of str
        """
        self.NetworkInterfaceIds = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.NetworkInterfaceIds = params.get("NetworkInterfaceIds")
        self.SecurityGroupIds = params.get("SecurityGroupIds")


class DisassociateNetworkInterfaceSecurityGroupsResponse(AbstractModel):
    """DisassociateNetworkInterfaceSecurityGroups返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DownloadCustomerGatewayConfigurationRequest(AbstractModel):
    """DownloadCustomerGatewayConfiguration請求參數結構體

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN閘道實例ID。
        :type VpnGatewayId: str
        :param VpnConnectionId: VPN通道實例ID。形如：vpnx-f49l6u0z。
        :type VpnConnectionId: str
        :param CustomerGatewayVendor: 對端閘道廠商訊息對象，可通過DescribeCustomerGatewayVendors獲取。
        :type CustomerGatewayVendor: :class:`tencentcloud.vpc.v20170312.models.CustomerGatewayVendor`
        :param InterfaceName: 通道接入設備物理介面名稱。
        :type InterfaceName: str
        """
        self.VpnGatewayId = None
        self.VpnConnectionId = None
        self.CustomerGatewayVendor = None
        self.InterfaceName = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.VpnConnectionId = params.get("VpnConnectionId")
        if params.get("CustomerGatewayVendor") is not None:
            self.CustomerGatewayVendor = CustomerGatewayVendor()
            self.CustomerGatewayVendor._deserialize(params.get("CustomerGatewayVendor"))
        self.InterfaceName = params.get("InterfaceName")


class DownloadCustomerGatewayConfigurationResponse(AbstractModel):
    """DownloadCustomerGatewayConfiguration返回參數結構體

    """

    def __init__(self):
        """
        :param CustomerGatewayConfiguration: XML格式配置訊息。
        :type CustomerGatewayConfiguration: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CustomerGatewayConfiguration = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CustomerGatewayConfiguration = params.get("CustomerGatewayConfiguration")
        self.RequestId = params.get("RequestId")


class EnableCcnRoutesRequest(AbstractModel):
    """EnableCcnRoutes請求參數結構體

    """

    def __init__(self):
        """
        :param CcnId: CCN實例ID。形如：ccn-f49l6u0z。
        :type CcnId: str
        :param RouteIds: CCN路由策略唯一ID。形如：ccnr-f49l6u0z。
        :type RouteIds: list of str
        """
        self.CcnId = None
        self.RouteIds = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.RouteIds = params.get("RouteIds")


class EnableCcnRoutesResponse(AbstractModel):
    """EnableCcnRoutes返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableGatewayFlowMonitorRequest(AbstractModel):
    """EnableGatewayFlowMonitor請求參數結構體

    """

    def __init__(self):
        """
        :param GatewayId: 閘道實例ID，目前我們支援的閘道實例有，
專線閘道實例ID，形如，`dcg-ltjahce6`；
Nat閘道實例ID，形如，`nat-ltjahce6`；
VPN閘道實例ID，形如，`vpn-ltjahce6`。
        :type GatewayId: str
        """
        self.GatewayId = None


    def _deserialize(self, params):
        self.GatewayId = params.get("GatewayId")


class EnableGatewayFlowMonitorResponse(AbstractModel):
    """EnableGatewayFlowMonitor返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableRoutesRequest(AbstractModel):
    """EnableRoutes請求參數結構體

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表唯一ID。
        :type RouteTableId: str
        :param RouteIds: 路由策略唯一ID。
        :type RouteIds: list of int non-negative
        """
        self.RouteTableId = None
        self.RouteIds = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RouteIds = params.get("RouteIds")


class EnableRoutesResponse(AbstractModel):
    """EnableRoutes返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """過濾器

    """

    def __init__(self):
        """
        :param Name: 屬性名稱, 若存在多個Filter時，Filter間的關系爲邏輯與（AND）關系。
        :type Name: str
        :param Values: 屬性值, 若同一個Filter存在多個Values，同一Filter下Values間的關系爲邏輯或（OR）關系。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class FilterObject(AbstractModel):
    """過濾器鍵值對

    """

    def __init__(self):
        """
        :param Name: 屬性名稱, 若存在多個Filter時，Filter間的關系爲邏輯與（AND）關系。
        :type Name: str
        :param Values: 屬性值, 若同一個Filter存在多個Values，同一Filter下Values間的關系爲邏輯或（OR）關系。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class FlowLog(AbstractModel):
    """流日志

    """

    def __init__(self):
        """
        :param VpcId: 私用網絡ID或者統一ID，建議使用統一ID
        :type VpcId: str
        :param FlowLogId: 流日志唯一ID
        :type FlowLogId: str
        :param FlowLogName: 流日志實例名字
        :type FlowLogName: str
        :param ResourceType: 流日志所屬資源類型，VPC|SUBNET|NETWORKINTERFACE
        :type ResourceType: str
        :param ResourceId: 資源唯一ID
        :type ResourceId: str
        :param TrafficType: 流日志采集類型，ACCEPT|REJECT|ALL
        :type TrafficType: str
        :param CloudLogId: 流日志儲存ID
        :type CloudLogId: str
        :param CloudLogState: 流日志儲存ID狀态
        :type CloudLogState: str
        :param FlowLogDescription: 流日志描述訊息
        :type FlowLogDescription: str
        :param CreatedTime: 流日志創建時間
        :type CreatedTime: str
        """
        self.VpcId = None
        self.FlowLogId = None
        self.FlowLogName = None
        self.ResourceType = None
        self.ResourceId = None
        self.TrafficType = None
        self.CloudLogId = None
        self.CloudLogState = None
        self.FlowLogDescription = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.FlowLogId = params.get("FlowLogId")
        self.FlowLogName = params.get("FlowLogName")
        self.ResourceType = params.get("ResourceType")
        self.ResourceId = params.get("ResourceId")
        self.TrafficType = params.get("TrafficType")
        self.CloudLogId = params.get("CloudLogId")
        self.CloudLogState = params.get("CloudLogState")
        self.FlowLogDescription = params.get("FlowLogDescription")
        self.CreatedTime = params.get("CreatedTime")


class GatewayFlowMonitorDetail(AbstractModel):
    """閘道流量監控明細

    """

    def __init__(self):
        """
        :param PrivateIpAddress: 來源`IP`。
        :type PrivateIpAddress: str
        :param InPkg: 入包量。
        :type InPkg: int
        :param OutPkg: 出包量。
        :type OutPkg: int
        :param InTraffic: 入頻寬，單位：`Byte`。
        :type InTraffic: int
        :param OutTraffic: 出頻寬，單位：`Byte`。
        :type OutTraffic: int
        """
        self.PrivateIpAddress = None
        self.InPkg = None
        self.OutPkg = None
        self.InTraffic = None
        self.OutTraffic = None


    def _deserialize(self, params):
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        self.InPkg = params.get("InPkg")
        self.OutPkg = params.get("OutPkg")
        self.InTraffic = params.get("InTraffic")
        self.OutTraffic = params.get("OutTraffic")


class GatewayQos(AbstractModel):
    """閘道流控頻寬訊息

    """

    def __init__(self):
        """
        :param VpcId: VPC實例ID。
        :type VpcId: str
        :param IpAddress: 雲伺服器内網IP。
        :type IpAddress: str
        :param Bandwidth: 流控頻寬值。
        :type Bandwidth: int
        :param CreateTime: 創建時間。
        :type CreateTime: str
        """
        self.VpcId = None
        self.IpAddress = None
        self.Bandwidth = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.IpAddress = params.get("IpAddress")
        self.Bandwidth = params.get("Bandwidth")
        self.CreateTime = params.get("CreateTime")


class HaVip(AbstractModel):
    """描述 HAVIP 訊息

    """

    def __init__(self):
        """
        :param HaVipId: `HAVIP`的`ID`，是`HAVIP`的唯一标識。
        :type HaVipId: str
        :param HaVipName: `HAVIP`名稱。
        :type HaVipName: str
        :param Vip: 虛拟IP網址。
        :type Vip: str
        :param VpcId: `HAVIP`所在私有網絡`ID`。
        :type VpcId: str
        :param SubnetId: `HAVIP`所在子網`ID`。
        :type SubnetId: str
        :param NetworkInterfaceId: `HAVIP`關聯彈性網卡`ID`。
        :type NetworkInterfaceId: str
        :param InstanceId: 被綁定的實例`ID`。
        :type InstanceId: str
        :param AddressIp: 綁定`EIP`。
        :type AddressIp: str
        :param State: 狀态：
<li>`AVAILABLE`：運作中</li>
<li>`UNBIND`：未綁定</li>
        :type State: str
        :param CreatedTime: 創建時間。
        :type CreatedTime: str
        :param Business: 使用havip的業務标識。
        :type Business: str
        """
        self.HaVipId = None
        self.HaVipName = None
        self.Vip = None
        self.VpcId = None
        self.SubnetId = None
        self.NetworkInterfaceId = None
        self.InstanceId = None
        self.AddressIp = None
        self.State = None
        self.CreatedTime = None
        self.Business = None


    def _deserialize(self, params):
        self.HaVipId = params.get("HaVipId")
        self.HaVipName = params.get("HaVipName")
        self.Vip = params.get("Vip")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.InstanceId = params.get("InstanceId")
        self.AddressIp = params.get("AddressIp")
        self.State = params.get("State")
        self.CreatedTime = params.get("CreatedTime")
        self.Business = params.get("Business")


class HaVipAssociateAddressIpRequest(AbstractModel):
    """HaVipAssociateAddressIp請求參數結構體

    """

    def __init__(self):
        """
        :param HaVipId: `HAVIP`唯一`ID`，形如：`havip-9o233uri`。必須是沒有綁定`EIP`的`HAVIP`
        :type HaVipId: str
        :param AddressIp: 彈性公網`IP`。必須是沒有綁定`HAVIP`的`EIP`
        :type AddressIp: str
        """
        self.HaVipId = None
        self.AddressIp = None


    def _deserialize(self, params):
        self.HaVipId = params.get("HaVipId")
        self.AddressIp = params.get("AddressIp")


class HaVipAssociateAddressIpResponse(AbstractModel):
    """HaVipAssociateAddressIp返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class HaVipDisassociateAddressIpRequest(AbstractModel):
    """HaVipDisassociateAddressIp請求參數結構體

    """

    def __init__(self):
        """
        :param HaVipId: `HAVIP`唯一`ID`，形如：`havip-9o233uri`。必須是已綁定`EIP`的`HAVIP`。
        :type HaVipId: str
        """
        self.HaVipId = None


    def _deserialize(self, params):
        self.HaVipId = params.get("HaVipId")


class HaVipDisassociateAddressIpResponse(AbstractModel):
    """HaVipDisassociateAddressIp返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class IKEOptionsSpecification(AbstractModel):
    """IKE配置（Internet Key Exchange，因特網金鑰交換），IKE具有一套自我保護機制，用戶配置網絡安全協議

    """

    def __init__(self):
        """
        :param PropoEncryAlgorithm: 加密算法，可選值：'3DES-CBC', 'AES-CBC-128', 'AES-CBS-192', 'AES-CBC-256', 'DES-CBC'，預設爲3DES-CBC
        :type PropoEncryAlgorithm: str
        :param PropoAuthenAlgorithm: 認證算法：可選值：'MD5', 'SHA1'，預設爲MD5
        :type PropoAuthenAlgorithm: str
        :param ExchangeMode: 協商模式：可選值：'AGGRESSIVE', 'MAIN'，預設爲MAIN
        :type ExchangeMode: str
        :param LocalIdentity: 本端标識類型：可選值：'ADDRESS', 'FQDN'，預設爲ADDRESS
        :type LocalIdentity: str
        :param RemoteIdentity: 對端标識類型：可選值：'ADDRESS', 'FQDN'，預設爲ADDRESS
        :type RemoteIdentity: str
        :param LocalAddress: 本端标識，當LocalIdentity選爲ADDRESS時，LocalAddress必填。localAddress預設爲vpn閘道公網IP
        :type LocalAddress: str
        :param RemoteAddress: 對端标識，當RemoteIdentity選爲ADDRESS時，RemoteAddress必填
        :type RemoteAddress: str
        :param LocalFqdnName: 本端标識，當LocalIdentity選爲FQDN時，LocalFqdnName必填
        :type LocalFqdnName: str
        :param RemoteFqdnName: 對端标識，當remoteIdentity選爲FQDN時，RemoteFqdnName必填
        :type RemoteFqdnName: str
        :param DhGroupName: DH group，指定IKE交換金鑰時使用的DH組，可選值：'GROUP1', 'GROUP2', 'GROUP5', 'GROUP14', 'GROUP24'，
        :type DhGroupName: str
        :param IKESaLifetimeSeconds: IKE SA Lifetime，單位：秒，設置IKE SA的生存週期，取值範圍：60-604800
        :type IKESaLifetimeSeconds: int
        :param IKEVersion: IKE版本
        :type IKEVersion: str
        """
        self.PropoEncryAlgorithm = None
        self.PropoAuthenAlgorithm = None
        self.ExchangeMode = None
        self.LocalIdentity = None
        self.RemoteIdentity = None
        self.LocalAddress = None
        self.RemoteAddress = None
        self.LocalFqdnName = None
        self.RemoteFqdnName = None
        self.DhGroupName = None
        self.IKESaLifetimeSeconds = None
        self.IKEVersion = None


    def _deserialize(self, params):
        self.PropoEncryAlgorithm = params.get("PropoEncryAlgorithm")
        self.PropoAuthenAlgorithm = params.get("PropoAuthenAlgorithm")
        self.ExchangeMode = params.get("ExchangeMode")
        self.LocalIdentity = params.get("LocalIdentity")
        self.RemoteIdentity = params.get("RemoteIdentity")
        self.LocalAddress = params.get("LocalAddress")
        self.RemoteAddress = params.get("RemoteAddress")
        self.LocalFqdnName = params.get("LocalFqdnName")
        self.RemoteFqdnName = params.get("RemoteFqdnName")
        self.DhGroupName = params.get("DhGroupName")
        self.IKESaLifetimeSeconds = params.get("IKESaLifetimeSeconds")
        self.IKEVersion = params.get("IKEVersion")


class IPSECOptionsSpecification(AbstractModel):
    """IPSec配置，Top Cloud 提供IPSec安全會話設置

    """

    def __init__(self):
        """
        :param EncryptAlgorithm: 加密算法，可選值：'3DES-CBC', 'AES-CBC-128', 'AES-CBC-192', 'AES-CBC-256', 'DES-CBC', 'NULL'， 預設爲AES-CBC-128
        :type EncryptAlgorithm: str
        :param IntegrityAlgorith: 認證算法：可選值：'MD5', 'SHA1'，預設爲
        :type IntegrityAlgorith: str
        :param IPSECSaLifetimeSeconds: IPsec SA lifetime(s)：單位秒，取值範圍：180-604800
        :type IPSECSaLifetimeSeconds: int
        :param PfsDhGroup: PFS：可選值：'NULL', 'DH-GROUP1', 'DH-GROUP2', 'DH-GROUP5', 'DH-GROUP14', 'DH-GROUP24'，預設爲NULL
        :type PfsDhGroup: str
        :param IPSECSaLifetimeTraffic: IPsec SA lifetime(KB)：單位KB，取值範圍：2560-604800
        :type IPSECSaLifetimeTraffic: int
        """
        self.EncryptAlgorithm = None
        self.IntegrityAlgorith = None
        self.IPSECSaLifetimeSeconds = None
        self.PfsDhGroup = None
        self.IPSECSaLifetimeTraffic = None


    def _deserialize(self, params):
        self.EncryptAlgorithm = params.get("EncryptAlgorithm")
        self.IntegrityAlgorith = params.get("IntegrityAlgorith")
        self.IPSECSaLifetimeSeconds = params.get("IPSECSaLifetimeSeconds")
        self.PfsDhGroup = params.get("PfsDhGroup")
        self.IPSECSaLifetimeTraffic = params.get("IPSECSaLifetimeTraffic")


class InquiryPriceCreateVpnGatewayRequest(AbstractModel):
    """InquiryPriceCreateVpnGateway請求參數結構體

    """

    def __init__(self):
        """
        :param InternetMaxBandwidthOut: 公網頻寬設置。可選頻寬規格：5, 10, 20, 50, 100；單位：Mbps。
        :type InternetMaxBandwidthOut: int
        :param InstanceChargeType: VPN閘道計費模式，PREPAID：表示預付費，即包年包月，POSTPAID_BY_HOUR：表示後付費，即按量計費。預設：POSTPAID_BY_HOUR，如果指定預付費模式，參數InstanceChargePrepaid必填。
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: 預付費模式，即包年包月相關參數設置。通過該參數可以指定包年包月實例的購買時長、是否設置自動續約等屬性。若指定實例的付費模式爲預付費則該參數必傳。
        :type InstanceChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.InstanceChargePrepaid`
        """
        self.InternetMaxBandwidthOut = None
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))


class InquiryPriceCreateVpnGatewayResponse(AbstractModel):
    """InquiryPriceCreateVpnGateway返回參數結構體

    """

    def __init__(self):
        """
        :param Price: 商品價格。
        :type Price: :class:`tencentcloud.vpc.v20170312.models.Price`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceRenewVpnGatewayRequest(AbstractModel):
    """InquiryPriceRenewVpnGateway請求參數結構體

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN閘道實例ID。
        :type VpnGatewayId: str
        :param InstanceChargePrepaid: 預付費模式，即包年包月相關參數設置。通過該參數可以指定包年包月實例的購買時長、是否設置自動續約等屬性。若指定實例的付費模式爲預付費則該參數必傳。
        :type InstanceChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.InstanceChargePrepaid`
        """
        self.VpnGatewayId = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))


class InquiryPriceRenewVpnGatewayResponse(AbstractModel):
    """InquiryPriceRenewVpnGateway返回參數結構體

    """

    def __init__(self):
        """
        :param Price: 商品價格。
        :type Price: :class:`tencentcloud.vpc.v20170312.models.Price`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceResetVpnGatewayInternetMaxBandwidthRequest(AbstractModel):
    """InquiryPriceResetVpnGatewayInternetMaxBandwidth請求參數結構體

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN閘道實例ID。
        :type VpnGatewayId: str
        :param InternetMaxBandwidthOut: 公網頻寬設置。可選頻寬規格：5, 10, 20, 50, 100；單位：Mbps。
        :type InternetMaxBandwidthOut: int
        """
        self.VpnGatewayId = None
        self.InternetMaxBandwidthOut = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")


class InquiryPriceResetVpnGatewayInternetMaxBandwidthResponse(AbstractModel):
    """InquiryPriceResetVpnGatewayInternetMaxBandwidth返回參數結構體

    """

    def __init__(self):
        """
        :param Price: 商品價格。
        :type Price: :class:`tencentcloud.vpc.v20170312.models.Price`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InstanceChargePrepaid(AbstractModel):
    """預付費（包年包月）計費對象。

    """

    def __init__(self):
        """
        :param Period: 購買實例的時長，單位：月。取值範圍：1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36。
        :type Period: int
        :param RenewFlag: 自動續約标識。取值範圍： NOTIFY_AND_AUTO_RENEW：通知過期且自動續約， NOTIFY_AND_MANUAL_RENEW：通知過期不自動續約。預設：NOTIFY_AND_MANUAL_RENEW
        :type RenewFlag: str
        """
        self.Period = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RenewFlag = params.get("RenewFlag")


class InstanceStatistic(AbstractModel):
    """用于描述實例的統計訊息

    """

    def __init__(self):
        """
        :param InstanceType: 實例的類型
        :type InstanceType: str
        :param InstanceCount: 實例的個數
        :type InstanceCount: int
        """
        self.InstanceType = None
        self.InstanceCount = None


    def _deserialize(self, params):
        self.InstanceType = params.get("InstanceType")
        self.InstanceCount = params.get("InstanceCount")


class Ip6Rule(AbstractModel):
    """IPV6轉換規則

    """

    def __init__(self):
        """
        :param Ip6RuleId: IPV6轉換規則唯一ID，形如rule6-xxxxxxxx
        :type Ip6RuleId: str
        :param Ip6RuleName: IPV6轉換規則名稱
        :type Ip6RuleName: str
        :param Vip6: IPV6網址
        :type Vip6: str
        :param Vport6: IPV6端口号
        :type Vport6: int
        :param Protocol: 協議類型，支援TCP/UDP
        :type Protocol: str
        :param Vip: IPV4網址
        :type Vip: str
        :param Vport: IPV4端口号
        :type Vport: int
        :param RuleStatus: 轉換規則狀态，限于CREATING,RUNNING,DELETING,MODIFYING
        :type RuleStatus: str
        :param CreatedTime: 轉換規則創建時間
        :type CreatedTime: str
        """
        self.Ip6RuleId = None
        self.Ip6RuleName = None
        self.Vip6 = None
        self.Vport6 = None
        self.Protocol = None
        self.Vip = None
        self.Vport = None
        self.RuleStatus = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.Ip6RuleId = params.get("Ip6RuleId")
        self.Ip6RuleName = params.get("Ip6RuleName")
        self.Vip6 = params.get("Vip6")
        self.Vport6 = params.get("Vport6")
        self.Protocol = params.get("Protocol")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.RuleStatus = params.get("RuleStatus")
        self.CreatedTime = params.get("CreatedTime")


class Ip6RuleInfo(AbstractModel):
    """IPV6轉換規則

    """

    def __init__(self):
        """
        :param Vport6: IPV6端口号，可在0~65535範圍取值
        :type Vport6: int
        :param Protocol: 協議類型，支援TCP/UDP
        :type Protocol: str
        :param Vip: IPV4網址
        :type Vip: str
        :param Vport: IPV4端口号，可在0~65535範圍取值
        :type Vport: int
        """
        self.Vport6 = None
        self.Protocol = None
        self.Vip = None
        self.Vport = None


    def _deserialize(self, params):
        self.Vport6 = params.get("Vport6")
        self.Protocol = params.get("Protocol")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")


class Ip6Translator(AbstractModel):
    """IPV6轉換實例訊息

    """

    def __init__(self):
        """
        :param Ip6TranslatorId: IPV6轉換實例唯一ID，形如ip6-xxxxxxxx
        :type Ip6TranslatorId: str
        :param Ip6TranslatorName: IPV6轉換實例名稱
        :type Ip6TranslatorName: str
        :param Vip6: IPV6網址
        :type Vip6: str
        :param IspName: IPV6轉換網址所屬運營商
        :type IspName: str
        :param TranslatorStatus: 轉換實例狀态，限于CREATING,RUNNING,DELETING,MODIFYING
        :type TranslatorStatus: str
        :param CreatedTime: IPV6轉換實例創建時間
        :type CreatedTime: str
        :param Ip6RuleCount: 綁定的IPV6轉換規則數量
        :type Ip6RuleCount: int
        :param IP6RuleSet: IPV6轉換規則訊息
        :type IP6RuleSet: list of Ip6Rule
        """
        self.Ip6TranslatorId = None
        self.Ip6TranslatorName = None
        self.Vip6 = None
        self.IspName = None
        self.TranslatorStatus = None
        self.CreatedTime = None
        self.Ip6RuleCount = None
        self.IP6RuleSet = None


    def _deserialize(self, params):
        self.Ip6TranslatorId = params.get("Ip6TranslatorId")
        self.Ip6TranslatorName = params.get("Ip6TranslatorName")
        self.Vip6 = params.get("Vip6")
        self.IspName = params.get("IspName")
        self.TranslatorStatus = params.get("TranslatorStatus")
        self.CreatedTime = params.get("CreatedTime")
        self.Ip6RuleCount = params.get("Ip6RuleCount")
        if params.get("IP6RuleSet") is not None:
            self.IP6RuleSet = []
            for item in params.get("IP6RuleSet"):
                obj = Ip6Rule()
                obj._deserialize(item)
                self.IP6RuleSet.append(obj)


class Ipv6Address(AbstractModel):
    """`IPv6`網址訊息。

    """

    def __init__(self):
        """
        :param Address: `IPv6`網址，形如：`3402:4e00:20:100:0:8cd9:2a67:71f3`
        :type Address: str
        :param Primary: 是否是主`IP`。
        :type Primary: bool
        :param AddressId: `EIP`實例`ID`，形如：`eip-hxlqja90`。
        :type AddressId: str
        :param Description: 描述訊息。
        :type Description: str
        :param IsWanIpBlocked: 公網IP是否被封堵。
        :type IsWanIpBlocked: bool
        :param State: `IPv6`網址狀态：
<li>`PENDING`：生産中</li>
<li>`MIGRATING`：遷移中</li>
<li>`DELETING`：删除中</li>
<li>`AVAILABLE`：可用的</li>
        :type State: str
        """
        self.Address = None
        self.Primary = None
        self.AddressId = None
        self.Description = None
        self.IsWanIpBlocked = None
        self.State = None


    def _deserialize(self, params):
        self.Address = params.get("Address")
        self.Primary = params.get("Primary")
        self.AddressId = params.get("AddressId")
        self.Description = params.get("Description")
        self.IsWanIpBlocked = params.get("IsWanIpBlocked")
        self.State = params.get("State")


class Ipv6SubnetCidrBlock(AbstractModel):
    """IPv6子網段對象。

    """

    def __init__(self):
        """
        :param SubnetId: 子網實例`ID`。形如：`subnet-pxir56ns`。
        :type SubnetId: str
        :param Ipv6CidrBlock: `IPv6`子網段。形如：`3402:4e00:20:1001::/64`
        :type Ipv6CidrBlock: str
        """
        self.SubnetId = None
        self.Ipv6CidrBlock = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")


class ItemPrice(AbstractModel):
    """單項計費價格訊息

    """

    def __init__(self):
        """
        :param UnitPrice: 按量計費後付費單價，單位：元。
        :type UnitPrice: float
        :param ChargeUnit: 按量計費後付費計價單元，可取值範圍： HOUR：表示計價單元是按每小時來計算。當前涉及該計價單元的場景有：實例按小時後付費（POSTPAID_BY_HOUR）、頻寬按小時後付費（BANDWIDTH_POSTPAID_BY_HOUR）： GB：表示計價單元是按每GB來計算。當前涉及該計價單元的場景有：流量按小時後付費（TRAFFIC_POSTPAID_BY_HOUR）。
        :type ChargeUnit: str
        :param OriginalPrice: 預付費商品的原價，單位：元。
        :type OriginalPrice: float
        :param DiscountPrice: 預付費商品的折扣價，單位：元。
        :type DiscountPrice: float
        """
        self.UnitPrice = None
        self.ChargeUnit = None
        self.OriginalPrice = None
        self.DiscountPrice = None


    def _deserialize(self, params):
        self.UnitPrice = params.get("UnitPrice")
        self.ChargeUnit = params.get("ChargeUnit")
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")


class MigrateNetworkInterfaceRequest(AbstractModel):
    """MigrateNetworkInterface請求參數結構體

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 彈性網卡實例ID，例如：eni-m6dyj72l。
        :type NetworkInterfaceId: str
        :param SourceInstanceId: 彈性網卡當前綁定的CVM實例ID。形如：ins-r8hr2upy。
        :type SourceInstanceId: str
        :param DestinationInstanceId: 待遷移的目的CVM實例ID。
        :type DestinationInstanceId: str
        """
        self.NetworkInterfaceId = None
        self.SourceInstanceId = None
        self.DestinationInstanceId = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.SourceInstanceId = params.get("SourceInstanceId")
        self.DestinationInstanceId = params.get("DestinationInstanceId")


class MigrateNetworkInterfaceResponse(AbstractModel):
    """MigrateNetworkInterface返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MigratePrivateIpAddressRequest(AbstractModel):
    """MigratePrivateIpAddress請求參數結構體

    """

    def __init__(self):
        """
        :param SourceNetworkInterfaceId: 當内網IP綁定的彈性網卡實例ID，例如：eni-m6dyj72l。
        :type SourceNetworkInterfaceId: str
        :param DestinationNetworkInterfaceId: 待遷移的目的彈性網卡實例ID。
        :type DestinationNetworkInterfaceId: str
        :param PrivateIpAddress: 遷移的内網IP網址，例如：10.0.0.6。
        :type PrivateIpAddress: str
        """
        self.SourceNetworkInterfaceId = None
        self.DestinationNetworkInterfaceId = None
        self.PrivateIpAddress = None


    def _deserialize(self, params):
        self.SourceNetworkInterfaceId = params.get("SourceNetworkInterfaceId")
        self.DestinationNetworkInterfaceId = params.get("DestinationNetworkInterfaceId")
        self.PrivateIpAddress = params.get("PrivateIpAddress")


class MigratePrivateIpAddressResponse(AbstractModel):
    """MigratePrivateIpAddress返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAddressAttributeRequest(AbstractModel):
    """ModifyAddressAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param AddressId: 标識 EIP 的唯一 ID。EIP 唯一 ID 形如：`eip-11112222`。
        :type AddressId: str
        :param AddressName: 修改後的 EIP 名稱。長度上限爲20個字元。
        :type AddressName: str
        :param EipDirectConnection: 設定EIP是否直通，"TRUE"表示直通，"FALSE"表示非直通。注意該參數僅對EIP直通功能可見的用戶可以設定。
        :type EipDirectConnection: str
        """
        self.AddressId = None
        self.AddressName = None
        self.EipDirectConnection = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.AddressName = params.get("AddressName")
        self.EipDirectConnection = params.get("EipDirectConnection")


class ModifyAddressAttributeResponse(AbstractModel):
    """ModifyAddressAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAddressInternetChargeTypeRequest(AbstractModel):
    """ModifyAddressInternetChargeType請求參數結構體

    """

    def __init__(self):
        """
        :param AddressId: 彈性公網IP的唯一ID，形如eip-xxx
        :type AddressId: str
        :param InternetChargeType: 彈性公網IP調整目标計費模式，只支援"BANDWIDTH_PREPAID_BY_MONTH"和"TRAFFIC_POSTPAID_BY_HOUR"
        :type InternetChargeType: str
        :param InternetMaxBandwidthOut: 彈性公網IP調整目标頻寬值
        :type InternetMaxBandwidthOut: int
        :param AddressChargePrepaid: 包月頻寬網絡計費模式參數。彈性公網IP的調整目标計費模式是"BANDWIDTH_PREPAID_BY_MONTH"時，必傳該參數。
        :type AddressChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.AddressChargePrepaid`
        """
        self.AddressId = None
        self.InternetChargeType = None
        self.InternetMaxBandwidthOut = None
        self.AddressChargePrepaid = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.InternetChargeType = params.get("InternetChargeType")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        if params.get("AddressChargePrepaid") is not None:
            self.AddressChargePrepaid = AddressChargePrepaid()
            self.AddressChargePrepaid._deserialize(params.get("AddressChargePrepaid"))


class ModifyAddressInternetChargeTypeResponse(AbstractModel):
    """ModifyAddressInternetChargeType返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAddressTemplateAttributeRequest(AbstractModel):
    """ModifyAddressTemplateAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param AddressTemplateId: IP網址範本實例ID，例如：ipm-mdunqeb6。
        :type AddressTemplateId: str
        :param AddressTemplateName: IP網址範本名稱。
        :type AddressTemplateName: str
        :param Addresses: 網址訊息，支援 IP、CIDR、IP 範圍。
        :type Addresses: list of str
        """
        self.AddressTemplateId = None
        self.AddressTemplateName = None
        self.Addresses = None


    def _deserialize(self, params):
        self.AddressTemplateId = params.get("AddressTemplateId")
        self.AddressTemplateName = params.get("AddressTemplateName")
        self.Addresses = params.get("Addresses")


class ModifyAddressTemplateAttributeResponse(AbstractModel):
    """ModifyAddressTemplateAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAddressTemplateGroupAttributeRequest(AbstractModel):
    """ModifyAddressTemplateGroupAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param AddressTemplateGroupId: IP網址範本集合實例ID，例如：ipmg-2uw6ujo6。
        :type AddressTemplateGroupId: str
        :param AddressTemplateGroupName: IP網址範本集合名稱。
        :type AddressTemplateGroupName: str
        :param AddressTemplateIds: IP網址範本實例ID， 例如：ipm-mdunqeb6。
        :type AddressTemplateIds: list of str
        """
        self.AddressTemplateGroupId = None
        self.AddressTemplateGroupName = None
        self.AddressTemplateIds = None


    def _deserialize(self, params):
        self.AddressTemplateGroupId = params.get("AddressTemplateGroupId")
        self.AddressTemplateGroupName = params.get("AddressTemplateGroupName")
        self.AddressTemplateIds = params.get("AddressTemplateIds")


class ModifyAddressTemplateGroupAttributeResponse(AbstractModel):
    """ModifyAddressTemplateGroupAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAddressesBandwidthRequest(AbstractModel):
    """ModifyAddressesBandwidth請求參數結構體

    """

    def __init__(self):
        """
        :param AddressIds: EIP唯一标識ID，形如'eip-xxxx'
        :type AddressIds: list of str
        :param InternetMaxBandwidthOut: 調整頻寬目标值
        :type InternetMaxBandwidthOut: int
        :param StartTime: 包月頻寬起始時間
        :type StartTime: str
        :param EndTime: 包月頻寬結束時間
        :type EndTime: str
        """
        self.AddressIds = None
        self.InternetMaxBandwidthOut = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.AddressIds = params.get("AddressIds")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class ModifyAddressesBandwidthResponse(AbstractModel):
    """ModifyAddressesBandwidth返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步任務TaskId。可以使用[DescribeTaskResult](https://cloud.tencent.com/document/api/215/36271)介面查詢任務狀态。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyAssistantCidrRequest(AbstractModel):
    """ModifyAssistantCidr請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: `VPC`實例`ID`。形如：`vpc-6v2ht8q5`
        :type VpcId: str
        :param NewCidrBlocks: 待添加的負載CIDR。CIDR數組，格式如["10.0.0.0/16", "172.16.0.0/16"]
        :type NewCidrBlocks: list of str
        :param OldCidrBlocks: 待删除的負載CIDR。CIDR數組，格式如["10.0.0.0/16", "172.16.0.0/16"]
        :type OldCidrBlocks: list of str
        """
        self.VpcId = None
        self.NewCidrBlocks = None
        self.OldCidrBlocks = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NewCidrBlocks = params.get("NewCidrBlocks")
        self.OldCidrBlocks = params.get("OldCidrBlocks")


class ModifyAssistantCidrResponse(AbstractModel):
    """ModifyAssistantCidr返回參數結構體

    """

    def __init__(self):
        """
        :param AssistantCidrSet: 輔助CIDR數組。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AssistantCidrSet: list of AssistantCidr
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AssistantCidrSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AssistantCidrSet") is not None:
            self.AssistantCidrSet = []
            for item in params.get("AssistantCidrSet"):
                obj = AssistantCidr()
                obj._deserialize(item)
                self.AssistantCidrSet.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyBandwidthPackageAttributeRequest(AbstractModel):
    """ModifyBandwidthPackageAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param BandwidthPackageId: 頻寬包唯一标識ID
        :type BandwidthPackageId: str
        :param BandwidthPackageName: 頻寬包名稱
        :type BandwidthPackageName: str
        :param ChargeType: 頻寬包計費模式
        :type ChargeType: str
        """
        self.BandwidthPackageId = None
        self.BandwidthPackageName = None
        self.ChargeType = None


    def _deserialize(self, params):
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        self.BandwidthPackageName = params.get("BandwidthPackageName")
        self.ChargeType = params.get("ChargeType")


class ModifyBandwidthPackageAttributeResponse(AbstractModel):
    """ModifyBandwidthPackageAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCcnAttributeRequest(AbstractModel):
    """ModifyCcnAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param CcnId: CCN實例ID。形如：ccn-f49l6u0z。
        :type CcnId: str
        :param CcnName: CCN名稱，最大長度不能超過60個位元。
        :type CcnName: str
        :param CcnDescription: CCN描述訊息，最大長度不能超過100個位元。
        :type CcnDescription: str
        """
        self.CcnId = None
        self.CcnName = None
        self.CcnDescription = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.CcnName = params.get("CcnName")
        self.CcnDescription = params.get("CcnDescription")


class ModifyCcnAttributeResponse(AbstractModel):
    """ModifyCcnAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCcnRegionBandwidthLimitsTypeRequest(AbstractModel):
    """ModifyCcnRegionBandwidthLimitsType請求參數結構體

    """

    def __init__(self):
        """
        :param CcnId: 雲聯網實例ID。
        :type CcnId: str
        :param BandwidthLimitType: 雲聯網限速類型，INTER_REGION_LIMIT：地域間限速，OUTER_REGION_LIMIT：地域出口限速。
        :type BandwidthLimitType: str
        """
        self.CcnId = None
        self.BandwidthLimitType = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.BandwidthLimitType = params.get("BandwidthLimitType")


class ModifyCcnRegionBandwidthLimitsTypeResponse(AbstractModel):
    """ModifyCcnRegionBandwidthLimitsType返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCustomerGatewayAttributeRequest(AbstractModel):
    """ModifyCustomerGatewayAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param CustomerGatewayId: 對端閘道ID，例如：cgw-2wqq41m9，可通過DescribeCustomerGateways介面查詢對端閘道。
        :type CustomerGatewayId: str
        :param CustomerGatewayName: 對端閘道名稱，可任意命名，但不得超過60個字元。
        :type CustomerGatewayName: str
        """
        self.CustomerGatewayId = None
        self.CustomerGatewayName = None


    def _deserialize(self, params):
        self.CustomerGatewayId = params.get("CustomerGatewayId")
        self.CustomerGatewayName = params.get("CustomerGatewayName")


class ModifyCustomerGatewayAttributeResponse(AbstractModel):
    """ModifyCustomerGatewayAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDirectConnectGatewayAttributeRequest(AbstractModel):
    """ModifyDirectConnectGatewayAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: 專線閘道唯一`ID`，形如：`dcg-9o233uri`。
        :type DirectConnectGatewayId: str
        :param DirectConnectGatewayName: 專線閘道名稱，可任意命名，但不得超過60個字元。
        :type DirectConnectGatewayName: str
        :param CcnRouteType: 雲聯網路由學習類型，可選值：`BGP`（自動學習）、`STATIC`（靜态，即用戶配置）。只有雲聯網類型專線閘道且開啓了BGP功能才支援修改`CcnRouteType`。
        :type CcnRouteType: str
        """
        self.DirectConnectGatewayId = None
        self.DirectConnectGatewayName = None
        self.CcnRouteType = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.DirectConnectGatewayName = params.get("DirectConnectGatewayName")
        self.CcnRouteType = params.get("CcnRouteType")


class ModifyDirectConnectGatewayAttributeResponse(AbstractModel):
    """ModifyDirectConnectGatewayAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyFlowLogAttributeRequest(AbstractModel):
    """ModifyFlowLogAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: 私用網絡ID或者統一ID，建議使用統一ID
        :type VpcId: str
        :param FlowLogId: 流日志唯一ID
        :type FlowLogId: str
        :param FlowLogName: 流日志實例名字
        :type FlowLogName: str
        :param FlowLogDescription: 流日志實例描述
        :type FlowLogDescription: str
        """
        self.VpcId = None
        self.FlowLogId = None
        self.FlowLogName = None
        self.FlowLogDescription = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.FlowLogId = params.get("FlowLogId")
        self.FlowLogName = params.get("FlowLogName")
        self.FlowLogDescription = params.get("FlowLogDescription")


class ModifyFlowLogAttributeResponse(AbstractModel):
    """ModifyFlowLogAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyGatewayFlowQosRequest(AbstractModel):
    """ModifyGatewayFlowQos請求參數結構體

    """

    def __init__(self):
        """
        :param GatewayId: 閘道實例ID，目前我們支援的閘道實例類型有，
專線閘道實例ID，形如，`dcg-ltjahce6`；
Nat閘道實例ID，形如，`nat-ltjahce6`；
VPN閘道實例ID，形如，`vpn-ltjahce6`。
        :type GatewayId: str
        :param Bandwidth: 流控頻寬值。
        :type Bandwidth: int
        :param IpAddresses: 限流的雲伺服器内網IP。
        :type IpAddresses: list of str
        """
        self.GatewayId = None
        self.Bandwidth = None
        self.IpAddresses = None


    def _deserialize(self, params):
        self.GatewayId = params.get("GatewayId")
        self.Bandwidth = params.get("Bandwidth")
        self.IpAddresses = params.get("IpAddresses")


class ModifyGatewayFlowQosResponse(AbstractModel):
    """ModifyGatewayFlowQos返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyHaVipAttributeRequest(AbstractModel):
    """ModifyHaVipAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param HaVipId: `HAVIP`唯一`ID`，形如：`havip-9o233uri`。
        :type HaVipId: str
        :param HaVipName: `HAVIP`名稱，可任意命名，但不得超過60個字元。
        :type HaVipName: str
        """
        self.HaVipId = None
        self.HaVipName = None


    def _deserialize(self, params):
        self.HaVipId = params.get("HaVipId")
        self.HaVipName = params.get("HaVipName")


class ModifyHaVipAttributeResponse(AbstractModel):
    """ModifyHaVipAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyIp6AddressesBandwidthRequest(AbstractModel):
    """ModifyIp6AddressesBandwidth請求參數結構體

    """

    def __init__(self):
        """
        :param InternetMaxBandwidthOut: 修改的目标頻寬，單位Mbps
        :type InternetMaxBandwidthOut: int
        :param Ip6Addresses: IPV6網址。Ip6Addresses和Ip6AddressId必須且只能傳一個
        :type Ip6Addresses: list of str
        :param Ip6AddressIds: IPV6網址對應的唯一ID，形如eip-xxxxxxxx。Ip6Addresses和Ip6AddressId必須且只能傳一個
        :type Ip6AddressIds: list of str
        """
        self.InternetMaxBandwidthOut = None
        self.Ip6Addresses = None
        self.Ip6AddressIds = None


    def _deserialize(self, params):
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.Ip6Addresses = params.get("Ip6Addresses")
        self.Ip6AddressIds = params.get("Ip6AddressIds")


class ModifyIp6AddressesBandwidthResponse(AbstractModel):
    """ModifyIp6AddressesBandwidth返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyIp6RuleRequest(AbstractModel):
    """ModifyIp6Rule請求參數結構體

    """

    def __init__(self):
        """
        :param Ip6TranslatorId: IPV6轉換實例唯一ID，形如ip6-xxxxxxxx
        :type Ip6TranslatorId: str
        :param Ip6RuleId: IPV6轉換規則唯一ID，形如rule6-xxxxxxxx
        :type Ip6RuleId: str
        :param Ip6RuleName: IPV6轉換規則修改後的名稱
        :type Ip6RuleName: str
        :param Vip: IPV6轉換規則修改後的IPV4網址
        :type Vip: str
        :param Vport: IPV6轉換規則修改後的IPV4端口号
        :type Vport: int
        """
        self.Ip6TranslatorId = None
        self.Ip6RuleId = None
        self.Ip6RuleName = None
        self.Vip = None
        self.Vport = None


    def _deserialize(self, params):
        self.Ip6TranslatorId = params.get("Ip6TranslatorId")
        self.Ip6RuleId = params.get("Ip6RuleId")
        self.Ip6RuleName = params.get("Ip6RuleName")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")


class ModifyIp6RuleResponse(AbstractModel):
    """ModifyIp6Rule返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyIp6TranslatorRequest(AbstractModel):
    """ModifyIp6Translator請求參數結構體

    """

    def __init__(self):
        """
        :param Ip6TranslatorId: IPV6轉換實例唯一ID，形如ip6-xxxxxxxxx
        :type Ip6TranslatorId: str
        :param Ip6TranslatorName: IPV6轉換實例修改名稱
        :type Ip6TranslatorName: str
        """
        self.Ip6TranslatorId = None
        self.Ip6TranslatorName = None


    def _deserialize(self, params):
        self.Ip6TranslatorId = params.get("Ip6TranslatorId")
        self.Ip6TranslatorName = params.get("Ip6TranslatorName")


class ModifyIp6TranslatorResponse(AbstractModel):
    """ModifyIp6Translator返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyIpv6AddressesAttributeRequest(AbstractModel):
    """ModifyIpv6AddressesAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 彈性網卡實例`ID`，形如：`eni-m6dyj72l`。
        :type NetworkInterfaceId: str
        :param Ipv6Addresses: 指定的内網IPv6`網址訊息。
        :type Ipv6Addresses: list of Ipv6Address
        """
        self.NetworkInterfaceId = None
        self.Ipv6Addresses = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("Ipv6Addresses") is not None:
            self.Ipv6Addresses = []
            for item in params.get("Ipv6Addresses"):
                obj = Ipv6Address()
                obj._deserialize(item)
                self.Ipv6Addresses.append(obj)


class ModifyIpv6AddressesAttributeResponse(AbstractModel):
    """ModifyIpv6AddressesAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNatGatewayAttributeRequest(AbstractModel):
    """ModifyNatGatewayAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param NatGatewayId: NAT閘道的ID，形如：`nat-df45454`。
        :type NatGatewayId: str
        :param NatGatewayName: NAT閘道的名稱，形如：`test_nat`。
        :type NatGatewayName: str
        :param InternetMaxBandwidthOut: NAT閘道最大外網出頻寬(單位:Mbps)。
        :type InternetMaxBandwidthOut: int
        """
        self.NatGatewayId = None
        self.NatGatewayName = None
        self.InternetMaxBandwidthOut = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        self.NatGatewayName = params.get("NatGatewayName")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")


class ModifyNatGatewayAttributeResponse(AbstractModel):
    """ModifyNatGatewayAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNatGatewayDestinationIpPortTranslationNatRuleRequest(AbstractModel):
    """ModifyNatGatewayDestinationIpPortTranslationNatRule請求參數結構體

    """

    def __init__(self):
        """
        :param NatGatewayId: NAT閘道的ID，形如：`nat-df45454`。
        :type NatGatewayId: str
        :param SourceNatRule: 源NAT閘道的端口轉換規則。
        :type SourceNatRule: :class:`tencentcloud.vpc.v20170312.models.DestinationIpPortTranslationNatRule`
        :param DestinationNatRule: 目的NAT閘道的端口轉換規則。
        :type DestinationNatRule: :class:`tencentcloud.vpc.v20170312.models.DestinationIpPortTranslationNatRule`
        """
        self.NatGatewayId = None
        self.SourceNatRule = None
        self.DestinationNatRule = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        if params.get("SourceNatRule") is not None:
            self.SourceNatRule = DestinationIpPortTranslationNatRule()
            self.SourceNatRule._deserialize(params.get("SourceNatRule"))
        if params.get("DestinationNatRule") is not None:
            self.DestinationNatRule = DestinationIpPortTranslationNatRule()
            self.DestinationNatRule._deserialize(params.get("DestinationNatRule"))


class ModifyNatGatewayDestinationIpPortTranslationNatRuleResponse(AbstractModel):
    """ModifyNatGatewayDestinationIpPortTranslationNatRule返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNetDetectRequest(AbstractModel):
    """ModifyNetDetect請求參數結構體

    """

    def __init__(self):
        """
        :param NetDetectId: 網絡探測實例`ID`。形如：`netd-12345678`
        :type NetDetectId: str
        :param NetDetectName: 網絡探測名稱，最大長度不能超過60個位元。
        :type NetDetectName: str
        :param DetectDestinationIp: 探測目的IPv4網址數組，最多兩個。
        :type DetectDestinationIp: list of str
        :param NextHopType: 下一跳類型，目前我們支援的類型有：
VPN：VPN閘道；
DIRECTCONNECT：專線閘道；
PEERCONNECTION：對等連接；
NAT：NAT閘道；
NORMAL_CVM：普通雲伺服器；
        :type NextHopType: str
        :param NextHopDestination: 下一跳目的閘道，取值與“下一跳類型”相關：
下一跳類型爲VPN，取值VPN閘道ID，形如：vpngw-12345678；
下一跳類型爲DIRECTCONNECT，取值專線閘道ID，形如：dcg-12345678；
下一跳類型爲PEERCONNECTION，取值對等連接ID，形如：pcx-12345678；
下一跳類型爲NAT，取值Nat閘道，形如：nat-12345678；
下一跳類型爲NORMAL_CVM，取值雲伺服器IPv4網址，形如：10.0.0.12；
        :type NextHopDestination: str
        :param NetDetectDescription: 網絡探測描述。
        :type NetDetectDescription: str
        """
        self.NetDetectId = None
        self.NetDetectName = None
        self.DetectDestinationIp = None
        self.NextHopType = None
        self.NextHopDestination = None
        self.NetDetectDescription = None


    def _deserialize(self, params):
        self.NetDetectId = params.get("NetDetectId")
        self.NetDetectName = params.get("NetDetectName")
        self.DetectDestinationIp = params.get("DetectDestinationIp")
        self.NextHopType = params.get("NextHopType")
        self.NextHopDestination = params.get("NextHopDestination")
        self.NetDetectDescription = params.get("NetDetectDescription")


class ModifyNetDetectResponse(AbstractModel):
    """ModifyNetDetect返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNetworkAclAttributeRequest(AbstractModel):
    """ModifyNetworkAclAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param NetworkAclId: 網絡ACL實例ID。例如：acl-12345678。
        :type NetworkAclId: str
        :param NetworkAclName: 網絡ACL名稱，最大長度不能超過60個位元。
        :type NetworkAclName: str
        """
        self.NetworkAclId = None
        self.NetworkAclName = None


    def _deserialize(self, params):
        self.NetworkAclId = params.get("NetworkAclId")
        self.NetworkAclName = params.get("NetworkAclName")


class ModifyNetworkAclAttributeResponse(AbstractModel):
    """ModifyNetworkAclAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNetworkAclEntriesRequest(AbstractModel):
    """ModifyNetworkAclEntries請求參數結構體

    """

    def __init__(self):
        """
        :param NetworkAclId: 網絡ACL實例ID。例如：acl-12345678。
        :type NetworkAclId: str
        :param NetworkAclEntrySet: 網絡ACL規則集。
        :type NetworkAclEntrySet: :class:`tencentcloud.vpc.v20170312.models.NetworkAclEntrySet`
        """
        self.NetworkAclId = None
        self.NetworkAclEntrySet = None


    def _deserialize(self, params):
        self.NetworkAclId = params.get("NetworkAclId")
        if params.get("NetworkAclEntrySet") is not None:
            self.NetworkAclEntrySet = NetworkAclEntrySet()
            self.NetworkAclEntrySet._deserialize(params.get("NetworkAclEntrySet"))


class ModifyNetworkAclEntriesResponse(AbstractModel):
    """ModifyNetworkAclEntries返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNetworkInterfaceAttributeRequest(AbstractModel):
    """ModifyNetworkInterfaceAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 彈性網卡實例ID，例如：eni-pxir56ns。
        :type NetworkInterfaceId: str
        :param NetworkInterfaceName: 彈性網卡名稱，最大長度不能超過60個位元。
        :type NetworkInterfaceName: str
        :param NetworkInterfaceDescription: 彈性網卡描述，可任意命名，但不得超過60個字元。
        :type NetworkInterfaceDescription: str
        :param SecurityGroupIds: 指定綁定的安全組，例如:['sg-1dd51d']。
        :type SecurityGroupIds: list of str
        """
        self.NetworkInterfaceId = None
        self.NetworkInterfaceName = None
        self.NetworkInterfaceDescription = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.NetworkInterfaceName = params.get("NetworkInterfaceName")
        self.NetworkInterfaceDescription = params.get("NetworkInterfaceDescription")
        self.SecurityGroupIds = params.get("SecurityGroupIds")


class ModifyNetworkInterfaceAttributeResponse(AbstractModel):
    """ModifyNetworkInterfaceAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPrivateIpAddressesAttributeRequest(AbstractModel):
    """ModifyPrivateIpAddressesAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 彈性網卡實例ID，例如：eni-m6dyj72l。
        :type NetworkInterfaceId: str
        :param PrivateIpAddresses: 指定的内網IP訊息。
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        """
        self.NetworkInterfaceId = None
        self.PrivateIpAddresses = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("PrivateIpAddresses") is not None:
            self.PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self.PrivateIpAddresses.append(obj)


class ModifyPrivateIpAddressesAttributeResponse(AbstractModel):
    """ModifyPrivateIpAddressesAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRouteTableAttributeRequest(AbstractModel):
    """ModifyRouteTableAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表實例ID，例如：rtb-azd4dt1c。
        :type RouteTableId: str
        :param RouteTableName: 路由表名稱。
        :type RouteTableName: str
        """
        self.RouteTableId = None
        self.RouteTableName = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RouteTableName = params.get("RouteTableName")


class ModifyRouteTableAttributeResponse(AbstractModel):
    """ModifyRouteTableAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySecurityGroupAttributeRequest(AbstractModel):
    """ModifySecurityGroupAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全組實例ID，例如sg-33ocnj9n，可通過DescribeSecurityGroups獲取。
        :type SecurityGroupId: str
        :param GroupName: 安全組名稱，可任意命名，但不得超過60個字元。
        :type GroupName: str
        :param GroupDescription: 安全組備注，最多100個字元。
        :type GroupDescription: str
        """
        self.SecurityGroupId = None
        self.GroupName = None
        self.GroupDescription = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.GroupName = params.get("GroupName")
        self.GroupDescription = params.get("GroupDescription")


class ModifySecurityGroupAttributeResponse(AbstractModel):
    """ModifySecurityGroupAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySecurityGroupPoliciesRequest(AbstractModel):
    """ModifySecurityGroupPolicies請求參數結構體

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全組實例ID，例如sg-33ocnj9n，可通過DescribeSecurityGroups獲取。
        :type SecurityGroupId: str
        :param SecurityGroupPolicySet: 安全組規則集合。 SecurityGroupPolicySet對象必須同時指定新的出（Egress）入（Ingress）站規則。 SecurityGroupPolicy對象不支援自定義索引（PolicyIndex）。
        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`
        :param SortPolicys: 排序安全組标識。值爲True時，支援安全組排序；SortPolicys不存在或SortPolicys爲False時，爲修改安全組規則。
        :type SortPolicys: bool
        """
        self.SecurityGroupId = None
        self.SecurityGroupPolicySet = None
        self.SortPolicys = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = SecurityGroupPolicySet()
            self.SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))
        self.SortPolicys = params.get("SortPolicys")


class ModifySecurityGroupPoliciesResponse(AbstractModel):
    """ModifySecurityGroupPolicies返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyServiceTemplateAttributeRequest(AbstractModel):
    """ModifyServiceTemplateAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param ServiceTemplateId: 協議端口範本實例ID，例如：ppm-529nwwj8。
        :type ServiceTemplateId: str
        :param ServiceTemplateName: 協議端口範本名稱。
        :type ServiceTemplateName: str
        :param Services: 支援單個端口、多個端口、連續端口及所有端口，協議支援：TCP、UDP、ICMP、GRE 協議。
        :type Services: list of str
        """
        self.ServiceTemplateId = None
        self.ServiceTemplateName = None
        self.Services = None


    def _deserialize(self, params):
        self.ServiceTemplateId = params.get("ServiceTemplateId")
        self.ServiceTemplateName = params.get("ServiceTemplateName")
        self.Services = params.get("Services")


class ModifyServiceTemplateAttributeResponse(AbstractModel):
    """ModifyServiceTemplateAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyServiceTemplateGroupAttributeRequest(AbstractModel):
    """ModifyServiceTemplateGroupAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param ServiceTemplateGroupId: 協議端口範本集合實例ID，例如：ppmg-ei8hfd9a。
        :type ServiceTemplateGroupId: str
        :param ServiceTemplateGroupName: 協議端口範本集合名稱。
        :type ServiceTemplateGroupName: str
        :param ServiceTemplateIds: 協議端口範本實例ID，例如：ppm-4dw6agho。
        :type ServiceTemplateIds: list of str
        """
        self.ServiceTemplateGroupId = None
        self.ServiceTemplateGroupName = None
        self.ServiceTemplateIds = None


    def _deserialize(self, params):
        self.ServiceTemplateGroupId = params.get("ServiceTemplateGroupId")
        self.ServiceTemplateGroupName = params.get("ServiceTemplateGroupName")
        self.ServiceTemplateIds = params.get("ServiceTemplateIds")


class ModifyServiceTemplateGroupAttributeResponse(AbstractModel):
    """ModifyServiceTemplateGroupAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubnetAttributeRequest(AbstractModel):
    """ModifySubnetAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param SubnetId: 子網實例ID。形如：subnet-pxir56ns。
        :type SubnetId: str
        :param SubnetName: 子網名稱，最大長度不能超過60個位元。
        :type SubnetName: str
        :param EnableBroadcast: 子網是否開啓廣播。
        :type EnableBroadcast: str
        """
        self.SubnetId = None
        self.SubnetName = None
        self.EnableBroadcast = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.EnableBroadcast = params.get("EnableBroadcast")


class ModifySubnetAttributeResponse(AbstractModel):
    """ModifySubnetAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVpcAttributeRequest(AbstractModel):
    """ModifyVpcAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: VPC實例ID。形如：vpc-f49l6u0z。每次請求的實例的上限爲100。參數不支援同時指定VpcIds和Filters。
        :type VpcId: str
        :param VpcName: 私有網絡名稱，可任意命名，但不得超過60個字元。
        :type VpcName: str
        :param EnableMulticast: 是否開啓組播。true: 開啓, false: 關閉。
        :type EnableMulticast: str
        :param DnsServers: DNS網址，最多支援4個，第1個預設爲主，其餘爲備
        :type DnsServers: list of str
        :param DomainName: 域名
        :type DomainName: str
        """
        self.VpcId = None
        self.VpcName = None
        self.EnableMulticast = None
        self.DnsServers = None
        self.DomainName = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.EnableMulticast = params.get("EnableMulticast")
        self.DnsServers = params.get("DnsServers")
        self.DomainName = params.get("DomainName")


class ModifyVpcAttributeResponse(AbstractModel):
    """ModifyVpcAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVpnConnectionAttributeRequest(AbstractModel):
    """ModifyVpnConnectionAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param VpnConnectionId: VPN通道實例ID。形如：vpnx-f49l6u0z。
        :type VpnConnectionId: str
        :param VpnConnectionName: VPN通道名稱，可任意命名，但不得超過60個字元。
        :type VpnConnectionName: str
        :param PreShareKey: 預共享金鑰。
        :type PreShareKey: str
        :param SecurityPolicyDatabases: SPD策略組，例如：{"10.0.0.5/24":["172.123.10.5/16"]}，10.0.0.5/24是vpc内網段172.123.10.5/16是IDC網段。用戶指定VPC内哪些網段可以和您IDC中哪些網段通信。
        :type SecurityPolicyDatabases: list of SecurityPolicyDatabase
        :param IKEOptionsSpecification: IKE配置（Internet Key Exchange，因特網金鑰交換），IKE具有一套自我保護機制，用戶配置網絡安全協議。
        :type IKEOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IKEOptionsSpecification`
        :param IPSECOptionsSpecification: IPSec配置，Top Cloud 提供IPSec安全會話設置。
        :type IPSECOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IPSECOptionsSpecification`
        """
        self.VpnConnectionId = None
        self.VpnConnectionName = None
        self.PreShareKey = None
        self.SecurityPolicyDatabases = None
        self.IKEOptionsSpecification = None
        self.IPSECOptionsSpecification = None


    def _deserialize(self, params):
        self.VpnConnectionId = params.get("VpnConnectionId")
        self.VpnConnectionName = params.get("VpnConnectionName")
        self.PreShareKey = params.get("PreShareKey")
        if params.get("SecurityPolicyDatabases") is not None:
            self.SecurityPolicyDatabases = []
            for item in params.get("SecurityPolicyDatabases"):
                obj = SecurityPolicyDatabase()
                obj._deserialize(item)
                self.SecurityPolicyDatabases.append(obj)
        if params.get("IKEOptionsSpecification") is not None:
            self.IKEOptionsSpecification = IKEOptionsSpecification()
            self.IKEOptionsSpecification._deserialize(params.get("IKEOptionsSpecification"))
        if params.get("IPSECOptionsSpecification") is not None:
            self.IPSECOptionsSpecification = IPSECOptionsSpecification()
            self.IPSECOptionsSpecification._deserialize(params.get("IPSECOptionsSpecification"))


class ModifyVpnConnectionAttributeResponse(AbstractModel):
    """ModifyVpnConnectionAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVpnGatewayAttributeRequest(AbstractModel):
    """ModifyVpnGatewayAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN閘道實例ID。
        :type VpnGatewayId: str
        :param VpnGatewayName: VPN閘道名稱，最大長度不能超過60個位元。
        :type VpnGatewayName: str
        :param InstanceChargeType: VPN閘道計費模式，目前只支援預付費（即包年包月）到後付費（即按量計費）的轉換。即參數只支援：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        """
        self.VpnGatewayId = None
        self.VpnGatewayName = None
        self.InstanceChargeType = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.VpnGatewayName = params.get("VpnGatewayName")
        self.InstanceChargeType = params.get("InstanceChargeType")


class ModifyVpnGatewayAttributeResponse(AbstractModel):
    """ModifyVpnGatewayAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVpnGatewayCcnRoutesRequest(AbstractModel):
    """ModifyVpnGatewayCcnRoutes請求參數結構體

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN閘道實例ID
        :type VpnGatewayId: str
        :param Routes: 雲聯網路由（IDC網段）清單
        :type Routes: list of VpngwCcnRoutes
        """
        self.VpnGatewayId = None
        self.Routes = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = VpngwCcnRoutes()
                obj._deserialize(item)
                self.Routes.append(obj)


class ModifyVpnGatewayCcnRoutesResponse(AbstractModel):
    """ModifyVpnGatewayCcnRoutes返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NatGateway(AbstractModel):
    """NAT閘道對象。

    """

    def __init__(self):
        """
        :param NatGatewayId: NAT閘道的ID。
        :type NatGatewayId: str
        :param NatGatewayName: NAT閘道的名稱。
        :type NatGatewayName: str
        :param CreatedTime: NAT閘道創建的時間。
        :type CreatedTime: str
        :param State: NAT閘道的狀态。
 'PENDING'：生産中，'DELETING'：删除中，'AVAILABLE'：運作中，'UPDATING'：升級中，
‘FAILED’：失敗。
        :type State: str
        :param InternetMaxBandwidthOut: 閘道最大外網出頻寬(單位:Mbps)。
        :type InternetMaxBandwidthOut: int
        :param MaxConcurrentConnection: 閘道并發連接上限。
        :type MaxConcurrentConnection: int
        :param PublicIpAddressSet: 綁定NAT閘道的公網IP對象數組。
        :type PublicIpAddressSet: list of NatGatewayAddress
        :param NetworkState: NAT閘道網絡狀态。“AVAILABLE”:運作中, “UNAVAILABLE”:不可用, “INSUFFICIENT”:欠費停服。
        :type NetworkState: str
        :param DestinationIpPortTranslationNatRuleSet: NAT閘道的端口轉發規則。
        :type DestinationIpPortTranslationNatRuleSet: list of DestinationIpPortTranslationNatRule
        :param VpcId: VPC實例ID。
        :type VpcId: str
        :param Zone: NAT閘道所在的可用區。
        :type Zone: str
        """
        self.NatGatewayId = None
        self.NatGatewayName = None
        self.CreatedTime = None
        self.State = None
        self.InternetMaxBandwidthOut = None
        self.MaxConcurrentConnection = None
        self.PublicIpAddressSet = None
        self.NetworkState = None
        self.DestinationIpPortTranslationNatRuleSet = None
        self.VpcId = None
        self.Zone = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        self.NatGatewayName = params.get("NatGatewayName")
        self.CreatedTime = params.get("CreatedTime")
        self.State = params.get("State")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.MaxConcurrentConnection = params.get("MaxConcurrentConnection")
        if params.get("PublicIpAddressSet") is not None:
            self.PublicIpAddressSet = []
            for item in params.get("PublicIpAddressSet"):
                obj = NatGatewayAddress()
                obj._deserialize(item)
                self.PublicIpAddressSet.append(obj)
        self.NetworkState = params.get("NetworkState")
        if params.get("DestinationIpPortTranslationNatRuleSet") is not None:
            self.DestinationIpPortTranslationNatRuleSet = []
            for item in params.get("DestinationIpPortTranslationNatRuleSet"):
                obj = DestinationIpPortTranslationNatRule()
                obj._deserialize(item)
                self.DestinationIpPortTranslationNatRuleSet.append(obj)
        self.VpcId = params.get("VpcId")
        self.Zone = params.get("Zone")


class NatGatewayAddress(AbstractModel):
    """NAT閘道綁定的彈性IP

    """

    def __init__(self):
        """
        :param AddressId: 彈性公網IP（EIP）的唯一 ID，形如：`eip-11112222`。
        :type AddressId: str
        :param PublicIpAddress: 外網IP網址，形如：`123.121.34.33`。
        :type PublicIpAddress: str
        :param IsBlocked: 資源封堵狀态。true表示彈性ip處于封堵狀态，false表示彈性ip處于未封堵狀态。
        :type IsBlocked: bool
        """
        self.AddressId = None
        self.PublicIpAddress = None
        self.IsBlocked = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.PublicIpAddress = params.get("PublicIpAddress")
        self.IsBlocked = params.get("IsBlocked")


class NatGatewayDestinationIpPortTranslationNatRule(AbstractModel):
    """NAT閘道的端口轉發規則

    """

    def __init__(self):
        """
        :param IpProtocol: 網絡協議，可選值：`TCP`、`UDP`。
        :type IpProtocol: str
        :param PublicIpAddress: 彈性IP。
        :type PublicIpAddress: str
        :param PublicPort: 公網端口。
        :type PublicPort: int
        :param PrivateIpAddress: 内網網址。
        :type PrivateIpAddress: str
        :param PrivatePort: 内網端口。
        :type PrivatePort: int
        :param Description: NAT閘道轉發規則描述。
        :type Description: str
        :param NatGatewayId: NAT閘道的ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type NatGatewayId: str
        :param VpcId: 私有網絡VPC的ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param CreatedTime: NAT閘道轉發規則創建時間。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        """
        self.IpProtocol = None
        self.PublicIpAddress = None
        self.PublicPort = None
        self.PrivateIpAddress = None
        self.PrivatePort = None
        self.Description = None
        self.NatGatewayId = None
        self.VpcId = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.IpProtocol = params.get("IpProtocol")
        self.PublicIpAddress = params.get("PublicIpAddress")
        self.PublicPort = params.get("PublicPort")
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        self.PrivatePort = params.get("PrivatePort")
        self.Description = params.get("Description")
        self.NatGatewayId = params.get("NatGatewayId")
        self.VpcId = params.get("VpcId")
        self.CreatedTime = params.get("CreatedTime")


class NetDetect(AbstractModel):
    """網絡探測對象。

    """

    def __init__(self):
        """
        :param VpcId: `VPC`實例`ID`。形如：`vpc-12345678`
        :type VpcId: str
        :param VpcName: `VPC`實例名稱。
        :type VpcName: str
        :param SubnetId: 子網實例ID。形如：subnet-12345678。
        :type SubnetId: str
        :param SubnetName: 子網實例名稱。
        :type SubnetName: str
        :param NetDetectId: 網絡探測實例ID。形如：netd-12345678。
        :type NetDetectId: str
        :param NetDetectName: 網絡探測名稱，最大長度不能超過60個位元。
        :type NetDetectName: str
        :param DetectDestinationIp: 探測目的IPv4網址數組，最多兩個。
        :type DetectDestinationIp: list of str
        :param DetectSourceIp: 系統自動分配的探測源IPv4數組。長度爲2。
        :type DetectSourceIp: list of str
        :param NextHopType: 下一跳類型，目前我們支援的類型有：
VPN：VPN閘道；
DIRECTCONNECT：專線閘道；
PEERCONNECTION：對等連接；
NAT：NAT閘道；
NORMAL_CVM：普通雲伺服器；
        :type NextHopType: str
        :param NextHopDestination: 下一跳目的閘道，取值與“下一跳類型”相關：
下一跳類型爲VPN，取值VPN閘道ID，形如：vpngw-12345678；
下一跳類型爲DIRECTCONNECT，取值專線閘道ID，形如：dcg-12345678；
下一跳類型爲PEERCONNECTION，取值對等連接ID，形如：pcx-12345678；
下一跳類型爲NAT，取值Nat閘道，形如：nat-12345678；
下一跳類型爲NORMAL_CVM，取值雲伺服器IPv4網址，形如：10.0.0.12；
        :type NextHopDestination: str
        :param NextHopName: 下一跳閘道名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type NextHopName: str
        :param NetDetectDescription: 網絡探測描述。
注意：此欄位可能返回 null，表示取不到有效值。
        :type NetDetectDescription: str
        :param CreateTime: 創建時間。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self.VpcId = None
        self.VpcName = None
        self.SubnetId = None
        self.SubnetName = None
        self.NetDetectId = None
        self.NetDetectName = None
        self.DetectDestinationIp = None
        self.DetectSourceIp = None
        self.NextHopType = None
        self.NextHopDestination = None
        self.NextHopName = None
        self.NetDetectDescription = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.NetDetectId = params.get("NetDetectId")
        self.NetDetectName = params.get("NetDetectName")
        self.DetectDestinationIp = params.get("DetectDestinationIp")
        self.DetectSourceIp = params.get("DetectSourceIp")
        self.NextHopType = params.get("NextHopType")
        self.NextHopDestination = params.get("NextHopDestination")
        self.NextHopName = params.get("NextHopName")
        self.NetDetectDescription = params.get("NetDetectDescription")
        self.CreateTime = params.get("CreateTime")


class NetDetectIpState(AbstractModel):
    """網絡探測目的IP的驗證結果。

    """

    def __init__(self):
        """
        :param DetectDestinationIp: 探測目的IPv4網址。
        :type DetectDestinationIp: str
        :param State: 探測結果。
0：成功；
-1：查詢不到路由丢包；
-2：外出ACL丢包；
-3：IN ACL丢包；
-4：其他錯誤；
        :type State: int
        :param Delay: 延遲，單位毫秒
        :type Delay: int
        :param PacketLossRate: 丢包率
        :type PacketLossRate: int
        """
        self.DetectDestinationIp = None
        self.State = None
        self.Delay = None
        self.PacketLossRate = None


    def _deserialize(self, params):
        self.DetectDestinationIp = params.get("DetectDestinationIp")
        self.State = params.get("State")
        self.Delay = params.get("Delay")
        self.PacketLossRate = params.get("PacketLossRate")


class NetDetectState(AbstractModel):
    """網絡探測驗證結果。

    """

    def __init__(self):
        """
        :param NetDetectId: 網絡探測實例ID。形如：netd-12345678。
        :type NetDetectId: str
        :param NetDetectIpStateSet: 網絡探測目的IP驗證結果對象數組。
        :type NetDetectIpStateSet: list of NetDetectIpState
        """
        self.NetDetectId = None
        self.NetDetectIpStateSet = None


    def _deserialize(self, params):
        self.NetDetectId = params.get("NetDetectId")
        if params.get("NetDetectIpStateSet") is not None:
            self.NetDetectIpStateSet = []
            for item in params.get("NetDetectIpStateSet"):
                obj = NetDetectIpState()
                obj._deserialize(item)
                self.NetDetectIpStateSet.append(obj)


class NetworkAcl(AbstractModel):
    """網絡ACL

    """

    def __init__(self):
        """
        :param VpcId: `VPC`實例`ID`。
        :type VpcId: str
        :param NetworkAclId: 網絡ACL實例`ID`。
        :type NetworkAclId: str
        :param NetworkAclName: 網絡ACL名稱，最大長度爲60。
        :type NetworkAclName: str
        :param CreatedTime: 創建時間。
        :type CreatedTime: str
        :param SubnetSet: 網絡ACL關聯的子網數組。
        :type SubnetSet: list of Subnet
        :param IngressEntries: 網絡ACl入站規則。
        :type IngressEntries: list of NetworkAclEntry
        :param EgressEntries: 網絡ACL出站規則。
        :type EgressEntries: list of NetworkAclEntry
        """
        self.VpcId = None
        self.NetworkAclId = None
        self.NetworkAclName = None
        self.CreatedTime = None
        self.SubnetSet = None
        self.IngressEntries = None
        self.EgressEntries = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NetworkAclId = params.get("NetworkAclId")
        self.NetworkAclName = params.get("NetworkAclName")
        self.CreatedTime = params.get("CreatedTime")
        if params.get("SubnetSet") is not None:
            self.SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = Subnet()
                obj._deserialize(item)
                self.SubnetSet.append(obj)
        if params.get("IngressEntries") is not None:
            self.IngressEntries = []
            for item in params.get("IngressEntries"):
                obj = NetworkAclEntry()
                obj._deserialize(item)
                self.IngressEntries.append(obj)
        if params.get("EgressEntries") is not None:
            self.EgressEntries = []
            for item in params.get("EgressEntries"):
                obj = NetworkAclEntry()
                obj._deserialize(item)
                self.EgressEntries.append(obj)


class NetworkAclEntry(AbstractModel):
    """網絡ACL規則。

    """

    def __init__(self):
        """
        :param ModifyTime: 修改時間。
        :type ModifyTime: str
        :param Protocol: 協議, 取值: TCP,UDP, ICMP, ALL。
        :type Protocol: str
        :param Port: 端口(all, 單個port,  range)。當Protocol爲ALL或ICMP時，不能指定Port。
        :type Port: str
        :param CidrBlock: 網段或IP(互斥)。
        :type CidrBlock: str
        :param Ipv6CidrBlock: 網段或IPv6(互斥)。
        :type Ipv6CidrBlock: str
        :param Action: ACCEPT 或 DROP。
        :type Action: str
        :param Description: 規則描述，最大長度100。
        :type Description: str
        """
        self.ModifyTime = None
        self.Protocol = None
        self.Port = None
        self.CidrBlock = None
        self.Ipv6CidrBlock = None
        self.Action = None
        self.Description = None


    def _deserialize(self, params):
        self.ModifyTime = params.get("ModifyTime")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        self.CidrBlock = params.get("CidrBlock")
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        self.Action = params.get("Action")
        self.Description = params.get("Description")


class NetworkAclEntrySet(AbstractModel):
    """網絡ACL規則集合

    """

    def __init__(self):
        """
        :param Ingress: 入站規則。
        :type Ingress: list of NetworkAclEntry
        :param Egress: 出站規則。
        :type Egress: list of NetworkAclEntry
        """
        self.Ingress = None
        self.Egress = None


    def _deserialize(self, params):
        if params.get("Ingress") is not None:
            self.Ingress = []
            for item in params.get("Ingress"):
                obj = NetworkAclEntry()
                obj._deserialize(item)
                self.Ingress.append(obj)
        if params.get("Egress") is not None:
            self.Egress = []
            for item in params.get("Egress"):
                obj = NetworkAclEntry()
                obj._deserialize(item)
                self.Egress.append(obj)


class NetworkInterface(AbstractModel):
    """彈性網卡

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 彈性網卡實例ID，例如：eni-f1xjkw1b。
        :type NetworkInterfaceId: str
        :param NetworkInterfaceName: 彈性網卡名稱。
        :type NetworkInterfaceName: str
        :param NetworkInterfaceDescription: 彈性網卡描述。
        :type NetworkInterfaceDescription: str
        :param SubnetId: 子網實例ID。
        :type SubnetId: str
        :param VpcId: VPC實例ID。
        :type VpcId: str
        :param GroupSet: 綁定的安全組。
        :type GroupSet: list of str
        :param Primary: 是否是主網卡。
        :type Primary: bool
        :param MacAddress: MAC網址。
        :type MacAddress: str
        :param State: 彈性網卡狀态：
<li>`PENDING`：創建中</li>
<li>`AVAILABLE`：可用的</li>
<li>`ATTACHING`：綁定中</li>
<li>`DETACHING`：解綁中</li>
<li>`DELETING`：删除中</li>
        :type State: str
        :param PrivateIpAddressSet: 内網IP訊息。
        :type PrivateIpAddressSet: list of PrivateIpAddressSpecification
        :param Attachment: 綁定的雲伺服器對象。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Attachment: :class:`tencentcloud.vpc.v20170312.models.NetworkInterfaceAttachment`
        :param Zone: 可用區。
        :type Zone: str
        :param CreatedTime: 創建時間。
        :type CreatedTime: str
        :param Ipv6AddressSet: `IPv6`網址清單。
        :type Ipv6AddressSet: list of Ipv6Address
        :param TagSet: 标簽鍵值對。
        :type TagSet: list of Tag
        :param EniType: 網卡類型。0 - 彈性網卡；1 - evm彈性網卡。
        :type EniType: int
        """
        self.NetworkInterfaceId = None
        self.NetworkInterfaceName = None
        self.NetworkInterfaceDescription = None
        self.SubnetId = None
        self.VpcId = None
        self.GroupSet = None
        self.Primary = None
        self.MacAddress = None
        self.State = None
        self.PrivateIpAddressSet = None
        self.Attachment = None
        self.Zone = None
        self.CreatedTime = None
        self.Ipv6AddressSet = None
        self.TagSet = None
        self.EniType = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.NetworkInterfaceName = params.get("NetworkInterfaceName")
        self.NetworkInterfaceDescription = params.get("NetworkInterfaceDescription")
        self.SubnetId = params.get("SubnetId")
        self.VpcId = params.get("VpcId")
        self.GroupSet = params.get("GroupSet")
        self.Primary = params.get("Primary")
        self.MacAddress = params.get("MacAddress")
        self.State = params.get("State")
        if params.get("PrivateIpAddressSet") is not None:
            self.PrivateIpAddressSet = []
            for item in params.get("PrivateIpAddressSet"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self.PrivateIpAddressSet.append(obj)
        if params.get("Attachment") is not None:
            self.Attachment = NetworkInterfaceAttachment()
            self.Attachment._deserialize(params.get("Attachment"))
        self.Zone = params.get("Zone")
        self.CreatedTime = params.get("CreatedTime")
        if params.get("Ipv6AddressSet") is not None:
            self.Ipv6AddressSet = []
            for item in params.get("Ipv6AddressSet"):
                obj = Ipv6Address()
                obj._deserialize(item)
                self.Ipv6AddressSet.append(obj)
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.EniType = params.get("EniType")


class NetworkInterfaceAttachment(AbstractModel):
    """彈性網卡綁定關系

    """

    def __init__(self):
        """
        :param InstanceId: 雲主機實例ID。
        :type InstanceId: str
        :param DeviceIndex: 網卡在雲主機實例内的序号。
        :type DeviceIndex: int
        :param InstanceAccountId: 雲主機所有者帳戶訊息。
        :type InstanceAccountId: str
        :param AttachTime: 綁定時間。
        :type AttachTime: str
        """
        self.InstanceId = None
        self.DeviceIndex = None
        self.InstanceAccountId = None
        self.AttachTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DeviceIndex = params.get("DeviceIndex")
        self.InstanceAccountId = params.get("InstanceAccountId")
        self.AttachTime = params.get("AttachTime")


class Price(AbstractModel):
    """價格

    """

    def __init__(self):
        """
        :param InstancePrice: 實例價格。
        :type InstancePrice: :class:`tencentcloud.vpc.v20170312.models.ItemPrice`
        :param BandwidthPrice: 網絡價格。
        :type BandwidthPrice: :class:`tencentcloud.vpc.v20170312.models.ItemPrice`
        """
        self.InstancePrice = None
        self.BandwidthPrice = None


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self.InstancePrice = ItemPrice()
            self.InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("BandwidthPrice") is not None:
            self.BandwidthPrice = ItemPrice()
            self.BandwidthPrice._deserialize(params.get("BandwidthPrice"))


class PrivateIpAddressSpecification(AbstractModel):
    """内網IP訊息

    """

    def __init__(self):
        """
        :param PrivateIpAddress: 内網IP網址。
        :type PrivateIpAddress: str
        :param Primary: 是否是主IP。
        :type Primary: bool
        :param PublicIpAddress: 公網IP網址。
        :type PublicIpAddress: str
        :param AddressId: EIP實例ID，例如：eip-11112222。
        :type AddressId: str
        :param Description: 内網IP描述訊息。
        :type Description: str
        :param IsWanIpBlocked: 公網IP是否被封堵。
        :type IsWanIpBlocked: bool
        :param State: IP狀态：
PENDING：生産中
MIGRATING：遷移中
DELETING：删除中
AVAILABLE：可用的
        :type State: str
        """
        self.PrivateIpAddress = None
        self.Primary = None
        self.PublicIpAddress = None
        self.AddressId = None
        self.Description = None
        self.IsWanIpBlocked = None
        self.State = None


    def _deserialize(self, params):
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        self.Primary = params.get("Primary")
        self.PublicIpAddress = params.get("PublicIpAddress")
        self.AddressId = params.get("AddressId")
        self.Description = params.get("Description")
        self.IsWanIpBlocked = params.get("IsWanIpBlocked")
        self.State = params.get("State")


class Quota(AbstractModel):
    """描述配額訊息

    """

    def __init__(self):
        """
        :param QuotaId: 配額名稱，取值範圍：<br><li>`TOTAL_EIP_QUOTA`：用戶當前地域下EIP的配額數；<br><li>`DAILY_EIP_APPLY`：用戶當前地域下今日申購次數；<br><li>`DAILY_PUBLIC_IP_ASSIGN`：用戶當前地域下，重新分配公網 IP次數。
        :type QuotaId: str
        :param QuotaCurrent: 當前數量
        :type QuotaCurrent: int
        :param QuotaLimit: 配額數量
        :type QuotaLimit: int
        """
        self.QuotaId = None
        self.QuotaCurrent = None
        self.QuotaLimit = None


    def _deserialize(self, params):
        self.QuotaId = params.get("QuotaId")
        self.QuotaCurrent = params.get("QuotaCurrent")
        self.QuotaLimit = params.get("QuotaLimit")


class ReferredSecurityGroup(AbstractModel):
    """安全組被引用訊息

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全組實例ID。
        :type SecurityGroupId: str
        :param ReferredSecurityGroupIds: 引用安全組實例ID（SecurityGroupId）的所有安全組實例ID。
        :type ReferredSecurityGroupIds: list of str
        """
        self.SecurityGroupId = None
        self.ReferredSecurityGroupIds = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.ReferredSecurityGroupIds = params.get("ReferredSecurityGroupIds")


class RejectAttachCcnInstancesRequest(AbstractModel):
    """RejectAttachCcnInstances請求參數結構體

    """

    def __init__(self):
        """
        :param CcnId: CCN實例ID。形如：ccn-f49l6u0z。
        :type CcnId: str
        :param Instances: 拒絕關聯實例清單。
        :type Instances: list of CcnInstance
        """
        self.CcnId = None
        self.Instances = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = CcnInstance()
                obj._deserialize(item)
                self.Instances.append(obj)


class RejectAttachCcnInstancesResponse(AbstractModel):
    """RejectAttachCcnInstances返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReleaseAddressesRequest(AbstractModel):
    """ReleaseAddresses請求參數結構體

    """

    def __init__(self):
        """
        :param AddressIds: 标識 EIP 的唯一 ID 清單。EIP 唯一 ID 形如：`eip-11112222`。
        :type AddressIds: list of str
        """
        self.AddressIds = None


    def _deserialize(self, params):
        self.AddressIds = params.get("AddressIds")


class ReleaseAddressesResponse(AbstractModel):
    """ReleaseAddresses返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步任務TaskId。可以使用[DescribeTaskResult](https://cloud.tencent.com/document/api/215/36271)介面查詢任務狀态。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ReleaseIp6AddressesBandwidthRequest(AbstractModel):
    """ReleaseIp6AddressesBandwidth請求參數結構體

    """

    def __init__(self):
        """
        :param Ip6Addresses: IPV6網址。Ip6Addresses和Ip6AddressIds必須且只能傳一個
        :type Ip6Addresses: list of str
        :param Ip6AddressIds: IPV6網址對應的唯一ID，形如eip-xxxxxxxx。Ip6Addresses和Ip6AddressIds必須且只能傳一個。
        :type Ip6AddressIds: list of str
        """
        self.Ip6Addresses = None
        self.Ip6AddressIds = None


    def _deserialize(self, params):
        self.Ip6Addresses = params.get("Ip6Addresses")
        self.Ip6AddressIds = params.get("Ip6AddressIds")


class ReleaseIp6AddressesBandwidthResponse(AbstractModel):
    """ReleaseIp6AddressesBandwidth返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步任務TaskId。可以使用[DescribeTaskResult](https://cloud.tencent.com/document/api/215/36271)介面查詢任務狀态。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class RemoveBandwidthPackageResourcesRequest(AbstractModel):
    """RemoveBandwidthPackageResources請求參數結構體

    """

    def __init__(self):
        """
        :param BandwidthPackageId: 頻寬包唯一标識ID，形如'bwp-xxxx'
        :type BandwidthPackageId: str
        :param ResourceType: 資源類型，包括‘Address’, ‘LoadBalance’
        :type ResourceType: str
        :param ResourceIds: 資源ID，可支援資源形如'eip-xxxx', 'lb-xxxx'
        :type ResourceIds: list of str
        """
        self.BandwidthPackageId = None
        self.ResourceType = None
        self.ResourceIds = None


    def _deserialize(self, params):
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        self.ResourceType = params.get("ResourceType")
        self.ResourceIds = params.get("ResourceIds")


class RemoveBandwidthPackageResourcesResponse(AbstractModel):
    """RemoveBandwidthPackageResources返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RemoveIp6RulesRequest(AbstractModel):
    """RemoveIp6Rules請求參數結構體

    """

    def __init__(self):
        """
        :param Ip6TranslatorId: IPV6轉換規則所屬的轉換實例唯一ID，形如ip6-xxxxxxxx
        :type Ip6TranslatorId: str
        :param Ip6RuleIds: 待删除IPV6轉換規則，形如rule6-xxxxxxxx
        :type Ip6RuleIds: list of str
        """
        self.Ip6TranslatorId = None
        self.Ip6RuleIds = None


    def _deserialize(self, params):
        self.Ip6TranslatorId = params.get("Ip6TranslatorId")
        self.Ip6RuleIds = params.get("Ip6RuleIds")


class RemoveIp6RulesResponse(AbstractModel):
    """RemoveIp6Rules返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RenewVpnGatewayRequest(AbstractModel):
    """RenewVpnGateway請求參數結構體

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN閘道實例ID。
        :type VpnGatewayId: str
        :param InstanceChargePrepaid: 預付費計費模式。
        :type InstanceChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.InstanceChargePrepaid`
        """
        self.VpnGatewayId = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))


class RenewVpnGatewayResponse(AbstractModel):
    """RenewVpnGateway返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplaceDirectConnectGatewayCcnRoutesRequest(AbstractModel):
    """ReplaceDirectConnectGatewayCcnRoutes請求參數結構體

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: 專線閘道ID，形如：dcg-prpqlmg1
        :type DirectConnectGatewayId: str
        :param Routes: 需要連通的IDC網段清單
        :type Routes: list of DirectConnectGatewayCcnRoute
        """
        self.DirectConnectGatewayId = None
        self.Routes = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = DirectConnectGatewayCcnRoute()
                obj._deserialize(item)
                self.Routes.append(obj)


class ReplaceDirectConnectGatewayCcnRoutesResponse(AbstractModel):
    """ReplaceDirectConnectGatewayCcnRoutes返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplaceRouteTableAssociationRequest(AbstractModel):
    """ReplaceRouteTableAssociation請求參數結構體

    """

    def __init__(self):
        """
        :param SubnetId: 子網實例ID，例如：subnet-3x5lf5q0。可通過DescribeSubnets介面查詢。
        :type SubnetId: str
        :param RouteTableId: 路由表實例ID，例如：rtb-azd4dt1c。
        :type RouteTableId: str
        """
        self.SubnetId = None
        self.RouteTableId = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.RouteTableId = params.get("RouteTableId")


class ReplaceRouteTableAssociationResponse(AbstractModel):
    """ReplaceRouteTableAssociation返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplaceRoutesRequest(AbstractModel):
    """ReplaceRoutes請求參數結構體

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表實例ID，例如：rtb-azd4dt1c。
        :type RouteTableId: str
        :param Routes: 路由策略對象。需要指定路由策略ID（RouteId）。
        :type Routes: list of Route
        """
        self.RouteTableId = None
        self.Routes = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = Route()
                obj._deserialize(item)
                self.Routes.append(obj)


class ReplaceRoutesResponse(AbstractModel):
    """ReplaceRoutes返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplaceSecurityGroupPolicyRequest(AbstractModel):
    """ReplaceSecurityGroupPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全組實例ID，例如sg-33ocnj9n，可通過DescribeSecurityGroups獲取。
        :type SecurityGroupId: str
        :param SecurityGroupPolicySet: 安全組規則集合對象。
        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`
        """
        self.SecurityGroupId = None
        self.SecurityGroupPolicySet = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = SecurityGroupPolicySet()
            self.SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))


class ReplaceSecurityGroupPolicyResponse(AbstractModel):
    """ReplaceSecurityGroupPolicy返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetAttachCcnInstancesRequest(AbstractModel):
    """ResetAttachCcnInstances請求參數結構體

    """

    def __init__(self):
        """
        :param CcnId: CCN實例ID。形如：ccn-f49l6u0z。
        :type CcnId: str
        :param CcnUin: CCN所屬UIN（根賬号）。
        :type CcnUin: str
        :param Instances: 重新申請關聯網絡實例清單。
        :type Instances: list of CcnInstance
        """
        self.CcnId = None
        self.CcnUin = None
        self.Instances = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.CcnUin = params.get("CcnUin")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = CcnInstance()
                obj._deserialize(item)
                self.Instances.append(obj)


class ResetAttachCcnInstancesResponse(AbstractModel):
    """ResetAttachCcnInstances返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetNatGatewayConnectionRequest(AbstractModel):
    """ResetNatGatewayConnection請求參數結構體

    """

    def __init__(self):
        """
        :param NatGatewayId: NAT閘道ID。
        :type NatGatewayId: str
        :param MaxConcurrentConnection: NAT閘道并發連接上限，形如：1000000、3000000、10000000。
        :type MaxConcurrentConnection: int
        """
        self.NatGatewayId = None
        self.MaxConcurrentConnection = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        self.MaxConcurrentConnection = params.get("MaxConcurrentConnection")


class ResetNatGatewayConnectionResponse(AbstractModel):
    """ResetNatGatewayConnection返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetRoutesRequest(AbstractModel):
    """ResetRoutes請求參數結構體

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表實例ID，例如：rtb-azd4dt1c。
        :type RouteTableId: str
        :param RouteTableName: 路由表名稱，最大長度不能超過60個位元。
        :type RouteTableName: str
        :param Routes: 路由策略。
        :type Routes: list of Route
        """
        self.RouteTableId = None
        self.RouteTableName = None
        self.Routes = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RouteTableName = params.get("RouteTableName")
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = Route()
                obj._deserialize(item)
                self.Routes.append(obj)


class ResetRoutesResponse(AbstractModel):
    """ResetRoutes返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetVpnConnectionRequest(AbstractModel):
    """ResetVpnConnection請求參數結構體

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN閘道實例ID。
        :type VpnGatewayId: str
        :param VpnConnectionId: VPN通道實例ID。形如：vpnx-f49l6u0z。
        :type VpnConnectionId: str
        """
        self.VpnGatewayId = None
        self.VpnConnectionId = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.VpnConnectionId = params.get("VpnConnectionId")


class ResetVpnConnectionResponse(AbstractModel):
    """ResetVpnConnection返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetVpnGatewayInternetMaxBandwidthRequest(AbstractModel):
    """ResetVpnGatewayInternetMaxBandwidth請求參數結構體

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN閘道實例ID。
        :type VpnGatewayId: str
        :param InternetMaxBandwidthOut: 公網頻寬設置。可選頻寬規格：5, 10, 20, 50, 100；單位：Mbps。
        :type InternetMaxBandwidthOut: int
        """
        self.VpnGatewayId = None
        self.InternetMaxBandwidthOut = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")


class ResetVpnGatewayInternetMaxBandwidthResponse(AbstractModel):
    """ResetVpnGatewayInternetMaxBandwidth返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Resource(AbstractModel):
    """描述頻寬包資源訊息的結構

    """

    def __init__(self):
        """
        :param ResourceType: 頻寬包資源類型，包括'Address'和'LoadBalance'
        :type ResourceType: str
        :param ResourceId: 頻寬包資源Id，形如'eip-xxxx', 'lb-xxxx'
        :type ResourceId: str
        :param AddressIp: 頻寬包資源Ip
        :type AddressIp: str
        """
        self.ResourceType = None
        self.ResourceId = None
        self.AddressIp = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.ResourceId = params.get("ResourceId")
        self.AddressIp = params.get("AddressIp")


class ResourceDashboard(AbstractModel):
    """VPC資源看板（各資源個數）

    """

    def __init__(self):
        """
        :param VpcId: Vpc實例ID，例如：vpc-f1xjkw1b。
        :type VpcId: str
        :param SubnetId: 子網實例ID，例如：subnet-bthucmmy。
        :type SubnetId: str
        :param Classiclink: 基礎網絡互通。
        :type Classiclink: int
        :param Dcg: 專線閘道。
        :type Dcg: int
        :param Pcx: 對等連接。
        :type Pcx: int
        :param Ip: 當前已使用的IP總數。
        :type Ip: int
        :param Nat: NAT閘道。
        :type Nat: int
        :param Vpngw: VPN閘道。
        :type Vpngw: int
        :param FlowLog: 流日志。
        :type FlowLog: int
        :param NetworkDetect: 網絡探測。
        :type NetworkDetect: int
        :param NetworkACL: 網絡ACL。
        :type NetworkACL: int
        :param CVM: 雲主機。
        :type CVM: int
        :param LB: 負載均衡。
        :type LB: int
        :param CDB: 關系型資料庫。
        :type CDB: int
        :param Cmem: 雲資料庫 TencentDB for Memcached。
        :type Cmem: int
        :param CTSDB: 時序資料庫。
        :type CTSDB: int
        :param MariaDB: 資料庫 TencentDB for MariaDB（TDSQL）。
        :type MariaDB: int
        :param SQLServer: 資料庫 TencentDB for SQL Server。
        :type SQLServer: int
        :param Postgres: 雲資料庫 TencentDB for PostgreSQL。
        :type Postgres: int
        :param NAS: 網絡附加儲存。
        :type NAS: int
        :param Greenplumn: Snova雲數據倉庫。
        :type Greenplumn: int
        :param Ckafka: 訊息隊列 CKAFKA。
        :type Ckafka: int
        :param Grocery: Grocery。
        :type Grocery: int
        :param HSM: 數據加密服務。
        :type HSM: int
        :param Tcaplus: 遊戲儲存 Tcaplus。
        :type Tcaplus: int
        :param Cnas: Cnas。
        :type Cnas: int
        :param TiDB: HTAP 資料庫 TiDB。
        :type TiDB: int
        :param Emr: EMR 集群。
        :type Emr: int
        :param SEAL: SEAL。
        :type SEAL: int
        :param CFS: 文件儲存 CFS。
        :type CFS: int
        :param Oracle: Oracle。
        :type Oracle: int
        :param ElasticSearch: ElasticSearch服務。
        :type ElasticSearch: int
        :param TBaaS: 區塊鏈服務。
        :type TBaaS: int
        :param Itop: Itop。
        :type Itop: int
        :param DBAudit: 雲資料庫審計。
        :type DBAudit: int
        :param CynosDBPostgres: 企業級雲資料庫 CynosDB for Postgres。
        :type CynosDBPostgres: int
        :param Redis: 資料庫 TencentDB for Redis。
        :type Redis: int
        :param MongoDB: 資料庫 TencentDB for MongoDB。
        :type MongoDB: int
        :param DCDB: 分布式資料庫 TencentDB for TDSQL。
        :type DCDB: int
        :param CynosDBMySQL: 企業級雲資料庫 CynosDB for MySQL。
        :type CynosDBMySQL: int
        :param Subnet: 子網。
        :type Subnet: int
        :param RouteTable: 路由表。
        :type RouteTable: int
        """
        self.VpcId = None
        self.SubnetId = None
        self.Classiclink = None
        self.Dcg = None
        self.Pcx = None
        self.Ip = None
        self.Nat = None
        self.Vpngw = None
        self.FlowLog = None
        self.NetworkDetect = None
        self.NetworkACL = None
        self.CVM = None
        self.LB = None
        self.CDB = None
        self.Cmem = None
        self.CTSDB = None
        self.MariaDB = None
        self.SQLServer = None
        self.Postgres = None
        self.NAS = None
        self.Greenplumn = None
        self.Ckafka = None
        self.Grocery = None
        self.HSM = None
        self.Tcaplus = None
        self.Cnas = None
        self.TiDB = None
        self.Emr = None
        self.SEAL = None
        self.CFS = None
        self.Oracle = None
        self.ElasticSearch = None
        self.TBaaS = None
        self.Itop = None
        self.DBAudit = None
        self.CynosDBPostgres = None
        self.Redis = None
        self.MongoDB = None
        self.DCDB = None
        self.CynosDBMySQL = None
        self.Subnet = None
        self.RouteTable = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Classiclink = params.get("Classiclink")
        self.Dcg = params.get("Dcg")
        self.Pcx = params.get("Pcx")
        self.Ip = params.get("Ip")
        self.Nat = params.get("Nat")
        self.Vpngw = params.get("Vpngw")
        self.FlowLog = params.get("FlowLog")
        self.NetworkDetect = params.get("NetworkDetect")
        self.NetworkACL = params.get("NetworkACL")
        self.CVM = params.get("CVM")
        self.LB = params.get("LB")
        self.CDB = params.get("CDB")
        self.Cmem = params.get("Cmem")
        self.CTSDB = params.get("CTSDB")
        self.MariaDB = params.get("MariaDB")
        self.SQLServer = params.get("SQLServer")
        self.Postgres = params.get("Postgres")
        self.NAS = params.get("NAS")
        self.Greenplumn = params.get("Greenplumn")
        self.Ckafka = params.get("Ckafka")
        self.Grocery = params.get("Grocery")
        self.HSM = params.get("HSM")
        self.Tcaplus = params.get("Tcaplus")
        self.Cnas = params.get("Cnas")
        self.TiDB = params.get("TiDB")
        self.Emr = params.get("Emr")
        self.SEAL = params.get("SEAL")
        self.CFS = params.get("CFS")
        self.Oracle = params.get("Oracle")
        self.ElasticSearch = params.get("ElasticSearch")
        self.TBaaS = params.get("TBaaS")
        self.Itop = params.get("Itop")
        self.DBAudit = params.get("DBAudit")
        self.CynosDBPostgres = params.get("CynosDBPostgres")
        self.Redis = params.get("Redis")
        self.MongoDB = params.get("MongoDB")
        self.DCDB = params.get("DCDB")
        self.CynosDBMySQL = params.get("CynosDBMySQL")
        self.Subnet = params.get("Subnet")
        self.RouteTable = params.get("RouteTable")


class Route(AbstractModel):
    """路由策略對象

    """

    def __init__(self):
        """
        :param DestinationCidrBlock: 目的網段，取值不能在私有網絡網段内，例如：112.20.51.0/24。
        :type DestinationCidrBlock: str
        :param GatewayType: 下一跳類型，目前我們支援的類型有：
CVM：公網閘道類型的雲伺服器；
VPN：VPN閘道；
DIRECTCONNECT：專線閘道；
PEERCONNECTION：對等連接；
SSLVPN：sslvpn閘道；
NAT：NAT閘道; 
NORMAL_CVM：普通雲伺服器；
EIP：雲伺服器的公網IP；
CCN：雲聯網。
        :type GatewayType: str
        :param GatewayId: 下一跳網址，這裏只需要指定不同下一跳類型的閘道ID，系統會自動比對到下一跳網址。
特别注意：當 GatewayType 爲 EIP 時，GatewayId 固定值 '0'
        :type GatewayId: str
        :param RouteId: 路由策略ID。
        :type RouteId: int
        :param RouteDescription: 路由策略描述。
        :type RouteDescription: str
        :param Enabled: 是否啓用
        :type Enabled: bool
        :param RouteType: 路由類型，目前我們支援的類型有：
USER：用戶路由；
NETD：網絡探測路由，創建網絡探測實例時，系統預設下發，不可編輯與删除；
CCN：雲聯網路由，系統預設下發，不可編輯與删除。
用戶只能添加和操作 USER 類型的路由。
        :type RouteType: str
        :param RouteTableId: 路由表實例ID，例如：rtb-azd4dt1c。
        :type RouteTableId: str
        """
        self.DestinationCidrBlock = None
        self.GatewayType = None
        self.GatewayId = None
        self.RouteId = None
        self.RouteDescription = None
        self.Enabled = None
        self.RouteType = None
        self.RouteTableId = None


    def _deserialize(self, params):
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        self.GatewayType = params.get("GatewayType")
        self.GatewayId = params.get("GatewayId")
        self.RouteId = params.get("RouteId")
        self.RouteDescription = params.get("RouteDescription")
        self.Enabled = params.get("Enabled")
        self.RouteType = params.get("RouteType")
        self.RouteTableId = params.get("RouteTableId")


class RouteConflict(AbstractModel):
    """路由沖突對象

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表實例ID，例如：rtb-azd4dt1c。
        :type RouteTableId: str
        :param DestinationCidrBlock: 要檢查的與之沖突的目的端
        :type DestinationCidrBlock: str
        :param ConflictSet: 沖突的路由策略清單
        :type ConflictSet: list of Route
        """
        self.RouteTableId = None
        self.DestinationCidrBlock = None
        self.ConflictSet = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        if params.get("ConflictSet") is not None:
            self.ConflictSet = []
            for item in params.get("ConflictSet"):
                obj = Route()
                obj._deserialize(item)
                self.ConflictSet.append(obj)


class RouteTable(AbstractModel):
    """路由表對象

    """

    def __init__(self):
        """
        :param VpcId: VPC實例ID。
        :type VpcId: str
        :param RouteTableId: 路由表實例ID，例如：rtb-azd4dt1c。
        :type RouteTableId: str
        :param RouteTableName: 路由表名稱。
        :type RouteTableName: str
        :param AssociationSet: 路由表關聯關系。
        :type AssociationSet: list of RouteTableAssociation
        :param RouteSet: 路由表策略集合。
        :type RouteSet: list of Route
        :param Main: 是否預設路由表。
        :type Main: bool
        :param CreatedTime: 創建時間。
        :type CreatedTime: str
        :param TagSet: 标簽鍵值對。
        :type TagSet: list of Tag
        """
        self.VpcId = None
        self.RouteTableId = None
        self.RouteTableName = None
        self.AssociationSet = None
        self.RouteSet = None
        self.Main = None
        self.CreatedTime = None
        self.TagSet = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.RouteTableId = params.get("RouteTableId")
        self.RouteTableName = params.get("RouteTableName")
        if params.get("AssociationSet") is not None:
            self.AssociationSet = []
            for item in params.get("AssociationSet"):
                obj = RouteTableAssociation()
                obj._deserialize(item)
                self.AssociationSet.append(obj)
        if params.get("RouteSet") is not None:
            self.RouteSet = []
            for item in params.get("RouteSet"):
                obj = Route()
                obj._deserialize(item)
                self.RouteSet.append(obj)
        self.Main = params.get("Main")
        self.CreatedTime = params.get("CreatedTime")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)


class RouteTableAssociation(AbstractModel):
    """路由表關聯關系

    """

    def __init__(self):
        """
        :param SubnetId: 子網實例ID。
        :type SubnetId: str
        :param RouteTableId: 路由表實例ID。
        :type RouteTableId: str
        """
        self.SubnetId = None
        self.RouteTableId = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.RouteTableId = params.get("RouteTableId")


class SecurityGroup(AbstractModel):
    """安全組對象

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全組實例ID，例如：sg-ohuuioma。
        :type SecurityGroupId: str
        :param SecurityGroupName: 安全組名稱，可任意命名，但不得超過60個字元。
        :type SecurityGroupName: str
        :param SecurityGroupDesc: 安全組備注，最多100個字元。
        :type SecurityGroupDesc: str
        :param ProjectId: 項目id，預設0。可在qcloud控制台項目管理頁面查詢到。
        :type ProjectId: str
        :param IsDefault: 是否是預設安全組，預設安全組不支援删除。
        :type IsDefault: bool
        :param CreatedTime: 安全組創建時間。
        :type CreatedTime: str
        :param TagSet: 标簽鍵值對。
        :type TagSet: list of Tag
        """
        self.SecurityGroupId = None
        self.SecurityGroupName = None
        self.SecurityGroupDesc = None
        self.ProjectId = None
        self.IsDefault = None
        self.CreatedTime = None
        self.TagSet = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.SecurityGroupName = params.get("SecurityGroupName")
        self.SecurityGroupDesc = params.get("SecurityGroupDesc")
        self.ProjectId = params.get("ProjectId")
        self.IsDefault = params.get("IsDefault")
        self.CreatedTime = params.get("CreatedTime")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)


class SecurityGroupAssociationStatistics(AbstractModel):
    """安全組關聯的實例統計

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全組實例ID。
        :type SecurityGroupId: str
        :param CVM: 雲伺服器實例數。
        :type CVM: int
        :param CDB: 資料庫實例數。
        :type CDB: int
        :param ENI: 彈性網卡實例數。
        :type ENI: int
        :param SG: 被安全組引用數。
        :type SG: int
        :param CLB: 負載均衡實例數。
        :type CLB: int
        :param InstanceStatistics: 全量實例的綁定統計。
        :type InstanceStatistics: list of InstanceStatistic
        :param TotalCount: 所有資源的總計數（不包含被安全組引用數）。
        :type TotalCount: int
        """
        self.SecurityGroupId = None
        self.CVM = None
        self.CDB = None
        self.ENI = None
        self.SG = None
        self.CLB = None
        self.InstanceStatistics = None
        self.TotalCount = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.CVM = params.get("CVM")
        self.CDB = params.get("CDB")
        self.ENI = params.get("ENI")
        self.SG = params.get("SG")
        self.CLB = params.get("CLB")
        if params.get("InstanceStatistics") is not None:
            self.InstanceStatistics = []
            for item in params.get("InstanceStatistics"):
                obj = InstanceStatistic()
                obj._deserialize(item)
                self.InstanceStatistics.append(obj)
        self.TotalCount = params.get("TotalCount")


class SecurityGroupLimitSet(AbstractModel):
    """用戶安全組配額限制。

    """

    def __init__(self):
        """
        :param SecurityGroupLimit: 每個項目每個地域可創建安全組數
        :type SecurityGroupLimit: int
        :param SecurityGroupPolicyLimit: 安全組下的最大規則數
        :type SecurityGroupPolicyLimit: int
        :param ReferedSecurityGroupLimit: 安全組下嵌套安全組規則數
        :type ReferedSecurityGroupLimit: int
        :param SecurityGroupInstanceLimit: 單安全組關聯實例數
        :type SecurityGroupInstanceLimit: int
        :param InstanceSecurityGroupLimit: 實例關聯安全組數
        :type InstanceSecurityGroupLimit: int
        """
        self.SecurityGroupLimit = None
        self.SecurityGroupPolicyLimit = None
        self.ReferedSecurityGroupLimit = None
        self.SecurityGroupInstanceLimit = None
        self.InstanceSecurityGroupLimit = None


    def _deserialize(self, params):
        self.SecurityGroupLimit = params.get("SecurityGroupLimit")
        self.SecurityGroupPolicyLimit = params.get("SecurityGroupPolicyLimit")
        self.ReferedSecurityGroupLimit = params.get("ReferedSecurityGroupLimit")
        self.SecurityGroupInstanceLimit = params.get("SecurityGroupInstanceLimit")
        self.InstanceSecurityGroupLimit = params.get("InstanceSecurityGroupLimit")


class SecurityGroupPolicy(AbstractModel):
    """安全組規則對象

    """

    def __init__(self):
        """
        :param PolicyIndex: 安全組規則索引号。
        :type PolicyIndex: int
        :param Protocol: 協議, 取值: TCP,UDP, ICMP。
        :type Protocol: str
        :param Port: 端口(all, 離散port,  range)。
        :type Port: str
        :param ServiceTemplate: 協議端口ID或者協議端口組ID。ServiceTemplate和Protocol+Port互斥。
        :type ServiceTemplate: :class:`tencentcloud.vpc.v20170312.models.ServiceTemplateSpecification`
        :param CidrBlock: 網段或IP(互斥)。
        :type CidrBlock: str
        :param Ipv6CidrBlock: 網段或IPv6(互斥)。
        :type Ipv6CidrBlock: str
        :param SecurityGroupId: 安全組實例ID，例如：sg-ohuuioma。
        :type SecurityGroupId: str
        :param AddressTemplate: IP網址ID或者ID網址組ID。
        :type AddressTemplate: :class:`tencentcloud.vpc.v20170312.models.AddressTemplateSpecification`
        :param Action: ACCEPT 或 DROP。
        :type Action: str
        :param PolicyDescription: 安全組規則描述。
        :type PolicyDescription: str
        :param ModifyTime: 安全組最近修改時間。
        :type ModifyTime: str
        """
        self.PolicyIndex = None
        self.Protocol = None
        self.Port = None
        self.ServiceTemplate = None
        self.CidrBlock = None
        self.Ipv6CidrBlock = None
        self.SecurityGroupId = None
        self.AddressTemplate = None
        self.Action = None
        self.PolicyDescription = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.PolicyIndex = params.get("PolicyIndex")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        if params.get("ServiceTemplate") is not None:
            self.ServiceTemplate = ServiceTemplateSpecification()
            self.ServiceTemplate._deserialize(params.get("ServiceTemplate"))
        self.CidrBlock = params.get("CidrBlock")
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("AddressTemplate") is not None:
            self.AddressTemplate = AddressTemplateSpecification()
            self.AddressTemplate._deserialize(params.get("AddressTemplate"))
        self.Action = params.get("Action")
        self.PolicyDescription = params.get("PolicyDescription")
        self.ModifyTime = params.get("ModifyTime")


class SecurityGroupPolicySet(AbstractModel):
    """安全組規則集合

    """

    def __init__(self):
        """
        :param Version: 安全組規則當前版本。用戶每次更新安全規則版本會自動加1，防止更新的路由規則已過期，不填不考慮沖突。
        :type Version: str
        :param Egress: 出站規則。
        :type Egress: list of SecurityGroupPolicy
        :param Ingress: 入站規則。
        :type Ingress: list of SecurityGroupPolicy
        """
        self.Version = None
        self.Egress = None
        self.Ingress = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        if params.get("Egress") is not None:
            self.Egress = []
            for item in params.get("Egress"):
                obj = SecurityGroupPolicy()
                obj._deserialize(item)
                self.Egress.append(obj)
        if params.get("Ingress") is not None:
            self.Ingress = []
            for item in params.get("Ingress"):
                obj = SecurityGroupPolicy()
                obj._deserialize(item)
                self.Ingress.append(obj)


class SecurityPolicyDatabase(AbstractModel):
    """SecurityPolicyDatabase策略

    """

    def __init__(self):
        """
        :param LocalCidrBlock: 本端網段
        :type LocalCidrBlock: str
        :param RemoteCidrBlock: 對端網段
        :type RemoteCidrBlock: list of str
        """
        self.LocalCidrBlock = None
        self.RemoteCidrBlock = None


    def _deserialize(self, params):
        self.LocalCidrBlock = params.get("LocalCidrBlock")
        self.RemoteCidrBlock = params.get("RemoteCidrBlock")


class ServiceTemplate(AbstractModel):
    """協議端口範本

    """

    def __init__(self):
        """
        :param ServiceTemplateId: 協議端口實例ID，例如：ppm-f5n1f8da。
        :type ServiceTemplateId: str
        :param ServiceTemplateName: 範本名稱。
        :type ServiceTemplateName: str
        :param ServiceSet: 協議端口訊息。
        :type ServiceSet: list of str
        :param CreatedTime: 創建時間。
        :type CreatedTime: str
        """
        self.ServiceTemplateId = None
        self.ServiceTemplateName = None
        self.ServiceSet = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.ServiceTemplateId = params.get("ServiceTemplateId")
        self.ServiceTemplateName = params.get("ServiceTemplateName")
        self.ServiceSet = params.get("ServiceSet")
        self.CreatedTime = params.get("CreatedTime")


class ServiceTemplateGroup(AbstractModel):
    """協議端口範本集合

    """

    def __init__(self):
        """
        :param ServiceTemplateGroupId: 協議端口範本集合實例ID，例如：ppmg-2klmrefu。
        :type ServiceTemplateGroupId: str
        :param ServiceTemplateGroupName: 協議端口範本集合名稱。
        :type ServiceTemplateGroupName: str
        :param ServiceTemplateIdSet: 協議端口範本實例ID。
        :type ServiceTemplateIdSet: list of str
        :param CreatedTime: 創建時間。
        :type CreatedTime: str
        :param ServiceTemplateSet: 協議端口範本實例訊息。
        :type ServiceTemplateSet: list of ServiceTemplate
        """
        self.ServiceTemplateGroupId = None
        self.ServiceTemplateGroupName = None
        self.ServiceTemplateIdSet = None
        self.CreatedTime = None
        self.ServiceTemplateSet = None


    def _deserialize(self, params):
        self.ServiceTemplateGroupId = params.get("ServiceTemplateGroupId")
        self.ServiceTemplateGroupName = params.get("ServiceTemplateGroupName")
        self.ServiceTemplateIdSet = params.get("ServiceTemplateIdSet")
        self.CreatedTime = params.get("CreatedTime")
        if params.get("ServiceTemplateSet") is not None:
            self.ServiceTemplateSet = []
            for item in params.get("ServiceTemplateSet"):
                obj = ServiceTemplate()
                obj._deserialize(item)
                self.ServiceTemplateSet.append(obj)


class ServiceTemplateSpecification(AbstractModel):
    """協議端口模版

    """

    def __init__(self):
        """
        :param ServiceId: 協議端口ID，例如：ppm-f5n1f8da。
        :type ServiceId: str
        :param ServiceGroupId: 協議端口組ID，例如：ppmg-f5n1f8da。
        :type ServiceGroupId: str
        """
        self.ServiceId = None
        self.ServiceGroupId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ServiceGroupId = params.get("ServiceGroupId")


class SetCcnRegionBandwidthLimitsRequest(AbstractModel):
    """SetCcnRegionBandwidthLimits請求參數結構體

    """

    def __init__(self):
        """
        :param CcnId: CCN實例ID。形如：ccn-f49l6u0z。
        :type CcnId: str
        :param CcnRegionBandwidthLimits: 雲聯網（CCN）各地域出頻寬上限。
        :type CcnRegionBandwidthLimits: list of CcnRegionBandwidthLimit
        """
        self.CcnId = None
        self.CcnRegionBandwidthLimits = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        if params.get("CcnRegionBandwidthLimits") is not None:
            self.CcnRegionBandwidthLimits = []
            for item in params.get("CcnRegionBandwidthLimits"):
                obj = CcnRegionBandwidthLimit()
                obj._deserialize(item)
                self.CcnRegionBandwidthLimits.append(obj)


class SetCcnRegionBandwidthLimitsResponse(AbstractModel):
    """SetCcnRegionBandwidthLimits返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Subnet(AbstractModel):
    """子網對象

    """

    def __init__(self):
        """
        :param VpcId: `VPC`實例`ID`。
        :type VpcId: str
        :param SubnetId: 子網實例`ID`，例如：subnet-bthucmmy。
        :type SubnetId: str
        :param SubnetName: 子網名稱。
        :type SubnetName: str
        :param CidrBlock: 子網的 `IPv4` `CIDR`。
        :type CidrBlock: str
        :param IsDefault: 是否預設子網。
        :type IsDefault: bool
        :param EnableBroadcast: 是否開啓廣播。
        :type EnableBroadcast: bool
        :param Zone: 可用區。
        :type Zone: str
        :param RouteTableId: 路由表實例ID，例如：rtb-l2h8d7c2。
        :type RouteTableId: str
        :param CreatedTime: 創建時間。
        :type CreatedTime: str
        :param AvailableIpAddressCount: 可用`IP`數。
        :type AvailableIpAddressCount: int
        :param Ipv6CidrBlock: 子網的 `IPv6` `CIDR`。
        :type Ipv6CidrBlock: str
        :param NetworkAclId: 關聯`ACL`ID
        :type NetworkAclId: str
        :param IsRemoteVpcSnat: 是否爲 `SNAT` 網址池子網。
        :type IsRemoteVpcSnat: bool
        :param TotalIpAddressCount: 子網`IP`總數。
        :type TotalIpAddressCount: int
        :param TagSet: 标簽鍵值對。
        :type TagSet: list of Tag
        """
        self.VpcId = None
        self.SubnetId = None
        self.SubnetName = None
        self.CidrBlock = None
        self.IsDefault = None
        self.EnableBroadcast = None
        self.Zone = None
        self.RouteTableId = None
        self.CreatedTime = None
        self.AvailableIpAddressCount = None
        self.Ipv6CidrBlock = None
        self.NetworkAclId = None
        self.IsRemoteVpcSnat = None
        self.TotalIpAddressCount = None
        self.TagSet = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.CidrBlock = params.get("CidrBlock")
        self.IsDefault = params.get("IsDefault")
        self.EnableBroadcast = params.get("EnableBroadcast")
        self.Zone = params.get("Zone")
        self.RouteTableId = params.get("RouteTableId")
        self.CreatedTime = params.get("CreatedTime")
        self.AvailableIpAddressCount = params.get("AvailableIpAddressCount")
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        self.NetworkAclId = params.get("NetworkAclId")
        self.IsRemoteVpcSnat = params.get("IsRemoteVpcSnat")
        self.TotalIpAddressCount = params.get("TotalIpAddressCount")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)


class SubnetInput(AbstractModel):
    """子網對象

    """

    def __init__(self):
        """
        :param CidrBlock: 子網的`CIDR`。
        :type CidrBlock: str
        :param SubnetName: 子網名稱。
        :type SubnetName: str
        :param Zone: 可用區。形如：`ap-guangzhou-2`。
        :type Zone: str
        :param RouteTableId: 指定關聯路由表，形如：`rtb-3ryrwzuu`。
        :type RouteTableId: str
        """
        self.CidrBlock = None
        self.SubnetName = None
        self.Zone = None
        self.RouteTableId = None


    def _deserialize(self, params):
        self.CidrBlock = params.get("CidrBlock")
        self.SubnetName = params.get("SubnetName")
        self.Zone = params.get("Zone")
        self.RouteTableId = params.get("RouteTableId")


class Tag(AbstractModel):
    """标簽鍵值對

    """

    def __init__(self):
        """
        :param Key: 标簽鍵
注意：此欄位可能返回 null，表示取不到有效值。
        :type Key: str
        :param Value: 标簽值
注意：此欄位可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class TemplateLimit(AbstractModel):
    """參數範本配額

    """

    def __init__(self):
        """
        :param AddressTemplateMemberLimit: 參數範本IP網址成員配額。
        :type AddressTemplateMemberLimit: int
        :param AddressTemplateGroupMemberLimit: 參數範本IP網址組成員配額。
        :type AddressTemplateGroupMemberLimit: int
        :param ServiceTemplateMemberLimit: 參數範本I協議端口成員配額。
        :type ServiceTemplateMemberLimit: int
        :param ServiceTemplateGroupMemberLimit: 參數範本協議端口組成員配額。
        :type ServiceTemplateGroupMemberLimit: int
        """
        self.AddressTemplateMemberLimit = None
        self.AddressTemplateGroupMemberLimit = None
        self.ServiceTemplateMemberLimit = None
        self.ServiceTemplateGroupMemberLimit = None


    def _deserialize(self, params):
        self.AddressTemplateMemberLimit = params.get("AddressTemplateMemberLimit")
        self.AddressTemplateGroupMemberLimit = params.get("AddressTemplateGroupMemberLimit")
        self.ServiceTemplateMemberLimit = params.get("ServiceTemplateMemberLimit")
        self.ServiceTemplateGroupMemberLimit = params.get("ServiceTemplateGroupMemberLimit")


class TransformAddressRequest(AbstractModel):
    """TransformAddress請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 待操作有普通公網 IP 的實例 ID。實例 ID 形如：`ins-11112222`。可通過登入[控制台](https://console.cloud.tencent.com/cvm)查詢，也可通過 [DescribeInstances](https://cloud.tencent.com/document/api/213/9389) 介面返回值中的`InstanceId`獲取。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class TransformAddressResponse(AbstractModel):
    """TransformAddress返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnassignIpv6AddressesRequest(AbstractModel):
    """UnassignIpv6Addresses請求參數結構體

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 彈性網卡實例`ID`，形如：`eni-m6dyj72l`。
        :type NetworkInterfaceId: str
        :param Ipv6Addresses: 指定的`IPv6`網址清單，單次最多指定10個。
        :type Ipv6Addresses: list of Ipv6Address
        """
        self.NetworkInterfaceId = None
        self.Ipv6Addresses = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("Ipv6Addresses") is not None:
            self.Ipv6Addresses = []
            for item in params.get("Ipv6Addresses"):
                obj = Ipv6Address()
                obj._deserialize(item)
                self.Ipv6Addresses.append(obj)


class UnassignIpv6AddressesResponse(AbstractModel):
    """UnassignIpv6Addresses返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnassignIpv6CidrBlockRequest(AbstractModel):
    """UnassignIpv6CidrBlock請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: `VPC`實例`ID`，形如：`vpc-f49l6u0z`。
        :type VpcId: str
        :param Ipv6CidrBlock: `IPv6`網段。形如：`3402:4e00:20:1000::/56`
        :type Ipv6CidrBlock: str
        """
        self.VpcId = None
        self.Ipv6CidrBlock = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")


class UnassignIpv6CidrBlockResponse(AbstractModel):
    """UnassignIpv6CidrBlock返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnassignIpv6SubnetCidrBlockRequest(AbstractModel):
    """UnassignIpv6SubnetCidrBlock請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: 子網所在私有網絡`ID`。形如：`vpc-f49l6u0z`。
        :type VpcId: str
        :param Ipv6SubnetCidrBlocks: `IPv6` 子網段清單。
        :type Ipv6SubnetCidrBlocks: list of Ipv6SubnetCidrBlock
        """
        self.VpcId = None
        self.Ipv6SubnetCidrBlocks = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        if params.get("Ipv6SubnetCidrBlocks") is not None:
            self.Ipv6SubnetCidrBlocks = []
            for item in params.get("Ipv6SubnetCidrBlocks"):
                obj = Ipv6SubnetCidrBlock()
                obj._deserialize(item)
                self.Ipv6SubnetCidrBlocks.append(obj)


class UnassignIpv6SubnetCidrBlockResponse(AbstractModel):
    """UnassignIpv6SubnetCidrBlock返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnassignPrivateIpAddressesRequest(AbstractModel):
    """UnassignPrivateIpAddresses請求參數結構體

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 彈性網卡實例ID，例如：eni-m6dyj72l。
        :type NetworkInterfaceId: str
        :param PrivateIpAddresses: 指定的内網IP訊息，單次最多指定10個。
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        """
        self.NetworkInterfaceId = None
        self.PrivateIpAddresses = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("PrivateIpAddresses") is not None:
            self.PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self.PrivateIpAddresses.append(obj)


class UnassignPrivateIpAddressesResponse(AbstractModel):
    """UnassignPrivateIpAddresses返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Vpc(AbstractModel):
    """私有網絡(VPC)對象。

    """

    def __init__(self):
        """
        :param VpcName: `VPC`名稱。
        :type VpcName: str
        :param VpcId: `VPC`實例`ID`，例如：vpc-azd4dt1c。
        :type VpcId: str
        :param CidrBlock: `VPC`的`IPv4` `CIDR`。
        :type CidrBlock: str
        :param IsDefault: 是否預設`VPC`。
        :type IsDefault: bool
        :param EnableMulticast: 是否開啓組播。
        :type EnableMulticast: bool
        :param CreatedTime: 創建時間。
        :type CreatedTime: str
        :param DnsServerSet: `DNS`清單。
        :type DnsServerSet: list of str
        :param DomainName: `DHCP`域名選項值。
        :type DomainName: str
        :param DhcpOptionsId: `DHCP`選項集`ID`。
        :type DhcpOptionsId: str
        :param EnableDhcp: 是否開啓`DHCP`。
        :type EnableDhcp: bool
        :param Ipv6CidrBlock: `VPC`的`IPv6` `CIDR`。
        :type Ipv6CidrBlock: str
        :param TagSet: 标簽鍵值對
        :type TagSet: list of Tag
        :param AssistantCidrSet: 輔助CIDR
注意：此欄位可能返回 null，表示取不到有效值。
        :type AssistantCidrSet: list of AssistantCidr
        """
        self.VpcName = None
        self.VpcId = None
        self.CidrBlock = None
        self.IsDefault = None
        self.EnableMulticast = None
        self.CreatedTime = None
        self.DnsServerSet = None
        self.DomainName = None
        self.DhcpOptionsId = None
        self.EnableDhcp = None
        self.Ipv6CidrBlock = None
        self.TagSet = None
        self.AssistantCidrSet = None


    def _deserialize(self, params):
        self.VpcName = params.get("VpcName")
        self.VpcId = params.get("VpcId")
        self.CidrBlock = params.get("CidrBlock")
        self.IsDefault = params.get("IsDefault")
        self.EnableMulticast = params.get("EnableMulticast")
        self.CreatedTime = params.get("CreatedTime")
        self.DnsServerSet = params.get("DnsServerSet")
        self.DomainName = params.get("DomainName")
        self.DhcpOptionsId = params.get("DhcpOptionsId")
        self.EnableDhcp = params.get("EnableDhcp")
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        if params.get("AssistantCidrSet") is not None:
            self.AssistantCidrSet = []
            for item in params.get("AssistantCidrSet"):
                obj = AssistantCidr()
                obj._deserialize(item)
                self.AssistantCidrSet.append(obj)


class VpcIpv6Address(AbstractModel):
    """VPC内網IPv6對象。

    """

    def __init__(self):
        """
        :param Ipv6Address: `VPC`内`IPv6`網址。
        :type Ipv6Address: str
        :param CidrBlock: 所屬子網 `IPv6` `CIDR`。
        :type CidrBlock: str
        :param Ipv6AddressType: `IPv6`類型。
        :type Ipv6AddressType: str
        :param CreatedTime: `IPv6`申請時間。
        :type CreatedTime: str
        """
        self.Ipv6Address = None
        self.CidrBlock = None
        self.Ipv6AddressType = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.Ipv6Address = params.get("Ipv6Address")
        self.CidrBlock = params.get("CidrBlock")
        self.Ipv6AddressType = params.get("Ipv6AddressType")
        self.CreatedTime = params.get("CreatedTime")


class VpcLimit(AbstractModel):
    """私有網絡配額

    """

    def __init__(self):
        """
        :param LimitType: 私有網絡配額描述
        :type LimitType: str
        :param LimitValue: 私有網絡配額值
        :type LimitValue: int
        """
        self.LimitType = None
        self.LimitValue = None


    def _deserialize(self, params):
        self.LimitType = params.get("LimitType")
        self.LimitValue = params.get("LimitValue")


class VpcPrivateIpAddress(AbstractModel):
    """VPC内網IP對象。

    """

    def __init__(self):
        """
        :param PrivateIpAddress: `VPC`内網`IP`。
        :type PrivateIpAddress: str
        :param CidrBlock: 所屬子網`CIDR`。
        :type CidrBlock: str
        :param PrivateIpAddressType: 内網`IP`類型。
        :type PrivateIpAddressType: str
        :param CreatedTime: `IP`申請時間。
        :type CreatedTime: str
        """
        self.PrivateIpAddress = None
        self.CidrBlock = None
        self.PrivateIpAddressType = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        self.CidrBlock = params.get("CidrBlock")
        self.PrivateIpAddressType = params.get("PrivateIpAddressType")
        self.CreatedTime = params.get("CreatedTime")


class VpnConnection(AbstractModel):
    """VPN通道對象。

    """

    def __init__(self):
        """
        :param VpnConnectionId: 通道實例ID。
        :type VpnConnectionId: str
        :param VpnConnectionName: 通道名稱。
        :type VpnConnectionName: str
        :param VpcId: VPC實例ID。
        :type VpcId: str
        :param VpnGatewayId: VPN閘道實例ID。
        :type VpnGatewayId: str
        :param CustomerGatewayId: 對端閘道實例ID。
        :type CustomerGatewayId: str
        :param PreShareKey: 預共享金鑰。
        :type PreShareKey: str
        :param VpnProto: 通道傳輸協議。
        :type VpnProto: str
        :param EncryptProto: 通道加密協議。
        :type EncryptProto: str
        :param RouteType: 路由類型。
        :type RouteType: str
        :param CreatedTime: 創建時間。
        :type CreatedTime: str
        :param State: 通道的生産狀态，PENDING：生産中，AVAILABLE：運作中，DELETING：删除中。
        :type State: str
        :param NetStatus: 通道連接狀态，AVAILABLE：已連接。
        :type NetStatus: str
        :param SecurityPolicyDatabaseSet: SPD。
        :type SecurityPolicyDatabaseSet: list of SecurityPolicyDatabase
        :param IKEOptionsSpecification: IKE選項。
        :type IKEOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IKEOptionsSpecification`
        :param IPSECOptionsSpecification: IPSEC選擇。
        :type IPSECOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IPSECOptionsSpecification`
        """
        self.VpnConnectionId = None
        self.VpnConnectionName = None
        self.VpcId = None
        self.VpnGatewayId = None
        self.CustomerGatewayId = None
        self.PreShareKey = None
        self.VpnProto = None
        self.EncryptProto = None
        self.RouteType = None
        self.CreatedTime = None
        self.State = None
        self.NetStatus = None
        self.SecurityPolicyDatabaseSet = None
        self.IKEOptionsSpecification = None
        self.IPSECOptionsSpecification = None


    def _deserialize(self, params):
        self.VpnConnectionId = params.get("VpnConnectionId")
        self.VpnConnectionName = params.get("VpnConnectionName")
        self.VpcId = params.get("VpcId")
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.CustomerGatewayId = params.get("CustomerGatewayId")
        self.PreShareKey = params.get("PreShareKey")
        self.VpnProto = params.get("VpnProto")
        self.EncryptProto = params.get("EncryptProto")
        self.RouteType = params.get("RouteType")
        self.CreatedTime = params.get("CreatedTime")
        self.State = params.get("State")
        self.NetStatus = params.get("NetStatus")
        if params.get("SecurityPolicyDatabaseSet") is not None:
            self.SecurityPolicyDatabaseSet = []
            for item in params.get("SecurityPolicyDatabaseSet"):
                obj = SecurityPolicyDatabase()
                obj._deserialize(item)
                self.SecurityPolicyDatabaseSet.append(obj)
        if params.get("IKEOptionsSpecification") is not None:
            self.IKEOptionsSpecification = IKEOptionsSpecification()
            self.IKEOptionsSpecification._deserialize(params.get("IKEOptionsSpecification"))
        if params.get("IPSECOptionsSpecification") is not None:
            self.IPSECOptionsSpecification = IPSECOptionsSpecification()
            self.IPSECOptionsSpecification._deserialize(params.get("IPSECOptionsSpecification"))


class VpnGateway(AbstractModel):
    """VPN閘道對象。

    """

    def __init__(self):
        """
        :param VpnGatewayId: 閘道實例ID。
        :type VpnGatewayId: str
        :param VpcId: VPC實例ID。
        :type VpcId: str
        :param VpnGatewayName: 閘道實例名稱。
        :type VpnGatewayName: str
        :param Type: 閘道實例類型：'IPSEC', 'SSL','CCN'。
        :type Type: str
        :param State: 閘道實例狀态， 'PENDING'：生産中，'DELETING'：删除中，'AVAILABLE'：運作中。
        :type State: str
        :param PublicIpAddress: 閘道公網IP。
        :type PublicIpAddress: str
        :param RenewFlag: 閘道續約類型：'NOTIFY_AND_MANUAL_RENEW'：手動續約，'NOTIFY_AND_AUTO_RENEW'：自動續約，'NOT_NOTIFY_AND_NOT_RENEW'：到期不續約。
        :type RenewFlag: str
        :param InstanceChargeType: 閘道付費類型：POSTPAID_BY_HOUR：按小時後付費，PREPAID：包年包月預付費，
        :type InstanceChargeType: str
        :param InternetMaxBandwidthOut: 閘道出頻寬。
        :type InternetMaxBandwidthOut: int
        :param CreatedTime: 創建時間。
        :type CreatedTime: str
        :param ExpiredTime: 預付費閘道過期時間。
        :type ExpiredTime: str
        :param IsAddressBlocked: 公網IP是否被封堵。
        :type IsAddressBlocked: bool
        :param NewPurchasePlan: 計費模式變更，PREPAID_TO_POSTPAID：包年包月預付費到期轉按小時後付費。
        :type NewPurchasePlan: str
        :param RestrictState: 閘道計費裝，PROTECTIVELY_ISOLATED：被安全隔離的實例，NORMAL：正常。
        :type RestrictState: str
        :param Zone: 可用區，如：ap-guangzhou-2
        :type Zone: str
        :param VpnGatewayQuotaSet: 閘道頻寬配額訊息
        :type VpnGatewayQuotaSet: list of VpnGatewayQuota
        :param Version: 閘道實例版本訊息
        :type Version: str
        :param NetworkInstanceId: Type值爲CCN時，該值表示雲聯網實例ID
        :type NetworkInstanceId: str
        """
        self.VpnGatewayId = None
        self.VpcId = None
        self.VpnGatewayName = None
        self.Type = None
        self.State = None
        self.PublicIpAddress = None
        self.RenewFlag = None
        self.InstanceChargeType = None
        self.InternetMaxBandwidthOut = None
        self.CreatedTime = None
        self.ExpiredTime = None
        self.IsAddressBlocked = None
        self.NewPurchasePlan = None
        self.RestrictState = None
        self.Zone = None
        self.VpnGatewayQuotaSet = None
        self.Version = None
        self.NetworkInstanceId = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.VpcId = params.get("VpcId")
        self.VpnGatewayName = params.get("VpnGatewayName")
        self.Type = params.get("Type")
        self.State = params.get("State")
        self.PublicIpAddress = params.get("PublicIpAddress")
        self.RenewFlag = params.get("RenewFlag")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.CreatedTime = params.get("CreatedTime")
        self.ExpiredTime = params.get("ExpiredTime")
        self.IsAddressBlocked = params.get("IsAddressBlocked")
        self.NewPurchasePlan = params.get("NewPurchasePlan")
        self.RestrictState = params.get("RestrictState")
        self.Zone = params.get("Zone")
        if params.get("VpnGatewayQuotaSet") is not None:
            self.VpnGatewayQuotaSet = []
            for item in params.get("VpnGatewayQuotaSet"):
                obj = VpnGatewayQuota()
                obj._deserialize(item)
                self.VpnGatewayQuotaSet.append(obj)
        self.Version = params.get("Version")
        self.NetworkInstanceId = params.get("NetworkInstanceId")


class VpnGatewayQuota(AbstractModel):
    """VPN閘道配額對象

    """

    def __init__(self):
        """
        :param Bandwidth: 頻寬配額
        :type Bandwidth: int
        :param Cname: 配額中文名稱
        :type Cname: str
        :param Name: 配額英文名稱
        :type Name: str
        """
        self.Bandwidth = None
        self.Cname = None
        self.Name = None


    def _deserialize(self, params):
        self.Bandwidth = params.get("Bandwidth")
        self.Cname = params.get("Cname")
        self.Name = params.get("Name")


class VpngwCcnRoutes(AbstractModel):
    """VPN閘道雲聯網路由訊息

    """

    def __init__(self):
        """
        :param RouteId: 路由訊息ID
        :type RouteId: str
        :param Status: 路由訊息是否啓用
ENABLE：啓用該路由
DISABLE：不啓用該路由
        :type Status: str
        """
        self.RouteId = None
        self.Status = None


    def _deserialize(self, params):
        self.RouteId = params.get("RouteId")
        self.Status = params.get("Status")