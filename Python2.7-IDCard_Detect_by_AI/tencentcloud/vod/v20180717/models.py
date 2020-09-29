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
        :type ClassificationConfigure: :class:`taifucloudcloud.vod.v20180717.models.ClassificationConfigureInfo`
        :param TagConfigure: 智慧標簽任務控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagConfigure: :class:`taifucloudcloud.vod.v20180717.models.TagConfigureInfo`
        :param CoverConfigure: 智慧封面任務控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CoverConfigure: :class:`taifucloudcloud.vod.v20180717.models.CoverConfigureInfo`
        :param FrameTagConfigure: 智慧按幀標簽任務控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FrameTagConfigure: :class:`taifucloudcloud.vod.v20180717.models.FrameTagConfigureInfo`
        :param CreateTime: 範本創建時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type CreateTime: str
        :param UpdateTime: 範本最後修改時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
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
        :param HeadTailConfigure: 頭尾識别控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type HeadTailConfigure: :class:`taifucloudcloud.vod.v20180717.models.HeadTailConfigureInfo`
        :param FaceConfigure: 人臉識别控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FaceConfigure: :class:`taifucloudcloud.vod.v20180717.models.FaceConfigureInfo`
        :param OcrFullTextConfigure: 文本全文識别控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OcrFullTextConfigure: :class:`taifucloudcloud.vod.v20180717.models.OcrFullTextConfigureInfo`
        :param OcrWordsConfigure: 文本關鍵詞識别控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OcrWordsConfigure: :class:`taifucloudcloud.vod.v20180717.models.OcrWordsConfigureInfo`
        :param AsrFullTextConfigure: 語音全文識别控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AsrFullTextConfigure: :class:`taifucloudcloud.vod.v20180717.models.AsrFullTextConfigureInfo`
        :param AsrWordsConfigure: 語音關鍵詞識别控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AsrWordsConfigure: :class:`taifucloudcloud.vod.v20180717.models.AsrWordsConfigureInfo`
        :param ObjectConfigure: 物體識别控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ObjectConfigure: :class:`taifucloudcloud.vod.v20180717.models.ObjectConfigureInfo`
        :param ScreenshotInterval: 截圖時間間隔，單位：秒。
        :type ScreenshotInterval: float
        :param CreateTime: 範本創建時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type CreateTime: str
        :param UpdateTime: 範本最後修改時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type UpdateTime: str
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.HeadTailConfigure = None
        self.FaceConfigure = None
        self.OcrFullTextConfigure = None
        self.OcrWordsConfigure = None
        self.AsrFullTextConfigure = None
        self.AsrWordsConfigure = None
        self.ObjectConfigure = None
        self.ScreenshotInterval = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("HeadTailConfigure") is not None:
            self.HeadTailConfigure = HeadTailConfigureInfo()
            self.HeadTailConfigure._deserialize(params.get("HeadTailConfigure"))
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
        if params.get("ObjectConfigure") is not None:
            self.ObjectConfigure = ObjectConfigureInfo()
            self.ObjectConfigure._deserialize(params.get("ObjectConfigure"))
        self.ScreenshotInterval = params.get("ScreenshotInterval")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class AdaptiveDynamicStreamingInfoItem(AbstractModel):
    """轉自适應碼流訊息

    """

    def __init__(self):
        """
        :param Definition: 轉自适應碼流規格。
        :type Definition: int
        :param Package: 打包格式，可能爲 hls 和 dash 兩種。
        :type Package: str
        :param DrmType: 加密類型。
        :type DrmType: str
        :param Url: 播放網址。
        :type Url: str
        """
        self.Definition = None
        self.Package = None
        self.DrmType = None
        self.Url = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Package = params.get("Package")
        self.DrmType = params.get("DrmType")
        self.Url = params.get("Url")


class AdaptiveDynamicStreamingTaskInput(AbstractModel):
    """對視訊轉自适應碼流的輸入參數類型

    """

    def __init__(self):
        """
        :param Definition: 轉自适應碼流範本 ID。
        :type Definition: int
        :param WatermarkSet: 浮水印清單，支援多張圖片或文字水印，最大可支援 10 張。
注意：此欄位可能返回 null，表示取不到有效值。
        :type WatermarkSet: list of WatermarkInput
        """
        self.Definition = None
        self.WatermarkSet = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)


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
        :type Type: str
        :param ClassificationTask: 視訊内容分析智慧分類任務的查詢結果，當任務類型爲 Classification 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClassificationTask: :class:`taifucloudcloud.vod.v20180717.models.AiAnalysisTaskClassificationResult`
        :param CoverTask: 視訊内容分析智慧封面任務的查詢結果，當任務類型爲 Cover 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CoverTask: :class:`taifucloudcloud.vod.v20180717.models.AiAnalysisTaskCoverResult`
        :param TagTask: 視訊内容分析智慧標簽任務的查詢結果，當任務類型爲 Tag 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagTask: :class:`taifucloudcloud.vod.v20180717.models.AiAnalysisTaskTagResult`
        :param FrameTagTask: 視訊内容分析智慧按幀標簽任務的查詢結果，當任務類型爲 FrameTag 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FrameTagTask: :class:`taifucloudcloud.vod.v20180717.models.AiAnalysisTaskFrameTagResult`
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
        :type Input: :class:`taifucloudcloud.vod.v20180717.models.AiAnalysisTaskClassificationInput`
        :param Output: 智慧分類任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.AiAnalysisTaskClassificationOutput`
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
        """
        self.CoverSet = None


    def _deserialize(self, params):
        if params.get("CoverSet") is not None:
            self.CoverSet = []
            for item in params.get("CoverSet"):
                obj = MediaAiAnalysisCoverItem()
                obj._deserialize(item)
                self.CoverSet.append(obj)


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
        :type Input: :class:`taifucloudcloud.vod.v20180717.models.AiAnalysisTaskCoverInput`
        :param Output: 智慧封面任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.AiAnalysisTaskCoverOutput`
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
        :type Input: :class:`taifucloudcloud.vod.v20180717.models.AiAnalysisTaskFrameTagInput`
        :param Output: 智慧按幀標簽任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.AiAnalysisTaskFrameTagOutput`
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
        :type Input: :class:`taifucloudcloud.vod.v20180717.models.AiAnalysisTaskTagInput`
        :param Output: 智慧標簽任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.AiAnalysisTaskTagOutput`
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
<li>Political.Asr：Asr 文字鑒政</li>
<li>Political.Ocr：Ocr 文字鑒政</li>
        :type Type: str
        :param PornTask: 視訊内容審核智慧畫面 任務的查詢結果，當任務類型爲 Porn 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PornTask: :class:`taifucloudcloud.vod.v20180717.models.AiReviewTaskPornResult`
        :param TerrorismTask: 視訊内容審核智慧畫面鑒恐任務的查詢結果，當任務類型爲 Terrorism 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TerrorismTask: :class:`taifucloudcloud.vod.v20180717.models.AiReviewTaskTerrorismResult`
        :param PoliticalTask: 視訊内容審核智慧畫面鑒政任務的查詢結果，當任務類型爲 Political 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PoliticalTask: :class:`taifucloudcloud.vod.v20180717.models.AiReviewTaskPoliticalResult`
        :param PornAsrTask: 視訊内容審核 Asr 文字 任務的查詢結果，當任務類型爲 Porn.Asr 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PornAsrTask: :class:`taifucloudcloud.vod.v20180717.models.AiReviewTaskPornAsrResult`
        :param PornOcrTask: 視訊内容審核 Ocr 文字 任務的查詢結果，當任務類型爲 Porn.Ocr 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PornOcrTask: :class:`taifucloudcloud.vod.v20180717.models.AiReviewTaskPornOcrResult`
        :param PoliticalAsrTask: 視訊内容審核 Asr 文字鑒政任務的查詢結果，當任務類型爲 Political.Asr 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PoliticalAsrTask: :class:`taifucloudcloud.vod.v20180717.models.AiReviewTaskPoliticalAsrResult`
        :param PoliticalOcrTask: 視訊内容審核 Ocr 文字鑒政任務的查詢結果，當任務類型爲 Political.Ocr 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PoliticalOcrTask: :class:`taifucloudcloud.vod.v20180717.models.AiReviewTaskPoliticalOcrResult`
        """
        self.Type = None
        self.PornTask = None
        self.TerrorismTask = None
        self.PoliticalTask = None
        self.PornAsrTask = None
        self.PornOcrTask = None
        self.PoliticalAsrTask = None
        self.PoliticalOcrTask = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
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
        :type FaceTask: :class:`taifucloudcloud.vod.v20180717.models.AiRecognitionTaskFaceResult`
        :param AsrWordsTask: 語音關鍵詞識别結果，當 Type 爲
 AsrWordsRecognition 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AsrWordsTask: :class:`taifucloudcloud.vod.v20180717.models.AiRecognitionTaskAsrWordsResult`
        :param AsrFullTextTask: 語音全文識别結果，當 Type 爲
 AsrFullTextRecognition 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AsrFullTextTask: :class:`taifucloudcloud.vod.v20180717.models.AiRecognitionTaskAsrFullTextResult`
        :param OcrWordsTask: 文本關鍵詞識别結果，當 Type 爲
 OcrWordsRecognition 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OcrWordsTask: :class:`taifucloudcloud.vod.v20180717.models.AiRecognitionTaskOcrWordsResult`
        :param OcrFullTextTask: 文本全文識别結果，當 Type 爲
 OcrFullTextRecognition 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OcrFullTextTask: :class:`taifucloudcloud.vod.v20180717.models.AiRecognitionTaskOcrFullTextResult`
        :param HeadTailTask: 視訊片頭片尾識别結果，當 Type 爲
 HeadTailRecognition 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type HeadTailTask: :class:`taifucloudcloud.vod.v20180717.models.AiRecognitionTaskHeadTailResult`
        :param ObjectTask: 物體識别結果，當 Type 爲
 ObjectRecognition 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ObjectTask: :class:`taifucloudcloud.vod.v20180717.models.AiRecognitionTaskObjectResult`
        """
        self.Type = None
        self.FaceTask = None
        self.AsrWordsTask = None
        self.AsrFullTextTask = None
        self.OcrWordsTask = None
        self.OcrFullTextTask = None
        self.HeadTailTask = None
        self.ObjectTask = None


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
        if params.get("HeadTailTask") is not None:
            self.HeadTailTask = AiRecognitionTaskHeadTailResult()
            self.HeadTailTask._deserialize(params.get("HeadTailTask"))
        if params.get("ObjectTask") is not None:
            self.ObjectTask = AiRecognitionTaskObjectResult()
            self.ObjectTask._deserialize(params.get("ObjectTask"))


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
        :type Input: :class:`taifucloudcloud.vod.v20180717.models.AiRecognitionTaskAsrFullTextResultInput`
        :param Output: 語音全文識别任務輸出訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.AiRecognitionTaskAsrFullTextResultOutput`
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
        :param SubtitleUrl: 字幕文件 Url。
        :type SubtitleUrl: str
        """
        self.SegmentSet = None
        self.SubtitleUrl = None


    def _deserialize(self, params):
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskAsrFullTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        self.SubtitleUrl = params.get("SubtitleUrl")


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
        :type Input: :class:`taifucloudcloud.vod.v20180717.models.AiRecognitionTaskAsrWordsResultInput`
        :param Output: 語音關鍵詞識别任務輸出訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.AiRecognitionTaskAsrWordsResultOutput`
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
        :type Input: :class:`taifucloudcloud.vod.v20180717.models.AiRecognitionTaskFaceResultInput`
        :param Output: 人臉識别任務輸出訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.AiRecognitionTaskFaceResultOutput`
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


class AiRecognitionTaskHeadTailResult(AbstractModel):
    """視訊片頭片尾識别結果。

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 視訊片頭片尾識别任務輸入訊息。
        :type Input: :class:`taifucloudcloud.vod.v20180717.models.AiRecognitionTaskHeadTailResultInput`
        :param Output: 視訊片頭片尾識别任務輸出訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.AiRecognitionTaskHeadTailResultOutput`
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
            self.Input = AiRecognitionTaskHeadTailResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskHeadTailResultOutput()
            self.Output._deserialize(params.get("Output"))


class AiRecognitionTaskHeadTailResultInput(AbstractModel):
    """視訊片頭片尾識别的輸入。

    """

    def __init__(self):
        """
        :param Definition: 視訊片頭片尾識别範本 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiRecognitionTaskHeadTailResultOutput(AbstractModel):
    """視訊片頭片尾識别輸出。

    """

    def __init__(self):
        """
        :param HeadConfidence: 片頭識别置信度。取值：0~100。
        :type HeadConfidence: float
        :param HeadTimeOffset: 視訊片頭的結束時間點，單位：秒。
        :type HeadTimeOffset: float
        :param TailConfidence: 片尾識别置信度。取值：0~100。
        :type TailConfidence: float
        :param TailTimeOffset: 視訊片尾的開始時間點，單位：秒。
        :type TailTimeOffset: float
        """
        self.HeadConfidence = None
        self.HeadTimeOffset = None
        self.TailConfidence = None
        self.TailTimeOffset = None


    def _deserialize(self, params):
        self.HeadConfidence = params.get("HeadConfidence")
        self.HeadTimeOffset = params.get("HeadTimeOffset")
        self.TailConfidence = params.get("TailConfidence")
        self.TailTimeOffset = params.get("TailTimeOffset")


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


class AiRecognitionTaskObjectResult(AbstractModel):
    """物體識别結果。

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 物體識别任務輸入訊息。
        :type Input: :class:`taifucloudcloud.vod.v20180717.models.AiRecognitionTaskObjectResultInput`
        :param Output: 物體識别任務輸出訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.AiRecognitionTaskObjectResultOutput`
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
            self.Input = AiRecognitionTaskObjectResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskObjectResultOutput()
            self.Output._deserialize(params.get("Output"))


class AiRecognitionTaskObjectResultInput(AbstractModel):
    """物體識别任務輸入類型。

    """

    def __init__(self):
        """
        :param Definition: 物體識别範本 ID。
        :type Definition: int
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class AiRecognitionTaskObjectResultItem(AbstractModel):
    """單個物體識别結果。

    """

    def __init__(self):
        """
        :param Name: 識别的物體名稱。
        :type Name: str
        :param SegmentSet: 物體出現的片段清單。
        :type SegmentSet: list of AiRecognitionTaskObjectSeqmentItem
        """
        self.Name = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskObjectSeqmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class AiRecognitionTaskObjectResultOutput(AbstractModel):
    """智慧物體識别輸出。

    """

    def __init__(self):
        """
        :param ResultSet: 智慧物體識别結果集。
        :type ResultSet: list of AiRecognitionTaskObjectResultItem
        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = AiRecognitionTaskObjectResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)


class AiRecognitionTaskObjectSeqmentItem(AbstractModel):
    """物體識别結果片段。

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
        :type Input: :class:`taifucloudcloud.vod.v20180717.models.AiRecognitionTaskOcrFullTextResultInput`
        :param Output: 文本全文識别任務輸出訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.AiRecognitionTaskOcrFullTextResultOutput`
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
        :type Input: :class:`taifucloudcloud.vod.v20180717.models.AiRecognitionTaskOcrWordsResultInput`
        :param Output: 文本關鍵詞識别任務輸出訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.AiRecognitionTaskOcrWordsResultOutput`
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
注意：此欄位可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param Suggestion: Asr 文字涉政、敏感結果建議，取值範圍：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param SegmentSet: Asr 文字有涉政、敏感嫌疑的視訊片段清單。
注意：此欄位可能返回 null，表示取不到有效值。
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
注意：此欄位可能返回 null，表示取不到有效值。
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
注意：此欄位可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param Suggestion: 涉政結果建議，取值範圍：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Label: 視訊鑒政結果標簽，取值範圍：
<li>politician：政治人物。</li>
<li>violation_photo：違規圖標。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type Label: str
        :param SegmentSet: 有涉政嫌疑的視訊片段清單。
注意：此欄位可能返回 null，表示取不到有效值。
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
注意：此欄位可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param Suggestion: Asr 文字涉黃結果建議，取值範圍：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param SegmentSet: Asr 文字有涉黃嫌疑的視訊片段清單。
注意：此欄位可能返回 null，表示取不到有效值。
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
注意：此欄位可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param Suggestion: Ocr 文字涉黃結果建議，取值範圍：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param SegmentSet: Ocr 文字有涉黃嫌疑的視訊片段清單。
注意：此欄位可能返回 null，表示取不到有效值。
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
注意：此欄位可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param Suggestion:  結果建議，取值範圍：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Label: 視訊 結果標簽，取值範圍：
<li>porn：色情。</li>
<li>sexy：性感。</li>
<li>vulgar：低俗。</li>
<li>intimacy：親密行爲。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type Label: str
        :param SegmentSet: 有涉黃嫌疑的視訊片段清單。
注意：此欄位可能返回 null，表示取不到有效值。
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


class AiReviewTaskPoliticalAsrResult(AbstractModel):
    """内容審核 Asr 文字鑒政、敏感任務結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 錯誤訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 内容審核 Asr 文字鑒政任務輸入。
        :type Input: :class:`taifucloudcloud.vod.v20180717.models.AiReviewPoliticalAsrTaskInput`
        :param Output: 内容審核 Asr 文字鑒政任務輸出。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.AiReviewPoliticalAsrTaskOutput`
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
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 錯誤訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 内容審核 Ocr 文字鑒政任務輸入。
        :type Input: :class:`taifucloudcloud.vod.v20180717.models.AiReviewPoliticalOcrTaskInput`
        :param Output: 内容審核 Ocr 文字鑒政任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.AiReviewPoliticalOcrTaskOutput`
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
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 錯誤訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 内容審核鑒政任務輸入。
        :type Input: :class:`taifucloudcloud.vod.v20180717.models.AiReviewPoliticalTaskInput`
        :param Output: 内容審核鑒政任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.AiReviewPoliticalTaskOutput`
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
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 錯誤訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 内容審核 Asr 文字 任務輸入。
        :type Input: :class:`taifucloudcloud.vod.v20180717.models.AiReviewPornAsrTaskInput`
        :param Output: 内容審核 Asr 文字 任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.AiReviewPornAsrTaskOutput`
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
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 錯誤訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 内容審核 Ocr 文字 任務輸入。
        :type Input: :class:`taifucloudcloud.vod.v20180717.models.AiReviewPornOcrTaskInput`
        :param Output: 内容審核 Ocr 文字 任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.AiReviewPornOcrTaskOutput`
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
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 錯誤訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 内容審核 任務輸入。
        :type Input: :class:`taifucloudcloud.vod.v20180717.models.AiReviewPornTaskInput`
        :param Output: 内容審核 任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.AiReviewPornTaskOutput`
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


class AiReviewTaskTerrorismResult(AbstractModel):
    """内容審核鑒恐任務結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 錯誤訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 内容審核鑒恐任務輸入。
        :type Input: :class:`taifucloudcloud.vod.v20180717.models.AiReviewTerrorismTaskInput`
        :param Output: 内容審核鑒恐任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.AiReviewTerrorismTaskOutput`
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
注意：此欄位可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param Suggestion: 暴恐結果建議，取值範圍：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
注意：此欄位可能返回 null，表示取不到有效值。
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
注意：此欄位可能返回 null，表示取不到有效值。
        :type Label: str
        :param SegmentSet: 有暴恐嫌疑的視訊片段清單。
注意：此欄位可能返回 null，表示取不到有效值。
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
注意：此欄位可能返回 null，表示取不到有效值。
        :type Description: str
        :param FaceInfoSet: 人臉訊息。
        :type FaceInfoSet: list of AiSampleFaceInfo
        :param TagSet: 人物標簽。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagSet: list of str
        :param UsageSet: 應用場景。
        :type UsageSet: list of str
        :param CreateTime: 創建時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type CreateTime: str
        :param UpdateTime: 最後修改時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
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
        :param CreateTime: 創建時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type CreateTime: str
        :param UpdateTime: 最後修改時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
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
    """轉動圖任務類型

    """

    def __init__(self):
        """
        :param Definition: 視訊轉動圖範本 ID
        :type Definition: int
        :param StartTimeOffset: 動圖在視訊中的開始時間，單位爲秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 動圖在視訊中的結束時間，單位爲秒。
        :type EndTimeOffset: float
        """
        self.Definition = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")


class ApplyUploadRequest(AbstractModel):
    """ApplyUpload請求參數結構體

    """

    def __init__(self):
        """
        :param MediaType: 媒體類型，可選值請參考[上傳能力綜述](https://cloud.taifucloud.com/document/product/266/9760#.E6.96.87.E4.BB.B6.E7.B1.BB.E5.9E.8B)。
        :type MediaType: str
        :param MediaName: 媒體名稱。
        :type MediaName: str
        :param CoverType: 封面類型，可選值請參考[上傳能力綜述](https://cloud.taifucloud.com/document/product/266/9760#.E6.96.87.E4.BB.B6.E7.B1.BB.E5.9E.8B)。
        :type CoverType: str
        :param Procedure: 媒體後續任務操作，詳見[上傳指定任務流](https://cloud.taifucloud.com/document/product/266/9759)。
        :type Procedure: str
        :param ExpireTime: 媒體文件過期時間，格式按照 ISO 8601 標準表示，詳見 [ISO 日期格式說明](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type ExpireTime: str
        :param StorageRegion: 指定上傳園區，僅适用於對上傳地域有特殊需求的用戶。
        :type StorageRegion: str
        :param ClassId: 分類ID，用於對媒體進行分類管理，可通過[創建分類](https://cloud.taifucloud.com/document/product/266/7812)介面，創建分類，獲得分類 ID。
<li>預設值：0，表示其他分類。</li>
        :type ClassId: int
        :param SourceContext: 來源上下文，用於透傳用戶請求訊息，上傳回調介面将返回該欄位值，最長 250 個字元。
        :type SourceContext: str
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.MediaType = None
        self.MediaName = None
        self.CoverType = None
        self.Procedure = None
        self.ExpireTime = None
        self.StorageRegion = None
        self.ClassId = None
        self.SourceContext = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.MediaType = params.get("MediaType")
        self.MediaName = params.get("MediaName")
        self.CoverType = params.get("CoverType")
        self.Procedure = params.get("Procedure")
        self.ExpireTime = params.get("ExpireTime")
        self.StorageRegion = params.get("StorageRegion")
        self.ClassId = params.get("ClassId")
        self.SourceContext = params.get("SourceContext")
        self.SubAppId = params.get("SubAppId")


class ApplyUploadResponse(AbstractModel):
    """ApplyUpload返回參數結構體

    """

    def __init__(self):
        """
        :param StorageBucket: 儲存桶，用於上傳介面 URL 的 bucket_name。
        :type StorageBucket: str
        :param StorageRegion: 儲存園區，用於上傳介面 Host 的 Region。
        :type StorageRegion: str
        :param VodSessionKey: 點播會話，用於确認上傳介面的參數 VodSessionKey。
        :type VodSessionKey: str
        :param MediaStoragePath: 媒體儲存路徑，用於上傳介面儲存媒體的對象鍵（Key）。
注意：此欄位可能返回 null，表示取不到有效值。
        :type MediaStoragePath: str
        :param CoverStoragePath: 封面儲存路徑，用於上傳介面儲存封面的對象鍵（Key）。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CoverStoragePath: str
        :param TempCertificate: 臨時憑證，用於上傳介面的權限驗證。
        :type TempCertificate: :class:`taifucloudcloud.vod.v20180717.models.TempCertificate`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.StorageBucket = None
        self.StorageRegion = None
        self.VodSessionKey = None
        self.MediaStoragePath = None
        self.CoverStoragePath = None
        self.TempCertificate = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StorageBucket = params.get("StorageBucket")
        self.StorageRegion = params.get("StorageRegion")
        self.VodSessionKey = params.get("VodSessionKey")
        self.MediaStoragePath = params.get("MediaStoragePath")
        self.CoverStoragePath = params.get("CoverStoragePath")
        if params.get("TempCertificate") is not None:
            self.TempCertificate = TempCertificate()
            self.TempCertificate._deserialize(params.get("TempCertificate"))
        self.RequestId = params.get("RequestId")


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
        :param Codec: 音訊流的編碼格式，可選值：
<li>libfdk_aac：更适合 mp4 和 hls；</li>
<li>libmp3lame：更适合 flv；</li>
<li>mp2。</li>
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
        :param Codec: 音訊流的編碼格式，可選值：
