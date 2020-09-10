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


class AccessGroup(AbstractModel):
    """權限組

    """

    def __init__(self):
        """
        :param AccessGroupId: 權限組ID
        :type AccessGroupId: str
        :param AccessGroupName: 權限組名稱
        :type AccessGroupName: str
        :param Description: 權限組描述
        :type Description: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        """
        self.AccessGroupId = None
        self.AccessGroupName = None
        self.Description = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.AccessGroupId = params.get("AccessGroupId")
        self.AccessGroupName = params.get("AccessGroupName")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")


class AccessRule(AbstractModel):
    """權限規則

    """

    def __init__(self):
        """
        :param AccessRuleId: 權限規則ID
        :type AccessRuleId: int
        :param Address: 權限規則網址（網段或IP）
        :type Address: str
        :param AccessMode: 權限規則訪問模式（1：只讀；2：讀寫）
        :type AccessMode: int
        :param Priority: 優先級（取值範圍1~100，值越小優先級越高）
        :type Priority: int
        :param CreateTime: 創建時間
        :type CreateTime: str
        """
        self.AccessRuleId = None
        self.Address = None
        self.AccessMode = None
        self.Priority = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.AccessRuleId = params.get("AccessRuleId")
        self.Address = params.get("Address")
        self.AccessMode = params.get("AccessMode")
        self.Priority = params.get("Priority")
        self.CreateTime = params.get("CreateTime")


class CreateAccessGroupRequest(AbstractModel):
    """CreateAccessGroup請求參數結構體

    """

    def __init__(self):
        """
        :param AccessGroupName: 權限組名稱
        :type AccessGroupName: str
        :param Description: 權限組描述
        :type Description: str
        """
        self.AccessGroupName = None
        self.Description = None


    def _deserialize(self, params):
        self.AccessGroupName = params.get("AccessGroupName")
        self.Description = params.get("Description")


class CreateAccessGroupResponse(AbstractModel):
    """CreateAccessGroup返回參數結構體

    """

    def __init__(self):
        """
        :param AccessGroup: 權限組
        :type AccessGroup: :class:`tencentcloud.chdfs.v20190718.models.AccessGroup`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AccessGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccessGroup") is not None:
            self.AccessGroup = AccessGroup()
            self.AccessGroup._deserialize(params.get("AccessGroup"))
        self.RequestId = params.get("RequestId")


class CreateAccessRulesRequest(AbstractModel):
    """CreateAccessRules請求參數結構體

    """

    def __init__(self):
        """
        :param AccessRules: 多個權限規則，上限爲10
        :type AccessRules: list of AccessRule
        :param AccessGroupId: 權限組ID
        :type AccessGroupId: str
        """
        self.AccessRules = None
        self.AccessGroupId = None


    def _deserialize(self, params):
        if params.get("AccessRules") is not None:
            self.AccessRules = []
            for item in params.get("AccessRules"):
                obj = AccessRule()
                obj._deserialize(item)
                self.AccessRules.append(obj)
        self.AccessGroupId = params.get("AccessGroupId")


class CreateAccessRulesResponse(AbstractModel):
    """CreateAccessRules返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateFileSystemRequest(AbstractModel):
    """CreateFileSystem請求參數結構體

    """

    def __init__(self):
        """
        :param FileSystemName: 文件系統名稱
        :type FileSystemName: str
        :param CapacityQuota: 文件系統容量（byte），下限爲1M，上限爲1P，且必須是1M的整數倍
        :type CapacityQuota: int
        :param Description: 文件系統描述
        :type Description: str
        """
        self.FileSystemName = None
        self.CapacityQuota = None
        self.Description = None


    def _deserialize(self, params):
        self.FileSystemName = params.get("FileSystemName")
        self.CapacityQuota = params.get("CapacityQuota")
        self.Description = params.get("Description")


