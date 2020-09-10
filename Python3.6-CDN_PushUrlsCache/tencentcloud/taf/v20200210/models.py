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


class DetectAccountActivityRequest(AbstractModel):
    """DetectAccountActivity請求參數結構體

    """

    def __init__(self):
        """
        :param BusinessSecurityData: 業務入參
        :type BusinessSecurityData: :class:`tencentcloud.taf.v20200210.models.InputDetectAccountActivity`
        """
        self.BusinessSecurityData = None


    def _deserialize(self, params):
        if params.get("BusinessSecurityData") is not None:
            self.BusinessSecurityData = InputDetectAccountActivity()
            self.BusinessSecurityData._deserialize(params.get("BusinessSecurityData"))


class DetectAccountActivityResponse(AbstractModel):
    """DetectAccountActivity返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 回包數據
        :type Data: :class:`tencentcloud.taf.v20200210.models.OutputDetectAccountActivity`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = OutputDetectAccountActivity()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DetectFraudKOLRequest(AbstractModel):
    """DetectFraudKOL請求參數結構體

    """

    def __init__(self):
        """
        :param BspData: 業務數據
        :type BspData: :class:`tencentcloud.taf.v20200210.models.InputKolBspData`
        """
        self.BspData = None


    def _deserialize(self, params):
        if params.get("BspData") is not None:
            self.BspData = InputKolBspData()
            self.BspData._deserialize(params.get("BspData"))


class DetectFraudKOLResponse(AbstractModel):
    """DetectFraudKOL返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 回包數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.taf.v20200210.models.OutputKolData`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = OutputKolData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class EnhanceTaDegreeRequest(AbstractModel):
    """EnhanceTaDegree請求參數結構體

    """

    def __init__(self):
        """
        :param BspData: 業務數據
        :type BspData: :class:`tencentcloud.taf.v20200210.models.InputTaBspData`
        """
        self.BspData = None


    def _deserialize(self, params):
        if params.get("BspData") is not None:
            self.BspData = InputTaBspData()
            self.BspData._deserialize(params.get("BspData"))


class EnhanceTaDegreeResponse(AbstractModel):
    """EnhanceTaDegree返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 回包數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.taf.v20200210.models.OutputTaData`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = OutputTaData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class InputDetectAccountActivity(AbstractModel):
    """業務入參

    """

    def __init__(self):
        """
        :param Uid: 用戶ID值，如微信/QQ openid，或 手機号等（如15912345687）
        :type Uid: str
        :param AccountType: 用戶賬号類型 
1：QQ開放帳号 
2：微信開放賬号 
4：手機号 （暫僅支援國内手機号）
10004： 手機号MD5
        :type AccountType: int
        :param UserIp: 用戶真實外網IP
        :type UserIp: str
        :param PostTime: 用戶操作時間戳，單位秒（格林威治時間精确到秒，如1501590972）
        :type PostTime: int
        :param AppIdU: accountType是QQ或微信開放賬号時，該參數必填，表示QQ或微信分配給網站或應用的appId，用來唯一标識網站或應用
        :type AppIdU: str
        :param NickName: 昵稱，UTF-8 編碼
        :type NickName: str
        :param PhoneNumber: 手機号。若 accountType 選4（手機号）、或10004（手機号 MD5），則無需重複填寫。否則填入對應的手機号（如15912345687）
        :type PhoneNumber: str
        :param EmailAddress: 用戶電子信箱網址（非系統自動生成）
        :type EmailAddress: str
        :param CookieHash: 用戶 HTTP 請求中的 cookie 進行2次 hash 的值，只要保證相同 cookie 的 hash 值一緻即可
        :type CookieHash: float
        :param UserAgent: 用戶HTTP請求的 userAgent
        :type UserAgent: str
        :param XForwardedFor: 用戶HTTP請求中的 x_forward_for
        :type XForwardedFor: str
        :param MacAddress: Mac網址或設備唯一标識
        :type MacAddress: str
        :param VendorId: 手機制造商ID，如果手機注冊，請帶上此訊息
        :type VendorId: str
        :param Imei: 手機設備号
        :type Imei: str
        """
        self.Uid = None
        self.AccountType = None
        self.UserIp = None
        self.PostTime = None
        self.AppIdU = None
        self.NickName = None
        self.PhoneNumber = None
        self.EmailAddress = None
        self.CookieHash = None
        self.UserAgent = None
        self.XForwardedFor = None
        self.MacAddress = None
        self.VendorId = None
        self.Imei = None


    def _deserialize(self, params):
        self.Uid = params.get("Uid")
        self.AccountType = params.get("AccountType")
        self.UserIp = params.get("UserIp")
        self.PostTime = params.get("PostTime")
        self.AppIdU = params.get("AppIdU")
        self.NickName = params.get("NickName")
        self.PhoneNumber = params.get("PhoneNumber")
        self.EmailAddress = params.get("EmailAddress")
        self.CookieHash = params.get("CookieHash")
        self.UserAgent = params.get("UserAgent")
        self.XForwardedFor = params.get("XForwardedFor")
        self.MacAddress = params.get("MacAddress")
        self.VendorId = params.get("VendorId")
        self.Imei = params.get("Imei")


