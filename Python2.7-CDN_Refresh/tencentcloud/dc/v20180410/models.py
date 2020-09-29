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


class AcceptDirectConnectTunnelRequest(AbstractModel):
    """AcceptDirectConnectTunnel請求參數結構體

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: 物理專線擁有者接受共享專用通道申請
        :type DirectConnectTunnelId: str
        """
        self.DirectConnectTunnelId = None


    def _deserialize(self, params):
        self.DirectConnectTunnelId = params.get("DirectConnectTunnelId")


class AcceptDirectConnectTunnelResponse(AbstractModel):
    """AcceptDirectConnectTunnel返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AccessPoint(AbstractModel):
    """接入點訊息。

    """

    def __init__(self):
        """
        :param AccessPointName: 接入點的名稱。
        :type AccessPointName: str
        :param AccessPointId: 接入點唯一ID。
        :type AccessPointId: str
        :param State: 接入點的狀态。可用，不可用。
        :type State: str
        :param Location: 接入點的位置。
        :type Location: str
        :param LineOperator: 接入點支援的運營商清單。
        :type LineOperator: list of str
        :param RegionId: 接入點管理的大區ID。
        :type RegionId: str
        """
        self.AccessPointName = None
        self.AccessPointId = None
        self.State = None
        self.Location = None
        self.LineOperator = None
        self.RegionId = None


    def _deserialize(self, params):
        self.AccessPointName = params.get("AccessPointName")
        self.AccessPointId = params.get("AccessPointId")
        self.State = params.get("State")
        self.Location = params.get("Location")
        self.LineOperator = params.get("LineOperator")
        self.RegionId = params.get("RegionId")


class BgpPeer(AbstractModel):
    """bgp參數，包括Asn，AuthKey

    """

    def __init__(self):
        """
        :param Asn: 用戶側，BGP Asn
        :type Asn: int
        :param AuthKey: 用戶側BGP金鑰
        :type AuthKey: str
        """
        self.Asn = None
        self.AuthKey = None


    def _deserialize(self, params):
        self.Asn = params.get("Asn")
        self.AuthKey = params.get("AuthKey")


class CreateDirectConnectRequest(AbstractModel):
    """CreateDirectConnect請求參數結構體

    """

    def __init__(self):
        """
        :param DirectConnectName: 物理專線的名稱。
        :type DirectConnectName: str
        :param AccessPointId: 物理專線所在的接入點。
