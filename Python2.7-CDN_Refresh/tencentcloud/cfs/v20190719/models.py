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


class AvailableProtoStatus(AbstractModel):
    """版本控制-協議詳情

    """

    def __init__(self):
        """
        :param SaleStatus: 售賣狀态。可選值有 sale_out 售罄、saling可售、no_saling不可銷售
        :type SaleStatus: str
        :param Protocol: 協議類型。可選值有 NFS、CIFS
        :type Protocol: str
        """
        self.SaleStatus = None
        self.Protocol = None


    def _deserialize(self, params):
        self.SaleStatus = params.get("SaleStatus")
        self.Protocol = params.get("Protocol")


class AvailableRegion(AbstractModel):
    """版本控制-區域數組

    """

    def __init__(self):
        """
        :param Region: 區域名稱，如“ap-beijing”
        :type Region: str
        :param RegionName: 區域名稱，如“bj”
        :type RegionName: str
        :param RegionStatus: 區域可用情況，當區域内至少有一個可用區處于可售狀态時，取值爲AVAILABLE，否則爲UNAVAILABLE
        :type RegionStatus: str
        :param Zones: 可用區數組
        :type Zones: list of AvailableZone
        :param RegionCnName: 區域中文名稱，如“ ”
        :type RegionCnName: str
        """
        self.Region = None
        self.RegionName = None
        self.RegionStatus = None
        self.Zones = None
        self.RegionCnName = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionStatus = params.get("RegionStatus")
        if params.get("Zones") is not None:
            self.Zones = []
            for item in params.get("Zones"):
                obj = AvailableZone()
                obj._deserialize(item)
                self.Zones.append(obj)
        self.RegionCnName = params.get("RegionCnName")


class AvailableType(AbstractModel):
    """版本控制-類型數組

    """

    def __init__(self):
        """
        :param Protocols: 協議與售賣詳情
        :type Protocols: list of AvailableProtoStatus
        :param Type: 儲存類型。可選值有 SD 标準型儲存、HP效能型儲存
        :type Type: str
        """
        self.Protocols = None
        self.Type = None


    def _deserialize(self, params):
        if params.get("Protocols") is not None:
            self.Protocols = []
            for item in params.get("Protocols"):
                obj = AvailableProtoStatus()
                obj._deserialize(item)
                self.Protocols.append(obj)
        self.Type = params.get("Type")


class AvailableZone(AbstractModel):
    """版本控制-可用區數組

    """

    def __init__(self):
        """
        :param Zone: 可用區名稱
        :type Zone: str
        :param ZoneId: 可用區ID
        :type ZoneId: int
        :param ZoneCnName: 可用區中文名稱
        :type ZoneCnName: str
        :param Types: Type數組
        :type Types: list of AvailableType
        :param ZoneName: 可用區中英文名稱
        :type ZoneName: str
        """
        self.Zone = None
        self.ZoneId = None
        self.ZoneCnName = None
        self.Types = None
        self.ZoneName = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneId = params.get("ZoneId")
        self.ZoneCnName = params.get("ZoneCnName")
        if params.get("Types") is not None:
            self.Types = []
            for item in params.get("Types"):
                obj = AvailableType()
                obj._deserialize(item)
                self.Types.append(obj)
        self.ZoneName = params.get("ZoneName")