<li>libfdk_aac：更适合 mp4 和 hls；</li>
<li>libmp3lame：更适合 flv；</li>
<li>mp2。</li>
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


class AudioTrackItem(AbstractModel):
    """音訊軌道上的音訊片段訊息。

    """

    def __init__(self):
        """
        :param SourceMedia: 音訊素材的媒體文件來源。可以是點播的文件 ID，也可以是其它文件的 URL。
        :type SourceMedia: str
        :param SourceMediaStartTime: 音訊片段取自素材文件的起始時間，單位爲秒。0 表示從素材開始位置截取。預設爲0。
        :type SourceMediaStartTime: float
        :param Duration: 音訊片段的時長，單位爲秒。預設和素材本身長度一緻，表示截取全部素材。
        :type Duration: float
        :param AudioOperations: 對音訊片段進行的操作，如音量調節等。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AudioOperations: list of AudioTransform
        """
        self.SourceMedia = None
        self.SourceMediaStartTime = None
        self.Duration = None
        self.AudioOperations = None


    def _deserialize(self, params):
        self.SourceMedia = params.get("SourceMedia")
        self.SourceMediaStartTime = params.get("SourceMediaStartTime")
        self.Duration = params.get("Duration")
        if params.get("AudioOperations") is not None:
            self.AudioOperations = []
            for item in params.get("AudioOperations"):
                obj = AudioTransform()
                obj._deserialize(item)
                self.AudioOperations.append(obj)


class AudioTransform(AbstractModel):
    """音訊操作

    """

    def __init__(self):
        """
        :param Type: 音訊操作類型，取值有：
<li>Volume：音量調節。</li>
        :type Type: str
        :param VolumeParam: 音量調節參數， 當 Type = Volume 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type VolumeParam: :class:`taifucloudcloud.vod.v20180717.models.AudioVolumeParam`
        """
        self.Type = None
        self.VolumeParam = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("VolumeParam") is not None:
            self.VolumeParam = AudioVolumeParam()
            self.VolumeParam._deserialize(params.get("VolumeParam"))


class AudioVolumeParam(AbstractModel):
    """音訊增益調節參數

    """

    def __init__(self):
        """
        :param Gain: 音訊增益，取值範圍0~10。僅在Mute=0時生效。
<li>大於1表示增加音量。</li>
<li>小於1表示降低音量。</li>
<li>1：表示不改變。</li>
預設是1。
        :type Gain: float
        :param Mute: 是否靜音，取值範圍0或1。
<li>0表示不靜音。</li>
<li>1表示靜音。</li>
預設是0。
        :type Mute: int
        """
        self.Gain = None
        self.Mute = None


    def _deserialize(self, params):
        self.Gain = params.get("Gain")
        self.Mute = params.get("Mute")


class Canvas(AbstractModel):
    """畫布訊息。制作視訊時，如果源素材（視訊或者圖片）不能填滿輸出的視訊視窗，将用設置的畫布進行背景繪制。

    """

    def __init__(self):
        """
        :param Color: 背景顔色，取值有：
<li>Black：黑色背景</li>
<li>White：白色背景</li>
預設值：Black。
        :type Color: str
        :param Width: 畫布寬度，即輸出視訊的寬度，取值範圍：0~ 4096，單位：px。
預設值：0，表示和第一個視訊軌的第一個視訊片段的視訊寬度一緻。
        :type Width: int
        :param Height: 畫布高度，即輸出視訊的高度（或長邊），取值範圍：0~ 4096，單位：px。
預設值：0，表示和第一個視訊軌的第一個視訊片段的視訊高度一緻。
        :type Height: int
        """
        self.Color = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.Color = params.get("Color")
        self.Width = params.get("Width")
        self.Height = params.get("Height")


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


class ClipFileInfo2017(AbstractModel):
    """視訊裁剪結果文件訊息（2017 版）

    """

    def __init__(self):
        """
        :param ErrCode: 錯誤碼
<li>0：成功；</li>
<li>其他值：失敗。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 錯誤描述。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param FileId: 輸出目標文件的文件 ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileId: str
        :param FileUrl: 輸出目標文件的文件網址。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileUrl: str
        :param FileType: 輸出目標文件的文件類型。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileType: str
        """
        self.ErrCode = None
        self.Message = None
        self.FileId = None
        self.FileUrl = None
        self.FileType = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.FileId = params.get("FileId")
        self.FileUrl = params.get("FileUrl")
        self.FileType = params.get("FileType")


class ClipTask2017(AbstractModel):
    """視訊剪輯任務訊息，該結構僅用於對 2017 版[視訊剪輯](https://cloud.taifucloud.com/document/product/266/10156)介面發起的任務。

    """

    def __init__(self):
        """
        :param TaskId: 視訊剪輯任務 ID。
        :type TaskId: str
        :param SrcFileId: 視訊剪輯任務源文件 ID。
        :type SrcFileId: str
        :param FileInfo: 視訊剪輯輸出的文件訊息。
        :type FileInfo: :class:`taifucloudcloud.vod.v20180717.models.ClipFileInfo2017`
        """
        self.TaskId = None
        self.SrcFileId = None
        self.FileInfo = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.SrcFileId = params.get("SrcFileId")
        if params.get("FileInfo") is not None:
            self.FileInfo = ClipFileInfo2017()
            self.FileInfo._deserialize(params.get("FileInfo"))


class CommitUploadRequest(AbstractModel):
    """CommitUpload請求參數結構體

    """

    def __init__(self):
        """
        :param VodSessionKey: 點播會話，取申請上傳介面的返回值 VodSessionKey。
        :type VodSessionKey: str
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.VodSessionKey = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.VodSessionKey = params.get("VodSessionKey")
        self.SubAppId = params.get("SubAppId")


class CommitUploadResponse(AbstractModel):
    """CommitUpload返回參數結構體

    """

    def __init__(self):
        """
        :param FileId: 媒體文件的唯一標識。
        :type FileId: str
        :param MediaUrl: 媒體播放網址。
注意：此欄位可能返回 null，表示取不到有效值。
        :type MediaUrl: str
        :param CoverUrl: 媒體封面網址。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CoverUrl: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FileId = None
        self.MediaUrl = None
        self.CoverUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.MediaUrl = params.get("MediaUrl")
        self.CoverUrl = params.get("CoverUrl")
        self.RequestId = params.get("RequestId")


class ComposeMediaOutput(AbstractModel):
    """輸出的媒體文件訊息。

    """

    def __init__(self):
        """
        :param FileName: 文件名稱，最長 64 個字元。
        :type FileName: str
        :param Description: 描述訊息，最長 128 個字元。
        :type Description: str
        :param Container: 封裝格式，可選值：mp4、mp3。其中，mp3 爲純音訊文件。
        :type Container: str
        :param VideoStream: 輸出的視訊訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type VideoStream: :class:`taifucloudcloud.vod.v20180717.models.OutputVideoStream`
        :param AudioStream: 輸出的音訊訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AudioStream: :class:`taifucloudcloud.vod.v20180717.models.OutputAudioStream`
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
        """
        self.FileName = None
        self.Description = None
        self.Container = None
        self.VideoStream = None
        self.AudioStream = None
        self.RemoveVideo = None
        self.RemoveAudio = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.Description = params.get("Description")
        self.Container = params.get("Container")
        if params.get("VideoStream") is not None:
            self.VideoStream = OutputVideoStream()
            self.VideoStream._deserialize(params.get("VideoStream"))
        if params.get("AudioStream") is not None:
            self.AudioStream = OutputAudioStream()
            self.AudioStream._deserialize(params.get("AudioStream"))
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")


