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


class AppInfo(AbstractModel):
    """物聯網卡應用訊息詳情

    """

    def __init__(self):
        """
        :param Sdkappid: 應用ID
        :type Sdkappid: str
        :param Appkey: 應用key
        :type Appkey: str
        :param CloudAppid: 用戶appid
        :type CloudAppid: str
        :param Name: 應用名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type Name: str
        :param Description: 應用描述
        :type Description: str
        :param CreatedTime: 創建時間
        :type CreatedTime: str
        :param BizType: 應用類型
        :type BizType: int
        :param Uin: 用戶Uin
        :type Uin: str
        """
        self.Sdkappid = None
        self.Appkey = None
        self.CloudAppid = None
        self.Name = None
        self.Description = None
        self.CreatedTime = None
        self.BizType = None
        self.Uin = None


    def _deserialize(self, params):
        self.Sdkappid = params.get("Sdkappid")
        self.Appkey = params.get("Appkey")
        self.CloudAppid = params.get("CloudAppid")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.CreatedTime = params.get("CreatedTime")
        self.BizType = params.get("BizType")
        self.Uin = params.get("Uin")


class CardInfo(AbstractModel):
    """卡片詳細訊息

    """

    def __init__(self):
        """
        :param Iccid: 卡片ID
        :type Iccid: str
        :param Msisdn: 卡電話号碼
注意：此欄位可能返回 null，表示取不到有效值。
        :type Msisdn: str
        :param Imsi: 卡imsi
注意：此欄位可能返回 null，表示取不到有效值。
        :type Imsi: str
        :param Imei: 卡imei
注意：此欄位可能返回 null，表示取不到有效值。
        :type Imei: str
        :param Sdkappid: 應用ID
        :type Sdkappid: str
        :param Teleoperator: 運營商編号
        :type Teleoperator: int
        :param CardStatus: 卡片狀态 1:未啟動 2：啟動 3：停卡 5：銷卡
        :type CardStatus: int
        :param NetworkStatus: 網絡狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type NetworkStatus: int
        :param ActivitedTime: 啟動時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type ActivitedTime: str
        :param Type: 資費類型，1 單卡，2 流量池
        :type Type: int
        :param ProductId: 套餐類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param PoolId: 流量池ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type PoolId: str
        :param DataUsedInPeriod: 周期套餐流量使用
注意：此欄位可能返回 null，表示取不到有效值。
        :type DataUsedInPeriod: float
        :param DataTotalInPeriod: 週期套餐總量
注意：此欄位可能返回 null，表示取不到有效值。
        :type DataTotalInPeriod: float
        :param ProductExpiredTime: 過期時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProductExpiredTime: str
        :param Description: 描述訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Description: str
        :param CreatedTime: 創建時間
        :type CreatedTime: str
        :param ModifiedTime: 修改時間
        :type ModifiedTime: str
        :param PreorderCnt: 套餐周期
注意：此欄位可能返回 null，表示取不到有效值。
        :type PreorderCnt: int
        :param IsActivated: 啟動被回調标志
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsActivated: int
        :param OrderId: 訂單ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type OrderId: str
        :param AutoRenew: 是否自動續約
注意：此欄位可能返回 null，表示取不到有效值。
        :type AutoRenew: int
        :param Remark: 備注
注意：此欄位可能返回 null，表示取不到有效值。
        :type Remark: str
        :param AllowArrears: 0 不需要開通達量不停卡 1 需要開通達量不停卡
注意：此欄位可能返回 null，表示取不到有效值。
        :type AllowArrears: int
        :param NeedSms: 是否開通簡訊0:未開簡訊 1:開通簡訊
        :type NeedSms: int
        :param Provider: 服務
        :type Provider: int
        """
        self.Iccid = None
        self.Msisdn = None
        self.Imsi = None
        self.Imei = None
        self.Sdkappid = None
        self.Teleoperator = None
        self.CardStatus = None
        self.NetworkStatus = None
        self.ActivitedTime = None
        self.Type = None
        self.ProductId = None
        self.PoolId = None
        self.DataUsedInPeriod = None
        self.DataTotalInPeriod = None
        self.ProductExpiredTime = None
        self.Description = None
        self.CreatedTime = None
        self.ModifiedTime = None
        self.PreorderCnt = None
        self.IsActivated = None
        self.OrderId = None
        self.AutoRenew = None
        self.Remark = None
        self.AllowArrears = None
        self.NeedSms = None
        self.Provider = None


    def _deserialize(self, params):
        self.Iccid = params.get("Iccid")
        self.Msisdn = params.get("Msisdn")
        self.Imsi = params.get("Imsi")
        self.Imei = params.get("Imei")
        self.Sdkappid = params.get("Sdkappid")
        self.Teleoperator = params.get("Teleoperator")
        self.CardStatus = params.get("CardStatus")
        self.NetworkStatus = params.get("NetworkStatus")
        self.ActivitedTime = params.get("ActivitedTime")
        self.Type = params.get("Type")
        self.ProductId = params.get("ProductId")
        self.PoolId = params.get("PoolId")
        self.DataUsedInPeriod = params.get("DataUsedInPeriod")
        self.DataTotalInPeriod = params.get("DataTotalInPeriod")
        self.ProductExpiredTime = params.get("ProductExpiredTime")
        self.Description = params.get("Description")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.PreorderCnt = params.get("PreorderCnt")
        self.IsActivated = params.get("IsActivated")
        self.OrderId = params.get("OrderId")
        self.AutoRenew = params.get("AutoRenew")
        self.Remark = params.get("Remark")
        self.AllowArrears = params.get("AllowArrears")
        self.NeedSms = params.get("NeedSms")
        self.Provider = params.get("Provider")


