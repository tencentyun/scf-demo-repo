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
        :param Image: 圖片 base64 數據。支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Image: str
        :param Url: 圖片的 Url、Image必須提供一個，如果都提供，只使用 Url。  
圖片儲存于Top Cloud 的Url可保障更高下載速度和穩定性，建議圖片儲存于Top Cloud 。 
非Top Cloud 儲存的Url速度和穩定性可能受一定影響。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Url: str
        """
        self.Mode = None
        self.Image = None
        self.Url = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        self.Image = params.get("Image")
        self.Url = params.get("Url")


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
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ImageWidth = None
        self.ImageHeight = None
        self.FaceShapeSet = None
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
10萬大小人臉庫，若人臉均爲類似抓拍照（人臉質量較差）， 
誤識率百分之一對應分數爲70分，誤識率千分之一對應分數爲80分，誤識率萬分之一對應分數爲90分； 
若人臉均爲類似自拍照（人臉質量較好）， 
誤識率百分之一對應分數爲60分，誤識率千分之一對應分數爲70分，誤識率萬分之一對應分數爲80分。 
建議分數不要超過90分。您可以根據實際情況選擇合适的分數。
        :type Score: float
        """
        self.PersonId = None
        self.FaceId = None
        self.Score = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.FaceId = params.get("FaceId")
        self.Score = params.get("Score")


class CompareFaceRequest(AbstractModel):
    """CompareFace請求參數結構體

    """

    def __init__(self):
        """
        :param ImageA: A 圖片 base64 數據。
若圖片中包含多張人臉，只選取其中人臉面積最大的人臉。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type ImageA: str
        :param ImageB: B 圖片 base64 數據。
若圖片中包含多張人臉，只選取其中人臉面積最大的人臉。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type ImageB: str
        :param UrlA: A 圖片的 Url 。A 圖片的 Url、Image必須提供一個，如果都提供，只使用 Url。 
圖片儲存于Top Cloud 的Url可保障更高下載速度和穩定性，建議圖片儲存于Top Cloud 。 
非Top Cloud 儲存的Url速度和穩定性可能受一定影響。
若圖片中包含多張人臉，只選取其中人臉面積最大的人臉。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type UrlA: str
        :param UrlB: B 圖片的 Url 。B 圖片的 Url、Image必須提供一個，如果都提供，只使用 Url。 
圖片儲存于Top Cloud 的Url可保障更高下載速度和穩定性，建議圖片儲存于Top Cloud 。 
非Top Cloud 儲存的Url速度和穩定性可能受一定影響。
若圖片中包含多張人臉，只選取其中人臉面積最大的人臉。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type UrlB: str
        """
        self.ImageA = None
        self.ImageB = None
        self.UrlA = None
        self.UrlB = None


    def _deserialize(self, params):
        self.ImageA = params.get("ImageA")
        self.ImageB = params.get("ImageB")
        self.UrlA = params.get("UrlA")
        self.UrlB = params.get("UrlB")


class CompareFaceResponse(AbstractModel):
    """CompareFace返回參數結構體

    """

    def __init__(self):
        """
        :param Score: 兩張圖片中人臉的相似度分數。 
若需要驗證兩張圖片中人臉是否爲同一人，則誤識率千分之一對應分數爲70分，誤識率萬分之一對應分數爲80分，誤識率十萬分之一對應分數爲90分。  
一般超過80分則可認定爲同一人。 
若需要驗證兩張圖片中的人臉是否爲同一人，建議使用人臉驗證介面。
        :type Score: float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Score = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Score = params.get("Score")
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
        :param Images: 圖片 base64 數據。人員人臉總數量不可超過5張。
若圖片中包含多張人臉，只選取其中人臉面積最大的人臉。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Images: list of str
        :param Urls: 圖片的 Url、Image必須提供一個，如果都提供，只使用 Url。
圖片儲存于Top Cloud 的Url可保障更高下載速度和穩定性，建議圖片儲存于Top Cloud 。 
非Top Cloud 儲存的Url速度和穩定性可能受一定影響。 
人員人臉總數量不可超過5張。
若圖片中包含多張人臉，只選取其中人臉面積最大的人臉。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Urls: list of str
        """
        self.PersonId = None
        self.Images = None
        self.Urls = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Images = params.get("Images")
        self.Urls = params.get("Urls")


