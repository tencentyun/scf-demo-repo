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


class AutoSummarizationRequest(AbstractModel):
    """AutoSummarization請求參數結構體

    """

    def __init__(self):
        """
        :param Text: 待處理的文本（僅支援UTF-8格式，不超過2000字）
        :type Text: str
        :param Length: 指定摘要的長度上限（預設值爲200）
注：爲保證摘要的可讀性，最終生成的摘要長度會低於指定的長度上限。
        :type Length: int
        """
        self.Text = None
        self.Length = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.Length = params.get("Length")


class AutoSummarizationResponse(AbstractModel):
    """AutoSummarization返回參數結構體

    """

    def __init__(self):
        """
        :param Summary: 文本摘要結果
        :type Summary: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Summary = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Summary = params.get("Summary")
        self.RequestId = params.get("RequestId")


class CCIToken(AbstractModel):
    """文本糾錯結果

    """

    def __init__(self):
        """
        :param BeginOffset: 錯别字的起始位置，從0開始
        :type BeginOffset: int
        :param CorrectWord: 錯别字糾錯結果
        :type CorrectWord: str
        :param Word: 錯别字内容
        :type Word: str
        """
        self.BeginOffset = None
        self.CorrectWord = None
        self.Word = None


    def _deserialize(self, params):
        self.BeginOffset = params.get("BeginOffset")
        self.CorrectWord = params.get("CorrectWord")
        self.Word = params.get("Word")


class ChatBotRequest(AbstractModel):
    """ChatBot請求參數結構體

    """

    def __init__(self):
        """
        :param Query: 用戶請求的query
        :type Query: str
        :param Flag: 0: 通用閑聊, 1:兒童閑聊, 預設是通用閑聊
        :type Flag: int
        :param OpenId: 服務的id,  主要用於兒童閑聊介面，比如手Q的openid
        :type OpenId: str
        """
        self.Query = None
        self.Flag = None
        self.OpenId = None


    def _deserialize(self, params):
        self.Query = params.get("Query")
        self.Flag = params.get("Flag")
        self.OpenId = params.get("OpenId")


class ChatBotResponse(AbstractModel):
    """ChatBot返回參數結構體

    """

    def __init__(self):
        """
        :param Confidence: 對於當前輸出回複的自信度
        :type Confidence: float
        :param Reply: 閑聊回複
        :type Reply: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Confidence = None
        self.Reply = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Reply = params.get("Reply")
        self.RequestId = params.get("RequestId")


class ClassificationResult(AbstractModel):
    """文本分類結果

    """

    def __init__(self):
        """
        :param FirstClassName: 一級分類名稱
        :type FirstClassName: str
        :param FirstClassProbability: 一級分類概率
        :type FirstClassProbability: float
        :param SecondClassName: 二級分類名稱
        :type SecondClassName: str
        :param SecondClassProbability: 二級分類概率
        :type SecondClassProbability: float
        """
        self.FirstClassName = None
        self.FirstClassProbability = None
        self.SecondClassName = None
        self.SecondClassProbability = None


    def _deserialize(self, params):
        self.FirstClassName = params.get("FirstClassName")
        self.FirstClassProbability = params.get("FirstClassProbability")
        self.SecondClassName = params.get("SecondClassName")
        self.SecondClassProbability = params.get("SecondClassProbability")


class DependencyParsingRequest(AbstractModel):
    """DependencyParsing請求參數結構體

    """

    def __init__(self):
        """
        :param Text: 待分析的文本（僅支援UTF-8格式，不超過200字）
        :type Text: str
        """
        self.Text = None


    def _deserialize(self, params):
        self.Text = params.get("Text")


