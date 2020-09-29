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


class Canvas(AbstractModel):
    """混流畫布參數

    """

    def __init__(self):
        """
        :param LayoutParams: 混流畫布寬高配置
        :type LayoutParams: :class:`taifucloudcloud.tiw.v20190919.models.LayoutParams`
        :param BackgroundColor: 背景顔色，預設爲黑色，格式爲RGB格式，如紅色爲"#FF0000"
        :type BackgroundColor: str
        """
        self.LayoutParams = None
        self.BackgroundColor = None


    def _deserialize(self, params):
        if params.get("LayoutParams") is not None:
            self.LayoutParams = LayoutParams()
            self.LayoutParams._deserialize(params.get("LayoutParams"))
        self.BackgroundColor = params.get("BackgroundColor")


class Concat(AbstractModel):
    """實時錄制視訊拼接參數

    """

    def __init__(self):
        """
        :param Enabled: 是否開啓拼接功能
在開啓了視訊拼接功能的情況下，實時錄制服務會把同一個用戶因爲暫停導緻的多段視訊拼接成一個視訊
        :type Enabled: bool
        :param Image: 視訊拼接時使用的墊片圖片下載網址，不填預設用全黑的圖片進行視訊墊片
        :type Image: str
        """
        self.Enabled = None
        self.Image = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.Image = params.get("Image")


class CreateTranscodeRequest(AbstractModel):
    """CreateTranscode請求參數結構體

    """

    def __init__(self):
        """
        :param SdkAppId: 客戶的SdkAppId
        :type SdkAppId: int
        :param Url: 需要進行轉碼文件網址
        :type Url: str
        :param IsStaticPPT: 是否爲靜态PPT，預設爲False；
如果IsStaticPPT爲False，後綴名爲.ppt或.pptx的文件會動态轉碼成HTML5頁面，其他格式的文件會靜态轉碼成圖片；如果IsStaticPPT爲True，所有格式的文件會靜态轉碼成圖片；
        :type IsStaticPPT: bool
        :param MinResolution: 轉碼後文件的最小分辨率，不傳、傳空字串或分辨率格式錯誤則使用文件原分辨率

注意分辨率寬高中間爲英文字母"xyz"的"x"
        :type MinResolution: str
        :param ThumbnailResolution: 動态PPT轉碼可以爲文件生成該分辨率的縮略圖，不傳、傳空字串或分辨率格式錯誤則不生成縮略圖，分辨率格式同MinResolution

靜态轉碼這個參數不起作用
        :type ThumbnailResolution: str
        :param CompressFileType: 轉碼文件壓縮格式，不傳、傳空字串或不是指定的格式則不生成壓縮文件，目前支援如下壓縮格式：

zip： 生成`.zip`壓縮包
tar.gz： 生成`.tar.gz`壓縮包
        :type CompressFileType: str
        """
        self.SdkAppId = None
        self.Url = None
        self.IsStaticPPT = None
        self.MinResolution = None
        self.ThumbnailResolution = None
        self.CompressFileType = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Url = params.get("Url")
        self.IsStaticPPT = params.get("IsStaticPPT")
        self.MinResolution = params.get("MinResolution")
        self.ThumbnailResolution = params.get("ThumbnailResolution")
        self.CompressFileType = params.get("CompressFileType")


