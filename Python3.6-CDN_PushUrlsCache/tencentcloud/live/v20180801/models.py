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


class AddDelayLiveStreamRequest(AbstractModel):
    """AddDelayLiveStream請求參數結構體

    """

    def __init__(self):
        """
        :param AppName: 推流路徑，與推流和播放網址中的 AppName 保持一緻，預設爲 live。
        :type AppName: str
        :param DomainName: 推流域名。
        :type DomainName: str
        :param StreamName: 流名稱。
        :type StreamName: str
        :param DelayTime: 延播時間，單位：秒，上限：600秒。
        :type DelayTime: int
        :param ExpireTime: 延播設置的過期時間。UTC 格式，例如：2018-11-29T19:00:00Z。
注意：
1. 預設7天後過期，且最長支援7天内生效。
2. 北京時間值爲 UTC 時間值 + 8 小時，格式按照 ISO 8601 标準表示，詳見 [ISO 日期格式說明](https://cloud.tencent.com/document/product/266/11732#I)。
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
預設值：1。
        :type PlayType: int
        :param IsDelayLive: 是否是慢直播：
0： 普通直播，
1 ：慢直播 。
預設值： 0。
        :type IsDelayLive: int
        :param IsMiniProgramLive: 是否是小程式直播：
0： 标準直播，
1 ：小程式直播 。
預設值： 0。
        :type IsMiniProgramLive: int
        """
        self.DomainName = None
        self.DomainType = None
        self.PlayType = None
        self.IsDelayLive = None
        self.IsMiniProgramLive = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.DomainType = params.get("DomainType")
        self.PlayType = params.get("PlayType")
        self.IsDelayLive = params.get("IsDelayLive")
        self.IsMiniProgramLive = params.get("IsMiniProgramLive")


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
        :param PictureUrl: 浮水印圖片 URL。
        :type PictureUrl: str
        :param WatermarkName: 浮水印名稱。
        :type WatermarkName: str
        :param XPosition: 顯示位置，X軸偏移，預設 0。
        :type XPosition: int
        :param YPosition: 顯示位置，Y軸偏移，預設 0。
        :type YPosition: int
        :param Width: 浮水印寬度，占直播原始畫面寬度百分比，建議高寬只設置一項，另外一項會自适應縮放，避免變形。預設原始寬度。
        :type Width: int
        :param Height: 浮水印高度，占直播原始畫面寬度百分比，建議高寬只設置一項，另外一項會自适應縮放，避免變形。預設原始高度。
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


class BillDataInfo(AbstractModel):
    """頻寬和流量訊息。

    """

    def __init__(self):
        """
        :param Time: 時間點，格式: yyyy-mm-dd HH:MM:SS。
        :type Time: str
        :param Bandwidth: 頻寬，單位是 Mbps。
        :type Bandwidth: float
        :param Flux: 流量，單位是 MB。
        :type Flux: float
        :param PeakTime: 峰值時間點，格式: yyyy-mm-dd HH:MM:SS，原始數據爲5分鍾粒度，如果查詢小時和天粒度數據，則返回對應粒度内的頻寬峰值時間點。
        :type PeakTime: str
        """
        self.Time = None
        self.Bandwidth = None
        self.Flux = None
        self.PeakTime = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Bandwidth = params.get("Bandwidth")
        self.Flux = params.get("Flux")
        self.PeakTime = params.get("PeakTime")


class BindLiveDomainCertRequest(AbstractModel):
    """BindLiveDomainCert請求參數結構體

    """

    def __init__(self):
        """
        :param CertId: 證書Id。使用添加證書介面獲驗證書Id。
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
        :param TemplateId: 範本 ID。
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
    """回調範本訊息。

    """

    def __init__(self):
        """
        :param TemplateId: 範本 ID。
        :type TemplateId: int
        :param TemplateName: 範本名稱。
        :type TemplateName: str
        :param Description: 描述訊息。
        :type Description: str
        :param StreamBeginNotifyUrl: 開播回調 URL。
        :type StreamBeginNotifyUrl: str
        :param StreamEndNotifyUrl: 斷流回調 URL。
        :type StreamEndNotifyUrl: str
        :param StreamMixNotifyUrl: 混流回調 URL。
        :type StreamMixNotifyUrl: str
        :param RecordNotifyUrl: 錄制回調 URL。
        :type RecordNotifyUrl: str
        :param SnapshotNotifyUrl: 截圖回調 URL。
        :type SnapshotNotifyUrl: str
        :param PornCensorshipNotifyUrl: 鑒黃回調 URL。
        :type PornCensorshipNotifyUrl: str
        :param CallbackKey: 回調的鑒權 key。
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


class CancelCommonMixStreamRequest(AbstractModel):
    """CancelCommonMixStream請求參數結構體

    """

    def __init__(self):
        """
        :param MixStreamSessionId: 混流會話（申請混流開始到取消混流結束）标識 ID。
        :type MixStreamSessionId: str
        """
        self.MixStreamSessionId = None


    def _deserialize(self, params):
        self.MixStreamSessionId = params.get("MixStreamSessionId")


class CancelCommonMixStreamResponse(AbstractModel):
    """CancelCommonMixStream返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CdnPlayStatData(AbstractModel):
    """下行播放統計指标

    """

    def __init__(self):
        """
        :param Time: 時間點，格式: yyyy-mm-dd HH:MM:SS。
        :type Time: str
        :param Bandwidth: 頻寬，單位: Mbps。
        :type Bandwidth: float
        :param Flux: 流量，單位: MB。
        :type Flux: float
        :param Request: 新增請求數。
        :type Request: int
        :param Online: 并發連接數。
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


class CertInfo(AbstractModel):
    """證書訊息。

    """

    def __init__(self):
        """
        :param CertId: 證書 ID。
        :type CertId: int
        :param CertName: 證書名稱。
        :type CertName: str
        :param Description: 描述訊息。
        :type Description: str
        :param CreateTime: 創建時間，UTC 格式。
        :type CreateTime: str
        :param HttpsCrt: 證書内容。
        :type HttpsCrt: str
        :param CertType: 證書類型:
0：Top Cloud 托管證書。
1：用戶添加證書。
        :type CertType: int
        :param CertExpireTime: 證書過期時間，UTC 格式。
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


class ClientIpPlaySumInfo(AbstractModel):
    """用戶端ip播放匯總訊息。

    """

    def __init__(self):
        """
        :param ClientIp: 用戶端 IP，點分型。
        :type ClientIp: str
        :param Province: 用戶端所在省份。
        :type Province: str
        :param TotalFlux: 總流量。
        :type TotalFlux: float
        :param TotalRequest: 總請求數。
        :type TotalRequest: int
        :param TotalFailedRequest: 總失敗請求數。
        :type TotalFailedRequest: int
        :param CountryArea: 用戶端所在國家。
        :type CountryArea: str
        """
        self.ClientIp = None
        self.Province = None
        self.TotalFlux = None
        self.TotalRequest = None
        self.TotalFailedRequest = None
        self.CountryArea = None


    def _deserialize(self, params):
        self.ClientIp = params.get("ClientIp")
        self.Province = params.get("Province")
        self.TotalFlux = params.get("TotalFlux")
        self.TotalRequest = params.get("TotalRequest")
        self.TotalFailedRequest = params.get("TotalFailedRequest")
        self.CountryArea = params.get("CountryArea")


class CommonMixControlParams(AbstractModel):
    """通用混流控制參數

    """

    def __init__(self):
        """
        :param UseMixCropCenter: 取值範圍[0,1]。
填1時，當參數中圖層分辨率參數與視訊實際分辨率不一緻時，自動從視訊中按圖層設置的分辨率比例進行裁剪。
        :type UseMixCropCenter: int
        """
        self.UseMixCropCenter = None


    def _deserialize(self, params):
        self.UseMixCropCenter = params.get("UseMixCropCenter")


class CommonMixCropParams(AbstractModel):
    """通用混流輸入裁剪參數。

    """

    def __init__(self):
        """
        :param CropWidth: 裁剪的寬度。取值範圍[0，3000]。
        :type CropWidth: float
        :param CropHeight: 裁剪的高度。取值範圍[0，3000]。
        :type CropHeight: float
        :param CropStartLocationX: 裁剪的起始X坐标。取值範圍[0，3000]。
        :type CropStartLocationX: float
        :param CropStartLocationY: 裁剪的起始Y坐标。取值範圍[0，3000]。
        :type CropStartLocationY: float
        """
        self.CropWidth = None
        self.CropHeight = None
        self.CropStartLocationX = None
        self.CropStartLocationY = None


    def _deserialize(self, params):
        self.CropWidth = params.get("CropWidth")
        self.CropHeight = params.get("CropHeight")
        self.CropStartLocationX = params.get("CropStartLocationX")
        self.CropStartLocationY = params.get("CropStartLocationY")


class CommonMixInputParam(AbstractModel):
    """通用混流輸入參數。

    """

    def __init__(self):
        """
        :param InputStreamName: 輸入流名稱。80位元以内，僅含字母、數字以及下劃線的字串。
        :type InputStreamName: str
        :param LayoutParams: 輸入流布局參數。
        :type LayoutParams: :class:`tencentcloud.live.v20180801.models.CommonMixLayoutParams`
        :param CropParams: 輸入流裁剪參數。
        :type CropParams: :class:`tencentcloud.live.v20180801.models.CommonMixCropParams`
        """
        self.InputStreamName = None
        self.LayoutParams = None
        self.CropParams = None


    def _deserialize(self, params):
        self.InputStreamName = params.get("InputStreamName")
        if params.get("LayoutParams") is not None:
            self.LayoutParams = CommonMixLayoutParams()
            self.LayoutParams._deserialize(params.get("LayoutParams"))
        if params.get("CropParams") is not None:
            self.CropParams = CommonMixCropParams()
            self.CropParams._deserialize(params.get("CropParams"))


class CommonMixLayoutParams(AbstractModel):
    """通用混流布局參數。

    """

    def __init__(self):
        """
        :param ImageLayer: 輸入圖層。取值範圍[1，16]。
1)背景流（即大主播畫面或畫布）的 image_layer 填1。
2)純音訊混流，該參數也需填。
        :type ImageLayer: int
        :param InputType: 輸入類型。取值範圍[0，5]。
不填預設爲0。
0表示輸入流爲影音。
2表示輸入流爲圖片。
3表示輸入流爲畫布。 
4表示輸入流爲音訊。
5表示輸入流爲純視訊。
        :type InputType: int
        :param ImageWidth: 輸入畫面在輸出時的寬度。取值範圍：
像素：[0，3000]
百分比：[0.01，0.99]
不填預設爲輸入流的寬度。
使用百分比時，期望輸出爲（百分比 * 背景寬）。
        :type ImageWidth: float
        :param ImageHeight: 輸入畫面在輸出時的高度。取值範圍：
像素：[0，3000]
百分比：[0.01，0.99]
不填預設爲輸入流的高度。
使用百分比時，期望輸出爲（百分比 * 背景高）。
        :type ImageHeight: float
        :param LocationX: 輸入在輸出畫面的X偏移。取值範圍：
像素：[0，3000]
百分比：[0.01，0.99]
不填預設爲0。
相對于大主播背景畫面左上角的橫向偏移。 
使用百分比時，期望輸出爲（百分比 * 背景寬）。
        :type LocationX: float
        :param LocationY: 輸入在輸出畫面的Y偏移。取值範圍：
像素：[0，3000]
百分比：[0.01，0.99]
不填預設爲0。
相對于大主播背景畫面左上角的縱向偏移。 
使用百分比時，期望輸出爲（百分比 * 背景寬）
        :type LocationY: float
        :param Color: 當InputType爲3(畫布)時，該值表示畫布的顔色。
常用的顔色有：
紅色：0xcc0033。
黃色：0xcc9900。
綠色：0xcccc33。
藍色：0x99CCFF。
黑色：0x000000。
白色：0xFFFFFF。
灰色：0x999999。
        :type Color: str
        :param WatermarkId: 當InputType爲2(圖片)時，該值是浮水印ID。
        :type WatermarkId: int
        """
        self.ImageLayer = None
        self.InputType = None
        self.ImageWidth = None
        self.ImageHeight = None
        self.LocationX = None
        self.LocationY = None
        self.Color = None
        self.WatermarkId = None


    def _deserialize(self, params):
        self.ImageLayer = params.get("ImageLayer")
        self.InputType = params.get("InputType")
        self.ImageWidth = params.get("ImageWidth")
        self.ImageHeight = params.get("ImageHeight")
        self.LocationX = params.get("LocationX")
        self.LocationY = params.get("LocationY")
        self.Color = params.get("Color")
        self.WatermarkId = params.get("WatermarkId")


class CommonMixOutputParams(AbstractModel):
    """通用混流輸出參數。

    """

    def __init__(self):
        """
        :param OutputStreamName: 輸出流名稱。
        :type OutputStreamName: str
        :param OutputStreamType: 輸出流類型，取值範圍[0,1]。
不填預設爲0。
當輸出流爲輸入流 list 中的一條時，填寫0。
當期望生成的混流結果成爲一條新流時，該值填爲1。
該值爲1時，output_stream_id 不能出現在 input_stram_list 中，且直播後台中，不能存在相同 ID 的流。
        :type OutputStreamType: int
        :param OutputStreamBitRate: 輸出流比特率。取值範圍[1，50000]。
不填的情況下，系統會自動判斷。
        :type OutputStreamBitRate: int
        :param OutputStreamGop: 輸出流GOP大小。取值範圍[1,10]。
不填的情況下，系統會自動判斷。
        :type OutputStreamGop: int
        :param OutputStreamFrameRate: 輸出流幀率大小。取值範圍[1,60]。
