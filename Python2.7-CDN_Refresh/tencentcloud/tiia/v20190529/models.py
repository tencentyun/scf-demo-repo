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


class AssessQualityRequest(AbstractModel):
    """AssessQuality請求參數結構體

    """

    def __init__(self):
        """
        :param ImageUrl: 圖片URL網址。 
圖片限制： 
• 圖片格式：PNG、JPG、JPEG。 
• 圖片大小：所下載圖片經Base64編碼後不超過4M。圖片下載時間不超過3秒。 
建議：
• 圖片像素：大于50*50像素，否則影響識别效果； 
• 長寬比：長邊：短邊<5； 
介面響應時間會受到圖片下載時間的影響，建議使用更可靠的儲存服務，推薦将圖片儲存在Top Cloud COS。
        :type ImageUrl: str
        :param ImageBase64: 圖片經過base64編碼的内容。最大不超過4M。與ImageUrl同時存在時優先使用ImageUrl欄位。
**注意：圖片需要base64編碼，并且要去掉編碼頭部。**
        :type ImageBase64: str
        """
        self.ImageUrl = None
        self.ImageBase64 = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")


class AssessQualityResponse(AbstractModel):
    """AssessQuality返回參數結構體

    """

    def __init__(self):
        """
        :param LongImage: 取值爲TRUE或FALSE，TRUE爲長圖，FALSE爲正常圖，長圖定義爲長寬比大于等于3或小於等于1/3的圖片。
        :type LongImage: bool
        :param BlackAndWhite: 取值爲TRUE或FALSE，TRUE爲黑白圖，FALSE爲否。黑白圖即灰度圖，指紅綠藍三個通道都是以灰度色階顯示的圖片，并非視覺上的“黑白圖片”。
        :type BlackAndWhite: bool
        :param SmallImage: 取值爲TRUE或FALSE，TRUE爲小圖，FALSE爲否, 小圖定義爲最長邊小於179像素的圖片。當一張圖片被判斷爲小圖時，不建議做推薦和展示，其他欄位統一輸出爲0或FALSE。
        :type SmallImage: bool
        :param BigImage: 取值爲TRUE或FALSE，TRUE爲大圖，FALSE爲否，定義爲最短邊大于1000像素的圖片
        :type BigImage: bool
        :param PureImage: 取值爲TRUE或FALSE，TRUE爲純色圖或純文字圖，即沒有内容或只有簡單内容的圖片，FALSE爲正常圖片。
        :type PureImage: bool
        :param ClarityScore: 綜合評分。圖像清晰度的得分，對圖片的噪聲、曝光、模糊、壓縮等因素進行綜合評估，取值爲[0, 100]，值越大，越清晰。一般大于50爲較清晰圖片，标準可以自行把握。
        :type ClarityScore: int
        :param AestheticScore: 綜合評分。圖像美觀度得分， 從構圖、色彩等多個藝術性維度評價圖片，取值爲[0, 100]，值越大，越美觀。一般大于50爲較美觀圖片，标準可以自行把握。
        :type AestheticScore: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.LongImage = None
        self.BlackAndWhite = None
        self.SmallImage = None
        self.BigImage = None
        self.PureImage = None
        self.ClarityScore = None
        self.AestheticScore = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LongImage = params.get("LongImage")
        self.BlackAndWhite = params.get("BlackAndWhite")
        self.SmallImage = params.get("SmallImage")
        self.BigImage = params.get("BigImage")
        self.PureImage = params.get("PureImage")
        self.ClarityScore = params.get("ClarityScore")
        self.AestheticScore = params.get("AestheticScore")
        self.RequestId = params.get("RequestId")


class CarTagItem(AbstractModel):
    """車輛屬性識别的結果

    """

    def __init__(self):
        """
        :param Serial: 車系
        :type Serial: str
        :param Brand: 車輛品牌
        :type Brand: str
        :param Type: 車輛類型
        :type Type: str
        :param Color: 車輛顔色
        :type Color: str
        :param Confidence: 置信度，0-100
        :type Confidence: int
        :param Year: 年份，沒識别出年份的時候返回0
        :type Year: int
        :param CarLocation: 車輛在圖片中的坐标訊息
        :type CarLocation: list of Coord
        """
        self.Serial = None
        self.Brand = None
        self.Type = None
        self.Color = None
        self.Confidence = None
        self.Year = None
        self.CarLocation = None


    def _deserialize(self, params):
        self.Serial = params.get("Serial")
        self.Brand = params.get("Brand")
        self.Type = params.get("Type")
        self.Color = params.get("Color")
        self.Confidence = params.get("Confidence")
        self.Year = params.get("Year")
        if params.get("CarLocation") is not None:
            self.CarLocation = []
            for item in params.get("CarLocation"):
                obj = Coord()
                obj._deserialize(item)
                self.CarLocation.append(obj)


class Coord(AbstractModel):
    """汽車坐标訊息

    """

    def __init__(self):
        """
        :param X: 橫坐标x
        :type X: int
        :param Y: 縱坐标y
        :type Y: int
        """
        self.X = None
        self.Y = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")


class CropImageRequest(AbstractModel):
    """CropImage請求參數結構體

    """

    def __init__(self):
        """
        :param Width: 需要裁剪區域的寬度，與Height共同組成所需裁剪的圖片寬高比例；
