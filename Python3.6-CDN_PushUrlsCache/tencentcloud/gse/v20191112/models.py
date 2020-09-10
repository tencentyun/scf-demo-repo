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


class CreateGameServerSessionRequest(AbstractModel):
    """CreateGameServerSession請求參數結構體

    """

    def __init__(self):
        """
        :param MaximumPlayerSessionCount: 最大玩家數量
        :type MaximumPlayerSessionCount: int
        :param AliasId: 别名ID
        :type AliasId: str
        :param CreatorId: 創建者ID
        :type CreatorId: str
        :param FleetId: 艦隊ID
        :type FleetId: str
        :param GameProperties: 遊戲屬性
        :type GameProperties: list of GameProperty
        :param GameServerSessionData: 遊戲服務器會話屬性詳情
        :type GameServerSessionData: str
        :param GameServerSessionId: 遊戲服務器會話自定義ID
        :type GameServerSessionId: str
        :param IdempotencyToken: 幂等token
        :type IdempotencyToken: str
        :param Name: 遊戲服務器會話名稱
        :type Name: str
        """
        self.MaximumPlayerSessionCount = None
        self.AliasId = None
        self.CreatorId = None
        self.FleetId = None
        self.GameProperties = None
        self.GameServerSessionData = None
        self.GameServerSessionId = None
        self.IdempotencyToken = None
        self.Name = None


    def _deserialize(self, params):
        self.MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self.AliasId = params.get("AliasId")
        self.CreatorId = params.get("CreatorId")
        self.FleetId = params.get("FleetId")
        if params.get("GameProperties") is not None:
            self.GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self.GameProperties.append(obj)
        self.GameServerSessionData = params.get("GameServerSessionData")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.IdempotencyToken = params.get("IdempotencyToken")
        self.Name = params.get("Name")


class CreateGameServerSessionResponse(AbstractModel):
    """CreateGameServerSession返回參數結構體

    """

    def __init__(self):
        """
        :param GameServerSession: 遊戲服務器會話
注意：此欄位可能返回 null，表示取不到有效值。
        :type GameServerSession: :class:`taifucloudcloud.gse.v20191112.models.GameServerSession`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.GameServerSession = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSession") is not None:
            self.GameServerSession = GameServerSession()
            self.GameServerSession._deserialize(params.get("GameServerSession"))
        self.RequestId = params.get("RequestId")


class Credentials(AbstractModel):
    """訪問實例所需要的憑據

    """

    def __init__(self):
        """
        :param Secret: ssh私鑰
        :type Secret: str
        :param UserName: 用戶名
        :type UserName: str
        """
        self.Secret = None
        self.UserName = None


    def _deserialize(self, params):
        self.Secret = params.get("Secret")
        self.UserName = params.get("UserName")


class DescribeGameServerSessionDetailsRequest(AbstractModel):
    """DescribeGameServerSessionDetails請求參數結構體

    """

    def __init__(self):
        """
        :param AliasId: 别名ID
        :type AliasId: str
        :param FleetId: 艦隊ID
        :type FleetId: str
        :param GameServerSessionId: 遊戲服務器會話ID
        :type GameServerSessionId: str
        :param Limit: 單次查詢記錄數上限
        :type Limit: int
        :param NextToken: 頁偏移，用于查詢下一頁
        :type NextToken: str
        :param StatusFilter: 遊戲服務器會話狀态(ACTIVE,ACTIVATING,TERMINATED,TERMINATING,ERROR)
        :type StatusFilter: str
        """
        self.AliasId = None
        self.FleetId = None
        self.GameServerSessionId = None
        self.Limit = None
        self.NextToken = None
        self.StatusFilter = None


    def _deserialize(self, params):
        self.AliasId = params.get("AliasId")
        self.FleetId = params.get("FleetId")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.Limit = params.get("Limit")
        self.NextToken = params.get("NextToken")
        self.StatusFilter = params.get("StatusFilter")


class DescribeGameServerSessionDetailsResponse(AbstractModel):
    """DescribeGameServerSessionDetails返回參數結構體

    """

    def __init__(self):
        """
        :param GameServerSessionDetails: 遊戲服務器會話詳情清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type GameServerSessionDetails: list of GameServerSessionDetail
        :param NextToken: 頁偏移，用于查詢下一頁