class DependencyParsingResponse(AbstractModel):
    """DependencyParsing返回參數結構體

    """

    def __init__(self):
        """
        :param DpTokens: 句法依存分析結果，其中句法依存關系的類型包括：
<li>主謂關系，eg: 我送她一束花 (我 <-- 送)
<li>動賓關系，eg: 我送她一束花 (送 --> 花)
<li>間賓關系，eg: 我送她一束花 (送 --> 她)
<li>前置賓語，eg: 他什麽書都讀 (書 <-- 讀)
<li>兼語，eg: 他請我吃飯 (請 --> 我)
<li>定中關系，eg: 紅蘋果 (紅 <-- 蘋果)
<li>狀中結構，eg: 非常美麗 (非常 <-- 美麗)
<li>動補結構，eg: 做完了作業 (做 --> 完)
<li>並列關系，eg: 大山和大海 (大山 --> 大海)
<li>介賓關系，eg: 在貿易區内 (在 --> 内)
<li>左附加關系，eg: 大山和大海 (和 <-- 大海)
<li>右附加關系，eg: 孩子們 (孩子 --> 們)
<li>獨立結構，eg: 兩個單句在結構上彼此獨立
<li>標點符號，eg: 。
<li>核心關系，eg: 整個句子的核心
        :type DpTokens: list of DpToken
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DpTokens = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DpTokens") is not None:
            self.DpTokens = []
            for item in params.get("DpTokens"):
                obj = DpToken()
                obj._deserialize(item)
                self.DpTokens.append(obj)
        self.RequestId = params.get("RequestId")


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


class DpToken(AbstractModel):
    """句法依存分析結果，包括基礎詞，基礎詞的序號，當前詞父節點的序號，句法依存關系的類型

    """

    def __init__(self):
        """
        :param HeadId: 當前詞父節點的序號
        :type HeadId: int
        :param Id: 基礎詞的序號
        :type Id: int
        :param Relation: 句法依存關系的類型
        :type Relation: str
        :param Word: 基礎詞
        :type Word: str
        """
        self.HeadId = None
        self.Id = None
        self.Relation = None
        self.Word = None


    def _deserialize(self, params):
        self.HeadId = params.get("HeadId")
        self.Id = params.get("Id")
        self.Relation = params.get("Relation")
        self.Word = params.get("Word")


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


class Keyword(AbstractModel):
    """關鍵詞提取結果

    """

    def __init__(self):
        """
        :param Score: 權重
        :type Score: float
        :param Word: 關鍵詞
        :type Word: str
        """
        self.Score = None
        self.Word = None


    def _deserialize(self, params):
        self.Score = params.get("Score")
        self.Word = params.get("Word")


class KeywordsExtractionRequest(AbstractModel):
    """KeywordsExtraction請求參數結構體

    """

    def __init__(self):
        """
        :param Text: 待處理的文本（僅支援UTF-8格式，不超過10000字）
        :type Text: str
        :param Num: 指定關鍵詞個數上限（預設值爲5）
        :type Num: int
        """
        self.Text = None
        self.Num = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.Num = params.get("Num")


class KeywordsExtractionResponse(AbstractModel):
    """KeywordsExtraction返回參數結構體

    """

    def __init__(self):
        """
        :param Keywords: 關鍵詞提取結果
        :type Keywords: list of Keyword
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Keywords = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Keywords") is not None:
            self.Keywords = []
            for item in params.get("Keywords"):
                obj = Keyword()
                obj._deserialize(item)
                self.Keywords.append(obj)
        self.RequestId = params.get("RequestId")


class LexicalAnalysisRequest(AbstractModel):
    """LexicalAnalysis請求參數結構體

    """

    def __init__(self):
        """
        :param Text: 待分析的文本（僅支援UTF-8格式，不超過500字）
        :type Text: str
        :param Flag: 詞法分析模式（預設取2值）：
1、高精度（混合粒度分詞能力）；
2、高效能（單粒度分詞能力）；
        :type Flag: int
        """
        self.Text = None
        self.Flag = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.Flag = params.get("Flag")