class CreateCfsFileSystemRequest(AbstractModel):
    """CreateCfsFileSystem請求參數結構體

    """

    def __init__(self):
        """
        :param Zone: 可用區名稱，例如ap-beijing-1，請參考 [概覽](https://cloud.taifucloud.com/document/product/582/13225) 文件中的地域與可用區清單
        :type Zone: str
        :param NetInterface: 網絡類型，值爲 VPC，BASIC；其中 VPC 爲私有網絡，BASIC 爲基礎網絡
        :type NetInterface: str
        :param PGroupId: 權限組 ID
        :type PGroupId: str
        :param Protocol: 文件系統協議類型， 值爲 NFS、CIFS; 若留空則預設爲 NFS協議
        :type Protocol: str
        :param StorageType: 文件系統儲存類型，值爲 SD ；其中 SD 爲标準型儲存， HP爲效能儲存。
        :type StorageType: str
        :param VpcId: 私有網絡（VPC） ID，若網絡類型選擇的是VPC，該欄位爲必填。
        :type VpcId: str
        :param SubnetId: 子網 ID，若網絡類型選擇的是VPC，該欄位爲必填。
        :type SubnetId: str
        :param MountIP: 指定IP網址，僅VPC網絡支援；若不填寫、将在該子網下随機分配 IP
        :type MountIP: str
        :param FsName: 用戶自定義文件系統名稱
        :type FsName: str
        :param ResourceTags: 文件系統标簽
        :type ResourceTags: list of TagInfo
        """
        self.Zone = None
        self.NetInterface = None
        self.PGroupId = None
        self.Protocol = None
        self.StorageType = None
        self.VpcId = None
        self.SubnetId = None
        self.MountIP = None
        self.FsName = None
        self.ResourceTags = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.NetInterface = params.get("NetInterface")
        self.PGroupId = params.get("PGroupId")
        self.Protocol = params.get("Protocol")
        self.StorageType = params.get("StorageType")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.MountIP = params.get("MountIP")
        self.FsName = params.get("FsName")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.ResourceTags.append(obj)


class CreateCfsFileSystemResponse(AbstractModel):
    """CreateCfsFileSystem返回參數結構體

    """

    def __init__(self):
        """
        :param CreationTime: 文件系統創建時間
        :type CreationTime: str
        :param CreationToken: 用戶自定義文件系統名稱
        :type CreationToken: str
        :param FileSystemId: 文件系統 ID
        :type FileSystemId: str
        :param LifeCycleState: 文件系統狀态
        :type LifeCycleState: str
        :param SizeByte: 文件系統已使用容量大小
        :type SizeByte: int
        :param ZoneId: 可用區 ID
        :type ZoneId: int
        :param FsName: 用戶自定義文件系統名稱
        :type FsName: str
        :param Encrypted: 文件系統是否加密
        :type Encrypted: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CreationTime = None
        self.CreationToken = None
        self.FileSystemId = None
        self.LifeCycleState = None
        self.SizeByte = None
        self.ZoneId = None
        self.FsName = None
        self.Encrypted = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CreationTime = params.get("CreationTime")
        self.CreationToken = params.get("CreationToken")
        self.FileSystemId = params.get("FileSystemId")
        self.LifeCycleState = params.get("LifeCycleState")
        self.SizeByte = params.get("SizeByte")
        self.ZoneId = params.get("ZoneId")
        self.FsName = params.get("FsName")
        self.Encrypted = params.get("Encrypted")
        self.RequestId = params.get("RequestId")


class CreateCfsPGroupRequest(AbstractModel):
    """CreateCfsPGroup請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 權限組名稱，1-64個字元且只能爲中文，字母，數字，下劃線或橫線
        :type Name: str
        :param DescInfo: 權限組描述訊息，1-255個字元
        :type DescInfo: str
        """
        self.Name = None
        self.DescInfo = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.DescInfo = params.get("DescInfo")


class CreateCfsPGroupResponse(AbstractModel):
    """CreateCfsPGroup返回參數結構體

    """

    def __init__(self):
        """
        :param PGroupId: 權限組 ID
        :type PGroupId: str
        :param Name: 權限組名字
        :type Name: str
        :param DescInfo: 權限組描述訊息
        :type DescInfo: str
        :param BindCfsNum: 已經與該權限組綁定的文件系統個數
        :type BindCfsNum: int
        :param CDate: 權限組創建時間
        :type CDate: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PGroupId = None
        self.Name = None
        self.DescInfo = None
        self.BindCfsNum = None
        self.CDate = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.Name = params.get("Name")
        self.DescInfo = params.get("DescInfo")
        self.BindCfsNum = params.get("BindCfsNum")
        self.CDate = params.get("CDate")
        self.RequestId = params.get("RequestId")


