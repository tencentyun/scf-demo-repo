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


class CallBackCdr(AbstractModel):
    """話單詳情

    """

    def __init__(self):
        """
        :param CallId: 呼叫通話 ID
        :type CallId: str
        :param Src: 主叫號碼
        :type Src: str
        :param Dst: 被叫號碼
        :type Dst: str
        :param StartSrcCallTime: 主叫呼叫開始時間
        :type StartSrcCallTime: str
        :param StartSrcRingTime: 主叫響鈴開始時間
        :type StartSrcRingTime: str
        :param SrcAcceptTime: 主叫接聽時間
        :type SrcAcceptTime: str
        :param StartDstCallTime: 被叫呼叫開始時間
        :type StartDstCallTime: str
        :param StartDstRingTime: 被叫響鈴開始時間
        :type StartDstRingTime: str
        :param DstAcceptTime: 被叫接聽時間
        :type DstAcceptTime: str
        :param EndCallTime: 用戶挂機通話結束時間
        :type EndCallTime: str
        :param CallEndStatus: 通話最後狀态：0：未知狀态 1：正常通話 2：主叫未接 3：主叫接聽，被叫未接 4：主叫未接通 5：被叫未接通
        :type CallEndStatus: str
        :param Duration: 通話計費時間
        :type Duration: str
        :param RecordUrl: 錄音 URL，如果不錄音或錄音失敗，該值爲空
        :type RecordUrl: str
        :param CallType: 通話類型(1: VOIP 2:IP TO PSTN 3: PSTN TO PSTN)，如果話單中沒有該欄位，預設值爲回撥 3 (PSTN TO PSTN)
注意：此欄位可能返回 null，表示取不到有效值。
        :type CallType: str
        :param BizId: 同回撥請求中的 bizId，如果回撥請求中帶 bizId 會有該欄位返回
注意：此欄位可能返回 null，表示取不到有效值。
        :type BizId: str
        :param OrderId: 訂單 ID,最大長度不超過 64 個位元，對於一些有訂單狀态 App 相關應用（如達人幫接入 App 應用)，該欄位只在帳單中帶上，其它回調不附帶該欄位
注意：此欄位可能返回 null，表示取不到有效值。
        :type OrderId: str
        """
        self.CallId = None
        self.Src = None
        self.Dst = None
        self.StartSrcCallTime = None
        self.StartSrcRingTime = None
        self.SrcAcceptTime = None
        self.StartDstCallTime = None
        self.StartDstRingTime = None
        self.DstAcceptTime = None
        self.EndCallTime = None
        self.CallEndStatus = None
        self.Duration = None
        self.RecordUrl = None
        self.CallType = None
        self.BizId = None
        self.OrderId = None


    def _deserialize(self, params):
        self.CallId = params.get("CallId")
        self.Src = params.get("Src")
        self.Dst = params.get("Dst")
        self.StartSrcCallTime = params.get("StartSrcCallTime")
        self.StartSrcRingTime = params.get("StartSrcRingTime")
        self.SrcAcceptTime = params.get("SrcAcceptTime")
        self.StartDstCallTime = params.get("StartDstCallTime")
        self.StartDstRingTime = params.get("StartDstRingTime")
        self.DstAcceptTime = params.get("DstAcceptTime")
        self.EndCallTime = params.get("EndCallTime")
        self.CallEndStatus = params.get("CallEndStatus")
        self.Duration = params.get("Duration")
        self.RecordUrl = params.get("RecordUrl")
        self.CallType = params.get("CallType")
        self.BizId = params.get("BizId")
        self.OrderId = params.get("OrderId")


class CallBackPhoneCode(AbstractModel):
    """回撥號碼欄位

    """

    def __init__(self):
        """
        :param Nation: 國家碼，統一以 00 開頭
        :type Nation: str
        :param Phone: 號碼（固話區號前加 0，如075586013388）
        :type Phone: str
        """
        self.Nation = None
        self.Phone = None


    def _deserialize(self, params):
        self.Nation = params.get("Nation")
        self.Phone = params.get("Phone")


