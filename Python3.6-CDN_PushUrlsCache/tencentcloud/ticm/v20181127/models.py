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


class Candidate(AbstractModel):
    """識别出人臉對應的候選人。

    """

    def __init__(self):
        """
        :param Name: 識别出人臉對應的候選人數組。當前返回相似度最高的候選人。
        :type Name: str
        :param Confidence: 相似度，0-100之間。
        :type Confidence: int
        """
        self.Name = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Confidence = params.get("Confidence")


class DescribeVideoTaskRequest(AbstractModel):
    """DescribeVideoTask請求參數結構體

    """

    def __init__(self):
        """
        :param VodTaskId: 需要查詢的視訊審核的任務ID
        :type VodTaskId: str
        """
        self.VodTaskId = None


    def _deserialize(self, params):
        self.VodTaskId = params.get("VodTaskId")


class DescribeVideoTaskResponse(AbstractModel):
    """DescribeVideoTask返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 任務狀态，取值：
WAITING：等待中；
PROCESSING：處理中；
FINISH：已完成。
        :type Status: str
        :param BeginProcessTime: 任務開始執行的時間，采用 ISO 日期格式。
        :type BeginProcessTime: str
        :param FinishTime: 任務執行完畢的時間，采用 ISO 日期格式。
        :type FinishTime: str
        :param PornResult: 視訊内容審核智慧畫面鑒黃任務的查詢結果。
        :type PornResult: :class:`tencentcloud.ticm.v20181127.models.VodPornReviewResult`
        :param TerrorismResult: 視訊内容審核智慧畫面鑒恐任務的查詢結果。
        :type TerrorismResult: :class:`tencentcloud.ticm.v20181127.models.VodTerrorismReviewResult`
        :param PoliticalResult: 視訊内容審核智慧畫面鑒政任務的查詢結果。
        :type PoliticalResult: :class:`tencentcloud.ticm.v20181127.models.VodPoliticalReviewResult`
        :param PoliticalOcrResult: 視訊内容審核 Ocr 文字鑒政任務的查詢結果。
        :type PoliticalOcrResult: :class:`tencentcloud.ticm.v20181127.models.VodPoliticalOcrReviewResult`
        :param PornAsrResult: 視訊内容審核 Asr 文字鑒黃任務的查詢結果。
        :type PornAsrResult: :class:`tencentcloud.ticm.v20181127.models.VodPornAsrReviewResult`
        :param PoliticalAsrResult: 視訊内容審核 Asr 文字鑒政任務的查詢結果。
        :type PoliticalAsrResult: :class:`tencentcloud.ticm.v20181127.models.VodPoliticalAsrReviewResult`
        :param PornOcrResult: 視訊内容審核 Ocr 文字鑒黃任務的查詢結果。
        :type PornOcrResult: :class:`tencentcloud.ticm.v20181127.models.VodPornOcrResult`
        :param MetaData: 原始視訊的元訊息。
        :type MetaData: :class:`tencentcloud.ticm.v20181127.models.VodMetaData`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.BeginProcessTime = None
        self.FinishTime = None
        self.PornResult = None
        self.TerrorismResult = None
        self.PoliticalResult = None
        self.PoliticalOcrResult = None
        self.PornAsrResult = None
        self.PoliticalAsrResult = None
        self.PornOcrResult = None
        self.MetaData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.BeginProcessTime = params.get("BeginProcessTime")
        self.FinishTime = params.get("FinishTime")
        if params.get("PornResult") is not None:
            self.PornResult = VodPornReviewResult()
            self.PornResult._deserialize(params.get("PornResult"))
        if params.get("TerrorismResult") is not None:
            self.TerrorismResult = VodTerrorismReviewResult()
            self.TerrorismResult._deserialize(params.get("TerrorismResult"))
        if params.get("PoliticalResult") is not None:
            self.PoliticalResult = VodPoliticalReviewResult()
            self.PoliticalResult._deserialize(params.get("PoliticalResult"))
        if params.get("PoliticalOcrResult") is not None:
            self.PoliticalOcrResult = VodPoliticalOcrReviewResult()
            self.PoliticalOcrResult._deserialize(params.get("PoliticalOcrResult"))
        if params.get("PornAsrResult") is not None:
            self.PornAsrResult = VodPornAsrReviewResult()
            self.PornAsrResult._deserialize(params.get("PornAsrResult"))
        if params.get("PoliticalAsrResult") is not None:
            self.PoliticalAsrResult = VodPoliticalAsrReviewResult()
            self.PoliticalAsrResult._deserialize(params.get("PoliticalAsrResult"))
        if params.get("PornOcrResult") is not None:
            self.PornOcrResult = VodPornOcrResult()
            self.PornOcrResult._deserialize(params.get("PornOcrResult"))
        if params.get("MetaData") is not None:
            self.MetaData = VodMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        self.RequestId = params.get("RequestId")


class DisgustResult(AbstractModel):
    """惡心識别結果。

    """

    def __init__(self):
        """
        :param Code: 該識别場景的錯誤碼：
