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


class AIAnalysisTemplateItem(AbstractModel):
    """AI 智慧分析範本詳情

    """

    def __init__(self):
        """
        :param Definition: 智慧分析範本唯一標識。
        :type Definition: int
        :param Name: 智慧分析範本名稱。
        :type Name: str
        :param Comment: 智慧分析範本描述訊息。
        :type Comment: str
        :param ClassificationConfigure: 智慧分類任務控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClassificationConfigure: :class:`taifucloudcloud.mps.v20190612.models.ClassificationConfigureInfo`
        :param TagConfigure: 智慧標簽任務控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagConfigure: :class:`taifucloudcloud.mps.v20190612.models.TagConfigureInfo`
        :param CoverConfigure: 智慧封面任務控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CoverConfigure: :class:`taifucloudcloud.mps.v20190612.models.CoverConfigureInfo`
        :param FrameTagConfigure: 智慧按幀標簽任務控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FrameTagConfigure: :class:`taifucloudcloud.mps.v20190612.models.FrameTagConfigureInfo`
        :param CreateTime: 範本創建時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param UpdateTime: 範本最後修改時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type UpdateTime: str
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.ClassificationConfigure = None
        self.TagConfigure = None
        self.CoverConfigure = None
        self.FrameTagConfigure = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("ClassificationConfigure") is not None:
            self.ClassificationConfigure = ClassificationConfigureInfo()
            self.ClassificationConfigure._deserialize(params.get("ClassificationConfigure"))
        if params.get("TagConfigure") is not None:
            self.TagConfigure = TagConfigureInfo()
            self.TagConfigure._deserialize(params.get("TagConfigure"))
        if params.get("CoverConfigure") is not None:
            self.CoverConfigure = CoverConfigureInfo()
            self.CoverConfigure._deserialize(params.get("CoverConfigure"))
        if params.get("FrameTagConfigure") is not None:
            self.FrameTagConfigure = FrameTagConfigureInfo()
            self.FrameTagConfigure._deserialize(params.get("FrameTagConfigure"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class AIRecognitionTemplateItem(AbstractModel):
    """視訊内容識别範本詳情

    """

    def __init__(self):
        """
        :param Definition: 視訊内容識别範本唯一標識。
        :type Definition: int
        :param Name: 視訊内容識别範本名稱。
        :type Name: str
        :param Comment: 視訊内容識别範本描述訊息。
        :type Comment: str
        :param FaceConfigure: 人臉識别控制參數。
        :type FaceConfigure: :class:`taifucloudcloud.mps.v20190612.models.FaceConfigureInfo`
        :param OcrFullTextConfigure: 文本全文識别控制參數。
        :type OcrFullTextConfigure: :class:`taifucloudcloud.mps.v20190612.models.OcrFullTextConfigureInfo`
        :param OcrWordsConfigure: 文本關鍵詞識别控制參數。
        :type OcrWordsConfigure: :class:`taifucloudcloud.mps.v20190612.models.OcrWordsConfigureInfo`
        :param AsrFullTextConfigure: 語音全文識别控制參數。
        :type AsrFullTextConfigure: :class:`taifucloudcloud.mps.v20190612.models.AsrFullTextConfigureInfo`
        :param AsrWordsConfigure: 語音關鍵詞識别控制參數。
        :type AsrWordsConfigure: :class:`taifucloudcloud.mps.v20190612.models.AsrWordsConfigureInfo`
        :param CreateTime: 範本創建時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param UpdateTime: 範本最後修改時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type UpdateTime: str
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.FaceConfigure = None
        self.OcrFullTextConfigure = None
        self.OcrWordsConfigure = None
        self.AsrFullTextConfigure = None
        self.AsrWordsConfigure = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("FaceConfigure") is not None:
            self.FaceConfigure = FaceConfigureInfo()
            self.FaceConfigure._deserialize(params.get("FaceConfigure"))
        if params.get("OcrFullTextConfigure") is not None:
            self.OcrFullTextConfigure = OcrFullTextConfigureInfo()
            self.OcrFullTextConfigure._deserialize(params.get("OcrFullTextConfigure"))
        if params.get("OcrWordsConfigure") is not None:
            self.OcrWordsConfigure = OcrWordsConfigureInfo()
            self.OcrWordsConfigure._deserialize(params.get("OcrWordsConfigure"))
        if params.get("AsrFullTextConfigure") is not None:
            self.AsrFullTextConfigure = AsrFullTextConfigureInfo()
            self.AsrFullTextConfigure._deserialize(params.get("AsrFullTextConfigure"))
        if params.get("AsrWordsConfigure") is not None:
            self.AsrWordsConfigure = AsrWordsConfigureInfo()
            self.AsrWordsConfigure._deserialize(params.get("AsrWordsConfigure"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class AiAnalysisResult(AbstractModel):
    """智慧分析結果

    """

    def __init__(self):
        """
        :param Type: 任務的類型，可以取的值有：
<li>Classification：智慧分類</li>
<li>Cover：智慧封面</li>
<li>Tag：智慧標簽</li>
<li>FrameTag：智慧按幀標簽</li>
<li>Highlight：智慧精彩集錦</li>
        :type Type: str
        :param ClassificationTask: 視訊内容分析智慧分類任務的查詢結果，當任務類型爲 Classification 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClassificationTask: :class:`taifucloudcloud.mps.v20190612.models.AiAnalysisTaskClassificationResult`
        :param CoverTask: 視訊内容分析智慧封面任務的查詢結果，當任務類型爲 Cover 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CoverTask: :class:`taifucloudcloud.mps.v20190612.models.AiAnalysisTaskCoverResult`
        :param TagTask: 視訊内容分析智慧標簽任務的查詢結果，當任務類型爲 Tag 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagTask: :class:`taifucloudcloud.mps.v20190612.models.AiAnalysisTaskTagResult`
        :param FrameTagTask: 視訊内容分析智慧按幀標簽任務的查詢結果，當任務類型爲 FrameTag 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FrameTagTask: :class:`taifucloudcloud.mps.v20190612.models.AiAnalysisTaskFrameTagResult`
        """
        self.Type = None
        self.ClassificationTask = None
        self.CoverTask = None
        self.TagTask = None
        self.FrameTagTask = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("ClassificationTask") is not None:
            self.ClassificationTask = AiAnalysisTaskClassificationResult()
            self.ClassificationTask._deserialize(params.get("ClassificationTask"))
        if params.get("CoverTask") is not None:
            self.CoverTask = AiAnalysisTaskCoverResult()
            self.CoverTask._deserialize(params.get("CoverTask"))
        if params.get("TagTask") is not None:
            self.TagTask = AiAnalysisTaskTagResult()
            self.TagTask._deserialize(params.get("TagTask"))
        if params.get("FrameTagTask") is not None:
            self.FrameTagTask = AiAnalysisTaskFrameTagResult()
            self.FrameTagTask._deserialize(params.get("FrameTagTask"))


class AiAnalysisTaskClassificationInput(AbstractModel):
    """智慧分類任務輸入類型

    """

    def __init__(self):
        """
        :param Definition: 視訊智慧分類範本 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiAnalysisTaskClassificationOutput(AbstractModel):
    """智慧分類結果訊息

    """

    def __init__(self):
        """
        :param ClassificationSet: 視訊智慧分類清單。
        :type ClassificationSet: list of MediaAiAnalysisClassificationItem
        """
        self.ClassificationSet = None


    def _deserialize(self, params):
        if params.get("ClassificationSet") is not None:
            self.ClassificationSet = []
            for item in params.get("ClassificationSet"):
                obj = MediaAiAnalysisClassificationItem()
                obj._deserialize(item)
                self.ClassificationSet.append(obj)


class AiAnalysisTaskClassificationResult(AbstractModel):
    """智慧分類任務結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 智慧分類任務輸入。
        :type Input: :class:`taifucloudcloud.mps.v20190612.models.AiAnalysisTaskClassificationInput`
        :param Output: 智慧分類任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.mps.v20190612.models.AiAnalysisTaskClassificationOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskClassificationInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiAnalysisTaskClassificationOutput()
            self.Output._deserialize(params.get("Output"))


class AiAnalysisTaskCoverInput(AbstractModel):
    """智慧分類任務輸入類型

    """

    def __init__(self):
        """
        :param Definition: 視訊智慧封面範本 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiAnalysisTaskCoverOutput(AbstractModel):
    """智慧封面結果訊息

    """

    def __init__(self):
        """
        :param CoverSet: 智慧封面清單。
        :type CoverSet: list of MediaAiAnalysisCoverItem
        :param OutputStorage: 智慧封面的儲存位置。
        :type OutputStorage: :class:`taifucloudcloud.mps.v20190612.models.TaskOutputStorage`
        """
        self.CoverSet = None
        self.OutputStorage = None


    def _deserialize(self, params):
        if params.get("CoverSet") is not None:
            self.CoverSet = []
            for item in params.get("CoverSet"):
                obj = MediaAiAnalysisCoverItem()
                obj._deserialize(item)
                self.CoverSet.append(obj)
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))


class AiAnalysisTaskCoverResult(AbstractModel):
    """智慧封面結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 智慧封面任務輸入。
        :type Input: :class:`taifucloudcloud.mps.v20190612.models.AiAnalysisTaskCoverInput`
        :param Output: 智慧封面任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.mps.v20190612.models.AiAnalysisTaskCoverOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskCoverInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiAnalysisTaskCoverOutput()
            self.Output._deserialize(params.get("Output"))


class AiAnalysisTaskFrameTagInput(AbstractModel):
    """智慧按幀標簽任務輸入類型

    """

    def __init__(self):
        """
        :param Definition: 視訊智慧按幀標簽範本 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiAnalysisTaskFrameTagOutput(AbstractModel):
    """智慧按幀標簽結果訊息

    """

    def __init__(self):
        """
        :param SegmentSet: 視訊按幀標簽清單。
        :type SegmentSet: list of MediaAiAnalysisFrameTagSegmentItem
        """
        self.SegmentSet = None


    def _deserialize(self, params):
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaAiAnalysisFrameTagSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiAnalysisTaskFrameTagResult(AbstractModel):
    """智慧按幀標簽結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 智慧按幀標簽任務輸入。
        :type Input: :class:`taifucloudcloud.mps.v20190612.models.AiAnalysisTaskFrameTagInput`
        :param Output: 智慧按幀標簽任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.mps.v20190612.models.AiAnalysisTaskFrameTagOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskFrameTagInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiAnalysisTaskFrameTagOutput()
            self.Output._deserialize(params.get("Output"))


class AiAnalysisTaskInput(AbstractModel):
    """AI 視訊智慧分析輸入參數類型

    """

    def __init__(self):
        """
        :param Definition: 視訊内容分析範本 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiAnalysisTaskTagInput(AbstractModel):
    """智慧標簽任務輸入類型

    """

    def __init__(self):
        """
        :param Definition: 視訊智慧標簽範本 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiAnalysisTaskTagOutput(AbstractModel):
    """智慧標簽結果訊息

    """

    def __init__(self):
        """
        :param TagSet: 視訊智慧標簽清單。
        :type TagSet: list of MediaAiAnalysisTagItem
        """
        self.TagSet = None


    def _deserialize(self, params):
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = MediaAiAnalysisTagItem()
                obj._deserialize(item)
                self.TagSet.append(obj)


class AiAnalysisTaskTagResult(AbstractModel):
    """智慧標簽結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 智慧標簽任務輸入。
        :type Input: :class:`taifucloudcloud.mps.v20190612.models.AiAnalysisTaskTagInput`
        :param Output: 智慧標簽任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.mps.v20190612.models.AiAnalysisTaskTagOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskTagInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiAnalysisTaskTagOutput()
            self.Output._deserialize(params.get("Output"))


class AiContentReviewResult(AbstractModel):
    """内容審核結果

    """

    def __init__(self):
        """
        :param Type: 任務的類型，可以取的值有：
<li>Porn：圖片 </li>
<li>Terrorism：圖片鑒恐</li>
<li>Political：圖片鑒政</li>
<li>Porn.Asr：Asr 文字 </li>
<li>Porn.Ocr：Ocr 文字 </li>
<li>Porn.Voice：聲音 </li>
<li>Political.Asr：Asr 文字鑒政</li>
<li>Political.Ocr：Ocr 文字鑒政</li>
<li>Terrorism.Ocr：Ocr 文字鑒恐</li>
<li>Prohibited.Asr：Asr 文字鑒違禁</li>
<li>Prohibited.Ocr：Ocr 文字鑒違禁</li>
        :type Type: str
        :param SampleRate: 采樣頻率，即對視訊每秒截取進行審核的幀數。
        :type SampleRate: float
        :param Duration: 審核的視訊時長，單位：秒。
        :type Duration: float
        :param PornTask: 視訊内容審核智慧畫面 任務的查詢結果，當任務類型爲 Porn 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PornTask: :class:`taifucloudcloud.mps.v20190612.models.AiReviewTaskPornResult`
        :param TerrorismTask: 視訊内容審核智慧畫面鑒恐任務的查詢結果，當任務類型爲 Terrorism 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TerrorismTask: :class:`taifucloudcloud.mps.v20190612.models.AiReviewTaskTerrorismResult`
        :param PoliticalTask: 視訊内容審核智慧畫面鑒政任務的查詢結果，當任務類型爲 Political 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PoliticalTask: :class:`taifucloudcloud.mps.v20190612.models.AiReviewTaskPoliticalResult`
        :param PornAsrTask: 視訊内容審核 Asr 文字 任務的查詢結果，當任務類型爲 Porn.Asr 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PornAsrTask: :class:`taifucloudcloud.mps.v20190612.models.AiReviewTaskPornAsrResult`
        :param PornOcrTask: 視訊内容審核 Ocr 文字 任務的查詢結果，當任務類型爲 Porn.Ocr 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PornOcrTask: :class:`taifucloudcloud.mps.v20190612.models.AiReviewTaskPornOcrResult`
        :param PoliticalAsrTask: 視訊内容審核 Asr 文字鑒政任務的查詢結果，當任務類型爲 Political.Asr 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PoliticalAsrTask: :class:`taifucloudcloud.mps.v20190612.models.AiReviewTaskPoliticalAsrResult`
        :param PoliticalOcrTask: 視訊内容審核 Ocr 文字鑒政任務的查詢結果，當任務類型爲 Political.Ocr 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PoliticalOcrTask: :class:`taifucloudcloud.mps.v20190612.models.AiReviewTaskPoliticalOcrResult`
        :param TerrorismOcrTask: 視訊内容審核 Ocr 文字鑒恐任務的查詢結果，當任務類型爲 Terrorism.Ocr 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TerrorismOcrTask: :class:`taifucloudcloud.mps.v20190612.models.AiReviewTaskTerrorismOcrResult`
        :param ProhibitedAsrTask: 視訊内容審核 Asr 文字鑒違禁任務的查詢結果，當任務類型爲 Prohibited.Asr 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProhibitedAsrTask: :class:`taifucloudcloud.mps.v20190612.models.AiReviewTaskProhibitedAsrResult`
        :param ProhibitedOcrTask: 視訊内容審核 Ocr 文字鑒違禁任務的查詢結果，當任務類型爲 Prohibited.Ocr 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProhibitedOcrTask: :class:`taifucloudcloud.mps.v20190612.models.AiReviewTaskProhibitedOcrResult`
        """
        self.Type = None
        self.SampleRate = None
        self.Duration = None
        self.PornTask = None
        self.TerrorismTask = None
        self.PoliticalTask = None
        self.PornAsrTask = None
        self.PornOcrTask = None
        self.PoliticalAsrTask = None
        self.PoliticalOcrTask = None
        self.TerrorismOcrTask = None
        self.ProhibitedAsrTask = None
        self.ProhibitedOcrTask = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.SampleRate = params.get("SampleRate")
        self.Duration = params.get("Duration")
        if params.get("PornTask") is not None:
            self.PornTask = AiReviewTaskPornResult()
            self.PornTask._deserialize(params.get("PornTask"))
        if params.get("TerrorismTask") is not None:
            self.TerrorismTask = AiReviewTaskTerrorismResult()
            self.TerrorismTask._deserialize(params.get("TerrorismTask"))
        if params.get("PoliticalTask") is not None:
            self.PoliticalTask = AiReviewTaskPoliticalResult()
            self.PoliticalTask._deserialize(params.get("PoliticalTask"))
        if params.get("PornAsrTask") is not None:
            self.PornAsrTask = AiReviewTaskPornAsrResult()
            self.PornAsrTask._deserialize(params.get("PornAsrTask"))
        if params.get("PornOcrTask") is not None:
            self.PornOcrTask = AiReviewTaskPornOcrResult()
            self.PornOcrTask._deserialize(params.get("PornOcrTask"))
        if params.get("PoliticalAsrTask") is not None:
            self.PoliticalAsrTask = AiReviewTaskPoliticalAsrResult()
            self.PoliticalAsrTask._deserialize(params.get("PoliticalAsrTask"))
        if params.get("PoliticalOcrTask") is not None:
            self.PoliticalOcrTask = AiReviewTaskPoliticalOcrResult()
            self.PoliticalOcrTask._deserialize(params.get("PoliticalOcrTask"))
        if params.get("TerrorismOcrTask") is not None:
            self.TerrorismOcrTask = AiReviewTaskTerrorismOcrResult()
            self.TerrorismOcrTask._deserialize(params.get("TerrorismOcrTask"))
        if params.get("ProhibitedAsrTask") is not None:
            self.ProhibitedAsrTask = AiReviewTaskProhibitedAsrResult()
            self.ProhibitedAsrTask._deserialize(params.get("ProhibitedAsrTask"))
        if params.get("ProhibitedOcrTask") is not None:
            self.ProhibitedOcrTask = AiReviewTaskProhibitedOcrResult()
            self.ProhibitedOcrTask._deserialize(params.get("ProhibitedOcrTask"))


class AiContentReviewTaskInput(AbstractModel):
    """智慧内容審核任務類型

    """

    def __init__(self):
        """
        :param Definition: 視訊内容審核範本 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiRecognitionResult(AbstractModel):
    """智慧識别結果。

    """

    def __init__(self):
        """
        :param Type: 任務的類型，取值範圍：
<li>FaceRecognition：人臉識别，</li>
<li>AsrWordsRecognition：語音關鍵詞識别，</li>
<li>OcrWordsRecognition：文本關鍵詞識别，</li>
<li>AsrFullTextRecognition：語音全文識别，</li>
<li>OcrFullTextRecognition：文本全文識别，</li>
<li>HeadTailRecognition：視訊片頭片尾識别，</li>
<li>ObjectRecognition：物體識别。</li>
        :type Type: str
        :param FaceTask: 人臉識别結果，當 Type 爲 
 FaceRecognition 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FaceTask: :class:`taifucloudcloud.mps.v20190612.models.AiRecognitionTaskFaceResult`
        :param AsrWordsTask: 語音關鍵詞識别結果，當 Type 爲
 AsrWordsRecognition 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AsrWordsTask: :class:`taifucloudcloud.mps.v20190612.models.AiRecognitionTaskAsrWordsResult`
        :param AsrFullTextTask: 語音全文識别結果，當 Type 爲
 AsrFullTextRecognition 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AsrFullTextTask: :class:`taifucloudcloud.mps.v20190612.models.AiRecognitionTaskAsrFullTextResult`
        :param OcrWordsTask: 文本關鍵詞識别結果，當 Type 爲
 OcrWordsRecognition 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OcrWordsTask: :class:`taifucloudcloud.mps.v20190612.models.AiRecognitionTaskOcrWordsResult`
        :param OcrFullTextTask: 文本全文識别結果，當 Type 爲
 OcrFullTextRecognition 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OcrFullTextTask: :class:`taifucloudcloud.mps.v20190612.models.AiRecognitionTaskOcrFullTextResult`
        """
        self.Type = None
        self.FaceTask = None
        self.AsrWordsTask = None
        self.AsrFullTextTask = None
        self.OcrWordsTask = None
        self.OcrFullTextTask = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("FaceTask") is not None:
            self.FaceTask = AiRecognitionTaskFaceResult()
            self.FaceTask._deserialize(params.get("FaceTask"))
        if params.get("AsrWordsTask") is not None:
            self.AsrWordsTask = AiRecognitionTaskAsrWordsResult()
            self.AsrWordsTask._deserialize(params.get("AsrWordsTask"))
        if params.get("AsrFullTextTask") is not None:
            self.AsrFullTextTask = AiRecognitionTaskAsrFullTextResult()
            self.AsrFullTextTask._deserialize(params.get("AsrFullTextTask"))
        if params.get("OcrWordsTask") is not None:
            self.OcrWordsTask = AiRecognitionTaskOcrWordsResult()
            self.OcrWordsTask._deserialize(params.get("OcrWordsTask"))
        if params.get("OcrFullTextTask") is not None:
            self.OcrFullTextTask = AiRecognitionTaskOcrFullTextResult()
            self.OcrFullTextTask._deserialize(params.get("OcrFullTextTask"))


class AiRecognitionTaskAsrFullTextResult(AbstractModel):
    """語音全文識别結果。

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 語音全文識别任務輸入訊息。
        :type Input: :class:`taifucloudcloud.mps.v20190612.models.AiRecognitionTaskAsrFullTextResultInput`
        :param Output: 語音全文識别任務輸出訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.mps.v20190612.models.AiRecognitionTaskAsrFullTextResultOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskAsrFullTextResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskAsrFullTextResultOutput()
            self.Output._deserialize(params.get("Output"))


class AiRecognitionTaskAsrFullTextResultInput(AbstractModel):
    """語音全文識别的輸入。

    """

    def __init__(self):
        """
        :param Definition: 語音全文識别範本 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiRecognitionTaskAsrFullTextResultOutput(AbstractModel):
    """語音全文識别結果。

    """

    def __init__(self):
        """
        :param SegmentSet: 語音全文識别片段清單。
        :type SegmentSet: list of AiRecognitionTaskAsrFullTextSegmentItem
        :param SubtitlePath: 字幕文件網址。
        :type SubtitlePath: str
        :param OutputStorage: 字幕文件儲存位置。
        :type OutputStorage: :class:`taifucloudcloud.mps.v20190612.models.TaskOutputStorage`
        """
        self.SegmentSet = None
        self.SubtitlePath = None
        self.OutputStorage = None


    def _deserialize(self, params):
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskAsrFullTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        self.SubtitlePath = params.get("SubtitlePath")
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))


class AiRecognitionTaskAsrFullTextSegmentItem(AbstractModel):
    """語音全文識别片段。

    """

    def __init__(self):
        """
        :param Confidence: 識别片段置信度。取值：0~100。
        :type Confidence: float
        :param StartTimeOffset: 識别片段起始的偏移時間，單位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 識别片段終止的偏移時間，單位：秒。
        :type EndTimeOffset: float
        :param Text: 識别文本。
        :type Text: str
        """
        self.Confidence = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Text = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Text = params.get("Text")


class AiRecognitionTaskAsrWordsResult(AbstractModel):
    """語音關鍵詞識别結果。

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 語音關鍵詞識别任務輸入訊息。
        :type Input: :class:`taifucloudcloud.mps.v20190612.models.AiRecognitionTaskAsrWordsResultInput`
        :param Output: 語音關鍵詞識别任務輸出訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.mps.v20190612.models.AiRecognitionTaskAsrWordsResultOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskAsrWordsResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskAsrWordsResultOutput()
            self.Output._deserialize(params.get("Output"))


class AiRecognitionTaskAsrWordsResultInput(AbstractModel):
    """語音關鍵詞識别輸入。

    """

    def __init__(self):
        """
        :param Definition: 語音關鍵詞識别範本 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiRecognitionTaskAsrWordsResultItem(AbstractModel):
    """語音關鍵詞識别結果。

    """

    def __init__(self):
        """
        :param Word: 語音關鍵詞。
        :type Word: str
        :param SegmentSet: 語音關鍵詞出現的時間片段清單。
        :type SegmentSet: list of AiRecognitionTaskAsrWordsSegmentItem
        """
        self.Word = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskAsrWordsSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiRecognitionTaskAsrWordsResultOutput(AbstractModel):
    """語音關鍵詞識别輸出。

    """

    def __init__(self):
        """
        :param ResultSet: 語音關鍵詞識别結果集。
        :type ResultSet: list of AiRecognitionTaskAsrWordsResultItem
        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = AiRecognitionTaskAsrWordsResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)


class AiRecognitionTaskAsrWordsSegmentItem(AbstractModel):
    """語音識别片段。

    """

    def __init__(self):
        """
        :param StartTimeOffset: 識别片段起始的偏移時間，單位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 識别片段終止的偏移時間，單位：秒。
        :type EndTimeOffset: float
        :param Confidence: 識别片段置信度。取值：0~100。
        :type Confidence: float
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")


class AiRecognitionTaskFaceResult(AbstractModel):
    """人臉識别結果。

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 人臉識别任務輸入訊息。
        :type Input: :class:`taifucloudcloud.mps.v20190612.models.AiRecognitionTaskFaceResultInput`
        :param Output: 人臉識别任務輸出訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.mps.v20190612.models.AiRecognitionTaskFaceResultOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskFaceResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskFaceResultOutput()
            self.Output._deserialize(params.get("Output"))


class AiRecognitionTaskFaceResultInput(AbstractModel):
    """人臉識别輸入。

    """

    def __init__(self):
        """
        :param Definition: 人臉識别範本 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiRecognitionTaskFaceResultItem(AbstractModel):
    """人臉識别結果

    """

    def __init__(self):
        """
        :param Id: 人物唯一標識 ID。
        :type Id: str
        :param Type: 人物庫類型，表示識别出的人物來自哪個人物庫：
<li>Default：預設人物庫；</li>
<li>UserDefine：用戶自定義人物庫。</li>
        :type Type: str
        :param Name: 人物名稱。
        :type Name: str
        :param SegmentSet: 人物出現的片段結果集。
        :type SegmentSet: list of AiRecognitionTaskFaceSegmentItem
        """
        self.Id = None
        self.Type = None
        self.Name = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskFaceSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiRecognitionTaskFaceResultOutput(AbstractModel):
    """智慧人臉識别輸出。

    """

    def __init__(self):
        """
        :param ResultSet: 智慧人臉識别結果集。
        :type ResultSet: list of AiRecognitionTaskFaceResultItem
        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = AiRecognitionTaskFaceResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)


class AiRecognitionTaskFaceSegmentItem(AbstractModel):
    """人臉識别結果片段

    """

    def __init__(self):
        """
        :param StartTimeOffset: 識别片段起始的偏移時間，單位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 識别片段終止的偏移時間，單位：秒。
        :type EndTimeOffset: float
        :param Confidence: 識别片段置信度。取值：0~100。
        :type Confidence: float
        :param AreaCoordSet: 識别結果的區域坐標。數組包含 4 個元素 [x1,y1,x2,y2]，依次表示區域左上點、右下點的橫縱坐標。
        :type AreaCoordSet: list of int
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.AreaCoordSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")


class AiRecognitionTaskInput(AbstractModel):
    """視訊内容識别輸入參數類型

    """

    def __init__(self):
        """
        :param Definition: 視訊智慧識别範本 ID 。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiRecognitionTaskOcrFullTextResult(AbstractModel):
    """文本全文識别結果。

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 文本全文識别任務輸入訊息。
        :type Input: :class:`taifucloudcloud.mps.v20190612.models.AiRecognitionTaskOcrFullTextResultInput`
        :param Output: 文本全文識别任務輸出訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.mps.v20190612.models.AiRecognitionTaskOcrFullTextResultOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskOcrFullTextResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskOcrFullTextResultOutput()
            self.Output._deserialize(params.get("Output"))


class AiRecognitionTaskOcrFullTextResultInput(AbstractModel):
    """文本全文識别輸入。

    """

    def __init__(self):
        """
        :param Definition: 文本全文識别範本 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiRecognitionTaskOcrFullTextResultOutput(AbstractModel):
    """文本全文識别輸出。

    """

    def __init__(self):
        """
        :param SegmentSet: 文本全文識别結果集。
        :type SegmentSet: list of AiRecognitionTaskOcrFullTextSegmentItem
        """
        self.SegmentSet = None


    def _deserialize(self, params):
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskOcrFullTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiRecognitionTaskOcrFullTextSegmentItem(AbstractModel):
    """文本全文識别片段。

    """

    def __init__(self):
        """
        :param StartTimeOffset: 識别片段起始的偏移時間，單位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 識别片段終止的偏移時間，單位：秒。
        :type EndTimeOffset: float
        :param TextSet: 識别片段結果集。
        :type TextSet: list of AiRecognitionTaskOcrFullTextSegmentTextItem
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.TextSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        if params.get("TextSet") is not None:
            self.TextSet = []
            for item in params.get("TextSet"):
                obj = AiRecognitionTaskOcrFullTextSegmentTextItem()
                obj._deserialize(item)
                self.TextSet.append(obj)


class AiRecognitionTaskOcrFullTextSegmentTextItem(AbstractModel):
    """文本全文識别片段。

    """

    def __init__(self):
        """
        :param Confidence: 識别片段置信度。取值：0~100。
        :type Confidence: float
        :param AreaCoordSet: 識别結果的區域坐標。數組包含 4 個元素 [x1,y1,x2,y2]，依次表示區域左上點、右下點的橫縱坐標。
        :type AreaCoordSet: list of int
        :param Text: 識别文本。
        :type Text: str
        """
        self.Confidence = None
        self.AreaCoordSet = None
        self.Text = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")
        self.Text = params.get("Text")


class AiRecognitionTaskOcrWordsResult(AbstractModel):
    """文本關鍵識别結果。

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 文本關鍵詞識别任務輸入訊息。
        :type Input: :class:`taifucloudcloud.mps.v20190612.models.AiRecognitionTaskOcrWordsResultInput`
        :param Output: 文本關鍵詞識别任務輸出訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.mps.v20190612.models.AiRecognitionTaskOcrWordsResultOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskOcrWordsResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskOcrWordsResultOutput()
            self.Output._deserialize(params.get("Output"))


class AiRecognitionTaskOcrWordsResultInput(AbstractModel):
    """文本關鍵詞識别輸入。

    """

    def __init__(self):
        """
        :param Definition: 文本關鍵詞識别範本 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiRecognitionTaskOcrWordsResultItem(AbstractModel):
    """文本關鍵詞識别結果。

    """

    def __init__(self):
        """
        :param Word: 文本關鍵詞。
        :type Word: str
        :param SegmentSet: 文本關鍵出現的片段清單。
        :type SegmentSet: list of AiRecognitionTaskOcrWordsSegmentItem
        """
        self.Word = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskOcrWordsSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiRecognitionTaskOcrWordsResultOutput(AbstractModel):
    """文本關鍵詞識别輸出。

    """

    def __init__(self):
        """
        :param ResultSet: 文本關鍵詞識别結果集。
        :type ResultSet: list of AiRecognitionTaskOcrWordsResultItem
        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = AiRecognitionTaskOcrWordsResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)


class AiRecognitionTaskOcrWordsSegmentItem(AbstractModel):
    """文本識别片段。

    """

    def __init__(self):
        """
        :param StartTimeOffset: 識别片段起始的偏移時間，單位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 識别片段終止的偏移時間，單位：秒。
        :type EndTimeOffset: float
        :param Confidence: 識别片段置信度。取值：0~100。
        :type Confidence: float
        :param AreaCoordSet: 識别結果的區域坐標。數組包含 4 個元素 [x1,y1,x2,y2]，依次表示區域左上點、右下點的橫縱坐標。
        :type AreaCoordSet: list of int
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.AreaCoordSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")


class AiReviewPoliticalAsrTaskInput(AbstractModel):
    """内容審核 Asr 文字鑒政、敏感任務輸入參數類型

    """

    def __init__(self):
        """
        :param Definition: 鑒政範本 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiReviewPoliticalAsrTaskOutput(AbstractModel):
    """Asr 文字涉政訊息

    """

    def __init__(self):
        """
        :param Confidence: Asr 文字涉政、敏感評分，分值爲0到100。
        :type Confidence: float
        :param Suggestion: Asr 文字涉政、敏感結果建議，取值範圍：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param SegmentSet: Asr 文字有涉政、敏感嫌疑的視訊片段清單。
        :type SegmentSet: list of MediaContentReviewAsrTextSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewAsrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiReviewPoliticalOcrTaskInput(AbstractModel):
    """内容審核 Ocr 文字鑒政任務輸入參數類型

    """

    def __init__(self):
        """
        :param Definition: 鑒政範本 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiReviewPoliticalOcrTaskOutput(AbstractModel):
    """Ocr 文字涉政訊息

    """

    def __init__(self):
        """
        :param Confidence: Ocr 文字涉政、敏感評分，分值爲0到100。
        :type Confidence: float
        :param Suggestion: Ocr 文字涉政、敏感結果建議，取值範圍：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param SegmentSet: Ocr 文字有涉政、敏感嫌疑的視訊片段清單。
        :type SegmentSet: list of MediaContentReviewOcrTextSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewOcrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiReviewPoliticalTaskInput(AbstractModel):
    """内容審核鑒政任務輸入參數類型

    """

    def __init__(self):
        """
        :param Definition: 鑒政範本 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiReviewPoliticalTaskOutput(AbstractModel):
    """涉政訊息

    """

    def __init__(self):
        """
        :param Confidence: 視訊涉政評分，分值爲0到100。
        :type Confidence: float
        :param Suggestion: 涉政結果建議，取值範圍：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param Label: 視訊鑒政結果標簽，取值範圍：
<li>politician：政治人物。</li>
<li>violation_photo：違規圖標。</li>
        :type Label: str
        :param SegmentSet: 有涉政嫌疑的視訊片段清單。
        :type SegmentSet: list of MediaContentReviewPoliticalSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewPoliticalSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiReviewPornAsrTaskInput(AbstractModel):
    """内容審核 Asr 文字 任務輸入參數類型

    """

    def __init__(self):
        """
        :param Definition:  範本 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiReviewPornAsrTaskOutput(AbstractModel):
    """Asr 文字涉黃訊息

    """

    def __init__(self):
        """
        :param Confidence: Asr 文字涉黃評分，分值爲0到100。
        :type Confidence: float
        :param Suggestion: Asr 文字涉黃結果建議，取值範圍：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param SegmentSet: Asr 文字有涉黃嫌疑的視訊片段清單。
        :type SegmentSet: list of MediaContentReviewAsrTextSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewAsrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiReviewPornOcrTaskInput(AbstractModel):
    """内容審核 Ocr 文字 任務輸入參數類型

    """

    def __init__(self):
        """
        :param Definition:  範本 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiReviewPornOcrTaskOutput(AbstractModel):
    """Ocr 文字涉黃訊息

    """

    def __init__(self):
        """
        :param Confidence: Ocr 文字涉黃評分，分值爲0到100。
        :type Confidence: float
        :param Suggestion: Ocr 文字涉黃結果建議，取值範圍：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param SegmentSet: Ocr 文字有涉黃嫌疑的視訊片段清單。
        :type SegmentSet: list of MediaContentReviewOcrTextSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewOcrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiReviewPornTaskInput(AbstractModel):
    """内容審核 任務輸入參數類型

    """

    def __init__(self):
        """
        :param Definition:  範本 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiReviewPornTaskOutput(AbstractModel):
    """ 結果訊息

    """

    def __init__(self):
        """
        :param Confidence: 視訊 評分，分值爲0到100。
        :type Confidence: float
        :param Suggestion:  結果建議，取值範圍：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param Label: 視訊 結果標簽，取值範圍：