class CreateCfsRuleRequest(AbstractModel):
    """CreateCfsRule請求參數結構體

    """

    def __init__(self):
        """
        :param PGroupId: 權限組 ID
        :type PGroupId: str
        :param AuthClientIp: 可以填寫單個 IP 或者單個網段，例如 10.1.10.11 或者 10.10.1.0/24。預設來訪網址爲*表示允許所有。同時需要注意，此處需填寫 CVM 的内網 IP。
        :type AuthClientIp: str
        :param Priority: 規則優先級，參數範圍1-100。 其中 1 爲最高，100爲最低
        :type Priority: int
        :param RWPermission: 讀寫權限, 值爲 RO、RW；其中 RO 爲只讀，RW 爲讀寫，不填預設爲只讀
        :type RWPermission: str
        :param UserPermission: 用戶權限，值爲 all_squash、no_all_squash、root_squash、no_root_squash。其中all_squash爲所有訪問用戶都會被映射爲匿名用戶或用戶組；no_all_squash爲訪問用戶會先與本機用戶比對，比對失敗後再映射爲匿名用戶或用戶組；root_squash爲将來訪的root用戶映射爲匿名用戶或用戶組；no_root_squash爲來訪的root用戶保持root帳号權限。不填預設爲root_squash。
        :type UserPermission: str
        """
        self.PGroupId = None
        self.AuthClientIp = None
        self.Priority = None
        self.RWPermission = None
        self.UserPermission = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.AuthClientIp = params.get("AuthClientIp")
        self.Priority = params.get("Priority")
        self.RWPermission = params.get("RWPermission")
        self.UserPermission = params.get("UserPermission")


class CreateCfsRuleResponse(AbstractModel):
    """CreateCfsRule返回參數結構體

    """

    def __init__(self):
        """
        :param RuleId: 規則 ID
        :type RuleId: str
        :param PGroupId: 權限組 ID
        :type PGroupId: str
        :param AuthClientIp: 用戶端 IP
        :type AuthClientIp: str
        :param RWPermission: 讀寫權限
        :type RWPermission: str
        :param UserPermission: 用戶權限
        :type UserPermission: str
        :param Priority: 優先級
        :type Priority: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RuleId = None
        self.PGroupId = None
        self.AuthClientIp = None
        self.RWPermission = None
        self.UserPermission = None
        self.Priority = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.PGroupId = params.get("PGroupId")
        self.AuthClientIp = params.get("AuthClientIp")
        self.RWPermission = params.get("RWPermission")
        self.UserPermission = params.get("UserPermission")
        self.Priority = params.get("Priority")
        self.RequestId = params.get("RequestId")


class DeleteCfsFileSystemRequest(AbstractModel):
    """DeleteCfsFileSystem請求參數結構體

    """

    def __init__(self):
        """
        :param FileSystemId: 文件系統 ID。說明，進行删除文件系統操作前需要先調用 DeleteMountTarget 介面删除該文件系統的掛載點，否則會删除失敗。
        :type FileSystemId: str
        """
        self.FileSystemId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")


class DeleteCfsFileSystemResponse(AbstractModel):
    """DeleteCfsFileSystem返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCfsPGroupRequest(AbstractModel):
    """DeleteCfsPGroup請求參數結構體

    """

    def __init__(self):
        """
        :param PGroupId: 權限組 ID
        :type PGroupId: str
        """
        self.PGroupId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")


