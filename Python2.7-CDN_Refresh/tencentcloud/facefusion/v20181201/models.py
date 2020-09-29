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


class FaceFusionRequest(AbstractModel):
    """FaceFusion請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: 活動 ID，請在人臉融合控制台檢視。
        :type ProjectId: str
        :param ModelId: 素材 ID，請在人臉融合控制台檢視。
        :type ModelId: str
        :param Image: 圖片 base64 數據。請确保人臉爲正臉，無旋轉。若某些手機拍攝後人臉被旋轉，請使用圖片的 EXIF 訊息對圖片進行旋轉處理；請勿在 base64 數據中包含頭部，如“data:image/jpeg;base64,”。
        :type Image: str
        :param RspImgType: 返回圖像方式（url 或 base64) ，二選一。url有效期爲30天。
        :type RspImgType: str
        :param PornDetect: 曆史遺留欄位，無需填寫。因爲融合只需提取人臉特征，不需要 。
        :type PornDetect: int
        :param CelebrityIdentify: 0表示不需要鑒政，1表示需要鑒政。預設值爲0。
請注意，鑒政服務開啓後，您需要根據返回結果自行判斷是否調整您的業務邏輯。例如提示您的用戶圖片非法，請更換圖片。
        :type CelebrityIdentify: int
        """
        self.ProjectId = None
        self.ModelId = None
        self.Image = None
        self.RspImgType = None
        self.PornDetect = None
        self.CelebrityIdentify = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ModelId = params.get("ModelId")
        self.Image = params.get("Image")
        self.RspImgType = params.get("RspImgType")
        self.PornDetect = params.get("PornDetect")
        self.CelebrityIdentify = params.get("CelebrityIdentify")


class FaceFusionResponse(AbstractModel):
    """FaceFusion返回參數結構體

    """

    def __init__(self):
        """
        :param Image: RspImgType 爲 url 時，返回結果的 url， RspImgType 爲 base64 時返回 base64 數據。
        :type Image: str
        :param ReviewResultSet: 鑒政結果
        :type ReviewResultSet: list of FuseFaceReviewResult
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Image = None
        self.ReviewResultSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        if params.get("ReviewResultSet") is not None:
            self.ReviewResultSet = []
            for item in params.get("ReviewResultSet"):
                obj = FuseFaceReviewResult()
                obj._deserialize(item)
                self.ReviewResultSet.append(obj)
        self.RequestId = params.get("RequestId")


class FaceRect(AbstractModel):
    """人臉框訊息

    """

    def __init__(self):
        """
        :param X: 人臉框左上角橫坐標。
        :type X: int
        :param Y: 人臉框左上角縱坐標。
        :type Y: int
        :param Width: 人臉框寬度。
        :type Width: int
        :param Height: 人臉框高度。
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


class FuseFaceRequest(AbstractModel):
    """FuseFace請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: 活動 ID，請在人臉融合控制台檢視。
        :type ProjectId: str
        :param ModelId: 素材 ID，請在人臉融合控制台檢視。
        :type ModelId: str
        :param RspImgType: 返回圖像方式（url 或 base64) ，二選一。url有效期爲30天。
        :type RspImgType: str
        :param MergeInfos: 用戶人臉圖片、素材範本圖的人臉位置訊息。
        :type MergeInfos: list of MergeInfo
        :param FuseProfileDegree: 臉型融合比例，數值越高，融合後的臉型越像素材人物。取值範圍[0,100] 
若此參數不填寫，則使用人臉融合控制台中臉型參數數值。（換臉版算法暫不支援此參數調整）
        :type FuseProfileDegree: int
        :param FuseFaceDegree: 五官融合比例，數值越高，融合後的五官越像素材人物。取值範圍[0,100] 
若此參數不填寫，則使用人臉融合控制台中五官參數數值。（換臉版算法暫不支援此參數調整）
        :type FuseFaceDegree: int
        :param CelebrityIdentify: 0表示不需要鑒政，1表示需要鑒政。預設值爲0。
請注意，鑒政服務開啓後，您需要根據返回結果自行判斷是否調整您的業務邏輯。例如提示您的用戶圖片非法，請更換圖片。
        :type CelebrityIdentify: int
        """
        self.ProjectId = None
        self.ModelId = None
        self.RspImgType = None
        self.MergeInfos = None
        self.FuseProfileDegree = None
        self.FuseFaceDegree = None
        self.CelebrityIdentify = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ModelId = params.get("ModelId")
        self.RspImgType = params.get("RspImgType")
        if params.get("MergeInfos") is not None:
            self.MergeInfos = []
            for item in params.get("MergeInfos"):
                obj = MergeInfo()
                obj._deserialize(item)
                self.MergeInfos.append(obj)
        self.FuseProfileDegree = params.get("FuseProfileDegree")
        self.FuseFaceDegree = params.get("FuseFaceDegree")
        self.CelebrityIdentify = params.get("CelebrityIdentify")