<li>porn：色情。</li>
<li>sexy：性感。</li>
<li>vulgar：低俗。</li>
<li>intimacy：親密行爲。</li>
        :type Label: str
        :param SegmentSet: 有涉黃嫌疑的視訊片段清單。
        :type SegmentSet: list of MediaContentReviewSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiReviewProhibitedAsrTaskInput(AbstractModel):
    """内容審核 Asr 文字鑒違禁任務輸入參數類型

    """

    def __init__(self):
        """
        :param Definition: 鑒違禁範本 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiReviewProhibitedAsrTaskOutput(AbstractModel):
    """Asr 文字涉違禁訊息

    """

    def __init__(self):
        """
        :param Confidence: Asr 文字涉違禁評分，分值爲0到100。
        :type Confidence: float
        :param Suggestion: Asr 文字涉違禁結果建議，取值範圍：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param SegmentSet: Asr 文字有涉違禁嫌疑的視訊片段清單。
        :type SegmentSet: list of MediaContentReviewAsrTextSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewAsrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiReviewProhibitedOcrTaskInput(AbstractModel):
    """内容審核 Ocr 文字鑒違禁任務輸入參數類型

    """

    def __init__(self):
        """
        :param Definition: 鑒違禁範本 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiReviewProhibitedOcrTaskOutput(AbstractModel):
    """Ocr 文字涉違禁訊息

    """

    def __init__(self):
        """
        :param Confidence: Ocr 文字涉違禁評分，分值爲0到100。
        :type Confidence: float
        :param Suggestion: Ocr 文字涉違禁結果建議，取值範圍：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param SegmentSet: Ocr 文字有涉違禁嫌疑的視訊片段清單。
        :type SegmentSet: list of MediaContentReviewOcrTextSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewOcrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiReviewTaskPoliticalAsrResult(AbstractModel):
    """内容審核 Asr 文字鑒政、敏感任務結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 内容審核 Asr 文字鑒政任務輸入。
        :type Input: :class:`taifucloudcloud.mps.v20190612.models.AiReviewPoliticalAsrTaskInput`
        :param Output: 内容審核 Asr 文字鑒政任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.mps.v20190612.models.AiReviewPoliticalAsrTaskOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPoliticalAsrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPoliticalAsrTaskOutput()
            self.Output._deserialize(params.get("Output"))


class AiReviewTaskPoliticalOcrResult(AbstractModel):
    """内容審核 Ocr 文字鑒政、敏感任務結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS �� FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 内容審核 Ocr 文字鑒政任務輸入。
        :type Input: :class:`taifucloudcloud.mps.v20190612.models.AiReviewPoliticalOcrTaskInput`
        :param Output: 内容審核 Ocr 文字鑒政任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.mps.v20190612.models.AiReviewPoliticalOcrTaskOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPoliticalOcrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPoliticalOcrTaskOutput()
            self.Output._deserialize(params.get("Output"))


class AiReviewTaskPoliticalResult(AbstractModel):
    """内容審核鑒政任務結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 内容審核鑒政任務輸入。
        :type Input: :class:`taifucloudcloud.mps.v20190612.models.AiReviewPoliticalTaskInput`
        :param Output: 内容審核鑒政任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.mps.v20190612.models.AiReviewPoliticalTaskOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPoliticalTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPoliticalTaskOutput()
            self.Output._deserialize(params.get("Output"))


class AiReviewTaskPornAsrResult(AbstractModel):
    """内容審核 Asr 文字 任務結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 内容審核 Asr 文字 任務輸入。
        :type Input: :class:`taifucloudcloud.mps.v20190612.models.AiReviewPornAsrTaskInput`
        :param Output: 内容審核 Asr 文字 任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.mps.v20190612.models.AiReviewPornAsrTaskOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPornAsrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPornAsrTaskOutput()
            self.Output._deserialize(params.get("Output"))


class AiReviewTaskPornOcrResult(AbstractModel):
    """内容審核 Ocr 文字 任務結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 内容審核 Ocr 文字 任務輸入。
        :type Input: :class:`taifucloudcloud.mps.v20190612.models.AiReviewPornOcrTaskInput`
        :param Output: 内容審核 Ocr 文字 任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.mps.v20190612.models.AiReviewPornOcrTaskOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPornOcrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPornOcrTaskOutput()
            self.Output._deserialize(params.get("Output"))


class AiReviewTaskPornResult(AbstractModel):
    """内容審核 任務結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 内容審核 任務輸入。
        :type Input: :class:`taifucloudcloud.mps.v20190612.models.AiReviewPornTaskInput`
        :param Output: 内容審核 任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.mps.v20190612.models.AiReviewPornTaskOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPornTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPornTaskOutput()
            self.Output._deserialize(params.get("Output"))


class AiReviewTaskProhibitedAsrResult(AbstractModel):
    """内容審核 Asr 文字鑒任違禁務結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0 表示成功，其他值表示失敗：
<li>40000：輸入參數不合法，請檢查輸入參數；</li>
<li>60000：源文件錯誤（如視訊數據損壞），請确認源文件是否正常；</li>
<li>70000：内部服務錯誤，建議重試。</li>
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 内容審核 Asr 文字鑒違禁任務輸入。
        :type Input: :class:`taifucloudcloud.mps.v20190612.models.AiReviewProhibitedAsrTaskInput`
        :param Output: 内容審核 Asr 文字鑒違禁任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.mps.v20190612.models.AiReviewProhibitedAsrTaskOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewProhibitedAsrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewProhibitedAsrTaskOutput()
            self.Output._deserialize(params.get("Output"))


class AiReviewTaskProhibitedOcrResult(AbstractModel):
    """内容審核 Ocr 文字鑒任違禁務結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0 表示成功，其他值表示失敗：
<li>40000：輸入參數不合法，請檢查輸入參數；</li>
<li>60000：源文件錯誤（如視訊數據損壞），請确認源文件是否正常；</li>
<li>70000：内部服務錯誤，建議重試。</li>
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 内容審核 Ocr 文字鑒違禁任務輸入。
        :type Input: :class:`taifucloudcloud.mps.v20190612.models.AiReviewProhibitedOcrTaskInput`
        :param Output: 内容審核 Ocr 文字鑒違禁任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.mps.v20190612.models.AiReviewProhibitedOcrTaskOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewProhibitedOcrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewProhibitedOcrTaskOutput()
            self.Output._deserialize(params.get("Output"))


class AiReviewTaskTerrorismOcrResult(AbstractModel):
    """内容審核 Ocr 文字鑒恐任務結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0 表示成功，其他值表示失敗：
<li>40000：輸入參數不合法，請檢查輸入參數；</li>
<li>60000：源文件錯誤（如視訊數據損壞），請确認源文件是否正常；</li>
<li>70000：内部服務錯誤，建議重試。</li>
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 内容審核 Ocr 文字鑒恐任務輸入。
        :type Input: :class:`taifucloudcloud.mps.v20190612.models.AiReviewTerrorismOcrTaskInput`
        :param Output: 内容審核 Ocr 文字鑒恐任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.mps.v20190612.models.AiReviewTerrorismOcrTaskOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewTerrorismOcrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewTerrorismOcrTaskOutput()
            self.Output._deserialize(params.get("Output"))


class AiReviewTaskTerrorismResult(AbstractModel):
    """内容審核鑒恐任務結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 内容審核鑒恐任務輸入。
        :type Input: :class:`taifucloudcloud.mps.v20190612.models.AiReviewTerrorismTaskInput`
        :param Output: 内容審核鑒恐任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.mps.v20190612.models.AiReviewTerrorismTaskOutput`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewTerrorismTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewTerrorismTaskOutput()
            self.Output._deserialize(params.get("Output"))


class AiReviewTerrorismOcrTaskInput(AbstractModel):
    """内容審核 Ocr 文字鑒恐任務輸入參數類型

    """

    def __init__(self):
        """
        :param Definition: 鑒恐範本 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiReviewTerrorismOcrTaskOutput(AbstractModel):
    """Ocr 文字涉恐訊息

    """

    def __init__(self):
        """
        :param Confidence: Ocr 文字涉恐評分，分值爲0到100。
        :type Confidence: float
        :param Suggestion: Ocr 文字涉恐結果建議，取值範圍：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param SegmentSet: Ocr 文字有涉恐嫌疑的視訊片段清單。
        :type SegmentSet: list of MediaContentReviewOcrTextSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewOcrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiReviewTerrorismTaskInput(AbstractModel):
    """内容審核鑒恐任務輸入參數類型

    """

    def __init__(self):
        """
        :param Definition: 鑒恐範本 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiReviewTerrorismTaskOutput(AbstractModel):
    """暴恐訊息

    """

    def __init__(self):
        """
        :param Confidence: 視訊暴恐評分，分值爲0到100。
        :type Confidence: float
        :param Suggestion: 暴恐結果建議，取值範圍：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param Label: 視訊暴恐結果標簽，取值範圍：
<li>guns：武器槍支。</li>
<li>crowd：人群聚集。</li>
<li>police：警察部隊。</li>
<li>bloody：血腥畫面。</li>
<li>banners：暴恐旗幟。</li>
<li>militant：武裝分子。</li>
<li>explosion：爆炸火災。</li>
<li>terrorists：暴恐人物。</li>
        :type Label: str
        :param SegmentSet: 有暴恐嫌疑的視訊片段清單。
        :type SegmentSet: list of MediaContentReviewSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiSampleFaceInfo(AbstractModel):
    """AI 樣本管理，人臉訊息。

    """

    def __init__(self):
        """
        :param FaceId: 人臉圖片 ID。
        :type FaceId: str
        :param Url: 人臉圖片網址。
        :type Url: str
        """
        self.FaceId = None
        self.Url = None


    def _deserialize(self, params):
        self.FaceId = params.get("FaceId")
        self.Url = params.get("Url")


class AiSampleFaceOperation(AbstractModel):
    """AI 樣本管理，人臉數據操作。

    """

    def __init__(self):
        """
        :param Type: 操作類型，可選值：add（添加）、delete（删除）、reset（重置）。重置操作将清空該人物已有人臉數據，並添加 FaceContents 指定人臉數據。
        :type Type: str
        :param FaceIds: 人臉 ID 集合，當 Type爲delete 時，該欄位必填。
        :type FaceIds: list of str
        :param FaceContents: 人臉圖片 [Base64](https://tools.ietf.org/html/rfc4648) 編碼後的字串集合。
<li>當 Type爲add 或 reset 時，該欄位必填；</li>
<li>數組長度限制：5 張圖片。</li>
注意：圖片必須是單人像正面人臉較清晰的照片，像素不低於 200*200。
        :type FaceContents: list of str
        """
        self.Type = None
        self.FaceIds = None
        self.FaceContents = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.FaceIds = params.get("FaceIds")
        self.FaceContents = params.get("FaceContents")


class AiSampleFailFaceInfo(AbstractModel):
    """AI 樣本管理，處理失敗的人臉訊息

    """

    def __init__(self):
        """
        :param Index: 對應入參 FaceContents 中錯誤圖片下標，從 0 開始。
        :type Index: int
        :param ErrCode: 錯誤碼，取值：
<li>0：成功；</li>
<li>其他：失敗。</li>
        :type ErrCode: int
        :param Message: 錯誤描述。
        :type Message: str
        """
        self.Index = None
        self.ErrCode = None
        self.Message = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")


class AiSamplePerson(AbstractModel):
    """AI 樣本管理，人物訊息。

    """

    def __init__(self):
        """
        :param PersonId: 人物 ID。
        :type PersonId: str
        :param Name: 人物名稱。
        :type Name: str
        :param Description: 人物描述。
        :type Description: str
        :param FaceInfoSet: 人臉訊息。
        :type FaceInfoSet: list of AiSampleFaceInfo
        :param TagSet: 人物標簽。
        :type TagSet: list of str
        :param UsageSet: 應用場景。
        :type UsageSet: list of str
        :param CreateTime: 創建時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param UpdateTime: 最後修改時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type UpdateTime: str
        """
        self.PersonId = None
        self.Name = None
        self.Description = None
        self.FaceInfoSet = None
        self.TagSet = None
        self.UsageSet = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("FaceInfoSet") is not None:
            self.FaceInfoSet = []
            for item in params.get("FaceInfoSet"):
                obj = AiSampleFaceInfo()
                obj._deserialize(item)
                self.FaceInfoSet.append(obj)
        self.TagSet = params.get("TagSet")
        self.UsageSet = params.get("UsageSet")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class AiSampleTagOperation(AbstractModel):
    """AI 樣本管理，標簽操作。

    """

    def __init__(self):
        """
        :param Type: 操作類型，可選值：add（添加）、delete（删除）、reset（重置）。
        :type Type: str
        :param Tags: 標簽，長度限制：128 個字元。
        :type Tags: list of str
        """
        self.Type = None
        self.Tags = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Tags = params.get("Tags")


class AiSampleWord(AbstractModel):
    """AI 樣本管理，關鍵詞輸出訊息。

    """

    def __init__(self):
        """
        :param Keyword: 關鍵詞。
        :type Keyword: str
        :param TagSet: 關鍵詞標簽。
        :type TagSet: list of str
        :param UsageSet: 關鍵詞應用場景。
        :type UsageSet: list of str
        :param CreateTime: 創建時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param UpdateTime: 最後修改時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type UpdateTime: str
        """
        self.Keyword = None
        self.TagSet = None
        self.UsageSet = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.TagSet = params.get("TagSet")
        self.UsageSet = params.get("UsageSet")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class AiSampleWordInfo(AbstractModel):
    """AI 樣本管理，關鍵詞輸入訊息。

    """

    def __init__(self):
        """
        :param Keyword: 關鍵詞，長度限制：20 個字元。
        :type Keyword: str
        :param Tags: 關鍵詞標簽
<li>數組長度限制：20 個標簽；</li>
<li>單個標簽長度限制：128 個字元。</li>
        :type Tags: list of str
        """
        self.Keyword = None
        self.Tags = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.Tags = params.get("Tags")


class AnimatedGraphicTaskInput(AbstractModel):
    """轉動圖任務類型。

    """

    def __init__(self):
        """
        :param Definition: 視訊轉動圖範本 ID。
        :type Definition: int
        :param StartTimeOffset: 動圖在視訊中的開始時間，單位爲秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 動圖在視訊中的結束時間，單位爲秒。
        :type EndTimeOffset: float
        :param OutputStorage: 轉動圖後文件的目標儲存，不填則繼承上層的 OutputStorage 值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OutputStorage: :class:`taifucloudcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputObjectPath: 轉動圖後文件的輸出路徑，可以爲相對路徑或者絕對路徑。如果不填，則預設爲相對路徑：`{inputName}_animatedGraphic_{definition}.{format}`。
        :type OutputObjectPath: str
        """
        self.Definition = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.OutputStorage = None
        self.OutputObjectPath = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")


class AnimatedGraphicsTemplate(AbstractModel):
    """轉動圖範本詳情。

    """

    def __init__(self):
        """
        :param Definition: 轉動圖範本唯一標識。
        :type Definition: int
        :param Type: 範本類型，取值範圍：
<li>Preset：系統預置範本；</li>
<li>Custom：用戶自定義範本。</li>
        :type Type: str
        :param Name: 轉動圖範本名稱。
        :type Name: str
        :param Comment: 轉動圖範本描述。
        :type Comment: str
        :param Width: 動圖寬度（或長邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
        :type Width: int
        :param Height: 動圖高度（或短邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适應，可選值：
<li>open：開啓，此時，Width 代表視訊的長邊，Height 表示視訊的短邊；</li>
<li>close：關閉，此時，Width 代表視訊的寬度，Height 表示視訊的高度。</li>
預設值：open。
        :type ResolutionAdaptive: str
        :param Format: 動圖格式。
        :type Format: str
        :param Fps: 幀率。
        :type Fps: int
        :param Quality: 圖片質量。
        :type Quality: float
        :param CreateTime: 範本創建時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param UpdateTime: 範本最後修改時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type UpdateTime: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Fps = None
        self.Quality = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Fps = params.get("Fps")
        self.Quality = params.get("Quality")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class AsrFullTextConfigureInfo(AbstractModel):
    """語音全文識别任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 語音全文識别任務開關，可選值：
<li>ON：開啓智慧語音全文識别任務；</li>
<li>OFF：關閉智慧語音全文識别任務。</li>
        :type Switch: str
        :param SubtitleFormat: 生成的字幕文件格式，不填或者填空字串表示不生成字幕文件，可選值：
<li>vtt：生成 WebVTT 字幕文件。</li>
        :type SubtitleFormat: str
        """
        self.Switch = None
        self.SubtitleFormat = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.SubtitleFormat = params.get("SubtitleFormat")


class AsrFullTextConfigureInfoForUpdate(AbstractModel):
    """語音全文識别任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 語音全文識别任務開關，可選值：
<li>ON：開啓智慧語音全文識别任務；</li>
<li>OFF：關閉智慧語音全文識别任務。</li>
        :type Switch: str
        :param SubtitleFormat: 生成的字幕文件格式，填空字串表示不生成字幕文件，可選值：
<li>vtt：生成 WebVTT 字幕文件。</li>
        :type SubtitleFormat: str
        """
        self.Switch = None
        self.SubtitleFormat = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.SubtitleFormat = params.get("SubtitleFormat")


class AsrWordsConfigureInfo(AbstractModel):
    """語音關鍵詞識别控制參數。

    """

    def __init__(self):
        """
        :param Switch: 語音關鍵詞識别任務開關，可選值：
<li>ON：開啓語音關鍵詞識别任務；</li>
<li>OFF：關閉語音關鍵詞識别任務。</li>
        :type Switch: str
        :param LabelSet: 關鍵詞過濾標簽，指定需要返回的關鍵詞的標簽。如果未填或者爲空，則全部結果都返回。
標簽個數最多 10 個，每個標簽長度最多 16 個字元。
        :type LabelSet: list of str
        """
        self.Switch = None
        self.LabelSet = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")


class AsrWordsConfigureInfoForUpdate(AbstractModel):
    """語音關鍵詞識别控制參數。

    """

    def __init__(self):
        """
        :param Switch: 語音關鍵詞識别任務開關，可選值：
<li>ON：開啓語音關鍵詞識别任務；</li>
<li>OFF：關閉語音關鍵詞識别任務。</li>
        :type Switch: str
        :param LabelSet: 關鍵詞過濾標簽，指定需要返回的關鍵詞的標簽。如果未填或者爲空，則全部結果都返回。
標簽個數最多 10 個，每個標簽長度最多 16 個字元。
        :type LabelSet: list of str
        """
        self.Switch = None
        self.LabelSet = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")


class AudioTemplateInfo(AbstractModel):
    """音訊流配置參數

    """

    def __init__(self):
        """
        :param Codec: 音訊流的編碼格式。
當外層參數 Container 爲 mp3 時，可選值爲：
<li>libmp3lame。</li>
當外層參數 Container 爲 ogg 或 flac 時，可選值爲：
<li>flac。</li>
當外層參數 Container 爲 m4a 時，可選值爲：
<li>libfdk_aac；</li>
<li>libmp3lame；</li>
<li>ac3。</li>
當外層參數 Container 爲 mp4 或 flv 時，可選值爲：
<li>libfdk_aac：更适合 mp4；</li>
<li>libmp3lame：更适合 flv；</li>
<li>mp2。</li>
當外層參數 Container 爲 hls 時，可選值爲：
<li>libfdk_aac；</li>
<li>libmp3lame。</li>
        :type Codec: str
        :param Bitrate: 音訊流的碼率，取值範圍：0 和 [26, 256]，單位：kbps。
當取值爲 0，表示音訊碼率和原始音訊保持一緻。
        :type Bitrate: int
        :param SampleRate: 音訊流的采樣率，可選值：
<li>32000</li>
<li>44100</li>
<li>48000</li>
單位：Hz。
        :type SampleRate: int
        :param AudioChannel: 音訊通道方式，可選值：
<li>1：單通道</li>
<li>2：雙通道</li>
<li>6：立體聲</li>
預設值：2。
        :type AudioChannel: int
        """
        self.Codec = None
        self.Bitrate = None
        self.SampleRate = None
        self.AudioChannel = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Bitrate = params.get("Bitrate")
        self.SampleRate = params.get("SampleRate")
        self.AudioChannel = params.get("AudioChannel")


class AudioTemplateInfoForUpdate(AbstractModel):
    """音訊流配置參數

    """

    def __init__(self):
        """
        :param Codec: 音訊流的編碼格式。
當外層參數 Container 爲 mp3 時，可選值爲：
<li>libmp3lame。</li>
當外層參數 Container 爲 ogg 或 flac 時，可選值爲：
<li>flac。</li>
當外層參數 Container 爲 m4a 時，可選值爲：
<li>libfdk_aac；</li>
<li>libmp3lame；</li>
<li>ac3。</li>
當外層參數 Container 爲 mp4 或 flv 時，可選值爲：
<li>libfdk_aac：更适合 mp4；</li>
<li>libmp3lame：更适合 flv；</li>
<li>mp2。</li>
當外層參數 Container 爲 hls 時，可選值爲：
<li>libfdk_aac；</li>
<li>libmp3lame。</li>
        :type Codec: str
        :param Bitrate: 音訊流的碼率，取值範圍：0 和 [26, 256]，單位：kbps。 當取值爲 0，表示音訊碼率和原始音訊保持一緻。
        :type Bitrate: int
        :param SampleRate: 音訊流的采樣率，可選值：
<li>32000</li>
<li>44100</li>
<li>48000</li>
單位：Hz。
        :type SampleRate: int
        :param AudioChannel: 音訊通道方式，可選值：
<li>1：單通道</li>
<li>2：雙通道</li>
<li>6：立體聲</li>
        :type AudioChannel: int
        """
        self.Codec = None
        self.Bitrate = None
        self.SampleRate = None
        self.AudioChannel = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Bitrate = params.get("Bitrate")
        self.SampleRate = params.get("SampleRate")
        self.AudioChannel = params.get("AudioChannel")


class ClassificationConfigureInfo(AbstractModel):
    """智慧分類任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 智慧分類任務開關，可選值：
<li>ON：開啓智慧分類任務；</li>
<li>OFF：關閉智慧分類任務。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class ClassificationConfigureInfoForUpdate(AbstractModel):
    """智慧分類任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 智慧分類任務開關，可選值：
<li>ON：開啓智慧分類任務；</li>
<li>OFF：關閉智慧分類任務。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class ContentReviewTemplateItem(AbstractModel):
    """内容審核範本詳情

    """

    def __init__(self):
        """
        :param Definition: 内容審核範本唯一標識。
        :type Definition: int
        :param Name: 内容審核範本名稱，長度限制：64 個字元。
        :type Name: str
        :param Comment: 内容審核範本描述訊息，長度限制：256 個字元。
        :type Comment: str
        :param PornConfigure:  控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PornConfigure: :class:`taifucloudcloud.mps.v20190612.models.PornConfigureInfo`
        :param TerrorismConfigure: 鑒恐控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TerrorismConfigure: :class:`taifucloudcloud.mps.v20190612.models.TerrorismConfigureInfo`
        :param PoliticalConfigure: 鑒政控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PoliticalConfigure: :class:`taifucloudcloud.mps.v20190612.models.PoliticalConfigureInfo`
        :param ProhibitedConfigure: 違禁控制參數。違禁内容包括：
<li>謾罵；</li>
<li>涉毒違法。</li>
注意：此參數尚未支援。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProhibitedConfigure: :class:`taifucloudcloud.mps.v20190612.models.ProhibitedConfigureInfo`
        :param UserDefineConfigure: 用戶自定義内容審核控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type UserDefineConfigure: :class:`taifucloudcloud.mps.v20190612.models.UserDefineConfigureInfo`
        :param CreateTime: 範本創建時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param UpdateTime: 範本最後修改時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type UpdateTime: str
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.PornConfigure = None
        self.TerrorismConfigure = None
        self.PoliticalConfigure = None
        self.ProhibitedConfigure = None
        self.UserDefineConfigure = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("PornConfigure") is not None:
            self.PornConfigure = PornConfigureInfo()
            self.PornConfigure._deserialize(params.get("PornConfigure"))
        if params.get("TerrorismConfigure") is not None:
            self.TerrorismConfigure = TerrorismConfigureInfo()
            self.TerrorismConfigure._deserialize(params.get("TerrorismConfigure"))
        if params.get("PoliticalConfigure") is not None:
            self.PoliticalConfigure = PoliticalConfigureInfo()
            self.PoliticalConfigure._deserialize(params.get("PoliticalConfigure"))
        if params.get("ProhibitedConfigure") is not None:
            self.ProhibitedConfigure = ProhibitedConfigureInfo()
            self.ProhibitedConfigure._deserialize(params.get("ProhibitedConfigure"))
        if params.get("UserDefineConfigure") is not None:
            self.UserDefineConfigure = UserDefineConfigureInfo()
            self.UserDefineConfigure._deserialize(params.get("UserDefineConfigure"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class CosFileUploadTrigger(AbstractModel):
    """綁定到 COS 的輸入規則。

    """

    def __init__(self):
        """
        :param Bucket: 工作流綁定的 COS Bucket 名，如 TopRankVideo-125xxx88。
        :type Bucket: str
        :param Region: 工作流綁定的 COS Bucket 所屬園區，如 ap-chongiqng。
        :type Region: str
        :param Dir: 工作流綁定的輸入路徑目錄，必須爲絕對路徑，即以 `/` 開頭和結尾。如`/movie/201907/`，不填代表根目錄`/`。
        :type Dir: str
        :param Formats: 工作流允許觸發的文件格式清單，如 ["mp4", "flv", "mov"]。不填代表所有格式的文件都可以觸發工作流。
        :type Formats: list of str
        """
        self.Bucket = None
        self.Region = None
        self.Dir = None
        self.Formats = None


    def _deserialize(self, params):
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.Dir = params.get("Dir")
        self.Formats = params.get("Formats")


class CosInputInfo(AbstractModel):
    """視訊處理 COS 對象訊息。

    """

    def __init__(self):
        """
        :param Bucket: 視訊處理對象文件所在的 COS Bucket 名，如 TopRankVideo-125xxx88。
        :type Bucket: str
        :param Region: 視訊處理對象文件所在的 COS Bucket 所屬園區，如 ap-chongqing。
        :type Region: str
        :param Object: 視訊處理對象文件的輸入路徑，如`/movie/201907/WildAnimal.mov`。
        :type Object: str
        """
        self.Bucket = None
        self.Region = None
        self.Object = None


    def _deserialize(self, params):
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.Object = params.get("Object")


class CosOutputStorage(AbstractModel):
    """視訊處理 COS 輸出對象訊息。

    """

    def __init__(self):
        """
        :param Bucket: 視訊處理生成的文件輸出的目標 Bucket 名，如 TopRankVideo-125xxx88。如果不填，表示繼承上層。
        :type Bucket: str
        :param Region: 視訊處理生成的文件輸出的目標 Bucket 的園區，如 ap-chongqing。如果不填，表示繼承上層。
        :type Region: str
        """
        self.Bucket = None
        self.Region = None


    def _deserialize(self, params):
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")


class CoverConfigureInfo(AbstractModel):
    """智慧封面任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 智慧封面任務開關，可選值：
<li>ON：開啓智慧封面任務；</li>
<li>OFF：關閉智慧封面任務。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class CoverConfigureInfoForUpdate(AbstractModel):
    """智慧封面任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 智慧封面任務開關，可選值：
<li>ON：開啓智慧封面任務；</li>
<li>OFF：關閉智慧封面任務。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class CreateAIAnalysisTemplateRequest(AbstractModel):
    """CreateAIAnalysisTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 視訊内容分析範本名稱，長度限制：64 個字元。
        :type Name: str
        :param Comment: 視訊内容分析範本描述訊息，長度限制：256 個字元。
        :type Comment: str
        :param ClassificationConfigure: 智慧分類任務控制參數。
        :type ClassificationConfigure: :class:`taifucloudcloud.mps.v20190612.models.ClassificationConfigureInfo`
        :param TagConfigure: 智慧標簽任務控制參數。
        :type TagConfigure: :class:`taifucloudcloud.mps.v20190612.models.TagConfigureInfo`
        :param CoverConfigure: 智慧封面任務控制參數。
        :type CoverConfigure: :class:`taifucloudcloud.mps.v20190612.models.CoverConfigureInfo`
        :param FrameTagConfigure: 智慧按幀標簽任務控制參數。
        :type FrameTagConfigure: :class:`taifucloudcloud.mps.v20190612.models.FrameTagConfigureInfo`
        """
        self.Name = None
        self.Comment = None
        self.ClassificationConfigure = None
        self.TagConfigure = None
        self.CoverConfigure = None
        self.FrameTagConfigure = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("ClassificationConfigure") is not None:
            self.ClassificationConfigure = ClassificationConfigureInfo()
            self.ClassificationConfigure._deserialize(params.get("ClassificationConfigure"))
        if params.get("TagConfigure") is not None:
            self.TagConfigure = TagConfigureInfo()
            self.TagConfigure._deserialize(params.get("TagConfigure"))
        if params.get("CoverConfigure") is not None:
            self.CoverConfigure = CoverConfigureInfo()
            self.CoverConfigure._deserialize(params.get("CoverConfigure"))
        if params.get("FrameTagConfigure") is not None:
            self.FrameTagConfigure = FrameTagConfigureInfo()
            self.FrameTagConfigure._deserialize(params.get("FrameTagConfigure"))


class CreateAIAnalysisTemplateResponse(AbstractModel):
    """CreateAIAnalysisTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param Definition: 視訊内容分析範本唯一標識。
        :type Definition: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateAIRecognitionTemplateRequest(AbstractModel):
    """CreateAIRecognitionTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 視訊内容識别範本名稱，長度限制：64 個字元。
        :type Name: str
        :param Comment: 視訊内容識别範本描述訊息，長度限制：256 個字元。
        :type Comment: str
        :param FaceConfigure: 人臉識别控制參數。
        :type FaceConfigure: :class:`taifucloudcloud.mps.v20190612.models.FaceConfigureInfo`
        :param OcrFullTextConfigure: 文本全文識别控制參數。
        :type OcrFullTextConfigure: :class:`taifucloudcloud.mps.v20190612.models.OcrFullTextConfigureInfo`
        :param OcrWordsConfigure: 文本關鍵詞識别控制參數。
        :type OcrWordsConfigure: :class:`taifucloudcloud.mps.v20190612.models.OcrWordsConfigureInfo`
        :param AsrFullTextConfigure: 語音全文識别控制參數。
        :type AsrFullTextConfigure: :class:`taifucloudcloud.mps.v20190612.models.AsrFullTextConfigureInfo`
        :param AsrWordsConfigure: 語音關鍵詞識别控制參數。
        :type AsrWordsConfigure: :class:`taifucloudcloud.mps.v20190612.models.AsrWordsConfigureInfo`
        """
        self.Name = None
        self.Comment = None
        self.FaceConfigure = None
        self.OcrFullTextConfigure = None
        self.OcrWordsConfigure = None
        self.AsrFullTextConfigure = None
        self.AsrWordsConfigure = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("FaceConfigure") is not None:
            self.FaceConfigure = FaceConfigureInfo()
            self.FaceConfigure._deserialize(params.get("FaceConfigure"))
        if params.get("OcrFullTextConfigure") is not None:
            self.OcrFullTextConfigure = OcrFullTextConfigureInfo()
            self.OcrFullTextConfigure._deserialize(params.get("OcrFullTextConfigure"))
        if params.get("OcrWordsConfigure") is not None:
            self.OcrWordsConfigure = OcrWordsConfigureInfo()
            self.OcrWordsConfigure._deserialize(params.get("OcrWordsConfigure"))
        if params.get("AsrFullTextConfigure") is not None:
            self.AsrFullTextConfigure = AsrFullTextConfigureInfo()
            self.AsrFullTextConfigure._deserialize(params.get("AsrFullTextConfigure"))
        if params.get("AsrWordsConfigure") is not None:
            self.AsrWordsConfigure = AsrWordsConfigureInfo()
            self.AsrWordsConfigure._deserialize(params.get("AsrWordsConfigure"))


class CreateAIRecognitionTemplateResponse(AbstractModel):
    """CreateAIRecognitionTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param Definition: 視訊内容識别範本唯一標識。
        :type Definition: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateAnimatedGraphicsTemplateRequest(AbstractModel):
    """CreateAnimatedGraphicsTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Fps: 幀率，取值範圍：[1, 30]，單位：Hz。
        :type Fps: int
        :param Width: 動圖寬度（或長邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
        :type Width: int
        :param Height: 動圖高度（或短邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适應，可選值：
<li>open：開啓，此時，Width 代表視訊的長邊，Height 表示視訊的短邊；</li>
<li>close：關閉，此時，Width 代表視訊的寬度，Height 表示視訊的高度。</li>
預設值：open。
        :type ResolutionAdaptive: str
        :param Format: 動圖格式，取值爲 gif 和 webp。預設爲 gif。
        :type Format: str
        :param Quality: 圖片質量，取值範圍：[1, 100]，預設值爲 75。
        :type Quality: float
        :param Name: 轉動圖範本名稱，長度限制：64 個字元。
        :type Name: str
        :param Comment: 範本描述訊息，長度限制：256 個字元。
        :type Comment: str
        """
        self.Fps = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Quality = None
        self.Name = None
        self.Comment = None


    def _deserialize(self, params):
        self.Fps = params.get("Fps")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Quality = params.get("Quality")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")


class CreateAnimatedGraphicsTemplateResponse(AbstractModel):
    """CreateAnimatedGraphicsTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param Definition: 轉動圖範本唯一標識。
        :type Definition: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateContentReviewTemplateRequest(AbstractModel):
    """CreateContentReviewTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 内容審核範本名稱，長度限制：64 個字元。
        :type Name: str
        :param Comment: 内容審核範本描述訊息，長度限制：256 個字元。
        :type Comment: str
        :param PornConfigure:  控制參數。
        :type PornConfigure: :class:`taifucloudcloud.mps.v20190612.models.PornConfigureInfo`
        :param TerrorismConfigure: 鑒恐控制參數。
        :type TerrorismConfigure: :class:`taifucloudcloud.mps.v20190612.models.TerrorismConfigureInfo`
        :param PoliticalConfigure: 鑒政控制參數。
        :type PoliticalConfigure: :class:`taifucloudcloud.mps.v20190612.models.PoliticalConfigureInfo`
        :param ProhibitedConfigure: 違禁控制參數。違禁内容包括：
<li>謾罵；</li>
<li>涉毒違法。</li>
注意：此參數尚未支援。
        :type ProhibitedConfigure: :class:`taifucloudcloud.mps.v20190612.models.ProhibitedConfigureInfo`
        :param UserDefineConfigure: 用戶自定義内容審核控制參數。
        :type UserDefineConfigure: :class:`taifucloudcloud.mps.v20190612.models.UserDefineConfigureInfo`
        """
        self.Name = None
        self.Comment = None
        self.PornConfigure = None
        self.TerrorismConfigure = None
        self.PoliticalConfigure = None
        self.ProhibitedConfigure = None
        self.UserDefineConfigure = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("PornConfigure") is not None:
            self.PornConfigure = PornConfigureInfo()
            self.PornConfigure._deserialize(params.get("PornConfigure"))
        if params.get("TerrorismConfigure") is not None:
            self.TerrorismConfigure = TerrorismConfigureInfo()
            self.TerrorismConfigure._deserialize(params.get("TerrorismConfigure"))
        if params.get("PoliticalConfigure") is not None:
            self.PoliticalConfigure = PoliticalConfigureInfo()
            self.PoliticalConfigure._deserialize(params.get("PoliticalConfigure"))
        if params.get("ProhibitedConfigure") is not None:
            self.ProhibitedConfigure = ProhibitedConfigureInfo()
            self.ProhibitedConfigure._deserialize(params.get("ProhibitedConfigure"))
        if params.get("UserDefineConfigure") is not None:
            self.UserDefineConfigure = UserDefineConfigureInfo()
            self.UserDefineConfigure._deserialize(params.get("UserDefineConfigure"))


class CreateContentReviewTemplateResponse(AbstractModel):
    """CreateContentReviewTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param Definition: 内容審核範本唯一標識。
        :type Definition: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateImageSpriteTemplateRequest(AbstractModel):
    """CreateImageSpriteTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param SampleType: 采樣類型，取值：
<li>Percent：按百分比。</li>
<li>Time：按時間間隔。</li>
        :type SampleType: str
        :param SampleInterval: 采樣間隔。