class DeleteCfsPGroupResponse(AbstractModel):
    """DeleteCfsPGroup返回參數結構體

    """

    def __init__(self):
        """
        :param PGroupId: 權限組 ID
        :type PGroupId: str
        :param AppId: 用戶 ID
        :type AppId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PGroupId = None
        self.AppId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.AppId = params.get("AppId")
        self.RequestId = params.get("RequestId")


class DeleteCfsRuleRequest(AbstractModel):
    """DeleteCfsRule請求參數結構體

    """

    def __init__(self):
        """
        :param PGroupId: 權限組 ID
        :type PGroupId: str
        :param RuleId: 規則 ID
        :type RuleId: str
        """
        self.PGroupId = None
        self.RuleId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.RuleId = params.get("RuleId")


class DeleteCfsRuleResponse(AbstractModel):
    """DeleteCfsRule返回參數結構體

    """

    def __init__(self):
        """
        :param RuleId: 規則 ID
        :type RuleId: str
        :param PGroupId: 權限組 ID
        :type PGroupId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RuleId = None
        self.PGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.PGroupId = params.get("PGroupId")
        self.RequestId = params.get("RequestId")


class DeleteMountTargetRequest(AbstractModel):
    """DeleteMountTarget請求參數結構體

    """

    def __init__(self):
        """
        :param FileSystemId: 文件系統 ID
        :type FileSystemId: str
        :param MountTargetId: 掛載點 ID
        :type MountTargetId: str
        """
        self.FileSystemId = None
        self.MountTargetId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        self.MountTargetId = params.get("MountTargetId")


class DeleteMountTargetResponse(AbstractModel):
    """DeleteMountTarget返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAvailableZoneInfoRequest(AbstractModel):
    """DescribeAvailableZoneInfo請求參數結構體

    """


class DescribeAvailableZoneInfoResponse(AbstractModel):
    """DescribeAvailableZoneInfo返回參數結構體

    """

    def __init__(self):
        """
        :param RegionZones: 各可用區的資源售賣情況以及支援的儲存類型、儲存協議等訊息
        :type RegionZones: list of AvailableRegion
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RegionZones = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionZones") is not None:
            self.RegionZones = []
            for item in params.get("RegionZones"):
                obj = AvailableRegion()
                obj._deserialize(item)
                self.RegionZones.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCfsFileSystemsRequest(AbstractModel):
    """DescribeCfsFileSystems請求參數結構體

    """

    def __init__(self):
        """
        :param FileSystemId: 文件系統 ID
        :type FileSystemId: str
        :param VpcId: 私有網絡（VPC） ID
        :type VpcId: str
        :param SubnetId: 子網 ID
        :type SubnetId: str
        """
        self.FileSystemId = None
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")


class DescribeCfsFileSystemsResponse(AbstractModel):
    """DescribeCfsFileSystems返回參數結構體

    """

    def __init__(self):
        """
        :param FileSystems: 文件系統訊息
        :type FileSystems: list of FileSystemInfo
        :param TotalCount: 文件系統總數
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FileSystems = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FileSystems") is not None:
            self.FileSystems = []
            for item in params.get("FileSystems"):
                obj = FileSystemInfo()
                obj._deserialize(item)
                self.FileSystems.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCfsPGroupsRequest(AbstractModel):
    """DescribeCfsPGroups請求參數結構體

    """


class DescribeCfsPGroupsResponse(AbstractModel):
    """DescribeCfsPGroups返回參數結構體

    """

    def __init__(self):
        """
        :param PGroupList: 權限組訊息清單
        :type PGroupList: list of PGroupInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PGroupList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PGroupList") is not None:
            self.PGroupList = []
            for item in params.get("PGroupList"):
                obj = PGroupInfo()
                obj._deserialize(item)
                self.PGroupList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCfsRulesRequest(AbstractModel):
    """DescribeCfsRules請求參數結構體

    """

    def __init__(self):
        """
        :param PGroupId: 權限組 ID
        :type PGroupId: str
        """
        self.PGroupId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")


