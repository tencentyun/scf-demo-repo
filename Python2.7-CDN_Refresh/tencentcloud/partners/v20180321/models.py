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


class AgentAuditedClient(AbstractModel):
    """已審核代客訊息

    """

    def __init__(self):
        """
        :param Uin:  賬号ID
        :type Uin: str
        :param ClientUin: 代客賬号ID
        :type ClientUin: str
        :param AgentTime: 代客審核通過時間戳
        :type AgentTime: str
        :param ClientFlag: 代客類型，可能值爲a/b/c
        :type ClientFlag: str
        :param ClientRemark: 代客備注
        :type ClientRemark: str
        :param ClientName: 代客名稱（首選實名認證名稱）
        :type ClientName: str
        :param AuthType: 認證類型, 0：個人，1：企業；其他：未認證
        :type AuthType: str
        :param AppId: 代客APPID
        :type AppId: str
        :param LastMonthAmt: 上月消費金額
        :type LastMonthAmt: int
        :param ThisMonthAmt: 本月消費金額
        :type ThisMonthAmt: int
        :param HasOverdueBill: 是否欠費,0：不欠費；1：欠費
        :type HasOverdueBill: int
        :param ClientType: 客戶類型：可以爲new(新拓)/assign(指定)/old(存量)/空
        :type ClientType: str
        :param ProjectType: 項目類型：可以爲self(自拓項目)/platform(合作項目)/repeat(複算項目  )/空
        :type ProjectType: str
        :param SalesUin: 業務員ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type SalesUin: str
        :param SalesName: 業務員姓名
注意：此欄位可能返回 null，表示取不到有效值。
        :type SalesName: str
        :param Mail: 代客電子信箱
注意：此欄位可能返回 null，表示取不到有效值。
        :type Mail: str
        """
        self.Uin = None
        self.ClientUin = None
        self.AgentTime = None
        self.ClientFlag = None
        self.ClientRemark = None
        self.ClientName = None
        self.AuthType = None
        self.AppId = None
        self.LastMonthAmt = None
        self.ThisMonthAmt = None
        self.HasOverdueBill = None
        self.ClientType = None
        self.ProjectType = None
        self.SalesUin = None
        self.SalesName = None
        self.Mail = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.ClientUin = params.get("ClientUin")
        self.AgentTime = params.get("AgentTime")
        self.ClientFlag = params.get("ClientFlag")
        self.ClientRemark = params.get("ClientRemark")
        self.ClientName = params.get("ClientName")
        self.AuthType = params.get("AuthType")
        self.AppId = params.get("AppId")
        self.LastMonthAmt = params.get("LastMonthAmt")
        self.ThisMonthAmt = params.get("ThisMonthAmt")
        self.HasOverdueBill = params.get("HasOverdueBill")
        self.ClientType = params.get("ClientType")
        self.ProjectType = params.get("ProjectType")
        self.SalesUin = params.get("SalesUin")
        self.SalesName = params.get("SalesName")
        self.Mail = params.get("Mail")


class AgentBillElem(AbstractModel):
    """業務訊息定義

    """

    def __init__(self):
        """
        :param Uin:  賬号ID
        :type Uin: str
        :param OrderId: 訂單号，僅對預付費帳單有意義
        :type OrderId: str
        :param ClientUin: 代客賬号ID
        :type ClientUin: str
        :param ClientRemark: 代客備注名稱
        :type ClientRemark: str
        :param PayTime: 支付時間
        :type PayTime: str
        :param GoodsType: 雲産品名稱
        :type GoodsType: str
        :param PayMode: 預付費/後付費
        :type PayMode: str
        :param SettleMonth: 支付月份
        :type SettleMonth: str
        :param Amt: 支付金額，單位分
        :type Amt: int
        :param PayerMode: agentpay：代付；selfpay：自付
        :type PayerMode: str
        :param ClientType: 客戶類型：可以爲new(新拓)/assign(指定)/old(存量)/空
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClientType: str
        :param ProjectType: 項目類型：可以爲self(自拓項目)/platform(合作項目)/repeat(複算項目  )/空
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProjectType: str
        :param ActivityId: 活動ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ActivityId: str
        """
        self.Uin = None
        self.OrderId = None
        self.ClientUin = None
        self.ClientRemark = None
        self.PayTime = None
        self.GoodsType = None
        self.PayMode = None
        self.SettleMonth = None
        self.Amt = None
        self.PayerMode = None
        self.ClientType = None
        self.ProjectType = None
        self.ActivityId = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.OrderId = params.get("OrderId")
        self.ClientUin = params.get("ClientUin")
        self.ClientRemark = params.get("ClientRemark")
        self.PayTime = params.get("PayTime")
        self.GoodsType = params.get("GoodsType")
        self.PayMode = params.get("PayMode")
        self.SettleMonth = params.get("SettleMonth")
        self.Amt = params.get("Amt")
        self.PayerMode = params.get("PayerMode")
        self.ClientType = params.get("ClientType")
        self.ProjectType = params.get("ProjectType")
        self.ActivityId = params.get("ActivityId")


