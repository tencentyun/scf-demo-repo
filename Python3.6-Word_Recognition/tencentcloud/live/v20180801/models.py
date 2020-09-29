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


class AddDelayLiveStreamRequest(AbstractModel):
    """AddDelayLiveStream請求參數結構體

    """

    def __init__(self):
        """
        :param AppName: 推流路徑，與推流和播放網址中的AppName保持一緻，預設爲live。
        :type AppName: str
        :param DomainName: 推流域名。
        :type DomainName: str
        :param StreamName: 流名稱。
        :type StreamName: str
        :param DelayTime: 延播時間，單位：秒，上限：600秒。
        :type DelayTime: int
        :param ExpireTime: 延播設置的過期時間。UTC 格式，例如：2018-11-29T19:00:00Z。
注意：預設7天後過期，且最長支援7天内生效。
        :type ExpireTime: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None
        self.DelayTime = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")
        self.DelayTime = params.get("DelayTime")
        self.ExpireTime = params.get("ExpireTime")


class AddDelayLiveStreamResponse(AbstractModel):
    """AddDelayLiveStream返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddLiveDomainRequest(AbstractModel):
    """AddLiveDomain請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 域名名稱。
        :type DomainName: str
        :param DomainType: 域名類型，
0：推流域名，
1：播放域名。
        :type DomainType: int
        :param PlayType: 拉流域名類型：
1：國内，
2：全球，
3：境外。
        :type PlayType: int
        :param IsDelayLive: 預設 0 ：普通直播，
1：慢直播。
        :type IsDelayLive: int
        """
        self.DomainName = None
        self.DomainType = None
        self.PlayType = None
        self.IsDelayLive = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.DomainType = params.get("DomainType")
        self.PlayType = params.get("PlayType")
        self.IsDelayLive = params.get("IsDelayLive")


class AddLiveDomainResponse(AbstractModel):
    """AddLiveDomain返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddLiveWatermarkRequest(AbstractModel):
    """AddLiveWatermark請求參數結構體

    """

    def __init__(self):
        """
        :param PictureUrl: 浮水印圖片url。
        :type PictureUrl: str
        :param WatermarkName: 浮水印名稱。
        :type WatermarkName: str
        :param XPosition: 顯示位置,X軸偏移。
        :type XPosition: int
        :param YPosition: 顯示位置,Y軸偏移。
        :type YPosition: int
        :param Width: 浮水印寬度，占直播原始畫面寬度百分比，建議高寬只設置一項，另外一項會自适應縮放，避免變形。
        :type Width: int
        :param Height: 浮水印高度，占直播原始畫面寬度百分比，建議高寬只設置一項，另外一項會自适應縮放，避免變形。
        :type Height: int
        """
        self.PictureUrl = None
        self.WatermarkName = None
        self.XPosition = None
        self.YPosition = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.PictureUrl = params.get("PictureUrl")
        self.WatermarkName = params.get("WatermarkName")
        self.XPosition = params.get("XPosition")
        self.YPosition = params.get("YPosition")
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class AddLiveWatermarkResponse(AbstractModel):
    """AddLiveWatermark返回參數結構體

    """

    def __init__(self):
        """
        :param WatermarkId: 浮水印ID。
        :type WatermarkId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.WatermarkId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")
        self.RequestId = params.get("RequestId")


class BindLiveDomainCertRequest(AbstractModel):
    """BindLiveDomainCert請求參數結構體

    """

    def __init__(self):
        """
        :param CertId: 證書Id。
        :type CertId: int
        :param DomainName: 播放域名。
        :type DomainName: str
        :param Status: 狀态，0： 關閉  1：打開。
        :type Status: int
        """
        self.CertId = None
        self.DomainName = None
        self.Status = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.DomainName = params.get("DomainName")
        self.Status = params.get("Status")


class BindLiveDomainCertResponse(AbstractModel):
    """BindLiveDomainCert返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CallBackRuleInfo(AbstractModel):
    """規則訊息

    """

    def __init__(self):
        """
        :param CreateTime: 規則創建時間。
        :type CreateTime: str
        :param UpdateTime: 規則更新時間。
        :type UpdateTime: str
        :param TemplateId: 範本Id。
        :type TemplateId: int
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路徑。
        :type AppName: str
        """
        self.CreateTime = None
        self.UpdateTime = None
        self.TemplateId = None
        self.DomainName = None
        self.AppName = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.TemplateId = params.get("TemplateId")
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")


class CallBackTemplateInfo(AbstractModel):
    """回調範本訊息

    """

    def __init__(self):
        """
        :param TemplateId: 範本Id。
        :type TemplateId: int
        :param TemplateName: 範本名稱。
        :type TemplateName: str
        :param Description: 描述訊息。
        :type Description: str
        :param StreamBeginNotifyUrl: 開播回調URL。
        :type StreamBeginNotifyUrl: str
        :param StreamEndNotifyUrl: 斷流回調URL。
        :type StreamEndNotifyUrl: str
        :param StreamMixNotifyUrl: 混流回調URL。
        :type StreamMixNotifyUrl: str
        :param RecordNotifyUrl: 錄制回調URL。
        :type RecordNotifyUrl: str
        :param SnapshotNotifyUrl: 截圖回調URL。
        :type SnapshotNotifyUrl: str
        :param PornCensorshipNotifyUrl:  回調URL。
        :type PornCensorshipNotifyUrl: str
        :param CallbackKey: 回調的鑒權key
        :type CallbackKey: str
        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.StreamBeginNotifyUrl = None
        self.StreamEndNotifyUrl = None
        self.StreamMixNotifyUrl = None
        self.RecordNotifyUrl = None
        self.SnapshotNotifyUrl = None
        self.PornCensorshipNotifyUrl = None
        self.CallbackKey = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        self.StreamBeginNotifyUrl = params.get("StreamBeginNotifyUrl")
        self.StreamEndNotifyUrl = params.get("StreamEndNotifyUrl")
        self.StreamMixNotifyUrl = params.get("StreamMixNotifyUrl")
        self.RecordNotifyUrl = params.get("RecordNotifyUrl")
        self.SnapshotNotifyUrl = params.get("SnapshotNotifyUrl")
        self.PornCensorshipNotifyUrl = params.get("PornCensorshipNotifyUrl")
        self.CallbackKey = params.get("CallbackKey")


class CertInfo(AbstractModel):
    """證書訊息

    """

    def __init__(self):
        """
        :param CertId: 證書Id。
        :type CertId: int
        :param CertName: 證書名稱。
        :type CertName: str
        :param Description: 描述訊息。
        :type Description: str
        :param CreateTime: 創建時間，UTC格式。
        :type CreateTime: str
        :param HttpsCrt: 證書内容。
        :type HttpsCrt: str
        :param CertType: 證書類型。
0：Top Cloud 托管證書
1：用戶添加證書。
        :type CertType: int
        :param CertExpireTime: 證書過期時間，UTC格式。
        :type CertExpireTime: str
        :param DomainList: 使用此證書的域名清單。
        :type DomainList: list of str
        """
        self.CertId = None
        self.CertName = None
        self.Description = None
        self.CreateTime = None
        self.HttpsCrt = None
        self.CertType = None
        self.CertExpireTime = None
        self.DomainList = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.CertName = params.get("CertName")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.HttpsCrt = params.get("HttpsCrt")
        self.CertType = params.get("CertType")
        self.CertExpireTime = params.get("CertExpireTime")
        self.DomainList = params.get("DomainList")


class CreateLiveCallbackRuleRequest(AbstractModel):
    """CreateLiveCallbackRule請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路徑，與推流和播放網址中的AppName保持一緻，預設爲live。
        :type AppName: str
        :param TemplateId: 範本ID。
        :type TemplateId: int
        """
        self.DomainName = None
        self.AppName = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.TemplateId = params.get("TemplateId")


class CreateLiveCallbackRuleResponse(AbstractModel):
    """CreateLiveCallbackRule返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLiveCallbackTemplateRequest(AbstractModel):
    """CreateLiveCallbackTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param TemplateName: 範本名稱。非空的字串
        :type TemplateName: str
        :param Description: 描述訊息。
        :type Description: str
        :param StreamBeginNotifyUrl: 開播回調URL，
相關協議文件：[事件訊息通知](/document/product/267/32744)。
        :type StreamBeginNotifyUrl: str
        :param StreamEndNotifyUrl: 斷流回調URL，
相關協議文件：[事件訊息通知](/document/product/267/32744)。
        :type StreamEndNotifyUrl: str
        :param RecordNotifyUrl: 錄制回調URL，
相關協議文件：[事件訊息通知](/document/product/267/32744)。
        :type RecordNotifyUrl: str
        :param SnapshotNotifyUrl: 截圖回調URL，
相關協議文件：[事件訊息通知](/document/product/267/32744)。
        :type SnapshotNotifyUrl: str
        :param PornCensorshipNotifyUrl:  回調URL，
相關協議文件：[事件訊息通知](/document/product/267/32741)。
        :type PornCensorshipNotifyUrl: str
        :param CallbackKey: 回調key，回調URL公用，鑒權回調說明詳見回調格式文件
        :type CallbackKey: str
        """
        self.TemplateName = None
        self.Description = None
        self.StreamBeginNotifyUrl = None
        self.StreamEndNotifyUrl = None
        self.RecordNotifyUrl = None
        self.SnapshotNotifyUrl = None
        self.PornCensorshipNotifyUrl = None
        self.CallbackKey = None


    def _deserialize(self, params):
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        self.StreamBeginNotifyUrl = params.get("StreamBeginNotifyUrl")
        self.StreamEndNotifyUrl = params.get("StreamEndNotifyUrl")
        self.RecordNotifyUrl = params.get("RecordNotifyUrl")
        self.SnapshotNotifyUrl = params.get("SnapshotNotifyUrl")
        self.PornCensorshipNotifyUrl = params.get("PornCensorshipNotifyUrl")
        self.CallbackKey = params.get("CallbackKey")


class CreateLiveCallbackTemplateResponse(AbstractModel):
    """CreateLiveCallbackTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param TemplateId: 範本ID。
        :type TemplateId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")


class CreateLiveCertRequest(AbstractModel):
    """CreateLiveCert請求參數結構體

    """

    def __init__(self):
        """
        :param CertType: 證書類型。0-用戶添加證書；1-Top Cloud 托管證書。
        :type CertType: int
        :param HttpsCrt: 證書内容，即公鑰。
        :type HttpsCrt: str
        :param HttpsKey: 私鑰。
        :type HttpsKey: str
        :param CertName: 證書名稱。
        :type CertName: str
        :param Description: 描述。
        :type Description: str
        """
        self.CertType = None
        self.HttpsCrt = None
        self.HttpsKey = None
        self.CertName = None
        self.Description = None


    def _deserialize(self, params):
        self.CertType = params.get("CertType")
        self.HttpsCrt = params.get("HttpsCrt")
        self.HttpsKey = params.get("HttpsKey")
        self.CertName = params.get("CertName")
        self.Description = params.get("Description")


class CreateLiveCertResponse(AbstractModel):
    """CreateLiveCert返回參數結構體

    """

    def __init__(self):
        """
        :param CertId: 證書ID
        :type CertId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CertId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.RequestId = params.get("RequestId")


class CreateLiveRecordRequest(AbstractModel):
    """CreateLiveRecord請求參數結構體

    """

    def __init__(self):
        """
        :param StreamName: 流名稱。
        :type StreamName: str
        :param AppName: 推流路徑，與推流和播放網址中的AppName保持一緻，預設爲 live。
        :type AppName: str
        :param DomainName: 推流域名。多域名推流必須設置。
        :type DomainName: str
        :param StartTime: 錄制開始時間。 標準時間，需要URLEncode。如 2017-01-01 10:10:01，編碼爲：2017-01-01+10%3a10%3a01。
定時錄制模式，必須設置該欄位；實時視訊錄制模式，忽略該欄位。
        :type StartTime: str
        :param EndTime: 錄制結束時間。 標準時間，需要URLEncode。如 2017-01-01 10:30:01，編碼爲：2017-01-01+10%3a30%3a01。
定時錄制模式，必須設置該欄位；實時錄制模式，爲可選欄位。如果通過Highlight參數，設置錄制爲實時視訊錄制模式，其設置的結束時間不應超過當前時間+30分鍾，如果設置的結束時間超過當前時間+30分鍾或者小於當前時間或者不設置該參數，則實際結束時間爲當前時間+30分鍾。
        :type EndTime: str
        :param RecordType: 錄制類型。
“video” : 影音錄制【預設】。
“audio” : 純音訊錄制。
在定時錄制模式或實時視訊錄制模式下，該參數均有效，不區分大小寫。
        :type RecordType: str
        :param FileFormat: 錄制文件格式。其值爲：
“flv”,“hls”,”mp4”,“aac”,”mp3”，預設“flv”。
在定時錄制模式或實時視訊錄制模式下，該參數均有效，不區分大小寫。
        :type FileFormat: str
        :param Highlight: 開啓實時視訊錄制模式標志。0：不開啓實時視訊錄制模式，即采用定時錄制模式【預設】；1：開啓實時視訊錄制模式。
        :type Highlight: int
        :param MixStream: 開啓A+B=C混流C流錄制標志。0：不開啓A+B=C混流C流錄制【預設】；1：開啓A+B=C混流C流錄制。
在定時錄制模式或實時視訊錄制模式下，該參數均有效。
        :type MixStream: int
        :param StreamParam: 錄制流參數。當前支援以下參數：
