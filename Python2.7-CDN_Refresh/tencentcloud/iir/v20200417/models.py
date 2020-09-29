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


class Location(AbstractModel):
    """檢測到的主體在圖片中的矩形框位置（四個頂點坐標）

    """

    def __init__(self):
        """
        :param XMin: 位置矩形框的左上角橫坐標
        :type XMin: int
        :param YMin: 位置矩形框的左上角縱坐標
        :type YMin: int
        :param XMax: 位置矩形框的右下角橫坐標
        :type XMax: int
        :param YMax: 位置矩形框的右下角縱坐標
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
        :param Location: 本商品在圖片中的坐標，表示爲矩形框的四個頂點坐標。
        :type Location: :class:`taifucloudcloud.iir.v20200417.models.Location`
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


class RecognizeProductRequest(AbstractModel):
    """RecognizeProduct請求參數結構體

    """

    def __init__(self):
        """
        :param ImageUrl: 圖片限制：内測版僅支援jpg、jpeg，圖片大小不超過1M，分辨率在25萬到100萬之間。 
建議先對圖片進行壓縮，以便提升處理速度。
        :type ImageUrl: str
        :param ImageBase64: 圖片經過base64編碼的内容。最大不超過1M，分辨率在25萬到100萬之間。 
與ImageUrl同時存在時優先使用ImageUrl欄位。
**注意：圖片需要base64編碼，並且要去掉編碼頭部。**
        :type ImageBase64: str
        """
        self.ImageUrl = None
        self.ImageBase64 = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.ImageBase64 = params.get("ImageBase64")


class RecognizeProductResponse(AbstractModel):
    """RecognizeProduct返回參數結構體

    """

    def __init__(self):
        """
        :param RegionDetected: 檢測到的圖片中的商品位置和品類預測。 
當圖片中存在多個商品時，輸出多組坐標，按照__顯著性__排序（綜合考慮面積、是否在中心、檢測算法置信度）。 
最多可以輸出__3組__檢測結果。
        :type RegionDetected: list of RegionDetected
        :param ProductInfo: 圖像識别出的商品的詳細訊息。 
當圖像中檢測到多個物品時，會對顯著性最高的進行識别。
        :type ProductInfo: :class:`taifucloudcloud.iir.v20200417.models.ProductInfo`
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


class RegionDetected(AbstractModel):
    """檢測到的圖片中的商品位置和品類預測。
    當圖片中存在多個商品時，輸出多組坐標，按照__顯著性__排序（綜合考慮面積、是否在中心、檢測算法置信度）。
    最多可以輸出__3組__檢測結果。

    """

    def __init__(self):
        """
        :param Category: 商品的品類預測結果。 
包含：鞋、圖書音像、箱包、美妝個護、服飾、家電數碼、玩具樂器、食品飲料、珠寶、家居家裝、藥品、酒水、綠植園藝、其他商品、非商品等。
        :type Category: str
        :param CategoryScore: 商品品類預測的置信度
        :type CategoryScore: float
        :param Location: 檢測到的主體在圖片中的坐標，表示爲矩形框的四個頂點坐標
        :type Location: :class:`taifucloudcloud.iir.v20200417.models.Location`
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