class AgentClientElem(AbstractModel):
    """描述待審核代客訊息

    """

    def __init__(self):
        """
        :param Uin:  賬号ID
        :type Uin: str
        :param ClientUin: 代客賬号ID
        :type ClientUin: str
        :param ApplyTime: 代客申請時間戳
        :type ApplyTime: int
        :param ClientFlag: 代客類型，可能值爲a/b/c
        :type ClientFlag: str
        :param Mail: 代客電子信箱，打碼顯示
        :type Mail: str
        :param Phone: 代客手機，打碼顯示
        :type Phone: str
        :param HasOverdueBill: 0表示不欠費，1表示欠費
        :type HasOverdueBill: int
        :param Status: 1:待 審核;2:待Top Cloud 審核
        :type Status: int
        :param SalesUin: 業務員ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type SalesUin: str
        :param SalesName: 業務員姓名
注意：此欄位可能返回 null，表示取不到有效值。
        :type SalesName: str
        """
        self.Uin = None
        self.ClientUin = None
        self.ApplyTime = None
        self.ClientFlag = None
        self.Mail = None
        self.Phone = None
        self.HasOverdueBill = None
        self.Status = None
        self.SalesUin = None
        self.SalesName = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.ClientUin = params.get("ClientUin")
        self.ApplyTime = params.get("ApplyTime")
        self.ClientFlag = params.get("ClientFlag")
        self.Mail = params.get("Mail")
        self.Phone = params.get("Phone")
        self.HasOverdueBill = params.get("HasOverdueBill")
        self.Status = params.get("Status")
        self.SalesUin = params.get("SalesUin")
        self.SalesName = params.get("SalesName")


