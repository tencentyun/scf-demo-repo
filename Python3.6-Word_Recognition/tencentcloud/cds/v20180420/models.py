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


class CdsAuditInstance(AbstractModel):
    """數據安全産品實例訊息

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param AppId: 用戶AppId
        :type AppId: str
        :param Uin: 用戶Uin
        :type Uin: str
        :param ProjectId: 項目ID
        :type ProjectId: int
        :param RenewFlag: 續約标識
        :type RenewFlag: int
        :param Region: 所屬地域
        :type Region: str
        :param PayMode: 付費模式（數據安全審計只支援預付費：1）
        :type PayMode: int
        :param Status: 實例狀态： 0，未生效；1：正常運作； 2：被隔離； 3，已過期
        :type Status: int
        :param IsolatedTimestamp: 實例被隔離時間，格式：yyyy-mm-dd HH:ii:ss
        :type IsolatedTimestamp: str
        :param CreateTime: 實例創建時間，格式： yyyy-mm-dd HH:ii:ss
        :type CreateTime: str
        :param ExpireTime: 實例過期時間，格式：yyyy-mm-dd HH:ii:ss
        :type ExpireTime: str
        """
        self.InstanceId = None
        self.AppId = None
        self.Uin = None
        self.ProjectId = None
        self.RenewFlag = None
        self.Region = None
        self.PayMode = None
        self.Status = None
        self.IsolatedTimestamp = None
        self.CreateTime = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AppId = params.get("AppId")
        self.Uin = params.get("Uin")
        self.ProjectId = params.get("ProjectId")
        self.RenewFlag = params.get("RenewFlag")
        self.Region = params.get("Region")
        self.PayMode = params.get("PayMode")
        self.Status = params.get("Status")
        self.IsolatedTimestamp = params.get("IsolatedTimestamp")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")


class DbauditTypesInfo(AbstractModel):
    """數據安全審計産品規格訊息

    """

    def __init__(self):
        """
        :param InstanceVersionName: 規格描述
        :type InstanceVersionName: str
        :param InstanceVersionKey: 規格名稱
        :type InstanceVersionKey: str
        :param Qps: 最大吞吐量
        :type Qps: int
        :param MaxInstances: 最大實例數
        :type MaxInstances: int
        :param InsertSpeed: 入庫速率（每小時）
        :type InsertSpeed: int
        :param OnlineStorageCapacity: 最大在線儲存量，單位：條
        :type OnlineStorageCapacity: int
        :param ArchivingStorageCapacity: 最大歸檔儲存量，單位：條
        :type ArchivingStorageCapacity: int
        """
        self.InstanceVersionName = None
        self.InstanceVersionKey = None
        self.Qps = None
        self.MaxInstances = None
        self.InsertSpeed = None
        self.OnlineStorageCapacity = None
        self.ArchivingStorageCapacity = None


    def _deserialize(self, params):
        self.InstanceVersionName = params.get("InstanceVersionName")
        self.InstanceVersionKey = params.get("InstanceVersionKey")
        self.Qps = params.get("Qps")
        self.MaxInstances = params.get("MaxInstances")
        self.InsertSpeed = params.get("InsertSpeed")
        self.OnlineStorageCapacity = params.get("OnlineStorageCapacity")
        self.ArchivingStorageCapacity = params.get("ArchivingStorageCapacity")


class DescribeDbauditInstanceTypeRequest(AbstractModel):
    """DescribeDbauditInstanceType請求參數結構體

    """


