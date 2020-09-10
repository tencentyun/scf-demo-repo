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


class DescribeHSMBySubnetIdRequest(AbstractModel):
    """DescribeHSMBySubnetId請求參數結構體

    """

    def __init__(self):
        """
        :param SubnetId: Subnet标識符
        :type SubnetId: str
        """
        self.SubnetId = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")


class DescribeHSMBySubnetIdResponse(AbstractModel):
    """DescribeHSMBySubnetId返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: HSM數量
        :type TotalCount: int
        :param SubnetId: 作爲查詢條件的SubnetId
        :type SubnetId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SubnetId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.SubnetId = params.get("SubnetId")
        self.RequestId = params.get("RequestId")


class DescribeHSMByVpcIdRequest(AbstractModel):
    """DescribeHSMByVpcId請求參數結構體

    """

    def __init__(self):
        """
        :param VpcId: VPC标識符
        :type VpcId: str
        """
        self.VpcId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")


class DescribeHSMByVpcIdResponse(AbstractModel):
    """DescribeHSMByVpcId返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: HSM數量
        :type TotalCount: int
        :param VpcId: 作爲查詢條件的VpcId
        :type VpcId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.VpcId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.VpcId = params.get("VpcId")
        self.RequestId = params.get("RequestId")


class DescribeSubnetRequest(AbstractModel):
    """DescribeSubnet請求參數結構體

    """

    def __init__(self):
        """
        :param Limit: 返回數量。
        :type Limit: int
        :param Offset: 偏移量。
        :type Offset: int
        :param VpcId: 查詢指定VpcId下的子網訊息。
        :type VpcId: str
        :param SearchWord: 查找關鍵字
        :type SearchWord: str
        """
        self.Limit = None
        self.Offset = None
        self.VpcId = None
        self.SearchWord = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.VpcId = params.get("VpcId")
        self.SearchWord = params.get("SearchWord")


class DescribeSubnetResponse(AbstractModel):
    """DescribeSubnet返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 返回的子網數量。
        :type TotalCount: int
        :param SubnetList: 返回的子網實例清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubnetList: list of Subnet
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SubnetList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SubnetList") is not None:
            self.SubnetList = []
            for item in params.get("SubnetList"):
                obj = Subnet()
                obj._deserialize(item)
                self.SubnetList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUsgRequest(AbstractModel):
    """DescribeUsg請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移量，當Offset和Limit均爲0時将一次性返回用戶所有的安全組清單。
        :type Offset: int
        :param Limit: 返回量，當Offset和Limit均爲0時将一次性返回用戶所有的安全組清單。
        :type Limit: int
        :param SearchWord: 搜索關鍵字
        :type SearchWord: str
        """
        self.Offset = None
        self.Limit = None
        self.SearchWord = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchWord = params.get("SearchWord")


class DescribeUsgResponse(AbstractModel):
    """DescribeUsg返回參數結構體

    """

    def __init__(self):
        """
        :param SgList: 用戶的安全組清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type SgList: list of SgUnit
        :param TotalCount: 返回的安全組數量
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SgList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SgList") is not None:
            self.SgList = []
            for item in params.get("SgList"):
                obj = SgUnit()
                obj._deserialize(item)
                self.SgList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeUsgRuleRequest(AbstractModel):
    """DescribeUsgRule請求參數結構體

    """

    def __init__(self):
        """
        :param SgIds: 根據安全組Id獲取安全組詳情
        :type SgIds: list of str
        """
        self.SgIds = None


    def _deserialize(self, params):
        self.SgIds = params.get("SgIds")


