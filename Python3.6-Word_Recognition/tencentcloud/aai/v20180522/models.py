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


class ChatRequest(AbstractModel):
    """Chat請求參數結構體

    """

    def __init__(self):
        """
        :param Text: 聊天輸入文本
        :type Text: str
        :param ProjectId: Top Cloud 項目 ID，可填 0，總長度不超過 1024 位元。
        :type ProjectId: int
        :param User: json格式，比如 {"id":"test","gender":"male"}。記錄當前與機器人交互的用戶id，非必須但強烈建議傳入，否則多輪聊天功能會受影響
        :type User: str
        """
        self.Text = None
        self.ProjectId = None
        self.User = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.ProjectId = params.get("ProjectId")
        self.User = params.get("User")


class ChatResponse(AbstractModel):
    """Chat返回參數結構體

    """

    def __init__(self):
        """
        :param Answer: 聊天輸出文本
        :type Answer: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Answer = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Answer = params.get("Answer")
        self.RequestId = params.get("RequestId")


class SentenceRecognitionRequest(AbstractModel):
    """SentenceRecognition請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: Top Cloud 項目 ID，可填 0，總長度不超過 1024 位元。
        :type ProjectId: int
        :param SubServiceType: 子服務類型。2，一句話識别。
        :type SubServiceType: int
        :param EngSerViceType: 引擎類型。8k：電話 8k 通用模型；16k：16k 通用模型。只支援單聲道音訊識别。
        :type EngSerViceType: str
        :param SourceType: 語音數據來源。0：語音 URL；1：語音數據（post body）。
        :type SourceType: int
        :param VoiceFormat: 識别音訊的音訊格式（支援mp3,wav）。
        :type VoiceFormat: str
        :param UsrAudioKey: 用戶端對此任務的唯一标識，用戶自助生成，用于用戶查找識别結果。
        :type UsrAudioKey: str
        :param Url: 語音 URL，公網可下載。當 SourceType 值爲 0 時須填寫該欄位，爲 1 時不填；URL 的長度大于 0，小於 2048，需進行urlencode編碼。音訊時間長度要小於60s。
        :type Url: str
        :param Data: 語音數據，當SourceType 值爲1時必須填寫，爲0可不寫。要base64編碼(采用python語言時注意讀取文件應該爲string而不是byte，以byte格式讀取後要decode()。編碼後的數據不可帶有回車換行符)。音訊數據要小於600kB。
        :type Data: str
        :param DataLen: 數據長度，當 SourceType 值爲1時必須填寫，爲0可不寫（此數據長度爲數據未進行base64編碼時的數據長度）。
        :type DataLen: int
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


class SimultaneousInterpretingRequest(AbstractModel):
    """SimultaneousInterpreting請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: Top Cloud 項目 ID，可填 0，總長度不超過 1024 位元。
        :type ProjectId: int
        :param SubServiceType: 子服務類型。0：離線語音識别。1：實時流式識别，2，一句話識别。3：同傳。
        :type SubServiceType: int
        :param RecEngineModelType: 識别引擎類型。8k_zh： 8k 中文會場模型；16k_zh：16k 中文會場模型，8k_en： 8k 英文會場模型；16k_en：16k 英文會場模型。當前僅支援16K。
        :type RecEngineModelType: str
        :param Data: 語音數據，要base64編碼。
        :type Data: str
        :param DataLen: 數據長度。
        :type DataLen: int
        :param VoiceId: 聲音id，标識一句話。
        :type VoiceId: str
        :param IsEnd: 是否是一句話的結束。
        :type IsEnd: int
        :param VoiceFormat: 聲音編碼的格式1:pcm，4:speex，6:silk，預設爲1。
        :type VoiceFormat: int
        :param OpenTranslate: 是否需要翻譯結果，1表示需要翻譯，0是不需要。
        :type OpenTranslate: int
        :param SourceLanguage: 如果需要翻譯，表示源語言類型，可取值：zh，en。
        :type SourceLanguage: str
        :param TargetLanguage: 如果需要翻譯，表示目标語言類型，可取值：zh，en。
        :type TargetLanguage: str
        :param Seq: 表明當前語音分片的索引，從0開始
        :type Seq: int
        """
        self.ProjectId = None
        self.SubServiceType = None
        self.RecEngineModelType = None
        self.Data = None
        self.DataLen = None
        self.VoiceId = None
        self.IsEnd = None
        self.VoiceFormat = None
        self.OpenTranslate = None
        self.SourceLanguage = None
        self.TargetLanguage = None
        self.Seq = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.SubServiceType = params.get("SubServiceType")
        self.RecEngineModelType = params.get("RecEngineModelType")
        self.Data = params.get("Data")
        self.DataLen = params.get("DataLen")
        self.VoiceId = params.get("VoiceId")
        self.IsEnd = params.get("IsEnd")
        self.VoiceFormat = params.get("VoiceFormat")
        self.OpenTranslate = params.get("OpenTranslate")
        self.SourceLanguage = params.get("SourceLanguage")
        self.TargetLanguage = params.get("TargetLanguage")
        self.Seq = params.get("Seq")


