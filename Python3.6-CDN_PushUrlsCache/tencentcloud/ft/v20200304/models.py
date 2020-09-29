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


class AgeInfo(AbstractModel):
    """人臉變年齡訊息

    """

    def __init__(self):
        """
        :param Age: 當前只支援設置爲10且不可調整（後續放開後再知會）。
        :type Age: int
        :param FaceRect: 人臉框位置。若不輸入則選擇 Image 或 Url 中面積最大的人臉。  
您可以通過 [人臉檢測與分析](https://cloud.taifucloud.com/document/api/867/32800)  介面獲取人臉框位置訊息。
        :type FaceRect: :class:`taifucloudcloud.ft.v20200304.models.FaceRect`
        """
        self.Age = None
        self.FaceRect = None


    def _deserialize(self, params):
        self.Age = params.get("Age")
        if params.get("FaceRect") is not None:
            self.FaceRect = FaceRect()
            self.FaceRect._deserialize(params.get("FaceRect"))


class ChangeAgePicRequest(AbstractModel):
    """ChangeAgePic請求參數結構體

    """

    def __init__(self):
        """
        :param AgeInfos: 人臉變老變年輕訊息。 
您可以輸入最多3個 AgeInfo 來實現給一張圖中的最多3張人臉變老變年輕。
        :type AgeInfos: list of AgeInfo
        :param Image: 圖片 base64 數據，base64 編碼後大小不可超過5M。 
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Image: str
        :param Url: 圖片的 Url ，對應圖片 base64 編碼後大小不可超過5M。 
圖片的 Url、Image必須提供一個，如果都提供，只使用 Url。 
圖片儲存於Top Cloud 的 Url 可保障更高下載速度和穩定性，建議圖片儲存於Top Cloud 。 
非Top Cloud 儲存的Url速度和穩定性可能受一定影響。 
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Url: str
        """
        self.AgeInfos = None
        self.Image = None
        self.Url = None


    def _deserialize(self, params):
        if params.get("AgeInfos") is not None:
            self.AgeInfos = []
            for item in params.get("AgeInfos"):
                obj = AgeInfo()
                obj._deserialize(item)
                self.AgeInfos.append(obj)
        self.Image = params.get("Image")
        self.Url = params.get("Url")


class ChangeAgePicResponse(AbstractModel):
    """ChangeAgePic返回參數結構體

    """

    def __init__(self):
        """
        :param ResultImage: base64編碼圖片
        :type ResultImage: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ResultImage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultImage = params.get("ResultImage")
        self.RequestId = params.get("RequestId")


class FaceRect(AbstractModel):
    """人臉框位置

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


class GenderInfo(AbstractModel):
    """人臉轉換性别訊息

    """

    def __init__(self):
        """
        :param Gender: 選擇轉換方向，0：男變女，1：女變男。
        :type Gender: int
        :param FaceRect: 人臉框位置。若不輸入則選擇 Image 或 Url 中面積最大的人臉。  
您可以通過 [人臉檢測與分析](https://cloud.taifucloud.com/document/api/867/32800)  介面獲取人臉框位置訊息。
        :type FaceRect: :class:`taifucloudcloud.ft.v20200304.models.FaceRect`
        """
        self.Gender = None
        self.FaceRect = None


    def _deserialize(self, params):
        self.Gender = params.get("Gender")
        if params.get("FaceRect") is not None:
            self.FaceRect = FaceRect()
            self.FaceRect._deserialize(params.get("FaceRect"))


class SwapGenderPicRequest(AbstractModel):
    """SwapGenderPic請求參數結構體

    """

    def __init__(self):
        """
        :param GenderInfos: 人臉轉化性别訊息。 
您可以輸入最多3個 GenderInfo 來實現給一張圖中的最多3張人臉轉換性别。
        :type GenderInfos: list of GenderInfo
        :param Image: 圖片 base64 數據，base64 編碼後大小不可超過5M。 
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Image: str
        :param Url: 圖片的 Url ，對應圖片 base64 編碼後大小不可超過5M。 
圖片的 Url、Image必須提供一個，如果都提供，只使用 Url。 
圖片儲存於Top Cloud 的 Url 可保障更高下載速度和穩定性，建議圖片儲存於Top Cloud 。 
非Top Cloud 儲存的Url速度和穩定性可能受一定影響。 
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Url: str
        """
        self.GenderInfos = None
        self.Image = None
        self.Url = None


    def _deserialize(self, params):
        if params.get("GenderInfos") is not None:
            self.GenderInfos = []
            for item in params.get("GenderInfos"):
                obj = GenderInfo()
                obj._deserialize(item)
                self.GenderInfos.append(obj)
        self.Image = params.get("Image")
        self.Url = params.get("Url")


class SwapGenderPicResponse(AbstractModel):
    """SwapGenderPic返回參數結構體

    """

    def __init__(self):
        """
        :param ResultImage: 結果圖片Base64訊息。
        :type ResultImage: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ResultImage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultImage = params.get("ResultImage")
        self.RequestId = params.get("RequestId")