class CreateFaceResponse(AbstractModel):
    """CreateFace返回參數結構體

    """

    def __init__(self):
        """
        :param SucFaceNum: 加入成功的人臉數量
        :type SucFaceNum: int
        :param SucFaceIds: 加入成功的人臉ID清單
        :type SucFaceIds: list of str
        :param RetCode: 每張人臉圖片添加結果，-1101 代表未檢測到人臉，-1102 代表圖片解碼失敗，其他非 0 值代表算法服務異常。
        :type RetCode: list of int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SucFaceNum = None
        self.SucFaceIds = None
        self.RetCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SucFaceNum = params.get("SucFaceNum")
        self.SucFaceIds = params.get("SucFaceIds")
        self.RetCode = params.get("RetCode")
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
        :param GroupExDescriptions: 人員庫自定義描述欄位，用于描述人員庫中人員屬性，該人員庫下所有人員将擁有此描述欄位。 
最多可以創建5個。 
每個自定義描述欄位支援[1,30]個字元。 
在同一人員庫中自定義描述欄位不可重複。 
例： 設置某人員庫“自定義描述欄位”爲["學号","工号","手機号"]， 
則該人員庫下所有人員将擁有名爲“學号”、“工号”、“手機号”的描述欄位， 
可在對應人員描述欄位中填寫内容，登記該人員的學号、工号、手機号等訊息。
        :type GroupExDescriptions: list of str
        :param Tag: 人員庫訊息備注，[0，40]個字元。
        :type Tag: str
        """
        self.GroupName = None
        self.GroupId = None
        self.GroupExDescriptions = None
        self.Tag = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupId = params.get("GroupId")
        self.GroupExDescriptions = params.get("GroupExDescriptions")
        self.Tag = params.get("Tag")


class CreateGroupResponse(AbstractModel):
    """CreateGroup返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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
        :param PersonId: 人員ID，單個Top Cloud 賬号下不可修改，不可重複。支援英文、數字、-%@#&_，長度限制64B。
        :type PersonId: str
        :param Gender: 0代表未填寫，1代表男性，2代表女性。
        :type Gender: int
        :param PersonExDescriptionInfos: 人員描述欄位内容，key-value。[0，60]個字元，可修改，可重複。
        :type PersonExDescriptionInfos: list of PersonExDescriptionInfo
        :param Image: 圖片 base64 數據。
若圖片中包含多張人臉，只選取其中人臉面積最大的人臉。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Image: str
        :param Url: 圖片的 Url、Image必須提供一個，如果都提供，只使用 Url。
圖片儲存于Top Cloud 的Url可保障更高下載速度和穩定性，建議圖片儲存于Top Cloud 。 
非Top Cloud 儲存的Url速度和穩定性可能受一定影響。
若圖片中包含多張人臉，只選取其中人臉面積最大的人臉。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Url: str
        """
        self.GroupId = None
        self.PersonName = None
        self.PersonId = None
        self.Gender = None
        self.PersonExDescriptionInfos = None
        self.Image = None
        self.Url = None


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