輸入數字請大于0、小於圖片寬度的像素值；
        :type Width: int
        :param Height: 需要裁剪區域的高度，與Width共同組成所需裁剪的圖片寬高比例；
輸入數字請請大于0、小於圖片高度的像素值；
寬高比例（Width : Height）會簡化爲最簡分數，即如果Width輸入10、Height輸入20，會簡化爲1：2。
Width : Height建議取值在[1, 2.5]之間，超過這個範圍可能會影響效果；
        :type Height: int
        :param ImageUrl: 圖片URL網址。 
圖片限制： 
• 圖片格式：PNG、JPG、JPEG。 
• 圖片大小：所下載圖片經Base64編碼後不超過4M。圖片下載時間不超過3秒。 
建議：
• 圖片像素：大于50*50像素，否則影響識别效果； 
• 長寬比：長邊：短邊<5； 
介面響應時間會受到圖片下載時間的影響，建議使用更可靠的儲存服務，推薦将圖片儲存在Top Cloud COS。
        :type ImageUrl: str
        :param ImageBase64: 圖片經過base64編碼的内容。最大不超過4M。與ImageUrl同時存在時優先使用ImageUrl欄位。
**注意：圖片需要base64編碼，并且要去掉編碼頭部。**
        :type ImageBase64: str
        """
        self.Width = None
        self.Height = None
        self.ImageUrl = None
        self.ImageBase64 = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")


class CropImageResponse(AbstractModel):
    """CropImage返回參數結構體

    """

    def __init__(self):
        """
        :param X: 裁剪區域左上角X坐标值
        :type X: int
        :param Y: 裁剪區域左上角Y坐标值
        :type Y: int
        :param Width: 裁剪區域的寬度，單位爲像素
        :type Width: int
        :param Height: 裁剪區域的高度，單位爲像素
        :type Height: int
        :param OriginalWidth: 原圖寬度，單位爲像素
        :type OriginalWidth: int
        :param OriginalHeight: 原圖高度，單位爲像素
        :type OriginalHeight: int
        :param CropResult: 0：摳圖正常；
1：原圖過長，指原圖的高度是寬度的1.8倍以上；
2：原圖過寬，指原圖的寬度是高度的1.8倍以上；
3：摳圖區域過長，指摳圖的高度是主體備選框高度的1.6倍以上；
4：摳圖區域過寬，指當沒有檢測到人臉時，摳圖區域寬度是檢測出的原圖主體區域寬度的1.6倍以上；
5：純色圖，指裁剪區域視覺較爲單一、缺乏主體部分 ；
6：寬高比異常，指Width : Height取值超出[1, 2.5]的範圍；

以上是輔助決策的參考建議，可以根據業務需求選擇采納或忽視。
        :type CropResult: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None
        self.OriginalWidth = None
        self.OriginalHeight = None
        self.CropResult = None
        self.RequestId = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.OriginalWidth = params.get("OriginalWidth")
        self.OriginalHeight = params.get("OriginalHeight")
        self.CropResult = params.get("CropResult")
        self.RequestId = params.get("RequestId")