record_interval - 錄制分片時長，單位 秒，1800 - 7200
storage_time - 錄制文件儲存時長，單位 秒
eg. record_interval=3600&storage_time=2592000
注：參數需要url encode。
在定時錄制模式或實時視訊錄制模式下，該參數均有效。
        :type StreamParam: str
        """
        self.StreamName = None
        self.AppName = None
        self.DomainName = None
        self.StartTime = None
        self.EndTime = None
        self.RecordType = None
        self.FileFormat = None
        self.Highlight = None
        self.MixStream = None
        self.StreamParam = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.RecordType = params.get("RecordType")
        self.FileFormat = params.get("FileFormat")
        self.Highlight = params.get("Highlight")
        self.MixStream = params.get("MixStream")
        self.StreamParam = params.get("StreamParam")


class CreateLiveRecordResponse(AbstractModel):
    """CreateLiveRecord返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID，全局唯一標識錄制任務。
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateLiveRecordRuleRequest(AbstractModel):
    """CreateLiveRecordRule請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param TemplateId: 範本Id。
        :type TemplateId: int
        :param AppName: 推流路徑，與推流和播放網址中的AppName保持一緻，預設爲 live。
        :type AppName: str
        :param StreamName: 流名稱。
注：如果本參數設置爲非空字串，規則将只對此推流起作用。
        :type StreamName: str
        """
        self.DomainName = None
        self.TemplateId = None
        self.AppName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.TemplateId = params.get("TemplateId")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")


class CreateLiveRecordRuleResponse(AbstractModel):
    """CreateLiveRecordRule返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLiveRecordTemplateRequest(AbstractModel):
    """CreateLiveRecordTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param TemplateName: 範本名。非空的字串
        :type TemplateName: str
        :param Description: 描述訊息。
        :type Description: str
        :param FlvParam: Flv錄制參數，開啓Flv錄制時設置。
        :type FlvParam: :class:`taifucloudcloud.live.v20180801.models.RecordParam`
        :param HlsParam: Hls錄制參數，開啓hls錄制時設置。
        :type HlsParam: :class:`taifucloudcloud.live.v20180801.models.RecordParam`
        :param Mp4Param: Mp4錄制參數，開啓Mp4錄制時設置。
        :type Mp4Param: :class:`taifucloudcloud.live.v20180801.models.RecordParam`
        :param AacParam: Aac錄制參數，開啓Aac錄制時設置。
        :type AacParam: :class:`taifucloudcloud.live.v20180801.models.RecordParam`
        :param IsDelayLive: 0：普通直播，
1：慢直播。
        :type IsDelayLive: int
        :param HlsSpecialParam: HLS專屬錄制參數。
        :type HlsSpecialParam: :class:`taifucloudcloud.live.v20180801.models.HlsSpecialParam`
        """
        self.TemplateName = None
        self.Description = None
        self.FlvParam = None
        self.HlsParam = None
        self.Mp4Param = None
        self.AacParam = None
        self.IsDelayLive = None
        self.HlsSpecialParam = None


    def _deserialize(self, params):
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        if params.get("FlvParam") is not None:
            self.FlvParam = RecordParam()
            self.FlvParam._deserialize(params.get("FlvParam"))
        if params.get("HlsParam") is not None:
            self.HlsParam = RecordParam()
            self.HlsParam._deserialize(params.get("HlsParam"))
        if params.get("Mp4Param") is not None:
            self.Mp4Param = RecordParam()
            self.Mp4Param._deserialize(params.get("Mp4Param"))
        if params.get("AacParam") is not None:
            self.AacParam = RecordParam()
            self.AacParam._deserialize(params.get("AacParam"))
        self.IsDelayLive = params.get("IsDelayLive")
        if params.get("HlsSpecialParam") is not None:
            self.HlsSpecialParam = HlsSpecialParam()
            self.HlsSpecialParam._deserialize(params.get("HlsSpecialParam"))


class CreateLiveRecordTemplateResponse(AbstractModel):
    """CreateLiveRecordTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param TemplateId: 範本Id。
        :type TemplateId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")


class CreateLiveSnapshotRuleRequest(AbstractModel):
    """CreateLiveSnapshotRule請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param TemplateId: 範本Id。
        :type TemplateId: int
        :param AppName: 推流路徑，與推流和播放網址中的AppName保持一緻，預設爲 live。
        :type AppName: str
        :param StreamName: 流名稱。
注：如果本參數設置爲非空字串，規則将只對此推流起作用。
        :type StreamName: str
        """
        self.DomainName = None
        self.TemplateId = None
        self.AppName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.TemplateId = params.get("TemplateId")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")


class CreateLiveSnapshotRuleResponse(AbstractModel):
    """CreateLiveSnapshotRule返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLiveSnapshotTemplateRequest(AbstractModel):
    """CreateLiveSnapshotTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param TemplateName: 範本名稱。非空的字串。
        :type TemplateName: str
        :param CosAppId: Cos AppId。
        :type CosAppId: int
        :param CosBucket: Cos Bucket名稱。
        :type CosBucket: str
        :param CosRegion: Cos地區。
        :type CosRegion: str
        :param Description: 描述訊息。
        :type Description: str
        :param SnapshotInterval: 截圖間隔，單位s，預設10s。
        :type SnapshotInterval: int
        :param Width: 截圖寬度。預設：0（原始寬）。
        :type Width: int
        :param Height: 截圖高度。預設：0（原始高）。
        :type Height: int
        :param PornFlag: 是否開啓 ，0：不開啓，1：開啓。預設：0。
        :type PornFlag: int
        """
        self.TemplateName = None
        self.CosAppId = None
        self.CosBucket = None
        self.CosRegion = None
        self.Description = None
        self.SnapshotInterval = None
        self.Width = None
        self.Height = None
        self.PornFlag = None


    def _deserialize(self, params):
        self.TemplateName = params.get("TemplateName")
        self.CosAppId = params.get("CosAppId")
        self.CosBucket = params.get("CosBucket")
        self.CosRegion = params.get("CosRegion")
        self.Description = params.get("Description")
        self.SnapshotInterval = params.get("SnapshotInterval")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.PornFlag = params.get("PornFlag")


class CreateLiveSnapshotTemplateResponse(AbstractModel):
    """CreateLiveSnapshotTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param TemplateId: 範本Id。
        :type TemplateId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")


class CreateLiveTranscodeRuleRequest(AbstractModel):
    """CreateLiveTranscodeRule請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 播放域名。
        :type DomainName: str
        :param AppName: 推流路徑，與推流和播放網址中的AppName保持一緻，預設爲 live。
        :type AppName: str
        :param StreamName: 流名稱。
        :type StreamName: str
        :param TemplateId: 指定已有的範本Id。
        :type TemplateId: int
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        self.TemplateId = params.get("TemplateId")


class CreateLiveTranscodeRuleResponse(AbstractModel):
    """CreateLiveTranscodeRule返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLiveTranscodeTemplateRequest(AbstractModel):
    """CreateLiveTranscodeTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param TemplateName: 範本名稱，例：900 900p 僅支援字母和數字的組合。
        :type TemplateName: str
        :param VideoBitrate: 視訊碼率。範圍：100-8000。
        :type VideoBitrate: int
        :param Vcodec: 視訊編碼：h264/h265，預設h264。
注意：當前該參數未生效，待後續支援！
        :type Vcodec: str
        :param Acodec: 音訊編碼：aac，預設原始音訊格式。
注意：當前該參數未生效，待後續支援！
        :type Acodec: str
        :param AudioBitrate: 音訊碼率：預設0。0-500。
        :type AudioBitrate: int
        :param Description: 範本描述。
        :type Description: str
        :param Width: 寬，預設0。
        :type Width: int
        :param NeedVideo: 是否保留視訊，0：否，1：是。預設1。
        :type NeedVideo: int
        :param NeedAudio: 是否保留音訊，0：否，1：是。預設1。
        :type NeedAudio: int
        :param Height: 高，預設0。
        :type Height: int
        :param Fps: 幀率，預設0。
        :type Fps: int
        :param Gop: 關鍵幀間隔，單位：秒。預設原始的間隔
        :type Gop: int
        :param Rotate: 是否旋轉，0：否，1：是。預設0。
        :type Rotate: int
        :param Profile: 編碼質量：
baseline/main/high。預設baseline
        :type Profile: str
        :param BitrateToOrig: 是否不超過原始碼率，0：否，1：是。預設0。
        :type BitrateToOrig: int
        :param HeightToOrig: 是否不超過原始高，0：否，1：是。預設0。
        :type HeightToOrig: int
        :param FpsToOrig: 是否不超過原始幀率，0：否，1：是。預設0。
        :type FpsToOrig: int
        """
        self.TemplateName = None
        self.VideoBitrate = None
        self.Vcodec = None
        self.Acodec = None
        self.AudioBitrate = None
        self.Description = None
        self.Width = None
        self.NeedVideo = None
        self.NeedAudio = None
        self.Height = None
        self.Fps = None
        self.Gop = None
        self.Rotate = None
        self.Profile = None
        self.BitrateToOrig = None
        self.HeightToOrig = None
        self.FpsToOrig = None


    def _deserialize(self, params):
        self.TemplateName = params.get("TemplateName")
        self.VideoBitrate = params.get("VideoBitrate")
        self.Vcodec = params.get("Vcodec")
        self.Acodec = params.get("Acodec")
        self.AudioBitrate = params.get("AudioBitrate")
        self.Description = params.get("Description")
        self.Width = params.get("Width")
        self.NeedVideo = params.get("NeedVideo")
        self.NeedAudio = params.get("NeedAudio")
        self.Height = params.get("Height")
        self.Fps = params.get("Fps")
        self.Gop = params.get("Gop")
        self.Rotate = params.get("Rotate")
        self.Profile = params.get("Profile")
        self.BitrateToOrig = params.get("BitrateToOrig")
        self.HeightToOrig = params.get("HeightToOrig")
        self.FpsToOrig = params.get("FpsToOrig")


class CreateLiveTranscodeTemplateResponse(AbstractModel):
    """CreateLiveTranscodeTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param TemplateId: 範本Id。
        :type TemplateId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")


class CreateLiveWatermarkRuleRequest(AbstractModel):
    """CreateLiveWatermarkRule請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路徑，與推流和播放網址中的AppName保持一緻，預設爲live。
        :type AppName: str
        :param StreamName: 流名稱。
        :type StreamName: str
        :param TemplateId: 浮水印Id，即調用[AddLiveWatermark](/document/product/267/30154)介面返回的WatermarkId。
        :type TemplateId: int
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        self.TemplateId = params.get("TemplateId")


class CreateLiveWatermarkRuleResponse(AbstractModel):
    """CreateLiveWatermarkRule返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreatePullStreamConfigRequest(AbstractModel):
    """CreatePullStreamConfig請求參數結構體

    """

    def __init__(self):
        """
        :param FromUrl: 源Url。
        :type FromUrl: str
        :param ToUrl: 目的Url，目前限制該目標網址爲 域名。
        :type ToUrl: str
        :param AreaId: 區域id,1- ,2- ，3- ,4- 。
        :type AreaId: int
        :param IspId: 運營商id,1-電信,2- ,3- ,4-其他,AreaId爲4的時候,IspId只能爲其他。
        :type IspId: int
        :param StartTime: 開始時間。
使用UTC格式時間，
例如：2019-01-08T10:00:00Z。
        :type StartTime: str
        :param EndTime: 結束時間，注意：
1. 結束時間必須大於開始時間；
2. 結束時間和開始時間必須大於當前時間；
3. 結束時間 和 開始時間 間隔必須小於七天。
使用UTC格式時間，
例如：2019-01-08T10:00:00Z。
        :type EndTime: str
        """
        self.FromUrl = None
        self.ToUrl = None
        self.AreaId = None
        self.IspId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.FromUrl = params.get("FromUrl")
        self.ToUrl = params.get("ToUrl")
        self.AreaId = params.get("AreaId")
        self.IspId = params.get("IspId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class CreatePullStreamConfigResponse(AbstractModel):
    """CreatePullStreamConfig返回參數結構體

    """

    def __init__(self):
        """
        :param ConfigId: 配置成功後的id。
        :type ConfigId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ConfigId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.RequestId = params.get("RequestId")


class DayStreamPlayInfo(AbstractModel):
    """流播放訊息

    """

    def __init__(self):
        """
        :param Time: 數據時間點，格式：yyyy-mm-dd HH:MM:SS。
        :type Time: str
        :param Bandwidth: 頻寬（單位Mbps）。
        :type Bandwidth: float
        :param Flux: 流量 （單位MB）。
        :type Flux: float
        :param Request: 請求數。
        :type Request: int
        :param Online: 在線人數。
        :type Online: int
        """
        self.Time = None
        self.Bandwidth = None
        self.Flux = None
        self.Request = None
        self.Online = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Bandwidth = params.get("Bandwidth")
        self.Flux = params.get("Flux")
        self.Request = params.get("Request")
        self.Online = params.get("Online")


class DeleteLiveCallbackRuleRequest(AbstractModel):
    """DeleteLiveCallbackRule請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路徑，與推流和播放網址中的AppName保持一緻，預設爲live。
        :type AppName: str
        """
        self.DomainName = None
        self.AppName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")


class DeleteLiveCallbackRuleResponse(AbstractModel):
    """DeleteLiveCallbackRule返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveCallbackTemplateRequest(AbstractModel):
    """DeleteLiveCallbackTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param TemplateId: 範本Id。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


class DeleteLiveCallbackTemplateResponse(AbstractModel):
    """DeleteLiveCallbackTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveCertRequest(AbstractModel):
    """DeleteLiveCert請求參數結構體

    """

    def __init__(self):
        """
        :param CertId: 證書Id。
        :type CertId: int
        """
        self.CertId = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")


class DeleteLiveCertResponse(AbstractModel):
    """DeleteLiveCert返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveDomainRequest(AbstractModel):
    """DeleteLiveDomain請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 要删除的域名
        :type DomainName: str
        :param DomainType: 類型。0-推流，1-播放
        :type DomainType: int
        """
        self.DomainName = None
        self.DomainType = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.DomainType = params.get("DomainType")


