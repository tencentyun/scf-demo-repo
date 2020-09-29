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


class AnalyzeFaceRequest(AbstractModel):
    """AnalyzeFace請求參數結構體

    """

    def __init__(self):
        """
        :param Mode: 檢測模式。0 爲檢測所有出現的人臉， 1 爲檢測面積最大的人臉。預設爲 0。最多返回 10 張人臉的五官定位（人臉關鍵點）具體訊息。
        :type Mode: int
        :param Image: 圖片 base64 數據，base64 編碼後大小不可超過5M。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Image: str
        :param Url: 圖片的 Url 。對應圖片 base64 編碼後大小不可超過5M。
Url、Image必須提供一個，如果都提供，只使用 Url。  
圖片儲存於Top Cloud 的Url可保障更高下載速度和穩定性，建議圖片儲存於Top Cloud 。 
非Top Cloud 儲存的Url速度和穩定性可能受一定影響。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Url: str
        :param FaceModelVersion: 人臉識别服務所用的算法模型版本。目前入參支援 “2.0”和“3.0“ 兩個輸入。  
2020年4月2日開始，預設爲“3.0”，之前使用過本介面的賬號若未填寫本參數預設爲“2.0”。  
不同算法模型版本對應的人臉識别算法不同，新版本的整體效果會優於舊版本，建議使用最新版本。
        :type FaceModelVersion: str
        :param NeedRotateDetection: 是否開啓圖片旋轉識别支援。0爲不開啓，1爲開啓。預設爲0。本參數的作用爲，當圖片中的人臉被旋轉且圖片沒有exif訊息時，如果不開啓圖片旋轉識别支援則無法正确檢測、識别圖片中的人臉。若您确認圖片包含exif訊息或者您确認輸入圖中人臉不會出現被旋轉情況，請不要開啓本參數。開啓後，整體耗時将可能增加數百毫秒。
        :type NeedRotateDetection: int
        """
        self.Mode = None
        self.Image = None
        self.Url = None
        self.FaceModelVersion = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class AnalyzeFaceResponse(AbstractModel):
    """AnalyzeFace返回參數結構體

    """

    def __init__(self):
        """
        :param ImageWidth: 請求的圖片寬度。
        :type ImageWidth: int
        :param ImageHeight: 請求的圖片高度。
        :type ImageHeight: int
        :param FaceShapeSet: 五官定位（人臉關鍵點）具體訊息。
        :type FaceShapeSet: list of FaceShape
        :param FaceModelVersion: 人臉識别所用的算法模型版本。
        :type FaceModelVersion: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ImageWidth = None
        self.ImageHeight = None
        self.FaceShapeSet = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageWidth = params.get("ImageWidth")
        self.ImageHeight = params.get("ImageHeight")
        if params.get("FaceShapeSet") is not None:
            self.FaceShapeSet = []
            for item in params.get("FaceShapeSet"):
                obj = FaceShape()
                obj._deserialize(item)
                self.FaceShapeSet.append(obj)
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class Candidate(AbstractModel):
    """識别出的最相似候選人

    """

    def __init__(self):
        """
        :param PersonId: 人員ID
        :type PersonId: str
        :param FaceId: 人臉ID
        :type FaceId: str
        :param Score: 候選者的比對得分。 

1萬大小人臉底庫下，誤識率百分之一對應分數爲70分，誤識率千分之一對應分數爲80分，誤識率萬分之一對應分數爲90分；
10萬大小人臉底庫下，誤識率百分之一對應分數爲80分，誤識率千分之一對應分數爲90分，誤識率萬分之一對應分數爲100分；
30萬大小人臉底庫下，誤識率百分之一對應分數爲85分，誤識率千分之一對應分數爲95分。

一般80分左右可适用大部分場景，建議分數不要超過90分。您可以根據實際情況選擇合适的分數。
        :type Score: float
        :param PersonName: 人員名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type PersonName: str
        :param Gender: 人員性别
注意：此欄位可能返回 null，表示取不到有效值。
        :type Gender: int
        :param PersonGroupInfos: 包含此人員的人員庫及描述欄位内容清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type PersonGroupInfos: list of PersonGroupInfo
        """
        self.PersonId = None
        self.FaceId = None
        self.Score = None
        self.PersonName = None
        self.Gender = None
        self.PersonGroupInfos = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.FaceId = params.get("FaceId")
        self.Score = params.get("Score")
        self.PersonName = params.get("PersonName")
        self.Gender = params.get("Gender")
        if params.get("PersonGroupInfos") is not None:
            self.PersonGroupInfos = []
            for item in params.get("PersonGroupInfos"):
                obj = PersonGroupInfo()
                obj._deserialize(item)
                self.PersonGroupInfos.append(obj)


class CheckSimilarPersonRequest(AbstractModel):
    """CheckSimilarPerson請求參數結構體

    """

    def __init__(self):
        """
        :param GroupIds: 待整理的人員庫清單。 
人員庫總人數不可超過200萬，人員庫個數不可超過10個。
        :type GroupIds: list of str
        :param UniquePersonControl: 人員查重整理力度的控制。
1：力度較高的檔案整理，能夠消除更多的重複身份，對應稍高的非重複身份誤清除率；
2：力度較低的檔案整理，非重複身份的誤清除率較低，對應稍低的重複身份消除率。
        :type UniquePersonControl: int
        """
        self.GroupIds = None
        self.UniquePersonControl = None


    def _deserialize(self, params):
        self.GroupIds = params.get("GroupIds")
        self.UniquePersonControl = params.get("UniquePersonControl")


class CheckSimilarPersonResponse(AbstractModel):
    """CheckSimilarPerson返回參數結構體

    """

    def __init__(self):
        """
        :param JobId: 查重任務ID，用於查詢、獲取查重的進度和結果。
        :type JobId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class CompareFaceRequest(AbstractModel):
    """CompareFace請求參數結構體

    """

    def __init__(self):
        """
        :param ImageA: A 圖片 base64 數據，base64 編碼後大小不可超過5M。
若圖片中包含多張人臉，只選取其中人臉面積最大的人臉。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type ImageA: str
        :param ImageB: B 圖片 base64 數據，base64 編碼後大小不可超過5M。
若圖片中包含多張人臉，只選取其中人臉面積最大的人臉。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type ImageB: str
        :param UrlA: A 圖片的 Url ，對應圖片 base64 編碼後大小不可超過5M。
A 圖片的 Url、Image必須提供一個，如果都提供，只使用 Url。 
圖片儲存於Top Cloud 的Url可保障更高下載速度和穩定性，建議圖片儲存於Top Cloud 。 
非Top Cloud 儲存的Url速度和穩定性可能受一定影響。
若圖片中包含多張人臉，只選取其中人臉面積最大的人臉。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type UrlA: str
        :param UrlB: B 圖片的 Url ，對應圖片 base64 編碼後大小不可超過5M。
B 圖片的 Url、Image必須提供一個，如果都提供，只使用 Url。 
圖片儲存於Top Cloud 的Url可保障更高下載速度和穩定性，建議圖片儲存於Top Cloud 。 
非Top Cloud 儲存的Url速度和穩定性可能受一定影響。
若圖片中包含多張人臉，只選取其中人臉面積最大的人臉。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type UrlB: str
        :param FaceModelVersion: 人臉識别服務所用的算法模型版本。目前入參支援 “2.0”和“3.0“ 兩個輸入。 
2020年4月2日開始，預設爲“3.0”，之前使用過本介面的賬號若未填寫本參數預設爲“2.0”。 
不同算法模型版本對應的人臉識别算法不同，新版本的整體效果會優於舊版本，建議使用“3.0”版本。
        :type FaceModelVersion: str
        :param QualityControl: 圖片質量控制。 
0: 不進行控制； 
1:較低的質量要求，圖像存在非常模糊，眼睛鼻子嘴巴遮擋至少其中一種或多種的情況； 
2: 一般的質量要求，圖像存在偏亮，偏暗，模糊或一般模糊，眉毛遮擋，臉頰遮擋，下巴遮擋，至少其中三種的情況； 
3: 較高的質量要求，圖像存在偏亮，偏暗，一般模糊，眉毛遮擋，臉頰遮擋，下巴遮擋，其中一到兩種的情況； 
4: 很高的質量要求，各個維度均爲最好或最多在某一維度上存在輕微問題； 
預設 0。 
若圖片質量不滿足要求，則返回結果中會提示圖片質量檢測不符要求。
        :type QualityControl: int
        :param NeedRotateDetection: 是否開啓圖片旋轉識别支援。0爲不開啓，1爲開啓。預設爲0。本參數的作用爲，當圖片中的人臉被旋轉且圖片沒有exif訊息時，如果不開啓圖片旋轉識别支援則無法正确檢測、識别圖片中的人臉。若您确認圖片包含exif訊息或者您确認輸入圖中人臉不會出現被旋轉情況，請不要開啓本參數。開啓後，整體耗時将可能增加數百毫秒。
        :type NeedRotateDetection: int
        """
        self.ImageA = None
        self.ImageB = None
        self.UrlA = None
        self.UrlB = None
        self.FaceModelVersion = None
        self.QualityControl = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.ImageA = params.get("ImageA")
        self.ImageB = params.get("ImageB")
        self.UrlA = params.get("UrlA")
        self.UrlB = params.get("UrlB")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.QualityControl = params.get("QualityControl")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class CompareFaceResponse(AbstractModel):
    """CompareFace返回參數結構體

    """

    def __init__(self):
        """
        :param Score: 兩張圖片中人臉的相似度分數。
不同算法版本返回的相似度分數不同。 
若需要驗證兩張圖片中人臉是否爲同一人，3.0版本誤識率千分之一對應分數爲40分，誤識率萬分之一對應分數爲50分，誤識率十萬分之一對應分數爲60分。  一般超過50分則可認定爲同一人。 
2.0版本誤識率千分之一對應分數爲70分，誤識率萬分之一對應分數爲80分，誤識率十萬分之一對應分數爲90分。 一般超過80分則可認定爲同一人。 
若需要驗證兩張圖片中的人臉是否爲同一人，建議使用人臉驗證介面。
        :type Score: float
        :param FaceModelVersion: 人臉識别所用的算法模型版本。
        :type FaceModelVersion: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Score = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Score = params.get("Score")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class CopyPersonRequest(AbstractModel):
    """CopyPerson請求參數結構體

    """

    def __init__(self):
        """
        :param PersonId: 人員ID
        :type PersonId: str
        :param GroupIds: 待加入的人員庫清單
        :type GroupIds: list of str
        """
        self.PersonId = None
        self.GroupIds = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.GroupIds = params.get("GroupIds")


class CopyPersonResponse(AbstractModel):
    """CopyPerson返回參數結構體

    """

    def __init__(self):
        """
        :param SucGroupNum: 成功加入的人員庫數量
        :type SucGroupNum: int
        :param SucGroupIds: 成功加入的人員庫清單
        :type SucGroupIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SucGroupNum = None
        self.SucGroupIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SucGroupNum = params.get("SucGroupNum")
        self.SucGroupIds = params.get("SucGroupIds")
        self.RequestId = params.get("RequestId")


