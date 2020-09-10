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


class Acct(AbstractModel):
    """帳戶訊息

    """

    def __init__(self):
        """
        :param SubAcctNo: STRING(50)，見證子帳戶的賬号（可重複）
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubAcctNo: str
        :param SubAcctProperty: STRING(10)，見證子帳戶的屬性（可重複。1: 普通會員子賬号; 2: 挂賬子賬号; 3: 手續約子賬号; 4: 利息子賬号; 5: 平台擔保子賬号）
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubAcctProperty: str
        :param TranNetMemberCode: STRING(32)，交易網會員代碼（可重複）
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranNetMemberCode: str
        :param SubAcctName: STRING(150)，見證子帳戶的名稱（可重複）
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubAcctName: str
        :param AcctAvailBal: STRING(20)，見證子帳戶可用餘額（可重複）
注意：此欄位可能返回 null，表示取不到有效值。
        :type AcctAvailBal: str
        :param CashAmt: STRING(20)，見證子帳戶可提現金額（可重複。開戶日期或修改日期）
注意：此欄位可能返回 null，表示取不到有效值。
        :type CashAmt: str
        :param MaintenanceDate: STRING(8)，維護日期
注意：此欄位可能返回 null，表示取不到有效值。
        :type MaintenanceDate: str
        """
        self.SubAcctNo = None
        self.SubAcctProperty = None
        self.TranNetMemberCode = None
        self.SubAcctName = None
        self.AcctAvailBal = None
        self.CashAmt = None
        self.MaintenanceDate = None


    def _deserialize(self, params):
        self.SubAcctNo = params.get("SubAcctNo")
        self.SubAcctProperty = params.get("SubAcctProperty")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.SubAcctName = params.get("SubAcctName")
        self.AcctAvailBal = params.get("AcctAvailBal")
        self.CashAmt = params.get("CashAmt")
        self.MaintenanceDate = params.get("MaintenanceDate")


class ApplyApplicationMaterialRequest(AbstractModel):
    """ApplyApplicationMaterial請求參數結構體

    """

    def __init__(self):
        """
        :param TransactionId: 對接方匯出指令編号
        :type TransactionId: str
        :param DeclareId: 申報流水号
        :type DeclareId: str
        :param PayerId: 付款人ID
        :type PayerId: str
        :param SourceCurrency: 源币種
        :type SourceCurrency: str
        :param TargetCurrency: 目的币種
        :type TargetCurrency: str
        :param TradeCode: 貿易編碼
        :type TradeCode: str
        :param OriginalDeclareId: 原申報流水号
        :type OriginalDeclareId: str
        :param SourceAmount: 源金額
        :type SourceAmount: int
        :param TargetAmount: 目的金額
        :type TargetAmount: int
        :param Profile: 接入環境。沙箱環境填sandbox
        :type Profile: str
        """
        self.TransactionId = None
        self.DeclareId = None
        self.PayerId = None
        self.SourceCurrency = None
        self.TargetCurrency = None
        self.TradeCode = None
        self.OriginalDeclareId = None
        self.SourceAmount = None
        self.TargetAmount = None
        self.Profile = None


    def _deserialize(self, params):
        self.TransactionId = params.get("TransactionId")
        self.DeclareId = params.get("DeclareId")
        self.PayerId = params.get("PayerId")
        self.SourceCurrency = params.get("SourceCurrency")
        self.TargetCurrency = params.get("TargetCurrency")
        self.TradeCode = params.get("TradeCode")
        self.OriginalDeclareId = params.get("OriginalDeclareId")
        self.SourceAmount = params.get("SourceAmount")
        self.TargetAmount = params.get("TargetAmount")
        self.Profile = params.get("Profile")


class ApplyApplicationMaterialResponse(AbstractModel):
    """ApplyApplicationMaterial返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 提交申報材料結果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.ApplyDeclareResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApplyDeclareResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ApplyDeclareData(AbstractModel):
    """提交申報材料結果

    """

    def __init__(self):
        """
        :param MerchantId: 商戶号
        :type MerchantId: str
        :param TransactionId: 第三方指令編号
        :type TransactionId: str
        :param Status: 受理狀态
        :type Status: str
        :param DeclareId: 申報流水号
        :type DeclareId: str
        :param OriginalDeclareId: 原申報流水号
注意：此欄位可能返回 null，表示取不到有效值。
        :type OriginalDeclareId: str
        :param PayerId: 付款人ID
        :type PayerId: str
        """
        self.MerchantId = None
        self.TransactionId = None
        self.Status = None
        self.DeclareId = None
        self.OriginalDeclareId = None
        self.PayerId = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.TransactionId = params.get("TransactionId")
        self.Status = params.get("Status")
        self.DeclareId = params.get("DeclareId")
        self.OriginalDeclareId = params.get("OriginalDeclareId")
        self.PayerId = params.get("PayerId")


class ApplyDeclareResult(AbstractModel):
    """提交申報材料結果

    """

    def __init__(self):
        """
        :param Code: 錯誤碼
        :type Code: str
        :param Data: 提交申報材料數據
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.ApplyDeclareData`
        """
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = ApplyDeclareData()
            self.Data._deserialize(params.get("Data"))


class ApplyOutwardOrderData(AbstractModel):
    """匯出指令申請數據

    """

    def __init__(self):
        """
        :param MerchantId: 商戶号
        :type MerchantId: str
        :param TransactionId: 對接方匯出指令編号
        :type TransactionId: str
        :param Status: 受理狀态
        :type Status: str
        """
        self.MerchantId = None
        self.TransactionId = None
        self.Status = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.TransactionId = params.get("TransactionId")
        self.Status = params.get("Status")


class ApplyOutwardOrderRequest(AbstractModel):
    """ApplyOutwardOrder請求參數結構體

    """

    def __init__(self):
        """
        :param TransactionId: 對接方匯出指令編号
        :type TransactionId: str
        :param PricingCurrency: 定價币種
        :type PricingCurrency: str
        :param SourceCurrency: 源币種
        :type SourceCurrency: str
        :param TargetCurrency: 目的币種
        :type TargetCurrency: str
        :param PayeeType: 收款人類型
        :type PayeeType: str
        :param PayeeAccount: 收款人賬号
        :type PayeeAccount: str
        :param SourceAmount: 源币種金額
        :type SourceAmount: float
        :param TargetAmount: 目的金額
        :type TargetAmount: float
        :param PayeeName: 收款人姓名
        :type PayeeName: str
        :param PayeeAddress: 收款人網址
        :type PayeeAddress: str
        :param PayeeBankAccountType: 收款人銀行賬号類型
        :type PayeeBankAccountType: str
        :param PayeeCountryCode: 收款人國家或地區編碼
        :type PayeeCountryCode: str
        :param PayeeBankName: 收款人開戶銀行名稱
        :type PayeeBankName: str
        :param PayeeBankAddress: 收款人開戶銀行網址
        :type PayeeBankAddress: str
        :param PayeeBankDistrict: 收款人開戶銀行所在國家或地區編碼
        :type PayeeBankDistrict: str
        :param PayeeBankSwiftCode: 收款銀行SwiftCode
        :type PayeeBankSwiftCode: str
        :param PayeeBankType: 收款銀行國際編碼類型
        :type PayeeBankType: str
        :param PayeeBankCode: 收款銀行國際編碼
        :type PayeeBankCode: str
        :param ReferenceForBeneficiary: 收款人附言
        :type ReferenceForBeneficiary: str
        :param Profile: 接入環境。沙箱環境填sandbox
        :type Profile: str
        """
        self.TransactionId = None
        self.PricingCurrency = None
        self.SourceCurrency = None
        self.TargetCurrency = None
        self.PayeeType = None
        self.PayeeAccount = None
        self.SourceAmount = None
        self.TargetAmount = None
        self.PayeeName = None
        self.PayeeAddress = None
        self.PayeeBankAccountType = None
        self.PayeeCountryCode = None
        self.PayeeBankName = None
        self.PayeeBankAddress = None
        self.PayeeBankDistrict = None
        self.PayeeBankSwiftCode = None
        self.PayeeBankType = None
        self.PayeeBankCode = None
        self.ReferenceForBeneficiary = None
        self.Profile = None


    def _deserialize(self, params):
        self.TransactionId = params.get("TransactionId")
        self.PricingCurrency = params.get("PricingCurrency")
        self.SourceCurrency = params.get("SourceCurrency")
        self.TargetCurrency = params.get("TargetCurrency")
        self.PayeeType = params.get("PayeeType")
        self.PayeeAccount = params.get("PayeeAccount")
        self.SourceAmount = params.get("SourceAmount")
        self.TargetAmount = params.get("TargetAmount")
        self.PayeeName = params.get("PayeeName")
        self.PayeeAddress = params.get("PayeeAddress")
        self.PayeeBankAccountType = params.get("PayeeBankAccountType")
        self.PayeeCountryCode = params.get("PayeeCountryCode")
        self.PayeeBankName = params.get("PayeeBankName")
        self.PayeeBankAddress = params.get("PayeeBankAddress")
        self.PayeeBankDistrict = params.get("PayeeBankDistrict")
        self.PayeeBankSwiftCode = params.get("PayeeBankSwiftCode")
        self.PayeeBankType = params.get("PayeeBankType")
        self.PayeeBankCode = params.get("PayeeBankCode")
        self.ReferenceForBeneficiary = params.get("ReferenceForBeneficiary")
        self.Profile = params.get("Profile")


class ApplyOutwardOrderResponse(AbstractModel):
    """ApplyOutwardOrder返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 匯出指令申請
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.ApplyOutwardOrderResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApplyOutwardOrderResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ApplyOutwardOrderResult(AbstractModel):
    """匯出指令申請結果

    """

    def __init__(self):
        """
        :param Data: 匯出指令申請數據
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.ApplyOutwardOrderData`
        :param Code: 錯誤碼
        :type Code: str
        """
        self.Data = None
        self.Code = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = ApplyOutwardOrderData()
            self.Data._deserialize(params.get("Data"))
        self.Code = params.get("Code")


class ApplyPayerInfoRequest(AbstractModel):
    """ApplyPayerInfo請求參數結構體

    """

    def __init__(self):
        """
        :param PayerId: 付款人ID
        :type PayerId: str
        :param PayerType: 付款人類型 (個人: INDIVIDUAL, 企業: CORPORATE)
        :type PayerType: str
        :param PayerName: 付款人姓名
        :type PayerName: str
        :param PayerIdType: 付款人證件類型 (身份證: ID_CARD, 統一社會信用代碼: UNIFIED_CREDIT_CODE)
        :type PayerIdType: str
        :param PayerIdNo: 付款人證件号
        :type PayerIdNo: str
        :param PayerCountryCode: 付款人常駐國家或地區編碼 (見常見問題-國家/地區編碼)
        :type PayerCountryCode: str
        :param PayerContactName: 付款人聯系人名稱
        :type PayerContactName: str
        :param PayerContactNumber: 付款人聯系電話 (PayerType=CORPORATE 必填)
        :type PayerContactNumber: str
        :param PayerEmailAddress: 付款人聯系電子信箱
        :type PayerEmailAddress: str
        :param Profile: 接入環境。沙箱環境填sandbox
        :type Profile: str
        """
        self.PayerId = None
        self.PayerType = None
        self.PayerName = None
        self.PayerIdType = None
        self.PayerIdNo = None
        self.PayerCountryCode = None
        self.PayerContactName = None
        self.PayerContactNumber = None
        self.PayerEmailAddress = None
        self.Profile = None


    def _deserialize(self, params):
        self.PayerId = params.get("PayerId")
        self.PayerType = params.get("PayerType")
        self.PayerName = params.get("PayerName")
        self.PayerIdType = params.get("PayerIdType")
        self.PayerIdNo = params.get("PayerIdNo")
        self.PayerCountryCode = params.get("PayerCountryCode")
        self.PayerContactName = params.get("PayerContactName")
        self.PayerContactNumber = params.get("PayerContactNumber")
        self.PayerEmailAddress = params.get("PayerEmailAddress")
        self.Profile = params.get("Profile")


class ApplyPayerInfoResponse(AbstractModel):
    """ApplyPayerInfo返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 付款人申請結果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.ApplyPayerinfoResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApplyPayerinfoResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ApplyPayerinfoData(AbstractModel):
    """付款人申請結果

    """

    def __init__(self):
        """
        :param MerchantId: 商戶号
        :type MerchantId: str
        :param PayerId: 付款人ID
        :type PayerId: str
        :param Status: 狀态
        :type Status: str
        :param FailReason: 失敗原因
注意：此欄位可能返回 null，表示取不到有效值。
        :type FailReason: str
        """
        self.MerchantId = None
        self.PayerId = None
        self.Status = None
        self.FailReason = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.PayerId = params.get("PayerId")
        self.Status = params.get("Status")
        self.FailReason = params.get("FailReason")


class ApplyPayerinfoResult(AbstractModel):
    """付款人申請結果

    """

    def __init__(self):
        """
        :param Code: 錯誤碼
        :type Code: str
        :param Data: 數據
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.ApplyPayerinfoData`
        """
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = ApplyPayerinfoData()
            self.Data._deserialize(params.get("Data"))


class ApplyReWithdrawalRequest(AbstractModel):
    """ApplyReWithdrawal請求參數結構體

    """

    def __init__(self):
        """
        :param BusinessType: 聚鑫業務類型
        :type BusinessType: int
        :param MidasSecretId: 由平台客服提供的計費金鑰Id
        :type MidasSecretId: str
        :param MidasSignature: 計費簽名
        :type MidasSignature: str
        :param Body: 提現訊息
        :type Body: :class:`tencentcloud.cpdp.v20190820.models.WithdrawBill`
        :param MidasAppId: 聚鑫業務ID
        :type MidasAppId: str
        """
        self.BusinessType = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.Body = None
        self.MidasAppId = None


    def _deserialize(self, params):
        self.BusinessType = params.get("BusinessType")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        if params.get("Body") is not None:
            self.Body = WithdrawBill()
            self.Body._deserialize(params.get("Body"))
        self.MidasAppId = params.get("MidasAppId")


class ApplyReWithdrawalResponse(AbstractModel):
    """ApplyReWithdrawal返回參數結構體

    """

    def __init__(self):
        """
        :param WithdrawOrderId: 重新提現業務訂單号
        :type WithdrawOrderId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.WithdrawOrderId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WithdrawOrderId = params.get("WithdrawOrderId")
        self.RequestId = params.get("RequestId")


class ApplyTradeData(AbstractModel):
    """提交貿易材料結果

    """

    def __init__(self):
        """
        :param MerchantId: 商戶号
        :type MerchantId: str
        :param TradeFileId: 貿易材料流水号
        :type TradeFileId: str
        :param TradeCurrency: 交易币種
        :type TradeCurrency: str
        :param TradeAmount: 交易金額
        :type TradeAmount: str
        :param PayerId: 付款人ID
        :type PayerId: str
        :param Status: 狀态
        :type Status: str
        """
        self.MerchantId = None
        self.TradeFileId = None
        self.TradeCurrency = None
        self.TradeAmount = None
        self.PayerId = None
        self.Status = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.TradeFileId = params.get("TradeFileId")
        self.TradeCurrency = params.get("TradeCurrency")
        self.TradeAmount = params.get("TradeAmount")
        self.PayerId = params.get("PayerId")
        self.Status = params.get("Status")


class ApplyTradeRequest(AbstractModel):
    """ApplyTrade請求參數結構體

    """

    def __init__(self):
        """
        :param TradeFileId: 貿易材料流水号
        :type TradeFileId: str
        :param TradeOrderId: 貿易材料訂單号
        :type TradeOrderId: str
        :param PayerId: 付款人ID
        :type PayerId: str
        :param PayeeName: 付款人姓名
        :type PayeeName: str
        :param PayeeCountryCode: 收款人常駐國家或地區編碼 (見常見問題)
        :type PayeeCountryCode: str
        :param TradeType: 貿易類型 (GOODS: 商品, SERVICE: 服務)
        :type TradeType: str
        :param TradeTime: 交易時間 (格式: yyyyMMdd)
        :type TradeTime: str
        :param TradeCurrency: 交易币種
        :type TradeCurrency: str
        :param TradeAmount: 交易金額
        :type TradeAmount: float
        :param TradeName: 交易名稱 
(TradeType=GOODS時填寫物品名稱，可填寫多個，格式無要求；
TradeType=SERVICE時填寫貿易類别，見常見問題-貿易類别)
        :type TradeName: str
        :param TradeCount: 交易數量 (TradeType=GOODS 填寫物品數量, TradeType=SERVICE填寫服務次數)
        :type TradeCount: int
        :param GoodsCarrier: 貨貿承運人 (TradeType=GOODS 必填)
        :type GoodsCarrier: str
        :param ServiceDetail: 服貿交易細節 (TradeType=GOODS 必填, 見常見問題-交易細節)
        :type ServiceDetail: str
        :param ServiceTime: 服貿服務時間 (TradeType=GOODS 必填, 見常見問題-服務時間)
        :type ServiceTime: str
        :param Profile: 接入環境。沙箱環境填sandbox
        :type Profile: str
        """
        self.TradeFileId = None
        self.TradeOrderId = None
        self.PayerId = None
        self.PayeeName = None
        self.PayeeCountryCode = None
        self.TradeType = None
        self.TradeTime = None
        self.TradeCurrency = None
        self.TradeAmount = None
        self.TradeName = None
        self.TradeCount = None
        self.GoodsCarrier = None
        self.ServiceDetail = None
        self.ServiceTime = None
        self.Profile = None


    def _deserialize(self, params):
        self.TradeFileId = params.get("TradeFileId")
        self.TradeOrderId = params.get("TradeOrderId")
        self.PayerId = params.get("PayerId")
        self.PayeeName = params.get("PayeeName")
        self.PayeeCountryCode = params.get("PayeeCountryCode")
        self.TradeType = params.get("TradeType")
        self.TradeTime = params.get("TradeTime")
        self.TradeCurrency = params.get("TradeCurrency")
        self.TradeAmount = params.get("TradeAmount")
        self.TradeName = params.get("TradeName")
        self.TradeCount = params.get("TradeCount")
        self.GoodsCarrier = params.get("GoodsCarrier")
        self.ServiceDetail = params.get("ServiceDetail")
        self.ServiceTime = params.get("ServiceTime")
        self.Profile = params.get("Profile")


class ApplyTradeResponse(AbstractModel):
    """ApplyTrade返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 提交貿易材料結果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.ApplyTradeResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApplyTradeResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ApplyTradeResult(AbstractModel):
    """提交貿易材料結果

    """

    def __init__(self):
        """
        :param Code: 錯誤碼
        :type Code: str
        :param Data: 提交貿易材料數據
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.ApplyTradeData`
        """
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = ApplyTradeData()
            self.Data._deserialize(params.get("Data"))


class ApplyWithdrawalRequest(AbstractModel):
    """ApplyWithdrawal請求參數結構體

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param SubAppId: 聚鑫計費SubAppId，代表子商戶
        :type SubAppId: str
        :param SettleAcctNo: 用于提現
<敏感訊息>加密詳見《商戶端介面敏感訊息加密說明》
        :type SettleAcctNo: str
        :param SettleAcctName: 結算帳戶戶名
<敏感訊息>加密詳見《商戶端介面敏感訊息加密說明》
        :type SettleAcctName: str
        :param CurrencyType: 币種 RMB
        :type CurrencyType: str
        :param CurrencyUnit: 單位，1：元，2：角，3：分
        :type CurrencyUnit: int
        :param CurrencyAmt: 金額
        :type CurrencyAmt: str
        :param TranWebName: 交易網名稱
        :type TranWebName: str
        :param IdType: 會員證件類型
        :type IdType: str
        :param IdCode: 會員證件号碼
<敏感訊息>加密詳見《商戶端介面敏感訊息加密說明》
        :type IdCode: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全金鑰計算的簽名
        :type MidasSignature: str
        """
        self.MidasAppId = None
        self.SubAppId = None
        self.SettleAcctNo = None
        self.SettleAcctName = None
        self.CurrencyType = None
        self.CurrencyUnit = None
        self.CurrencyAmt = None
        self.TranWebName = None
        self.IdType = None
        self.IdCode = None
        self.MidasSecretId = None
        self.MidasSignature = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.SettleAcctNo = params.get("SettleAcctNo")
        self.SettleAcctName = params.get("SettleAcctName")
        self.CurrencyType = params.get("CurrencyType")
        self.CurrencyUnit = params.get("CurrencyUnit")
        self.CurrencyAmt = params.get("CurrencyAmt")
        self.TranWebName = params.get("TranWebName")
        self.IdType = params.get("IdType")
        self.IdCode = params.get("IdCode")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")


class ApplyWithdrawalResponse(AbstractModel):
    """ApplyWithdrawal返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BankCardItem(AbstractModel):
    """綁卡清單

    """

    def __init__(self):
        """
        :param EiconBankBranchId: 超級網銀行号
        :type EiconBankBranchId: str
        :param CnapsBranchId: 大小額行号
        :type CnapsBranchId: str
        :param SettleAcctType: 結算帳戶類型
1 – 本行帳戶
2 – 他行帳戶
        :type SettleAcctType: int
        :param SettleAcctName: 結算帳戶戶名
<敏感訊息>
        :type SettleAcctName: str
        :param AcctBranchName: 開戶行名稱
        :type AcctBranchName: str
        :param SettleAcctNo: 用于提現
<敏感訊息>
        :type SettleAcctNo: str
        :param SubAppId: 聚鑫計費SubAppId，代表子商戶
        :type SubAppId: str
        :param BindType: 驗證類型
1 – 小額轉賬驗證
2 – 簡訊驗證
        :type BindType: int
        :param Mobile: 用于簡訊驗證
