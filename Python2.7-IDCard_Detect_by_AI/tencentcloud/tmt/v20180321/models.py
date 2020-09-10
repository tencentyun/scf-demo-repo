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


class ImageRecord(AbstractModel):
    """圖片翻譯結果

    """

    def __init__(self):
        """
        :param Value: 圖片翻譯結果
        :type Value: list of ItemValue
        """
        self.Value = None


    def _deserialize(self, params):
        if params.get("Value") is not None:
            self.Value = []
            for item in params.get("Value"):
                obj = ItemValue()
                obj._deserialize(item)
                self.Value.append(obj)


class ImageTranslateRequest(AbstractModel):
    """ImageTranslate請求參數結構體

    """

    def __init__(self):
        """
        :param SessionUuid: 唯一id，返回時原樣返回
        :type SessionUuid: str
        :param Scene: doc:文件掃描
        :type Scene: str
        :param Data: 圖片數據的Base64字串，圖片大小上限爲4M，建議對源圖片進行一定程度壓縮
        :type Data: str
        :param Source: 源語言，支援語言清單<li> zh : 中文 </li> <li> en : 英文 </li>
        :type Source: str
        :param Target: 目标語言，支援語言清單<li> zh : 中文 </li> <li> en : 英文 </li>
        :type Target: str
        :param ProjectId: 項目ID，可以根據控制台-賬号中心-項目管理中的配置填寫，如無配置請填寫預設項目ID:0
        :type ProjectId: int
        """
        self.SessionUuid = None
        self.Scene = None
        self.Data = None
        self.Source = None
        self.Target = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.SessionUuid = params.get("SessionUuid")
        self.Scene = params.get("Scene")
        self.Data = params.get("Data")
        self.Source = params.get("Source")
        self.Target = params.get("Target")
        self.ProjectId = params.get("ProjectId")


class ImageTranslateResponse(AbstractModel):
    """ImageTranslate返回參數結構體

    """

    def __init__(self):
        """
        :param SessionUuid: 請求的SessionUuid返回
        :type SessionUuid: str
        :param Source: 源語言
        :type Source: str
        :param Target: 目标語言
        :type Target: str
        :param ImageRecord: 圖片翻譯結果，翻譯結果按識别的文本每一行獨立翻譯，後續會推出按段落劃分并翻譯的版本
        :type ImageRecord: :class:`taifucloudcloud.tmt.v20180321.models.ImageRecord`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SessionUuid = None
        self.Source = None
        self.Target = None
        self.ImageRecord = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SessionUuid = params.get("SessionUuid")
        self.Source = params.get("Source")
        self.Target = params.get("Target")
        if params.get("ImageRecord") is not None:
            self.ImageRecord = ImageRecord()
            self.ImageRecord._deserialize(params.get("ImageRecord"))
        self.RequestId = params.get("RequestId")


class ItemValue(AbstractModel):
    """翻譯結果

    """

    def __init__(self):
        """
        :param SourceText: 識别出的源文
        :type SourceText: str
        :param TargetText: 翻譯後的譯文
        :type TargetText: str
        :param X: X坐标
        :type X: int
        :param Y: Y坐标
        :type Y: int
        :param W: 寬度
        :type W: int
        :param H: 高度
        :type H: int
        """
        self.SourceText = None
        self.TargetText = None
        self.X = None
        self.Y = None
        self.W = None
        self.H = None


    def _deserialize(self, params):
        self.SourceText = params.get("SourceText")
        self.TargetText = params.get("TargetText")
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.W = params.get("W")
        self.H = params.get("H")


class LanguageDetectRequest(AbstractModel):
    """LanguageDetect請求參數結構體

    """

    def __init__(self):
        """
        :param Text: 待識别的文本，文本統一使用utf-8格式編碼，非utf-8格式編碼字元會翻譯失敗。單次請求的文本長度需要低于2000。
        :type Text: str
        :param ProjectId: 項目ID，可以根據控制台-賬号中心-項目管理中的配置填寫，如無配置請填寫預設項目ID:0
        :type ProjectId: int
        """
        self.Text = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.ProjectId = params.get("ProjectId")


class LanguageDetectResponse(AbstractModel):
    """LanguageDetect返回參數結構體

    """

    def __init__(self):
        """
        :param Lang: 識别出的語言種類，參考語言清單
<li> zh : 中文 </li> <li> en : 英文 </li><li> jp : 日語 </li> <li> kr : 韓語 </li><li> de : 德語 </li><li> fr : 法語 </li><li> es : 西班牙文 </li> <li> it : 意大利文 </li><li> tr : 土耳其文 </li><li> ru : 俄文 </li><li> pt : 葡萄牙文 </li><li> vi : 越南文 </li><li> id : 印度尼西亞文 </li><li> ms : 馬來西亞文 </li><li> th : 泰文 </li>
        :type Lang: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Lang = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Lang = params.get("Lang")
        self.RequestId = params.get("RequestId")


