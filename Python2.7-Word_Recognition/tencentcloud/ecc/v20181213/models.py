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


class Aspect(AbstractModel):
    """作文批改每個維度名字與得分

    """

    def __init__(self):
        """
        :param Name: 項目 名字
        :type Name: str
        :param Score: 該項得分
        :type Score: float
        """
        self.Name = None
        self.Score = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Score = params.get("Score")


class CompostionContext(AbstractModel):
    """ocr返回的作文文本訊息

    """

    def __init__(self):
        """
        :param Content: 作文内容
        :type Content: str
        """
        self.Content = None


    def _deserialize(self, params):
        self.Content = params.get("Content")


class CorrectData(AbstractModel):
    """批改的結果

    """

    def __init__(self):
        """
        :param Score: 總得分
        :type Score: float
        :param ScoreCat: 各項得分詳情
        :type ScoreCat: :class:`taifucloudcloud.ecc.v20181213.models.ScoreCategory`
        :param Comment: 綜合評價
        :type Comment: str
        :param SentenceComments: 句子點評
        :type SentenceComments: list of SentenceCom
        """
        self.Score = None
        self.ScoreCat = None
        self.Comment = None
        self.SentenceComments = None


    def _deserialize(self, params):
        self.Score = params.get("Score")
        if params.get("ScoreCat") is not None:
            self.ScoreCat = ScoreCategory()
            self.ScoreCat._deserialize(params.get("ScoreCat"))
        self.Comment = params.get("Comment")
        if params.get("SentenceComments") is not None:
            self.SentenceComments = []
            for item in params.get("SentenceComments"):
                obj = SentenceCom()
                obj._deserialize(item)
                self.SentenceComments.append(obj)


class ECCRequest(AbstractModel):
    """ECC請求參數結構體

    """

    def __init__(self):
        """
        :param Content: 作文文本，必填
        :type Content: str
        :param Title: 作文題目，可選參數
        :type Title: str
        :param Grade: 年級標準， 預設以cet4爲標準，取值與意義如下：elementary 小學，grade7 grade8 grade9分别對應初一，初二，初三。 grade10 grade11 grade12 分别對應高一，高二，高三，以及cet4和cet6 分别表示 英語4級和6級。
        :type Grade: str
        :param Outline: 作文提綱，可選參數，作文的寫作要求。
        :type Outline: str
        :param ModelSubject: 範文標題，可選參數，本介面可以依據提供的範文對作文進行評分。
        :type ModelSubject: str
        :param ModelContent: 範文内容，可選參數，同上，範文的正文部分。
        :type ModelContent: str
        """
        self.Content = None
        self.Title = None
        self.Grade = None
        self.Outline = None
        self.ModelSubject = None
        self.ModelContent = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.Title = params.get("Title")
        self.Grade = params.get("Grade")
        self.Outline = params.get("Outline")
        self.ModelSubject = params.get("ModelSubject")
        self.ModelContent = params.get("ModelContent")


class ECCResponse(AbstractModel):
    """ECC返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 整體的批改結果
        :type Data: :class:`taifucloudcloud.ecc.v20181213.models.CorrectData`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CorrectData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class EHOCRRequest(AbstractModel):
    """EHOCR請求參數結構體

    """

    def __init__(self):
        """
        :param Image: 圖片所在的url或base64編碼後的圖像數據，依據InputType而定
        :type Image: str
        :param InputType: 輸出圖片類型，0表示Image欄位是圖片所在的url，1表示Image欄位是base64編碼後的圖像數據
        :type InputType: int
        """
        self.Image = None
        self.InputType = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.InputType = params.get("InputType")


class EHOCRResponse(AbstractModel):
    """EHOCR返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 識别後的作文内容
        :type Data: :class:`taifucloudcloud.ecc.v20181213.models.CompostionContext`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CompostionContext()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class ScoreCategory(AbstractModel):
    """四個維度的得分

    """

    def __init__(self):
        """
        :param Words: 詞匯項
        :type Words: :class:`taifucloudcloud.ecc.v20181213.models.Aspect`
        :param Sentences: 句子項
        :type Sentences: :class:`taifucloudcloud.ecc.v20181213.models.Aspect`
        :param Structure: 篇章結構
        :type Structure: :class:`taifucloudcloud.ecc.v20181213.models.Aspect`
        :param Content: 内容
        :type Content: :class:`taifucloudcloud.ecc.v20181213.models.Aspect`
        """
        self.Words = None
        self.Sentences = None
        self.Structure = None
        self.Content = None


    def _deserialize(self, params):
        if params.get("Words") is not None:
            self.Words = Aspect()
            self.Words._deserialize(params.get("Words"))
        if params.get("Sentences") is not None:
            self.Sentences = Aspect()
            self.Sentences._deserialize(params.get("Sentences"))
        if params.get("Structure") is not None:
            self.Structure = Aspect()
            self.Structure._deserialize(params.get("Structure"))
        if params.get("Content") is not None:
            self.Content = Aspect()
            self.Content._deserialize(params.get("Content"))


class SentenceCom(AbstractModel):
    """句子點評

    """

    def __init__(self):
        """
        :param Suggestions: 點評内容
        :type Suggestions: list of SentenceSuggest
        :param Sentence: 點評的句子訊息
        :type Sentence: :class:`taifucloudcloud.ecc.v20181213.models.SentenceItem`
        """
        self.Suggestions = None
        self.Sentence = None


    def _deserialize(self, params):
        if params.get("Suggestions") is not None:
            self.Suggestions = []
            for item in params.get("Suggestions"):
                obj = SentenceSuggest()
                obj._deserialize(item)
                self.Suggestions.append(obj)
        if params.get("Sentence") is not None:
            self.Sentence = SentenceItem()
            self.Sentence._deserialize(params.get("Sentence"))


class SentenceItem(AbstractModel):
    """句子的相關訊息

    """

    def __init__(self):
        """
        :param Sentence: 英語句子
        :type Sentence: str
        :param ParaID: 段落id
        :type ParaID: int
        :param SentenceID: 句子id
        :type SentenceID: int
        """
        self.Sentence = None
        self.ParaID = None
        self.SentenceID = None


    def _deserialize(self, params):
        self.Sentence = params.get("Sentence")
        self.ParaID = params.get("ParaID")
        self.SentenceID = params.get("SentenceID")


class SentenceSuggest(AbstractModel):
    """句子批閱建議

    """

    def __init__(self):
        """
        :param Type: 類型
        :type Type: str
        :param ErrorType: 錯誤類型
        :type ErrorType: str
        :param Origin: 原始單詞
        :type Origin: str
        :param Replace: 替換成 的單詞
        :type Replace: str
        :param Message: 提示訊息
        :type Message: str
        """
        self.Type = None
        self.ErrorType = None
        self.Origin = None
        self.Replace = None
        self.Message = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.ErrorType = params.get("ErrorType")
        self.Origin = params.get("Origin")
        self.Replace = params.get("Replace")
        self.Message = params.get("Message")