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


class CaptchaOperDataInterceptUnit(AbstractModel):
    """DescribeCaptchaOperData方法 攔截情況type = 2 返回的數據結構

    """

    def __init__(self):
        """
        :param DateKey: 時間
        :type DateKey: str
        :param AllStopCnt: 停止驗證數量
        :type AllStopCnt: float
        :param PicStopCnt: 圖片停止加載數量
        :type PicStopCnt: float
        :param StrategyStopCnt: 策略攔截數量
        :type StrategyStopCnt: float
        """
        self.DateKey = None
        self.AllStopCnt = None
        self.PicStopCnt = None
        self.StrategyStopCnt = None


    def _deserialize(self, params):
        self.DateKey = params.get("DateKey")
        self.AllStopCnt = params.get("AllStopCnt")
        self.PicStopCnt = params.get("PicStopCnt")
        self.StrategyStopCnt = params.get("StrategyStopCnt")


class CaptchaOperDataLoadTimeUnit(AbstractModel):
    """操作數據查詢方法DescribeCaptchaOperData 的返回結果，安全驗證碼加載耗時type = 1

    """

    def __init__(self):
        """
        :param DateKey: 時間
        :type DateKey: str
        :param MarketLoadTime: Market加載時間
        :type MarketLoadTime: float
        :param AppIdLoadTime: AppId加載時間
        :type AppIdLoadTime: float
        """
        self.DateKey = None
        self.MarketLoadTime = None
        self.AppIdLoadTime = None


    def _deserialize(self, params):
        self.DateKey = params.get("DateKey")
        self.MarketLoadTime = params.get("MarketLoadTime")
        self.AppIdLoadTime = params.get("AppIdLoadTime")


class CaptchaOperDataRes(AbstractModel):
    """DescribeCaptchaOperData 介面 返回數據類型集合

    """

    def __init__(self):
        """
        :param OperDataLoadTimeUnitArray: 驗證碼加載耗時數據返回
注意：此欄位可能返回 null，表示取不到有效值。
        :type OperDataLoadTimeUnitArray: list of CaptchaOperDataLoadTimeUnit
        :param OperDataInterceptUnitArray: 驗證碼攔截情況數據返回
注意：此欄位可能返回 null，表示取不到有效值。
        :type OperDataInterceptUnitArray: list of CaptchaOperDataInterceptUnit
        :param OperDataTryTimesUnitArray: 驗證碼嘗試次數數據返回
注意：此欄位可能返回 null，表示取不到有效值。
        :type OperDataTryTimesUnitArray: list of CaptchaOperDataTryTimesUnit
        :param OperDataTryTimesDistributeUnitArray: 驗證碼嘗試次數分布數據返回
注意：此欄位可能返回 null，表示取不到有效值。
        :type OperDataTryTimesDistributeUnitArray: list of CaptchaOperDataTryTimesDistributeUnit
        """
        self.OperDataLoadTimeUnitArray = None
        self.OperDataInterceptUnitArray = None
        self.OperDataTryTimesUnitArray = None
        self.OperDataTryTimesDistributeUnitArray = None


    def _deserialize(self, params):
        if params.get("OperDataLoadTimeUnitArray") is not None:
            self.OperDataLoadTimeUnitArray = []
            for item in params.get("OperDataLoadTimeUnitArray"):
                obj = CaptchaOperDataLoadTimeUnit()
                obj._deserialize(item)
                self.OperDataLoadTimeUnitArray.append(obj)
        if params.get("OperDataInterceptUnitArray") is not None:
            self.OperDataInterceptUnitArray = []
            for item in params.get("OperDataInterceptUnitArray"):
                obj = CaptchaOperDataInterceptUnit()
                obj._deserialize(item)
                self.OperDataInterceptUnitArray.append(obj)
        if params.get("OperDataTryTimesUnitArray") is not None:
            self.OperDataTryTimesUnitArray = []
            for item in params.get("OperDataTryTimesUnitArray"):
                obj = CaptchaOperDataTryTimesUnit()
                obj._deserialize(item)
                self.OperDataTryTimesUnitArray.append(obj)
        if params.get("OperDataTryTimesDistributeUnitArray") is not None:
            self.OperDataTryTimesDistributeUnitArray = []
            for item in params.get("OperDataTryTimesDistributeUnitArray"):
                obj = CaptchaOperDataTryTimesDistributeUnit()
                obj._deserialize(item)
                self.OperDataTryTimesDistributeUnitArray.append(obj)


