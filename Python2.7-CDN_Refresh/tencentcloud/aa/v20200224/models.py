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


class QueryActivityAntiRushRequest(AbstractModel):
    """QueryActivityAntiRush請求參數結構體

    """

    def __init__(self):
        """
        :param AccountType: 用戶賬號類型（預設開通   開放賬號、手機號，手機 MD5 賬號類型查詢。如需使用 開放賬號，則需要 提交工單 由Top Cloud 進行資格審核，審核通過後方可正常使用 開放賬號）：
1：  開放帳號。
2： 開放賬號。
4：手機號。
0：其他。
10004：手機號 MD5。
        :type AccountType: str
        :param Uid: 用戶 ID 不同的 accountType 對應不同的用戶 ID。如果是  ，則填入對應的 openid， 用戶則填入對應的 openid/unionid，手機號則填入對應真實用戶手機號（如13123456789）。
        :type Uid: str
        :param UserIp: 用戶的真實外網 IP。若填入非外網有效ip，會返回level=0的風控結果，risktype中會有205的風險碼返回作爲標識
        :type UserIp: str
        :param PostTime: 用戶操作時間戳。
        :type PostTime: str
        :param AppIdU: accountType 是 開放賬號時，該參數必填，表示   開放平台分配給網站或應用的 AppID，用來唯一標識網站或應用。
        :type AppIdU: str
        :param NickName: 昵稱，UTF-8 編碼。
        :type NickName: str
        :param PhoneNumber: 手機號。若 accountType 選4（手機號）、或10004（手機號 MD5），則無需重複填寫。否則填入對應的手機號（如15912345687）。accountType爲1或2時，該欄位支援MD5值；
        :type PhoneNumber: str
        :param EmailAddress: 用戶電子信箱網址。
        :type EmailAddress: str
        :param RegisterTime: 注冊時間戳。
        :type RegisterTime: str
        :param RegisterIp: 注冊來源的外網 IP。
        :type RegisterIp: str
        :param CookieHash: 用戶 HTTP 請求中的 cookie 進行2次 hash 的值，只要保證相同 cookie 的 hash 值一緻即可。
        :type CookieHash: str
        :param Address: 網址。
        :type Address: str
        :param LoginSource: 登入來源：
0：其他。
1：PC 網頁。
2： 頁面。
3：App。
4： 公衆號。
        :type LoginSource: str
        :param LoginType: 登入方式：
0：其他。
1：手動賬號密碼輸入。
2：動态簡訊密碼登入。
3：二維碼掃描登入。
        :type LoginType: str
        :param LoginSpend: 登入耗時，單位：秒。
        :type LoginSpend: str
        :param RootId: 用戶操作的目的 ID，如點贊等，該欄位就是被點贊的訊息 ID，如果是投票，則爲被投號碼的 ID。
        :type RootId: str
        :param Referer: 用戶 HTTP 請求的 referer 值。
        :type Referer: str
        :param JumpUrl: 登入成功後跳轉頁面。
        :type JumpUrl: str
        :param UserAgent: 用戶 HTTP 請求的 userAgent。
        :type UserAgent: str
        :param XForwardedFor: 用戶 HTTP 請求中的 x_forward_for。
        :type XForwardedFor: str
        :param MouseClickCount: 用戶操作過程中鼠標點擊次數。
        :type MouseClickCount: str
        :param KeyboardClickCount: 用戶操作過程中鍵盤點擊次數。
        :type KeyboardClickCount: str
        :param MacAddress: MAC 網址或設備唯一標識。
        :type MacAddress: str
        :param VendorId: 手機制造商 ID，如果手機注冊，請帶上此訊息。
        :type VendorId: str
        :param Imei: 手機設備號。支援以下格式：
1.imei明文
2.idfa明文,
3.imei小寫後MD5值小寫
4.idfa大寫後MD5值小寫
        :type Imei: str
        :param AppVersion: App 用戶端版本。
        :type AppVersion: str
        :param BusinessId: 業務 ID 網站或應用在多個業務中使用此服務，通過此 ID 區分統計數據。
        :type BusinessId: str
        :param WxSubType: 1： 公衆號。
2： 小程式。
        :type WxSubType: str
        :param RandNum: Token 簽名随機數，WxSubType爲 小程式時必填，建議16個字元。
        :type RandNum: str
        :param WxToken: 如果 accountType爲2而且wxSubType有填，該欄位必選，否則不需要填寫；
如果是 小程式（WxSubType=2），該欄位爲以ssesion_key爲key去簽名随機數radnNum得到的值（ hmac_sha256簽名算法）；如果是 公衆號或第三方登入，則爲授權的access_token（網頁版本的access_Token,而且獲取token的scope欄位必需填寫snsapi_userinfo；）
        :type WxToken: str
        :param CheckDevice: 是否識别設備異常：
0：不識别。
1：識别。
        :type CheckDevice: str
        """
        self.AccountType = None
        self.Uid = None
        self.UserIp = None
        self.PostTime = None
        self.AppIdU = None
        self.NickName = None
        self.PhoneNumber = None
        self.EmailAddress = None
        self.RegisterTime = None
        self.RegisterIp = None
        self.CookieHash = None
        self.Address = None
        self.LoginSource = None
        self.LoginType = None
        self.LoginSpend = None
        self.RootId = None
        self.Referer = None
        self.JumpUrl = None
        self.UserAgent = None
        self.XForwardedFor = None
        self.MouseClickCount = None
        self.KeyboardClickCount = None
        self.MacAddress = None
        self.VendorId = None
        self.Imei = None
        self.AppVersion = None
        self.BusinessId = None
        self.WxSubType = None
        self.RandNum = None
        self.WxToken = None
        self.CheckDevice = None


    def _deserialize(self, params):
        self.AccountType = params.get("AccountType")
        self.Uid = params.get("Uid")
        self.UserIp = params.get("UserIp")
        self.PostTime = params.get("PostTime")
        self.AppIdU = params.get("AppIdU")
        self.NickName = params.get("NickName")
        self.PhoneNumber = params.get("PhoneNumber")
        self.EmailAddress = params.get("EmailAddress")
        self.RegisterTime = params.get("RegisterTime")
        self.RegisterIp = params.get("RegisterIp")
        self.CookieHash = params.get("CookieHash")
        self.Address = params.get("Address")
        self.LoginSource = params.get("LoginSource")
        self.LoginType = params.get("LoginType")
        self.LoginSpend = params.get("LoginSpend")
        self.RootId = params.get("RootId")
        self.Referer = params.get("Referer")
        self.JumpUrl = params.get("JumpUrl")
        self.UserAgent = params.get("UserAgent")
        self.XForwardedFor = params.get("XForwardedFor")
        self.MouseClickCount = params.get("MouseClickCount")
        self.KeyboardClickCount = params.get("KeyboardClickCount")
        self.MacAddress = params.get("MacAddress")
        self.VendorId = params.get("VendorId")
        self.Imei = params.get("Imei")
        self.AppVersion = params.get("AppVersion")
        self.BusinessId = params.get("BusinessId")
        self.WxSubType = params.get("WxSubType")
        self.RandNum = params.get("RandNum")
        self.WxToken = params.get("WxToken")
        self.CheckDevice = params.get("CheckDevice")