<li>當 SampleType 爲 Percent 時，指定采樣間隔的百分比。</li>
<li>當 SampleType 爲 Time 時，指定采樣間隔的時間，單位爲秒。</li>
        :type SampleInterval: int
        :param RowCount: 雪碧圖中小圖的行數。
        :type RowCount: int
        :param ColumnCount: 雪碧圖中小圖的列數。
        :type ColumnCount: int
        :param Name: 雪碧圖範本名稱，長度限制：64 個字元。
        :type Name: str
        :param Width: 雪碧圖中小圖的寬度（或長邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
        :type Width: int
        :param Height: 雪碧圖中小圖的高度（或短邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适應，可選值：
<li>open：開啓，此時，Width 代表視訊的長邊，Height 表示視訊的短邊；</li>
<li>close：關閉，此時，Width 代表視訊的寬度，Height 表示視訊的高度。</li>
預設值：open。
        :type ResolutionAdaptive: str
        :param FillType: 填充方式，當視訊流配置寬高參數與原始視訊的寬高比不一緻時，對轉碼的處理方式，即爲“填充”。可選填充方式：
<li> stretch：拉伸，對每一幀進行拉伸，填滿整個畫面，可能導緻轉碼後的視訊被“壓扁“或者“拉長“；</li>
<li>black：留黑，保持視訊寬高比不變，邊緣剩餘部分使用黑色填充。</li>
預設值：black 。
        :type FillType: str
        :param Comment: 範本描述訊息，長度限制：256 個字元。
        :type Comment: str
        """
        self.SampleType = None
        self.SampleInterval = None
        self.RowCount = None
        self.ColumnCount = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.FillType = None
        self.Comment = None


    def _deserialize(self, params):
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.RowCount = params.get("RowCount")
        self.ColumnCount = params.get("ColumnCount")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.FillType = params.get("FillType")
        self.Comment = params.get("Comment")


class CreateImageSpriteTemplateResponse(AbstractModel):
    """CreateImageSpriteTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param Definition: 雪碧圖範本唯一標識。
        :type Definition: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreatePersonSampleRequest(AbstractModel):
    """CreatePersonSample請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 人物名稱，長度限制：20 個字元。
        :type Name: str
        :param Usages: 人物應用場景，可選值：
1. Recognition：用於内容識别，等價於 Recognition.Face。
2. Review：用於内容審核，等價於 Review.Face。
3. All：用於内容識别、内容審核，等價於 1+2。
        :type Usages: list of str
        :param Description: 人物描述，長度限制：1024 個字元。
        :type Description: str
        :param FaceContents: 人臉圖片 [Base64](https://tools.ietf.org/html/rfc4648) 編碼後的字串，僅支援 jpeg、png 圖片格式。數組長度限制：5 張圖片。
注意：圖片必須是單人像正面人臉較清晰的照片，像素不低於 200*200。
        :type FaceContents: list of str
        :param Tags: 人物標簽
<li>數組長度限制：20 個標簽；</li>
<li>單個標簽長度限制：128 個字元。</li>
        :type Tags: list of str
        """
        self.Name = None
        self.Usages = None
        self.Description = None
        self.FaceContents = None
        self.Tags = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Usages = params.get("Usages")
        self.Description = params.get("Description")
        self.FaceContents = params.get("FaceContents")
        self.Tags = params.get("Tags")


class CreatePersonSampleResponse(AbstractModel):
    """CreatePersonSample返回參數結構體

    """

    def __init__(self):
        """
        :param Person: 人物訊息。
        :type Person: :class:`taifucloudcloud.mps.v20190612.models.AiSamplePerson`
        :param FailFaceInfoSet: 處理失敗的人臉訊息。
        :type FailFaceInfoSet: list of AiSampleFailFaceInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Person = None
        self.FailFaceInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Person") is not None:
            self.Person = AiSamplePerson()
            self.Person._deserialize(params.get("Person"))
        if params.get("FailFaceInfoSet") is not None:
            self.FailFaceInfoSet = []
            for item in params.get("FailFaceInfoSet"):
                obj = AiSampleFailFaceInfo()
                obj._deserialize(item)
                self.FailFaceInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class CreateSampleSnapshotTemplateRequest(AbstractModel):
    """CreateSampleSnapshotTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param SampleType: 采樣截圖類型，取值：
<li>Percent：按百分比。</li>
<li>Time：按時間間隔。</li>
        :type SampleType: str
        :param SampleInterval: 采樣間隔。
<li>當 SampleType 爲 Percent 時，指定采樣間隔的百分比。</li>
<li>當 SampleType 爲 Time 時，指定采樣間隔的時間，單位爲秒。</li>
        :type SampleInterval: int
        :param Name: 采樣截圖範本名稱，長度限制：64 個字元。
        :type Name: str
        :param Width: 截圖寬度（或長邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
        :type Width: int
        :param Height: 截圖高度（或短邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适應，可選值：
<li>open：開啓，此時，Width 代表視訊的長邊，Height 表示視訊的短邊；</li>
<li>close：關閉，此時，Width 代表視訊的寬度，Height 表示視訊的高度。</li>
預設值：open。
        :type ResolutionAdaptive: str
        :param Format: 圖片格式，取值爲 jpg 和 png。預設爲 jpg。
        :type Format: str
        :param Comment: 範本描述訊息，長度限制：256 個字元。
        :type Comment: str
        :param FillType: 填充方式，當視訊流配置寬高參數與原始視訊的寬高比不一緻時，對轉碼的處理方式，即爲“填充”。可選填充方式：
<li> stretch：拉伸，對每一幀進行拉伸，填滿整個畫面，可能導緻轉碼後的視訊被“壓扁“或者“拉長“；</li>
<li>black：留黑，保持視訊寬高比不變，邊緣剩餘部分使用黑色填充。</li>
<li>white：留白，保持視訊寬高比不變，邊緣剩餘部分使用白色填充。</li>
<li>gauss：高斯模糊，保持視訊寬高比不變，邊緣剩餘部分使用高斯模糊。</li>
預設值：black 。
        :type FillType: str
        """
        self.SampleType = None
        self.SampleInterval = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Comment = None
        self.FillType = None


    def _deserialize(self, params):
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")
        self.FillType = params.get("FillType")


class CreateSampleSnapshotTemplateResponse(AbstractModel):
    """CreateSampleSnapshotTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param Definition: 采樣截圖範本唯一標識。
        :type Definition: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateSnapshotByTimeOffsetTemplateRequest(AbstractModel):
    """CreateSnapshotByTimeOffsetTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 指定時間點截圖範本名稱，長度限制：64 個字元。
        :type Name: str
        :param Width: 截圖寬度（或長邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
        :type Width: int
        :param Height: 截圖高度（或短邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适應，可選值：
<li>open：開啓，此時，Width 代表視訊的長邊，Height 表示視訊的短邊；</li>
<li>close：關閉，此時，Width 代表視訊的寬度，Height 表示視訊的高度。</li>
預設值：open。
        :type ResolutionAdaptive: str
        :param Format: 圖片格式，取值可以爲 jpg 和 png。預設爲 jpg。
        :type Format: str
        :param Comment: 範本描述訊息，長度限制：256 個字元。
        :type Comment: str
        :param FillType: 填充方式，當視訊流配置寬高參數與原始視訊的寬高比不一緻時，對轉碼的處理方式，即爲“填充”。可選填充方式：
<li> stretch：拉伸，對每一幀進行拉伸，填滿整個畫面，可能導緻轉碼後的視訊被“壓扁“或者“拉長“；</li>
<li>black：留黑，保持視訊寬高比不變，邊緣剩餘部分使用黑色填充。</li>
<li>white：留白，保持視訊寬高比不變，邊緣剩餘部分使用白色填充。</li>
<li>gauss：高斯模糊，保持視訊寬高比不變，邊緣剩餘部分使用高斯模糊。</li>
預設值：black 。
        :type FillType: str
        """
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Comment = None
        self.FillType = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")
        self.FillType = params.get("FillType")


class CreateSnapshotByTimeOffsetTemplateResponse(AbstractModel):
    """CreateSnapshotByTimeOffsetTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param Definition: 時間點截圖範本唯一標識。
        :type Definition: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateTranscodeTemplateRequest(AbstractModel):
    """CreateTranscodeTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Container: 封裝格式，可選值：mp4、flv、hls、mp3、flac、ogg、m4a。其中，mp3、flac、ogg、m4a 爲純音訊文件。
        :type Container: str
        :param Name: 轉碼範本名稱，長度限制：64 個字元。
        :type Name: str
        :param Comment: 範本描述訊息，長度限制：256 個字元。
        :type Comment: str
        :param RemoveVideo: 是否去除視訊數據，可選值：
<li>0：保留</li>
<li>1：去除</li>
預設值：0。
        :type RemoveVideo: int
        :param RemoveAudio: 是否去除音訊數據，可選值：
<li>0：保留</li>
<li>1：去除</li>
預設值：0。
        :type RemoveAudio: int
        :param VideoTemplate: 視訊流配置參數，當 RemoveVideo 爲 0，該欄位必填。
        :type VideoTemplate: :class:`taifucloudcloud.mps.v20190612.models.VideoTemplateInfo`
        :param AudioTemplate: 音訊流配置參數，當 RemoveAudio 爲 0，該欄位必填。
        :type AudioTemplate: :class:`taifucloudcloud.mps.v20190612.models.AudioTemplateInfo`
        :param TEHDConfig: 極速高清轉碼參數。
        :type TEHDConfig: :class:`taifucloudcloud.mps.v20190612.models.TEHDConfig`
        """
        self.Container = None
        self.Name = None
        self.Comment = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.TEHDConfig = None


    def _deserialize(self, params):
        self.Container = params.get("Container")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfo()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfo()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfig()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))


class CreateTranscodeTemplateResponse(AbstractModel):
    """CreateTranscodeTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param Definition: 轉碼範本唯一標識。
        :type Definition: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateWatermarkTemplateRequest(AbstractModel):
    """CreateWatermarkTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Type: 浮水印類型，可選值：
<li>image：圖片浮水印；</li>
<li>text：文字浮水印；</li>
<li>svg：SVG 浮水印。</li>
        :type Type: str
        :param Name: 浮水印範本名稱，長度限制：64 個字元。
        :type Name: str
        :param Comment: 範本描述訊息，長度限制：256 個字元。
        :type Comment: str
        :param CoordinateOrigin: 原點位置，可選值：
<li>TopLeft：表示坐標原點位於視訊圖像左上角，浮水印原點爲圖片或文字的左上角；</li>
<li>TopRight：表示坐標原點位於視訊圖像的右上角，浮水印原點爲圖片或文字的右上角；</li>
<li>BottomLeft：表示坐標原點位於視訊圖像的左下角，浮水印原點爲圖片或文字的左下角；</li>
<li>BottomRight：表示坐標原點位於視訊圖像的右下角，浮水印原點爲圖片或文字的右下角。</li>
預設值：TopLeft。
        :type CoordinateOrigin: str
        :param XPos: 浮水印原點距離視訊圖像坐標原點的水平位置。支援 %、px 兩種格式：
<li>當字串以 % 結尾，表示浮水印 XPos 爲視訊寬度指定百分比，如 10% 表示 XPos 爲視訊寬度的 10%；</li>
<li>當字串以 px 結尾，表示浮水印 XPos 爲指定像素，如 100px 表示 XPos 爲 100 像素。</li>
預設值：0px。
        :type XPos: str
        :param YPos: 浮水印原點距離視訊圖像坐標原點的垂直位置。支援 %、px 兩種格式：
<li>當字串以 % 結尾，表示浮水印 YPos 爲視訊高度指定百分比，如 10% 表示 YPos 爲視訊高度的 10%；</li>
<li>當字串以 px 結尾，表示浮水印 YPos 爲指定像素，如 100px 表示 YPos 爲 100 像素。</li>
預設值：0px。
        :type YPos: str
        :param ImageTemplate: 圖片浮水印範本，僅當 Type 爲 image，該欄位必填且有效。
        :type ImageTemplate: :class:`taifucloudcloud.mps.v20190612.models.ImageWatermarkInput`
        :param TextTemplate: 文字浮水印範本，僅當 Type 爲 text，該欄位必填且有效。
        :type TextTemplate: :class:`taifucloudcloud.mps.v20190612.models.TextWatermarkTemplateInput`
        :param SvgTemplate: SVG 浮水印範本，僅當 Type 爲 svg，該欄位必填且有效。
        :type SvgTemplate: :class:`taifucloudcloud.mps.v20190612.models.SvgWatermarkInput`
        """
        self.Type = None
        self.Name = None
        self.Comment = None
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.ImageTemplate = None
        self.TextTemplate = None
        self.SvgTemplate = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        if params.get("ImageTemplate") is not None:
            self.ImageTemplate = ImageWatermarkInput()
            self.ImageTemplate._deserialize(params.get("ImageTemplate"))
        if params.get("TextTemplate") is not None:
            self.TextTemplate = TextWatermarkTemplateInput()
            self.TextTemplate._deserialize(params.get("TextTemplate"))
        if params.get("SvgTemplate") is not None:
            self.SvgTemplate = SvgWatermarkInput()
            self.SvgTemplate._deserialize(params.get("SvgTemplate"))


class CreateWatermarkTemplateResponse(AbstractModel):
    """CreateWatermarkTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param Definition: 浮水印範本唯一標識。
        :type Definition: int
        :param ImageUrl: 浮水印圖片網址，僅當 Type 爲 image，該欄位有效。
        :type ImageUrl: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Definition = None
        self.ImageUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.ImageUrl = params.get("ImageUrl")
        self.RequestId = params.get("RequestId")


class CreateWordSamplesRequest(AbstractModel):
    """CreateWordSamples請求參數結構體

    """

    def __init__(self):
        """
        :param Usages: <b>關鍵詞應用場景，可選值：</b>
1. Recognition.Ocr：通過光學字元識别技術，進行内容識别；
2. Recognition.Asr：通過語音識别技術，進行内容識别；
3. Review.Ocr：通過光學字元識别技術，進行内容審核；
4. Review.Asr：通過語音識别技術，進行内容審核；
<b>可合並簡寫爲：</b>
5. Recognition：通過光學字元識别技術、語音識别技術，進行内容識别，等價於 1+2；
6. Review：通過光學字元識别技術、語音識别技術，進行内容審核，等價於 3+4；
7. All：通過光學字元識别技術、語音識别技術，進行内容識别、内容審核，等價於 1+2+3+4。
        :type Usages: list of str
        :param Words: 關鍵詞，數組長度限制：100。
        :type Words: list of AiSampleWordInfo
        """
        self.Usages = None
        self.Words = None


    def _deserialize(self, params):
        self.Usages = params.get("Usages")
        if params.get("Words") is not None:
            self.Words = []
            for item in params.get("Words"):
                obj = AiSampleWordInfo()
                obj._deserialize(item)
                self.Words.append(obj)


class CreateWordSamplesResponse(AbstractModel):
    """CreateWordSamples返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateWorkflowRequest(AbstractModel):
    """CreateWorkflow請求參數結構體

    """

    def __init__(self):
        """
        :param WorkflowName: 工作流名稱，最多128字元。同一個用戶該名稱唯一。
        :type WorkflowName: str
        :param Trigger: 工作流綁定的觸發規則，當上傳視訊命中該規則到該對象時即觸發工作流。
        :type Trigger: :class:`taifucloudcloud.mps.v20190612.models.WorkflowTrigger`
        :param OutputStorage: 視訊處理的文件輸出儲存位置。不填則繼承 Trigger 中的儲存位置。
        :type OutputStorage: :class:`taifucloudcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputDir: 視訊處理生成的文件輸出的目標目錄，如`/movie/201907/`。如果不填，表示與觸發文件所在的目錄一緻。
        :type OutputDir: str
        :param MediaProcessTask: 視訊處理類型任務參數。
        :type MediaProcessTask: :class:`taifucloudcloud.mps.v20190612.models.MediaProcessTaskInput`
        :param AiContentReviewTask: 視訊内容審核類型任務參數。
        :type AiContentReviewTask: :class:`taifucloudcloud.mps.v20190612.models.AiContentReviewTaskInput`
        :param AiAnalysisTask: 視訊内容分析類型任務參數。
        :type AiAnalysisTask: :class:`taifucloudcloud.mps.v20190612.models.AiAnalysisTaskInput`
        :param AiRecognitionTask: 視訊内容識别類型任務參數。
        :type AiRecognitionTask: :class:`taifucloudcloud.mps.v20190612.models.AiRecognitionTaskInput`
        :param TaskNotifyConfig: 任務的事件通知配置，不填代表不獲取事件通知。
        :type TaskNotifyConfig: :class:`taifucloudcloud.mps.v20190612.models.TaskNotifyConfig`
        :param TaskPriority: 工作流的優先級，數值越大優先級越高，取值範圍是 -10 到 10，不填代表 0。
        :type TaskPriority: int
        """
        self.WorkflowName = None
        self.Trigger = None
        self.OutputStorage = None
        self.OutputDir = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.TaskNotifyConfig = None
        self.TaskPriority = None


    def _deserialize(self, params):
        self.WorkflowName = params.get("WorkflowName")
        if params.get("Trigger") is not None:
            self.Trigger = WorkflowTrigger()
            self.Trigger._deserialize(params.get("Trigger"))
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputDir = params.get("OutputDir")
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        self.TaskPriority = params.get("TaskPriority")


class CreateWorkflowResponse(AbstractModel):
    """CreateWorkflow返回參數結構體

    """

    def __init__(self):
        """
        :param WorkflowId: 工作流 ID。
        :type WorkflowId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.WorkflowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")
        self.RequestId = params.get("RequestId")


class DeleteAIAnalysisTemplateRequest(AbstractModel):
    """DeleteAIAnalysisTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Definition: 視訊内容分析範本唯一標識。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class DeleteAIAnalysisTemplateResponse(AbstractModel):
    """DeleteAIAnalysisTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAIRecognitionTemplateRequest(AbstractModel):
    """DeleteAIRecognitionTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Definition: 視訊内容識别範本唯一標識。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class DeleteAIRecognitionTemplateResponse(AbstractModel):
    """DeleteAIRecognitionTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAnimatedGraphicsTemplateRequest(AbstractModel):
    """DeleteAnimatedGraphicsTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Definition: 轉動圖範本唯一標識。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class DeleteAnimatedGraphicsTemplateResponse(AbstractModel):
    """DeleteAnimatedGraphicsTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteContentReviewTemplateRequest(AbstractModel):
    """DeleteContentReviewTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Definition: 内容審核範本唯一標識。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class DeleteContentReviewTemplateResponse(AbstractModel):
    """DeleteContentReviewTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImageSpriteTemplateRequest(AbstractModel):
    """DeleteImageSpriteTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Definition: 雪碧圖範本唯一標識。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class DeleteImageSpriteTemplateResponse(AbstractModel):
    """DeleteImageSpriteTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePersonSampleRequest(AbstractModel):
    """DeletePersonSample請求參數結構體

    """

    def __init__(self):
        """
        :param PersonId: 人物 ID。
        :type PersonId: str
        """
        self.PersonId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")


class DeletePersonSampleResponse(AbstractModel):
    """DeletePersonSample返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSampleSnapshotTemplateRequest(AbstractModel):
    """DeleteSampleSnapshotTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Definition: 采樣截圖範本唯一標識。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class DeleteSampleSnapshotTemplateResponse(AbstractModel):
    """DeleteSampleSnapshotTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSnapshotByTimeOffsetTemplateRequest(AbstractModel):
    """DeleteSnapshotByTimeOffsetTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Definition: 指定時間點截圖範本唯一標識。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class DeleteSnapshotByTimeOffsetTemplateResponse(AbstractModel):
    """DeleteSnapshotByTimeOffsetTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTranscodeTemplateRequest(AbstractModel):
    """DeleteTranscodeTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Definition: 轉碼範本唯一標識。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class DeleteTranscodeTemplateResponse(AbstractModel):
    """DeleteTranscodeTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWatermarkTemplateRequest(AbstractModel):
    """DeleteWatermarkTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Definition: 浮水印範本唯一標識。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class DeleteWatermarkTemplateResponse(AbstractModel):
    """DeleteWatermarkTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWordSamplesRequest(AbstractModel):
    """DeleteWordSamples請求參數結構體

    """

    def __init__(self):
        """
        :param Keywords: 關鍵詞，數組長度限制：100 個詞。
        :type Keywords: list of str
        """
        self.Keywords = None


    def _deserialize(self, params):
        self.Keywords = params.get("Keywords")


class DeleteWordSamplesResponse(AbstractModel):
    """DeleteWordSamples返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWorkflowRequest(AbstractModel):
    """DeleteWorkflow請求參數結構體

    """

    def __init__(self):
        """
        :param WorkflowId: 工作流 ID。
        :type WorkflowId: int
        """
        self.WorkflowId = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")


class DeleteWorkflowResponse(AbstractModel):
    """DeleteWorkflow返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAIAnalysisTemplatesRequest(AbstractModel):
    """DescribeAIAnalysisTemplates請求參數結構體

    """

    def __init__(self):
        """
        :param Definitions: 視訊内容分析範本唯一標識過濾條件，數組長度限制：10。
        :type Definitions: list of int
        :param Offset: 分頁偏移量，預設值：0。
        :type Offset: int
        :param Limit: 返回記錄條數，預設值：10，最大值：100。
        :type Limit: int
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAIAnalysisTemplatesResponse(AbstractModel):
    """DescribeAIAnalysisTemplates返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合過濾條件的記錄總數。
        :type TotalCount: int
        :param AIAnalysisTemplateSet: 視訊内容分析範本詳情清單。
        :type AIAnalysisTemplateSet: list of AIAnalysisTemplateItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AIAnalysisTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AIAnalysisTemplateSet") is not None:
            self.AIAnalysisTemplateSet = []
            for item in params.get("AIAnalysisTemplateSet"):
                obj = AIAnalysisTemplateItem()
                obj._deserialize(item)
                self.AIAnalysisTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAIRecognitionTemplatesRequest(AbstractModel):
    """DescribeAIRecognitionTemplates請求參數結構體

    """

    def __init__(self):
        """
        :param Definitions: 視訊内容識别範本唯一標識過濾條件，數組長度限制：10。
        :type Definitions: list of int
        :param Offset: 分頁偏移量，預設值：0。
        :type Offset: int
        :param Limit: 返回記錄條數，預設值：10，最大值：50。
        :type Limit: int
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAIRecognitionTemplatesResponse(AbstractModel):
    """DescribeAIRecognitionTemplates返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合過濾條件的記錄總數。
        :type TotalCount: int
        :param AIRecognitionTemplateSet: 視訊内容識别範本詳情清單。
        :type AIRecognitionTemplateSet: list of AIRecognitionTemplateItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AIRecognitionTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AIRecognitionTemplateSet") is not None:
            self.AIRecognitionTemplateSet = []
            for item in params.get("AIRecognitionTemplateSet"):
                obj = AIRecognitionTemplateItem()
                obj._deserialize(item)
                self.AIRecognitionTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAnimatedGraphicsTemplatesRequest(AbstractModel):
    """DescribeAnimatedGraphicsTemplates請求參數結構體

    """

    def __init__(self):
        """
        :param Definitions: 轉動圖範本唯一標識過濾條件，數組長度限制：100。
        :type Definitions: list of int non-negative
        :param Offset: 分頁偏移量，預設值：0。
        :type Offset: int
        :param Limit: 返回記錄條數，預設值：10，最大值：100。
        :type Limit: int
        :param Type: 範本類型過濾條件，可選值：
<li>Preset：系統預置範本；</li>
<li>Custom：用戶自定義範本。</li>
        :type Type: str
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")


class DescribeAnimatedGraphicsTemplatesResponse(AbstractModel):
    """DescribeAnimatedGraphicsTemplates返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合過濾條件的記錄總數。
        :type TotalCount: int
        :param AnimatedGraphicsTemplateSet: 轉動圖範本詳情清單。
        :type AnimatedGraphicsTemplateSet: list of AnimatedGraphicsTemplate
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AnimatedGraphicsTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AnimatedGraphicsTemplateSet") is not None:
            self.AnimatedGraphicsTemplateSet = []
            for item in params.get("AnimatedGraphicsTemplateSet"):
                obj = AnimatedGraphicsTemplate()
                obj._deserialize(item)
                self.AnimatedGraphicsTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeContentReviewTemplatesRequest(AbstractModel):
    """DescribeContentReviewTemplates請求參數結構體

    """

    def __init__(self):
        """
        :param Definitions: 内容審核範本唯一標識過濾條件，數組長度限制：50。
        :type Definitions: list of int
        :param Offset: 分頁偏移量，預設值：0。
        :type Offset: int
        :param Limit: 返回記錄條數，預設值：10，最大值：50。
        :type Limit: int
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeContentReviewTemplatesResponse(AbstractModel):
    """DescribeContentReviewTemplates返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合過濾條件的記錄總數。
        :type TotalCount: int
        :param ContentReviewTemplateSet: 内容審核範本詳情清單。
        :type ContentReviewTemplateSet: list of ContentReviewTemplateItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ContentReviewTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ContentReviewTemplateSet") is not None:
            self.ContentReviewTemplateSet = []
            for item in params.get("ContentReviewTemplateSet"):
                obj = ContentReviewTemplateItem()
                obj._deserialize(item)
                self.ContentReviewTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImageSpriteTemplatesRequest(AbstractModel):
    """DescribeImageSpriteTemplates請求參數結構體

    """

    def __init__(self):
        """
        :param Definitions: 雪碧圖範本唯一標識過濾條件，數組長度限制：100。
        :type Definitions: list of int non-negative
        :param Offset: 分頁偏移量，預設值：0。
        :type Offset: int
        :param Limit: 返回記錄條數，預設值：10，最大值：100。
        :type Limit: int
        :param Type: 範本類型過濾條件，可選值：
<li>Preset：系統預置範本；</li>
<li>Custom：用戶自定義範本。</li>
        :type Type: str
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")


class DescribeImageSpriteTemplatesResponse(AbstractModel):
    """DescribeImageSpriteTemplates返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合過濾條件的記錄總數。
        :type TotalCount: int
        :param ImageSpriteTemplateSet: 雪碧圖範本詳情清單。
        :type ImageSpriteTemplateSet: list of ImageSpriteTemplate
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ImageSpriteTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ImageSpriteTemplateSet") is not None:
            self.ImageSpriteTemplateSet = []
            for item in params.get("ImageSpriteTemplateSet"):
                obj = ImageSpriteTemplate()
                obj._deserialize(item)
                self.ImageSpriteTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMediaMetaDataRequest(AbstractModel):
    """DescribeMediaMetaData請求參數結構體

    """

    def __init__(self):
        """
        :param InputInfo: 需要獲取元訊息的文件輸入訊息。
        :type InputInfo: :class:`taifucloudcloud.mps.v20190612.models.MediaInputInfo`
        """
        self.InputInfo = None


    def _deserialize(self, params):
        if params.get("InputInfo") is not None:
            self.InputInfo = MediaInputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))


class DescribeMediaMetaDataResponse(AbstractModel):
    """DescribeMediaMetaData返回參數結構體

    """

    def __init__(self):
        """
        :param MetaData: 媒體元訊息。
        :type MetaData: :class:`taifucloudcloud.mps.v20190612.models.MediaMetaData`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.MetaData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        self.RequestId = params.get("RequestId")


class DescribePersonSamplesRequest(AbstractModel):
    """DescribePersonSamples請求參數結構體

    """

    def __init__(self):
        """
        :param Type: 拉取的人物類型，可選值：
<li>UserDefine：用戶自定義人物庫；</li>
<li>Default：系統預設人物庫。</li>

預設值：UserDefine，拉取用戶自定義人物庫人物。
說明：如果是拉取系統預設人物庫，只能使用人物名字或者人物 ID + 人物名字的方式進行拉取，且人臉圖片只返回一張。
        :type Type: str
        :param PersonIds: 人物 ID，數組長度限制：100。
        :type PersonIds: list of str
        :param Names: 人物名稱，數組長度限制：20。
        :type Names: list of str
        :param Tags: 人物標簽，數組長度限制：20。
        :type Tags: list of str
        :param Offset: 分頁偏移量，預設值：0。
        :type Offset: int
        :param Limit: 返回記錄條數，預設值：100，最大值：100。
        :type Limit: int
        """
        self.Type = None
        self.PersonIds = None
        self.Names = None
        self.Tags = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.PersonIds = params.get("PersonIds")
        self.Names = params.get("Names")
        self.Tags = params.get("Tags")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribePersonSamplesResponse(AbstractModel):
    """DescribePersonSamples返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的記錄總數。
        :type TotalCount: int
        :param PersonSet: 人物訊息。
        :type PersonSet: list of AiSamplePerson
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.PersonSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PersonSet") is not None:
            self.PersonSet = []
            for item in params.get("PersonSet"):
                obj = AiSamplePerson()
                obj._deserialize(item)
                self.PersonSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSampleSnapshotTemplatesRequest(AbstractModel):
    """DescribeSampleSnapshotTemplates請求參數結構體

    """

    def __init__(self):
        """
        :param Definitions: 采樣截圖範本唯一標識過濾條件，數組長度限制：100。
        :type Definitions: list of int non-negative
        :param Offset: 分頁偏移量，預設值：0。
        :type Offset: int
        :param Limit: 返回記錄條數，預設值：10，最大值：100。
        :type Limit: int
        :param Type: 範本類型過濾條件，可選值：
<li>Preset：系統預置範本；</li>
<li>Custom：用戶自定義範本。</li>
        :type Type: str
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")


class DescribeSampleSnapshotTemplatesResponse(AbstractModel):
    """DescribeSampleSnapshotTemplates返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合過濾條件的記錄總數。
        :type TotalCount: int
        :param SampleSnapshotTemplateSet: 采樣截圖範本詳情清單。
        :type SampleSnapshotTemplateSet: list of SampleSnapshotTemplate
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SampleSnapshotTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SampleSnapshotTemplateSet") is not None:
            self.SampleSnapshotTemplateSet = []
            for item in params.get("SampleSnapshotTemplateSet"):
                obj = SampleSnapshotTemplate()
                obj._deserialize(item)
                self.SampleSnapshotTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSnapshotByTimeOffsetTemplatesRequest(AbstractModel):
    """DescribeSnapshotByTimeOffsetTemplates請求參數結構體

    """

    def __init__(self):
        """
        :param Definitions: 指定時間點截圖範本唯一標識過濾條件，數組長度限制：100。
        :type Definitions: list of int non-negative
        :param Offset: 分頁偏移量，預設值：0。
        :type Offset: int
        :param Limit: 返回記錄條數，預設值：10，最大值：100。
        :type Limit: int
        :param Type: 範本類型過濾條件，可選值：
<li>Preset：系統預置範本；</li>
<li>Custom：用戶自定義範本。</li>
        :type Type: str
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")


class DescribeSnapshotByTimeOffsetTemplatesResponse(AbstractModel):
    """DescribeSnapshotByTimeOffsetTemplates返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合過濾條件的記錄總數。
        :type TotalCount: int
        :param SnapshotByTimeOffsetTemplateSet: 指定時間點截圖範本詳情清單。
        :type SnapshotByTimeOffsetTemplateSet: list of SnapshotByTimeOffsetTemplate
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SnapshotByTimeOffsetTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SnapshotByTimeOffsetTemplateSet") is not None:
            self.SnapshotByTimeOffsetTemplateSet = []
            for item in params.get("SnapshotByTimeOffsetTemplateSet"):
                obj = SnapshotByTimeOffsetTemplate()
                obj._deserialize(item)
                self.SnapshotByTimeOffsetTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskDetailRequest(AbstractModel):
    """DescribeTaskDetail請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 視訊處理任務的任務 ID。
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class DescribeTaskDetailResponse(AbstractModel):
    """DescribeTaskDetail返回參數結構體

    """

    def __init__(self):
        """
        :param TaskType: 任務類型，目前取值有：
<li>WorkflowTask：視訊工作流處理任務。</li>
<li>EditMediaTask：視訊編輯任務。</li>
<li>LiveStreamProcessTask：直播流處理任務。</li>
        :type TaskType: str
        :param Status: 任務狀态，取值：
<li>WAITING：等待中；</li>
<li>PROCESSING：處理中；</li>
<li>FINISH：已完成。</li>
        :type Status: str
        :param CreateTime: 任務的創建時間，采用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param BeginProcessTime: 任務開始執行的時間，采用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type BeginProcessTime: str
        :param FinishTime: 任務執行完畢的時間，采用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type FinishTime: str
        :param WorkflowTask: 視訊處理任務訊息，僅當 TaskType 爲 WorkflowTask，該欄位有值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type WorkflowTask: :class:`taifucloudcloud.mps.v20190612.models.WorkflowTask`
        :param EditMediaTask: 視訊編輯任務訊息，僅當 TaskType 爲 EditMediaTask，該欄位有值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type EditMediaTask: :class:`taifucloudcloud.mps.v20190612.models.EditMediaTask`
        :param LiveStreamProcessTask: 直播流處理任務訊息，僅當 TaskType 爲 LiveStreamProcessTask，該欄位有值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type LiveStreamProcessTask: :class:`taifucloudcloud.mps.v20190612.models.LiveStreamProcessTask`
        :param TaskNotifyConfig: 任務的事件通知訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TaskNotifyConfig: :class:`taifucloudcloud.mps.v20190612.models.TaskNotifyConfig`
        :param TasksPriority: 任務流的優先級，取值範圍爲 [-10, 10]。
        :type TasksPriority: int
        :param SessionId: 用於去重的識别碼，如果七天内曾有過相同的識别碼的請求，則本次的請求會返回錯誤。最長50個字元，不帶或者帶空字串表示不做去重。
        :type SessionId: str
        :param SessionContext: 來源上下文，用於透傳用戶請求訊息，任務流狀态變更回調将返回該欄位值，最長1000個字元。
        :type SessionContext: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskType = None
        self.Status = None
        self.CreateTime = None
        self.BeginProcessTime = None
        self.FinishTime = None
        self.WorkflowTask = None
        self.EditMediaTask = None
        self.LiveStreamProcessTask = None
        self.TaskNotifyConfig = None
        self.TasksPriority = None
        self.SessionId = None
        self.SessionContext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.BeginProcessTime = params.get("BeginProcessTime")
        self.FinishTime = params.get("FinishTime")
        if params.get("WorkflowTask") is not None:
            self.WorkflowTask = WorkflowTask()
            self.WorkflowTask._deserialize(params.get("WorkflowTask"))
        if params.get("EditMediaTask") is not None:
            self.EditMediaTask = EditMediaTask()
            self.EditMediaTask._deserialize(params.get("EditMediaTask"))
        if params.get("LiveStreamProcessTask") is not None:
            self.LiveStreamProcessTask = LiveStreamProcessTask()
            self.LiveStreamProcessTask._deserialize(params.get("LiveStreamProcessTask"))
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        self.TasksPriority = params.get("TasksPriority")
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks請求參數結構體

    """

    def __init__(self):
        """
        :param Status: 過濾條件：任務狀态，可選值：WAITING（等待中）、PROCESSING（處理中）、FINISH（已完成）。
        :type Status: str
        :param Limit: 返回記錄條數，預設值：10，最大值：100。
        :type Limit: int
        :param ScrollToken: 翻頁標識，分批拉取時使用：當單次請求無法拉取所有數據，介面将會返回 ScrollToken，下一次請求攜帶該 Token，将會從下一條記錄開始獲取。
        :type ScrollToken: str
        """
        self.Status = None
        self.Limit = None
        self.ScrollToken = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Limit = params.get("Limit")
        self.ScrollToken = params.get("ScrollToken")


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回參數結構體

    """

    def __init__(self):
        """
        :param TaskSet: 任務概要清單。
        :type TaskSet: list of TaskSimpleInfo
        :param ScrollToken: 翻頁標識，當請求未返回所有數據，該欄位表示下一條記錄的 ID。當該欄位爲空字串，說明已無更多數據。
        :type ScrollToken: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskSet = None
        self.ScrollToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self.TaskSet = []
            for item in params.get("TaskSet"):
                obj = TaskSimpleInfo()
                obj._deserialize(item)
                self.TaskSet.append(obj)
        self.ScrollToken = params.get("ScrollToken")
        self.RequestId = params.get("RequestId")


class DescribeTranscodeTemplatesRequest(AbstractModel):
    """DescribeTranscodeTemplates請求參數結構體

    """

    def __init__(self):
        """
        :param Definitions: 轉碼範本唯一標識過濾條件，數組長度限制：100。
        :type Definitions: list of int
        :param Type: 範本類型過濾條件，可選值：
