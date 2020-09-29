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


class Group(AbstractModel):
    """Group是訊息組的具體定義，當前包含ContentType、Url、Content三個欄位。其中，具體的ContentType欄位定義，參考網際網路MIME類型標準。

    """

    def __init__(self):
        """
        :param ContentType: 訊息類型參考網際網路MIME類型標準，當前僅支援"text/plain"。
        :type ContentType: str
        :param Url: 返回内容以連結形式提供。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Url: str
        :param Content: 普通文本。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Content: str
        """
        self.ContentType = None
        self.Url = None
        self.Content = None


    def _deserialize(self, params):
        self.ContentType = params.get("ContentType")
        self.Url = params.get("Url")
        self.Content = params.get("Content")


class ResponseMessage(AbstractModel):
    """從TBP-RTS服務v1.3版本起，機器人以訊息組清單的形式響應，訊息組清單GroupList包含多組訊息，用戶根據需要對部分或全部訊息組進行組合使用。

    """

    def __init__(self):
        """
        :param GroupList: 訊息組清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type GroupList: list of Group
        """
        self.GroupList = None


    def _deserialize(self, params):
        if params.get("GroupList") is not None:
            self.GroupList = []
            for item in params.get("GroupList"):
                obj = Group()
                obj._deserialize(item)
                self.GroupList.append(obj)


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
        :param BotId: 機器人標識，用於定義抽象機器人。
        :type BotId: str
        :param BotEnv: 機器人版本，取值"dev"或"release"，{調試版本：dev；線上版本：release}。
        :type BotEnv: str
        :param TerminalId: 終端標識，每個終端(或線程)對應一個，區分並發多用戶。
        :type TerminalId: str
        :param InputText: 請求的文本。
        :type InputText: str
        :param SessionAttributes: 透傳欄位，透傳給用戶自定義的WebService服務。
        :type SessionAttributes: str
        :param PlatformType: 平台類型，{小程式：MiniProgram；小微：XiaoWei；公衆號：OfficialAccount；企業 : WXWork}。
        :type PlatformType: str
        :param PlatformId: 當PlatformType爲 公衆號或企業 時，傳遞對應 公衆號或企業 的唯一標識
        :type PlatformId: str
        """
        self.BotId = None
        self.BotEnv = None
        self.TerminalId = None
        self.InputText = None
        self.SessionAttributes = None
        self.PlatformType = None
        self.PlatformId = None


    def _deserialize(self, params):
        self.BotId = params.get("BotId")
        self.BotEnv = params.get("BotEnv")
        self.TerminalId = params.get("TerminalId")
        self.InputText = params.get("InputText")
        self.SessionAttributes = params.get("SessionAttributes")
        self.PlatformType = params.get("PlatformType")
        self.PlatformId = params.get("PlatformId")


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
        :param ResponseMessage: 機器人應答。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResponseMessage: :class:`taifucloudcloud.tbp.v20190627.models.ResponseMessage`
        :param SessionAttributes: 透傳欄位，由用戶自定義的WebService服務返回。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SessionAttributes: str
        :param ResultType: 結果類型 {中間邏輯出錯:0; 任務型機器人:1; 問答型機器人:2; 閑聊型機器人:3; 未比對上，返回預設兜底話術:5; 未比對上，返回相似問題清單:6}。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResultType: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DialogStatus = None
        self.BotName = None
        self.IntentName = None
        self.SlotInfoList = None
        self.InputText = None
        self.ResponseMessage = None
        self.SessionAttributes = None
        self.ResultType = None
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
        if params.get("ResponseMessage") is not None:
            self.ResponseMessage = ResponseMessage()
            self.ResponseMessage._deserialize(params.get("ResponseMessage"))
        self.SessionAttributes = params.get("SessionAttributes")
        self.ResultType = params.get("ResultType")
        self.RequestId = params.get("RequestId")


class TextResetRequest(AbstractModel):
    """TextReset請求參數結構體

    """

    def __init__(self):
        """
        :param BotId: 機器人標識，用於定義抽象機器人。
        :type BotId: str
        :param BotEnv: 機器人版本，取值"dev"或"release"，{調試版本：dev；線上版本：release}。
        :type BotEnv: str
        :param TerminalId: 終端標識，每個終端(或線程)對應一個，區分並發多用戶。
        :type TerminalId: str
        :param PlatformType: 平台類型，{小程式：MiniProgram；小微：XiaoWei；公衆號：OfficialAccount；企業 : WXWork}。
        :type PlatformType: str
        :param PlatformId: 當PlatformType爲 公衆號或企業 時，傳遞對應 公衆號或企業 的唯一標識
        :type PlatformId: str
        """
        self.BotId = None
        self.BotEnv = None
        self.TerminalId = None
        self.PlatformType = None
        self.PlatformId = None


    def _deserialize(self, params):
        self.BotId = params.get("BotId")
        self.BotEnv = params.get("BotEnv")
        self.TerminalId = params.get("TerminalId")
        self.PlatformType = params.get("PlatformType")
        self.PlatformId = params.get("PlatformId")


class TextResetResponse(AbstractModel):
    """TextReset返回參數結構體

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
        :param ResponseMessage: 機器人應答。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResponseMessage: :class:`taifucloudcloud.tbp.v20190627.models.ResponseMessage`
        :param SessionAttributes: 透傳欄位，由用戶自定義的WebService服務返回。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SessionAttributes: str
        :param ResultType: 結果類型 {中間邏輯出錯:0; 任務型機器人:1; 問答型機器人:2; 閑聊型機器人:3; 未比對上，返回預設兜底話術:5; 未比對上，返回相似問題清單:6}。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResultType: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DialogStatus = None
        self.BotName = None
        self.IntentName = None
        self.SlotInfoList = None
        self.InputText = None
        self.ResponseMessage = None
        self.SessionAttributes = None
        self.ResultType = None
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
        if params.get("ResponseMessage") is not None:
            self.ResponseMessage = ResponseMessage()
            self.ResponseMessage._deserialize(params.get("ResponseMessage"))
        self.SessionAttributes = params.get("SessionAttributes")
        self.ResultType = params.get("ResultType")
        self.RequestId = params.get("RequestId")