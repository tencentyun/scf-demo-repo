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


class AIAssistantRequest(AbstractModel):
    """AIAssistant請求參數結構體

    """

    def __init__(self):
        """
        :param FileContent: 輸入分析對象内容，輸入數據格式參考FileType參數釋義
        :type FileContent: str
        :param FileType: 輸入分析對象類型，picture_url:圖片網址，vod_url:視訊網址，live_url：直播網址，audio_url: 音訊文件，picture：圖片二進制數據的BASE64編碼
        :type FileType: str
        :param Lang: 音訊源的語言，預設0爲英文，1爲中文
        :type Lang: int
        :param LibrarySet: 查詢人員庫清單
        :type LibrarySet: list of str
        :param MaxVideoDuration: 視訊評估時間，單位秒，點播場景預設值爲2小時（無法探測長度時）或完整視訊，直播場景預設值爲10分鍾或直播提前結束
        :type MaxVideoDuration: int
        :param Template: 标準化範本選擇：0：AI助教基礎版本，1：AI評教基礎版本，2：AI評教标準版本。AI 助教基礎版本功能包括：人臉檢索、人臉檢測、人臉表情識别、學生動作選項，音訊訊息分析，微笑識别。AI 評教基礎版本功能包括：人臉檢索、人臉檢測、人臉表情識别、音訊訊息分析。AI 評教标準版功能包括人臉檢索、人臉檢測、人臉表情識别、手勢識别、音訊訊息分析、音訊關鍵詞分析、視訊精彩集錦分析。
        :type Template: int
        :param VocabLibNameList: 識别詞庫名清單，評估過程使用這些詞匯庫中的詞匯進行詞匯使用行爲分析
        :type VocabLibNameList: list of str
        :param VoiceEncodeType: 語音編碼類型 1:pcm
        :type VoiceEncodeType: int
        :param VoiceFileType: 語音文件類型 1:raw, 2:wav, 3:mp3，10:視訊（三種音訊格式目前僅支援16k采樣率16bit）
        :type VoiceFileType: int
        """
        self.FileContent = None
        self.FileType = None
        self.Lang = None
        self.LibrarySet = None
        self.MaxVideoDuration = None
        self.Template = None
        self.VocabLibNameList = None
        self.VoiceEncodeType = None
        self.VoiceFileType = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.FileType = params.get("FileType")
        self.Lang = params.get("Lang")
        self.LibrarySet = params.get("LibrarySet")
        self.MaxVideoDuration = params.get("MaxVideoDuration")
        self.Template = params.get("Template")
        self.VocabLibNameList = params.get("VocabLibNameList")
        self.VoiceEncodeType = params.get("VoiceEncodeType")
        self.VoiceFileType = params.get("VoiceFileType")


class AIAssistantResponse(AbstractModel):
    """AIAssistant返回參數結構體

    """

    def __init__(self):
        """
        :param ImageResults: 圖像任務直接返回結果
        :type ImageResults: list of ImageTaskResult
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ImageResults = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImageResults") is not None:
            self.ImageResults = []
            for item in params.get("ImageResults"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self.ImageResults.append(obj)
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ASRStat(AbstractModel):
    """當前音訊的統計結果

    """

    def __init__(self):
        """
        :param AvgSpeed: 當前音訊的平均語速
        :type AvgSpeed: float
        :param AvgVolume: Vad的平均音量
        :type AvgVolume: float
        :param MaxVolume: Vad的最大音量
        :type MaxVolume: float
        :param MinVolume: Vad的最小音量
        :type MinVolume: float
        :param MuteDuration: 當前音訊的非發音時長
        :type MuteDuration: int
        :param SoundDuration: 當前音訊的發音時長
        :type SoundDuration: int
        :param TotalDuration: 當前音訊的總時長
        :type TotalDuration: int
        :param VadNum: 當前音訊的句子總數
        :type VadNum: int
        :param WordNum: 當前音訊的單詞總數
        :type WordNum: int
        """
        self.AvgSpeed = None
        self.AvgVolume = None
        self.MaxVolume = None
        self.MinVolume = None
        self.MuteDuration = None
        self.SoundDuration = None
        self.TotalDuration = None
        self.VadNum = None
        self.WordNum = None


    def _deserialize(self, params):
        self.AvgSpeed = params.get("AvgSpeed")
        self.AvgVolume = params.get("AvgVolume")
        self.MaxVolume = params.get("MaxVolume")
        self.MinVolume = params.get("MinVolume")
        self.MuteDuration = params.get("MuteDuration")
        self.SoundDuration = params.get("SoundDuration")
        self.TotalDuration = params.get("TotalDuration")
        self.VadNum = params.get("VadNum")
        self.WordNum = params.get("WordNum")


class AbsenceInfo(AbstractModel):
    """缺勤人員訊息

    """

    def __init__(self):
        """
        :param LibraryIds: 識别到的人員所在的庫id
        :type LibraryIds: str
        :param PersonId: 識别到的人員id
        :type PersonId: str
        """
        self.LibraryIds = None
        self.PersonId = None


    def _deserialize(self, params):
        self.LibraryIds = params.get("LibraryIds")
        self.PersonId = params.get("PersonId")


class ActionCountStatistic(AbstractModel):
    """數量統計結果

    """

    def __init__(self):
        """
        :param Count: 數量
        :type Count: int
        :param Name: 名稱
        :type Name: str
        """
        self.Count = None
        self.Name = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.Name = params.get("Name")


class ActionDurationRatioStatistic(AbstractModel):
    """時長占比統計結果

    """

    def __init__(self):
        """
        :param Name: 名稱
        :type Name: str
        :param Ratio: 比例
        :type Ratio: float
        """
        self.Name = None
        self.Ratio = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Ratio = params.get("Ratio")


class ActionDurationStatistic(AbstractModel):
    """時長統計結果

    """

    def __init__(self):
        """
        :param Duration: 時長
        :type Duration: int
        :param Name: 名稱
        :type Name: str
        """
        self.Duration = None
        self.Name = None


    def _deserialize(self, params):
        self.Duration = params.get("Duration")
        self.Name = params.get("Name")


class ActionInfo(AbstractModel):
    """大教室場景肢體動作識别訊息

    """

    def __init__(self):
        """
        :param BodyPosture: 軀體動作識别結果，包含坐着（sit）、站立（stand）和趴睡（sleep）
        :type BodyPosture: :class:`tencentcloud.tci.v20190318.models.ActionType`
        :param Handup: 舉手識别結果，包含舉手（hand）和未檢測到舉手（nothand）
        :type Handup: :class:`tencentcloud.tci.v20190318.models.ActionType`
        :param LookHead: 是否低頭識别結果，包含擡頭（lookingahead）和未檢測到擡頭（notlookingahead）
        :type LookHead: :class:`tencentcloud.tci.v20190318.models.ActionType`
        :param Writing: 是否寫字識别結果，包含寫字（write）和未檢測到寫字（notlookingahead）
        :type Writing: :class:`tencentcloud.tci.v20190318.models.ActionType`
        :param Height: 動作圖像高度
        :type Height: int
        :param Left: 動作出現圖像的左側起始坐标位置
        :type Left: int
        :param Top: 動作出現圖像的上側起始側坐标位置
        :type Top: int
        :param Width: 動作圖像寬度
        :type Width: int
        """
        self.BodyPosture = None
        self.Handup = None
        self.LookHead = None
        self.Writing = None
        self.Height = None
        self.Left = None
        self.Top = None
        self.Width = None


    def _deserialize(self, params):
        if params.get("BodyPosture") is not None:
            self.BodyPosture = ActionType()
            self.BodyPosture._deserialize(params.get("BodyPosture"))
        if params.get("Handup") is not None:
            self.Handup = ActionType()
            self.Handup._deserialize(params.get("Handup"))
        if params.get("LookHead") is not None:
            self.LookHead = ActionType()
            self.LookHead._deserialize(params.get("LookHead"))
        if params.get("Writing") is not None:
            self.Writing = ActionType()
            self.Writing._deserialize(params.get("Writing"))
        self.Height = params.get("Height")
        self.Left = params.get("Left")
        self.Top = params.get("Top")
        self.Width = params.get("Width")


class ActionStatistic(AbstractModel):
    """統計結果

    """

    def __init__(self):
        """
        :param ActionCount: 數量統計
        :type ActionCount: list of ActionCountStatistic
        :param ActionDuration: 時長統計
        :type ActionDuration: list of ActionDurationStatistic
        :param ActionDurationRatio: 時長比例統計
        :type ActionDurationRatio: list of ActionDurationRatioStatistic
        """
        self.ActionCount = None
        self.ActionDuration = None
        self.ActionDurationRatio = None


    def _deserialize(self, params):
        if params.get("ActionCount") is not None:
            self.ActionCount = []
            for item in params.get("ActionCount"):
                obj = ActionCountStatistic()
                obj._deserialize(item)
                self.ActionCount.append(obj)
        if params.get("ActionDuration") is not None:
            self.ActionDuration = []
            for item in params.get("ActionDuration"):
                obj = ActionDurationStatistic()
                obj._deserialize(item)
                self.ActionDuration.append(obj)
        if params.get("ActionDurationRatio") is not None:
            self.ActionDurationRatio = []
            for item in params.get("ActionDurationRatio"):
                obj = ActionDurationRatioStatistic()
                obj._deserialize(item)
                self.ActionDurationRatio.append(obj)


class ActionType(AbstractModel):
    """動作行爲子類型

    """

    def __init__(self):
        """
        :param Confidence: 置信度
        :type Confidence: float
        :param Type: 動作類别
        :type Type: str
        """
        self.Confidence = None
        self.Type = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Type = params.get("Type")


class AllMuteSlice(AbstractModel):
    """如果請求中開啓了靜音檢測開關，則會返回所有的靜音片段（靜音時長超過阈值的片段）。

    """

    def __init__(self):
        """
        :param MuteSlice: 所有靜音片段。
        :type MuteSlice: list of MuteSlice
        :param MuteRatio: 靜音時長占比。
        :type MuteRatio: float
        :param TotalMuteDuration: 靜音總時長。
        :type TotalMuteDuration: int
        """
        self.MuteSlice = None
        self.MuteRatio = None
        self.TotalMuteDuration = None


    def _deserialize(self, params):
        if params.get("MuteSlice") is not None:
            self.MuteSlice = []
            for item in params.get("MuteSlice"):
                obj = MuteSlice()
                obj._deserialize(item)
                self.MuteSlice.append(obj)
        self.MuteRatio = params.get("MuteRatio")
        self.TotalMuteDuration = params.get("TotalMuteDuration")


class AttendanceInfo(AbstractModel):
    """識别到的人員訊息

    """

    def __init__(self):
        """
        :param Face: 識别到的人員訊息
        :type Face: :class:`tencentcloud.tci.v20190318.models.FrameInfo`
        :param PersonId: 識别到的人員id
        :type PersonId: str
        """
        self.Face = None
        self.PersonId = None


    def _deserialize(self, params):
        if params.get("Face") is not None:
            self.Face = FrameInfo()
            self.Face._deserialize(params.get("Face"))
        self.PersonId = params.get("PersonId")


class BodyMovementResult(AbstractModel):
    """老師肢體動作識别結果

    """

    def __init__(self):
        """
        :param Confidence: 置信度
        :type Confidence: float
        :param Height: 識别結果高度
        :type Height: int
        :param Left: 識别結果左坐标
        :type Left: int
        :param Movements: 老師動作識别結果，包含
1、teach_on_positive_attitude 正面講解
2、point_to_the_blackboard 指黑板
3、writing_blackboard 寫板書
4、other 其他
        :type Movements: str
        :param Top: 識别結果頂坐标
        :type Top: int
        :param Width: 識别結果寬度
        :type Width: int
        """
        self.Confidence = None
        self.Height = None
        self.Left = None
        self.Movements = None
        self.Top = None
        self.Width = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Height = params.get("Height")
        self.Left = params.get("Left")
        self.Movements = params.get("Movements")
        self.Top = params.get("Top")
        self.Width = params.get("Width")


class CancelTaskRequest(AbstractModel):
    """CancelTask請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 待取消任務标志符。
        :type JobId: int
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class CancelTaskResponse(AbstractModel):
    """CancelTask返回參數結構體

    """

    def __init__(self):
        """
        :param JobId: 取消任務标志符。
        :type JobId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class CheckFacePhotoRequest(AbstractModel):
    """CheckFacePhoto請求參數結構體

    """

    def __init__(self):
        """
        :param FileContent: 輸入分析對象内容
        :type FileContent: str
        :param FileType: 輸入分析對象類型，picture_url:圖片網址
        :type FileType: str
        """
        self.FileContent = None
        self.FileType = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.FileType = params.get("FileType")


class CheckFacePhotoResponse(AbstractModel):
    """CheckFacePhoto返回參數結構體

    """

    def __init__(self):
        """
        :param CheckResult: 人臉檢查結果，0：通過檢查，1：圖片模糊
        :type CheckResult: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CheckResult = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CheckResult = params.get("CheckResult")
        self.RequestId = params.get("RequestId")


class CreateFaceRequest(AbstractModel):
    """CreateFace請求參數結構體

    """

    def __init__(self):
        """
        :param PersonId: 人員唯一标識符
        :type PersonId: str
        :param Images: 圖片數據 base64 字串，與 Urls 參數選擇一個輸入
        :type Images: list of str
        :param LibraryId: 人員庫唯一标識符
        :type LibraryId: str
        :param Urls: 圖片下載網址，與 Images 參數選擇一個輸入
        :type Urls: list of str
        """
        self.PersonId = None
        self.Images = None
        self.LibraryId = None
        self.Urls = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Images = params.get("Images")
        self.LibraryId = params.get("LibraryId")
        self.Urls = params.get("Urls")


class CreateFaceResponse(AbstractModel):
    """CreateFace返回參數結構體

    """

    def __init__(self):
        """
        :param FaceInfoSet: 人臉操作結果訊息
        :type FaceInfoSet: list of FaceInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FaceInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FaceInfoSet") is not None:
            self.FaceInfoSet = []
            for item in params.get("FaceInfoSet"):
                obj = FaceInfo()
                obj._deserialize(item)
                self.FaceInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class CreateLibraryRequest(AbstractModel):
    """CreateLibrary請求參數結構體

    """

    def __init__(self):
        """
        :param LibraryName: 人員庫名稱
        :type LibraryName: str
        :param LibraryId: 人員庫唯一标志符，爲空則系統自動生成。
        :type LibraryId: str
        """
        self.LibraryName = None
        self.LibraryId = None


    def _deserialize(self, params):
        self.LibraryName = params.get("LibraryName")
        self.LibraryId = params.get("LibraryId")


class CreateLibraryResponse(AbstractModel):
    """CreateLibrary返回參數結構體

    """

    def __init__(self):
        """
        :param LibraryId: 人員庫唯一标識符
        :type LibraryId: str
        :param LibraryName: 人員庫名稱
        :type LibraryName: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.LibraryId = None
        self.LibraryName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")
        self.LibraryName = params.get("LibraryName")
        self.RequestId = params.get("RequestId")


