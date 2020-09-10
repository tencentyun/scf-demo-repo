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


class Address(AbstractModel):
    """描述 EIP 訊息

    """

    def __init__(self):
        """
        :param AddressId: EIP的ID，是EIP的唯一标識。
        :type AddressId: str
        :param AddressName: EIP名稱。
        :type AddressName: str
        :param AddressStatus: EIP狀态，包含'CREATING'(創建中),'BINDING'(綁定中),'BIND'(已綁定),'UNBINDING'(解綁中),'UNBIND'(已解綁),'OFFLINING'(釋放中),'BIND_ENI'(綁定懸空彈性網卡)
        :type AddressStatus: str
        :param AddressIp: 外網IP網址
        :type AddressIp: str
        :param InstanceId: 綁定的資源實例ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param CreatedTime: 創建時間。ISO 8601 格式：YYYY-MM-DDTHH:mm:ss.sssZ
        :type CreatedTime: str
        :param NetworkInterfaceId: 綁定的彈性網卡ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type NetworkInterfaceId: str
        :param PrivateAddressIp: 綁定的資源内網ip
注意：此欄位可能返回 null，表示取不到有效值。
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
        :param InternetServiceProvider: 運營商，CTCC電信，CUCC聯通，CMCC移動
注意：此欄位可能返回 null，表示取不到有效值。
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
        self.InternetServiceProvider = params.get("InternetServiceProvider")


class AllocateAddressesRequest(AbstractModel):
    """AllocateAddresses請求參數結構體

    """

    def __init__(self):
        """
        :param EcmRegion: ECM 地域
        :type EcmRegion: str
        :param AddressCount: EIP數量。預設值：1。
        :type AddressCount: int
        :param InternetServiceProvider: CMCC：中國移動
CTCC：中國電信
CUCC：中國聯通
        :type InternetServiceProvider: str
        :param InternetMaxBandwidthOut: 1 Mbps 至 5000 Mbps，預設值：1 Mbps。
        :type InternetMaxBandwidthOut: int
        :param Tags: 需要關聯的标簽清單。
        :type Tags: list of Tag
        """
        self.EcmRegion = None
        self.AddressCount = None
        self.InternetServiceProvider = None
        self.InternetMaxBandwidthOut = None
        self.Tags = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.AddressCount = params.get("AddressCount")
        self.InternetServiceProvider = params.get("InternetServiceProvider")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class AllocateAddressesResponse(AbstractModel):
    """AllocateAddresses返回參數結構體

    """

    def __init__(self):
        """
        :param AddressSet: 申請到的 EIP 的唯一 ID 清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AddressSet: list of str
        :param TaskId: 異步任務TaskId。可以使用DescribeTaskResult介面查詢任務狀态。
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


class Area(AbstractModel):
    """區域訊息

    """

    def __init__(self):
        """
        :param AreaId: 區域ID
        :type AreaId: str
        :param AreaName: 區域名稱
        :type AreaName: str
        """
        self.AreaId = None
        self.AreaName = None


    def _deserialize(self, params):
        self.AreaId = params.get("AreaId")
        self.AreaName = params.get("AreaName")


class AssignPrivateIpAddressesRequest(AbstractModel):
    """AssignPrivateIpAddresses請求參數結構體

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 彈性網卡實例ID，例如：eni-m6dyj72l。
        :type NetworkInterfaceId: str
        :param EcmRegion: ECM 地域
        :type EcmRegion: str
        :param PrivateIpAddresses: 指定的内網IP訊息，單次最多指定10個。與SecondaryPrivateIpAddressCount至少提供一個。
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        :param SecondaryPrivateIpAddressCount: 新申請的内網IP網址個數，與PrivateIpAddresses至少提供一個。内網IP網址個數總和不能超過配額數
        :type SecondaryPrivateIpAddressCount: int
        """
        self.NetworkInterfaceId = None
        self.EcmRegion = None
        self.PrivateIpAddresses = None
        self.SecondaryPrivateIpAddressCount = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.EcmRegion = params.get("EcmRegion")
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
注意：此欄位可能返回 null，表示取不到有效值。
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
        :param VpcId: VPC實例ID。形如：vpc-6v2ht8q5
        :type VpcId: str
        :param CidrBlock: 輔助CIDR。形如：172.16.0.0/16
        :type CidrBlock: str
        :param AssistantType: 輔助CIDR類型（0：普通輔助CIDR，1：容器輔助CIDR），預設都是0。
        :type AssistantType: int
        :param SubnetSet: 輔助CIDR拆分的子網。
注意：此欄位可能返回 null，表示取不到有效值。
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
        :param EcmRegion: ECM 地域
        :type EcmRegion: str
        :param AddressId: 标識 EIP 的唯一 ID。EIP 唯一 ID 形如：eip-11112222。
        :type AddressId: str
        :param InstanceId: 要綁定的實例 ID。
        :type InstanceId: str
        :param NetworkInterfaceId: 要綁定的彈性網卡 ID。 彈性網卡 ID 形如：eni-11112222。NetworkInterfaceId 與 InstanceId 不可同時指定。彈性網卡 ID 可通過DescribeNetworkInterfaces介面返回值中的networkInterfaceId獲取。
        :type NetworkInterfaceId: str
        :param PrivateIpAddress: 要綁定的内網 IP。如果指定了 NetworkInterfaceId 則也必須指定 PrivateIpAddress ，表示将 EIP 綁定到指定彈性網卡的指定内網 IP 上。同時要确保指定的 PrivateIpAddress 是指定的 NetworkInterfaceId 上的一個内網 IP。指定彈性網卡的内網 IP 可通過DescribeNetworkInterfaces介面返回值中的privateIpAddress獲取。
        :type PrivateIpAddress: str
        """
        self.EcmRegion = None
        self.AddressId = None
        self.InstanceId = None
        self.NetworkInterfaceId = None
        self.PrivateIpAddress = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.AddressId = params.get("AddressId")
        self.InstanceId = params.get("InstanceId")
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.PrivateIpAddress = params.get("PrivateIpAddress")


class AssociateAddressResponse(AbstractModel):
    """AssociateAddress返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步任務TaskId。可以使用DescribeTaskResult介面查詢任務狀态。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class AttachNetworkInterfaceRequest(AbstractModel):
    """AttachNetworkInterface請求參數結構體

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 彈性網卡實例ID，例如：eni-m6dyj72l。
        :type NetworkInterfaceId: str
        :param InstanceId: 實例ID。形如：ein-r8hr2upy。
        :type InstanceId: str
        :param EcmRegion: ECM 地域
        :type EcmRegion: str
        """
        self.NetworkInterfaceId = None
        self.InstanceId = None
        self.EcmRegion = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.InstanceId = params.get("InstanceId")
        self.EcmRegion = params.get("EcmRegion")


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


class City(AbstractModel):
    """城市訊息

    """

    def __init__(self):
        """
        :param CityId: 城市ID
        :type CityId: str
        :param CityName: 城市名稱
        :type CityName: str
        """
        self.CityId = None
        self.CityName = None


    def _deserialize(self, params):
        self.CityId = params.get("CityId")
        self.CityName = params.get("CityName")


class Country(AbstractModel):
    """國家訊息

    """

    def __init__(self):
        """
        :param CountryId: 國家ID
        :type CountryId: str
        :param CountryName: 國家名稱
        :type CountryName: str
        """
        self.CountryId = None
        self.CountryName = None


    def _deserialize(self, params):
        self.CountryId = params.get("CountryId")
        self.CountryName = params.get("CountryName")


class CreateModuleRequest(AbstractModel):
    """CreateModule請求參數結構體

    """

    def __init__(self):
        """
        :param ModuleName: 模組名稱，如視訊直播模組。限制：模組名稱不得以空格開頭，長度不得超過60個字元。
        :type ModuleName: str
        :param DefaultBandWidth: 預設頻寬，單位：M。範圍不得超過頻寬上下限，詳看DescribeConfig。
        :type DefaultBandWidth: int
        :param DefaultImageId: 預設映像，如img-qsdf3ff2。
        :type DefaultImageId: str
        :param InstanceType: 機型ID。
        :type InstanceType: str
        :param DefaultSystemDiskSize: 預設系統盤大小，單位：G，預設大小爲50G。範圍不得超過系統盤上下限制，詳看DescribeConfig。
        :type DefaultSystemDiskSize: int
        :param DefaultDataDiskSize: 預設數據盤大小，單位：G。範圍不得超過數據盤範圍大小，詳看DescribeConfig。
        :type DefaultDataDiskSize: int
        """
        self.ModuleName = None
        self.DefaultBandWidth = None
        self.DefaultImageId = None
        self.InstanceType = None
        self.DefaultSystemDiskSize = None
        self.DefaultDataDiskSize = None


    def _deserialize(self, params):
        self.ModuleName = params.get("ModuleName")
        self.DefaultBandWidth = params.get("DefaultBandWidth")
        self.DefaultImageId = params.get("DefaultImageId")
        self.InstanceType = params.get("InstanceType")
        self.DefaultSystemDiskSize = params.get("DefaultSystemDiskSize")
        self.DefaultDataDiskSize = params.get("DefaultDataDiskSize")


class CreateModuleResponse(AbstractModel):
    """CreateModule返回參數結構體

    """

    def __init__(self):
        """
        :param ModuleId: 模組ID，創模組化塊成功後分配給該模組的ID。
        :type ModuleId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ModuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
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
        :param EcmRegion: ECM 地域
        :type EcmRegion: str
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
        self.EcmRegion = None
        self.NetworkInterfaceDescription = None
        self.SecondaryPrivateIpAddressCount = None
        self.SecurityGroupIds = None
        self.PrivateIpAddresses = None
        self.Tags = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NetworkInterfaceName = params.get("NetworkInterfaceName")
        self.SubnetId = params.get("SubnetId")
        self.EcmRegion = params.get("EcmRegion")
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
        :type NetworkInterface: :class:`tencentcloud.ecm.v20190719.models.NetworkInterface`
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
        :param EcmRegion: ECM 地域
        :type EcmRegion: str
        :param Tags: 指定綁定的标簽清單，例如：[{"Key": "city", "Value": "shanghai"}]
        :type Tags: list of Tag
        """
        self.VpcId = None
        self.SubnetName = None
        self.CidrBlock = None
        self.Zone = None
        self.EcmRegion = None
        self.Tags = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetName = params.get("SubnetName")
        self.CidrBlock = params.get("CidrBlock")
        self.Zone = params.get("Zone")
        self.EcmRegion = params.get("EcmRegion")
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
        :type Subnet: :class:`tencentcloud.ecm.v20190719.models.Subnet`
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


class CreateVpcRequest(AbstractModel):
    """CreateVpc請求參數結構體

    """

    def __init__(self):
        """
        :param VpcName: vpc名稱，最大長度不能超過60個位元。
        :type VpcName: str
        :param CidrBlock: vpc的cidr，只能爲10.0.0.0/16，172.16.0.0/16，192.168.0.0/16這三個内網網段内。
        :type CidrBlock: str
        :param EcmRegion: ECM 地域
        :type EcmRegion: str
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
        self.EcmRegion = None
        self.EnableMulticast = None
        self.DnsServers = None
        self.DomainName = None
        self.Tags = None


    def _deserialize(self, params):
        self.VpcName = params.get("VpcName")
        self.CidrBlock = params.get("CidrBlock")
        self.EcmRegion = params.get("EcmRegion")
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
        :type Vpc: :class:`tencentcloud.ecm.v20190719.models.VpcInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Vpc = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Vpc") is not None:
            self.Vpc = VpcInfo()
            self.Vpc._deserialize(params.get("Vpc"))
        self.RequestId = params.get("RequestId")


class DeleteImageRequest(AbstractModel):
    """DeleteImage請求參數結構體

    """

    def __init__(self):
        """
        :param ImageIDSet: 映像ID清單。
        :type ImageIDSet: list of str
        """
        self.ImageIDSet = None


    def _deserialize(self, params):
        self.ImageIDSet = params.get("ImageIDSet")


class DeleteImageResponse(AbstractModel):
    """DeleteImage返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteModuleRequest(AbstractModel):
    """DeleteModule請求參數結構體

    """

    def __init__(self):
        """
        :param ModuleId: 模組ID。如：es-qn46snq8
        :type ModuleId: str
        """
        self.ModuleId = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")


