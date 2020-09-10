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


class BodyDetectResult(AbstractModel):
    """圖中檢測出來的人體框。

    """

    def __init__(self):
        """
        :param Confidence: 檢測出的人體置信度。 
誤識率百分之十對應的阈值是0.14；誤識率百分之五對應的阈值是0.32；誤識率百分之二對應的阈值是0.62；誤識率百分之一對應的阈值是0.81。 
通常情況建議使用阈值0.32，可适用大多數情況。
        :type Confidence: float
        :param BodyRect: 圖中檢測出來的人體框
        :type BodyRect: :class:`taifucloudcloud.bda.v20200324.models.BodyRect`
        """
        self.Confidence = None
        self.BodyRect = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        if params.get("BodyRect") is not None:
            self.BodyRect = BodyRect()
            self.BodyRect._deserialize(params.get("BodyRect"))


class BodyRect(AbstractModel):
    """人體框

    """

    def __init__(self):
        """
        :param X: 人體框左上角橫坐标。
        :type X: int
        :param Y: 人體框左上角縱坐标。
        :type Y: int
        :param Width: 人體寬度。
        :type Width: int
        :param Height: 人體高度。
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


class Candidate(AbstractModel):
    """識别出的最相似候選人。

    """

    def __init__(self):
        """
        :param PersonId: 人員ID。
        :type PersonId: str
        :param TraceId: 人體軌迹ID。
        :type TraceId: str
        :param Score: 候選者的比對得分。 
十萬人體庫下，誤識率百分之五對應的分數爲70分；誤識率百分之二對應的分數爲80分；誤識率百分之一對應的分數爲90分。
 
二十萬人體庫下，誤識率百分之五對應的分數爲80分；誤識率百分之二對應的分數爲90分；誤識率百分之一對應的分數爲95分。
 
通常情況建議使用分數80分（保召回）。若希望獲得較高精度，建議使用分數90分（保準确）。
        :type Score: float
        """
        self.PersonId = None
        self.TraceId = None
        self.Score = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.TraceId = params.get("TraceId")
        self.Score = params.get("Score")


class CreateGroupRequest(AbstractModel):
    """CreateGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupName: 人體庫名稱，[1,60]個字元，可修改，不可重複。
        :type GroupName: str
        :param GroupId: 人體庫 ID，不可修改，不可重複。支援英文、數字、-%@#&_，長度限制64B。
        :type GroupId: str
        :param Tag: 人體庫訊息備注，[0，40]個字元。
        :type Tag: str
        :param BodyModelVersion: 人體識别所用的算法模型版本。 
目前入參僅支援 “1.0”1個輸入。 預設爲"1.0"。  
不同算法模型版本對應的人體識别算法不同，新版本的整體效果會優于舊版本，後續我們将推出更新版本。
        :type BodyModelVersion: str
        """
        self.GroupName = None
        self.GroupId = None
        self.Tag = None
        self.BodyModelVersion = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupId = params.get("GroupId")
        self.Tag = params.get("Tag")
        self.BodyModelVersion = params.get("BodyModelVersion")


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
        :param PersonId: 人員ID，單個Top Cloud 賬号下不可修改，不可重複。 
支援英文、數字、-%@#&_，，長度限制64B。
        :type PersonId: str
        :param Trace: 人體軌迹訊息。
        :type Trace: :class:`taifucloudcloud.bda.v20200324.models.Trace`
        """
        self.GroupId = None
        self.PersonName = None
        self.PersonId = None
        self.Trace = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.PersonName = params.get("PersonName")
        self.PersonId = params.get("PersonId")
        if params.get("Trace") is not None:
            self.Trace = Trace()
            self.Trace._deserialize(params.get("Trace"))


