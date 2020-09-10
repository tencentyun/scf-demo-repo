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


class DescribeEntityRequest(AbstractModel):
    """DescribeEntity請求參數結構體

    """

    def __init__(self):
        """
        :param EntityName: 實體名稱
        :type EntityName: str
        """
        self.EntityName = None


    def _deserialize(self, params):
        self.EntityName = params.get("EntityName")


class DescribeEntityResponse(AbstractModel):
    """DescribeEntity返回參數結構體

    """

    def __init__(self):
        """
        :param Content: 返回查詢實體相關訊息
        :type Content: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Content = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.RequestId = params.get("RequestId")


class DescribeRelationRequest(AbstractModel):
    """DescribeRelation請求參數結構體

    """

    def __init__(self):
        """
        :param LeftEntityName: 輸入第一個實體
        :type LeftEntityName: str
        :param RightEntityName: 輸入第二個實體
        :type RightEntityName: str
        """
        self.LeftEntityName = None
        self.RightEntityName = None


    def _deserialize(self, params):
        self.LeftEntityName = params.get("LeftEntityName")
        self.RightEntityName = params.get("RightEntityName")


class DescribeRelationResponse(AbstractModel):
    """DescribeRelation返回參數結構體

    """

    def __init__(self):
        """
        :param Content: 返回查詢實體間的關系
        :type Content: list of EntityRelationContent
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Content = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = EntityRelationContent()
                obj._deserialize(item)
                self.Content.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTripleRequest(AbstractModel):
    """DescribeTriple請求參數結構體

    """

    def __init__(self):
        """
        :param TripleCondition: 三元組查詢條件
        :type TripleCondition: str
        """
        self.TripleCondition = None


    def _deserialize(self, params):
        self.TripleCondition = params.get("TripleCondition")


class DescribeTripleResponse(AbstractModel):
    """DescribeTriple返回參數結構體

    """

    def __init__(self):
        """
        :param Content: 返回三元組訊息
        :type Content: list of TripleContent
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Content = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = TripleContent()
                obj._deserialize(item)
                self.Content.append(obj)
        self.RequestId = params.get("RequestId")


class EntityRelationContent(AbstractModel):
    """返回的實體關系查詢結果詳細内容

    """

    def __init__(self):
        """
        :param Object: 實體關系查詢返回關系的object
        :type Object: list of EntityRelationObject
        :param Subject: 實體關系查詢返回關系的subject
        :type Subject: list of EntityRelationSubject
        :param Relation: 實體關系查詢返回的關系名稱
        :type Relation: str
        """
        self.Object = None
        self.Subject = None
        self.Relation = None


    def _deserialize(self, params):
        if params.get("Object") is not None:
            self.Object = []
            for item in params.get("Object"):
                obj = EntityRelationObject()
                obj._deserialize(item)
                self.Object.append(obj)
        if params.get("Subject") is not None:
            self.Subject = []
            for item in params.get("Subject"):
                obj = EntityRelationSubject()
                obj._deserialize(item)
                self.Subject.append(obj)
        self.Relation = params.get("Relation")


class EntityRelationObject(AbstractModel):
    """實體關系查詢返回的Object類型

    """

    def __init__(self):
        """
        :param Id: object對應id
        :type Id: list of str
        :param Name: object對應name
        :type Name: list of str
        :param Popular: object對應popular值
        :type Popular: list of int
        """
        self.Id = None
        self.Name = None
        self.Popular = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Popular = params.get("Popular")


class EntityRelationSubject(AbstractModel):
    """實體關系查詢返回Subject

    """

    def __init__(self):
        """
        :param Id: Subject對應id
        :type Id: list of str
        :param Name: Subject對應name
        :type Name: list of str
        :param Popular: Subject對應popular
        :type Popular: list of int
        """
        self.Id = None
        self.Name = None
        self.Popular = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Popular = params.get("Popular")


class TripleContent(AbstractModel):
    """三元組查詢返回的元記錄

    """

    def __init__(self):
        """
        :param Id: 實體id
        :type Id: str
        :param Name: 實體名稱
        :type Name: str
        :param Order: 實體order
        :type Order: int
        :param Popular: 實體流行度
        :type Popular: int
        """
        self.Id = None
        self.Name = None
        self.Order = None
        self.Popular = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Order = params.get("Order")
        self.Popular = params.get("Popular")