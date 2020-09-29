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
        :param Data: 數據操作結果
        :type Data: :class:`taifucloudcloud.yunsou.v20191115.models.DataManipulationResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DataManipulationResult()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DataManipulationResult(AbstractModel):
    """數據操作結果

    """

    def __init__(self):
        """
        :param AppId: 應用ID
        :type AppId: int
        :param Seq: 序號
        :type Seq: int
        :param TotalResult: 結果
        :type TotalResult: str
        :param Result: 操作結果明細
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: list of DataManipulationResultItem
        :param ErrorResult: 異常訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrorResult: str
        """
        self.AppId = None
        self.Seq = None
        self.TotalResult = None
        self.Result = None
        self.ErrorResult = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.Seq = params.get("Seq")
        self.TotalResult = params.get("TotalResult")
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = DataManipulationResultItem()
                obj._deserialize(item)
                self.Result.append(obj)
        self.ErrorResult = params.get("ErrorResult")


class DataManipulationResultItem(AbstractModel):
    """數據操作結果明細

    """

    def __init__(self):
        """
        :param Result: 結果
        :type Result: str
        :param DocId: 文件ID
        :type DocId: str
        :param Errno: 錯誤碼
        :type Errno: int
        """
        self.Result = None
        self.DocId = None
        self.Errno = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.DocId = params.get("DocId")
        self.Errno = params.get("Errno")


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
        :param SearchId: 當前檢索號，用於定位問題，建議指定並且全局唯一
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
        :param EnableAbsHighlight: 是否打開高紅標亮，0關閉，1打開
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
        :param MultiFilter: 分類過濾並集
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
        :param Data: 檢索結果
        :type Data: :class:`taifucloudcloud.yunsou.v20191115.models.SearchResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = SearchResult()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class SearchResult(AbstractModel):
    """搜索結果

    """

    def __init__(self):
        """
        :param CostTime: 檢索耗時，單位ms
        :type CostTime: int
        :param DisplayNum: 搜索最多可以展示的結果數，多頁
        :type DisplayNum: int
        :param Echo: 和檢索請求中的echo相對應
        :type Echo: str
        :param EResultNum: 檢索結果的估算篇數，由索引平台估算
        :type EResultNum: int
        :param ResultNum: 檢索返回的當前頁碼結果數
        :type ResultNum: int
        :param ResultList: 檢索結果清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResultList: list of SearchResultItem
        :param SegList: 檢索的分詞結果，array類型，可包含多個
注意：此欄位可能返回 null，表示取不到有效值。
        :type SegList: list of SearchResultSeg
        """
        self.CostTime = None
        self.DisplayNum = None
        self.Echo = None
        self.EResultNum = None
        self.ResultNum = None
        self.ResultList = None
        self.SegList = None


    def _deserialize(self, params):
        self.CostTime = params.get("CostTime")
        self.DisplayNum = params.get("DisplayNum")
        self.Echo = params.get("Echo")
        self.EResultNum = params.get("EResultNum")
        self.ResultNum = params.get("ResultNum")
        if params.get("ResultList") is not None:
            self.ResultList = []
            for item in params.get("ResultList"):
                obj = SearchResultItem()
                obj._deserialize(item)
                self.ResultList.append(obj)
        if params.get("SegList") is not None:
            self.SegList = []
            for item in params.get("SegList"):
                obj = SearchResultSeg()
                obj._deserialize(item)
                self.SegList.append(obj)


class SearchResultItem(AbstractModel):
    """搜索結果元素

    """

    def __init__(self):
        """
        :param DocAbs: 動态摘要訊息
        :type DocAbs: str
        :param DocId: 檢索文件id
        :type DocId: str
        :param DocMeta: 原始文件訊息
        :type DocMeta: str
        :param L2Score: 精計算得分
        :type L2Score: float
        :param SearchDebuginfo: 文件級回傳訊息
        :type SearchDebuginfo: str
        """
        self.DocAbs = None
        self.DocId = None
        self.DocMeta = None
        self.L2Score = None
        self.SearchDebuginfo = None


    def _deserialize(self, params):
        self.DocAbs = params.get("DocAbs")
        self.DocId = params.get("DocId")
        self.DocMeta = params.get("DocMeta")
        self.L2Score = params.get("L2Score")
        self.SearchDebuginfo = params.get("SearchDebuginfo")


class SearchResultSeg(AbstractModel):
    """SearchResultSeg

    """

    def __init__(self):
        """
        :param SegStr: 分詞
        :type SegStr: str
        """
        self.SegStr = None


    def _deserialize(self, params):
        self.SegStr = params.get("SegStr")