class DeleteModuleResponse(AbstractModel):
    """DeleteModule返回參數結構體

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
        :param EcmRegion: ECM 地域
        :type EcmRegion: str
        """
        self.NetworkInterfaceId = None
        self.EcmRegion = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.EcmRegion = params.get("EcmRegion")


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


class DeleteSubnetRequest(AbstractModel):
    """DeleteSubnet請求參數結構體

    """

    def __init__(self):
        """
        :param SubnetId: 子網實例ID。可通過DescribeSubnets介面返回值中的SubnetId獲取。
        :type SubnetId: str
        :param EcmRegion: ECM 地域
        :type EcmRegion: str
        """
        self.SubnetId = None
        self.EcmRegion = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.EcmRegion = params.get("EcmRegion")


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
        :param EcmRegion: ECM 地域
        :type EcmRegion: str
        """
        self.VpcId = None
        self.EcmRegion = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.EcmRegion = params.get("EcmRegion")


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


class DescribeAddressQuotaRequest(AbstractModel):
    """DescribeAddressQuota請求參數結構體

    """

    def __init__(self):
        """
        :param EcmRegion: ECM 地域
        :type EcmRegion: str
        """
        self.EcmRegion = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")


class DescribeAddressQuotaResponse(AbstractModel):
    """DescribeAddressQuota返回參數結構體

    """

    def __init__(self):
        """
        :param QuotaSet: 帳戶 EIP 配額訊息。
        :type QuotaSet: list of EipQuota
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.QuotaSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("QuotaSet") is not None:
            self.QuotaSet = []
            for item in params.get("QuotaSet"):
                obj = EipQuota()
                obj._deserialize(item)
                self.QuotaSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAddressesRequest(AbstractModel):
    """DescribeAddresses請求參數結構體

    """

    def __init__(self):
        """
        :param EcmRegion: ECM 地域
        :type EcmRegion: str
        :param AddressIds: 标識 EIP 的唯一 ID 清單。EIP 唯一 ID 形如：eip-11112222。參數不支援同時指定AddressIds和Filters。
        :type AddressIds: list of str
        :param Filters: 每次請求的Filters的上限爲10，Filter.Values的上限爲5。參數不支援同時指定AddressIds和Filters。詳細的過濾條件如下：
address-id - String - 是否必填：否 - （過濾條件）按照 EIP 的唯一 ID 過濾。EIP 唯一 ID 形如：eip-11112222。
address-name - String - 是否必填：否 - （過濾條件）按照 EIP 名稱過濾。不支援模糊過濾。
address-ip - String - 是否必填：否 - （過濾條件）按照 EIP 的 IP 網址過濾。
address-status - String - 是否必填：否 - （過濾條件）按照 EIP 的狀态過濾。取值範圍：詳見EIP狀态清單。
instance-id - String - 是否必填：否 - （過濾條件）按照 EIP 綁定的實例 ID 過濾。實例 ID 形如：ins-11112222。
private-ip-address - String - 是否必填：否 - （過濾條件）按照 EIP 綁定的内網 IP 過濾。
network-interface-id - String - 是否必填：否 - （過濾條件）按照 EIP 綁定的彈性網卡 ID 過濾。彈性網卡 ID 形如：eni-11112222。
is-arrears - String - 是否必填：否 - （過濾條件）按照 EIP 是否欠費進行過濾。（TRUE：EIP 處于欠費狀态|FALSE：EIP 費用狀态正常）
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。
        :type Limit: int
        """
        self.EcmRegion = None
        self.AddressIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
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


class DescribeBaseOverviewRequest(AbstractModel):
    """DescribeBaseOverview請求參數結構體

    """


class DescribeBaseOverviewResponse(AbstractModel):
    """DescribeBaseOverview返回參數結構體

    """

    def __init__(self):
        """
        :param ModuleNum: 模組數量，單位：個
        :type ModuleNum: int
        :param NodeNum: 節點數量，單位：個
        :type NodeNum: int
        :param VcpuNum: cpu核數，單位：個
        :type VcpuNum: int
        :param MemoryNum: 内存大小，單位：G
        :type MemoryNum: int
        :param StorageNum: 硬碟大小，單位：G
        :type StorageNum: int
        :param NetworkNum: 昨日網絡峰值,單位：M
        :type NetworkNum: int
        :param InstanceNum: 實例數量，單位：台
        :type InstanceNum: int
        :param RunningNum: 運作中數量，單位：台
        :type RunningNum: int
        :param IsolationNum: 安全隔離數量，單位：台
        :type IsolationNum: int
        :param ExpiredNum: 過期實例數量，單位：台
        :type ExpiredNum: int
        :param WillExpireNum: 即将過期實例數量，單位：台
        :type WillExpireNum: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ModuleNum = None
        self.NodeNum = None
        self.VcpuNum = None
        self.MemoryNum = None
        self.StorageNum = None
        self.NetworkNum = None
        self.InstanceNum = None
        self.RunningNum = None
        self.IsolationNum = None
        self.ExpiredNum = None
        self.WillExpireNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ModuleNum = params.get("ModuleNum")
        self.NodeNum = params.get("NodeNum")
        self.VcpuNum = params.get("VcpuNum")
        self.MemoryNum = params.get("MemoryNum")
        self.StorageNum = params.get("StorageNum")
        self.NetworkNum = params.get("NetworkNum")
        self.InstanceNum = params.get("InstanceNum")
        self.RunningNum = params.get("RunningNum")
        self.IsolationNum = params.get("IsolationNum")
        self.ExpiredNum = params.get("ExpiredNum")
        self.WillExpireNum = params.get("WillExpireNum")
        self.RequestId = params.get("RequestId")


class DescribeConfigRequest(AbstractModel):
    """DescribeConfig請求參數結構體

    """


class DescribeConfigResponse(AbstractModel):
    """DescribeConfig返回參數結構體

    """

    def __init__(self):
        """
        :param NetworkStorageRange: 網絡頻寬硬碟大小的範圍訊息。
        :type NetworkStorageRange: :class:`tencentcloud.ecm.v20190719.models.NetworkStorageRange`
        :param ImageWhiteSet: 映像作業系統白名單
注意：此欄位可能返回 null，表示取不到有效值。
        :type ImageWhiteSet: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NetworkStorageRange = None
        self.ImageWhiteSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetworkStorageRange") is not None:
            self.NetworkStorageRange = NetworkStorageRange()
            self.NetworkStorageRange._deserialize(params.get("NetworkStorageRange"))
        self.ImageWhiteSet = params.get("ImageWhiteSet")
        self.RequestId = params.get("RequestId")


class DescribeImageRequest(AbstractModel):
    """DescribeImage請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 過濾條件，每次請求的Filters的上限爲10，詳細的過濾條件如下：
image-id - String - 是否必填： 否 - （過濾條件）按照映像ID進行過濾
image-type - String - 是否必填： 否 - （過濾條件）按照映像類型進行過濾。取值範圍：
PRIVATE_IMAGE: 私有映像 (本帳戶創建的映像) 
PUBLIC_IMAGE: 公共映像 (Top Cloud 官方映像)
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。關于Offset的更進一步介紹請參考 API 簡介中的相關小節。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。關于Limit的更進一步介紹請參考 API 簡介中的相關小節。
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


class DescribeImageResponse(AbstractModel):
    """DescribeImage返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 映像總數
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param ImageSet: 映像數組
注意：此欄位可能返回 null，表示取不到有效值。
        :type ImageSet: list of Image
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ImageSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ImageSet") is not None:
            self.ImageSet = []
            for item in params.get("ImageSet"):
                obj = Image()
                obj._deserialize(item)
                self.ImageSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceTypeConfigRequest(AbstractModel):
    """DescribeInstanceTypeConfig請求參數結構體

    """


class DescribeInstanceTypeConfigResponse(AbstractModel):
    """DescribeInstanceTypeConfig返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 總數
        :type TotalCount: int
        :param InstanceTypeConfigSet: 機型配置訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceTypeConfigSet: list of InstanceTypeConfig
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceTypeConfigSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceTypeConfigSet") is not None:
            self.InstanceTypeConfigSet = []
            for item in params.get("InstanceTypeConfigSet"):
                obj = InstanceTypeConfig()
                obj._deserialize(item)
                self.InstanceTypeConfigSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesDeniedActionsRequest(AbstractModel):
    """DescribeInstancesDeniedActions請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIdSet: 無
        :type InstanceIdSet: list of str
        """
        self.InstanceIdSet = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")


class DescribeInstancesDeniedActionsResponse(AbstractModel):
    """DescribeInstancesDeniedActions返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceOperatorSet: 實例對應的禁止操作
        :type InstanceOperatorSet: list of InstanceOperator
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceOperatorSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceOperatorSet") is not None:
            self.InstanceOperatorSet = []
            for item in params.get("InstanceOperatorSet"):
                obj = InstanceOperator()
                obj._deserialize(item)
                self.InstanceOperatorSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 過濾條件。
zone      String      是否必填：否     （過濾條件）按照可用區中文名過濾,支援模糊比對。
module-id      String      是否必填：否     （過濾條件）按照模組ID過濾。
instance-id      String      是否必填：否      （過濾條件）按照實例ID過濾。
instance-name      String      是否必填：否      （過濾條件）按照實例名稱過濾,支援模糊比對。
ip-address      String      是否必填：否      （過濾條件）按照實例的内網/公網IP過濾。
instance-uuid   string 是否必填：否 （過濾條件）按照uuid過濾實例清單。
instance-state  string  是否必填：否 （過濾條件）按照實例狀态更新實例清單。
internet-service-provider      String      是否必填：否      （過濾條件）按照實例公網IP所屬的運營商進行過濾。
tag-key      String      是否必填：否      （過濾條件）按照标簽鍵進行過濾。
tag:tag-key      String      是否必填：否      （過濾條件）按照标簽鍵值對進行過濾。 tag-key使用具體的标簽鍵進行替換。
若不傳Filters參數則表示查詢所有相關的實例訊息。
單次請求的Filter.Values的上限爲5。
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Limit: 返回數量，預設爲20(如果查詢結果數目大于等于20)，最大值爲100。
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


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 返回的實例相關訊息清單的長度。
        :type TotalCount: int
        :param InstanceSet: 返回的實例相關訊息清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceSet: list of Instance
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
                obj = Instance()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeModuleDetailRequest(AbstractModel):
    """DescribeModuleDetail請求參數結構體

    """

    def __init__(self):
        """
        :param ModuleId: 模組ID，如em-qn46snq8。
        :type ModuleId: str
        """
        self.ModuleId = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")


class DescribeModuleDetailResponse(AbstractModel):
    """DescribeModuleDetail返回參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組的詳細訊息，詳細見數據結構中的ModuleInfo。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Module: :class:`tencentcloud.ecm.v20190719.models.Module`
        :param ModuleCounter: 模組的統計訊息，詳細見數據結構中的ModuleCounterInfo。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ModuleCounter: :class:`tencentcloud.ecm.v20190719.models.ModuleCounter`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Module = None
        self.ModuleCounter = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Module") is not None:
            self.Module = Module()
            self.Module._deserialize(params.get("Module"))
        if params.get("ModuleCounter") is not None:
            self.ModuleCounter = ModuleCounter()
            self.ModuleCounter._deserialize(params.get("ModuleCounter"))
        self.RequestId = params.get("RequestId")


class DescribeModuleRequest(AbstractModel):
    """DescribeModule請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 過濾條件。