BindType==2時必填
<敏感訊息>
        :type Mobile: str
        :param IdType: 證件類型
        :type IdType: str
        :param IdCode: 證件号碼
<敏感訊息>
        :type IdCode: str
        """
        self.EiconBankBranchId = None
        self.CnapsBranchId = None
        self.SettleAcctType = None
        self.SettleAcctName = None
        self.AcctBranchName = None
        self.SettleAcctNo = None
        self.SubAppId = None
        self.BindType = None
        self.Mobile = None
        self.IdType = None
        self.IdCode = None


    def _deserialize(self, params):
        self.EiconBankBranchId = params.get("EiconBankBranchId")
        self.CnapsBranchId = params.get("CnapsBranchId")
        self.SettleAcctType = params.get("SettleAcctType")
        self.SettleAcctName = params.get("SettleAcctName")
        self.AcctBranchName = params.get("AcctBranchName")
        self.SettleAcctNo = params.get("SettleAcctNo")
        self.SubAppId = params.get("SubAppId")
        self.BindType = params.get("BindType")
        self.Mobile = params.get("Mobile")
        self.IdType = params.get("IdType")
        self.IdCode = params.get("IdCode")


class BindAcctRequest(AbstractModel):
    """BindAcct請求參數結構體

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param SubAppId: 聚鑫計費SubAppId，代表子商戶
        :type SubAppId: str
        :param BindType: 1 – 小額轉賬驗證
2 – 簡訊驗證
每個結算帳戶每天只能使用一次小額轉賬驗證
        :type BindType: int
        :param SettleAcctNo: 用于提現
<敏感訊息>加密詳見《商戶端介面敏感訊息加密說明》
        :type SettleAcctNo: str
        :param SettleAcctName: 結算帳戶戶名
<敏感訊息>加密詳見《商戶端介面敏感訊息加密說明》
        :type SettleAcctName: str
        :param SettleAcctType: 1 – 本行帳戶
2 – 他行帳戶
        :type SettleAcctType: int
        :param IdType: 證件類型，見《證件類型》表
        :type IdType: str
        :param IdCode: 證件号碼
<敏感訊息>加密詳見《商戶端介面敏感訊息加密說明》
        :type IdCode: str
        :param AcctBranchName: 開戶行名稱
        :type AcctBranchName: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全金鑰計算的簽名
        :type MidasSignature: str
        :param Mobile: 用于簡訊驗證
BindType==2時必填
<敏感訊息>加密詳見《商戶端介面敏感訊息加密說明》
        :type Mobile: str
        :param CnapsBranchId: 大小額行号，超級網銀行号和大小額行号
二選一
        :type CnapsBranchId: str
        :param EiconBankBranchId: 超級網銀行号，超級網銀行号和大小額行号
二選一
        :type EiconBankBranchId: str
        """
        self.MidasAppId = None
        self.SubAppId = None
        self.BindType = None
        self.SettleAcctNo = None
        self.SettleAcctName = None
        self.SettleAcctType = None
        self.IdType = None
        self.IdCode = None
        self.AcctBranchName = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.Mobile = None
        self.CnapsBranchId = None
        self.EiconBankBranchId = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.BindType = params.get("BindType")
        self.SettleAcctNo = params.get("SettleAcctNo")
        self.SettleAcctName = params.get("SettleAcctName")
        self.SettleAcctType = params.get("SettleAcctType")
        self.IdType = params.get("IdType")
        self.IdCode = params.get("IdCode")
        self.AcctBranchName = params.get("AcctBranchName")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.Mobile = params.get("Mobile")
        self.CnapsBranchId = params.get("CnapsBranchId")
        self.EiconBankBranchId = params.get("EiconBankBranchId")


class BindAcctResponse(AbstractModel):
    """BindAcct返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BindRelateAccReUnionPayRequest(AbstractModel):
    """BindRelateAccReUnionPay請求參數結構體

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商戶号（簽約客戶号）
        :type MrchCode: str
        :param TranNetMemberCode: STRING(32)，交易網會員代碼（若需要把一個待綁定帳戶關聯到兩個會員名下，此欄位可上送兩個會員的交易網代碼，并且須用“|::|”（右側）進行分隔）
        :type TranNetMemberCode: str
        :param MemberAcctNo: STRING(50)，會員的待綁定帳戶的賬号（即 BindRelateAcctUnionPay介面中的“會員的待綁定帳戶的賬号”）
        :type MemberAcctNo: str
        :param MessageCheckCode: STRING(20)，簡訊驗證碼（即 BindRelateAcctUnionPay介面中的手機所接收到的簡訊驗證碼）
        :type MessageCheckCode: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.TranNetMemberCode = None
        self.MemberAcctNo = None
        self.MessageCheckCode = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberAcctNo = params.get("MemberAcctNo")
        self.MessageCheckCode = params.get("MessageCheckCode")
        self.ReservedMsg = params.get("ReservedMsg")


class BindRelateAccReUnionPayResponse(AbstractModel):
    """BindRelateAccReUnionPay返回參數結構體

    """

    def __init__(self):
        """
        :param FrontSeqNo: STRING(52)，見證系統流水号
注意：此欄位可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param TxnReturnCode: String(20)，返回碼
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回訊息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FrontSeqNo = None
        self.ReservedMsg = None
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.RequestId = params.get("RequestId")


class BindRelateAcctSmallAmountRequest(AbstractModel):
    """BindRelateAcctSmallAmount請求參數結構體

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商戶号（簽約客戶号）
        :type MrchCode: str
        :param TranNetMemberCode: STRING(32)，交易網會員代碼（若需要把一個待綁定帳戶關聯到兩個會員名下，此欄位可上送兩個會員的交易網代碼，并且須用“|::|”(右側)進行分隔）
        :type TranNetMemberCode: str
        :param MemberName: STRING(150)，見證子帳戶的戶名（首次綁定的情況下，此欄位即爲待綁定的提現帳戶的戶名。非首次綁定的情況下，須注意帶綁定的提現帳戶的戶名須與留存在後台系統的會員戶名一緻）
        :type MemberName: str
        :param MemberGlobalType: STRING(5)，會員證件類型（詳情見“常見問題”）
        :type MemberGlobalType: str
        :param MemberGlobalId: STRING(32)，會員證件号碼
        :type MemberGlobalId: str
        :param MemberAcctNo: STRING(50)，會員的待綁定帳戶的賬号（提現的銀行卡）
        :type MemberAcctNo: str
        :param BankType: STRING(10)，會員的待綁定帳戶的本他行類型（1: 本行; 2: 他行）
        :type BankType: str
        :param AcctOpenBranchName: STRING(150)，會員的待綁定帳戶的開戶行名稱
        :type AcctOpenBranchName: str
        :param Mobile: STRING(30)，會員的手機号（手機号須由長度爲11位的數字構成）
        :type Mobile: str
        :param CnapsBranchId: STRING(20)，會員的待綁定帳戶的開戶行的聯行号（本他行類型爲他行的情況下，此欄位和下一個欄位至少一個不爲空）
        :type CnapsBranchId: str
        :param EiconBankBranchId: STRING(20)，會員的待綁定帳戶的開戶行的超級網銀行号（本他行類型爲他行的情況下，此欄位和上一個欄位至少一個不爲空）
        :type EiconBankBranchId: str
        :param ReservedMsg: STRING(1027)，轉賬方式（1: 往賬鑒權(預設值); 2: 來賬鑒權）
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.TranNetMemberCode = None
        self.MemberName = None
        self.MemberGlobalType = None
        self.MemberGlobalId = None
        self.MemberAcctNo = None
        self.BankType = None
        self.AcctOpenBranchName = None
        self.Mobile = None
        self.CnapsBranchId = None
        self.EiconBankBranchId = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberName = params.get("MemberName")
        self.MemberGlobalType = params.get("MemberGlobalType")
        self.MemberGlobalId = params.get("MemberGlobalId")
        self.MemberAcctNo = params.get("MemberAcctNo")
        self.BankType = params.get("BankType")
        self.AcctOpenBranchName = params.get("AcctOpenBranchName")
        self.Mobile = params.get("Mobile")
        self.CnapsBranchId = params.get("CnapsBranchId")
        self.EiconBankBranchId = params.get("EiconBankBranchId")
        self.ReservedMsg = params.get("ReservedMsg")


class BindRelateAcctSmallAmountResponse(AbstractModel):
    """BindRelateAcctSmallAmount返回參數結構體

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回碼
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回訊息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域（來賬鑒權的方式下，此欄位的值爲客戶需往監管帳戶轉入的金額。在同名子帳戶綁定的場景下，若返回""VERIFIED""則說明無需驗證直接綁定成功）
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class BindRelateAcctUnionPayRequest(AbstractModel):
    """BindRelateAcctUnionPay請求參數結構體

    """

    def __init__(self):
        """
        :param TranNetMemberCode: STRING(32)，交易網會員代碼（若需要把一個待綁定帳戶關聯到兩個會員名下，此欄位可上送兩個會員的交易網代碼，并且須用“|::|”（右側）進行分隔）
        :type TranNetMemberCode: str
        :param MemberName: STRING(150)，見證子帳戶的戶名（首次綁定的情況下，此欄位即爲待綁定的提現帳戶的戶名。非首次綁定的情況下，須注意帶綁定的提現帳戶的戶名須與留存在後台系統的會員戶名一緻）
        :type MemberName: str
        :param MemberGlobalType: STRING(5)，會員證件類型（詳情見“常見問題”）
        :type MemberGlobalType: str
        :param MemberGlobalId: STRING(32)，會員證件号碼
        :type MemberGlobalId: str
        :param MemberAcctNo: STRING(50)，會員的待綁定帳戶的賬号（提現的銀行卡）
        :type MemberAcctNo: str
        :param BankType: STRING(10)，會員的待綁定帳戶的本他行類型（1: 本行; 2: 他行）
        :type BankType: str
        :param AcctOpenBranchName: STRING(150)，會員的待綁定帳戶的開戶行名稱（若大小額行号不填則送超級網銀号對應的銀行名稱，若填大小額行号則送大小額行号對應的銀行名稱）
        :type AcctOpenBranchName: str
        :param Mobile: STRING(30)，會員的手機号（手機号須由長度爲11位的數字構成）
        :type Mobile: str
        :param MrchCode: String(22)，商戶号（簽約客戶号）
        :type MrchCode: str
        :param CnapsBranchId: STRING(20)，會員的待綁定帳戶的開戶行的聯行号（本他行類型爲他行的情況下，此欄位和下一個欄位至少一個不爲空）
        :type CnapsBranchId: str
        :param EiconBankBranchId: STRING(20)，會員的待綁定帳戶的開戶行的超級網銀行号（本他行類型爲他行的情況下，此欄位和上一個欄位至少一個不爲空）
        :type EiconBankBranchId: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.TranNetMemberCode = None
        self.MemberName = None
        self.MemberGlobalType = None
        self.MemberGlobalId = None
        self.MemberAcctNo = None
        self.BankType = None
        self.AcctOpenBranchName = None
        self.Mobile = None
        self.MrchCode = None
        self.CnapsBranchId = None
        self.EiconBankBranchId = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberName = params.get("MemberName")
        self.MemberGlobalType = params.get("MemberGlobalType")
        self.MemberGlobalId = params.get("MemberGlobalId")
        self.MemberAcctNo = params.get("MemberAcctNo")
        self.BankType = params.get("BankType")
        self.AcctOpenBranchName = params.get("AcctOpenBranchName")
        self.Mobile = params.get("Mobile")
        self.MrchCode = params.get("MrchCode")
        self.CnapsBranchId = params.get("CnapsBranchId")
        self.EiconBankBranchId = params.get("EiconBankBranchId")
        self.ReservedMsg = params.get("ReservedMsg")


class BindRelateAcctUnionPayResponse(AbstractModel):
    """BindRelateAcctUnionPay返回參數結構體

    """

    def __init__(self):
        """
        :param ReservedMsg: STRING(1027)，保留域（在同名子帳戶綁定的場景下，若返回"VERIFIED"則說明無需驗證直接綁定成功）
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param TxnReturnCode: String(20)，返回碼
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回訊息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ReservedMsg = None
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReservedMsg = params.get("ReservedMsg")
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.RequestId = params.get("RequestId")


class CheckAcctRequest(AbstractModel):
    """CheckAcct請求參數結構體

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param SubAppId: 聚鑫計費SubAppId，代表子商戶
        :type SubAppId: str
        :param BindType: 1：小額鑒權
2：簡訊校驗鑒權
        :type BindType: int
        :param SettleAcctNo: 結算帳戶賬号
<敏感訊息>加密詳見《商戶端介面敏感訊息加密說明》
        :type SettleAcctNo: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全金鑰計算的簽名
        :type MidasSignature: str
        :param CheckCode: 簡訊驗證碼
BindType==2必填
        :type CheckCode: str
        :param CurrencyType: 币種 RMB
BindType==1必填
        :type CurrencyType: str
        :param CurrencyUnit: 單位
1：元，2：角，3：分
BindType==1必填
        :type CurrencyUnit: int
        :param CurrencyAmt: 金額
BindType==1必填
        :type CurrencyAmt: str
        """
        self.MidasAppId = None
        self.SubAppId = None
        self.BindType = None
        self.SettleAcctNo = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.CheckCode = None
        self.CurrencyType = None
        self.CurrencyUnit = None
        self.CurrencyAmt = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.BindType = params.get("BindType")
        self.SettleAcctNo = params.get("SettleAcctNo")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.CheckCode = params.get("CheckCode")
        self.CurrencyType = params.get("CurrencyType")
        self.CurrencyUnit = params.get("CurrencyUnit")
        self.CurrencyAmt = params.get("CurrencyAmt")


class CheckAcctResponse(AbstractModel):
    """CheckAcct返回參數結構體

    """

    def __init__(self):
        """
        :param FrontSeqNo: 前置流水号，請保存
        :type FrontSeqNo: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FrontSeqNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.RequestId = params.get("RequestId")


class CheckAmountRequest(AbstractModel):
    """CheckAmount請求參數結構體

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商戶号（簽約客戶号）
        :type MrchCode: str
        :param TranNetMemberCode: STRING(32)，交易網會員代碼（若需要把一個待綁定帳戶關聯到兩個會員名下，此欄位可上送兩個會員的交易網代碼，并且須用“|::|”(右側)進行分隔）
        :type TranNetMemberCode: str
        :param TakeCashAcctNo: STRING(50)，會員的待綁定帳戶的賬号（即 BindRelateAcctSmallAmount介面中的“會員的待綁定帳戶的賬号”）
        :type TakeCashAcctNo: str
        :param AuthAmt: STRING(20)，鑒權驗證金額（即 BindRelateAcctSmallAmount介面中的“會員的待綁定帳戶收到的驗證金額。原小額轉賬鑒權方式爲來賬鑒權的情況下此欄位須賦值爲0.00）
        :type AuthAmt: str
        :param Ccy: STRING(3)，币種（預設爲RMB）
        :type Ccy: str
        :param ReservedMsg: STRING(1027)，原小額轉賬方式（1: 往賬鑒權，此爲預設值; 2: 來賬鑒權）
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.TranNetMemberCode = None
        self.TakeCashAcctNo = None
        self.AuthAmt = None
        self.Ccy = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.TakeCashAcctNo = params.get("TakeCashAcctNo")
        self.AuthAmt = params.get("AuthAmt")
        self.Ccy = params.get("Ccy")
        self.ReservedMsg = params.get("ReservedMsg")


class CheckAmountResponse(AbstractModel):
    """CheckAmount返回參數結構體

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回碼
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回訊息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，見證系統流水号（即電商見證寶系統生成的流水号，可關聯具體一筆請求）
        :type FrontSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class ClearItem(AbstractModel):
    """銀行在途清算結果訊息

    """

    def __init__(self):
        """
        :param Date: STRING(8)，日期（格式: 20190101）
注意：此欄位可能返回 null，表示取不到有效值。
        :type Date: str
        :param SubAcctType: STRING(40)，子賬号類型（子帳号類型。1: 普通會員子賬号; 2: 挂賬子賬号; 3: 手續約子賬号; 4: 利息子賬号; 5: 平台擔保子賬号; 7: 在途; 8: 理财購買子帳号; 9: 理财贖回子帳号; 10: 平台子擁有結算子帳号）
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubAcctType: str
        :param ReconcileStatus: STRING(3)，對賬狀态（0: 成功; 1: 失敗）
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReconcileStatus: str
        :param ReconcileReturnMsg: STRING(300)，對賬返回訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReconcileReturnMsg: str
        :param ClearingStatus: STRING(20)，清算狀态（0: 成功; 1: 失敗; 2: 異常; 3: 待處理）
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClearingStatus: str
        :param ClearingReturnMsg: STRING(2)，清算返回訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClearingReturnMsg: str
        :param TotalAmt: STRING(300)，待清算總金額
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalAmt: str
        """
        self.Date = None
        self.SubAcctType = None
        self.ReconcileStatus = None
        self.ReconcileReturnMsg = None
        self.ClearingStatus = None
        self.ClearingReturnMsg = None
        self.TotalAmt = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.SubAcctType = params.get("SubAcctType")
        self.ReconcileStatus = params.get("ReconcileStatus")
        self.ReconcileReturnMsg = params.get("ReconcileReturnMsg")
        self.ClearingStatus = params.get("ClearingStatus")
        self.ClearingReturnMsg = params.get("ClearingReturnMsg")
        self.TotalAmt = params.get("TotalAmt")


class CloseOrderRequest(AbstractModel):
    """CloseOrder請求參數結構體

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param UserId: 用戶ID，長度不小於5位， 僅支援字母和數字的組合
        :type UserId: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全金鑰計算的簽名
        :type MidasSignature: str
        :param OutTradeNo: 業務訂單号，OutTradeNo ， TransactionId二選一，不能都爲空,優先使用 OutTradeNo
        :type OutTradeNo: str
        :param TransactionId: 聚鑫訂單号，OutTradeNo ， TransactionId二選一，不能都爲空,優先使用 OutTradeNo
        :type TransactionId: str
        """
        self.MidasAppId = None
        self.UserId = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.OutTradeNo = None
        self.TransactionId = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.UserId = params.get("UserId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.OutTradeNo = params.get("OutTradeNo")
        self.TransactionId = params.get("TransactionId")


class CloseOrderResponse(AbstractModel):
    """CloseOrder返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAcctRequest(AbstractModel):
    """CreateAcct請求參數結構體

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫平台分配的支付MidasAppId
        :type MidasAppId: str
        :param SubMchId: 業務平台的子商戶ID，唯一
        :type SubMchId: str
        :param SubMchName: 子商戶名稱
        :type SubMchName: str
        :param Address: 子商戶網址
        :type Address: str
        :param Contact: 子商戶聯系人
<敏感訊息>加密詳見《商戶端介面敏感訊息加密說明》
        :type Contact: str
        :param Mobile: 聯系人手機号
<敏感訊息>加密詳見《商戶端介面敏感訊息加密說明》
        :type Mobile: str
        :param Email: 電子信箱 
<敏感訊息>加密詳見《商戶端介面敏感訊息加密說明》
        :type Email: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全金鑰計算的簽名
        :type MidasSignature: str
        :param SubMchType: 子商戶類型：
個人: personal
企業：enterprise
缺省： enterprise
        :type SubMchType: str
        :param ShortName: 不填則預設子商戶名稱
        :type ShortName: str
        :param SubMerchantMemberType: 子商戶會員類型：
general:普通子帳戶
merchant:商戶子帳戶
缺省： general
        :type SubMerchantMemberType: str
        """
        self.MidasAppId = None
        self.SubMchId = None
        self.SubMchName = None
        self.Address = None
        self.Contact = None
        self.Mobile = None
        self.Email = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.SubMchType = None
        self.ShortName = None
        self.SubMerchantMemberType = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubMchId = params.get("SubMchId")
        self.SubMchName = params.get("SubMchName")
        self.Address = params.get("Address")
        self.Contact = params.get("Contact")
        self.Mobile = params.get("Mobile")
        self.Email = params.get("Email")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.SubMchType = params.get("SubMchType")
        self.ShortName = params.get("ShortName")
        self.SubMerchantMemberType = params.get("SubMerchantMemberType")


class CreateAcctResponse(AbstractModel):
    """CreateAcct返回參數結構體

    """

    def __init__(self):
        """
        :param SubAppId: 聚鑫計費SubAppId，代表子商戶
        :type SubAppId: str
        :param SubAcctNo: 平安銀行生成的子商戶帳戶
        :type SubAcctNo: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SubAppId = None
        self.SubAcctNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubAppId = params.get("SubAppId")
        self.SubAcctNo = params.get("SubAcctNo")
        self.RequestId = params.get("RequestId")


class CreateCustAcctIdRequest(AbstractModel):
    """CreateCustAcctId請求參數結構體

    """

    def __init__(self):
        """
        :param FunctionFlag: STRING(2)，功能标志（1: 開戶; 3: 銷戶）
        :type FunctionFlag: str
        :param FundSummaryAcctNo: STRING(50)，資金匯總賬号（即收單資金歸集入賬的賬号）
        :type FundSummaryAcctNo: str
        :param TranNetMemberCode: STRING(32)，交易網會員代碼（平台端的用戶ID，需要保證唯一性，可數字字母混合，如HY_120）
        :type TranNetMemberCode: str
        :param MemberProperty: STRING(10)，會員屬性（00-普通子帳戶(預設); SH-商戶子帳戶）
        :type MemberProperty: str
        :param Mobile: STRING(30)，手機号碼
        :type Mobile: str
        :param MrchCode: String(22)，商戶号（簽約客戶号）
        :type MrchCode: str
        :param SelfBusiness: String(2)，是否爲自營業務（0位非自營，1爲自營）
        :type SelfBusiness: bool
        :param ContactName: String(64)，聯系人
        :type ContactName: str
        :param SubAcctName: String(64)，子帳戶名稱
        :type SubAcctName: str
        :param SubAcctShortName: String(64)，子帳戶簡稱
        :type SubAcctShortName: str
        :param SubAcctType: String(4)，子帳戶類型（0: 個人子帳戶; 1: 企業子帳戶）
        :type SubAcctType: int
        :param UserNickname: STRING(150)，用戶昵稱
        :type UserNickname: str
        :param Email: STRING(150)，電子信箱
        :type Email: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.FunctionFlag = None
        self.FundSummaryAcctNo = None
        self.TranNetMemberCode = None
        self.MemberProperty = None
        self.Mobile = None
        self.MrchCode = None
        self.SelfBusiness = None
        self.ContactName = None
        self.SubAcctName = None
        self.SubAcctShortName = None
        self.SubAcctType = None
        self.UserNickname = None
        self.Email = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.FunctionFlag = params.get("FunctionFlag")
        self.FundSummaryAcctNo = params.get("FundSummaryAcctNo")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberProperty = params.get("MemberProperty")
        self.Mobile = params.get("Mobile")
        self.MrchCode = params.get("MrchCode")
        self.SelfBusiness = params.get("SelfBusiness")
        self.ContactName = params.get("ContactName")
        self.SubAcctName = params.get("SubAcctName")
        self.SubAcctShortName = params.get("SubAcctShortName")
        self.SubAcctType = params.get("SubAcctType")
        self.UserNickname = params.get("UserNickname")
        self.Email = params.get("Email")
        self.ReservedMsg = params.get("ReservedMsg")