注意：此欄位可能返回 null，表示取不到有效值。
        :type NextToken: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.GameServerSessionDetails = None
        self.NextToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessionDetails") is not None:
            self.GameServerSessionDetails = []
            for item in params.get("GameServerSessionDetails"):
                obj = GameServerSessionDetail()
                obj._deserialize(item)
                self.GameServerSessionDetails.append(obj)
        self.NextToken = params.get("NextToken")
        self.RequestId = params.get("RequestId")


class DescribeGameServerSessionPlacementRequest(AbstractModel):
    """DescribeGameServerSessionPlacement請求參數結構體

    """

    def __init__(self):
        """
        :param PlacementId: 遊戲服務器會話放置的唯一标識符
        :type PlacementId: str
        """
        self.PlacementId = None


    def _deserialize(self, params):
        self.PlacementId = params.get("PlacementId")


class DescribeGameServerSessionPlacementResponse(AbstractModel):
    """DescribeGameServerSessionPlacement返回參數結構體

    """

    def __init__(self):
        """
        :param GameServerSessionPlacement: 遊戲服務器會話放置
        :type GameServerSessionPlacement: :class:`taifucloudcloud.gse.v20191112.models.GameServerSessionPlacement`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.GameServerSessionPlacement = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessionPlacement") is not None:
            self.GameServerSessionPlacement = GameServerSessionPlacement()
            self.GameServerSessionPlacement._deserialize(params.get("GameServerSessionPlacement"))
        self.RequestId = params.get("RequestId")


class DescribeGameServerSessionsRequest(AbstractModel):
    """DescribeGameServerSessions請求參數結構體

    """

    def __init__(self):
        """
        :param AliasId: 别名ID
        :type AliasId: str
        :param FleetId: 艦隊ID
        :type FleetId: str
        :param GameServerSessionId: 遊戲服務器會話ID
        :type GameServerSessionId: str
        :param Limit: 單次查詢記錄數上限
        :type Limit: int
        :param NextToken: 頁偏移，用于查詢下一頁
        :type NextToken: str
        :param StatusFilter: 遊戲服務器會話狀态
        :type StatusFilter: str
        """
        self.AliasId = None
        self.FleetId = None
        self.GameServerSessionId = None
        self.Limit = None
        self.NextToken = None
        self.StatusFilter = None


    def _deserialize(self, params):
        self.AliasId = params.get("AliasId")
        self.FleetId = params.get("FleetId")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.Limit = params.get("Limit")
        self.NextToken = params.get("NextToken")
        self.StatusFilter = params.get("StatusFilter")


class DescribeGameServerSessionsResponse(AbstractModel):
    """DescribeGameServerSessions返回參數結構體

    """

    def __init__(self):
        """
        :param GameServerSessions: 遊戲服務器會話清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type GameServerSessions: list of GameServerSession
        :param NextToken: 頁便宜，用于查詢下一頁
注意：此欄位可能返回 null，表示取不到有效值。
        :type NextToken: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.GameServerSessions = None
        self.NextToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessions") is not None:
            self.GameServerSessions = []
            for item in params.get("GameServerSessions"):
                obj = GameServerSession()
                obj._deserialize(item)
                self.GameServerSessions.append(obj)
        self.NextToken = params.get("NextToken")
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances請求參數結構體

    """

    def __init__(self):
        """
        :param FleetId: 服務佈署ID
        :type FleetId: str
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param Offset: 結果返回最大數量
        :type Offset: int
        :param Limit: 返回結果偏移
        :type Limit: int
        """
        self.FleetId = None
        self.InstanceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回參數結構體

    """

    def __init__(self):
        """
        :param Instances: 實例訊息清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Instances: list of Instance
        :param TotalCount: 結果返回最大數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Instances = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = Instance()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribePlayerSessionsRequest(AbstractModel):
    """DescribePlayerSessions請求參數結構體

    """

    def __init__(self):
        """
        :param GameServerSessionId: 遊戲服務器會話ID
        :type GameServerSessionId: str
        :param Limit: 單次查詢記錄數上限
        :type Limit: int
        :param NextToken: 頁偏移，用于查詢下一頁
        :type NextToken: str
        :param PlayerId: 玩家ID
        :type PlayerId: str
        :param PlayerSessionId: 玩家會話ID
        :type PlayerSessionId: str
        :param PlayerSessionStatusFilter: 玩家會話狀态（RESERVED,ACTIVE,COMPLETED,TIMEDOUT）
        :type PlayerSessionStatusFilter: str
        """
        self.GameServerSessionId = None
        self.Limit = None
        self.NextToken = None
        self.PlayerId = None
        self.PlayerSessionId = None
        self.PlayerSessionStatusFilter = None


    def _deserialize(self, params):
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.Limit = params.get("Limit")
        self.NextToken = params.get("NextToken")
        self.PlayerId = params.get("PlayerId")
        self.PlayerSessionId = params.get("PlayerSessionId")
        self.PlayerSessionStatusFilter = params.get("PlayerSessionStatusFilter")


class DescribePlayerSessionsResponse(AbstractModel):
    """DescribePlayerSessions返回參數結構體

    """

    def __init__(self):
        """
        :param PlayerSessions: 玩家會話清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type PlayerSessions: list of PlayerSession
        :param NextToken: 頁偏移