class ComposeMediaTask(AbstractModel):
    """制作媒體文件任務訊息

    """

    def __init__(self):
        """
        :param TaskId: 任務 ID。
        :type TaskId: str
        :param Status: 任務流狀态，取值：
<li>PROCESSING：處理中；</li>
<li>FINISH：已完成。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: str
        :param ErrCode: 錯誤碼
<li>0：成功；</li>
<li>其他值：失敗。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 錯誤訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 制作媒體文件任務的輸入。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Input: :class:`taifucloudcloud.vod.v20180717.models.ComposeMediaTaskInput`
        :param Output: 制作媒體文件任務的輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.ComposeMediaTaskOutput`
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
            self.Input = ComposeMediaTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = ComposeMediaTaskOutput()
            self.Output._deserialize(params.get("Output"))


class ComposeMediaTaskInput(AbstractModel):
    """制作媒體文件任務的輸入。

    """

    def __init__(self):
        """
        :param Tracks: 輸入的媒體軌道清單，包括視訊、音訊、圖片等素材組成的多個軌道訊息。
        :type Tracks: list of MediaTrack
        :param Canvas: 制作視訊文件時使用的畫布。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Canvas: :class:`taifucloudcloud.vod.v20180717.models.Canvas`
        :param Output: 輸出的媒體文件訊息。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.ComposeMediaOutput`
        """
        self.Tracks = None
        self.Canvas = None
        self.Output = None


    def _deserialize(self, params):
        if params.get("Tracks") is not None:
            self.Tracks = []
            for item in params.get("Tracks"):
                obj = MediaTrack()
                obj._deserialize(item)
                self.Tracks.append(obj)
        if params.get("Canvas") is not None:
            self.Canvas = Canvas()
            self.Canvas._deserialize(params.get("Canvas"))
        if params.get("Output") is not None:
            self.Output = ComposeMediaOutput()
            self.Output._deserialize(params.get("Output"))


class ComposeMediaTaskOutput(AbstractModel):
    """制作媒體文件任務的輸出。

    """

    def __init__(self):
        """
        :param FileType: 文件類型，例如 mp4、mp3 等。
        :type FileType: str
        :param FileId: 媒體文件 ID。
        :type FileId: str
        :param FileUrl: 媒體文件播放網址。
        :type FileUrl: str
        """
        self.FileType = None
        self.FileId = None
        self.FileUrl = None


    def _deserialize(self, params):
        self.FileType = params.get("FileType")
        self.FileId = params.get("FileId")
        self.FileUrl = params.get("FileUrl")


class ConcatFileInfo2017(AbstractModel):
    """視訊拼接源文件訊息（2017 版）

    """

    def __init__(self):
        """
        :param ErrCode: 錯誤碼
<li>0：成功；</li>
<li>其他值：失敗。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 錯誤訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param FileId: 視訊拼接源文件的 ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileId: str
        :param FileUrl: 視訊拼接源文件的網址。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileUrl: str
        :param FileType: 視訊拼接源文件的格式。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileType: str
        """
        self.ErrCode = None
        self.Message = None
        self.FileId = None
        self.FileUrl = None
        self.FileType = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.FileId = params.get("FileId")
        self.FileUrl = params.get("FileUrl")
        self.FileType = params.get("FileType")


class ConcatTask2017(AbstractModel):
    """視訊拼接任務訊息，該結構僅用於對 2017 版[視訊拼接](https://cloud.taifucloud.com/document/product/266/7821)介面發起的任務。

    """

    def __init__(self):
        """
        :param TaskId: 視訊拼接任務 ID。
        :type TaskId: str
        :param FileInfoSet: 視訊拼接源文件訊息。
        :type FileInfoSet: list of ConcatFileInfo2017
        """
        self.TaskId = None
        self.FileInfoSet = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        if params.get("FileInfoSet") is not None:
            self.FileInfoSet = []
            for item in params.get("FileInfoSet"):
                obj = ConcatFileInfo2017()
                obj._deserialize(item)
                self.FileInfoSet.append(obj)


class ConfirmEventsRequest(AbstractModel):
    """ConfirmEvents請求參數結構體

    """

    def __init__(self):
        """
        :param EventHandles: 事件句柄，數組長度限制：16。
        :type EventHandles: list of str
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.EventHandles = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.EventHandles = params.get("EventHandles")
        self.SubAppId = params.get("SubAppId")


class ConfirmEventsResponse(AbstractModel):
    """ConfirmEvents返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


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
        :type PornConfigure: :class:`taifucloudcloud.vod.v20180717.models.PornConfigureInfo`
        :param TerrorismConfigure: 鑒恐控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TerrorismConfigure: :class:`taifucloudcloud.vod.v20180717.models.TerrorismConfigureInfo`
        :param PoliticalConfigure: 鑒政控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PoliticalConfigure: :class:`taifucloudcloud.vod.v20180717.models.PoliticalConfigureInfo`
        :param UserDefineConfigure: 用戶自定義内容審核控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type UserDefineConfigure: :class:`taifucloudcloud.vod.v20180717.models.UserDefineConfigureInfo`
        :param ReviewWallSwitch: 審核結果是否進入審核牆（對審核結果進行人工複核）的開關。
<li>ON：是；</li>
<li>OFF：否。</li>
        :type ReviewWallSwitch: str
        :param ScreenshotInterval: 截幀間隔，單位爲秒。當不填時，預設截幀間隔爲 1 秒，最小值爲 0.5 秒。
        :type ScreenshotInterval: float
        :param CreateTime: 範本創建時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type CreateTime: str
        :param UpdateTime: 範本最後修改時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type UpdateTime: str
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.PornConfigure = None
        self.TerrorismConfigure = None
        self.PoliticalConfigure = None
        self.UserDefineConfigure = None
        self.ReviewWallSwitch = None
        self.ScreenshotInterval = None
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
        if params.get("UserDefineConfigure") is not None:
            self.UserDefineConfigure = UserDefineConfigureInfo()
            self.UserDefineConfigure._deserialize(params.get("UserDefineConfigure"))
        self.ReviewWallSwitch = params.get("ReviewWallSwitch")
        self.ScreenshotInterval = params.get("ScreenshotInterval")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class CoverBySnapshotTaskInput(AbstractModel):
    """對視訊截圖做封面任務輸入參數類型

    """

    def __init__(self):
        """
        :param Definition: 指定時間點截圖範本 ID。
        :type Definition: int
        :param PositionType: 截圖方式。包含：
<li>Time：依照時間點截圖</li>
<li>Percent：依照百分比截圖</li>
        :type PositionType: str
        :param PositionValue: 截圖位置：
<li>對於依照時間點截圖，該值表示指定視訊第幾秒的截圖作爲封面</li>
<li>對於依照百分比截圖，該值表示使用視訊百分之多少的截圖作爲封面</li>
        :type PositionValue: float
        :param WatermarkSet: 浮水印清單，支援多張圖片或文字水印，最大可支援 10 張。
注意：此欄位可能返回 null，表示取不到有效值。
        :type WatermarkSet: list of WatermarkInput
        """
        self.Definition = None
        self.PositionType = None
        self.PositionValue = None
        self.WatermarkSet = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.PositionType = params.get("PositionType")
        self.PositionValue = params.get("PositionValue")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)


class CoverBySnapshotTaskOutput(AbstractModel):
    """對視訊截圖做封面任務輸出類型

    """

    def __init__(self):
        """
        :param CoverUrl: 封面 URL。
        :type CoverUrl: str
        """
        self.CoverUrl = None


    def _deserialize(self, params):
        self.CoverUrl = params.get("CoverUrl")


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
        :type ClassificationConfigure: :class:`taifucloudcloud.vod.v20180717.models.ClassificationConfigureInfo`
        :param TagConfigure: 智慧標簽任務控制參數。
        :type TagConfigure: :class:`taifucloudcloud.vod.v20180717.models.TagConfigureInfo`
        :param CoverConfigure: 智慧封面任務控制參數。
        :type CoverConfigure: :class:`taifucloudcloud.vod.v20180717.models.CoverConfigureInfo`
        :param FrameTagConfigure: 智慧按幀標簽任務控制參數。
        :type FrameTagConfigure: :class:`taifucloudcloud.vod.v20180717.models.FrameTagConfigureInfo`
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Name = None
        self.Comment = None
        self.ClassificationConfigure = None
        self.TagConfigure = None
        self.CoverConfigure = None
        self.FrameTagConfigure = None
        self.SubAppId = None


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
        self.SubAppId = params.get("SubAppId")


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
        :param HeadTailConfigure: 視訊片頭片尾識别控制參數。
        :type HeadTailConfigure: :class:`taifucloudcloud.vod.v20180717.models.HeadTailConfigureInfo`
        :param FaceConfigure: 人臉識别控制參數。
        :type FaceConfigure: :class:`taifucloudcloud.vod.v20180717.models.FaceConfigureInfo`
        :param OcrFullTextConfigure: 文本全文識别控制參數。
        :type OcrFullTextConfigure: :class:`taifucloudcloud.vod.v20180717.models.OcrFullTextConfigureInfo`
        :param OcrWordsConfigure: 文本關鍵詞識别控制參數。
        :type OcrWordsConfigure: :class:`taifucloudcloud.vod.v20180717.models.OcrWordsConfigureInfo`
        :param AsrFullTextConfigure: 語音全文識别控制參數。
        :type AsrFullTextConfigure: :class:`taifucloudcloud.vod.v20180717.models.AsrFullTextConfigureInfo`
        :param AsrWordsConfigure: 語音關鍵詞識别控制參數。
        :type AsrWordsConfigure: :class:`taifucloudcloud.vod.v20180717.models.AsrWordsConfigureInfo`
        :param ObjectConfigure: 物體識别控制參數。
        :type ObjectConfigure: :class:`taifucloudcloud.vod.v20180717.models.ObjectConfigureInfo`
        :param ScreenshotInterval: 截幀間隔，單位爲秒。當不填時，預設截幀間隔爲 1 秒，最小值爲 0.5 秒。
        :type ScreenshotInterval: float
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Name = None
        self.Comment = None
        self.HeadTailConfigure = None
        self.FaceConfigure = None
        self.OcrFullTextConfigure = None
        self.OcrWordsConfigure = None
        self.AsrFullTextConfigure = None
        self.AsrWordsConfigure = None
        self.ObjectConfigure = None
        self.ScreenshotInterval = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("HeadTailConfigure") is not None:
            self.HeadTailConfigure = HeadTailConfigureInfo()
            self.HeadTailConfigure._deserialize(params.get("HeadTailConfigure"))
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
        if params.get("ObjectConfigure") is not None:
            self.ObjectConfigure = ObjectConfigureInfo()
            self.ObjectConfigure._deserialize(params.get("ObjectConfigure"))
        self.ScreenshotInterval = params.get("ScreenshotInterval")
        self.SubAppId = params.get("SubAppId")


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


class CreateClassRequest(AbstractModel):
    """CreateClass請求參數結構體

    """

    def __init__(self):
        """
        :param ParentId: 父類 ID，一級分類填寫 -1。
        :type ParentId: int
        :param ClassName: 分類名稱，長度限制：1-64 個字元。
        :type ClassName: str
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.ParentId = None
        self.ClassName = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.ParentId = params.get("ParentId")
        self.ClassName = params.get("ClassName")
        self.SubAppId = params.get("SubAppId")


class CreateClassResponse(AbstractModel):
    """CreateClass返回參數結構體

    """

    def __init__(self):
        """
        :param ClassId: 分類 ID
        :type ClassId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ClassId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClassId = params.get("ClassId")
        self.RequestId = params.get("RequestId")


class CreateContentReviewTemplateRequest(AbstractModel):
    """CreateContentReviewTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param ReviewWallSwitch: 審核結果是否進入審核牆（對審核結果進行人工複核）的開關。
<li>ON：是；</li>
<li>OFF：否。</li>
        :type ReviewWallSwitch: str
        :param Name: 内容審核範本名稱，長度限制：64 個字元。
        :type Name: str
        :param Comment: 内容審核範本描述訊息，長度限制：256 個字元。
        :type Comment: str
        :param PornConfigure:  控制參數。
        :type PornConfigure: :class:`taifucloudcloud.vod.v20180717.models.PornConfigureInfo`
        :param TerrorismConfigure: 鑒恐控制參數。
        :type TerrorismConfigure: :class:`taifucloudcloud.vod.v20180717.models.TerrorismConfigureInfo`
        :param PoliticalConfigure: 鑒政控制參數。
        :type PoliticalConfigure: :class:`taifucloudcloud.vod.v20180717.models.PoliticalConfigureInfo`
        :param UserDefineConfigure: 用戶自定義内容審核控制參數。
        :type UserDefineConfigure: :class:`taifucloudcloud.vod.v20180717.models.UserDefineConfigureInfo`
        :param ScreenshotInterval: 截幀間隔，單位爲秒。當不填時，預設截幀間隔爲 1 秒，最小值爲 0.5 秒。
        :type ScreenshotInterval: float
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.ReviewWallSwitch = None
        self.Name = None
        self.Comment = None
        self.PornConfigure = None
        self.TerrorismConfigure = None
        self.PoliticalConfigure = None
        self.UserDefineConfigure = None
        self.ScreenshotInterval = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.ReviewWallSwitch = params.get("ReviewWallSwitch")
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
        if params.get("UserDefineConfigure") is not None:
            self.UserDefineConfigure = UserDefineConfigureInfo()
            self.UserDefineConfigure._deserialize(params.get("UserDefineConfigure"))
        self.ScreenshotInterval = params.get("ScreenshotInterval")
        self.SubAppId = params.get("SubAppId")


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


class CreateImageSpriteTask2017(AbstractModel):
    """視訊截取雪碧圖任務，該結構僅用於對 2017 版[截取雪碧圖](https://cloud.taifucloud.com/document/product/266/8101)介面發起的任務。

    """

    def __init__(self):
        """
        :param TaskId: 截圖雪碧圖任務 ID。
        :type TaskId: str
        :param ErrCode: 錯誤碼
<li>0：成功；</li>
<li>其他值：失敗。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 錯誤訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param FileId: 截取雪碧圖文件 ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileId: str
        :param Definition: 雪碧圖規格，參見[雪碧圖截圖範本](https://cloud.taifucloud.com/document/product/266/33480#.E9.9B.AA.E7.A2.A7.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Definition: int
        :param TotalCount: 雪碧圖小圖總數量。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param ImageSpriteUrlSet: 截取雪碧圖輸出的網址。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ImageSpriteUrlSet: list of str
        :param WebVttUrl: 雪碧圖子圖位置與時間關系 WebVtt 文件網址。
注意：此欄位可能返回 null，表示取不到有效值。
        :type WebVttUrl: str
        """
        self.TaskId = None
        self.ErrCode = None
        self.Message = None
        self.FileId = None
        self.Definition = None
        self.TotalCount = None
        self.ImageSpriteUrlSet = None
        self.WebVttUrl = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.FileId = params.get("FileId")
        self.Definition = params.get("Definition")
        self.TotalCount = params.get("TotalCount")
        self.ImageSpriteUrlSet = params.get("ImageSpriteUrlSet")
        self.WebVttUrl = params.get("WebVttUrl")


class CreatePersonSampleRequest(AbstractModel):
    """CreatePersonSample請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 人物名稱，長度限制：20 個字元。
        :type Name: str
        :param FaceContents: 人臉圖片 [Base64](https://tools.ietf.org/html/rfc4648) 編碼後的字串，僅支援 jpeg、png 圖片格式。數組長度限制：5 張圖片。
注意：圖片必須是單人像正面人臉較清晰的照片，像素不低於 200*200。
        :type FaceContents: list of str
        :param Usages: 人物應用場景，可選值：
1. Recognition：用於内容識别，等價於 Recognition.Face。
2. Review：用於内容審核，等價於 Review.Face。
3. All：用於内容識别、内容審核，等價於 1+2。
        :type Usages: list of str
        :param Description: 人物描述，長度限制：1024 個字元。
        :type Description: str
        :param Tags: 人物標簽
<li>數組長度限制：20 個標簽；</li>
<li>單個標簽長度限制：128 個字元。</li>
        :type Tags: list of str
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Name = None
        self.FaceContents = None
        self.Usages = None
        self.Description = None
        self.Tags = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.FaceContents = params.get("FaceContents")
        self.Usages = params.get("Usages")
        self.Description = params.get("Description")
        self.Tags = params.get("Tags")
        self.SubAppId = params.get("SubAppId")


class CreatePersonSampleResponse(AbstractModel):
    """CreatePersonSample返回參數結構體

    """

    def __init__(self):
        """
        :param Person: 人物訊息。
        :type Person: :class:`taifucloudcloud.vod.v20180717.models.AiSamplePerson`
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


class CreateProcedureTemplateRequest(AbstractModel):
    """CreateProcedureTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 任務流名字（支援中文，不超過20個字）。
        :type Name: str
        :param MediaProcessTask: 視訊處理類型任務參數。
        :type MediaProcessTask: :class:`taifucloudcloud.vod.v20180717.models.MediaProcessTaskInput`
        :param AiContentReviewTask: AI 智慧内容審核類型任務參數。
        :type AiContentReviewTask: :class:`taifucloudcloud.vod.v20180717.models.AiContentReviewTaskInput`
        :param AiAnalysisTask: AI 智慧内容分析類型任務參數。
        :type AiAnalysisTask: :class:`taifucloudcloud.vod.v20180717.models.AiAnalysisTaskInput`
        :param AiRecognitionTask: AI 内容識别類型任務參數。
        :type AiRecognitionTask: :class:`taifucloudcloud.vod.v20180717.models.AiRecognitionTaskInput`
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Name = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
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
        self.SubAppId = params.get("SubAppId")


class CreateProcedureTemplateResponse(AbstractModel):
    """CreateProcedureTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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
        :type VideoTemplate: :class:`taifucloudcloud.vod.v20180717.models.VideoTemplateInfo`
        :param AudioTemplate: 音訊流配置參數，當 RemoveAudio 爲 0，該欄位必填。
        :type AudioTemplate: :class:`taifucloudcloud.vod.v20180717.models.AudioTemplateInfo`
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Container = None
        self.Name = None
        self.Comment = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.SubAppId = None


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
        self.SubAppId = params.get("SubAppId")


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
<li>text：文字浮水印。</li>
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
預設值：TopLeft。目前，當 Type 爲 image，該欄位僅支援 TopLeft。
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
        :type ImageTemplate: :class:`taifucloudcloud.vod.v20180717.models.ImageWatermarkInput`
        :param TextTemplate: 文字浮水印範本，當 Type 爲 text，該欄位必填。當 Type 爲 image，該欄位無效。
        :type TextTemplate: :class:`taifucloudcloud.vod.v20180717.models.TextWatermarkTemplateInput`
        :param SvgTemplate: SVG浮水印範本，當 Type 爲 svg，該欄位必填。當 Type 爲 image 或 text，該欄位無效。
        :type SvgTemplate: :class:`taifucloudcloud.vod.v20180717.models.SvgWatermarkInput`
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
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
        self.SubAppId = None


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
        self.SubAppId = params.get("SubAppId")


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
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Usages = None
        self.Words = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Usages = params.get("Usages")
        if params.get("Words") is not None:
            self.Words = []
            for item in params.get("Words"):
                obj = AiSampleWordInfo()
                obj._deserialize(item)
                self.Words.append(obj)
        self.SubAppId = params.get("SubAppId")


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


class DeleteAIAnalysisTemplateRequest(AbstractModel):
    """DeleteAIAnalysisTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Definition: 視訊内容分析範本唯一標識。
        :type Definition: int
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Definition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SubAppId = params.get("SubAppId")


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
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Definition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SubAppId = params.get("SubAppId")


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


class DeleteClassRequest(AbstractModel):
    """DeleteClass請求參數結構體

    """

    def __init__(self):
        """
        :param ClassId: 分類 ID
        :type ClassId: int
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.ClassId = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.ClassId = params.get("ClassId")
        self.SubAppId = params.get("SubAppId")


class DeleteClassResponse(AbstractModel):
    """DeleteClass返回參數結構體

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
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Definition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SubAppId = params.get("SubAppId")


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


class DeleteMediaRequest(AbstractModel):
    """DeleteMedia請求參數結構體

    """

    def __init__(self):
        """
        :param FileId: 媒體文件的唯一標識。
        :type FileId: str
        :param DeleteParts: 指定本次需要删除的部分。預設值爲 "[]", 表示删除媒體及其對應的全部視訊處理文件。
        :type DeleteParts: list of MediaDeleteItem
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID 。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.FileId = None
        self.DeleteParts = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        if params.get("DeleteParts") is not None:
            self.DeleteParts = []
            for item in params.get("DeleteParts"):
                obj = MediaDeleteItem()
                obj._deserialize(item)
                self.DeleteParts.append(obj)
        self.SubAppId = params.get("SubAppId")


class DeleteMediaResponse(AbstractModel):
    """DeleteMedia返回參數結構體

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
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.PersonId = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.SubAppId = params.get("SubAppId")


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


class DeleteProcedureTemplateRequest(AbstractModel):
    """DeleteProcedureTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 任務流名字。
        :type Name: str
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Name = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.SubAppId = params.get("SubAppId")


class DeleteProcedureTemplateResponse(AbstractModel):
    """DeleteProcedureTemplate返回參數結構體

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
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Definition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SubAppId = params.get("SubAppId")


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
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Definition = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SubAppId = params.get("SubAppId")


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
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Keywords = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Keywords = params.get("Keywords")
        self.SubAppId = params.get("SubAppId")


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
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubAppId = params.get("SubAppId")


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
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubAppId = params.get("SubAppId")


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


class DescribeAllClassRequest(AbstractModel):
    """DescribeAllClass請求參數結構體

    """

    def __init__(self):
        """
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.SubAppId = None


    def _deserialize(self, params):
        self.SubAppId = params.get("SubAppId")


class DescribeAllClassResponse(AbstractModel):
    """DescribeAllClass返回參數結構體

    """

    def __init__(self):
        """
        :param ClassInfoSet: 分類訊息集合
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClassInfoSet: list of MediaClassInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ClassInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClassInfoSet") is not None:
            self.ClassInfoSet = []
            for item in params.get("ClassInfoSet"):
                obj = MediaClassInfo()
                obj._deserialize(item)
                self.ClassInfoSet.append(obj)
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
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubAppId = params.get("SubAppId")


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


class DescribeMediaInfosRequest(AbstractModel):
    """DescribeMediaInfos請求參數結構體

    """

    def __init__(self):
        """
        :param FileIds: 媒體文件 ID 清單，N 從 0 開始取值，最大 19。
        :type FileIds: list of str
        :param Filters: 指定所有媒體文件需要返回的訊息，可同時指定多個訊息，N 從 0 開始遞增。如果未填寫該欄位，預設返回所有訊息。選項有：
<li>basicInfo（視訊基礎訊息）。</li>
<li>metaData（視訊元訊息）。</li>
<li>transcodeInfo（視訊轉碼結果訊息）。</li>
<li>animatedGraphicsInfo（視訊轉動圖結果訊息）。</li>
<li>imageSpriteInfo（視訊雪碧圖訊息）。</li>
<li>snapshotByTimeOffsetInfo（視訊指定時間點截圖訊息）。</li>
<li>sampleSnapshotInfo（采樣截圖訊息）。</li>
<li>keyFrameDescInfo（打點訊息）。</li>
<li>adaptiveDynamicStreamingInfo（轉自适應碼流訊息）。</li>
        :type Filters: list of str
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID 。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.FileIds = None
        self.Filters = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.FileIds = params.get("FileIds")
        self.Filters = params.get("Filters")
        self.SubAppId = params.get("SubAppId")


class DescribeMediaInfosResponse(AbstractModel):
    """DescribeMediaInfos返回參數結構體

    """

    def __init__(self):
        """
        :param MediaInfoSet: 媒體文件訊息清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type MediaInfoSet: list of MediaInfo
        :param NotExistFileIdSet: 不存在的文件 ID 清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type NotExistFileIdSet: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.MediaInfoSet = None
        self.NotExistFileIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MediaInfoSet") is not None:
            self.MediaInfoSet = []
            for item in params.get("MediaInfoSet"):
                obj = MediaInfo()
                obj._deserialize(item)
                self.MediaInfoSet.append(obj)
        self.NotExistFileIdSet = params.get("NotExistFileIdSet")
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
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Type = None
        self.PersonIds = None
        self.Names = None
        self.Tags = None
        self.Offset = None
        self.Limit = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.PersonIds = params.get("PersonIds")
        self.Names = params.get("Names")
        self.Tags = params.get("Tags")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubAppId = params.get("SubAppId")


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


class DescribeProcedureTemplatesRequest(AbstractModel):
    """DescribeProcedureTemplates請求參數結構體

    """

    def __init__(self):
        """
        :param Names: 任務流範本名字過濾條件，數組長度限制：100。
        :type Names: list of str
        :param Offset: 分頁偏移量，預設值：0。
        :type Offset: int
        :param Limit: 返回記錄條數，預設值：10，最大值：100。
        :type Limit: int
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Names = None
        self.Offset = None
        self.Limit = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Names = params.get("Names")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubAppId = params.get("SubAppId")


class DescribeProcedureTemplatesResponse(AbstractModel):
    """DescribeProcedureTemplates返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合過濾條件的記錄總數。
        :type TotalCount: int
        :param ProcedureTemplateSet: 任務流範本詳情清單。
        :type ProcedureTemplateSet: list of ProcedureTemplate
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ProcedureTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ProcedureTemplateSet") is not None:
            self.ProcedureTemplateSet = []
            for item in params.get("ProcedureTemplateSet"):
                obj = ProcedureTemplate()
                obj._deserialize(item)
                self.ProcedureTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskDetailRequest(AbstractModel):
    """DescribeTaskDetail請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 視訊處理任務的任務 ID。
        :type TaskId: str
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.TaskId = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.SubAppId = params.get("SubAppId")


class DescribeTaskDetailResponse(AbstractModel):
    """DescribeTaskDetail返回參數結構體

    """

    def __init__(self):
        """
        :param TaskType: 任務類型，取值：
<li>Procedure：視訊處理任務；</li>
<li>EditMedia：視訊編輯任務；</li>
<li>WechatPublish： 發布任務。</li>
兼容 2017 版的任務類型：
<li>Transcode：視訊轉碼任務；</li>
<li>SnapshotByTimeOffset：視訊截圖任務；</li>
<li>Concat：視訊拼接任務；</li>
<li>Clip：視訊剪輯任務；</li>
<li>ImageSprites：截取雪碧圖任務。</li>
        :type TaskType: str
        :param Status: 任務狀态，取值：
<li>WAITING：等待中；</li>
<li>PROCESSING：處理中；</li>
<li>FINISH：已完成。</li>
        :type Status: str
        :param CreateTime: 任務的創建時間，采用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type CreateTime: str
        :param BeginProcessTime: 任務開始執行的時間，采用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type BeginProcessTime: str
        :param FinishTime: 任務執行完畢的時間，采用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type FinishTime: str
        :param ProcedureTask: 視訊處理任務訊息，僅當 TaskType 爲 Procedure，該欄位有值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProcedureTask: :class:`taifucloudcloud.vod.v20180717.models.ProcedureTask`
        :param EditMediaTask: 視訊編輯任務訊息，僅當 TaskType 爲 EditMedia，該欄位有值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type EditMediaTask: :class:`taifucloudcloud.vod.v20180717.models.EditMediaTask`
        :param WechatPublishTask:  發布任務訊息，僅當 TaskType 爲 WechatPublish，該欄位有值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type WechatPublishTask: :class:`taifucloudcloud.vod.v20180717.models.WechatPublishTask`
        :param TranscodeTask: 視訊轉碼任務訊息，僅當 TaskType 爲 Transcode，該欄位有值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranscodeTask: :class:`taifucloudcloud.vod.v20180717.models.TranscodeTask2017`
        :param SnapshotByTimeOffsetTask: 視訊指定時間點截圖任務訊息，僅當 TaskType 爲 SnapshotByTimeOffset，該欄位有值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SnapshotByTimeOffsetTask: :class:`taifucloudcloud.vod.v20180717.models.SnapshotByTimeOffsetTask2017`
        :param ConcatTask: 視訊拼接任務訊息，僅當 TaskType 爲 Concat，該欄位有值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConcatTask: :class:`taifucloudcloud.vod.v20180717.models.ConcatTask2017`
        :param ClipTask: 視訊剪輯任務訊息，僅當 TaskType 爲 Clip，該欄位有值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClipTask: :class:`taifucloudcloud.vod.v20180717.models.ClipTask2017`
        :param CreateImageSpriteTask: 截取雪碧圖任務訊息，僅當 TaskType 爲 ImageSprite，該欄位有值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateImageSpriteTask: :class:`taifucloudcloud.vod.v20180717.models.CreateImageSpriteTask2017`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskType = None
        self.Status = None
        self.CreateTime = None
        self.BeginProcessTime = None
        self.FinishTime = None
        self.ProcedureTask = None
        self.EditMediaTask = None
        self.WechatPublishTask = None
        self.TranscodeTask = None
        self.SnapshotByTimeOffsetTask = None
        self.ConcatTask = None
        self.ClipTask = None
        self.CreateImageSpriteTask = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.BeginProcessTime = params.get("BeginProcessTime")
        self.FinishTime = params.get("FinishTime")
        if params.get("ProcedureTask") is not None:
            self.ProcedureTask = ProcedureTask()
            self.ProcedureTask._deserialize(params.get("ProcedureTask"))
        if params.get("EditMediaTask") is not None:
            self.EditMediaTask = EditMediaTask()
            self.EditMediaTask._deserialize(params.get("EditMediaTask"))
        if params.get("WechatPublishTask") is not None:
            self.WechatPublishTask = WechatPublishTask()
            self.WechatPublishTask._deserialize(params.get("WechatPublishTask"))
        if params.get("TranscodeTask") is not None:
            self.TranscodeTask = TranscodeTask2017()
            self.TranscodeTask._deserialize(params.get("TranscodeTask"))
        if params.get("SnapshotByTimeOffsetTask") is not None:
            self.SnapshotByTimeOffsetTask = SnapshotByTimeOffsetTask2017()
            self.SnapshotByTimeOffsetTask._deserialize(params.get("SnapshotByTimeOffsetTask"))
        if params.get("ConcatTask") is not None:
            self.ConcatTask = ConcatTask2017()
            self.ConcatTask._deserialize(params.get("ConcatTask"))
        if params.get("ClipTask") is not None:
            self.ClipTask = ClipTask2017()
            self.ClipTask._deserialize(params.get("ClipTask"))
        if params.get("CreateImageSpriteTask") is not None:
            self.CreateImageSpriteTask = CreateImageSpriteTask2017()
            self.CreateImageSpriteTask._deserialize(params.get("CreateImageSpriteTask"))
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks請求參數結構體

    """

    def __init__(self):
        """
        :param Status: 過濾條件：任務狀态，可選值：WAITING（等待中）、PROCESSING（處理中）、FINISH（已完成）。
        :type Status: str
        :param FileId: 過濾條件：文件 ID。
        :type FileId: str
        :param Limit: 返回記錄條數，預設值：10，最大值：100。
        :type Limit: int
        :param ScrollToken: 翻頁標識，分批拉取時使用：當單次請求無法拉取所有數據，介面将會返回 ScrollToken，下一次請求攜帶該 Token，将會從下一條記錄開始獲取。
        :type ScrollToken: str
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Status = None
        self.FileId = None
        self.Limit = None
        self.ScrollToken = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.FileId = params.get("FileId")
        self.Limit = params.get("Limit")
        self.ScrollToken = params.get("ScrollToken")
        self.SubAppId = params.get("SubAppId")


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回參數結構體

    """

    def __init__(self):
        """
        :param TaskSet: 任務概要清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TaskSet: list of TaskSimpleInfo
        :param ScrollToken: 翻頁標識，當請求未返回所有數據，該欄位表示下一條記錄的 ID。當該欄位爲空，說明已無更多數據。
注意：此欄位可能返回 null，表示取不到有效值。
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
        :param Offset: 分頁偏移量，預設值：0。
        :type Offset: int
        :param Limit: 返回記錄條數，預設值：10，最大值：100。
        :type Limit: int
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Definitions = None
        self.Type = None
        self.ContainerType = None
        self.Offset = None
        self.Limit = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Type = params.get("Type")
        self.ContainerType = params.get("ContainerType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubAppId = params.get("SubAppId")


class DescribeTranscodeTemplatesResponse(AbstractModel):
    """DescribeTranscodeTemplates返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合過濾條件的記錄總數。
        :type TotalCount: int
        :param TranscodeTemplateSet: 轉碼範本詳情清單。
注意：此欄位可能返回 null，表示取不到有效值。
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
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Definitions = None
        self.Type = None
        self.Offset = None
        self.Limit = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Type = params.get("Type")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubAppId = params.get("SubAppId")


class DescribeWatermarkTemplatesResponse(AbstractModel):
    """DescribeWatermarkTemplates返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合過濾條件的記錄總數。
        :type TotalCount: int
        :param WatermarkTemplateSet: 浮水印範本詳情清單。
注意：此欄位可能返回 null，表示取不到有效值。
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
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Usages = None
        self.Keywords = None
        self.Tags = None
        self.Offset = None
        self.Limit = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Usages = params.get("Usages")
        self.Keywords = params.get("Keywords")
        self.Tags = params.get("Tags")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubAppId = params.get("SubAppId")


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


class EditMediaFileInfo(AbstractModel):
    """編輯點播視訊文件訊息

    """

    def __init__(self):
        """
        :param FileId: 視訊的 ID。
        :type FileId: str
        :param StartTimeOffset: 視訊剪輯的起始偏移時間偏移，單位：秒。
注意：此欄位可能返回 null，表示取不到有效值。
        :type StartTimeOffset: float
        :param EndTimeOffset: 視訊剪輯的起始結束時間偏移，單位：秒。
注意：此欄位可能返回 null，表示取不到有效值。
        :type EndTimeOffset: float
        """
        self.FileId = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")


class EditMediaRequest(AbstractModel):
    """EditMedia請求參數結構體

    """

    def __init__(self):
        """
        :param InputType: 輸入視訊的類型，可以取的值爲  File，Stream 兩種。
        :type InputType: str
        :param FileInfos: 輸入的視訊文件訊息，當 InputType 爲 File 時必填。
        :type FileInfos: list of EditMediaFileInfo
        :param StreamInfos: 輸入的流訊息，當 InputType 爲 Stream 時必填。
        :type StreamInfos: list of EditMediaStreamInfo
        :param ProcedureName: [任務流範本](/document/product/266/11700#.E4.BB.BB.E5.8A.A1.E6.B5.81.E6.A8.A1.E6.9D.BF)名字，如果要對生成的新視訊執行任務流時填寫。
        :type ProcedureName: str
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.InputType = None
        self.FileInfos = None
        self.StreamInfos = None
        self.ProcedureName = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.InputType = params.get("InputType")
        if params.get("FileInfos") is not None:
            self.FileInfos = []
            for item in params.get("FileInfos"):
                obj = EditMediaFileInfo()
                obj._deserialize(item)
                self.FileInfos.append(obj)
        if params.get("StreamInfos") is not None:
            self.StreamInfos = []
            for item in params.get("StreamInfos"):
                obj = EditMediaStreamInfo()
                obj._deserialize(item)
                self.StreamInfos.append(obj)
        self.ProcedureName = params.get("ProcedureName")
        self.SubAppId = params.get("SubAppId")


class EditMediaResponse(AbstractModel):
    """EditMedia返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 編輯視訊的任務 ID，可以通過該 ID 查詢編輯任務（任務類型爲 EditMedia）的狀态。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class EditMediaStreamInfo(AbstractModel):
    """編輯視訊流訊息

    """

    def __init__(self):
        """
        :param StreamId: 錄制的流 ID
        :type StreamId: str
        :param StartTime: 流剪輯的起始時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
注意：此欄位可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 流剪輯的結束時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
注意：此欄位可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self.StreamId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.StreamId = params.get("StreamId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class EditMediaTask(AbstractModel):
    """編輯視訊任務訊息

    """

    def __init__(self):
        """
        :param TaskId: 任務 ID。
        :type TaskId: str
        :param Status: 任務流狀态，取值：
<li>PROCESSING：處理中；</li>
<li>FINISH：已完成。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: str
        :param ErrCode: 錯誤碼
<li>0：成功；</li>
<li>其他值：失敗。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 錯誤訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 視訊編輯任務的輸入。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Input: :class:`taifucloudcloud.vod.v20180717.models.EditMediaTaskInput`
        :param Output: 視訊編輯任務的輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.EditMediaTaskOutput`
        :param ProcedureTaskId: 若發起視訊編輯任務時指定了視訊處理流程，則該欄位爲流程任務 ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProcedureTaskId: str
        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None
        self.ProcedureTaskId = None


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
        self.ProcedureTaskId = params.get("ProcedureTaskId")


class EditMediaTaskInput(AbstractModel):
    """編輯視訊任務的輸入。

    """

    def __init__(self):
        """
        :param InputType: 輸入視訊的來源類型，可以取的值爲 File，Stream 兩種。
        :type InputType: str
        :param FileInfoSet: 輸入的視訊文件訊息，當 InputType 爲 File 時，該欄位有值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileInfoSet: list of EditMediaFileInfo
        :param StreamInfoSet: 輸入的流訊息，當 InputType 爲 Stream 時，該欄位有值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type StreamInfoSet: list of EditMediaStreamInfo
        """
        self.InputType = None
        self.FileInfoSet = None
        self.StreamInfoSet = None


    def _deserialize(self, params):
        self.InputType = params.get("InputType")
        if params.get("FileInfoSet") is not None:
            self.FileInfoSet = []
            for item in params.get("FileInfoSet"):
                obj = EditMediaFileInfo()
                obj._deserialize(item)
                self.FileInfoSet.append(obj)
        if params.get("StreamInfoSet") is not None:
            self.StreamInfoSet = []
            for item in params.get("StreamInfoSet"):
                obj = EditMediaStreamInfo()
                obj._deserialize(item)
                self.StreamInfoSet.append(obj)


class EditMediaTaskOutput(AbstractModel):
    """編輯視訊任務的輸出

    """

    def __init__(self):
        """
        :param FileType: 文件類型，例如 mp4、flv 等。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileType: str
        :param FileId: 媒體文件 ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileId: str
        :param FileUrl: 媒體文件播放網址。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileUrl: str
        """
        self.FileType = None
        self.FileId = None
        self.FileUrl = None


    def _deserialize(self, params):
        self.FileType = params.get("FileType")
        self.FileId = params.get("FileId")
        self.FileUrl = params.get("FileUrl")


class EmptyTrackItem(AbstractModel):
    """空的軌道片段，用來進行時間軸的占位。如需要兩個音訊片段之間有一段時間的靜音，可以用 EmptyTrackItem 來進行占位。

    """

    def __init__(self):
        """
        :param Duration: 持續時間，單位爲秒。
        :type Duration: float
        """
        self.Duration = None


    def _deserialize(self, params):
        self.Duration = params.get("Duration")