class CreatePersonRequest(AbstractModel):
    """CreatePerson請求參數結構體

    """

    def __init__(self):
        """
        :param LibraryId: 人員庫唯一标識符
        :type LibraryId: str
        :param PersonName: 人員名稱
        :type PersonName: str
        :param Images: 圖片數據 base64 字串，與 Urls 參數選擇一個輸入
        :type Images: list of str
        :param JobNumber: 人員工作号碼
        :type JobNumber: str
        :param Mail: 人員電子信箱
        :type Mail: str
        :param Male: 人員性别，0：未知 1：男性，2：女性
        :type Male: int
        :param PersonId: 自定義人員 ID，注意不能使用 tci_person_ 前綴
        :type PersonId: str
        :param PhoneNumber: 人員電話号碼
        :type PhoneNumber: str
        :param StudentNumber: 人員學生号碼
        :type StudentNumber: str
        :param Urls: 圖片下載網址，與 Images 參數選擇一個輸入
        :type Urls: list of str
        """
        self.LibraryId = None
        self.PersonName = None
        self.Images = None
        self.JobNumber = None
        self.Mail = None
        self.Male = None
        self.PersonId = None
        self.PhoneNumber = None
        self.StudentNumber = None
        self.Urls = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")
        self.PersonName = params.get("PersonName")
        self.Images = params.get("Images")
        self.JobNumber = params.get("JobNumber")
        self.Mail = params.get("Mail")
        self.Male = params.get("Male")
        self.PersonId = params.get("PersonId")
        self.PhoneNumber = params.get("PhoneNumber")
        self.StudentNumber = params.get("StudentNumber")
        self.Urls = params.get("Urls")


class CreatePersonResponse(AbstractModel):
    """CreatePerson返回參數結構體

    """

    def __init__(self):
        """
        :param FaceInfoSet: 人臉操作結果訊息
        :type FaceInfoSet: list of FaceInfo
        :param LibraryId: 人員庫唯一标識符
        :type LibraryId: str
        :param PersonId: 人員唯一标識符
        :type PersonId: str
        :param PersonName: 人員名稱
        :type PersonName: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FaceInfoSet = None
        self.LibraryId = None
        self.PersonId = None
        self.PersonName = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FaceInfoSet") is not None:
            self.FaceInfoSet = []
            for item in params.get("FaceInfoSet"):
                obj = FaceInfo()
                obj._deserialize(item)
                self.FaceInfoSet.append(obj)
        self.LibraryId = params.get("LibraryId")
        self.PersonId = params.get("PersonId")
        self.PersonName = params.get("PersonName")
        self.RequestId = params.get("RequestId")


class CreateVocabLibRequest(AbstractModel):
    """CreateVocabLib請求參數結構體

    """

    def __init__(self):
        """
        :param VocabLibName: 詞匯庫名稱
        :type VocabLibName: str
        """
        self.VocabLibName = None


    def _deserialize(self, params):
        self.VocabLibName = params.get("VocabLibName")


class CreateVocabLibResponse(AbstractModel):
    """CreateVocabLib返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateVocabRequest(AbstractModel):
    """CreateVocab請求參數結構體

    """

    def __init__(self):
        """
        :param VocabLibName: 要添加詞匯的詞匯庫名
        :type VocabLibName: str
        :param VocabList: 要添加的詞匯清單
        :type VocabList: list of str
        """
        self.VocabLibName = None
        self.VocabList = None


    def _deserialize(self, params):
        self.VocabLibName = params.get("VocabLibName")
        self.VocabList = params.get("VocabList")


class CreateVocabResponse(AbstractModel):
    """CreateVocab返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteFaceRequest(AbstractModel):
    """DeleteFace請求參數結構體

    """

    def __init__(self):
        """
        :param FaceIdSet: 人臉标識符數組
        :type FaceIdSet: list of str
        :param PersonId: 人員唯一标識符
        :type PersonId: str
        :param LibraryId: 人員庫唯一标識符
        :type LibraryId: str
        """
        self.FaceIdSet = None
        self.PersonId = None
        self.LibraryId = None


    def _deserialize(self, params):
        self.FaceIdSet = params.get("FaceIdSet")
        self.PersonId = params.get("PersonId")
        self.LibraryId = params.get("LibraryId")


class DeleteFaceResponse(AbstractModel):
    """DeleteFace返回參數結構體

    """

    def __init__(self):
        """
        :param FaceInfoSet: 人臉操作結果
        :type FaceInfoSet: list of FaceInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FaceInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FaceInfoSet") is not None:
            self.FaceInfoSet = []
            for item in params.get("FaceInfoSet"):
                obj = FaceInfo()
                obj._deserialize(item)
                self.FaceInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DeleteLibraryRequest(AbstractModel):
    """DeleteLibrary請求參數結構體

    """

    def __init__(self):
        """
        :param LibraryId: 人員庫唯一标識符
        :type LibraryId: str
        """
        self.LibraryId = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")


class DeleteLibraryResponse(AbstractModel):
    """DeleteLibrary返回參數結構體

    """

    def __init__(self):
        """
        :param LibraryId: 人員庫唯一标識符
        :type LibraryId: str
        :param LibraryName: 人員庫名稱
        :type LibraryName: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.LibraryId = None
        self.LibraryName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")
        self.LibraryName = params.get("LibraryName")
        self.RequestId = params.get("RequestId")


class DeletePersonRequest(AbstractModel):
    """DeletePerson請求參數結構體

    """

    def __init__(self):
        """
        :param LibraryId: 人員庫唯一标識符
        :type LibraryId: str
        :param PersonId: 人員唯一标識符
        :type PersonId: str
        """
        self.LibraryId = None
        self.PersonId = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")
        self.PersonId = params.get("PersonId")


class DeletePersonResponse(AbstractModel):
    """DeletePerson返回參數結構體

    """

    def __init__(self):
        """
        :param FaceInfoSet: 人臉訊息
        :type FaceInfoSet: list of FaceInfo
        :param LibraryId: 人員庫唯一标識符
        :type LibraryId: str
        :param PersonId: 人員唯一标識符
        :type PersonId: str
        :param PersonName: 人員名稱
        :type PersonName: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FaceInfoSet = None
        self.LibraryId = None
        self.PersonId = None
        self.PersonName = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FaceInfoSet") is not None:
            self.FaceInfoSet = []
            for item in params.get("FaceInfoSet"):
                obj = FaceInfo()
                obj._deserialize(item)
                self.FaceInfoSet.append(obj)
        self.LibraryId = params.get("LibraryId")
        self.PersonId = params.get("PersonId")
        self.PersonName = params.get("PersonName")
        self.RequestId = params.get("RequestId")


class DeleteVocabLibRequest(AbstractModel):
    """DeleteVocabLib請求參數結構體

    """

    def __init__(self):
        """
        :param VocabLibName: 詞匯庫名稱
        :type VocabLibName: str
        """
        self.VocabLibName = None


    def _deserialize(self, params):
        self.VocabLibName = params.get("VocabLibName")


class DeleteVocabLibResponse(AbstractModel):
    """DeleteVocabLib返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteVocabRequest(AbstractModel):
    """DeleteVocab請求參數結構體

    """

    def __init__(self):
        """
        :param VocabLibName: 要删除詞匯的詞匯庫名
        :type VocabLibName: str
        :param VocabList: 要删除的詞匯清單
        :type VocabList: list of str
        """
        self.VocabLibName = None
        self.VocabList = None


    def _deserialize(self, params):
        self.VocabLibName = params.get("VocabLibName")
        self.VocabList = params.get("VocabList")


class DeleteVocabResponse(AbstractModel):
    """DeleteVocab返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAITaskResultRequest(AbstractModel):
    """DescribeAITaskResult請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務唯一标識符。在URL方式時提交請求後會返回一個任務标識符，後續查詢該url的結果時使用這個标識符進行查詢。
        :type TaskId: int
        :param Limit: 限制數目
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        """
        self.TaskId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeAITaskResultResponse(AbstractModel):
    """DescribeAITaskResult返回參數結構體

    """

    def __init__(self):
        """
        :param AudioResult: 音訊分析結果
        :type AudioResult: :class:`tencentcloud.tci.v20190318.models.StandardAudioResult`
        :param ImageResult: 圖像分析結果
        :type ImageResult: :class:`tencentcloud.tci.v20190318.models.StandardImageResult`
        :param VideoResult: 視訊分析結果
        :type VideoResult: :class:`tencentcloud.tci.v20190318.models.StandardVideoResult`
        :param Status: 任務狀态
        :type Status: str
        :param TaskId: 任務唯一id。在URL方式時提交請求後會返回一個jobid，後續查詢該url的結果時使用這個jobid進行查詢。
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AudioResult = None
        self.ImageResult = None
        self.VideoResult = None
        self.Status = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AudioResult") is not None:
            self.AudioResult = StandardAudioResult()
            self.AudioResult._deserialize(params.get("AudioResult"))
        if params.get("ImageResult") is not None:
            self.ImageResult = StandardImageResult()
            self.ImageResult._deserialize(params.get("ImageResult"))
        if params.get("VideoResult") is not None:
            self.VideoResult = StandardVideoResult()
            self.VideoResult._deserialize(params.get("VideoResult"))
        self.Status = params.get("Status")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DescribeAttendanceResultRequest(AbstractModel):
    """DescribeAttendanceResult請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 任務唯一标識符
        :type JobId: int
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class DescribeAttendanceResultResponse(AbstractModel):
    """DescribeAttendanceResult返回參數結構體

    """

    def __init__(self):
        """
        :param AbsenceSetInLibs: 缺失人員的ID清單(只針對請求中的libids欄位)
        :type AbsenceSetInLibs: list of AbsenceInfo
        :param AttendanceSet: 确定出勤人員清單
        :type AttendanceSet: list of AttendanceInfo
        :param SuspectedSet: 疑似出勤人員清單
        :type SuspectedSet: list of SuspectedInfo
        :param AbsenceSet: 缺失人員的ID清單(只針對請求中的personids欄位)
        :type AbsenceSet: list of str
        :param Progress: 請求處理進度
        :type Progress: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AbsenceSetInLibs = None
        self.AttendanceSet = None
        self.SuspectedSet = None
        self.AbsenceSet = None
        self.Progress = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AbsenceSetInLibs") is not None:
            self.AbsenceSetInLibs = []
            for item in params.get("AbsenceSetInLibs"):
                obj = AbsenceInfo()
                obj._deserialize(item)
                self.AbsenceSetInLibs.append(obj)
        if params.get("AttendanceSet") is not None:
            self.AttendanceSet = []
            for item in params.get("AttendanceSet"):
                obj = AttendanceInfo()
                obj._deserialize(item)
                self.AttendanceSet.append(obj)
        if params.get("SuspectedSet") is not None:
            self.SuspectedSet = []
            for item in params.get("SuspectedSet"):
                obj = SuspectedInfo()
                obj._deserialize(item)
                self.SuspectedSet.append(obj)
        self.AbsenceSet = params.get("AbsenceSet")
        self.Progress = params.get("Progress")
        self.RequestId = params.get("RequestId")


class DescribeAudioTaskRequest(AbstractModel):
    """DescribeAudioTask請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 音訊任務唯一id。在URL方式時提交請求後會返回一個jobid，後續查詢該url的結果時使用這個jobid進行查詢。
        :type JobId: int
        :param Limit: 限制數目
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        """
        self.JobId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeAudioTaskResponse(AbstractModel):
    """DescribeAudioTask返回參數結構體

    """

    def __init__(self):
        """
        :param AllMuteSlice: 如果請求中開啓了靜音檢測開關，則會返回所有的靜音片段（靜音時長超過阈值的片段）。
        :type AllMuteSlice: :class:`tencentcloud.tci.v20190318.models.AllMuteSlice`
        :param AsrStat: 返回的當前音訊的統計訊息。當進度爲100時返回。
        :type AsrStat: :class:`tencentcloud.tci.v20190318.models.ASRStat`
        :param Texts: 返回當前音訊流的詳細訊息，如果是流模式，返回的是對應流的詳細訊息，如果是 URL模式，返回的是查詢的那一段seq對應的音訊的詳細訊息。
        :type Texts: list of WholeTextItem
        :param VocabAnalysisDetailInfo: 返回詞匯庫中的單詞出現的詳細時間訊息。
        :type VocabAnalysisDetailInfo: list of VocabDetailInfomation
        :param VocabAnalysisStatInfo: 返回詞匯庫中的單詞出現的次數訊息。
        :type VocabAnalysisStatInfo: list of VocabStatInfomation
        :param AllTexts: 返回音訊全部文本。
        :type AllTexts: str
        :param JobId: 音訊任務唯一id。在URL方式時提交請求後會返回一個jobid，後續查詢該url的結果時使用這個jobid進行查詢。
        :type JobId: int
        :param Progress: 返回的當前處理進度。
        :type Progress: float
        :param TotalCount: 結果總數
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AllMuteSlice = None
        self.AsrStat = None
        self.Texts = None
        self.VocabAnalysisDetailInfo = None
        self.VocabAnalysisStatInfo = None
        self.AllTexts = None
        self.JobId = None
        self.Progress = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AllMuteSlice") is not None:
            self.AllMuteSlice = AllMuteSlice()
            self.AllMuteSlice._deserialize(params.get("AllMuteSlice"))
        if params.get("AsrStat") is not None:
            self.AsrStat = ASRStat()
            self.AsrStat._deserialize(params.get("AsrStat"))
        if params.get("Texts") is not None:
            self.Texts = []
            for item in params.get("Texts"):
                obj = WholeTextItem()
                obj._deserialize(item)
                self.Texts.append(obj)
        if params.get("VocabAnalysisDetailInfo") is not None:
            self.VocabAnalysisDetailInfo = []
            for item in params.get("VocabAnalysisDetailInfo"):
                obj = VocabDetailInfomation()
                obj._deserialize(item)
                self.VocabAnalysisDetailInfo.append(obj)
        if params.get("VocabAnalysisStatInfo") is not None:
            self.VocabAnalysisStatInfo = []
            for item in params.get("VocabAnalysisStatInfo"):
                obj = VocabStatInfomation()
                obj._deserialize(item)
                self.VocabAnalysisStatInfo.append(obj)
        self.AllTexts = params.get("AllTexts")
        self.JobId = params.get("JobId")
        self.Progress = params.get("Progress")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeConversationTaskRequest(AbstractModel):
    """DescribeConversationTask請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 音訊任務唯一id。在URL方式時提交請求後會返回一個jobid，後續查詢該url的結果時使用這個jobid進行查詢。
        :type JobId: int
        :param Identity: 要查詢明細的流的身份，1 老師 2 學生
        :type Identity: int
        :param Limit: 限制數目
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        """
        self.JobId = None
        self.Identity = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.Identity = params.get("Identity")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeConversationTaskResponse(AbstractModel):
    """DescribeConversationTask返回參數結構體

    """

    def __init__(self):
        """
        :param AsrStat: 返回的當前音訊的統計訊息。當進度爲100時返回。
        :type AsrStat: :class:`tencentcloud.tci.v20190318.models.ASRStat`
        :param Texts: 返回當前音訊流的詳細訊息，如果是流模式，返回的是對應流的詳細訊息，如果是 URL模式，返回的是查詢的那一段seq對應的音訊的詳細訊息。
        :type Texts: list of WholeTextItem
        :param VocabAnalysisDetailInfo: 返回詞匯庫中的單詞出現的詳細時間訊息。
        :type VocabAnalysisDetailInfo: list of VocabDetailInfomation
        :param VocabAnalysisStatInfo: 返回詞匯庫中的單詞出現的次數訊息。
        :type VocabAnalysisStatInfo: list of VocabStatInfomation
        :param AllTexts: 整個音訊流的全部文本
        :type AllTexts: str
        :param JobId: 音訊任務唯一id。在URL方式時提交請求後會返回一個jobid，後續查詢該url的結果時使用這個jobid進行查詢。
        :type JobId: int
        :param Progress: 返回的當前處理進度。
        :type Progress: float
        :param TotalCount: 結果總數
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AsrStat = None
        self.Texts = None
        self.VocabAnalysisDetailInfo = None
        self.VocabAnalysisStatInfo = None
        self.AllTexts = None
        self.JobId = None
        self.Progress = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AsrStat") is not None:
            self.AsrStat = ASRStat()
            self.AsrStat._deserialize(params.get("AsrStat"))
        if params.get("Texts") is not None:
            self.Texts = []
            for item in params.get("Texts"):
                obj = WholeTextItem()
                obj._deserialize(item)
                self.Texts.append(obj)
        if params.get("VocabAnalysisDetailInfo") is not None:
            self.VocabAnalysisDetailInfo = []
            for item in params.get("VocabAnalysisDetailInfo"):
                obj = VocabDetailInfomation()
                obj._deserialize(item)
                self.VocabAnalysisDetailInfo.append(obj)
        if params.get("VocabAnalysisStatInfo") is not None:
            self.VocabAnalysisStatInfo = []
            for item in params.get("VocabAnalysisStatInfo"):
                obj = VocabStatInfomation()
                obj._deserialize(item)
                self.VocabAnalysisStatInfo.append(obj)
        self.AllTexts = params.get("AllTexts")
        self.JobId = params.get("JobId")
        self.Progress = params.get("Progress")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeHighlightResultRequest(AbstractModel):
    """DescribeHighlightResult請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 精彩集錦任務唯一id。在URL方式時提交請求後會返回一個JobId，後續查詢該url的結果時使用這個JobId進行查詢。
        :type JobId: int
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class DescribeHighlightResultResponse(AbstractModel):
    """DescribeHighlightResult返回參數結構體

    """

    def __init__(self):
        """
        :param HighlightsInfo: 精彩集錦詳細訊息。
        :type HighlightsInfo: list of HighlightsInfomation
        :param JobId: 精彩集錦任務唯一id。在URL方式時提交請求後會返回一個JobId，後續查詢該url的結果時使用這個JobId進行查詢。
        :type JobId: int
        :param Progress: 任務的進度百分比，100表示任務已完成。
        :type Progress: float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.HighlightsInfo = None
        self.JobId = None
        self.Progress = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HighlightsInfo") is not None:
            self.HighlightsInfo = []
            for item in params.get("HighlightsInfo"):
                obj = HighlightsInfomation()
                obj._deserialize(item)
                self.HighlightsInfo.append(obj)
        self.JobId = params.get("JobId")
        self.Progress = params.get("Progress")
        self.RequestId = params.get("RequestId")


class DescribeImageTaskRequest(AbstractModel):
    """DescribeImageTask請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 任務标識符
        :type JobId: int
        :param Limit: 限制數目
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        """
        self.JobId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeImageTaskResponse(AbstractModel):
    """DescribeImageTask返回參數結構體

    """

    def __init__(self):
        """
        :param ResultSet: 任務處理結果
        :type ResultSet: list of ImageTaskResult
        :param JobId: 任務唯一标識
        :type JobId: int
        :param Progress: 任務執行進度
        :type Progress: int
        :param TotalCount: 任務結果數目
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ResultSet = None
        self.JobId = None
        self.Progress = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self.ResultSet.append(obj)
        self.JobId = params.get("JobId")
        self.Progress = params.get("Progress")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeImageTaskStatisticRequest(AbstractModel):
    """DescribeImageTaskStatistic請求參數結構體

    """

    def __init__(self):
        """
        :param JobId: 圖像任務标識符
        :type JobId: int
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class DescribeImageTaskStatisticResponse(AbstractModel):
    """DescribeImageTaskStatistic返回參數結構體

    """

    def __init__(self):
        """
        :param Statistic: 任務統計訊息
        :type Statistic: :class:`tencentcloud.tci.v20190318.models.ImageTaskStatistic`
        :param JobId: 圖像任務唯一标識符
        :type JobId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Statistic = None
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Statistic") is not None:
            self.Statistic = ImageTaskStatistic()
            self.Statistic._deserialize(params.get("Statistic"))
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class DescribeLibrariesRequest(AbstractModel):
    """DescribeLibraries請求參數結構體

    """