class CreateFaceRequest(AbstractModel):
    """CreateFace請求參數結構體

    """

    def __init__(self):
        """
        :param PersonId: 人員ID。
        :type PersonId: str
        :param Images: 圖片 base64 數據，base64 編碼後大小不可超過5M。
人員人臉總數量不可超過5張。
若圖片中包含多張人臉，只選取其中人臉面積最大的人臉。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Images: list of str
        :param Urls: 圖片的 Url 。對應圖片 base64 編碼後大小不可超過5M。
Url、Image必須提供一個，如果都提供，只使用 Url。  
圖片儲存於Top Cloud 的Url可保障更高下載速度和穩定性，建議圖片儲存於Top Cloud 。 
非Top Cloud 儲存的Url速度和穩定性可能受一定影響。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
人員人臉總數量不可超過5張。
若圖片中包含多張人臉，只選取其中人臉面積最大的人臉。
        :type Urls: list of str
        :param FaceMatchThreshold: 只有和該人員已有的人臉相似度超過FaceMatchThreshold值的人臉，才能增加人臉成功。 
預設值60分。取值範圍[0,100] 。
        :type FaceMatchThreshold: float
        :param QualityControl: 圖片質量控制。 
0: 不進行控制； 
1:較低的質量要求，圖像存在非常模糊，眼睛鼻子嘴巴遮擋至少其中一種或多種的情況； 
2: 一般的質量要求，圖像存在偏亮，偏暗，模糊或一般模糊，眉毛遮擋，臉頰遮擋，下巴遮擋，至少其中三種的情況； 
3: 較高的質量要求，圖像存在偏亮，偏暗，一般模糊，眉毛遮擋，臉頰遮擋，下巴遮擋，其中一到兩種的情況； 
4: 很高的質量要求，各個維度均爲最好或最多在某一維度上存在輕微問題； 
預設 0。 
若圖片質量不滿足要求，則返回結果中會提示圖片質量檢測不符要求。
        :type QualityControl: int
        :param NeedRotateDetection: 是否開啓圖片旋轉識别支援。0爲不開啓，1爲開啓。預設爲0。本參數的作用爲，當圖片中的人臉被旋轉且圖片沒有exif訊息時，如果不開啓圖片旋轉識别支援則無法正确檢測、識别圖片中的人臉。若您确認圖片包含exif訊息或者您确認輸入圖中人臉不會出現被旋轉情況，請不要開啓本參數。開啓後，整體耗時将可能增加數百毫秒。
        :type NeedRotateDetection: int
        """
        self.PersonId = None
        self.Images = None
        self.Urls = None
        self.FaceMatchThreshold = None
        self.QualityControl = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Images = params.get("Images")
        self.Urls = params.get("Urls")
        self.FaceMatchThreshold = params.get("FaceMatchThreshold")
        self.QualityControl = params.get("QualityControl")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class CreateFaceResponse(AbstractModel):
    """CreateFace返回參數結構體

    """

    def __init__(self):
        """
        :param SucFaceNum: 加入成功的人臉數量
        :type SucFaceNum: int
        :param SucFaceIds: 加入成功的人臉ID清單
        :type SucFaceIds: list of str
        :param RetCode: 每張人臉圖片添加結果，-1101 代表未檢測到人臉，-1102 代表圖片解碼失敗， 
-1601代表不符合圖片質量控制要求, -1604 代表人臉相似度沒有超過FaceMatchThreshold。 
其他非 0 值代表算法服務異常。 
RetCode的順序和入參中 Images 或 Urls 的順序一緻。
        :type RetCode: list of int
        :param SucIndexes: 加入成功的人臉索引。索引順序和入參中 Images 或 Urls 的順序一緻。 
例， Urls 中 有 3 個 url，第二個 url 失敗，則 SucIndexes 值爲 [0,2] 。
        :type SucIndexes: list of int non-negative
        :param SucFaceRects: 加入成功的人臉框位置。順序和入參中 Images 或 Urls 的順序一緻。
        :type SucFaceRects: list of FaceRect
        :param FaceModelVersion: 人臉識别所用的算法模型版本。
        :type FaceModelVersion: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SucFaceNum = None
        self.SucFaceIds = None
        self.RetCode = None
        self.SucIndexes = None
        self.SucFaceRects = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SucFaceNum = params.get("SucFaceNum")
        self.SucFaceIds = params.get("SucFaceIds")
        self.RetCode = params.get("RetCode")
        self.SucIndexes = params.get("SucIndexes")
        if params.get("SucFaceRects") is not None:
            self.SucFaceRects = []
            for item in params.get("SucFaceRects"):
                obj = FaceRect()
                obj._deserialize(item)
                self.SucFaceRects.append(obj)
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class CreateGroupRequest(AbstractModel):
    """CreateGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupName: 人員庫名稱，[1,60]個字元，可修改，不可重複。
        :type GroupName: str
        :param GroupId: 人員庫 ID，不可修改，不可重複。支援英文、數字、-%@#&_，長度限制64B。
        :type GroupId: str
        :param GroupExDescriptions: 人員庫自定義描述欄位，用於描述人員庫中人員屬性，該人員庫下所有人員将擁有此描述欄位。 
最多可以創建5個。 
每個自定義描述欄位支援[1,30]個字元。 
在同一人員庫中自定義描述欄位不可重複。 
例： 設置某人員庫“自定義描述欄位”爲["學號","工號","手機號"]， 
則該人員庫下所有人員将擁有名爲“學號”、“工號”、“手機號”的描述欄位， 
可在對應人員描述欄位中填寫内容，登記該人員的學號、工號、手機號等訊息。
        :type GroupExDescriptions: list of str
        :param Tag: 人員庫訊息備注，[0，40]個字元。
        :type Tag: str
        :param FaceModelVersion: 人臉識别服務所用的算法模型版本。目前入參支援 “2.0”和“3.0“ 兩個輸入。
2020年4月2日開始，預設爲“3.0”，之前使用過本介面的賬號若未填寫本參數預設爲“2.0”。 
不同算法模型版本對應的人臉識别算法不同，新版本的整體效果會優於舊版本，建議使用“3.0”版本。
        :type FaceModelVersion: str
        """
        self.GroupName = None
        self.GroupId = None
        self.GroupExDescriptions = None
        self.Tag = None
        self.FaceModelVersion = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupId = params.get("GroupId")
        self.GroupExDescriptions = params.get("GroupExDescriptions")
        self.Tag = params.get("Tag")
        self.FaceModelVersion = params.get("FaceModelVersion")


class CreateGroupResponse(AbstractModel):
    """CreateGroup返回參數結構體

    """

    def __init__(self):
        """
        :param FaceModelVersion: 人臉識别所用的算法模型版本。
        :type FaceModelVersion: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class CreatePersonRequest(AbstractModel):
    """CreatePerson請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 待加入的人員庫ID。
        :type GroupId: str
        :param PersonName: 人員名稱。[1，60]個字元，可修改，可重複。
        :type PersonName: str
        :param PersonId: 人員ID，單個Top Cloud 賬號下不可修改，不可重複。支援英文、數字、-%@#&_，長度限制64B。
        :type PersonId: str
        :param Gender: 0代表未填寫，1代表男性，2代表女性。
        :type Gender: int
        :param PersonExDescriptionInfos: 人員描述欄位内容，key-value。[0，60]個字元，可修改，可重複。
        :type PersonExDescriptionInfos: list of PersonExDescriptionInfo
        :param Image: 圖片 base64 數據，base64 編碼後大小不可超過5M。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Image: str
        :param Url: 圖片的 Url 。對應圖片 base64 編碼後大小不可超過5M。
Url、Image必須提供一個，如果都提供，只使用 Url。  
圖片儲存於Top Cloud 的Url可保障更高下載速度和穩定性，建議圖片儲存於Top Cloud 。 
非Top Cloud 儲存的Url速度和穩定性可能受一定影響。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Url: str
        :param UniquePersonControl: 此參數用於控制判斷 Image 或 Url 中圖片包含的人臉，是否在人員庫中已有疑似的同一人。 
如果判斷爲已有相同人在人員庫中，則不會創建新的人員，返回疑似同一人的人員訊息。 
如果判斷沒有，則完成創建人員。 
0: 不進行判斷，無論是否有疑似同一人在庫中均完成入庫； 
1:較低的同一人判斷要求（百一誤識别率）； 
2: 一般的同一人判斷要求（千一誤識别率）； 
3: 較高的同一人判斷要求（萬一誤識别率）； 
4: 很高的同一人判斷要求（十萬一誤識别率）。 
預設 0。  
注： 要求越高，則疑似同一人的概率越小。不同要求對應的誤識别率僅爲參考值，您可以根據實際情況調整。
        :type UniquePersonControl: int
        :param QualityControl: 圖片質量控制。 
0: 不進行控制； 
1:較低的質量要求，圖像存在非常模糊，眼睛鼻子嘴巴遮擋至少其中一種或多種的情況； 
2: 一般的質量要求，圖像存在偏亮，偏暗，模糊或一般模糊，眉毛遮擋，臉頰遮擋，下巴遮擋，至少其中三種的情況； 
3: 較高的質量要求，圖像存在偏亮，偏暗，一般模糊，眉毛遮擋，臉頰遮擋，下巴遮擋，其中一到兩種的情況； 
4: 很高的質量要求，各個維度均爲最好或最多在某一維度上存在輕微問題； 
預設 0。 
若圖片質量不滿足要求，則返回結果中會提示圖片質量檢測不符要求。
        :type QualityControl: int
        :param NeedRotateDetection: 是否開啓圖片旋轉識别支援。0爲不開啓，1爲開啓。預設爲0。本參數的作用爲，當圖片中的人臉被旋轉且圖片沒有exif訊息時，如果不開啓圖片旋轉識别支援則無法正确檢測、識别圖片中的人臉。若您确認圖片包含exif訊息或者您确認輸入圖中人臉不會出現被旋轉情況，請不要開啓本參數。開啓後，整體耗時将可能增加數百毫秒。
        :type NeedRotateDetection: int
        """
        self.GroupId = None
        self.PersonName = None
        self.PersonId = None
        self.Gender = None
        self.PersonExDescriptionInfos = None
        self.Image = None
        self.Url = None
        self.UniquePersonControl = None
        self.QualityControl = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.PersonName = params.get("PersonName")
        self.PersonId = params.get("PersonId")
        self.Gender = params.get("Gender")
        if params.get("PersonExDescriptionInfos") is not None:
            self.PersonExDescriptionInfos = []
            for item in params.get("PersonExDescriptionInfos"):
                obj = PersonExDescriptionInfo()
                obj._deserialize(item)
                self.PersonExDescriptionInfos.append(obj)
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.UniquePersonControl = params.get("UniquePersonControl")
        self.QualityControl = params.get("QualityControl")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class CreatePersonResponse(AbstractModel):
    """CreatePerson返回參數結構體

    """

    def __init__(self):
        """
        :param FaceId: 人臉圖片唯一標識。
        :type FaceId: str
        :param FaceRect: 檢測出的人臉框的位置。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FaceRect: :class:`taifucloudcloud.iai.v20180301.models.FaceRect`
        :param SimilarPersonId: 疑似同一人的PersonId。 
當 UniquePersonControl 參數不爲0且人員庫中有疑似的同一人，此參數才有意義。
        :type SimilarPersonId: str
        :param FaceModelVersion: 人臉識别所用的算法模型版本。
        :type FaceModelVersion: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FaceId = None
        self.FaceRect = None
        self.SimilarPersonId = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FaceId = params.get("FaceId")
        if params.get("FaceRect") is not None:
            self.FaceRect = FaceRect()
            self.FaceRect._deserialize(params.get("FaceRect"))
        self.SimilarPersonId = params.get("SimilarPersonId")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class DeleteFaceRequest(AbstractModel):
    """DeleteFace請求參數結構體

    """

    def __init__(self):
        """
        :param PersonId: 人員ID
        :type PersonId: str
        :param FaceIds: 待删除的人臉ID清單
        :type FaceIds: list of str
        """
        self.PersonId = None
        self.FaceIds = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.FaceIds = params.get("FaceIds")


class DeleteFaceResponse(AbstractModel):
    """DeleteFace返回參數結構體

    """

    def __init__(self):
        """
        :param SucDeletedNum: 删除成功的人臉數量
        :type SucDeletedNum: int
        :param SucFaceIds: 删除成功的人臉ID清單
        :type SucFaceIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SucDeletedNum = None
        self.SucFaceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SucDeletedNum = params.get("SucDeletedNum")
        self.SucFaceIds = params.get("SucFaceIds")
        self.RequestId = params.get("RequestId")