class SimultaneousInterpretingResponse(AbstractModel):
    """SimultaneousInterpreting返回參數結構體

    """

    def __init__(self):
        """
        :param AsrText: 語音識别的結果
        :type AsrText: str
        :param NmtText: 機器翻譯的結果
        :type NmtText: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AsrText = None
        self.NmtText = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsrText = params.get("AsrText")
        self.NmtText = params.get("NmtText")
        self.RequestId = params.get("RequestId")


class TextToVoiceRequest(AbstractModel):
    """TextToVoice請求參數結構體

    """

    def __init__(self):
        """
        :param Text: 合成語音的源文本，按UTF-8編碼統一計算，中文最大支援350字元，英文最大支援500字元
        :type Text: str
        :param SessionId: 一次請求對應一個SessionId，會原樣返回，建議傳入類似于uuid的字串防止重複。
        :type SessionId: str
        :param ModelType: 模型類型，1-預設模型。
        :type ModelType: int
        :param Volume: 音量大小，範圍：[0，10]，分别對應11個等級的音量，預設爲0，代表正常音量。沒有靜音選項。
輸入除以上整數之外的其他參數不生效，按預設值處理。
        :type Volume: float
        :param Speed: 語速，範圍：[-2，2]，分别對應不同語速：<li>-2代表0.6倍</li><li>-1代表0.8倍</li><li>0代表1.0倍（預設）</li><li>1代表1.2倍</li><li>2代表1.5倍</li>輸入除以上整數之外的其他參數不生效，按預設值處理。
        :type Speed: float
        :param ProjectId: 項目id，用戶自定義，預設爲0。
        :type ProjectId: int
        :param VoiceType: 音色<li>0-親和女聲預設)</li><li>1-親和男聲</li><li>2-成熟男聲</li><li>3-活力男聲</li><li>4-溫暖女聲</li><li>5-情感女聲</li><li>6-情感男聲</li>
        :type VoiceType: int
        :param PrimaryLanguage: 主語言類型：<li>1-中文（預設）</li><li>2-英文</li>
        :type PrimaryLanguage: int
        :param SampleRate: 音訊采樣率：<li>16000：16k（預設）</li><li>8000：8k</li>
        :type SampleRate: int
        """
        self.Text = None
        self.SessionId = None
        self.ModelType = None
        self.Volume = None
        self.Speed = None
        self.ProjectId = None
        self.VoiceType = None
        self.PrimaryLanguage = None
        self.SampleRate = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.SessionId = params.get("SessionId")
        self.ModelType = params.get("ModelType")
        self.Volume = params.get("Volume")
        self.Speed = params.get("Speed")
        self.ProjectId = params.get("ProjectId")
        self.VoiceType = params.get("VoiceType")
        self.PrimaryLanguage = params.get("PrimaryLanguage")
        self.SampleRate = params.get("SampleRate")


class TextToVoiceResponse(AbstractModel):
    """TextToVoice返回參數結構體

    """

    def __init__(self):
        """
        :param Audio: base64編碼的wav音訊數據
        :type Audio: str
        :param SessionId: 一次請求對應一個SessionId
        :type SessionId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Audio = None
        self.SessionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Audio = params.get("Audio")
        self.SessionId = params.get("SessionId")
        self.RequestId = params.get("RequestId")