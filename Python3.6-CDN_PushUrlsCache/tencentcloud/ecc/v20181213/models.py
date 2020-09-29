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
        :param Name: 維度名字
        :type Name: str
        :param Score: 維度得分
        :type Score: float
        :param Percentage: 維度分數占比
        :type Percentage: float
        """
        self.Name = None
        self.Score = None
        self.Percentage = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Score = params.get("Score")
        self.Percentage = params.get("Percentage")


class CompostionContext(AbstractModel):
    """圖像識别批改介面返回的作文文本訊息或批改訊息

    """

    def __init__(self):
        """
        :param Content: 作文内容
        :type Content: str
        :param CorrectData: 批改結果
注意：此欄位可能返回 null，表示取不到有效值。
        :type CorrectData: :class:`taifucloudcloud.ecc.v20181213.models.CorrectData`
        :param TaskId: 任務 id，用於查詢介面
注意：此欄位可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param SessionId: 圖像識别唯一標識，一次識别一個 SessionId
注意：此欄位可能返回 null，表示取不到有效值。
        :type SessionId: str
        """
        self.Content = None
        self.CorrectData = None
        self.TaskId = None
        self.SessionId = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        if params.get("CorrectData") is not None:
            self.CorrectData = CorrectData()
            self.CorrectData._deserialize(params.get("CorrectData"))
        self.TaskId = params.get("TaskId")
        self.SessionId = params.get("SessionId")


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


class CorrectMultiImageRequest(AbstractModel):
    """CorrectMultiImage請求參數結構體

    """

    def __init__(self):
        """
        :param Image: 圖片的url連結或base64數據。每張圖片數據作爲數組的一個元素，數組個數與圖片個數保持一緻。存放類别依據InputType而定，url與base64編碼不能混合使用。
        :type Image: list of str
        :param InputType: 輸出圖片類型，0 表示 Image 欄位是圖片所在的 url，1 表示 Image 欄位是 base64 編碼後的圖像數據。
        :type InputType: int
        :param EccAppid: 業務應用ID，與賬號應用APPID無關，是用來方便客戶管理服務的參數。
        :type EccAppid: str
        :param SessionId: 圖像識别唯一標識，一次識别一個 SessionId，使用識别功能時 SessionId 可用於使用文本批改介面，此時按圖像批改價格收費；如使用文本批改介面時沒有傳入 SessionId，則需要收取文本批改的費用。
        :type SessionId: str
        :param ServerType: 服務類型，0：“多圖像識别”，只返回識别結果；1：“多圖像批改”，同時返回識别結果與批改結果。預設爲 0。
        :type ServerType: int
        :param Title: 作文題目，可選參數
        :type Title: str
        :param Grade: 年級標準， 預設以 cet4 爲標準，取值與意義如下：elementary 小學，grade7 grade8 grade9分别對應初一，初二，初三。 grade10 grade11 grade12 分别對應高一，高二，高三，以及 cet4 和 cet6 分别表示 英語4級和6級。
        :type Grade: str
        :param Requirement: 作文提綱，可選參數，作文的寫作要求。
        :type Requirement: str
        :param ModelTitle: 範文標題，可選參數，本介面可以依據提供的範文對作文進行評分。
        :type ModelTitle: str
        :param ModelContent: 範文内容，可選參數，同上，範文的正文部分。
        :type ModelContent: str
        :param IsAsync: 異步模式標識，0：同步模式，1：異步模式。預設爲同步模式
        :type IsAsync: int
        """
        self.Image = None
        self.InputType = None
        self.EccAppid = None
        self.SessionId = None
        self.ServerType = None
        self.Title = None
        self.Grade = None
        self.Requirement = None
        self.ModelTitle = None
        self.ModelContent = None
        self.IsAsync = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.InputType = params.get("InputType")
        self.EccAppid = params.get("EccAppid")
        self.SessionId = params.get("SessionId")
        self.ServerType = params.get("ServerType")
        self.Title = params.get("Title")
        self.Grade = params.get("Grade")
        self.Requirement = params.get("Requirement")
        self.ModelTitle = params.get("ModelTitle")
        self.ModelContent = params.get("ModelContent")
        self.IsAsync = params.get("IsAsync")


class CorrectMultiImageResponse(AbstractModel):
    """CorrectMultiImage返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 介面返回數據
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


