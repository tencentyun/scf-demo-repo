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


class BindEipAclsRequest(AbstractModel):
    """BindEipAcls請求參數結構體

    """

    def __init__(self):
        """
        :param EipIdAclIdList: 待關聯的 EIP 與 ACL關系清單
        :type EipIdAclIdList: list of EipAclMap
        """
        self.EipIdAclIdList = None


    def _deserialize(self, params):
        if params.get("EipIdAclIdList") is not None:
            self.EipIdAclIdList = []
            for item in params.get("EipIdAclIdList"):
                obj = EipAclMap()
                obj._deserialize(item)
                self.EipIdAclIdList.append(obj)


class BindEipAclsResponse(AbstractModel):
    """BindEipAcls返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BindHostedRequest(AbstractModel):
    """BindHosted請求參數結構體

    """

    def __init__(self):
        """
        :param EipId: Eip實例ID，可通過DescribeBmEip 介面返回欄位中的 eipId獲取。Eip和EipId參數必須要填寫一個。
        :type EipId: str
        :param InstanceId: 托管機器實例ID
        :type InstanceId: str
        """
        self.EipId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.EipId = params.get("EipId")
        self.InstanceId = params.get("InstanceId")


class BindHostedResponse(AbstractModel):
    """BindHosted返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步任務ID，可以通過EipBmQueryTask查詢任務狀态
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class BindRsRequest(AbstractModel):
    """BindRs請求參數結構體

    """

    def __init__(self):
        """
        :param EipId: Eip實例ID
        :type EipId: str
        :param InstanceId: 物理服務器實例ID
        :type InstanceId: str
        """
        self.EipId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.EipId = params.get("EipId")
        self.InstanceId = params.get("InstanceId")


class BindRsResponse(AbstractModel):
    """BindRs返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 綁定黑石物理機異步任務ID，可以通過DescribeEipTask查詢任務狀态
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class BindVpcIpRequest(AbstractModel):
    """BindVpcIp請求參數結構體

    """

    def __init__(self):
        """
        :param EipId: Eip實例ID
        :type EipId: str
        :param VpcId: EIP歸屬VpcId，例如vpc-k7j1t2x1
        :type VpcId: str
        :param VpcIp: 綁定的VPC内IP網址
        :type VpcIp: str
        """
        self.EipId = None
        self.VpcId = None
        self.VpcIp = None


    def _deserialize(self, params):
        self.EipId = params.get("EipId")
        self.VpcId = params.get("VpcId")
        self.VpcIp = params.get("VpcIp")


class BindVpcIpResponse(AbstractModel):
    """BindVpcIp返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: EIP綁定VPC網絡IP異步任務ID，可以通過查詢EIP任務狀态查詢任務狀态
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateEipAclRequest(AbstractModel):
    """CreateEipAcl請求參數結構體

    """

    def __init__(self):
        """
        :param AclName: ACL 名稱
        :type AclName: str
        :param Status: ACL 狀态 0：無狀态，1：有狀态
        :type Status: int
        """
        self.AclName = None
        self.Status = None


    def _deserialize(self, params):
        self.AclName = params.get("AclName")
        self.Status = params.get("Status")


class CreateEipAclResponse(AbstractModel):
    """CreateEipAcl返回參數結構體

    """

    def __init__(self):
        """
        :param AclId: ACL 實例 ID
        :type AclId: str
        :param Status: ACL 實例狀态
        :type Status: int
        :param AclName: ACL 實例名稱
        :type AclName: str
        :param CreatedAt: ACL 實例創建時間
        :type CreatedAt: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AclId = None
        self.Status = None
        self.AclName = None
        self.CreatedAt = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AclId = params.get("AclId")
        self.Status = params.get("Status")
        self.AclName = params.get("AclName")
        self.CreatedAt = params.get("CreatedAt")
        self.RequestId = params.get("RequestId")


class CreateEipRequest(AbstractModel):
    """CreateEip請求參數結構體

    """

    def __init__(self):
        """
        :param GoodsNum: 申請數量，預設爲1, 最大 20
        :type GoodsNum: int
        :param PayMode: EIP計費方式，flow-流量計費；bandwidth-頻寬計費
        :type PayMode: str
        :param Bandwidth: 頻寬設定值（只在頻寬計費時生效）
        :type Bandwidth: int
        :param SetType: EIP模式，目前支援tunnel和fullnat
        :type SetType: str
        :param Exclusive: 是否使用獨占集群，0：不使用，1：使用。預設爲0
        :type Exclusive: int
        :param VpcId: EIP歸屬私有網絡ID，例如vpc-k7j1t2x1
        :type VpcId: str
        :param IpList: 指定申請的IP清單
        :type IpList: list of str
        """
        self.GoodsNum = None
        self.PayMode = None
        self.Bandwidth = None
        self.SetType = None
        self.Exclusive = None
        self.VpcId = None
        self.IpList = None


    def _deserialize(self, params):
        self.GoodsNum = params.get("GoodsNum")
        self.PayMode = params.get("PayMode")
        self.Bandwidth = params.get("Bandwidth")
        self.SetType = params.get("SetType")
        self.Exclusive = params.get("Exclusive")
        self.VpcId = params.get("VpcId")
        self.IpList = params.get("IpList")


class CreateEipResponse(AbstractModel):
    """CreateEip返回參數結構體

    """

    def __init__(self):
        """
        :param EipIds: EIP清單
        :type EipIds: list of str
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.EipIds = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EipIds = params.get("EipIds")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteEipAclRequest(AbstractModel):
    """DeleteEipAcl請求參數結構體

    """

    def __init__(self):
        """
        :param AclId: 待删除的 ACL 實例 ID
        :type AclId: str
        """
        self.AclId = None


    def _deserialize(self, params):
        self.AclId = params.get("AclId")