class DeleteGroupRequest(AbstractModel):
    """DeleteGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 人員庫ID。
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DeleteGroupResponse(AbstractModel):
    """DeleteGroup返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePersonFromGroupRequest(AbstractModel):
    """DeletePersonFromGroup請求參數結構體

    """

    def __init__(self):
        """
        :param PersonId: 人員ID
        :type PersonId: str
        :param GroupId: 人員庫ID
        :type GroupId: str
        """
        self.PersonId = None
        self.GroupId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.GroupId = params.get("GroupId")


class DeletePersonFromGroupResponse(AbstractModel):
    """DeletePersonFromGroup返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePersonRequest(AbstractModel):
    """DeletePerson請求參數結構體

    """

    def __init__(self):
        """
        :param PersonId: 人員ID
        :type PersonId: str
        """
        self.PersonId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")


class DeletePersonResponse(AbstractModel):
    """DeletePerson返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DetectFaceRequest(AbstractModel):
    """DetectFace請求參數結構體

    """

    def __init__(self):
        """
        :param MaxFaceNum: 最多處理的人臉數目。預設值爲1（僅檢測圖片中面積最大的那張人臉），最大值爲120。 
此參數用於控制處理待檢測圖片中的人臉個數，值越小，處理速度越快。
        :type MaxFaceNum: int
        :param MinFaceSize: 人臉長和寬的最小尺寸，單位爲像素。
預設爲34。建議不低於34。
低於MinFaceSize值的人臉不會被檢測。
        :type MinFaceSize: int
        :param Image: 圖片 base64 數據，base64 編碼後大小不可超過5M。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Image: str
        :param Url: 圖片的 Url 。對應圖片 base64 編碼後大小不可超過5M。
Url、Image必須提供一個，如果都提供，只使用 Url。  
圖片儲存於Top Cloud 的Url可保障更高下載速度和穩定性，建議圖片儲存於Top Cloud 。 
非Top Cloud 儲存的Url速度和穩定性可能受一定影響。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Url: str
        :param NeedFaceAttributes: 是否需要返回人臉屬性訊息（FaceAttributesInfo）。0 爲不需要返回，1 爲需要返回。預設爲 0。 
非 1 值均視爲不需要返回，此時 FaceAttributesInfo 不具備參考意義。  
最多返回面積最大的 5 張人臉屬性訊息，超過 5 張人臉（第 6 張及以後的人臉）的 FaceAttributesInfo 不具備參考意義。  
提取人臉屬性訊息較爲耗時，如不需要人臉屬性訊息，建議關閉此項功能，加快人臉檢測速度。
        :type NeedFaceAttributes: int
        :param NeedQualityDetection: 是否開啓質量檢測。0 爲關閉，1 爲開啓。預設爲 0。 
非 1 值均視爲不進行質量檢測。
最多返回面積最大的 30 張人臉質量分訊息，超過 30 張人臉（第 31 張及以後的人臉）的 FaceQualityInfo不具備參考意義。  
建議：人臉入庫操作建議開啓此功能。
        :type NeedQualityDetection: int
        :param FaceModelVersion: 人臉識别服務所用的算法模型版本。目前入參支援 “2.0”和“3.0“ 兩個輸入。  
2020年4月2日開始，預設爲“3.0”，之前使用過本介面的賬號若未填寫本參數預設爲“2.0”。 
不同算法模型版本對應的人臉識别算法不同，新版本的整體效果會優於舊版本，建議使用“3.0”版本。
        :type FaceModelVersion: str
        :param NeedRotateDetection: 是否開啓圖片旋轉識别支援。0爲不開啓，1爲開啓。預設爲0。本參數的作用爲，當圖片中的人臉被旋轉且圖片沒有exif訊息時，如果不開啓圖片旋轉識别支援則無法正确檢測、識别圖片中的人臉。若您确認圖片包含exif訊息或者您确認輸入圖中人臉不會出現被旋轉情況，請不要開啓本參數。開啓後，整體耗時将可能增加數百毫秒。
        :type NeedRotateDetection: int
        """
        self.MaxFaceNum = None
        self.MinFaceSize = None
        self.Image = None
        self.Url = None
        self.NeedFaceAttributes = None
        self.NeedQualityDetection = None
        self.FaceModelVersion = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.MaxFaceNum = params.get("MaxFaceNum")
        self.MinFaceSize = params.get("MinFaceSize")
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.NeedFaceAttributes = params.get("NeedFaceAttributes")
        self.NeedQualityDetection = params.get("NeedQualityDetection")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class DetectFaceResponse(AbstractModel):
    """DetectFace返回參數結構體

    """

    def __init__(self):
        """
        :param ImageWidth: 請求的圖片寬度。
        :type ImageWidth: int
        :param ImageHeight: 請求的圖片高度。
        :type ImageHeight: int
        :param FaceInfos: 人臉訊息清單。包含人臉坐標訊息、屬性訊息（若需要）、質量分訊息（若需要）。
        :type FaceInfos: list of FaceInfo
        :param FaceModelVersion: 人臉識别所用的算法模型版本。
        :type FaceModelVersion: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ImageWidth = None
        self.ImageHeight = None
        self.FaceInfos = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageWidth = params.get("ImageWidth")
        self.ImageHeight = params.get("ImageHeight")
        if params.get("FaceInfos") is not None:
            self.FaceInfos = []
            for item in params.get("FaceInfos"):
                obj = FaceInfo()
                obj._deserialize(item)
                self.FaceInfos.append(obj)
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class DetectLiveFaceRequest(AbstractModel):
    """DetectLiveFace請求參數結構體

    """

    def __init__(self):
        """
        :param Image: 圖片 base64 數據，base64 編碼後大小不可超過5M（圖片的寬高比請接近3:4，不符合寬高比的圖片返回的分值不具備參考意義）。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Image: str
        :param Url: 圖片的 Url 。對應圖片 base64 編碼後大小不可超過5M。
Url、Image必須提供一個，如果都提供，只使用 Url。 
（圖片的寬高比請接近 3:4，不符合寬高比的圖片返回的分值不具備參考意義） 
圖片儲存於Top Cloud 的Url可保障更高下載速度和穩定性，建議圖片儲存於Top Cloud 。 
非Top Cloud 儲存的Url速度和穩定性可能受一定影響。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Url: str
        :param FaceModelVersion: 人臉識别服務所用的算法模型版本。目前入參支援 “2.0”和“3.0“ 兩個輸入。  
2020年4月2日開始，預設爲“3.0”，之前使用過本介面的賬號若未填寫本參數預設爲“2.0”。 
不同算法模型版本對應的人臉識别算法不同，新版本的整體效果會優於舊版本，建議使用“3.0”版本。
        :type FaceModelVersion: str
        """
        self.Image = None
        self.Url = None
        self.FaceModelVersion = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.FaceModelVersion = params.get("FaceModelVersion")


class DetectLiveFaceResponse(AbstractModel):
    """DetectLiveFace返回參數結構體

    """

    def __init__(self):
        """
        :param Score: 活體打分，取值範圍 [0,100]，分數一般落於[80, 100]區間内，0分也爲常見值。推薦相大於 87 時可判斷爲活體。可根據具體場景自行調整阈值。
本欄位當且僅當FaceModelVersion爲2.0時才具備參考意義。
        :type Score: float
        :param FaceModelVersion: 人臉識别所用的算法模型版本。
        :type FaceModelVersion: str
        :param IsLiveness: 活體檢測是否通過。
本欄位只有FaceModelVersion爲3.0時才具備參考意義。
        :type IsLiveness: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Score = None
        self.FaceModelVersion = None
        self.IsLiveness = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Score = params.get("Score")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.IsLiveness = params.get("IsLiveness")
        self.RequestId = params.get("RequestId")


class EstimateCheckSimilarPersonCostTimeRequest(AbstractModel):
    """EstimateCheckSimilarPersonCostTime請求參數結構體

    """

    def __init__(self):
        """
        :param GroupIds: 待整理的人員庫清單。 
人員庫總人數不可超過200萬，人員庫個數不可超過10個。
        :type GroupIds: list of str
        """
        self.GroupIds = None


    def _deserialize(self, params):
        self.GroupIds = params.get("GroupIds")


class EstimateCheckSimilarPersonCostTimeResponse(AbstractModel):
    """EstimateCheckSimilarPersonCostTime返回參數結構體

    """

    def __init__(self):
        """
        :param EstimatedTimeCost: 人員查重任務預估需要耗費時間。 單位爲分鍾。
        :type EstimatedTimeCost: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.EstimatedTimeCost = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EstimatedTimeCost = params.get("EstimatedTimeCost")
        self.RequestId = params.get("RequestId")


class FaceAttributesInfo(AbstractModel):
    """人臉屬性訊息，包含性别( gender )、年齡( age )、表情( expression )、
    魅力( beauty )、眼鏡( glass )、口罩（mask）、頭發（hair）和姿态 (pitch，roll，yaw )。只有當 NeedFaceAttributes 設爲 1 時才返回有效訊息，最多返回面積最大的 5 張人臉屬性訊息，超過 5 張人臉（第 6 張及以後的人臉）的 FaceAttributesInfo 不具備參考意義。

    """

    def __init__(self):
        """
        :param Gender: 性别[0~49]爲女性，[50，100]爲男性，越接近0和100表示置信度越高。NeedFaceAttributes 不爲 1 或檢測超過 5 張人臉時，此參數仍返回，但不具備參考意義。
        :type Gender: int
        :param Age: 年齡 [0~100]。NeedFaceAttributes 不爲1 或檢測超過 5 張人臉時，此參數仍返回，但不具備參考意義。
        :type Age: int
        :param Expression: 微笑[0(normal，正常)~50(smile，微笑)~100(laugh，大笑)]。NeedFaceAttributes 不爲1 或檢測超過 5 張人臉時，此參數仍返回，但不具備參考意義。
        :type Expression: int
        :param Glass: 是否有眼鏡 [true,false]。NeedFaceAttributes 不爲1 或檢測超過 5 張人臉時，此參數仍返回，但不具備參考意義。
        :type Glass: bool
        :param Pitch: 上下偏移[-30,30]，單位角度。NeedFaceAttributes 不爲1 或檢測超過 5 張人臉時，此參數仍返回，但不具備參考意義。 
建議：人臉入庫選擇[-10,10]的圖片。
        :type Pitch: int
        :param Yaw: 左右偏移[-30,30]，單位角度。 NeedFaceAttributes 不爲1 或檢測超過 5 張人臉時，此參數仍返回，但不具備參考意義。 