class DeleteLiveDomainResponse(AbstractModel):
    """DeleteLiveDomain返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveRecordRequest(AbstractModel):
    """DeleteLiveRecord請求參數結構體

    """

    def __init__(self):
        """
        :param StreamName: 流名稱。
        :type StreamName: str
        :param TaskId: 任務ID，全局唯一標識錄制任務。
        :type TaskId: int
        """
        self.StreamName = None
        self.TaskId = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.TaskId = params.get("TaskId")


class DeleteLiveRecordResponse(AbstractModel):
    """DeleteLiveRecord返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveRecordRuleRequest(AbstractModel):
    """DeleteLiveRecordRule請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
域名+AppName+StreamName唯一標識單個轉碼規則，如需删除需要強比對，比如AppName爲空也需要傳空字串進行強比對。
        :type DomainName: str
        :param AppName: 推流路徑，與推流和播放網址中的AppName保持一緻，預設爲 live。
域名+AppName+StreamName唯一標識單個轉碼規則，如需删除需要強比對，比如AppName爲空也需要傳空字串進行強比對。
        :type AppName: str
        :param StreamName: 流名稱。
域名+AppName+StreamName唯一標識單個轉碼規則，如需删除需要強比對，比如AppName爲空也需要傳空字串進行強比對。
        :type StreamName: str
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")


class DeleteLiveRecordRuleResponse(AbstractModel):
    """DeleteLiveRecordRule返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveRecordTemplateRequest(AbstractModel):
    """DeleteLiveRecordTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param TemplateId: 範本ID。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


class DeleteLiveRecordTemplateResponse(AbstractModel):
    """DeleteLiveRecordTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveSnapshotRuleRequest(AbstractModel):
    """DeleteLiveSnapshotRule請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路徑，與推流和播放網址中的AppName保持一緻，預設爲 live。
        :type AppName: str
        :param StreamName: 流名稱。
        :type StreamName: str
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")


class DeleteLiveSnapshotRuleResponse(AbstractModel):
    """DeleteLiveSnapshotRule返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveSnapshotTemplateRequest(AbstractModel):
    """DeleteLiveSnapshotTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param TemplateId: 範本Id。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


class DeleteLiveSnapshotTemplateResponse(AbstractModel):
    """DeleteLiveSnapshotTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveTranscodeRuleRequest(AbstractModel):
    """DeleteLiveTranscodeRule請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
域名維度轉碼，域名+AppName+StreamName唯一標識單個轉碼規則，如需删除需要強比對，比如AppName爲空也需要傳空字串進行強比對。
        :type DomainName: str
        :param AppName: 推流路徑，與推流和播放網址中的AppName保持一緻，預設爲 live。
域名+AppName+StreamName+TemplateId唯一標識單個轉碼規則，如需删除需要強比對，比如AppName爲空也需要傳空字串進行強比對。
        :type AppName: str
        :param StreamName: 流名稱。
域名+AppName+StreamName+TemplateId唯一標識單個轉碼規則，如需删除需要強比對，比如AppName爲空也需要傳空字串進行強比對。
        :type StreamName: str
        :param TemplateId: 範本ID。
域名+AppName+StreamName+TemplateId唯一標識單個轉碼規則，如需删除需要強比對，比如AppName爲空也需要傳空字串進行強比對。
        :type TemplateId: int
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        self.TemplateId = params.get("TemplateId")


class DeleteLiveTranscodeRuleResponse(AbstractModel):
    """DeleteLiveTranscodeRule返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveTranscodeTemplateRequest(AbstractModel):
    """DeleteLiveTranscodeTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param TemplateId: 範本Id。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


class DeleteLiveTranscodeTemplateResponse(AbstractModel):
    """DeleteLiveTranscodeTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveWatermarkRequest(AbstractModel):
    """DeleteLiveWatermark請求參數結構體

    """

    def __init__(self):
        """
        :param WatermarkId: 浮水印ID。
        :type WatermarkId: int
        """
        self.WatermarkId = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")


class DeleteLiveWatermarkResponse(AbstractModel):
    """DeleteLiveWatermark返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveWatermarkRuleRequest(AbstractModel):
    """DeleteLiveWatermarkRule請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路徑。
        :type AppName: str
        :param StreamName: 流名稱。
        :type StreamName: str
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")


class DeleteLiveWatermarkRuleResponse(AbstractModel):
    """DeleteLiveWatermarkRule返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePullStreamConfigRequest(AbstractModel):
    """DeletePullStreamConfig請求參數結構體

    """

    def __init__(self):
        """
        :param ConfigId: 配置id。
        :type ConfigId: str
        """
        self.ConfigId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")


class DeletePullStreamConfigResponse(AbstractModel):
    """DeletePullStreamConfig返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeLiveCallbackRulesRequest(AbstractModel):
    """DescribeLiveCallbackRules請求參數結構體

    """


class DescribeLiveCallbackRulesResponse(AbstractModel):
    """DescribeLiveCallbackRules返回參數結構體

    """

    def __init__(self):
        """
        :param Rules: 規則訊息清單。
        :type Rules: list of CallBackRuleInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Rules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = CallBackRuleInfo()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveCallbackTemplateRequest(AbstractModel):
    """DescribeLiveCallbackTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param TemplateId: 範本Id。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


class DescribeLiveCallbackTemplateResponse(AbstractModel):
    """DescribeLiveCallbackTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param Template: 回調範本訊息。
        :type Template: :class:`taifucloudcloud.live.v20180801.models.CallBackTemplateInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Template = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = CallBackTemplateInfo()
            self.Template._deserialize(params.get("Template"))
        self.RequestId = params.get("RequestId")


class DescribeLiveCallbackTemplatesRequest(AbstractModel):
    """DescribeLiveCallbackTemplates請求參數結構體

    """


class DescribeLiveCallbackTemplatesResponse(AbstractModel):
    """DescribeLiveCallbackTemplates返回參數結構體

    """

    def __init__(self):
        """
        :param Templates: 範本訊息清單。
        :type Templates: list of CallBackTemplateInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Templates = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self.Templates = []
            for item in params.get("Templates"):
                obj = CallBackTemplateInfo()
                obj._deserialize(item)
                self.Templates.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveCertRequest(AbstractModel):
    """DescribeLiveCert請求參數結構體

    """

    def __init__(self):
        """
        :param CertId: 證書Id。
        :type CertId: int
        """
        self.CertId = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")


class DescribeLiveCertResponse(AbstractModel):
    """DescribeLiveCert返回參數結構體

    """

    def __init__(self):
        """
        :param CertInfo: 證書訊息。
        :type CertInfo: :class:`taifucloudcloud.live.v20180801.models.CertInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CertInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CertInfo") is not None:
            self.CertInfo = CertInfo()
            self.CertInfo._deserialize(params.get("CertInfo"))
        self.RequestId = params.get("RequestId")


class DescribeLiveCertsRequest(AbstractModel):
    """DescribeLiveCerts請求參數結構體

    """


class DescribeLiveCertsResponse(AbstractModel):
    """DescribeLiveCerts返回參數結構體

    """

    def __init__(self):
        """
        :param CertInfoSet: 證書訊息清單。
        :type CertInfoSet: list of CertInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CertInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CertInfoSet") is not None:
            self.CertInfoSet = []
            for item in params.get("CertInfoSet"):
                obj = CertInfo()
                obj._deserialize(item)
                self.CertInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveDomainCertRequest(AbstractModel):
    """DescribeLiveDomainCert請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 播放域名。
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")


class DescribeLiveDomainCertResponse(AbstractModel):
    """DescribeLiveDomainCert返回參數結構體

    """

    def __init__(self):
        """
        :param DomainCertInfo: 證書訊息。
        :type DomainCertInfo: :class:`taifucloudcloud.live.v20180801.models.DomainCertInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DomainCertInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainCertInfo") is not None:
            self.DomainCertInfo = DomainCertInfo()
            self.DomainCertInfo._deserialize(params.get("DomainCertInfo"))
        self.RequestId = params.get("RequestId")


class DescribeLiveDomainRequest(AbstractModel):
    """DescribeLiveDomain請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 域名。
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")


class DescribeLiveDomainResponse(AbstractModel):
    """DescribeLiveDomain返回參數結構體

    """

    def __init__(self):
        """
        :param DomainInfo: 域名訊息。
        :type DomainInfo: :class:`taifucloudcloud.live.v20180801.models.DomainInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DomainInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainInfo") is not None:
            self.DomainInfo = DomainInfo()
            self.DomainInfo._deserialize(params.get("DomainInfo"))
        self.RequestId = params.get("RequestId")


class DescribeLiveDomainsRequest(AbstractModel):
    """DescribeLiveDomains請求參數結構體

    """

    def __init__(self):
        """
        :param DomainStatus: 域名狀态過濾。0-停用，1-啓用
        :type DomainStatus: int
        :param DomainType: 域名類型過濾。0-推流，1-播放
        :type DomainType: int
        :param PageSize: 分頁大小，範圍：10~100。預設10
        :type PageSize: int
        :param PageNum: 取第幾頁，範圍：1~100000。預設1
        :type PageNum: int
        :param IsDelayLive: 0 普通直播 1慢直播 預設0
        :type IsDelayLive: int
        """
        self.DomainStatus = None
        self.DomainType = None
        self.PageSize = None
        self.PageNum = None
        self.IsDelayLive = None


    def _deserialize(self, params):
        self.DomainStatus = params.get("DomainStatus")
        self.DomainType = params.get("DomainType")
        self.PageSize = params.get("PageSize")
        self.PageNum = params.get("PageNum")
        self.IsDelayLive = params.get("IsDelayLive")


class DescribeLiveDomainsResponse(AbstractModel):
    """DescribeLiveDomains返回參數結構體

    """

    def __init__(self):
        """
        :param AllCount: 總記錄數
        :type AllCount: int
        :param DomainList: 域名詳細訊息清單
        :type DomainList: list of DomainInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AllCount = None
        self.DomainList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AllCount = params.get("AllCount")
        if params.get("DomainList") is not None:
            self.DomainList = []
            for item in params.get("DomainList"):
                obj = DomainInfo()
                obj._deserialize(item)
                self.DomainList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveForbidStreamListRequest(AbstractModel):
    """DescribeLiveForbidStreamList請求參數結構體

    """

    def __init__(self):
        """
        :param PageNum: 取得第幾頁，預設1。
        :type PageNum: int
        :param PageSize: 每頁大小，最大100。 
取值：1~100之前的任意整數。
預設值：10。
        :type PageSize: int
        """
        self.PageNum = None
        self.PageSize = None


    def _deserialize(self, params):
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")


class DescribeLiveForbidStreamListResponse(AbstractModel):
    """DescribeLiveForbidStreamList返回參數結構體

    """

    def __init__(self):
        """
        :param TotalNum: 符合條件的總個數。
        :type TotalNum: int
        :param TotalPage: 總頁數。
        :type TotalPage: int
        :param PageNum: 分頁的頁碼。
        :type PageNum: int
        :param PageSize: 每頁顯示的條數。
        :type PageSize: int
        :param ForbidStreamList: 禁推流清單。
        :type ForbidStreamList: list of ForbidStreamInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.TotalPage = None
        self.PageNum = None
        self.PageSize = None
        self.ForbidStreamList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        if params.get("ForbidStreamList") is not None:
            self.ForbidStreamList = []
            for item in params.get("ForbidStreamList"):
                obj = ForbidStreamInfo()
                obj._deserialize(item)
                self.ForbidStreamList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLivePlayAuthKeyRequest(AbstractModel):
    """DescribeLivePlayAuthKey請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 域名。
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")


class DescribeLivePlayAuthKeyResponse(AbstractModel):
    """DescribeLivePlayAuthKey返回參數結構體

    """

    def __init__(self):
        """
        :param PlayAuthKeyInfo: 播放鑒權key訊息。
        :type PlayAuthKeyInfo: :class:`taifucloudcloud.live.v20180801.models.PlayAuthKeyInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PlayAuthKeyInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlayAuthKeyInfo") is not None:
            self.PlayAuthKeyInfo = PlayAuthKeyInfo()
            self.PlayAuthKeyInfo._deserialize(params.get("PlayAuthKeyInfo"))
        self.RequestId = params.get("RequestId")


class DescribeLivePushAuthKeyRequest(AbstractModel):
    """DescribeLivePushAuthKey請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")


class DescribeLivePushAuthKeyResponse(AbstractModel):
    """DescribeLivePushAuthKey返回參數結構體

    """

    def __init__(self):
        """
        :param PushAuthKeyInfo: 推流鑒權key訊息。
        :type PushAuthKeyInfo: :class:`taifucloudcloud.live.v20180801.models.PushAuthKeyInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PushAuthKeyInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PushAuthKeyInfo") is not None:
            self.PushAuthKeyInfo = PushAuthKeyInfo()
            self.PushAuthKeyInfo._deserialize(params.get("PushAuthKeyInfo"))
        self.RequestId = params.get("RequestId")


class DescribeLiveRecordRulesRequest(AbstractModel):
    """DescribeLiveRecordRules請求參數結構體

    """


class DescribeLiveRecordRulesResponse(AbstractModel):
    """DescribeLiveRecordRules返回參數結構體

    """

    def __init__(self):
        """
        :param Rules: 規則清單。
        :type Rules: list of RuleInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Rules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleInfo()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveRecordTemplateRequest(AbstractModel):
    """DescribeLiveRecordTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param TemplateId: 範本Id。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


class DescribeLiveRecordTemplateResponse(AbstractModel):
    """DescribeLiveRecordTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param Template: 錄制範本訊息。
        :type Template: :class:`taifucloudcloud.live.v20180801.models.RecordTemplateInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Template = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = RecordTemplateInfo()
            self.Template._deserialize(params.get("Template"))
        self.RequestId = params.get("RequestId")


class DescribeLiveRecordTemplatesRequest(AbstractModel):
    """DescribeLiveRecordTemplates請求參數結構體

    """

    def __init__(self):
        """
        :param IsDelayLive: 是否屬於慢直播範本
        :type IsDelayLive: int
        """
        self.IsDelayLive = None


    def _deserialize(self, params):
        self.IsDelayLive = params.get("IsDelayLive")


class DescribeLiveRecordTemplatesResponse(AbstractModel):
    """DescribeLiveRecordTemplates返回參數結構體

    """

    def __init__(self):
        """
        :param Templates: 錄制範本訊息清單。
        :type Templates: list of RecordTemplateInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Templates = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self.Templates = []
            for item in params.get("Templates"):
                obj = RecordTemplateInfo()
                obj._deserialize(item)
                self.Templates.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveSnapshotRulesRequest(AbstractModel):
    """DescribeLiveSnapshotRules請求參數結構體

    """


