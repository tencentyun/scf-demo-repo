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


class ControlDeviceDataRequest(AbstractModel):
    """ControlDeviceData請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param Data: 屬性數據
        :type Data: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.Data = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Data = params.get("Data")


class ControlDeviceDataResponse(AbstractModel):
    """ControlDeviceData返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 返回訊息
        :type Data: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class CreateProjectRequest(AbstractModel):
    """CreateProject請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectName: 項目名稱
        :type ProjectName: str
        :param ProjectDesc: 項目描述
        :type ProjectDesc: str
        """
        self.ProjectName = None
        self.ProjectDesc = None


    def _deserialize(self, params):
        self.ProjectName = params.get("ProjectName")
        self.ProjectDesc = params.get("ProjectDesc")


class CreateProjectResponse(AbstractModel):
    """CreateProject返回參數結構體

    """

    def __init__(self):
        """
        :param Project: 返回訊息
        :type Project: :class:`taifucloudcloud.iotexplorer.v20190423.models.ProjectEntry`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Project = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Project") is not None:
            self.Project = ProjectEntry()
            self.Project._deserialize(params.get("Project"))
        self.RequestId = params.get("RequestId")


class CreateStudioProductRequest(AbstractModel):
    """CreateStudioProduct請求參數結構體

    """

    def __init__(self):
        """
        :param ProductName: 産品名稱
        :type ProductName: str
        :param CategoryId: 産品分組範本ID
        :type CategoryId: int
        :param ProductType: 産品類型
        :type ProductType: int
        :param EncryptionType: 加密類型
        :type EncryptionType: str
        :param NetType: 連接類型
        :type NetType: str
        :param DataProtocol: 數據協議
        :type DataProtocol: int
        :param ProductDesc: 産品描述
        :type ProductDesc: str
        :param ProjectId: 産品的項目ID
        :type ProjectId: str
        """
        self.ProductName = None
        self.CategoryId = None
        self.ProductType = None
        self.EncryptionType = None
        self.NetType = None
        self.DataProtocol = None
        self.ProductDesc = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProductName = params.get("ProductName")
        self.CategoryId = params.get("CategoryId")
        self.ProductType = params.get("ProductType")
        self.EncryptionType = params.get("EncryptionType")
        self.NetType = params.get("NetType")
        self.DataProtocol = params.get("DataProtocol")
        self.ProductDesc = params.get("ProductDesc")
        self.ProjectId = params.get("ProjectId")


class CreateStudioProductResponse(AbstractModel):
    """CreateStudioProduct返回參數結構體

    """

    def __init__(self):
        """
        :param Product: 産品描述
        :type Product: :class:`taifucloudcloud.iotexplorer.v20190423.models.ProductEntry`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Product = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Product") is not None:
            self.Product = ProductEntry()
            self.Product._deserialize(params.get("Product"))
        self.RequestId = params.get("RequestId")


class DeleteProjectRequest(AbstractModel):
    """DeleteProject請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: 項目ID
        :type ProjectId: int
        """
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")