class CreateTranscodeResponse(AbstractModel):
    """CreateTranscode返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 文件轉碼任務的唯一標識Id，用於查詢該任務的進度以及轉碼結果
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CustomLayout(AbstractModel):
    """自定義混流布局參數

    """

    def __init__(self):
        """
        :param Canvas: 混流畫布參數
        :type Canvas: :class:`taifucloudcloud.tiw.v20190919.models.Canvas`
        :param InputStreamList: 流布局參數，每路流的布局不能超出畫布區域
        :type InputStreamList: list of StreamLayout
        """
        self.Canvas = None
        self.InputStreamList = None


    def _deserialize(self, params):
        if params.get("Canvas") is not None:
            self.Canvas = Canvas()
            self.Canvas._deserialize(params.get("Canvas"))
        if params.get("InputStreamList") is not None:
            self.InputStreamList = []
            for item in params.get("InputStreamList"):
                obj = StreamLayout()
                obj._deserialize(item)
                self.InputStreamList.append(obj)


class DescribeOnlineRecordCallbackRequest(AbstractModel):
    """DescribeOnlineRecordCallback請求參數結構體

    """

    def __init__(self):
        """
        :param SdkAppId: 應用的SdkAppId
        :type SdkAppId: int
        """
        self.SdkAppId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")


class DescribeOnlineRecordCallbackResponse(AbstractModel):
    """DescribeOnlineRecordCallback返回參數結構體

    """

    def __init__(self):
        """
        :param Callback: 實時錄制事件回調網址，如果未設置回調網址，該欄位爲空字串
        :type Callback: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Callback = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Callback = params.get("Callback")
        self.RequestId = params.get("RequestId")


class DescribeOnlineRecordRequest(AbstractModel):
    """DescribeOnlineRecord請求參數結構體

    """

    def __init__(self):
        """
        :param SdkAppId: 客戶的SdkAppId
        :type SdkAppId: int
        :param TaskId: 實時錄制任務Id
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")


class DescribeOnlineRecordResponse(AbstractModel):
    """DescribeOnlineRecord返回參數結構體

    """

    def __init__(self):
        """
        :param FinishReason: 錄制結束原因，
- AUTO: 房間内長時間沒有影音上行及白板操作導緻自動停止錄制
- USER_CALL: 主動調用了停止錄制介面
- EXCEPTION: 錄制異常結束
        :type FinishReason: str
        :param TaskId: 需要查詢結果的錄制任務Id
        :type TaskId: str
        :param Status: 錄制任務狀态
- PREPARED: 表示錄制正在準備中（進房/啓動錄制服務等操作）
- RECORDING: 表示錄制已開始
- PAUSED: 表示錄制已暫停
- STOPPED: 表示錄制已停止，正在處理並上傳視訊
- FINISHED: 表示視訊處理並上傳完成，成功生成錄制結果
        :type Status: str
        :param RoomId: 房間號
        :type RoomId: int
        :param GroupId: 白板的群組 Id
        :type GroupId: str
        :param RecordUserId: 錄制用戶Id
        :type RecordUserId: str
        :param RecordStartTime: 實際開始錄制時間，Unix 時間戳，單位秒
        :type RecordStartTime: int
        :param RecordStopTime: 實際停止錄制時間，Unix 時間戳，單位秒
        :type RecordStopTime: int
        :param TotalTime: 回放視訊總時長（單位：毫秒）
        :type TotalTime: int
        :param ExceptionCnt: 錄制過程中出現異常的次數
        :type ExceptionCnt: int
        :param OmittedDurations: 拼接視訊中被忽略的時間段，只有開啓視訊拼接功能的時候，這個參數才是有效的
        :type OmittedDurations: list of OmittedDuration
        :param VideoInfos: 錄制視訊清單
        :type VideoInfos: list of VideoInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FinishReason = None
        self.TaskId = None
        self.Status = None
        self.RoomId = None
        self.GroupId = None
        self.RecordUserId = None
        self.RecordStartTime = None
        self.RecordStopTime = None
        self.TotalTime = None
        self.ExceptionCnt = None
        self.OmittedDurations = None
        self.VideoInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FinishReason = params.get("FinishReason")
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.RoomId = params.get("RoomId")
        self.GroupId = params.get("GroupId")
        self.RecordUserId = params.get("RecordUserId")
        self.RecordStartTime = params.get("RecordStartTime")
        self.RecordStopTime = params.get("RecordStopTime")
        self.TotalTime = params.get("TotalTime")
        self.ExceptionCnt = params.get("ExceptionCnt")
        if params.get("OmittedDurations") is not None:
            self.OmittedDurations = []
            for item in params.get("OmittedDurations"):
                obj = OmittedDuration()
                obj._deserialize(item)
                self.OmittedDurations.append(obj)
        if params.get("VideoInfos") is not None:
            self.VideoInfos = []
            for item in params.get("VideoInfos"):
                obj = VideoInfo()
                obj._deserialize(item)
                self.VideoInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTranscodeCallbackRequest(AbstractModel):
    """DescribeTranscodeCallback請求參數結構體

    """

    def __init__(self):
        """
        :param SdkAppId: 應用的SdkAppId
        :type SdkAppId: int
        """
        self.SdkAppId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")


