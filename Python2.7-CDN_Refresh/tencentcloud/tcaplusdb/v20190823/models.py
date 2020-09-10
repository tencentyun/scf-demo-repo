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


class ClearTablesRequest(AbstractModel):
    """ClearTables請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 表所屬集群實例ID
        :type ClusterId: str
        :param SelectedTables: 待清理表訊息清單
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self.ClusterId = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)


class ClearTablesResponse(AbstractModel):
    """ClearTables返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 清除表結果數量
        :type TotalCount: int
        :param TableResults: 清除表結果清單
        :type TableResults: list of TableResultNew
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class ClusterInfo(AbstractModel):
    """集群詳細訊息

    """

    def __init__(self):
        """
        :param ClusterName: 集群名稱
        :type ClusterName: str
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param Region: 集群所在地域
        :type Region: str
        :param IdlType: 集群數據描述語言類型，如：`PROTO`,`TDR`或`MIX`
        :type IdlType: str
        :param NetworkType: 網絡類型
        :type NetworkType: str
        :param VpcId: 集群關聯的用戶私有網絡實例ID
        :type VpcId: str
        :param SubnetId: 集群關聯的用戶子網實例ID
        :type SubnetId: str
        :param CreatedTime: 創建時間
        :type CreatedTime: str
        :param Password: 集群密碼
        :type Password: str
        :param PasswordStatus: 密碼狀态
        :type PasswordStatus: str
        :param ApiAccessId: TcaplusDB SDK連接參數，接入ID
        :type ApiAccessId: str
        :param ApiAccessIp: TcaplusDB SDK連接參數，接入網址
        :type ApiAccessIp: str
        :param ApiAccessPort: TcaplusDB SDK連接參數，接入端口
        :type ApiAccessPort: int
        :param OldPasswordExpireTime: 如果PasswordStatus是unmodifiable說明有舊密碼還未過期，此欄位将顯示舊密碼過期的時間，否則爲空
注意：此欄位可能返回 null，表示取不到有效值。
        :type OldPasswordExpireTime: str
        """
        self.ClusterName = None
        self.ClusterId = None
        self.Region = None
        self.IdlType = None
        self.NetworkType = None
        self.VpcId = None
        self.SubnetId = None
        self.CreatedTime = None
        self.Password = None
        self.PasswordStatus = None
        self.ApiAccessId = None
        self.ApiAccessIp = None
        self.ApiAccessPort = None
        self.OldPasswordExpireTime = None


    def _deserialize(self, params):
        self.ClusterName = params.get("ClusterName")
        self.ClusterId = params.get("ClusterId")
        self.Region = params.get("Region")
        self.IdlType = params.get("IdlType")
        self.NetworkType = params.get("NetworkType")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.CreatedTime = params.get("CreatedTime")
        self.Password = params.get("Password")
        self.PasswordStatus = params.get("PasswordStatus")
        self.ApiAccessId = params.get("ApiAccessId")
        self.ApiAccessIp = params.get("ApiAccessIp")
        self.ApiAccessPort = params.get("ApiAccessPort")
        self.OldPasswordExpireTime = params.get("OldPasswordExpireTime")