<li>Preset：系統預置範本；</li>
<li>Custom：用戶自定義範本。</li>
        :type Type: str
        :param ContainerType: 封裝格式過濾條件，可選值：
<li>Video：視訊格式，可以同時包含視訊流和音訊流的封裝格式板；</li>
<li>PureAudio：純音訊格式，只能包含音訊流的封裝格式。</li>
        :type ContainerType: str
        :param TEHDType: 極速高清過濾條件，用於過濾普通轉碼或極速高清轉碼範本，可選值：
<li>Common：普通轉碼範本；</li>
<li>TEHD：極速高清範本。</li>
        :type TEHDType: str
        :param Offset: 分頁偏移量，預設值：0。
        :type Offset: int
        :param Limit: 返回記錄條數，預設值：10，最大值：100。
        :type Limit: int
        """
        self.Definitions = None
        self.Type = None
        self.ContainerType = None
        self.TEHDType = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Type = params.get("Type")
        self.ContainerType = params.get("ContainerType")
        self.TEHDType = params.get("TEHDType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTranscodeTemplatesResponse(AbstractModel):
    """DescribeTranscodeTemplates返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合過濾條件的記錄總數。
        :type TotalCount: int
        :param TranscodeTemplateSet: 轉碼範本詳情清單。
        :type TranscodeTemplateSet: list of TranscodeTemplate
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TranscodeTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TranscodeTemplateSet") is not None:
            self.TranscodeTemplateSet = []
            for item in params.get("TranscodeTemplateSet"):
                obj = TranscodeTemplate()
                obj._deserialize(item)
                self.TranscodeTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWatermarkTemplatesRequest(AbstractModel):
    """DescribeWatermarkTemplates請求參數結構體

    """

    def __init__(self):
        """
        :param Definitions: 浮水印範本唯一標識過濾條件，數組長度限制：100。
        :type Definitions: list of int
        :param Type: 浮水印類型過濾條件，可選值：
<li>image：圖片浮水印；</li>
<li>text：文字浮水印。</li>
        :type Type: str
        :param Offset: 分頁偏移量，預設值：0。
        :type Offset: int
        :param Limit: 返回記錄條數
<li>預設值：10；</li>
<li>最大值：100。</li>
        :type Limit: int
        """
        self.Definitions = None
        self.Type = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Type = params.get("Type")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeWatermarkTemplatesResponse(AbstractModel):
    """DescribeWatermarkTemplates返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合過濾條件的記錄總數。
        :type TotalCount: int
        :param WatermarkTemplateSet: 浮水印範本詳情清單。
        :type WatermarkTemplateSet: list of WatermarkTemplate
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.WatermarkTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("WatermarkTemplateSet") is not None:
            self.WatermarkTemplateSet = []
            for item in params.get("WatermarkTemplateSet"):
                obj = WatermarkTemplate()
                obj._deserialize(item)
                self.WatermarkTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWordSamplesRequest(AbstractModel):
    """DescribeWordSamples請求參數結構體

    """

    def __init__(self):
        """
        :param Usages: <b>關鍵詞應用場景過濾條件，可選值：</b>
1. Recognition.Ocr：通過光學字元識别技術，進行内容識别；
2. Recognition.Asr：通過語音識别技術，進行内容識别；
3. Review.Ocr：通過光學字元識别技術，進行内容審核；
4. Review.Asr：通過語音識别技術，進行内容審核；
<b>可合並簡寫爲：</b>
5. Recognition：通過光學字元識别技術、語音識别技術，進行内容識别，等價於 1+2；
6. Review：通過光學字元識别技術、語音識别技術，進行内容審核，等價於 3+4；
可多選，元素間關系爲 or，即關鍵詞的應用場景包含該欄位集合中任意元素的記錄，均符合該條件。
        :type Usages: list of str
        :param Keywords: 關鍵詞過濾條件，數組長度限制：100 個詞。
        :type Keywords: list of str
        :param Tags: 標簽過濾條件，數組長度限制：20 個詞。
        :type Tags: list of str
        :param Offset: 分頁偏移量，預設值：0。
        :type Offset: int
        :param Limit: 返回記錄條數，預設值：100，最大值：100。
        :type Limit: int
        """
        self.Usages = None
        self.Keywords = None
        self.Tags = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Usages = params.get("Usages")
        self.Keywords = params.get("Keywords")
        self.Tags = params.get("Tags")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeWordSamplesResponse(AbstractModel):
    """DescribeWordSamples返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的記錄總數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param WordSet: 關鍵詞訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type WordSet: list of AiSampleWord
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.WordSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("WordSet") is not None:
            self.WordSet = []
            for item in params.get("WordSet"):
                obj = AiSampleWord()
                obj._deserialize(item)
                self.WordSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWorkflowsRequest(AbstractModel):
    """DescribeWorkflows請求參數結構體

    """

    def __init__(self):
        """
        :param WorkflowIds: 工作流 ID 過濾條件，數組長度限制：100。
        :type WorkflowIds: list of int
        :param Status: 工作流狀态，取值範圍：
<li>Enabled：已啓用，</li>
<li>Disabled：已禁用。</li>
不填此參數，則不區分工作流狀态。
        :type Status: str
        :param Offset: 分頁偏移量，預設值：0。
        :type Offset: int
        :param Limit: 返回記錄條數，預設值：10，最大值：100。
        :type Limit: int
        """
        self.WorkflowIds = None
        self.Status = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.WorkflowIds = params.get("WorkflowIds")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeWorkflowsResponse(AbstractModel):
    """DescribeWorkflows返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合過濾條件的記錄總數。
        :type TotalCount: int
        :param WorkflowInfoSet: 工作流訊息數組。
        :type WorkflowInfoSet: list of WorkflowInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.WorkflowInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("WorkflowInfoSet") is not None:
            self.WorkflowInfoSet = []
            for item in params.get("WorkflowInfoSet"):
                obj = WorkflowInfo()
                obj._deserialize(item)
                self.WorkflowInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DisableWorkflowRequest(AbstractModel):
    """DisableWorkflow請求參數結構體

    """

    def __init__(self):
        """
        :param WorkflowId: 工作流 ID。
        :type WorkflowId: int
        """
        self.WorkflowId = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")


class DisableWorkflowResponse(AbstractModel):
    """DisableWorkflow返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EditMediaFileInfo(AbstractModel):
    """編輯點播視訊文件訊息

    """

    def __init__(self):
        """
        :param InputInfo: 視訊的輸入訊息。
        :type InputInfo: :class:`taifucloudcloud.mps.v20190612.models.MediaInputInfo`
        :param StartTimeOffset: 視訊剪輯的起始時間偏移，單位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 視訊剪輯的結束時間偏移，單位：秒。
        :type EndTimeOffset: float
        """
        self.InputInfo = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        if params.get("InputInfo") is not None:
            self.InputInfo = MediaInputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")


class EditMediaRequest(AbstractModel):
    """EditMedia請求參數結構體

    """

    def __init__(self):
        """
        :param FileInfos: 輸入的視訊文件訊息。
        :type FileInfos: list of EditMediaFileInfo
        :param OutputStorage: 視訊處理輸出文件的目標儲存。
        :type OutputStorage: :class:`taifucloudcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputObjectPath: 視訊處理輸出文件的目標路徑。
        :type OutputObjectPath: str
        :param TaskNotifyConfig: 任務的事件通知訊息，不填代表不獲取事件通知。
        :type TaskNotifyConfig: :class:`taifucloudcloud.mps.v20190612.models.TaskNotifyConfig`
        :param TasksPriority: 任務優先級，數值越大優先級越高，取值範圍是-10到 10，不填代表0。
        :type TasksPriority: int
        :param SessionId: 用於去重的識别碼，如果七天内曾有過相同的識别碼的請求，則本次的請求會返回錯誤。最長 50 個字元，不帶或者帶空字串表示不做去重。
        :type SessionId: str
        :param SessionContext: 來源上下文，用於透傳用戶請求訊息，任務流狀态變更回調将返回該欄位值，最長 1000 個字元。
        :type SessionContext: str
        """
        self.FileInfos = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.TaskNotifyConfig = None
        self.TasksPriority = None
        self.SessionId = None
        self.SessionContext = None


    def _deserialize(self, params):
        if params.get("FileInfos") is not None:
            self.FileInfos = []
            for item in params.get("FileInfos"):
                obj = EditMediaFileInfo()
                obj._deserialize(item)
                self.FileInfos.append(obj)
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        self.TasksPriority = params.get("TasksPriority")
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")


class EditMediaResponse(AbstractModel):
    """EditMedia返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 編輯視訊的任務 ID，可以通過該 ID 查詢編輯任務的狀态。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class EditMediaTask(AbstractModel):
    """編輯視訊任務訊息

    """

    def __init__(self):
        """
        :param TaskId: 任務 ID。
        :type TaskId: str
        :param Status: 任務狀态，取值：
<li>PROCESSING：處理中；</li>
<li>FINISH：已完成。</li>
        :type Status: str
        :param ErrCode: 錯誤碼
<li>0：成功；</li>
<li>其他值：失敗。</li>
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 視訊編輯任務的輸入。
        :type Input: :class:`taifucloudcloud.mps.v20190612.models.EditMediaTaskInput`
        :param Output: 視訊編輯任務的輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.mps.v20190612.models.EditMediaTaskOutput`
        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = EditMediaTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = EditMediaTaskOutput()
            self.Output._deserialize(params.get("Output"))


class EditMediaTaskInput(AbstractModel):
    """編輯視訊任務的輸入。

    """

    def __init__(self):
        """
        :param FileInfoSet: 輸入的視訊文件訊息。
        :type FileInfoSet: list of EditMediaFileInfo
        """
        self.FileInfoSet = None


    def _deserialize(self, params):
        if params.get("FileInfoSet") is not None:
            self.FileInfoSet = []
            for item in params.get("FileInfoSet"):
                obj = EditMediaFileInfo()
                obj._deserialize(item)
                self.FileInfoSet.append(obj)


class EditMediaTaskOutput(AbstractModel):
    """編輯視訊任務的輸出

    """

    def __init__(self):
        """
        :param OutputStorage: 編輯後文件的目標儲存。
        :type OutputStorage: :class:`taifucloudcloud.mps.v20190612.models.TaskOutputStorage`
        :param Path: 編輯後的視訊文件路徑。
        :type Path: str
        """
        self.OutputStorage = None
        self.Path = None


    def _deserialize(self, params):
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.Path = params.get("Path")


class EnableWorkflowRequest(AbstractModel):
    """EnableWorkflow請求參數結構體

    """

    def __init__(self):
        """
        :param WorkflowId: 工作流 ID。
        :type WorkflowId: int
        """
        self.WorkflowId = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")


class EnableWorkflowResponse(AbstractModel):
    """EnableWorkflow返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class FaceConfigureInfo(AbstractModel):
    """人臉識别任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 人臉識别任務開關，可選值：
<li>ON：開啓智慧人臉識别任務；</li>
<li>OFF：關閉智慧人臉識别任務。</li>
        :type Switch: str
        :param Score: 人臉識别過濾分數，當識别結果達到該分數以上，返回識别結果。預設 95 分。取值範圍：0 - 100。
        :type Score: float
        :param DefaultLibraryLabelSet: 預設人物過濾標簽，指定需要返回的預設人物的標簽。如果未填或者爲空，則全部預設人物結果都返回。標簽可選值：
<li>entertainment：娛樂明星；</li>
<li>sport：體育明星；</li>
<li>politician：政治人物。</li>
        :type DefaultLibraryLabelSet: list of str
        :param UserDefineLibraryLabelSet: 用戶自定義人物過濾標簽，指定需要返回的用戶自定義人物的標簽。如果未填或者爲空，則全部自定義人物結果都返回。
標簽個數最多 10 個，每個標簽長度最多 16 個字元。
        :type UserDefineLibraryLabelSet: list of str
        :param FaceLibrary: 人物庫選擇，可選值：
<li>Default：使用預設人物庫；</li>
<li>UserDefine：使用用戶自定義人物庫。</li>
<li>All：同時使用預設人物庫和用戶自定義人物庫。</li>
預設值：All，使用系統預設人物庫及用戶自定義人物庫。
        :type FaceLibrary: str
        """
        self.Switch = None
        self.Score = None
        self.DefaultLibraryLabelSet = None
        self.UserDefineLibraryLabelSet = None
        self.FaceLibrary = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Score = params.get("Score")
        self.DefaultLibraryLabelSet = params.get("DefaultLibraryLabelSet")
        self.UserDefineLibraryLabelSet = params.get("UserDefineLibraryLabelSet")
        self.FaceLibrary = params.get("FaceLibrary")


class FaceConfigureInfoForUpdate(AbstractModel):
    """人臉識别任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 人臉識别任務開關，可選值：
<li>ON：開啓智慧人臉識别任務；</li>
<li>OFF：關閉智慧人臉識别任務。</li>
        :type Switch: str
        :param Score: 人臉識别過濾分數，當識别結果達到該分數以上，返回識别結果。取值範圍：0-100。
        :type Score: float
        :param DefaultLibraryLabelSet: 預設人物過濾標簽，指定需要返回的預設人物的標簽。如果未填或者爲空，則全部預設人物結果都返回。標簽可選值：
<li>entertainment：娛樂明星；</li>
<li>sport：體育明星；</li>
<li>politician：政治人物。</li>
        :type DefaultLibraryLabelSet: list of str
        :param UserDefineLibraryLabelSet: 用戶自定義人物過濾標簽，指定需要返回的用戶自定義人物的標簽。如果未填或者爲空，則全部自定義人物結果都返回。
標簽個數最多 10 個，每個標簽長度最多 16 個字元。
        :type UserDefineLibraryLabelSet: list of str
        :param FaceLibrary: 人物庫選擇，可選值：
<li>Default：使用預設人物庫；</li>
<li>UserDefine：使用用戶自定義人物庫。</li>
<li>All：同時使用預設人物庫和用戶自定義人物庫。</li>
        :type FaceLibrary: str
        """
        self.Switch = None
        self.Score = None
        self.DefaultLibraryLabelSet = None
        self.UserDefineLibraryLabelSet = None
        self.FaceLibrary = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Score = params.get("Score")
        self.DefaultLibraryLabelSet = params.get("DefaultLibraryLabelSet")
        self.UserDefineLibraryLabelSet = params.get("UserDefineLibraryLabelSet")
        self.FaceLibrary = params.get("FaceLibrary")


class FrameTagConfigureInfo(AbstractModel):
    """智慧按幀標簽任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 智慧按幀標簽任務開關，可選值：
<li>ON：開啓智慧按幀標簽任務；</li>
<li>OFF：關閉智慧按幀標簽任務。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class FrameTagConfigureInfoForUpdate(AbstractModel):
    """智慧按幀標簽任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 智慧按幀標簽任務開關，可選值：
<li>ON：開啓智慧按幀標簽任務；</li>
<li>OFF：關閉智慧按幀標簽任務。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class ImageSpriteTaskInput(AbstractModel):
    """對視訊截雪碧圖任務輸入參數類型

    """

    def __init__(self):
        """
        :param Definition: 雪碧圖範本 ID。
        :type Definition: int
        :param OutputStorage: 截取雪碧圖後文件的目標儲存，不填則繼承上層的 OutputStorage 值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OutputStorage: :class:`taifucloudcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputObjectPath: 截取雪碧圖後，雪碧圖圖片文件的輸出路徑，可以爲相對路徑或者絕對路徑。如果不填，則預設爲相對路徑：`{inputName}_imageSprite_{definition}_{number}.{format}`。
        :type OutputObjectPath: str
        :param WebVttObjectName: 截取雪碧圖後，Web VTT 文件的輸出路徑，只能爲相對路徑。如果不填，則預設爲相對路徑：`{inputName}_imageSprite_{definition}.{format}`。
        :type WebVttObjectName: str
        :param ObjectNumberFormat: 截取雪碧圖後輸出路徑中的`{number}`變量的規則。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ObjectNumberFormat: :class:`taifucloudcloud.mps.v20190612.models.NumberFormat`
        """
        self.Definition = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.WebVttObjectName = None
        self.ObjectNumberFormat = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        self.WebVttObjectName = params.get("WebVttObjectName")
        if params.get("ObjectNumberFormat") is not None:
            self.ObjectNumberFormat = NumberFormat()
            self.ObjectNumberFormat._deserialize(params.get("ObjectNumberFormat"))


class ImageSpriteTemplate(AbstractModel):
    """雪碧圖範本詳情

    """

    def __init__(self):
        """
        :param Definition: 雪碧圖範本唯一標識。
        :type Definition: int
        :param Type: 範本類型，取值範圍：
<li>Preset：系統預置範本；</li>
<li>Custom：用戶自定義範本。</li>
        :type Type: str
        :param Name: 雪碧圖範本名稱。
        :type Name: str
        :param Width: 雪碧圖中小圖的寬度（或長邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
        :type Width: int
        :param Height: 雪碧圖中小圖的高度（或短邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适應，可選值：
<li>open：開啓，此時，Width 代表視訊的長邊，Height 表示視訊的短邊；</li>
<li>close：關閉，此時，Width 代表視訊的寬度，Height 表示視訊的高度。</li>
預設值：open。
        :type ResolutionAdaptive: str
        :param SampleType: 采樣類型。
        :type SampleType: str
        :param SampleInterval: 采樣間隔。
        :type SampleInterval: int
        :param RowCount: 雪碧圖中小圖的行數。
        :type RowCount: int
        :param ColumnCount: 雪碧圖中小圖的列數。
        :type ColumnCount: int
        :param CreateTime: 範本創建時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param UpdateTime: 範本最後修改時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type UpdateTime: str
        :param FillType: 填充方式，當視訊流配置寬高參數與原始視訊的寬高比不一緻時，對轉碼的處理方式，即爲“填充”。可選填充方式：
<li> stretch：拉伸，對每一幀進行拉伸，填滿整個畫面，可能導緻轉碼後的視訊被“壓扁“或者“拉長“；</li>
<li>black：留黑，保持視訊寬高比不變，邊緣剩餘部分使用黑色填充。</li>
預設值：black 。
        :type FillType: str
        :param Comment: 範本描述訊息。
        :type Comment: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.SampleType = None
        self.SampleInterval = None
        self.RowCount = None
        self.ColumnCount = None
        self.CreateTime = None
        self.UpdateTime = None
        self.FillType = None
        self.Comment = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.RowCount = params.get("RowCount")
        self.ColumnCount = params.get("ColumnCount")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.FillType = params.get("FillType")
        self.Comment = params.get("Comment")


class ImageWatermarkInput(AbstractModel):
    """圖片浮水印範本輸入參數

    """

    def __init__(self):
        """
        :param ImageContent: 浮水印圖片 [Base64](https://tools.ietf.org/html/rfc4648) 編碼後的字串。支援 jpeg、png 圖片格式。
        :type ImageContent: str
        :param Width: 浮水印的寬度。支援 %、px 兩種格式：
<li>當字串以 % 結尾，表示浮水印 Width 爲視訊寬度的百分比大小，如 10% 表示 Width 爲視訊寬度的 10%；</li>
<li>當字串以 px 結尾，表示浮水印 Width 單位爲像素，如 100px 表示 Width 爲 100 像素。</li>
預設值：10%。
        :type Width: str
        :param Height: 浮水印的高度。支援 %、px 兩種格式：
<li>當字串以 % 結尾，表示浮水印 Height 爲視訊高度的百分比大小，如 10% 表示 Height 爲視訊高度的 10%；</li>
<li>當字串以 px 結尾，表示浮水印 Height 單位爲像素，如 100px 表示 Height 爲 100 像素。</li>
預設值：0px，表示 Height 按照原始浮水印圖片的寬高比縮放。
        :type Height: str
        """
        self.ImageContent = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.ImageContent = params.get("ImageContent")
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class ImageWatermarkInputForUpdate(AbstractModel):
    """圖片浮水印範本輸入參數

    """

    def __init__(self):
        """
        :param ImageContent: 浮水印圖片 [Base64](https://tools.ietf.org/html/rfc4648) 編碼後的字串。支援 jpeg、png 圖片格式。
        :type ImageContent: str
        :param Width: 浮水印的寬度。支援 %、px 兩種格式：
<li>當字串以 % 結尾，表示浮水印 Width 爲視訊寬度的百分比大小，如 10% 表示 Width 爲視訊寬度的 10%；</li>
<li>當字串以 px 結尾，表示浮水印 Width 單位爲像素，如 100px 表示 Width 爲 100 像素。</li>
        :type Width: str
        :param Height: 浮水印的高度。支援 %、px 兩種格式：
<li>當字串以 % 結尾，表示浮水印 Height 爲視訊高度的百分比大小，如 10% 表示 Height 爲視訊高度的 10%；</li>
<li>當字串以 px 結尾，表示浮水印 Width 單位爲像素，如 100px 表示 Width 爲 100 像素。</li>
0px 表示 Height 按照 Width 對視訊寬度的比例縮放。
        :type Height: str
        """
        self.ImageContent = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.ImageContent = params.get("ImageContent")
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class ImageWatermarkTemplate(AbstractModel):
    """圖片浮水印範本

    """

    def __init__(self):
        """
        :param ImageUrl: 浮水印圖片網址。
        :type ImageUrl: str
        :param Width: 浮水印的寬度。支援 %、px 兩種格式：
<li>當字串以 % 結尾，表示浮水印 Width 爲視訊寬度的百分比大小，如 10% 表示 Width 爲視訊寬度的 10%；</li>
<li>當字串以 px 結尾，表示浮水印 Width 單位爲像素，如 100px 表示 Width 爲 100 像素。</li>
        :type Width: str
        :param Height: 浮水印的高度。支援 %、px 兩種格式：
<li>當字串以 % 結尾，表示浮水印 Height 爲視訊高度的百分比大小，如 10% 表示 Height 爲視訊高度的 10%；</li>
<li>當字串以 px 結尾，表示浮水印 Width 單位爲像素，如 100px 表示 Width 爲 100 像素；</li>
0px：表示 Height 按照 Width 對視訊寬度的比例縮放。
        :type Height: str
        """
        self.ImageUrl = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class LiveStreamAiRecognitionResultInfo(AbstractModel):
    """直播流 AI 識别結果

    """

    def __init__(self):
        """
        :param ResultSet: 内容識别結果清單。
        :type ResultSet: list of LiveStreamAiRecognitionResultItem
        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = LiveStreamAiRecognitionResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)


class LiveStreamAiRecognitionResultItem(AbstractModel):
    """直播流 AI 識别結果

    """

    def __init__(self):
        """
        :param Type: 結果的類型，取值範圍：
<li>FaceRecognition：人臉識别，</li>
<li>AsrWordsRecognition：語音關鍵詞識别，</li>
<li>OcrWordsRecognition：文本關鍵詞識别，</li>
<li>AsrFullTextRecognition：語音全文識别，</li>
<li>OcrFullTextRecognition：文本全文識别。</li>
        :type Type: str
        :param FaceRecognitionResultSet: 人臉識别結果，當 Type 爲
FaceRecognition 時有效。
        :type FaceRecognitionResultSet: list of LiveStreamFaceRecognitionResult
        :param AsrWordsRecognitionResultSet: 語音關鍵詞識别結果，當 Type 爲
AsrWordsRecognition 時有效。
        :type AsrWordsRecognitionResultSet: list of LiveStreamAsrWordsRecognitionResult
        :param OcrWordsRecognitionResultSet: 文本關鍵詞識别結果，當 Type 爲
OcrWordsRecognition 時有效。
        :type OcrWordsRecognitionResultSet: list of LiveStreamOcrWordsRecognitionResult
        :param AsrFullTextRecognitionResultSet: 語音全文識别結果，當 Type 爲
AsrFullTextRecognition 時有效。
        :type AsrFullTextRecognitionResultSet: list of LiveStreamAsrFullTextRecognitionResult
        :param OcrFullTextRecognitionResultSet: 文本全文識别結果，當 Type 爲
OcrFullTextRecognition 時有效。
        :type OcrFullTextRecognitionResultSet: list of LiveStreamOcrFullTextRecognitionResult
        """
        self.Type = None
        self.FaceRecognitionResultSet = None
        self.AsrWordsRecognitionResultSet = None
        self.OcrWordsRecognitionResultSet = None
        self.AsrFullTextRecognitionResultSet = None
        self.OcrFullTextRecognitionResultSet = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("FaceRecognitionResultSet") is not None:
            self.FaceRecognitionResultSet = []
            for item in params.get("FaceRecognitionResultSet"):
                obj = LiveStreamFaceRecognitionResult()
                obj._deserialize(item)
                self.FaceRecognitionResultSet.append(obj)
        if params.get("AsrWordsRecognitionResultSet") is not None:
            self.AsrWordsRecognitionResultSet = []
            for item in params.get("AsrWordsRecognitionResultSet"):
                obj = LiveStreamAsrWordsRecognitionResult()
                obj._deserialize(item)
                self.AsrWordsRecognitionResultSet.append(obj)
        if params.get("OcrWordsRecognitionResultSet") is not None:
            self.OcrWordsRecognitionResultSet = []
            for item in params.get("OcrWordsRecognitionResultSet"):
                obj = LiveStreamOcrWordsRecognitionResult()
                obj._deserialize(item)
                self.OcrWordsRecognitionResultSet.append(obj)
        if params.get("AsrFullTextRecognitionResultSet") is not None:
            self.AsrFullTextRecognitionResultSet = []
            for item in params.get("AsrFullTextRecognitionResultSet"):
                obj = LiveStreamAsrFullTextRecognitionResult()
                obj._deserialize(item)
                self.AsrFullTextRecognitionResultSet.append(obj)
        if params.get("OcrFullTextRecognitionResultSet") is not None:
            self.OcrFullTextRecognitionResultSet = []
            for item in params.get("OcrFullTextRecognitionResultSet"):
                obj = LiveStreamOcrFullTextRecognitionResult()
                obj._deserialize(item)
                self.OcrFullTextRecognitionResultSet.append(obj)


class LiveStreamAiReviewImagePoliticalResult(AbstractModel):
    """直播 AI 内容審核圖片鑒政結果

    """

    def __init__(self):
        """
        :param StartPtsTime: 嫌疑片段起始的 PTS 時間，單位：秒。
        :type StartPtsTime: float
        :param EndPtsTime: 嫌疑片段結束的 PTS 時間，單位：秒。
        :type EndPtsTime: float
        :param Confidence: 嫌疑片段涉政分數。
        :type Confidence: float
        :param Suggestion: 嫌疑片段 結果建議，取值範圍：
<li>pass</li>
<li>review</li>
<li>block</li>
        :type Suggestion: str
        :param Label: 視訊鑒政結果標簽，取值範圍：
<li>politician：政治人物。</li>
<li>violation_photo：違規圖標。</li>
        :type Label: str
        :param Name: 涉政人物、違規圖標名字。
        :type Name: str
        :param AreaCoordSet: 涉政人物、違規圖標出現的區域坐標 (像素級)，[x1, y1, x2, y2]，即左上角坐標、右下角坐標。
        :type AreaCoordSet: list of int
        :param Url: 嫌疑圖片 URL （圖片不會永久儲存，到達
PicUrlExpireTime 時間點後圖片将被删除）。
        :type Url: str
        :param PicUrlExpireTime: 嫌疑圖片 URL 失效時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type PicUrlExpireTime: str
        """
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.Name = None
        self.AreaCoordSet = None
        self.Url = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.Name = params.get("Name")
        self.AreaCoordSet = params.get("AreaCoordSet")
        self.Url = params.get("Url")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")


class LiveStreamAiReviewImagePornResult(AbstractModel):
    """直播 AI 内容審核圖片 結果

    """

    def __init__(self):
        """
        :param StartPtsTime: 嫌疑片段起始的 PTS 時間，單位：秒。
        :type StartPtsTime: float
        :param EndPtsTime: 嫌疑片段結束的 PTS 時間，單位：秒。
        :type EndPtsTime: float
        :param Confidence: 嫌疑片段涉黃分數。
        :type Confidence: float
        :param Suggestion: 嫌疑片段 結果建議，取值範圍：
<li>pass</li>
<li>review</li>
<li>block</li>
        :type Suggestion: str
        :param Label: 視訊 結果標簽，取值範圍：
<li>porn：色情。</li>
<li>sexy：性感。</li>
<li>vulgar：低俗。</li>
<li>intimacy：親密行爲。</li>
        :type Label: str
        :param Url: 嫌疑圖片 URL （圖片不會永久儲存，到達
PicUrlExpireTime 時間點後圖片将被删除）。
        :type Url: str
        :param PicUrlExpireTime: 嫌疑圖片 URL 失效時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type PicUrlExpireTime: str
        """
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.Url = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.Url = params.get("Url")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")


class LiveStreamAiReviewImageTerrorismResult(AbstractModel):
    """直播 AI 内容審核圖片鑒恐結果

    """

    def __init__(self):
        """
        :param StartPtsTime: 嫌疑片段起始的 PTS 時間，單位：秒。
        :type StartPtsTime: float
        :param EndPtsTime: 嫌疑片段結束的 PTS 時間，單位：秒。
        :type EndPtsTime: float
        :param Confidence: 嫌疑片段涉恐分數。
        :type Confidence: float
        :param Suggestion: 嫌疑片段鑒恐結果建議，取值範圍：
<li>pass</li>
<li>review</li>
<li>block</li>
        :type Suggestion: str
        :param Label: 視訊暴恐結果標簽，取值範圍：
<li>guns：武器槍支。</li>
<li>crowd：人群聚集。</li>
<li>police：警察部隊。</li>
<li>bloody：血腥畫面。</li>
<li>banners：暴恐旗幟。</li>
<li>militant：武裝分子。</li>
<li>explosion：爆炸火災。</li>
<li>terrorists：暴恐人物。</li>
        :type Label: str
        :param Url: 嫌疑圖片 URL （圖片不會永久儲存，到達
PicUrlExpireTime 時間點後圖片将被删除）。
        :type Url: str
        :param PicUrlExpireTime: 嫌疑圖片 URL 失效時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type PicUrlExpireTime: str
        """
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.Url = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.Url = params.get("Url")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")


class LiveStreamAiReviewResultInfo(AbstractModel):
    """直播流 AI 審核結果

    """

    def __init__(self):
        """
        :param ResultSet: 内容審核結果清單。
        :type ResultSet: list of LiveStreamAiReviewResultItem
        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = LiveStreamAiReviewResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)


class LiveStreamAiReviewResultItem(AbstractModel):
    """直播流 AI 審核結果

    """

    def __init__(self):
        """
        :param Type: 審核結果的類型，可以取的值有：
<li>ImagePorn：圖片 </li>
<li>ImageTerrorism：圖片鑒恐</li>
<li>ImagePolitical：圖片鑒政</li>
<li>PornVoice：聲音 </li>
        :type Type: str
        :param ImagePornResultSet: 圖片 的結果，當 Type 爲 ImagePorn 時有效。
        :type ImagePornResultSet: list of LiveStreamAiReviewImagePornResult
        :param ImageTerrorismResultSet: 圖片鑒恐的結果，當 Type 爲 ImageTerrorism 時有效。
        :type ImageTerrorismResultSet: list of LiveStreamAiReviewImageTerrorismResult
        :param ImagePoliticalResultSet: 圖片鑒政的結果，當 Type 爲 ImagePolitical 時有效。
        :type ImagePoliticalResultSet: list of LiveStreamAiReviewImagePoliticalResult
        :param VoicePornResultSet: 聲音 的結果，當 Type 爲 PornVoice 時有效。
        :type VoicePornResultSet: list of LiveStreamAiReviewVoicePornResult
        """
        self.Type = None
        self.ImagePornResultSet = None
        self.ImageTerrorismResultSet = None
        self.ImagePoliticalResultSet = None
        self.VoicePornResultSet = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("ImagePornResultSet") is not None:
            self.ImagePornResultSet = []
            for item in params.get("ImagePornResultSet"):
                obj = LiveStreamAiReviewImagePornResult()
                obj._deserialize(item)
                self.ImagePornResultSet.append(obj)
        if params.get("ImageTerrorismResultSet") is not None:
            self.ImageTerrorismResultSet = []
            for item in params.get("ImageTerrorismResultSet"):
                obj = LiveStreamAiReviewImageTerrorismResult()
                obj._deserialize(item)
                self.ImageTerrorismResultSet.append(obj)
        if params.get("ImagePoliticalResultSet") is not None:
            self.ImagePoliticalResultSet = []
            for item in params.get("ImagePoliticalResultSet"):
                obj = LiveStreamAiReviewImagePoliticalResult()
                obj._deserialize(item)
                self.ImagePoliticalResultSet.append(obj)
        if params.get("VoicePornResultSet") is not None:
            self.VoicePornResultSet = []
            for item in params.get("VoicePornResultSet"):
                obj = LiveStreamAiReviewVoicePornResult()
                obj._deserialize(item)
                self.VoicePornResultSet.append(obj)


class LiveStreamAiReviewVoicePornResult(AbstractModel):
    """直播 AI 内容審核聲音 結果

    """

    def __init__(self):
        """
        :param StartPtsTime: 嫌疑片段起始的 PTS 時間，單位：秒。
        :type StartPtsTime: float
        :param EndPtsTime: 嫌疑片段結束的 PTS 時間，單位：秒。
        :type EndPtsTime: float
        :param Confidence: 嫌疑片段涉黃分數。
        :type Confidence: float
        :param Suggestion: 嫌疑片段 結果建議，取值範圍：
<li>pass</li>
<li>review</li>
<li>block</li>
        :type Suggestion: str
        :param Label: 視訊 結果標簽，取值範圍：
<li>sexual_moan：呻吟。</li>
        :type Label: str
        """
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.Suggestion = None
        self.Label = None


    def _deserialize(self, params):
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")


class LiveStreamAsrFullTextRecognitionResult(AbstractModel):
    """直播識别 Asr 全文識别

    """

    def __init__(self):
        """
        :param Text: 識别文本。
        :type Text: str
        :param StartPtsTime: 識别片段起始的 PTS 時間，單位：秒。
        :type StartPtsTime: float
        :param EndPtsTime: 識别片段終止的 PTS 時間，單位：秒。
        :type EndPtsTime: float
        :param Confidence: 識别片段置信度。取值：0~100。
        :type Confidence: float
        """
        self.Text = None
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")


class LiveStreamAsrWordsRecognitionResult(AbstractModel):
    """直播 AI Asr 單詞識别結果

    """

    def __init__(self):
        """
        :param Word: 語音關鍵詞。
        :type Word: str
        :param StartPtsTime: 識别片段起始的 PTS 時間，單位：秒。
        :type StartPtsTime: float
        :param EndPtsTime: 識别片段終止的 PTS 時間，單位：秒。
        :type EndPtsTime: float
        :param Confidence: 識别片段置信度。取值：0~100。
        :type Confidence: float
        """
        self.Word = None
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")


