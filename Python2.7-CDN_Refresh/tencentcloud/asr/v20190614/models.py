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


class CreateAsrVocabRequest(AbstractModel):
    """CreateAsrVocab請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 熱詞表名稱，長度在1-255之間
        :type Name: str
        :param Description: 熱詞表描述，長度在0-1000之間
        :type Description: str
        :param WordWeights: 詞權重數組，包含全部的熱詞和對應的權重。每個熱詞的長度不大于10，權重爲[1,10]之間整數，數組長度不大于128
        :type WordWeights: list of HotWord
        :param WordWeightStr: 詞權重文件（純文本文件）的二進制base64編碼，以行分隔，每行的格式爲word|weight，即以英文符号|爲分割，左邊爲詞，右邊爲權重，如：你好|5。
當用戶傳此參數（參數長度大于0），即以此參數解析詞權重，WordWeights會被忽略
        :type WordWeightStr: str
        """
        self.Name = None
        self.Description = None
        self.WordWeights = None
        self.WordWeightStr = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("WordWeights") is not None:
            self.WordWeights = []
            for item in params.get("WordWeights"):
                obj = HotWord()
                obj._deserialize(item)
                self.WordWeights.append(obj)
        self.WordWeightStr = params.get("WordWeightStr")


class CreateAsrVocabResponse(AbstractModel):
    """CreateAsrVocab返回參數結構體

    """

    def __init__(self):
        """
        :param VocabId: 詞表ID，可用于獲取詞表訊息
        :type VocabId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.VocabId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VocabId = params.get("VocabId")
        self.RequestId = params.get("RequestId")


class CreateRecTaskRequest(AbstractModel):
    """CreateRecTask請求參數結構體

    """

    def __init__(self):
        """
        :param EngineModelType: 引擎模型類型。
8k_zh：電話 8k 中文普通話通用，可用于雙聲道音訊的識别；
8k_zh_s：電話 8k 中文普通話話者分離，僅用于單聲道；
16k_zh：16k 中文普通話通用；
16k_en：16k 英語；
16k_ca：16k 粵語；
16k_zh_video：16k 影音領域模型。
        :type EngineModelType: str
        :param ChannelNum: 語音聲道數。1：單聲道；2：雙聲道（僅支援 8k_zh 引擎模型）。
        :type ChannelNum: int
        :param ResTextFormat: 識别結果返回形式。0： 識别結果文本(含分段時間戳)； 1：僅支援16k中文引擎，含識别結果詳情(詞時間戳清單，一般用于生成字幕場景)。
        :type ResTextFormat: int
        :param SourceType: 語音數據來源。0：語音 URL；1：語音數據（post body）。
        :type SourceType: int
        :param CallbackUrl: 回調 URL，用戶自行搭建的用于接收識别結果的服務器網址， 長度小於2048位元。如果用戶使用回調方式獲取識别結果，需提交該參數；如果用戶使用輪詢方式獲取識别結果，則無需提交該參數。
        :type CallbackUrl: str
        :param Url: 語音的URL網址，需要公網可下載。長度小於2048位元，當 SourceType 值爲 0 時須填寫該欄位，爲 1 時不需要填寫。注意：請确保錄音文件時長在一個小時之内，否則可能識别失敗。請保證文件的下載速度，否則可能下載失敗。
        :type Url: str
        :param Data: 語音數據，當SourceType 值爲1時必須填寫，爲0可不寫。要base64編碼(采用python語言時注意讀取文件應該爲string而不是byte，以byte格式讀取後要decode()。編碼後的數據不可帶有回車換行符)。音訊數據要小於5MB。
        :type Data: str
        :param DataLen: 數據長度，當 SourceType 值爲1時必須填寫，爲0可不寫（此數據長度爲數據未進行base64編碼時的數據長度）。
        :type DataLen: int
        :param HotwordId: 熱詞id。用于調用對應的熱詞表，如果在調用語音識别服務時，不進行單獨的熱詞id設置，自動生效預設熱詞；如果進行了單獨的熱詞id設置，那麽将生效單獨設置的熱詞id。
        :type HotwordId: str
        :param FilterDirty: 是否過濾髒詞（目前支援中文普通話引擎）。0：不過濾髒詞；1：過濾髒詞；2：将髒詞替換爲 * 。
        :type FilterDirty: int
        :param FilterModal: 是否過語氣詞（目前支援中文普通話引擎）。0：不過濾語氣詞；1：部分過濾；2：嚴格過濾 。
        :type FilterModal: int
        """
        self.EngineModelType = None
        self.ChannelNum = None
        self.ResTextFormat = None
        self.SourceType = None
        self.CallbackUrl = None
        self.Url = None
        self.Data = None
        self.DataLen = None
        self.HotwordId = None
        self.FilterDirty = None
        self.FilterModal = None


    def _deserialize(self, params):
        self.EngineModelType = params.get("EngineModelType")
        self.ChannelNum = params.get("ChannelNum")
        self.ResTextFormat = params.get("ResTextFormat")
        self.SourceType = params.get("SourceType")
        self.CallbackUrl = params.get("CallbackUrl")
        self.Url = params.get("Url")
        self.Data = params.get("Data")
        self.DataLen = params.get("DataLen")
        self.HotwordId = params.get("HotwordId")
        self.FilterDirty = params.get("FilterDirty")
        self.FilterModal = params.get("FilterModal")


class CreateRecTaskResponse(AbstractModel):
    """CreateRecTask返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 錄音文件識别的請求返回結果，包含結果查詢需要的TaskId
        :type Data: :class:`tencentcloud.asr.v20190614.models.Task`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = Task()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DeleteAsrVocabRequest(AbstractModel):
    """DeleteAsrVocab請求參數結構體

    """

    def __init__(self):
        """
        :param VocabId: 熱詞表Id
        :type VocabId: str
        """
        self.VocabId = None


    def _deserialize(self, params):
        self.VocabId = params.get("VocabId")