class CreatePersonResponse(AbstractModel):
    """CreatePerson返回參數結構體

    """

    def __init__(self):
        """
        :param FaceId: 人臉圖片唯一标識。
        :type FaceId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FaceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FaceId = params.get("FaceId")
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
此參數用于控制處理待檢測圖片中的人臉個數，值越小，處理速度越快。
        :type MaxFaceNum: int
        :param MinFaceSize: 人臉長和寬的最小尺寸，單位爲像素。預設爲40。低于此尺寸的人臉不會被檢測。
        :type MinFaceSize: int
        :param Image: 圖片 base64 數據。支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Image: str
        :param Url: 圖片的 Url、Image必須提供一個，如果都提供，只使用 Url。 
圖片儲存于Top Cloud 的Url可保障更高下載速度和穩定性，建議圖片儲存于Top Cloud 。 
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
最多返回面積最大的 5 張人臉質量分訊息，超過 5 張人臉（第 6 張及以後的人臉）的 FaceQualityInfo不具備參考意義。  
建議：人臉入庫操作建議開啓此功能。
        :type NeedQualityDetection: int
        """
        self.MaxFaceNum = None
        self.MinFaceSize = None
        self.Image = None
        self.Url = None
        self.NeedFaceAttributes = None
        self.NeedQualityDetection = None


    def _deserialize(self, params):
        self.MaxFaceNum = params.get("MaxFaceNum")
        self.MinFaceSize = params.get("MinFaceSize")
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.NeedFaceAttributes = params.get("NeedFaceAttributes")
        self.NeedQualityDetection = params.get("NeedQualityDetection")


class DetectFaceResponse(AbstractModel):
    """DetectFace返回參數結構體

    """

    def __init__(self):
        """
        :param ImageWidth: 請求的圖片寬度。
        :type ImageWidth: int
        :param ImageHeight: 請求的圖片高度。
        :type ImageHeight: int
        :param FaceInfos: 人臉訊息清單。
        :type FaceInfos: list of FaceInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ImageWidth = None
        self.ImageHeight = None
        self.FaceInfos = None
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
        self.RequestId = params.get("RequestId")


class DetectLiveFaceRequest(AbstractModel):
    """DetectLiveFace請求參數結構體

    """

    def __init__(self):
        """
        :param Image: 圖片 base64 數據（圖片的寬高比請接近3:4，不符合寬高比的圖片返回的分值不具備參考意義）。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Image: str
        :param Url: 圖片的 Url 。圖片的 Url、Image必須提供一個，如果都提供，只使用 Url。 
（圖片的寬高比請接近 3:4，不符合寬高比的圖片返回的分值不具備參考意義） 
圖片儲存于Top Cloud 的Url可保障更高下載速度和穩定性，建議圖片儲存于Top Cloud 。 
非Top Cloud 儲存的Url速度和穩定性可能受一定影響。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Url: str
        """
        self.Image = None
        self.Url = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.Url = params.get("Url")


class DetectLiveFaceResponse(AbstractModel):
    """DetectLiveFace返回參數結構體

    """

    def __init__(self):
        """
        :param Score: 活體打分，取值範圍 [0,100]，分數一般落于[80, 100]區間内，0分也爲常見值。推薦相大于 87 時可判斷爲活體。可根據具體場景自行調整阈值。
        :type Score: float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Score = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Score = params.get("Score")
        self.RequestId = params.get("RequestId")


