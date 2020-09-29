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


class InitOralProcessRequest(AbstractModel):
    """InitOralProcess請求參數結構體

    """

    def __init__(self):
        """
        :param SessionId: 語音段唯一標識，一段語音一個SessionId
        :type SessionId: str
        :param RefText: 被評估語音對應的文本，句子模式下不超過個 20 單詞或者中文文字，段落模式不超過 120 單詞或者中文文字，中文評估使用 utf-8 編碼，自由說模式該值傳空。如需要在單詞模式和句子模式下使用自定義音素，可以通過設置 TextMode 使用[音素標注](https://cloud.taifucloud.com/document/product/884/33698)。
        :type RefText: str
        :param WorkMode: 語音輸入模式，0：流式分片，1：非流式一次性評估
        :type WorkMode: int
        :param EvalMode: 評估模式，0：詞模式（中文評測模式下爲文字模式），1：句子模式，2：段落模式，3：自由說模式，當爲詞模式評估時，能夠提供每個音節的評估訊息，當爲句子模式時，能夠提供完整度和流利度訊息。
        :type EvalMode: int
        :param ScoreCoeff: 評價苛刻指數，取值爲[1.0 - 4.0]範圍内的浮點數，用於平滑不同年齡段的分數，1.0爲小年齡段，4.0爲最高年齡段
        :type ScoreCoeff: float
        :param SoeAppId: 業務應用ID，與賬號應用APPID無關，是用來方便客戶管理服務的參數，新的 SoeAppId 可以在[控制台](https://console.cloud.taifucloud.com/soe)【應用管理】下新建。
        :type SoeAppId: str
        :param IsLongLifeSession: 長效session標識，當該參數爲1時，session的持續時間爲300s，但會一定程度上影響第一個數據包的返回速度，且TransmitOralProcess必須同時爲1才可生效。
        :type IsLongLifeSession: int
        :param StorageMode: 音訊儲存模式，0：不儲存，1：儲存到公共物件儲存，輸出結果爲該會話最後一個分片TransmitOralProcess 返回結果 AudioUrl 欄位。
        :type StorageMode: int
        :param SentenceInfoEnabled: 輸出斷句中間結果標識，0：不輸出，1：輸出，通過設置該參數，可以在評估過程中的分片傳輸請求中，返回已經評估斷句的中間結果，中間結果可用於用戶端 UI 更新，輸出結果爲TransmitOralProcess請求返回結果 SentenceInfoSet 欄位。
        :type SentenceInfoEnabled: int
        :param ServerType: 評估語言，0：英文，1：中文。
        :type ServerType: int
        :param IsAsync: 異步模式標識，0：同步模式，1：異步模式，可選值參考[服務模式](https://cloud.taifucloud.com/document/product/884/33697)。
        :type IsAsync: int
        :param TextMode: 輸入文本模式，0: 普通文本，1：[音素結構](https://cloud.taifucloud.com/document/product/884/33698)文本。
        :type TextMode: int
        """
        self.SessionId = None
        self.RefText = None
        self.WorkMode = None
        self.EvalMode = None
        self.ScoreCoeff = None
        self.SoeAppId = None
        self.IsLongLifeSession = None
        self.StorageMode = None
        self.SentenceInfoEnabled = None
        self.ServerType = None
        self.IsAsync = None
        self.TextMode = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        self.RefText = params.get("RefText")
        self.WorkMode = params.get("WorkMode")
        self.EvalMode = params.get("EvalMode")
        self.ScoreCoeff = params.get("ScoreCoeff")
        self.SoeAppId = params.get("SoeAppId")
        self.IsLongLifeSession = params.get("IsLongLifeSession")
        self.StorageMode = params.get("StorageMode")
        self.SentenceInfoEnabled = params.get("SentenceInfoEnabled")
        self.ServerType = params.get("ServerType")
        self.IsAsync = params.get("IsAsync")
        self.TextMode = params.get("TextMode")