class InputKolBspData(AbstractModel):
    """CheckKol

    """

    def __init__(self):
        """
        :param DataList: BspData
        :type DataList: list of InputKolDataList
        """
        self.DataList = None


    def _deserialize(self, params):
        if params.get("DataList") is not None:
            self.DataList = []
            for item in params.get("DataList"):
                obj = InputKolDataList()
                obj._deserialize(item)
                self.DataList.append(obj)


class InputKolDataList(AbstractModel):
    """CheckKol

    """

    def __init__(self):
        """
        :param Type: 賬号類型[1：微信；2：qq；3：微博]
        :type Type: int
        :param Id: KOL賬号ID[比如微信公衆号ID]
        :type Id: str
        :param Name: KOL名稱
        :type Name: str
        :param Phone: 手機号
        :type Phone: str
        :param AgentInfo: 代理商名稱
        :type AgentInfo: str
        """
        self.Type = None
        self.Id = None
        self.Name = None
        self.Phone = None
        self.AgentInfo = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Phone = params.get("Phone")
        self.AgentInfo = params.get("AgentInfo")


class InputRecognizeTargetAudience(AbstractModel):
    """流量反欺詐-驗準入參

    """

    def __init__(self):
        """
        :param Uid: 設備ID，AccountType指定的類型
        :type Uid: str
        :param AccountType: 設備号類型，1.imei 2.imeiMd5（小寫後轉MD5轉小寫）3.idfa， 4.idfaMd5（大寫後轉MD5轉小寫），5.手機号,256.其它
        :type AccountType: int
        :param ModelIdList: 模型ID清單
        :type ModelIdList: list of int
        :param Ip: 用戶IP
        :type Ip: str
        :param Os: 作業系統類型(unknown，android，ios，windows)
        :type Os: str
        :param Osv: 作業系統版本
        :type Osv: str
        :param Lat: 緯度
        :type Lat: str
        :param Lon: 經度
        :type Lon: str
        :param DeviceModel: 設備型号(MI 6)
        :type DeviceModel: str
        :param BidFloor: 競價底價
        :type BidFloor: int
        :param Age: 年齡
        :type Age: int
        :param Gender: 性别(1.MALE 2.FEMALE)
        :type Gender: int
        :param Location: 用戶網址
        :type Location: str
        :param DeliveryMode: 投放模式（0=PDB，1=PD，2=RTB，10=其他）
        :type DeliveryMode: int
        :param AdvertisingType: 廣告位類型<br />（0=前貼片，1=開屏廣告，2=網頁頭部廣告、3=網頁中部廣告、4=網頁底部廣告、5=懸浮廣告、10=其它）
        :type AdvertisingType: int
        :param Mac: mac網址，建議提供
        :type Mac: str
        :param Phone: 電話号碼
        :type Phone: str
        :param Ua: 浏覽器類型
        :type Ua: str
        :param App: 用戶端應用
        :type App: str
        :param Package: 應用包名
        :type Package: str
        :param Maker: 設備制造商
        :type Maker: str
        :param DeviceType: 設備類型（PHONE,TABLET）
        :type DeviceType: str
        :param AccessMode: 入網方式(wifi,4g,3g,2g)
        :type AccessMode: str
        :param Sp: 運營商(1.移動 2.聯通 3.電信等)
        :type Sp: int
        :param DeviceW: 設備螢幕分辨率寬度像素數
        :type DeviceW: int
        :param DeviceH: 設備螢幕分辨率高度像素數
        :type DeviceH: int
        :param FullScreen: 是否全屏插廣告(0-否，1-是)
        :type FullScreen: int
        :param ImpBannerW: 廣告位寬度
        :type ImpBannerW: int
        :param ImpBannerH: 廣告位高度
        :type ImpBannerH: int
        :param Url: 網址
        :type Url: str
        :param Context: 上下文訊息
        :type Context: str
        :param Channel: 管道
        :type Channel: str
        :param ReqId: 請求ID
        :type ReqId: str
        :param ReqMd5: 請求ID的md5值
        :type ReqMd5: str
        :param AdType: ad_type
        :type AdType: int
        :param AppName: app name
        :type AppName: str
        :param AppVer: appVer
        :type AppVer: str
        :param ReqType: 競價模式1：rtb 2:pd
        :type ReqType: int
        """
        self.Uid = None
        self.AccountType = None
        self.ModelIdList = None
        self.Ip = None
        self.Os = None
        self.Osv = None
        self.Lat = None
        self.Lon = None
        self.DeviceModel = None
        self.BidFloor = None
        self.Age = None
        self.Gender = None
        self.Location = None
        self.DeliveryMode = None
        self.AdvertisingType = None
        self.Mac = None
        self.Phone = None
        self.Ua = None
        self.App = None
        self.Package = None
        self.Maker = None
        self.DeviceType = None
        self.AccessMode = None
        self.Sp = None
        self.DeviceW = None
        self.DeviceH = None
        self.FullScreen = None
        self.ImpBannerW = None
        self.ImpBannerH = None
        self.Url = None
        self.Context = None
        self.Channel = None
        self.ReqId = None
        self.ReqMd5 = None
        self.AdType = None
        self.AppName = None
        self.AppVer = None
        self.ReqType = None


    def _deserialize(self, params):
        self.Uid = params.get("Uid")
        self.AccountType = params.get("AccountType")
        self.ModelIdList = params.get("ModelIdList")
        self.Ip = params.get("Ip")
        self.Os = params.get("Os")
        self.Osv = params.get("Osv")
        self.Lat = params.get("Lat")
        self.Lon = params.get("Lon")
        self.DeviceModel = params.get("DeviceModel")
        self.BidFloor = params.get("BidFloor")
        self.Age = params.get("Age")
        self.Gender = params.get("Gender")
        self.Location = params.get("Location")
        self.DeliveryMode = params.get("DeliveryMode")
        self.AdvertisingType = params.get("AdvertisingType")
        self.Mac = params.get("Mac")
        self.Phone = params.get("Phone")
        self.Ua = params.get("Ua")
        self.App = params.get("App")
        self.Package = params.get("Package")
        self.Maker = params.get("Maker")
        self.DeviceType = params.get("DeviceType")
        self.AccessMode = params.get("AccessMode")
        self.Sp = params.get("Sp")
        self.DeviceW = params.get("DeviceW")
        self.DeviceH = params.get("DeviceH")
        self.FullScreen = params.get("FullScreen")
        self.ImpBannerW = params.get("ImpBannerW")
        self.ImpBannerH = params.get("ImpBannerH")
        self.Url = params.get("Url")
        self.Context = params.get("Context")
        self.Channel = params.get("Channel")
        self.ReqId = params.get("ReqId")
        self.ReqMd5 = params.get("ReqMd5")
        self.AdType = params.get("AdType")
        self.AppName = params.get("AppName")
        self.AppVer = params.get("AppVer")
        self.ReqType = params.get("ReqType")