class DescribeLibrariesResponse(AbstractModel):
    """DescribeLibraries返回參數結構體

    """

    def __init__(self):
        """
        :param LibrarySet: 人員庫清單
        :type LibrarySet: list of Library
        :param TotalCount: 人員庫總數量
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.LibrarySet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LibrarySet") is not None:
            self.LibrarySet = []
            for item in params.get("LibrarySet"):
                obj = Library()
                obj._deserialize(item)
                self.LibrarySet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribePersonRequest(AbstractModel):
    """DescribePerson請求參數結構體

    """

    def __init__(self):
        """
        :param LibraryId: 人員庫唯一标識符
        :type LibraryId: str
        :param PersonId: 人員唯一标識符
        :type PersonId: str
        """
        self.LibraryId = None
        self.PersonId = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")
        self.PersonId = params.get("PersonId")


class DescribePersonResponse(AbstractModel):
    """DescribePerson返回參數結構體

    """

    def __init__(self):
        """
        :param FaceSet: 人員人臉清單
        :type FaceSet: list of Face
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param JobNumber: 工作号碼
        :type JobNumber: str
        :param LibraryId: 人員庫唯一标識符
        :type LibraryId: str
        :param Mail: 電子信箱
        :type Mail: str
        :param Male: 性别
        :type Male: int
        :param PersonId: 人員唯一标識符
        :type PersonId: str
        :param PersonName: 人員名稱
        :type PersonName: str
        :param PhoneNumber: 電話号碼
        :type PhoneNumber: str
        :param StudentNumber: 學生号碼
        :type StudentNumber: str
        :param UpdateTime: 修改時間
        :type UpdateTime: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FaceSet = None
        self.CreateTime = None
        self.JobNumber = None
        self.LibraryId = None
        self.Mail = None
        self.Male = None
        self.PersonId = None
        self.PersonName = None
        self.PhoneNumber = None
        self.StudentNumber = None
        self.UpdateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FaceSet") is not None:
            self.FaceSet = []
            for item in params.get("FaceSet"):
                obj = Face()
                obj._deserialize(item)
                self.FaceSet.append(obj)
        self.CreateTime = params.get("CreateTime")
        self.JobNumber = params.get("JobNumber")
        self.LibraryId = params.get("LibraryId")
        self.Mail = params.get("Mail")
        self.Male = params.get("Male")
        self.PersonId = params.get("PersonId")
        self.PersonName = params.get("PersonName")
        self.PhoneNumber = params.get("PhoneNumber")
        self.StudentNumber = params.get("StudentNumber")
        self.UpdateTime = params.get("UpdateTime")
        self.RequestId = params.get("RequestId")


class DescribePersonsRequest(AbstractModel):
    """DescribePersons請求參數結構體

    """

    def __init__(self):
        """
        :param LibraryId: 人員庫唯一标識符
        :type LibraryId: str
        :param Limit: 限制數目
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        """
        self.LibraryId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribePersonsResponse(AbstractModel):
    """DescribePersons返回參數結構體

    """

    def __init__(self):
        """
        :param PersonSet: 人員清單
        :type PersonSet: list of Person
        :param TotalCount: 人員總數
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PersonSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PersonSet") is not None:
            self.PersonSet = []
            for item in params.get("PersonSet"):
                obj = Person()
                obj._deserialize(item)
                self.PersonSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeVocabLibRequest(AbstractModel):
    """DescribeVocabLib請求參數結構體

    """


class DescribeVocabLibResponse(AbstractModel):
    """DescribeVocabLib返回參數結構體

    """

    def __init__(self):
        """
        :param VocabLibNameSet: 返回該appid下的所有詞匯庫名
        :type VocabLibNameSet: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.VocabLibNameSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VocabLibNameSet = params.get("VocabLibNameSet")
        self.RequestId = params.get("RequestId")


class DescribeVocabRequest(AbstractModel):
    """DescribeVocab請求參數結構體

    """

    def __init__(self):
        """
        :param VocabLibName: 要查詢詞匯的詞匯庫名
        :type VocabLibName: str
        """
        self.VocabLibName = None


    def _deserialize(self, params):
        self.VocabLibName = params.get("VocabLibName")