注意：此欄位可能返回 null，表示取不到有效值。
        :type NextToken: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PlayerSessions = None
        self.NextToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlayerSessions") is not None:
            self.PlayerSessions = []
            for item in params.get("PlayerSessions"):
                obj = PlayerSession()
                obj._deserialize(item)
                self.PlayerSessions.append(obj)
        self.NextToken = params.get("NextToken")
        self.RequestId = params.get("RequestId")


class DesiredPlayerSession(AbstractModel):
    """玩家遊戲會話訊息

    """

    def __init__(self):
        """
        :param PlayerId: 與玩家會話關聯的唯一玩家标識
        :type PlayerId: str
        :param PlayerData: 開發人員定義的玩家數據
        :type PlayerData: str
        """
        self.PlayerId = None
        self.PlayerData = None


    def _deserialize(self, params):
        self.PlayerId = params.get("PlayerId")
        self.PlayerData = params.get("PlayerData")


class GameProperty(AbstractModel):
    """遊戲屬性詳情

    """

    def __init__(self):
        """
        :param Key: 屬性名稱
        :type Key: str
        :param Value: 屬性值
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class GameServerSession(AbstractModel):
    """遊戲會話詳情

    """

    def __init__(self):
        """
        :param CreationTime: 遊戲服務器會話創建時間
        :type CreationTime: str
        :param CreatorId: 創建者ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreatorId: str
        :param CurrentPlayerSessionCount: 當前玩家數量
        :type CurrentPlayerSessionCount: int
        :param DnsName: CVM的DNS标識符
注意：此欄位可能返回 null，表示取不到有效值。
        :type DnsName: str
        :param FleetId: 艦隊ID
        :type FleetId: str
        :param GameProperties: 遊戲屬性
注意：此欄位可能返回 null，表示取不到有效值。
        :type GameProperties: list of GameProperty
        :param GameServerSessionData: 遊戲服務器會話屬性詳情
注意：此欄位可能返回 null，表示取不到有效值。
        :type GameServerSessionData: str
        :param GameServerSessionId: 遊戲服務器會話ID
        :type GameServerSessionId: str
        :param IpAddress: CVM IP網址
        :type IpAddress: str
        :param MatchmakerData: 對戰程式詳情
注意：此欄位可能返回 null，表示取不到有效值。
        :type MatchmakerData: str
        :param MaximumPlayerSessionCount: 最大玩家數量
        :type MaximumPlayerSessionCount: int
        :param Name: 遊戲服務器會話名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type Name: str
        :param PlayerSessionCreationPolicy: 玩家會話創建策略
注意：此欄位可能返回 null，表示取不到有效值。
        :type PlayerSessionCreationPolicy: str
        :param Port: 端口号
        :type Port: int
        :param Status: 遊戲服務器會話狀态
        :type Status: str
        :param StatusReason: 遊戲服務器會話狀态附加訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type StatusReason: str
        :param TerminationTime: 終止的時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type TerminationTime: str
        :param InstanceType: 實例類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param CurrentCustomCount: 當前自定義數
注意：此欄位可能返回 null，表示取不到有效值。
        :type CurrentCustomCount: int
        :param MaxCustomCount: 最大自定義數
注意：此欄位可能返回 null，表示取不到有效值。
        :type MaxCustomCount: int
        :param Weight: 權重
注意：此欄位可能返回 null，表示取不到有效值。
        :type Weight: int
        :param AvailabilityStatus: 會話可用性狀态，是否被屏蔽