class DescribeLiveSnapshotRulesResponse(AbstractModel):
    """DescribeLiveSnapshotRules返回參數結構體

    """

    def __init__(self):
        """
        :param Rules: 規則清單。
        :type Rules: list of RuleInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Rules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleInfo()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveSnapshotTemplateRequest(AbstractModel):
    """DescribeLiveSnapshotTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param TemplateId: 範本Id。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


class DescribeLiveSnapshotTemplateResponse(AbstractModel):
    """DescribeLiveSnapshotTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param Template: 截圖範本訊息。
        :type Template: :class:`taifucloudcloud.live.v20180801.models.SnapshotTemplateInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Template = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = SnapshotTemplateInfo()
            self.Template._deserialize(params.get("Template"))
        self.RequestId = params.get("RequestId")


class DescribeLiveSnapshotTemplatesRequest(AbstractModel):
    """DescribeLiveSnapshotTemplates請求參數結構體

    """


class DescribeLiveSnapshotTemplatesResponse(AbstractModel):
    """DescribeLiveSnapshotTemplates返回參數結構體

    """

    def __init__(self):
        """
        :param Templates: 截圖範本清單。
        :type Templates: list of SnapshotTemplateInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Templates = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self.Templates = []
            for item in params.get("Templates"):
                obj = SnapshotTemplateInfo()
                obj._deserialize(item)
                self.Templates.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveStreamEventListRequest(AbstractModel):
    """DescribeLiveStreamEventList請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 起始時間。 
UTC 格式，例如：2018-12-29T19:00:00Z。
支援查詢60天内的曆史記錄。
        :type StartTime: str
        :param EndTime: 結束時間。
UTC 格式，例如：2018-12-29T20:00:00Z。
不超過當前時間，且和起始時間相差不得超過30天。
        :type EndTime: str
        :param AppName: 推流路徑，與推流和播放網址中的AppName保持一緻，預設爲 live。
        :type AppName: str
        :param DomainName: 推流域名。
        :type DomainName: str
        :param StreamName: 流名稱，不支援通配符（*）查詢，預設模糊比對。
可使用IsStrict欄位改爲精确查詢。
        :type StreamName: str
        :param PageNum: 取得第幾頁。
預設值：1。
注： 目前只支援10000條内的查詢。
        :type PageNum: int
        :param PageSize: 分頁大小。
最大值：100。
取值範圍：1~100 之前的任意整數。
預設值：10。
注： 目前只支援10000條内的查詢。
        :type PageSize: int
        :param IsFilter: 是否過濾，預設不過濾。
0：不進行任何過濾。
1：過濾掉開播失敗的，只返回開播成功的。
        :type IsFilter: int
        :param IsStrict: 是否精确查詢，預設模糊比對。
0：模糊比對。
1：精确查詢。
注：使用StreamName時該參數生效。
        :type IsStrict: int
        :param IsAsc: 是否按結束時間正序顯示，預設逆序。
0：逆序。
1：正序。
        :type IsAsc: int
        """
        self.StartTime = None
        self.EndTime = None
        self.AppName = None
        self.DomainName = None
        self.StreamName = None
        self.PageNum = None
        self.PageSize = None
        self.IsFilter = None
        self.IsStrict = None
        self.IsAsc = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.IsFilter = params.get("IsFilter")
        self.IsStrict = params.get("IsStrict")
        self.IsAsc = params.get("IsAsc")


class DescribeLiveStreamEventListResponse(AbstractModel):
    """DescribeLiveStreamEventList返回參數結構體

    """

    def __init__(self):
        """
        :param EventList: 推斷流事件清單。
        :type EventList: list of StreamEventInfo
        :param PageNum: 分頁的頁碼。
        :type PageNum: int
        :param PageSize: 每頁大小。
        :type PageSize: int
        :param TotalNum: 符合條件的總個數。
        :type TotalNum: int
        :param TotalPage: 總頁數。
        :type TotalPage: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.EventList = None
        self.PageNum = None
        self.PageSize = None
        self.TotalNum = None
        self.TotalPage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EventList") is not None:
            self.EventList = []
            for item in params.get("EventList"):
                obj = StreamEventInfo()
                obj._deserialize(item)
                self.EventList.append(obj)
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.RequestId = params.get("RequestId")


class DescribeLiveStreamOnlineInfoRequest(AbstractModel):
    """DescribeLiveStreamOnlineInfo請求參數結構體

    """

    def __init__(self):
        """
        :param PageNum: 取得第幾頁。
預設值：1。
        :type PageNum: int
        :param PageSize: 分頁大小。
最大值：100。
取值範圍：1~100 之前的任意整數。
預設值：10。
        :type PageSize: int
        :param Status: 0:未開始推流 1:正在推流
        :type Status: int
        :param StreamName: 流名稱。
        :type StreamName: str
        """
        self.PageNum = None
        self.PageSize = None
        self.Status = None
        self.StreamName = None


    def _deserialize(self, params):
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.Status = params.get("Status")
        self.StreamName = params.get("StreamName")


class DescribeLiveStreamOnlineInfoResponse(AbstractModel):
    """DescribeLiveStreamOnlineInfo返回參數結構體

    """

    def __init__(self):
        """
        :param PageNum: 分頁的頁碼。
        :type PageNum: int
        :param PageSize: 每頁大小。
        :type PageSize: int
        :param TotalNum: 符合條件的總個數。
        :type TotalNum: int
        :param TotalPage: 總頁數。
        :type TotalPage: int
        :param StreamInfoList: 流訊息清單。
        :type StreamInfoList: list of StreamInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PageNum = None
        self.PageSize = None
        self.TotalNum = None
        self.TotalPage = None
        self.StreamInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        if params.get("StreamInfoList") is not None:
            self.StreamInfoList = []
            for item in params.get("StreamInfoList"):
                obj = StreamInfo()
                obj._deserialize(item)
                self.StreamInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveStreamOnlineListRequest(AbstractModel):
    """DescribeLiveStreamOnlineList請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路徑，與推流和播放網址中的AppName保持一緻，預設爲 live。
        :type AppName: str
        :param PageNum: 取得第幾頁，預設1。
        :type PageNum: int
        :param PageSize: 每頁大小，最大100。 
取值：10~100之間的任意整數。
預設值：10。
        :type PageSize: int
        :param StreamName: 流名稱，用於精确查詢。
        :type StreamName: str
        """
        self.DomainName = None
        self.AppName = None
        self.PageNum = None
        self.PageSize = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.StreamName = params.get("StreamName")


class DescribeLiveStreamOnlineListResponse(AbstractModel):
    """DescribeLiveStreamOnlineList返回參數結構體

    """

    def __init__(self):
        """
        :param TotalNum: 符合條件的總個數。
        :type TotalNum: int
        :param TotalPage: 總頁數。
        :type TotalPage: int
        :param PageNum: 分頁的頁碼。
        :type PageNum: int
        :param PageSize: 每頁顯示的條數。
        :type PageSize: int
        :param OnlineInfo: 正在推送流的訊息清單。
        :type OnlineInfo: list of StreamOnlineInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.TotalPage = None
        self.PageNum = None
        self.PageSize = None
        self.OnlineInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        if params.get("OnlineInfo") is not None:
            self.OnlineInfo = []
            for item in params.get("OnlineInfo"):
                obj = StreamOnlineInfo()
                obj._deserialize(item)
                self.OnlineInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveStreamPublishedListRequest(AbstractModel):
    """DescribeLiveStreamPublishedList請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 您的域名。
        :type DomainName: str
        :param EndTime: 結束時間。
UTC 格式，例如：2016-06-30T19:00:00Z。
不超過當前時間。
        :type EndTime: str
        :param StartTime: 起始時間。 
UTC 格式，例如：2016-06-29T19:00:00Z。
和當前時間相隔不超過7天。
        :type StartTime: str
        :param AppName: 推流路徑，與推流和播放網址中的AppName保持一緻，預設爲 live。
        :type AppName: str
        :param PageNum: 取得第幾頁。
預設值：1。
        :type PageNum: int
        :param PageSize: 分頁大小。
最大值：100。
取值範圍：1~100 之前的任意整數。
預設值：10。
        :type PageSize: int
        """
        self.DomainName = None
        self.EndTime = None
        self.StartTime = None
        self.AppName = None
        self.PageNum = None
        self.PageSize = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        self.AppName = params.get("AppName")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")


class DescribeLiveStreamPublishedListResponse(AbstractModel):
    """DescribeLiveStreamPublishedList返回參數結構體

    """

    def __init__(self):
        """
        :param PublishInfo: 推流記錄訊息。
        :type PublishInfo: list of StreamName
        :param PageNum: 分頁的頁碼。
        :type PageNum: int
        :param PageSize: 每頁大小
        :type PageSize: int
        :param TotalNum: 符合條件的總個數。
        :type TotalNum: int
        :param TotalPage: 總頁數。
        :type TotalPage: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PublishInfo = None
        self.PageNum = None
        self.PageSize = None
        self.TotalNum = None
        self.TotalPage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PublishInfo") is not None:
            self.PublishInfo = []
            for item in params.get("PublishInfo"):
                obj = StreamName()
                obj._deserialize(item)
                self.PublishInfo.append(obj)
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.RequestId = params.get("RequestId")


class DescribeLiveStreamPushInfoListRequest(AbstractModel):
    """DescribeLiveStreamPushInfoList請求參數結構體

    """

    def __init__(self):
        """
        :param PushDomain: 推流域名。
        :type PushDomain: str
        :param AppName: 推流路徑，與推流和播放網址中的AppName保持一緻，預設爲live。
        :type AppName: str
        :param PageNum: 頁數，
範圍[1,10000]，
預設值：1。
        :type PageNum: int
        :param PageSize: 每頁個數，
範圍：[1,1000]，
預設值： 200。
        :type PageSize: int
        """
        self.PushDomain = None
        self.AppName = None
        self.PageNum = None
        self.PageSize = None


    def _deserialize(self, params):
        self.PushDomain = params.get("PushDomain")
        self.AppName = params.get("AppName")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")


class DescribeLiveStreamPushInfoListResponse(AbstractModel):
    """DescribeLiveStreamPushInfoList返回參數結構體

    """

    def __init__(self):
        """
        :param DataInfoList: 直播流的統計訊息清單。
        :type DataInfoList: list of PushDataInfo
        :param TotalNum: 所有在線流的總數量。
        :type TotalNum: int
        :param TotalPage: 總頁數。
        :type TotalPage: int
        :param PageNum: 當前數據所在頁碼。
        :type PageNum: int
        :param PageSize: 每頁的在線流的個數。
        :type PageSize: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DataInfoList = None
        self.TotalNum = None
        self.TotalPage = None
        self.PageNum = None
        self.PageSize = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = PushDataInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.RequestId = params.get("RequestId")


class DescribeLiveStreamStateRequest(AbstractModel):
    """DescribeLiveStreamState請求參數結構體

    """

    def __init__(self):
        """
        :param AppName: 推流路徑，與推流和播放網址中的AppName保持一緻，預設爲 live。
        :type AppName: str
        :param DomainName: 您的推流域名。
        :type DomainName: str
        :param StreamName: 流名稱。
        :type StreamName: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")


class DescribeLiveStreamStateResponse(AbstractModel):
    """DescribeLiveStreamState返回參數結構體

    """

    def __init__(self):
        """
        :param StreamState: 流狀态，
active：活躍，
inactive：非活躍，
forbid：禁播。
        :type StreamState: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.StreamState = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StreamState = params.get("StreamState")
        self.RequestId = params.get("RequestId")


class DescribeLiveTranscodeDetailInfoRequest(AbstractModel):
    """DescribeLiveTranscodeDetailInfo請求參數結構體

    """

    def __init__(self):
        """
        :param DayTime: 起始時間， 時間，
格式：yyyymmdd。
注意：當前只支援查詢近30天内某天的詳細數據。
        :type DayTime: str
        :param PushDomain: 推流域名。
        :type PushDomain: str
        :param StreamName: 流名稱。
        :type StreamName: str
        :param PageNum: 頁數，預設1，
不超過100頁。
        :type PageNum: int
        :param PageSize: 每頁個數，預設20，
範圍：[10,1000]。
        :type PageSize: int
        """
        self.DayTime = None
        self.PushDomain = None
        self.StreamName = None
        self.PageNum = None
        self.PageSize = None


    def _deserialize(self, params):
        self.DayTime = params.get("DayTime")
        self.PushDomain = params.get("PushDomain")
        self.StreamName = params.get("StreamName")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")


class DescribeLiveTranscodeDetailInfoResponse(AbstractModel):
    """DescribeLiveTranscodeDetailInfo返回參數結構體

    """

    def __init__(self):
        """
        :param DataInfoList: 統計數據清單。
        :type DataInfoList: list of TranscodeDetailInfo
        :param PageNum: 頁碼。
        :type PageNum: int
        :param PageSize: 每頁個數。
        :type PageSize: int
        :param TotalNum: 總個數。
        :type TotalNum: int
        :param TotalPage: 總頁數。
        :type TotalPage: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DataInfoList = None
        self.PageNum = None
        self.PageSize = None
        self.TotalNum = None
        self.TotalPage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = TranscodeDetailInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.RequestId = params.get("RequestId")


class DescribeLiveTranscodeRulesRequest(AbstractModel):
    """DescribeLiveTranscodeRules請求參數結構體

    """