class CreateCallBackRequest(AbstractModel):
    """CreateCallBack請求參數結構體

    """

    def __init__(self):
        """
        :param BizAppId: 業務appid
        :type BizAppId: str
        :param Src: 主叫號碼(必須爲 11 位手機號，號碼前加 0086，如 008613631686024)
        :type Src: str
        :param Dst: 被叫號碼(必須爲 11 位手機或固話號碼,號碼前加 0086，如008613631686024，固話如：0086075586013388)
        :type Dst: str
        :param SrcDisplayNum: 主叫顯示系統分配的固話號碼，如不填顯示随機分配號碼
        :type SrcDisplayNum: str
        :param DstDisplayNum: 被叫顯示系統分配的固話號碼，如不填顯示随機分配號碼
        :type DstDisplayNum: str
        :param Record: 是否錄音，0 表示不錄音，1 表示錄音。預設爲不錄音
        :type Record: str
        :param MaxAllowTime: 允許最大通話時間，不填預設爲 30 分鍾（單位：分鍾）
        :type MaxAllowTime: str
        :param StatusFlag: 主叫發起呼叫狀态：1 被叫發起呼叫狀态：256 主叫響鈴狀态：2 被叫響鈴狀态：512 主叫接聽狀态：4 被叫接聽狀态：1024 主叫拒絕接聽狀态：8 被叫拒絕接聽狀态：2048 主叫正常挂機狀态：16 被叫正常挂機狀态：4096 主叫呼叫異常：32 被叫呼叫異常：8192
例如：當值爲 0：表示所有狀态不需要推送；當值爲 4：表示只要推送主叫接聽狀态；當值爲 16191：表示所有狀态都需要推送(上面所有值和)
        :type StatusFlag: str
        :param StatusUrl: 狀态回調通知網址，正式環境可以配置預設推送網址
        :type StatusUrl: str
        :param HangupUrl: 話單回調通知網址，正式環境可以配置預設推送網址
        :type HangupUrl: str
        :param RecordUrl: 錄單 URL 回調通知網址，正式環境可以配置預設推送網址
        :type RecordUrl: str
        :param BizId: 業務應用 key，業務用該 key 可以區分内部業務或客戶産品等，該 key 需保證在該 appId 下全局唯一，最大長度不超過 64 個位元，bizId 只能包含數字、字母。
        :type BizId: str
        :param LastCallId: 最後一次呼叫 callId，帶上該欄位以後，平台會參考該 callId 分配線路，優先不分配該 callId 通話線路（注：謹慎使用，這個會影響線路調度）
        :type LastCallId: str
        :param PreCallerHandle: 結構體，主叫呼叫預處理操作，根據不同操作确認是否呼通被叫。如需使用，本結構體需要與 keyList 結構體配合使用，此時這兩個參數都爲必填項
        :type PreCallerHandle: :class:`taifucloudcloud.npp.v20190823.models.RreCallerHandle`
        :param OrderId: 訂單 ID，最大長度不超過64個位元，對於一些有訂單狀态 App 相關應用使用（如達人幫接入 App 應用)，該欄位只在帳單中帶上，其它回調不附帶該欄位
        :type OrderId: str
        """
        self.BizAppId = None
        self.Src = None
        self.Dst = None
        self.SrcDisplayNum = None
        self.DstDisplayNum = None
        self.Record = None
        self.MaxAllowTime = None
        self.StatusFlag = None
        self.StatusUrl = None
        self.HangupUrl = None
        self.RecordUrl = None
        self.BizId = None
        self.LastCallId = None
        self.PreCallerHandle = None
        self.OrderId = None


    def _deserialize(self, params):
        self.BizAppId = params.get("BizAppId")
        self.Src = params.get("Src")
        self.Dst = params.get("Dst")
        self.SrcDisplayNum = params.get("SrcDisplayNum")
        self.DstDisplayNum = params.get("DstDisplayNum")
        self.Record = params.get("Record")
        self.MaxAllowTime = params.get("MaxAllowTime")
        self.StatusFlag = params.get("StatusFlag")
        self.StatusUrl = params.get("StatusUrl")
        self.HangupUrl = params.get("HangupUrl")
        self.RecordUrl = params.get("RecordUrl")
        self.BizId = params.get("BizId")
        self.LastCallId = params.get("LastCallId")
        if params.get("PreCallerHandle") is not None:
            self.PreCallerHandle = RreCallerHandle()
            self.PreCallerHandle._deserialize(params.get("PreCallerHandle"))
        self.OrderId = params.get("OrderId")