class CaptchaOperDataTryTimesDistributeUnit(AbstractModel):
    """DescribeCaptchaOperData方法 嘗試次數分布 type = 4

    """

    def __init__(self):
        """
        :param TryCount: 嘗試次數
        :type TryCount: int
        :param UserCount: 用戶請求數量
        :type UserCount: int
        """
        self.TryCount = None
        self.UserCount = None


    def _deserialize(self, params):
        self.TryCount = params.get("TryCount")
        self.UserCount = params.get("UserCount")


class CaptchaOperDataTryTimesUnit(AbstractModel):
    """DescribeCaptchaOperData操作數據查詢嘗試次數 type = 3

    """

    def __init__(self):
        """
        :param DateKey: 時間
        :type DateKey: str
        :param CntPerPass: 平均嘗試次數
        :type CntPerPass: list of float
        :param MarketCntPerPass: market平均嘗試次數
        :type MarketCntPerPass: float
        """
        self.DateKey = None
        self.CntPerPass = None
        self.MarketCntPerPass = None


    def _deserialize(self, params):
        self.DateKey = params.get("DateKey")
        self.CntPerPass = params.get("CntPerPass")
        self.MarketCntPerPass = params.get("MarketCntPerPass")


class CaptchaQueryData(AbstractModel):
    """該類型爲DescribeCaptchaData 方法返回數據類型

    """

    def __init__(self):
        """
        :param Cnt: 數量
        :type Cnt: int
        :param Date: 時間
        :type Date: str
        """
        self.Cnt = None
        self.Date = None


    def _deserialize(self, params):
        self.Cnt = params.get("Cnt")
        self.Date = params.get("Date")


class CaptchaUserAllAppId(AbstractModel):
    """用戶注冊的APPID和應用名稱對象

    """

    def __init__(self):
        """
        :param CaptchaAppId: 驗證碼應用ID
        :type CaptchaAppId: int
        :param AppName: 注冊應用名稱
        :type AppName: str
        :param TcAppId: Top Cloud APPID
        :type TcAppId: int
        """
        self.CaptchaAppId = None
        self.AppName = None
        self.TcAppId = None


    def _deserialize(self, params):
        self.CaptchaAppId = params.get("CaptchaAppId")
        self.AppName = params.get("AppName")
        self.TcAppId = params.get("TcAppId")


class DescribeCaptchaAppIdInfoRequest(AbstractModel):
    """DescribeCaptchaAppIdInfo請求參數結構體

    """

    def __init__(self):
        """
        :param CaptchaAppId: 驗證碼應用注冊APPID
        :type CaptchaAppId: int
        """
        self.CaptchaAppId = None


    def _deserialize(self, params):
        self.CaptchaAppId = params.get("CaptchaAppId")