class DescribeLiveTranscodeRulesResponse(AbstractModel):
    """DescribeLiveTranscodeRules返回參數結構體

    """

    def __init__(self):
        """
        :param Rules: 轉碼規則清單。
        :type Rules: list of RuleInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Rules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleInfo()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveTranscodeTemplateRequest(AbstractModel):
    """DescribeLiveTranscodeTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param TemplateId: 範本Id。
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


class DescribeLiveTranscodeTemplateResponse(AbstractModel):
    """DescribeLiveTranscodeTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param Template: 範本訊息。
        :type Template: :class:`taifucloudcloud.live.v20180801.models.TemplateInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Template = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = TemplateInfo()
            self.Template._deserialize(params.get("Template"))
        self.RequestId = params.get("RequestId")


class DescribeLiveTranscodeTemplatesRequest(AbstractModel):
    """DescribeLiveTranscodeTemplates請求參數結構體

    """


class DescribeLiveTranscodeTemplatesResponse(AbstractModel):
    """DescribeLiveTranscodeTemplates返回參數結構體

    """

    def __init__(self):
        """
        :param Templates: 轉碼範本清單。
        :type Templates: list of TemplateInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Templates = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self.Templates = []
            for item in params.get("Templates"):
                obj = TemplateInfo()
                obj._deserialize(item)
                self.Templates.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveWatermarkRequest(AbstractModel):
    """DescribeLiveWatermark請求參數結構體

    """

    def __init__(self):
        """
        :param WatermarkId: 浮水印ID。
        :type WatermarkId: int
        """
        self.WatermarkId = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")


class DescribeLiveWatermarkResponse(AbstractModel):
    """DescribeLiveWatermark返回參數結構體

    """

    def __init__(self):
        """
        :param Watermark: 浮水印訊息。
        :type Watermark: :class:`taifucloudcloud.live.v20180801.models.WatermarkInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Watermark = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Watermark") is not None:
            self.Watermark = WatermarkInfo()
            self.Watermark._deserialize(params.get("Watermark"))
        self.RequestId = params.get("RequestId")


class DescribeLiveWatermarkRulesRequest(AbstractModel):
    """DescribeLiveWatermarkRules請求參數結構體

    """


class DescribeLiveWatermarkRulesResponse(AbstractModel):
    """DescribeLiveWatermarkRules返回參數結構體

    """

    def __init__(self):
        """
        :param Rules: 浮水印規則清單。
        :type Rules: list of RuleInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Rules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleInfo()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveWatermarksRequest(AbstractModel):
    """DescribeLiveWatermarks請求參數結構體

    """


class DescribeLiveWatermarksResponse(AbstractModel):
    """DescribeLiveWatermarks返回參數結構體

    """

    def __init__(self):
        """
        :param TotalNum: 浮水印總個數。
        :type TotalNum: int
        :param WatermarkList: 浮水印訊息清單。
        :type WatermarkList: list of WatermarkInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.WatermarkList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("WatermarkList") is not None:
            self.WatermarkList = []
            for item in params.get("WatermarkList"):
                obj = WatermarkInfo()
                obj._deserialize(item)
                self.WatermarkList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLogDownloadListRequest(AbstractModel):
    """DescribeLogDownloadList請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 開始時間， 時間。
格式：yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param EndTime: 結束時間， 時間。
格式：yyyy-mm-dd HH:MM:SS。
注意：結束時間 - 開始時間 <=7天。
        :type EndTime: str
        :param PlayDomains: 域名清單。
        :type PlayDomains: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.PlayDomains = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PlayDomains = params.get("PlayDomains")


class DescribeLogDownloadListResponse(AbstractModel):
    """DescribeLogDownloadList返回參數結構體

    """

    def __init__(self):
        """
        :param LogInfoList: 日志訊息清單。
        :type LogInfoList: list of LogInfo
        :param TotalNum: 總條數。
        :type TotalNum: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.LogInfoList = None
        self.TotalNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LogInfoList") is not None:
            self.LogInfoList = []
            for item in params.get("LogInfoList"):
                obj = LogInfo()
                obj._deserialize(item)
                self.LogInfoList.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.RequestId = params.get("RequestId")


class DescribeProIspPlaySumInfoListRequest(AbstractModel):
    """DescribeProIspPlaySumInfoList請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 起始時間， 時間，
格式：yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param EndTime: 結束時間， 時間，
格式：yyyy-mm-dd HH:MM:SS。
注：EndTime 和 StartTime 只支援最近1天的數據查詢。
        :type EndTime: str
        :param StatType: 統計的類型，可選值包括”Province”，”Isp”
        :type StatType: str
        :param PlayDomains: 不填則爲總體數據。
        :type PlayDomains: list of str
        :param PageNum: 頁號，
範圍是[1,1000]，
預設值是1
        :type PageNum: int
        :param PageSize: 每頁個數，範圍是[1,1000]，
預設值是20
        :type PageSize: int
        """
        self.StartTime = None
        self.EndTime = None
        self.StatType = None
        self.PlayDomains = None
        self.PageNum = None
        self.PageSize = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.StatType = params.get("StatType")
        self.PlayDomains = params.get("PlayDomains")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")


class DescribeProIspPlaySumInfoListResponse(AbstractModel):
    """DescribeProIspPlaySumInfoList返回參數結構體

    """

    def __init__(self):
        """
        :param TotalFlux: 總流量。
        :type TotalFlux: float
        :param TotalRequest: 總請求數。
        :type TotalRequest: int
        :param StatType: 統計的類型。
        :type StatType: str
        :param PageSize: 每頁的記錄數
        :type PageSize: int
        :param PageNum: 頁號
        :type PageNum: int
        :param TotalNum: 總記錄數
        :type TotalNum: int
        :param TotalPage: 總頁數
        :type TotalPage: int
        :param DataInfoList:  或運營商匯總數據清單
        :type DataInfoList: list of ProIspPlaySumInfo
        :param AvgFluxPerSecond: 平均頻寬
        :type AvgFluxPerSecond: float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalFlux = None
        self.TotalRequest = None
        self.StatType = None
        self.PageSize = None
        self.PageNum = None
        self.TotalNum = None
        self.TotalPage = None
        self.DataInfoList = None
        self.AvgFluxPerSecond = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalFlux = params.get("TotalFlux")
        self.TotalRequest = params.get("TotalRequest")
        self.StatType = params.get("StatType")
        self.PageSize = params.get("PageSize")
        self.PageNum = params.get("PageNum")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = ProIspPlaySumInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.AvgFluxPerSecond = params.get("AvgFluxPerSecond")
        self.RequestId = params.get("RequestId")


class DescribeProvinceIspPlayInfoListRequest(AbstractModel):
    """DescribeProvinceIspPlayInfoList請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 起始時間點，當前使用 時間，
例：2019-02-21 10:00:00。
        :type StartTime: str
        :param EndTime: 結束時間點，當前使用 時間，
例：2019-02-21 12:00:00。
注：EndTime 和 StartTime 只支援最近1天的數據查詢。
        :type EndTime: str
        :param Granularity: 支援如下粒度：
1：1分鍾粒度（跨度不支援超過1天）
        :type Granularity: int
        :param StatType: 統計指標類型：
“Bandwidth”：頻寬
“FluxPerSecond”：平均流量
“Flux”：流量
“Request”：請求數
“Online”：並發連接數
        :type StatType: str
        :param PlayDomains: 播放域名清單。
        :type PlayDomains: list of str
        :param ProvinceNames: 非必傳參數，要查詢的 （地區）英文名稱清單，如 Beijing
        :type ProvinceNames: list of str
        :param IspNames: 非必傳參數，要查詢的運營商英文名稱清單，如 China Mobile ，如果爲空，查詢所有運營商的數據
        :type IspNames: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.Granularity = None
        self.StatType = None
        self.PlayDomains = None
        self.ProvinceNames = None
        self.IspNames = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Granularity = params.get("Granularity")
        self.StatType = params.get("StatType")
        self.PlayDomains = params.get("PlayDomains")
        self.ProvinceNames = params.get("ProvinceNames")
        self.IspNames = params.get("IspNames")


class DescribeProvinceIspPlayInfoListResponse(AbstractModel):
    """DescribeProvinceIspPlayInfoList返回參數結構體

    """

    def __init__(self):
        """
        :param DataInfoList: 播放訊息清單。
        :type DataInfoList: list of PlayStatInfo
        :param StatType: 統計的類型，和輸入參數保持一緻。
        :type StatType: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DataInfoList = None
        self.StatType = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = PlayStatInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.StatType = params.get("StatType")
        self.RequestId = params.get("RequestId")


class DescribePullStreamConfigsRequest(AbstractModel):
    """DescribePullStreamConfigs請求參數結構體

    """

    def __init__(self):
        """
        :param ConfigId: 配置id。
        :type ConfigId: str
        """
        self.ConfigId = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")


class DescribePullStreamConfigsResponse(AbstractModel):
    """DescribePullStreamConfigs返回參數結構體

    """

    def __init__(self):
        """
        :param PullStreamConfigs: 拉流配置。
        :type PullStreamConfigs: list of PullStreamConfig
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PullStreamConfigs = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PullStreamConfigs") is not None:
            self.PullStreamConfigs = []
            for item in params.get("PullStreamConfigs"):
                obj = PullStreamConfig()
                obj._deserialize(item)
                self.PullStreamConfigs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStreamDayPlayInfoListRequest(AbstractModel):
    """DescribeStreamDayPlayInfoList請求參數結構體

    """

    def __init__(self):
        """
        :param DayTime: 日期，
格式：YYYY-mm-dd。
        :type DayTime: str
        :param PlayDomain: 播放域名。
        :type PlayDomain: str
        :param PageNum: 頁號，範圍[1,10]，預設值是1。
        :type PageNum: int
        :param PageSize: 每頁個數，範圍[100,1000]，預設值是1000。
        :type PageSize: int
        """
        self.DayTime = None
        self.PlayDomain = None
        self.PageNum = None
        self.PageSize = None


    def _deserialize(self, params):
        self.DayTime = params.get("DayTime")
        self.PlayDomain = params.get("PlayDomain")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")


class DescribeStreamDayPlayInfoListResponse(AbstractModel):
    """DescribeStreamDayPlayInfoList返回參數結構體

    """

    def __init__(self):
        """
        :param DataInfoList: 播放數據訊息清單。
        :type DataInfoList: list of PlayDataInfoByStream
        :param TotalNum: 總數量。
        :type TotalNum: int
        :param TotalPage: 總頁數。
        :type TotalPage: int
        :param PageNum: 當前數據所處頁碼。
        :type PageNum: int
        :param PageSize: 每頁個數。
        :type PageSize: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DataInfoList = None
        self.TotalNum = None
        self.TotalPage = None
        self.PageNum = None
        self.PageSize = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = PlayDataInfoByStream()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.RequestId = params.get("RequestId")


class DescribeStreamPlayInfoListRequest(AbstractModel):
    """DescribeStreamPlayInfoList請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 開始時間， 時間，格式爲yyyy-mm-dd HH:MM:SS，
當前時間 和 開始時間 間隔不超過30天。
        :type StartTime: str
        :param EndTime: 結束時間， 時間，格式爲yyyy-mm-dd HH:MM:SS，
結束時間 和 開始時間  必須在同一天内。
        :type EndTime: str
        :param PlayDomain: 播放域名，
若不填，則爲查詢所有播放域名的在線流數據。
        :type PlayDomain: str
        :param StreamName: 流名稱，精确比對。
若不填，則爲查詢總體播放數據。
        :type StreamName: str
        :param AppName: 推流路徑，與推流和播放網址中的AppName保持一緻，預設爲live。精确比對，不支援。
若不填，則爲查詢總體播放數據。
        :type AppName: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PlayDomain = None
        self.StreamName = None
        self.AppName = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PlayDomain = params.get("PlayDomain")
        self.StreamName = params.get("StreamName")
        self.AppName = params.get("AppName")


class DescribeStreamPlayInfoListResponse(AbstractModel):
    """DescribeStreamPlayInfoList返回參數結構體

    """

    def __init__(self):
        """
        :param DataInfoList: 統計訊息清單。
        :type DataInfoList: list of DayStreamPlayInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = DayStreamPlayInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DomainCertInfo(AbstractModel):
    """域名證書訊息

    """

    def __init__(self):
        """
        :param CertId: 證書Id。
        :type CertId: int
        :param CertName: 證書名稱。
        :type CertName: str
        :param Description: 描述訊息。
        :type Description: str
        :param CreateTime: 創建時間，UTC格式。
        :type CreateTime: str
        :param HttpsCrt: 證書内容。
        :type HttpsCrt: str
        :param CertType: 證書類型。
0：Top Cloud 托管證書
1：用戶添加證書。
        :type CertType: int
        :param CertExpireTime: 證書過期時間，UTC格式。
        :type CertExpireTime: str
        :param DomainName: 使用此證書的域名名稱。
        :type DomainName: str
        :param Status: 證書狀态
        :type Status: int
        """
        self.CertId = None
        self.CertName = None
        self.Description = None
        self.CreateTime = None
        self.HttpsCrt = None
        self.CertType = None
        self.CertExpireTime = None
        self.DomainName = None
        self.Status = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.CertName = params.get("CertName")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.HttpsCrt = params.get("HttpsCrt")
        self.CertType = params.get("CertType")
        self.CertExpireTime = params.get("CertExpireTime")
        self.DomainName = params.get("DomainName")
        self.Status = params.get("Status")