您可以通過調用 DescribeAccessPoints介面獲取地域ID。所選擇的接入點必須存在且處於可接入的狀态。
        :type AccessPointId: str
        :param LineOperator: 提供接入物理專線的運營商。ChinaTelecom： 電信， ChinaMobile：  ，ChinaUnicom：  ， In-houseWiring：樓内線，ChinaOther： 其他， InternationalOperator：境外其他。
        :type LineOperator: str
        :param Location: 本地數據中心的地理位置。
        :type Location: str
        :param PortType: 物理專線接入端口類型,取值：100Base-T：百兆電介面,1000Base-T（預設值）：千兆電介面,1000Base-LX：千兆單模光介面（10千米）,10GBase-T：萬兆電介面10GBase-LR：萬兆單模光介面（10千米），預設值，千兆單模光介面（10千米）。
        :type PortType: str
        :param CircuitCode: 運營商或者服務商爲物理專線提供的電路編碼。
        :type CircuitCode: str
        :param Bandwidth: 物理專線接入介面頻寬，單位爲Mbps，預設值爲1000，取值範圍爲 [2, 10240]。
        :type Bandwidth: int
        :param RedundantDirectConnectId: 備援物理專線的ID。
        :type RedundantDirectConnectId: str
        :param Vlan: 物理專線調試VLAN。預設開啓VLAN，自動分配VLAN。
        :type Vlan: int
        :param TencentAddress: 物理專線調試 側互聯 IP。預設自動分配。
        :type TencentAddress: str
        :param CustomerAddress: 物理專線調試用戶側互聯 IP。預設自動分配。
        :type CustomerAddress: str
        :param CustomerName: 物理專線申請者姓名。預設從帳戶體系獲取。
        :type CustomerName: str
        :param CustomerContactMail: 物理專線申請者聯系電子信箱。預設從帳戶體系獲取。
        :type CustomerContactMail: str
        :param CustomerContactNumber: 物理專線申請者聯系號碼。預設從帳戶體系獲取。
        :type CustomerContactNumber: str
        :param FaultReportContactPerson: 報障聯系人。
        :type FaultReportContactPerson: str
        :param FaultReportContactNumber: 報障聯系電話。
        :type FaultReportContactNumber: str
        """
        self.DirectConnectName = None
        self.AccessPointId = None
        self.LineOperator = None
        self.Location = None
        self.PortType = None
        self.CircuitCode = None
        self.Bandwidth = None
        self.RedundantDirectConnectId = None
        self.Vlan = None
        self.TencentAddress = None
        self.CustomerAddress = None
        self.CustomerName = None
        self.CustomerContactMail = None
        self.CustomerContactNumber = None
        self.FaultReportContactPerson = None
        self.FaultReportContactNumber = None


    def _deserialize(self, params):
        self.DirectConnectName = params.get("DirectConnectName")
        self.AccessPointId = params.get("AccessPointId")
        self.LineOperator = params.get("LineOperator")
        self.Location = params.get("Location")
        self.PortType = params.get("PortType")
        self.CircuitCode = params.get("CircuitCode")
        self.Bandwidth = params.get("Bandwidth")
        self.RedundantDirectConnectId = params.get("RedundantDirectConnectId")
        self.Vlan = params.get("Vlan")
        self.TencentAddress = params.get("TencentAddress")
        self.CustomerAddress = params.get("CustomerAddress")
        self.CustomerName = params.get("CustomerName")
        self.CustomerContactMail = params.get("CustomerContactMail")
        self.CustomerContactNumber = params.get("CustomerContactNumber")
        self.FaultReportContactPerson = params.get("FaultReportContactPerson")
        self.FaultReportContactNumber = params.get("FaultReportContactNumber")


class CreateDirectConnectResponse(AbstractModel):
    """CreateDirectConnect返回參數結構體

    """

    def __init__(self):
        """
        :param DirectConnectIdSet: 物理專線的ID。
        :type DirectConnectIdSet: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DirectConnectIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DirectConnectIdSet = params.get("DirectConnectIdSet")
        self.RequestId = params.get("RequestId")