class CreateCustAcctIdResponse(AbstractModel):
    """CreateCustAcctId返回參數結構體

    """

    def __init__(self):
        """
        :param SubAcctNo: STRING(50)，見證子帳戶的賬号（平台需要記錄下來，後續所有介面交互都會用到）
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubAcctNo: str
        :param ReservedMsg: STRING(1027)，保留域（需要開通智慧收款，此處返回智慧收款賬号，正常情況下返回空）
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param TxnReturnCode: String(20)，返回碼
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回訊息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SubAcctNo = None
        self.ReservedMsg = None
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubAcctNo = params.get("SubAcctNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.RequestId = params.get("RequestId")


class CreateInvoiceItem(AbstractModel):
    """發票開具明細

    """

    def __init__(self):
        """
        :param Name: 商品名稱
        :type Name: str
        :param TaxCode: 稅收商品編碼
        :type TaxCode: str
        :param TotalPrice: 不含稅商品總價（商品含稅價總額/（1+稅率））。單位爲分
        :type TotalPrice: int
        :param TaxRate: 商品稅率
        :type TaxRate: int
        :param TaxAmount: 商品稅額（不含稅商品總價*稅率）。單位爲分
        :type TaxAmount: int
        :param TaxType: 稅收商品類别
        :type TaxType: str
        :param Models: 商品規格
        :type Models: str
        :param Unit: 商品單位
        :type Unit: str
        :param Total: 商品數量
        :type Total: str
        :param Price: 不含稅商品單價
        :type Price: str
        :param Discount: 含稅折扣總額。單位爲分
        :type Discount: int
        :param PreferentialPolicyFlag: 優惠政策标志。0：不使用優惠政策；1：使用優惠政策。
        :type PreferentialPolicyFlag: str
        :param ZeroTaxFlag: 零稅率标識：
空：非零稅率；
0：出口零稅率；
1：免稅；
2：不征稅；
3：普通零稅率。
        :type ZeroTaxFlag: str
        :param VatSpecialManagement: 增值稅特殊管理。PreferentialPolicyFlag欄位爲1時，必填。目前僅支援5%(3%，2%，1.5%)簡易征稅、免稅、不征稅。
        :type VatSpecialManagement: str
        """
        self.Name = None
        self.TaxCode = None
        self.TotalPrice = None
        self.TaxRate = None
        self.TaxAmount = None
        self.TaxType = None
        self.Models = None
        self.Unit = None
        self.Total = None
        self.Price = None
        self.Discount = None
        self.PreferentialPolicyFlag = None
        self.ZeroTaxFlag = None
        self.VatSpecialManagement = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.TaxCode = params.get("TaxCode")
        self.TotalPrice = params.get("TotalPrice")
        self.TaxRate = params.get("TaxRate")
        self.TaxAmount = params.get("TaxAmount")
        self.TaxType = params.get("TaxType")
        self.Models = params.get("Models")
        self.Unit = params.get("Unit")
        self.Total = params.get("Total")
        self.Price = params.get("Price")
        self.Discount = params.get("Discount")
        self.PreferentialPolicyFlag = params.get("PreferentialPolicyFlag")
        self.ZeroTaxFlag = params.get("ZeroTaxFlag")
        self.VatSpecialManagement = params.get("VatSpecialManagement")


class CreateInvoiceRequest(AbstractModel):
    """CreateInvoice請求參數結構體

    """

    def __init__(self):
        """
        :param InvoicePlatformId: 開票平台ID。0：高燈
        :type InvoicePlatformId: int
        :param TitleType: 擡頭類型：1：個人/政府事業單位；2：企業
        :type TitleType: int
        :param BuyerTitle: 購方名稱
        :type BuyerTitle: str
        :param OrderId: 業務開票号
        :type OrderId: str
        :param AmountHasTax: 含稅總金額（單位爲分）
        :type AmountHasTax: int
        :param TaxAmount: 總稅額（單位爲分）
        :type TaxAmount: int
        :param AmountWithoutTax: 不含稅總金額（單位爲分）
        :type AmountWithoutTax: int
        :param SellerTaxpayerNum: 銷方納稅人識别号
        :type SellerTaxpayerNum: str
        :param SellerName: 銷方名稱。（不填預設讀取商戶注冊時輸入的訊息）
        :type SellerName: str
        :param SellerAddress: 銷方網址。（不填預設讀取商戶注冊時輸入的訊息）
        :type SellerAddress: str
        :param SellerPhone: 銷方電話。（不填預設讀取商戶注冊時輸入的訊息）
        :type SellerPhone: str
        :param SellerBankName: 銷方銀行名稱。（不填預設讀取商戶注冊時輸入的訊息）
        :type SellerBankName: str
        :param SellerBankAccount: 銷方銀行賬号。（不填預設讀取商戶注冊時輸入的訊息）
        :type SellerBankAccount: str
        :param BuyerTaxpayerNum: 購方納稅人識别号（購方票面訊息）,若擡頭類型爲2時，必傳
        :type BuyerTaxpayerNum: str
        :param BuyerAddress: 購方網址。開具專用發票時必填
        :type BuyerAddress: str
        :param BuyerBankName: 購方銀行名稱。開具專用發票時必填
        :type BuyerBankName: str
        :param BuyerBankAccount: 購方銀行賬号。開具專用發票時必填
        :type BuyerBankAccount: str
        :param BuyerPhone: 購方電話。開具專用發票時必填
        :type BuyerPhone: str
        :param BuyerEmail: 收票人電子信箱。若填入，會收到發票推送郵件
        :type BuyerEmail: str
        :param TakerPhone: 收票人手機号。若填入，會收到發票推送簡訊
        :type TakerPhone: str
        :param InvoiceType: 開票類型：
1：增值稅專用發票；
2：增值稅普通發票；
3：增值稅電子發票；
4：增值稅卷式發票；
5：區塊鏈電子發票。
若該欄位不填，或值不爲1-5，則認爲開具”增值稅電子發票”
        :type InvoiceType: int
        :param CallbackUrl: 發票結果回傳網址
        :type CallbackUrl: str
        :param Drawer: 開票人姓名。（不填預設讀取商戶注冊時輸入的訊息）
        :type Drawer: str
        :param Payee: 收款人姓名。（不填預設讀取商戶注冊時輸入的訊息）
        :type Payee: str
        :param Checker: 複核人姓名。（不填預設讀取商戶注冊時輸入的訊息）
        :type Checker: str
        :param TerminalCode: 稅盤号
        :type TerminalCode: str
        :param LevyMethod: 征收方式。開具差額征稅發票時必填2。開具普通征稅發票時爲空
        :type LevyMethod: str
        :param Deduction: 差額征稅扣除額（單位爲分）
        :type Deduction: int
        :param Remark: 備注（票面訊息）
        :type Remark: str
        :param Items: 項目商品明細
        :type Items: list of CreateInvoiceItem
        :param Profile: 接入環境。沙箱環境填sandbox。
        :type Profile: str
        """
        self.InvoicePlatformId = None
        self.TitleType = None
        self.BuyerTitle = None
        self.OrderId = None
        self.AmountHasTax = None
        self.TaxAmount = None
        self.AmountWithoutTax = None
        self.SellerTaxpayerNum = None
        self.SellerName = None
        self.SellerAddress = None
        self.SellerPhone = None
        self.SellerBankName = None
        self.SellerBankAccount = None
        self.BuyerTaxpayerNum = None
        self.BuyerAddress = None
        self.BuyerBankName = None
        self.BuyerBankAccount = None
        self.BuyerPhone = None
        self.BuyerEmail = None
        self.TakerPhone = None
        self.InvoiceType = None
        self.CallbackUrl = None
        self.Drawer = None
        self.Payee = None
        self.Checker = None
        self.TerminalCode = None
        self.LevyMethod = None
        self.Deduction = None
        self.Remark = None
        self.Items = None
        self.Profile = None


    def _deserialize(self, params):
        self.InvoicePlatformId = params.get("InvoicePlatformId")
        self.TitleType = params.get("TitleType")
        self.BuyerTitle = params.get("BuyerTitle")
        self.OrderId = params.get("OrderId")
        self.AmountHasTax = params.get("AmountHasTax")
        self.TaxAmount = params.get("TaxAmount")
        self.AmountWithoutTax = params.get("AmountWithoutTax")
        self.SellerTaxpayerNum = params.get("SellerTaxpayerNum")
        self.SellerName = params.get("SellerName")
        self.SellerAddress = params.get("SellerAddress")
        self.SellerPhone = params.get("SellerPhone")
        self.SellerBankName = params.get("SellerBankName")
        self.SellerBankAccount = params.get("SellerBankAccount")
        self.BuyerTaxpayerNum = params.get("BuyerTaxpayerNum")
        self.BuyerAddress = params.get("BuyerAddress")
        self.BuyerBankName = params.get("BuyerBankName")
        self.BuyerBankAccount = params.get("BuyerBankAccount")
        self.BuyerPhone = params.get("BuyerPhone")
        self.BuyerEmail = params.get("BuyerEmail")
        self.TakerPhone = params.get("TakerPhone")
        self.InvoiceType = params.get("InvoiceType")
        self.CallbackUrl = params.get("CallbackUrl")
        self.Drawer = params.get("Drawer")
        self.Payee = params.get("Payee")
        self.Checker = params.get("Checker")
        self.TerminalCode = params.get("TerminalCode")
        self.LevyMethod = params.get("LevyMethod")
        self.Deduction = params.get("Deduction")
        self.Remark = params.get("Remark")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = CreateInvoiceItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.Profile = params.get("Profile")


class CreateInvoiceResponse(AbstractModel):
    """CreateInvoice返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 發票開具結果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateInvoiceResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateInvoiceResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateInvoiceResult(AbstractModel):
    """發票結果

    """

    def __init__(self):
        """
        :param Message: 錯誤訊息
        :type Message: str
        :param Code: 錯誤碼
        :type Code: int
        :param Data: 數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.CreateInvoiceResultData`
        """
        self.Message = None
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Message = params.get("Message")
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = CreateInvoiceResultData()
            self.Data._deserialize(params.get("Data"))


class CreateInvoiceResultData(AbstractModel):
    """藍票結果數據

    """

    def __init__(self):
        """
        :param State: 開票狀态
        :type State: int
        :param InvoiceId: 發票ID
        :type InvoiceId: str
        :param OrderSn: 業務開票号
        :type OrderSn: str
        """
        self.State = None
        self.InvoiceId = None
        self.OrderSn = None


    def _deserialize(self, params):
        self.State = params.get("State")
        self.InvoiceId = params.get("InvoiceId")
        self.OrderSn = params.get("OrderSn")


class CreateMerchantRequest(AbstractModel):
    """CreateMerchant請求參數結構體

    """

    def __init__(self):
        """
        :param InvoicePlatformId: 開票平台ID
        :type InvoicePlatformId: int
        :param TaxpayerName: 企業名稱
        :type TaxpayerName: str
        :param TaxpayerNum: 銷方納稅人識别号
        :type TaxpayerNum: str
        :param LegalPersonName: 注冊企業法定代表人名稱
        :type LegalPersonName: str
        :param ContactsName: 聯系人
        :type ContactsName: str
        :param Phone: 聯系人手機号
        :type Phone: str
        :param Address: 不包含省市名稱的網址
        :type Address: str
        :param RegionCode: 地區編碼
        :type RegionCode: int
        :param CityName: 市（地區）名稱
        :type CityName: str
        :param Drawer: 開票人
        :type Drawer: str
        :param TaxRegistrationCertificate: 稅務登記證圖片（Base64）字串，需小於 3M
        :type TaxRegistrationCertificate: str
        :param Email: 聯系人電子信箱網址
        :type Email: str
        :param BusinessMobile: 企業電話
        :type BusinessMobile: str
        :param BankName: 銀行名稱
        :type BankName: str
        :param BankAccount: 銀行賬号
        :type BankAccount: str
        :param Reviewer: 複核人
        :type Reviewer: str
        :param Payee: 收款人
        :type Payee: str
        :param RegisterCode: 注冊邀請碼
        :type RegisterCode: str
        :param State: 不填預設爲1，有效狀态
0：表示無效；
1:表示有效；
2:表示禁止開藍票；
3:表示禁止沖紅。
        :type State: str
        :param CallbackUrl: 接收推送的訊息網址
        :type CallbackUrl: str
        :param Profile: 接入環境。沙箱環境填 sandbox。
        :type Profile: str
        """
        self.InvoicePlatformId = None
        self.TaxpayerName = None
        self.TaxpayerNum = None
        self.LegalPersonName = None
        self.ContactsName = None
        self.Phone = None
        self.Address = None
        self.RegionCode = None
        self.CityName = None
        self.Drawer = None
        self.TaxRegistrationCertificate = None
        self.Email = None
        self.BusinessMobile = None
        self.BankName = None
        self.BankAccount = None
        self.Reviewer = None
        self.Payee = None
        self.RegisterCode = None
        self.State = None
        self.CallbackUrl = None
        self.Profile = None


    def _deserialize(self, params):
        self.InvoicePlatformId = params.get("InvoicePlatformId")
        self.TaxpayerName = params.get("TaxpayerName")
        self.TaxpayerNum = params.get("TaxpayerNum")
        self.LegalPersonName = params.get("LegalPersonName")
        self.ContactsName = params.get("ContactsName")
        self.Phone = params.get("Phone")
        self.Address = params.get("Address")
        self.RegionCode = params.get("RegionCode")
        self.CityName = params.get("CityName")
        self.Drawer = params.get("Drawer")
        self.TaxRegistrationCertificate = params.get("TaxRegistrationCertificate")
        self.Email = params.get("Email")
        self.BusinessMobile = params.get("BusinessMobile")
        self.BankName = params.get("BankName")
        self.BankAccount = params.get("BankAccount")
        self.Reviewer = params.get("Reviewer")
        self.Payee = params.get("Payee")
        self.RegisterCode = params.get("RegisterCode")
        self.State = params.get("State")
        self.CallbackUrl = params.get("CallbackUrl")
        self.Profile = params.get("Profile")


