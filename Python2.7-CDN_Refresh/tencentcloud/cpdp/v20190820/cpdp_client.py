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

import json

from taifucloudcloud.common.exception.taifucloud_cloud_sdk_exception import TencentCloudSDKException
from taifucloudcloud.common.abstract_client import AbstractClient
from taifucloudcloud.cpdp.v20190820 import models


class CpdpClient(AbstractClient):
    _apiVersion = '2019-08-20'
    _endpoint = 'cpdp.taifucloudcloudapi.com'


    def ApplyApplicationMaterial(self, request):
        """跨境-提交申報材料

        :param request: Request instance for ApplyApplicationMaterial.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.ApplyApplicationMaterialRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.ApplyApplicationMaterialResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ApplyApplicationMaterial", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplyApplicationMaterialResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ApplyOutwardOrder(self, request):
        """跨境-匯出指令申請

        :param request: Request instance for ApplyOutwardOrder.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.ApplyOutwardOrderRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.ApplyOutwardOrderResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ApplyOutwardOrder", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplyOutwardOrderResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ApplyPayerInfo(self, request):
        """跨境-付款人申請

        :param request: Request instance for ApplyPayerInfo.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.ApplyPayerInfoRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.ApplyPayerInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ApplyPayerInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplyPayerInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ApplyReWithdrawal(self, request):
        """正常結算提現失敗情況下，發起重新提現的請求介面

        :param request: Request instance for ApplyReWithdrawal.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.ApplyReWithdrawalRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.ApplyReWithdrawalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ApplyReWithdrawal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplyReWithdrawalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ApplyTrade(self, request):
        """跨境-提交貿易材料

        :param request: Request instance for ApplyTrade.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.ApplyTradeRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.ApplyTradeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ApplyTrade", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplyTradeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ApplyWithdrawal(self, request):
        """商戶提現

        :param request: Request instance for ApplyWithdrawal.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.ApplyWithdrawalRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.ApplyWithdrawalResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ApplyWithdrawal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplyWithdrawalResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindAcct(self, request):
        """商戶綁定提現銀行卡，每個商戶只能綁定一張提現銀行卡

        :param request: Request instance for BindAcct.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.BindAcctRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.BindAcctResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindAcct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindAcctResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindRelateAccReUnionPay(self, request):
        """會員綁定提現帳戶-回填銀聯鑒權簡訊碼。用於會員填寫動态驗證碼後，發往銀行進行驗證，驗證成功則完成綁定。

        :param request: Request instance for BindRelateAccReUnionPay.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.BindRelateAccReUnionPayRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.BindRelateAccReUnionPayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindRelateAccReUnionPay", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindRelateAccReUnionPayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindRelateAcctSmallAmount(self, request):
        """會員綁定提現帳戶-小額鑒權。會員申請綁定提現帳戶，綁定後從會員子帳戶中提現到綁定帳戶。
        轉賬鑒權有兩種形式：往賬鑒權和來賬鑒權。
        往賬鑒權：該介面發起成功後，銀行會向提現帳戶轉入小於等於0.5元的随機金額，並簡訊通知客戶檢視，客戶檢視後，需将收到的金額大小，在電商平台頁面上回填，並通知銀行。銀行驗證通過後，完成提現帳戶綁定。
        來賬鑒權：該介面發起成功後，銀行以簡訊通知客戶檢視，客戶檢視後，需通過待綁定的帳戶往市場的監管帳戶轉入簡訊上指定的金額。銀行檢索到該筆指定金額的來賬是源自待綁定帳戶，則綁定成功。平安銀行的帳戶，即BankType送1時，大小額行號和超級網銀號都不用送。

        :param request: Request instance for BindRelateAcctSmallAmount.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.BindRelateAcctSmallAmountRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.BindRelateAcctSmallAmountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindRelateAcctSmallAmount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindRelateAcctSmallAmountResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindRelateAcctUnionPay(self, request):
        """會員綁定提現帳戶-銀聯鑒權。用於會員申請綁定提現帳戶，申請後銀行前往銀聯驗證卡訊息：姓名、證件、卡號、銀行預留手機是否相符，相符則發送給會員手機動态驗證碼並返回成功，不相符則返回失敗。
        平台接收到銀行返回成功後，進入輸入動态驗證碼的頁面，有效期120秒，若120秒未輸入，客戶可點擊重新發送動态驗證碼，這個步驟重新調用該介面即可。
        平安銀行的帳戶，大小額行號和超級網銀號都不用送。
        超級網銀號：單筆轉賬金額不超過5萬，不限制筆數，只用選XX銀行，不用具體到支行，可實時知道對方是否收款成功。
        大小額聯行號：單筆轉賬可超過5萬，需具體到支行，不能實時知道對方是否收款成功。金額超過5萬的，在工作日的8點30-17點間才會成功。

        :param request: Request instance for BindRelateAcctUnionPay.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.BindRelateAcctUnionPayRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.BindRelateAcctUnionPayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindRelateAcctUnionPay", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindRelateAcctUnionPayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckAcct(self, request):
        """商戶綁定提現銀行卡的驗證介面

        :param request: Request instance for CheckAcct.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.CheckAcctRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.CheckAcctResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckAcct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckAcctResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckAmount(self, request):
        """驗證鑒權金額。此介面可受理BindRelateAcctSmallAmount介面發起的轉賬金額（往賬鑒權方式）的驗證處理。若所回填的驗證金額驗證通過，則會綁定原申請中的銀行帳戶作爲提現帳戶。通過此介面也可以查得BindRelateAcctSmallAmount介面發起的來賬鑒權方式的申請的當前狀态。

        :param request: Request instance for CheckAmount.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.CheckAmountRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.CheckAmountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckAmount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckAmountResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CloseOrder(self, request):
        """通過此介面關閉此前已創建的訂單，關閉後，用戶将無法繼續付款。僅能關閉創建後未支付的訂單

        :param request: Request instance for CloseOrder.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.CloseOrderRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.CloseOrderResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CloseOrder", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CloseOrderResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAcct(self, request):
        """子商戶入駐聚鑫平台

        :param request: Request instance for CreateAcct.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.CreateAcctRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.CreateAcctResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAcct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAcctResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCustAcctId(self, request):
        """會員子帳戶開立。會員在銀行注冊，並開立會員子帳戶，交易網會員代碼即會員在平台端系統的會員編號。
        平台需保存銀行返回的子帳戶賬號，後續交易介面都會用到。會員屬性欄位爲預留擴展欄位，當前必須送預設值。

        :param request: Request instance for CreateCustAcctId.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.CreateCustAcctIdRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.CreateCustAcctIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCustAcctId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCustAcctIdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateInvoice(self, request):
        """智慧零售-發票開具

        :param request: Request instance for CreateInvoice.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.CreateInvoiceRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.CreateInvoiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateInvoice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateInvoiceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateMerchant(self, request):
        """智慧零售-商戶注冊

        :param request: Request instance for CreateMerchant.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.CreateMerchantRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.CreateMerchantResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMerchant", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMerchantResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateRedInvoice(self, request):
        """智慧零售-發票紅沖

        :param request: Request instance for CreateRedInvoice.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.CreateRedInvoiceRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.CreateRedInvoiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateRedInvoice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRedInvoiceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DownloadBill(self, request):
        """帳單下載介面，根據本介面返回的URL網址，在D+1日下載對帳單。注意，本介面返回的URL網址有時效，請盡快下載。URL超時時效後，請重新調用本介面再次獲取。

        :param request: Request instance for DownloadBill.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.DownloadBillRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.DownloadBillResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DownloadBill", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DownloadBillResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyMntMbrBindRelateAcctBankCode(self, request):
        """維護會員綁定提現帳戶聯行號。此介面可以支援市場修改會員的提現帳戶的開戶行訊息，具體包括開戶行行名、開戶行的銀行聯行號（大小額聯行號）和超級網銀行號。

        :param request: Request instance for ModifyMntMbrBindRelateAcctBankCode.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.ModifyMntMbrBindRelateAcctBankCodeRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.ModifyMntMbrBindRelateAcctBankCodeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMntMbrBindRelateAcctBankCode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMntMbrBindRelateAcctBankCodeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryAcctBinding(self, request):
        """聚鑫-查詢子帳戶綁定銀行卡

        :param request: Request instance for QueryAcctBinding.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.QueryAcctBindingRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.QueryAcctBindingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryAcctBinding", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryAcctBindingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryAcctInfo(self, request):
        """聚鑫-開戶訊息查詢

        :param request: Request instance for QueryAcctInfo.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.QueryAcctInfoRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.QueryAcctInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryAcctInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryAcctInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryAcctInfoList(self, request):
        """聚鑫-開戶訊息清單查詢, 查詢某一段時間的開戶訊息

        :param request: Request instance for QueryAcctInfoList.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.QueryAcctInfoListRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.QueryAcctInfoListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryAcctInfoList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryAcctInfoListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryApplicationMaterial(self, request):
        """跨境-成功申報材料查詢

        :param request: Request instance for QueryApplicationMaterial.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.QueryApplicationMaterialRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.QueryApplicationMaterialResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryApplicationMaterial", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryApplicationMaterialResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryBalance(self, request):
        """子商戶餘額查詢

        :param request: Request instance for QueryBalance.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.QueryBalanceRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.QueryBalanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryBalance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryBalanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryBankClear(self, request):
        """查詢銀行在途清算結果。查詢時間段内交易網的在途清算結果。

        :param request: Request instance for QueryBankClear.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.QueryBankClearRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.QueryBankClearResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryBankClear", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryBankClearResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryBankTransactionDetails(self, request):
        """查詢銀行時間段内交易明細。查詢時間段的會員成功交易。

        :param request: Request instance for QueryBankTransactionDetails.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.QueryBankTransactionDetailsRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.QueryBankTransactionDetailsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryBankTransactionDetails", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryBankTransactionDetailsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryBankWithdrawCashDetails(self, request):
        """查詢銀行時間段内清分提現明細。查詢銀行時間段内清分提現明細介面：若爲“見證+收單退款”“見證+收單儲值”記錄時備注Note爲“見證+收單儲值,訂單號”“見證+收單退款,訂單號”，此介面可以查到T0/T1的儲值明細和退款記錄。查詢標志：儲值記錄仍用3清分選項查詢，退款記錄同提現用2選項查詢。

        :param request: Request instance for QueryBankWithdrawCashDetails.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.QueryBankWithdrawCashDetailsRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.QueryBankWithdrawCashDetailsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryBankWithdrawCashDetails", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryBankWithdrawCashDetailsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryCommonTransferRecharge(self, request):
        """查詢普通轉賬儲值明細。介面用於查詢會員主動轉賬進資金匯總帳戶的明細情況。若會員使用綁定賬號轉入，則直接入賬到會員子帳戶。若未使用綁定賬號轉入，則系統無法自動清分到對應子帳戶，則轉入挂賬子帳戶由平台自行清分。若是 “見證+收單儲值”T0儲值記錄時備注Note爲“見證+收單儲值,訂單號” 此介面可以查到T0到賬的“見證+收單儲值”儲值記錄。

        :param request: Request instance for QueryCommonTransferRecharge.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.QueryCommonTransferRechargeRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.QueryCommonTransferRechargeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryCommonTransferRecharge", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryCommonTransferRechargeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryCustAcctIdBalance(self, request):
        """查詢銀行子帳戶餘額。查詢會員子帳戶以及平台的功能子帳戶的餘額。

        :param request: Request instance for QueryCustAcctIdBalance.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.QueryCustAcctIdBalanceRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.QueryCustAcctIdBalanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryCustAcctIdBalance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryCustAcctIdBalanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryExchangeRate(self, request):
        """跨境-查詢匯率

        :param request: Request instance for QueryExchangeRate.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.QueryExchangeRateRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.QueryExchangeRateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryExchangeRate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryExchangeRateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryInvoice(self, request):
        """智慧零售-發票查詢

        :param request: Request instance for QueryInvoice.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.QueryInvoiceRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.QueryInvoiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryInvoice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryInvoiceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryMemberBind(self, request):
        """會員綁定訊息查詢。查詢標志爲“單個會員”的情況下，返回該會員的有效的綁定帳戶訊息。
        查詢標志爲“全部會員”的情況下，返回市場下的全部的有效的綁定帳戶訊息。查詢標志爲“單個會員的證件訊息”的情況下，返回市場下的指定的會員的留存在電商見證寶系統的證件訊息。

        :param request: Request instance for QueryMemberBind.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.QueryMemberBindRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.QueryMemberBindResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryMemberBind", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryMemberBindResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryMemberTransaction(self, request):
        """會員間交易-不驗證。此介面可以實現會員間的餘額的交易，實現資金在會員之間流動。

        :param request: Request instance for QueryMemberTransaction.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.QueryMemberTransactionRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.QueryMemberTransactionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryMemberTransaction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryMemberTransactionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryMerchantBalance(self, request):
        """跨境-對接方帳戶餘額查詢

        :param request: Request instance for QueryMerchantBalance.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.QueryMerchantBalanceRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.QueryMerchantBalanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryMerchantBalance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryMerchantBalanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryOrder(self, request):
        """根據訂單號，或者用戶Id，查詢支付訂單狀态

        :param request: Request instance for QueryOrder.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.QueryOrderRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.QueryOrderResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryOrder", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryOrderResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryOutwardOrder(self, request):
        """跨境-查詢匯出結果

        :param request: Request instance for QueryOutwardOrder.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.QueryOutwardOrderRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.QueryOutwardOrderResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryOutwardOrder", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryOutwardOrderResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryPayerInfo(self, request):
        """跨境-付款人查詢

        :param request: Request instance for QueryPayerInfo.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.QueryPayerInfoRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.QueryPayerInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryPayerInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryPayerInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryReconciliationDocument(self, request):
        """查詢對賬文件訊息。平台調用該介面獲取需下載對賬文件的文件名稱以及金鑰。 平台獲取到訊息後， 可以再調用OPENAPI的文件下載功能。

        :param request: Request instance for QueryReconciliationDocument.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.QueryReconciliationDocumentRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.QueryReconciliationDocumentResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryReconciliationDocument", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryReconciliationDocumentResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryRefund(self, request):
        """提交退款申請後，通過調用該介面查詢退款狀态。退款可能有一定延時，用 零錢支付的退款約20分鍾内到賬，銀行卡支付的退款約3個工作日後到賬。

        :param request: Request instance for QueryRefund.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.QueryRefundRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.QueryRefundResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryRefund", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryRefundResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QuerySingleTransactionStatus(self, request):
        """查詢銀行單筆交易狀态。查詢單筆交易的狀态。

        :param request: Request instance for QuerySingleTransactionStatus.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.QuerySingleTransactionStatusRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.QuerySingleTransactionStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QuerySingleTransactionStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QuerySingleTransactionStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QuerySmallAmountTransfer(self, request):
        """查詢小額鑒權轉賬結果。查詢小額往賬鑒權的轉賬狀态。

        :param request: Request instance for QuerySmallAmountTransfer.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.QuerySmallAmountTransferRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.QuerySmallAmountTransferResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QuerySmallAmountTransfer", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QuerySmallAmountTransferResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryTrade(self, request):
        """跨境-貿易材料明細查詢

        :param request: Request instance for QueryTrade.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.QueryTradeRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.QueryTradeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryTrade", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryTradeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RechargeMemberThirdPay(self, request):
        """見證寶-會員在途儲值(經第三方支付管道)

        :param request: Request instance for RechargeMemberThirdPay.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.RechargeMemberThirdPayRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.RechargeMemberThirdPayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RechargeMemberThirdPay", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RechargeMemberThirdPayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def Refund(self, request):
        """如交易訂單需退款，可以通過本介面将支付款全部或部分退還給付款方，聚鑫将在收到退款請求並且驗證成功之後，按照退款規則将支付款按原路退回到支付帳號。最長支援1年的訂單退款。在訂單包含多個子訂單的情況下，如果使用本介面傳入OutTradeNo或TransactionId退款，則只支援全單退款；如果需要部分退款，請通過傳入子訂單的方式來指定部分金額退款。

        :param request: Request instance for Refund.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.RefundRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.RefundResponse`

        """
        try:
            params = request._serialize()
            body = self.call("Refund", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RefundResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RegisterBillSupportWithdraw(self, request):
        """登記挂賬(支援撤銷)。此介面可實現把不明來賬或自有資金等已登記在挂賬子帳戶下的資金調整到普通會員子帳戶。即通過申請調用此介面，将會減少挂賬子帳戶的資金，調增指定的普通會員子帳戶的可提現餘額及可用餘額。此介面不支援把挂賬子帳戶資金清分到功能子帳戶。

        :param request: Request instance for RegisterBillSupportWithdraw.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.RegisterBillSupportWithdrawRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.RegisterBillSupportWithdrawResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RegisterBillSupportWithdraw", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RegisterBillSupportWithdrawResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RevRegisterBillSupportWithdraw(self, request):
        """登記挂賬撤銷。此介面可以實現把RegisterBillSupportWithdraw介面完成的登記挂賬進行撤銷，即調減普通會員子帳戶的可提現和可用餘額，調增挂賬子帳戶的可用餘額。

        :param request: Request instance for RevRegisterBillSupportWithdraw.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.RevRegisterBillSupportWithdrawRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.RevRegisterBillSupportWithdrawResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RevRegisterBillSupportWithdraw", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RevRegisterBillSupportWithdrawResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RevResigterBillSupportWithdraw(self, request):
        """登記挂賬撤銷。此介面可以實現把RegisterBillSupportWithdraw介面完成的登記挂賬進行撤銷，即調減普通會員子帳戶的可提現和可用餘額，調增挂賬子帳戶的可用餘額。

        :param request: Request instance for RevResigterBillSupportWithdraw.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.RevResigterBillSupportWithdrawRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.RevResigterBillSupportWithdrawResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RevResigterBillSupportWithdraw", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RevResigterBillSupportWithdrawResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReviseMbrProperty(self, request):
        """修改會員屬性-普通商戶子帳戶。修改會員的會員屬性。

        :param request: Request instance for ReviseMbrProperty.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.ReviseMbrPropertyRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.ReviseMbrPropertyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReviseMbrProperty", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReviseMbrPropertyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RevokeMemberRechargeThirdPay(self, request):
        """撤銷會員在途儲值(經第三方支付管道)

        :param request: Request instance for RevokeMemberRechargeThirdPay.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.RevokeMemberRechargeThirdPayRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.RevokeMemberRechargeThirdPayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RevokeMemberRechargeThirdPay", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RevokeMemberRechargeThirdPayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnBindAcct(self, request):
        """商戶解除綁定的提現銀行卡

        :param request: Request instance for UnBindAcct.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.UnBindAcctRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.UnBindAcctResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnBindAcct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnBindAcctResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnbindRelateAcct(self, request):
        """會員解綁提現帳戶。此介面可以支援會員解除名下的綁定帳戶關系。

        :param request: Request instance for UnbindRelateAcct.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.UnbindRelateAcctRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.UnbindRelateAcctResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnbindRelateAcct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindRelateAcctResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnifiedOrder(self, request):
        """應用需要先調用本介面生成支付訂單號，並将應答的PayInfo透傳給聚鑫SDK，拉起用戶端（包括 公衆號/ 小程式/用戶端App）支付。

        :param request: Request instance for UnifiedOrder.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.UnifiedOrderRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.UnifiedOrderResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnifiedOrder", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnifiedOrderResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def WithdrawCashMembership(self, request):
        """會員提現-不驗證。此介面受理會員發起的提現申請。會員子帳戶的可提現餘額、可用餘額會減少，市場的資金匯總帳戶(監管帳戶)會減少相應的發生金額，提現到會員申請的收款帳戶。

        :param request: Request instance for WithdrawCashMembership.
        :type request: :class:`taifucloudcloud.cpdp.v20190820.models.WithdrawCashMembershipRequest`
        :rtype: :class:`taifucloudcloud.cpdp.v20190820.models.WithdrawCashMembershipResponse`

        """
        try:
            params = request._serialize()
            body = self.call("WithdrawCashMembership", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.WithdrawCashMembershipResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)