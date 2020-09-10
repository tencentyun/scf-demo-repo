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


class PostAudioRequest(AbstractModel):
    """PostAudio請求參數結構體

    """

    def __init__(self):
        """
        :param BotId: 機器人标識
        :type BotId: str
        :param EngineModelType: 語音識别引擎類型,{8k_0、16k_0、16k_en}
        :type EngineModelType: str
        :param AsrVoiceFormat: 輸入音訊文件編碼格式。1：wav(pcm)；4：speex(sp)；6：silk
        :type AsrVoiceFormat: int
        :param VoiceId: asr請求Id。長度爲16位的字串，同一句話VoiceId保持一緻
        :type VoiceId: str
        :param Seq: 語音分片序列号。同一句話必須從0開始，依次遞增
        :type Seq: int
        :param IsEnd: 是否爲尾包。傳遞最後一個語音分片時爲true，其他爲false
        :type IsEnd: bool
        :param WaveData: 待識别音訊位元流
        :type WaveData: str
        :param UserId: 子帳戶id，每個終端對應一個
        :type UserId: str
        :param BotVersion: 機器人版本号。BotVersion/BotEnv二選一：二者均填，僅BotVersion有效；二者均不填，預設BotEnv=dev
        :type BotVersion: str
        :param ResultTextFormat: 識别返回文本編碼格式	0：UTF-8（預設）；1：GB2312；2：GBK；3：BIG5
        :type ResultTextFormat: int
        :param SessionAttributes: 透傳欄位，傳遞給後台
        :type SessionAttributes: str
        :param NeedTts: 是否将機器人回答合成音訊并返回url
        :type NeedTts: bool
        :param Volume: 音量大小，範圍：[0，10]。預設值爲0，代表正常音量
        :type Volume: int
        :param Speed: 語速，範圍：[-2，2]。0代表1.0倍
        :type Speed: int
        :param VoiceType: 音色,{0：女聲,1:男聲}
        :type VoiceType: int
        :param SampleRate: 返回音訊的采樣率{8k,16k}。預設16k
        :type SampleRate: str
        :param BotEnv: 機器人環境{dev:測試;release:線上}。BotVersion/BotEnv二選一：二者均填，僅BotVersion有效；二者均不填，預設BotEnv=dev
        :type BotEnv: str
        :param TtsVoiceFormat: TTS合成音訊格式，{0：wav}。該欄位在當前版本僅支援取值爲0。
        :type TtsVoiceFormat: int
        """
        self.BotId = None
        self.EngineModelType = None
        self.AsrVoiceFormat = None
        self.VoiceId = None
        self.Seq = None
        self.IsEnd = None
        self.WaveData = None
        self.UserId = None
        self.BotVersion = None
        self.ResultTextFormat = None
        self.SessionAttributes = None
        self.NeedTts = None
        self.Volume = None
        self.Speed = None
        self.VoiceType = None
        self.SampleRate = None
        self.BotEnv = None
        self.TtsVoiceFormat = None


    def _deserialize(self, params):
        self.BotId = params.get("BotId")
        self.EngineModelType = params.get("EngineModelType")
        self.AsrVoiceFormat = params.get("AsrVoiceFormat")
        self.VoiceId = params.get("VoiceId")
        self.Seq = params.get("Seq")
        self.IsEnd = params.get("IsEnd")
        self.WaveData = params.get("WaveData")
        self.UserId = params.get("UserId")
        self.BotVersion = params.get("BotVersion")
        self.ResultTextFormat = params.get("ResultTextFormat")
        self.SessionAttributes = params.get("SessionAttributes")
        self.NeedTts = params.get("NeedTts")
        self.Volume = params.get("Volume")
        self.Speed = params.get("Speed")
        self.VoiceType = params.get("VoiceType")
        self.SampleRate = params.get("SampleRate")
        self.BotEnv = params.get("BotEnv")
        self.TtsVoiceFormat = params.get("TtsVoiceFormat")