class DeleteAsrVocabResponse(AbstractModel):
    """DeleteAsrVocab返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 從CreateRecTask介面獲取的TaskId，用于獲取任務狀态與結果。
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class DescribeTaskStatusResponse(AbstractModel):
    """DescribeTaskStatus返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 錄音文件識别的請求返回結果。
        :type Data: :class:`tencentcloud.asr.v20190614.models.TaskStatus`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = TaskStatus()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DownloadAsrVocabRequest(AbstractModel):
    """DownloadAsrVocab請求參數結構體

    """

    def __init__(self):
        """
        :param VocabId: 詞表ID。
        :type VocabId: str
        """
        self.VocabId = None


    def _deserialize(self, params):
        self.VocabId = params.get("VocabId")


class DownloadAsrVocabResponse(AbstractModel):
    """DownloadAsrVocab返回參數結構體

    """

    def __init__(self):
        """
        :param VocabId: 詞表ID。
        :type VocabId: str
        :param WordWeightStr: 詞表權重文件形式的base64值。
        :type WordWeightStr: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.VocabId = None
        self.WordWeightStr = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VocabId = params.get("VocabId")
        self.WordWeightStr = params.get("WordWeightStr")
        self.RequestId = params.get("RequestId")


class GetAsrVocabListRequest(AbstractModel):
    """GetAsrVocabList請求參數結構體

    """


class GetAsrVocabListResponse(AbstractModel):
    """GetAsrVocabList返回參數結構體

    """

    def __init__(self):
        """
        :param VocabList: 熱詞表清單
        :type VocabList: list of Vocab
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.VocabList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VocabList") is not None:
            self.VocabList = []
            for item in params.get("VocabList"):
                obj = Vocab()
                obj._deserialize(item)
                self.VocabList.append(obj)
        self.RequestId = params.get("RequestId")


class GetAsrVocabRequest(AbstractModel):
    """GetAsrVocab請求參數結構體

    """

    def __init__(self):
        """
        :param VocabId: 熱詞表ID
        :type VocabId: str
        """
        self.VocabId = None


    def _deserialize(self, params):
        self.VocabId = params.get("VocabId")