class DescribeCfsRulesResponse(AbstractModel):
    """DescribeCfsRules返回參數結構體

    """

    def __init__(self):
        """
        :param RuleList: 權限組規則清單
        :type RuleList: list of PGroupRuleInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RuleList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RuleList") is not None:
            self.RuleList = []
            for item in params.get("RuleList"):
                obj = PGroupRuleInfo()
                obj._deserialize(item)
                self.RuleList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCfsServiceStatusRequest(AbstractModel):
    """DescribeCfsServiceStatus請求參數結構體

    """


class DescribeCfsServiceStatusResponse(AbstractModel):
    """DescribeCfsServiceStatus返回參數結構體

    """

    def __init__(self):
        """
        :param CfsServiceStatus: 該用戶當前 CFS 服務的狀态，none 爲未開通，creating 爲開通中，created 爲已開通
        :type CfsServiceStatus: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CfsServiceStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CfsServiceStatus = params.get("CfsServiceStatus")
        self.RequestId = params.get("RequestId")


class DescribeMountTargetsRequest(AbstractModel):
    """DescribeMountTargets請求參數結構體

    """

    def __init__(self):
        """
        :param FileSystemId: 文件系統 ID
        :type FileSystemId: str
        """
        self.FileSystemId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")


class DescribeMountTargetsResponse(AbstractModel):
    """DescribeMountTargets返回參數結構體

    """

    def __init__(self):
        """
        :param MountTargets: 掛載點詳情
        :type MountTargets: list of MountInfo
        :param NumberOfMountTargets: 掛載點數量
        :type NumberOfMountTargets: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.MountTargets = None
        self.NumberOfMountTargets = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MountTargets") is not None:
            self.MountTargets = []
            for item in params.get("MountTargets"):
                obj = MountInfo()
                obj._deserialize(item)
                self.MountTargets.append(obj)
        self.NumberOfMountTargets = params.get("NumberOfMountTargets")
        self.RequestId = params.get("RequestId")


class FileSystemInfo(AbstractModel):
    """文件系統基本訊息

    """

    def __init__(self):
        """
        :param CreationTime: 創建時間
        :type CreationTime: str
        :param CreationToken: 用戶自定義名稱
        :type CreationToken: str
        :param FileSystemId: 文件系統 ID
        :type FileSystemId: str
        :param LifeCycleState: 文件系統狀态
        :type LifeCycleState: str
        :param SizeByte: 文件系統已使用容量
        :type SizeByte: int
        :param SizeLimit: 文件系統最大空間限制
        :type SizeLimit: int
        :param ZoneId: 區域 ID
        :type ZoneId: int
        :param Zone: 區域名稱
        :type Zone: str
        :param Protocol: 文件系統協議類型
        :type Protocol: str
        :param StorageType: 文件系統儲存類型
        :type StorageType: str
        :param StorageResourcePkg: 文件系統綁定的預付費儲存包（暫未支援）
        :type StorageResourcePkg: str
        :param BandwidthResourcePkg: 文件系統綁定的預付費頻寬包（暫未支援）
        :type BandwidthResourcePkg: str
        :param PGroup: 文件系統綁定權限組訊息
        :type PGroup: :class:`taifucloudcloud.cfs.v20190719.models.PGroup`
        :param FsName: 用戶自定義名稱
        :type FsName: str
        :param Encrypted: 文件系統是否加密
        :type Encrypted: bool
        :param KmsKeyId: 加密所使用的金鑰，可以爲金鑰的 ID 或者 ARN
        :type KmsKeyId: str
        :param AppId: 應用ID
        :type AppId: int
        """
        self.CreationTime = None
        self.CreationToken = None
        self.FileSystemId = None
        self.LifeCycleState = None
        self.SizeByte = None
        self.SizeLimit = None
        self.ZoneId = None
        self.Zone = None
        self.Protocol = None
        self.StorageType = None
        self.StorageResourcePkg = None
        self.BandwidthResourcePkg = None
        self.PGroup = None
        self.FsName = None
        self.Encrypted = None
        self.KmsKeyId = None
        self.AppId = None


    def _deserialize(self, params):
        self.CreationTime = params.get("CreationTime")
        self.CreationToken = params.get("CreationToken")
        self.FileSystemId = params.get("FileSystemId")
        self.LifeCycleState = params.get("LifeCycleState")
        self.SizeByte = params.get("SizeByte")
        self.SizeLimit = params.get("SizeLimit")
        self.ZoneId = params.get("ZoneId")
        self.Zone = params.get("Zone")
        self.Protocol = params.get("Protocol")
        self.StorageType = params.get("StorageType")
        self.StorageResourcePkg = params.get("StorageResourcePkg")
        self.BandwidthResourcePkg = params.get("BandwidthResourcePkg")
        if params.get("PGroup") is not None:
            self.PGroup = PGroup()
            self.PGroup._deserialize(params.get("PGroup"))
        self.FsName = params.get("FsName")
        self.Encrypted = params.get("Encrypted")
        self.KmsKeyId = params.get("KmsKeyId")
        self.AppId = params.get("AppId")


class MountInfo(AbstractModel):
    """掛載點訊息

    """

    def __init__(self):
        """
        :param FileSystemId: 文件系統 ID
        :type FileSystemId: str
        :param MountTargetId: 掛載點 ID
        :type MountTargetId: str
        :param IpAddress: 掛載點 IP
        :type IpAddress: str
        :param FSID: 掛載根目錄
        :type FSID: str
        :param LifeCycleState: 掛載點狀态
        :type LifeCycleState: str
        :param NetworkInterface: 網絡類型
        :type NetworkInterface: str
        :param VpcId: 私有網絡 ID
        :type VpcId: str
        :param VpcName: 私有網絡名稱
        :type VpcName: str
        :param SubnetId: 子網 Id
        :type SubnetId: str
        :param SubnetName: 子網名稱
        :type SubnetName: str
        """
        self.FileSystemId = None
        self.MountTargetId = None
        self.IpAddress = None
        self.FSID = None
        self.LifeCycleState = None
        self.NetworkInterface = None
        self.VpcId = None
        self.VpcName = None
        self.SubnetId = None
        self.SubnetName = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        self.MountTargetId = params.get("MountTargetId")
        self.IpAddress = params.get("IpAddress")
        self.FSID = params.get("FSID")
        self.LifeCycleState = params.get("LifeCycleState")
        self.NetworkInterface = params.get("NetworkInterface")
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")


class PGroup(AbstractModel):
    """文件系統綁定權限組訊息

    """

    def __init__(self):
        """
        :param PGroupId: 權限組ID
        :type PGroupId: str
        :param Name: 權限組名稱
        :type Name: str
        """
        self.PGroupId = None
        self.Name = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.Name = params.get("Name")


class PGroupInfo(AbstractModel):
    """權限組數組

    """

    def __init__(self):
        """
        :param PGroupId: 權限組ID
        :type PGroupId: str
        :param Name: 權限組名稱
        :type Name: str
        :param DescInfo: 描述訊息
        :type DescInfo: str
        :param CDate: 創建時間
        :type CDate: str
        :param BindCfsNum: 關聯文件系統個數
        :type BindCfsNum: int
        """
        self.PGroupId = None
        self.Name = None
        self.DescInfo = None
        self.CDate = None
        self.BindCfsNum = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.Name = params.get("Name")
        self.DescInfo = params.get("DescInfo")
        self.CDate = params.get("CDate")
        self.BindCfsNum = params.get("BindCfsNum")


class PGroupRuleInfo(AbstractModel):
    """權限組規則清單

    """

    def __init__(self):
        """
        :param RuleId: 規則ID
        :type RuleId: str
        :param AuthClientIp: 允許訪問的用戶端IP
        :type AuthClientIp: str
        :param RWPermission: 讀寫權限, ro爲只讀，rw爲讀寫
        :type RWPermission: str
        :param UserPermission: 用戶權限。其中all_squash爲所有訪問用戶都會被映射爲匿名用戶或用戶組；no_all_squash爲訪問用戶會先與本機用戶比對，比對失敗後再映射爲匿名用戶或用戶組；root_squash爲将來訪的root用戶映射爲匿名用戶或用戶組；no_root_squash爲來訪的root用戶保持root帳号權限。
        :type UserPermission: str
        :param Priority: 規則優先級，1-100。 其中 1 爲最高，100爲最低
        :type Priority: int
        """
        self.RuleId = None
        self.AuthClientIp = None
        self.RWPermission = None
        self.UserPermission = None
        self.Priority = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.AuthClientIp = params.get("AuthClientIp")
        self.RWPermission = params.get("RWPermission")
        self.UserPermission = params.get("UserPermission")
        self.Priority = params.get("Priority")


class SignUpCfsServiceRequest(AbstractModel):
    """SignUpCfsService請求參數結構體

    """


class SignUpCfsServiceResponse(AbstractModel):
    """SignUpCfsService返回參數結構體

    """

    def __init__(self):
        """
        :param CfsServiceStatus: 該用戶當前 CFS 服務的狀态，none 是未開通，creating 是開通中，created 是已開通
        :type CfsServiceStatus: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CfsServiceStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CfsServiceStatus = params.get("CfsServiceStatus")
        self.RequestId = params.get("RequestId")