class DescribeVocabResponse(AbstractModel):
    """DescribeVocab返回參數結構體

    """

    def __init__(self):
        """
        :param VocabNameSet: 詞匯清單
        :type VocabNameSet: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.VocabNameSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VocabNameSet = params.get("VocabNameSet")
        self.RequestId = params.get("RequestId")


class DetailInfo(AbstractModel):
    """單詞出現的那個句子的起始時間和結束時間訊息

    """

    def __init__(self):
        """
        :param Value: 單詞出現在該音訊中的那個句子的時間戳，出現了幾次， 就返回對應次數的起始和結束時間戳
        :type Value: list of WordTimePair
        :param Keyword: 詞匯庫中的單詞
        :type Keyword: str
        """
        self.Value = None
        self.Keyword = None


    def _deserialize(self, params):
        if params.get("Value") is not None:
            self.Value = []
            for item in params.get("Value"):
                obj = WordTimePair()
                obj._deserialize(item)
                self.Value.append(obj)
        self.Keyword = params.get("Keyword")


class DoubleVideoFunction(AbstractModel):
    """雙路混流視訊集錦開關項

    """

    def __init__(self):
        """
        :param EnableCoverPictures: 片頭片尾增加圖片開關
        :type EnableCoverPictures: bool
        """
        self.EnableCoverPictures = None


    def _deserialize(self, params):
        self.EnableCoverPictures = params.get("EnableCoverPictures")


class ExpressRatioStatistic(AbstractModel):
    """表情比例統計

    """

    def __init__(self):
        """
        :param Count: 出現次數
        :type Count: int
        :param Express: 表情
        :type Express: str
        :param Ratio: 該表情時長占所有表情時長的比例
        :type Ratio: float
        :param RatioUseDuration: 該表情時長占視訊總時長的比例
        :type RatioUseDuration: float
        """
        self.Count = None
        self.Express = None
        self.Ratio = None
        self.RatioUseDuration = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.Express = params.get("Express")
        self.Ratio = params.get("Ratio")
        self.RatioUseDuration = params.get("RatioUseDuration")


class Face(AbstractModel):
    """人臉描述

    """

    def __init__(self):
        """
        :param FaceId: 人臉唯一标識符
        :type FaceId: str
        :param FaceUrl: 人臉圖片 URL
        :type FaceUrl: str
        :param PersonId: 人員唯一标識符
        :type PersonId: str
        """
        self.FaceId = None
        self.FaceUrl = None
        self.PersonId = None


    def _deserialize(self, params):
        self.FaceId = params.get("FaceId")
        self.FaceUrl = params.get("FaceUrl")
        self.PersonId = params.get("PersonId")


class FaceAttrResult(AbstractModel):
    """FaceAttrResult

    """

    def __init__(self):
        """
        :param Age: 年齡
        :type Age: int
        :param Sex: 性别
        :type Sex: str
        """
        self.Age = None
        self.Sex = None


    def _deserialize(self, params):
        self.Age = params.get("Age")
        self.Sex = params.get("Sex")


class FaceDetectStatistic(AbstractModel):
    """人臉監測統計訊息

    """

    def __init__(self):
        """
        :param FaceSizeRatio: 人臉大小占畫面平均占比
        :type FaceSizeRatio: float
        :param FrontalFaceCount: 檢測到正臉次數
        :type FrontalFaceCount: int
        :param FrontalFaceRatio: 正臉時長占比
        :type FrontalFaceRatio: float
        :param FrontalFaceRealRatio: 正臉時長在總出現時常占比
        :type FrontalFaceRealRatio: float
        :param PersonId: 人員唯一标識符
        :type PersonId: str
        :param SideFaceCount: 檢測到側臉次數
        :type SideFaceCount: int
        :param SideFaceRatio: 側臉時長占比
        :type SideFaceRatio: float
        :param SideFaceRealRatio: 側臉時長在總出現時常占比
        :type SideFaceRealRatio: float
        """
        self.FaceSizeRatio = None
        self.FrontalFaceCount = None
        self.FrontalFaceRatio = None
        self.FrontalFaceRealRatio = None
        self.PersonId = None
        self.SideFaceCount = None
        self.SideFaceRatio = None
        self.SideFaceRealRatio = None


    def _deserialize(self, params):
        self.FaceSizeRatio = params.get("FaceSizeRatio")
        self.FrontalFaceCount = params.get("FrontalFaceCount")
        self.FrontalFaceRatio = params.get("FrontalFaceRatio")
        self.FrontalFaceRealRatio = params.get("FrontalFaceRealRatio")
        self.PersonId = params.get("PersonId")
        self.SideFaceCount = params.get("SideFaceCount")
        self.SideFaceRatio = params.get("SideFaceRatio")
        self.SideFaceRealRatio = params.get("SideFaceRealRatio")


class FaceExpressStatistic(AbstractModel):
    """人臉表情統計結果

    """

    def __init__(self):
        """
        :param PersonId: 人員唯一标識符
        :type PersonId: str
        :param ExpressRatio: 表情統計結果
        :type ExpressRatio: list of ExpressRatioStatistic
        """
        self.PersonId = None
        self.ExpressRatio = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        if params.get("ExpressRatio") is not None:
            self.ExpressRatio = []
            for item in params.get("ExpressRatio"):
                obj = ExpressRatioStatistic()
                obj._deserialize(item)
                self.ExpressRatio.append(obj)


class FaceExpressionResult(AbstractModel):
    """FaceExpressionResult

    """

    def __init__(self):
        """
        :param Confidence: 表情置信度
        :type Confidence: float
        :param Expression: 表情識别結果，包括"neutral":中性,"happiness":開心，"angry":"生氣"，"disgust":厭惡，"fear":"恐懼"，"sadness":"悲傷"，"surprise":"驚訝"，"contempt":"蔑視"
        :type Expression: str
        """
        self.Confidence = None
        self.Expression = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Expression = params.get("Expression")


class FaceIdentifyResult(AbstractModel):
    """FaceIdentifyResult

    """

    def __init__(self):
        """
        :param FaceId: 人臉标識符
        :type FaceId: str
        :param LibraryId: 人員庫标識符
        :type LibraryId: str
        :param PersonId: 人員标識符
        :type PersonId: str
        :param Similarity: 相似度
        :type Similarity: float
        """
        self.FaceId = None
        self.LibraryId = None
        self.PersonId = None
        self.Similarity = None


    def _deserialize(self, params):
        self.FaceId = params.get("FaceId")
        self.LibraryId = params.get("LibraryId")
        self.PersonId = params.get("PersonId")
        self.Similarity = params.get("Similarity")


class FaceIdentifyStatistic(AbstractModel):
    """人員檢索統計結果

    """

    def __init__(self):
        """
        :param Duration: 持續時間
        :type Duration: int
        :param EndTs: 結束時間
        :type EndTs: int
        :param PersonId: 人員唯一标識符
        :type PersonId: str
        :param Similarity: 相似度
        :type Similarity: float
        :param StartTs: 開始時間
        :type StartTs: int
        """
        self.Duration = None
        self.EndTs = None
        self.PersonId = None
        self.Similarity = None
        self.StartTs = None


    def _deserialize(self, params):
        self.Duration = params.get("Duration")
        self.EndTs = params.get("EndTs")
        self.PersonId = params.get("PersonId")
        self.Similarity = params.get("Similarity")
        self.StartTs = params.get("StartTs")


class FaceInfo(AbstractModel):
    """人臉操作訊息

    """

    def __init__(self):
        """
        :param ErrorCode: 人臉操作錯誤碼
        :type ErrorCode: str
        :param ErrorMsg: 人臉操作結果訊息
        :type ErrorMsg: str
        :param FaceId: 人臉唯一标識符
        :type FaceId: str
        :param FaceUrl: 人臉保存網址
        :type FaceUrl: str
        :param PersonId: 人員唯一标識
        :type PersonId: str
        """
        self.ErrorCode = None
        self.ErrorMsg = None
        self.FaceId = None
        self.FaceUrl = None
        self.PersonId = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.ErrorMsg = params.get("ErrorMsg")
        self.FaceId = params.get("FaceId")
        self.FaceUrl = params.get("FaceUrl")
        self.PersonId = params.get("PersonId")


class FaceInfoResult(AbstractModel):
    """FaceInfoResult

    """

    def __init__(self):
        """
        :param FaceRatio: 人臉尺寸的占比
        :type FaceRatio: float
        :param FrameHeight: 幀高度
        :type FrameHeight: int
        :param FrameWidth: 幀寬度
        :type FrameWidth: int
        :param Height: 人臉高度
        :type Height: int
        :param Left: 人臉左坐标
        :type Left: int
        :param Top: 人臉頂坐标
        :type Top: int
        :param Width: 人臉寬度
        :type Width: int
        """
        self.FaceRatio = None
        self.FrameHeight = None
        self.FrameWidth = None
        self.Height = None
        self.Left = None
        self.Top = None
        self.Width = None


    def _deserialize(self, params):
        self.FaceRatio = params.get("FaceRatio")
        self.FrameHeight = params.get("FrameHeight")
        self.FrameWidth = params.get("FrameWidth")
        self.Height = params.get("Height")
        self.Left = params.get("Left")
        self.Top = params.get("Top")
        self.Width = params.get("Width")


class FacePoseResult(AbstractModel):
    """FacePoseResult

    """

    def __init__(self):
        """
        :param Direction: 正臉或側臉的訊息
        :type Direction: str
        :param Pitch: 圍繞Z軸旋轉角度，俯仰角
        :type Pitch: float
        :param Roll: 圍繞X軸旋轉角度，翻滾角
        :type Roll: float
        :param Yaw: 圍繞Y軸旋轉角度，偏航角
        :type Yaw: float
        """
        self.Direction = None
        self.Pitch = None
        self.Roll = None
        self.Yaw = None


    def _deserialize(self, params):
        self.Direction = params.get("Direction")
        self.Pitch = params.get("Pitch")
        self.Roll = params.get("Roll")
        self.Yaw = params.get("Yaw")


class FrameInfo(AbstractModel):
    """人員訊息

    """

    def __init__(self):
        """
        :param Similarity: 相似度
        :type Similarity: float
        :param SnapshotUrl: 截圖的儲存網址
        :type SnapshotUrl: str
        :param Ts: 相對于視訊起始時間的時間戳，單位秒
        :type Ts: int
        """
        self.Similarity = None
        self.SnapshotUrl = None
        self.Ts = None


    def _deserialize(self, params):
        self.Similarity = params.get("Similarity")
        self.SnapshotUrl = params.get("SnapshotUrl")
        self.Ts = params.get("Ts")


class Function(AbstractModel):
    """功能開關清單，表示是否需要打開相應的功能，返回相應的訊息

    """

    def __init__(self):
        """
        :param EnableAllText: 輸出全部文本标識，當該值設置爲true時，會輸出當前音訊的全部文本
        :type EnableAllText: bool
        :param EnableKeyword: 輸出關鍵詞訊息标識，當該值設置爲true時，會輸出當前音訊的關鍵詞訊息。
        :type EnableKeyword: bool
        :param EnableMuteDetect: 靜音檢測标識，當設置爲 true 時，需要設置靜音時間阈值欄位mute_threshold，統計結果中會返回靜音片段。
        :type EnableMuteDetect: bool
        :param EnableVadInfo: 輸出音訊統計訊息标識，當設置爲 true 時，任務查詢結果會輸出音訊的統計訊息（AsrStat）
        :type EnableVadInfo: bool
        :param EnableVolume: 輸出音訊音量訊息标識，當設置爲 true 時，會輸出當前音訊音量訊息。
        :type EnableVolume: bool
        """
        self.EnableAllText = None
        self.EnableKeyword = None
        self.EnableMuteDetect = None
        self.EnableVadInfo = None
        self.EnableVolume = None


    def _deserialize(self, params):
        self.EnableAllText = params.get("EnableAllText")
        self.EnableKeyword = params.get("EnableKeyword")
        self.EnableMuteDetect = params.get("EnableMuteDetect")
        self.EnableVadInfo = params.get("EnableVadInfo")
        self.EnableVolume = params.get("EnableVolume")


class GestureResult(AbstractModel):
    """GestureResult

    """

    def __init__(self):
        """
        :param Class: 識别結果，包含"USPEAK":聽你說，"LISTEN":聽我說，"GOOD":GOOD，"TOOLS":拿教具，"OTHERS":其他
        :type Class: str
        :param Confidence: 置信度
        :type Confidence: float
        :param Height: 識别結果高度
        :type Height: int
        :param Left: 識别結果左坐标
        :type Left: int
        :param Top: 識别結果頂坐标
        :type Top: int
        :param Width: 識别結果寬度
        :type Width: int
        """
        self.Class = None
        self.Confidence = None
        self.Height = None
        self.Left = None
        self.Top = None
        self.Width = None


    def _deserialize(self, params):
        self.Class = params.get("Class")
        self.Confidence = params.get("Confidence")
        self.Height = params.get("Height")
        self.Left = params.get("Left")
        self.Top = params.get("Top")
        self.Width = params.get("Width")


class HLFunction(AbstractModel):
    """檢索配置開關項

    """

    def __init__(self):
        """
        :param EnableFaceDetect: 是否開啓人臉檢測
        :type EnableFaceDetect: bool
        :param EnableFaceExpression: 是否開啓表情識别
        :type EnableFaceExpression: bool
        :param EnableFaceIdent: 是否開啓人臉檢索
        :type EnableFaceIdent: bool
        :param EnableKeywordWonderfulTime: 是否開啓視訊集錦-老師關鍵字識别
        :type EnableKeywordWonderfulTime: bool
        :param EnableSmileWonderfulTime: 是否開啓視訊集錦-微笑識别
        :type EnableSmileWonderfulTime: bool
        """
        self.EnableFaceDetect = None
        self.EnableFaceExpression = None
        self.EnableFaceIdent = None
        self.EnableKeywordWonderfulTime = None
        self.EnableSmileWonderfulTime = None


    def _deserialize(self, params):
        self.EnableFaceDetect = params.get("EnableFaceDetect")
        self.EnableFaceExpression = params.get("EnableFaceExpression")
        self.EnableFaceIdent = params.get("EnableFaceIdent")
        self.EnableKeywordWonderfulTime = params.get("EnableKeywordWonderfulTime")
        self.EnableSmileWonderfulTime = params.get("EnableSmileWonderfulTime")


class HandTrackingResult(AbstractModel):
    """HandTrackingResult

    """

    def __init__(self):
        """
        :param Class: 識别結果
        :type Class: str
        :param Confidence: 置信度
        :type Confidence: float
        :param Height: 識别結果高度
        :type Height: int
        :param Left: 識别結果左坐标
        :type Left: int
        :param Top: 識别結果頂坐标
        :type Top: int
        :param Width: 識别結果寬度
        :type Width: int
        """
        self.Class = None
        self.Confidence = None
        self.Height = None
        self.Left = None
        self.Top = None
        self.Width = None


    def _deserialize(self, params):
        self.Class = params.get("Class")
        self.Confidence = params.get("Confidence")
        self.Height = params.get("Height")
        self.Left = params.get("Left")
        self.Top = params.get("Top")
        self.Width = params.get("Width")


class HighlightsInfomation(AbstractModel):
    """精彩集錦訊息

    """

    def __init__(self):
        """
        :param Concentration: 專注的起始與終止時間訊息。
        :type Concentration: list of TimeType
        :param Smile: 微笑的起始與終止時間訊息。
        :type Smile: list of TimeType
        :param HighlightsUrl: 高光集錦視訊網址，保存剪輯好的視訊網址。
        :type HighlightsUrl: str
        :param PersonId: 片段中識别出來的人臉ID。
        :type PersonId: str
        """
        self.Concentration = None
        self.Smile = None
        self.HighlightsUrl = None
        self.PersonId = None


    def _deserialize(self, params):
        if params.get("Concentration") is not None:
            self.Concentration = []
            for item in params.get("Concentration"):
                obj = TimeType()
                obj._deserialize(item)
                self.Concentration.append(obj)
        if params.get("Smile") is not None:
            self.Smile = []
            for item in params.get("Smile"):
                obj = TimeType()
                obj._deserialize(item)
                self.Smile.append(obj)
        self.HighlightsUrl = params.get("HighlightsUrl")
        self.PersonId = params.get("PersonId")


class ImageTaskFunction(AbstractModel):
    """圖像任務控制選項

    """

    def __init__(self):
        """
        :param EnableActionClass: 大教室場景學生肢體動作識别選項
        :type EnableActionClass: bool
        :param EnableFaceDetect: 人臉檢測選項（預設爲true，目前不可編輯）
        :type EnableFaceDetect: bool
        :param EnableFaceExpression: 人臉表情識别選項
        :type EnableFaceExpression: bool
        :param EnableFaceIdentify: 人臉檢索選項（預設爲true，目前不可編輯）
        :type EnableFaceIdentify: bool
        :param EnableGesture: 手勢選項
        :type EnableGesture: bool
        :param EnableHandTracking: 優圖手勢選項（該功能尚未支援）
        :type EnableHandTracking: bool
        :param EnableLightJudge: 光照選項
        :type EnableLightJudge: bool
        :param EnableStudentBodyMovements: 小班課場景學生肢體動作識别選項
        :type EnableStudentBodyMovements: bool
        :param EnableTeacherBodyMovements: 教師動作選項（該功能尚未支援）
        :type EnableTeacherBodyMovements: bool
        :param EnableTeacherOutScreen: 判斷老師是否在螢幕中（該功能尚未支援）
        :type EnableTeacherOutScreen: bool
        """
        self.EnableActionClass = None
        self.EnableFaceDetect = None
        self.EnableFaceExpression = None
        self.EnableFaceIdentify = None
        self.EnableGesture = None
        self.EnableHandTracking = None
        self.EnableLightJudge = None
        self.EnableStudentBodyMovements = None
        self.EnableTeacherBodyMovements = None
        self.EnableTeacherOutScreen = None


    def _deserialize(self, params):
        self.EnableActionClass = params.get("EnableActionClass")
        self.EnableFaceDetect = params.get("EnableFaceDetect")
        self.EnableFaceExpression = params.get("EnableFaceExpression")
        self.EnableFaceIdentify = params.get("EnableFaceIdentify")
        self.EnableGesture = params.get("EnableGesture")
        self.EnableHandTracking = params.get("EnableHandTracking")
        self.EnableLightJudge = params.get("EnableLightJudge")
        self.EnableStudentBodyMovements = params.get("EnableStudentBodyMovements")
        self.EnableTeacherBodyMovements = params.get("EnableTeacherBodyMovements")
        self.EnableTeacherOutScreen = params.get("EnableTeacherOutScreen")


class ImageTaskResult(AbstractModel):
    """圖像任務結果

    """

    def __init__(self):
        """
        :param ActionInfo: 大教室場景學生肢體動作識别訊息
        :type ActionInfo: :class:`tencentcloud.tci.v20190318.models.ActionInfo`
        :param FaceAttr: 屬性識别結果
        :type FaceAttr: :class:`tencentcloud.tci.v20190318.models.FaceAttrResult`
        :param FaceExpression: 表情識别結果
        :type FaceExpression: :class:`tencentcloud.tci.v20190318.models.FaceExpressionResult`
        :param FaceIdentify: 人臉檢索結果
        :type FaceIdentify: :class:`tencentcloud.tci.v20190318.models.FaceIdentifyResult`
        :param FaceInfo: 人臉檢測結果
        :type FaceInfo: :class:`tencentcloud.tci.v20190318.models.FaceInfoResult`
        :param FacePose: 姿勢識别結果
        :type FacePose: :class:`tencentcloud.tci.v20190318.models.FacePoseResult`
        :param Gesture: 動作分類結果
        :type Gesture: :class:`tencentcloud.tci.v20190318.models.GestureResult`
        :param HandTracking: 手勢分類結果
        :type HandTracking: :class:`tencentcloud.tci.v20190318.models.HandTrackingResult`
        :param Light: 光照識别結果
        :type Light: :class:`tencentcloud.tci.v20190318.models.LightResult`
        :param StudentBodyMovement: 學生肢體動作識别結果
        :type StudentBodyMovement: :class:`tencentcloud.tci.v20190318.models.StudentBodyMovementResult`
        :param TeacherBodyMovement: 老師肢體動作識别結果
        :type TeacherBodyMovement: :class:`tencentcloud.tci.v20190318.models.BodyMovementResult`
        :param TeacherOutScreen: 教師是否在螢幕内判斷結果
        :type TeacherOutScreen: :class:`tencentcloud.tci.v20190318.models.TeacherOutScreenResult`
        :param TimeInfo: 時間統計結果
        :type TimeInfo: :class:`tencentcloud.tci.v20190318.models.TimeInfoResult`
        """
        self.ActionInfo = None
        self.FaceAttr = None
        self.FaceExpression = None
        self.FaceIdentify = None
        self.FaceInfo = None
        self.FacePose = None
        self.Gesture = None
        self.HandTracking = None
        self.Light = None
        self.StudentBodyMovement = None
        self.TeacherBodyMovement = None
        self.TeacherOutScreen = None
        self.TimeInfo = None


    def _deserialize(self, params):
        if params.get("ActionInfo") is not None:
            self.ActionInfo = ActionInfo()
            self.ActionInfo._deserialize(params.get("ActionInfo"))
        if params.get("FaceAttr") is not None:
            self.FaceAttr = FaceAttrResult()
            self.FaceAttr._deserialize(params.get("FaceAttr"))
        if params.get("FaceExpression") is not None:
            self.FaceExpression = FaceExpressionResult()
            self.FaceExpression._deserialize(params.get("FaceExpression"))
        if params.get("FaceIdentify") is not None:
            self.FaceIdentify = FaceIdentifyResult()
            self.FaceIdentify._deserialize(params.get("FaceIdentify"))
        if params.get("FaceInfo") is not None:
            self.FaceInfo = FaceInfoResult()
            self.FaceInfo._deserialize(params.get("FaceInfo"))
        if params.get("FacePose") is not None:
            self.FacePose = FacePoseResult()
            self.FacePose._deserialize(params.get("FacePose"))
        if params.get("Gesture") is not None:
            self.Gesture = GestureResult()
            self.Gesture._deserialize(params.get("Gesture"))
        if params.get("HandTracking") is not None:
            self.HandTracking = HandTrackingResult()
            self.HandTracking._deserialize(params.get("HandTracking"))
        if params.get("Light") is not None:
            self.Light = LightResult()
            self.Light._deserialize(params.get("Light"))
        if params.get("StudentBodyMovement") is not None:
            self.StudentBodyMovement = StudentBodyMovementResult()
            self.StudentBodyMovement._deserialize(params.get("StudentBodyMovement"))
        if params.get("TeacherBodyMovement") is not None:
            self.TeacherBodyMovement = BodyMovementResult()
            self.TeacherBodyMovement._deserialize(params.get("TeacherBodyMovement"))
        if params.get("TeacherOutScreen") is not None:
            self.TeacherOutScreen = TeacherOutScreenResult()
            self.TeacherOutScreen._deserialize(params.get("TeacherOutScreen"))
        if params.get("TimeInfo") is not None:
            self.TimeInfo = TimeInfoResult()
            self.TimeInfo._deserialize(params.get("TimeInfo"))


class ImageTaskStatistic(AbstractModel):
    """圖像任務統計結果

    """

    def __init__(self):
        """
        :param FaceDetect: 人員檢測統計訊息
        :type FaceDetect: list of FaceDetectStatistic
        :param FaceExpression: 人臉表情統計訊息
        :type FaceExpression: list of FaceExpressStatistic
        :param FaceIdentify: 人臉檢索統計訊息
        :type FaceIdentify: list of FaceIdentifyStatistic
        :param Gesture: 姿勢識别統計訊息
        :type Gesture: :class:`tencentcloud.tci.v20190318.models.ActionStatistic`
        :param Handtracking: 手勢識别統計訊息
        :type Handtracking: :class:`tencentcloud.tci.v20190318.models.ActionStatistic`
        :param Light: 光照統計訊息
        :type Light: :class:`tencentcloud.tci.v20190318.models.LightStatistic`
        :param StudentMovement: 學生動作統計訊息
        :type StudentMovement: :class:`tencentcloud.tci.v20190318.models.ActionStatistic`
        :param TeacherMovement: 教師動作統計訊息
        :type TeacherMovement: :class:`tencentcloud.tci.v20190318.models.ActionStatistic`
        """
        self.FaceDetect = None
        self.FaceExpression = None
        self.FaceIdentify = None
        self.Gesture = None
        self.Handtracking = None
        self.Light = None
        self.StudentMovement = None
        self.TeacherMovement = None


    def _deserialize(self, params):
        if params.get("FaceDetect") is not None:
            self.FaceDetect = []
            for item in params.get("FaceDetect"):
                obj = FaceDetectStatistic()
                obj._deserialize(item)
                self.FaceDetect.append(obj)
        if params.get("FaceExpression") is not None:
            self.FaceExpression = []
            for item in params.get("FaceExpression"):
                obj = FaceExpressStatistic()
                obj._deserialize(item)
                self.FaceExpression.append(obj)
        if params.get("FaceIdentify") is not None:
            self.FaceIdentify = []
            for item in params.get("FaceIdentify"):
                obj = FaceIdentifyStatistic()
                obj._deserialize(item)
                self.FaceIdentify.append(obj)
        if params.get("Gesture") is not None:
            self.Gesture = ActionStatistic()
            self.Gesture._deserialize(params.get("Gesture"))
        if params.get("Handtracking") is not None:
            self.Handtracking = ActionStatistic()
            self.Handtracking._deserialize(params.get("Handtracking"))
        if params.get("Light") is not None:
            self.Light = LightStatistic()
            self.Light._deserialize(params.get("Light"))
        if params.get("StudentMovement") is not None:
            self.StudentMovement = ActionStatistic()
            self.StudentMovement._deserialize(params.get("StudentMovement"))
        if params.get("TeacherMovement") is not None:
            self.TeacherMovement = ActionStatistic()
            self.TeacherMovement._deserialize(params.get("TeacherMovement"))


class Library(AbstractModel):
    """人員庫描述

    """

    def __init__(self):
        """
        :param CreateTime: 人員庫創建時間
        :type CreateTime: str
        :param LibraryId: 人員庫唯一标識符
        :type LibraryId: str
        :param LibraryName: 人員庫名稱
        :type LibraryName: str
        :param PersonCount: 人員庫人員數量
        :type PersonCount: int
        :param UpdateTime: 人員庫修改時間
        :type UpdateTime: str
        """
        self.CreateTime = None
        self.LibraryId = None
        self.LibraryName = None
        self.PersonCount = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.LibraryId = params.get("LibraryId")
        self.LibraryName = params.get("LibraryName")
        self.PersonCount = params.get("PersonCount")
        self.UpdateTime = params.get("UpdateTime")


class LightDistributionStatistic(AbstractModel):
    """光照強度統計結果

    """

    def __init__(self):
        """
        :param Time: 時間點
        :type Time: int
        :param Value: 光線值
        :type Value: int
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")