class DetectCelebrityRequest(AbstractModel):
    """DetectCelebrity請求參數結構體

    """

    def __init__(self):
        """
        :param ImageUrl: 圖片URL網址。 
圖片限制： 
• 圖片格式：PNG、JPG、JPEG。 
• 圖片大小：所下載圖片經Base64編碼後不超過4M。圖片下載時間不超過3秒。 
建議：
• 圖片像素：大于50*50像素，否則影響識别效果； 
• 長寬比：長邊：短邊<5； 
介面響應時間會受到圖片下載時間的影響，建議使用更可靠的儲存服務，推薦将圖片儲存在Top Cloud COS。
        :type ImageUrl: str
        :param ImageBase64: 圖片經過base64編碼的内容。最大不超過4M。與ImageUrl同時存在時優先使用ImageUrl欄位。
**注意：圖片需要base64編碼，并且要去掉編碼頭部。**
        :type ImageBase64: str
        """
        self.ImageUrl = None
        self.ImageBase64 = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")


class DetectCelebrityResponse(AbstractModel):
    """DetectCelebrity返回參數結構體

    """

    def __init__(self):
        """
        :param Faces: 公衆人物識别結果數組。如果檢測不到人臉，返回爲空；最多可以返回10個人臉識别結果。
        :type Faces: list of Face
        :param Threshold: 本服務在不同誤識率水平下（将圖片中的人物識别錯誤的比例）的推薦阈值，可以用于控制識别結果的精度。 
FalseRate1Percent, FalseRate5Permil, FalseRate1Permil分别代表誤識率在百分之一、千分之五、千分之一情況下的推薦阈值。 
因爲阈值會存在變動，請勿将此處輸出的固定值處理，而是每次取值與confidence對比，來判斷本次的識别結果是否可信。
 例如，如果您業務中可以接受的誤識率是1%，則可以将所有confidence>=FalseRate1Percent的結論認爲是正确的。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Threshold: :class:`tencentcloud.tiia.v20190529.models.Threshold`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Faces = None
        self.Threshold = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Faces") is not None:
            self.Faces = []
            for item in params.get("Faces"):
                obj = Face()
                obj._deserialize(item)
                self.Faces.append(obj)
        if params.get("Threshold") is not None:
            self.Threshold = Threshold()
            self.Threshold._deserialize(params.get("Threshold"))
        self.RequestId = params.get("RequestId")


class DetectDisgustRequest(AbstractModel):
    """DetectDisgust請求參數結構體

    """

    def __init__(self):
        """
        :param ImageUrl: 圖片URL網址。 
圖片限制： 
• 圖片格式：PNG、JPG、JPEG。 
• 圖片大小：所下載圖片經Base64編碼後不超過4M。圖片下載時間不超過3秒。 
建議：
• 圖片像素：大于50*50像素，否則影響識别效果； 
• 長寬比：長邊：短邊<5； 
介面響應時間會受到圖片下載時間的影響，建議使用更可靠的儲存服務，推薦将圖片儲存在Top Cloud COS。
        :type ImageUrl: str
        :param ImageBase64: 圖片經過base64編碼的内容。最大不超過4M。與ImageUrl同時存在時優先使用ImageUrl欄位。
**注意：圖片需要base64編碼，并且要去掉編碼頭部。**
        :type ImageBase64: str
        """
        self.ImageUrl = None
        self.ImageBase64 = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")


class DetectDisgustResponse(AbstractModel):
    """DetectDisgust返回參數結構體

    """

    def __init__(self):
        """
        :param Confidence: 對于圖片中包含惡心内容的置信度，取值[0,1]，一般超過0.5則表明可能是惡心圖片。
        :type Confidence: float
        :param Type: 與圖像内容最相似的惡心内容的類别，包含腐爛、密集、畸形、血腥、蛇、蟲子、牙齒等。
        :type Type: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Confidence = None
        self.Type = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Type = params.get("Type")
        self.RequestId = params.get("RequestId")