class CreateCallBackResponse(AbstractModel):
    """CreateCallBack返回參數結構體

    """

    def __init__(self):
        """
        :param CallId: 話單id
注意：此欄位可能返回 null，表示取不到有效值。
        :type CallId: str
        :param SrcDisplayNum: 主叫顯示系統分配的固話號碼
注意：此欄位可能返回 null，表示取不到有效值。
        :type SrcDisplayNum: str
        :param DstDisplayNum: 被叫顯示系統分配的固話號碼
注意：此欄位可能返回 null，表示取不到有效值。
        :type DstDisplayNum: str
        :param ErrorCode: 錯誤碼
        :type ErrorCode: str
        :param Msg: 錯誤原因
注意：此欄位可能返回 null，表示取不到有效值。
        :type Msg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CallId = None
        self.SrcDisplayNum = None
        self.DstDisplayNum = None
        self.ErrorCode = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CallId = params.get("CallId")
        self.SrcDisplayNum = params.get("SrcDisplayNum")
        self.DstDisplayNum = params.get("DstDisplayNum")
        self.ErrorCode = params.get("ErrorCode")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DelVirtualNumRequest(AbstractModel):
    """DelVirtualNum請求參數結構體

    """

    def __init__(self):
        """
        :param BizAppId: 業務appid
        :type BizAppId: str
        :param BindId: 雙方號碼 + 中間號綁定 ID，該 ID 全局唯一
        :type BindId: str
        :param BizId: 應用二級業務 ID，bizId 需保證在該 appId 下全局唯一，最大長度不超過 16 個位元。
        :type BizId: str
        """
        self.BizAppId = None
        self.BindId = None
        self.BizId = None


    def _deserialize(self, params):
        self.BizAppId = params.get("BizAppId")
        self.BindId = params.get("BindId")
        self.BizId = params.get("BizId")


class DelVirtualNumResponse(AbstractModel):
    """DelVirtualNum返回參數結構體

    """

    def __init__(self):
        """
        :param ErrorCode: 錯誤碼
        :type ErrorCode: str
        :param Msg: 錯誤訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Msg: str
        :param BindId: 綁定 ID，該 ID 全局唯一
注意：此欄位可能返回 null，表示取不到有效值。
        :type BindId: str
        :param RefLeftNum: 中間號還剩引用計數，如果計數爲 0 會解綁
注意：此欄位可能返回 null，表示取不到有效值。
        :type RefLeftNum: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ErrorCode = None
        self.Msg = None
        self.BindId = None
        self.RefLeftNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.Msg = params.get("Msg")
        self.BindId = params.get("BindId")
        self.RefLeftNum = params.get("RefLeftNum")
        self.RequestId = params.get("RequestId")


class DeleteCallBackRequest(AbstractModel):
    """DeleteCallBack請求參數結構體

    """

    def __init__(self):
        """
        :param BizAppId: 業務appid
        :type BizAppId: str
        :param CallId: 回撥請求響應中返回的 callId
        :type CallId: str
        :param CancelFlag: 0：不管通話狀态直接拆線（預設) 1：主叫響鈴以後狀态不拆線 2：主叫接聽以後狀态不拆線 3：被叫響鈴以後狀态不拆線 4：被叫接聽以後狀态不拆線
        :type CancelFlag: str
        """
        self.BizAppId = None
        self.CallId = None
        self.CancelFlag = None


    def _deserialize(self, params):
        self.BizAppId = params.get("BizAppId")
        self.CallId = params.get("CallId")
        self.CancelFlag = params.get("CancelFlag")


class DeleteCallBackResponse(AbstractModel):
    """DeleteCallBack返回參數結構體

    """

    def __init__(self):
        """
        :param ErrorCode: 錯誤碼
        :type ErrorCode: str
        :param Msg: 錯誤原因
注意：此欄位可能返回 null，表示取不到有效值。
        :type Msg: str
        :param CallId: 話單id
注意：此欄位可能返回 null，表示取不到有效值。
        :type CallId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ErrorCode = None
        self.Msg = None
        self.CallId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.Msg = params.get("Msg")
        self.CallId = params.get("CallId")
        self.RequestId = params.get("RequestId")


class DescribeCallBackCdrRequest(AbstractModel):
    """DescribeCallBackCdr請求參數結構體

    """

    def __init__(self):
        """
        :param BizAppId: 業務appid
        :type BizAppId: str
        :param CallId: 回撥請求響應中返回的 callId，按 callId 查詢該話單詳細訊息
        :type CallId: str
        :param Src: 查詢主叫用戶産生的呼叫話單，如填空表示拉取這個時間段所有話單
        :type Src: str
        :param StartTimeStamp: 話單開始時間戳
        :type StartTimeStamp: str
        :param EndTimeStamp: 話單結束時間戳
        :type EndTimeStamp: str
        """
        self.BizAppId = None
        self.CallId = None
        self.Src = None
        self.StartTimeStamp = None
        self.EndTimeStamp = None


    def _deserialize(self, params):
        self.BizAppId = params.get("BizAppId")
        self.CallId = params.get("CallId")
        self.Src = params.get("Src")
        self.StartTimeStamp = params.get("StartTimeStamp")
        self.EndTimeStamp = params.get("EndTimeStamp")


class DescribeCallBackCdrResponse(AbstractModel):
    """DescribeCallBackCdr返回參數結構體

    """

    def __init__(self):
        """
        :param Cdr: 話單清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Cdr: list of CallBackCdr
        :param Offset: 偏移