class LightLevelRatioStatistic(AbstractModel):
    """光照強度比例統計結果

    """

    def __init__(self):
        """
        :param Level: 名稱
        :type Level: str
        :param Ratio: 比例
        :type Ratio: float
        """
        self.Level = None
        self.Ratio = None


    def _deserialize(self, params):
        self.Level = params.get("Level")
        self.Ratio = params.get("Ratio")


class LightResult(AbstractModel):
    """LightResult

    """

    def __init__(self):
        """
        :param LightLevel: 光照程度，參考提交任務時的LightStandard指定的Name參數
        :type LightLevel: str
        :param LightValue: 光照亮度
        :type LightValue: float
        """
        self.LightLevel = None
        self.LightValue = None


    def _deserialize(self, params):
        self.LightLevel = params.get("LightLevel")
        self.LightValue = params.get("LightValue")


class LightStandard(AbstractModel):
    """光照标準，結構的相關範例爲：
    {
        "Name":"dark"，
        "Range":[0,30]
    }
    當光照的區間落入在0到30的範圍時，就會命中dark的光照标準

    """

    def __init__(self):
        """
        :param Name: 光照名稱
        :type Name: str
        :param Range: 範圍
        :type Range: list of float
        """
        self.Name = None
        self.Range = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Range = params.get("Range")


class LightStatistic(AbstractModel):
    """光照統計結果

    """

    def __init__(self):
        """
        :param LightDistribution: 各個時間點的光線值
        :type LightDistribution: list of LightDistributionStatistic
        :param LightLevelRatio: 光照程度比例統計結果
        :type LightLevelRatio: list of LightLevelRatioStatistic
        """
        self.LightDistribution = None
        self.LightLevelRatio = None


    def _deserialize(self, params):
        if params.get("LightDistribution") is not None:
            self.LightDistribution = []
            for item in params.get("LightDistribution"):
                obj = LightDistributionStatistic()
                obj._deserialize(item)
                self.LightDistribution.append(obj)
        if params.get("LightLevelRatio") is not None:
            self.LightLevelRatio = []
            for item in params.get("LightLevelRatio"):
                obj = LightLevelRatioStatistic()
                obj._deserialize(item)
                self.LightLevelRatio.append(obj)


class ModifyLibraryRequest(AbstractModel):
    """ModifyLibrary請求參數結構體

    """

    def __init__(self):
        """
        :param LibraryId: 人員庫唯一标識符
        :type LibraryId: str
        :param LibraryName: 人員庫名稱
        :type LibraryName: str
        """
        self.LibraryId = None
        self.LibraryName = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")
        self.LibraryName = params.get("LibraryName")


class ModifyLibraryResponse(AbstractModel):
    """ModifyLibrary返回參數結構體

    """

    def __init__(self):
        """
        :param LibraryId: 人員庫唯一标識符
        :type LibraryId: str
        :param LibraryName: 人員庫名稱
        :type LibraryName: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.LibraryId = None
        self.LibraryName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")
        self.LibraryName = params.get("LibraryName")
        self.RequestId = params.get("RequestId")


class ModifyPersonRequest(AbstractModel):
    """ModifyPerson請求參數結構體

    """

    def __init__(self):
        """
        :param LibraryId: 人員庫唯一标識符
        :type LibraryId: str
        :param PersonId: 人員唯一标識符
        :type PersonId: str
        :param JobNumber: 人員工作号碼
        :type JobNumber: str
        :param Mail: 人員電子信箱
        :type Mail: str
        :param Male: 人員性别
        :type Male: int
        :param PersonName: 人員名稱
        :type PersonName: str
        :param PhoneNumber: 人員電話号碼
        :type PhoneNumber: str
        :param StudentNumber: 人員學生号碼
        :type StudentNumber: str
        """
        self.LibraryId = None
        self.PersonId = None
        self.JobNumber = None
        self.Mail = None
        self.Male = None
        self.PersonName = None
        self.PhoneNumber = None
        self.StudentNumber = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")
        self.PersonId = params.get("PersonId")
        self.JobNumber = params.get("JobNumber")
        self.Mail = params.get("Mail")
        self.Male = params.get("Male")
        self.PersonName = params.get("PersonName")
        self.PhoneNumber = params.get("PhoneNumber")
        self.StudentNumber = params.get("StudentNumber")


class ModifyPersonResponse(AbstractModel):
    """ModifyPerson返回參數結構體

    """

    def __init__(self):
        """
        :param FaceInfoSet: 人臉訊息
        :type FaceInfoSet: list of FaceInfo
        :param LibraryId: 人員所屬人員庫标識符
        :type LibraryId: str
        :param PersonId: 人員唯一标識符
        :type PersonId: str
        :param PersonName: 人員名稱
        :type PersonName: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FaceInfoSet = None
        self.LibraryId = None
        self.PersonId = None
        self.PersonName = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FaceInfoSet") is not None:
            self.FaceInfoSet = []
            for item in params.get("FaceInfoSet"):
                obj = FaceInfo()
                obj._deserialize(item)
                self.FaceInfoSet.append(obj)
        self.LibraryId = params.get("LibraryId")
        self.PersonId = params.get("PersonId")
        self.PersonName = params.get("PersonName")
        self.RequestId = params.get("RequestId")


class MuteSlice(AbstractModel):
    """所有靜音片段。

    """

    def __init__(self):
        """
        :param MuteBtm: 起始時間。
        :type MuteBtm: int
        :param MuteEtm: 終止時間。
        :type MuteEtm: int
        """
        self.MuteBtm = None
        self.MuteEtm = None


    def _deserialize(self, params):
        self.MuteBtm = params.get("MuteBtm")
        self.MuteEtm = params.get("MuteEtm")


class Person(AbstractModel):
    """人員描述

    """

    def __init__(self):
        """
        :param LibraryId: 人員庫唯一标識符
        :type LibraryId: str
        :param PersonId: 人員唯一标識符
        :type PersonId: str
        :param PersonName: 人員名稱
        :type PersonName: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param JobNumber: 工作号碼
        :type JobNumber: str
        :param Mail: 電子信箱
        :type Mail: str
        :param Male: 性别
        :type Male: int
        :param PhoneNumber: 電話号碼
        :type PhoneNumber: str
        :param StudentNumber: 學生号碼
        :type StudentNumber: str
        :param UpdateTime: 修改時間
        :type UpdateTime: str
        """
        self.LibraryId = None
        self.PersonId = None
        self.PersonName = None
        self.CreateTime = None
        self.JobNumber = None
        self.Mail = None
        self.Male = None
        self.PhoneNumber = None
        self.StudentNumber = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")
        self.PersonId = params.get("PersonId")
        self.PersonName = params.get("PersonName")
        self.CreateTime = params.get("CreateTime")
        self.JobNumber = params.get("JobNumber")
        self.Mail = params.get("Mail")
        self.Male = params.get("Male")
        self.PhoneNumber = params.get("PhoneNumber")
        self.StudentNumber = params.get("StudentNumber")
        self.UpdateTime = params.get("UpdateTime")


class PersonInfo(AbstractModel):
    """人員訊息

    """

    def __init__(self):
        """
        :param PersonId: 需要比對的人員的ID清單。
        :type PersonId: str
        :param CoverBeginUrl: 視訊集錦開始封面照片。
        :type CoverBeginUrl: str
        :param CoverEndUrl: 視訊集錦結束封面照片。
        :type CoverEndUrl: str
        """
        self.PersonId = None
        self.CoverBeginUrl = None
        self.CoverEndUrl = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.CoverBeginUrl = params.get("CoverBeginUrl")
        self.CoverEndUrl = params.get("CoverEndUrl")


class StandardAudioResult(AbstractModel):
    """标準化介面圖像分析結果

    """

    def __init__(self):
        """
        :param AsrStat: 返回的當前音訊的統計訊息。當進度爲100時返回。
        :type AsrStat: :class:`tencentcloud.tci.v20190318.models.ASRStat`
        :param Texts: 返回當前音訊流的詳細訊息，如果是流模式，返回的是對應流的詳細訊息，如果是 URL模式，返回的是查詢的那一段seq對應的音訊的詳細訊息。
        :type Texts: list of WholeTextItem
        :param VocabAnalysisDetailInfo: 返回詞匯庫中的單詞出現的詳細時間訊息。
        :type VocabAnalysisDetailInfo: list of VocabDetailInfomation
        :param VocabAnalysisStatInfo: 返回詞匯庫中的單詞出現的次數訊息。
        :type VocabAnalysisStatInfo: list of VocabStatInfomation
        :param Message: 狀态描述
        :type Message: str
        :param Status: 任務狀态
        :type Status: str
        :param TotalCount: 結果數量
        :type TotalCount: int
        """
        self.AsrStat = None
        self.Texts = None
        self.VocabAnalysisDetailInfo = None
        self.VocabAnalysisStatInfo = None
        self.Message = None
        self.Status = None
        self.TotalCount = None


    def _deserialize(self, params):
        if params.get("AsrStat") is not None:
            self.AsrStat = ASRStat()
            self.AsrStat._deserialize(params.get("AsrStat"))
        if params.get("Texts") is not None:
            self.Texts = []
            for item in params.get("Texts"):
                obj = WholeTextItem()
                obj._deserialize(item)
                self.Texts.append(obj)
        if params.get("VocabAnalysisDetailInfo") is not None:
            self.VocabAnalysisDetailInfo = []
            for item in params.get("VocabAnalysisDetailInfo"):
                obj = VocabDetailInfomation()
                obj._deserialize(item)
                self.VocabAnalysisDetailInfo.append(obj)
        if params.get("VocabAnalysisStatInfo") is not None:
            self.VocabAnalysisStatInfo = []
            for item in params.get("VocabAnalysisStatInfo"):
                obj = VocabStatInfomation()
                obj._deserialize(item)
                self.VocabAnalysisStatInfo.append(obj)
        self.Message = params.get("Message")
        self.Status = params.get("Status")
        self.TotalCount = params.get("TotalCount")


class StandardImageResult(AbstractModel):
    """标準化介面圖像分析結果

    """

    def __init__(self):
        """
        :param ResultSet: 詳細結果
        :type ResultSet: list of ImageTaskResult
        :param Statistic: 分析完成後的統計結果
        :type Statistic: :class:`tencentcloud.tci.v20190318.models.ImageTaskStatistic`
        :param Message: 狀态描述
        :type Message: str
        :param Status: 任務狀态
        :type Status: str
        :param TotalCount: 結果總數
        :type TotalCount: int
        """
        self.ResultSet = None
        self.Statistic = None
        self.Message = None
        self.Status = None
        self.TotalCount = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self.ResultSet.append(obj)
        if params.get("Statistic") is not None:
            self.Statistic = ImageTaskStatistic()
            self.Statistic._deserialize(params.get("Statistic"))
        self.Message = params.get("Message")
        self.Status = params.get("Status")
        self.TotalCount = params.get("TotalCount")