0表示成功，
-1表示系統錯誤，
-2表示引擎錯誤。
        :type Code: int
        :param Msg: 錯誤碼描述訊息。
        :type Msg: str
        :param Suggestion: 識别場景的審核結論：
PASS：正常
REVIEW：疑似
BLOCK：違規
        :type Suggestion: str
        :param Confidence: 圖像惡心的分數，0-100之間，分數越高惡心幾率越大。
        :type Confidence: int
        """
        self.Code = None
        self.Msg = None
        self.Suggestion = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        self.Suggestion = params.get("Suggestion")
        self.Confidence = params.get("Confidence")


class FaceRect(AbstractModel):
    """識别出的人臉在圖片中的位置。

    """

    def __init__(self):
        """
        :param X: 人臉區域左上角橫坐标。
        :type X: int
        :param Y: 人臉區域左上角縱坐标。
        :type Y: int
        :param Width: 人臉區域寬度。
        :type Width: int
        :param Height: 人臉區域高度。
        :type Height: int
        """
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class FaceResult(AbstractModel):
    """人臉識别結果。

    """

    def __init__(self):
        """
        :param FaceRect: 檢測出的人臉框位置。
        :type FaceRect: :class:`tencentcloud.ticm.v20181127.models.FaceRect`
        :param Candidates: 候選人清單。當前返回相似度最高的候選人。
        :type Candidates: list of Candidate
        """
        self.FaceRect = None
        self.Candidates = None


    def _deserialize(self, params):
        if params.get("FaceRect") is not None:
            self.FaceRect = FaceRect()
            self.FaceRect._deserialize(params.get("FaceRect"))
        if params.get("Candidates") is not None:
            self.Candidates = []
            for item in params.get("Candidates"):
                obj = Candidate()
                obj._deserialize(item)
                self.Candidates.append(obj)


class ImageModerationRequest(AbstractModel):
    """ImageModeration請求參數結構體

    """

    def __init__(self):
        """
        :param Scenes: 本次調用支援的識别場景，可選值如下：
1. PORN，即色情識别
2. TERRORISM，即暴恐識别
3. POLITICS，即政治敏感識别

支援多場景（Scenes）一起檢測。例如，使用 Scenes=["PORN", "TERRORISM"]，即對一張圖片同時進行色情識别和暴恐識别。
        :type Scenes: list of str
        :param ImageUrl: 圖片URL網址。 
圖片限制： 
 • 圖片格式：PNG、JPG、JPEG。 
 • 圖片大小：所下載圖片經Base64編碼後不超過4M。圖片下載時間不超過3秒。 
 • 圖片像素：大于50*50像素，否則影響識别效果； 
 • 長寬比：長邊：短邊<5； 
介面響應時間會受到圖片下載時間的影響，建議使用更可靠的儲存服務，推薦将圖片儲存在Top Cloud COS。
        :type ImageUrl: str
        :param Config: 預留欄位，後期用于展示更多識别訊息。
        :type Config: str
        :param Extra: 透傳欄位，透傳簡單訊息。
        :type Extra: str
        :param ImageBase64: 圖片經過base64編碼的内容。最大不超過4M。與ImageUrl同時存在時優先使用ImageUrl欄位。
        :type ImageBase64: str
        """
        self.Scenes = None
        self.ImageUrl = None
        self.Config = None
        self.Extra = None
        self.ImageBase64 = None


    def _deserialize(self, params):
        self.Scenes = params.get("Scenes")
        self.ImageUrl = params.get("ImageUrl")
        self.Config = params.get("Config")
        self.Extra = params.get("Extra")
        self.ImageBase64 = params.get("ImageBase64")


class ImageModerationResponse(AbstractModel):
    """ImageModeration返回參數結構體

    """

    def __init__(self):
        """
        :param Suggestion: 識别場景的審核結論：