注意：此欄位可能返回 null，表示取不到有效值。
        :type AvailabilityStatus: str
        """
        self.CreationTime = None
        self.CreatorId = None
        self.CurrentPlayerSessionCount = None
        self.DnsName = None
        self.FleetId = None
        self.GameProperties = None
        self.GameServerSessionData = None
        self.GameServerSessionId = None
        self.IpAddress = None
        self.MatchmakerData = None
        self.MaximumPlayerSessionCount = None
        self.Name = None
        self.PlayerSessionCreationPolicy = None
        self.Port = None
        self.Status = None
        self.StatusReason = None
        self.TerminationTime = None
        self.InstanceType = None
        self.CurrentCustomCount = None
        self.MaxCustomCount = None
        self.Weight = None
        self.AvailabilityStatus = None


    def _deserialize(self, params):
        self.CreationTime = params.get("CreationTime")
        self.CreatorId = params.get("CreatorId")
        self.CurrentPlayerSessionCount = params.get("CurrentPlayerSessionCount")
        self.DnsName = params.get("DnsName")
        self.FleetId = params.get("FleetId")
        if params.get("GameProperties") is not None:
            self.GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self.GameProperties.append(obj)
        self.GameServerSessionData = params.get("GameServerSessionData")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.IpAddress = params.get("IpAddress")
        self.MatchmakerData = params.get("MatchmakerData")
        self.MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self.Name = params.get("Name")
        self.PlayerSessionCreationPolicy = params.get("PlayerSessionCreationPolicy")
        self.Port = params.get("Port")
        self.Status = params.get("Status")
        self.StatusReason = params.get("StatusReason")
        self.TerminationTime = params.get("TerminationTime")
        self.InstanceType = params.get("InstanceType")
        self.CurrentCustomCount = params.get("CurrentCustomCount")
        self.MaxCustomCount = params.get("MaxCustomCount")
        self.Weight = params.get("Weight")
        self.AvailabilityStatus = params.get("AvailabilityStatus")


class GameServerSessionDetail(AbstractModel):
    """遊戲服務器會話詳情（GameServerSessionDetail）

    """

    def __init__(self):
        """
        :param GameServerSession: 遊戲服務器會話
        :type GameServerSession: :class:`taifucloudcloud.gse.v20191112.models.GameServerSession`
        :param ProtectionPolicy: 保護策略，可選（NoProtection,FullProtection）
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProtectionPolicy: str
        """
        self.GameServerSession = None
        self.ProtectionPolicy = None


    def _deserialize(self, params):
        if params.get("GameServerSession") is not None:
            self.GameServerSession = GameServerSession()
            self.GameServerSession._deserialize(params.get("GameServerSession"))
        self.ProtectionPolicy = params.get("ProtectionPolicy")


class GameServerSessionPlacement(AbstractModel):
    """遊戲會話佈署對象

    """

    def __init__(self):
        """
        :param PlacementId: 部署Id
        :type PlacementId: str
        :param GameServerSessionQueueName: 服務佈署組名稱
        :type GameServerSessionQueueName: str
        :param PlayerLatencies: 玩家延遲
注意：此欄位可能返回 null，表示取不到有效值。
        :type PlayerLatencies: list of PlayerLatency
        :param Status: 服務佈署狀态
        :type Status: str
        :param DnsName: 分配給正在運作遊戲會話的實例的DNS标識符
注意：此欄位可能返回 null，表示取不到有效值。
        :type DnsName: str
        :param GameServerSessionId: 遊戲會話Id
注意：此欄位可能返回 null，表示取不到有效值。
        :type GameServerSessionId: str
        :param GameServerSessionName: 遊戲會話名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type GameServerSessionName: str
        :param GameServerSessionRegion: 服務佈署區域
注意：此欄位可能返回 null，表示取不到有效值。
        :type GameServerSessionRegion: str
        :param GameProperties: 遊戲屬性
注意：此欄位可能返回 null，表示取不到有效值。
        :type GameProperties: list of GameProperty
        :param MaximumPlayerSessionCount: 最大玩家數量
        :type MaximumPlayerSessionCount: int
        :param GameServerSessionData: 遊戲會話數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type GameServerSessionData: str
        :param IpAddress: 運作遊戲會話的實例的IP網址
注意：此欄位可能返回 null，表示取不到有效值。
        :type IpAddress: str
        :param Port: 運作遊戲會話的實例的端口号