class StandardVideoResult(AbstractModel):
    """标準化介面圖像分析結果

    """

    def __init__(self):
        """
        :param HighlightsInfo: 分析完成後的統計結果
        :type HighlightsInfo: list of HighlightsInfomation
        :param Message: 狀态描述
        :type Message: str
        :param Status: 任務狀态
        :type Status: str
        """
        self.HighlightsInfo = None
        self.Message = None
        self.Status = None


    def _deserialize(self, params):
        if params.get("HighlightsInfo") is not None:
            self.HighlightsInfo = []
            for item in params.get("HighlightsInfo"):
                obj = HighlightsInfomation()
                obj._deserialize(item)
                self.HighlightsInfo.append(obj)
        self.Message = params.get("Message")
        self.Status = params.get("Status")


class StatInfo(AbstractModel):
    """單詞出現的次數訊息

    """

    def __init__(self):
        """
        :param Keyword: 詞匯庫中的單詞
        :type Keyword: str
        :param Value: 單詞出現在該音訊中總次數
        :type Value: int
        """
        self.Keyword = None
        self.Value = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.Value = params.get("Value")


class StudentBodyMovementResult(AbstractModel):
    """學生肢體動作結果

    """

    def __init__(self):
        """
        :param Confidence: 置信度（已廢棄）
        :type Confidence: float
        :param HandupConfidence: 舉手識别結果置信度
        :type HandupConfidence: float
        :param HandupStatus: 舉手識别結果，包含舉手（handup）和未舉手（nothandup）
        :type HandupStatus: str
        :param Height: 識别結果高度
        :type Height: int
        :param Left: 識别結果左坐标
        :type Left: int
        :param Movements: 動作識别結果（已廢棄）
        :type Movements: str
        :param StandConfidence: 站立識别結果置信度
        :type StandConfidence: float
        :param StandStatus: 站立識别結果，包含站立（stand）和坐着（sit）
        :type StandStatus: str
        :param Top: 識别結果頂坐标
        :type Top: int
        :param Width: 識别結果寬度
        :type Width: int
        """
        self.Confidence = None
        self.HandupConfidence = None
        self.HandupStatus = None
        self.Height = None
        self.Left = None
        self.Movements = None
        self.StandConfidence = None
        self.StandStatus = None
        self.Top = None
        self.Width = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.HandupConfidence = params.get("HandupConfidence")
        self.HandupStatus = params.get("HandupStatus")
        self.Height = params.get("Height")
        self.Left = params.get("Left")
        self.Movements = params.get("Movements")
        self.StandConfidence = params.get("StandConfidence")
        self.StandStatus = params.get("StandStatus")
        self.Top = params.get("Top")
        self.Width = params.get("Width")


class SubmitAudioTaskRequest(AbstractModel):
    """SubmitAudioTask請求參數結構體

    """

    def __init__(self):
        """
        :param Lang: 音訊源的語言，預設0爲英文，1爲中文
        :type Lang: int
        :param Url: 音訊URL。客戶請求爲URL方式時必須帶此欄位指名音訊的url。
        :type Url: str
        :param VoiceEncodeType: 語音編碼類型 1:pcm
        :type VoiceEncodeType: int
        :param VoiceFileType: 語音文件類型 1:raw, 2:wav, 3:mp3，10:視訊（三種音訊格式目前僅支援16k采樣率16bit）
        :type VoiceFileType: int
        :param Functions: 功能開關清單，表示是否需要打開相應的功能，返回相應的訊息
        :type Functions: :class:`tencentcloud.tci.v20190318.models.Function`
        :param FileType: 視訊文件類型，預設點播，直播填 live_url
        :type FileType: str
        :param MuteThreshold: 靜音阈值設置，如果靜音檢測開關開啓，則靜音時間超過這個阈值認爲是靜音片段，在結果中會返回, 沒給的話預設值爲3s
        :type MuteThreshold: int
        :param VocabLibNameList: 識别詞庫名清單，評估過程使用這些詞匯庫中的詞匯進行詞匯使用行爲分析
        :type VocabLibNameList: list of str
        """
        self.Lang = None
        self.Url = None
        self.VoiceEncodeType = None
        self.VoiceFileType = None
        self.Functions = None
        self.FileType = None
        self.MuteThreshold = None
        self.VocabLibNameList = None


    def _deserialize(self, params):
        self.Lang = params.get("Lang")
        self.Url = params.get("Url")
        self.VoiceEncodeType = params.get("VoiceEncodeType")
        self.VoiceFileType = params.get("VoiceFileType")
        if params.get("Functions") is not None:
            self.Functions = Function()
            self.Functions._deserialize(params.get("Functions"))
        self.FileType = params.get("FileType")
        self.MuteThreshold = params.get("MuteThreshold")
        self.VocabLibNameList = params.get("VocabLibNameList")


class SubmitAudioTaskResponse(AbstractModel):
    """SubmitAudioTask返回參數結構體

    """

    def __init__(self):
        """
        :param JobId: 	查詢結果時指名的jobid。在URL方式時提交請求後會返回一個jobid，後續查詢該url的結果時使用這個jobid進行查詢。
        :type JobId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class SubmitCheckAttendanceTaskPlusRequest(AbstractModel):
    """SubmitCheckAttendanceTaskPlus請求參數結構體

    """

    def __init__(self):
        """
        :param FileContent: 輸入數據
        :type FileContent: list of str
        :param FileType: 視訊流類型，vod_url表示點播URL，live_url表示直播URL，預設vod_url
        :type FileType: str
        :param LibraryIds: 人員庫 ID清單
        :type LibraryIds: list of str
        :param AttendanceThreshold: 确定出勤阈值；預設爲0.92
        :type AttendanceThreshold: float
        :param EnableStranger: 是否開啓陌生人模式，陌生人模式是指在任務中發現的非注冊人臉庫中的人臉也返回相關統計訊息，預設不開啓
        :type EnableStranger: bool
        :param EndTime: 考勤結束時間（到視訊的第幾秒結束考勤），單位秒；預設爲900 
對于直播場景，使用絕對時間戳，單位秒，預設當前時間往後12小時
        :type EndTime: int
        :param NoticeUrl: 通知回調網址，要求方法爲post，application/json格式
        :type NoticeUrl: str
        :param StartTime: 考勤開始時間（從視訊的第幾秒開始考勤），單位秒；預設爲0 
對于直播場景，使用絕對時間戳，單位秒，預設當前時間
        :type StartTime: int
        :param Threshold: 識别阈值；預設爲0.8
        :type Threshold: float
        """
        self.FileContent = None
        self.FileType = None
        self.LibraryIds = None
        self.AttendanceThreshold = None
        self.EnableStranger = None
        self.EndTime = None
        self.NoticeUrl = None
        self.StartTime = None
        self.Threshold = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.FileType = params.get("FileType")
        self.LibraryIds = params.get("LibraryIds")
        self.AttendanceThreshold = params.get("AttendanceThreshold")
        self.EnableStranger = params.get("EnableStranger")
        self.EndTime = params.get("EndTime")
        self.NoticeUrl = params.get("NoticeUrl")
        self.StartTime = params.get("StartTime")
        self.Threshold = params.get("Threshold")


class SubmitCheckAttendanceTaskPlusResponse(AbstractModel):
    """SubmitCheckAttendanceTaskPlus返回參數結構體

    """

    def __init__(self):
        """
        :param JobId: 任務标識符
        :type JobId: int
        :param NotRegisteredSet: 沒有注冊的人的ID清單
        :type NotRegisteredSet: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.NotRegisteredSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.NotRegisteredSet = params.get("NotRegisteredSet")
        self.RequestId = params.get("RequestId")


class SubmitCheckAttendanceTaskRequest(AbstractModel):
    """SubmitCheckAttendanceTask請求參數結構體

    """

    def __init__(self):
        """
        :param FileContent: 輸入數據
        :type FileContent: str
        :param FileType: 視訊流類型，vod_url表示點播URL，live_url表示直播URL，預設vod_url
        :type FileType: str
        :param LibraryIds: 人員庫 ID清單
        :type LibraryIds: list of str
        :param AttendanceThreshold: 确定出勤阈值；預設爲0.92
        :type AttendanceThreshold: float
        :param EnableStranger: 是否開啓陌生人模式，陌生人模式是指在任務中發現的非注冊人臉庫中的人臉也返回相關統計訊息，預設不開啓
        :type EnableStranger: bool
        :param EndTime: 考勤結束時間（到視訊的第幾秒結束考勤），單位秒；預設爲900 
對于直播場景，使用絕對時間戳，單位秒，預設當前時間往後12小時
        :type EndTime: int
        :param NoticeUrl: 通知回調網址，要求方法爲post，application/json格式
        :type NoticeUrl: str
        :param StartTime: 考勤開始時間（從視訊的第幾秒開始考勤），單位秒；預設爲0 
對于直播場景，使用絕對時間戳，單位秒，預設當前時間
        :type StartTime: int
        :param Threshold: 識别阈值；預設爲0.8
        :type Threshold: float
        """
        self.FileContent = None
        self.FileType = None
        self.LibraryIds = None
        self.AttendanceThreshold = None
        self.EnableStranger = None
        self.EndTime = None
        self.NoticeUrl = None
        self.StartTime = None
        self.Threshold = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.FileType = params.get("FileType")
        self.LibraryIds = params.get("LibraryIds")
        self.AttendanceThreshold = params.get("AttendanceThreshold")
        self.EnableStranger = params.get("EnableStranger")
        self.EndTime = params.get("EndTime")
        self.NoticeUrl = params.get("NoticeUrl")
        self.StartTime = params.get("StartTime")
        self.Threshold = params.get("Threshold")


class SubmitCheckAttendanceTaskResponse(AbstractModel):
    """SubmitCheckAttendanceTask返回參數結構體

    """

    def __init__(self):
        """
        :param JobId: 任務标識符
        :type JobId: int
        :param NotRegisteredSet: 沒有注冊的人的ID清單
        :type NotRegisteredSet: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.NotRegisteredSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.NotRegisteredSet = params.get("NotRegisteredSet")
        self.RequestId = params.get("RequestId")


class SubmitConversationTaskRequest(AbstractModel):
    """SubmitConversationTask請求參數結構體

    """

    def __init__(self):
        """
        :param Lang: 音訊源的語言，預設0爲英文，1爲中文
        :type Lang: int
        :param StudentUrl: 學生音訊流
        :type StudentUrl: str
        :param TeacherUrl: 教師音訊流
        :type TeacherUrl: str
        :param VoiceEncodeType: 語音編碼類型 1:pcm
        :type VoiceEncodeType: int
        :param VoiceFileType: 語音文件類型 1:raw, 2:wav, 3:mp3（三種格式目前僅支援16k采樣率16bit）
        :type VoiceFileType: int
        :param Functions: 功能開關清單，表示是否需要打開相應的功能，返回相應的訊息
        :type Functions: :class:`tencentcloud.tci.v20190318.models.Function`
        :param VocabLibNameList: 識别詞庫名清單，評估過程使用這些詞匯庫中的詞匯進行詞匯使用行爲分析
        :type VocabLibNameList: list of str
        """
        self.Lang = None
        self.StudentUrl = None
        self.TeacherUrl = None
        self.VoiceEncodeType = None
        self.VoiceFileType = None
        self.Functions = None
        self.VocabLibNameList = None


    def _deserialize(self, params):
        self.Lang = params.get("Lang")
        self.StudentUrl = params.get("StudentUrl")
        self.TeacherUrl = params.get("TeacherUrl")
        self.VoiceEncodeType = params.get("VoiceEncodeType")
        self.VoiceFileType = params.get("VoiceFileType")
        if params.get("Functions") is not None:
            self.Functions = Function()
            self.Functions._deserialize(params.get("Functions"))
        self.VocabLibNameList = params.get("VocabLibNameList")


class SubmitConversationTaskResponse(AbstractModel):
    """SubmitConversationTask返回參數結構體

    """

    def __init__(self):
        """
        :param JobId: 	查詢結果時指名的jobid。在URL方式時提交請求後會返回一個jobid，後續查詢該url的結果時使用這個jobid進行查詢。
        :type JobId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class SubmitDoubleVideoHighlightsRequest(AbstractModel):
    """SubmitDoubleVideoHighlights請求參數結構體

    """

    def __init__(self):
        """
        :param FileContent: 學生視訊url
        :type FileContent: str
        :param LibIds: 需要檢索的人臉合集庫，不在庫中的人臉将不參與精彩集錦；目前僅支援輸入一個人臉庫。
        :type LibIds: list of str
        :param Functions: 詳細功能開關配置項
        :type Functions: :class:`tencentcloud.tci.v20190318.models.DoubleVideoFunction`
        :param PersonInfoList: 需要比對的人員訊息清單。
        :type PersonInfoList: list of PersonInfo
        :param FrameInterval: 視訊處理的抽幀間隔，單位毫秒。建議留空。
        :type FrameInterval: int
        :param PersonIds: 舊版本需要比對的人員訊息清單。
        :type PersonIds: list of str
        :param SimThreshold: 人臉檢索的相似度阈值，預設值0.89。建議留空。
        :type SimThreshold: float
        :param TeacherFileContent: 老師視訊url
        :type TeacherFileContent: str
        """
        self.FileContent = None
        self.LibIds = None
        self.Functions = None
        self.PersonInfoList = None
        self.FrameInterval = None
        self.PersonIds = None
        self.SimThreshold = None
        self.TeacherFileContent = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.LibIds = params.get("LibIds")
        if params.get("Functions") is not None:
            self.Functions = DoubleVideoFunction()
            self.Functions._deserialize(params.get("Functions"))
        if params.get("PersonInfoList") is not None:
            self.PersonInfoList = []
            for item in params.get("PersonInfoList"):
                obj = PersonInfo()
                obj._deserialize(item)
                self.PersonInfoList.append(obj)
        self.FrameInterval = params.get("FrameInterval")
        self.PersonIds = params.get("PersonIds")
        self.SimThreshold = params.get("SimThreshold")
        self.TeacherFileContent = params.get("TeacherFileContent")


