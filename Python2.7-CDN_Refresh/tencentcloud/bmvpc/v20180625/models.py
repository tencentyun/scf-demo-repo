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

from taifucloudcloud.common.abstract_model import AbstractModel


class AcceptVpcPeerConnectionRequest(AbstractModel):
    """AcceptVpcPeerConnection請求參數結構體

    """

    def __init__(self):
        """
        :param VpcPeerConnectionId: 黑石對等連接實例ID
        :type VpcPeerConnectionId: str
        """
        self.VpcPeerConnectionId = None


    def _deserialize(self, params):
        self.VpcPeerConnectionId = params.get("VpcPeerConnectionId")


class AcceptVpcPeerConnectionResponse(AbstractModel):
    """AcceptVpcPeerConnection返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class AsyncRegisterIpsRequest(AbstractModel):
    """AsyncRegisterIps請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: 私有網絡的唯一ID。
        :type VpcId: str
        :param SubnetId: 子網唯一ID。
        :type SubnetId: str
        :param Ips: 需要注冊的IP清單。
        :type Ips: list of str
        """
        self.VpcId = None
        self.SubnetId = None
        self.Ips = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Ips = params.get("Ips")


class AsyncRegisterIpsResponse(AbstractModel):
    """AsyncRegisterIps返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID。
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class BindEipsToNatGatewayRequest(AbstractModel):
    """BindEipsToNatGateway請求參數結構體

    """

    def __init__(self):
        """
        :param NatId: NAT閘道ID，例如：nat-kdm476mp
        :type NatId: str
        :param VpcId: 私有網絡ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param AssignedEips: 已分配的EIP清單；AssignedEips和AutoAllocEipNum至少輸入一個
        :type AssignedEips: list of str
        :param AutoAllocEipNum: 新建EIP數目，系統将會按您的要求生産該數目個數EIP；AssignedEips和AutoAllocEipNum至少輸入一個
        :type AutoAllocEipNum: int
        """
        self.NatId = None
        self.VpcId = None
        self.AssignedEips = None
        self.AutoAllocEipNum = None


    def _deserialize(self, params):
        self.NatId = params.get("NatId")
        self.VpcId = params.get("VpcId")
        self.AssignedEips = params.get("AssignedEips")
        self.AutoAllocEipNum = params.get("AutoAllocEipNum")


class BindEipsToNatGatewayResponse(AbstractModel):
    """BindEipsToNatGateway返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class BindIpsToNatGatewayRequest(AbstractModel):
    """BindIpsToNatGateway請求參數結構體

    """

    def __init__(self):
        """
        :param NatId: NAT閘道ID，例如：nat-kdm476mp
        :type NatId: str
        :param VpcId: 私有網絡ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param IpInfoSet: 部分IP訊息，子網下只有該部分IP将加入NAT，僅當閘道轉發模式爲IP方式有效
        :type IpInfoSet: list of IpInfo
        """
        self.NatId = None
        self.VpcId = None
        self.IpInfoSet = None


    def _deserialize(self, params):
        self.NatId = params.get("NatId")
        self.VpcId = params.get("VpcId")
        if params.get("IpInfoSet") is not None:
            self.IpInfoSet = []
            for item in params.get("IpInfoSet"):
                obj = IpInfo()
                obj._deserialize(item)
                self.IpInfoSet.append(obj)


class BindIpsToNatGatewayResponse(AbstractModel):
    """BindIpsToNatGateway返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class BindSubnetsToNatGatewayRequest(AbstractModel):
    """BindSubnetsToNatGateway請求參數結構體

    """

    def __init__(self):
        """
        :param NatId: NAT閘道ID，例如：nat-kdm476mp
        :type NatId: str
        :param VpcId: 私有網絡ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param SubnetIds: 子網ID清單，子網下全部IP将加入NAT，不區分閘道轉發方式
        :type SubnetIds: list of str
        """
        self.NatId = None
        self.VpcId = None
        self.SubnetIds = None


    def _deserialize(self, params):
        self.NatId = params.get("NatId")
        self.VpcId = params.get("VpcId")
        self.SubnetIds = params.get("SubnetIds")


class BindSubnetsToNatGatewayResponse(AbstractModel):
    """BindSubnetsToNatGateway返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
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
        :param Zone: 可用區ID
        :type Zone: str
        """
        self.CustomerGatewayName = None
        self.IpAddress = None
        self.Zone = None


    def _deserialize(self, params):
        self.CustomerGatewayName = params.get("CustomerGatewayName")
        self.IpAddress = params.get("IpAddress")
        self.Zone = params.get("Zone")


class CreateCustomerGatewayResponse(AbstractModel):
    """CreateCustomerGateway返回參數結構體

    """

    def __init__(self):
        """
        :param CustomerGateway: 對端閘道對象
        :type CustomerGateway: :class:`taifucloudcloud.bmvpc.v20180625.models.CustomerGateway`
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


class CreateDockerSubnetWithVlanRequest(AbstractModel):
    """CreateDockerSubnetWithVlan請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: 系統分配的私有網絡ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param SubnetSet: 子網訊息
        :type SubnetSet: list of SubnetCreateInputInfo
        """
        self.VpcId = None
        self.SubnetSet = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        if params.get("SubnetSet") is not None:
            self.SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = SubnetCreateInputInfo()
                obj._deserialize(item)
                self.SubnetSet.append(obj)


class CreateDockerSubnetWithVlanResponse(AbstractModel):
    """CreateDockerSubnetWithVlan返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateHostedInterfaceRequest(AbstractModel):
    """CreateHostedInterface請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 托管機器唯一ID 數組
        :type InstanceIds: list of str
        :param VpcId: 私有網絡ID或者私有網絡統一ID，建議使用統一ID
        :type VpcId: str
        :param SubnetId: 子網ID或者子網統一ID，建議使用統一ID
        :type SubnetId: str
        """
        self.InstanceIds = None
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")


class CreateHostedInterfaceResponse(AbstractModel):
    """CreateHostedInterface返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步任務ID
        :type TaskId: int
        :param ResourceIds: 黑石托管機器ID
        :type ResourceIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.ResourceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ResourceIds = params.get("ResourceIds")
        self.RequestId = params.get("RequestId")


class CreateInterfacesRequest(AbstractModel):
    """CreateInterfaces請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 物理機實例ID清單
        :type InstanceIds: list of str
        :param VpcId: 私有網絡ID
        :type VpcId: str
        :param SubnetId: 子網ID
        :type SubnetId: str
        """
        self.InstanceIds = None
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")


class CreateInterfacesResponse(AbstractModel):
    """CreateInterfaces返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateNatGatewayRequest(AbstractModel):
    """CreateNatGateway請求參數結構體

    """

    def __init__(self):
        """
        :param ForwardMode: 轉發模式，其中0表示IP方式，1表示網段方式；通過cidr方式可支援更多的IP接入到NAT閘道
        :type ForwardMode: str
        :param VpcId: 私有網絡ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param NatName: NAT名稱
        :type NatName: str
        :param MaxConcurrent: 并發連接數規格；取值爲1000000、3000000、10000000，分别對應小型、中型、大型NAT閘道
        :type MaxConcurrent: int
        :param SubnetIds: 子網ID清單，子網下全部IP将加入NAT，不區分閘道轉發方式
        :type SubnetIds: list of str
        :param IpInfoSet: 部分IP訊息，子網下只有該部分IP将加入NAT，僅當閘道轉發模式爲IP方式有效；IpInfoSet和SubnetIds中的子網ID不能同時存在
        :type IpInfoSet: list of IpInfo
        :param AssignedEips: 已分配的EIP清單, AssignedEips和AutoAllocEipNum至少輸入一個
        :type AssignedEips: list of str
        :param AutoAllocEipNum: 新建EIP數目，系統将會按您的要求生産該數目個數EIP, AssignedEips和AutoAllocEipNum至少輸入一個
        :type AutoAllocEipNum: int
        :param Exclusive: 獨占标識，取值爲0和1，預設值爲0；0和1分别表示創建共享型NAT閘道和獨占NAT型閘道；由于同一個VPC網絡内，指向NAT集群的預設路由只有一條，因此VPC内只能創建一種類型NAT閘道；創建獨占型NAT閘道時，需聯系對應架構師進行獨占NAT集群搭建，否則無法創建獨占型NAT閘道。
        :type Exclusive: int
        """
        self.ForwardMode = None
        self.VpcId = None
        self.NatName = None
        self.MaxConcurrent = None
        self.SubnetIds = None
        self.IpInfoSet = None
        self.AssignedEips = None
        self.AutoAllocEipNum = None
        self.Exclusive = None


    def _deserialize(self, params):
        self.ForwardMode = params.get("ForwardMode")
        self.VpcId = params.get("VpcId")
        self.NatName = params.get("NatName")
        self.MaxConcurrent = params.get("MaxConcurrent")
        self.SubnetIds = params.get("SubnetIds")
        if params.get("IpInfoSet") is not None:
            self.IpInfoSet = []
            for item in params.get("IpInfoSet"):
                obj = IpInfo()
                obj._deserialize(item)
                self.IpInfoSet.append(obj)
        self.AssignedEips = params.get("AssignedEips")
        self.AutoAllocEipNum = params.get("AutoAllocEipNum")
        self.Exclusive = params.get("Exclusive")


class CreateNatGatewayResponse(AbstractModel):
    """CreateNatGateway返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateRoutePoliciesRequest(AbstractModel):
    """CreateRoutePolicies請求參數結構體

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表ID
        :type RouteTableId: str
        :param RoutePolicySet: 新增的路由
        :type RoutePolicySet: list of RoutePolicy
        """
        self.RouteTableId = None
        self.RoutePolicySet = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        if params.get("RoutePolicySet") is not None:
            self.RoutePolicySet = []
            for item in params.get("RoutePolicySet"):
                obj = RoutePolicy()
                obj._deserialize(item)
                self.RoutePolicySet.append(obj)


class CreateRoutePoliciesResponse(AbstractModel):
    """CreateRoutePolicies返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateSubnetRequest(AbstractModel):
    """CreateSubnet請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: 系統分配的私有網絡ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param SubnetSet: 子網訊息
        :type SubnetSet: list of SubnetCreateInputInfo
        """
        self.VpcId = None
        self.SubnetSet = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        if params.get("SubnetSet") is not None:
            self.SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = SubnetCreateInputInfo()
                obj._deserialize(item)
                self.SubnetSet.append(obj)


