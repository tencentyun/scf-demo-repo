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


class BeautifyPicRequest(AbstractModel):
    """BeautifyPic請求參數結構體

    """

    def __init__(self):
        """
        :param Image: 圖片 base64 數據，base64 編碼後大小不可超過5M。 
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Image: str
        :param Url: 圖片的 Url 。對應圖片 base64 編碼後大小不可超過5M。 
Url、Image必須提供一個，如果都提供，只使用 Url。  
圖片儲存于Top Cloud 的Url可保障更高下載速度和穩定性，建議圖片儲存于Top Cloud 。  
非Top Cloud 儲存的Url速度和穩定性可能受一定影響。 
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Url: str
        :param Whitening: 美白程度，取值範圍[0,100]。0不美白，100代表最高程度。預設值30。
        :type Whitening: int
        :param Smoothing: 磨皮程度，取值範圍[0,100]。0不磨皮，100代表最高程度。預設值10。
        :type Smoothing: int
        :param FaceLifting: 瘦臉程度，取值範圍[0,100]。0不瘦臉，100代表最高程度。預設值70。
        :type FaceLifting: int
        :param EyeEnlarging: 大眼程度，取值範圍[0,100]。0不大眼，100代表最高程度。預設值70。
        :type EyeEnlarging: int
        """
        self.Image = None
        self.Url = None
        self.Whitening = None
        self.Smoothing = None
        self.FaceLifting = None
        self.EyeEnlarging = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.Whitening = params.get("Whitening")
        self.Smoothing = params.get("Smoothing")
        self.FaceLifting = params.get("FaceLifting")
        self.EyeEnlarging = params.get("EyeEnlarging")


