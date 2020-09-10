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
        :param RspImgType: 返回圖像方式（url 或 base64) ，二選一。當前僅支援 url 方式，base64 方式後期開放。
        :type RspImgType: str
        :param PornDetect: 0表示不需要鑒黃，1表示需要鑒黃。2018年12月1号以前創建的活動預設值爲0，其他情況預設值爲1.
        :type PornDetect: int
        :param CelebrityIdentify: 0表示不需要鑒政，1表示需要鑒政。2018年12月1号以前創建的活動預設值爲0，其他情況預設值爲1。鑒政介面同時會對名人明星進行識别，您可以根據實際需要過濾。
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
        :param Image: RspImgType 爲 url 時，返回結果的 url， RspImgType 爲 base64 時返回 base64 數據。當前僅支援 url 方式，base64 方式後期開放。
        :type Image: str
        :param ReviewResultSet: 鑒黃鑒政結果
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


class FuseFaceReviewDetail(AbstractModel):
    """人臉融合鑒黃鑒政人臉訊息

    """

    def __init__(self):
        """
        :param Field: 鑒政使用欄位, 爲職業屬性,其他審核結果對應上一級category
        :type Field: str
        :param Label: 人員名稱
        :type Label: str
        :param Confidence: 對應識别label的置信度
        :type Confidence: float
        :param Suggestion: 此欄位爲保留欄位，目前統一返回pass。
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
    """人臉融合鑒黃鑒政返回參數item

    """

    def __init__(self):
        """
        :param Category: 對應的類别名稱 porn, politics, terror
        :type Category: str
        :param Code: 對應子類别狀态碼
        :type Code: str
        :param CodeDescription: 對應子類别狀态碼訊息描述
        :type CodeDescription: str
        :param Confidence: 對應識别種類的置信度
        :type Confidence: float
        :param Suggestion: 此欄位爲保留欄位，目前統一返回pass。
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