class CreateFileSystemResponse(AbstractModel):
    """CreateFileSystem返回參數結構體

    """

    def __init__(self):
        """
        :param FileSystem: 文件系統
        :type FileSystem: :class:`tencentcloud.chdfs.v20190718.models.FileSystem`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FileSystem = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FileSystem") is not None:
            self.FileSystem = FileSystem()
            self.FileSystem._deserialize(params.get("FileSystem"))
        self.RequestId = params.get("RequestId")


class CreateMountPointRequest(AbstractModel):
    """CreateMountPoint請求參數結構體

    """

    def __init__(self):
        """
        :param MountPointName: 掛載點名稱
        :type MountPointName: str
        :param FileSystemId: 文件系統ID
        :type FileSystemId: str
        :param AccessGroupId: 權限組ID
        :type AccessGroupId: str
        :param VpcId: VPC網絡ID
        :type VpcId: str
        :param MountPointStatus: 掛載點狀态（1：打開；2：關閉）
        :type MountPointStatus: int
        :param VpcType: VPC網絡類型（1：CVM；2：黑石1.0；3：黑石2.0）
        :type VpcType: int
        """
        self.MountPointName = None
        self.FileSystemId = None
        self.AccessGroupId = None
        self.VpcId = None
        self.MountPointStatus = None
        self.VpcType = None


    def _deserialize(self, params):
        self.MountPointName = params.get("MountPointName")
        self.FileSystemId = params.get("FileSystemId")
        self.AccessGroupId = params.get("AccessGroupId")
        self.VpcId = params.get("VpcId")
        self.MountPointStatus = params.get("MountPointStatus")
        self.VpcType = params.get("VpcType")


class CreateMountPointResponse(AbstractModel):
    """CreateMountPoint返回參數結構體

    """

    def __init__(self):
        """
        :param MountPoint: 掛載點
        :type MountPoint: :class:`tencentcloud.chdfs.v20190718.models.MountPoint`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.MountPoint = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MountPoint") is not None:
            self.MountPoint = MountPoint()
            self.MountPoint._deserialize(params.get("MountPoint"))
        self.RequestId = params.get("RequestId")


class DeleteAccessGroupRequest(AbstractModel):
    """DeleteAccessGroup請求參數結構體

    """

    def __init__(self):
        """
        :param AccessGroupId: 權限組ID
        :type AccessGroupId: str
        """
        self.AccessGroupId = None


    def _deserialize(self, params):
        self.AccessGroupId = params.get("AccessGroupId")


class DeleteAccessGroupResponse(AbstractModel):
    """DeleteAccessGroup返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAccessRulesRequest(AbstractModel):
    """DeleteAccessRules請求參數結構體

    """

    def __init__(self):
        """
        :param AccessRuleIds: 多個權限規則ID，上限爲10
        :type AccessRuleIds: list of int non-negative
        """
        self.AccessRuleIds = None


    def _deserialize(self, params):
        self.AccessRuleIds = params.get("AccessRuleIds")


class DeleteAccessRulesResponse(AbstractModel):
    """DeleteAccessRules返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteFileSystemRequest(AbstractModel):
    """DeleteFileSystem請求參數結構體

    """

    def __init__(self):
        """
        :param FileSystemId: 文件系統ID
        :type FileSystemId: str
        """
        self.FileSystemId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")