module-name - string - 是否必填：否 - （過濾條件）按照模組名稱過濾。
module-id - string - 是否必填：否 - （過濾條件）按照模組ID過濾。
每次請求的Filters的上限爲10，Filter.Values的上限爲5。
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。關于Offset的更進一步介紹請參考 API 簡介中的相關小節。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。關于Limit的更進一步介紹請參考 API 簡介中的相關小節。
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


class DescribeModuleResponse(AbstractModel):
    """DescribeModule返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的模組數量。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param ModuleItemSet: 模組詳情訊息的清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ModuleItemSet: list of ModuleItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ModuleItemSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ModuleItemSet") is not None:
            self.ModuleItemSet = []
            for item in params.get("ModuleItemSet"):
                obj = ModuleItem()
                obj._deserialize(item)
                self.ModuleItemSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNetworkInterfacesRequest(AbstractModel):
    """DescribeNetworkInterfaces請求參數結構體

    """

    def __init__(self):
        """
        :param EcmRegion: ECM 地域
        :type EcmRegion: str
        :param NetworkInterfaceIds: 彈性網卡實例ID查詢。形如：eni-pxir56ns。每次請求的實例的上限爲100。參數不支援同時指定NetworkInterfaceIds和Filters。
        :type NetworkInterfaceIds: list of str
        :param Filters: 過濾條件，參數不支援同時指定NetworkInterfaceIds和Filters。
vpc-id - String - （過濾條件）VPC實例ID，形如：vpc-f49l6u0z。
subnet-id - String - （過濾條件）所屬子網實例ID，形如：subnet-f49l6u0z。
network-interface-id - String - （過濾條件）彈性網卡實例ID，形如：eni-5k56k7k7。
attachment.instance-id - String - （過濾條件）綁定的雲伺服器實例ID，形如：ins-3nqpdn3i。
groups.security-group-id - String - （過濾條件）綁定的安全組實例ID，例如：sg-f9ekbxeq。
network-interface-name - String - （過濾條件）網卡實例名稱。
network-interface-description - String - （過濾條件）網卡實例描述。
address-ip - String - （過濾條件）内網IPv4網址。
tag-key - String -是否必填：否- （過濾條件）按照标簽鍵進行過濾。使用請參考範例2
tag:tag-key - String - 是否必填：否 - （過濾條件）按照标簽鍵值對進行過濾。 tag-key使用具體的标簽鍵進行替換。使用請參考範例3。
is-primary - Boolean - 是否必填：否 - （過濾條件）按照是否主網卡進行過濾。值爲true時，僅過濾主網卡；值爲false時，僅過濾輔助網卡；次過濾參數爲提供時，同時過濾主網卡和輔助網卡。
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。
        :type Limit: int
        """
        self.EcmRegion = None
        self.NetworkInterfaceIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
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
        :param TotalCount: 符合條件的實例數量。
        :type TotalCount: int
        :param NetworkInterfaceSet: 實例詳細訊息清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type NetworkInterfaceSet: list of NetworkInterface
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.NetworkInterfaceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("NetworkInterfaceSet") is not None:
            self.NetworkInterfaceSet = []
            for item in params.get("NetworkInterfaceSet"):
                obj = NetworkInterface()
                obj._deserialize(item)
                self.NetworkInterfaceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNodeRequest(AbstractModel):
    """DescribeNode請求參數結構體

    """


class DescribeNodeResponse(AbstractModel):
    """DescribeNode返回參數結構體

    """

    def __init__(self):
        """
        :param NodeSet: 節點詳細訊息的清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type NodeSet: list of Node
        :param TotalCount: 所有的節點數量。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NodeSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NodeSet") is not None:
            self.NodeSet = []
            for item in params.get("NodeSet"):
                obj = Node()
                obj._deserialize(item)
                self.NodeSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribePeakBaseOverviewRequest(AbstractModel):
    """DescribePeakBaseOverview請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 開始時間（xxxx-xx-xx）如2019-08-14，預設爲一周之前的日期。
        :type StartTime: str
        :param EndTime: 結束時間（xxxx-xx-xx）如2019-08-14，預設爲昨天。
        :type EndTime: str
        """
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribePeakBaseOverviewResponse(AbstractModel):
    """DescribePeakBaseOverview返回參數結構體

    """

    def __init__(self):
        """
        :param PeakFamilyInfoSet: 基礎峰值清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PeakFamilyInfoSet: list of PeakFamilyInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PeakFamilyInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PeakFamilyInfoSet") is not None:
            self.PeakFamilyInfoSet = []
            for item in params.get("PeakFamilyInfoSet"):
                obj = PeakFamilyInfo()
                obj._deserialize(item)
                self.PeakFamilyInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePeakNetworkOverviewRequest(AbstractModel):
    """DescribePeakNetworkOverview請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 開始時間（xxxx-xx-xx）如2019-08-14，預設爲一周之前的日期。
        :type StartTime: str
        :param EndTime: 結束時間（xxxx-xx-xx）如2019-08-14，預設爲昨天。
        :type EndTime: str
        :param Filters: 過濾條件。
region    String      是否必填：否     （過濾條件）按照region過濾,不支援模糊比對。
        :type Filters: list of Filter
        """
        self.StartTime = None
        self.EndTime = None
        self.Filters = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribePeakNetworkOverviewResponse(AbstractModel):
    """DescribePeakNetworkOverview返回參數結構體

    """

    def __init__(self):
        """
        :param PeakNetworkRegionSet: 網絡峰值數組。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PeakNetworkRegionSet: list of PeakNetworkRegionInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PeakNetworkRegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PeakNetworkRegionSet") is not None:
            self.PeakNetworkRegionSet = []
            for item in params.get("PeakNetworkRegionSet"):
                obj = PeakNetworkRegionInfo()
                obj._deserialize(item)
                self.PeakNetworkRegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSubnetsRequest(AbstractModel):
    """DescribeSubnets請求參數結構體

    """

    def __init__(self):
        """
        :param EcmRegion: ECM 地域
        :type EcmRegion: str
        :param SubnetIds: 子網實例ID查詢。形如：subnet-pxir56ns。每次請求的實例的上限爲100。參數不支援同時指定SubnetIds和Filters。
        :type SubnetIds: list of str
        :param Filters: 過濾條件，參數不支援同時指定SubnetIds和Filters。
subnet-id - String - （過濾條件）Subnet實例名稱。
vpc-id - String - （過濾條件）VPC實例ID，形如：vpc-f49l6u0z。
cidr-block - String - （過濾條件）子網網段，形如: 192.168.1.0 。
is-default - Boolean - （過濾條件）是否是預設子網。
is-remote-vpc-snat - Boolean - （過濾條件）是否爲VPC SNAT網址池子網。
subnet-name - String - （過濾條件）子網名稱。
zone - String - （過濾條件）可用區。
tag-key - String -是否必填：否- （過濾條件）按照标簽鍵進行過濾。
tag:tag-key - String - 是否必填：否 - （過濾條件）按照标簽鍵值對進行過濾。 tag-key使用具體的标簽鍵進行替換。使用請參考範例
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: str
        :param Limit: 返回數量
        :type Limit: str
        """
        self.EcmRegion = None
        self.SubnetIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
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
注意：此欄位可能返回 null，表示取不到有效值。
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
        :param EcmRegion: ECM 地域
        :type EcmRegion: str
        :param TaskId: 異步任務ID。
        :type TaskId: str
        """
        self.EcmRegion = None
        self.TaskId = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.TaskId = params.get("TaskId")


class DescribeTaskResultResponse(AbstractModel):
    """DescribeTaskResult返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步任務ID。
        :type TaskId: str
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


class DescribeVpcsRequest(AbstractModel):
    """DescribeVpcs請求參數結構體

    """

    def __init__(self):
        """
        :param VpcIds: VPC實例ID。形如：vpc-f49l6u0z。每次請求的實例的上限爲100。參數不支援同時指定VpcIds和Filters。
        :type VpcIds: list of str
        :param Filters: 過濾條件，參數不支援同時指定VpcIds和Filters。
vpc-name - String - （過濾條件）VPC實例名稱。
is-default - String - （過濾條件）是否預設VPC。
vpc-id - String - （過濾條件）VPC實例ID形如：vpc-f49l6u0z。
cidr-block - String - （過濾條件）vpc的cidr。
tag-key - String -是否必填：否- （過濾條件）按照标簽鍵進行過濾。
tag:tag-key - String - 是否必填：否 - （過濾條件）按照标簽鍵值對進行過濾。 tag-key使用具體的标簽鍵進行替換。使用請參考範例
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回數量
        :type Limit: int
        :param EcmRegion: 地域
        :type EcmRegion: str
        """
        self.VpcIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.EcmRegion = None


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
        self.EcmRegion = params.get("EcmRegion")


class DescribeVpcsResponse(AbstractModel):
    """DescribeVpcs返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的對象數。
        :type TotalCount: int
        :param VpcSet: 私有網絡對象。
注意：此欄位可能返回 null，表示取不到有效值。
        :type VpcSet: list of VpcInfo
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
                obj = VpcInfo()
                obj._deserialize(item)
                self.VpcSet.append(obj)
        self.RequestId = params.get("RequestId")


class DetachNetworkInterfaceRequest(AbstractModel):
    """DetachNetworkInterface請求參數結構體

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 彈性網卡實例ID，例如：eni-m6dyj72l。
        :type NetworkInterfaceId: str
        :param InstanceId: 實例ID。形如：ein-hcs7jkg4
        :type InstanceId: str
        :param EcmRegion: ECM 地域
        :type EcmRegion: str
        """
        self.NetworkInterfaceId = None
        self.InstanceId = None
        self.EcmRegion = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.InstanceId = params.get("InstanceId")
        self.EcmRegion = params.get("EcmRegion")


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


class DisassociateAddressRequest(AbstractModel):
    """DisassociateAddress請求參數結構體

    """

    def __init__(self):
        """
        :param EcmRegion: ECM 地域
        :type EcmRegion: str
        :param AddressId: 标識 EIP 的唯一 ID。EIP 唯一 ID 形如：eip-11112222。
        :type AddressId: str
        :param ReallocateNormalPublicIp: 表示解綁 EIP 之後是否分配普通公網 IP。取值範圍：
TRUE：表示解綁 EIP 之後分配普通公網 IP。
FALSE：表示解綁 EIP 之後不分配普通公網 IP。
預設取值：FALSE。

只有滿足以下條件時才能指定該參數：
只有在解綁主網卡的主内網 IP 上的 EIP 時才能指定該參數。
解綁 EIP 後重新分配普通公網 IP 操作一個賬号每天最多操作 10 次；詳情可通過 DescribeAddressQuota 介面獲取。
        :type ReallocateNormalPublicIp: bool
        """
        self.EcmRegion = None
        self.AddressId = None
        self.ReallocateNormalPublicIp = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.AddressId = params.get("AddressId")
        self.ReallocateNormalPublicIp = params.get("ReallocateNormalPublicIp")


class DisassociateAddressResponse(AbstractModel):
    """DisassociateAddress返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步任務TaskId。可以使用DescribeTaskResult介面查詢任務狀态。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DiskInfo(AbstractModel):
    """磁盤訊息

    """

    def __init__(self):
        """
        :param DiskType: 磁盤類型：LOCAL_BASIC
        :type DiskType: str
        :param DiskId: 磁盤ID
        :type DiskId: str
        :param DiskSize: 磁盤大小（GB）
        :type DiskSize: int
        """
        self.DiskType = None
        self.DiskId = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskId = params.get("DiskId")
        self.DiskSize = params.get("DiskSize")


