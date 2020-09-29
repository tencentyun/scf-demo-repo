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


class AppStatisticsItem(AbstractModel):
    """應用用量統計數據

    """

    def __init__(self):
        """
        :param RealtimeSpeechStatisticsItem: 實時語音統計數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type RealtimeSpeechStatisticsItem: :class:`taifucloudcloud.gme.v20180711.models.RealTimeSpeechStatisticsItem`
        :param VoiceMessageStatisticsItem: 語音訊息統計數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type VoiceMessageStatisticsItem: :class:`taifucloudcloud.gme.v20180711.models.VoiceMessageStatisticsItem`
        :param VoiceFilterStatisticsItem: 語音過濾統計數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type VoiceFilterStatisticsItem: :class:`taifucloudcloud.gme.v20180711.models.VoiceFilterStatisticsItem`
        :param Date: 統計時間
        :type Date: str
        """
        self.RealtimeSpeechStatisticsItem = None
        self.VoiceMessageStatisticsItem = None
        self.VoiceFilterStatisticsItem = None
        self.Date = None


    def _deserialize(self, params):
        if params.get("RealtimeSpeechStatisticsItem") is not None:
            self.RealtimeSpeechStatisticsItem = RealTimeSpeechStatisticsItem()
            self.RealtimeSpeechStatisticsItem._deserialize(params.get("RealtimeSpeechStatisticsItem"))
        if params.get("VoiceMessageStatisticsItem") is not None:
            self.VoiceMessageStatisticsItem = VoiceMessageStatisticsItem()
            self.VoiceMessageStatisticsItem._deserialize(params.get("VoiceMessageStatisticsItem"))
        if params.get("VoiceFilterStatisticsItem") is not None:
            self.VoiceFilterStatisticsItem = VoiceFilterStatisticsItem()
            self.VoiceFilterStatisticsItem._deserialize(params.get("VoiceFilterStatisticsItem"))
        self.Date = params.get("Date")