class DescribeCaptchaAppIdInfoResponse(AbstractModel):
    """DescribeCaptchaAppIdInfo返回參數結構體

    """

    def __init__(self):
        """
        :param SchemeColor: 界面風格
        :type SchemeColor: str
        :param Language: 語言
        :type Language: int
        :param SceneType: 場景
        :type SceneType: int
        :param EvilInterceptGrade: 防控風險等級
        :type EvilInterceptGrade: int
        :param SmartVerify: 智慧驗證
        :type SmartVerify: int
        :param SmartEngine: 智慧引擎
        :type SmartEngine: int
        :param CapType: 驗證碼類型
        :type CapType: int
        :param AppName: 應用名稱
        :type AppName: str
        :param DomainLimit: 域名限制
        :type DomainLimit: str
        :param MailAlarm: 郵件告警
注意：此欄位可能返回 null，表示取不到有效值。
        :type MailAlarm: list of str
        :param TrafficThreshold: 流量控制
        :type TrafficThreshold: int
        :param EncryptKey: 加密key
        :type EncryptKey: str
        :param TopFullScreen: 是否全屏
        :type TopFullScreen: int
        :param CaptchaCode: 成功返回0 其它失敗
        :type CaptchaCode: int
        :param CaptchaMsg: 返回操作訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SchemeColor = None
        self.Language = None
        self.SceneType = None
        self.EvilInterceptGrade = None
        self.SmartVerify = None
        self.SmartEngine = None
        self.CapType = None
        self.AppName = None
        self.DomainLimit = None
        self.MailAlarm = None
        self.TrafficThreshold = None
        self.EncryptKey = None
        self.TopFullScreen = None
        self.CaptchaCode = None
        self.CaptchaMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SchemeColor = params.get("SchemeColor")
        self.Language = params.get("Language")
        self.SceneType = params.get("SceneType")
        self.EvilInterceptGrade = params.get("EvilInterceptGrade")
        self.SmartVerify = params.get("SmartVerify")
        self.SmartEngine = params.get("SmartEngine")
        self.CapType = params.get("CapType")
        self.AppName = params.get("AppName")
        self.DomainLimit = params.get("DomainLimit")
        self.MailAlarm = params.get("MailAlarm")
        self.TrafficThreshold = params.get("TrafficThreshold")
        self.EncryptKey = params.get("EncryptKey")
        self.TopFullScreen = params.get("TopFullScreen")
        self.CaptchaCode = params.get("CaptchaCode")
        self.CaptchaMsg = params.get("CaptchaMsg")
        self.RequestId = params.get("RequestId")


class DescribeCaptchaDataRequest(AbstractModel):
    """DescribeCaptchaData請求參數結構體

    """

    def __init__(self):
        """
        :param CaptchaAppId: 驗證碼應用ID
        :type CaptchaAppId: int
        :param Start: 查詢開始時間
        :type Start: int
        :param End: 查詢結束時間
        :type End: int
        :param Type: 查詢類型
        :type Type: int
        """
        self.CaptchaAppId = None
        self.Start = None
        self.End = None
        self.Type = None


    def _deserialize(self, params):
        self.CaptchaAppId = params.get("CaptchaAppId")
        self.Start = params.get("Start")
        self.End = params.get("End")
        self.Type = params.get("Type")


class DescribeCaptchaDataResponse(AbstractModel):
    """DescribeCaptchaData返回參數結構體

    """

    def __init__(self):
        """
        :param CaptchaCode: 返回碼 0 成功 其它失敗
        :type CaptchaCode: int
        :param Data: 數據數組
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: list of CaptchaQueryData
        :param CaptchaMsg: 返回訊息描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CaptchaCode = None
        self.Data = None
        self.CaptchaMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CaptchaCode = params.get("CaptchaCode")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = CaptchaQueryData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.CaptchaMsg = params.get("CaptchaMsg")
        self.RequestId = params.get("RequestId")


class DescribeCaptchaDataSumRequest(AbstractModel):
    """DescribeCaptchaDataSum請求參數結構體

    """

    def __init__(self):
        """
        :param CaptchaAppId: 驗證碼應用ID
        :type CaptchaAppId: int
        :param Start: 查詢開始時間
        :type Start: int
        :param End: 查詢結束時間
        :type End: int
        """
        self.CaptchaAppId = None
        self.Start = None
        self.End = None


    def _deserialize(self, params):
        self.CaptchaAppId = params.get("CaptchaAppId")
        self.Start = params.get("Start")
        self.End = params.get("End")


