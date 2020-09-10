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


class TextToVoiceRequest(AbstractModel):
    """TextToVoice請求參數結構體

    """

    def __init__(self):
        """
        :param Text: 合成語音的源文本，按UTF-8編碼統一計算。
中文最大支援110個漢字（全角标點符号算一個漢字）；英文最大支援350個字母（半角标點符号算一個字母）。
        :type Text: str
        :param SessionId: 一次請求對應一個SessionId，會原樣返回，建議傳入類似于uuid的字串防止重複。
        :type SessionId: str
        :param ModelType: 模型類型，1-預設模型。
        :type ModelType: int
        :param Volume: 音量大小，範圍：[0，10]，分别對應11個等級的音量，預設爲0，代表正常音量。沒有靜音選項。
輸入除以上整數之外的其他參數不生效，按預設值處理。
        :type Volume: float
        :param Speed: 語速，範圍：[-2，2]，分别對應不同語速：<li>-2代表0.6倍</li><li>-1代表0.8倍</li><li>0代表1.0倍（預設）</li><li>1代表1.2倍</li><li>2代表1.5倍</li>如果需要更細化的語速，可以保留小數點後一位，例如0.5 1.1 1.8等。<br>
        :type Speed: float
        :param ProjectId: 項目id，用戶自定義，預設爲0。
        :type ProjectId: int
        :param VoiceType: 音色<li>0-雲小甯，親和女聲(預設)</li><li>1-雲小奇，親和男聲</li><li>2-雲小晚，成熟男聲</li><li>4-雲小葉，溫暖女聲</li><li>5-雲小欣，情感女聲</li><li>6-雲小龍，情感男聲</li><li>7-雲小曼，客服女聲（新）</li><li>1000-智俠，情感男聲（新）</li><li>1001-智瑜，情感女聲（新）</li><li>1002-智聆，通用女聲（新）</li><li>1003-智美，客服女聲（新）</li><li>1050-WeJack，英文男聲（新）</li><li>1051-WeRose，英文女聲（新）</li>
        :type VoiceType: int
        :param PrimaryLanguage: 主語言類型：<li>1-中文（預設）</li><li>2-英文</li>
        :type PrimaryLanguage: int
        :param SampleRate: 音訊采樣率：<li>16000：16k（預設）</li><li>8000：8k</li>
        :type SampleRate: int
        :param Codec: 返回音訊格式，可取值：wav（預設），mp3
        :type Codec: str
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
        self.Codec = None


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
        self.Codec = params.get("Codec")


class TextToVoiceResponse(AbstractModel):
    """TextToVoice返回參數結構體

    """

    def __init__(self):
        """
        :param Audio: base64編碼的wav/mp3音訊數據
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