class EipQuota(AbstractModel):
    """描述EIP配額訊息

    """

    def __init__(self):
        """
        :param QuotaId: 配額名稱，取值範圍：
TOTAL_EIP_QUOTA：用戶當前地域下EIP的配額數；
DAILY_EIP_APPLY：用戶當前地域下今日申購次數；
DAILY_PUBLIC_IP_ASSIGN：用戶當前地域下，重新分配公網 IP次數。
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


class EnhancedService(AbstractModel):
    """增強服務

    """

    def __init__(self):
        """
        :param SecurityService: 是否開啓雲鏡服務。
        :type SecurityService: :class:`tencentcloud.ecm.v20190719.models.RunSecurityServiceEnabled`
        :param MonitorService: 是否開啓雲監控服務。
        :type MonitorService: :class:`tencentcloud.ecm.v20190719.models.RunMonitorServiceEnabled`
        """
        self.SecurityService = None
        self.MonitorService = None


    def _deserialize(self, params):
        if params.get("SecurityService") is not None:
            self.SecurityService = RunSecurityServiceEnabled()
            self.SecurityService._deserialize(params.get("SecurityService"))
        if params.get("MonitorService") is not None:
            self.MonitorService = RunMonitorServiceEnabled()
            self.MonitorService._deserialize(params.get("MonitorService"))


class Filter(AbstractModel):
    """過濾器Filter;由Name和ValueSet組成，是string的key和字串數組的value

    """

    def __init__(self):
        """
        :param Name: 過濾欄位名稱
        :type Name: str
        :param Values: 過濾欄位内容數組
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class ISP(AbstractModel):
    """運營商訊息

    """

    def __init__(self):
        """
        :param ISPId: 運營商ID
        :type ISPId: str
        :param ISPName: 運營商名稱
        :type ISPName: str
        """
        self.ISPId = None
        self.ISPName = None


    def _deserialize(self, params):
        self.ISPId = params.get("ISPId")
        self.ISPName = params.get("ISPName")


class ISPCounter(AbstractModel):
    """運作商統計訊息

    """

    def __init__(self):
        """
        :param ProviderName: 運營商名稱
        :type ProviderName: str
        :param ProviderNodeNum: 節點數量
        :type ProviderNodeNum: int
        :param ProvederInstanceNum: 實例數量
        :type ProvederInstanceNum: int
        :param ZoneInstanceInfoSet: Zone實例訊息結構體數組
        :type ZoneInstanceInfoSet: list of ZoneInstanceInfo
        """
        self.ProviderName = None
        self.ProviderNodeNum = None
        self.ProvederInstanceNum = None
        self.ZoneInstanceInfoSet = None


    def _deserialize(self, params):
        self.ProviderName = params.get("ProviderName")
        self.ProviderNodeNum = params.get("ProviderNodeNum")
        self.ProvederInstanceNum = params.get("ProvederInstanceNum")
        if params.get("ZoneInstanceInfoSet") is not None:
            self.ZoneInstanceInfoSet = []
            for item in params.get("ZoneInstanceInfoSet"):
                obj = ZoneInstanceInfo()
                obj._deserialize(item)
                self.ZoneInstanceInfoSet.append(obj)


class Image(AbstractModel):
    """映像訊息

    """

    def __init__(self):
        """
        :param ImageId: 映像ID
        :type ImageId: str
        :param ImageName: 映像名稱
        :type ImageName: str
        :param ImageState: 映像狀态
        :type ImageState: str
        :param ImageType: 映像類型
        :type ImageType: str
        :param ImageOsName: 作業系統名稱
        :type ImageOsName: str
        :param ImageDescription: 映像描述
        :type ImageDescription: str
        :param ImageCreateTime: 映像導入時間
        :type ImageCreateTime: str
        :param Architecture: 作業系統位數
        :type Architecture: str
        :param OsType: 作業系統類型
        :type OsType: str
        :param OsVersion: 作業系統版本
        :type OsVersion: str
        :param Platform: 作業系統平台
        :type Platform: str
        :param ImageOwner: 映像所有者
        :type ImageOwner: int
        :param ImageSize: 映像大小。單位：GB
        :type ImageSize: int
        :param SrcImage: 映像來源訊息
        :type SrcImage: :class:`tencentcloud.ecm.v20190719.models.SrcImage`
        """
        self.ImageId = None
        self.ImageName = None
        self.ImageState = None
        self.ImageType = None
        self.ImageOsName = None
        self.ImageDescription = None
        self.ImageCreateTime = None
        self.Architecture = None
        self.OsType = None
        self.OsVersion = None
        self.Platform = None
        self.ImageOwner = None
        self.ImageSize = None
        self.SrcImage = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.ImageName = params.get("ImageName")
        self.ImageState = params.get("ImageState")
        self.ImageType = params.get("ImageType")
        self.ImageOsName = params.get("ImageOsName")
        self.ImageDescription = params.get("ImageDescription")
        self.ImageCreateTime = params.get("ImageCreateTime")
        self.Architecture = params.get("Architecture")
        self.OsType = params.get("OsType")
        self.OsVersion = params.get("OsVersion")
        self.Platform = params.get("Platform")
        self.ImageOwner = params.get("ImageOwner")
        self.ImageSize = params.get("ImageSize")
        if params.get("SrcImage") is not None:
            self.SrcImage = SrcImage()
            self.SrcImage._deserialize(params.get("SrcImage"))


class ImportImageRequest(AbstractModel):
    """ImportImage請求參數結構體

    """

    def __init__(self):
        """
        :param ImageId: 映像的Id。
        :type ImageId: str
        :param ImageDescription: 映像的描述。
        :type ImageDescription: str
        :param SourceRegion: 源地域
        :type SourceRegion: str
        """
        self.ImageId = None
        self.ImageDescription = None
        self.SourceRegion = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.ImageDescription = params.get("ImageDescription")
        self.SourceRegion = params.get("SourceRegion")


class ImportImageResponse(AbstractModel):
    """ImportImage返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Instance(AbstractModel):
    """用于描述實例相關的訊息。

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID。
        :type InstanceId: str
        :param InstanceName: 實例名稱，如ens-34241f3s。
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param InstanceState: 實例狀态。取值範圍：
PENDING：表示創建中
LAUNCH_FAILED：表示創建失敗
RUNNING：表示運作中
STOPPED：表示關機
STARTING：表示開機中
STOPPING：表示關機中
REBOOTING：表示重啓中
SHUTDOWN：表示停止待銷毀
TERMINATING：表示銷毀中。
        :type InstanceState: str
        :param Image: 實例當前使用的映像的訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Image: :class:`tencentcloud.ecm.v20190719.models.Image`
        :param SimpleModule: 實例當前所屬的模組簡要訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SimpleModule: :class:`tencentcloud.ecm.v20190719.models.SimpleModule`
        :param Position: 實例所在的位置相關訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Position: :class:`tencentcloud.ecm.v20190719.models.Position`
        :param Internet: 實例的網絡相關訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Internet: :class:`tencentcloud.ecm.v20190719.models.Internet`
        :param InstanceTypeConfig: 實例的配置相關訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceTypeConfig: :class:`tencentcloud.ecm.v20190719.models.InstanceTypeConfig`
        :param CreateTime: 實例的創建時間。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param TagSet: 實例的标簽訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagSet: list of Tag
        :param LatestOperation: 實例最後一次操作。
注意：此欄位可能返回 null，表示取不到有效值。
        :type LatestOperation: str
        :param LatestOperationState: 實例最後一次操作結果。
注意：此欄位可能返回 null，表示取不到有效值。
        :type LatestOperationState: str
        :param RestrictState: 實例業務狀态。取值範圍：
NORMAL：表示正常狀态的實例
EXPIRED：表示過期的實例
PROTECTIVELY_ISOLATED：表示被安全隔離的實例。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RestrictState: str
        :param SystemDiskSize: 系統盤大小，單位GB。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SystemDiskSize: int
        :param DataDiskSize: 數據盤大小，單位GB。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DataDiskSize: int
        :param UUID: 實例UUID
注意：此欄位可能返回 null，表示取不到有效值。
        :type UUID: str
        :param PayMode: 付費方式。
    0爲後付費。
    1爲預付費。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PayMode: int
        :param ExpireTime: 過期時間。格式爲yyyy-mm-dd HH:mm:ss。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param IsolatedTime: 隔離時間。格式爲yyyy-mm-dd HH:mm:ss。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsolatedTime: str
        :param RenewFlag: 是否自動續約。
      0爲不自動續約。
      1爲自動續約。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RenewFlag: int
        :param ExpireState: 過期狀态。
    NORMAL 表示機器運作正常。
    WILL_EXPIRE 表示即将過期。
    EXPIRED 表示已過期。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ExpireState: str
        :param SystemDisk: 系統盤訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type SystemDisk: :class:`tencentcloud.ecm.v20190719.models.DiskInfo`
        :param DataDisks: 數據盤訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type DataDisks: list of DiskInfo
        :param NewFlag: 新實例标志