class DescribeTranscodeCallbackResponse(AbstractModel):
    """DescribeTranscodeCallback返回參數結構體

    """

    def __init__(self):
        """
        :param Callback: 文件轉碼回調網址
        :type Callback: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Callback = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Callback = params.get("Callback")
        self.RequestId = params.get("RequestId")


class DescribeTranscodeRequest(AbstractModel):
    """DescribeTranscode請求參數結構體

    """

    def __init__(self):
        """
        :param SdkAppId: 客戶的SdkAppId
        :type SdkAppId: int
        :param TaskId: 文件轉碼任務的唯一標識Id
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")


class DescribeTranscodeResponse(AbstractModel):
    """DescribeTranscode返回參數結構體

    """

    def __init__(self):
        """
        :param Pages: 文件的總頁數
        :type Pages: int
        :param Progress: 轉碼的當前進度,取值範圍爲0~100
        :type Progress: int
        :param Resolution: 文件的分辨率
        :type Resolution: str
        :param ResultUrl: 轉碼完成後結果的URL
動态轉碼：PPT轉動态H5的連結
靜态轉碼：文件每一頁的圖片URL前綴，比如，該URL前綴爲`http://example.com/g0jb42ps49vtebjshilb/`，那麽文件第1頁的圖片URL爲
`http://example.com/g0jb42ps49vtebjshilb/1.jpg`，其它頁以此類推
        :type ResultUrl: str
        :param Status: 任務的當前狀态
- QUEUED: 正在排隊等待轉換
- PROCESSING: 轉換中
- FINISHED: 轉換完成
        :type Status: str
        :param TaskId: 轉碼任務的唯一標識Id
        :type TaskId: str
        :param Title: 文件的文件名
        :type Title: str
        :param ThumbnailUrl: 縮略圖URL前綴，比如，該URL前綴爲`http://example.com/g0jb42ps49vtebjshilb/ `，那麽動态PPT第1頁的縮略圖URL爲
`http://example.com/g0jb42ps49vtebjshilb/1.jpg`，其它頁以此類推

如果發起文件轉碼請求參數中帶了ThumbnailResolution參數，並且轉碼類型爲動态轉碼，該參數不爲空，其餘情況該參數爲空字串
        :type ThumbnailUrl: str
        :param ThumbnailResolution: 動态轉碼縮略圖生成分辨率
        :type ThumbnailResolution: str
        :param CompressFileUrl: 轉碼壓縮文件下載的URL，如果發起文件轉碼請求參數中`CompressFileType`爲空或者不是支援的壓縮格式，該參數爲空字串
        :type CompressFileUrl: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Pages = None
        self.Progress = None
        self.Resolution = None
        self.ResultUrl = None
        self.Status = None
        self.TaskId = None
        self.Title = None
        self.ThumbnailUrl = None
        self.ThumbnailResolution = None
        self.CompressFileUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Pages = params.get("Pages")
        self.Progress = params.get("Progress")
        self.Resolution = params.get("Resolution")
        self.ResultUrl = params.get("ResultUrl")
        self.Status = params.get("Status")
        self.TaskId = params.get("TaskId")
        self.Title = params.get("Title")
        self.ThumbnailUrl = params.get("ThumbnailUrl")
        self.ThumbnailResolution = params.get("ThumbnailResolution")
        self.CompressFileUrl = params.get("CompressFileUrl")
        self.RequestId = params.get("RequestId")


class LayoutParams(AbstractModel):
    """自定義混流配置布局參數

    """

    def __init__(self):
        """
        :param Width: 流畫面寬，取值範圍[2,3000]
        :type Width: int
        :param Height: 流畫面高，取值範圍[2,3000]
        :type Height: int
        :param X: 當前畫面左上角頂點相對於Canvas左上角頂點的x軸偏移量，預設爲0，取值範圍[0,3000]
        :type X: int
        :param Y: 當前畫面左上角頂點相對於Canvas左上角頂點的y軸偏移量，預設爲0， 取值範圍[0,3000]
        :type Y: int
        :param ZOrder: 畫面z軸位置，預設爲0