class SubmitDoubleVideoHighlightsResponse(AbstractModel):
    """SubmitDoubleVideoHighlights返回參數結構體

    """

    def __init__(self):
        """
        :param JobId: 視訊拆條任務ID，用來唯一标識視訊拆條任務。
        :type JobId: int
        :param NotRegistered: 未注冊的人員ID清單。若出現此項，代表評估出現了問題，輸入的PersonId中有不在庫中的人員ID。
        :type NotRegistered: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.NotRegistered = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.NotRegistered = params.get("NotRegistered")
        self.RequestId = params.get("RequestId")


class SubmitFullBodyClassTaskRequest(AbstractModel):
    """SubmitFullBodyClassTask請求參數結構體

    """

    def __init__(self):
        """
        :param FileContent: 輸入分析對象内容，輸入數據格式參考FileType參數釋義
        :type FileContent: str
        :param FileType: 輸入分析對象類型，picture_url:圖片網址，vod_url:視訊網址，live_url：直播網址，picture: 圖片二進制數據的BASE64編碼
        :type FileType: str
        :param Lang: 音訊源的語言，預設0爲英文，1爲中文
        :type Lang: int
        :param LibrarySet: 查詢人員庫清單，可填寫老師的注冊照所在人員庫
        :type LibrarySet: list of str
        :param MaxVideoDuration: 視訊評估時間，單位秒，點播場景預設值爲2小時（無法探測長度時）或完整視訊，直播場景預設值爲10分鍾或直播提前結束
        :type MaxVideoDuration: int
        :param VocabLibNameList: 識别詞庫名清單，這些詞匯庫用來維護關鍵詞，評估老師授課過程中，對這些關鍵詞的使用情況
        :type VocabLibNameList: list of str
        :param VoiceEncodeType: 語音編碼類型 1:pcm，當FileType爲vod_url或live_url時爲必填
        :type VoiceEncodeType: int
        :param VoiceFileType: 語音文件類型 10:視訊（三種音訊格式目前僅支援16k采樣率16bit），當FileType爲vod_url或live_url時爲必填
        :type VoiceFileType: int
        """
        self.FileContent = None
        self.FileType = None
        self.Lang = None
        self.LibrarySet = None
        self.MaxVideoDuration = None
        self.VocabLibNameList = None
        self.VoiceEncodeType = None
        self.VoiceFileType = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.FileType = params.get("FileType")
        self.Lang = params.get("Lang")
        self.LibrarySet = params.get("LibrarySet")
        self.MaxVideoDuration = params.get("MaxVideoDuration")
        self.VocabLibNameList = params.get("VocabLibNameList")
        self.VoiceEncodeType = params.get("VoiceEncodeType")
        self.VoiceFileType = params.get("VoiceFileType")


class SubmitFullBodyClassTaskResponse(AbstractModel):
    """SubmitFullBodyClassTask返回參數結構體

    """

    def __init__(self):
        """
        :param ImageResults: 圖像任務直接返回結果，包括： FaceAttr、 FaceExpression、 FaceIdentify、 FaceInfo、 FacePose、 TeacherBodyMovement、TimeInfo
        :type ImageResults: list of ImageTaskResult
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ImageResults = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImageResults") is not None:
            self.ImageResults = []
            for item in params.get("ImageResults"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self.ImageResults.append(obj)
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class SubmitHighlightsRequest(AbstractModel):
    """SubmitHighlights請求參數結構體

    """

    def __init__(self):
        """
        :param Functions: 表情配置開關項。
        :type Functions: :class:`tencentcloud.tci.v20190318.models.HLFunction`
        :param FileContent: 視訊url。
        :type FileContent: str
        :param FileType: 視訊類型及來源，目前只支援點播類型："vod_url"。
        :type FileType: str
        :param LibIds: 需要檢索的人臉合集庫，不在庫中的人臉将不參與精彩集錦。
        :type LibIds: list of str
        :param FrameInterval: 視訊處理的抽幀間隔，單位毫秒。建議留空。
        :type FrameInterval: int
        :param KeywordsLanguage: 關鍵詞語言類型，0爲英文，1爲中文。
        :type KeywordsLanguage: int
        :param KeywordsStrings: 關鍵詞數組，當且僅當Funtions中的EnableKeywordWonderfulTime爲true時有意義，比對相應的關鍵字。
        :type KeywordsStrings: list of str
        :param MaxVideoDuration: 處理視訊的總時長，單位毫秒。該值爲0或未設置時，預設值兩小時生效；當該值大于視訊實際時長時，視訊實際時長生效；當該值小於視訊實際時長時，該值生效；當獲取視訊實際時長失敗時，若該值設置則生效，否則預設值生效。建議留空。
        :type MaxVideoDuration: int
        :param SimThreshold: 人臉檢索的相似度阈值，預設值0.89。建議留空。
        :type SimThreshold: float
        """
        self.Functions = None
        self.FileContent = None
        self.FileType = None
        self.LibIds = None
        self.FrameInterval = None
        self.KeywordsLanguage = None
        self.KeywordsStrings = None
        self.MaxVideoDuration = None
        self.SimThreshold = None


    def _deserialize(self, params):
        if params.get("Functions") is not None:
            self.Functions = HLFunction()
            self.Functions._deserialize(params.get("Functions"))
        self.FileContent = params.get("FileContent")
        self.FileType = params.get("FileType")
        self.LibIds = params.get("LibIds")
        self.FrameInterval = params.get("FrameInterval")
        self.KeywordsLanguage = params.get("KeywordsLanguage")
        self.KeywordsStrings = params.get("KeywordsStrings")
        self.MaxVideoDuration = params.get("MaxVideoDuration")
        self.SimThreshold = params.get("SimThreshold")


class SubmitHighlightsResponse(AbstractModel):
    """SubmitHighlights返回參數結構體

    """

    def __init__(self):
        """
        :param JobId: 視訊拆條任務ID，用來唯一标識視訊拆條任務。
        :type JobId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class SubmitImageTaskPlusRequest(AbstractModel):
    """SubmitImageTaskPlus請求參數結構體

    """

    def __init__(self):
        """
        :param FileContent: 輸入分析對象内容，輸入數據格式參考FileType參數釋義
        :type FileContent: list of str
        :param FileType: 輸入分析對象類型，picture：二進制圖片的 base64 編碼字串，picture_url:圖片網址，vod_url：視訊網址，live_url：直播網址
        :type FileType: str
        :param Functions: 任務控制選項
        :type Functions: :class:`tencentcloud.tci.v20190318.models.ImageTaskFunction`
        :param LightStandardSet: 光照标準清單
        :type LightStandardSet: list of LightStandard
        :param FrameInterval: 抽幀的時間間隔，單位毫秒，預設值1000，保留欄位，當前不支援填寫。
        :type FrameInterval: int
        :param LibrarySet: 查詢人員庫清單
        :type LibrarySet: list of str
        :param MaxVideoDuration: 視訊評估時間，單位秒，點播場景預設值爲2小時（無法探測長度時）或完整視訊，直播場景預設值爲10分鍾或直播提前結束
        :type MaxVideoDuration: int
        :param SimThreshold: 人臉識别中的相似度阈值，預設值爲0.89，保留欄位，當前不支援填寫。
        :type SimThreshold: float
        """
        self.FileContent = None
        self.FileType = None
        self.Functions = None
        self.LightStandardSet = None
        self.FrameInterval = None
        self.LibrarySet = None
        self.MaxVideoDuration = None
        self.SimThreshold = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.FileType = params.get("FileType")
        if params.get("Functions") is not None:
            self.Functions = ImageTaskFunction()
            self.Functions._deserialize(params.get("Functions"))
        if params.get("LightStandardSet") is not None:
            self.LightStandardSet = []
            for item in params.get("LightStandardSet"):
                obj = LightStandard()
                obj._deserialize(item)
                self.LightStandardSet.append(obj)
        self.FrameInterval = params.get("FrameInterval")
        self.LibrarySet = params.get("LibrarySet")
        self.MaxVideoDuration = params.get("MaxVideoDuration")
        self.SimThreshold = params.get("SimThreshold")


class SubmitImageTaskPlusResponse(AbstractModel):
    """SubmitImageTaskPlus返回參數結構體

    """

    def __init__(self):
        """
        :param ResultSet: 識别結果
        :type ResultSet: list of ImageTaskResult
        :param JobId: 任務标識符
        :type JobId: int
        :param Progress: 任務進度
        :type Progress: int
        :param TotalCount: 結果總數目
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ResultSet = None
        self.JobId = None
        self.Progress = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self.ResultSet.append(obj)
        self.JobId = params.get("JobId")
        self.Progress = params.get("Progress")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class SubmitImageTaskRequest(AbstractModel):
    """SubmitImageTask請求參數結構體

    """

    def __init__(self):
        """
        :param FileContent: 輸入分析對象内容，輸入數據格式參考FileType參數釋義
        :type FileContent: str
        :param FileType: 輸入分析對象類型，picture：二進制圖片的 base64 編碼字串，picture_url:圖片網址，vod_url：視訊網址，live_url：直播網址
        :type FileType: str
        :param Functions: 任務控制選項
        :type Functions: :class:`tencentcloud.tci.v20190318.models.ImageTaskFunction`
        :param LightStandardSet: 光照标準清單
        :type LightStandardSet: list of LightStandard
        :param EventsCallBack: 結果更新回調網址。
        :type EventsCallBack: str
        :param FrameInterval: 抽幀的時間間隔，單位毫秒，預設值1000，保留欄位，當前不支援填寫。
        :type FrameInterval: int
        :param LibrarySet: 查詢人員庫清單
        :type LibrarySet: list of str
        :param MaxVideoDuration: 視訊評估時間，單位秒，點播場景預設值爲2小時（無法探測長度時）或完整視訊，直播場景預設值爲10分鍾或直播提前結束
        :type MaxVideoDuration: int
        :param SimThreshold: 人臉識别中的相似度阈值，預設值爲0.89，保留欄位，當前不支援填寫。
        :type SimThreshold: float
        """
        self.FileContent = None
        self.FileType = None
        self.Functions = None
        self.LightStandardSet = None
        self.EventsCallBack = None
        self.FrameInterval = None
        self.LibrarySet = None
        self.MaxVideoDuration = None
        self.SimThreshold = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.FileType = params.get("FileType")
        if params.get("Functions") is not None:
            self.Functions = ImageTaskFunction()
            self.Functions._deserialize(params.get("Functions"))
        if params.get("LightStandardSet") is not None:
            self.LightStandardSet = []
            for item in params.get("LightStandardSet"):
                obj = LightStandard()
                obj._deserialize(item)
                self.LightStandardSet.append(obj)
        self.EventsCallBack = params.get("EventsCallBack")
        self.FrameInterval = params.get("FrameInterval")
        self.LibrarySet = params.get("LibrarySet")
        self.MaxVideoDuration = params.get("MaxVideoDuration")
        self.SimThreshold = params.get("SimThreshold")


class SubmitImageTaskResponse(AbstractModel):
    """SubmitImageTask返回參數結構體

    """

    def __init__(self):
        """
        :param ResultSet: 識别結果
        :type ResultSet: list of ImageTaskResult
        :param JobId: 任務标識符
        :type JobId: int
        :param Progress: 任務進度
        :type Progress: int
        :param TotalCount: 結果總數目
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ResultSet = None
        self.JobId = None
        self.Progress = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self.ResultSet.append(obj)
        self.JobId = params.get("JobId")
        self.Progress = params.get("Progress")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class SubmitOneByOneClassTaskRequest(AbstractModel):
    """SubmitOneByOneClassTask請求參數結構體

    """

    def __init__(self):
        """
        :param FileContent: 輸入分析對象内容，輸入數據格式參考FileType參數釋義
        :type FileContent: str
        :param FileType: 輸入分析對象類型，picture_url:圖片網址，vod_url:視訊網址，live_url：直播網址，picture: 圖片二進制數據的BASE64編碼
        :type FileType: str
        :param Lang: 音訊源的語言，預設0爲英文，1爲中文 
        :type Lang: int
        :param LibrarySet: 查詢人員庫清單，可填寫學生的注冊照所在人員庫
        :type LibrarySet: list of str
        :param MaxVideoDuration: 視訊評估時間，單位秒，點播場景預設值爲2小時（無法探測長度時）或完整視訊，直播場景預設值爲10分鍾或直播提前結束
        :type MaxVideoDuration: int
        :param VocabLibNameList: 識别詞庫名清單，這些詞匯庫用來維護關鍵詞，評估學生對這些關鍵詞的使用情況
        :type VocabLibNameList: list of str
        :param VoiceEncodeType: 語音編碼類型 1:pcm，當FileType爲vod_url或live_url時爲必填
        :type VoiceEncodeType: int
        :param VoiceFileType: 語音文件類型10:視訊（三種音訊格式目前僅支援16k采樣率16bit），當FileType爲vod_url或live_url時爲必填
        :type VoiceFileType: int
        """
        self.FileContent = None
        self.FileType = None
        self.Lang = None
        self.LibrarySet = None
        self.MaxVideoDuration = None
        self.VocabLibNameList = None
        self.VoiceEncodeType = None
        self.VoiceFileType = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.FileType = params.get("FileType")
        self.Lang = params.get("Lang")
        self.LibrarySet = params.get("LibrarySet")
        self.MaxVideoDuration = params.get("MaxVideoDuration")
        self.VocabLibNameList = params.get("VocabLibNameList")
        self.VoiceEncodeType = params.get("VoiceEncodeType")
        self.VoiceFileType = params.get("VoiceFileType")


class SubmitOneByOneClassTaskResponse(AbstractModel):
    """SubmitOneByOneClassTask返回參數結構體

    """

    def __init__(self):
        """
        :param ImageResults: 圖像任務直接返回結果，包括：FaceAttr、 FaceExpression、 FaceIdentify、 FaceInfo、 FacePose、TimeInfo
        :type ImageResults: list of ImageTaskResult
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ImageResults = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImageResults") is not None:
            self.ImageResults = []
            for item in params.get("ImageResults"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self.ImageResults.append(obj)
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class SubmitOpenClassTaskRequest(AbstractModel):
    """SubmitOpenClassTask請求參數結構體

    """

    def __init__(self):
        """
        :param FileContent: 輸入分析對象内容，輸入數據格式參考FileType參數釋義
        :type FileContent: str
        :param FileType: 輸入分析對象類型，picture_url:圖片網址，vod_url:視訊網址，live_url：直播網址,picture: 圖片二進制數據的BASE64編碼
        :type FileType: str
        :param LibrarySet: 查詢人員庫清單，可填寫學生們的注冊照所在人員庫
        :type LibrarySet: list of str
        :param MaxVideoDuration: 視訊評估時間，單位秒，點播場景預設值爲2小時（無法探測長度時）或完整視訊，直播場景預設值爲10分鍾或直播提前結束
        :type MaxVideoDuration: int
        """
        self.FileContent = None
        self.FileType = None
        self.LibrarySet = None
        self.MaxVideoDuration = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.FileType = params.get("FileType")
        self.LibrarySet = params.get("LibrarySet")
        self.MaxVideoDuration = params.get("MaxVideoDuration")


class SubmitOpenClassTaskResponse(AbstractModel):
    """SubmitOpenClassTask返回參數結構體

    """

    def __init__(self):
        """
        :param ImageResults: 圖像任務直接返回結果，包括：FaceAttr、 FaceExpression、 FaceIdentify、 FaceInfo、 FacePose、 StudentBodyMovement、TimeInfo
        :type ImageResults: list of ImageTaskResult
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ImageResults = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImageResults") is not None:
            self.ImageResults = []
            for item in params.get("ImageResults"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self.ImageResults.append(obj)
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class SubmitPartialBodyClassTaskRequest(AbstractModel):
    """SubmitPartialBodyClassTask請求參數結構體

    """

    def __init__(self):
        """
        :param FileContent: 輸入分析對象内容，輸入數據格式參考FileType參數釋義
        :type FileContent: str
        :param FileType: 輸入分析對象類型，picture_url:圖片網址，vod_url:視訊網址，live_url：直播網址，picture: 圖片二進制數據的BASE64編碼
        :type FileType: str
        :param Lang: 音訊源的語言，預設0爲英文，1爲中文
        :type Lang: int
        :param LibrarySet: 查詢人員庫清單，可填寫老師的注冊照所在人員庫
        :type LibrarySet: list of str
        :param MaxVideoDuration: 視訊評估時間，單位秒，點播場景預設值爲2小時（無法探測長度時）或完整視訊，直播場景預設值爲10分鍾或直播提前結束
        :type MaxVideoDuration: int
        :param VocabLibNameList: 識别詞庫名清單，這些詞匯庫用來維護關鍵詞，評估老師授課過程中，對這些關鍵詞的使用情況
        :type VocabLibNameList: list of str
        :param VoiceEncodeType: 語音編碼類型 1:pcm，當FileType爲vod_url或live_url時爲必填
        :type VoiceEncodeType: int
        :param VoiceFileType: 語音文件類型 10:視訊（三種音訊格式目前僅支援16k采樣率16bit），當FileType爲vod_url或live_url時爲必填
        :type VoiceFileType: int
        """
        self.FileContent = None
        self.FileType = None
        self.Lang = None
        self.LibrarySet = None
        self.MaxVideoDuration = None
        self.VocabLibNameList = None
        self.VoiceEncodeType = None
        self.VoiceFileType = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.FileType = params.get("FileType")
        self.Lang = params.get("Lang")
        self.LibrarySet = params.get("LibrarySet")
        self.MaxVideoDuration = params.get("MaxVideoDuration")
        self.VocabLibNameList = params.get("VocabLibNameList")
        self.VoiceEncodeType = params.get("VoiceEncodeType")
        self.VoiceFileType = params.get("VoiceFileType")


class SubmitPartialBodyClassTaskResponse(AbstractModel):
    """SubmitPartialBodyClassTask返回參數結構體

    """

    def __init__(self):
        """
        :param ImageResults: 圖像任務直接返回結果，包括： FaceAttr、 FaceExpression、 FaceIdentify、 FaceInfo、 FacePose、 Gesture 、 Light、 TimeInfo
        :type ImageResults: list of ImageTaskResult
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ImageResults = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImageResults") is not None:
            self.ImageResults = []
            for item in params.get("ImageResults"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self.ImageResults.append(obj)
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class SubmitTraditionalClassTaskRequest(AbstractModel):
    """SubmitTraditionalClassTask請求參數結構體

    """

    def __init__(self):
        """
        :param FileContent: 輸入分析對象内容，輸入數據格式參考FileType參數釋義
        :type FileContent: str
        :param FileType: 輸入分析對象類型，picture_url:圖片網址，vod_url:視訊網址，live_url：直播網址，picture：圖片二進制數據的BASE64編碼
        :type FileType: str
        :param LibrarySet: 查詢人員庫清單，可填寫學生們的注冊照所在人員庫
        :type LibrarySet: list of str
        :param MaxVideoDuration: 視訊評估時間，單位秒，點播場景預設值爲2小時（無法探測長度時）或完整視訊，直播場景預設值爲10分鍾或直播提前結束
        :type MaxVideoDuration: int
        """
        self.FileContent = None
        self.FileType = None
        self.LibrarySet = None
        self.MaxVideoDuration = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.FileType = params.get("FileType")
        self.LibrarySet = params.get("LibrarySet")
        self.MaxVideoDuration = params.get("MaxVideoDuration")


class SubmitTraditionalClassTaskResponse(AbstractModel):
    """SubmitTraditionalClassTask返回參數結構體

    """

    def __init__(self):
        """
        :param ImageResults: 圖像任務直接返回結果，包括： ActionInfo、FaceAttr、 FaceExpression、 FaceIdentify、 FaceInfo、 FacePose、 TimeInfo
        :type ImageResults: list of ImageTaskResult
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ImageResults = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImageResults") is not None:
            self.ImageResults = []
            for item in params.get("ImageResults"):
                obj = ImageTaskResult()
                obj._deserialize(item)
                self.ImageResults.append(obj)
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class SuspectedInfo(AbstractModel):
    """疑似出席人員

    """

    def __init__(self):
        """
        :param FaceSet: TopN比對訊息清單
        :type FaceSet: list of FrameInfo
        :param PersonId: 識别到的人員id
        :type PersonId: str
        """
        self.FaceSet = None
        self.PersonId = None


    def _deserialize(self, params):
        if params.get("FaceSet") is not None:
            self.FaceSet = []
            for item in params.get("FaceSet"):
                obj = FrameInfo()
                obj._deserialize(item)
                self.FaceSet.append(obj)
        self.PersonId = params.get("PersonId")


class TeacherOutScreenResult(AbstractModel):
    """教師是否在螢幕内判斷結果

    """

    def __init__(self):
        """
        :param Class: 動作識别結果，InScreen：在螢幕内
OutScreen：不在螢幕内
        :type Class: str
        :param Height: 識别結果高度
        :type Height: int
        :param Left: 識别結果左坐标
        :type Left: int
        :param Top: 識别結果頂坐标
        :type Top: int
        :param Width: 識别結果寬度
        :type Width: int
        """
        self.Class = None
        self.Height = None
        self.Left = None
        self.Top = None
        self.Width = None


    def _deserialize(self, params):
        self.Class = params.get("Class")
        self.Height = params.get("Height")
        self.Left = params.get("Left")
        self.Top = params.get("Top")
        self.Width = params.get("Width")


class TextItem(AbstractModel):
    """當前句子的訊息

    """

    def __init__(self):
        """
        :param Words: 當前句子包含的所有單詞訊息
        :type Words: list of Word
        :param Confidence: 當前句子的置信度
        :type Confidence: float
        :param Mbtm: 當前句子語音的起始時間點，單位爲ms
        :type Mbtm: int
        :param Metm: 當前句子語音的終止時間點，單位爲ms
        :type Metm: int
        :param Tag: 保留參數，暫無意義
        :type Tag: int
        :param Text: 當前句子
        :type Text: str
        :param TextSize: 當前句子的位元數
        :type TextSize: int
        """
        self.Words = None
        self.Confidence = None
        self.Mbtm = None
        self.Metm = None
        self.Tag = None
        self.Text = None
        self.TextSize = None


    def _deserialize(self, params):
        if params.get("Words") is not None:
            self.Words = []
            for item in params.get("Words"):
                obj = Word()
                obj._deserialize(item)
                self.Words.append(obj)
        self.Confidence = params.get("Confidence")
        self.Mbtm = params.get("Mbtm")
        self.Metm = params.get("Metm")
        self.Tag = params.get("Tag")
        self.Text = params.get("Text")
        self.TextSize = params.get("TextSize")


class TimeInfoResult(AbstractModel):
    """TimeInfoResult

    """

    def __init__(self):
        """
        :param Duration: 持續時間，單位毫秒
        :type Duration: int
        :param EndTs: 結束時間戳，單位毫秒
        :type EndTs: int
        :param StartTs: 開始時間戳，單位毫秒
        :type StartTs: int
        """
        self.Duration = None
        self.EndTs = None
        self.StartTs = None


    def _deserialize(self, params):
        self.Duration = params.get("Duration")
        self.EndTs = params.get("EndTs")
        self.StartTs = params.get("StartTs")


class TimeType(AbstractModel):
    """起止時間

    """

    def __init__(self):
        """
        :param EndTime: 結束時間戳
        :type EndTime: int
        :param StartTime: 起始時間戳
        :type StartTime: int
        """
        self.EndTime = None
        self.StartTime = None


    def _deserialize(self, params):
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")


class TransmitAudioStreamRequest(AbstractModel):
    """TransmitAudioStream請求參數結構體

    """

    def __init__(self):
        """
        :param Functions: 功能開關清單，表示是否需要打開相應的功能，返回相應的訊息
        :type Functions: :class:`tencentcloud.tci.v20190318.models.Function`
        :param SeqId: 流式數據包的序号，從1開始，當IsEnd欄位爲1後後續序号無意義。
        :type SeqId: int
        :param SessionId: 語音段唯一标識，一個完整語音一個SessionId。
        :type SessionId: str
        :param UserVoiceData: 當前數據包數據, 流式模式下數據包大小可以按需設置，在網絡良好的情況下，建議設置爲0.5k，且必須保證分片幀完整（16bit的數據必須保證音訊長度爲偶數），編碼格式要求爲BASE64。
        :type UserVoiceData: str
        :param VoiceEncodeType: 語音編碼類型 1:pcm。
        :type VoiceEncodeType: int
        :param VoiceFileType: 語音文件類型 	1: raw, 2: wav, 3: mp3 (語言文件格式目前僅支援 16k 采樣率 16bit 編碼單聲道，如有不一緻可能導緻評估不準确或失敗)。
        :type VoiceFileType: int
        :param IsEnd: 是否傳輸完畢标志，若爲0表示未完畢，若爲1則傳輸完畢開始評估，非流式模式下無意義。
        :type IsEnd: int
        :param Lang: 音訊源的語言，預設0爲英文，1爲中文
        :type Lang: int
        :param StorageMode: 是否臨時保存 音訊連結
        :type StorageMode: int
        :param VocabLibNameList: 識别詞庫名清單，評估過程使用這些詞匯庫中的詞匯進行詞匯使用行爲分析
        :type VocabLibNameList: list of str
        """
        self.Functions = None
        self.SeqId = None
        self.SessionId = None
        self.UserVoiceData = None
        self.VoiceEncodeType = None
        self.VoiceFileType = None
        self.IsEnd = None
        self.Lang = None
        self.StorageMode = None
        self.VocabLibNameList = None


    def _deserialize(self, params):
        if params.get("Functions") is not None:
            self.Functions = Function()
            self.Functions._deserialize(params.get("Functions"))
        self.SeqId = params.get("SeqId")
        self.SessionId = params.get("SessionId")
        self.UserVoiceData = params.get("UserVoiceData")
        self.VoiceEncodeType = params.get("VoiceEncodeType")
        self.VoiceFileType = params.get("VoiceFileType")
        self.IsEnd = params.get("IsEnd")
        self.Lang = params.get("Lang")
        self.StorageMode = params.get("StorageMode")
        self.VocabLibNameList = params.get("VocabLibNameList")


class TransmitAudioStreamResponse(AbstractModel):
    """TransmitAudioStream返回參數結構體

    """

    def __init__(self):
        """
        :param AsrStat: 返回的當前音訊的統計訊息。當進度爲100時返回。
        :type AsrStat: :class:`tencentcloud.tci.v20190318.models.ASRStat`
        :param Texts: 返回當前音訊流的詳細訊息，如果是流模式，返回的是對應流的詳細訊息，如果是 URL模式，返回的是查詢的那一段seq對應的音訊的詳細訊息。
        :type Texts: list of WholeTextItem
        :param VocabAnalysisDetailInfo: 返回詞匯庫中的單詞出現的詳細時間訊息。
        :type VocabAnalysisDetailInfo: list of VocabDetailInfomation
        :param VocabAnalysisStatInfo: 返回詞匯庫中的單詞出現的次數訊息。
        :type VocabAnalysisStatInfo: list of VocabStatInfomation
        :param AllTexts: 音訊全部文本。
        :type AllTexts: str
        :param AudioUrl: 臨時保存的音訊連結
        :type AudioUrl: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AsrStat = None
        self.Texts = None
        self.VocabAnalysisDetailInfo = None
        self.VocabAnalysisStatInfo = None
        self.AllTexts = None
        self.AudioUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AsrStat") is not None:
            self.AsrStat = ASRStat()
            self.AsrStat._deserialize(params.get("AsrStat"))
        if params.get("Texts") is not None:
            self.Texts = []
            for item in params.get("Texts"):
                obj = WholeTextItem()
                obj._deserialize(item)
                self.Texts.append(obj)
        if params.get("VocabAnalysisDetailInfo") is not None:
            self.VocabAnalysisDetailInfo = []
            for item in params.get("VocabAnalysisDetailInfo"):
                obj = VocabDetailInfomation()
                obj._deserialize(item)
                self.VocabAnalysisDetailInfo.append(obj)
        if params.get("VocabAnalysisStatInfo") is not None:
            self.VocabAnalysisStatInfo = []
            for item in params.get("VocabAnalysisStatInfo"):
                obj = VocabStatInfomation()
                obj._deserialize(item)
                self.VocabAnalysisStatInfo.append(obj)
        self.AllTexts = params.get("AllTexts")
        self.AudioUrl = params.get("AudioUrl")
        self.RequestId = params.get("RequestId")


class VocabDetailInfomation(AbstractModel):
    """詞匯庫中的單詞出現在音訊中的那個句子的起始時間和結束時間訊息

    """

    def __init__(self):
        """
        :param VocabDetailInfo: 詞匯庫中的單詞出現在該音訊中的那個句子的時間戳，出現了幾次，就返回對應次數的起始和結束時間戳
        :type VocabDetailInfo: list of DetailInfo
        :param VocabLibName: 詞匯庫名
        :type VocabLibName: str
        """
        self.VocabDetailInfo = None
        self.VocabLibName = None


    def _deserialize(self, params):
        if params.get("VocabDetailInfo") is not None:
            self.VocabDetailInfo = []
            for item in params.get("VocabDetailInfo"):
                obj = DetailInfo()
                obj._deserialize(item)
                self.VocabDetailInfo.append(obj)
        self.VocabLibName = params.get("VocabLibName")


class VocabStatInfomation(AbstractModel):
    """詞匯庫中的單詞出現在音訊中的總次數訊息

    """

    def __init__(self):
        """
        :param VocabDetailInfo: 單詞出現在該音訊中總次數
        :type VocabDetailInfo: list of StatInfo
        :param VocabLibName: 詞匯庫名稱
        :type VocabLibName: str
        """
        self.VocabDetailInfo = None
        self.VocabLibName = None


    def _deserialize(self, params):
        if params.get("VocabDetailInfo") is not None:
            self.VocabDetailInfo = []
            for item in params.get("VocabDetailInfo"):
                obj = StatInfo()
                obj._deserialize(item)
                self.VocabDetailInfo.append(obj)
        self.VocabLibName = params.get("VocabLibName")


class WholeTextItem(AbstractModel):
    """含有語速的句子訊息

    """

    def __init__(self):
        """
        :param TextItem: 當前句子的訊息
        :type TextItem: :class:`tencentcloud.tci.v20190318.models.TextItem`
        :param AvgVolume: Vad的平均音量
        :type AvgVolume: float
        :param MaxVolume: Vad的最大音量
        :type MaxVolume: float
        :param MinVolume: Vad的最小音量
        :type MinVolume: float
        :param Speed: 當前句子的語速
        :type Speed: float
        """
        self.TextItem = None
        self.AvgVolume = None
        self.MaxVolume = None
        self.MinVolume = None
        self.Speed = None


    def _deserialize(self, params):
        if params.get("TextItem") is not None:
            self.TextItem = TextItem()
            self.TextItem._deserialize(params.get("TextItem"))
        self.AvgVolume = params.get("AvgVolume")
        self.MaxVolume = params.get("MaxVolume")
        self.MinVolume = params.get("MinVolume")
        self.Speed = params.get("Speed")


class Word(AbstractModel):
    """當前句子包含的所有單詞訊息

    """

    def __init__(self):
        """
        :param Confidence: 當前詞的置信度
        :type Confidence: float
        :param Mbtm: 當前單詞語音的起始時間點，單位爲ms
        :type Mbtm: int
        :param Metm: 當前單詞語音的終止時間點，單位爲ms
        :type Metm: int
        :param Text: 當前詞
        :type Text: str
        :param Wsize: 當前詞的位元數
        :type Wsize: int
        """
        self.Confidence = None
        self.Mbtm = None
        self.Metm = None
        self.Text = None
        self.Wsize = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Mbtm = params.get("Mbtm")
        self.Metm = params.get("Metm")
        self.Text = params.get("Text")
        self.Wsize = params.get("Wsize")


class WordTimePair(AbstractModel):
    """單詞出現的那個句子的起始時間和結束時間訊息

    """

    def __init__(self):
        """
        :param Mbtm: 單詞出現的那個句子的起始時間
        :type Mbtm: int
        :param Metm: 	單詞出現的那個句子的結束時間
        :type Metm: int
        """
        self.Mbtm = None
        self.Metm = None


    def _deserialize(self, params):
        self.Mbtm = params.get("Mbtm")
        self.Metm = params.get("Metm")