class DetectLabelItem(AbstractModel):
    """圖像标簽檢測結果。

    """

    def __init__(self):
        """
        :param Name: 圖片中的物體名稱。
        :type Name: str
        :param Confidence: 算法對于Name的置信度，0-100之間，值越高，表示對于Name越确定。
        :type Confidence: int
        :param FirstCategory: 标簽的一級分類
        :type FirstCategory: str
        :param SecondCategory: 标簽的二級分類
        :type SecondCategory: str
        """
        self.Name = None
        self.Confidence = None
        self.FirstCategory = None
        self.SecondCategory = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Confidence = params.get("Confidence")
        self.FirstCategory = params.get("FirstCategory")
        self.SecondCategory = params.get("SecondCategory")


class DetectLabelRequest(AbstractModel):
    """DetectLabel請求參數結構體

    """

    def __init__(self):
        """
        :param ImageUrl: 圖片URL網址。 
圖片限制： 
• 圖片格式：PNG、JPG、JPEG。 
• 圖片大小：所下載圖片經Base64編碼後不超過4M。圖片下載時間不超過3秒。 
建議：
• 圖片像素：大于50*50像素，否則影響識别效果； 
• 長寬比：長邊：短邊<5； 
介面響應時間會受到圖片下載時間的影響，建議使用更可靠的儲存服務，推薦将圖片儲存在Top Cloud COS。
        :type ImageUrl: str
        :param ImageBase64: 圖片經過base64編碼的内容。最大不超過4M。與ImageUrl同時存在時優先使用ImageUrl欄位。
**注意：圖片需要base64編碼，并且要去掉編碼頭部。**
        :type ImageBase64: str
        :param Scenes: 本次調用支援的識别場景，可選值如下：
WEB，針對網絡圖片優化;
CAMERA，針對手機攝像頭拍攝圖片優化;
ALBUM，針對手機相冊、網盤産品優化;
如果不傳此參數，則預設爲WEB。

支援多場景（Scenes）一起檢測。例如，使用 Scenes=["WEB", "CAMERA"]，即對一張圖片使用兩個模型同時檢測，輸出兩套識别結果。
        :type Scenes: list of str
        """
        self.ImageUrl = None
        self.ImageBase64 = None
        self.Scenes = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")
        self.Scenes = params.get("Scenes")


class DetectLabelResponse(AbstractModel):
    """DetectLabel返回參數結構體

    """

    def __init__(self):
        """
        :param Labels: Web網絡版标簽結果數組。如未選擇WEB場景，則爲空。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Labels: list of DetectLabelItem
        :param CameraLabels: Camera攝像頭版标簽結果數組。如未選擇CAMERA場景，則爲空。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CameraLabels: list of DetectLabelItem
        :param AlbumLabels: Album相冊版标簽結果數組。如未選擇ALBUM場景，則爲空。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AlbumLabels: list of DetectLabelItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Labels = None
        self.CameraLabels = None
        self.AlbumLabels = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = DetectLabelItem()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("CameraLabels") is not None:
            self.CameraLabels = []
            for item in params.get("CameraLabels"):
                obj = DetectLabelItem()
                obj._deserialize(item)
                self.CameraLabels.append(obj)
        if params.get("AlbumLabels") is not None:
            self.AlbumLabels = []
            for item in params.get("AlbumLabels"):
                obj = DetectLabelItem()
                obj._deserialize(item)
                self.AlbumLabels.append(obj)
        self.RequestId = params.get("RequestId")


class DetectMisbehaviorRequest(AbstractModel):
    """DetectMisbehavior請求參數結構體

    """

    def __init__(self):
        """
        :param ImageUrl: 圖片URL網址。 
圖片限制： 
• 圖片格式：PNG、JPG、JPEG。 
• 圖片大小：所下載圖片經Base64編碼後不超過4M。圖片下載時間不超過3秒。 
建議：
• 圖片像素：大于50*50像素，否則影響識别效果； 
• 長寬比：長邊：短邊<5； 
介面響應時間會受到圖片下載時間的影響，建議使用更可靠的儲存服務，推薦将圖片儲存在Top Cloud COS。
        :type ImageUrl: str
        :param ImageBase64: 圖片經過base64編碼的内容。最大不超過4M。與ImageUrl同時存在時優先使用ImageUrl欄位。