class EventContent(AbstractModel):
    """事件通知内容，其中，TranscodeCompleteEvent、ConcatCompleteEvent、ClipCompleteEvent、CreateImageSpriteCompleteEvent、SnapshotByTimeOffsetCompleteEvent 爲兼容 2017 版介面發起任務的事件通知。

    """

    def __init__(self):
        """
        :param EventHandle: 事件句柄，調用方必須調用 ConfirmEvents 來确認訊息已經收到，确認有效時間 30 秒。失效後，事件可重新被獲取。
        :type EventHandle: str
        :param EventType: <b>支援事件類型：</b>
<li>NewFileUpload：視訊上傳完成；</li>
<li>ProcedureStateChanged：任務流狀态變更；</li>
<li>FileDeleted：視訊删除完成；</li>
<li>PullComplete：視訊轉拉完成；</li>
<li>EditMediaComplete：視訊編輯完成；</li>
<li>WechatPublishComplete： 發布完成；</li>
<li>ComposeMediaComplete：制作媒體文件完成；</li>
<li>WechatMiniProgramPublishComplete： 小程式發布完成。</li>
<b>兼容 2017 版的事件類型：</b>
<li>TranscodeComplete：視訊轉碼完成；</li>
<li>ConcatComplete：視訊拼接完成；</li>
<li>ClipComplete：視訊剪輯完成；</li>
<li>CreateImageSpriteComplete：視訊截取雪碧圖完成；</li>
<li>CreateSnapshotByTimeOffsetComplete：視訊按時間點截圖完成。</li>
        :type EventType: str
        :param FileUploadEvent: 視訊上傳完成事件，當事件類型爲 NewFileUpload 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileUploadEvent: :class:`taifucloudcloud.vod.v20180717.models.FileUploadTask`
        :param ProcedureStateChangeEvent: 任務流狀态變更事件，當事件類型爲 ProcedureStateChanged 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProcedureStateChangeEvent: :class:`taifucloudcloud.vod.v20180717.models.ProcedureTask`
        :param FileDeleteEvent: 文件删除事件，當事件類型爲 FileDeleted 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileDeleteEvent: :class:`taifucloudcloud.vod.v20180717.models.FileDeleteTask`
        :param PullCompleteEvent: 視訊轉拉完成事件，當事件類型爲 PullComplete 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PullCompleteEvent: :class:`taifucloudcloud.vod.v20180717.models.PullFileTask`
        :param EditMediaCompleteEvent: 視訊編輯完成事件，當事件類型爲 EditMediaComplete 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type EditMediaCompleteEvent: :class:`taifucloudcloud.vod.v20180717.models.EditMediaTask`
        :param WechatPublishCompleteEvent:  發布完成事件，當事件類型爲 WechatPublishComplete 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type WechatPublishCompleteEvent: :class:`taifucloudcloud.vod.v20180717.models.WechatPublishTask`
        :param TranscodeCompleteEvent: 視訊轉碼完成事件，當事件類型爲 TranscodeComplete 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranscodeCompleteEvent: :class:`taifucloudcloud.vod.v20180717.models.TranscodeTask2017`
        :param ConcatCompleteEvent: 視訊拼接完成事件，當事件類型爲 ConcatComplete 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ConcatCompleteEvent: :class:`taifucloudcloud.vod.v20180717.models.ConcatTask2017`
        :param ClipCompleteEvent: 視訊剪輯完成事件，當事件類型爲 ClipComplete 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClipCompleteEvent: :class:`taifucloudcloud.vod.v20180717.models.ClipTask2017`
        :param CreateImageSpriteCompleteEvent: 視訊截取雪碧圖完成事件，當事件類型爲 CreateImageSpriteComplete 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateImageSpriteCompleteEvent: :class:`taifucloudcloud.vod.v20180717.models.CreateImageSpriteTask2017`
        :param SnapshotByTimeOffsetCompleteEvent: 視訊按時間點截圖完成事件，當事件類型爲 CreateSnapshotByTimeOffsetComplete 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SnapshotByTimeOffsetCompleteEvent: :class:`taifucloudcloud.vod.v20180717.models.SnapshotByTimeOffsetTask2017`
        :param ComposeMediaCompleteEvent: 制作媒體文件任務完成事件，當事件類型爲 ComposeMediaComplete 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ComposeMediaCompleteEvent: :class:`taifucloudcloud.vod.v20180717.models.ComposeMediaTask`
        :param WechatMiniProgramPublishEvent:  小程式視訊發布完成事件，當事件類型爲 WechatMiniProgramPublishComplete 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type WechatMiniProgramPublishEvent: :class:`taifucloudcloud.vod.v20180717.models.WechatMiniProgramPublishTask`
        """
        self.EventHandle = None
        self.EventType = None
        self.FileUploadEvent = None
        self.ProcedureStateChangeEvent = None
        self.FileDeleteEvent = None
        self.PullCompleteEvent = None
        self.EditMediaCompleteEvent = None
        self.WechatPublishCompleteEvent = None
        self.TranscodeCompleteEvent = None
        self.ConcatCompleteEvent = None
        self.ClipCompleteEvent = None
        self.CreateImageSpriteCompleteEvent = None
        self.SnapshotByTimeOffsetCompleteEvent = None
        self.ComposeMediaCompleteEvent = None
        self.WechatMiniProgramPublishEvent = None


    def _deserialize(self, params):
        self.EventHandle = params.get("EventHandle")
        self.EventType = params.get("EventType")
        if params.get("FileUploadEvent") is not None:
            self.FileUploadEvent = FileUploadTask()
            self.FileUploadEvent._deserialize(params.get("FileUploadEvent"))
        if params.get("ProcedureStateChangeEvent") is not None:
            self.ProcedureStateChangeEvent = ProcedureTask()
            self.ProcedureStateChangeEvent._deserialize(params.get("ProcedureStateChangeEvent"))
        if params.get("FileDeleteEvent") is not None:
            self.FileDeleteEvent = FileDeleteTask()
            self.FileDeleteEvent._deserialize(params.get("FileDeleteEvent"))
        if params.get("PullCompleteEvent") is not None:
            self.PullCompleteEvent = PullFileTask()
            self.PullCompleteEvent._deserialize(params.get("PullCompleteEvent"))
        if params.get("EditMediaCompleteEvent") is not None:
            self.EditMediaCompleteEvent = EditMediaTask()
            self.EditMediaCompleteEvent._deserialize(params.get("EditMediaCompleteEvent"))
        if params.get("WechatPublishCompleteEvent") is not None:
            self.WechatPublishCompleteEvent = WechatPublishTask()
            self.WechatPublishCompleteEvent._deserialize(params.get("WechatPublishCompleteEvent"))
        if params.get("TranscodeCompleteEvent") is not None:
            self.TranscodeCompleteEvent = TranscodeTask2017()
            self.TranscodeCompleteEvent._deserialize(params.get("TranscodeCompleteEvent"))
        if params.get("ConcatCompleteEvent") is not None:
            self.ConcatCompleteEvent = ConcatTask2017()
            self.ConcatCompleteEvent._deserialize(params.get("ConcatCompleteEvent"))
        if params.get("ClipCompleteEvent") is not None:
            self.ClipCompleteEvent = ClipTask2017()
            self.ClipCompleteEvent._deserialize(params.get("ClipCompleteEvent"))
        if params.get("CreateImageSpriteCompleteEvent") is not None:
            self.CreateImageSpriteCompleteEvent = CreateImageSpriteTask2017()
            self.CreateImageSpriteCompleteEvent._deserialize(params.get("CreateImageSpriteCompleteEvent"))
        if params.get("SnapshotByTimeOffsetCompleteEvent") is not None:
            self.SnapshotByTimeOffsetCompleteEvent = SnapshotByTimeOffsetTask2017()
            self.SnapshotByTimeOffsetCompleteEvent._deserialize(params.get("SnapshotByTimeOffsetCompleteEvent"))
        if params.get("ComposeMediaCompleteEvent") is not None:
            self.ComposeMediaCompleteEvent = ComposeMediaTask()
            self.ComposeMediaCompleteEvent._deserialize(params.get("ComposeMediaCompleteEvent"))
        if params.get("WechatMiniProgramPublishEvent") is not None:
            self.WechatMiniProgramPublishEvent = WechatMiniProgramPublishTask()
            self.WechatMiniProgramPublishEvent._deserialize(params.get("WechatMiniProgramPublishEvent"))


class FaceConfigureInfo(AbstractModel):
    """人臉識别任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 人臉識别任務開關，可選值：
<li>ON：開啓智慧人臉識别任務；</li>
<li>OFF：關閉智慧人臉識别任務。</li>
        :type Switch: str
        :param Score: 人臉識别過濾分數，當識别結果達到該分數以上，返回識别結果。預設 90 分。取值範圍：0 - 100。
        :type Score: float
        :param DefaultLibraryLabelSet: 預設人物過濾標簽，指定需要返回的預設人物的標簽。如果未填或者爲空，則全部預設人物結果都返回。標簽可選值：
<li>entertainments：娛樂明星；</li>
<li>sports：體育明星；</li>
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
<li>entertainments：娛樂明星；</li>
<li>sports：體育明星；</li>
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


class FileDeleteTask(AbstractModel):
    """文件删除任務

    """

    def __init__(self):
        """
        :param FileIdSet: 删除文件 ID 清單。
        :type FileIdSet: list of str
        """
        self.FileIdSet = None


    def _deserialize(self, params):
        self.FileIdSet = params.get("FileIdSet")


class FileUploadTask(AbstractModel):
    """文件上傳任務訊息

    """

    def __init__(self):
        """
        :param FileId: 文件唯一 ID。
        :type FileId: str
        :param MediaBasicInfo: 上傳完成後生成的媒體文件基礎訊息。
        :type MediaBasicInfo: :class:`taifucloudcloud.vod.v20180717.models.MediaBasicInfo`
        :param ProcedureTaskId: 若視訊上傳時指定了視訊處理流程，則該欄位爲流程任務 ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProcedureTaskId: str
        """
        self.FileId = None
        self.MediaBasicInfo = None
        self.ProcedureTaskId = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        if params.get("MediaBasicInfo") is not None:
            self.MediaBasicInfo = MediaBasicInfo()
            self.MediaBasicInfo._deserialize(params.get("MediaBasicInfo"))
        self.ProcedureTaskId = params.get("ProcedureTaskId")


class FrameTagConfigureInfo(AbstractModel):
    """智慧按幀標簽任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 智慧按幀標簽任務開關，可選值：
<li>ON：開啓智慧按幀標簽任務；</li>
<li>OFF：關閉智慧按幀標簽任務。</li>
        :type Switch: str
        :param ScreenshotInterval: 截幀間隔，單位爲秒，當不填時，預設截幀間隔爲 1 秒，最小值爲 0.5 秒。
        :type ScreenshotInterval: float
        """
        self.Switch = None
        self.ScreenshotInterval = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.ScreenshotInterval = params.get("ScreenshotInterval")


class FrameTagConfigureInfoForUpdate(AbstractModel):
    """智慧按幀標簽任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 智慧按幀標簽任務開關，可選值：
<li>ON：開啓智慧按幀標簽任務；</li>
<li>OFF：關閉智慧按幀標簽任務。</li>
        :type Switch: str
        :param ScreenshotInterval: 截幀間隔，單位爲秒，最小值爲 0.5 秒。
        :type ScreenshotInterval: float
        """
        self.Switch = None
        self.ScreenshotInterval = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.ScreenshotInterval = params.get("ScreenshotInterval")


class HeadTailConfigureInfo(AbstractModel):
    """視訊片頭片尾識别任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 視訊片頭片尾識别任務開關，可選值：
<li>ON：開啓智慧視訊片頭片尾識别任務；</li>
<li>OFF：關閉智慧視訊片頭片尾識别任務。</li>
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")


class HeadTailConfigureInfoForUpdate(AbstractModel):
    """視訊片頭片尾識别任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 視訊片頭片尾識别任務開關，可選值：
<li>ON：開啓智慧視訊片頭片尾識别任務；</li>
<li>OFF：關閉智慧視訊片頭片尾識别任務。</li>
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
        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")


class ImageTransform(AbstractModel):
    """圖像旋轉、翻轉等操作

    """

    def __init__(self):
        """
        :param Type: 類型，取值有：
<li> Rotate：圖像旋轉。</li>
<li> Flip：圖像翻轉。</li>
        :type Type: str
        :param RotateAngle: 圖像以中心點爲原點進行旋轉的角度，取值範圍0~360。當 Type = Rotate 時有效。
        :type RotateAngle: float
        :param Flip: 圖像翻轉動作，取值有：