class GetAsrVocabResponse(AbstractModel):
    """GetAsrVocab返回參數結構體

    """

    def __init__(self):
        """
        :param Name: 熱詞表名稱
        :type Name: str
        :param Description: 熱詞表描述
        :type Description: str
        :param VocabId: 熱詞表ID
        :type VocabId: str
        :param WordWeights: 詞權重清單
        :type WordWeights: list of HotWord
        :param CreateTime: 詞表創建時間
        :type CreateTime: str
        :param UpdateTime: 詞表更新時間
        :type UpdateTime: str
        :param State: 熱詞表狀态，1爲預設狀态即在識别時預設加載該熱詞表進行識别，0爲初始狀态
        :type State: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.Description = None
        self.VocabId = None
        self.WordWeights = None
        self.CreateTime = None
        self.UpdateTime = None
        self.State = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.VocabId = params.get("VocabId")
        if params.get("WordWeights") is not None:
            self.WordWeights = []
            for item in params.get("WordWeights"):
                obj = HotWord()
                obj._deserialize(item)
                self.WordWeights.append(obj)
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.State = params.get("State")
        self.RequestId = params.get("RequestId")


class HotWord(AbstractModel):
    """熱詞的詞和權重

    """

    def __init__(self):
        """
        :param Word: 熱詞
        :type Word: str
        :param Weight: 權重
        :type Weight: int
        """
        self.Word = None
        self.Weight = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        self.Weight = params.get("Weight")


class SentenceDetail(AbstractModel):
    """單句的詳細識别結果，包含單個詞的時間偏移，一般用于生成字幕的場景。

    """

    def __init__(self):
        """
        :param FinalSentence: 單句最終識别結果
注意：此欄位可能返回 null，表示取不到有效值。
        :type FinalSentence: str
        :param SliceSentence: 單句中間識别結果，使用空格拆分爲多個詞
注意：此欄位可能返回 null，表示取不到有效值。
        :type SliceSentence: str
        :param StartMs: 單句開始時間（毫秒）
注意：此欄位可能返回 null，表示取不到有效值。
        :type StartMs: int
        :param EndMs: 單句結束時間（毫秒）
注意：此欄位可能返回 null，表示取不到有效值。
        :type EndMs: int
        :param WordsNum: 單句中詞個數
注意：此欄位可能返回 null，表示取不到有效值。
        :type WordsNum: int
        :param Words: 單句中詞詳情
注意：此欄位可能返回 null，表示取不到有效值。
        :type Words: list of SentenceWords
        """
        self.FinalSentence = None
        self.SliceSentence = None
        self.StartMs = None
        self.EndMs = None
        self.WordsNum = None
        self.Words = None


    def _deserialize(self, params):
        self.FinalSentence = params.get("FinalSentence")
        self.SliceSentence = params.get("SliceSentence")
        self.StartMs = params.get("StartMs")
        self.EndMs = params.get("EndMs")
        self.WordsNum = params.get("WordsNum")
        if params.get("Words") is not None:
            self.Words = []
            for item in params.get("Words"):
                obj = SentenceWords()
                obj._deserialize(item)
                self.Words.append(obj)


class SentenceRecognitionRequest(AbstractModel):
    """SentenceRecognition請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: Top Cloud 項目 ID，可填 0，總長度不超過 1024 位元。
        :type ProjectId: int
        :param SubServiceType: 子服務類型。2： 一句話識别。
        :type SubServiceType: int
        :param EngSerViceType: 引擎模型類型。