class FaceAttributesInfo(AbstractModel):
    """人臉屬性訊息，包含性别( gender )、年齡( age )、表情( expression )、
    魅力( beauty )、眼鏡( glass )、口罩（mask）、頭發（hair）和姿态 (pitch，roll，yaw )。只有當 NeedFaceAttributes 設爲 1 時才返回有效訊息。

    """

    def __init__(self):
        """
        :param Gender: 性别 [0(female，女性)~100(male，男性)]。 NeedFaceAttributes 不爲 1 或檢測超過 5 張人臉時，此參數仍返回，但不具備參考意義。
        :type Gender: int
        :param Age: 年齡 [0~100]。NeedFaceAttributes 不爲1 或檢測超過 5 張人臉時，此參數仍返回，但不具備參考意義。
        :type Age: int
        :param Expression: 微笑[0(normal，正常)~50(smile，微笑)~100(laugh，大笑)]。NeedFaceAttributes 不爲1 或檢測超過 5 張人臉時，此參數仍返回，但不具備參考意義。
        :type Expression: int
        :param Glass: 是否有眼鏡 [true,false]。NeedFaceAttributes 不爲1 或檢測超過 5 張人臉時，此參數仍返回，但不具備參考意義。
        :type Glass: bool
        :param Pitch: 上下偏移[-30,30]。NeedFaceAttributes 不爲1 或檢測超過 5 張人臉時，此參數仍返回，但不具備參考意義。 
建議：人臉入庫選擇[-10,10]的圖片。
        :type Pitch: int
        :param Yaw: 左右偏移[-30,30]。 NeedFaceAttributes 不爲1 或檢測超過 5 張人臉時，此參數仍返回，但不具備參考意義。 
建議：人臉入庫選擇[-10,10]的圖片。
        :type Yaw: int
        :param Roll: 平面旋轉[-180,180]。 NeedFaceAttributes 不爲1 或檢測超過 5 張人臉時，此參數仍返回，但不具備參考意義。  
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
        :param X: 人臉框左上角橫坐标。
人臉框包含人臉五官位置并在此基礎上進行一定的擴展，若人臉框超出圖片範圍，會導緻坐标負值。 
若需截取完整人臉，可以在完整分completess滿足需求的情況下，将負值坐标取0。
        :type X: int
        :param Y: 人臉框左上角縱坐标。 
人臉框包含人臉五官位置并在此基礎上進行一定的擴展，若人臉框超出圖片範圍，會導緻坐标負值。 
若需截取完整人臉，可以在完整分completess滿足需求的情況下，将負值坐标取0。
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
        :param X: 人臉框左上角橫坐标。 
人臉框包含人臉五官位置并在此基礎上進行一定的擴展，若人臉框超出圖片範圍，會導緻坐标負值。 
若需截取完整人臉，可以在完整分completess滿足需求的情況下，将負值坐标取0。
        :type X: int
        :param Y: 人臉框左上角縱坐标。 
人臉框包含人臉五官位置并在此基礎上進行一定的擴展，若人臉框超出圖片範圍，會導緻坐标負值。 
若需截取完整人臉，可以在完整分completess滿足需求的情況下，将負值坐标取0。
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


class GetGroupListRequest(AbstractModel):
    """GetGroupList請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 起始序号，預設值爲0
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
        :param FaceIds: 包含的人臉圖片清單
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
        :param Offset: 起始序号，預設值爲0
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
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PersonGroupInfos = None
        self.GroupNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PersonGroupInfos") is not None:
            self.PersonGroupInfos = []
            for item in params.get("PersonGroupInfos"):
                obj = PersonGroupInfo()
                obj._deserialize(item)
                self.PersonGroupInfos.append(obj)
        self.GroupNum = params.get("GroupNum")
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
        :param Offset: 起始序号，預設值爲0
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
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PersonInfos = None
        self.PersonNum = None
        self.FaceNum = None
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
        self.RequestId = params.get("RequestId")


class GroupExDescriptionInfo(AbstractModel):
    """需要修改的人員庫自定義描述欄位key-value

    """

    def __init__(self):
        """
        :param GroupExDescriptionIndex: 人員庫自定義描述欄位Index，從0開始
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
        """
        self.GroupName = None
        self.GroupId = None
        self.GroupExDescriptions = None
        self.Tag = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupId = params.get("GroupId")
        self.GroupExDescriptions = params.get("GroupExDescriptions")
        self.Tag = params.get("Tag")


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
        """
        self.PersonName = None
        self.PersonId = None
        self.Gender = None
        self.PersonExDescriptions = None
        self.FaceIds = None


    def _deserialize(self, params):
        self.PersonName = params.get("PersonName")
        self.PersonId = params.get("PersonId")
        self.Gender = params.get("Gender")
        self.PersonExDescriptions = params.get("PersonExDescriptions")
        self.FaceIds = params.get("FaceIds")


class Point(AbstractModel):
    """坐标

    """

    def __init__(self):
        """
        :param X: x坐标
        :type X: int
        :param Y: Y坐标
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
        """
        self.Candidates = None
        self.FaceRect = None


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


class SearchFacesRequest(AbstractModel):
    """SearchFaces請求參數結構體

    """

    def __init__(self):
        """
        :param GroupIds: 希望搜索的人員庫清單，上限100個。
        :type GroupIds: list of str
        :param Image: 圖片 base64 數據。支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Image: str
        :param Url: 圖片的 Url、Image必須提供一個，如果都提供，只使用 Url。
