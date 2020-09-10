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


class BillDetail(AbstractModel):
    """帳單明細數據對象

    """

    def __init__(self):
        """
        :param BusinessCodeName: 産品名稱
        :type BusinessCodeName: str
        :param ProductCodeName: 子産品名稱
        :type ProductCodeName: str
        :param PayModeName: 計費模式
        :type PayModeName: str
        :param ProjectName: 項目
        :type ProjectName: str
        :param RegionName: 區域
        :type RegionName: str
        :param ZoneName: 可用區
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


class BillDetailComponent(AbstractModel):
    """帳單明細元件對象

    """

    def __init__(self):
        """
        :param ComponentCodeName: 元件名稱
        :type ComponentCodeName: str
        :param ItemCodeName: 元件類型名稱
        :type ItemCodeName: str
        :param SinglePrice: 元件刊例價
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


class BillResourceSummary(AbstractModel):
    """帳單資源匯總數據對象

    """

    def __init__(self):
        """
        :param BusinessCodeName: 産品
        :type BusinessCodeName: str
        :param ProductCodeName: 子産品
        :type ProductCodeName: str
        :param PayModeName: 計費模式
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
        :param ActionTypeName: 交易類型
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
        :param PeriodType: 週期類型，byPayTime按扣費週期/byUsedTime按計費週期。需要與費用中心該月份帳單的週期保持一緻。
        :type PeriodType: str
        :param Month: 月份，格式爲yyyy-mm，Month和BeginTime&EndTime必傳一個，如果有傳BeginTime&EndTime則Month欄位無效。不能早于開通帳單2.0的月份，最多可拉取24個月内的數據。
        :type Month: str
        :param BeginTime: 週期開始時間，格式爲Y-m-d H:i:s，Month和BeginTime&EndTime必傳一個，如果有該欄位則Month欄位無效。BeginTime和EndTime必須一起傳。不能早于開通帳單2.0的月份，最多可拉取24個月内的數據。
        :type BeginTime: str
        :param EndTime: 週期結束時間，格式爲Y-m-d H:i:s，Month和BeginTime&EndTime必傳一個，如果有該欄位則Month欄位無效。BeginTime和EndTime必須一起傳。不能早于開通帳單2.0的月份，最多可拉取24個月内的數據。
        :type EndTime: str
        """
        self.Offset = None
        self.Limit = None
        self.PeriodType = None
        self.Month = None
        self.BeginTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PeriodType = params.get("PeriodType")
        self.Month = params.get("Month")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")


class DescribeBillDetailResponse(AbstractModel):
    """DescribeBillDetail返回參數結構體

    """

    def __init__(self):
        """
        :param DetailSet: 詳情清單
        :type DetailSet: list of BillDetail
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DetailSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DetailSet") is not None:
            self.DetailSet = []
            for item in params.get("DetailSet"):
                obj = BillDetail()
                obj._deserialize(item)
                self.DetailSet.append(obj)
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
        :param PeriodType: 週期類型，byUsedTime按計費週期/byPayTime按扣費週期。需要與費用中心該月份帳單的週期保持一緻。
        :type PeriodType: str
        :param Month: 月份，格式爲yyyy-mm。不能早于開通帳單2.0的月份，最多可拉取24個月内的數據。
        :type Month: str
        :param NeedRecordNum: 是否需要訪問清單的總記錄數，用于前端分頁
1-表示需要， 0-表示不需要
        :type NeedRecordNum: int
        """
        self.Offset = None
        self.Limit = None
        self.PeriodType = None
        self.Month = None
        self.NeedRecordNum = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PeriodType = params.get("PeriodType")
        self.Month = params.get("Month")
        self.NeedRecordNum = params.get("NeedRecordNum")


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