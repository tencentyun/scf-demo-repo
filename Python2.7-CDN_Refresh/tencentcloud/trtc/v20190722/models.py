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


class DescribeCallDetailRequest(AbstractModel):
    """DescribeCallDetail請求參數結構體

    """

    def __init__(self):
        """
        :param CommId: 通話ID
        :type CommId: str
        :param StartTime: 查詢開始時間
        :type StartTime: int
        :param EndTime: 查詢結束時間
        :type EndTime: int
        :param SdkAppId: 用戶sdkappid
        :type SdkAppId: str
        :param UserIds: 需查詢的用戶數組，不填預設返回6個用戶
        :type UserIds: list of str
        :param DataType: 需查詢的指标，不填則只返回用戶清單，填all則返回所有指标。
appCpu：APP CPU使用率；
sysCpu：系統 CPU使用率；
aBit：上/下行音訊碼率；
aBlock：音訊卡頓時長；
vBit：上/下行視訊碼率；
vCapFps：視訊采集幀率；
vEncFps：視訊發送幀率；
vDecFps：渲染幀率；
vBlock：視訊卡頓時長；
aLoss：上/下行音訊丢包；
vLoss：上/下行視訊丢包；
vWidth：上/下行分辨率寬；
vHeight：上/下行分辨率高
        :type DataType: list of str
        """
        self.CommId = None
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None
        self.UserIds = None
        self.DataType = None


    def _deserialize(self, params):
        self.CommId = params.get("CommId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        self.UserIds = params.get("UserIds")
        self.DataType = params.get("DataType")


class DescribeCallDetailResponse(AbstractModel):
    """DescribeCallDetail返回參數結構體

    """

    def __init__(self):
        """
        :param Total: 返回的用戶總條數
        :type Total: int
        :param UserList: 用戶訊息清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type UserList: list of UserInformation
        :param Data: 質量數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: list of QualityData
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.UserList = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("UserList") is not None:
            self.UserList = []
            for item in params.get("UserList"):
                obj = UserInformation()
                obj._deserialize(item)
                self.UserList.append(obj)
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = QualityData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRealtimeNetworkRequest(AbstractModel):
    """DescribeRealtimeNetwork請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 查詢開始時間
        :type StartTime: int
        :param EndTime: 查詢結束時間
        :type EndTime: int
        :param SdkAppId: 用戶sdkappid
        :type SdkAppId: str
        :param DataType: 需查詢的數據類型
sendLossRateRaw：上行丢包率；
recvLossRateRaw：下行丢包率
        :type DataType: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None
        self.DataType = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        self.DataType = params.get("DataType")


class DescribeRealtimeNetworkResponse(AbstractModel):
    """DescribeRealtimeNetwork返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 查詢返回的數據
        :type Data: list of RealtimeData
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = RealtimeData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRealtimeQualityRequest(AbstractModel):
    """DescribeRealtimeQuality請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 查詢開始時間
        :type StartTime: int
        :param EndTime: 查詢結束時間
        :type EndTime: int
        :param SdkAppId: 用戶sdkappid
        :type SdkAppId: str
        :param DataType: 查詢的數據類型
enterTotalSuccPercent：進房成功率
fistFreamInSecRate：首幀秒開率
blockPercent：視訊卡頓率
audioBlockPercent：音訊卡頓率
        :type DataType: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None
        self.DataType = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        self.DataType = params.get("DataType")


class DescribeRealtimeQualityResponse(AbstractModel):
    """DescribeRealtimeQuality返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 返回的數據類型
        :type Data: list of RealtimeData
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = RealtimeData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRealtimeScaleRequest(AbstractModel):
    """DescribeRealtimeScale請求參數結構體

    """

    def __init__(self):
        """
        :param StartTime: 查詢開始時間
        :type StartTime: int
        :param EndTime: 查詢結束時間
        :type EndTime: int
        :param SdkAppId: 用戶sdkappid
        :type SdkAppId: str
        :param DataType: 查詢的數據類型
UserNum：通話人數；
RoomNum：房間數
        :type DataType: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.SdkAppId = None
        self.DataType = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SdkAppId = params.get("SdkAppId")
        self.DataType = params.get("DataType")


class DescribeRealtimeScaleResponse(AbstractModel):
    """DescribeRealtimeScale返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 返回的數據數組
        :type Data: list of RealtimeData
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = RealtimeData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRoomInformationRequest(AbstractModel):
    """DescribeRoomInformation請求參數結構體

    """

    def __init__(self):
        """
        :param SdkAppId: 用戶sdkappid
        :type SdkAppId: str
        :param StartTime: 查詢開始時間
        :type StartTime: int
        :param EndTime: 查詢結束時間
        :type EndTime: int
        :param RoomId: 數字房間号
        :type RoomId: str
        :param PageNumber: 分頁index（不填預設只返回10個）
        :type PageNumber: str
        :param PageSize: 分頁大小（不填預設返回10個,最多不超過100條）
        :type PageSize: str
        """
        self.SdkAppId = None
        self.StartTime = None
        self.EndTime = None
        self.RoomId = None
        self.PageNumber = None
        self.PageSize = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.RoomId = params.get("RoomId")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")


class DescribeRoomInformationResponse(AbstractModel):
    """DescribeRoomInformation返回參數結構體

    """

    def __init__(self):
        """
        :param Total: 返回的數據總條數
        :type Total: int
        :param RoomList: 房間訊息清單
        :type RoomList: list of RoomState
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.RoomList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("RoomList") is not None:
            self.RoomList = []
            for item in params.get("RoomList"):
                obj = RoomState()
                obj._deserialize(item)
                self.RoomList.append(obj)
        self.RequestId = params.get("RequestId")


class DismissRoomRequest(AbstractModel):
    """DismissRoom請求參數結構體

    """

    def __init__(self):
        """
        :param SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param RoomId: 房間号。
        :type RoomId: int
        """
        self.SdkAppId = None
        self.RoomId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")


class DismissRoomResponse(AbstractModel):
    """DismissRoom返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class QualityData(AbstractModel):
    """Es返回的質量數據

    """

    def __init__(self):
        """
        :param Content: 數據内容
        :type Content: list of TimeValue
        :param UserId: 用戶ID
        :type UserId: str
        :param PeerId: 對端Id,爲空時表示上行數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type PeerId: str
        :param DataType: 數據類型
        :type DataType: str
        """
        self.Content = None
        self.UserId = None
        self.PeerId = None
        self.DataType = None


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = TimeValue()
                obj._deserialize(item)
                self.Content.append(obj)
        self.UserId = params.get("UserId")
        self.PeerId = params.get("PeerId")
        self.DataType = params.get("DataType")


class RealtimeData(AbstractModel):
    """查詢秒級監控返回的數據

    """

    def __init__(self):
        """
        :param Content: 返回的數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type Content: list of TimeValue
        :param DataType: 數據類型欄位
        :type DataType: str
        """
        self.Content = None
        self.DataType = None


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = TimeValue()
                obj._deserialize(item)
                self.Content.append(obj)
        self.DataType = params.get("DataType")


class RemoveUserRequest(AbstractModel):
    """RemoveUser請求參數結構體

    """

    def __init__(self):
        """
        :param SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param RoomId: 房間号。
        :type RoomId: int
        :param UserIds: 要移出的用戶清單，最多10個。
        :type UserIds: list of str
        """
        self.SdkAppId = None
        self.RoomId = None
        self.UserIds = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.UserIds = params.get("UserIds")


class RemoveUserResponse(AbstractModel):
    """RemoveUser返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RoomState(AbstractModel):
    """房間訊息清單

    """

    def __init__(self):
        """
        :param CommId: 通話ID（唯一标識一次通話）
        :type CommId: str
        :param RoomString: 房間号
        :type RoomString: str
        :param CreateTime: 房間創建時間
        :type CreateTime: int
        :param DestroyTime: 房間銷毀時間
        :type DestroyTime: int
        :param IsFinished: 房間是否已經結束
        :type IsFinished: bool
        :param UserId: 房間創建者Id
        :type UserId: str
        """
        self.CommId = None
        self.RoomString = None
        self.CreateTime = None
        self.DestroyTime = None
        self.IsFinished = None
        self.UserId = None


    def _deserialize(self, params):
        self.CommId = params.get("CommId")
        self.RoomString = params.get("RoomString")
        self.CreateTime = params.get("CreateTime")
        self.DestroyTime = params.get("DestroyTime")
        self.IsFinished = params.get("IsFinished")
        self.UserId = params.get("UserId")


class TimeValue(AbstractModel):
    """返回的質量數據，時間:值

    """

    def __init__(self):
        """
        :param Time: 時間
        :type Time: int
        :param Value: 當前時間取值
        :type Value: float
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")


class UserInformation(AbstractModel):
    """用戶訊息，包括用戶進房時間，退房時間等

    """

    def __init__(self):
        """
        :param RoomStr: 房間号
        :type RoomStr: str
        :param UserId: 用戶Id
        :type UserId: str
        :param JoinTs: 用戶進房事件
        :type JoinTs: int
        :param LeaveTs: 用戶退房時間
        :type LeaveTs: int
        :param DeviceType: 終端類型
        :type DeviceType: str
        :param SdkVersion: Sdk版本号
        :type SdkVersion: str
        :param ClientIp: 用戶端IP網址
        :type ClientIp: str
        """
        self.RoomStr = None
        self.UserId = None
        self.JoinTs = None
        self.LeaveTs = None
        self.DeviceType = None
        self.SdkVersion = None
        self.ClientIp = None


    def _deserialize(self, params):
        self.RoomStr = params.get("RoomStr")
        self.UserId = params.get("UserId")
        self.JoinTs = params.get("JoinTs")
        self.LeaveTs = params.get("LeaveTs")
        self.DeviceType = params.get("DeviceType")
        self.SdkVersion = params.get("SdkVersion")
        self.ClientIp = params.get("ClientIp")