class DescribeDbauditInstanceTypeResponse(AbstractModel):
    """DescribeDbauditInstanceType返回參數結構體

    """

    def __init__(self):
        """
        :param DbauditTypesSet: 數據安全審計産品規格訊息清單
        :type DbauditTypesSet: list of DbauditTypesInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DbauditTypesSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DbauditTypesSet") is not None:
            self.DbauditTypesSet = []
            for item in params.get("DbauditTypesSet"):
                obj = DbauditTypesInfo()
                obj._deserialize(item)
                self.DbauditTypesSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDbauditInstancesRequest(AbstractModel):
    """DescribeDbauditInstances請求參數結構體

    """

    def __init__(self):
        """
        :param SearchRegion: 查詢條件地域
        :type SearchRegion: str
        :param Limit: 限制數目，預設10， 最大50
        :type Limit: int
        :param Offset: 偏移量，預設1
        :type Offset: int
        """
        self.SearchRegion = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.SearchRegion = params.get("SearchRegion")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeDbauditInstancesResponse(AbstractModel):
    """DescribeDbauditInstances返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 總實例數
        :type TotalCount: int
        :param CdsAuditInstanceSet: 數據安全審計實例訊息清單
        :type CdsAuditInstanceSet: list of CdsAuditInstance
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.CdsAuditInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("CdsAuditInstanceSet") is not None:
            self.CdsAuditInstanceSet = []
            for item in params.get("CdsAuditInstanceSet"):
                obj = CdsAuditInstance()
                obj._deserialize(item)
                self.CdsAuditInstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDbauditUsedRegionsRequest(AbstractModel):
    """DescribeDbauditUsedRegions請求參數結構體

    """


class DescribeDbauditUsedRegionsResponse(AbstractModel):
    """DescribeDbauditUsedRegions返回參數結構體

    """

    def __init__(self):
        """
        :param RegionSet: 可售賣地域訊息清單
        :type RegionSet: list of RegionInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionSet") is not None:
            self.RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.RegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class InquiryPriceDbauditInstanceRequest(AbstractModel):
    """InquiryPriceDbauditInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceVersion: 實例規格，取值範圍： cdsaudit，cdsaudit_adv， cdsaudit_ent 分别爲合規版，高級版，企業版
        :type InstanceVersion: str
        :param InquiryType: 詢價類型： renew，續約；newbuy，新購
        :type InquiryType: str
        :param TimeSpan: 購買實例的時長。取值範圍：1（y/m），2（y/m）,，3（y/m），4（m）， 5（m），6（m）， 7（m），8（m），9（m）， 10（m）
        :type TimeSpan: int
        :param TimeUnit: 購買時長單位，y：年；m：月
        :type TimeUnit: str
        :param ServiceRegion: 實例所在地域
        :type ServiceRegion: str
        """
        self.InstanceVersion = None
        self.InquiryType = None
        self.TimeSpan = None
        self.TimeUnit = None
        self.ServiceRegion = None


    def _deserialize(self, params):
        self.InstanceVersion = params.get("InstanceVersion")
        self.InquiryType = params.get("InquiryType")
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnit = params.get("TimeUnit")
        self.ServiceRegion = params.get("ServiceRegion")


class InquiryPriceDbauditInstanceResponse(AbstractModel):
    """InquiryPriceDbauditInstance返回參數結構體

    """

    def __init__(self):
        """
        :param TotalPrice: 總價，單位：元
        :type TotalPrice: float
        :param RealTotalCost: 真實價錢，預支費用的折扣價，單位：元
        :type RealTotalCost: float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalPrice = None
        self.RealTotalCost = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalPrice = params.get("TotalPrice")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RequestId = params.get("RequestId")


class ModifyDbauditInstancesRenewFlagRequest(AbstractModel):
    """ModifyDbauditInstancesRenewFlag請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param AutoRenewFlag: 0，表示預設狀态(用戶未設置，即初始狀态)；1，表示自動續約；2，表示明确不自動續約
        :type AutoRenewFlag: int
        """
        self.InstanceId = None
        self.AutoRenewFlag = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AutoRenewFlag = params.get("AutoRenewFlag")


class ModifyDbauditInstancesRenewFlagResponse(AbstractModel):
    """ModifyDbauditInstancesRenewFlag返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """數盾地域訊息

    """

    def __init__(self):
        """
        :param RegionId: 地域ID
        :type RegionId: int
        :param Region: 地域名稱
        :type Region: str
        :param RegionName: 地域描述
        :type RegionName: str
        :param RegionState: 地域可用狀态
        :type RegionState: int
        """
        self.RegionId = None
        self.Region = None
        self.RegionName = None
        self.RegionState = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionState = params.get("RegionState")