class InitOralProcessResponse(AbstractModel):
    """InitOralProcess返回參數結構體

    """

    def __init__(self):
        """
        :param SessionId: 語音段唯一標識，一個完整語音一個SessionId
        :type SessionId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SessionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        self.RequestId = params.get("RequestId")


class PhoneInfo(AbstractModel):
    """單音節評價結果

    """

    def __init__(self):
        """
        :param MemBeginTime: 當前音節語音起始時間點，單位爲ms
        :type MemBeginTime: int
        :param MemEndTime: 當前音節語音終止時間點，單位爲ms
        :type MemEndTime: int
        :param PronAccuracy: 音節發音準确度，取值範圍[-1, 100]，當取-1時指完全不比對
        :type PronAccuracy: float
        :param DetectedStress: 當前音節是否檢測爲重音
        :type DetectedStress: bool
        :param Phone: 當前音節
        :type Phone: str
        :param Stress: 當前音節是否應爲重音
        :type Stress: bool
        """
        self.MemBeginTime = None
        self.MemEndTime = None
        self.PronAccuracy = None
        self.DetectedStress = None
        self.Phone = None
        self.Stress = None


    def _deserialize(self, params):
        self.MemBeginTime = params.get("MemBeginTime")
        self.MemEndTime = params.get("MemEndTime")
        self.PronAccuracy = params.get("PronAccuracy")
        self.DetectedStress = params.get("DetectedStress")
        self.Phone = params.get("Phone")
        self.Stress = params.get("Stress")


class SentenceInfo(AbstractModel):
    """語音過程中斷句的中間結果

    """

    def __init__(self):
        """
        :param SentenceId: 句子序號，在段落、自由說模式下有效，表示斷句序號，最後的綜合結果的爲-1.
        :type SentenceId: int
        :param Words: 詳細發音評估結果
        :type Words: list of WordRsp
        :param PronAccuracy: 發音精準度，取值範圍[-1, 100]，當取-1時指完全不比對，當爲句子模式時，是所有已識别單詞準确度的加權平均值，在reftext中但未識别出來的詞不計入分數中。
        :type PronAccuracy: float
        :param PronFluency: 發音流利度，取值範圍[0, 1]，當爲詞模式時，取值無意義；當爲流式模式且請求中IsEnd未置1時，取值無意義
        :type PronFluency: float
        :param PronCompletion: 發音完整度，取值範圍[0, 1]，當爲詞模式時，取值無意義；當爲流式模式且請求中IsEnd未置1時，取值無意義
        :type PronCompletion: float
        :param SuggestedScore: 建議評分，取值範圍[0,100]，評分方式爲建議評分 = 準确度（PronAccuracyfloat）* 完整度（PronCompletionfloat）*（2 - 完整度（PronCompletionfloat）），如若評分策略不符合請參考Words數組中的詳細分數自定義評分邏輯。
        :type SuggestedScore: float
        """
        self.SentenceId = None
        self.Words = None
        self.PronAccuracy = None
        self.PronFluency = None
        self.PronCompletion = None
        self.SuggestedScore = None


    def _deserialize(self, params):
        self.SentenceId = params.get("SentenceId")
        if params.get("Words") is not None:
            self.Words = []
            for item in params.get("Words"):
                obj = WordRsp()
                obj._deserialize(item)
                self.Words.append(obj)
        self.PronAccuracy = params.get("PronAccuracy")
        self.PronFluency = params.get("PronFluency")
        self.PronCompletion = params.get("PronCompletion")
        self.SuggestedScore = params.get("SuggestedScore")


class TransmitOralProcessRequest(AbstractModel):
    """TransmitOralProcess請求參數結構體

    """

    def __init__(self):
        """
        :param SeqId: 流式數據包的序號，從1開始，當IsEnd欄位爲1後後續序號無意義，當IsLongLifeSession不爲1且爲非流式模式時無意義。
        :type SeqId: int
        :param IsEnd: 是否傳輸完畢標志，若爲0表示未完畢，若爲1則傳輸完畢開始評估，非流式模式下無意義。
        :type IsEnd: int
        :param VoiceFileType: 語音文件類型 	1:raw, 2:wav, 3:mp3(三種格式目前僅支援16k采樣率16bit編碼單聲道，如有不一緻可能導緻評估不準确或失敗)。
        :type VoiceFileType: int
        :param VoiceEncodeType: 語音編碼類型	1:pcm。
        :type VoiceEncodeType: int
        :param UserVoiceData: 當前數據包數據, 流式模式下數據包大小可以按需設置，在網絡穩定時，分片大小建議設置0.5k，且必須保證分片幀完整（16bit的數據必須保證音訊長度爲偶數），編碼格式要求爲BASE64。
        :type UserVoiceData: str
        :param SessionId: 語音段唯一標識，一個完整語音一個SessionId。
        :type SessionId: str
        :param SoeAppId: 業務應用ID，與賬號應用APPID無關，是用來方便客戶管理服務的參數，新的 SoeAppId 可以在[控制台](https://console.cloud.taifucloud.com/soe)【應用管理】下新建。
        :type SoeAppId: str
        :param IsLongLifeSession: 長效session標識，當該參數爲1時，session的持續時間爲300s，但會一定程度上影響第一個數據包的返回速度。當InitOralProcess介面調用時此項爲1時，此項必填1才可生效。
        :type IsLongLifeSession: int
        :param IsQuery: 查詢標識，當該參數爲1時，該請求爲查詢請求，請求返回該 Session 的評估結果。
        :type IsQuery: int
        """
        self.SeqId = None
        self.IsEnd = None
        self.VoiceFileType = None
        self.VoiceEncodeType = None
        self.UserVoiceData = None
        self.SessionId = None
        self.SoeAppId = None
        self.IsLongLifeSession = None
        self.IsQuery = None


    def _deserialize(self, params):
        self.SeqId = params.get("SeqId")
        self.IsEnd = params.get("IsEnd")
        self.VoiceFileType = params.get("VoiceFileType")
        self.VoiceEncodeType = params.get("VoiceEncodeType")
        self.UserVoiceData = params.get("UserVoiceData")
        self.SessionId = params.get("SessionId")
        self.SoeAppId = params.get("SoeAppId")
        self.IsLongLifeSession = params.get("IsLongLifeSession")
        self.IsQuery = params.get("IsQuery")


class TransmitOralProcessResponse(AbstractModel):
    """TransmitOralProcess返回參數結構體

    """

    def __init__(self):
        """
        :param PronAccuracy: 發音精準度，取值範圍[-1, 100]，當取-1時指完全不比對，當爲句子模式時，是所有已識别單詞準确度的加權平均值，在reftext中但未識别出來的詞不計入分數中。當爲流式模式且請求中IsEnd未置1時，取值無意義。
        :type PronAccuracy: float
        :param PronFluency: 發音流利度，取值範圍[0, 1]，當爲詞模式時，取值無意義；當爲流式模式且請求中IsEnd未置1時，取值無意義
        :type PronFluency: float
        :param PronCompletion: 發音完整度，取值範圍[0, 1]，當爲詞模式時，取值無意義；當爲流式模式且請求中IsEnd未置1時，取值無意義
        :type PronCompletion: float
        :param Words: 詳細發音評估結果
        :type Words: list of WordRsp
        :param SessionId: 語音段唯一標識，一段語音一個SessionId
        :type SessionId: str
        :param AudioUrl: 保存語音音訊文件下載網址
        :type AudioUrl: str
        :param SentenceInfoSet: 斷句中間結果，中間結果是局部最優而非全局最優的結果，所以中間結果有可能和最終整體結果對應部分不一緻；中間結果的輸出便於用戶端UI更新；待用戶發音完全結束後，系統會給出一個綜合所有句子的整體結果。
        :type SentenceInfoSet: list of SentenceInfo
        :param Status: 評估 session 狀态，“Evaluating"：評估中、"Failed"：評估失敗、"Finished"：評估完成
        :type Status: str
        :param SuggestedScore: 建議評分，取值範圍[0,100]，評分方式爲建議評分 = 準确度（PronAccuracyfloat）× 完整度（PronCompletionfloat）×（2 - 完整度（PronCompletionfloat）），如若評分策略不符合請參考Words數組中的詳細分數自定義評分邏輯。
        :type SuggestedScore: float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PronAccuracy = None
        self.PronFluency = None
        self.PronCompletion = None
        self.Words = None
        self.SessionId = None
        self.AudioUrl = None
        self.SentenceInfoSet = None
        self.Status = None
        self.SuggestedScore = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PronAccuracy = params.get("PronAccuracy")
        self.PronFluency = params.get("PronFluency")
        self.PronCompletion = params.get("PronCompletion")
        if params.get("Words") is not None:
            self.Words = []
            for item in params.get("Words"):
                obj = WordRsp()
                obj._deserialize(item)
                self.Words.append(obj)
        self.SessionId = params.get("SessionId")
        self.AudioUrl = params.get("AudioUrl")
        if params.get("SentenceInfoSet") is not None:
            self.SentenceInfoSet = []
            for item in params.get("SentenceInfoSet"):
                obj = SentenceInfo()
                obj._deserialize(item)
                self.SentenceInfoSet.append(obj)
        self.Status = params.get("Status")
        self.SuggestedScore = params.get("SuggestedScore")
        self.RequestId = params.get("RequestId")


class TransmitOralProcessWithInitRequest(AbstractModel):
    """TransmitOralProcessWithInit請求參數結構體

    """

    def __init__(self):
        """
        :param SeqId: 流式數據包的序號，從1開始，當IsEnd欄位爲1後後續序號無意義，當IsLongLifeSession不爲1且爲非流式模式時無意義。
        :type SeqId: int
        :param IsEnd: 是否傳輸完畢標志，若爲0表示未完畢，若爲1則傳輸完畢開始評估，非流式模式下無意義。
        :type IsEnd: int
        :param VoiceFileType: 語音文件類型 	1:raw, 2:wav, 3:mp3(三種格式目前僅支援16k采樣率16bit編碼單聲道，如有不一緻可能導緻評估不準确或失敗)。
        :type VoiceFileType: int
        :param VoiceEncodeType: 語音編碼類型	1:pcm。
        :type VoiceEncodeType: int
        :param UserVoiceData: 當前數據包數據, 流式模式下數據包大小可以按需設置，在網絡良好的情況下，建議設置爲0.5k，且必須保證分片幀完整（16bit的數據必須保證音訊長度爲偶數），編碼格式要求爲BASE64。
        :type UserVoiceData: str
        :param SessionId: 語音段唯一標識，一個完整語音一個SessionId。
        :type SessionId: str
        :param RefText: 被評估語音對應的文本，句子模式下不超過個 20 單詞或者中文文字，段落模式不超過 120 單詞或者中文文字，中文評估使用 utf-8 編碼，自由說模式該值無效。如需要在單詞模式和句子模式下使用自定義音素，可以通過設置 TextMode 使用[音素標注](https://cloud.taifucloud.com/document/product/884/33698)。
        :type RefText: str
        :param WorkMode: 語音輸入模式，0：流式分片，1：非流式一次性評估
        :type WorkMode: int
        :param EvalMode: 評估模式，0：詞模式（中文評測模式下爲文字模式），1：句子模式，2：段落模式，3：自由說模式，當爲詞模式評估時，能夠提供每個音節的評估訊息，當爲句子模式時，能夠提供完整度和流利度訊息。
        :type EvalMode: int
        :param ScoreCoeff: 評價苛刻指數，取值爲[1.0 - 4.0]範圍内的浮點數，用於平滑不同年齡段的分數，1.0爲小年齡段，4.0爲最高年齡段
        :type ScoreCoeff: float
        :param SoeAppId: 業務應用ID，與賬號應用APPID無關，是用來方便客戶管理服務的參數，新的 SoeAppId 可以在[控制台](https://console.cloud.taifucloud.com/soe)【應用管理】下新建。
        :type SoeAppId: str
        :param StorageMode: 音訊儲存模式，0：不儲存，1：儲存到公共物件儲存，輸出結果爲該會話最後一個分片TransmitOralProcess 返回結果 AudioUrl 欄位。
        :type StorageMode: int
        :param SentenceInfoEnabled: 輸出斷句中間結果標識，0：不輸出，1：輸出，通過設置該參數，可以在評估過程中的分片傳輸請求中，返回已經評估斷句的中間結果，中間結果可用於用戶端 UI 更新，輸出結果爲TransmitOralProcess請求返回結果 SentenceInfoSet 欄位。
        :type SentenceInfoEnabled: int
        :param ServerType: 評估語言，0：英文，1：中文。
        :type ServerType: int
        :param IsAsync: 異步模式標識，0：同步模式，1：異步模式，可選值參考[服務模式](https://cloud.taifucloud.com/document/product/884/33697)。
        :type IsAsync: int
        :param IsQuery: 查詢標識，當該參數爲1時，該請求爲查詢請求，請求返回該 Session 評估結果。
        :type IsQuery: int
        :param TextMode: 輸入文本模式，0: 普通文本，1：[音素結構](https://cloud.taifucloud.com/document/product/884/33698)文本。
        :type TextMode: int
        """
        self.SeqId = None
        self.IsEnd = None
        self.VoiceFileType = None
        self.VoiceEncodeType = None
        self.UserVoiceData = None
        self.SessionId = None
        self.RefText = None
        self.WorkMode = None
        self.EvalMode = None
        self.ScoreCoeff = None
        self.SoeAppId = None
        self.StorageMode = None
        self.SentenceInfoEnabled = None
        self.ServerType = None
        self.IsAsync = None
        self.IsQuery = None
        self.TextMode = None


    def _deserialize(self, params):
        self.SeqId = params.get("SeqId")
        self.IsEnd = params.get("IsEnd")
        self.VoiceFileType = params.get("VoiceFileType")
        self.VoiceEncodeType = params.get("VoiceEncodeType")
        self.UserVoiceData = params.get("UserVoiceData")
        self.SessionId = params.get("SessionId")
        self.RefText = params.get("RefText")
        self.WorkMode = params.get("WorkMode")
        self.EvalMode = params.get("EvalMode")
        self.ScoreCoeff = params.get("ScoreCoeff")
        self.SoeAppId = params.get("SoeAppId")
        self.StorageMode = params.get("StorageMode")
        self.SentenceInfoEnabled = params.get("SentenceInfoEnabled")
        self.ServerType = params.get("ServerType")
        self.IsAsync = params.get("IsAsync")
        self.IsQuery = params.get("IsQuery")
        self.TextMode = params.get("TextMode")


class TransmitOralProcessWithInitResponse(AbstractModel):
    """TransmitOralProcessWithInit返回參數結構體

    """

    def __init__(self):
        """
        :param PronAccuracy: 發音精準度，取值範圍[-1, 100]，當取-1時指完全不比對，當爲句子模式時，是所有已識别單詞準确度的加權平均值，在reftext中但未識别出來的詞不計入分數中。當爲流式模式且請求中IsEnd未置1時，取值無意義。
        :type PronAccuracy: float
        :param PronFluency: 發音流利度，取值範圍[0, 1]，當爲詞模式時，取值無意義；當爲流式模式且請求中IsEnd未置1時，取值無意義
        :type PronFluency: float
        :param PronCompletion: 發音完整度，取值範圍[0, 1]，當爲詞模式時，取值無意義；當爲流式模式且請求中IsEnd未置1時，取值無意義
        :type PronCompletion: float
        :param Words: 詳細發音評估結果
        :type Words: list of WordRsp
        :param SessionId: 語音段唯一標識，一段語音一個SessionId
        :type SessionId: str
        :param AudioUrl: 保存語音音訊文件下載網址
        :type AudioUrl: str
        :param SentenceInfoSet: 斷句中間結果，中間結果是局部最優而非全局最優的結果，所以中間結果有可能和最終整體結果對應部分不一緻；中間結果的輸出便於用戶端UI更新；待用戶發音完全結束後，系統會給出一個綜合所有句子的整體結果。
        :type SentenceInfoSet: list of SentenceInfo
        :param Status: 評估 session 狀态，“Evaluating"：評估中、"Failed"：評估失敗、"Finished"：評估完成
        :type Status: str
        :param SuggestedScore: 建議評分，取值範圍[0,100]，評分方式爲建議評分 = 準确度（PronAccuracyfloat）× 完整度（PronCompletionfloat）×（2 - 完整度（PronCompletionfloat）），如若評分策略不符合請參考Words數組中的詳細分數自定義評分邏輯。
        :type SuggestedScore: float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PronAccuracy = None
        self.PronFluency = None
        self.PronCompletion = None
        self.Words = None
        self.SessionId = None
        self.AudioUrl = None
        self.SentenceInfoSet = None
        self.Status = None
        self.SuggestedScore = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PronAccuracy = params.get("PronAccuracy")
        self.PronFluency = params.get("PronFluency")
        self.PronCompletion = params.get("PronCompletion")
        if params.get("Words") is not None:
            self.Words = []
            for item in params.get("Words"):
                obj = WordRsp()
                obj._deserialize(item)
                self.Words.append(obj)
        self.SessionId = params.get("SessionId")
        self.AudioUrl = params.get("AudioUrl")
        if params.get("SentenceInfoSet") is not None:
            self.SentenceInfoSet = []
            for item in params.get("SentenceInfoSet"):
                obj = SentenceInfo()
                obj._deserialize(item)
                self.SentenceInfoSet.append(obj)
        self.Status = params.get("Status")
        self.SuggestedScore = params.get("SuggestedScore")
        self.RequestId = params.get("RequestId")


class WordRsp(AbstractModel):
    """單詞評分細則

    """

    def __init__(self):
        """
        :param MemBeginTime: 當前單詞語音起始時間點，單位爲ms
        :type MemBeginTime: int
        :param MemEndTime: 當前單詞語音終止時間點，單位爲ms
        :type MemEndTime: int
        :param PronAccuracy: 單詞發音準确度，取值範圍[-1, 100]，當取-1時指完全不比對
        :type PronAccuracy: float
        :param PronFluency: 單詞發音流利度，取值範圍[0, 1]
        :type PronFluency: float
        :param Word: 當前詞
        :type Word: str
        :param MatchTag: 當前詞與輸入語句的比對情況，0：比對單詞、1：新增單詞、2：缺少單詞、3：錯讀的詞、4：未錄入單詞。
        :type MatchTag: int
        :param PhoneInfos: 音節評估詳情
        :type PhoneInfos: list of PhoneInfo
        """
        self.MemBeginTime = None
        self.MemEndTime = None
        self.PronAccuracy = None
        self.PronFluency = None
        self.Word = None
        self.MatchTag = None
        self.PhoneInfos = None


    def _deserialize(self, params):
        self.MemBeginTime = params.get("MemBeginTime")
        self.MemEndTime = params.get("MemEndTime")
        self.PronAccuracy = params.get("PronAccuracy")
        self.PronFluency = params.get("PronFluency")
        self.Word = params.get("Word")
        self.MatchTag = params.get("MatchTag")
        if params.get("PhoneInfos") is not None:
            self.PhoneInfos = []
            for item in params.get("PhoneInfos"):
                obj = PhoneInfo()
                obj._deserialize(item)
                self.PhoneInfos.append(obj)