建議：人臉入庫選擇[-10,10]的圖片。
        :type Yaw: int
        :param Roll: 平面旋轉[-180,180]，單位角度。 NeedFaceAttributes 不爲1 或檢測超過 5 張人臉時，此參數仍返回，但不具備參考意義。  
建議：人臉入庫選擇[-20,20]的圖片。
        :type Roll: int
        :param Beauty: 魅力[0~100]。NeedFaceAttributes 不爲1 或檢測超過 5 張人臉時，此參數仍返回，但不具備參考意義。
        :type Beauty: int
        :param Hat: 是否有帽子 [true,false]。NeedFaceAttributes 不爲1 或檢測超過 5 張人臉時，此參數仍返回，但不具備參考意義。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Hat: bool
        :param Mask: 是否有口罩 [true,false]。NeedFaceAttributes 不爲1 或檢測超過 5 張人臉時，此參數仍返回，但不具備參考意義。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Mask: bool
        :param Hair: 頭發訊息，包含頭發長度（length）、有無劉海（bang）、頭發顔色（color）。NeedFaceAttributes 不爲1 或檢測超過 5 張人臉時，此參數仍返回，但不具備參考意義。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Hair: :class:`taifucloudcloud.iai.v20180301.models.FaceHairAttributesInfo`
        :param EyeOpen: 雙眼是否睜開 [true,false]。只要有超過一只眼睛閉眼，就返回false。 NeedFaceAttributes 不爲1 或檢測超過 5 張人臉時，此參數仍返回，但不具備參考意義。
注意：此欄位可能返回 null，表示取不到有效值。
        :type EyeOpen: bool
        """
        self.Gender = None
        self.Age = None
        self.Expression = None
        self.Glass = None
        self.Pitch = None
        self.Yaw = None
        self.Roll = None
        self.Beauty = None
        self.Hat = None
        self.Mask = None
        self.Hair = None
        self.EyeOpen = None


    def _deserialize(self, params):
        self.Gender = params.get("Gender")
        self.Age = params.get("Age")
        self.Expression = params.get("Expression")
        self.Glass = params.get("Glass")
        self.Pitch = params.get("Pitch")
        self.Yaw = params.get("Yaw")
        self.Roll = params.get("Roll")
        self.Beauty = params.get("Beauty")
        self.Hat = params.get("Hat")
        self.Mask = params.get("Mask")
        if params.get("Hair") is not None:
            self.Hair = FaceHairAttributesInfo()
            self.Hair._deserialize(params.get("Hair"))
        self.EyeOpen = params.get("EyeOpen")


class FaceHairAttributesInfo(AbstractModel):
    """人臉屬性中的發型訊息。

    """

    def __init__(self):
        """
        :param Length: 0：光頭，1：短發，2：中發，3：長發，4：綁發
注意：此欄位可能返回 null，表示取不到有效值。
        :type Length: int
        :param Bang: 0：有劉海，1：無劉海
注意：此欄位可能返回 null，表示取不到有效值。
        :type Bang: int
        :param Color: 0：黑色，1：金色，2：棕色，3：灰白色
注意：此欄位可能返回 null，表示取不到有效值。
        :type Color: int
        """
        self.Length = None
        self.Bang = None
        self.Color = None


    def _deserialize(self, params):
        self.Length = params.get("Length")
        self.Bang = params.get("Bang")
        self.Color = params.get("Color")


class FaceInfo(AbstractModel):
    """人臉訊息清單。

    """

    def __init__(self):
        """
        :param X: 人臉框左上角橫坐標。
人臉框包含人臉五官位置並在此基礎上進行一定的擴展，若人臉框超出圖片範圍，會導緻坐標負值。 
若需截取完整人臉，可以在完整分completess滿足需求的情況下，将負值坐標取0。
        :type X: int
        :param Y: 人臉框左上角縱坐標。 
人臉框包含人臉五官位置並在此基礎上進行一定的擴展，若人臉框超出圖片範圍，會導緻坐標負值。 
若需截取完整人臉，可以在完整分completess滿足需求的情況下，将負值坐標取0。
        :type Y: int
        :param Width: 人臉框寬度。
        :type Width: int
        :param Height: 人臉框高度。
        :type Height: int
        :param FaceAttributesInfo: 人臉屬性訊息，包含性别( gender )、年齡( age )、表情( expression )、 
魅力( beauty )、眼鏡( glass )、口罩（mask）、頭發（hair）和姿态 (pitch，roll，yaw )。只有當 NeedFaceAttributes 設爲 1 時才返回有效訊息。
        :type FaceAttributesInfo: :class:`taifucloudcloud.iai.v20180301.models.FaceAttributesInfo`
        :param FaceQualityInfo: 人臉質量訊息，包含質量分（score）、模糊分（sharpness）、光照分（brightness）、遮擋分（completeness）。只有當NeedFaceDetection設爲1時才返回有效訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FaceQualityInfo: :class:`taifucloudcloud.iai.v20180301.models.FaceQualityInfo`
        """
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None
        self.FaceAttributesInfo = None
        self.FaceQualityInfo = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        if params.get("FaceAttributesInfo") is not None:
            self.FaceAttributesInfo = FaceAttributesInfo()
            self.FaceAttributesInfo._deserialize(params.get("FaceAttributesInfo"))
        if params.get("FaceQualityInfo") is not None:
            self.FaceQualityInfo = FaceQualityInfo()
            self.FaceQualityInfo._deserialize(params.get("FaceQualityInfo"))


class FaceQualityCompleteness(AbstractModel):
    """五官遮擋分，評價眉毛（Eyebrow）、眼睛（Eye）、鼻子（Nose）、臉頰（Cheek）、嘴巴（Mouth）、下巴（Chin）的被遮擋程度。

    """

    def __init__(self):
        """
        :param Eyebrow: 眉毛的遮擋分數[0,100]，分數越高遮擋越少。 
參考範圍：[0,80]表示發生遮擋。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Eyebrow: int
        :param Eye: 眼睛的遮擋分數[0,100],分數越高遮擋越少。 
參考範圍：[0,80]表示發生遮擋。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Eye: int
        :param Nose: 鼻子的遮擋分數[0,100],分數越高遮擋越少。 
參考範圍：[0,60]表示發生遮擋。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Nose: int
        :param Cheek: 臉頰的遮擋分數[0,100],分數越高遮擋越少。 
參考範圍：[0,70]表示發生遮擋。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Cheek: int
        :param Mouth: 嘴巴的遮擋分數[0,100],分數越高遮擋越少。 
參考範圍：[0,50]表示發生遮擋。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Mouth: int
        :param Chin: 下巴的遮擋分數[0,100],分數越高遮擋越少。 
參考範圍：[0,70]表示發生遮擋。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Chin: int
        """
        self.Eyebrow = None
        self.Eye = None
        self.Nose = None
        self.Cheek = None
        self.Mouth = None
        self.Chin = None


    def _deserialize(self, params):
        self.Eyebrow = params.get("Eyebrow")
        self.Eye = params.get("Eye")
        self.Nose = params.get("Nose")
        self.Cheek = params.get("Cheek")
        self.Mouth = params.get("Mouth")
        self.Chin = params.get("Chin")


class FaceQualityInfo(AbstractModel):
    """人臉質量訊息，包含質量分（score）、模糊分（sharpness）、光照分（brightness）、遮擋分（completeness）。只有當NeedFaceDetection設爲1時才返回有效訊息。

    """

    def __init__(self):
        """
        :param Score: 質量分: [0,100]，綜合評價圖像質量是否适合人臉識别，分數越高質量越好。 
正常情況，只需要使用Score作爲質量分總體的判斷標準即可。Sharpness、Brightness、Completeness等細項分僅供參考。
參考範圍：[0,40]較差，[40,60] 一般，[60,80]較好，[80,100]很好。 
建議：人臉入庫選取70以上的圖片。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Score: int
        :param Sharpness: 清晰分：[0,100]，評價圖片清晰程度，分數越高越清晰。 
參考範圍：[0,40]特别模糊，[40,60]模糊，[60,80]一般，[80,100]清晰。 
建議：人臉入庫選取80以上的圖片。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Sharpness: int
        :param Brightness: 光照分：[0,100]，評價圖片光照程度，分數越高越亮。 
參考範圍： [0,30]偏暗，[30,70]光照正常，[70,100]偏亮。 
建議：人臉入庫選取[30,70]的圖片。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Brightness: int
        :param Completeness: 五官遮擋分，評價眉毛（Eyebrow）、眼睛（Eye）、鼻子（Nose）、臉頰（Cheek）、嘴巴（Mouth）、下巴（Chin）的被遮擋程度。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Completeness: :class:`taifucloudcloud.iai.v20180301.models.FaceQualityCompleteness`
        """
        self.Score = None
        self.Sharpness = None
        self.Brightness = None
        self.Completeness = None


    def _deserialize(self, params):
        self.Score = params.get("Score")
        self.Sharpness = params.get("Sharpness")
        self.Brightness = params.get("Brightness")
        if params.get("Completeness") is not None:
            self.Completeness = FaceQualityCompleteness()
            self.Completeness._deserialize(params.get("Completeness"))


class FaceRect(AbstractModel):
    """檢測出的人臉框的位置

    """

    def __init__(self):
        """
        :param X: 人臉框左上角橫坐標。 
人臉框包含人臉五官位置並在此基礎上進行一定的擴展，若人臉框超出圖片範圍，會導緻坐標負值。 
若需截取完整人臉，可以在完整分completess滿足需求的情況下，将負值坐標取0。
        :type X: int
        :param Y: 人臉框左上角縱坐標。 
人臉框包含人臉五官位置並在此基礎上進行一定的擴展，若人臉框超出圖片範圍，會導緻坐標負值。 
若需截取完整人臉，可以在完整分completess滿足需求的情況下，将負值坐標取0。
        :type Y: int
        :param Width: 人臉寬度
        :type Width: int
        :param Height: 人臉高度
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


