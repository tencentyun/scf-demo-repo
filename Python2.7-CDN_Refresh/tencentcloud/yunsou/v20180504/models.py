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


class DataManipulationRequest(AbstractModel):
    """DataManipulation請求參數結構體

    """

    def __init__(self):
        """
        :param OpType: 操作類型，add或del
        :type OpType: str
        :param Encoding: 數據編碼類型
        :type Encoding: str
        :param Contents: 數據
        :type Contents: str
        :param ResourceId: 應用Id
        :type ResourceId: int
        """
        self.OpType = None
        self.Encoding = None
        self.Contents = None
        self.ResourceId = None


    def _deserialize(self, params):
        self.OpType = params.get("OpType")
        self.Encoding = params.get("Encoding")
        self.Contents = params.get("Contents")
        self.ResourceId = params.get("ResourceId")


class DataManipulationResponse(AbstractModel):
    """DataManipulation返回參數結構體

    """

    def __init__(self):
        """
        :param RetMsg: 返回訊息
        :type RetMsg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RetMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RetMsg = params.get("RetMsg")
        self.RequestId = params.get("RequestId")


class DataSearchRequest(AbstractModel):
    """DataSearch請求參數結構體

    """

    def __init__(self):
        """
        :param ResourceId: 雲搜的業務ID，用以表明當前數據請求的業務
        :type ResourceId: int
        :param SearchQuery: 檢索串
        :type SearchQuery: str
        :param PageId: 當前頁，從第0頁開始計算
        :type PageId: int
        :param NumPerPage: 每頁結果數
        :type NumPerPage: int
        :param SearchId: 當前檢索号，用于定位問題，建議指定并且全局唯一
        :type SearchId: str
        :param QueryEncode: 請求編碼，0表示utf8，1表示gbk，建議指定
        :type QueryEncode: int
        :param RankType: 排序類型
        :type RankType: int
        :param NumFilter: 數值過濾，結果中按屬性過濾
        :type NumFilter: str
        :param ClFilter: 分類過濾，導航類檢索請求
        :type ClFilter: str
        :param Extra: 檢索用戶相關欄位
        :type Extra: str
        :param SourceId: 檢索來源
        :type SourceId: int
        :param SecondSearch: 是否進行二次檢索，0關閉，1打開
        :type SecondSearch: int
        :param MaxDocReturn: 指定返回最大篇數，無特殊原因不建議指定
        :type MaxDocReturn: int
        :param IsSmartbox: 是否smartbox檢索，0關閉，1打開
        :type IsSmartbox: int
        :param EnableAbsHighlight: 是否打開高紅标亮，0關閉，1打開
        :type EnableAbsHighlight: int
        :param QcBid: 指定訪問QC糾錯業務ID
        :type QcBid: int
        :param GroupBy: 按指定欄位進行group by，只能對數值欄位進行操作
        :type GroupBy: str
        :param Distinct: 按指定欄位進行distinct，只能對數值欄位進行操作
        :type Distinct: str
        :param L4RankExpression: 高級排序參數，具體參見高級排序說明
        :type L4RankExpression: str
        :param MatchValue: 高級排序參數，具體參見高級排序說明
        :type MatchValue: str
        :param Longitude: 經度訊息
        :type Longitude: float
        :param Latitude: 緯度訊息
        :type Latitude: float
        :param MultiFilter: 分類過濾并集
        :type MultiFilter: list of str
        """
        self.ResourceId = None
        self.SearchQuery = None
        self.PageId = None
        self.NumPerPage = None
        self.SearchId = None
        self.QueryEncode = None
        self.RankType = None
        self.NumFilter = None
        self.ClFilter = None
        self.Extra = None
        self.SourceId = None
        self.SecondSearch = None
        self.MaxDocReturn = None
        self.IsSmartbox = None
        self.EnableAbsHighlight = None
        self.QcBid = None
        self.GroupBy = None
        self.Distinct = None
        self.L4RankExpression = None
        self.MatchValue = None
        self.Longitude = None
        self.Latitude = None
        self.MultiFilter = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.SearchQuery = params.get("SearchQuery")
        self.PageId = params.get("PageId")
        self.NumPerPage = params.get("NumPerPage")
        self.SearchId = params.get("SearchId")
        self.QueryEncode = params.get("QueryEncode")
        self.RankType = params.get("RankType")
        self.NumFilter = params.get("NumFilter")
        self.ClFilter = params.get("ClFilter")
        self.Extra = params.get("Extra")
        self.SourceId = params.get("SourceId")
        self.SecondSearch = params.get("SecondSearch")
        self.MaxDocReturn = params.get("MaxDocReturn")
        self.IsSmartbox = params.get("IsSmartbox")
        self.EnableAbsHighlight = params.get("EnableAbsHighlight")
        self.QcBid = params.get("QcBid")
        self.GroupBy = params.get("GroupBy")
        self.Distinct = params.get("Distinct")
        self.L4RankExpression = params.get("L4RankExpression")
        self.MatchValue = params.get("MatchValue")
        self.Longitude = params.get("Longitude")
        self.Latitude = params.get("Latitude")
        self.MultiFilter = params.get("MultiFilter")


class DataSearchResponse(AbstractModel):
    """DataSearch返回參數結構體

    """

    def __init__(self):
        """
        :param RetMsg: 數據返回訊息
        :type RetMsg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RetMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RetMsg = params.get("RetMsg")
        self.RequestId = params.get("RequestId")