class CreateAppRequest(AbstractModel):
    """CreateApp請求參數結構體

    """

    def __init__(self):
        """
        :param AppName: 應用名稱
        :type AppName: str
        :param ProjectId: Top Cloud 項目ID，預設爲0，表示預設項目
        :type ProjectId: int
        :param EngineList: 需要支援的引擎清單，預設全選。
        :type EngineList: list of str
        :param RegionList: 服務區域清單，預設全選。
        :type RegionList: list of str
        :param RealtimeSpeechConf: 實時語音服務配置數據
        :type RealtimeSpeechConf: :class:`taifucloudcloud.gme.v20180711.models.RealtimeSpeechConf`
        :param VoiceMessageConf: 語音訊息及轉文本服務配置數據
        :type VoiceMessageConf: :class:`taifucloudcloud.gme.v20180711.models.VoiceMessageConf`
        :param VoiceFilterConf: 語音分析服務配置數據
        :type VoiceFilterConf: :class:`taifucloudcloud.gme.v20180711.models.VoiceFilterConf`
        :param Tags: 需要添加的標簽清單
        :type Tags: list of Tag
        """
        self.AppName = None
        self.ProjectId = None
        self.EngineList = None
        self.RegionList = None
        self.RealtimeSpeechConf = None
        self.VoiceMessageConf = None
        self.VoiceFilterConf = None
        self.Tags = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.ProjectId = params.get("ProjectId")
        self.EngineList = params.get("EngineList")
        self.RegionList = params.get("RegionList")
        if params.get("RealtimeSpeechConf") is not None:
            self.RealtimeSpeechConf = RealtimeSpeechConf()
            self.RealtimeSpeechConf._deserialize(params.get("RealtimeSpeechConf"))
        if params.get("VoiceMessageConf") is not None:
            self.VoiceMessageConf = VoiceMessageConf()
            self.VoiceMessageConf._deserialize(params.get("VoiceMessageConf"))
        if params.get("VoiceFilterConf") is not None:
            self.VoiceFilterConf = VoiceFilterConf()
            self.VoiceFilterConf._deserialize(params.get("VoiceFilterConf"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class CreateAppResponse(AbstractModel):
    """CreateApp的輸出參數

    """

    def __init__(self):
        """
        :param BizId: 應用ID，由後台自動生成。
        :type BizId: int
        :param AppName: 應用名稱，透傳輸入參數的AppName
        :type AppName: str
        :param ProjectId: 項目ID，透傳輸入的ProjectId
        :type ProjectId: int
        :param SecretKey: 應用金鑰，GME SDK初始化時使用
        :type SecretKey: str
        :param CreateTime: 服務創建時間戳
        :type CreateTime: int
        :param RealtimeSpeechConf: 實時語音服務配置數據
        :type RealtimeSpeechConf: :class:`taifucloudcloud.gme.v20180711.models.RealtimeSpeechConf`
        :param VoiceMessageConf: 語音訊息及轉文本服務配置數據
        :type VoiceMessageConf: :class:`taifucloudcloud.gme.v20180711.models.VoiceMessageConf`
        :param VoiceFilterConf: 語音分析服務配置數據
        :type VoiceFilterConf: :class:`taifucloudcloud.gme.v20180711.models.VoiceFilterConf`
        """
        self.BizId = None
        self.AppName = None
        self.ProjectId = None
        self.SecretKey = None
        self.CreateTime = None
        self.RealtimeSpeechConf = None
        self.VoiceMessageConf = None
        self.VoiceFilterConf = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.AppName = params.get("AppName")
        self.ProjectId = params.get("ProjectId")
        self.SecretKey = params.get("SecretKey")
        self.CreateTime = params.get("CreateTime")
        if params.get("RealtimeSpeechConf") is not None:
            self.RealtimeSpeechConf = RealtimeSpeechConf()
            self.RealtimeSpeechConf._deserialize(params.get("RealtimeSpeechConf"))
        if params.get("VoiceMessageConf") is not None:
            self.VoiceMessageConf = VoiceMessageConf()
            self.VoiceMessageConf._deserialize(params.get("VoiceMessageConf"))
        if params.get("VoiceFilterConf") is not None:
            self.VoiceFilterConf = VoiceFilterConf()
            self.VoiceFilterConf._deserialize(params.get("VoiceFilterConf"))


class DescribeAppStatisticsRequest(AbstractModel):
    """DescribeAppStatistics請求參數結構體

    """

    def __init__(self):
        """
        :param BizId: GME應用ID
        :type BizId: int
        :param StartDate: 數據開始時間，東八區時間，格式: 年-月-日，如: 2018-07-13
        :type StartDate: str
        :param EndDate: 數據結束時間，東八區時間，格式: 年-月-日，如: 2018-07-13
        :type EndDate: str
        :param Services: 要查詢的服務清單，取值：RealTimeSpeech/VoiceMessage/VoiceFilter
        :type Services: list of str
        """
        self.BizId = None
        self.StartDate = None
        self.EndDate = None
        self.Services = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Services = params.get("Services")


class DescribeAppStatisticsResponse(AbstractModel):
    """獲取應用用量統計數據輸出參數

    """

    def __init__(self):
        """
        :param AppStatistics: 應用用量統計數據
        :type AppStatistics: list of AppStatisticsItem
        """
        self.AppStatistics = None


    def _deserialize(self, params):
        if params.get("AppStatistics") is not None:
            self.AppStatistics = []
            for item in params.get("AppStatistics"):
                obj = AppStatisticsItem()
                obj._deserialize(item)
                self.AppStatistics.append(obj)


class DescribeFilterResultListRequest(AbstractModel):
    """DescribeFilterResultList請求參數結構體

    """

    def __init__(self):
        """
        :param BizId: 應用ID
        :type BizId: int
        :param StartDate: 開始時間，格式爲 年-月-日，如: 2018-07-11
        :type StartDate: str
        :param EndDate: 結束時間，格式爲 年-月-日，如: 2018-07-11
        :type EndDate: str
        :param Offset: 偏移量，預設值爲0。
        :type Offset: int
        :param Limit: 返回數量，預設值爲10，最大值爲100。
        :type Limit: int
        """
        self.BizId = None
        self.StartDate = None
        self.EndDate = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeFilterResultListResponse(AbstractModel):
    """DescribeFilterResultList返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 過濾結果總數
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Data: 當前分頁過濾結果清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: list of VoiceFilterInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = VoiceFilterInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFilterResultRequest(AbstractModel):
    """DescribeFilterResult請求參數結構體

    """

    def __init__(self):
        """
        :param BizId: 應用ID
        :type BizId: int
        :param FileId: 文件ID
        :type FileId: str
        """
        self.BizId = None
        self.FileId = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.FileId = params.get("FileId")


class DescribeFilterResultResponse(AbstractModel):
    """DescribeFilterResult返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 過濾結果
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: :class:`taifucloudcloud.gme.v20180711.models.VoiceFilterInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = VoiceFilterInfo()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeScanResult(AbstractModel):
    """語音檢測結果返回

    """

    def __init__(self):
        """
        :param Code: 業務返回碼
        :type Code: int
        :param DataId: 數據唯一 ID
        :type DataId: str
        :param ScanFinishTime: 檢測完成的時間戳
        :type ScanFinishTime: int
        :param HitFlag: 是否違規
        :type HitFlag: bool
        :param Live: 是否爲流
        :type Live: bool
        :param Msg: 業務返回描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type Msg: str
        :param ScanPiece: 檢測結果，Code 爲 0 時返回
注意：此欄位可能返回 null，表示取不到有效值。
        :type ScanPiece: list of ScanPiece
        :param ScanStartTime: 提交檢測的時間戳
        :type ScanStartTime: int
        :param Scenes: 語音檢測場景，對應請求時的 Scene
        :type Scenes: list of str
        :param TaskId: 語音檢測任務 ID，由後台分配
        :type TaskId: str
        :param Url: 文件或接流網址
        :type Url: str
        :param Status: 檢測任務執行結果狀态，分别爲：
<li>Start: 任務開始</li>
<li>Success: 成功結束</li>
<li>Error: 異常</li>
        :type Status: str
        """
        self.Code = None
        self.DataId = None
        self.ScanFinishTime = None
        self.HitFlag = None
        self.Live = None
        self.Msg = None
        self.ScanPiece = None
        self.ScanStartTime = None
        self.Scenes = None
        self.TaskId = None
        self.Url = None
        self.Status = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.DataId = params.get("DataId")
        self.ScanFinishTime = params.get("ScanFinishTime")
        self.HitFlag = params.get("HitFlag")
        self.Live = params.get("Live")
        self.Msg = params.get("Msg")
        if params.get("ScanPiece") is not None:
            self.ScanPiece = []
            for item in params.get("ScanPiece"):
                obj = ScanPiece()
                obj._deserialize(item)
                self.ScanPiece.append(obj)
        self.ScanStartTime = params.get("ScanStartTime")
        self.Scenes = params.get("Scenes")
        self.TaskId = params.get("TaskId")
        self.Url = params.get("Url")
        self.Status = params.get("Status")


class DescribeScanResultListRequest(AbstractModel):
    """DescribeScanResultList請求參數結構體

    """

    def __init__(self):
        """
        :param BizId: 應用 ID，登入[控制台](https://console.cloud.taifucloud.com/gamegme)創建應用得到的AppID
        :type BizId: int
        :param TaskIdList: 查詢的任務 ID 清單，任務 ID 清單最多支援 100 個。
        :type TaskIdList: list of str
        :param Limit: 任務返回結果數量，預設10，上限500。大文件任務忽略此參數，返回全量結果
        :type Limit: int
        """
        self.BizId = None
        self.TaskIdList = None
        self.Limit = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.TaskIdList = params.get("TaskIdList")
        self.Limit = params.get("Limit")


class DescribeScanResultListResponse(AbstractModel):
    """DescribeScanResultList返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 要查詢的語音檢測任務的結果
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: list of DescribeScanResult
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DescribeScanResult()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyAppStatusRequest(AbstractModel):
    """ModifyAppStatus請求參數結構體

    """

    def __init__(self):
        """
        :param BizId: 應用ID，創建應用後由後台生成並返回。
        :type BizId: int
        :param Status: 應用狀态，取值：open/close
        :type Status: str
        """
        self.BizId = None
        self.Status = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.Status = params.get("Status")


class ModifyAppStatusResponse(AbstractModel):
    """ModifyAppStatus介面輸出參數

    """

    def __init__(self):
        """
        :param BizId: GME應用ID
        :type BizId: int
        :param Status: 應用狀态，取值：open/close
        :type Status: str
        """
        self.BizId = None
        self.Status = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.Status = params.get("Status")


class RealTimeSpeechStatisticsItem(AbstractModel):
    """實時語音用量統計數據

    """

    def __init__(self):
        """
        :param MainLandDau: 大陸地區DAU
        :type MainLandDau: int
        :param MainLandPcu: 大陸地區PCU
        :type MainLandPcu: int
        :param MainLandDuration: 大陸地區總使用時長，單位爲min
        :type MainLandDuration: int
        :param OverseaDau: 海外地區DAU
        :type OverseaDau: int
        :param OverseaPcu: 海外地區PCU
        :type OverseaPcu: int
        :param OverseaDuration: 海外地區總使用時長，單位爲min
        :type OverseaDuration: int
        """
        self.MainLandDau = None
        self.MainLandPcu = None
        self.MainLandDuration = None
        self.OverseaDau = None
        self.OverseaPcu = None
        self.OverseaDuration = None


    def _deserialize(self, params):
        self.MainLandDau = params.get("MainLandDau")
        self.MainLandPcu = params.get("MainLandPcu")
        self.MainLandDuration = params.get("MainLandDuration")
        self.OverseaDau = params.get("OverseaDau")
        self.OverseaPcu = params.get("OverseaPcu")
        self.OverseaDuration = params.get("OverseaDuration")


class RealtimeSpeechConf(AbstractModel):
    """實時語音配置數據

    """

    def __init__(self):
        """
        :param Status: 實時語音服務開關，取值：open/close
        :type Status: str
        :param Quality: 實時語音音質類型，取值：high-高音質，ordinary-普通音質。預設高音質。普通音質僅白名單開放，如需要普通音質，請聯系Top Cloud 商務。
        :type Quality: str
        """
        self.Status = None
        self.Quality = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Quality = params.get("Quality")


class ScanDetail(AbstractModel):
    """語音檢測詳情

    """

    def __init__(self):
        """
        :param Label: 違規場景，參照<a href="https://cloud.taifucloud.com/document/product/607/37622#Label_Value">Label</a>定義
        :type Label: str
        :param Rate: 該場景下概率[0.00,100.00],分值越大違規概率越高
        :type Rate: str
        :param KeyWord: 違規關鍵字
        :type KeyWord: str
        :param StartTime: 關鍵字在音訊的開始時間，從0開始的偏移量，單位爲毫秒
        :type StartTime: int
        :param EndTime: 關鍵字在音訊的結束時間，從0開始的偏移量,，單位爲毫秒
        :type EndTime: int
        """
        self.Label = None
        self.Rate = None
        self.KeyWord = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Rate = params.get("Rate")
        self.KeyWord = params.get("KeyWord")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class ScanPiece(AbstractModel):
    """語音檢測結果，Code 爲 0 時返回

    """

    def __init__(self):
        """
        :param DumpUrl: 流檢測時返回，音訊轉存網址，保留30min
注意：此欄位可能返回 null，表示取不到有效值。
        :type DumpUrl: str
        :param HitFlag: 是否違規
        :type HitFlag: bool
        :param MainType: 違規主要類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type MainType: str
        :param ScanDetail: 語音檢測詳情
        :type ScanDetail: list of ScanDetail
        :param RoomId: gme實時語音房間ID，透傳任務傳入時的RoomId
注意：此欄位可能返回 null，表示取不到有效值。
        :type RoomId: str
        :param OpenId: gme實時語音用戶ID，透傳任務傳入時的OpenId
注意：此欄位可能返回 null，表示取不到有效值。
        :type OpenId: str
        :param Info: 備注
注意：此欄位可能返回 null，表示取不到有效值。
        :type Info: str
        :param Offset: 流檢測時分片在流中的偏移時間，單位毫秒
注意：此欄位可能返回 null，表示取不到有效值。
        :type Offset: int
        :param Duration: 流檢測時分片時長
注意：此欄位可能返回 null，表示取不到有效值。
        :type Duration: int
        :param PieceStartTime: 分片開始檢測時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type PieceStartTime: int
        """
        self.DumpUrl = None
        self.HitFlag = None
        self.MainType = None
        self.ScanDetail = None
        self.RoomId = None
        self.OpenId = None
        self.Info = None
        self.Offset = None
        self.Duration = None
        self.PieceStartTime = None


    def _deserialize(self, params):
        self.DumpUrl = params.get("DumpUrl")
        self.HitFlag = params.get("HitFlag")
        self.MainType = params.get("MainType")
        if params.get("ScanDetail") is not None:
            self.ScanDetail = []
            for item in params.get("ScanDetail"):
                obj = ScanDetail()
                obj._deserialize(item)
                self.ScanDetail.append(obj)
        self.RoomId = params.get("RoomId")
        self.OpenId = params.get("OpenId")
        self.Info = params.get("Info")
        self.Offset = params.get("Offset")
        self.Duration = params.get("Duration")
        self.PieceStartTime = params.get("PieceStartTime")


class ScanVoiceRequest(AbstractModel):
    """ScanVoice請求參數結構體

    """

    def __init__(self):
        """
        :param BizId: 應用ID，登入[控制台 - 服務管理](https://console.cloud.taifucloud.com/gamegme)創建應用得到的AppID
        :type BizId: int
        :param Scenes: 語音檢測場景，參數值目前要求爲 default。 預留場景設置： 謾罵、色情、涉政、廣告、暴恐、違禁等場景，<a href="#Label_Value">具體取值見上述 Label 說明。</a>
        :type Scenes: list of str
        :param Live: 是否爲直播流。值爲 false 時表示普通語音文件檢測；爲 true 時表示語音流檢測。
        :type Live: bool
        :param Tasks: 語音檢測任務清單，清單最多支援100個檢測任務。結構體中包含：
<li>DataId：數據的唯一ID</li>
<li>Url：數據文件的url，爲 urlencode 編碼，流式則爲拉流網址</li>
        :type Tasks: list of Task
        :param Callback: 異步檢測結果回調網址，具體見上述<a href="#Callback_Declare">回調相關說明</a>。（說明：該欄位爲空時，必須通過介面(查詢語音檢測結果)獲取檢測結果）。
        :type Callback: str
        """
        self.BizId = None
        self.Scenes = None
        self.Live = None
        self.Tasks = None
        self.Callback = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.Scenes = params.get("Scenes")
        self.Live = params.get("Live")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.Callback = params.get("Callback")


class ScanVoiceResponse(AbstractModel):
    """ScanVoice返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 語音檢測返回。Data 欄位是 JSON 數組，每一個元素包含：<li>DataId： 請求中對應的 DataId。</li>
<li>TaskID ：該檢測任務的 ID，用於輪詢語音檢測結果。</li>
        :type Data: list of ScanVoiceResult
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ScanVoiceResult()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class ScanVoiceResult(AbstractModel):
    """語音檢測返回結果

    """

    def __init__(self):
        """
        :param DataId: 數據ID
        :type DataId: str
        :param TaskId: 任務ID
        :type TaskId: str
        """
        self.DataId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.DataId = params.get("DataId")
        self.TaskId = params.get("TaskId")


class Tag(AbstractModel):
    """標簽清單

    """

    def __init__(self):
        """
        :param TagKey: 標簽鍵
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param TagValue: 標簽值
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class Task(AbstractModel):
    """語音檢測任務清單

    """

    def __init__(self):
        """
        :param DataId: 數據的唯一ID
        :type DataId: str
        :param Url: 數據文件的url，爲 urlencode 編碼，流式則爲拉流網址
        :type Url: str
        :param RoomId: gme實時語音房間ID，通過gme實時語音進行語音分析時輸入
        :type RoomId: str
        :param OpenId: gme實時語音用戶ID，通過gme實時語音進行語音分析時輸入
        :type OpenId: str
        """
        self.DataId = None
        self.Url = None
        self.RoomId = None
        self.OpenId = None


    def _deserialize(self, params):
        self.DataId = params.get("DataId")
        self.Url = params.get("Url")
        self.RoomId = params.get("RoomId")
        self.OpenId = params.get("OpenId")


class VoiceFilter(AbstractModel):
    """過濾結果

    """

    def __init__(self):
        """
        :param Type: 過濾類型，1：政治，2：色情，3：涉毒，4：謾罵
注意：此欄位可能返回 null，表示取不到有效值。
        :type Type: int
        :param Word: 過濾命中關鍵詞
注意：此欄位可能返回 null，表示取不到有效值。
        :type Word: str
        """
        self.Type = None
        self.Word = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Word = params.get("Word")


class VoiceFilterConf(AbstractModel):
    """語音過濾服務配置數據

    """

    def __init__(self):
        """
        :param Status: 語音過濾服務開關，取值：open/close
        :type Status: str
        """
        self.Status = None


    def _deserialize(self, params):
        self.Status = params.get("Status")


class VoiceFilterInfo(AbstractModel):
    """語音文件過濾詳情

    """

    def __init__(self):
        """
        :param BizId: 應用ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type BizId: int
        :param FileId: 文件ID，表示文件唯一ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileId: str
        :param FileName: 文件名
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileName: str
        :param OpenId: 用戶ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type OpenId: str
        :param Timestamp: 數據創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type Timestamp: str
        :param Data: 過濾結果清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: list of VoiceFilter
        """
        self.BizId = None
        self.FileId = None
        self.FileName = None
        self.OpenId = None
        self.Timestamp = None
        self.Data = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.FileId = params.get("FileId")
        self.FileName = params.get("FileName")
        self.OpenId = params.get("OpenId")
        self.Timestamp = params.get("Timestamp")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = VoiceFilter()
                obj._deserialize(item)
                self.Data.append(obj)


class VoiceFilterRequest(AbstractModel):
    """VoiceFilter請求參數結構體

    """

    def __init__(self):
        """
        :param BizId: 應用ID，登入[控制台](https://console.cloud.taifucloud.com/gamegme)創建應用得到的AppID
        :type BizId: int
        :param FileId: 文件ID，表示文件唯一ID
        :type FileId: str
        :param FileName: 文件名
        :type FileName: str
        :param FileUrl: 文件url，urlencode編碼，FileUrl和FileContent二選一
        :type FileUrl: str
        :param FileContent: 文件内容，base64編碼，FileUrl和FileContent二選一
        :type FileContent: str
        :param OpenId: 用戶ID
        :type OpenId: str
        """
        self.BizId = None
        self.FileId = None
        self.FileName = None
        self.FileUrl = None
        self.FileContent = None
        self.OpenId = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.FileId = params.get("FileId")
        self.FileName = params.get("FileName")
        self.FileUrl = params.get("FileUrl")
        self.FileContent = params.get("FileContent")
        self.OpenId = params.get("OpenId")


class VoiceFilterResponse(AbstractModel):
    """VoiceFilter返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class VoiceFilterStatisticsItem(AbstractModel):
    """語音過濾用量統計數據

    """

    def __init__(self):
        """
        :param Duration: 語音過濾總時長
        :type Duration: int
        """
        self.Duration = None


    def _deserialize(self, params):
        self.Duration = params.get("Duration")


class VoiceMessageConf(AbstractModel):
    """離線語音服務配置數據

    """

    def __init__(self):
        """
        :param Status: 離線語音服務開關，取值：open/close
        :type Status: str
        :param Language: 離線語音支援語種，取值： all-全部，cnen-中英文。預設爲中英文
        :type Language: str
        """
        self.Status = None
        self.Language = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Language = params.get("Language")


class VoiceMessageStatisticsItem(AbstractModel):
    """語音訊息用量統計訊息

    """

    def __init__(self):
        """
        :param Dau: 離線語音DAU
        :type Dau: int
        """
        self.Dau = None


    def _deserialize(self, params):
        self.Dau = params.get("Dau")