class CardList(AbstractModel):
    """卡片清單數據

    """

    def __init__(self):
        """
        :param Total: 卡片總數
        :type Total: str
        :param List: 卡片清單訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type List: list of CardInfo
        """
        self.Total = None
        self.List = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = CardInfo()
                obj._deserialize(item)
                self.List.append(obj)


class DescribeAppRequest(AbstractModel):
    """DescribeApp請求參數結構體

    """

    def __init__(self):
        """
        :param Sdkappid: 物聯卡應用ID
        :type Sdkappid: int
        """
        self.Sdkappid = None


    def _deserialize(self, params):
        self.Sdkappid = params.get("Sdkappid")


class DescribeAppResponse(AbstractModel):
    """DescribeApp返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 應用訊息詳情
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: :class:`taifucloudcloud.ic.v20190307.models.AppInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = AppInfo()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeCardRequest(AbstractModel):
    """DescribeCard請求參數結構體

    """

    def __init__(self):
        """
        :param Sdkappid: 應用ID
        :type Sdkappid: int
        :param Iccid: 卡片ID
        :type Iccid: str
        """
        self.Sdkappid = None
        self.Iccid = None


    def _deserialize(self, params):
        self.Sdkappid = params.get("Sdkappid")
        self.Iccid = params.get("Iccid")


class DescribeCardResponse(AbstractModel):
    """DescribeCard返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 卡片詳細訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: :class:`taifucloudcloud.ic.v20190307.models.CardInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CardInfo()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeCardsRequest(AbstractModel):
    """DescribeCards請求參數結構體

    """

    def __init__(self):
        """
        :param Sdkappid: 應用ID
        :type Sdkappid: str
        :param Offset: 偏移值
        :type Offset: int
        :param Limit: 清單限制
        :type Limit: int
        """
        self.Sdkappid = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Sdkappid = params.get("Sdkappid")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeCardsResponse(AbstractModel):
    """DescribeCards返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 卡片清單訊息
        :type Data: :class:`taifucloudcloud.ic.v20190307.models.CardList`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CardList()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class SendMultiSmsRequest(AbstractModel):
    """SendMultiSms請求參數結構體

    """

    def __init__(self):
        """
        :param Sdkappid: 應用ID
        :type Sdkappid: str
        :param Iccids: 卡片清單
        :type Iccids: list of str
        :param Content: 簡訊内容 長度限制 70
        :type Content: str
        """
        self.Sdkappid = None
        self.Iccids = None
        self.Content = None


    def _deserialize(self, params):
        self.Sdkappid = params.get("Sdkappid")
        self.Iccids = params.get("Iccids")
        self.Content = params.get("Content")


class SendMultiSmsResponse(AbstractModel):
    """SendMultiSms返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 簡訊流水數組
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: list of SmsRet
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SmsRet()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class SendSmsRequest(AbstractModel):
    """SendSms請求參數結構體

    """

    def __init__(self):
        """
        :param Sdkappid: 應用ID
        :type Sdkappid: int
        :param Iccid: 卡片ID
        :type Iccid: str
        :param Content: 簡訊内容長度70限制
        :type Content: str
        """
        self.Sdkappid = None
        self.Iccid = None
        self.Content = None


    def _deserialize(self, params):
        self.Sdkappid = params.get("Sdkappid")
        self.Iccid = params.get("Iccid")
        self.Content = params.get("Content")


class SendSmsResponse(AbstractModel):
    """SendSms返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 簡訊流水訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: :class:`taifucloudcloud.ic.v20190307.models.SmsSid`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = SmsSid()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class SmsRet(AbstractModel):
    """簡訊流水訊息

    """

    def __init__(self):
        """
        :param Code: 該iccid請求狀态
        :type Code: str
        :param Msg: 簡訊發送返回訊息
        :type Msg: str
        :param Iccid: 卡片ID
        :type Iccid: str
        :param Sid: 流水ID
        :type Sid: str
        """
        self.Code = None
        self.Msg = None
        self.Iccid = None
        self.Sid = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        self.Iccid = params.get("Iccid")
        self.Sid = params.get("Sid")


class SmsSid(AbstractModel):
    """簡訊流水訊息

    """

    def __init__(self):
        """
        :param Iccid: 卡片ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type Iccid: str
        :param Sid: 訊息流水ID
        :type Sid: str
        """
        self.Iccid = None
        self.Sid = None


    def _deserialize(self, params):
        self.Iccid = params.get("Iccid")
        self.Sid = params.get("Sid")