class InputSendTrafficSecuritySmsMsg(AbstractModel):
    """業務入參

    """

    def __init__(self):
        """
        :param TaskId: 投放任務ID
        :type TaskId: str
        :param Mobiles: 手機号碼清單（号碼量<=200）
        :type Mobiles: list of str
        """
        self.TaskId = None
        self.Mobiles = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Mobiles = params.get("Mobiles")


class InputTaBspData(AbstractModel):
    """流量反欺詐-虛假TA識别

    """

    def __init__(self):
        """
        :param Seq: 請求序列号
        :type Seq: int
        :param OsType: 作業系統類型[0：未知；1：android；2：ios；3：windows]
        :type OsType: str
        :param AgeFloor: 年齡下限
        :type AgeFloor: int
        :param AgeCeil: 年齡上限
        :type AgeCeil: int
        :param Gender: 性别[1：男；2：女]
        :type Gender: int
        :param UserTime: 用戶操作時間
        :type UserTime: int
        :param Imei: Imei [在(Imei|ImeiMd5|Idfa|IdfaMd5)裏面4選1]
        :type Imei: str
        :param ImeiMd5: Imei小寫後加密Md5 [在(Imei|ImeiMd5|Idfa|IdfaMd5)裏面4選1]
        :type ImeiMd5: str
        :param Idfa: Idfa [在(Imei|ImeiMd5|Idfa|IdfaMd5)裏面4選1]
        :type Idfa: str
        :param IdfaMd5: Idfa大寫後加密Md5 [在(Imei|ImeiMd5|Idfa|IdfaMd5)裏面4選1]
        :type IdfaMd5: str
        :param UserIp: 用戶IP
        :type UserIp: str
        :param Mac: MAC網址[建議提供]
        :type Mac: str
        :param PhoneNum: 手機号碼[中國大陸]
        :type PhoneNum: str
        :param UserAgent: 浏覽器
        :type UserAgent: str
        :param App: APP名稱
        :type App: str
        :param Package: 應用安裝包名稱
        :type Package: str
        :param DeviceMaker: 設備制造商
        :type DeviceMaker: str
        :param DeviceModule: 設備型号
        :type DeviceModule: str
        :param AccessMode: 入網方式[1：WIFI；2：4G；3：3G；4：2G；5：其它]
        :type AccessMode: str
        :param Sp: 運營商[1：移動；2：聯通；3：電信；4：其它]
        :type Sp: str
        :param Url: 網址
        :type Url: str
        :param Location: 用戶網址
        :type Location: str
        :param Latitude: 緯度
        :type Latitude: str
        :param Longitude: 精度
        :type Longitude: str
        :param Context: 輔助區分訊息
        :type Context: str
        """
        self.Seq = None
        self.OsType = None
        self.AgeFloor = None
        self.AgeCeil = None
        self.Gender = None
        self.UserTime = None
        self.Imei = None
        self.ImeiMd5 = None
        self.Idfa = None
        self.IdfaMd5 = None
        self.UserIp = None
        self.Mac = None
        self.PhoneNum = None
        self.UserAgent = None
        self.App = None
        self.Package = None
        self.DeviceMaker = None
        self.DeviceModule = None
        self.AccessMode = None
        self.Sp = None
        self.Url = None
        self.Location = None
        self.Latitude = None
        self.Longitude = None
        self.Context = None


    def _deserialize(self, params):
        self.Seq = params.get("Seq")
        self.OsType = params.get("OsType")
        self.AgeFloor = params.get("AgeFloor")
        self.AgeCeil = params.get("AgeCeil")
        self.Gender = params.get("Gender")
        self.UserTime = params.get("UserTime")
        self.Imei = params.get("Imei")
        self.ImeiMd5 = params.get("ImeiMd5")
        self.Idfa = params.get("Idfa")
        self.IdfaMd5 = params.get("IdfaMd5")
        self.UserIp = params.get("UserIp")
        self.Mac = params.get("Mac")
        self.PhoneNum = params.get("PhoneNum")
        self.UserAgent = params.get("UserAgent")
        self.App = params.get("App")
        self.Package = params.get("Package")
        self.DeviceMaker = params.get("DeviceMaker")
        self.DeviceModule = params.get("DeviceModule")
        self.AccessMode = params.get("AccessMode")
        self.Sp = params.get("Sp")
        self.Url = params.get("Url")
        self.Location = params.get("Location")
        self.Latitude = params.get("Latitude")
        self.Longitude = params.get("Longitude")
        self.Context = params.get("Context")