class AgentDealElem(AbstractModel):
    """描述 代付的訂單訊息

    """

    def __init__(self):
        """
        :param DealId: 訂單自增 ID
        :type DealId: str
        :param DealName: 訂單号
        :type DealName: str
        :param GoodsCategoryId: 商品類型 ID
        :type GoodsCategoryId: str
        :param OwnerUin: 訂單所有者
        :type OwnerUin: str
        :param AppId: 訂單所有者對應 appId
注意：此欄位可能返回 null，表示取不到有效值。
        :type AppId: str
        :param GoodsNum: 商品數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type GoodsNum: str
        :param GoodsPrice: 價格詳情
注意：此欄位可能返回 null，表示取不到有效值。
        :type GoodsPrice: :class:`taifucloudcloud.partners.v20180321.models.DealGoodsPriceElem`
        :param Creater: 下單人
注意：此欄位可能返回 null，表示取不到有效值。
        :type Creater: str
        :param CreatTime: 下單時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreatTime: str
        :param PayEndTime: 支付結束時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type PayEndTime: str
        :param BillId: 扣費流水号
注意：此欄位可能返回 null，表示取不到有效值。
        :type BillId: str
        :param Payer: 支付人
注意：此欄位可能返回 null，表示取不到有效值。
        :type Payer: str
        :param DealStatus: 訂單狀态，中文描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type DealStatus: str
        :param Status: 訂單的狀态(1：未支付;2：已支付;3：發貨中;4：已發貨;5：發貨失敗;6：已退款;7：已關單;8：訂單過期;9：訂單已失效;10：産品已失效;11：代付拒絕;12：支付中)
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: str
        :param GoodsName: 産品名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type GoodsName: str
        :param ClientRemark: 客戶備注
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClientRemark: str
        :param ActionType: 訂單操作類型，purchase（新購），renew（續約），modify（配置變更）
注意：此欄位可能返回 null，表示取不到有效值。
        :type ActionType: str
        :param VoucherDecline:  抵扣金額，單位分
注意：此欄位可能返回 null，表示取不到有效值。
        :type VoucherDecline: str
        :param BigDealId: 大訂單号
注意：此欄位可能返回 null，表示取不到有效值。
        :type BigDealId: str
        :param ClientType: 客戶類型（new：新拓；old：存量；assign：指派）
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClientType: str
        :param ProjectType: 項目類型（self：自拓；repeat：直銷；platform：官網合作）
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProjectType: str
        :param SalesUin: 業務員賬号ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type SalesUin: str
        :param PayerMode: 支付方式，0：自付；1：代付
注意：此欄位可能返回 null，表示取不到有效值。
        :type PayerMode: str
        :param ActivityId: 活動ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ActivityId: str
        """
        self.DealId = None
        self.DealName = None
        self.GoodsCategoryId = None
        self.OwnerUin = None
        self.AppId = None
        self.GoodsNum = None
        self.GoodsPrice = None
        self.Creater = None
        self.CreatTime = None
        self.PayEndTime = None
        self.BillId = None
        self.Payer = None
        self.DealStatus = None
        self.Status = None
        self.GoodsName = None
        self.ClientRemark = None
        self.ActionType = None
        self.VoucherDecline = None
        self.BigDealId = None
        self.ClientType = None
        self.ProjectType = None
        self.SalesUin = None
        self.PayerMode = None
        self.ActivityId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.DealName = params.get("DealName")
        self.GoodsCategoryId = params.get("GoodsCategoryId")
        self.OwnerUin = params.get("OwnerUin")
        self.AppId = params.get("AppId")
        self.GoodsNum = params.get("GoodsNum")
        if params.get("GoodsPrice") is not None:
            self.GoodsPrice = DealGoodsPriceElem()
            self.GoodsPrice._deserialize(params.get("GoodsPrice"))
        self.Creater = params.get("Creater")
        self.CreatTime = params.get("CreatTime")
        self.PayEndTime = params.get("PayEndTime")
        self.BillId = params.get("BillId")
        self.Payer = params.get("Payer")
        self.DealStatus = params.get("DealStatus")
        self.Status = params.get("Status")
        self.GoodsName = params.get("GoodsName")
        self.ClientRemark = params.get("ClientRemark")
        self.ActionType = params.get("ActionType")
        self.VoucherDecline = params.get("VoucherDecline")
        self.BigDealId = params.get("BigDealId")
        self.ClientType = params.get("ClientType")
        self.ProjectType = params.get("ProjectType")
        self.SalesUin = params.get("SalesUin")
        self.PayerMode = params.get("PayerMode")
        self.ActivityId = params.get("ActivityId")


class AgentPayDealsRequest(AbstractModel):
    """AgentPayDeals請求參數結構體

    """

    def __init__(self):
        """
        :param OwnerUin: 訂單所有者uin
        :type OwnerUin: str
        :param AgentPay: 代付标志，1：代付；0：自付
        :type AgentPay: int
        :param DealNames: 訂單号數組
        :type DealNames: list of str
        """
        self.OwnerUin = None
        self.AgentPay = None
        self.DealNames = None


    def _deserialize(self, params):
        self.OwnerUin = params.get("OwnerUin")
        self.AgentPay = params.get("AgentPay")
        self.DealNames = params.get("DealNames")


class AgentPayDealsResponse(AbstractModel):
    """AgentPayDeals返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AgentSalesmanElem(AbstractModel):
    """ 業務員訊息

    """

    def __init__(self):
        """
        :param Uin:  賬号ID
        :type Uin: str
        :param SalesUin: 業務員ID
        :type SalesUin: str
        :param SalesName: 業務員姓名
        :type SalesName: str
        :param CreateTime: 業務員創建時間
        :type CreateTime: str
        """
        self.Uin = None
        self.SalesUin = None
        self.SalesName = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.SalesUin = params.get("SalesUin")
        self.SalesName = params.get("SalesName")
        self.CreateTime = params.get("CreateTime")


class AgentTransferMoneyRequest(AbstractModel):
    """AgentTransferMoney請求參數結構體

    """

    def __init__(self):
        """
        :param ClientUin: 客戶賬号ID
        :type ClientUin: str
        :param Amount: 轉賬金額，單位分
        :type Amount: int
        """
        self.ClientUin = None
        self.Amount = None


    def _deserialize(self, params):
        self.ClientUin = params.get("ClientUin")
        self.Amount = params.get("Amount")


class AgentTransferMoneyResponse(AbstractModel):
    """AgentTransferMoney返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AuditApplyClientRequest(AbstractModel):
    """AuditApplyClient請求參數結構體

    """

    def __init__(self):
        """
        :param ClientUin: 待審核客戶賬号ID
        :type ClientUin: str
        :param AuditResult: 審核結果，可能的取值：accept/reject
        :type AuditResult: str
        :param Note: 申請理由，B類客戶審核通過時必須填寫申請理由
        :type Note: str
        """
        self.ClientUin = None
        self.AuditResult = None
        self.Note = None


    def _deserialize(self, params):
        self.ClientUin = params.get("ClientUin")
        self.AuditResult = params.get("AuditResult")
        self.Note = params.get("Note")