PASS：正常
REVIEW：疑似
BLOCK：違規
        :type Suggestion: str
        :param PornResult: 色情識别結果。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PornResult: :class:`tencentcloud.ticm.v20181127.models.PornResult`
        :param TerrorismResult: 暴恐識别結果。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TerrorismResult: :class:`tencentcloud.ticm.v20181127.models.TerrorismResult`
        :param PoliticsResult: 政治敏感識别結果。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PoliticsResult: :class:`tencentcloud.ticm.v20181127.models.PoliticsResult`
        :param Extra: 透傳欄位，透傳簡單訊息。
        :type Extra: str
        :param DisgustResult: 惡心内容識别結果。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DisgustResult: :class:`tencentcloud.ticm.v20181127.models.DisgustResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Suggestion = None
        self.PornResult = None
        self.TerrorismResult = None
        self.PoliticsResult = None
        self.Extra = None
        self.DisgustResult = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Suggestion = params.get("Suggestion")
        if params.get("PornResult") is not None:
            self.PornResult = PornResult()
            self.PornResult._deserialize(params.get("PornResult"))
        if params.get("TerrorismResult") is not None:
            self.TerrorismResult = TerrorismResult()
            self.TerrorismResult._deserialize(params.get("TerrorismResult"))
        if params.get("PoliticsResult") is not None:
            self.PoliticsResult = PoliticsResult()
            self.PoliticsResult._deserialize(params.get("PoliticsResult"))
        self.Extra = params.get("Extra")
        if params.get("DisgustResult") is not None:
            self.DisgustResult = DisgustResult()
            self.DisgustResult._deserialize(params.get("DisgustResult"))
        self.RequestId = params.get("RequestId")


class PoliticsResult(AbstractModel):
    """政治敏感識别結果。

    """

    def __init__(self):
        """
        :param Code: 該識别場景的錯誤碼：
0表示成功，
-1表示系統錯誤，
-2表示引擎錯誤，
-1400表示圖片解碼失敗，
-1401表示圖片不符合規範。
        :type Code: int
        :param Msg: 錯誤碼描述訊息。
        :type Msg: str
        :param Suggestion: 識别場景的審核結論：
PASS：正常
REVIEW：疑似
BLOCK：違規
        :type Suggestion: str
        :param Confidence: 圖像涉政的分數，0-100之間，分數越高涉政幾率越大。
Type爲DNA時：
0到75，Suggestion建議爲PASS
75到90，Suggestion建議爲REVIEW
90到100，Suggestion建議爲BLOCK
Type爲FACE時：
0到55，Suggestion建議爲PASS
55到60，Suggestion建議爲REVIEW
60到100，Suggestion建議爲BLOCK
        :type Confidence: int
        :param FaceResults: Type取值爲‘FACE’時，人臉識别的結果清單。基于圖片中實際檢測到的人臉數，返回數組最大值不超過5個。
        :type FaceResults: list of FaceResult
        :param Type: 取值'DNA' 或‘FACE’。DNA表示結論和置信度來自圖像指紋，FACE表示結論和置信度來自人臉識别。
        :type Type: str
        :param AdvancedInfo: 鑒政識别返回的詳細标簽後期開放。
        :type AdvancedInfo: str
        """
        self.Code = None
        self.Msg = None
        self.Suggestion = None
        self.Confidence = None
        self.FaceResults = None
        self.Type = None
        self.AdvancedInfo = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        self.Suggestion = params.get("Suggestion")
        self.Confidence = params.get("Confidence")
        if params.get("FaceResults") is not None:
            self.FaceResults = []
            for item in params.get("FaceResults"):
                obj = FaceResult()
                obj._deserialize(item)
                self.FaceResults.append(obj)
        self.Type = params.get("Type")
        self.AdvancedInfo = params.get("AdvancedInfo")


class PornResult(AbstractModel):
    """色情識别結果。

    """

    def __init__(self):
        """
        :param Code: 該識别場景的錯誤碼：
0表示成功，
-1表示系統錯誤，
-2表示引擎錯誤，
-1400表示圖片解碼失敗。
        :type Code: int
        :param Msg: 錯誤碼描述訊息。
        :type Msg: str
        :param Suggestion: 識别場景的審核結論：
PASS：正常
REVIEW：疑似
BLOCK：違規
        :type Suggestion: str
        :param Confidence: 算法對于Suggestion的置信度，0-100之間，值越高，表示對于Suggestion越确定。
        :type Confidence: int
        :param AdvancedInfo: 預留欄位，後期用于展示更多識别訊息。
        :type AdvancedInfo: str
        :param Type: 取值'LABEL‘，LABEL表示結論和置信度來自标簽分類。
        :type Type: str
        """
        self.Code = None
        self.Msg = None
        self.Suggestion = None
        self.Confidence = None
        self.AdvancedInfo = None
        self.Type = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        self.Suggestion = params.get("Suggestion")
        self.Confidence = params.get("Confidence")
        self.AdvancedInfo = params.get("AdvancedInfo")
        self.Type = params.get("Type")


class TerrorismResult(AbstractModel):
    """暴恐識别結果。

    """

    def __init__(self):
        """
        :param Code: 該識别場景的錯誤碼：
0表示成功，
-1表示系統錯誤，
-2表示引擎錯誤，
-1400表示圖片解碼失敗。
        :type Code: int
        :param Msg: 錯誤碼描述訊息。
        :type Msg: str
        :param Suggestion: 識别場景的審核結論：
PASS：正常
REVIEW：疑似
BLOCK：違規
        :type Suggestion: str
        :param Confidence: 圖像涉恐的分數，0-100之間，分數越高涉恐幾率越大。
Type爲LABEL時：
0到86，Suggestion建議爲PASS
86到91，Suggestion建議爲REVIEW
91到100，Suggestion建議爲BLOCK
Type爲FACE時：
0到55，Suggestion建議爲PASS
55到60，Suggestion建議爲REVIEW
60到100，Suggestion建議爲BLOCK
        :type Confidence: int
        :param FaceResults: Type取值爲‘FACE’時，人臉識别的結果清單。基于圖片中實際檢測到的人臉數，返回數組最大值不超過5個。
        :type FaceResults: list of FaceResult
        :param AdvancedInfo: 暴恐識别返回的詳細标簽後期開放。
        :type AdvancedInfo: str
        :param Type: 取值'LABEL' 或‘FACE’，LABEL表示結論和置信度來自标簽分類，FACE表示結論和置信度來自人臉識别。
        :type Type: str
        """
        self.Code = None
        self.Msg = None
        self.Suggestion = None
        self.Confidence = None
        self.FaceResults = None
        self.AdvancedInfo = None
        self.Type = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        self.Suggestion = params.get("Suggestion")
        self.Confidence = params.get("Confidence")
        if params.get("FaceResults") is not None:
            self.FaceResults = []
            for item in params.get("FaceResults"):
                obj = FaceResult()
                obj._deserialize(item)
                self.FaceResults.append(obj)
        self.AdvancedInfo = params.get("AdvancedInfo")
        self.Type = params.get("Type")


class VideoModerationRequest(AbstractModel):
    """VideoModeration請求參數結構體

    """

    def __init__(self):
        """
        :param VideoUrl: 需要審核的視訊的URL網址
        :type VideoUrl: str
        :param DeveloperId: 開發者标識
        :type DeveloperId: str
        :param CBUrl: 審核完成後回調網址
        :type CBUrl: str
        :param Extra: 透傳欄位，透傳簡單訊息。
        :type Extra: str
        """
        self.VideoUrl = None
        self.DeveloperId = None
        self.CBUrl = None
        self.Extra = None


    def _deserialize(self, params):
        self.VideoUrl = params.get("VideoUrl")
        self.DeveloperId = params.get("DeveloperId")
        self.CBUrl = params.get("CBUrl")
        self.Extra = params.get("Extra")


class VideoModerationResponse(AbstractModel):
    """VideoModeration返回參數結構體

    """

    def __init__(self):
        """
        :param VodTaskId: 視訊審核任務ID
        :type VodTaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.VodTaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VodTaskId = params.get("VodTaskId")
        self.RequestId = params.get("RequestId")


class VodAsrTextSegmentItem(AbstractModel):
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
pass。
review。
block。

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


class VodAudioStreamItem(AbstractModel):
    """文件音訊流訊息

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


class VodMetaData(AbstractModel):
    """媒體文件元訊息。

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
        :type VideoStreamSet: list of VodVideoStreamItem
        :param AudioStreamSet: 音訊流訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AudioStreamSet: list of VodAudioStreamItem
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
                obj = VodVideoStreamItem()
                obj._deserialize(item)
                self.VideoStreamSet.append(obj)
        if params.get("AudioStreamSet") is not None:
            self.AudioStreamSet = []
            for item in params.get("AudioStreamSet"):
                obj = VodAudioStreamItem()
                obj._deserialize(item)
                self.AudioStreamSet.append(obj)
        self.VideoDuration = params.get("VideoDuration")
        self.AudioDuration = params.get("AudioDuration")


class VodOcrTextSegmentItem(AbstractModel):
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
pass。
review。
block。

注意：此欄位可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param KeywordSet: 嫌疑關鍵詞清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type KeywordSet: list of str
        :param AreaCoordSet: 嫌疑文字出現的區域坐标 (像素級)，[x1, y1, x2, y2]，即左上角坐标、右下角坐标。
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


class VodPoliticalAsrReviewResult(AbstractModel):
    """内容審核 Asr 文字鑒政、敏感任務結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param Code: 錯誤碼，0：成功，其他值：失敗。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Code: int
        :param Msg: 錯誤訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Msg: str
        :param Confidence: 嫌疑片段審核結果建議，取值範圍：
pass。
review。
block。

Asr 文字涉政、敏感評分，分值爲0到100。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param Suggestion: Asr 文字涉政、敏感結果建議，取值範圍：
pass。
review。
block。

注意：此欄位可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param SegmentSet: Asr 文字有涉政、敏感嫌疑的視訊片段清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SegmentSet: list of VodAsrTextSegmentItem
        """
        self.Status = None
        self.Code = None
        self.Msg = None
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = VodAsrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class VodPoliticalOcrReviewResult(AbstractModel):
    """内容審核 Ocr 文字鑒政、敏感任務結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param Code: 錯誤碼，0：成功，其他值：失敗。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Code: int
        :param Msg: 錯誤訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Msg: str
        :param Confidence: Ocr 文字涉政、敏感評分，分值爲0到100。
        :type Confidence: float
        :param Suggestion: Ocr 文字涉政、敏感結果建議，取值範圍：
pass。
review。
block。
        :type Suggestion: str
        :param SegmentSet: Ocr 文字有涉政、敏感嫌疑的視訊片段清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SegmentSet: list of VodOcrTextSegmentItem
        """
        self.Status = None
        self.Code = None
        self.Msg = None
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = VodOcrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class VodPoliticalReviewResult(AbstractModel):
    """涉政訊息

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param Code: 錯誤碼，0：成功，其他值：失敗。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Code: int
        :param Msg: 錯誤訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Msg: str
        :param Confidence: 視訊涉政評分，分值爲0到100。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param Suggestion: 涉政結果建議，取值範圍：
pass。
review。
block。

注意：此欄位可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Label: 視訊鑒政結果标簽，取值範圍：
politician：政治人物。
violation_photo：違規圖标。

注意：此欄位可能返回 null，表示取不到有效值。
        :type Label: str
        :param SegmentSet: 有涉政嫌疑的視訊片段清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SegmentSet: list of VodPoliticalReviewSegmentItem
        """
        self.Status = None
        self.Code = None
        self.Msg = None
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = VodPoliticalReviewSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class VodPoliticalReviewSegmentItem(AbstractModel):
    """内容審核鑒政任務結果類型

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
pass。
review。
block。

注意：此欄位可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Name: 涉政人物、違規圖标名字。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Name: str
        :param Label: 嫌疑片段鑒政結果标簽。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Label: str
        :param Url: 嫌疑圖片 URL （圖片不會永久儲存，到達
PicUrlExpireTime 時間點後圖片将被删除）。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Url: str
        :param PicUrlExpireTimeStamp: 嫌疑圖片 URL 失效時間，使用 ISO 日期格式。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PicUrlExpireTimeStamp: int
        :param AreaCoordSet: 涉政人物、違規圖标出現的區域坐标 (像素級)，[x1, y1, x2, y2]，即左上角坐标、右下角坐标。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AreaCoordSet: list of int
        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Suggestion = None
        self.Name = None
        self.Label = None
        self.Url = None
        self.PicUrlExpireTimeStamp = None
        self.AreaCoordSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Name = params.get("Name")
        self.Label = params.get("Label")
        self.Url = params.get("Url")
        self.PicUrlExpireTimeStamp = params.get("PicUrlExpireTimeStamp")
        self.AreaCoordSet = params.get("AreaCoordSet")


class VodPornAsrReviewResult(AbstractModel):
    """Asr 文字涉黃訊息

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param Code: 錯誤碼，0：成功，其他值：失敗。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Code: int
        :param Msg: 錯誤訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Msg: str
        :param Confidence: Asr 文字涉黃評分，分值爲0到100。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param Suggestion: Asr 文字涉黃結果建議，取值範圍：
pass。
review。
block。

注意：此欄位可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param SegmentSet: Asr 文字有涉黃嫌疑的視訊片段清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SegmentSet: list of VodAsrTextSegmentItem
        """
        self.Status = None
        self.Code = None
        self.Msg = None
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = VodAsrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class VodPornOcrResult(AbstractModel):
    """内容審核 Ocr 文字鑒黃任務結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param Code: 錯誤碼，0：成功，其他值：失敗。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Code: int
        :param Msg: 錯誤訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Msg: str
        :param Confidence: Ocr 文字涉黃評分，分值爲0到100。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param Suggestion: Ocr 文字涉黃結果建議，取值範圍：
pass。
review。
block。

注意：此欄位可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param SegmentSet: Ocr 文字有涉黃嫌疑的視訊片段清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SegmentSet: list of VodOcrTextSegmentItem
        """
        self.Status = None
        self.Code = None
        self.Msg = None
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = VodOcrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class VodPornReviewResult(AbstractModel):
    """内容審核鑒黃任務結果類型

    """

    def __init__(self):
        """
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param Code: 錯誤碼，0：成功，其他值：失敗。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Code: int
        :param Msg: 錯誤訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Msg: str
        :param Confidence: 視訊鑒黃評分，分值爲0到100。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param Suggestion: 鑒黃結果建議，取值範圍：
pass。
review。
block。

注意：此欄位可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Label: 視訊鑒黃結果标簽，取值範圍：
porn：色情。
sexy：性感。
vulgar：低俗。
intimacy：親密行爲。

注意：此欄位可能返回 null，表示取不到有效值。
        :type Label: str
        :param SegmentSet: 有涉黃嫌疑的視訊片段清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SegmentSet: list of VodPornReviewSegmentItem
        """
        self.Status = None
        self.Code = None
        self.Msg = None
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = VodPornReviewSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class VodPornReviewSegmentItem(AbstractModel):
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
        :param Label: 嫌疑片段鑒黃結果标簽。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Label: str
        :param Suggestion: 嫌疑片段鑒黃結果建議，取值範圍：
pass。
review。
block。

注意：此欄位可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Url: 嫌疑圖片 URL （圖片不會永久儲存，到達
PicUrlExpireTime 時間點後圖片将被删除）。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Url: str
        :param PicUrlExpireTimeStamp: 嫌疑圖片 URL 失效時間，使用 ISO 日期格式。
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


class VodTerrorismReviewResult(AbstractModel):
    """暴恐訊息

    """

    def __init__(self):
        """
        :param Confidence: 視訊暴恐評分，分值爲0到100。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Confidence: float
        :param Suggestion: 暴恐結果建議，取值範圍：
pass。
review。
block。

注意：此欄位可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Label: 視訊暴恐結果标簽，取值範圍：
guns：武器槍支。
crowd：人群聚集。
police：警察部隊。
bloody：血腥畫面。
banners：暴恐旗幟。
militant：武裝分子。
explosion：爆炸火災。
terrorists：暴恐人物。

注意：此欄位可能返回 null，表示取不到有效值。
        :type Label: str
        :param Status: 任務狀态，有 PROCESSING，SUCCESS 和 FAIL 三種。
        :type Status: str
        :param Code: 錯誤碼，0：成功，其他值：失敗。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Code: int
        :param Msg: 錯誤訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Msg: str
        :param SegmentSet: 有暴恐嫌疑的視訊片段清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SegmentSet: list of VodPornReviewSegmentItem
        """
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.Status = None
        self.Code = None
        self.Msg = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.Status = params.get("Status")
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = VodPornReviewSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class VodVideoStreamItem(AbstractModel):
    """文件視訊流訊息

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