**注意：圖片需要base64編碼，并且要去掉編碼頭部。**
        :type ImageBase64: str
        """
        self.ImageUrl = None
        self.ImageBase64 = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")


class DetectMisbehaviorResponse(AbstractModel):
    """DetectMisbehavior返回參數結構體

    """

    def __init__(self):
        """
        :param Confidence: 對于圖片中包含不良行爲的置信度，取值[0,1]，一般超過0.5則表明可能包含不良行爲内容；
        :type Confidence: float
        :param Type: 圖像中最可能包含的不良行爲類别，包括賭博、打架鬥毆、吸毒等。
        :type Type: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Confidence = None
        self.Type = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Type = params.get("Type")
        self.RequestId = params.get("RequestId")


class DetectProductBetaRequest(AbstractModel):
    """DetectProductBeta請求參數結構體

    """

    def __init__(self):
        """
        :param ImageUrl: 圖片限制：内測版僅支援jpg、jpeg，圖片大小不超過1M，分辨率在25萬到100萬之間。 
建議先對圖片進行壓縮，以便提升處理速度。
        :type ImageUrl: str
        :param ImageBase64: 圖片經過base64編碼的内容。最大不超過1M，分辨率在25萬到100萬之間。 
與ImageUrl同時存在時優先使用ImageUrl欄位。
        :type ImageBase64: str
        """
        self.ImageUrl = None
        self.ImageBase64 = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")


class DetectProductBetaResponse(AbstractModel):
    """DetectProductBeta返回參數結構體

    """

    def __init__(self):
        """
        :param RegionDetected: 檢測到的圖片中的商品位置和品類預測。 
當圖片中存在多個商品時，輸出多組坐标，按照__顯著性__排序（綜合考慮面積、是否在中心、檢測算法置信度）。 
最多可以輸出__3組__檢測結果。
        :type RegionDetected: list of RegionDetected
        :param ProductInfo: 圖像識别出的商品的詳細訊息。 
當圖像中檢測到多個物品時，會對顯著性最高的進行識别。
        :type ProductInfo: :class:`tencentcloud.tiia.v20190529.models.ProductInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RegionDetected = None
        self.ProductInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionDetected") is not None:
            self.RegionDetected = []
            for item in params.get("RegionDetected"):
                obj = RegionDetected()
                obj._deserialize(item)
                self.RegionDetected.append(obj)
        if params.get("ProductInfo") is not None:
            self.ProductInfo = ProductInfo()
            self.ProductInfo._deserialize(params.get("ProductInfo"))
        self.RequestId = params.get("RequestId")


class DetectProductRequest(AbstractModel):
    """DetectProduct請求參數結構體

    """

    def __init__(self):
        """
        :param ImageUrl: 圖片URL網址。 
圖片限制： 
• 圖片格式：PNG、JPG、JPEG。 
• 圖片大小：所下載圖片經Base64編碼後不超過4M。圖片下載時間不超過3秒。 
建議：
• 圖片像素：大于50*50像素，否則影響識别效果； 
• 長寬比：長邊：短邊<5； 
介面響應時間會受到圖片下載時間的影響，建議使用更可靠的儲存服務，推薦将圖片儲存在Top Cloud COS。
        :type ImageUrl: str
        :param ImageBase64: 圖片經過base64編碼的内容。最大不超過4M。與ImageUrl同時存在時優先使用ImageUrl欄位。
**注意：圖片需要base64編碼，并且要去掉編碼頭部。**
        :type ImageBase64: str
        """
        self.ImageUrl = None
        self.ImageBase64 = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")


class DetectProductResponse(AbstractModel):
    """DetectProduct返回參數結構體

    """

    def __init__(self):
        """
        :param Products: 商品識别結果數組
        :type Products: list of Product
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Products = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Products") is not None:
            self.Products = []
            for item in params.get("Products"):
                obj = Product()
                obj._deserialize(item)
                self.Products.append(obj)
        self.RequestId = params.get("RequestId")