class CreatePersonResponse(AbstractModel):
    """CreatePerson返回參數結構體

    """

    def __init__(self):
        """
        :param TraceId: 人員軌迹唯一标識。
        :type TraceId: str
        :param BodyModelVersion: 人體識别所用的算法模型版本。
        :type BodyModelVersion: str
        :param InputRetCode: 輸入的人體軌迹圖片中的合法性校驗結果。
只有爲0時結果才有意義。
-1001: 輸入圖片不合法。-1002: 輸入圖片不能構成軌迹。
        :type InputRetCode: int
        :param InputRetCodeDetails: 輸入的人體軌迹圖片中的合法性校驗結果詳情。 
-1101:圖片無效，-1102:url不合法。-1103:圖片過大。-1104:圖片下載失敗。-1105:圖片解碼失敗。-1109:圖片分辨率過高。-2023:軌迹中有非同人圖片。-2024: 軌迹提取失敗。-2025: 人體檢測失敗。
RetCode 的順序和入參中Images 或 Urls 的順序一緻。
        :type InputRetCodeDetails: list of int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TraceId = None
        self.BodyModelVersion = None
        self.InputRetCode = None
        self.InputRetCodeDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TraceId = params.get("TraceId")
        self.BodyModelVersion = params.get("BodyModelVersion")
        self.InputRetCode = params.get("InputRetCode")
        self.InputRetCodeDetails = params.get("InputRetCodeDetails")
        self.RequestId = params.get("RequestId")


class CreateTraceRequest(AbstractModel):
    """CreateTrace請求參數結構體

    """

    def __init__(self):
        """
        :param PersonId: 人員ID。
        :type PersonId: str
        :param Trace: 人體軌迹訊息。
        :type Trace: :class:`taifucloudcloud.bda.v20200324.models.Trace`
        """
        self.PersonId = None
        self.Trace = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        if params.get("Trace") is not None:
            self.Trace = Trace()
            self.Trace._deserialize(params.get("Trace"))


class CreateTraceResponse(AbstractModel):
    """CreateTrace返回參數結構體

    """

    def __init__(self):
        """
        :param TraceId: 人員軌迹唯一标識。
        :type TraceId: str
        :param BodyModelVersion: 人體識别所用的算法模型版本。
        :type BodyModelVersion: str
        :param InputRetCode: 輸入的人體軌迹圖片中的合法性校驗結果。
只有爲0時結果才有意義。
-1001: 輸入圖片不合法。-1002: 輸入圖片不能構成軌迹。
        :type InputRetCode: int
        :param InputRetCodeDetails: 輸入的人體軌迹圖片中的合法性校驗結果詳情。 
-1101:圖片無效，-1102:url不合法。-1103:圖片過大。-1104:圖片下載失敗。-1105:圖片解碼失敗。-1109:圖片分辨率過高。-2023:軌迹中有非同人圖片。-2024: 軌迹提取失敗。-2025: 人體檢測失敗。
        :type InputRetCodeDetails: list of int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TraceId = None
        self.BodyModelVersion = None
        self.InputRetCode = None
        self.InputRetCodeDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TraceId = params.get("TraceId")
        self.BodyModelVersion = params.get("BodyModelVersion")
        self.InputRetCode = params.get("InputRetCode")
        self.InputRetCodeDetails = params.get("InputRetCodeDetails")
        self.RequestId = params.get("RequestId")


class DeleteGroupRequest(AbstractModel):
    """DeleteGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 人體庫ID。
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


class DeletePersonRequest(AbstractModel):
    """DeletePerson請求參數結構體

    """

    def __init__(self):
        """
        :param PersonId: 人員ID。
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