class CreateSubnetResponse(AbstractModel):
    """CreateSubnet返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateVirtualSubnetWithVlanRequest(AbstractModel):
    """CreateVirtualSubnetWithVlan請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: 系統分配的私有網絡ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param SubnetSet: 子網訊息
        :type SubnetSet: list of SubnetCreateInputInfo
        """
        self.VpcId = None
        self.SubnetSet = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        if params.get("SubnetSet") is not None:
            self.SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = SubnetCreateInputInfo()
                obj._deserialize(item)
                self.SubnetSet.append(obj)


class CreateVirtualSubnetWithVlanResponse(AbstractModel):
    """CreateVirtualSubnetWithVlan返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateVpcPeerConnectionRequest(AbstractModel):
    """CreateVpcPeerConnection請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: 本端VPC唯一ID
        :type VpcId: str
        :param PeerVpcId: 對端VPC唯一ID
        :type PeerVpcId: str
        :param PeerRegion: 對端地域，取值範圍爲gz,sh,bj,hk,cd,de,sh_bm,gz_bm,bj_bm,cq_bm等
        :type PeerRegion: str
        :param VpcPeerConnectionName: 對等連接名稱
        :type VpcPeerConnectionName: str
        :param PeerUin: 對端帳戶OwnerUin（預設值爲本端帳戶）
        :type PeerUin: str
        :param Bandwidth: 跨地域必傳，頻寬上限值
        :type Bandwidth: int
        """
        self.VpcId = None
        self.PeerVpcId = None
        self.PeerRegion = None
        self.VpcPeerConnectionName = None
        self.PeerUin = None
        self.Bandwidth = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.PeerVpcId = params.get("PeerVpcId")
        self.PeerRegion = params.get("PeerRegion")
        self.VpcPeerConnectionName = params.get("VpcPeerConnectionName")
        self.PeerUin = params.get("PeerUin")
        self.Bandwidth = params.get("Bandwidth")


class CreateVpcPeerConnectionResponse(AbstractModel):
    """CreateVpcPeerConnection返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateVpcRequest(AbstractModel):
    """CreateVpc請求參數結構體

    """

    def __init__(self):
        """
        :param VpcName: 私有網絡的名稱
        :type VpcName: str
        :param CidrBlock: 私有網絡的CIDR
        :type CidrBlock: str
        :param Zone: 私有網絡的可用區
        :type Zone: str
        :param SubnetSet: 子網訊息
        :type SubnetSet: list of VpcSubnetCreateInfo
        :param EnableMonitoring: 是否啓用内網監控
        :type EnableMonitoring: bool
        """
        self.VpcName = None
        self.CidrBlock = None
        self.Zone = None
        self.SubnetSet = None
        self.EnableMonitoring = None


    def _deserialize(self, params):
        self.VpcName = params.get("VpcName")
        self.CidrBlock = params.get("CidrBlock")
        self.Zone = params.get("Zone")
        if params.get("SubnetSet") is not None:
            self.SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = VpcSubnetCreateInfo()
                obj._deserialize(item)
                self.SubnetSet.append(obj)
        self.EnableMonitoring = params.get("EnableMonitoring")


class CreateVpcResponse(AbstractModel):
    """CreateVpc返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
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
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param VpnConnNum: VPN通道引用個數
注意：此欄位可能返回 null，表示取不到有效值。
        :type VpnConnNum: int
        """
        self.CustomerGatewayId = None
        self.CustomerGatewayName = None
        self.IpAddress = None
        self.CreateTime = None
        self.VpnConnNum = None


    def _deserialize(self, params):
        self.CustomerGatewayId = params.get("CustomerGatewayId")
        self.CustomerGatewayName = params.get("CustomerGatewayName")
        self.IpAddress = params.get("IpAddress")
        self.CreateTime = params.get("CreateTime")
        self.VpnConnNum = params.get("VpnConnNum")


class DeleteCustomerGatewayRequest(AbstractModel):
    """DeleteCustomerGateway請求參數結構體

    """

    def __init__(self):
        """
        :param CustomerGatewayId: 對端閘道ID，例如：bmcgw-2wqq41m9，可通過DescribeCustomerGateways介面查詢對端閘道。
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


class DeleteHostedInterfaceRequest(AbstractModel):
    """DeleteHostedInterface請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 托管機器唯一ID 數組
        :type InstanceIds: list of str
        :param VpcId: 私有網絡ID或者私有網絡統一ID，建議使用統一ID
        :type VpcId: str
        :param SubnetId: 子網ID或者子網統一ID，建議使用統一ID
        :type SubnetId: str
        """
        self.InstanceIds = None
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")


class DeleteHostedInterfaceResponse(AbstractModel):
    """DeleteHostedInterface返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步任務ID
        :type TaskId: int
        :param ResourceIds: 黑石托管機器ID
        :type ResourceIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.ResourceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ResourceIds = params.get("ResourceIds")
        self.RequestId = params.get("RequestId")


class DeleteHostedInterfacesRequest(AbstractModel):
    """DeleteHostedInterfaces請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 物理機ID
        :type InstanceId: str
        :param SubnetIds: 物理機ID
        :type SubnetIds: list of str
        """
        self.InstanceId = None
        self.SubnetIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SubnetIds = params.get("SubnetIds")


class DeleteHostedInterfacesResponse(AbstractModel):
    """DeleteHostedInterfaces返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteInterfacesRequest(AbstractModel):
    """DeleteInterfaces請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 物理機ID
        :type InstanceId: str
        :param SubnetIds: 子網的唯一ID清單
        :type SubnetIds: list of str
        """
        self.InstanceId = None
        self.SubnetIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SubnetIds = params.get("SubnetIds")


class DeleteInterfacesResponse(AbstractModel):
    """DeleteInterfaces返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteNatGatewayRequest(AbstractModel):
    """DeleteNatGateway請求參數結構體

    """

    def __init__(self):
        """
        :param NatId: NAT閘道ID，例如：nat-kdm476mp
        :type NatId: str
        :param VpcId: 私有網絡ID，例如：vpc-kd7d06of
        :type VpcId: str
        """
        self.NatId = None
        self.VpcId = None


    def _deserialize(self, params):
        self.NatId = params.get("NatId")
        self.VpcId = params.get("VpcId")


class DeleteNatGatewayResponse(AbstractModel):
    """DeleteNatGateway返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteRoutePolicyRequest(AbstractModel):
    """DeleteRoutePolicy請求參數結構體

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表ID
        :type RouteTableId: str
        :param RoutePolicyId: 路由表策略ID
        :type RoutePolicyId: str
        """
        self.RouteTableId = None
        self.RoutePolicyId = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RoutePolicyId = params.get("RoutePolicyId")


class DeleteRoutePolicyResponse(AbstractModel):
    """DeleteRoutePolicy返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteSubnetRequest(AbstractModel):
    """DeleteSubnet請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: 私有網絡ID。可通過DescribeVpcs介面返回值中的VpcId獲取。
        :type VpcId: str
        :param SubnetId: 子網實例ID。可通過DescribeSubnets介面返回值中的SubnetId獲取。
        :type SubnetId: str
        """
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")


class DeleteSubnetResponse(AbstractModel):
    """DeleteSubnet返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步任務ID。
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteVirtualIpRequest(AbstractModel):
    """DeleteVirtualIp請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: 私有網絡唯一ID。
        :type VpcId: str
        :param Ips: 退還的IP清單。
        :type Ips: list of str
        """
        self.VpcId = None
        self.Ips = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.Ips = params.get("Ips")


class DeleteVirtualIpResponse(AbstractModel):
    """DeleteVirtualIp返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步任務ID。
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteVpcPeerConnectionRequest(AbstractModel):
    """DeleteVpcPeerConnection請求參數結構體

    """

    def __init__(self):
        """
        :param VpcPeerConnectionId: 黑石對等連接實例ID
        :type VpcPeerConnectionId: str
        """
        self.VpcPeerConnectionId = None


    def _deserialize(self, params):
        self.VpcPeerConnectionId = params.get("VpcPeerConnectionId")


class DeleteVpcPeerConnectionResponse(AbstractModel):
    """DeleteVpcPeerConnection返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
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
        :param TaskId: 異步任務ID。
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteVpnConnectionRequest(AbstractModel):
    """DeleteVpnConnection請求參數結構體

    """

    def __init__(self):
        """
        :param VpnConnectionId: VPN通道實例ID。形如：bmvpnx-f49l6u0z。
        :type VpnConnectionId: str
        """
        self.VpnConnectionId = None


    def _deserialize(self, params):
        self.VpnConnectionId = params.get("VpnConnectionId")


class DeleteVpnConnectionResponse(AbstractModel):
    """DeleteVpnConnection返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
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
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeregisterIpsRequest(AbstractModel):
    """DeregisterIps請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: 私有網絡ID
        :type VpcId: str
        :param IpSet: 注銷指定IP的清單
        :type IpSet: list of str
        :param SubnetId: 私有網絡子網ID
        :type SubnetId: str
        """
        self.VpcId = None
        self.IpSet = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.IpSet = params.get("IpSet")
        self.SubnetId = params.get("SubnetId")


class DeregisterIpsResponse(AbstractModel):
    """DeregisterIps返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeCustomerGatewaysRequest(AbstractModel):
    """DescribeCustomerGateways請求參數結構體

    """

    def __init__(self):
        """
        :param CustomerGatewayIds: 對端閘道ID，例如：bmcgw-2wqq41m9。每次請求的實例的上限爲100。參數不支援同時指定CustomerGatewayIds和Filters。
        :type CustomerGatewayIds: list of str
        :param Filters: 過濾條件，詳見下表：實例過濾條件表。每次請求的Filters的上限爲10，Filter.Values的上限爲5。參數不支援同時指定CustomerGatewayIds和Filters。
<li>customergateway-name - String - （過濾條件）對端閘道名稱。</li>
<li>ip-address - String - （過濾條件)對端閘道網址。</li>
<li>customergateway-id - String - （過濾條件）對端閘道唯一ID。</li>
<li>zone - String - （過濾條件）對端所在可用區，形如：ap-guangzhou-2。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。關于Offset的更進一步介紹請參考 API 簡介中的相關小節。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。
        :type Limit: int
        :param OrderField: 排序欄位, 支援"CreateTime"排序
        :type OrderField: str
        :param OrderDirection: 排序方向, “asc”、“desc”
        :type OrderDirection: str
        """
        self.CustomerGatewayIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.OrderDirection = None


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
        self.OrderField = params.get("OrderField")
        self.OrderDirection = params.get("OrderDirection")


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