class EnhanceImageRequest(AbstractModel):
    """EnhanceImage請求參數結構體

    """

    def __init__(self):
        """
        :param ImageUrl: 圖片URL網址。 
圖片限制： 
• 圖片格式：PNG、JPG、JPEG。 
• 圖片大小：所下載圖片經Base64編碼後不超過4M。圖片下載時間不超過3秒。 
建議：
• 圖片像素：大于50*50像素，否則影響識别效果； 
• 長寬比：長邊：短邊<5； 
介面響應時間會受到圖片下載時間的影響，建議使用更可靠的儲存服務，推薦将圖片儲存在Top Cloud COS。
        :type ImageUrl: str
        :param ImageBase64: 支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。圖片經過base64編碼的内容。最大不超過4M。與ImageUrl同時存在時優先使用ImageUrl欄位。
**注意：圖片需要base64編碼，并且要去掉編碼頭部。**
        :type ImageBase64: str
        """
        self.ImageUrl = None
        self.ImageBase64 = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")


class EnhanceImageResponse(AbstractModel):
    """EnhanceImage返回參數結構體

    """

    def __init__(self):
        """
        :param EnhancedImage: 增強後圖片的base64編碼。
        :type EnhancedImage: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.EnhancedImage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnhancedImage = params.get("EnhancedImage")
        self.RequestId = params.get("RequestId")


class Face(AbstractModel):
    """公衆人物識别人臉訊息

    """

    def __init__(self):
        """
        :param Name: 與圖片中人臉最相似的公衆人物的名字。
        :type Name: str
        :param Labels: 公衆人物身份标簽的數組，一個公衆人物可能有多個身份标簽。
        :type Labels: list of Labels
        :param BasicInfo: 對人物的簡介。
        :type BasicInfo: str
        :param Confidence: 算法對于Name的置信度（圖像中人臉與公衆人物的相似度），0-100之間，值越高，表示對于Name越确定。
        :type Confidence: int
        :param X: 人臉區域左上角橫坐标。
        :type X: int
        :param Y: 人臉區域左上角縱坐标。
        :type Y: int
        :param Width: 人臉區域寬度。
        :type Width: int
        :param Height: 人臉區域高度。
        :type Height: int
        :param ID: 公衆人物的唯一編号，可以用于區分同名人物、一個人物不同稱呼等情況。唯一編号爲8個字元構成的字串。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ID: str
        """
        self.Name = None
        self.Labels = None
        self.BasicInfo = None
        self.Confidence = None
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None
        self.ID = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Labels()
                obj._deserialize(item)
                self.Labels.append(obj)
        self.BasicInfo = params.get("BasicInfo")
        self.Confidence = params.get("Confidence")
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ID = params.get("ID")


class Labels(AbstractModel):
    """名人識别的标簽

    """

    def __init__(self):
        """
        :param FirstLabel: 公衆人物身份标簽的一級分類，例如體育明星、娛樂明星、政治人物等；
注意：此欄位可能返回 null，表示取不到有效值。
        :type FirstLabel: str
        :param SecondLabel: 公衆人物身份标簽的二級分類，例如歌手（對應一級标簽爲“娛樂明星”）；