z軸确定了重疊畫面的遮蓋順序，z軸值大的畫面處於頂層
        :type ZOrder: int
        """
        self.Width = None
        self.Height = None
        self.X = None
        self.Y = None
        self.ZOrder = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.ZOrder = params.get("ZOrder")


class MixStream(AbstractModel):
    """混流配置

    """

    def __init__(self):
        """
        :param Enabled: 是否開啓混流
        :type Enabled: bool
        :param DisableAudio: 是否禁用音訊混流
        :type DisableAudio: bool
        :param ModelId: 内置混流布局範本ID, 取值 [1, 2], 區别見内置混流布局範本樣式範例說明
在沒有填Custom欄位時候，ModelId是必填的
        :type ModelId: int
        :param TeacherId: 老師用戶ID
此欄位只有在ModelId填了的情況下生效
填寫TeacherId的效果是把指定爲TeacherId的用戶視訊流顯示在内置範本的第一個小畫面中
        :type TeacherId: str
        :param Custom: 自定義混流布局參數
當此欄位存在時，ModelId 及 TeacherId 欄位将被忽略
        :type Custom: :class:`taifucloudcloud.tiw.v20190919.models.CustomLayout`
        """
        self.Enabled = None
        self.DisableAudio = None
        self.ModelId = None
        self.TeacherId = None
        self.Custom = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.DisableAudio = params.get("DisableAudio")
        self.ModelId = params.get("ModelId")
        self.TeacherId = params.get("TeacherId")
        if params.get("Custom") is not None:
            self.Custom = CustomLayout()
            self.Custom._deserialize(params.get("Custom"))


class OmittedDuration(AbstractModel):
    """拼接視訊中被忽略的時間段

    """

    def __init__(self):
        """
        :param VideoTime: 錄制暫停時間戳對應的視訊播放時間(單位: 毫秒)
        :type VideoTime: int
        :param PauseTime: 錄制暫停時間戳(單位: 毫秒)
        :type PauseTime: int
        :param ResumeTime: 錄制恢複時間戳(單位: 毫秒)
        :type ResumeTime: int
        """
        self.VideoTime = None
        self.PauseTime = None
        self.ResumeTime = None


    def _deserialize(self, params):
        self.VideoTime = params.get("VideoTime")
        self.PauseTime = params.get("PauseTime")
        self.ResumeTime = params.get("ResumeTime")


class PauseOnlineRecordRequest(AbstractModel):
    """PauseOnlineRecord請求參數結構體

    """

    def __init__(self):
        """
        :param SdkAppId: 客戶的SdkAppId
        :type SdkAppId: int
        :param TaskId: 實時錄制任務 Id
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")


class PauseOnlineRecordResponse(AbstractModel):
    """PauseOnlineRecord返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResumeOnlineRecordRequest(AbstractModel):
    """ResumeOnlineRecord請求參數結構體

    """

    def __init__(self):
        """
        :param SdkAppId: 客戶的SdkAppId
        :type SdkAppId: int
        :param TaskId: 恢複錄制的實時錄制任務 Id
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")