class LexicalAnalysisResponse(AbstractModel):
    """LexicalAnalysis返回參數結構體

    """

    def __init__(self):
        """
        :param NerTokens: 命名實體識别結果。取值範圍：
<li>PER：表示人名</li>
<li>LOC：表示地名</li>
<li>ORG：表示機構團體名</li>
        :type NerTokens: list of NerToken
        :param PosTokens: 分詞&詞性標注結果（詞性表請參見附錄）
        :type PosTokens: list of PosToken
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NerTokens = None
        self.PosTokens = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NerTokens") is not None:
            self.NerTokens = []
            for item in params.get("NerTokens"):
                obj = NerToken()
                obj._deserialize(item)
                self.NerTokens.append(obj)
        if params.get("PosTokens") is not None:
            self.PosTokens = []
            for item in params.get("PosTokens"):
                obj = PosToken()
                obj._deserialize(item)
                self.PosTokens.append(obj)
        self.RequestId = params.get("RequestId")


class NerToken(AbstractModel):
    """命名實體識别結果

    """

    def __init__(self):
        """
        :param BeginOffset: 起始位置
        :type BeginOffset: int
        :param Length: 長度
        :type Length: int
        :param Type: 命名實體類型
        :type Type: str
        :param Word: 基礎詞
        :type Word: str
        """
        self.BeginOffset = None
        self.Length = None
        self.Type = None
        self.Word = None


    def _deserialize(self, params):
        self.BeginOffset = params.get("BeginOffset")
        self.Length = params.get("Length")
        self.Type = params.get("Type")
        self.Word = params.get("Word")


class PosToken(AbstractModel):
    """分詞&詞性標注結果

    """

    def __init__(self):
        """
        :param BeginOffset: 起始位置
        :type BeginOffset: int
        :param Length: 長度
        :type Length: int
        :param Pos: 詞性
        :type Pos: str
        :param Word: 基礎詞
        :type Word: str
        """
        self.BeginOffset = None
        self.Length = None
        self.Pos = None
        self.Word = None


    def _deserialize(self, params):
        self.BeginOffset = params.get("BeginOffset")
        self.Length = params.get("Length")
        self.Pos = params.get("Pos")
        self.Word = params.get("Word")


class SentenceEmbeddingRequest(AbstractModel):
    """SentenceEmbedding請求參數結構體

    """

    def __init__(self):
        """
        :param Text: 輸入的文本（僅支援UTF-8格式，不超過500字）
        :type Text: str
        """
        self.Text = None


    def _deserialize(self, params):
        self.Text = params.get("Text")


class SentenceEmbeddingResponse(AbstractModel):
    """SentenceEmbedding返回參數結構體

    """

    def __init__(self):
        """
        :param Dimension: 句向量的維度
        :type Dimension: int
        :param Vector: 句向量數組
        :type Vector: list of float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Dimension = None
        self.Vector = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Dimension = params.get("Dimension")
        self.Vector = params.get("Vector")
        self.RequestId = params.get("RequestId")


class SentenceSimilarityRequest(AbstractModel):
    """SentenceSimilarity請求參數結構體

    """

    def __init__(self):
        """
        :param SrcText: 計算相似度的源句子（僅支援UTF-8格式，不超過500字）
        :type SrcText: str
        :param TargetText: 計算相似度的目標句子（僅支援UTF-8格式，不超過500字）
        :type TargetText: str
        """
        self.SrcText = None
        self.TargetText = None


    def _deserialize(self, params):
        self.SrcText = params.get("SrcText")
        self.TargetText = params.get("TargetText")


class SentenceSimilarityResponse(AbstractModel):
    """SentenceSimilarity返回參數結構體

    """

    def __init__(self):
        """
        :param Similarity: 兩個文本的相似度
        :type Similarity: float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Similarity = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Similarity = params.get("Similarity")
        self.RequestId = params.get("RequestId")


class SentimentAnalysisRequest(AbstractModel):
    """SentimentAnalysis請求參數結構體

    """

    def __init__(self):
        """
        :param Text: 待分析的文本（僅支援UTF-8格式，不超過200字）
        :type Text: str
        :param Flag: 文本所屬類型（預設取4值）：
1、商品評論類
2、社交類
3、美食酒店類
4、通用領域類
        :type Flag: int
        """
        self.Text = None
        self.Flag = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.Flag = params.get("Flag")


class SentimentAnalysisResponse(AbstractModel):
    """SentimentAnalysis返回參數結構體

    """

    def __init__(self):
        """
        :param Negative: 負面情感概率
        :type Negative: float
        :param Positive: 正面情感概率
        :type Positive: float
        :param Sentiment: 情感屬性
        :type Sentiment: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Negative = None
        self.Positive = None
        self.Sentiment = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Negative = params.get("Negative")
        self.Positive = params.get("Positive")
        self.Sentiment = params.get("Sentiment")
        self.RequestId = params.get("RequestId")