class CompareIdlFilesRequest(AbstractModel):
    """CompareIdlFiles請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 待修改表格所在集群ID
        :type ClusterId: str
        :param SelectedTables: 待修改表格清單
        :type SelectedTables: list of SelectedTableInfoNew
        :param ExistingIdlFiles: 選中的已上傳IDL文件清單，與NewIdlFiles必選其一
        :type ExistingIdlFiles: list of IdlFileInfo
        :param NewIdlFiles: 本次上傳IDL文件清單，與ExistingIdlFiles必選其一
        :type NewIdlFiles: list of IdlFileInfo
        """
        self.ClusterId = None
        self.SelectedTables = None
        self.ExistingIdlFiles = None
        self.NewIdlFiles = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        if params.get("ExistingIdlFiles") is not None:
            self.ExistingIdlFiles = []
            for item in params.get("ExistingIdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.ExistingIdlFiles.append(obj)
        if params.get("NewIdlFiles") is not None:
            self.NewIdlFiles = []
            for item in params.get("NewIdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.NewIdlFiles.append(obj)


class CompareIdlFilesResponse(AbstractModel):
    """CompareIdlFiles返回參數結構體

    """

    def __init__(self):
        """
        :param IdlFiles: 本次上傳校驗所有的IDL文件訊息清單
        :type IdlFiles: list of IdlFileInfo
        :param TotalCount: 本次校驗合法的表格數量
        :type TotalCount: int
        :param TableInfos: 讀取IDL描述文件後,根據用戶指示的所選中表格解析校驗結果
        :type TableInfos: list of ParsedTableInfoNew
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.IdlFiles = None
        self.TotalCount = None
        self.TableInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("IdlFiles") is not None:
            self.IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.IdlFiles.append(obj)
        self.TotalCount = params.get("TotalCount")
        if params.get("TableInfos") is not None:
            self.TableInfos = []
            for item in params.get("TableInfos"):
                obj = ParsedTableInfoNew()
                obj._deserialize(item)
                self.TableInfos.append(obj)
        self.RequestId = params.get("RequestId")


class CreateBackupRequest(AbstractModel):
    """CreateBackup請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 待創建備份表所屬集群ID
        :type ClusterId: str
        :param SelectedTables: 待創建備份表訊息清單
        :type SelectedTables: list of SelectedTableInfoNew
        :param Remark: 備注訊息
        :type Remark: str
        """
        self.ClusterId = None
        self.SelectedTables = None
        self.Remark = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        self.Remark = params.get("Remark")


class CreateBackupResponse(AbstractModel):
    """CreateBackup返回參數結構體

    """

    def __init__(self):
        """
        :param TaskIds: 創建的備份任務ID清單
        :type TaskIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")
        self.RequestId = params.get("RequestId")


class CreateClusterRequest(AbstractModel):
    """CreateCluster請求參數結構體

    """

    def __init__(self):
        """
        :param IdlType: 集群數據描述語言類型，如：`PROTO`，`TDR`或`MIX`
        :type IdlType: str
        :param ClusterName: 集群名稱，可使用中文或英文字元，最大長度32個字元
        :type ClusterName: str
        :param VpcId: 集群所綁定的私有網絡實例ID，形如：vpc-f49l6u0z
        :type VpcId: str
        :param SubnetId: 集群所綁定的子網實例ID，形如：subnet-pxir56ns
        :type SubnetId: str
        :param Password: 集群訪問密碼，必須是a-zA-Z0-9的字元,且必須包含數字和大小寫字母
        :type Password: str
        """
        self.IdlType = None
        self.ClusterName = None
        self.VpcId = None
        self.SubnetId = None
        self.Password = None


    def _deserialize(self, params):
        self.IdlType = params.get("IdlType")
        self.ClusterName = params.get("ClusterName")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Password = params.get("Password")


class CreateClusterResponse(AbstractModel):
    """CreateCluster返回參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ClusterId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.RequestId = params.get("RequestId")


class CreateTableGroupRequest(AbstractModel):
    """CreateTableGroup請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 表格組所屬集群ID
        :type ClusterId: str
        :param TableGroupName: 表格組名稱，可以采用中文、英文或數字字元，最大長度32個字元
        :type TableGroupName: str
        :param TableGroupId: 表格組ID，可以由用戶指定，但在同一個集群内不能重複，如果不指定則采用自增的模式
        :type TableGroupId: str
        """
        self.ClusterId = None
        self.TableGroupName = None
        self.TableGroupId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupName = params.get("TableGroupName")
        self.TableGroupId = params.get("TableGroupId")


class CreateTableGroupResponse(AbstractModel):
    """CreateTableGroup返回參數結構體

    """

    def __init__(self):
        """
        :param TableGroupId: 創建成功的表格組ID
        :type TableGroupId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TableGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TableGroupId = params.get("TableGroupId")
        self.RequestId = params.get("RequestId")


class CreateTablesRequest(AbstractModel):
    """CreateTables請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 待創建表格所屬集群ID
        :type ClusterId: str
        :param IdlFiles: 用戶選定的建表格IDL文件清單
        :type IdlFiles: list of IdlFileInfo
        :param SelectedTables: 待創建表格訊息清單
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self.ClusterId = None
        self.IdlFiles = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("IdlFiles") is not None:
            self.IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.IdlFiles.append(obj)
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)


class CreateTablesResponse(AbstractModel):
    """CreateTables返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 批次創建表格結果數量
        :type TotalCount: int
        :param TableResults: 批次創建表格結果清單
        :type TableResults: list of TableResultNew
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class DeleteClusterRequest(AbstractModel):
    """DeleteCluster請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 待删除的集群ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")


class DeleteClusterResponse(AbstractModel):
    """DeleteCluster返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 删除集群生成的任務ID
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteIdlFilesRequest(AbstractModel):
    """DeleteIdlFiles請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: IDL所屬集群ID
        :type ClusterId: str
        :param IdlFiles: 待删除的IDL文件訊息清單
        :type IdlFiles: list of IdlFileInfo
        """
        self.ClusterId = None
        self.IdlFiles = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("IdlFiles") is not None:
            self.IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.IdlFiles.append(obj)


class DeleteIdlFilesResponse(AbstractModel):
    """DeleteIdlFiles返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 結果記錄數量
        :type TotalCount: int
        :param IdlFileInfos: 删除結果
        :type IdlFileInfos: list of IdlFileInfoWithoutContent
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.IdlFileInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("IdlFileInfos") is not None:
            self.IdlFileInfos = []
            for item in params.get("IdlFileInfos"):
                obj = IdlFileInfoWithoutContent()
                obj._deserialize(item)
                self.IdlFileInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DeleteTableGroupRequest(AbstractModel):
    """DeleteTableGroup請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 表格組所屬的集群ID
        :type ClusterId: str
        :param TableGroupId: 表格組ID
        :type TableGroupId: str
        """
        self.ClusterId = None
        self.TableGroupId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupId = params.get("TableGroupId")


class DeleteTableGroupResponse(AbstractModel):
    """DeleteTableGroup返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 删除表格組所創建的任務ID
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteTablesRequest(AbstractModel):
    """DeleteTables請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 待删除表所在集群ID
        :type ClusterId: str
        :param SelectedTables: 待删除表訊息清單
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self.ClusterId = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)


class DeleteTablesResponse(AbstractModel):
    """DeleteTables返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 删除表結果數量
        :type TotalCount: int
        :param TableResults: 删除表結果詳情清單
        :type TableResults: list of TableResultNew
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterIds: 指定查詢的集群ID清單
        :type ClusterIds: list of str
        :param Filters: 查詢過濾條件
        :type Filters: list of Filter
        :param Offset: 查詢清單偏移量
        :type Offset: int
        :param Limit: 查詢清單返回記錄數，預設值20
        :type Limit: int
        """
        self.ClusterIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterIds = params.get("ClusterIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeClustersResponse(AbstractModel):
    """DescribeClusters返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 集群實例數
        :type TotalCount: int
        :param Clusters: 集群實例清單
        :type Clusters: list of ClusterInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Clusters = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Clusters") is not None:
            self.Clusters = []
            for item in params.get("Clusters"):
                obj = ClusterInfo()
                obj._deserialize(item)
                self.Clusters.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIdlFileInfosRequest(AbstractModel):
    """DescribeIdlFileInfos請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 文件所屬集群ID
        :type ClusterId: str
        :param TableGroupIds: 文件所屬表格組ID
        :type TableGroupIds: list of str
        :param IdlFileIds: 指定文件ID清單
        :type IdlFileIds: list of str
        :param Offset: 查詢清單偏移量
        :type Offset: int
        :param Limit: 查詢清單返回記錄數
        :type Limit: int
        """
        self.ClusterId = None
        self.TableGroupIds = None
        self.IdlFileIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupIds = params.get("TableGroupIds")
        self.IdlFileIds = params.get("IdlFileIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeIdlFileInfosResponse(AbstractModel):
    """DescribeIdlFileInfos返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 文件數量
        :type TotalCount: int
        :param IdlFileInfos: 文件詳情清單
        :type IdlFileInfos: list of IdlFileInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.IdlFileInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("IdlFileInfos") is not None:
            self.IdlFileInfos = []
            for item in params.get("IdlFileInfos"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.IdlFileInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions請求參數結構體

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 可用區詳情結果數量
        :type TotalCount: int
        :param RegionInfos: 可用區詳情結果清單
        :type RegionInfos: list of RegionInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RegionInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RegionInfos") is not None:
            self.RegionInfos = []
            for item in params.get("RegionInfos"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.RegionInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTableGroupsRequest(AbstractModel):
    """DescribeTableGroups請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 表格組所屬集群ID
        :type ClusterId: str
        :param TableGroupIds: 表格組ID清單
        :type TableGroupIds: list of str
        :param Filters: 過濾條件，本介面支援：TableGroupName，TableGroupId
        :type Filters: list of Filter
        :param Offset: 查詢清單偏移量
        :type Offset: int
        :param Limit: 查詢清單返回記錄數
        :type Limit: int
        """
        self.ClusterId = None
        self.TableGroupIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupIds = params.get("TableGroupIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTableGroupsResponse(AbstractModel):
    """DescribeTableGroups返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 表格組數量
        :type TotalCount: int
        :param TableGroups: 表格組訊息清單
        :type TableGroups: list of TableGroupInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableGroups = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableGroups") is not None:
            self.TableGroups = []
            for item in params.get("TableGroups"):
                obj = TableGroupInfo()
                obj._deserialize(item)
                self.TableGroups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTablesInRecycleRequest(AbstractModel):
    """DescribeTablesInRecycle請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 待查詢表格所屬集群ID
        :type ClusterId: str
        :param TableGroupIds: 待查詢表格所屬表格組ID清單
        :type TableGroupIds: list of str
        :param Filters: 過濾條件，本介面支援：TableName，TableInstanceId
        :type Filters: list of Filter
        :param Offset: 查詢結果偏移量
        :type Offset: int
        :param Limit: 查詢結果返回記錄數量
        :type Limit: int
        """
        self.ClusterId = None
        self.TableGroupIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupIds = params.get("TableGroupIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTablesInRecycleResponse(AbstractModel):
    """DescribeTablesInRecycle返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 表格數量
        :type TotalCount: int
        :param TableInfos: 表格詳情結果清單
        :type TableInfos: list of TableInfoNew
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableInfos") is not None:
            self.TableInfos = []
            for item in params.get("TableInfos"):
                obj = TableInfoNew()
                obj._deserialize(item)
                self.TableInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTablesRequest(AbstractModel):
    """DescribeTables請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 待查詢表格所屬集群ID
        :type ClusterId: str
        :param TableGroupIds: 待查詢表格所屬表格組ID清單
        :type TableGroupIds: list of str
        :param SelectedTables: 待查詢表格訊息清單
        :type SelectedTables: list of SelectedTableInfoNew
        :param Filters: 過濾條件，本介面支援：TableName，TableInstanceId
        :type Filters: list of Filter
        :param Offset: 查詢結果偏移量
        :type Offset: int
        :param Limit: 查詢結果返回記錄數量
        :type Limit: int
        """
        self.ClusterId = None
        self.TableGroupIds = None
        self.SelectedTables = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupIds = params.get("TableGroupIds")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTablesResponse(AbstractModel):
    """DescribeTables返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 表格數量
        :type TotalCount: int
        :param TableInfos: 表格詳情結果清單
        :type TableInfos: list of TableInfoNew
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableInfos") is not None:
            self.TableInfos = []
            for item in params.get("TableInfos"):
                obj = TableInfoNew()
                obj._deserialize(item)
                self.TableInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterIds: 需要查詢任務所屬的集群ID清單
        :type ClusterIds: list of str
        :param TaskIds: 需要查詢的任務ID清單
        :type TaskIds: list of str
        :param Filters: 過濾條件，本介面支援：Content，TaskType, Operator, Time
        :type Filters: list of Filter
        :param Offset: 查詢清單偏移量
        :type Offset: int
        :param Limit: 查詢清單返回記錄數
        :type Limit: int
        """
        self.ClusterIds = None
        self.TaskIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterIds = params.get("ClusterIds")
        self.TaskIds = params.get("TaskIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 任務數量
        :type TotalCount: int
        :param TaskInfos: 查詢到的任務詳情清單
        :type TaskInfos: list of TaskInfoNew
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TaskInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TaskInfos") is not None:
            self.TaskInfos = []
            for item in params.get("TaskInfos"):
                obj = TaskInfoNew()
                obj._deserialize(item)
                self.TaskInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUinInWhitelistRequest(AbstractModel):
    """DescribeUinInWhitelist請求參數結構體

    """


class DescribeUinInWhitelistResponse(AbstractModel):
    """DescribeUinInWhitelist返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 查詢結果：`FALSE` 否；`TRUE` 是
        :type Result: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ErrorInfo(AbstractModel):
    """描述每個實例（應用，大區或表）處理過程中可能出現的錯誤詳情。

    """

    def __init__(self):
        """
        :param Code: 錯誤碼
        :type Code: str
        :param Message: 錯誤訊息
        :type Message: str
        """
        self.Code = None
        self.Message = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Message = params.get("Message")


class Filter(AbstractModel):
    """過濾條件

    """

    def __init__(self):
        """
        :param Name: 過濾欄位名
        :type Name: str
        :param Value: 過濾欄位值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class IdlFileInfo(AbstractModel):
    """表定義描述文件詳情，包含文件内容

    """

    def __init__(self):
        """
        :param FileName: 文件名稱，不包含擴展名
        :type FileName: str
        :param FileType: 數據描述語言（IDL）類型
        :type FileType: str
        :param FileExtType: 文件擴展名
        :type FileExtType: str
        :param FileSize: 文件大小（Bytes）
        :type FileSize: int
        :param FileId: 文件ID，對于已上傳的文件有意義
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileId: int
        :param FileContent: 文件内容，對于本次新上傳的文件有意義
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileContent: str
        """
        self.FileName = None
        self.FileType = None
        self.FileExtType = None
        self.FileSize = None
        self.FileId = None
        self.FileContent = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.FileType = params.get("FileType")
        self.FileExtType = params.get("FileExtType")
        self.FileSize = params.get("FileSize")
        self.FileId = params.get("FileId")
        self.FileContent = params.get("FileContent")


class IdlFileInfoWithoutContent(AbstractModel):
    """表定義描述文件詳情，不包含文件内容

    """

    def __init__(self):
        """
        :param FileName: 文件名稱，不包含擴展名
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileName: str
        :param FileType: 數據描述語言（IDL）類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileType: str
        :param FileExtType: 文件擴展名
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileExtType: str
        :param FileSize: 文件大小（Bytes）
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileSize: int
        :param FileId: 文件ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileId: int
        :param Error: 錯誤訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Error: :class:`taifucloudcloud.tcaplusdb.v20190823.models.ErrorInfo`
        """
        self.FileName = None
        self.FileType = None
        self.FileExtType = None
        self.FileSize = None
        self.FileId = None
        self.Error = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.FileType = params.get("FileType")
        self.FileExtType = params.get("FileExtType")
        self.FileSize = params.get("FileSize")
        self.FileId = params.get("FileId")
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))


class ModifyClusterNameRequest(AbstractModel):
    """ModifyClusterName請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 需要修改名稱的集群ID
        :type ClusterId: str
        :param ClusterName: 需要修改的集群名稱，可使用中文或英文字元，最大長度32個字元
        :type ClusterName: str
        """
        self.ClusterId = None
        self.ClusterName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")


class ModifyClusterNameResponse(AbstractModel):
    """ModifyClusterName返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterPasswordRequest(AbstractModel):
    """ModifyClusterPassword請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 需要修改密碼的集群ID
        :type ClusterId: str
        :param OldPassword: 集群舊密碼
        :type OldPassword: str
        :param OldPasswordExpireTime: 集群舊密碼預期失效時間
        :type OldPasswordExpireTime: str
        :param NewPassword: 集群新密碼，密碼必須是a-zA-Z0-9的字元,且必須包含數字和大小寫字母
        :type NewPassword: str
        :param Mode: 更新模式： `1` 更新密碼；`2` 更新舊密碼失效時間，預設爲`1` 模式
        :type Mode: str
        """
        self.ClusterId = None
        self.OldPassword = None
        self.OldPasswordExpireTime = None
        self.NewPassword = None
        self.Mode = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.OldPassword = params.get("OldPassword")
        self.OldPasswordExpireTime = params.get("OldPasswordExpireTime")
        self.NewPassword = params.get("NewPassword")
        self.Mode = params.get("Mode")


class ModifyClusterPasswordResponse(AbstractModel):
    """ModifyClusterPassword返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTableGroupNameRequest(AbstractModel):
    """ModifyTableGroupName請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 表格組所屬的集群ID
        :type ClusterId: str
        :param TableGroupId: 待修改名稱的表格組ID
        :type TableGroupId: str
        :param TableGroupName: 新的表格組名稱，可以使用中英文字元和符号
        :type TableGroupName: str
        """
        self.ClusterId = None
        self.TableGroupId = None
        self.TableGroupName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupId = params.get("TableGroupId")
        self.TableGroupName = params.get("TableGroupName")


class ModifyTableGroupNameResponse(AbstractModel):
    """ModifyTableGroupName返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTableMemosRequest(AbstractModel):
    """ModifyTableMemos請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 表所屬集群實例ID
        :type ClusterId: str
        :param TableMemos: 選定表詳情清單
        :type TableMemos: list of SelectedTableInfoNew
        """
        self.ClusterId = None
        self.TableMemos = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("TableMemos") is not None:
            self.TableMemos = []
            for item in params.get("TableMemos"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.TableMemos.append(obj)


class ModifyTableMemosResponse(AbstractModel):
    """ModifyTableMemos返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 表備注修改結果數量
        :type TotalCount: int
        :param TableResults: 表備注修改結果清單
        :type TableResults: list of TableResultNew
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyTableQuotasRequest(AbstractModel):
    """ModifyTableQuotas請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 帶擴縮容表所屬集群ID
        :type ClusterId: str
        :param TableQuotas: 已選中待修改的表配額清單
        :type TableQuotas: list of SelectedTableInfoNew
        """
        self.ClusterId = None
        self.TableQuotas = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("TableQuotas") is not None:
            self.TableQuotas = []
            for item in params.get("TableQuotas"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.TableQuotas.append(obj)


class ModifyTableQuotasResponse(AbstractModel):
    """ModifyTableQuotas返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 擴縮容結果數量
        :type TotalCount: int
        :param TableResults: 擴縮容結果清單
        :type TableResults: list of TableResultNew
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyTablesRequest(AbstractModel):
    """ModifyTables請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 待修改表格所在集群ID
        :type ClusterId: str
        :param IdlFiles: 選中的改表IDL文件
        :type IdlFiles: list of IdlFileInfo
        :param SelectedTables: 待改表格清單
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self.ClusterId = None
        self.IdlFiles = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("IdlFiles") is not None:
            self.IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.IdlFiles.append(obj)
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)


class ModifyTablesResponse(AbstractModel):
    """ModifyTables返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 修改表結果數量
        :type TotalCount: int
        :param TableResults: 修改表結果清單
        :type TableResults: list of TableResultNew
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class ParsedTableInfoNew(AbstractModel):
    """從IDL表描述文件中解析出來的表訊息

    """

    def __init__(self):
        """
        :param TableIdlType: 表格描述語言類型：`PROTO`或`TDR`
注意：此欄位可能返回 null，表示取不到有效值。
        :type TableIdlType: str
        :param TableInstanceId: 表格實例ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type TableInstanceId: str
        :param TableName: 表格名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type TableName: str
        :param TableType: 表格數據結構類型：`GENERIC`或`LIST`
注意：此欄位可能返回 null，表示取不到有效值。
        :type TableType: str
        :param KeyFields: 主鍵欄位訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type KeyFields: str
        :param OldKeyFields: 原主鍵欄位訊息，改表校驗時有效
注意：此欄位可能返回 null，表示取不到有效值。
        :type OldKeyFields: str
        :param ValueFields: 非主鍵欄位訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type ValueFields: str
        :param OldValueFields: 原非主鍵欄位訊息，改表校驗時有效
注意：此欄位可能返回 null，表示取不到有效值。
        :type OldValueFields: str
        :param TableGroupId: 所屬表格組ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type TableGroupId: str
        :param SumKeyFieldSize: 主鍵欄位總大小
注意：此欄位可能返回 null，表示取不到有效值。
        :type SumKeyFieldSize: int
        :param SumValueFieldSize: 非主鍵欄位總大小
注意：此欄位可能返回 null，表示取不到有效值。
        :type SumValueFieldSize: int
        :param IndexKeySet: 索引鍵集合
注意：此欄位可能返回 null，表示取不到有效值。
        :type IndexKeySet: str
        :param ShardingKeySet: 分表因子集合
注意：此欄位可能返回 null，表示取不到有效值。
        :type ShardingKeySet: str
        :param TdrVersion: TDR版本号
注意：此欄位可能返回 null，表示取不到有效值。
        :type TdrVersion: int
        :param Error: 錯誤訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Error: :class:`taifucloudcloud.tcaplusdb.v20190823.models.ErrorInfo`
        :param ListElementNum: LIST類型表格元素個數
注意：此欄位可能返回 null，表示取不到有效值。
        :type ListElementNum: int
        :param SortFieldNum: SORTLIST類型表格排序欄位個數
注意：此欄位可能返回 null，表示取不到有效值。
        :type SortFieldNum: int
        :param SortRule: SORTLIST類型表格排序順序
注意：此欄位可能返回 null，表示取不到有效值。
        :type SortRule: int
        """
        self.TableIdlType = None
        self.TableInstanceId = None
        self.TableName = None
        self.TableType = None
        self.KeyFields = None
        self.OldKeyFields = None
        self.ValueFields = None
        self.OldValueFields = None
        self.TableGroupId = None
        self.SumKeyFieldSize = None
        self.SumValueFieldSize = None
        self.IndexKeySet = None
        self.ShardingKeySet = None
        self.TdrVersion = None
        self.Error = None
        self.ListElementNum = None
        self.SortFieldNum = None
        self.SortRule = None


    def _deserialize(self, params):
        self.TableIdlType = params.get("TableIdlType")
        self.TableInstanceId = params.get("TableInstanceId")
        self.TableName = params.get("TableName")
        self.TableType = params.get("TableType")
        self.KeyFields = params.get("KeyFields")
        self.OldKeyFields = params.get("OldKeyFields")
        self.ValueFields = params.get("ValueFields")
        self.OldValueFields = params.get("OldValueFields")
        self.TableGroupId = params.get("TableGroupId")
        self.SumKeyFieldSize = params.get("SumKeyFieldSize")
        self.SumValueFieldSize = params.get("SumValueFieldSize")
        self.IndexKeySet = params.get("IndexKeySet")
        self.ShardingKeySet = params.get("ShardingKeySet")
        self.TdrVersion = params.get("TdrVersion")
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        self.ListElementNum = params.get("ListElementNum")
        self.SortFieldNum = params.get("SortFieldNum")
        self.SortRule = params.get("SortRule")


class RecoverRecycleTablesRequest(AbstractModel):
    """RecoverRecycleTables請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 表所在集群ID
        :type ClusterId: str
        :param SelectedTables: 待恢複表訊息
        :type SelectedTables: list of SelectedTableInfoNew
        """
        self.ClusterId = None
        self.SelectedTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)


class RecoverRecycleTablesResponse(AbstractModel):
    """RecoverRecycleTables返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 恢複表結果數量
        :type TotalCount: int
        :param TableResults: 恢複表訊息清單
        :type TableResults: list of TableResultNew
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """TcaplusDB服務地域訊息詳情

    """

    def __init__(self):
        """
        :param RegionName: 地域Ap-Code
        :type RegionName: str
        :param RegionAbbr: 地域縮寫
        :type RegionAbbr: str
        :param RegionId: 地域ID
        :type RegionId: int
        """
        self.RegionName = None
        self.RegionAbbr = None
        self.RegionId = None


    def _deserialize(self, params):
        self.RegionName = params.get("RegionName")
        self.RegionAbbr = params.get("RegionAbbr")
        self.RegionId = params.get("RegionId")


class RollbackTablesRequest(AbstractModel):
    """RollbackTables請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 待回檔表格所在集群ID
        :type ClusterId: str
        :param SelectedTables: 待回檔表格清單
        :type SelectedTables: list of SelectedTableInfoNew
        :param RollbackTime: 待回檔時間
        :type RollbackTime: str
        :param Mode: 回檔模式，支援：`KEYS`
        :type Mode: str
        """
        self.ClusterId = None
        self.SelectedTables = None
        self.RollbackTime = None
        self.Mode = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("SelectedTables") is not None:
            self.SelectedTables = []
            for item in params.get("SelectedTables"):
                obj = SelectedTableInfoNew()
                obj._deserialize(item)
                self.SelectedTables.append(obj)
        self.RollbackTime = params.get("RollbackTime")
        self.Mode = params.get("Mode")


class RollbackTablesResponse(AbstractModel):
    """RollbackTables返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 表格回檔任務結果數量
        :type TotalCount: int
        :param TableResults: 表格回檔任務結果清單
        :type TableResults: list of TableRollbackResultNew
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TableResults = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TableResults") is not None:
            self.TableResults = []
            for item in params.get("TableResults"):
                obj = TableRollbackResultNew()
                obj._deserialize(item)
                self.TableResults.append(obj)
        self.RequestId = params.get("RequestId")


class SelectedTableInfoNew(AbstractModel):
    """被選中的表訊息

    """

    def __init__(self):
        """
        :param TableGroupId: 表所屬表格組ID
        :type TableGroupId: str
        :param TableName: 表格名稱
        :type TableName: str
        :param TableInstanceId: 表實例ID
        :type TableInstanceId: str
        :param TableIdlType: 表格描述語言類型：`PROTO`或`TDR`
        :type TableIdlType: str
        :param TableType: 表格數據結構類型：`GENERIC`或`LIST`
        :type TableType: str
        :param ListElementNum: LIST表元素個數
        :type ListElementNum: int
        :param ReservedVolume: 表格預留容量（GB）
        :type ReservedVolume: int
        :param ReservedReadQps: 表格預留讀QPS
        :type ReservedReadQps: int
        :param ReservedWriteQps: 表格預留寫QPS
        :type ReservedWriteQps: int
        :param Memo: 表格備注訊息
        :type Memo: str
        :param FileName: Key回檔文件名，回檔專用
        :type FileName: str
        :param FileExtType: Key回檔文件擴展名，回檔專用
        :type FileExtType: str
        :param FileSize: Key回檔文件大小，回檔專用
        :type FileSize: int
        :param FileContent: Key回檔文件内容，回檔專用
        :type FileContent: str
        """
        self.TableGroupId = None
        self.TableName = None
        self.TableInstanceId = None
        self.TableIdlType = None
        self.TableType = None
        self.ListElementNum = None
        self.ReservedVolume = None
        self.ReservedReadQps = None
        self.ReservedWriteQps = None
        self.Memo = None
        self.FileName = None
        self.FileExtType = None
        self.FileSize = None
        self.FileContent = None


    def _deserialize(self, params):
        self.TableGroupId = params.get("TableGroupId")
        self.TableName = params.get("TableName")
        self.TableInstanceId = params.get("TableInstanceId")
        self.TableIdlType = params.get("TableIdlType")
        self.TableType = params.get("TableType")
        self.ListElementNum = params.get("ListElementNum")
        self.ReservedVolume = params.get("ReservedVolume")
        self.ReservedReadQps = params.get("ReservedReadQps")
        self.ReservedWriteQps = params.get("ReservedWriteQps")
        self.Memo = params.get("Memo")
        self.FileName = params.get("FileName")
        self.FileExtType = params.get("FileExtType")
        self.FileSize = params.get("FileSize")
        self.FileContent = params.get("FileContent")


class TableGroupInfo(AbstractModel):
    """表格組詳細訊息

    """

    def __init__(self):
        """
        :param TableGroupId: 表格組ID
        :type TableGroupId: str
        :param TableGroupName: 表格組名稱
        :type TableGroupName: str
        :param CreatedTime: 表格組創建時間
        :type CreatedTime: str
        :param TableCount: 表格組包含的表格數量
        :type TableCount: int
        :param TotalSize: 表格組包含的表格儲存總量（MB）
        :type TotalSize: int
        """
        self.TableGroupId = None
        self.TableGroupName = None
        self.CreatedTime = None
        self.TableCount = None
        self.TotalSize = None


    def _deserialize(self, params):
        self.TableGroupId = params.get("TableGroupId")
        self.TableGroupName = params.get("TableGroupName")
        self.CreatedTime = params.get("CreatedTime")
        self.TableCount = params.get("TableCount")
        self.TotalSize = params.get("TotalSize")


class TableInfoNew(AbstractModel):
    """表格詳情訊息

    """

    def __init__(self):
        """
        :param TableName: 表格名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type TableName: str
        :param TableInstanceId: 表格實例ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type TableInstanceId: str
        :param TableType: 表格數據結構類型，如：`GENERIC`或`LIST`
注意：此欄位可能返回 null，表示取不到有效值。
        :type TableType: str
        :param TableIdlType: 表格數據描述語言（IDL）類型，如：`PROTO`或`TDR`
注意：此欄位可能返回 null，表示取不到有效值。
        :type TableIdlType: str
        :param ClusterId: 表格所屬集群ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param ClusterName: 表格所屬集群名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param TableGroupId: 表格所屬表格組ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type TableGroupId: str
        :param TableGroupName: 表格所屬表格組名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type TableGroupName: str
        :param KeyStruct: 表格主鍵欄位結構json字串
注意：此欄位可能返回 null，表示取不到有效值。
        :type KeyStruct: str
        :param ValueStruct: 表格非主鍵欄位結構json字串
注意：此欄位可能返回 null，表示取不到有效值。
        :type ValueStruct: str
        :param ShardingKeySet: 表格分表因子集合，對PROTO類型表格有效
注意：此欄位可能返回 null，表示取不到有效值。
        :type ShardingKeySet: str
        :param IndexStruct: 表格索引鍵欄位集合，對PROTO類型表格有效
注意：此欄位可能返回 null，表示取不到有效值。
        :type IndexStruct: str
        :param ListElementNum: LIST類型表格元素個數
注意：此欄位可能返回 null，表示取不到有效值。
        :type ListElementNum: int
        :param IdlFiles: 表格所關聯IDL文件訊息清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type IdlFiles: list of IdlFileInfo
        :param ReservedVolume: 表格預留容量（GB）
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReservedVolume: int
        :param ReservedReadQps: 表格預留讀QPS
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReservedReadQps: int
        :param ReservedWriteQps: 表格預留寫QPS
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReservedWriteQps: int
        :param TableSize: 表格實際數據量大小（MB）
注意：此欄位可能返回 null，表示取不到有效值。
        :type TableSize: int
        :param Status: 表格狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: str
        :param CreatedTime: 表格創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param UpdatedTime: 表格最後一次修改時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type UpdatedTime: str
        :param Memo: 表格備注訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Memo: str
        :param Error: 錯誤訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Error: :class:`taifucloudcloud.tcaplusdb.v20190823.models.ErrorInfo`
        :param ApiAccessId: TcaplusDB SDK數據訪問接入ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ApiAccessId: str
        :param SortFieldNum: SORTLIST類型表格排序欄位個數
注意：此欄位可能返回 null，表示取不到有效值。
        :type SortFieldNum: int
        :param SortRule: SORTLIST類型表格排序順序
注意：此欄位可能返回 null，表示取不到有效值。
        :type SortRule: int
        :param DbClusterInfoStruct: 表格分布式索引訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type DbClusterInfoStruct: str
        """
        self.TableName = None
        self.TableInstanceId = None
        self.TableType = None
        self.TableIdlType = None
        self.ClusterId = None
        self.ClusterName = None
        self.TableGroupId = None
        self.TableGroupName = None
        self.KeyStruct = None
        self.ValueStruct = None
        self.ShardingKeySet = None
        self.IndexStruct = None
        self.ListElementNum = None
        self.IdlFiles = None
        self.ReservedVolume = None
        self.ReservedReadQps = None
        self.ReservedWriteQps = None
        self.TableSize = None
        self.Status = None
        self.CreatedTime = None
        self.UpdatedTime = None
        self.Memo = None
        self.Error = None
        self.ApiAccessId = None
        self.SortFieldNum = None
        self.SortRule = None
        self.DbClusterInfoStruct = None


    def _deserialize(self, params):
        self.TableName = params.get("TableName")
        self.TableInstanceId = params.get("TableInstanceId")
        self.TableType = params.get("TableType")
        self.TableIdlType = params.get("TableIdlType")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.TableGroupId = params.get("TableGroupId")
        self.TableGroupName = params.get("TableGroupName")
        self.KeyStruct = params.get("KeyStruct")
        self.ValueStruct = params.get("ValueStruct")
        self.ShardingKeySet = params.get("ShardingKeySet")
        self.IndexStruct = params.get("IndexStruct")
        self.ListElementNum = params.get("ListElementNum")
        if params.get("IdlFiles") is not None:
            self.IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.IdlFiles.append(obj)
        self.ReservedVolume = params.get("ReservedVolume")
        self.ReservedReadQps = params.get("ReservedReadQps")
        self.ReservedWriteQps = params.get("ReservedWriteQps")
        self.TableSize = params.get("TableSize")
        self.Status = params.get("Status")
        self.CreatedTime = params.get("CreatedTime")
        self.UpdatedTime = params.get("UpdatedTime")
        self.Memo = params.get("Memo")
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        self.ApiAccessId = params.get("ApiAccessId")
        self.SortFieldNum = params.get("SortFieldNum")
        self.SortRule = params.get("SortRule")
        self.DbClusterInfoStruct = params.get("DbClusterInfoStruct")


class TableResultNew(AbstractModel):
    """表處理結果訊息

    """

    def __init__(self):
        """
        :param TableInstanceId: 表格實例ID，形如：tcaplus-3be64cbb
注意：此欄位可能返回 null，表示取不到有效值。
        :type TableInstanceId: str
        :param TaskId: 任務ID，對于創建單任務的介面有效
注意：此欄位可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param TableName: 表格名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type TableName: str
        :param TableType: 表格數據結構類型，如：`GENERIC`或`LIST`
注意：此欄位可能返回 null，表示取不到有效值。
        :type TableType: str
        :param TableIdlType: 表數據描述語言（IDL）類型，如：`PROTO`或`TDR`
注意：此欄位可能返回 null，表示取不到有效值。
        :type TableIdlType: str
        :param TableGroupId: 表格所屬表格組ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type TableGroupId: str
        :param Error: 錯誤訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Error: :class:`taifucloudcloud.tcaplusdb.v20190823.models.ErrorInfo`
        :param TaskIds: 任務ID清單，對于創建多任務的介面有效
注意：此欄位可能返回 null，表示取不到有效值。
        :type TaskIds: list of str
        """
        self.TableInstanceId = None
        self.TaskId = None
        self.TableName = None
        self.TableType = None
        self.TableIdlType = None
        self.TableGroupId = None
        self.Error = None
        self.TaskIds = None


    def _deserialize(self, params):
        self.TableInstanceId = params.get("TableInstanceId")
        self.TaskId = params.get("TaskId")
        self.TableName = params.get("TableName")
        self.TableType = params.get("TableType")
        self.TableIdlType = params.get("TableIdlType")
        self.TableGroupId = params.get("TableGroupId")
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        self.TaskIds = params.get("TaskIds")


class TableRollbackResultNew(AbstractModel):
    """表格回檔結果訊息

    """

    def __init__(self):
        """
        :param TableInstanceId: 表格實例ID，形如：tcaplus-3be64cbb
注意：此欄位可能返回 null，表示取不到有效值。
        :type TableInstanceId: str
        :param TaskId: 任務ID，對于創建單任務的介面有效
注意：此欄位可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param TableName: 表格名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type TableName: str
        :param TableType: 表格數據結構類型，如：`GENERIC`或`LIST`
注意：此欄位可能返回 null，表示取不到有效值。
        :type TableType: str
        :param TableIdlType: 表格數據描述語言（IDL）類型，如：`PROTO`或`TDR`
注意：此欄位可能返回 null，表示取不到有效值。
        :type TableIdlType: str
        :param TableGroupId: 表格所屬表格組ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type TableGroupId: str
        :param Error: 錯誤訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Error: :class:`taifucloudcloud.tcaplusdb.v20190823.models.ErrorInfo`
        :param TaskIds: 任務ID清單，對于創建多任務的介面有效
注意：此欄位可能返回 null，表示取不到有效值。
        :type TaskIds: list of str
        :param FileId: 上傳的key文件ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileId: str
        :param SuccKeyNum: 校驗成功Key數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type SuccKeyNum: int
        :param TotalKeyNum: Key文件中包含總的Key數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalKeyNum: int
        """
        self.TableInstanceId = None
        self.TaskId = None
        self.TableName = None
        self.TableType = None
        self.TableIdlType = None
        self.TableGroupId = None
        self.Error = None
        self.TaskIds = None
        self.FileId = None
        self.SuccKeyNum = None
        self.TotalKeyNum = None


    def _deserialize(self, params):
        self.TableInstanceId = params.get("TableInstanceId")
        self.TaskId = params.get("TaskId")
        self.TableName = params.get("TableName")
        self.TableType = params.get("TableType")
        self.TableIdlType = params.get("TableIdlType")
        self.TableGroupId = params.get("TableGroupId")
        if params.get("Error") is not None:
            self.Error = ErrorInfo()
            self.Error._deserialize(params.get("Error"))
        self.TaskIds = params.get("TaskIds")
        self.FileId = params.get("FileId")
        self.SuccKeyNum = params.get("SuccKeyNum")
        self.TotalKeyNum = params.get("TotalKeyNum")


class TaskInfoNew(AbstractModel):
    """任務訊息詳情

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: str
        :param TaskType: 任務類型
        :type TaskType: str
        :param TransId: 任務所關聯的TcaplusDB内部事務ID
        :type TransId: str
        :param ClusterId: 任務所屬集群ID
        :type ClusterId: str
        :param ClusterName: 任務所屬集群名稱
        :type ClusterName: str
        :param Progress: 任務進度
        :type Progress: int
        :param StartTime: 任務創建時間
        :type StartTime: str
        :param UpdateTime: 任務最後更新時間
        :type UpdateTime: str
        :param Operator: 操作者
        :type Operator: str
        :param Content: 任務詳情
        :type Content: str
        """
        self.TaskId = None
        self.TaskType = None
        self.TransId = None
        self.ClusterId = None
        self.ClusterName = None
        self.Progress = None
        self.StartTime = None
        self.UpdateTime = None
        self.Operator = None
        self.Content = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskType = params.get("TaskType")
        self.TransId = params.get("TransId")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.Progress = params.get("Progress")
        self.StartTime = params.get("StartTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Operator = params.get("Operator")
        self.Content = params.get("Content")


class VerifyIdlFilesRequest(AbstractModel):
    """VerifyIdlFiles請求參數結構體

    """

    def __init__(self):
        """
        :param ClusterId: 待創建表格的集群ID
        :type ClusterId: str
        :param TableGroupId: 待創建表格的表格組ID
        :type TableGroupId: str
        :param ExistingIdlFiles: 曾經上傳過的IDL文件訊息清單，與NewIdlFiles至少有一者
        :type ExistingIdlFiles: list of IdlFileInfo
        :param NewIdlFiles: 待上傳的IDL文件訊息清單，與ExistingIdlFiles至少有一者
        :type NewIdlFiles: list of IdlFileInfo
        """
        self.ClusterId = None
        self.TableGroupId = None
        self.ExistingIdlFiles = None
        self.NewIdlFiles = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TableGroupId = params.get("TableGroupId")
        if params.get("ExistingIdlFiles") is not None:
            self.ExistingIdlFiles = []
            for item in params.get("ExistingIdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.ExistingIdlFiles.append(obj)
        if params.get("NewIdlFiles") is not None:
            self.NewIdlFiles = []
            for item in params.get("NewIdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.NewIdlFiles.append(obj)


class VerifyIdlFilesResponse(AbstractModel):
    """VerifyIdlFiles返回參數結構體

    """

    def __init__(self):
        """
        :param IdlFiles: 本次上傳校驗所有的IDL文件訊息清單
        :type IdlFiles: list of IdlFileInfo
        :param TotalCount: 讀取IDL描述文件後解析出的合法表數量，不包含已經創建的表
        :type TotalCount: int
        :param TableInfos: 讀取IDL描述文件後解析出的合法表清單，不包含已經創建的表
        :type TableInfos: list of ParsedTableInfoNew
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.IdlFiles = None
        self.TotalCount = None
        self.TableInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("IdlFiles") is not None:
            self.IdlFiles = []
            for item in params.get("IdlFiles"):
                obj = IdlFileInfo()
                obj._deserialize(item)
                self.IdlFiles.append(obj)
        self.TotalCount = params.get("TotalCount")
        if params.get("TableInfos") is not None:
            self.TableInfos = []
            for item in params.get("TableInfos"):
                obj = ParsedTableInfoNew()
                obj._deserialize(item)
                self.TableInfos.append(obj)
        self.RequestId = params.get("RequestId")