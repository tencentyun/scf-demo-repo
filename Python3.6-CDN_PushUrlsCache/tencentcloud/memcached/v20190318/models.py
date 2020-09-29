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


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 實例ID組成的數組，數組下標從0開始
        :type InstanceIds: list of str
        :param InstanceNames: 實例名稱組成的數組，數組下標從0開始
        :type InstanceNames: list of str
        :param Limit: 實例清單的大小，參數預設值100
        :type Limit: int
        :param Offset: 偏移量，取Limit整數倍
        :type Offset: int
        :param OrderBy: 列舉範圍： AddTimeStamp, InstanceName, ProjectId
        :type OrderBy: str
        :param OrderType: 0倒序，1正序，預設倒序
        :type OrderType: int
        :param ProjectIds: 項目ID組成的數組，數組下標從0開始
        :type ProjectIds: list of int
        :param SearchKeys: 搜索關鍵詞：支援實例ID、實例名稱、完整IP
        :type SearchKeys: list of str
        :param UniqSubnetIds: 子網ID數組，數組下標從0開始，如：subnet-fdj24n34j2
        :type UniqSubnetIds: list of str
        :param UniqVpcIds: 私有網絡ID數組，數組下標從0開始，如果不傳則預設選擇基礎網絡，如：vpc-sad23jfdfk
        :type UniqVpcIds: list of str
        :param Vips: 實例服務IP組成的數組，數組下標從0開始
        :type Vips: list of str
        """
        self.InstanceIds = None
        self.InstanceNames = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderType = None
        self.ProjectIds = None
        self.SearchKeys = None
        self.UniqSubnetIds = None
        self.UniqVpcIds = None
        self.Vips = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceNames = params.get("InstanceNames")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.ProjectIds = params.get("ProjectIds")
        self.SearchKeys = params.get("SearchKeys")
        self.UniqSubnetIds = params.get("UniqSubnetIds")
        self.UniqVpcIds = params.get("UniqVpcIds")
        self.Vips = params.get("Vips")


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceList: 實例詳細訊息清單
        :type InstanceList: list of InstanceListInfo
        :param TotalNum: 實例數量
        :type TotalNum: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceList = None
        self.TotalNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = InstanceListInfo()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.RequestId = params.get("RequestId")


class InstanceListInfo(AbstractModel):
    """實例詳細訊息清單

    """

    def __init__(self):
        """
        :param Tags: 實例關聯的標簽訊息
        :type Tags: list of TagInfo
        :param AddTimeStamp: 實例創建時間
        :type AddTimeStamp: str
        :param AppId: 用戶AppID
        :type AppId: int
        :param AutoRenewFlag: 實例是否設置自動續約標識，1：設置自動續約；0：未設置自動續約
        :type AutoRenewFlag: int
        :param CmemId: 實例内置ID
        :type CmemId: int
        :param DeadlineTimeStamp: 實例截止時間
        :type DeadlineTimeStamp: str
        :param Expire: 過期策略
        :type Expire: int
        :param InstanceDesc: 實例描述訊息
        :type InstanceDesc: str
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param InstanceName: 實例名稱
        :type InstanceName: str
        :param IsolateTimeStamp: 實例隔離時間
        :type IsolateTimeStamp: str
        :param ModTimeStamp: 實例修改時間
        :type ModTimeStamp: str
        :param PayMode: 計費模式：0-按量計費，1-包年包月
        :type PayMode: int
        :param ProjectId: 項目ID
        :type ProjectId: int
        :param RegionId: 地域id 1--  4--  5--   6--多倫多 7-- 金融 8--  9-- 新加坡 11-- 金融 15--美西（矽谷）16--  17--德國 18--韓國 19--  21--印度 22--美東（弗吉尼亞）23--泰國 24--俄羅斯 25--日本
        :type RegionId: int
        :param SetId: 倉庫ID
        :type SetId: int
        :param Status: 實例當前狀态，0：待初始化；1：實例在流程中；2：實例運作中；-2：實例已隔離；-3：實例待删除
        :type Status: int
        :param SubnetId: vpc網絡下子網id 如：46315
        :type SubnetId: int
        :param UniqSubnetId: vpc網絡下子網id 如：subnet-fd3j6l35mm0
        :type UniqSubnetId: str
        :param UniqVpcId: vpc網絡id 如：vpc-fk33jsf43kgv
        :type UniqVpcId: str
        :param Vip: 實例vip
        :type Vip: str
        :param VpcId: vpc網絡id 如：75101
        :type VpcId: int
        :param Vport: 實例端口號
        :type Vport: int
        :param ZoneId: 區域ID
        :type ZoneId: int
        """
        self.Tags = None
        self.AddTimeStamp = None
        self.AppId = None
        self.AutoRenewFlag = None
        self.CmemId = None
        self.DeadlineTimeStamp = None
        self.Expire = None
        self.InstanceDesc = None
        self.InstanceId = None
        self.InstanceName = None
        self.IsolateTimeStamp = None
        self.ModTimeStamp = None
        self.PayMode = None
        self.ProjectId = None
        self.RegionId = None
        self.SetId = None
        self.Status = None
        self.SubnetId = None
        self.UniqSubnetId = None
        self.UniqVpcId = None
        self.Vip = None
        self.VpcId = None
        self.Vport = None
        self.ZoneId = None


    def _deserialize(self, params):
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AddTimeStamp = params.get("AddTimeStamp")
        self.AppId = params.get("AppId")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.CmemId = params.get("CmemId")
        self.DeadlineTimeStamp = params.get("DeadlineTimeStamp")
        self.Expire = params.get("Expire")
        self.InstanceDesc = params.get("InstanceDesc")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.IsolateTimeStamp = params.get("IsolateTimeStamp")
        self.ModTimeStamp = params.get("ModTimeStamp")
        self.PayMode = params.get("PayMode")
        self.ProjectId = params.get("ProjectId")
        self.RegionId = params.get("RegionId")
        self.SetId = params.get("SetId")
        self.Status = params.get("Status")
        self.SubnetId = params.get("SubnetId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.UniqVpcId = params.get("UniqVpcId")
        self.Vip = params.get("Vip")
        self.VpcId = params.get("VpcId")
        self.Vport = params.get("Vport")
        self.ZoneId = params.get("ZoneId")


class TagInfo(AbstractModel):
    """標簽訊息

    """

    def __init__(self):
        """
        :param TagKey: 標簽鍵
        :type TagKey: str
        :param TagValue: 標簽值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")