class LiveStreamFaceRecognitionResult(AbstractModel):
    """直播 AI 人臉識别結果

    """

    def __init__(self):
        """
        :param Id: 人物唯一標識 ID。
        :type Id: str
        :param Name: 人物名稱。
        :type Name: str
        :param Type: 人物庫類型，表示識别出的人物來自哪個人物庫：
<li>Default：預設人物庫；</li><li>UserDefine：用戶自定義人物庫。</li>
        :type Type: str
        :param StartPtsTime: 識别片段起始的 PTS 時間，單位：秒。
        :type StartPtsTime: float
        :param EndPtsTime: 識别片段終止的 PTS 時間，單位：秒。
        :type EndPtsTime: float
        :param Confidence: 識别片段置信度。取值：0~100。
        :type Confidence: float
        :param AreaCoordSet: 識别結果的區域坐標。數組包含 4 個元素 [x1,y1,x2,y2]，依次表示區域左上點、右下點的橫縱坐標。
        :type AreaCoordSet: list of int
        """
        self.Id = None
        self.Name = None
        self.Type = None
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.AreaCoordSet = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")


class LiveStreamOcrFullTextRecognitionResult(AbstractModel):
    """直播識别 Ocr 全文識别

    """

    def __init__(self):
        """
        :param Text: 語音文本。
        :type Text: str
        :param StartPtsTime: 識别片段起始的 PTS 時間，單位：秒。
        :type StartPtsTime: float
        :param EndPtsTime: 識别片段終止的 PTS 時間，單位：秒。
        :type EndPtsTime: float
        :param Confidence: 識别片段置信度。取值：0~100。
        :type Confidence: float
        :param AreaCoordSet: 識别結果的區域坐標。數組包含 4 個元素 [x1,y1,x2,y2]，依次表示區域左上點、右下點的橫縱坐標。
        :type AreaCoordSet: list of int
        """
        self.Text = None
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.AreaCoordSet = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")


class LiveStreamOcrWordsRecognitionResult(AbstractModel):
    """直播 AI Ocr 單詞識别結果

    """

    def __init__(self):
        """
        :param Word: 文本關鍵詞。
        :type Word: str
        :param StartPtsTime: 識别片段起始的 PTS 時間，單位：秒。
        :type StartPtsTime: float
        :param EndPtsTime: 識别片段終止的 PTS 時間，單位：秒。
        :type EndPtsTime: float
        :param Confidence: 識别片段置信度。取值：0~100。
        :type Confidence: float
        :param AreaCoords: 識别結果的區域坐標。數組包含 4 個元素 [x1,y1,x2,y2]，依次表示區域左上點、右下點的橫縱坐標。
        :type AreaCoords: list of int
        """
        self.Word = None
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.AreaCoords = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.AreaCoords = params.get("AreaCoords")


class LiveStreamProcessErrorInfo(AbstractModel):
    """直播流處理錯誤訊息

    """

    def __init__(self):
        """
        :param ErrCode: 錯誤碼：
<li>0表示沒有錯誤；</li>
<li>非0表示錯誤，請參考 Message 錯誤訊息。</li>
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        """
        self.ErrCode = None
        self.Message = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")


class LiveStreamProcessTask(AbstractModel):
    """直播處理任務訊息

    """

    def __init__(self):
        """
        :param TaskId: 視訊處理任務 ID。
        :type TaskId: str
        :param Status: 任務流狀态，取值：
<li>PROCESSING：處理中；</li>
<li>FINISH：已完成。</li>
        :type Status: str
        :param ErrCode: 錯誤碼，0 表示成功，其他值表示失敗。
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Url: 直播流 URL。
        :type Url: str
        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Url = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.Url = params.get("Url")


class LiveStreamTaskNotifyConfig(AbstractModel):
    """任務處理的事件通知配置。

    """

    def __init__(self):
        """
        :param CmqModel: CMQ 的模型，有 Queue 和 Topic 兩種，目前僅支援 Queue。
        :type CmqModel: str
        :param CmqRegion: CMQ 的園區，如 sh，bj 等。
        :type CmqRegion: str
        :param QueueName: 當模型爲 Queue 時有效，表示接收事件通知的 CMQ 的隊列名。
        :type QueueName: str
        :param TopicName: 當模型爲 Topic 時有效，表示接收事件通知的 CMQ 的主題名。
        :type TopicName: str
        """
        self.CmqModel = None
        self.CmqRegion = None
        self.QueueName = None
        self.TopicName = None


    def _deserialize(self, params):
        self.CmqModel = params.get("CmqModel")
        self.CmqRegion = params.get("CmqRegion")
        self.QueueName = params.get("QueueName")
        self.TopicName = params.get("TopicName")


class ManageTaskRequest(AbstractModel):
    """ManageTask請求參數結構體

    """

    def __init__(self):
        """
        :param OperationType: 操作類型，取值範圍：
<li>Abort：終止任務。</li>
        :type OperationType: str
        :param TaskId: 視訊處理的任務 ID。
        :type TaskId: str
        """
        self.OperationType = None
        self.TaskId = None


    def _deserialize(self, params):
        self.OperationType = params.get("OperationType")
        self.TaskId = params.get("TaskId")


class ManageTaskResponse(AbstractModel):
    """ManageTask返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MediaAiAnalysisClassificationItem(AbstractModel):
    """智慧分類結果

    """

    def __init__(self):
        """
        :param Classification: 智慧分類的類别名稱。
        :type Classification: str
        :param Confidence: 智慧分類的可信度，取值範圍是 0 到 100。
        :type Confidence: float
        """
        self.Classification = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Classification = params.get("Classification")
        self.Confidence = params.get("Confidence")


class MediaAiAnalysisCoverItem(AbstractModel):
    """智慧封面訊息

    """

    def __init__(self):
        """
        :param CoverPath: 智慧封面儲存路徑。
        :type CoverPath: str
        :param Confidence: 智慧封面的可信度，取值範圍是 0 到 100。
        :type Confidence: float
        """
        self.CoverPath = None
        self.Confidence = None


    def _deserialize(self, params):
        self.CoverPath = params.get("CoverPath")
        self.Confidence = params.get("Confidence")


class MediaAiAnalysisFrameTagItem(AbstractModel):
    """智慧按幀標簽結果訊息

    """

    def __init__(self):
        """
        :param Tag: 按幀標簽名稱。
        :type Tag: str
        :param Confidence: 按幀標簽的可信度，取值範圍是 0 到 100。
        :type Confidence: float
        """
        self.Tag = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Tag = params.get("Tag")
        self.Confidence = params.get("Confidence")