class DomainInfo(AbstractModel):
    """直播域名訊息

    """

    def __init__(self):
        """
        :param Name: 直播域名
        :type Name: str
        :param Type: 域名類型。0-推流，1-播放
        :type Type: int
        :param Status: 域名狀态。0-停用，1-啓用
        :type Status: int
        :param CreateTime: 添加時間
        :type CreateTime: str
        :param BCName: 是否有CName到固定規則域名。0-否，1-是
        :type BCName: int
        :param TargetDomain: cname對應的域名
        :type TargetDomain: str
        :param PlayType: 播放區域，只在Type=1時該參數有意義。
1-國内，2-全球，3-海外。
        :type PlayType: int
        :param IsDelayLive: 0：普通直播，
1：慢直播。
        :type IsDelayLive: int
        """
        self.Name = None
        self.Type = None
        self.Status = None
        self.CreateTime = None
        self.BCName = None
        self.TargetDomain = None
        self.PlayType = None
        self.IsDelayLive = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.BCName = params.get("BCName")
        self.TargetDomain = params.get("TargetDomain")
        self.PlayType = params.get("PlayType")
        self.IsDelayLive = params.get("IsDelayLive")


class DropLiveStreamRequest(AbstractModel):
    """DropLiveStream請求參數結構體

    """

    def __init__(self):
        """
        :param StreamName: 流名稱。
        :type StreamName: str
        :param DomainName: 您的加速域名。
        :type DomainName: str
        :param AppName: 推流路徑，與推流和播放網址中的AppName保持一緻，預設爲 live。
        :type AppName: str
        """
        self.StreamName = None
        self.DomainName = None
        self.AppName = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")


class DropLiveStreamResponse(AbstractModel):
    """DropLiveStream返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableLiveDomainRequest(AbstractModel):
    """EnableLiveDomain請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 待啓用的直播域名
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")


class EnableLiveDomainResponse(AbstractModel):
    """EnableLiveDomain返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ForbidLiveDomainRequest(AbstractModel):
    """ForbidLiveDomain請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 停用的直播域名
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")


class ForbidLiveDomainResponse(AbstractModel):
    """ForbidLiveDomain返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ForbidLiveStreamRequest(AbstractModel):
    """ForbidLiveStream請求參數結構體

    """

    def __init__(self):
        """
        :param AppName: 推流路徑，與推流和播放網址中的AppName保持一緻，預設爲 live。
        :type AppName: str
        :param DomainName: 您的加速域名。
        :type DomainName: str
        :param StreamName: 流名稱。
        :type StreamName: str
        :param ResumeTime: 恢複流的時間。UTC 格式，例如：2018-11-29T19:00:00Z。
注意：預設禁播90天，且最長支援禁播90天。
        :type ResumeTime: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None
        self.ResumeTime = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")
        self.ResumeTime = params.get("ResumeTime")


class ForbidLiveStreamResponse(AbstractModel):
    """ForbidLiveStream返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ForbidStreamInfo(AbstractModel):
    """禁推流清單

    """

    def __init__(self):
        """
        :param StreamName: 流名稱。
        :type StreamName: str
        :param CreateTime: 創建時間。
        :type CreateTime: str
        :param ExpireTime: 禁推過期時間。
        :type ExpireTime: str
        """
        self.StreamName = None
        self.CreateTime = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")


class HlsSpecialParam(AbstractModel):
    """HLS專屬錄制參數

    """

    def __init__(self):
        """
        :param FlowContinueDuration: HLS續流超時時間。
        :type FlowContinueDuration: int
        """
        self.FlowContinueDuration = None


    def _deserialize(self, params):
        self.FlowContinueDuration = params.get("FlowContinueDuration")


class LogInfo(AbstractModel):
    """日志url訊息

    """

    def __init__(self):
        """
        :param LogName: 日志名稱。
        :type LogName: str
        :param LogUrl: 日志Url。
        :type LogUrl: str
        :param LogTime: 日志生成時間
        :type LogTime: str
        """
        self.LogName = None
        self.LogUrl = None
        self.LogTime = None


    def _deserialize(self, params):
        self.LogName = params.get("LogName")
        self.LogUrl = params.get("LogUrl")
        self.LogTime = params.get("LogTime")


class ModifyLiveCallbackTemplateRequest(AbstractModel):
    """ModifyLiveCallbackTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param TemplateId: 範本Id。
        :type TemplateId: int
        :param TemplateName: 範本名稱。
        :type TemplateName: str
        :param Description: 描述訊息。
        :type Description: str
        :param StreamBeginNotifyUrl: 開播回調URL。
        :type StreamBeginNotifyUrl: str
        :param StreamEndNotifyUrl: 斷流回調URL。
        :type StreamEndNotifyUrl: str
        :param RecordNotifyUrl: 錄制回調URL。
        :type RecordNotifyUrl: str
        :param SnapshotNotifyUrl: 截圖回調URL。
        :type SnapshotNotifyUrl: str
        :param PornCensorshipNotifyUrl:  回調URL。
        :type PornCensorshipNotifyUrl: str
        :param CallbackKey: 回調key，回調URL公用，鑒權回調說明詳見回調格式文件
        :type CallbackKey: str
        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.StreamBeginNotifyUrl = None
        self.StreamEndNotifyUrl = None
        self.RecordNotifyUrl = None
        self.SnapshotNotifyUrl = None
        self.PornCensorshipNotifyUrl = None
        self.CallbackKey = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        self.StreamBeginNotifyUrl = params.get("StreamBeginNotifyUrl")
        self.StreamEndNotifyUrl = params.get("StreamEndNotifyUrl")
        self.RecordNotifyUrl = params.get("RecordNotifyUrl")
        self.SnapshotNotifyUrl = params.get("SnapshotNotifyUrl")
        self.PornCensorshipNotifyUrl = params.get("PornCensorshipNotifyUrl")
        self.CallbackKey = params.get("CallbackKey")


class ModifyLiveCallbackTemplateResponse(AbstractModel):
    """ModifyLiveCallbackTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLiveCertRequest(AbstractModel):
    """ModifyLiveCert請求參數結構體

    """

    def __init__(self):
        """
        :param CertId: 證書Id。
        :type CertId: str
        :param CertType: 證書類型。0-用戶添加證書；1-Top Cloud 托管證書。
        :type CertType: int
        :param CertName: 證書名稱。
        :type CertName: str
        :param HttpsCrt: 證書内容，即公鑰。
        :type HttpsCrt: str
        :param HttpsKey: 私鑰。
        :type HttpsKey: str
        :param Description: 描述訊息。
        :type Description: str
        """
        self.CertId = None
        self.CertType = None
        self.CertName = None
        self.HttpsCrt = None
        self.HttpsKey = None
        self.Description = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.CertType = params.get("CertType")
        self.CertName = params.get("CertName")
        self.HttpsCrt = params.get("HttpsCrt")
        self.HttpsKey = params.get("HttpsKey")
        self.Description = params.get("Description")


class ModifyLiveCertResponse(AbstractModel):
    """ModifyLiveCert返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLiveDomainCertRequest(AbstractModel):
    """ModifyLiveDomainCert請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 播放域名。
        :type DomainName: str
        :param CertId: 證書Id。
        :type CertId: int
        :param Status: 狀态，0：關閉  1：打開。
        :type Status: int
        """
        self.DomainName = None
        self.CertId = None
        self.Status = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.CertId = params.get("CertId")
        self.Status = params.get("Status")


class ModifyLiveDomainCertResponse(AbstractModel):
    """ModifyLiveDomainCert返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLivePlayAuthKeyRequest(AbstractModel):
    """ModifyLivePlayAuthKey請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 域名。
        :type DomainName: str
        :param Enable: 是否啓用，0：關閉，1：啓用。
        :type Enable: int
        :param AuthKey: 鑒權key。
        :type AuthKey: str
        :param AuthDelta: 有效時間，單位：秒。
        :type AuthDelta: int
        :param AuthBackKey: 鑒權backkey。
        :type AuthBackKey: str
        """
        self.DomainName = None
        self.Enable = None
        self.AuthKey = None
        self.AuthDelta = None
        self.AuthBackKey = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Enable = params.get("Enable")
        self.AuthKey = params.get("AuthKey")
        self.AuthDelta = params.get("AuthDelta")
        self.AuthBackKey = params.get("AuthBackKey")


class ModifyLivePlayAuthKeyResponse(AbstractModel):
    """ModifyLivePlayAuthKey返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLivePlayDomainRequest(AbstractModel):
    """ModifyLivePlayDomain請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 播放域名。
        :type DomainName: str
        :param PlayType: 拉流域名類型。1-國内；2-全球；3-境外
        :type PlayType: int
        """
        self.DomainName = None
        self.PlayType = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.PlayType = params.get("PlayType")


class ModifyLivePlayDomainResponse(AbstractModel):
    """ModifyLivePlayDomain返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLivePushAuthKeyRequest(AbstractModel):
    """ModifyLivePushAuthKey請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param Enable: 是否啓用，0：關閉，1：啓用。
        :type Enable: int
        :param MasterAuthKey: 主鑒權key。
        :type MasterAuthKey: str
        :param BackupAuthKey: 備鑒權key。
        :type BackupAuthKey: str
        :param AuthDelta: 有效時間，單位：秒。
        :type AuthDelta: int
        """
        self.DomainName = None
        self.Enable = None
        self.MasterAuthKey = None
        self.BackupAuthKey = None
        self.AuthDelta = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Enable = params.get("Enable")
        self.MasterAuthKey = params.get("MasterAuthKey")
        self.BackupAuthKey = params.get("BackupAuthKey")
        self.AuthDelta = params.get("AuthDelta")


class ModifyLivePushAuthKeyResponse(AbstractModel):
    """ModifyLivePushAuthKey返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLiveRecordTemplateRequest(AbstractModel):
    """ModifyLiveRecordTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param TemplateId: 範本Id。
        :type TemplateId: int
        :param TemplateName: 範本名稱。
        :type TemplateName: str
        :param Description: 描述訊息。
        :type Description: str
        :param FlvParam: Flv錄制參數，開啓Flv錄制時設置。
        :type FlvParam: :class:`taifucloudcloud.live.v20180801.models.RecordParam`
        :param HlsParam: Hls錄制參數，開啓hls錄制時設置。
        :type HlsParam: :class:`taifucloudcloud.live.v20180801.models.RecordParam`
        :param Mp4Param: Mp4錄制參數，開啓Mp4錄制時設置。
        :type Mp4Param: :class:`taifucloudcloud.live.v20180801.models.RecordParam`
        :param AacParam: Aac錄制參數，開啓Aac錄制時設置。
        :type AacParam: :class:`taifucloudcloud.live.v20180801.models.RecordParam`
        :param HlsSpecialParam: HLS錄制定制參數
        :type HlsSpecialParam: :class:`taifucloudcloud.live.v20180801.models.HlsSpecialParam`
        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.FlvParam = None
        self.HlsParam = None
        self.Mp4Param = None
        self.AacParam = None
        self.HlsSpecialParam = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        if params.get("FlvParam") is not None:
            self.FlvParam = RecordParam()
            self.FlvParam._deserialize(params.get("FlvParam"))
        if params.get("HlsParam") is not None:
            self.HlsParam = RecordParam()
            self.HlsParam._deserialize(params.get("HlsParam"))
        if params.get("Mp4Param") is not None:
            self.Mp4Param = RecordParam()
            self.Mp4Param._deserialize(params.get("Mp4Param"))
        if params.get("AacParam") is not None:
            self.AacParam = RecordParam()
            self.AacParam._deserialize(params.get("AacParam"))
        if params.get("HlsSpecialParam") is not None:
            self.HlsSpecialParam = HlsSpecialParam()
            self.HlsSpecialParam._deserialize(params.get("HlsSpecialParam"))


class ModifyLiveRecordTemplateResponse(AbstractModel):
    """ModifyLiveRecordTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLiveSnapshotTemplateRequest(AbstractModel):
    """ModifyLiveSnapshotTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param TemplateId: 範本Id。
        :type TemplateId: int
        :param TemplateName: 範本名稱。
        :type TemplateName: str
        :param Description: 描述訊息。
        :type Description: str
        :param SnapshotInterval: 截圖時間間隔
        :type SnapshotInterval: int
        :param Width: 截圖寬度。
        :type Width: int
        :param Height: 截圖高度。
        :type Height: int
        :param PornFlag: 是否開啓 ，0：不開啓，1：開啓。
        :type PornFlag: int
        :param CosAppId: Cos AppId。
        :type CosAppId: int
        :param CosBucket: Cos Bucket名稱。
        :type CosBucket: str
        :param CosRegion: Cos 地域。
        :type CosRegion: str
        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.SnapshotInterval = None
        self.Width = None
        self.Height = None
        self.PornFlag = None
        self.CosAppId = None
        self.CosBucket = None
        self.CosRegion = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        self.SnapshotInterval = params.get("SnapshotInterval")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.PornFlag = params.get("PornFlag")
        self.CosAppId = params.get("CosAppId")
        self.CosBucket = params.get("CosBucket")
        self.CosRegion = params.get("CosRegion")


class ModifyLiveSnapshotTemplateResponse(AbstractModel):
    """ModifyLiveSnapshotTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLiveTranscodeTemplateRequest(AbstractModel):
    """ModifyLiveTranscodeTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param TemplateId: 範本Id。
        :type TemplateId: int
        :param Vcodec: 視訊編碼：
h264/h265。
        :type Vcodec: str
        :param Acodec: 音訊編碼：
aac/mp3。
        :type Acodec: str
        :param AudioBitrate: 音訊碼率，預設0。0-500
        :type AudioBitrate: int
        :param Description: 範本描述。
        :type Description: str
        :param VideoBitrate: 視訊碼率。100-8000
        :type VideoBitrate: int
        :param Width: 寬。0-3000
        :type Width: int
        :param NeedVideo: 是否保留視訊，0：否，1：是。預設1。
        :type NeedVideo: int
        :param NeedAudio: 是否保留音訊，0：否，1：是。預設1。
        :type NeedAudio: int
        :param Height: 高。0-3000
        :type Height: int
        :param Fps: 幀率。0-200
        :type Fps: int
        :param Gop: 關鍵幀間隔，單位：秒。0-50
        :type Gop: int
        :param Rotate: 旋轉角度。0 90 180 270
        :type Rotate: int
        :param Profile: 編碼質量：
baseline/main/high。
        :type Profile: str
        :param BitrateToOrig: 是否不超過原始碼率。0：否，1：是。預設0。
        :type BitrateToOrig: int
        :param HeightToOrig: 是否不超過原始高。0：否，1：是。預設0。
        :type HeightToOrig: int
        :param FpsToOrig: 是否不超過原始幀率。0：否，1：是。預設0。
        :type FpsToOrig: int
        """
        self.TemplateId = None
        self.Vcodec = None
        self.Acodec = None
        self.AudioBitrate = None
        self.Description = None
        self.VideoBitrate = None
        self.Width = None
        self.NeedVideo = None
        self.NeedAudio = None
        self.Height = None
        self.Fps = None
        self.Gop = None
        self.Rotate = None
        self.Profile = None
        self.BitrateToOrig = None
        self.HeightToOrig = None
        self.FpsToOrig = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.Vcodec = params.get("Vcodec")
        self.Acodec = params.get("Acodec")
        self.AudioBitrate = params.get("AudioBitrate")
        self.Description = params.get("Description")
        self.VideoBitrate = params.get("VideoBitrate")
        self.Width = params.get("Width")
        self.NeedVideo = params.get("NeedVideo")
        self.NeedAudio = params.get("NeedAudio")
        self.Height = params.get("Height")
        self.Fps = params.get("Fps")
        self.Gop = params.get("Gop")
        self.Rotate = params.get("Rotate")
        self.Profile = params.get("Profile")
        self.BitrateToOrig = params.get("BitrateToOrig")
        self.HeightToOrig = params.get("HeightToOrig")
        self.FpsToOrig = params.get("FpsToOrig")


