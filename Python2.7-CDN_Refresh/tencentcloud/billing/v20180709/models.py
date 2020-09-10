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


class ActionSummaryOverviewItem(AbstractModel):
    """按交易類型匯總消費詳情

    """

    def __init__(self):
        """
        :param ActionType: 交易類型：包年包月新購/續約/升降配/退款、按量計費扣費、調賬補償/扣費等類型
        :type ActionType: str
        :param ActionTypeName: 交易類型名稱
        :type ActionTypeName: str
        :param RealTotalCost: 實際花費
        :type RealTotalCost: str
        :param RealTotalCostRatio: 費用所占百分比，兩位小數
        :type RealTotalCostRatio: str
        :param CashPayAmount: 現金金額
        :type CashPayAmount: str
        :param IncentivePayAmount: 贈送金金額
        :type IncentivePayAmount: str
        :param VoucherPayAmount:  金額
        :type VoucherPayAmount: str
        :param BillMonth: 帳單月份，格式2019-08
        :type BillMonth: str
        """
        self.ActionType = None
        self.ActionTypeName = None
        self.RealTotalCost = None
        self.RealTotalCostRatio = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.BillMonth = None


    def _deserialize(self, params):
        self.ActionType = params.get("ActionType")
        self.ActionTypeName = params.get("ActionTypeName")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.BillMonth = params.get("BillMonth")


class BillDetail(AbstractModel):
    """帳單明細數據對象

    """

    def __init__(self):
        """
        :param BusinessCodeName: 産品名稱：雲産品大類，如雲伺服器CVM、雲資料庫MySQL
        :type BusinessCodeName: str
        :param ProductCodeName: 子産品名稱：雲産品子類，如雲伺服器CVM-标準型S1
        :type ProductCodeName: str
        :param PayModeName: 計費模式：包年包月和按量計費
        :type PayModeName: str
        :param ProjectName: 項目:資源所屬項目
        :type ProjectName: str
        :param RegionName: 區域：資源所屬地域，如華南地區（ ）
        :type RegionName: str
        :param ZoneName: 可用區：資源所屬可用區，如 三區
        :type ZoneName: str
        :param ResourceId: 資源實例ID
        :type ResourceId: str
        :param ResourceName: 實例名稱
        :type ResourceName: str
        :param ActionTypeName: 交易類型
        :type ActionTypeName: str
        :param OrderId: 訂單ID
        :type OrderId: str
        :param BillId: 交易ID
        :type BillId: str
        :param PayTime: 扣費時間
        :type PayTime: str
        :param FeeBeginTime: 開始使用時間
        :type FeeBeginTime: str
        :param FeeEndTime: 結束使用時間
        :type FeeEndTime: str
        :param ComponentSet: 元件清單
        :type ComponentSet: list of BillDetailComponent
        :param PayerUin: 支付者UIN
        :type PayerUin: str
        :param OwnerUin: 使用者UIN
        :type OwnerUin: str
        :param OperateUin: 操作者UIN
        :type OperateUin: str
        :param Tags: Tag 訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Tags: list of BillTagInfo
        :param BusinessCode: 商品名稱代碼（未開放的欄位）
注意：此欄位可能返回 null，表示取不到有效值。
        :type BusinessCode: str
        :param ProductCode: 子商品名稱代碼 （未開放的欄位）
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProductCode: str
        :param ActionType: 交易類型代碼（未開放的欄位）
注意：此欄位可能返回 null，表示取不到有效值。
        :type ActionType: str
        :param RegionId: 區域ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type RegionId: str
        """
        self.BusinessCodeName = None
        self.ProductCodeName = None
        self.PayModeName = None
        self.ProjectName = None
        self.RegionName = None
        self.ZoneName = None
        self.ResourceId = None
        self.ResourceName = None
        self.ActionTypeName = None
        self.OrderId = None
        self.BillId = None
        self.PayTime = None
        self.FeeBeginTime = None
        self.FeeEndTime = None
        self.ComponentSet = None
        self.PayerUin = None
        self.OwnerUin = None
        self.OperateUin = None
        self.Tags = None
        self.BusinessCode = None
        self.ProductCode = None
        self.ActionType = None
        self.RegionId = None


    def _deserialize(self, params):
        self.BusinessCodeName = params.get("BusinessCodeName")
        self.ProductCodeName = params.get("ProductCodeName")
        self.PayModeName = params.get("PayModeName")
        self.ProjectName = params.get("ProjectName")
        self.RegionName = params.get("RegionName")
        self.ZoneName = params.get("ZoneName")
        self.ResourceId = params.get("ResourceId")
        self.ResourceName = params.get("ResourceName")
        self.ActionTypeName = params.get("ActionTypeName")
        self.OrderId = params.get("OrderId")
        self.BillId = params.get("BillId")
        self.PayTime = params.get("PayTime")
        self.FeeBeginTime = params.get("FeeBeginTime")
        self.FeeEndTime = params.get("FeeEndTime")
        if params.get("ComponentSet") is not None:
            self.ComponentSet = []
            for item in params.get("ComponentSet"):
                obj = BillDetailComponent()
                obj._deserialize(item)
                self.ComponentSet.append(obj)
        self.PayerUin = params.get("PayerUin")
        self.OwnerUin = params.get("OwnerUin")
        self.OperateUin = params.get("OperateUin")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = BillTagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.BusinessCode = params.get("BusinessCode")
        self.ProductCode = params.get("ProductCode")
        self.ActionType = params.get("ActionType")
        self.RegionId = params.get("RegionId")