class QueryActivityAntiRushResponse(AbstractModel):
    """QueryActivityAntiRush返回參數結構體

    """

    def __init__(self):
        """
        :param PostTime: 操作時間戳，單位：秒。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PostTime: str
        :param UserIp: 用戶操作的真實外網 IP。
注意：此欄位可能返回 null，表示取不到有效值。
        :type UserIp: str
        :param Level: 0：表示無惡意。
1 - 4：惡意等級由低到高。
        :type Level: int
        :param RiskType: 風險類型。

賬號風險：

1，賬號信用低，賬號近期存在因惡意被處罰曆史，網絡低活躍，被舉報等因素；
2，垃圾賬號，疑似批次注冊小號，近期存在嚴重違規或大量舉報；
3，無效賬號，送檢賬號參數無法成功解析，請檢查 openid是否有誤 ， openid是否與appidU對應，手機號是否有誤。
4，黑名單，該賬號在業務側有過拉黑記錄
5，白名單，該賬號在業務側有過加白名單記錄

行爲風險：
101，批次操作，存在ip/設備/環境等因素的聚集性異常；
102，自動機，疑似自動機批次請求；
104， 登入态無效，檢查wxToken參數，是否已經失效；

環境風險：
201，環境異常，操作ip/設備/環境存在異常。當前ip爲非常用ip或惡意ip段；
205，非公網有效ip，傳進來的IP網址爲内網ip網址或者ip保留網址；
206，設備異常，該設備存在異常的使用行爲
        :type RiskType: list of int
        :param AssociateAccount: accountType是 或 開放賬號時，用於標識 或 用戶登入後關聯業務自身的賬號ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type AssociateAccount: str
        :param Uid: 用戶ID 
accountType不同對應不同的用戶ID。如果是 或 用戶則填入對應的openId
注意：此欄位可能返回 null，表示取不到有效值。
        :type Uid: str
        :param RootId: 用戶操作的目的ID 
比如：點贊，該欄位就是被點 贊的訊息 id，如果是投票，就是被投號碼的 ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type RootId: str
        :param CodeDesc: 業務側錯誤碼。成功時返回Success，錯誤時返回具體業務錯誤原因。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CodeDesc: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PostTime = None
        self.UserIp = None
        self.Level = None
        self.RiskType = None
        self.AssociateAccount = None
        self.Uid = None
        self.RootId = None
        self.CodeDesc = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PostTime = params.get("PostTime")
        self.UserIp = params.get("UserIp")
        self.Level = params.get("Level")
        self.RiskType = params.get("RiskType")
        self.AssociateAccount = params.get("AssociateAccount")
        self.Uid = params.get("Uid")
        self.RootId = params.get("RootId")
        self.CodeDesc = params.get("CodeDesc")
        self.RequestId = params.get("RequestId")