class OutputDetectAccountActivity(AbstractModel):
    """業務出參

    """

    def __init__(self):
        """
        :param Code: 返回碼（0，成功，其他失敗）
注意：此欄位可能返回 null，表示取不到有效值。
        :type Code: int
        :param Message: 返回碼對應的訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param Value: 返回活躍度訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Value: :class:`tencentcloud.taf.v20200210.models.OutputDetectAccountActivityValue`
        """
        self.Code = None
        self.Message = None
        self.Value = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        if params.get("Value") is not None:
            self.Value = OutputDetectAccountActivityValue()
            self.Value._deserialize(params.get("Value"))


class OutputDetectAccountActivityValue(AbstractModel):
    """業務出參

    """

    def __init__(self):
        """
        :param Uid: 用戶 ID accountType 不同對應不同的用戶 ID。如是 QQ 或微信用戶則填入對應的 openId
注意：此欄位可能返回 null，表示取不到有效值。
        :type Uid: str
        :param PostTime: 操作時間戳，單位：秒
注意：此欄位可能返回 null，表示取不到有效值。
        :type PostTime: int
        :param UserIp: 用戶操作的真實外網 IP
注意：此欄位可能返回 null，表示取不到有效值。
        :type UserIp: str
        :param Level: 0：表示不活躍
1 - 4：活躍等級由低到高
注意：此欄位可能返回 null，表示取不到有效值。
        :type Level: int
        :param Type: 賬号标簽：
3，無效賬号，送檢賬号參數無法成功解析，請檢查微信openid是否有誤 ，QQopenid是否與appidU對應，手機号是否有誤。
4，黑名單，該賬号在業務側有過拉黑記錄
5，白名單，該賬号在業務側有過加白名單記錄

環境标簽：
205，非公網有效ip，傳進來的IP網址爲内網ip網址或者ip保留網址；
注意：此欄位可能返回 null，表示取不到有效值。
        :type Type: list of int
        """
        self.Uid = None
        self.PostTime = None
        self.UserIp = None
        self.Level = None
        self.Type = None


    def _deserialize(self, params):
        self.Uid = params.get("Uid")
        self.PostTime = params.get("PostTime")
        self.UserIp = params.get("UserIp")
        self.Level = params.get("Level")
        self.Type = params.get("Type")