不填的情況下，系統會自動判斷。
        :type OutputStreamFrameRate: int
        :param OutputAudioBitRate: 輸出流音訊比特率。取值範圍[1,500]
不填的情況下，系統會自動判斷。
        :type OutputAudioBitRate: int
        :param OutputAudioSampleRate: 輸出流音訊采樣率。取值範圍[96000, 88200, 64000, 48000, 44100, 32000,24000, 22050, 16000, 12000, 11025, 8000]。
不填的情況下，系統會自動判斷。
        :type OutputAudioSampleRate: int
        :param OutputAudioChannels: 輸出流音訊聲道數。取值範圍[1,2]。
不填的情況下，系統會自動判斷。
        :type OutputAudioChannels: int
        :param MixSei: 輸出流中的sei訊息。如果無特殊需要，不填。
        :type MixSei: str
        """
        self.OutputStreamName = None
        self.OutputStreamType = None
        self.OutputStreamBitRate = None
        self.OutputStreamGop = None
        self.OutputStreamFrameRate = None
        self.OutputAudioBitRate = None
        self.OutputAudioSampleRate = None
        self.OutputAudioChannels = None
        self.MixSei = None


    def _deserialize(self, params):
        self.OutputStreamName = params.get("OutputStreamName")
        self.OutputStreamType = params.get("OutputStreamType")
        self.OutputStreamBitRate = params.get("OutputStreamBitRate")
        self.OutputStreamGop = params.get("OutputStreamGop")
        self.OutputStreamFrameRate = params.get("OutputStreamFrameRate")
        self.OutputAudioBitRate = params.get("OutputAudioBitRate")
        self.OutputAudioSampleRate = params.get("OutputAudioSampleRate")
        self.OutputAudioChannels = params.get("OutputAudioChannels")
        self.MixSei = params.get("MixSei")


class ConcurrentRecordStreamNum(AbstractModel):
    """并發錄制路數

    """

    def __init__(self):
        """
        :param Time: 時間點。
        :type Time: str
        :param Num: 路數。
        :type Num: int
        """
        self.Time = None
        self.Num = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Num = params.get("Num")


class CreateCommonMixStreamRequest(AbstractModel):
    """CreateCommonMixStream請求參數結構體

    """

    def __init__(self):
        """
        :param MixStreamSessionId: 混流會話（申請混流開始到取消混流結束）标識 ID。
        :type MixStreamSessionId: str
        :param InputStreamList: 混流輸入流清單。
        :type InputStreamList: list of CommonMixInputParam
        :param OutputParams: 混流輸出流參數。
        :type OutputParams: :class:`tencentcloud.live.v20180801.models.CommonMixOutputParams`
        :param MixStreamTemplateId: 輸入範本 ID，若設置該參數，将按預設範本布局輸出，無需填入自定義位置參數。
不填預設爲0。
兩輸入源支援10，20，30，40，50。
三輸入源支援310，390，391。
四輸入源支援410。
五輸入源支援510，590。
六輸入源支援610。
        :type MixStreamTemplateId: int
        :param ControlParams: 混流的特殊控制參數。如無特殊需求，無需填寫。
        :type ControlParams: :class:`tencentcloud.live.v20180801.models.CommonMixControlParams`
        """
        self.MixStreamSessionId = None
        self.InputStreamList = None
        self.OutputParams = None
        self.MixStreamTemplateId = None
        self.ControlParams = None


    def _deserialize(self, params):
        self.MixStreamSessionId = params.get("MixStreamSessionId")
        if params.get("InputStreamList") is not None:
            self.InputStreamList = []
            for item in params.get("InputStreamList"):
                obj = CommonMixInputParam()
                obj._deserialize(item)
                self.InputStreamList.append(obj)
        if params.get("OutputParams") is not None:
            self.OutputParams = CommonMixOutputParams()
            self.OutputParams._deserialize(params.get("OutputParams"))
        self.MixStreamTemplateId = params.get("MixStreamTemplateId")
        if params.get("ControlParams") is not None:
            self.ControlParams = CommonMixControlParams()
            self.ControlParams._deserialize(params.get("ControlParams"))


class CreateCommonMixStreamResponse(AbstractModel):
    """CreateCommonMixStream返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


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
        :param TemplateName: 範本名稱。
長度上限：255位元。
僅支援中文、英文、數字、_、-。
        :type TemplateName: str
        :param Description: 描述訊息。
長度上限：1024位元。
僅支援中文、英文、數字、_、-。
        :type Description: str
        :param StreamBeginNotifyUrl: 開播回調 URL，
相關協議文件：[事件訊息通知](/document/product/267/32744)。
        :type StreamBeginNotifyUrl: str
        :param StreamEndNotifyUrl: 斷流回調 URL，
相關協議文件：[事件訊息通知](/document/product/267/32744)。
        :type StreamEndNotifyUrl: str
        :param RecordNotifyUrl: 錄制回調 URL，
相關協議文件：[事件訊息通知](/document/product/267/32744)。
        :type RecordNotifyUrl: str
        :param SnapshotNotifyUrl: 截圖回調 URL，
相關協議文件：[事件訊息通知](/document/product/267/32744)。
        :type SnapshotNotifyUrl: str
        :param PornCensorshipNotifyUrl: 鑒黃回調 URL，
相關協議文件：[事件訊息通知](/document/product/267/32741)。
        :type PornCensorshipNotifyUrl: str
        :param CallbackKey: 回調 Key，回調 URL 公用，回調簽名詳見事件訊息通知文件。
[事件訊息通知](/document/product/267/32744)。
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
注意：當證書類型爲0時，HttpsCrt和HttpsKey必選；
當證書類型爲1時，優先使用CloudCertId對應證書，若CloudCertId爲空則使用HttpsCrt和HttpsKey。
        :type CertType: int
        :param CertName: 證書名稱。
        :type CertName: str
        :param HttpsCrt: 證書内容，即公鑰。
        :type HttpsCrt: str
        :param HttpsKey: 私鑰。
        :type HttpsKey: str
        :param Description: 描述。
        :type Description: str
        :param CloudCertId: Top Cloud 證書托管ID。
        :type CloudCertId: str
        """
        self.CertType = None
        self.CertName = None
        self.HttpsCrt = None
        self.HttpsKey = None
        self.Description = None
        self.CloudCertId = None


    def _deserialize(self, params):
        self.CertType = params.get("CertType")
        self.CertName = params.get("CertName")
        self.HttpsCrt = params.get("HttpsCrt")
        self.HttpsKey = params.get("HttpsKey")
        self.Description = params.get("Description")
        self.CloudCertId = params.get("CloudCertId")


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
        :param AppName: 推流路徑，與推流和播放網址中的 AppName保持一緻，預設爲 live。
        :type AppName: str
        :param DomainName: 推流域名。多域名推流必須設置。
        :type DomainName: str
        :param StartTime: 錄制開始時間。中國标準時間，需要 URLEncode(rfc3986)。如 2017-01-01 10:10:01，編碼爲：2017-01-01+10%3a10%3a01。
定時錄制模式，必須設置該欄位；實時視訊錄制模式，忽略該欄位。
        :type StartTime: str
        :param EndTime: 錄制結束時間。中國标準時間，需要 URLEncode(rfc3986)。如 2017-01-01 10:30:01，編碼爲：2017-01-01+10%3a30%3a01。
定時錄制模式，必須設置該欄位；實時錄制模式，爲可選欄位。如果通過Highlight參數，設置錄制爲實時視訊錄制模式，其設置的結束時間不應超過當前時間+30分鍾，如果設置的結束時間超過當前時間+30分鍾或者小於當前時間或者不設置該參數，則實際結束時間爲當前時間+30分鍾。
        :type EndTime: str
        :param RecordType: 錄制類型。
“video” : 影音錄制【預設】。
“audio” : 純音訊錄制。
在定時錄制模式或實時視訊錄制模式下，該參數均有效，不區分大小寫。
        :type RecordType: str
        :param FileFormat: 錄制文件格式。其值爲：
“flv”【預設】,“hls”,”mp4”,“aac”,”mp3”。
在定時錄制模式或實時視訊錄制模式下，該參數均有效，不區分大小寫。
        :type FileFormat: str
        :param Highlight: 開啓實時視訊錄制模式标志。
0：不開啓實時視訊錄制模式，即定時錄制模式【預設】。見[範例一](#.E7.A4.BA.E4.BE.8B1-.E5.88.9B.E5.BB.BA.E5.AE.9A.E6.97.B6.E5.BD.95.E5.88.B6.E4.BB.BB.E5.8A.A1)。
1：開啓實時視訊錄制模式。見[範例二](#.E7.A4.BA.E4.BE.8B2-.E5.88.9B.E5.BB.BA.E5.AE.9E.E6.97.B6.E5.BD.95.E5.88.B6.E4.BB.BB.E5.8A.A1)。
        :type Highlight: int
        :param MixStream: 開啓 A+B=C混流C流錄制标志。
0：不開啓 A+B=C混流C流錄制【預設】。
1：開啓 A+B=C混流C流錄制。
在定時錄制模式或實時視訊錄制模式下，該參數均有效。
        :type MixStream: int
        :param StreamParam: 錄制流參數。當前支援以下參數：
record_interval - 錄制分片時長，單位 秒，1800 - 7200。
storage_time - 錄制文件儲存時長，單位 秒。
eg. record_interval=3600&storage_time=2592000。
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
        :param TaskId: 任務 ID，全局唯一标識錄制任務。
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
        :param TemplateId: 範本 ID。
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
        :param TemplateName: 範本名。僅支援中文、英文、數字、_、-。
        :type TemplateName: str
        :param Description: 描述訊息。
        :type Description: str
        :param FlvParam: Flv錄制參數，開啓Flv錄制時設置。
        :type FlvParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param HlsParam: Hls錄制參數，開啓hls錄制時設置。
        :type HlsParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param Mp4Param: Mp4錄制參數，開啓Mp4錄制時設置。
        :type Mp4Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param AacParam: Aac錄制參數，開啓Aac錄制時設置。
        :type AacParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param IsDelayLive: 直播類型，預設 0。
0：普通直播，
1：慢直播。
        :type IsDelayLive: int
        :param HlsSpecialParam: HLS專屬錄制參數。
        :type HlsSpecialParam: :class:`tencentcloud.live.v20180801.models.HlsSpecialParam`
        :param Mp3Param: Mp3錄制參數，開啓Mp3錄制時設置。
        :type Mp3Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        """
        self.TemplateName = None
        self.Description = None
        self.FlvParam = None
        self.HlsParam = None
        self.Mp4Param = None
        self.AacParam = None
        self.IsDelayLive = None
        self.HlsSpecialParam = None
        self.Mp3Param = None


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
        if params.get("Mp3Param") is not None:
            self.Mp3Param = RecordParam()
            self.Mp3Param._deserialize(params.get("Mp3Param"))


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
        :param TemplateId: 範本 ID。
        :type TemplateId: int
        :param AppName: 推流路徑，與推流和播放網址中的 AppName 保持一緻，預設爲 live。
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
        :param TemplateName: 範本名稱。
長度上限：255位元。
僅支援中文、英文、數字、_、-。
        :type TemplateName: str
        :param CosAppId: Cos 應用 ID。
        :type CosAppId: int
        :param CosBucket: Cos Bucket名稱。
        :type CosBucket: str
        :param CosRegion: Cos地區。
        :type CosRegion: str
        :param Description: 描述訊息。
長度上限：1024位元。
僅支援中文、英文、數字、_、-。
        :type Description: str
        :param SnapshotInterval: 截圖間隔，單位s，預設10s。
範圍： 5s ~ 600s。
        :type SnapshotInterval: int
        :param Width: 截圖寬度。預設：0（原始寬）。
        :type Width: int
        :param Height: 截圖高度。預設：0（原始高）。
        :type Height: int
        :param PornFlag: 是否開啓鑒黃，0：不開啓，1：開啓。預設：0。
        :type PornFlag: int
        :param CosPrefix: Cos Bucket文件夾前綴。
        :type CosPrefix: str
        :param CosFileName: Cos 文件名稱。
        :type CosFileName: str
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
        self.CosPrefix = None
        self.CosFileName = None


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
        self.CosPrefix = params.get("CosPrefix")
        self.CosFileName = params.get("CosFileName")


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
        :param AppName: 推流路徑，與推流和播放網址中的AppName保持一緻。如果只綁定域名，則此處填空。
        :type AppName: str
        :param StreamName: 流名稱。如果只綁定域名或路徑，則此處填空。
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
注意：碼率必須是100的倍數。
        :type VideoBitrate: int
        :param Vcodec: 視訊編碼：h264/h265，預設h264。
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
        :param AiTransCode: 是否是極速高清範本，0：否，1：是。預設0。
        :type AiTransCode: int
        :param AdaptBitratePercent: 極速高清相比VideoBitrate少多少碼率，0.1到0.5
        :type AdaptBitratePercent: float
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
        self.AiTransCode = None
        self.AdaptBitratePercent = None


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
        self.AiTransCode = params.get("AiTransCode")
        self.AdaptBitratePercent = params.get("AdaptBitratePercent")


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
        :param FromUrl: 源 Url ，用于拉流的網址。目前可支援直播流及點播文件。
注意：
1. 多個點播url之間使用空格拼接。
2. 目前上限支援10個url。
3. 支援拉流文件格式：flv，rtmp，hls，mp4。
        :type FromUrl: str
        :param ToUrl: 目的 Url ，用于推流的網址，目前限制該目标網址爲騰訊域名。