注意：此欄位可能返回 null，表示取不到有效值。
        :type Offset: str
        :param ErrorCode: 錯誤碼
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrorCode: str
        :param Msg: 錯誤原因
注意：此欄位可能返回 null，表示取不到有效值。
        :type Msg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Cdr = None
        self.Offset = None
        self.ErrorCode = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Cdr") is not None:
            self.Cdr = []
            for item in params.get("Cdr"):
                obj = CallBackCdr()
                obj._deserialize(item)
                self.Cdr.append(obj)
        self.Offset = params.get("Offset")
        self.ErrorCode = params.get("ErrorCode")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class DescribeCallBackStatusRequest(AbstractModel):
    """DescribeCallBackStatus請求參數結構體

    """

    def __init__(self):
        """
        :param BizAppId: 業務appid
        :type BizAppId: str
        :param CallId: 回撥請求響應中返回的 callId
        :type CallId: str
        :param Src: 主叫號碼
        :type Src: str
        :param Dst: 被叫號碼
        :type Dst: str
        :param CallStatus: 通話最後狀态：0：未知狀态 1：主叫響鈴中 2：主叫接聽 3：被叫響鈴中 4：正常通話中 5：通話結束
        :type CallStatus: str
        """
        self.BizAppId = None
        self.CallId = None
        self.Src = None
        self.Dst = None
        self.CallStatus = None


    def _deserialize(self, params):
        self.BizAppId = params.get("BizAppId")
        self.CallId = params.get("CallId")
        self.Src = params.get("Src")
        self.Dst = params.get("Dst")
        self.CallStatus = params.get("CallStatus")


class DescribeCallBackStatusResponse(AbstractModel):
    """DescribeCallBackStatus返回參數結構體

    """

    def __init__(self):
        """
        :param ErrorCode: 錯誤碼
        :type ErrorCode: str
        :param Msg: 錯誤訊息
        :type Msg: str
        :param AppId: 業務appid
        :type AppId: str
        :param CallId: 回撥請求響應中返回的 callId
        :type CallId: str
        :param Src: 主叫號碼
        :type Src: str
        :param Dst: 被叫號碼
        :type Dst: str
        :param CallStatus: 通話最後狀态：0：未知狀态 1：主叫響鈴中 2：主叫接聽 3：被叫響鈴中 4：正常通話中 5：通話結束
        :type CallStatus: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ErrorCode = None
        self.Msg = None
        self.AppId = None
        self.CallId = None
        self.Src = None
        self.Dst = None
        self.CallStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.Msg = params.get("Msg")
        self.AppId = params.get("AppId")
        self.CallId = params.get("CallId")
        self.Src = params.get("Src")
        self.Dst = params.get("Dst")
        self.CallStatus = params.get("CallStatus")
        self.RequestId = params.get("RequestId")


class DescribeCallerDisplayListRequest(AbstractModel):
    """DescribeCallerDisplayList請求參數結構體

    """

    def __init__(self):
        """
        :param BizAppId: 業務appid
        :type BizAppId: str
        """
        self.BizAppId = None


    def _deserialize(self, params):
        self.BizAppId = params.get("BizAppId")


class DescribeCallerDisplayListResponse(AbstractModel):
    """DescribeCallerDisplayList返回參數結構體

    """

    def __init__(self):
        """
        :param AppId: appid
