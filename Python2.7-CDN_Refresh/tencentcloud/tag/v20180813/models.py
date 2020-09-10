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


class AddResourceTagRequest(AbstractModel):
    """AddResourceTag請求參數結構體

    """

    def __init__(self):
        """
        :param TagKey: 标簽鍵
        :type TagKey: str
        :param TagValue: 标簽值
        :type TagValue: str
        :param Resource: 資源六段式描述
        :type Resource: str
        """
        self.TagKey = None
        self.TagValue = None
        self.Resource = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        self.Resource = params.get("Resource")


class AddResourceTagResponse(AbstractModel):
    """AddResourceTag返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTagRequest(AbstractModel):
    """CreateTag請求參數結構體

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


class CreateTagResponse(AbstractModel):
    """CreateTag返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteResourceTagRequest(AbstractModel):
    """DeleteResourceTag請求參數結構體

    """

    def __init__(self):
        """
        :param TagKey: 标簽鍵
        :type TagKey: str
        :param Resource: 資源六段式描述
        :type Resource: str
        """
        self.TagKey = None
        self.Resource = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.Resource = params.get("Resource")


class DeleteResourceTagResponse(AbstractModel):
    """DeleteResourceTag返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTagRequest(AbstractModel):
    """DeleteTag請求參數結構體

    """

    def __init__(self):
        """
        :param TagKey: 需要删除的标簽鍵
        :type TagKey: str
        :param TagValue: 需要删除的标簽值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class DeleteTagResponse(AbstractModel):
    """DeleteTag返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeResourceTagsByResourceIdsRequest(AbstractModel):
    """DescribeResourceTagsByResourceIds請求參數結構體

    """

    def __init__(self):
        """
        :param ServiceType: 業務類型
        :type ServiceType: str
        :param ResourcePrefix: 資源前綴
        :type ResourcePrefix: str
        :param ResourceIds: 資源唯一标記
        :type ResourceIds: list of str
        :param ResourceRegion: 資源所在地域
        :type ResourceRegion: str
        :param Offset: 數據偏移量，預設爲 0, 必須爲Limit參數的整數倍
        :type Offset: int
        :param Limit: 每頁大小，預設爲 15
        :type Limit: int
        """
        self.ServiceType = None
        self.ResourcePrefix = None
        self.ResourceIds = None
        self.ResourceRegion = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ServiceType = params.get("ServiceType")
        self.ResourcePrefix = params.get("ResourcePrefix")
        self.ResourceIds = params.get("ResourceIds")
        self.ResourceRegion = params.get("ResourceRegion")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeResourceTagsByResourceIdsResponse(AbstractModel):
    """DescribeResourceTagsByResourceIds返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 結果總數
        :type TotalCount: int
        :param Offset: 數據位移偏量
        :type Offset: int
        :param Limit: 每頁大小
        :type Limit: int
        :param Tags: 标簽清單
        :type Tags: list of TagResource
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagResource()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResourceTagsByTagKeysRequest(AbstractModel):
    """DescribeResourceTagsByTagKeys請求參數結構體

    """

    def __init__(self):
        """
        :param ServiceType: 業務類型
        :type ServiceType: str
        :param ResourcePrefix: 資源前綴
        :type ResourcePrefix: str
        :param ResourceRegion: 資源地域
        :type ResourceRegion: str
        :param ResourceIds: 資源唯一标識
        :type ResourceIds: list of str
        :param TagKeys: 資源标簽鍵
        :type TagKeys: list of str
        :param Limit: 每頁大小，預設爲 400
        :type Limit: int
        :param Offset: 數據偏移量，預設爲 0, 必須爲Limit參數的整數倍
        :type Offset: int
        """
        self.ServiceType = None
        self.ResourcePrefix = None
        self.ResourceRegion = None
        self.ResourceIds = None
        self.TagKeys = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceType = params.get("ServiceType")
        self.ResourcePrefix = params.get("ResourcePrefix")
        self.ResourceRegion = params.get("ResourceRegion")
        self.ResourceIds = params.get("ResourceIds")
        self.TagKeys = params.get("TagKeys")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeResourceTagsByTagKeysResponse(AbstractModel):
    """DescribeResourceTagsByTagKeys返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 結果總數
        :type TotalCount: int
        :param Offset: 數據位移偏量
        :type Offset: int
        :param Limit: 每頁大小
        :type Limit: int
        :param Rows: 資源标簽
        :type Rows: list of ResourceIdTag
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Rows = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Rows") is not None:
            self.Rows = []
            for item in params.get("Rows"):
                obj = ResourceIdTag()
                obj._deserialize(item)
                self.Rows.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResourceTagsRequest(AbstractModel):
    """DescribeResourceTags請求參數結構體

    """

    def __init__(self):
        """
        :param CreateUin: 創建者uin
        :type CreateUin: int
        :param ResourceRegion: 資源所在地域
        :type ResourceRegion: str
        :param ServiceType: 業務類型
        :type ServiceType: str
        :param ResourcePrefix: 資源前綴
        :type ResourcePrefix: str
        :param ResourceId: 資源唯一标識
        :type ResourceId: str
        :param Offset: 數據偏移量，預設爲 0, 必須爲Limit參數的整數倍
        :type Offset: int
        :param Limit: 每頁大小，預設爲 15
        :type Limit: int
        :param CosResourceId: 是否是Cos的資源id
        :type CosResourceId: int
        """
        self.CreateUin = None
        self.ResourceRegion = None
        self.ServiceType = None
        self.ResourcePrefix = None
        self.ResourceId = None
        self.Offset = None
        self.Limit = None
        self.CosResourceId = None


    def _deserialize(self, params):
        self.CreateUin = params.get("CreateUin")
        self.ResourceRegion = params.get("ResourceRegion")
        self.ServiceType = params.get("ServiceType")
        self.ResourcePrefix = params.get("ResourcePrefix")
        self.ResourceId = params.get("ResourceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.CosResourceId = params.get("CosResourceId")


class DescribeResourceTagsResponse(AbstractModel):
    """DescribeResourceTags返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 結果總數
        :type TotalCount: int
        :param Offset: 數據位移偏量
        :type Offset: int
        :param Limit: 每頁大小
注意：此欄位可能返回 null，表示取不到有效值。
        :type Limit: int
        :param Rows: 資源标簽
        :type Rows: list of TagResource
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Rows = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Rows") is not None:
            self.Rows = []
            for item in params.get("Rows"):
                obj = TagResource()
                obj._deserialize(item)
                self.Rows.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResourcesByTagsRequest(AbstractModel):
    """DescribeResourcesByTags請求參數結構體

    """

    def __init__(self):
        """
        :param TagFilters: 标簽過濾數組
        :type TagFilters: list of TagFilter
        :param CreateUin: 創建标簽者uin
        :type CreateUin: int
        :param Offset: 數據偏移量，預設爲 0, 必須爲Limit參數的整數倍
        :type Offset: int
        :param Limit: 每頁大小，預設爲 15
        :type Limit: int
        :param ResourcePrefix: 資源前綴
        :type ResourcePrefix: str
        :param ResourceId: 資源唯一标記
        :type ResourceId: str
        :param ResourceRegion: 資源所在地域
        :type ResourceRegion: str
        :param ServiceType: 業務類型
        :type ServiceType: str
        """
        self.TagFilters = None
        self.CreateUin = None
        self.Offset = None
        self.Limit = None
        self.ResourcePrefix = None
        self.ResourceId = None
        self.ResourceRegion = None
        self.ServiceType = None


    def _deserialize(self, params):
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        self.CreateUin = params.get("CreateUin")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ResourcePrefix = params.get("ResourcePrefix")
        self.ResourceId = params.get("ResourceId")
        self.ResourceRegion = params.get("ResourceRegion")
        self.ServiceType = params.get("ServiceType")


class DescribeResourcesByTagsResponse(AbstractModel):
    """DescribeResourcesByTags返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 結果總數
        :type TotalCount: int
        :param Offset: 數據位移偏量
        :type Offset: int
        :param Limit: 每頁大小
注意：此欄位可能返回 null，表示取不到有效值。
        :type Limit: int
        :param Rows: 資源标簽
        :type Rows: list of ResourceTag
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Rows = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Rows") is not None:
            self.Rows = []
            for item in params.get("Rows"):
                obj = ResourceTag()
                obj._deserialize(item)
                self.Rows.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTagKeysRequest(AbstractModel):
    """DescribeTagKeys請求參數結構體

    """

    def __init__(self):
        """
        :param CreateUin: 創建者用戶 Uin，不傳或爲空只将 Uin 作爲條件查詢
        :type CreateUin: int
        :param Offset: 數據偏移量，預設爲 0, 必須爲Limit參數的整數倍
        :type Offset: int
        :param Limit: 每頁大小，預設爲 15
        :type Limit: int
        :param ShowProject: 是否展現項目
        :type ShowProject: int
        """
        self.CreateUin = None
        self.Offset = None
        self.Limit = None
        self.ShowProject = None


    def _deserialize(self, params):
        self.CreateUin = params.get("CreateUin")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ShowProject = params.get("ShowProject")


class DescribeTagKeysResponse(AbstractModel):
    """DescribeTagKeys返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 結果總數
        :type TotalCount: int
        :param Offset: 數據位移偏量
        :type Offset: int
        :param Limit: 每頁大小
        :type Limit: int
        :param Tags: 标簽清單
        :type Tags: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Tags = params.get("Tags")
        self.RequestId = params.get("RequestId")


class DescribeTagValuesRequest(AbstractModel):
    """DescribeTagValues請求參數結構體

    """

    def __init__(self):
        """
        :param TagKeys: 标簽鍵清單
        :type TagKeys: list of str
        :param CreateUin: 創建者用戶 Uin，不傳或爲空只将 Uin 作爲條件查詢
        :type CreateUin: int
        :param Offset: 數據偏移量，預設爲 0, 必須爲Limit參數的整數倍
        :type Offset: int
        :param Limit: 每頁大小，預設爲 15
        :type Limit: int
        """
        self.TagKeys = None
        self.CreateUin = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.TagKeys = params.get("TagKeys")
        self.CreateUin = params.get("CreateUin")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTagValuesResponse(AbstractModel):
    """DescribeTagValues返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 結果總數
        :type TotalCount: int
        :param Offset: 數據位移偏量
        :type Offset: int
        :param Limit: 每頁大小
        :type Limit: int
        :param Tags: 标簽清單
        :type Tags: list of Tag
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTagsRequest(AbstractModel):
    """DescribeTags請求參數結構體

    """

    def __init__(self):
        """
        :param TagKey: 标簽鍵,與标簽值同時存在或同時不存在，不存在時表示查詢該用戶所有标簽
        :type TagKey: str
        :param TagValue: 标簽值,與标簽鍵同時存在或同時不存在，不存在時表示查詢該用戶所有标簽
        :type TagValue: str
        :param Offset: 數據偏移量，預設爲 0, 必須爲Limit參數的整數倍
        :type Offset: int
        :param Limit: 每頁大小，預設爲 15
        :type Limit: int
        :param CreateUin: 創建者用戶 Uin，不傳或爲空只将 Uin 作爲條件查詢
        :type CreateUin: int
        :param TagKeys: 标簽鍵數組,與标簽值同時存在或同時不存在，不存在時表示查詢該用戶所有标簽,當與TagKey同時傳遞時只會本值
        :type TagKeys: list of str
        :param ShowProject: 是否展現項目标簽
        :type ShowProject: int
        """
        self.TagKey = None
        self.TagValue = None
        self.Offset = None
        self.Limit = None
        self.CreateUin = None
        self.TagKeys = None
        self.ShowProject = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.CreateUin = params.get("CreateUin")
        self.TagKeys = params.get("TagKeys")
        self.ShowProject = params.get("ShowProject")


class DescribeTagsResponse(AbstractModel):
    """DescribeTags返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 結果總數
        :type TotalCount: int
        :param Offset: 數據位移偏量
        :type Offset: int
        :param Limit: 每頁大小
        :type Limit: int
        :param Tags: 标簽清單
        :type Tags: list of TagWithDelete
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagWithDelete()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyResourceTagsRequest(AbstractModel):
    """ModifyResourceTags請求參數結構體

    """

    def __init__(self):
        """
        :param Resource: 資源的六段式描述
        :type Resource: str
        :param ReplaceTags: 需要增加或修改的标簽集合。如果Resource描述的資源未關聯輸入的标簽鍵，則增加關聯；若已關聯，則将該資源關聯的鍵對應的标簽值修改爲輸入值。本介面中ReplaceTags和DeleteTags二者必須存在其一，且二者不能包含相同的标簽鍵
        :type ReplaceTags: list of Tag
        :param DeleteTags: 需要解關聯的标簽集合。本介面中ReplaceTags和DeleteTags二者必須存在其一，且二者不能包含相同的标簽鍵
        :type DeleteTags: list of TagKeyObject
        """
        self.Resource = None
        self.ReplaceTags = None
        self.DeleteTags = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        if params.get("ReplaceTags") is not None:
            self.ReplaceTags = []
            for item in params.get("ReplaceTags"):
                obj = Tag()
                obj._deserialize(item)
                self.ReplaceTags.append(obj)
        if params.get("DeleteTags") is not None:
            self.DeleteTags = []
            for item in params.get("DeleteTags"):
                obj = TagKeyObject()
                obj._deserialize(item)
                self.DeleteTags.append(obj)


class ModifyResourceTagsResponse(AbstractModel):
    """ModifyResourceTags返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResourceIdTag(AbstractModel):
    """資源标簽鍵值

    """

    def __init__(self):
        """
        :param ResourceId: 資源唯一标識
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param TagKeyValues: 标簽鍵值對
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagKeyValues: list of Tag
        """
        self.ResourceId = None
        self.TagKeyValues = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        if params.get("TagKeyValues") is not None:
            self.TagKeyValues = []
            for item in params.get("TagKeyValues"):
                obj = Tag()
                obj._deserialize(item)
                self.TagKeyValues.append(obj)


class ResourceTag(AbstractModel):
    """資源标簽

    """

    def __init__(self):
        """
        :param ResourceRegion: 資源所在地域
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResourceRegion: str
        :param ServiceType: 業務類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type ServiceType: str
        :param ResourcePrefix: 資源前綴
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResourcePrefix: str
        :param ResourceId: 資源唯一标記
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param Tags: 資源标簽
注意：此欄位可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self.ResourceRegion = None
        self.ServiceType = None
        self.ResourcePrefix = None
        self.ResourceId = None
        self.Tags = None


    def _deserialize(self, params):
        self.ResourceRegion = params.get("ResourceRegion")
        self.ServiceType = params.get("ServiceType")
        self.ResourcePrefix = params.get("ResourcePrefix")
        self.ResourceId = params.get("ResourceId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class Tag(AbstractModel):
    """表示一個标簽鍵值對

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


class TagFilter(AbstractModel):
    """tag過濾數組多個是與的關系

    """

    def __init__(self):
        """
        :param TagKey: 标簽鍵
        :type TagKey: str
        :param TagValue: 标簽值數組 多個值的話是或的關系
        :type TagValue: list of str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class TagKeyObject(AbstractModel):
    """标簽鍵對象

    """

    def __init__(self):
        """
        :param TagKey: 标簽鍵
        :type TagKey: str
        """
        self.TagKey = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")


class TagResource(AbstractModel):
    """标簽鍵值對以及資源ID

    """

    def __init__(self):
        """
        :param TagKey: 标簽鍵
        :type TagKey: str
        :param TagValue: 标簽值
        :type TagValue: str
        :param ResourceId: 資源ID
        :type ResourceId: str
        :param TagKeyMd5: 标簽鍵MD5值
        :type TagKeyMd5: str
        :param TagValueMd5: 标簽值MD5值
        :type TagValueMd5: str
        :param ServiceType: 資源類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type ServiceType: str
        """
        self.TagKey = None
        self.TagValue = None
        self.ResourceId = None
        self.TagKeyMd5 = None
        self.TagValueMd5 = None
        self.ServiceType = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        self.ResourceId = params.get("ResourceId")
        self.TagKeyMd5 = params.get("TagKeyMd5")
        self.TagValueMd5 = params.get("TagValueMd5")
        self.ServiceType = params.get("ServiceType")


class TagWithDelete(AbstractModel):
    """表示一個标簽鍵值對以及是否允許删除

    """

    def __init__(self):
        """
        :param TagKey: 标簽鍵
        :type TagKey: str
        :param TagValue: 标簽值
        :type TagValue: str
        :param CanDelete: 是否可以删除
        :type CanDelete: int
        """
        self.TagKey = None
        self.TagValue = None
        self.CanDelete = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        self.CanDelete = params.get("CanDelete")


class UpdateResourceTagValueRequest(AbstractModel):
    """UpdateResourceTagValue請求參數結構體

    """

    def __init__(self):
        """
        :param TagKey: 資源關聯的标簽鍵
        :type TagKey: str
        :param TagValue: 修改後的标簽值
        :type TagValue: str
        :param Resource: 資源的六段式描述
        :type Resource: str
        """
        self.TagKey = None
        self.TagValue = None
        self.Resource = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        self.Resource = params.get("Resource")


class UpdateResourceTagValueResponse(AbstractModel):
    """UpdateResourceTagValue返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")