class FaceShape(AbstractModel):
    """五官定位（人臉關鍵點）具體訊息。

    """

    def __init__(self):
        """
        :param FaceProfile: 描述臉型輪廓的 21 點。
        :type FaceProfile: list of Point
        :param LeftEye: 描述左側眼睛輪廓的 8 點。
        :type LeftEye: list of Point
        :param RightEye: 描述右側眼睛輪廓的 8 點。
        :type RightEye: list of Point
        :param LeftEyeBrow: 描述左側眉毛輪廓的 8 點。
        :type LeftEyeBrow: list of Point
        :param RightEyeBrow: 描述右側眉毛輪廓的 8 點。
        :type RightEyeBrow: list of Point
        :param Mouth: 描述嘴巴輪廓的 22 點。
        :type Mouth: list of Point
        :param Nose: 描述鼻子輪廓的 13 點。
        :type Nose: list of Point
        :param LeftPupil: 左瞳孔輪廓的 1 個點。
        :type LeftPupil: list of Point
        :param RightPupil: 右瞳孔輪廓的 1 個點。
        :type RightPupil: list of Point
        """
        self.FaceProfile = None
        self.LeftEye = None
        self.RightEye = None
        self.LeftEyeBrow = None
        self.RightEyeBrow = None
        self.Mouth = None
        self.Nose = None
        self.LeftPupil = None
        self.RightPupil = None


    def _deserialize(self, params):
        if params.get("FaceProfile") is not None:
            self.FaceProfile = []
            for item in params.get("FaceProfile"):
                obj = Point()
                obj._deserialize(item)
                self.FaceProfile.append(obj)
        if params.get("LeftEye") is not None:
            self.LeftEye = []
            for item in params.get("LeftEye"):
                obj = Point()
                obj._deserialize(item)
                self.LeftEye.append(obj)
        if params.get("RightEye") is not None:
            self.RightEye = []
            for item in params.get("RightEye"):
                obj = Point()
                obj._deserialize(item)
                self.RightEye.append(obj)
        if params.get("LeftEyeBrow") is not None:
            self.LeftEyeBrow = []
            for item in params.get("LeftEyeBrow"):
                obj = Point()
                obj._deserialize(item)
                self.LeftEyeBrow.append(obj)
        if params.get("RightEyeBrow") is not None:
            self.RightEyeBrow = []
            for item in params.get("RightEyeBrow"):
                obj = Point()
                obj._deserialize(item)
                self.RightEyeBrow.append(obj)
        if params.get("Mouth") is not None:
            self.Mouth = []
            for item in params.get("Mouth"):
                obj = Point()
                obj._deserialize(item)
                self.Mouth.append(obj)
        if params.get("Nose") is not None:
            self.Nose = []
            for item in params.get("Nose"):
                obj = Point()
                obj._deserialize(item)
                self.Nose.append(obj)
        if params.get("LeftPupil") is not None:
            self.LeftPupil = []
            for item in params.get("LeftPupil"):
                obj = Point()
                obj._deserialize(item)
                self.LeftPupil.append(obj)
        if params.get("RightPupil") is not None:
            self.RightPupil = []
            for item in params.get("RightPupil"):
                obj = Point()
                obj._deserialize(item)
                self.RightPupil.append(obj)


class GetCheckSimilarPersonJobIdListRequest(AbstractModel):
    """GetCheckSimilarPersonJobIdList請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 起始序號，預設值爲0。
        :type Offset: int
        :param Limit: 返回數量，預設值爲10，最大值爲1000。
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetCheckSimilarPersonJobIdListResponse(AbstractModel):
    """GetCheckSimilarPersonJobIdList返回參數結構體

    """

    def __init__(self):
        """
        :param JobIdInfos: 人員查重任務訊息清單。
        :type JobIdInfos: list of JobIdInfo
        :param JobIdNum: 查重任務總數量。
        :type JobIdNum: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.JobIdInfos = None
        self.JobIdNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("JobIdInfos") is not None:
            self.JobIdInfos = []
            for item in params.get("JobIdInfos"):
                obj = JobIdInfo()
                obj._deserialize(item)
                self.JobIdInfos.append(obj)
        self.JobIdNum = params.get("JobIdNum")
        self.RequestId = params.get("RequestId")


class GetGroupInfoRequest(AbstractModel):
    """GetGroupInfo請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 人員庫 ID。
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class GetGroupInfoResponse(AbstractModel):
    """GetGroupInfo返回參數結構體

    """

    def __init__(self):
        """
        :param GroupName: 人員庫名稱
        :type GroupName: str
        :param GroupId: 人員庫ID
        :type GroupId: str
        :param GroupExDescriptions: 人員庫自定義描述欄位
        :type GroupExDescriptions: list of str
        :param Tag: 人員庫訊息備注
        :type Tag: str
        :param FaceModelVersion: 人臉識别所用的算法模型版本。
        :type FaceModelVersion: str
        :param CreationTimestamp: Group的創建時間和日期 CreationTimestamp。CreationTimestamp 的值是自 Unix 紀元時間到Group創建時間的毫秒數。
        :type CreationTimestamp: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.GroupName = None
        self.GroupId = None
        self.GroupExDescriptions = None
        self.Tag = None
        self.FaceModelVersion = None
        self.CreationTimestamp = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupId = params.get("GroupId")
        self.GroupExDescriptions = params.get("GroupExDescriptions")
        self.Tag = params.get("Tag")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.CreationTimestamp = params.get("CreationTimestamp")
        self.RequestId = params.get("RequestId")


class GetGroupListRequest(AbstractModel):
    """GetGroupList請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 起始序號，預設值爲0
        :type Offset: int
        :param Limit: 返回數量，預設值爲10，最大值爲1000
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetGroupListResponse(AbstractModel):
    """GetGroupList返回參數結構體

    """

    def __init__(self):
        """
        :param GroupInfos: 返回的人員庫訊息
        :type GroupInfos: list of GroupInfo
        :param GroupNum: 人員庫總數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupNum: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.GroupInfos = None
        self.GroupNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GroupInfos") is not None:
            self.GroupInfos = []
            for item in params.get("GroupInfos"):
                obj = GroupInfo()
                obj._deserialize(item)
                self.GroupInfos.append(obj)
        self.GroupNum = params.get("GroupNum")
        self.RequestId = params.get("RequestId")


class GetPersonBaseInfoRequest(AbstractModel):
    """GetPersonBaseInfo請求參數結構體

    """

    def __init__(self):
        """
        :param PersonId: 人員ID
        :type PersonId: str
        """
        self.PersonId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")


class GetPersonBaseInfoResponse(AbstractModel):
    """GetPersonBaseInfo返回參數結構體

    """

    def __init__(self):
        """
        :param PersonName: 人員名稱
        :type PersonName: str
        :param Gender: 人員性别
        :type Gender: int
        :param FaceIds: 包含的人臉 ID 清單
        :type FaceIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PersonName = None
        self.Gender = None
        self.FaceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PersonName = params.get("PersonName")
        self.Gender = params.get("Gender")
        self.FaceIds = params.get("FaceIds")
        self.RequestId = params.get("RequestId")


class GetPersonGroupInfoRequest(AbstractModel):
    """GetPersonGroupInfo請求參數結構體

    """

    def __init__(self):
        """
        :param PersonId: 人員ID
        :type PersonId: str
        :param Offset: 起始序號，預設值爲0
        :type Offset: int
        :param Limit: 返回數量，預設值爲10，最大值爲100
        :type Limit: int
        """
        self.PersonId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetPersonGroupInfoResponse(AbstractModel):
    """GetPersonGroupInfo返回參數結構體

    """

    def __init__(self):
        """
        :param PersonGroupInfos: 包含此人員的人員庫及描述欄位内容清單
        :type PersonGroupInfos: list of PersonGroupInfo
        :param GroupNum: 人員庫總數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupNum: int
        :param FaceModelVersion: 人臉識别服務所用的算法模型版本。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FaceModelVersion: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PersonGroupInfos = None
        self.GroupNum = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PersonGroupInfos") is not None:
            self.PersonGroupInfos = []
            for item in params.get("PersonGroupInfos"):
                obj = PersonGroupInfo()
                obj._deserialize(item)
                self.PersonGroupInfos.append(obj)
        self.GroupNum = params.get("GroupNum")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class GetPersonListNumRequest(AbstractModel):
    """GetPersonListNum請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 人員庫ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class GetPersonListNumResponse(AbstractModel):
    """GetPersonListNum返回參數結構體

    """

    def __init__(self):
        """
        :param PersonNum: 人員數量
        :type PersonNum: int
        :param FaceNum: 人臉數量
        :type FaceNum: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PersonNum = None
        self.FaceNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PersonNum = params.get("PersonNum")
        self.FaceNum = params.get("FaceNum")
        self.RequestId = params.get("RequestId")


class GetPersonListRequest(AbstractModel):
    """GetPersonList請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 人員庫ID
        :type GroupId: str
        :param Offset: 起始序號，預設值爲0
        :type Offset: int
        :param Limit: 返回數量，預設值爲10，最大值爲1000
        :type Limit: int
        """
        self.GroupId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetPersonListResponse(AbstractModel):
    """GetPersonList返回參數結構體

    """

    def __init__(self):
        """
        :param PersonInfos: 返回的人員訊息
        :type PersonInfos: list of PersonInfo
        :param PersonNum: 該人員庫的人員數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type PersonNum: int
        :param FaceNum: 該人員庫的人臉數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type FaceNum: int
        :param FaceModelVersion: 人臉識别所用的算法模型版本。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FaceModelVersion: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PersonInfos = None
        self.PersonNum = None
        self.FaceNum = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PersonInfos") is not None:
            self.PersonInfos = []
            for item in params.get("PersonInfos"):
                obj = PersonInfo()
                obj._deserialize(item)
                self.PersonInfos.append(obj)
        self.PersonNum = params.get("PersonNum")
        self.FaceNum = params.get("FaceNum")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class GetSimilarPersonResultRequest(AbstractModel):
    """GetSimilarPersonResult請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 查重任務ID，用於查詢、獲取查重的進度和結果。
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class GetSimilarPersonResultResponse(AbstractModel):
    """GetSimilarPersonResult返回參數結構體

    """

    def __init__(self):
        """
        :param Progress: 查重任務完成進度。取值[0.0，100.0]。當且僅當值爲100時，SimilarPersons才有意義。
        :type Progress: float
        :param SimilarPersonsUrl: 疑似同一人的人員訊息文件臨時下載連結， 有效時間爲5分鍾，結果文件實際保存90天。
文件内容由 SimilarPerson 的數組組成。
        :type SimilarPersonsUrl: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Progress = None
        self.SimilarPersonsUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Progress = params.get("Progress")
        self.SimilarPersonsUrl = params.get("SimilarPersonsUrl")
        self.RequestId = params.get("RequestId")


class GroupCandidate(AbstractModel):
    """分組識别結果Item

    """

    def __init__(self):
        """
        :param GroupId: 人員庫ID 。
        :type GroupId: str
        :param Candidates: 識别出的最相似候選人。
        :type Candidates: list of Candidate
        """
        self.GroupId = None
        self.Candidates = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        if params.get("Candidates") is not None:
            self.Candidates = []
            for item in params.get("Candidates"):
                obj = Candidate()
                obj._deserialize(item)
                self.Candidates.append(obj)


class GroupExDescriptionInfo(AbstractModel):
    """需要修改的人員庫自定義描述欄位key-value

    """

    def __init__(self):
        """
        :param GroupExDescriptionIndex: 人員庫自定義描述欄位Index，從0開始
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupExDescriptionIndex: int
        :param GroupExDescription: 需要更新的人員庫自定義描述欄位内容
        :type GroupExDescription: str
        """
        self.GroupExDescriptionIndex = None
        self.GroupExDescription = None


    def _deserialize(self, params):
        self.GroupExDescriptionIndex = params.get("GroupExDescriptionIndex")
        self.GroupExDescription = params.get("GroupExDescription")


class GroupInfo(AbstractModel):
    """返回的人員庫訊息

    """

    def __init__(self):
        """
        :param GroupName: 人員庫名稱
        :type GroupName: str
        :param GroupId: 人員庫ID
        :type GroupId: str
        :param GroupExDescriptions: 人員庫自定義描述欄位
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupExDescriptions: list of str
        :param Tag: 人員庫訊息備注
注意：此欄位可能返回 null，表示取不到有效值。
        :type Tag: str
        :param FaceModelVersion: 人臉識别所用的算法模型版本。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FaceModelVersion: str
        :param CreationTimestamp: Group的創建時間和日期 CreationTimestamp。CreationTimestamp 的值是自 Unix 紀元時間到Group創建時間的毫秒數。 