class PostAudioResponse(AbstractModel):
    """PostAudio返回參數結構體

    """

    def __init__(self):
        """
        :param DialogStatus: 當前會話狀态。取值:"start"/"continue"/"complete"
注意：此欄位可能返回 null，表示取不到有效值。
        :type DialogStatus: str
        :param BotName: 比對到的機器人名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type BotName: str
        :param IntentName: 比對到的意圖名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type IntentName: str
        :param ResponseText: 機器人應答文本
        :type ResponseText: str
        :param SlotInfoList: 語義解析的槽位結果清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type SlotInfoList: list of SlotInfo
        :param SessionAttributes: 透傳欄位
注意：此欄位可能返回 null，表示取不到有效值。
        :type SessionAttributes: str
        :param Question: 用戶說法。該說法是用戶原生說法或ASR識别結果，未經過語義優化
注意：此欄位可能返回 null，表示取不到有效值。
        :type Question: str
        :param WaveUrl: tts合成pcm音訊儲存連結。僅當請求參數NeedTts=true時返回
注意：此欄位可能返回 null，表示取不到有效值。
        :type WaveUrl: str
        :param WaveData: tts合成pcm音訊
注意：此欄位可能返回 null，表示取不到有效值。
        :type WaveData: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DialogStatus = None
        self.BotName = None
        self.IntentName = None
        self.ResponseText = None
        self.SlotInfoList = None
        self.SessionAttributes = None
        self.Question = None
        self.WaveUrl = None
        self.WaveData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DialogStatus = params.get("DialogStatus")
        self.BotName = params.get("BotName")
        self.IntentName = params.get("IntentName")
        self.ResponseText = params.get("ResponseText")
        if params.get("SlotInfoList") is not None:
            self.SlotInfoList = []
            for item in params.get("SlotInfoList"):
                obj = SlotInfo()
                obj._deserialize(item)
                self.SlotInfoList.append(obj)
        self.SessionAttributes = params.get("SessionAttributes")
        self.Question = params.get("Question")
        self.WaveUrl = params.get("WaveUrl")
        self.WaveData = params.get("WaveData")
        self.RequestId = params.get("RequestId")


class PostTextRequest(AbstractModel):
    """PostText請求參數結構體

    """

    def __init__(self):
        """
        :param BotId: 機器人标識
        :type BotId: str
        :param InputText: 請求的文本
        :type InputText: str
        :param UserId: 子帳戶id，每個終端對應一個
        :type UserId: str
        :param BotVersion: 機器人版本号。BotVersion/BotEnv二選一：二者均填，僅BotVersion有效；二者均不填，預設BotEnv=dev
        :type BotVersion: str
        :param SessionAttributes: 透傳欄位，傳遞給後台
        :type SessionAttributes: str
        :param NeedTts: 是否将機器人回答合成音訊并返回url
        :type NeedTts: bool
        :param Volume: 音量大小，範圍：[0，10]。預設值爲0，代表正常音量
        :type Volume: int
        :param Speed: 語速，範圍：[-2，2]。0代表1.0倍
        :type Speed: int
        :param VoiceType: 音色,{0：女聲,1:男聲}
        :type VoiceType: int
        :param SampleRate: 返回音訊的采樣率{8k,16k}。預設16k
        :type SampleRate: str
        :param BotEnv: 機器人環境{dev:測試;release:線上}。BotVersion/BotEnv二選一：二者均填，僅BotVersion有效；二者均不填，預設BotEnv=dev
        :type BotEnv: str
        :param TtsVoiceFormat: TTS合成音訊格式，{0：wav}。該欄位在當前版本僅支援取值爲0。
        :type TtsVoiceFormat: int
        """
        self.BotId = None
        self.InputText = None
        self.UserId = None
        self.BotVersion = None
        self.SessionAttributes = None
        self.NeedTts = None
        self.Volume = None
        self.Speed = None
        self.VoiceType = None
        self.SampleRate = None
        self.BotEnv = None
        self.TtsVoiceFormat = None


    def _deserialize(self, params):
        self.BotId = params.get("BotId")
        self.InputText = params.get("InputText")
        self.UserId = params.get("UserId")
        self.BotVersion = params.get("BotVersion")
        self.SessionAttributes = params.get("SessionAttributes")
        self.NeedTts = params.get("NeedTts")
        self.Volume = params.get("Volume")
        self.Speed = params.get("Speed")
        self.VoiceType = params.get("VoiceType")
        self.SampleRate = params.get("SampleRate")
        self.BotEnv = params.get("BotEnv")
        self.TtsVoiceFormat = params.get("TtsVoiceFormat")


class PostTextResponse(AbstractModel):
    """PostText返回參數結構體

    """

    def __init__(self):
        """
        :param DialogStatus: 當前會話狀态。取值:"start"/"continue"/"complete"
注意：此欄位可能返回 null，表示取不到有效值。
        :type DialogStatus: str
        :param BotName: 比對到的機器人名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type BotName: str
        :param IntentName: 比對到的意圖名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type IntentName: str
        :param ResponseText: 機器人回答
        :type ResponseText: str
        :param SlotInfoList: 語義解析的槽位結果清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type SlotInfoList: list of SlotInfo
        :param SessionAttributes: 透傳欄位
注意：此欄位可能返回 null，表示取不到有效值。
        :type SessionAttributes: str
        :param Question: 用戶說法。該說法是用戶原生說法或ASR識别結果，未經過語義優化
        :type Question: str
        :param WaveUrl: tts合成pcm音訊儲存連結。僅當請求參數NeedTts=true時返回