class DescribeTaskRequest(AbstractModel):
    """DescribeTask請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務 ID
        :type TaskId: str
        :param EccAppid: 業務應用ID，與賬號應用APPID無關，是用來方便客戶管理服務的參數（暫時無需傳入）。
        :type EccAppid: str
        """
        self.TaskId = None
        self.EccAppid = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.EccAppid = params.get("EccAppid")


class DescribeTaskResponse(AbstractModel):
    """DescribeTask返回參數結構體

    """

    def __init__(self):
        """
        :param Content: 作文識别文本
注意：此欄位可能返回 null，表示取不到有效值。
        :type Content: str
        :param CorrectData: 整體的批改結果
注意：此欄位可能返回 null，表示取不到有效值。
        :type CorrectData: :class:`taifucloudcloud.ecc.v20181213.models.CorrectData`
        :param Status: 任務狀态，“Progressing”: 處理中（此時無結果返回）、“Finished”: 處理完成
        :type Status: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Content = None
        self.CorrectData = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        if params.get("CorrectData") is not None:
            self.CorrectData = CorrectData()
            self.CorrectData._deserialize(params.get("CorrectData"))
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


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
        :param Requirement: 作文提綱，可選參數，作文的寫作要求。
        :type Requirement: str
        :param ModelTitle: 範文標題，可選參數，本介面可以依據提供的範文對作文進行評分。
        :type ModelTitle: str
        :param ModelContent: 範文内容，可選參數，同上，範文的正文部分。
        :type ModelContent: str
        :param EccAppid: 業務應用ID，與賬號應用APPID無關，是用來方便客戶管理服務的參數（暫時無需傳入）。
        :type EccAppid: str
        :param IsAsync: 異步模式標識，0：同步模式，1：異步模式，預設爲同步模式
        :type IsAsync: int
        :param SessionId: 圖像識别唯一標識，一次識别一個 SessionId。當傳入此前識别介面使用過的 SessionId，則本次批改按圖像批改價格收費；如使用了識别介面且本次沒有傳入 SessionId，則需要加取文本批改的費用；如果直接使用文本批改介面，則只收取文本批改的費用
        :type SessionId: str
        """
        self.Content = None
        self.Title = None
        self.Grade = None
        self.Requirement = None
        self.ModelTitle = None
        self.ModelContent = None
        self.EccAppid = None
        self.IsAsync = None
        self.SessionId = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.Title = params.get("Title")
        self.Grade = params.get("Grade")
        self.Requirement = params.get("Requirement")
        self.ModelTitle = params.get("ModelTitle")
        self.ModelContent = params.get("ModelContent")
        self.EccAppid = params.get("EccAppid")
        self.IsAsync = params.get("IsAsync")
        self.SessionId = params.get("SessionId")