class DescribeNatGatewaysRequest(AbstractModel):
    """DescribeNatGateways請求參數結構體

    """

    def __init__(self):
        """
        :param NatId: NAT閘道ID，例如：nat-kdm476mp
        :type NatId: str
        :param NatName: NAT名稱
        :type NatName: str
        :param SearchKey: 搜索欄位
        :type SearchKey: str
        :param VpcId: 私有網絡ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param Offset: 起始值
        :type Offset: int
        :param Limit: 偏移值，預設值爲 20
        :type Limit: int
        :param Zone: NAT所在可用區，形如：ap-guangzhou-2。
        :type Zone: str
        :param OrderField: 排序欄位, 支援"CreateTime"排序
        :type OrderField: str
        :param OrderDirection: 排序方向, “asc”、“desc”
        :type OrderDirection: str
        """
        self.NatId = None
        self.NatName = None
        self.SearchKey = None
        self.VpcId = None
        self.Offset = None
        self.Limit = None
        self.Zone = None
        self.OrderField = None
        self.OrderDirection = None


    def _deserialize(self, params):
        self.NatId = params.get("NatId")
        self.NatName = params.get("NatName")
        self.SearchKey = params.get("SearchKey")
        self.VpcId = params.get("VpcId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Zone = params.get("Zone")
        self.OrderField = params.get("OrderField")
        self.OrderDirection = params.get("OrderDirection")


class DescribeNatGatewaysResponse(AbstractModel):
    """DescribeNatGateways返回參數結構體

    """

    def __init__(self):
        """
        :param NatGatewayInfoSet: NAT閘道訊息清單
        :type NatGatewayInfoSet: list of NatGatewayInfo
        :param TotalCount: 總數目
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NatGatewayInfoSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NatGatewayInfoSet") is not None:
            self.NatGatewayInfoSet = []
            for item in params.get("NatGatewayInfoSet"):
                obj = NatGatewayInfo()
                obj._deserialize(item)
                self.NatGatewayInfoSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNatSubnetsRequest(AbstractModel):
    """DescribeNatSubnets請求參數結構體

    """

    def __init__(self):
        """
        :param NatId: NAT閘道ID，例如：nat-kdm476mp
        :type NatId: str
        :param VpcId: 私有網絡ID，例如：vpc-kd7d06of
        :type VpcId: str
        """
        self.NatId = None
        self.VpcId = None


    def _deserialize(self, params):
        self.NatId = params.get("NatId")
        self.VpcId = params.get("VpcId")


class DescribeNatSubnetsResponse(AbstractModel):
    """DescribeNatSubnets返回參數結構體

    """

    def __init__(self):
        """
        :param NatSubnetInfoSet: NAT子網訊息
        :type NatSubnetInfoSet: list of NatSubnetInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NatSubnetInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NatSubnetInfoSet") is not None:
            self.NatSubnetInfoSet = []
            for item in params.get("NatSubnetInfoSet"):
                obj = NatSubnetInfo()
                obj._deserialize(item)
                self.NatSubnetInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRoutePoliciesRequest(AbstractModel):
    """DescribeRoutePolicies請求參數結構體

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表實例ID，例如：rtb-afg8md3c。
        :type RouteTableId: str
        :param RoutePolicyIds: 路由策略實例ID，例如：rti-azd4dt1c。
        :type RoutePolicyIds: list of str
        :param Filters: 過濾條件，參數不支援同時指定RoutePolicyIds和Filters。
route-table-id - String - （過濾條件）路由表實例ID。
vpc-id - String - （過濾條件）VPC實例ID，形如：vpc-f49l6u0z。
route-policy-id - String - （過濾條件）路由策略ID。
route-policy-description-like - String -（過濾條件）路由項備注。
route-policy-type - String - （過濾條件）路由項策略類型。
destination-cidr-like - String - （過濾條件）路由項目的網址。
gateway-id-like - String - （過濾條件）路由項下一跳閘道。
gateway-type - String - （過濾條件）路由項下一條閘道類型。
enable - Bool - （過濾條件）路由策略是否啓用。
        :type Filters: list of Filter
        :param Offset: 初始行的偏移量，預設爲0。
        :type Offset: int
        :param Limit: 每頁行數，預設爲20。
        :type Limit: int
        """
        self.RouteTableId = None
        self.RoutePolicyIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RoutePolicyIds = params.get("RoutePolicyIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeRoutePoliciesResponse(AbstractModel):
    """DescribeRoutePolicies返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 路由策略數
        :type TotalCount: int
        :param RoutePolicySet: 路由策略清單
        :type RoutePolicySet: list of RoutePolicy
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RoutePolicySet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RoutePolicySet") is not None:
            self.RoutePolicySet = []
            for item in params.get("RoutePolicySet"):
                obj = RoutePolicy()
                obj._deserialize(item)
                self.RoutePolicySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRouteTablesRequest(AbstractModel):
    """DescribeRouteTables請求參數結構體

    """

    def __init__(self):
        """
        :param RouteTableIds: 路由表實例ID，例如：rtb-azd4dt1c。
        :type RouteTableIds: list of str
        :param Filters: 過濾條件，參數不支援同時指定RouteTableIds和Filters。
route-table-id - String - （過濾條件）路由表實例ID。
route-table-name - String - （過濾條件）路由表名稱。
route-table-id-like - String - （模糊過濾條件）路由表實例ID。
route-table-name-like - String - （模糊過濾條件）路由表名稱。
vpc-id - String - （過濾條件）VPC實例ID，形如：vpc-f49l6u0z。
zone - String - （過濾條件）可用區。
        :type Filters: list of Filter
        :param Offset: 初始行的偏移量，預設爲0。
        :type Offset: int
        :param Limit: 每頁行數，預設爲20。
        :type Limit: int
        :param OrderField: 排序欄位, 支援按“RouteTableId”，“VpcId”, "RouteTableName", "CreateTime"
        :type OrderField: str
        :param OrderDirection: 排序方向, “asc”、“desc”
        :type OrderDirection: str
        """
        self.RouteTableIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.OrderDirection = None


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
        self.OrderField = params.get("OrderField")
        self.OrderDirection = params.get("OrderDirection")


class DescribeRouteTablesResponse(AbstractModel):
    """DescribeRouteTables返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 路由表個數
        :type TotalCount: int
        :param RouteTableSet: 路由表清單
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


class DescribeSubnetAvailableIpsRequest(AbstractModel):
    """DescribeSubnetAvailableIps請求參數結構體

    """

    def __init__(self):
        """
        :param SubnetId: 私有網絡子網ID
        :type SubnetId: str
        :param Cidr: CIDR前綴，例如10.0.1
        :type Cidr: str
        """
        self.SubnetId = None
        self.Cidr = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.Cidr = params.get("Cidr")


class DescribeSubnetAvailableIpsResponse(AbstractModel):
    """DescribeSubnetAvailableIps返回參數結構體

    """

    def __init__(self):
        """
        :param IpSet: 可用IP的範圍清單
        :type IpSet: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.IpSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IpSet = params.get("IpSet")
        self.RequestId = params.get("RequestId")


class DescribeSubnetByDeviceRequest(AbstractModel):
    """DescribeSubnetByDevice請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 物理機ID
        :type InstanceId: str
        :param Types: 子網類型。0: 物理機子網; 7: DOCKER子網 8: 虛拟子網
        :type Types: list of int non-negative
        :param Offset: 查詢的起始位置。
        :type Offset: int
        :param Limit: 查詢的個數。
        :type Limit: int
        """
        self.InstanceId = None
        self.Types = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Types = params.get("Types")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeSubnetByDeviceResponse(AbstractModel):
    """DescribeSubnetByDevice返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 子網個數
        :type TotalCount: int
        :param Data: 子網清單
        :type Data: list of SubnetInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SubnetInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSubnetByHostedDeviceRequest(AbstractModel):
    """DescribeSubnetByHostedDevice請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 托管機器ID, 如chm-xasdfx2j
        :type InstanceId: str
        :param Types: 子網類型。0: 物理機子網; 7: DOCKER子網 8: 虛拟子網
        :type Types: list of int non-negative
        :param Offset: 查詢的起始位置。
        :type Offset: int
        :param Limit: 查詢的個數。
        :type Limit: int
        """
        self.InstanceId = None
        self.Types = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Types = params.get("Types")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeSubnetByHostedDeviceResponse(AbstractModel):
    """DescribeSubnetByHostedDevice返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 子網個數
        :type TotalCount: int
        :param Data: 子網清單
        :type Data: list of SubnetInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SubnetInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSubnetsRequest(AbstractModel):
    """DescribeSubnets請求參數結構體

    """

    def __init__(self):
        """
        :param SubnetIds: 子網實例ID查詢。形如：subnet-pxir56ns。參數不支援同時指定SubnetIds和Filters。
        :type SubnetIds: list of str
        :param Filters: 過濾條件，參數不支援同時指定SubnetIds和Filters。
subnet-id - String - （過濾條件）Subnet實例名稱。
vpc-id - String - （過濾條件）VPC實例ID，形如：vpc-f49l6u0z。
cidr-block - String - （過濾條件）vpc的cidr。
subnet-name - String - （過濾條件）子網名稱。
zone - String - （過濾條件）可用區。
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回數量
        :type Limit: int
        :param OrderField: 排序欄位, 支援按“CreateTime”，“VlanId”
        :type OrderField: str
        :param OrderDirection: 排序方向, “asc”、“desc”
        :type OrderDirection: str
        """
        self.SubnetIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.OrderDirection = None


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
        self.OrderField = params.get("OrderField")
        self.OrderDirection = params.get("OrderDirection")


class DescribeSubnetsResponse(AbstractModel):
    """DescribeSubnets返回參數結構體

    """

    def __init__(self):
        """
        :param SubnetSet: 子網清單訊息
        :type SubnetSet: list of SubnetInfo
        :param TotalCount: 返回的子網總數
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SubnetSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SubnetSet") is not None:
            self.SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = SubnetInfo()
                obj._deserialize(item)
                self.SubnetSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class DescribeTaskStatusResponse(AbstractModel):
    """DescribeTaskStatus返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 任務狀态，其中0表示任務執行成功，1表示任務執行失敗，2表示任務正在執行中
        :type Status: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeVpcPeerConnectionsRequest(AbstractModel):
    """DescribeVpcPeerConnections請求參數結構體

    """

    def __init__(self):
        """
        :param VpcPeerConnectionIds: 對等連接實例ID
        :type VpcPeerConnectionIds: list of str
        :param Filters: 過濾條件，詳見下表：實例過濾條件表。每次請求的Filters的上限爲10，Filter.Values的上限爲5。參數不支援同時指定VpcPeerConnectionIds和Filters。
過濾條件，參數不支援同時指定VpcPeerConnectionIds和Filters。
<li>peer-name - String - （過濾條件）對等連接名稱。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。關于Offset的更進一步介紹請參考 API 簡介中的相關小節。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。
        :type Limit: int
        :param VpcId: 私有網絡ID
        :type VpcId: str
        """
        self.VpcPeerConnectionIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.VpcId = None


    def _deserialize(self, params):
        self.VpcPeerConnectionIds = params.get("VpcPeerConnectionIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.VpcId = params.get("VpcId")


class DescribeVpcPeerConnectionsResponse(AbstractModel):
    """DescribeVpcPeerConnections返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的實例數量。
        :type TotalCount: int
        :param VpcPeerConnectionSet: 對等連接實例。
        :type VpcPeerConnectionSet: list of VpcPeerConnection
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.VpcPeerConnectionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VpcPeerConnectionSet") is not None:
            self.VpcPeerConnectionSet = []
            for item in params.get("VpcPeerConnectionSet"):
                obj = VpcPeerConnection()
                obj._deserialize(item)
                self.VpcPeerConnectionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVpcQuotaRequest(AbstractModel):
    """DescribeVpcQuota請求參數結構體

    """

    def __init__(self):
        """
        :param TypeIds: 類型
        :type TypeIds: list of int non-negative
        """
        self.TypeIds = None


    def _deserialize(self, params):
        self.TypeIds = params.get("TypeIds")


class DescribeVpcQuotaResponse(AbstractModel):
    """DescribeVpcQuota返回參數結構體

    """

    def __init__(self):
        """
        :param VpcQuotaSet: 配額訊息
        :type VpcQuotaSet: list of VpcQuota
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.VpcQuotaSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VpcQuotaSet") is not None:
            self.VpcQuotaSet = []
            for item in params.get("VpcQuotaSet"):
                obj = VpcQuota()
                obj._deserialize(item)
                self.VpcQuotaSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVpcResourceRequest(AbstractModel):
    """DescribeVpcResource請求參數結構體

    """

    def __init__(self):
        """
        :param VpcIds: 私有網絡實例ID
        :type VpcIds: list of str
        :param Filters: 過濾條件，參數不支援同時指定SubnetIds和Filters。
vpc-id - String - （過濾條件）私有網絡實例ID，形如：vpc-f49l6u0z。
vpc-name - String - （過濾條件）私有網絡名稱。
zone - String - （過濾條件）可用區。
state - String - （過濾條件）VPC狀态。available: 運營中; pending: 創建中; failed: 創建失敗; deleting: 删除中
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回數量
        :type Limit: int
        :param OrderField: 排序欄位
        :type OrderField: str
        :param OrderDirection: 排序方向, “asc”、“desc”
        :type OrderDirection: str
        """
        self.VpcIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.OrderDirection = None


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
        self.OrderField = params.get("OrderField")
        self.OrderDirection = params.get("OrderDirection")


class DescribeVpcResourceResponse(AbstractModel):
    """DescribeVpcResource返回參數結構體

    """

    def __init__(self):
        """
        :param VpcResourceSet: VPC數據
        :type VpcResourceSet: list of VpcResource
        :param TotalCount: VPC個數
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.VpcResourceSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VpcResourceSet") is not None:
            self.VpcResourceSet = []
            for item in params.get("VpcResourceSet"):
                obj = VpcResource()
                obj._deserialize(item)
                self.VpcResourceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeVpcViewRequest(AbstractModel):
    """DescribeVpcView請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: 私有網絡唯一ID
        :type VpcId: str
        """
        self.VpcId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")


class DescribeVpcViewResponse(AbstractModel):
    """DescribeVpcView返回參數結構體

    """

    def __init__(self):
        """
        :param VpcView: VPC視圖訊息
        :type VpcView: :class:`taifucloudcloud.bmvpc.v20180625.models.VpcViewInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.VpcView = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VpcView") is not None:
            self.VpcView = VpcViewInfo()
            self.VpcView._deserialize(params.get("VpcView"))
        self.RequestId = params.get("RequestId")


class DescribeVpcsRequest(AbstractModel):
    """DescribeVpcs請求參數結構體

    """

    def __init__(self):
        """
        :param VpcIds: VPC實例ID。形如：vpc-f49l6u0z。每次請求的實例的上限爲100。參數不支援同時指定VpcIds和Filters。
        :type VpcIds: list of str
        :param Filters: 過濾條件，參數不支援同時指定VpcIds和Filters。
vpc-name - String - （過濾條件）VPC實例名稱。
vpc-id - String - （過濾條件）VPC實例ID形如：vpc-f49l6u0z。
cidr-block - String - （過濾條件）vpc的cidr。
state - String - （過濾條件）VPC狀态。(pending | available).
zone -  String - （過濾條件）VPC的可用區。
        :type Filters: list of Filter
        :param Offset: 初始行的偏移量，預設爲0。
        :type Offset: int
        :param Limit: 每頁行數，預設爲20。
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


class DescribeVpcsResponse(AbstractModel):
    """DescribeVpcs返回參數結構體

    """

    def __init__(self):
        """
        :param VpcSet: VPC清單
        :type VpcSet: list of VpcInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.VpcSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VpcSet") is not None:
            self.VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self.VpcSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVpnConnectionsRequest(AbstractModel):
    """DescribeVpnConnections請求參數結構體

    """

    def __init__(self):
        """
        :param VpnConnectionIds: VPN通道實例ID。形如：bmvpnx-f49l6u0z。每次請求的實例的上限爲100。參數不支援同時指定VpnConnectionIds和Filters。
        :type VpnConnectionIds: list of str
        :param Filters: 過濾條件，詳見下表：實例過濾條件表。每次請求的Filters的上限爲10，Filter.Values的上限爲5。參數不支援同時指定VpnConnectionIds和Filters。
<li>vpc-id - String - （過濾條件）VPC實例ID形如：vpc-f49l6u0z。</li>
<li>state - String - （過濾條件 VPN狀态：creating，available，createfailed，changing，changefailed，deleting，deletefailed。</li>
<li>zone - String - （過濾條件）VPN所在可用區，形如：ap-guangzhou-2。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。關于Offset的更進一步介紹請參考 API 簡介中的相關小節。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。
        :type Limit: int
        :param VpnGatewayId: VPN閘道實例ID
        :type VpnGatewayId: str
        :param VpnConnectionName: VPN通道名稱
        :type VpnConnectionName: str
        :param OrderField: 排序欄位, 支援"CreateTime"排序
        :type OrderField: str
        :param OrderDirection: 排序方向, “asc”、“desc”
        :type OrderDirection: str
        """
        self.VpnConnectionIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.VpnGatewayId = None
        self.VpnConnectionName = None
        self.OrderField = None
        self.OrderDirection = None


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
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.VpnConnectionName = params.get("VpnConnectionName")
        self.OrderField = params.get("OrderField")
        self.OrderDirection = params.get("OrderDirection")


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


class DescribeVpnGatewaysRequest(AbstractModel):
    """DescribeVpnGateways請求參數結構體

    """

    def __init__(self):
        """
        :param VpnGatewayIds: VPN閘道實例ID。形如：bmvpngw-f49l6u0z。每次請求的實例的上限爲100。參數不支援同時指定VpnGatewayIds和Filters。
        :type VpnGatewayIds: list of str
        :param Filters: 過濾條件，參數不支援同時指定VpnGatewayIds和Filters。
<li>vpc-id - String - （過濾條件）VPC實例ID形如：vpc-f49l6u0z。</li>
<li>state - String - （過濾條件 VPN狀态：creating，available，createfailed，changing，changefailed，deleting，deletefailed。</li>
<li>zone - String - （過濾條件）VPN所在可用區，形如：ap-guangzhou-2。</li>
<li>vpngw-name - String - （過濾條件）vpn閘道名稱。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 請求對象個數
        :type Limit: int
        :param OrderField: 排序欄位, 支援"CreateTime"排序
        :type OrderField: str
        :param OrderDirection: 排序方向, “asc”、“desc”
        :type OrderDirection: str
        """
        self.VpnGatewayIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.OrderDirection = None


    def _deserialize(self, params):
        self.VpnGatewayIds = params.get("VpnGatewayIds")
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


class DownloadCustomerGatewayConfigurationRequest(AbstractModel):
    """DownloadCustomerGatewayConfiguration請求參數結構體

    """

    def __init__(self):
        """
        :param VpnConnectionId: VPN通道實例ID。形如：bmvpnx-f49l6u0z。
        :type VpnConnectionId: str
        :param VendorName: 廠商,取值 h3c，cisco
        :type VendorName: str
        """
        self.VpnConnectionId = None
        self.VendorName = None


    def _deserialize(self, params):
        self.VpnConnectionId = params.get("VpnConnectionId")
        self.VendorName = params.get("VendorName")


class DownloadCustomerGatewayConfigurationResponse(AbstractModel):
    """DownloadCustomerGatewayConfiguration返回參數結構體

    """

    def __init__(self):
        """
        :param CustomerGatewayConfiguration: 配置訊息。
        :type CustomerGatewayConfiguration: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CustomerGatewayConfiguration = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CustomerGatewayConfiguration = params.get("CustomerGatewayConfiguration")
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


class IKEOptionsSpecification(AbstractModel):
    """IKE配置（Internet Key Exchange，因特網金鑰交換），IKE具有一套自我保護機制，用戶配置網絡安全協議

    """

    def __init__(self):
        """
        :param PropoEncryAlgorithm: 加密算法，可選值：'3DES-CBC', 'AES-CBC-128', 'AES-CBC-192', 'AES-CBC-256', 'DES-CBC'，預設爲3DES-CBC
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
        :param PfsDhGroup: PFS：可選值：'NULL', 'DH-GROUP1', 'DH-GROUP2', 'DH-GROUP5', 'DH-GROUP14', 'DH-GROUP24'，預設爲NULL
        :type PfsDhGroup: str
        :param IPSECSaLifetimeTraffic: IPsec SA lifetime(KB)：單位KB，取值範圍：2560-604800
        :type IPSECSaLifetimeTraffic: int
        :param EncryptAlgorithm: 加密算法，可選值：'3DES-CBC', 'AES-CBC-128', 'AES-CBC-192', 'AES-CBC-256', 'DES-CBC', 'NULL'， 預設爲AES-CBC-128
        :type EncryptAlgorithm: str
        :param IntegrityAlgorith: 認證算法：可選值：'MD5', 'SHA1'，預設爲
        :type IntegrityAlgorith: str
        :param IPSECSaLifetimeSeconds: IPsec SA lifetime(s)：單位秒，取值範圍：180-604800
        :type IPSECSaLifetimeSeconds: int
        :param SecurityProto: 安全協議，預設爲ESP
        :type SecurityProto: str
        :param EncapMode: 報文封裝模式:預設爲Tunnel
        :type EncapMode: str
        """
        self.PfsDhGroup = None
        self.IPSECSaLifetimeTraffic = None
        self.EncryptAlgorithm = None
        self.IntegrityAlgorith = None
        self.IPSECSaLifetimeSeconds = None
        self.SecurityProto = None
        self.EncapMode = None


    def _deserialize(self, params):
        self.PfsDhGroup = params.get("PfsDhGroup")
        self.IPSECSaLifetimeTraffic = params.get("IPSECSaLifetimeTraffic")
        self.EncryptAlgorithm = params.get("EncryptAlgorithm")
        self.IntegrityAlgorith = params.get("IntegrityAlgorith")
        self.IPSECSaLifetimeSeconds = params.get("IPSECSaLifetimeSeconds")
        self.SecurityProto = params.get("SecurityProto")
        self.EncapMode = params.get("EncapMode")


class IpInfo(AbstractModel):
    """NAT IP訊息

    """

    def __init__(self):
        """
        :param SubnetId: 子網ID
        :type SubnetId: str
        :param Ips: IP清單
        :type Ips: list of str
        """
        self.SubnetId = None
        self.Ips = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.Ips = params.get("Ips")


class ModifyCustomerGatewayAttributeRequest(AbstractModel):
    """ModifyCustomerGatewayAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param CustomerGatewayId: 對端閘道ID，例如：bmcgw-2wqq41m9，可通過DescribeCustomerGateways介面查詢對端閘道。
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


class ModifyRoutePolicyRequest(AbstractModel):
    """ModifyRoutePolicy請求參數結構體

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表ID
        :type RouteTableId: str
        :param RoutePolicy: 修改的路由
        :type RoutePolicy: :class:`taifucloudcloud.bmvpc.v20180625.models.RoutePolicy`
        """
        self.RouteTableId = None
        self.RoutePolicy = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        if params.get("RoutePolicy") is not None:
            self.RoutePolicy = RoutePolicy()
            self.RoutePolicy._deserialize(params.get("RoutePolicy"))


class ModifyRoutePolicyResponse(AbstractModel):
    """ModifyRoutePolicy返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyRouteTableRequest(AbstractModel):
    """ModifyRouteTable請求參數結構體

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表ID
        :type RouteTableId: str
        :param RouteTableName: 路由表名稱
        :type RouteTableName: str
        """
        self.RouteTableId = None
        self.RouteTableName = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RouteTableName = params.get("RouteTableName")


class ModifyRouteTableResponse(AbstractModel):
    """ModifyRouteTable返回參數結構體

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
        :param VpcId: 私有網絡ID
        :type VpcId: str
        :param SubnetId: 子網ID
        :type SubnetId: str
        :param SubnetName: 子網名稱
        :type SubnetName: str
        """
        self.VpcId = None
        self.SubnetId = None
        self.SubnetName = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")


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


class ModifySubnetDHCPRelayRequest(AbstractModel):
    """ModifySubnetDHCPRelay請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: 私有網絡ID
        :type VpcId: str
        :param SubnetId: 子網ID
        :type SubnetId: str
        :param EnableDHCP: 是否開啓DHCP Relay
        :type EnableDHCP: bool
        :param ServerIps: DHCP服務器IP
        :type ServerIps: list of str
        :param ReservedIpCount: 預留IP個數
        :type ReservedIpCount: int
        """
        self.VpcId = None
        self.SubnetId = None
        self.EnableDHCP = None
        self.ServerIps = None
        self.ReservedIpCount = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.EnableDHCP = params.get("EnableDHCP")
        self.ServerIps = params.get("ServerIps")
        self.ReservedIpCount = params.get("ReservedIpCount")


class ModifySubnetDHCPRelayResponse(AbstractModel):
    """ModifySubnetDHCPRelay返回參數結構體

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
        :param VpcId: 私有網絡ID
        :type VpcId: str
        :param VpcName: 私有網絡名稱
        :type VpcName: str
        :param EnableMonitor: 是否開啓内網監控，0爲關閉，1爲開啓
        :type EnableMonitor: bool
        """
        self.VpcId = None
        self.VpcName = None
        self.EnableMonitor = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.EnableMonitor = params.get("EnableMonitor")


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


class ModifyVpcPeerConnectionRequest(AbstractModel):
    """ModifyVpcPeerConnection請求參數結構體

    """

    def __init__(self):
        """
        :param VpcPeerConnectionId: 黑石對等連接唯一ID
        :type VpcPeerConnectionId: str
        :param Bandwidth: 對等連接頻寬
        :type Bandwidth: int
        :param VpcPeerConnectionName: 對等連接名稱
        :type VpcPeerConnectionName: str
        """
        self.VpcPeerConnectionId = None
        self.Bandwidth = None
        self.VpcPeerConnectionName = None


    def _deserialize(self, params):
        self.VpcPeerConnectionId = params.get("VpcPeerConnectionId")
        self.Bandwidth = params.get("Bandwidth")
        self.VpcPeerConnectionName = params.get("VpcPeerConnectionName")


class ModifyVpcPeerConnectionResponse(AbstractModel):
    """ModifyVpcPeerConnection返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyVpnConnectionAttributeRequest(AbstractModel):
    """ModifyVpnConnectionAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param VpnConnectionId: VPN通道實例ID。形如：bmvpnx-f49l6u0z。
        :type VpnConnectionId: str
        :param VpcId: VPC實例ID
        :type VpcId: str
        :param VpnConnectionName: VPN通道名稱，可任意命名，但不得超過60個字元。
        :type VpnConnectionName: str
        :param PreShareKey: 預共享金鑰。
        :type PreShareKey: str
        :param SecurityPolicyDatabases: SPD策略組，例如：{"10.0.0.5/24":["172.123.10.5/16"]}，10.0.0.5/24是vpc内網段172.123.10.5/16是IDC網段。用戶指定VPC内哪些網段可以和您IDC中哪些網段通信。
        :type SecurityPolicyDatabases: list of SecurityPolicyDatabase
        :param IKEOptionsSpecification: IKE配置（Internet Key Exchange，因特網金鑰交換），IKE具有一套自我保護機制，用戶配置網絡安全協議。
        :type IKEOptionsSpecification: :class:`taifucloudcloud.bmvpc.v20180625.models.IKEOptionsSpecification`
        :param IPSECOptionsSpecification: IPSec配置，Top Cloud 提供IPSec安全會話設置。
        :type IPSECOptionsSpecification: :class:`taifucloudcloud.bmvpc.v20180625.models.IPSECOptionsSpecification`
        """
        self.VpnConnectionId = None
        self.VpcId = None
        self.VpnConnectionName = None
        self.PreShareKey = None
        self.SecurityPolicyDatabases = None
        self.IKEOptionsSpecification = None
        self.IPSECOptionsSpecification = None


    def _deserialize(self, params):
        self.VpnConnectionId = params.get("VpnConnectionId")
        self.VpcId = params.get("VpcId")
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
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
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
        """
        self.VpnGatewayId = None
        self.VpnGatewayName = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.VpnGatewayName = params.get("VpnGatewayName")


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


class NatGatewayInfo(AbstractModel):
    """NAT詳情

    """

    def __init__(self):
        """
        :param NatId: NAT閘道ID
        :type NatId: str
        :param NatName: 閘道名稱
        :type NatName: str
        :param VpcId: 私有網絡ID
        :type VpcId: str
        :param VpcName: 私有網絡名稱
        :type VpcName: str
        :param ProductionStatus: 閘道創建狀态，其中0表示創建中，1表示運作中，2表示創建失敗
        :type ProductionStatus: int
        :param Eips: EIP清單
        :type Eips: list of str
        :param MaxConcurrent: 并發連接數規格，取值爲1000000, 3000000, 10000000
        :type MaxConcurrent: int
        :param Zone: 可用區
        :type Zone: str
        :param Exclusive: 獨占标識，其中0表示共享，1表示獨占，預設值爲0
        :type Exclusive: int
        :param ForwardMode: 轉發模式，其中0表示IP方式，1表示網段方式
        :type ForwardMode: int
        :param VpcCidrBlock: 私有網絡網段
        :type VpcCidrBlock: str
        :param Type: 閘道類型，取值爲 small，middle，big，分别對應小型、中型、大型
        :type Type: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param State: 閘道啓用狀态，1爲禁用，0爲啓用。
        :type State: int
        :param IntVpcId: 私有網絡整型ID
        :type IntVpcId: int
        :param NatResourceId: NAT資源ID
        :type NatResourceId: int
        """
        self.NatId = None
        self.NatName = None
        self.VpcId = None
        self.VpcName = None
        self.ProductionStatus = None
        self.Eips = None
        self.MaxConcurrent = None
        self.Zone = None
        self.Exclusive = None
        self.ForwardMode = None
        self.VpcCidrBlock = None
        self.Type = None
        self.CreateTime = None
        self.State = None
        self.IntVpcId = None
        self.NatResourceId = None


    def _deserialize(self, params):
        self.NatId = params.get("NatId")
        self.NatName = params.get("NatName")
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.ProductionStatus = params.get("ProductionStatus")
        self.Eips = params.get("Eips")
        self.MaxConcurrent = params.get("MaxConcurrent")
        self.Zone = params.get("Zone")
        self.Exclusive = params.get("Exclusive")
        self.ForwardMode = params.get("ForwardMode")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.Type = params.get("Type")
        self.CreateTime = params.get("CreateTime")
        self.State = params.get("State")
        self.IntVpcId = params.get("IntVpcId")
        self.NatResourceId = params.get("NatResourceId")


class NatSubnetInfo(AbstractModel):
    """NAT子網訊息

    """

    def __init__(self):
        """
        :param Name: 子網名稱
        :type Name: str
        :param SubnetId: 子網ID
        :type SubnetId: str
        :param SubnetNatType: NAT子網類型，其中0表示綁定部分IP的NAT子網，1表示綁定全部IP的NAT子網，2表示綁定閘道方式的NAT子網
        :type SubnetNatType: int
        :param CidrBlock: 子網網段
        :type CidrBlock: str
        """
        self.Name = None
        self.SubnetId = None
        self.SubnetNatType = None
        self.CidrBlock = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.SubnetId = params.get("SubnetId")
        self.SubnetNatType = params.get("SubnetNatType")
        self.CidrBlock = params.get("CidrBlock")


class RejectVpcPeerConnectionRequest(AbstractModel):
    """RejectVpcPeerConnection請求參數結構體

    """

    def __init__(self):
        """
        :param VpcPeerConnectionId: 黑石對等連接實例ID
        :type VpcPeerConnectionId: str
        """
        self.VpcPeerConnectionId = None


    def _deserialize(self, params):
        self.VpcPeerConnectionId = params.get("VpcPeerConnectionId")


class RejectVpcPeerConnectionResponse(AbstractModel):
    """RejectVpcPeerConnection返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ResetVpnConnectionRequest(AbstractModel):
    """ResetVpnConnection請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: VPC唯一ID
        :type VpcId: str
        :param VpnConnectionId: VPN通道實例ID。形如：bmvpnx-f49l6u0z。
        :type VpnConnectionId: str
        """
        self.VpcId = None
        self.VpnConnectionId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
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


class RoutePolicy(AbstractModel):
    """路由條目

    """

    def __init__(self):
        """
        :param DestinationCidrBlock: 目的網段
        :type DestinationCidrBlock: str
        :param GatewayType: 下一跳類型，目前我們支援的類型有：
LOCAL：物理機預設路由；
VPN：VPN閘道；
PEERCONNECTION：對等連接；
CPM：物理機自定義路由；
CCN：雲聯網；
TGW：公網預設路由；
SSLVPN : SSH SSL VPN閘道。
        :type GatewayType: str
        :param GatewayId: 下一跳網址，這裏只需要指定不同下一跳類型的閘道ID，系統會自動比對到下一跳網址。
        :type GatewayId: str
        :param RouteDescription: 路由策略描述。
        :type RouteDescription: str
        :param RoutePolicyId: 路由策略ID
        :type RoutePolicyId: str
        :param RoutePolicyType: 路由類型，目前我們支援的類型有：
USER：用戶自定義路由；
NETD：網絡探測路由，創建網絡探測實例時，系統預設下發，不可編輯與删除；
CCN：雲聯網路由，系統預設下發，不可編輯與删除。
用戶只能添加和編輯USER 類型的路由。
        :type RoutePolicyType: str
        :param Enabled: 是否啓用
        :type Enabled: bool
        """
        self.DestinationCidrBlock = None
        self.GatewayType = None
        self.GatewayId = None
        self.RouteDescription = None
        self.RoutePolicyId = None
        self.RoutePolicyType = None
        self.Enabled = None


    def _deserialize(self, params):
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        self.GatewayType = params.get("GatewayType")
        self.GatewayId = params.get("GatewayId")
        self.RouteDescription = params.get("RouteDescription")
        self.RoutePolicyId = params.get("RoutePolicyId")
        self.RoutePolicyType = params.get("RoutePolicyType")
        self.Enabled = params.get("Enabled")


class RouteTable(AbstractModel):
    """路由表對象

    """

    def __init__(self):
        """
        :param VpcId: VPC實例ID。
        :type VpcId: str
        :param VpcName: VPC的名稱
        :type VpcName: str
        :param VpcCidrBlock: VPC的CIDR
        :type VpcCidrBlock: str
        :param Zone: 可用區
        :type Zone: str
        :param RouteTableId: 路由表實例ID，例如：rtb-azd4dt1c。
        :type RouteTableId: str
        :param RouteTableName: 路由表名稱。
        :type RouteTableName: str
        :param CreateTime: 創建時間。
        :type CreateTime: str
        """
        self.VpcId = None
        self.VpcName = None
        self.VpcCidrBlock = None
        self.Zone = None
        self.RouteTableId = None
        self.RouteTableName = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.Zone = params.get("Zone")
        self.RouteTableId = params.get("RouteTableId")
        self.RouteTableName = params.get("RouteTableName")
        self.CreateTime = params.get("CreateTime")


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


class SubnetCreateInputInfo(AbstractModel):
    """創建子網時的子網類型

    """

    def __init__(self):
        """
        :param SubnetName: 子網名稱，可任意命名，但不得超過60個字元
        :type SubnetName: str
        :param CidrBlock: 子網網段，子網網段必須在VPC網段内，相同VPC内子網網段不能重疊
        :type CidrBlock: str
        :param DistributedFlag: 是否開啓子網分布式閘道，預設傳1，傳0爲關閉子網分布式閘道。關閉分布式閘道子網用于雲伺服器化子網，此子網中只能有一台物理機，同時此物理機及其上子機只能在此子網中
        :type DistributedFlag: int
        :param DhcpEnable: 是否開啓dhcp relay ，關閉爲0，開啓爲1。預設爲0
        :type DhcpEnable: int
        :param DhcpServerIp: DHCP SERVER 的IP網址數組。IP網址爲相同VPC的子網内分配的IP
        :type DhcpServerIp: list of str
        :param IpReserve: 預留的IP個數。從該子網的最大可分配IP倒序分配N個IP 用于DHCP 動态分配使用的網址段
        :type IpReserve: int
        :param VlanId: 子網綁定的vlanId。VlanId取值範圍爲2000-2999。創建物理機子網，VlanId預設爲5; 創建docker子網或者虛拟子網，VlanId預設會分配2000--2999未使用的數值。
        :type VlanId: int
        :param Zone: 黑石子網的可用區
        :type Zone: str
        :param IsSmartNic: 是否25G子網，1爲是，0爲否。
        :type IsSmartNic: int
        """
        self.SubnetName = None
        self.CidrBlock = None
        self.DistributedFlag = None
        self.DhcpEnable = None
        self.DhcpServerIp = None
        self.IpReserve = None
        self.VlanId = None
        self.Zone = None
        self.IsSmartNic = None


    def _deserialize(self, params):
        self.SubnetName = params.get("SubnetName")
        self.CidrBlock = params.get("CidrBlock")
        self.DistributedFlag = params.get("DistributedFlag")
        self.DhcpEnable = params.get("DhcpEnable")
        self.DhcpServerIp = params.get("DhcpServerIp")
        self.IpReserve = params.get("IpReserve")
        self.VlanId = params.get("VlanId")
        self.Zone = params.get("Zone")
        self.IsSmartNic = params.get("IsSmartNic")


class SubnetInfo(AbstractModel):
    """黑石子網的訊息

    """

    def __init__(self):
        """
        :param VpcId: 私有網絡的唯一ID。
        :type VpcId: str
        :param VpcName: VPC的名稱。
        :type VpcName: str
        :param VpcCidrBlock: VPC的CIDR。
        :type VpcCidrBlock: str
        :param SubnetId: 私有網絡的唯一ID
        :type SubnetId: str
        :param SubnetName: 子網名稱。
        :type SubnetName: str
        :param CidrBlock: 子網CIDR。
        :type CidrBlock: str
        :param Type: 子網類型。0: 黑石物理機子網; 6: ccs子網; 7 Docker子網; 8: 虛拟機子網
        :type Type: int
        :param ZoneId: 子網可用區ID。
        :type ZoneId: int
        :param CpmNum: 子網物理機的個數
        :type CpmNum: int
        :param VlanId: 子網的VlanId。
        :type VlanId: int
        :param DistributedFlag: 是否開啓分布式閘道 ，關閉爲0，開啓爲1。
        :type DistributedFlag: int
        :param DhcpEnable: 是否開啓dhcp relay ，關閉爲0，開啓爲1。預設爲0。
        :type DhcpEnable: int
        :param DhcpServerIp: DHCP SERVER 的IP網址數組。IP網址爲相同VPC的子網内分配的IP。
        :type DhcpServerIp: list of str
        :param IpReserve: 預留的IP個數。從該子網的最大可分配IP倒序分配N個IP 用于DHCP 動态分配使用的網址段。
        :type IpReserve: int
        :param AvailableIpNum: 子網中可用的IP個數
        :type AvailableIpNum: int
        :param TotalIpNum: 子網中總共的IP個數
        :type TotalIpNum: int
        :param SubnetCreateTime: 子網創建時間
        :type SubnetCreateTime: str
        :param IsSmartNic: 25G子網标識
        :type IsSmartNic: int
        :param Zone: 子網可用區。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Zone: str
        :param VpcZoneId: VPC所在可用區ID
        :type VpcZoneId: int
        :param VpcZone: VPC所在可用區
        :type VpcZone: str
        :param BroadcastFlag: 是否開啓廣播，關閉爲0，開啓爲1。
        :type BroadcastFlag: int
        """
        self.VpcId = None
        self.VpcName = None
        self.VpcCidrBlock = None
        self.SubnetId = None
        self.SubnetName = None
        self.CidrBlock = None
        self.Type = None
        self.ZoneId = None
        self.CpmNum = None
        self.VlanId = None
        self.DistributedFlag = None
        self.DhcpEnable = None
        self.DhcpServerIp = None
        self.IpReserve = None
        self.AvailableIpNum = None
        self.TotalIpNum = None
        self.SubnetCreateTime = None
        self.IsSmartNic = None
        self.Zone = None
        self.VpcZoneId = None
        self.VpcZone = None
        self.BroadcastFlag = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.CidrBlock = params.get("CidrBlock")
        self.Type = params.get("Type")
        self.ZoneId = params.get("ZoneId")
        self.CpmNum = params.get("CpmNum")
        self.VlanId = params.get("VlanId")
        self.DistributedFlag = params.get("DistributedFlag")
        self.DhcpEnable = params.get("DhcpEnable")
        self.DhcpServerIp = params.get("DhcpServerIp")
        self.IpReserve = params.get("IpReserve")
        self.AvailableIpNum = params.get("AvailableIpNum")
        self.TotalIpNum = params.get("TotalIpNum")
        self.SubnetCreateTime = params.get("SubnetCreateTime")
        self.IsSmartNic = params.get("IsSmartNic")
        self.Zone = params.get("Zone")
        self.VpcZoneId = params.get("VpcZoneId")
        self.VpcZone = params.get("VpcZone")
        self.BroadcastFlag = params.get("BroadcastFlag")


class UnbindEipsFromNatGatewayRequest(AbstractModel):
    """UnbindEipsFromNatGateway請求參數結構體

    """

    def __init__(self):
        """
        :param NatId: NAT閘道ID，例如：nat-kdm476mp
        :type NatId: str
        :param VpcId: 私有網絡ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param AssignedEips: 已分配的EIP清單
        :type AssignedEips: list of str
        """
        self.NatId = None
        self.VpcId = None
        self.AssignedEips = None


    def _deserialize(self, params):
        self.NatId = params.get("NatId")
        self.VpcId = params.get("VpcId")
        self.AssignedEips = params.get("AssignedEips")


class UnbindEipsFromNatGatewayResponse(AbstractModel):
    """UnbindEipsFromNatGateway返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class UnbindIpsFromNatGatewayRequest(AbstractModel):
    """UnbindIpsFromNatGateway請求參數結構體

    """

    def __init__(self):
        """
        :param NatId: NAT閘道ID，例如：nat-kdm476mp
        :type NatId: str
        :param VpcId: 私有網絡ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param IpInfoSet: 部分IP訊息；子網須以部分IP将加入NAT閘道
        :type IpInfoSet: list of IpInfo
        """
        self.NatId = None
        self.VpcId = None
        self.IpInfoSet = None


    def _deserialize(self, params):
        self.NatId = params.get("NatId")
        self.VpcId = params.get("VpcId")
        if params.get("IpInfoSet") is not None:
            self.IpInfoSet = []
            for item in params.get("IpInfoSet"):
                obj = IpInfo()
                obj._deserialize(item)
                self.IpInfoSet.append(obj)


class UnbindIpsFromNatGatewayResponse(AbstractModel):
    """UnbindIpsFromNatGateway返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class UnbindSubnetsFromNatGatewayRequest(AbstractModel):
    """UnbindSubnetsFromNatGateway請求參數結構體

    """

    def __init__(self):
        """
        :param NatId: NAT閘道ID，例如：nat-kdm476mp
        :type NatId: str
        :param VpcId: 私有網絡ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param SubnetIds: 子網ID清單，子網不區分加入NAT閘道的轉發方式
        :type SubnetIds: list of str
        """
        self.NatId = None
        self.VpcId = None
        self.SubnetIds = None


    def _deserialize(self, params):
        self.NatId = params.get("NatId")
        self.VpcId = params.get("VpcId")
        self.SubnetIds = params.get("SubnetIds")


class UnbindSubnetsFromNatGatewayResponse(AbstractModel):
    """UnbindSubnetsFromNatGateway返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class UpgradeNatGatewayRequest(AbstractModel):
    """UpgradeNatGateway請求參數結構體

    """

    def __init__(self):
        """
        :param NatId: NAT閘道ID，例如：nat-kdm476mp
        :type NatId: str
        :param VpcId: 私有網絡ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param MaxConcurrent: 并發連接數規格；取值爲1000000、3000000、10000000，分别對應小型、中型、大型NAT閘道
        :type MaxConcurrent: int
        """
        self.NatId = None
        self.VpcId = None
        self.MaxConcurrent = None


    def _deserialize(self, params):
        self.NatId = params.get("NatId")
        self.VpcId = params.get("VpcId")
        self.MaxConcurrent = params.get("MaxConcurrent")


class UpgradeNatGatewayResponse(AbstractModel):
    """UpgradeNatGateway返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class VpcInfo(AbstractModel):
    """VPC訊息

    """

    def __init__(self):
        """
        :param VpcId: 私有網絡的唯一ID。
        :type VpcId: str
        :param VpcName: VPC的名稱。
        :type VpcName: str
        :param CidrBlock: VPC的CIDR。
        :type CidrBlock: str
        :param Zone: 可用區
        :type Zone: str
        :param State: VPC狀态
        :type State: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param IntVpcId: 整型私有網絡ID。
        :type IntVpcId: int
        """
        self.VpcId = None
        self.VpcName = None
        self.CidrBlock = None
        self.Zone = None
        self.State = None
        self.CreateTime = None
        self.IntVpcId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.CidrBlock = params.get("CidrBlock")
        self.Zone = params.get("Zone")
        self.State = params.get("State")
        self.CreateTime = params.get("CreateTime")
        self.IntVpcId = params.get("IntVpcId")


class VpcPeerConnection(AbstractModel):
    """對等連接對象

    """

    def __init__(self):
        """
        :param VpcId: 本端VPC唯一ID
        :type VpcId: str
        :param PeerVpcId: 對端VPC唯一ID
        :type PeerVpcId: str
        :param AppId: 本端APPID
        :type AppId: str
        :param PeerAppId: 對端APPID
        :type PeerAppId: str
        :param VpcPeerConnectionId: 對等連接唯一ID
        :type VpcPeerConnectionId: str
        :param VpcPeerConnectionName: 對等連接名稱
        :type VpcPeerConnectionName: str
        :param State: 對等連接狀态。pending:申請中,available:運作中,expired:已過期,rejected:已拒絕,deleted:已删除
        :type State: str
        :param VpcZone: 本端VPC所屬可用區
注意：此欄位可能返回 null，表示取不到有效值。
        :type VpcZone: str
        :param PeerVpcZone: 對端VPC所屬可用區
注意：此欄位可能返回 null，表示取不到有效值。
        :type PeerVpcZone: str
        :param Uin: 本端Uin
        :type Uin: int
        :param PeerUin: 對端Uin
        :type PeerUin: int
        :param PeerType: 對等連接類型
        :type PeerType: int
        :param Bandwidth: 對等連接頻寬
        :type Bandwidth: int
        :param Region: 本端VPC地域
        :type Region: str
        :param PeerRegion: 對端VPC地域
        :type PeerRegion: str
        :param DeleteFlag: 是否允許删除
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeleteFlag: int
        :param CreateTime: 創建時間
        :type CreateTime: str
        """
        self.VpcId = None
        self.PeerVpcId = None
        self.AppId = None
        self.PeerAppId = None
        self.VpcPeerConnectionId = None
        self.VpcPeerConnectionName = None
        self.State = None
        self.VpcZone = None
        self.PeerVpcZone = None
        self.Uin = None
        self.PeerUin = None
        self.PeerType = None
        self.Bandwidth = None
        self.Region = None
        self.PeerRegion = None
        self.DeleteFlag = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.PeerVpcId = params.get("PeerVpcId")
        self.AppId = params.get("AppId")
        self.PeerAppId = params.get("PeerAppId")
        self.VpcPeerConnectionId = params.get("VpcPeerConnectionId")
        self.VpcPeerConnectionName = params.get("VpcPeerConnectionName")
        self.State = params.get("State")
        self.VpcZone = params.get("VpcZone")
        self.PeerVpcZone = params.get("PeerVpcZone")
        self.Uin = params.get("Uin")
        self.PeerUin = params.get("PeerUin")
        self.PeerType = params.get("PeerType")
        self.Bandwidth = params.get("Bandwidth")
        self.Region = params.get("Region")
        self.PeerRegion = params.get("PeerRegion")
        self.DeleteFlag = params.get("DeleteFlag")
        self.CreateTime = params.get("CreateTime")


class VpcQuota(AbstractModel):
    """VPC限額訊息

    """

    def __init__(self):
        """
        :param TypeId: 配額類型ID
        :type TypeId: int
        :param Quota: 配額
        :type Quota: int
        """
        self.TypeId = None
        self.Quota = None


    def _deserialize(self, params):
        self.TypeId = params.get("TypeId")
        self.Quota = params.get("Quota")


class VpcResource(AbstractModel):
    """VPC占用資源

    """

    def __init__(self):
        """
        :param VpcId: 私有網絡ID
        :type VpcId: str
        :param VpcName: 私有網絡名稱
        :type VpcName: str
        :param CidrBlock: 私有網絡的CIDR
        :type CidrBlock: str
        :param SubnetNum: 子網個數
        :type SubnetNum: int
        :param NatNum: NAT個數
        :type NatNum: int
        :param State: VPC狀态
        :type State: str
        :param MonitorFlag: 是否開啓監控
        :type MonitorFlag: bool
        :param CpmNum: 物理機個數
        :type CpmNum: int
        :param LeaveIpNum: 可用IP個數
        :type LeaveIpNum: int
        :param LbNum: 負載均衡個數
        :type LbNum: int
        :param TrafficMirrorNum: 流量映像閘道個數
        :type TrafficMirrorNum: int
        :param EipNum: 彈性IP個數
        :type EipNum: int
        :param PlgwNum: 專線閘道個數
        :type PlgwNum: int
        :param PlvpNum: 專線通道個數
        :type PlvpNum: int
        :param SslVpnGwNum: ssl vpn閘道個數
        :type SslVpnGwNum: int
        :param VpcPeerNum: 對等連結個數
        :type VpcPeerNum: int
        :param IpsecVpnGwNum: ipsec vpn閘道個數
        :type IpsecVpnGwNum: int
        :param Zone: 可用區
        :type Zone: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param IsOld: 是否老專區VPC
        :type IsOld: bool
        :param CcnServiceNum: 雲聯網服務個數
注意：此欄位可能返回 null，表示取不到有效值。
        :type CcnServiceNum: int
        :param VpcPeerLimitToAllRegion: VPC允許創建的對等連接個數
注意：此欄位可能返回 null，表示取不到有效值。
        :type VpcPeerLimitToAllRegion: int
        :param VpcPeerLimitToSameRegion: VPC允許創建的同地域的對等連接的個數
注意：此欄位可能返回 null，表示取不到有效值。
        :type VpcPeerLimitToSameRegion: int
        :param IntVpcId: 整型私有網絡ID
        :type IntVpcId: int
        """
        self.VpcId = None
        self.VpcName = None
        self.CidrBlock = None
        self.SubnetNum = None
        self.NatNum = None
        self.State = None
        self.MonitorFlag = None
        self.CpmNum = None
        self.LeaveIpNum = None
        self.LbNum = None
        self.TrafficMirrorNum = None
        self.EipNum = None
        self.PlgwNum = None
        self.PlvpNum = None
        self.SslVpnGwNum = None
        self.VpcPeerNum = None
        self.IpsecVpnGwNum = None
        self.Zone = None
        self.CreateTime = None
        self.IsOld = None
        self.CcnServiceNum = None
        self.VpcPeerLimitToAllRegion = None
        self.VpcPeerLimitToSameRegion = None
        self.IntVpcId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.CidrBlock = params.get("CidrBlock")
        self.SubnetNum = params.get("SubnetNum")
        self.NatNum = params.get("NatNum")
        self.State = params.get("State")
        self.MonitorFlag = params.get("MonitorFlag")
        self.CpmNum = params.get("CpmNum")
        self.LeaveIpNum = params.get("LeaveIpNum")
        self.LbNum = params.get("LbNum")
        self.TrafficMirrorNum = params.get("TrafficMirrorNum")
        self.EipNum = params.get("EipNum")
        self.PlgwNum = params.get("PlgwNum")
        self.PlvpNum = params.get("PlvpNum")
        self.SslVpnGwNum = params.get("SslVpnGwNum")
        self.VpcPeerNum = params.get("VpcPeerNum")
        self.IpsecVpnGwNum = params.get("IpsecVpnGwNum")
        self.Zone = params.get("Zone")
        self.CreateTime = params.get("CreateTime")
        self.IsOld = params.get("IsOld")
        self.CcnServiceNum = params.get("CcnServiceNum")
        self.VpcPeerLimitToAllRegion = params.get("VpcPeerLimitToAllRegion")
        self.VpcPeerLimitToSameRegion = params.get("VpcPeerLimitToSameRegion")
        self.IntVpcId = params.get("IntVpcId")


class VpcSubnetCreateInfo(AbstractModel):
    """創建VPC下預設子網

    """

    def __init__(self):
        """
        :param SubnetName: 子網名稱
        :type SubnetName: str
        :param CidrBlock: 子網的CIDR
        :type CidrBlock: str
        :param Zone: 子網的可用區
        :type Zone: str
        """
        self.SubnetName = None
        self.CidrBlock = None
        self.Zone = None


    def _deserialize(self, params):
        self.SubnetName = params.get("SubnetName")
        self.CidrBlock = params.get("CidrBlock")
        self.Zone = params.get("Zone")


class VpcSubnetViewInfo(AbstractModel):
    """VPC視圖子網訊息

    """

    def __init__(self):
        """
        :param SubnetId: 子網ID
        :type SubnetId: str
        :param SubnetName: 子網名稱
        :type SubnetName: str
        :param CidrBlock: 子網CIDR
        :type CidrBlock: str
        :param CpmNum: 子網下設備個數
        :type CpmNum: int
        :param LbNum: 内網負載均衡個數
        :type LbNum: int
        :param Zone: 子網所在可用區
        :type Zone: str
        """
        self.SubnetId = None
        self.SubnetName = None
        self.CidrBlock = None
        self.CpmNum = None
        self.LbNum = None
        self.Zone = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.CidrBlock = params.get("CidrBlock")
        self.CpmNum = params.get("CpmNum")
        self.LbNum = params.get("LbNum")
        self.Zone = params.get("Zone")


class VpcViewInfo(AbstractModel):
    """VPC視圖訊息

    """

    def __init__(self):
        """
        :param VpcId: 私有網絡ID
        :type VpcId: str
        :param VpcName: 私有網絡名稱
        :type VpcName: str
        :param CidrBlock: 私有網絡CIDR
        :type CidrBlock: str
        :param Zone: 私有網絡所在可用區
        :type Zone: str
        :param LbNum: 外網負載均衡個數
        :type LbNum: int
        :param EipNum: 彈性公網IP個數
        :type EipNum: int
        :param NatNum: NAT閘道個數
        :type NatNum: int
        :param SubnetSet: 子網清單
        :type SubnetSet: list of VpcSubnetViewInfo
        """
        self.VpcId = None
        self.VpcName = None
        self.CidrBlock = None
        self.Zone = None
        self.LbNum = None
        self.EipNum = None
        self.NatNum = None
        self.SubnetSet = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.CidrBlock = params.get("CidrBlock")
        self.Zone = params.get("Zone")
        self.LbNum = params.get("LbNum")
        self.EipNum = params.get("EipNum")
        self.NatNum = params.get("NatNum")
        if params.get("SubnetSet") is not None:
            self.SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = VpcSubnetViewInfo()
                obj._deserialize(item)
                self.SubnetSet.append(obj)


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
        :param CreateTime: 創建時間。
        :type CreateTime: str
        :param State: 通道的生産狀态
        :type State: str
        :param NetStatus: 通道連接狀态
        :type NetStatus: str
        :param SecurityPolicyDatabaseSet: SPD。
        :type SecurityPolicyDatabaseSet: list of SecurityPolicyDatabase
        :param IKEOptionsSpecification: IKE選項。
        :type IKEOptionsSpecification: :class:`taifucloudcloud.bmvpc.v20180625.models.IKEOptionsSpecification`
        :param IPSECOptionsSpecification: IPSEC選項。
        :type IPSECOptionsSpecification: :class:`taifucloudcloud.bmvpc.v20180625.models.IPSECOptionsSpecification`
        :param Zone: 可用區
        :type Zone: str
        :param VpcCidrBlock: VPC網段
        :type VpcCidrBlock: str
        :param VpcName: VPC名稱
        :type VpcName: str
        :param VpnGatewayName: VPN閘道名稱
        :type VpnGatewayName: str
        :param CustomerGatewayName: 對端閘道名稱
        :type CustomerGatewayName: str
        :param DestinationCidr: IPSEC VPN通道路由策略目的端網址
注意：此欄位可能返回 null，表示取不到有效值。
        :type DestinationCidr: list of str
        :param SourceCidr: IPSEC VPN通道路由策略源端網址
注意：此欄位可能返回 null，表示取不到有效值。
        :type SourceCidr: list of str
        """
        self.VpnConnectionId = None
        self.VpnConnectionName = None
        self.VpcId = None
        self.VpnGatewayId = None
        self.CustomerGatewayId = None
        self.PreShareKey = None
        self.VpnProto = None
        self.CreateTime = None
        self.State = None
        self.NetStatus = None
        self.SecurityPolicyDatabaseSet = None
        self.IKEOptionsSpecification = None
        self.IPSECOptionsSpecification = None
        self.Zone = None
        self.VpcCidrBlock = None
        self.VpcName = None
        self.VpnGatewayName = None
        self.CustomerGatewayName = None
        self.DestinationCidr = None
        self.SourceCidr = None


    def _deserialize(self, params):
        self.VpnConnectionId = params.get("VpnConnectionId")
        self.VpnConnectionName = params.get("VpnConnectionName")
        self.VpcId = params.get("VpcId")
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.CustomerGatewayId = params.get("CustomerGatewayId")
        self.PreShareKey = params.get("PreShareKey")
        self.VpnProto = params.get("VpnProto")
        self.CreateTime = params.get("CreateTime")
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
        self.Zone = params.get("Zone")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.VpcName = params.get("VpcName")
        self.VpnGatewayName = params.get("VpnGatewayName")
        self.CustomerGatewayName = params.get("CustomerGatewayName")
        self.DestinationCidr = params.get("DestinationCidr")
        self.SourceCidr = params.get("SourceCidr")


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
        :param VpcCidrBlock: VPC網段
        :type VpcCidrBlock: str
        :param VpcName: VPC名稱
        :type VpcName: str
        :param InternetMaxBandwidthOut: 閘道出頻寬。
        :type InternetMaxBandwidthOut: int
        :param State: 閘道實例狀态
        :type State: str
        :param PublicIpAddress: 閘道公網IP。
        :type PublicIpAddress: str
        :param CreateTime: 創建時間。
        :type CreateTime: str
        :param Zone: 可用區，如：ap-guangzhou
        :type Zone: str
        :param VpnConnNum: VPN閘道的通道數
        :type VpnConnNum: int
        """
        self.VpnGatewayId = None
        self.VpcId = None
        self.VpnGatewayName = None
        self.VpcCidrBlock = None
        self.VpcName = None
        self.InternetMaxBandwidthOut = None
        self.State = None
        self.PublicIpAddress = None
        self.CreateTime = None
        self.Zone = None
        self.VpnConnNum = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.VpcId = params.get("VpcId")
        self.VpnGatewayName = params.get("VpnGatewayName")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.VpcName = params.get("VpcName")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.State = params.get("State")
        self.PublicIpAddress = params.get("PublicIpAddress")
        self.CreateTime = params.get("CreateTime")
        self.Zone = params.get("Zone")
        self.VpnConnNum = params.get("VpnConnNum")