class OutputKolData(AbstractModel):
    """CheckKol

    """

    def __init__(self):
        """
        :param Code: 錯誤碼[0:成功；非0：失敗的錯誤碼]
注意：此欄位可能返回 null，表示取不到有效值。
        :type Code: int
        :param Message: 錯誤訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param Value: 業務返回數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type Value: list of OutputKolValue
        """
        self.Code = None
        self.Message = None
        self.Value = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        if params.get("Value") is not None:
            self.Value = []
            for item in params.get("Value"):
                obj = OutputKolValue()
                obj._deserialize(item)
                self.Value.append(obj)


class OutputKolValue(AbstractModel):
    """CheckKol

    """

    def __init__(self):
        """
        :param Id: KOL賬号ID[比如微信公衆号ID]
注意：此欄位可能返回 null，表示取不到有效值。
        :type Id: str
        :param IsCheck: 是否查得[0：未查得；1：查得]
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsCheck: int
        :param FraudPScore: 作弊的可能性[0～100]
注意：此欄位可能返回 null，表示取不到有效值。
        :type FraudPScore: int
        :param EvilPScore: 作弊的嚴重性[0～100]
注意：此欄位可能返回 null，表示取不到有效值。
        :type EvilPScore: int
        """
        self.Id = None
        self.IsCheck = None
        self.FraudPScore = None
        self.EvilPScore = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.IsCheck = params.get("IsCheck")
        self.FraudPScore = params.get("FraudPScore")
        self.EvilPScore = params.get("EvilPScore")


class OutputRecognizeTargetAudience(AbstractModel):
    """流量反欺詐-驗準返回值

    """

    def __init__(self):
        """
        :param Code: 返回碼（0，成功，其他失敗）
        :type Code: int
        :param Message: 返回碼對應的訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param Value: 返回模型結果
注意：此欄位可能返回 null，表示取不到有效值。
        :type Value: list of OutputRecognizeTargetAudienceValue
        """
        self.Code = None
        self.Message = None
        self.Value = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        if params.get("Value") is not None:
            self.Value = []
            for item in params.get("Value"):
                obj = OutputRecognizeTargetAudienceValue()
                obj._deserialize(item)
                self.Value.append(obj)


class OutputRecognizeTargetAudienceValue(AbstractModel):
    """流量反欺詐-驗準返回的查詢分值

    """

    def __init__(self):
        """
        :param ModelId: 模型ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ModelId: int
        :param IsFound: 是否正常返回結果
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsFound: int
        :param Score: 返回分值
注意：此欄位可能返回 null，表示取不到有效值。
        :type Score: float
        """
        self.ModelId = None
        self.IsFound = None
        self.Score = None


    def _deserialize(self, params):
        self.ModelId = params.get("ModelId")
        self.IsFound = params.get("IsFound")
        self.Score = params.get("Score")