class CreateDirectConnectTunnelRequest(AbstractModel):
    """CreateDirectConnectTunnel請求參數結構體

    """

    def __init__(self):
        """
        :param DirectConnectId: 專線 ID，例如：dc-kd7d06of
        :type DirectConnectId: str
        :param DirectConnectTunnelName: 專用通道名稱
        :type DirectConnectTunnelName: str
        :param DirectConnectOwnerAccount: 物理專線 owner，缺省爲當前客戶（物理專線 owner）
共享專線時這裏需要填寫共享專線的開發商賬號 ID
        :type DirectConnectOwnerAccount: str
        :param NetworkType: 網絡類型，分别爲VPC、BMVPC，CCN，預設是VPC
VPC：私有網絡
BMVPC：黑石網絡
CCN：雲聯網
        :type NetworkType: str
        :param NetworkRegion: 網絡地域
        :type NetworkRegion: str
        :param VpcId: 私有網絡統一 ID 或者黑石網絡統一 ID
        :type VpcId: str
        :param DirectConnectGatewayId: 專線閘道 ID，例如 dcg-d545ddf
        :type DirectConnectGatewayId: str
        :param Bandwidth: 專線頻寬，單位：Mbps
預設是物理專線頻寬值
        :type Bandwidth: int
        :param RouteType: BGP ：BGP路由
STATIC：靜态
預設爲 BGP 路由
        :type RouteType: str
        :param BgpPeer: BgpPeer，用戶側bgp訊息，包括Asn和AuthKey
        :type BgpPeer: :class:`taifucloudcloud.dc.v20180410.models.BgpPeer`
        :param RouteFilterPrefixes: 靜态路由，用戶IDC的網段網址
        :type RouteFilterPrefixes: list of RouteFilterPrefix
        :param Vlan: vlan，範圍：0 ~ 3000
0：不開啓子介面
預設值是非0
        :type Vlan: int
        :param TencentAddress: TencentAddress， 側互聯 IP
        :type TencentAddress: str
        :param CustomerAddress: CustomerAddress，用戶側互聯 IP
        :type CustomerAddress: str
        :param TencentBackupAddress: TencentBackupAddress， 側備用互聯 IP
        :type TencentBackupAddress: str
        """
        self.DirectConnectId = None
        self.DirectConnectTunnelName = None
        self.DirectConnectOwnerAccount = None
        self.NetworkType = None
        self.NetworkRegion = None
        self.VpcId = None
        self.DirectConnectGatewayId = None
        self.Bandwidth = None
        self.RouteType = None
        self.BgpPeer = None
        self.RouteFilterPrefixes = None
        self.Vlan = None
        self.TencentAddress = None
        self.CustomerAddress = None
        self.TencentBackupAddress = None


    def _deserialize(self, params):
        self.DirectConnectId = params.get("DirectConnectId")
        self.DirectConnectTunnelName = params.get("DirectConnectTunnelName")
        self.DirectConnectOwnerAccount = params.get("DirectConnectOwnerAccount")
        self.NetworkType = params.get("NetworkType")
        self.NetworkRegion = params.get("NetworkRegion")
        self.VpcId = params.get("VpcId")
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.Bandwidth = params.get("Bandwidth")
        self.RouteType = params.get("RouteType")
        if params.get("BgpPeer") is not None:
            self.BgpPeer = BgpPeer()
            self.BgpPeer._deserialize(params.get("BgpPeer"))
        if params.get("RouteFilterPrefixes") is not None:
            self.RouteFilterPrefixes = []
            for item in params.get("RouteFilterPrefixes"):
                obj = RouteFilterPrefix()
                obj._deserialize(item)
                self.RouteFilterPrefixes.append(obj)
        self.Vlan = params.get("Vlan")
        self.TencentAddress = params.get("TencentAddress")
        self.CustomerAddress = params.get("CustomerAddress")
        self.TencentBackupAddress = params.get("TencentBackupAddress")


class CreateDirectConnectTunnelResponse(AbstractModel):
    """CreateDirectConnectTunnel返回參數結構體

    """

    def __init__(self):
        """
        :param DirectConnectTunnelIdSet: 專用通道ID
        :type DirectConnectTunnelIdSet: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DirectConnectTunnelIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DirectConnectTunnelIdSet = params.get("DirectConnectTunnelIdSet")
        self.RequestId = params.get("RequestId")


class DeleteDirectConnectRequest(AbstractModel):
    """DeleteDirectConnect請求參數結構體

    """

    def __init__(self):
        """
        :param DirectConnectId: 物理專線的ID。
        :type DirectConnectId: str
        """
        self.DirectConnectId = None


    def _deserialize(self, params):
        self.DirectConnectId = params.get("DirectConnectId")


class DeleteDirectConnectResponse(AbstractModel):
    """DeleteDirectConnect返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDirectConnectTunnelRequest(AbstractModel):
    """DeleteDirectConnectTunnel請求參數結構體

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: 專用通道ID
        :type DirectConnectTunnelId: str
        """
        self.DirectConnectTunnelId = None


    def _deserialize(self, params):
        self.DirectConnectTunnelId = params.get("DirectConnectTunnelId")


class DeleteDirectConnectTunnelResponse(AbstractModel):
    """DeleteDirectConnectTunnel返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccessPointsRequest(AbstractModel):
    """DescribeAccessPoints請求參數結構體

    """

    def __init__(self):
        """
        :param RegionId: 接入點所在的地域。使用DescribeRegions查詢