class ModifyLiveTranscodeTemplateResponse(AbstractModel):
    """ModifyLiveTranscodeTemplate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPullStreamConfigRequest(AbstractModel):
    """ModifyPullStreamConfig請求參數結構體

    """

    def __init__(self):
        """
        :param ConfigId: 配置id。
        :type ConfigId: str
        :param FromUrl: 源Url。
        :type FromUrl: str
        :param ToUrl: 目的Url。
        :type ToUrl: str
        :param AreaId: 區域id,1- ,2- ，3- ,4- 。如有改動，需同時傳入IspId。
        :type AreaId: int
        :param IspId: 運營商id,1-電信,2- ,3- ,4-其他,AreaId爲4的時候,IspId只能爲其他。如有改動，需同時傳入AreaId。
        :type IspId: int
        :param StartTime: 開始時間。
使用UTC格式時間，
例如：2019-01-08T10:00:00Z。
        :type StartTime: str
        :param EndTime: 結束時間，注意：
1. 結束時間必須大於開始時間；
2. 結束時間和開始時間必須大於當前時間；
3. 結束時間 和 開始時間 間隔必須小於七天。

使用UTC格式時間，
例如：2019-01-08T10:00:00Z。
        :type EndTime: str
        """
        self.ConfigId = None
        self.FromUrl = None
        self.ToUrl = None
        self.AreaId = None
        self.IspId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.FromUrl = params.get("FromUrl")
        self.ToUrl = params.get("ToUrl")
        self.AreaId = params.get("AreaId")
        self.IspId = params.get("IspId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class ModifyPullStreamConfigResponse(AbstractModel):
    """ModifyPullStreamConfig返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPullStreamStatusRequest(AbstractModel):
    """ModifyPullStreamStatus請求參數結構體

    """

    def __init__(self):
        """
        :param ConfigIds: 配置id清單。
        :type ConfigIds: list of str
        :param Status: 目標狀态。0無效，2正在運作，4暫停。
        :type Status: str
        """
        self.ConfigIds = None
        self.Status = None


    def _deserialize(self, params):
        self.ConfigIds = params.get("ConfigIds")
        self.Status = params.get("Status")


class ModifyPullStreamStatusResponse(AbstractModel):
    """ModifyPullStreamStatus返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PlayAuthKeyInfo(AbstractModel):
    """播放鑒權key訊息

    """

    def __init__(self):
        """
        :param DomainName: 域名。
        :type DomainName: str
        :param Enable: 是否啓用，0：關閉，1：啓用。
        :type Enable: int
        :param AuthKey: 鑒權key。
        :type AuthKey: str
        :param AuthDelta: 有效時間，單位：秒。
        :type AuthDelta: int
        :param AuthBackKey: 鑒權BackKey。
        :type AuthBackKey: str
        """
        self.DomainName = None
        self.Enable = None
        self.AuthKey = None
        self.AuthDelta = None
        self.AuthBackKey = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Enable = params.get("Enable")
        self.AuthKey = params.get("AuthKey")
        self.AuthDelta = params.get("AuthDelta")
        self.AuthBackKey = params.get("AuthBackKey")


class PlayDataInfoByStream(AbstractModel):
    """流維度的播放訊息

    """

    def __init__(self):
        """
        :param StreamName: 流名稱。
        :type StreamName: str
        :param TotalFlux: 總流量（單位MB）。
        :type TotalFlux: float
        """
        self.StreamName = None
        self.TotalFlux = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.TotalFlux = params.get("TotalFlux")


class PlayStatInfo(AbstractModel):
    """按 運營商查詢的播放訊息

    """

    def __init__(self):
        """
        :param Time: 數據時間點。
        :type Time: str
        :param Value: 頻寬/流量/請求數/並發連接數/下載速度的值，若沒數據返回時該值爲0
注意：此欄位可能返回 null，表示取不到有效值。
        :type Value: float
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")


class ProIspPlaySumInfo(AbstractModel):
    """獲取 /運營商的播放訊息

    """

    def __init__(self):
        """
        :param Name:  /運營商。
        :type Name: str
        :param TotalFlux: 總流量，單位：MB。
        :type TotalFlux: float
        :param TotalRequest: 總請求數。
        :type TotalRequest: int
        :param AvgFluxPerSecond: 平均下載流量，單位：MB/s
        :type AvgFluxPerSecond: float
        """
        self.Name = None
        self.TotalFlux = None
        self.TotalRequest = None
        self.AvgFluxPerSecond = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.TotalFlux = params.get("TotalFlux")
        self.TotalRequest = params.get("TotalRequest")
        self.AvgFluxPerSecond = params.get("AvgFluxPerSecond")


class PublishTime(AbstractModel):
    """推流時間

    """

    def __init__(self):
        """
        :param PublishTime: 推流時間
UTC 格式，例如：2018-06-29T19:00:00Z。
        :type PublishTime: str
        """
        self.PublishTime = None


    def _deserialize(self, params):
        self.PublishTime = params.get("PublishTime")


class PullStreamConfig(AbstractModel):
    """拉流配置

    """

    def __init__(self):
        """
        :param ConfigId: 拉流配置Id。
        :type ConfigId: str
        :param FromUrl: 源Url。
        :type FromUrl: str
        :param ToUrl: 目的Url。
        :type ToUrl: str
        :param AreaName: 區域名。
        :type AreaName: str
        :param IspName: 運營商名。
        :type IspName: str
        :param StartTime: 開始時間。
UTC格式時間，
例如：2019-01-08T10:00:00Z。
        :type StartTime: str
        :param EndTime: 結束時間。

UTC格式時間，
例如：2019-01-08T10:00:00Z。
        :type EndTime: str
        :param Status: 0無效，1初始狀态，2正在運作，3拉起失敗，4暫停。
        :type Status: str
        """
        self.ConfigId = None
        self.FromUrl = None
        self.ToUrl = None
        self.AreaName = None
        self.IspName = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None


    def _deserialize(self, params):
        self.ConfigId = params.get("ConfigId")
        self.FromUrl = params.get("FromUrl")
        self.ToUrl = params.get("ToUrl")
        self.AreaName = params.get("AreaName")
        self.IspName = params.get("IspName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")


class PushAuthKeyInfo(AbstractModel):
    """推流鑒權key訊息

    """

    def __init__(self):
        """
        :param DomainName: 域名。
        :type DomainName: str
        :param Enable: 是否啓用，0：關閉，1：啓用。
        :type Enable: int
        :param MasterAuthKey: 主鑒權key。
        :type MasterAuthKey: str
        :param BackupAuthKey: 備鑒權key。
        :type BackupAuthKey: str
        :param AuthDelta: 有效時間，單位：秒。
        :type AuthDelta: int
        """
        self.DomainName = None
        self.Enable = None
        self.MasterAuthKey = None
        self.BackupAuthKey = None
        self.AuthDelta = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Enable = params.get("Enable")
        self.MasterAuthKey = params.get("MasterAuthKey")
        self.BackupAuthKey = params.get("BackupAuthKey")
        self.AuthDelta = params.get("AuthDelta")


class PushDataInfo(AbstractModel):
    """推流數據訊息

    """

    def __init__(self):
        """
        :param StreamName: 流名稱。
        :type StreamName: str
        :param AppName: 推流路徑。
        :type AppName: str
        :param ClientIp: 推流用戶端ip。
        :type ClientIp: str
        :param ServerIp: 接流服務器ip。
        :type ServerIp: str
        :param VideoFps: 推流視訊幀率，單位是Hz。
        :type VideoFps: int
        :param VideoSpeed: 推流視訊碼率，單位是bps。
        :type VideoSpeed: int
        :param AudioFps: 推流音訊幀率，單位是Hz。
        :type AudioFps: int
        :param AudioSpeed: 推流音訊碼率，單位是bps。
        :type AudioSpeed: int
        :param PushDomain: 推流域名。
        :type PushDomain: str
        :param BeginPushTime: 推流開始時間。
        :type BeginPushTime: str
        :param Acodec: 音訊編碼格式，
例："AAC"。
        :type Acodec: str
        :param Vcodec: 視訊編碼格式，
例："H264"。
        :type Vcodec: str
        :param Resolution: 分辨率。
        :type Resolution: str
        """
        self.StreamName = None
        self.AppName = None
        self.ClientIp = None
        self.ServerIp = None
        self.VideoFps = None
        self.VideoSpeed = None
        self.AudioFps = None
        self.AudioSpeed = None
        self.PushDomain = None
        self.BeginPushTime = None
        self.Acodec = None
        self.Vcodec = None
        self.Resolution = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.AppName = params.get("AppName")
        self.ClientIp = params.get("ClientIp")
        self.ServerIp = params.get("ServerIp")
        self.VideoFps = params.get("VideoFps")
        self.VideoSpeed = params.get("VideoSpeed")
        self.AudioFps = params.get("AudioFps")
        self.AudioSpeed = params.get("AudioSpeed")
        self.PushDomain = params.get("PushDomain")
        self.BeginPushTime = params.get("BeginPushTime")
        self.Acodec = params.get("Acodec")
        self.Vcodec = params.get("Vcodec")
        self.Resolution = params.get("Resolution")


class RecordParam(AbstractModel):
    """錄制範本參數

    """

    def __init__(self):
        """
        :param RecordInterval: 錄制間隔。
單位秒，預設值1800。
取值範圍:300-7200。
此參數對 HLS 無效，當錄制 HLS 時從推流到斷流生成一個文件。
        :type RecordInterval: int
        :param StorageTime: 錄制儲存時長。
單位秒，取值範圍： 0-5184000。
0表示永久儲存。
        :type StorageTime: int
        :param Enable: 是否開啓當前格式錄制，0 否 1是。預設值0。
        :type Enable: int
        """
        self.RecordInterval = None
        self.StorageTime = None
        self.Enable = None


    def _deserialize(self, params):
        self.RecordInterval = params.get("RecordInterval")
        self.StorageTime = params.get("StorageTime")
        self.Enable = params.get("Enable")


class RecordTemplateInfo(AbstractModel):
    """錄制範本訊息

    """

    def __init__(self):
        """
        :param TemplateId: 範本Id。
        :type TemplateId: int
        :param TemplateName: 範本名稱。
        :type TemplateName: str
        :param Description: 描述訊息。
        :type Description: str
        :param FlvParam: Flv錄制參數。
        :type FlvParam: :class:`taifucloudcloud.live.v20180801.models.RecordParam`
        :param HlsParam: Hls錄制參數。
        :type HlsParam: :class:`taifucloudcloud.live.v20180801.models.RecordParam`
        :param Mp4Param: Mp4錄制參數。
        :type Mp4Param: :class:`taifucloudcloud.live.v20180801.models.RecordParam`
        :param AacParam: Aac錄制參數。
        :type AacParam: :class:`taifucloudcloud.live.v20180801.models.RecordParam`
        :param IsDelayLive: 0：普通直播，
1：慢直播。
        :type IsDelayLive: int
        :param HlsSpecialParam: HLS錄制定制參數
        :type HlsSpecialParam: :class:`taifucloudcloud.live.v20180801.models.HlsSpecialParam`
        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.FlvParam = None
        self.HlsParam = None
        self.Mp4Param = None
        self.AacParam = None
        self.IsDelayLive = None
        self.HlsSpecialParam = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        if params.get("FlvParam") is not None:
            self.FlvParam = RecordParam()
            self.FlvParam._deserialize(params.get("FlvParam"))
        if params.get("HlsParam") is not None:
            self.HlsParam = RecordParam()
            self.HlsParam._deserialize(params.get("HlsParam"))
        if params.get("Mp4Param") is not None:
            self.Mp4Param = RecordParam()
            self.Mp4Param._deserialize(params.get("Mp4Param"))
        if params.get("AacParam") is not None:
            self.AacParam = RecordParam()
            self.AacParam._deserialize(params.get("AacParam"))
        self.IsDelayLive = params.get("IsDelayLive")
        if params.get("HlsSpecialParam") is not None:
            self.HlsSpecialParam = HlsSpecialParam()
            self.HlsSpecialParam._deserialize(params.get("HlsSpecialParam"))


class ResumeDelayLiveStreamRequest(AbstractModel):
    """ResumeDelayLiveStream請求參數結構體

    """

    def __init__(self):
        """
        :param AppName: 推流路徑，與推流和播放網址中的AppName保持一緻，預設爲live。
        :type AppName: str
        :param DomainName: 推流域名。
        :type DomainName: str
        :param StreamName: 流名稱。
        :type StreamName: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")