class DeleteProjectResponse(AbstractModel):
    """DeleteProject返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteStudioProductRequest(AbstractModel):
    """DeleteStudioProduct請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class DeleteStudioProductResponse(AbstractModel):
    """DeleteStudioProduct返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDeviceDataHistoryRequest(AbstractModel):
    """DescribeDeviceDataHistory請求參數結構體

    """

    def __init__(self):
        """
        :param MinTime: 區間開始時間
        :type MinTime: int
        :param MaxTime: 區間結束時間
        :type MaxTime: int
        :param ProductId: 産品ID
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param FieldName: 屬性欄位名稱
        :type FieldName: str
        :param Limit: 返回條數
        :type Limit: int
        :param Context: 檢索上下文
        :type Context: str
        """
        self.MinTime = None
        self.MaxTime = None
        self.ProductId = None
        self.DeviceName = None
        self.FieldName = None
        self.Limit = None
        self.Context = None


    def _deserialize(self, params):
        self.MinTime = params.get("MinTime")
        self.MaxTime = params.get("MaxTime")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.FieldName = params.get("FieldName")
        self.Limit = params.get("Limit")
        self.Context = params.get("Context")


class DescribeDeviceDataHistoryResponse(AbstractModel):
    """DescribeDeviceDataHistory返回參數結構體

    """

    def __init__(self):
        """
        :param FieldName: 屬性欄位名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type FieldName: str
        :param Listover: 數據是否已全部返回，true 表示數據全部返回，false 表示還有數據待返回，可将 Context 作爲入參，繼續查詢返回結果。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Listover: bool
        :param Context: 檢索上下文，當 ListOver 爲false時，可以用此上下文，繼續讀取後續數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type Context: str
        :param Results: 曆史數據結果數組，返回對應時間點及取值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Results: list of DeviceDataHistoryItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FieldName = None
        self.Listover = None
        self.Context = None
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FieldName = params.get("FieldName")
        self.Listover = params.get("Listover")
        self.Context = params.get("Context")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = DeviceDataHistoryItem()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceDataRequest(AbstractModel):
    """DescribeDeviceData請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class DescribeDeviceDataResponse(AbstractModel):
    """DescribeDeviceData返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 設備數據
        :type Data: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeModelDefinitionRequest(AbstractModel):
    """DescribeModelDefinition請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class DescribeModelDefinitionResponse(AbstractModel):
    """DescribeModelDefinition返回參數結構體

    """

    def __init__(self):
        """
        :param Model: 産品數據範本
        :type Model: :class:`taifucloudcloud.iotexplorer.v20190423.models.ProductModelDefinition`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Model = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self.Model = ProductModelDefinition()
            self.Model._deserialize(params.get("Model"))
        self.RequestId = params.get("RequestId")


class DescribeProjectRequest(AbstractModel):
    """DescribeProject請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: 項目ID
        :type ProjectId: int
        """
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")


class DescribeProjectResponse(AbstractModel):
    """DescribeProject返回參數結構體

    """

    def __init__(self):
        """
        :param Project: 返回訊息
        :type Project: :class:`taifucloudcloud.iotexplorer.v20190423.models.ProjectEntryEx`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Project = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Project") is not None:
            self.Project = ProjectEntryEx()
            self.Project._deserialize(params.get("Project"))
        self.RequestId = params.get("RequestId")


class DescribeStudioProductRequest(AbstractModel):
    """DescribeStudioProduct請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class DescribeStudioProductResponse(AbstractModel):
    """DescribeStudioProduct返回參數結構體

    """

    def __init__(self):
        """
        :param Product: 産品詳情
        :type Product: :class:`taifucloudcloud.iotexplorer.v20190423.models.ProductEntry`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Product = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Product") is not None:
            self.Product = ProductEntry()
            self.Product._deserialize(params.get("Product"))
        self.RequestId = params.get("RequestId")


class DeviceDataHistoryItem(AbstractModel):
    """設備曆史數據結構

    """

    def __init__(self):
        """
        :param Time: 時間點，毫秒時間戳
        :type Time: str
        :param Value: 欄位取值
        :type Value: str
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")