注意：此欄位可能返回 null，表示取不到有效值。
        :type SecondLabel: str
        """
        self.FirstLabel = None
        self.SecondLabel = None


    def _deserialize(self, params):
        self.FirstLabel = params.get("FirstLabel")
        self.SecondLabel = params.get("SecondLabel")


class Location(AbstractModel):
    """檢測到的主體在圖片中的矩形框位置（四個頂點坐标）

    """

    def __init__(self):
        """
        :param XMin: 位置矩形框的左上角橫坐标
        :type XMin: int
        :param YMin: 位置矩形框的左上角縱坐标
        :type YMin: int
        :param XMax: 位置矩形框的右下角橫坐标
        :type XMax: int
        :param YMax: 位置矩形框的右下角縱坐标
        :type YMax: int
        """
        self.XMin = None
        self.YMin = None
        self.XMax = None
        self.YMax = None


    def _deserialize(self, params):
        self.XMin = params.get("XMin")
        self.YMin = params.get("YMin")
        self.XMax = params.get("XMax")
        self.YMax = params.get("YMax")


class Product(AbstractModel):
    """檢測到的單個商品結構體

    """

    def __init__(self):
        """
        :param Name: 圖片中商品的三級分類識别結果，選取所有三級分類中的置信度最大者
        :type Name: str
        :param Parents: 三級商品分類對應的一級分類和二級分類，兩級之間用“-”（中劃線）隔開，例如商品名稱是“硬碟”，那麽Parents輸出爲“電腦、辦公-電腦配件”
        :type Parents: str
        :param Confidence: 算法對于Name的置信度，0-100之間，值越高，表示對于Name越确定
        :type Confidence: int
        :param XMin: 商品坐标X軸的最小值
        :type XMin: int
        :param YMin: 商品坐标Y軸的最小值
        :type YMin: int
        :param XMax: 商品坐标X軸的最大值
        :type XMax: int
        :param YMax: 商品坐标Y軸的最大值
        :type YMax: int
        """
        self.Name = None
        self.Parents = None
        self.Confidence = None
        self.XMin = None
        self.YMin = None
        self.XMax = None
        self.YMax = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Parents = params.get("Parents")
        self.Confidence = params.get("Confidence")
        self.XMin = params.get("XMin")
        self.YMin = params.get("YMin")
        self.XMax = params.get("XMax")
        self.YMax = params.get("YMax")


class ProductInfo(AbstractModel):
    """圖像識别出的商品的詳細訊息。
    當圖像中檢測到多個物品時，會對顯著性最高的物品進行識别。

    """

    def __init__(self):
        """
        :param FindSKU: 1表示找到同款商品，以下欄位爲同款商品訊息； 
0表示未找到同款商品， 具體商品訊息爲空（參考價格、名稱、品牌等），僅提供商品類目。  
是否找到同款的判斷依據爲Score分值，分值越大則同款的可能性越大。
        :type FindSKU: int
        :param Location: 本商品在圖片中的坐标，表示爲矩形框的四個頂點坐标。
        :type Location: :class:`tencentcloud.tiia.v20190529.models.Location`
        :param Name: 商品名稱
        :type Name: str
        :param Brand: 商品品牌
        :type Brand: str
        :param Price: 參考價格，綜合多個訊息源，僅供參考。
        :type Price: str
        :param ProductCategory: 識别結果的商品類目。 
包含：鞋、圖書音像、箱包、美妝個護、服飾、家電數碼、玩具樂器、食品飲料、珠寶、家居家裝、藥品、酒水、綠植園藝、其他商品、非商品等。 
當類别爲“非商品”時，除Location、Score和本欄位之外的商品訊息爲空。
        :type ProductCategory: str
        :param Score: 輸入圖片中的主體物品和輸出結果的相似度。分值越大，輸出結果與輸入圖片是同款的可能性越高。
        :type Score: float
        :param Image: 搜索到的商品配圖URL
        :type Image: str
        """
        self.FindSKU = None
        self.Location = None
        self.Name = None
        self.Brand = None
        self.Price = None
        self.ProductCategory = None
        self.Score = None
        self.Image = None


    def _deserialize(self, params):
        self.FindSKU = params.get("FindSKU")
        if params.get("Location") is not None:
            self.Location = Location()
            self.Location._deserialize(params.get("Location"))
        self.Name = params.get("Name")
        self.Brand = params.get("Brand")
        self.Price = params.get("Price")
        self.ProductCategory = params.get("ProductCategory")
        self.Score = params.get("Score")
        self.Image = params.get("Image")


class RecognizeCarRequest(AbstractModel):
    """RecognizeCar請求參數結構體

    """

    def __init__(self):
        """
        :param ImageUrl: 圖片URL網址。 
圖片限制： 
• 圖片格式：PNG、JPG、JPEG。 
• 圖片大小：所下載圖片經Base64編碼後不超過4M。圖片下載時間不超過3秒。 
建議：
• 圖片像素：大于50*50像素，否則影響識别效果； 
• 長寬比：長邊：短邊<5； 
介面響應時間會受到圖片下載時間的影響，建議使用更可靠的儲存服務，推薦将圖片儲存在Top Cloud COS。
        :type ImageUrl: str
        :param ImageBase64: 圖片經過base64編碼的内容。最大不超過4M。與ImageUrl同時存在時優先使用ImageUrl欄位。