Unix 紀元時間是 1970 年 1 月 1 日星期四，協調世界時 (UTC) 00:00:00。有關更多訊息，請參閱 Unix 時間。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreationTimestamp: int
        """
        self.GroupName = None
        self.GroupId = None
        self.GroupExDescriptions = None
        self.Tag = None
        self.FaceModelVersion = None
        self.CreationTimestamp = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupId = params.get("GroupId")
        self.GroupExDescriptions = params.get("GroupExDescriptions")
        self.Tag = params.get("Tag")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.CreationTimestamp = params.get("CreationTimestamp")


class JobIdInfo(AbstractModel):
    """查重任務訊息

    """

    def __init__(self):
        """
        :param JobId: 查重任務ID，用於查詢、獲取查重的進度和結果。
        :type JobId: str
        :param StartTime: 查重起始時間。 
StartTime的值是自 Unix 紀元時間到Group創建時間的毫秒數。 
Unix 紀元時間是 1970 年 1 月 1 日星期四，協調世界時 (UTC) 00:00:00。 
有關更多訊息，請參閱 Unix 時間。
        :type StartTime: int
        :param JobStatus: 查重任務是否已完成。0: 成功 1: 未完成 2: 失敗
        :type JobStatus: int
        """
        self.JobId = None
        self.StartTime = None
        self.JobStatus = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.StartTime = params.get("StartTime")
        self.JobStatus = params.get("JobStatus")


class ModifyGroupRequest(AbstractModel):
    """ModifyGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 人員庫ID
        :type GroupId: str
        :param GroupName: 人員庫名稱
        :type GroupName: str
        :param GroupExDescriptionInfos: 需要修改的人員庫自定義描述欄位，key-value
        :type GroupExDescriptionInfos: list of GroupExDescriptionInfo
        :param Tag: 人員庫訊息備注
        :type Tag: str
        """
        self.GroupId = None
        self.GroupName = None
        self.GroupExDescriptionInfos = None
        self.Tag = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        if params.get("GroupExDescriptionInfos") is not None:
            self.GroupExDescriptionInfos = []
            for item in params.get("GroupExDescriptionInfos"):
                obj = GroupExDescriptionInfo()
                obj._deserialize(item)
                self.GroupExDescriptionInfos.append(obj)
        self.Tag = params.get("Tag")


class ModifyGroupResponse(AbstractModel):
    """ModifyGroup返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPersonBaseInfoRequest(AbstractModel):
    """ModifyPersonBaseInfo請求參數結構體

    """

    def __init__(self):
        """
        :param PersonId: 人員ID
        :type PersonId: str
        :param PersonName: 需要修改的人員名稱
        :type PersonName: str
        :param Gender: 需要修改的人員性别
        :type Gender: int
        """
        self.PersonId = None
        self.PersonName = None
        self.Gender = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.PersonName = params.get("PersonName")
        self.Gender = params.get("Gender")


class ModifyPersonBaseInfoResponse(AbstractModel):
    """ModifyPersonBaseInfo返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPersonGroupInfoRequest(AbstractModel):
    """ModifyPersonGroupInfo請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 人員庫ID
        :type GroupId: str
        :param PersonId: 人員ID
        :type PersonId: str
        :param PersonExDescriptionInfos: 需要修改的人員描述欄位内容，key-value
        :type PersonExDescriptionInfos: list of PersonExDescriptionInfo
        """
        self.GroupId = None
        self.PersonId = None
        self.PersonExDescriptionInfos = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.PersonId = params.get("PersonId")
        if params.get("PersonExDescriptionInfos") is not None:
            self.PersonExDescriptionInfos = []
            for item in params.get("PersonExDescriptionInfos"):
                obj = PersonExDescriptionInfo()
                obj._deserialize(item)
                self.PersonExDescriptionInfos.append(obj)


class ModifyPersonGroupInfoResponse(AbstractModel):
    """ModifyPersonGroupInfo返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PersonExDescriptionInfo(AbstractModel):
    """需要修改的人員描述欄位内容，key-value

    """

    def __init__(self):
        """
        :param PersonExDescriptionIndex: 人員描述欄位Index，從0開始
注意：此欄位可能返回 null，表示取不到有效值。
        :type PersonExDescriptionIndex: int
        :param PersonExDescription: 需要更新的人員描述欄位内容
        :type PersonExDescription: str
        """
        self.PersonExDescriptionIndex = None
        self.PersonExDescription = None


    def _deserialize(self, params):
        self.PersonExDescriptionIndex = params.get("PersonExDescriptionIndex")
        self.PersonExDescription = params.get("PersonExDescription")


class PersonGroupInfo(AbstractModel):
    """包含此人員的人員庫及描述欄位内容清單

    """

    def __init__(self):
        """
        :param GroupId: 包含此人員的人員庫ID
        :type GroupId: str
        :param PersonExDescriptions: 人員描述欄位内容
        :type PersonExDescriptions: list of str
        """
        self.GroupId = None
        self.PersonExDescriptions = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.PersonExDescriptions = params.get("PersonExDescriptions")


class PersonInfo(AbstractModel):
    """返回的人員訊息

    """

    def __init__(self):
        """
        :param PersonName: 人員名稱
        :type PersonName: str
        :param PersonId: 人員Id
        :type PersonId: str
        :param Gender: 人員性别
        :type Gender: int
        :param PersonExDescriptions: 人員描述欄位内容
        :type PersonExDescriptions: list of str
        :param FaceIds: 包含的人臉照片清單
        :type FaceIds: list of str
        :param CreationTimestamp: 人員的創建時間和日期 CreationTimestamp。CreationTimestamp 的值是自 Unix 紀元時間到Group創建時間的毫秒數。 
Unix 紀元時間是 1970 年 1 月 1 日星期四，協調世界時 (UTC) 00:00:00。有關更多訊息，請參閱 Unix 時間。
        :type CreationTimestamp: int
        """
        self.PersonName = None
        self.PersonId = None
        self.Gender = None
        self.PersonExDescriptions = None
        self.FaceIds = None
        self.CreationTimestamp = None


    def _deserialize(self, params):
        self.PersonName = params.get("PersonName")
        self.PersonId = params.get("PersonId")
        self.Gender = params.get("Gender")
        self.PersonExDescriptions = params.get("PersonExDescriptions")
        self.FaceIds = params.get("FaceIds")
        self.CreationTimestamp = params.get("CreationTimestamp")


class Point(AbstractModel):
    """坐標

    """

    def __init__(self):
        """
        :param X: x坐標
        :type X: int
        :param Y: Y坐標
        :type Y: int
        """
        self.X = None
        self.Y = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")


class Result(AbstractModel):
    """人臉的識别結果

    """

    def __init__(self):
        """
        :param Candidates: 識别出的最相似候選人
        :type Candidates: list of Candidate
        :param FaceRect: 檢測出的人臉框位置
        :type FaceRect: :class:`taifucloudcloud.iai.v20180301.models.FaceRect`
        :param RetCode: 檢測出的人臉圖片狀态返回碼。0 表示正常。 
-1601代表不符合圖片質量控制要求，此時Candidate内容爲空。
        :type RetCode: int
        """
        self.Candidates = None
        self.FaceRect = None
        self.RetCode = None


    def _deserialize(self, params):
        if params.get("Candidates") is not None:
            self.Candidates = []
            for item in params.get("Candidates"):
                obj = Candidate()
                obj._deserialize(item)
                self.Candidates.append(obj)
        if params.get("FaceRect") is not None:
            self.FaceRect = FaceRect()
            self.FaceRect._deserialize(params.get("FaceRect"))
        self.RetCode = params.get("RetCode")


class ResultsReturnsByGroup(AbstractModel):
    """識别結果。

    """

    def __init__(self):
        """
        :param FaceRect: 檢測出的人臉框位置。
        :type FaceRect: :class:`taifucloudcloud.iai.v20180301.models.FaceRect`
        :param GroupCandidates: 識别結果。
        :type GroupCandidates: list of GroupCandidate
        :param RetCode: 檢測出的人臉圖片狀态返回碼。0 表示正常。 
-1601代表不符合圖片質量控制要求，此時Candidate内容爲空。
        :type RetCode: int
        """
        self.FaceRect = None
        self.GroupCandidates = None
        self.RetCode = None


    def _deserialize(self, params):
        if params.get("FaceRect") is not None:
            self.FaceRect = FaceRect()
            self.FaceRect._deserialize(params.get("FaceRect"))
        if params.get("GroupCandidates") is not None:
            self.GroupCandidates = []
            for item in params.get("GroupCandidates"):
                obj = GroupCandidate()
                obj._deserialize(item)
                self.GroupCandidates.append(obj)
        self.RetCode = params.get("RetCode")


class SearchFacesRequest(AbstractModel):
    """SearchFaces請求參數結構體

    """

    def __init__(self):
        """
        :param GroupIds: 希望搜索的人員庫清單，上限100個。
        :type GroupIds: list of str
        :param Image: 圖片 base64 數據，base64 編碼後大小不可超過5M。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Image: str
        :param Url: 圖片的 Url 。對應圖片 base64 編碼後大小不可超過5M。
Url、Image必須提供一個，如果都提供，只使用 Url。  
圖片儲存於Top Cloud 的Url可保障更高下載速度和穩定性，建議圖片儲存於Top Cloud 。 
非Top Cloud 儲存的Url速度和穩定性可能受一定影響。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Url: str
        :param MaxFaceNum: 最多識别的人臉數目。預設值爲1（僅檢測圖片中面積最大的那張人臉），最大值爲10。 
MaxFaceNum用於，當輸入的待識别圖片包含多張人臉時，設定要搜索的人臉的數量。 
例：輸入的Image或Url中的圖片包含多張人臉，設MaxFaceNum=5，則會識别圖片中面積最大的5張人臉。
        :type MaxFaceNum: int
        :param MinFaceSize: 人臉長和寬的最小尺寸，單位爲像素。預設爲34。低於34的人臉圖片無法被識别。建議設置爲80。
        :type MinFaceSize: int
        :param MaxPersonNum: 單張被識别的人臉返回的最相似人員數量。預設值爲5，最大值爲100。 
例，設MaxFaceNum爲1，MaxPersonNum爲8，則返回Top8相似的人員訊息。
值越大，需要處理的時間越長。建議不要超過10。
        :type MaxPersonNum: int
        :param NeedPersonInfo: 是否返回人員具體訊息。0 爲關閉，1 爲開啓。預設爲 0。其他非0非1值預設爲0
        :type NeedPersonInfo: int
        :param QualityControl: 圖片質量控制。 
0: 不進行控制； 
1:較低的質量要求，圖像存在非常模糊，眼睛鼻子嘴巴遮擋至少其中一種或多種的情況； 
2: 一般的質量要求，圖像存在偏亮，偏暗，模糊或一般模糊，眉毛遮擋，臉頰遮擋，下巴遮擋，至少其中三種的情況； 
3: 較高的質量要求，圖像存在偏亮，偏暗，一般模糊，眉毛遮擋，臉頰遮擋，下巴遮擋，其中一到兩種的情況； 
4: 很高的質量要求，各個維度均爲最好或最多在某一維度上存在輕微問題； 
預設 0。 
若圖片質量不滿足要求，則返回結果中會提示圖片質量檢測不符要求。
        :type QualityControl: int
        :param FaceMatchThreshold: 出參Score中，只有超過FaceMatchThreshold值的結果才會返回。預設爲0。
        :type FaceMatchThreshold: float
        :param NeedRotateDetection: 是否開啓圖片旋轉識别支援。0爲不開啓，1爲開啓。預設爲0。本參數的作用爲，當圖片中的人臉被旋轉且圖片沒有exif訊息時，如果不開啓圖片旋轉識别支援則無法正确檢測、識别圖片中的人臉。若您确認圖片包含exif訊息或者您确認輸入圖中人臉不會出現被旋轉情況，請不要開啓本參數。開啓後，整體耗時将可能增加數百毫秒。
        :type NeedRotateDetection: int
        """
        self.GroupIds = None
        self.Image = None
        self.Url = None
        self.MaxFaceNum = None
        self.MinFaceSize = None
        self.MaxPersonNum = None
        self.NeedPersonInfo = None
        self.QualityControl = None
        self.FaceMatchThreshold = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.GroupIds = params.get("GroupIds")
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.MaxFaceNum = params.get("MaxFaceNum")
        self.MinFaceSize = params.get("MinFaceSize")
        self.MaxPersonNum = params.get("MaxPersonNum")
        self.NeedPersonInfo = params.get("NeedPersonInfo")
        self.QualityControl = params.get("QualityControl")
        self.FaceMatchThreshold = params.get("FaceMatchThreshold")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class SearchFacesResponse(AbstractModel):
    """SearchFaces返回參數結構體

    """

    def __init__(self):
        """
        :param Results: 識别結果。
        :type Results: list of Result
        :param FaceNum: 搜索的人員庫中包含的人臉數。
        :type FaceNum: int
        :param FaceModelVersion: 人臉識别所用的算法模型版本。
        :type FaceModelVersion: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Results = None
        self.FaceNum = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = Result()
                obj._deserialize(item)
                self.Results.append(obj)
        self.FaceNum = params.get("FaceNum")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class SearchFacesReturnsByGroupRequest(AbstractModel):
    """SearchFacesReturnsByGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupIds: 希望搜索的人員庫清單，上限60個。
        :type GroupIds: list of str
        :param Image: 圖片 base64 數據，base64 編碼後大小不可超過5M。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Image: str
        :param Url: 圖片的 Url 。對應圖片 base64 編碼後大小不可超過5M。