8k_zh：電話 8k 中文普通話通用；
16k_zh：16k 中文普通話通用；
16k_en：16k 英語；
16k_ca：16k 粵語。
        :type EngSerViceType: str
        :param SourceType: 語音數據來源。0：語音 URL；1：語音數據（post body）。
        :type SourceType: int
        :param VoiceFormat: 識别音訊的音訊格式。mp3、wav。
        :type VoiceFormat: str
        :param UsrAudioKey: 用戶端對此任務的唯一标識，用戶自助生成，用于用戶查找識别結果。
        :type UsrAudioKey: str
        :param Url: 語音 URL，公網可下載。當 SourceType 值爲 0（語音 URL上傳） 時須填寫該欄位，爲 1 時不填；URL 的長度大于 0，小於 2048，需進行urlencode編碼。音訊時間長度要小於60s。
        :type Url: str
        :param Data: 語音數據，當SourceType 值爲1（本地語音數據上傳）時必須填寫，當SourceType 值爲0（語音 URL上傳）可不寫。要使用base64編碼(采用python語言時注意讀取文件應該爲string而不是byte，以byte格式讀取後要decode()。編碼後的數據不可帶有回車換行符)。音訊數據要小於600KB。
        :type Data: str
        :param DataLen: 數據長度，單位爲位元。當 SourceType 值爲1（本地語音數據上傳）時必須填寫，當 SourceType 值爲0（語音 URL上傳）可不寫（此數據長度爲數據未進行base64編碼時的數據長度）。
        :type DataLen: int
        :param HotwordId: 熱詞id。用于調用對應的熱詞表，如果在調用語音識别服務時，不進行單獨的熱詞id設置，自動生效預設熱詞；如果進行了單獨的熱詞id設置，那麽将生效單獨設置的熱詞id。
        :type HotwordId: str
        :param FilterDirty: 是否過濾髒詞（目前支援中文普通話引擎）。0：不過濾髒詞；1：過濾髒詞；2：将髒詞替換爲 * 。
        :type FilterDirty: int
        :param FilterModal: 是否過語氣詞（目前支援中文普通話引擎）。0：不過濾語氣詞；1：部分過濾；2：嚴格過濾 。
        :type FilterModal: int
        :param FilterPunc: 是否過濾句末的句号（目前支援中文普通話引擎）。0：不過濾句末的句号；1：過濾句末的句号。
        :type FilterPunc: int
        """
        self.ProjectId = None
        self.SubServiceType = None
        self.EngSerViceType = None
        self.SourceType = None
        self.VoiceFormat = None
        self.UsrAudioKey = None
        self.Url = None
        self.Data = None
        self.DataLen = None
        self.HotwordId = None
        self.FilterDirty = None
        self.FilterModal = None
        self.FilterPunc = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.SubServiceType = params.get("SubServiceType")
        self.EngSerViceType = params.get("EngSerViceType")
        self.SourceType = params.get("SourceType")
        self.VoiceFormat = params.get("VoiceFormat")
        self.UsrAudioKey = params.get("UsrAudioKey")
        self.Url = params.get("Url")
        self.Data = params.get("Data")
        self.DataLen = params.get("DataLen")
        self.HotwordId = params.get("HotwordId")
        self.FilterDirty = params.get("FilterDirty")
        self.FilterModal = params.get("FilterModal")
        self.FilterPunc = params.get("FilterPunc")


class SentenceRecognitionResponse(AbstractModel):
    """SentenceRecognition返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 識别結果。
        :type Result: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class SentenceWords(AbstractModel):
    """識别結果中詞文本，以及對應時間偏移

    """

    def __init__(self):
        """
        :param Word: 詞文本
注意：此欄位可能返回 null，表示取不到有效值。
        :type Word: str
        :param OffsetStartMs: 在句子中的開始時間偏移量
注意：此欄位可能返回 null，表示取不到有效值。
        :type OffsetStartMs: int
        :param OffsetEndMs: 在句子中的結束時間偏移量
注意：此欄位可能返回 null，表示取不到有效值。
        :type OffsetEndMs: int
        """
        self.Word = None
        self.OffsetStartMs = None
        self.OffsetEndMs = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        self.OffsetStartMs = params.get("OffsetStartMs")
        self.OffsetEndMs = params.get("OffsetEndMs")


class SetVocabStateRequest(AbstractModel):
    """SetVocabState請求參數結構體

    """

    def __init__(self):
        """
        :param VocabId: 熱詞表ID。
        :type VocabId: str
        :param State: 熱詞表狀态，1：設爲預設狀态；0：設爲非預設狀态。
        :type State: int
        """
        self.VocabId = None
        self.State = None


    def _deserialize(self, params):
        self.VocabId = params.get("VocabId")
        self.State = params.get("State")