class GetProjectListRequest(AbstractModel):
    """GetProjectList請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 個數限制
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetProjectListResponse(AbstractModel):
    """GetProjectList返回參數結構體

    """

    def __init__(self):
        """
        :param Projects: 項目清單
        :type Projects: list of ProjectEntryEx
        :param Total: 清單項個數
        :type Total: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Projects = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Projects") is not None:
            self.Projects = []
            for item in params.get("Projects"):
                obj = ProjectEntryEx()
                obj._deserialize(item)
                self.Projects.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class GetStudioProductListRequest(AbstractModel):
    """GetStudioProductList請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: 項目ID
        :type ProjectId: str
        :param DevStatus: 産品DevStatus
        :type DevStatus: str
        :param Offset: Offset
        :type Offset: int
        :param Limit: Limit
        :type Limit: int
        """
        self.ProjectId = None
        self.DevStatus = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.DevStatus = params.get("DevStatus")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetStudioProductListResponse(AbstractModel):
    """GetStudioProductList返回參數結構體

    """

    def __init__(self):
        """
        :param Products: 産品清單
        :type Products: list of ProductEntry
        :param Total: 産品數量
        :type Total: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Products = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Products") is not None:
            self.Products = []
            for item in params.get("Products"):
                obj = ProductEntry()
                obj._deserialize(item)
                self.Products.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class ModifyModelDefinitionRequest(AbstractModel):
    """ModifyModelDefinition請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param ModelSchema: 數據範本定義
        :type ModelSchema: str
        """
        self.ProductId = None
        self.ModelSchema = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ModelSchema = params.get("ModelSchema")


class ModifyModelDefinitionResponse(AbstractModel):
    """ModifyModelDefinition返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyProjectRequest(AbstractModel):
    """ModifyProject請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: 項目ID
        :type ProjectId: int
        :param ProjectName: 項目名稱
        :type ProjectName: str
        :param ProjectDesc: 項目描述
        :type ProjectDesc: str
        """
        self.ProjectId = None
        self.ProjectName = None
        self.ProjectDesc = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.ProjectDesc = params.get("ProjectDesc")


class ModifyProjectResponse(AbstractModel):
    """ModifyProject返回參數結構體

    """

    def __init__(self):
        """
        :param Project: 項目詳情
        :type Project: :class:`taifucloudcloud.iotexplorer.v20190423.models.ProjectEntry`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Project = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Project") is not None:
            self.Project = ProjectEntry()
            self.Project._deserialize(params.get("Project"))
        self.RequestId = params.get("RequestId")


class ModifyStudioProductRequest(AbstractModel):
    """ModifyStudioProduct請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param ProductName: 産品名稱
        :type ProductName: str
        :param ProductDesc: 産品描述
        :type ProductDesc: str
        :param ModuleId: 模型ID
        :type ModuleId: int
        """
        self.ProductId = None
        self.ProductName = None
        self.ProductDesc = None
        self.ModuleId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.ProductDesc = params.get("ProductDesc")
        self.ModuleId = params.get("ModuleId")


class ModifyStudioProductResponse(AbstractModel):
    """ModifyStudioProduct返回參數結構體

    """

    def __init__(self):
        """
        :param Product: 産品描述
        :type Product: :class:`taifucloudcloud.iotexplorer.v20190423.models.ProductEntry`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Product = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Product") is not None:
            self.Product = ProductEntry()
            self.Product._deserialize(params.get("Product"))
        self.RequestId = params.get("RequestId")


class ProductEntry(AbstractModel):
    """産品詳情

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param ProductName: 産品名稱
        :type ProductName: str
        :param CategoryId: 産品分組範本ID
        :type CategoryId: int
        :param EncryptionType: 加密類型
        :type EncryptionType: str
        :param NetType: 連接類型
        :type NetType: str
        :param DataProtocol: 數據協議
        :type DataProtocol: int
        :param ProductDesc: 産品描述
        :type ProductDesc: str
        :param DevStatus: 狀态
        :type DevStatus: str
        :param CreateTime: 創建時間
        :type CreateTime: int
        :param UpdateTime: 更新時間
        :type UpdateTime: int
        :param Region: 區域
        :type Region: str
        :param ProductType: 産品類型
        :type ProductType: int
        :param ProjectId: 項目ID
        :type ProjectId: str
        :param ModuleId: 産品ModuleId
        :type ModuleId: int
        """
        self.ProductId = None
        self.ProductName = None
        self.CategoryId = None
        self.EncryptionType = None
        self.NetType = None
        self.DataProtocol = None
        self.ProductDesc = None
        self.DevStatus = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Region = None
        self.ProductType = None
        self.ProjectId = None
        self.ModuleId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.CategoryId = params.get("CategoryId")
        self.EncryptionType = params.get("EncryptionType")
        self.NetType = params.get("NetType")
        self.DataProtocol = params.get("DataProtocol")
        self.ProductDesc = params.get("ProductDesc")
        self.DevStatus = params.get("DevStatus")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Region = params.get("Region")
        self.ProductType = params.get("ProductType")
        self.ProjectId = params.get("ProjectId")
        self.ModuleId = params.get("ModuleId")