class MediaAiAnalysisFrameTagSegmentItem(AbstractModel):
    """按幀標簽片段清單

    """

    def __init__(self):
        """
        :param StartTimeOffset: 按幀標簽起始的偏移時間。
        :type StartTimeOffset: float
        :param EndTimeOffset: 按幀標簽結束的偏移時間。
        :type EndTimeOffset: float
        :param TagSet: 時間片段内的標簽清單。
        :type TagSet: list of MediaAiAnalysisFrameTagItem
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.TagSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = MediaAiAnalysisFrameTagItem()
                obj._deserialize(item)
                self.TagSet.append(obj)


class MediaAiAnalysisTagItem(AbstractModel):
    """智慧標簽結果訊息

    """

    def __init__(self):
        """
        :param Tag: 標簽名稱。
        :type Tag: str
        :param Confidence: 標簽的可信度，取值範圍是 0 到 100。
        :type Confidence: float
        """
        self.Tag = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Tag = params.get("Tag")
        self.Confidence = params.get("Confidence")


class MediaAnimatedGraphicsItem(AbstractModel):
    """視訊轉動圖結果訊息

    """

    def __init__(self):
        """
        :param Storage: 轉動圖文件的儲存位置。
        :type Storage: :class:`taifucloudcloud.mps.v20190612.models.TaskOutputStorage`
        :param Path: 轉動圖的文件路徑。
        :type Path: str
        :param Definition: 轉動圖範本 ID，參見[轉動圖參數範本](https://cloud.taifucloud.com/document/product/862/37042#.E9.A2.84.E7.BD.AE.E8.BD.AC.E5.8A.A8.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
        :type Definition: int
        :param Container: 動圖格式，如 gif。
        :type Container: str
        :param Height: 動圖的高度，單位：px。
        :type Height: int
        :param Width: 動圖的寬度，單位：px。
        :type Width: int
        :param Bitrate: 動圖碼率，單位：bps。
        :type Bitrate: int
        :param Size: 動圖大小，單位：位元。
        :type Size: int
        :param Md5: 動圖的md5值。
        :type Md5: str
        :param StartTimeOffset: 動圖在視訊中的起始時間偏移，單位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 動圖在視訊中的結束時間偏移，單位：秒。
        :type EndTimeOffset: float
        """
        self.Storage = None
        self.Path = None
        self.Definition = None
        self.Container = None
        self.Height = None
        self.Width = None
        self.Bitrate = None
        self.Size = None
        self.Md5 = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        if params.get("Storage") is not None:
            self.Storage = TaskOutputStorage()
            self.Storage._deserialize(params.get("Storage"))
        self.Path = params.get("Path")
        self.Definition = params.get("Definition")
        self.Container = params.get("Container")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Bitrate = params.get("Bitrate")
        self.Size = params.get("Size")
        self.Md5 = params.get("Md5")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")


class MediaAudioStreamItem(AbstractModel):
    """點播文件音訊流訊息

    """

    def __init__(self):
        """
        :param Bitrate: 音訊流的碼率，單位：bps。
        :type Bitrate: int
        :param SamplingRate: 音訊流的采樣率，單位：hz。
        :type SamplingRate: int
        :param Codec: 音訊流的編碼格式，例如 aac。
        :type Codec: str
        """
        self.Bitrate = None
        self.SamplingRate = None
        self.Codec = None


    def _deserialize(self, params):
        self.Bitrate = params.get("Bitrate")
        self.SamplingRate = params.get("SamplingRate")
        self.Codec = params.get("Codec")


class MediaContentReviewAsrTextSegmentItem(AbstractModel):
    """内容審核 Asr 文字審核嫌疑片段

    """

    def __init__(self):
        """
        :param StartTimeOffset: 嫌疑片段起始的偏移時間，單位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 嫌疑片段結束的偏移時間，單位：秒。
        :type EndTimeOffset: float
        :param Confidence: 嫌疑片段置信度。
        :type Confidence: float
        :param Suggestion: 嫌疑片段審核結果建議，取值範圍：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param KeywordSet: 嫌疑關鍵詞清單。
        :type KeywordSet: list of str
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Suggestion = None
        self.KeywordSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.KeywordSet = params.get("KeywordSet")


class MediaContentReviewOcrTextSegmentItem(AbstractModel):
    """内容審核 Ocr 文字審核嫌疑片段

    """

    def __init__(self):
        """
        :param StartTimeOffset: 嫌疑片段起始的偏移時間，單位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 嫌疑片段結束的偏移時間，單位：秒。
        :type EndTimeOffset: float
        :param Confidence: 嫌疑片段置信度。
        :type Confidence: float
        :param Suggestion: 嫌疑片段審核結果建議，取值範圍：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param KeywordSet: 嫌疑關鍵詞清單。
        :type KeywordSet: list of str
        :param AreaCoordSet: 嫌疑文字出現的區域坐標 (像素級)，[x1, y1, x2, y2]，即左上角坐標、右下角坐標。
        :type AreaCoordSet: list of int
        :param Url: 嫌疑圖片 URL （圖片不會永久儲存，到達
PicUrlExpireTime 時間點後圖片将被删除）。
        :type Url: str
        :param PicUrlExpireTime: 嫌疑圖片 URL 失效時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type PicUrlExpireTime: str
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Suggestion = None
        self.KeywordSet = None
        self.AreaCoordSet = None
        self.Url = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.KeywordSet = params.get("KeywordSet")
        self.AreaCoordSet = params.get("AreaCoordSet")
        self.Url = params.get("Url")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")


class MediaContentReviewPoliticalSegmentItem(AbstractModel):
    """内容審核涉政嫌疑片段

    """

    def __init__(self):
        """
        :param StartTimeOffset: 嫌疑片段起始的偏移時間，單位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 嫌疑片段結束的偏移時間，單位：秒。
        :type EndTimeOffset: float
        :param Confidence: 嫌疑片段涉政分數。
        :type Confidence: float
        :param Suggestion: 嫌疑片段鑒政結果建議，取值範圍：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param Name: 涉政人物、違規圖標名字。
        :type Name: str
        :param Label: 嫌疑片段鑒政結果標簽。
        :type Label: str
        :param Url: 嫌疑圖片 URL （圖片不會永久儲存，到達
 PicUrlExpireTime 時間點後圖片将被删除）。
        :type Url: str
        :param AreaCoordSet: 涉政人物、違規圖標出現的區域坐標 (像素級)，[x1, y1, x2, y2]，即左上角坐標、右下角坐標。
        :type AreaCoordSet: list of int
        :param PicUrlExpireTime: 嫌疑圖片 URL 失效時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type PicUrlExpireTime: str
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Suggestion = None
        self.Name = None
        self.Label = None
        self.Url = None
        self.AreaCoordSet = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Name = params.get("Name")
        self.Label = params.get("Label")
        self.Url = params.get("Url")
        self.AreaCoordSet = params.get("AreaCoordSet")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")


class MediaContentReviewSegmentItem(AbstractModel):
    """内容審核涉黃/暴恐嫌疑片段

    """

    def __init__(self):
        """
        :param StartTimeOffset: 嫌疑片段起始的偏移時間，單位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 嫌疑片段結束的偏移時間，單位：秒。
        :type EndTimeOffset: float
        :param Confidence: 嫌疑片段涉黃分數。
        :type Confidence: float
        :param Label: 嫌疑片段 結果標簽。
        :type Label: str
        :param Suggestion: 嫌疑片段 結果建議，取值範圍：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
        :type Suggestion: str
        :param Url: 嫌疑圖片 URL （圖片不會永久儲存，到達
 PicUrlExpireTime 時間點後圖片将被删除）。
        :type Url: str
        :param PicUrlExpireTime: 嫌疑圖片 URL 失效時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type PicUrlExpireTime: str
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Label = None
        self.Suggestion = None
        self.Url = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Label = params.get("Label")
        self.Suggestion = params.get("Suggestion")
        self.Url = params.get("Url")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")


class MediaImageSpriteItem(AbstractModel):
    """雪碧圖訊息

    """

    def __init__(self):
        """
        :param Definition: 雪碧圖規格，參見[雪碧圖參數範本](https://cloud.taifucloud.com/document/product/266/33480#.E9.9B.AA.E7.A2.A7.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
        :type Definition: int
        :param Height: 雪碧圖小圖的高度。
        :type Height: int
        :param Width: 雪碧圖小圖的寬度。
        :type Width: int
        :param TotalCount: 每一張雪碧圖大圖裏小圖的數量。
        :type TotalCount: int
        :param ImagePathSet: 每一張雪碧圖大圖的路徑。
        :type ImagePathSet: list of str
        :param WebVttPath: 雪碧圖子圖位置與時間關系的 WebVtt 文件路徑。WebVtt 文件表明了各個雪碧圖小圖對應的時間點，以及在雪碧大圖裏的坐標位置，一般被播放器用於實現預覽。
        :type WebVttPath: str
        :param Storage: 雪碧圖文件的儲存位置。
        :type Storage: :class:`taifucloudcloud.mps.v20190612.models.TaskOutputStorage`
        """
        self.Definition = None
        self.Height = None
        self.Width = None
        self.TotalCount = None
        self.ImagePathSet = None
        self.WebVttPath = None
        self.Storage = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.TotalCount = params.get("TotalCount")
        self.ImagePathSet = params.get("ImagePathSet")
        self.WebVttPath = params.get("WebVttPath")
        if params.get("Storage") is not None:
            self.Storage = TaskOutputStorage()
            self.Storage._deserialize(params.get("Storage"))


class MediaInputInfo(AbstractModel):
    """視訊處理的輸入對象訊息。

    """

    def __init__(self):
        """
        :param Type: 輸入來源對象的類型，現在僅支援 COS。
        :type Type: str
        :param CosInputInfo: 當 Type 爲 COS 時有效，則該項爲必填，表示視訊處理 COS 對象訊息。
        :type CosInputInfo: :class:`taifucloudcloud.mps.v20190612.models.CosInputInfo`
        """
        self.Type = None
        self.CosInputInfo = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("CosInputInfo") is not None:
            self.CosInputInfo = CosInputInfo()
            self.CosInputInfo._deserialize(params.get("CosInputInfo"))


class MediaMetaData(AbstractModel):
    """點播媒體文件元訊息

    """

    def __init__(self):
        """
        :param Size: 上傳的媒體文件大小（視訊爲 HLS 時，大小是 m3u8 和 ts 文件大小的總和），單位：位元。
        :type Size: int
        :param Container: 容器類型，例如 m4a，mp4 等。
        :type Container: str
        :param Bitrate: 視訊流碼率平均值與音訊流碼率平均值之和，單位：bps。
        :type Bitrate: int
        :param Height: 視訊流高度的最大值，單位：px。
        :type Height: int
        :param Width: 視訊流寬度的最大值，單位：px。
        :type Width: int
        :param Duration: 視訊時長，單位：秒。
        :type Duration: float
        :param Rotate: 視訊拍攝時的選擇角度，單位：度。
        :type Rotate: int
        :param VideoStreamSet: 視訊流訊息。
        :type VideoStreamSet: list of MediaVideoStreamItem
        :param AudioStreamSet: 音訊流訊息。
        :type AudioStreamSet: list of MediaAudioStreamItem
        :param VideoDuration: 視訊時長，單位：秒。
        :type VideoDuration: float
        :param AudioDuration: 音訊時長，單位：秒。
        :type AudioDuration: float
        """
        self.Size = None
        self.Container = None
        self.Bitrate = None
        self.Height = None
        self.Width = None
        self.Duration = None
        self.Rotate = None
        self.VideoStreamSet = None
        self.AudioStreamSet = None
        self.VideoDuration = None
        self.AudioDuration = None


    def _deserialize(self, params):
        self.Size = params.get("Size")
        self.Container = params.get("Container")
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Duration = params.get("Duration")
        self.Rotate = params.get("Rotate")
        if params.get("VideoStreamSet") is not None:
            self.VideoStreamSet = []
            for item in params.get("VideoStreamSet"):
                obj = MediaVideoStreamItem()
                obj._deserialize(item)
                self.VideoStreamSet.append(obj)
        if params.get("AudioStreamSet") is not None:
            self.AudioStreamSet = []
            for item in params.get("AudioStreamSet"):
                obj = MediaAudioStreamItem()
                obj._deserialize(item)
                self.AudioStreamSet.append(obj)
        self.VideoDuration = params.get("VideoDuration")
        self.AudioDuration = params.get("AudioDuration")


class MediaProcessTaskAnimatedGraphicResult(AbstractModel):
    """轉動圖任務結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0 表示成功，其他值表示失敗：
<li>40000：輸入參數不合法，請檢查輸入參數；</li>
<li>60000：源文件錯誤（如視訊數據損壞），請确認源文件是否正常；</li>
<li>70000：内部服務錯誤，建議重試。</li>
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 轉動圖任務的輸入。
        :type Input: :class:`taifucloudcloud.mps.v20190612.models.AnimatedGraphicTaskInput`
        :param Output: 轉動圖任務的輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.mps.v20190612.models.MediaAnimatedGraphicsItem`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AnimatedGraphicTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaAnimatedGraphicsItem()
            self.Output._deserialize(params.get("Output"))


class MediaProcessTaskImageSpriteResult(AbstractModel):
    """對視訊截雪碧圖任務結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0 表示成功，其他值表示失敗：
<li>40000：輸入參數不合法，請檢查輸入參數；</li>
<li>60000：源文件錯誤（如視訊數據損壞），請确認源文件是否正常；</li>
<li>70000：内部服務錯誤，建議重試。</li>
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 對視訊截雪碧圖任務的輸入。
        :type Input: :class:`taifucloudcloud.mps.v20190612.models.ImageSpriteTaskInput`
        :param Output: 對視訊截雪碧圖任務的輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.mps.v20190612.models.MediaImageSpriteItem`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = ImageSpriteTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaImageSpriteItem()
            self.Output._deserialize(params.get("Output"))


class MediaProcessTaskInput(AbstractModel):
    """視訊處理任務類型

    """

    def __init__(self):
        """
        :param TranscodeTaskSet: 視訊轉碼任務清單。
        :type TranscodeTaskSet: list of TranscodeTaskInput
        :param AnimatedGraphicTaskSet: 視訊轉動圖任務清單。
        :type AnimatedGraphicTaskSet: list of AnimatedGraphicTaskInput
        :param SnapshotByTimeOffsetTaskSet: 對視訊按時間點截圖任務清單。
        :type SnapshotByTimeOffsetTaskSet: list of SnapshotByTimeOffsetTaskInput
        :param SampleSnapshotTaskSet: 對視訊采樣截圖任務清單。
        :type SampleSnapshotTaskSet: list of SampleSnapshotTaskInput
        :param ImageSpriteTaskSet: 對視訊截雪碧圖任務清單。
        :type ImageSpriteTaskSet: list of ImageSpriteTaskInput
        """
        self.TranscodeTaskSet = None
        self.AnimatedGraphicTaskSet = None
        self.SnapshotByTimeOffsetTaskSet = None
        self.SampleSnapshotTaskSet = None
        self.ImageSpriteTaskSet = None


    def _deserialize(self, params):
        if params.get("TranscodeTaskSet") is not None:
            self.TranscodeTaskSet = []
            for item in params.get("TranscodeTaskSet"):
                obj = TranscodeTaskInput()
                obj._deserialize(item)
                self.TranscodeTaskSet.append(obj)
        if params.get("AnimatedGraphicTaskSet") is not None:
            self.AnimatedGraphicTaskSet = []
            for item in params.get("AnimatedGraphicTaskSet"):
                obj = AnimatedGraphicTaskInput()
                obj._deserialize(item)
                self.AnimatedGraphicTaskSet.append(obj)
        if params.get("SnapshotByTimeOffsetTaskSet") is not None:
            self.SnapshotByTimeOffsetTaskSet = []
            for item in params.get("SnapshotByTimeOffsetTaskSet"):
                obj = SnapshotByTimeOffsetTaskInput()
                obj._deserialize(item)
                self.SnapshotByTimeOffsetTaskSet.append(obj)
        if params.get("SampleSnapshotTaskSet") is not None:
            self.SampleSnapshotTaskSet = []
            for item in params.get("SampleSnapshotTaskSet"):
                obj = SampleSnapshotTaskInput()
                obj._deserialize(item)
                self.SampleSnapshotTaskSet.append(obj)
        if params.get("ImageSpriteTaskSet") is not None:
            self.ImageSpriteTaskSet = []
            for item in params.get("ImageSpriteTaskSet"):
                obj = ImageSpriteTaskInput()
                obj._deserialize(item)
                self.ImageSpriteTaskSet.append(obj)


class MediaProcessTaskResult(AbstractModel):
    """任務查詢結果類型

    """

    def __init__(self):
        """
        :param Type: 任務的類型，可以取的值有：
<li>Transcode：轉碼</li>
<li>AnimatedGraphics：轉動圖</li>
<li>SnapshotByTimeOffset：時間點截圖</li>
<li>SampleSnapshot：采樣截圖</li>
<li>ImageSprites：雪碧圖</li>
<li>CoverBySnapshot：截圖做封面</li>
<li>AdaptiveDynamicStreaming：自适應碼流</li>
        :type Type: str
        :param TranscodeTask: 視訊轉碼任務的查詢結果，當任務類型爲 Transcode 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranscodeTask: :class:`taifucloudcloud.mps.v20190612.models.MediaProcessTaskTranscodeResult`
        :param AnimatedGraphicTask: 視訊轉動圖任務的查詢結果，當任務類型爲 AnimatedGraphics 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AnimatedGraphicTask: :class:`taifucloudcloud.mps.v20190612.models.MediaProcessTaskAnimatedGraphicResult`
        :param SnapshotByTimeOffsetTask: 對視訊按時間點截圖任務的查詢結果，當任務類型爲 SnapshotByTimeOffset 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SnapshotByTimeOffsetTask: :class:`taifucloudcloud.mps.v20190612.models.MediaProcessTaskSnapshotByTimeOffsetResult`
        :param SampleSnapshotTask: 對視訊采樣截圖任務的查詢結果，當任務類型爲 SampleSnapshot 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SampleSnapshotTask: :class:`taifucloudcloud.mps.v20190612.models.MediaProcessTaskSampleSnapshotResult`
        :param ImageSpriteTask: 對視訊截雪碧圖任務的查詢結果，當任務類型爲 ImageSprite 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ImageSpriteTask: :class:`taifucloudcloud.mps.v20190612.models.MediaProcessTaskImageSpriteResult`
        """
        self.Type = None
        self.TranscodeTask = None
        self.AnimatedGraphicTask = None
        self.SnapshotByTimeOffsetTask = None
        self.SampleSnapshotTask = None
        self.ImageSpriteTask = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("TranscodeTask") is not None:
            self.TranscodeTask = MediaProcessTaskTranscodeResult()
            self.TranscodeTask._deserialize(params.get("TranscodeTask"))
        if params.get("AnimatedGraphicTask") is not None:
            self.AnimatedGraphicTask = MediaProcessTaskAnimatedGraphicResult()
            self.AnimatedGraphicTask._deserialize(params.get("AnimatedGraphicTask"))
        if params.get("SnapshotByTimeOffsetTask") is not None:
            self.SnapshotByTimeOffsetTask = MediaProcessTaskSnapshotByTimeOffsetResult()
            self.SnapshotByTimeOffsetTask._deserialize(params.get("SnapshotByTimeOffsetTask"))
        if params.get("SampleSnapshotTask") is not None:
            self.SampleSnapshotTask = MediaProcessTaskSampleSnapshotResult()
            self.SampleSnapshotTask._deserialize(params.get("SampleSnapshotTask"))
        if params.get("ImageSpriteTask") is not None:
            self.ImageSpriteTask = MediaProcessTaskImageSpriteResult()
            self.ImageSpriteTask._deserialize(params.get("ImageSpriteTask"))


class MediaProcessTaskSampleSnapshotResult(AbstractModel):
    """對視訊做采樣截圖任務結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0 表示成功，其他值表示失敗：
<li>40000：輸入參數不合法，請檢查輸入參數；</li>
<li>60000：源文件錯誤（如視訊數據損壞），請确認源文件是否正常；</li>
<li>70000：内部服務錯誤，建議重試。</li>
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 對視訊做采樣截圖任務輸入。
        :type Input: :class:`taifucloudcloud.mps.v20190612.models.SampleSnapshotTaskInput`
        :param Output: 對視訊做采樣截圖任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.mps.v20190612.models.MediaSampleSnapshotItem`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = SampleSnapshotTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaSampleSnapshotItem()
            self.Output._deserialize(params.get("Output"))


class MediaProcessTaskSnapshotByTimeOffsetResult(AbstractModel):
    """對視訊按指定時間點截圖任務結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0 表示成功，其他值表示失敗：
<li>40000：輸入參數不合法，請檢查輸入參數；</li>
<li>60000：源文件錯誤（如視訊數據損壞），請确認源文件是否正常；</li>
<li>70000：内部服務錯誤，建議重試。</li>
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 對視訊按指定時間點截圖任務輸入。
        :type Input: :class:`taifucloudcloud.mps.v20190612.models.SnapshotByTimeOffsetTaskInput`
        :param Output: 對視訊按指定時間點截圖任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.mps.v20190612.models.MediaSnapshotByTimeOffsetItem`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = SnapshotByTimeOffsetTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaSnapshotByTimeOffsetItem()
            self.Output._deserialize(params.get("Output"))


class MediaProcessTaskTranscodeResult(AbstractModel):
    """轉碼任務結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0 表示成功，其他值表示失敗：
<li>40000：輸入參數不合法，請檢查輸入參數；</li>
<li>60000：源文件錯誤（如視訊數據損壞），請确認源文件是否正常；</li>
<li>70000：内部服務錯誤，建議重試。</li>
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 轉碼任務的輸入。
        :type Input: :class:`taifucloudcloud.mps.v20190612.models.TranscodeTaskInput`
        :param Output: 轉碼任務的輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.mps.v20190612.models.MediaTranscodeItem`
        """
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = TranscodeTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaTranscodeItem()
            self.Output._deserialize(params.get("Output"))


class MediaSampleSnapshotItem(AbstractModel):
    """采樣截圖訊息

    """

    def __init__(self):
        """
        :param Definition: 采樣截圖規格 ID，參見[采樣截圖參數範本](https://cloud.taifucloud.com/document/product/266/33480#.E9.87.87.E6.A0.B7.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
        :type Definition: int
        :param SampleType: 采樣方式，取值範圍：
<li>Percent：根據百分比間隔采樣。</li>
<li>Time：根據時間間隔采樣。</li>
        :type SampleType: str
        :param Interval: 采樣間隔
<li>當 SampleType 爲 Percent 時，該值表示多少百分比一張圖。</li>
<li>當 SampleType 爲 Time 時，該值表示多少時間間隔一張圖，單位秒， 第一張圖均爲視訊首幀。</li>
        :type Interval: int
        :param Storage: 截圖後文件的儲存位置。
        :type Storage: :class:`taifucloudcloud.mps.v20190612.models.TaskOutputStorage`
        :param ImagePathSet: 生成的截圖 path 清單。
        :type ImagePathSet: list of str
        :param WaterMarkDefinition: 截圖如果被打上了浮水印，被打水印的範本 ID 清單。
        :type WaterMarkDefinition: list of int
        """
        self.Definition = None
        self.SampleType = None
        self.Interval = None
        self.Storage = None
        self.ImagePathSet = None
        self.WaterMarkDefinition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SampleType = params.get("SampleType")
        self.Interval = params.get("Interval")
        if params.get("Storage") is not None:
            self.Storage = TaskOutputStorage()
            self.Storage._deserialize(params.get("Storage"))
        self.ImagePathSet = params.get("ImagePathSet")
        self.WaterMarkDefinition = params.get("WaterMarkDefinition")


class MediaSnapshotByTimeOffsetItem(AbstractModel):
    """點播文件指定時間點截圖訊息

    """

    def __init__(self):
        """
        :param Definition: 指定時間點截圖規格，參見[指定時間點截圖參數範本](https://cloud.taifucloud.com/document/product/266/33480#.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
        :type Definition: int
        :param PicInfoSet: 同一規格的截圖訊息集合，每個元素代表一張截圖。
        :type PicInfoSet: list of MediaSnapshotByTimePicInfoItem
        :param Storage: 指定時間點截圖文件的儲存位置。
        :type Storage: :class:`taifucloudcloud.mps.v20190612.models.TaskOutputStorage`
        """
        self.Definition = None
        self.PicInfoSet = None
        self.Storage = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("PicInfoSet") is not None:
            self.PicInfoSet = []
            for item in params.get("PicInfoSet"):
                obj = MediaSnapshotByTimePicInfoItem()
                obj._deserialize(item)
                self.PicInfoSet.append(obj)
        if params.get("Storage") is not None:
            self.Storage = TaskOutputStorage()
            self.Storage._deserialize(params.get("Storage"))


class MediaSnapshotByTimePicInfoItem(AbstractModel):
    """指定時間點截圖訊息

    """

    def __init__(self):
        """
        :param TimeOffset: 該張截圖對應視訊文件中的時間偏移，單位爲<font color=red>毫秒</font>。
        :type TimeOffset: float
        :param Path: 該張截圖的路徑。
        :type Path: str
        :param WaterMarkDefinition: 截圖如果被打上了浮水印，被打水印的範本 ID 清單。
        :type WaterMarkDefinition: list of int
        """
        self.TimeOffset = None
        self.Path = None
        self.WaterMarkDefinition = None


    def _deserialize(self, params):
        self.TimeOffset = params.get("TimeOffset")
        self.Path = params.get("Path")
        self.WaterMarkDefinition = params.get("WaterMarkDefinition")


class MediaTranscodeItem(AbstractModel):
    """轉碼訊息

    """

    def __init__(self):
        """
        :param OutputStorage: 轉碼後文件的目標儲存。
        :type OutputStorage: :class:`taifucloudcloud.mps.v20190612.models.TaskOutputStorage`
        :param Path: 轉碼後的視訊文件路徑。
        :type Path: str
        :param Definition: 轉碼規格 ID，參見[轉碼參數範本](https://cloud.taifucloud.com/document/product/862/37042)。
        :type Definition: int
        :param Bitrate: 視訊流碼率平均值與音訊流碼率平均值之和， 單位：bps。
        :type Bitrate: int
        :param Height: 視訊流高度的最大值，單位：px。
        :type Height: int
        :param Width: 視訊流寬度的最大值，單位：px。
        :type Width: int
        :param Size: 媒體文件總大小（視訊爲 HLS 時，大小是 m3u8 和 ts 文件大小的總和），單位：位元。
        :type Size: int
        :param Duration: 視訊時長，單位：秒。
        :type Duration: float
        :param Container: 容器類型，例如 m4a，mp4 等。
        :type Container: str
        :param Md5: 視訊的 md5 值。
        :type Md5: str
        :param AudioStreamSet: 音訊流訊息。
        :type AudioStreamSet: list of MediaAudioStreamItem
        :param VideoStreamSet: 視訊流訊息。
        :type VideoStreamSet: list of MediaVideoStreamItem
        """
        self.OutputStorage = None
        self.Path = None
        self.Definition = None
        self.Bitrate = None
        self.Height = None
        self.Width = None
        self.Size = None
        self.Duration = None
        self.Container = None
        self.Md5 = None
        self.AudioStreamSet = None
        self.VideoStreamSet = None


    def _deserialize(self, params):
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.Path = params.get("Path")
        self.Definition = params.get("Definition")
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Size = params.get("Size")
        self.Duration = params.get("Duration")
        self.Container = params.get("Container")
        self.Md5 = params.get("Md5")
        if params.get("AudioStreamSet") is not None:
            self.AudioStreamSet = []
            for item in params.get("AudioStreamSet"):
                obj = MediaAudioStreamItem()
                obj._deserialize(item)
                self.AudioStreamSet.append(obj)
        if params.get("VideoStreamSet") is not None:
            self.VideoStreamSet = []
            for item in params.get("VideoStreamSet"):
                obj = MediaVideoStreamItem()
                obj._deserialize(item)
                self.VideoStreamSet.append(obj)


class MediaVideoStreamItem(AbstractModel):
    """點播文件視訊流訊息

    """

    def __init__(self):
        """
        :param Bitrate: 視訊流的碼率，單位：bps。
        :type Bitrate: int
        :param Height: 視訊流的高度，單位：px。
        :type Height: int
        :param Width: 視訊流的寬度，單位：px。
        :type Width: int
        :param Codec: 視訊流的編碼格式，例如 h264。
        :type Codec: str
        :param Fps: 幀率，單位：hz。
        :type Fps: int
        """
        self.Bitrate = None
        self.Height = None
        self.Width = None
        self.Codec = None
        self.Fps = None


    def _deserialize(self, params):
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")


class ModifyAIAnalysisTemplateRequest(AbstractModel):
    """ModifyAIAnalysisTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Definition: 視訊内容分析範本唯一標識。
        :type Definition: int
        :param Name: 視訊内容分析範本名稱，長度限制：64 個字元。
        :type Name: str
        :param Comment: 視訊内容分析範本描述訊息，長度限制：256 個字元。
        :type Comment: str
        :param ClassificationConfigure: 智慧分類任務控制參數。
        :type ClassificationConfigure: :class:`taifucloudcloud.mps.v20190612.models.ClassificationConfigureInfoForUpdate`
        :param TagConfigure: 智慧標簽任務控制參數。
        :type TagConfigure: :class:`taifucloudcloud.mps.v20190612.models.TagConfigureInfoForUpdate`
        :param CoverConfigure: 智慧封面任務控制參數。
        :type CoverConfigure: :class:`taifucloudcloud.mps.v20190612.models.CoverConfigureInfoForUpdate`
        :param FrameTagConfigure: 智慧按幀標簽任務控制參數。
        :type FrameTagConfigure: :class:`taifucloudcloud.mps.v20190612.models.FrameTagConfigureInfoForUpdate`
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.ClassificationConfigure = None
        self.TagConfigure = None
        self.CoverConfigure = None
        self.FrameTagConfigure = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("ClassificationConfigure") is not None:
            self.ClassificationConfigure = ClassificationConfigureInfoForUpdate()
            self.ClassificationConfigure._deserialize(params.get("ClassificationConfigure"))
        if params.get("TagConfigure") is not None:
            self.TagConfigure = TagConfigureInfoForUpdate()
            self.TagConfigure._deserialize(params.get("TagConfigure"))
        if params.get("CoverConfigure") is not None:
            self.CoverConfigure = CoverConfigureInfoForUpdate()
            self.CoverConfigure._deserialize(params.get("CoverConfigure"))
        if params.get("FrameTagConfigure") is not None:
            self.FrameTagConfigure = FrameTagConfigureInfoForUpdate()
            self.FrameTagConfigure._deserialize(params.get("FrameTagConfigure"))


class ModifyAIAnalysisTemplateResponse(AbstractModel):
    """ModifyAIAnalysisTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAIRecognitionTemplateRequest(AbstractModel):
    """ModifyAIRecognitionTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Definition: 視訊内容識别範本唯一標識。
        :type Definition: int
        :param Name: 視訊内容識别範本名稱，長度限制：64 個字元。
        :type Name: str
        :param Comment: 視訊内容識别範本描述訊息，長度限制：256 個字元。
        :type Comment: str
        :param FaceConfigure: 人臉識别控制參數。
        :type FaceConfigure: :class:`taifucloudcloud.mps.v20190612.models.FaceConfigureInfoForUpdate`
        :param OcrFullTextConfigure: 文本全文識别控制參數。
        :type OcrFullTextConfigure: :class:`taifucloudcloud.mps.v20190612.models.OcrFullTextConfigureInfoForUpdate`
        :param OcrWordsConfigure: 文本關鍵詞識别控制參數。
        :type OcrWordsConfigure: :class:`taifucloudcloud.mps.v20190612.models.OcrWordsConfigureInfoForUpdate`
        :param AsrFullTextConfigure: 語音全文識别控制參數。
        :type AsrFullTextConfigure: :class:`taifucloudcloud.mps.v20190612.models.AsrFullTextConfigureInfoForUpdate`
        :param AsrWordsConfigure: 語音關鍵詞識别控制參數。
        :type AsrWordsConfigure: :class:`taifucloudcloud.mps.v20190612.models.AsrWordsConfigureInfoForUpdate`
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.FaceConfigure = None
        self.OcrFullTextConfigure = None
        self.OcrWordsConfigure = None
        self.AsrFullTextConfigure = None
        self.AsrWordsConfigure = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("FaceConfigure") is not None:
            self.FaceConfigure = FaceConfigureInfoForUpdate()
            self.FaceConfigure._deserialize(params.get("FaceConfigure"))
        if params.get("OcrFullTextConfigure") is not None:
            self.OcrFullTextConfigure = OcrFullTextConfigureInfoForUpdate()
            self.OcrFullTextConfigure._deserialize(params.get("OcrFullTextConfigure"))
        if params.get("OcrWordsConfigure") is not None:
            self.OcrWordsConfigure = OcrWordsConfigureInfoForUpdate()
            self.OcrWordsConfigure._deserialize(params.get("OcrWordsConfigure"))
        if params.get("AsrFullTextConfigure") is not None:
            self.AsrFullTextConfigure = AsrFullTextConfigureInfoForUpdate()
            self.AsrFullTextConfigure._deserialize(params.get("AsrFullTextConfigure"))
        if params.get("AsrWordsConfigure") is not None:
            self.AsrWordsConfigure = AsrWordsConfigureInfoForUpdate()
            self.AsrWordsConfigure._deserialize(params.get("AsrWordsConfigure"))


class ModifyAIRecognitionTemplateResponse(AbstractModel):
    """ModifyAIRecognitionTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAnimatedGraphicsTemplateRequest(AbstractModel):
    """ModifyAnimatedGraphicsTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Definition: 轉動圖範本唯一標識。
        :type Definition: int
        :param Name: 轉動圖範本名稱，長度限制：64 個字元。
        :type Name: str
        :param Width: 動圖寬度（或長邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
        :type Width: int
        :param Height: 動圖高度（或短邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适應，可選值：
<li>open：開啓，此時，Width 代表視訊的長邊，Height 表示視訊的短邊；</li>
<li>close：關閉，此時，Width 代表視訊的寬度，Height 表示視訊的高度。</li>
預設值：open。
        :type ResolutionAdaptive: str
        :param Format: 動圖格式，取值爲 gif 和 webp。
        :type Format: str
        :param Fps: 幀率，取值範圍：[1, 30]，單位：Hz。
        :type Fps: int
        :param Quality: 圖片質量，取值範圍：[1, 100]，預設值爲 75。
        :type Quality: float
        :param Comment: 範本描述訊息，長度限制：256 個字元。
        :type Comment: str
        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Fps = None
        self.Quality = None
        self.Comment = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Fps = params.get("Fps")
        self.Quality = params.get("Quality")
        self.Comment = params.get("Comment")


class ModifyAnimatedGraphicsTemplateResponse(AbstractModel):
    """ModifyAnimatedGraphicsTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyContentReviewTemplateRequest(AbstractModel):
    """ModifyContentReviewTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Definition: 内容審核範本唯一標識。
        :type Definition: int
        :param Name: 内容審核範本名稱，長度限制：64 個字元。
        :type Name: str
        :param Comment: 内容審核範本描述訊息，長度限制：256 個字元。
        :type Comment: str
        :param PornConfigure:  控制參數。
        :type PornConfigure: :class:`taifucloudcloud.mps.v20190612.models.PornConfigureInfoForUpdate`
        :param TerrorismConfigure: 鑒恐控制參數。
        :type TerrorismConfigure: :class:`taifucloudcloud.mps.v20190612.models.TerrorismConfigureInfoForUpdate`
        :param PoliticalConfigure: 鑒政控制參數。
        :type PoliticalConfigure: :class:`taifucloudcloud.mps.v20190612.models.PoliticalConfigureInfoForUpdate`
        :param ProhibitedConfigure: 違禁控制參數。違禁内容包括：
<li>謾罵；</li>
<li>涉毒違法。</li>
注意：此參數尚未支援。
        :type ProhibitedConfigure: :class:`taifucloudcloud.mps.v20190612.models.ProhibitedConfigureInfoForUpdate`
        :param UserDefineConfigure: 用戶自定義内容審核控制參數。
        :type UserDefineConfigure: :class:`taifucloudcloud.mps.v20190612.models.UserDefineConfigureInfoForUpdate`
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.PornConfigure = None
        self.TerrorismConfigure = None
        self.PoliticalConfigure = None
        self.ProhibitedConfigure = None
        self.UserDefineConfigure = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("PornConfigure") is not None:
            self.PornConfigure = PornConfigureInfoForUpdate()
            self.PornConfigure._deserialize(params.get("PornConfigure"))
        if params.get("TerrorismConfigure") is not None:
            self.TerrorismConfigure = TerrorismConfigureInfoForUpdate()
            self.TerrorismConfigure._deserialize(params.get("TerrorismConfigure"))
        if params.get("PoliticalConfigure") is not None:
            self.PoliticalConfigure = PoliticalConfigureInfoForUpdate()
            self.PoliticalConfigure._deserialize(params.get("PoliticalConfigure"))
        if params.get("ProhibitedConfigure") is not None:
            self.ProhibitedConfigure = ProhibitedConfigureInfoForUpdate()
            self.ProhibitedConfigure._deserialize(params.get("ProhibitedConfigure"))
        if params.get("UserDefineConfigure") is not None:
            self.UserDefineConfigure = UserDefineConfigureInfoForUpdate()
            self.UserDefineConfigure._deserialize(params.get("UserDefineConfigure"))


class ModifyContentReviewTemplateResponse(AbstractModel):
    """ModifyContentReviewTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyImageSpriteTemplateRequest(AbstractModel):
    """ModifyImageSpriteTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Definition: 雪碧圖範本唯一標識。
        :type Definition: int
        :param Name: 雪碧圖範本名稱，長度限制：64 個字元。
        :type Name: str
        :param Width: 雪碧圖中小圖的寬度（或長邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
        :type Width: int
        :param Height: 雪碧圖中小圖的高度（或短邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适應，可選值：
<li>open：開啓，此時，Width 代表視訊的長邊，Height 表示視訊的短邊；</li>
<li>close：關閉，此時，Width 代表視訊的寬度，Height 表示視訊的高度。</li>
預設值：open。
        :type ResolutionAdaptive: str
        :param SampleType: 采樣類型，取值：
<li>Percent：按百分比。</li>
<li>Time：按時間間隔。</li>
        :type SampleType: str
        :param SampleInterval: 采樣間隔。
<li>當 SampleType 爲 Percent 時，指定采樣間隔的百分比。</li>
<li>當 SampleType 爲 Time 時，指定采樣間隔的時間，單位爲秒。</li>
        :type SampleInterval: int
        :param RowCount: 雪碧圖中小圖的行數。
        :type RowCount: int
        :param ColumnCount: 雪碧圖中小圖的列數。
        :type ColumnCount: int
        :param FillType: 填充方式，當視訊流配置寬高參數與原始視訊的寬高比不一緻時，對轉碼的處理方式，即爲“填充”。可選填充方式：
<li> stretch：拉伸，對每一幀進行拉伸，填滿整個畫面，可能導緻轉碼後的視訊被“壓扁“或者“拉長“；</li>
<li>black：留黑，保持視訊寬高比不變，邊緣剩餘部分使用黑色填充。</li>
預設值：black 。
        :type FillType: str
        :param Comment: 範本描述訊息，長度限制：256 個字元。
        :type Comment: str
        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.SampleType = None
        self.SampleInterval = None
        self.RowCount = None
        self.ColumnCount = None
        self.FillType = None
        self.Comment = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.RowCount = params.get("RowCount")
        self.ColumnCount = params.get("ColumnCount")
        self.FillType = params.get("FillType")
        self.Comment = params.get("Comment")


class ModifyImageSpriteTemplateResponse(AbstractModel):
    """ModifyImageSpriteTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPersonSampleRequest(AbstractModel):
    """ModifyPersonSample請求參數結構體

    """

    def __init__(self):
        """
        :param PersonId: 人物 ID。
        :type PersonId: str
        :param Name: 名稱，長度限制：128 個字元。
        :type Name: str
        :param Description: 描述，長度限制：1024 個字元。
        :type Description: str
        :param Usages: 人物應用場景，可選值：
1. Recognition：用於内容識别，等價於 Recognition.Face。
2. Review：用於内容審核，等價於 Review.Face。
3. All：用於内容識别、内容審核，等價於 1+2。
        :type Usages: list of str
        :param FaceOperationInfo: 人臉操作訊息。
        :type FaceOperationInfo: :class:`taifucloudcloud.mps.v20190612.models.AiSampleFaceOperation`
        :param TagOperationInfo: 標簽操作訊息。
        :type TagOperationInfo: :class:`taifucloudcloud.mps.v20190612.models.AiSampleTagOperation`
        """
        self.PersonId = None
        self.Name = None
        self.Description = None
        self.Usages = None
        self.FaceOperationInfo = None
        self.TagOperationInfo = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.Usages = params.get("Usages")
        if params.get("FaceOperationInfo") is not None:
            self.FaceOperationInfo = AiSampleFaceOperation()
            self.FaceOperationInfo._deserialize(params.get("FaceOperationInfo"))
        if params.get("TagOperationInfo") is not None:
            self.TagOperationInfo = AiSampleTagOperation()
            self.TagOperationInfo._deserialize(params.get("TagOperationInfo"))


class ModifyPersonSampleResponse(AbstractModel):
    """ModifyPersonSample返回參數結構體

    """

    def __init__(self):
        """
        :param Person: 人物訊息。
        :type Person: :class:`taifucloudcloud.mps.v20190612.models.AiSamplePerson`
        :param FailFaceInfoSet: 處理失敗的人臉訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FailFaceInfoSet: list of AiSampleFailFaceInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Person = None
        self.FailFaceInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Person") is not None:
            self.Person = AiSamplePerson()
            self.Person._deserialize(params.get("Person"))
        if params.get("FailFaceInfoSet") is not None:
            self.FailFaceInfoSet = []
            for item in params.get("FailFaceInfoSet"):
                obj = AiSampleFailFaceInfo()
                obj._deserialize(item)
                self.FailFaceInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class ModifySampleSnapshotTemplateRequest(AbstractModel):
    """ModifySampleSnapshotTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Definition: 采樣截圖範本唯一標識。
        :type Definition: int
        :param Name: 采樣截圖範本名稱，長度限制：64 個字元。
        :type Name: str
        :param Width: 截圖寬度（或長邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
        :type Width: int
        :param Height: 截圖高度（或短邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适應，可選值：
<li>open：開啓，此時，Width 代表視訊的長邊，Height 表示視訊的短邊；</li>
<li>close：關閉，此時，Width 代表視訊的寬度，Height 表示視訊的高度。</li>
預設值：open。
        :type ResolutionAdaptive: str
        :param SampleType: 采樣截圖類型，取值：
<li>Percent：按百分比。</li>
<li>Time：按時間間隔。</li>
        :type SampleType: str
        :param SampleInterval: 采樣間隔。
<li>當 SampleType 爲 Percent 時，指定采樣間隔的百分比。</li>
<li>當 SampleType 爲 Time 時，指定采樣間隔的時間，單位爲秒。</li>
        :type SampleInterval: int
        :param Format: 圖片格式，取值爲 jpg 和 png。
        :type Format: str
        :param Comment: 範本描述訊息，長度限制：256 個字元。
        :type Comment: str
        :param FillType: 填充方式，當視訊流配置寬高參數與原始視訊的寬高比不一緻時，對轉碼的處理方式，即爲“填充”。可選填充方式：
<li> stretch：拉伸，對每一幀進行拉伸，填滿整個畫面，可能導緻轉碼後的視訊被“壓扁“或者“拉長“；</li>
<li>black：留黑，保持視訊寬高比不變，邊緣剩餘部分使用黑色填充。</li>
<li>white：留白，保持視訊寬高比不變，邊緣剩餘部分使用白色填充。</li>
<li>gauss：高斯模糊，保持視訊寬高比不變，邊緣剩餘部分使用高斯模糊。</li>
預設值：black 。
        :type FillType: str
        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.SampleType = None
        self.SampleInterval = None
        self.Format = None
        self.Comment = None
        self.FillType = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")
        self.FillType = params.get("FillType")


class ModifySampleSnapshotTemplateResponse(AbstractModel):
    """ModifySampleSnapshotTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySnapshotByTimeOffsetTemplateRequest(AbstractModel):
    """ModifySnapshotByTimeOffsetTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Definition: 指定時間點截圖範本唯一標識。
        :type Definition: int
        :param Name: 指定時間點截圖範本名稱，長度限制：64 個字元。
        :type Name: str
        :param Width: 截圖寬度（或長邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
        :type Width: int
        :param Height: 截圖高度（或短邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适應，可選值：
<li>open：開啓，此時，Width 代表視訊的長邊，Height 表示視訊的短邊；</li>
<li>close：關閉，此時，Width 代表視訊的寬度，Height 表示視訊的高度。</li>
預設值：open。
        :type ResolutionAdaptive: str
        :param Format: 圖片格式，取值可以爲 jpg 和 png。
        :type Format: str
        :param Comment: 範本描述訊息，長度限制：256 個字元。
        :type Comment: str
        :param FillType: 填充方式，當視訊流配置寬高參數與原始視訊的寬高比不一緻時，對轉碼的處理方式，即爲“填充”。可選填充方式：
<li> stretch：拉伸，對每一幀進行拉伸，填滿整個畫面，可能導緻轉碼後的視訊被“壓扁“或者“拉長“；</li>
<li>black：留黑，保持視訊寬高比不變，邊緣剩餘部分使用黑色填充。</li>
<li>white：留白，保持視訊寬高比不變，邊緣剩餘部分使用白色填充。</li>
<li>gauss：高斯模糊，保持視訊寬高比不變，邊緣剩餘部分使用高斯模糊。</li>
預設值：black 。
        :type FillType: str
        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Comment = None
        self.FillType = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")
        self.FillType = params.get("FillType")


class ModifySnapshotByTimeOffsetTemplateResponse(AbstractModel):
    """ModifySnapshotByTimeOffsetTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTranscodeTemplateRequest(AbstractModel):
    """ModifyTranscodeTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Definition: 轉碼範本唯一標識。
        :type Definition: int
        :param Container: 封裝格式，可選值：mp4、flv、hls、mp3、flac、ogg、m4a。其中，mp3、flac、ogg、m4a 爲純音訊文件。
        :type Container: str
        :param Name: 轉碼範本名稱，長度限制：64 個字元。
        :type Name: str
        :param Comment: 範本描述訊息，長度限制：256 個位元。
        :type Comment: str
        :param RemoveVideo: 是否去除視訊數據，可選值：
<li>0：保留</li>
<li>1：去除</li>
        :type RemoveVideo: int
        :param RemoveAudio: 是否去除音訊數據，可選值：
<li>0：保留</li>
<li>1：去除</li>
        :type RemoveAudio: int
        :param VideoTemplate: 視訊流配置參數。
        :type VideoTemplate: :class:`taifucloudcloud.mps.v20190612.models.VideoTemplateInfoForUpdate`
        :param AudioTemplate: 音訊流配置參數。
        :type AudioTemplate: :class:`taifucloudcloud.mps.v20190612.models.AudioTemplateInfoForUpdate`
        :param TEHDConfig: 極速高清轉碼參數。
        :type TEHDConfig: :class:`taifucloudcloud.mps.v20190612.models.TEHDConfigForUpdate`
        """
        self.Definition = None
        self.Container = None
        self.Name = None
        self.Comment = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.TEHDConfig = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Container = params.get("Container")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfoForUpdate()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfoForUpdate()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfigForUpdate()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))


class ModifyTranscodeTemplateResponse(AbstractModel):
    """ModifyTranscodeTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyWatermarkTemplateRequest(AbstractModel):
    """ModifyWatermarkTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Definition: 浮水印範本唯一標識。
        :type Definition: int
        :param Name: 浮水印範本名稱，長度限制：64 個字元。
        :type Name: str
        :param Comment: 範本描述訊息，長度限制：256 個字元。
        :type Comment: str
        :param CoordinateOrigin: 原點位置，可選值：
<li>TopLeft：表示坐標原點位於視訊圖像左上角，浮水印原點爲圖片或文字的左上角；</li>
<li>TopRight：表示坐標原點位於視訊圖像的右上角，浮水印原點爲圖片或文字的右上角；</li>
<li>BottomLeft：表示坐標原點位於視訊圖像的左下角，浮水印原點爲圖片或文字的左下角；</li>
<li>BottomRight：表示坐標原點位於視訊圖像的右下角，浮水印原點爲圖片或文字的右下角。</li>
        :type CoordinateOrigin: str
        :param XPos: 浮水印原點距離視訊圖像坐標原點的水平位置。支援 %、px 兩種格式：
<li>當字串以 % 結尾，表示浮水印 XPos 爲視訊寬度指定百分比，如 10% 表示 XPos 爲視訊寬度的 10%；</li>
<li>當字串以 px 結尾，表示浮水印 XPos 爲指定像素，如 100px 表示 XPos 爲 100 像素。</li>
        :type XPos: str
        :param YPos: 浮水印原點距離視訊圖像坐標原點的垂直位置。支援 %、px 兩種格式：
<li>當字串以 % 結尾，表示浮水印 YPos 爲視訊高度指定百分比，如 10% 表示 YPos 爲視訊高度的 10%；</li>
<li>當字串以 px 結尾，表示浮水印 YPos 爲指定像素，如 100px 表示 YPos 爲 100 像素。</li>
        :type YPos: str
        :param ImageTemplate: 圖片浮水印範本，該欄位僅對圖片水印範本有效。
        :type ImageTemplate: :class:`taifucloudcloud.mps.v20190612.models.ImageWatermarkInputForUpdate`
        :param TextTemplate: 文字浮水印範本，該欄位僅對文字水印範本有效。
        :type TextTemplate: :class:`taifucloudcloud.mps.v20190612.models.TextWatermarkTemplateInputForUpdate`
        :param SvgTemplate: SVG浮水印範本，當 Type 爲 svg，該欄位必填。當 Type 爲 image 或 text，該欄位無效。
        :type SvgTemplate: :class:`taifucloudcloud.mps.v20190612.models.SvgWatermarkInputForUpdate`
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.ImageTemplate = None
        self.TextTemplate = None
        self.SvgTemplate = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        if params.get("ImageTemplate") is not None:
            self.ImageTemplate = ImageWatermarkInputForUpdate()
            self.ImageTemplate._deserialize(params.get("ImageTemplate"))
        if params.get("TextTemplate") is not None:
            self.TextTemplate = TextWatermarkTemplateInputForUpdate()
            self.TextTemplate._deserialize(params.get("TextTemplate"))
        if params.get("SvgTemplate") is not None:
            self.SvgTemplate = SvgWatermarkInputForUpdate()
            self.SvgTemplate._deserialize(params.get("SvgTemplate"))


class ModifyWatermarkTemplateResponse(AbstractModel):
    """ModifyWatermarkTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param ImageUrl: 圖片浮水印網址，僅當 ImageTemplate.ImageContent 非空，該欄位有效。
        :type ImageUrl: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ImageUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.RequestId = params.get("RequestId")


class ModifyWordSampleRequest(AbstractModel):
    """ModifyWordSample請求參數結構體

    """

    def __init__(self):
        """
        :param Keyword: 關鍵詞，長度限制：128 個字元。
        :type Keyword: str
        :param Usages: <b>關鍵詞應用場景，可選值：</b>
1. Recognition.Ocr：通過光學字元識别技術，進行内容識别；
2. Recognition.Asr：通過語音識别技術，進行内容識别；
3. Review.Ocr：通過光學字元識别技術，進行内容審核；
4. Review.Asr：通過語音識别技術，進行内容審核；
<b>可合並簡寫爲：</b>
5. Recognition：通過光學字元識别技術、語音識别技術，進行内容識别，等價於 1+2；
6. Review：通過光學字元識别技術、語音識别技術，進行内容審核，等價於 3+4；
7. All：通過光學字元識别技術、語音識别技術，進行内容識别、内容審核，等價於 1+2+3+4。
        :type Usages: list of str
        :param TagOperationInfo: 標簽操作訊息。
        :type TagOperationInfo: :class:`taifucloudcloud.mps.v20190612.models.AiSampleTagOperation`
        """
        self.Keyword = None
        self.Usages = None
        self.TagOperationInfo = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.Usages = params.get("Usages")
        if params.get("TagOperationInfo") is not None:
            self.TagOperationInfo = AiSampleTagOperation()
            self.TagOperationInfo._deserialize(params.get("TagOperationInfo"))


class ModifyWordSampleResponse(AbstractModel):
    """ModifyWordSample返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NumberFormat(AbstractModel):
    """輸出文件名的`{number}`變量的規則。

    """

    def __init__(self):
        """
        :param InitialValue: `{number}`變量的起始值，預設爲0。
        :type InitialValue: int
        :param Increment: `{number}`變量的增長步長，預設爲1。
        :type Increment: int
        :param MinLength: `{number}`變量的最小長度，不足時補占位符。預設爲1。
        :type MinLength: int
        :param PlaceHolder: `{number}`變量的長度不足時，補充的占位符。預設爲"0"。
        :type PlaceHolder: str
        """
        self.InitialValue = None
        self.Increment = None
        self.MinLength = None
        self.PlaceHolder = None


    def _deserialize(self, params):
        self.InitialValue = params.get("InitialValue")
        self.Increment = params.get("Increment")
        self.MinLength = params.get("MinLength")
        self.PlaceHolder = params.get("PlaceHolder")


class OcrFullTextConfigureInfo(AbstractModel):
    """文本全文本識别任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 文本全文識别任務開關，可選值：
<li>ON：開啓智慧文本全文識别任務；</li>
<li>OFF：關閉智慧文本全文識别任務。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class OcrFullTextConfigureInfoForUpdate(AbstractModel):
    """文本全文本識别任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 文本全文識别任務開關，可選值：
<li>ON：開啓智慧文本全文識别任務；</li>
<li>OFF：關閉智慧文本全文識别任務。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class OcrWordsConfigureInfo(AbstractModel):
    """文本關鍵詞識别控制參數。

    """

    def __init__(self):
        """
        :param Switch: 文本關鍵詞識别任務開關，可選值：
<li>ON：開啓文本關鍵詞識别任務；</li>
<li>OFF：關閉文本關鍵詞識别任務。</li>
        :type Switch: str
        :param LabelSet: 關鍵詞過濾標簽，指定需要返回的關鍵詞的標簽。如果未填或者爲空，則全部結果都返回。
標簽個數最多 10 個，每個標簽長度最多 16 個字元。
        :type LabelSet: list of str
        """
        self.Switch = None
        self.LabelSet = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")


class OcrWordsConfigureInfoForUpdate(AbstractModel):
    """文本關鍵詞識别控制參數。

    """

    def __init__(self):
        """
        :param Switch: 文本關鍵詞識别任務開關，可選值：
<li>ON：開啓文本關鍵詞識别任務；</li>
<li>OFF：關閉文本關鍵詞識别任務。</li>
        :type Switch: str
        :param LabelSet: 關鍵詞過濾標簽，指定需要返回的關鍵詞的標簽。如果未填或者爲空，則全部結果都返回。
標簽個數最多 10 個，每個標簽長度最多 16 個字元。
        :type LabelSet: list of str
        """
        self.Switch = None
        self.LabelSet = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")


class ParseLiveStreamProcessNotificationRequest(AbstractModel):
    """ParseLiveStreamProcessNotification請求參數結構體

    """

    def __init__(self):
        """
        :param Content: 從 CMQ 獲取到的直播流事件通知内容。
        :type Content: str
        """
        self.Content = None


    def _deserialize(self, params):
        self.Content = params.get("Content")


class ParseLiveStreamProcessNotificationResponse(AbstractModel):
    """ParseLiveStreamProcessNotification返回參數結構體

    """

    def __init__(self):
        """
        :param NotificationType: 直播流處理結果類型，包含：
<li>AiReviewResult：内容審核結果；</li>
<li>AiRecognitionResult：内容識别結果；</li>
<li>ProcessEof：直播流處理結束。</li>
        :type NotificationType: str
        :param TaskId: 視訊處理任務 ID。
        :type TaskId: str
        :param ProcessEofInfo: 直播流處理錯誤訊息，當 NotificationType 爲 ProcessEof 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProcessEofInfo: :class:`taifucloudcloud.mps.v20190612.models.LiveStreamProcessErrorInfo`
        :param AiReviewResultInfo: 内容審核結果，當 NotificationType 爲 AiReviewResult 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AiReviewResultInfo: :class:`taifucloudcloud.mps.v20190612.models.LiveStreamAiReviewResultInfo`
        :param AiRecognitionResultInfo: 内容識别結果，當 NotificationType 爲 AiRecognitionResult 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AiRecognitionResultInfo: :class:`taifucloudcloud.mps.v20190612.models.LiveStreamAiRecognitionResultInfo`
        :param SessionId: 用於去重的識别碼，如果七天内曾有過相同的識别碼的請求，則本次的請求會返回錯誤。最長50個字元，不帶或者帶空字串表示不做去重。
        :type SessionId: str
        :param SessionContext: 來源上下文，用於透傳用戶請求訊息，任務流狀态變更回調将返回該欄位值，最長1000個字元。
        :type SessionContext: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NotificationType = None
        self.TaskId = None
        self.ProcessEofInfo = None
        self.AiReviewResultInfo = None
        self.AiRecognitionResultInfo = None
        self.SessionId = None
        self.SessionContext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NotificationType = params.get("NotificationType")
        self.TaskId = params.get("TaskId")
        if params.get("ProcessEofInfo") is not None:
            self.ProcessEofInfo = LiveStreamProcessErrorInfo()
            self.ProcessEofInfo._deserialize(params.get("ProcessEofInfo"))
        if params.get("AiReviewResultInfo") is not None:
            self.AiReviewResultInfo = LiveStreamAiReviewResultInfo()
            self.AiReviewResultInfo._deserialize(params.get("AiReviewResultInfo"))
        if params.get("AiRecognitionResultInfo") is not None:
            self.AiRecognitionResultInfo = LiveStreamAiRecognitionResultInfo()
            self.AiRecognitionResultInfo._deserialize(params.get("AiRecognitionResultInfo"))
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")
        self.RequestId = params.get("RequestId")


class ParseNotificationRequest(AbstractModel):
    """ParseNotification請求參數結構體

    """

    def __init__(self):
        """
        :param Content: 從 CMQ 獲取到的事件通知内容。
        :type Content: str
        """
        self.Content = None


    def _deserialize(self, params):
        self.Content = params.get("Content")


class ParseNotificationResponse(AbstractModel):
    """ParseNotification返回參數結構體

    """

    def __init__(self):
        """
        :param EventType: 支援事件類型，目前取值有：
<li>WorkflowTask：視訊工作流處理任務。</li>
<li>EditMediaTask：視訊編輯任務。</li>
        :type EventType: str
        :param WorkflowTaskEvent: 視訊處理任務訊息，僅當 TaskType 爲 WorkflowTask，該欄位有值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type WorkflowTaskEvent: :class:`taifucloudcloud.mps.v20190612.models.WorkflowTask`
        :param EditMediaTaskEvent: 視訊編輯任務訊息，僅當 TaskType 爲 EditMediaTask，該欄位有值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type EditMediaTaskEvent: :class:`taifucloudcloud.mps.v20190612.models.EditMediaTask`
        :param SessionId: 用於去重的識别碼，如果七天内曾有過相同的識别碼的請求，則本次的請求會返回錯誤。最長50個字元，不帶或者帶空字串表示不做去重。
        :type SessionId: str
        :param SessionContext: 來源上下文，用於透傳用戶請求訊息，任務流狀态變更回調将返回該欄位值，最長1000個字元。
        :type SessionContext: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.EventType = None
        self.WorkflowTaskEvent = None
        self.EditMediaTaskEvent = None
        self.SessionId = None
        self.SessionContext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EventType = params.get("EventType")
        if params.get("WorkflowTaskEvent") is not None:
            self.WorkflowTaskEvent = WorkflowTask()
            self.WorkflowTaskEvent._deserialize(params.get("WorkflowTaskEvent"))
        if params.get("EditMediaTaskEvent") is not None:
            self.EditMediaTaskEvent = EditMediaTask()
            self.EditMediaTaskEvent._deserialize(params.get("EditMediaTaskEvent"))
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")
        self.RequestId = params.get("RequestId")


class PoliticalAsrReviewTemplateInfo(AbstractModel):
    """語音鑒政任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 語音鑒政任務開關，可選值：
<li>ON：開啓語音鑒政任務；</li>
<li>OFF：關閉語音鑒政任務。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌違規的分數阈值，當智慧審核達到該分數以上，認爲涉嫌違規，不填預設爲 100 分。取值範圍：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工複核是否違規的分數阈值，當智慧審核達到該分數以上，認爲需人工複核，不填預設爲 75 分。取值範圍：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class PoliticalAsrReviewTemplateInfoForUpdate(AbstractModel):
    """語音鑒政任務控制參數。

    """

    def __init__(self):
        """
        :param Switch: 語音鑒政任務開關，可選值：
<li>ON：開啓語音鑒政任務；</li>
<li>OFF：關閉語音鑒政任務。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌違規的分數阈值，當智慧審核達到該分數以上，認爲涉嫌違規。取值範圍：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工複核是否違規的分數阈值，當智慧審核達到該分數以上，認爲需人工複核。取值範圍：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class PoliticalConfigureInfo(AbstractModel):
    """鑒政任務控制參數

    """

    def __init__(self):
        """
        :param ImgReviewInfo: 畫面鑒政控制參數。
        :type ImgReviewInfo: :class:`taifucloudcloud.mps.v20190612.models.PoliticalImgReviewTemplateInfo`
        :param AsrReviewInfo: 語音鑒政控制參數。
        :type AsrReviewInfo: :class:`taifucloudcloud.mps.v20190612.models.PoliticalAsrReviewTemplateInfo`
        :param OcrReviewInfo: 文本鑒政控制參數。
        :type OcrReviewInfo: :class:`taifucloudcloud.mps.v20190612.models.PoliticalOcrReviewTemplateInfo`
        """
        self.ImgReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = PoliticalImgReviewTemplateInfo()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = PoliticalAsrReviewTemplateInfo()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = PoliticalOcrReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))


class PoliticalConfigureInfoForUpdate(AbstractModel):
    """鑒政任務控制參數。

    """

    def __init__(self):
        """
        :param ImgReviewInfo: 畫面鑒政控制參數。
        :type ImgReviewInfo: :class:`taifucloudcloud.mps.v20190612.models.PoliticalImgReviewTemplateInfoForUpdate`
        :param AsrReviewInfo: 語音鑒政控制參數。
        :type AsrReviewInfo: :class:`taifucloudcloud.mps.v20190612.models.PoliticalAsrReviewTemplateInfoForUpdate`
        :param OcrReviewInfo: 文本鑒政控制參數。
        :type OcrReviewInfo: :class:`taifucloudcloud.mps.v20190612.models.PoliticalOcrReviewTemplateInfoForUpdate`
        """
        self.ImgReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = PoliticalImgReviewTemplateInfoForUpdate()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = PoliticalAsrReviewTemplateInfoForUpdate()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = PoliticalOcrReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))


class PoliticalImgReviewTemplateInfo(AbstractModel):
    """畫面鑒政任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 畫面鑒政任務開關，可選值：
<li>ON：開啓畫面鑒政任務；</li>
<li>OFF：關閉畫面鑒政任務。</li>
        :type Switch: str
        :param LabelSet: 畫面鑒政過濾標簽，審核結果包含選擇的標簽則返回結果，如果過濾標簽爲空，則審核結果全部返回，可選值爲：
<li>violation_photo：違規圖標；</li>
<li>politician：政治人物；</li>
<li>entertainment：娛樂明星；</li>
<li>sport：體育明星。</li>
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌違規的分數阈值，當智慧審核達到該分數以上，認爲涉嫌違規，不填預設爲 97 分。取值範圍：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工複核是否違規的分數阈值，當智慧審核達到該分數以上，認爲需人工複核，不填預設爲 95 分。取值範圍：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class PoliticalImgReviewTemplateInfoForUpdate(AbstractModel):
    """畫面鑒政任務控制參數。

    """

    def __init__(self):
        """
        :param Switch: 畫面鑒政任務開關，可選值：
<li>ON：開啓畫面鑒政任務；</li>
<li>OFF：關閉畫面鑒政任務。</li>
        :type Switch: str
        :param LabelSet: 畫面鑒政過濾標簽，審核結果包含選擇的標簽則返回結果，如果過濾標簽爲空，則審核結果全部返回，可選值爲：
<li>violation_photo：違規圖標；</li>
<li>politician：政治人物；</li>
<li>entertainment：娛樂明星；</li>
<li>sport：體育明星。</li>
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌違規的分數阈值，當智慧審核達到該分數以上，認爲涉嫌違規。取值範圍：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工複核是否違規的分數阈值，當智慧審核達到該分數以上，認爲需人工複核。取值範圍：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class PoliticalOcrReviewTemplateInfo(AbstractModel):
    """文本鑒政任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 文本鑒政任務開關，可選值：
<li>ON：開啓文本鑒政任務；</li>
<li>OFF：關閉文本鑒政任務。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌違規的分數阈值，當智慧審核達到該分數以上，認爲涉嫌違規，不填預設爲 100 分。取值範圍：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工複核是否違規的分數阈值，當智慧審核達到該分數以上，認爲需人工複核，不填預設爲 75 分。取值範圍：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class PoliticalOcrReviewTemplateInfoForUpdate(AbstractModel):
    """文本鑒政任務控制參數。

    """

    def __init__(self):
        """
        :param Switch: 文本鑒政任務開關，可選值：