class BillDetailComponent(AbstractModel):
    """帳單明細元件對象

    """

    def __init__(self):
        """
        :param ComponentCodeName: 元件類型:資源元件類型的名稱，如内存、硬碟等
        :type ComponentCodeName: str
        :param ItemCodeName: 元件名稱:資源元件的名稱，如雲資料庫MySQL-内存等
        :type ItemCodeName: str
        :param SinglePrice: 元件刊例價:資源元件的原始價格，保持原始粒度
        :type SinglePrice: str
        :param SpecifiedPrice: 元件指定價
        :type SpecifiedPrice: str
        :param PriceUnit: 價格單位
        :type PriceUnit: str
        :param UsedAmount: 元件用量
        :type UsedAmount: str
        :param UsedAmountUnit: 元件用量單位
        :type UsedAmountUnit: str
        :param TimeSpan: 使用時長
        :type TimeSpan: str
        :param TimeUnitName: 時長單位
        :type TimeUnitName: str
        :param Cost: 元件原價
        :type Cost: str
        :param Discount: 折扣率
        :type Discount: str
        :param ReduceType: 優惠類型
        :type ReduceType: str
        :param RealCost: 優惠後總價
        :type RealCost: str
        :param VoucherPayAmount:  支付金額
        :type VoucherPayAmount: str
        :param CashPayAmount: 現金支付金額
        :type CashPayAmount: str
        :param IncentivePayAmount: 贈送帳戶支付金額
        :type IncentivePayAmount: str
        :param ItemCode: 元件類型代碼（未開放的欄位）
注意：此欄位可能返回 null，表示取不到有效值。
        :type ItemCode: str
        :param ComponentCode: 元件名稱代碼（未開放的欄位）
注意：此欄位可能返回 null，表示取不到有效值。
        :type ComponentCode: str
        :param ContractPrice: 合同價
注意：此欄位可能返回 null，表示取不到有效值。
        :type ContractPrice: str
        """
        self.ComponentCodeName = None
        self.ItemCodeName = None
        self.SinglePrice = None
        self.SpecifiedPrice = None
        self.PriceUnit = None
        self.UsedAmount = None
        self.UsedAmountUnit = None
        self.TimeSpan = None
        self.TimeUnitName = None
        self.Cost = None
        self.Discount = None
        self.ReduceType = None
        self.RealCost = None
        self.VoucherPayAmount = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.ItemCode = None
        self.ComponentCode = None
        self.ContractPrice = None


    def _deserialize(self, params):
        self.ComponentCodeName = params.get("ComponentCodeName")
        self.ItemCodeName = params.get("ItemCodeName")
        self.SinglePrice = params.get("SinglePrice")
        self.SpecifiedPrice = params.get("SpecifiedPrice")
        self.PriceUnit = params.get("PriceUnit")
        self.UsedAmount = params.get("UsedAmount")
        self.UsedAmountUnit = params.get("UsedAmountUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnitName = params.get("TimeUnitName")
        self.Cost = params.get("Cost")
        self.Discount = params.get("Discount")
        self.ReduceType = params.get("ReduceType")
        self.RealCost = params.get("RealCost")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.ItemCode = params.get("ItemCode")
        self.ComponentCode = params.get("ComponentCode")
        self.ContractPrice = params.get("ContractPrice")


class BillResourceSummary(AbstractModel):
    """帳單資源匯總數據對象

    """

    def __init__(self):
        """
        :param BusinessCodeName: 産品名稱：雲産品大類，如雲伺服器CVM、雲資料庫MySQL
        :type BusinessCodeName: str
        :param ProductCodeName: 子産品：雲産品子類，如雲伺服器CVM-标準型S1， 當沒有獲取到子産品名稱時，返回"-"
        :type ProductCodeName: str
        :param PayModeName: 計費模式：包年包月和按量計費
        :type PayModeName: str
        :param ProjectName: 項目
        :type ProjectName: str
        :param RegionName: 地域
        :type RegionName: str
        :param ZoneName: 可用區
        :type ZoneName: str
        :param ResourceId: 資源實例ID
        :type ResourceId: str
        :param ResourceName: 資源實例名稱
        :type ResourceName: str
        :param ActionTypeName: 交易類型：包年包月新購/續約/升降配/退款、按量計費扣費、調賬補償/扣費等類型
        :type ActionTypeName: str
        :param OrderId: 訂單ID
        :type OrderId: str
        :param PayTime: 扣費時間
        :type PayTime: str
        :param FeeBeginTime: 開始使用時間
        :type FeeBeginTime: str
        :param FeeEndTime: 結束使用時間
        :type FeeEndTime: str
        :param ConfigDesc: 配置描述
        :type ConfigDesc: str
        :param ExtendField1: 擴展欄位1
        :type ExtendField1: str
        :param ExtendField2: 擴展欄位2
        :type ExtendField2: str
        :param TotalCost: 原價，單位爲元
        :type TotalCost: str
        :param Discount: 折扣率
        :type Discount: str
        :param ReduceType: 優惠類型
        :type ReduceType: str
        :param RealTotalCost: 優惠後總價，單位爲元
        :type RealTotalCost: str
        :param VoucherPayAmount:  支付金額，單位爲元
        :type VoucherPayAmount: str
        :param CashPayAmount: 現金帳戶支付金額，單位爲元
        :type CashPayAmount: str
        :param IncentivePayAmount: 贈送帳戶支付金額，單位爲元
        :type IncentivePayAmount: str
        :param ExtendField3: 擴展欄位3
        :type ExtendField3: str
        :param ExtendField4: 擴展欄位4
        :type ExtendField4: str
        :param ExtendField5: 擴展欄位5
        :type ExtendField5: str
        :param Tags: Tag 訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Tags: list of BillTagInfo
        :param PayerUin: 付款方uin
        :type PayerUin: str
        :param OwnerUin: 資源所有者uin,無值則返回"-"
        :type OwnerUin: str
        :param OperateUin: 操作者uin,無值則返回"-"
        :type OperateUin: str
        :param BusinessCode: 商品名稱代碼
        :type BusinessCode: str
        :param ProductCode: 子商品名稱代碼
        :type ProductCode: str
        :param RegionId: 區域ID
        :type RegionId: int
        """
        self.BusinessCodeName = None
        self.ProductCodeName = None
        self.PayModeName = None
        self.ProjectName = None
        self.RegionName = None
        self.ZoneName = None
        self.ResourceId = None
        self.ResourceName = None
        self.ActionTypeName = None
        self.OrderId = None
        self.PayTime = None
        self.FeeBeginTime = None
        self.FeeEndTime = None
        self.ConfigDesc = None
        self.ExtendField1 = None
        self.ExtendField2 = None
        self.TotalCost = None
        self.Discount = None
        self.ReduceType = None
        self.RealTotalCost = None
        self.VoucherPayAmount = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.ExtendField3 = None
        self.ExtendField4 = None
        self.ExtendField5 = None
        self.Tags = None
        self.PayerUin = None
        self.OwnerUin = None
        self.OperateUin = None
        self.BusinessCode = None
        self.ProductCode = None
        self.RegionId = None


    def _deserialize(self, params):
        self.BusinessCodeName = params.get("BusinessCodeName")
        self.ProductCodeName = params.get("ProductCodeName")
        self.PayModeName = params.get("PayModeName")
        self.ProjectName = params.get("ProjectName")
        self.RegionName = params.get("RegionName")
        self.ZoneName = params.get("ZoneName")
        self.ResourceId = params.get("ResourceId")
        self.ResourceName = params.get("ResourceName")
        self.ActionTypeName = params.get("ActionTypeName")
        self.OrderId = params.get("OrderId")
        self.PayTime = params.get("PayTime")
        self.FeeBeginTime = params.get("FeeBeginTime")
        self.FeeEndTime = params.get("FeeEndTime")
        self.ConfigDesc = params.get("ConfigDesc")
        self.ExtendField1 = params.get("ExtendField1")
        self.ExtendField2 = params.get("ExtendField2")
        self.TotalCost = params.get("TotalCost")
        self.Discount = params.get("Discount")
        self.ReduceType = params.get("ReduceType")
        self.RealTotalCost = params.get("RealTotalCost")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.ExtendField3 = params.get("ExtendField3")
        self.ExtendField4 = params.get("ExtendField4")
        self.ExtendField5 = params.get("ExtendField5")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = BillTagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.PayerUin = params.get("PayerUin")
        self.OwnerUin = params.get("OwnerUin")
        self.OperateUin = params.get("OperateUin")
        self.BusinessCode = params.get("BusinessCode")
        self.ProductCode = params.get("ProductCode")
        self.RegionId = params.get("RegionId")


class BillTagInfo(AbstractModel):
    """帳單 Tag 訊息

    """

    def __init__(self):
        """
        :param TagKey: 分賬标簽鍵
        :type TagKey: str
        :param TagValue: 标簽值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class BillTransactionInfo(AbstractModel):
    """收支明細的流水訊息

    """

    def __init__(self):
        """
        :param ActionType: 收支類型：deduct 扣費, recharge 儲值, return 退費， block 鎖定, unblock 取消鎖定
        :type ActionType: str
        :param Amount: 流水金額，單位（分）；正數表示入賬，負數表示出賬
        :type Amount: int
        :param Balance: 可用餘額，單位（分）；正數表示入賬，負數表示出賬
        :type Balance: int
        :param BillId: 流水号，如20190131020000236005203583326401
        :type BillId: str
        :param OperationInfo: 描述訊息
        :type OperationInfo: str
        :param OperationTime: 操作時間"2019-01-31 23:35:10.000"
        :type OperationTime: str
        :param Cash: 現金帳戶餘額，單位（分）
        :type Cash: int
        :param Incentive: 贈送金餘額，單位（分）
        :type Incentive: int
        :param Freezing: 鎖定餘額，單位（分）
        :type Freezing: int
        """
        self.ActionType = None
        self.Amount = None
        self.Balance = None
        self.BillId = None
        self.OperationInfo = None
        self.OperationTime = None
        self.Cash = None
        self.Incentive = None
        self.Freezing = None


    def _deserialize(self, params):
        self.ActionType = params.get("ActionType")
        self.Amount = params.get("Amount")
        self.Balance = params.get("Balance")
        self.BillId = params.get("BillId")
        self.OperationInfo = params.get("OperationInfo")
        self.OperationTime = params.get("OperationTime")
        self.Cash = params.get("Cash")
        self.Incentive = params.get("Incentive")
        self.Freezing = params.get("Freezing")


class BusinessSummaryOverviewItem(AbstractModel):
    """按産品匯總産品詳情

    """

    def __init__(self):
        """
        :param BusinessCode: 産品碼
注意：此欄位可能返回 null，表示取不到有效值。
        :type BusinessCode: str
        :param BusinessCodeName: 産品名稱：雲産品大類，如雲伺服器CVM、雲資料庫MySQL
        :type BusinessCodeName: str
        :param RealTotalCost: 實際花費
        :type RealTotalCost: str
        :param RealTotalCostRatio: 費用所占百分比，兩位小數
        :type RealTotalCostRatio: str
        :param CashPayAmount: 現金金額
        :type CashPayAmount: str
        :param IncentivePayAmount: 贈送金金額
        :type IncentivePayAmount: str
        :param VoucherPayAmount:  金額
        :type VoucherPayAmount: str
        :param BillMonth: 帳單月份，格式2019-08
        :type BillMonth: str
        """
        self.BusinessCode = None
        self.BusinessCodeName = None
        self.RealTotalCost = None
        self.RealTotalCostRatio = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.BillMonth = None


    def _deserialize(self, params):
        self.BusinessCode = params.get("BusinessCode")
        self.BusinessCodeName = params.get("BusinessCodeName")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.BillMonth = params.get("BillMonth")


class BusinessSummaryTotal(AbstractModel):
    """按産品匯總總費用

    """

    def __init__(self):
        """
        :param RealTotalCost: 總花費
        :type RealTotalCost: str
        :param VoucherPayAmount:  金額
        :type VoucherPayAmount: str
        :param IncentivePayAmount: 贈送金金額
        :type IncentivePayAmount: str
        :param CashPayAmount: 現金金額
        :type CashPayAmount: str
        """
        self.RealTotalCost = None
        self.VoucherPayAmount = None
        self.IncentivePayAmount = None
        self.CashPayAmount = None


    def _deserialize(self, params):
        self.RealTotalCost = params.get("RealTotalCost")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.CashPayAmount = params.get("CashPayAmount")


class ConditionBusiness(AbstractModel):
    """産品過濾條件

    """

    def __init__(self):
        """
        :param BusinessCode: 産品碼
        :type BusinessCode: str
        :param BusinessCodeName: 産品名稱
        :type BusinessCodeName: str
        """
        self.BusinessCode = None
        self.BusinessCodeName = None


    def _deserialize(self, params):
        self.BusinessCode = params.get("BusinessCode")
        self.BusinessCodeName = params.get("BusinessCodeName")


class ConditionPayMode(AbstractModel):
    """付費模式過濾條件

    """

    def __init__(self):
        """
        :param PayMode: 付費模式
        :type PayMode: str
        :param PayModeName: 付費模式名稱
        :type PayModeName: str
        """
        self.PayMode = None
        self.PayModeName = None


    def _deserialize(self, params):
        self.PayMode = params.get("PayMode")
        self.PayModeName = params.get("PayModeName")


class ConditionProject(AbstractModel):
    """項目過濾條件

    """

    def __init__(self):
        """
        :param ProjectId: 項目ID
        :type ProjectId: str
        :param ProjectName: 項目名稱
        :type ProjectName: str
        """
        self.ProjectId = None
        self.ProjectName = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")


class ConditionRegion(AbstractModel):
    """地域過濾條件

    """

    def __init__(self):
        """
        :param RegionId: 地域ID
        :type RegionId: str
        :param RegionName: 地域名稱
        :type RegionName: str
        """
        self.RegionId = None
        self.RegionName = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")


class Conditions(AbstractModel):
    """帳單篩選條件對象

    """

    def __init__(self):
        """
        :param TimeRange: 只支援6和12兩個值
        :type TimeRange: int
        :param BusinessCode: 産品編碼
        :type BusinessCode: str
        :param ProjectId: 項目ID
        :type ProjectId: int
        :param RegionId: 地域ID
        :type RegionId: int
        :param PayMode: 付費模式，可選prePay和postPay
        :type PayMode: str
        :param ResourceKeyword: 資源關鍵字
        :type ResourceKeyword: str
        :param BusinessCodes: 産品編碼
        :type BusinessCodes: list of str
        :param ProductCodes: 子産品編碼
        :type ProductCodes: list of str
        :param RegionIds: 地域ID
        :type RegionIds: list of int
        :param ProjectIds: 項目ID
        :type ProjectIds: list of int
        :param PayModes: 付費模式，可選prePay和postPay
        :type PayModes: list of str
        :param ActionTypes: 交易類型
        :type ActionTypes: list of str
        :param HideFreeCost: 是否隐藏0元流水
        :type HideFreeCost: int
        :param OrderByCost: 排序規則，可選desc和asc
        :type OrderByCost: str
        :param BillIds: 交易ID
        :type BillIds: list of str
        :param ComponentCodes: 元件編碼
        :type ComponentCodes: list of str
        :param FileIds: 文件ID
        :type FileIds: list of str
        :param FileTypes: 文件類型
        :type FileTypes: list of str
        :param Status: 狀态
        :type Status: list of int non-negative
        """
        self.TimeRange = None
        self.BusinessCode = None
        self.ProjectId = None
        self.RegionId = None
        self.PayMode = None
        self.ResourceKeyword = None
        self.BusinessCodes = None
        self.ProductCodes = None
        self.RegionIds = None
        self.ProjectIds = None
        self.PayModes = None
        self.ActionTypes = None
        self.HideFreeCost = None
        self.OrderByCost = None
        self.BillIds = None
        self.ComponentCodes = None
        self.FileIds = None
        self.FileTypes = None
        self.Status = None


    def _deserialize(self, params):
        self.TimeRange = params.get("TimeRange")
        self.BusinessCode = params.get("BusinessCode")
        self.ProjectId = params.get("ProjectId")
        self.RegionId = params.get("RegionId")
        self.PayMode = params.get("PayMode")
        self.ResourceKeyword = params.get("ResourceKeyword")
        self.BusinessCodes = params.get("BusinessCodes")
        self.ProductCodes = params.get("ProductCodes")
        self.RegionIds = params.get("RegionIds")
        self.ProjectIds = params.get("ProjectIds")
        self.PayModes = params.get("PayModes")
        self.ActionTypes = params.get("ActionTypes")
        self.HideFreeCost = params.get("HideFreeCost")
        self.OrderByCost = params.get("OrderByCost")
        self.BillIds = params.get("BillIds")
        self.ComponentCodes = params.get("ComponentCodes")
        self.FileIds = params.get("FileIds")
        self.FileTypes = params.get("FileTypes")
        self.Status = params.get("Status")


class ConsumptionBusinessSummaryDataItem(AbstractModel):
    """消耗按産品匯總詳情

    """

    def __init__(self):
        """
        :param BusinessCode: 産品碼
        :type BusinessCode: str
        :param BusinessCodeName: 産品名稱
        :type BusinessCodeName: str
        :param RealTotalCost: 折後總價
        :type RealTotalCost: str
        :param Trend: 費用趨勢
        :type Trend: :class:`taifucloudcloud.billing.v20180709.models.ConsumptionSummaryTrend`
        """
        self.BusinessCode = None
        self.BusinessCodeName = None
        self.RealTotalCost = None
        self.Trend = None


    def _deserialize(self, params):
        self.BusinessCode = params.get("BusinessCode")
        self.BusinessCodeName = params.get("BusinessCodeName")
        self.RealTotalCost = params.get("RealTotalCost")
        if params.get("Trend") is not None:
            self.Trend = ConsumptionSummaryTrend()
            self.Trend._deserialize(params.get("Trend"))


class ConsumptionProjectSummaryDataItem(AbstractModel):
    """消耗按項目匯總詳情

    """

    def __init__(self):
        """
        :param ProjectId: 項目ID
        :type ProjectId: str
        :param ProjectName: 項目名稱
        :type ProjectName: str
        :param RealTotalCost: 折後總價
        :type RealTotalCost: str
        :param Trend: 趨勢
        :type Trend: :class:`taifucloudcloud.billing.v20180709.models.ConsumptionSummaryTrend`
        :param Business: 産品消耗詳情
        :type Business: list of ConsumptionBusinessSummaryDataItem
        """
        self.ProjectId = None
        self.ProjectName = None
        self.RealTotalCost = None
        self.Trend = None
        self.Business = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.RealTotalCost = params.get("RealTotalCost")
        if params.get("Trend") is not None:
            self.Trend = ConsumptionSummaryTrend()
            self.Trend._deserialize(params.get("Trend"))
        if params.get("Business") is not None:
            self.Business = []
            for item in params.get("Business"):
                obj = ConsumptionBusinessSummaryDataItem()
                obj._deserialize(item)
                self.Business.append(obj)


class ConsumptionRegionSummaryDataItem(AbstractModel):
    """消耗按地域匯總詳情

    """

    def __init__(self):
        """
        :param RegionId: 地域ID
        :type RegionId: str
        :param RegionName: 地域名稱
        :type RegionName: str
        :param RealTotalCost: 折後總價
        :type RealTotalCost: str
        :param Trend: 趨勢
        :type Trend: :class:`taifucloudcloud.billing.v20180709.models.ConsumptionSummaryTrend`
        :param Business: 産品消費詳情
        :type Business: list of ConsumptionBusinessSummaryDataItem
        """
        self.RegionId = None
        self.RegionName = None
        self.RealTotalCost = None
        self.Trend = None
        self.Business = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        self.RealTotalCost = params.get("RealTotalCost")
        if params.get("Trend") is not None:
            self.Trend = ConsumptionSummaryTrend()
            self.Trend._deserialize(params.get("Trend"))
        if params.get("Business") is not None:
            self.Business = []
            for item in params.get("Business"):
                obj = ConsumptionBusinessSummaryDataItem()
                obj._deserialize(item)
                self.Business.append(obj)


class ConsumptionResourceSummaryConditionValue(AbstractModel):
    """消耗按資源匯總過濾條件

    """

    def __init__(self):
        """
        :param Business: 産品清單
        :type Business: list of ConditionBusiness
        :param Project: 項目清單
        :type Project: list of ConditionProject
        :param Region: 地域清單
        :type Region: list of ConditionRegion
        :param PayMode: 付費模式清單
        :type PayMode: list of ConditionPayMode
        """
        self.Business = None
        self.Project = None
        self.Region = None
        self.PayMode = None


    def _deserialize(self, params):
        if params.get("Business") is not None:
            self.Business = []
            for item in params.get("Business"):
                obj = ConditionBusiness()
                obj._deserialize(item)
                self.Business.append(obj)
        if params.get("Project") is not None:
            self.Project = []
            for item in params.get("Project"):
                obj = ConditionProject()
                obj._deserialize(item)
                self.Project.append(obj)
        if params.get("Region") is not None:
            self.Region = []
            for item in params.get("Region"):
                obj = ConditionRegion()
                obj._deserialize(item)
                self.Region.append(obj)
        if params.get("PayMode") is not None:
            self.PayMode = []
            for item in params.get("PayMode"):
                obj = ConditionPayMode()
                obj._deserialize(item)
                self.PayMode.append(obj)


class ConsumptionResourceSummaryDataItem(AbstractModel):
    """消耗按資源匯總詳情

    """

    def __init__(self):
        """
        :param ResourceId: 資源ID
        :type ResourceId: str
        :param ResourceName: 資源名稱
        :type ResourceName: str
        :param RealTotalCost: 折後總價
        :type RealTotalCost: str
        :param CashPayAmount: 現金花費
        :type CashPayAmount: str
        :param ProjectId: 項目ID
        :type ProjectId: str
        :param ProjectName: 項目名稱
        :type ProjectName: str
        :param RegionId: 地域ID
        :type RegionId: str
        :param RegionName: 地域名稱
        :type RegionName: str
        :param PayMode: 付費模式
        :type PayMode: str
        :param PayModeName: 付費模式名稱
        :type PayModeName: str
        :param BusinessCode: 産品碼
        :type BusinessCode: str
        :param BusinessCodeName: 産品名稱
        :type BusinessCodeName: str
        :param ConsumptionTypeName: 消耗類型
        :type ConsumptionTypeName: str
        """
        self.ResourceId = None
        self.ResourceName = None
        self.RealTotalCost = None
        self.CashPayAmount = None
        self.ProjectId = None
        self.ProjectName = None
        self.RegionId = None
        self.RegionName = None
        self.PayMode = None
        self.PayModeName = None
        self.BusinessCode = None
        self.BusinessCodeName = None
        self.ConsumptionTypeName = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.ResourceName = params.get("ResourceName")
        self.RealTotalCost = params.get("RealTotalCost")
        self.CashPayAmount = params.get("CashPayAmount")
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        self.PayMode = params.get("PayMode")
        self.PayModeName = params.get("PayModeName")
        self.BusinessCode = params.get("BusinessCode")
        self.BusinessCodeName = params.get("BusinessCodeName")
        self.ConsumptionTypeName = params.get("ConsumptionTypeName")


class ConsumptionSummaryTotal(AbstractModel):
    """消耗匯總詳情

    """

    def __init__(self):
        """
        :param RealTotalCost: 折後總價
        :type RealTotalCost: str
        """
        self.RealTotalCost = None


    def _deserialize(self, params):
        self.RealTotalCost = params.get("RealTotalCost")


class ConsumptionSummaryTrend(AbstractModel):
    """消耗費用趨勢

    """

    def __init__(self):
        """
        :param Type: 趨勢類型，upward上升/downward下降/none無
        :type Type: str
        :param Value: 趨勢值，Type爲none是該欄位值爲null
注意：此欄位可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Type = None
        self.Value = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Value = params.get("Value")


class CostComponentSet(AbstractModel):
    """消耗元件明細

    """

    def __init__(self):
        """
        :param ComponentCodeName: 元件類型名稱
        :type ComponentCodeName: str
        :param ItemCodeName: 元件名稱
        :type ItemCodeName: str
        :param SinglePrice: 刊例價
        :type SinglePrice: str
        :param PriceUnit: 刊例價單位
        :type PriceUnit: str
        :param UsedAmount: 用量
        :type UsedAmount: str
        :param UsedAmountUnit: 用量單位
        :type UsedAmountUnit: str
        :param Cost: 原價
        :type Cost: str
        :param Discount: 折扣
        :type Discount: str
        :param RealCost: 折後價
        :type RealCost: str
        :param VoucherPayAmount:  支付金額
        :type VoucherPayAmount: str
        :param CashPayAmount: 現金支付金額
        :type CashPayAmount: str
        :param IncentivePayAmount: 贈送金支付金額
        :type IncentivePayAmount: str
        """
        self.ComponentCodeName = None
        self.ItemCodeName = None
        self.SinglePrice = None
        self.PriceUnit = None
        self.UsedAmount = None
        self.UsedAmountUnit = None
        self.Cost = None
        self.Discount = None
        self.RealCost = None
        self.VoucherPayAmount = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None


    def _deserialize(self, params):
        self.ComponentCodeName = params.get("ComponentCodeName")
        self.ItemCodeName = params.get("ItemCodeName")
        self.SinglePrice = params.get("SinglePrice")
        self.PriceUnit = params.get("PriceUnit")
        self.UsedAmount = params.get("UsedAmount")
        self.UsedAmountUnit = params.get("UsedAmountUnit")
        self.Cost = params.get("Cost")
        self.Discount = params.get("Discount")
        self.RealCost = params.get("RealCost")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")


class CostDetail(AbstractModel):
    """消耗明細數據類型

    """

    def __init__(self):
        """
        :param PayerUin: 支付者uin
        :type PayerUin: str
        :param BusinessCodeName: 業務名稱
        :type BusinessCodeName: str
        :param ProductCodeName: 産品名稱
        :type ProductCodeName: str
        :param PayModeName: 計費模式名稱
        :type PayModeName: str
        :param ProjectName: 項目名稱
        :type ProjectName: str
        :param RegionName: 區域名稱
        :type RegionName: str
        :param ZoneName: 地區名稱
        :type ZoneName: str
        :param ResourceId: 資源id
        :type ResourceId: str
        :param ResourceName: 資源名稱
        :type ResourceName: str
        :param ActionTypeName: 類型名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ActionTypeName: str
        :param OrderId: 訂單id
        :type OrderId: str
        :param BillId: 交易id
        :type BillId: str
        :param FeeBeginTime: 費用開始時間
        :type FeeBeginTime: str
        :param FeeEndTime: 費用結束時間
        :type FeeEndTime: str
        :param ComponentSet: 元件明細
        :type ComponentSet: list of CostComponentSet
        :param ProductCode: 産品代碼
        :type ProductCode: str
        """
        self.PayerUin = None
        self.BusinessCodeName = None
        self.ProductCodeName = None
        self.PayModeName = None
        self.ProjectName = None
        self.RegionName = None
        self.ZoneName = None
        self.ResourceId = None
        self.ResourceName = None
        self.ActionTypeName = None
        self.OrderId = None
        self.BillId = None
        self.FeeBeginTime = None
        self.FeeEndTime = None
        self.ComponentSet = None
        self.ProductCode = None


    def _deserialize(self, params):
        self.PayerUin = params.get("PayerUin")
        self.BusinessCodeName = params.get("BusinessCodeName")
        self.ProductCodeName = params.get("ProductCodeName")
        self.PayModeName = params.get("PayModeName")
        self.ProjectName = params.get("ProjectName")
        self.RegionName = params.get("RegionName")
        self.ZoneName = params.get("ZoneName")
        self.ResourceId = params.get("ResourceId")
        self.ResourceName = params.get("ResourceName")
        self.ActionTypeName = params.get("ActionTypeName")
        self.OrderId = params.get("OrderId")
        self.BillId = params.get("BillId")
        self.FeeBeginTime = params.get("FeeBeginTime")
        self.FeeEndTime = params.get("FeeEndTime")
        if params.get("ComponentSet") is not None:
            self.ComponentSet = []
            for item in params.get("ComponentSet"):
                obj = CostComponentSet()
                obj._deserialize(item)
                self.ComponentSet.append(obj)
        self.ProductCode = params.get("ProductCode")


class Deal(AbstractModel):
    """訂單數據對象

    """

    def __init__(self):
        """
        :param OrderId: 訂單号
        :type OrderId: str
        :param Status: 訂單狀态
        :type Status: int
        :param Payer: 支付者
        :type Payer: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param Creator: 創建人
        :type Creator: str
        :param RealTotalCost: 實際支付金額（分）
        :type RealTotalCost: int
        :param VoucherDecline:  抵扣金額（分）
        :type VoucherDecline: int
        :param ProjectId: 項目ID
        :type ProjectId: int
        :param GoodsCategoryId: 産品分類ID
        :type GoodsCategoryId: int
        :param ProductInfo: 産品詳情
        :type ProductInfo: list of ProductInfo
        :param TimeSpan: 時長
        :type TimeSpan: float
        :param TimeUnit: 時間單位
        :type TimeUnit: str
        :param Currency: 貨币單位
        :type Currency: str
        :param Policy: 折扣率
        :type Policy: float
        :param Price: 單價（分）
        :type Price: float
        :param TotalCost: 原價（分）
        :type TotalCost: float
        :param ProductCode: 産品編碼
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProductCode: str
        :param SubProductCode: 子産品編碼
        :type SubProductCode: str
        """
        self.OrderId = None
        self.Status = None
        self.Payer = None
        self.CreateTime = None
        self.Creator = None
        self.RealTotalCost = None
        self.VoucherDecline = None
        self.ProjectId = None
        self.GoodsCategoryId = None
        self.ProductInfo = None
        self.TimeSpan = None
        self.TimeUnit = None
        self.Currency = None
        self.Policy = None
        self.Price = None
        self.TotalCost = None
        self.ProductCode = None
        self.SubProductCode = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.Status = params.get("Status")
        self.Payer = params.get("Payer")
        self.CreateTime = params.get("CreateTime")
        self.Creator = params.get("Creator")
        self.RealTotalCost = params.get("RealTotalCost")
        self.VoucherDecline = params.get("VoucherDecline")
        self.ProjectId = params.get("ProjectId")
        self.GoodsCategoryId = params.get("GoodsCategoryId")
        if params.get("ProductInfo") is not None:
            self.ProductInfo = []
            for item in params.get("ProductInfo"):
                obj = ProductInfo()
                obj._deserialize(item)
                self.ProductInfo.append(obj)
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnit = params.get("TimeUnit")
        self.Currency = params.get("Currency")
        self.Policy = params.get("Policy")
        self.Price = params.get("Price")
        self.TotalCost = params.get("TotalCost")
        self.ProductCode = params.get("ProductCode")
        self.SubProductCode = params.get("SubProductCode")


class DescribeAccountBalanceRequest(AbstractModel):
    """DescribeAccountBalance請求參數結構體

    """


class DescribeAccountBalanceResponse(AbstractModel):
    """DescribeAccountBalance返回參數結構體

    """

    def __init__(self):
        """
        :param Balance: 雲帳戶訊息中的”展示可用餘額”欄位，單位爲"分"
        :type Balance: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Balance = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Balance = params.get("Balance")
        self.RequestId = params.get("RequestId")


class DescribeBillDetailRequest(AbstractModel):
    """DescribeBillDetail請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 數量，最大值爲100
        :type Limit: int
        :param PeriodType: 週期類型，byUsedTime按計費週期/byPayTime按扣費週期。需要與費用中心該月份帳單的週期保持一緻。您可前往[帳單概覽](https://console.cloud.taifucloud.com/expense/bill/overview)頁面頂部檢視确認您的帳單統計週期類型。
        :type PeriodType: str
        :param Month: 月份，格式爲yyyy-mm，Month和BeginTime&EndTime必傳一個，如果有傳BeginTime&EndTime則Month欄位無效。不能早于開通帳單2.0的月份，最多可拉取24個月内的數據。
        :type Month: str
        :param BeginTime: 週期開始時間，格式爲Y-m-d H:i:s，Month和BeginTime&EndTime必傳一個，如果有該欄位則Month欄位無效。BeginTime和EndTime必須一起傳。不能早于開通帳單2.0的月份，最多可拉取24個月内的數據。(不支援跨月查詢)
        :type BeginTime: str
        :param EndTime: 週期結束時間，格式爲Y-m-d H:i:s，Month和BeginTime&EndTime必傳一個，如果有該欄位則Month欄位無效。BeginTime和EndTime必須一起傳。不能早于開通帳單2.0的月份，最多可拉取24個月内的數據。（不支援跨月查詢）
        :type EndTime: str
        :param NeedRecordNum: 是否需要訪問清單的總記錄數，用于前端分頁
1-表示需要， 0-表示不需要
        :type NeedRecordNum: int
        :param ProductCode: 查詢指定産品訊息
        :type ProductCode: str
        :param PayMode: 付費模式 prePay/postPay
        :type PayMode: str
        :param ResourceId: 查詢指定資源訊息
        :type ResourceId: str
        :param ActionType: 查詢交易類型。如 按量計費日結，按量計費小時結 等
        :type ActionType: str
        """
        self.Offset = None
        self.Limit = None
        self.PeriodType = None
        self.Month = None
        self.BeginTime = None
        self.EndTime = None
        self.NeedRecordNum = None
        self.ProductCode = None
        self.PayMode = None
        self.ResourceId = None
        self.ActionType = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PeriodType = params.get("PeriodType")
        self.Month = params.get("Month")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.NeedRecordNum = params.get("NeedRecordNum")
        self.ProductCode = params.get("ProductCode")
        self.PayMode = params.get("PayMode")
        self.ResourceId = params.get("ResourceId")
        self.ActionType = params.get("ActionType")


class DescribeBillDetailResponse(AbstractModel):
    """DescribeBillDetail返回參數結構體

    """

    def __init__(self):
        """
        :param DetailSet: 詳情清單
        :type DetailSet: list of BillDetail
        :param Total: 總記錄數
注意：此欄位可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DetailSet = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DetailSet") is not None:
            self.DetailSet = []
            for item in params.get("DetailSet"):
                obj = BillDetail()
                obj._deserialize(item)
                self.DetailSet.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeBillListRequest(AbstractModel):
    """DescribeBillList請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 查詢範圍的起始時間（包含）
        :type StartTime: str
        :param EndTime: 查詢範圍的結束時間（包含）
        :type EndTime: str
        :param Offset: 翻頁偏移量，初始值爲0
        :type Offset: int
        :param Limit: 每頁的限制數量
        :type Limit: int
        :param PayType: 交易類型： all所有交易類型，recharge儲值，return退款，unblock取消鎖定，agentin資金轉入，advanced墊付，cash提現，deduct扣費，block鎖定，agentout資金轉出，repay墊付回款，repayment還款(僅國際信用帳戶)，adj_refund調增(僅國際信用帳戶)，adj_deduct調減(僅國際信用帳戶)
        :type PayType: list of str
        :param SubPayType: 扣費模式，當所選的交易類型中包含扣費deduct時有意義： all所有扣費類型，trade預付費支付，hour_h按量小時結，hour_d按量日結，hour_m按量月結，decompensate調賬扣費，other其他扣費
        :type SubPayType: list of str
        :param WithZeroAmount: 是否返回0元交易金額的交易項，取值：0-不返回，1-返回。不傳該參數則不返回
        :type WithZeroAmount: int
        """
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.PayType = None
        self.SubPayType = None
        self.WithZeroAmount = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PayType = params.get("PayType")
        self.SubPayType = params.get("SubPayType")
        self.WithZeroAmount = params.get("WithZeroAmount")


class DescribeBillListResponse(AbstractModel):
    """DescribeBillList返回參數結構體

    """

    def __init__(self):
        """
        :param TransactionList: 收支明細清單
        :type TransactionList: list of BillTransactionInfo
        :param Total: 總條數
        :type Total: int
        :param ReturnAmount: 退費總額，單位（分）
        :type ReturnAmount: float
        :param RechargeAmount: 儲值總額，單位（分）
        :type RechargeAmount: float
        :param BlockAmount: 鎖定總額，單位（分）
        :type BlockAmount: float
        :param UnblockAmount: 取消鎖定總額，單位（分）
        :type UnblockAmount: float
        :param DeductAmount: 扣費總額，單位（分）
        :type DeductAmount: float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TransactionList = None
        self.Total = None
        self.ReturnAmount = None
        self.RechargeAmount = None
        self.BlockAmount = None
        self.UnblockAmount = None
        self.DeductAmount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TransactionList") is not None:
            self.TransactionList = []
            for item in params.get("TransactionList"):
                obj = BillTransactionInfo()
                obj._deserialize(item)
                self.TransactionList.append(obj)
        self.Total = params.get("Total")
        self.ReturnAmount = params.get("ReturnAmount")
        self.RechargeAmount = params.get("RechargeAmount")
        self.BlockAmount = params.get("BlockAmount")
        self.UnblockAmount = params.get("UnblockAmount")
        self.DeductAmount = params.get("DeductAmount")
        self.RequestId = params.get("RequestId")


class DescribeBillResourceSummaryRequest(AbstractModel):
    """DescribeBillResourceSummary請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 數量，最大值爲1000
        :type Limit: int
        :param PeriodType: 週期類型，byUsedTime按計費週期/byPayTime按扣費週期。需要與費用中心該月份帳單的週期保持一緻。您可前往[帳單概覽](https://console.cloud.taifucloud.com/expense/bill/overview)頁面頂部檢視确認您的帳單統計週期類型。
        :type PeriodType: str
        :param Month: 月份，格式爲yyyy-mm。不能早于開通帳單2.0的月份，最多可拉取24個月内的數據。
        :type Month: str
        :param NeedRecordNum: 是否需要訪問清單的總記錄數，用于前端分頁
1-表示需要， 0-表示不需要
        :type NeedRecordNum: int
        :param ActionType: 查詢交易類型。如 按量計費日結，按量計費小時結 等
        :type ActionType: str
        """
        self.Offset = None
        self.Limit = None
        self.PeriodType = None
        self.Month = None
        self.NeedRecordNum = None
        self.ActionType = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PeriodType = params.get("PeriodType")
        self.Month = params.get("Month")
        self.NeedRecordNum = params.get("NeedRecordNum")
        self.ActionType = params.get("ActionType")


class DescribeBillResourceSummaryResponse(AbstractModel):
    """DescribeBillResourceSummary返回參數結構體

    """

    def __init__(self):
        """
        :param ResourceSummarySet: 資源匯總清單
        :type ResourceSummarySet: list of BillResourceSummary
        :param Total: 資源匯總清單總數
注意：此欄位可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ResourceSummarySet = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResourceSummarySet") is not None:
            self.ResourceSummarySet = []
            for item in params.get("ResourceSummarySet"):
                obj = BillResourceSummary()
                obj._deserialize(item)
                self.ResourceSummarySet.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeBillSummaryByPayModeRequest(AbstractModel):
    """DescribeBillSummaryByPayMode請求參數結構體

    """

    def __init__(self):
        """
        :param PayerUin: 查詢帳單數據的用戶UIN
        :type PayerUin: str
        :param BeginTime: 目前只支援傳當月開始，且必須和EndTime爲相同月份，例 2018-09-01 00:00:00
        :type BeginTime: str
        :param EndTime: 目前只支援傳當月結束，且必須和BeginTime爲相同月份，例 2018-09-30 23:59:59
        :type EndTime: str
        """
        self.PayerUin = None
        self.BeginTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.PayerUin = params.get("PayerUin")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")


class DescribeBillSummaryByPayModeResponse(AbstractModel):
    """DescribeBillSummaryByPayMode返回參數結構體

    """

    def __init__(self):
        """
        :param Ready: 數據是否準備好，0未準備好，1準備好
        :type Ready: int
        :param SummaryOverview: 各付費模式花費分布詳情
注意：此欄位可能返回 null，表示取不到有效值。
        :type SummaryOverview: list of PayModeSummaryOverviewItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Ready = None
        self.SummaryOverview = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ready = params.get("Ready")
        if params.get("SummaryOverview") is not None:
            self.SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = PayModeSummaryOverviewItem()
                obj._deserialize(item)
                self.SummaryOverview.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBillSummaryByProductRequest(AbstractModel):
    """DescribeBillSummaryByProduct請求參數結構體

    """

    def __init__(self):
        """
        :param PayerUin: 查詢帳單數據的用戶UIN
        :type PayerUin: str
        :param BeginTime: 目前只支援傳當月開始，且必須和EndTime爲相同月份，例 2018-09-01 00:00:00
        :type BeginTime: str
        :param EndTime: 目前只支援傳當月結束，且必須和BeginTime爲相同月份，例 2018-09-30 23:59:59
        :type EndTime: str
        """
        self.PayerUin = None
        self.BeginTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.PayerUin = params.get("PayerUin")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")


class DescribeBillSummaryByProductResponse(AbstractModel):
    """DescribeBillSummaryByProduct返回參數結構體

    """

    def __init__(self):
        """
        :param Ready: 數據是否準備好，0未準備好，1準備好
        :type Ready: int
        :param SummaryTotal: 總花費詳情
注意：此欄位可能返回 null，表示取不到有效值。
        :type SummaryTotal: :class:`taifucloudcloud.billing.v20180709.models.BusinessSummaryTotal`
        :param SummaryOverview: 各産品花費分布
注意：此欄位可能返回 null，表示取不到有效值。
        :type SummaryOverview: list of BusinessSummaryOverviewItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Ready = None
        self.SummaryTotal = None
        self.SummaryOverview = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ready = params.get("Ready")
        if params.get("SummaryTotal") is not None:
            self.SummaryTotal = BusinessSummaryTotal()
            self.SummaryTotal._deserialize(params.get("SummaryTotal"))
        if params.get("SummaryOverview") is not None:
            self.SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = BusinessSummaryOverviewItem()
                obj._deserialize(item)
                self.SummaryOverview.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBillSummaryByProjectRequest(AbstractModel):
    """DescribeBillSummaryByProject請求參數結構體

    """

    def __init__(self):
        """
        :param PayerUin: 查詢帳單數據的用戶UIN
        :type PayerUin: str
        :param BeginTime: 目前只支援傳當月開始，且必須和EndTime爲相同月份，例 2018-09-01 00:00:00
        :type BeginTime: str
        :param EndTime: 目前只支援傳當月結束，且必須和BeginTime爲相同月份，例 2018-09-30 23:59:59
        :type EndTime: str
        """
        self.PayerUin = None
        self.BeginTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.PayerUin = params.get("PayerUin")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")


class DescribeBillSummaryByProjectResponse(AbstractModel):
    """DescribeBillSummaryByProject返回參數結構體

    """

    def __init__(self):
        """
        :param Ready: 數據是否準備好，0未準備好，1準備好
        :type Ready: int
        :param SummaryOverview: 各項目花費分布詳情
注意：此欄位可能返回 null，表示取不到有效值。
        :type SummaryOverview: list of ProjectSummaryOverviewItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Ready = None
        self.SummaryOverview = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ready = params.get("Ready")
        if params.get("SummaryOverview") is not None:
            self.SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = ProjectSummaryOverviewItem()
                obj._deserialize(item)
                self.SummaryOverview.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBillSummaryByRegionRequest(AbstractModel):
    """DescribeBillSummaryByRegion請求參數結構體

    """

    def __init__(self):
        """
        :param PayerUin: 查詢帳單數據的用戶UIN
        :type PayerUin: str
        :param BeginTime: 目前只支援傳當月開始，且必須和EndTime爲相同月份，例 2018-09-01 00:00:00
        :type BeginTime: str
        :param EndTime: 目前只支援傳當月結束，且必須和BeginTime爲相同月份，例 2018-09-30 23:59:59
        :type EndTime: str
        """
        self.PayerUin = None
        self.BeginTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.PayerUin = params.get("PayerUin")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")


class DescribeBillSummaryByRegionResponse(AbstractModel):
    """DescribeBillSummaryByRegion返回參數結構體

    """

    def __init__(self):
        """
        :param Ready: 數據是否準備好，0未準備好，1準備好
        :type Ready: int
        :param SummaryOverview: 各地域花費分布詳情
注意：此欄位可能返回 null，表示取不到有效值。
        :type SummaryOverview: list of RegionSummaryOverviewItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Ready = None
        self.SummaryOverview = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ready = params.get("Ready")
        if params.get("SummaryOverview") is not None:
            self.SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = RegionSummaryOverviewItem()
                obj._deserialize(item)
                self.SummaryOverview.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBillSummaryByTagRequest(AbstractModel):
    """DescribeBillSummaryByTag請求參數結構體

    """

    def __init__(self):
        """
        :param PayerUin: 查詢帳單數據的用戶UIN
        :type PayerUin: str
        :param BeginTime: 目前只支援傳當月開始，且必須和EndTime爲相同月份，例 2018-09-01 00:00:00
        :type BeginTime: str
        :param EndTime: 目前只支援傳當月結束，且必須和BeginTime爲相同月份，例 2018-09-30 23:59:59
        :type EndTime: str
        :param TagKey: 分賬标簽鍵
        :type TagKey: str
        """
        self.PayerUin = None
        self.BeginTime = None
        self.EndTime = None
        self.TagKey = None


    def _deserialize(self, params):
        self.PayerUin = params.get("PayerUin")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.TagKey = params.get("TagKey")


class DescribeBillSummaryByTagResponse(AbstractModel):
    """DescribeBillSummaryByTag返回參數結構體

    """

    def __init__(self):
        """
        :param Ready: 數據是否準備好，0未準備好，1準備好
        :type Ready: int
        :param SummaryOverview: 各标簽值花費分布詳情
注意：此欄位可能返回 null，表示取不到有效值。
        :type SummaryOverview: list of TagSummaryOverviewItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Ready = None
        self.SummaryOverview = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ready = params.get("Ready")
        if params.get("SummaryOverview") is not None:
            self.SummaryOverview = []
            for item in params.get("SummaryOverview"):
                obj = TagSummaryOverviewItem()
                obj._deserialize(item)
                self.SummaryOverview.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCostDetailRequest(AbstractModel):
    """DescribeCostDetail請求參數結構體

    """

    def __init__(self):
        """
        :param Limit: 數量，最大值爲100
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        :param BeginTime: 週期開始時間，格式爲Y-m-d H:i:s，Month和BeginTime&EndTime必傳一個，如果有該欄位則Month欄位無效。BeginTime和EndTime必須一起傳。不能早于開通成本分析的月份，最多可拉取24個月内的數據。
        :type BeginTime: str
        :param EndTime: 週期結束時間，格式爲Y-m-d H:i:s，Month和BeginTime&EndTime必傳一個，如果有該欄位則Month欄位無效。BeginTime和EndTime必須一起傳。不能早于開通成本分析的月份，最多可拉取24個月内的數據。
        :type EndTime: str
        :param NeedRecordNum: 是否需要訪問清單的總記錄數，用于前端分頁
1-表示需要， 0-表示不需要
        :type NeedRecordNum: int
        :param Month: 月份，格式爲yyyy-mm，Month和BeginTime&EndTime必傳一個，如果有傳BeginTime&EndTime則Month欄位無效。不能早于開通成本分析的月份，最多可拉取24個月内的數據。
        :type Month: str
        :param ProductCode: 查詢指定産品訊息
        :type ProductCode: str
        :param PayMode: 付費模式 prePay/postPay
        :type PayMode: str
        :param ResourceId: 查詢指定資源訊息
        :type ResourceId: str
        """
        self.Limit = None
        self.Offset = None
        self.BeginTime = None
        self.EndTime = None
        self.NeedRecordNum = None
        self.Month = None
        self.ProductCode = None
        self.PayMode = None
        self.ResourceId = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.NeedRecordNum = params.get("NeedRecordNum")
        self.Month = params.get("Month")
        self.ProductCode = params.get("ProductCode")
        self.PayMode = params.get("PayMode")
        self.ResourceId = params.get("ResourceId")


class DescribeCostDetailResponse(AbstractModel):
    """DescribeCostDetail返回參數結構體

    """

    def __init__(self):
        """
        :param DetailSet: 消耗明細
注意：此欄位可能返回 null，表示取不到有效值。
        :type DetailSet: list of CostDetail
        :param Total: 記錄數
注意：此欄位可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DetailSet = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DetailSet") is not None:
            self.DetailSet = []
            for item in params.get("DetailSet"):
                obj = CostDetail()
                obj._deserialize(item)
                self.DetailSet.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeCostSummaryByProductRequest(AbstractModel):
    """DescribeCostSummaryByProduct請求參數結構體

    """

    def __init__(self):
        """
        :param PayerUin: 查詢帳單數據的用戶UIN
        :type PayerUin: str
        :param BeginTime: 目前只支援傳當月1号 00:00:00，且必須和EndTime爲相同月份，不支援跨月查詢，例 2018-09-01 00:00:00
        :type BeginTime: str
        :param EndTime: 目前只支援傳當月最後一天 23:59:59，且必須和BeginTime爲相同月份，不支援跨月查詢，例 2018-09-30 23:59:59
        :type EndTime: str
        :param Limit: 每次獲取數據量
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        :param NeedRecordNum: 是否需要返回記錄數量，0不需要，1需要，預設不需要
        :type NeedRecordNum: int
        """
        self.PayerUin = None
        self.BeginTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.NeedRecordNum = None


    def _deserialize(self, params):
        self.PayerUin = params.get("PayerUin")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.NeedRecordNum = params.get("NeedRecordNum")


class DescribeCostSummaryByProductResponse(AbstractModel):
    """DescribeCostSummaryByProduct返回參數結構體

    """

    def __init__(self):
        """
        :param Ready: 數據是否準備好，0未準備好，1準備好
        :type Ready: int
        :param Total: 消耗詳情
        :type Total: :class:`taifucloudcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        :param Data: 消耗按産品匯總詳情
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: list of ConsumptionBusinessSummaryDataItem
        :param RecordNum: 記錄數量，NeedRecordNum爲0是返回null
注意：此欄位可能返回 null，表示取不到有效值。
        :type RecordNum: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Ready = None
        self.Total = None
        self.Data = None
        self.RecordNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ready = params.get("Ready")
        if params.get("Total") is not None:
            self.Total = ConsumptionSummaryTotal()
            self.Total._deserialize(params.get("Total"))
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ConsumptionBusinessSummaryDataItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RecordNum = params.get("RecordNum")
        self.RequestId = params.get("RequestId")


class DescribeCostSummaryByProjectRequest(AbstractModel):
    """DescribeCostSummaryByProject請求參數結構體

    """

    def __init__(self):
        """
        :param PayerUin: 查詢帳單數據的用戶UIN
        :type PayerUin: str
        :param BeginTime: 目前只支援傳當月1号 00:00:00，且必須和EndTime爲相同月份，不支援跨月查詢，例 2018-09-01 00:00:00
        :type BeginTime: str
        :param EndTime: 目前只支援傳當月最後一天 23:59:59，且必須和BeginTime爲相同月份，不支援跨月查詢，例 2018-09-30 23:59:59
        :type EndTime: str
        :param Limit: 每次獲取數據量
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        :param NeedRecordNum: 是否需要返回記錄數量，0不需要，1需要，預設不需要
        :type NeedRecordNum: int
        """
        self.PayerUin = None
        self.BeginTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.NeedRecordNum = None


    def _deserialize(self, params):
        self.PayerUin = params.get("PayerUin")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.NeedRecordNum = params.get("NeedRecordNum")


class DescribeCostSummaryByProjectResponse(AbstractModel):
    """DescribeCostSummaryByProject返回參數結構體

    """

    def __init__(self):
        """
        :param Ready: 數據是否準備好，0未準備好，1準備好
        :type Ready: int
        :param Total: 消耗詳情
        :type Total: :class:`taifucloudcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        :param Data: 消耗按業務匯總詳情
        :type Data: list of ConsumptionProjectSummaryDataItem
        :param RecordNum: 記錄數量，NeedRecordNum爲0是返回null
        :type RecordNum: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Ready = None
        self.Total = None
        self.Data = None
        self.RecordNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ready = params.get("Ready")
        if params.get("Total") is not None:
            self.Total = ConsumptionSummaryTotal()
            self.Total._deserialize(params.get("Total"))
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ConsumptionProjectSummaryDataItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RecordNum = params.get("RecordNum")
        self.RequestId = params.get("RequestId")


class DescribeCostSummaryByRegionRequest(AbstractModel):
    """DescribeCostSummaryByRegion請求參數結構體

    """

    def __init__(self):
        """
        :param PayerUin: 查詢帳單數據的用戶UIN
        :type PayerUin: str
        :param BeginTime: 目前只支援傳當月1号 00:00:00，且必須和EndTime爲相同月份，不支援跨月查詢，例 2018-09-01 00:00:00
        :type BeginTime: str
        :param EndTime: 目前只支援傳當月最後一天 23:59:59，且必須和BeginTime爲相同月份，不支援跨月查詢，例 2018-09-30 23:59:59
        :type EndTime: str
        :param Limit: 每次獲取數據量
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        :param NeedRecordNum: 是否需要返回記錄數量，0不需要，1需要，預設不需要
        :type NeedRecordNum: int
        """
        self.PayerUin = None
        self.BeginTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.NeedRecordNum = None


    def _deserialize(self, params):
        self.PayerUin = params.get("PayerUin")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.NeedRecordNum = params.get("NeedRecordNum")


class DescribeCostSummaryByRegionResponse(AbstractModel):
    """DescribeCostSummaryByRegion返回參數結構體

    """

    def __init__(self):
        """
        :param Ready: 數據是否準備好，0未準備好，1準備好
        :type Ready: int
        :param Total: 消耗詳情
        :type Total: :class:`taifucloudcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        :param Data: 消耗按地域匯總詳情
        :type Data: list of ConsumptionRegionSummaryDataItem
        :param RecordNum: 記錄數量，NeedRecordNum爲0是返回null
注意：此欄位可能返回 null，表示取不到有效值。
        :type RecordNum: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Ready = None
        self.Total = None
        self.Data = None
        self.RecordNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ready = params.get("Ready")
        if params.get("Total") is not None:
            self.Total = ConsumptionSummaryTotal()
            self.Total._deserialize(params.get("Total"))
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ConsumptionRegionSummaryDataItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RecordNum = params.get("RecordNum")
        self.RequestId = params.get("RequestId")


class DescribeCostSummaryByResourceRequest(AbstractModel):
    """DescribeCostSummaryByResource請求參數結構體

    """

    def __init__(self):
        """
        :param PayerUin: 查詢帳單數據的用戶UIN
        :type PayerUin: str
        :param BeginTime: 目前只支援傳當月1号 00:00:00，且必須和EndTime爲相同月份，不支援跨月查詢，例 2018-09-01 00:00:00
        :type BeginTime: str
        :param EndTime: 目前只支援傳當月最後一天 23:59:59，且必須和BeginTime爲相同月份，不支援跨月查詢，例 2018-09-30 23:59:59
        :type EndTime: str
        :param Limit: 每次獲取數據量
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        :param NeedRecordNum: 是否需要返回記錄數量，0不需要，1需要，預設不需要
        :type NeedRecordNum: int
        :param NeedConditionValue: 是否需要返回過濾條件，0不需要，1需要，預設不需要
        :type NeedConditionValue: int
        :param Conditions: 過濾條件，只支援ResourceKeyword(資源關鍵字，支援資源id及資源名稱模糊查詢)，ProjectIds（項目id），RegionIds(地域id)，PayModes(付費模式，可選prePay和postPay)，HideFreeCost（是否隐藏0元流水，可選0和1），OrderByCost（按費用排序規則，可選desc和asc）
        :type Conditions: :class:`taifucloudcloud.billing.v20180709.models.Conditions`
        """
        self.PayerUin = None
        self.BeginTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.NeedRecordNum = None
        self.NeedConditionValue = None
        self.Conditions = None


    def _deserialize(self, params):
        self.PayerUin = params.get("PayerUin")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.NeedRecordNum = params.get("NeedRecordNum")
        self.NeedConditionValue = params.get("NeedConditionValue")
        if params.get("Conditions") is not None:
            self.Conditions = Conditions()
            self.Conditions._deserialize(params.get("Conditions"))


class DescribeCostSummaryByResourceResponse(AbstractModel):
    """DescribeCostSummaryByResource返回參數結構體

    """

    def __init__(self):
        """
        :param Ready: 數據是否準備好，0未準備好，1準備好
        :type Ready: int
        :param Total: 消耗詳情
注意：此欄位可能返回 null，表示取不到有效值。
        :type Total: :class:`taifucloudcloud.billing.v20180709.models.ConsumptionSummaryTotal`
        :param ConditionValue: 過濾條件
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConditionValue: :class:`taifucloudcloud.billing.v20180709.models.ConsumptionResourceSummaryConditionValue`
        :param RecordNum: 記錄數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type RecordNum: int
        :param Data: 資源消耗詳情
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: list of ConsumptionResourceSummaryDataItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Ready = None
        self.Total = None
        self.ConditionValue = None
        self.RecordNum = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ready = params.get("Ready")
        if params.get("Total") is not None:
            self.Total = ConsumptionSummaryTotal()
            self.Total._deserialize(params.get("Total"))
        if params.get("ConditionValue") is not None:
            self.ConditionValue = ConsumptionResourceSummaryConditionValue()
            self.ConditionValue._deserialize(params.get("ConditionValue"))
        self.RecordNum = params.get("RecordNum")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ConsumptionResourceSummaryDataItem()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDealsByCondRequest(AbstractModel):
    """DescribeDealsByCond請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 開始時間
        :type StartTime: str
        :param EndTime: 結束時間
        :type EndTime: str
        :param Limit: 一頁多少條數據，預設是20條，最大不超過1000
        :type Limit: int
        :param Offset: 第多少頁，從0開始，預設是0
        :type Offset: int
        :param Status: 訂單狀态,預設爲4（成功的訂單）
訂單的狀态
1：未支付
2：已支付3：發貨中
4：已發貨
5：發貨失敗
6：已退款
7：已關單
8：訂單過期
9：訂單已失效
10：産品已失效
11：代付拒絕
12：支付中
        :type Status: int
        :param OrderId: 訂單号
        :type OrderId: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.Status = None
        self.OrderId = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Status = params.get("Status")
        self.OrderId = params.get("OrderId")


class DescribeDealsByCondResponse(AbstractModel):
    """DescribeDealsByCond返回參數結構體

    """

    def __init__(self):
        """
        :param Deals: 訂單清單
        :type Deals: list of Deal
        :param TotalCount: 訂單總數
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Deals = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Deals") is not None:
            self.Deals = []
            for item in params.get("Deals"):
                obj = Deal()
                obj._deserialize(item)
                self.Deals.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDosageDetailByDateRequest(AbstractModel):
    """DescribeDosageDetailByDate請求參數結構體

    """

    def __init__(self):
        """
        :param StartDate: 查詢帳單開始日期，如 2019-01-01
        :type StartDate: str
        :param EndDate: 查詢帳單結束日期，如 2019-01-01， 時間跨度不超過7天
        :type EndDate: str
        :param ProductCode: 互動直播：
10194   互動直播-核心機房           :
10195   互動直播-邊緣機房

cdn業務：
10180：CDN靜态加速流量(國内)
10181：CDN靜态加速頻寬(國内)
10182：CDN靜态加速普通流量
10183：CDN靜态加速普通頻寬
10231：CDN靜态加速流量(海外)
10232：CDN靜态加速頻寬(海外)

100967：彈性公網IP-按流量計費
101065：公網負載均衡-按流量計費

視訊直播
10226 視訊直播流量(國内)
10227 視訊直播頻寬(國内)
100763 視訊直播流量(海外)
100762 視訊直播寬帶(海外)
        :type ProductCode: str
        :param Domain: 查詢域名 例如 www.qq.com
非CDN業務查詢時值爲空
        :type Domain: str
        :param InstanceID: 1、如果爲空，則返回EIP或CLB所有實例的明細；
2、如果傳入實例名，則返回該實例明細
        :type InstanceID: str
        """
        self.StartDate = None
        self.EndDate = None
        self.ProductCode = None
        self.Domain = None
        self.InstanceID = None


    def _deserialize(self, params):
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.ProductCode = params.get("ProductCode")
        self.Domain = params.get("Domain")
        self.InstanceID = params.get("InstanceID")


class DescribeDosageDetailByDateResponse(AbstractModel):
    """DescribeDosageDetailByDate返回參數結構體

    """

    def __init__(self):
        """
        :param Unit: 計量單位
注意：此欄位可能返回 null，表示取不到有效值。
        :type Unit: str
        :param DetailSets: 用量數組
注意：此欄位可能返回 null，表示取不到有效值。
        :type DetailSets: list of DetailSet
        :param RetCode: 錯誤碼
注意：此欄位可能返回 null，表示取不到有效值。
        :type RetCode: int
        :param RetMsg: 錯誤訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type RetMsg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Unit = None
        self.DetailSets = None
        self.RetCode = None
        self.RetMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Unit = params.get("Unit")
        if params.get("DetailSets") is not None:
            self.DetailSets = []
            for item in params.get("DetailSets"):
                obj = DetailSet()
                obj._deserialize(item)
                self.DetailSets.append(obj)
        self.RetCode = params.get("RetCode")
        self.RetMsg = params.get("RetMsg")
        self.RequestId = params.get("RequestId")


class DetailPoint(AbstractModel):
    """由時間和值組成的數據結構

    """

    def __init__(self):
        """
        :param Time: 時間
        :type Time: str
        :param Value: 值
        :type Value: str
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")


class DetailSet(AbstractModel):
    """由域名和使用明細組成的數據結構

    """

    def __init__(self):
        """
        :param Domain: 域名
        :type Domain: str
        :param DetailPoints: 使用數據明細
        :type DetailPoints: list of DetailPoint
        :param InstanceID: 實例ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceID: str
        """
        self.Domain = None
        self.DetailPoints = None
        self.InstanceID = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        if params.get("DetailPoints") is not None:
            self.DetailPoints = []
            for item in params.get("DetailPoints"):
                obj = DetailPoint()
                obj._deserialize(item)
                self.DetailPoints.append(obj)
        self.InstanceID = params.get("InstanceID")


class PayDealsRequest(AbstractModel):
    """PayDeals請求參數結構體

    """

    def __init__(self):
        """
        :param OrderIds: 需要支付的一個或者多個訂單号
        :type OrderIds: list of str
        :param AutoVoucher: 是否自動使用 ,1:是,0否,預設0
        :type AutoVoucher: int
        :param VoucherIds:  ID清單,目前僅支援指定一張 
        :type VoucherIds: list of str
        """
        self.OrderIds = None
        self.AutoVoucher = None
        self.VoucherIds = None


    def _deserialize(self, params):
        self.OrderIds = params.get("OrderIds")
        self.AutoVoucher = params.get("AutoVoucher")
        self.VoucherIds = params.get("VoucherIds")


class PayDealsResponse(AbstractModel):
    """PayDeals返回參數結構體

    """

    def __init__(self):
        """
        :param OrderIds: 此次操作支付成功的訂單号數組
        :type OrderIds: list of str
        :param ResourceIds: 此次操作支付成功的資源Id數組
        :type ResourceIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.OrderIds = None
        self.ResourceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OrderIds = params.get("OrderIds")
        self.ResourceIds = params.get("ResourceIds")
        self.RequestId = params.get("RequestId")


class PayModeSummaryOverviewItem(AbstractModel):
    """按付費模式匯總消費詳情

    """

    def __init__(self):
        """
        :param PayMode: 付費模式
        :type PayMode: str
        :param PayModeName: 付費模式名稱
        :type PayModeName: str
        :param RealTotalCost: 實際花費
        :type RealTotalCost: str
        :param RealTotalCostRatio: 費用所占百分比，兩位小數
        :type RealTotalCostRatio: str
        :param Detail: 按交易類型：包年包月新購/續約/升降配/退款、按量計費扣費、調賬補償/扣費等類型匯總消費詳情
        :type Detail: list of ActionSummaryOverviewItem
        :param CashPayAmount: 現金金額
        :type CashPayAmount: str
        :param IncentivePayAmount: 贈送金金額
        :type IncentivePayAmount: str
        :param VoucherPayAmount:  金額
        :type VoucherPayAmount: str
        """
        self.PayMode = None
        self.PayModeName = None
        self.RealTotalCost = None
        self.RealTotalCostRatio = None
        self.Detail = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None


    def _deserialize(self, params):
        self.PayMode = params.get("PayMode")
        self.PayModeName = params.get("PayModeName")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        if params.get("Detail") is not None:
            self.Detail = []
            for item in params.get("Detail"):
                obj = ActionSummaryOverviewItem()
                obj._deserialize(item)
                self.Detail.append(obj)
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")


class ProductInfo(AbstractModel):
    """商品詳細訊息

    """

    def __init__(self):
        """
        :param Name: 商品詳情名稱标識
        :type Name: str
        :param Value: 商品詳情
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class ProjectSummaryOverviewItem(AbstractModel):
    """按項目匯總消費詳情

    """

    def __init__(self):
        """
        :param ProjectId: 項目ID
        :type ProjectId: str
        :param ProjectName: 項目名稱
        :type ProjectName: str
        :param RealTotalCost: 實際花費
        :type RealTotalCost: str
        :param RealTotalCostRatio: 費用所占百分比，兩位小數
        :type RealTotalCostRatio: str
        :param CashPayAmount: 現金金額
        :type CashPayAmount: str
        :param IncentivePayAmount: 贈送金金額
        :type IncentivePayAmount: str
        :param VoucherPayAmount:  金額
        :type VoucherPayAmount: str
        :param BillMonth: 帳單月份，格式2019-08
        :type BillMonth: str
        """
        self.ProjectId = None
        self.ProjectName = None
        self.RealTotalCost = None
        self.RealTotalCostRatio = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.BillMonth = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.BillMonth = params.get("BillMonth")


class RegionSummaryOverviewItem(AbstractModel):
    """按地域匯總消費詳情

    """

    def __init__(self):
        """
        :param RegionId: 地域ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type RegionId: str
        :param RegionName: 地域名稱
        :type RegionName: str
        :param RealTotalCost: 實際花費
        :type RealTotalCost: str
        :param RealTotalCostRatio: 費用所占百分比，兩位小數
        :type RealTotalCostRatio: str
        :param CashPayAmount: 現金金額
        :type CashPayAmount: str
        :param IncentivePayAmount: 贈送金金額
        :type IncentivePayAmount: str
        :param VoucherPayAmount:  金額
        :type VoucherPayAmount: str
        :param BillMonth: 帳單月份，格式2019-08
        :type BillMonth: str
        """
        self.RegionId = None
        self.RegionName = None
        self.RealTotalCost = None
        self.RealTotalCostRatio = None
        self.CashPayAmount = None
        self.IncentivePayAmount = None
        self.VoucherPayAmount = None
        self.BillMonth = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")
        self.CashPayAmount = params.get("CashPayAmount")
        self.IncentivePayAmount = params.get("IncentivePayAmount")
        self.VoucherPayAmount = params.get("VoucherPayAmount")
        self.BillMonth = params.get("BillMonth")


class TagSummaryOverviewItem(AbstractModel):
    """按标簽匯總消費詳情

    """

    def __init__(self):
        """
        :param TagValue: 标簽值
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagValue: str
        :param RealTotalCost: 實際花費
注意：此欄位可能返回 null，表示取不到有效值。
        :type RealTotalCost: str
        :param RealTotalCostRatio: 費用所占百分比，兩位小數
注意：此欄位可能返回 null，表示取不到有效值。
        :type RealTotalCostRatio: str
        """
        self.TagValue = None
        self.RealTotalCost = None
        self.RealTotalCostRatio = None


    def _deserialize(self, params):
        self.TagValue = params.get("TagValue")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RealTotalCostRatio = params.get("RealTotalCostRatio")