注意：此欄位可能返回 null，表示取不到有效值。
        :type Port: int
        :param MatchmakerData: 遊戲比對數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type MatchmakerData: str
        :param PlacedPlayerSessions: 佈署的玩家遊戲數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type PlacedPlayerSessions: list of PlacedPlayerSession
        :param StartTime: 開始時間
        :type StartTime: str
        :param EndTime: 結束時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self.PlacementId = None
        self.GameServerSessionQueueName = None
        self.PlayerLatencies = None
        self.Status = None
        self.DnsName = None
        self.GameServerSessionId = None
        self.GameServerSessionName = None
        self.GameServerSessionRegion = None
        self.GameProperties = None
        self.MaximumPlayerSessionCount = None
        self.GameServerSessionData = None
        self.IpAddress = None
        self.Port = None
        self.MatchmakerData = None
        self.PlacedPlayerSessions = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.PlacementId = params.get("PlacementId")
        self.GameServerSessionQueueName = params.get("GameServerSessionQueueName")
        if params.get("PlayerLatencies") is not None:
            self.PlayerLatencies = []
            for item in params.get("PlayerLatencies"):
                obj = PlayerLatency()
                obj._deserialize(item)
                self.PlayerLatencies.append(obj)
        self.Status = params.get("Status")
        self.DnsName = params.get("DnsName")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.GameServerSessionName = params.get("GameServerSessionName")
        self.GameServerSessionRegion = params.get("GameServerSessionRegion")
        if params.get("GameProperties") is not None:
            self.GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self.GameProperties.append(obj)
        self.MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self.GameServerSessionData = params.get("GameServerSessionData")
        self.IpAddress = params.get("IpAddress")
        self.Port = params.get("Port")
        self.MatchmakerData = params.get("MatchmakerData")
        if params.get("PlacedPlayerSessions") is not None:
            self.PlacedPlayerSessions = []
            for item in params.get("PlacedPlayerSessions"):
                obj = PlacedPlayerSession()
                obj._deserialize(item)
                self.PlacedPlayerSessions.append(obj)
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class GetGameServerSessionLogUrlRequest(AbstractModel):
    """GetGameServerSessionLogUrl請求參數結構體

    """

    def __init__(self):
        """
        :param GameServerSessionId: 遊戲服務器會話ID
        :type GameServerSessionId: str
        """
        self.GameServerSessionId = None


    def _deserialize(self, params):
        self.GameServerSessionId = params.get("GameServerSessionId")


class GetGameServerSessionLogUrlResponse(AbstractModel):
    """GetGameServerSessionLogUrl返回參數結構體

    """

    def __init__(self):
        """
        :param PreSignedUrl: 日志下載URL
注意：此欄位可能返回 null，表示取不到有效值。
        :type PreSignedUrl: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PreSignedUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PreSignedUrl = params.get("PreSignedUrl")
        self.RequestId = params.get("RequestId")


class GetInstanceAccessRequest(AbstractModel):
    """GetInstanceAccess請求參數結構體

    """

    def __init__(self):
        """
        :param FleetId: 服務佈署Id
        :type FleetId: str
        :param InstanceId: 實例Id
        :type InstanceId: str
        """
        self.FleetId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.InstanceId = params.get("InstanceId")


class GetInstanceAccessResponse(AbstractModel):
    """GetInstanceAccess返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceAccess: 實例登入所需要的憑據
        :type InstanceAccess: :class:`taifucloudcloud.gse.v20191112.models.InstanceAccess`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceAccess = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceAccess") is not None:
            self.InstanceAccess = InstanceAccess()
            self.InstanceAccess._deserialize(params.get("InstanceAccess"))
        self.RequestId = params.get("RequestId")