class DescribeCaptchaDataSumResponse(AbstractModel):
    """DescribeCaptchaDataSum返回參數結構體

    """

    def __init__(self):
        """
        :param GetSum: 請求總量
        :type GetSum: int
        :param VfySuccSum: 請求驗證成功量
        :type VfySuccSum: int
        :param VfySum: 請求驗證量
        :type VfySum: int
        :param AttackSum: 攔截攻擊量
        :type AttackSum: int
        :param CaptchaMsg: 返回訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param CaptchaCode: 成功返回0  其它失敗
        :type CaptchaCode: int
        :param CheckTicketSum: 票據校驗量
        :type CheckTicketSum: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.GetSum = None
        self.VfySuccSum = None
        self.VfySum = None
        self.AttackSum = None
        self.CaptchaMsg = None
        self.CaptchaCode = None
        self.CheckTicketSum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GetSum = params.get("GetSum")
        self.VfySuccSum = params.get("VfySuccSum")
        self.VfySum = params.get("VfySum")
        self.AttackSum = params.get("AttackSum")
        self.CaptchaMsg = params.get("CaptchaMsg")
        self.CaptchaCode = params.get("CaptchaCode")
        self.CheckTicketSum = params.get("CheckTicketSum")
        self.RequestId = params.get("RequestId")


class DescribeCaptchaOperDataRequest(AbstractModel):
    """DescribeCaptchaOperData請求參數結構體

    """

    def __init__(self):
        """
        :param CaptchaAppId: 驗證碼應用ID
        :type CaptchaAppId: int
        :param Start: 查詢開始時間
        :type Start: int
        :param Type: 查詢類型
        :type Type: int
        """
        self.CaptchaAppId = None
        self.Start = None
        self.Type = None


    def _deserialize(self, params):
        self.CaptchaAppId = params.get("CaptchaAppId")
        self.Start = params.get("Start")
        self.Type = params.get("Type")


class DescribeCaptchaOperDataResponse(AbstractModel):
    """DescribeCaptchaOperData返回參數結構體

    """

    def __init__(self):
        """
        :param CaptchaCode: 成功返回 0 其它失敗
        :type CaptchaCode: int
        :param CaptchaMsg: 返回訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param Data: 用戶操作數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: :class:`taifucloudcloud.captcha.v20190722.models.CaptchaOperDataRes`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CaptchaCode = None
        self.CaptchaMsg = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CaptchaCode = params.get("CaptchaCode")
        self.CaptchaMsg = params.get("CaptchaMsg")
        if params.get("Data") is not None:
            self.Data = CaptchaOperDataRes()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeCaptchaResultRequest(AbstractModel):
    """DescribeCaptchaResult請求參數結構體

    """

    def __init__(self):
        """
        :param CaptchaType: 固定填值：9。可在控制台配置不同驗證碼類型。
        :type CaptchaType: int
        :param Ticket: 驗證碼返回給用戶的票據
        :type Ticket: str
        :param UserIp: 用戶操作來源的外網 IP
        :type UserIp: str
        :param Randstr: 驗證票據需要的随機字串
        :type Randstr: str
        :param CaptchaAppId: 驗證碼應用ID
        :type CaptchaAppId: int
        :param AppSecretKey: 用于服務器端校驗驗證碼票據的驗證金鑰，請妥善保密，請勿洩露給第三方
        :type AppSecretKey: str
        :param BusinessId: 業務 ID，網站或應用在多個業務中使用此服務，通過此 ID 區分統計數據
        :type BusinessId: int
        :param SceneId: 場景 ID，網站或應用的業務下有多個場景使用此服務，通過此 ID 區分統計數據
        :type SceneId: int
        :param MacAddress: mac 網址或設備唯一标識
        :type MacAddress: str
        :param Imei: 手機設備号
        :type Imei: str
        :param NeedGetCaptchaTime: 是否返回前端獲取驗證碼時間，取值1：需要返回
        :type NeedGetCaptchaTime: int
        """
        self.CaptchaType = None
        self.Ticket = None
        self.UserIp = None
        self.Randstr = None
        self.CaptchaAppId = None
        self.AppSecretKey = None
        self.BusinessId = None
        self.SceneId = None
        self.MacAddress = None
        self.Imei = None
        self.NeedGetCaptchaTime = None


    def _deserialize(self, params):
        self.CaptchaType = params.get("CaptchaType")
        self.Ticket = params.get("Ticket")
        self.UserIp = params.get("UserIp")
        self.Randstr = params.get("Randstr")
        self.CaptchaAppId = params.get("CaptchaAppId")
        self.AppSecretKey = params.get("AppSecretKey")
        self.BusinessId = params.get("BusinessId")
        self.SceneId = params.get("SceneId")
        self.MacAddress = params.get("MacAddress")
        self.Imei = params.get("Imei")
        self.NeedGetCaptchaTime = params.get("NeedGetCaptchaTime")