<li>ON：開啓文本鑒政任務；</li>
<li>OFF：關閉文本鑒政任務。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌違規的分數阈值，當智慧審核達到該分數以上，認爲涉嫌違規。取值範圍：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工複核是否違規的分數阈值，當智慧審核達到該分數以上，認爲需人工複核。取值範圍：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class PornAsrReviewTemplateInfo(AbstractModel):
    """語音 任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 語音 任務開關，可選值：
<li>ON：開啓語音 任務；</li>
<li>OFF：關閉語音 任務。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌違規的分數阈值，當智慧審核達到該分數以上，認爲涉嫌違規，不填預設爲 100 分。取值範圍：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工複核是否違規的分數阈值，當智慧審核達到該分數以上，認爲需人工複核，不填預設爲 75 分。取值範圍：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class PornAsrReviewTemplateInfoForUpdate(AbstractModel):
    """語音 任務控制參數。

    """

    def __init__(self):
        """
        :param Switch: 語音 任務開關，可選值：
<li>ON：開啓語音 任務；</li>
<li>OFF：關閉語音 任務。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌違規的分數阈值，當智慧審核達到該分數以上，認爲涉嫌違規。取值範圍：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工複核是否違規的分數阈值，當智慧審核達到該分數以上，認爲需人工複核。取值範圍：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class PornConfigureInfo(AbstractModel):
    """ 任務控制參數

    """

    def __init__(self):
        """
        :param ImgReviewInfo: 畫面 控制參數。
        :type ImgReviewInfo: :class:`taifucloudcloud.mps.v20190612.models.PornImgReviewTemplateInfo`
        :param AsrReviewInfo: 語音 控制參數。
        :type AsrReviewInfo: :class:`taifucloudcloud.mps.v20190612.models.PornAsrReviewTemplateInfo`
        :param OcrReviewInfo: 文本 控制參數。
        :type OcrReviewInfo: :class:`taifucloudcloud.mps.v20190612.models.PornOcrReviewTemplateInfo`
        """
        self.ImgReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = PornImgReviewTemplateInfo()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = PornAsrReviewTemplateInfo()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = PornOcrReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))


class PornConfigureInfoForUpdate(AbstractModel):
    """ 任務控制參數。

    """

    def __init__(self):
        """
        :param ImgReviewInfo: 畫面 控制參數。
        :type ImgReviewInfo: :class:`taifucloudcloud.mps.v20190612.models.PornImgReviewTemplateInfoForUpdate`
        :param AsrReviewInfo: 語音 控制參數。
        :type AsrReviewInfo: :class:`taifucloudcloud.mps.v20190612.models.PornAsrReviewTemplateInfoForUpdate`
        :param OcrReviewInfo: 文本 控制參數。
        :type OcrReviewInfo: :class:`taifucloudcloud.mps.v20190612.models.PornOcrReviewTemplateInfoForUpdate`
        """
        self.ImgReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = PornImgReviewTemplateInfoForUpdate()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = PornAsrReviewTemplateInfoForUpdate()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = PornOcrReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))


class PornImgReviewTemplateInfo(AbstractModel):
    """畫面 任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 畫面 任務開關，可選值：
<li>ON：開啓畫面 任務；</li>
<li>OFF：關閉畫面 任務。</li>
        :type Switch: str
        :param LabelSet: 畫面 過濾標簽，審核結果包含選擇的標簽則返回結果，如果過濾標簽爲空，則審核結果全部返回，可選值爲：
<li>porn：色情；</li>
<li>vulgar：低俗；</li>
<li>intimacy：親密行爲；</li>
<li>sexy：性感。</li>
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌違規的分數阈值，當智慧審核達到該分數以上，認爲涉嫌違規，不填預設爲 90 分。取值範圍：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工複核是否違規的分數阈值，當智慧審核達到該分數以上，認爲需人工複核，不填預設爲 0 分。取值範圍：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class PornImgReviewTemplateInfoForUpdate(AbstractModel):
    """畫面 任務控制參數。

    """

    def __init__(self):
        """
        :param Switch: 畫面 任務開關，可選值：
<li>ON：開啓畫面 任務；</li>
<li>OFF：關閉畫面 任務。</li>
        :type Switch: str
        :param LabelSet: 畫面 過濾標簽，審核結果包含選擇的標簽則返回結果，如果過濾標簽爲空，則審核結果全部返回，可選值爲：
<li>porn：色情；</li>
<li>vulgar：低俗；</li>
<li>intimacy：親密行爲；</li>
<li>sexy：性感。</li>
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌違規的分數阈值，當智慧審核達到該分數以上，認爲涉嫌違規。取值範圍：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工複核是否違規的分數阈值，當智慧審核達到該分數以上，認爲需人工複核。取值範圍：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class PornOcrReviewTemplateInfo(AbstractModel):
    """文本 任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 文本 任務開關，可選值：
<li>ON：開啓文本 任務；</li>
<li>OFF：關閉文本 任務。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌違規的分數阈值，當智慧審核達到該分數以上，認爲涉嫌違規，不填預設爲 100 分。取值範圍：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工複核是否違規的分數阈值，當智慧審核達到該分數以上，認爲需人工複核，不填預設爲 75 分。取值範圍：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class PornOcrReviewTemplateInfoForUpdate(AbstractModel):
    """文本 任務控制參數。

    """

    def __init__(self):
        """
        :param Switch: 文本 任務開關，可選值：
<li>ON：開啓文本 任務；</li>
<li>OFF：關閉文本 任務。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌違規的分數阈值，當智慧審核達到該分數以上，認爲涉嫌違規。取值範圍：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工複核是否違規的分數阈值，當智慧審核達到該分數以上，認爲需人工複核。取值範圍：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class ProcessLiveStreamRequest(AbstractModel):
    """ProcessLiveStream請求參數結構體

    """

    def __init__(self):
        """
        :param Url: 直播流 URL（必須是直播文件網址，支援 rtmp，hls 和 flv 等）。
        :type Url: str
        :param TaskNotifyConfig: 任務的事件通知訊息，用於指定直播流處理的結果。
        :type TaskNotifyConfig: :class:`taifucloudcloud.mps.v20190612.models.LiveStreamTaskNotifyConfig`
        :param OutputStorage: 直播流處理輸出文件的目標儲存。如處理有文件輸出，該參數爲必填項。
        :type OutputStorage: :class:`taifucloudcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputDir: 直播流處理生成的文件輸出的目標目錄，如`/movie/201909/`，如果不填爲 `/` 目錄。
        :type OutputDir: str
        :param AiContentReviewTask: 視訊内容審核類型任務參數。
        :type AiContentReviewTask: :class:`taifucloudcloud.mps.v20190612.models.AiContentReviewTaskInput`
        :param AiRecognitionTask: 視訊内容識别類型任務參數。
        :type AiRecognitionTask: :class:`taifucloudcloud.mps.v20190612.models.AiRecognitionTaskInput`
        :param SessionId: 用於去重的識别碼，如果七天内曾有過相同的識别碼的請求，則本次的請求會返回錯誤。最長 50 個字元，不帶或者帶空字串表示不做去重。
        :type SessionId: str
        :param SessionContext: 來源上下文，用於透傳用戶請求訊息，任務流狀态變更回調将返回該欄位值，最長 1000 個字元。
        :type SessionContext: str
        """
        self.Url = None
        self.TaskNotifyConfig = None
        self.OutputStorage = None
        self.OutputDir = None
        self.AiContentReviewTask = None
        self.AiRecognitionTask = None
        self.SessionId = None
        self.SessionContext = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = LiveStreamTaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputDir = params.get("OutputDir")
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")


class ProcessLiveStreamResponse(AbstractModel):
    """ProcessLiveStream返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務 ID
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ProcessMediaRequest(AbstractModel):
    """ProcessMedia請求參數結構體

    """

    def __init__(self):
        """
        :param InputInfo: 視訊處理的文件輸入訊息。
        :type InputInfo: :class:`taifucloudcloud.mps.v20190612.models.MediaInputInfo`
        :param OutputStorage: 視訊處理輸出文件的目標儲存。不填則繼承 InputInfo 中的儲存位置。
        :type OutputStorage: :class:`taifucloudcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputDir: 視訊處理生成的文件輸出的目標目錄，如`/movie/201907/`。如果不填，表示與 InputInfo 中文件所在的目錄一緻。
        :type OutputDir: str
        :param MediaProcessTask: 視訊處理類型任務參數。
        :type MediaProcessTask: :class:`taifucloudcloud.mps.v20190612.models.MediaProcessTaskInput`
        :param AiContentReviewTask: 視訊内容審核類型任務參數。
        :type AiContentReviewTask: :class:`taifucloudcloud.mps.v20190612.models.AiContentReviewTaskInput`
        :param AiAnalysisTask: 視訊内容分析類型任務參數。
        :type AiAnalysisTask: :class:`taifucloudcloud.mps.v20190612.models.AiAnalysisTaskInput`
        :param AiRecognitionTask: 視訊内容識别類型任務參數。
        :type AiRecognitionTask: :class:`taifucloudcloud.mps.v20190612.models.AiRecognitionTaskInput`
        :param TaskNotifyConfig: 任務的事件通知訊息，不填代表不獲取事件通知。
        :type TaskNotifyConfig: :class:`taifucloudcloud.mps.v20190612.models.TaskNotifyConfig`
        :param TasksPriority: 任務流的優先級，數值越大優先級越高，取值範圍是-10到 10，不填代表0。
        :type TasksPriority: int
        :param SessionId: 用於去重的識别碼，如果七天内曾有過相同的識别碼的請求，則本次的請求會返回錯誤。最長 50 個字元，不帶或者帶空字串表示不做去重。
        :type SessionId: str
        :param SessionContext: 來源上下文，用於透傳用戶請求訊息，任務流狀态變更回調将返回該欄位值，最長 1000 個字元。
        :type SessionContext: str
        """
        self.InputInfo = None
        self.OutputStorage = None
        self.OutputDir = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.TaskNotifyConfig = None
        self.TasksPriority = None
        self.SessionId = None
        self.SessionContext = None


    def _deserialize(self, params):
        if params.get("InputInfo") is not None:
            self.InputInfo = MediaInputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputDir = params.get("OutputDir")
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        self.TasksPriority = params.get("TasksPriority")
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")


class ProcessMediaResponse(AbstractModel):
    """ProcessMedia返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務 ID。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ProhibitedAsrReviewTemplateInfo(AbstractModel):
    """語音違禁任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 語音違禁任務開關，可選值：
<li>ON：開啓語音違禁任務；</li>
<li>OFF：關閉語音違禁任務。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌違規的分數阈值，當智慧審核達到該分數以上，認爲涉嫌違規，不填預設爲 100 分。取值範圍：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工複核是否違規的分數阈值，當智慧審核達到該分數以上，認爲需人工複核，不填預設爲 75 分。取值範圍：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class ProhibitedAsrReviewTemplateInfoForUpdate(AbstractModel):
    """語音違禁任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 語音違禁任務開關，可選值：
<li>ON：開啓語音違禁任務；</li>
<li>OFF：關閉語音違禁任務。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌違規的分數阈值，當智慧審核達到該分數以上，認爲涉嫌違規，不填預設爲 100 分。取值範圍：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工複核是否違規的分數阈值，當智慧審核達到該分數以上，認爲需人工複核，不填預設爲 75 分。取值範圍：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class ProhibitedConfigureInfo(AbstractModel):
    """違禁任務控制參數

    """

    def __init__(self):
        """
        :param AsrReviewInfo: 語音違禁控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AsrReviewInfo: :class:`taifucloudcloud.mps.v20190612.models.ProhibitedAsrReviewTemplateInfo`
        :param OcrReviewInfo: 文本違禁控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OcrReviewInfo: :class:`taifucloudcloud.mps.v20190612.models.ProhibitedOcrReviewTemplateInfo`
        """
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = ProhibitedAsrReviewTemplateInfo()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = ProhibitedOcrReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))


class ProhibitedConfigureInfoForUpdate(AbstractModel):
    """違禁任務控制參數

    """

    def __init__(self):
        """
        :param AsrReviewInfo: 語音違禁控制參數。
        :type AsrReviewInfo: :class:`taifucloudcloud.mps.v20190612.models.ProhibitedAsrReviewTemplateInfoForUpdate`
        :param OcrReviewInfo: 文本違禁控制參數。
        :type OcrReviewInfo: :class:`taifucloudcloud.mps.v20190612.models.ProhibitedOcrReviewTemplateInfoForUpdate`
        """
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = ProhibitedAsrReviewTemplateInfoForUpdate()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = ProhibitedOcrReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))


class ProhibitedOcrReviewTemplateInfo(AbstractModel):
    """文本違禁任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 文本違禁任務開關，可選值：
<li>ON：開啓文本違禁任務；</li>
<li>OFF：關閉文本違禁任務。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌違規的分數阈值，當智慧審核達到該分數以上，認爲涉嫌違規，不填預設爲 100 分。取值範圍：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工複核是否違規的分數阈值，當智慧審核達到該分數以上，認爲需人工複核，不填預設爲 75 分。取值範圍：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class ProhibitedOcrReviewTemplateInfoForUpdate(AbstractModel):
    """文本違禁任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 文本違禁任務開關，可選值：
<li>ON：開啓文本違禁任務；</li>
<li>OFF：關閉文本違禁任務。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌違規的分數阈值，當智慧審核達到該分數以上，認爲涉嫌違規，不填預設爲 100 分。取值範圍：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工複核是否違規的分數阈值，當智慧審核達到該分數以上，認爲需人工複核，不填預設爲 75 分。取值範圍：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class RawImageWatermarkInput(AbstractModel):
    """圖片浮水印範本輸入參數

    """

    def __init__(self):
        """
        :param ImageContent: 浮水印圖片的輸入内容。支援 jpeg、png 圖片格式。
        :type ImageContent: :class:`taifucloudcloud.mps.v20190612.models.MediaInputInfo`
        :param Width: 浮水印的寬度。支援 %、px 兩種格式：
<li>當字串以 % 結尾，表示浮水印 Width 爲視訊寬度的百分比大小，如 10% 表示 Width 爲視訊寬度的 10%；</li>
<li>當字串以 px 結尾，表示浮水印 Width 單位爲像素，如 100px 表示 Width 爲 100 像素。</li>
預設值：10%。
        :type Width: str
        :param Height: 浮水印的高度。支援 %、px 兩種格式：
<li>當字串以 % 結尾，表示浮水印 Height 爲視訊高度的百分比大小，如 10% 表示 Height 爲視訊高度的 10%；</li>
<li>當字串以 px 結尾，表示浮水印 Height 單位爲像素，如 100px 表示 Height 爲 100 像素。</li>
預設值：0px，表示 Height 按照原始浮水印圖片的寬高比縮放。
        :type Height: str
        """
        self.ImageContent = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        if params.get("ImageContent") is not None:
            self.ImageContent = MediaInputInfo()
            self.ImageContent._deserialize(params.get("ImageContent"))
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class RawTranscodeParameter(AbstractModel):
    """自定義轉碼的規格參數。

    """

    def __init__(self):
        """
        :param Container: 封裝格式，可選值：mp4、flv、hls、mp3、flac、ogg、m4a。其中，mp3、flac、ogg、m4a 爲純音訊文件。
        :type Container: str
        :param RemoveVideo: 是否去除視訊數據，取值：
<li>0：保留；</li>
<li>1：去除。</li>
預設值：0。
        :type RemoveVideo: int
        :param RemoveAudio: 是否去除音訊數據，取值：
<li>0：保留；</li>
<li>1：去除。</li>
預設值：0。
        :type RemoveAudio: int
        :param VideoTemplate: 視訊流配置參數，當 RemoveVideo 爲 0，該欄位必填。
        :type VideoTemplate: :class:`taifucloudcloud.mps.v20190612.models.VideoTemplateInfo`
        :param AudioTemplate: 音訊流配置參數，當 RemoveAudio 爲 0，該欄位必填。
        :type AudioTemplate: :class:`taifucloudcloud.mps.v20190612.models.AudioTemplateInfo`
        :param TEHDConfig: 極速高清轉碼參數。
        :type TEHDConfig: :class:`taifucloudcloud.mps.v20190612.models.TEHDConfig`
        """
        self.Container = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.TEHDConfig = None


    def _deserialize(self, params):
        self.Container = params.get("Container")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfo()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfo()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfig()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))


class RawWatermarkParameter(AbstractModel):
    """自定義浮水印規格參數。

    """

    def __init__(self):
        """
        :param Type: 浮水印類型，可選值：
<li>image：圖片浮水印。</li>
        :type Type: str
        :param CoordinateOrigin: 原點位置，目前僅支援：
<li>TopLeft：表示坐標原點位於視訊圖像左上角，浮水印原點爲圖片或文字的左上角。</li>
預設值：TopLeft。
        :type CoordinateOrigin: str
        :param XPos: 浮水印原點距離視訊圖像坐標原點的水平位置。支援 %、px 兩種格式：
<li>當字串以 % 結尾，表示浮水印 XPos 爲視訊寬度指定百分比，如 10% 表示 XPos 爲視訊寬度的 10%；</li>
<li>當字串以 px 結尾，表示浮水印 XPos 爲指定像素，如 100px 表示 XPos 爲 100 像素。</li>
預設值：0px。
        :type XPos: str
        :param YPos: 浮水印原點距離視訊圖像坐標原點的垂直位置。支援 %、px 兩種格式：
<li>當字串以 % 結尾，表示浮水印 YPos 爲視訊高度指定百分比，如 10% 表示 YPos 爲視訊高度的 10%；</li>
<li>當字串以 px 結尾，表示浮水印 YPos 爲指定像素，如 100px 表示 YPos 爲 100 像素。</li>
預設值：0px。
        :type YPos: str
        :param ImageTemplate: 圖片浮水印範本，當 Type 爲 image，該欄位必填。當 Type 爲 text，該欄位無效。
        :type ImageTemplate: :class:`taifucloudcloud.mps.v20190612.models.RawImageWatermarkInput`
        """
        self.Type = None
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.ImageTemplate = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        if params.get("ImageTemplate") is not None:
            self.ImageTemplate = RawImageWatermarkInput()
            self.ImageTemplate._deserialize(params.get("ImageTemplate"))


class ResetWorkflowRequest(AbstractModel):
    """ResetWorkflow請求參數結構體

    """

    def __init__(self):
        """
        :param WorkflowId: 工作流 ID。
        :type WorkflowId: int
        :param WorkflowName: 工作流名稱，最多128字元。同一個用戶該名稱唯一。
        :type WorkflowName: str
        :param Trigger: 工作流綁定的觸發規則，當上傳視訊命中該規則到該對象時即觸發工作流。
        :type Trigger: :class:`taifucloudcloud.mps.v20190612.models.WorkflowTrigger`
        :param OutputStorage: 視訊處理的文件輸出配置。不填則繼承 Trigger 中的儲存位置。
        :type OutputStorage: :class:`taifucloudcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputDir: 視訊處理生成的文件輸出的目標目錄，如`/movie/201907/`。如果不填，表示與觸發文件所在的目錄一緻，即`{inputDir}`。
        :type OutputDir: str
        :param MediaProcessTask: 視訊處理類型任務參數。
        :type MediaProcessTask: :class:`taifucloudcloud.mps.v20190612.models.MediaProcessTaskInput`
        :param AiContentReviewTask: 視訊内容審核類型任務參數。
        :type AiContentReviewTask: :class:`taifucloudcloud.mps.v20190612.models.AiContentReviewTaskInput`
        :param AiAnalysisTask: 視訊内容分析類型任務參數。
        :type AiAnalysisTask: :class:`taifucloudcloud.mps.v20190612.models.AiAnalysisTaskInput`
        :param AiRecognitionTask: 視訊内容識别類型任務參數。
        :type AiRecognitionTask: :class:`taifucloudcloud.mps.v20190612.models.AiRecognitionTaskInput`
        :param TaskPriority: 工作流的優先級，數值越大優先級越高，取值範圍是 -10 到 10，不填代表 0。
        :type TaskPriority: int
        :param TaskNotifyConfig: 任務的事件通知訊息，不填代表不獲取事件通知。
        :type TaskNotifyConfig: :class:`taifucloudcloud.mps.v20190612.models.TaskNotifyConfig`
        """
        self.WorkflowId = None
        self.WorkflowName = None
        self.Trigger = None
        self.OutputStorage = None
        self.OutputDir = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.TaskPriority = None
        self.TaskNotifyConfig = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")
        self.WorkflowName = params.get("WorkflowName")
        if params.get("Trigger") is not None:
            self.Trigger = WorkflowTrigger()
            self.Trigger._deserialize(params.get("Trigger"))
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputDir = params.get("OutputDir")
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        self.TaskPriority = params.get("TaskPriority")
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))


class ResetWorkflowResponse(AbstractModel):
    """ResetWorkflow返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SampleSnapshotTaskInput(AbstractModel):
    """對視訊做采樣截圖任務輸入參數類型。

    """

    def __init__(self):
        """
        :param Definition: 采樣截圖範本 ID。
        :type Definition: int
        :param WatermarkSet: 浮水印清單，支援多張圖片或文字水印，最大可支援 10 張。
        :type WatermarkSet: list of WatermarkInput
        :param OutputStorage: 采樣截圖後文件的目標儲存，不填則繼承上層的 OutputStorage 值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OutputStorage: :class:`taifucloudcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputObjectPath: 采樣截圖後圖片文件的輸出路徑，可以爲相對路徑或者絕對路徑。如果不填，則預設爲相對路徑：`{inputName}_sampleSnapshot_{definition}_{number}.{format}`。
        :type OutputObjectPath: str
        :param ObjectNumberFormat: 采樣截圖後輸出路徑中的`{number}`變量的規則。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ObjectNumberFormat: :class:`taifucloudcloud.mps.v20190612.models.NumberFormat`
        """
        self.Definition = None
        self.WatermarkSet = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.ObjectNumberFormat = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        if params.get("ObjectNumberFormat") is not None:
            self.ObjectNumberFormat = NumberFormat()
            self.ObjectNumberFormat._deserialize(params.get("ObjectNumberFormat"))