class DescribeUsgRuleResponse(AbstractModel):
    """DescribeUsgRule返回參數結構體

    """

    def __init__(self):
        """
        :param SgRules: 安全組詳情
注意：此欄位可能返回 null，表示取不到有效值。
        :type SgRules: list of UsgRuleDetail
        :param TotalCount: 安全組詳情數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SgRules = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SgRules") is not None:
            self.SgRules = []
            for item in params.get("SgRules"):
                obj = UsgRuleDetail()
                obj._deserialize(item)
                self.SgRules.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeVpcRequest(AbstractModel):
    """DescribeVpc請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 返回偏移量。
        :type Offset: int
        :param Limit: 返回數量。
        :type Limit: int
        :param SearchWord: 搜索關鍵字
        :type SearchWord: str
        """
        self.Offset = None
        self.Limit = None
        self.SearchWord = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchWord = params.get("SearchWord")


class DescribeVpcResponse(AbstractModel):
    """DescribeVpc返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 可查詢到的所有Vpc實例總數。
        :type TotalCount: int
        :param VpcList: Vpc對象清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type VpcList: list of Vpc
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.VpcList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VpcList") is not None:
            self.VpcList = []
            for item in params.get("VpcList"):
                obj = Vpc()
                obj._deserialize(item)
                self.VpcList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVsmAttributesRequest(AbstractModel):
    """DescribeVsmAttributes請求參數結構體

    """

    def __init__(self):
        """
        :param ResourceId: 資源Id
        :type ResourceId: str
        """
        self.ResourceId = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")


class DescribeVsmAttributesResponse(AbstractModel):
    """DescribeVsmAttributes返回參數結構體

    """

    def __init__(self):
        """
        :param ResourceId: 資源Id
        :type ResourceId: str
        :param ResourceName: 資源名稱
        :type ResourceName: str
        :param Status: 資源狀态
        :type Status: int
        :param Vip: 資源IP
        :type Vip: str
        :param VpcId: 資源所屬Vpc
        :type VpcId: str
        :param SubnetId: 資源所屬子網
        :type SubnetId: str
        :param Model: 資源所屬HSM的規格
        :type Model: str
        :param VsmType: 資源類型
        :type VsmType: int
        :param RegionId: 地域Id
        :type RegionId: int
        :param ZoneId: 區域Id
        :type ZoneId: int
        :param ExpireTime: 過期時間
        :type ExpireTime: int
        :param SgList: 安全組詳情訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type SgList: list of UsgRuleDetail
        :param SubnetName: 子網名
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubnetName: str
        :param RegionName: 地域名
注意：此欄位可能返回 null，表示取不到有效值。
        :type RegionName: str
        :param ZoneName: 區域名
注意：此欄位可能返回 null，表示取不到有效值。
        :type ZoneName: str
        :param Expired: 實例是否已經過期
注意：此欄位可能返回 null，表示取不到有效值。
        :type Expired: bool
        :param RemainSeconds: 爲正數表示實例距離過期時間剩餘秒數，爲負數表示實例已經過期多少秒
注意：此欄位可能返回 null，表示取不到有效值。
        :type RemainSeconds: int
        :param VpcName: 私有虛拟網絡名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param VpcCidrBlock: VPC的IPv4 CIDR
注意：此欄位可能返回 null，表示取不到有效值。
        :type VpcCidrBlock: str
        :param SubnetCidrBlock: 子網的CIDR
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubnetCidrBlock: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ResourceId = None
        self.ResourceName = None
        self.Status = None
        self.Vip = None
        self.VpcId = None
        self.SubnetId = None
        self.Model = None
        self.VsmType = None
        self.RegionId = None
        self.ZoneId = None
        self.ExpireTime = None
        self.SgList = None
        self.SubnetName = None
        self.RegionName = None
        self.ZoneName = None
        self.Expired = None
        self.RemainSeconds = None
        self.VpcName = None
        self.VpcCidrBlock = None
        self.SubnetCidrBlock = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.ResourceName = params.get("ResourceName")
        self.Status = params.get("Status")
        self.Vip = params.get("Vip")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Model = params.get("Model")
        self.VsmType = params.get("VsmType")
        self.RegionId = params.get("RegionId")
        self.ZoneId = params.get("ZoneId")
        self.ExpireTime = params.get("ExpireTime")
        if params.get("SgList") is not None:
            self.SgList = []
            for item in params.get("SgList"):
                obj = UsgRuleDetail()
                obj._deserialize(item)
                self.SgList.append(obj)
        self.SubnetName = params.get("SubnetName")
        self.RegionName = params.get("RegionName")
        self.ZoneName = params.get("ZoneName")
        self.Expired = params.get("Expired")
        self.RemainSeconds = params.get("RemainSeconds")
        self.VpcName = params.get("VpcName")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.SubnetCidrBlock = params.get("SubnetCidrBlock")
        self.RequestId = params.get("RequestId")


class DescribeVsmsRequest(AbstractModel):
    """DescribeVsms請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移
        :type Offset: int
        :param Limit: 最大數量
        :type Limit: int
        :param SearchWord: 查詢關鍵字
        :type SearchWord: str
        """
        self.Offset = None
        self.Limit = None
        self.SearchWord = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchWord = params.get("SearchWord")


class DescribeVsmsResponse(AbstractModel):
    """DescribeVsms返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 獲取實例的總個數
        :type TotalCount: int
        :param VsmList: 資源訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type VsmList: list of ResourceInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.VsmList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VsmList") is not None:
            self.VsmList = []
            for item in params.get("VsmList"):
                obj = ResourceInfo()
                obj._deserialize(item)
                self.VsmList.append(obj)
        self.RequestId = params.get("RequestId")