class TagInfo(AbstractModel):
    """Tag訊息單元

    """

    def __init__(self):
        """
        :param TagKey: 标簽鍵
        :type TagKey: str
        :param TagValue: 标簽值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class UpdateCfsFileSystemNameRequest(AbstractModel):
    """UpdateCfsFileSystemName請求參數結構體

    """

    def __init__(self):
        """
        :param FileSystemId: 文件系統 ID
        :type FileSystemId: str
        :param FsName: 用戶自定義文件系統名稱
        :type FsName: str
        """
        self.FileSystemId = None
        self.FsName = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        self.FsName = params.get("FsName")


class UpdateCfsFileSystemNameResponse(AbstractModel):
    """UpdateCfsFileSystemName返回參數結構體

    """

    def __init__(self):
        """
        :param CreationToken: 用戶自定義文件系統名稱
        :type CreationToken: str
        :param FileSystemId: 文件系統ID
        :type FileSystemId: str
        :param FsName: 用戶自定義文件系統名稱
        :type FsName: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CreationToken = None
        self.FileSystemId = None
        self.FsName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CreationToken = params.get("CreationToken")
        self.FileSystemId = params.get("FileSystemId")
        self.FsName = params.get("FsName")
        self.RequestId = params.get("RequestId")


class UpdateCfsFileSystemPGroupRequest(AbstractModel):
    """UpdateCfsFileSystemPGroup請求參數結構體

    """

    def __init__(self):
        """
        :param PGroupId: 權限組 ID
        :type PGroupId: str
        :param FileSystemId: 文件系統 ID
        :type FileSystemId: str
        """
        self.PGroupId = None
        self.FileSystemId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.FileSystemId = params.get("FileSystemId")