class SampleSnapshotTemplate(AbstractModel):
    """采樣截圖範本詳情

    """

    def __init__(self):
        """
        :param Definition: 采樣截圖範本唯一標識。
        :type Definition: int
        :param Type: 範本類型，取值範圍：
<li>Preset：系統預置範本；</li>
<li>Custom：用戶自定義範本。</li>
        :type Type: str
        :param Name: 采樣截圖範本名稱。
        :type Name: str
        :param Comment: 範本描述訊息。
        :type Comment: str
        :param Width: 截圖寬度（或長邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
        :type Width: int
        :param Height: 截圖高度（或短邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适應，可選值：
<li>open：開啓，此時，Width 代表視訊的長邊，Height 表示視訊的短邊；</li>
<li>close：關閉，此時，Width 代表視訊的寬度，Height 表示視訊的高度。</li>
預設值：open。
        :type ResolutionAdaptive: str
        :param Format: 圖片格式。
        :type Format: str
        :param SampleType: 采樣截圖類型。
        :type SampleType: str
        :param SampleInterval: 采樣間隔。
        :type SampleInterval: int
        :param CreateTime: 範本創建時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param UpdateTime: 範本最後修改時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type UpdateTime: str
        :param FillType: 填充方式，當視訊流配置寬高參數與原始視訊的寬高比不一緻時，對轉碼的處理方式，即爲“填充”。可選填充方式：
<li> stretch：拉伸，對每一幀進行拉伸，填滿整個畫面，可能導緻轉碼後的視訊被“壓扁“或者“拉長“；</li>
<li>black：留黑，保持視訊寬高比不變，邊緣剩餘部分使用黑色填充。</li>
<li>white：留白，保持視訊寬高比不變，邊緣剩餘部分使用白色填充。</li>
<li>gauss：高斯模糊，保持視訊寬高比不變，邊緣剩餘部分使用高斯模糊。</li>
預設值：black 。
        :type FillType: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.SampleType = None
        self.SampleInterval = None
        self.CreateTime = None
        self.UpdateTime = None
        self.FillType = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.FillType = params.get("FillType")


class SnapshotByTimeOffsetTaskInput(AbstractModel):
    """對視訊按指定時間點截圖任務輸入參數類型

    """

    def __init__(self):
        """
        :param Definition: 指定時間點截圖範本 ID。
        :type Definition: int
        :param TimeOffsetSet: 截圖時間點清單，單位爲<font color=red>秒</font>。
        :type TimeOffsetSet: list of float
        :param WatermarkSet: 浮水印清單，支援多張圖片或文字水印，最大可支援 10 張。
        :type WatermarkSet: list of WatermarkInput
        :param OutputStorage: 時間點截圖後文件的目標儲存，不填則繼承上層的 OutputStorage 值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OutputStorage: :class:`taifucloudcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputObjectPath: 時間點截圖後圖片文件的輸出路徑，可以爲相對路徑或者絕對路徑。如果不填，則預設爲相對路徑：`{inputName}_snapshotByTimeOffset_{definition}_{number}.{format}`。
        :type OutputObjectPath: str
        :param ObjectNumberFormat: 時間點截圖後輸出路徑中的`{number}`變量的規則。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ObjectNumberFormat: :class:`taifucloudcloud.mps.v20190612.models.NumberFormat`
        """
        self.Definition = None
        self.TimeOffsetSet = None
        self.WatermarkSet = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.ObjectNumberFormat = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.TimeOffsetSet = params.get("TimeOffsetSet")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        if params.get("ObjectNumberFormat") is not None:
            self.ObjectNumberFormat = NumberFormat()
            self.ObjectNumberFormat._deserialize(params.get("ObjectNumberFormat"))


class SnapshotByTimeOffsetTemplate(AbstractModel):
    """時間點截圖範本詳情

    """

    def __init__(self):
        """
        :param Definition: 時間點截圖範本唯一標識。
        :type Definition: int
        :param Type: 範本類型，取值範圍：
<li>Preset：系統預置範本；</li>
<li>Custom：用戶自定義範本。</li>
        :type Type: str
        :param Name: 時間點截圖範本名稱。
        :type Name: str
        :param Comment: 範本描述訊息。
        :type Comment: str
        :param Width: 截圖寬度（或長邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
        :type Width: int
        :param Height: 截圖高度（或短邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
        :type Height: int
        :param ResolutionAdaptive: 分辨率自适應，可選值：
<li>open：開啓，此時，Width 代表視訊的長邊，Height 表示視訊的短邊；</li>
<li>close：關閉，此時，Width 代表視訊的寬度，Height 表示視訊的高度。</li>
預設值：open。
        :type ResolutionAdaptive: str
        :param Format: 圖片格式。
        :type Format: str
        :param CreateTime: 範本創建時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param UpdateTime: 範本最後修改時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type UpdateTime: str
        :param FillType: 填充方式，當視訊流配置寬高參數與原始視訊的寬高比不一緻時，對轉碼的處理方式，即爲“填充”。可選填充方式：
<li> stretch：拉伸，對每一幀進行拉伸，填滿整個畫面，可能導緻轉碼後的視訊被“壓扁“或者“拉長“；</li>
<li>black：留黑，保持視訊寬高比不變，邊緣剩餘部分使用黑色填充。</li>
<li>black：留白，保持視訊寬高比不變，邊緣剩餘部分使用白色填充。</li>
<li>black：高斯模糊，保持視訊寬高比不變，邊緣剩餘部分使用高斯模糊。</li>
預設值：black 。
        :type FillType: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.CreateTime = None
        self.UpdateTime = None
        self.FillType = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.FillType = params.get("FillType")


class SvgWatermarkInput(AbstractModel):
    """SVG浮水印範本輸入參數

    """

    def __init__(self):
        """
        :param Width: 浮水印的寬度，支援 px，%，W%，H%，S%，L% 六種格式：
<li>當字串以 px 結尾，表示浮水印 Width 單位爲像素，如 100px 表示 Width 爲 100 像素；當填 0px 且
 Height 不爲 0px 時，表示浮水印的寬度按原始 SVG 圖像等比縮放；當 Width、Height 都填 0px 時，表示水印的寬度取原始 SVG 圖像的寬度；</li>
<li>當字串以 W% 結尾，表示浮水印 Width 爲視訊寬度的百分比大小，如 10W% 表示 Width 爲視訊寬度的 10%；</li>
<li>當字串以 H% 結尾，表示浮水印 Width 爲視訊高度的百分比大小，如 10H% 表示 Width 爲視訊高度的 10%；</li>
<li>當字串以 S% 結尾，表示浮水印 Width 爲視訊短邊的百分比大小，如 10S% 表示 Width 爲視訊短邊的 10%；</li>
<li>當字串以 L% 結尾，表示浮水印 Width 爲視訊長邊的百分比大小，如 10L% 表示 Width 爲視訊長邊的 10%；</li>
<li>當字串以 % 結尾時，含義同 W%。</li>
預設值爲 10W%。
        :type Width: str
        :param Height: 浮水印的高度，支援 px，W%，H%，S%，L% 六種格式：
<li>當字串以 px 結尾，表示浮水印 Height 單位爲像素，如 100px 表示 Height 爲 100 像素；當填 0px 且
 Width 不爲 0px 時，表示浮水印的高度按原始 SVG 圖像等比縮放；當 Width、Height 都填 0px 時，表示水印的高度取原始 SVG 圖像的高度；</li>
<li>當字串以 W% 結尾，表示浮水印 Height 爲視訊寬度的百分比大小，如 10W% 表示 Height 爲視訊寬度的 10%；</li>
<li>當字串以 H% 結尾，表示浮水印 Height 爲視訊高度的百分比大小，如 10H% 表示 Height 爲視訊高度的 10%；</li>
<li>當字串以 S% 結尾，表示浮水印 Height 爲視訊短邊的百分比大小，如 10S% 表示 Height 爲視訊短邊的 10%；</li>
<li>當字串以 L% 結尾，表示浮水印 Height 爲視訊長邊的百分比大小，如 10L% 表示 Height 爲視訊長邊的 10%；</li>
<li>當字串以 % 結尾時，含義同 H%。</li>
預設值爲 0px。
        :type Height: str
        """
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class SvgWatermarkInputForUpdate(AbstractModel):
    """SVG浮水印範本輸入參數

    """

    def __init__(self):
        """
        :param Width: 浮水印的寬度，支援 px，%，W%，H%，S%，L% 六種格式：
<li>當字串以 px 結尾，表示浮水印 Width 單位爲像素，如 100px 表示 Width 爲 100 像素；當填 0px 且
 Height 不爲 0px 時，表示浮水印的寬度按原始 SVG 圖像等比縮放；當 Width、Height 都填 0px 時，表示水印的寬度取原始 SVG 圖像的寬度；</li>
<li>當字串以 W% 結尾，表示浮水印 Width 爲視訊寬度的百分比大小，如 10W% 表示 Width 爲視訊寬度的 10%；</li>
<li>當字串以 H% 結尾，表示浮水印 Width 爲視訊高度的百分比大小，如 10H% 表示 Width 爲視訊高度的 10%；</li>
<li>當字串以 S% 結尾，表示浮水印 Width 爲視訊短邊的百分比大小，如 10S% 表示 Width 爲視訊短邊的 10%；</li>
<li>當字串以 L% 結尾，表示浮水印 Width 爲視訊長邊的百分比大小，如 10L% 表示 Width 爲視訊長邊的 10%；</li>
<li>當字串以 % 結尾時，含義同 W%。</li>
預設值爲 10W%。
        :type Width: str
        :param Height: 浮水印的高度，支援 px，%，W%，H%，S%，L% 六種格式：
<li>當字串以 px 結尾，表示浮水印 Height 單位爲像素，如 100px 表示 Height 爲 100 像素；當填 0px 且
 Width 不爲 0px 時，表示浮水印的高度按原始 SVG 圖像等比縮放；當 Width、Height 都填 0px 時，表示水印的高度取原始 SVG 圖像的高度；</li>
<li>當字串以 W% 結尾，表示浮水印 Height 爲視訊寬度的百分比大小，如 10W% 表示 Height 爲視訊寬度的 10%；</li>
<li>當字串以 H% 結尾，表示浮水印 Height 爲視訊高度的百分比大小，如 10H% 表示 Height 爲視訊高度的 10%；</li>
<li>當字串以 S% 結尾，表示浮水印 Height 爲視訊短邊的百分比大小，如 10S% 表示 Height 爲視訊短邊的 10%；</li>
<li>當字串以 L% 結尾，表示浮水印 Height 爲視訊長邊的百分比大小，如 10L% 表示 Height 爲視訊長邊的 10%；</li>
<li>當字串以 % 結尾時，含義同 H%。
預設值爲 0px。
        :type Height: str
        """
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class TEHDConfig(AbstractModel):
    """極速高清參數配置。

    """

    def __init__(self):
        """
        :param Type: 極速高清類型，可選值：
<li>TEHD-100：極速高清-100。</li>
不填代表不啓用極速高清。
        :type Type: str
        :param MaxVideoBitrate: 視訊碼率上限，當 Type 指定了極速高清類型時有效。
不填或填0表示不設視訊碼率上限。
        :type MaxVideoBitrate: int
        """
        self.Type = None
        self.MaxVideoBitrate = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.MaxVideoBitrate = params.get("MaxVideoBitrate")


class TEHDConfigForUpdate(AbstractModel):
    """極速高清參數配置。

    """

    def __init__(self):
        """
        :param Type: 極速高清類型，可選值：
<li>TEHD-100：極速高清-100。</li>
不填代表不修改。
        :type Type: str
        :param MaxVideoBitrate: 視訊碼率上限，不填代表不修改。
        :type MaxVideoBitrate: int
        """
        self.Type = None
        self.MaxVideoBitrate = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.MaxVideoBitrate = params.get("MaxVideoBitrate")


class TagConfigureInfo(AbstractModel):
    """智慧標簽任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 智慧標簽任務開關，可選值：
<li>ON：開啓智慧標簽任務；</li>
<li>OFF：關閉智慧標簽任務。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class TagConfigureInfoForUpdate(AbstractModel):
    """智慧標簽任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 智慧標簽任務開關，可選值：
<li>ON：開啓智慧標簽任務；</li>
<li>OFF：關閉智慧標簽任務。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class TaskNotifyConfig(AbstractModel):
    """任務的事件通知配置。

    """

    def __init__(self):
        """
        :param CmqModel: CMQ 的模型，有 Queue 和 Topic 兩種，目前僅支援 Queue。
        :type CmqModel: str
        :param CmqRegion: CMQ 的園區，如 sh，bj 等。
        :type CmqRegion: str
        :param QueueName: 當模型爲 Queue 時有效，表示接收事件通知的 CMQ 的隊列名。
        :type QueueName: str
        :param TopicName: 當模型爲 Topic 時有效，表示接收事件通知的 CMQ 的主題名。
        :type TopicName: str
        :param NotifyMode: 工作流通知的模式，可取值有 Finish 和 Change，不填代表 Finish。
        :type NotifyMode: str
        """
        self.CmqModel = None
        self.CmqRegion = None
        self.QueueName = None
        self.TopicName = None
        self.NotifyMode = None


    def _deserialize(self, params):
        self.CmqModel = params.get("CmqModel")
        self.CmqRegion = params.get("CmqRegion")
        self.QueueName = params.get("QueueName")
        self.TopicName = params.get("TopicName")
        self.NotifyMode = params.get("NotifyMode")


class TaskOutputStorage(AbstractModel):
    """視訊處理輸出對象訊息。

    """

    def __init__(self):
        """
        :param Type: 視訊處理輸出物件儲存位置的類型，現在僅支援 COS。
        :type Type: str
        :param CosOutputStorage: 當 Type 爲 COS 時有效，則該項爲必填，表示視訊處理 COS 輸出位置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CosOutputStorage: :class:`taifucloudcloud.mps.v20190612.models.CosOutputStorage`
        """
        self.Type = None
        self.CosOutputStorage = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("CosOutputStorage") is not None:
            self.CosOutputStorage = CosOutputStorage()
            self.CosOutputStorage._deserialize(params.get("CosOutputStorage"))


class TaskSimpleInfo(AbstractModel):
    """任務概要訊息

    """

    def __init__(self):
        """
        :param TaskId: 任務 ID。
        :type TaskId: str
        :param TaskType: 任務類型，包含：
<li> WorkflowTask：工作流處理任務；</li>
<li> EditMediaTask：視訊編輯任務；</li>
<li> LiveProcessTask：直播處理任務。</li>
        :type TaskType: str
        :param CreateTime: 任務創建時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param BeginProcessTime: 任務開始執行時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。若任務尚未開始，該欄位爲：0000-00-00T00:00:00Z。
        :type BeginProcessTime: str
        :param FinishTime: 任務結束時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。若任務尚未完成，該欄位爲：0000-00-00T00:00:00Z。
        :type FinishTime: str
        """
        self.TaskId = None
        self.TaskType = None
        self.CreateTime = None
        self.BeginProcessTime = None
        self.FinishTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskType = params.get("TaskType")
        self.CreateTime = params.get("CreateTime")
        self.BeginProcessTime = params.get("BeginProcessTime")
        self.FinishTime = params.get("FinishTime")


class TerrorismConfigureInfo(AbstractModel):
    """鑒恐任務控制參數

    """

    def __init__(self):
        """
        :param ImgReviewInfo: 畫面鑒恐任務控制參數。
        :type ImgReviewInfo: :class:`taifucloudcloud.mps.v20190612.models.TerrorismImgReviewTemplateInfo`
        :param OcrReviewInfo: 文本鑒恐任務控制參數。
        :type OcrReviewInfo: :class:`taifucloudcloud.mps.v20190612.models.TerrorismOcrReviewTemplateInfo`
        """
        self.ImgReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = TerrorismImgReviewTemplateInfo()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = TerrorismOcrReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))


class TerrorismConfigureInfoForUpdate(AbstractModel):
    """鑒恐任務控制參數。

    """

    def __init__(self):
        """
        :param ImgReviewInfo: 畫面鑒恐任務控制參數。
        :type ImgReviewInfo: :class:`taifucloudcloud.mps.v20190612.models.TerrorismImgReviewTemplateInfoForUpdate`
        :param OcrReviewInfo: 文本鑒恐任務控制參數。
        :type OcrReviewInfo: :class:`taifucloudcloud.mps.v20190612.models.TerrorismOcrReviewTemplateInfoForUpdate`
        """
        self.ImgReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = TerrorismImgReviewTemplateInfoForUpdate()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = TerrorismOcrReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))


class TerrorismImgReviewTemplateInfo(AbstractModel):
    """畫面鑒恐任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 畫面鑒恐任務開關，可選值：
<li>ON：開啓畫面鑒恐任務；</li>
<li>OFF：關閉畫面鑒恐任務。</li>
        :type Switch: str
        :param LabelSet: 畫面鑒恐過濾標簽，審核結果包含選擇的標簽則返回結果，如果過濾標簽爲空，則審核結果全部返回，可選值爲：
<li>guns：武器槍支；</li>
<li>crowd：人群聚集；</li>
<li>bloody：血腥畫面；</li>
<li>police：警察部隊；</li>
<li>banners：暴恐旗幟；</li>
<li>militant：武裝分子；</li>
<li>explosion：爆炸火災；</li>
<li>terrorists：暴恐人物。</li>
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌違規的分數阈值，當智慧審核達到該分數以上，認爲涉嫌違規，不填預設爲 90 分。取值範圍：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工複核是否違規的分數阈值，當智慧審核達到該分數以上，認爲需人工複核，不填預設爲 80 分。取值範圍：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class TerrorismImgReviewTemplateInfoForUpdate(AbstractModel):
    """畫面鑒恐任務控制參數。

    """

    def __init__(self):
        """
        :param Switch: 畫面鑒恐任務開關，可選值：
<li>ON：開啓畫面鑒恐任務；</li>
<li>OFF：關閉畫面鑒恐任務。</li>
        :type Switch: str
        :param LabelSet: 畫面鑒恐過濾標簽，審核結果包含選擇的標簽則返回結果，如果過濾標簽爲空，則審核結果全部返回，可選值爲：
<li>guns：武器槍支；</li>
<li>crowd：人群聚集；</li>
<li>bloody：血腥畫面；</li>
<li>police：警察部隊；</li>
<li>banners：暴恐旗幟；</li>
<li>militant：武裝分子；</li>
<li>explosion：爆炸火災；</li>
<li>terrorists：暴恐人物。</li>
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌違規的分數阈值，當智慧審核達到該分數以上，認爲涉嫌違規。取值範圍：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工複核是否違規的分數阈值，當智慧審核達到該分數以上，認爲需人工複核。取值範圍：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class TerrorismOcrReviewTemplateInfo(AbstractModel):
    """文本鑒恐任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 文本鑒恐任務開關，可選值：
<li>ON：開啓文本鑒恐任務；</li>
<li>OFF：關閉文本鑒恐任務。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌違規的分數阈值，當智慧審核達到該分數以上，認爲涉嫌違規，不填預設爲 100 分。取值範圍：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工複核是否違規的分數阈值，當智慧審核達到該分數以上，認爲需人工複核，不填預設爲 75 分。取值範圍：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class TerrorismOcrReviewTemplateInfoForUpdate(AbstractModel):
    """文本鑒恐任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 文本鑒恐任務開關，可選值：
<li>ON：開啓文本鑒恐任務；</li>
<li>OFF：關閉文本鑒恐任務。</li>
        :type Switch: str
        :param BlockConfidence: 判定涉嫌違規的分數阈值，當智慧審核達到該分數以上，認爲涉嫌違規，不填預設爲 100 分。取值範圍：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工複核是否違規的分數阈值，當智慧審核達到該分數以上，認爲需人工複核，不填預設爲 75 分。取值範圍：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class TextWatermarkTemplateInput(AbstractModel):
    """文字浮水印範本

    """

    def __init__(self):
        """
        :param FontType: 字體類型，目前可以支援兩種：
<li>simkai.ttf：可以支援中文和英文；</li>
<li>arial.ttf：僅支援英文。</li>
        :type FontType: str
        :param FontSize: 字體大小，格式：Npx，N 爲數值。
        :type FontSize: str
        :param FontColor: 字體顔色，格式：0xRRGGBB，預設值：0xFFFFFF（白色）。
        :type FontColor: str
        :param FontAlpha: 文字透明度，取值範圍：(0, 1]
<li>0：完全透明</li>
<li>1：完全不透明</li>
預設值：1。
        :type FontAlpha: float
        """
        self.FontType = None
        self.FontSize = None
        self.FontColor = None
        self.FontAlpha = None


    def _deserialize(self, params):
        self.FontType = params.get("FontType")
        self.FontSize = params.get("FontSize")
        self.FontColor = params.get("FontColor")
        self.FontAlpha = params.get("FontAlpha")


class TextWatermarkTemplateInputForUpdate(AbstractModel):
    """文字浮水印範本

    """

    def __init__(self):
        """
        :param FontType: 字體類型，目前可以支援兩種：
<li>simkai.ttf：可以支援中文和英文；</li>
<li>arial.ttf：僅支援英文。</li>
        :type FontType: str
        :param FontSize: 字體大小，格式：Npx，N 爲數值。
        :type FontSize: str
        :param FontColor: 字體顔色，格式：0xRRGGBB，預設值：0xFFFFFF（白色）。
        :type FontColor: str
        :param FontAlpha: 文字透明度，取值範圍：(0, 1]
<li>0：完全透明</li>
<li>1：完全不透明</li>
        :type FontAlpha: float
        """
        self.FontType = None
        self.FontSize = None
        self.FontColor = None
        self.FontAlpha = None


    def _deserialize(self, params):
        self.FontType = params.get("FontType")
        self.FontSize = params.get("FontSize")
        self.FontColor = params.get("FontColor")
        self.FontAlpha = params.get("FontAlpha")


class TranscodeTaskInput(AbstractModel):
    """轉碼任務輸入參數類型

    """

    def __init__(self):
        """
        :param Definition: 視訊轉碼範本 ID。
        :type Definition: int
        :param RawParameter: 視訊轉碼自定義參數，當 Definition 填 0 時有效。
該參數用於高度定制場景，建議您優先使用 Definition 指定轉碼參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RawParameter: :class:`taifucloudcloud.mps.v20190612.models.RawTranscodeParameter`
        :param WatermarkSet: 浮水印清單，支援多張圖片或文字水印，最大可支援 10 張。
注意：此欄位可能返回 null，表示取不到有效值。
        :type WatermarkSet: list of WatermarkInput
        :param OutputStorage: 轉碼後文件的目標儲存，不填則繼承上層的 OutputStorage 值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OutputStorage: :class:`taifucloudcloud.mps.v20190612.models.TaskOutputStorage`
        :param OutputObjectPath: 轉碼後主文件的輸出路徑，可以爲相對路徑或者絕對路徑。如果不填，則預設爲相對路徑：`{inputName}_transcode_{definition}.{format}`。
        :type OutputObjectPath: str
        :param SegmentObjectName: 轉碼後分片文件的輸出路徑（轉碼 HLS 時 ts 的路徑），只能爲相對路徑。如果不填，則預設爲：`{inputName}_transcode_{definition}_{number}.{format}`。
        :type SegmentObjectName: str
        :param ObjectNumberFormat: 轉碼後輸出路徑中的`{number}`變量的規則。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ObjectNumberFormat: :class:`taifucloudcloud.mps.v20190612.models.NumberFormat`
        """
        self.Definition = None
        self.RawParameter = None
        self.WatermarkSet = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.SegmentObjectName = None
        self.ObjectNumberFormat = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("RawParameter") is not None:
            self.RawParameter = RawTranscodeParameter()
            self.RawParameter._deserialize(params.get("RawParameter"))
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        self.SegmentObjectName = params.get("SegmentObjectName")
        if params.get("ObjectNumberFormat") is not None:
            self.ObjectNumberFormat = NumberFormat()
            self.ObjectNumberFormat._deserialize(params.get("ObjectNumberFormat"))


class TranscodeTemplate(AbstractModel):
    """轉碼範本詳情

    """

    def __init__(self):
        """
        :param Definition: 轉碼範本唯一標識。
        :type Definition: str
        :param Container: 封裝格式，取值：mp4、flv、hls、mp3、flac、ogg。
        :type Container: str
        :param Name: 轉碼範本名稱。
        :type Name: str
        :param Comment: 範本描述訊息。
        :type Comment: str
        :param Type: 範本類型，取值：
<li>Preset：系統預置範本；</li>
<li>Custom：用戶自定義範本。</li>
        :type Type: str
        :param RemoveVideo: 是否去除視訊數據，取值：
<li>0：保留；</li>
<li>1：去除。</li>
        :type RemoveVideo: int
        :param RemoveAudio: 是否去除音訊數據，取值：
<li>0：保留；</li>
<li>1：去除。</li>
        :type RemoveAudio: int
        :param VideoTemplate: 視訊流配置參數，僅當 RemoveVideo 爲 0，該欄位有效。
        :type VideoTemplate: :class:`taifucloudcloud.mps.v20190612.models.VideoTemplateInfo`
        :param AudioTemplate: 音訊流配置參數，僅當 RemoveAudio 爲 0，該欄位有效 。
        :type AudioTemplate: :class:`taifucloudcloud.mps.v20190612.models.AudioTemplateInfo`
        :param TEHDConfig: 極速高清轉碼參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TEHDConfig: :class:`taifucloudcloud.mps.v20190612.models.TEHDConfig`
        :param ContainerType: 封裝格式過濾條件，可選值：
<li>Video：視訊格式，可以同時包含視訊流和音訊流的封裝格式；</li>
<li>PureAudio：純音訊格式，只能包含音訊流的封裝格式板。</li>
        :type ContainerType: str
        :param CreateTime: 範本創建時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param UpdateTime: 範本最後修改時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type UpdateTime: str
        """
        self.Definition = None
        self.Container = None
        self.Name = None
        self.Comment = None
        self.Type = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.TEHDConfig = None
        self.ContainerType = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Container = params.get("Container")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Type = params.get("Type")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfo()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfo()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfig()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))
        self.ContainerType = params.get("ContainerType")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class UserDefineAsrTextReviewTemplateInfo(AbstractModel):
    """用戶自定義語音審核任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 用戶自定語音審核任務開關，可選值：
<li>ON：開啓自定義語音審核任務；</li>
<li>OFF：關閉自定義語音審核任務。</li>
        :type Switch: str
        :param LabelSet: 用戶自定義語音過濾標簽，審核結果包含選擇的標簽則返回結果，如果過濾標簽爲空，則審核結果全部返回。如果要使用標簽過濾功能，添加自定義語音關鍵詞素材時需要添加對應標簽。
標簽個數最多 10 個，每個標簽長度最多 16 個字元。
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌違規的分數阈值，當智慧審核達到該分數以上，認爲涉嫌違規，不填預設爲 100 分。取值範圍：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工複核是否違規的分數阈值，當智慧審核達到該分數以上，認爲需人工複核，不填預設爲 75 分。取值範圍：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class UserDefineAsrTextReviewTemplateInfoForUpdate(AbstractModel):
    """用戶自定義語音審核任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 用戶自定語音審核任務開關，可選值：
<li>ON：開啓自定義語音審核任務；</li>
<li>OFF：關閉自定義語音審核任務。</li>
        :type Switch: str
        :param LabelSet: 用戶自定義語音過濾標簽，審核結果包含選擇的標簽則返回結果，如果過濾標簽爲空，則審核結果全部返回。如果要使用標簽過濾功能，添加自定義語音關鍵詞素材時需要添加對應標簽。
標簽個數最多 10 個，每個標簽長度最多 16 個字元。
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌違規的分數阈值，當智慧審核達到該分數以上，認爲涉嫌違規。取值範圍：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工複核是否違規的分數阈值，當智慧審核達到該分數以上，認爲需人工複核。取值範圍：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class UserDefineConfigureInfo(AbstractModel):
    """用戶自定義審核任務控制參數

    """

    def __init__(self):
        """
        :param FaceReviewInfo: 用戶自定義人物審核控制參數。
        :type FaceReviewInfo: :class:`taifucloudcloud.mps.v20190612.models.UserDefineFaceReviewTemplateInfo`
        :param AsrReviewInfo: 用戶自定義語音審核控制參數。
        :type AsrReviewInfo: :class:`taifucloudcloud.mps.v20190612.models.UserDefineAsrTextReviewTemplateInfo`
        :param OcrReviewInfo: 用戶自定義文本審核控制參數。
        :type OcrReviewInfo: :class:`taifucloudcloud.mps.v20190612.models.UserDefineOcrTextReviewTemplateInfo`
        """
        self.FaceReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("FaceReviewInfo") is not None:
            self.FaceReviewInfo = UserDefineFaceReviewTemplateInfo()
            self.FaceReviewInfo._deserialize(params.get("FaceReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = UserDefineAsrTextReviewTemplateInfo()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = UserDefineOcrTextReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))


class UserDefineConfigureInfoForUpdate(AbstractModel):
    """用戶自定義審核任務控制參數。

    """

    def __init__(self):
        """
        :param FaceReviewInfo: 用戶自定義人物審核控制參數。
        :type FaceReviewInfo: :class:`taifucloudcloud.mps.v20190612.models.UserDefineFaceReviewTemplateInfoForUpdate`
        :param AsrReviewInfo: 用戶自定義語音審核控制參數。
        :type AsrReviewInfo: :class:`taifucloudcloud.mps.v20190612.models.UserDefineAsrTextReviewTemplateInfoForUpdate`
        :param OcrReviewInfo: 用戶自定義文本審核控制參數。
        :type OcrReviewInfo: :class:`taifucloudcloud.mps.v20190612.models.UserDefineOcrTextReviewTemplateInfoForUpdate`
        """
        self.FaceReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("FaceReviewInfo") is not None:
            self.FaceReviewInfo = UserDefineFaceReviewTemplateInfoForUpdate()
            self.FaceReviewInfo._deserialize(params.get("FaceReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = UserDefineAsrTextReviewTemplateInfoForUpdate()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = UserDefineOcrTextReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))


class UserDefineFaceReviewTemplateInfo(AbstractModel):
    """用戶自定義人物審核任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 用戶自定義人物審核任務開關，可選值：
<li>ON：開啓自定義人物審核任務；</li>
<li>OFF：關閉自定義人物審核任務。</li>
        :type Switch: str
        :param LabelSet: 用戶自定義人物過濾標簽，審核結果包含選擇的標簽則返回結果，如果過濾標簽爲空，則審核結果全部返回。如果要使用標簽過濾功能，添加自定義人物庫的時，需要添加對應人物標簽。
標簽個數最多 10 個，每個標簽長度最多 16 個字元。
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌違規的分數阈值，當智慧審核達到該分數以上，認爲涉嫌違規，不填預設爲 97 分。取值範圍：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工複核是否違規的分數阈值，當智慧審核達到該分數以上，認爲需人工複核，不填預設爲 95 分。取值範圍：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class UserDefineFaceReviewTemplateInfoForUpdate(AbstractModel):
    """用戶自定義人物審核任務控制參數。

    """

    def __init__(self):
        """
        :param Switch: 用戶自定義人物審核任務開關，可選值：
<li>ON：開啓自定義人物審核任務；</li>
<li>OFF：關閉自定義人物審核任務。</li>
        :type Switch: str
        :param LabelSet: 用戶自定義人物過濾標簽，審核結果包含選擇的標簽則返回結果，如果過濾標簽爲空，則審核結果全部返回。如果要使用標簽過濾功能，添加自定義人物庫的時，需要添加對應人物標簽。
標簽個數最多 10 個，每個標簽長度最多 16 個字元。
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌違規的分數阈值，當智慧審核達到該分數以上，認爲涉嫌違規。取值範圍：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工複核是否違規的分數阈值，當智慧審核達到該分數以上，認爲需人工複核。取值範圍：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class UserDefineOcrTextReviewTemplateInfo(AbstractModel):
    """用戶自定義文本審核任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 用戶自定文本審核任務開關，可選值：
<li>ON：開啓自定義文本審核任務；</li>
<li>OFF：關閉自定義文本審核任務。</li>
        :type Switch: str
        :param LabelSet: 用戶自定義文本過濾標簽，審核結果包含選擇的標簽則返回結果，如果過濾標簽爲空，則審核結果全部返回。如果要使用標簽過濾功能，添加自定義文本關鍵詞素材時需要添加對應標簽。
標簽個數最多 10 個，每個標簽長度最多 16 個字元。
        :type LabelSet: list of str
        :param BlockConfidence: 判定涉嫌違規的分數阈值，當智慧審核達到該分數以上，認爲涉嫌違規，不填預設爲 100 分。取值範圍：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工複核是否違規的分數阈值，當智慧審核達到該分數以上，認爲需人工複核，不填預設爲 75 分。取值範圍：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class UserDefineOcrTextReviewTemplateInfoForUpdate(AbstractModel):
    """用戶自定義文本審核任務控制參數。

    """

    def __init__(self):
        """
        :param Switch: 用戶自定文本審核任務開關，可選值：
<li>ON：開啓自定義文本審核任務；</li>
<li>OFF：關閉自定義文本審核任務。</li>
        :type Switch: str
        :param LabelSet: 用戶自定義文本過濾標簽，審核結果包含選擇的標簽則返回結果，如果過濾標簽爲空，則審核結果全部返回。如果要使用標簽過濾功能，添加自定義文本關鍵詞素材時需要添加對應標簽。
標簽個數最多 10 個，每個標簽長度最多 16 個字元。
        :type LabelSet: str
        :param BlockConfidence: 判定涉嫌違規的分數阈值，當智慧審核達到該分數以上，認爲涉嫌違規。取值範圍：0~100。
        :type BlockConfidence: int
        :param ReviewConfidence: 判定需人工複核是否違規的分數阈值，當智慧審核達到該分數以上，認爲需人工複核。取值範圍：0~100。
        :type ReviewConfidence: int
        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")


class VideoTemplateInfo(AbstractModel):
    """視訊流配置參數

    """

    def __init__(self):
        """
        :param Codec: 視訊流的編碼格式，可選值：
<li>libx264：H.264 編碼</li>
<li>libx265：H.265 編碼</li>
<li>av1：AOMedia Video 1 編碼</li>
目前 H.265 編碼必須指定分辨率，並且需要在 640*480 以内。av1 編碼容器目前只支援 mp4 。
        :type Codec: str
        :param Fps: 視訊幀率，取值範圍：[0, 60]，單位：Hz。
當取值爲 0，表示幀率和原始視訊保持一緻。
        :type Fps: int
        :param Bitrate: 視訊流的碼率，取值範圍：0 和 [128, 35000]，單位：kbps。
當取值爲 0，表示視訊碼率和原始視訊保持一緻。
        :type Bitrate: int
        :param ResolutionAdaptive: 分辨率自适應，可選值：
<li>open：開啓，此時，Width 代表視訊的長邊，Height 表示視訊的短邊；</li>
<li>close：關閉，此時，Width 代表視訊的寬度，Height 表示視訊的高度。</li>
預設值：open。
        :type ResolutionAdaptive: str
        :param Width: 視訊流寬度（或長邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
        :type Width: int
        :param Height: 視訊流高度（或短邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
        :type Height: int
        :param Gop: 關鍵幀 I 幀之間的間隔，取值範圍：0 和 [1, 100000]，單位：幀數。
當填 0 或不填時，系統将自動設置 gop 長度。
        :type Gop: int
        :param FillType: 填充方式，當視訊流配置寬高參數與原始視訊的寬高比不一緻時，對轉碼的處理方式，即爲“填充”。可選填充方式：
<li> stretch：拉伸，對每一幀進行拉伸，填滿整個畫面，可能導緻轉碼後的視訊被“壓扁“或者“拉長“；</li>
<li>black：留黑，保持視訊寬高比不變，邊緣剩餘部分使用黑色填充。</li>
預設值：black 。
        :type FillType: str
        """
        self.Codec = None
        self.Fps = None
        self.Bitrate = None
        self.ResolutionAdaptive = None
        self.Width = None
        self.Height = None
        self.Gop = None
        self.FillType = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        self.Bitrate = params.get("Bitrate")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Gop = params.get("Gop")
        self.FillType = params.get("FillType")


class VideoTemplateInfoForUpdate(AbstractModel):
    """視訊流配置參數

    """

    def __init__(self):
        """
        :param Codec: 視訊流的編碼格式，可選值：
<li>libx264：H.264 編碼</li>
<li>libx265：H.265 編碼</li>
<li>av1：AOMedia Video 1 編碼</li>
目前 H.265 編碼必須指定分辨率，並且需要在 640*480 以内。av1 編碼容器目前只支援 mp4 。
        :type Codec: str
        :param Fps: 視訊幀率，取值範圍：[0, 60]，單位：Hz。
當取值爲 0，表示幀率和原始視訊保持一緻。
        :type Fps: int
        :param Bitrate: 視訊流的碼率，取值範圍：0 和 [128, 35000]，單位：kbps。
當取值爲 0，表示視訊碼率和原始視訊保持一緻。
        :type Bitrate: int
        :param ResolutionAdaptive: 分辨率自适應，可選值：
<li>open：開啓，此時，Width 代表視訊的長邊，Height 表示視訊的短邊；</li>
<li>close：關閉，此時，Width 代表視訊的寬度，Height 表示視訊的高度。</li>
        :type ResolutionAdaptive: str
        :param Width: 視訊流寬度（或長邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
        :type Width: int
        :param Height: 視訊流高度（或短邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
        :type Height: int
        :param Gop: 關鍵幀 I 幀之間的間隔，取值範圍：0 和 [1, 100000]，單位：幀數。當填 0 時，系統将自動設置 gop 長度。
        :type Gop: int
        :param FillType: 填充方式，當視訊流配置寬高參數與原始視訊的寬高比不一緻時，對轉碼的處理方式，即爲“填充”。可選填充方式：
<li> stretch：拉伸，對每一幀進行拉伸，填滿整個畫面，可能導緻轉碼後的視訊被“壓扁“或者“拉長“；</li>
<li>black：留黑，保持視訊寬高比不變，邊緣剩餘部分使用黑色填充。</li>
        :type FillType: str
        """
        self.Codec = None
        self.Fps = None
        self.Bitrate = None
        self.ResolutionAdaptive = None
        self.Width = None
        self.Height = None
        self.Gop = None
        self.FillType = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        self.Bitrate = params.get("Bitrate")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Gop = params.get("Gop")
        self.FillType = params.get("FillType")


class WatermarkInput(AbstractModel):
    """視訊處理任務中的浮水印參數類型

    """

    def __init__(self):
        """
        :param Definition: 浮水印範本 ID。
        :type Definition: int
        :param RawParameter: 浮水印自定義參數，當 Definition 填 0 時有效。
該參數用於高度定制場景，建議您優先使用 Definition 指定浮水印參數。
        :type RawParameter: :class:`taifucloudcloud.mps.v20190612.models.RawWatermarkParameter`
        :param TextContent: 文字内容，長度不超過100個字元。僅當浮水印類型爲文字水印時填寫。
        :type TextContent: str
        :param SvgContent: SVG 内容。長度不超過 2000000 個字元。僅當浮水印類型爲 SVG 水印時填寫。
        :type SvgContent: str
        :param StartTimeOffset: 浮水印的起始時間偏移，單位：秒。不填或填0，表示水印從畫面出現時開始顯現。
<li>不填或填0，表示浮水印從畫面開始就出現；</li>
<li>當數值大於0時（假設爲 n），表示浮水印從畫面開始的第 n 秒出現；</li>
<li>當數值小於0時（假設爲 -n），表示浮水印從離畫面結束 n 秒前開始出現。</li>
        :type StartTimeOffset: float
        :param EndTimeOffset: 浮水印的結束時間偏移，單位：秒。
<li>不填或填0，表示浮水印持續到畫面結束；</li>
<li>當數值大於0時（假設爲 n），表示浮水印持續到第 n 秒時消失；</li>
<li>當數值小於0時（假設爲 -n），表示浮水印持續到離畫面結束 n 秒前消失。</li>
        :type EndTimeOffset: float
        """
        self.Definition = None
        self.RawParameter = None
        self.TextContent = None
        self.SvgContent = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("RawParameter") is not None:
            self.RawParameter = RawWatermarkParameter()
            self.RawParameter._deserialize(params.get("RawParameter"))
        self.TextContent = params.get("TextContent")
        self.SvgContent = params.get("SvgContent")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")


class WatermarkTemplate(AbstractModel):
    """浮水印範本詳情

    """

    def __init__(self):
        """
        :param Definition: 浮水印範本唯一標識。
        :type Definition: int
        :param Type: 浮水印類型，取值：
<li>image：圖片浮水印；</li>
<li>text：文字浮水印。</li>
        :type Type: str
        :param Name: 浮水印範本名稱。
        :type Name: str
        :param Comment: 範本描述訊息。
        :type Comment: str
        :param XPos: 浮水印圖片原點距離視訊圖像原點的水平位置。
<li>當字串以 % 結尾，表示浮水印 Left 爲視訊寬度指定百分比的位置，如 10% 表示 Left 爲視訊寬度的 10%；</li>
<li>當字串以 px 結尾，表示浮水印 Left 爲視訊寬度指定像素的位置，如 100px 表示 Left 爲 100 像素。</li>
        :type XPos: str
        :param YPos: 浮水印圖片原點距離視訊圖像原點的垂直位置。
<li>當字串以 % 結尾，表示浮水印 Top 爲視訊高度指定百分比的位置，如 10% 表示 Top 爲視訊高度的 10%；</li>
<li>當字串以 px 結尾，表示浮水印 Top 爲視訊高度指定像素的位置，如 100px 表示 Top 爲 100 像素。</li>
        :type YPos: str
        :param ImageTemplate: 圖片浮水印範本，僅當 Type 爲 image，該欄位有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ImageTemplate: :class:`taifucloudcloud.mps.v20190612.models.ImageWatermarkTemplate`
        :param TextTemplate: 文字浮水印範本，僅當 Type 爲 text，該欄位有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TextTemplate: :class:`taifucloudcloud.mps.v20190612.models.TextWatermarkTemplateInput`
        :param SvgTemplate: SVG 浮水印範本，當 Type 爲 svg，該欄位有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SvgTemplate: :class:`taifucloudcloud.mps.v20190612.models.SvgWatermarkInput`
        :param CreateTime: 範本創建時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param UpdateTime: 範本最後修改時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type UpdateTime: str
        :param CoordinateOrigin: 原點位置，可選值：
<li>topLeft：表示坐標原點位於視訊圖像左上角，浮水印原點爲圖片或文字的左上角；</li>
<li>topRight：表示坐標原點位於視訊圖像的右上角，浮水印原點爲圖片或文字的右上角；</li>
<li>bottomLeft：表示坐標原點位於視訊圖像的左下角，浮水印原點爲圖片或文字的左下角；</li>
<li>bottomRight：表示坐標原點位於視訊圖像的右下角，浮水印原點爲圖片或文字的右下。；</li>
        :type CoordinateOrigin: str
        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.XPos = None
        self.YPos = None
        self.ImageTemplate = None
        self.TextTemplate = None
        self.SvgTemplate = None
        self.CreateTime = None
        self.UpdateTime = None
        self.CoordinateOrigin = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        if params.get("ImageTemplate") is not None:
            self.ImageTemplate = ImageWatermarkTemplate()
            self.ImageTemplate._deserialize(params.get("ImageTemplate"))
        if params.get("TextTemplate") is not None:
            self.TextTemplate = TextWatermarkTemplateInput()
            self.TextTemplate._deserialize(params.get("TextTemplate"))
        if params.get("SvgTemplate") is not None:
            self.SvgTemplate = SvgWatermarkInput()
            self.SvgTemplate._deserialize(params.get("SvgTemplate"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.CoordinateOrigin = params.get("CoordinateOrigin")


class WorkflowInfo(AbstractModel):
    """工作流訊息詳情。

    """

    def __init__(self):
        """
        :param WorkflowId: 工作流 ID。
        :type WorkflowId: int
        :param WorkflowName: 工作流名稱。
        :type WorkflowName: str
        :param Status: 工作流狀态，取值範圍：
<li>Enabled：已啓用，</li>
<li>Disabled：已禁用。</li>
        :type Status: str
        :param Trigger: 工作流綁定的輸入規則，當上傳視訊命中該規則到該對象時即觸發工作流。
        :type Trigger: :class:`taifucloudcloud.mps.v20190612.models.WorkflowTrigger`
        :param OutputStorage: 視訊處理的文件輸出儲存位置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OutputStorage: :class:`taifucloudcloud.mps.v20190612.models.TaskOutputStorage`
        :param MediaProcessTask: 視訊處理類型任務參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type MediaProcessTask: :class:`taifucloudcloud.mps.v20190612.models.MediaProcessTaskInput`
        :param AiContentReviewTask: 視訊内容審核類型任務參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AiContentReviewTask: :class:`taifucloudcloud.mps.v20190612.models.AiContentReviewTaskInput`
        :param AiAnalysisTask: 視訊内容分析類型任務參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AiAnalysisTask: :class:`taifucloudcloud.mps.v20190612.models.AiAnalysisTaskInput`
        :param AiRecognitionTask: 視訊内容識别類型任務參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AiRecognitionTask: :class:`taifucloudcloud.mps.v20190612.models.AiRecognitionTaskInput`
        :param TaskNotifyConfig: 任務的事件通知訊息，不填代表不獲取事件通知。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TaskNotifyConfig: :class:`taifucloudcloud.mps.v20190612.models.TaskNotifyConfig`
        :param TaskPriority: 任務流的優先級，數值越大優先級越高，取值範圍是 -10 到 10，不填代表 0。
        :type TaskPriority: int
        :param OutputDir: 視訊處理生成的文件輸出的目標目錄，如`/movie/201907/`。
        :type OutputDir: str
        :param CreateTime: 工作流創建時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type CreateTime: str
        :param UpdateTime: 工作流最後修改時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/862/37710#52)。
        :type UpdateTime: str
        """
        self.WorkflowId = None
        self.WorkflowName = None
        self.Status = None
        self.Trigger = None
        self.OutputStorage = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.TaskNotifyConfig = None
        self.TaskPriority = None
        self.OutputDir = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")
        self.WorkflowName = params.get("WorkflowName")
        self.Status = params.get("Status")
        if params.get("Trigger") is not None:
            self.Trigger = WorkflowTrigger()
            self.Trigger._deserialize(params.get("Trigger"))
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        self.TaskPriority = params.get("TaskPriority")
        self.OutputDir = params.get("OutputDir")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class WorkflowTask(AbstractModel):
    """視訊處理任務訊息

    """

    def __init__(self):
        """
        :param TaskId: 視訊處理任務 ID。
        :type TaskId: str
        :param Status: 任務流狀态，取值：
<li>PROCESSING：處理中；</li>
<li>FINISH：已完成。</li>
        :type Status: str
        :param ErrCode: 已棄用，請使用各個具體任務的 ErrCode。
        :type ErrCode: int
        :param Message: 已棄用，請使用各個具體任務的 Message。
        :type Message: str
        :param InputInfo: 視訊處理的目標文件訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type InputInfo: :class:`taifucloudcloud.mps.v20190612.models.MediaInputInfo`
        :param MetaData: 原始視訊的元訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type MetaData: :class:`taifucloudcloud.mps.v20190612.models.MediaMetaData`
        :param MediaProcessResultSet: 視訊處理任務的執行狀态與結果。
        :type MediaProcessResultSet: list of MediaProcessTaskResult
        :param AiContentReviewResultSet: 視訊内容審核任務的執行狀态與結果。
        :type AiContentReviewResultSet: list of AiContentReviewResult
        :param AiAnalysisResultSet: 視訊内容分析任務的執行狀态與結果。
        :type AiAnalysisResultSet: list of AiAnalysisResult
        :param AiRecognitionResultSet: 視訊内容識别任務的執行狀态與結果。
        :type AiRecognitionResultSet: list of AiRecognitionResult
        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.InputInfo = None
        self.MetaData = None
        self.MediaProcessResultSet = None
        self.AiContentReviewResultSet = None
        self.AiAnalysisResultSet = None
        self.AiRecognitionResultSet = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("InputInfo") is not None:
            self.InputInfo = MediaInputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        if params.get("MediaProcessResultSet") is not None:
            self.MediaProcessResultSet = []
            for item in params.get("MediaProcessResultSet"):
                obj = MediaProcessTaskResult()
                obj._deserialize(item)
                self.MediaProcessResultSet.append(obj)
        if params.get("AiContentReviewResultSet") is not None:
            self.AiContentReviewResultSet = []
            for item in params.get("AiContentReviewResultSet"):
                obj = AiContentReviewResult()
                obj._deserialize(item)
                self.AiContentReviewResultSet.append(obj)
        if params.get("AiAnalysisResultSet") is not None:
            self.AiAnalysisResultSet = []
            for item in params.get("AiAnalysisResultSet"):
                obj = AiAnalysisResult()
                obj._deserialize(item)
                self.AiAnalysisResultSet.append(obj)
        if params.get("AiRecognitionResultSet") is not None:
            self.AiRecognitionResultSet = []
            for item in params.get("AiRecognitionResultSet"):
                obj = AiRecognitionResult()
                obj._deserialize(item)
                self.AiRecognitionResultSet.append(obj)


class WorkflowTrigger(AbstractModel):
    """輸入規則，當上傳視訊命中該規則時，即觸發工作流。

    """

    def __init__(self):
        """
        :param Type: 觸發器的類型，目前僅支援 CosFileUpload。
        :type Type: str
        :param CosFileUploadTrigger: 當 Type 爲 CosFileUpload 時必填且有效，爲 COS 觸發規則。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CosFileUploadTrigger: :class:`taifucloudcloud.mps.v20190612.models.CosFileUploadTrigger`
        """
        self.Type = None
        self.CosFileUploadTrigger = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("CosFileUploadTrigger") is not None:
            self.CosFileUploadTrigger = CosFileUploadTrigger()
            self.CosFileUploadTrigger._deserialize(params.get("CosFileUploadTrigger"))