class ResumeDelayLiveStreamResponse(AbstractModel):
    """ResumeDelayLiveStream返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResumeLiveStreamRequest(AbstractModel):
    """ResumeLiveStream請求參數結構體

    """

    def __init__(self):
        """
        :param AppName: 推流路徑，與推流和播放網址中的AppName保持一緻，預設爲 live。
        :type AppName: str
        :param DomainName: 您的加速域名。
        :type DomainName: str
        :param StreamName: 流名稱。
        :type StreamName: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")


class ResumeLiveStreamResponse(AbstractModel):
    """ResumeLiveStream返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RuleInfo(AbstractModel):
    """規則訊息

    """

    def __init__(self):
        """
        :param CreateTime: 規則創建時間。
        :type CreateTime: str
        :param UpdateTime: 規則更新時間。
        :type UpdateTime: str
        :param TemplateId: 範本Id。
        :type TemplateId: int
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路徑。
        :type AppName: str
        :param StreamName: 流名稱。
        :type StreamName: str
        """
        self.CreateTime = None
        self.UpdateTime = None
        self.TemplateId = None
        self.DomainName = None
        self.AppName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.TemplateId = params.get("TemplateId")
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")


class SetLiveWatermarkStatusRequest(AbstractModel):
    """SetLiveWatermarkStatus請求參數結構體

    """

    def __init__(self):
        """
        :param WatermarkId: 浮水印ID。
        :type WatermarkId: int
        :param Status: 狀态。0：停用，1:啓用
        :type Status: int
        """
        self.WatermarkId = None
        self.Status = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")
        self.Status = params.get("Status")


class SetLiveWatermarkStatusResponse(AbstractModel):
    """SetLiveWatermarkStatus返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SnapshotTemplateInfo(AbstractModel):
    """截圖範本訊息

    """

    def __init__(self):
        """
        :param TemplateId: 範本Id。
        :type TemplateId: int
        :param TemplateName: 範本名稱。
        :type TemplateName: str
        :param SnapshotInterval: 截圖時間間隔。5-300
        :type SnapshotInterval: int
        :param Width: 截圖寬度。0-3000 0原始寬度並适配原始比例
        :type Width: int
        :param Height: 截圖高度。0-2000 0原始高度並适配原始比例
        :type Height: int
        :param PornFlag: 是否開啓 ，0：不開啓，1：開啓。
        :type PornFlag: int
        :param CosAppId: Cos AppId。
        :type CosAppId: int
        :param CosBucket: Cos Bucket名稱。
        :type CosBucket: str
        :param CosRegion: Cos 地域。
        :type CosRegion: str
        :param Description: 範本描述
        :type Description: str
        """
        self.TemplateId = None
        self.TemplateName = None
        self.SnapshotInterval = None
        self.Width = None
        self.Height = None
        self.PornFlag = None
        self.CosAppId = None
        self.CosBucket = None
        self.CosRegion = None
        self.Description = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.SnapshotInterval = params.get("SnapshotInterval")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.PornFlag = params.get("PornFlag")
        self.CosAppId = params.get("CosAppId")
        self.CosBucket = params.get("CosBucket")
        self.CosRegion = params.get("CosRegion")
        self.Description = params.get("Description")


class StopLiveRecordRequest(AbstractModel):
    """StopLiveRecord請求參數結構體

    """

    def __init__(self):
        """
        :param StreamName: 流名稱。
        :type StreamName: str
        :param TaskId: 任務ID，全局唯一標識錄制任務。
        :type TaskId: int
        """
        self.StreamName = None
        self.TaskId = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.TaskId = params.get("TaskId")


class StopLiveRecordResponse(AbstractModel):
    """StopLiveRecord返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StreamEventInfo(AbstractModel):
    """推斷流事件訊息。

    """

    def __init__(self):
        """
        :param AppName: 應用名稱。
        :type AppName: str
        :param DomainName: 推流域名。
        :type DomainName: str
        :param StreamName: 流名稱。
        :type StreamName: str
        :param StreamStartTime: 推流開始時間。
UTC格式時間，
例如：2019-01-07T12:00:00Z。
        :type StreamStartTime: str
        :param StreamEndTime: 推流結束時間。
UTC格式時間，
例如：2019-01-07T15:00:00Z。
        :type StreamEndTime: str
        :param StopReason: 停止原因。
        :type StopReason: str
        :param Duration: 推流持續時長，單位：秒。
        :type Duration: int
        :param ClientIp: 主播IP。
        :type ClientIp: str
        :param Resolution: 分辨率。
        :type Resolution: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None
        self.StreamStartTime = None
        self.StreamEndTime = None
        self.StopReason = None
        self.Duration = None
        self.ClientIp = None
        self.Resolution = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")
        self.StreamStartTime = params.get("StreamStartTime")
        self.StreamEndTime = params.get("StreamEndTime")
        self.StopReason = params.get("StopReason")
        self.Duration = params.get("Duration")
        self.ClientIp = params.get("ClientIp")
        self.Resolution = params.get("Resolution")


class StreamInfo(AbstractModel):
    """推流訊息

    """

    def __init__(self):
        """
        :param AppName: 直播流所屬應用名稱
        :type AppName: str
        :param CreateMode: 創模組化式
        :type CreateMode: str
        :param CreateTime: 創建時間，如: 2018-07-13 14:48:23
        :type CreateTime: str
        :param Status: 流狀态
        :type Status: int
        :param StreamId: 流id
        :type StreamId: str
        :param StreamName: 流名稱
        :type StreamName: str
        :param WaterMarkId: 浮水印id
        :type WaterMarkId: str
        """
        self.AppName = None
        self.CreateMode = None
        self.CreateTime = None
        self.Status = None
        self.StreamId = None
        self.StreamName = None
        self.WaterMarkId = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.CreateMode = params.get("CreateMode")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")
        self.StreamId = params.get("StreamId")
        self.StreamName = params.get("StreamName")
        self.WaterMarkId = params.get("WaterMarkId")


class StreamName(AbstractModel):
    """流名稱清單

    """

    def __init__(self):
        """
        :param StreamName: 流名稱。
        :type StreamName: str
        """
        self.StreamName = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")


class StreamOnlineInfo(AbstractModel):
    """查詢當前正在推流的訊息

    """

    def __init__(self):
        """
        :param StreamName: 流名稱。
        :type StreamName: str
        :param PublishTimeList: 推流時間清單
        :type PublishTimeList: list of PublishTime
        :param AppName: 應用名稱。
        :type AppName: str
        :param DomainName: 推流域名。
        :type DomainName: str
        """
        self.StreamName = None
        self.PublishTimeList = None
        self.AppName = None
        self.DomainName = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        if params.get("PublishTimeList") is not None:
            self.PublishTimeList = []
            for item in params.get("PublishTimeList"):
                obj = PublishTime()
                obj._deserialize(item)
                self.PublishTimeList.append(obj)
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")


class TemplateInfo(AbstractModel):
    """轉碼範本訊息

    """

    def __init__(self):
        """
        :param Vcodec: 視訊編碼：
h264/h265。
        :type Vcodec: str
        :param VideoBitrate: 視訊碼率。100-8000kbps
        :type VideoBitrate: int
        :param Acodec: 音訊編碼：aac/mp3
aac/mp3。
        :type Acodec: str
        :param AudioBitrate: 音訊碼率。0-500
        :type AudioBitrate: int
        :param Width: 寬。0-3000
        :type Width: int
        :param Height: 高。0-3000
        :type Height: int
        :param Fps: 幀率。0-200
        :type Fps: int
        :param Gop: 關鍵幀間隔，單位：秒。1-50
        :type Gop: int
        :param Rotate: 旋轉角度。0 90 180 270
        :type Rotate: int
        :param Profile: 編碼質量：
baseline/main/high。
        :type Profile: str
        :param BitrateToOrig: 是否不超過原始碼率。0：否，1：是。
        :type BitrateToOrig: int
        :param HeightToOrig: 是否不超過原始高度。0：否，1：是。
        :type HeightToOrig: int
        :param FpsToOrig: 是否不超過原始幀率。0：否，1：是。
        :type FpsToOrig: int
        :param NeedVideo: 是否保留視訊。0：否，1：是。
        :type NeedVideo: int
        :param NeedAudio: 是否保留音訊。0：否，1：是。
        :type NeedAudio: int
        :param TemplateId: 範本Id。
        :type TemplateId: int
        :param TemplateName: 範本名稱
        :type TemplateName: str
        :param Description: 範本描述
        :type Description: str
        """
        self.Vcodec = None
        self.VideoBitrate = None
        self.Acodec = None
        self.AudioBitrate = None
        self.Width = None
        self.Height = None
        self.Fps = None
        self.Gop = None
        self.Rotate = None
        self.Profile = None
        self.BitrateToOrig = None
        self.HeightToOrig = None
        self.FpsToOrig = None
        self.NeedVideo = None
        self.NeedAudio = None
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None


    def _deserialize(self, params):
        self.Vcodec = params.get("Vcodec")
        self.VideoBitrate = params.get("VideoBitrate")
        self.Acodec = params.get("Acodec")
        self.AudioBitrate = params.get("AudioBitrate")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Fps = params.get("Fps")
        self.Gop = params.get("Gop")
        self.Rotate = params.get("Rotate")
        self.Profile = params.get("Profile")
        self.BitrateToOrig = params.get("BitrateToOrig")
        self.HeightToOrig = params.get("HeightToOrig")
        self.FpsToOrig = params.get("FpsToOrig")
        self.NeedVideo = params.get("NeedVideo")
        self.NeedAudio = params.get("NeedAudio")
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")


class TranscodeDetailInfo(AbstractModel):
    """轉碼詳細訊息

    """

    def __init__(self):
        """
        :param StreamName: 流名稱。
        :type StreamName: str
        :param StartTime: 開始時間， 時間，
格式：yyyy-mm-dd HH:MM。
        :type StartTime: str
        :param EndTime: 結束時間， 時間，
格式：yyyy-mm-dd HH:MM。
        :type EndTime: str
        :param Duration: 轉碼時長，單位：分鍾。
注意：因推流過程中可能有中斷重推情況，此處時長爲真實轉碼時長累加值，並非結束時間和開始時間的間隔。
        :type Duration: int
        :param ModuleCodec: 編碼方式，帶模組，
範例：
liveprocessor_H264 =》直播轉碼-H264，
liveprocessor_H265 =》 直播轉碼-H265，
topspeed_H264 =》極速高清-H264，
topspeed_H265 =》極速高清-H265。
        :type ModuleCodec: str
        :param Bitrate: 碼率。
        :type Bitrate: int
        :param Type: 類型，包含：轉碼(Transcode)，混流(MixStream)，浮水印(WaterMark)。
        :type Type: str
        :param PushDomain: 推流域名。
        :type PushDomain: str
        """
        self.StreamName = None
        self.StartTime = None
        self.EndTime = None
        self.Duration = None
        self.ModuleCodec = None
        self.Bitrate = None
        self.Type = None
        self.PushDomain = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Duration = params.get("Duration")
        self.ModuleCodec = params.get("ModuleCodec")
        self.Bitrate = params.get("Bitrate")
        self.Type = params.get("Type")
        self.PushDomain = params.get("PushDomain")


class UnBindLiveDomainCertRequest(AbstractModel):
    """UnBindLiveDomainCert請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 播放域名。
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")


class UnBindLiveDomainCertResponse(AbstractModel):
    """UnBindLiveDomainCert返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateLiveWatermarkRequest(AbstractModel):
    """UpdateLiveWatermark請求參數結構體

    """

    def __init__(self):
        """
        :param WatermarkId: 浮水印ID。
        :type WatermarkId: int
        :param PictureUrl: 浮水印圖片url。
        :type PictureUrl: str
        :param XPosition: 顯示位置，X軸偏移。
        :type XPosition: int
        :param YPosition: 顯示位置，Y軸偏移。
        :type YPosition: int
        :param WatermarkName: 浮水印名稱。
        :type WatermarkName: str
        :param Width: 浮水印寬度，占直播原始畫面寬度百分比，建議高寬只設置一項，另外一項會自适應縮放，避免變形。
        :type Width: int
        :param Height: 浮水印高度，占直播原始畫面寬度百分比，建議高寬只設置一項，另外一項會自适應縮放，避免變形。
        :type Height: int
        """
        self.WatermarkId = None
        self.PictureUrl = None
        self.XPosition = None
        self.YPosition = None
        self.WatermarkName = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")
        self.PictureUrl = params.get("PictureUrl")
        self.XPosition = params.get("XPosition")
        self.YPosition = params.get("YPosition")
        self.WatermarkName = params.get("WatermarkName")
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class UpdateLiveWatermarkResponse(AbstractModel):
    """UpdateLiveWatermark返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class WatermarkInfo(AbstractModel):
    """浮水印訊息

    """

    def __init__(self):
        """
        :param WatermarkId: 浮水印ID。
        :type WatermarkId: int
        :param PictureUrl: 浮水印圖片url。
        :type PictureUrl: str
        :param XPosition: 顯示位置，X軸偏移。
        :type XPosition: int
        :param YPosition: 顯示位置，Y軸偏移。
        :type YPosition: int
        :param WatermarkName: 浮水印名稱。
        :type WatermarkName: str
        :param Status: 當前狀态。0：未使用，1:使用中。
        :type Status: int
        :param CreateTime: 添加時間。
        :type CreateTime: str
        :param Width: 浮水印寬
        :type Width: int
        :param Height: 浮水印高
        :type Height: int
        """
        self.WatermarkId = None
        self.PictureUrl = None
        self.XPosition = None
        self.YPosition = None
        self.WatermarkName = None
        self.Status = None
        self.CreateTime = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")
        self.PictureUrl = params.get("PictureUrl")
        self.XPosition = params.get("XPosition")
        self.YPosition = params.get("YPosition")
        self.WatermarkName = params.get("WatermarkName")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.Width = params.get("Width")
        self.Height = params.get("Height")