class InquiryPriceBuyVsmRequest(AbstractModel):
    """InquiryPriceBuyVsm請求參數結構體

    """

    def __init__(self):
        """
        :param GoodsNum: 需購買實例的數量
        :type GoodsNum: int
        :param PayMode: 付費模式：0表示按需計費/後付費，1表示預付費
        :type PayMode: int
        :param TimeSpan: 商品的時間大小
        :type TimeSpan: str
        :param TimeUnit: 商品的時間單位
        :type TimeUnit: str
        :param Currency: 貨币類型，預設爲CNY
        :type Currency: str
        :param Type: 預設爲CREATE，可選RENEW
        :type Type: str
        """
        self.GoodsNum = None
        self.PayMode = None
        self.TimeSpan = None
        self.TimeUnit = None
        self.Currency = None
        self.Type = None


    def _deserialize(self, params):
        self.GoodsNum = params.get("GoodsNum")
        self.PayMode = params.get("PayMode")
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnit = params.get("TimeUnit")
        self.Currency = params.get("Currency")
        self.Type = params.get("Type")


class InquiryPriceBuyVsmResponse(AbstractModel):
    """InquiryPriceBuyVsm返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCost: 總金額
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCost: float
        :param GoodsNum: 購買的實例數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type GoodsNum: int
        :param TimeSpan: 商品的時間大小
注意：此欄位可能返回 null，表示取不到有效值。
        :type TimeSpan: str
        :param TimeUnit: 商品的時間單位
注意：此欄位可能返回 null，表示取不到有效值。
        :type TimeUnit: str
        :param OriginalCost: 原始總金額
注意：此欄位可能返回 null，表示取不到有效值。
        :type OriginalCost: float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCost = None
        self.GoodsNum = None
        self.TimeSpan = None
        self.TimeUnit = None
        self.OriginalCost = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCost = params.get("TotalCost")
        self.GoodsNum = params.get("GoodsNum")
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnit = params.get("TimeUnit")
        self.OriginalCost = params.get("OriginalCost")
        self.RequestId = params.get("RequestId")


class ModifyVsmAttributesRequest(AbstractModel):
    """ModifyVsmAttributes請求參數結構體

    """

    def __init__(self):
        """
        :param ResourceId: 資源Id
        :type ResourceId: str
        :param Type: UpdateResourceName-修改資源名稱,
