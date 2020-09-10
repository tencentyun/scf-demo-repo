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


class QueryRegisterProtectionRequest(AbstractModel):
    """QueryRegisterProtection請求參數結構體

    """

    def __init__(self):
        """
        :param RegisterIp: 注冊來源的外網 IP。
        :type RegisterIp: str
        :param Uid: 用戶 ID 不同的 accountType 對應不同的用戶 ID。如果是  ，則填入對應的 openid， 用戶則填入對應的 openid/unionid，手機号則填入對應真實用戶手機号（如13123456789）。
        :type Uid: str
        :param RegisterTime: 注冊時間戳，單位：秒。
        :type RegisterTime: str
        :param AccountType: 用戶賬号類型（  開放帳号、 開放賬号需要 提交工單 由Top Cloud 進行資格審核）：
1：  開放帳号。
2： 開放賬号。
4：手機号。
0：其他。
10004：手機号 MD5。
        :type AccountType: str
        :param AppIdU: accountType 是   或 開放賬号時，該參數必填，表示   或 分配給網站或應用的 AppID，用來唯一标識網站或應用。
        :type AppIdU: str
        :param AssociateAccount: accountType 是   或 開放賬号時，用于标識   或 用戶登入後關聯業務自身的賬号 ID。
        :type AssociateAccount: str
        :param NickName: 昵稱，UTF-8 編碼。
        :type NickName: str
        :param PhoneNumber: 手機号：國家代碼-手機号， 如0086-15912345687（0086前不需要+号）。
        :type PhoneNumber: str
        :param EmailAddress: 用戶電子信箱網址（非系統自動生成）。
        :type EmailAddress: str
        :param Address: 網址。
        :type Address: str
        :param CookieHash: 用戶 HTTP 請求中的 cookie 進行2次 hash 的值，只要保證相同 cookie 的 hash 值一緻即可。
        :type CookieHash: str
        :param RegisterSource: 注冊來源：
0：其他。
1：PC 網頁。
2： 頁面。
3：App。
4： 公衆号。
        :type RegisterSource: str
        :param Referer: 用戶 HTTP 請求的 referer 值。
        :type Referer: str
        :param JumpUrl: 注冊成功後跳轉頁面。
        :type JumpUrl: str
        :param UserAgent: 用戶 HTTP 請求的 userAgent。
        :type UserAgent: str
        :param XForwardedFor: 用戶 HTTP 請求中的 x_forward_for。
        :type XForwardedFor: str
        :param MouseClickCount: 用戶操作過程中鼠标點擊次數。
        :type MouseClickCount: str
        :param KeyboardClickCount: 用戶操作過程中鍵盤點擊次數。
        :type KeyboardClickCount: str
        :param Result: 注冊結果：
0：失敗。
1：成功。
        :type Result: str
        :param Reason: 失敗原因：
0：其他。
1：參數錯誤。
2：帳号沖突。
3：驗證錯誤。
        :type Reason: str
        :param RegisterSpend: 登入耗時，單位：秒。
        :type RegisterSpend: str
        :param MacAddress: MAC 網址或設備唯一标識。
        :type MacAddress: str
        :param VendorId: 手機制造商 ID，如果手機注冊，請帶上此訊息。
        :type VendorId: str
        :param AppVersion: App 用戶端版本。
        :type AppVersion: str
        :param Imei: 手機設備号。
        :type Imei: str
        :param BusinessId: 業務 ID 網站或應用在多個業務中使用此服務，通過此 ID 區分統計數據。
        :type BusinessId: str
        :param WxSubType: 1： 公衆号。
2： 小程式。
        :type WxSubType: str
        :param RandNum: Token 簽名随機數， 小程式必填，建議16個字元。
        :type RandNum: str
        :param WxToken: 如果是 小程式，該欄位爲以 ssesion_key 爲 key 去簽名随機數 radnNum 得到的值（hmac_sha256簽名算法）。
如果是 公衆号或第三方登入，則爲授權的 access_token（注意：不是普通 access_token，具體看  官方文件）。
        :type WxToken: str
        """
        self.RegisterIp = None
        self.Uid = None
        self.RegisterTime = None
        self.AccountType = None
        self.AppIdU = None
        self.AssociateAccount = None
        self.NickName = None
        self.PhoneNumber = None
        self.EmailAddress = None
        self.Address = None
        self.CookieHash = None
        self.RegisterSource = None
        self.Referer = None
        self.JumpUrl = None
        self.UserAgent = None
        self.XForwardedFor = None
        self.MouseClickCount = None
        self.KeyboardClickCount = None
        self.Result = None
        self.Reason = None
        self.RegisterSpend = None
        self.MacAddress = None
        self.VendorId = None
        self.AppVersion = None
        self.Imei = None
        self.BusinessId = None
        self.WxSubType = None
        self.RandNum = None
        self.WxToken = None


    def _deserialize(self, params):
        self.RegisterIp = params.get("RegisterIp")
        self.Uid = params.get("Uid")
        self.RegisterTime = params.get("RegisterTime")
        self.AccountType = params.get("AccountType")
        self.AppIdU = params.get("AppIdU")
        self.AssociateAccount = params.get("AssociateAccount")
        self.NickName = params.get("NickName")
        self.PhoneNumber = params.get("PhoneNumber")
        self.EmailAddress = params.get("EmailAddress")
        self.Address = params.get("Address")
        self.CookieHash = params.get("CookieHash")
        self.RegisterSource = params.get("RegisterSource")
        self.Referer = params.get("Referer")
        self.JumpUrl = params.get("JumpUrl")
        self.UserAgent = params.get("UserAgent")
        self.XForwardedFor = params.get("XForwardedFor")
        self.MouseClickCount = params.get("MouseClickCount")
        self.KeyboardClickCount = params.get("KeyboardClickCount")
        self.Result = params.get("Result")
        self.Reason = params.get("Reason")
        self.RegisterSpend = params.get("RegisterSpend")
        self.MacAddress = params.get("MacAddress")
        self.VendorId = params.get("VendorId")
        self.AppVersion = params.get("AppVersion")
        self.Imei = params.get("Imei")
        self.BusinessId = params.get("BusinessId")
        self.WxSubType = params.get("WxSubType")
        self.RandNum = params.get("RandNum")
        self.WxToken = params.get("WxToken")