class AuditApplyClientResponse(AbstractModel):
    """AuditApplyClient返回參數結構體

    """

    def __init__(self):
        """
        :param Uin:  賬号ID
        :type Uin: str
        :param ClientUin: 客戶賬号ID
        :type ClientUin: str
        :param AuditResult: 審核結果，包括accept/reject/qcloudaudit（Top Cloud 審核）
        :type AuditResult: str
        :param AgentTime: 關聯時間對應的時間戳
        :type AgentTime: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Uin = None
        self.ClientUin = None
        self.AuditResult = None
        self.AgentTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.ClientUin = params.get("ClientUin")
        self.AuditResult = params.get("AuditResult")
        self.AgentTime = params.get("AgentTime")
        self.RequestId = params.get("RequestId")


class CreatePayRelationForClientRequest(AbstractModel):
    """CreatePayRelationForClient請求參數結構體

    """

    def __init__(self):
        """
        :param ClientUin: 客戶賬号ID
        :type ClientUin: str
        """
        self.ClientUin = None


    def _deserialize(self, params):
        self.ClientUin = params.get("ClientUin")


class CreatePayRelationForClientResponse(AbstractModel):
    """CreatePayRelationForClient返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DealGoodsPriceElem(AbstractModel):
    """訂單價格詳情

    """

    def __init__(self):
        """
        :param RealTotalCost: 實付金額
        :type RealTotalCost: int
        """
        self.RealTotalCost = None


    def _deserialize(self, params):
        self.RealTotalCost = params.get("RealTotalCost")


class DescribeAgentAuditedClientsRequest(AbstractModel):
    """DescribeAgentAuditedClients請求參數結構體

    """

    def __init__(self):
        """
        :param ClientUin: 客戶賬号ID
        :type ClientUin: str
        :param ClientName: 客戶名稱。由于涉及隐私，名稱打碼顯示，故名稱僅支援打碼後的模糊搜索
        :type ClientName: str
        :param ClientFlag: 客戶類型，a/b，類型定義參考 相關政策文件
        :type ClientFlag: str
        :param OrderDirection: ASC/DESC， 不區分大小寫，按審核通過時間排序
        :type OrderDirection: str
        :param ClientUins: 客戶賬号ID清單
        :type ClientUins: list of str
        :param HasOverdueBill: 是否欠費。0：不欠費；1：欠費
        :type HasOverdueBill: int
        :param ClientRemark: 客戶備注
        :type ClientRemark: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制數目
        :type Limit: int
        :param ClientType: 客戶類型：可以爲new(新拓)/assign(指定)/old(存量)/空
        :type ClientType: str
        :param ProjectType: 項目類型：可以爲self(自拓項目)/platform(合作項目)/repeat(複算項目  )/空
        :type ProjectType: str
        :param SalesUin: 業務員ID
        :type SalesUin: str
        :param SalesName: 業務員姓名（模糊查詢）
        :type SalesName: str
        """
        self.ClientUin = None
        self.ClientName = None
        self.ClientFlag = None
        self.OrderDirection = None
        self.ClientUins = None
        self.HasOverdueBill = None
        self.ClientRemark = None
        self.Offset = None
        self.Limit = None
        self.ClientType = None
        self.ProjectType = None
        self.SalesUin = None
        self.SalesName = None


    def _deserialize(self, params):
        self.ClientUin = params.get("ClientUin")
        self.ClientName = params.get("ClientName")
        self.ClientFlag = params.get("ClientFlag")
        self.OrderDirection = params.get("OrderDirection")
        self.ClientUins = params.get("ClientUins")
        self.HasOverdueBill = params.get("HasOverdueBill")
        self.ClientRemark = params.get("ClientRemark")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ClientType = params.get("ClientType")
        self.ProjectType = params.get("ProjectType")
        self.SalesUin = params.get("SalesUin")
        self.SalesName = params.get("SalesName")