class DetectBodyRequest(AbstractModel):
    """DetectBody請求參數結構體

    """

    def __init__(self):
        """
        :param Image: 人體圖片 Base64 數據。
圖片 base64 編碼後大小不可超過5M。
圖片分辨率不得超過 2048*2048。
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Image: str
        :param Url: 人體圖片 Url 。
Url、Image必須提供一個，如果都提供，只使用 Url。
圖片 base64 編碼後大小不可超過5M。 
圖片分辨率不得超過 2048*2048。
圖片儲存于Top Cloud 的Url可保障更高下載速度和穩定性，建議圖片儲存于Top Cloud 。 
非Top Cloud 儲存的Url速度和穩定性可能受一定影響。 
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Url: str
        :param MaxBodyNum: 最多檢測的人體數目，預設值爲1（僅檢測圖片中面積最大的那個人體）； 最大值10 ，檢測圖片中面積最大的10個人體。
        :type MaxBodyNum: int
        """
        self.Image = None
        self.Url = None
        self.MaxBodyNum = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        self.MaxBodyNum = params.get("MaxBodyNum")


class DetectBodyResponse(AbstractModel):
    """DetectBody返回參數結構體

    """

    def __init__(self):
        """
        :param BodyDetectResults: 圖中檢測出來的人體框。
        :type BodyDetectResults: list of BodyDetectResult
        :param BodyModelVersion: 人體識别所用的算法模型版本。
        :type BodyModelVersion: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.BodyDetectResults = None
        self.BodyModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BodyDetectResults") is not None:
            self.BodyDetectResults = []
            for item in params.get("BodyDetectResults"):
                obj = BodyDetectResult()
                obj._deserialize(item)
                self.BodyDetectResults.append(obj)
        self.BodyModelVersion = params.get("BodyModelVersion")
        self.RequestId = params.get("RequestId")


class GetGroupListRequest(AbstractModel):
    """GetGroupList請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 起始序号，預設值爲0。
        :type Offset: int
        :param Limit: 返回數量，預設值爲10，最大值爲1000。
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
        :param GroupInfos: 返回的人體庫訊息。
        :type GroupInfos: list of GroupInfo
        :param GroupNum: 人體庫總數量。
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


class GetPersonListRequest(AbstractModel):
    """GetPersonList請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 人體庫ID。
        :type GroupId: str
        :param Offset: 起始序号，預設值爲0。
        :type Offset: int
        :param Limit: 返回數量，預設值爲10，最大值爲1000。
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
        :param PersonInfos: 返回的人員訊息。
        :type PersonInfos: list of PersonInfo
        :param PersonNum: 該人體庫的人員數量。
        :type PersonNum: int
        :param BodyModelVersion: 人體識别所用的算法模型版本。
        :type BodyModelVersion: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PersonInfos = None
        self.PersonNum = None
        self.BodyModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PersonInfos") is not None:
            self.PersonInfos = []
            for item in params.get("PersonInfos"):
                obj = PersonInfo()
                obj._deserialize(item)
                self.PersonInfos.append(obj)
        self.PersonNum = params.get("PersonNum")
        self.BodyModelVersion = params.get("BodyModelVersion")
        self.RequestId = params.get("RequestId")


class GroupInfo(AbstractModel):
    """返回的人員庫訊息。

    """

    def __init__(self):
        """
        :param GroupName: 人體庫名稱。
        :type GroupName: str
        :param GroupId: 人體庫ID。
        :type GroupId: str
        :param Tag: 人體庫訊息備注。
        :type Tag: str
        :param BodyModelVersion: 人體識别所用的算法模型版本。
        :type BodyModelVersion: str
        :param CreationTimestamp: Group的創建時間和日期 CreationTimestamp。CreationTimestamp 的值是自 Unix 紀元時間到Group創建時間的毫秒數。  