class Instance(AbstractModel):
    """實例訊息

    """

    def __init__(self):
        """
        :param FleetId: 服務佈署ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type FleetId: str
        :param InstanceId: 實例ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param IpAddress: IP網址
注意：此欄位可能返回 null，表示取不到有效值。
        :type IpAddress: str
        :param DnsName: dns
注意：此欄位可能返回 null，表示取不到有效值。
        :type DnsName: str
        :param OperatingSystem: 作業系統
注意：此欄位可能返回 null，表示取不到有效值。
        :type OperatingSystem: str
        :param Status: 狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: str
        :param Type: 類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type Type: str
        :param CreateTime: 創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self.FleetId = None
        self.InstanceId = None
        self.IpAddress = None
        self.DnsName = None
        self.OperatingSystem = None
        self.Status = None
        self.Type = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.FleetId = params.get("FleetId")
        self.InstanceId = params.get("InstanceId")
        self.IpAddress = params.get("IpAddress")
        self.DnsName = params.get("DnsName")
        self.OperatingSystem = params.get("OperatingSystem")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.CreateTime = params.get("CreateTime")


class InstanceAccess(AbstractModel):
    """實例訪問憑證訊息

    """

    def __init__(self):
        """
        :param Credentials: 訪問實例所需要的憑據
        :type Credentials: :class:`taifucloudcloud.gse.v20191112.models.Credentials`
        :param FleetId: 服務佈署Id
        :type FleetId: str
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param IpAddress: 實例公網IP
        :type IpAddress: str
        :param OperatingSystem: 作業系統
        :type OperatingSystem: str
        """
        self.Credentials = None
        self.FleetId = None
        self.InstanceId = None
        self.IpAddress = None
        self.OperatingSystem = None


    def _deserialize(self, params):
        if params.get("Credentials") is not None:
            self.Credentials = Credentials()
            self.Credentials._deserialize(params.get("Credentials"))
        self.FleetId = params.get("FleetId")
        self.InstanceId = params.get("InstanceId")
        self.IpAddress = params.get("IpAddress")
        self.OperatingSystem = params.get("OperatingSystem")


class JoinGameServerSessionRequest(AbstractModel):
    """JoinGameServerSession請求參數結構體

    """

    def __init__(self):
        """
        :param GameServerSessionId: 遊戲服務器會話ID
        :type GameServerSessionId: str
        :param PlayerId: 玩家ID
        :type PlayerId: str
        :param PlayerData: 玩家自定義訊息
        :type PlayerData: str
        """
        self.GameServerSessionId = None
        self.PlayerId = None
        self.PlayerData = None


    def _deserialize(self, params):
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.PlayerId = params.get("PlayerId")
        self.PlayerData = params.get("PlayerData")


class JoinGameServerSessionResponse(AbstractModel):
    """JoinGameServerSession返回參數結構體

    """

    def __init__(self):
        """
        :param PlayerSession: 玩家會話
注意：此欄位可能返回 null，表示取不到有效值。
        :type PlayerSession: :class:`taifucloudcloud.gse.v20191112.models.PlayerSession`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PlayerSession = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlayerSession") is not None:
            self.PlayerSession = PlayerSession()
            self.PlayerSession._deserialize(params.get("PlayerSession"))
        self.RequestId = params.get("RequestId")


class PlacedPlayerSession(AbstractModel):
    """佈署的玩家遊戲會話

    """

    def __init__(self):
        """
        :param PlayerId: 玩家Id
        :type PlayerId: str
        :param PlayerSessionId: 玩家會話Id
        :type PlayerSessionId: str
        """
        self.PlayerId = None
        self.PlayerSessionId = None


    def _deserialize(self, params):
        self.PlayerId = params.get("PlayerId")
        self.PlayerSessionId = params.get("PlayerSessionId")


class PlayerLatency(AbstractModel):
    """玩家延遲訊息

    """

    def __init__(self):
        """
        :param PlayerId: 玩家Id
注意：此欄位可能返回 null，表示取不到有效值。
        :type PlayerId: str
        :param RegionIdentifier: 延遲對應的區域名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type RegionIdentifier: str
        :param LatencyInMilliseconds: 毫秒級延遲
        :type LatencyInMilliseconds: int
        """
        self.PlayerId = None
        self.RegionIdentifier = None
        self.LatencyInMilliseconds = None


    def _deserialize(self, params):
        self.PlayerId = params.get("PlayerId")
        self.RegionIdentifier = params.get("RegionIdentifier")
        self.LatencyInMilliseconds = params.get("LatencyInMilliseconds")


class PlayerSession(AbstractModel):
    """玩家會話詳情

    """

    def __init__(self):
        """
        :param CreationTime: 玩家會話創建時間
        :type CreationTime: str
        :param DnsName: 遊戲服務器會話運作的DNS标識
注意：此欄位可能返回 null，表示取不到有效值。
        :type DnsName: str
        :param FleetId: 艦隊ID
        :type FleetId: str
        :param GameServerSessionId: 遊戲服務器會話ID
        :type GameServerSessionId: str
        :param IpAddress: 遊戲服務器會話運作的CVM網址
        :type IpAddress: str
        :param PlayerData: 玩家相關訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type PlayerData: str
        :param PlayerId: 玩家ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type PlayerId: str
        :param PlayerSessionId: 玩家會話ID
        :type PlayerSessionId: str
        :param Port: 端口号
        :type Port: int
        :param Status: 玩家會話的狀态
        :type Status: str
        :param TerminationTime: 玩家會話終止時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type TerminationTime: str
        """
        self.CreationTime = None
        self.DnsName = None
        self.FleetId = None
        self.GameServerSessionId = None
        self.IpAddress = None
        self.PlayerData = None
        self.PlayerId = None
        self.PlayerSessionId = None
        self.Port = None
        self.Status = None
        self.TerminationTime = None


    def _deserialize(self, params):
        self.CreationTime = params.get("CreationTime")
        self.DnsName = params.get("DnsName")
        self.FleetId = params.get("FleetId")
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.IpAddress = params.get("IpAddress")
        self.PlayerData = params.get("PlayerData")
        self.PlayerId = params.get("PlayerId")
        self.PlayerSessionId = params.get("PlayerSessionId")
        self.Port = params.get("Port")
        self.Status = params.get("Status")
        self.TerminationTime = params.get("TerminationTime")