UpdateSgIds-修改安全組名稱,
UpdateNetWork-修改網絡,
Default-預設不修改
        :type Type: list of str
        :param ResourceName: 資源名稱
        :type ResourceName: str
        :param SgIds: 安全組Id
        :type SgIds: list of str
        :param VpcId: VpcId
        :type VpcId: str
        :param SubnetId: 子網Id
        :type SubnetId: str
        """
        self.ResourceId = None
        self.Type = None
        self.ResourceName = None
        self.SgIds = None
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.Type = params.get("Type")
        self.ResourceName = params.get("ResourceName")
        self.SgIds = params.get("SgIds")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")


class ModifyVsmAttributesResponse(AbstractModel):
    """ModifyVsmAttributes返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResourceInfo(AbstractModel):
    """資源訊息

    """

    def __init__(self):
        """
        :param ResourceId: 資源Id
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param ResourceName: 資源名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResourceName: str
        :param Status: 資源狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: int
        :param Vip: 資源IP
注意：此欄位可能返回 null，表示取不到有效值。
        :type Vip: str
        :param VpcId: 資源所屬Vpc
注意：此欄位可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param SubnetId: 資源所屬子網
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param Model: 資源所屬HSM規格
注意：此欄位可能返回 null，表示取不到有效值。
        :type Model: str
        :param VsmType: 資源類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type VsmType: int
        :param RegionId: 地域Id
注意：此欄位可能返回 null，表示取不到有效值。
        :type RegionId: int
        :param ZoneId: 區域Id
注意：此欄位可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param ExpireTime: 過期時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type ExpireTime: int
        :param RegionName: 地域名
注意：此欄位可能返回 null，表示取不到有效值。
        :type RegionName: str
        :param ZoneName: 區域名
注意：此欄位可能返回 null，表示取不到有效值。
        :type ZoneName: str
        :param SgList: 實例的安全組清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type SgList: list of SgUnit
        :param SubnetName: 子網名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubnetName: str
        :param Expired: 當前實例是否已經過期
注意：此欄位可能返回 null，表示取不到有效值。
        :type Expired: bool
        :param RemainSeconds: 爲正數表示實例距離過期時間還剩餘多少秒，爲負數表示已經過期多少秒
注意：此欄位可能返回 null，表示取不到有效值。
        :type RemainSeconds: int
        :param VpcName: Vpc名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type VpcName: str
        """
        self.ResourceId = None
        self.ResourceName = None
        self.Status = None
        self.Vip = None
        self.VpcId = None
        self.SubnetId = None
        self.Model = None
        self.VsmType = None
        self.RegionId = None
        self.ZoneId = None
        self.ExpireTime = None
        self.RegionName = None
        self.ZoneName = None
        self.SgList = None
        self.SubnetName = None
        self.Expired = None
        self.RemainSeconds = None
        self.VpcName = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.ResourceName = params.get("ResourceName")
        self.Status = params.get("Status")
        self.Vip = params.get("Vip")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Model = params.get("Model")
        self.VsmType = params.get("VsmType")
        self.RegionId = params.get("RegionId")
        self.ZoneId = params.get("ZoneId")
        self.ExpireTime = params.get("ExpireTime")
        self.RegionName = params.get("RegionName")
        self.ZoneName = params.get("ZoneName")
        if params.get("SgList") is not None:
            self.SgList = []
            for item in params.get("SgList"):
                obj = SgUnit()
                obj._deserialize(item)
                self.SgList.append(obj)
        self.SubnetName = params.get("SubnetName")
        self.Expired = params.get("Expired")
        self.RemainSeconds = params.get("RemainSeconds")
        self.VpcName = params.get("VpcName")


class SgUnit(AbstractModel):
    """安全組基礎訊息

    """

    def __init__(self):
        """
        :param SgId: 安全組Id
注意：此欄位可能返回 null，表示取不到有效值。
        :type SgId: str
        :param SgName: 安全組名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type SgName: str
        :param SgRemark: 備注
注意：此欄位可能返回 null，表示取不到有效值。
        :type SgRemark: str
        :param CreateTime: 創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self.SgId = None
        self.SgName = None
        self.SgRemark = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.SgId = params.get("SgId")
        self.SgName = params.get("SgName")
        self.SgRemark = params.get("SgRemark")
        self.CreateTime = params.get("CreateTime")


class Subnet(AbstractModel):
    """Subnet對象

    """

    def __init__(self):
        """
        :param VpcId: VPC實例ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param SubnetId: 子網實例ID，例如：subnet-bthucmmy。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param SubnetName: 子網名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubnetName: str
        :param CidrBlock: 子網的 IPv4 CIDR。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CidrBlock: str
        :param CreatedTime: 創建時間。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param AvailableIpAddressCount: 可用IP數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AvailableIpAddressCount: int
        :param Ipv6CidrBlock: 子網的 IPv6 CIDR。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Ipv6CidrBlock: str
        :param TotalIpAddressCount: 總IP數
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalIpAddressCount: int
        :param IsDefault: 是否爲預設Subnet
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsDefault: bool
        """
        self.VpcId = None
        self.SubnetId = None
        self.SubnetName = None
        self.CidrBlock = None
        self.CreatedTime = None
        self.AvailableIpAddressCount = None
        self.Ipv6CidrBlock = None
        self.TotalIpAddressCount = None
        self.IsDefault = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.CidrBlock = params.get("CidrBlock")
        self.CreatedTime = params.get("CreatedTime")
        self.AvailableIpAddressCount = params.get("AvailableIpAddressCount")
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        self.TotalIpAddressCount = params.get("TotalIpAddressCount")
        self.IsDefault = params.get("IsDefault")


class UsgPolicy(AbstractModel):
    """安全組策略

    """

    def __init__(self):
        """
        :param Ip: cidr格式網址