Url、Image必須提供一個，如果都提供，只使用 Url。
圖片儲存於Top Cloud 的Url可保障更高下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的Url速度和穩定性可能受一定影響。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Url: str
        :param MaxFaceNum: 最多識别的人臉數目。預設值爲1（僅檢測圖片中面積最大的那張人臉），最大值爲10。
MaxFaceNum用於，當輸入的待識别圖片包含多張人臉時，設定要搜索的人臉的數量。
例：輸入的Image或Url中的圖片包含多張人臉，設MaxFaceNum=5，則會識别圖片中面積最大的5張人臉。
        :type MaxFaceNum: int
        :param MinFaceSize: 人臉長和寬的最小尺寸，單位爲像素。預設爲34。低於34将影響搜索精度。建議設置爲80。
        :type MinFaceSize: int
        :param MaxPersonNumPerGroup: 被檢測到的人臉，對應最多返回的最相似人員數目。預設值爲5，最大值爲10。  
例，設MaxFaceNum爲3，MaxPersonNum爲5，則最多可能返回3*5=15個人員。
        :type MaxPersonNumPerGroup: int
        :param NeedPersonInfo: 是否返回人員具體訊息。0 爲關閉，1 爲開啓。預設爲 0。其他非0非1值預設爲0
        :type NeedPersonInfo: int
        :param QualityControl: 圖片質量控制。 
0: 不進行控制； 
1:較低的質量要求，圖像存在非常模糊，眼睛鼻子嘴巴遮擋至少其中一種或多種的情況； 
2: 一般的質量要求，圖像存在偏亮，偏暗，模糊或一般模糊，眉毛遮擋，臉頰遮擋，下巴遮擋，至少其中三種的情況； 
3: 較高的質量要求，圖像存在偏亮，偏暗，一般模糊，眉毛遮擋，臉頰遮擋，下巴遮擋，其中一到兩種的情況； 
4: 很高的質量要求，各個維度均爲最好或最多在某一維度上存在輕微問題； 
預設 0。 
若圖片質量不滿足要求，則返回結果中會提示圖片質量檢測不符要求。
        :type QualityControl: int
        :param FaceMatchThreshold: 出參Score中，只有大於等於FaceMatchThreshold值的結果才會返回。
預設爲0。
取值範圍[0.0,100.0) 。
        :type FaceMatchThreshold: float
        :param NeedRotateDetection: 是否開啓圖片旋轉識别支援。0爲不開啓，1爲開啓。預設爲0。本參數的作用爲，當圖片中的人臉被旋轉且圖片沒有exif訊息時，如果不開啓圖片旋轉識别支援則無法正确檢測、識别圖片中的人臉。若您确認圖片包含exif訊息或者您确認輸入圖中人臉不會出現被旋轉情況，請不要開啓本參數。開啓後，整體耗時将可能增加數百毫秒。
        :type NeedRotateDetection: int
        """
        self.GroupIds = None
        self.Image = None
        self.Url = None
        self.MaxFaceNum = None
        self.MinFaceSize = None
        self.MaxPersonNumPerGroup = None
        self.NeedPersonInfo = None
        self.QualityControl = None
        self.FaceMatchThreshold = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.GroupIds = params.get("GroupIds")
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.MaxFaceNum = params.get("MaxFaceNum")
        self.MinFaceSize = params.get("MinFaceSize")
        self.MaxPersonNumPerGroup = params.get("MaxPersonNumPerGroup")
        self.NeedPersonInfo = params.get("NeedPersonInfo")
        self.QualityControl = params.get("QualityControl")
        self.FaceMatchThreshold = params.get("FaceMatchThreshold")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class SearchFacesReturnsByGroupResponse(AbstractModel):
    """SearchFacesReturnsByGroup返回參數結構體

    """

    def __init__(self):
        """
        :param FaceNum: 搜索的人員庫中包含的人臉數。
        :type FaceNum: int
        :param ResultsReturnsByGroup: 識别結果。
        :type ResultsReturnsByGroup: list of ResultsReturnsByGroup
        :param FaceModelVersion: 人臉識别所用的算法模型版本。
        :type FaceModelVersion: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FaceNum = None
        self.ResultsReturnsByGroup = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FaceNum = params.get("FaceNum")
        if params.get("ResultsReturnsByGroup") is not None:
            self.ResultsReturnsByGroup = []
            for item in params.get("ResultsReturnsByGroup"):
                obj = ResultsReturnsByGroup()
                obj._deserialize(item)
                self.ResultsReturnsByGroup.append(obj)
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class SearchPersonsRequest(AbstractModel):
    """SearchPersons請求參數結構體

    """

    def __init__(self):
        """
        :param GroupIds: 希望搜索的人員庫清單，上限100個。
        :type GroupIds: list of str
        :param Image: 圖片 base64 數據，base64 編碼後大小不可超過5M。
若圖片中包含多張人臉，只選取其中人臉面積最大的人臉。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Image: str
        :param Url: 圖片的 Url 。對應圖片 base64 編碼後大小不可超過5M。
Url、Image必須提供一個，如果都提供，只使用 Url。
圖片儲存於Top Cloud 的Url可保障更高下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的Url速度和穩定性可能受一定影響。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Url: str
        :param MaxFaceNum: 最多識别的人臉數目。預設值爲1（僅檢測圖片中面積最大的那張人臉），最大值爲10。
MaxFaceNum用於，當輸入的待識别圖片包含多張人臉時，設定要搜索的人臉的數量。
例：輸入的Image或Url中的圖片包含多張人臉，設MaxFaceNum=5，則會識别圖片中面積最大的5張人臉。
        :type MaxFaceNum: int
        :param MinFaceSize: 人臉長和寬的最小尺寸，單位爲像素。預設爲34。低於34将影響搜索精度。建議設置爲80。
        :type MinFaceSize: int
        :param MaxPersonNum: 單張被識别的人臉返回的最相似人員數量。預設值爲5，最大值爲100。
例，設MaxFaceNum爲1，MaxPersonNum爲8，則返回Top8相似的人員訊息。
值越大，需要處理的時間越長。建議不要超過10。
        :type MaxPersonNum: int
        :param QualityControl: 圖片質量控制。 
0: 不進行控制； 
1:較低的質量要求，圖像存在非常模糊，眼睛鼻子嘴巴遮擋至少其中一種或多種的情況； 
2: 一般的質量要求，圖像存在偏亮，偏暗，模糊或一般模糊，眉毛遮擋，臉頰遮擋，下巴遮擋，至少其中三種的情況； 
3: 較高的質量要求，圖像存在偏亮，偏暗，一般模糊，眉毛遮擋，臉頰遮擋，下巴遮擋，其中一到兩種的情況； 
4: 很高的質量要求，各個維度均爲最好或最多在某一維度上存在輕微問題； 
預設 0。 
若圖片質量不滿足要求，則返回結果中會提示圖片質量檢測不符要求。
        :type QualityControl: int
        :param FaceMatchThreshold: 出參Score中，只有大於等於FaceMatchThreshold值的結果才會返回。預設爲0。取值範圍[0.0,100.0) 。
        :type FaceMatchThreshold: float
        :param NeedPersonInfo: 是否返回人員具體訊息。0 爲關閉，1 爲開啓。預設爲 0。其他非0非1值預設爲0
        :type NeedPersonInfo: int
        :param NeedRotateDetection: 是否開啓圖片旋轉識别支援。0爲不開啓，1爲開啓。預設爲0。本參數的作用爲，當圖片中的人臉被旋轉且圖片沒有exif訊息時，如果不開啓圖片旋轉識别支援則無法正确檢測、識别圖片中的人臉。若您确認圖片包含exif訊息或者您确認輸入圖中人臉不會出現被旋轉情況，請不要開啓本參數。開啓後，整體耗時将可能增加數百毫秒。
        :type NeedRotateDetection: int
        """
        self.GroupIds = None
        self.Image = None
        self.Url = None
        self.MaxFaceNum = None
        self.MinFaceSize = None
        self.MaxPersonNum = None
        self.QualityControl = None
        self.FaceMatchThreshold = None
        self.NeedPersonInfo = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.GroupIds = params.get("GroupIds")
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.MaxFaceNum = params.get("MaxFaceNum")
        self.MinFaceSize = params.get("MinFaceSize")
        self.MaxPersonNum = params.get("MaxPersonNum")
        self.QualityControl = params.get("QualityControl")
        self.FaceMatchThreshold = params.get("FaceMatchThreshold")
        self.NeedPersonInfo = params.get("NeedPersonInfo")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class SearchPersonsResponse(AbstractModel):
    """SearchPersons返回參數結構體

    """

    def __init__(self):
        """
        :param Results: 識别結果。
        :type Results: list of Result
        :param PersonNum: 搜索的人員庫中包含的人員數。若輸入圖片中所有人臉均不符合質量要求，則返回0。
        :type PersonNum: int
        :param FaceModelVersion: 人臉識别所用的算法模型版本。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FaceModelVersion: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Results = None
        self.PersonNum = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = Result()
                obj._deserialize(item)
                self.Results.append(obj)
        self.PersonNum = params.get("PersonNum")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class SearchPersonsReturnsByGroupRequest(AbstractModel):
    """SearchPersonsReturnsByGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupIds: 希望搜索的人員庫清單，上限60個。
        :type GroupIds: list of str
        :param Image: 圖片 base64 數據，base64 編碼後大小不可超過5M。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Image: str
        :param Url: 圖片的 Url 。對應圖片 base64 編碼後大小不可超過5M。