僅支援：rtmp 協議。
        :type ToUrl: str
        :param AreaId: 選擇完成轉拉推的服務所在區域:
1-深圳，
2-上海，
3-天津，
4-中國香港。
        :type AreaId: int
        :param IspId: 選擇完成轉拉推服務使用的運營商網絡：
1-電信，
2-移動，
3-聯通，
4-其他。
注：AreaId 爲4的時候，IspId 只能爲其他。
        :type IspId: int
        :param StartTime: 開始時間。
使用 UTC 格式時間，
例如：2019-01-08T10:00:00Z。
注意：北京時間值爲 UTC 時間值 + 8 小時，格式按照 ISO 8601 标準表示，詳見 [ISO 日期格式說明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type StartTime: str
        :param EndTime: 結束時間，注意：
1. 結束時間必須大于開始時間；
2. 結束時間和開始時間必須大于當前時間；
3. 結束時間 和 開始時間 間隔必須小於七天。
使用 UTC 格式時間，
例如：2019-01-08T10:00:00Z。
注意：北京時間值爲 UTC 時間值 + 8 小時，格式按照 ISO 8601 标準表示，詳見 [ISO 日期格式說明](https://cloud.tencent.com/document/product/266/11732#I)。
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
        :param ConfigId: 配置成功後的 ID。
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


class DelayInfo(AbstractModel):
    """延播訊息。

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路徑，與推流和播放網址中的 
 AppName 保持一緻，預設爲 live。
        :type AppName: str
        :param StreamName: 流名稱。
        :type StreamName: str
        :param DelayInterval: 延播時間，單位：秒。
        :type DelayInterval: int
        :param CreateTime: 創建時間，UTC 時間。
注意：UTC時間和北京時間相差8小時。
例如：2019-06-18T12:00:00Z（爲北京時間 2019 年 6 月 18 日 20 點 0 分 0 秒）。
        :type CreateTime: str
        :param ExpireTime: 過期時間，UTC 時間。
注意：UTC時間和北京時間相差8小時。
例如：2019-06-18T12:00:00Z（爲北京時間 2019 年 6 月 18 日 20 點 0 分 0 秒）。
        :type ExpireTime: str
        :param Status: 當前狀态:
-1：已過期。
1： 生效中。
        :type Status: int
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None
        self.DelayInterval = None
        self.CreateTime = None
        self.ExpireTime = None
        self.Status = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        self.DelayInterval = params.get("DelayInterval")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.Status = params.get("Status")


class DeleteLiveCallbackRuleRequest(AbstractModel):
    """DeleteLiveCallbackRule請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。
        :type DomainName: str
        :param AppName: 推流路徑，與推流和播放網址中的 AppName 保持一緻，預設爲 live。
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
        :param TemplateId: 範本 ID。
1. 在創建回調範本介面 [CreateLiveCallbackTemplate](/document/product/267/32637) 調用的返回值中獲取範本 ID。
2. 可以從介面 [DescribeLiveCallbackTemplates](/document/product/267/32632) 查詢已經創建的過的範本清單。
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
        :param TaskId: 任務ID，全局唯一标識錄制任務。
從介面 [CreateLiveRecord](/document/product/267/30148) 的返回值中獲取TaskId。
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
域名+AppName+StreamName唯一标識單個轉碼規則，如需删除需要強比對，例如AppName爲空也需要傳空字串進行強比對。
        :type DomainName: str
        :param AppName: 推流路徑，與推流和播放網址中的AppName保持一緻，預設爲 live。
域名+AppName+StreamName唯一标識單個轉碼規則，如需删除需要強比對，例如AppName爲空也需要傳空字串進行強比對。
        :type AppName: str
        :param StreamName: 流名稱。
域名+AppName+StreamName唯一标識單個轉碼規則，如需删除需要強比對，例如AppName爲空也需要傳空字串進行強比對。
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
        :param TemplateId: 範本 ID。
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
        :param AppName: 推流路徑，與推流和播放網址中的 AppName 保持一緻，預設爲 live。
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
        :param TemplateId: 範本 ID。
1. 在創建截圖範本介面 [CreateLiveSnapshotTemplate](/document/product/267/32624) 調用的返回值中獲取。
2. 可以從介面 [DescribeLiveSnapshotTemplates](/document/product/267/32619) 中查詢已創建的截圖範本清單。
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
        :param DomainName: 播放域名。
        :type DomainName: str
        :param AppName: 推流路徑，與推流和播放網址中的AppName保持一緻，預設爲 live。
        :type AppName: str
        :param StreamName: 流名稱。
        :type StreamName: str
        :param TemplateId: 範本ID。
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
        :param TemplateId: 範本 ID。
1. 在創建轉碼範本介面 [CreateLiveTranscodeTemplate](/document/product/267/32646) 調用的返回值中獲取範本 ID。
2. 可以從介面 [DescribeLiveTranscodeTemplates](/document/product/267/32641) 查詢已經創建的過的範本清單。
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
        :param WatermarkId: 浮水印 ID。
在添加浮水印介面 [AddLiveWatermark](/document/product/267/30154) 調用返回值中獲取水印 ID。
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
        :param AppName: 推流路徑。與推流和播放網址中的 AppName 保持一緻，預設爲live。
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
        :param ConfigId: 配置 ID。
1. 在添加拉流配置介面 [CreatePullStreamConfig](/document/api/267/30159) 調用返回值中獲取配置 ID。
2. 可以從介面 [DescribePullStreamConfigs](/document/api/267/30158) 中查詢已創建過的拉流配置清單。
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


class DescribeAllStreamPlayInfoListRequest(AbstractModel):
    """DescribeAllStreamPlayInfoList請求參數結構體

    """

    def __init__(self):
        """
        :param QueryTime: 查詢時間點，精确到分鍾粒度，支援最近1個月的數據查詢，數據延遲爲5分鍾左右，如果要查詢實時的數據，建議傳遞5分鍾前的時間點，格式爲yyyy-mm-dd HH:MM:SS。
        :type QueryTime: str
        """
        self.QueryTime = None


    def _deserialize(self, params):
        self.QueryTime = params.get("QueryTime")


class DescribeAllStreamPlayInfoListResponse(AbstractModel):
    """DescribeAllStreamPlayInfoList返回參數結構體

    """

    def __init__(self):
        """
        :param QueryTime: 查詢時間點，回傳的輸入參數中的查詢時間。
        :type QueryTime: str
        :param DataInfoList: 數據訊息清單。
        :type DataInfoList: list of MonitorStreamPlayInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.QueryTime = None
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.QueryTime = params.get("QueryTime")
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = MonitorStreamPlayInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBillBandwidthAndFluxListRequest(AbstractModel):
    """DescribeBillBandwidthAndFluxList請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 起始時間點，格式爲yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param EndTime: 結束時間點，格式爲yyyy-mm-dd HH:MM:SS，起始和結束時間跨度不支援超過31天。
        :type EndTime: str
        :param PlayDomains: 直播播放域名，若不填，表示總體數據。
        :type PlayDomains: list of str
        :param MainlandOrOversea: 可選值：
Mainland：查詢國内數據，
Oversea：則查詢國外數據，
預設：查詢國内+國外的數據。
注：LEB（快直播）只支援國内+國外數據查詢。
        :type MainlandOrOversea: str
        :param Granularity: 數據粒度，支援如下粒度：
5：5分鍾粒度，（跨度不支援超過1天），
60：1小時粒度（跨度不支援超過一個月），
1440：天粒度（跨度不支援超過一個月）。
預設值：5。
        :type Granularity: int
        :param ServiceName: 服務名稱，可選值包括LVB(标準直播)，LEB(快直播)，預設值是LVB。
        :type ServiceName: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PlayDomains = None
        self.MainlandOrOversea = None
        self.Granularity = None
        self.ServiceName = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PlayDomains = params.get("PlayDomains")
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        self.Granularity = params.get("Granularity")
        self.ServiceName = params.get("ServiceName")


class DescribeBillBandwidthAndFluxListResponse(AbstractModel):
    """DescribeBillBandwidthAndFluxList返回參數結構體

    """

    def __init__(self):
        """
        :param PeakBandwidthTime: 峰值頻寬所在時間點，格式爲yyyy-mm-dd HH:MM:SS。
        :type PeakBandwidthTime: str
        :param PeakBandwidth: 峰值頻寬，單位是Mbps。
        :type PeakBandwidth: float
        :param P95PeakBandwidthTime: 95峰值頻寬所在時間點，格式爲yyyy-mm-dd HH:MM:SS。
        :type P95PeakBandwidthTime: str
        :param P95PeakBandwidth: 95峰值頻寬，單位是Mbps。
        :type P95PeakBandwidth: float
        :param SumFlux: 總流量，單位是MB。
        :type SumFlux: float
        :param DataInfoList: 明細數據訊息。
        :type DataInfoList: list of BillDataInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PeakBandwidthTime = None
        self.PeakBandwidth = None
        self.P95PeakBandwidthTime = None
        self.P95PeakBandwidth = None
        self.SumFlux = None
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PeakBandwidthTime = params.get("PeakBandwidthTime")
        self.PeakBandwidth = params.get("PeakBandwidth")
        self.P95PeakBandwidthTime = params.get("P95PeakBandwidthTime")
        self.P95PeakBandwidth = params.get("P95PeakBandwidth")
        self.SumFlux = params.get("SumFlux")
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = BillDataInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeConcurrentRecordStreamNumRequest(AbstractModel):
    """DescribeConcurrentRecordStreamNum請求參數結構體

    """

    def __init__(self):
        """
        :param LiveType: 直播類型，SlowLive：慢直播。
NormalLive：普通直播。
        :type LiveType: str
        :param StartTime: 起始時間，格式：yyyy-mm-dd HH:MM:SS。
可以查詢最近180天的數據。
        :type StartTime: str
        :param EndTime: 結束時間，格式：yyyy-mm-dd HH:MM:SS。
時間跨度最大支援31天。
        :type EndTime: str
        :param MainlandOrOversea: 如果爲空，查詢所有地區數據；如果爲“Mainland”，查詢國内數據；如果爲“Oversea”，則查詢國外數據。
        :type MainlandOrOversea: str
        :param PushDomains: 推流域名清單，不填表示總體數據。
        :type PushDomains: list of str
        """
        self.LiveType = None
        self.StartTime = None
        self.EndTime = None
        self.MainlandOrOversea = None
        self.PushDomains = None


    def _deserialize(self, params):
        self.LiveType = params.get("LiveType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        self.PushDomains = params.get("PushDomains")


class DescribeConcurrentRecordStreamNumResponse(AbstractModel):
    """DescribeConcurrentRecordStreamNum返回參數結構體

    """

    def __init__(self):
        """
        :param DataInfoList: 統計訊息清單。
        :type DataInfoList: list of ConcurrentRecordStreamNum
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = ConcurrentRecordStreamNum()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeGroupProIspPlayInfoListRequest(AbstractModel):
    """DescribeGroupProIspPlayInfoList請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 起始時間點，格式爲yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param EndTime: 結束時間點，格式爲yyyy-mm-dd HH:MM:SS
時間跨度在（0,3小時]，支援最近1個月數據查詢。
        :type EndTime: str
        :param PlayDomains: 播放域名，預設爲不填，表示求總體數據。
        :type PlayDomains: list of str
        :param ProvinceNames: 省份清單，預設不填，則返回各省份的數據。
        :type ProvinceNames: list of str
        :param IspNames: 運營商清單，預設不填，則返回整個運營商的數據。
        :type IspNames: list of str
        :param MainlandOrOversea: 國内還是國外，如果爲空，查詢所有地區數據；如果爲“Mainland”，查詢國内數據；如果爲“Oversea”，則查詢國外數據。
        :type MainlandOrOversea: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PlayDomains = None
        self.ProvinceNames = None
        self.IspNames = None
        self.MainlandOrOversea = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PlayDomains = params.get("PlayDomains")
        self.ProvinceNames = params.get("ProvinceNames")
        self.IspNames = params.get("IspNames")
        self.MainlandOrOversea = params.get("MainlandOrOversea")


class DescribeGroupProIspPlayInfoListResponse(AbstractModel):
    """DescribeGroupProIspPlayInfoList返回參數結構體

    """

    def __init__(self):
        """
        :param DataInfoList: 數據内容。
        :type DataInfoList: list of GroupProIspDataInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = GroupProIspDataInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHttpStatusInfoListRequest(AbstractModel):
    """DescribeHttpStatusInfoList請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 起始時間，北京時間，
格式：yyyy-mm-dd HH:MM:SS。
StartTime不能爲3個月前。
        :type StartTime: str
        :param EndTime: 結束時間，北京時間，
格式：yyyy-mm-dd HH:MM:SS。
注：EndTime 和 StartTime 只支援最近1天的數據查詢。
        :type EndTime: str
        :param PlayDomains: 播放域名清單。
        :type PlayDomains: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.PlayDomains = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PlayDomains = params.get("PlayDomains")


class DescribeHttpStatusInfoListResponse(AbstractModel):
    """DescribeHttpStatusInfoList返回參數結構體

    """

    def __init__(self):
        """
        :param DataInfoList: 播放狀态碼清單。
        :type DataInfoList: list of HttpStatusData
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = HttpStatusData()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
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
        :param TemplateId: 範本 ID。
1. 在創建回調範本介面 [CreateLiveCallbackTemplate](/document/product/267/32637) 調用的返回值中獲取範本 ID。
2. 可以從介面 [DescribeLiveCallbackTemplates](/document/product/267/32632) 查詢已經創建的過的範本清單。
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
        :type Template: :class:`tencentcloud.live.v20180801.models.CallBackTemplateInfo`
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
        :type CertInfo: :class:`tencentcloud.live.v20180801.models.CertInfo`
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


class DescribeLiveDelayInfoListRequest(AbstractModel):
    """DescribeLiveDelayInfoList請求參數結構體

    """


class DescribeLiveDelayInfoListResponse(AbstractModel):
    """DescribeLiveDelayInfoList返回參數結構體

    """

    def __init__(self):
        """
        :param DelayInfoList: 延播訊息清單。
        :type DelayInfoList: list of DelayInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DelayInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DelayInfoList") is not None:
            self.DelayInfoList = []
            for item in params.get("DelayInfoList"):
                obj = DelayInfo()
                obj._deserialize(item)
                self.DelayInfoList.append(obj)
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
        :type DomainCertInfo: :class:`tencentcloud.live.v20180801.models.DomainCertInfo`
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


class DescribeLiveDomainPlayInfoListRequest(AbstractModel):
    """DescribeLiveDomainPlayInfoList請求參數結構體

    """

    def __init__(self):
        """
        :param PlayDomains: 播放域名清單。
        :type PlayDomains: list of str
        """
        self.PlayDomains = None


    def _deserialize(self, params):
        self.PlayDomains = params.get("PlayDomains")


class DescribeLiveDomainPlayInfoListResponse(AbstractModel):
    """DescribeLiveDomainPlayInfoList返回參數結構體

    """

    def __init__(self):
        """
        :param Time: 數據時間，格式爲yyyy-mm-dd HH:MM:SS。
        :type Time: str
        :param TotalBandwidth: 實時總頻寬。
        :type TotalBandwidth: float
        :param TotalFlux: 實時總流量。
        :type TotalFlux: float
        :param TotalRequest: 總請求數。
        :type TotalRequest: int
        :param TotalOnline: 實時總連接數。
        :type TotalOnline: int
        :param DomainInfoList: 分域名的數據情況。
        :type DomainInfoList: list of DomainInfoList
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Time = None
        self.TotalBandwidth = None
        self.TotalFlux = None
        self.TotalRequest = None
        self.TotalOnline = None
        self.DomainInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.TotalBandwidth = params.get("TotalBandwidth")
        self.TotalFlux = params.get("TotalFlux")
        self.TotalRequest = params.get("TotalRequest")
        self.TotalOnline = params.get("TotalOnline")
        if params.get("DomainInfoList") is not None:
            self.DomainInfoList = []
            for item in params.get("DomainInfoList"):
                obj = DomainInfoList()
                obj._deserialize(item)
                self.DomainInfoList.append(obj)
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
        :type DomainInfo: :class:`tencentcloud.live.v20180801.models.DomainInfo`
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
        :param DomainStatus: 域名狀态過濾。0-停用，1-啓用。
        :type DomainStatus: int
        :param DomainType: 域名類型過濾。0-推流，1-播放。
        :type DomainType: int
        :param PageSize: 分頁大小，範圍：10~100。預設10。
        :type PageSize: int
        :param PageNum: 取第幾頁，範圍：1~100000。預設1。
        :type PageNum: int
        :param IsDelayLive: 0 普通直播 1慢直播 預設0。
        :type IsDelayLive: int
        :param DomainPrefix: 域名前綴。
        :type DomainPrefix: str
        """
        self.DomainStatus = None
        self.DomainType = None
        self.PageSize = None
        self.PageNum = None
        self.IsDelayLive = None
        self.DomainPrefix = None


    def _deserialize(self, params):
        self.DomainStatus = params.get("DomainStatus")
        self.DomainType = params.get("DomainType")
        self.PageSize = params.get("PageSize")
        self.PageNum = params.get("PageNum")
        self.IsDelayLive = params.get("IsDelayLive")
        self.DomainPrefix = params.get("DomainPrefix")


class DescribeLiveDomainsResponse(AbstractModel):
    """DescribeLiveDomains返回參數結構體

    """

    def __init__(self):
        """
        :param AllCount: 總記錄數。
        :type AllCount: int
        :param DomainList: 域名詳細訊息清單。
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


class DescribeLivePackageInfoRequest(AbstractModel):
    """DescribeLivePackageInfo請求參數結構體

    """

    def __init__(self):
        """
        :param PackageType: 包類型，可選值：
0：流量包；
1：轉碼包。
        :type PackageType: int
        """
        self.PackageType = None


    def _deserialize(self, params):
        self.PackageType = params.get("PackageType")


class DescribeLivePackageInfoResponse(AbstractModel):
    """DescribeLivePackageInfo返回參數結構體

    """

    def __init__(self):
        """
        :param LivePackageInfoList: 套餐包訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type LivePackageInfoList: list of LivePackageInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.LivePackageInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LivePackageInfoList") is not None:
            self.LivePackageInfoList = []
            for item in params.get("LivePackageInfoList"):
                obj = LivePackageInfo()
                obj._deserialize(item)
                self.LivePackageInfoList.append(obj)
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
        :type PlayAuthKeyInfo: :class:`tencentcloud.live.v20180801.models.PlayAuthKeyInfo`
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
        :type PushAuthKeyInfo: :class:`tencentcloud.live.v20180801.models.PushAuthKeyInfo`
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
        :param TemplateId: 範本 ID。
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
        :type Template: :class:`tencentcloud.live.v20180801.models.RecordTemplateInfo`
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
        :param IsDelayLive: 是否屬于慢直播範本，預設：0。
0： 标準直播。
1：慢直播。
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
        :param TemplateId: 範本 ID。
調用 [CreateLiveSnapshotTemplate](/document/product/267/32624) 時返回的範本 ID。
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
        :type Template: :class:`tencentcloud.live.v20180801.models.SnapshotTemplateInfo`
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


class DescribeLiveStreamOnlineListRequest(AbstractModel):
    """DescribeLiveStreamOnlineList請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 推流域名。多域名用戶需要填寫 DomainName。
        :type DomainName: str
        :param AppName: 推流路徑，與推流和播放網址中的 AppName 保持一緻，預設爲 live。多路徑用戶需要填寫 AppName。
        :type AppName: str
        :param PageNum: 取得第幾頁，預設1。
        :type PageNum: int
        :param PageSize: 每頁大小，最大100。 
取值：10~100之間的任意整數。
預設值：10。
        :type PageSize: int
        :param StreamName: 流名稱，用于精确查詢。
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
        :param DomainName: 您的推流域名。
        :type DomainName: str
        :param EndTime: 結束時間。
UTC 格式，例如：2016-06-30T19:00:00Z。
不超過當前時間。
注意：EndTime和StartTime相差不可超過30天。
        :type EndTime: str
        :param StartTime: 起始時間。 
UTC 格式，例如：2016-06-29T19:00:00Z。
最長支援查詢60天内數據。
        :type StartTime: str
        :param AppName: 推流路徑，與推流和播放網址中的 AppName 保持一緻，預設爲 live。不支援模糊比對。
        :type AppName: str
        :param PageNum: 取得第幾頁。
預設值：1。
        :type PageNum: int
        :param PageSize: 分頁大小。
最大值：100。
取值範圍：1~100 之前的任意整數。
預設值：10。
        :type PageSize: int
        :param StreamName: 流名稱，支援模糊比對。
        :type StreamName: str
        """
        self.DomainName = None
        self.EndTime = None
        self.StartTime = None
        self.AppName = None
        self.PageNum = None
        self.PageSize = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        self.AppName = params.get("AppName")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.StreamName = params.get("StreamName")


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
        :param PushDomain: 推流域名。
        :type PushDomain: str
        :param StreamName: 流名稱。
        :type StreamName: str
        :param DayTime: 查詢時間，北京時間，
格式：yyyymmdd。
注意：支援查詢近1個月内某天的詳細數據。
        :type DayTime: str
        :param PageNum: 頁數，預設1，
不超過100頁。
        :type PageNum: int
        :param PageSize: 每頁個數，預設20，
範圍：[10,1000]。
        :type PageSize: int
        :param StartDayTime: 起始天時間，北京時間，
格式：yyyymmdd。
注意：支援查詢近1個月内的詳細數據。
        :type StartDayTime: str
        :param EndDayTime: 結束天時間，北京時間，
格式：yyyymmdd。
注意：支援查詢近1個月内的詳細數據，注意DayTime 與（StartDayTime，EndDayTime）必須要傳一個，如果都傳，會以DayTime爲準 。
        :type EndDayTime: str
        """
        self.PushDomain = None
        self.StreamName = None
        self.DayTime = None
        self.PageNum = None
        self.PageSize = None
        self.StartDayTime = None
        self.EndDayTime = None


    def _deserialize(self, params):
        self.PushDomain = params.get("PushDomain")
        self.StreamName = params.get("StreamName")
        self.DayTime = params.get("DayTime")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.StartDayTime = params.get("StartDayTime")
        self.EndDayTime = params.get("EndDayTime")


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
        :param TemplateId: 範本 ID。
注意：在創建轉碼範本介面 [CreateLiveTranscodeTemplate](/document/product/267/32646) 調用的返回值中獲取範本 ID。
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
        :type Template: :class:`tencentcloud.live.v20180801.models.TemplateInfo`
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
        :param WatermarkId: 浮水印 ID。
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
        :type Watermark: :class:`tencentcloud.live.v20180801.models.WatermarkInfo`
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
        :param StartTime: 開始時間，北京時間。
格式：yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param EndTime: 結束時間，北京時間。
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


class DescribePlayErrorCodeDetailInfoListRequest(AbstractModel):
    """DescribePlayErrorCodeDetailInfoList請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 起始時間，北京時間，
格式：yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param EndTime: 結束時間，北京時間，
格式：yyyy-mm-dd HH:MM:SS。
注：EndTime 和 StartTime 只支援最近1天的數據查詢。
        :type EndTime: str
        :param Granularity: 查詢粒度：
1-1分鍾粒度。
        :type Granularity: int
        :param StatType: 是，可選值包括”4xx”,”5xx”，支援”4xx,5xx”等這種混合模式。
        :type StatType: str
        :param PlayDomains: 播放域名清單。
        :type PlayDomains: list of str
        :param MainlandOrOversea: 地域，可選值：Mainland，Oversea，China，Foreign，Global（預設值）；如果爲空，查詢總的數據；如果爲“Mainland”，查詢中國大陸的數據；如果爲“Oversea”，則查詢中國大陸以外的數據；如果爲China，查詢中國的數據（包括港澳台）；如果爲Foreign，查詢國外的數據（不包括港澳台）。
        :type MainlandOrOversea: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Granularity = None
        self.StatType = None
        self.PlayDomains = None
        self.MainlandOrOversea = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Granularity = params.get("Granularity")
        self.StatType = params.get("StatType")
        self.PlayDomains = params.get("PlayDomains")
        self.MainlandOrOversea = params.get("MainlandOrOversea")


class DescribePlayErrorCodeDetailInfoListResponse(AbstractModel):
    """DescribePlayErrorCodeDetailInfoList返回參數結構體

    """

    def __init__(self):
        """
        :param HttpCodeList: 統計訊息清單。
        :type HttpCodeList: list of HttpCodeInfo
        :param StatType: 統計類型。
        :type StatType: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.HttpCodeList = None
        self.StatType = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HttpCodeList") is not None:
            self.HttpCodeList = []
            for item in params.get("HttpCodeList"):
                obj = HttpCodeInfo()
                obj._deserialize(item)
                self.HttpCodeList.append(obj)
        self.StatType = params.get("StatType")
        self.RequestId = params.get("RequestId")


class DescribePlayErrorCodeSumInfoListRequest(AbstractModel):
    """DescribePlayErrorCodeSumInfoList請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 起始時間點，北京時間。
格式：yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param EndTime: 結束時間點，北京時間。
格式：yyyy-mm-dd HH:MM:SS。
注：EndTime 和 StartTime 只支援最近1天的數據查詢。
        :type EndTime: str
        :param PlayDomains: 播放域名清單，不填表示總體數據。
        :type PlayDomains: list of str
        :param PageNum: 頁數，範圍[1,1000]，預設值是1。
        :type PageNum: int
        :param PageSize: 每頁個數，範圍：[1,1000]，預設值是20。
        :type PageSize: int
        :param MainlandOrOversea: 地域，可選值：Mainland，Oversea，China，Foreign，Global（預設值）；如果爲空，查詢總的數據；如果爲“Mainland”，查詢中國大陸的數據；如果爲“Oversea”，則查詢中國大陸以外的數據；如果爲China，查詢中國的數據（包括港澳台）；如果爲Foreign，查詢國外的數據（不包括港澳台）。
        :type MainlandOrOversea: str
        :param GroupType: 分組參數，可選值：CountryProIsp（預設值），Country（國家），預設是按照國家+省份+運營商來進行分組；目前國外的省份和運營商暫時無法識别。
        :type GroupType: str
        :param OutLanguage: 輸出欄位使用的語言，可選值：Chinese（預設值），English，目前國家，省份和運營商支援多語言。
        :type OutLanguage: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PlayDomains = None
        self.PageNum = None
        self.PageSize = None
        self.MainlandOrOversea = None
        self.GroupType = None
        self.OutLanguage = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PlayDomains = params.get("PlayDomains")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        self.GroupType = params.get("GroupType")
        self.OutLanguage = params.get("OutLanguage")


class DescribePlayErrorCodeSumInfoListResponse(AbstractModel):
    """DescribePlayErrorCodeSumInfoList返回參數結構體

    """

    def __init__(self):
        """
        :param ProIspInfoList: 分省份分運營商錯誤碼爲4或5開頭的狀态碼數據訊息。
        :type ProIspInfoList: list of ProIspPlayCodeDataInfo
        :param TotalCodeAll: 所有狀态碼的加和的次數。
        :type TotalCodeAll: int
        :param TotalCode4xx: 狀态碼爲4開頭的總次數。
        :type TotalCode4xx: int
        :param TotalCode5xx: 狀态碼爲5開頭的總次數。
        :type TotalCode5xx: int
        :param TotalCodeList: 各狀态碼的總次數。
        :type TotalCodeList: list of PlayCodeTotalInfo
        :param PageNum: 頁号。
        :type PageNum: int
        :param PageSize: 每頁大小。
        :type PageSize: int
        :param TotalPage: 總頁數。
        :type TotalPage: int
        :param TotalNum: 總記錄數。
        :type TotalNum: int
        :param TotalCode2xx: 狀态碼爲2開頭的總次數。
        :type TotalCode2xx: int
        :param TotalCode3xx: 狀态碼爲3開頭的總次數。
        :type TotalCode3xx: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ProIspInfoList = None
        self.TotalCodeAll = None
        self.TotalCode4xx = None
        self.TotalCode5xx = None
        self.TotalCodeList = None
        self.PageNum = None
        self.PageSize = None
        self.TotalPage = None
        self.TotalNum = None
        self.TotalCode2xx = None
        self.TotalCode3xx = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProIspInfoList") is not None:
            self.ProIspInfoList = []
            for item in params.get("ProIspInfoList"):
                obj = ProIspPlayCodeDataInfo()
                obj._deserialize(item)
                self.ProIspInfoList.append(obj)
        self.TotalCodeAll = params.get("TotalCodeAll")
        self.TotalCode4xx = params.get("TotalCode4xx")
        self.TotalCode5xx = params.get("TotalCode5xx")
        if params.get("TotalCodeList") is not None:
            self.TotalCodeList = []
            for item in params.get("TotalCodeList"):
                obj = PlayCodeTotalInfo()
                obj._deserialize(item)
                self.TotalCodeList.append(obj)
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TotalPage = params.get("TotalPage")
        self.TotalNum = params.get("TotalNum")
        self.TotalCode2xx = params.get("TotalCode2xx")
        self.TotalCode3xx = params.get("TotalCode3xx")
        self.RequestId = params.get("RequestId")


class DescribeProIspPlaySumInfoListRequest(AbstractModel):
    """DescribeProIspPlaySumInfoList請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 起始時間，北京時間，
格式：yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param EndTime: 結束時間，北京時間，
格式：yyyy-mm-dd HH:MM:SS。
注：EndTime 和 StartTime 只支援最近1天的數據查詢。
        :type EndTime: str
        :param StatType: 統計的類型，可選值：”Province”，”Isp”，“CountryOrArea”。
        :type StatType: str
        :param PlayDomains: 不填則爲總體數據。
        :type PlayDomains: list of str
        :param PageNum: 頁号，範圍是[1,1000]，預設值是1。
        :type PageNum: int
        :param PageSize: 每頁個數，範圍是[1,1000]，預設值是20。
        :type PageSize: int
        :param MainlandOrOversea: 地域，可選值：Mainland，Oversea，China，Foreign，Global（預設值）；如果爲空，查詢總的數據；如果爲“Mainland”，查詢中國大陸的數據；如果爲“Oversea”，則查詢中國大陸以外的數據；如果爲China，查詢中國的數據（包括港澳台）；如果爲Foreign，查詢國外的數據（不包括港澳台）。
        :type MainlandOrOversea: str
        :param OutLanguage: 輸出欄位使用的語言，可選值：Chinese（預設值），English；目前國家，省份和運營商支援多語言。
        :type OutLanguage: str
        """
        self.StartTime = None
        self.EndTime = None
        self.StatType = None
        self.PlayDomains = None
        self.PageNum = None
        self.PageSize = None
        self.MainlandOrOversea = None
        self.OutLanguage = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.StatType = params.get("StatType")
        self.PlayDomains = params.get("PlayDomains")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        self.OutLanguage = params.get("OutLanguage")


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
        :param PageSize: 每頁的記錄數。
        :type PageSize: int
        :param PageNum: 頁号。
        :type PageNum: int
        :param TotalNum: 總記錄數。
        :type TotalNum: int
        :param TotalPage: 總頁數。
        :type TotalPage: int
        :param DataInfoList: 省份，運營商，國家或地區匯總數據清單。
        :type DataInfoList: list of ProIspPlaySumInfo
        :param AvgFluxPerSecond: 平均頻寬。
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
        :param StartTime: 起始時間點，當前使用北京時間，
例：2019-02-21 10:00:00。
        :type StartTime: str
        :param EndTime: 結束時間點，當前使用北京時間，
例：2019-02-21 12:00:00。
注：EndTime 和 StartTime 只支援最近1天的數據查詢。
        :type EndTime: str
        :param Granularity: 支援如下粒度：
1：1分鍾粒度（跨度不支援超過1天）
        :type Granularity: int
        :param StatType: 統計指标類型：
“Bandwidth”：頻寬
“FluxPerSecond”：平均流量
“Flux”：流量
“Request”：請求數
“Online”：并發連接數
        :type StatType: str
        :param PlayDomains: 播放域名清單。
        :type PlayDomains: list of str
        :param ProvinceNames: 要查詢的省份（地區）英文名稱清單，如 Beijing。
        :type ProvinceNames: list of str
        :param IspNames: 要查詢的運營商英文名稱清單，如 China Mobile ，如果爲空，查詢所有運營商的數據。
        :type IspNames: list of str
        :param MainlandOrOversea: 地域，可選值：Mainland，Oversea，China，Foreign，Global（預設值）；如果爲空，查詢總的數據；如果爲“Mainland”，查詢中國大陸的數據；如果爲“Oversea”，則查詢中國大陸以外的數據；如果爲China，查詢中國的數據（包括港澳台）；如果爲Foreign，查詢國外的數據（不包括港澳台）。
        :type MainlandOrOversea: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Granularity = None
        self.StatType = None
        self.PlayDomains = None
        self.ProvinceNames = None
        self.IspNames = None
        self.MainlandOrOversea = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Granularity = params.get("Granularity")
        self.StatType = params.get("StatType")
        self.PlayDomains = params.get("PlayDomains")
        self.ProvinceNames = params.get("ProvinceNames")
        self.IspNames = params.get("IspNames")
        self.MainlandOrOversea = params.get("MainlandOrOversea")


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
        :param ConfigId: 配置 ID。
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


class DescribeScreenShotSheetNumListRequest(AbstractModel):
    """DescribeScreenShotSheetNumList請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: utc起始時間，格式爲yyyy-mm-ddTHH:MM:SSZ
        :type StartTime: str
        :param EndTime: utc結束時間，格式爲yyyy-mm-ddTHH:MM:SSZ，支援查詢最近1年數據。
        :type EndTime: str
        :param Zone: 地域訊息，可選值包括Mainland，Oversea，前者是查詢中國大陸範圍内的數據，後者是除中國大陸範圍之外的數據，若不傳該參數，則查詢所有地區的數據。
        :type Zone: str
        :param PushDomains: 推流域名（支援查詢2019年11 月1日之後的域名維度數據）。
        :type PushDomains: list of str
        :param Granularity: 數據維度，數據延遲1個半小時，可選值包括：1、Minute（5分鍾粒度，最大支援查詢時間範圍是31天），2、Day（天粒度，預設值，最大支援查詢時間範圍是186天當天）。
        :type Granularity: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Zone = None
        self.PushDomains = None
        self.Granularity = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Zone = params.get("Zone")
        self.PushDomains = params.get("PushDomains")
        self.Granularity = params.get("Granularity")


class DescribeScreenShotSheetNumListResponse(AbstractModel):
    """DescribeScreenShotSheetNumList返回參數結構體

    """

    def __init__(self):
        """
        :param DataInfoList: 數據訊息清單。
        :type DataInfoList: list of TimeValue
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = TimeValue()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStreamDayPlayInfoListRequest(AbstractModel):
    """DescribeStreamDayPlayInfoList請求參數結構體

    """

    def __init__(self):
        """
        :param DayTime: 日期，格式：YYYY-mm-dd。
第二天淩晨3點出昨天的數據，建議在這個時間點之後查詢最新數據。
        :type DayTime: str
        :param PlayDomain: 播放域名。
        :type PlayDomain: str
        :param PageNum: 頁号，範圍[1,1000]，預設值是1。
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
        :param StartTime: 開始時間，北京時間，格式爲yyyy-mm-dd HH:MM:SS，
當前時間 和 開始時間 間隔不超過30天。
        :type StartTime: str
        :param EndTime: 結束時間，北京時間，格式爲yyyy-mm-dd HH:MM:SS，
結束時間 和 開始時間  必須在同一天内。
        :type EndTime: str
        :param PlayDomain: 播放域名，
若不填，則爲查詢所有播放域名的在線流數據。
        :type PlayDomain: str
        :param StreamName: 流名稱，精确比對。
若不填，則爲查詢總體播放數據。
        :type StreamName: str
        :param AppName: 推流路徑，與播放網址中的AppName保持一緻，會精确比對，在同時傳遞了StreamName時生效。
若不填，則爲查詢總體播放數據。
注意：按AppName查詢，需要聯系客服同學提單支援。
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


class DescribeStreamPushInfoListRequest(AbstractModel):
    """DescribeStreamPushInfoList請求參數結構體

    """

    def __init__(self):
        """
        :param StreamName: 流名稱。
        :type StreamName: str
        :param StartTime: 起始時間點，格式爲yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param EndTime: 結束時間點，格式爲yyyy-mm-dd HH:MM:SS，最大時間跨度支援6小時，支援最近6天數據查詢。
        :type EndTime: str
        :param PushDomain: 推流域名。
        :type PushDomain: str
        :param AppName: 推流路徑，與推流和播放網址中的AppName保持一緻，預設爲 live。
        :type AppName: str
        """
        self.StreamName = None
        self.StartTime = None
        self.EndTime = None
        self.PushDomain = None
        self.AppName = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PushDomain = params.get("PushDomain")
        self.AppName = params.get("AppName")


class DescribeStreamPushInfoListResponse(AbstractModel):
    """DescribeStreamPushInfoList返回參數結構體

    """

    def __init__(self):
        """
        :param DataInfoList: 返回的數據清單。
        :type DataInfoList: list of PushQualityData
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = PushQualityData()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTopClientIpSumInfoListRequest(AbstractModel):
    """DescribeTopClientIpSumInfoList請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 起始時間點，格式爲yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param EndTime: 結束時間點，格式爲yyyy-mm-dd HH:MM:SS
時間跨度在[0,4小時]，支援最近1天數據查詢。
        :type EndTime: str
        :param PlayDomains: 播放域名，預設爲不填，表示求總體數據。
        :type PlayDomains: list of str
        :param PageNum: 頁号，範圍是[1,1000]，預設值是1。
        :type PageNum: int
        :param PageSize: 每頁個數，範圍是[1,1000]，預設值是20。
        :type PageSize: int
        :param OrderParam: 排序指标，可選值包括TotalRequest（預設值），FailedRequest,TotalFlux。
        :type OrderParam: str
        :param MainlandOrOversea: 地域，可選值：Mainland，Oversea，China，Foreign，Global（預設值）；如果爲空，查詢總的數據；如果爲“Mainland”，查詢中國大陸的數據；如果爲“Oversea”，則查詢中國大陸以外的數據；如果爲China，查詢中國的數據（包括港澳台）；如果爲Foreign，查詢國外的數據（不包括港澳台）。
        :type MainlandOrOversea: str
        :param OutLanguage: 輸出欄位使用的語言，可選值：Chinese（預設值），English；目前國家，省份和運營商支援多語言。
        :type OutLanguage: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PlayDomains = None
        self.PageNum = None
        self.PageSize = None
        self.OrderParam = None
        self.MainlandOrOversea = None
        self.OutLanguage = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PlayDomains = params.get("PlayDomains")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.OrderParam = params.get("OrderParam")
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        self.OutLanguage = params.get("OutLanguage")


class DescribeTopClientIpSumInfoListResponse(AbstractModel):
    """DescribeTopClientIpSumInfoList返回參數結構體

    """

    def __init__(self):
        """
        :param PageNum: 頁号，範圍是[1,1000]，預設值是1。
        :type PageNum: int
        :param PageSize: 每頁個數，範圍是[1,1000]，預設值是20。
        :type PageSize: int
        :param OrderParam: 排序指标，可選值包括”TotalRequest”，”FailedRequest”,“TotalFlux”。
        :type OrderParam: str
        :param TotalNum: 記錄總數。
        :type TotalNum: int
        :param TotalPage: 記錄總頁數。
        :type TotalPage: int
        :param DataInfoList: 數據内容。
        :type DataInfoList: list of ClientIpPlaySumInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PageNum = None
        self.PageSize = None
        self.OrderParam = None
        self.TotalNum = None
        self.TotalPage = None
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.OrderParam = params.get("OrderParam")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = ClientIpPlaySumInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVisitTopSumInfoListRequest(AbstractModel):
    """DescribeVisitTopSumInfoList請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 起始時間點，格式爲yyyy-mm-dd HH:MM:SS。
        :type StartTime: str
        :param EndTime: 結束時間點，格式爲yyyy-mm-dd HH:MM:SS
時間跨度在(0,4小時]，支援最近1天數據查詢。
        :type EndTime: str
        :param TopIndex: 峰值指标，可選值包括”Domain”，”StreamId”。
        :type TopIndex: str
        :param PlayDomains: 播放域名，預設爲不填，表示求總體數據。
        :type PlayDomains: list of str
        :param PageNum: 頁号，
範圍是[1,1000]，
預設值是1。
        :type PageNum: int
        :param PageSize: 每頁個數，範圍是[1,1000]，
預設值是20。
        :type PageSize: int
        :param OrderParam: 排序指标，可選值包括” AvgFluxPerSecond”，”TotalRequest”（預設）,“TotalFlux”。
        :type OrderParam: str
        """
        self.StartTime = None
        self.EndTime = None
        self.TopIndex = None
        self.PlayDomains = None
        self.PageNum = None
        self.PageSize = None
        self.OrderParam = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TopIndex = params.get("TopIndex")
        self.PlayDomains = params.get("PlayDomains")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.OrderParam = params.get("OrderParam")


class DescribeVisitTopSumInfoListResponse(AbstractModel):
    """DescribeVisitTopSumInfoList返回參數結構體

    """

    def __init__(self):
        """
        :param PageNum: 頁号，
範圍是[1,1000]，
預設值是1。
        :type PageNum: int
        :param PageSize: 每頁個數，範圍是[1,1000]，
預設值是20。
        :type PageSize: int
        :param TopIndex: 峰值指标，可選值包括”Domain”，”StreamId”。
        :type TopIndex: str
        :param OrderParam: 排序指标，可選值包括” AvgFluxPerSecond”，”TotalRequest”（預設）,“TotalFlux”。
        :type OrderParam: str
        :param TotalNum: 記錄總數。
        :type TotalNum: int
        :param TotalPage: 記錄總頁數。
        :type TotalPage: int
        :param DataInfoList: 數據内容。
        :type DataInfoList: list of PlaySumStatInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PageNum = None
        self.PageSize = None
        self.TopIndex = None
        self.OrderParam = None
        self.TotalNum = None
        self.TotalPage = None
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TopIndex = params.get("TopIndex")
        self.OrderParam = params.get("OrderParam")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = PlaySumStatInfo()
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
0：用戶添加證書，
1：Top Cloud 托管證書。
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


class DomainDetailInfo(AbstractModel):
    """每個域名的統計訊息。

    """

    def __init__(self):
        """
        :param MainlandOrOversea: 國内還是國外:
Mainland: 表示國内數據。
Oversea: 表示國外數據。
        :type MainlandOrOversea: str
        :param Bandwidth: 頻寬，單位: Mbps。
        :type Bandwidth: float
        :param Flux: 流量，單位: MB。
        :type Flux: float
        :param Online: 人數。
        :type Online: int
        :param Request: 請求數。
        :type Request: int
        """
        self.MainlandOrOversea = None
        self.Bandwidth = None
        self.Flux = None
        self.Online = None
        self.Request = None


    def _deserialize(self, params):
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        self.Bandwidth = params.get("Bandwidth")
        self.Flux = params.get("Flux")
        self.Online = params.get("Online")
        self.Request = params.get("Request")


class DomainInfo(AbstractModel):
    """直播域名訊息

    """

    def __init__(self):
        """
        :param Name: 直播域名。
        :type Name: str
        :param Type: 域名類型:
0: 推流。
1: 播放。
        :type Type: int
        :param Status: 域名狀态:
0: 停用。
1: 啓用。
        :type Status: int
        :param CreateTime: 添加時間。
        :type CreateTime: str
        :param BCName: 是否有 CName 到固定規則域名:
0: 否。
1: 是。
        :type BCName: int
        :param TargetDomain: cname 對應的域名。
        :type TargetDomain: str
        :param PlayType: 播放區域，只在 Type=1 時該參數有意義。
1: 國内。
2: 全球。
3: 海外。
        :type PlayType: int
        :param IsDelayLive: 是否慢直播:
0: 普通直播。
1: 慢直播。
        :type IsDelayLive: int
        :param CurrentCName: 當前客戶使用的 cname 訊息。
        :type CurrentCName: str
        :param RentTag: 失效參數，可忽略。
        :type RentTag: int
        :param RentExpireTime: 失效參數，可忽略。
        :type RentExpireTime: str
        :param IsMiniProgramLive: 0: 标準直播。
1: 小程式直播。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsMiniProgramLive: int
        """
        self.Name = None
        self.Type = None
        self.Status = None
        self.CreateTime = None
        self.BCName = None
        self.TargetDomain = None
        self.PlayType = None
        self.IsDelayLive = None
        self.CurrentCName = None
        self.RentTag = None
        self.RentExpireTime = None
        self.IsMiniProgramLive = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.BCName = params.get("BCName")
        self.TargetDomain = params.get("TargetDomain")
        self.PlayType = params.get("PlayType")
        self.IsDelayLive = params.get("IsDelayLive")
        self.CurrentCName = params.get("CurrentCName")
        self.RentTag = params.get("RentTag")
        self.RentExpireTime = params.get("RentExpireTime")
        self.IsMiniProgramLive = params.get("IsMiniProgramLive")


class DomainInfoList(AbstractModel):
    """多個域名訊息清單

    """

    def __init__(self):
        """
        :param Domain: 域名。
        :type Domain: str
        :param DetailInfoList: 明細訊息。
        :type DetailInfoList: list of DomainDetailInfo
        """
        self.Domain = None
        self.DetailInfoList = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        if params.get("DetailInfoList") is not None:
            self.DetailInfoList = []
            for item in params.get("DetailInfoList"):
                obj = DomainDetailInfo()
                obj._deserialize(item)
                self.DetailInfoList.append(obj)


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
        :param DomainName: 待啓用的直播域名。
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
        :param DomainName: 待停用的直播域名。
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
        :param DomainName: 您的推流域名。
        :type DomainName: str
        :param StreamName: 流名稱。
        :type StreamName: str
        :param ResumeTime: 恢複流的時間。UTC 格式，例如：2018-11-29T19:00:00Z。
注意：
1. 預設禁播7天，且最長支援禁播90天。
2. 北京時間值爲 UTC 時間值 + 8 小時，格式按照 ISO 8601 标準表示，詳見 [ISO 日期格式說明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type ResumeTime: str
        :param Reason: 禁推原因。
注明：請務必填寫禁推原因，防止誤操作。
長度限制：2048位元。
        :type Reason: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None
        self.ResumeTime = None
        self.Reason = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")
        self.ResumeTime = params.get("ResumeTime")
        self.Reason = params.get("Reason")


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


class GroupProIspDataInfo(AbstractModel):
    """某省份某運營商在某段時間内的頻寬，流量，請求數和并發數

    """

    def __init__(self):
        """
        :param ProvinceName: 省份。
        :type ProvinceName: str
        :param IspName: 運營商。
        :type IspName: str
        :param DetailInfoList: 分鍾維度的明細數據。
        :type DetailInfoList: list of CdnPlayStatData
        """
        self.ProvinceName = None
        self.IspName = None
        self.DetailInfoList = None


    def _deserialize(self, params):
        self.ProvinceName = params.get("ProvinceName")
        self.IspName = params.get("IspName")
        if params.get("DetailInfoList") is not None:
            self.DetailInfoList = []
            for item in params.get("DetailInfoList"):
                obj = CdnPlayStatData()
                obj._deserialize(item)
                self.DetailInfoList.append(obj)


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


class HttpCodeInfo(AbstractModel):
    """HTTP返回碼和統計數據

    """

    def __init__(self):
        """
        :param HttpCode: HTTP協議返回碼。
例："2xx", "3xx", "4xx", "5xx"。
        :type HttpCode: str
        :param ValueList: 統計訊息，對于無數據的時間點，會補0。
        :type ValueList: list of HttpCodeValue
        """
        self.HttpCode = None
        self.ValueList = None


    def _deserialize(self, params):
        self.HttpCode = params.get("HttpCode")
        if params.get("ValueList") is not None:
            self.ValueList = []
            for item in params.get("ValueList"):
                obj = HttpCodeValue()
                obj._deserialize(item)
                self.ValueList.append(obj)


class HttpCodeValue(AbstractModel):
    """HTTP返回碼數據訊息

    """

    def __init__(self):
        """
        :param Time: 時間，格式：yyyy-mm-dd HH:MM:SS。
        :type Time: str
        :param Numbers: 次數。
        :type Numbers: int
        :param Percentage: 占比。
        :type Percentage: float
        """
        self.Time = None
        self.Numbers = None
        self.Percentage = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Numbers = params.get("Numbers")
        self.Percentage = params.get("Percentage")


class HttpStatusData(AbstractModel):
    """播放錯誤碼訊息

    """

    def __init__(self):
        """
        :param Time: 數據時間點，
格式：yyyy-mm-dd HH:MM:SS。
        :type Time: str
        :param HttpStatusInfoList: 播放狀态碼詳細訊息。
        :type HttpStatusInfoList: list of HttpStatusInfo
        """
        self.Time = None
        self.HttpStatusInfoList = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        if params.get("HttpStatusInfoList") is not None:
            self.HttpStatusInfoList = []
            for item in params.get("HttpStatusInfoList"):
                obj = HttpStatusInfo()
                obj._deserialize(item)
                self.HttpStatusInfoList.append(obj)


class HttpStatusInfo(AbstractModel):
    """播放錯誤碼訊息

    """

    def __init__(self):
        """
        :param HttpStatus: 播放HTTP狀态碼。
        :type HttpStatus: str
        :param Num: 個數。
        :type Num: int
        """
        self.HttpStatus = None
        self.Num = None


    def _deserialize(self, params):
        self.HttpStatus = params.get("HttpStatus")
        self.Num = params.get("Num")


class LivePackageInfo(AbstractModel):
    """直播包訊息。

    """

    def __init__(self):
        """
        :param Id: 包 ID。
        :type Id: str
        :param Total: 總量。
注意：當爲流量包時單位爲位元。
當爲轉碼包時單位爲分鍾。
        :type Total: int
        :param Used: 使用量。
注意：當爲流量包時單位爲位元。
當爲轉碼包時單位爲分鍾。
        :type Used: int
        :param Left: 剩餘量。
注意：當爲流量包時單位爲位元。
當爲轉碼包時單位爲分鍾。
        :type Left: int
        :param BuyTime: 購買時間。
        :type BuyTime: str
        :param ExpireTime: 過期時間。
        :type ExpireTime: str
        :param Type: 包類型，可選值:
0: 流量包。
1: 普通轉碼包。
2: 極速高清包。
        :type Type: int
        :param Status: 包狀态，可選值:
0: 未使用。
1: 使用中。
2: 已過期。
        :type Status: int
        """
        self.Id = None
        self.Total = None
        self.Used = None
        self.Left = None
        self.BuyTime = None
        self.ExpireTime = None
        self.Type = None
        self.Status = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Total = params.get("Total")
        self.Used = params.get("Used")
        self.Left = params.get("Left")
        self.BuyTime = params.get("BuyTime")
        self.ExpireTime = params.get("ExpireTime")
        self.Type = params.get("Type")
        self.Status = params.get("Status")


class LogInfo(AbstractModel):
    """日志url訊息。

    """

    def __init__(self):
        """
        :param LogName: 日志名稱。
        :type LogName: str
        :param LogUrl: 日志 URL。
        :type LogUrl: str
        :param LogTime: 日志生成時間。
        :type LogTime: str
        :param FileSize: 文件大小。
        :type FileSize: int
        """
        self.LogName = None
        self.LogUrl = None
        self.LogTime = None
        self.FileSize = None


    def _deserialize(self, params):
        self.LogName = params.get("LogName")
        self.LogUrl = params.get("LogUrl")
        self.LogTime = params.get("LogTime")
        self.FileSize = params.get("FileSize")


class ModifyLiveCallbackTemplateRequest(AbstractModel):
    """ModifyLiveCallbackTemplate請求參數結構體

    """

    def __init__(self):
        """
        :param TemplateId: 範本 ID。
        :type TemplateId: int
        :param TemplateName: 範本名稱。
        :type TemplateName: str
        :param Description: 描述訊息。
        :type Description: str
        :param StreamBeginNotifyUrl: 開播回調 URL。
        :type StreamBeginNotifyUrl: str
        :param StreamEndNotifyUrl: 斷流回調 URL。
        :type StreamEndNotifyUrl: str
        :param RecordNotifyUrl: 錄制回調 URL。
        :type RecordNotifyUrl: str
        :param SnapshotNotifyUrl: 截圖回調 URL。
        :type SnapshotNotifyUrl: str
        :param PornCensorshipNotifyUrl: 鑒黃回調 URL。
        :type PornCensorshipNotifyUrl: str
        :param CallbackKey: 回調 Key，回調 URL 公用，回調簽名詳見事件訊息通知文件。
[事件訊息通知](/document/product/267/32744)。
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
        :param TemplateId: 範本 ID。
        :type TemplateId: int
        :param TemplateName: 範本名稱。
        :type TemplateName: str
        :param Description: 描述訊息。
        :type Description: str
        :param FlvParam: FLV 錄制參數，開啓 FLV 錄制時設置。
        :type FlvParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param HlsParam: HLS 錄制參數，開啓 HLS 錄制時設置。
        :type HlsParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param Mp4Param: MP4 錄制參數，開啓 MP4 錄制時設置。
        :type Mp4Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param AacParam: AAC 錄制參數，開啓 AAC 錄制時設置。
        :type AacParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param HlsSpecialParam: HLS 錄制定制參數。
        :type HlsSpecialParam: :class:`tencentcloud.live.v20180801.models.HlsSpecialParam`
        :param Mp3Param: MP3 錄制參數，開啓 MP3 錄制時設置。
        :type Mp3Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.FlvParam = None
        self.HlsParam = None
        self.Mp4Param = None
        self.AacParam = None
        self.HlsSpecialParam = None
        self.Mp3Param = None


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
        if params.get("Mp3Param") is not None:
            self.Mp3Param = RecordParam()
            self.Mp3Param._deserialize(params.get("Mp3Param"))


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
        :param TemplateId: 範本 ID。
        :type TemplateId: int
        :param TemplateName: 範本名稱。
長度上限：255位元。
        :type TemplateName: str
        :param Description: 描述訊息。
長度上限：1024位元。
        :type Description: str
        :param SnapshotInterval: 截圖間隔，單位s，預設10s。
範圍： 5s ~ 600s。
        :type SnapshotInterval: int
        :param Width: 截圖寬度。預設：0（原始寬）。
        :type Width: int
        :param Height: 截圖高度。預設：0（原始高）。
        :type Height: int
        :param PornFlag: 是否開啓鑒黃，預設 0 。
0：不開啓。
1：開啓。
        :type PornFlag: int
        :param CosAppId: Cos 應用 ID。
        :type CosAppId: int
        :param CosBucket: Cos Bucket名稱。
        :type CosBucket: str
        :param CosRegion: Cos 地域。
        :type CosRegion: str
        :param CosPrefix: Cos Bucket文件夾前綴。
        :type CosPrefix: str
        :param CosFileName: Cos 文件名稱。
        :type CosFileName: str
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
        self.CosPrefix = None
        self.CosFileName = None


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
        self.CosPrefix = params.get("CosPrefix")
        self.CosFileName = params.get("CosFileName")


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
        :param TemplateId: 範本 Id。
        :type TemplateId: int
        :param Vcodec: 視訊編碼：
h264/h265。
        :type Vcodec: str
        :param Acodec: 音訊編碼：
aac/mp3。
        :type Acodec: str
        :param AudioBitrate: 音訊碼率，預設0。
範圍：0-500。
        :type AudioBitrate: int
        :param Description: 範本描述。
        :type Description: str
        :param VideoBitrate: 視訊碼率。範圍：100kbps - 8000kbps。
注意：碼率必須是100的倍數。
        :type VideoBitrate: int
        :param Width: 寬。0-3000。
        :type Width: int
        :param NeedVideo: 是否保留視訊，0：否，1：是。預設1。
        :type NeedVideo: int
        :param NeedAudio: 是否保留音訊，0：否，1：是。預設1。
        :type NeedAudio: int
        :param Height: 高。0-3000。
        :type Height: int
        :param Fps: 幀率。0-200。
        :type Fps: int
        :param Gop: 關鍵幀間隔，單位：秒。0-50。
        :type Gop: int
        :param Rotate: 旋轉角度。
0 90 180 270。
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
        :param AdaptBitratePercent: 極速高清相比 VideoBitrate 少多少碼率，0.1到0.5。
        :type AdaptBitratePercent: float
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
        self.AdaptBitratePercent = None


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
        self.AdaptBitratePercent = params.get("AdaptBitratePercent")


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
        :param AreaId: 區域id：
1-深圳，
2-上海，
3-天津，
4-中國香港。
如有改動，需同時傳入IspId。
        :type AreaId: int
        :param IspId: 運營商id,1-電信,2-移動,3-聯通,4-其他,AreaId爲4的時候,IspId只能爲其他。如有改動，需同時傳入AreaId。
        :type IspId: int
        :param StartTime: 開始時間。
使用UTC格式時間，
例如：2019-01-08T10:00:00Z。
注意：北京時間值爲 UTC 時間值 + 8 小時，格式按照 ISO 8601 标準表示，詳見 [ISO 日期格式說明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type StartTime: str
        :param EndTime: 結束時間，注意：
1. 結束時間必須大于開始時間；
2. 結束時間和開始時間必須大于當前時間；
3. 結束時間 和 開始時間 間隔必須小於七天。

使用UTC格式時間，
例如：2019-01-08T10:00:00Z。
注意：北京時間值爲 UTC 時間值 + 8 小時，格式按照 ISO 8601 标準表示，詳見 [ISO 日期格式說明](https://cloud.tencent.com/document/product/266/11732#I)。
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
        :param ConfigIds: 配置 ID 清單。
        :type ConfigIds: list of str
        :param Status: 目标狀态。0無效，2正在運作，4暫停。
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


class MonitorStreamPlayInfo(AbstractModel):
    """監控播放數據

    """

    def __init__(self):
        """
        :param PlayDomain: 播放域名。
        :type PlayDomain: str
        :param StreamName: 流id。
        :type StreamName: str
        :param Rate: 播放碼率，0表示原始碼率。
        :type Rate: int
        :param Protocol: 播放協議，可選值包括 Unknown，Flv，Hls，Rtmp，Huyap2p。
        :type Protocol: str
        :param Bandwidth: 頻寬，單位是Mbps。
        :type Bandwidth: float
        :param Online: 在線人數，1分鍾采樣一個點，統計采樣點的tcp連結數目。
        :type Online: int
        :param Request: 請求數。
        :type Request: int
        """
        self.PlayDomain = None
        self.StreamName = None
        self.Rate = None
        self.Protocol = None
        self.Bandwidth = None
        self.Online = None
        self.Request = None


    def _deserialize(self, params):
        self.PlayDomain = params.get("PlayDomain")
        self.StreamName = params.get("StreamName")
        self.Rate = params.get("Rate")
        self.Protocol = params.get("Protocol")
        self.Bandwidth = params.get("Bandwidth")
        self.Online = params.get("Online")
        self.Request = params.get("Request")


class PlayAuthKeyInfo(AbstractModel):
    """播放鑒權key訊息。

    """

    def __init__(self):
        """
        :param DomainName: 域名。
        :type DomainName: str
        :param Enable: 是否啓用:
0: 關閉。
1: 啓用。
        :type Enable: int
        :param AuthKey: 鑒權 Key。
        :type AuthKey: str
        :param AuthDelta: 有效時間，單位：秒。
        :type AuthDelta: int
        :param AuthBackKey: 鑒權 BackKey。
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


class PlayCodeTotalInfo(AbstractModel):
    """各狀态碼的總次數，支援大多數的 HTTP 協議返回碼。

    """

    def __init__(self):
        """
        :param Code: HTTP code，可選值包括:
400，403，404，500，502，503，504。
        :type Code: str
        :param Num: 總次數。
        :type Num: int
        """
        self.Code = None
        self.Num = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Num = params.get("Num")


class PlayDataInfoByStream(AbstractModel):
    """流維度的播放訊息。

    """

    def __init__(self):
        """
        :param StreamName: 流名稱。
        :type StreamName: str
        :param TotalFlux: 總流量，單位: MB。
        :type TotalFlux: float
        """
        self.StreamName = None
        self.TotalFlux = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.TotalFlux = params.get("TotalFlux")


class PlayStatInfo(AbstractModel):
    """按省份運營商查詢的播放訊息。

    """

    def __init__(self):
        """
        :param Time: 數據時間點。
        :type Time: str
        :param Value: 頻寬/流量/請求數/并發連接數/下載速度的值，若沒數據返回時該值爲0。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Value: float
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")


class PlaySumStatInfo(AbstractModel):
    """播放匯總統計訊息。

    """

    def __init__(self):
        """
        :param Name: 域名或流 ID。
        :type Name: str
        :param AvgFluxPerSecond: 平均下載速度，
單位: MB/s。
計算公式: 每分鍾的下載速度求平均值。
        :type AvgFluxPerSecond: float
        :param TotalFlux: 總流量，單位: MB。
        :type TotalFlux: float
        :param TotalRequest: 總請求數。
        :type TotalRequest: int
        """
        self.Name = None
        self.AvgFluxPerSecond = None
        self.TotalFlux = None
        self.TotalRequest = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.AvgFluxPerSecond = params.get("AvgFluxPerSecond")
        self.TotalFlux = params.get("TotalFlux")
        self.TotalRequest = params.get("TotalRequest")


class ProIspPlayCodeDataInfo(AbstractModel):
    """播放錯誤碼訊息

    """

    def __init__(self):
        """
        :param CountryAreaName: 國家或地區。
        :type CountryAreaName: str
        :param ProvinceName: 省份。
        :type ProvinceName: str
        :param IspName: 運營商。
        :type IspName: str
        :param Code2xx: 錯誤碼爲2開頭的次數。
        :type Code2xx: int
        :param Code3xx: 錯誤碼爲3開頭的次數。
        :type Code3xx: int
        :param Code4xx: 錯誤碼爲4開頭的次數。
        :type Code4xx: int
        :param Code5xx: 錯誤碼爲5開頭的次數。
        :type Code5xx: int
        """
        self.CountryAreaName = None
        self.ProvinceName = None
        self.IspName = None
        self.Code2xx = None
        self.Code3xx = None
        self.Code4xx = None
        self.Code5xx = None


    def _deserialize(self, params):
        self.CountryAreaName = params.get("CountryAreaName")
        self.ProvinceName = params.get("ProvinceName")
        self.IspName = params.get("IspName")
        self.Code2xx = params.get("Code2xx")
        self.Code3xx = params.get("Code3xx")
        self.Code4xx = params.get("Code4xx")
        self.Code5xx = params.get("Code5xx")


class ProIspPlaySumInfo(AbstractModel):
    """獲取省份/運營商的播放訊息。

    """

    def __init__(self):
        """
        :param Name: 省份/運營商/國家或地區。
        :type Name: str
        :param TotalFlux: 總流量，單位: MB。
        :type TotalFlux: float
        :param TotalRequest: 總請求數。
        :type TotalRequest: int
        :param AvgFluxPerSecond: 平均下載流量，單位: MB/s。
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
    """推流時間。

    """

    def __init__(self):
        """
        :param PublishTime: 推流時間。
UTC 格式，例如：2018-06-29T19:00:00Z。
        :type PublishTime: str
        """
        self.PublishTime = None


    def _deserialize(self, params):
        self.PublishTime = params.get("PublishTime")


class PullStreamConfig(AbstractModel):
    """拉流配置。

    """

    def __init__(self):
        """
        :param ConfigId: 拉流配置 ID。
        :type ConfigId: str
        :param FromUrl: 源 URL。
        :type FromUrl: str
        :param ToUrl: 目的 URL。
        :type ToUrl: str
        :param AreaName: 區域名。
        :type AreaName: str
        :param IspName: 運營商名。
        :type IspName: str
        :param StartTime: 開始時間。
UTC格式時間，例如: 2019-01-08T10:00:00Z。
注意：北京時間值爲 UTC 時間值 + 8 小時，格式按照 ISO 8601 标準表示，詳見 [ISO 日期格式說明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type StartTime: str
        :param EndTime: 結束時間。

UTC格式時間，例如：2019-01-08T10:00:00Z。
注意：北京時間值爲 UTC 時間值 + 8 小時，格式按照 ISO 8601 标準表示，詳見 [ISO 日期格式說明](https://cloud.tencent.com/document/product/266/11732#I)。
        :type EndTime: str
        :param Status: 狀态:
0: 無效。
1: 初始狀态。
2: 正在運作。
3: 拉起失敗。
4: 暫停。
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
    """推流鑒權key訊息。

    """

    def __init__(self):
        """
        :param DomainName: 域名。
        :type DomainName: str
        :param Enable: 是否啓用，0：關閉，1：啓用。
        :type Enable: int
        :param MasterAuthKey: 主鑒權 Key。
        :type MasterAuthKey: str
        :param BackupAuthKey: 備鑒權 Key。
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
        :param ClientIp: 推流用戶端 IP。
        :type ClientIp: str
        :param ServerIp: 接流服務器 IP。
        :type ServerIp: str
        :param VideoFps: 推流視訊幀率，單位: Hz。
        :type VideoFps: int
        :param VideoSpeed: 推流視訊碼率，單位: bps。
        :type VideoSpeed: int
        :param AudioFps: 推流音訊幀率，單位: Hz。
        :type AudioFps: int
        :param AudioSpeed: 推流音訊碼率，單位: bps。
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
        :param AsampleRate: 采樣率。
        :type AsampleRate: int
        :param MetaAudioSpeed: metadata 中的音訊碼率，單位: Kbps。
        :type MetaAudioSpeed: int
        :param MetaVideoSpeed: metadata 中的視訊碼率，單位: Kbps。
        :type MetaVideoSpeed: int
        :param MetaFps: metadata 中的幀率。
        :type MetaFps: int
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
        self.AsampleRate = None
        self.MetaAudioSpeed = None
        self.MetaVideoSpeed = None
        self.MetaFps = None


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
        self.AsampleRate = params.get("AsampleRate")
        self.MetaAudioSpeed = params.get("MetaAudioSpeed")
        self.MetaVideoSpeed = params.get("MetaVideoSpeed")
        self.MetaFps = params.get("MetaFps")


class PushQualityData(AbstractModel):
    """某條流的推流質量詳情數據。

    """

    def __init__(self):
        """
        :param Time: 數據時間，格式: %Y-%m-%d %H:%M:%S.%ms，精确到毫秒級。
        :type Time: str
        :param PushDomain: 推流域名。
        :type PushDomain: str
        :param AppName: 推流路徑。
        :type AppName: str
        :param ClientIp: 推流用戶端 IP。
        :type ClientIp: str
        :param BeginPushTime: 開始推流時間，格式: %Y-%m-%d %H:%M:%S.%ms，精确到毫秒級。
        :type BeginPushTime: str
        :param Resolution: 分辨率訊息。
        :type Resolution: str
        :param VCodec: 視訊編碼格式。
        :type VCodec: str
        :param ACodec: 音訊編碼格式。
        :type ACodec: str
        :param Sequence: 推流序列号，用來唯一的标志一次推流。
        :type Sequence: str
        :param VideoFps: 視訊幀率。
        :type VideoFps: int
        :param VideoRate: 視訊碼率，單位: bps。
        :type VideoRate: int
        :param AudioFps: 音訊幀率。
        :type AudioFps: int
        :param AudioRate: 音訊碼率，單位: bps。
        :type AudioRate: int
        :param LocalTs: 本地流逝時間，單位: ms，影音流逝時間與本地流逝時間的差距越大表示推流質量越差，上行卡頓越嚴重。
        :type LocalTs: int
        :param VideoTs: 視訊流逝時間，單位: ms。
        :type VideoTs: int
        :param AudioTs: 音訊流逝時間，單位: ms。
        :type AudioTs: int
        :param MetaVideoRate: metadata 中的視訊碼率，單位: kbps。
        :type MetaVideoRate: int
        :param MetaAudioRate: metadata 中的音訊碼率，單位: kbps。
        :type MetaAudioRate: int
        :param MateFps: metadata 中的幀率。
        :type MateFps: int
        """
        self.Time = None
        self.PushDomain = None
        self.AppName = None
        self.ClientIp = None
        self.BeginPushTime = None
        self.Resolution = None
        self.VCodec = None
        self.ACodec = None
        self.Sequence = None
        self.VideoFps = None
        self.VideoRate = None
        self.AudioFps = None
        self.AudioRate = None
        self.LocalTs = None
        self.VideoTs = None
        self.AudioTs = None
        self.MetaVideoRate = None
        self.MetaAudioRate = None
        self.MateFps = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.PushDomain = params.get("PushDomain")
        self.AppName = params.get("AppName")
        self.ClientIp = params.get("ClientIp")
        self.BeginPushTime = params.get("BeginPushTime")
        self.Resolution = params.get("Resolution")
        self.VCodec = params.get("VCodec")
        self.ACodec = params.get("ACodec")
        self.Sequence = params.get("Sequence")
        self.VideoFps = params.get("VideoFps")
        self.VideoRate = params.get("VideoRate")
        self.AudioFps = params.get("AudioFps")
        self.AudioRate = params.get("AudioRate")
        self.LocalTs = params.get("LocalTs")
        self.VideoTs = params.get("VideoTs")
        self.AudioTs = params.get("AudioTs")
        self.MetaVideoRate = params.get("MetaVideoRate")
        self.MetaAudioRate = params.get("MetaAudioRate")
        self.MateFps = params.get("MateFps")


class RecordParam(AbstractModel):
    """錄制範本參數。

    """

    def __init__(self):
        """
        :param RecordInterval: 錄制間隔。
單位秒，預設：1800。
取值範圍：300-7200。
此參數對 HLS 無效，當錄制 HLS 時從推流到斷流生成一個文件。
        :type RecordInterval: int
        :param StorageTime: 錄制儲存時長。
單位秒，取值範圍： 0 - 93312000。
0：表示永久儲存。
        :type StorageTime: int
        :param Enable: 是否開啓當前格式錄制，預設值爲0，0：否， 1：是。
        :type Enable: int
        :param VodSubAppId: 點播子應用 ID。
        :type VodSubAppId: int
        """
        self.RecordInterval = None
        self.StorageTime = None
        self.Enable = None
        self.VodSubAppId = None


    def _deserialize(self, params):
        self.RecordInterval = params.get("RecordInterval")
        self.StorageTime = params.get("StorageTime")
        self.Enable = params.get("Enable")
        self.VodSubAppId = params.get("VodSubAppId")


class RecordTemplateInfo(AbstractModel):
    """錄制範本訊息

    """

    def __init__(self):
        """
        :param TemplateId: 範本 ID。
        :type TemplateId: int
        :param TemplateName: 範本名稱。
        :type TemplateName: str
        :param Description: 描述訊息。
        :type Description: str
        :param FlvParam: FLV 錄制參數。
        :type FlvParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param HlsParam: HLS 錄制參數。
        :type HlsParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param Mp4Param: MP4 錄制參數。
        :type Mp4Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param AacParam: AAC 錄制參數。
        :type AacParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param IsDelayLive: 0：普通直播，
1：慢直播。
        :type IsDelayLive: int
        :param HlsSpecialParam: HLS 錄制定制參數
        :type HlsSpecialParam: :class:`tencentcloud.live.v20180801.models.HlsSpecialParam`
        :param Mp3Param: MP3 錄制參數。
        :type Mp3Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
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
        self.Mp3Param = None


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
        if params.get("Mp3Param") is not None:
            self.Mp3Param = RecordParam()
            self.Mp3Param._deserialize(params.get("Mp3Param"))


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
    """規則訊息。

    """

    def __init__(self):
        """
        :param CreateTime: 規則創建時間。
        :type CreateTime: str
        :param UpdateTime: 規則更新時間。
        :type UpdateTime: str
        :param TemplateId: 範本 ID。
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


class SnapshotTemplateInfo(AbstractModel):
    """截圖範本訊息。

    """

    def __init__(self):
        """
        :param TemplateId: 範本 ID。
        :type TemplateId: int
        :param TemplateName: 範本名稱。
        :type TemplateName: str
        :param SnapshotInterval: 截圖時間間隔，5-300秒。
        :type SnapshotInterval: int
        :param Width: 截圖寬度，範圍：0-3000。 
0：原始寬度并适配原始比例。
        :type Width: int
        :param Height: 截圖高度，範圍：0-2000。
0：原始高度并适配原始比例。
        :type Height: int
        :param PornFlag: 是否開啓鑒黃，0：不開啓，1：開啓。
        :type PornFlag: int
        :param CosAppId: Cos 應用 ID。
        :type CosAppId: int
        :param CosBucket: Cos Bucket名稱。
        :type CosBucket: str
        :param CosRegion: Cos 地域。
        :type CosRegion: str
        :param Description: 範本描述。
        :type Description: str
        :param CosPrefix: Cos Bucket文件夾前綴。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CosPrefix: str
        :param CosFileName: Cos 文件名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CosFileName: str
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
        self.CosPrefix = None
        self.CosFileName = None


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
        self.CosPrefix = params.get("CosPrefix")
        self.CosFileName = params.get("CosFileName")


class StopLiveRecordRequest(AbstractModel):
    """StopLiveRecord請求參數結構體

    """

    def __init__(self):
        """
        :param StreamName: 流名稱。
        :type StreamName: str
        :param TaskId: 任務ID，全局唯一标識錄制任務。
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
UTC 格式時間，例如：2019-01-07T12:00:00Z。
        :type StreamStartTime: str
        :param StreamEndTime: 推流結束時間。
UTC 格式時間，例如：2019-01-07T15:00:00Z。
        :type StreamEndTime: str
        :param StopReason: 停止原因。
        :type StopReason: str
        :param Duration: 推流持續時長，單位：秒。
        :type Duration: int
        :param ClientIp: 主播 IP。
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


class StreamName(AbstractModel):
    """流名稱清單。

    """

    def __init__(self):
        """
        :param StreamName: 流名稱。
        :type StreamName: str
        :param AppName: 應用名稱。
        :type AppName: str
        :param DomainName: 推流域名。
        :type DomainName: str
        :param StreamStartTime: 推流開始時間。
UTC格式時間，例如：2019-01-07T12:00:00Z。
        :type StreamStartTime: str
        :param StreamEndTime: 推流結束時間。
UTC格式時間，例如：2019-01-07T15:00:00Z。
        :type StreamEndTime: str
        :param StopReason: 停止原因。
        :type StopReason: str
        :param Duration: 推流持續時長，單位：秒。
        :type Duration: int
        :param ClientIp: 主播 IP。
        :type ClientIp: str
        :param Resolution: 分辨率。
        :type Resolution: str
        """
        self.StreamName = None
        self.AppName = None
        self.DomainName = None
        self.StreamStartTime = None
        self.StreamEndTime = None
        self.StopReason = None
        self.Duration = None
        self.ClientIp = None
        self.Resolution = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamStartTime = params.get("StreamStartTime")
        self.StreamEndTime = params.get("StreamEndTime")
        self.StopReason = params.get("StopReason")
        self.Duration = params.get("Duration")
        self.ClientIp = params.get("ClientIp")
        self.Resolution = params.get("Resolution")


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
    """轉碼範本訊息。

    """

    def __init__(self):
        """
        :param Vcodec: 視訊編碼：
h264/h265。
        :type Vcodec: str
        :param VideoBitrate: 視訊碼率，取值範圍：100kbps - 8000kbps。
        :type VideoBitrate: int
        :param Acodec: 音訊編碼，可選 aac 或 mp3。
        :type Acodec: str
        :param AudioBitrate: 音訊碼率。取值範圍：0kbps - 500kbps。
        :type AudioBitrate: int
        :param Width: 寬，取值範圍：0-3000。
        :type Width: int
        :param Height: 高，取值範圍：0-3000。
        :type Height: int
        :param Fps: 幀率。取值範圍：0fps - 200fps。
        :type Fps: int
        :param Gop: 關鍵幀間隔，取值範圍：1秒 - 50秒。
        :type Gop: int
        :param Rotate: 旋轉角度。可選擇：0 90 180 270。
        :type Rotate: int
        :param Profile: 編碼質量，可選擇：
baseline，main，high。
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
        :param TemplateId: 範本 ID。
        :type TemplateId: int
        :param TemplateName: 範本名稱。
        :type TemplateName: str
        :param Description: 範本描述。
        :type Description: str
        :param AiTransCode: 是否是極速高清範本，0：否，1：是。預設0。
        :type AiTransCode: int
        :param AdaptBitratePercent: 極速高清相比 VideoBitrate 少多少碼率，0.1到0.5。
        :type AdaptBitratePercent: float
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
        self.AiTransCode = None
        self.AdaptBitratePercent = None


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
        self.AiTransCode = params.get("AiTransCode")
        self.AdaptBitratePercent = params.get("AdaptBitratePercent")


class TimeValue(AbstractModel):
    """某個時間點的指标的數值是多少。

    """

    def __init__(self):
        """
        :param Time: UTC 時間，時間格式：yyyy-mm-ddTHH:MM:SSZ。
        :type Time: str
        :param Num: 數值。
        :type Num: int
        """
        self.Time = None
        self.Num = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Num = params.get("Num")


class TranscodeDetailInfo(AbstractModel):
    """轉碼詳細訊息。

    """

    def __init__(self):
        """
        :param StreamName: 流名稱。
        :type StreamName: str
        :param StartTime: 開始時間（北京時間），格式：yyyy-mm-dd HH:MM。
        :type StartTime: str
        :param EndTime: 結束時間（北京時間），格式：yyyy-mm-dd HH:MM。
        :type EndTime: str
        :param Duration: 轉碼時長，單位：分鍾。
注意：因推流過程中可能有中斷重推情況，此處時長爲真實轉碼時長累加值，并非結束時間和開始時間的間隔。
        :type Duration: int
        :param ModuleCodec: 編碼方式，帶模組，
範例：
liveprocessor_H264：直播轉碼-H264，
liveprocessor_H265： 直播轉碼-H265，
topspeed_H264：極速高清-H264，
topspeed_H265：極速高清-H265。
        :type ModuleCodec: str
        :param Bitrate: 碼率。
        :type Bitrate: int
        :param Type: 類型，包含：轉碼（Transcode），混流（MixStream），浮水印（WaterMark）。
        :type Type: str
        :param PushDomain: 推流域名。
        :type PushDomain: str
        :param Resolution: 分辨率。
        :type Resolution: str
        """
        self.StreamName = None
        self.StartTime = None
        self.EndTime = None
        self.Duration = None
        self.ModuleCodec = None
        self.Bitrate = None
        self.Type = None
        self.PushDomain = None
        self.Resolution = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Duration = params.get("Duration")
        self.ModuleCodec = params.get("ModuleCodec")
        self.Bitrate = params.get("Bitrate")
        self.Type = params.get("Type")
        self.PushDomain = params.get("PushDomain")
        self.Resolution = params.get("Resolution")


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
        :param WatermarkId: 浮水印 ID。
在添加浮水印介面 [AddLiveWatermark](/document/product/267/30154) 調用返回值中獲取水印 ID。
        :type WatermarkId: int
        :param PictureUrl: 浮水印圖片 URL。
        :type PictureUrl: str
        :param XPosition: 顯示位置，X軸偏移，預設 0。
        :type XPosition: int
        :param YPosition: 顯示位置，Y軸偏移，預設 0。
        :type YPosition: int
        :param WatermarkName: 浮水印名稱。
        :type WatermarkName: str
        :param Width: 浮水印寬度，占直播原始畫面寬度百分比，建議高寬只設置一項，另外一項會自适應縮放，避免變形。預設原始寬度。
        :type Width: int
        :param Height: 浮水印高度，占直播原始畫面寬度百分比，建議高寬只設置一項，另外一項會自适應縮放，避免變形。預設原始高度。
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
    """浮水印訊息。

    """

    def __init__(self):
        """
        :param WatermarkId: 浮水印 ID。
        :type WatermarkId: int
        :param PictureUrl: 浮水印圖片 URL。
        :type PictureUrl: str
        :param XPosition: 顯示位置，X 軸偏移。
        :type XPosition: int
        :param YPosition: 顯示位置，Y 軸偏移。
        :type YPosition: int
        :param WatermarkName: 浮水印名稱。
        :type WatermarkName: str
        :param Status: 當前狀态。0：未使用，1:使用中。
        :type Status: int
        :param CreateTime: 添加時間。
        :type CreateTime: str
        :param Width: 浮水印寬。
        :type Width: int
        :param Height: 浮水印高。
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