注意：此欄位可能返回 null，表示取不到有效值。
        :type Ip: str
        :param Id: 安全組id代表的網址集合
注意：此欄位可能返回 null，表示取不到有效值。
        :type Id: str
        :param AddressModule: 網址組id代表的網址集合
注意：此欄位可能返回 null，表示取不到有效值。
        :type AddressModule: str
        :param Proto: 協議
注意：此欄位可能返回 null，表示取不到有效值。
        :type Proto: str
        :param Port: 端口
注意：此欄位可能返回 null，表示取不到有效值。
        :type Port: str
        :param ServiceModule: 服務組id代表的協議和端口集合
注意：此欄位可能返回 null，表示取不到有效值。
        :type ServiceModule: str
        :param Desc: 備注
注意：此欄位可能返回 null，表示取不到有效值。
        :type Desc: str
        :param Action: 比對後行爲:ACCEPT/DROP
注意：此欄位可能返回 null，表示取不到有效值。
        :type Action: str
        """
        self.Ip = None
        self.Id = None
        self.AddressModule = None
        self.Proto = None
        self.Port = None
        self.ServiceModule = None
        self.Desc = None
        self.Action = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Id = params.get("Id")
        self.AddressModule = params.get("AddressModule")
        self.Proto = params.get("Proto")
        self.Port = params.get("Port")
        self.ServiceModule = params.get("ServiceModule")
        self.Desc = params.get("Desc")
        self.Action = params.get("Action")


class UsgRuleDetail(AbstractModel):
    """安全組規則詳情

    """

    def __init__(self):
        """
        :param InBound: 入站規則
注意：此欄位可能返回 null，表示取不到有效值。
        :type InBound: list of UsgPolicy
        :param OutBound: 出站規則
注意：此欄位可能返回 null，表示取不到有效值。
        :type OutBound: list of UsgPolicy
        :param SgId: 安全組Id
注意：此欄位可能返回 null，表示取不到有效值。
        :type SgId: str
        :param SgName: 安全組名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type SgName: str
        :param SgRemark: 備注
注意：此欄位可能返回 null，表示取不到有效值。
        :type SgRemark: str
        :param CreateTime: 創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param Version: 版本
注意：此欄位可能返回 null，表示取不到有效值。
        :type Version: int
        """
        self.InBound = None
        self.OutBound = None
        self.SgId = None
        self.SgName = None
        self.SgRemark = None
        self.CreateTime = None
        self.Version = None


    def _deserialize(self, params):
        if params.get("InBound") is not None:
            self.InBound = []
            for item in params.get("InBound"):
                obj = UsgPolicy()
                obj._deserialize(item)
                self.InBound.append(obj)
        if params.get("OutBound") is not None:
            self.OutBound = []
            for item in params.get("OutBound"):
                obj = UsgPolicy()
                obj._deserialize(item)
                self.OutBound.append(obj)
        self.SgId = params.get("SgId")
        self.SgName = params.get("SgName")
        self.SgRemark = params.get("SgRemark")
        self.CreateTime = params.get("CreateTime")
        self.Version = params.get("Version")


class Vpc(AbstractModel):
    """VPC對象

    """

    def __init__(self):
        """
        :param VpcName: Vpc名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param VpcId: VpcId
注意：此欄位可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param CreatedTime: 創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param IsDefault: 是否爲預設VPC
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsDefault: bool
        """
        self.VpcName = None
        self.VpcId = None
        self.CreatedTime = None
        self.IsDefault = None


    def _deserialize(self, params):
        self.VpcName = params.get("VpcName")
        self.VpcId = params.get("VpcId")
        self.CreatedTime = params.get("CreatedTime")
        self.IsDefault = params.get("IsDefault")