class CreateMerchantResponse(AbstractModel):
    """CreateMerchant返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 商戶注冊結果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateMerchantResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateMerchantResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateMerchantResult(AbstractModel):
    """創建商戶結果

    """

    def __init__(self):
        """
        :param Code: 狀态碼
        :type Code: int
        :param Message: 響應訊息
        :type Message: str
        :param Data: 創建商戶結果數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.CreateMerchantResultData`
        """
        self.Code = None
        self.Message = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        if params.get("Data") is not None:
            self.Data = CreateMerchantResultData()
            self.Data._deserialize(params.get("Data"))


class CreateMerchantResultData(AbstractModel):
    """創建商戶結果數據

    """

    def __init__(self):
        """
        :param TaxpayerName: 企業名稱
        :type TaxpayerName: str
        :param SerialNo: 請求流水号
        :type SerialNo: str
        :param TaxpayerNum: 納稅号
        :type TaxpayerNum: str
        """
        self.TaxpayerName = None
        self.SerialNo = None
        self.TaxpayerNum = None


    def _deserialize(self, params):
        self.TaxpayerName = params.get("TaxpayerName")
        self.SerialNo = params.get("SerialNo")
        self.TaxpayerNum = params.get("TaxpayerNum")


class CreateRedInvoiceItem(AbstractModel):
    """創建紅票明細

    """

    def __init__(self):
        """
        :param OrderId: 訂單号
        :type OrderId: str
        :param CallbackUrl: 發票結果回傳網址
        :type CallbackUrl: str
        :param OrderSn: 業務開票号
        :type OrderSn: str
        :param RedSerialNo: 紅字訊息表編碼
        :type RedSerialNo: str
        """
        self.OrderId = None
        self.CallbackUrl = None
        self.OrderSn = None
        self.RedSerialNo = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.CallbackUrl = params.get("CallbackUrl")
        self.OrderSn = params.get("OrderSn")
        self.RedSerialNo = params.get("RedSerialNo")


class CreateRedInvoiceRequest(AbstractModel):
    """CreateRedInvoice請求參數結構體

    """

    def __init__(self):
        """
        :param InvoicePlatformId: 開票平台ID
        :type InvoicePlatformId: int
        :param Invoices: 紅沖明細
        :type Invoices: list of CreateRedInvoiceItem
        :param Profile: 接入環境。沙箱環境填 sandbox。
        :type Profile: str
        """
        self.InvoicePlatformId = None
        self.Invoices = None
        self.Profile = None


    def _deserialize(self, params):
        self.InvoicePlatformId = params.get("InvoicePlatformId")
        if params.get("Invoices") is not None:
            self.Invoices = []
            for item in params.get("Invoices"):
                obj = CreateRedInvoiceItem()
                obj._deserialize(item)
                self.Invoices.append(obj)
        self.Profile = params.get("Profile")


class CreateRedInvoiceResponse(AbstractModel):
    """CreateRedInvoice返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 紅沖結果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.CreateRedInvoiceResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateRedInvoiceResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateRedInvoiceResult(AbstractModel):
    """紅票結果

    """

    def __init__(self):
        """
        :param Message: 錯誤訊息
        :type Message: str
        :param Code: 錯誤碼
        :type Code: int
        :param Data: 紅票數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: list of CreateRedInvoiceResultData
        """
        self.Message = None
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Message = params.get("Message")
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = CreateRedInvoiceResultData()
                obj._deserialize(item)
                self.Data.append(obj)


class CreateRedInvoiceResultData(AbstractModel):
    """紅票結果數據

    """

    def __init__(self):
        """
        :param Code: 紅沖狀态碼
        :type Code: int
        :param Message: 紅沖狀态訊息
        :type Message: str
        :param InvoiceId: 發票ID
        :type InvoiceId: str
        :param OrderSn: 業務開票号
        :type OrderSn: str
        """
        self.Code = None
        self.Message = None
        self.InvoiceId = None
        self.OrderSn = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        self.InvoiceId = params.get("InvoiceId")
        self.OrderSn = params.get("OrderSn")


class DownloadBillRequest(AbstractModel):
    """DownloadBill請求參數結構體

    """

    def __init__(self):
        """
        :param StateDate: 請求下載對帳單日期
        :type StateDate: str
        :param MidasAppId: 聚鑫分配的MidasAppId
        :type MidasAppId: str
        :param MidasSecretId: 聚鑫分配的SecretId
        :type MidasSecretId: str
        :param MidasSignature: 使用聚鑫安全金鑰計算的簽名
        :type MidasSignature: str
        """
        self.StateDate = None
        self.MidasAppId = None
        self.MidasSecretId = None
        self.MidasSignature = None


    def _deserialize(self, params):
        self.StateDate = params.get("StateDate")
        self.MidasAppId = params.get("MidasAppId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")


class DownloadBillResponse(AbstractModel):
    """DownloadBill返回參數結構體

    """

    def __init__(self):
        """
        :param FileName: 帳單文件名
        :type FileName: str
        :param FileMD5: 帳單文件的MD5值
        :type FileMD5: str
        :param DownloadUrl: 帳單文件的真實下載網址
        :type DownloadUrl: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FileName = None
        self.FileMD5 = None
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.FileMD5 = params.get("FileMD5")
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class FileItem(AbstractModel):
    """對賬文件訊息

    """

    def __init__(self):
        """
        :param FileName: STRING(256)，文件名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileName: str
        :param RandomPassword: STRING(120)，随機密碼
注意：此欄位可能返回 null，表示取不到有效值。
        :type RandomPassword: str
        :param FilePath: STRING(512)，文件路徑
注意：此欄位可能返回 null，表示取不到有效值。
        :type FilePath: str
        :param DrawCode: STRING(64)，提取碼
注意：此欄位可能返回 null，表示取不到有效值。
        :type DrawCode: str
        """
        self.FileName = None
        self.RandomPassword = None
        self.FilePath = None
        self.DrawCode = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.RandomPassword = params.get("RandomPassword")
        self.FilePath = params.get("FilePath")
        self.DrawCode = params.get("DrawCode")


class ModifyMntMbrBindRelateAcctBankCodeRequest(AbstractModel):
    """ModifyMntMbrBindRelateAcctBankCode請求參數結構體

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商戶号（簽約客戶号）
        :type MrchCode: str
        :param SubAcctNo: STRING(50)，見證子帳戶的賬号
        :type SubAcctNo: str
        :param MemberBindAcctNo: STRING(50)，會員綁定賬号
        :type MemberBindAcctNo: str
        :param AcctOpenBranchName: STRING(150)，開戶行名稱（若大小額行号不填則送超級網銀号對應的銀行名稱，若填大小額行号則送大小額行号對應的銀行名稱）
        :type AcctOpenBranchName: str
        :param CnapsBranchId: STRING(20)，大小額行号（CnapsBranchId和EiconBankBranchId兩者二選一必填）
        :type CnapsBranchId: str
        :param EiconBankBranchId: STRING(20)，超級網銀行号
        :type EiconBankBranchId: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.SubAcctNo = None
        self.MemberBindAcctNo = None
        self.AcctOpenBranchName = None
        self.CnapsBranchId = None
        self.EiconBankBranchId = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.SubAcctNo = params.get("SubAcctNo")
        self.MemberBindAcctNo = params.get("MemberBindAcctNo")
        self.AcctOpenBranchName = params.get("AcctOpenBranchName")
        self.CnapsBranchId = params.get("CnapsBranchId")
        self.EiconBankBranchId = params.get("EiconBankBranchId")
        self.ReservedMsg = params.get("ReservedMsg")


class ModifyMntMbrBindRelateAcctBankCodeResponse(AbstractModel):
    """ModifyMntMbrBindRelateAcctBankCode返回參數結構體

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回碼
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回訊息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryAcctBindingRequest(AbstractModel):
    """QueryAcctBinding請求參數結構體

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param SubAppId: 聚鑫計費SubAppId，代表子商戶
        :type SubAppId: str
        :param MidasSecretId: 由平台客服提供的計費金鑰Id
        :type MidasSecretId: str
        :param MidasSignature: 計費簽名
        :type MidasSignature: str
        """
        self.MidasAppId = None
        self.SubAppId = None
        self.MidasSecretId = None
        self.MidasSignature = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")


class QueryAcctBindingResponse(AbstractModel):
    """QueryAcctBinding返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 總行數
        :type TotalCount: int
        :param BankCardItems: 銀行卡訊息清單
        :type BankCardItems: list of BankCardItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.BankCardItems = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BankCardItems") is not None:
            self.BankCardItems = []
            for item in params.get("BankCardItems"):
                obj = BankCardItem()
                obj._deserialize(item)
                self.BankCardItems.append(obj)
        self.RequestId = params.get("RequestId")


class QueryAcctInfoListRequest(AbstractModel):
    """QueryAcctInfoList請求參數結構體

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param QueryAcctBeginTime: 查詢開始時間(以開戶時間爲準)
        :type QueryAcctBeginTime: str
        :param QueryAcctEndTime: 查詢結束時間(以開戶時間爲準)
        :type QueryAcctEndTime: str
        :param PageOffset: 分頁号,  起始值爲1，每次最多返回20條記錄，第二頁返回的記錄數爲第21至40條記錄，第三頁爲41至60條記錄，順序均按照開戶時間的先後
        :type PageOffset: str
        :param MidasSecretId: 由平台客服提供的計費金鑰Id
        :type MidasSecretId: str
        :param MidasSignature: 計費簽名
        :type MidasSignature: str
        """
        self.MidasAppId = None
        self.QueryAcctBeginTime = None
        self.QueryAcctEndTime = None
        self.PageOffset = None
        self.MidasSecretId = None
        self.MidasSignature = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.QueryAcctBeginTime = params.get("QueryAcctBeginTime")
        self.QueryAcctEndTime = params.get("QueryAcctEndTime")
        self.PageOffset = params.get("PageOffset")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")


class QueryAcctInfoListResponse(AbstractModel):
    """QueryAcctInfoList返回參數結構體

    """

    def __init__(self):
        """
        :param ResultCount: 本次交易返回查詢結果記錄數
        :type ResultCount: int
        :param TotalCount: 符合業務查詢條件的記錄總數
        :type TotalCount: int
        :param QueryAcctItems: 查詢結果項 [object,object]
        :type QueryAcctItems: list of QueryAcctItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ResultCount = None
        self.TotalCount = None
        self.QueryAcctItems = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultCount = params.get("ResultCount")
        self.TotalCount = params.get("TotalCount")
        if params.get("QueryAcctItems") is not None:
            self.QueryAcctItems = []
            for item in params.get("QueryAcctItems"):
                obj = QueryAcctItem()
                obj._deserialize(item)
                self.QueryAcctItems.append(obj)
        self.RequestId = params.get("RequestId")


class QueryAcctInfoRequest(AbstractModel):
    """QueryAcctInfo請求參數結構體

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫平台分配的支付MidasAppId
        :type MidasAppId: str
        :param SubMchId: 業務平台的子商戶Id，唯一
        :type SubMchId: str
        :param MidasSecretId: 由平台客服提供的計費金鑰Id
        :type MidasSecretId: str
        :param MidasSignature: 計費簽名
        :type MidasSignature: str
        """
        self.MidasAppId = None
        self.SubMchId = None
        self.MidasSecretId = None
        self.MidasSignature = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubMchId = params.get("SubMchId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")


class QueryAcctInfoResponse(AbstractModel):
    """QueryAcctInfo返回參數結構體

    """

    def __init__(self):
        """
        :param SubAppId: 聚鑫計費SubAppId，代表子商戶
        :type SubAppId: str
        :param SubMchName: 子商戶名稱
        :type SubMchName: str
        :param SubMchType: 子商戶類型：
個人: personal
企業：enterprise
缺省： enterprise
        :type SubMchType: str
        :param ShortName: 不填則預設子商戶名稱
        :type ShortName: str
        :param Address: 子商戶網址
        :type Address: str
        :param Contact: 子商戶聯系人子商戶聯系人
<敏感訊息>
        :type Contact: str
        :param Mobile: 聯系人手機号
<敏感訊息>
        :type Mobile: str
        :param Email: 電子信箱 
<敏感訊息>
        :type Email: str
        :param SubMchId: 子商戶id
        :type SubMchId: str
        :param SubAcctNo: 子帳戶
        :type SubAcctNo: str
        :param SubMerchantMemberType: 子商戶會員類型：
general:普通子帳戶
merchant:商戶子帳戶
缺省： general
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubMerchantMemberType: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SubAppId = None
        self.SubMchName = None
        self.SubMchType = None
        self.ShortName = None
        self.Address = None
        self.Contact = None
        self.Mobile = None
        self.Email = None
        self.SubMchId = None
        self.SubAcctNo = None
        self.SubMerchantMemberType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubAppId = params.get("SubAppId")
        self.SubMchName = params.get("SubMchName")
        self.SubMchType = params.get("SubMchType")
        self.ShortName = params.get("ShortName")
        self.Address = params.get("Address")
        self.Contact = params.get("Contact")
        self.Mobile = params.get("Mobile")
        self.Email = params.get("Email")
        self.SubMchId = params.get("SubMchId")
        self.SubAcctNo = params.get("SubAcctNo")
        self.SubMerchantMemberType = params.get("SubMerchantMemberType")
        self.RequestId = params.get("RequestId")


class QueryAcctItem(AbstractModel):
    """查詢帳戶清單介面

    """

    def __init__(self):
        """
        :param SubMchType: 子商戶類型：
個人: personal
企業：enterprise
缺省： enterprise
        :type SubMchType: str
        :param SubMchName: 子商戶名稱
        :type SubMchName: str
        :param SubAcctNo: 子賬号号
        :type SubAcctNo: str
        :param ShortName: 不填則預設子商戶名稱
        :type ShortName: str
        :param SubMchId: 業務平台的子商戶Id，唯一
        :type SubMchId: str
        :param SubAppId: 聚鑫計費SubAppId，代表子商戶
        :type SubAppId: str
        :param Contact: 子商戶聯系人
<敏感訊息>
        :type Contact: str
        :param Address: 子商戶網址
        :type Address: str
        :param Mobile: 聯系人手機号
<敏感訊息>
        :type Mobile: str
        :param Email: 電子信箱 
<敏感訊息>
        :type Email: str
        :param SubMerchantMemberType: 子商戶會員類型：
general:普通子帳戶
merchant:商戶子帳戶
缺省： general
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubMerchantMemberType: str
        """
        self.SubMchType = None
        self.SubMchName = None
        self.SubAcctNo = None
        self.ShortName = None
        self.SubMchId = None
        self.SubAppId = None
        self.Contact = None
        self.Address = None
        self.Mobile = None
        self.Email = None
        self.SubMerchantMemberType = None


    def _deserialize(self, params):
        self.SubMchType = params.get("SubMchType")
        self.SubMchName = params.get("SubMchName")
        self.SubAcctNo = params.get("SubAcctNo")
        self.ShortName = params.get("ShortName")
        self.SubMchId = params.get("SubMchId")
        self.SubAppId = params.get("SubAppId")
        self.Contact = params.get("Contact")
        self.Address = params.get("Address")
        self.Mobile = params.get("Mobile")
        self.Email = params.get("Email")
        self.SubMerchantMemberType = params.get("SubMerchantMemberType")


class QueryApplicationMaterialRequest(AbstractModel):
    """QueryApplicationMaterial請求參數結構體

    """

    def __init__(self):
        """
        :param DeclareId: 申報流水号
        :type DeclareId: str
        :param Profile: 接入環境。沙箱環境填sandbox
        :type Profile: str
        """
        self.DeclareId = None
        self.Profile = None


    def _deserialize(self, params):
        self.DeclareId = params.get("DeclareId")
        self.Profile = params.get("Profile")


class QueryApplicationMaterialResponse(AbstractModel):
    """QueryApplicationMaterial返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 成功申報材料查詢結果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryDeclareResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = QueryDeclareResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryBalanceRequest(AbstractModel):
    """QueryBalance請求參數結構體

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param SubAppId: 聚鑫計費SubAppId，代表子商戶
        :type SubAppId: str
        :param QueryFlag: 2：普通會員子賬号
3：功能子賬号
        :type QueryFlag: str
        :param PageOffset: 起始值爲1，每次最多返回20條記錄，第二頁返回的記錄數爲第21至40條記錄，第三頁爲41至60條記錄，順序均按照建立時間的先後
        :type PageOffset: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全金鑰計算的簽名
        :type MidasSignature: str
        """
        self.MidasAppId = None
        self.SubAppId = None
        self.QueryFlag = None
        self.PageOffset = None
        self.MidasSecretId = None
        self.MidasSignature = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.QueryFlag = params.get("QueryFlag")
        self.PageOffset = params.get("PageOffset")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")


class QueryBalanceResponse(AbstractModel):
    """QueryBalance返回參數結構體

    """

    def __init__(self):
        """
        :param ResultCount: 本次交易返回查詢結果記錄數
        :type ResultCount: str
        :param StartRecordOffset: 起始記錄号
        :type StartRecordOffset: str
        :param EndFlag: 結束标志
        :type EndFlag: str
        :param TotalCount: 符合業務查詢條件的記錄總數
        :type TotalCount: str
        :param QueryItems: 查詢結果項
        :type QueryItems: list of QueryItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ResultCount = None
        self.StartRecordOffset = None
        self.EndFlag = None
        self.TotalCount = None
        self.QueryItems = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultCount = params.get("ResultCount")
        self.StartRecordOffset = params.get("StartRecordOffset")
        self.EndFlag = params.get("EndFlag")
        self.TotalCount = params.get("TotalCount")
        if params.get("QueryItems") is not None:
            self.QueryItems = []
            for item in params.get("QueryItems"):
                obj = QueryItem()
                obj._deserialize(item)
                self.QueryItems.append(obj)
        self.RequestId = params.get("RequestId")


class QueryBankClearRequest(AbstractModel):
    """QueryBankClear請求參數結構體

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商戶号（簽約客戶号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（1: 全部; 2: 指定時間段）
        :type FunctionFlag: str
        :param PageNum: STRING (10)，頁碼（起始值爲1，每次最多返回20條記錄，第二頁返回的記錄數爲第21至40條記錄，第三頁爲41至60條記錄，順序均按照建立時間的先後）
        :type PageNum: str
        :param StartDate: STRING(8)，開始日期（若是指定時間段查詢，則必輸，當查詢全部時，不起作用。格式: 20190101）
        :type StartDate: str
        :param EndDate: STRING(8)，終止日期（若是指定時間段查詢，則必輸，當查詢全部時，不起作用。格式：20190101）
        :type EndDate: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.PageNum = None
        self.StartDate = None
        self.EndDate = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.PageNum = params.get("PageNum")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.ReservedMsg = params.get("ReservedMsg")


class QueryBankClearResponse(AbstractModel):
    """QueryBankClear返回參數結構體

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回碼
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回訊息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ResultNum: STRING (10)，本次交易返回查詢結果記錄數
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param StartRecordNo: STRING(30)，起始記錄号
注意：此欄位可能返回 null，表示取不到有效值。
        :type StartRecordNo: str
        :param EndFlag: STRING(2)，結束标志（0: 否; 1: 是）
注意：此欄位可能返回 null，表示取不到有效值。
        :type EndFlag: str
        :param TotalNum: STRING (10)，符合業務查詢條件的記錄總數（重複次數, 一次最多返回20條記錄）
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalNum: str
        :param TranItemArray: 交易訊息數組
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranItemArray: list of ClearItem
        :param ReservedMsg: STRING(1027)，保留域
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ResultNum = None
        self.StartRecordNo = None
        self.EndFlag = None
        self.TotalNum = None
        self.TranItemArray = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ResultNum = params.get("ResultNum")
        self.StartRecordNo = params.get("StartRecordNo")
        self.EndFlag = params.get("EndFlag")
        self.TotalNum = params.get("TotalNum")
        if params.get("TranItemArray") is not None:
            self.TranItemArray = []
            for item in params.get("TranItemArray"):
                obj = ClearItem()
                obj._deserialize(item)
                self.TranItemArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryBankTransactionDetailsRequest(AbstractModel):
    """QueryBankTransactionDetails請求參數結構體

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商戶号（簽約客戶号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（1: 當日; 2: 曆史）
        :type FunctionFlag: str
        :param SubAcctNo: STRING(50)，見證子帳戶的帳号
        :type SubAcctNo: str
        :param QueryFlag: STRING(4)，查詢标志（1: 全部; 2: 轉出; 3: 轉入 ）
        :type QueryFlag: str
        :param PageNum: STRING(10)，頁碼（起始值爲1，每次最多返回20條記錄，第二頁返回的記錄數爲第21至40條記錄，第三頁爲41至60條記錄，順序均按照建立時間的先後）
        :type PageNum: str
        :param StartDate: STRING(8)，開始日期（若是曆史查詢，則必輸，當日查詢時，不起作用。格式：20190101）
        :type StartDate: str
        :param EndDate: STRING(8)，終止日期（若是曆史查詢，則必輸，當日查詢時，不起作用。格式：20190101）
        :type EndDate: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.SubAcctNo = None
        self.QueryFlag = None
        self.PageNum = None
        self.StartDate = None
        self.EndDate = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.SubAcctNo = params.get("SubAcctNo")
        self.QueryFlag = params.get("QueryFlag")
        self.PageNum = params.get("PageNum")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.ReservedMsg = params.get("ReservedMsg")


class QueryBankTransactionDetailsResponse(AbstractModel):
    """QueryBankTransactionDetails返回參數結構體

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回碼
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回訊息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ResultNum: STRING(10)，本次交易返回查詢結果記錄數
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param StartRecordNo: STRING(30)，起始記錄号
注意：此欄位可能返回 null，表示取不到有效值。
        :type StartRecordNo: str
        :param EndFlag: STRING(2)，結束标志（0: 否; 1: 是）
注意：此欄位可能返回 null，表示取不到有效值。
        :type EndFlag: str
        :param TotalNum: STRING(10)，符合業務查詢條件的記錄總數（重複次數，一次最多返回20條記錄）
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalNum: str
        :param TranItemArray: 交易訊息數組
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranItemArray: list of TransactionItem
        :param ReservedMsg: STRING(1027)，保留域
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ResultNum = None
        self.StartRecordNo = None
        self.EndFlag = None
        self.TotalNum = None
        self.TranItemArray = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ResultNum = params.get("ResultNum")
        self.StartRecordNo = params.get("StartRecordNo")
        self.EndFlag = params.get("EndFlag")
        self.TotalNum = params.get("TotalNum")
        if params.get("TranItemArray") is not None:
            self.TranItemArray = []
            for item in params.get("TranItemArray"):
                obj = TransactionItem()
                obj._deserialize(item)
                self.TranItemArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryBankWithdrawCashDetailsRequest(AbstractModel):
    """QueryBankWithdrawCashDetails請求參數結構體

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商戶号（簽約客戶号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（1: 當日; 2: 曆史）
        :type FunctionFlag: str
        :param SubAcctNo: STRING(50)，見證子帳戶的帳号
        :type SubAcctNo: str
        :param QueryFlag: STRING(4)，查詢标志（2: 提現; 3: 清分）
        :type QueryFlag: str
        :param PageNum: STRING(10)，頁碼（起始值爲1，每次最多返回20條記錄，第二頁返回的記錄數爲第21至40條記錄，第三頁爲41至60條記錄，順序均按照建立時間的先後）
        :type PageNum: str
        :param BeginDate: STRING(8)，開始日期（若是曆史查詢，則必輸，當日查詢時，不起作用。格式：20190101）
        :type BeginDate: str
        :param EndDate: STRING(8)，結束日期（若是曆史查詢，則必輸，當日查詢時，不起作用。格式：20190101）
        :type EndDate: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.SubAcctNo = None
        self.QueryFlag = None
        self.PageNum = None
        self.BeginDate = None
        self.EndDate = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.SubAcctNo = params.get("SubAcctNo")
        self.QueryFlag = params.get("QueryFlag")
        self.PageNum = params.get("PageNum")
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")
        self.ReservedMsg = params.get("ReservedMsg")


class QueryBankWithdrawCashDetailsResponse(AbstractModel):
    """QueryBankWithdrawCashDetails返回參數結構體

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回碼
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回訊息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ResultNum: STRING(10)，本次交易返回查詢結果記錄數
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param StartRecordNo: STRING(30)，起始記錄号
注意：此欄位可能返回 null，表示取不到有效值。
        :type StartRecordNo: str
        :param EndFlag: STRING(2)，結束标志（0:否; 1:是）
注意：此欄位可能返回 null，表示取不到有效值。
        :type EndFlag: str
        :param TotalNum: STRING(10)，符合業務查詢條件的記錄總數（重複次數，一次最多返回20條記錄）
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalNum: str
        :param TranItemArray: 交易訊息數組
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranItemArray: list of WithdrawItem
        :param ReservedMsg: STRING(1027)，保留域
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ResultNum = None
        self.StartRecordNo = None
        self.EndFlag = None
        self.TotalNum = None
        self.TranItemArray = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ResultNum = params.get("ResultNum")
        self.StartRecordNo = params.get("StartRecordNo")
        self.EndFlag = params.get("EndFlag")
        self.TotalNum = params.get("TotalNum")
        if params.get("TranItemArray") is not None:
            self.TranItemArray = []
            for item in params.get("TranItemArray"):
                obj = WithdrawItem()
                obj._deserialize(item)
                self.TranItemArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryCommonTransferRechargeRequest(AbstractModel):
    """QueryCommonTransferRecharge請求參數結構體

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商戶号（簽約客戶号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（1爲查詢當日數據，0查詢曆史數據）
        :type FunctionFlag: str
        :param StartDate: STRING(8)，開始日期（格式：20190101）
        :type StartDate: str
        :param EndDate: STRING(8)，終止日期（格式：20190101）
        :type EndDate: str
        :param PageNum: STRING(10)，頁碼（起始值爲1，每次最多返回20條記錄，第二頁返回的記錄數爲第21至40條記錄，第三頁爲41至60條記錄，順序均按照建立時間的先後）
        :type PageNum: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.StartDate = None
        self.EndDate = None
        self.PageNum = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.PageNum = params.get("PageNum")
        self.ReservedMsg = params.get("ReservedMsg")


class QueryCommonTransferRechargeResponse(AbstractModel):
    """QueryCommonTransferRecharge返回參數結構體

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回碼
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回訊息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ResultNum: STRING(10)，本次交易返回查詢結果記錄數
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param StartRecordNo: STRING(30)，起始記錄号
注意：此欄位可能返回 null，表示取不到有效值。
        :type StartRecordNo: str
        :param EndFlag: STRING(2)，結束标志（0: 否; 1: 是）
注意：此欄位可能返回 null，表示取不到有效值。
        :type EndFlag: str
        :param TotalNum: STRING(10)，符合業務查詢條件的記錄總數（重複次數，一次最多返回20條記錄）
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalNum: str
        :param TranItemArray: 交易訊息數組
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranItemArray: list of TransferItem
        :param ReservedMsg: STRING(1027)，保留域
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ResultNum = None
        self.StartRecordNo = None
        self.EndFlag = None
        self.TotalNum = None
        self.TranItemArray = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ResultNum = params.get("ResultNum")
        self.StartRecordNo = params.get("StartRecordNo")
        self.EndFlag = params.get("EndFlag")
        self.TotalNum = params.get("TotalNum")
        if params.get("TranItemArray") is not None:
            self.TranItemArray = []
            for item in params.get("TranItemArray"):
                obj = TransferItem()
                obj._deserialize(item)
                self.TranItemArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryCustAcctIdBalanceRequest(AbstractModel):
    """QueryCustAcctIdBalance請求參數結構體

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商戶号（簽約客戶号）
        :type MrchCode: str
        :param QueryFlag: STRING(4)，查詢标志（2: 普通會員子賬号; 3: 功能子賬号）
        :type QueryFlag: str
        :param PageNum: STRING(10)，頁碼（起始值爲1，每次最多返回20條記錄，第二頁返回的記錄數爲第21至40條記錄，第三頁爲41至60條記錄，順序均按照建立時間的先後）
        :type PageNum: str
        :param SubAcctNo: STRING(50)，見證子帳戶的賬号（若SelectFlag爲2時，子賬号必輸）
        :type SubAcctNo: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.QueryFlag = None
        self.PageNum = None
        self.SubAcctNo = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.QueryFlag = params.get("QueryFlag")
        self.PageNum = params.get("PageNum")
        self.SubAcctNo = params.get("SubAcctNo")
        self.ReservedMsg = params.get("ReservedMsg")


class QueryCustAcctIdBalanceResponse(AbstractModel):
    """QueryCustAcctIdBalance返回參數結構體

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回碼
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回訊息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ResultNum: STRING(10)，本次交易返回查詢結果記錄數
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param StartRecordNo: STRING(30)，起始記錄号
注意：此欄位可能返回 null，表示取不到有效值。
        :type StartRecordNo: str
        :param EndFlag: STRING(2)，結束标志（0: 否; 1: 是）
注意：此欄位可能返回 null，表示取不到有效值。
        :type EndFlag: str
        :param TotalNum: STRING(10)，符合業務查詢條件的記錄總數（重複次數，一次最多返回20條記錄）
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalNum: str
        :param AcctArray: 帳戶訊息數組
注意：此欄位可能返回 null，表示取不到有效值。
        :type AcctArray: list of Acct
        :param ReservedMsg: STRING(1027)，保留域
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ResultNum = None
        self.StartRecordNo = None
        self.EndFlag = None
        self.TotalNum = None
        self.AcctArray = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ResultNum = params.get("ResultNum")
        self.StartRecordNo = params.get("StartRecordNo")
        self.EndFlag = params.get("EndFlag")
        self.TotalNum = params.get("TotalNum")
        if params.get("AcctArray") is not None:
            self.AcctArray = []
            for item in params.get("AcctArray"):
                obj = Acct()
                obj._deserialize(item)
                self.AcctArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryDeclareData(AbstractModel):
    """成功申報材料查詢數據

    """

    def __init__(self):
        """
        :param MerchantId: 商戶号
        :type MerchantId: str
        :param TransactionId: 對接方匯出指令編号
        :type TransactionId: str
        :param DeclareId: 申報流水号
        :type DeclareId: str
        :param OriginalDeclareId: 原申報流水号
注意：此欄位可能返回 null，表示取不到有效值。
        :type OriginalDeclareId: str
        :param PayerId: 付款人ID
        :type PayerId: str
        :param SourceCurrency: 源币種
        :type SourceCurrency: str
        :param SourceAmount: 源金額
注意：此欄位可能返回 null，表示取不到有效值。
        :type SourceAmount: str
        :param TargetCurrency: 目的币種
        :type TargetCurrency: str
        :param TargetAmount: 目的金額
注意：此欄位可能返回 null，表示取不到有效值。
        :type TargetAmount: str
        :param TradeCode: 交易編碼
        :type TradeCode: str
        :param Status: 狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self.MerchantId = None
        self.TransactionId = None
        self.DeclareId = None
        self.OriginalDeclareId = None
        self.PayerId = None
        self.SourceCurrency = None
        self.SourceAmount = None
        self.TargetCurrency = None
        self.TargetAmount = None
        self.TradeCode = None
        self.Status = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.TransactionId = params.get("TransactionId")
        self.DeclareId = params.get("DeclareId")
        self.OriginalDeclareId = params.get("OriginalDeclareId")
        self.PayerId = params.get("PayerId")
        self.SourceCurrency = params.get("SourceCurrency")
        self.SourceAmount = params.get("SourceAmount")
        self.TargetCurrency = params.get("TargetCurrency")
        self.TargetAmount = params.get("TargetAmount")
        self.TradeCode = params.get("TradeCode")
        self.Status = params.get("Status")


class QueryDeclareResult(AbstractModel):
    """成功申報材料查詢結果

    """

    def __init__(self):
        """
        :param Data: 成功申報材料查詢數據
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.QueryDeclareData`
        :param Code: 錯誤碼
        :type Code: str
        """
        self.Data = None
        self.Code = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = QueryDeclareData()
            self.Data._deserialize(params.get("Data"))
        self.Code = params.get("Code")


class QueryExchangeRateRequest(AbstractModel):
    """QueryExchangeRate請求參數結構體

    """

    def __init__(self):
        """
        :param SourceCurrency: 源币種 (預設CNY)
        :type SourceCurrency: str
        :param TargetCurrency: 目的币種 (見常見問題-匯出币種)
        :type TargetCurrency: str
        :param Profile: 接入環境。沙箱環境填sandbox
        :type Profile: str
        """
        self.SourceCurrency = None
        self.TargetCurrency = None
        self.Profile = None


    def _deserialize(self, params):
        self.SourceCurrency = params.get("SourceCurrency")
        self.TargetCurrency = params.get("TargetCurrency")
        self.Profile = params.get("Profile")


class QueryExchangeRateResponse(AbstractModel):
    """QueryExchangeRate返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 查詢匯率結果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryExchangerateResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = QueryExchangerateResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryExchangerateData(AbstractModel):
    """查詢匯率數據

    """

    def __init__(self):
        """
        :param Rate: 匯率
        :type Rate: str
        :param SourceCurrency: 源币種
        :type SourceCurrency: str
        :param TargetCurrency: 目的币種
        :type TargetCurrency: str
        :param RateTime: 匯率時間
        :type RateTime: str
        :param BaseCurrency: 基準币種
        :type BaseCurrency: str
        """
        self.Rate = None
        self.SourceCurrency = None
        self.TargetCurrency = None
        self.RateTime = None
        self.BaseCurrency = None


    def _deserialize(self, params):
        self.Rate = params.get("Rate")
        self.SourceCurrency = params.get("SourceCurrency")
        self.TargetCurrency = params.get("TargetCurrency")
        self.RateTime = params.get("RateTime")
        self.BaseCurrency = params.get("BaseCurrency")


