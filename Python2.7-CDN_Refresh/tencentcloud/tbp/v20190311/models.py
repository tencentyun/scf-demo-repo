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


class CreateBotRequest(AbstractModel):
    """CreateBot請求參數結構體

    """

    def __init__(self):
        """
        :param BotName: 機器人名稱
        :type BotName: str
        :param BotCnName: 機器人中文名稱
        :type BotCnName: str
        """
        self.BotName = None
        self.BotCnName = None


    def _deserialize(self, params):
        self.BotName = params.get("BotName")
        self.BotCnName = params.get("BotCnName")


class CreateBotResponse(AbstractModel):
    """CreateBot返回參數結構體

    """

    def __init__(self):
        """
        :param TaskRequestId: 任務ID
        :type TaskRequestId: str
        :param Msg: 任務訊息
        :type Msg: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskRequestId = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskRequestId = params.get("TaskRequestId")
        self.Msg = params.get("Msg")
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


class TextProcessRequest(AbstractModel):
    """TextProcess請求參數結構體

    """

    def __init__(self):
        """
        :param BotId: 機器人标識，用于定義抽象機器人。
        :type BotId: str
        :param TerminalId: 終端标識，每個終端(或線程)對應一個，區分并發多用戶。
        :type TerminalId: str
        :param InputText: 請求的文本。
        :type InputText: str
        :param BotEnv: 機器人版本，取值"dev"或"release"，{調試版本：dev；線上版本：release}。
        :type BotEnv: str
        :param SessionAttributes: 透傳欄位，透傳給用戶自定義的WebService服務。
        :type SessionAttributes: str
        """
        self.BotId = None
        self.TerminalId = None
        self.InputText = None
        self.BotEnv = None
        self.SessionAttributes = None


    def _deserialize(self, params):
        self.BotId = params.get("BotId")
        self.TerminalId = params.get("TerminalId")
        self.InputText = params.get("InputText")
        self.BotEnv = params.get("BotEnv")
        self.SessionAttributes = params.get("SessionAttributes")


class TextProcessResponse(AbstractModel):
    """TextProcess返回參數結構體

    """

    def __init__(self):
        """
        :param DialogStatus: 當前會話狀态{會話開始: START; 會話中: COUTINUE; 會話結束: COMPLETE}。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DialogStatus: str
        :param BotName: 比對到的機器人名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type BotName: str
        :param IntentName: 比對到的意圖名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IntentName: str
        :param SlotInfoList: 槽位訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SlotInfoList: list of SlotInfo
        :param InputText: 原始的用戶說法。
注意：此欄位可能返回 null，表示取不到有效值。
        :type InputText: str
        :param SessionAttributes: 透傳欄位，由用戶自定義的WebService服務返回。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SessionAttributes: str
        :param ResponseText: 機器人對話的應答文本。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResponseText: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DialogStatus = None
        self.BotName = None
        self.IntentName = None
        self.SlotInfoList = None
        self.InputText = None
        self.SessionAttributes = None
        self.ResponseText = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DialogStatus = params.get("DialogStatus")
        self.BotName = params.get("BotName")
        self.IntentName = params.get("IntentName")
        if params.get("SlotInfoList") is not None:
            self.SlotInfoList = []
            for item in params.get("SlotInfoList"):
                obj = SlotInfo()
                obj._deserialize(item)
                self.SlotInfoList.append(obj)
        self.InputText = params.get("InputText")
        self.SessionAttributes = params.get("SessionAttributes")
        self.ResponseText = params.get("ResponseText")
        self.RequestId = params.get("RequestId")


class TextResetRequest(AbstractModel):
    """TextReset請求參數結構體

    """

    def __init__(self):
        """
        :param BotId: 機器人标識，用于定義抽象機器人。
        :type BotId: str
        :param TerminalId: 終端标識，每個終端(或線程)對應一個，區分并發多用戶。
        :type TerminalId: str
        :param BotEnv: 機器人版本，取值"dev"或"release"，{調試版本：dev；線上版本：release}。
        :type BotEnv: str
        """
        self.BotId = None
        self.TerminalId = None
        self.BotEnv = None


    def _deserialize(self, params):
        self.BotId = params.get("BotId")
        self.TerminalId = params.get("TerminalId")
        self.BotEnv = params.get("BotEnv")


class TextResetResponse(AbstractModel):
    """TextReset返回參數結構體

    """

    def __init__(self):
        """
        :param DialogStatus: 當前會話狀态，取值："START"/"COUTINUE"/"COMPLETE"。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DialogStatus: str
        :param BotName: 比對到的機器人名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type BotName: str
        :param IntentName: 比對到的意圖名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IntentName: str
        :param SlotInfoList: 槽位訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SlotInfoList: list of SlotInfo
        :param InputText: 原始的用戶說法。
注意：此欄位可能返回 null，表示取不到有效值。
        :type InputText: str
        :param SessionAttributes: 透傳欄位，由用戶自定義的WebService服務返回。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SessionAttributes: str
        :param ResponseText: 機器人對話的應答文本。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResponseText: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DialogStatus = None
        self.BotName = None
        self.IntentName = None
        self.SlotInfoList = None
        self.InputText = None
        self.SessionAttributes = None
        self.ResponseText = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DialogStatus = params.get("DialogStatus")
        self.BotName = params.get("BotName")
        self.IntentName = params.get("IntentName")
        if params.get("SlotInfoList") is not None:
            self.SlotInfoList = []
            for item in params.get("SlotInfoList"):
                obj = SlotInfo()
                obj._deserialize(item)
                self.SlotInfoList.append(obj)
        self.InputText = params.get("InputText")
        self.SessionAttributes = params.get("SessionAttributes")
        self.ResponseText = params.get("ResponseText")
        self.RequestId = params.get("RequestId")