class DescribeCaptchaResultResponse(AbstractModel):
    """DescribeCaptchaResult返回參數結構體

    """

    def __init__(self):
        """
        :param CaptchaCode: 1	OK	驗證通過
6	user code len error	驗證碼長度不比對
7	captcha no match	驗證碼答案不比對/Randstr參數不比對
8	verify timeout	驗證碼簽名超時
9	Sequnce repeat	驗證碼簽名重放
10	Sequnce invalid	驗證碼簽名序列
11	Cookie invalid	驗證碼cooking訊息不合法
12	sig len error	簽名長度錯誤
13	verify ip no match	ip不比對
15	decrypt fail	驗證碼簽名解密失敗
16	appid no match	驗證碼強校驗appid錯誤
17	cmd no much	驗證碼系統命令不比對
18	uin no match	号碼不比對
19	seq redirect	重定向驗證
20	opt no vcode	操作使用pt免驗證碼校驗錯誤
21	diff	差别，驗證錯誤
22	captcha type not match	驗證碼類型與拉取時不一緻
23	verify type error	驗證類型錯誤
24	invalid pkg	非法請求包
25	bad visitor	策略攔截
26	system busy	系統内部錯誤
100	param err	appsecretkey 參數校驗錯誤
        :type CaptchaCode: int
        :param CaptchaMsg: 狀态描述及驗證錯誤訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param EvilLevel: [0,100]，惡意等級
注意：此欄位可能返回 null，表示取不到有效值。
        :type EvilLevel: int
        :param GetCaptchaTime: 前端獲取驗證碼時間，時間戳格式
注意：此欄位可能返回 null，表示取不到有效值。
        :type GetCaptchaTime: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CaptchaCode = None
        self.CaptchaMsg = None
        self.EvilLevel = None
        self.GetCaptchaTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CaptchaCode = params.get("CaptchaCode")
        self.CaptchaMsg = params.get("CaptchaMsg")
        self.EvilLevel = params.get("EvilLevel")
        self.GetCaptchaTime = params.get("GetCaptchaTime")
        self.RequestId = params.get("RequestId")


class DescribeCaptchaUserAllAppIdRequest(AbstractModel):
    """DescribeCaptchaUserAllAppId請求參數結構體

    """


class DescribeCaptchaUserAllAppIdResponse(AbstractModel):
    """DescribeCaptchaUserAllAppId返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 用戶注冊的所有Appid和應用名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: list of CaptchaUserAllAppId
        :param CaptchaCode: 成功返回 0  其它失敗
        :type CaptchaCode: int
        :param CaptchaMsg: 返回操作訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.CaptchaCode = None
        self.CaptchaMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = CaptchaUserAllAppId()
                obj._deserialize(item)
                self.Data.append(obj)
        self.CaptchaCode = params.get("CaptchaCode")
        self.CaptchaMsg = params.get("CaptchaMsg")
        self.RequestId = params.get("RequestId")


class UpdateCaptchaAppIdInfoRequest(AbstractModel):
    """UpdateCaptchaAppIdInfo請求參數結構體

    """

    def __init__(self):
        """
        :param CaptchaAppId: 驗證碼應用ID
        :type CaptchaAppId: int
        :param AppName: 應用名
        :type AppName: str
        :param DomainLimit: 域名限制
        :type DomainLimit: str
        :param SceneType: 場景類型
        :type SceneType: int
        :param CapType: 驗證碼類型
        :type CapType: int
        :param EvilInterceptGrade: 風險級别
        :type EvilInterceptGrade: int
        :param SmartVerify: 智慧檢測
        :type SmartVerify: int
        :param SmartEngine: 開啓智慧引擎
        :type SmartEngine: int
        :param SchemeColor: web風格
        :type SchemeColor: str
        :param CaptchaLanguage: 語言
        :type CaptchaLanguage: int
        :param MailAlarm: 告警電子信箱
        :type MailAlarm: str
        :param TopFullScreen: 是否全屏
        :type TopFullScreen: int
        :param TrafficThreshold: 流量限制
        :type TrafficThreshold: int
        """
        self.CaptchaAppId = None
        self.AppName = None
        self.DomainLimit = None
        self.SceneType = None
        self.CapType = None
        self.EvilInterceptGrade = None
        self.SmartVerify = None
        self.SmartEngine = None
        self.SchemeColor = None
        self.CaptchaLanguage = None
        self.MailAlarm = None
        self.TopFullScreen = None
        self.TrafficThreshold = None


    def _deserialize(self, params):
        self.CaptchaAppId = params.get("CaptchaAppId")
        self.AppName = params.get("AppName")
        self.DomainLimit = params.get("DomainLimit")
        self.SceneType = params.get("SceneType")
        self.CapType = params.get("CapType")
        self.EvilInterceptGrade = params.get("EvilInterceptGrade")
        self.SmartVerify = params.get("SmartVerify")
        self.SmartEngine = params.get("SmartEngine")
        self.SchemeColor = params.get("SchemeColor")
        self.CaptchaLanguage = params.get("CaptchaLanguage")
        self.MailAlarm = params.get("MailAlarm")
        self.TopFullScreen = params.get("TopFullScreen")
        self.TrafficThreshold = params.get("TrafficThreshold")


class UpdateCaptchaAppIdInfoResponse(AbstractModel):
    """UpdateCaptchaAppIdInfo返回參數結構體

    """

    def __init__(self):
        """
        :param CaptchaCode: 返回碼 0 成功，其它失敗
        :type CaptchaCode: int
        :param CaptchaMsg: 返回操作訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type CaptchaMsg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CaptchaCode = None
        self.CaptchaMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CaptchaCode = params.get("CaptchaCode")
        self.CaptchaMsg = params.get("CaptchaMsg")
        self.RequestId = params.get("RequestId")