class DescribeAgentAuditedClientsResponse(AbstractModel):
    """DescribeAgentAuditedClients返回參數結構體

    """

    def __init__(self):
        """
        :param AgentClientSet: 已審核代客清單
        :type AgentClientSet: list of AgentAuditedClient
        :param TotalCount: 符合條件的代客總數
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AgentClientSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AgentClientSet") is not None:
            self.AgentClientSet = []
            for item in params.get("AgentClientSet"):
                obj = AgentAuditedClient()
                obj._deserialize(item)
                self.AgentClientSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAgentBillsRequest(AbstractModel):
    """DescribeAgentBills請求參數結構體

    """

    def __init__(self):
        """
        :param SettleMonth: 支付月份，如2018-02
        :type SettleMonth: str
        :param ClientUin: 客戶賬号ID
        :type ClientUin: str
        :param PayMode: 支付方式，prepay/postpay
        :type PayMode: str
        :param OrderId: 預付費訂單号
        :type OrderId: str
        :param ClientRemark: 客戶備注名稱
        :type ClientRemark: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制數目
        :type Limit: int
        """
        self.SettleMonth = None
        self.ClientUin = None
        self.PayMode = None
        self.OrderId = None
        self.ClientRemark = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SettleMonth = params.get("SettleMonth")
        self.ClientUin = params.get("ClientUin")
        self.PayMode = params.get("PayMode")
        self.OrderId = params.get("OrderId")
        self.ClientRemark = params.get("ClientRemark")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAgentBillsResponse(AbstractModel):
    """DescribeAgentBills返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合查詢條件清單總數量
        :type TotalCount: int
        :param AgentBillSet: 業務明細清單
        :type AgentBillSet: list of AgentBillElem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AgentBillSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AgentBillSet") is not None:
            self.AgentBillSet = []
            for item in params.get("AgentBillSet"):
                obj = AgentBillElem()
                obj._deserialize(item)
                self.AgentBillSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAgentClientsRequest(AbstractModel):
    """DescribeAgentClients請求參數結構體

    """

    def __init__(self):
        """
        :param ClientUin: 客戶賬号ID
        :type ClientUin: str
        :param ClientName: 客戶名稱。由于涉及隐私，名稱打碼顯示，故名稱僅支援打碼後的模糊搜索
        :type ClientName: str
        :param ClientFlag: 客戶類型，a/b，類型定義參考 相關政策文件
        :type ClientFlag: str
        :param OrderDirection: ASC/DESC， 不區分大小寫，按申請時間排序
        :type OrderDirection: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制數目
        :type Limit: int
        :param SalesUin: 業務員ID
        :type SalesUin: str
        :param SalesName: 業務員姓名（模糊查詢）
        :type SalesName: str
        """
        self.ClientUin = None
        self.ClientName = None
        self.ClientFlag = None
        self.OrderDirection = None
        self.Offset = None
        self.Limit = None
        self.SalesUin = None
        self.SalesName = None


    def _deserialize(self, params):
        self.ClientUin = params.get("ClientUin")
        self.ClientName = params.get("ClientName")
        self.ClientFlag = params.get("ClientFlag")
        self.OrderDirection = params.get("OrderDirection")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SalesUin = params.get("SalesUin")
        self.SalesName = params.get("SalesName")


