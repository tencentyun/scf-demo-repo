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


class Account(AbstractModel):
    """帳号清單訊息數據。

    """

    def __init__(self):
        """
        :param Id: 唯一ID。
        :type Id: int
        :param Uuid: 雲鏡用戶端唯一Uuid
        :type Uuid: str
        :param MachineIp: 主機内網IP。
        :type MachineIp: str
        :param MachineName: 主機名稱。
        :type MachineName: str
        :param Username: 帳号名。
        :type Username: str
        :param Groups: 帳号所屬組。
        :type Groups: str
        :param Privilege: 帳号類型。
<li>ORDINARY：普通帳号</li>
<li>SUPPER：超級管理員帳号</li>
        :type Privilege: str
        :param AccountCreateTime: 帳号創建時間。
        :type AccountCreateTime: str
        :param LastLoginTime: 帳号最後登入時間。
        :type LastLoginTime: str
        """
        self.Id = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None
        self.Username = None
        self.Groups = None
        self.Privilege = None
        self.AccountCreateTime = None
        self.LastLoginTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.Username = params.get("Username")
        self.Groups = params.get("Groups")
        self.Privilege = params.get("Privilege")
        self.AccountCreateTime = params.get("AccountCreateTime")
        self.LastLoginTime = params.get("LastLoginTime")


class AccountStatistics(AbstractModel):
    """帳号統計數據。

    """

    def __init__(self):
        """
        :param Username: 用戶名。
        :type Username: str
        :param MachineNum: 主機數量。
        :type MachineNum: int
        """
        self.Username = None
        self.MachineNum = None


    def _deserialize(self, params):
        self.Username = params.get("Username")
        self.MachineNum = params.get("MachineNum")


class AgentVul(AbstractModel):
    """主機漏洞訊息

    """

    def __init__(self):
        """
        :param Id: 漏洞ID。
        :type Id: int
        :param MachineIp: 主機IP。
        :type MachineIp: str
        :param VulName: 漏洞名稱。
        :type VulName: str
        :param VulLevel: 漏洞危害等級。
<li>HIGH：高危</li>
<li>MIDDLE：中危</li>
<li>LOW：低危</li>
<li>NOTICE：提示</li>
        :type VulLevel: str
        :param LastScanTime: 最後掃描時間。
        :type LastScanTime: str
        :param Description: 漏洞描述。
        :type Description: str
        :param VulId: 漏洞種類ID。
        :type VulId: int
        :param VulStatus: 漏洞狀态。
<li>UN_OPERATED : 待處理</li>
<li>FIXED : 已修複</li>
        :type VulStatus: str
        """
        self.Id = None
        self.MachineIp = None
        self.VulName = None
        self.VulLevel = None
        self.LastScanTime = None
        self.Description = None
        self.VulId = None
        self.VulStatus = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MachineIp = params.get("MachineIp")
        self.VulName = params.get("VulName")
        self.VulLevel = params.get("VulLevel")
        self.LastScanTime = params.get("LastScanTime")
        self.Description = params.get("Description")
        self.VulId = params.get("VulId")
        self.VulStatus = params.get("VulStatus")


class BruteAttack(AbstractModel):
    """暴力破解清單

    """

    def __init__(self):
        """
        :param Id: 事件ID。
        :type Id: int
        :param MachineIp: 主機IP。
        :type MachineIp: str
        :param Status: 破解事件狀态
<li>BRUTEATTACK_FAIL_ACCOUNT： 暴力破解事件-失敗(存在帳号)  </li>
<li>BRUTEATTACK_FAIL_NOACCOUNT：暴力破解事件-失敗(帳号不存在)</li>
<li>BRUTEATTACK_SUCCESS：暴力破解事件-成功</li>
        :type Status: str
        :param UserName: 用戶名稱。
        :type UserName: str
        :param City: 城市ID。
        :type City: int
        :param Country: 國家ID。
        :type Country: int
        :param Province:  ID。
        :type Province: int
        :param SrcIp: 來源IP。
        :type SrcIp: str
        :param Count: 嘗試破解次數。
        :type Count: int
        :param CreateTime: 發生時間。
        :type CreateTime: str
        :param MachineName: 主機名稱。
        :type MachineName: str
        :param Uuid: 雲鏡用戶端唯一标識UUID。
        :type Uuid: str
        """
        self.Id = None
        self.MachineIp = None
        self.Status = None
        self.UserName = None
        self.City = None
        self.Country = None
        self.Province = None
        self.SrcIp = None
        self.Count = None
        self.CreateTime = None
        self.MachineName = None
        self.Uuid = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MachineIp = params.get("MachineIp")
        self.Status = params.get("Status")
        self.UserName = params.get("UserName")
        self.City = params.get("City")
        self.Country = params.get("Country")
        self.Province = params.get("Province")
        self.SrcIp = params.get("SrcIp")
        self.Count = params.get("Count")
        self.CreateTime = params.get("CreateTime")
        self.MachineName = params.get("MachineName")
        self.Uuid = params.get("Uuid")


class ChargePrepaid(AbstractModel):
    """預付費模式，即包年包月相關參數設置。通過該參數可以指定包年包月實例的購買時長、是否設置自動續約等屬性。

    """

    def __init__(self):
        """
        :param Period: 購買實例的時長，單位：月。取值範圍：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36。
        :type Period: int
        :param RenewFlag: 自動續約标識。取值範圍：
<li>NOTIFY_AND_AUTO_RENEW：通知過期且自動續約</li>
<li>NOTIFY_AND_MANUAL_RENEW：通知過期不自動續約</li>
<li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知過期不自動續約</li>

預設取值：NOTIFY_AND_MANUAL_RENEW。若該參數指定爲NOTIFY_AND_AUTO_RENEW，在帳戶餘額充足的情況下，實例到期後将按月自動續約。
        :type RenewFlag: str
        """
        self.Period = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RenewFlag = params.get("RenewFlag")


class CloseProVersionRequest(AbstractModel):
    """CloseProVersion請求參數結構體

    """

    def __init__(self):
        """
        :param Quuid: 主機唯一标識Uuid。
黑石的InstanceId，CVM的Uuid
        :type Quuid: str
        """
        self.Quuid = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")


class CloseProVersionResponse(AbstractModel):
    """CloseProVersion返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Component(AbstractModel):
    """元件清單數據。

    """

    def __init__(self):
        """
        :param Id: 唯一ID。
        :type Id: int
        :param Uuid: 雲鏡用戶端唯一Uuid。
        :type Uuid: str
        :param MachineIp: 主機内網IP。
        :type MachineIp: str
        :param MachineName: 主機名。
        :type MachineName: str
        :param ComponentVersion: 元件版本号。
        :type ComponentVersion: str
        :param ComponentType: 元件類型。
<li>SYSTEM：系統元件</li>
<li>WEB：WEB元件</li>
        :type ComponentType: str
        :param ComponentName: 元件名稱。
        :type ComponentName: str
        :param ModifyTime: 元件檢測更新時間。
        :type ModifyTime: str
        """
        self.Id = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None
        self.ComponentVersion = None
        self.ComponentType = None
        self.ComponentName = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.ComponentVersion = params.get("ComponentVersion")
        self.ComponentType = params.get("ComponentType")
        self.ComponentName = params.get("ComponentName")
        self.ModifyTime = params.get("ModifyTime")


class ComponentStatistics(AbstractModel):
    """元件統計數據。

    """

    def __init__(self):
        """
        :param Id: 元件ID。
        :type Id: int
        :param MachineNum: 主機數量。
        :type MachineNum: int
        :param ComponentName: 元件名稱。
        :type ComponentName: str
        :param ComponentType: 元件類型。
<li>WEB：web元件</li>
<li>SYSTEM：系統元件</li>
        :type ComponentType: str
        :param Description: 元件描述。
        :type Description: str
        """
        self.Id = None
        self.MachineNum = None
        self.ComponentName = None
        self.ComponentType = None
        self.Description = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MachineNum = params.get("MachineNum")
        self.ComponentName = params.get("ComponentName")
        self.ComponentType = params.get("ComponentType")
        self.Description = params.get("Description")


class CreateProcessTaskRequest(AbstractModel):
    """CreateProcessTask請求參數結構體

    """

    def __init__(self):
        """
        :param Uuid: 雲鏡用戶端唯一Uuid。
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")


class CreateProcessTaskResponse(AbstractModel):
    """CreateProcessTask返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateUsualLoginPlacesRequest(AbstractModel):
    """CreateUsualLoginPlaces請求參數結構體

    """

    def __init__(self):
        """
        :param Uuids: 雲鏡用戶端UUID數組。
        :type Uuids: list of str
        :param Places: 登入地域訊息數組。
        :type Places: list of Place
        """
        self.Uuids = None
        self.Places = None


    def _deserialize(self, params):
        self.Uuids = params.get("Uuids")
        if params.get("Places") is not None:
            self.Places = []
            for item in params.get("Places"):
                obj = Place()
                obj._deserialize(item)
                self.Places.append(obj)


class CreateUsualLoginPlacesResponse(AbstractModel):
    """CreateUsualLoginPlaces返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteBruteAttacksRequest(AbstractModel):
    """DeleteBruteAttacks請求參數結構體

    """

    def __init__(self):
        """
        :param Ids: 暴力破解事件Id數組。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteBruteAttacksResponse(AbstractModel):
    """DeleteBruteAttacks返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMachineRequest(AbstractModel):
    """DeleteMachine請求參數結構體

    """

    def __init__(self):
        """
        :param Uuid: 雲鏡用戶端Uuid。
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")


class DeleteMachineResponse(AbstractModel):
    """DeleteMachine返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMaliciousRequestsRequest(AbstractModel):
    """DeleteMaliciousRequests請求參數結構體

    """

    def __init__(self):
        """
        :param Ids: 惡意請求記錄ID數組，最大100條。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteMaliciousRequestsResponse(AbstractModel):
    """DeleteMaliciousRequests返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMalwaresRequest(AbstractModel):
    """DeleteMalwares請求參數結構體

    """

    def __init__(self):
        """
        :param Ids: 木馬記錄ID數組
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteMalwaresResponse(AbstractModel):
    """DeleteMalwares返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNonlocalLoginPlacesRequest(AbstractModel):
    """DeleteNonlocalLoginPlaces請求參數結構體

    """

    def __init__(self):
        """
        :param Ids: 異地登入事件Id數組。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteNonlocalLoginPlacesResponse(AbstractModel):
    """DeleteNonlocalLoginPlaces返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteUsualLoginPlacesRequest(AbstractModel):
    """DeleteUsualLoginPlaces請求參數結構體

    """

    def __init__(self):
        """
        :param Uuid: 雲鏡用戶端Uuid
        :type Uuid: str
        :param CityIds: 已添加常用登入地城市ID數組
        :type CityIds: list of int non-negative
        """
        self.Uuid = None
        self.CityIds = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.CityIds = params.get("CityIds")