class QueryRegisterProtectionResponse(AbstractModel):
    """QueryRegisterProtection返回參數結構體

    """

    def __init__(self):
        """
        :param CodeDesc: 業務側錯誤碼，成功時返回 Success，錯誤時返回具體業務錯誤原因。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CodeDesc: str
        :param AssociateAccount: accountType 是   或 開放賬号時，用于标識   或 用戶登入後關聯業務自身的賬号 ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AssociateAccount: str
        :param RegisterTime: 注冊時間戳，單位：秒。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RegisterTime: str
        :param Uid: 用戶 ID 不同的 accountType 對應不同的用戶 ID。如果是  ，則填入對應的 openid， 用戶則填入對應的 openid/unionid，手機号則填入對應真實用戶手機号（如13123456789）。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Uid: str
        :param RegisterIp: 注冊來源的外網 IP。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RegisterIp: str
        :param Level: 0：表示無惡意。
1 - 4：惡意等級由低到高。
        :type Level: int
        :param RiskType: 風險類型。
        :type RiskType: list of int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CodeDesc = None
        self.AssociateAccount = None
        self.RegisterTime = None
        self.Uid = None
        self.RegisterIp = None
        self.Level = None
        self.RiskType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CodeDesc = params.get("CodeDesc")
        self.AssociateAccount = params.get("AssociateAccount")
        self.RegisterTime = params.get("RegisterTime")
        self.Uid = params.get("Uid")
        self.RegisterIp = params.get("RegisterIp")
        self.Level = params.get("Level")
        self.RiskType = params.get("RiskType")
        self.RequestId = params.get("RequestId")