class DescribeAgentClientsResponse(AbstractModel):
    """DescribeAgentClients返回參數結構體

    """

    def __init__(self):
        """
        :param AgentClientSet: 待審核代客清單
        :type AgentClientSet: list of AgentClientElem
        :param TotalCount: 符合條件的代客總數
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AgentClientSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AgentClientSet") is not None:
            self.AgentClientSet = []
            for item in params.get("AgentClientSet"):
                obj = AgentClientElem()
                obj._deserialize(item)
                self.AgentClientSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAgentDealsCacheRequest(AbstractModel):
    """DescribeAgentDealsCache請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制數目
        :type Limit: int
        :param CreatTimeRangeStart: 下單時間範圍起始點
        :type CreatTimeRangeStart: str
        :param CreatTimeRangeEnd: 下單時間範圍終止點
        :type CreatTimeRangeEnd: str
        :param Order: 0:下單時間降序；其他：下單時間升序
        :type Order: int
        :param Status: 訂單的狀态(1：未支付;2：已支付;3：發貨中;4：已發貨;5：發貨失敗;6：已退款;7：已關單;8：訂單過期;9：訂單已失效;10：産品已失效;11：代付拒絕;12：支付中)
        :type Status: int
        :param OwnerUins: 下單人賬号ID清單
        :type OwnerUins: list of str
        :param DealNames: 訂單号清單
        :type DealNames: list of str
        :param PayerMode: 支付方式，0：自付；1：代付
        :type PayerMode: int
        """
        self.Offset = None
        self.Limit = None
        self.CreatTimeRangeStart = None
        self.CreatTimeRangeEnd = None
        self.Order = None
        self.Status = None
        self.OwnerUins = None
        self.DealNames = None
        self.PayerMode = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.CreatTimeRangeStart = params.get("CreatTimeRangeStart")
        self.CreatTimeRangeEnd = params.get("CreatTimeRangeEnd")
        self.Order = params.get("Order")
        self.Status = params.get("Status")
        self.OwnerUins = params.get("OwnerUins")
        self.DealNames = params.get("DealNames")
        self.PayerMode = params.get("PayerMode")


class DescribeAgentDealsCacheResponse(AbstractModel):
    """DescribeAgentDealsCache返回參數結構體

    """

    def __init__(self):
        """
        :param AgentDealSet: 訂單數組
        :type AgentDealSet: list of AgentDealElem
        :param TotalCount: 符合條件的訂單總數量
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AgentDealSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AgentDealSet") is not None:
            self.AgentDealSet = []
            for item in params.get("AgentDealSet"):
                obj = AgentDealElem()
                obj._deserialize(item)
                self.AgentDealSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAgentPayDealsRequest(AbstractModel):
    """DescribeAgentPayDeals請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制數目
        :type Limit: int
        :param CreatTimeRangeStart: 下單時間範圍起始點(不傳時會預設查15天内訂單，傳值時需要傳15天内的起始時間)
        :type CreatTimeRangeStart: str
        :param CreatTimeRangeEnd: 下單時間範圍終止點
        :type CreatTimeRangeEnd: str
        :param Order: 0:下單時間降序；其他：下單時間升序
        :type Order: int
        :param Status: 訂單的狀态(1：未支付;2：已支付;3：發貨中;4：已發貨;5：發貨失敗;6：已退款;7：已關單;8：訂單過期;9：訂單已失效;10：産品已失效;11：代付拒絕;12：支付中)
        :type Status: int
        :param OwnerUins: 下單人賬号ID清單
        :type OwnerUins: list of str
        :param DealNames: 訂單号清單
        :type DealNames: list of str
        """
        self.Offset = None
        self.Limit = None
        self.CreatTimeRangeStart = None
        self.CreatTimeRangeEnd = None
        self.Order = None
        self.Status = None
        self.OwnerUins = None
        self.DealNames = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.CreatTimeRangeStart = params.get("CreatTimeRangeStart")
        self.CreatTimeRangeEnd = params.get("CreatTimeRangeEnd")
        self.Order = params.get("Order")
        self.Status = params.get("Status")
        self.OwnerUins = params.get("OwnerUins")
        self.DealNames = params.get("DealNames")


class DescribeAgentPayDealsResponse(AbstractModel):
    """DescribeAgentPayDeals返回參數結構體

    """

    def __init__(self):
        """
        :param AgentPayDealSet: 訂單數組
        :type AgentPayDealSet: list of AgentDealElem
        :param TotalCount: 符合條件的訂單總數量
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AgentPayDealSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AgentPayDealSet") is not None:
            self.AgentPayDealSet = []
            for item in params.get("AgentPayDealSet"):
                obj = AgentDealElem()
                obj._deserialize(item)
                self.AgentPayDealSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeClientBalanceRequest(AbstractModel):
    """DescribeClientBalance請求參數結構體

    """

    def __init__(self):
        """
        :param ClientUin: 客戶(代客)賬号ID
        :type ClientUin: str
        """
        self.ClientUin = None


    def _deserialize(self, params):
        self.ClientUin = params.get("ClientUin")


class DescribeClientBalanceResponse(AbstractModel):
    """DescribeClientBalance返回參數結構體

    """

    def __init__(self):
        """
        :param Balance: 帳戶餘額，單位分
        :type Balance: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Balance = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Balance = params.get("Balance")
        self.RequestId = params.get("RequestId")