class ResumeOnlineRecordResponse(AbstractModel):
    """ResumeOnlineRecord返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetOnlineRecordCallbackRequest(AbstractModel):
    """SetOnlineRecordCallback請求參數結構體

    """

    def __init__(self):
        """
        :param SdkAppId: 客戶的SdkAppId
        :type SdkAppId: int
        :param Callback: 實時錄制任務結果回調網址，如果傳空字串會删除原來的回調網址配置，回調網址僅支援 http或https協議，即回調網址以http://或https://開頭
        :type Callback: str
        """
        self.SdkAppId = None
        self.Callback = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Callback = params.get("Callback")


class SetOnlineRecordCallbackResponse(AbstractModel):
    """SetOnlineRecordCallback返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetTranscodeCallbackRequest(AbstractModel):
    """SetTranscodeCallback請求參數結構體

    """

    def __init__(self):
        """
        :param SdkAppId: 客戶的SdkAppId
        :type SdkAppId: int
        :param Callback: 文件轉碼進度回調網址，如果傳空字串會删除原來的回調網址配置，回調網址僅支援http或https協議，即回調網址以http://或https://開頭
        :type Callback: str
        """
        self.SdkAppId = None
        self.Callback = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.Callback = params.get("Callback")


class SetTranscodeCallbackResponse(AbstractModel):
    """SetTranscodeCallback返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StartOnlineRecordRequest(AbstractModel):
    """StartOnlineRecord請求參數結構體

    """

    def __init__(self):
        """
        :param SdkAppId: 客戶的SdkAppId
        :type SdkAppId: int
        :param RoomId: 需要錄制的房間號
        :type RoomId: int
        :param RecordUserId: 用於實時錄制服務進房的用戶Id，格式爲`tic_record_user_${RoomId}_${Random}`，其中 `${RoomId}` 與錄制房間號對應，`${Random}`爲一個随機字串。
實時錄制服務會使用這個用戶Id進房進行錄制房間内的影音與白板，爲了防止進房沖突，請保證此 用戶Id不重複
        :type RecordUserId: str
        :param RecordUserSig: 與RecordUserId對應的簽名
        :type RecordUserSig: str
        :param GroupId: 白板的 IM 群組 Id，預設同房間號
        :type GroupId: str
        :param Concat: 實時錄制視訊拼接參數
        :type Concat: :class:`taifucloudcloud.tiw.v20190919.models.Concat`
        :param Whiteboard: 實時錄制白板參數，例如白板寬高等
        :type Whiteboard: :class:`taifucloudcloud.tiw.v20190919.models.Whiteboard`
        :param MixStream: 實時錄制混流參數
特别說明：
1. 混流功能需要根據額外開通， 請聯系Top Cloud 互動白板客服人員
2. 使用混流功能，必須提供 Extras 參數，且 Extras 參數中必須包含 "MIX_STREAM"
        :type MixStream: :class:`taifucloudcloud.tiw.v20190919.models.MixStream`
        :param Extras: 使用到的高級功能清單
可以選值清單：
MIX_STREAM - 混流功能
        :type Extras: list of str
        :param AudioFileNeeded: 是否需要在結果回調中返回各路流的純音訊錄制文件，文件格式爲mp3
        :type AudioFileNeeded: bool
        """
        self.SdkAppId = None
        self.RoomId = None
        self.RecordUserId = None
        self.RecordUserSig = None
        self.GroupId = None
        self.Concat = None
        self.Whiteboard = None
        self.MixStream = None
        self.Extras = None
        self.AudioFileNeeded = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.RecordUserId = params.get("RecordUserId")
        self.RecordUserSig = params.get("RecordUserSig")
        self.GroupId = params.get("GroupId")
        if params.get("Concat") is not None:
            self.Concat = Concat()
            self.Concat._deserialize(params.get("Concat"))
        if params.get("Whiteboard") is not None:
            self.Whiteboard = Whiteboard()
            self.Whiteboard._deserialize(params.get("Whiteboard"))
        if params.get("MixStream") is not None:
            self.MixStream = MixStream()
            self.MixStream._deserialize(params.get("MixStream"))
        self.Extras = params.get("Extras")
        self.AudioFileNeeded = params.get("AudioFileNeeded")


class StartOnlineRecordResponse(AbstractModel):
    """StartOnlineRecord返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 實時錄制的任務Id
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class StopOnlineRecordRequest(AbstractModel):
    """StopOnlineRecord請求參數結構體

    """

    def __init__(self):
        """
        :param SdkAppId: 客戶的SdkAppId
        :type SdkAppId: int
        :param TaskId: 需要停止錄制的任務 Id
        :type TaskId: str
        """
        self.SdkAppId = None
        self.TaskId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.TaskId = params.get("TaskId")