注意：此欄位可能返回 null，表示取不到有效值。
        :type AppId: str
        :param CodeList: 主叫顯號號碼集合，codeList[0...*] 結構體數組，如果業務是主被叫互顯，該欄位爲空
注意：此欄位可能返回 null，表示取不到有效值。
        :type CodeList: list of CallBackPhoneCode
        :param ErrorCode: 錯誤碼
        :type ErrorCode: str
        :param Msg: 錯誤原因
注意：此欄位可能返回 null，表示取不到有效值。
        :type Msg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AppId = None
        self.CodeList = None
        self.ErrorCode = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        if params.get("CodeList") is not None:
            self.CodeList = []
            for item in params.get("CodeList"):
                obj = CallBackPhoneCode()
                obj._deserialize(item)
                self.CodeList.append(obj)
        self.ErrorCode = params.get("ErrorCode")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class Get400CdrRequest(AbstractModel):
    """Get400Cdr請求參數結構體

    """

    def __init__(self):
        """
        :param BizAppId: 業務appid
        :type BizAppId: str
        :param CallId: 通話唯一標識 callId，即直撥呼叫響應中返回的 callId
        :type CallId: str
        :param Src: 查詢主叫用戶産生的呼叫話單（0086開頭），設置爲空表示拉取該時間段的所有話單
        :type Src: str
        :param StartTimeStamp: 話單開始時間戳
        :type StartTimeStamp: str
        :param EndTimeStamp: 話單結束時間戳
        :type EndTimeStamp: str
        """
        self.BizAppId = None
        self.CallId = None
        self.Src = None
        self.StartTimeStamp = None
        self.EndTimeStamp = None


    def _deserialize(self, params):
        self.BizAppId = params.get("BizAppId")
        self.CallId = params.get("CallId")
        self.Src = params.get("Src")
        self.StartTimeStamp = params.get("StartTimeStamp")
        self.EndTimeStamp = params.get("EndTimeStamp")


class Get400CdrResponse(AbstractModel):
    """Get400Cdr返回參數結構體

    """

    def __init__(self):
        """
        :param ErrorCode: 錯誤碼
        :type ErrorCode: str
        :param Msg: 錯誤原因
注意：此欄位可能返回 null，表示取不到有效值。
        :type Msg: str
        :param Offset: 偏移
注意：此欄位可能返回 null，表示取不到有效值。
        :type Offset: str
        :param Cdr: 話單清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Cdr: list of VirturalNumCdr
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ErrorCode = None
        self.Msg = None
        self.Offset = None
        self.Cdr = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.Msg = params.get("Msg")
        self.Offset = params.get("Offset")
        if params.get("Cdr") is not None:
            self.Cdr = []
            for item in params.get("Cdr"):
                obj = VirturalNumCdr()
                obj._deserialize(item)
                self.Cdr.append(obj)
        self.RequestId = params.get("RequestId")


class GetVirtualNumRequest(AbstractModel):
    """GetVirtualNum請求參數結構體

    """

    def __init__(self):
        """
        :param BizAppId: 業務appid
        :type BizAppId: str
        :param Dst: 被叫號碼(號碼前加 0086，如 008613631686024)
        :type Dst: str
        :param Src: 主叫號碼(號碼前加 0086，如 008613631686024)，xb 模式下是不用填寫，axb 模式下是必選
        :type Src: str
        :param AccreditList: {“accreditList”:[“008613631686024”,”008612345678910”]}，主要用於 N-1 場景，號碼綁定非共享是獨占型，指定了 dst 獨占中間號綁定，accreditList 表示這個清單成員可以撥打 dst 綁 定的中間號，預設值爲空，表示所有號碼都可以撥打獨占型中間號綁定，最大集合不允許超過 30 個，僅适用於xb模式
        :type AccreditList: list of str
        :param AssignVirtualNum: 指定中間號（格式：008617013541251），如果該中間號已被使用則返回綁定失敗。如果不帶該欄位則由 側從號碼池裏自動分配
        :type AssignVirtualNum: str
        :param Record: 是否錄音，0表示不錄音，1表示錄音。預設爲不錄音，注意如果需要錄音回調，通話完成後需要等待一段時間，收到錄音回調之後，再解綁中間號。
        :type Record: str
        :param CityId: 主被叫顯號號碼歸屬地，指定該參數說明顯號歸屬該城市，如果沒有該城市號碼會随機選取一個城市或者後台配置返回107，返回碼詳見 《 -中間號-城市id.xlsx》
        :type CityId: str
        :param BizId: 應用二級業務 ID，bizId 需保證在該 appId 下全局唯一，最大長度不超過 16 個位元。
        :type BizId: str
        :param MaxAssignTime: 號碼最大綁定時間，不填預設爲 24 小時，最長綁定時間是168小時，單位秒
        :type MaxAssignTime: str
        :param StatusFlag: 主叫發起呼叫狀态：1