class SimilarWordsRequest(AbstractModel):
    """SimilarWords請求參數結構體

    """

    def __init__(self):
        """
        :param Text: 輸入的詞語（僅支援UTF-8格式，不超過20字）
        :type Text: str
        :param WordNumber: 相似詞個數；取值範圍：1-200，預設爲10；
        :type WordNumber: int
        """
        self.Text = None
        self.WordNumber = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.WordNumber = params.get("WordNumber")


class SimilarWordsResponse(AbstractModel):
    """SimilarWords返回參數結構體

    """

    def __init__(self):
        """
        :param SimilarWords: 相似詞數組
        :type SimilarWords: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SimilarWords = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SimilarWords = params.get("SimilarWords")
        self.RequestId = params.get("RequestId")


class TextClassificationRequest(AbstractModel):
    """TextClassification請求參數結構體

    """

    def __init__(self):
        """
        :param Text: 待分類的文本（僅支援UTF-8格式，不超過10000字）
        :type Text: str
        :param Flag: 領域分類體系（預設取1值）：
1、通用領域
2、新聞領域
        :type Flag: int
        """
        self.Text = None
        self.Flag = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.Flag = params.get("Flag")


class TextClassificationResponse(AbstractModel):
    """TextClassification返回參數結構體

    """

    def __init__(self):
        """
        :param Classes: 文本分類結果（文本分類映射表請參見附錄）
        :type Classes: list of ClassificationResult
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Classes = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Classes") is not None:
            self.Classes = []
            for item in params.get("Classes"):
                obj = ClassificationResult()
                obj._deserialize(item)
                self.Classes.append(obj)
        self.RequestId = params.get("RequestId")


class TextCorrectionRequest(AbstractModel):
    """TextCorrection請求參數結構體

    """

    def __init__(self):
        """
        :param Text: 待糾錯的文本（僅支援UTF-8格式，不超過2000字）
        :type Text: str
        """
        self.Text = None


    def _deserialize(self, params):
        self.Text = params.get("Text")


class TextCorrectionResponse(AbstractModel):
    """TextCorrection返回參數結構體

    """

    def __init__(self):
        """
        :param CCITokens: 糾錯詳情
        :type CCITokens: list of CCIToken
        :param ResultText: 糾錯後的文本
        :type ResultText: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CCITokens = None
        self.ResultText = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CCITokens") is not None:
            self.CCITokens = []
            for item in params.get("CCITokens"):
                obj = CCIToken()
                obj._deserialize(item)
                self.CCITokens.append(obj)
        self.ResultText = params.get("ResultText")
        self.RequestId = params.get("RequestId")


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


class WordEmbeddingRequest(AbstractModel):
    """WordEmbedding請求參數結構體

    """

    def __init__(self):
        """
        :param Text: 輸入的詞語（僅支援UTF-8格式，不超過20字）
        :type Text: str
        """
        self.Text = None


    def _deserialize(self, params):
        self.Text = params.get("Text")


class WordEmbeddingResponse(AbstractModel):
    """WordEmbedding返回參數結構體

    """

    def __init__(self):
        """
        :param Dimension: 詞向量的維度
        :type Dimension: int
        :param Vector: 詞向量數組
        :type Vector: list of float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Dimension = None
        self.Vector = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Dimension = params.get("Dimension")
        self.Vector = params.get("Vector")
        self.RequestId = params.get("RequestId")


class WordSimilarityRequest(AbstractModel):
    """WordSimilarity請求參數結構體

    """

    def __init__(self):
        """
        :param SrcWord: 計算相似度的源詞（僅支援UTF-8格式，不超過20字）
        :type SrcWord: str
        :param TargetWord: 計算相似度的目標詞（僅支援UTF-8格式，不超過20字）
        :type TargetWord: str
        """
        self.SrcWord = None
        self.TargetWord = None


    def _deserialize(self, params):
        self.SrcWord = params.get("SrcWord")
        self.TargetWord = params.get("TargetWord")


class WordSimilarityResponse(AbstractModel):
    """WordSimilarity返回參數結構體

    """

    def __init__(self):
        """
        :param Similarity: 兩個詞語的相似度
        :type Similarity: float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Similarity = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Similarity = params.get("Similarity")
        self.RequestId = params.get("RequestId")