注意：此欄位可能返回 null，表示取不到有效值。
        :type WaveUrl: str
        :param WaveData: tts合成的pcm音訊。二進制數組經過base64編碼(暫時不返回)
注意：此欄位可能返回 null，表示取不到有效值。
        :type WaveData: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DialogStatus = None
        self.BotName = None
        self.IntentName = None
        self.ResponseText = None
        self.SlotInfoList = None
        self.SessionAttributes = None
        self.Question = None
        self.WaveUrl = None
        self.WaveData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DialogStatus = params.get("DialogStatus")
        self.BotName = params.get("BotName")
        self.IntentName = params.get("IntentName")
        self.ResponseText = params.get("ResponseText")
        if params.get("SlotInfoList") is not None:
            self.SlotInfoList = []
            for item in params.get("SlotInfoList"):
                obj = SlotInfo()
                obj._deserialize(item)
                self.SlotInfoList.append(obj)
        self.SessionAttributes = params.get("SessionAttributes")
        self.Question = params.get("Question")
        self.WaveUrl = params.get("WaveUrl")
        self.WaveData = params.get("WaveData")
        self.RequestId = params.get("RequestId")


class ResetRequest(AbstractModel):
    """Reset請求參數結構體

    """

    def __init__(self):
        """
        :param BotId: 機器人标識
        :type BotId: str
        :param UserId: 子帳戶id，每個終端對應一個
        :type UserId: str
        :param BotVersion: 機器人版本号。BotVersion/BotEnv二選一：二者均填，僅BotVersion有效；二者均不填，預設BotEnv=dev
        :type BotVersion: str
        :param BotEnv: 機器人環境{dev:測試;release:線上}。BotVersion/BotEnv二選一：二者均填，僅BotVersion有效；二者均不填，預設BotEnv=dev
        :type BotEnv: str
        """
        self.BotId = None
        self.UserId = None
        self.BotVersion = None
        self.BotEnv = None


    def _deserialize(self, params):
        self.BotId = params.get("BotId")
        self.UserId = params.get("UserId")
        self.BotVersion = params.get("BotVersion")
        self.BotEnv = params.get("BotEnv")


class ResetResponse(AbstractModel):
    """Reset返回參數結構體

    """

    def __init__(self):
        """
        :param DialogStatus: 當前會話狀态。取值:"start"/"continue"/"complete"
注意：此欄位可能返回 null，表示取不到有效值。
        :type DialogStatus: str
        :param BotName: 比對到的機器人名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type BotName: str
        :param IntentName: 比對到的意圖名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type IntentName: str
        :param ResponseText: 機器人回答
        :type ResponseText: str
        :param SlotInfoList: 語義解析的槽位結果清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type SlotInfoList: list of SlotInfo
        :param SessionAttributes: 透傳欄位
注意：此欄位可能返回 null，表示取不到有效值。
        :type SessionAttributes: str
        :param Question: 用戶說法。該說法是用戶原生說法或ASR識别結果，未經過語義優化
注意：此欄位可能返回 null，表示取不到有效值。
        :type Question: str
        :param WaveUrl: tts合成pcm音訊儲存連結。僅當請求參數NeedTts=true時返回
注意：此欄位可能返回 null，表示取不到有效值。
        :type WaveUrl: str
        :param WaveData: tts合成的pcm音訊。二進制數組經過base64編碼(暫時不返回)
注意：此欄位可能返回 null，表示取不到有效值。
        :type WaveData: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DialogStatus = None
        self.BotName = None
        self.IntentName = None
        self.ResponseText = None
        self.SlotInfoList = None
        self.SessionAttributes = None
        self.Question = None
        self.WaveUrl = None
        self.WaveData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DialogStatus = params.get("DialogStatus")
        self.BotName = params.get("BotName")
        self.IntentName = params.get("IntentName")
        self.ResponseText = params.get("ResponseText")
        if params.get("SlotInfoList") is not None:
            self.SlotInfoList = []
            for item in params.get("SlotInfoList"):
                obj = SlotInfo()
                obj._deserialize(item)
                self.SlotInfoList.append(obj)
        self.SessionAttributes = params.get("SessionAttributes")
        self.Question = params.get("Question")
        self.WaveUrl = params.get("WaveUrl")
        self.WaveData = params.get("WaveData")
        self.RequestId = params.get("RequestId")


class SlotInfo(AbstractModel):
    """槽位訊息

    """

    def __init__(self):
        """
        :param SlotName: 槽位名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type SlotName: str
        :param SlotValue: 槽位值
注意：此欄位可能返回 null，表示取不到有效值。
        :type SlotValue: str
        """
        self.SlotName = None
        self.SlotValue = None


    def _deserialize(self, params):
        self.SlotName = params.get("SlotName")
        self.SlotValue = params.get("SlotValue")