被叫發起呼叫狀态：256
主叫響鈴狀态：2
被叫響鈴狀态：512
主叫接聽狀态：4
被叫接聽狀态：1024
主叫拒絕接聽狀态：8
被叫拒絕接聽狀态：2048
主叫正常挂機狀态：16
被叫正常挂機狀态：4096
主叫呼叫異常：32
被叫呼叫異常：8192

例如：
值爲 0：表示所有狀态不需要推送
值爲 4：表示只要推送主叫接聽狀态
值爲 16191：表示所有狀态都需要推送（上面所有值和）
        :type StatusFlag: str
        :param StatusUrl: 請填寫statusFlag並設置值，狀态回調通知網址，正式環境可以配置預設推送網址
        :type StatusUrl: str
        :param HangupUrl: 話單回調通知網址，正式環境可以配置預設推送網址
        :type HangupUrl: str
        :param RecordUrl: 錄單 URL 回調通知網址，正式環境可以配置預設推送網址
        :type RecordUrl: str
        """
        self.BizAppId = None
        self.Dst = None
        self.Src = None
        self.AccreditList = None
        self.AssignVirtualNum = None
        self.Record = None
        self.CityId = None
        self.BizId = None
        self.MaxAssignTime = None
        self.StatusFlag = None
        self.StatusUrl = None
        self.HangupUrl = None
        self.RecordUrl = None


    def _deserialize(self, params):
        self.BizAppId = params.get("BizAppId")
        self.Dst = params.get("Dst")
        self.Src = params.get("Src")
        self.AccreditList = params.get("AccreditList")
        self.AssignVirtualNum = params.get("AssignVirtualNum")
        self.Record = params.get("Record")
        self.CityId = params.get("CityId")
        self.BizId = params.get("BizId")
        self.MaxAssignTime = params.get("MaxAssignTime")
        self.StatusFlag = params.get("StatusFlag")
        self.StatusUrl = params.get("StatusUrl")
        self.HangupUrl = params.get("HangupUrl")
        self.RecordUrl = params.get("RecordUrl")


class GetVirtualNumResponse(AbstractModel):
    """GetVirtualNum返回參數結構體

    """

    def __init__(self):
        """
        :param ErrorCode: 錯誤碼
        :type ErrorCode: str
        :param BindId: 綁定 ID，該 ID 全局唯一
注意：此欄位可能返回 null，表示取不到有效值。
        :type BindId: str
        :param RefNum: 中間號還剩引用計數，如果計數爲 0 會解綁
注意：此欄位可能返回 null，表示取不到有效值。
        :type RefNum: str
        :param VirtualNum: 中間號
注意：此欄位可能返回 null，表示取不到有效值。
        :type VirtualNum: str
        :param Msg: 錯誤原因
注意：此欄位可能返回 null，表示取不到有效值。
        :type Msg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ErrorCode = None
        self.BindId = None
        self.RefNum = None
        self.VirtualNum = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.BindId = params.get("BindId")
        self.RefNum = params.get("RefNum")
        self.VirtualNum = params.get("VirtualNum")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class KeyList(AbstractModel):
    """對應按鍵操作,如果沒有結構體裏定義按鍵操作用戶按鍵以後都從 interruptPrompt 重新播放

    """

    def __init__(self):
        """
        :param Key: 用戶按鍵（0-9、*、#、A-D)
        :type Key: str
        :param Operate: 1: 呼通被叫 2：interruptPrompt 重播提示 3：拆線
        :type Operate: str
        """
        self.Key = None
        self.Operate = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Operate = params.get("Operate")