class SearchGameServerSessionsRequest(AbstractModel):
    """SearchGameServerSessions請求參數結構體

    """

    def __init__(self):
        """
        :param AliasId: 别名ID
        :type AliasId: str
        :param FleetId: 艦隊ID
        :type FleetId: str
        :param Limit: 單次查詢記錄數上限
        :type Limit: int
        :param NextToken: 頁偏移，用于查詢下一頁
        :type NextToken: str
        :param FilterExpression: 搜索條件表達式，支援如下變量
gameServerSessionName 遊戲會話名稱 String
gameServerSessionId 遊戲會話ID String
maximumSessions 最大的玩家會話數 Number
creationTimeMillis 創建時間，單位：毫秒 Number
playerSessionCount 當前玩家會話數 Number
hasAvailablePlayerSessions 是否有可用玩家數 String 取值true或false
gameServerSessionProperties 遊戲會話屬性 String

表達式String類型 等于=，不等于<>判斷
表示Number類型支援 =,<>,>,>=,<,<=
        :type FilterExpression: str
        :param SortExpression: 排序條件關鍵字
支援排序欄位
gameServerSessionName 遊戲會話名稱 String
gameServerSessionId 遊戲會話ID String
maximumSessions 最大的玩家會話數 Number
creationTimeMillis 創建時間，單位：毫秒 Number
playerSessionCount 當前玩家會話數 Number
        :type SortExpression: str
        """
        self.AliasId = None
        self.FleetId = None
        self.Limit = None
        self.NextToken = None
        self.FilterExpression = None
        self.SortExpression = None


    def _deserialize(self, params):
        self.AliasId = params.get("AliasId")
        self.FleetId = params.get("FleetId")
        self.Limit = params.get("Limit")
        self.NextToken = params.get("NextToken")
        self.FilterExpression = params.get("FilterExpression")
        self.SortExpression = params.get("SortExpression")


class SearchGameServerSessionsResponse(AbstractModel):
    """SearchGameServerSessions返回參數結構體

    """

    def __init__(self):
        """
        :param GameServerSessions: 遊戲服務器會話清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type GameServerSessions: list of GameServerSession
        :param NextToken: 頁偏移，用于查詢下一頁
注意：此欄位可能返回 null，表示取不到有效值。
        :type NextToken: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.GameServerSessions = None
        self.NextToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessions") is not None:
            self.GameServerSessions = []
            for item in params.get("GameServerSessions"):
                obj = GameServerSession()
                obj._deserialize(item)
                self.GameServerSessions.append(obj)
        self.NextToken = params.get("NextToken")
        self.RequestId = params.get("RequestId")


class StartGameServerSessionPlacementRequest(AbstractModel):
    """StartGameServerSessionPlacement請求參數結構體

    """

    def __init__(self):
        """
        :param PlacementId: 開始佈署遊戲服務器會話的唯一标識符
        :type PlacementId: str
        :param GameServerSessionQueueName: 遊戲服務器會話隊列名稱
        :type GameServerSessionQueueName: str
        :param MaximumPlayerSessionCount: 遊戲服務器允許同時連接到遊戲會話的最大玩家數量
        :type MaximumPlayerSessionCount: int
        :param DesiredPlayerSessions: 玩家遊戲會話訊息
        :type DesiredPlayerSessions: list of DesiredPlayerSession
        :param GameProperties: 玩家遊戲會話屬性
        :type GameProperties: list of GameProperty
        :param GameServerSessionData: 遊戲服務器會話數據
        :type GameServerSessionData: str
        :param GameServerSessionName: 遊戲服務器會話名稱
        :type GameServerSessionName: str
        :param PlayerLatencies: 玩家延遲
        :type PlayerLatencies: list of PlayerLatency
        """
        self.PlacementId = None
        self.GameServerSessionQueueName = None
        self.MaximumPlayerSessionCount = None
        self.DesiredPlayerSessions = None
        self.GameProperties = None
        self.GameServerSessionData = None
        self.GameServerSessionName = None
        self.PlayerLatencies = None


    def _deserialize(self, params):
        self.PlacementId = params.get("PlacementId")
        self.GameServerSessionQueueName = params.get("GameServerSessionQueueName")
        self.MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        if params.get("DesiredPlayerSessions") is not None:
            self.DesiredPlayerSessions = []
            for item in params.get("DesiredPlayerSessions"):
                obj = DesiredPlayerSession()
                obj._deserialize(item)
                self.DesiredPlayerSessions.append(obj)
        if params.get("GameProperties") is not None:
            self.GameProperties = []
            for item in params.get("GameProperties"):
                obj = GameProperty()
                obj._deserialize(item)
                self.GameProperties.append(obj)
        self.GameServerSessionData = params.get("GameServerSessionData")
        self.GameServerSessionName = params.get("GameServerSessionName")
        if params.get("PlayerLatencies") is not None:
            self.PlayerLatencies = []
            for item in params.get("PlayerLatencies"):
                obj = PlayerLatency()
                obj._deserialize(item)
                self.PlayerLatencies.append(obj)


class StartGameServerSessionPlacementResponse(AbstractModel):
    """StartGameServerSessionPlacement返回參數結構體

    """

    def __init__(self):
        """
        :param GameServerSessionPlacement: 遊戲服務器會話放置
        :type GameServerSessionPlacement: :class:`taifucloudcloud.gse.v20191112.models.GameServerSessionPlacement`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.GameServerSessionPlacement = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessionPlacement") is not None:
            self.GameServerSessionPlacement = GameServerSessionPlacement()
            self.GameServerSessionPlacement._deserialize(params.get("GameServerSessionPlacement"))
        self.RequestId = params.get("RequestId")