class BeautifyPicResponse(AbstractModel):
    """BeautifyPic返回參數結構體

    """

    def __init__(self):
        """
        :param ResultImage: 處理後的圖片 base64 數據。
        :type ResultImage: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ResultImage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultImage = params.get("ResultImage")
        self.RequestId = params.get("RequestId")


class CreateModelRequest(AbstractModel):
    """CreateModel請求參數結構體

    """

    def __init__(self):
        """
        :param LUTFile: 用于試唇色，要求必須是LUT 格式的cube文件轉換成512*512的PNG圖片。檢視 [LUT文件的使用說明](https://cloud.tencent.com/document/product/1172/41701)。了解 [cube文件轉png圖片小工具](http://yyb.gtimg.com/aiplat/static/qcloud-cube-to-png.html)。
        :type LUTFile: str
        :param Description: 文件描述訊息，可用于備注。
        :type Description: str
        """
        self.LUTFile = None
        self.Description = None


    def _deserialize(self, params):
        self.LUTFile = params.get("LUTFile")
        self.Description = params.get("Description")


class CreateModelResponse(AbstractModel):
    """CreateModel返回參數結構體

    """

    def __init__(self):
        """
        :param ModelId: 唇色素材ID。
        :type ModelId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ModelId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ModelId = params.get("ModelId")
        self.RequestId = params.get("RequestId")


class DeleteModelRequest(AbstractModel):
    """DeleteModel請求參數結構體

    """

    def __init__(self):
        """
        :param ModelId: 素材ID。
        :type ModelId: str
        """
        self.ModelId = None


    def _deserialize(self, params):
        self.ModelId = params.get("ModelId")


class DeleteModelResponse(AbstractModel):
    """DeleteModel返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class FaceRect(AbstractModel):
    """人臉框訊息

    """

    def __init__(self):
        """
        :param X: 人臉框左上角橫坐标。
        :type X: int
        :param Y: 人臉框左上角縱坐标。
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


class GetModelListRequest(AbstractModel):
    """GetModelList請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 起始序号，預設值爲0。
        :type Offset: int
        :param Limit: 返回數量，預設值爲10，最大值爲100。
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetModelListResponse(AbstractModel):
    """GetModelList返回參數結構體

    """

    def __init__(self):
        """
        :param ModelIdNum: 唇色素材總數量。
        :type ModelIdNum: int
        :param ModelInfos: 素材數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type ModelInfos: list of ModelInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ModelIdNum = None
        self.ModelInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ModelIdNum = params.get("ModelIdNum")
        if params.get("ModelInfos") is not None:
            self.ModelInfos = []
            for item in params.get("ModelInfos"):
                obj = ModelInfo()
                obj._deserialize(item)
                self.ModelInfos.append(obj)
        self.RequestId = params.get("RequestId")


class LipColorInfo(AbstractModel):
    """唇色訊息

    """

    def __init__(self):
        """
        :param RGBA: 使用RGBA模型試唇色。
        :type RGBA: :class:`tencentcloud.fmu.v20191213.models.RGBAInfo`
        :param ModelId: 使用已注冊的 LUT 文件試唇色。  
ModelId 和 RGBA 兩個參數只需提供一個，若都提供只使用 ModelId。
        :type ModelId: str
        :param FaceRect: 人臉框位置。若不輸入則選擇 Image 或 Url 中面積最大的人臉。  
您可以通過 [人臉檢測與分析](https://cloud.tencent.com/document/api/867/32800)  介面獲取人臉框位置訊息。
        :type FaceRect: :class:`tencentcloud.fmu.v20191213.models.FaceRect`
        """
        self.RGBA = None
        self.ModelId = None
        self.FaceRect = None


    def _deserialize(self, params):
        if params.get("RGBA") is not None:
            self.RGBA = RGBAInfo()
            self.RGBA._deserialize(params.get("RGBA"))
        self.ModelId = params.get("ModelId")
        if params.get("FaceRect") is not None:
            self.FaceRect = FaceRect()
            self.FaceRect._deserialize(params.get("FaceRect"))


class ModelInfo(AbstractModel):
    """LUT素材訊息

    """

    def __init__(self):
        """
        :param ModelId: 唇色素材ID
        :type ModelId: str
        :param LUTFileUrl: 唇色素材 url 。 LUT 文件 url 5分鍾有效。
        :type LUTFileUrl: str
        :param Description: 文件描述訊息。
        :type Description: str
        """
        self.ModelId = None
        self.LUTFileUrl = None
        self.Description = None


    def _deserialize(self, params):
        self.ModelId = params.get("ModelId")
        self.LUTFileUrl = params.get("LUTFileUrl")
        self.Description = params.get("Description")


class RGBAInfo(AbstractModel):
    """RGBA通道訊息

    """

    def __init__(self):
        """
        :param R: R通道數值。[0,255]。
        :type R: int
        :param G: G通道數值。[0,255]。
        :type G: int
        :param B: B通道數值。[0,255]。
        :type B: int
        :param A: A通道數值。[0,100]。建議取值50。
        :type A: int
        """
        self.R = None
        self.G = None
        self.B = None
        self.A = None


    def _deserialize(self, params):
        self.R = params.get("R")
        self.G = params.get("G")
        self.B = params.get("B")
        self.A = params.get("A")


class TryLipstickPicRequest(AbstractModel):
    """TryLipstickPic請求參數結構體

    """

    def __init__(self):
        """
        :param LipColorInfos: 唇色訊息。 
您可以輸入最多3個 LipColorInfo 來實現給一張圖中的最多3張人臉試唇色。
        :type LipColorInfos: list of LipColorInfo
        :param Image: 圖片 base64 數據，base64 編碼後大小不可超過6M。 
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Image: str
        :param Url: 圖片的 Url ，對應圖片 base64 編碼後大小不可超過6M。 
圖片的 Url、Image必須提供一個，如果都提供，只使用 Url。 
圖片儲存于Top Cloud 的 Url 可保障更高下載速度和穩定性，建議圖片儲存于Top Cloud 。 
非Top Cloud 儲存的Url速度和穩定性可能受一定影響。 
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Url: str
        """
        self.LipColorInfos = None
        self.Image = None
        self.Url = None


    def _deserialize(self, params):
        if params.get("LipColorInfos") is not None:
            self.LipColorInfos = []
            for item in params.get("LipColorInfos"):
                obj = LipColorInfo()
                obj._deserialize(item)
                self.LipColorInfos.append(obj)
        self.Image = params.get("Image")
        self.Url = params.get("Url")


class TryLipstickPicResponse(AbstractModel):
    """TryLipstickPic返回參數結構體

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