class StopOnlineRecordResponse(AbstractModel):
    """StopOnlineRecord返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StreamLayout(AbstractModel):
    """流布局參數

    """

    def __init__(self):
        """
        :param LayoutParams: 流布局配置參數
        :type LayoutParams: :class:`taifucloudcloud.tiw.v20190919.models.LayoutParams`
        :param InputStreamId: 視訊流ID
流ID的取值含義如下：
1. tic_record_user - 表示當前畫面用於顯示白板視訊流
2. tic_substream - 表示當前畫面用於顯示輔路視訊流
3. 特定用戶ID - 表示當前畫面用於顯示指定用戶的視訊流
4. 不填 - 表示當前畫面用於備選，當有新的視訊流加入時，會從這些備選的空位中選擇一個沒有被占用的位置來顯示新的視訊流畫面
        :type InputStreamId: str
        :param BackgroundColor: 背景顔色，預設爲黑色，格式爲RGB格式，如紅色爲"#FF0000"
        :type BackgroundColor: str
        """
        self.LayoutParams = None
        self.InputStreamId = None
        self.BackgroundColor = None


    def _deserialize(self, params):
        if params.get("LayoutParams") is not None:
            self.LayoutParams = LayoutParams()
            self.LayoutParams._deserialize(params.get("LayoutParams"))
        self.InputStreamId = params.get("InputStreamId")
        self.BackgroundColor = params.get("BackgroundColor")


class VideoInfo(AbstractModel):
    """視訊訊息

    """

    def __init__(self):
        """
        :param VideoPlayTime: 視訊開始播放的時間（單位：毫秒）
        :type VideoPlayTime: int
        :param VideoSize: 視訊大小（位元）
        :type VideoSize: int
        :param VideoFormat: 視訊格式
        :type VideoFormat: str
        :param VideoDuration: 視訊播放時長（單位：毫秒）
        :type VideoDuration: int
        :param VideoUrl: 視訊文件URL
        :type VideoUrl: str
        :param VideoId: 視訊文件Id
        :type VideoId: str
        :param VideoType: 視訊流類型 
- 0：攝像頭視訊 
- 1：螢幕分享視訊
- 2：白板視訊 
- 3：混流視訊
- 4：純音訊（mp3)
        :type VideoType: int
        :param UserId: 攝像頭/螢幕分享視訊所屬用戶的 Id（白板視訊爲空、混流視訊tic_mixstream_房間號_混流布局類型、輔路視訊tic_substream_用戶Id）
        :type UserId: str
        """
        self.VideoPlayTime = None
        self.VideoSize = None
        self.VideoFormat = None
        self.VideoDuration = None
        self.VideoUrl = None
        self.VideoId = None
        self.VideoType = None
        self.UserId = None


    def _deserialize(self, params):
        self.VideoPlayTime = params.get("VideoPlayTime")
        self.VideoSize = params.get("VideoSize")
        self.VideoFormat = params.get("VideoFormat")
        self.VideoDuration = params.get("VideoDuration")
        self.VideoUrl = params.get("VideoUrl")
        self.VideoId = params.get("VideoId")
        self.VideoType = params.get("VideoType")
        self.UserId = params.get("UserId")


class Whiteboard(AbstractModel):
    """實時錄制白板參數，例如白板寬高等

    """

    def __init__(self):
        """
        :param Width: 實時錄制結果裏白板視訊寬，預設爲1280
        :type Width: int
        :param Height: 實時錄制結果裏白板視訊高，預設爲960
        :type Height: int
        :param InitParam: 白板初始化參數，透傳到白板 SDK
        :type InitParam: str
        """
        self.Width = None
        self.Height = None
        self.InitParam = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.InitParam = params.get("InitParam")