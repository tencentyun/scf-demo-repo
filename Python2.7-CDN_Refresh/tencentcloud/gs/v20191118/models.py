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
        :param UserId: 遊戲用戶ID
        :type UserId: str
        :param GameId: 遊戲ID
        :type GameId: str
        :param GameRegion: 遊戲區域，ap-guangzhou、ap-shanghai、ap-beijing等
        :type GameRegion: str
        :param GameParas: 遊戲參數
        :type GameParas: str
        :param Resolution: 分辨率,，可設置爲1080p或720p
        :type Resolution: str
        :param ImageUrl: 背景圖url，格式爲png或jpeg，寬高1920*1080
        :type ImageUrl: str
        :param SetNo: 資源池編號，1表示正式，2表示測試
        :type SetNo: int
        :param Bitrate: 單位Mbps，固定碼率，後端不動态調整(MaxBitrate和MinBitrate将無效)
        :type Bitrate: int
        :param MaxBitrate: 單位Mbps，動态調整最大碼率
        :type MaxBitrate: int
        :param MinBitrate: 單位Mbps，動态調整最小碼率
        :type MinBitrate: int
        :param Fps: 幀率，可設置爲30、45或60
        :type Fps: int
        :param UserIp: 遊戲用戶IP，用於就近調度，例如125.127.178.228
        :type UserIp: str
        :param Optimization: 優化項，便於客戶灰度開啓新的優化項，預設爲0
        :type Optimization: int
        """
        self.ClientSession = None
        self.UserId = None
        self.GameId = None
        self.GameRegion = None
        self.GameParas = None
        self.Resolution = None
        self.ImageUrl = None
        self.SetNo = None
        self.Bitrate = None
        self.MaxBitrate = None
        self.MinBitrate = None
        self.Fps = None
        self.UserIp = None
        self.Optimization = None


    def _deserialize(self, params):
        self.ClientSession = params.get("ClientSession")
        self.UserId = params.get("UserId")
        self.GameId = params.get("GameId")
        self.GameRegion = params.get("GameRegion")
        self.GameParas = params.get("GameParas")
        self.Resolution = params.get("Resolution")
        self.ImageUrl = params.get("ImageUrl")
        self.SetNo = params.get("SetNo")
        self.Bitrate = params.get("Bitrate")
        self.MaxBitrate = params.get("MaxBitrate")
        self.MinBitrate = params.get("MinBitrate")
        self.Fps = params.get("Fps")
        self.UserIp = params.get("UserIp")
        self.Optimization = params.get("Optimization")


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


class DescribeWorkersInfoRequest(AbstractModel):
    """DescribeWorkersInfo請求參數結構體

    """


class DescribeWorkersInfoResponse(AbstractModel):
    """DescribeWorkersInfo返回參數結構體

    """

    def __init__(self):
        """
        :param WorkerNum: 機器數量
        :type WorkerNum: int
        :param WorkerDetail: 機器詳細訊息
        :type WorkerDetail: list of WorkerDetail
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.WorkerNum = None
        self.WorkerDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WorkerNum = params.get("WorkerNum")
        if params.get("WorkerDetail") is not None:
            self.WorkerDetail = []
            for item in params.get("WorkerDetail"):
                obj = WorkerDetail()
                obj._deserialize(item)
                self.WorkerDetail.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWorkersRequest(AbstractModel):
    """DescribeWorkers請求參數結構體

    """

    def __init__(self):
        """
        :param SetNo: 資源池編號，1表示正式，2表示測試
        :type SetNo: int
        """
        self.SetNo = None


    def _deserialize(self, params):
        self.SetNo = params.get("SetNo")


class DescribeWorkersResponse(AbstractModel):
    """DescribeWorkers返回參數結構體

    """

    def __init__(self):
        """
        :param Idle: 空閑機器總數量
        :type Idle: int
        :param RegionNum: 區域個數
        :type RegionNum: int
        :param RegionDetail: 各個區域的機器情況
        :type RegionDetail: list of WorkerRegionInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Idle = None
        self.RegionNum = None
        self.RegionDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Idle = params.get("Idle")
        self.RegionNum = params.get("RegionNum")
        if params.get("RegionDetail") is not None:
            self.RegionDetail = []
            for item in params.get("RegionDetail"):
                obj = WorkerRegionInfo()
                obj._deserialize(item)
                self.RegionDetail.append(obj)
        self.RequestId = params.get("RequestId")


class EnterQueueRequest(AbstractModel):
    """EnterQueue請求參數結構體

    """

    def __init__(self):
        """
        :param First: true：第一次請求排隊 false：已在排隊中，查詢當前排名
        :type First: bool
        :param GameId: 遊戲ID
        :type GameId: str
        :param UserId: 用戶ID
        :type UserId: str
        :param SetNumber: 資源池編號
        :type SetNumber: int
        """
        self.First = None
        self.GameId = None
        self.UserId = None
        self.SetNumber = None


    def _deserialize(self, params):
        self.First = params.get("First")
        self.GameId = params.get("GameId")
        self.UserId = params.get("UserId")
        self.SetNumber = params.get("SetNumber")


class EnterQueueResponse(AbstractModel):
    """EnterQueue返回參數結構體

    """

    def __init__(self):
        """
        :param Rank: 排名
        :type Rank: int
        :param LockSuccess: 機器鎖定成功
        :type LockSuccess: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Rank = None
        self.LockSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Rank = params.get("Rank")
        self.LockSuccess = params.get("LockSuccess")
        self.RequestId = params.get("RequestId")