注意：此欄位可能返回 null，表示取不到有效值。
        :type NewFlag: int
        """
        self.InstanceId = None
        self.InstanceName = None
        self.InstanceState = None
        self.Image = None
        self.SimpleModule = None
        self.Position = None
        self.Internet = None
        self.InstanceTypeConfig = None
        self.CreateTime = None
        self.TagSet = None
        self.LatestOperation = None
        self.LatestOperationState = None
        self.RestrictState = None
        self.SystemDiskSize = None
        self.DataDiskSize = None
        self.UUID = None
        self.PayMode = None
        self.ExpireTime = None
        self.IsolatedTime = None
        self.RenewFlag = None
        self.ExpireState = None
        self.SystemDisk = None
        self.DataDisks = None
        self.NewFlag = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.InstanceState = params.get("InstanceState")
        if params.get("Image") is not None:
            self.Image = Image()
            self.Image._deserialize(params.get("Image"))
        if params.get("SimpleModule") is not None:
            self.SimpleModule = SimpleModule()
            self.SimpleModule._deserialize(params.get("SimpleModule"))
        if params.get("Position") is not None:
            self.Position = Position()
            self.Position._deserialize(params.get("Position"))
        if params.get("Internet") is not None:
            self.Internet = Internet()
            self.Internet._deserialize(params.get("Internet"))
        if params.get("InstanceTypeConfig") is not None:
            self.InstanceTypeConfig = InstanceTypeConfig()
            self.InstanceTypeConfig._deserialize(params.get("InstanceTypeConfig"))
        self.CreateTime = params.get("CreateTime")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.LatestOperation = params.get("LatestOperation")
        self.LatestOperationState = params.get("LatestOperationState")
        self.RestrictState = params.get("RestrictState")
        self.SystemDiskSize = params.get("SystemDiskSize")
        self.DataDiskSize = params.get("DataDiskSize")
        self.UUID = params.get("UUID")
        self.PayMode = params.get("PayMode")
        self.ExpireTime = params.get("ExpireTime")
        self.IsolatedTime = params.get("IsolatedTime")
        self.RenewFlag = params.get("RenewFlag")
        self.ExpireState = params.get("ExpireState")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = DiskInfo()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DiskInfo()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        self.NewFlag = params.get("NewFlag")


class InstanceFamilyConfig(AbstractModel):
    """機型族配置

    """

    def __init__(self):
        """
        :param InstanceFamilyName: 機型名稱
        :type InstanceFamilyName: str
        :param InstanceFamily: 機型ID
        :type InstanceFamily: str
        """
        self.InstanceFamilyName = None
        self.InstanceFamily = None


    def _deserialize(self, params):
        self.InstanceFamilyName = params.get("InstanceFamilyName")
        self.InstanceFamily = params.get("InstanceFamily")


class InstanceFamilyTypeConfig(AbstractModel):
    """實例系列類型配置

    """

    def __init__(self):
        """
        :param InstanceFamilyType: 實例機型系列類型Id
        :type InstanceFamilyType: str
        :param InstanceFamilyTypeName: 實例機型系列類型名稱
        :type InstanceFamilyTypeName: str
        """
        self.InstanceFamilyType = None
        self.InstanceFamilyTypeName = None


    def _deserialize(self, params):
        self.InstanceFamilyType = params.get("InstanceFamilyType")
        self.InstanceFamilyTypeName = params.get("InstanceFamilyTypeName")


class InstanceOperator(AbstractModel):
    """實例可執行操作

    """

    def __init__(self):
        """
        :param InstanceId: 實例id
        :type InstanceId: str
        :param DeniedActions: 實例禁止的操作
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeniedActions: list of OperatorAction
        """
        self.InstanceId = None
        self.DeniedActions = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("DeniedActions") is not None:
            self.DeniedActions = []
            for item in params.get("DeniedActions"):
                obj = OperatorAction()
                obj._deserialize(item)
                self.DeniedActions.append(obj)


class InstanceTypeConfig(AbstractModel):
    """機型配置

    """

    def __init__(self):
        """
        :param InstanceFamilyConfig: 機型族配置訊息
        :type InstanceFamilyConfig: :class:`tencentcloud.ecm.v20190719.models.InstanceFamilyConfig`
        :param InstanceType: 機型
        :type InstanceType: str
        :param Vcpu: CPU核數
        :type Vcpu: int
        :param Memory: 内存大小
        :type Memory: int
        :param Frequency: 主頻
        :type Frequency: str
        :param CpuModelName: 處理器型号
        :type CpuModelName: str
        :param InstanceFamilyTypeConfig: 機型族類别配置訊息
        :type InstanceFamilyTypeConfig: :class:`tencentcloud.ecm.v20190719.models.InstanceFamilyTypeConfig`
        :param ExtInfo: 機型額外訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type ExtInfo: str
        """
        self.InstanceFamilyConfig = None
        self.InstanceType = None
        self.Vcpu = None
        self.Memory = None
        self.Frequency = None
        self.CpuModelName = None
        self.InstanceFamilyTypeConfig = None
        self.ExtInfo = None


    def _deserialize(self, params):
        if params.get("InstanceFamilyConfig") is not None:
            self.InstanceFamilyConfig = InstanceFamilyConfig()
            self.InstanceFamilyConfig._deserialize(params.get("InstanceFamilyConfig"))
        self.InstanceType = params.get("InstanceType")
        self.Vcpu = params.get("Vcpu")
        self.Memory = params.get("Memory")
        self.Frequency = params.get("Frequency")
        self.CpuModelName = params.get("CpuModelName")
        if params.get("InstanceFamilyTypeConfig") is not None:
            self.InstanceFamilyTypeConfig = InstanceFamilyTypeConfig()
            self.InstanceFamilyTypeConfig._deserialize(params.get("InstanceFamilyTypeConfig"))
        self.ExtInfo = params.get("ExtInfo")


class Internet(AbstractModel):
    """實例的網絡相關訊息。

    """

    def __init__(self):
        """
        :param PrivateIPAddressSet: 實例的内網相關訊息清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PrivateIPAddressSet: list of PrivateIPAddressInfo
        :param PublicIPAddressSet: 實例的公網相關訊息清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PublicIPAddressSet: list of PublicIPAddressInfo
        """
        self.PrivateIPAddressSet = None
        self.PublicIPAddressSet = None


    def _deserialize(self, params):
        if params.get("PrivateIPAddressSet") is not None:
            self.PrivateIPAddressSet = []
            for item in params.get("PrivateIPAddressSet"):
                obj = PrivateIPAddressInfo()
                obj._deserialize(item)
                self.PrivateIPAddressSet.append(obj)
        if params.get("PublicIPAddressSet") is not None:
            self.PublicIPAddressSet = []
            for item in params.get("PublicIPAddressSet"):
                obj = PublicIPAddressInfo()
                obj._deserialize(item)
                self.PublicIPAddressSet.append(obj)


class Ipv6Address(AbstractModel):
    """IPv6網址訊息。

    """

    def __init__(self):
        """
        :param Address: IPv6網址，形如：3402:4e00:20:100:0:8cd9:2a67:71f3
        :type Address: str
        :param Primary: 是否是主IP。
        :type Primary: bool
        :param AddressId: EIP實例ID，形如：eip-hxlqja90。
        :type AddressId: str
        :param Description: 描述訊息。
        :type Description: str
        :param IsWanIpBlocked: 公網IP是否被封堵。
        :type IsWanIpBlocked: bool
        :param State: IPv6網址狀态：
PENDING：生産中
MIGRATING：遷移中
DELETING：删除中
AVAILABLE：可用的
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


class MigrateNetworkInterfaceRequest(AbstractModel):
    """MigrateNetworkInterface請求參數結構體

    """

    def __init__(self):
        """
        :param EcmRegion: ECM 地域
        :type EcmRegion: str
        :param NetworkInterfaceId: 彈性網卡實例ID，例如：eni-m6dyj72l。
        :type NetworkInterfaceId: str
        :param SourceInstanceId: 彈性網卡當前綁定的ECM實例ID。形如：ein-r8hr2upy。
        :type SourceInstanceId: str
        :param DestinationInstanceId: 待遷移的目的ECM實例ID。
        :type DestinationInstanceId: str
        """
        self.EcmRegion = None
        self.NetworkInterfaceId = None
        self.SourceInstanceId = None
        self.DestinationInstanceId = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
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
        :param EcmRegion: ECM 地域
        :type EcmRegion: str
        :param SourceNetworkInterfaceId: 當内網IP綁定的彈性網卡實例ID，例如：eni-11112222。
        :type SourceNetworkInterfaceId: str
        :param DestinationNetworkInterfaceId: 待遷移的目的彈性網卡實例ID。
        :type DestinationNetworkInterfaceId: str
        :param PrivateIpAddress: 遷移的内網IP網址，例如：10.0.0.6。
        :type PrivateIpAddress: str
        """
        self.EcmRegion = None
        self.SourceNetworkInterfaceId = None
        self.DestinationNetworkInterfaceId = None
        self.PrivateIpAddress = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
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
        :param EcmRegion: ECM 地域
        :type EcmRegion: str
        :param AddressId: 标識 EIP 的唯一 ID。EIP 唯一 ID 形如：eip-11112222。
        :type AddressId: str
        :param AddressName: 修改後的 EIP 名稱。長度上限爲20個字元。
        :type AddressName: str
        :param EipDirectConnection: 設定EIP是否直通，"TRUE"表示直通，"FALSE"表示非直通。注意該參數僅對EIP直通功能可見的用戶可以設定。
        :type EipDirectConnection: str
        """
        self.EcmRegion = None
        self.AddressId = None
        self.AddressName = None
        self.EipDirectConnection = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
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


class ModifyAddressesBandwidthRequest(AbstractModel):
    """ModifyAddressesBandwidth請求參數結構體

    """

    def __init__(self):
        """
        :param EcmRegion: ECM 地域
        :type EcmRegion: str
        :param AddressIds: EIP唯一标識ID，形如'eip-xxxxxxx'
        :type AddressIds: list of str
        :param InternetMaxBandwidthOut: 調整頻寬目标值
        :type InternetMaxBandwidthOut: int
        """
        self.EcmRegion = None
        self.AddressIds = None
        self.InternetMaxBandwidthOut = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.AddressIds = params.get("AddressIds")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")


class ModifyAddressesBandwidthResponse(AbstractModel):
    """ModifyAddressesBandwidth返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步任務TaskId。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyInstancesAttributeRequest(AbstractModel):
    """ModifyInstancesAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIdSet: 待修改的實例ID清單。在單次請求的過程中，請求實例數上限爲100。
        :type InstanceIdSet: list of str
        :param InstanceName: 修改成功後顯示的實例名稱，不得超過60個字元，不傳則名稱顯示爲空。
        :type InstanceName: str
        """
        self.InstanceIdSet = None
        self.InstanceName = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.InstanceName = params.get("InstanceName")


class ModifyInstancesAttributeResponse(AbstractModel):
    """ModifyInstancesAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyModuleImageRequest(AbstractModel):
    """ModifyModuleImage請求參數結構體

    """

    def __init__(self):
        """
        :param DefaultImageId: 預設映像ID
        :type DefaultImageId: str
        :param ModuleId: 模組ID
        :type ModuleId: str
        """
        self.DefaultImageId = None
        self.ModuleId = None


    def _deserialize(self, params):
        self.DefaultImageId = params.get("DefaultImageId")
        self.ModuleId = params.get("ModuleId")


class ModifyModuleImageResponse(AbstractModel):
    """ModifyModuleImage返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyModuleNameRequest(AbstractModel):
    """ModifyModuleName請求參數結構體

    """

    def __init__(self):
        """
        :param ModuleId: 模組ID。
        :type ModuleId: str
        :param ModuleName: 模組名稱。
        :type ModuleName: str
        """
        self.ModuleId = None
        self.ModuleName = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        self.ModuleName = params.get("ModuleName")


class ModifyModuleNameResponse(AbstractModel):
    """ModifyModuleName返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyModuleNetworkRequest(AbstractModel):
    """ModifyModuleNetwork請求參數結構體

    """

    def __init__(self):
        """
        :param ModuleId: 模組Id
        :type ModuleId: str
        :param DefaultBandwidth: 預設頻寬上限
        :type DefaultBandwidth: int
        """
        self.ModuleId = None
        self.DefaultBandwidth = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        self.DefaultBandwidth = params.get("DefaultBandwidth")


class ModifyModuleNetworkResponse(AbstractModel):
    """ModifyModuleNetwork返回參數結構體

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
        :param EcmRegion: ECM 地域
        :type EcmRegion: str
        :param SubnetName: 子網名稱，最大長度不能超過60個位元。
        :type SubnetName: str
        :param EnableBroadcast: 子網是否開啓廣播。
        :type EnableBroadcast: str
        """
        self.SubnetId = None
        self.EcmRegion = None
        self.SubnetName = None
        self.EnableBroadcast = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.EcmRegion = params.get("EcmRegion")
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
        :param VpcId: VPC實例ID。形如：vpc-f49l6u0z。
        :type VpcId: str
        :param EcmRegion: ECM 地域
        :type EcmRegion: str
        :param VpcName: 私有網絡名稱，可任意命名，但不得超過60個字元。
        :type VpcName: str
        """
        self.VpcId = None
        self.EcmRegion = None
        self.VpcName = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.EcmRegion = params.get("EcmRegion")
        self.VpcName = params.get("VpcName")


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


class Module(AbstractModel):
    """模組訊息

    """

    def __init__(self):
        """
        :param ModuleId: 模組Id
        :type ModuleId: str
        :param ModuleName: 模組名稱
        :type ModuleName: str
        :param ModuleState: 模組狀态：