class QueryExchangerateResult(AbstractModel):
    """查詢匯率結果

    """

    def __init__(self):
        """
        :param Code: 錯誤碼
        :type Code: str
        :param Data: 查詢匯率數據數組
        :type Data: list of QueryExchangerateData
        """
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = QueryExchangerateData()
                obj._deserialize(item)
                self.Data.append(obj)


class QueryInvoiceRequest(AbstractModel):
    """QueryInvoice請求參數結構體

    """

    def __init__(self):
        """
        :param InvoicePlatformId: 開票平台ID
        :type InvoicePlatformId: int
        :param OrderId: 訂單号
        :type OrderId: str
        :param OrderSn: 業務開票号
        :type OrderSn: str
        :param IsRed: 發票種類：
0：藍票
1：紅票【該欄位預設爲0， 如果需要查詢紅票訊息，本欄位必須傳1，否則可能查詢不到需要的發票訊息】。
        :type IsRed: int
        :param Profile: 接入環境。沙箱環境填sandbox。
        :type Profile: str
        """
        self.InvoicePlatformId = None
        self.OrderId = None
        self.OrderSn = None
        self.IsRed = None
        self.Profile = None


    def _deserialize(self, params):
        self.InvoicePlatformId = params.get("InvoicePlatformId")
        self.OrderId = params.get("OrderId")
        self.OrderSn = params.get("OrderSn")
        self.IsRed = params.get("IsRed")
        self.Profile = params.get("Profile")


class QueryInvoiceResponse(AbstractModel):
    """QueryInvoice返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 發票查詢結果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryInvoiceResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = QueryInvoiceResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryInvoiceResult(AbstractModel):
    """查詢發票結果

    """

    def __init__(self):
        """
        :param Message: 錯誤訊息
        :type Message: str
        :param Code: 錯誤碼
        :type Code: int
        :param Data: 查詢發票數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.QueryInvoiceResultData`
        """
        self.Message = None
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Message = params.get("Message")
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = QueryInvoiceResultData()
            self.Data._deserialize(params.get("Data"))


class QueryInvoiceResultData(AbstractModel):
    """查詢發票結果數據

    """

    def __init__(self):
        """
        :param OrderId: 訂單号
        :type OrderId: str
        :param OrderSn: 業務開票号
        :type OrderSn: str
        :param Status: 發票狀态
        :type Status: int
        :param Message: 開票描述
        :type Message: str
        :param TicketDate: 開票日期
        :type TicketDate: str
        :param TicketSn: 發票号碼
        :type TicketSn: str
        :param TicketCode: 發票代碼
        :type TicketCode: str
        :param CheckCode: 檢驗碼
        :type CheckCode: str
        :param AmountWithTax: 含稅金額(元)
        :type AmountWithTax: str
        :param AmountWithoutTax: 不含稅金額(元)
        :type AmountWithoutTax: str
        :param TaxAmount: 稅額(元)
        :type TaxAmount: str
        :param IsRedWashed: 是否被紅沖
        :type IsRedWashed: int
        :param PdfUrl: pdf網址
        :type PdfUrl: str
        """
        self.OrderId = None
        self.OrderSn = None
        self.Status = None
        self.Message = None
        self.TicketDate = None
        self.TicketSn = None
        self.TicketCode = None
        self.CheckCode = None
        self.AmountWithTax = None
        self.AmountWithoutTax = None
        self.TaxAmount = None
        self.IsRedWashed = None
        self.PdfUrl = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.OrderSn = params.get("OrderSn")
        self.Status = params.get("Status")
        self.Message = params.get("Message")
        self.TicketDate = params.get("TicketDate")
        self.TicketSn = params.get("TicketSn")
        self.TicketCode = params.get("TicketCode")
        self.CheckCode = params.get("CheckCode")
        self.AmountWithTax = params.get("AmountWithTax")
        self.AmountWithoutTax = params.get("AmountWithoutTax")
        self.TaxAmount = params.get("TaxAmount")
        self.IsRedWashed = params.get("IsRedWashed")
        self.PdfUrl = params.get("PdfUrl")


class QueryItem(AbstractModel):
    """聚鑫商戶餘額查詢輸出項

    """

    def __init__(self):
        """
        :param SubAcctNo: 子商戶帳戶
        :type SubAcctNo: str
        :param SubAcctProperty: 子帳戶屬性 
1：普通會員子賬号 
2：挂賬子賬号 
3：手續約子賬号 
4：利息子賬号
5：平台擔保子賬号
        :type SubAcctProperty: str
        :param SubMchId: 業務平台的子商戶Id，唯一
        :type SubMchId: str
        :param SubAcctName: 子帳戶名稱
        :type SubAcctName: str
        :param AcctAvailBal: 帳戶可用餘額
        :type AcctAvailBal: str
        :param CashAmt: 可提現金額
        :type CashAmt: str
        :param MaintenanceDate: 維護日期 開戶日期或修改日期
        :type MaintenanceDate: str
        """
        self.SubAcctNo = None
        self.SubAcctProperty = None
        self.SubMchId = None
        self.SubAcctName = None
        self.AcctAvailBal = None
        self.CashAmt = None
        self.MaintenanceDate = None


    def _deserialize(self, params):
        self.SubAcctNo = params.get("SubAcctNo")
        self.SubAcctProperty = params.get("SubAcctProperty")
        self.SubMchId = params.get("SubMchId")
        self.SubAcctName = params.get("SubAcctName")
        self.AcctAvailBal = params.get("AcctAvailBal")
        self.CashAmt = params.get("CashAmt")
        self.MaintenanceDate = params.get("MaintenanceDate")


class QueryMemberBindRequest(AbstractModel):
    """QueryMemberBind請求參數結構體

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商戶号（簽約客戶号）
        :type MrchCode: str
        :param QueryFlag: STRING(4)，查詢标志（1: 全部會員; 2: 單個會員; 3: 單個會員的證件訊息）
        :type QueryFlag: str
        :param PageNum: STRING (10)，頁碼（起始值爲1，每次最多返回20條記錄，第二頁返回的記錄數爲第21至40條記錄，第三頁爲41至60條記錄，順序均按照建立時間的先後）
        :type PageNum: str
        :param SubAcctNo: STRING(50)，見證子帳戶的賬号（若SelectFlag爲2或3時，子帳戶賬号必輸）
        :type SubAcctNo: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.QueryFlag = None
        self.PageNum = None
        self.SubAcctNo = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.QueryFlag = params.get("QueryFlag")
        self.PageNum = params.get("PageNum")
        self.SubAcctNo = params.get("SubAcctNo")
        self.ReservedMsg = params.get("ReservedMsg")


class QueryMemberBindResponse(AbstractModel):
    """QueryMemberBind返回參數結構體

    """

    def __init__(self):
        """
        :param ResultNum: STRING (10)，本次交易返回查詢結果記錄數
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param StartRecordNo: STRING(30)，起始記錄号
注意：此欄位可能返回 null，表示取不到有效值。
        :type StartRecordNo: str
        :param EndFlag: STRING(2)，結束标志（0: 否; 1: 是）
注意：此欄位可能返回 null，表示取不到有效值。
        :type EndFlag: str
        :param TotalNum: STRING (10)，符合業務查詢條件的記錄總數（重複次數，一次最多返回20條記錄）
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalNum: str
        :param TranItemArray: 交易訊息數組
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranItemArray: list of TranItem
        :param ReservedMsg: STRING(1027)，保留域
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param TxnReturnCode: String(20)，返回碼
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回訊息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ResultNum = None
        self.StartRecordNo = None
        self.EndFlag = None
        self.TotalNum = None
        self.TranItemArray = None
        self.ReservedMsg = None
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultNum = params.get("ResultNum")
        self.StartRecordNo = params.get("StartRecordNo")
        self.EndFlag = params.get("EndFlag")
        self.TotalNum = params.get("TotalNum")
        if params.get("TranItemArray") is not None:
            self.TranItemArray = []
            for item in params.get("TranItemArray"):
                obj = TranItem()
                obj._deserialize(item)
                self.TranItemArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.RequestId = params.get("RequestId")


class QueryMemberTransactionRequest(AbstractModel):
    """QueryMemberTransaction請求參數結構體

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商戶号（簽約客戶号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（1: 下單預支付; 2: 确認并付款; 3: 退款; 6: 直接支付T+1; 9: 直接支付T+0）
        :type FunctionFlag: str
        :param OutSubAcctNo: STRING(50)，轉出方的見證子帳戶的賬号（付款方）
        :type OutSubAcctNo: str
        :param OutMemberCode: STRING(32)，轉出方的交易網會員代碼
        :type OutMemberCode: str
        :param OutSubAcctName: STRING(150)，轉出方的見證子帳戶的戶名（戶名是綁卡時上送的帳戶名稱，如果未綁卡，就送OpenCustAcctId介面上送的用戶昵稱UserNickname）
        :type OutSubAcctName: str
        :param InSubAcctNo: STRING(50)，轉入方的見證子帳戶的賬号（收款方）
        :type InSubAcctNo: str
        :param InMemberCode: STRING(32)，轉入方的交易網會員代碼
        :type InMemberCode: str
        :param InSubAcctName: STRING(150)，轉入方的見證子帳戶的戶名（戶名是綁卡時上送的帳戶名稱，如果未綁卡，就送OpenCustAcctId介面上送的用戶昵稱UserNickname）
        :type InSubAcctName: str
        :param TranAmt: STRING(20)，交易金額
        :type TranAmt: str
        :param TranFee: STRING(20)，交易費用（平台收取交易費用）
        :type TranFee: str
        :param TranType: STRING(20)，交易類型（01: 普通交易）
        :type TranType: str
        :param Ccy: STRING(3)，币種（預設: RMB）
        :type Ccy: str
        :param OrderNo: STRING(50)，訂單号（功能标志爲1,2,3時必輸）
        :type OrderNo: str
        :param OrderContent: STRING(500)，訂單内容
        :type OrderContent: str
        :param Remark: STRING(300)，備注（建議可送訂單号，可在對賬文件的備注欄位獲取到）
        :type Remark: str
        :param ReservedMsg: STRING(1027)，保留域（若需簡訊驗證碼則此項必輸簡訊指令号）
        :type ReservedMsg: str
        :param WebSign: STRING(300)，網銀簽名（若需簡訊驗證碼則此項必輸）
        :type WebSign: str
        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.OutSubAcctNo = None
        self.OutMemberCode = None
        self.OutSubAcctName = None
        self.InSubAcctNo = None
        self.InMemberCode = None
        self.InSubAcctName = None
        self.TranAmt = None
        self.TranFee = None
        self.TranType = None
        self.Ccy = None
        self.OrderNo = None
        self.OrderContent = None
        self.Remark = None
        self.ReservedMsg = None
        self.WebSign = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.OutSubAcctNo = params.get("OutSubAcctNo")
        self.OutMemberCode = params.get("OutMemberCode")
        self.OutSubAcctName = params.get("OutSubAcctName")
        self.InSubAcctNo = params.get("InSubAcctNo")
        self.InMemberCode = params.get("InMemberCode")
        self.InSubAcctName = params.get("InSubAcctName")
        self.TranAmt = params.get("TranAmt")
        self.TranFee = params.get("TranFee")
        self.TranType = params.get("TranType")
        self.Ccy = params.get("Ccy")
        self.OrderNo = params.get("OrderNo")
        self.OrderContent = params.get("OrderContent")
        self.Remark = params.get("Remark")
        self.ReservedMsg = params.get("ReservedMsg")
        self.WebSign = params.get("WebSign")


class QueryMemberTransactionResponse(AbstractModel):
    """QueryMemberTransaction返回參數結構體

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回碼
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回訊息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，見證系統流水号（即電商見證寶系統生成的流水号，可關聯具體一筆請求）
注意：此欄位可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryMerchantBalanceData(AbstractModel):
    """對接帳戶餘額查詢數據

    """

    def __init__(self):
        """
        :param Currency: 餘額币種
        :type Currency: str
        :param Balance: 帳戶餘額
        :type Balance: str
        :param MerchantId: 商戶ID
        :type MerchantId: str
        """
        self.Currency = None
        self.Balance = None
        self.MerchantId = None


    def _deserialize(self, params):
        self.Currency = params.get("Currency")
        self.Balance = params.get("Balance")
        self.MerchantId = params.get("MerchantId")


class QueryMerchantBalanceRequest(AbstractModel):
    """QueryMerchantBalance請求參數結構體

    """

    def __init__(self):
        """
        :param Currency: 餘額币種
        :type Currency: str
        :param Profile: 接入環境。沙箱環境填sandbox
        :type Profile: str
        """
        self.Currency = None
        self.Profile = None


    def _deserialize(self, params):
        self.Currency = params.get("Currency")
        self.Profile = params.get("Profile")


class QueryMerchantBalanceResponse(AbstractModel):
    """QueryMerchantBalance返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 對接方帳戶餘額查詢結果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryMerchantBalanceResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = QueryMerchantBalanceResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryMerchantBalanceResult(AbstractModel):
    """對接帳戶餘額查詢結果

    """

    def __init__(self):
        """
        :param Code: 錯誤碼
        :type Code: str
        :param Data: 對接帳戶餘額查詢數據
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.QueryMerchantBalanceData`
        """
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = QueryMerchantBalanceData()
            self.Data._deserialize(params.get("Data"))


class QueryOrderOutOrderList(AbstractModel):
    """查詢訂單介面的出參，訂單清單

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param Amt: 支付金額，單位：分
        :type Amt: int
        :param UserId: 用戶Id
        :type UserId: str
        :param CashAmt: 現金支付金額
        :type CashAmt: str
        :param Metadata: 發貨标識，由業務在調用聚鑫下單 介面的時候下發
        :type Metadata: str
        :param PayTime: 支付時間unix時間戳
        :type PayTime: str
        :param CouponAmt: 抵扣券金額
        :type CouponAmt: str
        :param OrderTime: 下單時間unix時間戳
        :type OrderTime: str
        :param ProductId: 物品id
        :type ProductId: str
        :param SceneInfo: 高速場景訊息
        :type SceneInfo: str
        :param OrderState: 當前訂單的訂單狀态 
0：初始狀态，獲取聚鑫交易訂單成功；  
1：拉起聚鑫支付頁面成功，用戶未 支付；
2：用戶支付成功，正在發貨；
3：用戶支付成功，發貨失敗；
4：用戶支付成功，發貨成功；
5：聚鑫支付頁面正在失效中；
6：聚鑫支付頁面已經失效；
        :type OrderState: str
        :param Channel: 支付管道：wechat：微信支付;