class StopGameServerSessionPlacementRequest(AbstractModel):
    """StopGameServerSessionPlacement請求參數結構體

    """

    def __init__(self):
        """
        :param PlacementId: 遊戲服務器會話放置的唯一标識符
        :type PlacementId: str
        """
        self.PlacementId = None


    def _deserialize(self, params):
        self.PlacementId = params.get("PlacementId")


class StopGameServerSessionPlacementResponse(AbstractModel):
    """StopGameServerSessionPlacement返回參數結構體

    """

    def __init__(self):
        """
        :param GameServerSessionPlacement: 遊戲服務器會話放置
        :type GameServerSessionPlacement: :class:`taifucloudcloud.gse.v20191112.models.GameServerSessionPlacement`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.GameServerSessionPlacement = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSessionPlacement") is not None:
            self.GameServerSessionPlacement = GameServerSessionPlacement()
            self.GameServerSessionPlacement._deserialize(params.get("GameServerSessionPlacement"))
        self.RequestId = params.get("RequestId")


class UpdateGameServerSessionRequest(AbstractModel):
    """UpdateGameServerSession請求參數結構體

    """

    def __init__(self):
        """
        :param GameServerSessionId: 遊戲服務器會話ID
        :type GameServerSessionId: str
        :param MaximumPlayerSessionCount: 最大玩家數量
        :type MaximumPlayerSessionCount: int
        :param Name: 遊戲服務器會話名稱
        :type Name: str
        :param PlayerSessionCreationPolicy: 玩家會話創建策略（ACCEPT_ALL,DENY_ALL）
        :type PlayerSessionCreationPolicy: str
        :param ProtectionPolicy: 保護策略(NoProtection,TimeLimitProtection,FullProtection)
        :type ProtectionPolicy: str
        """
        self.GameServerSessionId = None
        self.MaximumPlayerSessionCount = None
        self.Name = None
        self.PlayerSessionCreationPolicy = None
        self.ProtectionPolicy = None


    def _deserialize(self, params):
        self.GameServerSessionId = params.get("GameServerSessionId")
        self.MaximumPlayerSessionCount = params.get("MaximumPlayerSessionCount")
        self.Name = params.get("Name")
        self.PlayerSessionCreationPolicy = params.get("PlayerSessionCreationPolicy")
        self.ProtectionPolicy = params.get("ProtectionPolicy")


class UpdateGameServerSessionResponse(AbstractModel):
    """UpdateGameServerSession返回參數結構體

    """

    def __init__(self):
        """
        :param GameServerSession: 更新後的遊戲會話
        :type GameServerSession: :class:`taifucloudcloud.gse.v20191112.models.GameServerSession`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.GameServerSession = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GameServerSession") is not None:
            self.GameServerSession = GameServerSession()
            self.GameServerSession._deserialize(params.get("GameServerSession"))
        self.RequestId = params.get("RequestId")