class SpeechTranslateRequest(AbstractModel):
    """SpeechTranslate請求參數結構體

    """

    def __init__(self):
        """
        :param SessionUuid: 一段完整的語音對應一個SessionUuid
        :type SessionUuid: str
        :param Source: 音訊中的語言類型，支援語言清單<li> zh : 中文 </li> <li> en : 英文 </li>
        :type Source: str
        :param Target: 翻譯目标語⾔言類型 ，支援的語言清單<li> zh : 中文 </li> <li> en : 英文 </li>
        :type Target: str
        :param AudioFormat: pcm : 146   amr : 33554432   mp3 : 83886080
        :type AudioFormat: int
        :param Seq: 語音分片的序号，從0開始
        :type Seq: int
        :param IsEnd: 是否最後一片語音分片，0-否，1-是
        :type IsEnd: int
        :param Data: 語音分片内容的base64字元串，音訊内容應含有效并可識别的文本
        :type Data: str
        :param ProjectId: 項目ID，可以根據控制台-賬号中心-項目管理中的配置填寫，如無配置請填寫預設項目ID:0
        :type ProjectId: int
        :param Mode: 識别模式，不填則由調用放進行vad(靜音檢測)，填bvad則由服務放進行vad，前者适合段語音翻譯（收到所有語音分片後翻譯），後者适合長語音翻譯（在完成一個斷句識别後就會返回部分結果）
        :type Mode: str
        """
        self.SessionUuid = None
        self.Source = None
        self.Target = None
        self.AudioFormat = None
        self.Seq = None
        self.IsEnd = None
        self.Data = None
        self.ProjectId = None
        self.Mode = None


    def _deserialize(self, params):
        self.SessionUuid = params.get("SessionUuid")
        self.Source = params.get("Source")
        self.Target = params.get("Target")
        self.AudioFormat = params.get("AudioFormat")
        self.Seq = params.get("Seq")
        self.IsEnd = params.get("IsEnd")
        self.Data = params.get("Data")
        self.ProjectId = params.get("ProjectId")
        self.Mode = params.get("Mode")


class SpeechTranslateResponse(AbstractModel):
    """SpeechTranslate返回參數結構體

    """

    def __init__(self):
        """
        :param SessionUuid: 請求的SessionUuid直接返回
        :type SessionUuid: str
        :param RecognizeStatus: 語音識别狀态 1-進行中 0-完成
        :type RecognizeStatus: int
        :param SourceText: 識别出的源文
        :type SourceText: str
        :param TargetText: 翻譯出的譯文
        :type TargetText: str
        :param Seq: 第幾個語音分片
        :type Seq: int
        :param Source: 源語言
        :type Source: str
        :param Target: 目标語言
        :type Target: str
        :param VadSeq: 當請求的Mode參數填寫bvad是，啓動VadSeq。此時Seq會被設置爲後台vad（靜音檢測）後的新序号，而VadSeq代表用戶端原始Seq值
        :type VadSeq: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SessionUuid = None
        self.RecognizeStatus = None
        self.SourceText = None
        self.TargetText = None
        self.Seq = None
        self.Source = None
        self.Target = None
        self.VadSeq = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SessionUuid = params.get("SessionUuid")
        self.RecognizeStatus = params.get("RecognizeStatus")
        self.SourceText = params.get("SourceText")
        self.TargetText = params.get("TargetText")
        self.Seq = params.get("Seq")
        self.Source = params.get("Source")
        self.Target = params.get("Target")
        self.VadSeq = params.get("VadSeq")
        self.RequestId = params.get("RequestId")


class TextTranslateRequest(AbstractModel):
    """TextTranslate請求參數結構體

    """

    def __init__(self):
        """
        :param SourceText: 待翻譯的文本，文本統一使用utf-8格式編碼，非utf-8格式編碼字元會翻譯失敗，請傳入有效文本，html标記等非常規翻譯文本會翻譯失敗。單次請求的文本長度需要低于2000。
        :type SourceText: str
        :param Source: 源語言，參照Target支援語言清單
        :type Source: str
        :param Target: 目标語言，參照支援語言清單
<li> zh : 中文 </li> <li> en : 英文 </li><li> jp : 日語 </li> <li> kr : 韓語 </li><li> de : 德語 </li><li> fr : 法語 </li><li> es : 西班牙文 </li> <li> it : 意大利文 </li><li> tr : 土耳其文 </li><li> ru : 俄文 </li><li> pt : 葡萄牙文 </li><li> vi : 越南文 </li><li> id : 印度尼西亞文 </li><li> ms : 馬來西亞文 </li><li> th : 泰文 </li><li> auto : 自動識别源語言，只能用于source欄位 </li>
        :type Target: str
        :param ProjectId: 項目ID，可以根據控制台-賬号中心-項目管理中的配置填寫，如無配置請填寫預設項目ID:0
        :type ProjectId: int
        """
        self.SourceText = None
        self.Source = None
        self.Target = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.SourceText = params.get("SourceText")
        self.Source = params.get("Source")
        self.Target = params.get("Target")
        self.ProjectId = params.get("ProjectId")


class TextTranslateResponse(AbstractModel):
    """TextTranslate返回參數結構體

    """

    def __init__(self):
        """
        :param TargetText: 翻譯後的文本
        :type TargetText: str
        :param Source: 源語言，詳見入參Target
        :type Source: str
        :param Target: 目标語言，詳見入參Target
        :type Target: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TargetText = None
        self.Source = None
        self.Target = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TargetText = params.get("TargetText")
        self.Source = params.get("Source")
        self.Target = params.get("Target")
        self.RequestId = params.get("RequestId")