class DeleteEipAclResponse(AbstractModel):
    """DeleteEipAcl返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEipRequest(AbstractModel):
    """DeleteEip請求參數結構體

    """

    def __init__(self):
        """
        :param EipIds: Eip實例ID清單
        :type EipIds: list of str
        """
        self.EipIds = None


    def _deserialize(self, params):
        self.EipIds = params.get("EipIds")


class DeleteEipResponse(AbstractModel):
    """DeleteEip返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務Id
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DescribeEipAclsRequest(AbstractModel):
    """DescribeEipAcls請求參數結構體

    """

    def __init__(self):
        """
        :param AclName: ACL 名稱，支援模糊查找
        :type AclName: str
        :param AclIds: ACL 實例 ID 清單，數組下标從 0 開始
        :type AclIds: list of str
        :param Offset: 分頁參數。偏移量，預設爲 0
        :type Offset: int
        :param Limit: 分頁參數。每一頁的 EIPACL 清單數目
        :type Limit: int
        :param EipIds: EIP實例ID清單
        :type EipIds: list of str
        :param EipIps: EIP IP網址清單
        :type EipIps: list of str
        :param EipNames: EIP名稱清單
        :type EipNames: list of str
        :param OrderField: 排序欄位
        :type OrderField: str
        :param Order: 排序方式，取值：0:增序(預設)，1:降序
        :type Order: int
        :param AclNames: ACL名稱清單，支援模糊查找
        :type AclNames: list of str
        """
        self.AclName = None
        self.AclIds = None
        self.Offset = None
        self.Limit = None
        self.EipIds = None
        self.EipIps = None
        self.EipNames = None
        self.OrderField = None
        self.Order = None
        self.AclNames = None


    def _deserialize(self, params):
        self.AclName = params.get("AclName")
        self.AclIds = params.get("AclIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.EipIds = params.get("EipIds")
        self.EipIps = params.get("EipIps")
        self.EipNames = params.get("EipNames")
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")
        self.AclNames = params.get("AclNames")


class DescribeEipAclsResponse(AbstractModel):
    """DescribeEipAcls返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 返回 EIPACL 清單總數
        :type TotalCount: int
        :param EipAclList: EIPACL清單
        :type EipAclList: list of EipAcl
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.EipAclList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("EipAclList") is not None:
            self.EipAclList = []
            for item in params.get("EipAclList"):
                obj = EipAcl()
                obj._deserialize(item)
                self.EipAclList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEipQuotaRequest(AbstractModel):
    """DescribeEipQuota請求參數結構體

    """


class DescribeEipQuotaResponse(AbstractModel):
    """DescribeEipQuota返回參數結構體

    """

    def __init__(self):
        """
        :param EipNumQuota: 能擁有的EIP個數的總配額，預設是100個
        :type EipNumQuota: int
        :param CurrentEipNum: 當前已使用的EIP個數，包括創建中、綁定中、已綁定、解綁中、未綁定幾種狀态的EIP個數總和
        :type CurrentEipNum: int
        :param DailyApplyCount: 當天申請EIP次數
        :type DailyApplyCount: int
        :param DailyApplyQuota: 每日申請EIP的次數限制
        :type DailyApplyQuota: int
        :param BatchApplyMax: BatchApplyMax
        :type BatchApplyMax: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.EipNumQuota = None
        self.CurrentEipNum = None
        self.DailyApplyCount = None
        self.DailyApplyQuota = None
        self.BatchApplyMax = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EipNumQuota = params.get("EipNumQuota")
        self.CurrentEipNum = params.get("CurrentEipNum")
        self.DailyApplyCount = params.get("DailyApplyCount")
        self.DailyApplyQuota = params.get("DailyApplyQuota")
        self.BatchApplyMax = params.get("BatchApplyMax")
        self.RequestId = params.get("RequestId")


class DescribeEipTaskRequest(AbstractModel):
    """DescribeEipTask請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: EIP查詢任務ID
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class DescribeEipTaskResponse(AbstractModel):
    """DescribeEipTask返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 當前任務狀态碼：0-成功，1-失敗，2-進行中
        :type Status: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeEipsRequest(AbstractModel):
    """DescribeEips請求參數結構體

    """

    def __init__(self):
        """
        :param EipIds: EIP實例ID清單
        :type EipIds: list of str
        :param Eips: EIP IP 清單
        :type Eips: list of str
        :param InstanceIds: 主機實例ID 清單
        :type InstanceIds: list of str
        :param SearchKey: EIP名稱,模糊比對
        :type SearchKey: str
        :param Status: 狀态清單, 預設所有
        :type Status: list of int
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 返回EIP數量，預設 20, 最大值 100
        :type Limit: int
        :param OrderField: 排序欄位，支援： EipId,Eip,Status, InstanceId,CreatedAt
        :type OrderField: str
        :param Order: 排序方式 0:遞增 1:遞減(預設)
        :type Order: int
        :param PayMode: 計費模式,流量：flow，頻寬：bandwidth
        :type PayMode: str
        :param VpcId: EIP歸屬VpcId，例如vpc-k7j1t2x1
        :type VpcId: str
        :param BindTypes: 綁定類型，-1：未綁定，0：物理機，1：nat閘道，2：虛拟IP, 3:托管機器
        :type BindTypes: list of int
        :param ExclusiveTag: 獨占标志，0：共享，1：獨占
        :type ExclusiveTag: int
        :param AclId: EIP ACL實例ID
        :type AclId: str
        :param BindAcl: 搜索條件，是否綁定了EIP ACL， 0：未綁定，1：綁定
        :type BindAcl: int
        """
        self.EipIds = None
        self.Eips = None
        self.InstanceIds = None
        self.SearchKey = None
        self.Status = None
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.Order = None
        self.PayMode = None
        self.VpcId = None
        self.BindTypes = None
        self.ExclusiveTag = None
        self.AclId = None
        self.BindAcl = None


    def _deserialize(self, params):
        self.EipIds = params.get("EipIds")
        self.Eips = params.get("Eips")
        self.InstanceIds = params.get("InstanceIds")
        self.SearchKey = params.get("SearchKey")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")
        self.PayMode = params.get("PayMode")
        self.VpcId = params.get("VpcId")
        self.BindTypes = params.get("BindTypes")
        self.ExclusiveTag = params.get("ExclusiveTag")
        self.AclId = params.get("AclId")
        self.BindAcl = params.get("BindAcl")


class DescribeEipsResponse(AbstractModel):
    """DescribeEips返回參數結構體

    """

    def __init__(self):
        """
        :param EipSet: 返回EIP訊息數組
        :type EipSet: list of EipInfo
        :param TotalCount: 返回EIP數量
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.EipSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EipSet") is not None:
            self.EipSet = []
            for item in params.get("EipSet"):
                obj = EipInfo()
                obj._deserialize(item)
                self.EipSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class EipAcl(AbstractModel):
    """EipAcl訊息

    """

    def __init__(self):
        """
        :param AclId: ACL 實例 ID。
        :type AclId: str
        :param AclName: ACL 實例名稱
        :type AclName: str
        :param Status: ACL 狀态。0：無狀态，1：有狀态
        :type Status: str
        :param CreatedAt: EIPACL 創建時間
        :type CreatedAt: str
        :param EipNum: EIPACL 已關聯的 eip 數目
        :type EipNum: int
        :param OutRules: 出站規則
        :type OutRules: list of EipAclRule
        :param InRules: 入站規則
        :type InRules: list of EipAclRule
        """
        self.AclId = None
        self.AclName = None
        self.Status = None
        self.CreatedAt = None
        self.EipNum = None
        self.OutRules = None
        self.InRules = None


    def _deserialize(self, params):
        self.AclId = params.get("AclId")
        self.AclName = params.get("AclName")
        self.Status = params.get("Status")
        self.CreatedAt = params.get("CreatedAt")
        self.EipNum = params.get("EipNum")
        if params.get("OutRules") is not None:
            self.OutRules = []
            for item in params.get("OutRules"):
                obj = EipAclRule()
                obj._deserialize(item)
                self.OutRules.append(obj)
        if params.get("InRules") is not None:
            self.InRules = []
            for item in params.get("InRules"):
                obj = EipAclRule()
                obj._deserialize(item)
                self.InRules.append(obj)


class EipAclMap(AbstractModel):
    """eipid與aclid關聯關系

    """

    def __init__(self):
        """
        :param EipId: EIP 實例 ID
        :type EipId: str
        :param AclId: ACL 實例 ID
        :type AclId: str
        """
        self.EipId = None
        self.AclId = None


    def _deserialize(self, params):
        self.EipId = params.get("EipId")
        self.AclId = params.get("AclId")


class EipAclRule(AbstractModel):
    """eipacl規則

    """

    def __init__(self):
        """
        :param Ip: 源 IP
        :type Ip: str
        :param Port: 目标端口
        :type Port: str
        :param Protocol: 協議(TCP/UDP/ICMP/ANY)
        :type Protocol: str
        :param Action: 策略（accept/drop）
        :type Action: str
        :param Description: 備注
        :type Description: str
        """
        self.Ip = None
        self.Port = None
        self.Protocol = None
        self.Action = None
        self.Description = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.Protocol = params.get("Protocol")
        self.Action = params.get("Action")
        self.Description = params.get("Description")


class EipInfo(AbstractModel):
    """Eip訊息

    """

    def __init__(self):
        """
        :param EipId: EIP實例ID
        :type EipId: str
        :param EipName: EIP名稱
        :type EipName: str
        :param Eip: EIP網址
        :type Eip: str
        :param IspId: 運營商ID 0：電信； 1：聯通； 2：移動； 3：教育網； 4：盈科； 5：BGP； 6：中國香港
        :type IspId: int
        :param Status: 狀态 0：創建中； 1：綁定中； 2：已綁定； 3：解綁中； 4：未綁定； 6：下線中； 9：創建失敗
        :type Status: int
        :param Arrears: 是否欠費隔離 1： 欠費隔離； 0： 正常。處在欠費隔離情況下的EIP不能進行任何管理操作。
        :type Arrears: int
        :param InstanceId: EIP所綁定的服務器實例ID，未綁定則爲空
        :type InstanceId: str
        :param InstanceAlias: 服務器别名
        :type InstanceAlias: str
        :param FreeAt: EIP解綁時間
        :type FreeAt: str
        :param CreatedAt: EIP創建時間
        :type CreatedAt: str
        :param UpdatedAt: EIP更新時間
        :type UpdatedAt: str
        :param FreeSecond: EIP未綁定服務器時長（單位：秒）
        :type FreeSecond: int
        :param Type: EIP所綁定的資源類型，-1：未綁定資源；0：黑石物理機，欄位對應unInstanceId；1：Nat閘道，欄位對應natUid；2：雲伺服器欄位對應vpcIp; 3: 托管機器，欄位對應HInstanceId, HInstanceAlias
        :type Type: int
        :param PayMode: EIP計費模式，"flow"：流量計費； "bandwidth"：頻寬計費
        :type PayMode: str
        :param Bandwidth: EIP頻寬計費模式下的頻寬上限（單位：MB）
        :type Bandwidth: int
        :param LatestPayMode: 最近一次操作變更的EIP計費模式，"flow"：流量計費； "bandwidth"：頻寬計費
        :type LatestPayMode: str
        :param LatestBandwidth: 最近一次操作變更的EIP計費模式對應的頻寬上限值，僅在頻寬計費模式下有效（單位：MB）
        :type LatestBandwidth: int
        :param VpcName: 私有網絡名稱
        :type VpcName: str
        :param NatId: EIP所綁定的NAT閘道的數字ID，形如：1001,，未綁定則爲空
        :type NatId: int
        :param NatUid: EIP所綁定的NAT閘道實例ID，形如："nat-n47xxxxx"，未綁定則爲空
        :type NatUid: str
        :param VpcIp: EIP所綁定的雲伺服器IP(托管或者雲伺服器的IP），形如："10.1.1.3"。 注意：IP資源需要通過bmvpc模組注冊或者申請後才可以綁定eip，介面使用申請子網IP和注冊子網IP：,未綁定則爲空
        :type VpcIp: str
        :param VpcId: 私有網絡實例ID
        :type VpcId: str
        :param Exclusive: 是否爲獨占類型EIP
        :type Exclusive: int
        :param VpcCidr: 私有網絡的cidr
        :type VpcCidr: str
        :param AclId: EIP ACL實例ID
        :type AclId: str
        :param AclName: EIP ACL名稱
        :type AclName: str
        :param HInstanceId: 托管機器實例ID
        :type HInstanceId: str
        :param HInstanceAlias: 托管機器别名
        :type HInstanceAlias: str
        """
        self.EipId = None
        self.EipName = None
        self.Eip = None
        self.IspId = None
        self.Status = None
        self.Arrears = None
        self.InstanceId = None
        self.InstanceAlias = None
        self.FreeAt = None
        self.CreatedAt = None
        self.UpdatedAt = None
        self.FreeSecond = None
        self.Type = None
        self.PayMode = None
        self.Bandwidth = None
        self.LatestPayMode = None
        self.LatestBandwidth = None
        self.VpcName = None
        self.NatId = None
        self.NatUid = None
        self.VpcIp = None
        self.VpcId = None
        self.Exclusive = None
        self.VpcCidr = None
        self.AclId = None
        self.AclName = None
        self.HInstanceId = None
        self.HInstanceAlias = None


    def _deserialize(self, params):
        self.EipId = params.get("EipId")
        self.EipName = params.get("EipName")
        self.Eip = params.get("Eip")
        self.IspId = params.get("IspId")
        self.Status = params.get("Status")
        self.Arrears = params.get("Arrears")
        self.InstanceId = params.get("InstanceId")
        self.InstanceAlias = params.get("InstanceAlias")
        self.FreeAt = params.get("FreeAt")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.FreeSecond = params.get("FreeSecond")
        self.Type = params.get("Type")
        self.PayMode = params.get("PayMode")
        self.Bandwidth = params.get("Bandwidth")
        self.LatestPayMode = params.get("LatestPayMode")
        self.LatestBandwidth = params.get("LatestBandwidth")
        self.VpcName = params.get("VpcName")
        self.NatId = params.get("NatId")
        self.NatUid = params.get("NatUid")
        self.VpcIp = params.get("VpcIp")
        self.VpcId = params.get("VpcId")
        self.Exclusive = params.get("Exclusive")
        self.VpcCidr = params.get("VpcCidr")
        self.AclId = params.get("AclId")
        self.AclName = params.get("AclName")
        self.HInstanceId = params.get("HInstanceId")
        self.HInstanceAlias = params.get("HInstanceAlias")


class EipRsMap(AbstractModel):
    """EipId與InstanceId綁定關系

    """

    def __init__(self):
        """
        :param EipId: EIP實例 ID
        :type EipId: str
        :param InstanceId: 黑石物理機實例ID
        :type InstanceId: str
        """
        self.EipId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.EipId = params.get("EipId")
        self.InstanceId = params.get("InstanceId")


class ModifyEipAclRequest(AbstractModel):
    """ModifyEipAcl請求參數結構體

    """

    def __init__(self):
        """
        :param AclId: ACL 實例 ID
        :type AclId: str
        :param AclName: ACL 名稱
        :type AclName: str
        :param Status: ACL 狀态。0：無狀态 1：有狀态
        :type Status: int
        :param Type: 規則類型（in/out）。in：入站規則 out：出站規則
        :type Type: str
        :param Rules: ACL規則清單
        :type Rules: list of EipAclRule
        """
        self.AclId = None
        self.AclName = None
        self.Status = None
        self.Type = None
        self.Rules = None


    def _deserialize(self, params):
        self.AclId = params.get("AclId")
        self.AclName = params.get("AclName")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = EipAclRule()
                obj._deserialize(item)
                self.Rules.append(obj)


class ModifyEipAclResponse(AbstractModel):
    """ModifyEipAcl返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyEipChargeRequest(AbstractModel):
    """ModifyEipCharge請求參數結構體

    """

    def __init__(self):
        """
        :param PayMode: EIP計費方式，flow-流量計費；bandwidth-頻寬計費
        :type PayMode: str
        :param EipIds: Eip實例ID清單
        :type EipIds: list of str
        :param Bandwidth: 頻寬設定值（只在頻寬計費時生效）
        :type Bandwidth: int
        """
        self.PayMode = None
        self.EipIds = None
        self.Bandwidth = None


    def _deserialize(self, params):
        self.PayMode = params.get("PayMode")
        self.EipIds = params.get("EipIds")
        self.Bandwidth = params.get("Bandwidth")


class ModifyEipChargeResponse(AbstractModel):
    """ModifyEipCharge返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 修改計費模式的異步任務ID，可以通過查詢EIP任務狀态查詢任務狀态
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyEipNameRequest(AbstractModel):
    """ModifyEipName請求參數結構體

    """

    def __init__(self):
        """
        :param EipId: Eip實例ID，可通過/v2/DescribeEip 介面返回欄位中的 eipId獲取
        :type EipId: str
        :param EipName: EIP 實例别名
        :type EipName: str
        """
        self.EipId = None
        self.EipName = None


    def _deserialize(self, params):
        self.EipId = params.get("EipId")
        self.EipName = params.get("EipName")


class ModifyEipNameResponse(AbstractModel):
    """ModifyEipName返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnbindEipAclsRequest(AbstractModel):
    """UnbindEipAcls請求參數結構體

    """

    def __init__(self):
        """
        :param EipIdAclIdList: 待解關聯的 EIP 與 ACL清單
        :type EipIdAclIdList: list of EipAclMap
        """
        self.EipIdAclIdList = None


    def _deserialize(self, params):
        if params.get("EipIdAclIdList") is not None:
            self.EipIdAclIdList = []
            for item in params.get("EipIdAclIdList"):
                obj = EipAclMap()
                obj._deserialize(item)
                self.EipIdAclIdList.append(obj)


class UnbindEipAclsResponse(AbstractModel):
    """UnbindEipAcls返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnbindHostedRequest(AbstractModel):
    """UnbindHosted請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 托管機器實例ID
        :type InstanceId: str
        :param EipId: Eip實例ID，可通過DescribeBmEip 介面返回欄位中的 eipId獲取。Eip和EipId參數必須要填寫一個。
        :type EipId: str
        :param Eip: 彈性IP。Eip和EipId參數必須要填寫一個。
        :type Eip: str
        """
        self.InstanceId = None
        self.EipId = None
        self.Eip = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.EipId = params.get("EipId")
        self.Eip = params.get("Eip")


class UnbindHostedResponse(AbstractModel):
    """UnbindHosted返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步任務ID，可以通過EipBmQueryTask查詢任務狀态
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class UnbindRsListRequest(AbstractModel):
    """UnbindRsList請求參數結構體

    """

    def __init__(self):
        """
        :param EipRsList: 物理機綁定的EIP清單
        :type EipRsList: list of EipRsMap
        """
        self.EipRsList = None


    def _deserialize(self, params):
        if params.get("EipRsList") is not None:
            self.EipRsList = []
            for item in params.get("EipRsList"):
                obj = EipRsMap()
                obj._deserialize(item)
                self.EipRsList.append(obj)


class UnbindRsListResponse(AbstractModel):
    """UnbindRsList返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 解綁操作的異步任務ID，可以通過查詢EIP任務狀态查詢任務狀态
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class UnbindRsRequest(AbstractModel):
    """UnbindRs請求參數結構體

    """

    def __init__(self):
        """
        :param EipId: Eip實例ID
        :type EipId: str
        :param InstanceId: 物理服務器實例ID
        :type InstanceId: str
        """
        self.EipId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.EipId = params.get("EipId")
        self.InstanceId = params.get("InstanceId")


class UnbindRsResponse(AbstractModel):
    """UnbindRs返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 解綁操作的異步任務ID，可以通過查詢EIP任務狀态查詢任務狀态
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class UnbindVpcIpRequest(AbstractModel):
    """UnbindVpcIp請求參數結構體

    """

    def __init__(self):
        """
        :param EipId: Eip實例ID
        :type EipId: str
        :param VpcId: EIP歸屬VpcId，例如vpc-k7j1t2x1
        :type VpcId: str
        :param VpcIp: 綁定的VPC内IP網址
        :type VpcIp: str
        """
        self.EipId = None
        self.VpcId = None
        self.VpcIp = None


    def _deserialize(self, params):
        self.EipId = params.get("EipId")
        self.VpcId = params.get("VpcId")
        self.VpcIp = params.get("VpcIp")


class UnbindVpcIpResponse(AbstractModel):
    """UnbindVpcIp返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 綁定黑石物理機異步任務ID，可以通過查詢EIP任務狀态查詢任務狀态
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")