qqwallet：QQ錢包;
bank：網銀
        :type Channel: str
        :param RefundFlag: 是否曾退款
        :type RefundFlag: str
        :param OutTradeNo: 務支付訂單号
        :type OutTradeNo: str
        :param ProductName: 商品名稱
        :type ProductName: str
        :param CallBackTime: 支付回調時間，unix時間戳
        :type CallBackTime: str
        :param CurrencyType: ISO 貨币代碼，CNY
        :type CurrencyType: str
        :param AcctSubAppId: 微校場景帳戶Id
        :type AcctSubAppId: str
        :param TransactionId: 調用下單介面獲取的聚鑫交易訂單
        :type TransactionId: str
        :param ChannelOrderId: 聚鑫内部管道訂單号
        :type ChannelOrderId: str
        :param SubOrderList: 調用下單介面傳進來的 SubOutTradeNoList
        :type SubOrderList: list of QueryOrderOutSubOrderList
        :param ChannelExternalOrderId: 支付機構訂單号
        :type ChannelExternalOrderId: str
        """
        self.MidasAppId = None
        self.Amt = None
        self.UserId = None
        self.CashAmt = None
        self.Metadata = None
        self.PayTime = None
        self.CouponAmt = None
        self.OrderTime = None
        self.ProductId = None
        self.SceneInfo = None
        self.OrderState = None
        self.Channel = None
        self.RefundFlag = None
        self.OutTradeNo = None
        self.ProductName = None
        self.CallBackTime = None
        self.CurrencyType = None
        self.AcctSubAppId = None
        self.TransactionId = None
        self.ChannelOrderId = None
        self.SubOrderList = None
        self.ChannelExternalOrderId = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.Amt = params.get("Amt")
        self.UserId = params.get("UserId")
        self.CashAmt = params.get("CashAmt")
        self.Metadata = params.get("Metadata")
        self.PayTime = params.get("PayTime")
        self.CouponAmt = params.get("CouponAmt")
        self.OrderTime = params.get("OrderTime")
        self.ProductId = params.get("ProductId")
        self.SceneInfo = params.get("SceneInfo")
        self.OrderState = params.get("OrderState")
        self.Channel = params.get("Channel")
        self.RefundFlag = params.get("RefundFlag")
        self.OutTradeNo = params.get("OutTradeNo")
        self.ProductName = params.get("ProductName")
        self.CallBackTime = params.get("CallBackTime")
        self.CurrencyType = params.get("CurrencyType")
        self.AcctSubAppId = params.get("AcctSubAppId")
        self.TransactionId = params.get("TransactionId")
        self.ChannelOrderId = params.get("ChannelOrderId")
        if params.get("SubOrderList") is not None:
            self.SubOrderList = []
            for item in params.get("SubOrderList"):
                obj = QueryOrderOutSubOrderList()
                obj._deserialize(item)
                self.SubOrderList.append(obj)
        self.ChannelExternalOrderId = params.get("ChannelExternalOrderId")


class QueryOrderOutSubOrderList(AbstractModel):
    """子訂單清單

    """

    def __init__(self):
        """
        :param Amt: 子訂單支付金額
        :type Amt: int
        :param SubMchIncome: 子訂單結算應收金額，單位：分
        :type SubMchIncome: int
        :param Metadata: 發貨标識，由業務在調用Midas下單介面的時候下發。
        :type Metadata: str
        :param OriginalAmt: 子訂單原始金額
        :type OriginalAmt: int
        :param PlatformIncome: 子訂單平台應收金額，單位：分
        :type PlatformIncome: int
        :param ProductDetail: 子訂單商品詳情
        :type ProductDetail: str
        :param ProductName: 子訂單商品名稱
        :type ProductName: str
        :param SettleCheck: 核銷狀态，1表示核銷，0表示未核銷
        :type SettleCheck: int
        :param SubAppId: 聚鑫計費SubAppId，代表子商戶
        :type SubAppId: str
        :param SubOutTradeNo: 子訂單号
        :type SubOutTradeNo: str
        """
        self.Amt = None
        self.SubMchIncome = None
        self.Metadata = None
        self.OriginalAmt = None
        self.PlatformIncome = None
        self.ProductDetail = None
        self.ProductName = None
        self.SettleCheck = None
        self.SubAppId = None
        self.SubOutTradeNo = None


    def _deserialize(self, params):
        self.Amt = params.get("Amt")
        self.SubMchIncome = params.get("SubMchIncome")
        self.Metadata = params.get("Metadata")
        self.OriginalAmt = params.get("OriginalAmt")
        self.PlatformIncome = params.get("PlatformIncome")
        self.ProductDetail = params.get("ProductDetail")
        self.ProductName = params.get("ProductName")
        self.SettleCheck = params.get("SettleCheck")
        self.SubAppId = params.get("SubAppId")
        self.SubOutTradeNo = params.get("SubOutTradeNo")


class QueryOrderRequest(AbstractModel):
    """QueryOrder請求參數結構體

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主 MidasAppId
        :type MidasAppId: str
        :param UserId: 用戶ID，長度不小於5位， 僅支援字母和數字的組合
        :type UserId: str
        :param Type: type=by_order根據訂單号 查訂單；
type=by_user根據用戶id 查訂單 。
        :type Type: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全金鑰計算的簽名
        :type MidasSignature: str
        :param Count: 每頁返回的記錄數。根據用戶 号碼查詢訂單清單時需要傳。 用于分頁展示。Type=by_order時必填
        :type Count: int
        :param Offset: 記錄數偏移量，預設從0開 始。根據用戶号碼查詢訂單列 表時需要傳。用于分頁展示。Type=by_order時必填
        :type Offset: int
        :param StartTime: 查詢開始時間，Unix時間戳。Type=by_order時必填
        :type StartTime: str
        :param EndTime: 查詢結束時間，Unix時間戳。Type=by_order時必填
        :type EndTime: str
        :param OutTradeNo: 業務訂單号，OutTradeNo與 TransactionId不能同時爲 空，都傳優先使用 OutTradeNo
        :type OutTradeNo: str
        :param TransactionId: 聚鑫訂單号，OutTradeNo與 TransactionId不能同時爲 空，都傳優先使用 OutTradeNo
        :type TransactionId: str
        """
        self.MidasAppId = None
        self.UserId = None
        self.Type = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.Count = None
        self.Offset = None
        self.StartTime = None
        self.EndTime = None
        self.OutTradeNo = None
        self.TransactionId = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.UserId = params.get("UserId")
        self.Type = params.get("Type")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.Count = params.get("Count")
        self.Offset = params.get("Offset")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.OutTradeNo = params.get("OutTradeNo")
        self.TransactionId = params.get("TransactionId")


class QueryOrderResponse(AbstractModel):
    """QueryOrder返回參數結構體

    """

    def __init__(self):
        """
        :param TotalNum: 返回訂單數
        :type TotalNum: int
        :param OrderList: 查詢結果的訂單清單
        :type OrderList: list of QueryOrderOutOrderList
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.OrderList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("OrderList") is not None:
            self.OrderList = []
            for item in params.get("OrderList"):
                obj = QueryOrderOutOrderList()
                obj._deserialize(item)
                self.OrderList.append(obj)
        self.RequestId = params.get("RequestId")


class QueryOutwardOrderData(AbstractModel):
    """查詢匯出數據

    """

    def __init__(self):
        """
        :param MerchantId: 商戶号
        :type MerchantId: str
        :param TransactionId: 對接方匯出指令編号
        :type TransactionId: str
        :param AcctDate: 财務日期
注意：此欄位可能返回 null，表示取不到有效值。
        :type AcctDate: str
        :param PricingCurrency: 定價币種
注意：此欄位可能返回 null，表示取不到有效值。
        :type PricingCurrency: str
        :param SourceCurrency: 源币種
注意：此欄位可能返回 null，表示取不到有效值。
        :type SourceCurrency: str
        :param SourceAmount: 源金額
注意：此欄位可能返回 null，表示取不到有效值。
        :type SourceAmount: str
        :param TargetCurrency: 目的币種
注意：此欄位可能返回 null，表示取不到有效值。
        :type TargetCurrency: str
        :param TargetAmount: 目的金額
注意：此欄位可能返回 null，表示取不到有效值。
        :type TargetAmount: str
        :param FxRate: 匯率
注意：此欄位可能返回 null，表示取不到有效值。
        :type FxRate: str
        :param Status: 指令狀态
        :type Status: str
        :param FailReason: 失敗原因
注意：此欄位可能返回 null，表示取不到有效值。
        :type FailReason: str
        :param RefundAmount: 退匯金額
注意：此欄位可能返回 null，表示取不到有效值。
        :type RefundAmount: str
        :param RefundCurrency: 退匯币種
注意：此欄位可能返回 null，表示取不到有效值。
        :type RefundCurrency: str
        """
        self.MerchantId = None
        self.TransactionId = None
        self.AcctDate = None
        self.PricingCurrency = None
        self.SourceCurrency = None
        self.SourceAmount = None
        self.TargetCurrency = None
        self.TargetAmount = None
        self.FxRate = None
        self.Status = None
        self.FailReason = None
        self.RefundAmount = None
        self.RefundCurrency = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.TransactionId = params.get("TransactionId")
        self.AcctDate = params.get("AcctDate")
        self.PricingCurrency = params.get("PricingCurrency")
        self.SourceCurrency = params.get("SourceCurrency")
        self.SourceAmount = params.get("SourceAmount")
        self.TargetCurrency = params.get("TargetCurrency")
        self.TargetAmount = params.get("TargetAmount")
        self.FxRate = params.get("FxRate")
        self.Status = params.get("Status")
        self.FailReason = params.get("FailReason")
        self.RefundAmount = params.get("RefundAmount")
        self.RefundCurrency = params.get("RefundCurrency")


class QueryOutwardOrderRequest(AbstractModel):
    """QueryOutwardOrder請求參數結構體

    """

    def __init__(self):
        """
        :param TransactionId: 對接方匯出指令編号
        :type TransactionId: str
        :param Profile: 接入環境。沙箱環境填sandbox
        :type Profile: str
        """
        self.TransactionId = None
        self.Profile = None


    def _deserialize(self, params):
        self.TransactionId = params.get("TransactionId")
        self.Profile = params.get("Profile")


class QueryOutwardOrderResponse(AbstractModel):
    """QueryOutwardOrder返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 查詢匯出結果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryOutwardOrderResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = QueryOutwardOrderResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryOutwardOrderResult(AbstractModel):
    """查詢匯出結果

    """

    def __init__(self):
        """
        :param Code: 錯誤碼
        :type Code: str
        :param Data: 查詢匯出數據
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.QueryOutwardOrderData`
        """
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = QueryOutwardOrderData()
            self.Data._deserialize(params.get("Data"))


class QueryPayerInfoRequest(AbstractModel):
    """QueryPayerInfo請求參數結構體

    """

    def __init__(self):
        """
        :param PayerId: 付款人ID
        :type PayerId: str
        :param Profile: 接入環境。沙箱環境填sandbox
        :type Profile: str
        """
        self.PayerId = None
        self.Profile = None


    def _deserialize(self, params):
        self.PayerId = params.get("PayerId")
        self.Profile = params.get("Profile")


class QueryPayerInfoResponse(AbstractModel):
    """QueryPayerInfo返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 付款人查詢結果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryPayerinfoResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = QueryPayerinfoResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryPayerinfoData(AbstractModel):
    """付款人查詢數據

    """

    def __init__(self):
        """
        :param MerchantId: 商戶号
        :type MerchantId: str
        :param PayerId: 付款人ID
        :type PayerId: str
        :param Status: 審核狀态
        :type Status: str
        :param FailReason: 失敗原因
注意：此欄位可能返回 null，表示取不到有效值。
        :type FailReason: str
        :param PayerType: 付款人類型
        :type PayerType: str
        :param PayerName: 付款人姓名
        :type PayerName: str
        :param PayerIdType: 付款人證件類型
        :type PayerIdType: str
        :param PayerIdNo: 付款人證件号
        :type PayerIdNo: str
        :param PayerContactNumber: 付款人聯系電話
注意：此欄位可能返回 null，表示取不到有效值。
        :type PayerContactNumber: str
        :param PayerEmailAddress: 付款人聯系電子信箱
注意：此欄位可能返回 null，表示取不到有效值。
        :type PayerEmailAddress: str
        :param PayerCountryCode: 付款人常駐國家或地區編碼
        :type PayerCountryCode: str
        :param PayerContactName: 付款人聯系名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type PayerContactName: str
        """
        self.MerchantId = None
        self.PayerId = None
        self.Status = None
        self.FailReason = None
        self.PayerType = None
        self.PayerName = None
        self.PayerIdType = None
        self.PayerIdNo = None
        self.PayerContactNumber = None
        self.PayerEmailAddress = None
        self.PayerCountryCode = None
        self.PayerContactName = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.PayerId = params.get("PayerId")
        self.Status = params.get("Status")
        self.FailReason = params.get("FailReason")
        self.PayerType = params.get("PayerType")
        self.PayerName = params.get("PayerName")
        self.PayerIdType = params.get("PayerIdType")
        self.PayerIdNo = params.get("PayerIdNo")
        self.PayerContactNumber = params.get("PayerContactNumber")
        self.PayerEmailAddress = params.get("PayerEmailAddress")
        self.PayerCountryCode = params.get("PayerCountryCode")
        self.PayerContactName = params.get("PayerContactName")


class QueryPayerinfoResult(AbstractModel):
    """付款人查詢結果

    """

    def __init__(self):
        """
        :param Code: 錯誤碼
        :type Code: str
        :param Data: 付款人查詢數據
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.QueryPayerinfoData`
        """
        self.Code = None
        self.Data = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        if params.get("Data") is not None:
            self.Data = QueryPayerinfoData()
            self.Data._deserialize(params.get("Data"))


class QueryReconciliationDocumentRequest(AbstractModel):
    """QueryReconciliationDocument請求參數結構體

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商戶号
        :type MrchCode: str
        :param FileType: STRING(10)，文件類型（儲值文件-CZ; 提現文件-TX; 交易文件-JY; 餘額文件-YE; 合約文件-HY）
        :type FileType: str
        :param FileDate: STRING(8)，文件日期（格式：20190101）
        :type FileDate: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.FileType = None
        self.FileDate = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FileType = params.get("FileType")
        self.FileDate = params.get("FileDate")
        self.ReservedMsg = params.get("ReservedMsg")


class QueryReconciliationDocumentResponse(AbstractModel):
    """QueryReconciliationDocument返回參數結構體

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回碼
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回訊息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ResultNum: STRING(10)，本次交易返回查詢結果記錄數
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResultNum: str
        :param TranItemArray: 交易訊息數組
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranItemArray: list of FileItem
        :param ReservedMsg: STRING(1027)，保留域
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ResultNum = None
        self.TranItemArray = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ResultNum = params.get("ResultNum")
        if params.get("TranItemArray") is not None:
            self.TranItemArray = []
            for item in params.get("TranItemArray"):
                obj = FileItem()
                obj._deserialize(item)
                self.TranItemArray.append(obj)
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryRefundRequest(AbstractModel):
    """QueryRefund請求參數結構體

    """

    def __init__(self):
        """
        :param UserId: 用戶ID，長度不小於5位，僅支援字母和數字的組合。
        :type UserId: str
        :param RefundId: 退款訂單号，僅支援數字、字母、下劃線（_）、橫杠字元（-）、點（.）的組合。
        :type RefundId: str
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全金鑰計算的簽名
        :type MidasSignature: str
        """
        self.UserId = None
        self.RefundId = None
        self.MidasAppId = None
        self.MidasSecretId = None
        self.MidasSignature = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.RefundId = params.get("RefundId")
        self.MidasAppId = params.get("MidasAppId")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")


class QueryRefundResponse(AbstractModel):
    """QueryRefund返回參數結構體

    """

    def __init__(self):
        """
        :param State: 退款狀态碼，退款提交成功後返回  1：退款中；  2：退款成功；  3：退款失敗。
        :type State: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.State = None
        self.RequestId = None


    def _deserialize(self, params):
        self.State = params.get("State")
        self.RequestId = params.get("RequestId")


class QuerySingleTransactionStatusRequest(AbstractModel):
    """QuerySingleTransactionStatus請求參數結構體

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商戶号（簽約客戶号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（2: 會員間交易; 3: 提現; 4: 儲值）
        :type FunctionFlag: str
        :param TranNetSeqNo: STRING(52)，交易網流水号（提現，儲值或會員交易請求時的CnsmrSeqNo值）
        :type TranNetSeqNo: str
        :param SubAcctNo: STRING(50)，見證子帳戶的帳号（未啓用）
        :type SubAcctNo: str
        :param TranDate: STRING(8)，交易日期（未啓用）
        :type TranDate: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.TranNetSeqNo = None
        self.SubAcctNo = None
        self.TranDate = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.TranNetSeqNo = params.get("TranNetSeqNo")
        self.SubAcctNo = params.get("SubAcctNo")
        self.TranDate = params.get("TranDate")
        self.ReservedMsg = params.get("ReservedMsg")


class QuerySingleTransactionStatusResponse(AbstractModel):
    """QuerySingleTransactionStatus返回參數結構體

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回碼
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回訊息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param BookingFlag: STRING(2)，記賬标志（記賬标志。1: 登記挂賬; 2: 支付; 3: 提現; 4: 清分; 5: 下單預支付; 6: 确認并付款; 7: 退款; 8: 支付到平台; N: 其他）
注意：此欄位可能返回 null，表示取不到有效值。
        :type BookingFlag: str
        :param TranStatus: STRING(32)，交易狀态（0: 成功; 1: 失敗; 2: 待确認; 5: 待處理; 6: 處理中。0和1是終态，2、5、6是中間态，其中2是特指提現後待确認提現是否成功，5是銀行收到交易等待處理，6是交易正在處理）
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranStatus: str
        :param TranAmt: STRING(20)，交易金額
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranAmt: str
        :param TranDate: STRING(8)，交易日期
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranDate: str
        :param TranTime: STRING(20)，交易時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranTime: str
        :param InSubAcctNo: STRING(50)，轉入子帳戶賬号
注意：此欄位可能返回 null，表示取不到有效值。
        :type InSubAcctNo: str
        :param OutSubAcctNo: STRING(50)，轉出子帳戶賬号
注意：此欄位可能返回 null，表示取不到有效值。
        :type OutSubAcctNo: str
        :param FailMsg: STRING(300)，失敗訊息（當提現失敗時，返回交易失敗原因）
注意：此欄位可能返回 null，表示取不到有效值。
        :type FailMsg: str
        :param OldTranFrontSeqNo: STRING(50)，原前置流水号
注意：此欄位可能返回 null，表示取不到有效值。
        :type OldTranFrontSeqNo: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.BookingFlag = None
        self.TranStatus = None
        self.TranAmt = None
        self.TranDate = None
        self.TranTime = None
        self.InSubAcctNo = None
        self.OutSubAcctNo = None
        self.FailMsg = None
        self.OldTranFrontSeqNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.BookingFlag = params.get("BookingFlag")
        self.TranStatus = params.get("TranStatus")
        self.TranAmt = params.get("TranAmt")
        self.TranDate = params.get("TranDate")
        self.TranTime = params.get("TranTime")
        self.InSubAcctNo = params.get("InSubAcctNo")
        self.OutSubAcctNo = params.get("OutSubAcctNo")
        self.FailMsg = params.get("FailMsg")
        self.OldTranFrontSeqNo = params.get("OldTranFrontSeqNo")
        self.RequestId = params.get("RequestId")


class QuerySmallAmountTransferRequest(AbstractModel):
    """QuerySmallAmountTransfer請求參數結構體

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商戶号（簽約客戶号）
        :type MrchCode: str
        :param OldTranSeqNo: STRING(52)，原交易流水号（小額鑒權交易請求時的CnsmrSeqNo值）
        :type OldTranSeqNo: str
        :param TranDate: STRING(8)，交易日期（格式：20190101）
        :type TranDate: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.OldTranSeqNo = None
        self.TranDate = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.OldTranSeqNo = params.get("OldTranSeqNo")
        self.TranDate = params.get("TranDate")
        self.ReservedMsg = params.get("ReservedMsg")


class QuerySmallAmountTransferResponse(AbstractModel):
    """QuerySmallAmountTransfer返回參數結構體

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回碼
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回訊息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ReturnStatus: STRING(10)，返回狀态（0: 成功; 1: 失敗; 2: 待确認）
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReturnStatus: str
        :param ReturnMsg: STRING(512)，返回訊息（失敗返回具體訊息）
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReturnMsg: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ReturnStatus = None
        self.ReturnMsg = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ReturnStatus = params.get("ReturnStatus")
        self.ReturnMsg = params.get("ReturnMsg")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class QueryTradeData(AbstractModel):
    """貿易材料明細查詢數據

    """

    def __init__(self):
        """
        :param MerchantId: 商戶号
        :type MerchantId: str
        :param TradeFileId: 貿易材料流水号
        :type TradeFileId: str
        :param TradeOrderId: 貿易材料訂單号
        :type TradeOrderId: str
        :param Status: 審核狀态
        :type Status: str
        :param FailReason: 失敗原因
注意：此欄位可能返回 null，表示取不到有效值。
        :type FailReason: str
        :param PayerId: 付款人ID
        :type PayerId: str
        :param PayeeName: 收款人姓名
        :type PayeeName: str
        :param PayeeCountryCode: 收款人常駐國家或地區編碼
        :type PayeeCountryCode: str
        :param TradeType: 交易類型
        :type TradeType: str
        :param TradeTime: 交易日期
        :type TradeTime: str
        :param TradeCurrency: 交易币種
        :type TradeCurrency: str
        :param TradeAmount: 交易金額
        :type TradeAmount: str
        :param TradeName: 交易名稱
        :type TradeName: str
        :param TradeCount: 交易數量
        :type TradeCount: int
        :param GoodsCarrier: 貨貿承運人
注意：此欄位可能返回 null，表示取不到有效值。
        :type GoodsCarrier: str
        :param ServiceDetail: 服貿交易細節
注意：此欄位可能返回 null，表示取不到有效值。
        :type ServiceDetail: str
        :param ServiceTime: 服貿服務時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type ServiceTime: str
        """
        self.MerchantId = None
        self.TradeFileId = None
        self.TradeOrderId = None
        self.Status = None
        self.FailReason = None
        self.PayerId = None
        self.PayeeName = None
        self.PayeeCountryCode = None
        self.TradeType = None
        self.TradeTime = None
        self.TradeCurrency = None
        self.TradeAmount = None
        self.TradeName = None
        self.TradeCount = None
        self.GoodsCarrier = None
        self.ServiceDetail = None
        self.ServiceTime = None


    def _deserialize(self, params):
        self.MerchantId = params.get("MerchantId")
        self.TradeFileId = params.get("TradeFileId")
        self.TradeOrderId = params.get("TradeOrderId")
        self.Status = params.get("Status")
        self.FailReason = params.get("FailReason")
        self.PayerId = params.get("PayerId")
        self.PayeeName = params.get("PayeeName")
        self.PayeeCountryCode = params.get("PayeeCountryCode")
        self.TradeType = params.get("TradeType")
        self.TradeTime = params.get("TradeTime")
        self.TradeCurrency = params.get("TradeCurrency")
        self.TradeAmount = params.get("TradeAmount")
        self.TradeName = params.get("TradeName")
        self.TradeCount = params.get("TradeCount")
        self.GoodsCarrier = params.get("GoodsCarrier")
        self.ServiceDetail = params.get("ServiceDetail")
        self.ServiceTime = params.get("ServiceTime")