class DeleteUsualLoginPlacesResponse(AbstractModel):
    """DeleteUsualLoginPlaces返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccountStatisticsRequest(AbstractModel):
    """DescribeAccountStatistics請求參數結構體

    """

    def __init__(self):
        """
        :param Limit: 返回數量，預設爲10，最大值爲100。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Filters: 過濾條件。
<li>Username - String - 是否必填：否 - 帳号用戶名</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeAccountStatisticsResponse(AbstractModel):
    """DescribeAccountStatistics返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 帳号統計清單記錄總數。
        :type TotalCount: int
        :param AccountStatistics: 帳号統計清單。
        :type AccountStatistics: list of AccountStatistics
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AccountStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AccountStatistics") is not None:
            self.AccountStatistics = []
            for item in params.get("AccountStatistics"):
                obj = AccountStatistics()
                obj._deserialize(item)
                self.AccountStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts請求參數結構體

    """

    def __init__(self):
        """
        :param Uuid: 雲鏡用戶端唯一Uuid。Username和Uuid必填其一，使用Uuid表示，查詢該主機下清單訊息。
        :type Uuid: str
        :param Username: 雲鏡用戶端唯一Uuid。Username和Uuid必填其一，使用Username表示，查詢該用戶名下清單訊息。
        :type Username: str
        :param Limit: 返回數量，預設爲10，最大值爲100。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Filters: 過濾條件。
<li>Username - String - 是否必填：否 - 帳号名</li>
<li>Privilege - String - 是否必填：否 - 帳号類型（ORDINARY: 普通帳号 | SUPPER: 超級管理員帳号）</li>
<li>MachineIp - String - 是否必填：否 - 主機内網IP</li>
        :type Filters: list of Filter
        """
        self.Uuid = None
        self.Username = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Username = params.get("Username")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 帳号清單記錄總數。
        :type TotalCount: int
        :param Accounts: 帳号數據清單。
        :type Accounts: list of Account
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Accounts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAgentVulsRequest(AbstractModel):
    """DescribeAgentVuls請求參數結構體

    """

    def __init__(self):
        """
        :param VulType: 漏洞類型。
<li>WEB: Web應用漏洞</li>
<li>SYSTEM：系統元件漏洞</li>
<li>BASELINE：安全基線</li>
        :type VulType: str
        :param Uuid: 用戶端UUID。
        :type Uuid: str
        :param Limit: 返回數量，預設爲10，最大值爲100。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Filters: 過濾條件。
<li>Status - String - 是否必填：否 - 狀态篩選（UN_OPERATED: 待處理 | FIXED：已修複）
        :type Filters: list of Filter
        """
        self.VulType = None
        self.Uuid = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.VulType = params.get("VulType")
        self.Uuid = params.get("Uuid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeAgentVulsResponse(AbstractModel):
    """DescribeAgentVuls返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 記錄總數
        :type TotalCount: int
        :param AgentVuls: 主機漏洞訊息
        :type AgentVuls: list of AgentVul
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AgentVuls = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AgentVuls") is not None:
            self.AgentVuls = []
            for item in params.get("AgentVuls"):
                obj = AgentVul()
                obj._deserialize(item)
                self.AgentVuls.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAlarmAttributeRequest(AbstractModel):
    """DescribeAlarmAttribute請求參數結構體

    """


class DescribeAlarmAttributeResponse(AbstractModel):
    """DescribeAlarmAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param Offline: 防護軟體離線告警狀态：
<li>OPEN：告警已開啓</li>
<li>CLOSE： 告警已關閉</li>
        :type Offline: str
        :param Malware: 發現木馬告警狀态：
<li>OPEN：告警已開啓</li>
<li>CLOSE： 告警已關閉</li>
        :type Malware: str
        :param NonlocalLogin: 發現異地登入告警狀态：
<li>OPEN：告警已開啓</li>
<li>CLOSE： 告警已關閉</li>
        :type NonlocalLogin: str
        :param CrackSuccess: 被暴力破解成功告警狀态：
<li>OPEN：告警已開啓</li>
<li>CLOSE： 告警已關閉</li>
        :type CrackSuccess: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Offline = None
        self.Malware = None
        self.NonlocalLogin = None
        self.CrackSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Offline = params.get("Offline")
        self.Malware = params.get("Malware")
        self.NonlocalLogin = params.get("NonlocalLogin")
        self.CrackSuccess = params.get("CrackSuccess")
        self.RequestId = params.get("RequestId")


class DescribeBruteAttacksRequest(AbstractModel):
    """DescribeBruteAttacks請求參數結構體

    """

    def __init__(self):
        """
        :param Uuid: 用戶端唯一Uuid。
        :type Uuid: str
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Filters: 過濾條件。
<li>Keywords - String - 是否必填：否 -  查詢關鍵字</li>
<li>Status - String - 是否必填：否 -  查詢狀态（FAILED：破解失敗 |SUCCESS：破解成功）</li>
        :type Filters: list of Filter
        :param Limit: 返回數量，預設爲10，最大值爲100。
        :type Limit: int
        """
        self.Uuid = None
        self.Offset = None
        self.Filters = None
        self.Limit = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")


class DescribeBruteAttacksResponse(AbstractModel):
    """DescribeBruteAttacks返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 事件數量
        :type TotalCount: int
        :param BruteAttacks: 暴力破解事件清單
        :type BruteAttacks: list of BruteAttack
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.BruteAttacks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BruteAttacks") is not None:
            self.BruteAttacks = []
            for item in params.get("BruteAttacks"):
                obj = BruteAttack()
                obj._deserialize(item)
                self.BruteAttacks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeComponentInfoRequest(AbstractModel):
    """DescribeComponentInfo請求參數結構體

    """

    def __init__(self):
        """
        :param ComponentId: 元件ID。
        :type ComponentId: int
        """
        self.ComponentId = None


    def _deserialize(self, params):
        self.ComponentId = params.get("ComponentId")


class DescribeComponentInfoResponse(AbstractModel):
    """DescribeComponentInfo返回參數結構體

    """

    def __init__(self):
        """
        :param Id: 元件ID。
        :type Id: int
        :param ComponentName: 元件名稱。
        :type ComponentName: str
        :param ComponentType: 元件類型。
<li>WEB：web元件</li>
<li>SYSTEM：系統元件</li>
        :type ComponentType: str
        :param Homepage: 元件官網。
        :type Homepage: str
        :param Description: 元件描述。
        :type Description: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.ComponentName = None
        self.ComponentType = None
        self.Homepage = None
        self.Description = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.ComponentName = params.get("ComponentName")
        self.ComponentType = params.get("ComponentType")
        self.Homepage = params.get("Homepage")
        self.Description = params.get("Description")
        self.RequestId = params.get("RequestId")


class DescribeComponentStatisticsRequest(AbstractModel):
    """DescribeComponentStatistics請求參數結構體

    """

    def __init__(self):
        """
        :param Limit: 返回數量，預設爲10，最大值爲100。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Filters: 過濾條件。
ComponentName - String - 是否必填：否 - 元件名稱
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeComponentStatisticsResponse(AbstractModel):
    """DescribeComponentStatistics返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 元件統計清單記錄總數。
        :type TotalCount: int
        :param ComponentStatistics: 元件統計清單數據數組。
        :type ComponentStatistics: list of ComponentStatistics
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ComponentStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ComponentStatistics") is not None:
            self.ComponentStatistics = []
            for item in params.get("ComponentStatistics"):
                obj = ComponentStatistics()
                obj._deserialize(item)
                self.ComponentStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeComponentsRequest(AbstractModel):
    """DescribeComponents請求參數結構體

    """

    def __init__(self):
        """
        :param Uuid: 雲鏡用戶端唯一Uuid。Uuid和ComponentId必填其一，使用Uuid表示，查詢該主機清單訊息。
        :type Uuid: str
        :param ComponentId: 元件ID。Uuid和ComponentId必填其一，使用ComponentId表示，查詢該元件清單訊息。
        :type ComponentId: int
        :param Limit: 返回數量，預設爲10，最大值爲100。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Filters: 過濾條件。
<li>ComponentVersion - String - 是否必填：否 - 元件版本号</li>
<li>MachineIp - String - 是否必填：否 - 主機内網IP</li>
        :type Filters: list of Filter
        """
        self.Uuid = None
        self.ComponentId = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.ComponentId = params.get("ComponentId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeComponentsResponse(AbstractModel):
    """DescribeComponents返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 元件清單記錄總數。
        :type TotalCount: int
        :param Components: 元件清單數據。
        :type Components: list of Component
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Components = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Components") is not None:
            self.Components = []
            for item in params.get("Components"):
                obj = Component()
                obj._deserialize(item)
                self.Components.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHistoryAccountsRequest(AbstractModel):
    """DescribeHistoryAccounts請求參數結構體

    """

    def __init__(self):
        """
        :param Uuid: 雲鏡用戶端唯一Uuid。
        :type Uuid: str
        :param Limit: 返回數量，預設爲10，最大值爲100。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Filters: 過濾條件。
<li>Username - String - 是否必填：否 - 帳号名</li>
        :type Filters: list of Filter
        """
        self.Uuid = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeHistoryAccountsResponse(AbstractModel):
    """DescribeHistoryAccounts返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 帳号變更曆史清單記錄總數。
        :type TotalCount: int
        :param HistoryAccounts: 帳号變更曆史數據數組。
        :type HistoryAccounts: list of HistoryAccount
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.HistoryAccounts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("HistoryAccounts") is not None:
            self.HistoryAccounts = []
            for item in params.get("HistoryAccounts"):
                obj = HistoryAccount()
                obj._deserialize(item)
                self.HistoryAccounts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImpactedHostsRequest(AbstractModel):
    """DescribeImpactedHosts請求參數結構體

    """

    def __init__(self):
        """
        :param VulId: 漏洞種類ID。
        :type VulId: int
        :param Limit: 返回數量，預設爲10，最大值爲100。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Filters: 過濾條件。
<li>Status - String - 是否必填：否 - 狀态篩選（UN_OPERATED：待處理 | FIXED：已修複）</li>
        :type Filters: list of Filter
        """
        self.VulId = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.VulId = params.get("VulId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeImpactedHostsResponse(AbstractModel):
    """DescribeImpactedHosts返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 記錄總數
        :type TotalCount: int
        :param ImpactedHosts: 漏洞影響機器清單數組
        :type ImpactedHosts: list of ImpactedHost
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ImpactedHosts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ImpactedHosts") is not None:
            self.ImpactedHosts = []
            for item in params.get("ImpactedHosts"):
                obj = ImpactedHost()
                obj._deserialize(item)
                self.ImpactedHosts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMachineInfoRequest(AbstractModel):
    """DescribeMachineInfo請求參數結構體

    """

    def __init__(self):
        """
        :param Uuid: 雲鏡用戶端唯一Uuid。
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")


class DescribeMachineInfoResponse(AbstractModel):
    """DescribeMachineInfo返回參數結構體

    """

    def __init__(self):
        """
        :param MachineIp: 機器ip。
        :type MachineIp: str
        :param ProtectDays: 受雲鏡保護天數。
        :type ProtectDays: int
        :param MachineOs: 作業系統。
        :type MachineOs: str
        :param MachineName: 主機名稱。
        :type MachineName: str
        :param MachineStatus: 在線狀态。
<li>ONLINE： 在線</li>
<li>OFFLINE：離線</li>
        :type MachineStatus: str
        :param InstanceId: CVM或BM主機唯一标識。
        :type InstanceId: str
        :param MachineWanIp: 主機外網IP。
        :type MachineWanIp: str
        :param Quuid: CVM或BM主機唯一Uuid。
        :type Quuid: str
        :param Uuid: 雲鏡用戶端唯一Uuid。
        :type Uuid: str
        :param IsProVersion: 是否開通專業版。
<li>true：是</li>
<li>false：否</li>
        :type IsProVersion: bool
        :param ProVersionOpenDate: 專業版開通時間。
        :type ProVersionOpenDate: str
        :param MachineType: 雲主機類型。
<li>CVM: 虛拟主機</li>
<li>BM: 黑石物理機</li>
        :type MachineType: str
        :param MachineRegion: 機器所屬地域。如：ap-guangzhou，ap-shanghai
        :type MachineRegion: str
        :param PayMode: 主機狀态。
<li>POSTPAY: 表示後付費，即按量計費  </li>
<li>PREPAY: 表示預付費，即包年包月</li>
        :type PayMode: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.MachineIp = None
        self.ProtectDays = None
        self.MachineOs = None
        self.MachineName = None
        self.MachineStatus = None
        self.InstanceId = None
        self.MachineWanIp = None
        self.Quuid = None
        self.Uuid = None
        self.IsProVersion = None
        self.ProVersionOpenDate = None
        self.MachineType = None
        self.MachineRegion = None
        self.PayMode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.ProtectDays = params.get("ProtectDays")
        self.MachineOs = params.get("MachineOs")
        self.MachineName = params.get("MachineName")
        self.MachineStatus = params.get("MachineStatus")
        self.InstanceId = params.get("InstanceId")
        self.MachineWanIp = params.get("MachineWanIp")
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.IsProVersion = params.get("IsProVersion")
        self.ProVersionOpenDate = params.get("ProVersionOpenDate")
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        self.PayMode = params.get("PayMode")
        self.RequestId = params.get("RequestId")


class DescribeMachinesRequest(AbstractModel):
    """DescribeMachines請求參數結構體

    """

    def __init__(self):
        """
        :param MachineType: 雲主機類型。
<li>CVM：表示虛拟主機</li>
<li>BM:  表示黑石物理機</li>
        :type MachineType: str
        :param MachineRegion: 機器所屬地域。如：ap-guangzhou，ap-shanghai
        :type MachineRegion: str
        :param Limit: 返回數量，預設爲10，最大值爲100。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Filters: 過濾條件。
<li>Keywords - String - 是否必填：否 - 查詢關鍵字 </li>
<li>Status - String - 是否必填：否 - 用戶端在線狀态（OFFLINE: 離線 | ONLINE: 在線）</li>
<li>Version - String  是否必填：否 - 當前防護版本（ PRO_VERSION：專業版 | BASIC_VERSION：基礎版）</li>
每個過濾條件只支援一個值，暫不支援多個值“或”關系查詢
        :type Filters: list of Filter
        """
        self.MachineType = None
        self.MachineRegion = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeMachinesResponse(AbstractModel):
    """DescribeMachines返回參數結構體

    """

    def __init__(self):
        """
        :param Machines: 主機清單
        :type Machines: list of Machine
        :param TotalCount: 主機數量
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Machines = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Machines") is not None:
            self.Machines = []
            for item in params.get("Machines"):
                obj = Machine()
                obj._deserialize(item)
                self.Machines.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeMaliciousRequestsRequest(AbstractModel):
    """DescribeMaliciousRequests請求參數結構體

    """

    def __init__(self):
        """
        :param Limit: 返回數量，預設爲10，最大值爲100。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Filters: 過濾條件。
<li>Status - String - 是否必填：否 - 狀态篩選（UN_OPERATED: 待處理 | TRUSTED：已信任 | UN_TRUSTED：已取消信任）</li>
<li>Domain - String - 是否必填：否 - 惡意請求的域名</li>
<li>MachineIp - String - 是否必填：否 - 主機内網IP</li>
        :type Filters: list of Filter
        :param Uuid: 雲鏡用戶端唯一UUID。
        :type Uuid: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Uuid = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Uuid = params.get("Uuid")


class DescribeMaliciousRequestsResponse(AbstractModel):
    """DescribeMaliciousRequests返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 記錄總數。
        :type TotalCount: int
        :param MaliciousRequests: 惡意請求記錄數組。
        :type MaliciousRequests: list of MaliciousRequest
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.MaliciousRequests = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("MaliciousRequests") is not None:
            self.MaliciousRequests = []
            for item in params.get("MaliciousRequests"):
                obj = MaliciousRequest()
                obj._deserialize(item)
                self.MaliciousRequests.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMalwaresRequest(AbstractModel):
    """DescribeMalwares請求參數結構體

    """

    def __init__(self):
        """
        :param Uuid: 用戶端唯一Uuid。
        :type Uuid: str
        :param Limit: 返回數量，預設爲10，最大值爲100。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Filters: 過濾條件。
<li>Keywords - String - 是否必填：否 - 查詢關鍵字 </li>
<li>Status - String - 是否必填：否 - 木馬狀态（UN_OPERATED: 未處理 | SEGREGATED: 已隔離|TRUSTED：信任）</li>
每個過濾條件只支援一個值，暫不支援多個值“或”關系查詢。
        :type Filters: list of Filter
        """
        self.Uuid = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeMalwaresResponse(AbstractModel):
    """DescribeMalwares返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 木馬總數。
        :type TotalCount: int
        :param Malwares: Malware數組。
        :type Malwares: list of Malware
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Malwares = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Malwares") is not None:
            self.Malwares = []
            for item in params.get("Malwares"):
                obj = Malware()
                obj._deserialize(item)
                self.Malwares.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNonlocalLoginPlacesRequest(AbstractModel):
    """DescribeNonlocalLoginPlaces請求參數結構體

    """

    def __init__(self):
        """
        :param Uuid: 用戶端唯一Uuid。
        :type Uuid: str
        :param Limit: 返回數量，預設爲10，最大值爲100。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Filters: 過濾條件。
<li>Keywords - String - 是否必填：否 -  查詢關鍵字</li>
<li>Status - String - 是否必填：否 -  登入狀态（NON_LOCAL_LOGIN: 異地登入 | NORMAL_LOGIN : 正常登入）</li>
        :type Filters: list of Filter
        """
        self.Uuid = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeNonlocalLoginPlacesResponse(AbstractModel):
    """DescribeNonlocalLoginPlaces返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 記錄總數。
        :type TotalCount: int
        :param NonLocalLoginPlaces: 異地登入訊息數組。
        :type NonLocalLoginPlaces: list of NonLocalLoginPlace
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.NonLocalLoginPlaces = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("NonLocalLoginPlaces") is not None:
            self.NonLocalLoginPlaces = []
            for item in params.get("NonLocalLoginPlaces"):
                obj = NonLocalLoginPlace()
                obj._deserialize(item)
                self.NonLocalLoginPlaces.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOpenPortStatisticsRequest(AbstractModel):
    """DescribeOpenPortStatistics請求參數結構體

    """

    def __init__(self):
        """
        :param Limit: 返回數量，預設爲10，最大值爲100。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Filters: 過濾條件。
<li>Port - Uint64 - 是否必填：否 - 端口号</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeOpenPortStatisticsResponse(AbstractModel):
    """DescribeOpenPortStatistics返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 端口統計清單總數
        :type TotalCount: int
        :param OpenPortStatistics: 端口統計數據清單
        :type OpenPortStatistics: list of OpenPortStatistics
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.OpenPortStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("OpenPortStatistics") is not None:
            self.OpenPortStatistics = []
            for item in params.get("OpenPortStatistics"):
                obj = OpenPortStatistics()
                obj._deserialize(item)
                self.OpenPortStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOpenPortsRequest(AbstractModel):
    """DescribeOpenPorts請求參數結構體

    """

    def __init__(self):
        """
        :param Uuid: 雲鏡用戶端唯一Uuid。Port和Uuid必填其一，使用Uuid表示，查詢該主機清單訊息。
        :type Uuid: str
        :param Port: 開放端口号。Port和Uuid必填其一，使用Port表示查詢該端口的清單訊息。
        :type Port: int
        :param Limit: 返回數量，預設爲10，最大值爲100。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Filters: 過濾條件。
<li>Port - Uint64 - 是否必填：否 - 端口号</li>
<li>ProcessName - String - 是否必填：否 - 程式名</li>
<li>MachineIp - String - 是否必填：否 - 主機内網IP</li>
        :type Filters: list of Filter
        """
        self.Uuid = None
        self.Port = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Port = params.get("Port")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeOpenPortsResponse(AbstractModel):
    """DescribeOpenPorts返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 端口清單記錄總數。
        :type TotalCount: int
        :param OpenPorts: 端口清單。
        :type OpenPorts: list of OpenPort
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.OpenPorts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("OpenPorts") is not None:
            self.OpenPorts = []
            for item in params.get("OpenPorts"):
                obj = OpenPort()
                obj._deserialize(item)
                self.OpenPorts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOverviewStatisticsRequest(AbstractModel):
    """DescribeOverviewStatistics請求參數結構體

    """


class DescribeOverviewStatisticsResponse(AbstractModel):
    """DescribeOverviewStatistics返回參數結構體

    """

    def __init__(self):
        """
        :param OnlineMachineNum: 服務器在線數。
        :type OnlineMachineNum: int
        :param ProVersionMachineNum: 專業服務器數。
        :type ProVersionMachineNum: int
        :param MalwareNum: 木馬文件數。
        :type MalwareNum: int
        :param NonlocalLoginNum: 異地登入數。
        :type NonlocalLoginNum: int
        :param BruteAttackSuccessNum: 暴力破解成功數。
        :type BruteAttackSuccessNum: int
        :param VulNum: 漏洞數。
        :type VulNum: int
        :param BaseLineNum: 安全基線數。
        :type BaseLineNum: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.OnlineMachineNum = None
        self.ProVersionMachineNum = None
        self.MalwareNum = None
        self.NonlocalLoginNum = None
        self.BruteAttackSuccessNum = None
        self.VulNum = None
        self.BaseLineNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OnlineMachineNum = params.get("OnlineMachineNum")
        self.ProVersionMachineNum = params.get("ProVersionMachineNum")
        self.MalwareNum = params.get("MalwareNum")
        self.NonlocalLoginNum = params.get("NonlocalLoginNum")
        self.BruteAttackSuccessNum = params.get("BruteAttackSuccessNum")
        self.VulNum = params.get("VulNum")
        self.BaseLineNum = params.get("BaseLineNum")
        self.RequestId = params.get("RequestId")


class DescribeProVersionInfoRequest(AbstractModel):
    """DescribeProVersionInfo請求參數結構體

    """


class DescribeProVersionInfoResponse(AbstractModel):
    """DescribeProVersionInfo返回參數結構體

    """

    def __init__(self):
        """
        :param PostPayCost: 後付費昨日扣費
        :type PostPayCost: int
        :param IsAutoOpenProVersion: 新增主機是否自動開通專業版
        :type IsAutoOpenProVersion: bool
        :param ProVersionNum: 開通專業版主機數
        :type ProVersionNum: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PostPayCost = None
        self.IsAutoOpenProVersion = None
        self.ProVersionNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PostPayCost = params.get("PostPayCost")
        self.IsAutoOpenProVersion = params.get("IsAutoOpenProVersion")
        self.ProVersionNum = params.get("ProVersionNum")
        self.RequestId = params.get("RequestId")


class DescribeProcessStatisticsRequest(AbstractModel):
    """DescribeProcessStatistics請求參數結構體

    """

    def __init__(self):
        """
        :param Limit: 返回數量，預設爲10，最大值爲100。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Filters: 過濾條件。
<li>ProcessName - String - 是否必填：否 - 程式名</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeProcessStatisticsResponse(AbstractModel):
    """DescribeProcessStatistics返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 程式統計清單記錄總數。
        :type TotalCount: int
        :param ProcessStatistics: 程式統計清單數據數組。
        :type ProcessStatistics: list of ProcessStatistics
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ProcessStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ProcessStatistics") is not None:
            self.ProcessStatistics = []
            for item in params.get("ProcessStatistics"):
                obj = ProcessStatistics()
                obj._deserialize(item)
                self.ProcessStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProcessTaskStatusRequest(AbstractModel):
    """DescribeProcessTaskStatus請求參數結構體

    """

    def __init__(self):
        """
        :param Uuid: 雲鏡用戶端唯一Uuid。
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")


class DescribeProcessTaskStatusResponse(AbstractModel):
    """DescribeProcessTaskStatus返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 任務狀态。
<li>COMPLETE：完成（此時可以調用DescribeProcesses介面獲取實時程式清單）</li>
<li>AGENT_OFFLINE：雲鏡用戶端離線</li>
<li>COLLECTING：程式獲取中</li>
<li>FAILED：程式獲取失敗</li>
        :type Status: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeProcessesRequest(AbstractModel):
    """DescribeProcesses請求參數結構體

    """

    def __init__(self):
        """
        :param Uuid: 雲鏡用戶端唯一Uuid。Uuid和ProcessName必填其一，使用Uuid表示，查詢該主機清單訊息。
        :type Uuid: str
        :param ProcessName: 程式名。Uuid和ProcessName必填其一，使用ProcessName表示，查詢該程式清單訊息。
        :type ProcessName: str
        :param Limit: 返回數量，預設爲10，最大值爲100。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Filters: 過濾條件。
<li>ProcessName - String - 是否必填：否 - 程式名</li>
<li>MachineIp - String - 是否必填：否 - 主機内網IP</li>
        :type Filters: list of Filter
        """
        self.Uuid = None
        self.ProcessName = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.ProcessName = params.get("ProcessName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeProcessesResponse(AbstractModel):
    """DescribeProcesses返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 程式清單記錄總數。
        :type TotalCount: int
        :param Processes: 程式清單數據數組。
        :type Processes: list of Process
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Processes = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Processes") is not None:
            self.Processes = []
            for item in params.get("Processes"):
                obj = Process()
                obj._deserialize(item)
                self.Processes.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecurityDynamicsRequest(AbstractModel):
    """DescribeSecurityDynamics請求參數結構體

    """

    def __init__(self):
        """
        :param Limit: 返回數量，預設爲10，最大值爲100。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeSecurityDynamicsResponse(AbstractModel):
    """DescribeSecurityDynamics返回參數結構體

    """

    def __init__(self):
        """
        :param SecurityDynamics: 安全事件訊息數組。
        :type SecurityDynamics: list of SecurityDynamic
        :param TotalCount: 記錄總數。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SecurityDynamics = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityDynamics") is not None:
            self.SecurityDynamics = []
            for item in params.get("SecurityDynamics"):
                obj = SecurityDynamic()
                obj._deserialize(item)
                self.SecurityDynamics.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSecurityTrendsRequest(AbstractModel):
    """DescribeSecurityTrends請求參數結構體

    """

    def __init__(self):
        """
        :param BeginDate: 開始時間。
        :type BeginDate: str
        :param EndDate: 結束時間。
        :type EndDate: str
        """
        self.BeginDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")


class DescribeSecurityTrendsResponse(AbstractModel):
    """DescribeSecurityTrends返回參數結構體

    """

    def __init__(self):
        """
        :param Malwares: 木馬事件統計數據數組。
        :type Malwares: list of SecurityTrend
        :param NonLocalLoginPlaces: 異地登入事件統計數據數組。
        :type NonLocalLoginPlaces: list of SecurityTrend
        :param BruteAttacks: 密碼破解事件統計數據數組。
        :type BruteAttacks: list of SecurityTrend
        :param Vuls: 漏洞統計數據數組。
        :type Vuls: list of SecurityTrend
        :param BaseLines: 基線統計數據數組。
        :type BaseLines: list of SecurityTrend
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Malwares = None
        self.NonLocalLoginPlaces = None
        self.BruteAttacks = None
        self.Vuls = None
        self.BaseLines = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Malwares") is not None:
            self.Malwares = []
            for item in params.get("Malwares"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.Malwares.append(obj)
        if params.get("NonLocalLoginPlaces") is not None:
            self.NonLocalLoginPlaces = []
            for item in params.get("NonLocalLoginPlaces"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.NonLocalLoginPlaces.append(obj)
        if params.get("BruteAttacks") is not None:
            self.BruteAttacks = []
            for item in params.get("BruteAttacks"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.BruteAttacks.append(obj)
        if params.get("Vuls") is not None:
            self.Vuls = []
            for item in params.get("Vuls"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.Vuls.append(obj)
        if params.get("BaseLines") is not None:
            self.BaseLines = []
            for item in params.get("BaseLines"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.BaseLines.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUsualLoginPlacesRequest(AbstractModel):
    """DescribeUsualLoginPlaces請求參數結構體

    """

    def __init__(self):
        """
        :param Uuid: 雲鏡用戶端UUID
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")


class DescribeUsualLoginPlacesResponse(AbstractModel):
    """DescribeUsualLoginPlaces返回參數結構體

    """

    def __init__(self):
        """
        :param UsualLoginPlaces: 常用登入地數組
        :type UsualLoginPlaces: list of UsualPlace
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.UsualLoginPlaces = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UsualLoginPlaces") is not None:
            self.UsualLoginPlaces = []
            for item in params.get("UsualLoginPlaces"):
                obj = UsualPlace()
                obj._deserialize(item)
                self.UsualLoginPlaces.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVulInfoRequest(AbstractModel):
    """DescribeVulInfo請求參數結構體

    """

    def __init__(self):
        """
        :param VulId: 漏洞種類ID。
        :type VulId: int
        """
        self.VulId = None


    def _deserialize(self, params):
        self.VulId = params.get("VulId")


class DescribeVulInfoResponse(AbstractModel):
    """DescribeVulInfo返回參數結構體

    """

    def __init__(self):
        """
        :param VulId: 漏洞種類ID。
        :type VulId: int
        :param VulName: 漏洞名稱。
        :type VulName: str
        :param VulLevel: 漏洞等級。
        :type VulLevel: str
        :param VulType: 漏洞類型。
        :type VulType: str
        :param Description: 漏洞描述。
        :type Description: str
        :param RepairPlan: 修複方案。
        :type RepairPlan: str
        :param CveId: 漏洞CVE。
        :type CveId: str
        :param Reference: 參考連結。
        :type Reference: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.VulId = None
        self.VulName = None
        self.VulLevel = None
        self.VulType = None
        self.Description = None
        self.RepairPlan = None
        self.CveId = None
        self.Reference = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VulId = params.get("VulId")
        self.VulName = params.get("VulName")
        self.VulLevel = params.get("VulLevel")
        self.VulType = params.get("VulType")
        self.Description = params.get("Description")
        self.RepairPlan = params.get("RepairPlan")
        self.CveId = params.get("CveId")
        self.Reference = params.get("Reference")
        self.RequestId = params.get("RequestId")


class DescribeVulScanResultRequest(AbstractModel):
    """DescribeVulScanResult請求參數結構體

    """


class DescribeVulScanResultResponse(AbstractModel):
    """DescribeVulScanResult返回參數結構體

    """

    def __init__(self):
        """
        :param VulNum: 漏洞數量。
        :type VulNum: int
        :param ProVersionNum: 專業版機器數。
        :type ProVersionNum: int
        :param ImpactedHostNum: 受影響的專業版主機數。
        :type ImpactedHostNum: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.VulNum = None
        self.ProVersionNum = None
        self.ImpactedHostNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VulNum = params.get("VulNum")
        self.ProVersionNum = params.get("ProVersionNum")
        self.ImpactedHostNum = params.get("ImpactedHostNum")
        self.RequestId = params.get("RequestId")


class DescribeVulsRequest(AbstractModel):
    """DescribeVuls請求參數結構體

    """

    def __init__(self):
        """
        :param VulType: 漏洞類型。
<li>WEB：Web應用漏洞</li>
<li>SYSTEM：系統元件漏洞</li>
<li>BASELINE：安全基線</li>
        :type VulType: str
        :param Limit: 返回數量，預設爲10，最大值爲100。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Filters: 過濾條件。
<li>Status - String - 是否必填：否 - 狀态篩選（UN_OPERATED: 待處理 | FIXED：已修複）

Status過濾條件值只能取其一，不能是“或”邏輯。
        :type Filters: list of Filter
        """
        self.VulType = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.VulType = params.get("VulType")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeVulsResponse(AbstractModel):
    """DescribeVuls返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 漏洞數量。
        :type TotalCount: int
        :param Vuls: 漏洞清單數組。
        :type Vuls: list of Vul
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Vuls = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Vuls") is not None:
            self.Vuls = []
            for item in params.get("Vuls"):
                obj = Vul()
                obj._deserialize(item)
                self.Vuls.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWeeklyReportBruteAttacksRequest(AbstractModel):
    """DescribeWeeklyReportBruteAttacks請求參數結構體

    """

    def __init__(self):
        """
        :param BeginDate: 專業周報開始時間。
        :type BeginDate: str
        :param Limit: 返回數量，預設爲10，最大值爲100。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        """
        self.BeginDate = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeWeeklyReportBruteAttacksResponse(AbstractModel):
    """DescribeWeeklyReportBruteAttacks返回參數結構體

    """

    def __init__(self):
        """
        :param WeeklyReportBruteAttacks: 專業周報密碼破解數組。
        :type WeeklyReportBruteAttacks: list of WeeklyReportBruteAttack
        :param TotalCount: 記錄總數。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.WeeklyReportBruteAttacks = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WeeklyReportBruteAttacks") is not None:
            self.WeeklyReportBruteAttacks = []
            for item in params.get("WeeklyReportBruteAttacks"):
                obj = WeeklyReportBruteAttack()
                obj._deserialize(item)
                self.WeeklyReportBruteAttacks.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWeeklyReportInfoRequest(AbstractModel):
    """DescribeWeeklyReportInfo請求參數結構體

    """

    def __init__(self):
        """
        :param BeginDate: 專業周報開始時間。
        :type BeginDate: str
        """
        self.BeginDate = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")


class DescribeWeeklyReportInfoResponse(AbstractModel):
    """DescribeWeeklyReportInfo返回參數結構體

    """

    def __init__(self):
        """
        :param CompanyName: 賬号所屬公司或個人名稱。
        :type CompanyName: str
        :param MachineNum: 機器總數。
        :type MachineNum: int
        :param OnlineMachineNum: 雲鏡用戶端在線數。
        :type OnlineMachineNum: int
        :param OfflineMachineNum: 雲鏡用戶端離線數。
        :type OfflineMachineNum: int
        :param ProVersionMachineNum: 開通雲鏡專業版數量。
        :type ProVersionMachineNum: int
        :param BeginDate: 周報開始時間。
        :type BeginDate: str
        :param EndDate: 周報結束時間。
        :type EndDate: str
        :param Level: 安全等級。
<li>HIGH：高</li>
<li>MIDDLE：中</li>
<li>LOW：低</li>
        :type Level: str
        :param MalwareNum: 木馬記錄數。
        :type MalwareNum: int
        :param NonlocalLoginNum: 異地登入數。
        :type NonlocalLoginNum: int
        :param BruteAttackSuccessNum: 密碼破解成功數。
        :type BruteAttackSuccessNum: int
        :param VulNum: 漏洞數。
        :type VulNum: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CompanyName = None
        self.MachineNum = None
        self.OnlineMachineNum = None
        self.OfflineMachineNum = None
        self.ProVersionMachineNum = None
        self.BeginDate = None
        self.EndDate = None
        self.Level = None
        self.MalwareNum = None
        self.NonlocalLoginNum = None
        self.BruteAttackSuccessNum = None
        self.VulNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyName = params.get("CompanyName")
        self.MachineNum = params.get("MachineNum")
        self.OnlineMachineNum = params.get("OnlineMachineNum")
        self.OfflineMachineNum = params.get("OfflineMachineNum")
        self.ProVersionMachineNum = params.get("ProVersionMachineNum")
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")
        self.Level = params.get("Level")
        self.MalwareNum = params.get("MalwareNum")
        self.NonlocalLoginNum = params.get("NonlocalLoginNum")
        self.BruteAttackSuccessNum = params.get("BruteAttackSuccessNum")
        self.VulNum = params.get("VulNum")
        self.RequestId = params.get("RequestId")


class DescribeWeeklyReportMalwaresRequest(AbstractModel):
    """DescribeWeeklyReportMalwares請求參數結構體

    """

    def __init__(self):
        """
        :param BeginDate: 專業周報開始時間。
        :type BeginDate: str
        :param Limit: 返回數量，預設爲10，最大值爲100。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        """
        self.BeginDate = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeWeeklyReportMalwaresResponse(AbstractModel):
    """DescribeWeeklyReportMalwares返回參數結構體

    """

    def __init__(self):
        """
        :param WeeklyReportMalwares: 專業周報木馬數據。
        :type WeeklyReportMalwares: list of WeeklyReportMalware
        :param TotalCount: 記錄總數。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.WeeklyReportMalwares = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WeeklyReportMalwares") is not None:
            self.WeeklyReportMalwares = []
            for item in params.get("WeeklyReportMalwares"):
                obj = WeeklyReportMalware()
                obj._deserialize(item)
                self.WeeklyReportMalwares.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWeeklyReportNonlocalLoginPlacesRequest(AbstractModel):
    """DescribeWeeklyReportNonlocalLoginPlaces請求參數結構體

    """

    def __init__(self):
        """
        :param BeginDate: 專業周報開始時間。
        :type BeginDate: str
        :param Limit: 返回數量，預設爲10，最大值爲100。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        """
        self.BeginDate = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeWeeklyReportNonlocalLoginPlacesResponse(AbstractModel):
    """DescribeWeeklyReportNonlocalLoginPlaces返回參數結構體

    """

    def __init__(self):
        """
        :param WeeklyReportNonlocalLoginPlaces: 專業周報異地登入數據。
        :type WeeklyReportNonlocalLoginPlaces: list of WeeklyReportNonlocalLoginPlace
        :param TotalCount: 記錄總數。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.WeeklyReportNonlocalLoginPlaces = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WeeklyReportNonlocalLoginPlaces") is not None:
            self.WeeklyReportNonlocalLoginPlaces = []
            for item in params.get("WeeklyReportNonlocalLoginPlaces"):
                obj = WeeklyReportNonlocalLoginPlace()
                obj._deserialize(item)
                self.WeeklyReportNonlocalLoginPlaces.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWeeklyReportVulsRequest(AbstractModel):
    """DescribeWeeklyReportVuls請求參數結構體

    """

    def __init__(self):
        """
        :param BeginDate: 專業版周報開始時間。
        :type BeginDate: str
        :param Limit: 返回數量，預設爲10，最大值爲100。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        """
        self.BeginDate = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeWeeklyReportVulsResponse(AbstractModel):
    """DescribeWeeklyReportVuls返回參數結構體

    """

    def __init__(self):
        """
        :param WeeklyReportVuls: 專業周報漏洞數據數組。
        :type WeeklyReportVuls: list of WeeklyReportVul
        :param TotalCount: 記錄總數。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.WeeklyReportVuls = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WeeklyReportVuls") is not None:
            self.WeeklyReportVuls = []
            for item in params.get("WeeklyReportVuls"):
                obj = WeeklyReportVul()
                obj._deserialize(item)
                self.WeeklyReportVuls.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWeeklyReportsRequest(AbstractModel):
    """DescribeWeeklyReports請求參數結構體

    """

    def __init__(self):
        """
        :param Limit: 返回數量，預設爲10，最大值爲100。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeWeeklyReportsResponse(AbstractModel):
    """DescribeWeeklyReports返回參數結構體

    """

    def __init__(self):
        """
        :param WeeklyReports: 專業周報清單數組。
        :type WeeklyReports: list of WeeklyReport
        :param TotalCount: 記錄總數。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.WeeklyReports = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WeeklyReports") is not None:
            self.WeeklyReports = []
            for item in params.get("WeeklyReports"):
                obj = WeeklyReport()
                obj._deserialize(item)
                self.WeeklyReports.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ExportMaliciousRequestsRequest(AbstractModel):
    """ExportMaliciousRequests請求參數結構體

    """


class ExportMaliciousRequestsResponse(AbstractModel):
    """ExportMaliciousRequests返回參數結構體

    """

    def __init__(self):
        """
        :param DownloadUrl: 導出文件下載連結網址。
        :type DownloadUrl: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """描述鍵值對過濾器，用于條件過濾查詢。例如過濾ID、名稱、狀态等

    若存在多個Filter時，Filter間的關系爲邏輯與（AND）關系。
    若同一個Filter存在多個Values，同一Filter下Values間的關系爲邏輯或（OR）關系。

    * 最多只能有5個Filter
    * 同一個Filter存在多個Values，Values值數量最多不能超過5個。

    """

    def __init__(self):
        """
        :param Name: 過濾鍵的名稱。
        :type Name: str
        :param Values: 一個或者多個過濾值。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class HistoryAccount(AbstractModel):
    """賬号變更曆史數據。

    """

    def __init__(self):
        """
        :param Id: 唯一ID。
        :type Id: int
        :param Uuid: 雲鏡用戶端唯一Uuid。
        :type Uuid: str
        :param MachineIp: 主機内網IP。
        :type MachineIp: str
        :param MachineName: 主機名。
        :type MachineName: str
        :param Username: 帳号名。
        :type Username: str
        :param ModifyType: 帳号變更類型。
<li>CREATE：表示新增帳号</li>
<li>MODIFY：表示修改帳号</li>
<li>DELETE：表示删除帳号</li>
        :type ModifyType: str
        :param ModifyTime: 變更時間。
        :type ModifyTime: str
        """
        self.Id = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None
        self.Username = None
        self.ModifyType = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.Username = params.get("Username")
        self.ModifyType = params.get("ModifyType")
        self.ModifyTime = params.get("ModifyTime")


class IgnoreImpactedHostsRequest(AbstractModel):
    """IgnoreImpactedHosts請求參數結構體

    """

    def __init__(self):
        """
        :param Ids: 漏洞ID數組。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class IgnoreImpactedHostsResponse(AbstractModel):
    """IgnoreImpactedHosts返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ImpactedHost(AbstractModel):
    """受影響主機訊息

    """

    def __init__(self):
        """
        :param Id: 漏洞ID。
        :type Id: int
        :param MachineIp: 主機IP。
        :type MachineIp: str
        :param MachineName: 主機名稱。
        :type MachineName: str
        :param LastScanTime: 最後檢測時間。
        :type LastScanTime: str
        :param VulStatus: 漏洞狀态。
<li>UN_OPERATED ：待處理</li>
<li>SCANING : 掃描中</li>
<li>FIXED : 已修複</li>
        :type VulStatus: str
        :param Uuid: 雲鏡用戶端唯一标識UUID。
        :type Uuid: str
        :param Description: 漏洞描述。
        :type Description: str
        :param VulId: 漏洞種類ID。
        :type VulId: int
        """
        self.Id = None
        self.MachineIp = None
        self.MachineName = None
        self.LastScanTime = None
        self.VulStatus = None
        self.Uuid = None
        self.Description = None
        self.VulId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.LastScanTime = params.get("LastScanTime")
        self.VulStatus = params.get("VulStatus")
        self.Uuid = params.get("Uuid")
        self.Description = params.get("Description")
        self.VulId = params.get("VulId")


class InquiryPriceOpenProVersionPrepaidRequest(AbstractModel):
    """InquiryPriceOpenProVersionPrepaid請求參數結構體

    """

    def __init__(self):
        """
        :param ChargePrepaid: 預付費模式(包年包月)參數設置。
        :type ChargePrepaid: :class:`taifucloudcloud.yunjing.v20180228.models.ChargePrepaid`
        :param Machines: 需要開通專業版機器清單數組。
        :type Machines: list of ProVersionMachine
        """
        self.ChargePrepaid = None
        self.Machines = None


    def _deserialize(self, params):
        if params.get("ChargePrepaid") is not None:
            self.ChargePrepaid = ChargePrepaid()
            self.ChargePrepaid._deserialize(params.get("ChargePrepaid"))
        if params.get("Machines") is not None:
            self.Machines = []
            for item in params.get("Machines"):
                obj = ProVersionMachine()
                obj._deserialize(item)
                self.Machines.append(obj)


class InquiryPriceOpenProVersionPrepaidResponse(AbstractModel):
    """InquiryPriceOpenProVersionPrepaid返回參數結構體

    """

    def __init__(self):
        """
        :param OriginalPrice: 預支費用的原價，單位：元。
        :type OriginalPrice: float
        :param DiscountPrice: 預支費用的折扣價，單位：元。
        :type DiscountPrice: float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.OriginalPrice = None
        self.DiscountPrice = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")
        self.RequestId = params.get("RequestId")


class Machine(AbstractModel):
    """主機清單

    """

    def __init__(self):
        """
        :param MachineName: 主機名稱。
        :type MachineName: str
        :param MachineOs: 主機系統。
        :type MachineOs: str
        :param MachineStatus: 主機狀态。
<li>OFFLINE: 離線  </li>
<li>ONLINE: 在線</li>
        :type MachineStatus: str
        :param Uuid: 雲鏡用戶端唯一Uuid，若用戶端長時間不在線将返回空字元。
        :type Uuid: str
        :param Quuid: CVM或BM機器唯一Uuid。
        :type Quuid: str
        :param VulNum: 漏洞數，非專業版将返回：0。
        :type VulNum: int
        :param MachineIp: 主機IP。
        :type MachineIp: str
        :param IsProVersion: 是否是專業版。
<li>true： 是</li>
<li>false：否</li>
        :type IsProVersion: bool
        :param MachineWanIp: 主機外網IP。
        :type MachineWanIp: str
        :param PayMode: 主機狀态。
<li>POSTPAY: 表示後付費，即按量計費  </li>
<li>PREPAY: 表示預付費，即包年包月</li>
        :type PayMode: str
        """
        self.MachineName = None
        self.MachineOs = None
        self.MachineStatus = None
        self.Uuid = None
        self.Quuid = None
        self.VulNum = None
        self.MachineIp = None
        self.IsProVersion = None
        self.MachineWanIp = None
        self.PayMode = None


    def _deserialize(self, params):
        self.MachineName = params.get("MachineName")
        self.MachineOs = params.get("MachineOs")
        self.MachineStatus = params.get("MachineStatus")
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        self.VulNum = params.get("VulNum")
        self.MachineIp = params.get("MachineIp")
        self.IsProVersion = params.get("IsProVersion")
        self.MachineWanIp = params.get("MachineWanIp")
        self.PayMode = params.get("PayMode")


class MaliciousRequest(AbstractModel):
    """惡意請求數據。

    """

    def __init__(self):
        """
        :param Id: 記錄ID。
        :type Id: int
        :param Uuid: 雲鏡用戶端UUID。
        :type Uuid: str
        :param MachineIp: 主機内網IP。
        :type MachineIp: str
        :param MachineName: 主機名。
        :type MachineName: str
        :param Domain: 惡意請求域名。
        :type Domain: str
        :param Count: 惡意請求數。
        :type Count: int
        :param ProcessName: 程式名。
        :type ProcessName: str
        :param Status: 記錄狀态。
<li>UN_OPERATED：待處理</li>
<li>TRUSTED：已信任</li>
<li>UN_TRUSTED：已取消信任</li>
        :type Status: str
        :param Description: 惡意請求域名描述。
        :type Description: str
        :param Reference: 參考網址。
        :type Reference: str
        :param CreateTime: 發現時間。
        :type CreateTime: str
        :param MergeTime: 記錄合并時間。
        :type MergeTime: str
        :param ProcessMd5: 程式MD5
值。
        :type ProcessMd5: str
        :param CmdLine: 執行命令行。
        :type CmdLine: str
        :param Pid: 程式PID。
        :type Pid: int
        """
        self.Id = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None
        self.Domain = None
        self.Count = None
        self.ProcessName = None
        self.Status = None
        self.Description = None
        self.Reference = None
        self.CreateTime = None
        self.MergeTime = None
        self.ProcessMd5 = None
        self.CmdLine = None
        self.Pid = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.Domain = params.get("Domain")
        self.Count = params.get("Count")
        self.ProcessName = params.get("ProcessName")
        self.Status = params.get("Status")
        self.Description = params.get("Description")
        self.Reference = params.get("Reference")
        self.CreateTime = params.get("CreateTime")
        self.MergeTime = params.get("MergeTime")
        self.ProcessMd5 = params.get("ProcessMd5")
        self.CmdLine = params.get("CmdLine")
        self.Pid = params.get("Pid")


class Malware(AbstractModel):
    """木馬相關訊息

    """

    def __init__(self):
        """
        :param Id: 事件ID。
        :type Id: int
        :param MachineIp: 主機IP。
        :type MachineIp: str
        :param Status: 當前木馬狀态。
<li>UN_OPERATED：未處理</li><li>SEGREGATED：已隔離</li><li>TRUSTED：已信任</li>
<li>SEPARATING：隔離中</li><li>RECOVERING：恢複中</li>
        :type Status: str
        :param FilePath: 木馬所在的路徑。
        :type FilePath: str
        :param Description: 木馬描述。
        :type Description: str
        :param MachineName: 主機名稱。
        :type MachineName: str
        :param FileCreateTime: 木馬文件創建時間。
        :type FileCreateTime: str
        :param ModifyTime: 木馬文件修改時間。
        :type ModifyTime: str
        :param Uuid: 雲鏡用戶端唯一标識UUID。
        :type Uuid: str
        """
        self.Id = None
        self.MachineIp = None
        self.Status = None
        self.FilePath = None
        self.Description = None
        self.MachineName = None
        self.FileCreateTime = None
        self.ModifyTime = None
        self.Uuid = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MachineIp = params.get("MachineIp")
        self.Status = params.get("Status")
        self.FilePath = params.get("FilePath")
        self.Description = params.get("Description")
        self.MachineName = params.get("MachineName")
        self.FileCreateTime = params.get("FileCreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.Uuid = params.get("Uuid")


class MisAlarmNonlocalLoginPlacesRequest(AbstractModel):
    """MisAlarmNonlocalLoginPlaces請求參數結構體

    """

    def __init__(self):
        """
        :param Ids: 異地登入事件Id數組。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class MisAlarmNonlocalLoginPlacesResponse(AbstractModel):
    """MisAlarmNonlocalLoginPlaces返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAlarmAttributeRequest(AbstractModel):
    """ModifyAlarmAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param Attribute: 告警項目。
<li>Offline：防護軟體離線</li>
<li>Malware：發現木馬文件</li>
<li>NonlocalLogin：發現異地登入行爲</li>
<li>CrackSuccess：被暴力破解成功</li>
        :type Attribute: str
        :param Value: 告警項目屬性。
<li>CLOSE：關閉</li>
<li>OPEN：打開</li>
        :type Value: str
        """
        self.Attribute = None
        self.Value = None


    def _deserialize(self, params):
        self.Attribute = params.get("Attribute")
        self.Value = params.get("Value")


class ModifyAlarmAttributeResponse(AbstractModel):
    """ModifyAlarmAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAutoOpenProVersionConfigRequest(AbstractModel):
    """ModifyAutoOpenProVersionConfig請求參數結構體

    """

    def __init__(self):
        """
        :param Status: 設置自動開通狀态。
<li>CLOSE：關閉</li>
<li>OPEN：打開</li>
        :type Status: str
        """
        self.Status = None


    def _deserialize(self, params):
        self.Status = params.get("Status")


class ModifyAutoOpenProVersionConfigResponse(AbstractModel):
    """ModifyAutoOpenProVersionConfig返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyProVersionRenewFlagRequest(AbstractModel):
    """ModifyProVersionRenewFlag請求參數結構體

    """

    def __init__(self):
        """
        :param RenewFlag: 自動續約标識。取值範圍：
<li>NOTIFY_AND_AUTO_RENEW：通知過期且自動續約</li>
<li>NOTIFY_AND_MANUAL_RENEW：通知過期不自動續約</li>
<li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知過期不自動續約</li>
        :type RenewFlag: str
        :param Quuid: 主機唯一ID，對應CVM的uuid、BM的instanceId。
        :type Quuid: str
        """
        self.RenewFlag = None
        self.Quuid = None


    def _deserialize(self, params):
        self.RenewFlag = params.get("RenewFlag")
        self.Quuid = params.get("Quuid")


class ModifyProVersionRenewFlagResponse(AbstractModel):
    """ModifyProVersionRenewFlag返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NonLocalLoginPlace(AbstractModel):
    """異地登入

    """

    def __init__(self):
        """
        :param Id: 事件ID。
        :type Id: int
        :param MachineIp: 主機IP。
        :type MachineIp: str
        :param Status: 登入狀态
<li>NON_LOCAL_LOGIN：異地登入</li>
<li>NORMAL_LOGIN：正常登入</li>
        :type Status: str
        :param UserName: 用戶名。
        :type UserName: str
        :param City: 城市ID。
        :type City: int
        :param Country: 國家ID。
        :type Country: int
        :param Province:  ID。
        :type Province: int
        :param SrcIp: 登入IP。
        :type SrcIp: str
        :param MachineName: 機器名稱。
        :type MachineName: str
        :param LoginTime: 登入時間。
        :type LoginTime: str
        :param Uuid: 雲鏡用戶端唯一标識Uuid。
        :type Uuid: str
        """
        self.Id = None
        self.MachineIp = None
        self.Status = None
        self.UserName = None
        self.City = None
        self.Country = None
        self.Province = None
        self.SrcIp = None
        self.MachineName = None
        self.LoginTime = None
        self.Uuid = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MachineIp = params.get("MachineIp")
        self.Status = params.get("Status")
        self.UserName = params.get("UserName")
        self.City = params.get("City")
        self.Country = params.get("Country")
        self.Province = params.get("Province")
        self.SrcIp = params.get("SrcIp")
        self.MachineName = params.get("MachineName")
        self.LoginTime = params.get("LoginTime")
        self.Uuid = params.get("Uuid")


class OpenPort(AbstractModel):
    """端口清單

    """

    def __init__(self):
        """
        :param Id: 唯一ID。
        :type Id: int
        :param Uuid: 雲鏡用戶端唯一UUID。
        :type Uuid: str
        :param Port: 開放端口号。
        :type Port: int
        :param MachineIp: 主機IP。
        :type MachineIp: str
        :param MachineName: 主機名。
        :type MachineName: str
        :param ProcessName: 端口對應程式名。
        :type ProcessName: str
        :param Pid: 端口對應程式Pid。
        :type Pid: int
        :param CreateTime: 記錄創建時間。
        :type CreateTime: str
        :param ModifyTime: 記錄更新時間。
        :type ModifyTime: str
        """
        self.Id = None
        self.Uuid = None
        self.Port = None
        self.MachineIp = None
        self.MachineName = None
        self.ProcessName = None
        self.Pid = None
        self.CreateTime = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.Port = params.get("Port")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.ProcessName = params.get("ProcessName")
        self.Pid = params.get("Pid")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")


class OpenPortStatistics(AbstractModel):
    """端口統計清單

    """

    def __init__(self):
        """
        :param Port: 端口号
        :type Port: int
        :param MachineNum: 主機數量
        :type MachineNum: int
        """
        self.Port = None
        self.MachineNum = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.MachineNum = params.get("MachineNum")


class OpenProVersionPrepaidRequest(AbstractModel):
    """OpenProVersionPrepaid請求參數結構體

    """

    def __init__(self):
        """
        :param ChargePrepaid: 購買相關參數。
        :type ChargePrepaid: :class:`taifucloudcloud.yunjing.v20180228.models.ChargePrepaid`
        :param Machines: 需要開通專業版主機訊息數組。
        :type Machines: list of ProVersionMachine
        """
        self.ChargePrepaid = None
        self.Machines = None


    def _deserialize(self, params):
        if params.get("ChargePrepaid") is not None:
            self.ChargePrepaid = ChargePrepaid()
            self.ChargePrepaid._deserialize(params.get("ChargePrepaid"))
        if params.get("Machines") is not None:
            self.Machines = []
            for item in params.get("Machines"):
                obj = ProVersionMachine()
                obj._deserialize(item)
                self.Machines.append(obj)


class OpenProVersionPrepaidResponse(AbstractModel):
    """OpenProVersionPrepaid返回參數結構體

    """

    def __init__(self):
        """
        :param DealIds: 訂單ID清單。
        :type DealIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DealIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealIds = params.get("DealIds")
        self.RequestId = params.get("RequestId")


class Place(AbstractModel):
    """登入地訊息

    """

    def __init__(self):
        """
        :param CityId: 城市 ID。
        :type CityId: int
        :param ProvinceId:   ID。
        :type ProvinceId: int
        :param CountryId: 國家ID，暫只支援國内：1。
        :type CountryId: int
        """
        self.CityId = None
        self.ProvinceId = None
        self.CountryId = None


    def _deserialize(self, params):
        self.CityId = params.get("CityId")
        self.ProvinceId = params.get("ProvinceId")
        self.CountryId = params.get("CountryId")


class ProVersionMachine(AbstractModel):
    """需要開通專業版機器訊息。

    """

    def __init__(self):
        """
        :param MachineType: 主機類型。
<li>CVM: 虛拟主機</li>
<li>BM: 黑石物理機</li>
        :type MachineType: str
        :param MachineRegion: 主機所在地域。
如：ap-guangzhou、ap-beijing
        :type MachineRegion: str
        :param Quuid: 主機唯一标識Uuid。
黑石的InstanceId，CVM的Uuid
        :type Quuid: str
        """
        self.MachineType = None
        self.MachineRegion = None
        self.Quuid = None


    def _deserialize(self, params):
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        self.Quuid = params.get("Quuid")


class Process(AbstractModel):
    """程式訊息數據。

    """

    def __init__(self):
        """
        :param Id: 唯一ID。
        :type Id: int
        :param Uuid: 雲鏡用戶端唯一UUID。
        :type Uuid: str
        :param MachineIp: 主機内網IP。
        :type MachineIp: str
        :param MachineName: 主機名。
        :type MachineName: str
        :param Pid: 程式Pid。
        :type Pid: int
        :param Ppid: 程式Ppid。
        :type Ppid: int
        :param ProcessName: 程式名。
        :type ProcessName: str
        :param Username: 程式用戶名。
        :type Username: str
        :param Platform: 所屬平台。
<li>WIN32：windows32位</li>
<li>WIN64：windows64位</li>
<li>LINUX32：Linux32位</li>
<li>LINUX64：Linux64位</li>
        :type Platform: str
        :param FullPath: 程式路徑。
        :type FullPath: str
        :param CreateTime: 創建時間。
        :type CreateTime: str
        """
        self.Id = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None
        self.Pid = None
        self.Ppid = None
        self.ProcessName = None
        self.Username = None
        self.Platform = None
        self.FullPath = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.Pid = params.get("Pid")
        self.Ppid = params.get("Ppid")
        self.ProcessName = params.get("ProcessName")
        self.Username = params.get("Username")
        self.Platform = params.get("Platform")
        self.FullPath = params.get("FullPath")
        self.CreateTime = params.get("CreateTime")


class ProcessStatistics(AbstractModel):
    """程式數據統計數據。

    """

    def __init__(self):
        """
        :param ProcessName: 程式名。
        :type ProcessName: str
        :param MachineNum: 主機數量。
        :type MachineNum: int
        """
        self.ProcessName = None
        self.MachineNum = None


    def _deserialize(self, params):
        self.ProcessName = params.get("ProcessName")
        self.MachineNum = params.get("MachineNum")


class RecoverMalwaresRequest(AbstractModel):
    """RecoverMalwares請求參數結構體

    """

    def __init__(self):
        """
        :param Ids: 木馬Id數組,單次最大删除不能超過200條
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class RecoverMalwaresResponse(AbstractModel):
    """RecoverMalwares返回參數結構體

    """

    def __init__(self):
        """
        :param SuccessIds: 恢複成功id數組
        :type SuccessIds: list of int non-negative
        :param FailedIds: 恢複失敗id數組
        :type FailedIds: list of int non-negative
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SuccessIds = None
        self.FailedIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessIds = params.get("SuccessIds")
        self.FailedIds = params.get("FailedIds")
        self.RequestId = params.get("RequestId")


class RenewProVersionRequest(AbstractModel):
    """RenewProVersion請求參數結構體

    """

    def __init__(self):
        """
        :param ChargePrepaid: 購買相關參數。
        :type ChargePrepaid: :class:`taifucloudcloud.yunjing.v20180228.models.ChargePrepaid`
        :param Quuid: 主機唯一ID，對應CVM的uuid、BM的InstanceId。
        :type Quuid: str
        """
        self.ChargePrepaid = None
        self.Quuid = None


    def _deserialize(self, params):
        if params.get("ChargePrepaid") is not None:
            self.ChargePrepaid = ChargePrepaid()
            self.ChargePrepaid._deserialize(params.get("ChargePrepaid"))
        self.Quuid = params.get("Quuid")


class RenewProVersionResponse(AbstractModel):
    """RenewProVersion返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RescanImpactedHostRequest(AbstractModel):
    """RescanImpactedHost請求參數結構體

    """

    def __init__(self):
        """
        :param Id: 漏洞ID。
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")


class RescanImpactedHostResponse(AbstractModel):
    """RescanImpactedHost返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SecurityDynamic(AbstractModel):
    """安全事件訊息數據。

    """

    def __init__(self):
        """
        :param Uuid: 雲鏡用戶端UUID。
        :type Uuid: str
        :param EventTime: 安全事件發生事件。
        :type EventTime: str
        :param EventType: 安全事件類型。
<li>MALWARE：木馬事件</li>
<li>NON_LOCAL_LOGIN：異地登入</li>
<li>BRUTEATTACK_SUCCESS：密碼破解成功</li>
<li>VUL：漏洞</li>
<li>BASELINE：安全基線</li>
        :type EventType: str
        :param Message: 安全事件訊息。
        :type Message: str
        """
        self.Uuid = None
        self.EventTime = None
        self.EventType = None
        self.Message = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.EventTime = params.get("EventTime")
        self.EventType = params.get("EventType")
        self.Message = params.get("Message")


class SecurityTrend(AbstractModel):
    """安全趨勢統計數據。

    """

    def __init__(self):
        """
        :param Date: 事件時間。
        :type Date: str
        :param EventNum: 事件數量。
        :type EventNum: int
        """
        self.Date = None
        self.EventNum = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.EventNum = params.get("EventNum")


class SeparateMalwaresRequest(AbstractModel):
    """SeparateMalwares請求參數結構體

    """

    def __init__(self):
        """
        :param Ids: 木馬事件Id數組。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class SeparateMalwaresResponse(AbstractModel):
    """SeparateMalwares返回參數結構體

    """

    def __init__(self):
        """
        :param SuccessIds: 隔離成功的id數組。
        :type SuccessIds: list of int non-negative
        :param FailedIds: 隔離失敗的id數組。
        :type FailedIds: list of int non-negative
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SuccessIds = None
        self.FailedIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessIds = params.get("SuccessIds")
        self.FailedIds = params.get("FailedIds")
        self.RequestId = params.get("RequestId")


class TrustMaliciousRequestRequest(AbstractModel):
    """TrustMaliciousRequest請求參數結構體

    """

    def __init__(self):
        """
        :param Id: 惡意請求記錄ID。
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")


class TrustMaliciousRequestResponse(AbstractModel):
    """TrustMaliciousRequest返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TrustMalwaresRequest(AbstractModel):
    """TrustMalwares請求參數結構體

    """

    def __init__(self):
        """
        :param Ids: 木馬ID數組。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class TrustMalwaresResponse(AbstractModel):
    """TrustMalwares返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UntrustMaliciousRequestRequest(AbstractModel):
    """UntrustMaliciousRequest請求參數結構體

    """

    def __init__(self):
        """
        :param Id: 受信任記錄ID。
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")


class UntrustMaliciousRequestResponse(AbstractModel):
    """UntrustMaliciousRequest返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UntrustMalwaresRequest(AbstractModel):
    """UntrustMalwares請求參數結構體

    """

    def __init__(self):
        """
        :param Ids: 木馬Id數組，單次最大處理不能超過200條。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class UntrustMalwaresResponse(AbstractModel):
    """UntrustMalwares返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UsualPlace(AbstractModel):
    """常用登入地

    """

    def __init__(self):
        """
        :param Id: ID。
        :type Id: int
        :param Uuid: 雲鏡用戶端唯一标識UUID。
        :type Uuid: str
        :param CountryId: 國家 ID。
        :type CountryId: int
        :param ProvinceId:   ID。
        :type ProvinceId: int
        :param CityId: 城市 ID。
        :type CityId: int
        """
        self.Id = None
        self.Uuid = None
        self.CountryId = None
        self.ProvinceId = None
        self.CityId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.CountryId = params.get("CountryId")
        self.ProvinceId = params.get("ProvinceId")
        self.CityId = params.get("CityId")


class Vul(AbstractModel):
    """漏洞清單數據

    """

    def __init__(self):
        """
        :param VulId: 漏洞種類ID
        :type VulId: int
        :param VulName: 漏洞名稱
        :type VulName: str
        :param VulLevel: 漏洞危害等級:
HIGH：高危
MIDDLE：中危
LOW：低危
NOTICE：提示
        :type VulLevel: str
        :param LastScanTime: 最後掃描時間
        :type LastScanTime: str
        :param ImpactedHostNum: 受影響機器數量
        :type ImpactedHostNum: int
        :param VulStatus: 漏洞狀态
* UN_OPERATED : 待處理
* FIXED : 已修複
        :type VulStatus: str
        """
        self.VulId = None
        self.VulName = None
        self.VulLevel = None
        self.LastScanTime = None
        self.ImpactedHostNum = None
        self.VulStatus = None


    def _deserialize(self, params):
        self.VulId = params.get("VulId")
        self.VulName = params.get("VulName")
        self.VulLevel = params.get("VulLevel")
        self.LastScanTime = params.get("LastScanTime")
        self.ImpactedHostNum = params.get("ImpactedHostNum")
        self.VulStatus = params.get("VulStatus")


class WeeklyReport(AbstractModel):
    """周報清單。

    """

    def __init__(self):
        """
        :param BeginDate: 周報開始時間。
        :type BeginDate: str
        :param EndDate: 周報結束時間。
        :type EndDate: str
        """
        self.BeginDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")


class WeeklyReportBruteAttack(AbstractModel):
    """專業周報密碼破解數據。

    """

    def __init__(self):
        """
        :param MachineIp: 主機IP。
        :type MachineIp: str
        :param Username: 被破解用戶名。
        :type Username: str
        :param SrcIp: 源IP。
        :type SrcIp: str
        :param Count: 嘗試次數。
        :type Count: int
        :param AttackTime: 攻擊時間。
        :type AttackTime: str
        """
        self.MachineIp = None
        self.Username = None
        self.SrcIp = None
        self.Count = None
        self.AttackTime = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.Username = params.get("Username")
        self.SrcIp = params.get("SrcIp")
        self.Count = params.get("Count")
        self.AttackTime = params.get("AttackTime")


class WeeklyReportMalware(AbstractModel):
    """專業周報木馬數據。

    """

    def __init__(self):
        """
        :param MachineIp: 主機IP。
        :type MachineIp: str
        :param FilePath: 木馬文件路徑。
        :type FilePath: str
        :param Md5: 木馬文件MD5值。
        :type Md5: str
        :param FindTime: 木馬發現時間。
        :type FindTime: str
        :param Status: 當前木馬狀态。
<li>UN_OPERATED：未處理</li>
<li>SEGREGATED：已隔離</li>
<li>TRUSTED：已信任</li>
<li>SEPARATING：隔離中</li>
<li>RECOVERING：恢複中</li>
        :type Status: str
        """
        self.MachineIp = None
        self.FilePath = None
        self.Md5 = None
        self.FindTime = None
        self.Status = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.FilePath = params.get("FilePath")
        self.Md5 = params.get("Md5")
        self.FindTime = params.get("FindTime")
        self.Status = params.get("Status")


class WeeklyReportNonlocalLoginPlace(AbstractModel):
    """專業周報異地登入數據。

    """

    def __init__(self):
        """
        :param MachineIp: 主機IP。
        :type MachineIp: str
        :param Username: 用戶名。
        :type Username: str
        :param SrcIp: 源IP。
        :type SrcIp: str
        :param Country: 國家ID。
        :type Country: int
        :param Province:  ID。
        :type Province: int
        :param City: 城市ID。
        :type City: int
        :param LoginTime: 登入時間。
        :type LoginTime: str
        """
        self.MachineIp = None
        self.Username = None
        self.SrcIp = None
        self.Country = None
        self.Province = None
        self.City = None
        self.LoginTime = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.Username = params.get("Username")
        self.SrcIp = params.get("SrcIp")
        self.Country = params.get("Country")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.LoginTime = params.get("LoginTime")


class WeeklyReportVul(AbstractModel):
    """專業版周報漏洞數據。

    """

    def __init__(self):
        """
        :param MachineIp: 主機内網IP。
        :type MachineIp: str
        :param VulName: 漏洞名稱。
        :type VulName: str
        :param VulType: 漏洞類型。
<li> WEB : WEB漏洞</li>
<li> SYSTEM :系統元件漏洞</li>
<li> BASELINE : 安全基線</li>
        :type VulType: str
        :param Description: 漏洞描述。
        :type Description: str
        :param VulStatus: 漏洞狀态。
<li> UN_OPERATED : 待處理</li>
<li> SCANING : 掃描中</li>
<li> FIXED : 已修複</li>
        :type VulStatus: str
        :param LastScanTime: 最後掃描時間。
        :type LastScanTime: str
        """
        self.MachineIp = None
        self.VulName = None
        self.VulType = None
        self.Description = None
        self.VulStatus = None
        self.LastScanTime = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.VulName = params.get("VulName")
        self.VulType = params.get("VulType")
        self.Description = params.get("Description")
        self.VulStatus = params.get("VulStatus")
        self.LastScanTime = params.get("LastScanTime")