class RreCallerHandle(AbstractModel):
    """結構體，主叫呼叫預處理操作，根據不同操作确認是否呼通被叫。如需使用，本結構體需要與 keyList 結構體配合使用，此時這兩個參數都爲必填項

    """

    def __init__(self):
        """
        :param ReadPrompt: 呼叫主叫以後，給主叫用戶的語音提示，播放該提示時用戶所有按鍵無效
        :type ReadPrompt: str
        :param InterruptPrompt: 可中斷提示，播放該提示時，用戶可以按鍵
        :type InterruptPrompt: str
        :param KeyList: 對應按鍵操作,如果沒有結構體裏定義按鍵操作用戶按鍵以後都從 interruptPrompt 重新播放
        :type KeyList: list of KeyList
        :param RepeatTimes: 最多重複播放次數，超過該次數拆線
        :type RepeatTimes: str
        :param KeyPressUrl: 用戶按鍵回調通知網址，如果爲空不回調
        :type KeyPressUrl: str
        :param PromptGender: 提示音男聲女聲：1女聲，2男聲。預設女聲
        :type PromptGender: str
        """
        self.ReadPrompt = None
        self.InterruptPrompt = None
        self.KeyList = None
        self.RepeatTimes = None
        self.KeyPressUrl = None
        self.PromptGender = None


    def _deserialize(self, params):
        self.ReadPrompt = params.get("ReadPrompt")
        self.InterruptPrompt = params.get("InterruptPrompt")
        if params.get("KeyList") is not None:
            self.KeyList = []
            for item in params.get("KeyList"):
                obj = KeyList()
                obj._deserialize(item)
                self.KeyList.append(obj)
        self.RepeatTimes = params.get("RepeatTimes")
        self.KeyPressUrl = params.get("KeyPressUrl")
        self.PromptGender = params.get("PromptGender")


class VirturalNumCdr(AbstractModel):
    """直撥話單詳情

    """

    def __init__(self):
        """
        :param CallId: 呼叫通話 ID
        :type CallId: str
        :param BindId: 雙方號碼 + 中間號綁定 ID，該 ID 全局唯一
        :type BindId: str
        :param Src: 主叫號碼
        :type Src: str
        :param Dst: 被叫號碼
        :type Dst: str
        :param DstVirtualNum: 主叫通訊錄直撥虛拟保護號碼
        :type DstVirtualNum: str
        :param CallCenterAcceptTime: 虛拟保護號碼平台收到呼叫時間
        :type CallCenterAcceptTime: str
        :param StartDstCallTime: 被叫呼叫開始時間
        :type StartDstCallTime: str
        :param StartDstRingTime: 被叫響鈴開始時間
        :type StartDstRingTime: str
        :param DstAcceptTime: 被叫接聽時間
        :type DstAcceptTime: str
        :param EndCallTime: 用戶挂機通話結束時間
        :type EndCallTime: str
        :param CallEndStatus: 通話最後狀态：0：未知狀态 1：正常通話 2：查詢呼叫轉移被叫號異常 3：未接通 4：未接聽 5：拒接挂斷 6：關機 7：空號 8：通話中 9：欠費 10：運營商線路或平台異常
        :type CallEndStatus: str
        :param SrcDuration: 主叫接通虛拟保護號碼到通話結束通話時間
        :type SrcDuration: str
        :param DstDuration: 呼叫轉接被叫接通到通話結束通話時間
        :type DstDuration: str
        :param RecordUrl: 錄音 URL，如果不錄音或錄音失敗，該值爲空
        :type RecordUrl: str
        """
        self.CallId = None
        self.BindId = None
        self.Src = None
        self.Dst = None
        self.DstVirtualNum = None
        self.CallCenterAcceptTime = None
        self.StartDstCallTime = None
        self.StartDstRingTime = None
        self.DstAcceptTime = None
        self.EndCallTime = None
        self.CallEndStatus = None
        self.SrcDuration = None
        self.DstDuration = None
        self.RecordUrl = None


    def _deserialize(self, params):
        self.CallId = params.get("CallId")
        self.BindId = params.get("BindId")
        self.Src = params.get("Src")
        self.Dst = params.get("Dst")
        self.DstVirtualNum = params.get("DstVirtualNum")
        self.CallCenterAcceptTime = params.get("CallCenterAcceptTime")
        self.StartDstCallTime = params.get("StartDstCallTime")
        self.StartDstRingTime = params.get("StartDstRingTime")
        self.DstAcceptTime = params.get("DstAcceptTime")
        self.EndCallTime = params.get("EndCallTime")
        self.CallEndStatus = params.get("CallEndStatus")
        self.SrcDuration = params.get("SrcDuration")
        self.DstDuration = params.get("DstDuration")
        self.RecordUrl = params.get("RecordUrl")