<li>Horizental：水平翻轉，即左右映像。</li>
<li>Vertical：垂直翻轉，即上下映像。</li>
當 Type = Flip 時有效。
        :type Flip: str
        """
        self.Type = None
        self.RotateAngle = None
        self.Flip = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.RotateAngle = params.get("RotateAngle")
        self.Flip = params.get("Flip")


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
<li>當字串以 px 結尾，表示浮水印 Width 單位爲像素，如 100px 表示 Width 爲 100 像素。</li>
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


class LiveRealTimeClipRequest(AbstractModel):
    """LiveRealTimeClip請求參數結構體

    """

    def __init__(self):
        """
        :param StreamId: 推流[直播碼](https://cloud.taifucloud.com/document/product/267/5959)。
        :type StreamId: str
        :param StartTime: 流剪輯的開始時間，格式參照 [ISO 日期格式說明](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type StartTime: str
        :param EndTime: 流剪輯的結束時間，格式參照 [ISO 日期格式說明](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type EndTime: str
        :param IsPersistence: 是否固化。0 不固化，1 固化。預設不固化。
        :type IsPersistence: int
        :param ExpireTime: 剪輯固化後的視訊儲存過期時間。格式參照 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。填“9999-12-31T23:59:59Z”表示永不過期。過期後該媒體文件及其相關資源（轉碼結果、雪碧圖等）将被永久删除。僅 IsPersistence 爲 1 時有效，預設剪輯固化的視訊永不過期。
        :type ExpireTime: str
        :param Procedure: 剪輯固化後的視訊點播任務流處理，詳見[上傳指定任務流](https://cloud.taifucloud.com/document/product/266/9759)。僅 IsPersistence 爲 1 時有效。
        :type Procedure: str
        :param MetaDataRequired: 是否需要返回剪輯後的視訊元訊息。0 不需要，1 需要。預設不需要。
        :type MetaDataRequired: int
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.StreamId = None
        self.StartTime = None
        self.EndTime = None
        self.IsPersistence = None
        self.ExpireTime = None
        self.Procedure = None
        self.MetaDataRequired = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.StreamId = params.get("StreamId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.IsPersistence = params.get("IsPersistence")
        self.ExpireTime = params.get("ExpireTime")
        self.Procedure = params.get("Procedure")
        self.MetaDataRequired = params.get("MetaDataRequired")
        self.SubAppId = params.get("SubAppId")


class LiveRealTimeClipResponse(AbstractModel):
    """LiveRealTimeClip返回參數結構體

    """

    def __init__(self):
        """
        :param Url: 剪輯後的視訊播放 URL。
        :type Url: str
        :param FileId: 剪輯固化後的視訊的媒體文件的唯一標識。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileId: str
        :param VodTaskId: 剪輯固化後的視訊任務流 ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type VodTaskId: str
        :param MetaData: 剪輯後的視訊元訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type MetaData: :class:`taifucloudcloud.vod.v20180717.models.MediaMetaData`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Url = None
        self.FileId = None
        self.VodTaskId = None
        self.MetaData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.FileId = params.get("FileId")
        self.VodTaskId = params.get("VodTaskId")
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        self.RequestId = params.get("RequestId")


class MediaAdaptiveDynamicStreamingInfo(AbstractModel):
    """轉自适應碼流訊息

    """

    def __init__(self):
        """
        :param AdaptiveDynamicStreamingSet: 轉自适應碼流訊息數組。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AdaptiveDynamicStreamingSet: list of AdaptiveDynamicStreamingInfoItem
        """
        self.AdaptiveDynamicStreamingSet = None


    def _deserialize(self, params):
        if params.get("AdaptiveDynamicStreamingSet") is not None:
            self.AdaptiveDynamicStreamingSet = []
            for item in params.get("AdaptiveDynamicStreamingSet"):
                obj = AdaptiveDynamicStreamingInfoItem()
                obj._deserialize(item)
                self.AdaptiveDynamicStreamingSet.append(obj)


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
        :param CoverUrl: 智慧封面網址。
        :type CoverUrl: str
        :param Confidence: 智慧封面的可信度，取值範圍是 0 到 100。
        :type Confidence: float
        """
        self.CoverUrl = None
        self.Confidence = None


    def _deserialize(self, params):
        self.CoverUrl = params.get("CoverUrl")
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


class MediaAnimatedGraphicsInfo(AbstractModel):
    """點播文件視訊轉動圖結果訊息

    """

    def __init__(self):
        """
        :param AnimatedGraphicsSet: 視訊轉動圖結果訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type AnimatedGraphicsSet: list of MediaAnimatedGraphicsItem
        """
        self.AnimatedGraphicsSet = None


    def _deserialize(self, params):
        if params.get("AnimatedGraphicsSet") is not None:
            self.AnimatedGraphicsSet = []
            for item in params.get("AnimatedGraphicsSet"):
                obj = MediaAnimatedGraphicsItem()
                obj._deserialize(item)
                self.AnimatedGraphicsSet.append(obj)


class MediaAnimatedGraphicsItem(AbstractModel):
    """視訊轉動圖結果訊息

    """

    def __init__(self):
        """
        :param Url: 轉動圖的文件網址。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Url: str
        :param Definition: 轉動圖範本 ID，參見[轉動圖參數範本](https://cloud.taifucloud.com/document/product/266/33481#.E8.BD.AC.E5.8A.A8.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Definition: int
        :param Container: 動圖格式，如 gif。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Container: str
        :param Height: 動圖的高度，單位：px。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Height: int
        :param Width: 動圖的寬度，單位：px。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Width: int
        :param Bitrate: 動圖碼率，單位：bps。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Bitrate: int
        :param Size: 動圖大小，單位：位元。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Size: int
        :param Md5: 動圖的md5值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Md5: str
        :param StartTimeOffset: 動圖在視訊中的起始時間偏移，單位：秒。
注意：此欄位可能返回 null，表示取不到有效值。
        :type StartTimeOffset: float
        :param EndTimeOffset: 動圖在視訊中的結束時間偏移，單位：秒。
注意：此欄位可能返回 null，表示取不到有效值。
        :type EndTimeOffset: float
        """
        self.Url = None
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
        self.Url = params.get("Url")
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
注意：此欄位可能返回 null，表示取不到有效值。
        :type Bitrate: int
        :param SamplingRate: 音訊流的采樣率，單位：hz。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SamplingRate: int
        :param Codec: 音訊流的編碼格式，例如 aac。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Codec: str
        """
        self.Bitrate = None
        self.SamplingRate = None
        self.Codec = None


    def _deserialize(self, params):
        self.Bitrate = params.get("Bitrate")
        self.SamplingRate = params.get("SamplingRate")
        self.Codec = params.get("Codec")


class MediaBasicInfo(AbstractModel):
    """點播媒體文件基礎訊息

    """

    def __init__(self):
        """
        :param Name: 媒體文件名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Name: str
        :param Description: 媒體文件描述。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Description: str
        :param CreateTime: 媒體文件的創建時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 媒體文件的最近更新時間（如修改視訊屬性、發起視訊處理等會觸發更新媒體文件訊息的操作），使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
注意：此欄位可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param ExpireTime: 媒體文件的過期時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。過期後該媒體文件及其相關資源（轉碼結果、雪碧圖等）将被永久删除。“9999-12-31T23:59:59Z”表示永不過期。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param ClassId: 媒體文件的分類 ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClassId: int
        :param ClassName: 媒體文件的分類名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClassName: str
        :param ClassPath: 媒體文件的分類路徑，分類間以“-”分隔，如“新的一級分類 - 新的二級分類”。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClassPath: str
        :param CoverUrl: 媒體文件的封面圖片網址。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CoverUrl: str
        :param Type: 媒體文件的封裝格式，例如 mp4、flv 等。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Type: str
        :param MediaUrl: 原始媒體文件的 URL 網址。
注意：此欄位可能返回 null，表示取不到有效值。
        :type MediaUrl: str
        :param SourceInfo: 該媒體文件的來源訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SourceInfo: :class:`taifucloudcloud.vod.v20180717.models.MediaSourceData`
        :param StorageRegion: 媒體文件儲存地區，如 ap-guangzhou，參見[地域清單](https://cloud.taifucloud.com/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。
注意：此欄位可能返回 null，表示取不到有效值。
        :type StorageRegion: str
        :param TagSet: 媒體文件的標簽訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagSet: list of str
        :param Vid: 直播錄制文件的唯一標識
注意：此欄位可能返回 null，表示取不到有效值。
        :type Vid: str
        """
        self.Name = None
        self.Description = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ExpireTime = None
        self.ClassId = None
        self.ClassName = None
        self.ClassPath = None
        self.CoverUrl = None
        self.Type = None
        self.MediaUrl = None
        self.SourceInfo = None
        self.StorageRegion = None
        self.TagSet = None
        self.Vid = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.ClassId = params.get("ClassId")
        self.ClassName = params.get("ClassName")
        self.ClassPath = params.get("ClassPath")
        self.CoverUrl = params.get("CoverUrl")
        self.Type = params.get("Type")
        self.MediaUrl = params.get("MediaUrl")
        if params.get("SourceInfo") is not None:
            self.SourceInfo = MediaSourceData()
            self.SourceInfo._deserialize(params.get("SourceInfo"))
        self.StorageRegion = params.get("StorageRegion")
        self.TagSet = params.get("TagSet")
        self.Vid = params.get("Vid")


class MediaClassInfo(AbstractModel):
    """分類訊息描述

    """

    def __init__(self):
        """
        :param ClassId: 分類 ID
        :type ClassId: int
        :param ParentId: 父類 ID，一級分類的父類 ID 爲 -1。
        :type ParentId: int
        :param ClassName: 分類名稱
        :type ClassName: str
        :param Level: 分類級别，一級分類爲 0，最大值爲 3，即最多允許 4 級分類層次。
        :type Level: int
        :param SubClassIdSet: 當前分類的第一級子類 ID 集合
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubClassIdSet: list of int
        """
        self.ClassId = None
        self.ParentId = None
        self.ClassName = None
        self.Level = None
        self.SubClassIdSet = None


    def _deserialize(self, params):
        self.ClassId = params.get("ClassId")
        self.ParentId = params.get("ParentId")
        self.ClassName = params.get("ClassName")
        self.Level = params.get("Level")
        self.SubClassIdSet = params.get("SubClassIdSet")


class MediaContentReviewAsrTextSegmentItem(AbstractModel):
    """内容審核 Asr 文字審核嫌疑片段

    """

    def __init__(self):
        """
        :param StartTimeOffset: 嫌疑片段起始的偏移時間，單位：秒。
注意：此欄位可能返回 null，表示取不到有效值。
        :type StartTimeOffset: float
        :param EndTimeOffset: 嫌疑片段結束的偏移時間，單位：秒。
注意：此欄位可能返回 null，表示取不到有效值。
        :type EndTimeOffset: float
        :param Confidence: 嫌疑片段置信度。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param Suggestion: 嫌疑片段審核結果建議，取值範圍：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param KeywordSet: 嫌疑關鍵詞清單。
注意：此欄位可能返回 null，表示取不到有效值。
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
注意：此欄位可能返回 null，表示取不到有效值。
        :type StartTimeOffset: float
        :param EndTimeOffset: 嫌疑片段結束的偏移時間，單位：秒。
注意：此欄位可能返回 null，表示取不到有效值。
        :type EndTimeOffset: float
        :param Confidence: 嫌疑片段置信度。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param Suggestion: 嫌疑片段審核結果建議，取值範圍：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param KeywordSet: 嫌疑關鍵詞清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type KeywordSet: list of str
        :param AreaCoordSet: 嫌疑文字出現的區域坐標 (像素級)，[x1, y1, x2, y2]，即左上角坐標、右下角坐標。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AreaCoordSet: list of int
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Suggestion = None
        self.KeywordSet = None
        self.AreaCoordSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.KeywordSet = params.get("KeywordSet")
        self.AreaCoordSet = params.get("AreaCoordSet")


class MediaContentReviewPoliticalSegmentItem(AbstractModel):
    """内容審核涉政嫌疑片段

    """

    def __init__(self):
        """
        :param StartTimeOffset: 嫌疑片段起始的偏移時間，單位：秒。
注意：此欄位可能返回 null，表示取不到有效值。
        :type StartTimeOffset: float
        :param EndTimeOffset: 嫌疑片段結束的偏移時間，單位：秒。
注意：此欄位可能返回 null，表示取不到有效值。
        :type EndTimeOffset: float
        :param Confidence: 嫌疑片段涉政分數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param Suggestion: 嫌疑片段鑒政結果建議，取值範圍：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Name: 涉政人物、違規圖標名字。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Name: str
        :param Label: 嫌疑片段鑒政結果標簽。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Label: str
        :param Url: 嫌疑圖片 URL （圖片不會永久儲存，到達
 PicUrlExpireTime 時間點後圖片将被删除）。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Url: str
        :param AreaCoordSet: 涉政人物、違規圖標出現的區域坐標 (像素級)，[x1, y1, x2, y2]，即左上角坐標、右下角坐標。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AreaCoordSet: list of int
        :param PicUrlExpireTimeStamp: 嫌疑圖片 URL 失效時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PicUrlExpireTimeStamp: int
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Suggestion = None
        self.Name = None
        self.Label = None
        self.Url = None
        self.AreaCoordSet = None
        self.PicUrlExpireTimeStamp = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Name = params.get("Name")
        self.Label = params.get("Label")
        self.Url = params.get("Url")
        self.AreaCoordSet = params.get("AreaCoordSet")
        self.PicUrlExpireTimeStamp = params.get("PicUrlExpireTimeStamp")


class MediaContentReviewSegmentItem(AbstractModel):
    """内容審核涉黃/暴恐嫌疑片段

    """

    def __init__(self):
        """
        :param StartTimeOffset: 嫌疑片段起始的偏移時間，單位：秒。
注意：此欄位可能返回 null，表示取不到有效值。
        :type StartTimeOffset: float
        :param EndTimeOffset: 嫌疑片段結束的偏移時間，單位：秒。
注意：此欄位可能返回 null，表示取不到有效值。
        :type EndTimeOffset: float
        :param Confidence: 嫌疑片段涉黃分數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param Label: 嫌疑片段 結果標簽。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Label: str
        :param Suggestion: 嫌疑片段 結果建議，取值範圍：
<li>pass。</li>
<li>review。</li>
<li>block。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Url: 嫌疑圖片 URL （圖片不會永久儲存，到達
 PicUrlExpireTime 時間點後圖片将被删除）。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Url: str
        :param PicUrlExpireTimeStamp: 嫌疑圖片 URL 失效時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PicUrlExpireTimeStamp: int
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Label = None
        self.Suggestion = None
        self.Url = None
        self.PicUrlExpireTimeStamp = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Label = params.get("Label")
        self.Suggestion = params.get("Suggestion")
        self.Url = params.get("Url")
        self.PicUrlExpireTimeStamp = params.get("PicUrlExpireTimeStamp")


class MediaDeleteItem(AbstractModel):
    """指定删除點播視訊時的删除内容

    """

    def __init__(self):
        """
        :param Type: 所指定的删除部分。如果未填寫該欄位則參數無效。可選值有：
<li>TranscodeFiles（删除轉碼文件）。</li>
<li>WechatPublishFiles（删除 發布文件）。</li>
        :type Type: str
        :param Definition: 删除由Type參數指定的種類下的視訊範本號，範本定義參見[轉碼範本](https://cloud.taifucloud.com/document/product/266/33478#.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF)。
預設值爲0，表示删除參數Type指定種類下所有的視訊。
        :type Definition: int
        """
        self.Type = None
        self.Definition = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Definition = params.get("Definition")


class MediaImageSpriteInfo(AbstractModel):
    """點播文件雪碧圖訊息

    """

    def __init__(self):
        """
        :param ImageSpriteSet: 特定規格的雪碧圖訊息集合，每個元素代表一套相同規格的雪碧圖。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ImageSpriteSet: list of MediaImageSpriteItem
        """
        self.ImageSpriteSet = None


    def _deserialize(self, params):
        if params.get("ImageSpriteSet") is not None:
            self.ImageSpriteSet = []
            for item in params.get("ImageSpriteSet"):
                obj = MediaImageSpriteItem()
                obj._deserialize(item)
                self.ImageSpriteSet.append(obj)


class MediaImageSpriteItem(AbstractModel):
    """雪碧圖訊息

    """

    def __init__(self):
        """
        :param Definition: 雪碧圖規格，參見[雪碧圖參數範本](https://cloud.taifucloud.com/document/product/266/33480#.E9.9B.AA.E7.A2.A7.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Definition: int
        :param Height: 雪碧圖小圖的高度。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Height: int
        :param Width: 雪碧圖小圖的寬度。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Width: int
        :param TotalCount: 每一張雪碧圖大圖裏小圖的數量。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param ImageUrlSet: 每一張雪碧圖大圖的網址。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ImageUrlSet: list of str
        :param WebVttUrl: 雪碧圖子圖位置與時間關系的 WebVtt 文件網址。WebVtt 文件表明了各個雪碧圖小圖對應的時間點，以及在在雪碧大圖裏的坐標位置，一般被播放器用於實現預覽。
注意：此欄位可能返回 null，表示取不到有效值。
        :type WebVttUrl: str
        """
        self.Definition = None
        self.Height = None
        self.Width = None
        self.TotalCount = None
        self.ImageUrlSet = None
        self.WebVttUrl = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.TotalCount = params.get("TotalCount")
        self.ImageUrlSet = params.get("ImageUrlSet")
        self.WebVttUrl = params.get("WebVttUrl")


class MediaInfo(AbstractModel):
    """點播文件訊息

    """

    def __init__(self):
        """
        :param BasicInfo: 基礎訊息。包括視訊名稱、大小、時長、封面圖片等。
注意：此欄位可能返回 null，表示取不到有效值。
        :type BasicInfo: :class:`taifucloudcloud.vod.v20180717.models.MediaBasicInfo`
        :param MetaData: 元訊息。包括視訊流訊息、音訊流訊息等。
注意：此欄位可能返回 null，表示取不到有效值。
        :type MetaData: :class:`taifucloudcloud.vod.v20180717.models.MediaMetaData`
        :param TranscodeInfo: 轉碼結果訊息。包括該視訊轉碼生成的各種碼率的視訊的網址、規格、碼率、分辨率等。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranscodeInfo: :class:`taifucloudcloud.vod.v20180717.models.MediaTranscodeInfo`
        :param AnimatedGraphicsInfo: 轉動圖結果訊息。對視訊轉動圖（如 gif）後，動圖相關訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AnimatedGraphicsInfo: :class:`taifucloudcloud.vod.v20180717.models.MediaAnimatedGraphicsInfo`
        :param SampleSnapshotInfo: 采樣截圖訊息。對視訊采樣截圖後，相關截圖訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SampleSnapshotInfo: :class:`taifucloudcloud.vod.v20180717.models.MediaSampleSnapshotInfo`
        :param ImageSpriteInfo: 雪碧圖訊息。對視訊截取雪碧圖之後，雪碧的相關訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ImageSpriteInfo: :class:`taifucloudcloud.vod.v20180717.models.MediaImageSpriteInfo`
        :param SnapshotByTimeOffsetInfo: 指定時間點截圖訊息。對視訊依照指定時間點截圖後，各個截圖的訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SnapshotByTimeOffsetInfo: :class:`taifucloudcloud.vod.v20180717.models.MediaSnapshotByTimeOffsetInfo`
        :param KeyFrameDescInfo: 視訊打點訊息。對視訊設置的各個打點訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type KeyFrameDescInfo: :class:`taifucloudcloud.vod.v20180717.models.MediaKeyFrameDescInfo`
        :param AdaptiveDynamicStreamingInfo: 轉自适應碼流訊息。包括規格、加密類型、打包格式等相關訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AdaptiveDynamicStreamingInfo: :class:`taifucloudcloud.vod.v20180717.models.MediaAdaptiveDynamicStreamingInfo`
        :param FileId: 媒體文件唯一標識 ID。
        :type FileId: str
        """
        self.BasicInfo = None
        self.MetaData = None
        self.TranscodeInfo = None
        self.AnimatedGraphicsInfo = None
        self.SampleSnapshotInfo = None
        self.ImageSpriteInfo = None
        self.SnapshotByTimeOffsetInfo = None
        self.KeyFrameDescInfo = None
        self.AdaptiveDynamicStreamingInfo = None
        self.FileId = None


    def _deserialize(self, params):
        if params.get("BasicInfo") is not None:
            self.BasicInfo = MediaBasicInfo()
            self.BasicInfo._deserialize(params.get("BasicInfo"))
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        if params.get("TranscodeInfo") is not None:
            self.TranscodeInfo = MediaTranscodeInfo()
            self.TranscodeInfo._deserialize(params.get("TranscodeInfo"))
        if params.get("AnimatedGraphicsInfo") is not None:
            self.AnimatedGraphicsInfo = MediaAnimatedGraphicsInfo()
            self.AnimatedGraphicsInfo._deserialize(params.get("AnimatedGraphicsInfo"))
        if params.get("SampleSnapshotInfo") is not None:
            self.SampleSnapshotInfo = MediaSampleSnapshotInfo()
            self.SampleSnapshotInfo._deserialize(params.get("SampleSnapshotInfo"))
        if params.get("ImageSpriteInfo") is not None:
            self.ImageSpriteInfo = MediaImageSpriteInfo()
            self.ImageSpriteInfo._deserialize(params.get("ImageSpriteInfo"))
        if params.get("SnapshotByTimeOffsetInfo") is not None:
            self.SnapshotByTimeOffsetInfo = MediaSnapshotByTimeOffsetInfo()
            self.SnapshotByTimeOffsetInfo._deserialize(params.get("SnapshotByTimeOffsetInfo"))
        if params.get("KeyFrameDescInfo") is not None:
            self.KeyFrameDescInfo = MediaKeyFrameDescInfo()
            self.KeyFrameDescInfo._deserialize(params.get("KeyFrameDescInfo"))
        if params.get("AdaptiveDynamicStreamingInfo") is not None:
            self.AdaptiveDynamicStreamingInfo = MediaAdaptiveDynamicStreamingInfo()
            self.AdaptiveDynamicStreamingInfo._deserialize(params.get("AdaptiveDynamicStreamingInfo"))
        self.FileId = params.get("FileId")


class MediaInputInfo(AbstractModel):
    """要處理的源視訊訊息，視訊名稱、視訊自定義 ID。

    """

    def __init__(self):
        """
        :param Url: 視訊 URL。
        :type Url: str
        :param Name: 視訊名稱。
        :type Name: str
        :param Id: 視訊自定義 ID。
        :type Id: str
        """
        self.Url = None
        self.Name = None
        self.Id = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.Name = params.get("Name")
        self.Id = params.get("Id")


class MediaKeyFrameDescInfo(AbstractModel):
    """視訊打點訊息

    """

    def __init__(self):
        """
        :param KeyFrameDescSet: 視訊打點訊息數組。
注意：此欄位可能返回 null，表示取不到有效值。
        :type KeyFrameDescSet: list of MediaKeyFrameDescItem
        """
        self.KeyFrameDescSet = None


    def _deserialize(self, params):
        if params.get("KeyFrameDescSet") is not None:
            self.KeyFrameDescSet = []
            for item in params.get("KeyFrameDescSet"):
                obj = MediaKeyFrameDescItem()
                obj._deserialize(item)
                self.KeyFrameDescSet.append(obj)


class MediaKeyFrameDescItem(AbstractModel):
    """視訊打點訊息

    """

    def __init__(self):
        """
        :param TimeOffset: 打點的視訊偏移時間，單位：秒。
        :type TimeOffset: float
        :param Content: 打點的内容字串，限制 1-128 個字元。
        :type Content: str
        """
        self.TimeOffset = None
        self.Content = None


    def _deserialize(self, params):
        self.TimeOffset = params.get("TimeOffset")
        self.Content = params.get("Content")


class MediaMetaData(AbstractModel):
    """點播媒體文件元訊息

    """

    def __init__(self):
        """
        :param Size: 上傳的媒體文件大小（視訊爲 HLS 時，大小是 m3u8 和 ts 文件大小的總和），單位：位元。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Size: int
        :param Container: 容器類型，例如 m4a，mp4 等。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Container: str
        :param Bitrate: 視訊流碼率平均值與音訊流碼率平均值之和，單位：bps。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Bitrate: int
        :param Height: 視訊流高度的最大值，單位：px。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Height: int
        :param Width: 視訊流寬度的最大值，單位：px。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Width: int
        :param Duration: 視訊時長，單位：秒。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Duration: float
        :param Rotate: 視訊拍攝時的選擇角度，單位：度。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Rotate: int
        :param VideoStreamSet: 視訊流訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type VideoStreamSet: list of MediaVideoStreamItem
        :param AudioStreamSet: 音訊流訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AudioStreamSet: list of MediaAudioStreamItem
        :param VideoDuration: 視訊時長，單位：秒。
注意：此欄位可能返回 null，表示取不到有效值。
        :type VideoDuration: float
        :param AudioDuration: 音訊時長，單位：秒。
注意：此欄位可能返回 null，表示取不到有效值。
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


class MediaOutputInfo(AbstractModel):
    """視訊處理輸出文件訊息參數。

    """

    def __init__(self):
        """
        :param Region: 輸出文件 Bucket 所屬地域，如 ap-guangzhou  。
        :type Region: str
        :param Bucket: 輸出文件 Bucket 。
        :type Bucket: str
        :param Dir: 輸出文件目錄，目錄名必須以 "/" 結尾。
        :type Dir: str
        """
        self.Region = None
        self.Bucket = None
        self.Dir = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Bucket = params.get("Bucket")
        self.Dir = params.get("Dir")


class MediaProcessTaskAdaptiveDynamicStreamingResult(AbstractModel):
    """對視訊轉自适應碼流任務結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param Input: 對視訊轉自适應碼流任務的輸入。
        :type Input: :class:`taifucloudcloud.vod.v20180717.models.AdaptiveDynamicStreamingTaskInput`
        :param Output: 對視訊轉自适應碼流任務的輸出。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.AdaptiveDynamicStreamingInfoItem`
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
            self.Input = AdaptiveDynamicStreamingTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AdaptiveDynamicStreamingInfoItem()
            self.Output._deserialize(params.get("Output"))


class MediaProcessTaskAnimatedGraphicResult(AbstractModel):
    """轉動圖任務結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 錯誤訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 轉動圖任務的輸入。
        :type Input: :class:`taifucloudcloud.vod.v20180717.models.AnimatedGraphicTaskInput`
        :param Output: 轉動圖任務的輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.MediaAnimatedGraphicsItem`
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


class MediaProcessTaskCoverBySnapshotResult(AbstractModel):
    """對視訊截圖做封面任務結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 錯誤訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 對視訊截圖做封面任務的輸入。
        :type Input: :class:`taifucloudcloud.vod.v20180717.models.CoverBySnapshotTaskInput`
        :param Output: 對視訊截圖做封面任務的輸出。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.CoverBySnapshotTaskOutput`
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
            self.Input = CoverBySnapshotTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = CoverBySnapshotTaskOutput()
            self.Output._deserialize(params.get("Output"))


class MediaProcessTaskImageSpriteResult(AbstractModel):
    """對視訊截雪碧圖任務結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 錯誤訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 對視訊截雪碧圖任務的輸入。
        :type Input: :class:`taifucloudcloud.vod.v20180717.models.ImageSpriteTaskInput`
        :param Output: 對視訊截雪碧圖任務的輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.MediaImageSpriteItem`
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
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranscodeTaskSet: list of TranscodeTaskInput
        :param AnimatedGraphicTaskSet: 視訊轉動圖任務清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AnimatedGraphicTaskSet: list of AnimatedGraphicTaskInput
        :param SnapshotByTimeOffsetTaskSet: 對視訊按時間點截圖任務清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SnapshotByTimeOffsetTaskSet: list of SnapshotByTimeOffsetTaskInput
        :param SampleSnapshotTaskSet: 對視訊采樣截圖任務清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SampleSnapshotTaskSet: list of SampleSnapshotTaskInput
        :param ImageSpriteTaskSet: 對視訊截雪碧圖任務清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ImageSpriteTaskSet: list of ImageSpriteTaskInput
        :param CoverBySnapshotTaskSet: 對視訊截圖做封面任務清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CoverBySnapshotTaskSet: list of CoverBySnapshotTaskInput
        :param AdaptiveDynamicStreamingTaskSet: 對視訊轉自适應碼流任務清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AdaptiveDynamicStreamingTaskSet: list of AdaptiveDynamicStreamingTaskInput
        """
        self.TranscodeTaskSet = None
        self.AnimatedGraphicTaskSet = None
        self.SnapshotByTimeOffsetTaskSet = None
        self.SampleSnapshotTaskSet = None
        self.ImageSpriteTaskSet = None
        self.CoverBySnapshotTaskSet = None
        self.AdaptiveDynamicStreamingTaskSet = None


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
        if params.get("CoverBySnapshotTaskSet") is not None:
            self.CoverBySnapshotTaskSet = []
            for item in params.get("CoverBySnapshotTaskSet"):
                obj = CoverBySnapshotTaskInput()
                obj._deserialize(item)
                self.CoverBySnapshotTaskSet.append(obj)
        if params.get("AdaptiveDynamicStreamingTaskSet") is not None:
            self.AdaptiveDynamicStreamingTaskSet = []
            for item in params.get("AdaptiveDynamicStreamingTaskSet"):
                obj = AdaptiveDynamicStreamingTaskInput()
                obj._deserialize(item)
                self.AdaptiveDynamicStreamingTaskSet.append(obj)


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
        :type TranscodeTask: :class:`taifucloudcloud.vod.v20180717.models.MediaProcessTaskTranscodeResult`
        :param AnimatedGraphicTask: 視訊轉動圖任務的查詢結果，當任務類型爲 AnimatedGraphics 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AnimatedGraphicTask: :class:`taifucloudcloud.vod.v20180717.models.MediaProcessTaskAnimatedGraphicResult`
        :param SnapshotByTimeOffsetTask: 對視訊按時間點截圖任務的查詢結果，當任務類型爲 SnapshotByTimeOffset 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SnapshotByTimeOffsetTask: :class:`taifucloudcloud.vod.v20180717.models.MediaProcessTaskSnapshotByTimeOffsetResult`
        :param SampleSnapshotTask: 對視訊采樣截圖任務的查詢結果，當任務類型爲 SampleSnapshot 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SampleSnapshotTask: :class:`taifucloudcloud.vod.v20180717.models.MediaProcessTaskSampleSnapshotResult`
        :param ImageSpriteTask: 對視訊截雪碧圖任務的查詢結果，當任務類型爲 ImageSprite 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ImageSpriteTask: :class:`taifucloudcloud.vod.v20180717.models.MediaProcessTaskImageSpriteResult`
        :param CoverBySnapshotTask: 對視訊截圖做封面任務的查詢結果，當任務類型爲 CoverBySnapshot 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CoverBySnapshotTask: :class:`taifucloudcloud.vod.v20180717.models.MediaProcessTaskCoverBySnapshotResult`
        :param AdaptiveDynamicStreamingTask: 對視訊轉自适應碼流任務的查詢結果，當任務類型爲 AdaptiveDynamicStreaming 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AdaptiveDynamicStreamingTask: :class:`taifucloudcloud.vod.v20180717.models.MediaProcessTaskAdaptiveDynamicStreamingResult`
        """
        self.Type = None
        self.TranscodeTask = None
        self.AnimatedGraphicTask = None
        self.SnapshotByTimeOffsetTask = None
        self.SampleSnapshotTask = None
        self.ImageSpriteTask = None
        self.CoverBySnapshotTask = None
        self.AdaptiveDynamicStreamingTask = None


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
        if params.get("CoverBySnapshotTask") is not None:
            self.CoverBySnapshotTask = MediaProcessTaskCoverBySnapshotResult()
            self.CoverBySnapshotTask._deserialize(params.get("CoverBySnapshotTask"))
        if params.get("AdaptiveDynamicStreamingTask") is not None:
            self.AdaptiveDynamicStreamingTask = MediaProcessTaskAdaptiveDynamicStreamingResult()
            self.AdaptiveDynamicStreamingTask._deserialize(params.get("AdaptiveDynamicStreamingTask"))


class MediaProcessTaskSampleSnapshotResult(AbstractModel):
    """對視訊做采樣截圖任務結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 錯誤訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 對視訊做采樣截圖任務輸入。
        :type Input: :class:`taifucloudcloud.vod.v20180717.models.SampleSnapshotTaskInput`
        :param Output: 對視訊做采樣截圖任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.MediaSampleSnapshotItem`
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
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 錯誤訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 對視訊按指定時間點截圖任務輸入。
        :type Input: :class:`taifucloudcloud.vod.v20180717.models.SnapshotByTimeOffsetTaskInput`
        :param Output: 對視訊按指定時間點截圖任務輸出。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.MediaSnapshotByTimeOffsetItem`
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
        :param ErrCode: 錯誤碼，0：成功，其他值：失敗。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 錯誤訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param Input: 轉碼任務的輸入。
        :type Input: :class:`taifucloudcloud.vod.v20180717.models.TranscodeTaskInput`
        :param Output: 轉碼任務的輸出。
        :type Output: :class:`taifucloudcloud.vod.v20180717.models.MediaTranscodeItem`
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


class MediaSampleSnapshotInfo(AbstractModel):
    """點播文件采樣截圖訊息

    """

    def __init__(self):
        """
        :param SampleSnapshotSet: 特定規格的采樣截圖訊息集合，每個元素代表一套相同規格的采樣截圖。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SampleSnapshotSet: list of MediaSampleSnapshotItem
        """
        self.SampleSnapshotSet = None


    def _deserialize(self, params):
        if params.get("SampleSnapshotSet") is not None:
            self.SampleSnapshotSet = []
            for item in params.get("SampleSnapshotSet"):
                obj = MediaSampleSnapshotItem()
                obj._deserialize(item)
                self.SampleSnapshotSet.append(obj)


class MediaSampleSnapshotItem(AbstractModel):
    """采樣截圖訊息

    """

    def __init__(self):
        """
        :param Definition: 采樣截圖規格 ID，參見[采樣截圖參數範本](https://cloud.taifucloud.com/document/product/266/33480#.E9.87.87.E6.A0.B7.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Definition: int
        :param SampleType: 采樣方式，取值範圍：
<li>Percent：根據百分比間隔采樣。</li>
<li>Time：根據時間間隔采樣。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type SampleType: str
        :param Interval: 采樣間隔
<li>當 SampleType 爲 Percent 時，該值表示多少百分比一張圖。</li>
<li>當 SampleType 爲 Time 時，該值表示多少時間間隔一張圖，單位秒， 第一張圖均爲視訊首幀。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type Interval: int
        :param ImageUrlSet: 生成的截圖 url 清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ImageUrlSet: list of str
        :param WaterMarkDefinition: 截圖如果被打上了浮水印，被打水印的範本 ID 清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type WaterMarkDefinition: list of int
        """
        self.Definition = None
        self.SampleType = None
        self.Interval = None
        self.ImageUrlSet = None
        self.WaterMarkDefinition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SampleType = params.get("SampleType")
        self.Interval = params.get("Interval")
        self.ImageUrlSet = params.get("ImageUrlSet")
        self.WaterMarkDefinition = params.get("WaterMarkDefinition")


class MediaSnapshotByTimeOffsetInfo(AbstractModel):
    """點播文件指定時間點截圖訊息

    """

    def __init__(self):
        """
        :param SnapshotByTimeOffsetSet: 特定規格的指定時間點截圖訊息集合。目前每種規格只能有一套截圖。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SnapshotByTimeOffsetSet: list of MediaSnapshotByTimeOffsetItem
        """
        self.SnapshotByTimeOffsetSet = None


    def _deserialize(self, params):
        if params.get("SnapshotByTimeOffsetSet") is not None:
            self.SnapshotByTimeOffsetSet = []
            for item in params.get("SnapshotByTimeOffsetSet"):
                obj = MediaSnapshotByTimeOffsetItem()
                obj._deserialize(item)
                self.SnapshotByTimeOffsetSet.append(obj)


class MediaSnapshotByTimeOffsetItem(AbstractModel):
    """點播文件指定時間點截圖訊息

    """

    def __init__(self):
        """
        :param Definition: 指定時間點截圖規格，參見[指定時間點截圖參數範本](https://cloud.taifucloud.com/document/product/266/33480#.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Definition: int
        :param PicInfoSet: 同一規格的截圖訊息集合，每個元素代表一張截圖。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PicInfoSet: list of MediaSnapshotByTimePicInfoItem
        """
        self.Definition = None
        self.PicInfoSet = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("PicInfoSet") is not None:
            self.PicInfoSet = []
            for item in params.get("PicInfoSet"):
                obj = MediaSnapshotByTimePicInfoItem()
                obj._deserialize(item)
                self.PicInfoSet.append(obj)


class MediaSnapshotByTimePicInfoItem(AbstractModel):
    """指定時間點截圖訊息

    """

    def __init__(self):
        """
        :param TimeOffset: 該張截圖對應視訊文件中的時間偏移，單位：秒。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TimeOffset: float
        :param Url: 該張截圖的 URL 網址。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Url: str
        :param WaterMarkDefinition: 截圖如果被打上了浮水印，被打水印的範本 ID 清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type WaterMarkDefinition: list of int
        """
        self.TimeOffset = None
        self.Url = None
        self.WaterMarkDefinition = None


    def _deserialize(self, params):
        self.TimeOffset = params.get("TimeOffset")
        self.Url = params.get("Url")
        self.WaterMarkDefinition = params.get("WaterMarkDefinition")


class MediaSourceData(AbstractModel):
    """來源文件訊息

    """

    def __init__(self):
        """
        :param SourceType: 媒體文件的來源類别：
<li>Record：來自錄制。如直播錄制、直播時移錄制等。</li>
<li>Upload：來自上傳。如拉取上傳、服務端上傳、用戶端 UGC 上傳等。</li>
<li>VideoProcessing：來自視訊處理。如視訊拼接、視訊剪輯等。</li>
<li>Unknown：未知來源。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type SourceType: str
        :param SourceContext: 用戶創建文件時透傳的欄位
注意：此欄位可能返回 null，表示取不到有效值。
        :type SourceContext: str
        """
        self.SourceType = None
        self.SourceContext = None


    def _deserialize(self, params):
        self.SourceType = params.get("SourceType")
        self.SourceContext = params.get("SourceContext")


class MediaTrack(AbstractModel):
    """軌道訊息

    """

    def __init__(self):
        """
        :param Type: 軌道類型，取值有：
<ul>
<li>Video ：視訊軌道。視訊軌道由以下 Item 組成：<ul><li>VideoTrackItem</li><li>MediaTransitionItem</li> <li>EmptyTrackItem</li></ul> </li>
<li>Audio ：音訊軌道。音訊軌道由以下 Item 組成：<ul><li>AudioTrackItem</li><li>MediaTransitionItem</li><li>EmptyTrackItem</li></ul></li>
<li>Sticker ：貼圖軌道。貼圖軌道以下 Item 組成：<ul><li> StickerTrackItem</li><li>EmptyTrackItem</li></ul></li>	
</ul>
        :type Type: str
        :param TrackItems: 軌道上的媒體片段清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TrackItems: list of MediaTrackItem
        """
        self.Type = None
        self.TrackItems = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("TrackItems") is not None:
            self.TrackItems = []
            for item in params.get("TrackItems"):
                obj = MediaTrackItem()
                obj._deserialize(item)
                self.TrackItems.append(obj)


class MediaTrackItem(AbstractModel):
    """媒體軌道的片段訊息

    """

    def __init__(self):
        """
        :param Type: 片段類型。取值有：
<li>Video：視訊片段。</li>
<li>Audio：音訊片段。</li>
<li>Sticker：貼圖片段。</li>
<li>Transition：轉場。</li>
<li>Empty：空白片段。</li>
        :type Type: str
        :param VideoItem: 視訊片段，當 Type = Video 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type VideoItem: :class:`taifucloudcloud.vod.v20180717.models.VideoTrackItem`
        :param AudioItem: 音訊片段，當 Type = Audio 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AudioItem: :class:`taifucloudcloud.vod.v20180717.models.AudioTrackItem`
        :param StickerItem: 貼圖片段，當 Type = Sticker 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type StickerItem: :class:`taifucloudcloud.vod.v20180717.models.StickerTrackItem`
        :param TransitionItem: 轉場，當 Type = Transition 時有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TransitionItem: :class:`taifucloudcloud.vod.v20180717.models.MediaTransitionItem`
        :param EmptyItem: 空白片段，當 Type = Empty 時有效。空片段用於時間軸的占位。<li>如需要兩個音訊片段之間有一段時間的靜音，可以用 EmptyTrackItem 來進行占位。</li>
<li>使用 EmptyTrackItem 進行占位，來定位某個Item。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type EmptyItem: :class:`taifucloudcloud.vod.v20180717.models.EmptyTrackItem`
        """
        self.Type = None
        self.VideoItem = None
        self.AudioItem = None
        self.StickerItem = None
        self.TransitionItem = None
        self.EmptyItem = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("VideoItem") is not None:
            self.VideoItem = VideoTrackItem()
            self.VideoItem._deserialize(params.get("VideoItem"))
        if params.get("AudioItem") is not None:
            self.AudioItem = AudioTrackItem()
            self.AudioItem._deserialize(params.get("AudioItem"))
        if params.get("StickerItem") is not None:
            self.StickerItem = StickerTrackItem()
            self.StickerItem._deserialize(params.get("StickerItem"))
        if params.get("TransitionItem") is not None:
            self.TransitionItem = MediaTransitionItem()
            self.TransitionItem._deserialize(params.get("TransitionItem"))
        if params.get("EmptyItem") is not None:
            self.EmptyItem = EmptyTrackItem()
            self.EmptyItem._deserialize(params.get("EmptyItem"))


class MediaTranscodeInfo(AbstractModel):
    """點播文件轉碼訊息

    """

    def __init__(self):
        """
        :param TranscodeSet: 各規格的轉碼訊息集合，每個元素代表一個規格的轉碼結果。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TranscodeSet: list of MediaTranscodeItem
        """
        self.TranscodeSet = None


    def _deserialize(self, params):
        if params.get("TranscodeSet") is not None:
            self.TranscodeSet = []
            for item in params.get("TranscodeSet"):
                obj = MediaTranscodeItem()
                obj._deserialize(item)
                self.TranscodeSet.append(obj)


class MediaTranscodeItem(AbstractModel):
    """轉碼訊息

    """

    def __init__(self):
        """
        :param Url: 轉碼後的視訊文件網址。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Url: str
        :param Definition: 轉碼規格 ID，參見[轉碼參數範本](https://cloud.taifucloud.com/document/product/266/33478#.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF)。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Definition: int
        :param Bitrate: 視訊流碼率平均值與音訊流碼率平均值之和， 單位：bps。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Bitrate: int
        :param Height: 視訊流高度的最大值，單位：px。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Height: int
        :param Width: 視訊流寬度的最大值，單位：px。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Width: int
        :param Size: 媒體文件總大小（視訊爲 HLS 時，大小是 m3u8 和 ts 文件大小的總和），單位：位元。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Size: int
        :param Duration: 視訊時長，單位：秒。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Duration: float
        :param Container: 容器類型，例如 m4a，mp4 等。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Container: str
        :param Md5: 視訊的 md5 值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Md5: str
        :param AudioStreamSet: 音訊流訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AudioStreamSet: list of MediaAudioStreamItem
        :param VideoStreamSet: 視訊流訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type VideoStreamSet: list of MediaVideoStreamItem
        """
        self.Url = None
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
        self.Url = params.get("Url")
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


class MediaTransitionItem(AbstractModel):
    """轉場訊息

    """

    def __init__(self):
        """
        :param Duration: 轉場持續時間，單位爲秒。進行轉場處理的兩個媒體片段，第二個片段在軌道上的起始時間會自動進行調整，設置爲前面一個片段的結束時間減去轉場的持續時間。
        :type Duration: float
        :param Transitions: 轉場操作清單。圖像轉場操作和音訊轉場操作各自最多支援一個。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Transitions: list of TransitionOpertion
        """
        self.Duration = None
        self.Transitions = None


    def _deserialize(self, params):
        self.Duration = params.get("Duration")
        if params.get("Transitions") is not None:
            self.Transitions = []
            for item in params.get("Transitions"):
                obj = TransitionOpertion()
                obj._deserialize(item)
                self.Transitions.append(obj)


class MediaVideoStreamItem(AbstractModel):
    """點播文件視訊流訊息

    """

    def __init__(self):
        """
        :param Bitrate: 視訊流的碼率，單位：bps。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Bitrate: int
        :param Height: 視訊流的高度，單位：px。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Height: int
        :param Width: 視訊流的寬度，單位：px。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Width: int
        :param Codec: 視訊流的編碼格式，例如 h264。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Codec: str
        :param Fps: 幀率，單位：hz。
注意：此欄位可能返回 null，表示取不到有效值。
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
        :type ClassificationConfigure: :class:`taifucloudcloud.vod.v20180717.models.ClassificationConfigureInfoForUpdate`
        :param TagConfigure: 智慧標簽任務控制參數。
        :type TagConfigure: :class:`taifucloudcloud.vod.v20180717.models.TagConfigureInfoForUpdate`
        :param CoverConfigure: 智慧封面任務控制參數。
        :type CoverConfigure: :class:`taifucloudcloud.vod.v20180717.models.CoverConfigureInfoForUpdate`
        :param FrameTagConfigure: 智慧按幀標簽任務控制參數。
        :type FrameTagConfigure: :class:`taifucloudcloud.vod.v20180717.models.FrameTagConfigureInfoForUpdate`
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.ClassificationConfigure = None
        self.TagConfigure = None
        self.CoverConfigure = None
        self.FrameTagConfigure = None
        self.SubAppId = None


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
        self.SubAppId = params.get("SubAppId")


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
        :param HeadTailConfigure: 視訊片頭片尾識别控制參數。
        :type HeadTailConfigure: :class:`taifucloudcloud.vod.v20180717.models.HeadTailConfigureInfoForUpdate`
        :param FaceConfigure: 人臉識别控制參數。
        :type FaceConfigure: :class:`taifucloudcloud.vod.v20180717.models.FaceConfigureInfoForUpdate`
        :param OcrFullTextConfigure: 文本全文識别控制參數。
        :type OcrFullTextConfigure: :class:`taifucloudcloud.vod.v20180717.models.OcrFullTextConfigureInfoForUpdate`
        :param OcrWordsConfigure: 文本關鍵詞識别控制參數。
        :type OcrWordsConfigure: :class:`taifucloudcloud.vod.v20180717.models.OcrWordsConfigureInfoForUpdate`
        :param AsrFullTextConfigure: 語音全文識别控制參數。
        :type AsrFullTextConfigure: :class:`taifucloudcloud.vod.v20180717.models.AsrFullTextConfigureInfoForUpdate`
        :param AsrWordsConfigure: 語音關鍵詞識别控制參數。
        :type AsrWordsConfigure: :class:`taifucloudcloud.vod.v20180717.models.AsrWordsConfigureInfoForUpdate`
        :param ObjectConfigure: 物體識别控制參數。
        :type ObjectConfigure: :class:`taifucloudcloud.vod.v20180717.models.ObjectConfigureInfoForUpdate`
        :param ScreenshotInterval: 截幀間隔，單位爲秒，最小值爲 0.5 秒。
        :type ScreenshotInterval: float
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.HeadTailConfigure = None
        self.FaceConfigure = None
        self.OcrFullTextConfigure = None
        self.OcrWordsConfigure = None
        self.AsrFullTextConfigure = None
        self.AsrWordsConfigure = None
        self.ObjectConfigure = None
        self.ScreenshotInterval = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("HeadTailConfigure") is not None:
            self.HeadTailConfigure = HeadTailConfigureInfoForUpdate()
            self.HeadTailConfigure._deserialize(params.get("HeadTailConfigure"))
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
        if params.get("ObjectConfigure") is not None:
            self.ObjectConfigure = ObjectConfigureInfoForUpdate()
            self.ObjectConfigure._deserialize(params.get("ObjectConfigure"))
        self.ScreenshotInterval = params.get("ScreenshotInterval")
        self.SubAppId = params.get("SubAppId")


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


class ModifyClassRequest(AbstractModel):
    """ModifyClass請求參數結構體

    """

    def __init__(self):
        """
        :param ClassId: 分類 ID
        :type ClassId: int
        :param ClassName: 分類名稱。長度限制：1-64 個字元。
        :type ClassName: str
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.ClassId = None
        self.ClassName = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.ClassId = params.get("ClassId")
        self.ClassName = params.get("ClassName")
        self.SubAppId = params.get("SubAppId")


class ModifyClassResponse(AbstractModel):
    """ModifyClass返回參數結構體

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
        :type PornConfigure: :class:`taifucloudcloud.vod.v20180717.models.PornConfigureInfoForUpdate`
        :param TerrorismConfigure: 鑒恐控制參數。
        :type TerrorismConfigure: :class:`taifucloudcloud.vod.v20180717.models.TerrorismConfigureInfoForUpdate`
        :param PoliticalConfigure: 鑒政控制參數。
        :type PoliticalConfigure: :class:`taifucloudcloud.vod.v20180717.models.PoliticalConfigureInfoForUpdate`
        :param UserDefineConfigure: 用戶自定義内容審核控制參數。
        :type UserDefineConfigure: :class:`taifucloudcloud.vod.v20180717.models.UserDefineConfigureInfoForUpdate`
        :param ScreenshotInterval: 截幀間隔，單位爲秒，最小值爲 0.5 秒。
        :type ScreenshotInterval: float
        :param ReviewWallSwitch: 審核結果是否進入審核牆（對審核結果進行人工複核）的開關。
<li>ON：是；</li>
<li>OFF：否。</li>
        :type ReviewWallSwitch: str
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.PornConfigure = None
        self.TerrorismConfigure = None
        self.PoliticalConfigure = None
        self.UserDefineConfigure = None
        self.ScreenshotInterval = None
        self.ReviewWallSwitch = None
        self.SubAppId = None


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
        if params.get("UserDefineConfigure") is not None:
            self.UserDefineConfigure = UserDefineConfigureInfoForUpdate()
            self.UserDefineConfigure._deserialize(params.get("UserDefineConfigure"))
        self.ScreenshotInterval = params.get("ScreenshotInterval")
        self.ReviewWallSwitch = params.get("ReviewWallSwitch")
        self.SubAppId = params.get("SubAppId")


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


class ModifyMediaInfoRequest(AbstractModel):
    """ModifyMediaInfo請求參數結構體

    """

    def __init__(self):
        """
        :param FileId: 媒體文件唯一標識。
        :type FileId: str
        :param Name: 媒體文件名稱，最長 64 個字元。
        :type Name: str
        :param Description: 媒體文件描述，最長 128 個字元。
        :type Description: str
        :param ClassId: 媒體文件分類 ID。
        :type ClassId: int
        :param ExpireTime: 媒體文件過期時間，采用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。填“9999-12-31T23:59:59Z”表示永不過期。過期後該媒體文件及其相關資源（轉碼結果、雪碧圖等）将被永久删除。
        :type ExpireTime: str
        :param CoverData: 視訊封面圖片文件（如 jpeg, png 等）進行 [Base64](https://tools.ietf.org/html/rfc4648) 編碼後的字串，僅支援 gif、jpeg、png 三種圖片格式。
        :type CoverData: str
        :param AddKeyFrameDescs: 新增的一組視訊打點訊息，如果某個偏移時間已存在打點，則會進行函蓋操作，單個媒體文件最多 100 個打點訊息。同一個請求裏，AddKeyFrameDescs 的時間偏移參數必須與 DeleteKeyFrameDescs 都不同。
        :type AddKeyFrameDescs: list of MediaKeyFrameDescItem
        :param DeleteKeyFrameDescs: 要删除的一組視訊打點訊息的時間偏移，單位：秒。同一個請求裏，AddKeyFrameDescs 的時間偏移參數必須與 DeleteKeyFrameDescs 都不同。
        :type DeleteKeyFrameDescs: list of float
        :param ClearKeyFrameDescs: 取值 1 表示清空視訊打點訊息，其他值無意義。
同一個請求裏，ClearKeyFrameDescs 與 AddKeyFrameDescs 不能同時出現。
        :type ClearKeyFrameDescs: int
        :param AddTags: 新增的一組標簽，單個媒體文件最多 16 個標簽，單個標簽最多 16 個字元。同一個請求裏，AddTags 參數必須與 DeleteTags 都不同。
        :type AddTags: list of str
        :param DeleteTags: 要删除的一組標簽。同一個請求裏，AddTags 參數必須與 DeleteTags 都不同。
        :type DeleteTags: list of str
        :param ClearTags: 取值 1 表示清空媒體文件所有標簽，其他值無意義。
同一個請求裏，ClearTags 與 AddTags 不能同時出現。
        :type ClearTags: int
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID 。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.FileId = None
        self.Name = None
        self.Description = None
        self.ClassId = None
        self.ExpireTime = None
        self.CoverData = None
        self.AddKeyFrameDescs = None
        self.DeleteKeyFrameDescs = None
        self.ClearKeyFrameDescs = None
        self.AddTags = None
        self.DeleteTags = None
        self.ClearTags = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.ClassId = params.get("ClassId")
        self.ExpireTime = params.get("ExpireTime")
        self.CoverData = params.get("CoverData")
        if params.get("AddKeyFrameDescs") is not None:
            self.AddKeyFrameDescs = []
            for item in params.get("AddKeyFrameDescs"):
                obj = MediaKeyFrameDescItem()
                obj._deserialize(item)
                self.AddKeyFrameDescs.append(obj)
        self.DeleteKeyFrameDescs = params.get("DeleteKeyFrameDescs")
        self.ClearKeyFrameDescs = params.get("ClearKeyFrameDescs")
        self.AddTags = params.get("AddTags")
        self.DeleteTags = params.get("DeleteTags")
        self.ClearTags = params.get("ClearTags")
        self.SubAppId = params.get("SubAppId")


class ModifyMediaInfoResponse(AbstractModel):
    """ModifyMediaInfo返回參數結構體

    """

    def __init__(self):
        """
        :param CoverUrl: 新的視訊封面 URL。
* 注意：僅當請求攜帶 CoverData 時此返回值有效。 *
注意：此欄位可能返回 null，表示取不到有效值。
        :type CoverUrl: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CoverUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CoverUrl = params.get("CoverUrl")
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
        :type FaceOperationInfo: :class:`taifucloudcloud.vod.v20180717.models.AiSampleFaceOperation`
        :param TagOperationInfo: 標簽操作訊息。
        :type TagOperationInfo: :class:`taifucloudcloud.vod.v20180717.models.AiSampleTagOperation`
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.PersonId = None
        self.Name = None
        self.Description = None
        self.Usages = None
        self.FaceOperationInfo = None
        self.TagOperationInfo = None
        self.SubAppId = None


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
        self.SubAppId = params.get("SubAppId")


class ModifyPersonSampleResponse(AbstractModel):
    """ModifyPersonSample返回參數結構體

    """

    def __init__(self):
        """
        :param Person: 人物訊息。
        :type Person: :class:`taifucloudcloud.vod.v20180717.models.AiSamplePerson`
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
        :type VideoTemplate: :class:`taifucloudcloud.vod.v20180717.models.VideoTemplateInfoForUpdate`
        :param AudioTemplate: 音訊流配置參數。
        :type AudioTemplate: :class:`taifucloudcloud.vod.v20180717.models.AudioTemplateInfoForUpdate`
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Definition = None
        self.Container = None
        self.Name = None
        self.Comment = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.SubAppId = None


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
        self.SubAppId = params.get("SubAppId")


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
目前，當 Type 爲 image，該欄位僅支援 TopLeft。
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
        :type ImageTemplate: :class:`taifucloudcloud.vod.v20180717.models.ImageWatermarkInputForUpdate`
        :param TextTemplate: 文字浮水印範本，該欄位僅對文字水印範本有效。
        :type TextTemplate: :class:`taifucloudcloud.vod.v20180717.models.TextWatermarkTemplateInputForUpdate`
        :param SvgTemplate: SVG浮水印範本，當 Type 爲 svg，該欄位必填。當 Type 爲 image 或 text，該欄位無效。
        :type SvgTemplate: :class:`taifucloudcloud.vod.v20180717.models.SvgWatermarkInputForUpdate`
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
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
        self.SubAppId = None


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
        self.SubAppId = params.get("SubAppId")


class ModifyWatermarkTemplateResponse(AbstractModel):
    """ModifyWatermarkTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param ImageUrl: 圖片浮水印網址，僅當 ImageTemplate.ImageContent 非空，該欄位有值。
注意：此欄位可能返回 null，表示取不到有效值。
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
        :type TagOperationInfo: :class:`taifucloudcloud.vod.v20180717.models.AiSampleTagOperation`
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Keyword = None
        self.Usages = None
        self.TagOperationInfo = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.Usages = params.get("Usages")
        if params.get("TagOperationInfo") is not None:
            self.TagOperationInfo = AiSampleTagOperation()
            self.TagOperationInfo._deserialize(params.get("TagOperationInfo"))
        self.SubAppId = params.get("SubAppId")


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


class ObjectConfigureInfo(AbstractModel):
    """物體識别任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 物體識别任務開關，可選值：
<li>ON：開啓智慧物體識别任務；</li>
<li>OFF：關閉智慧物體識别任務。</li>
        :type Switch: str
        :param ObjectLibrary: 物體庫選擇，可選值：
<li>Default：使用預設物體庫；</li>
<li>UserDefine：使用用戶自定義物體庫。</li>
<li>All：同時使用預設物體庫和用戶自定義物體庫。</li>
預設值： All，同時使用預設物體庫和用戶自定義物體庫。
        :type ObjectLibrary: str
        """
        self.Switch = None
        self.ObjectLibrary = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.ObjectLibrary = params.get("ObjectLibrary")


class ObjectConfigureInfoForUpdate(AbstractModel):
    """物體識别任務控制參數

    """

    def __init__(self):
        """
        :param Switch: 物體識别任務開關，可選值：
<li>ON：開啓智慧物體識别任務；</li>
<li>OFF：關閉智慧物體識别任務。</li>
        :type Switch: str
        :param ObjectLibrary: 物體庫選擇，可選值：
<li>Default：使用預設物體庫；</li>
<li>UserDefine：使用用戶自定義物體庫。</li>
<li>All：同時使用預設物體庫和用戶自定義物體庫。</li>
        :type ObjectLibrary: str
        """
        self.Switch = None
        self.ObjectLibrary = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.ObjectLibrary = params.get("ObjectLibrary")


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


class OutputAudioStream(AbstractModel):
    """輸出的音訊流訊息

    """

    def __init__(self):
        """
        :param Codec: 音訊流的編碼格式，可選值：
<li>libfdk_aac：适合 mp4 文件。</li>
<li>libmp3lame：适合 mp3 文件。</li>
預設值：libfdk_aac。
        :type Codec: str
        :param SampleRate: 音訊流的采樣率，可選值：
<li>16000</li>
<li>32000</li>
<li>44100</li>
<li>48000</li>
單位：Hz。
預設值：16000。
        :type SampleRate: int
        :param AudioChannel: 音訊聲道數，可選值：
<li>1：單聲道 。</li>
<li>2：雙聲道</li>
預設值：2。
        :type AudioChannel: int
        """
        self.Codec = None
        self.SampleRate = None
        self.AudioChannel = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.SampleRate = params.get("SampleRate")
        self.AudioChannel = params.get("AudioChannel")


class OutputVideoStream(AbstractModel):
    """輸出的視訊流訊息

    """

    def __init__(self):
        """
        :param Codec: 視訊流的編碼格式，可選值：
<li>libx264：H.264 編碼 </li>
預設值：libx264。
        :type Codec: str
        :param Fps: 視訊幀率，取值範圍：[0, 60]，單位：Hz。
預設值：0，表示和第一個視訊軌的第一個視訊片段的視訊幀率一緻。
        :type Fps: int
        """
        self.Codec = None
        self.Fps = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")


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
注意：此欄位可能返回 null，表示取不到有效值。
        :type ImgReviewInfo: :class:`taifucloudcloud.vod.v20180717.models.PoliticalImgReviewTemplateInfo`
        :param AsrReviewInfo: 語音鑒政控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AsrReviewInfo: :class:`taifucloudcloud.vod.v20180717.models.PoliticalAsrReviewTemplateInfo`
        :param OcrReviewInfo: 文本鑒政控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OcrReviewInfo: :class:`taifucloudcloud.vod.v20180717.models.PoliticalOcrReviewTemplateInfo`
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
        :type ImgReviewInfo: :class:`taifucloudcloud.vod.v20180717.models.PoliticalImgReviewTemplateInfoForUpdate`
        :param AsrReviewInfo: 語音鑒政控制參數。
        :type AsrReviewInfo: :class:`taifucloudcloud.vod.v20180717.models.PoliticalAsrReviewTemplateInfoForUpdate`
        :param OcrReviewInfo: 文本鑒政控制參數。
        :type OcrReviewInfo: :class:`taifucloudcloud.vod.v20180717.models.PoliticalOcrReviewTemplateInfoForUpdate`
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
<li>politician：政治人物。</li>
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
<li>politician：政治人物。</li>
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
注意：此欄位可能返回 null，表示取不到有效值。
        :type ImgReviewInfo: :class:`taifucloudcloud.vod.v20180717.models.PornImgReviewTemplateInfo`
        :param AsrReviewInfo: 語音 控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AsrReviewInfo: :class:`taifucloudcloud.vod.v20180717.models.PornAsrReviewTemplateInfo`
        :param OcrReviewInfo: 文本 控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OcrReviewInfo: :class:`taifucloudcloud.vod.v20180717.models.PornOcrReviewTemplateInfo`
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
        :type ImgReviewInfo: :class:`taifucloudcloud.vod.v20180717.models.PornImgReviewTemplateInfoForUpdate`
        :param AsrReviewInfo: 語音 控制參數。
        :type AsrReviewInfo: :class:`taifucloudcloud.vod.v20180717.models.PornAsrReviewTemplateInfoForUpdate`
        :param OcrReviewInfo: 文本 控制參數。
        :type OcrReviewInfo: :class:`taifucloudcloud.vod.v20180717.models.PornOcrReviewTemplateInfoForUpdate`
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


class ProcedureTask(AbstractModel):
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
        :param ErrCode: 錯誤碼
<li>0：成功；</li>
<li>其他值：失敗。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 錯誤訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param FileId: 媒體文件 ID
<li>若流程由 [ProcessMedia](https://cloud.taifucloud.com/document/product/266/33427) 發起，該欄位表示 [MediaInfo](https://cloud.taifucloud.com/document/product/266/31773#MediaInfo) 的 FileId；</li>
<li>若流程由 [ProcessMediaByUrl](https://cloud.taifucloud.com/document/product/266/33426) 發起，該欄位表示 [MediaInputInfo](https://cloud.taifucloud.com/document/product/266/31773#MediaInputInfo) 的 Id。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileId: str
        :param FileName: 媒體文件名稱
<li>若流程由 [ProcessMedia](https://cloud.taifucloud.com/document/product/266/33427) 發起，該欄位表示 [MediaInfo](https://cloud.taifucloud.com/document/product/266/31773#MediaInfo) 的 BasicInfo.Name；</li>
<li>若流程由 [ProcessMediaByUrl](https://cloud.taifucloud.com/document/product/266/33426) 發起，該欄位表示 [MediaInputInfo](https://cloud.taifucloud.com/document/product/266/31773#MediaInputInfo) 的 Name。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileName: str
        :param FileUrl: 媒體文件網址
<li>若流程由 [ProcessMedia](https://cloud.taifucloud.com/document/product/266/33427) 發起，該欄位表示 [MediaInfo](https://cloud.taifucloud.com/document/product/266/31773#MediaInfo) 的 BasicInfo.MediaUrl；</li>
<li>若流程由 [ProcessMediaByUrl](https://cloud.taifucloud.com/document/product/266/33426) 發起，該欄位表示 [MediaInputInfo](https://cloud.taifucloud.com/document/product/266/31773#MediaInputInfo) 的 Url。</li>
        :type FileUrl: str
        :param MetaData: 原始視訊的元訊息。
        :type MetaData: :class:`taifucloudcloud.vod.v20180717.models.MediaMetaData`
        :param MediaProcessResultSet: 視訊處理任務的執行狀态與結果。
注意：此欄位可能返回 null，表示取不到有效值。
        :type MediaProcessResultSet: list of MediaProcessTaskResult
        :param AiContentReviewResultSet: 視訊内容審核任務的執行狀态與結果。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AiContentReviewResultSet: list of AiContentReviewResult
        :param AiAnalysisResultSet: 視訊内容分析任務的執行狀态與結果。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AiAnalysisResultSet: list of AiAnalysisResult
        :param AiRecognitionResultSet: 視訊内容識别任務的執行狀态與結果。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AiRecognitionResultSet: list of AiRecognitionResult
        :param TasksPriority: 任務流的優先級，取值範圍爲 [-10, 10]。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TasksPriority: int
        :param TasksNotifyMode: 任務流狀态變更通知模式。
<li>Finish：只有當任務流全部執行完畢時，才發起一次事件通知；</li>
<li>Change：只要任務流中每個子任務的狀态發生變化，都進行事件通知；</li>
<li>None：不接受該任務流回調。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type TasksNotifyMode: str
        :param SessionContext: 來源上下文，用於透傳用戶請求訊息，任務流狀态變更回調将返回該欄位值，最長 250 個字元。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SessionContext: str
        :param SessionId: 用於去重的識别碼，如果七天内曾有過相同的識别碼的請求，則本次的請求會返回錯誤。最長 50 個字元，不帶或者帶空字串表示不做去重。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SessionId: str
        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.FileId = None
        self.FileName = None
        self.FileUrl = None
        self.MetaData = None
        self.MediaProcessResultSet = None
        self.AiContentReviewResultSet = None
        self.AiAnalysisResultSet = None
        self.AiRecognitionResultSet = None
        self.TasksPriority = None
        self.TasksNotifyMode = None
        self.SessionContext = None
        self.SessionId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.FileId = params.get("FileId")
        self.FileName = params.get("FileName")
        self.FileUrl = params.get("FileUrl")
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
        self.TasksPriority = params.get("TasksPriority")
        self.TasksNotifyMode = params.get("TasksNotifyMode")
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")


class ProcedureTemplate(AbstractModel):
    """任務流範本詳情

    """

    def __init__(self):
        """
        :param Name: 任務流名字。
        :type Name: str
        :param MediaProcessTask: 視訊處理類型任務參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type MediaProcessTask: :class:`taifucloudcloud.vod.v20180717.models.MediaProcessTaskInput`
        :param AiContentReviewTask: AI 智慧内容審核類型任務參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AiContentReviewTask: :class:`taifucloudcloud.vod.v20180717.models.AiContentReviewTaskInput`
        :param AiAnalysisTask: AI 智慧内容分析類型任務參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AiAnalysisTask: :class:`taifucloudcloud.vod.v20180717.models.AiAnalysisTaskInput`
        :param AiRecognitionTask: AI 内容識别類型任務參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AiRecognitionTask: :class:`taifucloudcloud.vod.v20180717.models.AiRecognitionTaskInput`
        :param CreateTime: 範本創建時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type CreateTime: str
        :param UpdateTime: 範本最後修改時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type UpdateTime: str
        """
        self.Name = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
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
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class ProcessMediaByProcedureRequest(AbstractModel):
    """ProcessMediaByProcedure請求參數結構體

    """

    def __init__(self):
        """
        :param FileId: 媒體文件 ID。
        :type FileId: str
        :param ProcedureName: [任務流範本](/document/product/266/11700#.E4.BB.BB.E5.8A.A1.E6.B5.81.E6.A8.A1.E6.9D.BF)名字。
        :type ProcedureName: str
        :param TasksPriority: 任務流的優先級，數值越大優先級越高，取值範圍是-10到10，不填代表0。
        :type TasksPriority: int
        :param TasksNotifyMode: 任務流狀态變更通知模式，可取值有 Finish，Change 和 None，不填代表 Finish。
        :type TasksNotifyMode: str
        :param SessionContext: 來源上下文，用於透傳用戶請求訊息，任務流狀态變更回調将返回該欄位值，最長 250 個字元。
        :type SessionContext: str
        :param SessionId: 用於去重的識别碼，如果一天内曾有過相同的識别碼的請求，則本次的請求會返回錯誤。最長 50 個字元，不帶或者帶空字串表示不做去重。
        :type SessionId: str
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.FileId = None
        self.ProcedureName = None
        self.TasksPriority = None
        self.TasksNotifyMode = None
        self.SessionContext = None
        self.SessionId = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.ProcedureName = params.get("ProcedureName")
        self.TasksPriority = params.get("TasksPriority")
        self.TasksNotifyMode = params.get("TasksNotifyMode")
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")
        self.SubAppId = params.get("SubAppId")


class ProcessMediaByProcedureResponse(AbstractModel):
    """ProcessMediaByProcedure返回參數結構體

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


class ProcessMediaByUrlRequest(AbstractModel):
    """ProcessMediaByUrl請求參數結構體

    """

    def __init__(self):
        """
        :param InputInfo: 輸入視訊訊息，包括視訊 URL ， 名稱、視訊自定義 ID。
        :type InputInfo: :class:`taifucloudcloud.vod.v20180717.models.MediaInputInfo`
        :param OutputInfo: 輸出文件 COS 路徑訊息。
        :type OutputInfo: :class:`taifucloudcloud.vod.v20180717.models.MediaOutputInfo`
        :param AiContentReviewTask: 視訊内容審核類型任務參數。
        :type AiContentReviewTask: :class:`taifucloudcloud.vod.v20180717.models.AiContentReviewTaskInput`
        :param AiAnalysisTask: 視訊内容分析類型任務參數。
        :type AiAnalysisTask: :class:`taifucloudcloud.vod.v20180717.models.AiAnalysisTaskInput`
        :param AiRecognitionTask: 視訊内容識别類型任務參數。
        :type AiRecognitionTask: :class:`taifucloudcloud.vod.v20180717.models.AiRecognitionTaskInput`
        :param TasksPriority: 任務流的優先級，數值越大優先級越高，取值範圍是 -10 到 10，不填代表 0。
        :type TasksPriority: int
        :param TasksNotifyMode: 任務流狀态變更通知模式，可取值有 Finish，Change 和 None，不填代表 Finish。
        :type TasksNotifyMode: str
        :param SessionContext: 來源上下文，用於透傳用戶請求訊息，任務流狀态變更回調将返回該欄位值，最長 250 個字元。
        :type SessionContext: str
        :param SessionId: 用於去重的識别碼，如果七天内曾有過相同的識别碼的請求，則本次的請求會返回錯誤。最長 50 個字元，不帶或者帶空字串表示不做去重。
        :type SessionId: str
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.InputInfo = None
        self.OutputInfo = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.TasksPriority = None
        self.TasksNotifyMode = None
        self.SessionContext = None
        self.SessionId = None
        self.SubAppId = None


    def _deserialize(self, params):
        if params.get("InputInfo") is not None:
            self.InputInfo = MediaInputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        if params.get("OutputInfo") is not None:
            self.OutputInfo = MediaOutputInfo()
            self.OutputInfo._deserialize(params.get("OutputInfo"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        self.TasksPriority = params.get("TasksPriority")
        self.TasksNotifyMode = params.get("TasksNotifyMode")
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")
        self.SubAppId = params.get("SubAppId")


class ProcessMediaByUrlResponse(AbstractModel):
    """ProcessMediaByUrl返回參數結構體

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
        :param FileId: 媒體文件 ID。
        :type FileId: str
        :param MediaProcessTask: 視訊處理類型任務參數。
        :type MediaProcessTask: :class:`taifucloudcloud.vod.v20180717.models.MediaProcessTaskInput`
        :param AiContentReviewTask: 視訊内容審核類型任務參數。
        :type AiContentReviewTask: :class:`taifucloudcloud.vod.v20180717.models.AiContentReviewTaskInput`
        :param AiAnalysisTask: 視訊内容分析類型任務參數。
        :type AiAnalysisTask: :class:`taifucloudcloud.vod.v20180717.models.AiAnalysisTaskInput`
        :param AiRecognitionTask: 視訊内容識别類型任務參數。
        :type AiRecognitionTask: :class:`taifucloudcloud.vod.v20180717.models.AiRecognitionTaskInput`
        :param TasksPriority: 任務流的優先級，數值越大優先級越高，取值範圍是 -10 到 10，不填代表 0。
        :type TasksPriority: int
        :param TasksNotifyMode: 任務流狀态變更通知模式，可取值有 Finish，Change 和 None，不填代表 Finish。
        :type TasksNotifyMode: str
        :param SessionContext: 來源上下文，用於透傳用戶請求訊息，任務流狀态變更回調将返回該欄位值，最長 250 個字元。
        :type SessionContext: str
        :param SessionId: 用於去重的識别碼，如果七天内曾有過相同的識别碼的請求，則本次的請求會返回錯誤。最長 50 個字元，不帶或者帶空字串表示不做去重。
        :type SessionId: str
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.FileId = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.TasksPriority = None
        self.TasksNotifyMode = None
        self.SessionContext = None
        self.SessionId = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
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
        self.TasksPriority = params.get("TasksPriority")
        self.TasksNotifyMode = params.get("TasksNotifyMode")
        self.SessionContext = params.get("SessionContext")
        self.SessionId = params.get("SessionId")
        self.SubAppId = params.get("SubAppId")


class ProcessMediaResponse(AbstractModel):
    """ProcessMedia返回參數結構體

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


class PullEventsRequest(AbstractModel):
    """PullEvents請求參數結構體

    """

    def __init__(self):
        """
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.SubAppId = None


    def _deserialize(self, params):
        self.SubAppId = params.get("SubAppId")


class PullEventsResponse(AbstractModel):
    """PullEvents返回參數結構體

    """

    def __init__(self):
        """
        :param EventSet: 事件清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type EventSet: list of EventContent
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.EventSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EventSet") is not None:
            self.EventSet = []
            for item in params.get("EventSet"):
                obj = EventContent()
                obj._deserialize(item)
                self.EventSet.append(obj)
        self.RequestId = params.get("RequestId")


class PullFileTask(AbstractModel):
    """視訊轉拉任務訊息

    """

    def __init__(self):
        """
        :param TaskId: 轉拉上傳任務 ID。
        :type TaskId: str
        :param ErrCode: 錯誤碼
<li>0：成功；</li>
<li>其他值：失敗。</li>
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param FileId: 轉拉上傳完成後生成的視訊 ID。
        :type FileId: str
        :param MediaBasicInfo: 上傳完成後生成的媒體文件基礎訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type MediaBasicInfo: str
        :param FileUrl: 轉拉上傳完成後生成的播放網址。
        :type FileUrl: str
        :param ProcedureTaskId: 若轉拉上傳時指定了視訊處理流程，則該參數爲流程任務 ID。
        :type ProcedureTaskId: str
        """
        self.TaskId = None
        self.ErrCode = None
        self.Message = None
        self.FileId = None
        self.MediaBasicInfo = None
        self.FileUrl = None
        self.ProcedureTaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.FileId = params.get("FileId")
        self.MediaBasicInfo = params.get("MediaBasicInfo")
        self.FileUrl = params.get("FileUrl")
        self.ProcedureTaskId = params.get("ProcedureTaskId")


class ResetProcedureTemplateRequest(AbstractModel):
    """ResetProcedureTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 任務流名字
        :type Name: str
        :param MediaProcessTask: 視訊處理類型任務參數。
        :type MediaProcessTask: :class:`taifucloudcloud.vod.v20180717.models.MediaProcessTaskInput`
        :param AiContentReviewTask: AI 智慧内容審核類型任務參數。
        :type AiContentReviewTask: :class:`taifucloudcloud.vod.v20180717.models.AiContentReviewTaskInput`
        :param AiAnalysisTask: AI 智慧内容分析類型任務參數。
        :type AiAnalysisTask: :class:`taifucloudcloud.vod.v20180717.models.AiAnalysisTaskInput`
        :param AiRecognitionTask: AI 内容識别類型任務參數。
        :type AiRecognitionTask: :class:`taifucloudcloud.vod.v20180717.models.AiRecognitionTaskInput`
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Name = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
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
        self.SubAppId = params.get("SubAppId")


class ResetProcedureTemplateResponse(AbstractModel):
    """ResetProcedureTemplate返回參數結構體

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
    """對視訊做采樣截圖任務輸入參數類型

    """

    def __init__(self):
        """
        :param Definition: 采樣截圖範本 ID。
        :type Definition: int
        :param WatermarkSet: 浮水印清單，支援多張圖片或文字水印，最大可支援 10 張。
注意：此欄位可能返回 null，表示取不到有效值。
        :type WatermarkSet: list of WatermarkInput
        """
        self.Definition = None
        self.WatermarkSet = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)


class SearchMediaRequest(AbstractModel):
    """SearchMedia請求參數結構體

    """

    def __init__(self):
        """
        :param Text: 搜索文本，模糊比對媒體文件名稱或描述訊息，比對項越多，比對度越高，排序越優先。長度限制：64 個字元。
        :type Text: str
        :param Tags: 標簽集合，比對集合中任意元素。
<li>單個標簽長度限制：8 個字元。</li>
<li>數組長度限制：10。</li>
        :type Tags: list of str
        :param ClassIds: 分類 ID 集合，比對集合指定 ID 的分類及其所有子類。數組長度限制：10。
        :type ClassIds: list of int
        :param StartTime: 創建時間的開始時間。
<li>大於等於開始時間。</li>
<li>格式按照 ISO 8601 標準表示，詳見 [ISO 日期格式說明](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。</li>
        :type StartTime: str
        :param EndTime: 創建時間的結束時間。
<li>小於結束時間。</li>
<li>格式按照 ISO 8601 標準表示，詳見 [ISO 日期格式說明](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。</li>
        :type EndTime: str
        :param SourceType: 媒體文件來源，來源取值參見 [SourceType](https://cloud.taifucloud.com/document/product/266/31773#MediaSourceData)。
        :type SourceType: str
        :param StreamId: 推流[直播碼](https://cloud.taifucloud.com/document/product/267/5959)。
        :type StreamId: str
        :param Vid: 直播錄制文件的唯一標識。
        :type Vid: str
        :param Sort: 排序方式。
<li>Sort.Field 可選值：CreateTime</li>
<li>指定 Text 搜索時，将根據比對度排序，該欄位無效</li>
        :type Sort: :class:`taifucloudcloud.vod.v20180717.models.SortBy`
        :param Offset: 偏移量。
<li>預設值：0。</li>
<li>取值範圍：Offset + Limit 不超過 5000。</li>
        :type Offset: int
        :param Limit: 返回記錄條數，預設值：10。
        :type Limit: int
        :param SubAppId: 點播[子應用](/document/product/266/14574) ID。如果要訪問子應用中的資源，則将該欄位填寫爲子應用 ID；否則無需填寫該欄位。
        :type SubAppId: int
        """
        self.Text = None
        self.Tags = None
        self.ClassIds = None
        self.StartTime = None
        self.EndTime = None
        self.SourceType = None
        self.StreamId = None
        self.Vid = None
        self.Sort = None
        self.Offset = None
        self.Limit = None
        self.SubAppId = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.Tags = params.get("Tags")
        self.ClassIds = params.get("ClassIds")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SourceType = params.get("SourceType")
        self.StreamId = params.get("StreamId")
        self.Vid = params.get("Vid")
        if params.get("Sort") is not None:
            self.Sort = SortBy()
            self.Sort._deserialize(params.get("Sort"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubAppId = params.get("SubAppId")


class SearchMediaResponse(AbstractModel):
    """SearchMedia返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合搜索條件的記錄總數
<li>最大值：5000，即，當命中記錄數超過 5000，該欄位将返回 5000，而非實際命中總數。</li>
        :type TotalCount: int
        :param MediaInfoSet: 媒體文件訊息清單，只包含基礎訊息（BasicInfo）
注意：此欄位可能返回 null，表示取不到有效值。
        :type MediaInfoSet: list of MediaInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.MediaInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("MediaInfoSet") is not None:
            self.MediaInfoSet = []
            for item in params.get("MediaInfoSet"):
                obj = MediaInfo()
                obj._deserialize(item)
                self.MediaInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class SimpleHlsClipRequest(AbstractModel):
    """SimpleHlsClip請求參數結構體

    """

    def __init__(self):
        """
        :param Url: 需要裁剪的Top Cloud 點播 HLS 視訊 URL。
        :type Url: str
        :param StartTimeOffset: 裁剪的開始偏移時間，單位秒。預設 0，即從視訊開頭開始裁剪。負數表示距離視訊結束多少秒開始裁剪。比如 -10 表示從倒數第 10 秒開始裁剪。
        :type StartTimeOffset: float
        :param EndTimeOffset: 裁剪的結束偏移時間，單位秒。預設 0，即裁剪到視訊尾部。負數表示距離視訊結束多少秒結束裁剪。比如 -10 表示到倒數第 10 秒結束裁剪。
        :type EndTimeOffset: float
        """
        self.Url = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")


class SimpleHlsClipResponse(AbstractModel):
    """SimpleHlsClip返回參數結構體

    """

    def __init__(self):
        """
        :param Url: 裁剪後的視訊網址。
        :type Url: str
        :param MetaData: 裁剪後的視訊元訊息。目前`Size`，`Rotate`，`VideoDuration`，`AudioDuration` 幾個欄位暫時缺省，沒有真實數據。
        :type MetaData: :class:`taifucloudcloud.vod.v20180717.models.MediaMetaData`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Url = None
        self.MetaData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        self.RequestId = params.get("RequestId")


class SnapshotByTimeOffset2017(AbstractModel):
    """截圖輸出訊息（2017 版）

    """

    def __init__(self):
        """
        :param ErrCode: 錯誤碼
<li>0：成功；</li>
<li>其他值：失敗。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param TimeOffset: 截圖的具體時間點，單位：毫秒。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TimeOffset: int
        :param Url: 截圖輸出文件網址。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Url: str
        """
        self.ErrCode = None
        self.TimeOffset = None
        self.Url = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.TimeOffset = params.get("TimeOffset")
        self.Url = params.get("Url")


class SnapshotByTimeOffsetTask2017(AbstractModel):
    """視訊指定時間點截圖任務訊息，該結構僅用於 2017 版[指定時間點截圖](https://cloud.taifucloud.com/document/product/266/8102)介面發起的任務。

    """

    def __init__(self):
        """
        :param TaskId: 截圖任務 ID。
        :type TaskId: str
        :param FileId: 截圖文件 ID。
        :type FileId: str
        :param Definition: 截圖規格，參見[指定時間點截圖參數範本](https://cloud.taifucloud.com/document/product/266/33480#.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF)。
        :type Definition: int
        :param SnapshotInfoSet: 截圖結果訊息。
        :type SnapshotInfoSet: list of SnapshotByTimeOffset2017
        """
        self.TaskId = None
        self.FileId = None
        self.Definition = None
        self.SnapshotInfoSet = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.FileId = params.get("FileId")
        self.Definition = params.get("Definition")
        if params.get("SnapshotInfoSet") is not None:
            self.SnapshotInfoSet = []
            for item in params.get("SnapshotInfoSet"):
                obj = SnapshotByTimeOffset2017()
                obj._deserialize(item)
                self.SnapshotInfoSet.append(obj)


class SnapshotByTimeOffsetTaskInput(AbstractModel):
    """對視訊按指定時間點截圖任務輸入參數類型

    """

    def __init__(self):
        """
        :param Definition: 指定時間點截圖範本 ID。
        :type Definition: int
        :param TimeOffsetSet: 截圖時間點清單，單位爲秒。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TimeOffsetSet: list of float
        :param WatermarkSet: 浮水印清單，支援多張圖片或文字水印，最大可支援 10 張。
注意：此欄位可能返回 null，表示取不到有效值。
        :type WatermarkSet: list of WatermarkInput
        """
        self.Definition = None
        self.TimeOffsetSet = None
        self.WatermarkSet = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.TimeOffsetSet = params.get("TimeOffsetSet")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)


class SortBy(AbstractModel):
    """排序依據

    """

    def __init__(self):
        """
        :param Field: 排序欄位
        :type Field: str
        :param Order: 排序方式，可選值：Asc（升序）、Desc（降序）
        :type Order: str
        """
        self.Field = None
        self.Order = None


    def _deserialize(self, params):
        self.Field = params.get("Field")
        self.Order = params.get("Order")


class StickerTrackItem(AbstractModel):
    """貼圖軌上的貼圖訊息。

    """

    def __init__(self):
        """
        :param SourceMedia: 貼圖素材的媒體文件來源。可以是點播的文件 ID，也可以是其它文件的 URL。
        :type SourceMedia: str
        :param Duration: 貼圖的持續時間，單位爲秒。
        :type Duration: float
        :param StartTime: 貼圖在軌道上的起始時間，單位爲秒。
        :type StartTime: float
        :param CoordinateOrigin: 原點位置，取值有：
<li>Center：坐標原點爲中心位置，如畫布中心。</li>
預設值：Center。
        :type CoordinateOrigin: str
        :param XPos: 貼圖原點距離畫布原點的水平位置。支援 %、px 兩種格式：
<li>當字串以 % 結尾，表示貼圖 XPos 爲畫布寬度指定百分比的位置，如 10% 表示 XPos 爲畫布寬度的 10%。</li><li>當字串以 px 結尾，表示貼圖 XPos 單位爲像素，如 100px 表示 XPos 爲 100 像素。</li>
預設值：0px。
        :type XPos: str
        :param YPos: 貼圖原點距離畫布原點的垂直位置。支援 %、px 兩種格式：
<li>當字串以 % 結尾，表示貼圖 YPos 爲畫布高度指定百分比的位置，如 10% 表示 YPos 爲畫布高度的 10%。</li>
<li>當字串以 px 結尾，表示貼圖 YPos 單位爲像素，如 100px 表示 YPos 爲 100 像素。</li>
預設值：0px。
        :type YPos: str
        :param Width: 貼圖的寬度。支援 %、px 兩種格式：
<li>當字串以 % 結尾，表示貼圖 Width 爲畫布寬度的百分比大小，如 10% 表示 Width 爲畫布寬度的 10%。</li>
<li>當字串以 px 結尾，表示貼圖 Width 單位爲像素，如 100px 表示 Width 爲 100 像素。</li>
<li>當 Width、Height 均爲空，則 Width 和 Height 取貼圖素材本身的 Width、Height。</li>
<li>當 Width 爲空0，Height 非空，則 Width 按比例縮放</li>
<li>當 Width 非空，Height 爲空，則 Height 按比例縮放。</li>
        :type Width: str
        :param Height: 貼圖的高度。支援 %、px 兩種格式：
<li>當字串以 % 結尾，表示貼圖 Height 爲畫布高度的百分比大小，如 10% 表示 Height 爲畫布高度的 10%。</li>
<li>當字串以 px 結尾，表示貼圖 Height 單位爲像素，如 100px 表示 Hieght 爲 100 像素。</li>
<li>當 Width、Height 均爲空，則 Width 和 Height 取貼圖素材本身的 Width、Height。</li>
<li>當 Width 爲空，Height 非空，則 Width 按比例縮放</li>
<li>當 Width 非空，Height 爲空，則 Height 按比例縮放。</li>
        :type Height: str
        :param ImageOperations: 對貼圖進行的操作，如圖像旋轉等。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ImageOperations: list of ImageTransform
        """
        self.SourceMedia = None
        self.Duration = None
        self.StartTime = None
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.Width = None
        self.Height = None
        self.ImageOperations = None


    def _deserialize(self, params):
        self.SourceMedia = params.get("SourceMedia")
        self.Duration = params.get("Duration")
        self.StartTime = params.get("StartTime")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        if params.get("ImageOperations") is not None:
            self.ImageOperations = []
            for item in params.get("ImageOperations"):
                obj = ImageTransform()
                obj._deserialize(item)
                self.ImageOperations.append(obj)


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


class TaskSimpleInfo(AbstractModel):
    """任務概要訊息

    """

    def __init__(self):
        """
        :param TaskId: 任務 ID。
        :type TaskId: str
        :param TaskType: 任務類型，取值：
<li>Procedure：視訊處理任務；</li>
<li>EditMedia：視訊編輯任務</li>
<li>WechatDistribute： 發布任務。</li>
兼容 2017 版的任務類型：
<li>Transcode：視訊轉碼任務；</li>
<li>SnapshotByTimeOffset：視訊截圖任務；</li>
<li>Concat：視訊拼接任務；</li>
<li>Clip：視訊剪輯任務；</li>
<li>ImageSprites：截取雪碧圖任務。</li>
        :type TaskType: str
        :param CreatTime: 任務創建時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type CreatTime: str
        :param BeginProcessTime: 任務開始執行時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。若任務尚未開始，該欄位爲空。
注意：此欄位可能返回 null，表示取不到有效值。
        :type BeginProcessTime: str
        :param FinishTime: 任務結束時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。若任務尚未完成，該欄位爲空。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FinishTime: str
        """
        self.TaskId = None
        self.TaskType = None
        self.CreatTime = None
        self.BeginProcessTime = None
        self.FinishTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskType = params.get("TaskType")
        self.CreatTime = params.get("CreatTime")
        self.BeginProcessTime = params.get("BeginProcessTime")
        self.FinishTime = params.get("FinishTime")


class TempCertificate(AbstractModel):
    """臨時憑證

    """

    def __init__(self):
        """
        :param SecretId: 臨時安全證書 Id。
        :type SecretId: str
        :param SecretKey: 臨時安全證書 Key。
        :type SecretKey: str
        :param Token: Token 值。
        :type Token: str
        :param ExpiredTime: 證書無效的時間，返回 Unix 時間戳，精确到秒。
        :type ExpiredTime: int
        """
        self.SecretId = None
        self.SecretKey = None
        self.Token = None
        self.ExpiredTime = None


    def _deserialize(self, params):
        self.SecretId = params.get("SecretId")
        self.SecretKey = params.get("SecretKey")
        self.Token = params.get("Token")
        self.ExpiredTime = params.get("ExpiredTime")


class TerrorismConfigureInfo(AbstractModel):
    """鑒恐任務控制參數

    """

    def __init__(self):
        """
        :param ImgReviewInfo: 畫面鑒恐任務控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ImgReviewInfo: :class:`taifucloudcloud.vod.v20180717.models.TerrorismImgReviewTemplateInfo`
        """
        self.ImgReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = TerrorismImgReviewTemplateInfo()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))


class TerrorismConfigureInfoForUpdate(AbstractModel):
    """鑒恐任務控制參數。

    """

    def __init__(self):
        """
        :param ImgReviewInfo: 畫面鑒恐任務控制參數。
        :type ImgReviewInfo: :class:`taifucloudcloud.vod.v20180717.models.TerrorismImgReviewTemplateInfoForUpdate`
        """
        self.ImgReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = TerrorismImgReviewTemplateInfoForUpdate()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))


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


class TextWatermarkTemplateInput(AbstractModel):
    """文字浮水印範本

    """

    def __init__(self):
        """
        :param FontType: 字體類型，目前僅支援 arial.ttf。
        :type FontType: str
        :param FontSize: 字體大小，格式：Npx，N 爲數值。
        :type FontSize: str
        :param FontColor: 字體顔色，格式：0xRRGGBB，預設值：0xFFFFFF（黑色）。
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
        :param FontType: 字體類型，目前僅支援 arial.ttf。
        :type FontType: str
        :param FontSize: 字體大小，格式：Npx，N 爲數值。
        :type FontSize: str
        :param FontColor: 字體顔色，格式：0xRRGGBB，預設值：0xFFFFFF（黑色）。
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


class TranscodePlayInfo2017(AbstractModel):
    """視訊轉碼播放訊息（2017 版）

    """

    def __init__(self):
        """
        :param Url: 播放網址。
        :type Url: str
        :param Definition: 轉碼規格 ID，參見[轉碼參數範本](https://cloud.taifucloud.com/document/product/266/33478#.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF)。
        :type Definition: int
        :param Bitrate: 視訊流碼率平均值與音訊流碼率平均值之和， 單位：bps。
        :type Bitrate: int
        :param Height: 視訊流高度的最大值，單位：px。
        :type Height: int
        :param Width: 視訊流寬度的最大值，單位：px。
        :type Width: int
        """
        self.Url = None
        self.Definition = None
        self.Bitrate = None
        self.Height = None
        self.Width = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.Definition = params.get("Definition")
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")


class TranscodeTask2017(AbstractModel):
    """視訊轉碼任務訊息，該結構僅用於對 2017 版[視訊轉碼](https://cloud.taifucloud.com/document/product/266/7822)介面發起的任務。

    """

    def __init__(self):
        """
        :param TaskId: 轉碼任務 ID。
        :type TaskId: str
        :param ErrCode: 錯誤碼
<li>0：成功；</li>
<li>其他值：失敗。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 錯誤訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param FileId: 被轉碼文件 ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileId: str
        :param FileName: 被轉碼文件名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileName: str
        :param Duration: 視訊時長，單位：秒。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Duration: int
        :param CoverUrl: 封面網址。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CoverUrl: str
        :param PlayInfoSet: 視訊轉碼後生成的播放訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PlayInfoSet: list of TranscodePlayInfo2017
        """
        self.TaskId = None
        self.ErrCode = None
        self.Message = None
        self.FileId = None
        self.FileName = None
        self.Duration = None
        self.CoverUrl = None
        self.PlayInfoSet = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.FileId = params.get("FileId")
        self.FileName = params.get("FileName")
        self.Duration = params.get("Duration")
        self.CoverUrl = params.get("CoverUrl")
        if params.get("PlayInfoSet") is not None:
            self.PlayInfoSet = []
            for item in params.get("PlayInfoSet"):
                obj = TranscodePlayInfo2017()
                obj._deserialize(item)
                self.PlayInfoSet.append(obj)


class TranscodeTaskInput(AbstractModel):
    """轉碼任務輸入參數類型

    """

    def __init__(self):
        """
        :param Definition: 視訊轉碼範本 ID。
        :type Definition: int
        :param WatermarkSet: 浮水印清單，支援多張圖片或文字水印，最大可支援 10 張。
注意：此欄位可能返回 null，表示取不到有效值。
        :type WatermarkSet: list of WatermarkInput
        """
        self.Definition = None
        self.WatermarkSet = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)


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
注意：此欄位可能返回 null，表示取不到有效值。
        :type Name: str
        :param Comment: 範本描述訊息。
注意：此欄位可能返回 null，表示取不到有效值。
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
注意：此欄位可能返回 null，表示取不到有效值。
        :type VideoTemplate: :class:`taifucloudcloud.vod.v20180717.models.VideoTemplateInfo`
        :param AudioTemplate: 音訊流配置參數，僅當 RemoveAudio 爲 0，該欄位有效 。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AudioTemplate: :class:`taifucloudcloud.vod.v20180717.models.AudioTemplateInfo`
        :param ContainerType: 封裝格式過濾條件，可選值：
<li>Video：視訊格式，可以同時包含視訊流和音訊流的封裝格式；</li>
<li>PureAudio：純音訊格式，只能包含音訊流的封裝格式板。</li>
        :type ContainerType: str
        :param CreateTime: 範本創建時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type CreateTime: str
        :param UpdateTime: 範本最後修改時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
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
        self.ContainerType = params.get("ContainerType")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class TransitionOpertion(AbstractModel):
    """轉場操作

    """

    def __init__(self):
        """
        :param Type: 轉場類型，取值有：
<ul>
<li>圖像的轉場操作，用於兩個視訊片段圖像間的轉場處理：
<ul>
<li>ImageFadeInFadeOut：圖像淡入淡出。 </li>
<li>BowTieHorizontal：水平蝴蝶結。 </li>
<li>BowTieVertical：垂直蝴蝶結。 </li>
<li>ButterflyWaveScrawler：晃動。 </li>
<li>Cannabisleaf：楓葉。 </li>
<li>Circle：弧形收放。 </li>
<li>CircleCrop：圓環聚攏。 </li>
<li>Circleopen：橢圓聚攏。 </li>
<li>Crosswarp：橫向翹曲。 </li>
<li>Cube：立方體。 </li>
<li>DoomScreenTransition：幕布。 </li>
<li>Doorway：門廊。 </li>
<li>Dreamy：波浪。 </li>
<li>DreamyZoom：水平聚攏。 </li>
<li>FilmBurn：火燒雲。 </li>
<li>GlitchMemories：抖動。 </li>
<li>Heart：心形。 </li>
<li>InvertedPageCurl：翻頁。 </li>
<li>Luma：腐蝕。 </li>
<li>Mosaic：九宮格。 </li>
<li>Pinwheel：風車。 </li>
<li>PolarFunction：橢圓擴散。 </li>
<li>PolkaDotsCurtain：弧形擴散。 </li>
<li>Radial：雷達掃描 </li>
<li>RotateScaleFade：上下收放。 </li>
<li>Squeeze：上下聚攏。 </li>
<li>Swap：放大切換。 </li>
<li>Swirl：螺旋。 </li>
<li>UndulatingBurnOutSwirl：水流蔓延。 </li>
<li>Windowblinds：百葉窗。 </li>
<li>WipeDown：向下收起。 </li>
<li>WipeLeft：向左收起。 </li>
<li>WipeRight：向右收起。 </li>
<li>WipeUp：向上收起。 </li>
<li>ZoomInCircles：水波紋。 </li>
</ul>
</li>
<li>音訊的轉場操作，用於兩個音訊片段間的轉場處理：
<ul>
<li>AudioFadeInFadeOut：聲音淡入淡出。 </li>
</ul>
</li>
</ul>
        :type Type: str
        """
        self.Type = None


    def _deserialize(self, params):
        self.Type = params.get("Type")


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
注意：此欄位可能返回 null，表示取不到有效值。
        :type FaceReviewInfo: :class:`taifucloudcloud.vod.v20180717.models.UserDefineFaceReviewTemplateInfo`
        :param AsrReviewInfo: 用戶自定義語音審核控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AsrReviewInfo: :class:`taifucloudcloud.vod.v20180717.models.UserDefineAsrTextReviewTemplateInfo`
        :param OcrReviewInfo: 用戶自定義文本審核控制參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OcrReviewInfo: :class:`taifucloudcloud.vod.v20180717.models.UserDefineOcrTextReviewTemplateInfo`
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
        :type FaceReviewInfo: :class:`taifucloudcloud.vod.v20180717.models.UserDefineFaceReviewTemplateInfoForUpdate`
        :param AsrReviewInfo: 用戶自定義語音審核控制參數。
        :type AsrReviewInfo: :class:`taifucloudcloud.vod.v20180717.models.UserDefineAsrTextReviewTemplateInfoForUpdate`
        :param OcrReviewInfo: 用戶自定義文本審核控制參數。
        :type OcrReviewInfo: :class:`taifucloudcloud.vod.v20180717.models.UserDefineOcrTextReviewTemplateInfoForUpdate`
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


class VideoTemplateInfo(AbstractModel):
    """視訊流配置參數

    """

    def __init__(self):
        """
        :param Codec: 視訊流的編碼格式，可選值：
<li>libx264：H.264 編碼</li>
<li>libx265：H.265 編碼</li>
目前 H.265 編碼必須指定分辨率，並且需要在 640*480 以内。
        :type Codec: str
        :param Fps: 視訊幀率，取值範圍：[0, 60]，單位：Hz。
當取值爲 0，表示幀率和原始視訊保持一緻。
        :type Fps: int
        :param Bitrate: 視訊流的碼率，取值範圍：0 和 [128, 35000]，單位：kbps。
當取值爲 0，表示視訊碼率和原始視訊保持一緻。
        :type Bitrate: int
        :param ResolutionAdaptive: 分辨率自适應，可選值：
<li>open：開啓，此時，Width 代表視訊的寬度，Height 表示視訊的高度；</li>
<li>close：關閉，此時，Width 代表視訊的長邊，Height 表示視訊的短邊。</li>
預設值：open。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResolutionAdaptive: str
        :param Width: 視訊流寬度（或長邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Width: int
        :param Height: 視訊流高度（或短邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
預設值：0。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Height: int
        """
        self.Codec = None
        self.Fps = None
        self.Bitrate = None
        self.ResolutionAdaptive = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        self.Bitrate = params.get("Bitrate")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class VideoTemplateInfoForUpdate(AbstractModel):
    """視訊流配置參數

    """

    def __init__(self):
        """
        :param Codec: 視訊流的編碼格式，可選值：
<li>libx264：H.264 編碼</li>
<li>libx265：H.265 編碼</li>
目前 H.265 編碼必須指定分辨率，並且需要在 640*480 以内。
        :type Codec: str
        :param Fps: 視訊幀率，取值範圍：[0, 60]，單位：Hz。
當取值爲 0，表示幀率和原始視訊保持一緻。
        :type Fps: int
        :param Bitrate: 視訊流的碼率，取值範圍：0 和 [128, 35000]，單位：kbps。
當取值爲 0，表示視訊碼率和原始視訊保持一緻。
        :type Bitrate: int
        :param ResolutionAdaptive: 分辨率自适應，可選值：
<li>open：開啓，此時，Width 代表視訊的寬度，Height 表示視訊的高度；</li>
<li>close：關閉，此時，Width 代表視訊的長邊，Height 表示視訊的短邊。</li>
        :type ResolutionAdaptive: str
        :param Width: 視訊流寬度（或長邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
<li>當 Width、Height 均爲 0，則分辨率同源；</li>
<li>當 Width 爲 0，Height 非 0，則 Width 按比例縮放；</li>
<li>當 Width 非 0，Height 爲 0，則 Height 按比例縮放；</li>
<li>當 Width、Height 均非 0，則分辨率按用戶指定。</li>
        :type Width: int
        :param Height: 視訊流高度（或短邊）的最大值，取值範圍：0 和 [128, 4096]，單位：px。
        :type Height: int
        """
        self.Codec = None
        self.Fps = None
        self.Bitrate = None
        self.ResolutionAdaptive = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        self.Bitrate = params.get("Bitrate")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class VideoTrackItem(AbstractModel):
    """視訊軌的視訊片段訊息。

    """

    def __init__(self):
        """
        :param SourceMedia: 視訊片段的媒體素材來源，可以是點播的文件 ID，或者是其它文件的 URL。
        :type SourceMedia: str
        :param SourceMediaStartTime: 視訊片段取自素材文件的起始時間，單位爲秒。預設爲0。
        :type SourceMediaStartTime: float
        :param Duration: 視訊片段時長，單位爲秒。預設取視訊素材本身長度，表示截取全部素材。如果源文件是圖片，Duration需要大於0。
        :type Duration: float
        :param CoordinateOrigin: 視訊原點位置，取值有：
<li>Center：坐標原點爲中心位置，如畫布中心。</li>
預設值 ：Center。
        :type CoordinateOrigin: str
        :param XPos: 視訊片段原點距離畫布原點的水平位置。支援 %、px 兩種格式：
<li>當字串以 % 結尾，表示視訊片段 XPos 爲畫布寬度指定百分比的位置，如 10% 表示 XPos 爲畫布口寬度的 10%。</li>
<li>當字串以 px 結尾，表示視訊片段 XPos 單位爲像素，如 100px 表示 XPos 爲100像素。</li>
預設值：0px。
        :type XPos: str
        :param YPos: 視訊片段原點距離畫布原點的垂直位置。支援 %、px 兩種格式：
<li>當字串以 % 結尾，表示視訊片段 YPos 爲畫布高度指定百分比的位置，如 10% 表示 YPos 爲畫布高度的 10%。</li>
<li>當字串以 px 結尾，表示視訊片段 YPos 單位爲像素，如 100px 表示 YPos 爲100像素。</li>
預設值：0px。
        :type YPos: str
        :param Width: 視訊片段的寬度。支援 %、px 兩種格式：
<li>當字串以 % 結尾，表示視訊片段 Width 爲畫布寬度的百分比大小，如 10% 表示 Width 爲畫布寬度的 10%。</li>
<li>當字串以 px 結尾，表示視訊片段 Width 單位爲像素，如 100px 表示 Width 爲100像素。</li>
<li>當 Width、Height 均爲空，則 Width 和 Height 取視訊素材本身的 Width、Height。</li>
<li>當 Width 爲空，Height 非空，則 Width 按比例縮放</li>
<li>當 Width 非空，Height 爲空，則 Height 按比例縮放。</li>
        :type Width: str
        :param Height: 視訊片段的高度。支援 %、px 兩種格式：
<li>當字串以 % 結尾，表示視訊片段 Height 爲畫布高度的百分比大小，如 10% 表示 Height 爲畫布高度的 10%；
</li><li>當字串以 px 結尾，表示視訊片段 Height 單位爲像素，如 100px 表示 Height 爲100像素。</li>
<li>當 Width、Height 均爲空，則 Width 和 Height 取視訊素材本身的 Width、Height。</li>
<li>當 Width 爲空，Height 非空，則 Width 按比例縮放</li>
<li>當 Width 非空，Height 爲空，則 Height 按比例縮放。</li>
        :type Height: str
        :param ImageOperations: 對圖像進行的操作，如圖像旋轉等。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ImageOperations: list of ImageTransform
        :param AudioOperations: 對音訊進行操作，如靜音等。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AudioOperations: list of AudioTransform
        """
        self.SourceMedia = None
        self.SourceMediaStartTime = None
        self.Duration = None
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.Width = None
        self.Height = None
        self.ImageOperations = None
        self.AudioOperations = None


    def _deserialize(self, params):
        self.SourceMedia = params.get("SourceMedia")
        self.SourceMediaStartTime = params.get("SourceMediaStartTime")
        self.Duration = params.get("Duration")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        if params.get("ImageOperations") is not None:
            self.ImageOperations = []
            for item in params.get("ImageOperations"):
                obj = ImageTransform()
                obj._deserialize(item)
                self.ImageOperations.append(obj)
        if params.get("AudioOperations") is not None:
            self.AudioOperations = []
            for item in params.get("AudioOperations"):
                obj = AudioTransform()
                obj._deserialize(item)
                self.AudioOperations.append(obj)


class WatermarkInput(AbstractModel):
    """視訊處理任務中的浮水印參數類型

    """

    def __init__(self):
        """
        :param Definition: 浮水印範本 ID。
        :type Definition: int
        :param TextContent: 文字内容，長度不超過100個字元。僅當浮水印類型爲文字水印時填寫。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TextContent: str
        :param SvgContent: SVG 内容。長度不超過 2000000 個字元。僅當浮水印類型爲 SVG 水印時填寫。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SvgContent: str
        """
        self.Definition = None
        self.TextContent = None
        self.SvgContent = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.TextContent = params.get("TextContent")
        self.SvgContent = params.get("SvgContent")


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
注意：此欄位可能返回 null，表示取不到有效值。
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
        :type ImageTemplate: :class:`taifucloudcloud.vod.v20180717.models.ImageWatermarkTemplate`
        :param TextTemplate: 文字浮水印範本，僅當 Type 爲 text，該欄位有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TextTemplate: :class:`taifucloudcloud.vod.v20180717.models.TextWatermarkTemplateInput`
        :param SvgTemplate: SVG 浮水印範本，當 Type 爲 svg，該欄位有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SvgTemplate: :class:`taifucloudcloud.vod.v20180717.models.SvgWatermarkInput`
        :param CreateTime: 範本創建時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
        :type CreateTime: str
        :param UpdateTime: 範本最後修改時間，使用 [ISO 日期格式](https://cloud.taifucloud.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。
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


class WechatMiniProgramPublishTask(AbstractModel):
    """ 小程式發布任務訊息

    """

    def __init__(self):
        """
        :param TaskId: 任務 ID。
        :type TaskId: str
        :param Status: 任務狀态，取值：
WAITING：等待中；
PROCESSING：處理中；
FINISH：已完成。
        :type Status: str
        :param ErrCode: 錯誤碼
<li>0：成功；</li>
<li>其他值：失敗。</li>
        :type ErrCode: int
        :param Message: 錯誤訊息。
        :type Message: str
        :param FileId: 發布視訊文件 ID。
        :type FileId: str
        :param SourceDefinition: 發布視訊所對應的轉碼範本 ID，爲 0 代表原始視訊。
        :type SourceDefinition: int
        :param PublishResult:  小程式視訊發布狀态，取值：
<li>Pass：成功；</li>
<li>Rejected：審核未通過。</li>
        :type PublishResult: str
        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.FileId = None
        self.SourceDefinition = None
        self.PublishResult = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.FileId = params.get("FileId")
        self.SourceDefinition = params.get("SourceDefinition")
        self.PublishResult = params.get("PublishResult")


class WechatPublishTask(AbstractModel):
    """ 發布任務訊息

    """

    def __init__(self):
        """
        :param TaskId: 任務 ID。
        :type TaskId: str
        :param Status: 任務狀态，取值：
WAITING：等待中；
PROCESSING：處理中；
FINISH：已完成。
        :type Status: str
        :param ErrCode: 錯誤碼
<li>0：成功；</li>
<li>其他值：失敗。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type ErrCode: int
        :param Message: 錯誤訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Message: str
        :param FileId: 發布視訊文件 ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileId: str
        :param Definition:  發布範本 ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Definition: int
        :param SourceDefinition: 發布視訊所對應的轉碼範本 ID，爲 0 代表原始視訊。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SourceDefinition: int
        :param WechatStatus:  發布狀态，取值：
<li>FAIL：失敗；</li>
<li>SUCCESS：成功；</li>
<li>AUDITNOTPASS：審核未通過；</li>
<li>NOTTRIGGERED：尚未發起 發布。</li>
注意：此欄位可能返回 null，表示取不到有效值。
        :type WechatStatus: str
        :param WechatVid:   Vid。
注意：此欄位可能返回 null，表示取不到有效值。
        :type WechatVid: str
        :param WechatUrl:  網址。
注意：此欄位可能返回 null，表示取不到有效值。
        :type WechatUrl: str
        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.FileId = None
        self.Definition = None
        self.SourceDefinition = None
        self.WechatStatus = None
        self.WechatVid = None
        self.WechatUrl = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.FileId = params.get("FileId")
        self.Definition = params.get("Definition")
        self.SourceDefinition = params.get("SourceDefinition")
        self.WechatStatus = params.get("WechatStatus")
        self.WechatVid = params.get("WechatVid")
        self.WechatUrl = params.get("WechatUrl")