NORMAL：正常
DELETING：删除中 
DELETEFAILED：删除失敗
        :type ModuleState: str
        :param DefaultSystemDiskSize: 預設系統盤大小
        :type DefaultSystemDiskSize: int
        :param DefaultDataDiskSize: 預設數據盤大小
        :type DefaultDataDiskSize: int
        :param InstanceTypeConfig: 預設機型
        :type InstanceTypeConfig: :class:`tencentcloud.ecm.v20190719.models.InstanceTypeConfig`
        :param DefaultImage: 預設映像
        :type DefaultImage: :class:`tencentcloud.ecm.v20190719.models.Image`
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param DefaultBandwidth: 預設頻寬
        :type DefaultBandwidth: int
        """
        self.ModuleId = None
        self.ModuleName = None
        self.ModuleState = None
        self.DefaultSystemDiskSize = None
        self.DefaultDataDiskSize = None
        self.InstanceTypeConfig = None
        self.DefaultImage = None
        self.CreateTime = None
        self.DefaultBandwidth = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        self.ModuleName = params.get("ModuleName")
        self.ModuleState = params.get("ModuleState")
        self.DefaultSystemDiskSize = params.get("DefaultSystemDiskSize")
        self.DefaultDataDiskSize = params.get("DefaultDataDiskSize")
        if params.get("InstanceTypeConfig") is not None:
            self.InstanceTypeConfig = InstanceTypeConfig()
            self.InstanceTypeConfig._deserialize(params.get("InstanceTypeConfig"))
        if params.get("DefaultImage") is not None:
            self.DefaultImage = Image()
            self.DefaultImage._deserialize(params.get("DefaultImage"))
        self.CreateTime = params.get("CreateTime")
        self.DefaultBandwidth = params.get("DefaultBandwidth")


class ModuleCounter(AbstractModel):
    """節點統計數據

    """

    def __init__(self):
        """
        :param ISPCounterSet: 運營商統計訊息清單
        :type ISPCounterSet: list of ISPCounter
        :param ProvinceNum: 省份數量
        :type ProvinceNum: int
        :param CityNum: 城市數量
        :type CityNum: int
        :param NodeNum: 節點數量
        :type NodeNum: int
        :param InstanceNum: 實例數量
        :type InstanceNum: int
        """
        self.ISPCounterSet = None
        self.ProvinceNum = None
        self.CityNum = None
        self.NodeNum = None
        self.InstanceNum = None


    def _deserialize(self, params):
        if params.get("ISPCounterSet") is not None:
            self.ISPCounterSet = []
            for item in params.get("ISPCounterSet"):
                obj = ISPCounter()
                obj._deserialize(item)
                self.ISPCounterSet.append(obj)
        self.ProvinceNum = params.get("ProvinceNum")
        self.CityNum = params.get("CityNum")
        self.NodeNum = params.get("NodeNum")
        self.InstanceNum = params.get("InstanceNum")


class ModuleItem(AbstractModel):
    """模組清單Item訊息

    """

    def __init__(self):
        """
        :param NodeInstanceNum: 節點實例統計訊息
        :type NodeInstanceNum: :class:`tencentcloud.ecm.v20190719.models.NodeInstanceNum`
        :param Module: 模組訊息
        :type Module: :class:`tencentcloud.ecm.v20190719.models.Module`
        """
        self.NodeInstanceNum = None
        self.Module = None


    def _deserialize(self, params):
        if params.get("NodeInstanceNum") is not None:
            self.NodeInstanceNum = NodeInstanceNum()
            self.NodeInstanceNum._deserialize(params.get("NodeInstanceNum"))
        if params.get("Module") is not None:
            self.Module = Module()
            self.Module._deserialize(params.get("Module"))


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
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupSet: list of str
        :param Primary: 是否是主網卡。
        :type Primary: bool
        :param MacAddress: MAC網址。
        :type MacAddress: str
        :param State: 彈性網卡狀态：
PENDING：創建中
AVAILABLE：可用的
ATTACHING：綁定中
DETACHING：解綁中
DELETING：删除中
        :type State: str
        :param PrivateIpAddressSet: 内網IP訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PrivateIpAddressSet: list of PrivateIpAddressSpecification
        :param Attachment: 綁定的雲伺服器對象。
注意：此欄位可能返回 null，表示取不到有效值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Attachment: :class:`tencentcloud.ecm.v20190719.models.NetworkInterfaceAttachment`
        :param Zone: 可用區。
        :type Zone: str
        :param CreatedTime: 創建時間。
        :type CreatedTime: str
        :param Ipv6AddressSet: IPv6網址清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Ipv6AddressSet: list of Ipv6Address
        :param TagSet: 标簽鍵值對。
注意：此欄位可能返回 null，表示取不到有效值。
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


class NetworkStorageRange(AbstractModel):
    """網絡硬碟上下限數據

    """

    def __init__(self):
        """
        :param MaxBandwidth: 網絡頻寬上限
        :type MaxBandwidth: int
        :param MaxSystemDiskSize: 數據盤上限
        :type MaxSystemDiskSize: int
        :param MinBandwidth: 網絡頻寬下限
        :type MinBandwidth: int
        :param MinSystemDiskSize: 數據盤下限
        :type MinSystemDiskSize: int
        :param MaxDataDiskSize: 最大數據盤大小
        :type MaxDataDiskSize: int
        :param MinDataDiskSize: 最小數據盤大小
        :type MinDataDiskSize: int
        :param SuggestBandwidth: 建議頻寬
        :type SuggestBandwidth: int
        :param SuggestDataDiskSize: 建議硬碟大小
        :type SuggestDataDiskSize: int
        :param SuggestSystemDiskSize: 建議系統盤大小
        :type SuggestSystemDiskSize: int
        :param MaxVcpu: Cpu核數峰值
        :type MaxVcpu: int
        :param MinVcpu: Cpu核最小值
        :type MinVcpu: int
        :param MaxVcpuPerReq: 單次請求最大cpu核數
        :type MaxVcpuPerReq: int
        :param PerBandwidth: 頻寬步長
        :type PerBandwidth: int
        :param PerDataDisk: 數據盤步長
        :type PerDataDisk: int
        :param MaxModuleNum: 總模組數量
        :type MaxModuleNum: int
        """
        self.MaxBandwidth = None
        self.MaxSystemDiskSize = None
        self.MinBandwidth = None
        self.MinSystemDiskSize = None
        self.MaxDataDiskSize = None
        self.MinDataDiskSize = None
        self.SuggestBandwidth = None
        self.SuggestDataDiskSize = None
        self.SuggestSystemDiskSize = None
        self.MaxVcpu = None
        self.MinVcpu = None
        self.MaxVcpuPerReq = None
        self.PerBandwidth = None
        self.PerDataDisk = None
        self.MaxModuleNum = None


    def _deserialize(self, params):
        self.MaxBandwidth = params.get("MaxBandwidth")
        self.MaxSystemDiskSize = params.get("MaxSystemDiskSize")
        self.MinBandwidth = params.get("MinBandwidth")
        self.MinSystemDiskSize = params.get("MinSystemDiskSize")
        self.MaxDataDiskSize = params.get("MaxDataDiskSize")
        self.MinDataDiskSize = params.get("MinDataDiskSize")
        self.SuggestBandwidth = params.get("SuggestBandwidth")
        self.SuggestDataDiskSize = params.get("SuggestDataDiskSize")
        self.SuggestSystemDiskSize = params.get("SuggestSystemDiskSize")
        self.MaxVcpu = params.get("MaxVcpu")
        self.MinVcpu = params.get("MinVcpu")
        self.MaxVcpuPerReq = params.get("MaxVcpuPerReq")
        self.PerBandwidth = params.get("PerBandwidth")
        self.PerDataDisk = params.get("PerDataDisk")
        self.MaxModuleNum = params.get("MaxModuleNum")


class Node(AbstractModel):
    """節點訊息

    """

    def __init__(self):
        """
        :param ZoneInfo: zone訊息
        :type ZoneInfo: :class:`tencentcloud.ecm.v20190719.models.ZoneInfo`
        :param Country: 國家訊息
        :type Country: :class:`tencentcloud.ecm.v20190719.models.Country`
        :param Area: 區域訊息
        :type Area: :class:`tencentcloud.ecm.v20190719.models.Area`
        :param Province: 省份訊息
        :type Province: :class:`tencentcloud.ecm.v20190719.models.Province`
        :param City: 城市訊息
        :type City: :class:`tencentcloud.ecm.v20190719.models.City`
        :param RegionInfo: Region訊息
        :type RegionInfo: :class:`tencentcloud.ecm.v20190719.models.RegionInfo`
        :param ISPSet: 運營商清單
        :type ISPSet: list of ISP
        :param ISPNum: 運營商數量
        :type ISPNum: int
        """
        self.ZoneInfo = None
        self.Country = None
        self.Area = None
        self.Province = None
        self.City = None
        self.RegionInfo = None
        self.ISPSet = None
        self.ISPNum = None


    def _deserialize(self, params):
        if params.get("ZoneInfo") is not None:
            self.ZoneInfo = ZoneInfo()
            self.ZoneInfo._deserialize(params.get("ZoneInfo"))
        if params.get("Country") is not None:
            self.Country = Country()
            self.Country._deserialize(params.get("Country"))
        if params.get("Area") is not None:
            self.Area = Area()
            self.Area._deserialize(params.get("Area"))
        if params.get("Province") is not None:
            self.Province = Province()
            self.Province._deserialize(params.get("Province"))
        if params.get("City") is not None:
            self.City = City()
            self.City._deserialize(params.get("City"))
        if params.get("RegionInfo") is not None:
            self.RegionInfo = RegionInfo()
            self.RegionInfo._deserialize(params.get("RegionInfo"))
        if params.get("ISPSet") is not None:
            self.ISPSet = []
            for item in params.get("ISPSet"):
                obj = ISP()
                obj._deserialize(item)
                self.ISPSet.append(obj)
        self.ISPNum = params.get("ISPNum")


class NodeInstanceNum(AbstractModel):
    """節點實例數量訊息

    """

    def __init__(self):
        """
        :param NodeNum: 節點數量
        :type NodeNum: int
        :param InstanceNum: 實例數量
        :type InstanceNum: int
        """
        self.NodeNum = None
        self.InstanceNum = None


    def _deserialize(self, params):
        self.NodeNum = params.get("NodeNum")
        self.InstanceNum = params.get("InstanceNum")


class OperatorAction(AbstractModel):
    """操作Action

    """

    def __init__(self):
        """
        :param Action: 可執行操作
        :type Action: str
        :param Code: 編碼Code
注意：此欄位可能返回 null，表示取不到有效值。
        :type Code: str
        :param Message: 具體訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self.Action = None
        self.Code = None
        self.Message = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.Code = params.get("Code")
        self.Message = params.get("Message")


class PeakBase(AbstractModel):
    """峰值訊息

    """

    def __init__(self):
        """
        :param PeakCpuNum: CPU峰值
        :type PeakCpuNum: int
        :param PeakMemoryNum: 内存峰值
        :type PeakMemoryNum: int
        :param PeakStorageNum: 硬碟峰值
        :type PeakStorageNum: int
        :param RecordTime: 記錄時間
        :type RecordTime: str
        """
        self.PeakCpuNum = None
        self.PeakMemoryNum = None
        self.PeakStorageNum = None
        self.RecordTime = None


    def _deserialize(self, params):
        self.PeakCpuNum = params.get("PeakCpuNum")
        self.PeakMemoryNum = params.get("PeakMemoryNum")
        self.PeakStorageNum = params.get("PeakStorageNum")
        self.RecordTime = params.get("RecordTime")


class PeakFamilyInfo(AbstractModel):
    """PeakFamilyInfo 按機型類别分類的cpu等數據的峰值訊息

    """

    def __init__(self):
        """
        :param InstanceFamily: 機型類别訊息。
        :type InstanceFamily: :class:`tencentcloud.ecm.v20190719.models.InstanceFamilyTypeConfig`
        :param PeakBaseSet: 基礎數據峰值訊息。
        :type PeakBaseSet: list of PeakBase
        """
        self.InstanceFamily = None
        self.PeakBaseSet = None


    def _deserialize(self, params):
        if params.get("InstanceFamily") is not None:
            self.InstanceFamily = InstanceFamilyTypeConfig()
            self.InstanceFamily._deserialize(params.get("InstanceFamily"))
        if params.get("PeakBaseSet") is not None:
            self.PeakBaseSet = []
            for item in params.get("PeakBaseSet"):
                obj = PeakBase()
                obj._deserialize(item)
                self.PeakBaseSet.append(obj)


class PeakNetwork(AbstractModel):
    """峰值網絡數據

    """

    def __init__(self):
        """
        :param RecordTime: 記錄時間。
        :type RecordTime: str
        :param PeakInNetwork: 入頻寬數據。
        :type PeakInNetwork: str
        :param PeakOutNetwork: 出頻寬數據。
        :type PeakOutNetwork: str
        """
        self.RecordTime = None
        self.PeakInNetwork = None
        self.PeakOutNetwork = None


    def _deserialize(self, params):
        self.RecordTime = params.get("RecordTime")
        self.PeakInNetwork = params.get("PeakInNetwork")
        self.PeakOutNetwork = params.get("PeakOutNetwork")