class QueryTradeRequest(AbstractModel):
    """QueryTrade請求參數結構體

    """

    def __init__(self):
        """
        :param TradeFileId: 貿易材料流水号
        :type TradeFileId: str
        :param Profile: 接入環境。沙箱環境填sandbox
        :type Profile: str
        """
        self.TradeFileId = None
        self.Profile = None


    def _deserialize(self, params):
        self.TradeFileId = params.get("TradeFileId")
        self.Profile = params.get("Profile")


class QueryTradeResponse(AbstractModel):
    """QueryTrade返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 貿易材料明細查詢結果
        :type Result: :class:`tencentcloud.cpdp.v20190820.models.QueryTradeResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = QueryTradeResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class QueryTradeResult(AbstractModel):
    """貿易材料明細查詢結果

    """

    def __init__(self):
        """
        :param Data: 貿易材料明細查詢數據
        :type Data: :class:`tencentcloud.cpdp.v20190820.models.QueryTradeData`
        :param Code: 錯誤碼
        :type Code: str
        """
        self.Data = None
        self.Code = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = QueryTradeData()
            self.Data._deserialize(params.get("Data"))
        self.Code = params.get("Code")


class RechargeMemberThirdPayRequest(AbstractModel):
    """RechargeMemberThirdPay請求參數結構體

    """

    def __init__(self):
        """
        :param TranNetMemberCode: STRING(32)，交易網會代碼
        :type TranNetMemberCode: str
        :param MemberFillAmt: STRING(20)，會員儲值金額
        :type MemberFillAmt: str
        :param Commission: STRING(20)，手續約金額
        :type Commission: str
        :param Ccy: STRING(3)，币種。如RMB
        :type Ccy: str
        :param PayChannelType: STRING(20)，支付管道類型。
0001-微信
0002-支付寶
0003-京東支付
        :type PayChannelType: str
        :param PayChannelAssignMerNo: STRING(50)，支付管道所分配的商戶号
        :type PayChannelAssignMerNo: str
        :param PayChannelTranSeqNo: STRING(52)，支付管道交易流水号
        :type PayChannelTranSeqNo: str
        :param EjzbOrderNo: STRING(52)，電商見證寶訂單号
        :type EjzbOrderNo: str
        :param MrchCode: String(22)，商戶号
        :type MrchCode: str
        :param EjzbOrderContent: STRING(500)，電商見證寶訂單内容
        :type EjzbOrderContent: str
        :param Remark: STRING(300)，備注
        :type Remark: str
        :param ReservedMsgOne: STRING(300)，保留域1
        :type ReservedMsgOne: str
        :param ReservedMsgTwo: STRING(300)，保留域2
        :type ReservedMsgTwo: str
        :param ReservedMsgThree: STRING(300)，保留域3
        :type ReservedMsgThree: str
        """
        self.TranNetMemberCode = None
        self.MemberFillAmt = None
        self.Commission = None
        self.Ccy = None
        self.PayChannelType = None
        self.PayChannelAssignMerNo = None
        self.PayChannelTranSeqNo = None
        self.EjzbOrderNo = None
        self.MrchCode = None
        self.EjzbOrderContent = None
        self.Remark = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.ReservedMsgThree = None


    def _deserialize(self, params):
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberFillAmt = params.get("MemberFillAmt")
        self.Commission = params.get("Commission")
        self.Ccy = params.get("Ccy")
        self.PayChannelType = params.get("PayChannelType")
        self.PayChannelAssignMerNo = params.get("PayChannelAssignMerNo")
        self.PayChannelTranSeqNo = params.get("PayChannelTranSeqNo")
        self.EjzbOrderNo = params.get("EjzbOrderNo")
        self.MrchCode = params.get("MrchCode")
        self.EjzbOrderContent = params.get("EjzbOrderContent")
        self.Remark = params.get("Remark")
        self.ReservedMsgOne = params.get("ReservedMsgOne")
        self.ReservedMsgTwo = params.get("ReservedMsgTwo")
        self.ReservedMsgThree = params.get("ReservedMsgThree")


class RechargeMemberThirdPayResponse(AbstractModel):
    """RechargeMemberThirdPay返回參數結構體

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回碼
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回訊息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，前置流水号
注意：此欄位可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param MemberSubAcctPreAvailBal: STRING(20)，會員子帳戶交易前可用餘額
注意：此欄位可能返回 null，表示取不到有效值。
        :type MemberSubAcctPreAvailBal: str
        :param ReservedMsgOne: STRING(300)，保留域1
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReservedMsgOne: str
        :param ReservedMsgTwo: STRING(300)，保留域2
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReservedMsgTwo: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.MemberSubAcctPreAvailBal = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.MemberSubAcctPreAvailBal = params.get("MemberSubAcctPreAvailBal")
        self.ReservedMsgOne = params.get("ReservedMsgOne")
        self.ReservedMsgTwo = params.get("ReservedMsgTwo")
        self.RequestId = params.get("RequestId")


class RefundOutSubOrderRefundList(AbstractModel):
    """退款子訂單清單

    """

    def __init__(self):
        """
        :param PlatformRefundAmt: 平台應退金額
        :type PlatformRefundAmt: int
        :param RefundAmt: 子訂單退款金額
        :type RefundAmt: int
        :param SubMchRefundAmt: 商家應退金額
        :type SubMchRefundAmt: int
        :param SubOutTradeNo: 子訂單号
        :type SubOutTradeNo: str
        :param SubRefundId: 子退款單号，調用方需要保證 全局唯一性
        :type SubRefundId: str
        """
        self.PlatformRefundAmt = None
        self.RefundAmt = None
        self.SubMchRefundAmt = None
        self.SubOutTradeNo = None
        self.SubRefundId = None


    def _deserialize(self, params):
        self.PlatformRefundAmt = params.get("PlatformRefundAmt")
        self.RefundAmt = params.get("RefundAmt")
        self.SubMchRefundAmt = params.get("SubMchRefundAmt")
        self.SubOutTradeNo = params.get("SubOutTradeNo")
        self.SubRefundId = params.get("SubRefundId")


class RefundRequest(AbstractModel):
    """Refund請求參數結構體

    """

    def __init__(self):
        """
        :param UserId: 用戶ID，長度不小於5位， 僅支援字母和數字的組合
        :type UserId: str
        :param RefundId: 退款訂單号，僅支援數字、 字母、下劃線（_）、橫杠字 符（-）、點（.）的組合
        :type RefundId: str
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param TotalRefundAmt: 退款金額，單位：分。備注：當該欄位爲空或者爲0 時，系統會預設使用訂單當 實付金額作爲退款金額
        :type TotalRefundAmt: int
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全金鑰計算的簽名
        :type MidasSignature: str
        :param OutTradeNo: 商品訂單，僅支援數字、字 母、下劃線（_）、橫杠字元 （-）、點（.）的組合。  OutTradeNo ,TransactionId 二選一,不能都爲空,優先使用 OutTradeNo
        :type OutTradeNo: str
        :param MchRefundAmt: 結算應收金額，單位：分
        :type MchRefundAmt: int
        :param TransactionId: 調用下單介面獲取的聚鑫交 易訂單。  OutTradeNo ,TransactionId 二選一,不能都爲空,優先使用 OutTradeNo
        :type TransactionId: str
        :param PlatformRefundAmt: 平台應收金額，單位：分
        :type PlatformRefundAmt: int
        :param SubOrderRefundList: 支援多個子訂單批次退款單 個子訂單退款支援傳 SubOutTradeNo ，也支援傳 SubOutTradeNoList ，都傳的時候以 SubOutTradeNoList 爲準。  如果傳了子單退款細節，外 部不需要再傳退款金額，平 台應退，商戶應退金額，我 們可以直接根據子單退款算出來總和。
        :type SubOrderRefundList: list of RefundOutSubOrderRefundList
        """
        self.UserId = None
        self.RefundId = None
        self.MidasAppId = None
        self.TotalRefundAmt = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.OutTradeNo = None
        self.MchRefundAmt = None
        self.TransactionId = None
        self.PlatformRefundAmt = None
        self.SubOrderRefundList = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.RefundId = params.get("RefundId")
        self.MidasAppId = params.get("MidasAppId")
        self.TotalRefundAmt = params.get("TotalRefundAmt")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.OutTradeNo = params.get("OutTradeNo")
        self.MchRefundAmt = params.get("MchRefundAmt")
        self.TransactionId = params.get("TransactionId")
        self.PlatformRefundAmt = params.get("PlatformRefundAmt")
        if params.get("SubOrderRefundList") is not None:
            self.SubOrderRefundList = []
            for item in params.get("SubOrderRefundList"):
                obj = RefundOutSubOrderRefundList()
                obj._deserialize(item)
                self.SubOrderRefundList.append(obj)


class RefundResponse(AbstractModel):
    """Refund返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegisterBillSupportWithdrawRequest(AbstractModel):
    """RegisterBillSupportWithdraw請求參數結構體

    """

    def __init__(self):
        """
        :param TranNetMemberCode: STRING(32)，交易網會員代碼
        :type TranNetMemberCode: str
        :param OrderNo: STRING(50)，訂單号
        :type OrderNo: str
        :param SuspendAmt: STRING(20)，挂賬金額（包含交易費用）
        :type SuspendAmt: str
        :param TranFee: STRING(20)，交易費用（暫未使用，預設傳0.0）
        :type TranFee: str
        :param MrchCode: String(22)，商戶号（簽約客戶号）
        :type MrchCode: str
        :param Remark: STRING(300)，備注
        :type Remark: str
        :param ReservedMsgOne: STRING(300)，保留域1
        :type ReservedMsgOne: str
        :param ReservedMsgTwo: STRING(300)，保留域2
        :type ReservedMsgTwo: str
        :param ReservedMsgThree: STRING(300)，保留域3
        :type ReservedMsgThree: str
        """
        self.TranNetMemberCode = None
        self.OrderNo = None
        self.SuspendAmt = None
        self.TranFee = None
        self.MrchCode = None
        self.Remark = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.ReservedMsgThree = None


    def _deserialize(self, params):
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.OrderNo = params.get("OrderNo")
        self.SuspendAmt = params.get("SuspendAmt")
        self.TranFee = params.get("TranFee")
        self.MrchCode = params.get("MrchCode")
        self.Remark = params.get("Remark")
        self.ReservedMsgOne = params.get("ReservedMsgOne")
        self.ReservedMsgTwo = params.get("ReservedMsgTwo")
        self.ReservedMsgThree = params.get("ReservedMsgThree")


class RegisterBillSupportWithdrawResponse(AbstractModel):
    """RegisterBillSupportWithdraw返回參數結構體

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回碼
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回訊息
        :type TxnReturnMsg: str
        :param FrontSeqNo: STRING(52)，見證系統流水号
注意：此欄位可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param CnsmrSeqNo: String(22)，交易流水号
注意：此欄位可能返回 null，表示取不到有效值。
        :type CnsmrSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.FrontSeqNo = None
        self.CnsmrSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class RevRegisterBillSupportWithdrawRequest(AbstractModel):
    """RevRegisterBillSupportWithdraw請求參數結構體

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商戶号（簽約客戶号）
        :type MrchCode: str
        :param TranNetMemberCode: STRING(32)，交易網會員代碼
        :type TranNetMemberCode: str
        :param OldOrderNo: STRING(30)，原訂單号（RegisterBillSupportWithdraw介面中的訂單号）
        :type OldOrderNo: str
        :param CancelAmt: STRING(20)，撤銷金額（支援部分撤銷，不能大于原訂單可用金額，包含交易費用）
        :type CancelAmt: str
        :param TranFee: STRING(20)，交易費用（暫未使用，預設傳0.0）
        :type TranFee: str
        :param Remark: STRING(300)，備注
        :type Remark: str
        :param ReservedMsgOne: STRING(300)，保留域1
        :type ReservedMsgOne: str
        :param ReservedMsgTwo: STRING(300)，保留域2
        :type ReservedMsgTwo: str
        :param ReservedMsgThree: STRING(300)，保留域3
        :type ReservedMsgThree: str
        """
        self.MrchCode = None
        self.TranNetMemberCode = None
        self.OldOrderNo = None
        self.CancelAmt = None
        self.TranFee = None
        self.Remark = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.ReservedMsgThree = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.OldOrderNo = params.get("OldOrderNo")
        self.CancelAmt = params.get("CancelAmt")
        self.TranFee = params.get("TranFee")
        self.Remark = params.get("Remark")
        self.ReservedMsgOne = params.get("ReservedMsgOne")
        self.ReservedMsgTwo = params.get("ReservedMsgTwo")
        self.ReservedMsgThree = params.get("ReservedMsgThree")


class RevRegisterBillSupportWithdrawResponse(AbstractModel):
    """RevRegisterBillSupportWithdraw返回參數結構體

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回碼
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回訊息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，見證系統流水号
注意：此欄位可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class RevResigterBillSupportWithdrawRequest(AbstractModel):
    """RevResigterBillSupportWithdraw請求參數結構體

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商戶号（簽約客戶号）
        :type MrchCode: str
        :param TranNetMemberCode: STRING(32)，交易網會員代碼
        :type TranNetMemberCode: str
        :param OldOrderNo: STRING(30)，原訂單号（RegisterBillSupportWithdraw介面中的訂單号）
        :type OldOrderNo: str
        :param CancelAmt: STRING(20)，撤銷金額（支援部分撤銷，不能大于原訂單可用金額，包含交易費用）
        :type CancelAmt: str
        :param TranFee: STRING(20)，交易費用（暫未使用，預設傳0.0）
        :type TranFee: str
        :param Remark: STRING(300)，備注
        :type Remark: str
        :param ReservedMsgOne: STRING(300)，保留域1
        :type ReservedMsgOne: str
        :param ReservedMsgTwo: STRING(300)，保留域2
        :type ReservedMsgTwo: str
        :param ReservedMsgThree: STRING(300)，保留域3
        :type ReservedMsgThree: str
        """
        self.MrchCode = None
        self.TranNetMemberCode = None
        self.OldOrderNo = None
        self.CancelAmt = None
        self.TranFee = None
        self.Remark = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.ReservedMsgThree = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.OldOrderNo = params.get("OldOrderNo")
        self.CancelAmt = params.get("CancelAmt")
        self.TranFee = params.get("TranFee")
        self.Remark = params.get("Remark")
        self.ReservedMsgOne = params.get("ReservedMsgOne")
        self.ReservedMsgTwo = params.get("ReservedMsgTwo")
        self.ReservedMsgThree = params.get("ReservedMsgThree")


class RevResigterBillSupportWithdrawResponse(AbstractModel):
    """RevResigterBillSupportWithdraw返回參數結構體

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回碼
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回訊息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，見證系統流水号
注意：此欄位可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class ReviseMbrPropertyRequest(AbstractModel):
    """ReviseMbrProperty請求參數結構體

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商戶号（簽約客戶号）
        :type MrchCode: str
        :param SubAcctNo: STRING(50)，見證子帳戶的賬号
        :type SubAcctNo: str
        :param MemberProperty: STRING(10)，會員屬性（00-普通子賬号; SH-商戶子帳戶。暫時只支援00-普通子賬号改爲SH-商戶子帳戶）
        :type MemberProperty: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.SubAcctNo = None
        self.MemberProperty = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.SubAcctNo = params.get("SubAcctNo")
        self.MemberProperty = params.get("MemberProperty")
        self.ReservedMsg = params.get("ReservedMsg")


class ReviseMbrPropertyResponse(AbstractModel):
    """ReviseMbrProperty返回參數結構體

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回碼
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回訊息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class RevokeMemberRechargeThirdPayRequest(AbstractModel):
    """RevokeMemberRechargeThirdPay請求參數結構體

    """

    def __init__(self):
        """
        :param OldFillFrontSeqNo: STRING(52)，原儲值的前置流水号
        :type OldFillFrontSeqNo: str
        :param OldFillPayChannelType: STRING(20)，原儲值的支付管道類型
        :type OldFillPayChannelType: str
        :param OldPayChannelTranSeqNo: STRING(52)，原儲值的支付管道交易流水号
        :type OldPayChannelTranSeqNo: str
        :param OldFillEjzbOrderNo: STRING(52)，原儲值的電商見證寶訂單号
        :type OldFillEjzbOrderNo: str
        :param ApplyCancelMemberAmt: STRING(20)，申請撤銷的會員金額
        :type ApplyCancelMemberAmt: str
        :param ApplyCancelCommission: STRING(20)，申請撤銷的手續約金額
        :type ApplyCancelCommission: str
        :param MrchCode: String(22)，商戶号
        :type MrchCode: str
        :param Remark: STRING(300)，備注
        :type Remark: str
        :param ReservedMsgOne: STRING(300)，保留域1
        :type ReservedMsgOne: str
        :param ReservedMsgTwo: STRING(300)，保留域2
        :type ReservedMsgTwo: str
        :param ReservedMsgThree: STRING(300)，保留域3
        :type ReservedMsgThree: str
        """
        self.OldFillFrontSeqNo = None
        self.OldFillPayChannelType = None
        self.OldPayChannelTranSeqNo = None
        self.OldFillEjzbOrderNo = None
        self.ApplyCancelMemberAmt = None
        self.ApplyCancelCommission = None
        self.MrchCode = None
        self.Remark = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.ReservedMsgThree = None


    def _deserialize(self, params):
        self.OldFillFrontSeqNo = params.get("OldFillFrontSeqNo")
        self.OldFillPayChannelType = params.get("OldFillPayChannelType")
        self.OldPayChannelTranSeqNo = params.get("OldPayChannelTranSeqNo")
        self.OldFillEjzbOrderNo = params.get("OldFillEjzbOrderNo")
        self.ApplyCancelMemberAmt = params.get("ApplyCancelMemberAmt")
        self.ApplyCancelCommission = params.get("ApplyCancelCommission")
        self.MrchCode = params.get("MrchCode")
        self.Remark = params.get("Remark")
        self.ReservedMsgOne = params.get("ReservedMsgOne")
        self.ReservedMsgTwo = params.get("ReservedMsgTwo")
        self.ReservedMsgThree = params.get("ReservedMsgThree")


class RevokeMemberRechargeThirdPayResponse(AbstractModel):
    """RevokeMemberRechargeThirdPay返回參數結構體

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回碼
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回訊息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，前置流水号
注意：此欄位可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param ReservedMsgOne: STRING(300)，保留域1
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReservedMsgOne: str
        :param ReservedMsgTwo: STRING(300)，保留域2
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReservedMsgTwo: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.ReservedMsgOne = None
        self.ReservedMsgTwo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.ReservedMsgOne = params.get("ReservedMsgOne")
        self.ReservedMsgTwo = params.get("ReservedMsgTwo")
        self.RequestId = params.get("RequestId")


class TranItem(AbstractModel):
    """交易訊息

    """

    def __init__(self):
        """
        :param FundSummaryAcctNo: STRING(50)，資金匯總賬号
注意：此欄位可能返回 null，表示取不到有效值。
        :type FundSummaryAcctNo: str
        :param SubAcctNo: STRING(50)，見證子帳戶的賬号
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubAcctNo: str
        :param TranNetMemberCode: STRING(32)，交易網會員代碼
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranNetMemberCode: str
        :param MemberName: STRING(150)，會員名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type MemberName: str
        :param MemberGlobalType: STRING(5)，會員證件類型（詳情見“常見問題”）
注意：此欄位可能返回 null，表示取不到有效值。
        :type MemberGlobalType: str
        :param MemberGlobalId: STRING(32)，會員證件号碼
注意：此欄位可能返回 null，表示取不到有效值。
        :type MemberGlobalId: str
        :param MemberAcctNo: STRING(50)，會員綁定帳戶的賬号（提現的銀行卡）
注意：此欄位可能返回 null，表示取不到有效值。
        :type MemberAcctNo: str
        :param BankType: STRING(10)，會員綁定帳戶的本他行類型（1: 本行; 2: 他行）
注意：此欄位可能返回 null，表示取不到有效值。
        :type BankType: str
        :param AcctOpenBranchName: STRING(150)，會員綁定帳戶的開戶行名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type AcctOpenBranchName: str
        :param CnapsBranchId: STRING(20)，會員綁定帳戶的開戶行的聯行号
注意：此欄位可能返回 null，表示取不到有效值。
        :type CnapsBranchId: str
        :param EiconBankBranchId: STRING(20)，會員綁定帳戶的開戶行的超級網銀行号
注意：此欄位可能返回 null，表示取不到有效值。
        :type EiconBankBranchId: str
        :param Mobile: STRING(30)，會員的手機号
注意：此欄位可能返回 null，表示取不到有效值。
        :type Mobile: str
        """
        self.FundSummaryAcctNo = None
        self.SubAcctNo = None
        self.TranNetMemberCode = None
        self.MemberName = None
        self.MemberGlobalType = None
        self.MemberGlobalId = None
        self.MemberAcctNo = None
        self.BankType = None
        self.AcctOpenBranchName = None
        self.CnapsBranchId = None
        self.EiconBankBranchId = None
        self.Mobile = None


    def _deserialize(self, params):
        self.FundSummaryAcctNo = params.get("FundSummaryAcctNo")
        self.SubAcctNo = params.get("SubAcctNo")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberName = params.get("MemberName")
        self.MemberGlobalType = params.get("MemberGlobalType")
        self.MemberGlobalId = params.get("MemberGlobalId")
        self.MemberAcctNo = params.get("MemberAcctNo")
        self.BankType = params.get("BankType")
        self.AcctOpenBranchName = params.get("AcctOpenBranchName")
        self.CnapsBranchId = params.get("CnapsBranchId")
        self.EiconBankBranchId = params.get("EiconBankBranchId")
        self.Mobile = params.get("Mobile")


class TransactionItem(AbstractModel):
    """交易明細訊息

    """

    def __init__(self):
        """
        :param BookingFlag: STRING(2)，記賬标志（1: 轉出; 2: 轉入）