class OutputSendTrafficSecuritySmsMsg(AbstractModel):
    """返回結果

    """

    def __init__(self):
        """
        :param Code: 返回碼（0：介面調用成功 非0：介面調用失敗）
        :type Code: int
        :param Message: 返回碼對應的訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param Value: 發送失敗的号碼清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Value: list of str
        """
        self.Code = None
        self.Message = None
        self.Value = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        self.Value = params.get("Value")


class OutputTaData(AbstractModel):
    """流量反欺詐-虛假TA識别

    """

    def __init__(self):
        """
        :param Code: 錯誤碼[0:成功；非0：失敗的錯誤碼]
        :type Code: int
        :param Message: 錯誤訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param Value: 結果數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type Value: :class:`tencentcloud.taf.v20200210.models.OutputTaValue`
        """
        self.Code = None
        self.Message = None
        self.Value = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        if params.get("Value") is not None:
            self.Value = OutputTaValue()
            self.Value._deserialize(params.get("Value"))


class OutputTaValue(AbstractModel):
    """流量反欺詐-虛假TA識别

    """

    def __init__(self):
        """
        :param IsCheck: 是否查得[0：未查得；1：查得]
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsCheck: int
        :param IsMatch: 是否符合[0：不符合；1：符合]
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsMatch: int
        """
        self.IsCheck = None
        self.IsMatch = None


    def _deserialize(self, params):
        self.IsCheck = params.get("IsCheck")
        self.IsMatch = params.get("IsMatch")


class RecognizeCustomizedAudienceRequest(AbstractModel):
    """RecognizeCustomizedAudience請求參數結構體

    """

    def __init__(self):
        """
        :param BspData: 業務入參
        :type BspData: :class:`tencentcloud.taf.v20200210.models.InputRecognizeTargetAudience`
        """
        self.BspData = None


    def _deserialize(self, params):
        if params.get("BspData") is not None:
            self.BspData = InputRecognizeTargetAudience()
            self.BspData._deserialize(params.get("BspData"))


class RecognizeCustomizedAudienceResponse(AbstractModel):
    """RecognizeCustomizedAudience返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 業務出參
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.taf.v20200210.models.OutputRecognizeTargetAudience`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = OutputRecognizeTargetAudience()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class RecognizePreciseTargetAudienceRequest(AbstractModel):
    """RecognizePreciseTargetAudience請求參數結構體

    """

    def __init__(self):
        """
        :param BspData: 業務數據
        :type BspData: :class:`tencentcloud.taf.v20200210.models.InputRecognizeTargetAudience`
        """
        self.BspData = None


    def _deserialize(self, params):
        if params.get("BspData") is not None:
            self.BspData = InputRecognizeTargetAudience()
            self.BspData._deserialize(params.get("BspData"))


class RecognizePreciseTargetAudienceResponse(AbstractModel):
    """RecognizePreciseTargetAudience返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 回包數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.taf.v20200210.models.OutputRecognizeTargetAudience`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = OutputRecognizeTargetAudience()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class RecognizeTargetAudienceRequest(AbstractModel):
    """RecognizeTargetAudience請求參數結構體

    """

    def __init__(self):
        """
        :param BspData: 業務數據
        :type BspData: :class:`tencentcloud.taf.v20200210.models.InputRecognizeTargetAudience`
        """
        self.BspData = None


    def _deserialize(self, params):
        if params.get("BspData") is not None:
            self.BspData = InputRecognizeTargetAudience()
            self.BspData._deserialize(params.get("BspData"))


class RecognizeTargetAudienceResponse(AbstractModel):
    """RecognizeTargetAudience返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 回包數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.taf.v20200210.models.OutputRecognizeTargetAudience`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = OutputRecognizeTargetAudience()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class SendTrafficSecuritySmsMessageRequest(AbstractModel):
    """SendTrafficSecuritySmsMessage請求參數結構體

    """

    def __init__(self):
        """
        :param BspData: 業務入參
        :type BspData: :class:`tencentcloud.taf.v20200210.models.InputSendTrafficSecuritySmsMsg`
        """
        self.BspData = None


    def _deserialize(self, params):
        if params.get("BspData") is not None:
            self.BspData = InputSendTrafficSecuritySmsMsg()
            self.BspData._deserialize(params.get("BspData"))


class SendTrafficSecuritySmsMessageResponse(AbstractModel):
    """SendTrafficSecuritySmsMessage返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 返回結果
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.taf.v20200210.models.OutputSendTrafficSecuritySmsMsg`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = OutputSendTrafficSecuritySmsMsg()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")