class PeakNetworkRegionInfo(AbstractModel):
    """region維度的網絡峰值訊息

    """

    def __init__(self):
        """
        :param Region: region訊息
        :type Region: str
        :param PeakNetworkSet: 網絡峰值集合
注意：此欄位可能返回 null，表示取不到有效值。
        :type PeakNetworkSet: list of PeakNetwork
        """
        self.Region = None
        self.PeakNetworkSet = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        if params.get("PeakNetworkSet") is not None:
            self.PeakNetworkSet = []
            for item in params.get("PeakNetworkSet"):
                obj = PeakNetwork()
                obj._deserialize(item)
                self.PeakNetworkSet.append(obj)


class Position(AbstractModel):
    """描述實例的位置相關訊息。

    """

    def __init__(self):
        """
        :param ZoneInfo: 實例所在的Zone的訊息。
        :type ZoneInfo: :class:`tencentcloud.ecm.v20190719.models.ZoneInfo`
        :param Country: 實例所在的國家的訊息。
        :type Country: :class:`tencentcloud.ecm.v20190719.models.Country`
        :param Area: 實例所在的Area的訊息。
        :type Area: :class:`tencentcloud.ecm.v20190719.models.Area`
        :param Province: 實例所在的省份的訊息。
        :type Province: :class:`tencentcloud.ecm.v20190719.models.Province`
        :param City: 實例所在的城市的訊息。
        :type City: :class:`tencentcloud.ecm.v20190719.models.City`
        :param RegionInfo: 實例所在的Region的訊息。
        :type RegionInfo: :class:`tencentcloud.ecm.v20190719.models.RegionInfo`
        """
        self.ZoneInfo = None
        self.Country = None
        self.Area = None
        self.Province = None
        self.City = None
        self.RegionInfo = None


    def _deserialize(self, params):
        if params.get("ZoneInfo") is not None:
            self.ZoneInfo = ZoneInfo()
            self.ZoneInfo._deserialize(params.get("ZoneInfo"))
        if params.get("Country") is not None:
            self.Country = Country()
            self.Country._deserialize(params.get("Country"))
        if params.get("Area") is not None:
            self.Area = Area()
            self.Area._deserialize(params.get("Area"))
        if params.get("Province") is not None:
            self.Province = Province()
            self.Province._deserialize(params.get("Province"))
        if params.get("City") is not None:
            self.City = City()
            self.City._deserialize(params.get("City"))
        if params.get("RegionInfo") is not None:
            self.RegionInfo = RegionInfo()
            self.RegionInfo._deserialize(params.get("RegionInfo"))


class PrivateIPAddressInfo(AbstractModel):
    """實例的内網ip相關訊息。

    """

    def __init__(self):
        """
        :param PrivateIPAddress: 實例的内網ip。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PrivateIPAddress: str
        """
        self.PrivateIPAddress = None


    def _deserialize(self, params):
        self.PrivateIPAddress = params.get("PrivateIPAddress")


class PrivateIpAddressSpecification(AbstractModel):
    """内網IP訊息

    """

    def __init__(self):
        """
        :param PrivateIpAddress: 内網IP網址。
        :type PrivateIpAddress: str
        :param Primary: 是否是主IP。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Primary: bool
        :param PublicIpAddress: 公網IP網址。
        :type PublicIpAddress: str
        :param AddressId: EIP實例ID，例如：eip-11112222。
        :type AddressId: str
        :param Description: 内網IP描述訊息。
        :type Description: str
        :param IsWanIpBlocked: 公網IP是否被封堵。
注意：此欄位可能返回 null，表示取不到有效值。
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


class Province(AbstractModel):
    """省份訊息

    """

    def __init__(self):
        """
        :param ProvinceId: 省份Id
        :type ProvinceId: str
        :param ProvinceName: 省份名稱
        :type ProvinceName: str
        """
        self.ProvinceId = None
        self.ProvinceName = None


    def _deserialize(self, params):
        self.ProvinceId = params.get("ProvinceId")
        self.ProvinceName = params.get("ProvinceName")


class PublicIPAddressInfo(AbstractModel):
    """實例的公網ip相關訊息。

    """

    def __init__(self):
        """
        :param ChargeMode: 計費模式。
        :type ChargeMode: str
        :param PublicIPAddress: 實例的公網ip。
        :type PublicIPAddress: str
        :param ISP: 實例的公網ip所屬的運營商。
        :type ISP: :class:`tencentcloud.ecm.v20190719.models.ISP`
        :param MaxBandwidthOut: 實例的最大出頻寬上限。
        :type MaxBandwidthOut: int
        """
        self.ChargeMode = None
        self.PublicIPAddress = None
        self.ISP = None
        self.MaxBandwidthOut = None


    def _deserialize(self, params):
        self.ChargeMode = params.get("ChargeMode")
        self.PublicIPAddress = params.get("PublicIPAddress")
        if params.get("ISP") is not None:
            self.ISP = ISP()
            self.ISP._deserialize(params.get("ISP"))
        self.MaxBandwidthOut = params.get("MaxBandwidthOut")


class RebootInstancesRequest(AbstractModel):
    """RebootInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIdSet: 待重啓的實例ID清單。在單次請求的過程中，單個region下的請求實例數上限爲100。
        :type InstanceIdSet: list of str
        :param ForceReboot: 是否在正常重啓失敗後選擇強制重啓實例。取值範圍：
TRUE：表示在正常重啓失敗後進行強制重啓；
FALSE：表示在正常重啓失敗後不進行強制重啓；
預設取值：FALSE。
        :type ForceReboot: bool
        :param StopType: 關機類型。取值範圍：
SOFT：表示軟關機
HARD：表示硬關機
SOFT_FIRST：表示優先軟關機，失敗再執行硬關機

預設取值：SOFT。
        :type StopType: str
        """
        self.InstanceIdSet = None
        self.ForceReboot = None
        self.StopType = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.ForceReboot = params.get("ForceReboot")
        self.StopType = params.get("StopType")


class RebootInstancesResponse(AbstractModel):
    """RebootInstances返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """Region和RegionName

    """

    def __init__(self):
        """
        :param Region: Region
        :type Region: str
        :param RegionName: Region名稱
        :type RegionName: str
        :param RegionId: RegionID
        :type RegionId: int
        """
        self.Region = None
        self.RegionName = None
        self.RegionId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionId = params.get("RegionId")


class ReleaseAddressesRequest(AbstractModel):
    """ReleaseAddresses請求參數結構體

    """

    def __init__(self):
        """
        :param EcmRegion: ECM 地域
        :type EcmRegion: str
        :param AddressIds: 标識 EIP 的唯一 ID 清單。
        :type AddressIds: list of str
        """
        self.EcmRegion = None
        self.AddressIds = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.AddressIds = params.get("AddressIds")


class ReleaseAddressesResponse(AbstractModel):
    """ReleaseAddresses返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步任務TaskId。可以使用DescribeTaskResult介面查詢任務狀态。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class RemovePrivateIpAddressesRequest(AbstractModel):
    """RemovePrivateIpAddresses請求參數結構體

    """

    def __init__(self):
        """
        :param EcmRegion: ECM 地域。
        :type EcmRegion: str
        :param NetworkInterfaceId: 彈性網卡實例ID，例如：eni-11112222。
        :type NetworkInterfaceId: str
        :param PrivateIpAddresses: 指定的内網IP訊息，單次最多指定10個。
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        """
        self.EcmRegion = None
        self.NetworkInterfaceId = None
        self.PrivateIpAddresses = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("PrivateIpAddresses") is not None:
            self.PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self.PrivateIpAddresses.append(obj)


class RemovePrivateIpAddressesResponse(AbstractModel):
    """RemovePrivateIpAddresses返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetInstancesMaxBandwidthRequest(AbstractModel):
    """ResetInstancesMaxBandwidth請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIdSet: 待重置頻寬上限的實例ID清單。在單次請求的過程中，單個region下的請求實例數上限爲100。
        :type InstanceIdSet: list of str
        :param MaxBandwidthOut: 修改後的最大頻寬上限。
        :type MaxBandwidthOut: int
        """
        self.InstanceIdSet = None
        self.MaxBandwidthOut = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.MaxBandwidthOut = params.get("MaxBandwidthOut")


class ResetInstancesMaxBandwidthResponse(AbstractModel):
    """ResetInstancesMaxBandwidth返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetInstancesPasswordRequest(AbstractModel):
    """ResetInstancesPassword請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIdSet: 待重置密碼的實例ID清單。在單次請求的過程中，單個region下的請求實例數上限爲100。
        :type InstanceIdSet: list of str
        :param Password: 新密碼，Linux實例密碼必須8到16位，至少包括兩項[a-z，A-Z]、[0-9]和[( ) ~ ~ ! @ # $ % ^ & * - + = _ | { } [ ] : ; ' < > , . ? /]中的符号。密碼不允許以/符号開頭。
Windows實例密碼必須12到16位，至少包括三項[a-z]，[A-Z]，[0-9]和[( ) ~ ~ ! @ # $ % ^ & * - + = _ | { } [ ] : ; ' < > , . ? /]中的符号。密碼不允許以/符号開頭。
如果實例即包含Linux實例又包含Windows實例，則密碼複雜度限制按照Windows實例的限制。
        :type Password: str
        :param ForceStop: 是否強制關機，預設爲false。
        :type ForceStop: bool
        :param UserName: 待重置密碼的實例的用戶名，不得超過64個字元。若未指定用戶名，則對于Linux而言，預設重置root用戶的密碼，對于Windows而言，預設重置administrator的密碼。
        :type UserName: str
        """
        self.InstanceIdSet = None
        self.Password = None
        self.ForceStop = None
        self.UserName = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.Password = params.get("Password")
        self.ForceStop = params.get("ForceStop")
        self.UserName = params.get("UserName")


class ResetInstancesPasswordResponse(AbstractModel):
    """ResetInstancesPassword返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetInstancesRequest(AbstractModel):
    """ResetInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIdSet: 待重裝的實例ID清單。
        :type InstanceIdSet: list of str
        :param ImageId: 重裝使用的映像ID，若未指定，則使用各個實例當前的映像進行重裝。
        :type ImageId: str
        :param Password: 密碼設置，若未指定，則後續将以站内信的形式通知密碼。
        :type Password: str
        :param EnhancedService: 是否開啓雲監控和雲鏡服務，未指定時預設開啓。
        :type EnhancedService: :class:`tencentcloud.ecm.v20190719.models.EnhancedService`
        """
        self.InstanceIdSet = None
        self.ImageId = None
        self.Password = None
        self.EnhancedService = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.ImageId = params.get("ImageId")
        self.Password = params.get("Password")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))


class ResetInstancesResponse(AbstractModel):
    """ResetInstances返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RunInstancesRequest(AbstractModel):
    """RunInstances請求參數結構體

    """

    def __init__(self):
        """
        :param ZoneInstanceCountISPSet: 需要創建實例的可用區及創建數目及運營商的清單。在單次請求的過程中，單個region下的請求創建實例數上限爲100
        :type ZoneInstanceCountISPSet: list of ZoneInstanceCountISP
        :param ModuleId: 模組ID
        :type ModuleId: str
        :param Password: 實例登入密碼。不同作業系統類型密碼複雜度限制不一樣，具體如下：