class DeleteFileSystemResponse(AbstractModel):
    """DeleteFileSystem返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMountPointRequest(AbstractModel):
    """DeleteMountPoint請求參數結構體

    """

    def __init__(self):
        """
        :param MountPointId: 掛載點ID
        :type MountPointId: str
        """
        self.MountPointId = None


    def _deserialize(self, params):
        self.MountPointId = params.get("MountPointId")


class DeleteMountPointResponse(AbstractModel):
    """DeleteMountPoint返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccessGroupsRequest(AbstractModel):
    """DescribeAccessGroups請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 過濾條件，Name可選“AccessGroupId“和“AccessGroupName”，Values上限爲10
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 返回數量，預設爲所有
        :type Limit: int
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAccessGroupsResponse(AbstractModel):
    """DescribeAccessGroups返回參數結構體

    """

    def __init__(self):
        """
        :param AccessGroups: 權限組清單
        :type AccessGroups: list of AccessGroup
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AccessGroups = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccessGroups") is not None:
            self.AccessGroups = []
            for item in params.get("AccessGroups"):
                obj = AccessGroup()
                obj._deserialize(item)
                self.AccessGroups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAccessRulesRequest(AbstractModel):
    """DescribeAccessRules請求參數結構體

    """

    def __init__(self):
        """
        :param AccessGroupId: 權限組ID
        :type AccessGroupId: str
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 返回數量，預設爲所有
        :type Limit: int
        """
        self.AccessGroupId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.AccessGroupId = params.get("AccessGroupId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAccessRulesResponse(AbstractModel):
    """DescribeAccessRules返回參數結構體

    """

    def __init__(self):
        """
        :param AccessRules: 權限規則清單
        :type AccessRules: list of AccessRule
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AccessRules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccessRules") is not None:
            self.AccessRules = []
            for item in params.get("AccessRules"):
                obj = AccessRule()
                obj._deserialize(item)
                self.AccessRules.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFileSystemRequest(AbstractModel):
    """DescribeFileSystem請求參數結構體

    """

    def __init__(self):
        """
        :param FileSystemId: 文件系統ID
        :type FileSystemId: str
        """
        self.FileSystemId = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")


class DescribeFileSystemResponse(AbstractModel):
    """DescribeFileSystem返回參數結構體

    """

    def __init__(self):
        """
        :param FileSystem: 文件系統
        :type FileSystem: :class:`tencentcloud.chdfs.v20190718.models.FileSystem`
        :param FileSystemCapacityUsed: 文件系統已使用大小（byte）
        :type FileSystemCapacityUsed: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FileSystem = None
        self.FileSystemCapacityUsed = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FileSystem") is not None:
            self.FileSystem = FileSystem()
            self.FileSystem._deserialize(params.get("FileSystem"))
        self.FileSystemCapacityUsed = params.get("FileSystemCapacityUsed")
        self.RequestId = params.get("RequestId")


class DescribeFileSystemsRequest(AbstractModel):
    """DescribeFileSystems請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 返回數量，預設爲所有
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeFileSystemsResponse(AbstractModel):
    """DescribeFileSystems返回參數結構體

    """

    def __init__(self):
        """
        :param FileSystems: 文件系統清單
        :type FileSystems: list of FileSystem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FileSystems = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FileSystems") is not None:
            self.FileSystems = []
            for item in params.get("FileSystems"):
                obj = FileSystem()
                obj._deserialize(item)
                self.FileSystems.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMountPointRequest(AbstractModel):
    """DescribeMountPoint請求參數結構體

    """

    def __init__(self):
        """
        :param MountPointId: 掛載點ID
        :type MountPointId: str
        """
        self.MountPointId = None


    def _deserialize(self, params):
        self.MountPointId = params.get("MountPointId")


class DescribeMountPointResponse(AbstractModel):
    """DescribeMountPoint返回參數結構體

    """

    def __init__(self):
        """
        :param MountPoint: 掛載點
        :type MountPoint: :class:`tencentcloud.chdfs.v20190718.models.MountPoint`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.MountPoint = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MountPoint") is not None:
            self.MountPoint = MountPoint()
            self.MountPoint._deserialize(params.get("MountPoint"))
        self.RequestId = params.get("RequestId")


class DescribeMountPointsRequest(AbstractModel):
    """DescribeMountPoints請求參數結構體

    """

    def __init__(self):
        """
        :param FileSystemId: 文件系統ID
注意：若根據AccessGroupId檢視掛載點清單，則無需設置FileSystemId
        :type FileSystemId: str
        :param AccessGroupId: 權限組ID
注意：若根據FileSystemId檢視掛載點清單，則無需設置AccessGroupId
        :type AccessGroupId: str
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param Limit: 返回數量，預設爲所有
        :type Limit: int
        """
        self.FileSystemId = None
        self.AccessGroupId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        self.AccessGroupId = params.get("AccessGroupId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeMountPointsResponse(AbstractModel):
    """DescribeMountPoints返回參數結構體

    """

    def __init__(self):
        """
        :param MountPoints: 掛載點清單
        :type MountPoints: list of MountPoint
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.MountPoints = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MountPoints") is not None:
            self.MountPoints = []
            for item in params.get("MountPoints"):
                obj = MountPoint()
                obj._deserialize(item)
                self.MountPoints.append(obj)
        self.RequestId = params.get("RequestId")


class FileSystem(AbstractModel):
    """文件系統

    """

    def __init__(self):
        """
        :param AppId: appid
        :type AppId: int
        :param FileSystemName: 文件系統名稱
        :type FileSystemName: str
        :param Description: 文件系統描述
        :type Description: str
        :param Region: 地域
        :type Region: str
        :param FileSystemId: 文件系統ID
        :type FileSystemId: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param BlockSize: 文件系統塊大小（byte）
        :type BlockSize: int
        :param CapacityQuota: 文件系統容量（byte）
        :type CapacityQuota: int
        :param Status: 文件系統狀态（1：創建中；2：創建成功；3：創建失敗）
        :type Status: int
        """
        self.AppId = None
        self.FileSystemName = None
        self.Description = None
        self.Region = None
        self.FileSystemId = None
        self.CreateTime = None
        self.BlockSize = None
        self.CapacityQuota = None
        self.Status = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.FileSystemName = params.get("FileSystemName")
        self.Description = params.get("Description")
        self.Region = params.get("Region")
        self.FileSystemId = params.get("FileSystemId")
        self.CreateTime = params.get("CreateTime")
        self.BlockSize = params.get("BlockSize")
        self.CapacityQuota = params.get("CapacityQuota")
        self.Status = params.get("Status")


class Filter(AbstractModel):
    """過濾條件

    """

    def __init__(self):
        """
        :param Name: 過濾欄位
        :type Name: str
        :param Values: 過濾值
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class ModifyAccessGroupRequest(AbstractModel):
    """ModifyAccessGroup請求參數結構體

    """

    def __init__(self):
        """
        :param AccessGroupId: 權限組ID
        :type AccessGroupId: str
        :param AccessGroupName: 權限組名稱
        :type AccessGroupName: str
        :param Description: 權限組描述
        :type Description: str
        """
        self.AccessGroupId = None
        self.AccessGroupName = None
        self.Description = None


    def _deserialize(self, params):
        self.AccessGroupId = params.get("AccessGroupId")
        self.AccessGroupName = params.get("AccessGroupName")
        self.Description = params.get("Description")


class ModifyAccessGroupResponse(AbstractModel):
    """ModifyAccessGroup返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAccessRulesRequest(AbstractModel):
    """ModifyAccessRules請求參數結構體

    """

    def __init__(self):
        """
        :param AccessRules: 多個權限規則，上限爲10
        :type AccessRules: list of AccessRule
        """
        self.AccessRules = None


    def _deserialize(self, params):
        if params.get("AccessRules") is not None:
            self.AccessRules = []
            for item in params.get("AccessRules"):
                obj = AccessRule()
                obj._deserialize(item)
                self.AccessRules.append(obj)


class ModifyAccessRulesResponse(AbstractModel):
    """ModifyAccessRules返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyFileSystemRequest(AbstractModel):
    """ModifyFileSystem請求參數結構體

    """

    def __init__(self):
        """
        :param FileSystemId: 文件系統ID
        :type FileSystemId: str
        :param FileSystemName: 文件系統名稱
        :type FileSystemName: str
        :param Description: 文件系統描述
        :type Description: str
        :param CapacityQuota: 文件系統容量（byte），下限爲1M，上限爲1P，且必須是1M的整數倍
注意：修改的文件系統容量不能小於當前使用量
        :type CapacityQuota: int
        """
        self.FileSystemId = None
        self.FileSystemName = None
        self.Description = None
        self.CapacityQuota = None


    def _deserialize(self, params):
        self.FileSystemId = params.get("FileSystemId")
        self.FileSystemName = params.get("FileSystemName")
        self.Description = params.get("Description")
        self.CapacityQuota = params.get("CapacityQuota")


class ModifyFileSystemResponse(AbstractModel):
    """ModifyFileSystem返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMountPointRequest(AbstractModel):
    """ModifyMountPoint請求參數結構體

    """

    def __init__(self):
        """
        :param MountPointId: 掛載點ID
        :type MountPointId: str
        :param MountPointName: 掛載點名稱
        :type MountPointName: str
        :param MountPointStatus: 掛載點狀态
        :type MountPointStatus: int
        :param AccessGroupId: 權限組ID
        :type AccessGroupId: str
        """
        self.MountPointId = None
        self.MountPointName = None
        self.MountPointStatus = None
        self.AccessGroupId = None


    def _deserialize(self, params):
        self.MountPointId = params.get("MountPointId")
        self.MountPointName = params.get("MountPointName")
        self.MountPointStatus = params.get("MountPointStatus")
        self.AccessGroupId = params.get("AccessGroupId")


class ModifyMountPointResponse(AbstractModel):
    """ModifyMountPoint返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MountPoint(AbstractModel):
    """掛載點

    """

    def __init__(self):
        """
        :param MountPointId: 掛載點ID
        :type MountPointId: str
        :param MountPointName: 掛載點名稱
        :type MountPointName: str
        :param FileSystemId: 文件系統ID
        :type FileSystemId: str
        :param AccessGroupId: 權限組ID
        :type AccessGroupId: str
        :param VpcId: VPC網絡ID
        :type VpcId: str
        :param Status: 掛載點狀态（1：打開；2：關閉）
        :type Status: int
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param VpcType: VPC網絡類型
        :type VpcType: int
        """
        self.MountPointId = None
        self.MountPointName = None
        self.FileSystemId = None
        self.AccessGroupId = None
        self.VpcId = None
        self.Status = None
        self.CreateTime = None
        self.VpcType = None


    def _deserialize(self, params):
        self.MountPointId = params.get("MountPointId")
        self.MountPointName = params.get("MountPointName")
        self.FileSystemId = params.get("FileSystemId")
        self.AccessGroupId = params.get("AccessGroupId")
        self.VpcId = params.get("VpcId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.VpcType = params.get("VpcType")