Unix 紀元時間是 1970 年 1 月 1 日星期四，協調世界時 (UTC) 。
        :type CreationTimestamp: int
        """
        self.GroupName = None
        self.GroupId = None
        self.Tag = None
        self.BodyModelVersion = None
        self.CreationTimestamp = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupId = params.get("GroupId")
        self.Tag = params.get("Tag")
        self.BodyModelVersion = params.get("BodyModelVersion")
        self.CreationTimestamp = params.get("CreationTimestamp")


class ModifyGroupRequest(AbstractModel):
    """ModifyGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 人體庫ID。
        :type GroupId: str
        :param GroupName: 人體庫名稱。
        :type GroupName: str
        :param Tag: 人體庫訊息備注。
        :type Tag: str
        """
        self.GroupId = None
        self.GroupName = None
        self.Tag = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
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


class ModifyPersonInfoRequest(AbstractModel):
    """ModifyPersonInfo請求參數結構體

    """

    def __init__(self):
        """
        :param PersonId: 人員ID。
        :type PersonId: str
        :param PersonName: 人員名稱。
        :type PersonName: str
        """
        self.PersonId = None
        self.PersonName = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.PersonName = params.get("PersonName")


class ModifyPersonInfoResponse(AbstractModel):
    """ModifyPersonInfo返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PersonInfo(AbstractModel):
    """人員訊息。

    """

    def __init__(self):
        """
        :param PersonName: 人員名稱。
        :type PersonName: str
        :param PersonId: 人員ID。
        :type PersonId: str
        :param TraceInfos: 包含的人體軌迹圖片訊息清單。
        :type TraceInfos: list of TraceInfo
        """
        self.PersonName = None
        self.PersonId = None
        self.TraceInfos = None


    def _deserialize(self, params):
        self.PersonName = params.get("PersonName")
        self.PersonId = params.get("PersonId")
        if params.get("TraceInfos") is not None:
            self.TraceInfos = []
            for item in params.get("TraceInfos"):
                obj = TraceInfo()
                obj._deserialize(item)
                self.TraceInfos.append(obj)


class SearchTraceRequest(AbstractModel):
    """SearchTrace請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 希望搜索的人體庫ID。
        :type GroupId: str
        :param Trace: 人體軌迹訊息。
        :type Trace: :class:`taifucloudcloud.bda.v20200324.models.Trace`
        :param MaxPersonNum: 單張被識别的人體軌迹返回的最相似人員數量。
預設值爲5，最大值爲100。
 例，設MaxPersonNum爲8，則返回Top8相似的人員訊息。 值越大，需要處理的時間越長。建議不要超過10。
        :type MaxPersonNum: int
        :param TraceMatchThreshold: 出參Score中，只有超過TraceMatchThreshold值的結果才會返回。
預設爲0。範圍[0, 100.0]。
        :type TraceMatchThreshold: float
        """
        self.GroupId = None
        self.Trace = None
        self.MaxPersonNum = None
        self.TraceMatchThreshold = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        if params.get("Trace") is not None:
            self.Trace = Trace()
            self.Trace._deserialize(params.get("Trace"))
        self.MaxPersonNum = params.get("MaxPersonNum")
        self.TraceMatchThreshold = params.get("TraceMatchThreshold")


class SearchTraceResponse(AbstractModel):
    """SearchTrace返回參數結構體

    """

    def __init__(self):
        """
        :param Candidates: 識别出的最相似候選人。
        :type Candidates: list of Candidate
        :param InputRetCode: 輸入的人體軌迹圖片中的合法性校驗結果。
只有爲0時結果才有意義。
-1001: 輸入圖片不合法。-1002: 輸入圖片不能構成軌迹。
        :type InputRetCode: int
        :param InputRetCodeDetails: 輸入的人體軌迹圖片中的合法性校驗結果詳情。 
-1101:圖片無效，-1102:url不合法。-1103:圖片過大。-1104:圖片下載失敗。-1105:圖片解碼失敗。-1109:圖片分辨率過高。-2023:軌迹中有非同人圖片。-2024: 軌迹提取失敗。-2025: 人體檢測失敗。
        :type InputRetCodeDetails: list of int
        :param BodyModelVersion: 人體識别所用的算法模型版本。
        :type BodyModelVersion: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Candidates = None
        self.InputRetCode = None
        self.InputRetCodeDetails = None
        self.BodyModelVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Candidates") is not None:
            self.Candidates = []
            for item in params.get("Candidates"):
                obj = Candidate()
                obj._deserialize(item)
                self.Candidates.append(obj)
        self.InputRetCode = params.get("InputRetCode")
        self.InputRetCodeDetails = params.get("InputRetCodeDetails")
        self.BodyModelVersion = params.get("BodyModelVersion")
        self.RequestId = params.get("RequestId")


class SegmentPortraitPicRequest(AbstractModel):
    """SegmentPortraitPic請求參數結構體

    """

    def __init__(self):
        """
        :param Image: 圖片 base64 數據，base64 編碼後大小不可超過5M。