**注意：圖片需要base64編碼，并且要去掉編碼頭部。**
支援的圖片格式：PNG、JPG、JPEG、BMP，暫不支援GIF格式。支援的圖片大小：所下載圖片經Base64編碼後不超過4M。圖片下載時間不超過3秒。
        :type ImageBase64: str
        """
        self.ImageUrl = None
        self.ImageBase64 = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")


class RecognizeCarResponse(AbstractModel):
    """RecognizeCar返回參數結構體

    """

    def __init__(self):
        """
        :param CarCoords: 汽車的四個矩形頂點坐标，如果圖片中存在多輛車，則輸出最大車輛的坐标。
        :type CarCoords: list of Coord
        :param CarTags: 車輛屬性識别的結果數組，如果識别到多輛車，則會輸出每輛車的top1結果。
        :type CarTags: list of CarTagItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CarCoords = None
        self.CarTags = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CarCoords") is not None:
            self.CarCoords = []
            for item in params.get("CarCoords"):
                obj = Coord()
                obj._deserialize(item)
                self.CarCoords.append(obj)
        if params.get("CarTags") is not None:
            self.CarTags = []
            for item in params.get("CarTags"):
                obj = CarTagItem()
                obj._deserialize(item)
                self.CarTags.append(obj)
        self.RequestId = params.get("RequestId")


class RegionDetected(AbstractModel):
    """檢測到的圖片中的商品位置和品類預測。
    當圖片中存在多個商品時，輸出多組坐标，按照__顯著性__排序（綜合考慮面積、是否在中心、檢測算法置信度）。
    最多可以輸出__3組__檢測結果。

    """

    def __init__(self):
        """
        :param Category: 商品的品類預測結果。 
包含：鞋、圖書音像、箱包、美妝個護、服飾、家電數碼、玩具樂器、食品飲料、珠寶、家居家裝、藥品、酒水、綠植園藝、其他商品、非商品等。
        :type Category: str
        :param CategoryScore: 商品品類預測的置信度
        :type CategoryScore: float
        :param Location: 檢測到的主體在圖片中的坐标，表示爲矩形框的四個頂點坐标
        :type Location: :class:`tencentcloud.tiia.v20190529.models.Location`
        """
        self.Category = None
        self.CategoryScore = None
        self.Location = None


    def _deserialize(self, params):
        self.Category = params.get("Category")
        self.CategoryScore = params.get("CategoryScore")
        if params.get("Location") is not None:
            self.Location = Location()
            self.Location._deserialize(params.get("Location"))


class Threshold(AbstractModel):
    """本服務在不同誤識率水平下（将圖片中的人物識别錯誤的比例）的推薦阈值，可以用于控制識别結果的精度。
    {FalseRate1Percent, FalseRate5Permil, FalseRate1Permil}分别代表誤識率在百分之一、千分之五、千分之一情況下的推薦阈值。
    因爲阈值會存在變動，請勿将此處輸出的固定值處理，而是每次取值與confidence對比，來判斷本次的識别結果是否可信。
    例如，如果您業務中可以接受的誤識率是1%，則可以将所有confidence>=FalseRate1Percent的結論認爲是正确的。

    """

    def __init__(self):
        """
        :param FalseRate1Percent: 誤識率在百分之一時的推薦阈值。
        :type FalseRate1Percent: int
        :param FalseRate5Permil: 誤識率在千分之五時的推薦阈值。
        :type FalseRate5Permil: int
        :param FalseRate1Permil: 誤識率在千分之一時的推薦阈值。
        :type FalseRate1Permil: int
        """
        self.FalseRate1Percent = None
        self.FalseRate5Permil = None
        self.FalseRate1Permil = None


    def _deserialize(self, params):
        self.FalseRate1Percent = params.get("FalseRate1Percent")
        self.FalseRate5Permil = params.get("FalseRate5Permil")
        self.FalseRate1Permil = params.get("FalseRate1Permil")