圖片儲存于Top Cloud 的Url可保障更高下載速度和穩定性，建議圖片儲存于Top Cloud 。 
非Top Cloud 儲存的Url速度和穩定性可能受一定影響。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Url: str
        :param MaxFaceNum: 最多處理的人臉數目。預設值爲1（僅檢測圖片中面積最大的那張人臉），最大值爲10。 
MaxFaceNum用于，當待識别圖片包含多張人臉時，要搜索的人臉數量。 
當 MaxFaceNum 不爲1時，設MaxFaceNum=M，則實際上是 M:N 的人臉搜索。
        :type MaxFaceNum: int
        :param MinFaceSize: 人臉長和寬的最小尺寸，單位爲像素。預設爲80。低于40将影響搜索精度。建議設置爲80。
        :type MinFaceSize: int
        :param MaxPersonNum: 被檢測到的人臉，對應最多返回的最相似人員數目。預設值爲5，最大值爲10。  
例，設MaxFaceNum爲3，MaxPersonNum爲5，則最多可能返回3*5=15個人員。
        :type MaxPersonNum: int
        """
        self.GroupIds = None
        self.Image = None
        self.Url = None
        self.MaxFaceNum = None
        self.MinFaceSize = None
        self.MaxPersonNum = None


    def _deserialize(self, params):
        self.GroupIds = params.get("GroupIds")
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.MaxFaceNum = params.get("MaxFaceNum")
        self.MinFaceSize = params.get("MinFaceSize")
        self.MaxPersonNum = params.get("MaxPersonNum")


class SearchFacesResponse(AbstractModel):
    """SearchFaces返回參數結構體

    """

    def __init__(self):
        """
        :param Results: 識别結果。
        :type Results: list of Result
        :param FaceNum: 搜索的人員庫中包含的人臉數。
        :type FaceNum: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Results = None
        self.FaceNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = Result()
                obj._deserialize(item)
                self.Results.append(obj)
        self.FaceNum = params.get("FaceNum")
        self.RequestId = params.get("RequestId")


class VerifyFaceRequest(AbstractModel):
    """VerifyFace請求參數結構體

    """

    def __init__(self):
        """
        :param PersonId: 待驗證的人員ID。人員ID具體訊息請參考人員庫管理相關介面。
        :type PersonId: str
        :param Image: 圖片 base64 數據。
若圖片中包含多張人臉，只選取其中人臉面積最大的人臉。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Image: str
        :param Url: 圖片的 Url 。 圖片的 Url、Image必須提供一個，如果都提供，只使用 Url。 
圖片儲存于Top Cloud 的Url可保障更高下載速度和穩定性，建議圖片儲存于Top Cloud 。 
非Top Cloud 儲存的Url速度和穩定性可能受一定影響。
若圖片中包含多張人臉，只選取其中人臉面積最大的人臉。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Url: str
        """
        self.PersonId = None
        self.Image = None
        self.Url = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Image = params.get("Image")
        self.Url = params.get("Url")


class VerifyFaceResponse(AbstractModel):
    """VerifyFace返回參數結構體

    """

    def __init__(self):
        """
        :param Score: 給定的人臉圖片與 PersonId 對應人臉的相似度。若 PersonId 下有多張人臉（Face），返回相似度最大的分數。
        :type Score: float
        :param IsMatch: 是否爲同一人的判斷。
        :type IsMatch: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Score = None
        self.IsMatch = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Score = params.get("Score")
        self.IsMatch = params.get("IsMatch")
        self.RequestId = params.get("RequestId")