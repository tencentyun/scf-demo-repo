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
        :type FaceRect: :class:`taifucloudcloud.ticm.v20181127.models.FaceRect`
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
        :type PornResult: :class:`taifucloudcloud.ticm.v20181127.models.PornResult`
        :param TerrorismResult: 暴恐識别結果。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TerrorismResult: :class:`taifucloudcloud.ticm.v20181127.models.TerrorismResult`
        :param PoliticsResult: 政治敏感識别結果。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PoliticsResult: :class:`taifucloudcloud.ticm.v20181127.models.PoliticsResult`
        :param Extra: 透傳欄位，透傳簡單訊息。
        :type Extra: str
        :param DisgustResult: 惡心内容識别結果。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DisgustResult: :class:`taifucloudcloud.ticm.v20181127.models.DisgustResult`
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