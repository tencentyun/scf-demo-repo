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


class CreateSessionRequest(AbstractModel):
    """CreateSession請求參數結構體

    """

    def __init__(self):
        """
        :param ClientSession: 用戶端session訊息，從JSSDK請求中獲得
        :type ClientSession: str
        :param GameId: 遊戲ID
        :type GameId: str
        :param UserId: 遊戲用戶ID
        :type UserId: str
        :param GameParas: 遊戲參數
        :type GameParas: str
        :param GameRegion: 遊戲區域
        :type GameRegion: str
        :param ImageUrl: 背景圖url
        :type ImageUrl: str
        :param Resolution: 分辨率
        :type Resolution: str
        """
        self.ClientSession = None
        self.GameId = None
        self.UserId = None
        self.GameParas = None
        self.GameRegion = None
        self.ImageUrl = None
        self.Resolution = None


    def _deserialize(self, params):
        self.ClientSession = params.get("ClientSession")
        self.GameId = params.get("GameId")
        self.UserId = params.get("UserId")
        self.GameParas = params.get("GameParas")
        self.GameRegion = params.get("GameRegion")
        self.ImageUrl = params.get("ImageUrl")
        self.Resolution = params.get("Resolution")


class CreateSessionResponse(AbstractModel):
    """CreateSession返回參數結構體

    """

    def __init__(self):
        """
        :param ServerSession: 服務端session訊息，返回給JSSDK
        :type ServerSession: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ServerSession = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServerSession = params.get("ServerSession")
        self.RequestId = params.get("RequestId")


class DayStreamPlayInfo(AbstractModel):
    """流播放訊息

    """

    def __init__(self):
        """
        :param Bandwidth: 頻寬（單位Mbps）。
        :type Bandwidth: float
        :param Flux: 流量 （單位MB）。
        :type Flux: float
        :param Online: 在線人數。
        :type Online: int
        :param Request: 請求數。
        :type Request: int
        :param Time: 數據時間點，格式：yyyy-mm-dd HH:MM:SS。
        :type Time: str
        """
        self.Bandwidth = None
        self.Flux = None
        self.Online = None
        self.Request = None
        self.Time = None


    def _deserialize(self, params):
        self.Bandwidth = params.get("Bandwidth")
        self.Flux = params.get("Flux")
        self.Online = params.get("Online")
        self.Request = params.get("Request")
        self.Time = params.get("Time")


class DescribeStreamPlayInfoListRequest(AbstractModel):
    """DescribeStreamPlayInfoList請求參數結構體

    """

    def __init__(self):
        """
        :param EndTime: 結束時間， 時間，格式：2019-04-28 10:36:00
結束時間 和 開始時間  必須在同一天内。
        :type EndTime: str
        :param PlayDomain: 播放域名。
        :type PlayDomain: str
        :param StartTime: 開始時間， 時間，格式：2019-04-28 10:36:00
當前時間 和 開始時間 間隔不超過30天。
        :type StartTime: str
        :param StreamName: 流名稱，精确比對。
若不填，則爲查詢總體播放數據。
        :type StreamName: str
        """
        self.EndTime = None
        self.PlayDomain = None
        self.StartTime = None
        self.StreamName = None


    def _deserialize(self, params):
        self.EndTime = params.get("EndTime")
        self.PlayDomain = params.get("PlayDomain")
        self.StartTime = params.get("StartTime")
        self.StreamName = params.get("StreamName")


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


class DescribeWorkersRequest(AbstractModel):
    """DescribeWorkers請求參數結構體

    """


class DescribeWorkersResponse(AbstractModel):
    """DescribeWorkers返回參數結構體

    """

    def __init__(self):
        """
        :param RegionDetail: 各個區域的機器情況
        :type RegionDetail: list of WorkerRegionInfo
        :param Idle: 空閑機器總數量
        :type Idle: int
        :param RegionNum: 區域個數
        :type RegionNum: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RegionDetail = None
        self.Idle = None
        self.RegionNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionDetail") is not None:
            self.RegionDetail = []
            for item in params.get("RegionDetail"):
                obj = WorkerRegionInfo()
                obj._deserialize(item)
                self.RegionDetail.append(obj)
        self.Idle = params.get("Idle")
        self.RegionNum = params.get("RegionNum")
        self.RequestId = params.get("RequestId")


class ForbidLiveStreamRequest(AbstractModel):
    """ForbidLiveStream請求參數結構體

    """

    def __init__(self):
        """
        :param AppName: 應用名稱。
        :type AppName: str
        :param DomainName: 您的推流域名。
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


class RegisterIMRequest(AbstractModel):
    """RegisterIM請求參數結構體

    """

    def __init__(self):
        """
        :param Nickname: 用戶昵稱
        :type Nickname: str
        :param UserId: 用戶唯一ID，建議采用用戶小程式OpenID加鹽形式
        :type UserId: str
        :param HeadImgUrl: 用戶頭像URL
        :type HeadImgUrl: str
        :param Level: 用戶身份，預設值：0，表示無特殊身份
        :type Level: int
        """
        self.Nickname = None
        self.UserId = None
        self.HeadImgUrl = None
        self.Level = None


    def _deserialize(self, params):
        self.Nickname = params.get("Nickname")
        self.UserId = params.get("UserId")
        self.HeadImgUrl = params.get("HeadImgUrl")
        self.Level = params.get("Level")


class RegisterIMResponse(AbstractModel):
    """RegisterIM返回參數結構體

    """

    def __init__(self):
        """
        :param UserKey: 用來傳遞給插件的關鍵欄位
        :type UserKey: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.UserKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserKey = params.get("UserKey")
        self.RequestId = params.get("RequestId")


class StopGameRequest(AbstractModel):
    """StopGame請求參數結構體

    """

    def __init__(self):
        """
        :param UserId: 遊戲用戶ID
        :type UserId: str
        """
        self.UserId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")


class StopGameResponse(AbstractModel):
    """StopGame返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class WorkerRegionInfo(AbstractModel):
    """worker的區域訊息

    """

    def __init__(self):
        """
        :param Idle: 該區域空閑機器數量
        :type Idle: int
        :param Region: 區域
        :type Region: str
        """
        self.Idle = None
        self.Region = None


    def _deserialize(self, params):
        self.Idle = params.get("Idle")
        self.Region = params.get("Region")