注意：此欄位可能返回 null，表示取不到有效值。
        :type BookingFlag: str
        :param TranStatus: STRING(32)，交易狀态（0: 成功）
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranStatus: str
        :param TranAmt: STRING(20)，交易金額
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranAmt: str
        :param TranDate: STRING(8)，交易日期
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranDate: str
        :param TranTime: STRING(20)，交易時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranTime: str
        :param FrontSeqNo: STRING(52)，見證系統流水号
注意：此欄位可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param BookingType: STRING(20)，記賬類型（詳情見“常見問題”）
注意：此欄位可能返回 null，表示取不到有效值。
        :type BookingType: str
        :param InSubAcctNo: STRING(50)，轉入見證子帳戶的帳号
注意：此欄位可能返回 null，表示取不到有效值。
        :type InSubAcctNo: str
        :param OutSubAcctNo: STRING(50)，轉出見證子帳戶的帳号
注意：此欄位可能返回 null，表示取不到有效值。
        :type OutSubAcctNo: str
        :param Remark: STRING(300)，備注（返回交易訂單号）
注意：此欄位可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self.BookingFlag = None
        self.TranStatus = None
        self.TranAmt = None
        self.TranDate = None
        self.TranTime = None
        self.FrontSeqNo = None
        self.BookingType = None
        self.InSubAcctNo = None
        self.OutSubAcctNo = None
        self.Remark = None


    def _deserialize(self, params):
        self.BookingFlag = params.get("BookingFlag")
        self.TranStatus = params.get("TranStatus")
        self.TranAmt = params.get("TranAmt")
        self.TranDate = params.get("TranDate")
        self.TranTime = params.get("TranTime")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.BookingType = params.get("BookingType")
        self.InSubAcctNo = params.get("InSubAcctNo")
        self.OutSubAcctNo = params.get("OutSubAcctNo")
        self.Remark = params.get("Remark")


class TransferItem(AbstractModel):
    """轉賬儲值明細訊息

    """

    def __init__(self):
        """
        :param InAcctType: STRING(10)，入賬類型（02: 會員儲值; 03: 資金挂賬）
注意：此欄位可能返回 null，表示取不到有效值。
        :type InAcctType: str
        :param TranNetMemberCode: STRING(32)，交易網會員代碼
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranNetMemberCode: str
        :param SubAcctNo: STRING(50)，見證子帳戶的帳号
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubAcctNo: str
        :param TranAmt: STRING(20)，入金金額
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranAmt: str
        :param InAcctNo: STRING(50)，入金賬号
注意：此欄位可能返回 null，表示取不到有效值。
        :type InAcctNo: str
        :param InAcctName: STRING(150)，入金帳戶名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type InAcctName: str
        :param Ccy: STRING(3)，币種
注意：此欄位可能返回 null，表示取不到有效值。
        :type Ccy: str
        :param AccountingDate: STRING(8)，會計日期（即銀行主機記賬日期）
注意：此欄位可能返回 null，表示取不到有效值。
        :type AccountingDate: str
        :param BankName: STRING(150)，銀行名稱（付款帳戶銀行名稱）
注意：此欄位可能返回 null，表示取不到有效值。
        :type BankName: str
        :param Remark: STRING(300)，轉賬備注
注意：此欄位可能返回 null，表示取不到有效值。
        :type Remark: str
        :param FrontSeqNo: STRING(52)，見證系統流水号
注意：此欄位可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        """
        self.InAcctType = None
        self.TranNetMemberCode = None
        self.SubAcctNo = None
        self.TranAmt = None
        self.InAcctNo = None
        self.InAcctName = None
        self.Ccy = None
        self.AccountingDate = None
        self.BankName = None
        self.Remark = None
        self.FrontSeqNo = None


    def _deserialize(self, params):
        self.InAcctType = params.get("InAcctType")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.SubAcctNo = params.get("SubAcctNo")
        self.TranAmt = params.get("TranAmt")
        self.InAcctNo = params.get("InAcctNo")
        self.InAcctName = params.get("InAcctName")
        self.Ccy = params.get("Ccy")
        self.AccountingDate = params.get("AccountingDate")
        self.BankName = params.get("BankName")
        self.Remark = params.get("Remark")
        self.FrontSeqNo = params.get("FrontSeqNo")


class UnBindAcctRequest(AbstractModel):
    """UnBindAcct請求參數結構體

    """

    def __init__(self):
        """
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param SubAppId: 聚鑫計費SubAppId，代表子商戶
        :type SubAppId: str
        :param SettleAcctNo: 用于提現
<敏感訊息>加密詳見《商戶端介面敏感訊息加密說明》
        :type SettleAcctNo: str
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全金鑰計算的簽名
        :type MidasSignature: str
        """
        self.MidasAppId = None
        self.SubAppId = None
        self.SettleAcctNo = None
        self.MidasSecretId = None
        self.MidasSignature = None


    def _deserialize(self, params):
        self.MidasAppId = params.get("MidasAppId")
        self.SubAppId = params.get("SubAppId")
        self.SettleAcctNo = params.get("SettleAcctNo")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")


class UnBindAcctResponse(AbstractModel):
    """UnBindAcct返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnbindRelateAcctRequest(AbstractModel):
    """UnbindRelateAcct請求參數結構體

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商戶号（簽約客戶号）
        :type MrchCode: str
        :param FunctionFlag: STRING(2)，功能标志（1: 解綁）
        :type FunctionFlag: str
        :param TranNetMemberCode: STRING(32)，交易網會員代碼（若需要把一個待綁定帳戶關聯到兩個會員名下，此欄位可上送兩個會員的交易網代碼，并且須用“|::|”(右側)進行分隔）
        :type TranNetMemberCode: str
        :param MemberAcctNo: STRING(50)，待解綁的提現帳戶的賬号（提現賬号）
        :type MemberAcctNo: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        """
        self.MrchCode = None
        self.FunctionFlag = None
        self.TranNetMemberCode = None
        self.MemberAcctNo = None
        self.ReservedMsg = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.FunctionFlag = params.get("FunctionFlag")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberAcctNo = params.get("MemberAcctNo")
        self.ReservedMsg = params.get("ReservedMsg")


class UnbindRelateAcctResponse(AbstractModel):
    """UnbindRelateAcct返回參數結構體

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回碼
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回訊息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，見證系統流水号（即電商見證寶系統生成的流水号，可關聯具體一筆請求）
注意：此欄位可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class UnifiedOrderInSubOrderList(AbstractModel):
    """子訂單清單

    """

    def __init__(self):
        """
        :param SubMchIncome: 子訂單結算應收金額，單位： 分
        :type SubMchIncome: int
        :param PlatformIncome: 子訂單平台應收金額，單位：分
        :type PlatformIncome: int
        :param ProductDetail: 子訂單商品詳情
        :type ProductDetail: str
        :param ProductName: 子訂單商品名稱
        :type ProductName: str
        :param SubAppId: 聚鑫計費SubAppId，代表子商戶
        :type SubAppId: str
        :param SubOutTradeNo: 子訂單号
        :type SubOutTradeNo: str
        :param Amt: 子訂單支付金額
        :type Amt: int
        :param Metadata: 發貨标識，由業務在調用聚鑫下單介面的 時候下發
        :type Metadata: str
        :param OriginalAmt: 子訂單原始金額
        :type OriginalAmt: int
        """
        self.SubMchIncome = None
        self.PlatformIncome = None
        self.ProductDetail = None
        self.ProductName = None
        self.SubAppId = None
        self.SubOutTradeNo = None
        self.Amt = None
        self.Metadata = None
        self.OriginalAmt = None


    def _deserialize(self, params):
        self.SubMchIncome = params.get("SubMchIncome")
        self.PlatformIncome = params.get("PlatformIncome")
        self.ProductDetail = params.get("ProductDetail")
        self.ProductName = params.get("ProductName")
        self.SubAppId = params.get("SubAppId")
        self.SubOutTradeNo = params.get("SubOutTradeNo")
        self.Amt = params.get("Amt")
        self.Metadata = params.get("Metadata")
        self.OriginalAmt = params.get("OriginalAmt")


class UnifiedOrderRequest(AbstractModel):
    """UnifiedOrder請求參數結構體

    """

    def __init__(self):
        """
        :param CurrencyType: ISO 貨币代碼，CNY
        :type CurrencyType: str
        :param MidasAppId: 聚鑫分配的支付主MidasAppId
        :type MidasAppId: str
        :param OutTradeNo: 支付訂單号，僅支援數字、字母、下劃線（_）、橫杠字元（-）、點（.）的組合
        :type OutTradeNo: str
        :param ProductDetail: 商品詳情，需要URL編碼
        :type ProductDetail: str
        :param ProductId: 商品ID，僅支援數字、字母、下劃線（_）、橫杠字元（-）、點（.）的組合
        :type ProductId: str
        :param ProductName: 商品名稱，需要URL編碼
        :type ProductName: str
        :param TotalAmt: 支付金額，單位： 分
        :type TotalAmt: int
        :param UserId: 用戶ID，長度不小於5位，僅支援字母和數字的組合
        :type UserId: str
        :param RealChannel: 銀行真實管道.如:bank_pingan
        :type RealChannel: str
        :param OriginalAmt: 原始金額
        :type OriginalAmt: int
        :param MidasSecretId: 聚鑫分配的安全ID
        :type MidasSecretId: str
        :param MidasSignature: 按照聚鑫安全金鑰計算的簽名
        :type MidasSignature: str
        :param CallbackUrl: Web端回調網址
        :type CallbackUrl: str
        :param Channel: 指定支付管道：  wechat：微信支付  qqwallet：QQ錢包 
 bank：網銀支付  只有一個管道時需要指定
        :type Channel: str
        :param Metadata: 透傳欄位，支付成功回調透傳給應用，用于業務透傳自定義内容
        :type Metadata: str
        :param Quantity: 購買數量，不傳預設爲1
        :type Quantity: int
        :param SubAppId: 聚鑫計費SubAppId，代表子商戶
        :type SubAppId: str
        :param SubOrderList: 子訂單訊息清單，格式：子訂單号、子應用ID、金額。 壓縮後最長不可超過65535位元(去除空格，換行，制表符等無意義字元)
注：接入銀行或其他支付管道服務商模式下，必傳
        :type SubOrderList: list of UnifiedOrderInSubOrderList
        :param TotalMchIncome: 結算應收金額，單位：分
        :type TotalMchIncome: int
        :param TotalPlatformIncome: 平台應收金額，單位：分
        :type TotalPlatformIncome: int
        :param WxOpenId: 微信公衆号/小程式支付時爲必選，需要傳微信下的openid
        :type WxOpenId: str
        :param WxSubOpenId: 在服務商模式下，微信公衆号/小程式支付時wx_sub_openid和wx_openid二選一
        :type WxSubOpenId: str
        """
        self.CurrencyType = None
        self.MidasAppId = None
        self.OutTradeNo = None
        self.ProductDetail = None
        self.ProductId = None
        self.ProductName = None
        self.TotalAmt = None
        self.UserId = None
        self.RealChannel = None
        self.OriginalAmt = None
        self.MidasSecretId = None
        self.MidasSignature = None
        self.CallbackUrl = None
        self.Channel = None
        self.Metadata = None
        self.Quantity = None
        self.SubAppId = None
        self.SubOrderList = None
        self.TotalMchIncome = None
        self.TotalPlatformIncome = None
        self.WxOpenId = None
        self.WxSubOpenId = None


    def _deserialize(self, params):
        self.CurrencyType = params.get("CurrencyType")
        self.MidasAppId = params.get("MidasAppId")
        self.OutTradeNo = params.get("OutTradeNo")
        self.ProductDetail = params.get("ProductDetail")
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.TotalAmt = params.get("TotalAmt")
        self.UserId = params.get("UserId")
        self.RealChannel = params.get("RealChannel")
        self.OriginalAmt = params.get("OriginalAmt")
        self.MidasSecretId = params.get("MidasSecretId")
        self.MidasSignature = params.get("MidasSignature")
        self.CallbackUrl = params.get("CallbackUrl")
        self.Channel = params.get("Channel")
        self.Metadata = params.get("Metadata")
        self.Quantity = params.get("Quantity")
        self.SubAppId = params.get("SubAppId")
        if params.get("SubOrderList") is not None:
            self.SubOrderList = []
            for item in params.get("SubOrderList"):
                obj = UnifiedOrderInSubOrderList()
                obj._deserialize(item)
                self.SubOrderList.append(obj)
        self.TotalMchIncome = params.get("TotalMchIncome")
        self.TotalPlatformIncome = params.get("TotalPlatformIncome")
        self.WxOpenId = params.get("WxOpenId")
        self.WxSubOpenId = params.get("WxSubOpenId")


class UnifiedOrderResponse(AbstractModel):
    """UnifiedOrder返回參數結構體

    """

    def __init__(self):
        """
        :param TotalAmt: 支付金額，單位： 分
        :type TotalAmt: int
        :param OutTradeNo: 應用支付訂單号
        :type OutTradeNo: str
        :param PayInfo: 支付參數透傳給聚鑫SDK（原文透傳給SDK即可，不需要解碼）
        :type PayInfo: str
        :param TransactionId: 聚鑫的交易訂單
        :type TransactionId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalAmt = None
        self.OutTradeNo = None
        self.PayInfo = None
        self.TransactionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalAmt = params.get("TotalAmt")
        self.OutTradeNo = params.get("OutTradeNo")
        self.PayInfo = params.get("PayInfo")
        self.TransactionId = params.get("TransactionId")
        self.RequestId = params.get("RequestId")


class WithdrawBill(AbstractModel):
    """聚鑫提現訂單内容

    """

    def __init__(self):
        """
        :param WithdrawOrderId: 業務提現訂單号
        :type WithdrawOrderId: str
        :param Date: 提現日期
        :type Date: str
        :param PayAmt: 提現金額，單位： 分
        :type PayAmt: str
        :param InSubAppId: 聚鑫分配轉入帳戶appid
        :type InSubAppId: str
        :param OutSubAppId: 聚鑫分配轉出帳戶appid
        :type OutSubAppId: str
        :param CurrencyType: ISO貨币代碼
        :type CurrencyType: str
        :param MetaData: 透傳欄位
        :type MetaData: str
        :param ExtendFieldData: 擴展欄位
        :type ExtendFieldData: str
        """
        self.WithdrawOrderId = None
        self.Date = None
        self.PayAmt = None
        self.InSubAppId = None
        self.OutSubAppId = None
        self.CurrencyType = None
        self.MetaData = None
        self.ExtendFieldData = None


    def _deserialize(self, params):
        self.WithdrawOrderId = params.get("WithdrawOrderId")
        self.Date = params.get("Date")
        self.PayAmt = params.get("PayAmt")
        self.InSubAppId = params.get("InSubAppId")
        self.OutSubAppId = params.get("OutSubAppId")
        self.CurrencyType = params.get("CurrencyType")
        self.MetaData = params.get("MetaData")
        self.ExtendFieldData = params.get("ExtendFieldData")


class WithdrawCashMembershipRequest(AbstractModel):
    """WithdrawCashMembership請求參數結構體

    """

    def __init__(self):
        """
        :param MrchCode: String(22)，商戶号（簽約客戶号）
        :type MrchCode: str
        :param TranWebName: STRING(150)，交易網名稱（市場名稱）
        :type TranWebName: str
        :param MemberGlobalType: STRING(5)，會員證件類型（詳情見“常見問題”）
        :type MemberGlobalType: str
        :param MemberGlobalId: STRING(32)，會員證件号碼
        :type MemberGlobalId: str
        :param TranNetMemberCode: STRING(32)，交易網會員代碼
        :type TranNetMemberCode: str
        :param MemberName: STRING(150)，會員名稱
        :type MemberName: str
        :param TakeCashAcctNo: STRING(50)，提現賬号（銀行卡）
        :type TakeCashAcctNo: str
        :param OutAmtAcctName: STRING(150)，出金帳戶名稱（銀行卡戶名）
        :type OutAmtAcctName: str
        :param Ccy: STRING(3)，币種（預設爲RMB）
        :type Ccy: str
        :param CashAmt: STRING(20)，可提現金額
        :type CashAmt: str
        :param Remark: STRING(300)，備注（建議可送訂單号，可在對賬文件的備注欄位獲取到）
        :type Remark: str
        :param ReservedMsg: STRING(1027)，保留域
        :type ReservedMsg: str
        :param WebSign: STRING(300)，網銀簽名
        :type WebSign: str
        """
        self.MrchCode = None
        self.TranWebName = None
        self.MemberGlobalType = None
        self.MemberGlobalId = None
        self.TranNetMemberCode = None
        self.MemberName = None
        self.TakeCashAcctNo = None
        self.OutAmtAcctName = None
        self.Ccy = None
        self.CashAmt = None
        self.Remark = None
        self.ReservedMsg = None
        self.WebSign = None


    def _deserialize(self, params):
        self.MrchCode = params.get("MrchCode")
        self.TranWebName = params.get("TranWebName")
        self.MemberGlobalType = params.get("MemberGlobalType")
        self.MemberGlobalId = params.get("MemberGlobalId")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.MemberName = params.get("MemberName")
        self.TakeCashAcctNo = params.get("TakeCashAcctNo")
        self.OutAmtAcctName = params.get("OutAmtAcctName")
        self.Ccy = params.get("Ccy")
        self.CashAmt = params.get("CashAmt")
        self.Remark = params.get("Remark")
        self.ReservedMsg = params.get("ReservedMsg")
        self.WebSign = params.get("WebSign")


class WithdrawCashMembershipResponse(AbstractModel):
    """WithdrawCashMembership返回參數結構體

    """

    def __init__(self):
        """
        :param TxnReturnCode: String(20)，返回碼
        :type TxnReturnCode: str
        :param TxnReturnMsg: String(100)，返回訊息
        :type TxnReturnMsg: str
        :param CnsmrSeqNo: String(22)，交易流水号
        :type CnsmrSeqNo: str
        :param FrontSeqNo: STRING(52)，見證系統流水号
注意：此欄位可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param TransferFee: STRING(20)，轉賬手續約（固定返回0.00）
注意：此欄位可能返回 null，表示取不到有效值。
        :type TransferFee: str
        :param ReservedMsg: STRING(1027)，保留域
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReservedMsg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TxnReturnCode = None
        self.TxnReturnMsg = None
        self.CnsmrSeqNo = None
        self.FrontSeqNo = None
        self.TransferFee = None
        self.ReservedMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxnReturnCode = params.get("TxnReturnCode")
        self.TxnReturnMsg = params.get("TxnReturnMsg")
        self.CnsmrSeqNo = params.get("CnsmrSeqNo")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.TransferFee = params.get("TransferFee")
        self.ReservedMsg = params.get("ReservedMsg")
        self.RequestId = params.get("RequestId")


class WithdrawItem(AbstractModel):
    """清分提現明細訊息

    """

    def __init__(self):
        """
        :param BookingFlag: STRING(2)，記賬标志（01: 提現; 02: 清分 ）
注意：此欄位可能返回 null，表示取不到有效值。
        :type BookingFlag: str
        :param TranStatus: STRING(32)，交易狀态（0: 成功）
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranStatus: str
        :param BookingMsg: STRING(200)，記賬說明
注意：此欄位可能返回 null，表示取不到有效值。
        :type BookingMsg: str
        :param TranNetMemberCode: STRING(32)，交易網會員代碼
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranNetMemberCode: str
        :param SubAcctNo: STRING(50)，見證子帳戶的帳号
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubAcctNo: str
        :param SubAcctName: STRING(150)，見證子帳戶的名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubAcctName: str
        :param TranAmt: STRING(20)，交易金額
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranAmt: str
        :param Commission: STRING(20)，手續約
注意：此欄位可能返回 null，表示取不到有效值。
        :type Commission: str
        :param TranDate: STRING(8)，交易日期
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranDate: str
        :param TranTime: STRING(20)，交易時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranTime: str
        :param FrontSeqNo: STRING(52)，見證系統流水号
注意：此欄位可能返回 null，表示取不到有效值。
        :type FrontSeqNo: str
        :param Remark: STRING(300)，備注
注意：此欄位可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self.BookingFlag = None
        self.TranStatus = None
        self.BookingMsg = None
        self.TranNetMemberCode = None
        self.SubAcctNo = None
        self.SubAcctName = None
        self.TranAmt = None
        self.Commission = None
        self.TranDate = None
        self.TranTime = None
        self.FrontSeqNo = None
        self.Remark = None


    def _deserialize(self, params):
        self.BookingFlag = params.get("BookingFlag")
        self.TranStatus = params.get("TranStatus")
        self.BookingMsg = params.get("BookingMsg")
        self.TranNetMemberCode = params.get("TranNetMemberCode")
        self.SubAcctNo = params.get("SubAcctNo")
        self.SubAcctName = params.get("SubAcctName")
        self.TranAmt = params.get("TranAmt")
        self.Commission = params.get("Commission")
        self.TranDate = params.get("TranDate")
        self.TranTime = params.get("TranTime")
        self.FrontSeqNo = params.get("FrontSeqNo")
        self.Remark = params.get("Remark")