class ECCResponse(AbstractModel):
    """ECC返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 整體的批改結果
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: :class:`taifucloudcloud.ecc.v20181213.models.CorrectData`
        :param TaskId: 任務 id，用於查詢介面
注意：此欄位可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CorrectData()
            self.Data._deserialize(params.get("Data"))
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class EHOCRRequest(AbstractModel):
    """EHOCR請求參數結構體

    """

    def __init__(self):
        """
        :param Image: 圖片所在的url或base64編碼後的圖像數據，依據InputType而定
        :type Image: str
        :param InputType: 輸出圖片類型，0 表示 Image 欄位是圖片所在的 url，1 表示 Image 欄位是 base64 編碼後的圖像數據
        :type InputType: int
        :param EccAppid: 業務應用ID，與賬號應用APPID無關，是用來方便客戶管理服務的參數（暫時無需傳入）。
        :type EccAppid: str
        :param SessionId: 圖像識别唯一標識，一次識别一個 SessionId，使用識别功能時 SessionId 可用於使用文本批改介面，此時按圖像批改價格收費；如使用文本批改介面時沒有傳入 SessionId，則需要收取文本批改的費用
        :type SessionId: str
        :param ServerType: 服務類型，0：“圖像識别”，只返回識别結果，1：“圖像批改”，同時返回識别結果與批改結果。預設爲 0
        :type ServerType: int
        :param Title: 作文題目，可選參數
        :type Title: str
        :param Grade: 年級標準， 預設以 cet4 爲標準，取值與意義如下：elementary 小學，grade7 grade8 grade9分别對應初一，初二，初三。 grade10 grade11 grade12 分别對應高一，高二，高三，以及 cet4 和 cet6 分别表示 英語4級和6級。
        :type Grade: str
        :param Requirement: 作文提綱，可選參數，作文的寫作要求。
        :type Requirement: str
        :param ModelTitle: 範文標題，可選參數，本介面可以依據提供的範文對作文進行評分。
        :type ModelTitle: str
        :param ModelContent: 範文内容，可選參數，同上，範文的正文部分。
        :type ModelContent: str
        :param IsAsync: 異步模式標識，0：同步模式，1：異步模式。預設爲同步模式
        :type IsAsync: int
        """
        self.Image = None
        self.InputType = None
        self.EccAppid = None
        self.SessionId = None
        self.ServerType = None
        self.Title = None
        self.Grade = None
        self.Requirement = None
        self.ModelTitle = None
        self.ModelContent = None
        self.IsAsync = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.InputType = params.get("InputType")
        self.EccAppid = params.get("EccAppid")
        self.SessionId = params.get("SessionId")
        self.ServerType = params.get("ServerType")
        self.Title = params.get("Title")
        self.Grade = params.get("Grade")
        self.Requirement = params.get("Requirement")
        self.ModelTitle = params.get("ModelTitle")
        self.ModelContent = params.get("ModelContent")
        self.IsAsync = params.get("IsAsync")


class EHOCRResponse(AbstractModel):
    """EHOCR返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 介面返回數據
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


class ErrorCoordinate(AbstractModel):
    """維度單詞坐標

    """

    def __init__(self):
        """
        :param Coordinate: 維度單詞坐標
        :type Coordinate: list of int
        """
        self.Coordinate = None


    def _deserialize(self, params):
        self.Coordinate = params.get("Coordinate")


class ScoreCategory(AbstractModel):
    """四個維度的得分

    """

    def __init__(self):
        """
        :param Words: 詞匯維度
        :type Words: :class:`taifucloudcloud.ecc.v20181213.models.Aspect`
        :param Sentences: 句子維度
        :type Sentences: :class:`taifucloudcloud.ecc.v20181213.models.Aspect`
        :param Structure: 篇章結構維度
        :type Structure: :class:`taifucloudcloud.ecc.v20181213.models.Aspect`
        :param Content: 内容維度
        :type Content: :class:`taifucloudcloud.ecc.v20181213.models.Aspect`
        :param Score: 維度得分
        :type Score: float
        :param Percentage: 維度分數占比
        :type Percentage: float
        """
        self.Words = None
        self.Sentences = None
        self.Structure = None
        self.Content = None
        self.Score = None
        self.Percentage = None


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
        self.Score = params.get("Score")
        self.Percentage = params.get("Percentage")


class SentenceCom(AbstractModel):
    """批改結果按句點評的詳細訊息

    """

    def __init__(self):
        """
        :param Suggestions: 句子錯誤糾正訊息
        :type Suggestions: list of SentenceSuggest
        :param Sentence: 句子訊息
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
        :param ErrorPosition: 維度單詞位置，在句子的第幾個到第幾個單詞之間
        :type ErrorPosition: list of int
        :param ErrorCoordinates: 維度單詞坐標，錯誤單詞在圖片中的坐標，只有傳圖片時正常返回，傳文字時返回[ ]
        :type ErrorCoordinates: list of ErrorCoordinate
        """
        self.Type = None
        self.ErrorType = None
        self.Origin = None
        self.Replace = None
        self.Message = None
        self.ErrorPosition = None
        self.ErrorCoordinates = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.ErrorType = params.get("ErrorType")
        self.Origin = params.get("Origin")
        self.Replace = params.get("Replace")
        self.Message = params.get("Message")
        self.ErrorPosition = params.get("ErrorPosition")
        if params.get("ErrorCoordinates") is not None:
            self.ErrorCoordinates = []
            for item in params.get("ErrorCoordinates"):
                obj = ErrorCoordinate()
                obj._deserialize(item)
                self.ErrorCoordinates.append(obj)