Url、Image必須提供一個，如果都提供，只使用 Url。
圖片儲存於Top Cloud 的Url可保障更高下載速度和穩定性，建議圖片儲存於Top Cloud 。
非Top Cloud 儲存的Url速度和穩定性可能受一定影響。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Url: str
        :param MaxFaceNum: 最多識别的人臉數目。預設值爲1（僅檢測圖片中面積最大的那張人臉），最大值爲10。
MaxFaceNum用於，當輸入的待識别圖片包含多張人臉時，設定要搜索的人臉的數量。
例：輸入的Image或Url中的圖片包含多張人臉，設MaxFaceNum=5，則會識别圖片中面積最大的5張人臉。
        :type MaxFaceNum: int
        :param MinFaceSize: 人臉長和寬的最小尺寸，單位爲像素。預設爲34。低於34将影響搜索精度。建議設置爲80。
        :type MinFaceSize: int
        :param MaxPersonNumPerGroup: 被檢測到的人臉，對應最多返回的最相似人員數目。預設值爲5，最大值爲10。  
例，設MaxFaceNum爲3，MaxPersonNumPerGroup爲5，GroupIds長度爲3，則最多可能返回3*5*3=45個人員。
        :type MaxPersonNumPerGroup: int
        :param QualityControl: 圖片質量控制。 
0: 不進行控制； 
1:較低的質量要求，圖像存在非常模糊，眼睛鼻子嘴巴遮擋至少其中一種或多種的情況； 
2: 一般的質量要求，圖像存在偏亮，偏暗，模糊或一般模糊，眉毛遮擋，臉頰遮擋，下巴遮擋，至少其中三種的情況； 
3: 較高的質量要求，圖像存在偏亮，偏暗，一般模糊，眉毛遮擋，臉頰遮擋，下巴遮擋，其中一到兩種的情況； 
4: 很高的質量要求，各個維度均爲最好或最多在某一維度上存在輕微問題； 
預設 0。 
若圖片質量不滿足要求，則返回結果中會提示圖片質量檢測不符要求。
        :type QualityControl: int
        :param FaceMatchThreshold: 出參Score中，只有超過FaceMatchThreshold值的結果才會返回。預設爲0。
        :type FaceMatchThreshold: float
        :param NeedPersonInfo: 是否返回人員具體訊息。0 爲關閉，1 爲開啓。預設爲 0。其他非0非1值預設爲0
        :type NeedPersonInfo: int
        :param NeedRotateDetection: 是否開啓圖片旋轉識别支援。0爲不開啓，1爲開啓。預設爲0。本參數的作用爲，當圖片中的人臉被旋轉且圖片沒有exif訊息時，如果不開啓圖片旋轉識别支援則無法正确檢測、識别圖片中的人臉。若您确認圖片包含exif訊息或者您确認輸入圖中人臉不會出現被旋轉情況，請不要開啓本參數。開啓後，整體耗時将可能增加數百毫秒。
        :type NeedRotateDetection: int
        """
        self.GroupIds = None
        self.Image = None
        self.Url = None
        self.MaxFaceNum = None
        self.MinFaceSize = None
        self.MaxPersonNumPerGroup = None
        self.QualityControl = None
        self.FaceMatchThreshold = None
        self.NeedPersonInfo = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.GroupIds = params.get("GroupIds")
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.MaxFaceNum = params.get("MaxFaceNum")
        self.MinFaceSize = params.get("MinFaceSize")
        self.MaxPersonNumPerGroup = params.get("MaxPersonNumPerGroup")
        self.QualityControl = params.get("QualityControl")
        self.FaceMatchThreshold = params.get("FaceMatchThreshold")
        self.NeedPersonInfo = params.get("NeedPersonInfo")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class SearchPersonsReturnsByGroupResponse(AbstractModel):
    """SearchPersonsReturnsByGroup返回參數結構體

    """

    def __init__(self):
        """
        :param PersonNum: 搜索的人員庫中包含的人員數。若輸入圖片中所有人臉均不符合質量要求，則返回0。
        :type PersonNum: int
        :param ResultsReturnsByGroup: 識别結果。
        :type ResultsReturnsByGroup: list of ResultsReturnsByGroup
        :param FaceModelVersion: 人臉識别所用的算法模型版本。
        :type FaceModelVersion: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PersonNum = None
        self.ResultsReturnsByGroup = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PersonNum = params.get("PersonNum")
        if params.get("ResultsReturnsByGroup") is not None:
            self.ResultsReturnsByGroup = []
            for item in params.get("ResultsReturnsByGroup"):
                obj = ResultsReturnsByGroup()
                obj._deserialize(item)
                self.ResultsReturnsByGroup.append(obj)
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class VerifyFaceRequest(AbstractModel):
    """VerifyFace請求參數結構體

    """

    def __init__(self):
        """
        :param PersonId: 待驗證的人員ID。人員ID具體訊息請參考人員庫管理相關介面。
        :type PersonId: str
        :param Image: 圖片 base64 數據，base64 編碼後大小不可超過5M。
若圖片中包含多張人臉，只選取其中人臉面積最大的人臉。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Image: str
        :param Url: 圖片的 Url 。對應圖片 base64 編碼後大小不可超過5M。
Url、Image必須提供一個，如果都提供，只使用 Url。  
圖片儲存於Top Cloud 的Url可保障更高下載速度和穩定性，建議圖片儲存於Top Cloud 。 
非Top Cloud 儲存的Url速度和穩定性可能受一定影響。
若圖片中包含多張人臉，只選取其中人臉面積最大的人臉。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Url: str
        :param QualityControl: 圖片質量控制。 
0: 不進行控制； 
1:較低的質量要求，圖像存在非常模糊，眼睛鼻子嘴巴遮擋至少其中一種或多種的情況； 
2: 一般的質量要求，圖像存在偏亮，偏暗，模糊或一般模糊，眉毛遮擋，臉頰遮擋，下巴遮擋，至少其中三種的情況； 
3: 較高的質量要求，圖像存在偏亮，偏暗，一般模糊，眉毛遮擋，臉頰遮擋，下巴遮擋，其中一到兩種的情況； 
4: 很高的質量要求，各個維度均爲最好或最多在某一維度上存在輕微問題； 
預設 0。 
若圖片質量不滿足要求，則返回結果中會提示圖片質量檢測不符要求。
        :type QualityControl: int
        :param NeedRotateDetection: 是否開啓圖片旋轉識别支援。0爲不開啓，1爲開啓。預設爲0。本參數的作用爲，當圖片中的人臉被旋轉且圖片沒有exif訊息時，如果不開啓圖片旋轉識别支援則無法正确檢測、識别圖片中的人臉。若您确認圖片包含exif訊息或者您确認輸入圖中人臉不會出現被旋轉情況，請不要開啓本參數。開啓後，整體耗時将可能增加數百毫秒。
        :type NeedRotateDetection: int
        """
        self.PersonId = None
        self.Image = None
        self.Url = None
        self.QualityControl = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.QualityControl = params.get("QualityControl")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class VerifyFaceResponse(AbstractModel):
    """VerifyFace返回參數結構體

    """

    def __init__(self):
        """
        :param Score: 給定的人臉圖片與 PersonId 對應人臉的相似度。若 PersonId 下有多張人臉（Face），返回相似度最大的分數。

不同算法版本返回的相似度分數不同。
若需要驗證兩張圖片中人臉是否爲同一人，3.0版本誤識率千分之一對應分數爲40分，誤識率萬分之一對應分數爲50分，誤識率十萬分之一對應分數爲60分。 一般超過50分則可認定爲同一人。
2.0版本誤識率千分之一對應分數爲70分，誤識率萬分之一對應分數爲80分，誤識率十萬分之一對應分數爲90分。 一般超過80分則可認定爲同一人。
        :type Score: float
        :param IsMatch: 是否爲同一人的判斷。
        :type IsMatch: bool
        :param FaceModelVersion: 人臉識别所用的算法模型版本。
        :type FaceModelVersion: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Score = None
        self.IsMatch = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Score = params.get("Score")
        self.IsMatch = params.get("IsMatch")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")


class VerifyPersonRequest(AbstractModel):
    """VerifyPerson請求參數結構體

    """

    def __init__(self):
        """
        :param Image: 圖片 base64 數據。
若圖片中包含多張人臉，只選取其中人臉面積最大的人臉。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Image: str
        :param Url: 圖片的 Url 。 圖片的 Url、Image必須提供一個，如果都提供，只使用 Url。 
圖片儲存於Top Cloud 的Url可保障更高下載速度和穩定性，建議圖片儲存於Top Cloud 。 
非Top Cloud 儲存的Url速度和穩定性可能受一定影響。
若圖片中包含多張人臉，只選取其中人臉面積最大的人臉。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Url: str
        :param PersonId: 待驗證的人員ID。人員ID具體訊息請參考人員庫管理相關介面。
        :type PersonId: str
        :param QualityControl: 圖片質量控制。 
0: 不進行控制； 
1:較低的質量要求，圖像存在非常模糊，眼睛鼻子嘴巴遮擋至少其中一種或多種的情況； 
2: 一般的質量要求，圖像存在偏亮，偏暗，模糊或一般模糊，眉毛遮擋，臉頰遮擋，下巴遮擋，至少其中三種的情況； 
3: 較高的質量要求，圖像存在偏亮，偏暗，一般模糊，眉毛遮擋，臉頰遮擋，下巴遮擋，其中一到兩種的情況； 
4: 很高的質量要求，各個維度均爲最好或最多在某一維度上存在輕微問題； 
預設 0。 
若圖片質量不滿足要求，則返回結果中會提示圖片質量檢測不符要求。
        :type QualityControl: int
        :param NeedRotateDetection: 是否開啓圖片旋轉識别支援。0爲不開啓，1爲開啓。預設爲0。本參數的作用爲，當圖片中的人臉被旋轉且圖片沒有exif訊息時，如果不開啓圖片旋轉識别支援則無法正确檢測、識别圖片中的人臉。若您确認圖片包含exif訊息或者您确認輸入圖中人臉不會出現被旋轉情況，請不要開啓本參數。開啓後，整體耗時将可能增加數百毫秒。
        :type NeedRotateDetection: int
        """
        self.Image = None
        self.Url = None
        self.PersonId = None
        self.QualityControl = None
        self.NeedRotateDetection = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.PersonId = params.get("PersonId")
        self.QualityControl = params.get("QualityControl")
        self.NeedRotateDetection = params.get("NeedRotateDetection")


class VerifyPersonResponse(AbstractModel):
    """VerifyPerson返回參數結構體

    """

    def __init__(self):
        """
        :param Score: 給定的人臉照片與 PersonId 對應的相似度。若 PersonId 下有多張人臉（Face），會融合多張人臉訊息進行驗證。
        :type Score: float
        :param IsMatch: 是否爲同一人的判斷。
        :type IsMatch: bool
        :param FaceModelVersion: 人臉識别所用的算法模型版本。
        :type FaceModelVersion: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Score = None
        self.IsMatch = None
        self.FaceModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Score = params.get("Score")
        self.IsMatch = params.get("IsMatch")
        self.FaceModelVersion = params.get("FaceModelVersion")
        self.RequestId = params.get("RequestId")