class UpdateCfsFileSystemPGroupResponse(AbstractModel):
    """UpdateCfsFileSystemPGroup返回參數結構體

    """

    def __init__(self):
        """
        :param PGroupId: 權限組 ID
        :type PGroupId: str
        :param FileSystemId: 文件系統 ID
        :type FileSystemId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PGroupId = None
        self.FileSystemId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.FileSystemId = params.get("FileSystemId")
        self.RequestId = params.get("RequestId")


class UpdateCfsFileSystemSizeLimitRequest(AbstractModel):
    """UpdateCfsFileSystemSizeLimit請求參數結構體

    """

    def __init__(self):
        """
        :param FsLimit: 文件系統容量限制大小，輸入範圍0-1073741824, 單位爲GB；其中輸入值爲0時，表示不限制文件系統容量。
        :type FsLimit: int
        :param FileSystemId: 文件系統ID
        :type FileSystemId: str
        """
        self.FsLimit = None
        self.FileSystemId = None


    def _deserialize(self, params):
        self.FsLimit = params.get("FsLimit")
        self.FileSystemId = params.get("FileSystemId")


class UpdateCfsFileSystemSizeLimitResponse(AbstractModel):
    """UpdateCfsFileSystemSizeLimit返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateCfsPGroupRequest(AbstractModel):
    """UpdateCfsPGroup請求參數結構體

    """

    def __init__(self):
        """
        :param PGroupId: 權限組 ID
        :type PGroupId: str
        :param Name: 權限組名稱，1-64個字元且只能爲中文，字母，數字，下劃線或橫線
        :type Name: str
        :param DescInfo: 權限組描述訊息，1-255個字元
        :type DescInfo: str
        """
        self.PGroupId = None
        self.Name = None
        self.DescInfo = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.Name = params.get("Name")
        self.DescInfo = params.get("DescInfo")