class FuseFaceResponse(AbstractModel):
    """FuseFace返回參數結構體

    """

    def __init__(self):
        """
        :param FusedImage: RspImgType 爲 url 時，返回結果的 url， RspImgType 爲 base64 時返回 base64 數據。
        :type FusedImage: str
        :param ReviewResultSet: 鑒政結果。該數組的順序和請求中mergeinfo的順序一緻，一一對應
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReviewResultSet: list of FuseFaceReviewResult
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FusedImage = None
        self.ReviewResultSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FusedImage = params.get("FusedImage")
        if params.get("ReviewResultSet") is not None:
            self.ReviewResultSet = []
            for item in params.get("ReviewResultSet"):
                obj = FuseFaceReviewResult()
                obj._deserialize(item)
                self.ReviewResultSet.append(obj)
        self.RequestId = params.get("RequestId")


class FuseFaceReviewDetail(AbstractModel):
    """人臉融合 鑒政人臉訊息

    """

    def __init__(self):
        """
        :param Field: 保留欄位
        :type Field: str
        :param Label: 人員名稱
        :type Label: str
        :param Confidence: 對應識别label的置信度，分數越高意味涉政可能性越大。 
0到70，Suggestion建議爲PASS； 
70到80，Suggestion建議爲REVIEW； 
80到100，Suggestion建議爲BLOCK。
        :type Confidence: float
        :param Suggestion: 識别場景的審核結論：  
PASS：正常 
REVIEW：疑似  
BLOCK：違規
        :type Suggestion: str
        """
        self.Field = None
        self.Label = None
        self.Confidence = None
        self.Suggestion = None


    def _deserialize(self, params):
        self.Field = params.get("Field")
        self.Label = params.get("Label")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")


class FuseFaceReviewResult(AbstractModel):
    """人臉融合 鑒政返回參數item

    """

    def __init__(self):
        """
        :param Category: 保留欄位
        :type Category: str
        :param Code: 狀态碼， 0爲處理成功，其他值爲處理失敗
        :type Code: str
        :param CodeDescription: 對應狀态碼訊息描述
        :type CodeDescription: str
        :param Confidence: 保留欄位
        :type Confidence: float
        :param Suggestion: 保留欄位
        :type Suggestion: str
        :param DetailSet: 審核詳細内容
        :type DetailSet: list of FuseFaceReviewDetail
        """
        self.Category = None
        self.Code = None
        self.CodeDescription = None
        self.Confidence = None
        self.Suggestion = None
        self.DetailSet = None


    def _deserialize(self, params):
        self.Category = params.get("Category")
        self.Code = params.get("Code")
        self.CodeDescription = params.get("CodeDescription")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("DetailSet") is not None:
            self.DetailSet = []
            for item in params.get("DetailSet"):
                obj = FuseFaceReviewDetail()
                obj._deserialize(item)
                self.DetailSet.append(obj)


class MergeInfo(AbstractModel):
    """人臉圖片和待被融合的素材範本圖的人臉位置訊息。

    """

    def __init__(self):
        """
        :param Image: 輸入圖片base64
        :type Image: str
        :param Url: 輸入圖片url
        :type Url: str
        :param InputImageFaceRect: 上傳的圖片人臉位置訊息（人臉框）
        :type InputImageFaceRect: :class:`taifucloudcloud.facefusion.v20181201.models.FaceRect`
        :param TemplateFaceID: 控制台上傳的素材人臉ID
        :type TemplateFaceID: str
        """
        self.Image = None
        self.Url = None
        self.InputImageFaceRect = None
        self.TemplateFaceID = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        if params.get("InputImageFaceRect") is not None:
            self.InputImageFaceRect = FaceRect()
            self.InputImageFaceRect._deserialize(params.get("InputImageFaceRect"))
        self.TemplateFaceID = params.get("TemplateFaceID")