class SetVocabStateResponse(AbstractModel):
    """SetVocabState返回參數結構體

    """

    def __init__(self):
        """
        :param VocabId: 熱詞表ID
        :type VocabId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.VocabId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VocabId = params.get("VocabId")
        self.RequestId = params.get("RequestId")


class Task(AbstractModel):
    """錄音文件識别請求的返回數據

    """

    def __init__(self):
        """
        :param TaskId: 任務ID，可通過此ID在輪詢介面獲取識别狀态與結果
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class TaskStatus(AbstractModel):
    """獲取錄音識别結果結果的返回參數

    """

    def __init__(self):
        """
        :param TaskId: 任務标識。
        :type TaskId: int
        :param Status: 任務狀态碼，0：任務等待，1：任務執行中，2：任務成功，3：任務失敗。
        :type Status: int
        :param StatusStr: 任務狀态，waiting：任務等待，doing：任務執行中，success：任務成功，failed：任務失敗。
        :type StatusStr: str
        :param Result: 識别結果。
        :type Result: str
        :param ErrorMsg: 失敗原因說明。
        :type ErrorMsg: str
        :param ResultDetail: 識别結果詳情，包含每個句子中的詞時間偏移，一般用于生成字幕的場景。(錄音識别請求中ResTextFormat=1時該欄位不爲空)
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResultDetail: list of SentenceDetail
        """
        self.TaskId = None
        self.Status = None
        self.StatusStr = None
        self.Result = None
        self.ErrorMsg = None
        self.ResultDetail = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.StatusStr = params.get("StatusStr")
        self.Result = params.get("Result")
        self.ErrorMsg = params.get("ErrorMsg")
        if params.get("ResultDetail") is not None:
            self.ResultDetail = []
            for item in params.get("ResultDetail"):
                obj = SentenceDetail()
                obj._deserialize(item)
                self.ResultDetail.append(obj)


class UpdateAsrVocabRequest(AbstractModel):
    """UpdateAsrVocab請求參數結構體

    """

    def __init__(self):
        """
        :param VocabId: 熱詞表ID
        :type VocabId: str
        :param Name: 熱詞表名稱
        :type Name: str
        :param WordWeights: 詞權重數組，包含全部的熱詞和對應的權重。每個熱詞的長度不大于10，權重爲[1,10]之間整數，數組長度不大于128
        :type WordWeights: list of HotWord
        :param WordWeightStr: 詞權重文件（純文本文件）的二進制base64編碼，以行分隔，每行的格式爲word|weight，即以英文符号|爲分割，左邊爲詞，右邊爲權重，如：你好|5。
當用戶傳此參數（參數長度大于0），即以此參數解析詞權重，WordWeights會被忽略
        :type WordWeightStr: str
        :param Description: 熱詞表描述
        :type Description: str
        """
        self.VocabId = None
        self.Name = None
        self.WordWeights = None
        self.WordWeightStr = None
        self.Description = None


    def _deserialize(self, params):
        self.VocabId = params.get("VocabId")
        self.Name = params.get("Name")
        if params.get("WordWeights") is not None:
            self.WordWeights = []
            for item in params.get("WordWeights"):
                obj = HotWord()
                obj._deserialize(item)
                self.WordWeights.append(obj)
        self.WordWeightStr = params.get("WordWeightStr")
        self.Description = params.get("Description")


class UpdateAsrVocabResponse(AbstractModel):
    """UpdateAsrVocab返回參數結構體

    """

    def __init__(self):
        """
        :param VocabId: 熱詞表ID
        :type VocabId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.VocabId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VocabId = params.get("VocabId")
        self.RequestId = params.get("RequestId")


class Vocab(AbstractModel):
    """詞表内容

    """

    def __init__(self):
        """
        :param Name: 熱詞表名稱
        :type Name: str
        :param Description: 熱詞表描述
        :type Description: str
        :param VocabId: 熱詞表ID
        :type VocabId: str
        :param WordWeights: 詞權重清單
        :type WordWeights: list of HotWord
        :param CreateTime: 詞表創建時間
        :type CreateTime: str
        :param UpdateTime: 詞表更新時間
        :type UpdateTime: str
        :param State: 熱詞表狀态，1爲預設狀态即在識别時預設加載該熱詞表進行識别，0爲初始狀态
        :type State: int
        """
        self.Name = None
        self.Description = None
        self.VocabId = None
        self.WordWeights = None
        self.CreateTime = None
        self.UpdateTime = None
        self.State = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.VocabId = params.get("VocabId")
        if params.get("WordWeights") is not None:
            self.WordWeights = []
            for item in params.get("WordWeights"):
                obj = HotWord()
                obj._deserialize(item)
                self.WordWeights.append(obj)
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.State = params.get("State")