class ModifyWorkersRequest(AbstractModel):
    """ModifyWorkers請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 批次機器ID，最多不超過100個
        :type InstanceIds: list of str
        :param SetNo: 資源池編號，修改有效範圍爲[1,100]，在idle狀态下才能修改成功
        :type SetNo: int
        """
        self.InstanceIds = None
        self.SetNo = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.SetNo = params.get("SetNo")


class ModifyWorkersResponse(AbstractModel):
    """ModifyWorkers返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class QuitQueueRequest(AbstractModel):
    """QuitQueue請求參數結構體

    """

    def __init__(self):
        """
        :param UserId: 用戶ID
        :type UserId: str
        :param SetNumber: 資源池編號
        :type SetNumber: int
        """
        self.UserId = None
        self.SetNumber = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.SetNumber = params.get("SetNumber")


class QuitQueueResponse(AbstractModel):
    """QuitQueue返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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


class TrylockWorkerRequest(AbstractModel):
    """TrylockWorker請求參數結構體

    """

    def __init__(self):
        """
        :param UserId: 遊戲用戶ID
        :type UserId: str
        :param GameId: 遊戲ID
        :type GameId: str
        :param GameRegion: 遊戲區域，ap-guangzhou、ap-shanghai、ap-beijing等
        :type GameRegion: str
        :param SetNo: 資源池編號，1表示共用，2表示測試
        :type SetNo: int
        :param UserIp: 遊戲用戶IP，用於就近調度，例如125.127.178.228
        :type UserIp: str
        """
        self.UserId = None
        self.GameId = None
        self.GameRegion = None
        self.SetNo = None
        self.UserIp = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.GameId = params.get("GameId")
        self.GameRegion = params.get("GameRegion")
        self.SetNo = params.get("SetNo")
        self.UserIp = params.get("UserIp")


class TrylockWorkerResponse(AbstractModel):
    """TrylockWorker返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class WorkerDetail(AbstractModel):
    """機器詳細訊息

    """

    def __init__(self):
        """
        :param AppId: 客戶appid
        :type AppId: int
        :param SetNo: 資源池編號
        :type SetNo: int
        :param Region: 機器所屬區域
        :type Region: str
        :param InstanceId: 機器ID
        :type InstanceId: str
        :param InstanceType: 機器類型：
LARGE-大型
MEDIUM-中型
SMALL-小型
        :type InstanceType: str
        :param Ip: 機器IP
        :type Ip: str
        :param ServiceState: 服務狀态：
IDLE-空閑
LOCK-鎖定
ESTABLISHED-遊戲中
RECONNECT-等待重連
RECOVERY-清理恢複
FORBID-禁用
UNAVAILABLE-不可用
        :type ServiceState: str
        :param UserId: 用戶ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type UserId: str
        :param GameId: 遊戲ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type GameId: str
        """
        self.AppId = None
        self.SetNo = None
        self.Region = None
        self.InstanceId = None
        self.InstanceType = None
        self.Ip = None
        self.ServiceState = None
        self.UserId = None
        self.GameId = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.SetNo = params.get("SetNo")
        self.Region = params.get("Region")
        self.InstanceId = params.get("InstanceId")
        self.InstanceType = params.get("InstanceType")
        self.Ip = params.get("Ip")
        self.ServiceState = params.get("ServiceState")
        self.UserId = params.get("UserId")
        self.GameId = params.get("GameId")


class WorkerRegionInfo(AbstractModel):
    """worker的區域訊息

    """

    def __init__(self):
        """
        :param Region: 區域
        :type Region: str
        :param Idle: 該區域空閑機器數量
        :type Idle: int
        """
        self.Region = None
        self.Idle = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Idle = params.get("Idle")