Linux實例密碼必須8到30位，至少包括兩項[a-z]，[A-Z]、[0-9] 和 [( ) ` ~ ! @ # $ % ^ & - + = | { } [ ] : ; ' , . ? / ]中的特殊符。Windows實例密碼必須12到30位，至少包括三項[a-z]，[A-Z]，[0-9] 和 [( ) ` ~ ! @ # $ % ^ & - + = | { } [ ] : ; ' , . ? /]中的特殊符号。
        :type Password: str
        :param InternetMaxBandwidthOut: 公網出頻寬上限，單位：Mbps
        :type InternetMaxBandwidthOut: int
        :param ImageId: 映像ID，不傳則使用模組下的預設值
        :type ImageId: str
        :param InstanceName: 實例顯示名稱。
不指定實例顯示名稱則預設顯示‘未命名’。
購買多台實例，如果指定模式串{R:x}，表示生成數字[x, x+n-1]，其中n表示購買實例的數量，例如server\_{R:3}，購買1台時，實例顯示名稱爲server\_3；購買2台時，實例顯示名稱分别爲server\_3，server\_4。
支援指定多個模式串{R:x}。
購買多台實例，如果不指定模式串，則在實例顯示名稱添加後綴1、2...n，其中n表示購買實例的數量，例如server_，購買2台時，實例顯示名稱分别爲server\_1，server\_2。
如果購買的實例屬于不同的地域或運營商，則上述規則在每個地域和運營商内獨立計數。
最多支援60個字元（包含模式串）。
        :type InstanceName: str
        :param HostName: 主機名稱
點号（.）和短橫線（-）不能作爲 HostName 的首尾字元，不能連續使用。
Windows 實例：名字元長度爲[2, 15]，允許字母（不限制大小寫）、數字和短橫線（-）組成，不支援點号（.），不能全是數字。
其他類型（Linux 等）實例：字元長度爲[2, 60]，允許支援多個點号，點之間爲一段，每段允許字母（不限制大小寫）、數字和短橫線（-）組成。
        :type HostName: str
        :param ClientToken: 用于保證請求幂等性的字串。目前爲保留參數，請勿使用。
        :type ClientToken: str
        :param EnhancedService: 增強服務。通過該參數可以指定是否開啓雲安全、雲監控等服務。若不指定該參數，則預設公共映像開啓雲監控、雲安全服務
        :type EnhancedService: :class:`tencentcloud.ecm.v20190719.models.EnhancedService`
        :param TagSpecification: 标簽清單
        :type TagSpecification: list of TagSpecification
        :param UserData: 提供給實例使用的用戶數據，需要以 base64 方式編碼，支援的最大數據大小爲 16KB
        :type UserData: str
        """
        self.ZoneInstanceCountISPSet = None
        self.ModuleId = None
        self.Password = None
        self.InternetMaxBandwidthOut = None
        self.ImageId = None
        self.InstanceName = None
        self.HostName = None
        self.ClientToken = None
        self.EnhancedService = None
        self.TagSpecification = None
        self.UserData = None


    def _deserialize(self, params):
        if params.get("ZoneInstanceCountISPSet") is not None:
            self.ZoneInstanceCountISPSet = []
            for item in params.get("ZoneInstanceCountISPSet"):
                obj = ZoneInstanceCountISP()
                obj._deserialize(item)
                self.ZoneInstanceCountISPSet.append(obj)
        self.ModuleId = params.get("ModuleId")
        self.Password = params.get("Password")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.ImageId = params.get("ImageId")
        self.InstanceName = params.get("InstanceName")
        self.HostName = params.get("HostName")
        self.ClientToken = params.get("ClientToken")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        self.UserData = params.get("UserData")


class RunInstancesResponse(AbstractModel):
    """RunInstances返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceIdSet: 創建中的實例ID清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceIdSet: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.RequestId = params.get("RequestId")


class RunMonitorServiceEnabled(AbstractModel):
    """雲監控服務

    """

    def __init__(self):
        """
        :param Enabled: 是否開啓。
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")


class RunSecurityServiceEnabled(AbstractModel):
    """雲鏡服務；

    """

    def __init__(self):
        """
        :param Enabled: 是否開啓。
        :type Enabled: bool
        :param Version: 雲鏡版本：0 基礎版，1 專業版。目前僅支援基礎版
        :type Version: int
        """
        self.Enabled = None
        self.Version = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.Version = params.get("Version")


class SimpleModule(AbstractModel):
    """Module的簡要訊息

    """

    def __init__(self):
        """
        :param ModuleId: 模組ID
        :type ModuleId: str
        :param ModuleName: 模組名稱
        :type ModuleName: str
        """
        self.ModuleId = None
        self.ModuleName = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        self.ModuleName = params.get("ModuleName")


class SrcImage(AbstractModel):
    """映像來源訊息

    """

    def __init__(self):
        """
        :param ImageId: 映像id
        :type ImageId: str
        :param ImageName: 映像名稱
        :type ImageName: str
        :param ImageOsName: 系統名稱
        :type ImageOsName: str
        :param ImageDescription: 映像描述
        :type ImageDescription: str
        :param Region: 區域
        :type Region: str
        :param RegionID: 區域ID
        :type RegionID: int
        :param RegionName: 區域名稱
        :type RegionName: str
        """
        self.ImageId = None
        self.ImageName = None
        self.ImageOsName = None
        self.ImageDescription = None
        self.Region = None
        self.RegionID = None
        self.RegionName = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.ImageName = params.get("ImageName")
        self.ImageOsName = params.get("ImageOsName")
        self.ImageDescription = params.get("ImageDescription")
        self.Region = params.get("Region")
        self.RegionID = params.get("RegionID")
        self.RegionName = params.get("RegionName")


class StartInstancesRequest(AbstractModel):
    """StartInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIdSet: 待開啓的實例ID清單。在單次請求的過程中，單個region下的請求實例數上限爲100。
        :type InstanceIdSet: list of str
        """
        self.InstanceIdSet = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")


class StartInstancesResponse(AbstractModel):
    """StartInstances返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopInstancesRequest(AbstractModel):
    """StopInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIdSet: 需要關機的實例ID清單。在單次請求的過程中，單個region下的請求實例數上限爲100。
        :type InstanceIdSet: list of str
        :param ForceStop: 是否在正常關閉失敗後選擇強制關閉實例，預設爲false，即否。
        :type ForceStop: bool
        :param StopType: 實例的關閉模式。取值範圍：
SOFT_FIRST：表示在正常關閉失敗後進行強制關閉;
HARD：直接強制關閉;
SOFT：僅軟關機；
預設爲SOFT。
        :type StopType: str
        """
        self.InstanceIdSet = None
        self.ForceStop = None
        self.StopType = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.ForceStop = params.get("ForceStop")
        self.StopType = params.get("StopType")


class StopInstancesResponse(AbstractModel):
    """StopInstances返回參數結構體

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
        :param VpcId: VPC實例ID。
        :type VpcId: str
        :param SubnetId: 子網實例ID，例如：subnet-bthucmmy。
        :type SubnetId: str
        :param SubnetName: 子網名稱。
        :type SubnetName: str
        :param CidrBlock: 子網的 IPv4 CIDR。
        :type CidrBlock: str
        :param IsDefault: 是否預設子網。
        :type IsDefault: bool
        :param EnableBroadcast: 是否開啓廣播。
        :type EnableBroadcast: bool
        :param RouteTableId: 路由表實例ID，例如：rtb-l2h8d7c2。
        :type RouteTableId: str
        :param CreatedTime: 創建時間。
        :type CreatedTime: str
        :param AvailableIpAddressCount: 可用IP數。
        :type AvailableIpAddressCount: int
        :param Ipv6CidrBlock: 子網的 IPv6 CIDR。
        :type Ipv6CidrBlock: str
        :param NetworkAclId: 關聯ACLID
        :type NetworkAclId: str
        :param IsRemoteVpcSnat: 是否爲 SNAT 網址池子網。
        :type IsRemoteVpcSnat: bool
        :param TagSet: 标簽鍵值對。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagSet: list of Tag
        """
        self.VpcId = None
        self.SubnetId = None
        self.SubnetName = None
        self.CidrBlock = None
        self.IsDefault = None
        self.EnableBroadcast = None
        self.RouteTableId = None
        self.CreatedTime = None
        self.AvailableIpAddressCount = None
        self.Ipv6CidrBlock = None
        self.NetworkAclId = None
        self.IsRemoteVpcSnat = None
        self.TagSet = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.CidrBlock = params.get("CidrBlock")
        self.IsDefault = params.get("IsDefault")
        self.EnableBroadcast = params.get("EnableBroadcast")
        self.RouteTableId = params.get("RouteTableId")
        self.CreatedTime = params.get("CreatedTime")
        self.AvailableIpAddressCount = params.get("AvailableIpAddressCount")
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        self.NetworkAclId = params.get("NetworkAclId")
        self.IsRemoteVpcSnat = params.get("IsRemoteVpcSnat")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)


class Tag(AbstractModel):
    """标簽訊息。

    """

    def __init__(self):
        """
        :param Key: 标簽的鍵。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Key: str
        :param Value: 标簽的值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class TagSpecification(AbstractModel):
    """TagSpecification

    """

    def __init__(self):
        """
        :param ResourceType: 資源類型，目前僅支援"instance"
        :type ResourceType: str
        :param Tags: 标簽清單
        :type Tags: list of Tag
        """
        self.ResourceType = None
        self.Tags = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class TerminateInstancesRequest(AbstractModel):
    """TerminateInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIdSet: 待銷毀的實例ID清單。
        :type InstanceIdSet: list of str
        :param TerminateDelay: 是否定時銷毀，預設爲否。
        :type TerminateDelay: bool
        :param TerminateTime: 定時銷毀的時間，格式形如："2019-08-05 12:01:30"，若非定時銷毀，則此參數被忽略。
        :type TerminateTime: str
        """
        self.InstanceIdSet = None
        self.TerminateDelay = None
        self.TerminateTime = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.TerminateDelay = params.get("TerminateDelay")
        self.TerminateTime = params.get("TerminateTime")


class TerminateInstancesResponse(AbstractModel):
    """TerminateInstances返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class VpcInfo(AbstractModel):
    """私有網絡(VPC)對象。

    """

    def __init__(self):
        """
        :param VpcName: VPC名稱。
        :type VpcName: str
        :param VpcId: VPC實例ID，例如：vpc-azd4dt1c。
        :type VpcId: str
        :param CidrBlock: VPC的IPv4 CIDR。
        :type CidrBlock: str
        :param IsDefault: 是否預設VPC。
        :type IsDefault: bool
        :param EnableMulticast: 是否開啓組播。
        :type EnableMulticast: bool
        :param CreatedTime: 創建時間。
        :type CreatedTime: str
        :param DnsServerSet: DNS清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DnsServerSet: list of str
        :param DomainName: DHCP域名選項值。
        :type DomainName: str
        :param DhcpOptionsId: DHCP選項集ID。
        :type DhcpOptionsId: str
        :param EnableDhcp: 是否開啓DHCP。
        :type EnableDhcp: bool
        :param Ipv6CidrBlock: VPC的IPv6 CIDR。
        :type Ipv6CidrBlock: str
        :param TagSet: 标簽鍵值對
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagSet: list of Tag
        :param AssistantCidrSet: 輔助CIDR
注意：此欄位可能返回 null，表示取不到有效值。
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


class ZoneInfo(AbstractModel):
    """Zone訊息

    """

    def __init__(self):
        """
        :param ZoneId: ZoneId
        :type ZoneId: int
        :param ZoneName: ZoneName
        :type ZoneName: str
        :param Zone: Zone
        :type Zone: str
        """
        self.ZoneId = None
        self.ZoneName = None
        self.Zone = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.Zone = params.get("Zone")


class ZoneInstanceCountISP(AbstractModel):
    """實例可用區及對應的實例創建數目及運營商的組合；

    """

    def __init__(self):
        """
        :param Zone: 創建實例的可用區。
        :type Zone: str
        :param InstanceCount: 在當前可用區欲創建的實例數目。
        :type InstanceCount: int
        :param ISP: 運營商。
        :type ISP: str
        """
        self.Zone = None
        self.InstanceCount = None
        self.ISP = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceCount = params.get("InstanceCount")
        self.ISP = params.get("ISP")


class ZoneInstanceInfo(AbstractModel):
    """Zone的實例訊息

    """

    def __init__(self):
        """
        :param ZoneName: Zone名稱
        :type ZoneName: str
        :param InstanceNum: 實例數量
        :type InstanceNum: int
        """
        self.ZoneName = None
        self.InstanceNum = None


    def _deserialize(self, params):
        self.ZoneName = params.get("ZoneName")
        self.InstanceNum = params.get("InstanceNum")