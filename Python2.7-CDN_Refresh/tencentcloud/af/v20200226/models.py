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


class QueryAntiFraudRequest(AbstractModel):
    """QueryAntiFraud請求參數結構體

    """

    def __init__(self):
        """
        :param PhoneNumber: 電話号碼(五選二)
        :type PhoneNumber: str
        :param IdNumber: Id(五選二)
        :type IdNumber: str
        :param BankCardNumber: 銀行卡号(五選二)
        :type BankCardNumber: str
        :param UserIp: 用戶請求來源 IP(五選二)
        :type UserIp: str
        :param Imei: 國際 設備識别碼(五選二)
        :type Imei: str
        :param Idfa: ios 系統廣告标示符(五選二)
        :type Idfa: str
        :param Scene: 業務場景 ID，需要找技術對接
        :type Scene: str
        :param Name: 姓名
        :type Name: str
        :param EmailAddress: 用戶電子信箱網址
        :type EmailAddress: str
        :param Address: 用戶住址
        :type Address: str
        :param Mac: MAC 網址
        :type Mac: str
        :param Imsi: 國際 用戶識别碼
        :type Imsi: str
        :param AccountType: 關聯的 帳号  ：1；
開放帳号 ： 2；
        :type AccountType: str
        :param Uid: 可選的   或  openid
        :type Uid: str
        :param AppIdU: qq 或 分配給網站或應用的 appid，用來
唯一标識網站或應用
        :type AppIdU: str
        :param WifiMac: WIFI MAC
        :type WifiMac: str
        :param WifiSSID: WIFI 服務集标識
        :type WifiSSID: str
        :param WifiBSSID: WIFI-BSSID
        :type WifiBSSID: str
        :param BusinessId: 業務 ID，在多個業務中使用此服務，通過此
ID 區分統計數據
        :type BusinessId: str
        :param IdCryptoType: Id加密類型
0：不加密（預設值）
1：md5
2：sha256
3：SM3
        :type IdCryptoType: str
        :param PhoneCryptoType: 手機号加密類型
0：不加密（預設值）
1：md5, 2：sha256
3：SM3
        :type PhoneCryptoType: str
        :param NameCryptoType: 姓名加密類型
0：不加密（預設值）
1：md5
2：sha256
3：SM3
        :type NameCryptoType: str
        """
        self.PhoneNumber = None
        self.IdNumber = None
        self.BankCardNumber = None
        self.UserIp = None
        self.Imei = None
        self.Idfa = None
        self.Scene = None
        self.Name = None
        self.EmailAddress = None
        self.Address = None
        self.Mac = None
        self.Imsi = None
        self.AccountType = None
        self.Uid = None
        self.AppIdU = None
        self.WifiMac = None
        self.WifiSSID = None
        self.WifiBSSID = None
        self.BusinessId = None
        self.IdCryptoType = None
        self.PhoneCryptoType = None
        self.NameCryptoType = None


    def _deserialize(self, params):
        self.PhoneNumber = params.get("PhoneNumber")
        self.IdNumber = params.get("IdNumber")
        self.BankCardNumber = params.get("BankCardNumber")
        self.UserIp = params.get("UserIp")
        self.Imei = params.get("Imei")
        self.Idfa = params.get("Idfa")
        self.Scene = params.get("Scene")
        self.Name = params.get("Name")
        self.EmailAddress = params.get("EmailAddress")
        self.Address = params.get("Address")
        self.Mac = params.get("Mac")
        self.Imsi = params.get("Imsi")
        self.AccountType = params.get("AccountType")
        self.Uid = params.get("Uid")
        self.AppIdU = params.get("AppIdU")
        self.WifiMac = params.get("WifiMac")
        self.WifiSSID = params.get("WifiSSID")
        self.WifiBSSID = params.get("WifiBSSID")
        self.BusinessId = params.get("BusinessId")
        self.IdCryptoType = params.get("IdCryptoType")
        self.PhoneCryptoType = params.get("PhoneCryptoType")
        self.NameCryptoType = params.get("NameCryptoType")


class QueryAntiFraudResponse(AbstractModel):
    """QueryAntiFraud返回參數結構體

    """

    def __init__(self):
        """
        :param Found: 表示該條記錄能否查到：1爲能查到，-1爲查不到
        :type Found: int
        :param IdFound: 表示該條Id能否查到：1爲能查到，-1爲查不到
        :type IdFound: int
        :param RiskScore: 0~100;值越高 欺詐可能性越大
        :type RiskScore: int
        :param RiskInfo: 擴展欄位，對風險類型的說明
        :type RiskInfo: list of RiskDetail
        :param CodeDesc: 業務側錯誤碼。成功時返回Success，錯誤時返回具體業務錯誤原因。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CodeDesc: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Found = None
        self.IdFound = None
        self.RiskScore = None
        self.RiskInfo = None
        self.CodeDesc = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Found = params.get("Found")
        self.IdFound = params.get("IdFound")
        self.RiskScore = params.get("RiskScore")
        if params.get("RiskInfo") is not None:
            self.RiskInfo = []
            for item in params.get("RiskInfo"):
                obj = RiskDetail()
                obj._deserialize(item)
                self.RiskInfo.append(obj)
        self.CodeDesc = params.get("CodeDesc")
        self.RequestId = params.get("RequestId")


class RiskDetail(AbstractModel):
    """擴展欄位，對風險類型的說明

    """

    def __init__(self):
        """
        :param RiskCode: 風險碼
        :type RiskCode: int
        """
        self.RiskCode = None


    def _deserialize(self, params):
        self.RiskCode = params.get("RiskCode")