圖片分辨率須小於2000*2000。 
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Image: str
        :param Url: 圖片的 Url 。
Url、Image必須提供一個，如果都提供，只使用 Url。
圖片分辨率須小於2000*2000 ，圖片 base64 編碼後大小不可超過5M。 
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


class SegmentPortraitPicResponse(AbstractModel):
    """SegmentPortraitPic返回參數結構體

    """

    def __init__(self):
        """
        :param ResultImage: 處理後的圖片 base64 數據，透明背景圖
        :type ResultImage: str
        :param ResultMask: 一個通過 Base64 編碼的文件，解碼後文件由 Float 型浮點數組成。這些浮點數代表原圖從左上角開始的每一行的每一個像素點，每一個浮點數的值是原圖相應像素點位于人體輪廓内的置信度（0-1）轉化的灰度值（0-255）
        :type ResultMask: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ResultImage = None
        self.ResultMask = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultImage = params.get("ResultImage")
        self.ResultMask = params.get("ResultMask")
        self.RequestId = params.get("RequestId")


class Trace(AbstractModel):
    """人體軌迹訊息

    """

    def __init__(self):
        """
        :param Images: 人體軌迹圖片 Base64 數組。 
數組長度最小爲1最大爲5。 
單個圖片 base64 編碼後大小不可超過2M。 
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Images: list of str
        :param Urls: 人體軌迹圖片 Url 數組。 
數組長度最小爲1最大爲5。 
單個圖片 base64 編碼後大小不可超過2M。 
Urls、Images必須提供一個，如果都提供，只使用 Urls。 
圖片儲存于Top Cloud 的Url可保障更高下載速度和穩定性，建議圖片儲存于Top Cloud 。 
非Top Cloud 儲存的Url速度和穩定性可能受一定影響。 
支援PNG、JPG、JPEG、BMP，不支援 GIF 圖片。
        :type Urls: list of str
        :param BodyRects: 若輸入的Images 和 Urls 是已經裁剪後的人體小圖，則可以忽略本參數。 
若否，或圖片中包含多個人體，則需要通過本參數來指定圖片中的人體框。 
順序對應 Images 或 Urls 中的順序。  
當不輸入本參數時，我們将認爲輸入圖片已是經過裁剪後的人體小圖，不會進行人體檢測而直接進行特征提取處理。
        :type BodyRects: list of BodyRect
        """
        self.Images = None
        self.Urls = None
        self.BodyRects = None


    def _deserialize(self, params):
        self.Images = params.get("Images")
        self.Urls = params.get("Urls")
        if params.get("BodyRects") is not None:
            self.BodyRects = []
            for item in params.get("BodyRects"):
                obj = BodyRect()
                obj._deserialize(item)
                self.BodyRects.append(obj)


class TraceInfo(AbstractModel):
    """人體軌迹訊息。

    """

    def __init__(self):
        """
        :param TraceId: 人體軌迹ID。
        :type TraceId: str
        :param BodyIds: 包含的人體軌迹圖片Id清單。
        :type BodyIds: list of str
        """
        self.TraceId = None
        self.BodyIds = None


    def _deserialize(self, params):
        self.TraceId = params.get("TraceId")
        self.BodyIds = params.get("BodyIds")