您可以通過調用 DescribeRegions介面獲取地域ID。
        :type RegionId: str
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。
        :type Limit: int
        """
        self.RegionId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAccessPointsResponse(AbstractModel):
    """DescribeAccessPoints返回參數結構體

    """

    def __init__(self):
        """
        :param AccessPointSet: 接入點訊息。
        :type AccessPointSet: list of AccessPoint
        :param TotalCount: 符合接入點數量。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AccessPointSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccessPointSet") is not None:
            self.AccessPointSet = []
            for item in params.get("AccessPointSet"):
                obj = AccessPoint()
                obj._deserialize(item)
                self.AccessPointSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDirectConnectTunnelsRequest(AbstractModel):
    """DescribeDirectConnectTunnels請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 過濾條件:
參數不支援同時指定DirectConnectTunnelIds和Filters。
<li> direct-connect-tunnel-name, 專用通道名稱。</li>
<li> direct-connect-tunnel-id, 專用通道實例ID，如dcx-abcdefgh。</li>
<li>direct-connect-id, 物理專線實例ID，如，dc-abcdefgh。</li>
        :type Filters: list of Filter
        :param DirectConnectTunnelIds: 專用通道 ID數組
        :type DirectConnectTunnelIds: list of str
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100
        :type Limit: int
        """
        self.Filters = None
        self.DirectConnectTunnelIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.DirectConnectTunnelIds = params.get("DirectConnectTunnelIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeDirectConnectTunnelsResponse(AbstractModel):
    """DescribeDirectConnectTunnels返回參數結構體

    """

    def __init__(self):
        """
        :param DirectConnectTunnelSet: 專用通道清單
        :type DirectConnectTunnelSet: list of DirectConnectTunnel
        :param TotalCount: 符合專用通道數量。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DirectConnectTunnelSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DirectConnectTunnelSet") is not None:
            self.DirectConnectTunnelSet = []
            for item in params.get("DirectConnectTunnelSet"):
                obj = DirectConnectTunnel()
                obj._deserialize(item)
                self.DirectConnectTunnelSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDirectConnectsRequest(AbstractModel):
    """DescribeDirectConnects請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 過濾條件:
        :type Filters: list of Filter
        :param DirectConnectIds: 物理專線 ID數組
        :type DirectConnectIds: list of str
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100
        :type Limit: int
        """
        self.Filters = None
        self.DirectConnectIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.DirectConnectIds = params.get("DirectConnectIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeDirectConnectsResponse(AbstractModel):
    """DescribeDirectConnects返回參數結構體

    """

    def __init__(self):
        """
        :param DirectConnectSet: 物理專線清單。
        :type DirectConnectSet: list of DirectConnect
        :param TotalCount: 符合物理專線清單數量。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DirectConnectSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DirectConnectSet") is not None:
            self.DirectConnectSet = []
            for item in params.get("DirectConnectSet"):
                obj = DirectConnect()
                obj._deserialize(item)
                self.DirectConnectSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DirectConnect(AbstractModel):
    """物理專線訊息清單

    """

    def __init__(self):
        """
        :param DirectConnectId: 物理專線ID。
        :type DirectConnectId: str
        :param DirectConnectName: 物理專線的名稱。
        :type DirectConnectName: str
        :param AccessPointId: 物理專線的接入點ID。
        :type AccessPointId: str
        :param State: 物理專線的狀态。
申請中：PENDING 
申請駁回：REJECTED   
待付款：TOPAY 
已付款：PAID 
建設中：ALLOCATED   
已開通：AVAILABLE  
删除中 ：DELETING
已删除：DELETED 。
        :type State: str
        :param CreatedTime: 物理專線創建時間。
        :type CreatedTime: str
        :param EnabledTime: 物理專線的開通時間。
        :type EnabledTime: str
        :param LineOperator: 提供接入物理專線的運營商。ChinaTelecom： 電信， ChinaMobile：  ，ChinaUnicom：  ， In-houseWiring：樓内線，ChinaOther： 其他， InternationalOperator：境外其他。
        :type LineOperator: str
        :param Location: 本地數據中心的地理位置。
        :type Location: str
        :param Bandwidth: 物理專線接入介面頻寬，單位爲Mbps。
        :type Bandwidth: int
        :param PortType: 用戶側物理專線接入端口類型,取值：100Base-T：百兆電介面,1000Base-T（預設值）：千兆電介面,1000Base-LX：千兆單模光介面（10千米）,10GBase-T：萬兆電介面10GBase-LR：萬兆單模光介面（10千米），預設值，千兆單模光介面（10千米）
        :type PortType: str
        :param CircuitCode: 運營商或者服務商爲物理專線提供的電路編碼。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CircuitCode: str
        :param RedundantDirectConnectId: 備援物理專線的ID。
        :type RedundantDirectConnectId: str
        :param Vlan: 物理專線調試VLAN。預設開啓VLAN，自動分配VLAN。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Vlan: int
        :param TencentAddress: 物理專線調試 側互聯IP。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TencentAddress: str
        :param CustomerAddress: 物理專線調試用戶側互聯IP。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CustomerAddress: str
        :param CustomerName: 物理專線申請者姓名。預設從帳戶體系獲取。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CustomerName: str
        :param CustomerContactMail: 物理專線申請者聯系電子信箱。預設從帳戶體系獲取。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CustomerContactMail: str
        :param CustomerContactNumber: 物理專線申請者聯系號碼。預設從帳戶體系獲取。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CustomerContactNumber: str
        :param ExpiredTime: 物理專線的過期時間。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ExpiredTime: str
        :param ChargeType: 物理專線計費類型。 NON_RECURRING_CHARGE：一次性接入費用；PREPAID_BY_YEAR：按年預付費。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ChargeType: str
        :param FaultReportContactPerson: 報障聯系人。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FaultReportContactPerson: str
        :param FaultReportContactNumber: 報障聯系電話。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FaultReportContactNumber: str
        :param TagSet: 標簽鍵值對
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagSet: list of Tag
        :param AccessPointType: 物理專線的接入點類型。
        :type AccessPointType: str
        :param IdcCity: IDC所在城市
注意：此欄位可能返回 null，表示取不到有效值。
        :type IdcCity: str
        :param ChargeState: 計費狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type ChargeState: str
        """
        self.DirectConnectId = None
        self.DirectConnectName = None
        self.AccessPointId = None
        self.State = None
        self.CreatedTime = None
        self.EnabledTime = None
        self.LineOperator = None
        self.Location = None
        self.Bandwidth = None
        self.PortType = None
        self.CircuitCode = None
        self.RedundantDirectConnectId = None
        self.Vlan = None
        self.TencentAddress = None
        self.CustomerAddress = None
        self.CustomerName = None
        self.CustomerContactMail = None
        self.CustomerContactNumber = None
        self.ExpiredTime = None
        self.ChargeType = None
        self.FaultReportContactPerson = None
        self.FaultReportContactNumber = None
        self.TagSet = None
        self.AccessPointType = None
        self.IdcCity = None
        self.ChargeState = None


    def _deserialize(self, params):
        self.DirectConnectId = params.get("DirectConnectId")
        self.DirectConnectName = params.get("DirectConnectName")
        self.AccessPointId = params.get("AccessPointId")
        self.State = params.get("State")
        self.CreatedTime = params.get("CreatedTime")
        self.EnabledTime = params.get("EnabledTime")
        self.LineOperator = params.get("LineOperator")
        self.Location = params.get("Location")
        self.Bandwidth = params.get("Bandwidth")
        self.PortType = params.get("PortType")
        self.CircuitCode = params.get("CircuitCode")
        self.RedundantDirectConnectId = params.get("RedundantDirectConnectId")
        self.Vlan = params.get("Vlan")
        self.TencentAddress = params.get("TencentAddress")
        self.CustomerAddress = params.get("CustomerAddress")
        self.CustomerName = params.get("CustomerName")
        self.CustomerContactMail = params.get("CustomerContactMail")
        self.CustomerContactNumber = params.get("CustomerContactNumber")
        self.ExpiredTime = params.get("ExpiredTime")
        self.ChargeType = params.get("ChargeType")
        self.FaultReportContactPerson = params.get("FaultReportContactPerson")
        self.FaultReportContactNumber = params.get("FaultReportContactNumber")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.AccessPointType = params.get("AccessPointType")
        self.IdcCity = params.get("IdcCity")
        self.ChargeState = params.get("ChargeState")


class DirectConnectTunnel(AbstractModel):
    """專用通道訊息清單

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: 專用通道ID
        :type DirectConnectTunnelId: str
        :param DirectConnectId: 物理專線ID
        :type DirectConnectId: str
        :param State: 專用通道狀态
AVAILABLE:就緒或者已連接
PENDING:申請中
ALLOCATING:配置中
ALLOCATED:配置完成
ALTERING:修改中
DELETING:删除中
DELETED:删除完成
COMFIRMING:待接受
REJECTED:拒絕
        :type State: str
        :param DirectConnectOwnerAccount: 物理專線的擁有者，開發商賬號 ID
        :type DirectConnectOwnerAccount: str
        :param OwnerAccount: 專用通道的擁有者，開發商賬號 ID
        :type OwnerAccount: str
        :param NetworkType: 網絡類型，分别爲VPC、BMVPC、CCN
 VPC：私有網絡 ，BMVPC：黑石網絡，CCN：雲聯網
        :type NetworkType: str
        :param NetworkRegion: VPC地域對應的網絡名，如ap-guangzhou
        :type NetworkRegion: str
        :param VpcId: 私有網絡統一 ID 或者黑石網絡統一 ID
        :type VpcId: str
        :param DirectConnectGatewayId: 專線閘道 ID
        :type DirectConnectGatewayId: str
        :param RouteType: BGP ：BGP路由 STATIC：靜态 預設爲 BGP 路由
        :type RouteType: str
        :param BgpPeer: 用戶側BGP，Asn，AuthKey
        :type BgpPeer: :class:`taifucloudcloud.dc.v20180410.models.BgpPeer`
        :param RouteFilterPrefixes: 用戶側網段網址
        :type RouteFilterPrefixes: list of RouteFilterPrefix
        :param Vlan: 專用通道的Vlan
        :type Vlan: int
        :param TencentAddress: TencentAddress， 側互聯 IP
        :type TencentAddress: str
        :param CustomerAddress: CustomerAddress，用戶側互聯 IP
        :type CustomerAddress: str
        :param DirectConnectTunnelName: 專用通道名稱
        :type DirectConnectTunnelName: str
        :param CreatedTime: 專用通道創建時間
        :type CreatedTime: str
        :param Bandwidth: 專用通道頻寬值
        :type Bandwidth: int
        :param TagSet: 專用通道標簽值
        :type TagSet: list of Tag
        :param NetDetectId: 關聯的網絡自定義探測ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type NetDetectId: str
        :param EnableBGPCommunity: BGP community開關
注意：此欄位可能返回 null，表示取不到有效值。
        :type EnableBGPCommunity: bool
        :param NatType: 是否爲Nat通道
注意：此欄位可能返回 null，表示取不到有效值。
        :type NatType: int
        :param VpcRegion: VPC地域簡碼，如gz、cd
注意：此欄位可能返回 null，表示取不到有效值。
        :type VpcRegion: str
        :param BfdEnable: 是否開啓BFD
注意：此欄位可能返回 null，表示取不到有效值。
        :type BfdEnable: int
        :param AccessPointType: 專用通道接入點類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type AccessPointType: str
        :param DirectConnectGatewayName: 專線閘道名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type DirectConnectGatewayName: str
        :param VpcName: VPC名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param TencentBackupAddress: TencentBackupAddress， 側備用互聯 IP
注意：此欄位可能返回 null，表示取不到有效值。
        :type TencentBackupAddress: str
        """
        self.DirectConnectTunnelId = None
        self.DirectConnectId = None
        self.State = None
        self.DirectConnectOwnerAccount = None
        self.OwnerAccount = None
        self.NetworkType = None
        self.NetworkRegion = None
        self.VpcId = None
        self.DirectConnectGatewayId = None
        self.RouteType = None
        self.BgpPeer = None
        self.RouteFilterPrefixes = None
        self.Vlan = None
        self.TencentAddress = None
        self.CustomerAddress = None
        self.DirectConnectTunnelName = None
        self.CreatedTime = None
        self.Bandwidth = None
        self.TagSet = None
        self.NetDetectId = None
        self.EnableBGPCommunity = None
        self.NatType = None
        self.VpcRegion = None
        self.BfdEnable = None
        self.AccessPointType = None
        self.DirectConnectGatewayName = None
        self.VpcName = None
        self.TencentBackupAddress = None


    def _deserialize(self, params):
        self.DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        self.DirectConnectId = params.get("DirectConnectId")
        self.State = params.get("State")
        self.DirectConnectOwnerAccount = params.get("DirectConnectOwnerAccount")
        self.OwnerAccount = params.get("OwnerAccount")
        self.NetworkType = params.get("NetworkType")
        self.NetworkRegion = params.get("NetworkRegion")
        self.VpcId = params.get("VpcId")
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.RouteType = params.get("RouteType")
        if params.get("BgpPeer") is not None:
            self.BgpPeer = BgpPeer()
            self.BgpPeer._deserialize(params.get("BgpPeer"))
        if params.get("RouteFilterPrefixes") is not None:
            self.RouteFilterPrefixes = []
            for item in params.get("RouteFilterPrefixes"):
                obj = RouteFilterPrefix()
                obj._deserialize(item)
                self.RouteFilterPrefixes.append(obj)
        self.Vlan = params.get("Vlan")
        self.TencentAddress = params.get("TencentAddress")
        self.CustomerAddress = params.get("CustomerAddress")
        self.DirectConnectTunnelName = params.get("DirectConnectTunnelName")
        self.CreatedTime = params.get("CreatedTime")
        self.Bandwidth = params.get("Bandwidth")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.NetDetectId = params.get("NetDetectId")
        self.EnableBGPCommunity = params.get("EnableBGPCommunity")
        self.NatType = params.get("NatType")
        self.VpcRegion = params.get("VpcRegion")
        self.BfdEnable = params.get("BfdEnable")
        self.AccessPointType = params.get("AccessPointType")
        self.DirectConnectGatewayName = params.get("DirectConnectGatewayName")
        self.VpcName = params.get("VpcName")
        self.TencentBackupAddress = params.get("TencentBackupAddress")


class Filter(AbstractModel):
    """用於條件過濾查詢

    """

    def __init__(self):
        """
        :param Name: 需要過濾的欄位。
        :type Name: str
        :param Values: 欄位的過濾值。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class ModifyDirectConnectAttributeRequest(AbstractModel):
    """ModifyDirectConnectAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param DirectConnectId: 物理專線的ID。
        :type DirectConnectId: str
        :param DirectConnectName: 物理專線名稱。
        :type DirectConnectName: str
        :param CircuitCode: 運營商或者服務商爲物理專線提供的電路編碼。
        :type CircuitCode: str
        :param Vlan: 物理專線調試VLAN。
        :type Vlan: int
        :param TencentAddress: 物理專線調試 側互聯 IP。
        :type TencentAddress: str
        :param CustomerAddress: 物理專線調試用戶側互聯 IP。
        :type CustomerAddress: str
        :param CustomerName: 物理專線申請者姓名。預設從帳戶體系獲取。
        :type CustomerName: str
        :param CustomerContactMail: 物理專線申請者聯系電子信箱。預設從帳戶體系獲取。
        :type CustomerContactMail: str
        :param CustomerContactNumber: 物理專線申請者聯系號碼。預設從帳戶體系獲取。
        :type CustomerContactNumber: str
        :param FaultReportContactPerson: 報障聯系人。
        :type FaultReportContactPerson: str
        :param FaultReportContactNumber: 報障聯系電話。
        :type FaultReportContactNumber: str
        """
        self.DirectConnectId = None
        self.DirectConnectName = None
        self.CircuitCode = None
        self.Vlan = None
        self.TencentAddress = None
        self.CustomerAddress = None
        self.CustomerName = None
        self.CustomerContactMail = None
        self.CustomerContactNumber = None
        self.FaultReportContactPerson = None
        self.FaultReportContactNumber = None


    def _deserialize(self, params):
        self.DirectConnectId = params.get("DirectConnectId")
        self.DirectConnectName = params.get("DirectConnectName")
        self.CircuitCode = params.get("CircuitCode")
        self.Vlan = params.get("Vlan")
        self.TencentAddress = params.get("TencentAddress")
        self.CustomerAddress = params.get("CustomerAddress")
        self.CustomerName = params.get("CustomerName")
        self.CustomerContactMail = params.get("CustomerContactMail")
        self.CustomerContactNumber = params.get("CustomerContactNumber")
        self.FaultReportContactPerson = params.get("FaultReportContactPerson")
        self.FaultReportContactNumber = params.get("FaultReportContactNumber")


class ModifyDirectConnectAttributeResponse(AbstractModel):
    """ModifyDirectConnectAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDirectConnectTunnelAttributeRequest(AbstractModel):
    """ModifyDirectConnectTunnelAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: 專用通道ID
        :type DirectConnectTunnelId: str
        :param DirectConnectTunnelName: 專用通道名稱
        :type DirectConnectTunnelName: str
        :param BgpPeer: 用戶側BGP，包括Asn，AuthKey
        :type BgpPeer: :class:`taifucloudcloud.dc.v20180410.models.BgpPeer`
        :param RouteFilterPrefixes: 用戶側網段網址
        :type RouteFilterPrefixes: list of RouteFilterPrefix
        :param TencentAddress:  側互聯IP
        :type TencentAddress: str
        :param CustomerAddress: 用戶側互聯IP
        :type CustomerAddress: str
        :param Bandwidth: 專用通道頻寬值，單位爲M。
        :type Bandwidth: int
        :param TencentBackupAddress:  側備用互聯IP
        :type TencentBackupAddress: str
        """
        self.DirectConnectTunnelId = None
        self.DirectConnectTunnelName = None
        self.BgpPeer = None
        self.RouteFilterPrefixes = None
        self.TencentAddress = None
        self.CustomerAddress = None
        self.Bandwidth = None
        self.TencentBackupAddress = None


    def _deserialize(self, params):
        self.DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        self.DirectConnectTunnelName = params.get("DirectConnectTunnelName")
        if params.get("BgpPeer") is not None:
            self.BgpPeer = BgpPeer()
            self.BgpPeer._deserialize(params.get("BgpPeer"))
        if params.get("RouteFilterPrefixes") is not None:
            self.RouteFilterPrefixes = []
            for item in params.get("RouteFilterPrefixes"):
                obj = RouteFilterPrefix()
                obj._deserialize(item)
                self.RouteFilterPrefixes.append(obj)
        self.TencentAddress = params.get("TencentAddress")
        self.CustomerAddress = params.get("CustomerAddress")
        self.Bandwidth = params.get("Bandwidth")
        self.TencentBackupAddress = params.get("TencentBackupAddress")


class ModifyDirectConnectTunnelAttributeResponse(AbstractModel):
    """ModifyDirectConnectTunnelAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RejectDirectConnectTunnelRequest(AbstractModel):
    """RejectDirectConnectTunnel請求參數結構體

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: 無
        :type DirectConnectTunnelId: str
        """
        self.DirectConnectTunnelId = None


    def _deserialize(self, params):
        self.DirectConnectTunnelId = params.get("DirectConnectTunnelId")


class RejectDirectConnectTunnelResponse(AbstractModel):
    """RejectDirectConnectTunnel返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RouteFilterPrefix(AbstractModel):
    """用戶側網段網址

    """

    def __init__(self):
        """
        :param Cidr: 用戶側網段網址
        :type Cidr: str
        """
        self.Cidr = None


    def _deserialize(self, params):
        self.Cidr = params.get("Cidr")


class Tag(AbstractModel):
    """標簽鍵值對

    """

    def __init__(self):
        """
        :param Key: 標簽鍵
注意：此欄位可能返回 null，表示取不到有效值。
        :type Key: str
        :param Value: 標簽值
注意：此欄位可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")