class UpdateCfsPGroupResponse(AbstractModel):
    """UpdateCfsPGroup返回參數結構體

    """

    def __init__(self):
        """
        :param PGroupId: 權限組ID
        :type PGroupId: str
        :param Name: 權限組名稱
        :type Name: str
        :param DescInfo: 描述訊息
        :type DescInfo: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PGroupId = None
        self.Name = None
        self.DescInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.Name = params.get("Name")
        self.DescInfo = params.get("DescInfo")
        self.RequestId = params.get("RequestId")


class UpdateCfsRuleRequest(AbstractModel):
    """UpdateCfsRule請求參數結構體

    """

    def __init__(self):
        """
        :param PGroupId: 權限組 ID
        :type PGroupId: str
        :param RuleId: 規則 ID
        :type RuleId: str
        :param AuthClientIp: 可以填寫單個 IP 或者單個網段，例如 10.1.10.11 或者 10.10.1.0/24。預設來訪網址爲*表示允許所有。同時需要注意，此處需填寫 CVM 的内網 IP。
        :type AuthClientIp: str
        :param RWPermission: 讀寫權限, 值爲RO、RW；其中 RO 爲只讀，RW 爲讀寫，不填預設爲只讀
        :type RWPermission: str
        :param UserPermission: 用戶權限，值爲all_squash、no_all_squash、root_squash、no_root_squash。其中all_squash爲所有訪問用戶都會被映射爲匿名用戶或用戶組；no_all_squash爲訪問用戶會先與本機用戶比對，比對失敗後再映射爲匿名用戶或用戶組；root_squash爲将來訪的root用戶映射爲匿名用戶或用戶組；no_root_squash爲來訪的root用戶保持root帳号權限。不填預設爲root_squash。
        :type UserPermission: str
        :param Priority: 規則優先級，參數範圍1-100。 其中 1 爲最高，100爲最低
        :type Priority: int
        """
        self.PGroupId = None
        self.RuleId = None
        self.AuthClientIp = None
        self.RWPermission = None
        self.UserPermission = None
        self.Priority = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.RuleId = params.get("RuleId")
        self.AuthClientIp = params.get("AuthClientIp")
        self.RWPermission = params.get("RWPermission")
        self.UserPermission = params.get("UserPermission")
        self.Priority = params.get("Priority")


class UpdateCfsRuleResponse(AbstractModel):
    """UpdateCfsRule返回參數結構體

    """

    def __init__(self):
        """
        :param PGroupId: 權限組 ID
        :type PGroupId: str
        :param RuleId: 規則 ID
        :type RuleId: str
        :param AuthClientIp: 允許訪問的用戶端 IP 或者 IP 段
        :type AuthClientIp: str
        :param RWPermission: 讀寫權限
        :type RWPermission: str
        :param UserPermission: 用戶權限
        :type UserPermission: str
        :param Priority: 優先級
        :type Priority: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PGroupId = None
        self.RuleId = None
        self.AuthClientIp = None
        self.RWPermission = None
        self.UserPermission = None
        self.Priority = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PGroupId = params.get("PGroupId")
        self.RuleId = params.get("RuleId")
        self.AuthClientIp = params.get("AuthClientIp")
        self.RWPermission = params.get("RWPermission")
        self.UserPermission = params.get("UserPermission")
        self.Priority = params.get("Priority")
        self.RequestId = params.get("RequestId")