class ProductModelDefinition(AbstractModel):
    """産品模型定義

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param ModelDefine: 模型定義
        :type ModelDefine: str
        :param UpdateTime: 更新時間，秒級時間戳
        :type UpdateTime: int
        :param CreateTime: 創建時間，秒級時間戳
        :type CreateTime: int
        """
        self.ProductId = None
        self.ModelDefine = None
        self.UpdateTime = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ModelDefine = params.get("ModelDefine")
        self.UpdateTime = params.get("UpdateTime")
        self.CreateTime = params.get("CreateTime")


class ProjectEntry(AbstractModel):
    """項目詳情

    """

    def __init__(self):
        """
        :param ProjectId: 項目ID
        :type ProjectId: int
        :param ProjectName: 項目名稱
        :type ProjectName: str
        :param ProjectDesc: 項目描述
        :type ProjectDesc: str
        :param CreateTime: 創建時間，unix時間戳
        :type CreateTime: int
        :param UpdateTime: 更新時間，unix時間戳
        :type UpdateTime: int
        """
        self.ProjectId = None
        self.ProjectName = None
        self.ProjectDesc = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.ProjectDesc = params.get("ProjectDesc")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class ProjectEntryEx(AbstractModel):
    """項目詳情

    """

    def __init__(self):
        """
        :param ProjectId: 項目ID
        :type ProjectId: int
        :param ProjectName: 項目名稱
        :type ProjectName: str
        :param ProjectDesc: 項目描述
        :type ProjectDesc: str
        :param CreateTime: 項目創建時間，unix時間戳
        :type CreateTime: int
        :param UpdateTime: 項目更新時間，unix時間戳
        :type UpdateTime: int
        :param ProductCount: 産品數量
        :type ProductCount: int
        :param NativeAppCount: NativeApp數量
        :type NativeAppCount: int
        :param WebAppCount: WebApp數量
        :type WebAppCount: int
        """
        self.ProjectId = None
        self.ProjectName = None
        self.ProjectDesc = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ProductCount = None
        self.NativeAppCount = None
        self.WebAppCount = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.ProjectDesc = params.get("ProjectDesc")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ProductCount = params.get("ProductCount")
        self.NativeAppCount = params.get("NativeAppCount")
        self.WebAppCount = params.get("WebAppCount")


class ReleaseStudioProductRequest(AbstractModel):
    """ReleaseStudioProduct請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param DevStatus: 産品DevStatus
        :type DevStatus: str
        """
        self.ProductId = None
        self.DevStatus = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DevStatus = params.get("DevStatus")


class ReleaseStudioProductResponse(AbstractModel):
    """ReleaseStudioProduct返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SearchStudioProductRequest(AbstractModel):
    """SearchStudioProduct請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: 項目ID
        :type ProjectId: str
        :param ProductName: 産品名稱
        :type ProductName: str
        :param Limit: 清單Limit
        :type Limit: int
        :param Offset: 清單Offset
        :type Offset: int
        """
        self.ProjectId = None
        self.ProductName = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProductName = params.get("ProductName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class SearchStudioProductResponse(AbstractModel):
    """SearchStudioProduct返回參數結構體

    """

    def __init__(self):
        """
        :param Products: 産品清單
        :type Products: list of ProductEntry
        :param Total: 産品數量
        :type Total: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Products = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Products") is not None:
            self.Products = []
            for item in params.get("Products"):
                obj = ProductEntry()
                obj._deserialize(item)
                self.Products.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")