class DescribeRebateInfosRequest(AbstractModel):
    """DescribeRebateInfos請求參數結構體

    """

    def __init__(self):
        """
        :param RebateMonth: 返傭月份，如2018-02
        :type RebateMonth: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制數目
        :type Limit: int
        """
        self.RebateMonth = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.RebateMonth = params.get("RebateMonth")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeRebateInfosResponse(AbstractModel):
    """DescribeRebateInfos返回參數結構體

    """

    def __init__(self):
        """
        :param RebateInfoSet: 返傭訊息清單
        :type RebateInfoSet: list of RebateInfoElem
        :param TotalCount: 符合查詢條件返傭訊息數目
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RebateInfoSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RebateInfoSet") is not None:
            self.RebateInfoSet = []
            for item in params.get("RebateInfoSet"):
                obj = RebateInfoElem()
                obj._deserialize(item)
                self.RebateInfoSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSalesmansRequest(AbstractModel):
    """DescribeSalesmans請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制數目
        :type Limit: int
        :param SalesName: 業務員姓名(模糊查詢)
        :type SalesName: str
        :param SalesUin: 業務員ID
        :type SalesUin: str
        :param OrderDirection: ASC/DESC， 不區分大小寫，按創建通過時間排序
        :type OrderDirection: str
        """
        self.Offset = None
        self.Limit = None
        self.SalesName = None
        self.SalesUin = None
        self.OrderDirection = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SalesName = params.get("SalesName")
        self.SalesUin = params.get("SalesUin")
        self.OrderDirection = params.get("OrderDirection")


class DescribeSalesmansResponse(AbstractModel):
    """DescribeSalesmans返回參數結構體

    """

    def __init__(self):
        """
        :param AgentSalesmanSet: 業務員清單
        :type AgentSalesmanSet: list of AgentSalesmanElem
        :param TotalCount: 符合條件的代客總數
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AgentSalesmanSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AgentSalesmanSet") is not None:
            self.AgentSalesmanSet = []
            for item in params.get("AgentSalesmanSet"):
                obj = AgentSalesmanElem()
                obj._deserialize(item)
                self.AgentSalesmanSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ModifyClientRemarkRequest(AbstractModel):
    """ModifyClientRemark請求參數結構體

    """

    def __init__(self):
        """
        :param ClientRemark: 客戶備注名稱
        :type ClientRemark: str
        :param ClientUin: 客戶賬号ID
        :type ClientUin: str
        """
        self.ClientRemark = None
        self.ClientUin = None


    def _deserialize(self, params):
        self.ClientRemark = params.get("ClientRemark")
        self.ClientUin = params.get("ClientUin")


class ModifyClientRemarkResponse(AbstractModel):
    """ModifyClientRemark返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RebateInfoElem(AbstractModel):
    """返傭訊息定義

    """

    def __init__(self):
        """
        :param Uin:  賬号ID
        :type Uin: str
        :param RebateMonth: 返傭月份，如2018-02
        :type RebateMonth: str
        :param Amt: 返傭金額，單位分
        :type Amt: int
        :param MonthSales: 月業績，單位分
        :type MonthSales: int
        :param QuarterSales: 季度業績，單位分
        :type QuarterSales: int
        :param ExceptionFlag: NORMAL(正常)/HAS_OVERDUE_BILL(欠費)/NO_CONTRACT(缺合同)
        :type ExceptionFlag: str
        """
        self.Uin = None
        self.RebateMonth = None
        self.Amt = None
        self.MonthSales = None
        self.QuarterSales = None
        self.ExceptionFlag = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.RebateMonth = params.get("RebateMonth")
        self.Amt = params.get("Amt")
        self.MonthSales = params.get("MonthSales")
        self.QuarterSales = params.get("QuarterSales")
        self.ExceptionFlag = params.get("ExceptionFlag")


class RemovePayRelationForClientRequest(AbstractModel):
    """RemovePayRelationForClient請求參數結構體

    """

    def __init__(self):
        """
        :param ClientUin: 客戶賬号ID
        :type ClientUin: str
        """
        self.ClientUin = None


    def _deserialize(self, params):
        self.ClientUin = params.get("ClientUin")


class RemovePayRelationForClientResponse(AbstractModel):
    """RemovePayRelationForClient返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")